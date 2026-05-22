"""
step_classifier.py - 步骤操作性质分类器

对生成的每个 trajectory step，独立判断其 step_mode。
使用 DeepSeek API 做分类，结果缓存。

step_mode 分类：
  推进层（产出新物理量）:
    strict_derivation      - 严格数学/物理推导
    citation               - 引用文献结果
    empirical_approximation - 经验公式或近似
    numerical_fitting      - 数值计算/拟合
    analogy_extrapolation  - 类比外推

  决策层（影响路径但不产出量）:
    physical_argument      - 物理论证选路
    model_selection        - 模型/方法选择
    symmetry_constraint    - 对称性/守恒律约束
    error_analysis         - 误差分析
    consistency_check      - 一致性检验
    falsification          - 否定/排除某方法
"""

import json
import os
import re
import time

import openai

DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")

CLASSIFICATION_SYSTEM_PROMPT = """\
你是一个科学推理分析专家。给定一个物理推导步骤，判断该步骤的操作性质。

## 分类标签（必须选且只选一个）

### 推进层（产出新物理量）
- strict_derivation: 严格的数学/物理推导。特征：含公式变换、方程求解、积分计算、从已知量严格推出新量。
- citation: 引用文献或已知结果。特征：提到作者名/年份/文献编号，或"已知..."、"根据XX的结果..."。
- empirical_approximation: 经验公式或近似处理。特征："近似为..."、"忽略..."、"在XX条件下简化为..."。
- numerical_fitting: 数值计算或参数拟合。特征：代入数值、最小二乘拟合、chi^2优化。
- analogy_extrapolation: 类比或外推。特征："类似于..."、"推广到..."、"外推至..."。

### 决策层（不产出新物理量，影响推导路径选择）
- physical_argument: 基于物理原理的论证/选路。特征："由于XX效应..."、"物理上要求..."。
- model_selection: 选择模型/方法/参数化形式。特征："选择..."、"采用..."、"比较后决定用..."。
- symmetry_constraint: 对称性或守恒律约束。特征："由宇称守恒..."、"对称性要求..."。
- error_analysis: 误差分析/不确定度评估。特征："误差来源..."、"不确定度为..."。
- consistency_check: 一致性检验/验证。特征："代回验证..."、"与实验对比..."。
- falsification: 否定/排除某方法或结果。特征："排除..."、"不适用..."、"与实验矛盾..."。

## 判断规则
1. 如果步骤中有明确的公式推导过程（等号变换、积分、微分方程求解），选 strict_derivation
2. 如果步骤主要是"做选择"而非"算东西"，选决策层标签
3. 如果步骤引入了一个近似但同时也在推导，看主要动作：近似是手段还是目的
4. 一个步骤只能有一个标签

## 输出格式
严格输出 JSON：{"step_mode": "标签名", "confidence": 0.0-1.0, "reason": "一句话理由"}
只输出 JSON，不要任何其他文字。"""


class StepClassifier:
    """步骤操作性质分类器"""

    VALID_MODES = {
        "strict_derivation", "citation", "empirical_approximation",
        "numerical_fitting", "analogy_extrapolation",
        "physical_argument", "model_selection", "symmetry_constraint",
        "error_analysis", "consistency_check", "falsification",
    }

    DECISION_MODES = {
        "physical_argument", "model_selection", "symmetry_constraint",
        "error_analysis", "consistency_check", "falsification",
    }

    ADVANCING_MODES = {
        "strict_derivation", "citation", "empirical_approximation",
        "numerical_fitting", "analogy_extrapolation",
    }

    def __init__(self):
        self.client = openai.OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url="https://api.deepseek.com"
        )

    def classify(self, step: dict) -> dict:
        """
        分类单个步骤的 step_mode。

        Args:
            step: trajectory step dict (含 thought, tool, action, observation 等)

        Returns:
            {"step_mode": str, "confidence": float, "reason": str}
        """
        # 构建用户消息
        thought = step.get("thought", "")
        tool_name = step.get("tool", {}).get("name", "")
        action = step.get("action", "")
        observation = step.get("observation", "")

        user_msg = (
            f"步骤内容:\n"
            f"  thought: {thought[:500]}\n"
            f"  tool: {tool_name}\n"
            f"  action: {action}\n"
            f"  observation: {observation[:300]}\n"
        )

        for attempt in range(3):
            try:
                resp = self.client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": CLASSIFICATION_SYSTEM_PROMPT},
                        {"role": "user", "content": user_msg},
                    ],
                    temperature=0.1,
                    max_tokens=200,
                )
                raw = resp.choices[0].message.content.strip()
                raw = re.sub(r'^```(?:json)?\s*', '', raw)
                raw = re.sub(r'\s*```$', '', raw)
                result = json.loads(raw)

                mode = result.get("step_mode", "")
                if mode not in self.VALID_MODES:
                    result["step_mode"] = "strict_derivation"  # fallback
                return result

            except Exception as e:
                if attempt < 2:
                    time.sleep(2)
                else:
                    return {
                        "step_mode": "strict_derivation",
                        "confidence": 0.0,
                        "reason": f"classification failed: {e}"
                    }

    def is_decision(self, step_mode: str) -> bool:
        return step_mode in self.DECISION_MODES

    def triggers_hard_check(self, step_mode: str) -> bool:
        return step_mode == "strict_derivation"
