# Session history search and navigation

Read-only access to local coding-agent session histories. The reader streams
decoded records from the stores the harnesses already write — it creates no
index, no database, and no cache. Every emitted record carries a native locator
(file + line, or db + table + key) so any conclusion can be traced back to the
raw source.

Supported harnesses: `claude-code`, `codex` (CLI + Desktop), `opencode`,
`grok`, `devin` (CLI/Desktop), `gemini`, `cursor`, `claude-desktop`,
`qwen-code`, `kimi-code`, `omp`, plus `consilium` for this skill's own
delegate/review runs.

## Command surface

```bash
consilium sessions roots  [-a h1,h2] [--store SUBSTR]
consilium sessions list   [-a h1,h2] [--store S] [--cwd S] [--since T] [--until T] [--limit N]
consilium sessions grep   [-a h1,h2] [--scope S] [-i] [--regex] [--limit N] PATTERN
consilium sessions show   <harness:session-id> [--scope S] [--limit N]
consilium sessions show   <harness:session-id> --around SEQ [--context N]
consilium sessions show   --file PATH          # sniff a single file/db
```

`history` is an alias of `sessions`. All output is JSONL on stdout: session
headers (`_session`), fragments, and a final `_summary` record. Diagnostics go
to stderr; exit codes are 0 ok / 2 partial (some stores unavailable) / 70+ hard
failure.

## The navigation algorithm

Follow these steps in order. Each step narrows before the next one reads more
data — do not grep before you know which sessions exist.

1. **Discover stores** — `sessions roots`. Each store reports `status`
   (`ok`/`missing`/`empty`/`unavailable`) and `evidence` (`verified` =
   confirmed against a live install, `spec` = format documented but only
   fixture-verified, `guess` = best effort). Note which harnesses are absent;
   absence is a fact about the machine, not an error.
2. **List candidate sessions** — `sessions list`. Cheap metadata scan only:
   session id, title, cwd, created/updated, models. Filter with `--cwd`,
   `--since/--until`, `-a`, `--store`. Session ids are stable addresses —
   keep them verbatim for `show`.
3. **Search text** — `sessions grep PATTERN`. Runs over decoded fragment text
   (not raw bytes), honors the same filters. Each hit is a fragment with
   `kind`, `authorship`, `ts`, `model`, `seq`, and `locator`. Default
   `--scope convo` emits only `prompt` + `assistant` fragments; widen with
   `--scope all|tools|system|reasoning|prompts`.
4. **Read around a hit** — `sessions show <harness:id> --around SEQ --context N`.
   `seq` is the fragment's native sequence position within its session;
   `--context` emits N fragments on each side. This is how you see what a
   prompt answered, which tool call preceded a failure, or what the user saw.
5. **Open the raw record** — every fragment's `locator` points at the source:
   `{"file": ..., "line": N}` for JSONL stores, `{"db": ..., "table": ...,
   "key"/"row_id": ...}` for SQLite, `{"dir": ...}` for directory stores.
   When normalized classification is in doubt, read the raw record — it is
   the ground truth.
6. **Check coverage** — the `_summary` record reports `sessions_scanned`,
   `fragments_emitted`, `malformed_records`, `truncated_tail_files`,
   `unreadable_files`, `scan_complete`. If `scan_complete` is false or
   malformed counts are high, say so — an empty result under an incomplete
   scan means "not found in the readable part", not "does not exist".

### Finding "what the human actually asked"

```bash
consilium sessions grep --scope prompts --since 2026-01-01 "deploy"
```

`--scope prompts` emits only `kind=prompt` fragments. Within that set,
`authorship=human` marks genuine user input; `authorship=agent` marks
orchestrator-injected user-role records (task notifications, IDE context
blocks, `<system-reminder>` wrappers, environment bootstrap). The `basis`
field explains why the classifier decided as it did — quote it when the
distinction matters.

### Following branches, forks, and subagents

- `rel` on a fragment carries native link ids: `parent`, `uuid`, `sessionId`,
  `parent_node_id`, `parent_thread_id`, `subagent` — whatever the harness
  recorded. Collect these from `show` output to walk a tree.
- Session-level `parent` on `sessions list` output marks subagent/sidechain
  sessions where the harness records the linkage (opencode `parent_id`,
  claude `subagents/` transcripts, codex `thread_spawn_edges` +
  `source.subagent.thread_spawn`, claude-desktop `priorCliSessionIds` /
  `cliSessionId`).
