# Antigravity (AGY) Skills & Plugins Reference

Guide to how Google Antigravity discovers, loads, validates, and manages skills and plugins across **Antigravity App (2.0 desktop)**, **Antigravity IDE**, and **Antigravity CLI (`agy`)**.

## Contents

- [Surfaces and Shared Storage](#surfaces-and-shared-storage)
- [Discovery Roots and Precedence](#discovery-roots-and-precedence)
- [SKILL.md Contract in Antigravity](#skillmd-contract-in-antigravity)
- [JSON Discovery Manifests (`skills.json`, `plugins.json`)](#json-discovery-manifests-skillsjson-pluginsjson)
- [Plugins Lifecycle (App, IDE, CLI)](#plugins-lifecycle-app-ide-cli)
- [Remote Agent Sessions](#remote-agent-sessions)
- [Headless `agy` for Testing and Optimization](#headless-agy-for-testing-and-optimization)
- [Live Documentation](#live-documentation)

## Surfaces and Shared Storage

All three Antigravity surfaces share the same customization model and global directory `~/.gemini/config/`:

| Surface | Config / State Notes | Plugin & Skill UI |
|---|---|---|
| **Antigravity App (2.0)** | Desktop Electron app; reads `~/.gemini/config/` + workspace `.agents/` | Left sidebar `Skills & Customizations`; `customization://<dir>` links and `<plugin-card>` |
| **Antigravity IDE** | VS Code-based editor; reads `~/.gemini/config/` + workspace `.agents/` | Customizations view + inline slash commands `/<name>` |
| **Antigravity CLI (`agy`)** | Terminal TUI/headless binary; CLI settings in `~/.gemini/antigravity-cli/settings.json`; shares `~/.gemini/config/` for skills, plugins, hooks, MCP | `/skills`, `/skills reload`, `/plugin`, `agy plugin <subcommand>` |

## Discovery Roots and Precedence

Antigravity discovers skills hierarchically and resolves name collisions from highest to lowest priority:

| Priority | Scope | Location | Notes |
|---|---|---|---|
| 1 | Workspace project | `<dir>/.agents/skills/<name>/SKILL.md` (and legacy `.agent/`, `_agents/`, `_agent/`) | Walks up from CWD to repository root (`.git`) |
| 2 | Declared configs (workspace) | `.agents/skills.json`, `.agents/plugins.json` (in any ancestor `.agents/` up to repo root) | Entries pointing outside workspace/repo root (absolute, `../`, outward symlinks) are skipped |
| 3 | Global discovery (primary) | `~/.gemini/config/skills/<name>/SKILL.md` | Canonical global write directory (`antigravity` & `antigravity-cli` in `scripts/agents.py`); `~/.gemini` wins on collisions with `~/.agents/skills` |
| 4 | Global discovery (cross-tool) | `~/.agents/skills/<name>/SKILL.md` | Supported by `agy` (1.5.16+) and shared across Codex/Cursor/OpenCode; appears in `/skills` and `/` autocomplete |
| 5 | Installed & workspace plugins | `~/.gemini/config/plugins/<dir>/skills/` and `<repo>/.agents/plugins/<dir>/skills/` | Active only when plugin is enabled; namespaced when needed |
| 6 | Built-in customizations | `~/.gemini/antigravity/builtin/skills/` and `/builtin/plugins/` | Bundled read-only layer mounted by agent config; never delete or edit |
| 7 | Global declared configs | `~/.gemini/config/skills.json`, `~/.gemini/config/plugins.json` | Supports `entries` and `inherits` with `include_only` / `exclude` |

Note: `~/.gemini/antigravity/skills` is the pre-2.0 global directory (on current installs typically a symlink to `~/.gemini/config/skills`). See `references/legacy/migrations.md` for older paths and deprecated workflows.

## SKILL.md Contract in Antigravity

Every skill is a folder under a `skills/` root containing `SKILL.md`:

```text
skills/<skill-name>/
├── SKILL.md          # Required: YAML frontmatter + instructions
├── scripts/          # Optional: helper scripts
├── references/       # Optional: deep docs linked from SKILL.md
├── examples/         # Optional: reference implementations
└── resources/        # Optional: templates or assets
```

- **Frontmatter requirements:** `name` (lowercase kebab-case matching the directory name) and non-empty `description` (what it does + when to trigger). Antigravity drops skills missing frontmatter or `name`.
- **Unquoted colons:** Current `agy` releases (1.3.6+) accept colons inside unquoted descriptions, though quoting or block scalars (`>-`) remain safer across tools.
- **Progressive disclosure:** Only `name` and `description` load into context at startup; the full `SKILL.md` body loads when the agent activates the skill or the user runs `/<skill-name>`.
- **Live reload:** Use `/skills reload` in `agy` after adding or editing skills mid-session.

## JSON Discovery Manifests (`skills.json`, `plugins.json`)

Use `skills.json` or `plugins.json` inside `.agents/` or `~/.gemini/config/` to register customizations in non-standard folders (scanned one level deep per entry):

```json
{
  "inherits": [
    {
      "path": "shared/skills.json",
      "include_only": ["linter-skill"],
      "exclude": ["deprecated-skill"]
    }
  ],
  "entries": [
    {
      "path": "tools/agents/skills",
      "exclude": ["experimental-.*"]
    }
  ]
}
```

- **Relative paths** resolve against the directory containing `.agents/` (falling back to repo root if absent there).
- **Security confinement (`agy 1.5.2+`):** Workspace `skills.json` and `plugins.json` load targets only inside the workspace or repository root; absolute paths, `~/`, `../` escapes, and outward symlinks are ignored.

## Plugins Lifecycle (App, IDE, CLI)

A plugin packages `skills/`, `agents/`, `rules/AGENTS.md`, `mcp_config.json`, root `hooks.json` (never `hooks/hooks.json` for native plugins), and optional `assets/logo.svg` alongside `plugin.json` (JSONC allowed; `name`, `displayName`, `version`, `description`, `logo`, `suggestedPrompts`, `author`, `homepage`, `repository`, `category`, `disabled`).

### CLI Commands (`agy plugin`)

```bash
agy plugin list --json                                # Inventory installed plugins (name, enabled, path, skills, ...)
agy plugin validate --strict <dir|zip|github-url>     # Validate manifest, skills, hooks, sidecars, logo, MCP configs
agy plugin install <path|plugin@marketplace>          # Install local or marketplace plugin
agy plugin import claude|gemini                       # Import Claude Code plugins or Gemini CLI extensions
agy plugin enable <dir-or-name>                       # Enable / disable / uninstall
agy plugin disable <dir-or-name>
agy plugin uninstall <dir-or-name>
```

Interactive TUI: run `/plugin` to browse shelves (`Discover`), configure MCP variables (`Configure MCP servers...`), sign in to OAuth providers, or toggle/uninstall bundles.

### Antigravity App (2.0) and Config Safety

- **Key links on `<dir>`, not `name`:** In App UI responses, always link to `[<name>](customization://<dir>)` using the install directory name (`.path | split("/") | last` from `GetAllPlugins`), never `plugin.json`'s `name` (older Marketplace installs use numeric catalog IDs). Do not emit `plugin://` or `plugins://`.
- **Marketplace installs:** Suggest catalog plugins with `<plugin-card catalog-id="<marketplace-id>"></plugin-card>` on its own line.
- **Never hand-edit `~/.gemini/config/config.json`:** `config.json` holds `userSettings`, `plugins.<dir>.enabled`, and permission grants written atomically at mode `0600`. Manual edits risk clobbering concurrent state and skip live reload; use `agy plugin enable|disable`, `/plugin`, or `customization://<dir>`.
- **Built-in plugins (`/builtin/plugins/`):** Cannot be uninstalled; disable them instead.
- **Inspecting via Language Server:** Always pipe `GetAllPlugins` through `jq` — unfiltered output inlines full `SKILL.md` bodies.

## Remote Agent Sessions

In `agy --remote-agent` sessions, the `/` menu excludes local machine skills. Cloud-connected plugins still expose their skills under `Remote agent skills` in `/skills`.

## Headless `agy` for Testing and Optimization

`agy -p` accepts prompts via CLI argument or stdin and supports `--disable-slash-commands` (prevents slash/skill expansion during evaluation) and `--model`:

```bash
uv run scripts/trigger_test.py <name> --agent antigravity --cases cases.yaml --judge agy-cli
uv run scripts/optimize_skill.py <name> --agent antigravity --tasks tasks.jsonl \
    --optimizer-cmd "agy -p --disable-slash-commands" \
    --target-cmd "agy -p --disable-slash-commands"
```

## Live Documentation

- Official docs index: `https://antigravity.google/llms.txt` (append `.md` to any docs page URL for Markdown)
- Skills: `https://antigravity.google/docs/skills.md`
- Plugins: `https://antigravity.google/docs/plugins.md`
- CLI reference: `https://antigravity.google/docs/cli/reference.md`
- Changelog: `https://antigravity.google/docs/changelog.md` (or `agy changelog` / `/changelog`)
- Built-in assistant guide: `/agy-customizations` and `/antigravity-guide`
