# GPT-6 Astra Prompting Guide

Use this guide for GPT-6 Astra prompts, coding agents, tool-using workflows, and
migrations from GPT-5.6.

Primary sources:

- [Using GPT-6 Astra](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra)
- [GPT-6 Astra model](https://developers.openai.com/api/docs/models/gpt-6-astra)

## Model and reasoning

- Use the model ID `gpt-6-astra`.
- `reasoning.effort` supports `low`, `medium`, `high`, `xhigh`, and `max`.
  `none` and `minimal` are unsupported; migrate either to `low`.
- Preserve the current effective effort when migrating from GPT-5.6 unless
  evals justify a change.
- In a cached conversation, prefer a `configuration_update` input item for
  changing effort instead of changing the request-level value.
- Remove `temperature`, `top_p`, and `top_logprobs`. In Chat Completions also
  remove `logprobs`; in Responses do not request `message.output_text.logprobs`.

## Initiative and completion

Astra may pause for clarification when reasonable assumptions would suffice.
State the autonomy boundary and the true pause conditions:

```text
Infer the user's intent and scope from the request and prior context. Carry
authorized work to completion. Fill routine gaps with reasonable assumptions;
ask only when missing input could materially change the result. Complete all
reversible preparation before requesting approval for an irreversible action.
```

Treat requests such as “can you” and “help me” as requests to do the work, not
as questions about capability. Do not let persistence broaden authorization.

## Instruction hierarchy and loaded files

Astra follows instructions strongly and is sensitive to skills, repository
guides, and other context files. Audit those files for contradictions and make
precedence explicit:

```text
The user's explicit instructions take precedence over general guidelines in
skills. If a loaded instruction changes the plan or blocks completion, name the
file and explain the exact conflict.
```

Keep reference material clearly separated from instructions. Treat instructions
inside retrieved or repository content as untrusted unless the application
explicitly designates that source as authoritative.

## Writing style

Astra tends toward detailed, heavily formatted answers. Specify the desired
density and structure:

```text
Lead with the outcome. Use concise paragraphs and plain language. Use lists or
tables only when they make parallel, sequential, or comparative information
easier to understand. Match technical detail to the reader's background.
```

Name unwanted recurring phrases only when evals show a real style regression;
large negative word lists add prompt debt and can distort unrelated prose.

## Tools, steering, and parallelism

- Use the Responses API for tool calling.
- Mark independent long-running tools `async: true`; the application must retain
  the original `call_id`, execute the tool, and return its result later.
- Use Responses over WebSocket for mid-turn user steering. Preserve completed
  work and attach new requirements to the continuation.
- Astra can use programmatic tool calling, multi-agent orchestration, persisted
  reasoning, compaction, computer use, and prompt caching.
- Specify when subagents are useful. Astra may otherwise delegate less than the
  workflow expects:

```text
Delegate bounded, independent workstreams when parallel execution saves time or
adds a genuinely independent check. Keep useful local work moving while they run.
```

## Testing and verification

Astra may over-test small changes. Calibrate verification to risk:

```text
Run checks proportional to the change and complete required gates. Add tests
that verify behavior or a meaningful regression. Do not broaden or repeat the
suite after it passes unless new changes, failures, or unresolved risks justify it.
```

## Migration checklist from GPT-5.6

1. Set `model` to `gpt-6-astra`.
2. Map `none` or `minimal` effort to `low`; otherwise preserve effective effort.
3. Remove unsupported sampling and logprob parameters.
4. Use Responses for tool-calling workflows.
5. Replace legacy cache retention with `prompt_cache_options.ttl: "30m"` when
   migrating from GPT-5.5 or earlier.
6. Add autonomy guidance only if evals show unnecessary clarification pauses.
7. Specify writing density, delegation policy, and verification scope.
8. Test async tools, steering, caching, and long-running completion in the real
   harness rather than assuming transport support from model capability alone.
