"""Steerable delegate supervisor: one adapter, mailbox consumer, durable state."""
from __future__ import annotations

import os
import signal
import sys
import time
import traceback
from pathlib import Path
from typing import Any, Dict, Optional, Set

from .adapters import make_adapter
from .config_loader import agent_settings
from .mailbox import Mailbox, MailboxError
from .registry import Registry, RegistryError, TERMINAL_STATUSES
from .util import (
    DIR_MODE,
    append_jsonl,
    atomic_write_text,
    ensure_dir,
    kill_process_group,
    preview_text,
    progress,
    secure_touch,
    utc_now_iso,
)

# Success-path mailbox ranks for async steer_ack reconciliation.
# Higher wins; equal rank allows evidence upgrade. Never demote.
_STEER_SUCCESS_RANK = {
    "accepted": 0,
    "delivering": 1,
    "request_sent": 2,
    "queued": 3,
    "applied": 10,
    "delivered": 10,
}
_STEER_FAILURE_TERMINAL = frozenset({"failed", "rejected"})
# Evidence preference when status rank is equal (higher = better confirmation).
_EVIDENCE_RANK = {
    "concurrent_prompt_request_in_flight": 1,
    "prompt_request_written": 1,
    "backend_queue_entry": 2,
    "promptId_notification_meta": 5,
    "running_prompt_id": 6,
    "prompt_result": 7,
    "prompt_complete": 8,
}


