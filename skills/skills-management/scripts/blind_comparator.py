#!/usr/bin/env python3
"""Blind A/B comparator for two skill versions.

Runs the same set of tasks against a target agent twice — once per skill — and
asks an independent judge to pick the better output without knowing which side
is which. The judge sees only the task prompt and two anonymised outputs; it
never sees the skill text itself, so it cannot be biased toward whichever
version "looks newer" or matches a known training signal.

This is intentionally separate from optimize_skill.py's internal validation
gate: the SkillOpt loop uses the same verifier that proposed the edits, which
can self-confirm. The comparator is the independent oracle.

Usage:
    python3 blind_comparator.py \\
        --skill-a path/to/skill_a/SKILL.md \\
        --skill-b path/to/skill_b/SKILL.md \\
        --tasks tasks.jsonl \\
        --target-cmd "claude -p --model claude-haiku-4-5-20251001" \\
        --judge-cmd  "claude -p --model claude-opus-4-7" \\
        --output-dir comparison-out/
"""

import argparse
import json
import os
import random
import re
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_SEED = 42
DEFAULT_TIMEOUT = 300


# --------------------------------------------------------------------------- #
# Helpers (mirroring optimize_skill.py conventions)                           #
# --------------------------------------------------------------------------- #

def log(msg: str) -> None:
    """Log to stderr so stdout stays clean for piping."""
    print(msg, file=sys.stderr, flush=True)


