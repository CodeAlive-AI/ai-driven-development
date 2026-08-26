# What the storefront gets wrong

Each item is a reproduced disagreement between what
`/api/v1/models/<slug>/endpoints` (or the performance page) reports and what the
endpoint actually does. All were observed in one session against
`deepseek/deepseek-v4-flash-0731` across 29 endpoints, and every one of them
changed the choice.

The rule they all follow from: **a catalogue field is a hypothesis, a
measurement is a fact.** Do not rank on a field that is cheaper to check than to
explain away.

## 1. `supports_implicit_caching` can be false when caching works

It read `false` on every endpoint except first-party. Measured by three
identical requests in a row, reading
`usage.prompt_tokens_details.cached_tokens`:

| endpoint | claimed | measured |
|---|---|---|
| coreweave/fp8 | `false` | 24 320 of 24 618 — 98.8 % |
| fireworks | `false` | 24 696 of 24 697 — 99.996 % |
| io-net/fp8 | `false` | 0 — genuinely absent |

The conclusion drawn from the field — "only first-party caches, so there is no
saving here" — was wrong and inverted the final order. Checking it costs three
requests.

## 2. Headline price and effective price can swap places

`fireworks` has the most expensive rate card ($0.22/$0.66 per million, two to
three times its neighbours) and **the lowest measured cost per step**
($0.000965), because its `input_cache_read` is $0.007 per million at a 99.996 %
hit rate.

Always price on the token profile, from components: `in`, `out`, `cache_read`,
`cache_write`, `per_request_fee`, and any conditional overrides.

## 3. Cache on a bench and cache in an agent are different numbers

The same prompt three times: 98.8 %. The same endpoint in an agent run, where
the prefix grows from step to step: **68 %**. A saving computed from the first
is overstated twofold.

Measure the hit rate on the profile that will ship, and record the profile next
to the number.

## 4. Storefront TTFT is taken on short prompts

| endpoint | `latency_last_30m.p50` | measured at 24.6k input tokens |
|---|---:|---:|
| coreweave/fp8 | 0.65 s | 3.38 s |
| deepseek | 0.92 s | 5.05 s |
| io-net/fp8 | 0.96 s | 8.26 s |

Four to six times out. In a multi-step workload TTFT is multiplied by the number
of steps and dominates the felt latency — so the field that misleads is the one
that matters most.

Units: `latency_*` arrives in **milliseconds**. `1624.8` is 1.6 s, not 27
minutes; getting this wrong has already produced a report reading "1624.80s".

## 5. Ranking on p90 throughput is ranking on the tail

`akashml/fp8`: p90 = 57, **p50 = 33**. Sorting by p90 put it first even though
its typical request is half the speed of the runner-up's.

Agree explicitly that "speed" means `p50`. A p90 *throughput* is the fast tail;
a p90 *latency* is the slow one. Publish both, rank on p50.

## 6. Fitness for one request is not fitness for load

`fireworks`: 98 % uptime, serves a single request perfectly, cheapest by
measurement. In an agent run — 6 tasks of 5-8 sequential calls each — it served
**0 of 6**, `rate-limited upstream` every time. `parasail/fp8` returned 429 on
six attempts spread over an hour.

Uptime measures whether the endpoint is up, not whether it will survive your
pattern. Check with a sequential series, not a single call.

## 7. A provider may not honour the request contract

Published nowhere, and it breaks more than a slow response does:

- **`max_tokens` ignored.** `siliconflow/fp8` returned 3693 completion tokens
  against `max_tokens: 1200`; every other endpoint returned exactly 1200. Token
  budgets and per-step accounting rest on this, and such an endpoint's
  cheapness is illusory: it bills for three times the output.
- **Structured output falls apart.** A model in a judge role returned no
  parsable object in 4 of 39 verdicts; the caller substituted its fallback and
  the scores dropped silently — indistinguishable from a strict grader.

Worth collecting: `respects_max_tokens`, `structured_output_failure_rate`,
`tool_call_schema_failure_rate`.

## 8. Reasoning effort is a configuration axis, not a flag

`"none"` on OpenRouter means "do not send the field", not "turn reasoning off".
The model then thinks as much as it likes.

Measured on one task: `none` — 8843 output tokens, $0.0253, 9.0 s median;
`low` — 2362 tokens, $0.0132, 3.4 s median. The mode that reads as "no
reasoning" was **twice the price and three times the latency** of an explicit
`low`.

Consequences for ranking:

- a comparison row is `endpoint × effort`, not an endpoint;
- reasoning tokens bill as output, and output costs more than input, so price
  climbs faster with effort than it appears to;
- the provider's enum can run ahead of SDK types: OpenRouter accepts
  `max|xhigh|high|medium|low|minimal|none` — verified by sending an invalid
  value and reading the 400 — while `@openrouter/ai-sdk-provider` 3.0.0 types
  only six, so `max` has to travel in `extraBody`.

## 9. A provider pool belongs to its own model

`provider.only` applies to whatever request carries it. A pool chosen for the
answering model, set globally, travelled with a call to the judge model and got:

```
No allowed providers are available for the selected model.
Providers serving google/gemini-3.7-flash: google-vertex, google-ai-studio,
but your request's provider.only preference permits only: fireworks, coreweave/fp8
```

A slug names an endpoint **of one model**. Apply a pool only to the model it was
computed for.

## 10. Check the data policy with a request, not a field

`data_collection: deny` removes endpoints silently and wholesale. For
`deepseek/deepseek-v4-flash-0731` it leaves **none at all**, first-party
included:

```
404 No endpoints found matching your data policy (Paid model training)
```

One request per candidate with `max_tokens: 1` and `allow_fallbacks: false`
shows this in seconds, and separates a policy refusal from a provider 429.

## How to read a verification result

Verification **disqualifies reliably and confirms weakly**. "Failed six of six"
is a conclusion; "respected `max_tokens` over three requests" is only an absence
of refutation.

Observed while writing this page: `io-net/fp8` returned `cached_tokens: 0` on a
60 KB document and 94 % on an 8k synthetic prompt; `siliconflow/fp8` overran
`max_tokens` threefold on one profile and respected it on another. Contract
violations are condition-dependent.

Two rules follow:

- verify with **your own** prompt (`--prompt-file`) once a decision is actually
  being made, not with filler;
- record a negative result as a fact, and a positive one as "on this profile, in
  this window, over N requests".

## 11. A cache miss in a short probe is not a cache miss

Measured while writing the probe that checks this page's other claims: the same
endpoint returned **99 % cache hit over two calls** with a prompt that had been
sent all day, and **0 % over four calls** with a freshly generated one.

An implicit cache is not established by a handful of consecutive requests. A
prefix nobody has sent before does not become readable inside a short probe, so
`cached_tokens: 0` there says nothing about the endpoint.

Therefore: a cache *hit* proves caching; a cache *miss* proves it only when the
prompt is one the system genuinely reuses. `probe_endpoints.py` marks an
inconclusive reading with `?` and refuses to fail an endpoint on it, and warns
when `--require-cache` is passed without `--prompt-file`.

The same asymmetry applies to every check on this page, and it is the reason
step 5 exists rather than a promise that the probe settles the question.
