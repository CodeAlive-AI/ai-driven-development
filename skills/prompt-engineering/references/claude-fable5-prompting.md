# Claude Fable 5 Prompting Guide

Use this guide for Claude Fable 5 and Claude Mythos 5 prompts, skills, agent harnesses, and migrations from Claude Opus 4.8.

Primary sources:

- [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
- [Claude Fable 5 overview](https://www.anthropic.com/claude/fable)

Fable 5 is optimized for difficult, ambiguous, end-to-end work that can run for hours or days. Use it as a job handoff: give it the goal, context, definition of done, boundaries, and verification method without over-prescribing the route.

## API and Reasoning Changes

- Thinking is always on and adaptive; adaptive thinking is the only supported mode.
- Control the intelligence/latency/cost tradeoff with `output_config.effort`.
- Start with `high` for most substantial tasks, use `xhigh` for capability-sensitive work, and test `medium` or `low` for routine or interactive work.
- Legacy `thinking.budget_tokens` is unsupported and returns HTTP 400.
- Thinking output is summarized rather than exposed verbatim.
- Requests can end with `stop_reason: "refusal"`; configure fallback to Opus 4.8 where appropriate.

Do not ask Fable 5 to reveal, transcribe, reproduce, or explain its hidden reasoning. Such instructions can trigger the `reasoning_extraction` refusal category. Ask for a concise rationale, evidence, verification results, or decision summary instead.

## Prefer Brief, High-Level Instructions

Fable 5 follows instructions strongly enough that a short behavioral rule often replaces a long checklist. Review old skills and system prompts for obsolete scaffolding.

```text
Lead with the outcome. Include supporting detail only when it changes what the
reader would do next. Prefer clear complete sentences over compressed shorthand.
```

At higher effort, prevent unnecessary expansion:

```text
Don't add features, refactor, or introduce abstractions beyond what the task
requires. Do the simplest thing that works well. Validate at system boundaries.
```

Give the reason behind a request when it affects priorities or judgment:

```text
I'm working on [larger task] for [audience]. They need [what the output enables].
With that in mind: [request].
```

## Long Runs and Progress Claims

Hard turns can run for many minutes and autonomous sessions can run for hours. Adjust timeouts, streaming, progress UI, and asynchronous scheduling before migration.

Ground every progress claim in actual tool output:

```text
Before reporting progress, audit each claim against a tool result from this
session. If work is unverified, skipped, or failed, say so explicitly. Report
completed and verified work plainly.
```

Use sparse progress updates at meaningful milestones. Do not narrate routine tool calls. For long asynchronous agents, consider a dedicated `send_to_user` tool for verbatim deliverables or messages that must reach the user without ending the run.

## Action and Approval Boundaries

Fable 5 can take proactive actions that were not requested. State the boundary between assessment and mutation:

```text
When the user describes a problem, asks a question, or thinks out loud, the
deliverable is an assessment. Report findings and stop. Apply changes only when
requested. Before changing system state, verify that the evidence supports that
specific action.
```

For authorized autonomous work, define the real pause conditions compactly:

```text
Pause only for a destructive or irreversible action, a real scope change, or
input only the user can provide. Proceed with reversible in-scope work.
```

If the harness is unattended, explicitly forbid ending on a promise or an unnecessary permission question.

## Subagents and Verification

Fable 5 is more capable and more eager at parallel delegation than prior Claude models.

- Delegate only independent workstreams that benefit from separate context.
- Keep working while subagents run and communicate asynchronously.
- Give each subagent a bounded deliverable and relevant context.
- Prefer a separate fresh-context verifier over self-critique for long-running work.
- Reuse long-lived subagents across related subtasks when retained context and cache reads improve efficiency.

Make verification periodic and specification-based:

```text
Establish a method for checking the work as you build. At each milestone, have a
fresh-context verifier compare the current artifact with the specification and
report concrete mismatches.
```

## Memory Systems

Fable 5 benefits from a writable, curated memory rather than raw session accumulation.

```text
Store one lesson per file with a one-line summary. Record confirmed approaches
and corrections, including why they mattered. Do not duplicate facts already in
the repository or chat. Update existing notes and delete lessons proven wrong.
```

Keep memory scoped, reviewable, and correctable. Do not surface explicit remaining-token countdowns to the model unless necessary; they can provoke premature handoff or session-ending behavior.

## Communication After Long Runs

The final answer must re-ground a reader who did not see the tool loop:

- open with the outcome;
- use complete sentences, not arrow chains or internal shorthand;
- explain identifiers and newly introduced terms;
- separate verified results from blockers and unresolved risk;
- mention only the next actions that materially matter.

## Migration Checklist from Opus 4.8

1. Remove legacy `budget_tokens` and use always-on adaptive thinking plus effort.
2. Start with `high`, then evaluate lower effort for latency/cost and `xhigh` for hard tasks.
3. Audit prompts for hidden-reasoning extraction requests.
4. Shorten repetitive, prescriptive instructions and rerun evals.
5. Increase client timeouts and support asynchronous progress.
6. Add evidence-grounded progress rules and explicit action boundaries.
7. Add fresh-context verification for long runs.
8. Define when subagents and persistent memory are appropriate.
9. Test refusal and Opus 4.8 fallback behavior for cyber and life-sciences workloads.
