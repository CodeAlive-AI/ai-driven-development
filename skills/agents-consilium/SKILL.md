---
name: agents-consilium
description: "Query external AI agents (Codex, Claude Code, OpenCode, native Grok Build, Gemini) for independent second opinions, multi-depth code review, and full-YOLO single-agent delegation. Two public modes via scripts/consilium: review (read-only ask/code) and delegate (exact agent, no sandbox). Use for architecture choices, security review, deep multi-stage review, or handing a whole task to one agent. Not for simple questions answerable from docs or the codebase."
---

# Consilium v5: Multi-Agent Review & Delegation

Query external AI agents for independent expert opinions, structured code review, or full-YOLO task delegation. Review modes stay read-only. Delegate hands the whole task to **exactly one** explicitly selected agent in the caller's CWD.

## Public CLI (only entrypoint)

```bash
scripts/consilium review ask [...]
scripts/consilium review code --depth basic|specialists|super|ultra [...]
scripts/consilium delegate -a <exact-agent-id> [...]
scripts/consilium --list-agents
```

Old public scripts (`consensus-query.sh`, `code-review.sh`, `superreview.sh`, `ultrareview.sh`, `*-query.sh`) were removed in v5. Internal modules live under `scripts/lib/`.

## Why this skill

**Different frontier models see different things.** Parallel independent reviews surface issues and alternatives one model alone misses. Consilium keeps agents independent (no debate, no cross-contamination) and lets the caller adjudicate.

## Modes

| Mode | Read/write | Purpose |
|------|------------|---------|
| `review ask` | read-only | Open-ended question → parallel opinions |
| `review code --depth basic` | read-only | 2 specialists: security + correctness |
| `review code --depth specialists` | read-only | 5 specialists |
| `review code --depth super` | read-only | Multi-stage superreview + LLM judge |
| `review code --depth ultra` | read-only | Multi-stage ultrareview + LLM judge |
| `delegate -a <id>` | **full YOLO** | One agent implements the task in CWD |

### `review ask`

```bash
scripts/consilium review ask "Should we use Postgres or SQLite?"
scripts/consilium review ask --xml --prompt-file prompt.md
scripts/consilium review ask -a codex,grok "Review this approach"
scripts/consilium review ask -a 'opencode-go-*' -x opencode-go-minimax "Q"
scripts/consilium --list-agents
```

Exit codes: `0` all ok · `2` partial · `3` all failed · `4` config · `5` usage.

### `review code`

```bash
scripts/consilium review code path/to/file.py
scripts/consilium review code --depth specialists --xml path/to/file.py
git diff HEAD | scripts/consilium review code --diff
scripts/consilium review code --depth super path/to/file.cs
scripts/consilium review code --depth ultra --dry-run path/to/file.cs
```

- **basic** (default): security + correctness, fixed 2 passes, quoted-code validation.
- **specialists**: + performance, architecture, consistency.
- **super** / **ultra**: multi-stage discovery + deterministic dedup + LLM judge (same stage layouts as v4 superreview/ultrareview).

Review is always read-only. Do **not** use Grok's `/review` slash command — consilium owns review semantics.

### `delegate`

```bash
scripts/consilium delegate -a grok "Implement the caching layer described in DESIGN.md"
scripts/consilium delegate -a codex --prompt-file task.md
```

- Exact agent id required (`-a`). **No globs, no default agent, no multi-select.**
- Full YOLO in the caller's CWD: no sandbox, no approval prompts, no confirmation flag.
- Supported: Codex CLI, Claude Code, OpenCode, **native Grok Build**.
- **Gemini is review-only** — delegate rejects `gemini-cli`.

## Observability contract

| Stream | Content |
|--------|---------|
| **stderr** | Compact semantic **live** progress (`[consilium] start|event|done|stage …`) while the model is still running — not post-hoc after completion |
| **stdout** | Clean final answer only |
| **artifacts** | Per-run dir under `CONSILIUM_OUTPUT_DIR` (or `CONSILIUM_RUN_DIR`): `raw/*.jsonl`, `normalized/*.jsonl`, `final/*.txt`, `final.txt` |

Architecture: `backend_cmd | normalize_stream.py --raw-out --progress --extract-text`. Each raw line is persisted and normalized immediately; progress reaches stderr before process completion. `PIPESTATUS` preserves backend exit (timeout/signal) and Grok end/error validation independently.

Disable archival with `CONSILIUM_SAVE_OUTPUTS=0`.

## Resource-limit contract

Consilium is unlimited by default:

- no wrapper timeout (`AGENT_TIMEOUT=0`);
- no `max-turns`, step, token, response-length, or budget flags;
- prompts travel over stdin or a temporary prompt file, never as large argv values;
- raw, normalized, and final artifacts are not truncated;
- final text is streamed to disk rather than buffered as one in-memory response.

Provider context windows, model output limits, and limits in user/managed harness
configuration still apply. To add an explicit watchdog for one invocation, set
`AGENT_TIMEOUT` to a positive number of seconds.

## Transport: direct CLI (not ACP)

