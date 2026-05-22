"""
fix_wkb_ids.py — 修复 WKB 新增10篇文件的 ID 碰撞问题

将以下10篇新增文件的 id 从碰撞值重新分配为 NPP_0091–NPP_0100：
  arxiv_0909.1602    NPP_0001 → NPP_0091
  arxiv_1405.5633    NPP_0003 → NPP_0092
  arxiv_1707.04568   NPP_0005 → NPP_0093
  arxiv_1708.01935   NPP_0006 → NPP_0094
  arxiv_2407.19647   NPP_0008 → NPP_0095
  arxiv_2508.03155   NPP_0009 → NPP_0096
  arxiv_2602.02070   NPP_0014 → NPP_0097
  arxiv_nucl-th_0204010  NPP_0023 → NPP_0098
  arxiv_nucl-th_0505067  NPP_0024 → NPP_0099
  arxiv_nucl-th_0510082  NPP_0025 → NPP_0100

用法:
  python fix_wkb_ids.py [--dry-run]
"""

import argparse
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
WKB_DIR = PROJECT_ROOT / "raw_dataset" / "papers" / "alpha   WKB"

# 新增10篇文件名 → 新 ID 映射
NEW_ID_MAP = {
    "arxiv_0909.1602.json":       "NPP_0091",
    "arxiv_1405.5633.json":       "NPP_0092",
    "arxiv_1707.04568.json":      "NPP_0093",
    "arxiv_1708.01935.json":      "NPP_0094",
    "arxiv_2407.19647.json":      "NPP_0095",
    "arxiv_2508.03155.json":      "NPP_0096",
    "arxiv_2602.02070.json":      "NPP_0097",
    "arxiv_nucl-th_0204010.json": "NPP_0098",
    "arxiv_nucl-th_0505067.json": "NPP_0099",
    "arxiv_nucl-th_0510082.json": "NPP_0100",
}


def fix_ids(dry_run: bool = False):
    changed = 0
    for fname, new_id in NEW_ID_MAP.items():
        fpath = WKB_DIR / fname
        if not fpath.exists():
            print(f"[!] 文件不存在，跳过: {fname}")
            continue

        with open(fpath, encoding="utf-8") as f:
            data = json.load(f)

        old_id = data.get("id", "")
        old_meta_id = data.get("meta", {}).get("id", "")

        if old_id == new_id:
            print(f"[OK] 已是正确ID，跳过: {fname} ({new_id})")
            continue

        print(f"{'[DRY]' if dry_run else '[FIX]'} {fname}: {old_id} -> {new_id}")

        if not dry_run:
            data["id"] = new_id
            if "meta" in data:
                data["meta"]["id"] = new_id
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            changed += 1

    if not dry_run:
        print(f"\n[OK] 完成，共修改 {changed} 个文件")
    else:
        print(f"\n[DRY] 以上为预览，未实际修改")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="预览，不实际写入")
    args = parser.parse_args()
    fix_ids(dry_run=args.dry_run)
