# Research 层复核清单

本清单包含 P0/P1/P2 样本。P0/P1 同步列入清单，用于在数据处置前核验证据。

## NPP_0196 - P0 删除或替换

- Subdomain: `ml_alpha_halflife`
- Source: `arxiv_2103.04667`
- Final 标题: Voting in Transfer Learning System for Ground-Based Cloud Classification
- Parsed 标题: Voting in Transfer Learning System for Ground-Based Cloud Classification
- 处置项: 从 final 集合移除，或以同子领域核物理论文样本替换。
- 问题记录:
  - `P0` `source_subject_mismatch`: parsed 源文件呈现非核物理主题信号（['\\bcloud(s)?\\b', 'ground[- ]based cloud', 'meteorolog', 'climate change', 'weather']），但 final 样本呈现核物理主题信号（['\\balpha\\b', '\\\\alpha']）。parsed 标题='Voting in Transfer Learning System for Ground-Based Cloud Classification'
  - `P2` `source_subdomain_low_keyword_support`: parsed 源文件仅命中 1/3 组预期子领域信号：['machine/deep/neural']。parsed_title='Voting in Transfer Learning System for Ground-Based Cloud Classification'
  - `P3` `metric_unit_contains_condition`: metrics.half_life 的 unit 字段疑似写入条件说明：'Z=120, A=298, 使用Voting Learning集成预测'
  - `P3` `metric_unit_contains_condition`: metrics.preformation_probability 的 unit 字段疑似写入条件说明：'Z=120, A=298, 基于RMF(NL3)计算'
  - `P3` `paper_derivation_template_like`: 6/8 条 paper_derivation observation 含泛化或模板化表述

## NPP_0117 - P1 必须修复

- Subdomain: `deep_learning_nuclear`
- Source: `arxiv_1911.13092`
- Final 标题: Machine learning the deuteron
- Parsed 标题: Machine learning the deuteron
- 处置项: 发布前修复 schema/字段错误；必要时重新生成 metadata。
- 问题记录:
  - `P1` `bad_error_tag`: 第 3 步 error_tag 非法：'null'
  - `P1` `bad_error_tag`: 第 5 步 error_tag 非法：'null'
  - `P1` `bad_error_tag`: 第 6 步 error_tag 非法：'null'
  - `P1` `bad_error_tag`: 第 7 步 error_tag 非法：'null'
  - `P1` `invalid_step_missing_error_reason`: 第 3 步 valid=false，但缺少 error_reason
  - `P1` `invalid_step_missing_error_reason`: 第 5 步 valid=false，但缺少 error_reason
  - `P1` `invalid_step_missing_error_reason`: 第 6 步 valid=false，但缺少 error_reason
  - `P1` `invalid_step_missing_error_reason`: 第 7 步 valid=false，但缺少 error_reason
  - ... 其余 5 条见 JSONL

## NPP_0120 - P1 必须修复

- Subdomain: `deep_learning_nuclear`
- Source: `arxiv_2005.04636`
- Final 标题: The study of Nuclear binding energy for $\mathbf { A } \geq \mathbf { 1 0 0 }$ based on Odd-Even staggering of nuclear masses
- Parsed 标题: The study of Nuclear binding energy for $\mathbf { A } \geq \mathbf { 1 0 0 }$ based on Odd-Even staggering of nuclear masses
- 处置项: 发布前修复 schema/字段错误；必要时重新生成 metadata。
- 问题记录:
  - `P1` `bad_action`: 第 22 步 action 非法：'model_prediction'

## NPP_0122 - P1 必须修复

- Subdomain: `deep_learning_nuclear`
- Source: `arxiv_2105.02445`
- Final 标题: Machine learning the nuclear mass
- Parsed 标题: Machine learning the nuclear mass
- 处置项: 发布前修复 schema/字段错误；必要时重新生成 metadata。
- 问题记录:
  - `P1` `bad_action`: 第 12 步 action 非法：'feature_engineering'
  - `P3` `metric_unit_contains_condition`: metrics.result_1 的 unit 字段疑似写入条件说明：'对已知核素测试集，Z=1-118'

## NPP_0141 - P1 必须修复

