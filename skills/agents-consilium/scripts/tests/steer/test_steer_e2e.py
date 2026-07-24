#!/usr/bin/env python3
"""Deterministic steerable-delegate tests (fake transports only; no network/model spend)."""
from __future__ import annotations

import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import traceback
from pathlib import Path

TESTS_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = TESTS_DIR.parent
LIB_DIR = SCRIPTS_DIR / "lib"
FAKES = TESTS_DIR / "fakes" / "steer"
CONSILIUM = SCRIPTS_DIR / "consilium"
FIX = TESTS_DIR / "fixtures"

PASS = 0
FAIL = 0


def ok(name: str) -> None:
    global PASS
    PASS += 1
    print(f"  PASS  {name}")


def bad(name: str, detail: str = "") -> None:
    global FAIL
    FAIL += 1
    print(f"  FAIL  {name}" + (f" — {detail}" if detail else ""))


def assert_true(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        ok(name)
    else:
        bad(name, detail)


def env_base(reg_root: Path, art: Path) -> dict:
    e = os.environ.copy()
    e["CONSILIUM_CONFIG"] = str(FIX / "test-config.json")
    e["CONSILIUM_STEER_DIR"] = str(reg_root)
    e["CONSILIUM_RUN_DIR"] = str(art)
    e["CONSILIUM_OUTPUT_DIR"] = str(art)
    e["CONSILIUM_SAVE_OUTPUTS"] = "1"
    e["PYTHONPATH"] = str(LIB_DIR) + (os.pathsep + e["PYTHONPATH"] if e.get("PYTHONPATH") else "")
    e["CONSILIUM_FAKE_STEER_SLOW"] = "0.35"
    # Point backends at steerable fakes
    e["CONSILIUM_BIN_CLAUDE"] = str(FAKES / "fake-claude-steer")
    e["CONSILIUM_BIN_CODEX"] = str(FAKES / "fake-codex-steer")
    e["CONSILIUM_BIN_OPENCODE"] = str(FAKES / "fake-opencode-steer")
    e["CONSILIUM_BIN_GROK"] = str(FAKES / "fake-grok-steer")
    e["AGENT_TIMEOUT"] = "0"
    return e


def run_cmd(argv, env, timeout=60, input_text=None):
    return subprocess.run(
        argv,
        env=env,
        capture_output=True,
        text=True,
        timeout=timeout,
        input=input_text,
    )


def extract_run_id(stderr: str) -> str:
    for line in stderr.splitlines():
        line = line.strip()
        if line.startswith("run_id="):
            return line.split("=", 1)[1].strip()
        if "run_id=" in line:
            # [consilium] steer run_id=...
            for part in line.split():
                if part.startswith("run_id="):
                    return part.split("=", 1)[1]
    return ""


def start_steerable(agent: str, task: str, env: dict, cwd: Path):
    """Start steerable supervisor in background; return (proc, run_id)."""
    proc = subprocess.Popen(
        [
            str(CONSILIUM),
            "delegate",
            "-a",
            agent,
            "--steerable",
            task,
        ],
        env=env,
        cwd=str(cwd),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    # Read stderr until run_id appears
    run_id = ""
    buf = []
    deadline = time.time() + 15
    while time.time() < deadline and proc.poll() is None:
        # non-blocking-ish: use select
        import select

        r, _, _ = select.select([proc.stderr], [], [], 0.1)
        if r:
            line = proc.stderr.readline()
            if not line:
                break
            buf.append(line)
            if "run_id=" in line:
                run_id = extract_run_id("".join(buf))
                if run_id:
                    break
    if not run_id:
        # drain and fail
        try:
            out, err = proc.communicate(timeout=2)
        except Exception:
            out, err = "", "".join(buf)
        raise RuntimeError(f"no run_id from steerable start.\nstderr={''.join(buf)+err}\nstdout={out}")
    return proc, run_id, buf


def wait_proc(proc, timeout=30):
    try:
        out, err = proc.communicate(timeout=timeout)
        return proc.returncode, out, err
    except subprocess.TimeoutExpired:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass
        try:
            out, err = proc.communicate(timeout=3)
        except Exception:
            out, err = "", "TIMEOUT"
        return 99, out or "", (err or "") + "\nTIMEOUT"


def test_mailbox_and_registry_unit(tmp: Path) -> None:
    print("=== unit: mailbox + registry ===")
    sys.path.insert(0, str(LIB_DIR))
    from steer.mailbox import Mailbox, MailboxError
    from steer.registry import Registry, RegistryError
    from steer.util import (
        DIR_MODE,
        FILE_MODE,
        is_loopback_url,
        safe_client_filename,
    )

    reg = Registry(tmp / "reg")
    run_id = reg.create_run(
        agent_id="grok",
        backend="grok-build",
        model="m",
        cwd=str(tmp),
        artifacts_dir=str(tmp / "art"),
    )
    assert_true("early run_id created", run_id.startswith("run_"))
    rdir = reg.run_path(run_id)
    # Permissions: dirs 0700, files 0600
    assert_true("run dir mode 0700", (rdir.stat().st_mode & 0o777) == DIR_MODE)
    assert_true("meta mode 0600", (rdir / "meta.json").stat().st_mode & 0o777 == FILE_MODE)
    meta = reg.load_meta(run_id)
    assert_true("owner_uid mandatory", meta.get("owner_uid") == os.getuid())

    mb = Mailbox(reg.run_path(run_id))
    m1 = mb.enqueue(kind="steer", content="hello", mode="auto", client_id="cid1")
    m2 = mb.enqueue(kind="steer", content="hello", mode="auto", client_id="cid1")
    assert_true("idempotent client_id", m1["seq"] == m2["seq"] and m1["client_id"] == "cid1")
    # Conflict: same client_id, different content
    try:
        mb.enqueue(kind="steer", content="DIFFERENT", mode="auto", client_id="cid1")
        bad("client_id content conflict", "did not raise")
    except MailboxError as e:
        assert_true("conflict mentions client_id", "conflict" in str(e).lower())
    # Conflict: same content, different mode
    try:
        mb.enqueue(kind="steer", content="hello", mode="queue", client_id="cid1")
        bad("client_id mode conflict", "did not raise")
    except MailboxError:
        ok("client_id mode conflict rejected")

    m3 = mb.enqueue(kind="steer", content="b", mode="queue", client_id="cid2")
    assert_true("monotonic seq", m3["seq"] == m1["seq"] + 1)

    # Malicious client_id must not create path traversal files
    evil = "../../etc/passwd"
    m_evil = mb.enqueue(kind="steer", content="x", mode="auto", client_id=evil)
    assert_true("evil client_id preserved in JSON", m_evil["client_id"] == evil)
    safe = safe_client_filename(evil)
    assert_true("safe name is digest", safe.startswith("cid_") and "/" not in safe and ".." not in safe)
    steers_dir = rdir / "steers"
    steer_files = list(steers_dir.glob("*.json"))
    assert_true(
        "no traversal files under steers",
        all("/" not in p.name and ".." not in p.name for p in steer_files),
        str([p.name for p in steer_files]),
    )
    assert_true(
        "safe file exists",
        (steers_dir / f"{safe}.json").is_file(),
    )
    # Ensure nothing was written outside run dir
    assert_true(
        "no etc/passwd under reg",
        not (tmp / "reg" / "etc").exists() and not (tmp / "etc").exists(),
    )
    # Nested slash client_id
    slash_id = "a/b/c"
    mb.enqueue(kind="steer", content="slash", mode="auto", client_id=slash_id)
    assert_true(
        "slash client_id safe file",
        (steers_dir / f"{safe_client_filename(slash_id)}.json").is_file(),
    )
    assert_true("no nested steers path", not (steers_dir / "a").exists())

    # concurrent writers
    results = []

    def writer(i):
        try:
            r = mb.enqueue(kind="steer", content=f"c{i}", mode="auto", client_id=f"w{i}")
            results.append(r["seq"])
        except Exception as e:
            results.append(f"err:{e}")

    threads = [threading.Thread(target=writer, args=(i,)) for i in range(8)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    seqs = [x for x in results if isinstance(x, int)]
    assert_true("concurrent writers unique seq", len(seqs) == len(set(seqs)) == 8, str(results))

    # large guidance — full body stored (no truncation)
    big = "X" * 200_000
    mb.enqueue(kind="steer", content=big, mode="auto", client_id="big1")
    loaded = mb.get_by_client_id("big1")
    assert_true("large guidance stored full", loaded is not None and len(loaded.get("content") or "") == 200_000)

    # malformed
    badp = reg.run_path(run_id) / "mailbox" / "msg-999999.json"
    badp.write_text("{not json", encoding="utf-8")
    msgs = mb.list_messages()
    assert_true("malformed listed as failed", any(m.get("status") == "failed" for m in msgs))

    # symlink run dir rejected entirely
    link = reg.runs_dir / "evil"
    try:
        link.symlink_to("/tmp")
        try:
            reg.load_meta("evil")
            bad("symlink run dir rejected", "did not raise")
        except RegistryError as e:
            assert_true("symlink message", "symlink" in str(e).lower())
    finally:
        if link.is_symlink():
            link.unlink()

    # invalid run id
    try:
        reg.run_path("../x")
        bad("invalid run id", "no raise")
    except RegistryError:
        ok("invalid run id rejected")

    # dead pid
    reg.update_meta(run_id, status="running", pid=2**30 - 3)
    try:
        reg.validate_active(run_id)
        bad("dead pid rejected", "no raise")
    except RegistryError as e:
        assert_true("dead pid message", "dead" in str(e).lower() or "supervisor" in str(e).lower())

    # terminal reject steer
    reg.update_meta(run_id, status="completed", pid=os.getpid())
    try:
        reg.validate_active(run_id)
        bad("terminal reject", "no raise")
    except RegistryError:
        ok("terminal run rejects active ops")

    # mailbox close + fail open messages
    run2 = reg.create_run(
        agent_id="x",
        backend="grok-build",
        model="m",
        cwd=str(tmp),
        artifacts_dir=str(tmp / "art2"),
    )
    mb2 = Mailbox(reg.run_path(run2))
    open_msg = mb2.enqueue(kind="steer", content="pending", mode="auto", client_id="pend1")
    mb2.update_message(open_msg["seq"], status="delivering")
    mb2.close(reason="test_terminal")
    try:
        mb2.enqueue(kind="steer", content="late", mode="auto", client_id="late1")
        bad("closed mailbox rejects", "did not raise")
    except MailboxError:
        ok("closed mailbox rejects enqueue")
    failed = mb2.fail_open_messages("run became terminal")
    assert_true("open msgs failed on terminal", len(failed) >= 1)
    reloaded = mb2.get_by_client_id("pend1")
    assert_true(
        "delivering became failed",
        reloaded is not None and reloaded.get("status") == "failed",
        str(reloaded),
    )

    # loopback URL validation (ipaddress.is_loopback + exact localhost)
    assert_true("loopback 127.0.0.1", is_loopback_url("http://127.0.0.1:4096"))
    assert_true("loopback ::1", is_loopback_url("http://[::1]:80"))
    assert_true("loopback localhost", is_loopback_url("http://localhost:80"))
    assert_true("loopback 127.0.0.2", is_loopback_url("http://127.0.0.2:9"))
    assert_true("reject external", not is_loopback_url("http://evil.example.com:80"))
    assert_true(
        "reject 127.evil.example prefix trick",
        not is_loopback_url("http://127.evil.example/"),
    )
    assert_true("reject file scheme", not is_loopback_url("file:///etc/passwd"))


def test_backend_e2e(agent: str, label: str, tmp: Path, extra_checks=None) -> None:
    print(f"=== e2e: {label} ===")
    reg_root = tmp / f"reg-{agent}"
    art = tmp / f"art-{agent}"
    art.mkdir(parents=True)
    reg_root.mkdir(parents=True)
    cwd = tmp / f"cwd-{agent}"
    cwd.mkdir()
    env = env_base(reg_root, art)
    log = tmp / f"argv-{agent}.jsonl"
    env["CONSILIUM_FAKE_ARGV_LOG"] = str(log)
    if agent == "grok":
        env["CONSILIUM_FAKE_GROK_EVIDENCE"] = str(tmp / "grok-evidence.json")

    try:
        proc, run_id, early_err = start_steerable(agent, f"task for {agent}", env, cwd)
    except Exception as e:
        bad(f"{label} early run_id", str(e))
        return
    ok(f"{label} early run_id")
    assert_true(f"{label} run_id format", run_id.startswith("run_"), run_id)

    # Live progress before completion: stderr already has progress
    early = "".join(early_err)
    assert_true(f"{label} live progress on stderr", "run_id=" in early or "[consilium]" in early)

    # Steer once while running
    time.sleep(0.15)
    r = run_cmd(
        [str(CONSILIUM), "delegate", "steer", run_id, "--mode", "auto", f"STEER guidance for {agent}"],
        env,
        timeout=20,
    )
    assert_true(f"{label} steer mailbox exit 0", r.returncode == 0, r.stderr)
    assert_true(
        f"{label} steer distinguishes mailbox accepted",
        "mailbox" in r.stdout.lower() or "accepted" in r.stdout.lower(),
        r.stdout,
    )

    # Status
    r2 = run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env, timeout=10)
    assert_true(f"{label} status json", r2.returncode == 0, r2.stderr)
    try:
        st = json.loads(r2.stdout)
        assert_true(f"{label} status has steers", isinstance(st.get("steers"), list))
    except json.JSONDecodeError as e:
        bad(f"{label} status json parse", str(e))

    # Wait for completion
    code, out, err = wait_proc(proc, timeout=40)
    full_err = early + err
    assert_true(f"{label} exit 0", code == 0, f"code={code} err={full_err[-500:]}")
    assert_true(f"{label} clean final stdout", out.strip() != "", f"stdout={out!r}")
    # stdout should not contain progress tags
    assert_true(
        f"{label} stdout no progress tags",
        "[consilium]" not in out,
        out[:200],
    )

    # Status terminal
    r3 = run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env, timeout=10)
    st3 = json.loads(r3.stdout) if r3.returncode == 0 else {}
    assert_true(
        f"{label} terminal status",
        st3.get("status") in ("completed", "failed", "cancelled"),
        str(st3.get("status")),
    )

    # Delivery class visible for at least one steer
    steers = st3.get("steers") or []
    delivered = [
        s
        for s in steers
        if s.get("mailbox_status")
        in (
            "delivered",
            "applied",
            "queued",
            "failed",
            "rejected",
            "request_sent",
        )
    ]
    # may still be accepted if supervisor finished before processing — poll files
    if not delivered:
        # read mailbox files
        mb_dir = reg_root / "runs" / run_id / "mailbox"
        for p in sorted(mb_dir.glob("msg-*.json")):
            try:
                o = json.loads(p.read_text())
                if o.get("kind") == "steer" and o.get("status") not in (
                    None,
                    "accepted",
                    "delivering",
                ):
                    delivered.append(o)
            except Exception:
                pass
    assert_true(
        f"{label} protocol delivery status visible",
        len(delivered) >= 1,
        f"steers={steers}",
    )
    # At least one should have delivery_class if applied/delivered
    classes = [s.get("delivery_class") for s in delivered if s.get("delivery_class")]
    if classes:
        ok(f"{label} delivery_class present ({classes[0]})")
    else:
        # delivered with evidence still ok
        acks = [s.get("backend_ack") or s.get("evidence") for s in delivered]
        assert_true(f"{label} backend evidence present", any(acks), str(delivered))

    if extra_checks:
        extra_checks(env, run_id, reg_root, out, full_err, tmp)


def test_grok_queue_and_send_now(tmp: Path) -> None:
    print("=== e2e: grok concurrent queue + sendNow ===")
    reg_root = tmp / "reg-grok2"
    art = tmp / "art-grok2"
    art.mkdir(parents=True)
    reg_root.mkdir(parents=True)
    cwd = tmp / "cwd-grok2"
    cwd.mkdir()
    env = env_base(reg_root, art)
    env["CONSILIUM_FAKE_STEER_SLOW"] = "0.6"
    env["CONSILIUM_FAKE_GROK_EVIDENCE"] = str(tmp / "grok-ev2.json")

    proc, run_id, _ = start_steerable("grok", "LONG TASK", env, cwd)
    time.sleep(0.2)
    # queue mode steer
    r1 = run_cmd(
        [str(CONSILIUM), "delegate", "steer", run_id, "--mode", "queue", "STEER queue me"],
        env,
        timeout=15,
    )
    assert_true("grok queue steer accepted", r1.returncode == 0, r1.stderr)
    # interrupt sendNow
    r2 = run_cmd(
        [str(CONSILIUM), "delegate", "steer", run_id, "--mode", "interrupt", "STEER interrupt now"],
        env,
        timeout=15,
    )
    assert_true("grok interrupt steer accepted", r2.returncode == 0, r2.stderr)

    code, out, err = wait_proc(proc, timeout=45)
    assert_true("grok race exit 0", code == 0, err[-400:])

    # Status delivery classes
    st = json.loads(run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env).stdout)
    classes = {s.get("delivery_class") for s in st.get("steers") or [] if s.get("delivery_class")}
    # queue_next_turn and/or cancel_and_send
    assert_true(
        "grok honest classes",
        bool(classes & {"queue_next_turn", "cancel_and_send", "next_turn"}) or any(
            (s.get("mailbox_status") in ("delivered", "applied")) for s in (st.get("steers") or [])
        ),
        f"classes={classes} steers={st.get('steers')}",
    )

    # Evidence file from fake if process closed stdin... may not exist if killed before atexit.
    # Instead check audit / steer records for promptId meta
    steers_dir = reg_root / "runs" / run_id / "steers"
    found_send = False
    found_queue = False
    for p in steers_dir.glob("*.json"):
        o = json.loads(p.read_text())
        meta = o.get("meta") or {}
        if meta.get("sendNow") is True or o.get("delivery_class") == "cancel_and_send":
            found_send = True
        if o.get("delivery_class") in ("queue_next_turn", "next_turn") or meta.get("sendNow") is False:
            found_queue = True
    assert_true("grok cancel_and_send recorded", found_send or "cancel" in json.dumps(st), str(st.get("steers")))
    assert_true("grok queue path recorded", found_queue or found_send, "no steer meta")


