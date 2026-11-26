#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Initialize a new Claude Code or Antigravity plugin with modern defaults."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from _jsonc import is_kebab_case


def create_claude_plugin_json(plugin_name: str, author_name: str = "Your Name") -> dict:
    """Create a Claude Code plugin.json manifest."""
    return {
        "name": plugin_name,
        "description": f"TODO: Add description for {plugin_name}",
        "version": "1.0.0",
        "author": {"name": author_name},
        "keywords": [],
    }


def create_antigravity_plugin_json(plugin_name: str, author_name: str = "Your Name") -> dict:
    """Create an Antigravity native plugin.json manifest."""
    return {
        "$schema": "https://antigravity.dev/schemas/plugin.json",
        "name": plugin_name,
        "displayName": plugin_name.replace("-", " ").title(),
        "version": "1.0.0",
        "description": f"TODO: Add description for {plugin_name}",
        "author": {"name": author_name},
        "category": "Developer Tools",
        "suggestedPrompts": [f"Run {plugin_name} workflow"],
        "skills": "skills/",
        "disabled": False,
    }


def create_readme(plugin_name: str, agent: str) -> str:
    """Create README.md content."""
    install_block = (
        f"```bash\n/plugin marketplace add <marketplace-source>\n/plugin install {plugin_name}@<marketplace>\n```"
        if agent == "claude-code"
        else f"```bash\nagy plugin install ./{plugin_name}\nagy plugin validate ./{plugin_name} --strict\n```"
    )
    return f"""# {plugin_name.replace('-', ' ').title()}

## Description

TODO: Describe what this plugin does.

## Installation

{install_block}

## Usage

TODO: Describe how to use the plugin.

## License

MIT License
"""


def create_command_template(command_name: str) -> str:
    """Create a legacy slash command markdown file."""
    return f"""---
description: TODO: Describe what /{command_name} does
---

# {command_name.replace('-', ' ').title()} Command

TODO: Add instructions for when this command is invoked.
"""


def create_agent_template(agent_name: str) -> str:
    """Create an agent markdown file."""
    return f"""---
description: TODO: Describe this agent's specialty
---

# {agent_name.replace('-', ' ').title()} Agent

TODO: Add detailed instructions and expertise for this agent.
"""


def create_skill_template(skill_name: str) -> str:
    """Create a starter SKILL.md file."""
    return f"""---
name: {skill_name}
description: TODO: What this skill does and when to trigger it. Do not use for unrelated tasks.
---

# {skill_name.replace('-', ' ').title()}

## Workflow

TODO: Describe how the agent executes this skill.
"""


def create_claude_hooks_json() -> dict:
    """Create Claude Code hooks/hooks.json template."""
    return {
        "hooks": {
            "PostToolUse": [
                {
                    "matcher": "Write|Edit",
                    "hooks": [
                        {
                            "type": "command",
                            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh",
                            "timeout": 10,
                        }
                    ],
                }
            ]
        }
    }


def create_antigravity_hooks_json() -> dict:
    """Create Antigravity root hooks.json template (named-hook map)."""
    return {
        "validate-edits": {
            "enabled": True,
            "PostToolUse": [
                {
                    "matcher": "write_to_file|edit_file",
                    "hooks": [
                        {
                            "type": "command",
                            "command": "./scripts/validate.sh",
                            "timeout": 10,
                        }
                    ],
                }
            ],
        }
    }


def create_claude_mcp_json() -> dict:
    """Create Claude Code .mcp.json template."""
    return {
        "mcpServers": {
            "example-server": {
                "command": "node",
                "args": ["${CLAUDE_PLUGIN_ROOT}/servers/server.js"],
                "env": {},
            }
        }
    }


def create_antigravity_mcp_json() -> dict:
    """Create Antigravity mcp_config.json template."""
    return {
        "mcpServers": {
            "example-server": {
                "command": "node",
                "args": ["./servers/server.js"],
                "variables": {
                    "API_TOKEN": {
                        "description": "API token for example-server",
                        "required": False,
                    }
                },
            }
        }
    }


