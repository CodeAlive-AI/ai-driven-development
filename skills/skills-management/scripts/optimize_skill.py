#!/usr/bin/env python3
"""SkillOpt-style optimisation loop for a Claude Code skill.

Treats the SKILL.md document as the trainable state of a frozen agent and
drives a forward (rollout) + backward (reflection) loop. All LLM calls are
shelled out to `claude -p` so the script inherits whatever subscription/API
the caller has configured.

See prompts/ for the per-stage contract texts. See the README/SKILL.md of
skills-management for the overall protocol.
"""

import argparse
import hashlib
import json
import math
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


# Protected slow-update markers — step-level edits must never touch this region.
SLOW_UPDATE_START = "<!-- SLOW_UPDATE_START -->"
SLOW_UPDATE_END = "<!-- SLOW_UPDATE_END -->"

DEFAULT_SEED = 42
DEFAULT_TIMEOUT = 300
LR_FLOOR = 2


# --------------------------------------------------------------------------- #
# Skill discovery (mirrors show_skill.py / review_skill.py)                    #
# --------------------------------------------------------------------------- #

def get_user_skills_dir() -> Path:
    return Path.home() / ".claude" / "skills"


def get_project_skills_dir() -> Path:
    return Path.cwd() / ".claude" / "skills"


def find_skill(name: str, scope: str | None = None) -> tuple[Path | None, str | None]:
    """Find a skill by name, optionally filtering by scope."""
    scopes_to_check: list[tuple[str, Path]] = []
    if scope is None or scope == "user":
        scopes_to_check.append(("user", get_user_skills_dir()))
    if scope is None or scope == "project":
        scopes_to_check.append(("project", get_project_skills_dir()))

    for scope_name, skills_dir in scopes_to_check:
        skill_path = skills_dir / name
        if skill_path.exists() and (skill_path / "SKILL.md").exists():
            return skill_path, scope_name
    return None, None


# --------------------------------------------------------------------------- #
# Helpers                                                                     #
# --------------------------------------------------------------------------- #

def approx_tokens(text: str) -> int:
    """Approximate token count (English-ish, ~4 chars/token)."""
    return len(text) // 4


def log(msg: str) -> None:
    """Log to stderr so stdout stays clean for piping."""
    print(msg, file=sys.stderr, flush=True)


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


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- #
# Task splits                                                                 #
# --------------------------------------------------------------------------- #

def hash_split(
    tasks: list[dict],
    train_frac: float,
    sel_frac: float,
    test_frac: float,
    seed: int = DEFAULT_SEED,
) -> dict:
    """Deterministically split tasks into train/sel/test by stable shuffle."""
    total = train_frac + sel_frac + test_frac
    if abs(total - 1.0) > 1e-6:
        raise ValueError(f"Splits must sum to 1.0 (got {total})")
    if not tasks:
        raise ValueError("Empty task list")

    ids = [str(t["id"]) for t in tasks]
    # Stable order by id-hash + seed so the split is reproducible.
    def sort_key(tid: str) -> str:
        return hashlib.sha256(f"{seed}:{tid}".encode("utf-8")).hexdigest()

    ordered = sorted(ids, key=sort_key)
    n = len(ordered)
    n_train = max(1, int(round(n * train_frac)))
    n_sel = max(1, int(round(n * sel_frac)))
    # Test gets whatever's left so totals always reconcile.
    n_train = min(n_train, n - 2)
    n_sel = min(n_sel, n - n_train - 1)

    train_ids = ordered[:n_train]
    sel_ids = ordered[n_train:n_train + n_sel]
    test_ids = ordered[n_train + n_sel:]

    return {
        "seed": seed,
        "train": train_ids,
        "selection": sel_ids,
        "test": test_ids,
    }


# --------------------------------------------------------------------------- #
# Skill document I/O & edit application                                       #
# --------------------------------------------------------------------------- #

def read_skill_body(skill_path: Path) -> str:
    return (skill_path / "SKILL.md").read_text(encoding="utf-8")


def split_protected(content: str) -> tuple[str, str | None, str]:
    """Split content into (before, protected_block_with_markers, after).

    Returns (content, None, "") if no protected block exists.
    """
    start = content.find(SLOW_UPDATE_START)
    end = content.find(SLOW_UPDATE_END)
    if start == -1 or end == -1 or end < start:
        return content, None, ""
    end_with_marker = end + len(SLOW_UPDATE_END)
    return content[:start], content[start:end_with_marker], content[end_with_marker:]


def touches_protected(content: str, target: str | None) -> bool:
    """Return True if `target` overlaps the protected slow-update region."""
    if not target:
        return False
    before, protected, _ = split_protected(content)
    if protected is None:
        return False
    return target in protected


