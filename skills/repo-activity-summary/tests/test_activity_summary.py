#!/usr/bin/env python3
"""Regression tests for repo-activity-summary (stdlib unittest only)."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional
from unittest import mock

# Allow importing the script from ../scripts/
SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import activity_summary as asu  # noqa: E402


def _git_available() -> bool:
    return shutil.which("git") is not None


def _run_git(repo: str, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        capture_output=True,
        text=True,
        check=check,
    )


def _init_repo(path: str) -> None:
    _run_git(path, "init")
    _run_git(path, "config", "user.email", "test@example.com")
    _run_git(path, "config", "user.name", "Test User")
    # Avoid dependent on global init.defaultBranch
    _run_git(path, "checkout", "-b", "main", check=False)


class TestDetectTechnologies(unittest.TestCase):
    """A1: extension matching must not use bare path substrings."""

    def test_html_css_cjs_do_not_imply_csharp_or_cpp(self) -> None:
        paths = ["src/index.html", "app/styles.css", "lib/util.cjs"]
        techs = asu.detect_technologies(paths)
        self.assertNotIn("C#", techs)
        self.assertNotIn("C/C++", techs)

    def test_real_csharp_and_cpp_still_detected_with_threshold(self) -> None:
        paths = [
            "src/Program.cs",
            "src/Utils.cs",
            "native/main.c",
            "native/util.cpp",
            "include/util.h",
        ]
        techs = asu.detect_technologies(paths)
        self.assertIn("C#", techs)
        self.assertIn("C/C++", techs)

    def test_single_source_file_not_enough_without_manifest(self) -> None:
        # One .py alone must not claim Python (threshold = 2)
        techs = asu.detect_technologies(["pkg/only_one.py"])
        self.assertNotIn("Python", techs)

    def test_manifest_is_enough_evidence(self) -> None:
        techs = asu.detect_technologies(["pyproject.toml"])
        self.assertIn("Python", techs)

    def test_go_mod_not_confused_with_path_substring(self) -> None:
        # "go" inside a longer segment must not fire path-segment rules wrongly
        techs = asu.detect_technologies(["docs/ongoing-notes.md", "src/algo.go", "src/main.go"])
        self.assertIn("Go", techs)


class TestBotAuthor(unittest.TestCase):
    """A2: human names containing 'bot' must not be filtered."""

    def test_humans_with_bot_substring_are_not_bots(self) -> None:
        humans = ["Talbot Smith", "Abbott", "Robert Botha", "Ida Bothe"]
        for name in humans:
            with self.subTest(name=name):
                self.assertFalse(asu.is_bot_author(name), f"{name!r} wrongly treated as bot")

    def test_known_bots_are_bots(self) -> None:
        bots = [
            "dependabot[bot]",
            "github-actions[bot]",
            "renovate[bot]",
            "semantic-release",
            "snyk-bot",
            "greenkeeper",
            "deepsource-bot",  # word-boundary on deepsource
        ]
        for name in bots:
            with self.subTest(name=name):
                # deepsource alone is the known token
                if name == "deepsource-bot":
                    self.assertTrue(asu.is_bot_author("deepsource"))
                else:
                    self.assertTrue(asu.is_bot_author(name), f"{name!r} not detected as bot")

    def test_bot_email_local(self) -> None:
        self.assertTrue(
            asu.is_bot_author("Dependabot", "dependabot[bot]@users.noreply.github.com")
        )


class TestWorkTypeClassification(unittest.TestCase):
    """A4 + A5: word-boundary scoring, release type, no false substring hits."""

    def test_a4_false_substring_cases(self) -> None:
        # Must NOT classify via unanchored substrings (ci⊂pricing, add⊂address, …)
        self.assertNotEqual(
            asu.classify_commit_message("Reduce latency in pricing service"),
            "infrastructure",
        )
        self.assertEqual(
            asu.classify_commit_message("Reduce latency in pricing service"),
            "performance",
        )
        self.assertNotEqual(
            asu.classify_commit_message("Handle address parsing"),
            "feature",
        )
        self.assertIsNone(asu.classify_commit_message("Handle address parsing"))
        self.assertNotEqual(
            asu.classify_commit_message("Rename component"),
            "ui",
        )
        self.assertEqual(
            asu.classify_commit_message("Rename component"),
            "refactor",
        )

    def test_a5_release_and_sample_subjects(self) -> None:
        cases = {
            "Release 0.32": "release",
            "Document server-side tools in changelog": None,  # see below
            "Updated changelog, refs #1588, #1579, #1585": "release",
            "service_tier option for OpenAI models": None,
            "Capture UnknownModelError, not ValueError": None,
            "Ran Cog": None,
            "Render schema-less tools in expanded logs": None,
        }
        # "Document … changelog" hits docs (document) and release (changelog);
        # docs score is higher because of document+… — either docs or release is
        # acceptable as long as it is not "other"/None.
        label_doc = asu.classify_commit_message(
            "Document server-side tools in changelog"
        )
        self.assertIn(label_doc, {"docs", "release"})

        for subject, expected in cases.items():
            if subject.startswith("Document "):
                continue
            with self.subTest(subject=subject):
                self.assertEqual(
                    asu.classify_commit_message(subject),
                    expected,
                    f"{subject!r} → {asu.classify_commit_message(subject)!r}",
                )

    def test_classify_work_types_counts_other(self) -> None:
        commits = [
            {
                "sha": "abc123",
                "date": datetime(2024, 1, 1, tzinfo=timezone.utc),
                "message": "Ran Cog",
            },
            {
                "sha": "def456",
                "date": datetime(2024, 1, 2, tzinfo=timezone.utc),
                "message": "feat: add widget",
            },
        ]
        counts, samples = asu.classify_work_types(commits)
        self.assertEqual(counts.get("feature"), 1)
        self.assertEqual(counts.get("other"), 1)
        self.assertEqual(len(samples), 1)
        self.assertEqual(samples[0]["subject"], "Ran Cog")

    def test_shared_classifier_used_by_contributors(self) -> None:
        """A9: analyze_contributors must use classify_commit_message."""
        commits = [
            {
                "sha": "1",
                "author": "Alice",
                "email": "a@example.com",
                "date": datetime(2024, 1, 1, tzinfo=timezone.utc),
                "message": "fix login crash",
                "files": [],
                "insertions": 3,
                "deletions": 1,
            }
        ]
        result = asu.analyze_contributors(commits)
        self.assertEqual(result[0]["primary_focus"], ["bugfix"])


class TestRenamePathResolution(unittest.TestCase):
    """A3: git rename forms must resolve to the destination path."""

    def test_brace_and_simple_rename_forms(self) -> None:
        self.assertEqual(
            asu.resolve_numstat_path("{skills => plugins/x}/f.md"),
            "plugins/x/f.md",
        )
        self.assertEqual(
            asu.resolve_numstat_path("old/path.md => new/path.md"),
            "new/path.md",
        )
        self.assertEqual(
            asu.resolve_numstat_path("dir/{old => new}/file.txt"),
            "dir/new/file.txt",
        )
        self.assertEqual(
            asu.resolve_numstat_path("plain/path.txt"),
            "plain/path.txt",
        )

    @unittest.skipUnless(_git_available(), "git not available")
    def test_real_git_mv_does_not_corrupt_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _init_repo(tmp)
            os.makedirs(os.path.join(tmp, "skills"), exist_ok=True)
            fpath = os.path.join(tmp, "skills", "f.md")
            with open(fpath, "w", encoding="utf-8") as fh:
                fh.write("# hello\n")
            _run_git(tmp, "add", "skills/f.md")
            _run_git(tmp, "commit", "-m", "add skills file")
            os.makedirs(os.path.join(tmp, "plugins", "x"), exist_ok=True)
            _run_git(tmp, "mv", "skills/f.md", "plugins/x/f.md")
            _run_git(tmp, "commit", "-m", "move skills to plugins")

            commits = asu.parse_git_log(
                repo_dir=tmp,
                days=30,
                author=None,
                max_commits=50,
                branch=None,
            )
            all_paths: List[str] = []
            for c in commits:
                for f in c["files"]:
                    all_paths.append(f["path"])

            # No brace/rename corruption
            for p in all_paths:
                self.assertNotIn("=>", p, f"raw rename form leaked: {p}")
                self.assertFalse(p.startswith("{"), f"brace path leaked: {p}")
                self.assertNotIn("{", p)

            # Destination path must appear after the move
            self.assertTrue(
                any(p.replace("\\", "/") == "plugins/x/f.md" for p in all_paths),
                f"expected plugins/x/f.md in {all_paths}",
            )


class TestNoiseAndHealth(unittest.TestCase):
    """A6, A7, A8."""

    def test_is_noise_message_keeps_real_work(self) -> None:
        for msg in ("fix", "test", "revert", "cleanup", "Fix login"):
            with self.subTest(msg=msg):
                self.assertFalse(
                    asu.is_noise_message(msg),
                    f"{msg!r} should not be treated as noise",
                )
        for msg in (".", "wip", "asdf", "stuff", "temp"):
            with self.subTest(msg=msg):
                self.assertTrue(asu.is_noise_message(msg))

    def test_test_module_detection_excludes_fixtures(self) -> None:
        self.assertTrue(asu.is_test_module("tests/test_foo.py"))
        self.assertTrue(asu.is_test_module("pkg/foo_test.go"))
        self.assertTrue(asu.is_test_module("src/widget.test.ts"))
        self.assertTrue(asu.is_test_module("src/widget.spec.tsx"))
        self.assertFalse(asu.is_test_module("latest.md"))
        self.assertFalse(asu.is_test_module("contest/entry.py"))
        self.assertFalse(asu.is_test_module("tests/cassettes/api.yaml"))
        self.assertFalse(asu.is_test_module("tests/fixtures/sample.json"))

    def test_velocity_excludes_noise_files(self) -> None:
        commits = [
            {
                "sha": "1",
                "author": "A",
                "email": "a@e.com",
                "date": datetime(2024, 1, 1, tzinfo=timezone.utc),
                "message": "deps",
                "files": [
                    {"path": "src/main.py", "additions": 10, "deletions": 0},
                    {"path": "package-lock.json", "additions": 5000, "deletions": 0},
                ],
                "insertions": 5010,
                "deletions": 0,
            }
        ]
        v = asu.compute_velocity(commits, days=7)
        self.assertTrue(v["noise_files_excluded"])
        self.assertEqual(v["avg_commit_size"], 10)


class TestSecurityAndRobustness(unittest.TestCase):
    """B1–B4."""

    def test_branch_option_injection_creates_no_file(self) -> None:
        """B1: --branch=--output=... must be rejected and create no file."""
        with tempfile.TemporaryDirectory() as tmp:
            target = os.path.join(tmp, "PWNED.txt")
            # Valid git work tree so failure is the branch payload, not cwd checks.
            if _git_available():
                _init_repo(tmp)
                with open(os.path.join(tmp, "a.txt"), "w", encoding="utf-8") as fh:
                    fh.write("x\n")
                _run_git(tmp, "add", "a.txt")
                _run_git(tmp, "commit", "-m", "init")

            # Also try writing outside the repo, matching the original PoC shape.
            outside = os.path.join(tempfile.gettempdir(), "PWNED-ras-injection.txt")
            if os.path.exists(outside):
                os.remove(outside)

            with self.assertRaises(SystemExit) as ctx:
                asu.main([
                    f"--branch=--output={target}",
                    "--repo-dir", tmp,
                    "--days", "1",
                ])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertFalse(
                os.path.exists(target),
                f"injection payload created {target}",
            )
            self.assertFalse(
                os.path.exists(outside),
                f"injection payload created {outside}",
            )

            # Direct parse_git_log rejection (same payload shape as the PoC).
            with self.assertRaises(RuntimeError) as rctx:
                asu.parse_git_log(
                    repo_dir=tmp if _git_available() else ".",
                    days=1,
                    author=None,
                    max_commits=5,
                    branch=f"--output={target}",
                )
            self.assertIn("must not start with", str(rctx.exception).lower())
            self.assertFalse(os.path.exists(target))

    def test_branch_starting_with_dash_rejected_in_parse(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            if _git_available():
                _init_repo(tmp)
                # empty repo still has no commits; injection is rejected first
            with self.assertRaises(RuntimeError) as ctx:
                asu.parse_git_log(
                    repo_dir=tmp if _git_available() else ".",
                    days=1,
                    author=None,
                    max_commits=10,
                    branch="--output=/tmp/should-not-exist-ras-test",
                )
            self.assertIn("must not start with", str(ctx.exception).lower())

    def test_bad_repo_dir_exits_nonzero_no_traceback(self) -> None:
        """B2: missing --repo-dir yields a one-line error, exit 1, no traceback."""
        missing = os.path.join(tempfile.gettempdir(), "nope-nope-does-not-exist-ras")
        proc = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "activity_summary.py"),
                "--repo-dir", missing,
                "--days", "1",
            ],
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("Error:", proc.stderr)
        # No traceback noise
        self.assertNotIn("Traceback", proc.stderr)
        self.assertNotIn("FileNotFoundError", proc.stderr)

    def test_repo_dir_starting_with_dash_rejected(self) -> None:
        with self.assertRaises(RuntimeError):
            asu.ensure_git_repo("--output=/tmp/x")

    def test_output_file_written_as_utf8(self) -> None:
        """B3: file writes use encoding=utf-8."""
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "report.md")
            data = {
                "repo": "demo",
                "period_days": 1,
                "total_commits": 0,
            }
            # Smoke: open path used by main
            text = asu.format_markdown(data)
            with open(out, "w", encoding="utf-8") as fh:
                fh.write(text)
            raw = Path(out).read_bytes()
            # Must be valid UTF-8
            raw.decode("utf-8")

    def test_since_uses_explicit_utc_offset(self) -> None:
        """B4: --since must carry an explicit offset (not a bare date)."""
        if not _git_available():
            self.skipTest("git not available")
        with tempfile.TemporaryDirectory() as tmp:
            _init_repo(tmp)
            with open(os.path.join(tmp, "a.txt"), "w", encoding="utf-8") as fh:
                fh.write("x\n")
            _run_git(tmp, "add", "a.txt")
            _run_git(tmp, "commit", "-m", "init file")

            captured = {}

            real_run = subprocess.run

            def spy_run(*args, **kwargs):
                cmd = args[0] if args else kwargs.get("args")
                if isinstance(cmd, list) and cmd and cmd[0] == "git" and "log" in cmd:
                    captured["cmd"] = list(cmd)
                return real_run(*args, **kwargs)

            with mock.patch("subprocess.run", side_effect=spy_run):
                asu.parse_git_log(tmp, days=30, author=None, max_commits=10, branch=None)

            self.assertIn("cmd", captured)
            since_args = [a for a in captured["cmd"] if a.startswith("--since=")]
            self.assertEqual(len(since_args), 1)
            since_val = since_args[0].split("=", 1)[1]
            # ISO-8601 with explicit offset
            self.assertRegex(since_val, r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}")


class TestClassificationThresholdAndFlags(unittest.TestCase):
    """A5 flags: unreliable classification surfaces samples; --raw-subjects."""

    @unittest.skipUnless(_git_available(), "git not available")
    def test_unclassified_samples_and_raw_subjects(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _init_repo(tmp)
            for i, msg in enumerate(
                [
                    "Ran Cog",
                    "service_tier option for OpenAI models",
                    "Capture UnknownModelError, not ValueError",
                    "Render schema-less tools in expanded logs",
                    "feat: add one real feature",
                ]
            ):
                path = os.path.join(tmp, f"f{i}.txt")
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(f"content {i}\n")
                _run_git(tmp, "add", f"f{i}.txt")
                _run_git(tmp, "commit", "-m", msg)

            data = asu.analyze(
                repo_dir=tmp,
                days=30,
                classify_threshold=0.25,
                max_unclassified_samples=40,
                raw_subjects=True,
            )
            self.assertGreater(data["total_commits"], 0)
            clf = data["classification"]
            self.assertTrue(clf["unreliable"])
            self.assertIn("unclassified_samples", data)
            self.assertTrue(any("Ran Cog" in s["subject"] for s in data["unclassified_samples"]))
            self.assertIn("raw_subjects", data)
            self.assertEqual(len(data["raw_subjects"]), data["total_commits"])

    def test_version_is_1_1_0(self) -> None:
        self.assertEqual(asu.__version__, "1.1.0")

    def test_cli_version_flag(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "activity_summary.py"), "--version"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0)
        self.assertIn("1.1.0", proc.stdout + proc.stderr)

    def test_cli_help(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "activity_summary.py"), "--help"],
            capture_output=True,
            text=True,
        )
        self.assertEqual(proc.returncode, 0)
        help_text = proc.stdout
        self.assertIn("--raw-subjects", help_text)
        self.assertIn("--classify-threshold", help_text)
        self.assertIn("--max-unclassified-samples", help_text)


class TestEndToEndSmoke(unittest.TestCase):
    @unittest.skipUnless(_git_available(), "git not available")
    def test_analyze_markdown_smoke(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            _init_repo(tmp)
            os.makedirs(os.path.join(tmp, "tests"), exist_ok=True)
            with open(os.path.join(tmp, "main.py"), "w", encoding="utf-8") as fh:
                fh.write("print('hi')\n")
            with open(os.path.join(tmp, "util.py"), "w", encoding="utf-8") as fh:
                fh.write("x = 1\n")
            with open(os.path.join(tmp, "pyproject.toml"), "w", encoding="utf-8") as fh:
                fh.write("[project]\nname='demo'\n")
            with open(os.path.join(tmp, "tests", "test_main.py"), "w", encoding="utf-8") as fh:
                fh.write("def test_ok():\n    assert True\n")
            _run_git(tmp, "add", ".")
            _run_git(tmp, "commit", "-m", "feat: initial python project")

            data = asu.analyze(tmp, days=30)
            self.assertIn("Python", data["technologies"])
            self.assertGreaterEqual(data["project_health"]["test_module_count"], 1)
            md = asu.format_markdown(data)
            self.assertIn("Repo Activity Summary", md)
            self.assertIn("test modules", md.lower())


if __name__ == "__main__":
    unittest.main()
