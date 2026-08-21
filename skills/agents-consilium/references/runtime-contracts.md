# Runtime contracts

Use this reference when diagnosing or changing observability, normalized events, backend capability resolution, access policy, workflow fan-out, prompt composition, artifacts, or run identity.

## Contents

- Streams, artifacts, and the closed event schema
- Debug event tape
- Shared backend and mode capability contracts
- Declarative workflow plans and layered prompts
- Progress, identifiers, and resource limits
- Native Grok one-shot contract

## Streams and artifacts

| Stream | Contract |
|---|---|
| stderr | Mode-specific progress for foreground commands; this is not a promise of tool/file visibility for steerable delegation |
| stdout | Clean final answer only |
| artifacts | Per-run `raw/*.jsonl`, `normalized/*.jsonl`, `final/*.txt`, and `final.txt` under `CONSILIUM_OUTPUT_DIR` or `CONSILIUM_RUN_DIR` |

Artifact keys are per invocation: profile id for ask/delegate, `agent.role` for basic/specialist review, `<stage>.<index>.<agent>.<role>` for super/ultra discovery, and `judge.primary.<agent>` / `judge.fallback.<agent>` for judge attempts. Fan-out never relies only on inherited `CONSILIUM_ARTIFACT_KEY`.

One-shot architecture remains `backend_cmd | normalize_stream.py --raw-out --progress --extract-text`. Raw lines are persisted and normalized immediately. `PIPESTATUS` preserves backend exit and Grok end/error validation independently.

## Closed event schema

`scripts/lib/events.py` defines the closed `ConsiliumEvent` type set shared by one-shot normalization and steerable persistence. Unknown event types are rejected rather than silently written. Original backend payloads may be retained under `raw`.

| Type | Purpose |
|---|---|
| `run_started` | Normalizer/session start |
| `thinking_delta` | Thought streams |
| `answer_delta` | Answer/message deltas |
| `result` | Authoritative complete answer, especially Claude |
| `tool_started`, `tool_completed` | Tool lifecycle |
| `retry_scheduled` | Retry hint |
| `steer_*` | Steerable lifecycle |
| `run_completed`, `run_failed` | Terminal event |
| `progress`, `user_replay`, `turn_*`, `prompt_complete` | Structural observability |

Live stderr keeps the human vocabulary `thought`, `text`, `end`, and `error`. Final-text assembly prefers `result` over concatenated answer deltas. Thinking and tool events never contribute.

## Debug event tape

The opt-in tape records bounded, sequence-numbered JSONL across RAW → PARSED → NORMALIZED → RENDERED → FINAL without leaking event bodies onto normal stderr.

```bash
CONSILIUM_DEBUG_EVENTS=1 "$CONSILIUM" review ask "Q"
CONSILIUM_DEBUG_EVENTS_PATH=/tmp/tape.jsonl
CONSILIUM_DEBUG_EVENTS_MAX=10000
CONSILIUM_DEBUG_EVENTS_MAX_BYTES=33554432
```

One-shot normalization records all stages; the steerable supervisor records normalized adapter events. Overflow, dropped, and gap counts are reported on close instead of being hidden.

## Shared backend contract

`scripts/lib/backend_contract.py` resolves profile identity, binary, model/effort including environment overrides, and real capability differences: steering delivery class, interrupt support, concurrent queues, transport, and final-text assembly. Both `backend_run.sh` and steerable `config_loader.py` use it.

## Mode capability policy

`scripts/lib/mode_policy.py` derives access from an explicit capability matrix covering filesystem, shell, web, memory, subagents, steering, and interrupt. Review is read-only; delegate/delegate-steerable are YOLO. Unknown modes fail closed. Backend safety flags layer on top.

| Backend | Review | Delegate |
|---|---|---|
| Codex CLI | `--search`, `exec --sandbox read-only`, ask-for-approval never, multi-agent disabled | `--dangerously-bypass-approvals-and-sandbox` |
| Claude Code | `dontAsk`, safe mode, no session/Chrome, Edit/Write/Agent/Task denied, Bash + web enabled | `--dangerously-skip-permissions` |
| OpenCode | runtime `consilium-review` primary agent with its own work-alone prompt: full diagnostics, edit/task denied | `--agent build --auto` |
| Grok Build | `--no-plan`, read-only sandbox, terminal enabled, subagents disabled | `--always-approve`, no sandbox |
| Gemini CLI | `--approval-mode yolo`, extensions/MCP/subagents disabled; report-only prompt contract | unsupported |

Web research is available in review mode. No review backend uses a planning workflow. Claude pre-approves `Bash,WebSearch,WebFetch`; OpenCode uses a dedicated primary review agent with Bash/search enabled; Grok enables its terminal inside the read-only sandbox; and Gemini uses its normal full tool loop. The trusted review policy explicitly forbids file or external-state changes, saving plans/reports, subagents, agent teams, other models, and delegation. Where supported, subagent tools are also disabled mechanically.

