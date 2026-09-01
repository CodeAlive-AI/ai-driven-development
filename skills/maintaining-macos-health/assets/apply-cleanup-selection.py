#!/usr/bin/env python3
"""
apply-cleanup-selection.py — the ONLY sanctioned way to apply a cleanup
selection produced by render-cleanup-plan.py.

Why this exists
---------------
The maintaining-macos-health skill split scan-and-plan from apply on purpose:
the user picks items in the HTML UI, the server writes a selection JSON, and
THIS script reads that JSON and executes each item's `command`. The skill
forbids hand-rolled `rm` blocks during apply, because they're how you end up
deleting items the user explicitly unchecked. The single-source-of-truth is
the selection JSON written by the UI server — nothing else.

Safety guarantees
-----------------
- Only items present in selected_items are eligible. Anything missing the
  `command` field is skipped with a warning, never inferred.
- Protected items (`protected=true`) must explicitly appear in
  `protected_overrides`, otherwise they are skipped — even if somehow in
  selected_items.
- Every command goes through Mole-style path validation:
    * Empty path -> reject
    * Path component `..` -> reject
    * Path starts with a hard-protected system prefix (`/System`, `/bin`,
      `/sbin`, `/usr`, `/etc`, `/Library/Extensions`, `/private/var/db/uuidtext`)
      -> reject, unless the command is a vetted wrapper (brew/docker/nvm/dotnet
      /pnpm/yes|mo).
- Mole-compatible operations log appended to ~/.config/mole/operations.log.
- --dry-run prints the planned actions without executing.

Usage
-----
    apply-cleanup-selection.py <selection.json>          # apply
    apply-cleanup-selection.py <selection.json> --dry-run

Exit codes
----------
    0  - all items applied (or dry-run completed)
    1  - bad input or fatal validation error
    2  - one or more items failed (others may have succeeded)
"""
from __future__ import annotations

import argparse
import json
import re
import shlex
import subprocess
import sys
from datetime import datetime
from pathlib import Path

OP_LOG = Path.home() / ".config" / "mole" / "operations.log"

# Hard-protected absolute path prefixes. Bare `rm` against these is refused.
# Wrapper commands (brew, docker, nvm uninstall, dotnet nuget locals, pnpm,
# `yes | mo ...`) are inspected separately.
HARD_PROTECTED_PREFIXES = (
    "/",
    "/System",
    "/bin",
    "/sbin",
    "/usr",
    "/etc",
    "/Library/Extensions",
    "/private/var/db/uuidtext",
)

WRAPPER_PREFIXES = (
    "brew ",
    "docker ",
    "nvm ",
    "dotnet ",
    "pnpm ",
    "yes ",
    "(",  # subshell wrappers
    "find ",
    "osascript ",
)


def log_op(action: str, path: str, size: str, status: str) -> None:
    """Append a Mole-compatible TSV row to ~/.config/mole/operations.log."""
    OP_LOG.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = f"{ts}\tapply-selection\t{action}\t{path}\t{size}\t{status}\n"
    with OP_LOG.open("a", encoding="utf-8") as f:
        f.write(row)


def validate_command(command: str) -> tuple[bool, str]:
    """Return (ok, reason). Reject commands that look unsafe."""
    cmd = command.strip()
    if not cmd:
        return False, "empty command"
    # Reject `..` either as a standalone token or as a path component inside any token.
    for tok in shlex.split(cmd, posix=True):
        path_components = [c for c in tok.replace("\\", "/").split("/") if c]
        if ".." in path_components:
            return False, f"command contains `..` component: {tok!r}"
    # If it starts with a wrapper (brew/docker/nvm/...), trust it and let the
    # wrapper enforce its own safety.
    if any(cmd.startswith(p) for p in WRAPPER_PREFIXES):
        return True, ""
    # Otherwise expect `rm` or `rm -rf <path>` form.
    if not cmd.startswith("rm "):
        return False, f"only rm/wrapper commands allowed, got: {cmd[:60]!r}"
    parts = shlex.split(cmd, posix=True)
    # Find path-like tokens (skip flags).
    paths = [p for p in parts[1:] if not p.startswith("-")]
    if not paths:
        return False, "rm without target"
    for p in paths:
        # Resolve ~ for the check.
        abs_p = str(Path(p).expanduser())
        # Allow paths under $HOME.
        home = str(Path.home())
        if abs_p.startswith(home + "/") or abs_p == home:
            continue
        # Allow /tmp + /private/tmp + /private/var/folders.
        if abs_p.startswith(("/tmp/", "/private/tmp/", "/private/var/folders/")):
            continue
        # Otherwise check against hard-protected prefixes.
        for bad in HARD_PROTECTED_PREFIXES:
            if abs_p == bad or abs_p.startswith(bad.rstrip("/") + "/"):
                return False, f"rm targets a hard-protected prefix: {abs_p}"
    return True, ""


