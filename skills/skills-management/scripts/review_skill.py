#!/usr/bin/env python3
"""Review a Claude Code skill against best practices."""

import argparse
import json
import re
import sys
from pathlib import Path


def get_user_skills_dir() -> Path:
    return Path.home() / ".claude" / "skills"


def get_project_skills_dir() -> Path:
    return Path.cwd() / ".claude" / "skills"


def find_skill(name: str, scope: str | None = None) -> tuple[Path | None, str | None]:
    """Find a skill by name, optionally filtering by scope."""
    scopes_to_check = []
    if scope is None or scope == "user":
        scopes_to_check.append(("user", get_user_skills_dir()))
    if scope is None or scope == "project":
        scopes_to_check.append(("project", get_project_skills_dir()))

    for scope_name, skills_dir in scopes_to_check:
        skill_path = skills_dir / name
        if skill_path.exists() and (skill_path / "SKILL.md").exists():
            return skill_path, scope_name
    return None, None


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter and return (metadata, body)."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content

    frontmatter = match.group(1)
    body = match.group(2)
    metadata = {}

    for line in frontmatter.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip().strip('"\'')

    return metadata, body


def check_name(name: str) -> list[dict]:
    """Check name against best practices."""
    issues = []

    # Reserved words
    reserved = ["anthropic", "claude"]
    for word in reserved:
        if word in name.lower():
            issues.append({
                "severity": "warning",
                "rule": "reserved-word",
                "message": f"Name contains reserved word '{word}'",
                "suggestion": f"Consider renaming without '{word}' (e.g., 'skills-manager' instead of 'claude-skills-manager')"
            })

    # Naming convention (gerund form preferred)
    if not re.match(r"^[a-z][a-z0-9-]*$", name):
        issues.append({
            "severity": "error",
            "rule": "name-format",
            "message": "Name must be lowercase letters, numbers, and hyphens only",
            "suggestion": "Use format like 'processing-pdfs' or 'managing-databases'"
        })

    if len(name) > 64:
        issues.append({
            "severity": "error",
            "rule": "name-length",
            "message": f"Name exceeds 64 characters ({len(name)} chars)",
            "suggestion": "Shorten the name to 64 characters or less"
        })

    # Check for gerund form (recommended but not required)
    gerund_pattern = r"^[a-z]+-?[a-z]*ing(-[a-z]+)*$|^[a-z]*ing-[a-z]+(-[a-z]+)*$"
    if not re.match(gerund_pattern, name):
        issues.append({
            "severity": "info",
            "rule": "gerund-form",
            "message": "Name doesn't use recommended gerund form (verb + -ing)",
            "suggestion": f"Consider renaming to gerund form (e.g., 'managing-skills' instead of '{name}')"
        })

    return issues


def check_description(description: str) -> list[dict]:
    """Check description against best practices."""
    issues = []

    if not description:
        issues.append({
            "severity": "error",
            "rule": "description-required",
            "message": "Description is empty",
            "suggestion": "Add a description that explains what the skill does and when to use it"
        })
        return issues

    if len(description) > 1024:
        issues.append({
            "severity": "error",
            "rule": "description-length",
            "message": f"Description exceeds 1024 characters ({len(description)} chars)",
            "suggestion": "Shorten the description to 1024 characters or less"
        })

    # Check for trigger words
    trigger_patterns = [
        r"\buse when\b",
        r"\buse for\b",
        r"\btrigger[s]? on\b",
        r"\bwhen (the )?user\b",
        r"\bwhen asked\b",
    ]
    has_trigger = any(re.search(p, description.lower()) for p in trigger_patterns)
    if not has_trigger:
        issues.append({
            "severity": "warning",
            "rule": "missing-triggers",
            "message": "Description doesn't include trigger conditions",
            "suggestion": "Add 'Use when...' to help Claude know when to invoke this skill"
        })

    # Check for first/second person (should be third person)
    first_second_person = [
        (r"\bI can\b", "I can"),
        (r"\bI will\b", "I will"),
        (r"\bI help\b", "I help"),
        (r"\byou can\b", "you can"),
        (r"\byou will\b", "you will"),
        (r"\bwe can\b", "we can"),
    ]
    for pattern, phrase in first_second_person:
        if re.search(pattern, description, re.IGNORECASE):
            issues.append({
                "severity": "warning",
                "rule": "third-person",
                "message": f"Description uses '{phrase}' instead of third person",
                "suggestion": "Rewrite in third person (e.g., 'Processes files...' not 'I process files...')"
            })
            break

    # Check for vague descriptions
    vague_patterns = [
        (r"^helps with \w+$", "Too vague"),
        (r"^processes data$", "Too vague"),
        (r"^does stuff", "Too vague"),
        (r"^utility for", "Too vague"),
        (r"^helper for", "Too vague"),
    ]
    for pattern, reason in vague_patterns:
        if re.search(pattern, description.lower()):
            issues.append({
                "severity": "warning",
                "rule": "vague-description",
                "message": f"Description is too vague: {reason}",
                "suggestion": "Be specific about what the skill does and include key terms"
            })
            break

    # Check for negative triggers (reduces overtriggering)
    negative_patterns = [
        r"\bdon'?t use\b",
        r"\bdo not use\b",
        r"\bnot for\b",
        r"\bnot when\b",
        r"\bdon'?t trigger\b",
        r"\bnot intended for\b",
    ]
    has_negative = any(re.search(p, description.lower()) for p in negative_patterns)
    if not has_negative:
        issues.append({
            "severity": "info",
            "rule": "missing-negative-triggers",
            "message": "Description doesn't include negative triggers",
            "suggestion": "Add 'Don't use for...' or 'Not for...' to prevent overtriggering on similar tasks"
        })

    return issues


