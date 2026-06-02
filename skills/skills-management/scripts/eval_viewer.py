#!/usr/bin/env python3
"""Render an HTML viewer for a SkillOpt optimisation run.

Reads the artefacts written by `optimize_skill.py` and produces a single
self-contained HTML page summarising the run. Inspired by upstream
skill-creator's eval-viewer but adapted for our artefact layout. Supports
side-by-side comparison of two runs.

See `../references/optimization-artifacts-schemas.md` for the artefact
contract this script reads.
"""

import argparse
import difflib
import html
import json
import re
import sys
import webbrowser
from pathlib import Path


# Protected slow-update markers — mirror optimize_skill.py.
SLOW_UPDATE_START = "<!-- SLOW_UPDATE_START -->"
SLOW_UPDATE_END = "<!-- SLOW_UPDATE_END -->"

PROMPT_PREVIEW_CHARS = 200
REASONING_PREVIEW_CHARS = 120
EDIT_CONTENT_PREVIEW_CHARS = 80
MAX_DIFF_CONTEXT_LINES = 3


# --------------------------------------------------------------------------- #
# Helpers                                                                     #
# --------------------------------------------------------------------------- #

def log(msg: str) -> None:
    """Log to stderr so stdout stays clean."""
    print(msg, file=sys.stderr, flush=True)


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                log(f"  [warn] {path}: line {i}: invalid JSON ({exc})")
                continue
    return rows


def safe_read_text(path: Path) -> str | None:
    if not path.exists():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        log(f"  [warn] could not read {path}: {exc}")
        return None


def safe_read_json(path: Path):
    if not path.exists():
        return None
    try:
        return read_json(path)
    except (json.JSONDecodeError, OSError) as exc:
        log(f"  [warn] could not read {path}: {exc}")
        return None


def safe_read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        return read_jsonl(path)
    except OSError as exc:
        log(f"  [warn] could not read {path}: {exc}")
        return []


def truncate(text: str, limit: int) -> str:
    if text is None:
        return ""
    text = str(text)
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + "..."


def parse_skill_name(skill_text: str | None, report_text: str | None) -> str:
    """Pull a skill name from a YAML frontmatter or the report header."""
    if skill_text:
        match = re.match(r"^---\s*\n(.*?)\n---", skill_text, re.DOTALL)
        if match:
            for line in match.group(1).splitlines():
                line = line.strip()
                if line.startswith("name:"):
                    return line.split(":", 1)[1].strip().strip("\"'")
    if report_text:
        match = re.search(r"^#\s*SkillOpt Optimization Report:\s*(.+)$", report_text, re.M)
        if match:
            return match.group(1).strip()
    return "(unknown)"


def parse_report_summary(text: str | None) -> dict:
    """Pull the `## Summary` bullet list out of optimization_report.md."""
    if not text:
        return {}
    match = re.search(r"##\s*Summary\s*\n(.*?)(?:\n##\s|\Z)", text, re.DOTALL)
    if not match:
        return {}
    out: dict = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if not line.startswith("-") or ":" not in line:
            continue
        line = line.lstrip("- ").strip()
        key, raw_val = line.split(":", 1)
        out[key.strip()] = raw_val.strip()
    return out


def split_protected(content: str) -> tuple[str, str | None, str]:
    """Same semantics as optimize_skill.split_protected."""
    start = content.find(SLOW_UPDATE_START)
    end = content.find(SLOW_UPDATE_END)
    if start == -1 or end == -1 or end < start:
        return content, None, ""
    end_with_marker = end + len(SLOW_UPDATE_END)
    return content[:start], content[start:end_with_marker], content[end_with_marker:]


def extract_slow_update(skill_text: str | None) -> str | None:
    """Return the inner text of the slow-update block, if any."""
    if not skill_text:
        return None
    _, protected, _ = split_protected(skill_text)
    if protected is None:
        return None
    inner = protected[len(SLOW_UPDATE_START):-len(SLOW_UPDATE_END)]
    return inner.strip() or None


# --------------------------------------------------------------------------- #
# Artefact loader                                                             #
# --------------------------------------------------------------------------- #

def discover_steps(run_dir: Path) -> list[tuple[int, int, Path]]:
    """Walk epoch-*/step-* dirs in numerical order."""
    out: list[tuple[int, int, Path]] = []
    for epoch_dir in sorted(run_dir.glob("epoch-*")):
        if not epoch_dir.is_dir():
            continue
        match = re.match(r"epoch-(\d+)$", epoch_dir.name)
        if not match:
            continue
        epoch = int(match.group(1))
        for step_dir in sorted(epoch_dir.glob("step-*")):
            if not step_dir.is_dir():
                continue
            step_match = re.match(r"step-(\d+)$", step_dir.name)
            if not step_match:
                continue
            out.append((epoch, int(step_match.group(1)), step_dir))
    out.sort(key=lambda x: (x[0], x[1]))
    return out


