"""
audit_quality.py — 数据质量自动审核器

对 Research 层 _v2.json 文件进行多维度质量评分，输出四档分级报告。
评分维度：结构完整性、逻辑一致性、数值交叉验证、文本质量、语义深度(LLM审核)、预测-论文对比价值

用法:
  python agent_Review/audit_quality.py                          # 全量扫描
  python agent_Review/audit_quality.py --limit 10               # 前10篇测试
  python agent_Review/audit_quality.py --subdomain "alpha   WKB" # 单子领域
  python agent_Review/audit_quality.py --paper NPP_0001          # 单篇
  python agent_Review/audit_quality.py --skip-llm                # 仅规则层（零API成本）
  python agent_Review/audit_quality.py --reaudit                 # 忽略LLM缓存
"""

import argparse
import hashlib
import json
import os
import re
import time
from datetime import datetime
from pathlib import Path

import openai

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = PROJECT_ROOT / "raw_dataset" / "papers"

RESEARCH_DIRS = [
    PAPERS_DIR / "alpha   WKB",
    PAPERS_DIR / "alpha_液滴模型",
    PAPERS_DIR / "alpha_壳模型",
    PAPERS_DIR / "alpha_团簇模型",
    PAPERS_DIR / "alpha_双折叠势模型",
    PAPERS_DIR / "深度学习_核结构",
    PAPERS_DIR / "核散射_截面",
    PAPERS_DIR / "机器学习_alpha半衰期",
]

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")

# ── 评分权重表 ─────────────────────────────────────────────────────────────────

WEIGHTS_PRED_PAPER = {
    "structural_completeness": 0.25,
    "logical_consistency": 0.25,
    "numerical_cross_validation": 0.15,
    "text_quality": 0.15,
    "semantic_depth": 0.20,
}

WEIGHTS_DECISION = {
    "structural_completeness": 0.20,
    "logical_consistency": 0.20,
    "text_quality": 0.15,
    "semantic_depth": 0.20,
    "prediction_paper_contrast": 0.25,
}

# 四档分级阈值
TIER_THRESHOLDS = {
    "GOLD":   {"overall": 0.90, "phase_floor": 0.85},
    "SILVER": {"overall": 0.75, "phase_floor": 0.70},
    "BRONZE": {"overall": 0.60, "phase_floor": 0.50},
    # below 0.60 → REJECT
}

VALID_ACTIONS = {
    "symbolic_derivation", "numerical_computation", "approximation",
    "verification", "rule_application", "model_building", "correction",
}

VALID_OBSERVATION_SOURCES = {"paper", "inferred"}

# ── 文本质量检测正则 ────────────────────────────────────────────────────────────

PLACEHOLDER_PATTERNS = [
    re.compile(p, re.IGNORECASE) for p in [
        r'numerical\s+result', r'to\s+be\s+determined', r'TBD',
        r'need\s+to\s+compute', r'will\s+be\s+calculated',
        r'not\s+shown', r'can\s+be\s+estimated',
        r'约\s*\d+\s*[–\-—]\s*\d+',  # "约 30-40"
        r'大约\s*\d+\s*[–\-—]\s*\d+',
        r'详见', r'参见\s', r'具体\s*.*\s*待',
        r'需要\s*(进一步|更多|额外)',
        r'数值结果',
    ]
]

GENERIC_PHRASE_PATTERNS = [
    re.compile(p, re.IGNORECASE) for p in [
        r'^(The\s+)?(next\s+)?step\s+(is|will|would|should|can)',
        r'^We\s+need\s+to', r'^Let\s+us\s+now',
        r'^Proceeding\s+to', r'^Moving\s+on\s+to',
        r'^In\s+the\s+following', r'^接下来', r'^下一步',
        r'^然后', r'^接着',
    ]
]

# ── 工具函数 ────────────────────────────────────────────────────────────────────

def _is_numerical_value(val) -> bool:
    """检查值是否看起来是数值（含数字且不是纯定性短语）。"""
    if not val or not isinstance(val, str):
        return False
    val_clean = val.strip()
    if not val_clean:
        return False
    _NON_NUMERICAL_PREFIXES = [
        r'^found\s', r'^very\s', r'^as\s', r'^shown\s', r'^see\s',
        r'^cf\.?\s', r'^Table\s', r'^Figure\s', r'^Eq\.?\s', r'^Ref\.?\s',
        r'^approximately\s', r'^about\s', r'^roughly\s', r'^nearly\s',
        r'^almost\s', r'^around\s', r'^on the order of\s',
    ]
    for pat in _NON_NUMERICAL_PREFIXES:
        if re.match(pat, val_clean, re.IGNORECASE):
            return False
    return bool(re.search(r'\d', val_clean))


def _extract_numbers(text: str) -> list[str]:
    """从文本中提取数值子串（含科学计数法和单位前缀）。"""
    if not text:
        return []
    patterns = [
        r'\d+\.?\d*\s*[×xX]\s*10\^?[+-]?\d+',  # 科学计数法
        r'\d+\.\d+',                              # 小数
        r'\b\d{2,}\b',                             # 多位数整数
    ]
    found = []
    for pat in patterns:
        found.extend(re.findall(pat, text, re.IGNORECASE))
    # 去重保留顺序
    seen = set()
    result = []
    for n in found:
        if n not in seen:
            seen.add(n)
            result.append(n)
    return result


def levenshtein_ratio(a: list[str], b: list[str]) -> float:
    """编辑距离相似度（0-1）。"""
    m, n = len(a), len(b)
    if m == 0 and n == 0:
        return 1.0
    if m == 0 or n == 0:
        return 0.0
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + cost)
    max_len = max(m, n)
    return 1.0 - dp[m][n] / max_len


