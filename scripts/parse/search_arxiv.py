"""
search_arxiv.py — arXiv API 精品论文搜索脚本

搜索 α 衰变及相关领域的论文，支持：
- 8 个预设子领域（5个α衰变 + 3个扩展领域）
- 分页抓取，保证每个领域达到目标篇数（默认 30）
- 通过 Semantic Scholar API 补充引用数（可选，--enrich）
- 自动跳过已在 raw_dataset/papers/ 中的论文
- 输出 JSON 列表，可直接用于后续 pipeline

子领域列表:
  wkb                      alpha 衰变 WKB 近似
  liquid_drop              alpha 衰变液滴模型
  shell_model              alpha 衰变壳模型
  cluster                  alpha 衰变团簇模型
  double_folding           alpha 衰变双折叠势模型
  deep_learning_nuclear    深度学习与核结构
  nuclear_scattering       核散射与截面
  ml_alpha_halflife        机器学习预测 alpha 衰变半衰期

用法:
  python search_arxiv.py                                      # 搜索全部 8 个子领域，各 30 篇
  python search_arxiv.py --subdomain wkb                      # 只搜 WKB，30 篇
  python search_arxiv.py --subdomain ml_alpha_halflife --target 50 --enrich
  python search_arxiv.py --query "alpha decay neural network" --max 40
  python search_arxiv.py --list-subdomains
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

from tqdm import tqdm

# ── 路径配置 ──────────────────────────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
PAPERS_DIR   = PROJECT_ROOT / "raw_dataset" / "papers"
OUTPUT_DIR   = PROJECT_ROOT / "raw_dataset" / "arxiv_search_results"

ARXIV_API = "https://export.arxiv.org/api/query"
S2_API    = "https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}"
S2_FIELDS = "citationCount,influentialCitationCount,year,publicationDate"

# ── 预设子领域搜索配置 ────────────────────────────────────────────────────────
# queries: 按优先级排列，前面的 query 质量更高
# keywords: 用于关键词相关性二次排序
SUBDOMAIN_QUERIES: dict[str, dict] = {
    # ── α 衰变五子领域 ──────────────────────────────────────────────────────
    "wkb": {
        "label": "alpha_WKB",
        "queries": [
            'ti:"alpha decay" AND (ti:WKB OR ti:tunneling OR ti:"barrier penetration")',
            'abs:"alpha decay" AND abs:"WKB approximation" AND cat:nucl-th',
            'abs:"alpha radioactivity" AND abs:"semiclassical" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"Gamow" AND abs:"tunneling" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"penetration factor" AND cat:nucl-th',
        ],
        "keywords": ["WKB", "tunneling", "barrier penetration", "semiclassical", "Gamow", "penetration"],
    },
    "liquid_drop": {
        "label": "alpha_液滴模型",
        "queries": [
            'abs:"alpha decay" AND abs:"liquid drop" AND cat:nucl-th',
            'abs:"alpha radioactivity" AND abs:"proximity potential" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"surface energy" AND abs:"Coulomb" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"Royer" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"empirical formula" AND abs:"liquid drop" AND cat:nucl-th',
        ],
        "keywords": ["liquid drop", "proximity potential", "surface energy", "Coulomb energy", "Royer"],
    },
    "shell_model": {
        "label": "alpha_壳模型",
        "queries": [
            'abs:"alpha decay" AND abs:"shell model" AND cat:nucl-th',
            'abs:"alpha radioactivity" AND abs:"nuclear shell" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"single particle" AND abs:"shell" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"magic number" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"spin-orbit" AND cat:nucl-th',
        ],
        "keywords": ["shell model", "single particle", "magic number", "spin-orbit", "nuclear shell", "closed shell"],
    },
    "cluster": {
        "label": "alpha_团簇模型",
        "queries": [
            'abs:"alpha decay" AND abs:"cluster model" AND cat:nucl-th',
            'abs:"alpha radioactivity" AND abs:"preformation" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"preformed cluster" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"cluster formation probability" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"alpha cluster" AND abs:"formation amplitude" AND cat:nucl-th',
        ],
        "keywords": ["cluster model", "preformation", "cluster formation", "alpha cluster", "formation amplitude"],
    },
    "double_folding": {
        "label": "alpha_双折叠势模型",
        "queries": [
            'abs:"alpha decay" AND abs:"double folding" AND cat:nucl-th',
            'abs:"alpha radioactivity" AND abs:"folding potential" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"M3Y" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"CDM3Y" AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"nucleon-nucleon interaction" AND abs:"folding" AND cat:nucl-th',
        ],
        "keywords": ["double folding", "folding potential", "M3Y", "CDM3Y", "DDM3Y", "nucleon-nucleon"],
    },

    # ── 三个扩展领域 ────────────────────────────────────────────────────────
    "deep_learning_nuclear": {
        "label": "深度学习与核结构",
        "queries": [
            'abs:"nuclear structure" AND (abs:"deep learning" OR abs:"neural network") AND cat:nucl-th',
            'abs:"nuclear mass" AND (abs:"deep learning" OR abs:"machine learning") AND cat:nucl-th',
            'abs:"binding energy" AND abs:"neural network" AND cat:nucl-th',
            'abs:"nuclear" AND abs:"convolutional neural network" AND (cat:nucl-th OR cat:nucl-ex)',
            'abs:"nuclear" AND abs:"deep learning" AND (abs:"deformation" OR abs:"shell" OR abs:"level") AND cat:nucl-th',
            'abs:"nuclear structure" AND abs:"transformer" AND cat:nucl-th',
            'abs:"nuclear" AND abs:"graph neural network" AND cat:nucl-th',
        ],
        "keywords": ["deep learning", "neural network", "nuclear structure", "binding energy",
                     "nuclear mass", "convolutional", "transformer", "graph neural"],
    },
    "nuclear_scattering": {
        "label": "核散射与截面",
        "queries": [
            'abs:"nuclear scattering" AND abs:"cross section" AND cat:nucl-th',
            'abs:"reaction cross section" AND abs:"optical model" AND cat:nucl-th',
            'abs:"elastic scattering" AND abs:"nuclear" AND abs:"optical potential" AND cat:nucl-th',
            'abs:"inelastic scattering" AND abs:"nuclear" AND abs:"cross section" AND cat:nucl-th',
            'abs:"total reaction cross section" AND cat:nucl-th',
            'abs:"nuclear" AND abs:"scattering amplitude" AND abs:"Coulomb" AND cat:nucl-th',
            'abs:"fusion cross section" AND abs:"nuclear" AND cat:nucl-th',
        ],
        "keywords": ["cross section", "optical model", "scattering", "reaction cross section",
                     "elastic scattering", "optical potential", "fusion"],
    },
    "ml_alpha_halflife": {
        "label": "机器学习预测alpha衰变半衰期",
        "queries": [
            'abs:"alpha decay" AND (abs:"machine learning" OR abs:"neural network" OR abs:"deep learning") AND cat:nucl-th',
            'abs:"alpha radioactivity" AND (abs:"machine learning" OR abs:"neural network") AND cat:nucl-th',
            'ti:"alpha decay" AND (ti:"machine learning" OR ti:"neural network" OR ti:"deep learning" OR ti:"prediction") AND cat:nucl-th',
            'abs:"Geiger-Nuttall" AND (abs:"machine learning" OR abs:"neural network" OR abs:"deep learning") AND cat:nucl-th',
            'abs:"alpha preformation" AND (abs:"machine learning" OR abs:"neural network") AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"half-life" AND (abs:"machine learning" OR abs:"neural network") AND cat:nucl-th',
            'abs:"alpha emitter" AND (abs:"machine learning" OR abs:"neural network") AND cat:nucl-th',
            'abs:"alpha decay" AND (abs:"random forest" OR abs:"support vector" OR abs:"gradient boosting" OR abs:"Bayesian neural") AND cat:nucl-th',
            'abs:"alpha decay" AND abs:"half-life" AND abs:"prediction" AND (abs:"ANN" OR abs:"regression" OR abs:"classification")',
            'abs:"alpha decay half-life" AND (abs:"machine learning" OR abs:"neural network" OR abs:"deep learning")',
        ],
        "keywords": ["alpha decay", "half-life", "machine learning", "neural network",
                     "deep learning", "alpha radioactivity", "preformation",
                     "Geiger-Nuttall", "prediction", "alpha emitter"],
    },
}

# ── arXiv XML 命名空间 ────────────────────────────────────────────────────────
NS = {
    "atom":       "http://www.w3.org/2005/Atom",
    "arxiv":      "http://arxiv.org/schemas/atom",
    "opensearch": "http://a9.com/-/spec/opensearch/1.1/",
}


# ── 工具函数 ──────────────────────────────────────────────────────────────────

def _get_existing_arxiv_ids() -> set[str]:
    """收集 raw_dataset/papers/ 下所有已有的 arXiv ID。"""
    ids: set[str] = set()
    for json_file in PAPERS_DIR.rglob("arxiv_*.json"):
        stem = json_file.stem          # e.g. "arxiv_2510.02764"
        arxiv_id = stem.replace("arxiv_", "", 1)
        ids.add(arxiv_id)
    return ids


def _parse_arxiv_id(entry_id: str) -> str:
    """从 arXiv entry id URL 提取 arXiv ID（去掉版本号）。
    'http://arxiv.org/abs/2510.02764v1' → '2510.02764'
    """
    m = re.search(r"arxiv\.org/abs/(.+?)(?:v\d+)?$", entry_id, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return entry_id.split("/")[-1].split("v")[0]


def _fetch_arxiv(query: str, start: int = 0, max_results: int = 30,
                 year_from: int | None = None, year_to: int | None = None) -> list[dict]:
    """调用 arXiv API，返回解析后的论文列表。"""
    full_query = query
    if year_from or year_to:
        y_from = f"{year_from}0101" if year_from else "19900101"
        y_to   = f"{year_to}1231"   if year_to   else "20991231"
        full_query = f"({query}) AND submittedDate:[{y_from}0000 TO {y_to}2359]"

    params = urllib.parse.urlencode({
        "search_query": full_query,
        "start":        start,
        "max_results":  max_results,
        "sortBy":       "relevance",
        "sortOrder":    "descending",
    })
    url = f"{ARXIV_API}?{params}"

    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                xml_bytes = resp.read()
            break
        except Exception as e:
            if attempt == 2:
                raise RuntimeError(f"arXiv API 请求失败: {e}") from e
            time.sleep(5)

    root = ET.fromstring(xml_bytes)
    papers: list[dict] = []

    for entry in root.findall("atom:entry", NS):
        id_elem = entry.find("atom:id", NS)
        if id_elem is None:
            continue
        arxiv_id  = _parse_arxiv_id(id_elem.text or "")
        title     = (entry.find("atom:title",   NS).text or "").strip().replace("\n", " ")
        abstract  = (entry.find("atom:summary", NS).text or "").strip().replace("\n", " ")
        published = (entry.find("atom:published", NS).text or "")[:10]

        authors = [
            a.find("atom:name", NS).text
            for a in entry.findall("atom:author", NS)
            if a.find("atom:name", NS) is not None
        ]
        categories = [c.get("term", "") for c in entry.findall("atom:category", NS)]

        pdf_url = ""
        for link in entry.findall("atom:link", NS):
            if link.get("title") == "pdf":
                pdf_url = link.get("href", "")
                break

        papers.append({
            "arxiv_id":              arxiv_id,
            "title":                 title,
            "abstract":              abstract,
            "authors":               authors,
            "published":             published,
            "categories":            categories,
            "pdf_url":               pdf_url or f"https://arxiv.org/pdf/{arxiv_id}",
            "abs_url":               f"https://arxiv.org/abs/{arxiv_id}",
            "citation_count":        None,
            "influential_citations": None,
        })

    return papers


def _enrich_with_s2(papers: list[dict], bar: tqdm | None = None) -> list[dict]:
    """通过 Semantic Scholar API 补充引用数（rate limit: ~1 req/s）。"""
    for p in papers:
        url = S2_API.format(arxiv_id=p["arxiv_id"]) + f"?fields={S2_FIELDS}"
        try:
            with urllib.request.urlopen(url, timeout=15) as resp:
                data = json.loads(resp.read())
            p["citation_count"]        = data.get("citationCount")
            p["influential_citations"] = data.get("influentialCitationCount")
        except Exception:
            pass
        time.sleep(1.1)
        if bar:
            bar.update(1)
    return papers


def _keyword_score(paper: dict, keywords: list[str]) -> int:
    """title + abstract 关键词命中数，用于相关性二次排序。"""
    text = (paper["title"] + " " + paper["abstract"]).lower()
    return sum(1 for kw in keywords if kw.lower() in text)


# ── 核心搜索逻辑（带分页，保证达到 target） ───────────────────────────────────

def search_subdomain(
    subdomain: str,
    target: int = 30,
    year_from: int | None = None,
    year_to: int | None = None,
    enrich: bool = False,
    existing_ids: set[str] | None = None,
) -> list[dict]:
    """
    搜索单个子领域，分页抓取直到达到 target 篇（或所有 query 耗尽）。
    返回按关键词相关性（或引用数）排序的去重结果。
    """
    cfg = SUBDOMAIN_QUERIES[subdomain]
    existing_ids = existing_ids or set()
    keywords     = cfg["keywords"]

    seen_ids:   set[str]   = set()
    all_papers: list[dict] = []

    print(f"\n[{subdomain}] 目标 {target} 篇，共 {len(cfg['queries'])} 个 query")

    for q_idx, query in enumerate(cfg["queries"]):
        if len(all_papers) >= target:
            break

        # 每个 query 最多抓 3 页（每页 30 条），避免过度请求
        for page in range(3):
            if len(all_papers) >= target:
                break
            start = page * 30
            try:
                results = _fetch_arxiv(query, start=start, max_results=30,
                                       year_from=year_from, year_to=year_to)
            except Exception as e:
                print(f"  ERR query[{q_idx}] page{page}: {e}")
                break

            new = [
                p for p in results
                if p["arxiv_id"] not in seen_ids
                and p["arxiv_id"] not in existing_ids
            ]
            seen_ids.update(p["arxiv_id"] for p in new)
            all_papers.extend(new)

            short_q = query[:55] + "..." if len(query) > 55 else query
            print(f"  q[{q_idx}] p{page}: {short_q}")
            print(f"    → {len(results)} 条, {len(new)} 条新, 累计 {len(all_papers)} 篇")

            if len(results) < 30:
                break  # 该 query 已无更多结果
            time.sleep(3)

        time.sleep(3)

    # 关键词相关性排序
    all_papers.sort(key=lambda p: _keyword_score(p, keywords), reverse=True)

    if len(all_papers) < target:
        print(f"  [!] 仅找到 {len(all_papers)} 篇（目标 {target}），已穷尽所有 query")
    else:
        print(f"  [OK] 找到 {len(all_papers)} 篇，取前 {target} 篇")
        all_papers = all_papers[:target]

    if enrich and all_papers:
        print(f"  Semantic Scholar 补充引用数 ({len(all_papers)} 篇) ...")
        bar = tqdm(total=len(all_papers), desc="S2 enrich", unit="篇", ncols=70)
        all_papers = _enrich_with_s2(all_papers, bar)
        bar.close()
        all_papers.sort(key=lambda p: (p["citation_count"] or 0), reverse=True)

    return all_papers


def search_custom(
    query: str,
    max_results: int = 30,
    year_from: int | None = None,
    year_to: int | None = None,
    enrich: bool = False,
    existing_ids: set[str] | None = None,
) -> list[dict]:
    """自定义 query 搜索（单次，不分页）。"""
    existing_ids = existing_ids or set()
    print(f"\n[custom] {query}")
    results = _fetch_arxiv(query, max_results=max_results,
                           year_from=year_from, year_to=year_to)
    results = [p for p in results if p["arxiv_id"] not in existing_ids]
    print(f"  → {len(results)} 条新结果")

    if enrich and results:
        bar = tqdm(total=len(results), desc="S2 enrich", unit="篇", ncols=70)
        results = _enrich_with_s2(results, bar)
        bar.close()
        results.sort(key=lambda p: (p["citation_count"] or 0), reverse=True)

    return results


# ── 输出 ──────────────────────────────────────────────────────────────────────

def save_results(papers: list[dict], subdomain: str, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    fname = output_dir / f"search_{subdomain}.json"
    fname.write_text(json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8")
    return fname


def print_summary(papers: list[dict], subdomain: str, top_n: int = 10) -> None:
    print(f"\n{'='*62}")
    print(f"[{subdomain}]  {len(papers)} 篇  (按相关性/引用数排序)")
    print(f"{'='*62}")
    for i, p in enumerate(papers[:top_n], 1):
        cite = f"  cite:{p['citation_count']}" if p["citation_count"] is not None else ""
        print(f"{i:2d}. [{p['published'][:4]}] {p['title'][:68]}")
        print(f"    {p['arxiv_id']}{cite}")
    if len(papers) > top_n:
        print(f"    ... 还有 {len(papers) - top_n} 篇，见输出文件")


# ── 主函数 ────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="arXiv 核物理论文搜索工具（8 个子领域，保证每域 30 篇）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--subdomain",
        choices=list(SUBDOMAIN_QUERIES.keys()),
        help="指定子领域（不填则搜索全部 8 个）",
    )
    parser.add_argument("--query",     help="自定义搜索 query（覆盖 --subdomain）")
    parser.add_argument("--target",    type=int, default=40,
                        help="每个子领域目标篇数（默认 40）")
    parser.add_argument("--max",       type=int, default=30,
                        help="自定义 query 模式下最多取多少篇（默认 30）")
    parser.add_argument("--year-from", type=int, dest="year_from",
                        help="发表年份下限（如 2015）")
    parser.add_argument("--year-to",   type=int, dest="year_to",
                        help="发表年份上限（如 2024）")
    parser.add_argument("--enrich",    action="store_true",
                        help="通过 Semantic Scholar 补充引用数（每篇 ~1s）")
    parser.add_argument("--top",       type=int, default=10,
                        help="打印摘要时显示前 N 篇（默认 10）")
    parser.add_argument("--no-skip",   action="store_true",
                        help="不跳过已有论文（默认跳过）")
    parser.add_argument("--list-subdomains", action="store_true",
                        help="列出所有预设子领域")
    args = parser.parse_args()

    if args.list_subdomains:
        print(f"{'子领域 key':<28} {'标签':<20} 关键词示例")
        print("-" * 72)
        for k, v in SUBDOMAIN_QUERIES.items():
            kws = ", ".join(v["keywords"][:3])
            print(f"  {k:<26} {v['label']:<20} {kws}")
        sys.exit(0)

    existing_ids = set() if args.no_skip else _get_existing_arxiv_ids()
    if existing_ids:
        print(f"已有 {len(existing_ids)} 篇论文，搜索时自动跳过")

    # ── 自定义 query 模式 ──────────────────────────────────────────────────
    if args.query:
        papers = search_custom(
            args.query, max_results=args.max,
            year_from=args.year_from, year_to=args.year_to,
            enrich=args.enrich, existing_ids=existing_ids,
        )
        print_summary(papers, "custom", args.top)
        out = save_results(papers, "custom", OUTPUT_DIR)
        print(f"\n结果已保存: {out}")
        return

    # ── 子领域模式 ─────────────────────────────────────────────────────────
    targets = [args.subdomain] if args.subdomain else list(SUBDOMAIN_QUERIES.keys())
    all_results: dict[str, list[dict]] = {}

    for sd in targets:
        papers = search_subdomain(
            sd, target=args.target,
            year_from=args.year_from, year_to=args.year_to,
            enrich=args.enrich, existing_ids=existing_ids,
        )
        all_results[sd] = papers
        print_summary(papers, sd, args.top)
        out = save_results(papers, sd, OUTPUT_DIR)
        print(f"已保存: {out}")
        if sd != targets[-1]:
            time.sleep(5)

    # ── 汇总 ───────────────────────────────────────────────────────────────
    if len(targets) > 1:
        total = sum(len(v) for v in all_results.values())
        print(f"\n{'='*62}")
        print(f"全部完成: {total} 篇")
        for sd, papers in all_results.items():
            flag = "✓" if len(papers) >= args.target else "⚠"
            print(f"  {flag} {sd:<28} {len(papers):>3} 篇  →  {OUTPUT_DIR / f'search_{sd}.json'}")


if __name__ == "__main__":
    main()