- Forks and rewinds appear as repeated `sessionId`/`message_id` at different
  sequence positions (devin node forest, claude `parentUuid` chains). Treat
  the file order (`seq`) as the canonical timeline; reconstruct trees only
  when `rel` fields support it.

## Normalized fragment schema

Every emitted fragment:

| field | meaning |
|---|---|
| `harness`, `store`, `session_id` | provenance |
| `seq` | native sequence position (line order or row order) |
| `kind` | `prompt` / `assistant` / `reasoning` / `tool_call` / `tool_result` / `context` / `permission` / `compaction` / `boundary` / `metadata` / `unknown` |
| `authorship` | `human` / `agent` / `system` / `unknown` (omitted when `unknown`) |
| `native_type` | the record/part type as the harness named it |
| `locator` | `file`+`line`, `db`+`table`+`key`/`row_id`, or `dir` |
| `text` | decoded text, capped at `--max-chars` (`truncated: true` when capped) |
| `ts` | record timestamp, ISO-8601 |
| `model` | model id when the record carries one |
| `cwd` | session working directory when known |
| `visible` | false for internal/scratchpad records |
| `basis` | why the classifier chose `kind`/`authorship` |
| `rel` | native relationship ids (see above) |
| `status` | record status when meaningful (e.g. `stop`, `error`) |

`kind` and `authorship` are deliberately separate axes: a `kind=prompt`
record is user-*shaped*, while `authorship` says who actually wrote it.
Never infer authorship from `kind` alone — check `authorship` and `basis`.

## Per-harness store map and format recipes

### claude-code — `~/.claude/projects/<encoded-cwd>/**/*.jsonl` (+ `~/.claude/history.jsonl`)

- One JSON object per line. `type` ∈ `user`, `assistant`, `system`,
  `summary`, `file-history-snapshot`, …
- Genuine prompts: `type=user` with string `message.content`, or content
  blocks that are not `tool_result`. `origin.kind` may name the producer
  (`human`, `task-notification`, …); `isMeta=true` and `isSidechain=true`
  mark technical/subagent records — classify them `system`/technical, keep
  `authorship=agent` for orchestrator-injected user records.
- `parentUuid`/`uuid` chain gives conversation order; `sessionId` groups
  records; `subagents/` subdirectories hold sidechain transcripts whose
  `agentId`/`promptId` identify the subagent.
- Session id used by `show`: the file path relative to the project dir
  without `.jsonl` (e.g. `-Users-rodio/1f0e382c-…`); a bare uuid also
  resolves if unique.
- `history.jsonl` is a flat prompt log (`display` text + `project`), useful
  for prompt search without per-session context.

### codex — layered: canonical rollouts + state index + App/Desktop catalog

Codex stores the same threads in several layers with different authority.
`roots` shows them as separate stores; do not merge them mentally.

| store | path | authority |
|---|---|---|
| `sessions`, `archived` | `~/.codex/{sessions,archived_sessions}/YYYY/MM/DD/rollout-*.jsonl` | **canonical conversation body** |
| `state:state_N.sqlite` | `~/.codex/state_*.sqlite` | canonical thread index (all surfaces: CLI, VS Code, exec) |
| `catalog` | `~/.codex/sqlite/codex-dev.db` → `local_thread_catalog` | Desktop/sidebar catalog — includes `chatgpt` cloud threads with **no local transcript** |
| `summaries` | `~/.codex/sqlite/codex-thread-summaries-dev.db` → `thread_turn_summaries` | app-generated summaries, not messages |
| `history` | `~/.codex/history.jsonl` | flat prompt log `{session_id, ts, text}` |

- `threads` (state index): `rollout_path` links the index row to the
  canonical rollout file — `show` on a `state:*` session reads through to
  the rollout and emits real fragments. `first_user_message`, `preview`,
  `git_branch`, `archived`, `tokens_used`, `model`, `reasoning_effort`,
  `approval_mode`/`sandbox_policy` are index-level metadata.
- **Subagent lineage**: `threads.source` may be a JSON object
  `{"subagent": {"thread_spawn": {"parent_thread_id", "depth",
  "agent_nickname", "agent_path"}}}`; `thread_spawn_edges` maps
  parent→child. Both are surfaced as `parent`/`agent` on the session.
- `catalog` rows carry `source_kind` (`vscode`/`cli`/`exec`/`chatgpt`/
  subagent JSON), `host_id`, `missing_candidate`. ChatGPT-cloud and stale
  rows have **no local rollout** — `show` emits an `index_row` metadata
  fragment (`basis: "no local rollout file"`) plus the catalog/thread
  summary if one exists; it never fabricates a conversation.
