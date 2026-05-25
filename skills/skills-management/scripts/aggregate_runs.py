#!/usr/bin/env python3
"""Aggregate one or more SkillOpt optimisation runs into a comparable summary.

Reads the artefacts written by `optimize_skill.py` and surfaces the metrics
that matter when deciding whether to ship `best_skill.md`. Robust to partial
runs — incomplete output dirs are listed but excluded from aggregate stats.

See `../references/optimization-artifacts-schemas.md` for the artefact
contract this script reads.
"""

import argparse
import glob
import json
import math
import re
import sys
from pathlib import Path


# --------------------------------------------------------------------------- #
# Helpers                                                                     #
# --------------------------------------------------------------------------- #

def log(msg: str) -> None:
    """Log to stderr so stdout stays clean for piping."""
    print(msg, file=sys.stderr, flush=True)


def approx_tokens(text: str) -> int:
    """Approximate token count (~4 chars/token)."""
    return len(text) // 4


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def safe_read_text(path: Path) -> str | None:
    if not path.exists():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def sample_stddev(values: list[float]) -> float:
    n = len(values)
    if n < 2:
        return 0.0
    mean = sum(values) / n
    var = sum((x - mean) ** 2 for x in values) / (n - 1)
    return math.sqrt(var)


def stat_block(values: list[float]) -> dict:
    if not values:
        return {"mean": 0.0, "stddev": 0.0, "min": 0.0, "max": 0.0, "n": 0}
    return {
        "mean": round(sum(values) / len(values), 4),
        "stddev": round(sample_stddev(values), 4),
        "min": round(min(values), 4),
        "max": round(max(values), 4),
        "n": len(values),
    }


# --------------------------------------------------------------------------- #
# Report-frontmatter parsing                                                  #
# --------------------------------------------------------------------------- #

REPORT_KEYS = {
    "Baseline selection score": "baseline_score",
    "Best selection score": "best_score",
    "Final test score": "test_score",
    "Steps recorded": "steps_recorded",
    "Accepted edits": "accepted_edits_reported",
    "Rejected proposals (last epoch buffer)": "rejected_last_epoch",
    "Approx tokens (rough)": "approx_tokens",
}


def parse_report_summary(text: str) -> dict:
    """Extract the Summary bullet list from optimization_report.md."""
    out: dict = {}
    # The Summary section is "## Summary\n- Key: value\n..." until the next "##".
    match = re.search(r"##\s*Summary\s*\n(.*?)(?:\n##\s|\Z)", text, re.DOTALL)
    if not match:
        return out
    body = match.group(1)
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue
        line = line.lstrip("- ").strip()
        if ":" not in line:
            continue
        key, raw_val = line.split(":", 1)
        key = key.strip()
        raw_val = raw_val.strip()
        if key not in REPORT_KEYS:
            continue
        mapped = REPORT_KEYS[key]
        # Numeric coercion.
        if raw_val in ("n/a", "None", ""):
            out[mapped] = None
            continue
        try:
            if "." in raw_val:
                out[mapped] = float(raw_val)
            else:
                out[mapped] = int(raw_val)
        except ValueError:
            out[mapped] = raw_val
    return out


# --------------------------------------------------------------------------- #
# Per-run loader                                                              #
# --------------------------------------------------------------------------- #