def jaccard_similarity(text_a: str, text_b: str, n: int = 3) -> float:
    """两段文本的 n-gram Jaccard 相似度（0-1）。"""
    def ngrams(text, ng=n):
        chars = list(text.lower())
        return set("".join(chars[i:i+ng]) for i in range(len(chars) - ng + 1))
    a_grams = ngrams(text_a)
    b_grams = ngrams(text_b)
    if not a_grams or not b_grams:
        return 0.0
    return len(a_grams & b_grams) / len(a_grams | b_grams)


# ── LLM 审核器 Prompt ───────────────────────────────────────────────────────────

AUDITOR_SYSTEM = """你是一位严格的物理期刊审稿人。你的任务不是判断物理推导是否正确，而是评估AI生成的物理推理轨迹的**文本质量和逻辑严谨性**。

你必须像一个挑剔的期刊编辑一样，评估以下方面：

1. **具体性 (specificity)**：思考过程和观察是否针对这篇具体论文？还是泛泛而谈，可以套用到任何类似论文上？
   - 高分：提到论文的具体方法名、具体物理量值、具体条件
   - 低分：全是通用表述，换个论文标题也能用

2. **连贯性 (coherence)**：步骤之间是否形成连贯的推进关系？后一步是否建立在前一步的结果之上？
   - 高分：每步的observation明确产生新信息，后续步骤引用前步产出
   - 低分：步骤各自独立，看不出前一步的结果如何被后一步使用

3. **内容实质 (substance)**：observation是否包含实质性的物理内容（具体数值、明确公式、可验证的断言），还是仅仅复述了thought中的意图？
   - 高分：observation有具体数值、公式、可验证的物理判断
   - 低分：observation只是"完成了X计算"、"得到了Y结果"这类空泛描述
   - 注意：文本长度不等于内容实质。一个50字的含数值observation比200字的纯描述更有实质内容。

4. **模板化程度 (template_free)**：文本中是否包含大量模板句式？
   - **重要豁免**：`thought` 字段中的 `[Background]` / `[Gap]` / `[Decision]` 三段式标记是数据集 schema 的有意设计，**不算模板语言**。评估 thought 时只看这三段内部的文字是否具体，不看这三个标签本身。
   - 低分特征：observation 中机械过渡句（"下一步我们将..."、"需要计算..."、"接下来应该..."、"Let us now..."）、thought 三段内部文字空洞复述
   - 高分特征：thought 三段各自内容具体、observation 语言自然流动，没有机械过渡句

核心原则：冗长≠高质量。简洁、含有具体数值和可验证断言的文本，远比长篇但空泛的描述得分更高。
不要因为文本较长就给高分——先检查它是否包含具体数值、公式、可验证的物理判断。

注意：你绝对不要评估物理推导是否正确。即使是物理上错误的推导，只要其文本表达具体、非模板化、有实质内容、逻辑自洽，就应该得高分。

输出严格JSON格式，不要任何其他文字：
{
  "scores": {
    "specificity": 0.0,
    "coherence": 0.0,
    "substance": 0.0,
    "template_free": 0.0
  },
  "flags": [
    {"step": 1, "issue": "template_language", "detail": "具体问题"}
  ],
  "rationale": "2-3句话总体评价，指出最突出的优缺点"
}

评分标准：
- 0.0-0.3: 严重问题，几乎所有步骤都有缺陷
- 0.4-0.6: 中等，部分步骤有缺陷
- 0.7-0.8: 良好，少数步骤有小问题
- 0.9-1.0: 优秀，几乎没有可挑剔的地方"""


def _build_auditor_user(phase: str, steps: list[dict], paper_facts: dict | None) -> str:
    """构建 LLM 审核器的 user prompt。"""
    if paper_facts is None:
        paper_facts = {}

    methods = [m.get("name", "") for m in paper_facts.get("methods", [])[:5]]
    key_results = [
        f"{r.get('quantity', '?')}: {r.get('value', '?')}"
        for r in paper_facts.get("key_results", [])[:3]
    ]

    ctx_lines = [
        f"论文方法: {', '.join(methods) if methods else '未提取'}",
        f"论文关键结果: {'; '.join(key_results) if key_results else '未提取'}",
        "",
        f"待审核阶段: {phase}（共 {len(steps)} 步）",
        "---",
    ]

    for s in steps:
        thought = (s.get("thought", "") or "")[:300]
        obs = (s.get("observation", "") or "")[:200]
        tool_name = s.get("tool", {}).get("name", "?")
        step_idx = s.get("step_index", "?")
        ctx_lines.append(
            f"Step {step_idx}: tool={tool_name}\n"
            f"  thought: {thought}\n"
            f"  observation: {obs}"
        )

    ctx_lines.append("---")
    ctx_lines.append(
        f"请按系统提示中的标准对以上{phase}阶段的{len(steps)}个步骤进行质量评估。"
        "注意：thought 中的 [Background]/[Gap]/[Decision] 是 schema 设计，不算模板语言。只输出JSON。"
    )

    return "\n".join(ctx_lines)


# ── 主审核器 ────────────────────────────────────────────────────────────────────

