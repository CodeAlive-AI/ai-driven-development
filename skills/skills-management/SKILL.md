---
name: skills-management
description: Search, find, discover, install, remove, update, review, deduplicate, list, move, optimise, and iterate on skills for AI coding and framework agents including Antigravity (App, IDE, CLI), Claude Code, Codex, Cursor, OpenCode, Mastra, and LangGraph / Deep Agents. Use when user asks "find a skill for X", "install skill", "remove skill", "update skills", "list skills", "deduplicate skills", "why are two skills shown", "choose the canonical skill", "check for skill conflicts", "review skill quality", "audit progressive disclosure", "agent experience (AX)", "move skill", "check for updates", "optimise skill", "audit skill edits", "trigger test skill", or "transfer skill across agents". Includes duplicate-free installation preflight and SkillOpt-style training loops. Do not use for creating skills from scratch (use /skill-creator instead).
---

# Skills Manager

## Running the scripts

Run every script with `uv run scripts/<script>.py …` from this skill's directory (all paths below are relative to it). Each script declares `requires-python >= 3.11` via PEP 723; without uv, use Python 3.11+.

## Quick Reference

| Task | Command |
|------|---------|
| **Inspect & review (`--agent` or `--path` for any agent; Claude Code by default)** | |
| List Claude Code / agent skills | `uv run scripts/list_skills.py` · `list_agent_skills.py --agent antigravity` (`--all`, `-f json`) |
| Show / review skill | `uv run scripts/show_skill.py` · `review_skill.py <name>` (`--agent antigravity`, `--path <dir>`, `-f json`) |
| Delete / move between scopes | `uv run scripts/delete_skill.py <name>` (`-a antigravity`, `--all-agents`, `--force`) · `move_skill.py <name> user\|project` |
| Audit duplicates / preflight | `uv run scripts/audit_skill_duplicates.py` · `--candidate /path/to/skill --fail-on-conflict` |
| Detect agents / install / copy / move | `uv run scripts/detect_agents.py --all` · `install_skill.py /path -a antigravity --link` · `copy_skill.py` · `move_skill_agent.py` |
| **Antigravity (App / IDE / CLI)** | |
| List / validate plugins | `agy plugin list --json` · `agy plugin validate --strict <dir\|zip\|github-url>` |
| Manage plugins / reload / migrate | `agy plugin install <target>` · `agy plugin import claude\|gemini` · `/plugin` · `/skills reload` · `/migrate-workflows` · `/migrate-agent-settings` |
| **Ecosystem ([Skills CLI](https://github.com/vercel-labs/skills), [skills.sh](https://skills.sh))** | |
| Find / preview / try / install | `npx skills find [q]` · `add <repo> --list` · `use <repo>@<skill>` · `add <repo@skill> -g -y` (after preflight) |
| List / remove / update / assess | `npx skills list` · `remove <name> -g -y` · `update` · assess top 3–6 via [remote-skill-assessment.md](references/remote-skill-assessment.md) |
| **Optimise (SkillOpt-style)** | |
| Plan / run / test / compare | `optimize_skill.py <name> --tasks t.jsonl --dry-run` (`--agent`, `--path`) · `trigger_test.py` (`--judge agy-cli\|claude-cli`) · `transfer_test.py` · `aggregate_runs.py` |

## Scopes and duplicate invariant

Discovery is consumer-specific. **Antigravity (App, IDE, CLI)** reads `~/.gemini/config/skills` globally (highest global priority), walks workspace `.agents/skills` (plus legacy `.agent/`, `_agents/`, `_agent/`) to the repo root, reads `skills.json`/`plugins.json`, loads enabled plugins under `~/.gemini/config/plugins/` and `.agents/plugins/`, and in `agy` also reads `~/.agents/skills`. Codex and OpenCode read `~/.agents/skills` and walk `.agents/skills` to the repo root. Print all agent paths with `detect_agents.py --all`.

Keep one active implementation per frontmatter `name` for each consumer topology. Aliases to one real directory are fine; divergent global, workspace, manifest, or plugin copies require a canonical-source decision via [skill-deduplication.md](references/skill-deduplication.md).

## Changing skills safely and reviewing quality

- **Confirm before deleting**, then pass `--force` (non-interactive shells refuse otherwise). `delete_skill.py --agent antigravity` leaves shared `~/.agents/skills` intact; `--all-agents` removes canonical dirs and all symlinks cleanly.
- **Staged atomic swaps**: `install`, `copy`, `move`, and `move_skill_agent` keep old targets on failure. For local sources prefer `install_skill.py --link`.
- **Mandatory install preflight**: run `audit_skill_duplicates.py --candidate /path/to/skill --fail-on-conflict` before installing. Treat `npx skills check` as potentially mutating; rerun duplicate audit after any managed update.
- **Review & AX audit**: `review_skill.py` checks `name` presence/match, trigger & negative-trigger `description`, XML safety, forbidden docs, 300–2000 token budget, procedurality, patch anchors, `SLOW_UPDATE` markers, TOCs, and progressive disclosure (broken local links, orphaned references, eager-load directives). For manual AX and CLI ergonomics checks, consult [agent-experience-and-progressive-disclosure.md](references/agent-experience-and-progressive-disclosure.md).
- **Optimise (SkillOpt-style)**: for underperforming skills with 20–100 measurable tasks, use `optimize_skill.py` with `agy -p --disable-slash-commands` or `claude -p`.

## Important notes

- **Antigravity App, IDE, and CLI share `~/.gemini/config/`**: never hand-edit `config.json`; manage plugins via `agy plugin`, `/plugin`, or `[<name>](customization://<dir>)` (keyed on install directory `<dir>`, not manifest `name`). Workspace manifests ignore paths outside the repo root, and `/builtin/` layers are read-only.
- **Claude Code**: live reload applies to existing `~/.claude/skills/`, `.claude/skills/`, and `--add-dir` `.claude/skills/`; new top-level `skills/` dirs need a restart.

## References

Read **only** the reference matching the current task:

| Read when… | Reference |
|---|---|
| Designing or auditing AX, progressive disclosure, context budgets, or bundled CLI ergonomics | [agent-experience-and-progressive-disclosure.md](references/agent-experience-and-progressive-disclosure.md) |
| Working with Antigravity App (2.0), IDE, CLI (`agy`), `skills.json`/`plugins.json`, or plugins | [antigravity-skills.md](references/antigravity-skills.md) |
| Authoring or adapting skills for Mastra workspaces or LangGraph / Deep Agents | [framework-agent-skills.md](references/framework-agent-skills.md) |
| Structuring a skill, picking a workflow pattern, publishing, or troubleshooting | [skill-design-and-troubleshooting.md](references/skill-design-and-troubleshooting.md) |
| Checking YAML frontmatter fields across agents, substitutions, or security rules | [ref-b-yaml-frontmatter.md](references/ref-b-yaml-frontmatter.md) |
| Targeting OpenCode discovery paths, permissions, or frontmatter compatibility | [opencode-skills.md](references/opencode-skills.md) |
| Resolving duplicate names, plugin-vs-standalone conflicts, or install preflight | [skill-deduplication.md](references/skill-deduplication.md) |
| Evaluating candidate ecosystem skills from `skills.sh` before installation | [remote-skill-assessment.md](references/remote-skill-assessment.md) |
| Running a SkillOpt loop, blind A/B comparison, HTML viewer, or edit-log diffs | [skill-optimization.md](references/skill-optimization.md) |
| Inspecting JSON schemas for `optimize_skill.py` or `log_skill_edit.py` outputs | [optimization-artifacts-schemas.md](references/optimization-artifacts-schemas.md) |
| Auditing a finished SkillOpt run before shipping `best_skill.md` | [optimization-grading-checklist.md](references/optimization-grading-checklist.md) |
| Migrating deprecated AGY workflows, pre-2.0 paths, `.claude/commands/`, or renamed CLIs | [legacy/migrations.md](references/legacy/migrations.md) |
