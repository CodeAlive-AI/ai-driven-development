#!/usr/bin/env python3
"""Diff two versions of a Claude Code skill's SKILL.md.

Supports diffing across git commits, between two arbitrary files, or against
the previous logged snapshot (when log_skill_edit.py --snapshot was used).
"""

import argparse
import difflib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


LOG_FILENAME = ".skill_edit_log.jsonl"
SNAPSHOTS_DIRNAME = ".skill_snapshots"


def get_user_skills_dir() -> Path:
    """Get the user-level skills directory."""
    return Path.home() / ".claude" / "skills"


def get_project_skills_dir() -> Path:
    """Get the project-level skills directory (current working directory)."""
    return Path.cwd() / ".claude" / "skills"


def find_skill(name: str, scope: str | None = None) -> tuple[Path | None, str | None]:
    """Find a skill by name, optionally filtering by scope."""
    scopes_to_check = []
    if scope is None or scope == "user":
        scopes_to_check.append(("user", get_user_skills_dir()))
    if scope is None or scope == "project":
        scopes_to_check.append(("project", get_project_skills_dir()))

    for scope_name, skills_dir in scopes_to_check:
        skill_path = skills_dir / name
        if skill_path.exists() and (skill_path / "SKILL.md").exists():
            return skill_path, scope_name

    return None, None


def parse_frontmatter_body(content: str) -> str:
    """Return the body portion of SKILL.md (everything after the frontmatter)."""
    body_match = re.match(r"^---\s*\n.*?\n---\s*\n(.*)$", content, re.DOTALL)
    if body_match:
        return body_match.group(1)
    return content


def git_available() -> bool:
    """Check whether git is on PATH."""
    return shutil.which("git") is not None


def git_show_file(repo_path: Path, commit: str, relative_path: str) -> tuple[str | None, str | None]:
    """Run `git show <commit>:<relative_path>` inside repo_path.

    Returns:
        (content, error_message). One of them is None.
    """
    if not git_available():
        return None, "git is not available on PATH"
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_path), "show", f"{commit}:{relative_path}"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError as e:
        return None, f"failed to invoke git: {e}"

    if result.returncode != 0:
        msg = result.stderr.strip() or f"git exited with code {result.returncode}"
        return None, msg
    return result.stdout, None


def git_repo_root(path: Path) -> Path | None:
    """Find the git repo root that contains path, if any."""
    if not git_available():
        return None
    try:
        result = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    if result.returncode != 0:
        return None
    return Path(result.stdout.strip())


def find_previous_snapshot(skill_path: Path, current_sha: str | None) -> Path | None:
    """Return the most recent snapshot file that is not the current SKILL.md.

    Picks by modification time so the chain reflects log order.
    """
    snapshots_dir = skill_path / SNAPSHOTS_DIRNAME
    if not snapshots_dir.exists():
        return None
    snapshots = sorted(
        snapshots_dir.glob("SKILL.*.md"),
        key=lambda p: p.stat().st_mtime,
    )
    if not snapshots:
        return None
    # If the newest snapshot matches the current sha8, prefer the one before it.
    if current_sha and snapshots[-1].stem.endswith(current_sha[:8]) and len(snapshots) >= 2:
        return snapshots[-2]
    return snapshots[-1]


def colorise_unified(diff_text: str) -> str:
    """Add ANSI colors to a unified diff if stdout is a TTY."""
    if not sys.stdout.isatty():
        return diff_text
    red = "\033[31m"
    green = "\033[32m"
    cyan = "\033[36m"
    reset = "\033[0m"
    out_lines = []
    for line in diff_text.split("\n"):
        if line.startswith("+++") or line.startswith("---"):
            out_lines.append(f"{cyan}{line}{reset}")
        elif line.startswith("@@"):
            out_lines.append(f"{cyan}{line}{reset}")
        elif line.startswith("+"):
            out_lines.append(f"{green}{line}{reset}")
        elif line.startswith("-"):
            out_lines.append(f"{red}{line}{reset}")
        else:
            out_lines.append(line)
    return "\n".join(out_lines)


