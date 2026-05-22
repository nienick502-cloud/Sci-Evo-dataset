"""
fix_tool_names.py
对 dataset/foundation/ 下已转换的文件做 tool 命名校正 pass。
只修改 tool.name 字段，不改动其他内容。

用法：
  python fix_tool_names.py --domain quantum
  python fix_tool_names.py --domain nuclear
  python fix_tool_names.py --domain all
"""

import argparse
import json
import os
import sys
import time

import openai

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIRS = {
    "quantum": os.path.join(BASE, "dataset", "foundation", "quantum"),
    "nuclear": os.path.join(BASE, "dataset", "foundation", "nuclear"),
}

SYSTEM_PROMPT = """\
你是一个物理数据集质量审核助手。你的任务是检查 JSON 中每个 agent trajectory 步骤的 tool.name 字段，
判断它是否准确描述了该步骤实际使用的物理方法，如有错误则修正。

## 现有 tool 池（优先从中选择）

量子力学：
- separation_of_variables    — 对偏微分方程做变量分离（如求解定态薛定谔方程）
- fourier_transform          — 表象变换（位置↔动量表象的傅里叶变换）
- boundary_condition_matching — 在势能分区边界匹配波函数及其导数
- bohr_sommerfeld_quantization — 应用 Bohr-Sommerfeld 量子化条件 ∮p dq = nh
- normalization_condition    — 归一化波函数
- ladder_operator_method     — 升降算符代数（谐振子、角动量）
- perturbation_theory_first_order
- perturbation_theory_second_order
- variational_method
- wkb_approximation
- angular_momentum_coupling  — 角动量耦合（CG系数、j1⊗j2 合成）
- symmetry_argument          — 利用对称性（宇称、时间反演等）简化计算

核物理：
- shell_filling              — 核壳模型填充规则
- pairing_rule               — 配对规则（自旋-宇称）
- bethe_weizsacker_formula   — 使用半经验质量公式（SEMF）计算结合能或质量
- nuclear_radius_formula     — 使用 R=r₀A^(1/3) 做几何/密度估算（不涉及 SEMF）
- coulomb_barrier_estimate   — 估算库仑势垒高度或穿透温度
- nuclear_decay_kinematics   — 衰变运动学（Q值、反冲、能量守恒）
- nuclear_reaction_rate      — 核反应率、截面与束流强度的关系
- optical_model_potential    — 光学模型势

通用验证：
- dimensional_analysis       — 量纲分析
- limiting_case_check        — 极限情况检验
- physical_intuition_check   — 物理直觉验证

## 扩展规则

如果某步骤使用的物理方法在上述池中找不到合适的名称，**允许新增 tool**，命名规范：
- 使用 snake_case，全小写
- 名称必须是物理方法本身，不是操作描述（如 `expectation_value_calculation` 不好，`matrix_element_method` 更好）
- 新增的 tool 必须在 thought 或 observation 中有明确对应的物理操作支撑

## 常见错误模式（必须修正）

- 做傅里叶变换却用了 separation_of_variables → fourier_transform
- 用 R=r₀A^(1/3) 估算密度却用了 bethe_weizsacker_formula → nuclear_radius_formula
- 应用 ∮p dq = nh 却用了 boundary_condition_matching → bohr_sommerfeld_quantization
- 估算库仑势垒/聚变温度却用了 nuclear_decay_kinematics → coulomb_barrier_estimate
- 计算截面×束流强度→反应率却用了 nuclear_decay_kinematics → nuclear_reaction_rate
- 代入能量公式求本征值却用了 angular_momentum_coupling → separation_of_variables 或更精确的名称
- 计算期望值积分却用了 boundary_condition_matching → expectation_value_integral 或 normalization_condition

## 输出要求

1. 只输出修正后的完整 JSON，不要任何解释文字
2. 除 tool.name 外，不修改任何其他字段
3. 如果所有 tool.name 都已正确，原样输出 JSON
"""


def fix_one(client: openai.OpenAI, data: dict) -> dict:
    data_str = json.dumps(data, ensure_ascii=False, indent=2)
    response = client.chat.completions.create(
        model="deepseek-chat",
        max_tokens=8192,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"请检查并修正以下 JSON 的 tool.name 字段：\n\n```json\n{data_str}\n```"},
        ],
    )
    text = response.choices[0].message.content
    if not text:
        raise ValueError("API 返回内容为空")
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.rsplit("```", 1)[0].strip()
    return json.loads(text)


def process_domain(client: openai.OpenAI, domain: str):
    out_dir = OUT_DIRS[domain]
    files = sorted(f for f in os.listdir(out_dir) if f.endswith(".json"))
    print(f"\n[{domain}] {len(files)} 个文件")

    ok, changed, fail = 0, 0, 0
    for fname in files:
        path = os.path.join(out_dir, fname)
        with open(path, encoding="utf-8") as f:
            original = json.load(f)

        # 提取原始 tool 列表
        orig_tools = [s["tool"]["name"] for s in original.get("02_agent_trajectory", [])]

        print(f"  {fname} ...", end=" ", flush=True)
        try:
            fixed = fix_one(client, original)
            new_tools = [s["tool"]["name"] for s in fixed.get("02_agent_trajectory", [])]

            if orig_tools != new_tools:
                diffs = [(i+1, o, n) for i, (o, n) in enumerate(zip(orig_tools, new_tools)) if o != n]
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(fixed, f, ensure_ascii=False, indent=2)
                print(f"修正 {len(diffs)} 处: " + ", ".join(f"step{s}:{o}→{n}" for s, o, n in diffs))
                changed += 1
            else:
                print("OK（无需修改）")
                ok += 1
        except json.JSONDecodeError as e:
            print(f"JSON 解析失败: {e}")
            fail += 1
        except Exception as e:
            print(f"错误: {e}")
            fail += 1

        time.sleep(0.3)

    print(f"  [{domain}] 完成：{ok} 无需修改，{changed} 已修正，{fail} 失败")


def main():
    parser = argparse.ArgumentParser(description="Fix tool names in foundation dataset")
    parser.add_argument("--domain", required=True, choices=["quantum", "nuclear", "all"])
    args = parser.parse_args()

    api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    client = openai.OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

    domains = ["quantum", "nuclear"] if args.domain == "all" else [args.domain]
    for domain in domains:
        process_domain(client, domain)


if __name__ == "__main__":
    main()
