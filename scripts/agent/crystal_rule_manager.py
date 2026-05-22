"""
crystal_rule_manager.py - Crystal Growth Dynamic Experience System

Accumulates physics derivation rules across papers within a subdomain.
Rules are extracted from common error patterns and injected into future predictions.

Lifecycle:
  1. Before prediction: inject top-K active rules into system prompt
  2. After Phase 4: evaluate whether rules helped
  3. Every BATCH_SIZE papers: extract new rules from accumulated errors
"""

import datetime
import json
import os
import re
import time
from pathlib import Path

# Default rules_db.json location (global, single file)
_DEFAULT_DB_PATH = Path(__file__).resolve().parent / "rules_db.json"

# DeepSeek API key (reuse from environment)
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")


# ── Prompts ───────────────────────────────────────────────────────────────────

RULE_EXTRACTION_PROMPT = """\
你是核物理推导专家。基于以下在 {subdomain} 子领域中常见的推导错误，\
总结3-5条物理层面或逻辑层面的先验避错规则。

要求：
- 规则必须是通用的物理/逻辑原则，不包含具体公式或数值
- 每条规则应该能帮助避免类似错误的再次发生
- 用中文表述，简洁明了（每条不超过80字）

## 常见错误汇总
{error_summary}

输出严格 JSON：
{{"rules": ["规则1内容", "规则2内容", ...]}}
只输出 JSON。"""

RULE_EVAL_PROMPT = """\
你是核物理推导专家。以下经验规则在本次预测中被注入：
{rules_text}

以下是预测步骤的错误分析结果：
{error_summary}

请评估每条规则对本次预测的影响：
- "help": 规则帮助避免了错误或引导了正确推理
- "harm": 规则误导了推理方向，导致了错误
- "none": 规则对本次推理无明显影响

输出严格 JSON：
{{"rule_eval": {{{rule_ids_template}}}}}
只输出 JSON。"""