- Subdomain: `deep_learning_nuclear`
- Source: `arxiv_2508.01001`
- Final 标题: Criticality analysis of nuclear binding energy neural networks
- Parsed 标题: Criticality analysis of nuclear binding energy neural networks
- 处置项: 发布前修复 schema/字段错误；必要时重新生成 metadata。
- 问题记录:
  - `P1` `bad_action`: 第 7 步 action 非法：'physical_argument'

## NPP_0179 - P1 必须修复

- Subdomain: `nuclear_scattering`
- Source: `arxiv_2501.03958`
- Final 标题: Nuclear cross sections from low-energy interactions
- Parsed 标题: Nuclear cross sections from low-energy interactions
- 处置项: 发布前修复 schema/字段错误；必要时重新生成 metadata。
- 问题记录:
  - `P1` `invalid_step_missing_error_reason`: 第 3 步 valid=false，但缺少 error_reason
  - `P2` `paper_methods_unsupported_by_source`: 3/5 个 paper_methods 在 parsed 源文件中缺少词面支持：['dyson_equation', 'kallen_lehmann_representation', 'coupled_cluster_method']

## NPP_0009 - P2 人工复核

- Subdomain: `alpha_decay_wkb`
- Source: `arxiv_1609.00847`
- Final 标题: Shell plus pairing effect arguments for cluster preformation at the nuclear surface in cold fission
- Parsed 标题: Shell plus pairing effect arguments for cluster preformation at the nuclear surface in cold fission
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `subdomain_low_keyword_support`: 样本内容仅命中 1/2 组预期子领域信号：['wkb/tunnel/penetrab']。title='Shell plus pairing effect arguments for cluster preformation at the nuclear surface in cold fission'
  - `P3` `final_verdict_failure_points_not_referenced`: final_verdict 未引用 failure_points：['预测将预形成因子S_pre作为独立于WKB穿透概率的乘性因子引入，并声称论文方法中未明确提及预形成因子。然而论文实际推导中，预形成因子P_pre是通过谱因子从微观波函数重叠积分直接计算的，并非独立经验参数；且论文中预形成因子是衰变宽度公式的固有组成部分，并非在WKB之后额外引入。预测的物理图像（预形成因子作为后加的经验修正）与论文的微观自洽处理不符。', '预测采用经验指数形式S_pre = S_0 * exp(-c * |δE_shell(2) + δE_pair(2)| / Q)来建模预形成因子，但论文中预形成因子是通过不对称双中心壳模型和BCS理论直接计算谱因子得到的，不依赖于这种经验系统学近似。该经验形式忽略了预形成因子对波函数重叠积分的具体依赖，且将壳修正和对修正作为指数衰减的输入在物理上缺乏微观基础，属于在该物理情境下不适用的近似。', '预测引入贝叶斯不确定性量化来评估模型参数的后验分布，但论文的宏观-微观方法中并未使用贝叶斯框架；论文通过直接拟合实验数据确定参数（如S_0, c），而非通过后验分布更新。更重要的是，预测将贝叶斯步骤置于预形成因子建模之后，试图通过训练数据集调整预形成因子参数，但论文中预形成因子是从微观模型直接计算的，不依赖于实验数据的统计拟合。这种统计推断方法忽略了论文中预形成因子的微观确定性本质。', '预测继续使用贝叶斯后验分布来更新模型权重（如S_0和c的后验均值），但论文中预形成因子参数并非通过贝叶斯统计确定，而是通过微观模型（ATCSM和BCS）直接计算谱因子得到。预测将模型权重与后验分布关联，试图量化不同预形成因子形式的置信度，但论文方法中预形成因子形式是确定的（基于波函数重叠），不存在多种假设需要权重分配。这种统计处理忽略了论文中预形成因子的微观物理基础。']

## NPP_0025 - P2 人工复核

- Subdomain: `alpha_decay_wkb`
- Source: `arxiv_nucl-th_0510082`
- Final 标题: $\alpha$ -nucleus potential for $\alpha$ -decay and sub-barrier fusion
- Parsed 标题: $\alpha$ -nucleus potential for $\alpha$ -decay and sub-barrier fusion
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `empty_paper_facts_key_results`: paper_facts.key_results 为空

## NPP_0036 - P2 人工复核