def load_run(run_dir: Path) -> dict:
    """Load one optimisation run's summary. Marks `status=incomplete` if
    the run never reached the final test evaluation.
    """
    record: dict = {
        "path": str(run_dir),
        "name": run_dir.name,
        "status": "ok",
        "warnings": [],
    }

    if not run_dir.exists():
        record["status"] = "missing"
        record["warnings"].append(f"directory does not exist: {run_dir}")
        return record

    # Splits.
    splits_path = run_dir / "splits.json"
    if splits_path.exists():
        try:
            splits = read_json(splits_path)
            record["splits"] = {
                "train": len(splits.get("train", [])),
                "selection": len(splits.get("selection", [])),
                "test": len(splits.get("test", [])),
                "seed": splits.get("seed"),
            }
        except (json.JSONDecodeError, OSError) as exc:
            record["warnings"].append(f"splits.json unreadable: {exc}")

    # State.
    state_path = run_dir / "state.json"
    if state_path.exists():
        try:
            state = read_json(state_path)
            record["epoch_reached"] = state.get("epoch")
            record["current_score"] = state.get("current_score")
            record["best_score_selection"] = state.get("best_score")
        except (json.JSONDecodeError, OSError) as exc:
            record["warnings"].append(f"state.json unreadable: {exc}")

    # Test rollouts.
    test_path = run_dir / "test_rollouts.jsonl"
    if test_path.exists():
        rows = read_jsonl(test_path)
        scores = [r.get("score", 0) for r in rows if isinstance(r.get("score"), int)]
        record["test_n"] = len(scores)
        record["test_score"] = round(sum(scores) / len(scores), 4) if scores else None
    else:
        record["test_n"] = 0
        record["test_score"] = None
        record["status"] = "incomplete"
        record["warnings"].append("no test_rollouts.jsonl — run did not reach final test")

    # Accepted edits.
    accepted_path = run_dir / "edit_apply_report.json"
    accepted: list[dict] = []
    if accepted_path.exists():
        try:
            accepted = read_json(accepted_path) or []
        except (json.JSONDecodeError, OSError) as exc:
            record["warnings"].append(f"edit_apply_report.json unreadable: {exc}")
    record["accepted_edits"] = len(accepted)
    record["accepted_edits_total_ops"] = sum(len(e.get("edits", [])) for e in accepted)

    # Rejected buffer (last-epoch snapshot only — earlier epochs were cleared).
    rejected_path = run_dir / "rejected_buffer.json"
    if rejected_path.exists():
        try:
            rejected = read_json(rejected_path) or []
            record["rejected_edits_last_epoch"] = len(rejected)
        except (json.JSONDecodeError, OSError) as exc:
            record["warnings"].append(f"rejected_buffer.json unreadable: {exc}")
            record["rejected_edits_last_epoch"] = 0
    else:
        record["rejected_edits_last_epoch"] = 0

    # Skill tokens.
    initial_text = safe_read_text(run_dir / "initial_skill.md")
    best_text = safe_read_text(run_dir / "best_skill.md")
    current_text = safe_read_text(run_dir / "current_skill.md")
    if initial_text is not None:
        record["tokens_initial"] = approx_tokens(initial_text)
    if best_text is not None:
        record["tokens_best"] = approx_tokens(best_text)
    elif current_text is not None:
        record["tokens_best"] = approx_tokens(current_text)
    if "tokens_initial" in record and "tokens_best" in record:
        record["tokens_delta"] = record["tokens_best"] - record["tokens_initial"]

    # Report frontmatter takes priority for the headline numbers.
    report_text = safe_read_text(run_dir / "optimization_report.md")
    if report_text:
        report = parse_report_summary(report_text)
        if "baseline_score" in report and report["baseline_score"] is not None:
            record["baseline_score"] = report["baseline_score"]
        if "test_score" in report and report["test_score"] is not None:
            # Report value already trims to 3dp; prefer the jsonl-derived one
            # if both exist, but use the report when test_rollouts missing.
            if record.get("test_score") is None:
                record["test_score"] = report["test_score"]
        if "approx_tokens" in report:
            record["report_approx_tokens"] = report["approx_tokens"]

    # Meta-skill presence.
    meta_path = run_dir / "meta_skill.json"
    record["has_meta_skill"] = meta_path.exists()

    if record.get("baseline_score") is not None and record.get("test_score") is not None:
        record["test_delta_vs_baseline"] = round(
            record["test_score"] - record["baseline_score"], 4
        )

    return record


# --------------------------------------------------------------------------- #
# Aggregation                                                                 #
# --------------------------------------------------------------------------- #

def aggregate(records: list[dict]) -> dict:
    eligible = [r for r in records if r["status"] == "ok"]
    incomplete = [r for r in records if r["status"] != "ok"]

    test_scores = [r["test_score"] for r in eligible if r.get("test_score") is not None]
    accepted = [r["accepted_edits"] for r in eligible]
    rejected = [r["rejected_edits_last_epoch"] for r in eligible]
    tokens_initial = [r["tokens_initial"] for r in eligible if "tokens_initial" in r]
    tokens_best = [r["tokens_best"] for r in eligible if "tokens_best" in r]
    tokens_delta = [r["tokens_delta"] for r in eligible if "tokens_delta" in r]
    deltas_vs_baseline = [
        r["test_delta_vs_baseline"] for r in eligible if "test_delta_vs_baseline" in r
    ]
    positive_runs = sum(1 for d in deltas_vs_baseline if d > 0)

    return {
        "runs_total": len(records),
        "runs_eligible": len(eligible),
        "runs_incomplete": len(incomplete),
        "incomplete_paths": [r["path"] for r in incomplete],
        "test_score": stat_block(test_scores),
        "accepted_edits": {
            "total": sum(accepted),
            "per_run": accepted,
        },
        "rejected_edits_last_epoch": {
            "total": sum(rejected),
            "per_run": rejected,
        },
        "tokens_initial_mean": round(sum(tokens_initial) / len(tokens_initial), 1)
            if tokens_initial else None,
        "tokens_best_mean": round(sum(tokens_best) / len(tokens_best), 1)
            if tokens_best else None,
        "tokens_delta": stat_block([float(d) for d in tokens_delta]),
        "test_delta_vs_baseline": stat_block(deltas_vs_baseline),
        "runs_with_positive_delta": positive_runs,
        "epochs_completed": [r.get("epoch_reached") for r in records],
    }


