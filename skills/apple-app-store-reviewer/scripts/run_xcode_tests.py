#!/usr/bin/env python3
"""Run configured Xcode tests and convert the result into review evidence."""

from __future__ import annotations

import argparse
import os
import platform
import re
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Mapping

from common import (
    ReviewInputError,
    dump_json,
    load_json,
    make_check,
    make_evidence,
    make_finding,
    now_iso,
    redact,
    resolve_config_paths,
)

FORBIDDEN_EXTRA_ARGS = {
    "-workspace", "-project", "-scheme", "-configuration", "-destination",
    "-resultBundlePath", "-testPlan", "test", "archive", "clean", "build",
}
SECRET_ASSIGNMENT = re.compile(r"(?i)(password|passwd|secret|token|api[_-]?key|authorization|credential)=")


def _validate_extra_args(items: list[str]) -> None:
    for item in items:
        if item in FORBIDDEN_EXTRA_ARGS:
            raise ReviewInputError(f"runtime.extra_xcodebuild_args may not override controlled argument {item}")
        if "\x00" in item or "\n" in item or "\r" in item:
            raise ReviewInputError("runtime.extra_xcodebuild_args may not contain control characters")
        if SECRET_ASSIGNMENT.search(item):
            raise ReviewInputError("Do not pass credentials through extra_xcodebuild_args; use a protected test environment")


def _runtime_command(config: Mapping[str, Any], output_dir: Path) -> tuple[list[str], Path]:
    runtime = config.get("runtime", {})
    if not isinstance(runtime, Mapping):
        raise ReviewInputError("runtime must be an object")
    workspace = runtime.get("workspace")
    project = runtime.get("project")
    if bool(workspace) == bool(project):
        raise ReviewInputError("Configure exactly one of runtime.workspace or runtime.project")
    scheme = str(runtime.get("scheme") or "").strip()
    if not scheme:
        raise ReviewInputError("runtime.scheme is required")
    destination = str(runtime.get("destination") or "platform=iOS Simulator,name=iPhone 17 Pro Max,OS=latest")
    configuration = str(runtime.get("configuration") or "Release")
    extra = [str(item) for item in runtime.get("extra_xcodebuild_args", [])]
    _validate_extra_args(extra)

    configured_result = runtime.get("result_bundle")
    result_bundle = Path(configured_result).resolve() if configured_result else (output_dir / "AppReviewTests.xcresult")
    command = ["xcodebuild", "test"]
    if workspace:
        command.extend(["-workspace", str(workspace)])
    else:
        command.extend(["-project", str(project)])
    command.extend([
        "-scheme", scheme,
        "-configuration", configuration,
        "-destination", destination,
        "-resultBundlePath", str(result_bundle),
    ])
    if runtime.get("test_plan"):
        command.extend(["-testPlan", str(runtime["test_plan"])])
    journey_tests = [str(item).strip() for item in runtime.get("reviewer_journey_tests", []) if str(item).strip()]
    for identifier in journey_tests:
        if not re.fullmatch(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+){1,2}", identifier):
            raise ReviewInputError(f"Invalid runtime.reviewer_journey_tests identifier: {identifier}")
        command.append(f"-only-testing:{identifier}")
    command.extend(extra)
    return command, result_bundle


def _run_to_log(command: list[str], log_path: Path, timeout: float) -> tuple[int, float, str]:
    started = time.monotonic()
    with log_path.open("w", encoding="utf-8", errors="replace") as log:
        try:
            process = subprocess.Popen(
                command,
                stdout=log,
                stderr=subprocess.STDOUT,
                text=True,
                start_new_session=True,
                env=os.environ.copy(),
            )
            try:
                returncode = process.wait(timeout=timeout)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(process.pid, signal.SIGTERM)
                except (ProcessLookupError, PermissionError):
                    process.terminate()
                try:
                    process.wait(timeout=10)
                except subprocess.TimeoutExpired:
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except (ProcessLookupError, PermissionError):
                        process.kill()
                    process.wait()
                log.write(f"\nTIMEOUT: xcodebuild exceeded {timeout} seconds.\n")
                returncode = 124
        except OSError as exc:
            log.write(f"Could not start xcodebuild: {type(exc).__name__}: {exc}\n")
            returncode = 127
    tail = ""
    try:
        with log_path.open("r", encoding="utf-8", errors="replace") as handle:
            text = handle.read()
            tail = text[-16000:]
    except OSError:
        pass
    return returncode, round(time.monotonic() - started, 3), str(redact(tail))


