# Input formats

## Endpoint input

Live mode:

```bash
export OPENROUTER_API_KEY='...'
python3 scripts/rank_providers.py --model author/model-slug --config config.json
```

The current Endpoints API may require an OpenRouter management-capable key. If the
key is not authorized, export endpoint JSON from an authorized environment and use
offline mode; never weaken the analysis by substituting remembered provider data.

Offline mode accepts the saved response from:

`GET /api/v1/models/{author}/{slug}/endpoints`

```bash
python3 scripts/rank_providers.py --endpoints-file endpoints.json --config config.json
```

The file may be the full `{ "data": { "id": ..., "endpoints": [...] } }` response or a bare endpoint array.

## Configuration

All fields are optional; omitted values use defaults. Example:

```json
{
  "profile": "agentic-balanced",
  "routing_mode": "auto",
  "deterministic_order": false,
  "max_ranked_providers": 5,
  "workload": {
    "uses_tools": true,
    "streaming": true,
    "expected_prompt_tokens": 24000,
    "expected_completion_tokens": 1800,
    "required_context_tokens": 30000,
    "required_completion_tokens": 4000,
    "required_parameters": ["tools", "tool_choice", "response_format"],
    "expected_requests_per_session": 8,
    "session_id_available": true,
    "cacheable_prompt_fraction": 0.75,
    "assumed_cache_token_hit_rate": 0.0,
    "assumed_cache_write_token_rate": 0.0,
    "assumed_response_cache_hit_rate": 0.0,
    "cache_ttl": "5m"
  },
  "constraints": {
    "only": [],
    "ignore": [],
    "allowed_quantizations": ["bf16", "fp16", "fp8"],
    "allowed_service_tiers": ["default"],
    "require_caching": false,
    "require_unmoderated": false,
    "min_uptime_1d": 0.99,
    "hard_min_throughput_tps": null,
    "hard_max_latency_seconds": null,
    "max_effective_cost_usd": null,
    "max_prompt_price_per_million": 0.50,
    "max_completion_price_per_million": 1.50,
    "max_request_price": 0,
    "data_collection": "deny",
    "zdr": false,
    "preferred_min_throughput": {"p90": 30},
    "preferred_max_latency": {"p90": 3.0}
  },
  "weights": {},
  "speed_mix": {},
  "stability": {"previous_order": [], "switch_margin": 0.03},
  "diversity": {"enabled": true, "max_score_gap": 0.12},
  "routing": {
    "allow_fallbacks": true,
    "strict_hard_constraints": true,
    "include_session_id_placeholder": true
  }
}
```

Important unit rules:

- endpoint pricing input is USD per token/request/unit;
- `max_prompt_price_per_million`, `max_completion_price_per_million`, and OpenRouter `provider.max_price.prompt/completion` are USD per million tokens;
- latency fields are seconds;
- uptime/rates accept either `0..1`, `0..100`, or strings such as `99.9%`;
- benchmark scores accept `0..1`, `0..100`, or percent strings.

### Routing modes

- `auto`: `native-exacto` for tool workloads unless `deterministic_order=true`; otherwise `manual`.
- `native-exacto`: emit `model: ...:exacto`, never emit `provider.order`.
- `manual`: emit ranked `provider.order`.

## Aggregated observations

Object keyed by exact endpoint tag is preferred:

```json
{
  "providers": {
    "provider-a": {
      "requests": 500,
      "request_attempts": 500,
      "request_successes": 496,
      "tool_attempts": 240,
      "tool_successes": 226,
      "observed_tps": 74.2,
      "observed_ttft_seconds": 0.91,
      "prompt_tokens": 12000000,
      "cached_tokens": 6900000,
      "cache_write_tokens": 900000,
      "exacto_score": 83.4,
      "tau_bench": 76.2,
      "gpqa_diamond": 85.1
    }
  }
}
```

Matching order: exact `tag`, `provider_name`, then provider family. Family-level observations applied to a regional/tier variant generate a warning.

## Request-level JSONL telemetry

One JSON object per line. Accepted aliases are intentionally broad:

```json
{"provider_name":"provider-a","success":true,"tool_success":true,"usage":{"prompt_tokens":24000,"completion_tokens":1800,"prompt_tokens_details":{"cached_tokens":16000,"cache_write_tokens":0}},"ttft_ms":820,"generation_time_seconds":18.4,"total_cost":0.0061}
```

The ranker aggregates:

- request and tool success counts;
- prompt/completion/cache-read/cache-write tokens;
- mean observed TPS/TTFT/cost;
- response cache hits;
- optional quality signals.

It also accepts:

- a bare OpenRouter generation record;
- a generation API wrapper such as `{ "data": { ... } }`;
- an array or `{ "data": [...] }` collection of records;
- Chat Completions `usage.prompt_tokens_details` and Responses
  `usage.input_tokens_details` cache fields.

For generation records, `generation_time` and `latency` are interpreted as
milliseconds; explicit `*_seconds` fields take precedence.

Prefer exact endpoint tag when available. OpenRouter generation records may expose provider display name rather than tag; map it explicitly if display names are ambiguous.

## Previous ranking

Pass a prior output file with `--previous-ranking`. The script reads `routing.provider.order`, or falls back to `ranking[].tag`, and applies a small hysteresis bonus.

## Output

JSON output contains:

- `mode`, `profile`, workload and normalized weights;
- `routing_order` and ready-to-use `routing` request fragment;
- diagnostic `ranking` with component scores and raw metrics;
- `excluded` with hard-filter reasons;
- `coverage` and `warnings`.

Markdown output is for human review and contains the ranking table plus request fragment.
