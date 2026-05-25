#!/usr/bin/env python3
"""Run trigger tests against a skill's description.

Given a list of user prompts and the expected trigger outcome for each,
report match rate. Two judges are supported: a heuristic regex-based judge
(default) and an opt-in `claude -p` CLI judge.

Inspired by Microsoft's SkillOpt paper (arXiv 2605.23904) which shows
optimised skills transfer across models and harnesses; trigger fidelity is
a precondition for that.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


def get_user_skills_dir() -> Path:
    """Get the user-level skills directory."""
    return Path.home() / ".claude" / "skills"


def get_project_skills_dir() -> Path:
    """Get the project-level skills directory (current working directory)."""
    return Path.cwd() / ".claude" / "skills"


def find_skill(name: str, scope: str | None = None) -> tuple[Path | None, str | None]:
    """Find a skill by name, optionally filtering by scope.

    Returns:
        Tuple of (skill_path, scope_name) or (None, None) if not found
    """
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


def parse_frontmatter(content: str) -> dict:
    """Parse YAML frontmatter from SKILL.md content."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}

    frontmatter = match.group(1)
    metadata = {}

    current_key = None
    current_value = []

    for line in frontmatter.split("\n"):
        key_match = re.match(r"^(\w[\w-]*):\s*(.*)", line)
        if key_match:
            if current_key:
                value = "\n".join(current_value).strip()
                metadata[current_key] = value.strip('"\'')
            current_key = key_match.group(1)
            current_value = [key_match.group(2)]
        elif current_key and line.startswith("  "):
            current_value.append(line.strip())

    if current_key:
        value = "\n".join(current_value).strip()
        metadata[current_key] = value.strip('"\'')

    return metadata


# Common English stop words removed when extracting keywords.
STOP_WORDS = {
    "a", "an", "the", "and", "or", "but", "if", "then", "else", "when",
    "while", "of", "to", "in", "on", "at", "for", "with", "by", "from",
    "as", "is", "are", "was", "were", "be", "been", "being", "have",
    "has", "had", "do", "does", "did", "doing", "will", "would", "shall",
    "should", "may", "might", "must", "can", "could", "this", "that",
    "these", "those", "it", "its", "they", "them", "their", "he", "she",
    "his", "her", "we", "our", "you", "your", "i", "me", "my", "us",
    "use", "uses", "used", "using", "user", "user's", "trigger", "triggers",
    "triggered", "triggering", "skill", "skills", "claude", "code",
    "ask", "asks", "asking", "asked", "want", "wants", "needs", "need",
    "any", "all", "some", "no", "not", "yes", "also", "only", "just",
    "what", "which", "who", "where", "why", "how", "include", "includes",
    "like", "such", "etc", "via", "through", "into", "out", "up", "down",
    "over", "under", "again", "more", "most", "other", "than", "so",
    "very", "really", "much", "many", "few", "lot", "lots", "every",
    "each", "either", "both", "between", "across", "during", "before",
    "after", "above", "below", "since", "until",
}


def extract_quoted_phrases(description: str) -> list[str]:
    """Extract quoted trigger phrases from a description.

    Picks up both double-quoted and single-quoted spans plus backtick spans.
    Returns lowercased phrases stripped of surrounding whitespace.
    """
    phrases = []
    # Double quotes
    for match in re.finditer(r'"([^"]+)"', description):
        phrase = match.group(1).strip()
        if phrase:
            phrases.append(phrase.lower())
    # Single quotes (avoid possessives by requiring a space inside)
    for match in re.finditer(r"'([^']+ [^']+)'", description):
        phrase = match.group(1).strip()
        if phrase:
            phrases.append(phrase.lower())
    # Backticks
    for match in re.finditer(r"`([^`]+)`", description):
        phrase = match.group(1).strip()
        if phrase:
            phrases.append(phrase.lower())
    return phrases


def extract_keywords(description: str) -> set[str]:
    """Extract trigger keywords from a description.

    Looks for words after "Use when", "triggers on", "triggers include",
    then falls back to the whole description. Stop words are removed.
    """
    desc_lower = description.lower()
    sections = []

    trigger_intros = [
        r"use when\b",
        r"use for\b",
        r"triggers on\b",
        r"triggers include\b",
        r"trigger[s]? when\b",
        r"when (?:the )?user\b",
        r"when asked\b",
    ]

    for pattern in trigger_intros:
        for match in re.finditer(pattern, desc_lower):
            start = match.end()
            chunk = desc_lower[start:start + 400]
            sections.append(chunk)

    if not sections:
        sections.append(desc_lower)

    keywords = set()
    for section in sections:
        # Strip punctuation, keep words
        for raw in re.findall(r"[a-z][a-z0-9'-]{2,}", section):
            if raw in STOP_WORDS:
                continue
            keywords.add(raw)

    return keywords


