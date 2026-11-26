#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Initialize a new Claude Code plugin marketplace repository."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


def create_marketplace_json(name: str, owner_name: str = "Your Name") -> dict:
    """Create the marketplace.json manifest."""
    return {
        "name": name,
        "owner": {"name": owner_name},
        "metadata": {
            "description": f"TODO: Add description for {name} marketplace",
            "version": "1.0.0",
        },
        "plugins": [],
    }


def create_marketplace_readme(name: str) -> str:
    """Create README.md content for marketplace."""
    return f"""# {name.replace('-', ' ').title()} Marketplace

A coding-agent plugin marketplace.

## Installation

```bash
/plugin marketplace add <github-username>/{name}
```

## Available Plugins

| Plugin | Description | Version |
|--------|-------------|---------|
| TODO | Add plugins | 1.0.0 |

## License

MIT License
"""


def add_plugin_to_marketplace(marketplace_json: dict, plugin_name: str, plugin_path: str) -> dict:
    """Add a plugin entry to marketplace.json."""
    marketplace_json["plugins"].append(
        {
            "name": plugin_name,
            "source": plugin_path,
            "description": f"TODO: Add description for {plugin_name}",
            "version": "1.0.0",
        }
    )
    return marketplace_json


def init_marketplace(
    name: str,
    output_path: str,
    owner_name: str = "Your Name",
    initial_plugins: list[str] | None = None,
) -> Path:
    """Initialize a new marketplace directory structure."""
    marketplace_dir = Path(output_path) / name
    if marketplace_dir.exists():
        raise FileExistsError(f"Directory already exists: {marketplace_dir}")

    marketplace_dir.mkdir(parents=True)
    claude_plugin_dir = marketplace_dir / ".claude-plugin"
    claude_plugin_dir.mkdir()

    marketplace_json = create_marketplace_json(name, owner_name)

    if initial_plugins:
        for plugin_name in initial_plugins:
            plugin_path = f"./plugins/{plugin_name}"
            add_plugin_to_marketplace(marketplace_json, plugin_name, plugin_path)
            plugin_dir = marketplace_dir / "plugins" / plugin_name
            (plugin_dir / ".claude-plugin").mkdir(parents=True)
            (plugin_dir / ".claude-plugin" / "plugin.json").write_text(
                json.dumps(
                    {
                        "name": plugin_name,
                        "description": f"TODO: Add description for {plugin_name}",
                        "version": "1.0.0",
                        "author": {"name": owner_name},
                    },
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
            (plugin_dir / "README.md").write_text(
                f"# {plugin_name}\n\nTODO: Add documentation\n", encoding="utf-8"
            )

    (claude_plugin_dir / "marketplace.json").write_text(
        json.dumps(marketplace_json, indent=2) + "\n", encoding="utf-8"
    )

    plugins_dir = marketplace_dir / "plugins"
    if not plugins_dir.exists():
        plugins_dir.mkdir()
        (plugins_dir / ".gitkeep").write_text("", encoding="utf-8")

    (marketplace_dir / "README.md").write_text(create_marketplace_readme(name), encoding="utf-8")
    (marketplace_dir / "LICENSE").write_text(
        "MIT License\n\nCopyright (c) 2026\n\nTODO: Add full license text\n", encoding="utf-8"
    )

    return marketplace_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Initialize a new plugin marketplace")
    parser.add_argument("marketplace_name", help="Name of the marketplace (kebab-case)")
    parser.add_argument("--path", "-p", default=".", help="Output directory (default: current directory)")
    parser.add_argument("--owner", "-o", default="Your Name", help="Owner name for marketplace.json")
    parser.add_argument(
        "--with-plugin",
        action="append",
        dest="plugins",
        help="Create marketplace with initial plugin(s) (repeatable)",
    )

    args = parser.parse_args()

    try:
        marketplace_dir = init_marketplace(
            name=args.marketplace_name,
            output_path=args.path,
            owner_name=args.owner,
            initial_plugins=args.plugins,
        )
    except FileExistsError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Initialized marketplace '{args.marketplace_name}' at: {marketplace_dir}")
    for root, _, files in os.walk(marketplace_dir):
        rel = Path(root).relative_to(marketplace_dir)
        indent = "  " * (0 if rel == Path(".") else len(rel.parts))
        label = marketplace_dir.name if rel == Path(".") else rel.name
        print(f"{indent}{label}/")
        for fname in sorted(files):
            print(f"{indent}  {fname}")


if __name__ == "__main__":
    main()
