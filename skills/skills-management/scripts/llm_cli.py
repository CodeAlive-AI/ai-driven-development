#!/usr/bin/env python3
"""Calls to an LLM through its command-line interface, shared by optimize_skill.py
and blind_comparator.py. The prompt goes to the CLI's stdin; stdout is the answer.
"""

from __future__ import annotations

import json
import re
import subprocess

from run_io import log

DEFAULT_TIMEOUT = 300


def safe_json_loads(text: str) -> dict | None:
    """Parse JSON; if that fails, try to extract the first {...} block."""
    text = text.strip()
    # Strip markdown fences if present.
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*\n", "", text)
        text = re.sub(r"\n```\s*$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Fallback: greedy first balanced-ish object.
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            return None
    return None


def run_cli(cmd: list[str], stdin: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Run a CLI command, pipe stdin, return stdout. Raises on non-zero exit."""
    try:
        result = subprocess.run(
            cmd,
            input=stdin,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError as exc:
        raise RuntimeError(
            f"CLI not found: {' '.join(cmd)} ({exc}). "
            f"Use --dry-run to plan without executing."
        ) from exc
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"CLI timed out after {timeout}s: {' '.join(cmd)}") from exc

    if result.returncode != 0:
        raise RuntimeError(
            f"CLI exited {result.returncode}: {' '.join(cmd)}\n"
            f"stderr: {result.stderr[:400]}"
        )
    return result.stdout


def call_llm_text(cmd_str: str, prompt: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Call an LLM CLI with a free-text prompt. Returns the model's stdout."""
    return run_cli(cmd_str.split(), stdin=prompt, timeout=timeout)


def call_llm_json(cmd_str: str, prompt: str, timeout: int = DEFAULT_TIMEOUT) -> dict | None:
    """Call an LLM CLI expecting a JSON response. Retries once on parse failure."""
    parsed = safe_json_loads(call_llm_text(cmd_str, prompt, timeout=timeout))
    if parsed is not None:
        return parsed
    log("  [warn] JSON parse failed, retrying with stricter prompt")
    retry_prompt = prompt + "\n\nRespond ONLY with valid JSON. Previous output was malformed."
    return safe_json_loads(call_llm_text(cmd_str, retry_prompt, timeout=timeout))


def run_rollout(target_cmd: str, skill_text: str, task: dict, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Run one task against the target agent with the skill prepended to the prompt.

    Prepending is the lowest common denominator: CLIs differ in how (and whether)
    they accept a separate system prompt.
    """
    composite = (
        "SKILL DOCUMENT (read this before answering):\n"
        "---\n"
        f"{skill_text}\n"
        "---\n\n"
        f"TASK:\n{task['prompt']}\n"
    )
    return call_llm_text(target_cmd, composite, timeout=timeout)