def apply_edit(content: str, edit: dict) -> tuple[str, str | None]:
    """Apply a single edit. Returns (new_content, error_message_or_None)."""
    op = edit.get("op")
    target = edit.get("target")
    new_text = edit.get("content", "")

    if touches_protected(content, target):
        return content, "edit targets protected slow-update section"

    if op == "append":
        # Append after the protected region if it exists so step-level edits
        # never end up inside or after the closing marker reorders text.
        before, protected, after = split_protected(content)
        if protected is None:
            return content.rstrip("\n") + "\n\n" + new_text + "\n", None
        return before + protected + after.rstrip("\n") + "\n\n" + new_text + "\n", None

    if op == "insert_after":
        if not target or target not in content:
            return content, f"insert_after target not found: {target!r}"
        idx = content.find(target) + len(target)
        return content[:idx] + "\n" + new_text + content[idx:], None

    if op == "replace":
        if not target or target not in content:
            return content, f"replace target not found: {target!r}"
        return content.replace(target, new_text, 1), None

    if op == "delete":
        if not target or target not in content:
            return content, f"delete target not found: {target!r}"
        return content.replace(target, "", 1), None

    return content, f"unknown op: {op!r}"


def apply_edits(content: str, edits: list[dict]) -> tuple[str, list[dict]]:
    """Apply a sequence of edits. Returns (new_content, application_report)."""
    report: list[dict] = []
    current = content
    for i, edit in enumerate(edits):
        new_content, err = apply_edit(current, edit)
        report.append({
            "index": i,
            "op": edit.get("op"),
            "target_preview": (edit.get("target") or "")[:80],
            "applied": err is None,
            "error": err,
        })
        if err is None:
            current = new_content
        else:
            log(f"  [skip] edit #{i} ({edit.get('op')}): {err}")
    return current, report


def overwrite_protected(content: str, slow_update_text: str) -> str:
    """Insert/replace the protected slow-update block."""
    block = f"{SLOW_UPDATE_START}\n{slow_update_text.strip()}\n{SLOW_UPDATE_END}"
    before, protected, after = split_protected(content)
    if protected is None:
        # Append a new block right before any trailing whitespace.
        return content.rstrip("\n") + "\n\n" + block + "\n"
    return before + block + after


# --------------------------------------------------------------------------- #
# LR schedules                                                                #
# --------------------------------------------------------------------------- #

def lr_for_epoch(budget: int, schedule: str, epoch: int, total_epochs: int) -> int:
    """Return the textual edit budget L_t for `epoch` (1-indexed)."""
    if schedule == "constant" or total_epochs <= 1:
        return budget
    if schedule == "linear":
        # Linear decay from budget at epoch 1 to LR_FLOOR at the last epoch.
        if total_epochs == 1:
            return budget
        slope = (LR_FLOOR - budget) / (total_epochs - 1)
        return max(LR_FLOOR, int(round(budget + slope * (epoch - 1))))
    if schedule == "cosine":
        # Standard half-cosine warm-decay between budget (epoch 1) and LR_FLOOR.
        # The formula in the task spec: floor + (budget - floor) * 0.5 * (1 + cos(pi * e / E)).
        return max(LR_FLOOR, int(round(LR_FLOOR + (budget - LR_FLOOR) * 0.5 * (1.0 + math.cos(math.pi * epoch / total_epochs)))))
    raise ValueError(f"Unknown LR schedule: {schedule}")


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


def call_llm_text(
    cmd_str: str,
    prompt: str,
    timeout: int = DEFAULT_TIMEOUT,
) -> str:
    """Call an LLM CLI with a free-text prompt. Returns the model's stdout."""
    cmd = cmd_str.split()
    return _run_cli(cmd, stdin=prompt, timeout=timeout)


def call_llm_json(
    cmd_str: str,
    prompt: str,
    timeout: int = DEFAULT_TIMEOUT,
) -> dict | None:
    """Call an LLM CLI expecting a JSON response. Retries once on parse failure."""
    raw = call_llm_text(cmd_str, prompt, timeout=timeout)
    parsed = safe_json_loads(raw)
    if parsed is not None:
        return parsed
    log("  [warn] JSON parse failed, retrying with stricter prompt")
    retry_prompt = prompt + "\n\nRespond ONLY with valid JSON. Previous output was malformed."
    raw = call_llm_text(cmd_str, retry_prompt, timeout=timeout)
    return safe_json_loads(raw)


# --------------------------------------------------------------------------- #
# Rollout & verification                                                      #
# --------------------------------------------------------------------------- #

def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").strip().lower())


def verify_exact_match(rollout_output: str, reference: str) -> int:
    return 1 if _normalize(rollout_output) == _normalize(reference) else 0


def verify_llm_judge(
    optimizer_cmd: str,
    rollout_output: str,
    reference: str,
    prompt: str,
) -> int:
    judge_prompt = (
        "You are a strict pass/fail judge for AI agent outputs. "
        "Compare the agent's output to the reference answer for the given prompt. "
        "Respond ONLY with a valid JSON object like {\"score\": 0} or {\"score\": 1}.\n\n"
        f"PROMPT:\n{prompt}\n\n"
        f"REFERENCE:\n{reference}\n\n"
        f"AGENT OUTPUT:\n{rollout_output}\n"
    )
    try:
        parsed = call_llm_json(optimizer_cmd, judge_prompt) or {}
        score = parsed.get("score", 0)
        return 1 if int(score) >= 1 else 0
    except Exception as exc:  # noqa: BLE001
        log(f"  [warn] judge failed: {exc}; scoring 0")
        return 0


