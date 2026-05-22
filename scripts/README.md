# Reproduction Scripts

This directory contains all scripts needed to reproduce the Physics-PreProc-QN dataset.

## Prerequisites

- Python 3.10+
- DeepSeek API access (set `DEEPSEEK_API_KEY` environment variable)
- MinerU API access (set `MINERU_TOKEN` environment variable, for PDF parsing)

```bash
pip install openai requests
```

## Directory Structure

```
scripts/
├── agent/                        # Core Sci-Evo Agent v2
│   ├── sci_evo_agent.py               # Main agent (Phase 1-4 pipeline)
│   ├── dfs_engine.py                  # DFS reverse-chain search engine
│   ├── step_classifier.py             # Step classifier (DeepSeek API)
│   ├── crystal_rule_manager.py        # Crystal growing experience system
│   ├── reasoning_formatter.py         # Trajectory temporal reordering
│   ├── audit_quality.py               # 6-dimension quality auditor
│   ├── validate_foundation.py         # Foundation-tier logic validator
│   ├── core_tool_library_v2.json      # 84 physics tool library
│   └── core_tool_library_ml.json      # 14 ML tool library
├── parse/                        # PDF parsing & arXiv search
│   ├── parse_pdf.py                  # MinerU PDF → Markdown + segmentation
│   ├── parse_papers.py               # Batch MinerU parsing for papers
│   ├── search_arxiv.py               # arXiv keyword search
│   ├── search_and_download_arxiv.py  # arXiv search + PDF download
│   └── download_new_papers.py        # Batch PDF download
├── generate/                     # Schema conversion & generation
│   ├── convert_schema.py             # Old schema → new schema conversion
│   └── refactor_foundation.py        # Foundation-tier batch generation
├── postprocess/                  # Post-processing
│   ├── format_for_submission.py      # Final formatting (reorder + fusion + polish)
│   └── gen_metadata.py               # Generate metadata.jsonl index
└── fix/                          # Data quality fixes
    ├── fix_tool_names.py             # LLM-based tool name normalization
    ├── fix_no_solution.py            # Extract solutions from unlabelled problems
    ├── filter_no_solution.py         # Filter problems without solutions
    ├── fix_wkb_ids.py                # Fix WKB ID collisions
    └── audit_topic_match.py          # Check paper-subdomain topic match
```

## Script Reference

### agent/ — Sci-Evo Agent v2 Core

| Script | Description |
|--------|-------------|
| `sci_evo_agent.py` | **Main agent**: 4-phase pipeline (Phase 1 extract paper_facts → Phase 2 DFS-constrained semi-blind prediction → Phase 3 paper derivation extraction → Phase 4 error analysis + decision summary + verification generation). Auto-detects ML papers and enables dual-track DFS (physics + ML). Supports `--paper` single-paper and `--folder` batch modes. |
| `dfs_engine.py` | **DFS reverse-chain search engine**: Starting from target physical quantities, searches all legal derivation paths backwards on the requires→provides dependency graph of 84 tools (+14 ML tools). Supports dependency satisfaction checking and path pruning. |
| `step_classifier.py` | **Step classifier**: Calls DeepSeek API to label each generated step with a `step_mode` (11 types: strict_derivation, citation, empirical_approximation, etc.), determining whether the step triggers hard validation or path pruning only. |
| `crystal_rule_manager.py` | **Crystal growing experience system**: Accumulates derivation error patterns across papers, extracts physics avoidance rules (extract→inject→evaluate→decay→circuit-break). Global `rules_db.json` filtered by subdomain. Only active in `--folder` mode. |
| `reasoning_formatter.py` | **Trajectory temporal reorderer**: Reorders agent output steps (interleaved prediction/paper_derivation/decision_summary) into the fixed learning sequence: prediction → decision → paper derivation. |
| `audit_quality.py` | **6-dimension quality auditor**: Scores each sample across six dimensions (structural integrity, content quality, physics correctness, etc.) Outputs GOLD/SILVER/BRONZE/REJECT tier classifications. |
| `validate_foundation.py` | **Foundation-tier logic validator**: Checks each Foundation sample's derivation chain — starting from given conditions, tracks whether each tool's requires are satisfied step by step, outputs dependency pass rate. |
| `core_tool_library_v2.json` | **84 physics tool library**: Each tool has strict requires→provides definitions + physical quantity ontology. 8 categories: nuclear structure, potentials, WKB/tunneling, scattering/reactions, machine learning, numerical/verification, macro-micro, cluster model, statistics/QRPA, nuclear many-body, decay kinematics. |
| `core_tool_library_ml.json` | **14 ML tool library**: ML DFS track专用. Covers data engineering → model selection → training → evaluation → prediction. 7 standard ML workflow paths. |

### parse/ — PDF Parsing & Paper Acquisition

