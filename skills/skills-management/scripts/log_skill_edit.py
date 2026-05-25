#!/usr/bin/env python3
"""Log a manual edit to a Claude Code skill into an append-only audit trail.

Modelled on Microsoft's SkillOpt paper (arXiv 2605.23904): every accepted skill
edit is recorded so regressions can be diagnosed and bisected. Each entry is one
line of JSON in <skill>/.skill_edit_log.jsonl.
"""

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
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
    """Find a skill by name, optionally filtering by scope.

    Returns:
        Tuple of (skill_path, scope_name) or (None, None) if not found
    """
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


def compute_sha256(text: str) -> str:
    """Compute SHA256 hex digest of a string."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_duration(spec: str) -> int:
    """Parse a duration spec like '7d', '30m', '12h', '60s' into seconds.

    Raises:
        ValueError: on malformed input.
    """
    match = re.fullmatch(r"(\d+)([smhd])", spec.strip())
    if not match:
        raise ValueError(f"Invalid duration '{spec}'. Use formats like '60s', '30m', '12h', '7d'.")
    n = int(match.group(1))
    unit = match.group(2)
    multipliers = {"s": 1, "m": 60, "h": 3600, "d": 86400}
    return n * multipliers[unit]


def read_log_entries(log_path: Path) -> list[dict]:
    """Read all entries from the JSONL log file.

    Returns:
        List of entries in file order. Malformed lines are skipped silently.
    """
    if not log_path.exists():
        return []
    entries = []
    with log_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return entries


def append_log_entry(log_path: Path, entry: dict) -> None:
    """Append a single entry as JSONL."""
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False))
        f.write("\n")


def save_snapshot(skill_path: Path, content: str, sha_after: str) -> Path:
    """Save the current SKILL.md content to .skill_snapshots/SKILL.<sha8>.md."""
    snapshots_dir = skill_path / SNAPSHOTS_DIRNAME
    snapshots_dir.mkdir(exist_ok=True)
    sha8 = sha_after[:8]
    snapshot_path = snapshots_dir / f"SKILL.{sha8}.md"
    if not snapshot_path.exists():
        snapshot_path.write_text(content, encoding="utf-8")
    return snapshot_path


def build_entry(
    skill_path: Path,
    reason: str,
    source: str,
    ref: str | None,
    previous_entries: list[dict],
) -> tuple[dict, str]:
    """Build a new log entry from the current SKILL.md state.

    Returns:
        (entry_dict, current_skill_md_content)
    """
    skill_md = skill_path / "SKILL.md"
    content = skill_md.read_text(encoding="utf-8")
    body = parse_frontmatter_body(content)
    body_lines = len(body.split("\n"))
    body_tokens = len(body) // 4

    sha_after = compute_sha256(content)
    sha_before = previous_entries[-1].get("sha_after") if previous_entries else None
    prev_tokens = previous_entries[-1].get("body_tokens") if previous_entries else None
    delta_tokens = body_tokens - prev_tokens if prev_tokens is not None else None

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "sha_before": sha_before,
        "sha_after": sha_after,
        "body_lines": body_lines,
        "body_tokens": body_tokens,
        "delta_tokens": delta_tokens,
        "reason": reason,
        "source": source,
        "ref": ref,
        "user": os.environ.get("USER"),
    }
    return entry, content


def filter_entries_since(entries: list[dict], since_spec: str) -> list[dict]:
    """Return entries whose timestamp is within the given duration of now."""
    seconds = parse_duration(since_spec)
    cutoff = datetime.now(timezone.utc).timestamp() - seconds
    kept = []
    for entry in entries:
        ts = entry.get("timestamp")
        if not ts:
            continue
        try:
            entry_dt = datetime.fromisoformat(ts)
        except ValueError:
            continue
        if entry_dt.timestamp() >= cutoff:
            kept.append(entry)
    return kept


def format_list_text(entries: list[dict]) -> str:
    """Render entries as a simple text table."""
    if not entries:
        return "No entries to display."

    rows = [("TIMESTAMP", "SOURCE", "DELTA", "REASON")]
    for entry in entries:
        ts = entry.get("timestamp", "")
        source = entry.get("source", "")
        delta = entry.get("delta_tokens")
        delta_s = "-" if delta is None else (f"+{delta}" if delta > 0 else str(delta))
        reason = entry.get("reason", "")
        if len(reason) > 60:
            reason = reason[:57] + "..."
        rows.append((ts, source, delta_s, reason))

    widths = [max(len(r[i]) for r in rows) for i in range(len(rows[0]))]
    lines = []
    for i, row in enumerate(rows):
        line = "  ".join(row[j].ljust(widths[j]) for j in range(len(row)))
        lines.append(line)
        if i == 0:
            lines.append("  ".join("-" * widths[j] for j in range(len(row))))
    return "\n".join(lines)


def cmd_log(args: argparse.Namespace) -> int:
    """Handle a logging invocation."""
    skill_path, _ = find_skill(args.name, args.scope)
    if not skill_path:
        print(f"Error: Skill '{args.name}' not found.", file=sys.stderr)
        return 1

    log_path = skill_path / LOG_FILENAME

    try:
        previous_entries = read_log_entries(log_path)
    except OSError as e:
        print(f"Error: Cannot read log file: {e}", file=sys.stderr)
        return 1

    try:
        entry, content = build_entry(
            skill_path,
            reason=args.reason,
            source=args.source,
            ref=args.ref,
            previous_entries=previous_entries,
        )
    except OSError as e:
        print(f"Error: Cannot read SKILL.md: {e}", file=sys.stderr)
        return 1

    if args.dry_run:
        print("[dry-run] Would append the following entry:")
        print(json.dumps(entry, indent=2, ensure_ascii=False))
        if args.snapshot:
            sha8 = entry["sha_after"][:8]
            print(f"[dry-run] Would save snapshot: {skill_path / SNAPSHOTS_DIRNAME / f'SKILL.{sha8}.md'}")
        return 0

    try:
        append_log_entry(log_path, entry)
    except OSError as e:
        print(f"Error: Cannot write log file: {e}", file=sys.stderr)
        return 1

    snapshot_msg = ""
    if args.snapshot:
        try:
            snapshot_path = save_snapshot(skill_path, content, entry["sha_after"])
            snapshot_msg = f" (snapshot saved to {snapshot_path})"
        except OSError as e:
            print(f"Warning: Cannot save snapshot: {e}", file=sys.stderr)

    delta = entry["delta_tokens"]
    delta_s = "n/a" if delta is None else (f"+{delta}" if delta > 0 else str(delta))
    print(f"Logged edit to '{args.name}': delta_tokens={delta_s}, sha_after={entry['sha_after'][:12]}{snapshot_msg}")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    """Handle a --list invocation."""
    skill_path, _ = find_skill(args.name, args.scope)
    if not skill_path:
        print(f"Error: Skill '{args.name}' not found.", file=sys.stderr)
        return 1

    log_path = skill_path / LOG_FILENAME
    if not log_path.exists():
        print(f"No edit log yet for '{args.name}'", file=sys.stderr)
        return 0

    try:
        entries = read_log_entries(log_path)
    except OSError as e:
        print(f"Error: Cannot read log file: {e}", file=sys.stderr)
        return 1

    if args.since:
        try:
            entries = filter_entries_since(entries, args.since)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1

    # Default: show last 20.
    tail = entries[-20:]

    if args.format == "json":
        print(json.dumps(tail, indent=2, ensure_ascii=False))
    else:
        print(format_list_text(tail))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Log a manual edit to a Claude Code skill (append-only audit trail)"
    )
    parser.add_argument("name", help="Name of the skill")
    parser.add_argument(
        "--reason",
        help="Why the edit was made (required for logging an entry)"
    )
    parser.add_argument(
        "--source",
        choices=["manual", "from-bug", "from-trajectory", "from-review", "external"],
        default="manual",
        help="Where the edit originated (default: manual)"
    )
    parser.add_argument(
        "--scope", "-s",
        choices=["user", "project"],
        help="Scope to search (default: search both)"
    )
    parser.add_argument(
        "--ref",
        help="External reference: bug id, PR url, etc."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be logged without writing"
    )
    parser.add_argument(
        "--snapshot",
        action="store_true",
        help="Also save a snapshot of SKILL.md to .skill_snapshots/ for diffing"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Show recent log entries (default: last 20)"
    )
    parser.add_argument(
        "--since",
        help="When listing, only show entries newer than this duration (e.g. 7d, 12h, 30m, 60s)"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["text", "json"],
        default="text",
        help="Output format for --list (default: text)"
    )
    args = parser.parse_args()

    if args.list:
        return cmd_list(args)

    if not args.reason:
        parser.error("--reason is required when logging an entry (or pass --list to view history)")

    return cmd_log(args)


if __name__ == "__main__":
    sys.exit(main())
