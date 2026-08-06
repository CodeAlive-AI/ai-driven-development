# Repo Activity Summary

Gives AI coding agents a fast answer to "what's been happening in this repo" — without reading every file.

One script, one `git log` call: no API keys, no network, no dependencies beyond Python 3.9+ and git.

Adapted from a git-signal-extraction tool I built independently.

## What you get

A structured report covering:

- **Technologies** in use (languages, frameworks, tooling)
- **Work type breakdown** (feature / bugfix / refactor / docs / infra)
- **Churn hotspots** — which files and directories change the most
- **Contributor patterns** — who's working on what
- **Velocity** — commits/week, active days, average commit size
- **Project health** — tests, CI, docs, last activity date

## Quick start

```bash
python3 scripts/activity_summary.py --repo-dir . --days 90
```

Supports `--format json` for machine-readable output, `--author "name"` to scope to one contributor, and `--format text` for a compact one-liner summary.

## How it complements `investigating-repository-history`

That skill answers "why does this specific code exist" at the file/symbol level. This one answers "what has the whole repo been doing" — useful for onboarding, maintenance triage, or understanding a codebase before diving in.

## Install

```bash
npx skills add CodeAlive-AI/ai-driven-development --skill repo-activity-summary
```

## File structure

```text
repo-activity-summary/
├── SKILL.md                        ← agent-facing contract
├── README.md                       ← this file
└── scripts/
    └── activity_summary.py         ← analysis engine (Python 3.9+, stdlib only)
```

## License

MIT