def load_run(run_dir: Path) -> dict:
    """Read everything we need from an output-dir into one dict."""
    record: dict = {
        "path": run_dir,
        "name": run_dir.name,
        "exists": run_dir.exists(),
    }
    if not run_dir.exists():
        log(f"  [warn] run dir does not exist: {run_dir}")
        return record

    record["splits"] = safe_read_json(run_dir / "splits.json") or {}
    record["state"] = safe_read_json(run_dir / "state.json") or {}
    record["meta_skill"] = safe_read_json(run_dir / "meta_skill.json")
    record["rejected_buffer"] = safe_read_json(run_dir / "rejected_buffer.json") or []
    record["accepted_log"] = safe_read_json(run_dir / "edit_apply_report.json") or []
    record["initial_skill"] = safe_read_text(run_dir / "initial_skill.md")
    record["best_skill"] = safe_read_text(run_dir / "best_skill.md")
    record["current_skill"] = safe_read_text(run_dir / "current_skill.md")
    record["report_text"] = safe_read_text(run_dir / "optimization_report.md")
    record["test_rollouts"] = safe_read_jsonl(run_dir / "test_rollouts.jsonl")

    # Headline metadata.
    record["report_summary"] = parse_report_summary(record["report_text"])
    record["skill_name"] = parse_skill_name(
        record.get("initial_skill"), record.get("report_text")
    )

    # Per-step data.
    steps: list[dict] = []
    for epoch, step, step_dir in discover_steps(run_dir):
        rollouts = safe_read_jsonl(step_dir / "rollouts.jsonl")
        proposals = safe_read_json(step_dir / "proposals.json")
        decision = safe_read_json(step_dir / "decision.json")
        candidate_text = safe_read_text(step_dir / "candidate.md")
        n_pass = sum(1 for r in rollouts if r.get("score") == 1)
        n_fail = sum(1 for r in rollouts if r.get("score") == 0)
        mean_score = (sum(r.get("score", 0) for r in rollouts) / len(rollouts)) if rollouts else None
        steps.append({
            "epoch": epoch,
            "step": step,
            "step_dir": step_dir,
            "rollouts": rollouts,
            "proposals": proposals,
            "decision": decision,
            "candidate_text": candidate_text,
            "n_pass": n_pass,
            "n_fail": n_fail,
            "mean_score": mean_score,
        })
    record["steps"] = steps

    # Per-epoch aggregation for the bar chart.
    by_epoch: dict[int, list[dict]] = {}
    for s in steps:
        by_epoch.setdefault(s["epoch"], []).append(s)
    epoch_summaries: list[dict] = []
    for epoch in sorted(by_epoch.keys()):
        epoch_steps = by_epoch[epoch]
        scored = [s for s in epoch_steps if s["mean_score"] is not None]
        mean_rollout = (
            sum(s["mean_score"] for s in scored) / len(scored)
            if scored else None
        )
        decisions = [s["decision"] for s in epoch_steps if s["decision"]]
        cand_scores = [d.get("candidate_score") for d in decisions if d.get("candidate_score") is not None]
        mean_candidate = sum(cand_scores) / len(cand_scores) if cand_scores else None
        accepted_in_epoch = sum(1 for d in decisions if d.get("accepted"))
        rejected_in_epoch = sum(1 for d in decisions if d.get("accepted") is False)
        epoch_summaries.append({
            "epoch": epoch,
            "n_steps": len(epoch_steps),
            "mean_rollout_score": mean_rollout,
            "mean_candidate_score": mean_candidate,
            "accepted": accepted_in_epoch,
            "rejected": rejected_in_epoch,
        })
    record["epoch_summaries"] = epoch_summaries

    return record


# --------------------------------------------------------------------------- #
# Rendering helpers                                                           #
# --------------------------------------------------------------------------- #

def esc(text) -> str:
    if text is None:
        return ""
    return html.escape(str(text))


def fmt_score(value, places: int = 3) -> str:
    if value is None:
        return "n/a"
    try:
        return f"{float(value):.{places}f}"
    except (TypeError, ValueError):
        return esc(value)


def render_mini_markdown(text: str | None) -> str:
    """Render a very small subset of markdown safely.

    Handles fenced code blocks, **bold**, and paragraph breaks. Anything
    else stays inside the output as literal escaped text. We intentionally
    do not pull a markdown library — readability over fanciness.
    """
    if not text:
        return ""
    # Pull out fenced code blocks first so their content is not touched.
    code_blocks: list[str] = []
    def _stash(match: re.Match) -> str:
        code_blocks.append(match.group(1))
        return f"\x00CODE{len(code_blocks) - 1}\x00"
    text = re.sub(r"```(?:[a-zA-Z0-9_-]*)\n(.*?)```", _stash, text, flags=re.DOTALL)

    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)

    paragraphs = re.split(r"\n\s*\n", escaped.strip())
    rendered_paragraphs: list[str] = []
    for p in paragraphs:
        if not p.strip():
            continue
        # Preserve single line breaks within a paragraph.
        p_html = p.replace("\n", "<br>")
        rendered_paragraphs.append(f"<p>{p_html}</p>")
    body = "\n".join(rendered_paragraphs)

    def _restore(match: re.Match) -> str:
        idx = int(match.group(1))
        return (
            "</p><pre><code>"
            + html.escape(code_blocks[idx])
            + "</code></pre><p>"
        )

    body = re.sub(r"\x00CODE(\d+)\x00", _restore, body)
    # Clean up empty paragraphs introduced by code-block restoration.
    body = re.sub(r"<p>\s*</p>", "", body)
    return body


