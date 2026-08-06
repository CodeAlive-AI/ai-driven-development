---
name: repo-activity-summary
description: Summarize a repository's recent engineering activity from git history — technologies, work types, churn hotspots, contributor patterns, and velocity. Use when asking "what has this repo been working on", "is this project active", "who contributes what", "where are the hotspots", or before onboarding onto an unfamiliar codebase.
license: MIT
compatibility: Any coding agent with shell access. Requires git and Python 3.9+. No API keys or network access needed.
allowed-tools: Bash(git:*), Bash(python3:*), Read
metadata:
  version: "1.1.0"
  methodology: "commit-signal-extraction"
---

# Repo Activity Summary

Answer "what's been happening in this repo" from local git history — no network, no tokens, no setup.

## Trigger conditions

Use this skill when the user asks:

- "What has this repo been working on recently?"
- "What technologies does this project use?"
- "Where are the high-churn files / hotspots?"
- "Who's contributing and what are they working on?"
- "Is this project actively maintained?"
- Before onboarding onto an unfamiliar codebase.

Do not use this skill for file-level blame or provenance — use `investigating-repository-history` for that.

## Quick start

```bash
python3 scripts/activity_summary.py --repo-dir . --days 90
```

| Flag | Default | Description |
|------|---------|-------------|
| `--repo-dir` | `.` | Path to the git repository |
| `--days` | `90` | Days of history to analyze |
| `--author` | *(all)* | Filter to one author |
| `--format` | `markdown` | `markdown`, `json`, or `text` |
| `--max-commits` | `500` | Cap for very active repos |
| `--branch` | *(current)* | Branch / revision to analyze (must not start with `-`) |
| `--output` / `-o` | *(stdout)* | Write the report to a file (UTF-8) |
| `--classify-threshold` | `0.25` | If the share of unclassified commits exceeds this fraction, mark work-type classification unreliable and emit subject samples |
| `--max-unclassified-samples` | `40` | Cap on unclassified commit subjects included in the report |
| `--raw-subjects` | *off* | Emit every filtered commit subject with sha and date for agent-side classification |
| `--version` | — | Print version (`1.1.0`) and exit |

## What it produces

A structured report with:

1. **Overview** — commit count, date range, contributors, lines added/deleted
2. **Technologies** — languages and frameworks inferred from file paths (heuristic)
3. **Work type breakdown** — feature / bugfix / refactor / docs / infra / release / … (keyword heuristic)
4. **Unclassified subjects** — when keyword classification is unreliable, the raw subjects so the agent can classify them
5. **Churn hotspots** — most frequently modified files and directories (lockfiles/generated paths excluded)
6. **Contributor patterns** — per-author commits, lines, and primary focus
7. **Velocity** — commits/week, active days, average commit size (same noise filter as churn)
8. **Project health** — test modules (by basename/path convention), CI, docs, recency

## How it works

1. Collects commits via `git log --numstat --no-renames` with an explicit UTC `--since` timestamp
2. Filters bots (GitHub-style `[bot]` names and known automation identities) and keeps the filtered count
3. Detects technologies from extensions, exact manifest filenames, and path segments — never bare path substrings; requires a manifest hit or at least two source files
4. Classifies work types with precompiled word-boundary regexes and scored multi-label tie-break; does **not** present a large "Other" bucket as a finding
5. Ranks files/directories by modification frequency
6. Aggregates per-author stats using the same classifier
7. Checks for test modules, CI config, documentation, and last activity date

## Agent guidance

- Prefer the **facts** in the report (counts, paths, subjects, dates) over the keyword labels.
- When `classification.unreliable` is true, or the unclassified share is high, **classify from the emitted subjects** (or re-run with `--raw-subjects`) instead of trusting the work-type percentages.
- Technology labels are path heuristics, not an import graph — verify against manifests when it matters.

## Limitations

- Shallow clones (`--depth 1`) limit the analysis window.
- **Technology detection is a heuristic** (extensions, manifests, path segments — not imports or lockfile graphs). Labels are hints.
- **Work-type classification is a keyword heuristic**, not ground truth. Conventional-commit prefixes classify well; free-form subjects often do not. When the unclassified share exceeds `--classify-threshold` (default 25%), the report says so and emits subjects for the agent to classify.
- Average commit size and churn exclude lockfiles and common generated/vendor paths; the report states this filter.
- Summarizes *activity*, not *code quality*.
