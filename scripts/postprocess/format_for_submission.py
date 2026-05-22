"""
format_for_submission.py - 阶段 10.5 后处理编排

将原始 _v2.json + Foundation 层数据转换为最终提交格式。
纯提取拼接，不调 LLM，不改原始文件，幂等。

三项操作：
  1. 轨迹顺序重排：prediction → decision_summary → paper_derivation
  2. 信息融合：paper_facts 内容注入轨迹步骤
  3. 格式微调：去 generation_config、清残留字段、补全 failure_points

Usage:
    python format_for_submission.py                  # 全量处理 239 条
    python format_for_submission.py --research-only  # 只处理 Research 层
    python format_for_submission.py --dry-run        # 只统计，不写文件
"""

import argparse
import copy
import json
import re
import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PAPERS_DIR = PROJECT_ROOT / "raw_dataset" / "papers"
FOUNDATION_DIR = PROJECT_ROOT / "dataset" / "foundation"
OUTPUT_DIR = PROJECT_ROOT / "dataset" / "final"


# ══════════════════════════════════════════════════════════════════════════════
# 操作 1：轨迹顺序重排
# ══════════════════════════════════════════════════════════════════════════════

def reorder_trajectory(trajectory: list[dict]) -> list[dict]:
    """重排轨迹：prediction → decision_summary → paper_derivation，重编号 step_index。"""
    prediction = [s for s in trajectory if s.get("phase") == "prediction"]
    decision_summary = [s for s in trajectory if s.get("phase") == "decision_summary"]
    paper_derivation = [s for s in trajectory if s.get("phase") == "paper_derivation"]

    merged = prediction + decision_summary + paper_derivation
    for i, step in enumerate(merged, start=1):
        step["step_index"] = i
    return merged


# ══════════════════════════════════════════════════════════════════════════════
# 操作 2：信息融合
# ══════════════════════════════════════════════════════════════════════════════

def _extract_symbols(latex_str: str) -> set[str]:
    """从 LaTeX 公式中提取变量名/物理量符号。"""
    symbols = set()
    # 提取单字母或下标变量：P, K, Q, V_l, T_{1/2}, E_v
    for m in re.finditer(r'([A-Za-z])(?:_\{?([A-Za-z0-9/]+)\}?)?', latex_str):
        base = m.group(1)
        sub = m.group(2) or ""
        symbols.add(base.lower())
        if sub:
            symbols.add(f"{base}_{sub}".lower())
    # 提取 LaTeX 命令中的物理量名：\rho, \mu, \hbar
    for m in re.finditer(r'\\([a-zA-Z]+)', latex_str):
        cmd = m.group(1)
        if cmd not in ("frac", "left", "right", "mathrm", "times", "exp", "sqrt",
                       "int", "sum", "prod", "pi", "cdot", "quad", "text"):
            symbols.add(cmd.lower())
    return symbols


def _step_symbols(step: dict) -> set[str]:
    """从步骤的 output_state keys 和 thought 中提取物理量关键词。"""
    symbols = set()
    # output_state keys
    for key in (step.get("output_state") or {}).keys():
        symbols.add(key.lower())
        # 拆分 snake_case
        for part in key.split("_"):
            if len(part) > 1:
                symbols.add(part.lower())
    # thought 中的物理量（简单提取）
    thought = step.get("thought", "")
    for m in re.finditer(r'([A-Z][a-z_]*(?:_[a-z]+)*)', thought):
        symbols.add(m.group(1).lower())
    return symbols


def fuse_formulas(paper_derivation: list[dict], key_formulas: list[dict]) -> None:
    """2a: 将 key_formulas 匹配注入 paper_derivation 步骤的 observation。"""
    if not key_formulas:
        return
    used_formulas = set()
    for step in paper_derivation:
        step_syms = _step_symbols(step)
        if not step_syms:
            continue
        for i, formula in enumerate(key_formulas):
            if i in used_formulas:
                continue
            content = formula.get("content", "")
            label = formula.get("label", "")
            formula_syms = _extract_symbols(content)
            # 至少 2 个符号交集才算匹配
            overlap = step_syms & formula_syms
            if len(overlap) >= 2:
                obs = step.get("observation", "")
                step["observation"] = f"{obs}\n[论文公式] {label}: {content}"
                used_formulas.add(i)
                break  # 每步最多注入一个公式


def fuse_methods_desc(paper_derivation: list[dict], methods: list[dict]) -> None:
    """2c: 首次出现的方法步骤注入 methods.desc。"""
    if not methods:
        return
    # 建立 method name → desc 映射（模糊匹配用小写）
    method_map = {}
    for m in methods:
        name = m.get("name", "")
        desc = m.get("desc", "")
        if name and desc:
            method_map[name.lower().replace(" ", "_")] = desc

    seen_tools = set()
    for step in paper_derivation:
        tool_name = step.get("tool", {}).get("name", "")
        if not tool_name or tool_name in seen_tools:
            continue
        seen_tools.add(tool_name)
        # 模糊匹配：子串包含 或 共享至少 2 个有意义的词根
        tool_lower = tool_name.lower()
        tool_parts = set(p for p in tool_lower.split("_") if len(p) > 2)
        for mname, desc in method_map.items():
            if mname in tool_lower or tool_lower in mname:
                obs = step.get("observation", "")
                step["observation"] = f"[方法说明] {desc}\n{obs}"
                break
            # 词根交集匹配
            mname_parts = set(p for p in mname.split("_") if len(p) > 2)
            if len(tool_parts & mname_parts) >= 2:
                obs = step.get("observation", "")
                step["observation"] = f"[方法说明] {desc}\n{obs}"
                break


