"""
parse_pdf.py — Physics-PreProc-QN 阶段2：PDF 解析与切题

用法:
  python parse_pdf.py --file ../raw_pdf/量子力学/量子力学：习题解-曾谨言.pdf
  python parse_pdf.py --all
  python parse_pdf.py --file <path> --dry-run   # 只解析，不切题写 JSON

输出:
  parsed/          ← MinerU 解析的 markdown（缓存）
  raw_dataset/quantum/QN_XXXX.json
  raw_dataset/nuclear/NP_XXXX.json
"""

import argparse
import io
import json
import os
import re
import sys
import time
import zipfile
from pathlib import Path

import requests

# ── 路径配置 ─────────────────────────────────────────────────
PROJECT_ROOT  = Path(__file__).resolve().parent.parent
RAW_PDF_DIR   = PROJECT_ROOT / "raw_pdf"
PARSED_DIR    = PROJECT_ROOT / "parsed"
RAW_DS_DIR    = PROJECT_ROOT / "raw_dataset"

# ── MinerU API ───────────────────────────────────────────────
MINERU_TOKEN    = os.environ.get("MINERU_TOKEN", "")
MINERU_BASE     = "https://mineru.net/api/v4"
MAX_PAGES_PART  = 300   # 超过此页数自动拆分上传
POLL_INTERVAL   = 3     # 秒
POLL_MAX        = 200   # 最多轮询次数

# ── 书目元数据映射 ────────────────────────────────────────────
# key: PDF 文件名（不含扩展名的关键词，小写匹配）
BOOK_META = {
    "格里菲斯": {
        "domain": "quantum_mechanics",
        "source_type": "textbook",
        "title": "格里菲斯《量子力学概论》",
        "lang": "zh",
        "id_prefix": "QN",
        "splitter": "griffiths",
    },
    "曾谨言": {
        "domain": "quantum_mechanics",
        "source_type": "problem_book",
        "title": "量子力学习题解（曾谨言）",
        "lang": "zh",
        "id_prefix": "QN",
        "splitter": "zeng",
    },
    "nuclear": {
        "domain": "nuclear_physics",
        "source_type": "problem_book",
        "title": "Problems and Solutions in Nuclear and Particle Physics",
        "lang": "en",
        "id_prefix": "NP",
        "splitter": "nuclear_en",
    },
}

# ── 子领域关键词映射 ──────────────────────────────────────────
SUBDOMAIN_KEYWORDS = {
    "quantum_mechanics": [
        ("infinite_square_well_1D",   ["无限深势阱", "infinite square well", "infinite potential well"]),
        ("finite_square_well",        ["有限深势阱", "finite square well", "finite potential well"]),
        ("delta_potential",           ["δ势", "delta potential", "delta function potential"]),
        ("harmonic_oscillator_1D",    ["简谐振子", "harmonic oscillator", "ladder operator", "升降算符"]),
        ("hydrogen_atom",             ["氢原子", "hydrogen atom", "coulomb potential", "库仑势"]),
        ("angular_momentum",          ["角动量", "angular momentum", "spherical harmonics", "球谐函数"]),
        ("perturbation_theory",       ["微扰", "perturbation theory"]),
        ("scattering_1D",             ["散射", "scattering", "transmission", "reflection", "透射", "反射"]),
        ("central_potential",         ["中心势", "central potential", "radial equation"]),
    ],
    "nuclear_physics": [
        ("shell_model_single_particle", ["shell model", "magic number", "魔数", "壳模型", "single particle"]),
        ("liquid_drop_model",           ["liquid drop", "semi-empirical", "binding energy", "结合能", "质量公式"]),
        ("nuclear_decay",               ["decay", "衰变", "alpha", "beta", "gamma", "半衰期", "half-life"]),
        ("nuclear_reactions",           ["reaction", "cross section", "截面", "核反应"]),
        ("nuclear_scattering",          ["scattering", "散射", "optical model", "光学模型"]),
    ],
}


# ════════════════════════════════════════════════════════════
# MinerU API 封装（复用 demo/local_rag.py 的逻辑）
# ════════════════════════════════════════════════════════════

def _mineru_headers():
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {MINERU_TOKEN}",
    }


