# Delegate mode

Delegate hands one task to exactly one explicitly selected coding-agent profile in the caller's current directory.

## Contents

- Default steerable, explicit one-shot, and detached runs
- Required caller workflow and exit codes
- Steering modes and mailbox lifecycle
- Retry safety, registry, and artifacts
- Backend delivery differences

```bash
scripts/consilium delegate -a grok "Implement the caching layer described in DESIGN.md"
scripts/consilium delegate -a codex --prompt-file task.md
```

- Exact `-a <agent-id>` is mandatory: no default, globs, or multi-select.
- Delegate is full YOLO: no sandbox, approval prompts, or confirmation flag.
- Codex CLI, Claude Code, OpenCode, and native Grok Build support delegation.
- Gemini is review-only and is rejected by delegate.
- Delegate is steerable by default. Use `--one-shot` only for the legacy direct execution path.

## Steerable and detached runs

Delegate starts a long-lived single-agent session with a private filesystem mailbox by default. It prints `run_id=…` early on stderr. The final answer goes to stdout and is also served later by `delegate wait`. `--steerable` remains as an explicit compatibility alias.

```bash
scripts/consilium delegate -a grok "Implement the caching layer"
scripts/consilium delegate steer run_<id> --mode auto "Prefer Redis"
scripts/consilium delegate status run_<id> --json
scripts/consilium delegate watch run_<id>
scripts/consilium delegate wait run_<id>
scripts/consilium delegate cancel run_<id>
```

Use `--detach` when the run must outlive the calling process or be reattached from another session:

```bash
RUN_ID=$(scripts/consilium delegate -a grok --detach "Implement the task")
scripts/consilium delegate list --active
scripts/consilium delegate wait "$RUN_ID"
```

`--detach` uses the default steerable path, creates the registry entry required for reattachment, prints the run id on stdout, and returns immediately. The supervisor becomes its own session leader; caller `SIGINT`/`SIGHUP` cannot reach it. Supervisor stdio is stored in a private `supervisor.log`, but `wait` is the authoritative result interface. `--detach` and `--one-shot` are mutually exclusive.

## Required caller workflow

1. Start from the target project CWD. The default run is steerable and remains in the current session; use `--detach` when it may outlive the session. Recover a lost id with `delegate list --active`.
2. If `CONSILIUM_STEER_DIR` was overridden at start, pass the same value to `steer`, `status`, `cancel`, `wait`, `watch`, and `list`.
3. Steer only with new information or a genuine course correction. Do not repeat the original task. Prefer `--prompt-file` or stdin for long guidance and default to `--mode auto`.
4. The immediate `accepted` response proves only mailbox persistence. Query `status --json` once and inspect the matching `client_id` fields: `mailbox_status`, `delivery_class`, `backend_ack`, and `error`.
5. Use `watch` for supported lifecycle monitoring. It emits attach/status, steer lifecycle, selected turn-boundary/error events, heartbeats, and terminal state. It deliberately does **not** show the current tool, file, command, model text, reasoning, or a semantic percent-complete estimate. A heartbeat proves only that the supervisor still sees a live run.
6. Use `wait` to block and print the full final answer. `wait` never cancels work; only `cancel` does.

### Observation model

Keep these concepts separate:

| Concept / command | What it proves | What it does not prove |
|---|---|---|
| steerable run | Control commands can be accepted through the mailbox | Rich progress visibility or that a steer changed the work |
| `--detach` | The supervisor outlives the caller and the run can be reattached | More observability than a foreground steerable run |
| `status --json` | One point-in-time state snapshot; use once after steering to verify delivery fields | Ongoing progress; do not poll it as a monitor |
| `watch` | Supported lifecycle transitions, liveness heartbeats, and terminal state | Which tool/file is active, substantive progress, or final answer text |
| `wait` | Liveness heartbeats, terminal exit, and the complete final answer | Detailed lifecycle or substantive progress while the run is active |

For an observed detached run, use `watch RUN_ID`, then `wait RUN_ID` after
`watch` reaches terminal state. If only completion and the answer matter, call
`wait` directly. A `watch --timeout` exit of `75` means only that the observer
stopped; the worker continues and either command can be reattached later.

Do not tail or parse the private registry, `audit.jsonl`, `supervisor.log`, or
raw/normalized cache artifacts for routine progress. They are implementation
and diagnostic data, may contain per-chunk noise, and are not a richer public
progress contract. `watch` already filters lifecycle-bearing audit events. Do
not infer progress from partially written task artifacts unless the delegated
task explicitly defines those artifacts as checkpoints.

## Wait and watch exits

