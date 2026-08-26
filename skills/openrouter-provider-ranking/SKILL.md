---
name: openrouter-provider-ranking
description: "Use this skill when a user asks to rank, compare, benchmark, prioritize, or generate routing for OpenRouter provider endpoints (provider.order, provider.only, :exacto) by TPS/throughput, TTFT/latency, effective price, uptime, cache hit rate, tool-call/Exacto quality, quantization, context, privacy, or fallback diversity; also for requests about OpenRouter provider sorting or prioritization. Do not use for broad model-family selection unless endpoint-level provider routing is required."
compatibility: "Requires Python 3.10+; live endpoint discovery requires outbound HTTPS and a management-capable OpenRouter key in OPENROUTER_API_KEY. Offline endpoint JSON is supported. The bundled ranker uses only the Python standard library."
metadata:
  version: "1.0.0"
  domain: "openrouter-routing"
---

# OpenRouter Provider Ranking

Rank the **endpoint providers of a single OpenRouter model slug** for a
specific workload. Never call the order "globally optimal": it is optimal only
against the stated constraints, weights, token profile and available telemetry.

## Mandatory rules

1. Apply hard constraints first, score second. Never let high TPS or a low price compensate for an incompatibility.
2. For tool calling default to `native-exacto`: the `:exacto` model suffix, no `provider.sort`, no `provider.order`. Your own score in that mode is diagnostic, not a replacement for OpenRouter's private telemetry.
3. Use `manual` only when the user requires a deterministic order, when your own production telemetry outweighs Exacto, or when a failover chain has to be pinned explicitly.
4. Never combine `:exacto` with `provider.sort` — an explicit sort wins. Never add `provider.order` in `native-exacto` mode.
5. Price **on the real token profile**, not on headline input/output rates. Include cache read/write, per-request fees, conditional pricing overrides and the observed cache hit rate.
6. Do not invent missing Exacto, benchmark, cache or tool-success metrics. Apply a conservative prior and an uncertainty penalty, and name the gaps explicitly.
7. For multi-turn workloads pass a stable `session_id`. Remember that a manual `provider.order` disables OpenRouter's sticky provider routing, and `session_id` does not restore it.
8. Never store the API key in the skill, a config, a log or the output JSON. Read it only from `OPENROUTER_API_KEY` or the environment variable the user names.
9. **A catalogue field is a hypothesis; a measurement is a fact.** Do not hand back a ranking as the answer: always propose the minimal verification of the top candidates against the constraints that were asked for (step 5), and say plainly whether it was run.
10. The comparison row is `endpoint × reasoning effort`, not the endpoint. Changing effort moves price, latency and quality more than changing provider does — and `"none"` means "omit the field", not "no reasoning".
11. Compute price from components on the token profile (`in`, `out`, `cache_read`, `cache_write`, per-request fee). Headline and effective price swap places: the most expensive rate card produced the lowest cost per step at a 99.996 % cache hit.
12. Measure cache, latency and reliability on the profile that will ship. Cache hit on a repeated identical prompt (99 %) and in an agent run (68 %) are different numbers; TTFT on a short prompt is 4-6x optimistic; and fitness for a single request does not predict behaviour under sequential load.

## Inputs

Collect or estimate:

- the model slug, e.g. `deepseek/deepseek-v4-flash-0731`;
- `uses_tools`, streaming, required parameters, context and output limits;
- expected prompt/completion tokens and requests per session;
- cacheable prompt fraction, token-level cache read/write rate, response-cache hit rate;
- hard caps: price, latency, TPS, uptime, quantization, moderation, ZDR/data policy;
- the goal: quality, balanced, interactive latency, cost or batch throughput;
- your own telemetry by provider tag, if any exists.

When the input is incomplete, use the `agentic-balanced` profile. For tool calling set `uses_tools=true`. Do not assume a non-zero cache hit rate without observations or a defensible workload model.

## Procedure

### 1. Classify the workload

Pick one profile:

- `agentic-balanced` — the default for agents and B2B SaaS;
- `agentic-quality` — tool correctness and reliability outweigh price;
- `interactive` — minimise TTFT and end-to-end latency;
- `cost` — minimise expected cost under an SLO;
- `batch` — throughput and cost for long completions.