# --------------------------------------------------------------------------- #
# Rendering                                                                   #
# --------------------------------------------------------------------------- #

def fmt_value(v) -> str:
    if v is None:
        return "n/a"
    if isinstance(v, float):
        return f"{v:.4f}"
    return str(v)


def render_text(records: list[dict], summary: dict) -> str:
    lines: list[str] = []
    lines.append(f"Runs scanned: {summary['runs_total']} "
                 f"(eligible: {summary['runs_eligible']}, "
                 f"incomplete: {summary['runs_incomplete']})")
    lines.append("")
    header = ["RUN", "STATUS", "EPOCH", "BASE", "BEST_SEL", "TEST", "DELTA", "ACC", "REJ", "TOK_INIT", "TOK_BEST"]
    rows = [header]
    for r in records:
        rows.append([
            r["name"],
            r["status"],
            fmt_value(r.get("epoch_reached")),
            fmt_value(r.get("baseline_score")),
            fmt_value(r.get("best_score_selection")),
            fmt_value(r.get("test_score")),
            fmt_value(r.get("test_delta_vs_baseline")),
            str(r.get("accepted_edits", 0)),
            str(r.get("rejected_edits_last_epoch", 0)),
            fmt_value(r.get("tokens_initial")),
            fmt_value(r.get("tokens_best")),
        ])
    widths = [max(len(row[i]) for row in rows) for i in range(len(header))]
    for i, row in enumerate(rows):
        lines.append("  ".join(row[j].ljust(widths[j]) for j in range(len(row))))
        if i == 0:
            lines.append("  ".join("-" * widths[j] for j in range(len(row))))

    lines.append("")
    lines.append("Aggregate (eligible runs only):")
    ts = summary["test_score"]
    lines.append(
        f"  test_score: mean={ts['mean']} stddev={ts['stddev']} "
        f"min={ts['min']} max={ts['max']} n={ts['n']}"
    )
    lines.append(
        f"  accepted_edits: total={summary['accepted_edits']['total']} "
        f"per_run={summary['accepted_edits']['per_run']}"
    )
    lines.append(
        f"  rejected_edits_last_epoch: total={summary['rejected_edits_last_epoch']['total']} "
        f"per_run={summary['rejected_edits_last_epoch']['per_run']}"
    )
    td = summary["tokens_delta"]
    lines.append(
        f"  tokens_delta: mean={td['mean']} stddev={td['stddev']} "
        f"min={td['min']} max={td['max']}"
    )
    db = summary["test_delta_vs_baseline"]
    lines.append(
        f"  test_delta_vs_baseline: mean={db['mean']} stddev={db['stddev']} "
        f"min={db['min']} max={db['max']}"
    )
    lines.append(
        f"  runs_with_positive_delta: {summary['runs_with_positive_delta']} / "
        f"{summary['runs_eligible']}"
    )
    if summary["incomplete_paths"]:
        lines.append("")
        lines.append("Incomplete runs (excluded from stats):")
        for p in summary["incomplete_paths"]:
            lines.append(f"  - {p}")
    return "\n".join(lines)


def render_compare(records: list[dict]) -> str:
    """Side-by-side: one column per run, one row per metric."""
    metrics = [
        ("status", "status"),
        ("epoch_reached", "epoch_reached"),
        ("baseline_score", "baseline_score"),
        ("best_score_selection", "best_score_sel"),
        ("test_score", "test_score"),
        ("test_delta_vs_baseline", "test_delta"),
        ("accepted_edits", "accepted_edits"),
        ("rejected_edits_last_epoch", "rejected_last_epoch"),
        ("tokens_initial", "tokens_initial"),
        ("tokens_best", "tokens_best"),
        ("tokens_delta", "tokens_delta"),
        ("has_meta_skill", "has_meta_skill"),
    ]
    header = ["METRIC"] + [r["name"] for r in records]
    rows = [header]
    for key, label in metrics:
        row = [label]
        for r in records:
            row.append(fmt_value(r.get(key)))
        rows.append(row)
    widths = [max(len(row[i]) for row in rows) for i in range(len(header))]
    lines = []
    for i, row in enumerate(rows):
        lines.append("  ".join(row[j].ljust(widths[j]) for j in range(len(row))))
        if i == 0:
            lines.append("  ".join("-" * widths[j] for j in range(len(row))))
    return "\n".join(lines)


def render_json(records: list[dict], summary: dict) -> str:
    return json.dumps({"runs": records, "summary": summary}, indent=2, ensure_ascii=False)


