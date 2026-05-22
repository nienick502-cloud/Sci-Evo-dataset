# Physics-PreProc-QN Dataset

**Physics-PreProc-QN** is a two-tier dataset for quantum mechanics and nuclear physics, built for the [2026 MinerU Challenge · Track 1: Sci-Evo (Scientific Evolution Data)](https://mineru.net).

The dataset captures the *reasoning evolution* of physical science — from standard textbook derivations to the prediction-failure-correction trajectories found in real research papers.

---

## Dataset Overview

| Tier | Source | Samples |
|------|--------|---------|
| Foundation | Quantum mechanics & nuclear physics textbooks | 60 |
| Research | Nuclear physics papers (8 subdomains) | 159 |
| **Total** | | **219** |

### Foundation Tier (60 samples)

Covers classical problems across quantum mechanics and nuclear physics subdomains, representing standard reasoning paths that serve as the model's subdomain knowledge base.

**Quantum mechanics subdomains:**
- Infinite/finite square well, δ-potential
- Harmonic oscillator, ladder operators, first-order perturbation
- Hydrogen atom, angular momentum, orbital quantum numbers
- 1D barrier scattering

**Nuclear physics subdomains:**
- Shell model: single-particle levels, magic numbers
- Liquid drop model / semi-empirical mass formula
- Nuclear potential scattering and effective potential

### Research Tier (159 samples)

Based on real nuclear physics papers. Each sample encodes a full prediction-comparison-correction trajectory: the agent first predicts under DFS constraints, then compares against the paper's actual derivation, and finally performs root-cause analysis.

| Subdomain | `subdomain` value | Papers |
|-----------|-------------------|--------|
| α-decay WKB | `alpha_decay_wkb` | 24 |
| α-decay Liquid Drop | `alpha_decay_liquid_drop` | 12 |
| α-decay Shell Model | `alpha_decay_shell_model` | 17 |
| α-decay Cluster Model | `alpha_decay_cluster_model` | 14 |
| α-decay Double Folding | `alpha_decay_double_folding` | 13 |
| Deep Learning (Nuclear Structure) | `deep_learning_nuclear` | 37 |
| Nuclear Scattering Cross-Section | `nuclear_scattering` | 39 |
| ML α Half-life | `ml_alpha_halflife` | 3 |

---

## Schema

Each sample is a JSON file with three top-level sections:

```
{
  "id": "NPP_0001",
  "meta": { ... },                    // metadata
  "01_initial_request": { ... },      // problem statement
  "02_agent_trajectory": [ ... ],     // step-by-step reasoning trajectory
  "03_success_verification": { ... }  // validation and final results
}
```

### `meta` fields

| Field | Type | Description |
|-------|------|-------------|
| `data_tier` | string | `"foundation"` or `"research"` |
| `domain` | string | `"quantum_mechanics"` or `"nuclear_physics"` |
| `subdomain` | string | Fine-grained subdomain label |
| `difficulty` | int | 1–5 scale |
| `is_gold` | bool | High-quality gold standard flag |
| `source.type` | string | `"textbook"` or `"paper"` |
| `source.problem_number_or_doi` | string | Problem number or arXiv ID |

### Research-tier extra fields

| Field | Type | Description |
|-------|------|-------------|
| `paper_methods` | list[str] | Methods used in the paper |
| `paper_facts` | object | Extracted formulas, results, failure points |

### Trajectory step fields

Each step in `02_agent_trajectory` contains:

| Field | Type | Description |
|-------|------|-------------|
| `step_index` | int | Step number |
| `thought` | string | `[Background] ... [Gap] ... [Decision] ...` |
| `action` | string | Step type (e.g., `symbolic_derivation`, `approximation`) |
| `tool` | object | Physical tool used (`name`, `version`) |
| `parameters` | object | Input parameters |
| `output_state` | object | Physical quantities produced |
| `observation` | string | Actual result of this step |
| `valid` | bool | Whether this step is correct |

Research-tier steps additionally have: `phase`, `error_tag`, `error_reason`, `observation_source`, `overall_lesson`.

For the full schema specification, see [`schema/schema_overview.md`](schema/schema_overview.md).

---

## File Naming

- Foundation (quantum): `QN_XXXX.json`
- Foundation (nuclear): `NP_XXXX.json`
- Research (nuclear papers): `NPP_XXXX.json`

All 219 final samples are in `dataset/final/`, organized by tier:

```
dataset/final/
├── foundation/   # 60 samples (QN_*.json, NP_*.json)
└── Research/     # 159 samples (NPP_*.json)
```

A summary index is available at `dataset/metadata.jsonl`.

---

## Loading the Dataset

### Load the metadata index

```python
import json

metadata = []
with open("dataset/metadata.jsonl", encoding="utf-8") as f:
    for line in f:
        metadata.append(json.loads(line))

# Filter by tier
foundation = [m for m in metadata if m["data_tier"] == "foundation"]
research   = [m for m in metadata if m["data_tier"] == "research"]

print(f"Foundation: {len(foundation)}, Research: {len(research)}")
```

### Load a single sample

```python
import json
from pathlib import Path

def load_sample(sample_id: str, final_dir="dataset/final") -> dict:
    """Search both tier subdirectories for the sample."""
    base = Path(final_dir)
    for subdir in base.iterdir():
        path = subdir / f"{sample_id}.json"
        if path.exists():
            with open(path, encoding="utf-8") as f:
                return json.load(f)
    raise FileNotFoundError(f"{sample_id}.json not found in {final_dir}")

sample = load_sample("NPP_0001")
print(sample["meta"]["subdomain"])          # alpha_decay_wkb
print(len(sample["02_agent_trajectory"]))   # number of reasoning steps
```

### Iterate all samples

```python
from pathlib import Path
import json

final_dir = Path("dataset/final")
for path in sorted(final_dir.rglob("*.json")):
    with open(path, encoding="utf-8") as f:
        sample = json.load(f)
    tier = sample["meta"]["data_tier"]
    steps = sample["02_agent_trajectory"]
    print(f"{sample['id']} | {tier} | {len(steps)} steps")
```

---

## License

This dataset is released under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt the material for any purpose, provided appropriate credit is given.

---

## Citation

If you use this dataset in your research, please cite:

```bibtex
@dataset{physics_preproc_qn_2026,
  title   = {Physics-PreProc-QN: A Two-Tier Dataset for Scientific Reasoning Evolution in Quantum and Nuclear Physics},
  author  = {Myron Soan},
  year    = {2026},
  note    = {2026 MinerU Challenge, Track 1: Sci-Evo},
  license = {CC BY 4.0}
}
```

---

## Contact

For questions or issues, please open a GitHub issue in this repository.
