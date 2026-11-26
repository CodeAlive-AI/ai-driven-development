"""Tests for cross-agent resolution, --path/--agent CLI flags, and agy judge support."""

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

import agents  # noqa: E402
import list_agent_skills  # noqa: E402
import review_skill  # noqa: E402
import show_skill  # noqa: E402
import trigger_test  # noqa: E402


def write_skill(root: Path, folder: str, name: str | None = None, desc: str = "Use when testing skills.") -> Path:
    skill_dir = root / folder
    skill_dir.mkdir(parents=True, exist_ok=True)
    fm_lines = ["---"]
    if name is not None:
        fm_lines.append(f"name: {name}")
    if desc:
        fm_lines.append(f"description: {desc}")
    fm_lines.append("---")
    (skill_dir / "SKILL.md").write_text("\n".join(fm_lines) + "\n\n# Body\n\nFollow steps.\n", encoding="utf-8")
    return skill_dir


class CrossAgentResolutionTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.base = Path(self._tmp.name)

    def test_resolve_skill_by_path_dir_and_skill_md(self):
        skill_dir = write_skill(self.base, "demo", "demo")
        resolved, scope, err = agents.resolve_skill(path=skill_dir)
        self.assertEqual((resolved, scope, err), (skill_dir, "path", None))

        resolved_md, scope_md, err_md = agents.resolve_skill(path=skill_dir / "SKILL.md")
        self.assertEqual((resolved_md, scope_md, err_md), (skill_dir, "path", None))

    def test_resolve_skill_for_antigravity_user_alias_and_project(self):
        fake_home = self.base / "home"
        ws = self.base / "ws"
        agy_global = fake_home / ".gemini" / "config" / "skills"
        shared_global = fake_home / ".agents" / "skills"
        ws_legacy = ws / ".agent" / "skills"

        s_primary = write_skill(agy_global, "g-skill", "g-skill")
        s_shared = write_skill(shared_global, "u-skill", "u-skill")
        s_proj = write_skill(ws_legacy, "p-skill", "p-skill")

        with patch.object(agents, "expand_path", side_effect=lambda p, c=None: Path(p.replace("~", str(fake_home)))):
            self.assertEqual(
                agents.resolve_skill("g-skill", agent="antigravity", scope="user", cwd=ws),
                (s_primary, "global", None),
            )
            self.assertEqual(
                agents.resolve_skill("u-skill", agent="antigravity", scope="global", cwd=ws),
                (s_shared, "global", None),
            )
            self.assertEqual(
                agents.resolve_skill("p-skill", agent="antigravity", scope="project", cwd=ws),
                (s_proj, "project", None),
            )

    def test_review_skill_by_path_and_missing_name_error(self):
        good = write_skill(self.base, "good-skill", "good-skill")
        res_good = review_skill.review_skill(path=good)
        self.assertTrue(res_good["found"])
        self.assertEqual(res_good["summary"]["errors"], 0)

        no_name = write_skill(self.base, "no-name", name=None)
        res_bad = review_skill.review_skill(path=no_name)
        rules = {issue["rule"] for issue in res_bad["issues"]}
        self.assertIn("name-required", rules)
        self.assertNotIn("name-dir-mismatch", rules)

    def test_show_skill_by_path_and_symlink_metadata(self):
        real = write_skill(self.base / "src", "linked-skill", "linked-skill")
        link = self.base / "dst" / "linked-skill"
        link.parent.mkdir(parents=True)
        link.symlink_to(real, target_is_directory=True)

        buf = io.StringIO()
        with redirect_stdout(buf):
            ok = show_skill.show_skill(path=link, output_format="json")
        self.assertTrue(ok)
        data = json.loads(buf.getvalue())
        self.assertTrue(data["is_symlink"])
        self.assertEqual(Path(data["symlink_target"]), real)

    def test_trigger_test_agy_and_custom_cli_judges(self):
        cases = [{"prompt": "please trigger demo", "expect": "trigger"}]
        with patch("trigger_test.subprocess.run") as run:
            run.return_value.returncode = 0
            run.return_value.stdout = '{"trigger": true, "reason": "matched"}'
            run.return_value.stderr = ""
            report = trigger_test.run_cases("Use when testing demo.", cases, "agy-cli")
            self.assertEqual(report["metrics"]["f1"], 1.0)
            self.assertEqual(run.call_args.args[0][:3], ["agy", "-p", "--disable-slash-commands"])

            report_custom = trigger_test.run_cases(
                "Use when testing demo.", cases, "custom-cli", judge_cmd="my-cli --flag"
            )
            self.assertEqual(report_custom["metrics"]["f1"], 1.0)
            self.assertEqual(run.call_args.args[0], ["my-cli", "--flag"])
            self.assertIn("Skill description:", run.call_args.kwargs["input"])

    def test_list_agent_skills_antigravity_skips_symlinked_legacy_root(self):
        fake_home = self.base / "home"
        primary = fake_home / ".gemini" / "config" / "skills"
        shared = fake_home / ".agents" / "skills"
        legacy = fake_home / ".gemini" / "antigravity" / "skills"
        write_skill(primary, "one", "one")
        write_skill(shared, "two", "two")
        legacy.parent.mkdir(parents=True, exist_ok=True)
        legacy.symlink_to(primary, target_is_directory=True)

        with patch.object(agents, "expand_path", side_effect=lambda p, c=None: Path(p.replace("~", str(fake_home)))):
            items = list_agent_skills.list_skills_for_agent("antigravity", scope="global")
        names = [item["name"] for item in items]
        self.assertEqual(names, ["one", "two"])

    def test_progressive_disclosure_checks_and_nested_url_filtering(self):
        skill = self.base / "pd-skill"
        (skill / "references" / "legacy").mkdir(parents=True)
        (skill / "references" / "used.md").write_text(
            "# Used\n\nSee [external](https://example.com/docs.md) for live docs.\n",
            encoding="utf-8",
        )
        (skill / "references" / "orphan.md").write_text("# Orphan\n", encoding="utf-8")
        (skill / "references" / "legacy" / "README.md").write_text("# Index\n", encoding="utf-8")
        (skill / "SKILL.md").write_text(
            "---\n"
            "name: pd-skill\n"
            "description: Reviews skills. Use when auditing progressive disclosure. Do not use for other tasks.\n"
            "---\n\n"
            "# PD Skill\n\n"
            "Read all files in references before starting.\n\n"
            "```markdown\n"
            "Read all references inside code block.\n"
            "```\n\n"
            "- [used](references/used.md#section)\n"
            "- [used again](references/used.md)\n"
            "- [missing](references/missing.md)\n"
            "- [web](https://example.com/page)\n"
            "- [app](customization://dir)\n",
            encoding="utf-8",
        )

        res = review_skill.review_skill(path=skill)
        rules = [issue["rule"] for issue in res["issues"]]
        self.assertIn("broken-reference-link", rules)
        self.assertIn("unreferenced-reference", rules)
        self.assertIn("eager-reference-load", rules)
        self.assertNotIn("nested-references", rules)
        # Ensure legacy/README.md was not flagged as unreferenced-reference
        orphan_msgs = [i["message"] for i in res["issues"] if i["rule"] == "unreferenced-reference"]
        self.assertEqual(len(orphan_msgs), 1)
        self.assertIn("references/orphan.md", orphan_msgs[0])

        # Verify fenced-only eager wording does not trigger eager-reference-load
        (skill / "references" / "orphan.md").unlink()
        (skill / "SKILL.md").write_text(
            "---\n"
            "name: pd-skill\n"
            "description: Reviews skills. Use when auditing progressive disclosure. Do not use for other tasks.\n"
            "---\n\n"
            "# PD Skill\n\n"
            "```markdown\n"
            "Read all files in references before starting.\n"
            "```\n\n"
            "- [used](references/used.md)\n",
            encoding="utf-8",
        )
        clean = review_skill.review_skill(path=skill)
        clean_rules = [issue["rule"] for issue in clean["issues"]]
        self.assertNotIn("eager-reference-load", clean_rules)
        self.assertNotIn("broken-reference-link", clean_rules)
        self.assertNotIn("unreferenced-reference", clean_rules)


if __name__ == "__main__":
    unittest.main()
