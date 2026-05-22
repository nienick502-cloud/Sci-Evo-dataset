"""
sci_evo_agent.py - Sci-Evo 生成 Agent（DFS 约束版）

从论文 markdown 出发，生成完整的 Research 层 JSON（prediction + paper_derivation）。
核心机制：逐步生成 + DFS 约束验证 + 决策剪枝。

用法:
  python agent_Review/sci_evo_agent.py --paper "raw_dataset/papers/alpha   WKB/arxiv_0708.4355.json"
  python agent_Review/sci_evo_agent.py --folder "alpha   WKB" --limit 3

依赖:
  - core_tool_library_v2.json (62 原子 tool)
  - dfs_engine.py (DFS 搜索引擎)
  - step_classifier.py (步骤分类器)
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import time
from pathlib import Path

import openai

from dfs_engine import DFSEngine
from step_classifier import StepClassifier
from reasoning_formatter import ReasoningFormatter
from crystal_rule_manager import CrystalRuleManager

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PAPERS_DIR = PROJECT_ROOT / "raw_dataset" / "papers"
PARSED_DIR = PROJECT_ROOT / "parsed" / "papers"
ML_LIBRARY_PATH = PROJECT_ROOT / "agent_Review" / "core_tool_library_ml.json"

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")

# ── Tool 名映射：Research 层常见 tool 名 → 核心库 tool_id ──────────────────────
TOOL_NAME_MAP = {
    # === 核心库自身映射 ===
    "nuclear_radius_estimation": "T01", "shell_model_filling": "T02",
    "bethe_weizsacker_mass_formula": "T03", "Q_value_calculation": "T04",
    "mean_field_density_calculation": "T05", "deformation_parameter_extraction": "T06",
    "pairing_correlation_BCS": "T07", "woods_saxon_parameterization": "T08",
    "double_folding_integral": "T09", "NN_effective_interaction": "T10",
    "coulomb_potential_calculation": "T11", "centrifugal_potential_construction": "T12",
    "effective_potential_assembly": "T13", "proximity_potential_calculation": "T14",
    "liquid_drop_potential": "T15", "optical_potential_construction": "T16",
    "deformation_potential_correction": "T17", "turning_point_solver": "T18",
    "WKB_action_integral": "T19", "penetrability_from_action": "T20",
    "preformation_factor_model": "T21", "assault_frequency_calculation": "T22",
    "decay_width_formula": "T23", "halflife_from_width": "T24",
    "empirical_halflife_formula": "T25", "cluster_formation_probability": "T26",
    "R_matrix_decay_width": "T27", "schrodinger_equation_solver": "T28",
    "partial_wave_expansion": "T29", "cross_section_from_amplitude": "T30",
    "optical_model_fitting": "T31", "reaction_cross_section_calculation": "T32",
    "transmission_coefficient_from_potential": "T33",
    "folding_model_optical_potential": "T34", "dispersive_optical_model": "T35",
    "feature_engineering": "T36", "training_data_preparation": "T37",
    "neural_network_training": "T38", "model_prediction": "T39",
    "cross_validation_evaluation": "T40", "bayesian_uncertainty_quantification": "T41",
    "numerical_integration": "T42", "eigenvalue_solver": "T43",
    "chi_squared_minimization": "T44", "matrix_element_calculation": "T45",
    "experimental_comparison": "T46", "systematic_trend_analysis": "T47",
    "dimensional_analysis_check": "T48", "limiting_case_verification": "T49",
    "macroscopic_microscopic_method": "T50", "shell_correction_strutinsky": "T51",
    "cranking_inertia_calculation": "T52", "RGM_cluster_wave_function": "T53",
    "THSR_wave_function": "T54", "spectroscopic_factor_extraction": "T55",
    "Wildermuth_condition": "T56", "statistical_model_decay": "T57",
    "QRPA_transition_strength": "T58", "coupled_channel_calculation": "T59",
    "Brueckner_G_matrix": "T60", "no_core_shell_model": "T61",
    "interacting_boson_model": "T62",
    # === Research 层常见别名 ===
    "wkb_approximation": "T19", "WKB_approximation": "T19",
    "WKB_framework": "T19", "wkb_barrier_penetration": "T19",
    "double_folding_model": "T09", "double_folding": "T09",
    "double_folding_potential": "T09", "double_folding_procedure": "T09",
    "generalized_liquid_drop_model": "T15", "GLDM": "T15",
    "liquid_drop_model": "T15", "Generalized_Liquid_Drop_Model": "T15",
    "optical_model": "T16", "optical_potential_method": "T16",
    "optical_model_calculation": "T16", "optical_model_potential": "T16",
    "shell_filling": "T02", "shell_model": "T02",
    "relativistic_mean_field": "T05", "hartree_fock_bogoliubov": "T05",
    "RMF_plus_BCS": "T05", "mean_field": "T05",
    "cluster_formation_model": "T26", "alpha_cluster_model": "T26",
    "preformed_cluster_model": "T21", "preformed_cluster_decay_model": "T21",
    "viola_seaborg_formula": "T25",
    "Geiger_Nuttall": "T25", "royer_empirical_formula": "T25",
    "cross_section_calculation": "T30",
    "proximity_potential": "T14", "proximity_potential_formalism": "T14",
    "bcs_method": "T07", "BCS_theory": "T07",
    "numerical_computation": "T42",
    "artificial_neural_network": "T38", "neural_network": "T38",
    "multilayer_perceptron": "T38", "bayesian_neural_network": "T41",
    # === ML DFS 库映射（M01-M14）===
    "ml_data_acquisition": "M01",
    "ml_feature_construction": "M02",
    "ml_model_selection": "M03",
    "ml_neural_network_training": "M04",
    "ml_tree_ensemble_training": "M05",
    "ml_gaussian_process_training": "M06",
    "ml_bayesian_inference": "M07",
    "ml_physics_informed_training": "M08",
    "ml_transfer_learning": "M09",
    "ml_model_evaluation": "M10",
    "ml_direct_prediction": "M11",
    "ml_physics_hybrid_correction": "M12",
    "ml_ensemble_prediction": "M13",
    "ml_feature_importance_analysis": "M14",
}


# ── Phase 1: 论文理解 Prompt ─────────────────────────────────────────────────

PHASE1_SYSTEM = """\
你是核物理论文分析专家。从论文内容中提取结构化信息。

输出严格 JSON：
{
  "target": "目标物理量（用英文 snake_case，如 half_life, cross_section）",
  "initial_conditions": ["初始可用物理量列表，如 mass_number_A, charge_number_Z"],
  "premises": {
    "definitions": ["论文中的定义/符号约定"],
    "assumptions": ["论文中的物理假设"],
    "experimental_facts": ["引用的实验事实"]
  },
  "paper_methods": ["论文使用的物理方法名列表（英文 snake_case）"],
  "paper_facts": {
    "methods": [{"name": "方法名", "desc": "一句话描述"}],
    "key_formulas": [{"label": "公式编号", "content": "LaTeX"}],
    "key_results": [{"quantity": "物理量", "value": "数值", "condition": "条件"}],
    "failure_points": ["论文明确指出不足、失败或被改进的方法名（英文 snake_case）"]
  }
}

规则：
- target 必须是以下之一：half_life, cross_section, binding_energy, alpha_decay_width, penetrability, nuclear_potential, prediction_output
- initial_conditions 从以下选择：mass_number_A, charge_number_Z, neutron_number_N, nuclear_radius, nucleon_density, deformation_parameter, Q_value