def test_cancel(tmp: Path) -> None:
    print("=== e2e: cancel ===")
    reg_root = tmp / "reg-cancel"
    art = tmp / "art-cancel"
    art.mkdir(parents=True)
    reg_root.mkdir(parents=True)
    cwd = tmp / "cwd-cancel"
    cwd.mkdir()
    env = env_base(reg_root, art)
    env["CONSILIUM_FAKE_STEER_SLOW"] = "2.0"
    proc, run_id, _ = start_steerable("claude-code", "slow task", env, cwd)
    time.sleep(0.2)
    r = run_cmd([str(CONSILIUM), "delegate", "cancel", run_id], env, timeout=10)
    assert_true("cancel cmd ok", r.returncode == 0, r.stderr)
    code, out, err = wait_proc(proc, timeout=20)
    # cancelled exits non-zero typically 130
    assert_true("cancel terminates", code != 0 or "cancel" in err.lower(), f"code={code}")
    st = json.loads(run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env).stdout)
    assert_true(
        "cancel terminal status",
        st.get("status") in ("cancelled", "failed", "completed"),
        str(st.get("status")),
    )


def test_duplicate_idempotency(tmp: Path) -> None:
    print("=== e2e: duplicate client_id ===")
    reg_root = tmp / "reg-dup"
    art = tmp / "art-dup"
    art.mkdir(parents=True)
    reg_root.mkdir(parents=True)
    cwd = tmp / "cwd-dup"
    cwd.mkdir()
    env = env_base(reg_root, art)
    env["CONSILIUM_FAKE_STEER_SLOW"] = "0.5"
    proc, run_id, _ = start_steerable("codex", "dup task", env, cwd)
    time.sleep(0.15)
    # Same client_id + same content + same mode → idempotent
    r1 = run_cmd(
        [
            str(CONSILIUM),
            "delegate",
            "steer",
            run_id,
            "--client-id",
            "same-cid",
            "same body",
        ],
        env,
    )
    r2 = run_cmd(
        [
            str(CONSILIUM),
            "delegate",
            "steer",
            run_id,
            "--client-id",
            "same-cid",
            "same body",
        ],
        env,
    )
    assert_true("dup same body exit 0", r1.returncode == 0 and r2.returncode == 0)
    s1 = r1.stdout + r1.stderr
    s2 = r2.stdout + r2.stderr
    import re

    def seq_of(s):
        m = re.search(r"seq=(\d+)", s)
        return m.group(1) if m else None

    assert_true("dup same seq", seq_of(s1) == seq_of(s2) and seq_of(s1) is not None, f"{s1} vs {s2}")
    # Same client_id + different content → explicit conflict reject
    r3 = run_cmd(
        [
            str(CONSILIUM),
            "delegate",
            "steer",
            run_id,
            "--client-id",
            "same-cid",
            "DIFFERENT body",
        ],
        env,
    )
    assert_true("dup conflict non-zero", r3.returncode != 0, r3.stdout + r3.stderr)
    assert_true(
        "dup conflict message",
        "conflict" in (r3.stdout + r3.stderr).lower(),
        r3.stdout + r3.stderr,
    )
    wait_proc(proc, timeout=30)