def render_markdown(records: list[dict], summary: dict) -> str:
    lines: list[str] = []
    lines.append("# SkillOpt Run Aggregation")
    lines.append("")
    lines.append(f"- Runs scanned: {summary['runs_total']}")
    lines.append(f"- Eligible (ok): {summary['runs_eligible']}")
    lines.append(f"- Incomplete: {summary['runs_incomplete']}")
    lines.append(f"- Runs with positive test delta vs baseline: "
                 f"{summary['runs_with_positive_delta']} / {summary['runs_eligible']}")
    lines.append("")
    lines.append("## Per-run summary")
    lines.append("")
    lines.append("| Run | Status | Epoch | Baseline | Best (sel) | Test | Delta | Accepted | Rejected | Tokens init | Tokens best |")
    lines.append("|-----|--------|-------|----------|------------|------|-------|----------|----------|-------------|-------------|")
    for r in records:
        lines.append(
            f"| {r['name']} | {r['status']} | {fmt_value(r.get('epoch_reached'))} | "
            f"{fmt_value(r.get('baseline_score'))} | {fmt_value(r.get('best_score_selection'))} | "
            f"{fmt_value(r.get('test_score'))} | {fmt_value(r.get('test_delta_vs_baseline'))} | "
            f"{r.get('accepted_edits', 0)} | {r.get('rejected_edits_last_epoch', 0)} | "
            f"{fmt_value(r.get('tokens_initial'))} | {fmt_value(r.get('tokens_best'))} |"
        )
    lines.append("")
    lines.append("## Aggregate (eligible runs only)")
    lines.append("")
    ts = summary["test_score"]
    lines.append(f"- test_score: mean={ts['mean']}, stddev={ts['stddev']}, "
                 f"min={ts['min']}, max={ts['max']}, n={ts['n']}")
    td = summary["tokens_delta"]
    lines.append(f"- tokens_delta: mean={td['mean']}, stddev={td['stddev']}, "
                 f"min={td['min']}, max={td['max']}")
    db = summary["test_delta_vs_baseline"]
    lines.append(f"- test_delta_vs_baseline: mean={db['mean']}, stddev={db['stddev']}, "
                 f"min={db['min']}, max={db['max']}")
    lines.append(f"- accepted_edits total: {summary['accepted_edits']['total']}")
    lines.append(f"- rejected_edits_last_epoch total: "
                 f"{summary['rejected_edits_last_epoch']['total']}")
    if summary["incomplete_paths"]:
        lines.append("")
        lines.append("## Incomplete runs")
        lines.append("")
        for p in summary["incomplete_paths"]:
            lines.append(f"- `{p}`")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# Path expansion                                                              #
# --------------------------------------------------------------------------- #

def expand_paths(raw_paths: list[str]) -> list[Path]:
    """Expand glob patterns and resolve to Paths. Preserves order, drops dupes."""
    seen: set[str] = set()
    out: list[Path] = []
    for raw in raw_paths:
        matches = sorted(glob.glob(raw)) if any(ch in raw for ch in "*?[") else [raw]
        if not matches:
            # Keep the literal so the user sees a missing-path warning.
            matches = [raw]
        for m in matches:
            p = Path(m).resolve()
            key = str(p)
            if key in seen:
                continue
            seen.add(key)
            out.append(p)
    return out


# --------------------------------------------------------------------------- #
# CLI                                                                         #
# --------------------------------------------------------------------------- #

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Aggregate SkillOpt optimisation runs into a single summary"
    )
    p.add_argument(
        "run_dirs",
        nargs="+",
        help="One or more output-dirs (from optimize_skill.py). Globs accepted, e.g. 'runs/*'.",
    )
    p.add_argument(
        "--format", "-f",
        choices=["text", "json", "md"],
        default="text",
        help="Output format (default: text)",
    )
    p.add_argument(
        "--compare",
        action="store_true",
        help="Render a side-by-side per-run comparison table instead of the summary",
    )
    p.add_argument(
        "--output", "-o",
        type=Path,
        help="Write output to this path (default: stdout)",
    )
    return p


def main() -> int:
    args = build_parser().parse_args()
    paths = expand_paths(args.run_dirs)
    if not paths:
        log("Error: no run directories matched")
        return 1

    records = [load_run(p) for p in paths]
    summary = aggregate(records)

    if args.compare:
        rendered = render_compare(records)
    elif args.format == "json":
        rendered = render_json(records, summary)
    elif args.format == "md":
        rendered = render_markdown(records, summary)
    else:
        rendered = render_text(records, summary)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + ("\n" if not rendered.endswith("\n") else ""),
                               encoding="utf-8")
        log(f"Wrote {args.output}")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