def verify_script(script_path: Path, rollout_output: str, reference: str, prompt: str) -> int:
    """Shell out to a user-provided verifier script.

    Contract: stdin is a JSON object {prompt, reference, output}; stdout is
    a JSON object {score: 0|1}.
    """
    payload = json.dumps({"prompt": prompt, "reference": reference, "output": rollout_output})
    raw = _run_cli([str(script_path)], stdin=payload)
    parsed = safe_json_loads(raw) or {}
    return 1 if int(parsed.get("score", 0)) >= 1 else 0


def run_rollout(
    target_cmd: str,
    skill_text: str,
    task: dict,
    timeout: int = DEFAULT_TIMEOUT,
) -> str:
    """Run one task against the target agent with the skill prepended.

    Tries `--system-prompt-file` first, then falls back to plain prepend.
    """
    # We use plain prepend for portability — Claude Code's `claude -p` reads
    # stdin as the user prompt and accepts an `--append-system-prompt` arg but
    # not every CLI surface speaks the same dialect. Prepending is the lowest
    # common denominator.
    composite = (
        "SKILL DOCUMENT (read this before answering):\n"
        "---\n"
        f"{skill_text}\n"
        "---\n\n"
        f"TASK:\n{task['prompt']}\n"
    )
    return call_llm_text(target_cmd, composite, timeout=timeout)


def score_rollout(
    verifier: str,
    optimizer_cmd: str,
    rollout_output: str,
    task: dict,
) -> int:
    if verifier == "exact-match":
        return verify_exact_match(rollout_output, task.get("reference_answer", ""))
    if verifier == "llm-judge":
        return verify_llm_judge(
            optimizer_cmd,
            rollout_output,
            task.get("reference_answer", ""),
            task["prompt"],
        )
    # Treat anything else as a script path.
    return verify_script(Path(verifier), rollout_output, task.get("reference_answer", ""), task["prompt"])


# --------------------------------------------------------------------------- #
# Reflection stages                                                           #
# --------------------------------------------------------------------------- #

def _read_prompt(prompts_dir: Path, name: str) -> str:
    return (prompts_dir / name).read_text(encoding="utf-8")


def _format_trajectories(rollouts: list[dict]) -> str:
    out = []
    for r in rollouts:
        out.append(
            f"--- TASK {r['task_id']} (score={r['score']}) ---\n"
            f"PROMPT: {r['prompt']}\n"
            f"REFERENCE: {r['reference']}\n"
            f"AGENT_OUTPUT: {r['output']}\n"
        )
    return "\n".join(out)


def analyse_minibatch(
    optimizer_cmd: str,
    prompts_dir: Path,
    contract_file: str,
    rollouts: list[dict],
    skill_text: str,
    edit_budget: int,
    meta_skill: str | None,
) -> dict:
    """Run one analyst call on a minibatch and return the patch."""
    contract = _read_prompt(prompts_dir, contract_file)
    pieces = []
    if meta_skill:
        pieces.append(f"## OPTIMIZER MEMORY (apply this guidance)\n{meta_skill}\n")
    pieces.append(contract)
    pieces.append(f"\n## EDIT BUDGET\nL = {edit_budget}\n")
    pieces.append(f"\n## CURRENT SKILL DOCUMENT\n```\n{skill_text}\n```\n")
    pieces.append(f"\n## TRAJECTORIES\n{_format_trajectories(rollouts)}\n")
    prompt = "".join(pieces)
    parsed = call_llm_json(optimizer_cmd, prompt) or {}
    # Normalise: the analyst contracts wrap edits inside a `patch` envelope.
    patch = parsed.get("patch") or {"edits": parsed.get("edits", []), "reasoning": parsed.get("reasoning", "")}
    return patch


def merge_patches(
    optimizer_cmd: str,
    prompts_dir: Path,
    contract_file: str,
    patches: list[dict],
    skill_text: str,
    meta_skill: str | None,
) -> dict:
    """Merge a list of patches via the given merge contract."""
    if not patches:
        return {"edits": [], "reasoning": "no patches to merge"}
    contract = _read_prompt(prompts_dir, contract_file)
    pieces = []
    if meta_skill:
        pieces.append(f"## OPTIMIZER MEMORY (apply this guidance)\n{meta_skill}\n")
    pieces.append(contract)
    pieces.append(f"\n## CURRENT SKILL DOCUMENT\n```\n{skill_text}\n```\n")
    pieces.append(f"\n## PATCHES TO MERGE\n{json.dumps(patches, indent=2)}\n")
    parsed = call_llm_json(optimizer_cmd, "".join(pieces)) or {}
    if "edits" not in parsed:
        parsed["edits"] = []
    return parsed