For a goal outside these, override `weights`; the sum after normalisation must be positive. The formula: [references/scoring.md](references/scoring.md).

### 2. Fetch fresh endpoint metrics

Preferred path — the OpenRouter Endpoints API through the bundled script:

```bash
python3 scripts/rank_providers.py \
  --model deepseek/deepseek-v4-flash-0731 \
  --config assets/config.example.json \
  --format markdown \
  --output recommendation.md
```

For a reproducible or offline analysis:

```bash
python3 scripts/rank_providers.py \
  --endpoints-file endpoints.json \
  --config config.json \
  --observations telemetry.jsonl \
  --previous-ranking previous-result.json \
  --output result.json
```

The Endpoints API gives the provider tag, pricing, quantization, context and output limits, supported parameters, uptime, and latency and throughput percentiles. When reading a performance page, carry any provider-specific Auto Exacto or benchmark values into observations by exact `tag`; never guess the match from a display name when a tag exists.

Input formats: [references/input-formats.md](references/input-formats.md).

**Read the metrics as they are defined, not as they read.** `latency_*` arrives
in **milliseconds** — `1624.8` is 1.6 s. A p90 *throughput* is the fast tail and
a p90 *latency* is the slow one, so rank on `p50` and report both. The
storefront's own numbers are collected on short prompts; see step 5 and
[references/storefront-traps.md](references/storefront-traps.md).

### 3. Add production telemetry

Quality signals, in order of priority:

1. your own tool-call/schema success for the same model, prompt class and provider tag;
2. provider-specific Exacto or benchmark values from the performance page;
3. the endpoint performance/uptime API;
4. a conservative prior when nothing is available.

Collect at least: `provider_name` or `provider_tag`, success, tool success, prompt/completion/cached/cache-write tokens, TTFT, generation time or TPS, and total cost. For rates from a small sample use a Wilson lower bound, not the raw percentage.

### 4. Run the ranking and check the result

The script should:

- drop inactive and incompatible endpoints;
- resolve pricing overrides as of the request;
- compute the expected cost for the workload;
- blend OpenRouter percentiles with your own observations by sample confidence;
- normalise cost, TPS, TTFT and E2E against the current eligible pool;
- apply the quality, reliability, cache, fidelity and uncertainty components;
- stabilise the order against a previous result;
- pick a fallback chain with provider-family diversity when the score gap allows.

Check the exit code. On `4` do not relax anything silently: show which constraints eliminated every endpoint and propose the smallest relaxation.

### 5. Verify the candidates with real requests — mandatory

A ranking is built from catalogue fields, and several of them are wrong often
enough to change the answer: `supports_implicit_caching` reads `false` on an
endpoint that caches 99 % of the prefix; storefront TTFT is taken on short
prompts and is 4-6x optimistic; and the cheapest endpoint on a bench may serve
no request at all under sequential load. The full list, each with its
reproduction: [references/storefront-traps.md](references/storefront-traps.md).

So **never hand back a ranking as the final answer**. Always propose the
minimal verification of the top candidates against the same hard constraints
the score used, and run it where you can:

```bash
python3 scripts/probe_endpoints.py \
  --model deepseek/deepseek-v4-flash-0731 \
  --providers coreweave/fp8,fireworks,siliconflow/fp8 \
  --prompt-file real-prompt.txt \
  --max-tokens 600 --runs 3 \
  --min-tps 50 --max-ttft 6 --require-cache --require-max-tokens
```

The script sends `--runs` identical requests per endpoint and reports the
measured TTFT, TPS, cost, cache hit share, completion tokens and error class,
then judges each against the thresholds you pass. Exit code `4` means none
survived — the ranker's own convention; do not relax the thresholds silently.

What must be passed:

- `--prompt-file` with **your own** prompt once a decision is actually being
  made. The `--prompt-tokens` filler is fine for a rough cut, but TTFT depends
  on size and contract compliance depends on content.
- `--runs >= 2`, but do not read a cache miss from filler as a verdict: a fresh
  prefix does not become cacheable inside a short probe. The same endpoint gave
  99 % over two calls on a prompt that was already in use and 0 % over four on a
  new one. A hit proves caching; a miss proves it only with `--prompt-file`.