def check_name_matches_dir(name: str, skill_path: Path) -> list[dict]:
    """Check that frontmatter name matches the parent directory name."""
    issues = []
    dir_name = skill_path.name
    if name and name != dir_name:
        issues.append({
            "severity": "error",
            "rule": "name-dir-mismatch",
            "message": f"Frontmatter name '{name}' does not match directory name '{dir_name}'",
            "suggestion": f"Rename the directory to '{name}' or change the name field to '{dir_name}'"
        })
    return issues


def check_frontmatter_xml(metadata: dict) -> list[dict]:
    """Check frontmatter fields for forbidden XML angle brackets."""
    issues = []
    for field in ("name", "description"):
        value = metadata.get(field, "")
        if re.search(r"[<>]", value):
            issues.append({
                "severity": "error",
                "rule": "xml-in-frontmatter",
                "message": f"Field '{field}' contains XML angle brackets (< >)",
                "suggestion": "Remove < > characters — they can cause prompt injection in the system prompt"
            })
    return issues


def check_body(body: str, skill_path: Path) -> list[dict]:
    """Check SKILL.md body against best practices."""
    issues = []
    lines = body.split("\n")
    line_count = len(lines)

    # Line count check
    if line_count > 500:
        issues.append({
            "severity": "warning",
            "rule": "body-length",
            "message": f"SKILL.md body exceeds 500 lines ({line_count} lines)",
            "suggestion": "Split content into separate reference files using progressive disclosure"
        })

    # Check for time-sensitive information
    time_patterns = [
        (r"\b(before|after) (january|february|march|april|may|june|july|august|september|october|november|december) \d{4}\b", "date reference"),
        (r"\b(before|after) \d{4}\b", "year reference"),
        (r"\bas of \d{4}\b", "as of year"),
        (r"\bstarting (in )?\d{4}\b", "starting year"),
        (r"\buntil \d{4}\b", "until year"),
    ]
    for pattern, desc in time_patterns:
        matches = re.findall(pattern, body.lower())
        if matches:
            issues.append({
                "severity": "warning",
                "rule": "time-sensitive",
                "message": f"Body contains time-sensitive information ({desc})",
                "suggestion": "Move time-sensitive info to 'Old patterns' section or remove"
            })
            break

    # Check for Windows-style paths
    if re.search(r"[a-zA-Z]:\\|\\\\", body):
        issues.append({
            "severity": "warning",
            "rule": "windows-paths",
            "message": "Body contains Windows-style paths (backslashes)",
            "suggestion": "Use forward slashes for cross-platform compatibility"
        })

    # Check for deeply nested references (more than one level)
    ref_files = re.findall(r"\[.*?\]\(([^)]+\.md)\)", body)
    for ref_file in ref_files:
        ref_path = skill_path / ref_file
        if ref_path.exists():
            ref_content = ref_path.read_text()
            nested_refs = re.findall(r"\[.*?\]\(([^)]+\.md)\)", ref_content)
            if nested_refs:
                issues.append({
                    "severity": "info",
                    "rule": "nested-references",
                    "message": f"Reference file '{ref_file}' contains further references",
                    "suggestion": "Keep references one level deep from SKILL.md for reliable file reading"
                })

    # Check for table of contents in long files
    if line_count > 100:
        toc_patterns = [r"## contents", r"## table of contents", r"- \[.*\]\(#"]
        has_toc = any(re.search(p, body.lower()) for p in toc_patterns)
        if not has_toc:
            issues.append({
                "severity": "info",
                "rule": "missing-toc",
                "message": "Long file (>100 lines) without table of contents",
                "suggestion": "Add a table of contents to help Claude navigate the content"
            })

    return issues