def rank_and_clip(
    optimizer_cmd: str,
    prompts_dir: Path,
    edits: list[dict],
    skill_text: str,
    budget: int,
    meta_skill: str | None,
) -> list[dict]:
    """Ask the optimiser to rank edits and clip to `budget`."""
    if not edits:
        return []
    if len(edits) <= budget:
        return edits
    contract = _read_prompt(prompts_dir, "ranking.md")
    pieces = []
    if meta_skill:
        pieces.append(f"## OPTIMIZER MEMORY (apply this guidance)\n{meta_skill}\n")
    pieces.append(contract)
    pieces.append(f"\n## BUDGET\nSelect at most {budget} edits.\n")
    pieces.append(f"\n## CURRENT SKILL DOCUMENT\n```\n{skill_text}\n```\n")
    pieces.append(f"\n## CANDIDATE EDITS (indexed)\n{json.dumps(edits, indent=2)}\n")
    parsed = call_llm_json(optimizer_cmd, "".join(pieces)) or {}
    indices = parsed.get("selected_indices") or list(range(min(budget, len(edits))))
    picked = []
    for idx in indices[:budget]:
        if isinstance(idx, int) and 0 <= idx < len(edits):
            picked.append(edits[idx])
    return picked or edits[:budget]


# --------------------------------------------------------------------------- #
# Slow update + meta-skill                                                    #
# --------------------------------------------------------------------------- #

def slow_update_step(
    optimizer_cmd: str,
    prompts_dir: Path,
    prev_skill_text: str,
    curr_skill_text: str,
    longitudinal: dict,
    previous_guidance: str | None,
) -> str | None:
    contract = _read_prompt(prompts_dir, "slow_update.md")
    pieces = [
        contract,
        f"\n## PREVIOUS EPOCH SKILL\n```\n{prev_skill_text}\n```\n",
        f"\n## CURRENT EPOCH SKILL\n```\n{curr_skill_text}\n```\n",
        f"\n## LONGITUDINAL COMPARISON\n{json.dumps(longitudinal, indent=2)}\n",
    ]
    if previous_guidance:
        pieces.append(f"\n## PREVIOUS SLOW UPDATE GUIDANCE\n{previous_guidance}\n")
    parsed = call_llm_json(optimizer_cmd, "".join(pieces)) or {}
    return parsed.get("slow_update_content")


def meta_skill_step(
    optimizer_cmd: str,
    prompts_dir: Path,
    prev_skill_text: str,
    curr_skill_text: str,
    longitudinal: dict,
    previous_meta_skill: str | None,
) -> str | None:
    contract = _read_prompt(prompts_dir, "meta_skill.md")
    pieces = [
        contract,
        f"\n## PREVIOUS EPOCH SKILL\n```\n{prev_skill_text}\n```\n",
        f"\n## CURRENT EPOCH SKILL\n```\n{curr_skill_text}\n```\n",
        f"\n## LONGITUDINAL COMPARISON\n{json.dumps(longitudinal, indent=2)}\n",
    ]
    if previous_meta_skill:
        pieces.append(f"\n## PREVIOUS OPTIMIZER MEMORY\n{previous_meta_skill}\n")
    parsed = call_llm_json(optimizer_cmd, "".join(pieces)) or {}
    return parsed.get("meta_skill_content")


def build_longitudinal(
    prev_rollouts: list[dict],
    curr_rollouts: list[dict],
) -> dict:
    """Categorise paired same-task rollouts into regress/improve/stable."""
    prev_by_id = {r["task_id"]: r for r in prev_rollouts}
    regressions, persistent_failures, improvements, stable_successes = [], [], [], []
    for curr in curr_rollouts:
        prev = prev_by_id.get(curr["task_id"])
        if prev is None:
            continue
        pair = {
            "task_id": curr["task_id"],
            "prompt": curr["prompt"],
            "prev_score": prev["score"],
            "curr_score": curr["score"],
            "prev_output": prev["output"],
            "curr_output": curr["output"],
        }
        if prev["score"] == 1 and curr["score"] == 0:
            regressions.append(pair)
        elif prev["score"] == 0 and curr["score"] == 0:
            persistent_failures.append(pair)
        elif prev["score"] == 0 and curr["score"] == 1:
            improvements.append(pair)
        else:
            stable_successes.append(pair)
    return {
        "regressions": regressions,
        "persistent_failures": persistent_failures,
        "improvements": improvements,
        "stable_successes": stable_successes,
    }


# --------------------------------------------------------------------------- #
# Orchestration                                                               #
# --------------------------------------------------------------------------- #

def evaluate_skill(
    target_cmd: str,
    optimizer_cmd: str,
    verifier: str,
    skill_text: str,
    tasks: list[dict],
) -> tuple[float, list[dict]]:
    """Run rollouts for every task and return (mean_score, rollouts)."""
    rollouts: list[dict] = []
    for task in tasks:
        try:
            output = run_rollout(target_cmd, skill_text, task)
        except Exception as exc:  # noqa: BLE001
            log(f"  [warn] rollout for {task['id']} failed: {exc}")
            output = ""
        score = score_rollout(verifier, optimizer_cmd, output, task)
        rollouts.append({
            "task_id": task["id"],
            "prompt": task["prompt"],
            "reference": task.get("reference_answer", ""),
            "output": output,
            "score": score,
        })
    mean = sum(r["score"] for r in rollouts) / max(1, len(rollouts))
    return mean, rollouts


