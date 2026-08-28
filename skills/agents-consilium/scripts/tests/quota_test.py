#!/usr/bin/env python3

import importlib.util
import pathlib
import unittest
from unittest import mock


MODULE_PATH = pathlib.Path(__file__).parents[1] / "lib" / "quota.py"
SPEC = importlib.util.spec_from_file_location("consilium_quota", MODULE_PATH)
quota = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(quota)


class QuotaTest(unittest.TestCase):
    def test_normalize_codex_preserves_multiple_limit_buckets(self):
        result = quota.normalize_codex({
            "rateLimits": {"planType": "pro"},
            "rateLimitsByLimitId": {
                "codex": {
                    "limitName": None,
                    "primary": {"usedPercent": 24, "windowDurationMins": 10080, "resetsAt": 1788456265},
                    "secondary": None,
                },
                "spark": {
                    "limitName": "Spark",
                    "primary": {"usedPercent": 10, "windowDurationMins": 300, "resetsAt": 1787957812},
                    "secondary": {"usedPercent": 100, "windowDurationMins": 10080, "resetsAt": 1788161839},
                },
            },
            "rateLimitResetCredits": {"availableCount": 1},
        })
        self.assertEqual(result["limits"]["codex"]["primary"]["remainingPercent"], 76)
        self.assertEqual(result["limits"]["spark"]["secondary"]["remainingPercent"], 0)
        self.assertEqual(result["resetCreditsAvailable"], 1)

    def test_parse_grok_screen(self):
        result = quota.parse_grok_screen("Weekly limit: 52%\nNext reset: August 31, 18:59\n")
        self.assertEqual(result["usedPercent"], 52)
        self.assertEqual(result["remainingPercent"], 48)
        self.assertEqual(result["nextResetDisplay"], "August 31, 18:59")

    def test_parse_grok_screen_fails_closed(self):
        with self.assertRaisesRegex(RuntimeError, "lacks Weekly limit"):
            quota.parse_grok_screen("blank overlay")

    def test_remote_script_shell_quotes_cwd(self):
        script = quota._grok_remote_script("/mnt/work spaces/example")
        self.assertIn("cd '/mnt/work spaces/example' && grok --no-alt-screen", script)

    def test_grok_retries_one_transient_transport_failure(self):
        success = {"ok": True, "remainingPercent": 48}
        with mock.patch.object(
            quota,
            "_read_grok_once",
            side_effect=[RuntimeError("remote exit 1"), success],
        ) as reader, mock.patch.object(quota.time, "sleep"):
            self.assertEqual(quota.read_grok(), success)
            self.assertEqual(reader.call_count, 2)


if __name__ == "__main__":
    unittest.main()