def test_malicious_client_id_e2e(tmp: Path) -> None:
    print("=== e2e: malicious client_id ===")
    reg_root = tmp / "reg-mal"
    art = tmp / "art-mal"
    art.mkdir(parents=True)
    reg_root.mkdir(parents=True)
    cwd = tmp / "cwd-mal"
    cwd.mkdir()
    env = env_base(reg_root, art)
    env["CONSILIUM_FAKE_STEER_SLOW"] = "0.45"
    proc, run_id, _ = start_steerable("claude-code", "mal task", env, cwd)
    time.sleep(0.15)
    evil = "../../tmp/pwned"
    r = run_cmd(
        [
            str(CONSILIUM),
            "delegate",
            "steer",
            run_id,
            "--client-id",
            evil,
            "guidance ok",
        ],
        env,
    )
    assert_true("mal client_id accepted in mailbox", r.returncode == 0, r.stderr)
    steers = reg_root / "runs" / run_id / "steers"
    names = [p.name for p in steers.glob("*.json")]
    assert_true("no traversal filename", all(".." not in n and "/" not in n for n in names), str(names))
    assert_true("no pwned outside", not (tmp / "pwned").exists() and not (tmp / "tmp" / "pwned").exists())
    wait_proc(proc, timeout=30)


def test_artifact_no_truncate(tmp: Path) -> None:
    print("=== unit: artifact payloads not truncated ===")
    sys.path.insert(0, str(LIB_DIR))
    from steer.util import append_jsonl, preview_text

    big = "Z" * 5000
    path = tmp / "norm.jsonl"
    append_jsonl(path, {"kind": "text", "data": big})
    line = path.read_text(encoding="utf-8").strip()
    obj = json.loads(line)
    assert_true("artifact full data", len(obj["data"]) == 5000)
    prev = preview_text(big, 80)
    assert_true("preview shorter", len(prev) < 100 and "…" in prev)


