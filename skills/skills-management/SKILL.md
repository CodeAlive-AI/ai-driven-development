---
name: skills-management
description: Search, find, discover, install, remove, update, review, deduplicate, list, move, optimise, and iterate on skills for AI coding agents. Use when user asks "find a skill for X", "install skill", "remove skill", "update skills", "list skills", "deduplicate skills", "why are two skills shown", "choose the canonical skill", "check for skill conflicts", "review skill quality", "move skill", "check for updates", "optimise skill", "audit skill edits", "trigger test skill", or "transfer skill across agents". Includes duplicate-free installation preflight and SkillOpt-style training loops. Do not use for creating skills from scratch (use /skill-creator instead).
---

# Skills Manager

## Quick Reference

| Task | Command |
|------|---------|
| List all | `python3 scripts/list_skills.py` |
| List by scope | `python3 scripts/list_skills.py -s user` or `-s project` |
| Show details | `python3 scripts/show_skill.py <name>` |
| Review skill | `python3 scripts/review_skill.py <name>` |
| Delete | `python3 scripts/delete_skill.py <name>` |
| Delete from agents | `python3 scripts/delete_skill.py <name> --all-agents --force` |
| Move to user | `python3 scripts/move_skill.py <name> user` |
| Move to project | `python3 scripts/move_skill.py <name> project` |
| Audit duplicate names | `python3 scripts/audit_skill_duplicates.py` |
| Preflight install | `python3 scripts/audit_skill_duplicates.py --candidate /path/to/skill --fail-on-conflict` |
| Create new | Use `/skill-creator` |
| **Optimize & Iterate (SkillOpt-style)** | |
| Plan optimisation | `python3 scripts/optimize_skill.py <name> --tasks tasks.jsonl --dry-run` |
| Run optimisation | `python3 scripts/optimize_skill.py <name> --tasks tasks.jsonl --output-dir runs/r1` |
| Log a manual edit | `python3 scripts/log_skill_edit.py <name> --reason "..." --snapshot` |
| List recent edits | `python3 scripts/log_skill_edit.py <name> --list --since 7d` |
| Diff vs last snapshot | `python3 scripts/diff_skill_versions.py <name> --log --format stats` |
| Diff between commits | `python3 scripts/diff_skill_versions.py <name> --git HEAD~3 HEAD` |
| Trigger test | `python3 scripts/trigger_test.py <name> --cases cases.yaml` |
| Generate trigger cases | `python3 scripts/trigger_test.py <name> --generate > cases.yaml` |
| Transfer test | `python3 scripts/transfer_test.py <name> --all` |
| Aggregate runs | `python3 scripts/aggregate_runs.py runs/*` |
| Compare runs | `python3 scripts/aggregate_runs.py runs/r1 runs/r2 --compare` |
| Assertion-graded run | `python3 scripts/optimize_skill.py <name> --tasks tasks.jsonl --verifier assertions` |
| Multi-run variance | `python3 scripts/optimize_skill.py <name> --tasks tasks.jsonl --runs-per-task 3` |
| Blind A/B compare | `python3 scripts/blind_comparator.py --skill-a runs/r1/initial_skill.md --skill-b runs/r1/best_skill.md --tasks tasks.jsonl --output-dir cmp/` |
| HTML viewer | `python3 scripts/eval_viewer.py runs/r1` |
| Compare two runs (HTML) | `python3 scripts/eval_viewer.py runs/r1 runs/r2 --compare` |
| **Discovery & Install** | |
| Find skills | `npx skills find [query]` |
| Review remote skills | Fetch skills.sh pages, assess using [assessment framework](references/remote-skill-assessment.md) |
| List ecosystem skills | `npx skills list` or `npx skills ls` |
| Install from GitHub | `npx skills add <owner/repo@skill> -g -y` |
| Remove ecosystem skill | `npx skills remove <name> -g -y` or `npx skills rm` |
| Inspect installed versions | Read lock metadata and upstream state; do not assume `npx skills check` is read-only |
| Update all | `npx skills update` |
| Browse online | [skills.sh](https://skills.sh) |
| **Multi-Agent** | |
| Detect agents | `python3 scripts/detect_agents.py` |
| List agent skills | `python3 scripts/list_agent_skills.py --agent cursor` |
| Install to agent | `python3 scripts/install_skill.py /path --agent cursor` |
| Copy between agents | `python3 scripts/copy_skill.py <name> --from claude-code --to cursor` |
| Move between agents | `python3 scripts/move_skill_agent.py <name> --from claude-code --to cursor` |

## Scopes and duplicate invariant

Skill discovery is consumer-specific. Codex uses `$HOME/.agents/skills` for user skills,
scans `.agents/skills` from CWD to repo root, and follows symlinks. Other agents use the
paths in `scripts/agents.py`; plugins add a separately managed namespaced layer.

Maintain one active implementation of a frontmatter `name` per consumer topology. Aliases
to one real directory are not independent copies; identical agent-specific replicas may be
necessary, but divergent global/repo/plugin copies require a canonical-source decision.
Read [skill-deduplication.md](references/skill-deduplication.md) before installing,
deduplicating, migrating, or resolving plugin-vs-standalone conflicts.

## Operations

### List Skills

```bash
python3 scripts/list_skills.py              # All skills
python3 scripts/list_skills.py -s user      # User scope only
python3 scripts/list_skills.py -f json      # JSON output
```

### Show Skill Details

```bash
python3 scripts/show_skill.py <name>           # Basic info
python3 scripts/show_skill.py <name> --files   # Include file listing
python3 scripts/show_skill.py <name> -f json   # JSON output
```

### Review Skill

Audits a skill against best practices and suggests improvements:

```bash
python3 scripts/review_skill.py <name>         # Review with text output
python3 scripts/review_skill.py <name> -f json # JSON output for programmatic use
```

**Checks performed:**
- Name format (lowercase, hyphens, max 64 chars, gerund form)
- Name matches directory name
- Description quality (triggers, negative triggers, third person, specificity)
- XML angle brackets in frontmatter (security)
- Forbidden docs files (README.md, CHANGELOG.md)
- Body length (warns if >500 lines)
- **Token footprint** (300-2000 tokens target per SkillOpt; warns at 2000, penalises at 4000)
- **Procedurality** (instance-specific markers — filenames, literal numbers, task references — should be rare)
- **Patch-friendliness** (anchor density: `##`/`###` headings + `**Label:**` markers needed for reliable `insert_after` edits)
- **Slow-update section integrity** (`<!-- SLOW_UPDATE_START -->` / `<!-- SLOW_UPDATE_END -->` markers must be balanced and unnested)
- Time-sensitive content
- Path format (no Windows backslashes)
- Reference depth (should be one level)
- Table of contents for long files

**After reviewing:** Read the skill's SKILL.md and apply the suggested fixes directly.

### Delete Skill

**CRITICAL**: Always use `AskUserQuestion` to confirm before deleting: "Are you sure you want to delete the skill '[name]'? This cannot be undone."

```bash
python3 scripts/delete_skill.py <name>              # Claude Code only, with confirmation
python3 scripts/delete_skill.py <name> --force      # Skip confirmation prompt
python3 scripts/delete_skill.py <name> -s project   # Target specific scope
python3 scripts/delete_skill.py <name> -a cursor    # Delete from specific agent
python3 scripts/delete_skill.py <name> --all-agents --force  # Delete from all agents
```

**Multi-agent deletion:** Skills installed via `npx skills add` may exist in multiple agent directories. The default mode (no flags) deletes from Claude Code only and warns if copies remain in other agents. Use `--all-agents` to delete from every detected agent at once.

For ecosystem-installed skills, prefer `npx skills remove <name> -g -y` first. Use `delete_skill.py --all-agents` as fallback for manual cleanup.

### Move Skill

```bash
python3 scripts/move_skill.py <name> user      # Project → User (personal)
python3 scripts/move_skill.py <name> project   # User → Project (share with team)
python3 scripts/move_skill.py <name> user -f   # Overwrite if exists
```

### Modify Skill

1. Run `python3 scripts/show_skill.py <name>` to locate it
2. Edit SKILL.md directly at the returned path

### Create New Skill

Use the `/skill-creator` skill for guided creation with proper structure.

## Optimize a Skill (SkillOpt-style)

Treat a skill as a **trainable text artefact**: bounded edits + held-out validation gate + rejected-edit buffer + epoch-wise slow update. See [references/skill-optimization.md](references/skill-optimization.md) for the full method (Microsoft, arXiv 2605.23904, May 2026).

**When to use this loop:**
- Skill already exists and underperforms on a measurable task set
- You have (or can write) a verifier — exact-match, scored output, or LLM judge
- You can produce 20-100 representative tasks with reference answers

**When NOT to use:**
- Task has no measurable success signal — bounded text optimisation needs a gate
- Creating a skill from scratch — write a v0 with `/skill-creator` first
- Only 1-5 tasks available — the loop needs evidence batches

### Run the loop

```bash
# 1. Dry-run to see the plan (splits, schedule, prompt previews)
python3 scripts/optimize_skill.py <name> \
    --tasks tasks.jsonl --epochs 4 --edit-budget 4 \
    --output-dir runs/r1 --dry-run

# 2. Real run
python3 scripts/optimize_skill.py <name> \
    --tasks tasks.jsonl --output-dir runs/r1 \
    --optimizer-cmd "claude -p --model claude-opus-4-7" \
    --target-cmd  "claude -p --model claude-haiku-4-5-20251001"

# 3. Inspect
cat runs/r1/optimization_report.md
python3 scripts/diff_skill_versions.py <name> --files \
    runs/r1/initial_skill.md runs/r1/best_skill.md --format stats
```

The loop produces `best_skill.md`, `optimization_report.md`, `edit_apply_report.json`, `rejected_buffer.json`, and `meta_skill.json` (optimiser-side only — not shipped).

### Manual-edit audit trail

For edits made outside the loop (hand-tweaks, bug-fix follow-ups), keep a lightweight log:

```bash
# After saving an edit
python3 scripts/log_skill_edit.py <name> \
    --reason "tightened insert_after target" \
    --source from-bug --ref "issue #42" --snapshot

python3 scripts/log_skill_edit.py <name> --list --since 30d
python3 scripts/diff_skill_versions.py <name> --log
```

`--snapshot` saves a copy under `<skill>/.skill_snapshots/SKILL.<sha8>.md` so the diff helper can show actual content, not just hashes.

### Protected slow-update section

A skill that gets optimised iteratively should include a markup-fenced region for longitudinal guidance:

```markdown
<!-- SLOW_UPDATE_START -->
<!-- This block is managed by the epoch-boundary slow-update process.
     Step-level edits never modify it. -->
<!-- SLOW_UPDATE_END -->
```

`scripts/review_skill.py` flags unbalanced or nested markers. `scripts/optimize_skill.py` refuses to apply step-level edits that target content inside this region.

### Trigger and transfer tests

```bash
# Auto-generate candidate trigger cases from the skill's description
python3 scripts/trigger_test.py <name> --generate > cases.yaml
# Curate, then run
python3 scripts/trigger_test.py <name> --cases cases.yaml --threshold 0.8

# Verify skill lands and parses in other agents
python3 scripts/transfer_test.py <name> --all --scope global
```

### Rich grading: assertions verifier

Pass `--verifier assertions` to grade each rollout against declarative `assertions[]` from `tasks.jsonl`. The grader returns per-assertion pass/fail with evidence, extracted claims, AND a **critique of the assertions themselves** (`eval_feedback`) — a meta layer that flags weak or non-discriminating checks. `optimization_report.md` aggregates these into an "Assertion critique" section.

```json
// tasks.jsonl entry for --verifier assertions
{"id":"t1","prompt":"...","assertions":["The output is a valid JSON array","Each item has a name field"]}
```

### Variance: multi-run per task

Pass `--runs-per-task 3` to run each task N times. `rollouts.jsonl` records `score_mean` and `score_stddev`; validation gate uses the mean. Use this when the verifier is noisy or the agent's behaviour is non-deterministic.

### Blind A/B comparison

Independent verdict on whether `best_skill.md` is actually better than `initial_skill.md` — important because the SkillOpt gate uses the same verifier that proposed the edits, which can be self-confirming.

```bash
python3 scripts/blind_comparator.py \
    --skill-a runs/r1/initial_skill.md \
    --skill-b runs/r1/best_skill.md \
    --tasks tasks.jsonl \
    --output-dir cmp/r1
```

Per task: both skills run on the same prompt, outputs presented as X/Y to an independent judge with randomised labels. Aggregated to `comparison_report.{json,md}`.

### HTML viewer for a run

```bash
python3 scripts/eval_viewer.py runs/r1                    # opens in browser
python3 scripts/eval_viewer.py runs/r1 runs/r2 --compare  # side-by-side
```

Single-page static HTML: per-epoch chart, accepted/rejected edit timelines, slow-update history, per-task rollouts with grading, initial→best diff. No JS / CSS deps.

## Discover & Install Skills

Search and install skills from the open agent skills ecosystem via the [Skills CLI](https://github.com/vercel-labs/add-skill) (`npx skills`). Browse at [skills.sh](https://skills.sh).

### Find Skills

```bash
npx skills find [query]              # Interactive search
npx skills find react performance    # Keyword search
npx skills find pr review            # Search by task
```

### Install from Ecosystem

**Mandatory preflight:** determine the candidate frontmatter `name` and run the duplicate
auditor before installation. If the name exists, update/reuse the canonical copy instead.
For intentional cross-agent replicas, document the need and use
`install_skill.py --allow-duplicate-name` only after review.

For a locally maintained canonical source, prefer `install_skill.py --link`: every agent
sees the same real directory and future edits cannot make copied installs drift. Use a copy
only when the consumer cannot follow symlinks or deliberately needs an isolated snapshot.

```bash
npx skills add <owner/repo@skill> -g -y    # Install globally, skip prompts
npx skills add vercel-labs/agent-skills@vercel-react-best-practices -g -y
```

### List Ecosystem Skills

```bash
npx skills list                      # List all installed ecosystem skills
npx skills ls                        # Alias
npx skills list -g                   # Global skills only
npx skills list -a cursor            # Skills for a specific agent
```

### Remove Ecosystem Skills

Uninstalls skills installed via `npx skills add`. For locally-created skills, use `python3 scripts/delete_skill.py` instead.

**CRITICAL**: Always confirm with the user before removing.

```bash
npx skills remove <name> -g -y       # Remove a global skill, skip prompt
npx skills rm <name>                 # Alias, with confirmation prompt
npx skills remove <name> -a cursor   # Remove from specific agent
npx skills remove --all -g -y        # Remove all global ecosystem skills
```

### Check & Update

```bash
npx skills check                     # Check for available updates
npx skills update                    # Update all installed skills
```

Treat `npx skills check` as potentially mutating: some CLI versions update during `check`,
and `check --help` may enter the same workflow. Do not run it for read-only inspection unless
the user already authorized updates. Prefer repository HEAD, manager lock metadata, and
installed hashes for a read-only freshness comparison. After any managed update, rerun the
duplicate audit because stale lock entries can recreate removed copies.

### When to Search

Use `npx skills find` when the user:
- Asks "how do I do X" where X is a common task
- Says "find a skill for X" or "is there a skill for X"
- Wants specialized capabilities (design, testing, deployment, etc.)

### Common Search Categories

| Category | Example queries |
|----------|----------------|
| Web Dev | react, nextjs, typescript, tailwind |
| Testing | testing, jest, playwright, e2e |
| DevOps | deploy, docker, kubernetes, ci-cd |
| Docs | docs, readme, changelog, api-docs |
| Quality | review, lint, refactor, best-practices |
| Design | ui, ux, design-system, accessibility |
| Productivity | workflow, automation, git |

### Review & Compare Results

**Always suggest reviewing found skills after a search.** After presenting search results, ask the user if they'd like you to review and compare the top candidates before installing.

When there are 2+ results, proactively offer to fetch and assess the top candidates. This is agent-driven — use WebFetch on `https://skills.sh/<owner>/<repo>/<skill>` pages and apply judgment.

**Always offer review when:**
- Any search returns results (ask: "Want me to review these skills before you install?")
- 3+ results returned — review is especially valuable
- Multiple results with similar names or overlapping descriptions
- User asks to compare, review, evaluate, or pick the best
- A result has suspicious metrics (niche topic with very high installs)

**Process:**
1. Present the search results summary first
2. Ask the user if they want you to review/compare the top candidates
3. If yes: fetch skills.sh pages for top 3-6 candidates
4. Evaluate quality signals: install count, agent distribution, age, description, relevance, overlap with installed skills
5. Assign verdict: Recommended / Consider / Skip
6. Present ranked summary with 1-2 sentence assessments

See [references/remote-skill-assessment.md](references/remote-skill-assessment.md) for the full assessment framework including red flags and scoring signals.

### No Results

If no skills found: offer to help directly, then suggest `npx skills init <name>` to create a custom skill.

## Multi-Agent Operations

Manage skills across 42 supported AI coding agents. Full registry at [skills.sh](https://skills.sh).

### Supported agents

The authoritative registry of supported agents and discovery paths is
`scripts/agents.py`. Use `detect_agents.py --all` to print it instead of copying the table
into instructions where paths become stale.

### Detect Installed Agents

```bash
python3 scripts/detect_agents.py              # List detected agents
python3 scripts/detect_agents.py --all        # Show all supported agents
python3 scripts/detect_agents.py -f json      # JSON output
```

### List Skills for Any Agent

```bash
python3 scripts/list_agent_skills.py --agent cursor           # Single agent
python3 scripts/list_agent_skills.py --agent goose -s global  # Specific scope
python3 scripts/list_agent_skills.py --all                    # All detected agents
python3 scripts/list_agent_skills.py --agent amp -f json      # JSON output
```

### Install Skill to Agents

```bash
python3 scripts/install_skill.py /path/to/skill --agent cursor              # Single agent
python3 scripts/install_skill.py /path/to/skill --agent cursor --agent amp  # Multiple agents
python3 scripts/install_skill.py /path/to/skill --all                       # All detected
python3 scripts/install_skill.py /path/to/skill --agent goose -s global     # Global scope
python3 scripts/install_skill.py /path/to/skill --agent cursor --force      # Overwrite
python3 scripts/install_skill.py /path/to/skill --agent cursor --link --allow-duplicate-name  # Canonical alias
```

### Copy Skill Between Agents

```bash
python3 scripts/copy_skill.py my-skill --from claude-code --to cursor
python3 scripts/copy_skill.py my-skill --from claude-code --to cursor --to-scope global
python3 scripts/copy_skill.py my-skill --from claude-code --from-scope project --to amp
python3 scripts/copy_skill.py my-skill --from claude-code --to cursor --force
```

### Move Skill Between Agents

```bash
python3 scripts/move_skill_agent.py my-skill --from claude-code --to cursor
python3 scripts/move_skill_agent.py my-skill --from claude-code --to goose --force
```

## Important Notes

- **Restart required for new top-level dirs**: Creating a top-level `skills/` directory that did not exist when the session started requires restarting Claude Code so the directory can be watched
- **Live change detection (Claude Code, 2026)**: Adding, editing, or removing a skill under `~/.claude/skills/`, project `.claude/skills/`, or `.claude/skills/` inside an `--add-dir` directory takes effect within the current Claude Code session — no restart needed
- **Edits are immediate**: Changes to existing skill content work without restart
- **Agent detection**: Uses config directory presence to detect installed agents
- **Install once per discovery topology**: prefer one shared canonical root or symlink. Create agent-specific replicas only for consumers that cannot read that root, and audit after replication.
- **Custom commands have merged into skills (Claude Code, 2026)**: A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy`. Existing `.claude/commands/` files keep working; skills add a directory for supporting files, frontmatter, and auto-invocation.
- **Plugin skills are namespaced** as `plugin-name:skill-name` and cannot conflict with user/project skills

## OpenCode-specific notes

OpenCode (anomalyco/opencode v1.14.x) reads skills from **multiple compatible locations** in addition to its native paths:

- Project: `.opencode/skills/`, `.claude/skills/`, `.agents/skills/` — all loaded
- Global: `~/.config/opencode/skills/`, `~/.claude/skills/`, `~/.agents/skills/` — all loaded
- Walks up from CWD to the git worktree root, collecting skills along the way

This means a single Anthropic-format `SKILL.md` skill works across Claude Code, Codex, and OpenCode unchanged. Optional polish for OpenCode users:
- Add `compatibility: opencode,claude-code,codex` to the frontmatter
- Use lowercase tool names if your skill body invokes tools (`bash`, `edit`, `read` — not `Bash`/`Edit`/`Read`)

Skill access can be gated per-name with the `permission.skill` block in `opencode.json`:

```json
{ "permission": { "skill": { "*": "allow", "internal-*": "deny" } } }
```

See [references/opencode-skills.md](references/opencode-skills.md) for the full OpenCode skills reference.

## References — The Complete Guide to Building Skills for Claude

Consult these when reviewing skills or advising on skill structure and best practices.

| File | Description |
|------|-------------|
| `references/01-introduction.md` | What skills are, who this guide is for, two learning paths |
| `references/02-fundamentals.md` | Skill structure, progressive disclosure, composability, MCP integration |
| `references/03-planning-and-design.md` | Use cases, categories, success criteria, YAML frontmatter, writing instructions |
| `references/04-testing-and-iteration.md` | Trigger tests, functional tests, performance comparison, skill-creator usage |
| `references/05-distribution-and-sharing.md` | Distribution model, API usage, GitHub hosting, positioning |
| `references/06-patterns-and-troubleshooting.md` | 7 workflow patterns (incl. SkillOpt-style validated iterative refinement), common errors and fixes |
| `references/07-resources-and-references.md` | Official docs, example skills, tools, support channels |
| `references/ref-a-quick-checklist.md` | Pre-build, development, upload, and post-upload checklists |
| `references/ref-b-yaml-frontmatter.md` | Required/optional fields, security restrictions |
| `references/ref-c-complete-skill-examples.md` | Links to production-ready skill examples |
| `references/remote-skill-assessment.md` | Framework for evaluating ecosystem skills before installation |
| `references/skill-deduplication.md` | Canonical-source selection, duplicate classification, plugin handling, install preflight, and verification |
| `references/skill-optimization.md` | SkillOpt-style training loop: bounded edits, validation gate, rejected buffer, slow/meta update (Microsoft, arXiv 2605.23904) |
| `references/optimization-artifacts-schemas.md` | JSON schemas for every artefact written by `optimize_skill.py` and `log_skill_edit.py` (splits, state, rollouts, proposals, decisions, edit_apply_report, rejected_buffer, meta_skill, etc.) |
| `references/optimization-grading-checklist.md` | Audit checklist for a finished optimization run — what to inspect in `best_skill.md`, `edit_apply_report.json`, `rejected_buffer.json` before shipping |
| `prompts/analyst_error.md`, `analyst_success.md` | Failure / success analysis prompt contracts for the optimiser |
| `prompts/merge_failure.md`, `merge_success.md`, `merge_final.md` | Hierarchical edit-merge contracts |
| `prompts/ranking.md` | Edit ranking and selection contract |
| `prompts/slow_update.md`, `meta_skill.md` | Epoch-boundary slow-update and optimiser-side meta-skill contracts |
| `prompts/grader.md` | Rich grading contract for `--verifier assertions` (per-assertion pass/fail + claims + eval_feedback critique) |
| `prompts/blind_comparator.md` | Independent A/B judge contract for `blind_comparator.py` |

## Acknowledgments

Multi-agent support is based on the [Skills CLI](https://github.com/vercel-labs/add-skill) (`npx skills`) by Vercel Labs. Browse the open agent skills ecosystem at [skills.sh](https://skills.sh).