def tokenize_prompt(prompt: str) -> set[str]:
    """Tokenize a prompt to lowercased non-stop-word tokens."""
    tokens = set()
    for raw in re.findall(r"[a-z][a-z0-9'-]{2,}", prompt.lower()):
        if raw in STOP_WORDS:
            continue
        tokens.add(raw)
    return tokens


def heuristic_judge(description: str, prompt: str) -> tuple[bool, str]:
    """Heuristic regex-based judge.

    Returns (would_trigger, reason).
    """
    prompt_lower = prompt.lower()

    # 1. Exact quoted-phrase match wins immediately.
    for phrase in extract_quoted_phrases(description):
        if phrase in prompt_lower:
            return True, f"matched quoted phrase: '{phrase}'"

    # 2. Keyword overlap.
    keywords = extract_keywords(description)
    tokens = tokenize_prompt(prompt)
    overlap = keywords & tokens
    if len(overlap) >= 2:
        sample = sorted(overlap)[:5]
        return True, f"keyword overlap ({len(overlap)}): {', '.join(sample)}"

    if overlap:
        return False, f"insufficient overlap ({len(overlap)}): {sorted(overlap)[0]}"

    return False, "no quoted phrase or keyword overlap"


def claude_cli_judge(description: str, prompt: str) -> tuple[bool, str]:
    """Use `claude -p` as the judge.

    Falls back to a clear error reason if the CLI is unavailable or returns
    something other than the expected JSON.
    """
    instruction = (
        "You are testing whether a skill description triggers on a user prompt.\n"
        "\n"
        f"Skill description: {description}\n"
        "\n"
        f"User prompt: {prompt}\n"
        "\n"
        "Would Claude Code auto-invoke this skill on the prompt? Respond ONLY "
        'with a JSON object:\n'
        '{"trigger": true|false, "reason": "<one line>"}'
    )

    try:
        result = subprocess.run(
            ["claude", "-p", instruction],
            capture_output=True,
            text=True,
            timeout=120,
        )
    except FileNotFoundError:
        return False, "claude CLI not found on PATH"
    except subprocess.TimeoutExpired:
        return False, "claude CLI timed out"

    if result.returncode != 0:
        stderr = result.stderr.strip().splitlines()[-1] if result.stderr else ""
        return False, f"claude CLI exit={result.returncode}: {stderr}"

    raw = result.stdout.strip()
    # Pick out the first {...} block in case the CLI wraps the answer.
    json_match = re.search(r"\{.*?\}", raw, re.DOTALL)
    if not json_match:
        return False, f"no JSON in response: {raw[:80]}"

    try:
        parsed = json.loads(json_match.group(0))
    except json.JSONDecodeError as exc:
        return False, f"invalid JSON ({exc}): {json_match.group(0)[:80]}"

    trig = bool(parsed.get("trigger", False))
    reason = str(parsed.get("reason", "")).strip() or "(no reason)"
    return trig, reason


# ---------- cases file loading ----------

def parse_simple_yaml_list(text: str) -> list[dict]:
    """Parse a tiny YAML subset: top-level list of dicts, scalar values only.

    Supports:
      - lines starting with '- key: value'
      - continuation lines '  key: value'
      - '#' comments
      - quoted string values (single or double quotes)
    """
    items: list[dict] = []
    current: dict | None = None

    for raw_line in text.splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        dash_match = re.match(r"^-\s+([\w-]+):\s*(.*)$", line)
        if dash_match:
            if current is not None:
                items.append(current)
            current = {}
            key = dash_match.group(1)
            value = dash_match.group(2).strip().strip('"\'')
            current[key] = value
            continue

        cont_match = re.match(r"^\s+([\w-]+):\s*(.*)$", line)
        if cont_match and current is not None:
            key = cont_match.group(1)
            value = cont_match.group(2).strip().strip('"\'')
            current[key] = value
            continue

    if current is not None:
        items.append(current)

    return items