def render_bar_chart(epoch_summaries: list[dict]) -> str:
    """Inline SVG bar chart of per-epoch mean candidate scores."""
    if not epoch_summaries:
        return "<p class=\"empty\">No epoch data yet.</p>"

    width = 600
    height = 240
    pad_left = 50
    pad_right = 20
    pad_top = 30
    pad_bottom = 50
    plot_w = width - pad_left - pad_right
    plot_h = height - pad_top - pad_bottom
    n = len(epoch_summaries)
    bar_gap = 16
    bar_w = max(8.0, (plot_w - bar_gap * (n - 1)) / n) if n else 0
    parts: list[str] = []
    parts.append(
        f'<svg viewBox="0 0 {width} {height}" width="100%" '
        'preserveAspectRatio="xMidYMid meet" class="bar-chart" role="img" '
        'aria-label="Per-epoch mean score">'
    )
    # Axes.
    parts.append(
        f'<line x1="{pad_left}" y1="{pad_top}" x2="{pad_left}" '
        f'y2="{height - pad_bottom}" stroke="#333" />'
    )
    parts.append(
        f'<line x1="{pad_left}" y1="{height - pad_bottom}" '
        f'x2="{width - pad_right}" y2="{height - pad_bottom}" stroke="#333" />'
    )
    # Y-axis gridlines + labels at 0, 0.5, 1.
    for frac in (0.0, 0.5, 1.0):
        y = pad_top + plot_h * (1.0 - frac)
        parts.append(
            f'<line x1="{pad_left}" y1="{y:.1f}" x2="{width - pad_right}" '
            f'y2="{y:.1f}" stroke="#ddd" stroke-dasharray="2,2" />'
        )
        parts.append(
            f'<text x="{pad_left - 6:.1f}" y="{y + 4:.1f}" '
            f'text-anchor="end" font-size="11" fill="#555">{frac:.1f}</text>'
        )

    for i, summary in enumerate(epoch_summaries):
        score = summary.get("mean_candidate_score")
        if score is None:
            score = summary.get("mean_rollout_score") or 0.0
        if score is None:
            score = 0.0
        x = pad_left + i * (bar_w + bar_gap)
        bar_h = max(1.0, plot_h * score)
        y = pad_top + plot_h - bar_h
        accepted = summary.get("accepted", 0)
        rejected = summary.get("rejected", 0)
        title = (
            f"Epoch {summary['epoch']}: mean candidate "
            f"{score:.3f} (accepted {accepted}, rejected {rejected})"
        )
        parts.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bar_h:.1f}" '
            f'fill="#3b6fb5" rx="2"><title>{esc(title)}</title></rect>'
        )
        # Score above each bar.
        parts.append(
            f'<text x="{x + bar_w / 2:.1f}" y="{y - 6:.1f}" text-anchor="middle" '
            f'font-size="11" fill="#222">{score:.2f}</text>'
        )
        # X-axis label.
        parts.append(
            f'<text x="{x + bar_w / 2:.1f}" y="{height - pad_bottom + 18:.1f}" '
            f'text-anchor="middle" font-size="12" fill="#222">E{summary["epoch"]}</text>'
        )
        parts.append(
            f'<text x="{x + bar_w / 2:.1f}" y="{height - pad_bottom + 34:.1f}" '
            f'text-anchor="middle" font-size="10" fill="#666">+{accepted}/-{rejected}</text>'
        )
    # Title.
    parts.append(
        f'<text x="{width / 2:.1f}" y="18" text-anchor="middle" '
        'font-size="13" fill="#222" font-weight="600">'
        'Mean candidate score per epoch</text>'
    )
    parts.append("</svg>")
    return "".join(parts)


def render_edit_block(edit: dict) -> str:
    """Compact representation of a single edit. Caller wraps in <details>."""
    op = esc(edit.get("op"))
    target = edit.get("target") or ""
    content = edit.get("content") or ""
    reasoning = edit.get("reasoning") or ""
    rows = [f'<div class="edit-op"><span class="op-{esc(edit.get("op") or "unknown")}">{op}</span></div>']
    if target:
        rows.append(
            f'<div class="edit-row"><span class="label">target:</span>'
            f'<pre class="inline">{esc(truncate(target, 240))}</pre></div>'
        )
    if content:
        rows.append(
            f'<div class="edit-row"><span class="label">content:</span>'
            f'<pre>{esc(content)}</pre></div>'
        )
    if reasoning:
        rows.append(
            f'<div class="edit-row"><span class="label">reasoning:</span>'
            f'<div>{esc(reasoning)}</div></div>'
        )
    return '<div class="edit-block">' + "".join(rows) + "</div>"