def _xcresult_summary(result_bundle: Path, output_dir: Path) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    if not result_bundle.exists() or not shutil.which("xcrun"):
        return None, {"status": "SKIPPED", "detail": "No result bundle or xcrun unavailable"}
    variants = [
        ["xcrun", "xcresulttool", "get", "test-results", "summary", "--path", str(result_bundle), "--compact"],
        ["xcrun", "xcresulttool", "get", "--format", "json", "--path", str(result_bundle)],
    ]
    for command in variants:
        try:
            completed = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=90, check=False)
        except (OSError, subprocess.TimeoutExpired) as exc:
            continue
        if completed.returncode == 0 and completed.stdout.strip():
            raw_path = output_dir / "xcresult-summary.json"
            raw_path.write_text(completed.stdout, encoding="utf-8")
            try:
                import json
                return json.loads(completed.stdout), {"status": "PASS", "detail": f"Parsed with {' '.join(command[1:5])}"}
            except json.JSONDecodeError:
                return None, {"status": "ERROR", "detail": "xcresulttool output was not JSON"}
    return None, {"status": "ERROR", "detail": "xcresulttool could not parse the result bundle"}


def run_xcode_tests(config: Mapping[str, Any], *, config_path: str | Path, output_dir: str | Path, timeout: float = 1800) -> dict[str, Any]:
    output_path = Path(output_dir).resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    result: dict[str, Any] = {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "tools": [],
        "checks": [],
        "findings": [],
        "facts": {},
    }
    if platform.system() != "Darwin" or not shutil.which("xcodebuild"):
        detail = "Xcode runtime tests require macOS with xcodebuild on PATH"
        result["tools"].append({"name": "xcodebuild", "status": "UNAVAILABLE", "detail": detail})
        result["checks"].append(make_check("runtime.xcode-tests", "Configured XCUITest/unit-test run", "SKIPPED", mandatory=True, tool="run_xcode_tests.py", detail=detail))
        result["checks"].append(make_check("runtime.reviewer-journey", "Clean-install reviewer journey and failure-state verification", "SKIPPED", mandatory=True, tool="run_xcode_tests.py", detail=detail))
        result["facts"]["status"] = "SKIPPED"
        dump_json(result, output_path / "runtime-results.json")
        return result

    command, result_bundle = _runtime_command(config, output_path)
    if result_bundle.exists():
        if result_bundle.is_dir():
            shutil.rmtree(result_bundle)
        else:
            result_bundle.unlink()
    log_path = output_path / "xcodebuild.log"
    dump_json({"command": redact(command), "timeout_seconds": timeout}, output_path / "xcodebuild-command.json")
    returncode, duration, tail = _run_to_log(command, log_path, timeout)
    summary, summary_tool = _xcresult_summary(result_bundle, output_path)

    result["tools"].extend([
        {"name": "xcodebuild", "status": "PASS" if returncode == 0 else "ERROR", "detail": f"Return code {returncode}; {duration}s"},
        {"name": "xcresulttool", **summary_tool},
    ])
    journey_tests = [str(item).strip() for item in config.get("runtime", {}).get("reviewer_journey_tests", []) if str(item).strip()]
    result["facts"].update({
        "status": "PASS" if returncode == 0 else "FAIL",
        "reviewer_journey_tests": journey_tests,
        "returncode": returncode,
        "duration_seconds": duration,
        "log": str(log_path),
        "result_bundle": str(result_bundle),
        "summary": redact(summary) if summary is not None else None,
    })
    if returncode == 0:
        result["checks"].append(make_check(
            "runtime.xcode-tests", "Configured XCUITest/unit-test run", "PASS", mandatory=True,
            tool="run_xcode_tests.py", detail=f"xcodebuild test completed successfully in {duration}s",
            evidence=[make_evidence(kind="test-log", location=str(log_path), detail="xcodebuild return code 0")],
        ))
        result["checks"].append(make_check(
            "runtime.reviewer-journey",
            "Clean-install reviewer journey and failure-state verification",
            "PASS" if journey_tests else "NEEDS_REVIEW",
            mandatory=True,
            tool="run_xcode_tests.py",
            detail=(f"Passed {len(journey_tests)} controlled reviewer-journey test identifier(s)." if journey_tests else "The configured test run passed, but runtime.reviewer_journey_tests was empty; generic tests do not prove the App Review path."),
            evidence=[make_evidence(kind="test-log", location=str(log_path), detail="Controlled xcodebuild test execution")],
        ))
    else:
        status = "ERROR" if returncode in {124, 127} else "OPEN"
        result["checks"].append(make_check(
            "runtime.xcode-tests", "Configured XCUITest/unit-test run", "ERROR" if status == "ERROR" else "NEEDS_REVIEW", mandatory=True,
            tool="run_xcode_tests.py", detail=f"xcodebuild returned {returncode}",
            evidence=[make_evidence(kind="test-log", location=str(log_path), detail="Tail is recorded in runtime-results.json")],
        ))
        result["checks"].append(make_check(
            "runtime.reviewer-journey", "Clean-install reviewer journey and failure-state verification",
            "ERROR" if status == "ERROR" else "NEEDS_REVIEW", mandatory=True, tool="run_xcode_tests.py",
            detail=f"Reviewer journey was not demonstrated because xcodebuild returned {returncode}",
            evidence=[make_evidence(kind="test-log", location=str(log_path), detail="Runtime journey did not pass")],
        ))
        result["findings"].append(make_finding(
            id="RUNTIME-XCODE-TESTS-FAILED",
            title="Configured release test run did not pass",
            severity="BLOCKER",
            status=status,
            category="runtime-completeness",
            guideline="2.1 App Completeness",
            confidence="CERTAIN",
            evidence=[make_evidence(kind="test-log", location=str(log_path), detail=f"xcodebuild return code {returncode}", value=tail)],
            rationale="A release candidate with a failing, timed-out, or unstartable reviewer-journey test is not demonstrated complete and functional.",
            remediation="Fix the failing build/test/environment path, rerun on the same clean simulator destination, and preserve the passing xcresult bundle.",
            verification=["run_xcode_tests.py exits 0", "The result bundle shows all configured release tests passed"],
            sources=["https://developer.apple.com/app-store/review/guidelines/#app-completeness"],
            automation="deterministic-runtime",
        ))
    dump_json(result, output_path / "runtime-results.json")
    return result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run configured Xcode release tests and emit structured App Review evidence.")
    parser.add_argument("--config", required=True, help="review-input.json")
    parser.add_argument("--output-dir", required=True, help="Directory for logs, xcresult, and runtime-results.json")
    parser.add_argument("--timeout", type=float, default=1800, help="Maximum xcodebuild duration in seconds (default: 1800)")
    parser.add_argument("--always-zero", action="store_true", help="Return 0 after producing evidence even when tests fail")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        raw = load_json(args.config)
        if not isinstance(raw, Mapping):
            raise ReviewInputError("Config root must be a JSON object")
        config = resolve_config_paths(raw, args.config)
        result = run_xcode_tests(config, config_path=args.config, output_dir=args.output_dir, timeout=args.timeout)
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"run_xcode_tests: {exc}\n")
        return 3
    if args.always_zero:
        return 0
    status = result.get("facts", {}).get("status")
    if status == "PASS":
        return 0
    if status == "SKIPPED":
        return 1
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