def init_plugin(
    plugin_name: str,
    output_path: str,
    agent: str = "claude-code",
    with_commands: bool = False,
    with_agents: bool = False,
    with_skills: bool = True,
    with_hooks: bool = False,
    with_mcp: bool = False,
    with_rules: bool = False,
    author_name: str = "Your Name",
) -> Path:
    """Initialize a new plugin directory structure."""
    if not is_kebab_case(plugin_name):
        raise ValueError(
            f"Invalid plugin name '{plugin_name}'. Use lowercase kebab-case (e.g., 'my-plugin')."
        )

    plugin_dir = Path(output_path) / plugin_name
    if plugin_dir.exists():
        raise FileExistsError(f"Directory already exists: {plugin_dir}")

    plugin_dir.mkdir(parents=True)

    if agent == "antigravity":
        manifest = create_antigravity_plugin_json(plugin_name, author_name)
        (plugin_dir / "plugin.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    else:
        claude_plugin_dir = plugin_dir / ".claude-plugin"
        claude_plugin_dir.mkdir()
        manifest = create_claude_plugin_json(plugin_name, author_name)
        (claude_plugin_dir / "plugin.json").write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
        )

    (plugin_dir / "README.md").write_text(create_readme(plugin_name, agent), encoding="utf-8")
    (plugin_dir / "LICENSE").write_text(
        "MIT License\n\nCopyright (c) 2026\n\nTODO: Add full license text\n", encoding="utf-8"
    )

    if with_skills:
        skill_dir = plugin_dir / "skills" / "example-skill"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(create_skill_template("example-skill"), encoding="utf-8")

    if with_commands:
        commands_dir = plugin_dir / "commands"
        commands_dir.mkdir()
        (commands_dir / "example.md").write_text(create_command_template("example"), encoding="utf-8")

    if with_agents:
        agents_dir = plugin_dir / "agents"
        agents_dir.mkdir()
        (agents_dir / "example-agent.md").write_text(create_agent_template("example-agent"), encoding="utf-8")

    if with_hooks:
        if agent == "antigravity":
            (plugin_dir / "hooks.json").write_text(
                json.dumps(create_antigravity_hooks_json(), indent=2) + "\n", encoding="utf-8"
            )
        else:
            hooks_dir = plugin_dir / "hooks"
            hooks_dir.mkdir()
            (hooks_dir / "hooks.json").write_text(
                json.dumps(create_claude_hooks_json(), indent=2) + "\n", encoding="utf-8"
            )

    if with_mcp:
        mcp_filename = "mcp_config.json" if agent == "antigravity" else ".mcp.json"
        mcp_payload = create_antigravity_mcp_json() if agent == "antigravity" else create_claude_mcp_json()
        (plugin_dir / mcp_filename).write_text(json.dumps(mcp_payload, indent=2) + "\n", encoding="utf-8")
        servers_dir = plugin_dir / "servers"
        servers_dir.mkdir()
        (servers_dir / ".gitkeep").write_text("", encoding="utf-8")

    if with_rules or agent == "antigravity":
        rules_dir = plugin_dir / "rules"
        rules_dir.mkdir(exist_ok=True)
        (rules_dir / "AGENTS.md").write_text(
            f"# {plugin_name}\n\nKeep instructions concise (under 24 KB).\n", encoding="utf-8"
        )

    return plugin_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a Claude Code or Antigravity plugin")
    parser.add_argument("plugin_name", help="Name of the plugin (lowercase kebab-case)")
    parser.add_argument("--path", "-p", default=".", help="Output directory (default: current directory)")
    parser.add_argument(
        "--agent",
        choices=("claude-code", "antigravity"),
        default="claude-code",
        help="Target agent plugin format (default: claude-code)",
    )
    parser.add_argument("--author", "-a", default="Your Name", help="Author name for plugin.json")
    parser.add_argument(
        "--with-skills",
        action="store_true",
        default=True,
        help="Include starter skills/<name>/SKILL.md directory (default: True)",
    )
    parser.add_argument("--no-skills", action="store_true", help="Exclude starter skills directory")
    parser.add_argument("--with-commands", action="store_true", help="Include legacy commands/ directory")
    parser.add_argument("--with-agents", action="store_true", help="Include agents/ directory")
    parser.add_argument("--with-hooks", action="store_true", help="Include hooks configuration")
    parser.add_argument("--with-mcp", action="store_true", help="Include MCP server configuration")
    parser.add_argument("--with-rules", action="store_true", help="Include rules/AGENTS.md")
    parser.add_argument("--all", action="store_true", help="Include skills, agents, hooks, MCP, and rules")

    args = parser.parse_args()

    with_skills = False if args.no_skills else (args.with_skills or args.all)
    with_commands = args.with_commands
    with_agents = args.with_agents or args.all
    with_hooks = args.with_hooks or args.all
    with_mcp = args.with_mcp or args.all
    with_rules = args.with_rules or args.all

    try:
        plugin_dir = init_plugin(
            plugin_name=args.plugin_name,
            output_path=args.path,
            agent=args.agent,
            with_commands=with_commands,
            with_agents=with_agents,
            with_skills=with_skills,
            with_hooks=with_hooks,
            with_mcp=with_mcp,
            with_rules=with_rules,
            author_name=args.author,
        )
    except (ValueError, FileExistsError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Initialized {args.agent} plugin '{args.plugin_name}' at: {plugin_dir}")
    for root, _, files in os.walk(plugin_dir):
        rel = Path(root).relative_to(plugin_dir)
        indent = "  " * (0 if rel == Path(".") else len(rel.parts))
        label = plugin_dir.name if rel == Path(".") else rel.name
        print(f"{indent}{label}/")
        for fname in sorted(files):
            print(f"{indent}  {fname}")

    validate_hint = (
        f"agy plugin validate {plugin_dir} --strict"
        if args.agent == "antigravity"
        else f"uv run scripts/validate_plugin.py {plugin_dir}"
    )
    print(f"\nNext: run `{validate_hint}` after editing placeholders.")


if __name__ == "__main__":
    main()