def render_unified(label_a: str, label_b: str, text_a: str, text_b: str) -> str:
    """Render a unified diff."""
    diff = difflib.unified_diff(
        text_a.splitlines(keepends=True),
        text_b.splitlines(keepends=True),
        fromfile=label_a,
        tofile=label_b,
        n=3,
    )
    text = "".join(diff)
    if not text:
        return f"(no differences between {label_a} and {label_b})"
    return colorise_unified(text)


def render_stats(label_a: str, label_b: str, text_a: str, text_b: str) -> str:
    """Render a compact stats summary."""
    body_a = parse_frontmatter_body(text_a)
    body_b = parse_frontmatter_body(text_b)
    tokens_a = len(body_a) // 4
    tokens_b = len(body_b) // 4
    headings_a = len(re.findall(r"^#+\s", body_a, re.MULTILINE))
    headings_b = len(re.findall(r"^#+\s", body_b, re.MULTILINE))

    added = 0
    removed = 0
    for line in difflib.unified_diff(text_a.splitlines(), text_b.splitlines(), n=0):
        if line.startswith("+") and not line.startswith("+++"):
            added += 1
        elif line.startswith("-") and not line.startswith("---"):
            removed += 1

    lines = [
        f"Diff stats: {label_a} -> {label_b}",
        "-" * 40,
        f"  Lines added:    {added}",
        f"  Lines removed:  {removed}",
        f"  Tokens before:  {tokens_a}",
        f"  Tokens after:   {tokens_b}",
        f"  Token delta:    {tokens_b - tokens_a:+d}",
        f"  Headings before:{headings_a:>4}",
        f"  Headings after: {headings_b:>4}",
    ]
    return "\n".join(lines)


def render_side_by_side(label_a: str, label_b: str, text_a: str, text_b: str) -> str:
    """Render a side-by-side HTML diff to a temp file and return the path message."""
    html = difflib.HtmlDiff(wrapcolumn=80).make_file(
        text_a.splitlines(),
        text_b.splitlines(),
        fromdesc=label_a,
        todesc=label_b,
    )
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", prefix="skill-diff-", delete=False, encoding="utf-8"
    )
    try:
        tmp.write(html)
    finally:
        tmp.close()
    return f"Side-by-side diff written to: {tmp.name}"


def render(format_name: str, label_a: str, label_b: str, text_a: str, text_b: str) -> str:
    """Dispatch to the appropriate renderer."""
    if format_name == "stats":
        return render_stats(label_a, label_b, text_a, text_b)
    if format_name == "side-by-side":
        return render_side_by_side(label_a, label_b, text_a, text_b)
    return render_unified(label_a, label_b, text_a, text_b)


def resolve_git_diff(
    skill_path: Path, commit_a: str, commit_b: str
) -> tuple[str, str, str, str] | None:
    """Resolve the two sides of a git-mode diff.

    Returns (label_a, label_b, text_a, text_b) or None on failure (already printed).
    """
    repo_root = git_repo_root(skill_path)
    if repo_root is None:
        print(
            f"Error: '{skill_path}' is not inside a git repository (or git is unavailable).",
            file=sys.stderr,
        )
        return None

    try:
        rel = (skill_path / "SKILL.md").resolve().relative_to(repo_root.resolve())
    except ValueError:
        print(
            f"Error: SKILL.md path is not inside repo root {repo_root}.",
            file=sys.stderr,
        )
        return None

    text_a, err_a = git_show_file(repo_root, commit_a, str(rel))
    if err_a is not None:
        print(f"Error: git show {commit_a}:{rel}: {err_a}", file=sys.stderr)
        return None
    text_b, err_b = git_show_file(repo_root, commit_b, str(rel))
    if err_b is not None:
        print(f"Error: git show {commit_b}:{rel}: {err_b}", file=sys.stderr)
        return None

    return f"{commit_a}:SKILL.md", f"{commit_b}:SKILL.md", text_a, text_b


def resolve_files_diff(
    path_a: Path, path_b: Path
) -> tuple[str, str, str, str] | None:
    """Resolve a file-mode diff."""
    for p in (path_a, path_b):
        if not p.exists():
            print(f"Error: file not found: {p}", file=sys.stderr)
            return None
    text_a = path_a.read_text(encoding="utf-8")
    text_b = path_b.read_text(encoding="utf-8")
    return str(path_a), str(path_b), text_a, text_b


