#!/usr/bin/env python3
"""
Repo Activity Summary — extract structured engineering signals from git history.

Runs entirely against the local git log. No API keys, no network access.
Originally derived from an independent git-signal-extraction tool; maintained
here as a stdlib-only Agent Skill.

Usage:
    python3 activity_summary.py --repo-dir /path/to/repo --days 90
    python3 activity_summary.py --repo-dir . --days 30 --author "alice" --format json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List, Optional, Tuple

__version__ = "1.1.0"

# ---------------------------------------------------------------------------
# Technology detection
# Patterns are classified by kind — never matched as bare substrings of a path.
# ---------------------------------------------------------------------------

# Source-file extensions (matched via os.path.splitext on the basename).
TECH_EXTENSIONS: Dict[str, List[str]] = {
    "Python": [".py"],
    "JavaScript": [".js", ".jsx", ".mjs", ".cjs"],
    "TypeScript": [".ts", ".tsx"],
    "React": [".jsx", ".tsx"],
    "Vue": [".vue"],
    "Svelte": [".svelte"],
    "Rust": [".rs"],
    "Go": [".go"],
    "Java": [".java"],
    "Kotlin": [".kt", ".kts"],
    "Swift": [".swift"],
    "C#": [".cs", ".csproj", ".sln"],
    "C/C++": [".c", ".cpp", ".h", ".hpp", ".cc", ".cxx"],
    "Ruby": [".rb"],
    "PHP": [".php"],
    "Elixir": [".ex", ".exs"],
    "Scala": [".scala"],
    "Terraform": [".tf"],
    "SQL": [".sql"],
    "GraphQL": [".graphql", ".gql"],
    "CSS": [".css", ".scss", ".sass", ".less"],
}

# Exact basenames (config / manifest files). A single hit is enough evidence.
TECH_MANIFESTS: Dict[str, List[str]] = {
    "Python": ["requirements.txt", "setup.py", "pyproject.toml", "pipfile"],
    "JavaScript": ["package.json"],
    "TypeScript": ["tsconfig.json"],
    "React": ["next.config.js", "next.config.mjs", "next.config.ts", "next.config.cjs"],
    "Vue": ["vue.config.js", "vue.config.ts", "nuxt.config.js", "nuxt.config.ts"],
    "Svelte": ["svelte.config.js", "svelte.config.ts"],
    "Rust": ["cargo.toml"],
    "Go": ["go.mod", "go.sum"],
    "Java": ["pom.xml", "build.gradle", "build.gradle.kts"],
    "Swift": ["package.swift"],
    "C/C++": ["cmakelists.txt", "makefile"],
    "Ruby": ["gemfile", "rakefile"],
    "PHP": ["composer.json"],
    "Elixir": ["mix.exs"],
    "Scala": ["build.sbt"],
    "Docker": ["dockerfile", "docker-compose.yml", "docker-compose.yaml", ".dockerignore"],
    "Kubernetes": ["kustomization.yaml", "kustomization.yml", "chart.yaml"],
    "Terraform": ["terraform.tf", "main.tf", "versions.tf"],
    "CSS": ["tailwind.config.js", "tailwind.config.ts", "tailwind.config.cjs"],
    "CI/CD": ["jenkinsfile", ".gitlab-ci.yml", ".travis.yml"],
}

# Path-segment matches (compared to individual path components, lowercased).
TECH_PATH_SEGMENTS: Dict[str, List[str]] = {
    "Kubernetes": ["k8s", "helm", "charts"],
    "Terraform": ["terraform"],
    "SQL": ["migrations", "prisma", "drizzle"],
    "Docker": ["docker"],
    "CI/CD": [".github", ".circleci", ".gitlab"],
}

# Minimum distinct source-file hits (by extension) required to claim a tech
# when no manifest/config file was seen. Prevents fixture-only false positives.
TECH_SOURCE_FILE_THRESHOLD = 2

# ---------------------------------------------------------------------------
# Work type classification from commit messages
# ---------------------------------------------------------------------------

# Multi-word phrases first where needed; all matched with word boundaries.
WORK_TYPE_PATTERNS: Dict[str, List[str]] = {
    "feature": [
        "feat", "feature", "implement", "introduce",
        r"add(?:s|ed|ing)?", r"create[sd]?", r"new\s+feature",
        r"support\s+for",
    ],
    "bugfix": [
        "fix", "bugfix", "bug", "patch", "hotfix", "resolve", "correct", "repair",
    ],
    "refactor": [
        "refactor", "rename", "cleanup", r"clean\s*up", "improve",
        "reorganize", "restructure", "simplify",
    ],
    "docs": [
        "docs", "readme", "documentation", "jsdoc", "docstring",
        r"document(?:s|ed|ing|ation)?",
    ],
    "testing": [
        "test", "tests", "coverage", "jest", "pytest", "e2e", "vitest",
        r"\bspec\b",
    ],
    "infrastructure": [
        "config", "deploy", "docker", "infra", "devops",
        r"\bci\b", r"\bcd\b", r"\benv\b", r"\bbuild\b",
    ],
    "ui": [
        r"\bui\b", "stylesheet", r"\bcss\b", "layout", "responsive",
        r"\bstyle\b", r"\bdesign\b",
    ],
    "performance": [
        "perf", "performance", "speed", "cache", "optimize", "lazy", "memo", "latency",
    ],
    "security": [
        "security", "vulnerability", "sanitize", "encrypt",
        r"\bauth\b", r"\bvalidate\b",
    ],
    "release": [
        "release", r"bump\s+version", "changelog", r"\brc\d*\b",
        r"v?\d+\.\d+\.\d+", r"version\s+\d+",
    ],
}

# Deterministic tie-break when scores are equal (more specific first).
WORK_TYPE_TIEBREAK: List[str] = [
    "security",
    "release",
    "bugfix",
    "performance",
    "testing",
    "docs",
    "feature",
    "refactor",
    "infrastructure",
    "ui",
]


def _compile_work_type_regexes() -> Dict[str, List[re.Pattern[str]]]:
    compiled: Dict[str, List[re.Pattern[str]]] = {}
    for work_type, patterns in WORK_TYPE_PATTERNS.items():
        regs: List[re.Pattern[str]] = []
        for p in patterns:
            # Patterns may already include regex metacharacters; wrap with
            # word-boundary anchors only when the pattern does not start/end
            # with an explicit boundary or quantifier group edge.
            if p.startswith(r"\b") or p.startswith(r"(?"):
                body = p
            else:
                body = rf"\b(?:{p})\b"
            regs.append(re.compile(body, re.IGNORECASE))
        compiled[work_type] = regs
    return compiled


WORK_TYPE_REGEXES: Dict[str, List[re.Pattern[str]]] = _compile_work_type_regexes()

# True no-signal messages only — do not drop real work ("fix", "test", …).
NOISE_MESSAGES = {
    ".",
    "wip",
    "work in progress",
    "asdf",
    "asd",
    "stuff",
    "temp",
    "foo",
    "bar",
    "xxx",
    "tmp",
}

# Bot detection: GitHub-style markers and known automation identities.
# Never match a bare "bot" substring inside a human name.
_BOT_NAME_END = re.compile(r"\[bot\]\s*$", re.IGNORECASE)
_BOT_KNOWN_NAME = re.compile(
    r"(?i)\b("
    r"dependabot(\[bot\])?"
    r"|renovate(\[bot\])?"
    r"|github-actions(\[bot\])?"
    r"|semantic-release"
    r"|snyk-bot"
    r"|greenkeeper"
    r"|deepsource"
    r")\b"
)
_BOT_EMAIL_LOCALS = re.compile(
    r"(?i)^(dependabot|renovate|github-actions|semantic-release|snyk-bot|greenkeeper|deepsource)(\[bot\])?@"
)

# Files that indicate noise, not real engineering work
NOISE_FILE_HINTS = [
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "Pipfile.lock",
    "poetry.lock", "Cargo.lock", "go.sum", "Gemfile.lock", "composer.lock",
    ".min.", ".map", "dist/", "build/", ".next/", "node_modules/",
    "vendor/", "__pycache__/", ".generated.", ".auto.",
]

# Test-module detection (basename / path-segment conventions)
TEST_DIR_SEGMENTS = frozenset({"tests", "__tests__", "spec", "test"})
FIXTURE_DIR_SEGMENTS = frozenset({
    "fixtures", "fixture", "cassettes", "cassette", "vcr_cassettes",
    "testdata", "test-data", "test_data", "__snapshots__", "snapshots",
    "golden", "goldens", "__fixtures__",
})
_TEST_BASENAME_RE = re.compile(
    r"(?i)^("
    r"test_.*\.py"
    r"|.*_test\.py"
    r"|.*_test\.go"
    r"|test_.*\.go"
    r"|.*\.test\.[jt]sx?"
    r"|.*\.spec\.[jt]sx?"
    r"|.*_spec\.rb"
    r"|.*\.spec\.rb"
    r"|test_.*\.rs"
    r"|.*_test\.rs"
    r")$"
)

# git numstat rename forms: "old => new" or "prefix{old => new}suffix"
_RENAME_BRACE_RE = re.compile(r"\{([^{}]*) => ([^{}]*)\}")


# ---------------------------------------------------------------------------
# Git log parsing
# ---------------------------------------------------------------------------

def run_git(args: List[str], repo_dir: str) -> str:
    result = subprocess.run(
        ["git"] + args,
        cwd=repo_dir,
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def ensure_git_repo(repo_dir: str) -> str:
    """Resolve repo_dir and verify it is inside a git work tree.

    Returns the absolute path. Raises RuntimeError with a one-line message
    on any failure (missing path, not a git repo, etc.).
    """
    if repo_dir.startswith("-"):
        raise RuntimeError(
            f"Invalid --repo-dir {repo_dir!r}: values must not start with '-'."
        )
    abs_dir = os.path.abspath(repo_dir)
    if not os.path.isdir(abs_dir):
        raise RuntimeError(f"Repository path does not exist or is not a directory: {abs_dir}")
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=abs_dir,
            capture_output=True,
            text=True,
            timeout=30,
        )
    except FileNotFoundError as exc:
        raise RuntimeError(f"git is not available: {exc}") from exc
    if result.returncode != 0 or result.stdout.strip() != "true":
        err = (result.stderr or result.stdout or "not a git repository").strip()
        raise RuntimeError(f"Not a git work tree: {abs_dir} ({err})")
    return abs_dir


def resolve_numstat_path(filepath: str) -> str:
    """Resolve git --numstat rename forms to the destination path.

    Handles:
      - ``old/path => new/path``
      - ``{old => new}/file``
      - ``dir/{old => new}``
      - ``dir/{old => new}/file``
    """
    if " => " not in filepath:
        return filepath
    if "{" in filepath and "}" in filepath:
        return _RENAME_BRACE_RE.sub(r"\2", filepath)
    # Simple whole-path rename
    return filepath.split(" => ", 1)[1]


def parse_git_log(
    repo_dir: str,
    days: int,
    author: Optional[str],
    max_commits: int,
    branch: Optional[str],
) -> List[Dict[str, Any]]:
    """Parse git log with --numstat into structured commit dicts."""
    # Explicit UTC offset so git does not reinterpret the window in local time.
    since_dt = datetime.now(timezone.utc) - timedelta(days=days)
    since = since_dt.strftime("%Y-%m-%dT%H:%M:%S+00:00")

    cmd = [
        "log",
        f"--since={since}",
        f"--max-count={max_commits}",
        "--format=COMMIT_SEP%n%H%n%an%n%ae%n%aI%n%s",
        "--numstat",
        "--no-merges",
        "--no-renames",
    ]
    if author:
        cmd.append(f"--author={author}")
    # Prevent option injection: reject dash-leading revisions. Append the
    # revision as a positional arg (NOT after bare `--`, which would make git
    # treat it as a pathspec), then end with `--` so nothing following can be
    # reinterpreted as a revision or option.
    if branch:
        if branch.startswith("-"):
            raise RuntimeError(
                f"Invalid --branch {branch!r}: values must not start with '-'."
            )
        cmd.append(branch)
        cmd.append("--")

    raw = run_git(cmd, repo_dir)
    if not raw.strip():
        return []

    commits = []
    for block in raw.split("COMMIT_SEP\n"):
        block = block.strip()
        if not block:
            continue

        lines = block.split("\n")
        if len(lines) < 5:
            continue

        sha = lines[0].strip()
        author_name = lines[1].strip()
        author_email = lines[2].strip()
        date_str = lines[3].strip()
        message = lines[4].strip()

        try:
            committed_at = datetime.fromisoformat(date_str)
        except ValueError:
            continue

        files = []
        insertions = 0
        deletions = 0
        for stat_line in lines[5:]:
            stat_line = stat_line.strip()
            if not stat_line:
                continue
            parts = stat_line.split("\t")
            if len(parts) != 3:
                continue
            add_str, del_str, filepath = parts
            filepath = resolve_numstat_path(filepath)
            try:
                add = int(add_str) if add_str != "-" else 0
                rem = int(del_str) if del_str != "-" else 0
            except ValueError:
                continue
            insertions += add
            deletions += rem
            files.append({"path": filepath, "additions": add, "deletions": rem})

        commits.append({
            "sha": sha,
            "author": author_name,
            "email": author_email,
            "date": committed_at,
            "message": message,
            "files": files,
            "insertions": insertions,
            "deletions": deletions,
        })

    return commits


# ---------------------------------------------------------------------------
# Filtering
# ---------------------------------------------------------------------------

def is_bot_author(author: str, email: str = "") -> bool:
    """Return True if the author looks like automation, not a human.

    Matches GitHub-style ``Name[bot]`` suffixes and known bot identities.
    Does **not** match the bare substring ``bot`` inside human names
    (e.g. Talbot Smith, Abbott, Robert Botha, Ida Bothe).
    """
    if not author and not email:
        return False
    name = author.strip()
    if _BOT_NAME_END.search(name):
        return True
    if _BOT_KNOWN_NAME.search(name):
        return True
    if email:
        email_l = email.strip().lower()
        if _BOT_EMAIL_LOCALS.search(email_l):
            return True
        # users.noreply.github.com only counts as bot when the name is marked [bot]
        if email_l.endswith("@users.noreply.github.com") and _BOT_NAME_END.search(name):
            return True
    return False


def is_noise_message(message: str) -> bool:
    return message.lower().strip().rstrip(".") in NOISE_MESSAGES or message.strip() in NOISE_MESSAGES


def is_noise_file(filepath: str) -> bool:
    lower = filepath.lower().replace("\\", "/")
    return any(hint.lower() in lower for hint in NOISE_FILE_HINTS)


def filter_commits(commits: List[Dict]) -> Tuple[List[Dict], int]:
    """Filter out bot commits. Returns (filtered, skipped_bot_count)."""
    filtered = []
    skipped = 0
    for commit in commits:
        if is_bot_author(commit["author"], commit.get("email", "")):
            skipped += 1
            continue
        filtered.append(commit)
    return filtered, skipped


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def _path_components(path: str) -> List[str]:
    return [p for p in path.replace("\\", "/").split("/") if p]


def detect_technologies(commits_or_paths: Any) -> List[str]:
    """Detect technologies from file paths using typed pattern matching.

    Matching rules (no bare substring over the full path):
      - extension: ``os.path.splitext(basename)`` / endswith on basename
      - exact filename: compare against ``os.path.basename`` (case-insensitive)
      - path segment: compare against individual ``path.split('/')`` components

    A technology is reported if a manifest/config file hits, **or** at least
    ``TECH_SOURCE_FILE_THRESHOLD`` distinct source files match by extension.

    Accepts either a list of commit dicts (each with a ``files`` list) or a
    plain list of path strings (convenient for unit tests).
    """
    # tech -> set of distinct source paths matched by extension
    source_hits: Dict[str, set] = defaultdict(set)
    # tech -> True if a manifest/config was seen
    manifest_hits: Dict[str, bool] = defaultdict(bool)

    all_paths: List[str] = []
    if commits_or_paths and isinstance(commits_or_paths[0], str):
        all_paths = list(commits_or_paths)
    else:
        for commit in commits_or_paths or []:
            for f in commit.get("files", []):
                all_paths.append(f["path"])

    for path in all_paths:
        norm = path.replace("\\", "/")
        basename = os.path.basename(norm)
        basename_l = basename.lower()
        _stem, ext = os.path.splitext(basename)
        ext_l = ext.lower()
        segments = [s.lower() for s in _path_components(norm)]

        for tech, extensions in TECH_EXTENSIONS.items():
            if ext_l and ext_l in extensions:
                source_hits[tech].add(norm)
            # also allow endswith for multi-dot extensions listed fully
            elif any(basename_l.endswith(e.lower()) for e in extensions if e.count(".") > 1):
                source_hits[tech].add(norm)

        for tech, manifests in TECH_MANIFESTS.items():
            if basename_l in {m.lower() for m in manifests}:
                manifest_hits[tech] = True

        for tech, segs in TECH_PATH_SEGMENTS.items():
            if any(s in segments for s in segs):
                # Path-segment evidence counts as a config/structural hit
                # (directory layout), not a single source file.
                manifest_hits[tech] = True

    techs = set()
    all_tech_names = (
        set(TECH_EXTENSIONS) | set(TECH_MANIFESTS) | set(TECH_PATH_SEGMENTS)
    )
    for tech in all_tech_names:
        if manifest_hits.get(tech):
            techs.add(tech)
        elif len(source_hits.get(tech, ())) >= TECH_SOURCE_FILE_THRESHOLD:
            techs.add(tech)
    return sorted(techs)


def classify_commit_message(message: str) -> Optional[str]:
    """Classify a single commit subject into a work type, or None.

    Uses precompiled word-boundary regexes, scores every category, and breaks
    ties via ``WORK_TYPE_TIEBREAK`` (then alphabetical) for determinism.
    """
    if not message or not message.strip():
        return None
    scores: Dict[str, int] = {}
    for work_type, regexes in WORK_TYPE_REGEXES.items():
        score = sum(1 for r in regexes if r.search(message))
        if score:
            scores[work_type] = score
    if not scores:
        return None
    max_score = max(scores.values())
    candidates = [wt for wt, s in scores.items() if s == max_score]
    if len(candidates) == 1:
        return candidates[0]
    for preferred in WORK_TYPE_TIEBREAK:
        if preferred in candidates:
            return preferred
    return sorted(candidates)[0]


def classify_work_types(
    commits: List[Dict],
) -> Tuple[Dict[str, int], List[Dict[str, str]]]:
    """Classify commits by work type. Returns (counts, unclassified_samples).

    Each unclassified sample is ``{sha, date, subject}``.
    """
    counts: Dict[str, int] = defaultdict(int)
    unclassified: List[Dict[str, str]] = []
    for commit in commits:
        label = classify_commit_message(commit["message"])
        if label is None:
            counts["other"] += 1
            date_val = commit["date"]
            date_str = date_val.isoformat() if hasattr(date_val, "isoformat") else str(date_val)
            unclassified.append({
                "sha": commit.get("sha", "")[:12],
                "date": date_str[:10] if date_str else "",
                "subject": commit["message"],
            })
        else:
            counts[label] += 1
    if counts.get("other") == 0:
        counts.pop("other", None)
    ordered = dict(sorted(counts.items(), key=lambda x: -x[1]))
    return ordered, unclassified


def compute_churn_hotspots(commits: List[Dict], top_n: int = 10) -> List[Dict]:
    """Find the most frequently modified files (noise files excluded)."""
    file_stats: Dict[str, Dict] = defaultdict(lambda: {
        "modifications": 0, "additions": 0, "deletions": 0,
    })
    for commit in commits:
        for f in commit["files"]:
            path = f["path"]
            if is_noise_file(path):
                continue
            file_stats[path]["modifications"] += 1
            file_stats[path]["additions"] += f["additions"]
            file_stats[path]["deletions"] += f["deletions"]

    ranked = sorted(file_stats.items(), key=lambda x: -x[1]["modifications"])
    return [
        {"path": path, **stats}
        for path, stats in ranked[:top_n]
    ]


def compute_directory_hotspots(commits: List[Dict], top_n: int = 8) -> List[Dict]:
    """Aggregate churn to top-level directories (noise files excluded)."""
    dir_stats: Dict[str, Dict] = defaultdict(lambda: {
        "modifications": 0, "additions": 0, "deletions": 0, "files": set(),
    })
    for commit in commits:
        for f in commit["files"]:
            path = f["path"]
            if is_noise_file(path):
                continue
            parts = path.replace("\\", "/").split("/")
            directory = parts[0] if len(parts) > 1 else "."
            dir_stats[directory]["modifications"] += 1
            dir_stats[directory]["additions"] += f["additions"]
            dir_stats[directory]["deletions"] += f["deletions"]
            dir_stats[directory]["files"].add(path)

    ranked = sorted(dir_stats.items(), key=lambda x: -x[1]["modifications"])
    return [
        {
            "directory": d,
            "modifications": stats["modifications"],
            "additions": stats["additions"],
            "deletions": stats["deletions"],
            "unique_files": len(stats["files"]),
        }
        for d, stats in ranked[:top_n]
    ]


def analyze_contributors(commits: List[Dict]) -> List[Dict]:
    """Per-author contribution stats with primary work focus."""
    author_stats: Dict[str, Dict] = defaultdict(lambda: {
        "commits": 0, "additions": 0, "deletions": 0,
        "work_types": Counter(), "first_commit": None, "last_commit": None,
    })

    for commit in commits:
        name = commit["author"]
        stats = author_stats[name]
        stats["commits"] += 1
        stats["additions"] += commit["insertions"]
        stats["deletions"] += commit["deletions"]

        label = classify_commit_message(commit["message"])
        if label:
            stats["work_types"][label] += 1

        d = commit["date"]
        if stats["first_commit"] is None or d < stats["first_commit"]:
            stats["first_commit"] = d
        if stats["last_commit"] is None or d > stats["last_commit"]:
            stats["last_commit"] = d

    result = []
    for name, stats in sorted(author_stats.items(), key=lambda x: -x[1]["commits"]):
        top_types = [t for t, _ in stats["work_types"].most_common(2)]
        result.append({
            "author": name,
            "commits": stats["commits"],
            "additions": stats["additions"],
            "deletions": stats["deletions"],
            "primary_focus": top_types if top_types else ["general"],
        })
    return result


def _commit_changes_excluding_noise(commit: Dict) -> int:
    """Lines changed in a commit, excluding lockfiles / generated paths."""
    total = 0
    for f in commit.get("files", []):
        if is_noise_file(f["path"]):
            continue
        total += f["additions"] + f["deletions"]
    return total


def compute_velocity(commits: List[Dict], days: int) -> Dict[str, Any]:
    """Compute velocity indicators.

    ``avg_commit_size`` excludes noise files (lockfiles, build output) — the
    same filter used by churn hotspots.
    """
    if not commits:
        return {
            "commits_per_week": 0,
            "active_days": 0,
            "avg_commit_size": 0,
            "noise_files_excluded": True,
        }

    dates = {c["date"].date() for c in commits}
    active_days = len(dates)
    total_changes = sum(_commit_changes_excluding_noise(c) for c in commits)
    weeks = max(days / 7, 1)

    return {
        "commits_per_week": round(len(commits) / weeks, 1),
        "active_days": active_days,
        "active_day_ratio": round(active_days / max(days, 1), 2),
        "avg_commit_size": round(total_changes / len(commits)) if commits else 0,
        "noise_files_excluded": True,
    }


def is_test_module(path: str) -> bool:
    """True if path looks like a real test module (not a fixture/cassette).

    Counts files whose basename matches common test conventions, or that live
    under a ``tests/`` / ``__tests__/`` / ``spec/`` path segment — excluding
    fixture and cassette directories.
    """
    norm = path.replace("\\", "/")
    parts = _path_components(norm)
    if not parts:
        return False
    lower_parts = [p.lower() for p in parts]
    # Exclude fixture/cassette directories entirely
    if any(p in FIXTURE_DIR_SEGMENTS for p in lower_parts):
        return False
    basename = parts[-1]
    if _TEST_BASENAME_RE.match(basename):
        return True
    # Files directly under a test directory (not fixtures) with a code extension
    parent_segs = lower_parts[:-1]
    if any(p in TEST_DIR_SEGMENTS for p in parent_segs):
        _stem, ext = os.path.splitext(basename)
        if ext.lower() in {
            ".py", ".go", ".js", ".jsx", ".ts", ".tsx", ".rb", ".rs",
            ".java", ".kt", ".php", ".cs",
        }:
            # Skip obvious non-module support files
            name_l = basename.lower()
            if name_l in {"conftest.py", "__init__.py"}:
                return name_l == "conftest.py"
            return True
    return False


def assess_project_health(commits: List[Dict], repo_dir: str) -> Dict[str, Any]:
    """Check for tests, CI, docs, and recency."""
    all_files = set()
    for commit in commits:
        for f in commit["files"]:
            all_files.add(f["path"])

    try:
        tree_files = run_git(["ls-files"], repo_dir).strip().split("\n")
        tree_files = [f for f in tree_files if f]
    except RuntimeError:
        tree_files = []

    combined = all_files | set(tree_files)
    combined_list = list(combined)
    combined_lower = {f.lower().replace("\\", "/") for f in combined}

    test_module_count = sum(1 for f in combined_list if is_test_module(f))
    has_tests = test_module_count > 0

    has_ci = any(
        "/.github/workflows/" in f or f.startswith(".github/workflows/")
        or "/.gitlab-ci" in f or f.startswith(".gitlab-ci")
        or f.endswith("jenkinsfile") or f == "jenkinsfile"
        or "/.circleci/" in f or f.startswith(".circleci/")
        for f in combined_lower
    )

    has_docs = any(
        f.endswith("readme.md") or f.startswith("docs/") or "/docs/" in f
        or f.endswith(".rst")
        for f in combined_lower
    )

    last_commit_date = max((c["date"] for c in commits), default=None)
    days_since_last = None
    if last_commit_date:
        now = datetime.now(timezone.utc)
        if last_commit_date.tzinfo is None:
            last_commit_date = last_commit_date.replace(tzinfo=timezone.utc)
        days_since_last = (now - last_commit_date).days

    return {
        "has_tests": has_tests,
        "test_module_count": test_module_count,
        "has_ci": has_ci,
        "has_docs": has_docs,
        "days_since_last_commit": days_since_last,
    }


# ---------------------------------------------------------------------------
# Full analysis
# ---------------------------------------------------------------------------

def analyze(
    repo_dir: str,
    days: int = 90,
    author: Optional[str] = None,
    max_commits: int = 500,
    branch: Optional[str] = None,
    classify_threshold: float = 0.25,
    max_unclassified_samples: int = 40,
    raw_subjects: bool = False,
) -> Dict[str, Any]:
    """Run the full analysis pipeline and return structured results."""
    repo_dir = ensure_git_repo(repo_dir)

    try:
        remote = run_git(["remote", "get-url", "origin"], repo_dir).strip()
        repo_name = remote.rstrip("/").split("/")[-1]
        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]
    except RuntimeError:
        repo_name = os.path.basename(repo_dir)

    raw_commits = parse_git_log(repo_dir, days, author, max_commits, branch)
    commits, skipped = filter_commits(raw_commits)

    if not commits:
        return {
            "repo": repo_name,
            "period_days": days,
            "author_filter": author,
            "total_commits": 0,
            "message": "No commits found in the specified period.",
        }

    dates = [c["date"] for c in commits]
    total_additions = sum(c["insertions"] for c in commits)
    total_deletions = sum(c["deletions"] for c in commits)
    unique_authors = len({c["author"] for c in commits})

    # Filter out noise-only commits for work type analysis
    meaningful = [c for c in commits if not is_noise_message(c["message"])]
    work_types, unclassified_samples = (
        classify_work_types(meaningful) if meaningful else ({}, [])
    )

    total_classified = sum(work_types.values()) if work_types else 0
    other_count = work_types.get("other", 0)
    other_share = (other_count / total_classified) if total_classified else 0.0
    classification_unreliable = other_share > classify_threshold

    result: Dict[str, Any] = {
        "repo": repo_name,
        "period_days": days,
        "author_filter": author,
        "total_commits": len(commits),
        "skipped_bot_commits": skipped,
        "unique_authors": unique_authors,
        "date_range": {
            "start": min(dates).isoformat(),
            "end": max(dates).isoformat(),
        },
        "lines": {
            "additions": total_additions,
            "deletions": total_deletions,
            "net": total_additions - total_deletions,
        },
        "technologies": detect_technologies(commits),
        "work_types": work_types,
        "classification": {
            "threshold": classify_threshold,
            "other_share": round(other_share, 4),
            "unreliable": classification_unreliable,
            "unclassified_count": other_count,
            "note": (
                "Work-type labels are keyword heuristics. When the unclassified "
                "share exceeds the threshold, prefer classifying from the emitted "
                "subjects rather than trusting the keyword breakdown."
                if classification_unreliable
                else "Work-type labels are keyword heuristics, not ground truth."
            ),
        },
        "churn_hotspots": compute_churn_hotspots(commits),
        "directory_hotspots": compute_directory_hotspots(commits),
        "contributors": analyze_contributors(commits),
        "velocity": compute_velocity(commits, days),
        "project_health": assess_project_health(commits, repo_dir),
        "noise_filter": {
            "applied_to": ["churn_hotspots", "directory_hotspots", "velocity.avg_commit_size"],
            "description": (
                "Lockfiles, minified assets, and common generated/vendor paths "
                "are excluded from churn and average commit size."
            ),
        },
    }

    if classification_unreliable or other_count:
        result["unclassified_samples"] = unclassified_samples[:max_unclassified_samples]
        result["unclassified_samples_truncated"] = (
            len(unclassified_samples) > max_unclassified_samples
        )

    if raw_subjects:
        result["raw_subjects"] = [
            {
                "sha": c["sha"][:12],
                "date": (
                    c["date"].isoformat()[:10]
                    if hasattr(c["date"], "isoformat")
                    else str(c["date"])[:10]
                ),
                "subject": c["message"],
            }
            for c in commits
        ]

    return result


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def _status_glyph(ok: bool) -> str:
    """Return a status glyph, with ASCII fallback when stdout is not UTF-8."""
    try:
        encoding = getattr(sys.stdout, "encoding", None) or "utf-8"
        "✓".encode(encoding)
        return "✓" if ok else "✗"
    except (UnicodeEncodeError, LookupError):
        return "OK" if ok else "NO"


def format_markdown(data: Dict[str, Any]) -> str:
    """Render analysis as a readable markdown report."""
    if data.get("total_commits", 0) == 0:
        return (
            f"## Repo Activity Summary — {data['repo']}\n\n"
            f"No commits found in the last {data['period_days']} days."
        )

    lines = []
    period = f"last {data['period_days']} days"
    author_note = f" (author: {data['author_filter']})" if data.get("author_filter") else ""
    lines.append(f"## Repo Activity Summary — {data['repo']} ({period}){author_note}\n")

    # Overview
    dr = data["date_range"]
    start = dr["start"][:10]
    end = dr["end"][:10]
    lines.append("### Overview")
    lines.append(
        f"- **{data['total_commits']}** commits by **{data['unique_authors']}** contributor(s)"
    )
    lines.append(
        f"- **{data['lines']['additions']:,}** lines added, "
        f"**{data['lines']['deletions']:,}** deleted (net {data['lines']['net']:+,})"
    )
    lines.append(f"- Date range: {start} → {end}")
    if data.get("skipped_bot_commits"):
        lines.append(f"- {data['skipped_bot_commits']} bot commits filtered out")
    lines.append("")

    # Technologies
    if data.get("technologies"):
        lines.append("### Technologies")
        lines.append(", ".join(data["technologies"]))
        lines.append("")
        lines.append(
            "_Heuristic from file extensions, manifests, and path segments — not imports._"
        )
        lines.append("")

    # Work types
    if data.get("work_types"):
        lines.append("### Work Type Breakdown")
        clf = data.get("classification") or {}
        if clf.get("unreliable"):
            lines.append(
                f"**Classification unreliable:** {clf.get('unclassified_count', 0)} of "
                f"{sum(data['work_types'].values())} meaningful commits "
                f"({round(100 * clf.get('other_share', 0))}%) fell into "
                f"`other` (threshold {round(100 * clf.get('threshold', 0.25))}%). "
                "Keyword labels below are weak signals — classify from the "
                "unclassified subjects (or re-run with `--raw-subjects`) instead."
            )
            lines.append("")
        total = sum(data["work_types"].values())
        for wt, count in data["work_types"].items():
            pct = round(100 * count / total) if total else 0
            lines.append(f"- {wt.capitalize()}: {pct}% ({count} commits)")
        lines.append("")

    # Unclassified subjects for the agent to interpret
    if data.get("unclassified_samples") and (data.get("classification") or {}).get("unreliable"):
        lines.append("### Unclassified Commit Subjects")
        lines.append(
            "Keyword classifier could not label these; the calling agent should "
            "classify them from the subjects themselves:"
        )
        lines.append("")
        for sample in data["unclassified_samples"]:
            lines.append(
                f"- `{sample.get('sha', '')}` ({sample.get('date', '')}) "
                f"{sample.get('subject', '')}"
            )
        if data.get("unclassified_samples_truncated"):
            lines.append("")
            lines.append(
                f"_Sample capped; re-run with a higher "
                f"`--max-unclassified-samples` or use `--raw-subjects`._"
            )
        lines.append("")

    # Raw subjects (optional)
    if data.get("raw_subjects"):
        lines.append("### Raw Commit Subjects")
        for sample in data["raw_subjects"]:
            lines.append(
                f"- `{sample.get('sha', '')}` ({sample.get('date', '')}) "
                f"{sample.get('subject', '')}"
            )
        lines.append("")

    # Churn hotspots
    if data.get("churn_hotspots"):
        lines.append("### Churn Hotspots")
        lines.append("_Lockfiles and generated paths excluded._")
        for i, h in enumerate(data["churn_hotspots"], 1):
            lines.append(
                f"{i}. `{h['path']}` — {h['modifications']} modifications, "
                f"+{h['additions']}/-{h['deletions']}"
            )
        lines.append("")

    # Directory hotspots
    if data.get("directory_hotspots"):
        lines.append("### Directory Activity")
        lines.append("_Lockfiles and generated paths excluded._")
        for dh in data["directory_hotspots"]:
            lines.append(
                f"- `{dh['directory']}/` — {dh['modifications']} changes across "
                f"{dh['unique_files']} files"
            )
        lines.append("")

    # Contributors
    if data.get("contributors"):
        lines.append("### Contributors")
        lines.append("| Author | Commits | Lines +/- | Primary Focus |")
        lines.append("|--------|---------|-----------|---------------|")
        for c in data["contributors"]:
            focus = ", ".join(c["primary_focus"])
            lines.append(
                f"| {c['author']} | {c['commits']} | "
                f"+{c['additions']:,}/-{c['deletions']:,} | {focus} |"
            )
        lines.append("")

    # Velocity
    if data.get("velocity"):
        v = data["velocity"]
        lines.append("### Velocity")
        lines.append(f"- {v['commits_per_week']} commits/week")
        lines.append(
            f"- {v['active_days']} active days "
            f"({round(v.get('active_day_ratio', 0) * 100)}% of period)"
        )
        noise_note = (
            " (lockfiles/generated paths excluded)"
            if v.get("noise_files_excluded")
            else ""
        )
        lines.append(
            f"- Average commit size: {v['avg_commit_size']:,} lines changed{noise_note}"
        )
        lines.append("")

    # Project health
    if data.get("project_health"):
        ph = data["project_health"]
        lines.append("### Project Health")
        yes, no = _status_glyph(True), _status_glyph(False)
        test_count = ph.get("test_module_count", ph.get("test_file_count", 0))
        test_detail = (
            f" ({test_count} test modules by basename/path convention)"
            if test_count
            else ""
        )
        lines.append(
            f"- {yes if ph['has_tests'] else no} Tests "
            f"{'present' if ph['has_tests'] else 'not detected'}{test_detail}"
        )
        lines.append(
            f"- {yes if ph['has_ci'] else no} CI "
            f"{'configured' if ph['has_ci'] else 'not detected'}"
        )
        lines.append(
            f"- {yes if ph['has_docs'] else no} Documentation "
            f"{'exists' if ph['has_docs'] else 'not detected'}"
        )
        if ph.get("days_since_last_commit") is not None:
            if ph["days_since_last_commit"] <= 7:
                lines.append(
                    f"- {yes} Active — last commit {ph['days_since_last_commit']} day(s) ago"
                )
            elif ph["days_since_last_commit"] <= 30:
                lines.append(
                    f"- ~ Moderately active — last commit {ph['days_since_last_commit']} days ago"
                )
            else:
                lines.append(
                    f"- {no} Inactive — last commit {ph['days_since_last_commit']} days ago"
                )
        lines.append("")

    return "\n".join(lines)


def format_text(data: Dict[str, Any]) -> str:
    """Plain-text compact format."""
    if data.get("total_commits", 0) == 0:
        return f"No commits in {data['repo']} over the last {data['period_days']} days."

    parts = [
        f"REPO: {data['repo']} | {data['total_commits']} commits | "
        f"{data['unique_authors']} contributors | last {data['period_days']} days",
        f"LINES: +{data['lines']['additions']:,} -{data['lines']['deletions']:,} "
        f"(net {data['lines']['net']:+,})",
    ]
    if data.get("technologies"):
        parts.append(f"TECH: {', '.join(data['technologies'])}")
    if data.get("work_types"):
        total = sum(data["work_types"].values())
        wt_str = ", ".join(
            f"{k} {round(100 * v / total)}%" for k, v in data["work_types"].items()
        )
        parts.append(f"WORK: {wt_str}")
        clf = data.get("classification") or {}
        if clf.get("unreliable"):
            parts.append(
                f"CLASSIFY: unreliable other={round(100 * clf.get('other_share', 0))}%"
            )
    if data.get("churn_hotspots"):
        top3 = [h["path"] for h in data["churn_hotspots"][:3]]
        parts.append(f"HOTSPOTS: {', '.join(top3)}")
    if data.get("velocity"):
        parts.append(
            f"VELOCITY: {data['velocity']['commits_per_week']} commits/week, "
            f"{data['velocity']['active_days']} active days "
            f"(noise files excluded from avg size)"
        )
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _configure_stdout_utf8() -> None:
    """Best-effort UTF-8 stdout so status glyphs do not crash on Windows."""
    reconfigure = getattr(sys.stdout, "reconfigure", None)
    if callable(reconfigure):
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def main(argv: Optional[List[str]] = None) -> None:
    parser = argparse.ArgumentParser(
        description="Summarize repository engineering activity from git history.",
    )
    parser.add_argument(
        "--repo-dir", default=".",
        help="Path to git repository (default: current directory)",
    )
    parser.add_argument(
        "--days", type=int, default=90,
        help="Days of history to analyze (default: 90)",
    )
    parser.add_argument("--author", default=None, help="Filter to a specific author")
    parser.add_argument(
        "--format", choices=["markdown", "json", "text"], default="markdown",
        help="Output format",
    )
    parser.add_argument(
        "--max-commits", type=int, default=500,
        help="Max commits to process (default: 500)",
    )
    parser.add_argument(
        "--branch", default=None,
        help="Branch to analyze (default: current HEAD)",
    )
    parser.add_argument(
        "--output", "-o", default=None,
        help="Write output to file instead of stdout",
    )
    parser.add_argument(
        "--classify-threshold", type=float, default=0.25,
        help=(
            "If the share of unclassified commits exceeds this fraction "
            "(default: 0.25), mark classification unreliable and emit samples"
        ),
    )
    parser.add_argument(
        "--max-unclassified-samples", type=int, default=40,
        help="Max unclassified commit subjects to include (default: 40)",
    )
    parser.add_argument(
        "--raw-subjects", action="store_true",
        help="Include every filtered commit subject (sha + date + message)",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args(argv)

    if args.classify_threshold < 0 or args.classify_threshold > 1:
        print(
            "Error: --classify-threshold must be between 0 and 1 inclusive.",
            file=sys.stderr,
        )
        sys.exit(2)

    try:
        data = analyze(
            repo_dir=args.repo_dir,
            days=args.days,
            author=args.author,
            max_commits=args.max_commits,
            branch=args.branch,
            classify_threshold=args.classify_threshold,
            max_unclassified_samples=args.max_unclassified_samples,
            raw_subjects=args.raw_subjects,
        )
    except (RuntimeError, FileNotFoundError, NotADirectoryError, OSError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.format == "json":
        output = json.dumps(data, indent=2, default=str)
    elif args.format == "text":
        output = format_text(data)
    else:
        output = format_markdown(data)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Written to {args.output}", file=sys.stderr)
    else:
        _configure_stdout_utf8()
        try:
            print(output)
        except UnicodeEncodeError:
            # Last-resort ASCII-safe write for legacy consoles
            encoding = getattr(sys.stdout, "encoding", None) or "ascii"
            sys.stdout.buffer.write(
                output.encode(encoding, errors="replace") + b"\n"
            )


if __name__ == "__main__":
    main()
