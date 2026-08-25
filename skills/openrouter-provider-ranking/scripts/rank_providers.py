#!/usr/bin/env python3
"""Rank OpenRouter provider endpoints for a concrete workload.

The script uses only the Python standard library. It can fetch live endpoint data
from OpenRouter or consume a saved Endpoints API response for reproducible runs.

Exit codes:
  0 success
  2 invalid arguments or configuration
  3 authentication/network/API failure
  4 no eligible provider remains after hard constraints
  5 malformed input data
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, MutableMapping, Sequence

EXIT_ARGUMENT = 2
EXIT_NETWORK = 3
EXIT_NO_ELIGIBLE = 4
EXIT_DATA = 5

VIRTUAL_ROUTING_SUFFIXES = (":exacto", ":nitro", ":floor")
TIER_SUFFIXES = {"fast", "priority", "flex"}
QUANTIZATION_GROUPS = {
    "fp8": {"fp8", "mxfp8"},
    "fp4": {"fp4", "mxfp4", "nvfp4"},
}
PRICE_KEYS = {
    "prompt",
    "completion",
    "request",
    "image",
    "web_search",
    "internal_reasoning",
    "input_cache_read",
    "input_cache_write",
    "input_cache_write_1h",
}
OVERRIDE_CONDITION_KEYS = {"min_prompt_tokens", "utc_start", "utc_end", "utc_days"}

PROFILES: dict[str, dict[str, Any]] = {
    "agentic-balanced": {
        "weights": {
            "quality": 0.30,
            "reliability": 0.24,
            "cost": 0.18,
            "speed": 0.18,
            "cache": 0.07,
            "fidelity": 0.03,
        },
        "speed_mix": {"tps": 0.30, "ttft": 0.30, "e2e": 0.40},
    },
    "agentic-quality": {
        "weights": {
            "quality": 0.42,
            "reliability": 0.25,
            "cost": 0.10,
            "speed": 0.15,
            "cache": 0.05,
            "fidelity": 0.03,
        },
        "speed_mix": {"tps": 0.25, "ttft": 0.30, "e2e": 0.45},
    },
    "interactive": {
        "weights": {
            "quality": 0.20,
            "reliability": 0.22,
            "cost": 0.15,
            "speed": 0.33,
            "cache": 0.07,
            "fidelity": 0.03,
        },
        "speed_mix": {"tps": 0.20, "ttft": 0.45, "e2e": 0.35},
    },
    "cost": {
        "weights": {
            "quality": 0.16,
            "reliability": 0.22,
            "cost": 0.38,
            "speed": 0.12,
            "cache": 0.09,
            "fidelity": 0.03,
        },
        "speed_mix": {"tps": 0.30, "ttft": 0.20, "e2e": 0.50},
    },
    "batch": {
        "weights": {
            "quality": 0.18,
            "reliability": 0.22,
            "cost": 0.28,
            "speed": 0.25,
            "cache": 0.04,
            "fidelity": 0.03,
        },
        "speed_mix": {"tps": 0.45, "ttft": 0.10, "e2e": 0.45},
    },
}

DEFAULT_CONFIG: dict[str, Any] = {
    "profile": "agentic-balanced",
    "routing_mode": "auto",
    "deterministic_order": False,
    "max_ranked_providers": 5,
    "workload": {
        "uses_tools": False,
        "streaming": True,
        "expected_prompt_tokens": 10000,
        "expected_completion_tokens": 1000,
        "required_context_tokens": None,
        "required_completion_tokens": None,
        "required_parameters": [],
        "expected_requests_per_session": 1,
        "session_id_available": True,
        "cacheable_prompt_fraction": 1.0,
        "assumed_cache_token_hit_rate": 0.0,
        "assumed_cache_write_token_rate": 0.0,
        "assumed_response_cache_hit_rate": 0.0,
        "cache_ttl": "5m",
    },
    "constraints": {
        "only": [],
        "ignore": [],
        "allowed_quantizations": [],
        "allowed_service_tiers": ["default"],
        "require_caching": False,
        "require_unmoderated": False,
        "min_uptime_1d": 0.0,
        "min_uptime_30m": 0.0,
        "min_uptime_5m": 0.0,
        "hard_min_throughput_tps": None,
        "hard_max_latency_seconds": None,
        "max_effective_cost_usd": None,
        "max_prompt_price_per_million": None,
        "max_completion_price_per_million": None,
        "max_request_price": None,
        "data_collection": None,
        "zdr": False,
        "max_price": {},
        "preferred_min_throughput": None,
        "preferred_max_latency": None,
    },
    "weights": {},
    "speed_mix": {},
    "quality": {
        "unknown_tool_quality": 0.35,
        "unknown_general_quality": 0.50,
        "tool_signal_weights": {
            "tool_success_lcb": 0.45,
            "tau_bench": 0.25,
            "exacto_score": 0.20,
            "gpqa_diamond": 0.05,
            "quality_score": 0.05,
        },
        "general_signal_weights": {
            "quality_score": 0.45,
            "gpqa_diamond": 0.25,
            "exacto_score": 0.15,
            "tau_bench": 0.15,
        },
    },
    "reliability": {
        "uptime_weights": {"5m": 0.50, "30m": 0.30, "1d": 0.20},
        "floor": 0.9700,
        "target": 0.9995,
        "observed_blend_k": 100,
    },
    "scoring": {
        "performance_percentile": "p90",
        "observed_blend_k": 50,
        "missing_normalized_score": 0.15,
        "uncertainty_penalty": 0.06,
    },
    "stability": {
        "previous_order": [],
        "switch_margin": 0.03,
    },
    "diversity": {
        "enabled": True,
        "max_score_gap": 0.12,
    },
    "routing": {
        "allow_fallbacks": True,
        "strict_hard_constraints": True,
        "include_session_id_placeholder": True,
    },
}


class RankingError(RuntimeError):
    def __init__(self, message: str, exit_code: int) -> None:
        super().__init__(message)
        self.exit_code = exit_code


def eprint(*args: object) -> None:
    print(*args, file=sys.stderr)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def parse_number(value: Any) -> float | None:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        if math.isfinite(float(value)):
            return float(value)
        return None
    if isinstance(value, str):
        text = value.strip().lower().replace(",", "")
        if text in {"", "--", "none", "null", "n/a", "na", "unknown"}:
            return None
        text = text.replace("$", "")
        is_percent = text.endswith("%")
        if is_percent:
            text = text[:-1]
        try:
            number = float(text)
        except ValueError:
            return None
        return number / 100.0 if is_percent else number
    return None


def ratio01(value: Any) -> float | None:
    number = parse_number(value)
    if number is None:
        return None
    if number > 1.0 and number <= 100.0:
        number /= 100.0
    return clamp(number)


def uptime_ratio(value: Any) -> float | None:
    return ratio01(value)


def deep_merge(base: MutableMapping[str, Any], override: Mapping[str, Any]) -> MutableMapping[str, Any]:
    for key, value in override.items():
        if isinstance(value, Mapping) and isinstance(base.get(key), MutableMapping):
            deep_merge(base[key], value)  # type: ignore[index]
        else:
            base[key] = deepcopy(value)
    return base


def normalize_weights(weights: Mapping[str, Any], expected: Iterable[str]) -> dict[str, float]:
    result: dict[str, float] = {}
    for key in expected:
        value = parse_number(weights.get(key))
        result[key] = max(0.0, value or 0.0)
    total = sum(result.values())
    if total <= 0:
        raise RankingError("All scoring weights are zero.", EXIT_ARGUMENT)
    return {key: value / total for key, value in result.items()}


def load_json_file(path: str | Path) -> Any:
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise RankingError(f"Input file not found: {path}", EXIT_DATA) from exc
    except json.JSONDecodeError as exc:
        raise RankingError(f"Invalid JSON in {path}: {exc}", EXIT_DATA) from exc
    except OSError as exc:
        raise RankingError(f"Cannot read {path}: {exc}", EXIT_DATA) from exc


def load_config(path: str | None) -> dict[str, Any]:
    config = deepcopy(DEFAULT_CONFIG)
    if path:
        loaded = load_json_file(path)
        if not isinstance(loaded, Mapping):
            raise RankingError("Configuration root must be a JSON object.", EXIT_ARGUMENT)
        deep_merge(config, loaded)

    profile_name = str(config.get("profile", "agentic-balanced"))
    if profile_name not in PROFILES:
        valid = ", ".join(sorted(PROFILES))
        raise RankingError(f"Unknown profile {profile_name!r}. Valid profiles: {valid}.", EXIT_ARGUMENT)
    profile = PROFILES[profile_name]

    weights = deepcopy(profile["weights"])
    weights.update(config.get("weights") or {})
    config["weights"] = normalize_weights(
        weights, ("quality", "reliability", "cost", "speed", "cache", "fidelity")
    )

    speed_mix = deepcopy(profile["speed_mix"])
    speed_mix.update(config.get("speed_mix") or {})
    config["speed_mix"] = normalize_weights(speed_mix, ("tps", "ttft", "e2e"))

    mode = str(config.get("routing_mode", "auto"))
    if mode not in {"auto", "native-exacto", "manual"}:
        raise RankingError("routing_mode must be auto, native-exacto, or manual.", EXIT_ARGUMENT)

    percentile = str(config["scoring"].get("performance_percentile", "p90"))
    if percentile not in {"p50", "p75", "p90", "p99"}:
        raise RankingError("performance_percentile must be p50, p75, p90, or p99.", EXIT_ARGUMENT)

    workload = config["workload"]
    for field in ("expected_prompt_tokens", "expected_completion_tokens", "expected_requests_per_session"):
        value = parse_number(workload.get(field))
        if value is None or value < 0:
            raise RankingError(f"workload.{field} must be a non-negative number.", EXIT_ARGUMENT)
        workload[field] = int(value)

    for field in (
        "cacheable_prompt_fraction",
        "assumed_cache_token_hit_rate",
        "assumed_cache_write_token_rate",
        "assumed_response_cache_hit_rate",
    ):
        value = ratio01(workload.get(field))
        if value is None:
            raise RankingError(f"workload.{field} must be between 0 and 1.", EXIT_ARGUMENT)
        workload[field] = value

    if workload.get("required_context_tokens") is None:
        workload["required_context_tokens"] = (
            workload["expected_prompt_tokens"] + workload["expected_completion_tokens"]
        )
    if workload.get("required_completion_tokens") is None:
        workload["required_completion_tokens"] = workload["expected_completion_tokens"]

    max_ranked = parse_number(config.get("max_ranked_providers"))
    if max_ranked is None or max_ranked < 1:
        raise RankingError("max_ranked_providers must be at least 1.", EXIT_ARGUMENT)
    config["max_ranked_providers"] = int(max_ranked)
    return config


def strip_virtual_suffix(model: str) -> str:
    result = model.strip()
    for suffix in VIRTUAL_ROUTING_SUFFIXES:
        if result.endswith(suffix):
            return result[: -len(suffix)]
    return result


def append_exacto(model: str) -> str:
    model = strip_virtual_suffix(model)
    return model if model.endswith(":exacto") else f"{model}:exacto"


def fetch_endpoint_payload(model: str, api_key_env: str, timeout: float) -> dict[str, Any]:
    base_model = strip_virtual_suffix(model)
    if "/" not in base_model:
        raise RankingError("Model must be in author/slug form.", EXIT_ARGUMENT)
    author, slug = base_model.split("/", 1)
    url = (
        "https://openrouter.ai/api/v1/models/"
        f"{urllib.parse.quote(author, safe='')}/{urllib.parse.quote(slug, safe=':')}/endpoints"
    )
    api_key = os.environ.get(api_key_env)
    if not api_key:
        raise RankingError(
            f"Environment variable {api_key_env} is not set; it is required for live OpenRouter data.",
            EXIT_NETWORK,
        )
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "User-Agent": "openrouter-provider-ranking-skill/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise RankingError(f"OpenRouter Endpoints API returned HTTP {exc.code}: {detail}", EXIT_NETWORK) from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise RankingError(f"Cannot fetch OpenRouter endpoint data: {exc}", EXIT_NETWORK) from exc
    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        raise RankingError("OpenRouter returned malformed JSON.", EXIT_NETWORK) from exc
    if not isinstance(payload, dict):
        raise RankingError("Unexpected OpenRouter endpoint response shape.", EXIT_NETWORK)
    return payload


def extract_endpoints(payload: Any) -> tuple[str, list[dict[str, Any]]]:
    data = payload.get("data", payload) if isinstance(payload, Mapping) else payload
    if isinstance(data, list):
        return "unknown/model", [dict(item) for item in data if isinstance(item, Mapping)]
    if not isinstance(data, Mapping):
        raise RankingError("Endpoint input must contain an object or array.", EXIT_DATA)
    endpoints = data.get("endpoints")
    if not isinstance(endpoints, list):
        raise RankingError("Endpoint input does not contain data.endpoints[].", EXIT_DATA)
    model_id = str(data.get("id") or data.get("model_id") or "unknown/model")
    return model_id, [dict(item) for item in endpoints if isinstance(item, Mapping)]


def nested_get(mapping: Mapping[str, Any], paths: Sequence[str]) -> Any:
    for path in paths:
        current: Any = mapping
        ok = True
        for part in path.split("."):
            if not isinstance(current, Mapping) or part not in current:
                ok = False
                break
            current = current[part]
        if ok:
            return current
    return None


def first_number(mapping: Mapping[str, Any], paths: Sequence[str]) -> float | None:
    return parse_number(nested_get(mapping, paths))


def first_bool(mapping: Mapping[str, Any], paths: Sequence[str]) -> bool | None:
    value = nested_get(mapping, paths)
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "yes", "1", "ok", "success", "passed"}:
            return True
        if lowered in {"false", "no", "0", "error", "failed", "failure"}:
            return False
    return None


def provider_key(record: Mapping[str, Any]) -> str | None:
    value = nested_get(
        record,
        (
            "provider_tag",
            "provider",
            "tag",
            "provider_slug",
            "provider_name",
            "generation.provider_name",
        ),
    )
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def normalize_observation(values: Mapping[str, Any]) -> dict[str, Any]:
    result = dict(values)
    count_pairs = (
        ("tool_success_rate", "tool_successes", "tool_attempts"),
        ("request_success_rate", "request_successes", "request_attempts"),
        ("cache_request_hit_rate", "cache_hit_requests", "requests"),
        ("response_cache_hit_rate", "response_cache_hits", "requests"),
    )
    for rate_key, successes_key, attempts_key in count_pairs:
        if ratio01(result.get(rate_key)) is None:
            successes = parse_number(result.get(successes_key))
            attempts = parse_number(result.get(attempts_key))
            if successes is not None and attempts and attempts > 0:
                result[rate_key] = clamp(successes / attempts)
        else:
            result[rate_key] = ratio01(result.get(rate_key))

    if ratio01(result.get("cache_token_hit_rate")) is None:
        cached = parse_number(result.get("cached_tokens"))
        prompt = parse_number(result.get("prompt_tokens"))
        if cached is not None and prompt and prompt > 0:
            result["cache_token_hit_rate"] = clamp(cached / prompt)
    else:
        result["cache_token_hit_rate"] = ratio01(result.get("cache_token_hit_rate"))

    if ratio01(result.get("cache_write_token_rate")) is None:
        written = parse_number(result.get("cache_write_tokens"))
        prompt = parse_number(result.get("prompt_tokens"))
        if written is not None and prompt and prompt > 0:
            result["cache_write_token_rate"] = clamp(written / prompt)
    else:
        result["cache_write_token_rate"] = ratio01(result.get("cache_write_token_rate"))

    for key in ("exacto_score", "tau_bench", "gpqa_diamond", "quality_score"):
        normalized = ratio01(result.get(key))
        if normalized is not None:
            result[key] = normalized

    for key in (
        "requests",
        "request_attempts",
        "request_successes",
        "tool_attempts",
        "tool_successes",
        "prompt_tokens",
        "cached_tokens",
        "cache_write_tokens",
    ):
        number = parse_number(result.get(key))
        if number is not None:
            result[key] = number
    for key in ("observed_tps", "observed_ttft_seconds", "observed_cost_usd"):
        number = parse_number(result.get(key))
        if number is not None:
            result[key] = number
    return result


def aggregate_raw_observations(records: Sequence[Mapping[str, Any]]) -> dict[str, dict[str, Any]]:
    buckets: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "requests": 0,
            "request_attempts": 0,
            "request_successes": 0,
            "tool_attempts": 0,
            "tool_successes": 0,
            "prompt_tokens": 0.0,
            "cached_tokens": 0.0,
            "cache_write_tokens": 0.0,
            "completion_tokens": 0.0,
            "cache_hit_requests": 0,
            "response_cache_hits": 0,
            "_tps_values": [],
            "_ttft_values": [],
            "_cost_values": [],
            "_quality_values": defaultdict(list),
        }
    )
    for record in records:
        key = provider_key(record)
        if not key:
            continue
        bucket = buckets[key]
        bucket["requests"] += 1
        bucket["request_attempts"] += 1

        success = first_bool(record, ("success", "request_success", "ok"))
        if success is None:
            status = first_number(record, ("status_code", "http_status", "status"))
            success = status is not None and 200 <= status < 300
        if success:
            bucket["request_successes"] += 1

        tool_success = first_bool(record, ("tool_success", "tool_call_success", "schema_valid"))
        if tool_success is not None:
            bucket["tool_attempts"] += 1
            if tool_success:
                bucket["tool_successes"] += 1

        prompt_tokens = first_number(
            record,
            (
                "prompt_tokens",
                "input_tokens",
                "tokens_prompt",
                "native_tokens_prompt",
                "usage.prompt_tokens",
                "usage.input_tokens",
            ),
        ) or 0.0
        cached_tokens = first_number(
            record,
            (
                "cached_tokens",
                "native_tokens_cached",
                "usage.prompt_tokens_details.cached_tokens",
                "usage.input_tokens_details.cached_tokens",
            ),
        ) or 0.0
        write_tokens = first_number(
            record,
            (
                "cache_write_tokens",
                "usage.prompt_tokens_details.cache_write_tokens",
                "usage.input_tokens_details.cache_write_tokens",
            ),
        ) or 0.0
        completion_tokens = first_number(
            record,
            (
                "completion_tokens",
                "output_tokens",
                "tokens_completion",
                "native_tokens_completion",
                "usage.completion_tokens",
                "usage.output_tokens",
            ),
        ) or 0.0
        bucket["prompt_tokens"] += max(0.0, prompt_tokens)
        bucket["cached_tokens"] += max(0.0, cached_tokens)
        bucket["cache_write_tokens"] += max(0.0, write_tokens)
        bucket["completion_tokens"] += max(0.0, completion_tokens)
        if cached_tokens > 0:
            bucket["cache_hit_requests"] += 1

        response_cache_hit = first_bool(record, ("response_cache_hit",))
        if response_cache_hit is None:
            response_cache_hit = bool(nested_get(record, ("response_cache_source_id",)))
        if response_cache_hit:
            bucket["response_cache_hits"] += 1

        tps = first_number(record, ("observed_tps", "tps", "throughput_tps"))
        if tps is None and completion_tokens > 0:
            generation_seconds = first_number(
                record,
                ("generation_seconds", "generation_time_seconds", "generation_time_s"),
            )
            if generation_seconds is None:
                # OpenRouter generation records define generation_time in milliseconds.
                generation_ms = first_number(record, ("generation_time_ms", "generation_time"))
                if generation_ms is not None:
                    generation_seconds = generation_ms / 1000.0
            if generation_seconds and generation_seconds > 0:
                tps = completion_tokens / generation_seconds
        if tps is not None and tps > 0:
            bucket["_tps_values"].append(tps)

        ttft = first_number(
            record,
            ("observed_ttft_seconds", "ttft_seconds", "time_to_first_token_seconds"),
        )
        if ttft is None:
            # OpenRouter generation records expose first-token latency as `latency`
            # in milliseconds. Keep explicit second-based fields higher priority.
            ttft_ms = first_number(
                record, ("ttft_ms", "time_to_first_token_ms", "latency_ms", "latency")
            )
            if ttft_ms is not None:
                ttft = ttft_ms / 1000.0
        if ttft is not None and ttft >= 0:
            bucket["_ttft_values"].append(ttft)

        cost = first_number(record, ("cost_usd", "total_cost", "usage"))
        if cost is not None and cost >= 0:
            bucket["_cost_values"].append(cost)

        for quality_key in ("exacto_score", "tau_bench", "gpqa_diamond", "quality_score"):
            quality_value = ratio01(record.get(quality_key))
            if quality_value is not None:
                bucket["_quality_values"][quality_key].append(quality_value)

    output: dict[str, dict[str, Any]] = {}
    for key, bucket in buckets.items():
        tps_values = bucket.pop("_tps_values")
        ttft_values = bucket.pop("_ttft_values")
        cost_values = bucket.pop("_cost_values")
        quality_values = bucket.pop("_quality_values")
        if tps_values:
            bucket["observed_tps"] = sum(tps_values) / len(tps_values)
        if ttft_values:
            bucket["observed_ttft_seconds"] = sum(ttft_values) / len(ttft_values)
        if cost_values:
            bucket["observed_cost_usd"] = sum(cost_values) / len(cost_values)
        for quality_key, values in quality_values.items():
            if values:
                bucket[quality_key] = sum(values) / len(values)
        output[key] = normalize_observation(bucket)
    return output


def load_observations(path: str | None) -> dict[str, dict[str, Any]]:
    if not path:
        return {}
    text: str
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        raise RankingError(f"Cannot read observations file {path}: {exc}", EXIT_DATA) from exc

    parsed: Any
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        records: list[Mapping[str, Any]] = []
        for line_number, line in enumerate(text.splitlines(), start=1):
            if not line.strip():
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RankingError(
                    f"Invalid JSONL at {path}:{line_number}: {exc}", EXIT_DATA
                ) from exc
            if not isinstance(item, Mapping):
                raise RankingError(f"JSONL record {line_number} must be an object.", EXIT_DATA)
            records.append(item)
        return aggregate_raw_observations(records)

    if isinstance(parsed, list):
        records = [item for item in parsed if isinstance(item, Mapping)]
        return aggregate_raw_observations(records)
    if not isinstance(parsed, Mapping):
        raise RankingError("Observations must be a JSON object, array, or JSONL.", EXIT_DATA)

    # Accept raw OpenRouter generation API responses (`{"data": {...}}`),
    # bare generation records, and collection wrappers in addition to the
    # preferred aggregated `providers` mapping.
    data = parsed.get("data")
    if isinstance(data, Mapping) and provider_key(data):
        return aggregate_raw_observations([data])
    if isinstance(data, list):
        records = [item for item in data if isinstance(item, Mapping)]
        if records and any(provider_key(item) for item in records):
            return aggregate_raw_observations(records)
    if provider_key(parsed):
        return aggregate_raw_observations([parsed])

    providers = parsed.get("providers", parsed)
    if isinstance(providers, list):
        records = [item for item in providers if isinstance(item, Mapping)]
        return aggregate_raw_observations(records)
    if not isinstance(providers, Mapping):
        raise RankingError("observations.providers must be an object or array.", EXIT_DATA)

    result: dict[str, dict[str, Any]] = {}
    for key, value in providers.items():
        if isinstance(value, Mapping):
            result[str(key)] = normalize_observation(value)
    return result


def observation_for_endpoint(
    endpoint: Mapping[str, Any], observations: Mapping[str, Mapping[str, Any]]
) -> tuple[dict[str, Any], str | None]:
    if not observations:
        return {}, None
    lower_map = {str(key).lower(): value for key, value in observations.items()}
    tag = str(endpoint.get("tag") or "").strip()
    provider_name = str(endpoint.get("provider_name") or "").strip()
    family = tag.split("/", 1)[0] if tag else ""
    for candidate, match_kind in (
        (tag, "tag"),
        (provider_name, "provider_name"),
        (family, "provider_family"),
    ):
        if candidate and candidate.lower() in lower_map:
            return dict(lower_map[candidate.lower()]), match_kind
    return {}, None


def parse_iso_datetime(value: str | None) -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    text = value.strip().replace("Z", "+00:00")
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError as exc:
        raise RankingError("--at-utc must be an ISO-8601 timestamp.", EXIT_ARGUMENT) from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def hhmm_in_window(now_hhmm: int, start: int, end: int) -> bool:
    if start == end:
        return True
    if start < end:
        return start <= now_hhmm < end
    return now_hhmm >= start or now_hhmm < end


def pricing_override_matches(
    override: Mapping[str, Any], prompt_tokens: int, at_utc: datetime
) -> bool:
    unknown_conditions = {
        key
        for key in override
        if key not in PRICE_KEYS and key not in OVERRIDE_CONDITION_KEYS
    }
    if unknown_conditions:
        return False

    min_prompt = parse_number(override.get("min_prompt_tokens"))
    if min_prompt is not None and not (prompt_tokens > min_prompt):
        return False

    days = override.get("utc_days")
    if days is not None:
        if not isinstance(days, Sequence) or isinstance(days, (str, bytes)):
            return False
        current_day = at_utc.strftime("%A").lower()
        allowed_days = {str(day).lower() for day in days}
        if current_day not in allowed_days:
            return False

    start = parse_number(override.get("utc_start"))
    end = parse_number(override.get("utc_end"))
    if start is not None or end is not None:
        if start is None or end is None:
            return False
        now_hhmm = at_utc.hour * 100 + at_utc.minute
        if not hhmm_in_window(now_hhmm, int(start), int(end)):
            return False
    return True


def resolve_pricing(
    raw_pricing: Any, prompt_tokens: int, at_utc: datetime
) -> tuple[dict[str, float | None], list[str]]:
    warnings: list[str] = []
    if not isinstance(raw_pricing, Mapping):
        return {key: None for key in PRICE_KEYS}, ["pricing object is missing"]

    resolved: dict[str, float | None] = {
        key: parse_number(raw_pricing.get(key)) for key in PRICE_KEYS
    }
    overrides = raw_pricing.get("overrides")
    if isinstance(overrides, list):
        for index, override in enumerate(overrides):
            if not isinstance(override, Mapping):
                warnings.append(f"pricing override {index} is not an object and was ignored")
                continue
            unknown_conditions = {
                key
                for key in override
                if key not in PRICE_KEYS and key not in OVERRIDE_CONDITION_KEYS
            }
            if unknown_conditions:
                warnings.append(
                    "pricing override ignored because it contains unknown condition fields: "
                    + ", ".join(sorted(unknown_conditions))
                )
                continue
            if pricing_override_matches(override, prompt_tokens, at_utc):
                for key in PRICE_KEYS:
                    if key in override:
                        resolved[key] = parse_number(override.get(key))

    discount = ratio01(raw_pricing.get("discount"))
    if discount is not None and discount > 0:
        multiplier = 1.0 - discount
        for key, value in list(resolved.items()):
            if value is not None:
                resolved[key] = value * multiplier
    return resolved, warnings


def endpoint_active(status: Any) -> bool:
    if status is None:
        return True
    if isinstance(status, bool):
        return status is False
    if isinstance(status, (int, float)):
        return int(status) in {0, 200}
    lowered = str(status).strip().lower()
    return lowered in {"0", "200", "active", "operational", "ok", "available", "healthy"}


def endpoint_service_tier(tag: str) -> str:
    parts = tag.lower().split("/")
    if len(parts) > 1 and parts[-1] in TIER_SUFFIXES:
        return "priority" if parts[-1] == "fast" else parts[-1]
    return "default"


def slug_matches(rule: str, tag: str) -> bool:
    rule_l = rule.strip().lower().rstrip("/")
    tag_l = tag.strip().lower().rstrip("/")
    if not rule_l or not tag_l:
        return False
    if rule_l == tag_l:
        return True
    if not tag_l.startswith(rule_l + "/"):
        return False
    first_suffix = tag_l[len(rule_l) + 1 :].split("/", 1)[0]
    return first_suffix not in TIER_SUFFIXES


def quantization_matches(actual: str, allowed: Iterable[str]) -> bool:
    actual_l = actual.strip().lower()
    allowed_l = {str(item).strip().lower() for item in allowed if str(item).strip()}
    if not allowed_l:
        return True
    for requested in allowed_l:
        if actual_l in QUANTIZATION_GROUPS.get(requested, {requested}):
            return True
    return False


def percentile_value(endpoint: Mapping[str, Any], field: str, percentile: str) -> float | None:
    values = endpoint.get(field)
    if not isinstance(values, Mapping):
        return None
    preferred = parse_number(values.get(percentile))
    if preferred is not None:
        return preferred
    for fallback in ("p50", "p75", "p90", "p99"):
        value = parse_number(values.get(fallback))
        if value is not None:
            return value
    return None


def blend_observed(base: float | None, observed: float | None, sample_count: float, k: float) -> float | None:
    if observed is None:
        return base
    if base is None:
        return observed
    alpha = sample_count / (sample_count + max(1.0, k))
    return alpha * observed + (1.0 - alpha) * base


def wilson_lower(successes: float, attempts: float, z: float = 1.96) -> float | None:
    if attempts <= 0:
        return None
    successes = clamp(successes, 0.0, attempts)
    p = successes / attempts
    z2 = z * z
    denominator = 1.0 + z2 / attempts
    centre = p + z2 / (2.0 * attempts)
    margin = z * math.sqrt((p * (1.0 - p) + z2 / (4.0 * attempts)) / attempts)
    return clamp((centre - margin) / denominator)


def smooth_slo(value: float | None, floor: float, target: float) -> float:
    if value is None:
        return 0.15
    if target <= floor:
        return clamp(value)
    x = clamp((value - floor) / (target - floor))
    return x * x * (3.0 - 2.0 * x)


def reliability_score(
    endpoint: Mapping[str, Any], observation: Mapping[str, Any], config: Mapping[str, Any]
) -> tuple[float, float | None, float | None]:
    rel_cfg = config["reliability"]
    window_values = {
        "5m": uptime_ratio(endpoint.get("uptime_last_5m")),
        "30m": uptime_ratio(endpoint.get("uptime_last_30m")),
        "1d": uptime_ratio(endpoint.get("uptime_last_1d")),
    }
    weighted_sum = 0.0
    weight_sum = 0.0
    for window, weight_raw in rel_cfg.get("uptime_weights", {}).items():
        value = window_values.get(window)
        weight = parse_number(weight_raw) or 0.0
        if value is not None and weight > 0:
            weighted_sum += value * weight
            weight_sum += weight
    endpoint_uptime = weighted_sum / weight_sum if weight_sum > 0 else None
    endpoint_score = smooth_slo(
        endpoint_uptime,
        float(rel_cfg.get("floor", 0.97)),
        float(rel_cfg.get("target", 0.9995)),
    )

    attempts = parse_number(observation.get("request_attempts"))
    if attempts is None:
        attempts = parse_number(observation.get("requests")) or 0.0
    successes = parse_number(observation.get("request_successes"))
    observed_lcb: float | None = None
    if successes is not None and attempts > 0:
        observed_lcb = wilson_lower(successes, attempts)
    elif ratio01(observation.get("request_success_rate")) is not None:
        observed_lcb = ratio01(observation.get("request_success_rate"))

    if observed_lcb is None:
        return endpoint_score, endpoint_uptime, None
    k = float(rel_cfg.get("observed_blend_k", 100))
    alpha = attempts / (attempts + max(1.0, k))
    observed_score = smooth_slo(
        observed_lcb,
        float(rel_cfg.get("floor", 0.97)),
        float(rel_cfg.get("target", 0.9995)),
    )
    return alpha * observed_score + (1.0 - alpha) * endpoint_score, endpoint_uptime, observed_lcb


def weighted_available(values: Mapping[str, float | None], weights: Mapping[str, Any]) -> float | None:
    numerator = 0.0
    denominator = 0.0
    for key, weight_raw in weights.items():
        value = values.get(key)
        weight = parse_number(weight_raw) or 0.0
        if value is not None and weight > 0:
            numerator += value * weight
            denominator += weight
    return numerator / denominator if denominator > 0 else None


def quality_score(
    observation: Mapping[str, Any], uses_tools: bool, config: Mapping[str, Any]
) -> tuple[float, float, dict[str, float]]:
    attempts = parse_number(observation.get("tool_attempts")) or 0.0
    successes = parse_number(observation.get("tool_successes"))
    tool_lcb: float | None = None
    if successes is not None and attempts > 0:
        tool_lcb = wilson_lower(successes, attempts)
    elif ratio01(observation.get("tool_success_rate")) is not None:
        tool_lcb = ratio01(observation.get("tool_success_rate"))

    signals: dict[str, float | None] = {
        "tool_success_lcb": tool_lcb,
        "tau_bench": ratio01(observation.get("tau_bench")),
        "exacto_score": ratio01(observation.get("exacto_score")),
        "gpqa_diamond": ratio01(observation.get("gpqa_diamond")),
        "quality_score": ratio01(observation.get("quality_score")),
    }
    quality_cfg = config["quality"]
    weights = quality_cfg["tool_signal_weights" if uses_tools else "general_signal_weights"]
    raw = weighted_available(signals, weights)
    if raw is None:
        unknown = float(
            quality_cfg["unknown_tool_quality" if uses_tools else "unknown_general_quality"]
        )
        return clamp(unknown), 0.0, {}

    available = {key: value for key, value in signals.items() if value is not None}
    non_telemetry_count = sum(1 for key in available if key != "tool_success_lcb")
    telemetry_confidence = min(1.0, attempts / 100.0) if tool_lcb is not None else 0.0
    confidence = clamp(0.45 * telemetry_confidence + 0.25 * min(2, non_telemetry_count))
    # Shrink sparse evidence toward a neutral prior rather than over-ranking one noisy score.
    shrunk = 0.5 + confidence * (raw - 0.5)
    return clamp(shrunk), confidence, {key: float(value) for key, value in available.items()}


def fidelity_score(quantization: Any) -> float:
    quant = str(quantization or "unknown").strip().lower()
    mapping = {
        "fp32": 1.00,
        "fp16": 1.00,
        "bf16": 1.00,
        "fp8": 0.94,
        "mxfp8": 0.94,
        "fp6": 0.89,
        "int8": 0.88,
        "fp4": 0.78,
        "mxfp4": 0.78,
        "nvfp4": 0.78,
        "int4": 0.75,
        "unknown": 0.65,
    }
    return mapping.get(quant, 0.65)


def cache_and_cost(
    pricing: Mapping[str, float | None],
    endpoint: Mapping[str, Any],
    observation: Mapping[str, Any],
    config: Mapping[str, Any],
) -> tuple[float | None, dict[str, float], float, list[str]]:
    workload = config["workload"]
    warnings: list[str] = []
    prompt_tokens = float(workload["expected_prompt_tokens"])
    completion_tokens = float(workload["expected_completion_tokens"])
    cacheable_fraction = float(workload["cacheable_prompt_fraction"])

    prompt_price = pricing.get("prompt")
    completion_price = pricing.get("completion")
    request_price = pricing.get("request") or 0.0
    if prompt_price is None or completion_price is None:
        return None, {}, 0.0, ["prompt or completion price is missing"]

    cache_read_price = pricing.get("input_cache_read")
    cache_ttl = str(workload.get("cache_ttl", "5m")).lower()
    cache_write_price = (
        pricing.get("input_cache_write_1h")
        if cache_ttl == "1h" and pricing.get("input_cache_write_1h") is not None
        else pricing.get("input_cache_write")
    )
    cache_capable = bool(endpoint.get("supports_implicit_caching")) or cache_read_price is not None

    observed_hit = ratio01(observation.get("cache_token_hit_rate"))
    observed_write = ratio01(observation.get("cache_write_token_rate"))
    hit_rate = (
        observed_hit
        if observed_hit is not None
        else float(workload.get("assumed_cache_token_hit_rate", 0.0))
    )
    write_rate = (
        observed_write
        if observed_write is not None
        else float(workload.get("assumed_cache_write_token_rate", 0.0))
    )
    response_hit_rate = ratio01(observation.get("response_cache_hit_rate"))
    if response_hit_rate is None:
        response_hit_rate = float(workload.get("assumed_response_cache_hit_rate", 0.0))

    if not cache_capable:
        if hit_rate > 0 or write_rate > 0:
            warnings.append("cache hit/write assumptions ignored because endpoint has no cache signal")
        hit_rate = 0.0
        write_rate = 0.0
    hit_rate = min(clamp(hit_rate), cacheable_fraction)
    write_rate = min(clamp(write_rate), cacheable_fraction)
    if hit_rate + write_rate > 1.0:
        write_rate = max(0.0, 1.0 - hit_rate)

    cached_tokens = prompt_tokens * hit_rate
    write_tokens = prompt_tokens * write_rate
    uncached_tokens = max(0.0, prompt_tokens - cached_tokens - write_tokens)
    effective_cache_read_price = cache_read_price if cache_read_price is not None else prompt_price
    effective_cache_write_price = cache_write_price if cache_write_price is not None else prompt_price

    upstream_cost = (
        uncached_tokens * prompt_price
        + cached_tokens * effective_cache_read_price
        + write_tokens * effective_cache_write_price
        + completion_tokens * completion_price
        + request_price
    )
    expected_cost = upstream_cost * (1.0 - clamp(response_hit_rate))

    sessions = int(workload.get("expected_requests_per_session", 1))
    session_cache_eligible = bool(workload.get("session_id_available")) and sessions > 1
    cache_score_value = 0.85 * hit_rate + 0.15 * (1.0 if cache_capable and session_cache_eligible else 0.0)
    breakdown = {
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "cached_prompt_tokens": cached_tokens,
        "cache_write_tokens": write_tokens,
        "uncached_prompt_tokens": uncached_tokens,
        "cache_token_hit_rate": hit_rate,
        "cache_write_token_rate": write_rate,
        "response_cache_hit_rate": clamp(response_hit_rate),
        "upstream_cost_before_response_cache_usd": upstream_cost,
    }
    return expected_cost, breakdown, clamp(cache_score_value), warnings


def robust_quantile(sorted_values: Sequence[float], q: float) -> float:
    if not sorted_values:
        raise ValueError("quantile requires values")
    if len(sorted_values) == 1:
        return sorted_values[0]
    position = (len(sorted_values) - 1) * q
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return sorted_values[lower]
    fraction = position - lower
    return sorted_values[lower] * (1.0 - fraction) + sorted_values[upper] * fraction


def normalized_metric_scores(
    candidates: Sequence[Mapping[str, Any]],
    key: str,
    *,
    lower_is_better: bool,
    log_scale: bool,
    missing_score: float,
) -> dict[str, float]:
    transformed: list[float] = []
    values_by_tag: dict[str, float | None] = {}
    for candidate in candidates:
        tag = str(candidate["tag"])
        raw = parse_number(candidate["metrics"].get(key))
        if raw is None or (log_scale and raw < 0):
            values_by_tag[tag] = None
            continue
        value = math.log(max(raw, 1e-12)) if log_scale else raw
        values_by_tag[tag] = value
        transformed.append(value)

    if not transformed:
        return {str(candidate["tag"]): missing_score for candidate in candidates}
    transformed.sort()
    low = robust_quantile(transformed, 0.10)
    high = robust_quantile(transformed, 0.90)
    if math.isclose(low, high, rel_tol=1e-12, abs_tol=1e-12):
        return {
            str(candidate["tag"]): (0.5 if values_by_tag[str(candidate["tag"])] is not None else missing_score)
            for candidate in candidates
        }

    output: dict[str, float] = {}
    for tag, value in values_by_tag.items():
        if value is None:
            output[tag] = missing_score
            continue
        relative = clamp((value - low) / (high - low))
        output[tag] = 1.0 - relative if lower_is_better else relative
    return output


def hard_filter_reasons(
    endpoint: Mapping[str, Any],
    tag: str,
    pricing: Mapping[str, float | None],
    tps: float | None,
    latency: float | None,
    config: Mapping[str, Any],
) -> list[str]:
    workload = config["workload"]
    constraints = config["constraints"]
    reasons: list[str] = []

    if not endpoint_active(endpoint.get("status")):
        reasons.append("endpoint status is not active")

    only = [str(item) for item in constraints.get("only") or []]
    ignore = [str(item) for item in constraints.get("ignore") or []]
    if only and not any(slug_matches(rule, tag) for rule in only):
        reasons.append("not in constraints.only")
    if any(slug_matches(rule, tag) for rule in ignore):
        reasons.append("matched constraints.ignore")

    allowed_tiers = {str(item).lower() for item in constraints.get("allowed_service_tiers") or []}
    tier = endpoint_service_tier(tag)
    if allowed_tiers and tier not in allowed_tiers:
        reasons.append(f"service tier {tier!r} is not allowed")

    quantization = str(endpoint.get("quantization") or "unknown").lower()
    allowed_quantizations = [
        str(item).lower() for item in constraints.get("allowed_quantizations") or []
    ]
    if not quantization_matches(quantization, allowed_quantizations):
        reasons.append(f"quantization {quantization!r} is not allowed")

    required_context = int(workload.get("required_context_tokens") or 0)
    context_length = parse_number(endpoint.get("context_length"))
    if context_length is not None and context_length < required_context:
        reasons.append(f"context_length {int(context_length)} < required {required_context}")

    expected_prompt = int(workload.get("expected_prompt_tokens") or 0)
    max_prompt = parse_number(endpoint.get("max_prompt_tokens"))
    if max_prompt is not None and max_prompt < expected_prompt:
        reasons.append(f"max_prompt_tokens {int(max_prompt)} < expected {expected_prompt}")

    required_completion = int(workload.get("required_completion_tokens") or 0)
    max_completion = parse_number(endpoint.get("max_completion_tokens"))
    if max_completion is not None and max_completion < required_completion:
        reasons.append(
            f"max_completion_tokens {int(max_completion)} < required {required_completion}"
        )

    required_parameters = {
        str(item) for item in (workload.get("required_parameters") or [])
    }
    supported = {str(item) for item in (endpoint.get("supported_parameters") or [])}
    missing_parameters = sorted(required_parameters - supported)
    if missing_parameters:
        reasons.append("missing required parameters: " + ", ".join(missing_parameters))

    if constraints.get("require_caching"):
        cache_capable = bool(endpoint.get("supports_implicit_caching")) or pricing.get("input_cache_read") is not None
        if not cache_capable:
            reasons.append("caching is required but endpoint exposes no cache support")

    if constraints.get("require_unmoderated") and endpoint.get("is_moderated") is True:
        reasons.append("moderated endpoint is disallowed")

    uptime_checks = (
        ("uptime_last_1d", "min_uptime_1d"),
        ("uptime_last_30m", "min_uptime_30m"),
        ("uptime_last_5m", "min_uptime_5m"),
    )
    for endpoint_key, constraint_key in uptime_checks:
        minimum = ratio01(constraints.get(constraint_key)) or 0.0
        value = uptime_ratio(endpoint.get(endpoint_key))
        if minimum > 0 and (value is None or value < minimum):
            shown = "unknown" if value is None else f"{value * 100:.3f}%"
            reasons.append(f"{endpoint_key} {shown} < required {minimum * 100:.3f}%")

    min_tps = parse_number(constraints.get("hard_min_throughput_tps"))
    if min_tps is not None and (tps is None or tps < min_tps):
        reasons.append(f"throughput {tps if tps is not None else 'unknown'} < {min_tps} tps")
    max_latency = parse_number(constraints.get("hard_max_latency_seconds"))
    if max_latency is not None and (latency is None or latency > max_latency):
        reasons.append(
            f"latency {latency if latency is not None else 'unknown'} > {max_latency} seconds"
        )

    prompt_cap = parse_number(constraints.get("max_prompt_price_per_million"))
    completion_cap = parse_number(constraints.get("max_completion_price_per_million"))
    request_cap = parse_number(constraints.get("max_request_price"))
    prompt_price = pricing.get("prompt")
    completion_price = pricing.get("completion")
    request_price = pricing.get("request") or 0.0
    if prompt_cap is not None and (prompt_price is None or prompt_price * 1_000_000 > prompt_cap):
        reasons.append("prompt price exceeds configured cap")
    if completion_cap is not None and (
        completion_price is None or completion_price * 1_000_000 > completion_cap
    ):
        reasons.append("completion price exceeds configured cap")
    if request_cap is not None and request_price > request_cap:
        reasons.append("per-request price exceeds configured cap")
    return reasons


def data_confidence(metrics: Mapping[str, Any], uses_tools: bool) -> float:
    checks: list[tuple[bool, float]] = [
        (metrics.get("expected_cost_usd") is not None, 0.25),
        (metrics.get("throughput_tps") is not None, 0.20),
        (metrics.get("latency_seconds") is not None, 0.15),
        (metrics.get("endpoint_uptime") is not None, 0.20),
        (metrics.get("quality_confidence", 0.0) > 0, 0.20 if uses_tools else 0.05),
    ]
    denominator = sum(weight for _, weight in checks)
    numerator = sum(weight for present, weight in checks if present)
    return numerator / denominator if denominator > 0 else 0.0


def evaluate_candidates(
    endpoints: Sequence[Mapping[str, Any]],
    observations: Mapping[str, Mapping[str, Any]],
    config: Mapping[str, Any],
    at_utc: datetime,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    percentile = str(config["scoring"]["performance_percentile"])
    blend_k = float(config["scoring"].get("observed_blend_k", 50))
    workload = config["workload"]
    uses_tools = bool(workload.get("uses_tools"))
    candidates: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []

    for endpoint in endpoints:
        tag = str(endpoint.get("tag") or "").strip()
        if not tag:
            excluded.append({"tag": None, "provider": endpoint.get("provider_name"), "reasons": ["missing endpoint tag"]})
            continue
        observation, observation_match = observation_for_endpoint(endpoint, observations)
        sample_count = parse_number(observation.get("requests")) or parse_number(
            observation.get("request_attempts")
        ) or 0.0

        pricing, pricing_warnings = resolve_pricing(
            endpoint.get("pricing"), int(workload["expected_prompt_tokens"]), at_utc
        )
        endpoint_tps = percentile_value(endpoint, "throughput_last_30m", percentile)
        endpoint_latency = percentile_value(endpoint, "latency_last_30m", percentile)
        tps = blend_observed(
            endpoint_tps,
            parse_number(observation.get("observed_tps")),
            sample_count,
            blend_k,
        )
        latency = blend_observed(
            endpoint_latency,
            parse_number(observation.get("observed_ttft_seconds")),
            sample_count,
            blend_k,
        )

        reasons = hard_filter_reasons(endpoint, tag, pricing, tps, latency, config)
        if reasons:
            excluded.append(
                {
                    "tag": tag,
                    "provider": endpoint.get("provider_name"),
                    "reasons": reasons,
                }
            )
            continue

        reliability, endpoint_uptime, observed_success_lcb = reliability_score(
            endpoint, observation, config
        )
        quality, quality_confidence, quality_signals = quality_score(
            observation, uses_tools, config
        )
        expected_cost, cost_breakdown, cache_score_value, cache_warnings = cache_and_cost(
            pricing, endpoint, observation, config
        )
        if expected_cost is None:
            excluded.append(
                {
                    "tag": tag,
                    "provider": endpoint.get("provider_name"),
                    "reasons": ["cannot compute cost because prompt/completion pricing is missing"],
                }
            )
            continue
        max_effective_cost = parse_number(config["constraints"].get("max_effective_cost_usd"))
        if max_effective_cost is not None and expected_cost > max_effective_cost:
            excluded.append(
                {
                    "tag": tag,
                    "provider": endpoint.get("provider_name"),
                    "reasons": [
                        f"expected cost ${expected_cost:.8f} exceeds cap ${max_effective_cost:.8f}"
                    ],
                }
            )
            continue

        completion_tokens = float(workload["expected_completion_tokens"])
        e2e_seconds = None
        if tps is not None and tps > 0:
            e2e_seconds = (latency or 0.0) + completion_tokens / tps

        metrics: dict[str, Any] = {
            "throughput_tps": tps,
            "endpoint_throughput_tps": endpoint_tps,
            "latency_seconds": latency,
            "endpoint_latency_seconds": endpoint_latency,
            "estimated_e2e_seconds": e2e_seconds,
            "expected_cost_usd": expected_cost,
            "prompt_price_per_million": (
                pricing["prompt"] * 1_000_000 if pricing.get("prompt") is not None else None
            ),
            "completion_price_per_million": (
                pricing["completion"] * 1_000_000
                if pricing.get("completion") is not None
                else None
            ),
            "cache_read_price_per_million": (
                pricing["input_cache_read"] * 1_000_000
                if pricing.get("input_cache_read") is not None
                else None
            ),
            "endpoint_uptime": endpoint_uptime,
            "observed_request_success_lcb": observed_success_lcb,
            "quality_confidence": quality_confidence,
            "quality_signals": quality_signals,
            "observation_match": observation_match,
            "observation_requests": sample_count,
            "context_length": parse_number(endpoint.get("context_length")),
            "max_completion_tokens": parse_number(endpoint.get("max_completion_tokens")),
            "quantization": endpoint.get("quantization") or "unknown",
            "service_tier": endpoint_service_tier(tag),
            **cost_breakdown,
        }
        confidence = data_confidence(metrics, uses_tools)
        warnings = pricing_warnings + cache_warnings
        if observation_match == "provider_family" and "/" in tag:
            warnings.append("provider-family observations were applied to a specific endpoint variant")
        if not quality_signals and uses_tools:
            warnings.append("no provider-specific Exacto/tool-quality signal; conservative prior used")
        if tps is None:
            warnings.append("throughput metric is missing")
        if latency is None:
            warnings.append("latency metric is missing")

        candidates.append(
            {
                "tag": tag,
                "provider": endpoint.get("provider_name") or endpoint.get("name") or tag,
                "name": endpoint.get("name") or tag,
                "components": {
                    "quality": quality,
                    "reliability": reliability,
                    "cache": cache_score_value,
                    "fidelity": fidelity_score(endpoint.get("quantization")),
                },
                "metrics": metrics,
                "data_confidence": confidence,
                "warnings": warnings,
            }
        )
    return candidates, excluded


def score_candidates(candidates: list[dict[str, Any]], config: Mapping[str, Any]) -> None:
    missing_score = float(config["scoring"].get("missing_normalized_score", 0.15))
    cost_scores = normalized_metric_scores(
        candidates,
        "expected_cost_usd",
        lower_is_better=True,
        log_scale=True,
        missing_score=missing_score,
    )
    tps_scores = normalized_metric_scores(
        candidates,
        "throughput_tps",
        lower_is_better=False,
        log_scale=False,
        missing_score=missing_score,
    )
    ttft_scores = normalized_metric_scores(
        candidates,
        "latency_seconds",
        lower_is_better=True,
        log_scale=True,
        missing_score=missing_score,
    )
    e2e_scores = normalized_metric_scores(
        candidates,
        "estimated_e2e_seconds",
        lower_is_better=True,
        log_scale=True,
        missing_score=missing_score,
    )

    weights = config["weights"]
    speed_mix = config["speed_mix"]
    uncertainty_penalty = float(config["scoring"].get("uncertainty_penalty", 0.06))
    previous_order = [str(item) for item in config["stability"].get("previous_order") or []]
    switch_margin = float(config["stability"].get("switch_margin", 0.03))

    for candidate in candidates:
        tag = candidate["tag"]
        speed = (
            speed_mix["tps"] * tps_scores[tag]
            + speed_mix["ttft"] * ttft_scores[tag]
            + speed_mix["e2e"] * e2e_scores[tag]
        )
        candidate["components"].update(
            {
                "cost": cost_scores[tag],
                "speed": clamp(speed),
                "tps": tps_scores[tag],
                "ttft": ttft_scores[tag],
                "e2e": e2e_scores[tag],
            }
        )
        utility = sum(
            weights[key] * candidate["components"][key]
            for key in ("quality", "reliability", "cost", "speed", "cache", "fidelity")
        )
        penalty = uncertainty_penalty * (1.0 - candidate["data_confidence"])
        score = clamp(utility - penalty)
        stability_bonus = 0.0
        if tag in previous_order and previous_order:
            position = previous_order.index(tag)
            stability_bonus = switch_margin * (len(previous_order) - position) / len(previous_order)
        candidate["score"] = score
        candidate["stability_bonus"] = stability_bonus
        candidate["rank_score"] = score + stability_bonus

    candidates.sort(key=lambda item: (item["rank_score"], item["score"]), reverse=True)
    for index, candidate in enumerate(candidates, start=1):
        candidate["diagnostic_rank"] = index
        main_components = {
            key: candidate["components"][key]
            for key in ("quality", "reliability", "cost", "speed", "cache", "fidelity")
        }
        strongest = sorted(main_components.items(), key=lambda item: item[1], reverse=True)[:2]
        weakest = sorted(main_components.items(), key=lambda item: item[1])[:1]
        candidate["summary"] = {
            "strengths": [f"{key}={value:.3f}" for key, value in strongest],
            "weaknesses": [f"{key}={value:.3f}" for key, value in weakest],
        }


def provider_family(tag: str) -> str:
    return tag.split("/", 1)[0].lower()


def diversified_order(
    candidates: Sequence[Mapping[str, Any]], max_count: int, config: Mapping[str, Any]
) -> list[str]:
    remaining = list(candidates)
    selected: list[Mapping[str, Any]] = []
    families: set[str] = set()
    enabled = bool(config["diversity"].get("enabled", True))
    max_gap = float(config["diversity"].get("max_score_gap", 0.12))

    while remaining and len(selected) < max_count:
        choice_index = 0
        if enabled and selected:
            top_score = float(remaining[0]["rank_score"])
            for index, candidate in enumerate(remaining):
                family = provider_family(str(candidate["tag"]))
                gap = top_score - float(candidate["rank_score"])
                if family not in families and gap <= max_gap:
                    choice_index = index
                    break
        chosen = remaining.pop(choice_index)
        selected.append(chosen)
        families.add(provider_family(str(chosen["tag"])))
    return [str(item["tag"]) for item in selected]


def load_previous_order(path: str | None) -> list[str]:
    if not path:
        return []
    payload = load_json_file(path)
    if not isinstance(payload, Mapping):
        raise RankingError("Previous ranking must be a JSON object.", EXIT_DATA)
    provider = nested_get(payload, ("routing.provider", "request.provider"))
    if isinstance(provider, Mapping) and isinstance(provider.get("order"), list):
        return [str(item) for item in provider["order"]]
    ranking = payload.get("ranking")
    if isinstance(ranking, list):
        return [str(item.get("tag")) for item in ranking if isinstance(item, Mapping) and item.get("tag")]
    return []


def determine_mode(config: Mapping[str, Any]) -> str:
    mode = str(config.get("routing_mode", "auto"))
    if mode != "auto":
        return mode
    uses_tools = bool(config["workload"].get("uses_tools"))
    deterministic = bool(config.get("deterministic_order"))
    return "native-exacto" if uses_tools and not deterministic else "manual"


def nonexpressible_exclusions_present(
    excluded: Sequence[Mapping[str, Any]], config: Mapping[str, Any]
) -> bool:
    """Return true when local filtering removed an endpoint for a rule OpenRouter cannot express directly.

    Expressible filters such as require_parameters, quantizations, max_price, only,
    and ignore are emitted in the request. Snapshot-only constraints need an
    explicit eligible provider.only pool if strict enforcement is requested.
    """

    allowed_tiers = {
        str(item).lower() for item in config["constraints"].get("allowed_service_tiers") or []
    }
    service_tier_needs_pin = bool(allowed_tiers) and allowed_tiers != {"default"}
    nonexpressible_prefixes = (
        "context_length ",
        "max_prompt_tokens ",
        "max_completion_tokens ",
        "caching is required",
        "moderated endpoint is disallowed",
        "uptime_last_",
        "throughput ",
        "latency ",
        "expected cost ",
    )
    for item in excluded:
        for reason_raw in item.get("reasons") or []:
            reason = str(reason_raw)
            if reason.startswith(nonexpressible_prefixes):
                return True
            if service_tier_needs_pin and reason.startswith("service tier "):
                return True
    return False


def build_provider_preferences(
    mode: str,
    model: str,
    candidates: Sequence[Mapping[str, Any]],
    routing_order: Sequence[str],
    excluded: Sequence[Mapping[str, Any]],
    config: Mapping[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    constraints = config["constraints"]
    workload = config["workload"]
    routing_cfg = config["routing"]
    warnings: list[str] = []
    provider: dict[str, Any] = {}

    explicit_only = [str(item) for item in constraints.get("only") or []]
    explicit_ignore = [str(item) for item in constraints.get("ignore") or []]
    if explicit_only:
        provider["only"] = explicit_only
    if explicit_ignore:
        provider["ignore"] = explicit_ignore
    if explicit_only and explicit_ignore:
        warnings.append("Both provider.only and provider.ignore are configured; verify their intersection is non-empty.")

    required_parameters = [str(item) for item in workload.get("required_parameters") or []]
    if required_parameters:
        provider["require_parameters"] = True
    data_collection = constraints.get("data_collection")
    if data_collection in {"allow", "deny"}:
        provider["data_collection"] = data_collection
    if constraints.get("zdr"):
        provider["zdr"] = True
    allowed_quantizations = [str(item) for item in constraints.get("allowed_quantizations") or []]
    if allowed_quantizations:
        provider["quantizations"] = allowed_quantizations

    max_price = dict(constraints.get("max_price") or {})
    prompt_cap = parse_number(constraints.get("max_prompt_price_per_million"))
    completion_cap = parse_number(constraints.get("max_completion_price_per_million"))
    request_cap = parse_number(constraints.get("max_request_price"))
    if prompt_cap is not None:
        max_price["prompt"] = prompt_cap
    if completion_cap is not None:
        max_price["completion"] = completion_cap
    if request_cap is not None:
        max_price["request"] = request_cap
    if max_price:
        provider["max_price"] = max_price

    if constraints.get("preferred_min_throughput") is not None:
        provider["preferred_min_throughput"] = constraints["preferred_min_throughput"]
    if constraints.get("preferred_max_latency") is not None:
        provider["preferred_max_latency"] = constraints["preferred_max_latency"]

    allow_fallbacks = bool(routing_cfg.get("allow_fallbacks", True))
    provider["allow_fallbacks"] = allow_fallbacks
    eligible_tags = [str(candidate["tag"]) for candidate in candidates]
    strict_hard = bool(routing_cfg.get("strict_hard_constraints", True))
    must_pin_eligible_pool = strict_hard and nonexpressible_exclusions_present(excluded, config)

    request_model = strip_virtual_suffix(model)
    if mode == "native-exacto":
        request_model = append_exacto(request_model)
        if must_pin_eligible_pool:
            provider["only"] = eligible_tags
            warnings.append(
                "provider.only was generated to enforce local hard constraints; rerun ranking frequently so the pool does not become stale."
            )
        warnings.append(
            "Exacto performs the authoritative quality-first ordering inside the eligible pool; the diagnostic score is not a reimplementation of OpenRouter's private telemetry."
        )
    else:
        provider["order"] = list(routing_order)
        if must_pin_eligible_pool:
            provider["only"] = eligible_tags
        warnings.append(
            "Manual provider.order disables OpenRouter load balancing and provider sticky routing; keep a stable first provider per session and monitor cache hit rate after rollout."
        )

    request: dict[str, Any] = {"model": request_model, "provider": provider}
    sessions = int(workload.get("expected_requests_per_session", 1))
    if (
        routing_cfg.get("include_session_id_placeholder", True)
        and workload.get("session_id_available")
        and sessions > 1
    ):
        request["session_id"] = "<stable-session-id>"
    return request, warnings


def make_result(
    model: str,
    endpoints: Sequence[Mapping[str, Any]],
    observations: Mapping[str, Mapping[str, Any]],
    config: Mapping[str, Any],
    at_utc: datetime,
) -> dict[str, Any]:
    candidates, excluded = evaluate_candidates(endpoints, observations, config, at_utc)
    if not candidates:
        reasons = "; ".join(
            f"{item.get('tag')}: {', '.join(item.get('reasons') or [])}" for item in excluded[:10]
        )
        raise RankingError(f"No eligible providers remain. {reasons}", EXIT_NO_ELIGIBLE)
    score_candidates(candidates, config)
    mode = determine_mode(config)
    routing_order = diversified_order(candidates, int(config["max_ranked_providers"]), config)
    request, routing_warnings = build_provider_preferences(
        mode, model, candidates, routing_order, excluded, config
    )

    coverage = {
        "endpoint_count": len(endpoints),
        "eligible_count": len(candidates),
        "excluded_count": len(excluded),
        "providers_with_observations": sum(
            1 for candidate in candidates if candidate["metrics"].get("observation_match")
        ),
        "providers_with_quality_signals": sum(
            1 for candidate in candidates if candidate["metrics"].get("quality_signals")
        ),
    }
    return {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "pricing_evaluated_at_utc": at_utc.isoformat(),
        "model": strip_virtual_suffix(model),
        "mode": mode,
        "profile": config["profile"],
        "workload": config["workload"],
        "weights": config["weights"],
        "routing_order": routing_order,
        "routing": request,
        "ranking": candidates,
        "excluded": excluded,
        "coverage": coverage,
        "warnings": routing_warnings,
    }


def render_markdown(result: Mapping[str, Any]) -> str:
    lines = [
        "# OpenRouter provider recommendation",
        "",
        f"- Model: `{result['model']}`",
        f"- Mode: `{result['mode']}`",
        f"- Profile: `{result['profile']}`",
        "",
        "## Diagnostic ranking",
        "",
        "| Rank | Provider tag | Score | Cost/request | TPS | TTFT | E2E | Uptime | Quality | Cache hit |",
        "|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for item in result["ranking"]:
        metrics = item["metrics"]
        uptime = metrics.get("endpoint_uptime")
        lines.append(
            "| {rank} | `{tag}` | {score:.3f} | ${cost:.6f} | {tps} | {ttft} | {e2e} | {uptime} | {quality:.3f} | {cache:.1%} |".format(
                rank=item["diagnostic_rank"],
                tag=item["tag"],
                score=item["score"],
                cost=metrics["expected_cost_usd"],
                tps="—" if metrics.get("throughput_tps") is None else f"{metrics['throughput_tps']:.1f}",
                ttft="—" if metrics.get("latency_seconds") is None else f"{metrics['latency_seconds']:.2f}s",
                e2e="—" if metrics.get("estimated_e2e_seconds") is None else f"{metrics['estimated_e2e_seconds']:.2f}s",
                uptime="—" if uptime is None else f"{uptime:.3%}",
                quality=item["components"]["quality"],
                cache=metrics.get("cache_token_hit_rate", 0.0),
            )
        )
    lines.extend(
        [
            "",
            "## Request fragment",
            "",
            "```json",
            json.dumps(result["routing"], ensure_ascii=False, indent=2),
            "```",
        ]
    )
    if result.get("warnings"):
        lines.extend(["", "## Warnings", ""])
        lines.extend(f"- {warning}" for warning in result["warnings"])
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Rank OpenRouter provider endpoints using workload-aware quality, reliability, "
            "effective cost, throughput, latency, cache, and quantization signals."
        ),
        epilog=(
            "Examples:\n"
            "  rank_providers.py --model deepseek/deepseek-v4-flash-0731 --config config.json\n"
            "  rank_providers.py --endpoints-file endpoints.json --observations telemetry.jsonl "
            "--format markdown --output report.md"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--model", help="OpenRouter model slug; fetch live Endpoints API data")
    source.add_argument("--endpoints-file", help="Saved OpenRouter Endpoints API JSON response")
    parser.add_argument("--config", help="Ranking configuration JSON")
    parser.add_argument("--observations", help="Aggregated JSON, JSON array, or JSONL request telemetry")
    parser.add_argument("--previous-ranking", help="Prior output JSON used for hysteresis")
    parser.add_argument("--api-key-env", default="OPENROUTER_API_KEY", help="API key environment variable")
    parser.add_argument("--timeout", type=float, default=20.0, help="HTTP timeout in seconds")
    parser.add_argument("--at-utc", help="ISO-8601 time used to evaluate pricing overrides")
    parser.add_argument("--mode", choices=("auto", "native-exacto", "manual"), help="Override routing mode")
    parser.add_argument("--profile", choices=tuple(PROFILES), help="Override scoring profile")
    parser.add_argument("--max-providers", type=int, help="Override maximum provider.order entries")
    parser.add_argument("--format", choices=("json", "markdown"), default="json", help="Output format")
    parser.add_argument("--output", help="Write output to a file instead of stdout")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        config = load_config(args.config)
        if args.mode:
            config["routing_mode"] = args.mode
        if args.profile:
            # Rebuild through load_config semantics without mutating a user file.
            config["profile"] = args.profile
            profile = PROFILES[args.profile]
            config["weights"] = normalize_weights(
                profile["weights"], ("quality", "reliability", "cost", "speed", "cache", "fidelity")
            )
            config["speed_mix"] = normalize_weights(
                profile["speed_mix"], ("tps", "ttft", "e2e")
            )
        if args.max_providers is not None:
            if args.max_providers < 1:
                raise RankingError("--max-providers must be at least 1.", EXIT_ARGUMENT)
            config["max_ranked_providers"] = args.max_providers

        previous = load_previous_order(args.previous_ranking)
        if previous:
            config["stability"]["previous_order"] = previous

        if args.model:
            payload = fetch_endpoint_payload(args.model, args.api_key_env, args.timeout)
            inferred_model, endpoints = extract_endpoints(payload)
            model = args.model or inferred_model
        else:
            payload = load_json_file(args.endpoints_file)
            inferred_model, endpoints = extract_endpoints(payload)
            model = inferred_model
        if not endpoints:
            raise RankingError("Endpoint list is empty.", EXIT_NO_ELIGIBLE)

        observations = load_observations(args.observations)
        at_utc = parse_iso_datetime(args.at_utc)
        result = make_result(model, endpoints, observations, config, at_utc)
        if args.format == "markdown":
            output = render_markdown(result)
        else:
            output = json.dumps(
                result,
                ensure_ascii=False,
                indent=None if args.compact else 2,
                separators=(",", ":") if args.compact else None,
            ) + "\n"
        if args.output:
            Path(args.output).write_text(output, encoding="utf-8")
            eprint(f"Wrote {args.output}")
        else:
            sys.stdout.write(output)
        return 0
    except RankingError as exc:
        eprint(f"Error: {exc}")
        return exc.exit_code
    except KeyboardInterrupt:
        eprint("Interrupted.")
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