- Subdomain: `alpha_decay_liquid_drop`
- Source: `arxiv_2101.07142`
- Final 标题: I. INTRODUCTION
- Parsed 标题: I. INTRODUCTION
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 3/5 个 paper_methods 在 parsed 源文件中缺少词面支持：['wkb_approximation', 'classical_vibration_energy', 'preformation_factor_model']
  - `P3` `metric_unit_contains_condition`: metrics.half_life 的 unit 字段疑似写入条件说明：'Z=104-118已知核素'

## NPP_0037 - P2 人工复核

- Subdomain: `alpha_decay_liquid_drop`
- Source: `arxiv_2201.08268`
- Final 标题: On the Stability of Superheavy Nuclei
- Parsed 标题: On the Stability of Superheavy Nuclei
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `subdomain_low_keyword_support`: 样本内容仅命中 1/2 组预期子领域信号：['liquid/drop/gldm']。title='On the Stability of Superheavy Nuclei'

## NPP_0065 - P2 人工复核

- Subdomain: `alpha_decay_shell_model`
- Source: `arxiv_2108.12484`
- Final 标题: Energy dependent ratios of level-density parameters in superheavy nuclei
- Parsed 标题: Energy dependent ratios of level-density parameters in superheavy nuclei
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `subdomain_low_keyword_support`: 样本内容仅命中 1/2 组预期子领域信号：['decay/half life/half-life']。title='Energy dependent ratios of level-density parameters in superheavy nuclei'
  - `P3` `metric_unit_contains_condition`: metrics.a_f_a_n 的 unit 字段疑似写入条件说明：'核素范围 Z=112-120，激发能 0-40 MeV'
  - `P3` `metric_unit_contains_condition`: metrics.a_n 的 unit 字段疑似写入条件说明：'核素范围 Z=112-120'

## NPP_0069 - P2 人工复核

- Subdomain: `alpha_decay_shell_model`
- Source: `arxiv_2407.18025`
- Final 标题: Alpha-decay from $^ { 4 4 }$ Ti: Microscopic alpha half-live calculation using normalized spectroscopic factor
- Parsed 标题: Alpha-decay from $^ { 4 4 }$ Ti: Microscopic alpha half-live calculation using normalized spectroscopic factor
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `key_formulas_not_used_in_derivation`: paper_derivation observation 中未检出 key_formulas 的引用或注入痕迹

## NPP_0070 - P2 人工复核

- Subdomain: `alpha_decay_shell_model`
- Source: `arxiv_2506.02684`
- Final 标题: Deformed magic numbers at ${ \bf { { N = 1 7 8 } } }$ and ${ Z = } \mathbf { 1 } 2 \mathbf { 0 }$ , 124 in the ${ \bf 1 1 2 } \le N \le { \bf 1 9 0 }$ superheavy region from Skyrme mean-field calculations
- Parsed 标题: Deformed magic numbers at ${ \bf { { N = 1 7 8 } } }$ and ${ Z = } \mathbf { 1 } 2 \mathbf { 0 }$ , 124 in the ${ \bf 1 1 2 } \le N \le { \bf 1 9 0 }$ superheavy region from Skyrme mean-field calculations
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 3/5 个 paper_methods 在 parsed 源文件中缺少词面支持：['seniority_pairing_force', 'gauss_hermite_integration', 'slater_approximation']
  - `P3` `metric_unit_contains_condition`: metrics.result_1 的 unit 字段疑似写入条件说明：'核素^{298}114（Z=114, N=184），使用SkM*参数集'
  - `P3` `metric_unit_contains_condition`: metrics.result_2 的 unit 字段疑似写入条件说明：'核素^{298}114（Z=114, N=184），使用SkM*参数集'

## NPP_0073 - P2 人工复核

- Subdomain: `alpha_decay_shell_model`
- Source: `arxiv_1604.00296`
- Final 标题: Predictions on the alpha decay half lives of Superheavy nuclei with $\mathbf { Z } = \mathbf { 1 } \mathbf { 1 } 3$ in the range $2 5 5 \leq \mathrm { A } \leq 3 1 4$
- Parsed 标题: Predictions on the alpha decay half lives of Superheavy nuclei with $\mathbf { Z } = \mathbf { 1 } \mathbf { 1 } 3$ in the range $2 5 5 \leq \mathrm { A } \leq 3 1 4$
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 3/4 个 paper_methods 在 parsed 源文件中缺少词面支持：['viola_seaborg_formula', 'generalized_liquid_drop_model', 'density_dependent_cluster_model']

