"""
gen_metadata.py — Generate dataset/metadata.jsonl from dataset/final/*.json

Each line in the output is a JSON object with:
  id, data_tier, domain, subdomain, difficulty, is_gold,
  source_type, source_doi, paper_methods, num_trajectory_steps
"""

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
FINAL_DIR = PROJECT_ROOT / "dataset" / "final"
OUTPUT_PATH = PROJECT_ROOT / "dataset" / "metadata.jsonl"


def extract_meta(filepath: Path) -> dict:
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)

    meta = data.get("meta", {})
    source = meta.get("source", {})
    trajectory = data.get("02_agent_trajectory", [])

    return {
        "id": data.get("id") or meta.get("id", filepath.stem),
        "data_tier": meta.get("data_tier", ""),
        "domain": meta.get("domain", ""),
        "subdomain": meta.get("subdomain", ""),
        "difficulty": meta.get("difficulty", None),
        "is_gold": meta.get("is_gold", False),
        "source_type": source.get("type", ""),
        "source_doi": source.get("problem_number_or_doi", ""),
        "paper_methods": data.get("paper_methods", []),
        "num_trajectory_steps": len(trajectory),
    }


def main():
    files = sorted(FINAL_DIR.glob("*.json"))
    if not files:
        print(f"[!] No JSON files found in {FINAL_DIR}")
        return

    records = []
    errors = []
    for fp in files:
        try:
            records.append(extract_meta(fp))
        except Exception as e:
            errors.append((fp.name, str(e)))

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"[OK] Written {len(records)} records to {OUTPUT_PATH}")
    if errors:
        print(f"[!] {len(errors)} errors:")
        for name, err in errors:
            print(f"    {name}: {err}")

    # Quick stats
    tiers = {}
    subdomains = {}
    gold_count = 0
    for r in records:
        tiers[r["data_tier"]] = tiers.get(r["data_tier"], 0) + 1
        subdomains[r["subdomain"]] = subdomains.get(r["subdomain"], 0) + 1
        if r["is_gold"]:
            gold_count += 1

    print("\n--- Stats ---")
    for tier, count in sorted(tiers.items()):
        print(f"  {tier}: {count}")
    print(f"  is_gold=True: {gold_count}")
    print("\n  Subdomain breakdown:")
    for sd, count in sorted(subdomains.items(), key=lambda x: -x[1]):
        print(f"    {sd}: {count}")


if __name__ == "__main__":
    main()
