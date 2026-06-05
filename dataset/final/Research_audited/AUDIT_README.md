# Research_audited

本目录是 `dataset/final/Research` 的审核后副本，用于在不改动已发布原始数据的前提下保存分类和小修版本。

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