class QualityAuditor:
    """多维度数据质量审核器。"""

    def __init__(self, skip_llm: bool = False, cache_path: str | None = None):
        self.skip_llm = skip_llm
        self.client = None if skip_llm else openai.OpenAI(
            api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com"
        )
        self.cache_path = cache_path or str(
            PROJECT_ROOT / "agent_Review" / ".audit_llm_cache.json"
        )
        self._llm_cache: dict[str, dict] = {}
        self._load_cache()

    def _load_cache(self):
        if Path(self.cache_path).exists():
            try:
                self._llm_cache = json.loads(
                    Path(self.cache_path).read_text(encoding="utf-8")
                )
            except Exception:
                self._llm_cache = {}

    def _save_cache(self):
        Path(self.cache_path).write_text(
            json.dumps(self._llm_cache, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    # ── API 调用 ────────────────────────────────────────────────────────────────

    def _call_auditor_llm(self, system: str, user: str) -> dict:
        """LLM 审核器调用（temperature=0.1，比生成器更确定）。"""
        for attempt in range(3):
            try:
                resp = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    temperature=0.1,
                    max_tokens=1000,
                )
                raw = resp.choices[0].message.content.strip()
                raw = re.sub(r'^```(?:json)?\s*', '', raw)
                raw = re.sub(r'\s*```$', '', raw)
                raw = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', raw)
                try:
                    return json.loads(raw)
                except json.JSONDecodeError:
                    raw2 = raw.replace('\\\\\\', '\\\\')
                    return json.loads(raw2)
            except Exception as e:
                if attempt < 2:
                    time.sleep(2)
                else:
                    print(f"    [!] Auditor LLM failed: {e}")
                    return {"scores": {}, "flags": [], "rationale": "API error"}

    # ── 维度1: 结构完整性 ────────────────────────────────────────────────────

    def _score_structural(self, steps: list[dict], phase: str) -> dict:
        """检查字段存在性、非空性、枚举合法性。"""
        deductions = []
        score = 1.0
        n = max(len(steps), 1)

        # ── 防御性检查：步数下限 ──
        if phase == "paper_derivation":
            if n < 3:
                reason = (
                    f"paper_derivation only {n} step(s), "
                    f"severely truncated (expected >= 5)"
                )
                deductions.append({
                    "step_index": 0, "dimension": "structural_completeness",
                    "severity": "high", "description": reason,
                    "deduction": 0.35,
                })
                score -= 0.35
            elif n < 5:
                reason = (
                    f"paper_derivation only {n} step(s), "
                    f"likely truncated or degraded (expected >= 5)"
                )
                deductions.append({
                    "step_index": 0, "dimension": "structural_completeness",
                    "severity": "high", "description": reason,
                    "deduction": 0.18,
                })
                score -= 0.18

        if phase == "prediction":
            if n < 4:
                reason = (
                    f"prediction only {n} step(s), "
                    f"severely abbreviated (expected >= 6)"
                )
                deductions.append({
                    "step_index": 0, "dimension": "structural_completeness",
                    "severity": "high", "description": reason,
                    "deduction": 0.25,
                })
                score -= 0.25
            elif n < 6:
                reason = (
                    f"prediction only {n} step(s), "
                    f"below recommended minimum (expected >= 6)"
                )
                deductions.append({
                    "step_index": 0, "dimension": "structural_completeness",
                    "severity": "medium", "description": reason,
                    "deduction": 0.12,
                })
                score -= 0.12

        REQUIRED_FIELDS = [
            "step_index", "thought", "action", "tool", "parameters",
            "output_state", "observation", "valid", "phase",
        ]

        for s in steps:
            si = s.get("step_index", "?")

            # 必需字段存在性
            for field in REQUIRED_FIELDS:
                if field not in s:
                    deductions.append({
                        "step_index": si, "dimension": "structural_completeness",
                        "severity": "high", "description": f"Missing required field '{field}'",
                        "deduction": 0.05 / n,
                    })
                    score -= 0.05 / n

            # tool.name 非空
            tool = s.get("tool", {})
            if isinstance(tool, dict) and not tool.get("name", "").strip():
                deductions.append({
                    "step_index": si, "dimension": "structural_completeness",
                    "severity": "medium", "description": "tool.name is empty",
                    "deduction": 0.04 / n,
                })
                score -= 0.04 / n

            # thought 长度 >= 50
            thought = s.get("thought", "")
            if isinstance(thought, str) and len(thought) < 50:
                deductions.append({
                    "step_index": si, "dimension": "structural_completeness",
                    "severity": "medium",
                    "description": f"thought too short ({len(thought)} chars)",
                    "deduction": 0.03 / n,
                })
                score -= 0.03 / n

            # observation 长度 >= 20
            obs = s.get("observation", "")
            if isinstance(obs, str) and len(obs) < 20:
                deductions.append({
                    "step_index": si, "dimension": "structural_completeness",
                    "severity": "medium",
                    "description": f"observation too short ({len(obs)} chars)",
                    "deduction": 0.03 / n,
                })
                score -= 0.03 / n

            # output_state 至少有1个key（decision_summary 为分析性阶段，允许空字典）
            if phase != "decision_summary":
                out = s.get("output_state", {})
                if isinstance(out, dict) and len(out) == 0:
                    deductions.append({
                        "step_index": si, "dimension": "structural_completeness",
                        "severity": "low", "description": "output_state is empty dict",
                        "deduction": 0.02 / n,
                    })
                    score -= 0.02 / n

            # action 枚举合法
            action = s.get("action", "")
            if action and action not in VALID_ACTIONS:
                deductions.append({
                    "step_index": si, "dimension": "structural_completeness",
                    "severity": "low",
                    "description": f"Invalid action '{action}'",
                    "deduction": 0.02 / n,
                })
                score -= 0.02 / n

            # Phase 特定字段
            if phase == "prediction":
                if "error_tag" not in s:
                    deductions.append({
                        "step_index": si, "dimension": "structural_completeness",
                        "severity": "medium", "description": "Missing error_tag field",
                        "deduction": 0.03 / n,
                    })
                    score -= 0.03 / n
                if s.get("valid") is False and not s.get("error_reason"):
                    deductions.append({
                        "step_index": si, "dimension": "structural_completeness",
                        "severity": "high",
                        "description": "valid=False but error_reason is empty",
                        "deduction": 0.05 / n,
                    })
                    score -= 0.05 / n

            if phase == "paper_derivation":
                src = s.get("observation_source")
                if src is not None and src not in VALID_OBSERVATION_SOURCES:
                    deductions.append({
                        "step_index": si, "dimension": "structural_completeness",
                        "severity": "low",
                        "description": f"Invalid observation_source '{src}'",
                        "deduction": 0.03 / n,
                    })
                    score -= 0.03 / n

        return {
            "score": max(score, 0.0),
            "deductions": deductions,
        }

    # ── 维度2: 逻辑一致性 ────────────────────────────────────────────────────

    def _score_logical(self, steps: list[dict], phase: str) -> dict:
        """检查 error_tag/valid/error_reason 三元组、连续同 tool、三段式格式等。"""
        deductions = []
        score = 1.0
        n = max(len(steps), 1)

        for s in steps:
            si = s.get("step_index", "?")

            # error_tag / valid / error_reason 三元组
            et = s.get("error_tag")
            valid = s.get("valid")
            er = s.get("error_reason")

            if et is not None and et != "null":
                if valid is not False:
                    deductions.append({
                        "step_index": si, "dimension": "logical_consistency",
                        "severity": "high",
                        "description": f"error_tag='{et}' but valid is not False",
                        "deduction": 0.08 / n,
                    })
                    score -= 0.08 / n
                if not er or (isinstance(er, str) and len(er) < 10):
                    deductions.append({
                        "step_index": si, "dimension": "logical_consistency",
                        "severity": "high",
                        "description": f"error_tag='{et}' but error_reason missing/too short",
                        "deduction": 0.08 / n,
                    })
                    score -= 0.08 / n

            if valid is False and (et is None or et == "null"):
                deductions.append({
                    "step_index": si, "dimension": "logical_consistency",
                    "severity": "high",
                    "description": "valid=False but error_tag is null",
                    "deduction": 0.08 / n,
                })
                score -= 0.08 / n

            # thought 三段式格式
            thought = s.get("thought", "")
            if isinstance(thought, str):
                for marker in ["[Background]", "[Gap]", "[Decision]"]:
                    if marker.lower() not in thought.lower():
                        deductions.append({
                            "step_index": si, "dimension": "logical_consistency",
                            "severity": "low",
                            "description": f"thought missing '{marker}' marker",
                            "deduction": 0.02 / n,
                        })
                        score -= 0.02 / n

        # 连续同 tool 检测
        for i in range(len(steps) - 1):
            t1 = steps[i].get("tool", {}).get("name", "")
            t2 = steps[i + 1].get("tool", {}).get("name", "")
            if t1 and t2 and t1 == t2:
                a2 = steps[i + 1].get("action", "")
                if a2 != "correction":
                    deductions.append({
                        "step_index": steps[i + 1].get("step_index", "?"),
                        "dimension": "logical_consistency",
                        "severity": "medium",
                        "description": f"Consecutive same tool '{t1}' as previous step",
                        "deduction": 0.06 / n,
                    })
                    score -= 0.06 / n

        # observation_source 一致性
        if phase == "paper_derivation":
            for s in steps:
                src = s.get("observation_source")
                if src is not None and src != "paper":
                    deductions.append({
                        "step_index": s.get("step_index", "?"),
                        "dimension": "logical_consistency",
                        "severity": "medium",
                        "description": f"paper_derivation step has observation_source='{src}' (expected 'paper')",
                        "deduction": 0.05 / n,
                    })
                    score -= 0.05 / n

        if phase == "decision_summary":
            for s in steps:
                src = s.get("observation_source")
                if src is not None and src != "inferred":
                    deductions.append({
                        "step_index": s.get("step_index", "?"),
                        "dimension": "logical_consistency",
                        "severity": "low",
                        "description": f"decision_summary step has observation_source='{src}' (expected 'inferred')",
                        "deduction": 0.03 / n,
                    })
                    score -= 0.03 / n

        return {
            "score": max(score, 0.0),
            "deductions": deductions,
        }

    # ── 维度3: 数值交叉验证 ──────────────────────────────────────────────────

    def _score_numerical(self, steps: list[dict], phase: str,
                         paper_facts: dict | None) -> dict:
        """检查 paper_facts 数值是否出现在轨迹中 / 预测内部数值一致性。"""
        deductions = []
        score = 0.5  # 中性起始
        n = max(len(steps), 1)

        if paper_facts is None:
            paper_facts = {}

        if phase == "paper_derivation":
            # ── 内容覆盖率：方法覆盖 + 公式覆盖 ──
            methods = paper_facts.get("methods", [])
            key_formulas = paper_facts.get("key_formulas", [])

            # 收集 paper_derivation 所有文本
            all_text = ""
            for s in steps:
                all_text += json.dumps(s.get("output_state", {}), ensure_ascii=False) + " "
                all_text += (s.get("observation", "") or "") + " "
            all_text_lower = all_text.lower()

            # 1. 方法覆盖率：论文声明的方法是否在推导步骤中被提及
            method_matches = 0
            for m in methods:
                name = m.get("name", "")
                desc = m.get("desc", "")
                # snake_case → 空格分隔的 tokens
                tokens = [t for t in name.replace("_", " ").lower().split() if len(t) > 2]
                desc_words = re.findall(r'[a-z]{4,}', (desc or "").lower())
                # 任一 token 出现在文本中即视为覆盖
                if tokens and any(t in all_text_lower for t in tokens):
                    method_matches += 1
                elif desc_words and any(w in all_text_lower for w in desc_words):
                    method_matches += 1

            method_score = method_matches / max(len(methods), 1) if methods else 0.5

            # 2. 公式覆盖率：三级匹配（标签引用 / token重叠 / LHS量名）
            STOP_WORDS = {
                'the', 'and', 'for', 'from', 'with', 'where', 'left', 'right',
                'mathrm', 'rm', 'it', 'ex', 'in', 'out', 'to', 'of', 'or', 'is',
                'sp', 'infty', 'partial', 'sum', 'int', 'frac', 'sqrt', 'exp',
                'cos', 'sin', 'ln', 'log', 'lim', 'max', 'min', 'det', 'Tr',
                'begin', 'end', 'array', 'dot', 'ddot', 'bar', 'hat', 'tilde',
            }

            formula_matches = 0.0
            for kf in key_formulas:
                content = kf.get("content", "")
                label = kf.get("label", "")
                if not content:
                    continue

                # Level 1: 标签引用（如 "Eq.(1)" 出现在文本中，权重 1.0）
                label_clean = re.sub(r'\s+', '', label).lower()
                if label_clean and label_clean in all_text_lower:
                    formula_matches += 1.0
                    continue

                # Level 2: token 重叠（权重 0.7）
                plain = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', ' ', content)
                plain = re.sub(r'[\{\}\\^_]', ' ', plain)
                tokens = set(
                    t for t in re.findall(r'[a-zA-Z0-9_]{1,}', plain)
                    if t.strip() and not t.isdigit()
                    and t.lower() not in STOP_WORDS
                )
                if tokens:
                    found = sum(1 for t in tokens if t.lower() in all_text_lower)
                    ratio = found / len(tokens)
                    if ratio >= 0.25:
                        formula_matches += 0.7
                        continue

                # Level 3: LHS 物理量名（权重 0.4）
                if '=' in content:
                    lhs = content.split('=')[0]
                    lhs_clean = re.sub(r'\\[a-zA-Z]+(\{[^}]*\})*', '', lhs)
                    lhs_clean = re.sub(r'[\{\}\\]', '', lhs_clean).strip()
                    lhs_tokens = re.findall(r'[a-zA-Z]{2,}', lhs_clean)
                    if lhs_tokens and any(t.lower() in all_text_lower for t in lhs_tokens):
                        formula_matches += 0.4

            formula_score = (formula_matches / max(len(key_formulas), 1)
                             if key_formulas else 0.5)

            # 综合：基准 0.35 + 方法覆盖率(0.5) + 公式覆盖率(0.5)
            score = 0.35 + 0.65 * (method_score * 0.5 + formula_score * 0.5)

        elif phase == "prediction":
            score = 1.0
            # 按物理量名分组检查数值一致性
            q_groups: dict[str, list[tuple[int, float]]] = {}
            for s in steps:
                out = s.get("output_state", {})
                if isinstance(out, dict):
                    for key, val in out.items():
                        key_norm = re.sub(r'[^a-z0-9]', '', key.lower())
                        try:
                            num = float(str(val).replace(",", ""))
                            if key_norm not in q_groups:
                                q_groups[key_norm] = []
                            q_groups[key_norm].append((s.get("step_index", 0), num))
                        except (ValueError, TypeError):
                            pass

            for key_norm, vals in q_groups.items():
                if len(vals) >= 2:
                    nums_only = [v[1] for v in vals if v[1] != 0]
                    if len(nums_only) >= 2 and min(nums_only) > 0:
                        ratio = max(nums_only) / min(nums_only)
                        if ratio > 2.0:
                            steps_involved = [v[0] for v in vals]
                            deductions.append({
                                "step_index": steps_involved[0],
                                "dimension": "numerical_cross_validation",
                                "severity": "medium",
                                "description": (
                                    f"Quantity '{key_norm}' varies by {ratio:.1f}x "
                                    f"across steps {steps_involved} (possible numeric drift)"
                                ),
                                "deduction": 0.10,
                            })
                            score -= 0.10

        return {
            "score": max(score, 0.2),
            "deductions": deductions,
        }

    # ── 维度4: 文本质量 ──────────────────────────────────────────────────────

    def _score_text_quality(self, steps: list[dict], phase: str) -> dict:
        """检查模板重复、占位符、observation 实质性。"""
        deductions = []
        score = 1.0
        n = max(len(steps), 1)

        # 模板重复检测（相邻步骤 observation Jaccard 相似度）
        for i in range(len(steps) - 1):
            obs1 = steps[i].get("observation", "") or ""
            obs2 = steps[i + 1].get("observation", "") or ""
            sim = jaccard_similarity(obs1, obs2)
            if sim > 0.60:
                deductions.append({
                    "step_index": steps[i + 1].get("step_index", "?"),
                    "dimension": "text_quality",
                    "severity": "low",
                    "description": f"Observation similar to previous step (Jaccard={sim:.2f})",
                    "deduction": 0.05 / n,
                })
                score -= 0.05 / n

        for i in range(len(steps) - 1):
            t1 = steps[i].get("thought", "") or ""
            t2 = steps[i + 1].get("thought", "") or ""
            sim = jaccard_similarity(t1[:200], t2[:200])
            if sim > 0.70:
                deductions.append({
                    "step_index": steps[i + 1].get("step_index", "?"),
                    "dimension": "text_quality",
                    "severity": "low",
                    "description": f"Thought similar to previous step (Jaccard={sim:.2f})",
                    "deduction": 0.03 / n,
                })
                score -= 0.03 / n

        # 占位符检测
        for s in steps:
            si = s.get("step_index", "?")
            obs = s.get("observation", "") or ""
            for pat in PLACEHOLDER_PATTERNS:
                if pat.search(obs):
                    deductions.append({
                        "step_index": si, "dimension": "text_quality",
                        "severity": "medium",
                        "description": f"Observation contains placeholder: '{pat.pattern}'",
                        "deduction": 0.08 / n,
                    })
                    score -= 0.08 / n
                    break

            # 通用过渡语检测
            for pat in GENERIC_PHRASE_PATTERNS:
                if pat.search(obs):
                    deductions.append({
                        "step_index": si, "dimension": "text_quality",
                        "severity": "low",
                        "description": f"Observation starts with generic phrase: '{pat.pattern}'",
                        "deduction": 0.04 / n,
                    })
                    score -= 0.04 / n
                    break

        # observation 平均长度（decision_summary 分析性文本自然较短，阈值降低）
        avg_len = sum(len(s.get("observation", "") or "") for s in steps) / n
        if phase == "decision_summary":
            if avg_len < 20:
                deductions.append({
                    "step_index": 0, "dimension": "text_quality",
                    "severity": "high",
                    "description": f"Average observation length {avg_len:.0f} < 20 chars (too short for decision_summary)",
                    "deduction": 0.12,
                })
                score -= 0.12
            elif avg_len < 35:
                deductions.append({
                    "step_index": 0, "dimension": "text_quality",
                    "severity": "medium",
                    "description": f"Average observation length {avg_len:.0f} < 35 chars",
                    "deduction": 0.05,
                })
                score -= 0.05
        else:
            if avg_len < 30:
                deductions.append({
                    "step_index": 0, "dimension": "text_quality",
                    "severity": "high",
                    "description": f"Average observation length {avg_len:.0f} < 30 chars (too short)",
                    "deduction": 0.15,
                })
                score -= 0.15
            elif avg_len < 60:
                deductions.append({
                    "step_index": 0, "dimension": "text_quality",
                    "severity": "medium",
                    "description": f"Average observation length {avg_len:.0f} < 60 chars",
                    "deduction": 0.07,
                })
                score -= 0.07

        return {
            "score": max(score, 0.0),
            "deductions": deductions,
        }

    # ── 维度5: LLM 语义深度 ──────────────────────────────────────────────────

    def _score_semantic(self, steps: list[dict], phase: str,
                        paper_facts: dict | None, paper_id: str) -> dict:
        """LLM 审核器评估语义质量，含缓存。"""
        if self.skip_llm or len(steps) == 0:
            return {
                "score": 0.5,
                "deductions": [],
                "llm_scores": {},
                "llm_flags": [],
                "llm_rationale": "LLM audit skipped",
            }

        # 缓存 key
        content_hash = hashlib.md5(
            json.dumps([
                [s.get("step_index"), s.get("tool", {}).get("name"),
                 (s.get("thought") or "")[:200], (s.get("observation") or "")[:150]]
                for s in steps
            ], sort_keys=True, ensure_ascii=False).encode()
        ).hexdigest()
        cache_key = f"{paper_id}_{phase}_{content_hash}"

        if cache_key in self._llm_cache:
            cached = self._llm_cache[cache_key]
            return {
                "score": cached.get("score", 0.5),
                "deductions": [],
                "llm_scores": cached.get("llm_scores", {}),
                "llm_flags": cached.get("llm_flags", []),
                "llm_rationale": cached.get("llm_rationale", "(cached)"),
            }

        # 调用 LLM 审核
        user_prompt = _build_auditor_user(phase, steps, paper_facts)
        result = self._call_auditor_llm(AUDITOR_SYSTEM, user_prompt)

        llm_scores = result.get("scores", {})
        if llm_scores:
            # 四个子维度取平均
            avg = sum(llm_scores.values()) / len(llm_scores)
        else:
            avg = 0.5

        llm_flags = result.get("flags", [])
        llm_rationale = result.get("rationale", "")

        # 缓存
        self._llm_cache[cache_key] = {
            "score": avg,
            "llm_scores": llm_scores,
            "llm_flags": llm_flags,
            "llm_rationale": llm_rationale,
        }
        self._save_cache()

        # LLM flags 转为 deductions
        deductions = []
        for flag in llm_flags:
            deductions.append({
                "step_index": flag.get("step", "?"),
                "dimension": "semantic_depth",
                "severity": "low",
                "description": f"[LLM] {flag.get('issue', '?')}: {flag.get('detail', '')}",
                "deduction": 0.02,
            })

        return {
            "score": avg,
            "deductions": deductions,
            "llm_scores": llm_scores,
            "llm_flags": llm_flags,
            "llm_rationale": llm_rationale,
        }

    # ── 维度6: 预测-论文对比价值（仅 decision_summary）─────────────────────

    def _score_contrast(self, ds_steps: list[dict],
                        pred_steps: list[dict],
                        paper_derivation_steps: list[dict]) -> dict:
        """评估 decision_summary 的对比分析质量。"""
        deductions = []
        score = 1.0
        n_ds = max(len(ds_steps), 1)

        # 错误覆盖检测
        error_indices = [
            s.get("step_index") for s in pred_steps
            if s.get("error_tag") not in (None, "null")
        ]

        ds_error_refs = 0
        for ds in ds_steps:
            thought = ds.get("thought", "") or ""
            for ei in error_indices:
                if str(ei) in thought or f"步骤{ei}" in thought or f"step {ei}" in thought.lower():
                    ds_error_refs += 1
                    break

        if len(error_indices) > ds_error_refs:
            missing = len(error_indices) - ds_error_refs
            deductions.append({
                "step_index": 0, "dimension": "prediction_paper_contrast",
                "severity": "high",
                "description": (
                    f"{len(error_indices)} prediction errors but only "
                    f"{ds_error_refs} referenced in decision_summary"
                ),
                "deduction": min(0.30, 0.10 * missing),
            })
            score -= min(0.30, 0.10 * missing)

        # 三要素完整性（仅检查错误分析步骤，merged non-error 步骤使用不同格式）
        TRIAD_MARKERS_CN = ["决策时刻", "错过的信号", "正确的判断"]
        TRIAD_MARKERS_EN = ["decision_point", "missed_signal", "correct_reasoning"]

        for ds in ds_steps:
            si = ds.get("step_index", "?")
            thought = ds.get("thought", "") or ""
            # 仅对引用特定错误步骤的 decision_summary 要求 triad markers
            is_error_ds = any(
                str(ei) in thought or f"步骤{ei}" in thought or f"step {ei}" in thought.lower()
                for ei in error_indices
            )
            if not is_error_ds:
                continue  # merged non-error 步骤，允许使用 [Background][Gap][Decision] 格式
            cn_found = [m for m in TRIAD_MARKERS_CN if m in thought]
            en_found = [m for m in TRIAD_MARKERS_EN if m.lower() in thought.lower()]
            # 中文匹配优先；要求至少 2/3 标记出现（容忍 LLM 输出的微小措辞变化）
            best_found = max(len(cn_found), len(en_found))
            if best_found < 2:
                missing_cn = [m for m in TRIAD_MARKERS_CN if m not in thought]
                deductions.append({
                    "step_index": si, "dimension": "prediction_paper_contrast",
                    "severity": "medium",
                    "description": f"Decision step missing triad elements (found {best_found}/3): {missing_cn}",
                    "deduction": 0.06 / n_ds,
                })
                score -= 0.06 / n_ds

        # overall_lesson 检查（仅当 prediction 有错误步骤时要求有教训可学）
        if len(error_indices) > 0:
            has_lesson = False
            lesson_quality = False
            for ds in ds_steps:
                lesson = ds.get("overall_lesson", "")
                if lesson and isinstance(lesson, str) and len(lesson) >= 50:
                    has_lesson = True
                    lesson_quality = True
                elif lesson and isinstance(lesson, str) and len(lesson) > 0:
                    has_lesson = True

            if not has_lesson:
                deductions.append({
                    "step_index": 0, "dimension": "prediction_paper_contrast",
                    "severity": "high",
                    "description": f"{len(error_indices)} prediction errors but no overall_lesson in decision_summary",
                    "deduction": 0.30,
                })
                score -= 0.30
            elif not lesson_quality:
                deductions.append({
                    "step_index": 0, "dimension": "prediction_paper_contrast",
                    "severity": "medium",
                    "description": "overall_lesson exists but too short (< 50 chars)",
                    "deduction": 0.15,
                })
                score -= 0.15

        return {
            "score": max(score, 0.0),
            "deductions": deductions,
        }

    # ── 评分编排 ──────────────────────────────────────────────────────────────

    def score_phase(self, steps: list[dict], phase: str,
                    paper_facts: dict | None, paper_id: str,
                    all_pred_steps: list[dict] | None = None,
                    all_paper_steps: list[dict] | None = None) -> dict:
        """对单个 phase 的所有维度打分，返回加权总分。"""
        dims = {}
        weighted_total = 0.0
        weights = WEIGHTS_DECISION if phase == "decision_summary" else WEIGHTS_PRED_PAPER

        # 结构完整性
        dims["structural_completeness"] = self._score_structural(steps, phase)

        # 逻辑一致性
        dims["logical_consistency"] = self._score_logical(steps, phase)

        # 数值交叉验证
        dims["numerical_cross_validation"] = self._score_numerical(
            steps, phase, paper_facts
        )

        # 文本质量
        dims["text_quality"] = self._score_text_quality(steps, phase)

        # 语义深度（LLM）
        dims["semantic_depth"] = self._score_semantic(
            steps, phase, paper_facts, paper_id
        )

        # 预测-论文对比价值（仅 decision_summary）
        if phase == "decision_summary" and all_pred_steps is not None:
            dims["prediction_paper_contrast"] = self._score_contrast(
                steps, all_pred_steps, (all_paper_steps or [])
            )
        elif phase == "decision_summary":
            dims["prediction_paper_contrast"] = {"score": 0.5, "deductions": []}

        # 加权汇总
        for dim_name, w in weights.items():
            if dim_name in dims:
                s = dims[dim_name]["score"]
                dims[dim_name]["weight"] = w
                dims[dim_name]["weighted"] = s * w
                weighted_total += s * w

        return {
            "score": round(weighted_total, 4),
            "step_count": len(steps),
            "dimensions": dims,
        }

    # ── 单篇审核 ──────────────────────────────────────────────────────────────

    def audit_paper(self, paper_path: Path, paper_data: dict) -> dict:
        """审核单篇论文，返回完整评分报告。"""
        paper_id = paper_data.get("id", paper_path.stem)
        traj = paper_data.get("02_agent_trajectory", [])
        paper_facts = paper_data.get("paper_facts", {})

        # 按 phase 分组
        pred_steps = [s for s in traj if s.get("phase") == "prediction"]
        paper_steps = [s for s in traj if s.get("phase") == "paper_derivation"]
        ds_steps = [s for s in traj if s.get("phase") == "decision_summary"]

        phase_scores = {}

        if pred_steps:
            phase_scores["prediction"] = self.score_phase(
                pred_steps, "prediction", paper_facts, paper_id
            )

        if paper_steps:
            phase_scores["paper_derivation"] = self.score_phase(
                paper_steps, "paper_derivation", paper_facts, paper_id
            )

        if ds_steps:
            phase_scores["decision_summary"] = self.score_phase(
                ds_steps, "decision_summary", paper_facts, paper_id,
                all_pred_steps=pred_steps, all_paper_steps=paper_steps
            )

        # 整体分数（各 phase 等权）
        if phase_scores:
            overall = sum(ps["score"] for ps in phase_scores.values()) / len(phase_scores)
        else:
            overall = 0.0

        tier = self._classify_tier(overall, phase_scores)

        # 收集所有扣分项
        all_deductions = []
        for phase, ps in phase_scores.items():
            for dim_name, dim in ps.get("dimensions", {}).items():
                for d in dim.get("deductions", []):
                    d["phase"] = phase
                    all_deductions.append(d)

        return {
            "paper_id": paper_id,
            "file_path": str(paper_path.resolve().relative_to(PROJECT_ROOT.resolve())),
            "subdomain": paper_data.get("meta", {}).get("subdomain", "unknown"),
            "overall_score": round(overall, 4),
            "tier": tier,
            "phase_scores": phase_scores,
            "all_deductions": all_deductions,
        }

    def _classify_tier(self, overall: float,
                       phase_scores: dict[str, dict]) -> str:
        """根据总分和各 phase 最低分分类。"""
        ps = {k: v["score"] for k, v in phase_scores.items()}
        phase_floor = min(ps.values()) if ps else 0.0

        if overall >= 0.90 and phase_floor >= 0.85:
            return "GOLD"
        if overall >= 0.75 and phase_floor >= 0.70:
            return "SILVER"
        if overall >= 0.60:
            return "BRONZE"
        return "REJECT"

    # ── 批量运行 ──────────────────────────────────────────────────────────────

    def run(self, target_paper: str | None = None,
            subdomain: str | None = None,
            folder: str | None = None,
            limit: int = 0,
            reaudit: bool = False) -> dict:
        """扫描目录、审核论文、生成报告。"""
        # 加载论文
        papers: list[tuple[Path, dict]] = []

        if folder:
            dirs = [Path(folder).resolve()]
        elif subdomain:
            dirs = [PAPERS_DIR / subdomain]
        else:
            dirs = RESEARCH_DIRS

        for d in dirs:
            if not d.exists():
                continue
            for fpath in sorted(d.glob("*_v2.json")):
                try:
                    data = json.loads(fpath.read_text(encoding="utf-8"))
                except Exception:
                    continue
                if not data.get("02_agent_trajectory"):
                    continue
                if target_paper and data.get("id") != target_paper:
                    continue
                papers.append((fpath, data))

        if target_paper and not papers:
            print(f"[!] Paper '{target_paper}' not found")
            return {}

        if limit > 0:
            papers = papers[:limit]

        print(f"[*] Found {len(papers)} papers to audit"
              f"{' (LLM audit enabled)' if not self.skip_llm else ' (rules only)'}")
        if reaudit:
            self._llm_cache.clear()
            print("[*] LLM cache cleared")

        results = {}
        tier_counts = {"GOLD": 0, "SILVER": 0, "BRONZE": 0, "REJECT": 0}

        for idx, (fpath, data) in enumerate(papers, 1):
            paper_id = data.get("id", fpath.stem)
            print(f"  [{idx}/{len(papers)}] {paper_id} ...", end=" ", flush=True)

            result = self.audit_paper(fpath, data)
            results[paper_id] = result

            tier = result["tier"]
            tier_counts[tier] += 1
            phases_str = ", ".join(
                f"{p}={result['phase_scores'][p]['score']:.2f}"
                for p in result["phase_scores"]
            )
            print(f"[{tier}] overall={result['overall_score']:.2f} ({phases_str})")

        # 汇总统计
        all_overall = [r["overall_score"] for r in results.values()]
        avg_overall = sum(all_overall) / len(all_overall) if all_overall else 0.0

        phase_totals: dict[str, list[float]] = {}
        for r in results.values():
            for phase, ps in r["phase_scores"].items():
                if phase not in phase_totals:
                    phase_totals[phase] = []
                phase_totals[phase].append(ps["score"])

        phase_avgs = {
            p: sum(vs) / len(vs) for p, vs in phase_totals.items()
        }

        # 维度平均
        dim_totals: dict[str, list[float]] = {}
        for r in results.values():
            for ps in r["phase_scores"].values():
                for dim_name, dim in ps.get("dimensions", {}).items():
                    if dim_name not in dim_totals:
                        dim_totals[dim_name] = []
                    dim_totals[dim_name].append(dim["score"])

        dim_avgs = {
            d: sum(vs) / len(vs) for d, vs in dim_totals.items()
        }

        report = {
            "$schema": "audit_quality_report_v1",
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "config": {
                "script": "audit_quality.py",
                "deepseek_model": "deepseek-chat",
                "auditor_temperature": 0.1,
                "llm_audit_enabled": not self.skip_llm,
                "weight_tables": {
                    "prediction_paper_derivation": WEIGHTS_PRED_PAPER,
                    "decision_summary": WEIGHTS_DECISION,
                },
            },
            "summary": {
                "total_audited": len(results),
                "tier_counts": tier_counts,
                "average_overall_score": round(avg_overall, 4),
                "phase_averages": {k: round(v, 4) for k, v in phase_avgs.items()},
                "dimension_averages": {k: round(v, 4) for k, v in dim_avgs.items()},
            },
            "papers": results,
        }

        return report


# ── 入口 ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Quality auditor for Sci-Evo Research layer _v2.json files"
    )
    parser.add_argument("--paper", type=str, default=None,
                        help="Audit a single paper by ID (e.g., NPP_0001)")
    parser.add_argument("--subdomain", type=str, default=None,
                        help="Audit papers from a specific subdomain folder")
    parser.add_argument("--folder", type=str, default=None,
                        help="Audit papers from a custom folder path")
    parser.add_argument("--limit", type=int, default=0,
                        help="Max papers to audit (default: 0 = all)")
    parser.add_argument("--skip-llm", action="store_true",
                        help="Skip LLM semantic auditor (rules-only mode)")
    parser.add_argument("--output", type=str, default=None,
                        help="Output report path (default: agent_Review/audit_quality_report.json)")
    parser.add_argument("--reaudit", action="store_true",
                        help="Ignore LLM cache and re-run all LLM audits")
    args = parser.parse_args()

    output_path = args.output or str(
        PROJECT_ROOT / "agent_Review" / "audit_quality_report.json"
    )

    auditor = QualityAuditor(skip_llm=args.skip_llm)
    report = auditor.run(
        target_paper=args.paper,
        subdomain=args.subdomain,
        folder=args.folder,
        limit=args.limit,
        reaudit=args.reaudit,
    )

    if report:
        Path(output_path).write_text(
            json.dumps(report, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"\n[*] Report written to: {output_path}")

        summary = report["summary"]
        print(f"\n{'='*60}")
        print(f"Audit Summary: {summary['total_audited']} papers")
        print(f"  Tier distribution: {summary['tier_counts']}")
        print(f"  Average score: {summary['average_overall_score']:.3f}")
        if summary.get("phase_averages"):
            print(f"  Phase averages: {summary['phase_averages']}")
        print(f"{'='*60}")


if __name__ == "__main__":
    main()