Consilium uses **direct headless CLI** invocations for every backend (argv + stdout streams). It does **not** use the Agent Client Protocol as the batch transport.

Grok Build already exposes native ACP via `grok agent stdio`, so a separate `grok-acp` wrapper is unnecessary and intentionally not part of this skill. ACP is not the batch transport because:

1. **Safety stays on CLI flags.** Review/delegate enforcement is backend-specific (`--sandbox read-only`, plan agents, tool allow/deny lists, YOLO bypasses). Consilium must set those explicitly; ACP sessions do not replace harness/OS safety.
2. **Uniform multi-backend surface.** Codex and Claude need adapters for ACP today; direct CLI is the common denominator that works for Codex, Claude Code, OpenCode, Grok Build, and Gemini without per-vendor bridges.
3. **Streaming observability maps cleanly.** Raw JSONL capture, normalized events, and live stderr progress are straightforward over CLI stdout pipes.

## Backends & read-only / YOLO flags

| Backend | Review (read-only) | Delegate (YOLO) |
|---------|--------------------|-----------------|
| `codex-cli` | `exec --sandbox read-only` + ask-for-approval never | `--dangerously-bypass-approvals-and-sandbox` |
| `claude-code` | `--permission-mode plan` + disallowed Edit/Write | `--dangerously-skip-permissions` |
| `opencode` | `--agent plan` | `--agent build --auto` |
| `grok-build` | `--sandbox read-only` + tool allowlist/denylist (plan alone is **not** read-only) | `--always-approve`, no sandbox |
| `gemini-cli` | `--approval-mode plan` | not supported |

### Native Grok Build (default Grok path)

```json
"grok": {
  "enabled": true,
  "backend": "grok-build",
  "model": "grok-4.5",
  "effort": "high",
  "role": "analyst",
  "label": "Grok 4.5 (native)"
}
```

- One-shot headless: `grok --prompt-file … --output-format streaming-json` (`--prompt-file` is the documented single-turn-from-file path; equivalent class to `-p/--single` for inline prompts)
- Final text = concatenation of `type=text` event `data` fields
- Success requires process exit 0, an `end` event, and no `error` event
- OpenCode `xai/grok-4.5` remains as **disabled** fallback (`opencode-xai-grok45`)

## Configuration

`config.json` at the skill root (`CONSILIUM_CONFIG` override). Per agent:

| Field | Purpose |
|-------|---------|
| `enabled` | Default participation in `review ask` / basic code agent pool |
| `backend` | `codex-cli` \| `claude-code` \| `opencode` \| `grok-build` \| `gemini-cli` |
| `model` | Model id |
| `role` | `analyst` \| `lateral` \| specialist roles |
| `effort` | Backend-specific reasoning effort |
| `label` | Display name |
| `supports_delegate` | Optional; `false` for review-only agents |

## Shell escaping

Prefer `--prompt-file`, stdin, or a single-quoted heredoc for prompts with backticks, `$`, `!`, or quotes. Double-quoted positionals are expanded by the shell and can hang backends waiting on stdin.

A shell-interpolation warning is emitted only for **positional** prompts that still contain `` ` `` or `$(...)`. Content from `--prompt-file` or stdin is never warned (code samples legitimately contain those characters).

```bash
scripts/consilium review ask --prompt-file prompt.md
scripts/consilium review ask "$(cat <<'EOF'
Explain `foo` and $PATH handling.
EOF
)"
```

## When to use which

| Situation | Command |
|-----------|---------|
| Architecture / brainstorm | `review ask` |
| Quick file/diff review | `review code` (basic) |
| High-stakes PR file | `review code --depth specialists` or `super` |
| Max coverage | `review code --depth ultra` |
| “Just implement this” with one agent | `delegate -a <id>` |

## Environment variables

- `CONSILIUM_CONFIG`, `CONSILIUM_AGENTS`, `CONSILIUM_EXCLUDE`
- `CONSILIUM_OUTPUT_DIR`, `CONSILIUM_RUN_DIR`, `CONSILIUM_SAVE_OUTPUTS`
- `AGENT_TIMEOUT` (`0`/unset = unlimited; positive integer = opt-in seconds)
- Per-backend: `CODEX_MODEL` / `CODEX_EFFORT`, `CLAUDE_MODEL` / `CLAUDE_EFFORT`, `OPENCODE_MODEL` / `OPENCODE_EFFORT`, `GEMINI_MODEL`, `GEMINI_API_KEY`

## Tests

```bash
scripts/tests/run.sh
```

Uses fake backend CLIs; asserts argv safety (review sandboxes vs delegate YOLO), exact agent selection, stdout/stderr separation, artifacts, Grok streaming-json success/failure, and a timing/order test that progress is observable before backend exit.

## Prerequisites

- [Codex CLI](https://github.com/openai/codex) — `codex-cli` backend
- [OpenCode](https://opencode.ai) — `opencode` backend
- [Claude Code](https://docs.claude.com/claude-code) — `claude-code` backend
- [Grok Build](https://grok.x.ai) CLI (`grok`) — `grok-build` backend
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — optional, review-only
- Python 3
