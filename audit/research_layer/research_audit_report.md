# Research 层审核报告

本报告由 `scripts/audit/research_layer_audit.py` 生成。报告以证据为核心，仅用于审核，不修改数据集文件。

## 总览

- 已扫描 Research 样本数：159
- 问题记录数：183
- P0 删除或替换：1 条样本
- P1 必须修复：5 条样本
- P2 人工复核：26 条样本
- P3 格式清理：76 条样本
- PASS 通过：51 条样本

## 子领域风险分布

| 子领域 | 样本数 | P0 | P1 | P2 | P3 | PASS |
|---|---:|---:|---:|---:|---:|---:|
| `alpha_decay_cluster_model` | 14 | 0 | 0 | 5 | 5 | 4 |
| `alpha_decay_double_folding` | 13 | 0 | 0 | 2 | 9 | 2 |
| `alpha_decay_liquid_drop` | 12 | 0 | 0 | 2 | 5 | 5 |
| `alpha_decay_shell_model` | 17 | 0 | 0 | 4 | 8 | 5 |
| `alpha_decay_wkb` | 24 | 0 | 0 | 2 | 20 | 2 |
| `deep_learning_nuclear` | 37 | 0 | 4 | 6 | 11 | 16 |
| `ml_alpha_halflife` | 3 | 1 | 0 | 1 | 1 | 0 |
| `nuclear_scattering` | 39 | 0 | 1 | 4 | 17 | 17 |

## 问题类别计数

- `metric_unit_contains_condition`: 115
- `paper_methods_unsupported_by_source`: 15
- `paper_derivation_template_like`: 11
- `final_verdict_failure_points_not_referenced`: 10
- `subdomain_low_keyword_support`: 6
- `key_formulas_not_used_in_derivation`: 6
- `invalid_step_missing_error_reason`: 5
- `bad_error_tag`: 4
- `invalid_step_missing_error_tag`: 4
- `bad_action`: 3
- `source_subdomain_low_keyword_support`: 2
- `source_subject_mismatch`: 1
- `empty_paper_facts_key_results`: 1

## P0 删除或替换清单

- `NPP_0196` `ml_alpha_halflife` `arxiv_2103.04667`: Voting in Transfer Learning System for Ground-Based Cloud Classification
  - 证据：parsed 源文件呈现非核物理主题信号（['\\bcloud(s)?\\b', 'ground[- ]based cloud', 'meteorolog', 'climate change', 'weather']），但 final 样本呈现核物理主题信号（['\\balpha\\b', '\\\\alpha']）。parsed 标题='Voting in Transfer Learning System for Ground-Based Cloud Classification'

## P1 必须修复样本

- `NPP_0117` `deep_learning_nuclear`: bad_error_tag, invalid_step_missing_error_reason, invalid_step_missing_error_tag
- `NPP_0120` `deep_learning_nuclear`: bad_action
- `NPP_0122` `deep_learning_nuclear`: bad_action
- `NPP_0141` `deep_learning_nuclear`: bad_action
- `NPP_0179` `nuclear_scattering`: invalid_step_missing_error_reason

## P2 人工复核样本

- `NPP_0009` `alpha_decay_wkb` `arxiv_1609.00847`: subdomain_low_keyword_support
- `NPP_0025` `alpha_decay_wkb` `arxiv_nucl-th_0510082`: empty_paper_facts_key_results
- `NPP_0036` `alpha_decay_liquid_drop` `arxiv_2101.07142`: paper_methods_unsupported_by_source
- `NPP_0037` `alpha_decay_liquid_drop` `arxiv_2201.08268`: subdomain_low_keyword_support
- `NPP_0065` `alpha_decay_shell_model` `arxiv_2108.12484`: subdomain_low_keyword_support
- `NPP_0069` `alpha_decay_shell_model` `arxiv_2407.18025`: key_formulas_not_used_in_derivation
- `NPP_0070` `alpha_decay_shell_model` `arxiv_2506.02684`: paper_methods_unsupported_by_source
- `NPP_0073` `alpha_decay_shell_model` `arxiv_1604.00296`: paper_methods_unsupported_by_source
- `NPP_0078` `alpha_decay_cluster_model` `arxiv_1505.05013`: paper_methods_unsupported_by_source
- `NPP_0079` `alpha_decay_cluster_model` `arxiv_1809.04952`: paper_methods_unsupported_by_source
- `NPP_0081` `alpha_decay_cluster_model` `arxiv_2305.05613`: paper_methods_unsupported_by_source
- `NPP_0088` `alpha_decay_cluster_model` `arxiv_2602.24175`: paper_methods_unsupported_by_source
- `NPP_0090` `alpha_decay_cluster_model` `arxiv_nucl-th_0510082`: key_formulas_not_used_in_derivation
- `NPP_0092` `alpha_decay_double_folding` `arxiv_0803.4151`: paper_methods_unsupported_by_source
- `NPP_0107` `alpha_decay_double_folding` `arxiv_nucl-th_0602008`: paper_methods_unsupported_by_source
- `NPP_0110` `deep_learning_nuclear` `arxiv_1301.2407`: paper_methods_unsupported_by_source
- `NPP_0119` `deep_learning_nuclear` `arxiv_2003.07050`: paper_methods_unsupported_by_source
- `NPP_0121` `deep_learning_nuclear` `arxiv_2101.12117`: paper_methods_unsupported_by_source
- `NPP_0123` `deep_learning_nuclear` `arxiv_2112.12562`: key_formulas_not_used_in_derivation
- `NPP_0126` `deep_learning_nuclear` `arxiv_2208.04783`: paper_methods_unsupported_by_source
- `NPP_0129` `deep_learning_nuclear` `arxiv_2306.11314`: subdomain_low_keyword_support
- `NPP_0153` `nuclear_scattering` `arxiv_1009.0545`: paper_methods_unsupported_by_source, subdomain_low_keyword_support
- `NPP_0154` `nuclear_scattering` `arxiv_1206.4445`: key_formulas_not_used_in_derivation
- `NPP_0177` `nuclear_scattering` `arxiv_2404.01653`: key_formulas_not_used_in_derivation
- `NPP_0189` `nuclear_scattering` `arxiv_nucl-th_9212009`: key_formulas_not_used_in_derivation
- `NPP_0228` `ml_alpha_halflife` `arxiv_2603.07983`: source_subdomain_low_keyword_support, subdomain_low_keyword_support

## 处置流程

1. P0：核验证据后移除或替换。
2. P1：发布前完成 schema 错误修复。
3. P2：读取证据摘录和对应 parsed Markdown 源文件，完成复核判定。
4. P3：内容取舍稳定后，批量清理格式和文本问题。

## 输出文件

- `research_audit_findings.jsonl`：每行一条 finding，便于机器读取。
- `research_audit_summary.csv`：每行一条样本摘要。
- `p0_reject_candidates.txt`：P0 删除或替换清单。
- `p2_manual_review_queue.md`：证据复核清单。