## NPP_0078 - P2 人工复核

- Subdomain: `alpha_decay_cluster_model`
- Source: `arxiv_1505.05013`
- Final 标题: Single universal curve for  decay derived from semi-microscopic calculations
- Parsed 标题: Single universal curve for  decay derived from semi-microscopic calculations
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 3/4 个 paper_methods 在 parsed 源文件中缺少词面支持：['double_folding_model', 'multipole_expansion_method', 'angle_averaging']
  - `P3` `metric_unit_contains_condition`: metrics.half_life 的 unit 字段疑似写入条件说明：'所有考虑的核素（166个偶偶核、117个奇偶核、141个偶奇核、72个奇奇核）'

## NPP_0079 - P2 人工复核

- Subdomain: `alpha_decay_cluster_model`
- Source: `arxiv_1809.04952`
- Final 标题: Cluster-Daughter Overlap as a New Probe of Alpha-Cluster Formation in Medium-Mass and Heavy Even-Even Nuclei
- Parsed 标题: Cluster-Daughter Overlap as a New Probe of Alpha-Cluster Formation in Medium-Mass and Heavy Even-Even Nuclei
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 3/4 个 paper_methods 在 parsed 源文件中缺少词面支持：['local_density_approximation', 'double_folding_procedure', 'm3y_nucleon_nucleon_interaction']
  - `P3` `paper_derivation_template_like`: 6/8 条 paper_derivation observation 含泛化或模板化表述

## NPP_0081 - P2 人工复核

- Subdomain: `alpha_decay_cluster_model`
- Source: `arxiv_2305.05613`
- Final 标题: Quest for a Universal Cluster Preformation Formula: A new paradigm for estimating the cluster formation energy
- Parsed 标题: Quest for a Universal Cluster Preformation Formula: A new paradigm for estimating the cluster formation energy
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 3/4 个 paper_methods 在 parsed 源文件中缺少词面支持：['relativistic_mean_field', 'double_folding_procedure', 'wkb_approximation']

## NPP_0088 - P2 人工复核

- Subdomain: `alpha_decay_cluster_model`
- Source: `arxiv_2602.24175`
- Final 标题: Theoretical Studies of $\alpha$ Clustering in Nuclei and Beyond
- Parsed 标题: Theoretical Studies of $\alpha$ Clustering in Nuclei and Beyond
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 4/4 个 paper_methods 在 parsed 源文件中缺少词面支持：['relativistic_mean_field_theory', 'coupled_channels_method', 'double_folding_potential', 'wenzel_kramers_brillouin_approximation']
  - `P3` `metric_unit_contains_condition`: metrics.half_life 的 unit 字段疑似写入条件说明：'Z=120, A=294, 与实验值偏差在因子2以内'
  - `P3` `metric_unit_contains_condition`: metrics.preformation_factor 的 unit 字段疑似写入条件说明：'Z=120同位素链，A=256-304，随中子数增加而增大'

## NPP_0090 - P2 人工复核

- Subdomain: `alpha_decay_cluster_model`
- Source: `arxiv_nucl-th_0510082`
- Final 标题: $\alpha$ -nucleus potential for $\alpha$ -decay and sub-barrier fusion
- Parsed 标题: $\alpha$ -nucleus potential for $\alpha$ -decay and sub-barrier fusion
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `key_formulas_not_used_in_derivation`: paper_derivation observation 中未检出 key_formulas 的引用或注入痕迹
  - `P3` `metric_unit_contains_condition`: metrics.V_0 的 unit 字段疑似写入条件说明：'对于α+^{40}Ca、α+^{59}Co、α+^{208}Pb系统'

## NPP_0092 - P2 人工复核

- Subdomain: `alpha_decay_double_folding`
- Source: `arxiv_0803.4151`
- Final 标题: SUPERHEAVY ELEMENTS IN THE MAGIC ISLANDS
- Parsed 标题: SUPERHEAVY ELEMENTS IN THE MAGIC ISLANDS
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 3/4 个 paper_methods 在 parsed 源文件中缺少词面支持：['double_folding_model', 'wkb_approximation', 'quantum_tunneling_model']
  - `P3` `metric_unit_contains_condition`: metrics.half_life 的 unit 字段疑似写入条件说明：'Z=120, N=172, 幻数候选区域'