提取规则（严格遵守）：
- key_formulas：必须提取至少2个核心公式
  - 从 Method/Formalism/Results 章节中提取论文的标志性公式
  - label 用论文中的公式编号（如 Eq.(1)），content 用 LaTeX
  - 如果论文纯数值/图表为主，提取参数化公式或拟合公式
- key_results：必须提取至少2个关键数值结果
  - 优先提取与目标物理量直接相关的数值（半衰期、截面、结合能等）
  - condition 注明核素范围或能量条件
  - 如果论文给出系统趋势而非单点值，描述趋势方向和量级
- key_formulas 和 key_results 不允许同时为空数组
- failure_points：提取论文中明确批评、否定或指出局限性的方法/模型
  - 只提取论文明确指出的（如 "XX method fails for..."、"YY model overestimates..."）
  - 方法名用英文 snake_case（如 liquid_drop_model, optical_model_fitting）
  - 如果没有明确的批评或否定，返回空数组 []
- 只输出 JSON"""


# ── Phase 3: 逐步生成 Prompt ─────────────────────────────────────────────────

PHASE3_SYSTEM_TEMPLATE = """\
你是核物理专家。你正在逐步生成物理推导轨迹。

## 当前合法推导路径（严格推导步骤必须在这些路径上）

{valid_paths_text}

## 可用原子工具（tool.name 必须从此列表中选择）

核结构: nuclear_radius_estimation, shell_model_filling, bethe_weizsacker_mass_formula, Q_value_calculation, mean_field_density_calculation, deformation_parameter_extraction, pairing_correlation_BCS
势能构建: woods_saxon_parameterization, double_folding_integral, NN_effective_interaction, coulomb_potential_calculation, centrifugal_potential_construction, effective_potential_assembly, proximity_potential_calculation, liquid_drop_potential, optical_potential_construction, deformation_potential_correction
隧穿衰变: turning_point_solver, WKB_action_integral, penetrability_from_action, preformation_factor_model, assault_frequency_calculation, decay_width_formula, halflife_from_width, empirical_halflife_formula, cluster_formation_probability, R_matrix_decay_width
散射: schrodinger_equation_solver, partial_wave_expansion, cross_section_from_amplitude, optical_model_fitting, reaction_cross_section_calculation, transmission_coefficient_from_potential, folding_model_optical_potential, dispersive_optical_model
机器学习: feature_engineering, training_data_preparation, neural_network_training, model_prediction, cross_validation_evaluation, bayesian_uncertainty_quantification
{ml_tools_section}
数学: numerical_integration, eigenvalue_solver, chi_squared_minimization, matrix_element_calculation
验证: experimental_comparison, systematic_trend_analysis, dimensional_analysis_check, limiting_case_verification
多体: macroscopic_microscopic_method, shell_correction_strutinsky, cranking_inertia_calculation, RGM_cluster_wave_function, THSR_wave_function, spectroscopic_factor_extraction, Wildermuth_condition, statistical_model_decay, QRPA_transition_strength, coupled_channel_calculation, Brueckner_G_matrix, no_core_shell_model, interacting_boson_model

## 规则

1. 每次只生成 1 个步骤
2. tool.name 必须从上面的列表中选择，不能自创工具名
3. 每步必须包含以下字段：
   - step_index: 步骤编号
   - thought: [Background]...[Gap]...[Decision]... 三段式
   - action: symbolic_derivation | numerical_computation | approximation | verification | rule_application | model_building | correction
   - tool: {{"name": "从上面列表选", "version": ""}}
   - parameters: {{}}
   - output_state: {{"物理量名": "表达式或描述"}}
   - observation: "该步骤的结果"
   - valid: true

3. 你可以生成以下类型的步骤：
   - 严格推导（必须沿合法路径前进，tool 必须是路径上的工具）
   - 引用文献结果（自由选 tool）
   - 经验近似（自由选 tool）
   - 物理论证/模型选择/对称性约束（自由，但不能与合法路径矛盾）
   - 数值计算/拟合（自由选 tool）

4. 当你认为已经达到目标物理量时，在 observation 中写 "[DONE]"
5. LaTeX 公式中的反斜杠必须写成双反斜杠（如 \\\\hbar, \\\\frac）

## 输出格式
严格输出单个步骤的 JSON 对象（不是数组）。只输出 JSON。"""


PHASE3_USER_TEMPLATE = """\
{phase_label}

前提层:
  定义: {definitions}
  假设: {assumptions}
  实验事实: {experimental_facts}

目标: {target}
初始条件: {initial_conditions}
论文方法: {paper_methods}

已生成步骤:
{previous_steps}

请生成第 {next_step_index} 步。"""


# ── Phase 4: Error Analysis & Decision Summary Prompts ─────────────────────────

ERROR_ANALYSIS_PROMPT = """\
你是一个核物理专家。你的任务是对比"模型预测的推理步骤"和"论文实际的推导步骤"，
找出预测中在物理推理上出错的地方。

## 核心原则：只标注物理推理错误，不标注信息差异

- 预测中公式参数与论文不同 → 如果物理逻辑正确，这是信息差异，不是错误，标 null
- 预测中使用了论文未用的近似 → 如果该近似在物理上合理，标 null
- 预测中缺少论文有的一步 → 如果预测的逻辑链自洽，标 null（不是每个差异都是错误）

## 错误标签枚举

对每个预测步骤，选择最匹配的标签：
- null — 无物理推理错误
- "wrong_approximation"      — 使用了在该物理情境下不适用的近似
- "missing_physical_effect"   — 忽略了一个不可忽略的物理效应
- "incorrect_derivation"      — 推导过程有数学/逻辑错误
- "wrong_parameter_choice"    — 选择了错误的参数或变量
- "over_simplification"       — 过度简化，丢失了关键物理结构
- "wrong_physical_interpretation" — 对物理量的理解或解释有误

## error_reason 要求

当 error_tag 不为 null 时，error_reason 必须：
- 说明**为什么这个推理在物理上站不住**
- 不只是"论文的做法不同"
- 要指出具体的物理机制或原理上的错误

## 输出格式（严格 JSON，LaTeX 反斜杠写成双反斜杠 \\\\）

{
  "error_tags": [
    {"step_index": 1, "error_tag": null, "error_reason": null},
    {"step_index": 2, "error_tag": "wrong_approximation",
     "error_reason": "具体物理理由..."},
    ...
  ]
}

## 重要：关于 null 标签和 over_simplification

如果所有预测步骤的物理推理都是合理的（即使与论文做法不完全一致），
全部返回 null 是完全正确的做法。不要为了"找到一个错误"而过度标注。

over_simplification 标签应保留用于预测确实丢失了关键物理结构的场景
（例如忽略了主导阶项、将强耦合系统当作弱耦合处理、数学简化破坏了守恒律），
而不是仅仅因为"预测比论文的推导更简洁"就标注。

只输出 JSON，不要任何解释文字。"""

DECISION_SUMMARY_PROMPT = """\
你是一个核物理专家，擅长分析物理推理中的决策失误。
你的任务是：基于预测步骤的错误标注，总结出错的**决策根因**。

## 核心要求：不要写马后炮

不要写"如果读过论文就不会犯这个错"——那是废话。
要回答的是：**在推理的那个时刻，有什么物理信号本应该提醒你换一种做法？**

## 在写每个决策点之前，必须完成以下三步思考（不输出，仅内部推理）

1. **时间线锚定**：错误发生在第X步。在此步骤之前，你已经知道什么？
   - 只能引用：前 X-1 步的 observation 内容、input_data 中给定的条件、教科书级别的物理常识
   - 禁止引用：论文后续步骤的内容、论文的关键结果、任何需要"读了论文才知道"的信息