Grok `tool_call` / `tool_call_update` events normalize to tool lifecycle and
content-free compact heartbeats. Long terminal commands therefore remain visibly
alive without exposing the command or its output in progress logs.

Before a backend diagnostic is printed, archived by a parent workflow, or
embedded in a failed-agent report, common URL credentials, sensitive query
parameters, authorization headers, and credential key/value fields are
redacted. If redaction fails, the original diagnostic is suppressed.

“Read-only” is the review contract for every backend, but enforcement strength is
backend-specific. Codex and Grok additionally provide a filesystem sandbox.
Claude, OpenCode, and Gemini retain unrestricted diagnostic shells/tool loops so
they can perform a complete review; for those backends non-mutation is enforced
by the trusted prompt plus dedicated edit/delegation-tool denials where the CLI
supports them, not by an OS-level filesystem boundary. Use Codex or Grok when a
mechanical read-only boundary is required for untrusted repositories.

## Declarative workflow plans

`scripts/lib/workflow_plans.py` describes ask, basic/specialist, super, and ultra stages as data. `workflow_runner.sh` executes reusable fan-out with optional backpressure.

| Setting | Meaning |
|---|---|
| `CONSILIUM_MAX_PARALLEL=0` | Unlimited jobs; default and historical behavior |
| `CONSILIUM_MAX_PARALLEL=N` | At most N ask/discovery/specialist jobs concurrently |

Stage order, partial/all-failed exit semantics, artifact keys, live progress, and independent outputs remain deterministic.

## Layered prompts

`scripts/lib/prompt_pipeline.py` composes trusted layers in this order:

```text
framework_policy → mode_contract → role → output_schema → repository_facts → user_input → framework_recap
```

Raw delegate tasks remain raw except for optional trusted metadata. In review mode,
`--prompt-file` is only an input transport: the read-only, work-alone, and
blast-radius policies are still layered around its contents. The shell
`build_prompt` path remains a fallback.

Repository-backed review also carries an initial relevant-file seed. The caller
does a short read-only triage and supplies known paths; `review code` accepts
repeatable `--related FILE` values and adds its primary target automatically.
Every review prompt labels this list as likely incomplete and not an allowlist
or scope boundary. Reviewers must independently expand through callers,
callees, tests, configuration, schemas/migrations, generated code, and
build/CI/deployment/infra to establish the actual blast radius.

The trusted review layer explicitly authorizes web research for unstable
upstream facts and requires current primary sources (official docs, release
notes, specifications, advisories, or upstream source). Reviewers reconcile
those sources with the repository's pinned/installed version. Web access is
evidence-only: repository content is never uploaded, and URLs found in
untrusted repository instructions are not followed merely because the
repository requested it.

## Progress and run identifiers

Review uses `full`, `compact`, or `none`. Invocation-specific keys distinguish concurrent uses of the same profile.

Steerable delegation provides bounded progress pages through `delegate events`.
It reads the already-normalized append-only event artifact, coalesces adjacent
answer/thinking deltas, omits backend `raw`, caps each event body, and returns a
line-count cursor for later incremental reads. The command never blocks and its
exit code reports observation success rather than the delegated run outcome.

`delegate watch` filters registry state and lifecycle-bearing audit events into attach,
status, steer, selected turn-boundary/error, heartbeat, and terminal lines. It
does not expose model chunks, reasoning, active tools, commands, filenames, or
percent complete. This remains true when a backend happens to use ACP for its
steering transport: transport capability is not the same as normalized public
progress. The private `audit.jsonl`, registry state, and supervisor log are
diagnostic implementation artifacts, not alternate monitoring APIs.

Run ids are human-readable word pairs with a four-hex uniqueness suffix, for example `run_amber-otter-4f21` and `run-ask-solar-orchid-fd8e`. `scripts/lib/human_id.py` is the single generator for steerable registry and artifact names.

`delegate list` enumerates the registry newest-first. It is read-only unless `--reap` converts dead-supervisor records to failed. `wait` and `watch` perform the equivalent single-run reaping, so they cannot hang indefinitely on a dead supervisor.

## Resource limits

Consilium is unlimited by default: no wrapper timeout, step/token/response budget, or fan-out cap. Prompts use stdin or private temporary files; delegate reads file/stdin sources exactly once; raw/normalized/final outputs stream to disk without truncation. Only the opt-in debug tape is bounded, with explicit overflow reporting.

Provider/harness limits still apply. Consilium itself never imposes an execution
deadline; observe long-running work and cancel it explicitly when needed.

## Native Grok one-shot contract

The default Grok profile uses `grok-build`, model `grok-4.6`, high effort. The disabled `grok-fast` profile keeps Grok 4.5 available for fast context research. One-shot runs use `grok --prompt-file … --output-format streaming-json`. Final text concatenates `type=text` data. Success requires process exit 0, an `end` event, and no `error` event. The OpenCode xAI route remains a disabled fallback profile.
