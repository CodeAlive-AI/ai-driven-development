#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Validate a Claude Code or Antigravity plugin structure and manifest."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from _jsonc import is_kebab_case, load_jsonc
from validate_hooks import validate_antigravity_hooks_config, validate_claude_hooks_config

AGY_KNOWN_MANIFEST_FIELDS = {
    "$schema",
    "name",
    "displayName",
    "version",
    "description",
    "logo",
    "suggestedPrompts",
    "author",
    "homepage",
    "repository",
    "category",
    "disabled",
    "skills",
    "extensions",
}


class ValidationResult:
    """Accumulator for validation errors, warnings, and info messages."""

    def __init__(self, agent: str = "claude-code") -> None:
        self.agent = agent
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.info: list[str] = []

    def add_error(self, msg: str) -> None:
        self.errors.append(msg)

    def add_warning(self, msg: str) -> None:
        self.warnings.append(msg)

    def add_info(self, msg: str) -> None:
        self.info.append(msg)

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "valid": self.is_valid,
            "agent": self.agent,
            "errors": self.errors,
            "warnings": self.warnings,
            "info": self.info,
        }

    def print_report(self, quiet: bool = False) -> None:
        if not quiet and self.info:
            print("\nInfo:")
            for msg in self.info:
                print(f"  - {msg}")
        if not quiet and self.warnings:
            print("\nWarnings:")
            for msg in self.warnings:
                print(f"  - {msg}")
        if self.errors:
            print("\nErrors:")
            for msg in self.errors:
                print(f"  - {msg}")
        if not quiet or not self.is_valid:
            state = "VALID" if self.is_valid else f"INVALID ({len(self.errors)} error(s))"
            print(f"\nResult ({self.agent}): {state}")


def validate_version(version: str) -> tuple[bool, str]:
    """Validate semantic version format."""
    if not re.match(r"^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?(\+[a-zA-Z0-9.]+)?$", version):
        return False, f"Version '{version}' should follow semver (e.g., '1.0.0')"
    return True, ""


def _validate_skills_dir(skills_dir: Path, result: ValidationResult, required_present: bool = False) -> None:
    if not skills_dir.exists():
        if required_present:
            result.add_error(f"Configured skills path does not exist: {skills_dir}")
        return
    if (skills_dir / "SKILL.md").exists():
        result.add_info(f"Found skill: {skills_dir.name}")
        return
    skill_dirs = [d for d in skills_dir.iterdir() if d.is_dir()]
    if not skill_dirs:
        result.add_warning(f"{skills_dir.name}/ directory exists but contains no skill subdirectories")
        return
    result.add_info(f"Found {len(skill_dirs)} skill(s) in {skills_dir.name}/")
    for sdir in skill_dirs:
        if not (sdir / "SKILL.md").exists():
            result.add_error(f"Skill '{sdir.name}' missing SKILL.md")


def _validate_mcp_servers_map(mcp_data: Any, filename: str, result: ValidationResult, is_agy: bool = False) -> None:
    if not isinstance(mcp_data, dict) or "mcpServers" not in mcp_data:
        result.add_error(f"{filename} missing 'mcpServers' object")
        return
    servers = mcp_data["mcpServers"]
    if not isinstance(servers, dict):
        result.add_error(f"{filename} 'mcpServers' must be an object")
        return
    result.add_info(f"Found {len(servers)} MCP server(s) in {filename}")
    for name, cfg in servers.items():
        if not isinstance(cfg, dict):
            result.add_error(f"MCP server '{name}' in {filename} must be an object")
            continue
        transport = cfg.get("type") or cfg.get("transport")
        has_stdio = isinstance(cfg.get("command"), str) and bool(cfg["command"].strip())
        url_val = cfg.get("serverUrl") if is_agy and "serverUrl" in cfg else cfg.get("url")
        if is_agy and not url_val:
            url_val = cfg.get("url")
        has_http = isinstance(url_val, str) and bool(url_val.strip())

        if transport == "sse" or (isinstance(url_val, str) and url_val.rstrip("/").endswith("/sse")):
            result.add_warning(
                f"MCP server '{name}' uses legacy SSE endpoint/transport; prefer Streamable HTTP or mcp-remote bridge"
            )
        if not has_stdio and not has_http:
            result.add_error(f"MCP server '{name}' in {filename} requires 'command' (stdio) or 'url'/'serverUrl' (HTTP)")

        if is_agy and has_stdio and "env" in cfg and "variables" not in cfg:
            raw_env = json.dumps(cfg["env"])
            if "${" in raw_env:
                result.add_warning(
                    f"Antigravity plugin MCP server '{name}' uses ${{...}} without declaring 'variables'; host env vars do not auto-expand"
                )


