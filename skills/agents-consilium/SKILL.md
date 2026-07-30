---
name: agents-consilium
description: "Query external AI agents (Codex, Claude Code, OpenCode, native Grok Build, Gemini) for independent second opinions, multi-depth code review, repository context exploration, and full-YOLO single-agent delegation. Three public modes via scripts/consilium: review (read-only ask/code), explore (read-only exploration of a local or remote repository — clones remotes, answers from cited evidence, Grok 4.5 by default), and delegate (exact agent, no sandbox; optional --steerable long session with steer/status/cancel, plus --detach to outlive the caller and wait/watch/list to block on, follow, or rediscover a run). Use for architecture choices, security review, deep multi-stage review, understanding an unfamiliar or third-party codebase, handing a whole task to one agent, or waiting on a delegated agent that was started earlier. Not for simple questions answerable from docs or the codebase."
---

# Consilium v6: Multi-Agent Review, Exploration & Delegation

Query external AI agents for independent expert opinions, structured code review, repository exploration, or full-YOLO task delegation. Review and explore stay read-only. Delegate hands the whole task to **exactly one** explicitly selected agent in the caller's CWD.

## Public CLI (only entrypoint)

```bash
scripts/consilium review ask [...]
scripts/consilium review code --depth basic|specialists|super|ultra [...]
scripts/consilium explore [--repo SOURCE] [--ref REF] [...]
scripts/consilium delegate -a <exact-agent-id> [...]
scripts/consilium delegate -a <exact-agent-id> --steerable [...]
scripts/consilium delegate -a <exact-agent-id> --detach [...]
scripts/consilium delegate steer RUN_ID [--mode auto|queue|interrupt] [...]
scripts/consilium delegate status RUN_ID [--json]
scripts/consilium delegate cancel RUN_ID
scripts/consilium delegate wait RUN_ID [--timeout SEC] [--json] [--quiet]
scripts/consilium delegate watch RUN_ID [--timeout SEC] [--heartbeat SEC] [--json]
scripts/consilium delegate list [--active|--all] [--reap] [--json]
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
| `explore` | read-only | One agent maps the context a question depends on |
| `delegate -a <id>` | **full YOLO** | One agent implements the task in CWD |

Review and explore are different jobs, not two depths of one job:

```
review    finds and validates problems in code you already own
explore   builds a relevance-first map of context and answers from evidence
delegate  changes the repository
```

`explore` never loads review principles, review roles, `review_instructions`, or the Assessment/Blind Spots/Recommendation template. Asking it to review is a category error — use `review` for that.

### `review ask`

```bash
scripts/consilium review ask "Should we use Postgres or SQLite?"
scripts/consilium review ask --xml --prompt-file prompt.md
scripts/consilium review ask -a codex,grok "Review this approach"
scripts/consilium review ask -a 'opencode-go-*' -x opencode-go-minimax "Q"
scripts/consilium review ask --progress compact -a codex,grok "Q"   # quiet, still live
scripts/consilium --list-agents
```

Each agent answers under its own heading; consilium does not merge or rank them — you are the judge.

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

### `explore`

Read-only exploration of a repository's context — local tree or remote repo — answering a question from cited evidence. Single agent, **Grok 4.5 by default**.

```bash
# current directory
scripts/consilium explore "How is authentication wired up?"

# another local repository
scripts/consilium explore --repo ~/src/app "Where is the public API assembled?"

# remote; bare owner/repo means GitHub
scripts/consilium explore --repo owner/repository "What handles incremental builds?"

# pinned to a branch, tag, or commit
scripts/consilium explore --repo https://github.com/owner/repository --ref v2.4.0 \
  "How does the middleware pipeline work?"

