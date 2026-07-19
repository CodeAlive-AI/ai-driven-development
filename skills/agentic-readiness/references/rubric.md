# Agentic Readiness Rubric

Score evidence, not file count. A repository that intentionally supports one agent can be excellent without configuring all three.

## Scoring

### Discovery and ownership: 0–4

- **0:** No usable project instructions.
- **1:** Instructions exist but are missed by an intended agent.
- **2:** All intended agents can load guidance, but ownership or precedence is ambiguous.
- **3:** Canonical source and compatibility adapters are explicit.
- **4:** Discovery is verified from representative roots, subtrees, and child repositories.

### Commands and verification: 0–4

- **0:** No executable workflow documented.
- **1:** Commands are partial or stale.
- **2:** Main build/test/lint commands exist.
- **3:** Focused checks and definition of done are documented and accurate.
- **4:** Critical requirements are also enforced by CI, hooks, or policy.

### Architecture and routing: 0–4

- **0:** Agent must guess repository structure and boundaries.
- **1:** Basic directory list only.
- **2:** Entry points and major modules are identified.
- **3:** Nested or child-repository instruction routing is scoped and non-duplicative.
- **4:** Routing has drift checks and excludes generated/unrelated trees.

### Conciseness and consistency: 0–4

- **0:** Contradictory or dangerously stale guidance.
- **1:** Large duplicated files or unresolved imports.
- **2:** Mostly clear, with some duplication or excess startup context.
- **3:** Concise canonical guidance with on-demand references.
- **4:** Context budgets are measured and recurring feedback is folded into the right layer.

### Safety and configuration: 0–4

- **0:** Instructions or config expose secrets or authorize obviously unsafe defaults.
- **1:** Important boundaries are missing or only implied.
- **2:** Destructive actions, secrets, and external-state changes are addressed.
- **3:** Settings, MCP, skills, and subagents are scoped to real needs.
- **4:** Non-negotiable boundaries are mechanically enforced and tested.

## Rating

| Total | Rating |
|---|---|
| 0–5 | Not ready |
| 6–10 | Fragile |
| 11–15 | Functional |
| 16–18 | Strong |
| 19–20 | Excellent |

Do not hide a P0 behind a high aggregate score.

## Common findings

### P0

- Intended agents cannot discover any project instructions.
- Documented workflow risks destructive production or credential exposure.
- Required command is wrong in a way that blocks all verification.

### P1

- `AGENTS.md` and `CLAUDE.md` are independent copies with conflicting rules.
- A Codex session crosses into a child repository without an explicit read/routing rule.
- A committed `AGENTS.override.md` unintentionally masks canonical instructions.
- Critical nested guidance is not reachable from normal starting directories.
- Codex instruction chains exceed the configured byte budget.
- Build/test/release requirements are stale.

### P2

- `CLAUDE.md` is a symlink where a portable import shim would be easier.
- Routing indexes omit useful descriptions or contain generated paths.
- Claude imports organize text but unnecessarily preload large documents.
- OpenCode relies on `@references` it does not expand automatically.
- Agent-specific config is present but poorly documented.

### P3

- Minor navigation improvements.
- Optional focused-test examples.
- Formatting or wording refinements with no observed failure mode.

## Report template

```markdown
# Agentic Readiness Report

## Executive summary
- Overall score: X/20
- Intended agents: Codex/Codex App, Claude Code, OpenCode
- Main strength: ...
- Main risk: ...
- First action: ...

## Instruction topology
| Path | Agent(s) | Scope | Status |
|---|---|---|---|

## Issues
### P0
### P1
### P2
### P3

## Recommended edits
1. ...

## Verification
- Commands run: ...
- Fresh-session checks: ...
- Not verified: ...
```
