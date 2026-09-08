# Claude Fable 5.1 Prompting Guide

Use this guide for Claude Fable 5.1 prompts, long-horizon agents, and migrations
from Claude Fable 5.

Primary sources:

- [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)
- [Claude Fable 5.1 overview](https://platform.claude.com/docs/en/models/fable-5-1/overview)
- [Effort](https://platform.claude.com/docs/en/build-with-claude/effort)

## Model and effort

- Use the model ID `claude-fable-5-1`.
- Thinking is adaptive and always on. Control it with `output_config.effort`.
- Start at the default `high`; evaluate `low`, `medium`, `xhigh`, and `max` on
  your own tasks. Effort labels do not represent the same compute as Fable 5.
- Fable 5.1 supports per-message effort changes in beta. Use the documented
  effort-only system message so the cached conversation prefix remains intact.
- At `xhigh` or `max`, leave enough `max_tokens` for both thinking and the reply;
  use at least 64K for demanding long outputs.

## Progress and tool loops

Fable 5.1 emits fewer visible updates by default. First enable progress-update
thinking blocks with `thinking.display: "updates"` and the required beta header;
prompt only if the resulting cadence is still too sparse:

```text
Before starting, say in one line what you will do. During long tool loops, send
brief updates at meaningful milestones. End with a self-contained recap of the
result, verification, and any real blocker.
```

In coding and computer-use loops, explicitly request batching when independent
calls are otherwise issued one per turn:

```text
Batch independent tool calls in the same turn. Continue useful lead-agent work
while asynchronous tools or subagents run, and wait only when their result is a
dependency for the next step.
```

## Conversation integrity

Keep conversation history append-only. Editing earlier messages can invalidate
Fable 5.1 thinking blocks and cause a `bound to a different conversation`
error. Earlier Claude models cannot consume Fable 5.1 thinking blocks, so strip
or summarize them before switching to an older fallback.

Forced tool use is a breaking change: Fable 5.1 returns an error for unsupported
forced-tool configurations. Prefer `auto` tool choice and express the required
outcome in the prompt; validate any harness-specific forcing behavior.

## Completion, scope, and edits

Fable 5.1 may stop early, ask permission for authorized work, expand scope, or
rewrite whole files for small edits. Use compact boundaries:

```text
Finish the requested task in this turn when possible. Proceed with reversible,
authorized work and pause only for destructive action, a real scope change, or
input only the user can provide. Keep implementation and tests within scope.
For localized changes, edit only the affected regions unless most of the file
must change.
```

For client-side compaction, require preservation of the goal, constraints,
decisions, exact identifiers and values, completed work, verification evidence,
and unresolved blockers.

## Research, safety, and vision

- At `low` effort, explicitly require search for unfamiliar or fast-moving names;
  familiarity is not evidence that remembered details are current.
- Handle `stop_reason: "refusal"`. Benign security work benefits from clear
  defensive context, authorization, and bounded scope. Do not ask for hidden
  reasoning; request evidence and a concise rationale.
- For charts and dense images, provide crop and zoom tools and tell the model to
  inspect labels, legends, axes, and small regions before concluding.
- Mark copied wording as quotation and preserve source attribution.

## Migration checklist from Fable 5

1. Change the model ID to `claude-fable-5-1` and keep existing prompts initially.
2. Re-run the full effort sweep; start at `high` for difficult work.
3. Keep history append-only and test thinking-block compatibility across fallbacks.
4. Remove or validate forced tool choice.
5. Enable progress-update blocks if users need visible long-run status.
6. Prompt batching, completion, scoped tests, and targeted edits only where evals
   show those behaviors need correction.
7. Increase output limits for long deliverables at `xhigh` and `max`.
8. Test refusal handling, compaction, search behavior at `low`, subagent overlap,
   and detailed vision tasks in the production harness.
