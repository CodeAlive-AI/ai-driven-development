"""Opt-in disk response controller. Tick is cheap; workers own slow work/UI."""
from __future__ import annotations

import argparse
import contextlib
import fcntl
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
import uuid

from disk_safety import (ASSETS, PROFILE, PROFILE_HASH, Mole, candidate, digest,
                         inventory, measure, no_links, private_dir, read_json,
                         remove_files, write_json)
from disk_agent import capabilities, run_codex


class Context:
    def __init__(self, home=None):
        self.home = Path.home() if home is None else Path(home)
        self.config = self.home / ".config/mac-health/disk-response-consent.json"
        self.state = self.home / ".local/state/mac-health/disk-responses"
        self.pause = self.home / ".config/mac-health/pause-disk-responses"

    def consent(self):
        if not self.config.exists():
            return {}
        result = read_json(self.config)
        if result.get("schema_version") != 1:
            raise ValueError("unsupported consent schema")
        return result

    def allowed(self, mode):
        if self.pause.exists():
            return False
        entry = self.consent().get(mode, {})
        return (entry.get("decision") == "approved" and entry.get("scope_revision") == 1
                and (mode != "emergency" or entry.get("profile_sha256") == PROFILE_HASH))

    def incident(self, name):
        if str(uuid.UUID(name)) != name:
            raise ValueError("invalid incident ID")
        return private_dir(self.state / name)

    @contextlib.contextmanager
    def lock(self, name, blocking=False):
        private_dir(self.state)
        path = no_links(self.state / (name + ".lock"))
        fd = os.open(path, os.O_CREAT | os.O_RDWR | os.O_NOFOLLOW, 0o600)
        try:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | (0 if blocking else fcntl.LOCK_NB))
            except BlockingIOError:
                yield False
                return
            yield True
        finally:
            os.close(fd)


def set_status(incident, status, **extra):
    path = incident / "status.json"
    previous = read_json(path) if path.exists() else {}
    write_json(path, {**previous, **extra, "status": status, "updated_at": time.time()})


def launch(context, mode, incident_id):
    incident = context.incident(incident_id)
    command = [sys.executable, str(ASSETS / "mac-health-disk"), "worker", mode, incident_id]
    output_path = no_links(incident / "worker.log")
    with open(output_path, "xb") as output:
        os.chmod(output_path, 0o600)
        process = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=output,
                                   stderr=subprocess.STDOUT, start_new_session=True)
    write_json(incident / "worker-process.json", {"pid": process.pid})