## NPP_0107 - P2 人工复核

- Subdomain: `alpha_decay_double_folding`
- Source: `arxiv_nucl-th_0602008`
- Final 标题: $\alpha$ -nucleus potentials, $\alpha$ -decay half-lives, and shell closures for superheavy nuclei
- Parsed 标题: $\alpha$ -nucleus potentials, $\alpha$ -decay half-lives, and shell closures for superheavy nuclei
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 3/4 个 paper_methods 在 parsed 源文件中缺少词面支持：['wkb_approximation', 'wildermuth_condition', 'phase_shift_analysis']
  - `P3` `metric_unit_contains_condition`: metrics.result_1 的 unit 字段疑似写入条件说明：'^{294}Og (Z=118, A=294)'

## NPP_0110 - P2 人工复核

- Subdomain: `deep_learning_nuclear`
- Source: `arxiv_1301.2407`
- Final 标题: Systematics on ground-state energies of nuclei within the neural networks
- Parsed 标题: Systematics on ground-state energies of nuclei within the neural networks
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 3/5 个 paper_methods 在 parsed 源文件中缺少词面支持：['feedforward_neural_network', 'back_propagation_algorithm', 'levenberg_marquardt_algorithm']
  - `P3` `metric_unit_contains_condition`: metrics.binding_energy 的 unit 字段疑似写入条件说明：'A=190-210的Pb同位素'

## NPP_0119 - P2 人工复核

- Subdomain: `deep_learning_nuclear`
- Source: `arxiv_2003.07050`
- Final 标题: Determination of Photonuclear Reaction Cross-Sections on stable p-shell Nuclei by Using Deep Neural Networks
- Parsed 标题: Determination of Photonuclear Reaction Cross-Sections on stable p-shell Nuclei by Using Deep Neural Networks
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 4/4 个 paper_methods 在 parsed 源文件中缺少词面支持：['deep_sequential_neural_network', 'adam_optimization_algorithm', 'relu_activation_function', 'tanh_activation_function']

## NPP_0121 - P2 人工复核

- Subdomain: `deep_learning_nuclear`
- Source: `arxiv_2101.12117`
- Final 标题: Nuclear binding energy predictions using neural networks: Application of the multilayer perceptron
- Parsed 标题: Nuclear binding energy predictions using neural networks: Application of the multilayer perceptron
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 3/4 个 paper_methods 在 parsed 源文件中缺少词面支持：['backpropagation_algorithm', 'adam_optimization_algorithm', 'glorot_normal_initializer']

## NPP_0123 - P2 人工复核

- Subdomain: `deep_learning_nuclear`
- Source: `arxiv_2112.12562`
- Final 标题: Artificial Intelligence Supported Shell-Model Calculations for Light Sn Isotopes
- Parsed 标题: Artificial Intelligence Supported Shell-Model Calculations for Light Sn Isotopes
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `key_formulas_not_used_in_derivation`: paper_derivation observation 中未检出 key_formulas 的引用或注入痕迹
  - `P3` `metric_unit_contains_condition`: metrics.result_1 的 unit 字段疑似写入条件说明：'^{102-108}Sn同位素，中子轨道包括1g7/2, 2d5/2, 2d3/2, 3s1/2, 1h11/2'

## NPP_0126 - P2 人工复核

- Subdomain: `deep_learning_nuclear`
- Source: `arxiv_2208.04783`
- Final 标题: Nuclear mass predictions with machine learning reaching the accuracy required by $r$ -process studies
- Parsed 标题: Nuclear mass predictions with machine learning reaching the accuracy required by $r$ -process studies
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 4/5 个 paper_methods 在 parsed 源文件中缺少词面支持：['macroscopic_microscopic_model', 'relativistic_mean_field', 'hartree_fock_bogoliubov', 'finite_range_droplet_model']

## NPP_0129 - P2 人工复核