- Thresholds taken from the hard constraints, not invented: the check must
  answer the user's question, not a generic one.

What the check does **not** do: it does not measure exact throughput and it does
not certify fitness. A failure is a conclusion; a pass is "on this profile, in
this window, over N calls". For an agentic workload add a run of sequential
calls — fitness for a single request does not predict it.

A separate one-request check of the data policy, whenever the constraints carry
`data_collection: deny` or `zdr`: `max_tokens: 1`, `allow_fallbacks: false`, one
request per candidate. Distinguish a policy refusal (`404 No endpoints found
matching your data policy`) from a provider 429 — different causes, different
conclusions.

### 6. Choose the routing mode

| Condition | Mode | What to send |
|---|---|---|
| Tool calls, no fixed order required | `native-exacto` | `model: <slug>:exacto`, filters/preferences, no `sort`/`order` |
| A pinned failover chain, or strong first-party telemetry | `manual` | `provider.order` from the ranking |
| One simple goal with no custom score | native OpenRouter | `provider.sort: price/throughput/latency`; the bundled ranker is optional |

OpenRouter-specific interactions and limits: [references/openrouter-routing.md](references/openrouter-routing.md).

## Response format

Always return:

1. the chosen mode and a short justification;
2. the eligible ranking table: provider tag, score, expected cost per request, TPS percentile, TTFT, E2E, uptime, quality confidence and cache hit rate;
3. a ready JSON request fragment;
4. the excluded providers, each with its reason;
5. coverage and warnings, and the list of missing signals;
6. **the minimal verification plan** — a ready `probe_endpoints.py` command with
   thresholds taken from the hard constraints, and its result if it was run.
   Call the ranking a hypothesis until that check has been made;
7. the refresh rule: recompute after noticeable drift, a price or endpoint
   change, or enough new telemetry. Never pin an order indefinitely.

In `native-exacto`, keep **the diagnostic ranking** and **the authoritative runtime ordering by Exacto** clearly apart.

## Validation checklist

Before returning a result, check that:

- provider tags come from a fresh API call or file, not from memory;
- hard constraints were applied before the score;
- prices were converted from USD/token to readable USD/M and to workload cost without double conversion;
- **`p90` throughput is read as the fast tail — the value about 10 % of requests exceed — and `p90` latency as the slow one. Rank on `p50`;** a provider whose p90 is 57 and p50 is 33 is not the fastest, and reading p90 as a floor already put one first;
- `latency_*` is read as milliseconds, while `provider.max_price` is passed in USD per million tokens and endpoint pricing is stored in USD per token;
- `provider.order` is absent in `native-exacto`;
- service-tier tags (`/fast`, `/flex`) were not included by accident;
- cache-heavy sessions carry a stable `session_id`, and the consequences of a manual order are noted;
- a small sample is not over-read;
- the final request JSON is syntactically valid;
- the minimal verification of the top candidates was proposed — and run where possible — and a ranking without it was called a hypothesis;
- `supports_implicit_caching`, TTFT and throughput were not taken on faith wherever the conclusion depends on them.

## Bundled resources

- `scripts/rank_providers.py` — the standalone ranker and routing-fragment generator.
- `scripts/probe_endpoints.py` — the minimal verification of candidates with real
  requests: TTFT, TPS, cost, cache hit, `max_tokens` compliance and error class;
  judges each against the thresholds passed, exit code `4` when none survives.
- `scripts/validate_skill.py` — self-check of frontmatter, resources, syntax and unit tests.
- `assets/config.example.json` — a config for a tool-using agent workload.
- `assets/observations.example.json` — aggregated provider observations.
- `assets/telemetry.example.jsonl` — raw request-level observations.
- `tests/trigger-evals.json` — positive and negative activation queries for the description.
- `references/scoring.md` — the formula, normalisation and profiles.
- `references/input-formats.md` — the config and telemetry schema.
- `references/openrouter-routing.md` — semantics OpenRouter routing/caching.
- `references/storefront-traps.md` — reproduced disagreements between catalogue
  fields and endpoint behaviour; read it before ranking.

To validate the package, run:

```bash
python3 scripts/validate_skill.py
```
