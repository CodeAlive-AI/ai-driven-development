from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "rank_providers.py"
SPEC = importlib.util.spec_from_file_location("rank_providers", SCRIPT)
assert SPEC and SPEC.loader
ranker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ranker)


class RankProvidersTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.payload = json.loads((ROOT / "tests" / "fixture-endpoints.json").read_text())
        cls.model, cls.endpoints = ranker.extract_endpoints(cls.payload)
        cls.observations = ranker.load_observations(ROOT / "tests" / "fixture-observations.json")
        cls.now = datetime(2026, 8, 25, 12, 0, tzinfo=timezone.utc)

    def make_config(self, *, deterministic: bool = False, profile: str = "agentic-balanced"):
        override = {
            "profile": profile,
            "routing_mode": "auto",
            "deterministic_order": deterministic,
            "workload": {
                "uses_tools": True,
                "expected_prompt_tokens": 10000,
                "expected_completion_tokens": 1000,
                "required_context_tokens": 12000,
                "required_completion_tokens": 2000,
                "required_parameters": ["tools", "tool_choice", "response_format"],
                "expected_requests_per_session": 5,
                "cacheable_prompt_fraction": 0.8,
            },
            "constraints": {
                "allowed_service_tiers": ["default"],
                "allowed_quantizations": ["bf16", "fp8"],
                "max_prompt_price_per_million": 1.0,
                "max_completion_price_per_million": 2.0,
            },
        }
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(override, handle)
            path = handle.name
        try:
            return ranker.load_config(path)
        finally:
            Path(path).unlink(missing_ok=True)

    def test_auto_tool_workload_uses_native_exacto_without_order(self) -> None:
        config = self.make_config(deterministic=False)
        result = ranker.make_result(self.model, self.endpoints, self.observations, config, self.now)
        self.assertEqual(result["mode"], "native-exacto")
        self.assertEqual(result["routing"]["model"], "acme/test-model:exacto")
        provider = result["routing"]["provider"]
        self.assertNotIn("order", provider)
        self.assertNotIn("sort", provider)
        self.assertTrue(provider["require_parameters"])
        self.assertEqual(provider["max_price"]["prompt"], 1.0)
        self.assertEqual(provider["max_price"]["completion"], 2.0)

    def test_hard_filters_remove_missing_tools_and_priority_tier(self) -> None:
        config = self.make_config()
        result = ranker.make_result(self.model, self.endpoints, self.observations, config, self.now)
        excluded = {item["tag"]: " | ".join(item["reasons"]) for item in result["excluded"]}
        self.assertIn("provider-d", excluded)
        self.assertIn("missing required parameters", excluded["provider-d"])
        self.assertIn("provider-a/fast", excluded)
        self.assertIn("service tier", excluded["provider-a/fast"])
        eligible = {item["tag"] for item in result["ranking"]}
        self.assertEqual(eligible, {"provider-a", "provider-b", "provider-c"})

    def test_manual_quality_profile_prefers_provider_a(self) -> None:
        config = self.make_config(deterministic=True, profile="agentic-quality")
        result = ranker.make_result(self.model, self.endpoints, self.observations, config, self.now)
        self.assertEqual(result["mode"], "manual")
        self.assertEqual(result["routing_order"][0], "provider-a")
        self.assertEqual(result["routing"]["provider"]["order"][0], "provider-a")
        self.assertFalse(any(tag.endswith("/fast") for tag in result["routing_order"]))

    def test_cache_cost_uses_token_level_read_and_write_rates(self) -> None:
        config = self.make_config()
        endpoint = next(item for item in self.endpoints if item["tag"] == "provider-a")
        pricing, warnings = ranker.resolve_pricing(endpoint["pricing"], 10000, self.now)
        self.assertEqual(warnings, [])
        observation = self.observations["provider-a"]
        expected, breakdown, _, _ = ranker.cache_and_cost(pricing, endpoint, observation, config)
        self.assertIsNotNone(expected)
        self.assertAlmostEqual(breakdown["cache_token_hit_rate"], 0.5, places=6)
        self.assertAlmostEqual(breakdown["cache_write_token_rate"], 0.1, places=6)
        self.assertAlmostEqual(expected, 0.0020, places=9)
        no_cache_config = self.make_config()
        no_cache, _, _, _ = ranker.cache_and_cost(pricing, endpoint, {}, no_cache_config)
        self.assertAlmostEqual(no_cache, 0.0027, places=9)
        self.assertLess(expected, no_cache)

    def test_pricing_override_is_strict_and_later_match_wins(self) -> None:
        pricing = {
            "prompt": "0.000001",
            "completion": "0.000002",
            "overrides": [
                {"min_prompt_tokens": 10000, "prompt": "0.000003"},
                {"min_prompt_tokens": 10000, "prompt": "0.000004"},
            ],
        }
        exact_threshold, _ = ranker.resolve_pricing(pricing, 10000, self.now)
        above_threshold, _ = ranker.resolve_pricing(pricing, 10001, self.now)
        self.assertEqual(exact_threshold["prompt"], 0.000001)
        self.assertEqual(above_threshold["prompt"], 0.000004)

    def test_jsonl_aggregation_derives_tps_and_cache_rates(self) -> None:
        lines = [
            {
                "provider_tag": "provider-z",
                "success": True,
                "tool_success": True,
                "usage": {
                    "prompt_tokens": 1000,
                    "completion_tokens": 100,
                    "prompt_tokens_details": {"cached_tokens": 500, "cache_write_tokens": 100},
                },
                "generation_time_seconds": 2,
                "ttft_ms": 250,
            },
            {
                "provider_tag": "provider-z",
                "success": False,
                "tool_success": False,
                "usage": {
                    "prompt_tokens": 1000,
                    "completion_tokens": 200,
                    "prompt_tokens_details": {"cached_tokens": 0, "cache_write_tokens": 0},
                },
                "generation_time_seconds": 4,
                "ttft_ms": 750,
            },
        ]
        aggregated = ranker.aggregate_raw_observations(lines)["provider-z"]
        self.assertEqual(aggregated["requests"], 2)
        self.assertEqual(aggregated["request_successes"], 1)
        self.assertAlmostEqual(aggregated["cache_token_hit_rate"], 0.25)
        self.assertAlmostEqual(aggregated["cache_write_token_rate"], 0.05)
        self.assertAlmostEqual(aggregated["observed_tps"], 50.0)
        self.assertAlmostEqual(aggregated["observed_ttft_seconds"], 0.5)

    def test_openrouter_generation_wrapper_and_response_usage_aliases(self) -> None:
        payload = {
            "data": {
                "provider_name": "Provider A",
                "native_tokens_prompt": 1000,
                "native_tokens_cached": 600,
                "native_tokens_completion": 120,
                "generation_time": 2000,
                "latency": 750,
                "total_cost": 0.0012,
            }
        }
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump(payload, handle)
            path = handle.name
        try:
            observations = ranker.load_observations(path)
        finally:
            Path(path).unlink(missing_ok=True)
        item = observations["Provider A"]
        self.assertEqual(item["requests"], 1)
        self.assertAlmostEqual(item["cache_token_hit_rate"], 0.6)
        self.assertAlmostEqual(item["observed_tps"], 60.0)
        self.assertAlmostEqual(item["observed_ttft_seconds"], 0.75)

        responses_record = {
            "provider_tag": "provider-responses",
            "success": True,
            "usage": {
                "input_tokens": 2000,
                "output_tokens": 100,
                "input_tokens_details": {
                    "cached_tokens": 1000,
                    "cache_write_tokens": 200,
                },
            },
            "generation_time_seconds": 2,
        }
        responses_item = ranker.aggregate_raw_observations([responses_record])["provider-responses"]
        self.assertAlmostEqual(responses_item["cache_token_hit_rate"], 0.5)
        self.assertAlmostEqual(responses_item["cache_write_token_rate"], 0.1)
        self.assertAlmostEqual(responses_item["observed_tps"], 50.0)

    def test_quantization_groups_and_strict_cache_pool(self) -> None:
        self.assertTrue(ranker.quantization_matches("mxfp8", ["fp8"]))
        self.assertTrue(ranker.quantization_matches("nvfp4", ["fp4"]))
        self.assertFalse(ranker.quantization_matches("int4", ["fp8"]))

        config = self.make_config()
        config["constraints"]["require_caching"] = True
        result = ranker.make_result(self.model, self.endpoints, self.observations, config, self.now)
        excluded = {item["tag"] for item in result["excluded"]}
        self.assertIn("provider-b", excluded)
        self.assertEqual(result["routing"]["provider"]["only"], ["provider-a", "provider-c"])


if __name__ == "__main__":
    unittest.main()