def tick(context, disk_measure=measure, dispatch=launch, now=None):
    if not any(context.allowed(mode) for mode in ["emergency", "agent_plan"]):
        return
    now = time.time() if now is None else now
    free, total = disk_measure()
    with context.lock("tick") as locked:
        if not locked:
            return
        path = context.state / "incidents.json"
        state = read_json(path) if path.exists() else {}
        gap = now - state.get("sample_at", now) > 900
        for mode, threshold, recovery in [("emergency", 2, 4), ("agent_plan", 5, 7)]:
            record = state.setdefault(mode, {})
            count = 0 if gap else record.get("recovery_count", 0)
            record["recovery_count"] = count + 1 if free * 100 > total * recovery else 0
            incident_id = record.get("incident_id")
            if incident_id:
                existing = context.incident(incident_id)
                status_record = read_json(existing / "status.json")
                status = status_record.get("status")
                if status in {"queued", "scanning", "applying", "reviewing"} and now - status_record["updated_at"] > 30:
                    # Locks are released by the OS after crash/reboot. Do not
                    # trust a stale PID or replay its uncertain side effects.
                    with context.lock("worker-" + incident_id) as worker_gone:
                        if worker_gone:
                            set_status(existing, "failed", error="worker interrupted; inspect audit before explicit retry")
                            status = "failed"
                active = status in {"queued", "scanning", "awaiting_selection", "reviewing",
                                    "awaiting_confirmation", "applying"}
                if (record["recovery_count"] >= 3 and not active
                        and (mode != "emergency" or now - record["attempt_at"] >= 86400)):
                    record.pop("incident_id", None)
            triggered = free * 100 < total * threshold if mode == "emergency" else free * 100 <= total * threshold
            if not triggered or not context.allowed(mode) or record.get("incident_id"):
                continue
            if mode == "emergency":
                with context.lock("deletion") as deletion_available:
                    if not deletion_available:
                        continue
            # A new emergency invalidates any earlier plan's snapshot. It does
            # not turn a previously selected plan into consent for more files.
            if mode == "emergency" and state.get("agent_plan", {}).get("incident_id"):
                old = context.incident(state["agent_plan"]["incident_id"])
                write_json(old / "stale.json", {"reason": "emergency cleanup started"})
                if read_json(old / "status.json")["status"] in {"awaiting_selection", "awaiting_confirmation"}:
                    set_status(old, "stale", error="Emergency cleanup invalidated this plan; use retry to rescan")
            # If emergency is pending/running, a subsequent tick will plan from
            # a fresh measurement. This avoids racing scan against deletion.
            if mode == "agent_plan" and state.get("emergency", {}).get("incident_id"):
                emergency = context.incident(state["emergency"]["incident_id"])
                if read_json(emergency / "status.json")["status"] in {"queued", "applying"}:
                    continue
            incident_id = str(uuid.uuid4())
            record.update(incident_id=incident_id, attempt_at=now)
            incident = context.incident(incident_id)
            set_status(incident, "queued", mode=mode, free=free, total=total)
            # Commit deduplication BEFORE the side effect, including failed spawn.
            state["sample_at"] = now
            write_json(path, state)
            try:
                dispatch(context, mode, incident_id)
            except Exception as exc:
                set_status(incident, "failed", error=str(exc))
        state["sample_at"] = now
        write_json(path, state)


def worker(context, mode, incident_id):
    with context.lock("worker-" + incident_id) as locked:
        if not locked:
            raise ValueError("incident worker already running")
        if read_json(context.incident(incident_id) / "status.json")["status"] != "queued":
            raise ValueError("incident already attempted; explicit retry required")
        return run_worker(context, mode, incident_id)


def run_worker(context, mode, incident_id):
    incident = context.incident(incident_id)
    try:
        if not context.allowed(mode):
            raise ValueError("consent missing/revoked or responses paused")
        free, total = measure()
        recovered = free * 100 >= total * 2 if mode == "emergency" else free * 100 > total * 5
        if recovered:
            set_status(incident, "recovered")
            return
        settings = context.consent()[mode]
        if mode == "emergency":
            with context.lock("deletion") as locked:
                if not locked:
                    raise ValueError("another cleanup is running; explicit retry required")
                set_status(incident, "applying")
                backend = Mole(settings["mole_core"])
                if context.home.stat().st_dev != Path("/System/Volumes/Data").stat().st_dev:
                    raise ValueError("home and monitored Data volume differ")
                rows, truncated = inventory(context.home, seconds=10, limit=100)
                result = remove_files(context.home, rows, incident, backend,
                                      lambda: context.allowed(mode), emergency=True)
                set_status(incident, "completed", removed=len(result["removed"]),
                           before=result["before"], after=result["after"], truncated=truncated)
            # Both independent modes may be approved; remeasure and dispatch the
            # plan immediately after emergency instead of waiting five minutes.
            tick(context)
            return
        set_status(incident, "scanning")
        rows, truncated = inventory(context.home, allow_downloads=True, limit=250)
        payload = {"free_bytes": free, "total_bytes": total, "items": rows,
                   "truncated": truncated, "scope": "Package caches and top-level Downloads archives only"}
        write_json(incident / "inventory.json", payload)
        answer, session_id = run_codex(settings, incident, "scan", payload)
        descriptions = {item["id"]: item["description"] for item in answer["items"]}
        for item in rows:
            # The agent may annotate, never add/replace paths, identities or ops.
            item["description"] = descriptions.get(item["id"], item["description"])
        plan = {**payload, "summary": answer["summary"], "session_id": session_id,
                "created_at": time.time(), "incident_id": incident_id}
        write_json(incident / "plan.json", plan)
        set_status(incident, "awaiting_selection", session_id=session_id)
        from disk_review import serve
        serve(context, incident)
    except Exception as exc:
        set_status(incident, "failed", error=str(exc))
        print(f"Disk response failed: {exc}", file=sys.stderr)
        # Keep normal disk alerts; no fallback mutation or paid retry.
        raise


