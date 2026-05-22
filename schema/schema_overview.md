# Schema Overview — Physics-PreProc-QN

This document specifies the full data schema for the Physics-PreProc-QN dataset.
Both Foundation and Research tiers share the same top-level structure, distinguished
by `meta.data_tier` and `meta.source.type`. The Research tier has extra fields at
the top level and in each trajectory step.

---

## Top-Level Structure

```json
{
  "id": "NPP_0001",
  "meta": { ... },
  "01_initial_request": { ... },
  "02_agent_trajectory": [ ... ],
  "03_success_verification": { ... }
}
```

## `meta`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | yes | Unique sample identifier |
| `data_tier` | string | yes | `"foundation"` or `"research"` |
| `domain` | string | yes | `"quantum_mechanics"` or `"nuclear_physics"` |
| `subdomain` | string | yes | Fine-grained subdomain (see below) |
| `source.type` | string | yes | `"textbook"` or `"paper"` |
| `source.title` | string | yes | Book or paper title |
| `source.chapter_or_section` | string | Foundation only | Chapter/section reference |
| `source.problem_number_or_doi` | string | yes | Problem number or arXiv DOI |
| `difficulty` | int | yes | 1–5 scale |
| `is_gold` | bool | yes | High-quality gold standard flag |
| `version` | string | yes | Schema version (`"1.0"`) |

### Foundation subdomains

**Quantum mechanics:**
- `infinite_square_well_1D`, `finite_square_well_1D`, `delta_potential_1D`
- `harmonic_oscillator_1D`, `ladder_operators`, `perturbation_first_order`
- `hydrogen_atom`, `angular_momentum`, `barrier_scattering_1D`

**Nuclear physics:**
- `shell_model_single_particle`, `liquid_drop_model`, `nuclear_potential_scattering`

### Research subdomains

| `subdomain` value | Topic |
|-------------------|-------|
| `alpha_decay_wkb` | α-decay WKB approximation |
| `alpha_decay_liquid_drop` | α-decay liquid drop model |
| `alpha_decay_shell_model` | α-decay shell model |
| `alpha_decay_cluster_model` | α-decay cluster model |
| `alpha_decay_double_folding` | α-decay double-folding potential |
| `deep_learning_nuclear` | Deep learning for nuclear structure |
| `nuclear_scattering` | Nuclear scattering cross-sections |
| `ml_alpha_halflife` | ML for α-decay half-life prediction |

---

## `01_initial_request`

| Field | Type | Description |
|-------|------|-------------|
| `target_name` | string | The quantity to solve for |
| `input_data` | string | Known conditions and parameters |
| `user_intent` | string | The problem-solving intent |
| `quantifiable_goal` | string | Quantifiable goal (quantity name + unit, no numeric value) |

---

## `02_agent_trajectory`

An ordered list of reasoning steps. Each step has the following fields:

### Shared fields (both tiers)

| Field | Type | Description |
|-------|------|-------------|
| `step_index` | int | 1-indexed step number |
| `thought` | string | `[Background] ... [Gap] ... [Decision] ...` three-part reasoning |
| `action` | string | Step type (see Action Types below) |
| `tool.name` | string | Tool used (see Tool Naming below) |
| `tool.version` | string | Tool version |
| `parameters` | object | Input parameters for this step |
| `output_state` | object | Physical quantities produced: `{"quantity_name": "expression or value"}` |
| `observation` | string | The actual result of this step |
| `valid` | bool | Whether this step is correct |

### Research-tier extra step fields

| Field | Type | Description |
|-------|------|-------------|
| `phase` | string | `"prediction"`, `"paper_derivation"`, or `"decision_summary"` |
| `error_tag` | string or null | Error label if step is incorrect (see below) |
| `error_reason` | string | Physical reason for the error (when error_tag is non-null) |
| `observation_source` | string | `"paper"` or `"inferred"` |
| `overall_lesson` | string | Generalizable lesson (last step of decision_summary only) |
| `dfs_warning` | string | DFS constraint warning (paper_derivation phase only) |

### Research-tier extra top-level fields

| Field | Type | Description |
|-------|------|-------------|
| `paper_methods` | list[string] | Methods used in the paper |
| `paper_facts.methods` | list[object] | Extracted method descriptions |
| `paper_facts.key_formulas` | list[object] | Key formulas: `{"label": "Eq.(1)", "content": "LaTeX"}` |
| `paper_facts.key_results` | list[object] | Key results: `{"quantity", "value", "condition"}` |
| `paper_facts.failure_points` | list[string] | Methods the paper explicitly invalidates |

### Action Types