| Exit | Meaning |
|---|---|
| `0` | Completed |
| `130` | Cancelled |
| `70` | Supervisor died without finishing |
| `75` | Caller-specified timeout expired; the run continues and `wait` may be run again |
| `74` | Completed without answer text |
| other non-zero | Agent/backend failure |

## Steering modes

| Mode | Use when | Consequence |
|---|---|---|
| `auto` | Normal clarification, added constraint, or preferred direction | Safest native behavior available on the backend |
| `queue` | Current work may finish before guidance is applied | May affect only the next safe boundary; Grok uses a real next-turn FIFO entry |
| `interrupt` | Current direction is wrong and partial work should be abandoned | May cancel the active turn/tool flow; Claude rejects instead of silently downgrading |

For Grok, `auto`/`queue` is the productive default for additive guidance. Use `interrupt` only to replace direction because each later interrupt supersedes the prompt currently running, including an earlier steer.

## Mailbox lifecycle

| `mailbox_status` | Meaning |
|---|---|
| `accepted` | Persisted locally, not dispatched |
| `delivering` | Supervisor is calling the backend adapter |
| `request_sent` | Written to transport; no application evidence yet |
| `queued` | Accepted by backend but not observed running |
| `awaiting_queue_resolution` | Grok follower cancellation awaits authoritative queue evidence |
| `merged` | Grok combined this guidance into another running prompt |
| `running` | Correlated with an active prompt/turn; does not prove semantic effect |
| `completed` | Steer prompt ended normally; verify task artifacts/result |
| `incomplete` | Steer stopped at an output/token limit |
| `applied` | Backend directly acknowledged replay/injection; still verify task effects |
| `cancelled` | Steer started but was cancelled |
| `superseded` | A later Grok interrupt replaced it |
| `dropped` | A never-running Grok prompt was absent from later merge evidence |
| `abandoned` | Overall run ended before steer reached a protocol terminal state |
| `failed` / `rejected` | Steer did not complete normally; inspect backend evidence |

Never interpret `accepted`, `request_sent`, `queued`, or `running` as proof that guidance changed files or the final answer. `completed` proves prompt lifecycle completion, not semantic compliance.

## Retry-safe steering

```bash
scripts/consilium delegate steer run_<id> \
  --client-id requirement-cache-backend-v1 \
  --mode auto \
  --prompt-file steer.md
```

Retry a stable `client_id` only with identical content, mode, and kind. Any mismatch is an idempotency conflict. If the run or mailbox is terminal, start a new delegate with the remaining task instead of retrying. Client ids are SHA-256-mapped for paths; the original value remains in JSON.

Do not put secrets in tasks or steering guidance unless persistence in private raw/audit artifacts is intentional. Large task and guidance bodies travel through files or mailbox JSON, not large argv/env values.

## Registry and artifacts

The registry defaults below the user cache. Registry/run directories are `0700`, state files are `0600`, and symlink run directories are rejected. An active supervisor validates and can safely reconstruct missing or malformed owned registry metadata; unsafe ownership/symlink failures remain degraded instead of being overwritten.

Steerable runs always retain the private service registry and protocol artifacts required for steer/status/cancel, even when `CONSILIUM_SAVE_OUTPUTS=0` disables ordinary archival. Terminal transition serializes with enqueue so no accepted/delivering mailbox entry remains without a terminal outcome.

## Backend delivery matrix

| Backend | `auto` / `queue` | `interrupt` |
|---|---|---|
| Claude Code | `queue_next_turn` through stream-json user replay | Rejected; no downgrade |
| Codex CLI | `same_turn` through `turn/steer` and expected turn id | Abort active turn, wait for its completion acknowledgement, then start a prompt |
| OpenCode | `step_inject` through loopback HTTP/SSE `prompt_async` | Abort session then prompt |
| Grok Build | `queue_next_turn` through concurrent ACP prompt FIFO | Cancel-and-send using `sendNow` and its own prompt id |

OpenCode's server is loopback-only with redirect revalidation and per-run Basic auth; the password is never logged or stored. Claude's authoritative `result` completes the adapter even while stdin remains open; user replay proves transport acknowledgement, not semantic compliance. Codex interrupt uses a bounded local protocol handshake, not a run deadline.

Grok attribution uses prompt ids and queue snapshots. Combined followers move through `awaiting_queue_resolution` to `merged` or `dropped`; stop reasons map to `completed`, `incomplete`, `rejected`, `cancelled`, `superseded`, or `failed`. The adapter never claims `applied` because transport events cannot prove semantic compliance. Only agent message chunks contribute to final text; thoughts and replayed user messages do not.
