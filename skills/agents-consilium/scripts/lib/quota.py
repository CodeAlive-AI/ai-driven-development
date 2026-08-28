#!/usr/bin/env python3
"""Read Codex and Grok subscription quota without consuming model turns."""

from __future__ import annotations

import argparse
import json
import os
import re
import select
import shlex
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import PurePosixPath
from typing import Any


class ConsiliumArgumentParser(argparse.ArgumentParser):
    def error(self, message: str) -> None:
        self.print_usage(sys.stderr)
        self.exit(5, f"{self.prog}: error: {message}\n")


def _iso_from_epoch(value: int | float | None) -> str | None:
    if value is None:
        return None
    return datetime.fromtimestamp(value, tz=timezone.utc).isoformat().replace("+00:00", "Z")


def _window(value: dict[str, Any] | None) -> dict[str, Any] | None:
    if not value:
        return None
    used = float(value["usedPercent"])
    return {
        "usedPercent": used,
        "remainingPercent": max(0.0, 100.0 - used),
        "windowDurationMins": value.get("windowDurationMins"),
        "resetsAt": _iso_from_epoch(value.get("resetsAt")),
    }


def normalize_codex(result: dict[str, Any]) -> dict[str, Any]:
    historical = result.get("rateLimits") or {}
    buckets = result.get("rateLimitsByLimitId") or {"codex": historical}
    limits = {}
    for limit_id, snapshot in buckets.items():
        limits[limit_id] = {
            "name": snapshot.get("limitName"),
            "primary": _window(snapshot.get("primary")),
            "secondary": _window(snapshot.get("secondary")),
        }
    return {
        "ok": True,
        "source": "codex-app-server:account/rateLimits/read",
        "planType": historical.get("planType"),
        "limits": limits,
        "resetCreditsAvailable": (result.get("rateLimitResetCredits") or {}).get("availableCount"),
    }


def parse_grok_screen(screen: str) -> dict[str, Any]:
    used_match = re.search(r"Weekly limit:\s*(\d+(?:\.\d+)?)%", screen, re.IGNORECASE)
    reset_match = re.search(r"Next reset:\s*([^\r\n]+)", screen, re.IGNORECASE)
    if not used_match or not reset_match:
        raise RuntimeError("Grok /usage output lacks Weekly limit or Next reset")
    used = float(used_match.group(1))
    return {
        "ok": True,
        "source": "grok-build-tui:/usage",
        "usedPercent": used,
        "remainingPercent": max(0.0, 100.0 - used),
        "nextResetDisplay": reset_match.group(1).strip(),
    }


def read_codex(timeout: float = 15.0) -> dict[str, Any]:
    binary = os.environ.get("CONSILIUM_BIN_CODEX", "codex")
    process = subprocess.Popen(
        [binary, "app-server"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )
    assert process.stdin is not None and process.stdout is not None
    deadline = time.monotonic() + timeout
    try:
        process.stdin.write(json.dumps({
            "id": 1,
            "method": "initialize",
            "params": {"clientInfo": {"name": "agents-consilium-quota", "version": "1.0.0"}},
        }) + "\n")
        process.stdin.flush()
        initialized = False
        while time.monotonic() < deadline:
            ready, _, _ = select.select([process.stdout], [], [], min(0.5, deadline - time.monotonic()))
            if not ready:
                if process.poll() is not None:
                    break
                continue
            line = process.stdout.readline()
            if not line:
                break
            try:
                message = json.loads(line)
            except json.JSONDecodeError:
                continue
            if message.get("id") == 1 and not initialized:
                initialized = True
                process.stdin.write(json.dumps({"method": "initialized"}) + "\n")
                process.stdin.write(json.dumps({"id": 2, "method": "account/rateLimits/read"}) + "\n")
                process.stdin.flush()
            elif message.get("id") == 2:
                if message.get("error"):
                    raise RuntimeError(message["error"].get("message", "Codex quota query failed"))
                return normalize_codex(message["result"])
        stderr = process.stderr.read() if process.stderr and process.poll() is not None else ""
        raise RuntimeError(f"Codex quota query timed out or exited: {stderr.strip()}")
    finally:
        process.terminate()
        try:
            process.wait(timeout=2)
        except subprocess.TimeoutExpired:
            process.kill()


def _grok_remote_script(cwd: str) -> str:
    quoted_cwd = shlex.quote(cwd)
    return f'''set -eu
session="consilium-quota-$$"
cleanup() {{ tmux kill-session -t "$session" 2>/dev/null || true; }}
trap cleanup EXIT INT TERM
tmux new-session -d -s "$session" -x 180 -y 55
tmux set-option -t "$session" remain-on-exit on
tmux send-keys -t "$session" "cd {quoted_cwd} && grok --no-alt-screen" Enter
sleep 5
screen="$(tmux capture-pane -p -J -t "$session" -S -80)"
case "$screen" in
  *'Do you trust the contents of this directory?'*) tmux send-keys -t "$session" y; sleep 4 ;;
esac
tmux send-keys -t "$session" /usage Enter
sleep 5
tmux capture-pane -p -J -t "$session" -S -100
'''


def _read_grok_once(host: str, cwd: str, timeout: float) -> dict[str, Any]:
    completed = subprocess.run(
        ["ssh", "-T", "-o", "BatchMode=yes", host, "bash", "-s"],
        input=_grok_remote_script(cwd),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    if completed.returncode != 0:
        detail = completed.stderr.strip() or f"remote exit {completed.returncode}"
        raise RuntimeError(f"Grok quota transport failed: {detail}")
    return parse_grok_screen(completed.stdout)


def read_grok(timeout: float = 25.0) -> dict[str, Any]:
    host = os.environ.get("CONSILIUM_GROK_QUOTA_SSH_HOST", "grok-aws")
    cwd = os.environ.get("CONSILIUM_GROK_QUOTA_CWD", "/mnt/codealive/workspaces")
    if not re.fullmatch(r"[A-Za-z0-9._-]+", host):
        raise RuntimeError("CONSILIUM_GROK_QUOTA_SSH_HOST must be a safe SSH alias")
    if not PurePosixPath(cwd).is_absolute() or "\x00" in cwd:
        raise RuntimeError("CONSILIUM_GROK_QUOTA_CWD must be an absolute remote path")
    errors = []
    for attempt in range(2):
        try:
            return _read_grok_once(host, cwd, timeout)
        except (RuntimeError, subprocess.TimeoutExpired) as error:
            errors.append(str(error))
            if attempt == 0:
                time.sleep(1)
    raise RuntimeError(f"Grok quota query failed twice: {'; '.join(errors)}")


def main() -> int:
    parser = ConsiliumArgumentParser(prog="consilium quota")
    parser.add_argument("provider", nargs="?", choices=("all", "codex", "grok"), default="all")
    args = parser.parse_args()
    readers = {"codex": read_codex, "grok": read_grok}
    selected = readers if args.provider == "all" else {args.provider: readers[args.provider]}
    providers: dict[str, Any] = {}
    successes = 0
    for name, reader in selected.items():
        try:
            providers[name] = reader()
            successes += 1
        except Exception as error:  # keep the other provider's result
            providers[name] = {"ok": False, "error": str(error)}
    payload = {
        "schemaVersion": 1,
        "checkedAt": datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z"),
        "providers": providers,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    if successes == len(selected):
        return 0
    return 2 if successes else 3


if __name__ == "__main__":
    sys.exit(main())