scripts/consilium explore --repo owner/repository --prompt-file question.md
```

| Option | Meaning |
|--------|---------|
| `--repo SOURCE` | Local path, `owner/repo` (GitHub), or git URL. Default `.` |
| `--ref REF` | Branch, tag, or commit — **remote sources only** |
| `-a, --agent ID` | Exact agent id, no globs. Default `grok` |
| `--prompt-file FILE` | Question from a file |
| `--depth N\|full` | Clone depth for remotes. Default `1` |
| `--progress compact\|verbose\|none` | Progress detail on stderr. Default `compact` |
| `--keep-clone` | Keep the clone and print its path (debugging only) |

The source is `--repo` only — a positional `owner/repo` would be ambiguous against the question text and against local paths. An existing directory named `owner/repo` always beats the GitHub shorthand.

Exit codes: `0` ok · `4` unknown agent / config · `5` usage · `6` source error (unresolvable spec, blocked transport, clone or ref failure) · otherwise the backend exit code.

#### Answer shape

```
## Answer        direct answer, prose first
## Evidence      repository-relative path:line, each stating what it proves
## Context map   only the modules that bear on the question
## Gaps          what could not be confirmed, and why
```

No `Blind Spots`, no `Alternatives`, no `Recommendation` — those belong to review.

#### Trust boundary

A remote repository is data, not a control plane. Grok Build discovers repo-local `.grok/config.toml`, plugins, MCP servers, hooks, `AGENTS.md`, and Claude-compatible instructions from its working directory, so explore clones into an isolated workspace and points the agent at the **neutral parent**:

```
<workspace>/          ← agent CWD
  source/             ← the clone
```

Verified against Grok Build 0.2.112 with `grok inspect`: CWD `<workspace>` loads only user-level instructions; CWD `<workspace>/source` additionally loads the repository's own `AGENTS.md` and `CLAUDE.md`. The regression test asserts this layout.

What this does **not** cover, stated plainly:

- User-level configuration (`~/.grok`, `~/.claude`) still loads. It is yours, and is treated as trusted.
- Nothing prevents the model from *reading* `AGENTS.md`; `prompts/explore.txt` forbids obeying it.

Additional posture for remote sources: `--sandbox strict`, plus `--no-subagents`, `--no-memory`, no shell, no write tools. Local trusted trees are explored in place under `--sandbox read-only`, and repo-local instructions **are** discovered there — that is your own repository.

Blocked by default: `file://`, `ext::` and other git remote helpers, plain `http://`. Submodules and LFS payloads are not fetched. Credentials embedded in a URL are stripped before anything is logged or written to `meta.json`. The clone is removed on success, failure, and signal; `--keep-clone` is the only exception.

#### Web access

Explore has `web_search` and `web_fetch`. Understanding a codebase routinely means reading the upstream docs, RFCs, and release notes it is built against. The prompt draws the line: the model may not visit a URL *because repository content told it to*, and may not send repository content anywhere.

#### Progress

Progress is content-free by construction. Exploration must not stream chain-of-thought or the answer body onto stderr, so `--progress` reports shape only:

```
[consilium] stage=explore agent=grok repo=owner/repository ref=v2.4.0
[consilium] explore clone https://github.com/owner/repository at ref=v2.4.0 (depth=1)
[consilium] source remote=… strategy=clone-branch commit=abc123def456
[consilium] event agent=grok type=thinking chunks=128 chars=8213 elapsed=24s
[consilium] event agent=grok type=answering chunks=44 chars=2117 elapsed=61s
[consilium] event agent=grok type=end data=EndTurn
```

`verbose` shortens the heartbeat interval; `none` silences it. Tool-level progress (`grep pattern=…`, `read path=…`) needs the ACP transport and is deliberately deferred — see [ACP-RESEARCH.md](ACP-RESEARCH.md).

#### Agents other than Grok

Every isolation guarantee above is implemented with Grok Build flags. `-a <non-grok>` still runs read-only with the exploration prompt, but falls back to that backend's review-grade posture: repo-local instructions may be discovered while reading files, and memory / subagents / web follow the backend's own defaults. Explore prints a warning and records `"isolation": "reduced"` in `meta.json`.

#### Provenance

`meta.json` records mode, agent, backend, isolation level, source kind, **redacted** source URL, requested ref, resolved commit, branch, shallow/dirty flags, clone depth and strategy, caller CWD, exploration root, agent CWD, inventory size, and the question's SHA-256.

Because explore has no shell, the orchestrator collects git facts (`rev-parse`, `log`, `status`) and a bounded file inventory (`git ls-files`, or a filtered walk for non-git trees) and passes them into the prompt as stated facts. Large repositories get a directory-level rollup that is explicitly labelled as incomplete rather than a silently truncated file list.

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

Long-lived single-agent session with a filesystem mailbox. Prints `run_id=…` early on stderr; final answer still goes to stdout when the run completes, and is also served by `delegate wait` from `<run_dir>/final.txt`.