- Subdomain: `deep_learning_nuclear`
- Source: `arxiv_2306.11314`
- Final 标题: Analysis of a Skyrme energy density functional with deep learning
- Parsed 标题: Analysis of a Skyrme energy density functional with deep learning
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `subdomain_low_keyword_support`: 样本内容仅命中 1/2 组预期子领域信号：['deep/neural/learning']。title='Analysis of a Skyrme energy density functional with deep learning'
  - `P3` `metric_unit_contains_condition`: metrics.result_1 的 unit 字段疑似写入条件说明：'^{24}Mg核，使用Skyrme-EDF基准'

## NPP_0153 - P2 人工复核

- Subdomain: `nuclear_scattering`
- Source: `arxiv_1009.0545`
- Final 标题: Running Coupling Corrections to High Energy Inclusive Gluon Production
- Parsed 标题: Running Coupling Corrections to High Energy Inclusive Gluon Production
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `paper_methods_unsupported_by_source`: 4/5 个 paper_methods 在 parsed 源文件中缺少词面支持：['eikonal_approximation', 'light_cone_gauge', 'feynman_perturbation_theory', 'dimensional_regularization']
  - `P2` `subdomain_low_keyword_support`: 样本内容仅命中 0/1 组预期子领域信号：[]。title='Running Coupling Corrections to High Energy Inclusive Gluon Production'

## NPP_0154 - P2 人工复核

- Subdomain: `nuclear_scattering`
- Source: `arxiv_1206.4445`
- Final 标题: Tensor polarization of deuterons passing through matter
- Parsed 标题: Tensor polarization of deuterons passing through matter
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `key_formulas_not_used_in_derivation`: paper_derivation observation 中未检出 key_formulas 的引用或注入痕迹

## NPP_0177 - P2 人工复核

- Subdomain: `nuclear_scattering`
- Source: `arxiv_2404.01653`
- Final 标题: Investigation of reaction and $\alpha$ production cross sections with 9Be projectile
- Parsed 标题: Investigation of reaction and $\alpha$ production cross sections with 9Be projectile
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `key_formulas_not_used_in_derivation`: paper_derivation observation 中未检出 key_formulas 的引用或注入痕迹
  - `P3` `metric_unit_contains_condition`: metrics.result_1 的 unit 字段疑似写入条件说明：'9Be+209Bi在库仑势垒附近能量（E_cm ≈ 40-50 MeV）'
  - `P3` `metric_unit_contains_condition`: metrics.result_2 的 unit 字段疑似写入条件说明：'9Be+209Bi在库仑势垒附近能量（E_cm ≈ 40-50 MeV）'

## NPP_0189 - P2 人工复核

- Subdomain: `nuclear_scattering`
- Source: `arxiv_nucl-th_9212009`
- Final 标题: Cross section fluctuations and chaoticity in heavy–ion dynamics
- Parsed 标题: Cross section fluctuations and chaoticity in heavy–ion dynamics
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `key_formulas_not_used_in_derivation`: paper_derivation observation 中未检出 key_formulas 的引用或注入痕迹

## NPP_0228 - P2 人工复核

- Subdomain: `ml_alpha_halflife`
- Source: `arxiv_2603.07983`
- Final 标题: Correlation between nuclear isospin asymmetry and $\alpha$ -particle preformation probability for superheavy nuclei from a Bayesian inference
- Parsed 标题: Correlation between nuclear isospin asymmetry and $\alpha$ -particle preformation probability for superheavy nuclei from a Bayesian inference
- 处置项: 复核证据，确定保留、修复或替换。
- 问题记录:
  - `P2` `source_subdomain_low_keyword_support`: parsed 源文件仅命中 2/3 组预期子领域信号：['alpha/\\alpha', 'half life/half-life/decay']。parsed_title='Correlation between nuclear isospin asymmetry and $\\alpha$ -particle preformation probability for superheavy nuclei from a Bayesian inference'
  - `P2` `subdomain_low_keyword_support`: 样本内容仅命中 2/3 组预期子领域信号：['alpha/\\alpha', 'half life/half-life/decay']。title='Correlation between nuclear isospin asymmetry and $\\alpha$ -particle preformation probability for superheavy nuclei from a Bayesian inference'
  - `P3` `metric_unit_contains_condition`: metrics.half_life 的 unit 字段疑似写入条件说明：'核素 ^{256}Rf (Z=104, A=256)'
  - `P3` `paper_derivation_template_like`: 1/1 条 paper_derivation observation 含泛化或模板化表述

