"""
dfs_engine.py - DFS 反向链式搜索引擎

从目标物理量出发，反向搜索所有合法推导路径。
支持决策层剪枝：排除/锁定特定 tool 后重新搜索。

用法:
  python agent_Review/dfs_engine.py --target half_life
  python agent_Review/dfs_engine.py --target cross_section --exclude T19
  python agent_Review/dfs_engine.py --target half_life --available "mass_number_A,charge_number_Z,neutron_number_N,nucleon_density"
"""

import argparse
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CORE_LIBRARY_PATH = PROJECT_ROOT / "agent_Review" / "core_tool_library_v2.json"


class DFSEngine:
    """DFS 反向链式搜索引擎"""

    def __init__(self, library_path: str | Path = CORE_LIBRARY_PATH):
        with open(library_path, encoding="utf-8") as f:
            lib = json.load(f)

        self.tools = [t for t in lib["tools"] if "id" in t]
        self.ontology = lib.get("physical_quantity_ontology", {})
        self.composite_decomposition = lib.get("composite_tool_decomposition", {})
        self.context_constraints = lib.get("context_constraints", {})

        # 构建索引
        self.provides_index: dict[str, list[str]] = {}  # quantity -> [tool_id]
        self.tool_map: dict[str, dict] = {}  # tool_id -> tool

        for t in self.tools:
            self.tool_map[t["id"]] = t
            for p in t.get("provides", []):
                self.provides_index.setdefault(p, []).append(t["id"])

    def load_auxiliary_library(self, library_path: str | Path) -> int:
        """加载辅助工具库（如 ML DFS 库），合并到当前引擎的索引中。

        用于双轨 DFS：物理库作为主库，ML 库按需挂载。
        纯物理论文不调用此方法，行为与单库完全一致。

        Args:
            library_path: 辅助库 JSON 文件路径

        Returns:
            加载的 tool 数量（0 表示文件不存在或无效）
        """
        lib_path = Path(library_path)
        if not lib_path.exists():
            return 0

        with open(lib_path, encoding="utf-8") as f:
            lib = json.load(f)

        new_tools = [t for t in lib.get("tools", []) if "id" in t]
        for t in new_tools:
            self.tools.append(t)
            self.tool_map[t["id"]] = t
            for p in t.get("provides", []):
                self.provides_index.setdefault(p, []).append(t["id"])

        # 合并 ontology（ML 专用量加入 ml_quantities 或新增顶级键）
        aux_ontology = lib.get("ml_quantity_ontology", {})
        if aux_ontology:
            existing_ml = self.ontology.setdefault("ml_quantities", {})
            for key, spec in aux_ontology.items():
                if key not in existing_ml:
                    existing_ml[key] = spec

        # 合并 composite_decomposition
        aux_composite = lib.get("composite_paths", {})
        if aux_composite:
            self.composite_decomposition.update(aux_composite)

        # 合并 context_constraints
        aux_constraints = lib.get("context_constraints", {})
        if aux_constraints:
            self.context_constraints.update(aux_constraints)

        return len(new_tools)

    def find_all_paths(
        self,
        target: str,
        available: set[str],
        excluded_tools: set[str] | None = None,
        locked_tools: set[str] | None = None,
        max_depth: int = 15,
        max_paths: int = 10,
    ) -> list[list[str]]:
        """
        从 target 反向搜索所有合法推导路径。

        Args:
            target: 目标物理量
            available: 初始可用物理量集合
            excluded_tools: 被决策层排除的 tool_id 集合
            locked_tools: 被决策层锁定的 tool_id 集合（如果非空，优先使用这些）
            max_depth: 最大搜索深度
            max_paths: 最多返回路径数

        Returns:
            list of paths, 每条路径是 tool_id 的有序列表（从起点到终点）
        """
        excluded = excluded_tools or set()
        locked = locked_tools or set()
        all_paths: list[list[str]] = []

        def dfs(tgt: str, avail: set[str], path: list[str],
                visited_tools: set[str], depth: int):
            if len(all_paths) >= max_paths:
                return
            if tgt in avail:
                # 目标已可用，当前 path 是一条合法路径
                all_paths.append(list(reversed(path)))
                return
            if depth >= max_depth:
                return

            providers = self.provides_index.get(tgt, [])
            for tid in providers:
                if tid in excluded:
                    continue
                if tid in visited_tools:
                    continue
                # 如果有 locked_tools 且该 target 有 locked 的 provider，优先用 locked
                if locked:
                    locked_providers = [p for p in providers if p in locked]
                    if locked_providers and tid not in locked:
                        continue

                tool = self.tool_map[tid]
                requires = tool.get("requires", [])

                # 尝试满足该 tool 的所有 requires
                new_avail = avail | set(tool.get("provides", []))
                new_visited = visited_tools | {tid}

                # 检查所有 requires 是否可满足（递归）
                feasible = True
                sub_path = [tid]

                for req in requires:
                    if req in new_avail:
                        continue
                    # 递归搜索 req
                    sub_paths_before = len(all_paths)
                    saved_paths = list(all_paths)

                    # 临时搜索：看 req 是否可达
                    temp_paths: list[list[str]] = []
                    self._find_one_path(req, new_avail, excluded, locked,
                                        new_visited, max_depth - depth - 1,
                                        temp_paths)
                    if not temp_paths:
                        feasible = False
                        break
                    # 取第一条可行子路径
                    sub_path = temp_paths[0] + sub_path
                    for sub_tid in temp_paths[0]:
                        sub_tool = self.tool_map[sub_tid]
                        new_avail = new_avail | set(sub_tool.get("provides", []))
                        new_visited = new_visited | {sub_tid}

                if feasible:
                    full_path = path + sub_path
                    # 检查 target 现在是否可用
                    if tgt in new_avail:
                        all_paths.append(list(reversed(full_path)))
                    else:
                        dfs(tgt, new_avail, full_path, new_visited, depth + 1)

        dfs(target, available, [], set(), 0)
        return all_paths

    def _find_one_path(
        self,
        target: str,
        available: set[str],
        excluded: set[str],
        locked: set[str],
        visited: set[str],
        max_depth: int,
        result: list[list[str]],
    ):
        """找到一条从 available 到 target 的路径"""
        if target in available:
            result.append([])
            return
        if max_depth <= 0:
            return

        providers = self.provides_index.get(target, [])
        for tid in providers:
            if tid in excluded or tid in visited:
                continue
            if locked:
                locked_providers = [p for p in providers if p in locked]
                if locked_providers and tid not in locked:
                    continue

            tool = self.tool_map[tid]
            new_avail = available | set(tool.get("provides", []))
            new_visited = visited | {tid}

            sub_chain = [tid]
            feasible = True

            for req in tool.get("requires", []):
                if req in new_avail:
                    continue
                sub_result: list[list[str]] = []
                self._find_one_path(req, new_avail, excluded, locked,
                                    new_visited, max_depth - 1, sub_result)
                if not sub_result:
                    feasible = False
                    break
                sub_chain = sub_result[0] + sub_chain
                for sub_tid in sub_result[0]:
                    sub_tool = self.tool_map[sub_tid]
                    new_avail = new_avail | set(sub_tool.get("provides", []))
                    new_visited = new_visited | {sub_tid}

            if feasible:
                result.append(sub_chain)
                return

    def find_optimal_path(
        self,
        target: str,
        available: set[str],
        excluded_tools: set[str] | None = None,
        locked_tools: set[str] | None = None,
    ) -> list[str] | None:
        """找到最短的一条合法路径"""
        paths = self.find_all_paths(target, available, excluded_tools,
                                     locked_tools, max_paths=5)
        if not paths:
            return None
        return min(paths, key=len)

    def path_to_readable(self, path: list[str]) -> str:
        """将 tool_id 路径转为人类可读的物理量传递链"""
        if not path:
            return "(empty)"
        parts = []
        for tid in path:
            tool = self.tool_map[tid]
            provides = tool.get("provides", [])
            parts.append(f"{tool['tool_name']} -> {', '.join(provides)}")
        return " => ".join(parts)

    def path_to_quantity_chain(self, path: list[str]) -> str:
        """将路径转为简洁的物理量链"""
        if not path:
            return "(empty)"
        quantities = []
        for tid in path:
            tool = self.tool_map[tid]
            for p in tool.get("provides", []):
                if p not in quantities:
                    quantities.append(p)
        return " -> ".join(quantities)

    def apply_decision(
        self,
        decision_type: str,
        decision_content: str,
        current_paths: list[list[str]],
        failure_points: list[str] | None = None,
    ) -> tuple[list[list[str]], dict]:
        """
        应用决策层步骤的剪枝。支持三层置信度。

        Layer 1 (hard_exclude): 论文明确否定的方法（来自 failure_points）
        Layer 2 (soft_disfavor): LLM thought 中的排除性陈述（降权不删除）
        Layer 3 (lock): LLM thought 中的选择性陈述（优先级提升）

        Args:
            decision_type: 决策类型 (model_selection, physical_argument, etc.)
            decision_content: 决策内容（thought 字段文本）
            current_paths: 当前合法路径集合
            failure_points: 论文明确否定的方法描述列表（来自 paper_facts）

        Returns:
            (filtered_paths, decision_log)
        """
        hard_exclude_ids: set[str] = set()
        soft_disfavor_ids: set[str] = set()
        locked_ids: set[str] = set()

        content_lower = decision_content.lower().replace("-", "_").replace(" ", "_")

        # ── Layer 1: failure_points -> hard_exclude ─────────────────
        if failure_points:
            for fp in failure_points:
                fp_lower = fp.lower().replace("-", "_").replace(" ", "_")
                for tool in self.tools:
                    name_lower = tool["tool_name"].lower()
                    if self._tool_name_in_text(name_lower, fp_lower):
                        hard_exclude_ids.add(tool["id"])

        # ── Layer 2+3: LLM thought 解析 ──────────────────────────
        HARD_EXCLUDE_KW = [
            "fails", "breakdown", "physically_invalid", "contradicts_experiment",
            "gives_wrong", "severely_overestimates", "severely_underestimates",
        ]
        SOFT_DISFAVOR_KW = [
            "not_use", "instead_of", "rather_than", "exclude",
            "inappropriate", "not_applicable", "not_suitable",
            "reject", "abandon", "inadequate",
        ]
        LOCK_KW = [
            "choose", "select", "adopt", "employ", "apply",
            "we_use", "is_used", "will_use", "prefer",
        ]

        for tool in self.tools:
            name_lower = tool["tool_name"].lower()
            if not self._tool_name_in_text(name_lower, content_lower):
                continue

            # 优先级：hard_exclude > soft_disfavor > lock
            if any(kw in content_lower for kw in HARD_EXCLUDE_KW):
                hard_exclude_ids.add(tool["id"])
            elif any(kw in content_lower for kw in SOFT_DISFAVOR_KW):
                soft_disfavor_ids.add(tool["id"])
            elif any(kw in content_lower for kw in LOCK_KW):
                locked_ids.add(tool["id"])

        if not hard_exclude_ids and not soft_disfavor_ids and not locked_ids:
            return current_paths, {
                "decision_type": decision_type,
                "hard_excluded_tools": [],
                "soft_disfavored_tools": [],
                "locked_tools": [],
                "paths_before": len(current_paths),
                "paths_after": len(current_paths),
                "hard_exclude_from_failure_points": False,
            }

        # ── 路径过滤 ────────────────────────────────────────────
        # Step 1: 硬排除
        if hard_exclude_ids:
            filtered = [p for p in current_paths if not (set(p) & hard_exclude_ids)]
            if not filtered:
                # 所有路径都被硬排除 -> 仅删除 hard_exclude，保留其余
                filtered = list(current_paths)
        else:
            filtered = list(current_paths)

        # Step 2: locked 路径置顶（仅在前3个元素内，不删除非locked路径）
        if locked_ids:
            locked_paths = [p for p in filtered if set(p) & locked_ids]
            unlocked_paths = [p for p in filtered if not (set(p) & locked_ids)]
            filtered = locked_paths + unlocked_paths

        # Step 3: soft_disfavor 路径降底（保留所有路径，仅调整顺序）
        if soft_disfavor_ids:
            disfavored = [p for p in filtered if set(p) & soft_disfavor_ids]
            neutral = [p for p in filtered if not (set(p) & soft_disfavor_ids)]
            filtered = neutral + disfavored

        # ── 决策日志 ────────────────────────────────────────────
        decision_log = {
            "decision_type": decision_type,
            "hard_excluded_tools": [self.tool_map[tid]["tool_name"] for tid in hard_exclude_ids],
            "soft_disfavored_tools": [self.tool_map[tid]["tool_name"] for tid in soft_disfavor_ids],
            "locked_tools": [self.tool_map[tid]["tool_name"] for tid in locked_ids],
            "paths_before": len(current_paths),
            "paths_after": len(filtered),
            "hard_exclude_from_failure_points": len(hard_exclude_ids) > 0 and failure_points is not None,
        }

        return filtered, decision_log


    def _tool_name_in_text(self, tool_name_lower: str, text_lower: str) -> bool:
        """检查 tool 名是否出现在文本中（子串匹配，含分词逻辑）"""
        if tool_name_lower in text_lower:
            return True
        # 分词匹配：至少匹配 2 个有效词干
        parts = tool_name_lower.split("_")
        significant = [p for p in parts if len(p) > 3]
        if len(significant) < 2:
            significant = parts
        return all(p in text_lower for p in significant if len(p) > 3)

    def step_on_valid_path(
        self,
        tool_id: str,
        step_index: int,
        current_paths: list[list[str]],
        available_quantities: set[str] | None = None,
    ) -> bool:
        """检查某个 tool 是否合法：1) 在路径上 2) requires 已被满足"""
        # 检查 1: 路径归属
        on_path = any(tool_id in path for path in current_paths)
        if not on_path:
            return False
        # 检查 2: 依赖满足
        if available_quantities is not None:
            tool = self.tool_map.get(tool_id)
            if tool:
                unmet = set(tool.get("requires", [])) - available_quantities
                if unmet:
                    return False
        return True