```bash
scripts/consilium delegate -a grok --steerable "Implement the caching layer"
# other terminal / later:
scripts/consilium delegate steer run_<id> --mode auto "Prefer Redis over memcached"
scripts/consilium delegate status run_<id> --json
scripts/consilium delegate cancel run_<id>
scripts/consilium delegate wait run_<id>
```

#### Required workflow for the calling agent

1. **Start** from the target project CWD, either way:

   ```bash
   RUN_ID=$(scripts/consilium delegate -a grok --detach "Implement the caching layer")
   ```

   or start with `--steerable` under your harness's background execution and
   read `run_id=run_<id>` off early stderr. Lost the id? `delegate list --active`.
2. If `CONSILIUM_STEER_DIR` was overridden at start, pass the same environment
   value to every later `steer`, `status`, `cancel`, `wait`, `watch`, and `list`.
3. **Steer** only with new information or a clear course correction — never
   repeat the original task. Use `--prompt-file` or stdin for long guidance, and
   `--mode auto` unless the user explicitly needs different semantics. Record the
   returned `client_id` and `seq`. For Grok, `auto`/`queue` is the productive
   default for additive details; use `interrupt` only to replace the current
   direction, since every later `interrupt` supersedes the prompt currently
   running, including an earlier steer. The immediate `accepted` response means
   mailbox persistence only — query `delegate status RUN_ID --json` once
   afterwards and inspect `mailbox_status`, `delivery_class`, `backend_ack`, and
   `error` for the matching `client_id`. Later backend events may advance a steer
   from `request_sent`/`queued` to `running` and `completed`, or end it as
   `cancelled`, `dropped`, `failed`, or `rejected`.
4. **Observe** with `delegate watch RUN_ID` when the user wants live visibility.
   It emits one line per meaningful change (status transitions, steer delivery,
   turn boundaries, errors) and exits on its own at the terminal status. Per-chunk
   model text is deliberately excluded. Skip this entirely if only the result
   matters — do not poll `status` in a loop.
5. **Collect** with `delegate wait RUN_ID [--timeout SEC]`. It blocks until the
   run is terminal and prints the **full** final answer on stdout.

| `wait` / `watch` exit | Meaning |
|---|---|
| `0` | completed |
| `130` | cancelled |
| `70` | the supervisor died without finishing |
| `75` | **your** `--timeout` expired — the run continues; re-run `wait` |
| `74` | completed but produced no answer text |
| other non-zero | the agent's own failure code |

`wait` never cancels anything. `cancel` remains the only way to stop actual work.

#### `--detach` vs. running it in the background yourself

| Situation | Use |
|---|---|
| The run should finish inside this session, and you want its stderr in the transcript | your harness's background execution + `--steerable` |
| The run may outlive the session, the run id goes to another session/agent, or you want to reattach later | `--detach` |

`--detach` implies `--steerable` (a registry entry is required to reattach),
prints `run_id` on stdout and returns immediately. The supervisor calls
`setsid`, so a `SIGINT`/`SIGHUP` aimed at the caller's process group cannot
reach the run. Its stdio lands in `<run_dir>/supervisor.log` (0600), but that
log is not the contract — `wait` serves the authoritative answer.

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
| `awaiting_queue_resolution` | Grok returned Cancelled for a never-observed-running prompt; wait for the authoritative next queue snapshot before deciding merged vs dropped |
| `merged` | Grok combined this steer text into another running prompt; keep observing that linked prompt |
| `running` | The backend correlated the steer with an active prompt/turn; this does **not** prove the requested effect happened |
| `completed` | That steer prompt ended without a cancellation/error stop reason; verify artifacts/result for semantic compliance |
| `incomplete` | Grok stopped the steer at a token limit; its requested work may be partial |
| `applied` | A backend with a direct replay/injection acknowledgement confirmed receipt; still verify task effects when they matter |
| `cancelled` | The steer turn started but was cancelled, commonly by a later `interrupt`; do not assume its requested work happened |
| `superseded` | A later Grok `interrupt` (`sendNow`) intentionally replaced this steer; inspect `superseded_by_prompt_id` |
| `dropped` | Grok removed a never-observed-running prompt and later queue evidence did not show a merge |
| `abandoned` | The overall delegate run ended before this steer produced a terminal protocol outcome |
| `failed` / `rejected` | The steer did not complete normally; inspect `error` / `backend_ack` and decide whether to retry or start a new run |

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
- **Mailbox `accepted` ≠ protocol delivery, execution, or compliance.** `status` shows `delivery_class` and backend evidence separately.
- Protocol lifecycle is backend-specific. Never reinterpret `request_sent`, `queued`, or `running` as proof that guidance changed files or the final answer. `completed` proves prompt lifecycle completion, not semantic compliance.
- Registry root: `CONSILIUM_STEER_DIR` (default under user cache). Permissions: registry/run dirs `0700`, state files `0600`. Symlink run dirs are rejected.
- An active supervisor periodically validates its registry independently of model output. If its own run metadata is deleted or malformed, it safely rebuilds the private run structure, emits `registry_recovered`, and keeps the harness running. Unsafe symlink/ownership failures remain degraded instead of being overwritten; they cannot suppress the model's final stdout, and final artifacts are attempted before service-state finalization.
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