def render_accepted_edits(accepted_log: list[dict]) -> str:
    if not accepted_log:
        return "<p class=\"empty\">No accepted edits.</p>"
    items: list[str] = []
    for i, entry in enumerate(accepted_log):
        epoch = entry.get("epoch")
        step = entry.get("step")
        score_before = entry.get("score_before")
        score_after = entry.get("score_after")
        delta = None
        if isinstance(score_before, (int, float)) and isinstance(score_after, (int, float)):
            delta = score_after - score_before
        edits = entry.get("edits", []) or []
        first_reasoning = ""
        if edits:
            first_reasoning = truncate(edits[0].get("reasoning") or "", REASONING_PREVIEW_CHARS)
        summary = (
            f'<span class="badge accept">accept</span>'
            f'<span class="cell">E{esc(epoch)} S{esc(step)}</span>'
            f'<span class="cell">{esc(len(edits))} edit(s)</span>'
            f'<span class="cell">{fmt_score(score_before)} &rarr; {fmt_score(score_after)}'
        )
        if delta is not None:
            sign = "+" if delta >= 0 else ""
            summary += f' <span class="delta">({sign}{delta:.3f})</span>'
        summary += "</span>"
        if first_reasoning:
            summary += f'<span class="reasoning">{esc(first_reasoning)}</span>'
        body = "".join(render_edit_block(e) for e in edits) if edits else \
            "<p class=\"empty\">no edits recorded</p>"
        items.append(
            f'<details class="timeline-entry"><summary>{summary}</summary>'
            f'{body}</details>'
        )
    return "<div class=\"timeline\">" + "".join(items) + "</div>"


def render_rejected_edits(steps: list[dict], rejected_buffer: list[dict]) -> str:
    """Show rejected items from both per-step decisions and the last-epoch buffer.

    The per-step `decision.json` files cover the whole run; the
    `rejected_buffer.json` only covers the last epoch (it is cleared at
    every epoch boundary). We merge the two and dedupe.
    """
    rows: list[dict] = []
    seen: set[tuple] = set()

    for step_data in steps:
        decision = step_data.get("decision") or {}
        if decision.get("accepted") is not False:
            continue
        edits = decision.get("edits") or []
        key = (step_data["epoch"], step_data["step"], "decision")
        seen.add(key)
        rows.append({
            "epoch": step_data["epoch"],
            "step": step_data["step"],
            "edits": edits,
            "candidate_score": decision.get("candidate_score"),
            "current_score": decision.get("current_score"),
            "delta": decision.get("delta"),
            "reason": "validation gate: candidate score not strictly greater",
            "apply_report": decision.get("apply_report") or [],
        })

    for entry in rejected_buffer:
        key = (entry.get("epoch"), entry.get("step"), "buffer")
        if (entry.get("epoch"), entry.get("step"), "decision") in seen:
            continue
        if key in seen:
            continue
        seen.add(key)
        rows.append({
            "epoch": entry.get("epoch"),
            "step": entry.get("step"),
            "edits": entry.get("edits") or [],
            "candidate_score": None,
            "current_score": None,
            "delta": entry.get("score_delta"),
            "reason": entry.get("reason") or "rejected",
            "apply_report": [],
        })

    if not rows:
        return "<p class=\"empty\">No rejected proposals.</p>"

    rows.sort(key=lambda r: (r["epoch"] or 0, r["step"] or 0))
    items: list[str] = []
    for r in rows:
        edits = r["edits"]
        delta = r["delta"]
        first_reasoning = ""
        if edits:
            first_reasoning = truncate(edits[0].get("reasoning") or "", REASONING_PREVIEW_CHARS)
        summary = (
            f'<span class="badge reject">reject</span>'
            f'<span class="cell">E{esc(r["epoch"])} S{esc(r["step"])}</span>'
            f'<span class="cell">{esc(len(edits))} edit(s)</span>'
        )
        if r["candidate_score"] is not None and r["current_score"] is not None:
            summary += (
                f'<span class="cell">{fmt_score(r["current_score"])} &rarr; '
                f'{fmt_score(r["candidate_score"])}</span>'
            )
        if delta is not None:
            try:
                summary += f' <span class="delta">({float(delta):+.3f})</span>'
            except (TypeError, ValueError):
                pass
        summary += f' <span class="reason">{esc(r["reason"])}</span>'
        if first_reasoning:
            summary += f'<span class="reasoning">{esc(first_reasoning)}</span>'

        body_parts = [render_edit_block(e) for e in edits] if edits else \
            ["<p class=\"empty\">no edits recorded</p>"]
        # Render the apply_report — useful when the gate rejected because every
        # edit silently failed to apply.
        if r["apply_report"]:
            ar_rows = ["<table class=\"apply-report\"><thead><tr>"
                       "<th>#</th><th>op</th><th>applied</th><th>error</th>"
                       "<th>target</th></tr></thead><tbody>"]
            for ar in r["apply_report"]:
                ar_rows.append(
                    f'<tr><td>{esc(ar.get("index"))}</td>'
                    f'<td>{esc(ar.get("op"))}</td>'
                    f'<td>{"yes" if ar.get("applied") else "no"}</td>'
                    f'<td>{esc(ar.get("error") or "")}</td>'
                    f'<td><code>{esc(truncate(ar.get("target_preview") or "", 80))}</code></td></tr>'
                )
            ar_rows.append("</tbody></table>")
            body_parts.append("".join(ar_rows))
        body = "".join(body_parts)
        items.append(
            f'<details class="timeline-entry rejected"><summary>{summary}</summary>'
            f'{body}</details>'
        )
    return "<div class=\"timeline\">" + "".join(items) + "</div>"


