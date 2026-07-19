---
name: agentic-readiness
description: Audit and improve repositories for reliable agentic work across Codex and Codex App, Claude Code, and OpenCode. Use when reviewing AGENTS.md or CLAUDE.md quality and discovery, instruction routing in monorepos or meta-repos, agent settings, MCP configuration, skills, subagents, context budgets, or repository organization for coding agents.
---

# Agentic Readiness

Default to audit-only. Present findings and wait for approval unless the user explicitly asks to implement changes.

## Audit workflow

1. Read the repository's existing instruction chain before inspecting other files.
2. Run from the repository root:

```bash
python scripts/audit_repo.py --root .
```

Add `--include-user-scope` only when the user explicitly wants personal Codex, Claude Code, and OpenCode configuration included. Never inspect credential stores or print secret values.

3. Inspect the JSON report and verify findings against the actual build files, scripts, and repository layout. The script detects structural risks; it cannot prove that documented commands or architecture are current.
4. Read the references needed for the task:
   - [instruction-files.md](references/instruction-files.md) for `AGENTS.md`/`CLAUDE.md` ownership, discovery, routing, compatibility, and CodeAlive lessons learned.
   - [rubric.md](references/rubric.md) for scoring and priority definitions.
   - [checklist.md](references/checklist.md) for the full cross-agent audit.
   - [best-practices.md](references/best-practices.md) for settings, workflows, context, and safety beyond instruction files.
5. Report evidence before recommendations.

## Report shape

Keep the report concise:

- **Executive summary**: readiness, strongest area, main failure mode, first action.
- **Repository profile**: scale, languages/frameworks, Git/worktree shape.
- **Instruction topology**: canonical file, compatibility shim, nested routing, active-chain caveats, context-budget risks.
- **Agent surfaces**: Codex/Codex App, Claude Code, and OpenCode settings, MCP, skills, and subagents actually present.
- **Issues**: P0 through P3 with file paths and evidence.
- **Recommendations**: concrete edits and verification commands.

Do not penalize a repository for omitting agent-specific configuration it does not need. Do flag a claimed cross-agent setup that one of the named agents cannot discover.

## Implementation workflow

When the user asks to apply changes:

1. Confirm the requested scope from the conversation; do not ask again when it is already explicit.
2. Preserve one source of truth. Prefer root `AGENTS.md` plus a regular `CLAUDE.md` containing `@AGENTS.md` when the same rules should serve all three agents.
3. Put scoped rules near their target paths. Add routing indexes only where they prevent real discovery mistakes.
4. Keep generated directories, dependencies, caches, secondary worktrees, and unrelated subtrees out of routing tables.
5. Turn non-negotiable rules into hooks, linters, or CI checks; instruction files are guidance, not enforcement.
6. Show the diff, rerun the audit and tests, then explain any remaining intentional gaps.

## Large and multi-repository workspaces

For more than 3,000 tracked files, emphasize navigation, bounded routing, focused verification, and retrieval support rather than copying documentation into startup context.

For a directory containing multiple child Git repositories, treat each child as an independent instruction root. Codex builds its instruction chain once per run/session, so changing a command's working directory does not load the child repository's files. Recommend an explicit meta-repository routing rule and verify each child from a fresh session or by reading its chain before the first operation.
