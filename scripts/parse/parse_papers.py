"""
parse_papers.py — 阶段6：论文 PDF → MinerU 解析 → Markdown

用法:
  python parse_papers.py                    # 解析所有子文件夹
  python parse_papers.py --folder alpha_壳模型   # 只解析指定子文件夹
  python parse_papers.py --file path/to/paper.pdf

输出: parsed/papers/<subfolder>/<stem>.md
断点续跑：已存在的 .md 文件自动跳过
"""

import argparse
import io
import os
import sys
import time
import zipfile
from pathlib import Path

import requests

# ── 路径配置 ─────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PAPERS_PDF   = PROJECT_ROOT / "raw_pdf" / "papers"
PAPERS_MD    = PROJECT_ROOT / "parsed" / "papers"

# ── MinerU API ───────────────────────────────────────────────
MINERU_TOKEN   = os.environ.get("MINERU_TOKEN", "")
MINERU_BASE    = "https://mineru.net/api/v4"
POLL_INTERVAL  = 3
POLL_MAX       = 200


def _headers():
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MINERU_TOKEN}",
    }


def parse_one(pdf_path: Path, out_dir: Path) -> Path:
    """上传单个 PDF 到 MinerU，返回保存的 .md 路径。"""
    out_dir.mkdir(parents=True, exist_ok=True)
    out_md = out_dir / f"{pdf_path.stem}.md"

    if out_md.exists():
        print(f"  SKIP {pdf_path.name} (已解析)")
        return out_md

    print(f"\n[MinerU] {pdf_path.name}")

    # 1. 获取上传 URL
    resp = requests.post(
        f"{MINERU_BASE}/file-urls/batch",
        headers=_headers(),
        json={"files": [{"name": pdf_path.name}], "model_version": "vlm"},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if data["code"] != 0:
        raise RuntimeError(f"file-urls 失败: {data['msg']}")
    batch_id   = data["data"]["batch_id"]
    upload_url = data["data"]["file_urls"][0]

    # 2. 上传
    with open(pdf_path, "rb") as f:
        requests.put(upload_url, data=f, timeout=300).raise_for_status()
    print(f"  已上传")

    # 3. 轮询
    poll_url = f"{MINERU_BASE}/extract-results/batch/{batch_id}"
    for attempt in range(POLL_MAX):
        time.sleep(POLL_INTERVAL)
        r = requests.get(poll_url, headers=_headers(), timeout=30)
        r.raise_for_status()
        result = r.json()["data"]["extract_result"][0]
        state  = result["state"]
        if state == "done":
            zip_url = result["full_zip_url"]
            break
        elif state == "failed":
            raise RuntimeError(f"解析失败: {result.get('err_msg', '未知')}")
        if attempt % 10 == 0:
            print(f"  状态: {state} ({attempt * POLL_INTERVAL}s)...")
    else:
        raise RuntimeError("轮询超时 (>10min)")

    # 4. 下载 zip，提取 .md
    zip_resp = requests.get(zip_url, timeout=120)
    zip_resp.raise_for_status()
    md_text = None
    with zipfile.ZipFile(io.BytesIO(zip_resp.content)) as zf:
        for name in zf.namelist():
            if name.endswith(".md"):
                md_text = zf.read(name).decode("utf-8")
                break
    if md_text is None:
        raise RuntimeError("zip 中未找到 .md 文件")

    out_md.write_text(md_text, encoding="utf-8")
    print(f"  -> {out_md.relative_to(PROJECT_ROOT)}  ({len(md_text):,} chars)")
    return out_md


def parse_folder(folder: Path):
    pdfs = sorted(folder.glob("*.pdf"))
    if not pdfs:
        print(f"  无 PDF: {folder}")
        return
    out_dir = PAPERS_MD / folder.name
    print(f"\n=== {folder.name} ({len(pdfs)} 篇) ===")
    ok, skip, fail = 0, 0, 0
    for pdf in pdfs:
        out_md = out_dir / f"{pdf.stem}.md"
        if out_md.exists():
            print(f"  SKIP {pdf.name}")
            skip += 1
            continue
        try:
            parse_one(pdf, out_dir)
            ok += 1
        except Exception as e:
            print(f"  ERR  {pdf.name}: {e}")
            fail += 1
    print(f"\n  完成: {ok} 解析, {skip} 跳过, {fail} 失败")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", help="只处理指定子文件夹名（如 alpha_壳模型）")
    parser.add_argument("--file",   help="只处理单个 PDF 文件路径")
    args = parser.parse_args()

    if args.file:
        pdf = Path(args.file).resolve()
        out_dir = PAPERS_MD / pdf.parent.name
        parse_one(pdf, out_dir)
    elif args.folder:
        folder = PAPERS_PDF / args.folder
        if not folder.exists():
            print(f"文件夹不存在: {folder}")
            sys.exit(1)
        parse_folder(folder)
    else:
        # 处理所有子文件夹
        folders = sorted(f for f in PAPERS_PDF.iterdir() if f.is_dir())
        if not folders:
            print(f"raw_pdf/papers/ 下无子文件夹")
            sys.exit(1)
        for folder in folders:
            parse_folder(folder)


if __name__ == "__main__":
    main()
