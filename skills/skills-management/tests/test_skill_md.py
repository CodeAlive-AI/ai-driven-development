"""Characterization tests for the shared SKILL.md parser (scripts/skill_md.py).

Before skill_md.py, nine scripts carried their own copy of the frontmatter regex and
read fields differently. Each case below names what the old copies returned, so the
behaviour change stays visible:

- "line copies": install_skill, list_skills, list_agent_skills, eval_viewer and
  audit_skill_duplicates read ``name:``/``description:`` line by line and stripped any
  quote characters from both ends;
- "continuation copies": show_skill, transfer_test and trigger_test also appended
  indented lines, joined with newlines;
- review_skill split every line containing ``:``, nested ones included.

The expected values match PyYAML on the frontmatter of real SKILL.md files.
"""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from skill_md import (  # noqa: E402
    extract_body,
    parse_frontmatter,
    parse_skill_md,
    read_skill_md,
    skill_name,
    skill_summary,
    split_frontmatter,
)


def fm(*lines: str) -> str:
    return "---\n" + "\n".join(lines) + "\n---\nBody\n"


class ScalarValueTests(unittest.TestCase):
    def test_plain_values(self):
        meta = parse_frontmatter(fm("name: demo", "description: Does things."))
        self.assertEqual(meta, {"name": "demo", "description": "Does things."})

    def test_double_quoted_value_unescapes(self):
        # Old: every copy kept the backslashes: 'Say \\"hi\\": now'.
        meta = parse_frontmatter(fm('name: "demo"', 'description: "Say \\"hi\\": now"'))
        self.assertEqual(meta["name"], "demo")
        self.assertEqual(meta["description"], 'Say "hi": now')

    def test_single_quoted_value_unescapes_doubled_quote(self):
        # Old: "It''s fine".
        meta = parse_frontmatter(fm("name: 'demo'", "description: 'It''s fine'"))
        self.assertEqual(meta["description"], "It's fine")

    def test_unbalanced_quote_is_kept(self):
        # Old: every copy stripped the stray quote and returned "demo".
        self.assertEqual(parse_frontmatter(fm("name: demo'"))["name"], "demo'")
        self.assertEqual(
            parse_frontmatter(fm('description: ends with "quote"'))["description"],
            'ends with "quote"',
        )

    def test_quoted_value_on_the_next_line(self):
        text = fm("name: demo", "description:", '  "Solve problems', '  carefully."')
        self.assertEqual(parse_frontmatter(text)["description"], "Solve problems carefully.")

    def test_quoted_value_spanning_lines(self):
        text = fm('description: "First line', '  second line."')
        self.assertEqual(parse_frontmatter(text)["description"], "First line second line.")

    def test_trailing_comment_is_removed_from_plain_values_only(self):
        # Old: "demo # the name".
        meta = parse_frontmatter(fm("name: demo # the name", 'description: "C # stays"'))
        self.assertEqual(meta["name"], "demo")
        self.assertEqual(meta["description"], "C # stays")

    def test_hash_without_space_is_not_a_comment(self):
        self.assertEqual(parse_frontmatter(fm("description: Use for C# code"))["description"],
                         "Use for C# code")

    def test_colon_inside_value(self):
        self.assertEqual(parse_frontmatter(fm("description: Use when: X happens"))["description"],
                         "Use when: X happens")

    def test_key_without_space_after_colon_is_still_read(self):
        # Every old copy accepted "name:demo"; kept so no installed skill changes name.
        self.assertEqual(parse_frontmatter(fm("name:demo"))["name"], "demo")


class MultiLineValueTests(unittest.TestCase):
    def test_folded_description(self):
        # Old: line copies and review returned ">", which review_skill and
        # transfer_test then reported as forbidden angle brackets; continuation
        # copies returned ">\nLine one\nline two.".
        text = fm("name: demo", "description: >", "  Line one", "  line two.")
        self.assertEqual(parse_frontmatter(text)["description"], "Line one line two.")

    def test_folded_description_keeps_paragraph_breaks(self):
        text = fm("description: >-", "  One", "  two.", "", "  Three.")
        self.assertEqual(parse_frontmatter(text)["description"], "One two.\nThree.")

    def test_literal_description(self):
        # Old: "|" or "|\nLine one\nline two.".
        text = fm("description: |", "  Line one", "  line two.")
        self.assertEqual(parse_frontmatter(text)["description"], "Line one\nline two.")

    def test_plain_value_continues_on_indented_lines(self):
        # Old: line copies returned "Line one"; continuation copies joined with "\n".
        text = fm("description: Line one", "  line two.")
        self.assertEqual(parse_frontmatter(text)["description"], "Line one line two.")

    def test_nested_block_does_not_leak_keys(self):
        # Old: review_skill read the nested name and returned "inner".
        text = fm("name: demo", "metadata:", "  version: 2.0", "  name: inner")
        meta = parse_frontmatter(text)
        self.assertEqual(meta["name"], "demo")
        self.assertEqual(meta["metadata"], "version: 2.0\nname: inner")
        self.assertNotIn("version", meta)

    def test_indented_key_is_not_top_level(self):
        # Old: eval_viewer and review_skill read the indented name.
        meta = parse_frontmatter(fm("  name: indented", "description: x"))
        self.assertNotIn("name", meta)

    def test_values_have_no_trailing_line_break(self):
        meta = parse_frontmatter(fm('description: "Ends with newline.\\n"'))
        self.assertEqual(meta["description"], "Ends with newline.")

    def test_repeated_key_last_wins(self):
        # Old: install_skill and eval_viewer took the first, the others the last.
        self.assertEqual(parse_frontmatter(fm("name: first", "name: second"))["name"], "second")