class Supervisor:
    def __init__(
        self,
        *,
        agent_id: str,
        task: str,
        cwd: str,
        artifacts_dir: str,
        registry: Optional[Registry] = None,
    ):
        self.agent_id = agent_id
        self.task = task
        self.cwd = cwd
        self.artifacts_dir = artifacts_dir
        self.registry = registry or Registry()
        self.run_id: Optional[str] = None
        self.mailbox: Optional[Mailbox] = None
        self.adapter = None
        self._last_seq = 0
        self._processed: Set[int] = set()
        self._shutting_down = False
        self._terminal = False

    def run(self) -> int:
        agent, backend, model, binary = agent_settings(self.agent_id)
        effort = agent.get("effort") or ""

        # Resolve protocol artifacts dir before create_run so meta is honest.
        # Never use project cwd when archival is disabled / path is empty/".".
        self.artifacts_dir = self._resolve_artifacts_dir(self.artifacts_dir)

        # Early run id before any long work
        self.run_id = self.registry.create_run(
            agent_id=self.agent_id,
            backend=backend,
            model=model,
            cwd=self.cwd,
            artifacts_dir=self.artifacts_dir,
            extra={"task_hash_prefix": _prefix_hash(self.task)},
        )
        progress("steer", f"run_id={self.run_id}", f"agent={self.agent_id}", f"backend={backend}")
        # Also print bare run_id line for easy capture
        sys.stderr.write(f"run_id={self.run_id}\n")
        sys.stderr.flush()

        run_dir = self.registry.run_path(self.run_id)
        self.mailbox = Mailbox(run_dir)

        # If caller passed a placeholder (empty / "." / cwd) we relocate protocol
        # artifacts under the private registry run dir (0700) and update meta.
        if self._artifacts_need_private_home(self.artifacts_dir):
            private = run_dir / "artifacts"
            ensure_dir(private, DIR_MODE)
            self.artifacts_dir = str(private)
            self.registry.update_meta(self.run_id, artifacts_dir=self.artifacts_dir)

        # Ensure artifact dirs (protocol artifacts always on for steerable observability)
        for sub in ("raw", "normalized", "final", "turns", "control"):
            ensure_dir(Path(self.artifacts_dir) / sub, DIR_MODE)
        secure_touch(run_dir / "audit.jsonl")

        self.registry.update_meta(
            self.run_id,
            status="running",
            pid=os.getpid(),
            backend_binary=binary,
            artifacts_dir=self.artifacts_dir,
        )
        self.registry.update_state(self.run_id, status="running")

        def _handle_sig(signum, frame):
            self._shutting_down = True
            progress("steer", f"run_id={self.run_id}", f"signal={signum}")

        signal.signal(signal.SIGTERM, _handle_sig)
        signal.signal(signal.SIGINT, _handle_sig)

        try:
            self.adapter = make_adapter(
                backend,
                binary=binary,
                model=model,
                effort=effort,
                cwd=self.cwd,
                artifacts_dir=self.artifacts_dir,
                agent_id=self.agent_id,
            )
            self.adapter.start(self.task)
            child = self.adapter.child_pid()
            if child:
                self.registry.update_meta(self.run_id, child_pid=child)
            progress("steer", f"run_id={self.run_id}", "adapter_started")
            return self._loop()
        except Exception as e:
            progress("steer", f"run_id={self.run_id}", f"failed={e}")
            append_jsonl(
                run_dir / "audit.jsonl",
                {
                    "ts": utc_now_iso(),
                    "event": "supervisor_error",
                    "error": str(e),
                    "trace": traceback.format_exc(),
                },
            )
            self._finalize(status="failed", exit_code=1, error=str(e))
            return 1
        finally:
            self._cleanup_adapter()

    def _loop(self) -> int:
        assert self.adapter and self.mailbox and self.run_id
        last_progress = time.time()
        while not self._shutting_down:
            # Control cancel file
            if self.registry.cancel_requested(self.run_id):
                progress("steer", f"run_id={self.run_id}", "cancel_file")
                self.adapter.cancel()
                self._finalize(status="cancelled", exit_code=130)
                return 130

            # Drain mailbox first so steers land before we observe a terminal idle
            self._drain_mailbox()

            # Drain adapter events → progress + artifacts
            for ev in self.adapter.poll_events():
                self._handle_event(ev)
                last_progress = time.time()

            if self.adapter.is_done():
                # One more mailbox pass for late writers racing completion,
                # still under non-terminal meta so run-lock enqueue can succeed.
                self._drain_mailbox()
                text = self.adapter.final_text()
                code = self.adapter.exit_code()
                # Cancel path may have set _done without success text
                if getattr(self.adapter, "_cancelled", False):
                    status = "cancelled"
                    code = 130 if code == 0 else code
                else:
                    status = "completed" if code == 0 else "failed"
                self._finalize(status=status, exit_code=code, final_text=text)
                return code

            # Heartbeat
            if time.time() - last_progress > 15:
                progress("steer", f"run_id={self.run_id}", "alive")
                last_progress = time.time()
                self.registry.update_meta(self.run_id)  # touch updated_at

            time.sleep(0.05)

        # shutting down
        self.adapter.cancel()
        self._finalize(status="cancelled", exit_code=130)
        return 130

    def _drain_mailbox(self) -> None:
        assert self.mailbox
        for msg in self.mailbox.list_messages(after_seq=self._last_seq):
            seq = int(msg.get("seq") or 0)
            if seq <= 0:
                continue
            if seq in self._processed:
                # Already finished; safe to advance cursor past it.
                self._last_seq = max(self._last_seq, seq)
                continue
            status = msg.get("status")
            # Only accept never-started messages. delivering is in-progress in this
            # process and always gets a terminal outcome from _process_mailbox_msg
            # or from finalize.fail_open_messages.
            if status not in (None, "accepted"):
                self._processed.add(seq)
                self._last_seq = max(self._last_seq, seq)
                continue
            try:
                self._process_mailbox_msg(msg)
            except Exception as e:
                # Any exception after/during delivery must leave a terminal failed
                # outcome — never orphan "delivering"/"accepted" — then advance.
                try:
                    self.mailbox.update_message(
                        seq,
                        status="failed",
                        error=f"supervisor exception: {e}",
                    )
                except Exception:
                    pass
                append_jsonl(
                    self.registry.run_path(self.run_id) / "audit.jsonl",  # type: ignore[arg-type]
                    {
                        "ts": utc_now_iso(),
                        "event": "mailbox_process_exception",
                        "seq": seq,
                        "error": str(e),
                        "trace": traceback.format_exc(),
                    },
                )
            self._processed.add(seq)
            # Advance cursor only after processing completes (success or failed).
            self._last_seq = max(self._last_seq, seq)

    def _handle_event(self, ev) -> None:
        assert self.run_id
        run_dir = self.registry.run_path(self.run_id)
        # Full payload in normalized artifacts — never truncate data field.
        record: Dict[str, Any] = {
            "ts": utc_now_iso(),
            "kind": ev.kind,
            "data": ev.data or "",
        }
        if ev.raw is not None:
            record["raw"] = ev.raw
        append_jsonl(
            Path(self.artifacts_dir) / "normalized" / f"{self.agent_id}.jsonl",
            record,
        )
        if ev.kind == "text" and ev.data:
            progress("event", f"run_id={self.run_id}", "text", preview_text(ev.data, 80))
        elif ev.kind == "thought":
            progress("event", f"run_id={self.run_id}", "thought", preview_text(ev.data, 60))
        elif ev.kind == "steer_ack":
            progress("event", f"run_id={self.run_id}", "steer_ack", preview_text(ev.data, 80))
            self._reconcile_steer_ack(ev)
        elif ev.kind in (
            "turn_started",
            "turn_completed",
            "prompt_complete",
            "progress",
            "user_replay",
        ):
            progress("event", f"run_id={self.run_id}", ev.kind, preview_text(ev.data, 60))
            # prompt_complete also carries promptId — reconcile if adapter did not
            # already emit a dedicated steer_ack (older adapters / other backends).
            if ev.kind == "prompt_complete" and isinstance(ev.raw, dict):
                pid = ev.raw.get("promptId") or ""
                if pid:
                    self._reconcile_steer_ack_fields(
                        prompt_id=pid,
                        status="applied",
                        evidence="prompt_complete",
                        raw=ev.raw,
                    )
        elif ev.kind == "error":
            progress("event", f"run_id={self.run_id}", "error", preview_text(ev.data, 120))
        elif ev.kind == "done":
            progress("event", f"run_id={self.run_id}", "done", preview_text(ev.data, 80))
        # Audit keeps a short preview only (status/debug); full body is in normalized.
        append_jsonl(
            run_dir / "audit.jsonl",
            {
                "ts": utc_now_iso(),
                "event": "adapter_event",
                "kind": ev.kind,
                "data_preview": preview_text(ev.data, 200),
            },
        )

    def _reconcile_steer_ack(self, ev) -> None:
        raw = ev.raw if isinstance(ev.raw, dict) else {}
        prompt_id = raw.get("promptId") or ""
        status = raw.get("status") or ""
        evidence = raw.get("evidence") or ""
        if not prompt_id or not status:
            return
        self._reconcile_steer_ack_fields(
            prompt_id=prompt_id,
            status=status,
            evidence=evidence,
            raw=raw,
        )

    def _reconcile_steer_ack_fields(
        self,
        *,
        prompt_id: str,
        status: str,
        evidence: str,
        raw: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Find mailbox record by saved meta.promptId and safely advance status/evidence."""
        assert self.mailbox and self.run_id
        if not prompt_id:
            return
        msg = self._find_mailbox_by_prompt_id(prompt_id)
        if not msg:
            return
        seq = int(msg.get("seq") or 0)
        if not seq:
            return
        old_status = msg.get("status") or ""
        old_evidence = msg.get("backend_ack") or ""
        if not self._can_advance_steer_status(old_status, status, old_evidence, evidence):
            return
        client_id = msg.get("client_id") or f"seq_{seq}"
        # Preserve delivery_class; only advance protocol status/evidence.
        fields: Dict[str, Any] = {
            "status": status if self._status_rank(status) >= self._status_rank(old_status) else old_status,
            "backend_ack": evidence or old_evidence,
        }
        # Never demote: if ranks equal keep higher-rank status name preference applied>queued
        if self._status_rank(status) > self._status_rank(old_status):
            fields["status"] = status
        elif self._status_rank(status) == self._status_rank(old_status):
            fields["status"] = old_status if old_status else status
            # Prefer stronger evidence
            if self._evidence_rank(evidence) >= self._evidence_rank(old_evidence):
                fields["backend_ack"] = evidence or old_evidence
            else:
                fields["backend_ack"] = old_evidence
        else:
            return
        # Failure terminals already blocked in _can_advance
        try:
            updated = self.mailbox.update_message(seq, **fields)
        except MailboxError:
            return
        # Mirror into state.steers
        state = self.registry.load_state(self.run_id)
        steers = dict(state.get("steers") or {})
        prev = dict(steers.get(client_id) or {})
        prev.update(
            {
                "seq": seq,
                "status": updated.get("status"),
                "delivery_class": updated.get("delivery_class") or prev.get("delivery_class"),
                "evidence": updated.get("backend_ack"),
                "error": updated.get("error") or prev.get("error") or "",
                "updated_at": utc_now_iso(),
            }
        )
        steers[client_id] = prev
        self.registry.update_state(self.run_id, steers=steers)
        append_jsonl(
            self.registry.run_path(self.run_id) / "audit.jsonl",
            {
                "ts": utc_now_iso(),
                "event": "steer_ack_reconcile",
                "client_id": client_id,
                "promptId": prompt_id,
                "old_status": old_status,
                "new_status": updated.get("status"),
                "old_evidence": old_evidence,
                "new_evidence": updated.get("backend_ack"),
                "raw_keys": sorted((raw or {}).keys()),
            },
        )
        progress(
            "steer",
            f"run_id={self.run_id}",
            f"reconcile client_id={client_id}",
            f"promptId={prompt_id}",
            f"{old_status}->{updated.get('status')}",
            f"evidence={updated.get('backend_ack')}",
        )

    def _find_mailbox_by_prompt_id(self, prompt_id: str) -> Optional[Dict[str, Any]]:
        assert self.mailbox
        for msg in self.mailbox.list_messages(after_seq=0):
            meta = msg.get("meta") or {}
            if isinstance(meta, dict) and meta.get("promptId") == prompt_id:
                return msg
        return None

    @staticmethod
    def _status_rank(status: str) -> int:
        if status in _STEER_FAILURE_TERMINAL:
            return 100
        return _STEER_SUCCESS_RANK.get(status or "", -1)

    @staticmethod
    def _evidence_rank(evidence: str) -> int:
        return _EVIDENCE_RANK.get(evidence or "", 0)

    def _can_advance_steer_status(
        self,
        old_status: str,
        new_status: str,
        old_evidence: str,
        new_evidence: str,
    ) -> bool:
        if old_status in _STEER_FAILURE_TERMINAL:
            return False
        if new_status in _STEER_FAILURE_TERMINAL:
            # Async acks are success-path only; never clobber with failure here.
            return False
        old_r = self._status_rank(old_status)
        new_r = self._status_rank(new_status)
        if new_r > old_r:
            return True
        if new_r == old_r and new_r >= 0:
            # Same rung: allow evidence upgrade only.
            return self._evidence_rank(new_evidence) > self._evidence_rank(old_evidence)
        return False

    def _process_mailbox_msg(self, msg: Dict[str, Any]) -> None:
        assert self.adapter and self.mailbox and self.run_id
        if self._terminal:
            # Should not deliver after terminal; mark failed if still open
            seq = int(msg.get("seq") or 0)
            if seq and msg.get("status") in (None, "accepted", "delivering"):
                self.mailbox.update_message(
                    seq,
                    status="failed",
                    error="run already terminal",
                )
            return
        seq = int(msg["seq"])
        kind = msg.get("kind")
        client_id = msg.get("client_id") or f"seq_{seq}"
        if kind == "cancel":
            self.mailbox.update_message(seq, status="applied", backend_ack="cancel")
            self.adapter.cancel()
            return
        if kind != "steer":
            self.mailbox.update_message(seq, status="failed", error=f"unknown kind {kind}")
            return
        content = msg.get("content") or ""
        mode = msg.get("mode") or "auto"
        progress(
            "steer",
            f"run_id={self.run_id}",
            f"deliver client_id={client_id}",
            f"mode={mode}",
            f"bytes={len(content)}",
        )
        self.mailbox.update_message(seq, status="delivering")
        try:
            result = self.adapter.steer(content, mode, client_id)
        except Exception as e:
            self.mailbox.update_message(
                seq,
                status="failed",
                error=str(e),
                delivery_class=None,
            )
            append_jsonl(
                self.registry.run_path(self.run_id) / "audit.jsonl",
                {
                    "ts": utc_now_iso(),
                    "event": "steer_failed",
                    "client_id": client_id,
                    "error": str(e),
                },
            )
            return
        dclass = result.delivery_class.value if result.delivery_class else None
        # Never leave delivering without an outcome
        status = result.status if result.status else ("failed" if not result.ok else "request_sent")
        self.mailbox.update_message(
            seq,
            status=status,
            delivery_class=dclass,
            backend_ack=result.evidence,
            error=result.error or None,
            meta={**(msg.get("meta") or {}), **(result.meta or {})},
        )
        # Update state steers map
        state = self.registry.load_state(self.run_id)
        steers = dict(state.get("steers") or {})
        steers[client_id] = {
            "seq": seq,
            "status": status,
            "delivery_class": dclass,
            "evidence": result.evidence,
            "error": result.error,
            "updated_at": utc_now_iso(),
        }
        self.registry.update_state(self.run_id, steers=steers)
        append_jsonl(
            self.registry.run_path(self.run_id) / "audit.jsonl",
            {
                "ts": utc_now_iso(),
                "event": "steer_result",
                "client_id": client_id,
                "ok": result.ok,
                "status": status,
                "delivery_class": dclass,
                "evidence": result.evidence,
                "error": result.error,
            },
        )
        progress(
            "steer",
            f"run_id={self.run_id}",
            f"ack client_id={client_id}",
            f"status={status}",
            f"class={dclass}",
            f"evidence={result.evidence}",
        )

    def _finalize(
        self,
        *,
        status: str,
        exit_code: int,
        final_text: str = "",
        error: str = "",
    ) -> None:
        if not self.run_id:
            return
        if self._terminal:
            return
        text = final_text
        if not text and self.adapter:
            try:
                text = self.adapter.final_text()
            except Exception:
                text = ""

        run_dir = self.registry.run_path(self.run_id)
        # Atomic terminal transition under run-level lock:
        # 1) close mailbox acceptance
        # 2) fail any open messages without outcome
        # 3) mark meta terminal
        reason = f"run_{status}"
        with self.registry.with_run_lock(self.run_id):
            self._terminal = True
            if self.mailbox:
                self.mailbox.close(reason=reason)
                failed = self.mailbox.fail_open_messages(
                    f"run became terminal ({status}) before delivery completed"
                )
                if failed:
                    append_jsonl(
                        run_dir / "audit.jsonl",
                        {
                            "ts": utc_now_iso(),
                            "event": "open_messages_failed_on_terminal",
                            "count": len(failed),
                            "reason": reason,
                            "seqs": [m.get("seq") for m in failed],
                        },
                    )
            self.registry.update_meta(
                self.run_id,
                status=status,
                exit_code=exit_code,
                error=error or None,
                finished_at=utc_now_iso(),
            )
            self.registry.update_state(self.run_id, status=status)

        # Artifacts (full text, never truncated)
        final_path = Path(self.artifacts_dir) / "final" / f"{self.agent_id}.txt"
        atomic_write_text(final_path, text)
        atomic_write_text(Path(self.artifacts_dir) / "final.txt", text)
        atomic_write_text(run_dir / "final.txt", text)

        progress("done", f"run_id={self.run_id}", f"status={status}", f"exit={exit_code}")
        # Clean final answer on stdout only
        if text:
            sys.stdout.write(text)
            if not text.endswith("\n"):
                sys.stdout.write("\n")
            sys.stdout.flush()

    def _cleanup_adapter(self) -> None:
        if not self.adapter:
            return
        try:
            child = self.adapter.child_pid()
            self.adapter.close()
            if child:
                kill_process_group(child, timeout=2.0)
        except Exception:
            pass

    def _artifacts_need_private_home(self, path: str) -> bool:
        """True when protocol artifacts must not land in project cwd."""
        if os.environ.get("CONSILIUM_SAVE_OUTPUTS", "1") == "0":
            return True
        p = (path or "").strip()
        if not p or p == ".":
            return True
        try:
            resolved = Path(p).resolve()
            if resolved == Path.cwd().resolve():
                return True
        except OSError:
            return True
        return False

    def _resolve_artifacts_dir(self, path: str) -> str:
        """
        Return artifacts path for create_run meta.

        When SAVE_OUTPUTS=0 or the path is empty/./cwd, return empty so run()
        places protocol artifacts under the private registry run dir after
        create_run. Never leave protocol artifacts in the project cwd.
        """
        if self._artifacts_need_private_home(path):
            return ""
        return str(Path(path).expanduser())


def _prefix_hash(text: str) -> str:
    import hashlib

    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def main(argv: Optional[list] = None) -> int:
    import argparse

    p = argparse.ArgumentParser(prog="steer-supervisor")
    p.add_argument("--agent-id", required=True)
    p.add_argument("--task-file", required=True)
    p.add_argument("--cwd", default=os.getcwd())
    # Empty string is allowed: supervisor relocates protocol artifacts under the
    # private registry run when archival is off or path is project cwd.
    p.add_argument("--artifacts-dir", default="", required=False)
    p.add_argument("--registry-root", default="")
    args = p.parse_args(argv)
    task = Path(args.task_file).read_text(encoding="utf-8")
    reg = Registry(Path(args.registry_root) if args.registry_root else None)
    sup = Supervisor(
        agent_id=args.agent_id,
        task=task,
        cwd=args.cwd,
        artifacts_dir=args.artifacts_dir,
        registry=reg,
    )
    return sup.run()


if __name__ == "__main__":
    sys.exit(main())