def reflect_and_propose(
    optimizer_cmd: str,
    prompts_dir: Path,
    rollouts: list[dict],
    skill_text: str,
    minibatch_size: int,
    edit_budget: int,
    meta_skill: str | None,
    rejected_buffer: list[dict],
) -> dict:
    """Run §C.2 reflection: failure + success analyses, three merge calls,
    then ranking. Returns the final patch with `edits`.
    """
    failures = [r for r in rollouts if r["score"] == 0]
    successes = [r for r in rollouts if r["score"] == 1]

    failure_patches: list[dict] = []
    success_patches: list[dict] = []

    # Per-minibatch failure analysis.
    for i in range(0, len(failures), minibatch_size):
        mb = failures[i:i + minibatch_size]
        if not mb:
            continue
        try:
            patch = analyse_minibatch(
                optimizer_cmd, prompts_dir,
                "analyst_error.md", mb, skill_text, edit_budget, meta_skill,
            )
            failure_patches.append(patch)
        except Exception as exc:  # noqa: BLE001
            log(f"  [warn] failure analysis failed: {exc}")

    # Per-minibatch success analysis.
    for i in range(0, len(successes), minibatch_size):
        mb = successes[i:i + minibatch_size]
        if not mb:
            continue
        try:
            patch = analyse_minibatch(
                optimizer_cmd, prompts_dir,
                "analyst_success.md", mb, skill_text, edit_budget, meta_skill,
            )
            success_patches.append(patch)
        except Exception as exc:  # noqa: BLE001
            log(f"  [warn] success analysis failed: {exc}")

    # Inject rejected-buffer context into the failure-merge call: per §4.4 it
    # is fed back into the next optimiser call within the same epoch.
    rejected_summary = json.dumps(rejected_buffer[-10:], indent=2) if rejected_buffer else "[]"
    failure_patches_with_context = failure_patches + [{
        "source": "rejected_buffer",
        "note": "These edits were rejected by the validation gate. Avoid repeating them.",
        "rejected": json.loads(rejected_summary),
    }] if rejected_buffer else failure_patches

    merged_failure = merge_patches(
        optimizer_cmd, prompts_dir,
        "merge_failure.md", failure_patches_with_context, skill_text, meta_skill,
    )
    merged_success = merge_patches(
        optimizer_cmd, prompts_dir,
        "merge_success.md", success_patches, skill_text, meta_skill,
    )
    merged_final = merge_patches(
        optimizer_cmd, prompts_dir,
        "merge_final.md", [merged_failure, merged_success], skill_text, meta_skill,
    )

    # Rank + clip.
    edits = merged_final.get("edits", []) or []
    edits = rank_and_clip(
        optimizer_cmd, prompts_dir,
        edits, skill_text, edit_budget, meta_skill,
    )
    return {
        "edits": edits,
        "merged_failure": merged_failure,
        "merged_success": merged_success,
        "merged_final": merged_final,
    }