class CrystalRuleManager:
    """Crystal Growth Dynamic Experience System."""

    TOP_K = 5
    SCORE_HELP = 10
    SCORE_HARM = -20
    SCORE_NONE = -1
    CIRCUIT_BREAKER_THRESHOLD = 50

    def __init__(self, subdomain: str, batch_size: int = 30, rules_db_path: Path = None):
        """
        Args:
            subdomain: Current subdomain for rule filtering (e.g., "alpha_decay_wkb")
            batch_size: Number of papers between rule extraction triggers (default 30)
            rules_db_path: Path to rules_db.json. Defaults to agent_Review/rules_db.json.
        """
        self.subdomain = subdomain
        self.batch_size = batch_size
        self.db_path = rules_db_path or _DEFAULT_DB_PATH
        self._error_buffer: list[dict] = []
        self._papers_since_last_extraction = 0

    # ── Public API ────────────────────────────────────────────────────────────

    def get_experience_prompt(self) -> tuple[str, list[str]]:
        """
        Query top-K active rules for current subdomain.

        Returns:
            (prompt_text, list_of_rule_ids_injected)
            prompt_text is empty string if no active rules exist.
        """
        db = self._load_db()
        active_rules = [
            r for r in db["rules"]
            if r["status"] == "active" and r["subdomain"] == self.subdomain
        ]
        # Sort by confidence descending, take top-K
        active_rules.sort(key=lambda r: r["confidence_score"], reverse=True)
        top_rules = active_rules[: self.TOP_K]

        if not top_rules:
            return ("", [])

        lines = []
        rule_ids = []
        for i, rule in enumerate(top_rules, start=1):
            lines.append(f"{i}. [{rule['rule_id']}] {rule['content']}")
            rule_ids.append(rule["rule_id"])

        prompt_text = "\n".join(lines)
        return (prompt_text, rule_ids)

    def record_paper_errors(self, error_tags: list[dict]) -> None:
        """
        Accumulate error_tag/error_reason from a completed paper.

        Args:
            error_tags: List of {"error_tag": str, "error_reason": str}
        """
        self._error_buffer.extend(error_tags)
        self._papers_since_last_extraction += 1

        # Update metadata
        db = self._load_db()
        db["metadata"]["total_papers_processed"] = (
            db["metadata"].get("total_papers_processed", 0) + 1
        )
        self._save_db(db)

    def maybe_extract_rules(self, client) -> int:
        """
        If papers_processed >= BATCH_SIZE, trigger rule extraction via LLM.

        Args:
            client: OpenAI-compatible client (DeepSeek)

        Returns:
            Number of new rules extracted (0 if not triggered)
        """
        if self._papers_since_last_extraction < self.batch_size:
            return 0

        if not self._error_buffer:
            self._papers_since_last_extraction = 0
            return 0

        # Build error summary
        error_summary = self._build_error_summary()

        # Call LLM
        prompt = RULE_EXTRACTION_PROMPT.format(
            subdomain=self.subdomain,
            error_summary=error_summary,
        )

        try:
            new_rules = self._call_extraction(client, prompt)
        except Exception as e:
            print(f"  [!] Crystal rule extraction failed: {e}")
            self._papers_since_last_extraction = 0
            self._error_buffer.clear()
            return 0

        # Store new rules
        db = self._load_db()
        count = 0
        for content in new_rules:
            rule_id = self._generate_rule_id(db)
            db["rules"].append({
                "rule_id": rule_id,
                "content": content,
                "confidence_score": 100,
                "usage_count": 0,
                "status": "active",
                "subdomain": self.subdomain,
                "created_at": datetime.datetime.now().isoformat(),
                "last_used": None,
            })
            count += 1

        db["metadata"]["last_extraction_at"] = datetime.datetime.now().isoformat()
        self._save_db(db)

        # Reset
        self._papers_since_last_extraction = 0
        self._error_buffer.clear()

        print(f"  [Crystal] Extracted {count} new rules for {self.subdomain}")
        return count

    def evaluate_rules(
        self,
        prediction_traj: list[dict],
        injected_rule_ids: list[str],
        client,
    ) -> None:
        """
        After Phase 4, ask LLM to evaluate whether injected rules helped.
        Update confidence_score and status accordingly.

        Fault-tolerant: API failures default to "none" for all rules.
        """
        if not injected_rule_ids:
            return

        # Build context
        db = self._load_db()
        rules_text = self._format_rules_for_eval(db, injected_rule_ids)
        error_summary = self._build_prediction_error_summary(prediction_traj)
        rule_ids_template = ", ".join(
            f'"{rid}": "help|harm|none"' for rid in injected_rule_ids
        )

        prompt = RULE_EVAL_PROMPT.format(
            rules_text=rules_text,
            error_summary=error_summary,
            rule_ids_template=rule_ids_template,
        )

        # Call LLM with fault tolerance
        try:
            evaluations = self._call_evaluation(client, prompt)
        except Exception as e:
            print(f"  [!] Crystal rule evaluation failed: {e}")
            evaluations = {rid: "none" for rid in injected_rule_ids}

        # Apply scores
        self._apply_scores(evaluations, injected_rule_ids)

    # ── Internal Methods ──────────────────────────────────────────────────────

    def _apply_scores(self, evaluations: dict, injected_rule_ids: list[str]) -> None:
        """Apply score changes and circuit breaker logic."""
        db = self._load_db()
        rule_map = {r["rule_id"]: r for r in db["rules"]}

        for rid in injected_rule_ids:
            verdict = evaluations.get(rid, "none")
            if rid not in rule_map:
                continue

            rule = rule_map[rid]
            if verdict == "help":
                rule["confidence_score"] += self.SCORE_HELP
                rule["usage_count"] += 1
            elif verdict == "harm":
                rule["confidence_score"] += self.SCORE_HARM
            else:  # "none" or unknown
                rule["confidence_score"] += self.SCORE_NONE

            rule["last_used"] = datetime.datetime.now().isoformat()

            # Circuit breaker
            if rule["confidence_score"] < self.CIRCUIT_BREAKER_THRESHOLD:
                rule["status"] = "inactive"
                print(f"  [Crystal] Rule {rid} deactivated (score={rule['confidence_score']})")

        self._save_db(db)

    def _build_error_summary(self) -> str:
        """Format accumulated errors for extraction prompt."""
        if not self._error_buffer:
            return "(no errors recorded)"

        lines = []
        for i, err in enumerate(self._error_buffer[:50], start=1):  # Cap at 50
            tag = err.get("error_tag", "unknown")
            reason = err.get("error_reason", "")
            if reason:
                lines.append(f"{i}. [{tag}] {reason}")
            else:
                lines.append(f"{i}. [{tag}]")
        return "\n".join(lines)

    def _build_prediction_error_summary(self, prediction_traj: list[dict]) -> str:
        """Format prediction errors for evaluation prompt."""
        errors = [s for s in prediction_traj if s.get("error_tag")]
        if not errors:
            return "prediction has no errors (all steps valid)"

        lines = []
        for s in errors:
            lines.append(
                f"Step {s['step_index']}: [{s['error_tag']}] "
                f"{s.get('error_reason', '')}"
            )
        return "\n".join(lines)

    def _format_rules_for_eval(self, db: dict, rule_ids: list[str]) -> str:
        """Format injected rules for evaluation prompt."""
        rule_map = {r["rule_id"]: r for r in db["rules"]}
        lines = []
        for rid in rule_ids:
            if rid in rule_map:
                lines.append(f"- [{rid}] {rule_map[rid]['content']}")
        return "\n".join(lines)

    def _call_extraction(self, client, prompt: str) -> list[str]:
        """Call DeepSeek for rule extraction. Returns list of rule content strings."""
        for attempt in range(3):
            try:
                resp = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": "You are a nuclear physics expert."},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.3,
                    max_tokens=1000,
                )
                raw = resp.choices[0].message.content.strip()
                raw = re.sub(r"^```(?:json)?\s*", "", raw)
                raw = re.sub(r"\s*```$", "", raw)
                result = json.loads(raw)
                rules = result.get("rules", [])
                if isinstance(rules, list) and all(isinstance(r, str) for r in rules):
                    return rules[:5]  # Cap at 5
                return []
            except (json.JSONDecodeError, KeyError, AttributeError):
                if attempt < 2:
                    time.sleep(2)
                    continue
                raise
        return []

    def _call_evaluation(self, client, prompt: str) -> dict:
        """Call DeepSeek for rule evaluation. Returns {rule_id: verdict} dict."""
        for attempt in range(3):
            try:
                resp = client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": "You are a nuclear physics expert."},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.1,
                    max_tokens=500,
                )
                raw = resp.choices[0].message.content.strip()
                raw = re.sub(r"^```(?:json)?\s*", "", raw)
                raw = re.sub(r"\s*```$", "", raw)
                result = json.loads(raw)
                evaluations = result.get("rule_eval", {})
                if isinstance(evaluations, dict):
                    # Validate values
                    valid_verdicts = {"help", "harm", "none"}
                    return {
                        k: v if v in valid_verdicts else "none"
                        for k, v in evaluations.items()
                    }
                return {}
            except (json.JSONDecodeError, KeyError, AttributeError):
                if attempt < 2:
                    time.sleep(2)
                    continue
                raise
        return {}

    def _generate_rule_id(self, db: dict) -> str:
        """Generate next rule_id like 'rule_001', 'rule_002', etc."""
        existing_ids = [r["rule_id"] for r in db["rules"]]
        if not existing_ids:
            return "rule_001"
        # Extract max number
        max_num = 0
        for rid in existing_ids:
            match = re.match(r"rule_(\d+)", rid)
            if match:
                max_num = max(max_num, int(match.group(1)))
        return f"rule_{max_num + 1:03d}"

    def _load_db(self) -> dict:
        """Load rules_db.json, create with empty structure if not exists or corrupted."""
        if not self.db_path.exists():
            return self._empty_db()
        try:
            data = json.loads(self.db_path.read_text(encoding="utf-8"))
            if "rules" not in data or "metadata" not in data:
                return self._empty_db()
            return data
        except (json.JSONDecodeError, OSError):
            print(f"  [!] rules_db.json corrupted, recreating")
            return self._empty_db()

    def _save_db(self, db: dict) -> None:
        """Write rules_db.json atomically (write .tmp then rename)."""
        tmp_path = self.db_path.with_suffix(".json.tmp")
        tmp_path.write_text(
            json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        tmp_path.replace(self.db_path)

    @staticmethod
    def _empty_db() -> dict:
        """Return empty database structure."""
        return {
            "rules": [],
            "metadata": {
                "total_papers_processed": 0,
                "last_extraction_at": None,
            },
        }