def main():
    parser = argparse.ArgumentParser(description="DFS Engine - find valid derivation paths")
    parser.add_argument("--target", type=str, default="half_life")
    parser.add_argument("--available", type=str,
                        default="mass_number_A,charge_number_Z,neutron_number_N")
    parser.add_argument("--exclude", type=str, default="", help="Comma-separated tool IDs to exclude")
    parser.add_argument("--lock", type=str, default="", help="Comma-separated tool IDs to lock")
    args = parser.parse_args()

    engine = DFSEngine()
    available = set(args.available.split(","))
    excluded = set(args.exclude.split(",")) if args.exclude else set()
    locked = set(args.lock.split(",")) if args.lock else set()

    print(f"[*] Target: {args.target}")
    print(f"[*] Available: {available}")
    if excluded:
        print(f"[*] Excluded: {excluded}")
    if locked:
        print(f"[*] Locked: {locked}")

    paths = engine.find_all_paths(args.target, available, excluded, locked)
    print(f"\n[OK] Found {len(paths)} valid paths:\n")

    for i, path in enumerate(paths, 1):
        print(f"  Path {i} ({len(path)} steps):")
        for tid in path:
            tool = engine.tool_map[tid]
            print(f"    {tid}: {tool['tool_name']}")
            print(f"        {tool['requires']} -> {tool['provides']}")
        print(f"  Quantity chain: {engine.path_to_quantity_chain(path)}")
        print()


if __name__ == "__main__":
    main()