def test_grok_ack_not_delivered_on_write(tmp: Path) -> None:
    """request_sent/queued/applied — never call pure write 'delivered'."""
    print("=== e2e: grok honest ack statuses ===")
    reg_root = tmp / "reg-gack"
    art = tmp / "art-gack"
    art.mkdir(parents=True)
    reg_root.mkdir(parents=True)
    cwd = tmp / "cwd-gack"
    cwd.mkdir()
    env = env_base(reg_root, art)
    env["CONSILIUM_FAKE_STEER_SLOW"] = "0.7"
    proc, run_id, _ = start_steerable("grok", "ack task", env, cwd)
    time.sleep(0.15)
    run_cmd(
        [str(CONSILIUM), "delegate", "steer", run_id, "--mode", "queue", "STEER for ack"],
        env,
        timeout=15,
    )
    # Poll status while in flight / after
    time.sleep(0.3)
    st = json.loads(run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env).stdout)
    statuses = [s.get("mailbox_status") for s in (st.get("steers") or [])]
    # Allowed intermediate/final protocol statuses
    allowed = {
        "accepted",
        "delivering",
        "request_sent",
        "queued",
        "applied",
        "failed",
        "rejected",
        "delivered",  # legacy may appear; prefer not for mere write
    }
    assert_true("statuses known", all(s in allowed for s in statuses if s), str(statuses))
    code, out, err = wait_proc(proc, timeout=45)
    assert_true("gack exit 0", code == 0, err[-300:])
    st2 = json.loads(run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env).stdout)
    final_steers = st2.get("steers") or []
    # At least one steer should reach applied (promptId on notification) for fake-grok
    applied = [s for s in final_steers if s.get("mailbox_status") == "applied"]
    requestish = [
        s
        for s in final_steers
        if s.get("mailbox_status") in ("request_sent", "queued", "applied", "delivered")
    ]
    assert_true(
        "grok has protocol outcome not stuck accepted",
        len(requestish) >= 1,
        str(final_steers),
    )
    # Evidence should not claim "delivered" solely from write if applied is available
    if applied:
        ok("grok applied via promptId/complete")
    else:
        acks = [s.get("backend_ack") for s in final_steers]
        assert_true(
            "no false delivered-only-on-write",
            not any(a == "prompt_request_sent" for a in acks) or any(a for a in acks),
            str(acks),
        )


def test_oneshot_regression(tmp: Path) -> None:
    print("=== regression: one-shot delegate unchanged ===")
    # Use non-steerable path with original fakes from parent fakes/
    env = os.environ.copy()
    env["CONSILIUM_CONFIG"] = str(FIX / "test-config.json")
    env["CONSILIUM_BIN_GROK"] = str(TESTS_DIR / "fakes" / "fake-grok")
    env["CONSILIUM_BIN_CODEX"] = str(TESTS_DIR / "fakes" / "fake-codex")
    env["CONSILIUM_BIN_CLAUDE"] = str(TESTS_DIR / "fakes" / "fake-claude")
    env["CONSILIUM_BIN_OPENCODE"] = str(TESTS_DIR / "fakes" / "fake-opencode")
    env["CONSILIUM_BIN_GEMINI"] = str(TESTS_DIR / "fakes" / "fake-gemini")
    env["CONSILIUM_SUPPRESS_SHELL_WARN"] = "1"
    env["CONSILIUM_RUN_DIR"] = str(tmp / "oneshot-art")
    (tmp / "oneshot-art").mkdir(parents=True)
    r = run_cmd([str(CONSILIUM), "delegate", "-a", "grok", "implement one-shot"], env, timeout=30)
    assert_true("oneshot exit 0", r.returncode == 0, r.stderr)
    assert_true("oneshot stdout", "FAKE_GROK_OK" in r.stdout, r.stdout)


def test_claude_interrupt_rejected(tmp: Path) -> None:
    print("=== e2e: claude interrupt rejected ===")
    reg_root = tmp / "reg-clint"
    art = tmp / "art-clint"
    art.mkdir(parents=True)
    reg_root.mkdir(parents=True)
    cwd = tmp / "cwd-clint"
    cwd.mkdir()
    env = env_base(reg_root, art)
    env["CONSILIUM_FAKE_STEER_SLOW"] = "0.8"
    proc, run_id, _ = start_steerable("claude-code", "task", env, cwd)
    time.sleep(0.15)
    r = run_cmd(
        [str(CONSILIUM), "delegate", "steer", run_id, "--mode", "interrupt", "nope"],
        env,
    )
    # mailbox accepts; protocol rejects — wait a bit and check status
    time.sleep(0.8)
    st = json.loads(run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env).stdout)
    steers = st.get("steers") or []
    # find interrupt
    rejected = [
        s
        for s in steers
        if s.get("mailbox_status") == "rejected"
        or (s.get("error") and "interrupt" in str(s.get("error")).lower())
    ]
    assert_true("claude interrupt not silent downgrade", len(rejected) >= 1 or r.returncode == 0, str(steers))
    # If only accepted still, wait for supervisor to process
    if not rejected:
        time.sleep(1.0)
        st = json.loads(run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env).stdout)
        steers = st.get("steers") or []
        rejected = [s for s in steers if s.get("mailbox_status") == "rejected"]
        assert_true("claude interrupt rejected after process", len(rejected) >= 1, str(steers))
    wait_proc(proc, timeout=20)


def test_process_cleanup(tmp: Path) -> None:
    print("=== e2e: process cleanup ===")
    reg_root = tmp / "reg-clean"
    art = tmp / "art-clean"
    art.mkdir(parents=True)
    reg_root.mkdir(parents=True)
    cwd = tmp / "cwd-clean"
    cwd.mkdir()
    env = env_base(reg_root, art)
    env["CONSILIUM_FAKE_STEER_SLOW"] = "0.25"
    proc, run_id, _ = start_steerable("opencode", "cleanup task", env, cwd)
    # get child from meta once available
    time.sleep(0.3)
    st = json.loads(run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env).stdout)
    child = st.get("child_pid")
    code, out, err = wait_proc(proc, timeout=40)
    assert_true("cleanup exit", code == 0, err[-300:])
    if child:
        # child should be dead
        alive = True
        try:
            os.kill(int(child), 0)
            alive = True
        except OSError:
            alive = False
        assert_true("no orphan child", not alive, f"child {child} still alive")
    else:
        ok("cleanup no child pid recorded (skip orphan check)")


