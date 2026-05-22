"""
convert_schema.py
将 raw_dataset/{quantum,nuclear}/ 下的旧格式 JSON 批量转换为新 schema（01/02/03 三段式）。
输出到 dataset/foundation/{quantum,nuclear}/。

用法：
  python convert_schema.py --domain quantum [--batch-size 15] [--start 0]
  python convert_schema.py --domain nuclear [--batch-size 15]
  python convert_schema.py --domain quantum --exclude-subdomain general

断点续跑：自动跳过 output_dir 中已存在的文件。
默认排除 general 子领域（子领域标注不精确，质量差）。
"""

import argparse
import json
import os
import re
import sys
import time

import openai

# ── 路径配置 ──────────────────────────────────────────────────────────────────
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIRS = {
    "quantum": os.path.join(BASE, "raw_dataset", "quantum"),
    "nuclear": os.path.join(BASE, "raw_dataset", "nuclear"),
}
OUT_DIRS = {
    "quantum": os.path.join(BASE, "dataset", "foundation", "quantum"),
    "nuclear": os.path.join(BASE, "dataset", "foundation", "nuclear"),
}
DEMO_FILES = {
    "quantum": os.path.join(BASE, "templates", "demo_new_QN_0021.json"),
    "nuclear": os.path.join(BASE, "templates", "demo_new_NP_0001.json"),
}

# ── Schema 说明（系统提示） ────────────────────────────────────────────────────
SYSTEM_PROMPT = """\
你是一个物理数据集构建助手。你的任务是将旧格式的量子/核物理习题 JSON 转换为新的 Sci-Evo schema。

新 schema 结构：
{
  "id": "...",
  "meta": {
    "id": "...",
    "data_tier": "foundation",
    "domain": "quantum_mechanics | nuclear_physics",
    "subdomain": "...",
    "source": {
      "type": "textbook",
      "title": "...",
      "chapter_or_section": "...",
      "problem_number_or_doi": "..."
    },
    "difficulty": 1-5,
    "is_gold": false,
    "version": "1.0"
  },
  "01_initial_request": {
    "target_name": "求解目标的简短名称",
    "input_data": "已知条件，保留 LaTeX 公式",
    "user_intent": "解题意图（一句话）",
    "quantifiable_goal": "可量化的目标（能量本征值、跃迁概率、结合能等）"
  },
  "02_agent_trajectory": [
    {
      "step_index": 1,
      "thought": "[Background] 已知/已完成的内容。[Gap] 缺失/未解决的问题。[Decision] 选择了什么方法/工具，预期得到什么结果。",
      "action": "symbolic_derivation | numerical_computation | approximation | verification | correction",
      "tool": {
        "name": "见下方工具列表",
        "version": ""
      },
      "parameters": {},
      "observation": "该步骤的实际结果（含关键公式或数值）",
      "valid": true
    }
  ],
  "03_success_verification": {
    "validation_technique": "验证方法（量纲分析、极限情况检验、物理直觉验证等）",
    "metrics": {
      "物理量名": {
        "value": "数值或表达式",
        "unit": "单位",
        "interpretation": "物理意义说明"
      }
    },
    "final_verdict": "最终结论（一两句话）"
  }
}

tool.name 规范命名（只能用以下名称，选择时必须精确匹配实际操作）：

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

选择规则：
- 做傅里叶变换 → fourier_transform，不是 separation_of_variables
- 用 R=r₀A^(1/3) 估算密度/半径 → nuclear_radius_formula，不是 bethe_weizsacker_formula
- 应用 ∮p dq = nh → bohr_sommerfeld_quantization，不是 boundary_condition_matching
- 估算库仑势垒/聚变温度 → coulomb_barrier_estimate，不是 nuclear_decay_kinematics
- 计算截面×束流强度→反应率 → nuclear_reaction_rate，不是 nuclear_decay_kinematics

如果某步骤使用的物理方法在上述池中找不到合适名称，允许新增 tool，命名规范：
- snake_case 全小写，名称是物理方法本身（如 expectation_value_integral、matrix_element_method）
- 新增 tool 必须在 thought 或 observation 中有明确对应的物理操作支撑

要求：
1. thought 必须严格包含 [Background]、[Gap]、[Decision] 三段，每段一句话以上
2. observation 必须包含该步骤的关键结果（公式或数值），不能只写"计算完成"
3. 保留所有 LaTeX 公式，使用 $...$ 或 $$...$$ 格式
4. 只输出合法 JSON，不要加任何解释文字
"""