def render_slow_update_history(run: dict) -> str:
    """Show every epoch's terminal slow-update content (if any).

    We can only reliably extract two snapshots from on-disk artefacts: the
    current `best_skill.md` (whatever the latest accepted candidate looked
    like) and the `meta_skill.json` (optimiser-side memory). The
    optimisation loop does not snapshot the slow-update text per epoch on
    disk, so the per-epoch history is best-effort.
    """
    slow = extract_slow_update(run.get("best_skill"))
    meta = run.get("meta_skill") or {}
    parts: list[str] = []
    if slow:
        parts.append(
            f'<details open><summary>Best skill slow-update block</summary>'
            f'<pre class="slow-update">{esc(slow)}</pre></details>'
        )
    if meta:
        epoch = meta.get("epoch")
        content = meta.get("content") or ""
        parts.append(
            f'<details><summary>Optimizer memory '
            f'(meta_skill, epoch {esc(epoch)})</summary>'
            f'<pre class="meta-skill">{esc(content)}</pre></details>'
        )
    if not parts:
        return "<p class=\"empty\">No slow-update or meta-skill content.</p>"
    return "".join(parts)


def render_rollout_grading(grading) -> str:
    """Render an assertions-style grading block as a checklist."""
    if grading is None:
        return ""
    if isinstance(grading, list):
        items = grading
    elif isinstance(grading, dict) and isinstance(grading.get("checks"), list):
        items = grading["checks"]
    else:
        return f'<pre class="grading-raw">{esc(json.dumps(grading, indent=2))}</pre>'
    if not items:
        return ""
    rows: list[str] = ["<ul class=\"grading\">"]
    for item in items:
        if not isinstance(item, dict):
            rows.append(f"<li>{esc(item)}</li>")
            continue
        passed = item.get("pass")
        if passed is None:
            passed = item.get("passed")
        if passed is None:
            passed = item.get("score") == 1
        check_mark = "[x]" if passed else "[ ]"
        label = item.get("name") or item.get("description") or item.get("assertion") or ""
        evidence = item.get("evidence") or item.get("reason") or ""
        css_class = "pass" if passed else "fail"
        rows.append(
            f'<li class="{css_class}"><span class="check">{check_mark}</span> '
            f'{esc(label)}'
            + (f'<div class="evidence">{esc(evidence)}</div>' if evidence else "")
            + "</li>"
        )
    rows.append("</ul>")
    return "".join(rows)


def pick_per_task_rollouts(run: dict) -> tuple[list[dict], str]:
    """Prefer test_rollouts.jsonl. Fall back to the last step's rollouts."""
    if run.get("test_rollouts"):
        return run["test_rollouts"], "test_rollouts.jsonl (held-out test split)"
    if run.get("steps"):
        last = run["steps"][-1]
        if last.get("rollouts"):
            return last["rollouts"], (
                f"epoch-{last['epoch']}/step-{last['step']}/rollouts.jsonl "
                f"(no test rollouts on disk)"
            )
    return [], ""


def render_per_task_rollouts(run: dict) -> str:
    rollouts, source = pick_per_task_rollouts(run)
    if not rollouts:
        return "<p class=\"empty\">No rollouts on disk.</p>"

    # Group by task_id to handle runs_per_task > 1 if the data has duplicates.
    groups: dict[str, list[dict]] = {}
    for r in rollouts:
        task_id = str(r.get("task_id"))
        groups.setdefault(task_id, []).append(r)

    items: list[str] = [f'<p class="source-note">Source: {esc(source)}</p>']
    for task_id in sorted(groups.keys()):
        entries = groups[task_id]
        scores = [e.get("score", 0) for e in entries if isinstance(e.get("score"), (int, float))]
        mean = sum(scores) / len(scores) if scores else 0.0
        stddev = None
        if len(scores) > 1:
            mean_val = sum(scores) / len(scores)
            var = sum((x - mean_val) ** 2 for x in scores) / (len(scores) - 1)
            stddev = var ** 0.5

        first = entries[0]
        prompt_preview = truncate(first.get("prompt") or "", PROMPT_PREVIEW_CHARS)
        score_display = f"{mean:.2f}" if len(scores) == 1 else f"{mean:.2f}"
        if stddev is not None:
            score_display += f" (sd {stddev:.2f}, n={len(scores)})"

        outputs: list[str] = []
        for i, e in enumerate(entries):
            grading_html = render_rollout_grading(e.get("grading"))
            label = f"Run {i + 1}" if len(entries) > 1 else "Output"
            outputs.append(
                f'<div class="rollout-run">'
                f'<div class="rollout-meta">{esc(label)} '
                f'(score {esc(e.get("score"))})</div>'
                f'<details><summary>prompt</summary>'
                f'<pre>{esc(e.get("prompt") or "")}</pre></details>'
                f'<details><summary>reference</summary>'
                f'<pre>{esc(e.get("reference") or "")}</pre></details>'
                f'<details><summary>output</summary>'
                f'<pre>{esc(e.get("output") or "")}</pre></details>'
                f'{grading_html}'
                f'</div>'
            )

        score_class = "pass" if mean >= 0.5 else "fail"
        items.append(
            f'<details class="task-entry"><summary>'
            f'<span class="cell task-id">{esc(task_id)}</span>'
            f'<span class="cell score {score_class}">{score_display}</span>'
            f'<span class="cell prompt-preview">{esc(prompt_preview)}</span>'
            f'</summary>'
            f'{"".join(outputs)}'
            f'</details>'
        )
    return "<div class=\"task-list\">" + "".join(items) + "</div>"


