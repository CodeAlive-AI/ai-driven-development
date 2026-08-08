#!/usr/bin/env python3
"""Offline contract tests for the shared Consilium runtime."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

LIB = Path(__file__).resolve().parents[1] / "lib"
sys.path.insert(0, str(LIB))

PASS = 0
FAIL = 0


def ok(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if cond:
        print(f"  PASS  {name}")
        PASS += 1
    else:
        print(f"  FAIL  {name}" + (f" — {detail}" if detail else ""))
        FAIL += 1


def main() -> int:
    from events import (
        EventValidationError,
        assemble_final_text,
        filter_persistable,
        make_event,
        map_stream_type,
        validate_normalized_record,
        KNOWN_EVENT_TYPES,
    )
    from mode_policy import (
        UnknownModeError,
        access_policy_for,
        assert_no_yolo_leak,
        get_mode_capabilities,
        validate_matrix,
    )
    from prompt_pipeline import (
        build_prompt,
        assert_layer_order,
        assert_mode_isolation,
        assert_raw_purity,
        FRAMEWORK_POLICY_REVIEW,
        FRAMEWORK_RECAP_REVIEW,
        LAYER_ORDER,
    )
    from workflow_plans import get_plan, assign_agents_to_roles, max_parallel
    from debug_tape import DebugTape
    from backend_contract import backend_capabilities, resolve_binary, list_backend_capabilities
    from terminal_guard import is_terminal
    from normalize_stream import normalize_grok, normalize_opencode

    print("=== Event schema ===")
    ok("closed set non-empty", len(KNOWN_EVENT_TYPES) >= 15)
    ok("text→answer_delta", map_stream_type("text") == "answer_delta")
    ok("thought→thinking_delta", map_stream_type("thought") == "thinking_delta")
    ok("end→run_completed", map_stream_type("end") == "run_completed")
    ok("error→run_failed", map_stream_type("error") == "run_failed")
    ok("unknown stream unmapped", map_stream_type("totally_unknown_xyz") is None)
    e = make_event(stream_type="text", backend="grok-build", agent_id="g", data="hi", raw={"type": "text"})
    ok("make_event answer_delta", e is not None and e.type == "answer_delta")
    ok("raw payload retained", e.raw == {"type": "text"})
    try:
        validate_normalized_record({"type": "not_a_real_type", "data": "x"})
        ok("reject unknown type", False, "should have raised")
    except EventValidationError:
        ok("reject unknown type", True)

    valid, rejected = filter_persistable(
        [
            {"type": "answer_delta", "data": "a", "backend": "x", "agent_id": "y"},
            {"type": "bogus_type", "data": "nope"},
            {"type": "thinking_delta", "data": "t"},
        ]
    )
    ok("filter keeps known", len(valid) == 2)
    ok("filter rejects unknown", len(rejected) == 1)
    ok(
        "assemble prefers result",
        assemble_final_text(
            [
                make_event(stream_type="text", data="delta"),
                make_event(stream_type="result", data="FULL"),
            ]
        )
        == "FULL",
    )
    ok(
        "empty result does not erase deltas",
        assemble_final_text(
            [
                make_event(stream_type="text", data="kept"),
                make_event(stream_type="result", data="   "),
            ]
        )
        == "kept",
    )
    ok(
        "whitespace-only result does not erase deltas",
        assemble_final_text(
            [
                make_event(stream_type="text", data="A"),
                make_event(stream_type="text", data="B"),
                make_event(stream_type="result", data="\n\t"),
            ]
        )
        == "AB",
    )

    # Protocol-drift via normalize_stream CLI
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        raw = td / "raw.jsonl"
        # known + unknown stream types
        raw.write_text(
            '{"type":"thought","data":"t"}\n'
            '{"type":"text","data":"A"}\n'
            '{"type":"totally_unknown_stream","data":"leak"}\n'
            '{"type":"end","stopReason":"EndTurn"}\n',
            encoding="utf-8",
        )
        norm = td / "norm.jsonl"
        text = td / "final.txt"
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "grok-build",
                "--agent-id",
                "grok",
                "--input",
                str(raw),
                "--extract-text",
                "--text-out",
                str(text),
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
        )
        ok("normalize exit 0", proc.returncode == 0, proc.stderr[-200:])
        lines = [json.loads(l) for l in proc.stdout.splitlines() if l.strip()]
        types = [r["type"] for r in lines]
        ok("no unknown type in normalized stdout", "totally_unknown_stream" not in types, str(types))
        ok("has thinking_delta", "thinking_delta" in types)
        ok("has answer_delta", "answer_delta" in types)
        ok("has run_completed", "run_completed" in types)
        ok("has run_started", "run_started" in types)
        for r in lines:
            ok(f"type {r['type']} is known", r["type"] in KNOWN_EVENT_TYPES)
        ok("final text A", text.read_text() == "A")

    print("=== Backend contract ===")
    caps = list_backend_capabilities()
    ok("all five backends", set(caps) >= {"codex-cli", "claude-code", "opencode", "grok-build", "gemini-cli"})
    g = backend_capabilities("grok-build")
    ok("grok live_queue", g.live_queue is True)
    ok("grok steerable", g.steerable is True)
    cl = backend_capabilities("claude-code")
    ok("claude interrupt unsupported", cl.steer_interrupt == "")
    gem = backend_capabilities("gemini-cli")
    ok("gemini not steerable", gem.steerable is False and gem.supports_delegate is False)
    ok("gemini final rule plain", gem.final_text_rule == "plain_stdout")
    # Distinct oneshot vs steerable transports where they differ
    codex = backend_capabilities("codex-cli")
    ok("codex oneshot transport exec-json", codex.oneshot_transport == "exec-json")
    ok("codex steerable transport app-server", codex.steerable_transport == "app-server")
    ok("codex transports distinct", codex.oneshot_transport != codex.steerable_transport)
    ok(
        "grok oneshot streaming-json",
        g.oneshot_transport == "streaming-json",
    )
    ok("grok steerable acp-stdio", g.steerable_transport == "acp-stdio")
    ok("grok transports distinct", g.oneshot_transport != g.steerable_transport)
    oc = backend_capabilities("opencode")
    ok(
        "opencode notes mention part snapshots / step_inject",
        "step_inject" in oc.notes and "cumulative" in oc.notes.lower(),
    )
    ok(
        "opencode session.complete is terminal",
        is_terminal(b'{"type":"session.complete"}', "opencode"),
    )
    ok(
        "opencode session.idle is not process-terminal",
        not is_terminal(b'{"type":"session.idle"}', "opencode"),
    )
    ok(
        "opencode normalizer records idle as progress",
        normalize_opencode({"type": "session.idle"}) == ("progress", "session.idle"),
    )
    ok(
        "grok tool call exposes tool liveness",
        normalize_grok(
            {
                "type": "tool_call",
                "toolName": "run_terminal_command",
                "status": "pending",
            }
        )
        == ("tool_started", "run_terminal_command"),
    )
    ok(
        "grok tool update exposes content-free progress",
        normalize_grok({"type": "tool_call_update", "status": "in_progress"})
        == ("progress", "in_progress"),
    )
    ok(
        "grok completed tool update closes tool lifecycle",
        normalize_grok({"type": "tool_call_update", "status": "completed"})
        == ("tool_completed", "completed"),
    )
    if os.name == "posix":
        with tempfile.TemporaryDirectory() as td:
            child_pid_file = Path(td) / "child.pid"
            child_code = (
                "import json,os,signal,sys,time;"
                "open(sys.argv[1],'w').write(str(os.getpid()));"
                "signal.signal(signal.SIGTERM,signal.SIG_IGN);"
                "print(json.dumps({'type':'session.complete'}),flush=True);"
                "time.sleep(30)"
            )
            guard = subprocess.Popen(
                [
                    sys.executable,
                    str(LIB / "terminal_guard.py"),
                    "--backend",
                    "opencode",
                    "--terminal-grace",
                    "30",
                    "--",
                    sys.executable,
                    "-c",
                    child_code,
                    str(child_pid_file),
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            deadline = time.monotonic() + 3
            while not child_pid_file.is_file() and time.monotonic() < deadline:
                time.sleep(0.01)
            child_pid = int(child_pid_file.read_text()) if child_pid_file.is_file() else -1
            guard.terminate()
            try:
                guard.wait(timeout=4)
            except subprocess.TimeoutExpired:
                guard.kill()
                guard.wait()
            child_alive = child_pid > 0
            if child_alive:
                try:
                    os.kill(child_pid, 0)
                except ProcessLookupError:
                    child_alive = False
            ok(
                "terminal guard SIGTERM reaps resistant child",
                guard.returncode == 143 and not child_alive,
                f"guard_rc={guard.returncode} child_pid={child_pid} alive={child_alive}",
            )

    print("=== Workflow plans and concurrency ===")
    os.environ.pop("CONSILIUM_MAX_PARALLEL", None)
    ok("default unlimited concurrency", max_parallel() == 0)
    os.environ["CONSILIUM_MAX_PARALLEL"] = "2"
    # re-import value via function reads env live
    ok("override concurrency", max_parallel() == 2)
    os.environ["CONSILIUM_MAX_PARALLEL"] = "0"
    super_p = get_plan("super")
    ok("super has 9 discovery passes", len(super_p.all_passes()) == 9, str(len(super_p.all_passes())))
    ok("super stage order", [s.id for s in super_p.stages][:3] == [
        "discovery-small",
        "discovery-frontier",
        "dedup",
    ])
    basic = assign_agents_to_roles(get_plan("basic"), ["codex", "grok"])
    roles = [p.role for p in basic.all_passes()]
    ok("basic roles", roles == ["security", "correctness"])
    keys = [p.artifact_key() for p in basic.all_passes()]
    ok("basic keys agent.role form", all("." in k for k in keys), str(keys))
    ultra = get_plan("ultra")
    ok("ultra has probe stage", any(s.id == "probe" for s in ultra.stages))
    ultra_spec = next(s for s in ultra.stages if s.id == "specialists")
    ok(
        "ultra specialists are 3×5 matrix (15)",
        len(ultra_spec.passes) == 15,
        str(len(ultra_spec.passes)),
    )
    ok(
        "ultra total discovery passes 20 (4+15+1)",
        len(ultra.all_passes()) == 20,
        str(len(ultra.all_passes())),
    )
    ultra_keys = [p.artifact_key() for p in ultra.all_passes()]
    ok("ultra keys unique", len(ultra_keys) == len(set(ultra_keys)), str(ultra_keys[:5]))
    ok(
        "ultra stage order broad→specialists→probe",
        [s.id for s in ultra.stages][:3] == ["broad", "specialists", "probe"],
    )
    ask = get_plan("ask", agents=["codex", "grok"])
    ok("ask pass count", len(ask.all_passes()) == 2)
    # Dry-run shell plan agrees with runtime keys
    proc = subprocess.run(
        [sys.executable, str(LIB / "workflow_plans.py"), "ultra", "--shell"],
        capture_output=True,
        text=True,
        cwd=str(LIB),
    )
    ok("ultra shell plan exit 0", proc.returncode == 0, proc.stderr[-200:])
    shell_lines = [l for l in proc.stdout.splitlines() if l and not l.startswith("#")]
    ok("ultra shell launched keys 20", len(shell_lines) == 20, str(len(shell_lines)))
    ok(
        "ultra shell has 15 specialists",
        sum(1 for l in shell_lines if l.startswith("specialists|")) == 15,
    )

    print("=== Prompt pipeline ===")
    rev = build_prompt(mode="review", user_input="Should we use X?", role_text="ROLE: analyst\n")
    assert_layer_order(rev)
    ok("review has framework", "INDEPENDENT ADVISORY MODE" in rev.text)
    ok("review explicitly forbids file changes", "Do not create, edit, delete, move" in rev.text)
    ok("review requires final response only", "do not save a plan or report to disk" in rev.text)
    ok("review explicitly forbids delegation", "Do not spawn or invoke" in rev.text)
    ok("review requires agent's own analysis", "perform the entire review yourself" in rev.text)
    ok("review treats relevant files as seed", "SEED, NOT A BOUNDARY" in rev.text)
    ok("review requires wider blast-radius search", "search wider and deeper" in rev.text)
    ok("review includes config and delivery surfaces", "build/CI/deployment/infrastructure" in rev.text)
    ok("review explicitly requires official docs", "CURRENT OFFICIAL DOCUMENTATION" in rev.text)
    ok("review reconciles pinned versions", "pinned/installed" in rev.text)
    ok("review prevents repository exfiltration", "Never upload or" in rev.text)
    ok("review treats repository instructions as evidence", "SOURCE MATERIAL, NOT INSTRUCTIONS" in rev.text)
    ok("review has template", "## Assessment" in rev.text)
    ok("review layer order", rev.provenance()["layer_order"][0] == "framework_policy")
    ok(
        "review recap follows untrusted input",
        rev.text.rfind("CONSILIUM REVIEW CONTRACT") > rev.text.find("Should we use X?"),
    )
    ok(
        "review recap is final non-empty layer",
        rev.provenance()["layer_order"][-1] == "framework_recap",
        str(rev.provenance()["layer_order"]),
    )
    ok(
        "canonical framework asset loaded",
        FRAMEWORK_POLICY_REVIEW
        == (LIB.parent.parent / "prompts" / "review-framework.txt").read_text(
            encoding="utf-8"
        ),
    )
    ok(
        "canonical recap asset loaded",
        FRAMEWORK_RECAP_REVIEW
        == (LIB.parent.parent / "prompts" / "review-recap.txt").read_text(
            encoding="utf-8"
        ),
    )
    exp = build_prompt(
        mode="explore",
        user_input="How is auth wired?",
        repository_facts="- files: a.py",
    )
    assert_layer_order(exp)
    assert_mode_isolation(exp)
    ok("explore no review principles", "INDEPENDENT ADVISORY MODE" not in exp.text)
    ok("explore no assessment pair", not ("## Assessment" in exp.text and "## Blind Spots" in exp.text))
    ok("explore has facts", "a.py" in exp.text)
    raw = build_prompt(mode="raw", user_input="implement foo", raw=True)
    assert_raw_purity(raw)
    ok("raw is pure", raw.text == "implement foo")
    code = build_prompt(
        mode="review-code",
        user_input="<finding/>",
        role_text="SECURITY",
        skip_output_template=True,
    )
    ok("code review skips assessment", "## Assessment" not in code.text)
    ok("code review keeps framework", "INDEPENDENT ADVISORY MODE" in code.text)
    prompt_dir = LIB.parent.parent / "prompts"
    for template_name in (
        "specialist.txt",
        "probe-generic.txt",
        "broad-analyst.txt",
        "broad-lateral.txt",
    ):
        template = (prompt_dir / template_name).read_text(encoding="utf-8")
        ok(
            f"{template_name} receives relevant-file seed",
            "{{INITIAL_RELEVANT_FILES}}" in template,
        )
        ok(
            f"{template_name} expands blast radius",
            "likely-incomplete navigation seed" in template
            and "configuration" in template
            and "build/CI/deployment/infra" in template,
        )
        ok(
            f"{template_name} has no closed-file scope",
            "entire scope" not in template and "Do not read external files" not in template,
        )
    # User input remains untrusted; a compact trusted recap follows it.
    prov = rev.provenance()
    ok("user_input untrusted", "user_input" in prov["trusted_boundary"]["untrusted"])
    ok("framework trusted", "framework_policy" in prov["trusted_boundary"]["trusted"])
    ok("framework recap trusted", "framework_recap" in prov["trusted_boundary"]["trusted"])

    print("=== Mode capability policy ===")
    validate_matrix()
    ok("review readonly", access_policy_for("review") == "readonly")
    ok("explore readonly", access_policy_for("explore") == "readonly")
    ok("delegate yolo", access_policy_for("delegate") == "yolo")
    ok("review-ask aliases review", access_policy_for("review-ask") == "readonly")
    rcaps = get_mode_capabilities("review")
    ok("review has diagnostic shell", rcaps.shell is True and rcaps.filesystem == "read")
    ok("review web on", rcaps.web is True)
    ok("review no steer", rcaps.steer is False)
    ecaps = get_mode_capabilities("explore")
    ok("explore does not claim unavailable shell", ecaps.shell is False)
    dcaps = get_mode_capabilities("delegate")
    ok("delegate write+shell", dcaps.filesystem == "write" and dcaps.shell is True)
    scaps = get_mode_capabilities("delegate-steerable")
    ok("steerable has steer", scaps.steer is True and scaps.interrupt is True)
    try:
        access_policy_for("invented-mode-xyz")
        ok("unknown mode fails closed", False)
    except UnknownModeError:
        ok("unknown mode fails closed", True)
    assert_no_yolo_leak("review")
    assert_no_yolo_leak("explore")
    ok("no yolo leak on readonly", True)
    # New readonly mode cannot appear without matrix entry → no silent YOLO
    try:
        get_mode_capabilities("review-new-depth")
        # alias maps review-* to review — still readonly
        ok("review-new-depth stays readonly", access_policy_for("review-new-depth") == "readonly")
    except UnknownModeError:
        ok("review-new-depth fails closed (also fine)", True)

    print("=== Debug event tape ===")
    with tempfile.TemporaryDirectory() as td:
        path = str(Path(td) / "tape.jsonl")
        tape = DebugTape(path=path, max_records=100, max_bytes=1_000_000)
        tape.open()
        tape.record("RAW", {"line": 1}, content_preview="raw")
        tape.record("PARSED", {"ok": True})
        tape.record("NORMALIZED", {"type": "answer_delta"})
        tape.record("RENDERED", {"progress_type": "text"})
        tape.record("FINAL", {"event": "done"})
        st = tape.report_gaps()
        tape.close()
        ok("tape wrote records", st["records_written"] >= 5)
        ok("tape no overflow default", st["overflow"] is False)
        ok("tape file exists", Path(path).is_file())
        # overflow honesty
        path2 = str(Path(td) / "small.jsonl")
        t2 = DebugTape(path=path2, max_records=3, max_bytes=1_000_000)
        t2.open()  # writes open marker
        for i in range(10):
            t2.record("RAW", {"i": i})
        s2 = t2.report_gaps()
        t2.close()
        ok("overflow detected", s2["overflow"] is True and s2["dropped"] > 0, str(s2))

        # normalize with debug tape
        raw = Path(td) / "r.jsonl"
        raw.write_text('{"type":"text","data":"Z"}\n{"type":"end","stopReason":"x"}\n', encoding="utf-8")
        dpath = str(Path(td) / "norm-tape.jsonl")
        env = os.environ.copy()
        env["CONSILIUM_DEBUG_EVENTS"] = "1"
        env["CONSILIUM_DEBUG_EVENTS_PATH"] = dpath
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "grok-build",
                "--agent-id",
                "g",
                "--input",
                str(raw),
                "--debug-events",
                dpath,
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
            env=env,
        )
        ok("normalize+debug exit 0", proc.returncode == 0, proc.stderr[-200:])
        ok("debug tape created", Path(dpath).is_file())
        stages = set()
        for line in Path(dpath).read_text().splitlines():
            try:
                stages.add(json.loads(line).get("stage"))
            except Exception:
                pass
        ok("tape has RAW", "RAW" in stages)
        ok("tape has NORMALIZED", "NORMALIZED" in stages)
        # disabled by default: no tape path pollution when env unset
        env2 = {k: v for k, v in os.environ.items() if not k.startswith("CONSILIUM_DEBUG")}
        raw2 = Path(td) / "r2.jsonl"
        raw2.write_text('{"type":"text","data":"Z"}\n{"type":"end"}\n', encoding="utf-8")
        dpath2 = str(Path(td) / "should-not.jsonl")
        subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "plain",
                "--agent-id",
                "g",
                "--input",
                str(raw2),
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
            env=env2,
        )
        ok("default no tape file", not Path(dpath2).is_file())

    print("=== Production-shaped normalizers ===")
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        # Codex exec --json nested item.completed + tool item
        codex_raw = td / "codex.jsonl"
        codex_raw.write_text(
            "\n".join(
                [
                    json.dumps(
                        {
                            "type": "item.completed",
                            "item": {
                                "type": "agent_message",
                                "text": "CODEX_ANSWER",
                            },
                        }
                    ),
                    json.dumps(
                        {
                            "type": "item.completed",
                            "item": {
                                "type": "command_execution",
                                "command": "ls",
                            },
                        }
                    ),
                    json.dumps({"type": "turn.completed"}),
                ]
            )
            + "\n",
            encoding="utf-8",
        )
        text = td / "codex-final.txt"
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "codex-cli",
                "--agent-id",
                "codex",
                "--input",
                str(codex_raw),
                "--extract-text",
                "--text-out",
                str(text),
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
        )
        ok("codex nested normalize exit 0", proc.returncode == 0, proc.stderr[-200:])
        ok("codex nested answer", text.read_text() == "CODEX_ANSWER", text.read_text())
        types = [
            json.loads(l)["type"]
            for l in proc.stdout.splitlines()
            if l.strip()
        ]
        ok("codex has answer_delta", "answer_delta" in types, str(types))
        ok("codex tool_completed present", "tool_completed" in types, str(types))
        ok("codex run_completed", "run_completed" in types, str(types))

        # Claude empty result must keep deltas
        claude_raw = td / "claude-empty.jsonl"
        claude_raw.write_text(
            '{"type":"content_block_delta","delta":{"type":"text_delta","text":"KEEP"}}\n'
            '{"type":"result","result":"   "}\n',
            encoding="utf-8",
        )
        ctext = td / "claude-empty.txt"
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "claude-code",
                "--agent-id",
                "c",
                "--input",
                str(claude_raw),
                "--extract-text",
                "--text-out",
                str(ctext),
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
        )
        ok("claude empty-result keeps deltas", ctext.read_text() == "KEEP", ctext.read_text())

        # Claude is_error → run_failed
        cerr = td / "claude-err.jsonl"
        cerr.write_text(
            '{"type":"result","result":"x","is_error":true,"error":"boom"}\n',
            encoding="utf-8",
        )
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "claude-code",
                "--agent-id",
                "c",
                "--input",
                str(cerr),
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
        )
        ctypes = [json.loads(l)["type"] for l in proc.stdout.splitlines() if l.strip()]
        ok("claude is_error → run_failed", "run_failed" in ctypes, str(ctypes))

        # content_block_stop for non-tool is progress, not tool_completed
        cstop = td / "claude-stop.jsonl"
        cstop.write_text(
            '{"type":"content_block_start","index":0,"content_block":{"type":"text"}}\n'
            '{"type":"content_block_stop","index":0}\n',
            encoding="utf-8",
        )
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "claude-code",
                "--agent-id",
                "c",
                "--input",
                str(cstop),
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
        )
        stypes = [json.loads(l)["type"] for l in proc.stdout.splitlines() if l.strip()]
        ok(
            "text block_stop is progress not tool_completed",
            "tool_completed" not in stypes and "progress" in stypes,
            str(stypes),
        )

        # Grok end stopReason error/rate_limit/cancel/max_tokens → non-success
        for stop, label in (
            ("Error", "error"),
            ("rate_limit", "rate_limit"),
            ("cancelled", "cancelled"),
            ("MaxTokens", "max_tokens"),
        ):
            graw = td / f"grok-stop-{label}.jsonl"
            graw.write_text(
                '{"type":"text","data":"partial"}\n'
                f'{{"type":"end","stopReason":"{stop}"}}\n',
                encoding="utf-8",
            )
            proc = subprocess.run(
                [
                    sys.executable,
                    str(LIB / "normalize_stream.py"),
                    "--backend",
                    "grok-build",
                    "--agent-id",
                    "g",
                    "--input",
                    str(graw),
                ],
                capture_output=True,
                text=True,
                cwd=str(LIB),
            )
            ok(
                f"grok end stopReason {label} non-success",
                proc.returncode != 0,
                f"rc={proc.returncode} out={proc.stdout[-200:]} err={proc.stderr[-200:]}",
            )
            gtypes = [json.loads(l)["type"] for l in proc.stdout.splitlines() if l.strip()]
            ok(
                f"grok end stopReason {label} → run_failed",
                "run_failed" in gtypes,
                str(gtypes),
            )

        # EndTurn remains success when validation is on
        gok = td / "grok-endturn.jsonl"
        gok.write_text(
            '{"type":"text","data":"ok"}\n{"type":"end","stopReason":"EndTurn"}\n',
            encoding="utf-8",
        )
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "grok-build",
                "--agent-id",
                "g",
                "--input",
                str(gok),
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
        )
        ok("grok EndTurn still success", proc.returncode == 0, proc.stderr[-200:])

        # OpenCode production-shaped cumulative snapshots → Hello not HHeHello
        ocraw = td / "oc-hello.jsonl"
        ocraw.write_text(
            "\n".join(
                [
                    json.dumps(
                        {
                            "directory": "/tmp/proj",
                            "payload": {
                                "type": "message.part.updated",
                                "properties": {
                                    "part": {
                                        "id": "prt_1",
                                        "type": "text",
                                        "text": snap,
                                    }
                                },
                            },
                        }
                    )
                    for snap in ("H", "He", "Hello")
                ]
                + [json.dumps({"type": "session.idle"})]
            )
            + "\n",
            encoding="utf-8",
        )
        octext = td / "oc-hello.txt"
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "opencode",
                "--agent-id",
                "oc",
                "--input",
                str(ocraw),
                "--extract-text",
                "--text-out",
                str(octext),
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
        )
        got = octext.read_text() if octext.is_file() else ""
        ok("opencode H/He/Hello → Hello", got == "Hello", repr(got))
        ok("opencode not HHeHello", got != "HHeHello", repr(got))

        # Gemini backend identity + plain text
        graw = td / "gem.txt"
        graw.write_text("GEMINI_OK\n", encoding="utf-8")
        gtext = td / "gem-out.txt"
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "gemini-cli",
                "--agent-id",
                "gemini-cli",
                "--input",
                str(graw),
                "--extract-text",
                "--text-out",
                str(gtext),
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
        )
        ok("gemini-cli normalize exit 0", proc.returncode == 0, proc.stderr[-200:])
        ok("gemini plain text extracted", gtext.read_text().strip() == "GEMINI_OK")
        glines = [json.loads(l) for l in proc.stdout.splitlines() if l.strip()]
        ok(
            "gemini backend label in events",
            all(r.get("backend") == "gemini-cli" for r in glines if r.get("type") != "run_started")
            or any(r.get("backend") == "gemini-cli" for r in glines),
            str(glines[:2]),
        )

        # Protocol drift: visible signal, never persisted
        drift = td / "drift.jsonl"
        drift.write_text(
            '{"type":"text","data":"ok"}\n{"type":"weird_unknown_xyz","data":"nope"}\n{"type":"end"}\n',
            encoding="utf-8",
        )
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "grok-build",
                "--agent-id",
                "g",
                "--input",
                str(drift),
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
        )
        ok("drift process continues (artifact fail-closed)", proc.returncode == 0)
        ok(
            "drift types never in stdout",
            "weird_unknown_xyz" not in proc.stdout,
        )
        ok(
            "drift visible bounded signal",
            "protocol-drift" in proc.stderr and "rejected_unknown" in proc.stderr,
            proc.stderr[-300:],
        )

        # Bare --debug-events enables tape
        raw3 = td / "d3.jsonl"
        raw3.write_text('{"type":"text","data":"Z"}\n{"type":"end"}\n', encoding="utf-8")
        d3 = str(td / "bare-tape.jsonl")
        env3 = {k: v for k, v in os.environ.items() if not k.startswith("CONSILIUM_DEBUG")}
        proc = subprocess.run(
            [
                sys.executable,
                str(LIB / "normalize_stream.py"),
                "--backend",
                "plain",
                "--agent-id",
                "g",
                "--input",
                str(raw3),
                "--debug-events",
                d3,
                "--no-validate",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB),
            env=env3,
        )
        ok("bare --debug-events enables tape", Path(d3).is_file() and proc.returncode == 0)

    print("=== Mode capability argv alignment ===")
    # Review must deny memory/subagents on grok when matrix says false.
    with tempfile.TemporaryDirectory() as td2:
        td2 = Path(td2)
        dump_path = td2 / "grok-argv.json"
        env = os.environ.copy()
        env["CONSILIUM_CONFIG"] = str(LIB.parent / "tests" / "fixtures" / "test-config.json")
        env["CONSILIUM_BIN_GROK"] = str(LIB.parent / "tests" / "fakes" / "fake-grok")
        env["CONSILIUM_DUMP_ARGV"] = str(dump_path)
        env.pop("CONSILIUM_RAW_PROMPT", None)
        proc = subprocess.run(
            [
                "bash",
                str(LIB / "backend_run.sh"),
                "--mode",
                "review",
                "--agent-id",
                "grok",
                "--raw",
                "q",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB.parent),
            env=env,
        )
        ok("grok review dump exit 0", proc.returncode == 0, proc.stderr[-200:])
        if dump_path.is_file():
            argv = " ".join(json.load(open(dump_path))["argv"])
            ok("review grok has --no-subagents", "--no-subagents" in argv, argv)
            ok("review grok has --no-memory", "--no-memory" in argv, argv)
            ok("review grok sandbox read-only", "read-only" in argv, argv)
            ok("review grok avoids plan mode", "--no-plan" in argv, argv)
            ok("review grok keeps terminal", "run_terminal_cmd" in argv, argv)
        else:
            ok("review grok has --no-subagents", False, "no dump")
            ok("review grok has --no-memory", False, "no dump")
            ok("review grok sandbox read-only", False, "no dump")
            ok("review grok avoids plan mode", False, "no dump")
            ok("review grok keeps terminal", False, "no dump")

        dump_c = td2 / "claude-argv.json"
        env["CONSILIUM_DUMP_ARGV"] = str(dump_c)
        env["CONSILIUM_BIN_CLAUDE"] = str(LIB.parent / "tests" / "fakes" / "fake-claude")
        proc = subprocess.run(
            [
                "bash",
                str(LIB / "backend_run.sh"),
                "--mode",
                "review",
                "--agent-id",
                "claude-code",
                "--raw",
                "q",
            ],
            capture_output=True,
            text=True,
            cwd=str(LIB.parent),
            env=env,
        )
        if dump_c.is_file():
            argv = " ".join(json.load(open(dump_c))["argv"])
            ok(
                "claude review keeps Bash and denies edit tools",
                "Bash,WebSearch,WebFetch" in argv
                and "Edit,Write,NotebookEdit,Bash" not in argv,
                argv,
            )
            ok("claude review disables agent tools", "Agent,Task" in argv, argv)
            ok(
                "claude review avoids plan workflow",
                "--permission-mode dontAsk" in argv
                and "--permission-mode plan" not in argv,
                argv,
            )
            ok("claude review disables customizations", "--safe-mode" in argv, argv)
            ok(
                "claude review has no session persistence",
                "--no-session-persistence" in argv,
                argv,
            )
        else:
            ok("claude review keeps Bash and denies edit tools", False, "no dump")
            ok("claude review avoids plan workflow", False, "no dump")
            ok("claude review disables agent tools", False, "no dump")
            ok("claude review disables customizations", False, "no dump")
            ok("claude review has no session persistence", False, "no dump")

    print(f"\nruntime contract tests: {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
