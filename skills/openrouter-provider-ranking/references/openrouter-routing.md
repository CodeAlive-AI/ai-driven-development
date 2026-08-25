# OpenRouter routing semantics

This reference captures interactions that materially affect provider ranking. Re-check the linked official documentation when behavior may have changed.

## Decision table

| Mechanism | Runtime behavior | Main caveat |
|---|---|---|
| Default routing | price-weighted load balancing with uptime handling and fallbacks | not a deterministic order |
| `provider.sort` | explicit `price`, `throughput`, or `latency` ordering | disables load balancing; single-objective only |
| `provider.order` | tries listed providers in order | disables load balancing and prompt-cache sticky provider routing |
| `:exacto` | quality-first ordering using OpenRouter tool-use, performance and benchmark signals | do not override with `sort`; internal weights/telemetry are not public |
| Auto Exacto | applied automatically to tool-calling requests where supported | use explicit `:exacto` when deterministic activation of the mode matters |

Official sources:

- Provider selection: https://openrouter.ai/docs/guides/routing/provider-selection
- Exacto: https://openrouter.ai/docs/guides/routing/model-variants/exacto
- Prompt caching: https://openrouter.ai/docs/guides/best-practices/prompt-caching
- Endpoints API: https://openrouter.ai/docs/api/api-reference/endpoints/list-all-endpoints-for-a-model

## `order`, `only`, `ignore`, and fallbacks

`provider.order` gives preferred provider slugs/tags. Providers omitted from `order` may still be used as fallbacks unless the request also constrains the pool or disables fallbacks.

Use:

- `provider.only` to define the complete eligible pool;
- `provider.ignore` to remove known-bad providers;
- `provider.allow_fallbacks=false` only when failure is preferable to using an unlisted endpoint.

A base provider slug can match ordinary variants/regions, but service tiers such as `/fast` and `/flex` require explicit eligibility. The ranker excludes service tiers by default through `allowed_service_tiers: ["default"]`.

Do not create a stale permanent `only` list from one snapshot. Refresh it when endpoint availability or local hard constraints change.

## Parameter compatibility

Set `provider.require_parameters=true` whenever the request depends on specific provider-supported parameters. Tool support, `response_format`, structured outputs, reasoning controls and other fields can differ by endpoint.

The local ranker hard-filters `workload.required_parameters`; the emitted request also sets `require_parameters` so runtime routing revalidates the current pool.

## Performance preferences versus hard filters

`preferred_min_throughput` and `preferred_max_latency` are soft routing preferences. They can be numbers or percentile objects. They do not guarantee an SLO and should not replace local hard filters when violating the threshold is unacceptable.

Percentile interpretation:

- throughput p90 = approximately 90% of requests reach at least that TPS;
- latency p90 = approximately 90% of requests complete first-token latency at or below that value.

Use p90 for production defaults; p50 is useful for exploratory/UI estimates but understates tail risk.

## Price units

Endpoint API prices are USD per token/request/unit. OpenRouter `provider.max_price.prompt` and `.completion` are expressed in USD per million tokens. Convert exactly once.

Price must be evaluated against the workload. Two endpoints with equal headline prompt/completion price can differ through cache read/write price, request fees, long-context overrides or time-window overrides.

## Caching and session stickiness

OpenRouter can keep a conversation on the same provider to preserve upstream prompt cache. A stable top-level `session_id` is the clearest routing key for multi-turn agents.

Manual `provider.order` takes priority and disables sticky provider routing. Therefore:

- prefer default/Exacto routing for cache-heavy multi-turn workloads unless manual order is necessary;
- in manual mode keep the first provider stable across a session and monitor token-level cache hit rate;
- do not claim that adding `session_id` restores stickiness under manual order;
- still send `session_id` for session grouping/observability when useful.

Read cache telemetry from `usage.prompt_tokens_details.cached_tokens` and `cache_write_tokens`. Optimize token-level hit rate and successful-task cost, not just the percentage of requests with any hit.

## Exacto integration

Exacto uses OpenRouter-maintained quality/performance signals, including tool-use reliability and benchmark data. Treat it as an external ranking service, not a numeric feature that can be faithfully reconstructed from public data.

Recommended hybrid:

1. Build an eligible pool with policy, parameter, context, quantization and price constraints.
2. Use `:exacto` inside that pool for tool workloads.
3. Keep the local multi-objective score for diagnostics, cost planning and detecting endpoints that should be excluded.
4. Switch to `manual` only when production evidence supports it.

Explicit `provider.sort` takes precedence over Exacto and must not be emitted in `native-exacto` mode.

## Privacy and tiers

When required, propagate:

- `provider.data_collection: "deny"`;
- `provider.zdr: true`;
- `provider.quantizations`;
- explicit service-tier tags.

Do not assume provider-level privacy from display name. Enforce the OpenRouter request preference and any organization-level policy independently.

## BYOK caveat

Bring-your-own-key behavior can change provider selection economics and order. If BYOK is enabled, validate whether the relevant provider is preferred or has separate routing semantics before relying on a cost-based order.
