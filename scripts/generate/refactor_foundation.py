"""
refactor_foundation.py
三合一重构脚本，修复 Foundation 层三个架构风险：
  Phase 1 (--step tool)   : Tool 归并，83个 → ~25个核心 tool
  Phase 2 (--step action) : Action 修正，新增 rule_application / model_building
  Phase 3 (--step state)  : output_state 注入（空占位）+ DeepSeek API 填充

用法：
  python refactor_foundation.py --domain all --step all
  python refactor_foundation.py --domain quantum --step tool --dry-run
  python refactor_foundation.py --domain nuclear --step state
"""

import argparse
import json
import os
import time

import openai
from tqdm import tqdm

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIRS = {
    "quantum": os.path.join(BASE, "dataset", "foundation", "quantum"),
    "nuclear": os.path.join(BASE, "dataset", "foundation", "nuclear"),
}

# ---------------------------------------------------------------------------
# Phase 1: Tool 归并映射表
# ---------------------------------------------------------------------------

TOOL_MERGE_MAP: dict[str, str] = {
    # → symbolic_algebra（代数化简、变量代换、几何计算）
    "algebraic_substitution":           "symbolic_algebra",
    "substitution":                     "symbolic_algebra",
    "differential_equation_substitution": "symbolic_algebra",
    "variable_transformation":          "symbolic_algebra",
    "coordinate_transformation":        "symbolic_algebra",
    "parameterization":                 "symbolic_algebra",
    "ansatz_substitution":              "symbolic_algebra",
    "recursive_differentiation":        "symbolic_algebra",
    "gamma_function_manipulation":      "symbolic_algebra",
    "equation_identification":          "symbolic_algebra",
    "pattern_recognition":              "symbolic_algebra",
    "direct_comparison":                "symbolic_algebra",
    "vector_projection_definition":     "symbolic_algebra",
    "geometric_volume_calculation":     "symbolic_algebra",
    "series_summation":                 "symbolic_algebra",
    # → symbolic_computation（方程求解，parameters 中注明类型）
    "algebraic_solution":               "symbolic_computation",
    "special_function_solution":        "symbolic_computation",
    "special_function_transformation":  "symbolic_computation",
    "series_termination_condition":     "symbolic_computation",
    # → integral_evaluation（积分计算，含期望值积分）
    "integral_calculation":             "integral_evaluation",
    "expectation_value_integral":       "integral_evaluation",
    "expectation_value_calculation":    "integral_evaluation",
    "expectation_value_decomposition":  "integral_evaluation",
    "matrix_element_method":            "integral_evaluation",
    "variance_calculation":             "integral_evaluation",
    # → numerical_computation（数值代入与计算）
    "numerical_substitution":           "numerical_computation",
    "numerical_evaluation":             "numerical_computation",
    "proportionality_calculation":      "numerical_computation",
    "relative_error_calculation":       "numerical_computation",
    "probability_calculation":          "numerical_computation",
    "mass_difference_calculation":      "numerical_computation",
    "activity_calculation":             "numerical_computation",
    "integration_method":               "numerical_computation",
    "function_optimization":            "numerical_computation",
    "scaling_relation":                 "numerical_computation",
    "inverse_square_law":               "numerical_computation",
    "weighted_average_method":          "numerical_computation",
    # → dimensional_analysis_and_conversion（量纲分析与单位换算）
    "dimensional_analysis":             "dimensional_analysis_and_conversion",
    "unit_conversion_and_rate_calculation": "dimensional_analysis_and_conversion",
    "unit_conversion_and_substitution": "dimensional_analysis_and_conversion",
    # → series_expansion（级数展开）
    "taylor_series_expansion":          "series_expansion",
    # 合并重复的散射/Mott tool
    "scattering_kinematics":            "nuclear_scattering_kinematics",
    "elastic_collision_kinematics":     "nuclear_scattering_kinematics",
    "mott_formula_calculation":         "mott_scattering_formula",
}

# ---------------------------------------------------------------------------
# Phase 2: Action 修正映射表（tool_name → 正确的 action）
# ---------------------------------------------------------------------------

# 规则应用：应用已知物理规则/定理，无需推导
RULE_APPLICATION_TOOLS = {
    "shell_filling",
    "pairing_rule",
    "radioactive_decay_law",
    "secular_equilibrium_condition",
    "bateman_equation_solution",
}

