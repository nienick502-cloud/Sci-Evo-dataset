# Research_audited

本目录是 `dataset/final/Research` 的审核后副本，用于在不改动已发布原始数据的前提下保存分类和小修版本。

## 设立原因

`dataset/final/Research/` 是已经发布的原始 Research 层数据，保留原样有利于版本追溯、外部复现和公开数据对照。本目录不替代原始目录，也不改变 `dataset/metadata.jsonl` 中的 219 条主数据集计数。

新增 `Research_audited/` 的目的，是把审核结论和保守修正放在一个独立、可复核的位置：

- 原始样本保持不变，评审者可以直接比较原始版本和审核版本。
- 每条 Research 样本按风险级别进入对应目录，便于定位 P0/P1/P2/P3/PASS。
- 少量确定性 schema 修正只应用在副本中，避免对已发布数据做原地覆盖。
- 完整证据链保存在 `audit/research_layer/`，包括逐问题 JSONL、逐样本 CSV、P0 清单和人工复核清单。

## 分类目录

- `P0_reject_replace/`：源论文主体错配或列入替换处置的样本。
- `P1_must_fix/`：原始样本存在 schema 硬错误；本副本已做确定性小修，列入重点复核。
- `P2_review_needed/`：内容或子领域匹配需要人工复核的样本。
- `P3_polish/`：主体可用但有格式/文本清洗项的样本。
- `PASS/`：当前审核规则未命中问题的样本。

## 本副本应用的保守修正

- 将少量非法 `action` 映射到 schema 允许的 action。
- 将字符串形式的 `error_tag: "null"` 转为 JSON `null`。
- 为 `valid=false` 且缺少 `error_reason` 的步骤补充审核说明。
- 将明显写成条件说明的 `metrics.*.unit` 移入 `interpretation`，并把 `unit` 置为 `condition`。

## 样本数

- `P0_reject_replace`：1
- `P1_must_fix`：5
- `P2_review_needed`：26
- `P3_polish`：76
- `PASS`：51

完整审核证据见 `audit/research_layer/`。
