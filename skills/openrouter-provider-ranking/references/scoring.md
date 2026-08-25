# Scoring model

## Scope

The ranker solves a constrained, workload-specific multi-objective decision problem over the endpoints of one OpenRouter model. It does not claim a universal optimum and does not reproduce OpenRouter's private Exacto telemetry.

Let `i` be an endpoint. First construct the eligible set:

`E = {i | status, context, output, parameters, policy, tier, quantization, SLO and price constraints pass}`.

Only endpoints in `E` receive a score.

## Expected cost

Endpoint prices returned by OpenRouter are USD per token/unit. Resolve all matching pricing overrides for the selected UTC instant; later matching overrides win per key. Skip an override with an unknown condition field.

For a workload with prompt tokens `P`, completion tokens `O`, cache-read fraction `h`, cache-write fraction `w`, and response-cache hit rate `r`:

```text
P_read    = P * h
P_write   = P * w
P_regular = max(0, P - P_read - P_write)

C_upstream =
    P_regular * price_prompt
  + P_read    * price_cache_read
  + P_write   * price_cache_write
  + O         * price_completion
  + price_request

C_expected = (1 - r) * C_upstream
```

If a cache-specific price is absent, use regular prompt price for that token class. If the endpoint has no cache signal, force `h=w=0`. Do not infer hit rate from cache capability alone.

`h` and `w` are token-level fractions, not request-level fractions. Clamp `h+w <= 1`.

## Performance

Use the configured percentile, default `p90`:

- throughput `TPS_i`: higher is better;
- latency `TTFT_i`: lower is better;
- estimated end-to-end latency:
  `E2E_i = TTFT_i + expected_completion_tokens / TPS_i`.

Blend own telemetry with OpenRouter's rolling metric:

`metric = alpha * observed + (1-alpha) * OpenRouter`, where `alpha = n/(n+k)`.

This prevents a small local sample from replacing a stable platform estimate.

## Reliability

Create a weighted uptime estimate from 5m, 30m and 1d windows. Default weights are 0.50, 0.30 and 0.20. Map uptime through a smooth SLO curve between `floor=0.97` and `target=0.9995`.

When request success counts exist, calculate the 95% Wilson lower bound and blend it by sample size. Do not rank `10/10` above `990/1000` merely because the raw percentage is higher.

## Quality and Exacto signals

For tool workloads, default signal weights before confidence shrinkage:

```text
tool_success_lcb  0.45
tau_bench         0.25
exacto_score      0.20
gpqa_diamond      0.05
quality_score     0.05
```

For non-tool workloads:

```text
quality_score     0.45
gpqa_diamond      0.25
exacto_score      0.15
tau_bench         0.15
```

Average only available signals, then shrink sparse evidence toward 0.5:

`Q = 0.5 + confidence * (Q_raw - 0.5)`.

If no quality signal exists, use a conservative prior (`0.35` for tools, `0.50` otherwise) and zero quality confidence. In `native-exacto` mode this score is explanatory only; Exacto remains the runtime ordering authority.

## Fidelity prior

Quantization is a weak prior, not a substitute for measured quality. Defaults:

| Quantization | Prior |
|---|---:|
| fp32/fp16/bf16 | 1.00 |
| fp8/mxfp8 | 0.94 |
| fp6 | 0.89 |
| int8 | 0.88 |
| fp4/mxfp4/nvfp4 | 0.78 |
| int4 | 0.75 |
| unknown | 0.65 |

Keep its top-level weight small (default 0.03). Override or hard-filter quantization when the application has verified requirements.

## Relative normalization

For cost, TPS, TTFT and E2E, normalize inside the current eligible pool using the 10th and 90th percentiles. Cost and latency use log scale. Clamp outliers to `[0,1]`. Missing values receive a low configured score.

```text
N(x) = clamp((x - q10) / (q90 - q10))
```

Invert `N` for lower-is-better metrics.

The relative normalization means scores should not be compared across different models, endpoint pools, dates or workload configurations.

## Composite utility

```text
Speed = wtps*TPS_score + wttft*TTFT_score + we2e*E2E_score

Utility =
    wquality     * Quality
  + wreliability * Reliability
  + wcost        * Cost_score
  + wspeed       * Speed
  + wcache       * Cache_score
  + wfidelity    * Fidelity

Score = clamp(Utility - uncertainty_penalty*(1-data_confidence))
```

Default profiles:

| Profile | Quality | Reliability | Cost | Speed | Cache | Fidelity |
|---|---:|---:|---:|---:|---:|---:|
| agentic-balanced | .30 | .24 | .18 | .18 | .07 | .03 |
| agentic-quality | .42 | .25 | .10 | .15 | .05 | .03 |
| interactive | .20 | .22 | .15 | .33 | .07 | .03 |
| cost | .16 | .22 | .38 | .12 | .09 | .03 |
| batch | .18 | .22 | .28 | .25 | .04 | .03 |

## Stability and fallback diversity

Add a small rank-only hysteresis bonus to providers in the previous order. This prevents frequent changes caused by insignificant metric noise; the displayed diagnostic `score` remains unmodified.

For fallback selection, prefer a new provider family when its rank score is within `diversity.max_score_gap` of the current best remaining endpoint. This reduces correlated failure risk without accepting a materially worse fallback.

Do not infer physical infrastructure independence from provider display names. Diversity here is a best-effort provider-family heuristic.

## Tuning process

1. Start with a built-in profile.
2. Set hard SLO and policy constraints.
3. Backtest against production traces.
4. Optimize weights against a business objective: successful task cost, p95 session latency, gross margin, or task completion rate.
5. Use a holdout period and guard against overfitting.
6. Roll out gradually; compare task-level outcomes, not only endpoint metrics.