def safe_json_loads(text: str) -> dict | None:
    """Parse JSON; if that fails, try to extract the first {...} block."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*\n", "", text)
        text = re.sub(r"\n```\s*$", "", text)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group(0))
        except json.JSONDecodeError:
            return None
    return None


def load_jsonl(path: Path) -> list[dict]:
    items: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for i, raw in enumerate(fh, 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                items.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}: line {i}: invalid JSON: {exc}") from exc
    return items


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def read_skill_file(path: Path) -> str:
    """Read a SKILL.md file as plain text. Accepts either a SKILL.md path or a
    directory containing one (handled below by resolve_skill_path)."""
    return path.read_text(encoding="utf-8")


def resolve_skill_path(raw: str) -> Path:
    """Accept either a path to SKILL.md or to its parent directory."""
    p = Path(raw).expanduser().resolve()
    if p.is_dir():
        candidate = p / "SKILL.md"
        if candidate.exists():
            return candidate
        raise FileNotFoundError(f"No SKILL.md found in directory: {p}")
    if not p.exists():
        raise FileNotFoundError(f"Skill file not found: {p}")
    return p


# --------------------------------------------------------------------------- #
# CLI runner                                                                  #
# --------------------------------------------------------------------------- #

def _run_cli(cmd: list[str], stdin: str, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Run a CLI command, pipe stdin, return stdout. Raises on non-zero exit."""
    try:
        result = subprocess.run(
            cmd,
            input=stdin,
            capture_output=True,
            text=True,
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
    cmd = cmd_str.split()
    return _run_cli(cmd, stdin=prompt, timeout=timeout)


def call_llm_json(cmd_str: str, prompt: str, timeout: int = DEFAULT_TIMEOUT) -> dict | None:
    """Call an LLM CLI expecting a JSON response. Retries once on parse failure."""
    raw = call_llm_text(cmd_str, prompt, timeout=timeout)
    parsed = safe_json_loads(raw)
    if parsed is not None:
        return parsed
    log("  [warn] JSON parse failed, retrying with stricter prompt")
    retry_prompt = prompt + "\n\nRespond ONLY with valid JSON. Previous output was malformed."
    raw = call_llm_text(cmd_str, retry_prompt, timeout=timeout)
    return safe_json_loads(raw)


def cli_available(cmd_str: str) -> bool:
    """Return True if the first token of cmd_str is on PATH."""
    if not cmd_str.strip():
        return False
    head = cmd_str.split()[0]
    return shutil.which(head) is not None


# --------------------------------------------------------------------------- #
# Target rollout                                                              #
# --------------------------------------------------------------------------- #

def run_rollout(target_cmd: str, skill_text: str, task: dict, timeout: int = DEFAULT_TIMEOUT) -> str:
    """Run one task against the target agent with the skill text prepended.

    Mirrors optimize_skill.py's approach: prepend the skill document as part of
    the user prompt rather than relying on --append-system-prompt semantics
    that may vary across CLI surfaces.
    """
    composite = (
        "SKILL DOCUMENT (read this before answering):\n"
        "---\n"
        f"{skill_text}\n"
        "---\n\n"
        f"TASK:\n{task['prompt']}\n"
    )
    return call_llm_text(target_cmd, composite, timeout=timeout)


# --------------------------------------------------------------------------- #
# Judge                                                                       #
# --------------------------------------------------------------------------- #

def judge_pair(
    judge_cmd: str,
    judge_contract: str,
    task: dict,
    output_x: str,
    output_y: str,
    timeout: int = DEFAULT_TIMEOUT,
) -> dict:
    """Ask the blind judge to pick between Output X and Output Y."""
    prompt = (
        f"{judge_contract.rstrip()}\n\n"
        f"## TASK PROMPT\n{task['prompt']}\n\n"
        f"## OUTPUT X\n{output_x}\n\n"
        f"## OUTPUT Y\n{output_y}\n"
    )
    parsed = call_llm_json(judge_cmd, prompt, timeout=timeout) or {}
    # Normalise fields the aggregator depends on.
    parsed.setdefault("winner", "tie")
    parsed.setdefault("confidence", "low")
    parsed.setdefault("reasoning", "")
    for field in ("x_strengths", "x_weaknesses", "y_strengths", "y_weaknesses"):
        parsed.setdefault(field, [])
    return parsed


# --------------------------------------------------------------------------- #
# Per-task orchestration                                                      #
# --------------------------------------------------------------------------- #

def compare_one_task(
    task: dict,
    skill_a_text: str,
    skill_b_text: str,
    target_cmd: str,
    judge_cmd: str,
    judge_contract: str,
    task_dir: Path,
    randomise: bool,
    rng: random.Random,
    timeout: int,
) -> dict:
    """Compare both skills on one task. Writes per-task artifacts.

    Returns a result dict with both the raw verdict and the unblinded mapping.
    """
    task_dir.mkdir(parents=True, exist_ok=True)
    task_id = str(task["id"])

    # Step 1: rollout A.
    try:
        output_a = run_rollout(target_cmd, skill_a_text, task, timeout=timeout)
    except Exception as exc:  # noqa: BLE001
        log(f"  [error] target rollout (A) failed for task {task_id}: {exc}")
        return {
            "task_id": task_id,
            "prompt": task["prompt"],
            "winner": "error",
            "error": f"target_a: {exc}",
        }

    # Step 2: rollout B.
    try:
        output_b = run_rollout(target_cmd, skill_b_text, task, timeout=timeout)
    except Exception as exc:  # noqa: BLE001
        log(f"  [error] target rollout (B) failed for task {task_id}: {exc}")
        return {
            "task_id": task_id,
            "prompt": task["prompt"],
            "winner": "error",
            "error": f"target_b: {exc}",
        }

    # Step 3: randomise label assignment. Coin flip per task. The map records
    # which underlying skill ("a" or "b") was shown as label X vs Y so we can
    # unblind after the judge writes its verdict.
    if randomise and rng.random() < 0.5:
        x_label, y_label = "b", "a"
        output_x, output_y = output_b, output_a
    else:
        x_label, y_label = "a", "b"
        output_x, output_y = output_a, output_b

    (task_dir / "output_a.txt").write_text(output_a, encoding="utf-8")
    (task_dir / "output_b.txt").write_text(output_b, encoding="utf-8")
    (task_dir / "output_x.txt").write_text(output_x, encoding="utf-8")
    (task_dir / "output_y.txt").write_text(output_y, encoding="utf-8")
    write_json(task_dir / "label_map.json", {"x_label": x_label, "y_label": y_label})

    # Step 4: judge.
    try:
        verdict = judge_pair(
            judge_cmd, judge_contract, task, output_x, output_y, timeout=timeout,
        )
    except Exception as exc:  # noqa: BLE001
        log(f"  [error] judge failed for task {task_id}: {exc}")
        return {
            "task_id": task_id,
            "prompt": task["prompt"],
            "x_label": x_label,
            "y_label": y_label,
            "winner": "error",
            "error": f"judge: {exc}",
        }
    write_json(task_dir / "verdict.json", verdict)

    # Step 5: unblind.
    winner_raw = (verdict.get("winner") or "").strip().lower()
    if winner_raw == "x":
        winner_actual = x_label
    elif winner_raw == "y":
        winner_actual = y_label
    elif winner_raw == "tie":
        winner_actual = "tie"
    else:
        winner_actual = "tie"

    return {
        "task_id": task_id,
        "prompt": task["prompt"],
        "x_label": x_label,
        "y_label": y_label,
        "winner_raw": winner_raw,
        "winner": winner_actual,
        "confidence": (verdict.get("confidence") or "low").lower(),
        "reasoning": verdict.get("reasoning", ""),
        "verdict": verdict,
    }


# --------------------------------------------------------------------------- #
# Aggregation & reporting                                                     #
# --------------------------------------------------------------------------- #

def aggregate(results: list[dict]) -> dict:
    a_wins = sum(1 for r in results if r.get("winner") == "a")
    b_wins = sum(1 for r in results if r.get("winner") == "b")
    ties = sum(1 for r in results if r.get("winner") == "tie")
    errors = sum(1 for r in results if r.get("winner") == "error")

    confidence_breakdown: dict[str, dict[str, int]] = {
        "a": {"high": 0, "medium": 0, "low": 0},
        "b": {"high": 0, "medium": 0, "low": 0},
        "tie": {"high": 0, "medium": 0, "low": 0},
    }
    for r in results:
        winner = r.get("winner")
        conf = r.get("confidence", "low")
        if winner in confidence_breakdown and conf in confidence_breakdown[winner]:
            confidence_breakdown[winner][conf] += 1

    high_conf_a = confidence_breakdown["a"]["high"]
    high_conf_b = confidence_breakdown["b"]["high"]
    total = len(results)
    decided = total - errors
    return {
        "total_tasks": total,
        "decided": decided,
        "errors": errors,
        "a_wins": a_wins,
        "b_wins": b_wins,
        "ties": ties,
        "high_confidence_a": high_conf_a,
        "high_confidence_b": high_conf_b,
        "confidence_breakdown": confidence_breakdown,
    }


def render_markdown(
    skill_a_path: Path,
    skill_b_path: Path,
    target_cmd: str,
    judge_cmd: str,
    randomise: bool,
    seed: int,
    summary: dict,
    results: list[dict],
) -> str:
    lines = [
        "# Blind A/B Comparison Report",
        "",
        "## Setup",
        f"- Skill A: `{skill_a_path}`",
        f"- Skill B: `{skill_b_path}`",
        f"- Target CLI: `{target_cmd}`",
        f"- Judge CLI: `{judge_cmd}`",
        f"- Randomised labels: {randomise}",
        f"- Seed: {seed}",
        "",
        "## Summary",
        f"- Total tasks: {summary['total_tasks']}",
        f"- A wins: {summary['a_wins']}",
        f"- B wins: {summary['b_wins']}",
        f"- Ties: {summary['ties']}",
        f"- Errors: {summary['errors']}",
        f"- High-confidence A wins: {summary['high_confidence_a']}",
        f"- High-confidence B wins: {summary['high_confidence_b']}",
        "",
        "## Confidence Breakdown",
        "| Winner | High | Medium | Low |",
        "|--------|------|--------|-----|",
    ]
    for winner_key in ("a", "b", "tie"):
        cb = summary["confidence_breakdown"][winner_key]
        label = {"a": "A", "b": "B", "tie": "Tie"}[winner_key]
        lines.append(f"| {label} | {cb['high']} | {cb['medium']} | {cb['low']} |")
    lines += [
        "",
        "## Per-task Results",
        "| Task | Winner | Confidence | Showed as X | Showed as Y |",
        "|------|--------|------------|-------------|-------------|",
    ]
    for r in results:
        if r.get("winner") == "error":
            lines.append(
                f"| {r['task_id']} | error | - | - | - |"
            )
            continue
        lines.append(
            f"| {r['task_id']} | {r.get('winner', '?').upper()} | "
            f"{r.get('confidence', '?')} | "
            f"{r.get('x_label', '?').upper()} | "
            f"{r.get('y_label', '?').upper()} |"
        )
    lines += ["", "## Sample Reasoning"]
    for r in results[:10]:
        if r.get("winner") == "error":
            lines.append(f"\n### Task {r['task_id']}: ERROR")
            lines.append(f"- {r.get('error', '(no detail)')}")
            continue
        lines.append(f"\n### Task {r['task_id']} (winner: {r.get('winner', '?').upper()})")
        lines.append(f"- {r.get('reasoning', '(no reasoning)')}")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# Orchestration                                                               #
# --------------------------------------------------------------------------- #

def run_comparison(args: argparse.Namespace) -> int:
    # Resolve and validate skill files.
    try:
        skill_a_path = resolve_skill_path(args.skill_a)
        skill_b_path = resolve_skill_path(args.skill_b)
    except FileNotFoundError as exc:
        log(f"Error: {exc}")
        return 1

    tasks_path = Path(args.tasks).expanduser().resolve()
    if not tasks_path.exists():
        log(f"Error: tasks file not found: {tasks_path}")
        return 1

    tasks = load_jsonl(tasks_path)
    if not tasks:
        log("Error: no tasks loaded")
        return 1

    # Locate the contract prompt.
    skill_root = Path(__file__).resolve().parent.parent
    contract_path = skill_root / "prompts" / "blind_comparator.md"
    if not contract_path.exists():
        log(f"Error: judge contract not found: {contract_path}")
        return 1
    judge_contract = contract_path.read_text(encoding="utf-8")

    output_dir = Path(args.output_dir).expanduser().resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    rng = random.Random(args.seed)

    if args.dry_run:
        log("--- DRY RUN ---")
        log(f"Skill A: {skill_a_path}")
        log(f"Skill B: {skill_b_path}")
        log(f"Target CLI: {args.target_cmd}")
        log(f"Judge CLI: {args.judge_cmd}")
        log(f"Randomise labels: {args.randomise_labels}")
        log(f"Seed: {args.seed}")
        log(f"Output dir: {output_dir}")
        log(f"Task count: {len(tasks)}")
        log("Tasks that would run:")
        for t in tasks:
            log(f"  - {t.get('id')}: {str(t.get('prompt', ''))[:80]}")
        log(f"Judge contract preview: {judge_contract[:200].replace(chr(10), ' ')}")
        log("--- end dry run ---")
        return 0

    # Both CLIs must be available outside dry-run mode.
    if not cli_available(args.target_cmd):
        log(f"Error: target CLI not on PATH: {args.target_cmd.split()[0]!r}")
        log("Use --dry-run to plan without executing.")
        return 1
    if not cli_available(args.judge_cmd):
        log(f"Error: judge CLI not on PATH: {args.judge_cmd.split()[0]!r}")
        log("Use --dry-run to plan without executing.")
        return 1

    skill_a_text = read_skill_file(skill_a_path)
    skill_b_text = read_skill_file(skill_b_path)

    log(f"Skill A: {skill_a_path}")
    log(f"Skill B: {skill_b_path}")
    log(f"Tasks: {len(tasks)}  output_dir={output_dir}")

    # Snapshot the skill files for posterity.
    snapshots = output_dir / "skill_snapshots"
    snapshots.mkdir(parents=True, exist_ok=True)
    (snapshots / "skill_a.md").write_text(skill_a_text, encoding="utf-8")
    (snapshots / "skill_b.md").write_text(skill_b_text, encoding="utf-8")

    results: list[dict] = []
    for i, task in enumerate(tasks, 1):
        task_id = str(task["id"])
        log(f"\n[{i}/{len(tasks)}] Task {task_id}")
        task_dir = output_dir / f"task-{task_id}"
        result = compare_one_task(
            task=task,
            skill_a_text=skill_a_text,
            skill_b_text=skill_b_text,
            target_cmd=args.target_cmd,
            judge_cmd=args.judge_cmd,
            judge_contract=judge_contract,
            task_dir=task_dir,
            randomise=args.randomise_labels,
            rng=rng,
            timeout=args.timeout,
        )
        results.append(result)
        if result.get("winner") == "error":
            log(f"  result: ERROR ({result.get('error')})")
        else:
            log(
                f"  result: winner={result.get('winner', '?').upper()} "
                f"confidence={result.get('confidence', '?')}"
            )

    summary = aggregate(results)

    report = {
        "skill_a": str(skill_a_path),
        "skill_b": str(skill_b_path),
        "target_cmd": args.target_cmd,
        "judge_cmd": args.judge_cmd,
        "randomise_labels": args.randomise_labels,
        "seed": args.seed,
        "summary": summary,
        "results": results,
    }
    write_json(output_dir / "comparison_report.json", report)

    md = render_markdown(
        skill_a_path,
        skill_b_path,
        args.target_cmd,
        args.judge_cmd,
        args.randomise_labels,
        args.seed,
        summary,
        results,
    )
    (output_dir / "comparison_report.md").write_text(md, encoding="utf-8")

    # Final verdict line on stdout (so callers can grep it).
    total = summary["total_tasks"]
    a_wins = summary["a_wins"]
    b_wins = summary["b_wins"]
    ties = summary["ties"]
    high_a = summary["high_confidence_a"]
    high_b = summary["high_confidence_b"]
    if a_wins > b_wins:
        leader, leader_wins, leader_high = "A", a_wins, high_a
    elif b_wins > a_wins:
        leader, leader_wins, leader_high = "B", b_wins, high_b
    else:
        print(f"Result: tie {a_wins}/{total} each (ties={ties})")
        return 0
    pct = (leader_high * 100 // total) if total else 0
    print(
        f"Result: {leader} wins {leader_wins}/{total} "
        f"({pct}% high-confidence; ties={ties})"
    )
    return 0


# --------------------------------------------------------------------------- #
# Argparse                                                                    #
# --------------------------------------------------------------------------- #

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Blind A/B comparator for two skill versions",
    )
    p.add_argument("--skill-a", required=True,
                   help="Path to skill A's SKILL.md (or its parent directory)")
    p.add_argument("--skill-b", required=True,
                   help="Path to skill B's SKILL.md (or its parent directory)")
    p.add_argument("--tasks", required=True, help="Path to tasks.jsonl")
    p.add_argument("--target-cmd", default="claude -p --model claude-haiku-4-5-20251001",
                   help="CLI command for the target agent (the one under test)")
    p.add_argument("--judge-cmd", default="claude -p --model claude-opus-4-7",
                   help="CLI command for the blind judge")
    p.add_argument("--output-dir", default="./comparison-runs/run-001",
                   help="Directory for per-task artifacts and the final report")
    p.add_argument("--randomise-labels", dest="randomise_labels",
                   action="store_true", default=True,
                   help="Randomise which output is shown as X vs Y (default: on)")
    p.add_argument("--no-randomise-labels", dest="randomise_labels",
                   action="store_false",
                   help="Disable randomisation; A is always X, B is always Y")
    p.add_argument("--seed", type=int, default=DEFAULT_SEED)
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT,
                   help="Per-CLI-call timeout in seconds")
    p.add_argument("--dry-run", action="store_true",
                   help="Plan and print configuration without running any LLM calls")
    return p


def main() -> int:
    args = build_parser().parse_args()
    try:
        return run_comparison(args)
    except KeyboardInterrupt:
        log("Interrupted")
        return 130
    except Exception as exc:  # noqa: BLE001
        log(f"Fatal: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
