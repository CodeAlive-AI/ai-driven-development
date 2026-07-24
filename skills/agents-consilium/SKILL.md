---
name: agents-consilium
description: "Query external AI agents (Codex, Claude Code, OpenCode, native Grok Build, Gemini) for independent second opinions, multi-depth code review, and full-YOLO single-agent delegation. Two public modes via scripts/consilium: review (read-only ask/code) and delegate (exact agent, no sandbox; optional --steerable long session with steer/status/cancel). Use for architecture choices, security review, deep multi-stage review, or handing a whole task to one agent. Not for simple questions answerable from docs or the codebase."
---

# Consilium v5: Multi-Agent Review & Delegation

Query external AI agents for independent expert opinions, structured code review, or full-YOLO task delegation. Review modes stay read-only. Delegate hands the whole task to **exactly one** explicitly selected agent in the caller's CWD.

## Public CLI (only entrypoint)

```bash
scripts/consilium review ask [...]
scripts/consilium review code --depth basic|specialists|super|ultra [...]
scripts/consilium delegate -a <exact-agent-id> [...]
scripts/consilium delegate -a <exact-agent-id> --steerable [...]
scripts/consilium delegate steer RUN_ID [--mode auto|queue|interrupt] [...]
scripts/consilium delegate status RUN_ID [--json]
scripts/consilium delegate cancel RUN_ID
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

Exit codes for `review code` (basic/specialists): `0` all specialists ok · `2` partial (report still emitted from successes) · `3` all failed · `4` config · `5` usage.

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

### `delegate --steerable`

Long-lived single-agent session with a filesystem mailbox. Prints `run_id=…` early on stderr; final answer still goes to stdout when the run completes.

```bash
scripts/consilium delegate -a grok --steerable "Implement the caching layer"
# other terminal / later:
scripts/consilium delegate steer run_<id> --mode auto "Prefer Redis over memcached"
scripts/consilium delegate status run_<id> --json
scripts/consilium delegate cancel run_<id>
```

#### Required workflow for the calling agent

Use this sequence whenever the user may want to redirect an active delegate:

1. Run the command from the target project CWD. Start it in a long-running
   process/PTY or in the background so the calling agent remains able to read
   progress and issue control commands. Do **not** wait synchronously for the
   final stdout before attempting to steer.
2. Read early stderr and capture the exact `run_id=run_<id>`. Keep the original
   process handle open: its stderr is the live progress stream and its stdout
   will contain the final answer.
3. If `CONSILIUM_STEER_DIR` was overridden for the start command, pass the same
   environment value to every later `steer`, `status`, and `cancel` command.
4. Send only new information or a clear course correction. Do not repeat the
   entire original task. Use `--prompt-file` or stdin for long guidance.
5. Use `--mode auto` unless the user explicitly needs different semantics.
   Record the returned `client_id` and `seq`.
6. Treat the immediate `accepted` response as mailbox persistence only. Query
   `delegate status RUN_ID --json`, find the matching `client_id`, and inspect
   `mailbox_status`, `delivery_class`, `backend_ack`, and `error`.
7. Continue observing the original process. A later backend event may promote
   the steer from `request_sent`/`queued` to `applied`.
8. Wait for the original delegate process to finish and consume its stdout as
   the final answer. Use `cancel` only when intentionally stopping the whole
   delegated run.

Choose the mode deliberately:

| Mode | Use when | Important consequence |
|------|----------|-----------------------|
| `auto` | Normal clarification, extra constraint, or preferred direction | Uses the safest native behavior available for that backend |
| `queue` | The current work may finish; apply guidance at the backend's next safe boundary | May not affect the currently executing turn; for Grok it is a real next-turn FIFO entry |
| `interrupt` | The current direction is wrong and its partial work should be abandoned | May cancel the active turn/tool flow; Claude rejects it instead of silently downgrading |

Interpret steer status precisely:

| `mailbox_status` | Meaning |
|------------------|---------|
| `accepted` | Persisted locally; the supervisor has not dispatched it yet |
| `delivering` | The supervisor is currently calling the backend adapter |
| `request_sent` | Written to the backend transport; no application evidence yet |
| `queued` | Queued/accepted by the backend but not yet observed running |
| `applied` | Correlated backend evidence confirms the guidance was replayed, started, or completed |
| `failed` / `rejected` | Not applied; inspect `error` and decide whether to start a new run |

For retry-safe automation, provide a stable `--client-id`:

```bash
scripts/consilium delegate steer run_<id> \
  --client-id requirement-cache-backend-v1 \
  --mode auto \
  --prompt-file steer.md