def _split_pdf_parts(file_path: Path):
    """将大 PDF 拆分为临时文件列表，每份 ≤ MAX_PAGES_PART 页。"""
    try:
        import pymupdf
    except ImportError:
        print("  提示：未安装 pymupdf，跳过大文件拆分（直接上传整个文件）")
        return [(str(file_path), None)]

    pdf = pymupdf.open(str(file_path))
    total = len(pdf)
    if total <= MAX_PAGES_PART:
        pdf.close()
        return [(str(file_path), None)]

    tmp_dir = PARSED_DIR / "_tmp"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    parts = []
    for start in range(0, total, MAX_PAGES_PART):
        end = min(start + MAX_PAGES_PART, total)
        label = f"{file_path.stem}_p{start+1}-{end}"
        sub = pymupdf.open()
        sub.insert_pdf(pdf, from_page=start, to_page=end - 1)
        tmp_path = str(tmp_dir / f"{label}.pdf")
        sub.save(tmp_path)
        sub.close()
        parts.append((tmp_path, label))
        print(f"  拆分：{label}（{end - start} 页）")
    pdf.close()
    return parts


def _upload_and_poll(file_path: str, file_name: str) -> str:
    """上传单个 PDF 到 MinerU，轮询直到完成，返回 markdown 文本。"""
    headers = _mineru_headers()

    # 1. 获取上传 URL
    resp = requests.post(
        f"{MINERU_BASE}/file-urls/batch",
        headers=headers,
        json={"files": [{"name": file_name}], "model_version": "vlm"},
        timeout=30,
    )
    resp.raise_for_status()
    data = resp.json()
    if data["code"] != 0:
        raise RuntimeError(f"MinerU file-urls 失败: {data['msg']}")
    batch_id   = data["data"]["batch_id"]
    upload_url = data["data"]["file_urls"][0]

    # 2. PUT 上传
    with open(file_path, "rb") as f:
        put_resp = requests.put(upload_url, data=f, timeout=300)
        put_resp.raise_for_status()
    print(f"  已上传：{file_name}")

    # 3. 轮询
    poll_url = f"{MINERU_BASE}/extract-results/batch/{batch_id}"
    for attempt in range(POLL_MAX):
        time.sleep(POLL_INTERVAL)
        r = requests.get(poll_url, headers=headers, timeout=30)
        r.raise_for_status()
        result = r.json()["data"]["extract_result"][0]
        state  = result["state"]
        if state == "done":
            zip_url = result["full_zip_url"]
            break
        elif state == "failed":
            raise RuntimeError(f"MinerU 解析失败: {result.get('err_msg', '未知')}")
        if attempt % 10 == 0:
            print(f"  MinerU 状态：{state}（已等待 {attempt * POLL_INTERVAL}s）…")
    else:
        raise RuntimeError("MinerU 轮询超时（>10 分钟）")

    # 4. 下载 zip，提取 .md
    zip_resp = requests.get(zip_url, timeout=120)
    zip_resp.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(zip_resp.content)) as zf:
        for name in zf.namelist():
            if name.endswith(".md"):
                return zf.read(name).decode("utf-8")
    raise RuntimeError("MinerU zip 中未找到 .md 文件")


def parse_pdf_to_markdown(pdf_path: Path) -> str:
    """
    用 MinerU API 解析 PDF，返回 markdown 文本。
    结果缓存到 parsed/<stem>.md，避免重复调用。
    """
    PARSED_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = PARSED_DIR / f"{pdf_path.stem}.md"

    # 缓存命中
    if cache_file.exists() and cache_file.stat().st_mtime >= pdf_path.stat().st_mtime:
        print(f"  缓存命中：{cache_file.name}")
        return cache_file.read_text(encoding="utf-8")

    print(f"\n[MinerU] 解析：{pdf_path.name}")
    parts = _split_pdf_parts(pdf_path)
    md_parts = []

    try:
        for i, (part_path, label) in enumerate(parts):
            name = f"{label}.pdf" if label else pdf_path.name
            print(f"  上传 {name}（{i+1}/{len(parts)}）…")
            md = _upload_and_poll(part_path, name)
            md_parts.append(md)
            print(f"  完成：{name}")
    finally:
        import shutil
        tmp_dir = PARSED_DIR / "_tmp"
        if tmp_dir.exists():
            shutil.rmtree(tmp_dir, ignore_errors=True)

    md_text = "\n\n".join(md_parts)
    cache_file.write_text(md_text, encoding="utf-8")
    print(f"  已缓存至：{cache_file}")
    return md_text