def load_cases(cases_path: Path) -> list[dict]:
    """Load test cases from a YAML or JSON file."""
    text = cases_path.read_text()
    suffix = cases_path.suffix.lower()

    if suffix == ".json":
        data = json.loads(text)
        if not isinstance(data, list):
            raise ValueError("JSON cases file must be a top-level list")
        return data

    if suffix in (".yaml", ".yml"):
        return parse_simple_yaml_list(text)

    # Try to be forgiving: detect by leading character.
    stripped = text.lstrip()
    if stripped.startswith("["):
        return json.loads(text)
    return parse_simple_yaml_list(text)


def normalise_expect(value: str) -> str:
    """Normalise an 'expect' field to 'trigger' or 'no-trigger'."""
    val = (value or "").strip().lower()
    if val in ("trigger", "yes", "true", "1"):
        return "trigger"
    if val in ("no-trigger", "no", "false", "0", "notrigger", "no_trigger"):
        return "no-trigger"
    return val


# ---------- core run ----------

def run_cases(
    description: str,
    cases: list[dict],
    judge: str,
) -> dict:
    """Run cases and return aggregate metrics + per-case results."""
    judge_fn = heuristic_judge if judge == "heuristic" else claude_cli_judge

    tp = fp = tn = fn = 0
    results = []

    for idx, case in enumerate(cases):
        prompt = str(case.get("prompt", "")).strip()
        expected = normalise_expect(str(case.get("expect", "")))
        if not prompt or expected not in ("trigger", "no-trigger"):
            results.append({
                "index": idx,
                "prompt": prompt,
                "expected": expected,
                "actual": None,
                "reason": "invalid case (missing prompt or expect)",
                "correct": False,
            })
            continue

        actual_bool, reason = judge_fn(description, prompt)
        actual = "trigger" if actual_bool else "no-trigger"
        correct = actual == expected

        if expected == "trigger" and actual == "trigger":
            tp += 1
        elif expected == "no-trigger" and actual == "trigger":
            fp += 1
        elif expected == "no-trigger" and actual == "no-trigger":
            tn += 1
        elif expected == "trigger" and actual == "no-trigger":
            fn += 1

        results.append({
            "index": idx,
            "prompt": prompt,
            "expected": expected,
            "actual": actual,
            "reason": reason,
            "correct": correct,
        })

    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = (
        2 * precision * recall / (precision + recall)
        if (precision + recall)
        else 0.0
    )
    accuracy = (tp + tn) / len(cases) if cases else 0.0

    return {
        "judge": judge,
        "total": len(cases),
        "confusion": {
            "true_pos": tp,
            "false_pos": fp,
            "true_neg": tn,
            "false_neg": fn,
        },
        "metrics": {
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "f1": round(f1, 4),
            "accuracy": round(accuracy, 4),
        },
        "results": results,
    }


def format_text(skill_name: str, description: str, report: dict) -> str:
    """Format a text report."""
    lines = [
        "=" * 60,
        f"Trigger Test: {skill_name}",
        "=" * 60,
        f"Judge:       {report['judge']}",
        f"Cases:       {report['total']}",
        f"Description: {description[:200]}{'...' if len(description) > 200 else ''}",
        "",
        "Confusion Matrix:",
        f"  true_pos   = {report['confusion']['true_pos']}",
        f"  false_pos  = {report['confusion']['false_pos']}",
        f"  true_neg   = {report['confusion']['true_neg']}",
        f"  false_neg  = {report['confusion']['false_neg']}",
        "",
        "Metrics:",
        f"  precision = {report['metrics']['precision']:.4f}",
        f"  recall    = {report['metrics']['recall']:.4f}",
        f"  f1        = {report['metrics']['f1']:.4f}",
        f"  accuracy  = {report['metrics']['accuracy']:.4f}",
        "",
        "Per-Case Results:",
        "-" * 60,
    ]
    for r in report["results"]:
        status = "PASS" if r["correct"] else "FAIL"
        prompt = r["prompt"][:60] + ("..." if len(r["prompt"]) > 60 else "")
        lines.append(
            f"  [{status}] exp={r['expected']:<10} got={r['actual'] or 'invalid':<10} "
            f"prompt={prompt!r}"
        )
        if not r["correct"] or report["judge"] == "claude-cli":
            lines.append(f"         reason: {r['reason']}")
    return "\n".join(lines)


# ---------- --generate mode ----------