# 模型建立：建立物理模型/近似框架（仅 step_index==1 且 action 为 symbolic_derivation 时修正）
MODEL_BUILDING_TOOLS = {
    "fermi_gas_model",
    "optical_model_potential",
}

# ---------------------------------------------------------------------------
# Phase 1 实现
# ---------------------------------------------------------------------------

def apply_tool_merge(data: dict) -> tuple[dict, list[str]]:
    """按 TOOL_MERGE_MAP 归并 tool.name，返回 (修改后data, 变更描述列表)。"""
    changes: list[str] = []
    for step in data.get("02_agent_trajectory", []):
        old_name = step.get("tool", {}).get("name", "")
        new_name = TOOL_MERGE_MAP.get(old_name)
        if new_name and new_name != old_name:
            step["tool"]["name"] = new_name
            changes.append(f"  step{step['step_index']}: {old_name} → {new_name}")
    return data, changes


# ---------------------------------------------------------------------------
# Phase 2 实现
# ---------------------------------------------------------------------------

def apply_action_fix(data: dict) -> tuple[dict, list[str]]:
    """修正 action 字段，新增 rule_application / model_building 类型。"""
    changes: list[str] = []
    for step in data.get("02_agent_trajectory", []):
        tool_name = step.get("tool", {}).get("name", "")
        old_action = step.get("action", "")

        if tool_name in RULE_APPLICATION_TOOLS and old_action == "symbolic_derivation":
            step["action"] = "rule_application"
            changes.append(f"  step{step['step_index']}: action {old_action} → rule_application (tool={tool_name})")

        elif (tool_name in MODEL_BUILDING_TOOLS
              and old_action == "symbolic_derivation"
              and step.get("step_index") == 1):
            step["action"] = "model_building"
            changes.append(f"  step{step['step_index']}: action {old_action} → model_building (tool={tool_name})")

    return data, changes


# ---------------------------------------------------------------------------
# Phase 3 实现
# ---------------------------------------------------------------------------

OUTPUT_STATE_SYSTEM_PROMPT = """\
你是物理数据集标注助手。给定一个 agent trajectory 步骤的 observation 字段，
提取该步骤产出的关键物理量或符号表达式，以严格 JSON 格式返回。

规则：
- key 使用物理符号名（如 "rho_U", "E_n", "N_U", "psi_n"）
- value 使用 LaTeX 表达式字符串或数值字符串
- 【重要】JSON 字符串中的 LaTeX 反斜杠必须写成双反斜杠 \\\\，例如：
    正确：{"rho": "\\\\rho_{U}"}
    错误：{"rho": "\\rho_{U}"}
- 只提取该步骤新产出的量，不重复上一步已有的量
- 若该步骤无新产出量（如纯验证步骤），返回 {}
- 只输出 JSON，不要任何解释文字、不要 markdown 代码块
"""


def inject_output_state(data: dict) -> tuple[dict, bool]:
    """为所有步骤注入 output_state: null 占位（幂等）。返回 (data, 是否有注入)。"""
    injected = False
    for step in data.get("02_agent_trajectory", []):
        if "output_state" not in step:
            # 在 parameters 和 observation 之间插入
            new_step: dict = {}
            for k, v in step.items():
                new_step[k] = v
                if k == "parameters":
                    new_step["output_state"] = None  # null = 未填充；{} = 已填充（可为空）
            step.clear()
            step.update(new_step)
            injected = True
    return data, injected


def _repair_json_escapes(text: str) -> str:
    """修复 JSON 字符串中 LaTeX 反斜杠导致的非法转义（如 \\r, \\m, \\f 等）。"""
    import re
    # 合法的 JSON 转义字符：" \\ / b f n r t u
    return re.sub(r'\\(?!["\\/bfnrtu])', r'\\\\', text)


