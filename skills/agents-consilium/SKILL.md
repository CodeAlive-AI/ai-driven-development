---
name: agents-consilium
description: "Run external coding agents (Codex, Claude Code, OpenCode, native Grok Build, Gemini) as independent reviewers, repository researchers, or single-agent implementers. Use for multi-model opinions and code review, evidence-backed exploration of local or remote repositories, full-access delegation, steerable long-running work, or reattaching to delegated runs. Not for simple questions answerable directly from docs or the current codebase."
---

# Agents Consilium

Use only `scripts/consilium`. Select the mode from the user's intent and load only the linked reference needed for that mode.

## Decision map by intent

| User intent | Mode / reasonable default | Access | Read first |
|---|---|---|---|
| Independent architecture, design, debugging, or planning opinions | `review ask` with enabled profiles | read-only | [references/review.md](references/review.md) |
| Review a file or diff | `review code` (`basic`: security + correctness) | read-only | [references/review.md](references/review.md) |
| Review high-risk code | `review code --depth specialists` or `super` | read-only | [references/review.md](references/review.md) |
| Maximize review coverage | `review code --depth ultra` | read-only | [references/review.md](references/review.md) |
| Understand a local or remote repository | `explore` with Grok 4.5 | read-only | [references/explore.md](references/explore.md) |
| Implement with one external worker | `delegate -a <exact-id>` | **full YOLO** | [references/delegate.md](references/delegate.md) |
| Redirect and observe a long-running worker | `delegate --steerable`; steer with `--mode auto` | **full YOLO** | [references/delegate.md](references/delegate.md) |
| Let work outlive the caller or reattach later | `delegate --detach`, then `watch` or `wait` | **full YOLO for worker** | [references/delegate.md](references/delegate.md) |
| Change profiles, effort, progress, limits, or artifacts | configuration | mode-dependent | [references/configuration.md](references/configuration.md) |
| Diagnose events, capabilities, policy, prompts, or workflows | runtime contract | mode-dependent | [references/runtime-contracts.md](references/runtime-contracts.md) |
| Run or extend tests | offline fake suite by default | test-dependent | [references/testing.md](references/testing.md) |

`review` finds and validates problems. `explore` builds a relevance-first context map and answers from evidence. Do not substitute one for the other.

## Default launch commands

```bash
scripts/consilium --list-agents

# Independent opinions
scripts/consilium review ask "Should we use Postgres or SQLite?"
scripts/consilium review ask -a codex,grok,claude-fable --prompt-file prompt.md

# Code review
scripts/consilium review code path/to/file.py
git diff HEAD | scripts/consilium review code --diff
scripts/consilium review code --depth specialists path/to/file.py
scripts/consilium review code --depth super path/to/file.py
scripts/consilium review code --depth ultra path/to/file.py

# Repository exploration
scripts/consilium explore "How is authentication wired up?"
scripts/consilium explore --repo owner/repository --ref main "How are plugins loaded?"

# One-shot delegate; run from the target project CWD
scripts/consilium delegate -a grok "Implement the caching layer and run tests."

# Long-running delegate and steering
scripts/consilium delegate -a grok --steerable "Implement the caching layer."
scripts/consilium delegate steer run_<id> --mode auto "Keep the API compatible."
scripts/consilium delegate status run_<id> --json
scripts/consilium delegate watch run_<id>
scripts/consilium delegate wait run_<id>

# Detached delegate and recovery
RUN_ID=$(scripts/consilium delegate -a grok --detach "Implement SPEC.md.")
scripts/consilium delegate list --active
scripts/consilium delegate wait "$RUN_ID"
```

## Detail map

| File | Load for |
|---|---|
| [references/review.md](references/review.md) | selection, effort overrides, depths, progress, output, exit codes |
| [references/explore.md](references/explore.md) | sources, answer shape, isolation, trust boundary, web, provenance |
| [references/delegate.md](references/delegate.md) | YOLO rules, steering workflow, detach, mailbox states, delivery guarantees |
| [references/configuration.md](references/configuration.md) | prerequisites, profiles, shell-safe prompts, environment, limits |
| [references/runtime-contracts.md](references/runtime-contracts.md) | events, debug tape, safety/capabilities, workflows, prompt layers, artifacts |
| [references/testing.md](references/testing.md) | offline suite and opt-in real-backend smoke tests |
| [ACP-RESEARCH.md](ACP-RESEARCH.md) | deferred ACP transport research |
