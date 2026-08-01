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
| stderr | Live semantic progress while a model is running, controlled by the mode's progress style |
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
CONSILIUM_DEBUG_EVENTS=1 scripts/consilium review ask "Q"
CONSILIUM_DEBUG_EVENTS_PATH=/tmp/tape.jsonl
CONSILIUM_DEBUG_EVENTS_MAX=10000
CONSILIUM_DEBUG_EVENTS_MAX_BYTES=33554432
```

One-shot normalization records all stages; the steerable supervisor records normalized adapter events. Overflow, dropped, and gap counts are reported on close instead of being hidden.

## Shared backend contract

`scripts/lib/backend_contract.py` resolves profile identity, binary, model/effort including environment overrides, and real capability differences: steering delivery class, interrupt support, concurrent queues, transport, and final-text assembly. Both `backend_run.sh` and steerable `config_loader.py` use it.

## Mode capability policy

`scripts/lib/mode_policy.py` derives access from an explicit capability matrix covering filesystem, shell, web, memory, subagents, steering, and interrupt. Review/explore are read-only; delegate/delegate-steerable are YOLO. Unknown modes fail closed. Backend safety flags layer on top.

| Backend | Review / explore | Delegate |
|---|---|---|
| Codex CLI | `exec --sandbox read-only` plus ask-for-approval never | `--dangerously-bypass-approvals-and-sandbox` |
| Claude Code | `--permission-mode plan` plus Edit/Write denylist | `--dangerously-skip-permissions` |
| OpenCode | `--agent plan` | `--agent build --auto` |
| Grok Build | `--sandbox read-only` plus explicit tool allow/deny lists | `--always-approve`, no sandbox |
| Gemini CLI | `--approval-mode plan` | unsupported |

Web research is available in read-only modes. Grok explicitly allows `web_search,web_fetch`; Claude pre-approves `WebSearch,WebFetch` while the Edit/Write denylist remains authoritative. Explore adds Grok-specific isolation for remote sources.

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
framework_policy → mode_contract → role → output_schema → repository_facts → user_input
```

Explore never loads review principles, roles, or review schemas. Raw delegate tasks and `--prompt-file` remain raw except for optional trusted metadata. The shell `build_prompt` path remains a fallback.

## Progress and run identifiers

Review uses `full`, `compact`, or `none`; explore uses content-free `compact`, `verbose`, or `none`. Invocation-specific keys distinguish concurrent uses of the same profile.

Run ids are human-readable word pairs with a four-hex uniqueness suffix, for example `run_amber-otter-4f21` and `run-ask-solar-orchid-fd8e`. `scripts/lib/human_id.py` is the single generator for steerable registry and artifact names.

`delegate list` enumerates the registry newest-first. It is read-only unless `--reap` converts dead-supervisor records to failed. `wait` and `watch` perform the equivalent single-run reaping, so they cannot hang indefinitely on a dead supervisor.

## Resource limits

Consilium is unlimited by default: no wrapper timeout, step/token/response budget, or fan-out cap. Prompts use stdin or private temporary files; delegate reads file/stdin sources exactly once; raw/normalized/final outputs stream to disk without truncation. Only the opt-in debug tape is bounded, with explicit overflow reporting.

Provider/harness limits still apply. Set a positive `AGENT_TIMEOUT` only for an explicit watchdog on ordinary review or one-shot delegation. Steerable runs have no wrapper deadline; observe them and cancel explicitly.

## Native Grok one-shot contract

The default Grok profile uses `grok-build`, model `grok-4.5`, high effort. One-shot runs use `grok --prompt-file … --output-format streaming-json`. Final text concatenates `type=text` data. Success requires process exit 0, an `end` event, and no `error` event. The OpenCode xAI route remains a disabled fallback profile.