def generate_cases(description: str, target_count: int = 10) -> list[dict]:
    """Generate candidate test cases from a description.

    For each quoted phrase: 1-2 paraphrase prompts (expect=trigger) + 1
    unrelated prompt (expect=no-trigger). Keeps generating until target_count
    is reached or we run out of phrases.
    """
    cases: list[dict] = []

    phrases = extract_quoted_phrases(description)
    keywords = sorted(extract_keywords(description))

    # If no quoted phrases, synthesise some from top keywords.
    if not phrases and keywords:
        # Take pairs of keywords as pseudo-phrases.
        for kw in keywords[:3]:
            phrases.append(kw)

    unrelated_prompts = [
        "What's the weather today?",
        "Convert 100 USD to EUR.",
        "Tell me a joke.",
        "What time is it in Tokyo?",
        "Recommend a recipe for pasta.",
        "Who won the last World Cup?",
        "Explain quantum entanglement briefly.",
        "What's the capital of Australia?",
    ]
    unrelated_idx = 0

    for phrase in phrases:
        if len(cases) >= target_count:
            break

        # Paraphrase 1: literal use
        cases.append({
            "prompt": f"Can you help me with: {phrase}?",
            "expect": "trigger",
        })
        if len(cases) >= target_count:
            break

        # Paraphrase 2: instructional form
        cases.append({
            "prompt": f"I want to {phrase}.",
            "expect": "trigger",
        })
        if len(cases) >= target_count:
            break

        # Unrelated
        if unrelated_idx < len(unrelated_prompts):
            cases.append({
                "prompt": unrelated_prompts[unrelated_idx],
                "expect": "no-trigger",
            })
            unrelated_idx += 1

    # Pad with unrelated prompts if short.
    while len(cases) < target_count and unrelated_idx < len(unrelated_prompts):
        cases.append({
            "prompt": unrelated_prompts[unrelated_idx],
            "expect": "no-trigger",
        })
        unrelated_idx += 1

    return cases[:target_count]


def emit_yaml(cases: list[dict]) -> str:
    """Emit a list of cases as YAML (top-level list of dicts)."""
    out = ["# Generated trigger test cases. Curate before running."]
    for case in cases:
        prompt = case["prompt"].replace('"', '\\"')
        out.append(f'- prompt: "{prompt}"')
        out.append(f"  expect: {case['expect']}")
    return "\n".join(out) + "\n"


# ---------- main ----------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run trigger tests against a skill's description"
    )
    parser.add_argument("name", help="Name of the skill to test")
    parser.add_argument(
        "--cases",
        help="Path to a YAML or JSON file with test cases",
    )
    parser.add_argument(
        "--judge",
        choices=["heuristic", "claude-cli"],
        default="heuristic",
        help="Judge to use (default: heuristic)",
    )
    parser.add_argument(
        "--scope", "-s",
        choices=["user", "project"],
        help="Skill scope (default: search both)",
    )
    parser.add_argument(
        "--format", "-f",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument(
        "--generate",
        action="store_true",
        help="Print 10 candidate test cases derived from the description",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="Number of cases to generate with --generate (default: 10)",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.8,
        help="F1 threshold for exit-success (default: 0.8)",
    )
    args = parser.parse_args()

    skill_path, _ = find_skill(args.name, args.scope)
    if not skill_path:
        print(f"Error: Skill '{args.name}' not found", file=sys.stderr)
        return 1

    skill_md = skill_path / "SKILL.md"
    metadata = parse_frontmatter(skill_md.read_text())
    description = metadata.get("description", "")

    if not description:
        print(
            f"Error: Skill '{args.name}' has no description in frontmatter",
            file=sys.stderr,
        )
        return 1

    if args.generate:
        cases = generate_cases(description, args.count)
        sys.stdout.write(emit_yaml(cases))
        return 0

    if not args.cases:
        print(
            "Error: --cases is required unless --generate is used",
            file=sys.stderr,
        )
        return 1

    cases_path = Path(args.cases)
    if not cases_path.exists():
        print(f"Error: Cases file '{cases_path}' does not exist", file=sys.stderr)
        return 1

    try:
        cases = load_cases(cases_path)
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"Error loading cases: {exc}", file=sys.stderr)
        return 1

    if not cases:
        print("Error: No cases loaded", file=sys.stderr)
        return 1

    report = run_cases(description, cases, args.judge)

    if args.format == "json":
        out = {
            "skill": args.name,
            "description": description,
            **report,
        }
        print(json.dumps(out, indent=2))
    else:
        print(format_text(args.name, description, report))

    return 0 if report["metrics"]["f1"] >= args.threshold else 1


if __name__ == "__main__":
    sys.exit(main())