def _validate_claude_plugin(plugin_dir: Path, result: ValidationResult) -> None:
    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        result.add_error("Missing .claude-plugin/plugin.json")
    else:
        try:
            data = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
        except json.JSONDecodeError as exc:
            result.add_error(f"Invalid JSON in .claude-plugin/plugin.json: {exc}")
            data = None
        if isinstance(data, dict):
            for field in ("name", "description", "version", "author"):
                if field not in data:
                    result.add_error(f"Missing required field '{field}' in plugin.json")
            if "name" in data and not is_kebab_case(str(data["name"])):
                result.add_error(f"Plugin name '{data['name']}' must be lowercase kebab-case")
            if "version" in data:
                ok, msg = validate_version(str(data["version"]))
                if not ok:
                    result.add_error(msg)
            if "author" in data and (not isinstance(data["author"], dict) or "name" not in data["author"]):
                result.add_error("'author' must be an object containing 'name'")
            if "keywords" in data and not isinstance(data["keywords"], list):
                result.add_error("'keywords' must be an array")
            desc = str(data.get("description", ""))
            if desc and (len(desc) < 10 or "TODO" in desc):
                result.add_warning("plugin.json description is incomplete or short")
            result.add_info(f"Plugin: {data.get('name', 'unknown')} v{data.get('version', 'unknown')}")

    commands_dir = plugin_dir / "commands"
    if commands_dir.exists():
        md_files = list(commands_dir.glob("*.md"))
        if not md_files:
            result.add_warning("commands/ directory exists but contains no .md files")
        else:
            result.add_info(f"Found {len(md_files)} legacy command(s)")

    agents_dir = plugin_dir / "agents"
    if agents_dir.exists():
        md_files = list(agents_dir.glob("*.md"))
        if not md_files:
            result.add_warning("agents/ directory exists but contains no .md files")

    _validate_skills_dir(plugin_dir / "skills", result)

    hooks_json = plugin_dir / "hooks" / "hooks.json"
    if hooks_json.exists():
        try:
            hdata = load_jsonc(hooks_json)
            if not isinstance(hdata, dict):
                result.add_error("hooks/hooks.json must be a JSON object")
            else:
                errs, warns = validate_claude_hooks_config(hdata)
                for e in errs:
                    result.add_error(f"hooks/hooks.json: {e}")
                for w in warns:
                    result.add_warning(f"hooks/hooks.json: {w}")
        except Exception as exc:
            result.add_error(f"Invalid hooks/hooks.json: {exc}")

    mcp_json = plugin_dir / ".mcp.json"
    if mcp_json.exists():
        try:
            _validate_mcp_servers_map(load_jsonc(mcp_json), ".mcp.json", result, is_agy=False)
        except Exception as exc:
            result.add_error(f"Invalid .mcp.json: {exc}")

    readme = plugin_dir / "README.md"
    if not readme.exists():
        result.add_error("Missing README.md")
    elif len(readme.read_text(encoding="utf-8")) < 50 or "TODO" in readme.read_text(encoding="utf-8"):
        result.add_warning("README.md is brief or contains TODO placeholders")

    if not (plugin_dir / "LICENSE").exists():
        result.add_warning("Missing LICENSE file (recommended)")