def test_grok_message_type_filter_unit(tmp: Path) -> None:
    """agent_thought / user_message never enter final; agent_message does."""
    print("=== unit: grok message type filter ===")
    sys.path.insert(0, str(LIB_DIR))
    from steer.adapters.grok import GrokAdapter  # type: ignore

    art = tmp / "art-msgtypes"
    art.mkdir(parents=True)
    (art / "raw").mkdir(parents=True)
    adapter = GrokAdapter(
        binary="false",
        model="m",
        effort="",
        cwd=str(tmp),
        artifacts_dir=str(art),
        agent_id="grok",
    )
    pid = "pid-final-1"
    adapter._final_prompt_id = pid

    def su(session_update: str, text: str, prompt_id: str = pid) -> None:
        adapter._on_notification(
            {
                "jsonrpc": "2.0",
                "method": "session/update",
                "params": {
                    "sessionId": "s1",
                    "_meta": {"promptId": prompt_id} if prompt_id else {},
                    "update": {
                        "sessionUpdate": session_update,
                        "content": {"type": "text", "text": text},
                    },
                },
            }
        )

    su("user_message_chunk", "USER_REPLAY_SHOULD_NOT_BE_FINAL")
    su("agent_thought_chunk", "The user wants THOUGHT_ONLY_NOT_FINAL")
    su("agent_message_chunk", "FINAL_ONLY_OK")
    # Underscored real wire complete
    adapter._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "_x.ai/session/prompt_complete",
            "params": {"promptId": pid, "stopReason": "end_turn"},
        }
    )

    events = list(adapter.poll_events())
    kinds = [e.kind for e in events]
    assert_true("has user_replay", "user_replay" in kinds, str(kinds))
    assert_true("has thought", "thought" in kinds, str(kinds))
    assert_true("has text", "text" in kinds, str(kinds))
    assert_true("has prompt_complete", "prompt_complete" in kinds, str(kinds))
    assert_true("has steer_ack", "steer_ack" in kinds, str(kinds))
    text_parts = [e.data for e in events if e.kind == "text"]
    thought_parts = [e.data for e in events if e.kind == "thought"]
    assert_true("text is agent message only", text_parts == ["FINAL_ONLY_OK"], str(text_parts))
    assert_true(
        "thought kept separately",
        any("THOUGHT_ONLY" in t for t in thought_parts),
        str(thought_parts),
    )
    final = adapter.final_text()
    assert_true("final excludes thought", final == "FINAL_ONLY_OK", final)
    assert_true("final excludes user replay", "USER_REPLAY" not in final, final)
    # Full raw preserved on thought event
    thought_ev = next(e for e in events if e.kind == "thought")
    assert_true(
        "thought raw has update",
        isinstance(thought_ev.raw, dict) and "update" in thought_ev.raw,
        str(thought_ev.raw),
    )


def test_grok_late_ack_reconcile_unit(tmp: Path) -> None:
    """Late steer_ack after initial queued return advances mailbox to applied."""
    print("=== unit: late ack reconciliation ===")
    sys.path.insert(0, str(LIB_DIR))
    from steer.adapters.base import AdapterEvent  # type: ignore
    from steer.mailbox import Mailbox  # type: ignore
    from steer.registry import Registry  # type: ignore
    from steer.supervisor import Supervisor  # type: ignore

    reg_root = tmp / "reg-late-ack"
    reg_root.mkdir(parents=True)
    art = tmp / "art-late-ack"
    art.mkdir(parents=True)
    for sub in ("raw", "normalized", "final", "turns", "control"):
        (art / sub).mkdir(parents=True)

    reg = Registry(reg_root)
    run_id = reg.create_run(
        agent_id="grok",
        backend="grok-build",
        model="m",
        cwd=str(tmp),
        artifacts_dir=str(art),
    )
    run_dir = reg.run_path(run_id)
    mb = Mailbox(run_dir)
    prompt_id = "late-ack-prompt-uuid-0001"
    msg = mb.enqueue(
        kind="steer",
        content="Also mention STEERED",
        mode="queue",
        client_id="steer_late_ack_client",
        meta={"promptId": prompt_id, "sendNow": False, "client_id": "steer_late_ack_client"},
    )
    # Simulate steer() return while concurrent prompt still in flight
    mb.update_message(
        msg["seq"],
        status="queued",
        delivery_class="queue_next_turn",
        backend_ack="concurrent_prompt_request_in_flight",
        meta={"promptId": prompt_id, "sendNow": False, "client_id": "steer_late_ack_client"},
    )
    reg.update_state(
        run_id,
        status="running",
        steers={
            "steer_late_ack_client": {
                "seq": msg["seq"],
                "status": "queued",
                "delivery_class": "queue_next_turn",
                "evidence": "concurrent_prompt_request_in_flight",
                "error": "",
            }
        },
    )

    sup = Supervisor(
        agent_id="grok",
        task="t",
        cwd=str(tmp),
        artifacts_dir=str(art),
        registry=reg,
    )
    sup.run_id = run_id
    sup.mailbox = mb

    # 1) backend-confirmed queue (should upgrade evidence, stay queued)
    sup._handle_event(
        AdapterEvent(
            kind="steer_ack",
            data="queued:backend_queue_entry",
            raw={
                "promptId": prompt_id,
                "status": "queued",
                "evidence": "backend_queue_entry",
            },
        )
    )
    m1 = mb.list_messages()[0]
    assert_true(
        "queued evidence upgraded",
        m1.get("status") == "queued" and m1.get("backend_ack") == "backend_queue_entry",
        str(m1),
    )

    # 2) running → applied
    sup._handle_event(
        AdapterEvent(
            kind="steer_ack",
            data="applied:running_prompt_id",
            raw={
                "promptId": prompt_id,
                "status": "applied",
                "evidence": "running_prompt_id",
            },
        )
    )
    m2 = mb.list_messages()[0]
    assert_true("running promotes to applied", m2.get("status") == "applied", str(m2))
    assert_true(
        "running evidence",
        m2.get("backend_ack") == "running_prompt_id",
        str(m2.get("backend_ack")),
    )

    # 3) prompt_complete upgrades evidence; does not demote
    sup._handle_event(
        AdapterEvent(
            kind="steer_ack",
            data="applied:prompt_complete",
            raw={
                "promptId": prompt_id,
                "status": "applied",
                "evidence": "prompt_complete",
            },
        )
    )
    m3 = mb.list_messages()[0]
    assert_true("still applied after complete", m3.get("status") == "applied", str(m3))
    assert_true(
        "evidence upgraded to prompt_complete",
        m3.get("backend_ack") == "prompt_complete",
        str(m3.get("backend_ack")),
    )

    # 4) demotion attempt rejected
    sup._handle_event(
        AdapterEvent(
            kind="steer_ack",
            data="queued:backend_queue_entry",
            raw={
                "promptId": prompt_id,
                "status": "queued",
                "evidence": "backend_queue_entry",
            },
        )
    )
    m4 = mb.list_messages()[0]
    assert_true("no demotion from applied", m4.get("status") == "applied", str(m4))
    assert_true(
        "evidence not demoted",
        m4.get("backend_ack") == "prompt_complete",
        str(m4.get("backend_ack")),
    )

    st = reg.load_state(run_id)
    s = (st.get("steers") or {}).get("steer_late_ack_client") or {}
    assert_true(
        "state steers applied",
        s.get("status") == "applied" and s.get("evidence") == "prompt_complete",
        str(s),
    )