# ════════════════════════════════════════════════════════════
# 切题逻辑
# ════════════════════════════════════════════════════════════

# LaTeX 公式提取
_EQUATION_RE = re.compile(r"\$\$(.+?)\$\$|\\\[(.+?)\\\]", re.DOTALL)


def _extract_equations(text: str) -> list:
    eqs = []
    for m in _EQUATION_RE.finditer(text):
        eq = (m.group(1) or m.group(2) or "").strip()
        if eq and len(eq) < 300:
            eqs.append(eq)
    return eqs[:10]


# ── 格式1：英文核物理书（# Exercise X.X.X header，题目与解答分两段）──

def _split_nuclear_en(md_text: str) -> list:
    """
    结构：前半部分是题目，'# Appendix Solutions of Exercises' 之后是解答。
    两段都用 `# Exercise X.X.X` 作 header。按题号合并。
    """
    appendix_m = re.search(r"\n# Appendix Solutions of Exercises", md_text)
    if not appendix_m:
        # fallback：找 A.1 Solutions
        appendix_m = re.search(r"\n# A\.\d+ Solutions", md_text)
    if appendix_m:
        problems_text  = md_text[:appendix_m.start()]
        solutions_text = md_text[appendix_m.start():]
    else:
        problems_text  = md_text
        solutions_text = ""

    header_re = re.compile(r"\n# (Exercise\s+[\d\.]+)", re.IGNORECASE)

    def _extract_blocks(text):
        """返回 {exercise_id: block_text}"""
        matches = list(header_re.finditer(text))
        blocks = {}
        for i, m in enumerate(matches):
            ex_id = m.group(1).strip()
            start = m.end()
            end   = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            blocks[ex_id] = text[start:end].strip()
        return blocks

    prob_blocks = _extract_blocks(problems_text)
    sol_blocks  = _extract_blocks(solutions_text)

    # 推断章节：Exercise 1.2.3 → chapter "1.2"
    def _chapter(ex_id):
        m = re.search(r"([\d]+\.[\d]+)", ex_id)
        return m.group(1) if m else ""

    problems = []
    for ex_id, prob_text in prob_blocks.items():
        if len(prob_text) < 15:
            continue
        sol_text = sol_blocks.get(ex_id, "")
        problems.append({
            "header":        ex_id,
            "problem_text":  prob_text,
            "solution_text": sol_text,
            "chapter":       _chapter(ex_id),
            "problem_number": ex_id,
        })

    print(f"  切分出 {len(problems)} 道题目（nuclear_en）")
    return problems


# ── 格式2：曾谨言习题解（[N] 编号，[解] 紧跟）──

def _split_zeng(md_text: str) -> list:
    """
    结构：
      # 第X章：...
      [1] 题目正文
      [解] 解答正文
      [2] 下一题...
    """
    chapter_re = re.compile(r"\n# (第[^\n]+章[^\n]*)\n")
    prob_re    = re.compile(r"\n\[(\d+)\][ \t]*")
    # 三种解答标记：[解] (解) （解）
    sol_re     = re.compile(r"\[解\]|\(解\)|（解）")

    chapter_positions = [(m.start(), m.group(1)) for m in chapter_re.finditer(md_text)]

    def _current_chapter(pos):
        ch = ""
        for cpos, cname in chapter_positions:
            if cpos <= pos:
                ch = cname
        return ch

    prob_matches = list(prob_re.finditer(md_text))
    problems = []

    for i, pm in enumerate(prob_matches):
        prob_num = pm.group(1)
        prob_start = pm.end()
        prob_end   = prob_matches[i + 1].start() if i + 1 < len(prob_matches) else len(md_text)
        block = md_text[prob_start:prob_end]

        sol_m = sol_re.search(block)
        if sol_m:
            problem_text  = block[:sol_m.start()].strip()
            solution_text = block[sol_m.end():].strip()
        else:
            problem_text  = block.strip()
            solution_text = ""

        if len(problem_text) < 15:
            continue

        chapter = _current_chapter(pm.start())
        problems.append({
            "header":         f"[{prob_num}]",
            "problem_text":   problem_text,
            "solution_text":  solution_text,
            "chapter":        chapter,
            "problem_number": prob_num,
        })

    print(f"  切分出 {len(problems)} 道题目（zeng）")
    return problems