Grok steerable uses native ACP `grok agent stdio` concurrent prompt queue semantics (not same-turn injection, not external holding of prompts until first completion). Attribution uses `_meta.promptId` on notifications and `x.ai/session/prompt_complete` / `_x.ai/session/prompt_complete`, plus `_x.ai/queue/changed` (`entries[].id`, `runningPromptId`, `runningCombinedTexts`). Writing a concurrent `session/prompt` is `request_sent`/`queued`; `runningPromptId` or prompt-attributed updates advance it only to `running`. When Grok combines a queued follower into another prompt, consilium reports `merged`, links `merged_into_prompt_id`, and follows the front prompt to a terminal outcome. Grok deliberately returns a Cancelled RPC for a combined follower before its authoritative `runningCombinedTexts` broadcast, so consilium first reports `awaiting_queue_resolution`; the next queue snapshot resolves that state to `merged` or `dropped`. `end_turn` becomes `completed`; `max_tokens` becomes `incomplete`; refusal becomes `rejected`; a normal cancellation becomes `cancelled`; `cancelTrigger=send_now` becomes `superseded` and links `superseded_by_prompt_id`; `error`, `rate_limit`, and unknown stop reasons become `failed`. Grok transport events cannot prove that the model semantically obeyed guidance, so the Grok adapter never claims `applied`. `steer()` itself never waits on Grok: it returns transport state immediately so the supervisor can accept more guidance and stream/reconcile lifecycle events. Terminal outcomes cannot be overwritten by late weaker acknowledgements except the evidence-backed refinement `cancelled → superseded`. If the whole run ends while a steer is still lifecycle-open, it becomes `abandoned` instead of remaining stuck. Only `agent_message_chunk` (and confirmed aliases) contributes to final text; `agent_thought_chunk` is progress/thought only; `user_message_chunk` is replay only.

