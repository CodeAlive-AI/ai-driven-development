#!/usr/bin/env python3
"""
Repo Activity Summary — extract structured engineering signals from git history.

Runs entirely against the local git log. No API keys, no network access.
Adapted from a git-signal-extraction tool built independently.

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

__version__ = "1.0.0"

# ---------------------------------------------------------------------------
# Technology detection patterns (file extension / name → technology label)
# ---------------------------------------------------------------------------

TECH_PATTERNS: Dict[str, List[str]] = {
    "Python": [".py", "requirements.txt", "setup.py", "pyproject.toml", "Pipfile"],
    "JavaScript": [".js", ".jsx", "package.json", ".mjs", ".cjs"],
    "TypeScript": [".ts", ".tsx", "tsconfig.json"],
    "React": [".jsx", ".tsx", "next.config"],
    "Vue": [".vue", "vue.config", "nuxt.config"],
    "Svelte": [".svelte", "svelte.config"],
    "Rust": [".rs", "Cargo.toml"],
    "Go": [".go", "go.mod", "go.sum"],
    "Java": [".java", "pom.xml", "build.gradle"],
    "Kotlin": [".kt", ".kts"],
    "Swift": [".swift", "Package.swift"],
    "C#": [".cs", ".csproj", ".sln"],
    "C/C++": [".c", ".cpp", ".h", ".hpp", "CMakeLists.txt", "Makefile"],
    "Ruby": [".rb", "Gemfile", "Rakefile"],
    "PHP": [".php", "composer.json"],
    "Elixir": [".ex", ".exs", "mix.exs"],
    "Scala": [".scala", "build.sbt"],
    "Docker": ["Dockerfile", "docker-compose", ".dockerignore"],
    "Kubernetes": ["k8s", "helm", "kustomization"],
    "Terraform": [".tf", "terraform"],
    "SQL": [".sql", "migrations/", "prisma/", "drizzle/"],
    "GraphQL": [".graphql", ".gql"],
    "CSS": [".css", ".scss", ".sass", ".less", "tailwind"],
    "CI/CD": [".github/workflows", ".gitlab-ci", "Jenkinsfile", ".circleci"],
}

# ---------------------------------------------------------------------------
# Work type classification from commit messages
# ---------------------------------------------------------------------------

WORK_TYPE_PATTERNS: Dict[str, List[str]] = {
    "feature": ["feat", "add", "implement", "new", "create", "introduce", "support"],
    "bugfix": ["fix", "bug", "patch", "hotfix", "resolve", "correct", "repair"],
    "refactor": ["refactor", "cleanup", "improve", "optimize", "reorganize", "restructure", "simplify"],
    "docs": ["docs", "readme", "documentation", "comment", "jsdoc", "docstring"],
    "testing": ["test", "spec", "coverage", "jest", "pytest", "e2e", "vitest"],
    "infrastructure": ["config", "ci", "cd", "deploy", "env", "build", "docker", "infra", "devops"],
    "ui": ["ui", "style", "css", "design", "layout", "component", "page", "responsive"],
    "performance": ["perf", "performance", "speed", "cache", "optimize", "lazy", "memo"],
    "security": ["security", "vulnerability", "sanitize", "validate", "encrypt", "auth"],
}

# Commit messages that carry no useful signal
NOISE_MESSAGES = {
    "initial commit", "init", "first commit", "update", "updates",
    "wip", "work in progress", "fix", "fixes", "minor", "misc",
    "changes", "stuff", "temp", "test", "testing", ".",
    "commit", "save", "push", "done", "finished",
    "lint", "linting", "format", "formatting", "typo", "typos",
    "cleanup", "clean up", "clean", "prettier", "eslint",
    "nit", "oops", "revert", "undo", "retry", "again",
    "asdf", "asd", "foo", "bar", "xxx", "todo",
}

BOT_AUTHOR_PATTERNS = [
    "bot", "dependabot", "renovate", "github-actions",
    "semantic-release", "greenkeeper", "snyk", "deepsource",
]

# Files that indicate noise, not real engineering work
NOISE_FILE_HINTS = [
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "Pipfile.lock",
    "poetry.lock", "Cargo.lock", "go.sum", "Gemfile.lock", "composer.lock",
    ".min.", ".map", "dist/", "build/", ".next/", "node_modules/",
    "vendor/", "__pycache__/", ".generated.", ".auto.",
]


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


def parse_git_log(
    repo_dir: str,
    days: int,
    author: Optional[str],
    max_commits: int,
    branch: Optional[str],
) -> List[Dict[str, Any]]:
    """Parse git log with --numstat into structured commit dicts."""
    since = (datetime.now(timezone.utc) - timedelta(days=days)).strftime("%Y-%m-%d")

    cmd = [
        "log",
        f"--since={since}",
        f"--max-count={max_commits}",
        "--format=COMMIT_SEP%n%H%n%an%n%ae%n%aI%n%s",
        "--numstat",
        "--no-merges",
    ]
    if author:
        cmd.append(f"--author={author}")
    if branch:
        cmd.append(branch)

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

def is_bot_author(author: str) -> bool:
    author_lower = author.lower()
    return any(p in author_lower for p in BOT_AUTHOR_PATTERNS)


def is_noise_message(message: str) -> bool:
    return message.lower().strip().rstrip(".") in NOISE_MESSAGES


def is_noise_file(filepath: str) -> bool:
    lower = filepath.lower()
    return any(hint in lower for hint in NOISE_FILE_HINTS)


def filter_commits(commits: List[Dict]) -> Tuple[List[Dict], int]:
    """Filter out bot commits and pure-noise commits. Returns (filtered, skipped_count)."""
    filtered = []
    skipped = 0
    for commit in commits:
        if is_bot_author(commit["author"]):
            skipped += 1
            continue
        filtered.append(commit)
    return filtered, skipped


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def detect_technologies(commits: List[Dict]) -> List[str]:
    """Detect technologies from file paths across all commits."""
    techs = set()
    for commit in commits:
        for f in commit["files"]:
            path_lower = f["path"].lower()
            for tech, patterns in TECH_PATTERNS.items():
                if any(p.lower() in path_lower for p in patterns):
                    techs.add(tech)
    return sorted(techs)


def classify_work_types(commits: List[Dict]) -> Dict[str, int]:
    """Classify commits by work type from their messages."""
    counts: Dict[str, int] = defaultdict(int)
    unclassified = 0
    for commit in commits:
        msg_lower = commit["message"].lower()
        matched = False
        for work_type, patterns in WORK_TYPE_PATTERNS.items():
            if any(p in msg_lower for p in patterns):
                counts[work_type] += 1
                matched = True
                break
        if not matched:
            unclassified += 1
    if unclassified:
        counts["other"] = unclassified
    return dict(sorted(counts.items(), key=lambda x: -x[1]))


def compute_churn_hotspots(commits: List[Dict], top_n: int = 10) -> List[Dict]:
    """Find the most frequently modified files."""
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
    """Aggregate churn to top-level directories."""
    dir_stats: Dict[str, Dict] = defaultdict(lambda: {
        "modifications": 0, "additions": 0, "deletions": 0, "files": set(),
    })
    for commit in commits:
        for f in commit["files"]:
            path = f["path"]
            if is_noise_file(path):
                continue
            parts = path.split("/")
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

        msg_lower = commit["message"].lower()
        for work_type, patterns in WORK_TYPE_PATTERNS.items():
            if any(p in msg_lower for p in patterns):
                stats["work_types"][work_type] += 1
                break

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


def compute_velocity(commits: List[Dict], days: int) -> Dict[str, Any]:
    """Compute velocity indicators."""
    if not commits:
        return {"commits_per_week": 0, "active_days": 0, "avg_commit_size": 0}

    dates = {c["date"].date() for c in commits}
    active_days = len(dates)
    total_changes = sum(c["insertions"] + c["deletions"] for c in commits)
    weeks = max(days / 7, 1)

    return {
        "commits_per_week": round(len(commits) / weeks, 1),
        "active_days": active_days,
        "active_day_ratio": round(active_days / max(days, 1), 2),
        "avg_commit_size": round(total_changes / len(commits)) if commits else 0,
    }


def assess_project_health(commits: List[Dict], repo_dir: str) -> Dict[str, Any]:
    """Check for tests, CI, docs, and recency."""
    all_files = set()
    for commit in commits:
        for f in commit["files"]:
            all_files.add(f["path"])

    # Also check current tree for baseline signals
    try:
        tree_files = run_git(["ls-files"], repo_dir).strip().split("\n")
    except RuntimeError:
        tree_files = []

    combined = all_files | set(tree_files)
    combined_lower = {f.lower() for f in combined}

    has_tests = any(
        "test" in f or "spec" in f or "__tests__" in f
        for f in combined_lower
    )
    test_file_count = sum(
        1 for f in combined_lower
        if re.search(r"(test_|_test\.|\.test\.|\.spec\.|__tests__)", f)
    )

    has_ci = any(
        ".github/workflows" in f or ".gitlab-ci" in f
        or "jenkinsfile" in f or ".circleci" in f
        for f in combined_lower
    )

    has_docs = any(
        f.endswith("readme.md") or f.startswith("docs/") or f.endswith(".rst")
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
        "test_file_count": test_file_count,
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
) -> Dict[str, Any]:
    """Run the full analysis pipeline and return structured results."""
    repo_dir = os.path.abspath(repo_dir)

    # Get repo name from the directory or git remote
    try:
        remote = run_git(["remote", "get-url", "origin"], repo_dir).strip()
        repo_name = remote.rstrip("/").split("/")[-1].removesuffix(".git")
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
    work_types = classify_work_types(meaningful) if meaningful else {}

    return {
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
        "churn_hotspots": compute_churn_hotspots(commits),
        "directory_hotspots": compute_directory_hotspots(commits),
        "contributors": analyze_contributors(commits),
        "velocity": compute_velocity(commits, days),
        "project_health": assess_project_health(commits, repo_dir),
    }


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def format_markdown(data: Dict[str, Any]) -> str:
    """Render analysis as a readable markdown report."""
    if data.get("total_commits", 0) == 0:
        return f"## Repo Activity Summary — {data['repo']}\n\nNo commits found in the last {data['period_days']} days."

    lines = []
    period = f"last {data['period_days']} days"
    author_note = f" (author: {data['author_filter']})" if data.get("author_filter") else ""
    lines.append(f"## Repo Activity Summary — {data['repo']} ({period}){author_note}\n")

    # Overview
    dr = data["date_range"]
    start = dr["start"][:10]
    end = dr["end"][:10]
    lines.append("### Overview")
    lines.append(f"- **{data['total_commits']}** commits by **{data['unique_authors']}** contributor(s)")
    lines.append(f"- **{data['lines']['additions']:,}** lines added, **{data['lines']['deletions']:,}** deleted (net {data['lines']['net']:+,})")
    lines.append(f"- Date range: {start} → {end}")
    if data.get("skipped_bot_commits"):
        lines.append(f"- {data['skipped_bot_commits']} bot commits filtered out")
    lines.append("")

    # Technologies
    if data.get("technologies"):
        lines.append("### Technologies")
        lines.append(", ".join(data["technologies"]))
        lines.append("")

    # Work types
    if data.get("work_types"):
        lines.append("### Work Type Breakdown")
        total = sum(data["work_types"].values())
        for wt, count in data["work_types"].items():
            pct = round(100 * count / total) if total else 0
            lines.append(f"- {wt.capitalize()}: {pct}% ({count} commits)")
        lines.append("")

    # Churn hotspots
    if data.get("churn_hotspots"):
        lines.append("### Churn Hotspots")
        for i, h in enumerate(data["churn_hotspots"], 1):
            lines.append(f"{i}. `{h['path']}` — {h['modifications']} modifications, +{h['additions']}/-{h['deletions']}")
        lines.append("")

    # Directory hotspots
    if data.get("directory_hotspots"):
        lines.append("### Directory Activity")
        for dh in data["directory_hotspots"]:
            lines.append(f"- `{dh['directory']}/` — {dh['modifications']} changes across {dh['unique_files']} files")
        lines.append("")

    # Contributors
    if data.get("contributors"):
        lines.append("### Contributors")
        lines.append("| Author | Commits | Lines +/- | Primary Focus |")
        lines.append("|--------|---------|-----------|---------------|")
        for c in data["contributors"]:
            focus = ", ".join(c["primary_focus"])
            lines.append(f"| {c['author']} | {c['commits']} | +{c['additions']:,}/-{c['deletions']:,} | {focus} |")
        lines.append("")

    # Velocity
    if data.get("velocity"):
        v = data["velocity"]
        lines.append("### Velocity")
        lines.append(f"- {v['commits_per_week']} commits/week")
        lines.append(f"- {v['active_days']} active days ({round(v.get('active_day_ratio', 0) * 100)}% of period)")
        lines.append(f"- Average commit size: {v['avg_commit_size']:,} lines changed")
        lines.append("")

    # Project health
    if data.get("project_health"):
        ph = data["project_health"]
        lines.append("### Project Health")
        lines.append(f"- {'✓' if ph['has_tests'] else '✗'} Tests {'present' if ph['has_tests'] else 'not detected'}" +
                      (f" ({ph['test_file_count']} test files)" if ph.get("test_file_count") else ""))
        lines.append(f"- {'✓' if ph['has_ci'] else '✗'} CI {'configured' if ph['has_ci'] else 'not detected'}")
        lines.append(f"- {'✓' if ph['has_docs'] else '✗'} Documentation {'exists' if ph['has_docs'] else 'not detected'}")
        if ph.get("days_since_last_commit") is not None:
            if ph["days_since_last_commit"] <= 7:
                lines.append(f"- ✓ Active — last commit {ph['days_since_last_commit']} day(s) ago")
            elif ph["days_since_last_commit"] <= 30:
                lines.append(f"- ~ Moderately active — last commit {ph['days_since_last_commit']} days ago")
            else:
                lines.append(f"- ✗ Inactive — last commit {ph['days_since_last_commit']} days ago")
        lines.append("")

    return "\n".join(lines)


def format_text(data: Dict[str, Any]) -> str:
    """Plain-text compact format."""
    if data.get("total_commits", 0) == 0:
        return f"No commits in {data['repo']} over the last {data['period_days']} days."

    parts = [
        f"REPO: {data['repo']} | {data['total_commits']} commits | {data['unique_authors']} contributors | last {data['period_days']} days",
        f"LINES: +{data['lines']['additions']:,} -{data['lines']['deletions']:,} (net {data['lines']['net']:+,})",
    ]
    if data.get("technologies"):
        parts.append(f"TECH: {', '.join(data['technologies'])}")
    if data.get("work_types"):
        total = sum(data["work_types"].values())
        wt_str = ", ".join(f"{k} {round(100*v/total)}%" for k, v in data["work_types"].items())
        parts.append(f"WORK: {wt_str}")
    if data.get("churn_hotspots"):
        top3 = [h["path"] for h in data["churn_hotspots"][:3]]
        parts.append(f"HOTSPOTS: {', '.join(top3)}")
    if data.get("velocity"):
        parts.append(f"VELOCITY: {data['velocity']['commits_per_week']} commits/week, {data['velocity']['active_days']} active days")
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Summarize repository engineering activity from git history.",
    )
    parser.add_argument("--repo-dir", default=".", help="Path to git repository (default: current directory)")
    parser.add_argument("--days", type=int, default=90, help="Days of history to analyze (default: 90)")
    parser.add_argument("--author", default=None, help="Filter to a specific author")
    parser.add_argument("--format", choices=["markdown", "json", "text"], default="markdown", help="Output format")
    parser.add_argument("--max-commits", type=int, default=500, help="Max commits to process (default: 500)")
    parser.add_argument("--branch", default=None, help="Branch to analyze (default: current HEAD)")
    parser.add_argument("--output", "-o", default=None, help="Write output to file instead of stdout")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()

    try:
        data = analyze(
            repo_dir=args.repo_dir,
            days=args.days,
            author=args.author,
            max_commits=args.max_commits,
            branch=args.branch,
        )
    except RuntimeError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.format == "json":
        output = json.dumps(data, indent=2, default=str)
    elif args.format == "text":
        output = format_text(data)
    else:
        output = format_markdown(data)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"Written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
