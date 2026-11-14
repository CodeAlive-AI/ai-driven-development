---
name: skills-management
description: Search, find, discover, install, remove, update, review, deduplicate, list, move, optimise, and iterate on skills for AI coding agents. Use when user asks "find a skill for X", "install skill", "remove skill", "update skills", "list skills", "deduplicate skills", "why are two skills shown", "choose the canonical skill", "check for skill conflicts", "review skill quality", "move skill", "check for updates", "optimise skill", "audit skill edits", "trigger test skill", or "transfer skill across agents". Includes duplicate-free installation preflight and SkillOpt-style training loops. Do not use for creating skills from scratch (use /skill-creator instead).
---

# Skills Manager

## Running the scripts

Run every script with `uv run scripts/<script>.py …` from this skill's directory (all paths
below are relative to it). Each script declares `requires-python >= 3.11` in a PEP 723 header,
so uv picks a matching interpreter even when `python3` on PATH is an old system Python, as on
macOS (3.9) and in sandboxed shells. Without uv, use any Python 3.11+ (`python3.13 scripts/…`).
On an older interpreter a script exits with the exact `uv run` command to use instead.

## Quick Reference

| Task | Command |
|------|---------|
| **Local skills (Claude Code scopes unless `--agent` is given)** | |
| List / by scope / JSON | `uv run scripts/list_skills.py` · `-s user` · `-s project` · `-f json` |
| Show details | `uv run scripts/show_skill.py <name>` (`--files`, `-f json`) |
| Review against best practices | `uv run scripts/review_skill.py <name>` (`-f json`) |
| Delete | `uv run scripts/delete_skill.py <name>` (`-s project`, `-a cursor`, `--all-agents`, `--force`) |
| Move between scopes | `uv run scripts/move_skill.py <name> user\|project` (`-f` to overwrite) |
| Audit duplicate names | `uv run scripts/audit_skill_duplicates.py` |
| Preflight an install | `uv run scripts/audit_skill_duplicates.py --candidate /path/to/skill --fail-on-conflict` |
| Create new | Use `/skill-creator` |
| **Multi-agent** | |
| Detect agents / print registry | `uv run scripts/detect_agents.py` (`--all`, `-f json`) |
| List an agent's skills | `uv run scripts/list_agent_skills.py --agent cursor` (`--all`, `-s global`, `-f json`) |
| Install to agents | `uv run scripts/install_skill.py /path --agent cursor` (repeat `--agent`, or `--all`; `-s global`, `--link`, `--force`) |
| Copy between agents | `uv run scripts/copy_skill.py <name> --from claude-code --to cursor` (`--from-scope`, `--to-scope`, `--force`) |
| Move between agents | `uv run scripts/move_skill_agent.py <name> --from claude-code --to cursor` (`--force`) |
| **Ecosystem ([Skills CLI](https://github.com/vercel-labs/add-skill), [skills.sh](https://skills.sh))** | |
| Find | `npx skills find [query]` |
| List installed | `npx skills list` (`-g`, `-a cursor`) |
| Install from GitHub | `npx skills add <owner/repo@skill> -g -y` (after the preflight) |
| Remove | `npx skills remove <name> -g -y` (`-a cursor`, `--all`) |
| Update all | `npx skills update` |
| Review remote skills | Fetch skills.sh pages and assess with [remote-skill-assessment.md](references/remote-skill-assessment.md) |
| **Optimise (SkillOpt-style)** | |
| Plan / run | `uv run scripts/optimize_skill.py <name> --tasks tasks.jsonl --dry-run` · `--output-dir runs/r1` |
| Trigger / transfer tests | `uv run scripts/trigger_test.py <name> --cases cases.yaml` · `uv run scripts/transfer_test.py <name> --all` |
| Aggregate / compare runs | `uv run scripts/aggregate_runs.py runs/*` · `runs/r1 runs/r2 --compare` |
| Blind A/B, HTML viewer, edit log, diffs | See [skill-optimization.md § Tooling](references/skill-optimization.md#tooling) |

## Scopes and duplicate invariant

Skill discovery is consumer-specific. Codex uses `$HOME/.agents/skills` for user skills,
scans `.agents/skills` from CWD to repo root, and follows symlinks. Other agents use the
paths in `scripts/agents.py` (print them with `detect_agents.py --all` rather than copying
them into instructions); plugins add a separately managed namespaced layer.

Maintain one active implementation of a frontmatter `name` per consumer topology. Aliases
to one real directory are not independent copies; identical agent-specific replicas may be
necessary, but divergent global/repo/plugin copies require a canonical-source decision.
Read [skill-deduplication.md](references/skill-deduplication.md) before installing,
deduplicating, migrating, or resolving plugin-vs-standalone conflicts.

## Changing installed skills safely

- **Confirm with the user before deleting or removing** anything ("Delete the skill
  '[name]'? This cannot be undone." — `AskUserQuestion` in Claude Code). Then pass
  `--force`: without a terminal the scripts refuse instead of prompting.
- **Without `--agent`, `list`, `show`, `move` and `delete` touch Claude Code scopes only.**
  Use `--agent`, `--all-agents` or `list_agent_skills.py` for other agents.
- **Symlinks are entries of their own.** `delete_skill.py` refuses to delete a real directory
  that other agents' symlinks point at and prints the next command; `--all-agents` removes the
  directory and every link to it (links first). Moving a symlink keeps it a symlink to the same
  real directory.
- **Shared directories affect every reader.** Several agents read one directory (for example
  `~/.agents/skills`); deleting or moving there removes the skill for all of them, and the
  scripts name the agents affected.
- **Replacement is staged.** `install`, `copy`, `move` and `move_skill_agent` replace an
  existing target only after the new copy or link is complete, so a failure keeps the old one.
- For ecosystem-installed skills prefer `npx skills remove <name> -g -y`; use
  `delete_skill.py --all-agents` for manual cleanup.

To modify a skill, locate it with `show_skill.py <name>` and edit its `SKILL.md` in place.

## Review a skill

`review_skill.py` checks name format and directory match, description quality (triggers,
negative triggers, third person, specificity), XML angle brackets in frontmatter, forbidden
doc files, body length, token footprint (300–2000 tokens target; warns at 2000, penalises at
4000), procedurality, patch-friendliness (heading and `**Label:**` anchors), balanced
`<!-- SLOW_UPDATE_START/END -->` markers, time-sensitive content, path format, reference depth
and tables of contents. After reviewing, read the skill's `SKILL.md` and apply the fixes.

## Install from the ecosystem

**Mandatory preflight:** determine the candidate frontmatter `name` and run the duplicate
auditor before installation. If the name exists, update or reuse the canonical copy instead.
For intentional cross-agent replicas, document the need and use
`install_skill.py --allow-duplicate-name` only after review.

For a locally maintained canonical source, prefer `install_skill.py --link`: every agent sees
the same real directory and edits cannot make copies drift. Copy only when the consumer cannot
follow symlinks or deliberately needs an isolated snapshot.

Treat `npx skills check` as potentially mutating: some CLI versions update during `check`, and
`check --help` may enter the same workflow. For a read-only freshness comparison use repository
HEAD, manager lock metadata and installed hashes. After any managed update, rerun the duplicate
audit, because stale lock entries can recreate removed copies.

## Find and assess ecosystem skills

Search with `npx skills find <keywords>` when the user asks how to do a common task, asks for
a skill for X, or wants specialised capabilities. After presenting results, offer to review the
top candidates before installing, especially with 3+ results, similar names, overlapping
descriptions or suspicious metrics (a niche topic with very high installs). If the user agrees:
fetch `https://skills.sh/<owner>/<repo>/<skill>` for the top 3–6, weigh installs, agent
distribution, age, description, relevance and overlap with installed skills, and present a
ranked summary with a verdict (Recommended / Consider / Skip) and a 1–2 sentence assessment.
Red flags and scoring signals: [remote-skill-assessment.md](references/remote-skill-assessment.md).
If nothing fits, offer to help directly or suggest `npx skills init <name>`.

## Optimise a skill (SkillOpt-style)

Treat a skill as a trainable text artefact: bounded edits, a held-out validation gate, a
rejected-edit buffer and an epoch-wise slow update (Microsoft, arXiv 2605.23904, May 2026).

- **Use it when** the skill exists and underperforms on a measurable task set, you have a
  verifier (exact match, scored output or LLM judge), and you can write 20–100 tasks with
  reference answers.
- **Do not use it** without a measurable success signal, for a skill that does not exist yet
  (write v0 with `/skill-creator`), or with only 1–5 tasks.

```bash
uv run scripts/optimize_skill.py <name> --tasks tasks.jsonl --epochs 4 --edit-budget 4 \
    --output-dir runs/r1 --dry-run          # plan: splits, schedule, prompt previews
uv run scripts/optimize_skill.py <name> --tasks tasks.jsonl --output-dir runs/r1 \
    --optimizer-cmd "claude -p --model opus" \
    --target-cmd "claude -p --model sonnet"
cat runs/r1/optimization_report.md
```

The loop writes `best_skill.md`, `optimization_report.md`, `edit_apply_report.json`,
`rejected_buffer.json` and `meta_skill.json` (optimiser-side only, not shipped). Method,
hyperparameters, failure modes and the tooling for assertion grading, multi-run variance,
blind A/B comparison, the HTML viewer, manual-edit logs and trigger/transfer tests:
[skill-optimization.md](references/skill-optimization.md). Audit a finished run with
[optimization-grading-checklist.md](references/optimization-grading-checklist.md).

## Important notes

- **Restart for new top-level dirs**: a top-level `skills/` directory created after the session
  started needs a Claude Code restart before it is watched.
- **Live change detection (Claude Code, 2026)**: adding, editing or removing a skill under
  `~/.claude/skills/`, project `.claude/skills/`, or `.claude/skills/` inside an `--add-dir`
  directory takes effect in the current session.
- **Agent detection** uses config-directory presence.
- **Install once per discovery topology**: prefer one shared canonical root or symlink; create
  agent-specific replicas only for consumers that cannot read it, and audit after replicating.
- **Commands are skills (Claude Code, 2026)**: `.claude/commands/deploy.md` and
  `.claude/skills/deploy/SKILL.md` both create `/deploy`; skills add supporting files,
  frontmatter and auto-invocation.
- **Plugin skills are namespaced** as `plugin-name:skill-name` and cannot conflict with user or
  project skills.
- **OpenCode** also loads `.claude/skills/` and `.agents/skills/` (project and global), so one
  Anthropic-format skill works across Claude Code, Codex and OpenCode. Paths, permissions and
  frontmatter: [opencode-skills.md](references/opencode-skills.md).

## References

Consult these when reviewing skills or advising on structure and best practices.

| File | Description |
|------|-------------|
| `references/01-introduction.md` … `07-resources-and-references.md` | The Complete Guide to Building Skills for Claude: fundamentals, planning and design, testing, distribution, patterns and troubleshooting, resources |
| `references/ref-a-quick-checklist.md` | Pre-build, development, upload and post-upload checklists |
| `references/ref-b-yaml-frontmatter.md` | Required/optional fields, security restrictions |
| `references/ref-c-complete-skill-examples.md` | Links to production-ready skill examples |
| `references/remote-skill-assessment.md` | Evaluating ecosystem skills before installation |
| `references/skill-deduplication.md` | Canonical-source selection, duplicate classification, plugin handling, install preflight, verification |
| `references/opencode-skills.md` | OpenCode discovery paths, frontmatter, permissions |
| `references/skill-optimization.md` | SkillOpt method and the optimisation tooling |
| `references/optimization-artifacts-schemas.md` | JSON schemas for every artefact written by `optimize_skill.py` and `log_skill_edit.py` |
| `references/optimization-grading-checklist.md` | What to inspect in a finished run before shipping |
| `prompts/*.md` | Optimiser contracts: analyst, merge, ranking, slow update, meta skill, grader, blind comparator |

## Acknowledgments

Multi-agent support is based on the [Skills CLI](https://github.com/vercel-labs/add-skill)
(`npx skills`) by Vercel Labs. Browse the open agent skills ecosystem at [skills.sh](https://skills.sh).
