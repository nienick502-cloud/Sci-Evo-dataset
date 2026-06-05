"""
Build an audited copy of the Research layer without modifying originals.

Input:
  dataset/final/Research/*.json
  audit/research_layer/research_audit_summary.csv

Output:
  dataset/final/Research_audited/
    P0_reject_replace/
    P1_must_fix/
    P2_review_needed/
    P3_polish/
    PASS/
    AUDIT_README.md
    manifest.csv

Only deterministic, low-risk fixes are applied to the copied JSON files:
  - known invalid action labels are mapped to schema-valid action labels
  - string "null" error_tag is converted to JSON null
  - valid=false steps missing error_reason get a conservative audit note
  - metric.unit fields that contain conditions are split into unit + interpretation

The original dataset/final/Research directory is never modified.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from pathlib import Path
from typing import Any


RISK_DIRS = {
    "P0": "P0_reject_replace",
    "P1": "P1_must_fix",
    "P2": "P2_review_needed",
    "P3": "P3_polish",
    "PASS": "PASS",
}

ACTION_FIXES = {
    "model_prediction": "numerical_computation",
    "feature_engineering": "model_building",
    "physical_argument": "verification",
}

MISSING_ERROR_REASON_FIXES = {
    ("NPP_0117", 3): "原样本将该步骤标记为 valid=false 但缺少 error_reason。该步骤延续了预测路径中 Yukawa 型势和简化径向积分的假设，未体现论文实际强调的神经网络变分波函数、势模型选择及氘核张量力/s-d 波耦合等关键物理结构，因此保留为错误步骤并补全原因。",
    ("NPP_0117", 5): "原样本将该步骤标记为 valid=false 但缺少 error_reason。该验证声称简化预测波函数与精确解几乎一致，但其前提模型未包含论文实际处理所需的张量力和 d 波成分，验证对象与论文模型不一致，因此该结论不可靠。",
    ("NPP_0117", 6): "原样本将该步骤标记为 valid=false 但缺少 error_reason。该步骤将氘核两体波函数问题处理为 mean_field_density_calculation 路径，容易混淆少体束缚态波函数与平均场密度计算；与论文的机器学习氘核波函数求解主体不一致。",
    ("NPP_0117", 7): "原样本将该步骤标记为 valid=false 但缺少 error_reason。该半径积分建立在前一步不一致的密度计算路径上，且把数值吻合当作模型正确性的验证，忽略了论文所需的势模型和波函数分量检查，因此保留为错误步骤。",
    ("NPP_0179", 3): "原样本将该步骤标记为 valid=false 但缺少 error_reason。该步骤引入 GCM/RGM 结构波函数和谱因子作为反应截面输入，但样本来源论文的主体是低能相互作用到核截面的散射/反应框架；该结构模型路径与论文方法主体不一致，因此保留为错误步骤。",
}

MISSING_ERROR_TAG_FIXES = {
    ("NPP_0117", 3): "incorrect_derivation",
    ("NPP_0117", 5): "wrong_physical_interpretation",
    ("NPP_0117", 6): "wrong_approximation",
    ("NPP_0117", 7): "incorrect_derivation",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def save_json(path: Path, data: dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def read_summary(path: Path) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return {row["id"]: row for row in csv.DictReader(f)}


def split_metric_unit(metric: dict[str, Any]) -> bool:
    unit = str(metric.get("unit") or "")
    if not unit:
        return False
    looks_like_condition = len(unit) > 30 or any(token in unit for token in ["使用", "基于", "Z=", "A=", "测试集", "condition"])
    if not looks_like_condition:
        return False
    interp = str(metric.get("interpretation") or "")
    condition = unit
    metric["unit"] = "condition"
    metric["interpretation"] = f"{interp}; {condition}" if interp else condition
    return True


def fix_copy(data: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    sample_id = str(data.get("id") or data.get("meta", {}).get("id") or "")
    changes: list[str] = []

    for step in data.get("02_agent_trajectory", []) or []:
        step_index = step.get("step_index")
        action = step.get("action")
        if action in ACTION_FIXES:
            step["action"] = ACTION_FIXES[action]
            changes.append(f"第 {step_index} 步：action 由 {action!r} 规范为 {step['action']!r}")

        if step.get("error_tag") == "null":
            step["error_tag"] = None
            changes.append(f"第 {step_index} 步：error_tag 字符串 'null' 规范为 JSON null")

        if step.get("valid") is False and not step.get("error_tag"):
            tag = MISSING_ERROR_TAG_FIXES.get((sample_id, step_index), "incorrect_derivation")
            step["error_tag"] = tag
            changes.append(f"第 {step_index} 步：补充缺失 error_tag 为 {tag!r}")

        if step.get("valid") is False and not step.get("error_reason"):
            reason = MISSING_ERROR_REASON_FIXES.get((sample_id, step_index))
            if reason is None:
                reason = "原样本将该步骤标记为 valid=false 但缺少 error_reason；本审核副本保留 invalid 判定，并补充该字段以满足 Research 层 schema 要求。具体物理原因由后续人工复核进一步细化。"
            step["error_reason"] = reason
            changes.append(f"第 {step_index} 步：补充缺失 error_reason")

    verification = data.get("03_success_verification") or {}
    metrics = verification.get("metrics") or {}
    if isinstance(metrics, dict):
        for name, metric in metrics.items():
            if isinstance(metric, dict) and split_metric_unit(metric):
                changes.append(f"metrics.{name}：将条件说明从 unit 移入 interpretation")

    return data, changes


def write_readme(out_dir: Path, counts: dict[str, int]) -> None:
    lines = [
        "# Research_audited",
        "",
        "本目录是 `dataset/final/Research` 的审核后副本，用于在不改动已发布原始数据的前提下保存分类和小修版本。",
        "",
        "## 分类目录",
        "",
        "- `P0_reject_replace/`：源论文主体错配或列入替换处置的样本。",
        "- `P1_must_fix/`：原始样本存在 schema 硬错误；本副本已做确定性小修，列入重点复核。",
        "- `P2_review_needed/`：内容或子领域匹配需要人工复核的样本。",
        "- `P3_polish/`：主体可用但有格式/文本清洗项的样本。",
        "- `PASS/`：当前审核规则未命中问题的样本。",
        "",
        "## 本副本应用的保守修正",
        "",
        "- 将少量非法 `action` 映射到 schema 允许的 action。",
        "- 将字符串形式的 `error_tag: \"null\"` 转为 JSON `null`。",
        "- 为 `valid=false` 且缺少 `error_reason` 的步骤补充审核说明。",
        "- 将明显写成条件说明的 `metrics.*.unit` 移入 `interpretation`，并把 `unit` 置为 `condition`。",
        "",
        "## 样本数",
        "",
    ]
    for risk, dirname in RISK_DIRS.items():
        lines.append(f"- `{dirname}`：{counts.get(risk, 0)}")
    lines.extend(
        [
            "",
            "完整审核证据见 `audit/research_layer/`。",
            "",
        ]
    )
    (out_dir / "AUDIT_README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build categorized audited Research copy.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root")
    parser.add_argument("--force", action="store_true", help="Overwrite existing output directory")
    args = parser.parse_args()

    root = args.root.resolve()
    source_dir = root / "dataset" / "final" / "Research"
    summary_path = root / "audit" / "research_layer" / "research_audit_summary.csv"
    out_dir = root / "dataset" / "final" / "Research_audited"

    if not source_dir.exists():
        raise FileNotFoundError(source_dir)
    if not summary_path.exists():
        raise FileNotFoundError(summary_path)
    if out_dir.exists():
        if not args.force:
            raise FileExistsError(f"{out_dir} already exists. Re-run with --force to overwrite.")

    summary = read_summary(summary_path)
    out_dir.mkdir(parents=True, exist_ok=True)
    for dirname in RISK_DIRS.values():
        (out_dir / dirname).mkdir(exist_ok=True)

    manifest_rows = []
    counts = {risk: 0 for risk in RISK_DIRS}
    for src in sorted(source_dir.glob("*.json")):
        sample_id = src.stem
        row = summary.get(sample_id)
        if row is None:
            raise KeyError(f"{sample_id} missing from audit summary")
        risk = row["risk_level"]
        dirname = RISK_DIRS[risk]
        data = load_json(src)
        fixed, changes = fix_copy(data)
        dst = out_dir / dirname / src.name
        save_json(dst, fixed)
        counts[risk] += 1
        manifest_rows.append(
            {
                "id": sample_id,
                "risk_level": risk,
                "risk_dir": dirname,
                "source_path": str(src),
                "audited_path": str(dst),
                "issue_count": row.get("issue_count", ""),
                "changes_applied": " | ".join(changes),
            }
        )

    with (out_dir / "manifest.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "id",
                "risk_level",
                "risk_dir",
                "source_path",
                "audited_path",
                "issue_count",
                "changes_applied",
            ],
        )
        writer.writeheader()
        writer.writerows(manifest_rows)

    write_readme(out_dir, counts)
    print(f"[OK] Wrote audited Research copy to {out_dir}")
    for risk, dirname in RISK_DIRS.items():
        print(f"  {dirname}: {counts[risk]}")


if __name__ == "__main__":
    main()
