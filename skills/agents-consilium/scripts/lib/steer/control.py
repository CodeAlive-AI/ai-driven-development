"""Client-side steer / status / cancel against the filesystem mailbox."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Optional

from .mailbox import Mailbox, MailboxError
from .registry import Registry, RegistryError, TERMINAL_STATUSES
from .util import preview_text, progress


def cmd_steer(args: argparse.Namespace) -> int:
    reg = Registry(Path(args.registry_root) if args.registry_root else None)
    content = args.guidance or ""
    if args.prompt_file:
        path = Path(args.prompt_file)
        if not path.is_file():
            sys.stderr.write(f"Error: prompt file not found: {path}\n")
            return 5
        content = path.read_text(encoding="utf-8")
    if not content and not sys.stdin.isatty():
        content = sys.stdin.read()
    if not content:
        sys.stderr.write("Error: no guidance provided\n")
        return 5

    mode = args.mode or "auto"
    if mode not in ("auto", "queue", "interrupt"):
        sys.stderr.write("Error: --mode must be auto|queue|interrupt\n")
        return 5

    client_id = args.client_id or None
    # Serialize validate_active + enqueue with supervisor terminal transition.
    try:
        with reg.with_run_lock(args.run_id):
            reg.validate_active(args.run_id)
            run_dir = reg.run_path(args.run_id)
            mb = Mailbox(run_dir)
            if mb.is_closed():
                raise RegistryError(
                    f"run is terminal (mailbox closed); cannot steer: {args.run_id}",
                    exit_code=5,
                )
            msg = mb.enqueue(
                kind="steer",
                content=content,
                mode=mode,
                client_id=client_id,
            )
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code
    except MailboxError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code

    progress(
        "steer",
        f"run_id={args.run_id}",
        f"mailbox_accepted client_id={msg['client_id']}",
        f"seq={msg['seq']}",
        f"mode={mode}",
        f"status={msg['status']}",
    )
    # Distinguish mailbox accepted from protocol delivery (status still accepted)
    out = {
        "run_id": args.run_id,
        "client_id": msg["client_id"],
        "client_id_safe": msg.get("client_id_safe"),
        "seq": msg["seq"],
        "mailbox_status": msg["status"],
        "mode": mode,
        "content_hash": msg.get("content_hash"),
        "note": "mailbox accepted only; poll status for delivery_class/protocol ack",
    }
    if args.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        print(
            f"accepted client_id={msg['client_id']} seq={msg['seq']} "
            f"mailbox_status={msg['status']} (not yet protocol-delivered)"
        )
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    reg = Registry(Path(args.registry_root) if args.registry_root else None)
    try:
        meta = reg.load_meta(args.run_id)
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code
    try:
        state = reg.load_state(args.run_id)
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code

    run_dir = reg.run_path(args.run_id)
    mb = Mailbox(run_dir)
    messages = mb.list_messages(after_seq=0)
    steers = []
    for m in messages:
        if m.get("kind") == "steer" or m.get("kind") == "invalid":
            steers.append(
                {
                    "seq": m.get("seq"),
                    "client_id": m.get("client_id"),
                    "client_id_safe": m.get("client_id_safe"),
                    "mailbox_status": m.get("status"),
                    "delivery_class": m.get("delivery_class"),
                    "backend_ack": m.get("backend_ack"),
                    "error": m.get("error"),
                    "mode": m.get("mode"),
                    "content_hash": m.get("content_hash"),
                    "updated_at": m.get("updated_at"),
                }
            )

    payload: Dict[str, Any] = {
        "run_id": args.run_id,
        "status": meta.get("status"),
        "agent_id": meta.get("agent_id"),
        "backend": meta.get("backend"),
        "model": meta.get("model"),
        "pid": meta.get("pid"),
        "child_pid": meta.get("child_pid"),
        "exit_code": meta.get("exit_code"),
        "error": meta.get("error"),
        "started_at": meta.get("started_at"),
        "updated_at": meta.get("updated_at"),
        "finished_at": meta.get("finished_at"),
        "mailbox_closed": mb.is_closed(),
        "steers": steers,
        "state": state,
    }
    if meta.get("status") in TERMINAL_STATUSES:
        final = run_dir / "final.txt"
        if final.is_file():
            # Explicit preview label — full body remains in final.txt artifact
            payload["final_preview"] = preview_text(
                final.read_text(encoding="utf-8"), 500
            )
            payload["final_preview_note"] = "truncated status preview only; full text in final.txt"

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(f"run_id={args.run_id} status={meta.get('status')} backend={meta.get('backend')}")
        print(f"agent={meta.get('agent_id')} pid={meta.get('pid')} child={meta.get('child_pid')}")
        if meta.get("error"):
            print(f"error={meta.get('error')}")
        for s in steers:
            print(
                f"  steer seq={s.get('seq')} client_id={s.get('client_id')} "
                f"mailbox={s.get('mailbox_status')} class={s.get('delivery_class')} "
                f"ack={s.get('backend_ack')} err={s.get('error')}"
            )
    return 0


def cmd_cancel(args: argparse.Namespace) -> int:
    reg = Registry(Path(args.registry_root) if args.registry_root else None)
    try:
        with reg.with_run_lock(args.run_id):
            reg.request_cancel(args.run_id)
            run_dir = reg.run_path(args.run_id)
            mb = Mailbox(run_dir)
            # Cancel may still be useful while closing; allow when not fully closed yet.
            if not mb.is_closed():
                mb.enqueue(kind="cancel", content="", mode="auto", allow_when_closed=False)
    except RegistryError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code
    except MailboxError as e:
        sys.stderr.write(f"Error: {e}\n")
        return e.exit_code
    progress("steer", f"run_id={args.run_id}", "cancel_enqueued")
    if args.json:
        print(json.dumps({"run_id": args.run_id, "cancel": "requested"}, indent=2))
    else:
        print(f"cancel requested for {args.run_id}")
    return 0


def main(argv: Optional[list] = None) -> int:
    p = argparse.ArgumentParser(prog="consilium-steer-control")
    p.add_argument("--registry-root", default=os.environ.get("CONSILIUM_STEER_DIR", ""))
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("steer")
    s.add_argument("run_id")
    s.add_argument("guidance", nargs="?", default="")
    s.add_argument("--mode", default="auto", choices=["auto", "queue", "interrupt"])
    s.add_argument("--prompt-file", default="")
    s.add_argument("--client-id", default="")
    s.add_argument("--json", action="store_true")
    s.set_defaults(func=cmd_steer)

    st = sub.add_parser("status")
    st.add_argument("run_id")
    st.add_argument("--json", action="store_true")
    st.set_defaults(func=cmd_status)

    c = sub.add_parser("cancel")
    c.add_argument("run_id")
    c.add_argument("--json", action="store_true")
    c.set_defaults(func=cmd_cancel)

    args = p.parse_args(argv)
    if not args.registry_root:
        args.registry_root = ""
    # empty --client-id → None so mailbox generates one
    if hasattr(args, "client_id") and args.client_id == "":
        args.client_id = None
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
