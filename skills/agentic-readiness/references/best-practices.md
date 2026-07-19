# Agentic Repository Best Practices

Use this reference after instruction-file topology is understood. For `AGENTS.md` and `CLAUDE.md` details, read [instruction-files.md](instruction-files.md).

## Repository context

- Give the agent a map, not a duplicate wiki.
- Document exact commands and focused-test variants.
- Identify architectural boundaries and dangerous operational surfaces.
- Keep instructions close to their scope and avoid unrelated subtree context.
- Treat repeated agent mistakes and repeated review comments as signals to update guidance or enforcement.

## Cross-agent configuration

Audit only the surfaces the repository intentionally uses:

| Concern | Codex / Codex App | Claude Code | OpenCode |
|---|---|---|---|
| Project instructions | `AGENTS.md`, `.codex/config.toml` fallbacks | `CLAUDE.md`, `.claude/rules/` | `AGENTS.md`, `opencode.json` `instructions` |
| Project settings | `.codex/config.toml` | `.claude/settings.json`, `.claude/settings.local.json` | `opencode.json` / `opencode.jsonc`, `.opencode/` |
| Skills | Agent Skills locations and installed plugins | `.claude/skills/`, plugins | `.opencode/skills/`, Agent Skills compatibility |
| Subagents | `.codex/agents/*.toml` | `.claude/agents/*.md` | `.opencode/agents/*.md` |
| MCP | `mcp_servers` in TOML | `.mcp.json` / settings | `mcp` in OpenCode config |

Do not copy user configuration into a project. Never include credentials in audit output.

## Context management

- Keep persistent instructions concise and high-signal.
- Put conditional procedures in skills or scoped rules.
- Use retrieval or a context engine for large repositories; do not preload the entire documentation tree.
- Reset or start a fresh session when switching unrelated tasks or Git roots.
- Verify instruction discovery after changing launch directory, workspace, worktree, or config home.

## Reliable workflows

For implementation work:

1. Read applicable instructions.
2. Inspect before editing.
3. Make the smallest coherent change.
4. Run focused checks, then broader checks in proportion to risk.
5. Review the diff for unrelated user changes.
6. Report what was verified and what was not.

For large or risky work, separate planning, implementation, and independent review. Use subagents only when tasks are genuinely independent and the active instructions permit delegation.

## Safety

- Keep secrets out of prompts, instruction files, logs, and generated reports.
- Distinguish advice from enforcement: permissions, sandboxes, hooks, CI, and branch protection enforce boundaries.
- Scope allowlists narrowly; broad shell permissions are difficult to reason about.
- Resolve exact targets before destructive actions.
- Preserve dirty worktrees and unrelated staged changes.
- Treat network, infrastructure, release, and messaging actions as external state changes requiring the user's intended scope.

## Readiness over configuration volume

A repository is not more agent-ready because it has more rules, MCP servers, skills, or subagents. Prefer the smallest configuration that makes common work predictable. Flag missing configuration only when it creates a demonstrated gap.