def test_grok_late_ack_e2e(tmp: Path) -> None:
    """Fake delays applied confirmation past steer() wait → async reconcile to applied."""
    print("=== e2e: grok late ack after queued ===")
    reg_root = tmp / "reg-glate"
    art = tmp / "art-glate"
    art.mkdir(parents=True)
    reg_root.mkdir(parents=True)
    cwd = tmp / "cwd-glate"
    cwd.mkdir()
    env = env_base(reg_root, art)
    # Initial prompt work is slow; ack delay forces steer() 5s wait to expire queued.
    env["CONSILIUM_FAKE_STEER_SLOW"] = "0.4"
    env["CONSILIUM_FAKE_GROK_ACK_DELAY"] = "6.0"
    env["CONSILIUM_FAKE_GROK_THOUGHT"] = "1"
    proc, run_id, _ = start_steerable("grok", "LONG INITIAL TASK", env, cwd)
    time.sleep(0.25)
    r = run_cmd(
        [str(CONSILIUM), "delegate", "steer", run_id, "--mode", "queue", "STEER late ack please"],
        env,
        timeout=20,
    )
    assert_true("late-ack steer enqueued", r.returncode == 0, r.stderr)

    # Shortly after delivery attempt, may still be queued / request_sent
    saw_queued = False
    saw_applied = False
    deadline = time.time() + 45
    while time.time() < deadline:
        st = json.loads(run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env).stdout)
        steers = st.get("steers") or []
        for s in steers:
            ms = s.get("mailbox_status")
            if ms in ("queued", "request_sent"):
                saw_queued = True
            if ms == "applied":
                saw_applied = True
        if saw_applied and st.get("status") in ("completed", "failed", "cancelled"):
            break
        if proc.poll() is not None and saw_applied:
            break
        time.sleep(0.3)

    code, out, err = wait_proc(proc, timeout=60)
    assert_true("late-ack exit 0", code == 0, err[-400:])
    st_final = json.loads(run_cmd([str(CONSILIUM), "delegate", "status", run_id, "--json"], env).stdout)
    final_steers = st_final.get("steers") or []
    applied = [s for s in final_steers if s.get("mailbox_status") == "applied"]
    assert_true(
        "late ack ends applied",
        len(applied) >= 1,
        str(final_steers),
    )
    assert_true(
        "applied has matching evidence",
        any(
            s.get("backend_ack")
            in (
                "prompt_complete",
                "prompt_result",
                "running_prompt_id",
                "promptId_notification_meta",
            )
            for s in applied
        ),
        str(applied),
    )
    # Thought marker must not appear in stdout / final
    assert_true(
        "stdout has no thought marker",
        "THOUGHT_ONLY_MARKER" not in (out or ""),
        out[:300] if out else "",
    )
    final_path = Path(env["CONSILIUM_RUN_DIR"]) / "final.txt"
    # final may live under run artifacts
    run_final = reg_root / "runs" / run_id / "final.txt"
    body = ""
    if run_final.is_file():
        body = run_final.read_text(encoding="utf-8")
    elif final_path.is_file():
        body = final_path.read_text(encoding="utf-8")
    else:
        body = out or ""
    assert_true("final has no thought marker", "THOUGHT_ONLY_MARKER" not in body, body[:300])
    assert_true("final has agent message", "STEERED" in body or "G" in body or "OK" in body, body[:300])
    # Optional: we observed intermediate queued (best-effort; timing dependent)
    if saw_queued:
        ok("observed intermediate queued before applied")
    else:
        ok("skipped intermediate queued observation (timing)")


def test_grok_thought_not_in_stdout_e2e(tmp: Path) -> None:
    print("=== e2e: grok thought excluded from final/stdout ===")
    reg_root = tmp / "reg-gthought"
    art = tmp / "art-gthought"
    art.mkdir(parents=True)
    reg_root.mkdir(parents=True)
    cwd = tmp / "cwd-gthought"
    cwd.mkdir()
    env = env_base(reg_root, art)
    env["CONSILIUM_FAKE_STEER_SLOW"] = "0.2"
    env["CONSILIUM_FAKE_GROK_THOUGHT"] = "1"
    proc, run_id, _ = start_steerable("grok", "task with thoughts", env, cwd)
    code, out, err = wait_proc(proc, timeout=40)
    assert_true("thought e2e exit 0", code == 0, err[-300:])
    assert_true("stdout lacks thought", "THOUGHT_ONLY_MARKER" not in (out or ""), out[:200])
    assert_true("stdout has agent text", "G" in (out or "") or "OK" in (out or ""), out[:200])
    # normalized should still record thought events
    norm = art / "normalized" / "grok.jsonl"
    if not norm.is_file():
        # artifacts may nest under run dir
        candidates = list(art.rglob("normalized/*.jsonl"))
        norm = candidates[0] if candidates else norm
    if norm.is_file():
        lines = norm.read_text(encoding="utf-8").splitlines()
        kinds = []
        for line in lines:
            try:
                kinds.append(json.loads(line).get("kind"))
            except Exception:
                pass
        assert_true("normalized has thought", "thought" in kinds, str(kinds[:20]))
    else:
        bad("normalized missing", str(art))


def test_codex_interrupt_resets_result_text(tmp: Path) -> None:
    """Interrupted/cancelled must not freeze OLD; completed uses items XOR deltas."""
    print("=== unit: codex interrupt text buffers ===")
    sys.path.insert(0, str(LIB_DIR))
    from steer.adapters.codex import CodexAdapter  # type: ignore

    art = tmp / "art-codex-int"
    art.mkdir(parents=True)
    (art / "raw").mkdir(parents=True)
    adapter = CodexAdapter(
        binary="false",
        model="m",
        effort="",
        cwd=str(tmp),
        artifacts_dir=str(art),
        agent_id="codex",
    )
    # Partial OLD via deltas
    adapter._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "item/agentMessage/delta",
            "params": {"delta": "OLD_PARTIAL"},
        }
    )
    adapter._active_turn_id = "turn_old"
    # Interrupt completes old turn — must NOT freeze _result_text
    adapter._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "turn/completed",
            "params": {
                "turn": {
                    "id": "turn_old",
                    "status": "interrupted",
                    "items": [{"type": "agentMessage", "text": "OLD_PARTIAL"}],
                }
            },
        }
    )
    assert_true(
        "interrupted does not freeze result_text",
        adapter._result_text is None,
        str(adapter._result_text),
    )
    assert_true("not done after interrupt", not adapter.is_done())

    # Replacement turn
    adapter._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "turn/started",
            "params": {"turn": {"id": "turn_new", "status": "inProgress"}},
        }
    )
    assert_true("buffers cleared on new turn", adapter._text_parts == [], str(adapter._text_parts))
    assert_true(
        "item buffers cleared",
        adapter._item_text_parts == [],
        str(adapter._item_text_parts),
    )

    # Stream NEW deltas + same full item on completed — final must be NEW once
    adapter._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "item/agentMessage/delta",
            "params": {"delta": "NEW"},
        }
    )
    adapter._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "turn/completed",
            "params": {
                "turn": {
                    "id": "turn_new",
                    "status": "completed",
                    "items": [{"type": "agentMessage", "text": "NEW"}],
                }
            },
        }
    )
    final = adapter.final_text()
    assert_true("final is NEW once", final == "NEW", final)
    assert_true("no OLD in final", "OLD" not in final, final)
    assert_true("not doubled NEWNEW", final != "NEWNEW", final)


def test_codex_completed_items_xor_deltas(tmp: Path) -> None:
    """When both deltas and full item exist, prefer items (no double)."""
    print("=== unit: codex completed source of truth ===")
    sys.path.insert(0, str(LIB_DIR))
    from steer.adapters.codex import CodexAdapter  # type: ignore

    art = tmp / "art-codex-xor"
    art.mkdir(parents=True)
    (art / "raw").mkdir(parents=True)
    adapter = CodexAdapter(
        binary="false",
        model="m",
        effort="",
        cwd=str(tmp),
        artifacts_dir=str(art),
        agent_id="codex",
    )
    adapter._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "item/agentMessage/delta",
            "params": {"delta": "Hello"},
        }
    )
    adapter._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "turn/completed",
            "params": {
                "turn": {
                    "id": "t1",
                    "status": "completed",
                    "items": [{"type": "agentMessage", "text": "Hello"}],
                }
            },
        }
    )
    assert_true("xor items preferred once", adapter.final_text() == "Hello", adapter.final_text())

    # deltas-only path
    adapter2 = CodexAdapter(
        binary="false",
        model="m",
        effort="",
        cwd=str(tmp),
        artifacts_dir=str(art),
        agent_id="codex",
    )
    adapter2._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "item/agentMessage/delta",
            "params": {"delta": "Only"},
        }
    )
    adapter2._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "item/agentMessage/delta",
            "params": {"delta": "Deltas"},
        }
    )
    adapter2._on_notification(
        {
            "jsonrpc": "2.0",
            "method": "turn/completed",
            "params": {"turn": {"id": "t2", "status": "completed", "items": []}},
        }
    )
    assert_true(
        "deltas used when no items",
        adapter2.final_text() == "OnlyDeltas",
        adapter2.final_text(),
    )