| Script | Description |
|--------|-------------|
| `parse_pdf.py` | **Textbook PDF parsing & segmentation**: Calls MinerU API to convert textbook PDFs to Markdown, then uses regex matching to split long text into individual problem JSONs. Outputs to `raw_dataset/quantum/` or `raw_dataset/nuclear/`. |
| `parse_papers.py` | **Batch paper PDF parsing**: Iterates all subfolder paper PDFs, calls MinerU API to batch-convert to Markdown. Supports checkpoint resume (skips existing .md files). Outputs to `parsed/papers/`. |
| `search_arxiv.py` | **arXiv keyword search**: Calls arXiv API to search papers by keyword, returns paper list (title, abstract, arXiv ID). Results saved as JSON. |
| `search_and_download_arxiv.py` | **arXiv search + download**: Extends `search_arxiv.py` with PDF download capability. Search results are downloaded directly to `raw_pdf/papers/` subfolders. |
| `download_new_papers.py` | **Batch PDF supplement download**: Downloads PDFs from a supplementary arXiv ID list, used for expanding existing subdomains (original 5 subdomains each got 10-20 new papers). |

### generate/ — Schema Conversion & Batch Generation

| Script | Description |
|--------|-------------|
| `convert_schema.py` | **Old→new schema conversion** (Stage 5): Converts old-format Exercise JSON (question/solution/trajectory) to new format (01_initial_request / 02_agent_trajectory / 03_success_verification). Calls DeepSeek API to rewrite trajectory steps. |
| `refactor_foundation.py` | **Foundation-tier batch generation** (Stage 5): Starting from raw exercises in `raw_dataset/`, calls DeepSeek API to batch-generate complete trajectories for all 60 Foundation samples with tool annotations and 01/02/03 three-section structure. |

### postprocess/ — Post-Processing

| Script | Description |
|--------|-------------|
| `format_for_submission.py` | **Final format orchestration** (Stage 10.5): Converts agent output `_v2.json` to submission format. Three operations: ① trajectory reordering (prediction→decision→paper_derivation); ② information fusion (386 formula + 166 method description injections into observations); ③ format polishing (fill failure_points, remove redundant fields). Pure extraction/concatenation, no LLM calls, idempotent. |
| `gen_metadata.py` | **Metadata index generation**: Scans all JSONs in `dataset/final/`, extracts id/tier/domain/subdomain/difficulty/is_gold per sample, generates `metadata.jsonl` summary file. Pure Python, no API calls. |

### fix/ — Data Repair Tools

| Script | Description |
|--------|-------------|
| `fix_tool_names.py` | **Tool name normalization**: Calls DeepSeek API to check and fix non-standard or inconsistent tool names in `_v2.json`, unified mapping to core library naming conventions. |
| `fix_no_solution.py` | **Solution label repair**: Some problem PDFs had unmarked solution sections after parsing (regex missed them). This script uses LLM to locate and label "solution"/"answer" paragraphs, enabling proper solution field inclusion. |
| `filter_no_solution.py` | **No-solution filter**: Filters out exercise JSONs in `raw_dataset/` that lack solutions (MinerU parse failure or no solution in original book), moves them to `raw_dataset/no_solution/`. |
| `fix_wkb_ids.py` | **WKB ID repair**: Fixes ID assignment issues in the WKB subdomain (early arXiv ID ↔ NPP ID mapping errors), reassigns consecutive IDs and updates references. |
| `audit_topic_match.py` | **Topic match auditor**: Batch-checks whether each paper's title/target/intent fields match its assigned subdomain, flags suspected misclassified papers (used for P0 data cleanup, found 16 misclassifications). |

## Setup

Set API keys before running:

```bash
export DEEPSEEK_API_KEY="your-deepseek-key"
export MINERU_TOKEN="your-mineru-jwt-token"
```

## Pipeline Overview

The full reproduction pipeline has these stages:

### 1. PDF Parsing (MinerU)

Parse textbooks and papers using MinerU API:

```bash
cd scripts/parse
python parse_pdf.py --file /path/to/textbook.pdf        # Single PDF
python parse_pdf.py --all                                 # All textbooks
python parse_papers.py                                    # All paper subfolders
```

### 2. Schema Conversion & Generation

Convert raw parsed data into the dataset schema:

```bash
cd scripts/generate
python convert_schema.py                                  # Old→new schema
python refactor_foundation.py                             # Foundation batch gen
```

### 3. Agent Trajectory Generation (Sci-Evo Agent v2)

Generate paper trajectories with DFS-constrained prediction:

```bash
cd scripts/agent
python sci_evo_agent.py --paper "/path/to/paper.json"     # Single paper
python sci_evo_agent.py --folder "alpha   WKB" --limit 3  # Batch (note triple space)
```

Key options:
- `--batch-size N` — Crystal batch size (0 = auto)
- `--output-dir DIR` — Output to custom directory
- `--no-crystal` — Disable Crystal experience system
- `--force` — Overwrite existing output files

### 4. Quality Audit

```bash
cd scripts/agent
python audit_quality.py --subdomain "alpha_decay_wkb"
```

### 5. Post-processing

Convert raw `_v2.json` files to submission format:

```bash
cd scripts/postprocess
python format_for_submission.py
python gen_metadata.py
```

## Foundation Validation

Validate Foundation-tier trajectories against the tool library:

```bash
cd scripts/agent
python validate_foundation.py
```
