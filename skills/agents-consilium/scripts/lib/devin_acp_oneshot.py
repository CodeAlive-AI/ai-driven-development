#!/usr/bin/env python3
"""One-shot Devin runner over `devin acp` (JSON-RPC 2.0 NDJSON on stdio).

Why ACP instead of `devin -p`: in print mode a denied or confirmation-required
tool call silently cancels the whole session (no final text), so read-only
review cannot be enforced via config deny rules. `devin acp --agent-type review`
is a read-only + shell agent with no write/edit tools at all, so the boundary
holds by construction. Delegate (yolo) uses the default agent type plus
`session/set_mode bypass`.

Every inbound JSON-RPC line (notifications, server requests, and the prompt
response) is echoed verbatim to stdout so backend_run.sh can tee it into
raw/<agent>.jsonl and feed normalize_stream.py. Outbound client traffic is not
echoed.

ACP_BACKEND must not reach the child: inside Devin Desktop it is inherited as
"windsurf" and the CLI reports "Not logged in".
"""
from __future__ import annotations

import argparse
import os
import queue
import sys
from typing import Any, Dict, Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from steer.jsonrpc import JsonRpcProcess  # noqa: E402
from steer.util import kill_process_group  # noqa: E402


class _StdoutWire:
    """Raw-wire sink that mirrors inbound lines to stdout (skips outbound)."""

    def write(self, s: str) -> int:
        if not s.startswith(">>"):
            sys.stdout.write(s)
            sys.stdout.flush()
        return len(s)

    def flush(self) -> None:
        sys.stdout.flush()

    def close(self) -> None:
        pass


def _pick_allow_option(options: Any) -> Optional[str]:
    if not isinstance(options, list):
        return None
    fallback = None
    for opt in options:
        if not isinstance(opt, dict):
            continue
        kind = str(opt.get("kind") or "")
        if kind == "allow_once":
            return str(opt.get("optionId") or "allow_once")
        if kind.startswith("allow") and fallback is None:
            fallback = str(opt.get("optionId") or "")
    return fallback


def _on_server_request(msg: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    method = msg.get("method") or ""
    rid = msg.get("id")
    if method == "session/request_permission":
        option_id = _pick_allow_option((msg.get("params") or {}).get("options"))
        if option_id is None:
            return None
        return {
            "jsonrpc": "2.0",
            "id": rid,
            "result": {"outcome": {"outcome": "selected", "optionId": option_id}},
        }
    if method == "elicitation/create":
        return {"jsonrpc": "2.0", "id": rid, "result": {"action": "cancel"}}
    return None


def _stderr_tail(rpc: JsonRpcProcess, limit: int = 30) -> str:
    tail = rpc.stderr_lines[-limit:]
    return "\n".join(tail)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--binary", default="devin")
    ap.add_argument("--model", default="")
    ap.add_argument("--cwd", required=True)
    ap.add_argument("--access", choices=["readonly", "yolo"], required=True)
    ap.add_argument("--prompt-file", required=True)
    ap.add_argument("--web", choices=["true", "false"], default="false",
                    help="reserved; the review agent type governs the tool surface")
    args = ap.parse_args()

    try:
        with open(args.prompt_file, encoding="utf-8") as f:
            prompt_text = f.read()
    except OSError as e:
        print(f"devin acp one-shot: cannot read prompt file: {e}", file=sys.stderr)
        return 1

    argv = [args.binary, "acp"]
    if args.access == "readonly":
        argv += ["--agent-type", "review"]
    if args.model:
        argv += ["--model", args.model]

    env = dict(os.environ)
    env.pop("ACP_BACKEND", None)

    rpc = JsonRpcProcess(
        argv,
        cwd=args.cwd,
        env=env,
        on_server_request=_on_server_request,
    )
    rpc.set_raw_out_fp(_StdoutWire())

    exit_code = 1
    reason = ""
    try:
        rpc.start()
        rpc.request(
            "initialize",
            {
                "protocolVersion": 1,
                "clientCapabilities": {
                    "fs": {"readTextFile": False, "writeTextFile": False},
                    "terminal": False,
                },
                "clientInfo": {"name": "agents-consilium", "version": "1.0.0"},
            },
            timeout=60.0,
        )
        result = rpc.request(
            "session/new", {"cwd": args.cwd, "mcpServers": []}, timeout=60.0
        )
        session_id = (result or {}).get("sessionId")
        if not session_id:
            raise RuntimeError(f"session/new missing sessionId: {result}")
        if args.access == "yolo":
            try:
                rpc.request(
                    "session/set_mode",
                    {"sessionId": session_id, "modeId": "bypass"},
                    timeout=30.0,
                )
            except Exception as e:
                print(
                    f"devin acp one-shot: set_mode bypass failed ({e}); continuing",
                    file=sys.stderr,
                )
        rid, q = rpc.start_request(
            "session/prompt",
            {
                "sessionId": session_id,
                "prompt": [{"type": "text", "text": prompt_text}],
            },
        )
        # Poll the response queue so a dead child cannot hang the run forever.
        # (await_response pops the pending entry on timeout, so wait on the
        # queue directly instead of looping over it.)
        prompt_result: Optional[Dict[str, Any]] = None
        while True:
            try:
                resp = q.get(timeout=1.0)
            except queue.Empty:
                rc = rpc.poll_exit()
                if rc is not None:
                    rpc.drop_pending(rid)
                    reason = f"devin acp exited {rc} before prompt response"
                    exit_code = 1
                    break
                continue
            rpc.drop_pending(rid)
            if "error" in resp:
                reason = f"JSON-RPC error: {resp['error']}"
                exit_code = 1
            else:
                prompt_result = resp.get("result")
            break
        if isinstance(prompt_result, dict):
            stop = str(prompt_result.get("stopReason") or "")
            if stop == "end_turn":
                exit_code = 0
            elif stop in ("cancelled", "canceled"):
                exit_code = 130
                reason = "stopReason=cancelled"
            else:
                exit_code = 1
                reason = f"stopReason={stop or 'missing'}"
    except Exception as e:
        reason = str(e)
        exit_code = 1
    finally:
        pid = rpc.pid()
        try:
            rpc.terminate()
        except Exception:
            pass
        if pid:
            try:
                kill_process_group(pid, timeout=3.0)
            except Exception:
                pass

    if exit_code != 0:
        tail = _stderr_tail(rpc)
        parts = [f"devin acp one-shot failed: {reason or 'unknown'}"]
        if tail:
            parts.append(tail)
        print("\n".join(parts), file=sys.stderr)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