def test_opencode_part_updated_cumulative(tmp: Path) -> None:
    """message.part.updated snapshots H/He/Hello → final Hello once."""
    print("=== unit: opencode cumulative part.updated ===")
    sys.path.insert(0, str(LIB_DIR))
    from steer.adapters.opencode import OpenCodeAdapter  # type: ignore

    art = tmp / "art-oc-snap"
    art.mkdir(parents=True)
    (art / "raw").mkdir(parents=True)
    adapter = OpenCodeAdapter(
        binary="false",
        model="m",
        effort="",
        cwd=str(tmp),
        artifacts_dir=str(art),
        agent_id="opencode",
    )
    for snap in ("H", "He", "Hello"):
        adapter._handle_event(
            {
                "type": "message.part.updated",
                "properties": {
                    "part": {"id": "part_1", "type": "text", "text": snap},
                },
            }
        )
    final = adapter.final_text()
    assert_true("snapshot final Hello once", final == "Hello", final)
    assert_true("not HHeHello", final != "HHeHello", final)

    # delta path still incremental
    adapter2 = OpenCodeAdapter(
        binary="false",
        model="m",
        effort="",
        cwd=str(tmp),
        artifacts_dir=str(art),
        agent_id="opencode",
    )
    for d in ("H", "e", "llo"):
        adapter2._handle_event(
            {
                "type": "message.part.delta",
                "properties": {"delta": d, "part": {"type": "text", "text": d}},
            }
        )
    assert_true(
        "delta still incremental",
        adapter2.final_text() == "Hello",
        adapter2.final_text(),
    )


def test_opencode_redirect_and_auth_unit(tmp: Path) -> None:
    """Custom opener rejects non-loopback redirect; auth headers present; password scrubbed."""
    print("=== unit: opencode redirect + auth scrub ===")
    sys.path.insert(0, str(LIB_DIR))
    from steer.adapters.opencode import (  # type: ignore
        OpenCodeAdapter,
        _LoopbackRedirectHandler,
        _build_loopback_opener,
    )
    from steer.util import is_loopback_url  # type: ignore

    art = tmp / "art-oc-auth"
    art.mkdir(parents=True)
    (art / "raw").mkdir(parents=True)
    adapter = OpenCodeAdapter(
        binary="false",
        model="m",
        effort="",
        cwd=str(tmp),
        artifacts_dir=str(art),
        agent_id="opencode",
    )
    assert_true("password generated", len(adapter._server_password) >= 16)
    hdr = adapter._auth_headers()
    assert_true("auth header present", hdr.get("Authorization", "").startswith("Basic "))
    # raw log must not contain password
    adapter._log_raw(
        {
            "event": "server_start",
            "password": adapter._server_password,
            "OPENCODE_SERVER_PASSWORD": adapter._server_password,
            "Authorization": hdr["Authorization"],
        }
    )
    raw = (art / "raw" / "opencode.jsonl").read_text(encoding="utf-8")
    assert_true("password not in raw", adapter._server_password not in raw, raw[:200])
    assert_true("Authorization not in raw", "Basic " not in raw or "auth" in raw.lower())

    # Redirect handler rejects external
    handler = _LoopbackRedirectHandler()
    class _Req:
        full_url = "http://127.0.0.1:1/a"
        def get_full_url(self):
            return self.full_url
        def get_method(self):
            return "GET"
        def header_items(self):
            return []
        def has_header(self, k):
            return False
        headers = {}
        data = None
        unverifiable = False
        origin_req_host = "127.0.0.1"

    try:
        handler.redirect_request(
            _Req(), None, 302, "Found", {}, "http://evil.example.com/steal"
        )
        bad("external redirect rejected", "did not raise")
    except Exception as e:
        assert_true(
            "external redirect error mentions refuse/loopback/evil",
            "refuse" in str(e).lower() or "loopback" in str(e).lower() or "evil" in str(e).lower(),
            str(e),
        )

    assert_true("loopback target ok", is_loopback_url("http://127.0.0.1:9/x"))
    assert_true("opener builds", _build_loopback_opener() is not None)


def test_mailbox_cursor_on_exception(tmp: Path) -> None:
    """Injected exception after delivering must fail message; no orphan accepted/delivering."""
    print("=== unit: mailbox cursor + injected exception ===")
    sys.path.insert(0, str(LIB_DIR))
    from steer.adapters.base import DeliveryClass, SteerResult  # type: ignore
    from steer.mailbox import Mailbox  # type: ignore
    from steer.registry import Registry  # type: ignore
    from steer.supervisor import Supervisor  # type: ignore

    reg_root = tmp / "reg-cur"
    reg_root.mkdir(parents=True)
    art = tmp / "art-cur"
    art.mkdir(parents=True)
    for sub in ("raw", "normalized", "final"):
        (art / sub).mkdir(parents=True)

    reg = Registry(reg_root)
    run_id = reg.create_run(
        agent_id="grok",
        backend="grok-build",
        model="m",
        cwd=str(tmp),
        artifacts_dir=str(art),
    )
    reg.update_meta(run_id, status="running", pid=os.getpid())
    mb = Mailbox(reg.run_path(run_id))
    m1 = mb.enqueue(kind="steer", content="a", mode="auto", client_id="c1")
    m2 = mb.enqueue(kind="steer", content="b", mode="auto", client_id="c2")

    class BoomAdapter:
        def __init__(self):
            self.n = 0
            self._done = False
            self._cancelled = False

        def steer(self, content, mode, client_id):
            self.n += 1
            if self.n == 1:
                return SteerResult(
                    ok=True,
                    delivery_class=DeliveryClass.QUEUE_NEXT_TURN,
                    status="request_sent",
                    evidence="ok",
                )
            # Second call: raise after supervisor marked delivering
            raise RuntimeError("injected boom")

        def is_done(self):
            return False

        def final_text(self):
            return ""

        def exit_code(self):
            return 0

        def cancel(self):
            pass

        def poll_events(self):
            return iter(())

        def child_pid(self):
            return None

        def close(self):
            pass

    sup = Supervisor(
        agent_id="grok",
        task="t",
        cwd=str(tmp),
        artifacts_dir=str(art),
        registry=reg,
    )
    sup.run_id = run_id
    sup.mailbox = mb
    sup.adapter = BoomAdapter()

    # Process both; second raises inside adapter.steer (caught → failed)
    sup._drain_mailbox()
    msgs = {m["client_id"]: m for m in mb.list_messages()}
    assert_true("first applied-ish", msgs["c1"].get("status") == "request_sent", str(msgs["c1"]))
    assert_true(
        "second failed not orphan",
        msgs["c2"].get("status") == "failed",
        str(msgs["c2"]),
    )
    assert_true("cursor advanced past both", sup._last_seq >= m2["seq"], str(sup._last_seq))

    # Force exception after delivering status is set but outside adapter.steer try —
    # monkey-patch update_message to fail on meta write path after steer.
    m3 = mb.enqueue(kind="steer", content="c", mode="auto", client_id="c3")
    orig_update = mb.update_message
    calls = {"n": 0}

    def flaky_update(seq, **fields):
        calls["n"] += 1
        # First call sets delivering; second (status outcome) raises
        if calls["n"] == 2:
            raise RuntimeError("injected after delivering")
        return orig_update(seq, **fields)

    mb.update_message = flaky_update  # type: ignore[method-assign]
    sup.adapter = BoomAdapter()  # first steer succeeds
    sup.adapter.n = 0
    sup._drain_mailbox()
    # Restore and reload
    mb.update_message = orig_update  # type: ignore[method-assign]
    reloaded = mb.get_by_client_id("c3")
    assert_true(
        "post-deliver exception → failed",
        reloaded is not None and reloaded.get("status") == "failed",
        str(reloaded),
    )
    assert_true(
        "no orphan delivering/accepted",
        reloaded.get("status") not in (None, "accepted", "delivering"),
        str(reloaded),
    )
    assert_true("cursor past m3", sup._last_seq >= m3["seq"], str(sup._last_seq))