# ── 格式3：格里菲斯中译本（习题/例题编号）──

def _split_griffiths(md_text: str) -> list:
    """
    格里菲斯教材：习题以 '习题 X.Y' 标记，解答以 '解答' 开头。
    """
    prob_re = re.compile(
        r"(?:^|(?<=\n))(?:习题|例题)\s*([\d\.]+)[^\n]*\n",
        re.MULTILINE,
    )
    sol_re     = re.compile(r"解答\s*[\(（]?")
    chapter_re = re.compile(r"\n# (第[^\n]+章[^\n]*)\n")

    chapter_positions = [(m.start(), m.group(1)) for m in chapter_re.finditer(md_text)]

    def _current_chapter(pos):
        ch = ""
        for cpos, cname in chapter_positions:
            if cpos <= pos:
                ch = cname
        return ch

    matches = list(prob_re.finditer(md_text))
    problems = []
    for i, m in enumerate(matches):
        prob_num = m.group(1)
        start = m.end()
        end   = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        block = md_text[start:end].strip()
        if len(block) < 15:
            continue

        sol_m = sol_re.search(block)
        if sol_m:
            problem_text  = block[:sol_m.start()].strip()
            solution_text = block[sol_m.end():].strip()
        else:
            problem_text  = block
            solution_text = ""

        chapter = _current_chapter(m.start())
        problems.append({
            "header":         m.group(0).strip(),
            "problem_text":   problem_text,
            "solution_text":  solution_text,
            "chapter":        chapter,
            "problem_number": prob_num,
        })

    print(f"  切分出 {len(problems)} 道题目（griffiths）")
    return problems


def split_problems(md_text: str, book_meta: dict) -> list:
    """分发到对应切题函数。"""
    splitter = book_meta.get("splitter", "zeng")
    if splitter == "nuclear_en":
        return _split_nuclear_en(md_text)
    elif splitter == "zeng":
        return _split_zeng(md_text)
    elif splitter == "griffiths":
        return _split_griffiths(md_text)
    else:
        return _split_zeng(md_text)


# ════════════════════════════════════════════════════════════
# ID 管理
# ════════════════════════════════════════════════════════════

def _next_id(prefix: str) -> str:
    """扫描 raw_dataset 目录，返回下一个可用 ID（如 QN_0042）。"""
    subdir = RAW_DS_DIR / ("quantum" if prefix == "QN" else "nuclear")
    subdir.mkdir(parents=True, exist_ok=True)
    existing = sorted(subdir.glob(f"{prefix}_*.json"))
    if not existing:
        return f"{prefix}_0001"
    last = existing[-1].stem  # e.g. "QN_0041"
    num  = int(last.split("_")[1]) + 1
    return f"{prefix}_{num:04d}"


# ════════════════════════════════════════════════════════════
# JSON 构建与写入
# ════════════════════════════════════════════════════════════

def _detect_subdomain(text: str, domain: str) -> str:
    text_lower = text.lower()
    for subdomain, keywords in SUBDOMAIN_KEYWORDS.get(domain, []):
        for kw in keywords:
            if kw.lower() in text_lower:
                return subdomain
    return "general"


def _detect_book_meta(pdf_path: Path) -> dict:
    name_lower = pdf_path.name.lower()
    for keyword, meta in BOOK_META.items():
        if keyword.lower() in name_lower:
            return meta
    parts_str = str(pdf_path)
    if "量子" in parts_str:
        return BOOK_META["曾谨言"]
    if "核物理" in parts_str or "nuclear" in name_lower:
        return BOOK_META["nuclear"]
    return {"domain": "quantum_mechanics", "source_type": "textbook",
            "title": pdf_path.stem, "lang": "zh", "id_prefix": "QN", "splitter": "zeng"}


