"""Offline platform regressions, runnable with native Python on Windows/POSIX."""
from __future__ import annotations

import importlib
import json
import os
import pkgutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

LIB = Path(__file__).resolve().parents[1] / "lib"
sys.path.insert(0, str(LIB))
import steer
from steer import util
from steer.registry import Registry, RegistryError
from steer.session import SessionLease
from steer.waiter import wait_for_any


class PlatformTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="consilium platform ü ")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.env = dict(os.environ, PYTHONPATH=str(LIB), PYTHONIOENCODING="utf-8",
                        PYTHONDONTWRITEBYTECODE="1")

    def python(self, code, *args, **kwargs):
        return subprocess.run([sys.executable, "-c", code, *map(str, args)],
                              env=self.env, capture_output=True, text=True,
                              encoding="utf-8", timeout=15, **kwargs)

    def record(self, reg, status="running", **extra):
        rid = reg.create_run(agent_id="codex", backend="codex-cli", model="test",
                             cwd=str(self.root), artifacts_dir="", extra=extra)
        reg.update_meta(rid, status=status, exit_code=0 if status == "completed" else None)
        return rid

    def test_all_modules_import(self):
        for module in pkgutil.walk_packages(steer.__path__, steer.__name__ + "."):
            importlib.import_module(module.name)
        importlib.import_module("terminal_guard")

    def test_liveness_does_not_kill(self):
        child = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(30)"])
        try:
            self.assertTrue(util.pid_alive(child.pid))
            time.sleep(0.1)
            self.assertIsNone(child.poll())
            self.assertFalse(util.pid_alive(9999999))
        finally:
            child.kill()
            child.wait()
        self.assertFalse(util.pid_alive(child.pid))

    def test_lock_contention_is_immediate_and_release_allows_another_process(self):
        lock = self.root / "run.lock"
        lock.write_text("non-empty lock\n", encoding="utf-8")
        code = """
import sys
from pathlib import Path
from steer.util import flock_exclusive
try:
    with flock_exclusive(Path(sys.argv[1]), blocking=False):
        print('acquired')
except BlockingIOError:
    print('busy')
"""
        for _ in range(2):
            with util.flock_exclusive(lock):
                started = time.monotonic()
                result = self.python(code, lock)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.strip(), "busy")
                self.assertLess(time.monotonic() - started, 5)
            result = self.python(code, lock)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), "acquired")

    def test_busy_run_lock_does_not_overrun_wait_deadline(self):
        reg = Registry(self.root / "registry")
        rid = self.record(reg, pid=9999999)
        with reg.with_run_lock(rid):
            started = time.monotonic()
            snaps, timed_out = wait_for_any(reg, [rid], timeout=1, poll_interval=0.05)
            self.assertTrue(timed_out)
            self.assertEqual(snaps[rid].status, "running")
            self.assertLess(time.monotonic() - started, 3)

    def test_session_continuation_is_exclusive_and_never_replayed(self):
        reg = Registry(self.root / "registry")
        source = self.record(reg, "completed")
        handle = {"backend": "codex-cli", "thread_id": "test", "anchor_run_id": source}
        reg.update_meta(source, session_handle=handle)
        util.atomic_write_json(reg.run_path(source) / "session.json", {"latest_run_id": source})
        current = self.record(reg)
        lease = SessionLease(reg, current, source)
        lease.acquire()
        try:
            result = self.python("""
import sys
from pathlib import Path
from steer.registry import Registry, RegistryError
from steer.session import SessionLease
lease = SessionLease(Registry(Path(sys.argv[1])), sys.argv[2], sys.argv[3])
try:
    lease.acquire()
except RegistryError as exc:
    print(exc)
else:
    lease.close()
    raise AssertionError('concurrent continuation accepted')
""", reg.root, current, source)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("already in use", result.stdout)
        finally:
            lease.close()
        with self.assertRaisesRegex(RegistryError, "not the latest"):
            SessionLease(reg, current, source).acquire()

    def test_lock_refuses_symlink(self):
        target = self.root / "target"
        target.write_text("unchanged", encoding="utf-8")
        link = self.root / "link"
        try:
            link.symlink_to(target)
        except OSError as exc:
            self.skipTest(f"symlink creation unavailable: {exc}")
        with self.assertRaises(OSError):
            fd = util.open_lock_fd(link)
            os.close(fd)
        self.assertEqual(target.read_text(encoding="utf-8"), "unchanged")

    def test_process_tree_cancellation(self):
        marker = self.root / "child.pid"
        code = "import subprocess,sys,time; from pathlib import Path; p=subprocess.Popen([sys.executable,'-c','import time; time.sleep(60)']); Path(sys.argv[1]).write_text(str(p.pid)); time.sleep(60)"
        proc = subprocess.Popen([sys.executable, "-c", code, str(marker)], **util.detached_popen_kwargs())
        try:
            deadline = time.monotonic() + 10
            while not marker.exists() and time.monotonic() < deadline:
                time.sleep(0.05)
            self.assertTrue(marker.exists())
            child_pid = int(marker.read_text())
            util.kill_process_group(proc.pid)
            proc.wait(timeout=10)
            # Windows has no zombie state; assert both members are gone. POSIX
            # descendants can remain zombies until the system reaper runs.
            if os.name == "nt":
                self.assertFalse(util.pid_alive(child_pid), "descendant survived cancellation")
        finally:
            if proc.poll() is None:
                util.kill_process_group(proc.pid)
                proc.wait(timeout=10)

    def test_taskkill_failure_is_observable(self):
        with patch.object(util, "system_executable", return_value="system-taskkill"), \
             patch.object(util.subprocess, "run", return_value=subprocess.CompletedProcess([], 5)), \
             patch.object(util, "pid_alive", return_value=False):
            with self.assertRaisesRegex(RuntimeError, "exit 5"):
                util.taskkill_tree(123)

    def test_taskkill_timeout_is_observable(self):
        with patch.object(util, "system_executable", return_value="system-taskkill"), \
             patch.object(util.subprocess, "run", return_value=subprocess.CompletedProcess([], 0)), \
             patch.object(util, "pid_alive", return_value=True):
            with self.assertRaises(TimeoutError):
                util.taskkill_tree(123, timeout=0)

    def test_missing_system_tool_never_searches_path(self):
        with patch.dict(os.environ, {"SystemRoot": str(self.root)}):
            with self.assertRaises(FileNotFoundError):
                util.system_executable("taskkill.exe")

    def test_terminal_guard_stops_completed_backend(self):
        event = '{"type":"session.complete"}'
        result = subprocess.run(
            [sys.executable, str(LIB / "terminal_guard.py"), "--backend", "opencode",
             "--terminal-grace", "0.1", "--", sys.executable, "-c",
             f"import time; print({event!r}, flush=True); time.sleep(60)"],
            stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=20,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(event, result.stdout)

    def test_terminal_guard_reports_timer_failure_without_hanging(self):
        result = self.python(r"""
import sys
import terminal_guard as guard
real_signal = guard.signal_tree
calls = 0
def fail_once(proc, *, force):
    global calls
    calls += 1
    if calls == 1:
        raise RuntimeError('injected taskkill failure')
    return real_signal(proc, force=force)
guard.signal_tree = fail_once
sys.argv = ['terminal_guard', '--backend', 'opencode', '--terminal-grace', '0.1',
            '--', sys.executable, '-c',
            'import time; print(\'{"type":"session.complete"}\', flush=True); time.sleep(60)']
guard.main()
""")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("backend process-tree cleanup failed", result.stderr)

    @unittest.skipUnless(os.name == "nt", "native Windows launcher contract")
    def test_python_shebang_preserves_argv(self):
        script = self.root / "python-launcher"
        script.write_text("#!/usr/bin/env python3\nimport json,sys; print(json.dumps(sys.argv[1:], ensure_ascii=False))\n", encoding="utf-8")
        args = ["a b", 'quote"', "$(no-command)", "x&y", "ü"]
        result = subprocess.run(util.resolve_argv([str(script), *args]),
                                capture_output=True, text=True, encoding="utf-8", timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), args)

    @unittest.skipUnless(os.name == "nt", "native Windows launcher contract")
    def test_shell_shebang_preserves_argv(self):
        script = self.root / "shell-launcher"
        script.write_text('#!/bin/sh\nprintf "%s\\n" "$@"\n', encoding="utf-8")
        args = ["a b", "$(no-command)", "x&y", "ü"]
        result = subprocess.run(util.resolve_argv([str(script), *args]),
                                capture_output=True, text=True, encoding="utf-8", timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), args)

    @unittest.skipUnless(os.name == "nt", "native Windows launcher contract")
    def test_batch_launcher_and_rejection_of_shell_syntax(self):
        script = self.root / "batch.cmd"
        script.write_text('@echo off\necho %~1\n', encoding="utf-8")
        result = subprocess.run(util.resolve_argv([str(script), "two words"]),
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), "two words")
        with self.assertRaises(ValueError):
            util.resolve_argv([str(script), "x&echo INJECTED"])

    @unittest.skipUnless(os.name == "nt", "native Windows launcher contract")
    def test_unknown_shebang_is_rejected(self):
        script = self.root / "unknown"
        script.write_text("#!/usr/bin/ruby\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unsupported shebang"):
            util.resolve_argv([str(script)])

    def test_native_supervisor_durable_codex_followup(self):
        tests = Path(__file__).resolve().parent
        env = dict(self.env, CONSILIUM_CONFIG=str(tests / "fixtures/test-config.json"),
                   CONSILIUM_BIN_CODEX=str(tests / "fakes/steer/fake-codex-steer"),
                   CONSILIUM_FAKE_STEER_SLOW="0.01",
                   CONSILIUM_FAKE_RPC_LOG=str(self.root / "rpc.jsonl"))
        root = self.root / "registry"
        previous = None
        for index, prompt in enumerate(("INITIAL_ONLY", "FOLLOWUP_ONLY")):
            task = self.root / "task.txt"
            task.write_text(prompt, encoding="utf-8")
            rid_file = self.root / f"run-{index}.txt"
            args = [sys.executable, "-m", "steer.supervisor", "--agent-id", "codex",
                    "--task-file", str(task), "--cwd", str(self.root),
                    "--registry-root", str(root), "--run-id-file", str(rid_file),
                    "--persist-session", "--detach-setsid"]
            if previous:
                args += ["--continue-run", previous]
            result = subprocess.run(args, env=env, capture_output=True, text=True,
                                    encoding="utf-8", timeout=25)
            self.assertEqual(result.returncode, 0, result.stderr)
            rid = rid_file.read_text(encoding="utf-8").strip()
            meta = Registry(root).load_meta(rid)
            self.assertEqual(meta["status"], "completed")
            if previous:
                self.assertEqual(meta["continued_from"], previous)
                self.assertEqual(meta["session_handle"]["thread_id"], old_thread)
            old_thread = meta["session_handle"]["thread_id"]
            previous = rid
        calls = [json.loads(line) for line in (self.root / "rpc.jsonl").read_text(encoding="utf-8").splitlines()]
        turns = [call for call in calls if call.get("method") == "turn/start"]
        self.assertEqual(len(turns), 2)
        self.assertNotIn("INITIAL_ONLY", json.dumps(turns[1]))
        self.assertIn("FOLLOWUP_ONLY", json.dumps(turns[1]))


if __name__ == "__main__":
    unittest.main()