def _fill_one_step(client: openai.OpenAI, step: dict) -> dict:
    """调用 DeepSeek 填充单个步骤的 output_state。"""
    observation = step.get("observation", "")
    if not observation:
        return {}

    response = client.chat.completions.create(
        model="deepseek-chat",
        max_tokens=512,
        temperature=0.1,
        messages=[
            {"role": "system", "content": OUTPUT_STATE_SYSTEM_PROMPT},
            {"role": "user", "content": f"observation:\n{observation}"},
        ],
    )
    text = response.choices[0].message.content or ""
    text = text.strip()
    # 去除可能的 markdown 代码块
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.rsplit("```", 1)[0].strip()
    # 修复 LaTeX 反斜杠导致的非法 JSON 转义
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return json.loads(_repair_json_escapes(text))


def fill_output_state(client: openai.OpenAI, data: dict, fname: str) -> tuple[dict, int]:
    """对 output_state == {} 的步骤调用 DeepSeek 填充。返回 (data, 填充步骤数)。"""
    filled = 0
    for step in data.get("02_agent_trajectory", []):
        if step.get("output_state") is not None:
            continue  # None = 未填充；非 None（含 {}）= 已填充，跳过
        idx = step.get("step_index", "?")
        print(f"    step{idx} 填充 output_state ...", end=" ", flush=True)
        try:
            result = _fill_one_step(client, step)
            step["output_state"] = result
            filled += 1
            print(f"OK ({len(result)} 个量)")
        except json.JSONDecodeError as e:
            print(f"JSON 解析失败: {e}")
        except Exception as e:
            print(f"错误: {e}")
        time.sleep(0.3)
    return data, filled


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_json(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def process_domain(domain: str, steps: set[str], dry_run: bool,
                   client: openai.OpenAI | None) -> None:
    out_dir = OUT_DIRS[domain]
    files = sorted(f for f in os.listdir(out_dir) if f.endswith(".json"))
    print(f"\n[{domain}] {len(files)} 个文件，执行阶段: {sorted(steps)}")

    bar = tqdm(files, desc=domain, unit="文件", ncols=80)
    for fname in bar:
        bar.set_postfix_str(fname)
        path = os.path.join(out_dir, fname)
        data = load_json(path)
        file_changed = False

        # Phase 1: tool 归并
        if "tool" in steps or "all" in steps:
            data, changes = apply_tool_merge(data)
            if changes:
                tqdm.write(f"  {fname} [tool] {len(changes)} 处变更")
                file_changed = True

        # Phase 2: action 修正
        if "action" in steps or "all" in steps:
            data, changes = apply_action_fix(data)
            if changes:
                tqdm.write(f"  {fname} [action] {len(changes)} 处变更")
                file_changed = True

        # Phase 3: output_state 注入 + 填充
        if "state" in steps or "all" in steps:
            data, injected = inject_output_state(data)
            if injected:
                tqdm.write(f"  {fname} [state] 注入空占位")
                file_changed = True

            if client is not None:
                n_pending = sum(
                    1 for s in data.get("02_agent_trajectory", [])
                    if s.get("output_state") is None
                )
                if n_pending:
                    bar.set_postfix_str(f"{fname} state×{n_pending}")
                    data, filled = fill_output_state(client, data, fname)
                    if filled:
                        tqdm.write(f"  {fname} [state] 填充 {filled} 步")
                        file_changed = True

        # 写回
        if file_changed and not dry_run:
            save_json(path, data)


def main() -> None:
    parser = argparse.ArgumentParser(description="Foundation 层三合一重构脚本")
    parser.add_argument("--domain", required=True, choices=["quantum", "nuclear", "all"])
    parser.add_argument("--step", default="all",
                        help="tool | action | state | all（逗号分隔可组合，如 tool,action）")
    parser.add_argument("--dry-run", action="store_true", help="只打印变更，不写文件")
    args = parser.parse_args()

    steps: set[str] = set(s.strip() for s in args.step.split(","))
    valid_steps = {"tool", "action", "state", "all"}
    if not steps.issubset(valid_steps):
        parser.error(f"--step 只接受: {valid_steps}")

    # 仅 state 阶段需要 API client
    client: openai.OpenAI | None = None
    if "state" in steps or "all" in steps:
        api_key = os.environ.get("DEEPSEEK_API_KEY", "")
        client = openai.OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    domains = ["quantum", "nuclear"] if args.domain == "all" else [args.domain]
    for domain in domains:
        process_domain(domain, steps, args.dry_run, client)

    print("\n完成。")


if __name__ == "__main__":
    main()