def build_raw_entry(sample_id: str, problem: dict, book_meta: dict, pdf_path: Path) -> dict:
    """将切分出的题目块组装成 raw_dataset JSON 结构。"""
    domain    = book_meta["domain"]
    subdomain = _detect_subdomain(
        problem["problem_text"] + " " + problem.get("solution_text", ""), domain
    )
    # 优先使用切题函数已提取的 chapter/problem_number
    chapter = problem.get("chapter", "")
    prob_no = problem.get("problem_number", "")
    eqs     = _extract_equations(problem["problem_text"] + "\n" + problem.get("solution_text", ""))

    return {
        "id": sample_id,
        "meta": {
            "id": sample_id,
            "domain": domain,
            "subdomain": subdomain,
            "source": {
                "type":           book_meta["source_type"],
                "title":          book_meta["title"],
                "chapter":        chapter,
                "problem_number": prob_no,
                "pdf_file":       pdf_path.name,
            },
            "difficulty": 0,
            "is_gold":    False,
            "version":    "0.1",
        },
        "raw_problem": {
            "problem_text":       problem["problem_text"],
            "solution_text":      problem.get("solution_text", ""),
            "original_equations": eqs,
        },
    }


def save_entry(entry: dict, prefix: str) -> Path:
    """将单条 JSON 写入 raw_dataset/{quantum|nuclear}/。"""
    subdir = RAW_DS_DIR / ("quantum" if prefix == "QN" else "nuclear")
    subdir.mkdir(parents=True, exist_ok=True)
    out_path = subdir / f"{entry['id']}.json"
    out_path.write_text(json.dumps(entry, ensure_ascii=False, indent=2), encoding="utf-8")
    return out_path


# ════════════════════════════════════════════════════════════
# 主流程
# ════════════════════════════════════════════════════════════

def process_pdf(pdf_path: Path, dry_run: bool = False):
    """完整处理单个 PDF：解析 → 切题 → 写 JSON。"""
    print(f"\n{'='*60}")
    print(f"处理：{pdf_path.name}")
    print(f"{'='*60}")

    book_meta = _detect_book_meta(pdf_path)
    print(f"  书目：{book_meta['title']}  领域：{book_meta['domain']}")

    # 1. MinerU 解析
    md_text = parse_pdf_to_markdown(pdf_path)
    print(f"  Markdown 长度：{len(md_text):,} 字符")

    if dry_run:
        print("  [dry-run] 跳过切题与写入")
        return

    # 2. 切题
    problems = split_problems(md_text, book_meta)

    # 3. 写 JSON
    prefix   = book_meta["id_prefix"]
    saved    = []
    for prob in problems:
        sample_id = _next_id(prefix)
        entry     = build_raw_entry(sample_id, prob, book_meta, pdf_path)
        out_path  = save_entry(entry, prefix)
        saved.append(out_path)
        print(f"  写入：{out_path.name}  子领域：{entry['meta']['subdomain']}")

    print(f"\n  完成：共写入 {len(saved)} 条样本")
    return saved


def process_all(dry_run: bool = False):
    """处理 raw_pdf/ 下所有 PDF。"""
    pdfs = list(RAW_PDF_DIR.rglob("*.pdf"))
    if not pdfs:
        print(f"raw_pdf/ 下未找到 PDF 文件：{RAW_PDF_DIR}")
        sys.exit(1)
    print(f"发现 {len(pdfs)} 个 PDF 文件")
    for pdf in pdfs:
        process_pdf(pdf, dry_run=dry_run)


def main():
    parser = argparse.ArgumentParser(
        description="Physics-PreProc-QN：PDF 解析与切题脚本"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", help="指定单个 PDF 文件路径")
    group.add_argument("--all",  action="store_true", help="处理 raw_pdf/ 下所有 PDF")
    parser.add_argument("--dry-run", action="store_true",
                        help="只解析 PDF（缓存 markdown），不切题写 JSON")
    args = parser.parse_args()

    if args.file:
        pdf_path = Path(args.file).resolve()
        if not pdf_path.exists():
            print(f"文件不存在：{pdf_path}")
            sys.exit(1)
        process_pdf(pdf_path, dry_run=args.dry_run)
    else:
        process_all(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
