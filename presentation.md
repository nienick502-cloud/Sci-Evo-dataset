---
marp: true
theme: default
paginate: true
backgroundColor: #ffffff
style: |
  h1 {
    color: #1a365d;
    border-bottom: 2px solid #3182ce;
    padding-bottom: 0.2em;
  }
  h2 {
    color: #2b6cb0;
  }
  strong {
    color: #c53030;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  section {
    font-size: 26px;
    font-family: 'Segoe UI', system-ui, sans-serif;
  }
  .footnote {
    position: absolute;
    bottom: 20px;
    font-size: 14px;
    color: #718096;
  }
---

<!-- _class: lead -->
# Physics-PreProc-QN
## 核物理与量子力学深度推理数据集
**构建大模型时代的“过程监督”灯塔**

**团队：** Sci-Evo 我能突破束缚的
**发布日期：** 2026年5月

---

# 1. 痛点与动机 (Motivation)

当通用大模型面对高阶硬核物理时，往往会陷入**“形式-实质鸿沟 (Form-Substance Gap)”**：
- **形式上极其自信**：能够生成排版精美的 LaTeX 推导和代码。
- **实质上漏洞百出**：常常忽略隐藏前提、误用近似或选错模型。

**行业痛点：**
目前开源领域**极度缺乏**包含真实“试错、反思与修正”过程的垂直科学数据集。没有失败轨迹，大模型就无法学习如何避开思维陷阱。

---

# 2. 数据集全貌 (Dataset Overview)

Physics-PreProc-QN 是一个**聚焦试错过程**的双层架构数据集。

- **规模**：总计 **219** 篇深度推理轨迹（含数十万字推导）。
- **工具生态**：包含 **114** 种独立工具（84 种核物理工具 + 14 种 ML 工具）。
- **双层认知梯度**：
  - **基础层 (60 篇)**：提取自经典教科书，建立确定性的领域认知基线。
  - **研究层 (159 篇)**：提取自 arXiv 前沿论文，覆盖 8 个核物理子领域，捕获真实科研中的“预测-失败-修正”动态。

---

# 3. 项目整体架构 (Architecture Workflow)

我们的工程实现与开源目录结构高度映射：

<div class="columns">
<div>

1. **事实获取** (`raw_pdf/` & `parsed/`)
   利用 MinerU 提取论文文本与公式。
2. **能力封装** (`feynman-skill/`)
   定义具有严格输入输出 API 的物理工具。
3. **因果推演** (`scripts/`)
   DFS 引擎驱动 Agent 进行受限探索。

</div>
<div>

4. **语义评审** (`agent_Review/`)
   六维 LLM 专家评审盲测。
5. **成品沉淀** (`dataset/final/`)
   格式清洗与结构化后的最终 JSON 语料。

</div>
</div>

---

# 4. 核心技术一：DFS 约束生成引擎

为了防止大模型的“幻觉”推导，我们为 Agent 装上了“刹车”：

- **`requires` $\rightarrow$ `provides` 依赖签名**：
  每个工具调用前，DFS 引擎必须检查前置物理量是否已经通过合法途径计算得出。
- **物理因果性硬检查**：
  如果违背逻辑断层，该步骤的 `valid` 标签会被**强制打为 false**，并强制 Agent 产生对应的 `error_tag`。

> 这种机制确保了数据集中的错误是**真实的物理错误**，而不是格式幻觉。

---

# 5. 核心技术二：Crystal 经验系统

Agent 不能在同一个坑里跌倒两次。

- **操作级经验 (Operational Level)**：
  我们在运行中积累“如果处于 A 状态，不要用 B 近似”的规则池（Rule Pool）。
- **跨论文迁移**：
  实验证明，在 $6/8$ 的核物理子领域中，操作级规则可以实现**同类型课题间的有效迁移**，显著降低后续论文解析的搜索深度。
- **粒度边界发现**：
  证实了方法论级别（Methodological）的顶层经验难以直接作为操作规则使用，揭示了 Agent 认知边界。

---

# 6. 数据集结构：解码 JSON

每个样本都是一个信息密度极高的结构化字典：

- **`01_initial_request`**：
  定义了物理问题的**初始已知条件**和**可定量验证的目标**。
- **`02_agent_trajectory` (核心价值)**：
  记录时序推理链。包括基于 `[Background] -> [Gap] -> [Decision]` 的三段式 `thought`。
- **核心监督信号**：
  - `valid` (布尔值)：判定当前推导是否成立。
  - `error_tag`：6 种预定义的物理错误分类（如 `missing_physical_effect`）。
- **`03_success_verification`**：
  比对实验值与理论预测值的差异，给出是否复现原论文的结论。

---

# 7. 质量评估与核心发现

我们采用了三重严格审计，拒绝自欺欺人：

1. **结构审计 (Checklist)**：
   **63.5% (101/159)** 的论文达到 GOLD 候选标准（结构完备）。
2. **语义审计 (LLM 盲审)**：
   六维评分均分达 **0.880**，但受限于超重核等前沿领域的未知性，极少数突破绝对阈值。
3. **核心发现 (0.304 Gap)**：
   形式合规性 (0.925) 与 物理实质正确性 (0.621) 之间存在 **0.304 的显著鸿沟**，印证了本数据集解决的正是大模型的认知软肋！

---

# 8. 应用场景：如何使用我们的数据？

开发者可直接提取 `dataset/final/` 中的数据进行模型赋能：

1. **过程奖励模型 (PRM) 训练**：
   提取 `valid: false` 和对应的 `error_tag`，完美构建 Positive/Negative 推理对。
2. **Tool-Augmented Agent 微调**：
   超过 488 种正确与错误的工具调用序列，可极大提升模型在复杂科学场景下的 Tool-use 鲁棒性。
3. **深度推理 Benchmark**：
   用于测试模型在面对信息不全、需要中途撤回和反思时的纠错能力。

---

<!-- _class: lead -->
# 总结与展望

Physics-PreProc-QN 提供了一个极其透明的科学推理语料库。
**我们记录的每一次失败，都是未来 AI 向未知物理世界探索的基石。**

代码与数据集已全面开源，期待社区的共建！
**感谢评委聆听！**