```

Retry the same `client_id` only with identical guidance, mode, and kind.
Changing any of them is an idempotency conflict and is rejected. If the run is
already terminal or its mailbox is closed, do not keep retrying that run; start
a new delegate with the remaining task. Do not put secrets into steer guidance
unless persistence in private raw/audit artifacts is intentional.

- Large task/guidance bodies travel via files or mailbox JSON — never large argv/env.
- **Mailbox `accepted` ≠ protocol delivered/applied.** `status` shows `delivery_class` and backend evidence separately.
- Protocol ack ladder: `request_sent`/`queued` = transport wrote the request; `applied` only after backend confirmation (matching `promptId` / user replay / `clientUserMessageId`).
- Registry root: `CONSILIUM_STEER_DIR` (default under user cache). Permissions: registry/run dirs `0700`, state files `0600`. Symlink run dirs are rejected.
- **Steerable always keeps a service registry + protocol artifacts** (mailbox, audit, raw/normalized/final under the private registry run or the configured `CONSILIUM_RUN_DIR`) for observability — even when `CONSILIUM_SAVE_OUTPUTS=0` disables ordinary review/delegate archival. With `SAVE_OUTPUTS=0`, protocol artifacts never land in the project cwd; `meta.artifacts_dir` records the private 0700 path. Registry is independent of output archival.
- Client ids are never used as path components (SHA-256 safe names); original `client_id` is stored in JSON. Idempotent retry requires the same content hash, mode, and kind; otherwise conflict is rejected.
- Terminal transition serializes with enqueue: remaining open mailbox messages are failed with an explicit reason; no accepted/delivering message is left without a terminal outcome.

#### Honest delivery matrix

| Backend | `auto` | `queue` | `interrupt` |
|---------|--------|---------|-------------|
| Claude Code | `same_turn` (stream-json stdin + user replay) | same as auto | **rejected** (no silent downgrade) |
| Codex CLI | `same_turn` (`turn/steer` + `expectedTurnId`) | same as auto | `abort_and_prompt` (`turn/interrupt` → wait `turn/completed` for that turn → `turn/start`); stale turn id → explicit reject |
| OpenCode | `step_inject` (`prompt_async` at step boundary; works while busy) | same as auto | `abort_and_prompt` (session abort then prompt); loopback-only URL + redirect re-validation; per-run `OPENCODE_SERVER_PASSWORD` Basic auth (password never logged/stored); `message.part.updated` is cumulative per part id |
| Grok Build | `queue_next_turn` (concurrent ACP `session/prompt`; server FIFO) | same as auto | `cancel_and_send` (second prompt with `_meta.sendNow: true` + own `promptId`) |

Grok steerable uses native ACP `grok agent stdio` concurrent prompt queue semantics (not same-turn injection, not external holding of prompts until first completion). Attribution uses `_meta.promptId` on notifications and `x.ai/session/prompt_complete` / `_x.ai/session/prompt_complete`, plus `_x.ai/queue/changed` (`entries[].id`, `runningPromptId`). Writing a concurrent `session/prompt` is `request_sent`/`queued`, not `applied`, until the matching promptId is observed. If confirmation arrives after `steer()` returns `queued`, the adapter emits correlated `steer_ack` events and the supervisor reconciles mailbox/state by saved `meta.promptId` (never demoting terminal statuses). Only `agent_message_chunk` (and confirmed aliases) contributes to final text; `agent_thought_chunk` is progress/thought only; `user_message_chunk` is replay only.

Codex interrupt uses a **local protocol-ack wait** (bounded handshake for the interrupted turn's `turn/completed`) — not a global run timeout. Ordinary `turn/completed` with status `completed` ends this delegate run (not a permanent idle session).

Claude authoritative `result` events complete the adapter even if stdin remains open; stderr is always drained. Same-turn steers remain possible until that result.

## Observability contract

| Stream | Content |
|--------|---------|
| **stderr** | Compact semantic **live** progress (`[consilium] start|event|done|stage …`) while the model is still running — not post-hoc after completion |
| **stdout** | Clean final answer only |
| **artifacts** | Per-run dir under `CONSILIUM_OUTPUT_DIR` (or `CONSILIUM_RUN_DIR`): `raw/*.jsonl`, `normalized/*.jsonl`, `final/*.txt`, `final.txt`. Keys are per-invocation: plain agent id for ask/delegate, `agent.role` for basic/specialists code review, explicit stage/index keys for super/ultra discovery (`<stage>.<index>.<agent>.<role>`), and `judge.primary.<agent>` / `judge.fallback.<agent>` for judge attempts. Fan-out never relies on ambient inherited `CONSILIUM_ARTIFACT_KEY` alone. |

Architecture: `backend_cmd | normalize_stream.py --raw-out --progress --extract-text`. Each raw line is persisted and normalized immediately; progress reaches stderr before process completion. `PIPESTATUS` preserves backend exit (timeout/signal) and Grok end/error validation independently.

Disable ordinary review/delegate archival with `CONSILIUM_SAVE_OUTPUTS=0`. Steerable runs still maintain their service registry (`CONSILIUM_STEER_DIR`) and protocol artifacts needed for steer/status/cancel observability.

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
| Delegate while retaining the ability to redirect it mid-run | `delegate -a <id> --steerable` |

## Environment variables

- `CONSILIUM_CONFIG`, `CONSILIUM_AGENTS`, `CONSILIUM_EXCLUDE`
- `CONSILIUM_OUTPUT_DIR`, `CONSILIUM_RUN_DIR`, `CONSILIUM_SAVE_OUTPUTS`
- `CONSILIUM_STEER_DIR` — registry root for steerable runs
- `AGENT_TIMEOUT` (`0`/unset = unlimited; positive integer = opt-in seconds)
- Per-backend: `CODEX_MODEL` / `CODEX_EFFORT`, `CLAUDE_MODEL` / `CLAUDE_EFFORT`, `OPENCODE_MODEL` / `OPENCODE_EFFORT`, `GEMINI_MODEL`, `GEMINI_API_KEY`

## Tests

```bash
scripts/tests/run.sh
```

Uses fake backend CLIs; asserts argv safety (review sandboxes vs delegate YOLO), exact agent selection, stdout/stderr separation, artifacts, Grok streaming-json success/failure, live progress before backend exit, and steerable-delegate mailbox/adapters (Claude/Codex/OpenCode/Grok transport fakes, concurrent Grok queue + sendNow, cancel, idempotency, cleanup). Default suite is offline — no network/model spend.

Opt-in real smoke (spends tokens):

```bash
CONSILIUM_STEER_SMOKE=1 bash scripts/tests/steer/smoke_real.sh -a grok
```

## Prerequisites

- [Codex CLI](https://github.com/openai/codex) — `codex-cli` backend
- [OpenCode](https://opencode.ai) — `opencode` backend
- [Claude Code](https://docs.claude.com/claude-code) — `claude-code` backend
- [Grok Build](https://grok.x.ai) CLI (`grok`) — `grok-build` backend
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — optional, review-only
- Python 3