def render_diff(initial: str | None, best: str | None) -> str:
    if initial is None and best is None:
        return "<p class=\"empty\">No skill text on disk.</p>"
    initial_lines = (initial or "").splitlines()
    best_lines = (best or "").splitlines()
    if initial_lines == best_lines:
        return "<p class=\"empty\">Initial and best skill are identical.</p>"
    differ = difflib.HtmlDiff(wrapcolumn=80, tabsize=4)
    table_html = differ.make_table(
        initial_lines,
        best_lines,
        fromdesc="initial_skill.md",
        todesc="best_skill.md",
        context=True,
        numlines=MAX_DIFF_CONTEXT_LINES,
    )
    # difflib's HtmlDiff emits a small inline legend with classes we can style.
    return f'<div class="diff-wrap">{table_html}</div>'


def render_header(run: dict) -> str:
    state = run.get("state") or {}
    summary = run.get("report_summary") or {}
    steps = run.get("steps") or []
    n_steps = len(steps)
    epochs_completed = len({s["epoch"] for s in steps})
    accepted = len(run.get("accepted_log") or [])
    rejected_total = sum(
        1 for s in steps
        if isinstance(s.get("decision"), dict) and s["decision"].get("accepted") is False
    )

    baseline = summary.get("Baseline selection score")
    best_sel = summary.get("Best selection score") or state.get("best_score")
    final_test = summary.get("Final test score")

    rows = [
        ("Skill", esc(run.get("skill_name"))),
        ("Output dir", f"<code>{esc(run['path'])}</code>"),
        ("Epochs completed", esc(epochs_completed)),
        ("Steps recorded", esc(n_steps)),
        ("Baseline (selection)", esc(baseline if baseline is not None else fmt_score(state.get("current_score")))),
        ("Best (selection)", esc(best_sel) if best_sel is not None else "n/a"),
        ("Final test score", esc(final_test) if final_test is not None else "n/a"),
        ("Accepted edits", esc(accepted)),
        ("Rejected proposals", esc(rejected_total)),
    ]
    rendered = "".join(
        f'<tr><th>{label}</th><td>{value}</td></tr>'
        for label, value in rows
    )
    return f'<table class="header-table"><tbody>{rendered}</tbody></table>'


def render_footer_links(run: dict) -> str:
    """Relative links so they resolve when the HTML lives inside the run dir."""
    candidates = [
        ("optimization_report.md", "Full optimisation report"),
        ("meta_skill.json", "Optimizer memory"),
        ("edit_apply_report.json", "Accepted-edits log"),
        ("rejected_buffer.json", "Rejected buffer (last epoch)"),
        ("state.json", "Optimiser state"),
        ("splits.json", "Task splits"),
        ("test_rollouts.jsonl", "Test rollouts"),
        ("best_skill.md", "Best skill"),
        ("initial_skill.md", "Initial skill"),
    ]
    links: list[str] = []
    run_path = run["path"]
    for name, label in candidates:
        if (run_path / name).exists():
            links.append(f'<li><a href="{esc(name)}">{esc(label)}</a></li>')
    if not links:
        return ""
    return "<ul class=\"footer-links\">" + "".join(links) + "</ul>"


# --------------------------------------------------------------------------- #
# Page assembly                                                               #
# --------------------------------------------------------------------------- #