def _approx_tokens(text: str) -> int:
    """Approximate token count using the SkillOpt heuristic (chars / 4)."""
    return len(text) // 4


def _strip_fenced_code(body: str) -> str:
    """Remove fenced code blocks and indented (4-space) code blocks from body."""
    # Remove triple-fenced blocks (``` … ```)
    without_fences = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    # Remove indented code blocks (lines starting with 4+ spaces or a tab)
    cleaned_lines = []
    for line in without_fences.split("\n"):
        if re.match(r"^( {4,}|\t)", line):
            continue
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)


def _extract_slow_update_section(body: str) -> str | None:
    """Return content between SLOW_UPDATE markers, or None if not both present."""
    start_marker = "<!-- SLOW_UPDATE_START -->"
    end_marker = "<!-- SLOW_UPDATE_END -->"
    if start_marker not in body or end_marker not in body:
        return None
    start_idx = body.find(start_marker)
    end_idx = body.find(end_marker)
    if start_idx >= end_idx:
        return None
    return body[start_idx + len(start_marker):end_idx]


def check_tokens(body: str, skill_path: Path) -> list[dict]:
    """Check token footprint against SkillOpt guidelines (300-2000 tokens)."""
    issues = []

    body_tokens = _approx_tokens(body)

    # Sum tokens across all reference files
    references_tokens = 0
    references_dir = skill_path / "references"
    if references_dir.exists() and references_dir.is_dir():
        for ref_file in references_dir.rglob("*"):
            if ref_file.is_file():
                try:
                    ref_text = ref_file.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                references_tokens += _approx_tokens(ref_text)

    total_tokens = body_tokens + references_tokens

    # Footprint info line (synthetic issue carrying the totals)
    issues.append({
        "severity": "info",
        "rule": "token-footprint",
        "message": (
            f"Token footprint — body: {body_tokens}, "
            f"references: {references_tokens}, total: {total_tokens}"
        ),
        "suggestion": "SkillOpt sweet spot is 300-2000 body tokens; push detail into references/"
    })

    if body_tokens < 300:
        issues.append({
            "severity": "info",
            "rule": "body-tokens-small",
            "message": f"Skill body unusually small ({body_tokens} tokens); may be a stub or over-summarised",
            "suggestion": "Expand the body to ~300-2000 tokens if more procedural guidance is needed"
        })
    elif body_tokens <= 2000:
        issues.append({
            "severity": "info",
            "rule": "body-tokens-compact",
            "message": f"Compact ({body_tokens} tokens) — SkillOpt sweet spot",
            "suggestion": "Maintain compactness; move new detail into references/ when adding content"
        })
    elif body_tokens <= 4000:
        issues.append({
            "severity": "warning",
            "rule": "body-tokens-large",
            "message": f"Above SkillOpt 2000-token target ({body_tokens} tokens) — consider splitting into references/",
            "suggestion": "Move detail, examples, and tables into references/ to keep SKILL.md compact"
        })
    else:
        issues.append({
            "severity": "warning",
            "rule": "body-tokens-bloated",
            "message": f"Far above SkillOpt target ({body_tokens} tokens) — high risk of context bloat; move detail into references/",
            "suggestion": "Aggressively extract sections into references/; SKILL.md should be procedural rules, not a manual"
        })

    return issues