2. **信号扫描**：在决策时刻可用的信息中，有什么本应触发警觉？
   - 物理量级是否进入了方法的失效区？（如 WKB 在 Q≈V_barrier 时不适用）
   - 已知条件是否暗示了被忽略的物理效应？（如高 Z 核暗示了显著的库仑修正）
   - 假设是否与已知的系统学趋势矛盾？（如轻核区用液滴模型本应三思）

3. **决策重演**：面对第2步识别的信号，一个经验丰富的核物理学家会：
   - 在继续之前先做什么检查？
   - 考虑哪些替代方法？
   - 用什么样的量级估算来验证当前方法的适用性？

## 每个错误决策点必须包含三个要素

1. **决策时刻**（decision_point）：推理过程中的哪个步骤、做了什么选择。
   格式："步骤X：[做了什么选择]，当时已知的条件包括[列出关键已知量]"

2. **错过的信号**（missed_signal）：有什么已知的物理事实（不需要读论文就能知道）本应提示重新考虑。
   格式："[物理信号]，在决策时已知因为[为什么已知]，本应触发[什么警觉]"
   反例（禁止）："论文实际使用了X方法"（这是事后信息，不是决策时已知的信号）

3. **正确的判断方式**（correct_reasoning）：面对同样的信息，一个经验丰富的物理学家会怎么思考。
   格式："面对[条件A]和[条件B]，应首先检查[什么]，如果[条件]，则[行动]"
   要求：必须可转化为"如果...就..."规则

## tool_name 选择

每个决策点必须选择一个最匹配的验证工具：
- "physical_intuition_check" — 错误源于对物理图像/机制的误判（如忽略了某个效应的量级）
- "limiting_case_check" — 错误源于未检查近似的适用边界或极限情况（如 WKB 条件不满足）
- "dimensional_analysis" — 错误源于量纲、量级或单位上的疏忽

## 输出格式（严格 JSON，LaTeX 反斜杠写成双反斜杠 \\\\）

{
  "decision_summary": [
    {
      "decision_point": "步骤X：[什么选择]，已知条件：[列出]",
      "missed_signal": "[物理信号]，决策时已知因为[理由]",
      "correct_reasoning": "面对[条件]，应检查[什么]，如果[条件]则[行动]",
      "root_cause": "一句话根因：推理过程中跳过了哪个检查步骤",
      "tool_name": "physical_intuition_check | limiting_case_check | dimensional_analysis"
    }
  ],
  "overall_lesson": "一两句话总结这篇论文揭示的物理推理教训，必须可泛化到其他类似问题"
}