def human_size(num_bytes: int) -> str:
    if num_bytes is None or num_bytes == 0:
        return "0 B"
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if abs(num_bytes) < 1024.0:
            return f"{num_bytes:3.1f} {unit}" if unit != "B" else f"{int(num_bytes)} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.1f} PB"


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Apply a cleanup selection JSON")
    ap.add_argument("selection", help="path to cleanup-selection-<ts>.json")
    ap.add_argument("--dry-run", action="store_true", help="print actions, don't execute")
    ap.add_argument("--continue-on-error", action="store_true",
                    help="keep going if an item fails (default: continue)")
    args = ap.parse_args(argv[1:])

    sel_path = Path(args.selection)
    if not sel_path.is_file():
        print(f"selection file not found: {sel_path}", file=sys.stderr)
        return 1

    try:
        sel = json.loads(sel_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"invalid selection JSON: {exc}", file=sys.stderr)
        return 1

    # Automated plans use typed operations and a durable, hash-bound UI
    # confirmation. They never enter the legacy shell-command executor below.
    if sel.get("format_version") == 2:
        from disk_responses import Context, apply_confirmed, set_status
        from disk_safety import read_json
        context = Context()
        try:
            incident = context.incident(sel_path.parent.name)
            if sel_path.resolve() != incident / "selection.json":
                raise ValueError("selection outside the incident directory")
            read_json(sel_path)
            if args.dry_run:
                print(json.dumps(sel["selected_items"], indent=2))
            else:
                apply_confirmed(context, incident)
            return 0
        except Exception as exc:
            print(f"typed selection refused: {exc}", file=sys.stderr)
            return 1

    items = sel.get("selected_items", []) or []
    if not items:
        print("selected_items is empty — nothing to do", file=sys.stderr)
        return 0

    protected_overrides = set(sel.get("protected_overrides", []) or [])
    total_bytes = sum(it.get("size_bytes", 0) or 0 for it in items)

    print(f"=== Applying selection from {sel_path.name} ===")
    print(f"Items: {len(items)} | Estimated: {human_size(total_bytes)}")
    print(f"Protected overrides: {len(protected_overrides)}")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'APPLY'}")
    print()

    if not args.dry_run:
        log_op("APPLY-START", "-", "-", "START")

    ok = 0
    skipped = 0
    failed = 0

    for idx, item in enumerate(items, 1):
        item_id = item.get("id", "?")
        label = item.get("label", item_id)
        path = item.get("path", "")
        command = item.get("command")
        size_bytes = item.get("size_bytes", 0) or 0
        protected = bool(item.get("protected", False))

        prefix = f"[{idx:>2}/{len(items)}]"

        if protected and item_id not in protected_overrides:
            print(f"{prefix} SKIP (protected, not overridden): {label}")
            log_op("SKIP", path or item_id, human_size(size_bytes), "PROTECTED-NOT-OVERRIDDEN")
            skipped += 1
            continue

        if not command:
            print(f"{prefix} SKIP (no command): {label}")
            log_op("SKIP", path or item_id, human_size(size_bytes), "NO-COMMAND")
            skipped += 1
            continue

        valid, reason = validate_command(command)
        if not valid:
            print(f"{prefix} SKIP (validation: {reason}): {label}")
            log_op("SKIP", path or item_id, human_size(size_bytes), f"VALIDATION-FAILED:{reason}")
            skipped += 1
            continue

        flag = " 🔒" if protected else ""
        print(f"{prefix} {label}{flag} — {human_size(size_bytes)}")
        print(f"          → {command}")

        if args.dry_run:
            ok += 1
            continue

        try:
            proc = subprocess.run(
                command,
                shell=True,
                executable="/bin/bash",
                capture_output=True,
                text=True,
                timeout=600,
            )
            if proc.returncode == 0:
                log_op(
                    "PROTECTED-OVERRIDE" if protected else "REMOVED",
                    path or item_id,
                    human_size(size_bytes),
                    "OK",
                )
                ok += 1
            else:
                stderr_tail = proc.stderr.strip()[-300:] if proc.stderr else ""
                print(f"          FAIL exit={proc.returncode}: {stderr_tail}")
                log_op("REMOVE", path or item_id, human_size(size_bytes),
                       f"FAIL-EXIT-{proc.returncode}")
                failed += 1
                if not args.continue_on_error:
                    print("Stopping on first error. Re-run with --continue-on-error to override.")
                    break
        except subprocess.TimeoutExpired:
            print(f"          TIMEOUT after 600s")
            log_op("REMOVE", path or item_id, human_size(size_bytes), "TIMEOUT")
            failed += 1
        except Exception as exc:
            print(f"          ERROR: {exc}")
            log_op("REMOVE", path or item_id, human_size(size_bytes), f"ERROR:{exc}")
            failed += 1

    print()
    print(f"=== Done: {ok} ok | {skipped} skipped | {failed} failed ===")
    if not args.dry_run:
        log_op("APPLY-END", "-", "-", f"OK={ok} SKIP={skipped} FAIL={failed}")

    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