def check_procedurality(body: str) -> list[dict]:
    """Detect instance-specific signals that hint the skill is task-tied rather than procedural."""
    issues = []

    # Strip fenced/indented code blocks so legitimate examples don't trip heuristics
    prose = _strip_fenced_code(body)

    triggered_heuristics = 0
    concrete_hits: list[str] = []

    # 1) Long quoted strings containing digits or filename-like tokens
    quoted_matches = re.findall(r'"([^"\n]{41,})"', prose)
    quoted_concrete = [
        q for q in quoted_matches
        if re.search(r"\d", q) or re.search(r"\b\w+\.(csv|json|xml|xlsx|sql|parquet|md|txt|py|js|tsv)\b", q)
    ]
    if quoted_concrete:
        triggered_heuristics += 1
        concrete_hits.extend(quoted_concrete[:5])

    # 2) Task-specific filenames in prose
    filename_matches = re.findall(r"\b\w+\.(?:csv|json|xml|xlsx|sql|parquet)\b", prose)
    if filename_matches:
        triggered_heuristics += 1
        concrete_hits.extend(filename_matches[:5])

    # 3) Long literal numbers in non-code context (percentages, quarter labels, etc.)
    literal_numbers = re.findall(r"\b\d{2,}\.\d+%|\b\d{4}-Q[1-4]\b|\b\d{4}-\d{2}-\d{2}\b", prose)
    if literal_numbers:
        triggered_heuristics += 1
        concrete_hits.extend(literal_numbers[:5])

    # 4) Patterns like "task X", "question #N", "the file at /path/to/specific.thing"
    pattern_hits: list[str] = []
    pattern_hits.extend(re.findall(r"\btask\s+[A-Z0-9]+\b", prose))
    pattern_hits.extend(re.findall(r"\bquestion\s*#\s*\d+\b", prose, re.IGNORECASE))
    pattern_hits.extend(re.findall(r"the file at\s+/[\w./-]+\.\w+", prose, re.IGNORECASE))
    if pattern_hits:
        triggered_heuristics += 1
        concrete_hits.extend(pattern_hits[:5])

    if triggered_heuristics >= 3 or len(concrete_hits) >= 5:
        issues.append({
            "severity": "info",
            "rule": "instance-specific-leakage",
            "message": (
                f"Body contains {len(concrete_hits)} instance-specific markers — "
                "SkillOpt rules should be procedural, not task-specific"
            ),
            "suggestion": (
                "Prefer general principles ('Infer expected answer type from clue wording') "
                "over task-specific values"
            )
        })

    return issues


def check_patch_friendliness(body: str) -> list[dict]:
    """Check that the body has stable anchors for atomic patch operations."""
    issues = []

    lines = body.split("\n")
    body_lines = len(lines)

    # Count ## and ### headings (exclude #### and deeper, and excluded #)
    heading_lines = [ln for ln in lines if re.match(r"^#{2,3}\s+\S", ln)]
    heading_count = len(heading_lines)

    # Count bolded labels like **Foo:**
    bolded_label_count = len(re.findall(r"\*\*[^*\n]+:\*\*", body))

    anchor_density = (heading_count + bolded_label_count) / max(1, body_lines)

    if anchor_density < 0.04 and body_lines > 60:
        issues.append({
            "severity": "info",
            "rule": "low-anchor-density",
            "message": (
                "Body has few headings/anchors relative to length — "
                "automated `insert_after` edits will be unreliable"
            ),
            "suggestion": (
                "Add `##`/`###` headings or `**Label:**` markers every ~25 lines "
                "so patches have stable targets"
            )
        })

    # Detect duplicate heading texts (break exact-match insert_after targets)
    heading_texts = [re.sub(r"^#{2,3}\s+", "", ln).strip() for ln in heading_lines]
    seen: dict[str, int] = {}
    for text in heading_texts:
        seen[text] = seen.get(text, 0) + 1
    duplicates = sorted({text for text, count in seen.items() if count > 1})
    if duplicates:
        preview = ", ".join(f"'{t}'" for t in duplicates[:3])
        more = f" (+{len(duplicates) - 3} more)" if len(duplicates) > 3 else ""
        issues.append({
            "severity": "info",
            "rule": "duplicate-anchors",
            "message": (
                f"Repeated heading texts detected: {preview}{more} — "
                "these break exact-match `insert_after` targets"
            ),
            "suggestion": "Make each heading unique so patch operations can locate it unambiguously"
        })

    return issues