只输出 JSON，不要任何解释文字。"""


# ── 辅助函数 ──────────────────────────────────────────────────────────────────

def _get_git_commit() -> str:
    """获取当前 git commit 7 位短 hash"""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--short=7", "HEAD"],
            capture_output=True, text=True, cwd=PROJECT_ROOT
        )
        return result.stdout.strip() if result.returncode == 0 else "unknown"
    except Exception:
        return "unknown"


# ── 数值质量检查 ──────────────────────────────────────────────────────────────

def _is_numerical_value(val) -> bool:
    """检查值是否看起来是数值（含数字且不是纯定性短语）。"""
    if not val or not isinstance(val, str):
        return False
    val_clean = val.strip()
    if not val_clean:
        return False
    # 以定性前缀开头的非数值字符串
    _NON_NUMERICAL_PREFIXES = [
        r'^found\s', r'^very\s', r'^as\s', r'^shown\s', r'^see\s',
        r'^cf\.?\s', r'^Table\s', r'^Figure\s', r'^Eq\.?\s', r'^Ref\.?\s',
        r'^approximately\s', r'^about\s', r'^roughly\s', r'^nearly\s',
        r'^almost\s', r'^around\s', r'^on the order of\s',
    ]
    for pat in _NON_NUMERICAL_PREFIXES:
        if re.match(pat, val_clean, re.IGNORECASE):
            return False
    # 必须包含至少一个数字
    return bool(re.search(r'\d', val_clean))


# ── Agent 主类 ────────────────────────────────────────────────────────────────

class SciEvoAgent:
    """Sci-Evo 生成 Agent"""

    # ── ML 方法检测关键词 ─────────────────────────────────────────────
    ML_KEYWORDS: set[str] = set()

    def __init__(self):
        self.dfs = DFSEngine()
        self.classifier = StepClassifier()
        self.client = openai.OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url="https://api.deepseek.com"
        )
        self._ml_loaded = False
        self.formatter = ReasoningFormatter()
        self._crystal_manager = None  # Injected by main() for --folder mode

    # ── ML 方法检测 ───────────────────────────────────────────────────

    @classmethod
    def _load_ml_keywords(cls):
        """从 ML 库文件加载 ML 检测关键词（只做一次，类级缓存）。"""
        if cls.ML_KEYWORDS:
            return
        ml_lib_path = ML_LIBRARY_PATH
        if not ml_lib_path.exists():
            return
        try:
            lib = json.loads(ml_lib_path.read_text(encoding="utf-8"))
            keywords_dict = lib.get("ml_method_keywords", {})
            for kw_list in keywords_dict.values():
                cls.ML_KEYWORDS.update(kw_list)
        except Exception:
            pass

    # ── ML 子串检测的根词（检测更灵活）──────────────────────────────
    ML_ROOT_WORDS: set[str] = set()

    @classmethod
    def _load_ml_root_words(cls):
        """加载 ML 检测根词（只做一次）。比完整关键词更灵活，用子串匹配。"""
        if cls.ML_ROOT_WORDS:
            return
        cls.ML_ROOT_WORDS = {
            "neural_network", "deep_network", "convolutional",
            "bayesian_neural", "bnn", "physics_informed",
            "gradient_boosting", "lightgbm", "xgboost", "catboost",
            "random_forest", "decision_tree", "gbdt",
            "gaussian_process", "kernel_ridge",
            "support_vector", "svr", "svm",
            "machine_learning", "deep_learning", "supervised_learning",
            "data_driven", "ml_based",
            "transfer_learning", "fine_tuning", "pretrained",
            "ensemble_learning", "voting_classifier",
            "autoencoder", "variational_autoencoder", "vae",
            "multilayer_perceptron", "mlp",
            "feedforward", "backpropagation",
            "cross_validation", "k_fold",
            "markov_chain_monte", "mcmc",
            "bayesian", "bayesian_inference", "bayesian_model",
            "bayesian_probability", "bayesian_theorem",
            "dropout", "regularization",
            "feature_engineering", "feature_selection",
            "hyperparameter", "grid_search",
            # CNN / image models
            "resnet", "densenet", "cnn", "mobilenet", "efficientnet",
            # Optimizers (ML-specific)
            "adam_optim", "stochastic_gradient",
            "rmsprop",
            # Loss functions
            "cross_entropy", "mean_squared_error",
            # Data augmentation / balancing
            "randaugment", "over_sampling", "data_augmentation",
            # Neural quantum states (quantum-inspired ML)
            "neural_quantum", "feynmannet",
            # Embedding / representation learning
            "embedding", "representation_learning",
            # Training protocols
            "alternating_training", "co_training",
        }

    @staticmethod
    def _has_ml_methods(paper_methods: list[str]) -> bool:
        """检测 paper_methods 中是否包含 ML 方法，决定是否激活 ML DFS。

        采用双层匹配：
        1. 精确关键词匹配（ml_method_keywords 完整词条）
        2. 子串匹配（ML_ROOT_WORDS 作为子串出现在 method 名中）
        """
        if not paper_methods:
            return False
        SciEvoAgent._load_ml_keywords()
        SciEvoAgent._load_ml_root_words()
        if not SciEvoAgent.ML_KEYWORDS and not SciEvoAgent.ML_ROOT_WORDS:
            return False

        methods_lower = {m.lower().replace("-", "_").replace(" ", "_") for m in paper_methods}

        # Layer 1: 精确关键词匹配
        if methods_lower & SciEvoAgent.ML_KEYWORDS:
            return True

        # Layer 2: 子串匹配（根词出现在 method 名中）
        for method in methods_lower:
            for root in SciEvoAgent.ML_ROOT_WORDS:
                if root in method:
                    return True

        return False

    @staticmethod
    def _get_ml_tools_prompt_section() -> str:
        """返回 ML 专用工具列表，注入到 Phase 3 system prompt 中。"""
        return (
            "ML数据工程: ml_data_acquisition, ml_feature_construction\n"
            "ML模型选择: ml_model_selection\n"
            "ML训练: ml_neural_network_training, ml_tree_ensemble_training, "
            "ml_gaussian_process_training, ml_bayesian_inference, "
            "ml_physics_informed_training, ml_transfer_learning\n"
            "ML评估: ml_model_evaluation, ml_feature_importance_analysis\n"
            "ML预测: ml_direct_prediction, ml_physics_hybrid_correction, ml_ensemble_prediction"
        )

    def run(self, paper_json_path: Path, parsed_md_path: Path | None = None) -> dict:
        """
        对单篇论文运行完整 pipeline。

        Returns:
            完整的 Research 层 JSON dict
        """
        # 加载现有 JSON
        paper = json.loads(paper_json_path.read_text(encoding="utf-8"))
        paper_id = paper.get("id", paper_json_path.stem)
        print(f"\n[{paper_id}] Starting Sci-Evo Agent...")

        # 加载论文 markdown（如果有）
        md_content = ""
        if parsed_md_path and parsed_md_path.exists():
            md_content = parsed_md_path.read_text(encoding="utf-8")[:8000]

        # Phase 1: 论文理解
        print(f"  [Phase 1] Extracting paper structure...")
        extraction = self._phase1_extract(paper, md_content)

        # ML 方法检测：如果论文涉及 ML，加载 ML DFS 库（双轨架构）
        paper_methods = extraction.get("paper_methods", [])
        has_ml = self._has_ml_methods(paper_methods)
        if has_ml and not self._ml_loaded:
            n_ml = self.dfs.load_auxiliary_library(ML_LIBRARY_PATH)
            self._ml_loaded = True
            print(f"  [ML-DFS] Loaded {n_ml} ML tools (detected ML methods: "
                  f"{[m for m in paper_methods if m.lower().replace('-','_').replace(' ','_') in self.ML_KEYWORDS][:3]})")

        # Phase 2: DFS 路径搜索
        print(f"  [Phase 2] DFS path search...")
        target = extraction.get("target", "half_life")
        initial = set(extraction.get("initial_conditions",
                                      ["mass_number_A", "charge_number_Z", "neutron_number_N"]))
        valid_paths = self.dfs.find_all_paths(target, initial, max_paths=5)
        print(f"    Found {len(valid_paths)} valid paths to '{target}'")

        if not valid_paths:
            print(f"    [!] No valid paths found, falling back to default")
            valid_paths = self.dfs.find_all_paths("half_life", initial, max_paths=5)

        # Phase 3a: Prediction 生成
        print(f"  [Phase 3a] Generating prediction trajectory...")
        # Crystal Rules: inject experience into prediction prompt
        experience_prompt, injected_rule_ids = "", []
        if self._crystal_manager:
            experience_prompt, injected_rule_ids = self._crystal_manager.get_experience_prompt()
        prediction_traj = self._phase3_generate(
            extraction, valid_paths, phase="prediction",
            experience_prompt=experience_prompt,
        )

        # Phase 3b: Paper derivation 生成
        print(f"  [Phase 3b] Generating paper_derivation trajectory...")
        paper_deriv_traj = self._phase3_generate(
            extraction, valid_paths, phase="paper_derivation"
        )

        # 重编号 paper_derivation step_index（Phase 3a/3b 各自从 1 开始，需连续化）
        next_idx = len(prediction_traj) + 1
        for s in paper_deriv_traj:
            s["step_index"] = next_idx
            next_idx += 1

        # Phase 4: Error Analysis + Decision Summary
        print(f"  [Phase 4] Analyzing prediction vs paper derivation...")
        prediction_traj, decision_steps = self._phase4_analyze(
            prediction_traj, paper_deriv_traj,
            paper_facts=extraction.get("paper_facts", {}),
            initial_request=paper.get("01_initial_request", {}),
        )

        # Crystal Rules: evaluate and accumulate
        if self._crystal_manager:
            self._crystal_manager.evaluate_rules(
                prediction_traj, injected_rule_ids, self.client
            )
            error_steps = [
                {"error_tag": s.get("error_tag"), "error_reason": s.get("error_reason", "")}
                for s in prediction_traj if s.get("error_tag")
            ]
            self._crystal_manager.record_paper_errors(error_steps)
            self._crystal_manager.maybe_extract_rules(self.client)

        # 合并轨迹（prediction -> decision_summary -> paper_derivation）
        full_trajectory = self.formatter.format(
            prediction_traj, decision_steps, paper_deriv_traj
        )

        # 更新 paper JSON（清理旧 pipeline 残留字段）
        paper.pop("predicted_trajectory", None)
        paper["02_agent_trajectory"] = full_trajectory
        paper["paper_methods"] = extraction.get("paper_methods", [])
        paper["paper_facts"] = extraction.get("paper_facts", {})

        # 注入 generation_config（可复现性）
        lib_path = PROJECT_ROOT / "agent_Review" / "core_tool_library_v2.json"
        lib_hash = hashlib.md5(lib_path.read_bytes()).hexdigest()[:8]
        if "meta" not in paper:
            paper["meta"] = {}
        gen_cfg = {
            "agent_script": "sci_evo_agent.py",
            "agent_version": "2.2",
            "agent_git_commit": _get_git_commit(),
            "tool_library_version": "2.0",
            "tool_library_hash": lib_hash,
            "deepseek_model": "deepseek-chat",
            "temperature": 0.3,
            "generation_timestamp": datetime.datetime.now().isoformat(),
            "generated_by": os.environ.get("USERNAME", os.environ.get("USER", "unknown")),
        }
        if self._ml_loaded:
            ml_hash = hashlib.md5(ML_LIBRARY_PATH.read_bytes()).hexdigest()[:8]
            gen_cfg["ml_library_version"] = "1.0"
            gen_cfg["ml_library_hash"] = ml_hash
        paper["meta"]["generation_config"] = gen_cfg

        # Phase 4c: 生成 03_success_verification
        paper["03_success_verification"] = self._generate_verification(
            paper.get("paper_facts", {}),
            paper.get("01_initial_request", {}),
        )

        n_errors = sum(1 for s in prediction_traj if s.get("error_tag"))
        print(f"  [OK] Generated {len(full_trajectory)} steps "
              f"({len(prediction_traj)} pred + {len(paper_deriv_traj)} paper + "
              f"{len(decision_steps)} decision), {n_errors} errors")

        return paper

    def _phase1_extract(self, paper: dict, md_content: str) -> dict:
        """Phase 1: 从论文提取结构化信息"""
        # 如果已有 01_initial_request，直接用
        req = paper.get("01_initial_request", {})
        existing_methods = paper.get("paper_methods", [])

        user_msg = f"论文信息:\n"
        if req:
            user_msg += f"  目标: {req.get('target_name', '')}\n"
            user_msg += f"  条件: {req.get('input_data', '')}\n"
            user_msg += f"  动机: {req.get('user_intent', '')}\n"
        if existing_methods:
            user_msg += f"  已知方法: {', '.join(existing_methods)}\n"
        if md_content:
            user_msg += f"\n论文摘要（前6000字）:\n{md_content[:6000]}\n"

        try:
            resp = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": PHASE1_SYSTEM},
                    {"role": "user", "content": user_msg},
                ],
                temperature=0.2,
                max_tokens=1500,
            )
            raw = resp.choices[0].message.content.strip()
            raw = re.sub(r'^```(?:json)?\s*', '', raw)
            raw = re.sub(r'\s*```$', '', raw)
            return json.loads(raw)
        except Exception as e:
            print(f"    [!] Phase 1 failed: {e}")
            return {
                "target": "half_life",
                "initial_conditions": ["mass_number_A", "charge_number_Z", "neutron_number_N"],
                "premises": {"definitions": [], "assumptions": [], "experimental_facts": []},
                "paper_methods": existing_methods,
                "paper_facts": paper.get("paper_facts", {}),
            }

    def _phase3_generate(
        self,
        extraction: dict,
        valid_paths: list[list[str]],
        phase: str,
        max_steps: int = 8,
        experience_prompt: str = "",
    ) -> list[dict]:
        """
        Phase 3: 逐步生成轨迹（带 DFS 约束验证）

        Args:
            extraction: Phase 1 提取结果
            valid_paths: 当前合法路径集合
            phase: "prediction" 或 "paper_derivation"
            max_steps: 最大步骤数
            experience_prompt: 经验规则层文本（仅 prediction 阶段注入）
        """
        current_paths = list(valid_paths)
        generated_steps = []
        step_index = 1

        # 维护已提供物理量集合（依赖满足检查）
        # 只允许基础物理量作为初始条件，不接受 Phase 1 返回的派生量
        BASIC_QUANTITIES = {
            "mass_number_A", "charge_number_Z", "neutron_number_N",
            "nuclear_radius", "nucleon_density", "deformation_parameter", "Q_value"
        }
        available = set(extraction.get("initial_conditions",
                                       ["mass_number_A", "charge_number_Z", "neutron_number_N"]))
        available = available & BASIC_QUANTITIES  # 过滤掉派生量

        # 构建路径文本
        paths_text = self._format_paths(current_paths)

        # 构建系统 prompt（含 ML tools 条件注入）
        ml_tools_text = self._get_ml_tools_prompt_section() if self._ml_loaded else ""
        system_prompt = PHASE3_SYSTEM_TEMPLATE.format(
            valid_paths_text=paths_text,
            ml_tools_section=ml_tools_text,
        )
        # 经验规则层注入（仅 prediction 阶段）
        if experience_prompt and phase == "prediction":
            system_prompt += (
                "\n\n## 经验规则层\n"
                "在本次推导中，请参考以下经验规则以避免常见错误：\n"
                f"{experience_prompt}"
            )

        phase_label = ("【半盲预测模式】你知道论文用了哪些方法，但不知道具体细节和结果。"
                       if phase == "prediction" else
                       "【论文推导提取模式】基于论文实际内容，提取真实的推导步骤。")
        is_paper_derivation = (phase == "paper_derivation")
        gen_max_tokens = 1500 if is_paper_derivation else 1000

        for _ in range(max_steps):
            # 构建用户消息
            premises = extraction.get("premises", {})
            user_msg = PHASE3_USER_TEMPLATE.format(
                phase_label=phase_label,
                definitions=json.dumps(premises.get("definitions", []), ensure_ascii=False),
                assumptions=json.dumps(premises.get("assumptions", []), ensure_ascii=False),
                experimental_facts=json.dumps(premises.get("experimental_facts", []), ensure_ascii=False),
                target=extraction.get("target", "half_life"),
                initial_conditions=", ".join(extraction.get("initial_conditions", [])),
                paper_methods=", ".join(extraction.get("paper_methods", [])),
                previous_steps=self._format_previous_steps(generated_steps),
                next_step_index=step_index,
            )

            # 生成一步（最多重试 2 次）
            step = None
            for retry in range(3):
                step = self._generate_one_step(system_prompt, user_msg,
                                               max_tokens=gen_max_tokens)
                if step is None:
                    break

                # 字段完整性验证（Issue 4 fix）
                missing_fields = self._validate_step_fields(step)
                if missing_fields:
                    if retry < 2:
                        print(f"    step {step_index}: missing/invalid fields "
                              f"{missing_fields}, retry {retry+1}")
                        missing_hint = "; ".join(missing_fields)
                        # 清除上次的 retry hint 再追加，防止 prompt 膨胀
                        user_msg = re.sub(r'\n{0,2}\[RETRY HINT\].*$', '', user_msg)
                        user_msg += (
                            f"\n\n[RETRY HINT] 缺少字段: {missing_hint}。"
                        )
                        continue
                    else:
                        print(f"    step {step_index}: missing fields "
                              f"{missing_fields} after max retries, skipping step")
                        step = None
                        break

                # 连续重复 tool 阻止
                if generated_steps:
                    prev_tool = generated_steps[-1].get("tool", {}).get("name", "")
                    curr_tool = step.get("tool", {}).get("name", "")
                    if curr_tool and curr_tool == prev_tool:
                        if retry < 2:
                            print(f"    step {step_index}: same tool '{curr_tool}' as previous step, retry {retry+1}")
                            continue

                # 独立分类器标注 step_mode
                classification = self.classifier.classify(step)
                step["step_mode"] = classification["step_mode"]
                step["phase"] = phase

                # paper_derivation 阶段 DFS 约束降级：硬约束→软警告
                soft_dfs = (phase == "paper_derivation")

                # DFS 验证
                mode = classification["step_mode"]
                if self.classifier.is_decision(mode):
                    # 决策步骤：尝试剪枝（两个 phase 都硬约束）
                    thought = step.get("thought", "")
                    paper_facts = extraction.get("paper_facts", {})
                    failure_points = paper_facts.get("failure_points", [])

                    pruned, decision_log = self.dfs.apply_decision(
                        mode, thought, current_paths,
                        failure_points=failure_points,
                    )

                    # decision_log 写入调试字段（production 可移除）
                    if decision_log["hard_excluded_tools"] or decision_log["soft_disfavored_tools"]:
                        step.setdefault("_decision_log", decision_log)

                    if len(pruned) == 0 and retry < 2:
                        # 路径全部被排除，要求重新生成
                        print(f"    step {step_index}: decision eliminates all paths"
                              f" (hard_excluded={decision_log['hard_excluded_tools']}), retry {retry+1}")
                        continue
                    elif len(pruned) == 0:
                        # 重试用尽，标记错误
                        step["valid"] = False
                        step["error_tag"] = "path_elimination"
                        step.setdefault("_decision_log", decision_log)
                    else:
                        current_paths = pruned
                    break

                elif self.classifier.triggers_hard_check(mode):
                    # 严格推导：验证在合法路径上 + 依赖满足
                    tool_name = step.get("tool", {}).get("name", "")
                    tool_id = TOOL_NAME_MAP.get(tool_name)
                    if tool_id and not self.dfs.step_on_valid_path(tool_id, step_index, current_paths, available):
                        if soft_dfs:
                            # paper_derivation: 降为软警告，不 retry，不设 valid=False
                            step["dfs_warning"] = "temporal_logic_break"
                            print(f"    step {step_index}: [soft] {tool_name} not on valid path (paper_derivation)")
                            break
                        if retry < 2:
                            print(f"    step {step_index}: {tool_name} not on valid path, retry {retry+1}")
                            continue
                        else:
                            step["valid"] = False
                            step["error_tag"] = "temporal_logic_break"
                    break
                else:
                    # 其他推进层（citation/empirical_approximation等）：依赖满足检查
                    tool_name = step.get("tool", {}).get("name", "")
                    tool_id = TOOL_NAME_MAP.get(tool_name)
                    if tool_id:
                        tool_info = self.dfs.tool_map.get(tool_id, {})
                        unmet = set(tool_info.get("requires", [])) - available
                        if unmet:
                            if soft_dfs:
                                # paper_derivation: 降为软警告
                                step["dfs_warning"] = f"unmet_requires: {', '.join(sorted(unmet))}"
                                print(f"    step {step_index}: [soft] {tool_name} requires {unmet} (paper_derivation)")
                                break
                            if retry < 2:
                                print(f"    step {step_index}: {tool_name} requires {unmet} not yet available, retry {retry+1}")
                                continue
                            else:
                                step["valid"] = False
                                step["error_tag"] = "unmet_requires"
                    break

            if step is None:
                break

            step.setdefault("valid", True)
            step["step_index"] = step_index
            # paper_derivation 步骤自动补充 observation_source
            if phase == "paper_derivation":
                step.setdefault("observation_source", "paper")
            generated_steps.append(step)
            step_index += 1

            # 更新已提供物理量集合
            tool_name = step.get("tool", {}).get("name", "")
            tool_id = TOOL_NAME_MAP.get(tool_name)
            if tool_id:
                tool_info = self.dfs.tool_map.get(tool_id, {})
                available |= set(tool_info.get("provides", []))

            # 检查是否到达目标
            # paper_derivation 至少需要 5 步才能 [DONE] 退出，防止 LLM 过早总结
            if "[DONE]" in step.get("observation", ""):
                if is_paper_derivation and len(generated_steps) < 5:
                    print(f"    step {step_index-1}: [DONE] too early ({len(generated_steps)} steps), continuing")
                    continue
                break

            # 更新路径文本（如果路径被剪枝了）
            if len(current_paths) != len(valid_paths):
                paths_text = self._format_paths(current_paths)
                ml_tools_text = self._get_ml_tools_prompt_section() if self._ml_loaded else ""
                system_prompt = PHASE3_SYSTEM_TEMPLATE.format(
                    valid_paths_text=paths_text,
                    ml_tools_section=ml_tools_text,
                )

        return generated_steps

    def _call_deepseek(self, system: str, user: str,
                       temperature: float = 0.1, max_tokens: int = 2000) -> dict | list:
        """通用 DeepSeek API 调用，含重试和 JSON 修复。"""
        for attempt in range(3):
            try:
                resp = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                finish = resp.choices[0].finish_reason
                if finish == "length":
                    print(f"    [!] DeepSeek call truncated "
                          f"(finish_reason=length), attempt {attempt+1}/3")
                    if attempt < 2:
                        time.sleep(2)
                        continue
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
                    print(f"    [!] DeepSeek call failed: {e}")
                    return {}

    def _generate_one_step(self, system_prompt: str, user_msg: str,
                           max_tokens: int = 800) -> dict | None:
        """调用 LLM 生成单个步骤"""
        for attempt in range(2):
            try:
                resp = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_msg},
                    ],
                    temperature=0.3,
                    max_tokens=max_tokens,
                )
                finish = resp.choices[0].finish_reason
                if finish == "length":
                    if attempt < 1:
                        print(f"    [!] Step generation truncated "
                              f"(finish_reason=length), retrying")
                        time.sleep(1)
                        continue
                    else:
                        print(f"    [!] Step generation truncated "
                              f"after retry, attempting partial parse")
                raw = resp.choices[0].message.content.strip()
                raw = re.sub(r'^```(?:json)?\s*', '', raw)
                raw = re.sub(r'\s*```$', '', raw)
                # 修复 LaTeX 反斜杠：将非法转义全部双反斜杠化
                raw = re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', raw)
                try:
                    return json.loads(raw)
                except json.JSONDecodeError as je:
                    # DEBUG: 打印 parse 失败的原始 LLM 输出
                    print(f"    [DEBUG] JSON parse failed: {je}")
                    print(f"    [DEBUG] Raw (first 500 chars): {raw[:500]}")
                    # 二次修复：处理嵌套转义
                    raw2 = raw.replace('\\\\\\', '\\\\')
                    try:
                        return json.loads(raw2)
                    except json.JSONDecodeError:
                        print(f"    [DEBUG] Secondary parse also failed. "
                              f"Raw (last 200 chars): ...{raw[-200:]}")
                        raise
            except Exception as e:
                if attempt == 0:
                    time.sleep(2)
                else:
                    print(f"    [!] Generation failed: {e}")
                    return None

    def _format_paths(self, paths: list[list[str]]) -> str:
        """将路径集合格式化为 prompt 文本"""
        if not paths:
            return "(no valid paths)"
        lines = []
        for i, path in enumerate(paths[:5], 1):
            chain = self.dfs.path_to_quantity_chain(path)
            lines.append(f"  Path {i}: {chain}")
        return "\n".join(lines)

    def _format_previous_steps(self, steps: list[dict]) -> str:
        """格式化已生成步骤作为 context，包含 output_state 以防止数值漂移"""
        if not steps:
            return "(none)"
        lines = []
        for s in steps[-4:]:  # 只保留最近 4 步避免 prompt 过长
            tool_name = s.get("tool", {}).get("name", "?")
            obs = s.get("observation", "")[:100]
            mode = s.get("step_mode", "?")
            # 显式传递 output_state，防止 LLM 从 observation 文本重建时丢失数值精度
            output_state = s.get("output_state", {})
            if output_state and isinstance(output_state, dict):
                state_parts = []
                for k, v in output_state.items():
                    v_str = str(v)[:60]
                    state_parts.append(f"{k}={v_str}")
                state_text = ", ".join(state_parts)
                lines.append(
                    f"  Step {s.get('step_index')}: [{mode}] {tool_name} "
                    f"-> state: {state_text} | obs: {obs}"
                )
            else:
                lines.append(
                    f"  Step {s.get('step_index')}: [{mode}] {tool_name} -> {obs}"
                )
        return "\n".join(lines)

    # ── 步骤字段完整性验证 ─────────────────────────────────────────────────────

    _REQUIRED_STEP_FIELDS = {
        "thought": lambda v: isinstance(v, str) and len(v.strip()) >= 10,
        "action": lambda v: isinstance(v, str) and len(v.strip()) > 0,
        "tool": lambda v: isinstance(v, dict) and len(v.get("name", "").strip()) > 0,
        "parameters": lambda v: isinstance(v, dict),
        "output_state": lambda v: isinstance(v, dict),
        "observation": lambda v: isinstance(v, str) and len(v.strip()) > 0,
    }

    def _validate_step_fields(self, step: dict) -> list[str]:
        """检查步骤是否包含所有必需字段且内容非空。返回缺失/问题字段列表。"""
        missing = []
        for field, check_fn in self._REQUIRED_STEP_FIELDS.items():
            val = step.get(field)
            if val is None:
                missing.append(f"{field} (null)")
            elif not check_fn(val):
                if field == "tool" and isinstance(val, dict):
                    missing.append("tool.name (empty/missing)")
                else:
                    missing.append(f"{field} (empty/invalid)")
        return missing

    # ── Phase 4: Error Analysis + Decision Summary ─────────────────────────────

    def _phase4_analyze(
        self,
        prediction_traj: list[dict],
        paper_deriv_traj: list[dict],
        paper_facts: dict,
        initial_request: dict,
    ) -> tuple[list[dict], list[dict]]:
        """
        Phase 4: 对比 prediction vs paper_derivation，回标 error_tag，
        生成 decision_summary 步骤。

        Returns:
            (updated_prediction_traj, decision_summary_steps)
        """
        # ── 4a: Error Analysis ─────────────────────────────────────────────
        print(f"    [4a] Error analysis...")

        # 构建步骤摘要（控制长度避免 prompt 过长）
        pred_summary = []
        for s in prediction_traj:
            pred_summary.append({
                "step_index": s["step_index"],
                "tool": s.get("tool", {}).get("name", ""),
                "thought": s.get("thought", "")[:350],
                "observation": s.get("observation", "")[:200],
            })

        paper_summary = []
        for s in paper_deriv_traj:
            paper_summary.append({
                "step_index": s["step_index"],
                "tool": s.get("tool", {}).get("name", ""),
                "thought": s.get("thought", "")[:350],
                "observation": s.get("observation", "")[:200],
            })

        phase3_user = (
            f"## 模型预测的推理步骤（prediction 阶段）\n"
            f"{json.dumps(pred_summary, ensure_ascii=False, indent=2)}\n\n"
            f"## 论文实际的推导步骤（paper_derivation 阶段）\n"
            f"{json.dumps(paper_summary, ensure_ascii=False, indent=2)}\n\n"
            f"请逐个检查预测步骤，标注物理推理错误。只输出 JSON。"
        )

        error_result = self._call_deepseek(
            ERROR_ANALYSIS_PROMPT, phase3_user,
            temperature=0.1, max_tokens=2000,
        )

        # 解析 error_tags
        error_tags_map = {}
        for item in error_result.get("error_tags", []):
            idx = item.get("step_index")
            if idx is not None:
                error_tags_map[idx] = {
                    "error_tag": item.get("error_tag"),
                    "error_reason": item.get("error_reason"),
                }

        # DFS 内部 tag → schema 合法 error_tag 映射
        _DFS_TAG_MAP = {
            "temporal_logic_break": "incorrect_derivation",
            "path_elimination": "incorrect_derivation",
            "unmet_requires": "missing_physical_effect",
        }

        # 回标 prediction 步骤
        for s in prediction_traj:
            tag_info = error_tags_map.get(s["step_index"], {})
            llm_tag = tag_info.get("error_tag")

            if llm_tag:
                # LLM 发现物理错误 -> 用 LLM 的（更具体）
                s["error_tag"] = llm_tag
                s["valid"] = False
                if tag_info.get("error_reason"):
                    s["error_reason"] = tag_info["error_reason"]

            elif s.get("valid") is False:
                # DFS 已标 invalid，但 LLM 未发现物理错误
                existing_tag = s.get("error_tag", "")

                if existing_tag == "path_elimination":
                    # 路径被决策层完全排除 — 硬错误，保留
                    s["error_tag"] = _DFS_TAG_MAP.get(existing_tag, "incorrect_derivation")
                    if not s.get("error_reason"):
                        s["error_reason"] = "推导路径被决策层排除，所选方法不被物理情景支持"

                elif existing_tag in _DFS_TAG_MAP:
                    # temporal_logic_break / unmet_requires:
                    # DFS 结构检查发现了问题，但 LLM 审查后认为物理正确
                    # -> 信任 LLM 的物理判断，降级为 dfs_warning
                    s["dfs_warning"] = existing_tag
                    s["valid"] = True
                    s["error_tag"] = None
                    if s.get("error_reason") and "违反物理量依赖链" in str(s.get("error_reason", "")):
                        s["error_reason"] = None

                else:
                    # valid=False 但无已知标签 -> 兜底清理
                    s["error_tag"] = None
                    s["valid"] = True

            else:
                # LLM 说 null，step 本身 valid -> 清理
                s["error_tag"] = None

        n_errors = sum(1 for s in prediction_traj if s.get("error_tag"))
        print(f"    [4a] {n_errors} physical reasoning errors found")

        # ── 4b: Decision Summary ───────────────────────────────────────────
        print(f"    [4b] Decision summary...")

        next_index = (paper_deriv_traj[-1]["step_index"] + 1) if paper_deriv_traj else 1
        error_steps = [s for s in prediction_traj if s.get("error_tag")]
        non_error_steps = [s for s in prediction_traj if not s.get("error_tag")]

        decision_summary_steps = []

        if error_steps:
            # 错误步骤：调用 LLM 生成详细决策根因
            error_summary = []
            for s in error_steps:
                error_summary.append({
                    "step_index": s["step_index"],
                    "tool": s.get("tool", {}).get("name", ""),
                    "thought": s.get("thought", "")[:350],
                    "observation": s.get("observation", "")[:200],
                    "error_tag": s.get("error_tag"),
                    "error_reason": s.get("error_reason", ""),
                })

            phase4_user = (
                f"## 预测中出错的步骤（含错误标签和原因）\n"
                f"{json.dumps(error_summary, ensure_ascii=False, indent=2)}\n\n"
                f"## 论文实际的推导步骤\n"
                f"{json.dumps(paper_summary, ensure_ascii=False, indent=2)}\n\n"
                f"请分析每个错误的决策根因，不要写马后炮。只输出 JSON。"
            )

            decision_result = self._call_deepseek(
                DECISION_SUMMARY_PROMPT, phase4_user,
                temperature=0.2, max_tokens=2000,
            )

            summaries = decision_result.get("decision_summary", [])
            for i, ds in enumerate(summaries):
                decision_summary_steps.append({
                    "step_index": next_index + i,
                    "phase": "decision_summary",
                    "thought": (
                        f"[Background] 决策时刻：{ds.get('decision_point', '')}。"
                        f"[Gap] 错过的信号：{ds.get('missed_signal', '')}。"
                        f"[Decision] 正确判断方式：{ds.get('correct_reasoning', '')}。"
                    ),
                    "action": "verification",
                    "tool": {"name": self._pick_ds_tool(ds.get("tool_name", "")), "version": ""},
                    "parameters": {},
                    "output_state": {},
                    "observation": ds.get('root_cause', ''),
                    "observation_source": "inferred",
                    "valid": True,
                    "error_tag": None,
                })

            # overall_lesson 附加到最后一步
            overall_lesson = decision_result.get("overall_lesson", "")
            if overall_lesson and decision_summary_steps:
                decision_summary_steps[-1]["overall_lesson"] = overall_lesson

        # 非错误步骤：合并为 1 条轻量确认（避免每个正确的步骤各写一条套话稀释信息）
        if non_error_steps:
            correct_indices = [s["step_index"] for s in non_error_steps]
            correct_tools = [s.get("tool", {}).get("name", "?") for s in non_error_steps]
            idx_str = ", ".join(str(i) for i in correct_indices)
            tool_str = " -> ".join(correct_tools)
            decision_summary_steps.append({
                "step_index": next_index + len(decision_summary_steps),
                "phase": "decision_summary",
                "thought": (
                    f"[Background] 步骤 {idx_str} 分别使用 {tool_str} 进行推导。"
                    f"[Gap] 逐步审查这些步骤的物理推理逻辑。"
                    f"[Decision] 上述步骤在给定前提和已知条件下，物理推理无错误，"
                    f"方法选择合理，推导链自洽。"
                ),
                "action": "verification",
                "tool": {"name": "physical_intuition_check", "version": ""},
                "parameters": {},
                "output_state": {},
                "observation": f"步骤 {idx_str} 的物理推理经过审查，未发现逻辑或方法错误",
                "observation_source": "inferred",
                "valid": True,
                "error_tag": None,
            })

        print(f"    [4b] {len(decision_summary_steps)} decision summary steps "
              f"({len(error_steps)} error analysis + "
              f"{1 if non_error_steps else 0} correct confirmation)")

        return prediction_traj, decision_summary_steps

    _VALID_DS_TOOLS = {"physical_intuition_check", "limiting_case_check", "dimensional_analysis"}

    def _pick_ds_tool(self, raw: str) -> str:
        """从 LLM 返回的 tool_name 中选取合法值，无效则 fallback。"""
        cleaned = raw.strip().lower().replace("-", "_").replace(" ", "_")
        if cleaned in self._VALID_DS_TOOLS:
            return cleaned
        return "physical_intuition_check"

    def _generate_verification(self, paper_facts: dict, initial_request: dict) -> dict:
        """从 paper_facts 生成 03_success_verification，调 LLM 生成具体验证方法。"""
        metrics = {}
        for i, r in enumerate(paper_facts.get("key_results", [])[:6]):
            val_str = r.get("value", "")
            if not _is_numerical_value(val_str):
                # 跳过定性值（如 "found at", "very high"），它们不是可验证的指标
                continue
            qty = r.get("quantity", f"result_{i+1}")
            key = re.sub(r'[^a-zA-Z0-9_]', '_', qty).strip('_')
            if not key:
                key = f"result_{i+1}"
            metrics[key] = {
                "value": val_str,
                "unit": r.get("condition", ""),
                "interpretation": qty,
            }

        if not metrics:
            metrics["completeness"] = {
                "value": "paper_derivation 提取完成",
                "unit": "",
                "interpretation": "论文推导步骤已成功提取",
            }

        # ── validation_technique: 调 LLM 生成具体验证方法 ──
        methods = [m.get("name", "") for m in paper_facts.get("methods", [])]
        goal = initial_request.get("quantifiable_goal", "")
        results_brief = "; ".join(
            f"{r.get('quantity','')}: {r.get('value','')}"
            for r in paper_facts.get("key_results", [])[:3]
        )

        vt_prompt = (
            "你是核物理专家。请用2-3句话描述如何验证以下研究结果的正确性。\n"
            "要求：\n"
            "1. 提及具体验证手段（与具体实验数据对比、量纲分析、极限情况检验、"
            "已知系统学趋势对比、独立方法交叉验证等）\n"
            "2. 如果提到实验对比，指明对比什么实验数据、在什么条件范围\n"
            "3. 如果涉及计算方法，说明该方法的适用条件和可能的失效模式\n"
            "4. 禁止写'通过实验验证''与理论对比'等泛泛套话\n\n"
            f"研究目标：{goal}\n"
            f"使用方法：{', '.join(methods[:5])}\n"
            f"关键结果：{results_brief}\n\n"
            '输出严格 JSON：{{"validation_technique": "你的2-3句话描述"}}'
        )
        try:
            vt_resp = self._call_deepseek(
                "你是一个简洁的科学写作助手。只输出 JSON。", vt_prompt,
                temperature=0.3, max_tokens=300,
            )
            validation_technique = vt_resp.get("validation_technique", "") if isinstance(vt_resp, dict) else ""
        except Exception:
            validation_technique = ""

        # fallback：从 methods 拼接
        if not validation_technique or len(validation_technique) < 15:
            if methods and goal:
                validation_technique = (
                    f"通过 {' 和 '.join(methods[:2])} 计算的 {goal} "
                    f"与实验数据进行定量对比验证"
                )
            else:
                validation_technique = "对比理论计算结果与实验测量值，检验偏差量级"

        # ── final_verdict ──
        final_verdict = ""
        fp = paper_facts.get("failure_points", [])
        if fp:
            final_verdict = f"论文否定/改进了以下方法：{'；'.join(fp[:3])}。"
        else:
            # failure_points 为空时，从 key_results 生成摘要
            kr = paper_facts.get("key_results", [])
            if kr:
                final_verdict = f"论文通过 {', '.join(methods[:2]) if methods else '理论计算'} 得到了 {kr[0].get('quantity', '目标物理量')} 等关键结果，与已有实验数据或理论预期一致。"
            else:
                final_verdict = "论文推导步骤已完整提取，关键物理量的计算结果见 metrics。"

        return {
            "validation_technique": validation_technique,
            "metrics": metrics,
            "final_verdict": final_verdict,
        }


# ── 入口 ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Sci-Evo Agent v2")
    parser.add_argument("--paper", type=str, help="Single paper JSON path")
    parser.add_argument("--folder", type=str, help="Subdomain folder name")
    parser.add_argument("--limit", type=int, default=0, help="Max papers to process (0=all)")
    parser.add_argument("--dry-run", action="store_true", help="Only run Phase 1+2, skip generation")
    parser.add_argument("--batch-size", type=int, default=0, help="Crystal BATCH_SIZE (0=auto ceil(N/3), min 3)")
    parser.add_argument("--output-dir", type=str, default=None, help="Output directory (default: same as input)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing output files")
    parser.add_argument("--no-crystal", action="store_true", help="Disable Crystal Rule Manager")
    args = parser.parse_args()

    agent = SciEvoAgent()

    if args.paper:
        paper_path = Path(args.paper)
        if not paper_path.is_absolute():
            paper_path = PROJECT_ROOT / paper_path
        result = agent.run(paper_path)
        # 保存结果
        out_path = paper_path.parent / f"{paper_path.stem}_v2.json"
        out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\n[OK] Saved to {out_path}")

    elif args.folder:
        folder_path = PAPERS_DIR / args.folder
        if not folder_path.exists():
            print(f"[!] Folder not found: {folder_path}")
            return

        # 只选原始 JSON，排除 _v2.json
        all_papers = [p for p in sorted(folder_path.glob("*.json"))
                      if not p.stem.endswith("_v2")]

        # Crystal Rule Manager（仅 --folder 模式激活）
        if not args.no_crystal:
            subdomain = args.folder.replace(" ", "_").lower()
            if args.batch_size > 0:
                batch_size = args.batch_size
            else:
                n_papers = len(all_papers)
                batch_size = max(3, (n_papers + 2) // 3)  # ceil(N/3), min 3
            print(f"[*] Crystal: subdomain={subdomain}, batch_size={batch_size}")
            agent._crystal_manager = CrystalRuleManager(subdomain, batch_size=batch_size)
        else:
            print(f"[*] Crystal: DISABLED (--no-crystal)")

        # 输出目录
        if args.output_dir:
            output_dir = Path(args.output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
        else:
            output_dir = folder_path

        # 断点续跑：跳过已有输出的文件（除非 --force）
        papers = []
        for p in all_papers:
            out_path = output_dir / f"{p.stem}_v2.json"
            if out_path.exists() and not args.force:
                print(f"  [SKIP] {p.name} (output exists)")
                continue
            papers.append(p)
            if args.limit > 0 and len(papers) >= args.limit:
                break
        print(f"[*] Processing {len(papers)} papers from {args.folder} "
              f"({len(all_papers)} total, {len(all_papers)-len(papers)} skipped)")

        for paper_path in papers:
            try:
                result = agent.run(paper_path)
                out_path = output_dir / f"{paper_path.stem}_v2.json"
                out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            except Exception as e:
                print(f"  [!] Failed: {e}")
                continue


if __name__ == "__main__":
    main()