CSS = """
:root {
  color-scheme: light;
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  margin: 0;
  padding: 24px;
  background: #f7f8fa;
  color: #1d1f23;
  line-height: 1.45;
}
h1 { font-size: 22px; margin: 0 0 8px; }
h2 { font-size: 18px; margin: 28px 0 12px; padding-bottom: 6px; border-bottom: 1px solid #d8dde3; }
h3 { font-size: 15px; margin: 16px 0 8px; }
section { background: #fff; border: 1px solid #e1e4ea; border-radius: 8px;
          padding: 18px 22px; margin-bottom: 18px; }
table { border-collapse: collapse; }
.header-table th { text-align: left; padding: 4px 12px 4px 0; color: #555;
                   font-weight: 500; }
.header-table td { padding: 4px 0; }
code, pre { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
pre { background: #f4f5f8; border: 1px solid #e1e4ea; border-radius: 4px;
      padding: 8px 10px; overflow-x: auto; white-space: pre-wrap;
      word-wrap: break-word; max-width: 100%; font-size: 12px; line-height: 1.4; }
pre.inline { display: inline-block; padding: 2px 6px; margin: 0; }
.empty { color: #888; font-style: italic; margin: 8px 0; }
.bar-chart { display: block; max-width: 700px; }
.timeline { display: flex; flex-direction: column; gap: 8px; }
.timeline-entry { background: #f4f7fb; border: 1px solid #d6dee8; border-radius: 6px;
                  padding: 10px 12px; }
.timeline-entry.rejected { background: #fdf3f3; border-color: #ecc7c7; }
.timeline-entry summary { cursor: pointer; display: flex; flex-wrap: wrap;
                          gap: 10px; align-items: baseline; font-size: 13px; }
.timeline-entry[open] { padding-bottom: 14px; }
.cell { color: #444; }
.cell.task-id { font-family: ui-monospace, monospace; font-weight: 600; color: #1d1f23; }
.cell.prompt-preview { color: #555; flex: 1; min-width: 200px; }
.cell.score { font-family: ui-monospace, monospace; font-weight: 600; }
.cell.score.pass { color: #1b6f3e; }
.cell.score.fail { color: #a3271f; }
.badge { display: inline-block; padding: 2px 8px; border-radius: 10px;
         font-size: 11px; font-weight: 600; }
.badge.accept { background: #d5ecd9; color: #1b6f3e; }
.badge.reject { background: #f2d3d1; color: #a3271f; }
.delta { color: #555; font-family: ui-monospace, monospace; }
.reason { color: #a3271f; font-size: 12px; }
.reasoning { color: #555; font-size: 12px; flex-basis: 100%;
             margin-top: 4px; font-style: italic; }
.edit-block { background: #fff; border: 1px solid #dee2e9; border-radius: 4px;
              padding: 8px 10px; margin-top: 8px; }
.edit-op { font-family: ui-monospace, monospace; font-size: 12px;
           font-weight: 600; margin-bottom: 6px; }
.op-append { color: #1b6f3e; }
.op-insert_after { color: #295e9b; }
.op-replace { color: #8a6300; }
.op-delete { color: #a3271f; }
.op-unknown { color: #555; }
.edit-row { margin: 4px 0; font-size: 12px; }
.edit-row .label { display: inline-block; color: #777; min-width: 80px;
                   font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; }
.apply-report { width: 100%; margin-top: 10px; font-size: 12px; }
.apply-report th, .apply-report td { border: 1px solid #dee2e9;
                                     padding: 4px 6px; text-align: left; }
.apply-report th { background: #f4f5f8; }
.slow-update, .meta-skill { font-size: 12px; }
.task-entry { background: #f4f7fb; border: 1px solid #d6dee8;
              border-radius: 6px; padding: 10px 12px; }
.task-entry + .task-entry { margin-top: 8px; }
.task-entry summary { cursor: pointer; display: flex; gap: 12px;
                      align-items: baseline; font-size: 13px; flex-wrap: wrap; }
.task-list { display: flex; flex-direction: column; gap: 8px; }
.rollout-run { background: #fff; border: 1px solid #dee2e9; border-radius: 4px;
               padding: 8px 10px; margin-top: 8px; }
.rollout-meta { font-family: ui-monospace, monospace; font-size: 12px;
                color: #555; margin-bottom: 6px; }
.grading { list-style: none; padding: 0; margin: 8px 0 0; }
.grading li { padding: 4px 6px; border-radius: 4px; font-size: 12px; }
.grading li.pass { background: #e8f4ec; color: #1b6f3e; }
.grading li.fail { background: #f9e6e5; color: #a3271f; }
.grading .check { font-family: ui-monospace, monospace; font-weight: 700;
                  margin-right: 6px; }
.grading .evidence { color: #555; font-style: italic; margin-top: 4px;
                     font-size: 11px; }
.source-note { color: #777; font-size: 12px; margin: 0 0 10px; }
.diff-wrap { overflow-x: auto; }
.diff-wrap table { font-family: ui-monospace, monospace; font-size: 11px; border: 1px solid #ccc; }
.diff-wrap td { padding: 1px 4px; }
.diff-wrap .diff_header { background: #f4f5f8; padding: 4px 6px; }
.diff-wrap .diff_next { background: #f4f5f8; color: #888; }
.diff-wrap .diff_add { background: #e6f4ea; }
.diff-wrap .diff_chg { background: #fff4d4; }
.diff-wrap .diff_sub { background: #fbe1de; }
.footer-links { list-style: none; padding: 0; display: flex; gap: 14px;
                flex-wrap: wrap; }
.footer-links a { color: #295e9b; text-decoration: none; }
.footer-links a:hover { text-decoration: underline; }
.compare-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
.compare-grid > section { margin-bottom: 0; }
.compare-grid h1 { font-size: 18px; }
@media (max-width: 1000px) {
  .compare-grid { grid-template-columns: 1fr; }
}
.warning { background: #fff3cd; border: 1px solid #f0d57a; padding: 8px 12px;
           border-radius: 6px; color: #6b5500; font-size: 13px; }
"""