def check_slow_update_section(body: str) -> list[dict]:
    """Validate the protected SLOW_UPDATE longitudinal-guidance section markers."""
    issues = []

    start_marker = "<!-- SLOW_UPDATE_START -->"
    end_marker = "<!-- SLOW_UPDATE_END -->"
    has_start = start_marker in body
    has_end = end_marker in body

    if has_start ^ has_end:
        issues.append({
            "severity": "error",
            "rule": "slow-update-unbalanced",
            "message": "Slow-update markers are unbalanced",
            "suggestion": "Either include both markers or remove the lone one"
        })
        return issues

    if not has_start and not has_end:
        return issues

    start_idx = body.find(start_marker)
    end_idx = body.find(end_marker)

    if start_idx > end_idx:
        issues.append({
            "severity": "error",
            "rule": "slow-update-unbalanced",
            "message": "Slow-update START marker appears after END marker",
            "suggestion": "Reorder markers so START precedes END"
        })
        return issues

    inner = body[start_idx + len(start_marker):end_idx]
    if start_marker in inner:
        issues.append({
            "severity": "warning",
            "rule": "slow-update-nested",
            "message": "Nested SLOW_UPDATE_START marker found inside slow-update section",
            "suggestion": "Remove nested START markers — the section must be flat"
        })

    issues.append({
        "severity": "info",
        "rule": "slow-update-present",
        "message": "Protected slow-update section detected (managed by epoch-boundary optimiser)",
        "suggestion": "Do not edit this section with normal patches; reserved for slow-update flow"
    })

    return issues


def check_structure(skill_path: Path) -> list[dict]:
    """Check skill directory structure."""
    issues = []

    # README.md is allowed for skills that are published (e.g. via `npx skills add` / skills.sh):
    # the page renders the skill's README, so a top-level README is part of the public surface.
    # We only flag it as INFO so the maintainer is reminded not to duplicate SKILL.md content there.
    readme_path = skill_path / "README.md"
    if readme_path.exists():
        issues.append({
            "severity": "info",
            "rule": "readme-present",
            "message": "Skill contains a README.md",
            "suggestion": "OK for publishable skills (rendered on skills.sh/GitHub). Keep it short — install instructions + 'why this skill' only. Do not duplicate SKILL.md guidance; that file is what the agent reads at runtime."
        })

    # Other doc files are still warnings — agents do not read them and they bloat the skill.
    forbidden_docs = ["CHANGELOG.md", "INSTALLATION_GUIDE.md", "CONTRIBUTING.md", "LICENSE.md"]
    for doc_name in forbidden_docs:
        doc_path = skill_path / doc_name
        if doc_path.exists():
            issues.append({
                "severity": "warning",
                "rule": "forbidden-doc-file",
                "message": f"Skill contains '{doc_name}' — not needed inside a skill folder",
                "suggestion": "Move documentation to SKILL.md, references/, or the repository root. Skills are for agents, not humans"
            })

    # Check for reference files longer than 100 lines without TOC
    for md_file in skill_path.glob("**/*.md"):
        if md_file.name == "SKILL.md":
            continue
        content = md_file.read_text()
        lines = content.split("\n")
        if len(lines) > 100:
            toc_patterns = [r"## contents", r"## table of contents", r"- \[.*\]\(#"]
            has_toc = any(re.search(p, content.lower()) for p in toc_patterns)
            if not has_toc:
                rel_path = md_file.relative_to(skill_path)
                issues.append({
                    "severity": "info",
                    "rule": "reference-toc",
                    "message": f"Reference file '{rel_path}' exceeds 100 lines without TOC",
                    "suggestion": "Add table of contents to help Claude navigate"
                })

    return issues


