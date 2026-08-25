#!/usr/bin/env python3
"""Executable regression tests for the bundled reviewer skill."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run_script(script: str, *args: str, expected: tuple[int, ...] = (0,)) -> tuple[subprocess.CompletedProcess[str], dict]:
    with tempfile.TemporaryDirectory(prefix="apple-review-test-") as tmp:
        output = Path(tmp) / "result.json"
        command = [PYTHON, str(ROOT / "scripts" / script), *map(str, args), "--output", str(output)]
        completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=120, check=False)
        if completed.returncode not in expected:
            raise AssertionError(
                f"{command!r} returned {completed.returncode}; stdout={completed.stdout!r}; stderr={completed.stderr!r}"
            )
        if not output.is_file():
            raise AssertionError(f"{script} did not create {output}; stderr={completed.stderr!r}")
        return completed, json.loads(output.read_text(encoding="utf-8"))


class SkillSmokeTests(unittest.TestCase):
    def test_skill_package_contract(self) -> None:
        _, result = run_script("validate_skill.py", str(ROOT))
        self.assertTrue(result["valid"], result["errors"])
        self.assertEqual([], result["errors"])
        self.assertLessEqual(result["facts"]["skill_md_lines"], 500)

    def test_example_input_schema(self) -> None:
        config_path = ROOT / "assets" / "review-input.example.json"
        _, result = run_script("validate_input.py", "--config", str(config_path))
        check_map = {item["id"]: item for item in result["checks"]}
        self.assertEqual("PASS", check_map["input.schema"]["status"])
        # Credentials are deliberately environment-variable references, never fixture secrets.
        config = json.loads(config_path.read_text(encoding="utf-8"))
        demo = config["review"]["demo_account"]
        self.assertIn("username_env", demo)
        self.assertIn("password_env", demo)
        self.assertNotIn("username", demo)
        self.assertNotIn("password", demo)

    def test_valid_screenshot_and_visual_evidence(self) -> None:
        screenshot_root = ROOT / "tests" / "fixtures" / "screenshots"
        with tempfile.TemporaryDirectory(prefix="apple-review-screens-") as tmp:
            output = Path(tmp) / "screenshots.json"
            sheets = Path(tmp) / "contact-sheets"
            command = [
                PYTHON, str(ROOT / "scripts" / "inspect_screenshots.py"),
                "--screenshots", str(screenshot_root),
                "--config", str(ROOT / "tests" / "fixtures" / "review-input.screenshots.json"),
                "--contact-sheets", str(sheets),
                "--output", str(output),
                "--strict",
            ]
            completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=120, check=False)
            self.assertEqual(0, completed.returncode, completed.stderr)
            result = json.loads(output.read_text(encoding="utf-8"))
            open_major = [
                item for item in result["findings"]
                if item.get("severity") in {"BLOCKER", "HIGH"} and item.get("status") in {"OPEN", "NEEDS_REVIEW", "ERROR"}
            ]
            self.assertEqual([], open_major)
            checks = {item["id"]: item for item in result["checks"]}
            self.assertEqual("PASS", checks["screenshots.coverage.iphone"]["status"])
            self.assertEqual("NEEDS_REVIEW", checks["screenshots.visual_review"]["status"])
            self.assertTrue((sheets / "visual-review-queue.json").is_file())

        _, evidence = run_script(
            "validate_evidence.py",
            "--evidence", str(ROOT / "tests" / "fixtures" / "evidence" / "visual-good.json"),
            "--screenshots-root", str(screenshot_root),
            "--require-check", "screenshots.visual",
            "--strict",
        )
        self.assertTrue(evidence["valid"], evidence["findings"])

    def test_visual_pass_requires_matching_hashes_and_complete_scope(self) -> None:
        completed, evidence = run_script(
            "validate_evidence.py",
            "--evidence", str(ROOT / "tests" / "fixtures" / "evidence" / "visual-bad.json"),
            "--screenshots-root", str(ROOT / "tests" / "fixtures" / "screenshots"),
            "--require-check", "screenshots.visual",
            "--strict",
            expected=(2,),
        )
        self.assertEqual(2, completed.returncode)
        self.assertFalse(evidence["valid"])
        self.assertIn("EVIDENCE-VISUAL-PASS-UNSUPPORTED", {item["id"] for item in evidence["findings"]})

    def test_bad_source_fixture_triggers_direct_and_heuristic_controls(self) -> None:
        completed, result = run_script(
            "scan_project.py",
            "--project", str(ROOT / "tests" / "fixtures" / "project-bad"),
            "--config", str(ROOT / "tests" / "fixtures" / "review-input.bad-project.json"),
            "--strict",
            expected=(2,),
        )
        self.assertEqual(2, completed.returncode)
        ids = {item["id"] for item in result["findings"]}
        required = {
            "SOURCE-HARDCODED-SECRET",
            "SOURCE-PURPOSE-NSCAMERAUSAGEDESCRIPTION-GENERIC",
            "SOURCE-ATS-ARBITRARY-LOADS",
            "SOURCE-AI-CONSENT-NOT-FOUND",
            "SOURCE-ACCOUNT-DELETION-NOT-FOUND",
            "SOURCE-LOGIN-EQUIVALENT-NOT-FOUND",
            "SOURCE-PRIVATE-DEPRECATED-API",
            "SOURCE-DYNAMIC-CODE-REVIEW",
            "SOURCE-PRIVACY-REASON-INVALID-NSPrivacyAccessedAPICategoryUserDefaults",
        }
        self.assertTrue(required.issubset(ids), sorted(required - ids))

    def test_capacitor_85_fixture_triggers_release_and_uiscene_controls(self) -> None:
        completed, result = run_script(
            "scan_project.py",
            "--project", str(ROOT / "tests" / "fixtures" / "project-capacitor-bad"),
            "--strict",
            expected=(2,),
        )

        self.assertEqual(2, completed.returncode)
        ids = {item["id"] for item in result["findings"]}
        required = {
            "SOURCE-CAPACITOR-VERSION-MISMATCH",
            "SOURCE-CAPACITOR-DEVELOPMENT-SERVER",
            "SOURCE-CAPACITOR-UNSAFE-NAVIGATION",
            "SOURCE-CAPACITOR-RELEASE-DIAGNOSTICS",
            "SOURCE-CAPACITOR-UISCENE-MIGRATION-INCOMPLETE",
            "SOURCE-CAPACITOR-PLUGIN-PRIVACY-MANIFEST",
            "SOURCE-CAPACITOR-LIVE-UPDATES-REVIEW",
        }
        self.assertTrue(required.issubset(ids), sorted(required - ids))
        self.assertEqual("8.5", result["facts"]["capacitor"]["target_line"])
        self.assertIn("@capacitor/preferences", result["facts"]["capacitor"]["plugins"])

    def test_capacitor_85_release_fixture_passes_overlay_checks(self) -> None:
        completed, result = run_script(
            "scan_project.py",
            "--project", str(ROOT / "tests" / "fixtures" / "project-capacitor-good"),
            "--strict",
        )

        self.assertEqual(0, completed.returncode)
        capacitor_findings = [
            item for item in result["findings"]
            if item["id"].startswith("SOURCE-CAPACITOR-")
        ]
        self.assertEqual([], capacitor_findings)
        checks = {item["id"]: item for item in result["checks"]}
        self.assertEqual("PASS", checks["source.capacitor.release-config"]["status"])
        self.assertEqual("PASS", checks["source.capacitor.uiscene"]["status"])
        self.assertTrue(result["facts"]["capacitor"]["uiscene"]["proxy_forwarding"])

    def test_community_sources_remain_non_authoritative_signals(self) -> None:
        catalog = json.loads((ROOT / "references" / "source-catalog.json").read_text(encoding="utf-8"))
        community = {item["id"]: item for item in catalog["community_sources"]}
        expected = {
            "x-ai-wrapper-spam-2026",
            "x-release-completeness-2026",
            "x-guideline-21-evidence-request-2026",
            "x-generative-content-enforcement-2026",
            "x-app-store-preflight-tool-2026",
            "x-rork-reviewer-marketing-2026",
        }
        self.assertTrue(expected.issubset(community), sorted(expected - community.keys()))
        self.assertTrue(all(community[item_id]["reliability"] == "low" for item_id in expected))
        self.assertIn("commercial marketing", community["x-rork-reviewer-marketing-2026"]["use"])

        signals = (ROOT / "references" / "community-signals.md").read_text(encoding="utf-8")
        self.assertIn("cannot create a blocker", signals)
        self.assertIn("Do not fabricate a recording requirement", signals)
        self.assertIn("Do not ship or maintain a blacklist derived from a social post", signals)

    def test_capacitor_release_integrity_contract_is_fail_closed(self) -> None:
        reference = (ROOT / "references" / "capacitor-release-integrity.md").read_text(encoding="utf-8")
        required_terms = {
            ">=8.5.0 <9.0.0",
            "FRAMEWORK BASELINE UNVERIFIED",
            "architecture fact, not evidence of a thin wrapper",
            "Never run `cap sync` in the user's working tree",
            "capacitor.config-native-bundle-parity",
            "capacitor.web-assets-native-bundle-parity",
            "declared, lockfile-resolved, natively integrated, and finally embedded",
            "Source-only evidence cannot pass final parity",
        }
        self.assertEqual(set(), {term for term in required_terms if term not in reference})

        config = json.loads((ROOT / "assets" / "review-input.example.json").read_text(encoding="utf-8"))
        capacitor = config["frameworks"]["capacitor"]
        self.assertEqual("auto", capacitor["mode"])
        self.assertEqual(">=8.5.0 <9.0.0", capacitor["tested_version_range"])
        self.assertFalse(capacitor["trusted_cli"])
        self.assertFalse(capacitor["live_updates"]["enabled"])


    def test_orchestrator_is_fail_closed_and_report_validates(self) -> None:
        with tempfile.TemporaryDirectory(prefix="apple-review-orchestrator-") as tmp:
            output_dir = Path(tmp) / "review-output"
            command = [
                PYTHON, str(ROOT / "scripts" / "review_app.py"),
                "--config", str(ROOT / "assets" / "review-input.example.json"),
                "--output-dir", str(output_dir),
                "--always-zero",
            ]
            completed = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=120, check=False)
            self.assertEqual(0, completed.returncode, completed.stderr)
            report_path = output_dir / "report.json"
            self.assertTrue(report_path.is_file())
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertNotEqual("READY FOR SUBMISSION", report["gate"]["state"])
            checks = {item["id"]: item for item in report["checks"]}
            self.assertNotEqual("PASS", checks["screenshots.visual"]["status"])
            self.assertNotEqual("PASS", checks["runtime.reviewer-journey"]["status"])
            self.assertNotEqual("PASS", checks["ai.semantic-review"]["status"])

            validation_path = Path(tmp) / "report-validation.json"
            validate = subprocess.run([
                PYTHON, str(ROOT / "scripts" / "validate_report.py"), str(report_path),
                "--strict", "--output", str(validation_path),
            ], cwd=ROOT, text=True, capture_output=True, timeout=120, check=False)
            self.assertEqual(0, validate.returncode, validate.stderr)
            validation = json.loads(validation_path.read_text(encoding="utf-8"))
            self.assertTrue(validation["valid"], validation["errors"])

    def test_ai_contracts_are_separate_from_semantic_review(self) -> None:
        _, result = run_script(
            "run_ai_safety_suite.py",
            "--suite", str(ROOT / "assets" / "ai-safety-test-cases.json"),
            "--ids", "AI-BENIGN-001,AI-DOXXING-001,AI-CONSENT-001,AI-CONSENT-DISCLOSURE-001,AI-PROMPT-INJECTION-001",
            "--command", str(ROOT / "assets" / "ai-adapter.example.py"),
        )
        checks = {item["id"]: item for item in result["checks"]}
        self.assertEqual("PASS", result["status"])
        self.assertEqual("PASS", checks["ai.adapter-contracts"]["status"])
        self.assertEqual("NEEDS_REVIEW", checks["ai.semantic-review"]["status"])
        self.assertGreater(result["counts"]["needs_review"], 0)
        self.assertEqual(0, result["counts"]["fail"])
        self.assertEqual(0, result["counts"]["error"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
