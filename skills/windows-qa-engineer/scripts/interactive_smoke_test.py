#!/usr/bin/env python3
"""Exercise UFO discovery, window selection, and capture against Windows Notepad."""

from __future__ import annotations

import argparse
import asyncio
import base64
import json
import subprocess
import tempfile
from enum import Enum
from pathlib import Path
from typing import Any

from fastmcp import Client


def result_data(result: Any) -> Any:
    structured = getattr(result, "structured_content", None)
    if isinstance(structured, dict) and set(structured) == {"result"}:
        return structured["result"]
    if structured is not None:
        return structured
    return getattr(result, "data", None)


def to_plain(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, Enum):
        return to_plain(value.value)
    if isinstance(value, Path):
        return str(value)
    root = getattr(value, "root", None)
    if root is not None:
        return to_plain(root)
    if hasattr(value, "model_dump"):
        return to_plain(value.model_dump())
    if isinstance(value, dict):
        return {str(key): to_plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [to_plain(item) for item in value]
    if isinstance(value, type):
        return f"{value.__module__}.{value.__qualname__}"
    attributes = getattr(value, "__dict__", None)
    if isinstance(attributes, dict):
        public_attributes = {
            str(key): to_plain(item)
            for key, item in attributes.items()
            if not str(key).startswith("_")
        }
        if public_attributes:
            return public_attributes
    return str(value)


async def run(project_dir: Path, output_dir: Path) -> dict[str, Any]:
    config_path = project_dir / ".mcp.json"
    if not config_path.exists():
        raise FileNotFoundError(f"MCP configuration not found: {config_path}")

    output_dir.mkdir(parents=True, exist_ok=True)
    screenshot_path = output_dir / "notepad.png"
    report_path = output_dir / "report.json"
    notepad = subprocess.Popen(["notepad.exe"])
    report: dict[str, Any] = {"success": False}

    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
        async with Client(config, timeout=45) as client:
            await asyncio.sleep(2)
            tools = await client.list_tools()
            report["tool_count"] = len(tools)

            discovery = await client.call_tool("qa_refresh_and_list_windows", {})
            windows = to_plain(result_data(discovery) or [])
            report["windows"] = windows
            match = next(
                (
                    window
                    for window in windows
                    if "notepad" in json.dumps(window, ensure_ascii=False).lower()
                ),
                None,
            )
            if not isinstance(match, dict):
                raise RuntimeError("Notepad was not found in the interactive window list")

            window_id = str(match.get("id", ""))
            window_name = str(match.get("name", ""))
            if not window_id or not window_name:
                raise RuntimeError(f"Unsupported window record: {match!r}")

            await client.call_tool(
                "select_application_window", {"id": window_id, "name": window_name}
            )
            capture = await client.call_tool("capture_window_screenshot", {})
            encoded = to_plain(result_data(capture))
            if not isinstance(encoded, str):
                raise RuntimeError("UFO returned no screenshot string")
            if encoded.startswith("data:image/"):
                encoded = encoded.split(",", 1)[1]
            screenshot_path.write_bytes(base64.b64decode(encoded, validate=True))

            report.update(
                {
                    "success": True,
                    "window": {"id": window_id, "name": window_name},
                    "screenshot": str(screenshot_path),
                }
            )
            return report
    except Exception as exc:
        report["error"] = str(exc)
        raise
    finally:
        report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        notepad.terminate()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-dir", type=Path, default=Path.cwd())
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(tempfile.gettempdir()) / "windows-qa-engineer-smoke",
    )
    args = parser.parse_args()
    report = asyncio.run(run(args.project_dir.resolve(), args.output_dir.resolve()))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