def review_selection(context, incident):
    try:
        if not context.allowed("agent_plan") or (incident / "stale.json").exists():
            raise ValueError("plan stale, consent revoked, or responses paused")
        plan, selection = read_json(incident / "plan.json"), read_json(incident / "selection.json")
        answer, session_id = run_codex(context.consent()["agent_plan"], incident, "review",
                                      {"items": selection["selected_items"]}, plan["session_id"])
        set_status(incident, "awaiting_confirmation", review=answer["summary"], session_id=session_id)
    except Exception as exc:
        set_status(incident, "failed", error=str(exc))


def apply_confirmed(context, incident):
    with context.lock("deletion") as locked:
        if not locked:
            raise ValueError("another cleanup is running")
        if not context.allowed("agent_plan") or (incident / "stale.json").exists():
            raise ValueError("plan stale, consent revoked, or responses paused")
        if read_json(incident / "status.json")["status"] != "applying":
            raise ValueError("no pending confirmed apply; refusing replay")
        plan = read_json(incident / "plan.json")
        selection = read_json(incident / "selection.json")
        confirmation = read_json(incident / "confirmation.json")
        if (confirmation["selection_sha256"] != digest(selection)
                or selection["plan_sha256"] != digest(plan)
                or time.time() - confirmation["confirmed_at"] > 300
                or time.time() - plan["created_at"] > 3600):
            raise ValueError("changed or expired confirmation/plan")
        indexed = {row["id"]: row for row in plan["items"]}
        ids = selection["selected_ids"]
        if not ids or len(set(ids)) != len(ids) or selection["selected_items"] != [indexed[i] for i in ids]:
            raise ValueError("selection does not match trusted plan")
        # Consume the confirmation before touching any user file. An uncertain
        # result requires inspection, never replay after restart.
        if (incident / "apply-started.json").exists():
            raise ValueError("apply already attempted; refusing replay")
        write_json(incident / "apply-started.json", {"at": time.time(), "selection": digest(selection)})
        backend = Mole(context.consent()["agent_plan"]["mole_core"])
        result = remove_files(context.home, selection["selected_items"], incident, backend,
                              lambda: context.allowed("agent_plan") and not (incident / "stale.json").exists())
        set_status(incident, result["status"], removed=len(result["removed"]),
                   before=result["before"], after=result["after"],
                   error="Time budget reached; remaining files were preserved" if result["status"] == "partial" else "")
        return result


def configure(context, args):
    consent = context.consent() or {"schema_version": 1, "installation_id": str(uuid.uuid4())}
    changes = [(mode, getattr(args, mode)) for mode in ["emergency", "agent_plan"]
               if getattr(args, mode) is not None]
    if not changes:
        raise ValueError("choose at least one option explicitly")
    for mode, choice in changes:
        if choice == "enable":
            if not args.record or len(args.record.strip()) < 8:
                raise ValueError("enable requires --record with the user's explicit authorization")
            core = args.mole_core
            if not core:
                raise ValueError("--mole-core must name the audited lib/core directory")
            Mole(core)
            entry = {"decision": "approved", "scope_revision": 1, "approved_at": time.time(),
                     "authorization": args.record, "mole_core": str(Path(core).absolute())}
            if mode == "emergency":
                entry["profile_sha256"] = PROFILE_HASH
            else:
                binary = args.codex or shutil.which("codex")
                if not binary:
                    raise ValueError("Codex CLI unavailable")
                entry.update(binary=str(Path(binary).resolve()), binary_sha256=capabilities(binary),
                             provider="codex", model=args.model or "")
            consent[mode] = entry
        else:
            consent[mode] = {"decision": "declined" if choice == "decline" else "revoked",
                             "updated_at": time.time()}
    consent["offered_at"] = consent.get("offered_at", time.time())
    # Older alert-only installations created this directory with mode 755.
    # Explicit setup may tighten its permissions; background ticks never do.
    parent = no_links(context.config.parent)
    if parent.exists():
        if parent.stat().st_uid != os.getuid():
            raise ValueError("configuration directory is not owned by this user")
        parent.chmod(0o700)
    write_json(context.config, consent)
    print(json.dumps({mode: consent[mode]["decision"] for mode, _ in changes}))