def _validate_antigravity_plugin(plugin_dir: Path, result: ValidationResult) -> None:
    manifest_path = plugin_dir / "plugin.json"
    if not manifest_path.exists():
        result.add_error("Missing root plugin.json")
        return

    try:
        data = load_jsonc(manifest_path)
    except Exception as exc:
        result.add_error(f"Invalid JSON/JSONC in plugin.json: {exc}")
        return

    if not isinstance(data, dict):
        result.add_error("plugin.json root must be a JSON object")
        return

    for field in ("name", "description"):
        if field not in data:
            result.add_error(f"Missing required field '{field}' in plugin.json")

    if "name" in data and not is_kebab_case(str(data["name"])):
        result.add_error(f"Plugin name '{data['name']}' must be lowercase kebab-case")

    if "version" in data:
        ok, msg = validate_version(str(data["version"]))
        if not ok:
            result.add_error(msg)

    unknown = sorted(set(data.keys()) - AGY_KNOWN_MANIFEST_FIELDS)
    if unknown:
        result.add_warning(
            f"Unknown top-level plugin.json field(s) silently discarded by Antigravity: {', '.join(unknown)}"
        )

    prompts = data.get("suggestedPrompts")
    if prompts is not None:
        if not isinstance(prompts, list) or not all(isinstance(p, str) for p in prompts):
            result.add_error("'suggestedPrompts' must be an array of strings")
        elif len(prompts) > 3:
            result.add_warning(f"'suggestedPrompts' has {len(prompts)} entries (Antigravity UI caps at 3)")

    skills_spec = data.get("skills")
    if skills_spec is None:
        _validate_skills_dir(plugin_dir / "skills", result)
    else:
        specs = [skills_spec] if isinstance(skills_spec, str) else skills_spec if isinstance(skills_spec, list) else []
        if not specs and skills_spec != []:
            result.add_error("'skills' in plugin.json must be a string or array of strings")
        for rel in specs:
            if not isinstance(rel, str):
                result.add_error("'skills' entries must be strings")
                continue
            target = (plugin_dir / rel).resolve()
            try:
                target.relative_to(plugin_dir.resolve())
            except ValueError:
                result.add_error(f"skills path escapes plugin directory: {rel}")
                continue
            _validate_skills_dir(target, result, required_present=True)

    # Native Antigravity plugins load root hooks.json, NOT hooks/hooks.json
    if (plugin_dir / "hooks" / "hooks.json").exists():
        result.add_error(
            "Found hooks/hooks.json; native Antigravity plugins require hooks.json at the plugin root"
        )

    root_hooks = plugin_dir / "hooks.json"
    if root_hooks.exists():
        try:
            hdata = load_jsonc(root_hooks)
            if not isinstance(hdata, dict):
                result.add_error("hooks.json root must be a JSON object")
            else:
                errs, warns = validate_antigravity_hooks_config(hdata, root_hooks)
                for e in errs:
                    result.add_error(f"hooks.json: {e}")
                for w in warns:
                    result.add_warning(f"hooks.json: {w}")
        except Exception as exc:
            result.add_error(f"Invalid hooks.json: {exc}")

    mcp_config = plugin_dir / "mcp_config.json"
    if mcp_config.exists():
        try:
            _validate_mcp_servers_map(load_jsonc(mcp_config), "mcp_config.json", result, is_agy=True)
        except Exception as exc:
            result.add_error(f"Invalid mcp_config.json: {exc}")

    if not (plugin_dir / "README.md").exists():
        result.add_warning("Missing README.md (recommended)")


def detect_plugin_agent(plugin_dir: Path) -> str:
    """Detect plugin target format ('claude-code' or 'antigravity')."""
    if (plugin_dir / ".claude-plugin" / "plugin.json").exists():
        return "claude-code"
    if (plugin_dir / "plugin.json").exists():
        return "antigravity"
    return "claude-code"


def validate_plugin(plugin_path: str, agent: str = "auto") -> ValidationResult:
    """Validate a plugin directory against Claude Code or Antigravity layout."""
    plugin_dir = Path(plugin_path).resolve()
    resolved_agent = detect_plugin_agent(plugin_dir) if agent == "auto" else agent
    result = ValidationResult(agent=resolved_agent)

    if not plugin_dir.exists():
        result.add_error(f"Plugin directory does not exist: {plugin_dir}")
        return result
    if not plugin_dir.is_dir():
        result.add_error(f"Path is not a directory: {plugin_dir}")
        return result

    if resolved_agent == "antigravity":
        _validate_antigravity_plugin(plugin_dir, result)
    else:
        _validate_claude_plugin(plugin_dir, result)

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a Claude Code or Antigravity plugin")
    parser.add_argument("plugin_path", help="Path to plugin root directory")
    parser.add_argument(
        "--agent",
        choices=("auto", "claude-code", "antigravity"),
        default="auto",
        help="Target plugin specification (default: auto)",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format (default: text)",
    )
    parser.add_argument("--quiet", "-q", action="store_true", help="Only show errors")
    args = parser.parse_args()

    result = validate_plugin(args.plugin_path, agent=args.agent)

    if args.format == "json":
        print(json.dumps(result.to_dict(), indent=2))
    else:
        result.print_report(quiet=args.quiet)

    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
