"""
Research-layer audit for Physics-PreProc-QN.

Reads dataset/final/Research/*.json plus parsed/raw evidence and writes:
  audit/research_layer/research_audit_report.md
  audit/research_layer/research_audit_findings.jsonl
  audit/research_layer/research_audit_summary.csv
  audit/research_layer/p0_reject_candidates.txt
  audit/research_layer/p2_manual_review_queue.md

The audit is intentionally high-recall for P2 review items and conservative for
P0 reject items. It does not modify dataset files.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


VALID_PHASES = {"prediction", "decision_summary", "paper_derivation"}
VALID_ACTIONS = {
    "symbolic_derivation",
    "numerical_computation",
    "approximation",
    "verification",
    "rule_application",
    "model_building",
    "correction",
}
VALID_ERROR_TAGS = {
    None,
    "wrong_approximation",
    "missing_physical_effect",
    "incorrect_derivation",
    "wrong_parameter_choice",
    "over_simplification",
    "wrong_physical_interpretation",
}
REQUIRED_TOP_LEVEL = [
    "id",
    "meta",
    "01_initial_request",
    "02_agent_trajectory",
    "03_success_verification",
    "paper_methods",
    "paper_facts",
]

SEVERITY_RANK = {"P0": 0, "P1": 1, "P2": 2, "P3": 3, "PASS": 4}
SEVERITY_LABEL = {
    "P0": "删除或替换",
    "P1": "必须修复",
    "P2": "人工复核",
    "P3": "格式清理",
    "PASS": "通过",
}
ACTION_BY_SEVERITY = {
    "P0": "从 final 集合移除，或以同子领域核物理论文样本替换。",
    "P1": "发布前修复 schema/字段错误；必要时重新生成 metadata。",
    "P2": "复核证据，确定保留、修复或替换。",
    "P3": "批量清理格式和文本问题。",
}

NON_NUCLEAR_PATTERNS = [
    r"\bcloud(s)?\b",
    r"ground[- ]based cloud",
    r"meteorolog",
    r"climate change",
    r"weather",
    r"image classification",
    r"cloud image",
]

NUCLEAR_DOMAIN_PATTERNS = [
    r"\bnuclear\b",
    r"\bnuclei\b",
    r"\bnucleus\b",
    r"\bneutron\b",
    r"\bproton\b",
    r"\balpha\b",
    r"\\alpha",
    r"\bdecay\b",
    r"half[- ]?life",
    r"\bscattering\b",
    r"cross[- ]?section",
    r"\boptical model\b",
    r"\bshell\b",
    r"\bfission\b",
    r"\bdeuteron\b",
]

SUBDOMAIN_RULES = {
    "alpha_decay_wkb": {
        "must_any": [["alpha", "\\alpha"], ["decay", "half life", "half-life"], ["wkb", "tunnel", "penetrab"]],
        "review_if_fewer_hits": 2,
    },
    "alpha_decay_liquid_drop": {
        "must_any": [["alpha", "\\alpha"], ["decay", "half life", "half-life"], ["liquid", "drop", "gldm", "proximity"]],
        "review_if_fewer_hits": 2,
    },
    "alpha_decay_shell_model": {
        "must_any": [["alpha", "\\alpha"], ["decay", "half life", "half-life", "superheavy"], ["shell", "magic", "level-density", "mean-field"]],
        "review_if_fewer_hits": 2,
    },
    "alpha_decay_cluster_model": {
        "must_any": [["alpha", "\\alpha"], ["cluster", "preformation", "formation"], ["decay", "half life", "half-life", "surface"]],
        "review_if_fewer_hits": 2,
    },
    "alpha_decay_double_folding": {
        "must_any": [["alpha", "\\alpha"], ["folding", "ddm3y", "m3y"], ["decay", "potential", "barrier"]],
        "review_if_fewer_hits": 2,
    },
    "deep_learning_nuclear": {
        "must_any": [["nuclear", "nuclei", "neutron", "proton", "deuteron", "mass", "shell"], ["deep", "neural", "learning", "bayesian", "boosting", "ai"]],
        "review_if_fewer_hits": 2,
    },
    "nuclear_scattering": {
        "must_any": [["scattering", "cross section", "reaction", "channel", "annihilation"], ["optical", "potential", "coupled", "transmission", "deuteron", "antiproton", "alpha-particle"]],
        "review_if_fewer_hits": 1,
    },
    "ml_alpha_halflife": {
        "must_any": [["alpha", "\\alpha"], ["half life", "half-life", "decay"], ["machine", "deep", "neural", "learning", "transfer", "voting"]],
        "review_if_fewer_hits": 3,
    },
}

GENERIC_PATTERNS = [
    r"typical value",
    r"will be used",
    r"will be calculated",
    r"后续.*计算",
    r"典型值",
    r"大约",
    r"约\s*\d+\s*[-至]",
]


@dataclass
class Finding:
    id: str
    subdomain: str
    source_doi: str
    severity: str
    category: str
    evidence: str
    file_path: str
    parsed_path: str
    recommended_action: str


def norm_text(text: str) -> str:
    return re.sub(r"[^a-z0-9\\]+", " ", (text or "").lower()).strip()


def compact(text: Any, limit: int = 350) -> str:
    s = str(text or "").replace("\r", " ").replace("\n", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s[: limit - 3] + "..." if len(s) > limit else s


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as f:
        return json.load(f)


def first_heading(md_path: Path) -> str:
    try:
        for line in md_path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    except Exception as exc:
        return f"<read error: {exc}>"
    return ""


def parsed_excerpt(md_path: Path, max_chars: int = 4500) -> str:
    if not md_path or not md_path.exists():
        return ""
    text = md_path.read_text(encoding="utf-8-sig", errors="replace")
    return text[:max_chars]


def find_parsed(parsed_root: Path, source_doi: str) -> Path | None:
    if not source_doi:
        return None
    matches = sorted(parsed_root.rglob(f"{source_doi}.md"))
    return matches[0] if matches else None


def add_finding(
    findings: list[Finding],
    sample_id: str,
    subdomain: str,
    source_doi: str,
    severity: str,
    category: str,
    evidence: str,
    file_path: Path,
    parsed_path: Path | None,
    action: str | None = None,
) -> None:
    findings.append(
        Finding(
            id=sample_id,
            subdomain=subdomain,
            source_doi=source_doi,
            severity=severity,
            category=category,
            evidence=compact(evidence, 1000),
            file_path=str(file_path),
            parsed_path=str(parsed_path) if parsed_path else "",
            recommended_action=action or ACTION_BY_SEVERITY[severity],
        )
    )


def regex_hits(patterns: list[str], text: str) -> list[str]:
    return [p for p in patterns if re.search(p, text, flags=re.IGNORECASE)]


def subdomain_hits(subdomain: str, text_norm: str) -> tuple[int, list[str]]:
    rule = SUBDOMAIN_RULES.get(subdomain)
    if not rule:
        return 0, []
    labels = []
    for group in rule["must_any"]:
        if any(token.lower() in text_norm for token in group):
            labels.append("/".join(group[:3]))
    return len(labels), labels


def method_support_ratio(methods: list[str], parsed_norm: str) -> tuple[int, int, list[str]]:
    unsupported = []
    checked = 0
    ignore = {
        "model",
        "method",
        "theory",
        "calculation",
        "learning",
        "neural",
        "network",
        "deep",
    }
    for method in methods:
        parts = [p for p in re.split(r"[_\W]+", method.lower()) if len(p) > 3 and p not in ignore]
        if not parts:
            continue
        checked += 1
        hits = sum(1 for p in parts if p in parsed_norm)
        if hits == 0:
            unsupported.append(method)
    return len(unsupported), checked, unsupported


def phase_order_status(phases: list[str]) -> bool:
    order = {"prediction": 0, "decision_summary": 1, "paper_derivation": 2}
    values = [order.get(p, -1) for p in phases]
    return all(a <= b for a, b in zip(values, values[1:]))


def audit_one(path: Path, parsed_root: Path) -> tuple[dict[str, Any], list[Finding]]:
    findings: list[Finding] = []
    data = load_json(path)
    meta = data.get("meta") or {}
    source = meta.get("source") or {}
    sample_id = str(data.get("id") or meta.get("id") or path.stem)
    subdomain = str(meta.get("subdomain") or "")
    source_doi = str(source.get("problem_number_or_doi") or "")
    title = str(source.get("title") or "")
    parsed_path = find_parsed(parsed_root, source_doi)
    parsed_title = first_heading(parsed_path) if parsed_path else ""
    excerpt = parsed_excerpt(parsed_path)
    excerpt_norm = norm_text(excerpt)

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            add_finding(findings, sample_id, subdomain, source_doi, "P1", "missing_top_level_field", f"缺少顶层字段：{key}", path, parsed_path)

    if data.get("id") != meta.get("id"):
        add_finding(findings, sample_id, subdomain, source_doi, "P1", "id_mismatch", f"顶层 id={data.get('id')}，meta.id={meta.get('id')}", path, parsed_path)

    if not data.get("paper_methods"):
        add_finding(findings, sample_id, subdomain, source_doi, "P1", "empty_paper_methods", "paper_methods 为空", path, parsed_path)

    paper_facts = data.get("paper_facts") or {}
    for field in ["methods", "key_formulas", "key_results"]:
        if not paper_facts.get(field):
            severity = "P2" if field == "key_results" else "P1"
            add_finding(findings, sample_id, subdomain, source_doi, severity, f"empty_paper_facts_{field}", f"paper_facts.{field} 为空", path, parsed_path)

    if not parsed_path:
        add_finding(findings, sample_id, subdomain, source_doi, "P1", "missing_parsed_source", "未找到与 source DOI 对应的 parsed Markdown 源文件", path, parsed_path)
    else:
        a = norm_text(title)
        b = norm_text(parsed_title)
        if a and b and a != b and a not in b and b not in a:
            add_finding(
                findings,
                sample_id,
                subdomain,
                source_doi,
                "P1",
                "source_title_mismatch",
                f"final 标题与 parsed H1 不一致。final={title!r}；parsed={parsed_title!r}",
                path,
                parsed_path,
            )

    initial = data.get("01_initial_request") or {}
    trajectory = data.get("02_agent_trajectory") or []
    verification = data.get("03_success_verification") or {}
    sample_text = " ".join(
        [
            title,
            json.dumps(initial, ensure_ascii=False),
            " ".join(data.get("paper_methods") or []),
            json.dumps(paper_facts, ensure_ascii=False),
            json.dumps(verification, ensure_ascii=False),
        ]
    )
    sample_norm = norm_text(sample_text)
    source_norm = norm_text(" ".join([parsed_title, excerpt]))

    non_nuclear_hits = regex_hits(NON_NUCLEAR_PATTERNS, " ".join([parsed_title, excerpt[:1800]]))
    nuclear_hits = regex_hits(NUCLEAR_DOMAIN_PATTERNS, " ".join([parsed_title, excerpt[:2500]]))
    final_nuclear_hits = regex_hits(NUCLEAR_DOMAIN_PATTERNS, sample_text)
    if non_nuclear_hits and len(nuclear_hits) < 2 and len(final_nuclear_hits) >= 2:
        add_finding(
            findings,
            sample_id,
            subdomain,
            source_doi,
            "P0",
            "source_subject_mismatch",
            f"parsed 源文件呈现非核物理主题信号（{non_nuclear_hits[:5]}），但 final 样本呈现核物理主题信号（{final_nuclear_hits[:5]}）。parsed 标题={parsed_title!r}",
            path,
            parsed_path,
        )

    source_hit_count, source_hit_labels = subdomain_hits(subdomain, norm_text(" ".join([parsed_title, excerpt[:2500]])))
    source_required_hits = SUBDOMAIN_RULES.get(subdomain, {}).get("review_if_fewer_hits", 1)
    if source_hit_count < source_required_hits:
        add_finding(
            findings,
            sample_id,
            subdomain,
            source_doi,
            "P2",
            "source_subdomain_low_keyword_support",
            f"parsed 源文件仅命中 {source_hit_count}/{source_required_hits} 组预期子领域信号：{source_hit_labels}。parsed_title={parsed_title!r}",
            path,
            parsed_path,
        )

    hit_count, hit_labels = subdomain_hits(subdomain, norm_text(" ".join([title, sample_text])))
    required_hits = SUBDOMAIN_RULES.get(subdomain, {}).get("review_if_fewer_hits", 1)
    if hit_count < required_hits:
        add_finding(
            findings,
            sample_id,
            subdomain,
            source_doi,
            "P2",
            "subdomain_low_keyword_support",
            f"样本内容仅命中 {hit_count}/{required_hits} 组预期子领域信号：{hit_labels}。title={title!r}",
            path,
            parsed_path,
        )

    unsupported_count, checked_count, unsupported = method_support_ratio(data.get("paper_methods") or [], source_norm)
    if checked_count and (unsupported_count / checked_count >= 0.75 or (unsupported_count >= 3 and unsupported_count / checked_count >= 0.6)):
        severity = "P2"
        if non_nuclear_hits and len(final_nuclear_hits) >= 2:
            severity = "P0"
        add_finding(
            findings,
            sample_id,
            subdomain,
            source_doi,
            severity,
            "paper_methods_unsupported_by_source",
            f"{unsupported_count}/{checked_count} 个 paper_methods 在 parsed 源文件中缺少词面支持：{unsupported[:8]}",
            path,
            parsed_path,
        )

    phases = []
    formula_texts = [str(f.get("label", "")) + " " + str(f.get("content", "")) for f in paper_facts.get("key_formulas") or [] if isinstance(f, dict)]
    paper_derivation_obs = []
    decision_summary_texts = []
    invalid_steps = 0
    generic_paper_steps = 0
    for expected_idx, step in enumerate(trajectory, start=1):
        phase = step.get("phase")
        phases.append(phase)
        if step.get("step_index") != expected_idx:
            add_finding(findings, sample_id, subdomain, source_doi, "P1", "bad_step_index", f"step_index 应为 {expected_idx}，实际为 {step.get('step_index')}", path, parsed_path)
        if phase not in VALID_PHASES:
            add_finding(findings, sample_id, subdomain, source_doi, "P1", "bad_phase", f"第 {expected_idx} 步 phase 非法：{phase!r}", path, parsed_path)
        if step.get("action") not in VALID_ACTIONS:
            add_finding(findings, sample_id, subdomain, source_doi, "P1", "bad_action", f"第 {expected_idx} 步 action 非法：{step.get('action')!r}", path, parsed_path)
        if not isinstance(step.get("valid"), bool):
            add_finding(findings, sample_id, subdomain, source_doi, "P1", "bad_valid_type", f"第 {expected_idx} 步 valid 不是 bool：{step.get('valid')!r}", path, parsed_path)
        if step.get("error_tag") not in VALID_ERROR_TAGS:
            add_finding(findings, sample_id, subdomain, source_doi, "P1", "bad_error_tag", f"第 {expected_idx} 步 error_tag 非法：{step.get('error_tag')!r}", path, parsed_path)
        if step.get("valid") is False:
            invalid_steps += 1
            if not step.get("error_tag") or step.get("error_tag") == "null":
                add_finding(findings, sample_id, subdomain, source_doi, "P1", "invalid_step_missing_error_tag", f"第 {expected_idx} 步 valid=false，但 error_tag 缺失或非法", path, parsed_path)
            if not step.get("error_reason"):
                add_finding(findings, sample_id, subdomain, source_doi, "P1", "invalid_step_missing_error_reason", f"第 {expected_idx} 步 valid=false，但缺少 error_reason", path, parsed_path)
        if phase == "paper_derivation":
            obs = str(step.get("observation") or "")
            paper_derivation_obs.append(obs)
            if step.get("observation_source") != "paper":
                add_finding(findings, sample_id, subdomain, source_doi, "P3", "paper_derivation_observation_source", f"第 {expected_idx} 步 paper_derivation 的 observation_source={step.get('observation_source')!r}", path, parsed_path)
            if any(re.search(p, obs, flags=re.IGNORECASE) for p in GENERIC_PATTERNS):
                generic_paper_steps += 1
        if phase == "decision_summary":
            thought_obs = str(step.get("thought") or "") + " " + str(step.get("observation") or "") + " " + str(step.get("overall_lesson") or "")
            decision_summary_texts.append(thought_obs)

    if trajectory and not phase_order_status(phases):
        add_finding(findings, sample_id, subdomain, source_doi, "P2", "phase_order_nonstandard", f"phase 顺序不符合 prediction -> decision_summary -> paper_derivation：{phases}", path, parsed_path)

    if invalid_steps and decision_summary_texts:
        joined_decision = "\n".join(decision_summary_texts)
        required = ["决策", "错过", "正确"]
        has_lesson = any("overall_lesson" in step and step.get("overall_lesson") for step in trajectory if step.get("phase") == "decision_summary")
        if not all(token in joined_decision for token in required) and not has_lesson:
            add_finding(
                findings,
                sample_id,
                subdomain,
                source_doi,
                "P2",
                "weak_decision_summary",
                "decision_summary 在样本整体层面缺少完整的决策时刻、错过信号、正确判断元素。",
                path,
                parsed_path,
            )

    if formula_texts and paper_derivation_obs:
        combined_obs = "\n".join(paper_derivation_obs)
        used = 0
        for f in formula_texts:
            label = f.split(" ", 1)[0]
            if label and label in combined_obs:
                used += 1
            else:
                content_tokens = [t for t in re.split(r"[^A-Za-z0-9]+", f) if len(t) > 3]
                if content_tokens and sum(1 for t in content_tokens[:12] if t in combined_obs) >= 2:
                    used += 1
        if used == 0:
            add_finding(findings, sample_id, subdomain, source_doi, "P2", "key_formulas_not_used_in_derivation", "paper_derivation observation 中未检出 key_formulas 的引用或注入痕迹", path, parsed_path)

    if paper_derivation_obs and generic_paper_steps / max(1, len(paper_derivation_obs)) >= 0.75:
        add_finding(
            findings,
            sample_id,
            subdomain,
            source_doi,
            "P3",
            "paper_derivation_template_like",
            f"{generic_paper_steps}/{len(paper_derivation_obs)} 条 paper_derivation observation 含泛化或模板化表述",
            path,
            parsed_path,
        )

    metrics = verification.get("metrics") if isinstance(verification, dict) else None
    if not metrics:
        add_finding(findings, sample_id, subdomain, source_doi, "P1", "empty_verification_metrics", "03_success_verification.metrics 为空或缺失", path, parsed_path)
    else:
        for metric_name, spec in metrics.items():
            if not isinstance(spec, dict):
                add_finding(findings, sample_id, subdomain, source_doi, "P1", "bad_metric_shape", f"metrics.{metric_name} 不是 object", path, parsed_path)
                continue
            unit = str(spec.get("unit") or "")
            if len(unit) > 30 or any(token in unit for token in ["使用", "基于", "condition", "Z=", "A="]):
                add_finding(findings, sample_id, subdomain, source_doi, "P3", "metric_unit_contains_condition", f"metrics.{metric_name} 的 unit 字段疑似写入条件说明：{unit!r}", path, parsed_path)

    failure_points = [str(x) for x in paper_facts.get("failure_points") or []]
    final_verdict = str(verification.get("final_verdict") or "") if isinstance(verification, dict) else ""
    if failure_points and final_verdict:
        missing = [fp for fp in failure_points if fp and fp not in final_verdict]
        if len(missing) == len(failure_points):
            add_finding(findings, sample_id, subdomain, source_doi, "P3", "final_verdict_failure_points_not_referenced", f"final_verdict 未引用 failure_points：{failure_points[:6]}", path, parsed_path)

    severity = "PASS"
    if findings:
        severity = sorted((f.severity for f in findings), key=lambda s: SEVERITY_RANK[s])[0]
    summary = {
        "id": sample_id,
        "subdomain": subdomain,
        "source_doi": source_doi,
        "title": title,
        "parsed_title": parsed_title,
        "file_path": str(path),
        "parsed_path": str(parsed_path) if parsed_path else "",
        "risk_level": severity,
        "risk_label": SEVERITY_LABEL[severity],
        "issue_count": len(findings),
        "recommended_action": "无。" if severity == "PASS" else ACTION_BY_SEVERITY[severity],
        "num_steps": len(trajectory),
        "invalid_steps": invalid_steps,
    }
    return summary, findings


def write_outputs(out_dir: Path, summaries: list[dict[str, Any]], findings: list[Finding]) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    findings_path = out_dir / "research_audit_findings.jsonl"
    with findings_path.open("w", encoding="utf-8", newline="\n") as f:
        for finding in findings:
            f.write(json.dumps(asdict(finding), ensure_ascii=False) + "\n")

    summary_path = out_dir / "research_audit_summary.csv"
    summary_fields = [
        "id",
        "subdomain",
        "source_doi",
        "risk_level",
        "risk_label",
        "issue_count",
        "recommended_action",
        "num_steps",
        "invalid_steps",
        "title",
        "parsed_title",
        "file_path",
        "parsed_path",
    ]
    with summary_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=summary_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(summaries)

    by_id = defaultdict(list)
    for finding in findings:
        by_id[finding.id].append(finding)

    p0 = [s for s in summaries if s["risk_level"] == "P0"]
    with (out_dir / "p0_reject_candidates.txt").open("w", encoding="utf-8", newline="\n") as f:
        for s in p0:
            f.write(f"{s['id']}\t{s['subdomain']}\t{s['source_doi']}\t{s['title']}\n")

    manual = [s for s in summaries if s["risk_level"] in {"P0", "P1", "P2"}]
    with (out_dir / "p2_manual_review_queue.md").open("w", encoding="utf-8", newline="\n") as f:
        f.write("# Research 层复核清单\n\n")
        f.write("本清单包含 P0/P1/P2 样本。P0/P1 同步列入清单，用于在数据处置前核验证据。\n\n")
        for s in manual:
            f.write(f"## {s['id']} - {s['risk_level']} {s['risk_label']}\n\n")
            f.write(f"- Subdomain: `{s['subdomain']}`\n")
            f.write(f"- Source: `{s['source_doi']}`\n")
            f.write(f"- Final 标题: {s['title']}\n")
            f.write(f"- Parsed 标题: {s['parsed_title']}\n")
            f.write(f"- 处置项: {s['recommended_action']}\n")
            f.write("- 问题记录:\n")
            for finding in by_id[s["id"]][:8]:
                f.write(f"  - `{finding.severity}` `{finding.category}`: {finding.evidence}\n")
            if len(by_id[s["id"]]) > 8:
                f.write(f"  - ... 其余 {len(by_id[s['id']]) - 8} 条见 JSONL\n")
            f.write("\n")

    severity_counts = Counter(s["risk_level"] for s in summaries)
    category_counts = Counter(f.category for f in findings)
    subdomain_counts = Counter(s["subdomain"] for s in summaries)
    subdomain_risks = defaultdict(Counter)
    for s in summaries:
        subdomain_risks[s["subdomain"]][s["risk_level"]] += 1
    p1 = [s for s in summaries if s["risk_level"] == "P1"]
    p2 = [s for s in summaries if s["risk_level"] == "P2"]
    p3 = [s for s in summaries if s["risk_level"] == "P3"]
    pass_rows = [s for s in summaries if s["risk_level"] == "PASS"]

    report_path = out_dir / "research_audit_report.md"
    with report_path.open("w", encoding="utf-8", newline="\n") as f:
        f.write("# Research 层审核报告\n\n")
        f.write("本报告由 `scripts/audit/research_layer_audit.py` 生成。报告以证据为核心，仅用于审核，不修改数据集文件。\n\n")
        f.write("## 总览\n\n")
        f.write(f"- 已扫描 Research 样本数：{len(summaries)}\n")
        f.write(f"- 问题记录数：{len(findings)}\n")
        for sev in ["P0", "P1", "P2", "P3", "PASS"]:
            f.write(f"- {sev} {SEVERITY_LABEL[sev]}：{severity_counts.get(sev, 0)} 条样本\n")
        f.write("\n## 子领域风险分布\n\n")
        f.write("| 子领域 | 样本数 | P0 | P1 | P2 | P3 | PASS |\n")
        f.write("|---|---:|---:|---:|---:|---:|---:|\n")
        for subdomain, total in sorted(subdomain_counts.items()):
            risks = subdomain_risks[subdomain]
            f.write(f"| `{subdomain}` | {total} | {risks['P0']} | {risks['P1']} | {risks['P2']} | {risks['P3']} | {risks['PASS']} |\n")
        f.write("\n## 问题类别计数\n\n")
        for category, count in category_counts.most_common():
            f.write(f"- `{category}`: {count}\n")
        f.write("\n## P0 删除或替换清单\n\n")
        if not p0:
            f.write("未检出 P0 样本。\n")
        for s in p0:
            f.write(f"- `{s['id']}` `{s['subdomain']}` `{s['source_doi']}`: {s['title']}\n")
            for finding in by_id[s["id"]]:
                if finding.severity == "P0":
                    f.write(f"  - 证据：{finding.evidence}\n")
        f.write("\n## P1 必须修复样本\n\n")
        if not p1:
            f.write("未检出 P1 样本。\n")
        for s in p1[:60]:
            cats = ", ".join(sorted({f.category for f in by_id[s["id"]] if f.severity == "P1"}))
            f.write(f"- `{s['id']}` `{s['subdomain']}`: {cats}\n")
        if len(p1) > 60:
            f.write(f"- ... 其余 {len(p1) - 60} 条 P1 样本见 CSV/JSONL\n")
        f.write("\n## P2 人工复核样本\n\n")
        if not p2:
            f.write("未检出 P2 样本。\n")
        for s in p2[:80]:
            cats = ", ".join(sorted({f.category for f in by_id[s["id"]] if f.severity == "P2"}))
            f.write(f"- `{s['id']}` `{s['subdomain']}` `{s['source_doi']}`: {cats}\n")
        if len(p2) > 80:
            f.write(f"- ... 其余 {len(p2) - 80} 条 P2 样本见复核清单\n")
        f.write("\n## 处置流程\n\n")
        f.write("1. P0：核验证据后移除或替换。\n")
        f.write("2. P1：发布前完成 schema 错误修复。\n")
        f.write("3. P2：读取证据摘录和对应 parsed Markdown 源文件，完成复核判定。\n")
        f.write("4. P3：内容取舍稳定后，批量清理格式和文本问题。\n")
        f.write("\n## 输出文件\n\n")
        f.write("- `research_audit_findings.jsonl`：每行一条 finding，便于机器读取。\n")
        f.write("- `research_audit_summary.csv`：每行一条样本摘要。\n")
        f.write("- `p0_reject_candidates.txt`：P0 删除或替换清单。\n")
        f.write("- `p2_manual_review_queue.md`：证据复核清单。\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit Research layer dataset samples.")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Project root")
    parser.add_argument("--output", type=Path, default=None, help="Output audit directory")
    args = parser.parse_args()

    root = args.root.resolve()
    research_dir = root / "dataset" / "final" / "Research"
    parsed_root = root / "parsed" / "papers"
    out_dir = args.output or (root / "audit" / "research_layer")

    summaries: list[dict[str, Any]] = []
    findings: list[Finding] = []
    for path in sorted(research_dir.glob("*.json")):
        summary, sample_findings = audit_one(path, parsed_root)
        summaries.append(summary)
        findings.extend(sample_findings)

    summaries.sort(key=lambda s: (SEVERITY_RANK[s["risk_level"]], s["id"]))
    findings.sort(key=lambda f: (SEVERITY_RANK[f.severity], f.id, f.category))
    write_outputs(out_dir, summaries, findings)

    print(f"[OK] Scanned {len(summaries)} Research samples")
    print(f"[OK] Findings: {len(findings)}")
    print(f"[OK] Output: {out_dir}")
    for sev in ["P0", "P1", "P2", "P3", "PASS"]:
        print(f"  {sev}: {sum(1 for s in summaries if s['risk_level'] == sev)}")


if __name__ == "__main__":
    main()
