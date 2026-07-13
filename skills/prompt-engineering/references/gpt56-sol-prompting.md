# GPT-5.6 Sol Prompting Guide

Use this guide when adapting prompts, tool descriptions, agent instructions, or prompt stacks to GPT-5.6 Sol or the GPT-5.6 family.

Primary source: [Using GPT-5.6](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-5.6)

GPT-5.6 works best when prompts define the outcome, important constraints, available evidence, and completion bar, then leave room for the model to choose an efficient path.

## Model Selection and Controls

- `gpt-5.6` aliases `gpt-5.6-sol`, the flagship model.
- Use `gpt-5.6-terra` for a stronger cost/performance balance and `gpt-5.6-luna` for efficient high-volume work.
- Supported `reasoning.effort` values are `none`, `low`, `medium`, `high`, `xhigh`, and `max`.
- `reasoning.mode: "pro"` spends more model work on a single final answer. Use it only when evals justify the added latency and cost.
- Set default answer detail with `text.verbosity`: `low`, `medium`, or `high`.

When migrating from GPT-5.4 or GPT-5.5, preserve the current reasoning effort as the baseline, then test the same setting and one level lower. Reserve `max` for the hardest quality-first workloads.

## Simplify Prompts First

Start with a prompt and tool set that already works. Remove one group of instructions, examples, or tools at a time, then rerun the same evals.

Trim:

- repeated statements of the same rule;
- repeated style or process instructions that do not change behavior;
- examples that do not change behavior;
- process scaffolding for behavior the model already performs reliably;
- tools and tool descriptions unrelated to the task.

Keep:

- the user-visible outcome and definition of done;
- safety, business, evidence, and permission constraints;
- context-dependent tool-routing rules;
- required output shape and validation requirements;
- stopping conditions.

Conflicting rules are often more destabilizing than missing detail. State each instruction once.

## Outcome-First Prompting

Describe the destination rather than prescribing every step:

```text
Resolve the customer's issue end to end.

Success means:
- make the eligibility decision from available policy and account evidence
- complete any allowed action before responding
- return completed_actions, customer_message, and blockers
- if required evidence is missing, ask for the smallest missing field
```

Use absolute words such as ALWAYS, NEVER, MUST, and ONLY for real invariants. For judgment calls, provide decision criteria. Add a stop rule so loop minimization never outranks correctness, evidence, calculations, or citations.

## Autonomy and Approval Boundaries

GPT-5.6 can be proactive and persistent. Define what each request authorizes:

```text
For requests to answer, explain, review, diagnose, or plan, inspect the relevant
materials and report the result. Do not implement changes unless requested.

For requests to change, build, or fix, make the requested in-scope local changes
and run relevant non-destructive validation without asking first.

Require confirmation for external writes, destructive actions, purchases, or a
material expansion of scope.
```

Keep this policy in one place. Repeating approval rules can cause unnecessary pauses on safe, expected actions.

## Response Length and Collaboration

GPT-5.6 is more concise by default than GPT-5.5. Re-evaluate broad brevity instructions after migration; they may make answers too short.

For shorter answers, specify what must survive trimming:

```text
Lead with the conclusion. Include the evidence needed to support it, any material
caveat, and the next action. Omit secondary detail and repetition.
```

Define personality and collaboration separately. Personality governs tone; collaboration governs assumptions, initiative, questions, tradeoffs, verification, and uncertainty.

## Tool Routing and Programmatic Tool Calling

Expose only relevant tools. Tool descriptions should say what the tool does, when to use it, important return fields, and error behavior.

Use Programmatic Tool Calling (PTC) for bounded workflows where JavaScript can reduce many structured tool results through filtering, joining, sorting, ranking, deduplication, aggregation, batching, or deterministic validation.

Prefer direct tool calls when:

- one call is sufficient;
- each result changes the next decision;
- an action needs approval;
- citations or native artifacts must be preserved;
- semantic judgment is required between calls.

For PTC, define the bounded stage, eligible tools, compact output schema, retry limit, stop condition, and handoff back to direct model judgment. Validate both the `program_output` item and the final assistant message.

## Grounding and Retrieval Budgets

Define what claims need support, what counts as enough evidence, and what to do when evidence is missing. Absence of evidence is not automatically evidence of absence.

- Start with one broad retrieval pass using discriminative terms.
- Retrieve again only for a missing required fact, owner, date, ID, source, exhaustive comparison, or unsupported important claim.
- Cite only retrieved sources and attach citations to the claims they support.
- Label inference separately, state source conflicts, and narrow the answer rather than guessing.

## Long-Running State

- Give sparse, outcome-based user updates at major phase changes.
- Preserve assistant `phase` values when replaying history.
- Compact after milestones rather than after every turn.
- Use persisted reasoning only while objectives, assumptions, and priorities remain stable.
- Keep cacheable prompt prefixes stable; use explicit cache breakpoints only when measurements justify them.

## Frontend and Visual Work

GPT-5.6 has stronger layout, visual hierarchy, and design judgment, but still needs product context and explicit constraints.

- Preserve existing design tokens, components, responsive behavior, and states.
- Do not add decorative UI or unrelated features.
- Render and inspect the result before finalizing.
- Use original image detail for dense or coordinate-sensitive inputs when its added token cost and latency are justified.

## Validation

Tell the model what verification matters. For code, prefer targeted tests, type checks or lint, affected-package builds, and a minimal smoke test. For visual artifacts, render and inspect layout, clipping, spacing, missing content, and visual consistency.

## Suggested Prompt Structure

```text
Role: [the model's function and context]
Personality: [tone and collaboration style]
Goal: [user-visible outcome]
Success criteria: [what must be true before the final answer]
Constraints: [policy, safety, evidence, and side-effect limits]
Tools: [which tools to use and when]
Output: [sections, length, format, and tone]
Stop rules: [when to retry, fallback, abstain, ask, or stop]
```

## Migration Workflow

1. Switch the model and preserve current reasoning effort.
2. Run representative evals before changing the prompt.
3. Remove obsolete scaffolding, repeated instructions, and irrelevant tools.
4. Add only the smallest targeted instruction that fixes a measured regression.
5. Re-run the same evals after each prompt or reasoning change.

Do not rewrite a working prompt stack all at once; otherwise model, prompt, tool-set, and runtime effects become impossible to isolate.
