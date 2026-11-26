#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Prepare a Claude Code plugin for submission to the Anthropic Plugin Directory."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import webbrowser
from pathlib import Path

PLUGIN_DOCS_URL = "https://code.claude.com/docs/en/plugins"
MARKETPLACE_DOCS_URL = "https://code.claude.com/docs/en/plugin-marketplaces"
REFERENCE_DOCS_URL = "https://code.claude.com/docs/en/plugins-reference"


def run_command(cmd: list[str], cwd: str | None = None) -> tuple[bool, str]:
    """Run a shell command and return (success, stdout)."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, timeout=30)
        return result.returncode == 0, result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        return False, str(e)


def get_git_info(plugin_path: str) -> dict:
    """Get git repository information using git and gh CLI."""
    git_info: dict = {
        "repo_url": None,
        "full_sha": None,
        "branch": None,
        "is_clean": False,
        "has_remote": False,
        "errors": [],
    }

    success, _ = run_command(["git", "rev-parse", "--git-dir"], cwd=plugin_path)
    if not success:
        git_info["errors"].append("Not a git repository")
        return git_info

    success, sha = run_command(["git", "rev-parse", "HEAD"], cwd=plugin_path)
    if success:
        git_info["full_sha"] = sha
    else:
        git_info["errors"].append("Could not get commit SHA")

    success, branch = run_command(["git", "branch", "--show-current"], cwd=plugin_path)
    if success:
        git_info["branch"] = branch

    success, status = run_command(["git", "status", "--porcelain"], cwd=plugin_path)
    if success:
        git_info["is_clean"] = len(status) == 0

    success, repo_url = run_command(["gh", "repo", "view", "--json", "url", "-q", ".url"], cwd=plugin_path)
    if success and repo_url:
        git_info["repo_url"] = repo_url
        git_info["has_remote"] = True
    else:
        success, remote_url = run_command(["git", "remote", "get-url", "origin"], cwd=plugin_path)
        if success and remote_url:
            if remote_url.startswith("git@github.com:"):
                remote_url = remote_url.replace("git@github.com:", "https://github.com/")
            if remote_url.endswith(".git"):
                remote_url = remote_url[:-4]
            git_info["repo_url"] = remote_url
            git_info["has_remote"] = True
        else:
            git_info["errors"].append("No remote repository found. Push to GitHub first.")

    return git_info


def gather_plugin_info(plugin_path: str, email: str | None = None, company_url: str | None = None) -> dict:
    """Gather all information needed for plugin submission."""
    plugin_dir = Path(plugin_path).resolve()
    info: dict = {
        "plugin_path": str(plugin_dir),
        "validation": {"passed": True, "issues": [], "warnings": []},
        "metadata": {},
        "git": get_git_info(str(plugin_dir)),
        "components": {},
        "form_fields": {},
    }

    plugin_json_path = plugin_dir / ".claude-plugin" / "plugin.json"
    if not plugin_json_path.exists():
        info["validation"]["passed"] = False
        info["validation"]["issues"].append("Missing .claude-plugin/plugin.json")
        info["form_fields"] = {
            "link_to_plugin": info["git"].get("repo_url", ""),
            "full_sha": info["git"].get("full_sha", ""),
            "plugin_homepage": "",
            "company_url": company_url or "",
            "primary_contact_email": email or "",
            "plugin_name": "",
            "plugin_description": "",
        }
        return info

    try:
        plugin_data = json.loads(plugin_json_path.read_text(encoding="utf-8-sig"))
        info["metadata"] = plugin_data
    except json.JSONDecodeError as e:
        info["validation"]["passed"] = False
        info["validation"]["issues"].append(f"Invalid plugin.json: {e}")
        return info

    for field in ("name", "description", "version", "author"):
        if field not in plugin_data:
            info["validation"]["passed"] = False
            info["validation"]["issues"].append(f"Missing required field: {field}")

    description = plugin_data.get("description", "")
    if "TODO" in description:
        info["validation"]["passed"] = False
        info["validation"]["issues"].append("Description contains TODO placeholder")

    word_count = len(description.split())
    if word_count < 50 or word_count > 100:
        info["validation"]["warnings"].append(f"Description is {word_count} words (50-100 recommended)")

    components = info["components"]
    if (plugin_dir / "commands").exists():
        components["commands"] = [c.stem for c in (plugin_dir / "commands").glob("*.md")]
    if (plugin_dir / "agents").exists():
        components["agents"] = [a.stem for a in (plugin_dir / "agents").glob("*.md")]
    if (plugin_dir / "skills").exists():
        components["skills"] = [d.name for d in (plugin_dir / "skills").iterdir() if d.is_dir()]
    if (plugin_dir / "hooks" / "hooks.json").exists():
        components["hooks"] = True
    mcp_json = plugin_dir / ".mcp.json"
    if mcp_json.exists():
        try:
            mcp_data = json.loads(mcp_json.read_text(encoding="utf-8-sig"))
            components["mcp_servers"] = list(mcp_data.get("mcpServers", {}).keys())
        except json.JSONDecodeError:
            pass

    readme = plugin_dir / "README.md"
    if not readme.exists():
        info["validation"]["passed"] = False
        info["validation"]["issues"].append("Missing README.md")
    elif "TODO" in readme.read_text(encoding="utf-8"):
        info["validation"]["warnings"].append("README.md contains TODO placeholders")

    if not (plugin_dir / "LICENSE").exists():
        info["validation"]["warnings"].append("Missing LICENSE file (recommended)")

    if not info["git"]["has_remote"]:
        info["validation"]["passed"] = False
        info["validation"]["issues"].append("Plugin must be pushed to GitHub before submission")

    if not info["git"]["is_clean"]:
        info["validation"]["warnings"].append("Working directory has uncommitted changes")

    info["form_fields"] = {
        "link_to_plugin": info["git"].get("repo_url", ""),
        "full_sha": info["git"].get("full_sha", ""),
        "plugin_homepage": plugin_data.get("homepage", "") or info["git"].get("repo_url", ""),
        "company_url": company_url or "",
        "primary_contact_email": email or plugin_data.get("author", {}).get("email", ""),
        "plugin_name": plugin_data.get("name", ""),
        "plugin_description": description,
    }

    for key, msg in (
        ("link_to_plugin", "Link to Plugin is required"),
        ("full_sha", "Full SHA is required"),
        ("plugin_homepage", "Plugin Homepage is required"),
    ):
        if not info["form_fields"][key]:
            info["validation"]["issues"].append(msg)

    if not info["form_fields"]["company_url"]:
        info["validation"]["warnings"].append("Company/Organization URL not provided (use --company-url)")
    if not info["form_fields"]["primary_contact_email"]:
        info["validation"]["warnings"].append("Primary Contact Email not provided (use --email)")

    return info


def print_form_fields(info: dict) -> None:
    """Print form fields in a copy-paste friendly format."""
    fields = info["form_fields"]
    validation = info["validation"]
    git = info["git"]

    print("\n" + "=" * 70)
    print("ANTHROPIC PLUGIN SUBMISSION DATA")
    print("=" * 70)
    print(f"Docs: {PLUGIN_DOCS_URL}")

    if validation["passed"]:
        print("\nValidation: PASSED")
    else:
        print("\nValidation: FAILED")
        for issue in validation["issues"]:
            print(f"  - ERROR: {issue}")

    for warning in validation["warnings"]:
        print(f"  - WARN: {warning}")

    print(f"\nRepository: branch={git.get('branch', 'N/A')} clean={git.get('is_clean')}")
    for label, key in (
        ("Link to Plugin", "link_to_plugin"),
        ("Full SHA", "full_sha"),
        ("Plugin Homepage", "plugin_homepage"),
        ("Company URL", "company_url"),
        ("Primary Contact Email", "primary_contact_email"),
        ("Plugin Name", "plugin_name"),
        ("Plugin Description", "plugin_description"),
    ):
        print(f"  {label}: {fields.get(key) or '[missing]'}")


def copy_to_clipboard(text: str) -> bool:
    """Try to copy text to system clipboard."""
    for cmd in (["pbcopy"], ["xclip", "-selection", "clipboard"]):
        try:
            proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
            proc.communicate(text.encode("utf-8"))
            if proc.returncode == 0:
                return True
        except FileNotFoundError:
            continue
    return False


def generate_submission_json(info: dict) -> str:
    """Generate JSON string with submission metadata."""
    return json.dumps(
        {
            "form_fields": info["form_fields"],
            "validation": info["validation"],
            "git": info["git"],
            "components": info["components"],
            "metadata": info["metadata"],
        },
        indent=2,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare a Claude Code plugin for directory submission")
    parser.add_argument("plugin_path", help="Path to the plugin directory")
    parser.add_argument("--email", "-e", help="Primary contact email")
    parser.add_argument("--company-url", "-c", help="Company or organization URL")
    parser.add_argument("--output", "-o", help="Save submission data to JSON file")
    parser.add_argument("--json", action="store_true", help="Output JSON to stdout")
    parser.add_argument("--form-url", help="Override submission form URL to open")
    parser.add_argument("--open-form", action="store_true", help="Open form/docs URL in browser")
    parser.add_argument("--copy-sha", action="store_true", help="Copy full commit SHA to clipboard")

    args = parser.parse_args()
    info = gather_plugin_info(args.plugin_path, email=args.email, company_url=args.company_url)

    if args.json:
        print(generate_submission_json(info))
    else:
        print_form_fields(info)
        if args.output:
            Path(args.output).write_text(generate_submission_json(info) + "\n", encoding="utf-8")
            print(f"\nSaved submission JSON to: {args.output}")
        if args.copy_sha and info["git"].get("full_sha"):
            if copy_to_clipboard(info["git"]["full_sha"]):
                print("\nFull SHA copied to clipboard.")

    if args.open_form:
        target_url = args.form_url or PLUGIN_DOCS_URL
        print(f"\nOpening: {target_url}")
        webbrowser.open(target_url)

    if not info["validation"]["passed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
