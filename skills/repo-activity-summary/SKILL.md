---
name: repo-activity-summary
description: Summarize a repository's recent engineering activity from git history — technologies, work types, churn hotspots, contributor patterns, and velocity. Use when asking "what has this repo been working on", "is this project active", "who contributes what", "where are the hotspots", or before onboarding onto an unfamiliar codebase.
license: MIT
compatibility: Any coding agent with shell access. Requires git and Python 3.9+. No API keys or network access needed.
allowed-tools: Bash(git:*) Bash(python3:*) Read
metadata:
  version: "1.0.0"
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
| `--branch` | *(current)* | Branch to analyze |

## What it produces

A structured report with:

1. **Overview** — commit count, date range, contributors, lines added/deleted
2. **Technologies** — languages and frameworks inferred from file paths
3. **Work type breakdown** — feature vs bugfix vs refactor vs docs vs infra
4. **Churn hotspots** — most frequently modified files and directories
5. **Contributor patterns** — per-author commits, lines, and primary focus
6. **Velocity** — commits/week, active days, average commit size
7. **Project health** — tests, CI, docs, recency

## How it works

1. Collects commits via `git log --numstat`
2. Filters noise — merge commits, bots (dependabot, renovate, etc.), trivial messages
3. Detects technologies from file extensions and config file names
4. Classifies work types from commit message keywords
5. Ranks files/directories by modification frequency
6. Aggregates per-author stats
7. Checks for tests, CI config, documentation, and last activity date

## Limitations

- Shallow clones (`--depth 1`) limit the analysis window.
- Technology detection is heuristic (file paths, not imports).
- Work type classification depends on commit message quality.
- Summarizes *activity*, not *code quality*.
