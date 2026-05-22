"""
下载团簇模型和双折叠势模型论文 PDF
"""
import os
import time
import urllib.request
from pathlib import Path

BASE = os.environ.get("PAPERS_DIR", str(Path(__file__).resolve().parent.parent.parent / "raw_pdf" / "papers"))

PAPERS = {
    "alpha_团簇模型": [
        ("nucl-th/0404007", "arxiv_nucl-th_0404007.pdf"),
        ("2305.05613",      "arxiv_2305.05613.pdf"),
        ("2307.01706",      "arxiv_2307.01706.pdf"),
        ("2511.08051",      "arxiv_2511.08051.pdf"),
        ("2511.14705",      "arxiv_2511.14705.pdf"),
        ("2507.19091",      "arxiv_2507.19091.pdf"),
        ("2507.16613",      "arxiv_2507.16613.pdf"),
        ("2507.17059",      "arxiv_2507.17059.pdf"),
        ("2602.24175",      "arxiv_2602.24175.pdf"),
    ],
    "alpha_双折叠势模型": [
        ("nucl-th/0206035", "arxiv_nucl-th_0206035.pdf"),
        ("nucl-th/0602008", "arxiv_nucl-th_0602008.pdf"),
        ("1609.00789",      "arxiv_1609.00789.pdf"),
        ("1808.10234",      "arxiv_1808.10234.pdf"),
        ("2111.05604",      "arxiv_2111.05604.pdf"),
        ("2401.07219",      "arxiv_2401.07219.pdf"),
        ("2601.21317",      "arxiv_2601.21317.pdf"),
    ],
}

def arxiv_url(arxiv_id: str) -> str:
    return f"https://arxiv.org/pdf/{arxiv_id}.pdf"

def is_valid_pdf(path: str) -> bool:
    if not os.path.exists(path):
        return False
    if os.path.getsize(path) < 10240:
        return False
    with open(path, "rb") as f:
        return f.read(5) == b"%PDF-"

def download(arxiv_id: str, dest: str) -> bool:
    url = arxiv_url(arxiv_id)
    headers = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        with open(dest, "wb") as f:
            f.write(data)
        return is_valid_pdf(dest)
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

def main():
    results = {"ok": [], "fail": [], "skip": []}
    for folder, papers in PAPERS.items():
        folder_path = os.path.join(BASE, folder)
        os.makedirs(folder_path, exist_ok=True)
        for arxiv_id, filename in papers:
            dest = os.path.join(folder_path, filename)
            if is_valid_pdf(dest):
                print(f"[SKIP] {filename}")
                results["skip"].append(filename)
                continue
            print(f"[DOWN] {arxiv_id} -> {folder}/{filename}")
            ok = download(arxiv_id, dest)
            if ok:
                size_kb = os.path.getsize(dest) // 1024
                print(f"  OK  {size_kb} KB")
                results["ok"].append(filename)
            else:
                print(f"  FAIL")
                results["fail"].append(filename)
            time.sleep(2)

    print("\n=== 结果 ===")
    print(f"成功: {len(results['ok'])}")
    print(f"跳过: {len(results['skip'])}")
    print(f"失败: {len(results['fail'])}")
    if results["fail"]:
        print("失败列表:", results["fail"])

if __name__ == "__main__":
    main()
