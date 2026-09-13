"""Regression coverage for bounded observation and durable follow-up turns."""
import contextlib
import io
import json
import os
import signal
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest.mock import patch

from test_steer_e2e import CONSILIUM, env_base, extract_run_id
from steer.adapters.opencode import OpenCodeAdapter
from steer.control import _duration_seconds
from steer.registry import Registry, RegistryError
from steer.session import SessionLease
from steer.util import atomic_write_json, atomic_write_text
from steer.waiter import wait_for_any, wait_for_terminal


class OrchestrationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="consilium-orchestration-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / "raw").mkdir()
        self.reg = Registry(self.root / "registry")
        self.env = env_base(self.reg.root, self.root / "artifacts")
        self.env["CONSILIUM_FAKE_STEER_SLOW"] = "0.02"
        self.env["CONSILIUM_SAVE_OUTPUTS"] = "0"
        self.env["CONSILIUM_FAKE_RPC_LOG"] = str(self.root / "rpc.jsonl")

    def run_record(self, status="running", **extra):
        rid = self.reg.create_run(agent_id="codex", backend="codex-cli", model="test",
                                  cwd=str(self.root), artifacts_dir=str(self.root / "artifacts"),
                                  extra={"effort": "high", "backend_binary": "codex", **extra})
        self.reg.update_meta(rid, status=status, exit_code=0 if status == "completed" else None)
        return rid

    def cli(self, *args, **kwargs):
        return subprocess.run([str(CONSILIUM), "delegate", *args], cwd=kwargs.pop("cwd", self.root),
                              env=kwargs.pop("env", self.env), text=True, input="", capture_output=True,
                              timeout=30, **kwargs)

    def start_durable(self):
        p = self.cli("-a", "codex", "--persist-session", "INITIAL_ONLY")
        self.assertEqual(p.returncode, 0, p.stderr)
        rid = extract_run_id(p.stderr)
        self.assertTrue(rid)
        return rid

    def rpc_calls(self):
        p = self.root / "rpc.jsonl"
        return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []

    def test_abort_failure_never_sends_replacement(self):
        a = OpenCodeAdapter(binary="fake", model="test", cwd=str(self.root), artifacts_dir=str(self.root))
        a.session_id = "test"
        with patch.object(a, "_http_json", side_effect=TimeoutError("unresolved")), patch.object(a, "_prompt_async") as send:
            result = a.steer("replacement", "interrupt", "id")
        self.assertFalse(result.ok)
        self.assertEqual(result.status, "failed")
        self.assertIn("outcome unknown", result.error)
        send.assert_not_called()
        self.assertTrue(a.is_done())
        self.assertNotEqual(a.exit_code(), 0)
        self.assertFalse(a._replacement_pending)

    def test_abort_idle_then_failure_does_not_leave_wait_hanging(self):
        a = OpenCodeAdapter(binary="fake", model="test", cwd=str(self.root), artifacts_dir=str(self.root))
        a.session_id = "test"
        def abort():
            a._busy = False  # idle arrived while replacement was pending
            raise RuntimeError("abort failed after idle")
        with patch.object(a, "_abort", side_effect=abort), patch.object(a, "_prompt_async") as send:
            result = a.steer("replacement", "interrupt", "id")
        self.assertFalse(result.ok)
        self.assertTrue(a.is_done())
        send.assert_not_called()

    def test_abort_rejection_never_sends_replacement(self):
        a = OpenCodeAdapter(binary="fake", model="test", cwd=str(self.root), artifacts_dir=str(self.root))
        a.session_id = "test"
        with patch.object(a, "_http_json", return_value=False), patch.object(a, "_prompt_async") as send:
            result = a.steer("replacement", "interrupt", "id")
        self.assertFalse(result.ok)
        self.assertIn("rejected abort", result.error)
        send.assert_not_called()

    def test_unresolved_stop_never_sends_replacement(self):
        a = OpenCodeAdapter(binary="fake", model="test", cwd=str(self.root), artifacts_dir=str(self.root))
        a.session_id = "test"
        with patch.object(a, "_abort"), patch.object(a, "_runner_is_idle", return_value=False), patch.object(a, "_prompt_async") as send:
            wait = a._wait_for_abort_idle
            with patch.object(a, "_wait_for_abort_idle", side_effect=lambda: wait(timeout=.02)):
                result = a.steer("replacement", "interrupt", "id")
        self.assertFalse(result.ok)
        self.assertIn("outcome unknown", result.error)
        send.assert_not_called()

    def test_status_idle_without_abort_event_allows_replacement(self):
        a = OpenCodeAdapter(binary="fake", model="test", cwd=str(self.root), artifacts_dir=str(self.root))
        a.session_id = "test"
        calls = []
        with patch.object(a, "_abort", side_effect=lambda: calls.append("abort")), patch.object(a, "_runner_is_idle", side_effect=lambda **kw: calls.append("status") or True), patch.object(a, "_prompt_async", side_effect=lambda *args, **kw: calls.append("prompt")):
            result = a.steer("replacement", "interrupt", "id")
        self.assertTrue(result.ok)
        self.assertEqual(calls, ["abort", "status", "prompt"])

    def test_late_old_idle_does_not_finish_busy_replacement(self):
        a = OpenCodeAdapter(binary="fake", model="test", cwd=str(self.root), artifacts_dir=str(self.root))
        a.session_id = "test"
        with patch.object(a, "_http_json", return_value={}):
            self.assertTrue(a.steer("replacement", "interrupt", "id").ok)
        idle = {"type": "session.idle", "properties": {"sessionID": "test"}}
        with patch.object(a, "_runner_is_idle", return_value=False):
            a._handle_event(idle)
        self.assertFalse(a.is_done())
        self.assertTrue(a.is_busy())
        with patch.object(a, "_runner_is_idle", return_value=True):
            a._handle_event(idle)
        self.assertTrue(a.is_done())
        self.assertEqual(a.exit_code(), 0)

    def test_malformed_runner_status_is_not_idle(self):
        a = OpenCodeAdapter(binary="fake", model="test", cwd=str(self.root), artifacts_dir=str(self.root))
        a.session_id = "test"
        for data in (None, False, {"test": {"type": "unexpected"}}, {"raw": "not json"}):
            with patch.object(a, "_http_json", return_value=data), self.assertRaises(RuntimeError):
                a._runner_is_idle()

    def test_wait_timeout_leaves_worker_untouched(self):
        rid = self.run_record()
        before = self.reg.load_meta(rid)
        started = time.monotonic()
        snaps, timeout = wait_for_any(self.reg, [rid], timeout=.03, poll_interval=10)
        self.assertTrue(timeout)
        self.assertLess(time.monotonic() - started, .5)
        self.assertFalse(snaps[rid].terminal)
        self.assertEqual(self.reg.load_meta(rid), before)

    def test_zero_snapshot_and_ready_wins_over_deadline(self):
        active, complete = self.run_record(), self.run_record("completed")
        snaps, timeout = wait_for_any(self.reg, [active, complete], timeout=0)
        self.assertFalse(timeout)
        self.assertTrue(snaps[complete].terminal)
        self.assertFalse(snaps[active].terminal)

    def test_wait_any_later_worker_completes(self):
        slow, fast = self.run_record(), self.run_record()
        timer = threading.Timer(.03, lambda: self.reg.update_meta(fast, status="completed", exit_code=0))
        timer.start()
        self.addCleanup(timer.join)
        snaps, timed_out = wait_for_any(self.reg, [slow, fast], timeout=2, poll_interval=.01)
        self.assertFalse(timed_out)
        self.assertTrue(snaps[fast].terminal)
        self.assertFalse(snaps[slow].terminal)

    def test_failure_wakes_wait_any(self):
        slow, failed = self.run_record(), self.run_record("failed")
        p = self.cli("wait-any", slow, failed, "--timeout", "0")
        self.assertEqual(p.returncode, 0, p.stderr)
        data = json.loads(p.stdout)
        self.assertEqual(data["ready"], [failed])
        self.assertEqual(data["runs"][1]["exit_code"], 1)

    def test_unknown_target_is_not_hidden_by_ready_target(self):
        rid = self.run_record("completed")
        with self.assertRaises(RegistryError):
            wait_for_any(self.reg, [rid, "missing"], timeout=0)

    def test_dead_first_worker_cannot_delay_later_result(self):
        dead, ready = self.run_record(pid=99999999), self.run_record("completed")
        start = time.monotonic()
        snapshots, _ = wait_for_any(self.reg, [dead, ready])
        self.assertLess(time.monotonic() - start, .3)
        self.assertTrue(snapshots[ready].terminal)

    def test_dead_worker_is_reaped_after_grace(self):
        rid = self.run_record(pid=99999999)
        with patch("steer.waiter.DEAD_PID_GRACE_SECONDS", .01):
            snap = wait_for_terminal(self.reg, rid, timeout=1, poll_interval=.01)
        self.assertTrue(snap.terminal)
        self.assertEqual(snap.meta["error"], "supervisor_dead")

    def test_wait_timeout_json_has_bounded_progress_and_cursor(self):
        rid = self.run_record()
        log = self.root / "artifacts" / "normalized" / "codex.jsonl"
        log.parent.mkdir(parents=True)
        log.write_text(''.join(json.dumps({"type": "tool_call", "name": f"tool-{n}"})+'\n' for n in range(12)))
        p = self.cli("wait", rid, "--timeout", "0", "--json")
        self.assertEqual(p.returncode, 124, p.stderr)
        data = json.loads(p.stdout)
        self.assertTrue(data["timed_out"])
        self.assertFalse(data["terminal"])
        self.assertLessEqual(len(data["events"]), 5)
        self.assertEqual(data["next_cursor"], 12)
        self.assertEqual(self.reg.load_meta(rid)["status"], "running")

    def test_progress_failure_does_not_hide_readiness_or_timeout(self):
        rid = self.run_record()
        self.reg.update_meta(rid, artifacts_dir="invalid\0path")
        result = self.cli("wait", rid, "--timeout", "0", "--json")
        self.assertEqual(result.returncode, 124, result.stderr)
        self.assertIn("events_error", json.loads(result.stdout))
        self.reg.update_meta(rid, status="completed", exit_code=0)
        result = self.cli("wait-any", rid, "--timeout", "0")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["ready"], [rid])
        self.assertIn("events_error", json.loads(result.stdout)["runs"][0])

    def test_wait_any_timeout_and_remove_consumed_result(self):
        ready, active = self.run_record("completed"), self.run_record()
        first = self.cli("wait-any", ready, active, "--timeout", "0")
        self.assertEqual(json.loads(first.stdout)["ready"], [ready])
        next_page = self.cli("wait-any", active, "--timeout", "0")
        self.assertEqual(next_page.returncode, 124)
        self.assertEqual(json.loads(next_page.stdout)["ready"], [])

    def test_invalid_timeouts(self):
        for value in ("nan", "inf", "-1"):
            p = self.cli("wait-any", "missing", "--timeout", value)
            self.assertEqual(p.returncode, 2, p.stderr)

    def test_group_retains_acknowledged_runs_without_repeated_wakeup(self):
        done = self.run_record("completed", started_at="2026-01-01T00:00:00Z",
                               finished_at="2026-01-01T00:01:30Z")
        active = self.run_record(pid=os.getpid())
        self.run_record("completed")  # Unrelated registry entry must be excluded.
        p = self.cli("wait-any", done, active, "--acknowledged", done, "--timeout", "0.01")
        self.assertEqual(p.returncode, 124, p.stderr)
        data = json.loads(p.stdout)
        self.assertEqual(data["ready"], [])
        self.assertEqual([r["run_id"] for r in data["runs"]], [done, active])
        self.assertEqual(data["runs"][0]["elapsed_seconds"], 90)
        self.assertGreaterEqual(data["runs"][1]["elapsed_seconds"], 0)
        self.assertEqual(data["runs"][1]["model"], "test")
        self.reg.update_meta(active, status="failed", exit_code=7,
                             finished_at="2026-09-13T12:00:00Z")
        p = self.cli("wait-any", done, active, "--acknowledged", done, "--timeout", "900")
        self.assertEqual(p.returncode, 0, p.stderr)
        data = json.loads(p.stdout)
        self.assertEqual(data["ready"], [active])
        self.assertEqual(len(data["runs"]), 2)
        self.assertEqual(data["runs"][1]["exit_code"], 7)

    def test_invalid_acknowledgement_fails_explicitly(self):
        active, done = self.run_record(), self.run_record("completed")
        for group, acknowledged in (([active], active), ([done], "missing"), ([done], done)):
            p = self.cli("wait-any", *group, "--acknowledged", acknowledged, "--timeout", "0")
            self.assertEqual(p.returncode, 5, p.stderr)

    def test_duration_uses_timezone_and_preserves_unknown_terminal_time(self):
        meta = {"started_at": "2026-01-01T01:00:00+01:00",
                "finished_at": "2026-01-01T00:00:30Z", "status": "completed"}
        self.assertEqual(_duration_seconds(meta, include_running=True), 30)
        for invalid in (None, "bad", 123):
            self.assertIsNone(_duration_seconds(dict(meta, started_at=invalid), include_running=True))
        self.assertIsNone(_duration_seconds(dict(meta, finished_at=None), include_running=True))

    def test_backend_does_not_inherit_parent_artifact_destination(self):
        log = self.root / "backend-env.json"
        p = self.cli("-a", "codex", "ENV_CHECK", env=dict(self.env,
                     CONSILIUM_SAVE_OUTPUTS="1", CONSILIUM_ARTIFACT_KEY="parent",
                     CONSILIUM_FAKE_ARTIFACT_ENV_LOG=str(log)))
        self.assertEqual(p.returncode, 0, p.stderr)
        observed = json.loads(log.read_text())
        self.assertIsNone(observed["CONSILIUM_RUN_DIR"])
        self.assertIsNone(observed["CONSILIUM_ARTIFACT_KEY"])
        self.assertEqual(observed["CONSILIUM_OUTPUT_DIR"], self.env["CONSILIUM_OUTPUT_DIR"])
        self.assertEqual(observed["CONSILIUM_STEER_DIR"], self.env["CONSILIUM_STEER_DIR"])
        rid = extract_run_id(p.stderr)
        self.assertEqual(self.reg.load_meta(rid)["artifacts_dir"], self.env["CONSILIUM_RUN_DIR"])

    def test_detached_wait_loop_timeout_then_collects_every_result(self):
        pending = []
        try:
            for delay in (2, .5):
                started = self.cli("-a", "codex", "--detach", "WAIT_LOOP",
                                   env=dict(self.env, CONSILIUM_FAKE_STEER_SLOW=str(delay)))
                self.assertEqual(started.returncode, 0, started.stderr)
                pending.append(started.stdout.strip())
            expected = set(pending)
            group = list(pending)
            # A short observation deadline must leave both detached runs alive.
            observed = self.cli("wait-any", *pending, "--timeout", "0.01")
            self.assertEqual(observed.returncode, 124, observed.stderr)
            self.assertEqual(json.loads(observed.stdout)["ready"], [])
            collected = set()
            while pending:
                acknowledged = [arg for rid in collected for arg in ("--acknowledged", rid)]
                observed = self.cli("wait-any", *group, *acknowledged, "--timeout", "900")
                self.assertEqual(observed.returncode, 0, observed.stderr)
                data = json.loads(observed.stdout)
                self.assertEqual({r["run_id"] for r in data["runs"]}, expected)
                self.assertTrue(all(r["elapsed_seconds"] is not None for r in data["runs"]))
                ready = data["ready"]
                self.assertTrue(ready)
                for rid in ready:
                    result = self.cli("wait", rid, "--timeout", "5", "--json")
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn("FAKE_CODEX", result.stdout)
                    collected.add(rid)
                    pending.remove(rid)
            self.assertEqual(collected, expected)
        finally:
            for rid in pending:
                self.cli("cancel", rid)

    def test_completion_between_observations_is_not_lost(self):
        rid = self.run_record(pid=os.getpid())
        first = self.cli("wait-any", rid, "--timeout", "0")
        self.assertEqual(first.returncode, 124, first.stderr)
        self.reg.update_meta(rid, status="completed", exit_code=0)
        resumed = self.cli("wait-any", rid, "--timeout", "900")
        self.assertEqual(resumed.returncode, 0, resumed.stderr)
        self.assertEqual(json.loads(resumed.stdout)["ready"], [rid])

    def test_observer_interrupt_does_not_cancel_worker(self):
        rid = self.run_record()
        p = subprocess.Popen([str(CONSILIUM), "delegate", "wait-any", rid], cwd=self.root,
                             env=self.env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            time.sleep(.4)
            p.send_signal(signal.SIGINT)
            out, err = p.communicate(timeout=5)
            self.assertEqual(p.returncode, 130, err)
            self.assertEqual(self.reg.load_meta(rid)["status"], "running")
        finally:
            if p.poll() is None:
                p.kill()
                p.wait()

    def test_continue_reuses_thread_and_only_sends_new_instruction(self):
        rid = self.start_durable()
        old_meta = self.reg.load_meta(rid)
        p = self.cli("-a", "codex", "--continue-run", rid, "FOLLOWUP_ONLY")
        self.assertEqual(p.returncode, 0, p.stderr)
        successor = extract_run_id(p.stderr)
        new_meta = self.reg.load_meta(successor)
        self.assertEqual(new_meta["continued_from"], rid)
        self.assertEqual(old_meta, self.reg.load_meta(rid))
        self.assertEqual(new_meta["session_handle"], old_meta["session_handle"])
        calls = self.rpc_calls()
        self.assertEqual(len([c for c in calls if c["method"] == "thread/start"]), 1)
        resumes = [c for c in calls if c["method"] == "thread/resume"]
        self.assertEqual(len(resumes), 1)
        self.assertEqual(resumes[0]["params"]["threadId"], old_meta["session_handle"]["thread_id"])
        texts = [c["params"]["input"][0]["text"] for c in calls if c["method"] == "turn/start"]
        self.assertEqual(texts, ["INITIAL_ONLY", "FOLLOWUP_ONLY"])
        third = self.cli("-a", "codex", "--continue-run", successor, "THIRD")
        self.assertEqual(third.returncode, 0, third.stderr)

    def test_default_stays_ephemeral_and_cannot_continue(self):
        p = self.cli("-a", "codex", "ordinary")
        rid = extract_run_id(p.stderr)
        self.assertEqual(p.returncode, 0, p.stderr)
        self.assertTrue(next(c for c in self.rpc_calls() if c["method"] == "thread/start")["params"]["ephemeral"])
        followup = self.cli("-a", "codex", "--continue-run", rid, "new")
        self.assertNotEqual(followup.returncode, 0)
        self.assertIn("no durable", followup.stderr)

    def test_resume_failure_never_falls_back_or_retries_old_source(self):
        rid = self.start_durable()
        broken = dict(self.env, CONSILIUM_FAKE_CODEX_STEER_MODE="resume-error")
        p = self.cli("-a", "codex", "--continue-run", rid, "DO_NOT_SEND", env=broken)
        self.assertNotEqual(p.returncode, 0)
        successor = extract_run_id(p.stderr)
        self.assertEqual(self.reg.load_meta(successor)["status"], "failed")
        retry = self.cli("-a", "codex", "--continue-run", rid, "RETRY")
        self.assertNotEqual(retry.returncode, 0)
        self.assertIn("not the latest", retry.stderr)
        calls = self.rpc_calls()
        self.assertEqual(len([c for c in calls if c["method"] == "thread/start"]), 1)
        self.assertEqual(len([c for c in calls if c["method"] == "turn/start"]), 1)

    def test_failed_source_rejected(self):
        rid = self.start_durable()
        self.reg.update_meta(rid, status="failed", exit_code=1)
        p = self.cli("-a", "codex", "--continue-run", rid, "new")
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("outcome may be unknown", p.stderr)

    def test_lost_session_coordination_fails_without_replaying(self):
        rid = self.start_durable()
        (self.reg.run_path(rid) / "session.json").unlink()
        count = len(self.rpc_calls())
        p = self.cli("-a", "codex", "--continue-run", rid, "new")
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("cannot safely continue after registry loss", p.stderr)
        self.assertEqual(len(self.rpc_calls()), count)

    def test_changed_root_rejected_without_provider_call(self):
        rid = self.start_durable()
        elsewhere = self.root / "elsewhere"
        elsewhere.mkdir()
        count = len(self.rpc_calls())
        p = self.cli("-a", "codex", "--continue-run", rid, "new", cwd=elsewhere)
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("original working directory", p.stderr)
        self.assertEqual(len(self.rpc_calls()), count)

    def test_changed_model_rejected(self):
        rid = self.start_durable()
        self.reg.update_meta(rid, model="different")
        p = self.cli("-a", "codex", "--continue-run", rid, "new")
        self.assertNotEqual(p.returncode, 0)
        self.assertIn("unchanged model", p.stderr)

    def test_concurrent_continuation_and_stale_source_rejected(self):
        source = self.start_durable()
        old = self.reg.load_meta(source)
        current = self.reg.create_run(agent_id=old["agent_id"], backend=old["backend"], model=old["model"],
                                     cwd=old["cwd"], artifacts_dir="", extra={"effort":old["effort"], "backend_binary":old["backend_binary"]})
        lease = SessionLease(self.reg, current, source)
        lease.acquire()
        try:
            other = SessionLease(self.reg, current, source)
            with self.assertRaisesRegex(RegistryError, "already in use"):
                other.acquire()
        finally:
            lease.close()
        with self.assertRaisesRegex(RegistryError, "not the latest"):
            SessionLease(self.reg, current, source).acquire()

    def test_unsupported_session_combinations_rejected(self):
        for args in (("-a", "claude-code", "--persist-session", "task"),
                     ("-a", "codex", "--one-shot", "--persist-session", "task")):
            p = self.cli(*args)
            self.assertNotEqual(p.returncode, 0)
            self.assertIn("require steerable Codex", p.stderr)
        self.assertFalse(self.rpc_calls())

    def test_detached_continue(self):
        source = self.start_durable()
        p = self.cli("-a", "codex", "--continue-run", source, "--detach", "followup")
        self.assertEqual(p.returncode, 0, p.stderr)
        rid = p.stdout.strip()
        result = self.cli("wait", rid, "--timeout", "10", "--json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["status"], "completed")
        self.assertEqual(self.reg.load_meta(rid)["continued_from"], source)


if __name__ == "__main__":
    unittest.main()