def fuse_results_interpretation(paper: dict, key_results: list[dict]) -> None:
    """2b: 补全 metrics.interpretation。"""
    if not key_results:
        return
    metrics = paper.get("03_success_verification", {}).get("metrics", {})
    if not metrics:
        return
    for metric_key, metric_val in metrics.items():
        if not isinstance(metric_val, dict):
            continue
        interp = metric_val.get("interpretation", "")
        if interp and len(interp) >= 20:
            continue
        # 尝试从 key_results 找匹配
        metric_lower = metric_key.lower()
        for kr in key_results:
            qty = kr.get("quantity", "").lower()
            if metric_lower in qty or qty in metric_lower:
                condition = kr.get("condition", "")
                if condition:
                    metric_val["interpretation"] = (
                        f"{interp}; {condition}" if interp else condition
                    )
                break


def fuse_information(paper: dict) -> None:
    """操作 2：信息融合主入口。"""
    paper_facts = paper.get("paper_facts", {})
    if not paper_facts:
        return

    trajectory = paper.get("02_agent_trajectory", [])
    paper_derivation = [s for s in trajectory if s.get("phase") == "paper_derivation"]

    # 2a: formulas → observation
    fuse_formulas(paper_derivation, paper_facts.get("key_formulas", []))
    # 2c: methods.desc → observation
    fuse_methods_desc(paper_derivation, paper_facts.get("methods", []))
    # 2b: key_results → interpretation
    fuse_results_interpretation(paper, paper_facts.get("key_results", []))


# ══════════════════════════════════════════════════════════════════════════════
# 操作 3：格式微调
# ══════════════════════════════════════════════════════════════════════════════

def cleanup_fields(paper: dict) -> None:
    """操作 3：去除内部元数据、补全缺失字段。"""
    # 去除 generation_config
    meta = paper.get("meta", {})
    meta.pop("generation_config", None)

    # 清理 predicted_trajectory 残留
    paper.pop("predicted_trajectory", None)

    # failure_points 补全
    paper_facts = paper.get("paper_facts", {})
    if paper_facts and not paper_facts.get("failure_points"):
        trajectory = paper.get("02_agent_trajectory", [])
        error_steps = [
            s for s in trajectory
            if s.get("error_tag") and s["error_tag"] != "null"
        ]
        if error_steps:
            paper_facts["failure_points"] = [
                s.get("error_reason", f"步骤 {s.get('step_index')}: {s.get('error_tag')}")
                for s in error_steps
                if s.get("error_reason")
            ]

    # 确保 paper_derivation 步骤有 observation_source
    trajectory = paper.get("02_agent_trajectory", [])
    for step in trajectory:
        if step.get("phase") == "paper_derivation":
            if not step.get("observation_source"):
                step["observation_source"] = "paper"


# ══════════════════════════════════════════════════════════════════════════════
# 主流程
# ══════════════════════════════════════════════════════════════════════════════

def process_foundation(dst_dir: Path, dry_run: bool = False) -> int:
    """直接复制 Foundation 层文件到输出目录。"""
    count = 0
    for subdir in ("nuclear", "quantum"):
        src = FOUNDATION_DIR / subdir
        if not src.exists():
            continue
        for f in sorted(src.glob("*.json")):
            count += 1
            if not dry_run:
                shutil.copy2(f, dst_dir / f.name)
    return count


def process_single_research(filepath: Path) -> dict:
    """处理单篇 Research 层论文，返回处理后的 dict。"""
    with open(filepath, "r", encoding="utf-8") as f:
        paper = json.load(f)

    # 深拷贝避免修改原始数据
    paper = copy.deepcopy(paper)

    # 操作 1：轨迹重排
    trajectory = paper.get("02_agent_trajectory", [])
    paper["02_agent_trajectory"] = reorder_trajectory(trajectory)

    # 操作 2：信息融合
    fuse_information(paper)

    # 操作 3：格式微调
    cleanup_fields(paper)

    return paper


def process_research(dst_dir: Path, dry_run: bool = False) -> int:
    """处理全部 Research 层 _v2.json。"""
    count = 0
    for folder in sorted(PAPERS_DIR.iterdir()):
        if not folder.is_dir():
            continue
        for f in sorted(folder.glob("*_v2.json")):
            count += 1
            if not dry_run:
                paper = process_single_research(f)
                paper_id = paper.get("id", f.stem.replace("_v2", ""))
                out_path = dst_dir / f"{paper_id}.json"
                with open(out_path, "w", encoding="utf-8") as fh:
                    json.dump(paper, fh, ensure_ascii=False, indent=2)
    return count


def main():
    parser = argparse.ArgumentParser(description="Post-processing for submission")
    parser.add_argument("--research-only", action="store_true",
                        help="Only process Research layer")
    parser.add_argument("--dry-run", action="store_true",
                        help="Only count files, don't write")
    args = parser.parse_args()

    # 创建输出目录
    if not args.dry_run:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    foundation_count = 0
    if not args.research_only:
        foundation_count = process_foundation(OUTPUT_DIR, dry_run=args.dry_run)
        print(f"[OK] Foundation: {foundation_count} files"
              + (" (dry-run)" if args.dry_run else ""))

    research_count = process_research(OUTPUT_DIR, dry_run=args.dry_run)
    print(f"[OK] Research: {research_count} files"
          + (" (dry-run)" if args.dry_run else ""))

    total = foundation_count + research_count
    print(f"[OK] Total: {total} files -> {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