def resolve_log_diff(skill_path: Path) -> tuple[str, str, str, str] | None:
    """Resolve a log-mode diff (current SKILL.md vs. previous snapshot)."""
    skill_md = skill_path / "SKILL.md"
    current = skill_md.read_text(encoding="utf-8")
    import hashlib
    current_sha = hashlib.sha256(current.encode("utf-8")).hexdigest()

    snapshot = find_previous_snapshot(skill_path, current_sha)
    if snapshot is not None:
        prev_text = snapshot.read_text(encoding="utf-8")
        return f"snapshot:{snapshot.name}", "SKILL.md (current)", prev_text, current

    # Fallback: try git HEAD~1 vs HEAD on SKILL.md.
    print(
        "Hint: no snapshots in .skill_snapshots/. "
        "Pass --snapshot to log_skill_edit.py to record full history. "
        "Falling back to git HEAD~1..HEAD.",
        file=sys.stderr,
    )
    repo_root = git_repo_root(skill_path)
    if repo_root is None:
        print(
            "Error: no snapshots and skill is not in a git repository — nothing to diff.",
            file=sys.stderr,
        )
        return None
    try:
        rel = skill_md.resolve().relative_to(repo_root.resolve())
    except ValueError:
        print(f"Error: SKILL.md path is not inside repo root {repo_root}.", file=sys.stderr)
        return None
    prev_text, err = git_show_file(repo_root, "HEAD~1", str(rel))
    if err is not None:
        print(f"Error: git show HEAD~1:{rel}: {err}", file=sys.stderr)
        return None
    head_text, err = git_show_file(repo_root, "HEAD", str(rel))
    if err is not None:
        print(f"Error: git show HEAD:{rel}: {err}", file=sys.stderr)
        return None
    return "HEAD~1:SKILL.md", "HEAD:SKILL.md", prev_text, head_text


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Diff two versions of a Claude Code skill's SKILL.md"
    )
    parser.add_argument("name", help="Name of the skill")
    parser.add_argument(
        "--scope", "-s",
        choices=["user", "project"],
        help="Scope to search (default: search both)"
    )

    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--git",
        nargs="+",
        metavar="COMMIT",
        help="Diff between two git commits (second defaults to HEAD)"
    )
    mode.add_argument(
        "--files",
        nargs=2,
        metavar=("PATH_A", "PATH_B"),
        help="Diff between two explicit file paths"
    )
    mode.add_argument(
        "--log",
        action="store_true",
        help="Diff current SKILL.md vs. previous logged snapshot"
    )

    parser.add_argument(
        "--format", "-f",
        choices=["unified", "stats", "side-by-side"],
        default="unified",
        help="Output format (default: unified)"
    )
    args = parser.parse_args()

    skill_path, _ = find_skill(args.name, args.scope)
    if not skill_path:
        print(f"Error: Skill '{args.name}' not found.", file=sys.stderr)
        return 1

    # Resolve diff sources by mode.
    resolved: tuple[str, str, str, str] | None
    if args.git is not None:
        if len(args.git) == 1:
            commit_a, commit_b = args.git[0], "HEAD"
        elif len(args.git) == 2:
            commit_a, commit_b = args.git[0], args.git[1]
        else:
            print("Error: --git accepts 1 or 2 commit arguments.", file=sys.stderr)
            return 1
        resolved = resolve_git_diff(skill_path, commit_a, commit_b)
    elif args.files is not None:
        resolved = resolve_files_diff(Path(args.files[0]), Path(args.files[1]))
    elif args.log:
        resolved = resolve_log_diff(skill_path)
    else:
        print(
            "Error: choose one of --git, --files, or --log. See --help.",
            file=sys.stderr,
        )
        return 1

    if resolved is None:
        return 1

    label_a, label_b, text_a, text_b = resolved
    print(render(args.format, label_a, label_b, text_a, text_b))
    return 0


if __name__ == "__main__":
    sys.exit(main())
