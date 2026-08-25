# OpenRouter Provider Ranking

Rank the provider endpoints behind a single OpenRouter model slug for a specific workload. The skill combines hard compatibility constraints, endpoint performance, workload-aware cost, production telemetry, cache behavior, quality confidence, and fallback diversity into an auditable routing recommendation.

## Install

```bash
npx skills add CodeAlive-AI/ai-driven-development@openrouter-provider-ranking -g -y
```

The bundled ranker requires Python 3.10 or newer and uses only the Python standard library. Live endpoint discovery also requires outbound HTTPS and an OpenRouter key exposed through `OPENROUTER_API_KEY`; offline endpoint JSON works without a key.

## When to use it

Use this skill when you need to:

- compare OpenRouter provider endpoints for one model by throughput, TTFT, end-to-end latency, expected price, uptime, cache behavior, quality, privacy, quantization, or context limits;
- create a deterministic `provider.order` failover chain;
- decide between native `:exacto`, a manual ranking, and OpenRouter's built-in `provider.sort` modes;
- combine OpenRouter endpoint data with provider-tagged production telemetry;
- explain which endpoints were excluded and which signals are missing or uncertain.

It is not a general model-selection skill. Its scope is endpoint-level routing after the OpenRouter model slug is known.

## Quick start

Run against the live OpenRouter Endpoints API:

```bash
cd skills/openrouter-provider-ranking
export OPENROUTER_API_KEY="..."
python3 scripts/rank_providers.py \
  --model deepseek/deepseek-v4-flash-0731 \
  --config assets/config.example.json \
  --format markdown \
  --output recommendation.md
```

Run a reproducible offline analysis:

```bash
python3 scripts/rank_providers.py \
  --endpoints-file endpoints.json \
  --config config.json \
  --observations telemetry.jsonl \
  --previous-ranking previous-result.json \
  --output result.json
```

The output includes the selected routing mode, eligible and excluded endpoints, score components, workload-level expected cost, coverage warnings, and a ready-to-use OpenRouter request fragment.

## Routing modes

| Mode | Best fit | Generated routing |
|------|----------|-------------------|
| `native-exacto` | Tool-calling without a fixed provider order | Uses the model's `:exacto` suffix and omits `provider.sort` and `provider.order` |
| `manual` | Deterministic failover or strong production telemetry | Emits `provider.order` from the computed ranking |
| Native OpenRouter sort | A single simple optimization objective | Uses `provider.sort` for price, throughput, or latency |

The skill treats hard compatibility requirements as filters, never as score penalties that a fast or cheap incompatible endpoint could overcome. Missing quality, cache, or benchmark data receives a conservative prior and an uncertainty penalty instead of invented values.

## Bundled resources

- `scripts/rank_providers.py` — stdlib-only endpoint ranker and routing-fragment generator.
- `scripts/validate_skill.py` — package, syntax, JSON, and unit-test validation.
- `assets/config.example.json` — example tool-using agent workload.
- `assets/observations.example.json` — aggregated provider observations.
- `assets/telemetry.example.jsonl` — request-level production telemetry.
- `references/scoring.md` — scoring formula, normalization, and workload profiles.
- `references/input-formats.md` — configuration and telemetry formats.
- `references/openrouter-routing.md` — OpenRouter routing and caching semantics.
- `tests/trigger-evals.json` — positive and negative activation examples.

## Validate

```bash
cd skills/openrouter-provider-ranking
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## Security

Do not place API keys in configs, telemetry, logs, or generated output. The ranker reads the key from `OPENROUTER_API_KEY` or an explicitly selected environment variable.

## License

MIT
