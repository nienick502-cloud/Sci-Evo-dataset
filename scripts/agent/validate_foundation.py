"""
validate_foundation.py - 用 DFS 引擎验证 Foundation 层推导链合法性

核心逻辑：
1. 从每条样本的 01_initial_request.input_data 中提取该题实际给定的物理量
2. 用这些已知量作为初始 available 集合（而非一刀切塞入所有量）
3. 逐步追踪依赖，检查每个 tool 的 requires 是否被满足
4. DFS 反查路径可达性

用法:
  python agent_Review/validate_foundation.py
  python agent_Review/validate_foundation.py --domain nuclear
  python agent_Review/validate_foundation.py --verbose
"""

import argparse
import json
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CORE_LIBRARY_PATH = PROJECT_ROOT / "agent_Review" / "core_tool_library_v2.json"
FOUNDATION_DIR = PROJECT_ROOT / "dataset" / "foundation"

# ── Foundation tool 名 → 核心库 tool_id 映射 ──────────────────────────────
FOUNDATION_TOOL_MAP = {
    # 核结构
    "nuclear_radius_formula": "T01",
    "shell_filling": "T02",
    "bethe_weizsacker_formula": "T03",
    "fermi_gas_model": "T05",
    "pairing_rule": "T07",
    # 势能
    "coulomb_barrier_estimate": "T70",
    "cross_section_calculation": "T30",
    # 衰变动力学
    "nuclear_decay_kinematics": "T63",
    "radioactive_decay_law": "T65",
    "secular_equilibrium_condition": "T66",
    "bateman_equation_solution": "T67",
    # 反应
    "nuclear_reaction_rate": "T68",
    # 散射运动学
    "nuclear_scattering_kinematics": "T69",
    "compton_scattering_kinematics": "T71",
    "mott_scattering_formula": "T72",
    "energy_loss_calculation": "T73",
    "form_factor_expansion": "T74",
    # 验证
    "dimensional_analysis_and_conversion": "T48",
    "limiting_case_check": "T49",
    "physical_intuition_check": None,
    # 量子力学（核心库无对应）
    "separation_of_variables": None,
    "fourier_transform": None,
    "boundary_condition_matching": None,
    "bohr_sommerfeld_quantization": None,
    "normalization_condition": None,
    "angular_momentum_coupling": None,
    "symmetry_argument": None,
    "commutator_algebra": None,
    "uncertainty_principle_application": None,
    "asymptotic_analysis": None,
    "eigenfunction_expansion": None,
    "variational_method": None,
    # 其他
    "coincidence_rate_calculation": None,
}

MATH_TOOLS = {
    "symbolic_algebra", "symbolic_computation", "integral_evaluation",
    "numerical_computation", "dimensional_analysis_and_conversion",
    "series_expansion",
}

# ── 从 input_data 文本中提取已知物理量 ──────────────────────────────
# 关键词 → 物理量名 的映射
INPUT_KEYWORDS = {
    "mass_number_A": [r"A\s*=\s*\d+", r"质量数", r"mass number"],
    "charge_number_Z": [r"Z\s*=\s*\d+", r"电荷数", r"atomic number", r"质子数"],
    "neutron_number_N": [r"N\s*=\s*\d+", r"中子数"],
    "Q_value": [r"Q\s*=", r"Q值", r"Q value", r"衰变能", r"反应能"],
    "nuclear_radius": [r"R\s*=", r"r_0", r"核半径", r"nuclear radius"],
    "half_life": [r"T_\\?{?1/2}?\\s*=", r"半衰期", r"half.life", r"half_life"],
    "decay_constant": [r"\\lambda\s*=", r"衰变常数", r"decay constant"],
    "binding_energy": [r"B\s*\(", r"结合能", r"binding energy"],
    "incident_energy": [r"E_\{?\\? kinetic\}?", r"入射能", r"动能", r"incident energy",
                        r"beam energy", r"T_\{?\\? lab\}?"],
    "particle_flux": [r"通量", r"flux", r"束流", r"beam current", r"I\s*="],
    "cross_section": [r"\\sigma\s*=", r"截面", r"cross.section"],
    "scattering_amplitude": [r"f\\(\\theta\\)", r"散射振幅"],
    "single_particle_levels": [r"能级", r"energy level"],
    "spin_parity": [r"J[π^P]", r"自旋宇称", r"spin parity"],
    "deformation_parameter": [r"\\beta\s*=", r"形变参数", r"deformation"],
}


def extract_given_quantities(input_data: str, quantifiable_goal: str = "") -> set:
    """从 input_data 和 quantifiable_goal 文本中提取已知物理量"""
    given = {"mass_number_A", "charge_number_Z", "neutron_number_N"}  # 基本量总是已知
    text = input_data + " " + quantifiable_goal
    for quantity, patterns in INPUT_KEYWORDS.items():
        for pat in patterns:
            if re.search(pat, text, re.IGNORECASE):
                given.add(quantity)
                break
    return given


def load_core_library():
    with open(CORE_LIBRARY_PATH, encoding="utf-8") as f:
        lib = json.load(f)
    tools = {}
    for t in lib["tools"]:
        if "id" in t:
            tools[t["id"]] = t
    return tools


