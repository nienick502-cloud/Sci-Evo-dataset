"""
audit_topic_match.py  --  数据主题筛查与清理
用法:
    python audit_topic_match.py              # dry-run，只输出报告
    python audit_topic_match.py --delete     # 确认后删除不匹配文件
"""
import json, re, sys, os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATASET = PROJECT_ROOT / "raw_dataset" / "papers"
RAW_PDF     = PROJECT_ROOT / "raw_pdf" / "papers"
PARSED      = PROJECT_ROOT / "parsed" / "papers"

# ---------------------------------------------------------------------------
# 关键词匹配规则
# ---------------------------------------------------------------------------

def _has_alpha(text: str) -> bool:
    """检测文本是否包含 alpha/α 相关关键词"""
    return bool(re.search(r'alpha|α|\\alpha', text, re.IGNORECASE))

def _has_decay(text: str) -> bool:
    """检测文本是否包含衰变/半衰期相关关键词"""
    return bool(re.search(
        r'decay|衰变|half.?life|半衰期|tunneling|隧穿|Q.?val|Q值|'
        r'Geiger.?Nuttall|preformation|预成形|emission|发射|radioactiv|放射',
        text, re.IGNORECASE
    ))

def _has_ml(text: str) -> bool:
    """检测文本是否包含机器学习/深度学习相关关键词（严格版，排除泛化词）"""
    return bool(re.search(
        r'machine.?learn|neural.?network|deep.?learn|'
        r'artificial.?neural|multilayer.?perceptron|MLP|'
        r'random.?forest|support.?vector|SVM|kernel.?ridge|'
        r'XGBoost|gradient.?boost|adaboost|lightgbm|catboost|'
        r'\bCNN\b|\bRNN\b|\bLSTM\b|\bGRU\b|\bGAN\b|\btransformer\b|attention.?mechanism|'
        r'BNN|Bayesian.?neural|Gaussian.?process|'
        r'cross.?validat|train.?set|test.?set|hyperparameter|'
        r'backpropagat|feature.?select|feature.?engineer|'
        r'classif(?:ier|ication)|决策树|随机森林|支持向量|'
        r'机器学习|深度学习|神经网络|贝叶斯网络|'
        r'data.?driven|emulat|surrogate|模拟器|'
        r'k.?nearest|naive.?bayes|logistic.?regression',
        text, re.IGNORECASE
    ))

def _has_nuclear_structure(text: str) -> bool:
    """检测文本是否包含核结构相关关键词"""
    return bool(re.search(
        r'nucle|核|binding.?energy|结合能|mass|质量|'
        r'charge.?radi|电荷半径|separation.?energy|分离能|'
        r'shell|壳|fission|裂变|structure|结构|'
        r'drip.?line|滴线|isotope|同位素|'
        r'energy.?level|能级|excitat|激发|deform|形变',
        text, re.IGNORECASE
    ))

def _has_scattering(text: str) -> bool:
    """检测文本是否包含核散射/截面相关关键词"""
    return bool(re.search(
        r'scatter|散射|cross.?section|截面|reaction|反应|'
        r'elastic|弹性|optical.?model|光学模型|optical.?potential|光学势|'
        r'collision|碰撞|projectile|靶|target|入射|'
        r'angular.?distribut|角分布|differential|微分|'
        r'total.?cross|反应截面|fusion|熔合|'
        r'polariz|极化|nucleon.?nucleus|核子.?核',
        text, re.IGNORECASE
    ))

# ---------------------------------------------------------------------------
# 每个子领域的匹配函数
# ---------------------------------------------------------------------------

def _has_alpha_cluster(text: str) -> bool:
    """团簇模型专用：alpha衰变 OR 团簇放射性（alpha衰变是团簇放射的特例）"""
    if _has_alpha(text) and _has_decay(text):
        return True
    # 团簇放射性（cluster radioactivity）本身就包含alpha衰变
    if re.search(r'cluster.?radioactiv|团簇放射|cluster.?decay|团簇衰变', text, re.IGNORECASE):
        return True
    return False