| `action` | Meaning | Typical trigger |
|----------|---------|-----------------|
| `symbolic_derivation` | Symbolic derivation (separation of variables, operator algebra, etc.) | Deriving wave functions, energy eigenvalues |
| `numerical_computation` | Numerical computation (substituting values, order-of-magnitude estimation) | Computing binding energies |
| `approximation` | Introducing an approximation (perturbation, WKB, independent particle, etc.) | Setting up an approximate framework |
| `verification` | Verification step (dimensional analysis, limiting cases, physical intuition) | Checking result validity |
| `rule_application` | Applying a known physical rule/theorem without derivation | Shell filling, radioactive decay law |
| `model_building` | Building a physical model/approximation framework (step_index==1 only) | Fermi gas model, optical model potential |
| `correction` | Correction step (follow-up to `valid: false` in Research tier) | Switching to correct method after failure |

### Error Tags (Research tier)

| `error_tag` | Description |
|-------------|-------------|
| `wrong_approximation` | Wrong approximation chosen |
| `missing_physical_effect` | Overlooked a relevant physical effect |
| `incorrect_derivation` | Mathematical or logical error in derivation |
| `wrong_parameter_choice` | Incorrect parameter values or ranges |
| `over_simplification` | Model too simplified for the problem |
| `wrong_physical_interpretation` | Misinterpretation of physical meaning |

---

## `03_success_verification`

| Field | Type | Description |
|-------|------|-------------|
| `validation_technique` | string | Specific verification method (dimensional analysis, limiting case check, etc.) |
| `metrics` | object | `{"quantity_name": {"value", "unit", "interpretation"}}` |
| `final_verdict` | string | Final conclusion |

---

## Research-tier Trajectory Structure

The `02_agent_trajectory` in Research samples consists of three interleaved phases:

| Phase | Source | `valid` | Key fields |
|-------|--------|---------|------------|
| `prediction` | Semi-blind prediction under DFS constraints | true/false | `error_tag` (may be non-null after Phase 4 back-annotation) |
| `paper_derivation` | Actual derivation steps extracted from the paper | true | `observation_source: "paper"`, `dfs_warning` |
| `decision_summary` | Root cause analysis, three anti-hindsight elements | true | `overall_lesson` (last step) |

### Decision Summary Three Anti-Hindsight Elements

1. **Decision moment**: What choice was made at which step
2. **Missed signals**: What known physical facts should have prompted reconsideration
3. **Correct judgment**: How an experienced physicist would think given the same information

---

## Foundation-tier Tool Naming

### Physics mechanism layer (~30 tools)

**Quantum mechanics:** `separation_of_variables`, `fourier_transform`, `boundary_condition_matching`,
`bohr_sommerfeld_quantization`, `normalization_condition`, `ladder_operator_method`,
`perturbation_theory_first_order`, `perturbation_theory_second_order`, `variational_method`,
`wkb_approximation`, `angular_momentum_coupling`, `symmetry_argument`, `commutator_algebra`,
`uncertainty_principle_application`, `asymptotic_analysis`, `eigenfunction_expansion`

**Nuclear physics:** `shell_filling`, `pairing_rule`, `bethe_weizsacker_formula`,
`nuclear_radius_formula`, `coulomb_barrier_estimate`, `nuclear_decay_kinematics`,
`nuclear_reaction_rate`, `optical_model_potential`, `radioactive_decay_law`,
`secular_equilibrium_condition`, `fermi_gas_model`, `nuclear_scattering_kinematics`,
`bateman_equation_solution`, `cross_section_calculation`

**Verification:** `dimensional_analysis`, `limiting_case_check`, `physical_intuition_check`

### Mathematical operations layer (6 tools)

`symbolic_algebra`, `symbolic_computation`, `integral_evaluation`, `numerical_computation`,
`dimensional_analysis_and_conversion`, `series_expansion`

New tools must be physical mechanisms; pure math operations are unified under the 6 math-layer tools.

---

## Research-tier Tool Naming

No fixed tool pool. `tool.name` directly reflects the method used in the paper, sourced from
`paper_methods`. Examples: `relativistic_mean_field`, `double_folding_model`, `cluster_formation_model`,
`hartree_fock_bogoliubov`, `r_matrix_theory`, `dbhf_potential`, or any real physics method in snake_case.

During `paper_derivation` phase, tool names are taken from `paper_facts.methods`.

---

## File Naming Convention

| Tier | Prefix | Example |
|------|--------|---------|
| Foundation (quantum) | `QN_XXXX` | `QN_0001.json` |
| Foundation (nuclear) | `NP_XXXX` | `NP_0001.json` |
| Research (nuclear papers) | `NPP_XXXX` | `NPP_0001.json` |

---

## Notes

- All LaTeX in JSON must use double backslashes: `\\rho`, `\\frac`
- All files use UTF-8 encoding
- `output_state` values are expressions or numeric values, formatted as strings when containing LaTeX
- For the complete tool library (84 physics tools + 14 ML tools), see the source repository
