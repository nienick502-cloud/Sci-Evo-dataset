"""
filter_no_solution.py
将 raw_dataset/ 中 solution_text 为空的样本移到 raw_dataset/no_solution/
"""
import json
import os
import shutil
import glob

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(BASE, "raw_dataset")
NO_SOL_DIR = os.path.join(RAW, "no_solution")

os.makedirs(NO_SOL_DIR, exist_ok=True)

moved, kept = [], []

for f in sorted(glob.glob(os.path.join(RAW, "**", "*.json"), recursive=True)):
    # 跳过 no_solution 目录本身
    if "no_solution" in f.replace("\\", "/"):
        continue
    with open(f, encoding="utf-8") as fp:
        d = json.load(fp)
    sol = d.get("raw_problem", {}).get("solution_text", "")
    if not sol or not sol.strip():
        dest = os.path.join(NO_SOL_DIR, os.path.basename(f))
        shutil.move(f, dest)
        moved.append(os.path.basename(f))
    else:
        kept.append(os.path.basename(f))

print(f"移出（无解答）: {len(moved)} 条")
print(f"保留（有解答）: {len(kept)} 条")
print(f"移出文件已放入: raw_dataset/no_solution/")
if moved:
    print("移出列表:", ", ".join(moved[:10]), "..." if len(moved) > 10 else "")