def render_run_page(run: dict, *, single: bool = True) -> str:
    """Render the body of one run as a sequence of <section> blocks."""
    if not run.get("exists"):
        return (
            f'<section class="warning">Run directory not found: '
            f'<code>{esc(run["path"])}</code></section>'
        )

    parts: list[str] = []
    title = f"SkillOpt run: {esc(run.get('skill_name') or '(unknown)')}"
    parts.append(f'<section><h1>{title}</h1>{render_header(run)}</section>')

    parts.append(
        '<section><h2>Per-epoch progress</h2>'
        + render_bar_chart(run.get("epoch_summaries") or [])
        + '</section>'
    )

    parts.append(
        '<section><h2>Accepted edits timeline</h2>'
        + render_accepted_edits(run.get("accepted_log") or [])
        + '</section>'
    )

    parts.append(
        '<section><h2>Rejected proposals</h2>'
        + render_rejected_edits(run.get("steps") or [], run.get("rejected_buffer") or [])
        + '</section>'
    )

    parts.append(
        '<section><h2>Slow-update &amp; optimizer memory</h2>'
        + render_slow_update_history(run)
        + '</section>'
    )

    parts.append(
        '<section><h2>Per-task rollouts</h2>'
        + render_per_task_rollouts(run)
        + '</section>'
    )

    parts.append(
        '<section><h2>Diff: initial &rarr; best</h2>'
        + render_diff(run.get("initial_skill"), run.get("best_skill"))
        + '</section>'
    )

    footer = render_footer_links(run)
    if footer:
        parts.append(f'<section><h2>Artefacts</h2>{footer}</section>')

    return "".join(parts)


def render_full_document(title: str, body: str) -> str:
    return (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        f'<title>{esc(title)}</title>\n'
        f'<style>{CSS}</style>\n'
        '</head>\n<body>\n'
        f"{body}\n"
        "</body>\n</html>\n"
    )


# --------------------------------------------------------------------------- #
# CLI                                                                         #
# --------------------------------------------------------------------------- #

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Render an HTML viewer for one or two SkillOpt run output dirs"
    )
    p.add_argument(
        "run_dirs",
        nargs="+",
        type=Path,
        help="One or two output-dirs from optimize_skill.py",
    )
    p.add_argument(
        "--output", "-o",
        type=Path,
        default=None,
        help="Output HTML path (default: <run-dir>/report.html for single, "
             "cwd/skillopt_compare.html for compare)",
    )
    p.add_argument(
        "--no-open",
        action="store_true",
        help="Do not try to open the report in a browser",
    )
    p.add_argument(
        "--static",
        action="store_true",
        default=True,
        help="Generate a fully static self-contained HTML page (default)",
    )
    p.add_argument(
        "--compare",
        action="store_true",
        help="Render two run dirs side-by-side",
    )
    return p


def main() -> int:
    args = build_parser().parse_args()

    if args.compare and len(args.run_dirs) != 2:
        log("Error: --compare requires exactly two run directories")
        return 1
    if not args.compare and len(args.run_dirs) > 1:
        log("Note: multiple run dirs given without --compare; using the first one")
        args.run_dirs = args.run_dirs[:1]

    runs = [load_run(p.resolve()) for p in args.run_dirs]

    if args.compare:
        title = f"SkillOpt compare: {runs[0]['name']} vs {runs[1]['name']}"
        body_parts = [f'<h1>{esc(title)}</h1>', '<div class="compare-grid">']
        for run in runs:
            body_parts.append('<div class="compare-column">')
            body_parts.append(render_run_page(run, single=False))
            body_parts.append('</div>')
        body_parts.append('</div>')
        body = "".join(body_parts)
        if args.output is not None:
            output_path = args.output.resolve()
        else:
            output_path = Path.cwd() / "skillopt_compare.html"
    else:
        run = runs[0]
        title = f"SkillOpt run: {run.get('skill_name') or run['name']}"
        body = render_run_page(run, single=True)
        if args.output is not None:
            output_path = args.output.resolve()
        else:
            output_path = run["path"] / "report.html" if run["exists"] \
                else Path.cwd() / "report.html"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    document = render_full_document(title, body)
    output_path.write_text(document, encoding="utf-8")
    log(f"Wrote {output_path}")

    if not args.no_open:
        try:
            webbrowser.open(output_path.as_uri())
        except Exception as exc:  # noqa: BLE001
            log(f"Could not open browser: {exc}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