def run_optimization(args: argparse.Namespace) -> int:
    skill_path, scope = find_skill(args.skill)
    if not skill_path:
        log(f"Error: skill '{args.skill}' not found in user or project scope")
        return 1
    log(f"Found skill: {skill_path} ({scope})")

    skill_root = Path(__file__).resolve().parent.parent
    prompts_dir = skill_root / "prompts"
    if not prompts_dir.exists():
        log(f"Error: prompts dir not found: {prompts_dir}")
        return 1

    tasks_path = Path(args.tasks).resolve()
    tasks = load_jsonl(tasks_path)
    if not tasks:
        log("Error: no tasks loaded")
        return 1
    tasks_by_id = {str(t["id"]): t for t in tasks}

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    # Splits.
    splits_path = output_dir / "splits.json"
    if args.resume and splits_path.exists():
        splits = read_json(splits_path)
        log(f"Resumed splits from {splits_path}")
    else:
        splits = hash_split(tasks, args.train_frac, args.sel_frac, args.test_frac, args.seed)
        write_json(splits_path, splits)
    train_tasks = [tasks_by_id[i] for i in splits["train"] if i in tasks_by_id]
    sel_tasks = [tasks_by_id[i] for i in splits["selection"] if i in tasks_by_id]
    test_tasks = [tasks_by_id[i] for i in splits["test"] if i in tasks_by_id]
    log(f"Splits: train={len(train_tasks)} selection={len(sel_tasks)} test={len(test_tasks)}")

    # State.
    state_path = output_dir / "state.json"
    if args.resume and state_path.exists():
        state = read_json(state_path)
        log(f"Resumed state: epoch={state['epoch']} step={state['step']}")
    else:
        state = {
            "epoch": 1,
            "step": 0,
            "current_score": None,
            "best_score": None,
        }

    current_skill_path = output_dir / "current_skill.md"
    best_skill_path = output_dir / "best_skill.md"
    meta_skill_path = output_dir / "meta_skill.json"
    rejected_buffer_path = output_dir / "rejected_buffer.json"
    edit_apply_report_path = output_dir / "edit_apply_report.json"

    # Seed skill from source if not resuming.
    if not (args.resume and current_skill_path.exists()):
        shutil.copyfile(skill_path / "SKILL.md", current_skill_path)
    if not best_skill_path.exists():
        shutil.copyfile(current_skill_path, best_skill_path)

    meta_skill: str | None = None
    if meta_skill_path.exists():
        meta_skill = read_json(meta_skill_path).get("content")

    rejected_buffer: list[dict] = []
    if rejected_buffer_path.exists():
        rejected_buffer = read_json(rejected_buffer_path)

    accepted_log: list[dict] = []
    if edit_apply_report_path.exists():
        accepted_log = read_json(edit_apply_report_path)

    history: list[dict] = []
    random.seed(args.seed)

    # Compute the planned schedule up front for reporting and dry-run.
    schedule_table = [
        {"epoch": e, "L_t": lr_for_epoch(args.edit_budget, args.lr_schedule, e, args.epochs)}
        for e in range(1, args.epochs + 1)
    ]
    log(f"L_t schedule ({args.lr_schedule}): {schedule_table}")

    if args.dry_run:
        log("--- DRY RUN ---")
        log(f"splits: {json.dumps(splits, indent=2)}")
        log(f"target_cmd: {args.target_cmd}")
        log(f"optimizer_cmd: {args.optimizer_cmd}")
        log(f"verifier: {args.verifier}")
        log(f"rollout_batch={args.rollout_batch} reflection_minibatch={args.reflection_minibatch}")
        # Print prompt previews.
        for name in ("analyst_error.md", "analyst_success.md", "merge_failure.md",
                     "merge_success.md", "merge_final.md", "ranking.md",
                     "slow_update.md", "meta_skill.md"):
            preview = _read_prompt(prompts_dir, name)[:200].replace("\n", " ")
            log(f"  prompt[{name}]: {preview}...")
        log("--- end dry run ---")
        return 0

    # Baseline score on selection split using current skill.
    if state["current_score"] is None:
        log("Scoring baseline on selection split...")
        skill_text = current_skill_path.read_text(encoding="utf-8")
        baseline, _ = evaluate_skill(
            args.target_cmd, args.optimizer_cmd, args.verifier, skill_text, sel_tasks,
        )
        state["current_score"] = baseline
        state["best_score"] = baseline
        write_json(state_path, state)
        log(f"Baseline selection score: {baseline:.3f}")

    epoch_end_rollouts: dict[int, list[dict]] = {}
    epoch_end_skills: dict[int, str] = {}

    for epoch in range(state["epoch"], args.epochs + 1):
        state["epoch"] = epoch
        L_t = lr_for_epoch(args.edit_budget, args.lr_schedule, epoch, args.epochs)
        log(f"\n=== Epoch {epoch}/{args.epochs} (L_t={L_t}) ===")
        # Steps per epoch = ceil(train / rollout_batch).
        steps_per_epoch = max(1, math.ceil(len(train_tasks) / max(1, args.rollout_batch)))

        for step in range(state["step"] + 1, steps_per_epoch + 1):
            state["step"] = step
            log(f"\n-- Step {step}/{steps_per_epoch} --")
            step_dir = output_dir / f"epoch-{epoch}" / f"step-{step}"
            step_dir.mkdir(parents=True, exist_ok=True)

            # Sample rollout_batch tasks.
            batch = random.sample(train_tasks, min(args.rollout_batch, len(train_tasks)))
            skill_text = current_skill_path.read_text(encoding="utf-8")

            log(f"Rolling out {len(batch)} train tasks...")
            _, rollouts = evaluate_skill(
                args.target_cmd, args.optimizer_cmd, args.verifier, skill_text, batch,
            )
            write_jsonl(step_dir / "rollouts.jsonl", rollouts)
            n_fail = sum(1 for r in rollouts if r["score"] == 0)
            n_pass = len(rollouts) - n_fail
            log(f"Rollouts: {n_pass} pass / {n_fail} fail")

            # Reflect.
            log("Reflecting...")
            proposal = reflect_and_propose(
                args.optimizer_cmd, prompts_dir,
                rollouts, skill_text, args.reflection_minibatch, L_t,
                meta_skill, rejected_buffer,
            )
            write_json(step_dir / "proposals.json", proposal)

            edits = proposal.get("edits", []) or []
            log(f"Proposed {len(edits)} edits after rank+clip")

            if not edits:
                log("No edits; nothing to validate")
                state["step"] = step
                write_json(state_path, state)
                continue

            # Apply to a candidate.
            candidate_text, apply_report = apply_edits(skill_text, edits)
            (step_dir / "candidate.md").write_text(candidate_text, encoding="utf-8")

            # Validate on the selection split.
            log("Validating candidate on selection split...")
            cand_score, _ = evaluate_skill(
                args.target_cmd, args.optimizer_cmd, args.verifier, candidate_text, sel_tasks,
            )
            decision = {
                "candidate_score": cand_score,
                "current_score": state["current_score"],
                "delta": cand_score - state["current_score"],
                "accepted": cand_score > state["current_score"],
                "L_t": L_t,
                "apply_report": apply_report,
                "edits": edits,
            }
            write_json(step_dir / "decision.json", decision)

            if decision["accepted"]:
                log(f"ACCEPT: {state['current_score']:.3f} -> {cand_score:.3f}")
                current_skill_path.write_text(candidate_text, encoding="utf-8")
                state["current_score"] = cand_score
                if cand_score > (state["best_score"] or 0.0):
                    state["best_score"] = cand_score
                    shutil.copyfile(current_skill_path, best_skill_path)
                accepted_log.append({
                    "epoch": epoch,
                    "step": step,
                    "score_before": decision["current_score"],
                    "score_after": cand_score,
                    "edits": edits,
                })
                write_json(edit_apply_report_path, accepted_log)
            else:
                log(f"REJECT: {state['current_score']:.3f} -> {cand_score:.3f}")
                rejected_buffer.append({
                    "epoch": epoch,
                    "step": step,
                    "score_delta": decision["delta"],
                    "reason": "validation gate: candidate score not strictly greater",
                    "edits": edits,
                })
                write_json(rejected_buffer_path, rejected_buffer)

            history.append({
                "epoch": epoch,
                "step": step,
                "L_t": L_t,
                "n_pass": n_pass,
                "n_fail": n_fail,
                "candidate_score": cand_score,
                "current_score": state["current_score"],
                "best_score": state["best_score"],
                "accepted": decision["accepted"],
            })
            write_json(state_path, state)

        # End of epoch: roll out a sampled subset of train for slow-update comparison.
        epoch_skill_text = current_skill_path.read_text(encoding="utf-8")
        epoch_end_skills[epoch] = epoch_skill_text

        if epoch >= 2 and (epoch - 1) in epoch_end_skills:
            log("Computing slow-update + meta-skill...")
            # Use a deterministic sample (top-N by id-hash) so comparison is paired.
            sample_size = min(20, len(train_tasks))
            sampled = sorted(train_tasks, key=lambda t: hashlib.sha256(str(t["id"]).encode()).hexdigest())[:sample_size]
            prev_text = epoch_end_skills[epoch - 1]
            _, prev_rollouts = evaluate_skill(
                args.target_cmd, args.optimizer_cmd, args.verifier, prev_text, sampled,
            )
            _, curr_rollouts = evaluate_skill(
                args.target_cmd, args.optimizer_cmd, args.verifier, epoch_skill_text, sampled,
            )
            epoch_end_rollouts[epoch] = curr_rollouts
            longitudinal = build_longitudinal(prev_rollouts, curr_rollouts)

            # Slow update -> protected section of the current skill.
            existing = epoch_skill_text
            _, prev_protected, _ = split_protected(existing)
            previous_guidance = None
            if prev_protected:
                inner = prev_protected[len(SLOW_UPDATE_START):-len(SLOW_UPDATE_END)].strip()
                previous_guidance = inner or None
            try:
                slow_text = slow_update_step(
                    args.optimizer_cmd, prompts_dir,
                    prev_text, epoch_skill_text, longitudinal, previous_guidance,
                )
                if slow_text:
                    new_text = overwrite_protected(existing, slow_text)
                    current_skill_path.write_text(new_text, encoding="utf-8")
                    epoch_end_skills[epoch] = new_text
                    log("Slow update applied to protected section")
            except Exception as exc:  # noqa: BLE001
                log(f"  [warn] slow update failed: {exc}")

            # Meta-skill -> optimizer-side memory only (never shipped).
            try:
                new_meta = meta_skill_step(
                    args.optimizer_cmd, prompts_dir,
                    prev_text, epoch_end_skills[epoch], longitudinal, meta_skill,
                )
                if new_meta:
                    meta_skill = new_meta
                    write_json(meta_skill_path, {"content": meta_skill, "epoch": epoch})
                    log("Meta-skill updated (optimizer-side only)")
            except Exception as exc:  # noqa: BLE001
                log(f"  [warn] meta-skill update failed: {exc}")

        # Reset step counter for next epoch and clear rejected buffer per §C
        # (the buffer is epoch-scoped so the optimiser sees fresh rejections).
        state["step"] = 0
        rejected_buffer = []
        write_json(rejected_buffer_path, rejected_buffer)
        write_json(state_path, state)

    # Final test evaluation on best skill.
    log("\n=== Final test evaluation on best_skill ===")
    best_text = best_skill_path.read_text(encoding="utf-8")
    test_score, test_rollouts = evaluate_skill(
        args.target_cmd, args.optimizer_cmd, args.verifier, best_text, test_tasks,
    )
    log(f"Test score: {test_score:.3f}")

    # Report.
    total_tokens = sum(approx_tokens(h.get("note", "")) for h in history)
    write_optimization_report(
        output_dir / "optimization_report.md",
        skill_name=args.skill,
        history=history,
        accepted_log=accepted_log,
        rejected_buffer_path=rejected_buffer_path,
        test_score=test_score,
        baseline_score=history[0]["current_score"] if history else None,
        best_score=state["best_score"],
        schedule_table=schedule_table,
        approx_tokens_used=total_tokens,
    )
    write_jsonl(output_dir / "test_rollouts.jsonl", test_rollouts)
    return 0


