# Repo Activity Summary

Gives AI coding agents a fast answer to "what's been happening in this repo" — without reading every file.

One script, one `git log` call: no API keys, no network, no dependencies beyond Python 3.9+ and git.

Originally derived from an independent git-signal-extraction tool; maintained here as a stdlib-only Agent Skill.

## What you get

A structured report covering:

- **Technologies** in use (languages, frameworks, tooling) — path heuristics
- **Work type breakdown** (feature / bugfix / refactor / docs / infra / release / …) — keyword heuristics, with subject samples when classification is unreliable
- **Churn hotspots** — which files and directories change the most (lockfiles excluded)
- **Contributor patterns** — who's working on what
- **Velocity** — commits/week, active days, average commit size (same noise filter)
- **Project health** — test modules, CI, docs, last activity date

## Quick start

```bash
python3 scripts/activity_summary.py --repo-dir . --days 90
```

Useful flags:

| Flag | Description |
|------|-------------|
| `--format json` | Machine-readable output |
| `--author "name"` | Scope to one contributor |
| `--format text` | Compact one-liner summary |
| `--classify-threshold 0.25` | Mark work-type labels unreliable above this unclassified share |
| `--max-unclassified-samples 40` | Cap on unclassified subjects in the report |
| `--raw-subjects` | Emit every filtered commit subject (sha + date + message) |
| `--branch main` | Analyze a specific branch / revision |
| `--output report.md` | Write UTF-8 report to a file |

## Measured benefit

The skill was benchmarked against the same agent answering the same question *without* it —
identical prompt, identical clone of [`simonw/llm`](https://github.com/simonw/llm)
(186 commits / 8 contributors / 90 days), Grok 4.5 in both arms, token and cost figures taken
from the backend's own `usage` events:

| | Without the skill | With the skill | Δ |
|---|---:|---:|---:|
| **Cost** | $0.3004 | **$0.1748** | **−42%** |
| Total tokens | 240,251 | 190,694 | −21% |
| Input tokens | 96,497 | 45,901 | −52% |
| Output tokens | 11,274 | 6,937 | −39% |
| Reasoning tokens | 7,975 | 2,291 | −71% |
| Wall clock | 169 s | 106 s | −37% |

**Report quality was a tie.** Both arms matched a hand-computed ground truth on every
mechanical figure (churn ranking, active days, commits/week, line totals, test-module count).
The unassisted agent produced a somewhat broader report; the skill-assisted one was more
compact. The saving comes from not re-deriving a methodology on every run — hence the 71% drop
in reasoning tokens.

**What the skill does buy is reproducibility of the mechanical half.** Across three runs the
unassisted agent's work-type split swung from 43.5% / 23.1% / 42.5% `feature` and
3.8% / 18.3% / 5.9% `refactor`, while churn, velocity, and contributor counts stayed identical
in every skill-assisted run. Interpretation varies either way — which is why the script flags
low-confidence classification instead of asserting it (see below).

Caveats: cost is a single paired measurement on a single mid-size repository. Treat −42% as an
order of magnitude, not a guarantee, and expect it to move with repo size and commit-message style.

## Design note: facts here, interpretation in the agent

The keyword classifier is deliberately not trusted. When more than `--classify-threshold` of
commits land in `other` (25% by default), the report says so in plain text and emits the
unclassified subjects so the calling agent can classify them from the messages themselves.
On `simonw/llm` that path triggers at 56% — the agent reclassifies and the final report is
correct, whereas asserting the keyword guess would have shipped `Other: 56%` as the headline
finding. Technology labels carry the same caveat: they are path heuristics, not an import graph.

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
├── scripts/
│   └── activity_summary.py         ← analysis engine (Python 3.9+, stdlib only)
└── tests/
    └── test_activity_summary.py    ← unittest regression suite
```

## Tests

```bash
python3 -m unittest discover -s skills/repo-activity-summary/tests -v
```

## License

MIT