class DelimiterAndBodyTests(unittest.TestCase):
    def test_no_frontmatter(self):
        self.assertEqual(split_frontmatter("# Title\nBody\n"), (None, "# Title\nBody\n"))
        self.assertEqual(parse_frontmatter("# Title\n"), {})

    def test_body_after_frontmatter_without_leading_blank_lines(self):
        self.assertEqual(extract_body("---\nname: demo\n---\n\n# Title\n"), "# Title\n")

    def test_closing_delimiter_at_end_of_file(self):
        # Old: review_skill found no frontmatter; diff/log returned the whole file as body.
        self.assertEqual(parse_skill_md("---\nname: demo\n---"), ({"name": "demo"}, ""))

    def test_closing_delimiter_must_be_exactly_three_dashes(self):
        # Old: "----" closed the frontmatter, so description was lost.
        text = "---\nname: demo\n----\ndescription: x\n---\nBody\n"
        self.assertEqual(parse_skill_md(text), ({"name": "demo", "description": "x"}, "Body\n"))

    def test_empty_frontmatter(self):
        self.assertEqual(parse_skill_md("---\n---\nBody\n"), ({}, "Body\n"))

    def test_crlf(self):
        meta, body = parse_skill_md("---\r\nname: demo\r\ndescription: x\r\n---\r\nBody\r\n")
        self.assertEqual(meta, {"name": "demo", "description": "x"})
        self.assertEqual(body, "Body\r\n")


class SkillDirectoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def make_skill(self, directory: str, text: str) -> Path:
        skill = self.base / directory
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text(text, encoding="utf-8")
        return skill

    def test_missing_skill_md(self):
        (self.base / "empty").mkdir()
        self.assertIsNone(read_skill_md(self.base / "empty"))

    def test_name_falls_back_to_directory(self):
        skill = self.make_skill("dir-name", "# no frontmatter\n")
        self.assertEqual(skill_name(read_skill_md(skill)[0], skill), "dir-name")
        skill = self.make_skill("blank-name", fm("name: ''"))
        self.assertEqual(skill_name(read_skill_md(skill)[0], skill), "blank-name")

    def test_undecodable_bytes_do_not_change_the_name(self):
        skill = self.base / "latin"
        skill.mkdir()
        (skill / "SKILL.md").write_bytes(b"---\nname: real-name\ndescription: caf\xe9\n---\n")
        self.assertEqual(skill_name(read_skill_md(skill)[0], skill), "real-name")

    @staticmethod
    def review_name(review_skill, skill: Path) -> str:
        with patch.object(review_skill, "find_skill", return_value=(skill, "user")):
            return review_skill.review_skill(skill.name)["name"]

    def test_every_script_reads_the_same_name(self):
        """The duplicate preflight and the installer must agree on a skill's name."""
        import audit_skill_duplicates
        import eval_viewer
        import install_skill
        import review_skill
        import show_skill
        import transfer_test
        import trigger_test

        texts = {
            "quoted": fm('name: "real-name"  # comment', "description: >", "  Folded text."),
            "nested": fm("metadata:", "  name: inner", "name: real-name"),
            "repeated": fm("name: old-name", "description: x", "name: real-name"),
        }
        for label, text in texts.items():
            with self.subTest(label):
                skill = self.make_skill(f"dir-{label}", text)
                record = audit_skill_duplicates.record_for_directory(skill, self.base, "test")
                names = {
                    "audit": record.name,
                    "install": install_skill.parse_skill_name(skill),
                    "list": skill_summary(skill)["name"],
                    "eval": eval_viewer.parse_skill_name(text, None),
                    "show": show_skill.get_skill_info(skill, "user")["name"],
                    "review": self.review_name(review_skill, skill),
                    "transfer": transfer_test.parse_frontmatter(text)["name"],
                    "trigger": trigger_test.parse_frontmatter(text)["name"],
                }
                self.assertEqual(set(names.values()), {"real-name"}, names)


class FindSkillInAgentTests(unittest.TestCase):
    def test_copy_and_move_share_one_lookup(self):
        import agents
        import copy_skill
        import move_skill_agent

        self.assertIs(copy_skill.find_skill_in_agent, agents.find_skill_in_agent)
        self.assertIs(move_skill_agent.find_skill_in_agent, agents.find_skill_in_agent)

    def test_global_scope_wins_and_requires_skill_md(self):
        import agents

        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            dirs = {"global": base / "global", "project": base / "project"}
            (dirs["global"] / "only-dir").mkdir(parents=True)
            for scope in dirs:
                (dirs[scope] / "demo").mkdir(parents=True)
                (dirs[scope] / "demo" / "SKILL.md").write_text(fm("name: demo"), encoding="utf-8")

            with patch.object(agents, "get_skills_dir", side_effect=lambda a, s, cwd=None: dirs[s]):
                self.assertEqual(agents.find_skill_in_agent("demo", "codex"),
                                 (dirs["global"] / "demo", "global"))
                self.assertEqual(agents.find_skill_in_agent("demo", "codex", "project"),
                                 (dirs["project"] / "demo", "project"))
                self.assertEqual(agents.find_skill_in_agent("only-dir", "codex"), (None, None))


if __name__ == "__main__":
    unittest.main()
