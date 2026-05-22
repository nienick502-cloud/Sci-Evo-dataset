"""
search_and_download_arxiv.py — 搜索 + 下载 PDF 一体化脚本

1. 调用 arXiv API 搜索各子领域论文（默认 40 篇/领域）
2. 搜索结果 JSON 保存到 raw_dataset/arxiv_search_results/
3. PDF 下载到 raw_pdf/papers/{folder}/

用法:
  python search_and_download_arxiv.py                        # 全部 8 个子领域
  python search_and_download_arxiv.py --subdomain deep_learning_nuclear
  python search_and_download_arxiv.py --download-only        # 跳过搜索，用已有 JSON 下载
"""

import argparse
import json
import sys
import time
import urllib.request
from pathlib import Path

from tqdm import tqdm

# ── 路径 ──────────────────────────────────────────────────────────────────────
_HERE        = Path(__file__).resolve().parent
PROJECT_ROOT = _HERE.parent.parent
sys.path.insert(0, str(_HERE))

from search_arxiv import (  # noqa: E402
    SUBDOMAIN_QUERIES, OUTPUT_DIR,
    _get_existing_arxiv_ids, save_results, search_subdomain,
)

RAW_PDF_DIR = PROJECT_ROOT / "raw_pdf" / "papers"

# 子领域 → raw_pdf/papers/ 文件夹名
FOLDER_MAP: dict[str, str] = {
    "wkb":                   "alpha   WKB",
    "liquid_drop":           "alpha_液滴模型",
    "shell_model":           "alpha_壳模型",
    "cluster":               "alpha_团簇模型",
    "double_folding":        "alpha_双折叠势模型",
    "deep_learning_nuclear": "深度学习_核结构",
    "nuclear_scattering":    "核散射_截面",
    "ml_alpha_halflife":     "机器学习_alpha半衰期",
}


# ── 下载工具函数 ──────────────────────────────────────────────────────────────

def _arxiv_id_to_filename(arxiv_id: str) -> str:
    """'2510.02764' → 'arxiv_2510.02764.pdf'  |  'nucl-th/0206035' → 'arxiv_nucl-th_0206035.pdf'"""
    return "arxiv_" + arxiv_id.replace("/", "_") + ".pdf"


def _is_valid_pdf(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 10240:
        return False
    with open(path, "rb") as f:
        return f.read(5) == b"%PDF-"


def _get_existing_pdf_ids(folder: Path) -> set[str]:
    """返回文件夹内已下载的 arXiv ID 集合。"""
    ids: set[str] = set()
    for pdf in folder.glob("arxiv_*.pdf"):
        arxiv_id = pdf.stem.replace("arxiv_", "", 1).replace("_", "/", 1) \
            if pdf.stem.startswith("arxiv_nucl") else pdf.stem.replace("arxiv_", "", 1)
        ids.add(arxiv_id)
        # 也存 underscore 版本，方便比对
        ids.add(pdf.stem.replace("arxiv_", "", 1))
    return ids


def _download_pdf(arxiv_id: str, dest: Path) -> bool:
    """下载单篇 PDF，失败最多重试 3 次，返回是否成功。"""
    url = f"https://arxiv.org/pdf/{arxiv_id}"
    headers = {"User-Agent": "Mozilla/5.0 (compatible; research-downloader/1.0)"}
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                dest.write_bytes(resp.read())
            return _is_valid_pdf(dest)
        except Exception:
            if dest.exists():
                dest.unlink()
            if attempt < 2:
                time.sleep(6 * (attempt + 1))
    return False


# ── 核心流程 ──────────────────────────────────────────────────────────────────

def search_and_download(
    subdomain: str,
    target: int = 40,
    download_only: bool = False,
    existing_ids: set[str] | None = None,
) -> dict:
    folder_path = RAW_PDF_DIR / FOLDER_MAP[subdomain]
    folder_path.mkdir(parents=True, exist_ok=True)
    result_file = OUTPUT_DIR / f"search_{subdomain}.json"

    # Step 1: 搜索或加载
    if download_only and result_file.exists():
        papers = json.loads(result_file.read_text(encoding="utf-8"))
        print(f"\n[{subdomain}] 加载已有结果: {len(papers)} 篇")
    else:
        print(f"\n{'='*60}\n[{subdomain}] 搜索中 (目标 {target} 篇) ...")
        papers = search_subdomain(subdomain, target=target, existing_ids=existing_ids or set())
        save_results(papers, subdomain, OUTPUT_DIR)
        print(f"  搜索完成: {len(papers)} 篇")

    # Step 2: 下载 PDF
    existing_pdf_ids = _get_existing_pdf_ids(folder_path)
    to_download = [p for p in papers if p["arxiv_id"] not in existing_pdf_ids
                   and p["arxiv_id"].replace("/", "_") not in existing_pdf_ids]
    skip_count = len(papers) - len(to_download)
    print(f"  下载: {len(to_download)} 篇  跳过(已有): {skip_count} 篇")

    ok = fail = 0
    bar = tqdm(to_download, desc=FOLDER_MAP[subdomain][:18], unit="篇", ncols=80)
    for p in bar:
        arxiv_id = p["arxiv_id"]
        dest = folder_path / _arxiv_id_to_filename(arxiv_id)
        bar.set_postfix_str(arxiv_id)
        if _is_valid_pdf(dest):
            skip_count += 1
            continue
        if _download_pdf(arxiv_id, dest):
            ok += 1
            tqdm.write(f"  OK  {arxiv_id}  ({dest.stat().st_size // 1024} KB)")
        else:
            fail += 1
            tqdm.write(f"  FAIL  {arxiv_id}")
        time.sleep(2)
    bar.close()
    print(f"  完成: 下载 {ok}, 跳过 {skip_count}, 失败 {fail}")
    return {"subdomain": subdomain, "total": len(papers), "ok": ok,
            "skip": skip_count, "fail": fail}


# ── 主函数 ────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="arXiv 论文搜索 + PDF 下载")
    parser.add_argument("--subdomain", choices=list(SUBDOMAIN_QUERIES.keys()),
                        help="只处理指定子领域（不填则全部 8 个）")
    parser.add_argument("--target",        type=int, default=40)
    parser.add_argument("--download-only", action="store_true",
                        help="跳过搜索，直接用已有 JSON 下载")
    args = parser.parse_args()

    existing_ids = _get_existing_arxiv_ids()
    print(f"已有 {len(existing_ids)} 篇论文，搜索时自动跳过")

    targets = [args.subdomain] if args.subdomain else list(SUBDOMAIN_QUERIES.keys())
    stats = []
    for sd in targets:
        stats.append(search_and_download(
            sd, target=args.target,
            download_only=args.download_only,
            existing_ids=existing_ids,
        ))

    print(f"\n{'='*60}")
    print(f"{'子领域':<28} {'搜索':>5} {'下载':>5} {'跳过':>5} {'失败':>5}")
    print("-" * 50)
    for s in stats:
        flag = "[!]" if s["fail"] > 0 else "[ ]"
        print(f"{flag} {s['subdomain']:<26} {s['total']:>5} {s['ok']:>5} {s['skip']:>5} {s['fail']:>5}")
    print(f"\n  合计下载: {sum(s['ok'] for s in stats)} 篇  "
          f"失败: {sum(s['fail'] for s in stats)} 篇")
    print(f"  PDF 目录: {RAW_PDF_DIR}")


if __name__ == "__main__":
    main()