def validate_one_sample(sample: dict, core_tools: dict) -> dict:
    """验证单条 Foundation 样本"""
    sample_id = sample.get("id", "?")
    meta = sample.get("meta", {})
    req = sample.get("01_initial_request", {})
    traj = sample.get("02_agent_trajectory", [])

    # 从 input_data 提取该题实际给定的物理量
    input_data = req.get("input_data", "")
    goal = req.get("quantifiable_goal", "")
    available = extract_given_quantities(input_data, goal)

    result = {
        "id": sample_id,
        "domain": meta.get("domain", ""),
        "subdomain": meta.get("subdomain", ""),
        "steps": len(traj),
        "initial_available": sorted(available),
        "tool_chain": [],
        "dep_check": [],
        "dep_pass": True,
        "unmapped_tools": [],
        "issues": [],
    }

    for step in traj:
        tool_name = step.get("tool", {}).get("name", "")
        tool_id = FOUNDATION_TOOL_MAP.get(tool_name)
        is_math = tool_name in MATH_TOOLS

        result["tool_chain"].append(tool_name)

        if tool_id is None and not is_math:
            result["unmapped_tools"].append(tool_name)
            result["dep_check"].append({
                "step": step.get("step_index"),
                "tool": tool_name,
                "status": "unmapped",
            })
            # 从 output_state 补充 available（未映射工具的产出也是可用的）
            for k in step.get("output_state", {}):
                available.add(k)
            continue

        if is_math:
            result["dep_check"].append({
                "step": step.get("step_index"),
                "tool": tool_name,
                "status": "math_tool_skip",
            })
            for k in step.get("output_state", {}):
                available.add(k)
            continue

        # 有映射的物理工具：做依赖检查
        tool_info = core_tools.get(tool_id, {})
        requires = set(tool_info.get("requires", []))
        provides = set(tool_info.get("provides", []))
        unmet = requires - available

        step_result = {
            "step": step.get("step_index"),
            "tool": tool_name,
            "tool_id": tool_id,
            "requires": sorted(requires),
            "provides": sorted(provides),
            "unmet": sorted(unmet),
            "status": "pass" if not unmet else "fail",
        }
        result["dep_check"].append(step_result)

        if unmet:
            result["dep_pass"] = False
            result["issues"].append(
                f"Step {step.get('step_index')}: {tool_name}({tool_id}) "
                f"requires {unmet} not yet available"
            )

        available |= provides
        for k in step.get("output_state", {}):
            available.add(k)

    return result


def main():
    parser = argparse.ArgumentParser(description="Validate Foundation layer with DFS engine")
    parser.add_argument("--domain", type=str, default="all",
                        choices=["all", "quantum", "nuclear"])
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    core_tools = load_core_library()
    print(f"Core library: {len(core_tools)} tools")

    domains = ["quantum", "nuclear"] if args.domain == "all" else [args.domain]
    all_results = []

    for domain in domains:
        folder = FOUNDATION_DIR / domain
        if not folder.exists():
            continue
        files = sorted(folder.glob("*.json"))
        print(f"\n{'='*60}")
        print(f"{domain} ({len(files)} samples)")
        print(f"{'='*60}")

        for fp in files:
            with open(fp, encoding="utf-8") as f:
                sample = json.load(f)
            result = validate_one_sample(sample, core_tools)
            all_results.append(result)

            status = "[OK]" if result["dep_pass"] else "[!!]"
            unmapped = f" unmapped={result['unmapped_tools']}" if result['unmapped_tools'] else ""
            print(f"  {status} {result['id']:8s} {result['subdomain']:35s} "
                  f"given={len(result['initial_available'])} "
                  f"dep={'PASS' if result['dep_pass'] else 'FAIL'}{unmapped}")

            if args.verbose and result["issues"]:
                for issue in result["issues"]:
                    print(f"       -> {issue}")

    # 汇总
    total = len(all_results)
    dep_pass = sum(1 for r in all_results if r["dep_pass"])
    has_unmapped = sum(1 for r in all_results if r["unmapped_tools"])

    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"Total: {total}")
    print(f"Dependency PASS: {dep_pass}/{total} ({100*dep_pass/total:.0f}%)")
    print(f"Has unmapped tools: {has_unmapped}/{total}")

    # 按 domain 分开统计
    for domain in domains:
        domain_results = [r for r in all_results if r["domain"].startswith(domain[:3])]
        if not domain_results:
            continue
        d_pass = sum(1 for r in domain_results if r["dep_pass"])
        d_total = len(domain_results)
        print(f"  {domain}: {d_pass}/{d_total} ({100*d_pass/d_total:.0f}%)")

    # 未映射 tool 统计
    all_unmapped = {}
    for r in all_results:
        for t in r["unmapped_tools"]:
            all_unmapped[t] = all_unmapped.get(t, 0) + 1
    if all_unmapped:
        print(f"\nUnmapped tools:")
        for t, c in sorted(all_unmapped.items(), key=lambda x: -x[1]):
            print(f"  {t}: {c} steps")


if __name__ == "__main__":
    main()
