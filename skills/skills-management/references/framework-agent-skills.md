# Framework Agent Skills: Mastra & LangGraph / Deep Agents

Guide to how runtime agent frameworks (**Mastra** and **LangGraph / Deep Agents**) discover, load, retrieve, and authorize `SKILL.md` capabilities, and how they differ from coding-agent harnesses.

## Contents

- [Runtime Frameworks vs. Coding-Agent Harnesses](#runtime-frameworks-vs-coding-agent-harnesses)
- [Mastra (`@mastra/core`)](#mastra-mastracore)
- [LangGraph / Deep Agents (`SkillsMiddleware`)](#langgraph--deep-agents-skillsmiddleware)
- [Cross-Framework Portability Checklist](#cross-framework-portability-checklist)

## Runtime Frameworks vs. Coding-Agent Harnesses

| Dimension | Coding-Agent Harnesses (Antigravity, Claude Code, Codex, OpenCode) | Mastra (`@mastra/core`) | LangGraph / Deep Agents (`SkillsMiddleware`) |
|---|---|---|---|
| **Skill source** | Filesystem roots (`.agents/skills/`, `~/.gemini/config/skills/`, `~/.claude/skills/`) | `Workspace` paths/globs OR code-defined `createSkill()` | Abstract `BackendProtocol` (`FilesystemBackend`, `StateBackend`, `StoreBackend`, `CompositeBackend`) |
| **Discovery** | Startup frontmatter scan (~50–100 tokens/skill) | Default eager `SkillsProcessor` OR on-demand `SkillSearchProcessor` (BM25 / vector) | Startup frontmatter scan injected by `SkillsMiddleware` |
| **Loading** | Model reads `SKILL.md` or user runs `/<name>` | `search_skills` → `load_skill` → `skill_read` | Agent reads `SKILL.md` via file tools, or forced via `pinned_skills` / `/<name>` |
| **Collision order** | First-match wins (workspace > global > built-in) | Workspace registration order | **Last source wins** (`sources=[base, user, project, team]`) |
| **Tool gating** | Host permissions / `allowed-tools` (CC) | Workspace + agent tool configuration | Dynamic unlocking via `metadata.include_tools` |

## Mastra (`@mastra/core`)

Mastra supports the `SKILL.md` standard in two distinct contexts:

1. **Coding-agent skills for developing Mastra apps**: Community/vendor skills (for example `npx skills add mastra-ai/skills`) installed into `.agents/skills/` or `~/.claude/skills/` so coding agents write current Mastra TypeScript code.
2. **Runtime workspace skills for Mastra agents**: Skills loaded by your deployed TypeScript agent at runtime.

### Filesystem Workspace vs. `createSkill()`

- **Filesystem-backed skills**: Register skill roots relative to a `Workspace` filesystem (`skills: ['skills']` or globs like `['./**/skills']`). Each skill folder holds `SKILL.md` plus optional `references/`, `scripts/`, and `assets/`.
- **Code-defined skills (`createSkill`)**: Use `createSkill({ name, description, instructions, references })` from `@mastra/core/skills` when an agent runs without a filesystem workspace or ships bundled inline references (`references: { 'guide.md': '...' }`).

### On-Demand Discovery with `SkillSearchProcessor`

By default, `SkillsProcessor` loads skill context eagerly. For larger skill catalogs, attach **`SkillSearchProcessor`** (with `bm25: true` or vector indexing on `Workspace`) to keep startup tokens flat:

1. **`search_skills`**: Agent queries available skills by keywords/semantics (`topK`, `minScore`) rather than seeing all instructions upfront.
2. **`load_skill`**: Pulls the matched `SKILL.md` instructions into the active thread on demand.
3. **`skill_read`**: Scoped reader for inspecting `references/`, `scripts/`, or `assets/` inside an already-loaded skill without exposing arbitrary workspace filesystem tools.

### Mastra Authoring Nuances

- **BM25-friendly `description`**: Because `SkillSearchProcessor` retrieves via BM25 or embeddings, include concrete domain nouns, API names, error terms, and action verbs in `description` rather than generic summaries.
- **Keep `references/` paths clean**: Reference bundled files using relative paths (`references/style-guide.md`) so `skill_read` resolves them cleanly inside the skill bundle.

## LangGraph / Deep Agents (`SkillsMiddleware`)

In LangChain/LangGraph Deep Agents, **`SkillsMiddleware`** decouples skill storage, discovery, and tool exposure from local OS assumptions.

### Abstract Storage Backends (`BackendProtocol`)

`SkillsMiddleware` never assumes a local POSIX shell or direct disk access — skills can live in:

- **`FilesystemBackend`** (`root_dir`): Local or mounted disk directories.
- **`StateBackend`**: Ephemeral, thread-scoped skills inside LangGraph state.
- **`StoreBackend`**: Durable cross-thread skills in LangGraph's persistent store.
- **`CompositeBackend`**: Hybrid routing across multiple backends.

Design skill instructions without assuming `/Users/...` paths or arbitrary bash execution unless `compatibility` explicitly states a sandbox/shell requirement.

### Precedence: Last-Source-Wins

Unlike Antigravity, Claude Code, and OpenCode (where higher-priority workspace dirs win first), `SkillsMiddleware(backend=..., sources=[...])` scans `sources` in order and **later sources override earlier ones** on `name` collision:

```python
skills_middleware = SkillsMiddleware(
    backend=backend,
    sources=[
        "/app/skills/base/",      # Lowest priority
        "/app/skills/user/",      # Overrides base
        "/app/skills/project/",   # Highest priority (overrides user & base)
    ],
)
```

Passing tuples such as `("/home/user/.claude/skills", "User Override")` disambiguates source labels in diagnostics. Note that the standalone **`deepagents` CLI** (`scripts/agents.py`) still reads `.agents/skills`, `~/.agents/skills`, and legacy `~/.deepagents/agent/skills`.

### Dynamic Tool Binding (`metadata.include_tools`)

To prevent tool-schema bloat at startup, bind skill-specific tools in `SKILL.md` frontmatter using `metadata.include_tools` (space-separated string or YAML list) alongside `SkillsMiddleware(tools=[...])`:

```yaml
---
name: call-transcripts
description: Search call records and summarize transcripts. Use when asked to inspect customer calls.
metadata:
  include_tools: search_calls get_transcript
---
```

When the agent reads the full `SKILL.md`, the bound tools are unlocked for subsequent turns in that thread.

### Pinned Skills

Users or orchestrators can bypass semantic discovery by passing `pinned_skills` or invoking `/<skill-name>`, which pre-loads the full `SKILL.md` directly into the conversation as a `HumanMessage`.

## Cross-Framework Portability Checklist

- [ ] `name` is lowercase kebab-case matching the directory name (`1–64` chars)
- [ ] `description` front-loads concrete domain keywords (works for both LLM catalog routing and Mastra BM25 search) plus imperative triggers and negative triggers
- [ ] Optional `compatibility` notes when a local shell, sandbox, or external binary is required (avoids silent failures under `StateBackend` / `StoreBackend`)
- [ ] Skill-specific runtime tools (if used in LangGraph Deep Agents) are listed under `metadata.include_tools`
- [ ] Supporting files use relative paths (`references/...`, `scripts/...`) compatible with `skill_read`, `BackendProtocol`, and coding-agent file tools
