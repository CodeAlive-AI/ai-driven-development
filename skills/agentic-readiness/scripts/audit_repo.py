#!/usr/bin/env python3
"""Audit repository readiness for Codex, Claude Code, and OpenCode.

The script emits JSON and intentionally reports configuration metadata only. It
never prints configuration values and never inspects credential stores.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python <3.11
    tomllib = None


EXCLUDED_DIRS = {
    ".git",
    ".hg",
    ".svn",
    ".idea",
    ".next",
    ".nuxt",
    ".output",
    ".pytest_cache",
    ".tox",
    ".venv",
    ".worktrees",
    "__pycache__",
    "bin",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "obj",
    "target",
    "vendor",
    "worktrees",
}
INSTRUCTION_NAMES = {"AGENTS.md", "AGENTS.override.md", "CLAUDE.md", "CLAUDE.local.md"}
IMPORT_RE = re.compile(
    r"(?<![\w`])@((?:~|\.{1,2})?/?[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_. -]+)*\.[A-Za-z0-9_-]+)"
)
SECRET_KEY_RE = re.compile(
    r"(?:secret|token|password|api[_-]?key|private[_-]?key|credential)", re.I
)
PRIORITY_ORDER = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}


@dataclass
class InstructionFileReport:
    path: str
    kind: str
    scope: str
    platforms: list[str]
    bytes: int = 0
    lines: int = 0
    headings: int = 0
    imports: list[str] = field(default_factory=list)
    missing_imports: list[str] = field(default_factory=list)
    is_symlink: bool = False
    symlink_target: str | None = None
    tracked: bool = False
    last_git_commit_iso: str | None = None
    issues: list[str] = field(default_factory=list)


@dataclass
class ConfigFileReport:
    path: str
    platform: str
    scope: str
    format: str
    bytes: int = 0
    valid: bool = True
    top_level_keys: list[str] = field(default_factory=list)
    possible_secret_keys: list[str] = field(default_factory=list)
    mcp_server_count: int = 0
    issues: list[str] = field(default_factory=list)


@dataclass
class SkillReport:
    path: str
    name: str
    scope: str
    source: str
    has_description: bool = False
    has_scripts: bool = False
    has_references: bool = False
    has_assets: bool = False
    skill_md_lines: int = 0
    issues: list[str] = field(default_factory=list)


@dataclass
class SubagentReport:
    path: str
    name: str
    platform: str
    scope: str
    lines: int = 0
    issues: list[str] = field(default_factory=list)


def _run(cmd: list[str], cwd: Path) -> tuple[int, str, str]:
    try:
        result = subprocess.run(
            cmd, cwd=str(cwd), text=True, capture_output=True, check=False
        )
    except OSError as exc:
        return 127, "", str(exc)
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def _is_git_repo(root: Path) -> bool:
    rc, out, _ = _run(["git", "rev-parse", "--is-inside-work-tree"], root)
    return rc == 0 and out == "true"


def _git_tracked_files(root: Path) -> list[str] | None:
    rc, out, _ = _run(["git", "ls-files"], root)
    if rc != 0:
        return None
    return [line for line in out.splitlines() if line.strip()]


def _git_last_commit_iso(root: Path, rel_path: str) -> str | None:
    rc, out, _ = _run(["git", "log", "-1", "--format=%cI", "--", rel_path], root)
    return out.splitlines()[0].strip() if rc == 0 and out else None


def _safe_read_text(path: Path, max_bytes: int = 2_000_000) -> str:
    try:
        data = path.read_bytes()[:max_bytes]
        return data.decode("utf-8", errors="replace")
    except OSError:
        return ""


def _relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def _walk_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for current, dirs, names in os.walk(root, followlinks=False):
        current_path = Path(current)
        dirs[:] = sorted(
            d
            for d in dirs
            if d not in EXCLUDED_DIRS and not (current_path / d / ".git").exists()
        )
        for name in sorted(names):
            files.append(current_path / name)
    return files


def _extract_imports(text: str) -> list[str]:
    imports: list[str] = []
    for match in IMPORT_RE.finditer(text):
        value = match.group(1).strip()
        if value not in imports:
            imports.append(value)
    return imports


def _resolve_reference(base_dir: Path, raw: str) -> Path:
    if raw.startswith("~"):
        return Path(os.path.expanduser(raw)).resolve()
    candidate = Path(raw)
    return (
        candidate.resolve()
        if candidate.is_absolute()
        else (base_dir / candidate).resolve()
    )


def _instruction_kind(path: Path) -> tuple[str, list[str]]:
    if path.name == "AGENTS.override.md":
        return "agents-override", ["codex"]
    if path.name == "AGENTS.md":
        return "agents", ["codex", "opencode"]
    if path.name == "CLAUDE.local.md":
        return "claude-local", ["claude-code"]
    if path.name == "CLAUDE.md":
        return "claude", ["claude-code", "opencode-fallback"]
    if ".claude" in path.parts and "rules" in path.parts:
        return "claude-rule", ["claude-code"]
    if path.name == "GEMINI.md":
        return "legacy-agent-copy", ["other"]
    return "other", []


def _analyze_instruction(
    path: Path,
    scope: str,
    root: Path,
    tracked: set[str],
) -> InstructionFileReport:
    kind, platforms = _instruction_kind(path)
    rel = _relative(path, root)
    exists = path.exists() or path.is_symlink()
    report = InstructionFileReport(
        path=rel, kind=kind, scope=scope, platforms=platforms
    )
    if not exists:
        report.issues.append("Path does not resolve")
        return report

    report.is_symlink = path.is_symlink()
    if report.is_symlink:
        try:
            report.symlink_target = os.readlink(path)
        except OSError:
            report.issues.append("Cannot read symlink target")

    text = _safe_read_text(path)
    try:
        report.bytes = path.stat().st_size
    except OSError:
        report.bytes = 0
    report.lines = text.count("\n") + (1 if text else 0)
    report.headings = len(re.findall(r"^#{1,6}\s+", text, re.MULTILINE))
    report.imports = _extract_imports(text)
    for imported in report.imports:
        if not _resolve_reference(path.parent, imported).exists():
            report.missing_imports.append(imported)

    report.tracked = rel in tracked
    if report.tracked:
        report.last_git_commit_iso = _git_last_commit_iso(root, rel)

    is_shim = kind == "claude" and report.imports and report.lines <= 10
    if not text.strip():
        report.issues.append("Empty instruction file")
    if report.missing_imports and kind in {"claude", "claude-local"}:
        report.issues.append(
            f"Missing Claude imports: {', '.join(report.missing_imports)}"
        )
    if report.lines > 500:
        report.issues.append(f"Very large instruction file ({report.lines} lines)")
    elif kind.startswith("claude") and report.lines > 200:
        report.issues.append(
            f"Claude recommends keeping each CLAUDE.md under 200 lines ({report.lines})"
        )
    if report.headings == 0 and not is_shim and report.lines > 10:
        report.issues.append("Long instruction file has no Markdown headings")
    return report


def _discover_instruction_files(
    root: Path, include_user_scope: bool
) -> list[tuple[Path, str]]:
    discovered: list[tuple[Path, str]] = []
    for path in _walk_files(root):
        if path.name in INSTRUCTION_NAMES or path.name == "GEMINI.md":
            discovered.append(
                (path, "project-nested" if path.parent != root else "project")
            )
        elif path.suffix == ".md" and ".claude" in path.parts and "rules" in path.parts:
            discovered.append((path, "project-rule"))

    if include_user_scope:
        home = Path.home()
        candidates = [
            home / ".codex" / "AGENTS.override.md",
            home / ".codex" / "AGENTS.md",
            home / ".claude" / "CLAUDE.md",
            home / ".config" / "opencode" / "AGENTS.md",
        ]
        discovered.extend(
            (path, "user") for path in candidates if path.exists() or path.is_symlink()
        )
    return discovered


def _strip_jsonc(text: str) -> str:
    text = re.sub(r"^\s*//.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r",\s*([}\]])", r"\1", text)
    return text


def _collect_secret_keys(value: Any, prefix: str = "") -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key)
            qualified = f"{prefix}.{key_text}" if prefix else key_text
            if SECRET_KEY_RE.search(key_text):
                found.add(qualified)
            found.update(_collect_secret_keys(child, qualified))
    elif isinstance(value, list):
        for child in value:
            found.update(_collect_secret_keys(child, prefix))
    return found


def _analyze_config(
    path: Path, platform: str, scope: str, root: Path
) -> ConfigFileReport:
    fmt = (
        "toml"
        if path.suffix == ".toml"
        else "jsonc"
        if path.suffix == ".jsonc"
        else "json"
    )
    report = ConfigFileReport(
        path=_relative(path, root),
        platform=platform,
        scope=scope,
        format=fmt,
        bytes=path.stat().st_size,
    )
    text = _safe_read_text(path)
    try:
        if fmt == "toml":
            if tomllib is None:
                raise ValueError("Python 3.11+ is required to parse TOML")
            data = tomllib.loads(text)
        else:
            data = json.loads(_strip_jsonc(text) if fmt == "jsonc" else text)
        if not isinstance(data, dict):
            raise ValueError("Top-level configuration must be an object/table")
    except (json.JSONDecodeError, ValueError) as exc:
        report.valid = False
        report.issues.append(f"Invalid {fmt.upper()} configuration: {exc}")
        return report

    report.top_level_keys = sorted(str(key) for key in data.keys())
    report.possible_secret_keys = sorted(_collect_secret_keys(data))
    if platform == "codex":
        servers = data.get("mcp_servers", {})
    elif platform == "claude-code":
        servers = data.get("mcpServers", {})
    else:
        servers = data.get("mcp", {})
    report.mcp_server_count = len(servers) if isinstance(servers, dict) else 0
    if scope.startswith("project") and report.possible_secret_keys:
        report.issues.append(
            "Project config contains secret-like keys; verify values are references, not credentials"
        )
    return report


def _discover_configs(
    root: Path, include_user_scope: bool
) -> list[tuple[Path, str, str]]:
    candidates: list[tuple[Path, str, str]] = [
        (root / ".codex" / "config.toml", "codex", "project"),
        (root / ".claude" / "settings.json", "claude-code", "project"),
        (root / ".claude" / "settings.local.json", "claude-code", "project-local"),
        (root / "opencode.json", "opencode", "project"),
        (root / "opencode.jsonc", "opencode", "project"),
        (root / ".opencode" / "opencode.json", "opencode", "project"),
        (root / ".opencode" / "opencode.jsonc", "opencode", "project"),
    ]
    if include_user_scope:
        home = Path.home()
        candidates.extend(
            [
                (home / ".codex" / "config.toml", "codex", "user"),
                (home / ".claude" / "settings.json", "claude-code", "user"),
                (home / ".config" / "opencode" / "opencode.json", "opencode", "user"),
                (home / ".config" / "opencode" / "opencode.jsonc", "opencode", "user"),
            ]
        )
    return [
        (path, platform, scope)
        for path, platform, scope in candidates
        if path.is_file()
    ]


def _discover_mcp_configs(
    root: Path, include_user_scope: bool
) -> list[tuple[Path, str, str]]:
    candidates: list[tuple[Path, str, str]] = [
        (root / ".mcp.json", "claude-code", "project"),
        (root / ".claude" / "mcp.json", "claude-code", "project"),
    ]
    if include_user_scope:
        candidates.append((Path.home() / ".claude" / "mcp.json", "claude-code", "user"))
    return [
        (path, platform, scope)
        for path, platform, scope in candidates
        if path.is_file()
    ]


def _discover_skills(
    root: Path, include_user_scope: bool
) -> list[tuple[Path, str, str]]:
    locations: list[tuple[Path, str, str]] = [
        (root / "skills", "project", "agent-skills"),
        (root / ".agents" / "skills", "project", "agent-skills"),
        (root / ".codex" / "skills", "project", "codex"),
        (root / ".claude" / "skills", "project", "claude-code"),
        (root / ".opencode" / "skills", "project", "opencode"),
    ]
    if include_user_scope:
        home = Path.home()
        locations.extend(
            [
                (home / ".agents" / "skills", "user", "agent-skills"),
                (home / ".codex" / "skills", "user", "codex"),
                (home / ".claude" / "skills", "user", "claude-code"),
                (home / ".config" / "opencode" / "skills", "user", "opencode"),
            ]
        )

    found: dict[Path, tuple[Path, str, str]] = {}
    for base, scope, source in locations:
        if not base.is_dir():
            continue
        for child in base.iterdir():
            if child.is_dir() and (child / "SKILL.md").is_file():
                found.setdefault(child.resolve(), (child, scope, source))
    return list(found.values())


def _analyze_skill(path: Path, scope: str, source: str, root: Path) -> SkillReport:
    skill_md = path / "SKILL.md"
    text = _safe_read_text(skill_md)
    lines = text.count("\n") + (1 if text else 0)
    frontmatter = (
        text.split("---", 2)[1]
        if text.startswith("---") and text.count("---") >= 2
        else ""
    )
    report = SkillReport(
        path=_relative(path, root),
        name=path.name,
        scope=scope,
        source=source,
        has_description=bool(
            re.search(r"^description:\s*\S", frontmatter, re.MULTILINE)
        ),
        has_scripts=(path / "scripts").is_dir(),
        has_references=(path / "references").is_dir(),
        has_assets=(path / "assets").is_dir(),
        skill_md_lines=lines,
    )
    if not report.has_description:
        report.issues.append("Missing description in SKILL.md frontmatter")
    if not re.search(
        r"^name:\s*" + re.escape(path.name) + r"\s*$", frontmatter, re.MULTILINE
    ):
        report.issues.append("Skill frontmatter name does not match directory name")
    if lines > 500:
        report.issues.append(
            f"SKILL.md is very large ({lines} lines); move detail to references/"
        )
    return report


def _discover_subagents(
    root: Path, include_user_scope: bool
) -> list[tuple[Path, str, str]]:
    locations: list[tuple[Path, str, str, str]] = [
        (root / ".codex" / "agents", "*.toml", "codex", "project"),
        (root / ".claude" / "agents", "*.md", "claude-code", "project"),
        (root / ".opencode" / "agents", "*.md", "opencode", "project"),
    ]
    if include_user_scope:
        home = Path.home()
        locations.extend(
            [
                (home / ".codex" / "agents", "*.toml", "codex", "user"),
                (home / ".claude" / "agents", "*.md", "claude-code", "user"),
                (home / ".config" / "opencode" / "agents", "*.md", "opencode", "user"),
            ]
        )
    found: list[tuple[Path, str, str]] = []
    for base, pattern, platform, scope in locations:
        if base.is_dir():
            found.extend((path, platform, scope) for path in sorted(base.glob(pattern)))
    return found


def _analyze_subagent(
    path: Path, platform: str, scope: str, root: Path
) -> SubagentReport:
    text = _safe_read_text(path)
    report = SubagentReport(
        path=_relative(path, root),
        name=path.stem,
        platform=platform,
        scope=scope,
        lines=text.count("\n") + (1 if text else 0),
    )
    if not text.strip():
        report.issues.append("Empty subagent definition")
    if "description" not in text.lower():
        report.issues.append("No description found")
    return report


def _directory_stats(root: Path, tracked: list[str] | None) -> list[dict[str, Any]]:
    counts: dict[str, int] = {}
    if tracked is not None:
        for rel in tracked:
            top = rel.split("/", 1)[0] if "/" in rel else "."
            counts[top] = counts.get(top, 0) + 1
    else:
        for path in _walk_files(root):
            rel = _relative(path, root)
            top = rel.split("/", 1)[0] if "/" in rel else "."
            counts[top] = counts.get(top, 0) + 1
    return [
        {"dir": name, "files": count}
        for name, count in sorted(
            counts.items(), key=lambda item: item[1], reverse=True
        )[:20]
    ]


def _codex_chain_metrics(root: Path, instruction_paths: list[Path]) -> dict[str, Any]:
    directories = {root}
    directories.update(
        path.parent
        for path in instruction_paths
        if path.name in {"AGENTS.md", "AGENTS.override.md"}
    )
    chains: list[dict[str, Any]] = []
    for target in sorted(directories, key=lambda path: str(path)):
        try:
            relative_parts = target.relative_to(root).parts
        except ValueError:
            continue
        current = root
        selected: list[Path] = []
        for part in (None, *relative_parts):
            if part is not None:
                current /= part
            override = current / "AGENTS.override.md"
            standard = current / "AGENTS.md"
            if override.is_file():
                selected.append(override)
            elif standard.is_file():
                selected.append(standard)
        total = sum(path.stat().st_size for path in selected)
        chains.append(
            {
                "target_directory": _relative(target, root),
                "files": [_relative(path, root) for path in selected],
                "combined_bytes": total,
            }
        )
    worst = max(
        chains,
        key=lambda item: item["combined_bytes"],
        default={"combined_bytes": 0, "files": [], "target_directory": "."},
    )
    return {
        "default_max_bytes": 32768,
        "worst_known_chain": worst,
        "known_chains": chains,
    }


def _child_git_repositories(root: Path) -> list[str]:
    children: list[str] = []
    try:
        entries = list(root.iterdir())
    except OSError:
        return children
    for child in entries:
        if (
            child.is_dir()
            and child.name not in EXCLUDED_DIRS
            and (child / ".git").exists()
        ):
            children.append(child.name)
    return sorted(children)


def _issue(
    priority: str, category: str, message: str, file: str | None = None
) -> dict[str, str]:
    result = {"priority": priority, "category": category, "message": message}
    if file:
        result["file"] = file
    return result


def audit(root: Path, include_user_scope: bool = False) -> dict[str, Any]:
    root = root.resolve()
    tracked_list = _git_tracked_files(root) if _is_git_repo(root) else None
    tracked = set(tracked_list or [])
    project_files = _walk_files(root)
    file_count = len(tracked_list) if tracked_list is not None else len(project_files)

    instruction_candidates = _discover_instruction_files(root, include_user_scope)
    instruction_reports = [
        _analyze_instruction(path, scope, root, tracked)
        for path, scope in instruction_candidates
    ]
    project_instruction_paths = [
        path for path, scope in instruction_candidates if scope.startswith("project")
    ]

    config_reports = [
        _analyze_config(path, platform, scope, root)
        for path, platform, scope in _discover_configs(root, include_user_scope)
    ]
    mcp_reports = [
        _analyze_config(path, platform, scope, root)
        for path, platform, scope in _discover_mcp_configs(root, include_user_scope)
    ]
    skill_reports = [
        _analyze_skill(path, scope, source, root)
        for path, scope, source in _discover_skills(root, include_user_scope)
    ]
    subagent_reports = [
        _analyze_subagent(path, platform, scope, root)
        for path, platform, scope in _discover_subagents(root, include_user_scope)
    ]

    issues: list[dict[str, str]] = []
    recommendations: list[dict[str, str]] = []
    root_agents = root / "AGENTS.md"
    root_claude = root / "CLAUDE.md"
    agents_exists = root_agents.exists() or root_agents.is_symlink()
    claude_exists = root_claude.exists() or root_claude.is_symlink()

    if not agents_exists and not claude_exists:
        issues.append(
            _issue("P0", "instructions", "No root AGENTS.md or CLAUDE.md found")
        )
    elif not agents_exists:
        issues.append(
            _issue(
                "P1",
                "instructions",
                "No root AGENTS.md; Codex and OpenCode lack a shared canonical instruction file",
            )
        )
    elif not claude_exists:
        issues.append(
            _issue(
                "P1",
                "instructions",
                "No root CLAUDE.md; Claude Code does not natively load AGENTS.md",
            )
        )

    if agents_exists and root_agents.is_symlink():
        issues.append(
            _issue(
                "P2",
                "instructions",
                "Canonical AGENTS.md should normally be a regular file",
                "AGENTS.md",
            )
        )

    if agents_exists and claude_exists:
        agents_text = _safe_read_text(root_agents).strip()
        claude_text = _safe_read_text(root_claude).strip()
        claude_imports = _extract_imports(claude_text)
        imports_agents = any(
            _resolve_reference(root_claude.parent, item) == root_agents.resolve()
            for item in claude_imports
        )
        if root_claude.is_symlink():
            recommendations.append(
                _issue(
                    "P2",
                    "instructions",
                    "Prefer a portable CLAUDE.md containing @AGENTS.md over a symlink",
                    "CLAUDE.md",
                )
            )
        elif not imports_agents:
            if agents_text == claude_text:
                issues.append(
                    _issue(
                        "P1",
                        "instructions",
                        "AGENTS.md and CLAUDE.md are independent duplicate copies and can drift",
                        "CLAUDE.md",
                    )
                )
            else:
                issues.append(
                    _issue(
                        "P1",
                        "instructions",
                        "CLAUDE.md does not import canonical AGENTS.md; verify intentional divergence",
                        "CLAUDE.md",
                    )
                )

    for report in instruction_reports:
        for message in report.issues:
            priority = (
                "P1"
                if "Missing Claude imports" in message or "Empty" in message
                else "P2"
            )
            issues.append(_issue(priority, "instructions", message, report.path))
        if report.kind == "agents-override" and report.tracked:
            issues.append(
                _issue(
                    "P1",
                    "instructions",
                    "Tracked AGENTS.override.md masks AGENTS.md at the same directory for Codex",
                    report.path,
                )
            )

    nested_agents = sorted(
        report.path
        for report in instruction_reports
        if report.scope == "project-nested"
        and report.kind in {"agents", "agents-override"}
    )
    root_text = _safe_read_text(root_agents) if agents_exists else ""
    has_chain_invariant = bool(
        re.search(r"read every applicable\s+`?AGENTS\.md`?", root_text, re.I)
        or (
            "applicable instruction chain" in root_text.lower()
            and "AGENTS.md" in root_text
        )
    )
    unindexed_nested = [path for path in nested_agents if path not in root_text]
    if unindexed_nested and not has_chain_invariant:
        recommendations.append(
            _issue(
                "P2",
                "routing",
                f"{len(unindexed_nested)} nested AGENTS files are not named in root routing and no general chain invariant was detected",
                "AGENTS.md",
            )
        )

    child_repos = _child_git_repositories(root)
    unrouted_children = [
        name for name in child_repos if f"{name}/AGENTS.md" not in root_text
    ]
    if unrouted_children:
        issues.append(
            _issue(
                "P1",
                "routing",
                "Child Git repositories lack explicit AGENTS.md routes: "
                + ", ".join(unrouted_children),
                "AGENTS.md" if agents_exists else None,
            )
        )

    codex_metrics = _codex_chain_metrics(root, project_instruction_paths)
    if (
        codex_metrics["worst_known_chain"]["combined_bytes"]
        > codex_metrics["default_max_bytes"]
    ):
        issues.append(
            _issue(
                "P1",
                "context-budget",
                "Worst known Codex instruction chain exceeds the default 32 KiB project_doc_max_bytes limit",
                codex_metrics["worst_known_chain"]["target_directory"],
            )
        )

    for report in [*config_reports, *mcp_reports]:
        for message in report.issues:
            issues.append(
                _issue(
                    "P1" if not report.valid else "P2",
                    "configuration",
                    message,
                    report.path,
                )
            )
    for report in skill_reports:
        for message in report.issues:
            issues.append(_issue("P2", "skills", message, report.path))
    for report in subagent_reports:
        for message in report.issues:
            issues.append(_issue("P2", "subagents", message, report.path))

    if file_count > 3000:
        recommendations.append(
            _issue(
                "P1",
                "scale",
                f"Repository has {file_count} files; prioritize routing and retrieval/context-engine support",
            )
        )

    issues.sort(
        key=lambda item: (
            PRIORITY_ORDER[item["priority"]],
            item["category"],
            item.get("file", ""),
        )
    )
    recommendations.sort(
        key=lambda item: (
            PRIORITY_ORDER[item["priority"]],
            item["category"],
            item.get("file", ""),
        )
    )

    return {
        "meta": {
            "tool": "agentic-readiness.audit_repo",
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "root": str(root),
            "user_scope_included": include_user_scope,
            "secret_values_reported": False,
        },
        "repository": {
            "is_git_repo": _is_git_repo(root),
            "tracked_file_count": len(tracked_list)
            if tracked_list is not None
            else None,
            "file_count": file_count,
            "is_large_repo": file_count > 3000,
            "top_level_directories": _directory_stats(root, tracked_list),
            "child_git_repositories": child_repos,
        },
        "instruction_topology": {
            "canonical_agents_md": agents_exists,
            "claude_compatibility_file": claude_exists,
            "files": [asdict(report) for report in instruction_reports],
            "nested_agents_files": nested_agents,
            "unindexed_nested_agents_files": unindexed_nested,
            "has_general_chain_invariant": has_chain_invariant,
            "unrouted_child_git_repositories": unrouted_children,
            "codex_project_chains": codex_metrics,
            "discovery_note": "Codex builds the chain once per run/session; changing command cwd does not reload child or nested instructions.",
        },
        "agent_configuration": [asdict(report) for report in config_reports],
        "mcp_configuration": [asdict(report) for report in mcp_reports],
        "skills": {
            "total_count": len(skill_reports),
            "discovered": [asdict(report) for report in skill_reports],
        },
        "subagents": {
            "total_count": len(subagent_reports),
            "discovered": [asdict(report) for report in subagent_reports],
        },
        "issues": issues,
        "recommendations": recommendations,
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit repository readiness for Codex, Claude Code, and OpenCode"
    )
    parser.add_argument("--root", default=".", help="Repository root directory")
    parser.add_argument(
        "--include-user-scope",
        action="store_true",
        help="Include metadata from known user-scope instruction and config paths; secret values are never reported",
    )
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists() or not root.is_dir():
        print(
            f"Error: repository root does not exist or is not a directory: {root}",
            file=sys.stderr,
        )
        return 1
    print(
        json.dumps(
            audit(root, include_user_scope=args.include_user_scope),
            indent=2,
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