def load_demo(domain: str) -> dict:
    with open(DEMO_FILES[domain], encoding="utf-8") as f:
        return json.load(f)


def build_user_prompt(raw: dict, demo: dict) -> str:
    demo_str = json.dumps(demo, ensure_ascii=False, indent=2)
    raw_str = json.dumps(raw, ensure_ascii=False, indent=2)
    return f"""\
下面是一个新格式示例（few-shot）：

```json
{demo_str}
```

现在请将以下旧格式 JSON 转换为相同的新格式：

```json
{raw_str}
```

只输出转换后的 JSON，不要任何额外文字。"""


def convert_one(client: openai.OpenAI, raw: dict, demo: dict) -> dict:
    prompt = build_user_prompt(raw, demo)
    response = client.chat.completions.create(
        model="deepseek-chat",
        max_tokens=8192,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    msg = response.choices[0].message
    text = msg.content
    if not text:
        raise ValueError("API 返回内容为空")
    text = text.strip()
    # 去掉可能的 markdown 代码块包裹
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.rsplit("```", 1)[0].strip()
    # 修复非法 LaTeX 转义：将 JSON 字符串值中的单反斜杠（非法转义）替换为双反斜杠
    # 只处理 \x 形式中 x 不是合法 JSON 转义字符的情况
    valid_escapes = set('"\\' + '/bfnrtu')
    def fix_escape(m):
        ch = m.group(1)
        if ch in valid_escapes:
            return m.group(0)
        return '\\\\' + ch
    text = re.sub(r'\\(.)', fix_escape, text)
    return json.loads(text)


def main():
    parser = argparse.ArgumentParser(description="Convert raw_dataset to new schema")
    parser.add_argument("--domain", required=True, choices=["quantum", "nuclear"])
    parser.add_argument("--batch-size", type=int, default=15)
    parser.add_argument("--start", type=int, default=0, help="从第几个文件开始（0-indexed，用于手动跳过）")
    parser.add_argument(
        "--exclude-subdomain",
        nargs="+",
        default=["general"],
        metavar="SUBDOMAIN",
        help="排除指定子领域（默认排除 general）",
    )
    args = parser.parse_args()

    raw_dir = RAW_DIRS[args.domain]
    out_dir = OUT_DIRS[args.domain]
    os.makedirs(out_dir, exist_ok=True)

    # 收集待处理文件（跳过已存在的输出，排除指定子领域）
    all_files = sorted(f for f in os.listdir(raw_dir) if f.endswith(".json"))

    excluded = set(args.exclude_subdomain)
    filtered = []
    skipped_subdomain = 0
    for fname in all_files:
        in_path = os.path.join(raw_dir, fname)
        with open(in_path, encoding="utf-8") as f:
            d = json.load(f)
        subdomain = d.get("meta", {}).get("subdomain", "")
        if subdomain in excluded:
            skipped_subdomain += 1
            continue
        filtered.append(fname)

    pending = [f for f in filtered if not os.path.exists(os.path.join(out_dir, f))]
    pending = pending[args.start:]

    if skipped_subdomain:
        print(f"已排除子领域 {excluded}：跳过 {skipped_subdomain} 个文件")

    if not pending:
        print("没有待处理文件，全部已完成。")
        return

    batch = pending[: args.batch_size]
    print(f"待处理：{len(pending)} 个文件，本次处理：{len(batch)} 个")
    print(f"输出目录：{out_dir}\n")

    api_key = os.environ.get("DEEPSEEK_API_KEY", "")
    client = openai.OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
    demo = load_demo(args.domain)

    ok, fail = 0, 0
    for fname in batch:
        in_path = os.path.join(raw_dir, fname)
        out_path = os.path.join(out_dir, fname)

        with open(in_path, encoding="utf-8") as f:
            raw = json.load(f)

        print(f"  处理 {fname} ...", end=" ", flush=True)
        try:
            result = convert_one(client, raw, demo)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print("OK")
            ok += 1
        except json.JSONDecodeError as e:
            print(f"JSON 解析失败: {e}")
            fail += 1
        except openai.APIError as e:
            print(f"API 错误: {e}")
            fail += 1
            time.sleep(5)
        except Exception as e:
            print(f"未知错误: {e}")
            fail += 1

        time.sleep(0.5)  # 避免触发速率限制

    print(f"\n完成：{ok} 成功，{fail} 失败")
    remaining = len(pending) - len(batch)
    if remaining > 0:
        print(f"剩余 {remaining} 个文件，下次运行继续（断点续跑自动跳过已完成文件）")


if __name__ == "__main__":
    main()
