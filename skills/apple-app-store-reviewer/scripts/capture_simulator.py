#!/usr/bin/env python3
"""Capture deterministic iOS Simulator screenshots from a safe JSON plan.

The plan supports only a small allow-listed action set. It never evaluates
shell text. Destructive simulator erase requires both a plan declaration and
``--allow-erase``.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Mapping

from common import ReviewInputError, dump_json, load_json, now_iso, redact

ALLOWED_ACTIONS = {"launch", "terminate", "open_url", "wait", "screenshot", "status_bar"}
SAFE_SCREEN_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,119}$")
MAX_STEPS = 100
MAX_WAIT_SECONDS = 30.0


def _run(command: list[str], *, timeout: float = 90.0, env: Mapping[str, str] | None = None) -> dict[str, Any]:
    started = time.monotonic()
    try:
        completed = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            check=False,
            env=dict(env) if env is not None else None,
        )
        return {
            "command": redact(command),
            "returncode": completed.returncode,
            "stdout": redact(completed.stdout[-12000:]),
            "stderr": redact(completed.stderr[-12000:]),
            "duration_seconds": round(time.monotonic() - started, 3),
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "command": redact(command),
            "returncode": 124,
            "stdout": redact((exc.stdout or "")[-12000:] if isinstance(exc.stdout, str) else ""),
            "stderr": f"Timed out after {timeout} seconds",
            "duration_seconds": round(time.monotonic() - started, 3),
        }
    except OSError as exc:
        return {
            "command": redact(command),
            "returncode": 127,
            "stdout": "",
            "stderr": f"{type(exc).__name__}: {exc}",
            "duration_seconds": round(time.monotonic() - started, 3),
        }


def _require_ok(result: Mapping[str, Any], context: str) -> None:
    if int(result.get("returncode", 1)) != 0:
        raise ReviewInputError(f"{context} failed: {result.get('stderr') or result.get('stdout') or 'unknown error'}")


def _validate_plan(plan: Mapping[str, Any]) -> None:
    steps = plan.get("steps")
    if not isinstance(steps, list) or not steps:
        raise ReviewInputError("Capture plan must contain a non-empty steps array")
    if len(steps) > MAX_STEPS:
        raise ReviewInputError(f"Capture plan exceeds {MAX_STEPS} steps")
    device = plan.get("device", {})
    if not isinstance(device, Mapping):
        raise ReviewInputError("device must be an object")
    if not device.get("udid") and not device.get("name"):
        raise ReviewInputError("device.udid or device.name is required")
    for index, step in enumerate(steps):
        if not isinstance(step, Mapping):
            raise ReviewInputError(f"steps[{index}] must be an object")
        action = str(step.get("action", ""))
        if action not in ALLOWED_ACTIONS:
            raise ReviewInputError(f"steps[{index}].action is not allowed: {action!r}")
        if action == "wait":
            try:
                seconds = float(step.get("seconds", 0))
            except (TypeError, ValueError) as exc:
                raise ReviewInputError(f"steps[{index}].seconds must be numeric") from exc
            if seconds < 0 or seconds > MAX_WAIT_SECONDS:
                raise ReviewInputError(f"steps[{index}].seconds must be between 0 and {MAX_WAIT_SECONDS}")
        if action == "screenshot":
            name = str(step.get("name", ""))
            if not SAFE_SCREEN_NAME.fullmatch(name):
                raise ReviewInputError(f"steps[{index}].name must match {SAFE_SCREEN_NAME.pattern}")
        if action == "open_url":
            url = str(step.get("url", ""))
            if not re.fullmatch(r"[A-Za-z][A-Za-z0-9+.-]*://[^\s]{1,2000}", url):
                raise ReviewInputError(f"steps[{index}].url is not a valid absolute app/deep-link URL")
        if action == "status_bar":
            operation = str(step.get("operation", "override"))
            if operation not in {"override", "clear"}:
                raise ReviewInputError(f"steps[{index}].operation must be override or clear")


def _devices() -> dict[str, Any]:
    result = _run(["xcrun", "simctl", "list", "devices", "available", "--json"], timeout=30)
    _require_ok(result, "Simulator device discovery")
    try:
        return json.loads(str(result.get("stdout", "{}")))
    except json.JSONDecodeError as exc:
        raise ReviewInputError(f"simctl returned invalid JSON: {exc}") from exc


def _select_device(plan: Mapping[str, Any]) -> dict[str, str]:
    selector = plan.get("device", {})
    target_udid = str(selector.get("udid") or "")
    target_name = str(selector.get("name") or "")
    runtime_contains = str(selector.get("runtime_contains") or "")
    candidates: list[dict[str, str]] = []
    for runtime, devices in _devices().get("devices", {}).items():
        if runtime_contains and runtime_contains.casefold() not in str(runtime).casefold():
            continue
        for device in devices or []:
            if not bool(device.get("isAvailable", True)):
                continue
            record = {
                "udid": str(device.get("udid", "")),
                "name": str(device.get("name", "")),
                "state": str(device.get("state", "")),
                "runtime": str(runtime),
            }
            if target_udid and record["udid"] == target_udid:
                return record
            if not target_udid and target_name and record["name"] == target_name:
                candidates.append(record)
    if target_udid:
        raise ReviewInputError(f"No available simulator matched UDID {target_udid}")
    if not candidates:
        raise ReviewInputError(f"No available simulator matched name {target_name!r} and runtime filter {runtime_contains!r}")
    candidates.sort(key=lambda item: item["runtime"], reverse=True)
    return candidates[0]


def _normalize_status_bar(udid: str) -> dict[str, Any]:
    command = [
        "xcrun", "simctl", "status_bar", udid, "override",
        "--time", "9:41", "--batteryState", "charged", "--batteryLevel", "100",
        "--wifiBars", "3", "--cellularBars", "4", "--operatorName", "",
    ]
    return _run(command, timeout=30)


def capture(
    *,
    app: str | Path,
    bundle_id: str,
    plan: Mapping[str, Any],
    output_dir: str | Path,
    normalize_status_bar: bool = False,
    allow_erase: bool = False,
) -> dict[str, Any]:
    _validate_plan(plan)
    app_path = Path(app).resolve()
    output_path = Path(output_dir).resolve()
    output_path.mkdir(parents=True, exist_ok=True)
    if platform.system() != "Darwin":
        raise ReviewInputError("Simulator capture requires macOS")
    if not shutil.which("xcrun"):
        raise ReviewInputError("xcrun was not found; install/select Xcode command-line tools")
    if not app_path.is_dir() or app_path.suffix != ".app":
        raise ReviewInputError(f"--app must be an existing simulator .app directory: {app_path}")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9.-]+", bundle_id):
        raise ReviewInputError("--bundle-id is malformed")

    selected = _select_device(plan)
    udid = selected["udid"]
    log: dict[str, Any] = {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "status": "RUNNING",
        "app": str(app_path),
        "bundle_id": bundle_id,
        "device": selected,
        "screenshots": [],
        "operations": [],
    }

    def op(command: list[str], context: str, *, timeout: float = 90, env: Mapping[str, str] | None = None) -> dict[str, Any]:
        result = _run(command, timeout=timeout, env=env)
        result["context"] = context
        log["operations"].append(result)
        _require_ok(result, context)
        return result

    try:
        if bool(plan.get("erase_before_capture")):
            if not allow_erase:
                raise ReviewInputError("Plan requests simulator erase; rerun with --allow-erase to acknowledge the destructive action")
            if selected.get("state") == "Booted":
                op(["xcrun", "simctl", "shutdown", udid], "Simulator shutdown before erase")
            op(["xcrun", "simctl", "erase", udid], "Simulator erase")

        boot = _run(["xcrun", "simctl", "boot", udid], timeout=60)
        boot["context"] = "Simulator boot"
        log["operations"].append(boot)
        if int(boot.get("returncode", 1)) != 0 and "current state: Booted" not in str(boot.get("stderr", "")):
            _require_ok(boot, "Simulator boot")
        op(["xcrun", "simctl", "bootstatus", udid, "-b"], "Simulator boot status", timeout=180)
        op(["xcrun", "simctl", "install", udid, str(app_path)], "Install app", timeout=180)

        if normalize_status_bar:
            result = _normalize_status_bar(udid)
            result["context"] = "Normalize status bar"
            log["operations"].append(result)
            _require_ok(result, "Normalize status bar")

        languages = plan.get("languages", [])
        if isinstance(languages, str):
            languages = [languages]
        locale = str(plan.get("locale") or "")
        launch_args = [str(item) for item in plan.get("launch_arguments", [])]
        plan_env = {str(k): str(v) for k, v in dict(plan.get("environment", {})).items()}
        if languages:
            launch_args.extend(["-AppleLanguages", "(" + ",".join(str(v) for v in languages) + ")"])
        if locale:
            launch_args.extend(["-AppleLocale", locale])

        for index, step in enumerate(plan["steps"]):
            action = str(step["action"])
            if action == "wait":
                seconds = float(step.get("seconds", 0))
                time.sleep(seconds)
                log["operations"].append({"context": f"Wait step {index}", "returncode": 0, "duration_seconds": seconds})
            elif action == "launch":
                command = ["xcrun", "simctl", "launch", udid, bundle_id, *launch_args]
                launch_env = os.environ.copy()
                for key, value in sorted(plan_env.items()):
                    if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]{0,127}", key):
                        raise ReviewInputError(f"Invalid simulator environment key: {key!r}")
                    launch_env[f"SIMCTL_CHILD_{key}"] = value
                op(command, str(step.get("name") or f"Launch step {index}"), timeout=90, env=launch_env)
            elif action == "terminate":
                result = _run(["xcrun", "simctl", "terminate", udid, bundle_id], timeout=30)
                result["context"] = f"Terminate step {index}"
                log["operations"].append(result)
                # Terminating an app that is not running is harmless for capture plans.
                if int(result.get("returncode", 1)) != 0 and "found nothing to terminate" not in str(result.get("stderr", "")).casefold():
                    _require_ok(result, f"Terminate step {index}")
            elif action == "open_url":
                op(["xcrun", "simctl", "openurl", udid, str(step["url"])], f"Open URL step {index}")
            elif action == "screenshot":
                filename = f"{step['name']}.png"
                target = output_path / filename
                op(["xcrun", "simctl", "io", udid, "screenshot", "--type=png", str(target)], f"Screenshot {filename}")
                if not target.is_file() or target.stat().st_size == 0:
                    raise ReviewInputError(f"simctl reported success but screenshot was not created: {target}")
                log["screenshots"].append({"step": index, "name": step["name"], "path": str(target), "bytes": target.stat().st_size})
            elif action == "status_bar":
                operation = str(step.get("operation", "override"))
                if operation == "clear":
                    op(["xcrun", "simctl", "status_bar", udid, "clear"], f"Clear status bar step {index}")
                else:
                    result = _normalize_status_bar(udid)
                    result["context"] = f"Override status bar step {index}"
                    log["operations"].append(result)
                    _require_ok(result, f"Override status bar step {index}")
        log["status"] = "PASS"
    except Exception as exc:
        log["status"] = "ERROR"
        log["error"] = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        dump_json(log, output_path / "capture-log.json")
    return log


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Capture iOS Simulator screenshots from an allow-listed, noninteractive JSON plan.")
    parser.add_argument("--app", required=True, help="Path to a simulator .app bundle.")
    parser.add_argument("--bundle-id", required=True, help="Application bundle identifier.")
    parser.add_argument("--plan", required=True, help="JSON capture plan.")
    parser.add_argument("--output-dir", required=True, help="Directory for PNG screenshots and capture-log.json.")
    parser.add_argument("--normalize-status-bar", action="store_true", help="Override status bar to a stable 9:41/100%% state.")
    parser.add_argument("--allow-erase", action="store_true", help="Permit erase only when the plan also requests erase_before_capture.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        plan = load_json(args.plan)
        if not isinstance(plan, Mapping):
            raise ReviewInputError("Capture plan root must be a JSON object")
        result = capture(
            app=args.app,
            bundle_id=args.bundle_id,
            plan=plan,
            output_dir=args.output_dir,
            normalize_status_bar=args.normalize_status_bar,
            allow_erase=args.allow_erase,
        )
        sys.stdout.write(dump_json(result))
        return 0
    except (ReviewInputError, OSError, ValueError) as exc:
        sys.stderr.write(f"capture_simulator: {exc}\n")
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