def write_optimization_report(
    path: Path,
    *,
    skill_name: str,
    history: list[dict],
    accepted_log: list[dict],
    rejected_buffer_path: Path,
    test_score: float,
    baseline_score: float | None,
    best_score: float | None,
    schedule_table: list[dict],
    approx_tokens_used: int,
) -> None:
    rejected_count = 0
    if rejected_buffer_path.exists():
        try:
            rejected_count = len(read_json(rejected_buffer_path))
        except Exception:  # noqa: BLE001
            rejected_count = 0

    lines = [
        f"# SkillOpt Optimization Report: {skill_name}",
        "",
        "## Summary",
        f"- Baseline selection score: {baseline_score if baseline_score is not None else 'n/a'}",
        f"- Best selection score: {best_score if best_score is not None else 'n/a'}",
        f"- Final test score: {test_score:.3f}",
        f"- Steps recorded: {len(history)}",
        f"- Accepted edits: {len(accepted_log)}",
        f"- Rejected proposals (last epoch buffer): {rejected_count}",
        f"- Approx tokens (rough): {approx_tokens_used}",
        "",
        "## L_t Schedule",
        "| Epoch | L_t |",
        "|-------|-----|",
    ]
    for row in schedule_table:
        lines.append(f"| {row['epoch']} | {row['L_t']} |")

    lines += [
        "",
        "## Per-step History",
        "| Epoch | Step | L_t | Pass | Fail | Candidate | Current | Best | Accepted |",
        "|-------|------|-----|------|------|-----------|---------|------|----------|",
    ]
    for h in history:
        lines.append(
            f"| {h['epoch']} | {h['step']} | {h['L_t']} | {h['n_pass']} | {h['n_fail']} | "
            f"{h['candidate_score']:.3f} | {h['current_score']:.3f} | {h['best_score']:.3f} | "
            f"{'yes' if h['accepted'] else 'no'} |"
        )

    lines += ["", "## Accepted Edits (Table 6 / Fig 4 style)"]
    for entry in accepted_log[:10]:
        lines.append(f"\n### Epoch {entry['epoch']} Step {entry['step']} ({entry['score_before']:.3f} -> {entry['score_after']:.3f})")
        for edit in entry["edits"][:3]:
            op = edit.get("op")
            target = (edit.get("target") or "")[:80]
            content_preview = (edit.get("content") or "")[:200].replace("\n", " ")
            lines.append(f"- **{op}** target=`{target}` content=`{content_preview}`")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