def main(argv=None):
    parser = argparse.ArgumentParser(description="Optional disk responses; nothing is enabled by installation")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("tick")
    sub.add_parser("status")
    config = sub.add_parser("configure", help="only after independent explicit user consent")
    config.add_argument("--emergency", choices=["enable", "disable", "decline"])
    config.add_argument("--agent-plan", choices=["enable", "disable", "decline"])
    config.add_argument("--record", help="the user's explicit consent, not inferred approval")
    config.add_argument("--mole-core")
    config.add_argument("--codex")
    config.add_argument("--model")
    work = sub.add_parser("worker")
    work.add_argument("mode", choices=["emergency", "agent_plan"])
    work.add_argument("incident_id")
    reopen = sub.add_parser("reopen", help="reopen an unexpired page; does not rerun the agent")
    reopen.add_argument("incident_id")
    retry = sub.add_parser("retry", help="explicit retry of a failed/cancelled mode after inspection")
    retry.add_argument("mode", choices=["emergency", "agent_plan"])
    args = parser.parse_args(argv)
    context = Context()
    os.umask(0o077)
    try:
        if os.geteuid() == 0:
            raise ValueError("run as the logged-in user, never through sudo/root")
        if args.command == "tick":
            tick(context)
        elif args.command == "status":
            print(json.dumps({"consent": context.consent(), "paused": context.pause.exists(),
                              "state_directory": str(context.state)}, indent=2))
            for path in context.state.glob("*/status.json"):
                print(path.parent.name, json.dumps(read_json(path)))
        elif args.command == "configure":
            configure(context, args)
        elif args.command == "worker":
            worker(context, args.mode, args.incident_id)
        elif args.command == "reopen":
            from disk_review import serve
            with context.lock("worker-" + args.incident_id) as locked:
                if not locked:
                    raise ValueError("incident page/worker is already running")
                incident = context.incident(args.incident_id)
                # Opening the browser may have failed after a successful scan.
                # Reopening that existing plan must not cost another model call.
                status = read_json(incident / "status.json")["status"]
                if (status == "failed" and (incident / "plan.json").exists()
                        and not (incident / "selection.json").exists() and not (incident / "stale.json").exists()):
                    set_status(incident, "awaiting_selection", error="")
                if status == "awaiting_selection" and (incident / "selection.json").exists():
                    set_status(incident, "failed", error="submission dispatch interrupted; inspect before explicit retry")
                serve(context, incident)
        elif args.command == "retry":
            with context.lock("tick") as locked:
                if not locked:
                    raise ValueError("monitor busy")
                path = context.state / "incidents.json"
                state = read_json(path)
                old = context.incident(state[args.mode]["incident_id"])
                status = read_json(old / "status.json")["status"]
                if status not in {"failed", "cancelled", "expired", "recovered", "completed", "partial", "stale"}:
                    raise ValueError("worker/plan is active; cannot retry")
                if (old / "holding").exists() and any((old / "holding").iterdir()):
                    raise ValueError("recover held files before retry")
                state[args.mode].pop("incident_id", None)
                write_json(path, state)
            tick(context)
        return 0
    except Exception as exc:
        print(f"mac-health-disk: {exc}", file=sys.stderr)
        return 1
