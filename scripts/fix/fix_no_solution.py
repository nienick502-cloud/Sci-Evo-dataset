"""
fix_no_solution.py

修复 raw_dataset/no_solution/ 中的字段分配错误：
- 解答文本混入了 problem_text，solution_text 为空
- 检测解答标记，切分字段，写入 raw_dataset/quantum/
- 输出修复报告 raw_dataset/no_solution/fix_report.json
"""

import json
import re
import copy
import os
from pathlib import Path
from datetime import datetime

# ── 路径配置 ──────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent
NO_SOL_DIR = BASE_DIR / "raw_dataset" / "no_solution"
QUANTUM_DIR = BASE_DIR / "raw_dataset" / "quantum"
REPORT_PATH = NO_SOL_DIR / "fix_report.json"

# ── 解答标记正则（re.MULTILINE，匹配行首） ────────────────────────────────────
# 优先级：括号类 > 冒号类 > 证明行首 > 裸解
SOLUTION_MARKER_RE = re.compile(
    r'^('
    r'（证明）|（证）|\(证明\)|\(证\)'
    r'|【证明】|\[证明\]|【证】|\[证\]'
    r'|【解】|\[解\]'
    r'|解[：:]'
    r'|证[：:]'             # 证： 行首（不会匹配 证明：，因为证后跟明不是冒号）
    r'|证明'               # 证明 行首（格里菲斯风格：独占行/后跟空格/后跟冒号均可）
    r'|解(?![：:\n])'       # 裸 解 行首，不跟冒号/换行（如"解本题..."）
    r')',
    re.MULTILINE
)

# ── 多题拼接检测 ──────────────────────────────────────────────────────────────
MULTI_PROB_RE = re.compile(r'【\d+】')


def is_multi_problem(text: str) -> bool:
    return len(MULTI_PROB_RE.findall(text)) >= 2


def split_at_marker(problem_text: str):
    """
    在 problem_text 中找解答标记，切分为 (problem_part, solution_part)。
    标记本身保留在 solution_part 开头。
    遍历所有匹配，返回第一个能给出非空 problem_part 的切分。
    返回 None 表示未找到有效切分。
    """
    for m in SOLUTION_MARKER_RE.finditer(problem_text):
        split_pos = m.start()
        problem_part = problem_text[:split_pos].strip()
        solution_part = problem_text[split_pos:].strip()
        if problem_part:
            return problem_part, solution_part
    return None


def fix_entry(entry: dict, problem_part: str, solution_part: str) -> dict:
    fixed = copy.deepcopy(entry)
    fixed["raw_problem"]["problem_text"] = problem_part
    fixed["raw_problem"]["solution_text"] = solution_part
    fixed["meta"]["version"] = "0.2"
    return fixed


def process_all():
    files = sorted(f for f in NO_SOL_DIR.glob("*.json") if f.name != "fix_report.json")
    fixed_list = []
    unfixable_list = []
    skipped_list = []

    for fpath in files:
        with open(fpath, encoding="utf-8") as f:
            entry = json.load(f)

        fid = entry["id"]
        problem_text = entry["raw_problem"]["problem_text"]

        # 1. 多题拼接检测
        if is_multi_problem(problem_text):
            unfixable_list.append({
                "id": fid,
                "reason": "MULTI_PROBLEM",
                "detail": f"检测到 {len(MULTI_PROB_RE.findall(problem_text))} 个题号标记"
            })
            continue

        # 2. 尝试切分
        result = split_at_marker(problem_text)
        if result is None:
            # 判断是所有标记都给出空题目，还是根本没有标记
            has_any_marker = SOLUTION_MARKER_RE.search(problem_text) is not None
            reason = "EMPTY_PROBLEM_AFTER_SPLIT" if has_any_marker else "NO_MARKER_FOUND"
            unfixable_list.append({"id": fid, "reason": reason})
            continue

        problem_part, solution_part = result

        # 3. 检查目标文件是否已存在
        out_path = QUANTUM_DIR / fpath.name
        if out_path.exists():
            skipped_list.append({"id": fid, "reason": "COLLISION", "path": str(out_path)})
            continue

        # 4. 写入修复后的文件
        fixed = fix_entry(entry, problem_part, solution_part)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(fixed, f, ensure_ascii=False, indent=2)

        # 找到实际使用的标记（solution_part 开头的标记）
        m_used = SOLUTION_MARKER_RE.match(solution_part)
        fixed_list.append({
            "id": fid,
            "marker": m_used.group(0) if m_used else solution_part[:10],
            "problem_text_len": len(problem_part),
            "solution_text_len": len(solution_part),
        })

    # 5. 写报告
    report = {
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total": len(files),
            "fixed": len(fixed_list),
            "unfixable": len(unfixable_list),
            "skipped_collision": len(skipped_list),
        },
        "fixed": fixed_list,
        "unfixable": unfixable_list,
        "skipped": skipped_list,
    }
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"完成：fixed={len(fixed_list)}, unfixable={len(unfixable_list)}, skipped={len(skipped_list)}")
    print(f"报告：{REPORT_PATH}")


if __name__ == "__main__":
    process_all()