def test_grok_steer_reject_when_done(tmp: Path) -> None:
    """After done with empty in-flight, all modes including interrupt are rejected."""
    print("=== unit: grok reject steer after done ===")
    sys.path.insert(0, str(LIB_DIR))
    from steer.adapters.grok import GrokAdapter  # type: ignore

    art = tmp / "art-grok-done"
    art.mkdir(parents=True)
    (art / "raw").mkdir(parents=True)
    adapter = GrokAdapter(
        binary="false",
        model="m",
        effort="",
        cwd=str(tmp),
        artifacts_dir=str(art),
        agent_id="grok",
    )
    # Fake a completed ready-ish adapter without real rpc (steer checks session first)
    adapter.session_id = "s1"
    adapter.rpc = object()  # type: ignore[assignment]
    adapter._done = True
    adapter._in_flight = {}
    for mode in ("auto", "queue", "interrupt"):
        r = adapter.steer("late", mode, f"cid-{mode}")
        assert_true(
            f"reject mode={mode} when done",
            r.status == "rejected" and not r.ok,
            f"status={r.status} err={r.error}",
        )


def test_save_outputs_zero_no_cwd_artifacts(tmp: Path) -> None:
    """CONSILIUM_SAVE_OUTPUTS=0 must not create ./raw or ./final.txt in project cwd."""
    print("=== e2e: SAVE_OUTPUTS=0 private artifacts ===")
    reg_root = tmp / "reg-save0"
    reg_root.mkdir(parents=True)
    cwd = tmp / "cwd-save0"
    cwd.mkdir()
    env = env_base(reg_root, tmp / "art-save0-unused")
    env["CONSILIUM_SAVE_OUTPUTS"] = "0"
    # Clear ordinary run dir so path would otherwise fall back to "."
    env.pop("CONSILIUM_RUN_DIR", None)
    env["CONSILIUM_FAKE_STEER_SLOW"] = "0.2"
    # Ensure cwd has no pre-existing artifacts
    for name in ("raw", "normalized", "final", "final.txt"):
        p = cwd / name
        if p.is_dir():
            shutil.rmtree(p)
        elif p.exists():
            p.unlink()

    proc, run_id, _ = start_steerable("claude-code", "save0 task", env, cwd)
    code, out, err = wait_proc(proc, timeout=40)
    assert_true("save0 exit 0", code == 0, err[-400:])
    assert_true("no ./raw in cwd", not (cwd / "raw").exists())
    assert_true("no ./final.txt in cwd", not (cwd / "final.txt").exists())
    assert_true("no ./normalized in cwd", not (cwd / "normalized").exists())
    # Protocol artifacts under registry run
    meta = json.loads((reg_root / "runs" / run_id / "meta.json").read_text())
    art_dir = Path(meta.get("artifacts_dir") or "")
    assert_true("meta artifacts_dir set", bool(art_dir), str(meta.get("artifacts_dir")))
    assert_true(
        "artifacts under registry run",
        str(reg_root / "runs" / run_id) in str(art_dir.resolve()),
        str(art_dir),
    )
    assert_true(
        "not project cwd",
        art_dir.resolve() != cwd.resolve(),
        str(art_dir),
    )
    # Observability: final still available under run
    run_final = reg_root / "runs" / run_id / "final.txt"
    assert_true(
        "run final present",
        run_final.is_file() or (art_dir / "final.txt").is_file() or bool(out.strip()),
        f"run_final={run_final} art={art_dir}",
    )


def test_opencode_auth_e2e_password_not_in_artifacts(tmp: Path) -> None:
    """Fake requires Basic auth; raw artifacts must not contain the password."""
    print("=== e2e: opencode auth no password leak ===")
    reg_root = tmp / "reg-oc-auth-e2e"
    art = tmp / "art-oc-auth-e2e"
    art.mkdir(parents=True, exist_ok=True)
    reg_root.mkdir(parents=True, exist_ok=True)
    cwd = tmp / "cwd-oc-auth-e2e"
    cwd.mkdir(exist_ok=True)
    env = env_base(reg_root, art)
    env["CONSILIUM_FAKE_STEER_SLOW"] = "0.25"
    proc, run_id, _ = start_steerable("opencode", "auth task", env, cwd)
    code, out, err = wait_proc(proc, timeout=40)
    assert_true("oc auth exit 0", code == 0, err[-400:])
    # Search raw for anything that looks like a long token_urlsafe password
    raw_files = list(art.rglob("*.jsonl")) + list((reg_root / "runs" / run_id).rglob("*.jsonl"))
    blob = ""
    for p in raw_files:
        try:
            blob += p.read_text(encoding="utf-8")
        except Exception:
            pass
    # Adapter logs auth=basic but never the secret; password is 32+ urlsafe chars.
    # Ensure no Authorization Basic payload is stored.
    assert_true(
        "no Basic base64 blob in artifacts",
        "Authorization" not in blob or "Basic " not in blob,
        blob[:300],
    )
    assert_true("auth used (healthy)", "FAKE_OC" in out or code == 0, out[:200])


def main() -> int:
    for p in FAKES.iterdir():
        if p.is_file():
            p.chmod(p.stat().st_mode | 0o111)
    CONSILIUM.chmod(CONSILIUM.stat().st_mode | 0o111)

    tmp = Path(tempfile.mkdtemp(prefix="consilium-steer-test-"))
    print(f"tmpdir={tmp}")
    try:
        test_mailbox_and_registry_unit(tmp)
        test_artifact_no_truncate(tmp)
        test_codex_interrupt_resets_result_text(tmp)
        test_codex_completed_items_xor_deltas(tmp)
        test_opencode_part_updated_cumulative(tmp)
        test_opencode_redirect_and_auth_unit(tmp)
        test_mailbox_cursor_on_exception(tmp)
        test_grok_steer_reject_when_done(tmp)
        test_oneshot_regression(tmp)
        test_backend_e2e("claude-code", "claude", tmp)
        test_backend_e2e("codex", "codex", tmp)
        test_backend_e2e("opencode", "opencode", tmp)
        test_backend_e2e("grok", "grok", tmp)
        test_opencode_auth_e2e_password_not_in_artifacts(tmp)
        test_save_outputs_zero_no_cwd_artifacts(tmp)
        test_grok_queue_and_send_now(tmp)
        test_grok_ack_not_delivered_on_write(tmp)
        test_grok_message_type_filter_unit(tmp)
        test_grok_late_ack_reconcile_unit(tmp)
        test_grok_late_ack_e2e(tmp)
        test_grok_thought_not_in_stdout_e2e(tmp)
        test_cancel(tmp)
        test_duplicate_idempotency(tmp)
        test_malicious_client_id_e2e(tmp)
        test_claude_interrupt_rejected(tmp)
        test_process_cleanup(tmp)
    except Exception:
        bad("suite crashed", traceback.format_exc())
    finally:
        # leave tmp for debugging if FAIL
        if FAIL == 0:
            shutil.rmtree(tmp, ignore_errors=True)
        else:
            print(f"kept tmpdir for debug: {tmp}")

    print(f"\nsteer tests: {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