def review_skill(name: str, scope: str | None = None, output_format: str = "text") -> dict:
    """Review a skill against best practices.

    Returns:
        Dict with skill info and issues found
    """
    skill_path, found_scope = find_skill(name, scope)

    if not skill_path:
        return {
            "error": f"Skill '{name}' not found",
            "found": False
        }

    skill_md = skill_path / "SKILL.md"
    content = skill_md.read_text()
    metadata, body = parse_frontmatter(content)

    skill_name = metadata.get("name", skill_path.name)
    description = metadata.get("description", "")

    all_issues = []
    all_issues.extend(check_name(skill_name))
    all_issues.extend(check_name_matches_dir(skill_name, skill_path))
    all_issues.extend(check_description(description))
    all_issues.extend(check_frontmatter_xml(metadata))
    all_issues.extend(check_body(body, skill_path))
    all_issues.extend(check_structure(skill_path))
    all_issues.extend(check_tokens(body, skill_path))
    all_issues.extend(check_procedurality(body))
    all_issues.extend(check_patch_friendliness(body))
    all_issues.extend(check_slow_update_section(body))

    # Compute footprint stats (re-used for both JSON output and scoring)
    body_tokens = _approx_tokens(body)
    references_tokens = 0
    references_dir = skill_path / "references"
    if references_dir.exists() and references_dir.is_dir():
        for ref_file in references_dir.rglob("*"):
            if ref_file.is_file():
                try:
                    references_tokens += _approx_tokens(
                        ref_file.read_text(encoding="utf-8", errors="replace")
                    )
                except OSError:
                    continue

    slow_update_inner = _extract_slow_update_section(body)
    slow_update_tokens = _approx_tokens(slow_update_inner) if slow_update_inner is not None else 0
    total_tokens = body_tokens + references_tokens

    # Anchor density (re-derived for output / scoring)
    body_line_list = body.split("\n")
    body_lines = len(body_line_list)
    heading_lines = [ln for ln in body_line_list if re.match(r"^#{2,3}\s+\S", ln)]
    heading_count = len(heading_lines)
    bolded_label_count = len(re.findall(r"\*\*[^*\n]+:\*\*", body))
    anchor_density = (heading_count + bolded_label_count) / max(1, body_lines)

    # Count by severity
    error_count = len([i for i in all_issues if i["severity"] == "error"])
    warning_count = len([i for i in all_issues if i["severity"] == "warning"])
    info_count = len([i for i in all_issues if i["severity"] == "info"])

    # Calculate score
    score = 100
    score -= error_count * 20
    score -= warning_count * 10
    score -= info_count * 2
    if body_tokens > 4000:
        score -= 15
    if body_tokens > 2000:
        score -= 5
    if anchor_density < 0.04 and body_lines > 60:
        score -= 5
    score = max(0, score)

    return {
        "found": True,
        "name": skill_name,
        "scope": found_scope,
        "path": str(skill_path),
        "description": description,
        "body_lines": body_lines,
        "body_tokens": body_tokens,
        "references_tokens": references_tokens,
        "slow_update_tokens": slow_update_tokens,
        "total_tokens": total_tokens,
        "anchor_density": round(anchor_density, 4),
        "heading_count": heading_count,
        "issues": all_issues,
        "summary": {
            "errors": error_count,
            "warnings": warning_count,
            "info": info_count,
            "score": score
        }
    }


def format_output(result: dict, output_format: str) -> str:
    """Format review results for output."""
    if output_format == "json":
        return json.dumps(result, indent=2)

    if not result.get("found"):
        return f"Error: {result.get('error', 'Unknown error')}"

    lines = [
        f"{'=' * 60}",
        f"Skill Review: {result['name']}",
        f"{'=' * 60}",
        f"Scope: {result['scope']}",
        f"Path:  {result['path']}",
        f"Lines: {result['body_lines']}",
        f"",
        f"Token footprint:",
        f"  Body:           {result['body_tokens']} tokens  (target 300-2000)",
        f"  References:     {result['references_tokens']} tokens",
        f"  Slow-update:    {result['slow_update_tokens']} tokens  (protected section)",
        f"  Total:          {result['total_tokens']} tokens",
        f"",
        f"Score: {result['summary']['score']}/100",
        f"  Errors:   {result['summary']['errors']}",
        f"  Warnings: {result['summary']['warnings']}",
        f"  Info:     {result['summary']['info']}",
    ]

    if result["issues"]:
        lines.append("")
        lines.append("Issues Found:")
        lines.append("-" * 40)

        for issue in result["issues"]:
            severity = issue["severity"].upper()
            icon = {"error": "❌", "warning": "⚠️", "info": "ℹ️"}.get(issue["severity"], "•")
            lines.append(f"")
            lines.append(f"{icon} [{severity}] {issue['rule']}")
            lines.append(f"   {issue['message']}")
            lines.append(f"   → {issue['suggestion']}")
    else:
        lines.append("")
        lines.append("✅ No issues found! Skill follows best practices.")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Review a Claude Code skill against best practices"
    )
    parser.add_argument("name", help="Name of the skill to review")
    parser.add_argument(
        "--scope", "-s",
        choices=["user", "project"],
        help="Scope to search (default: search both)"
    )
    parser.add_argument(
        "--format", "-f",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)"
    )
    args = parser.parse_args()

    result = review_skill(args.name, args.scope, args.format)
    print(format_output(result, args.format))

    if not result.get("found"):
        return 1
    return 0 if result["summary"]["errors"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