- Rollout JSONL record types: `session_meta` (cwd, originator, cli_version,
  model_provider), `turn_context` (per-turn model/effort/approval policy),
  `response_item` (typed payload: message/reasoning/function_call/…),
  `event_msg` (user-facing events), `token_count` (cumulative usage — never
  sum across records), `compacted`/`turn_aborted` markers.
- **Genuine prompts come from `event_msg` with `user_message` payload**, or
  `response_item` `message` with `role=user` whose text is not bootstrap
  material. `response_item` user-role messages containing
  `<environment_context>`, AGENTS.md content, or tool schemas are bootstrap
  context — `kind=context`, `authorship=system`.
- Real-world files can contain corrupted interior lines (truncated records,
  binary spills) — counted as `malformed_records`, never silently skipped.
- `history` sessions are grouped prompt-log entries (`native_type
  history.entry`, `authorship=unknown`): useful for prompt search, not a
  transcript.

### opencode — `~/.local/share/opencode/opencode.db` + `storage/{session,message,part}/`

- SQLite `session` table: id, project_id, parent_id (subagent link),
  directory, title, agent, model, time_created/updated, token counters.
- Messages live in `message` (role on the message), content in `part`
  (type `text`/`tool`/`reasoning`/…, `message_id` foreign key). **A text
  part inherits its message's role** — never classify by part type alone.
- File-tree storage mirrors the same shape under `storage/` when the db is
  absent; both are read.

### grok — `~/.grok/sessions/<encoded-cwd>/<session-id>/`

- `summary.json`: session id, cwd, created/updated, generated title, model,
  reasoning effort, agent name, message counts.
- `chat_history.jsonl`: typed records — `system`, `user`, `reasoning`,
  `assistant`, `tool_result`, `backend_tool_call`. A `user` record whose
  text starts with `<system-reminder>` is technical context, not a prompt.
- `prompt_history.jsonl` is the clean prompt-only stream; `events.jsonl`,
  `updates.jsonl`, `terminal/` are auxiliary.

### devin — `~/.local/share/devin/cli/sessions.db` + `~/.local/share/devin/cli/transcripts/`

- `sessions` table: id (slug like `mature-band`), title, working_directory,
  model, agent_mode (`normal`/`accept-edits`/`bypass`), hidden flag,
  created/last_activity, `main_chain_id`.
- `message_nodes` table: a **node forest** — `node_id`/`parent_node_id`
  edges encode branches and rewinds; the same `message_id` may appear at
  several nodes. `role` ∈ `user`/`assistant`/`system`/`tool`; `seq` output
  order is node order.
- `transcripts/<id>.json`: ACP-style `{session_id, steps[]}` exports when
  present.
- Desktop/session UI state under `~/Library/Application Support/Devin` and
  `~/.devin` is not a transcript source.

### gemini — `~/.gemini/tmp/<project-hash>/chats/session-*.json`, `~/.gemini/projects.json`

- Whole-session JSON: `sessionId`, `messages[]` with `type`
  (`user`/`gemini`/`tool`/`info`), `model`, timestamps. `projects.json`
  maps project hash → cwd.

### cursor — `~/Library/Application Support/Cursor/User/{globalStorage,workspaceStorage/*/}state.vscdb`

- VS Code KV sqlite (`cursorDiskKV` table). Sessions are `composerData:<id>`
  keys: `name` (title), `createdAt`, `lastUpdatedAt`, `usageData` (per-model
  token counters).
- Message bodies are under `bubbleId:<composer>:<msg>` keys in the same db.
- Workspace path: `workspaceIdentifier.uri.fsPath` in `composerHeaders`
  when present, else `workspace.json` next to the workspace `state.vscdb`.

### claude-desktop — two layers: `cowork` + `code-sessions`

`~/Library/Application Support/Claude/` holds two unrelated session trees.

**`cowork`** — `local-agent-mode-sessions/<org>/<user>/local_<id>{.json,/}`:

- `local_<id>.json` is the session manifest: `title`, `cwd`, `model`,
  `effort`, `permissionMode`, `isArchived`, `createdAt`/`lastActivityAt`,
  and **`initialMessage` — the user's first message, always emitted as a
  `prompt` fragment with `authorship=human`**.
- `local_<id>/audit.jsonl` is the canonical Cowork record: append-only,
  HMAC-chained (`.audit-key` sibling — **never read it**). Record types:
  `user`/`assistant` messages (same taxonomy as claude-code), `system`
  `init`/`permission_request`/`permission_response` (→ `metadata`/
  `permission`), `result` (turn boundary with usage → `boundary`),
  `rate_limit_event` (→ `metadata`). `parent_tool_use_id` marks subagent
  records → `authorship=agent`.