MATCHERS = {
    "alpha   WKB":       lambda t: _has_alpha(t) and _has_decay(t),
    "alpha_液滴模型":     lambda t: _has_alpha(t) and _has_decay(t),
    "alpha_壳模型":       lambda t: _has_alpha(t) and _has_decay(t),
    "alpha_团簇模型":     lambda t: _has_alpha_cluster(t),
    "alpha_双折叠势模型": lambda t: _has_alpha(t) and _has_decay(t),
    "深度学习_核结构":    lambda t: _has_ml(t) and _has_nuclear_structure(t),
    "核散射_截面":        lambda t: _has_scattering(t),
    "机器学习_alpha半衰期": lambda t: _has_ml(t) and bool(re.search(
        r'alpha.?decay|α.?衰变|alpha.?radioactiv|alpha.?emission|alpha.?preformation|'
        r'Geiger.?Nuttall|alpha.?cluster|α衰变|alpha衰变',
        t, re.IGNORECASE
    )),
}

def scan_subdomain(folder_name: str) -> list[dict]:
    """扫描一个子领域，返回不匹配文件列表"""
    matcher = MATCHERS.get(folder_name)
    if matcher is None:
        return []

    folder = RAW_DATASET / folder_name
    if not folder.exists():
        print(f"[!] folder not found: {folder}")
        return []

    mismatches = []
    for jf in sorted(folder.glob("*.json")):
        try:
            data = json.loads(jf.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[!] read error {jf.name}: {e}")
            continue

        title = ""
        target = ""
        intent = ""
        try:
            title = data.get("meta", {}).get("source", {}).get("title", "")
        except Exception:
            pass
        try:
            target = data.get("01_initial_request", {}).get("target_name", "")
        except Exception:
            pass
        try:
            intent = data.get("01_initial_request", {}).get("user_intent", "")
        except Exception:
            pass

        combined = f"{title} {target} {intent}"
        if not matcher(combined):
            stem = jf.stem
            mismatches.append({
                "stem": stem,
                "folder": folder_name,
                "title": title[:80],
                "target": target[:80],
            })
    return mismatches


def delete_files(mismatches: list[dict]) -> None:
    """删除不匹配文件的 json/pdf/md"""
    for m in mismatches:
        folder = m["folder"]
        stem = m["stem"]
        paths = [
            RAW_DATASET / folder / f"{stem}.json",
            RAW_PDF / folder / f"{stem}.pdf",
            PARSED / folder / f"{stem}.md",
        ]
        for p in paths:
            if p.exists():
                p.unlink()
                print(f"  deleted: {p.relative_to(PROJECT_ROOT)}")
            else:
                print(f"  skip (not found): {p.relative_to(PROJECT_ROOT)}")


def main():
    delete_mode = "--delete" in sys.argv

    all_mismatches = []
    for folder_name in MATCHERS:
        folder = RAW_DATASET / folder_name
        if not folder.exists():
            continue
        total = len(list(folder.glob("*.json")))
        mm = scan_subdomain(folder_name)
        all_mismatches.extend(mm)
        status = f"{len(mm)}/{total} mismatch" if mm else f"0/{total} OK"
        print(f"[{'!' if mm else 'OK'}] {folder_name}: {status}")

    if not all_mismatches:
        print(f"\n=== All {sum(1 for _ in RAW_DATASET.rglob('*.json'))} files passed. ===")
        return

    print(f"\n=== {len(all_mismatches)} mismatched files ===\n")
    for i, m in enumerate(all_mismatches, 1):
        print(f"{i:3d}. [{m['folder']}] {m['stem']}")
        print(f"     title:  {m['title']}")
        print(f"     target: {m['target']}")
        print()

    if delete_mode:
        print("--- Deleting mismatched files ---")
        delete_files(all_mismatches)
        remaining = sum(1 for _ in RAW_DATASET.rglob("*.json"))
        print(f"\n=== Done. {len(all_mismatches)} entries removed. {remaining} files remaining. ===")
    else:
        print("--- Dry-run mode. Use --delete to remove these files. ---")


if __name__ == "__main__":
    main()