Codex interrupt uses a **local protocol-ack wait** (bounded handshake for the interrupted turn's `turn/completed`) — not a global run timeout. Ordinary `turn/completed` with status `completed` ends this delegate run (not a permanent idle session).

Claude authoritative `result` events complete the adapter even if stdin remains open; stderr is always drained. Same-turn steers remain possible until that result.

## Observability contract

| Stream | Content |
|--------|---------|
| **stderr** | Compact semantic **live** progress (`[consilium] start|event|done|stage …`) while the model is still running — not post-hoc after completion. Style is selectable per run — see below |
| **stdout** | Clean final answer only |
| **artifacts** | Per-run dir under `CONSILIUM_OUTPUT_DIR` (or `CONSILIUM_RUN_DIR`): `raw/*.jsonl`, `normalized/*.jsonl`, `final/*.txt`, `final.txt`. Keys are per-invocation: plain agent id for ask/delegate, `agent.role` for basic/specialists code review, explicit stage/index keys for super/ultra discovery (`<stage>.<index>.<agent>.<role>`), and `judge.primary.<agent>` / `judge.fallback.<agent>` for judge attempts. Fan-out never relies on ambient inherited `CONSILIUM_ARTIFACT_KEY` alone. |

Architecture: `backend_cmd | normalize_stream.py --raw-out --progress --extract-text`. Each raw line is persisted and normalized immediately; progress reaches stderr before process completion. `PIPESTATUS` preserves backend exit (timeout/signal) and Grok end/error validation independently.

### Progress styles

`review ask` and every `review code` depth take `--progress` (env fallback `CONSILIUM_PROGRESS`):

| Style | stderr carries |
|-------|----------------|
| `full` (default) | Per-agent thinking / answer previews, live |
| `compact` | Content-free liveness only: `chunks=N chars=M elapsed=Ts` |
| `none` | Nothing. Stage lines, per-pass `ok`, and model progress are all silenced; failures and the report itself are not |

`explore` keeps its own vocabulary (`compact` / `verbose` / `none`) and never offers `full` — exploration must not stream chain-of-thought or the answer body.

Progress lines are keyed by the **invocation**, not the agent: `agent=codex` for `ask`, `agent=codex.security` for a code-review pass, `agent=discovery-small.0.opencode-go-glm.correctness` for super/ultra fan-out. Two concurrent passes of the same agent therefore stay distinguishable while they run, and each key matches its artifact file under the run dir.

The skill never synthesizes a verdict for `ask`, `basic`, or `specialists`: every agent's answer is returned verbatim under its own heading and the calling agent judges. (`super` / `ultra` are the deliberate exception — they run an explicit LLM judge stage over the deduped union.)

### Run identifiers

Run ids and run-dir names are human-readable word pairs — `run_amber-otter-4f21`, `run-ask-solar-orchid-fd8e` — not raw hex. They are quoted back on stderr, retyped into `delegate status <run_id>`, and referenced several turns later, all of which words survive and UUIDs do not. The 4-hex tail keeps them unique; `scripts/lib/human_id.py` is the single generator for both the steerable registry and artifact directories.

Disable ordinary review/delegate archival with `CONSILIUM_SAVE_OUTPUTS=0`. Steerable runs still maintain their service registry (`CONSILIUM_STEER_DIR`) and protocol artifacts needed for steer/status/cancel observability.

`delegate list` enumerates that registry, newest first, and is the recovery path when a run id was lost. It is read-only by default: a run whose supervisor died still shows its stored `status` alongside `effective_status: "stale"`. Only `--reap` rewrites those to `failed` / `supervisor_dead`. `wait` and `watch` perform the same reaping for the single run they are attached to, which is why neither can hang on a dead supervisor.

## Resource-limit contract

Consilium is unlimited by default:

- no wrapper timeout (`AGENT_TIMEOUT=0`);
- no `max-turns`, step, token, response-length, or budget flags;
- prompts travel over stdin or a temporary prompt file, never as large argv values;
- delegate reads file/stdin/`/dev/stdin` task sources exactly once into a private temporary file, so pseudo-files and non-seekable streams work in both one-shot and steerable modes;
- raw, normalized, and final artifacts are not truncated;
- final text is streamed to disk rather than buffered as one in-memory response.

Provider context windows, model output limits, and limits in user/managed harness
configuration still apply. To add an explicit watchdog for an ordinary review
or one-shot delegate invocation, set `AGENT_TIMEOUT` to a positive number of
seconds. Steerable runs intentionally have no wrapper deadline; observe them
with `status` and stop them explicitly with `cancel`.

## Backends & read-only / YOLO flags

| Backend | Review / explore (read-only) | Delegate (YOLO) |
|---------|-----------------------------|-----------------|
| `codex-cli` | `exec --sandbox read-only` + ask-for-approval never | `--dangerously-bypass-approvals-and-sandbox` |
| `claude-code` | `--permission-mode plan` + disallowed Edit/Write | `--dangerously-skip-permissions` |
| `opencode` | `--agent plan` | `--agent build --auto` |
| `grok-build` | `--sandbox read-only` + tool allowlist/denylist (plan alone is **not** read-only) | `--always-approve`, no sandbox |
| `gemini-cli` | `--approval-mode plan` | not supported |

**Web research is on in every read-only mode.** Reviewing and exploring both depend on checking a CVE, an upstream API contract, a spec, or a release note. The two backends that needed help now get it explicitly:

| Backend | Web in review/explore | How |
|---------|----------------------|-----|
| `codex-cli` | already available | default under `--sandbox read-only` |
| `opencode` | already available | default in the `plan` agent |
| `grok-build` | **added** | `web_search,web_fetch` in the `--tools` allowlist — the allowlist is exhaustive, so omitting them removed web access entirely |
| `claude-code` | **added** | `--allowedTools "WebSearch,WebFetch"` — `plan` alone leaves them unapproved, and a headless run cannot answer the permission prompt |
| `gemini-cli` | built-in `google_web_search` | unchanged |

`--allowedTools` pre-approves; it does not restrict. Read/Grep/Glob remain available, and `--disallowedTools Edit,Write,NotebookEdit` still wins. Verified against Grok Build 0.2.112 and Claude Code 2.1.220 by probing each backend in its exact production argv.

Read-only enforcement is driven by an access policy (`review` and `explore` → `readonly`, `delegate` → `yolo`), not by a literal mode comparison — a new read-only mode cannot accidentally inherit YOLO argv. `explore` additionally layers Grok-only isolation flags (`--cwd`, `--sandbox strict` for remote clones, `--no-subagents`, `--no-memory`) and grants `web_search` / `web_fetch`.

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
| `review_instructions` | Optional model-specific instructions appended to non-raw review prompts only |
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
| Understand an unfamiliar or third-party codebase | `explore --repo <source>` |
| "Where/how does X work here?" | `explore` |
| Architecture / brainstorm | `review ask` |
| Quick file/diff review | `review code` (basic) |
| High-stakes PR file | `review code --depth specialists` or `super` |
| Max coverage | `review code --depth ultra` |
| “Just implement this” with one agent | `delegate -a <id>` |
| Delegate while retaining the ability to redirect it mid-run | `delegate -a <id> --steerable` |
| Delegate something that may outlive this session | `delegate -a <id> --detach` |
| Block until a delegated run finishes and take its answer | `delegate wait <run_id>` |
| Follow a delegated run's progress without polling | `delegate watch <run_id>` |
| Reattach to a run started earlier / find a lost run id | `delegate list --active` |

## Environment variables

- `CONSILIUM_CONFIG`, `CONSILIUM_AGENTS`, `CONSILIUM_EXCLUDE`
- `CONSILIUM_PROGRESS` — default progress style for review modes (`full` | `compact` | `none`)
- `CONSILIUM_OUTPUT_DIR`, `CONSILIUM_RUN_DIR`, `CONSILIUM_SAVE_OUTPUTS`
- `CONSILIUM_STEER_DIR` — registry root for steerable runs; must be passed identically to `steer`, `status`, `cancel`, `wait`, `watch`, and `list`
- `CONSILIUM_DETACH_START_TIMEOUT` — seconds `--detach` waits for the supervisor to report a run id (default `30`)
- `CONSILIUM_EXPLORE_ALLOW_LOCAL_REMOTE=1` — permit `file://` sources (offline tests only; blocked in normal use)
- `CONSILIUM_EXPLORE_ALLOW_INSECURE=1` — permit plain `http://` clone URLs
- `AGENT_TIMEOUT` (`0`/unset = unlimited; positive integer = opt-in seconds for ordinary review/one-shot delegate; steerable remains unlimited)
- Per-backend: `CODEX_MODEL` / `CODEX_EFFORT`, `CLAUDE_MODEL` / `CLAUDE_EFFORT`, `OPENCODE_MODEL` / `OPENCODE_EFFORT`, `GROK_MODEL` / `GROK_EFFORT`, `GEMINI_MODEL`, `GEMINI_API_KEY`. Non-empty model/effort variables override `config.json` for that invocation in both ordinary and steerable modes. OpenCode effort maps to its model `variant`; use `none` to omit the variant consistently.

## Tests

```bash
scripts/tests/run.sh
```

Uses fake backend CLIs; asserts argv safety (review/explore sandboxes vs delegate YOLO), exact agent selection, stdout/stderr separation, artifacts, Grok streaming-json success/failure, live progress before backend exit, explore source resolution (local / shorthand / URL / SSH, shorthand-vs-existing-directory precedence, credential redaction, blocked transports, branch/tag/SHA refs, clone cleanup on success, failure, and `--keep-clone`, isolation argv, prompt purity, and content-free progress), review progress styles (`full` / `compact` / `none` across every depth, per-invocation progress keys, human-readable run ids and run dirs), and steerable-delegate mailbox/adapters (Claude/Codex/OpenCode/Grok transport fakes, concurrent Grok queue + sendNow, cancel, idempotency, cleanup). Default suite is offline — no network/model spend.

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