- The audit log **re-emits the triggering user message after each `init`
  boundary** — duplicates across turns are the format's own bookkeeping,
  not reader noise.
- `local_<id>/.claude/projects/**` are inner claude-code subprocess
  transcripts — signposted as `inner_transcript` metadata, never scanned
  twice (they are not under `~/.claude/projects`).

**`code-sessions`** — `claude-code-sessions/**/local_<id>.json`:

- Desktop metadata for the embedded code tab: `sessionId`, **`cliSessionId`
  → the link to the canonical transcript** at
  `~/.claude/projects/<encoded-cwd>/<cliSessionId>.jsonl`, plus
  `priorCliSessionIds` (session continuation chain), `title`,
  `permissionMode`, `enabledMcpTools`, `completedTurns`, `isArchived`.
- `show` emits the manifest as `metadata`, then delegates to the linked
  claude-code transcript (fragments keep `harness=claude-desktop` and carry
  `rel.cli_session_id`). Missing transcript → explicit `cli_transcript`
  metadata fragment (`basis: "cliSessionId has no transcript"`), never
  silent.

### qwen-code — `~/.qwen/projects/<encoded-cwd>/chats/*.jsonl` (+ `subagents/`)

- Claude-code-like JSONL; content arrives as `message.parts[]` with typed
  parts including `functionResponse` (tool results — classify
  `tool_result`, not prompt). `subagents/<sid>/agent-*.jsonl` hold sidechain
  transcripts.

### kimi-code — `~/.kimi-code/sessions/<encoded-cwd>/<session-id>/` + `session_index.jsonl`

- Per-session directory; records typed `turn.prompt`, `turn.steer`,
  `context.append_loop_event`, etc. `session_index.jsonl` is a fast
  title/time index.

### omp — `~/.omp/agent/sessions/**/*.jsonl`

- Generic JSONL transcripts; conservative fallback classification applies.

### consilium — `$CONSILIUM_STEER_DIR/runs/<run-id>/` (default `~/Library/Caches/agents-consilium/steer/runs/`)

- `meta.json`: agent_id, backend, model, effort, cwd, status, timestamps,
  `native_session` linkage (e.g. codex thread id for `--persist-session`
  runs — joinable to `codex:` sessions).
- `events.jsonl`: normalized event stream emitted by the run; raw provider
  output under `raw/`.

## Classification contract

| `kind` | assigned to |
|---|---|
| `prompt` | user-role content (human or orchestrator-injected — see `authorship`) |
| `assistant` | model-visible reply text |
| `reasoning` | model thinking / chain-of-thought blocks |
| `tool_call` | tool/function invocations |
| `tool_result` | tool/function outputs, including function responses |
| `context` | system prompts, bootstrap/environment blocks, reminders |
| `permission` | permission-mode changes, auto-approve, guardian assessments |
| `compaction` | history compaction records |
| `boundary` | turn/step boundaries, task lifecycle events |
| `metadata` | titles, bookkeeping, session_meta, usage snapshots |
| `unknown` | unrecognized but preserved records |

| `authorship` | assigned to |
|---|---|
| `human` | genuine user keystrokes/pastes |
| `agent` | orchestrator-injected user-role content (task notifications, IDE context, sidechain prompts) and model output |
| `system` | harness bootstrap, system prompts, reminders, tool-produced output |
| `unknown` | insufficient evidence |

Rules:

- Authorship is never guessed from `kind`. When uncertain, `authorship` is
  omitted or `unknown`, and `basis` records the deciding evidence.
- Technical content is never discarded — it is classified
  `context`/`tool_call`/`tool_result`/`metadata` with `visible=false` where
  appropriate and excluded only by scope filters.
- Malformed lines (undecodable JSON, binary spills, truncated tails) are
  counted in `_summary.malformed_records` / `truncated_tail_files`, not
  dropped silently.
- Usage/token records are cumulative snapshots — report latest value, never
  sum.

## Safety contract

- Pure read: sqlite opened `mode=ro` (never `immutable=1` on live dbs — WAL
  state matters), files only opened for reading, nothing written anywhere.
- `sessions` never prints record content beyond `--max-chars` per fragment;
  use `show --file`/`--around` deliberately rather than bulk-dumping whole
  histories — sessions may contain secrets pasted by the user.
- Do not pipe `sessions` output into files committed to a repository.