# Argparse                                                                    #
# --------------------------------------------------------------------------- #

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="SkillOpt-style optimisation loop for a Claude Code skill"
    )
    p.add_argument("skill", help="Skill name (must exist in user or project scope)")
    p.add_argument("--tasks", required=True, help="Path to tasks.jsonl")
    p.add_argument("--train-frac", type=float, default=0.4)
    p.add_argument("--sel-frac", type=float, default=0.2)
    p.add_argument("--test-frac", type=float, default=0.4)
    p.add_argument("--epochs", type=int, default=4)
    p.add_argument("--rollout-batch", type=int, default=8)
    p.add_argument("--reflection-minibatch", type=int, default=4)
    p.add_argument("--edit-budget", type=int, default=4)
    p.add_argument("--lr-schedule", choices=["constant", "linear", "cosine"], default="cosine")
    p.add_argument("--optimizer-cmd", default="claude -p --model claude-opus-4-7")
    p.add_argument("--target-cmd", default="claude -p --model claude-haiku-4-5-20251001")
    p.add_argument("--verifier", default="llm-judge",
                   help="'exact-match', 'llm-judge', or a path to a script")
    p.add_argument("--output-dir", default="./skillopt-runs/run-001")
    p.add_argument("--seed", type=int, default=DEFAULT_SEED)
    p.add_argument("--resume", action="store_true",
                   help="Resume from output-dir state.json if present")
    p.add_argument("--dry-run", action="store_true",
                   help="Plan and print schedule without running any LLM calls")
    return p


def main() -> int:
    args = build_parser().parse_args()
    try:
        return run_optimization(args)
    except KeyboardInterrupt:
        log("Interrupted")
        return 130
    except Exception as exc:  # noqa: BLE001
        log(f"Fatal: {exc}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
