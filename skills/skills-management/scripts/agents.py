#!/usr/bin/env python3
"""Shared agent definitions for multi-agent skill management.

The single source of truth for where each AI coding agent reads Agent Skills.

Baseline: the Skills CLI registry, ``src/agents.ts`` in vercel-labs/skills at
commit b716f9d (2026-11-12, verified unchanged through 57217cf on 2026-11-17),
https://github.com/vercel-labs/skills/blob/b716f9dc2ba36b6aa8f0080615e5a3a6caeac63b/src/agents.ts
(``UPSTREAM`` below). Entries that differ from it, or were checked against the
vendor's own documentation, name that source in ``source``.

Path conventions:

- ``global_dir`` is where a global install of this skill manager writes, i.e. a
  directory the agent reads. For "universal" agents that read the shared
  ``~/.agents/skills`` this is that shared directory, as in the upstream
  installer's ``getAgentBaseDir``.
- ``extra_global_dirs`` are further user-level directories the agent reads or
  earlier installers wrote to. They are scanned by the duplicate audit and by
  ``delete_skill.py --all-agents`` but never written to.
- ``~/.config`` honours ``$XDG_CONFIG_HOME``; ``home_env`` names an environment
  variable that relocates the agent's home directory (for example ``GROK_HOME``).
"""

from __future__ import annotations

import os
import shutil
from collections.abc import Callable
from pathlib import Path
from typing import TypedDict

UPSTREAM = "vercel-labs/skills@b716f9d src/agents.ts"
DOCS = "vendor docs, checked 2026-11-14: "
DOCS_NOV26 = "vendor docs, checked 2026-11-26: "
SHARED_GLOBAL = "~/.agents/skills"
SHARED_PROJECT = ".agents/skills"


class AgentConfig(TypedDict, total=False):
    """Configuration for an AI coding agent."""
    name: str
    display_name: str
    project_dir: str      # Relative path for project-level skills
    extra_project_dirs: list[str]  # Additional workspace-relative dirs read (audit/discovery only)
    global_dir: str       # Path for user-level skills (supports ~ and ~/.config)
    global_dir_windows: str  # Windows override for global_dir (%VARS% expanded)
    extra_global_dirs: list[str]  # Further user-level dirs the agent reads (audit/delete only)
    reads_shared_global: bool  # True when agent also reads ~/.agents/skills at lower priority
    supports_nested_categories: bool  # True when root may hold <category>/<skill>/SKILL.md (Hermes)
    home_env: tuple[str, str]  # (ENV_VAR, default home): ENV_VAR replaces that prefix
    detect_paths: list[str]  # User-level paths that indicate the agent is installed
    detect_project_markers: list[str]  # Paths relative to cwd that indicate the agent
    detect_binaries: list[str]  # CLI binaries whose presence indicates an active install
    detect_apps: list[str]  # macOS .app bundles whose presence indicates an active install
    detect_extensions: list[str]  # IDE extension/plugin ID prefixes (lowercase matched)
    source: str           # Where the paths were verified


def _agent(
    name: str,
    display_name: str,
    project_dir: str,
    global_dir: str,
    detect_paths: list[str],
    *,
    extra_project_dirs: list[str] | None = None,
    extra_global_dirs: list[str] | None = None,
    reads_shared_global: bool = False,
    supports_nested_categories: bool = False,
    home_env: tuple[str, str] | None = None,
    global_dir_windows: str | None = None,
    detect_project_markers: list[str] | None = None,
    detect_binaries: list[str] | None = None,
    detect_apps: list[str] | None = None,
    detect_extensions: list[str] | None = None,
    source: str = UPSTREAM,
) -> AgentConfig:
    config: AgentConfig = {
        "name": name,
        "display_name": display_name,
        "project_dir": project_dir,
        "global_dir": global_dir,
        "detect_paths": detect_paths,
        "source": source,
    }
    if extra_project_dirs:
        config["extra_project_dirs"] = extra_project_dirs
    if extra_global_dirs:
        config["extra_global_dirs"] = extra_global_dirs
    if reads_shared_global:
        config["reads_shared_global"] = True
    if supports_nested_categories:
        config["supports_nested_categories"] = True
    if home_env:
        config["home_env"] = home_env
    if global_dir_windows:
        config["global_dir_windows"] = global_dir_windows
    if detect_project_markers:
        config["detect_project_markers"] = detect_project_markers
    if detect_binaries:
        config["detect_binaries"] = detect_binaries
    if detect_apps:
        config["detect_apps"] = detect_apps
    if detect_extensions:
        config["detect_extensions"] = detect_extensions
    return config


AGENT_ALIASES: dict[str, str] = {
    "agy": "antigravity-cli",
    "gemini": "gemini-cli",
    "hermes": "hermes-agent",
    "kimi-code": "kimi-code-cli",
    "grok-build": "grok",
    "codex-cli": "codex",
    "cursor-cli": "cursor",
    "devin-cli": "devin",
    "claude-desktop": "claude-code",
}

NON_INSTALLABLE_HARNESSES: dict[str, str] = {
    "porch": (
        "porch is an orchestrator over underlying harnesses "
        "(claude-code, codex, opencode, agy, grok, devin, gemini-cli, cursor); "
        "install skills into those target harnesses instead."
    ),
}

PORCH_HARNESS_AGENTS: tuple[str, ...] = (
    "claude-code",
    "codex",
    "opencode",
    "antigravity",
    "antigravity-cli",
    "grok",
    "devin",
    "gemini-cli",
    "cursor",
    "qwen-code",
    "kimi-code-cli",
    "hermes-agent",
    "omp",
)


_REGISTRY: list[AgentConfig] = [
    _agent("adal", "AdaL", ".adal/skills", "~/.adal/skills", ["~/.adal"],
           detect_binaries=["adal"]),
    _agent("aider-desk", "AiderDesk", ".aider-desk/skills", "~/.aider-desk/skills", ["~/.aider-desk"],
           detect_apps=["AiderDesk.app"]),
    _agent("amp", "Amp", SHARED_PROJECT, SHARED_GLOBAL, ["~/.config/amp"],
           extra_global_dirs=["~/.config/agents/skills", "~/.config/amp/skills"],
           detect_binaries=["amp"], detect_extensions=["sourcegraph.amp"],
           source=DOCS + "https://ampcode.com/docs/customize/skills"),
    # Antigravity App 2.0 / IDE reads .agents/skills (plus legacy .agent, _agents,
    # _agent) in a workspace and ~/.gemini/config/skills globally (NOT ~/.agents/skills).
    # Antigravity CLI (agy) additionally reads ~/.agents/skills at lower priority (1.5.16+).
    # ~/.gemini/antigravity/skills is pre-2.0 (typically a symlink to ~/.gemini/config/skills).
    _agent("antigravity", "Antigravity (App / IDE)", SHARED_PROJECT, "~/.gemini/config/skills",
           ["~/.gemini/antigravity", "~/.gemini/config/skills", "~/.gemini/config/config.json",
            "/Applications/Antigravity.app"],
           extra_project_dirs=[".agent/skills", "_agents/skills", "_agent/skills"],
           extra_global_dirs=["~/.gemini/antigravity/skills", "~/.gemini/skills"],
           reads_shared_global=False,
           detect_apps=["Antigravity.app"],
           source=DOCS_NOV26 + "https://antigravity.google/docs/skills; agy-customizations SKILL.md"),
    _agent("antigravity-cli", "Antigravity CLI", SHARED_PROJECT, "~/.gemini/config/skills",
           ["~/.gemini/antigravity-cli"],
           extra_project_dirs=[".agent/skills", "_agents/skills", "_agent/skills"],
           extra_global_dirs=["~/.gemini/antigravity-cli/skills", "~/.gemini/skills"],
           reads_shared_global=True,
           detect_binaries=["agy"],
           source=DOCS_NOV26 + "https://antigravity.google/docs/skills; agy 1.5.16 changelog; " + UPSTREAM + " (fe7ff9a)"),
    _agent("augment", "Augment", ".augment/skills", "~/.augment/skills", ["~/.augment"],
           detect_binaries=["auggie"],
           detect_extensions=["augment.vscode-augment", "com.augmentcode"]),
    _agent("autohand-code", "Autohand Code CLI", ".autohand/skills", "~/.autohand/skills",
           ["~/.autohand"], home_env=("AUTOHAND_HOME", "~/.autohand"),
           detect_binaries=["autohand"]),
    _agent("bob", "IBM Bob", ".bob/skills", "~/.bob/skills", ["~/.bob"]),
    _agent("claude-code", "Claude Code", ".claude/skills", "~/.claude/skills", ["~/.claude"],
           home_env=("CLAUDE_CONFIG_DIR", "~/.claude"),
           detect_binaries=["claude"], detect_apps=["Claude.app"],
           detect_extensions=["anthropic.claude-code"],
           source=DOCS + "https://code.claude.com/docs/en/skills; CLAUDE_CONFIG_DIR from " + UPSTREAM),
    # Deliberately differs from upstream, which treats Cline as universal (#440, #441):
    # Cline's docs list only .cline/skills, .clinerules/skills, .claude/skills and
    # ~/.cline/skills, and never .agents/skills.
    _agent("cline", "Cline", ".cline/skills", "~/.cline/skills", ["~/.cline"],
           detect_binaries=["cline"], detect_extensions=["saoudrizwan.claude-dev"],
           source=DOCS + "https://docs.cline.bot/customization/skills"),
    _agent("codearts-agent", "CodeArts Agent", ".codeartsdoer/skills", "~/.codeartsdoer/skills",
           ["~/.codeartsdoer"]),
    _agent("codebuddy", "CodeBuddy", ".codebuddy/skills", "~/.codebuddy/skills", ["~/.codebuddy"],
           detect_project_markers=[".codebuddy"],
           detect_binaries=["codebuddy"], detect_apps=["CodeBuddy.app"]),
    _agent("codemaker", "Codemaker", ".codemaker/skills", "~/.codemaker/skills", ["~/.codemaker"]),
    _agent("codestudio", "Code Studio", ".codestudio/skills", "~/.codestudio/skills", ["~/.codestudio"]),
    _agent("codex", "Codex", SHARED_PROJECT, SHARED_GLOBAL, ["~/.codex", "/etc/codex"],
           home_env=("CODEX_HOME", "~/.codex"),
           detect_binaries=["codex"], detect_apps=["Codex.app"],
           detect_extensions=["openai.chatgpt"],
           source=DOCS + "https://learn.chatgpt.com/docs/build-skills"),
    _agent("command-code", "Command Code", ".commandcode/skills", "~/.commandcode/skills",
           ["~/.commandcode"], detect_binaries=["command-code", "cmdc"]),
    _agent("continue", "Continue", ".continue/skills", "~/.continue/skills", ["~/.continue"],
           detect_project_markers=[".continue"],
           detect_binaries=["cn"], detect_extensions=["continue.continue"]),
    _agent("cortex", "Cortex Code", ".cortex/skills", "~/.snowflake/cortex/skills",
           ["~/.snowflake/cortex"], detect_binaries=["cortex"]),
    _agent("crush", "Crush", ".crush/skills", "~/.config/crush/skills", ["~/.config/crush"],
           detect_binaries=["crush"]),
    _agent("cursor", "Cursor", SHARED_PROJECT, SHARED_GLOBAL, ["~/.cursor"],
           extra_global_dirs=["~/.cursor/skills"],
           home_env=("CURSOR_CONFIG_DIR", "~/.cursor"),
           detect_binaries=["cursor", "cursor-agent"],
           detect_apps=["Cursor.app"],
           source=DOCS_NOV26 + "https://cursor.com/docs/context/skills; porch backend_contract.py"),
    _agent("deepagents", "Deep Agents", SHARED_PROJECT, SHARED_GLOBAL, ["~/.deepagents"],
           extra_global_dirs=["~/.deepagents/agent/skills"],
           detect_binaries=["deepagents", "deepagents-code"]),
    # Devin CLI reads .agents/skills and .devin/skills in a project, and
    # ~/.agents/skills and ~/.config/devin/skills globally; ~/.devin/skills is not
    # a documented location. The shared project dir avoids a second copy.
    _agent("devin", "Devin CLI / Desktop", SHARED_PROJECT, "~/.config/devin/skills",
           ["~/.config/devin"], global_dir_windows="%APPDATA%\\devin\\skills",
           reads_shared_global=True,
           detect_binaries=["devin", "devin-desktop"], detect_apps=["Devin.app"],
           source=DOCS + "https://docs.devin.ai/cli/extensibility/skills/overview"),
    _agent("dexto", "Dexto", SHARED_PROJECT, SHARED_GLOBAL, ["~/.dexto"]),
    # Droid reads .agents/skills and ~/.agents/skills as compatibility locations;
    # ~/.factory/skills holds skills placed by earlier installers.
    _agent("droid", "Droid", SHARED_PROJECT, SHARED_GLOBAL, ["~/.factory"],
           extra_global_dirs=["~/.factory/skills"],
           detect_binaries=["droid"],
           source=DOCS + "https://docs.factory.com/cli/configuration/skills"),
    _agent("firebender", "Firebender", SHARED_PROJECT, SHARED_GLOBAL, ["~/.firebender"],
           extra_global_dirs=["~/.firebender/skills"]),
    _agent("forgecode", "ForgeCode", ".forge/skills", "~/.forge/skills", ["~/.forge"],
           detect_binaries=["forgecode"]),
    _agent("fx", "fx", SHARED_PROJECT, SHARED_GLOBAL, ["~/.fx"]),
    _agent("gemini-cli", "Gemini CLI", SHARED_PROJECT, SHARED_GLOBAL, ["~/.gemini"],
           extra_global_dirs=["~/.gemini/skills"],
           detect_binaries=["gemini"],
           source=DOCS + "https://geminicli.com/docs/cli/skills/"),
    _agent("github-copilot", "GitHub Copilot", SHARED_PROJECT, SHARED_GLOBAL, ["~/.copilot"],
           extra_global_dirs=["~/.copilot/skills"],
           detect_binaries=["copilot"],
           detect_extensions=["github.copilot", "github.copilot-chat"],
           source=DOCS + "https://docs.github.com/en/copilot/concepts/agents/about-agent-skills"),
    # Goose 1.25+ (Summon extension) recommends .agents/skills and ~/.agents/skills;
    # ~/.config/goose/skills is the 1.16-1.24 location. Upstream still uses .goose/skills.
    _agent("goose", "Goose", SHARED_PROJECT, SHARED_GLOBAL, ["~/.config/goose"],
           extra_global_dirs=["~/.config/goose/skills"],
           detect_binaries=["goose"], detect_apps=["Goose.app"],
           source=DOCS + "https://goose-docs.ai/docs/guides/context-engineering/using-skills"),
    # Grok reads ~/.agents/skills too, but not a project .agents/skills. GROK_HOME
    # comes from upstream only; the xAI page does not mention it.
    _agent("grok", "Grok Build", ".grok/skills", "~/.grok/skills", ["~/.grok"],
           home_env=("GROK_HOME", "~/.grok"),
           reads_shared_global=True,
           detect_binaries=["grok"], detect_apps=["Grok Bot.app", "Grok.app"],
           source=DOCS + "https://docs.x.ai/build/features/skills-plugins-marketplaces; " + UPSTREAM),
    # Hermes reads ~/.agents/skills only when listed in skills.external_dirs, and
    # project skills only in a repository trusted with `hermes skills trust`.
    # HERMES_HOME (profile home) comes from upstream.
    _agent("hermes-agent", "Hermes Agent", ".hermes/skills", "~/.hermes/skills", ["~/.hermes"],
           home_env=("HERMES_HOME", "~/.hermes"),
           supports_nested_categories=True,
           detect_binaries=["hermes"], detect_apps=["Hermes.app"],
           source=DOCS_NOV26 + "https://hermes-agent.nousresearch.com/docs/user-guide/features/skills; " + UPSTREAM),
    _agent("iflow-cli", "iFlow CLI", ".iflow/skills", "~/.iflow/skills", ["~/.iflow"],
           detect_binaries=["iflow"]),
    _agent("inference-sh", "inference.sh", ".inferencesh/skills", "~/.inferencesh/skills",
           ["~/.inferencesh"]),
    _agent("jazz", "Jazz", ".jazz/skills", "~/.jazz/skills", ["~/.jazz"],
           detect_project_markers=[".jazz"]),
    _agent("junie", "Junie", ".junie/skills", "~/.junie/skills", ["~/.junie"],
           detect_binaries=["junie"],
           detect_extensions=["org.jetbrains.junie", "junie"]),
    # .kilocode is Kilo's legacy config directory.
    _agent("kilo", "Kilo Code", SHARED_PROJECT, SHARED_GLOBAL, ["~/.kilo", "~/.kilocode"],
           extra_global_dirs=["~/.kilo/skills", "~/.kilocode/skills"],
           detect_binaries=["kilo", "kilocode"],
           detect_extensions=["kilocode.kilo-code"],
           source=DOCS + "https://kilo.ai/docs/customize/skills; .kilocode from " + UPSTREAM),
    _agent("kimchi", "Kimchi", ".kimchi/skills", "~/.config/kimchi/harness/skills",
           ["~/.config/kimchi"]),
    # Renamed upstream from kimi-cli (eaad526); global dir moved off ~/.config/agents/skills.
    _agent("kimi-code-cli", "Kimi Code CLI", SHARED_PROJECT, SHARED_GLOBAL,
           ["~/.kimi-code", "~/.kimi"],
           extra_global_dirs=["~/.config/agents/skills", "~/.kimi/skills"],
           home_env=("KIMI_CODE_HOME", "~/.kimi-code"),
           detect_binaries=["kimi", "kimi-code"],
           source=DOCS_NOV26 + "https://moonshotai.github.io/kimi-cli/en/customization/skills.html; "
           + UPSTREAM + " (eaad526)"),
    _agent("kiro-cli", "Kiro CLI", ".kiro/skills", "~/.kiro/skills", ["~/.kiro"],
           detect_binaries=["kiro-cli", "kiro"], detect_apps=["Kiro.app"]),
    _agent("kode", "Kode", ".kode/skills", "~/.kode/skills", ["~/.kode"]),
    _agent("lingma", "Lingma", ".lingma/skills", "~/.lingma/skills", ["~/.lingma"]),
    _agent("loaf", "Loaf", SHARED_PROJECT, SHARED_GLOBAL, ["~/.loaf"]),
    _agent("mcpjam", "MCPJam", ".mcpjam/skills", "~/.mcpjam/skills", ["~/.mcpjam"]),
    _agent("minimax-code", "MiniMax Code", ".minimax/skills", "~/.minimax/skills",
           ["~/.minimax", "/Applications/MiniMax Code.app"],
           detect_apps=["MiniMax Code.app"]),
    _agent("mistral-vibe", "Mistral Vibe", ".vibe/skills", "~/.vibe/skills", ["~/.vibe"],
           home_env=("VIBE_HOME", "~/.vibe"),
           detect_binaries=["vibe"]),
    _agent("moxby", "Moxby", ".moxby/skills", "~/.moxby/skills", ["~/.moxby"]),
    _agent("mux", "Mux", ".mux/skills", "~/.mux/skills", ["~/.mux"],
           detect_binaries=["mux", "xum"], detect_apps=["Mux.app", "Xum.app"]),
    _agent("neovate", "Neovate", ".neovate/skills", "~/.neovate/skills", ["~/.neovate"],
           detect_binaries=["neovate"]),
    _agent("omp", "Oh My Pi", ".omp/skills", "~/.omp/agent/skills", ["~/.omp", "~/.omp/agent"],
           extra_project_dirs=[SHARED_PROJECT],
           extra_global_dirs=["~/.omp/skills", "~/.omp/agent/managed-skills"],
           reads_shared_global=True,
           detect_binaries=["omp"],
           source=DOCS_NOV26 + "https://github.com/can1357/oh-my-pi"),
    _agent("ona", "Ona", ".ona/skills", "~/.ona/skills", ["~/.ona"]),
    # The project dir is the repository's own skills/ folder; ~/.clawdbot and
    # ~/.moltbot are pre-rename homes (upstream reads the first that exists).
    _agent("openclaw", "OpenClaw", "skills", "~/.openclaw/skills",
           ["~/.openclaw", "~/.clawdbot", "~/.moltbot"],
           extra_global_dirs=["~/.clawdbot/skills", "~/.moltbot/skills"],
           detect_binaries=["openclaw", "clawdbot", "moltbot"],
           detect_apps=["OpenClaw.app"]),
    _agent("opencode", "OpenCode", SHARED_PROJECT, SHARED_GLOBAL, ["~/.config/opencode"],
           extra_global_dirs=["~/.config/opencode/skills"],
           detect_binaries=["opencode"], detect_apps=["OpenCode.app"],
           source=DOCS + "https://opencode.ai/docs/skills/"),
    _agent("openhands", "OpenHands", ".openhands/skills", "~/.openhands/skills", ["~/.openhands"],
           detect_binaries=["openhands"]),
    # Pi reads .agents/skills up the tree and ~/.agents/skills globally
    # (https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md).
    _agent("pi", "Pi", SHARED_PROJECT, SHARED_GLOBAL, ["~/.pi/agent"],
           extra_global_dirs=["~/.pi/agent/skills"],
           detect_binaries=["pi"],
           source=UPSTREAM + " (2a286c7); pi-mono docs/skills.md"),
    _agent("pochi", "Pochi", ".pochi/skills", "~/.pochi/skills", ["~/.pochi"],
           detect_binaries=["pochi"], detect_extensions=["tabbyml.pochi"]),
    _agent("posit-assistant", "Posit Assistant", ".posit/assistant/skills",
           "~/.posit/assistant/skills", ["~/.posit/assistant", "~/.positai"]),
    _agent("qoder", "Qoder", ".qoder/skills", "~/.qoder/skills", ["~/.qoder"],
           detect_binaries=["qodercli", "qoder"], detect_apps=["Qoder.app"]),
    _agent("qoder-cn", "Qoder CN", ".qoder/skills", "~/.qoder-cn/skills", ["~/.qoder-cn"],
           detect_binaries=["qodercli", "qoder"], detect_apps=["Qoder CN.app", "Qoder.app"]),
    _agent("qwen-code", "Qwen Code", ".qwen/skills", "~/.qwen/skills", ["~/.qwen"],
           detect_binaries=["qwen"]),
    _agent("reasonix", "Reasonix", ".reasonix/skills", "~/.reasonix/skills", ["~/.reasonix"],
           home_env=("REASONIX_HOME", "~/.reasonix"),
           global_dir_windows="%APPDATA%\\reasonix\\skills"),
    # Replit is detected by a project's .replit file, not by a home directory. Its
    # docs describe only project skills (/.agents/skills); the global dir is upstream's.
    _agent("replit", "Replit", SHARED_PROJECT, SHARED_GLOBAL, [],
           extra_global_dirs=["~/.config/agents/skills"], detect_project_markers=[".replit"],
           source=DOCS + "https://docs.replit.com/core-concepts/agent/skills; global from " + UPSTREAM),
    _agent("roo", "Roo Code", ".roo/skills", "~/.roo/skills", ["~/.roo"],
           detect_extensions=["rooveterinaryinc.roo-cline"]),
    _agent("rovodev", "Rovo Dev", ".rovodev/skills", "~/.rovodev/skills", ["~/.rovodev"],
           detect_binaries=["acli"]),
    _agent("sarvam-code", "Sarvam Code", SHARED_PROJECT, SHARED_GLOBAL, ["~/.sarvam"],
           home_env=("SARVAM_HOME", "~/.sarvam")),
    _agent("tabnine-cli", "Tabnine CLI", ".tabnine/agent/skills", "~/.tabnine/agent/skills",
           ["~/.tabnine"], detect_binaries=["tabnine"]),
    _agent("terramind", "Terramind", ".terramind/skills", "~/.terramind/skills", ["~/.terramind"]),
    _agent("tinycloud", "Tinycloud", ".tinycloud/skills", "~/.tinycloud/skills", ["~/.tinycloud"]),
    _agent("trae", "Trae", ".trae/skills", "~/.trae/skills", ["~/.trae"],
           detect_binaries=["trae"], detect_apps=["Trae.app"]),
    _agent("trae-cn", "Trae CN", ".trae/skills", "~/.trae-cn/skills", ["~/.trae-cn"],
           detect_binaries=["trae-cn", "trae"], detect_apps=["Trae CN.app", "Trae.app"]),
    _agent("warp", "Warp", SHARED_PROJECT, SHARED_GLOBAL, ["~/.warp"],
           detect_binaries=["warp"], detect_apps=["Warp.app"]),
    # Windsurf docs now redirect to Devin Desktop, which still reads .windsurf/skills
    # (legacy) and ~/.codeium/<channel>/skills.
    _agent("windsurf", "Windsurf", ".windsurf/skills", "~/.codeium/windsurf/skills",
           ["~/.codeium/windsurf"],
           detect_binaries=["windsurf", "devin-desktop"], detect_apps=["Windsurf.app", "Devin.app"],
           source=DOCS + "https://docs.devin.ai/cli/extensibility/skills/overview; " + UPSTREAM),
    _agent("zcode", "ZCode", ".zcode/skills", "~/.zcode/skills",
           ["~/.zcode", "/Applications/ZCode.app"],
           detect_apps=["ZCode.app"]),
    _agent("zed", "Zed", SHARED_PROJECT, SHARED_GLOBAL, ["~/.config/zed"],
           detect_binaries=["zed"], detect_apps=["Zed.app"],
           source=DOCS + "https://zed.dev/docs/ai/skills"),
    _agent("zencoder", "Zencoder", ".zencoder/skills", "~/.zencoder/skills", ["~/.zencoder"],
           detect_binaries=["zen", "zencoder"],
           detect_extensions=["zencoderai.zencoder", "zencoder"]),
    _agent("zenflow", "Zenflow", ".zencoder/skills", "~/.zencoder/skills", ["~/.zencoder"],
           detect_binaries=["zenflow"], detect_apps=["Zenflow.app", "Zenflow Code.app"]),
]

# Upstream entries not carried over: eve and promptscript (project-only, detected
# by package.json or config markers), astrbot (project dir is a generic data/skills),
# and universal (a pseudo-agent for the shared directory itself).

AGENTS: dict[str, AgentConfig] = {config["name"]: config for config in _REGISTRY}


def canonical_agent_id(agent: str) -> str:
    """Normalize a user-supplied agent or harness name to its canonical registry ID."""
    norm = agent.strip().lower()
    return AGENT_ALIASES.get(norm, norm)


def expand_path(path: str, config: AgentConfig | None = None) -> Path:
    """Expand ``~``, ``$XDG_CONFIG_HOME`` for ``~/.config`` and the agent's ``home_env``."""
    xdg = os.environ.get("XDG_CONFIG_HOME", "").strip()
    if config and (home_env := config.get("home_env")):
        env_var, default_home = home_env
        override = os.environ.get(env_var, "").strip()
        if not override and env_var == "CURSOR_CONFIG_DIR" and xdg:
            xdg_cursor = Path(xdg).expanduser() / "cursor"
            if xdg_cursor.exists():
                override = str(xdg_cursor)
        if override and (path == default_home or path.startswith(default_home + "/")):
            path = override + path[len(default_home):]
    if xdg and (path == "~/.config" or path.startswith("~/.config/")):
        path = xdg + path[len("~/.config"):]
    return Path(path).expanduser()


def expand_path_for_home(path: str, home: Path | None = None, config: AgentConfig | None = None) -> Path:
    """Expand ``path`` respecting custom ``home`` cleanly in tests and live runs."""
    if home is None or home == Path.home():
        return expand_path(path, config)
    if path == "~/.config" or path.startswith("~/.config/"):
        xdg = os.environ.get("XDG_CONFIG_HOME", "").strip()
        if xdg:
            return Path(xdg + path[len("~/.config"):])
    if config and (home_env := config.get("home_env")):
        env_var, default_home = home_env
        override = os.environ.get(env_var, "").strip()
        if override and (path == default_home or path.startswith(default_home + "/")):
            return Path(override + path[len(default_home):])
    if path.startswith("~/"):
        return home / path[2:]
    if path == "~":
        return home
    return Path(path)


def find_agent_binary(
    binary: str,
    *,
    home: Path | None = None,
    which_fn: Callable[[str], str | None] | None = None,
) -> str | None:
    """Locate ``binary`` in ``PATH`` and common user/Homebrew binary directories."""
    if which_fn is not None:
        return which_fn(binary)
    base_home = home or Path.home()
    paths: list[str] = []
    if env_path := os.environ.get("PATH", ""):
        paths.append(env_path)
    if base_home == Path.home():
        extra_bins = [
            base_home / ".local" / "bin",
            base_home / ".bun" / "bin",
            base_home / ".cargo" / "bin",
            base_home / ".npm-global" / "bin",
            base_home / ".volta" / "bin",
            base_home / ".codeium" / "windsurf" / "bin",
            Path("/opt/homebrew/bin"),
            Path("/usr/local/bin"),
        ]
        paths.extend(str(p) for p in extra_bins if p.is_dir())
    search_path = os.pathsep.join(paths) if paths else None
    return shutil.which(binary, path=search_path)


def _installed_extension_names(
    home: Path,
    extension_dirs: list[Path] | None = None,
) -> list[str]:
    """Collect lowercase directory names of installed VS Code/Cursor/JetBrains plugins."""
    dirs: list[Path] = []
    if extension_dirs is not None:
        dirs.extend(extension_dirs)
    else:
        for rel in (
            ".vscode/extensions",
            ".cursor/extensions",
            ".antigravity/extensions",
            ".windsurf/extensions",
        ):
            cand = home / rel
            if cand.is_dir():
                dirs.append(cand)
        for jb_root in (
            home / "Library" / "Application Support" / "JetBrains",
            home / ".local" / "share" / "JetBrains",
        ):
            if jb_root.is_dir():
                try:
                    for ide_dir in jb_root.iterdir():
                        plug = ide_dir / "plugins"
                        if plug.is_dir():
                            dirs.append(plug)
                except OSError:
                    pass

    names: list[str] = []
    for ext_dir in dirs:
        if not ext_dir.is_dir():
            continue
        try:
            for item in ext_dir.iterdir():
                if not item.name.startswith("."):
                    names.append(item.name.lower())
        except OSError:
            continue
    return names


def inspect_agent_installations(
    agent_ids: list[str] | None = None,
    *,
    cwd: Path | None = None,
    home: Path | None = None,
    which_fn: Callable[[str], str | None] | None = None,
    app_dirs: list[Path] | None = None,
    extension_dirs: list[Path] | None = None,
) -> dict[str, dict]:
    """Classify installed agent roots as active, skills-only-stub, orphaned-agent, or unverified."""
    home = home or Path.home()
    cwd = cwd or Path.cwd()
    default_apps = [Path("/Applications"), home / "Applications"] if home == Path.home() else [home / "Applications"]
    check_app_dirs = app_dirs if app_dirs is not None else default_apps
    ext_names = _installed_extension_names(home, extension_dirs)

    if agent_ids is not None:
        target_ids = agent_ids
    elif home == Path.home():
        target_ids = detect_installed_agents(cwd=cwd)
    else:
        target_ids = [
            aid for aid, cfg in AGENTS.items()
            if any(
                expand_path_for_home(p, home, cfg).exists()
                for p in cfg["detect_paths"]
                if not p.startswith("/")
            )
            or any((cwd / m).exists() for m in cfg.get("detect_project_markers", []))
        ]

    porch_bin_env = {
        "codex": "PORCH_BIN_CODEX",
        "claude-code": "PORCH_BIN_CLAUDE",
        "opencode": "PORCH_BIN_OPENCODE",
        "grok": "PORCH_BIN_GROK",
        "gemini-cli": "PORCH_BIN_GEMINI",
        "devin": "PORCH_BIN_DEVIN",
        "antigravity-cli": "PORCH_BIN_AGY",
        "cursor": "PORCH_BIN_CURSOR",
    }
    results: dict[str, dict] = {}
    generic_parents = {
        str(home.absolute()),
        str((home / ".config").absolute()),
        str((home / ".agents").absolute()),
        str((home / ".gemini").absolute()),
    }
    shared_skill_dirs = {
        str((home / ".agents" / "skills").absolute()),
        str((home / ".config" / "agents" / "skills").absolute()),
    }

    for raw_id in target_ids:
        aid = canonical_agent_id(raw_id)
        cfg = AGENTS.get(aid)
        if not cfg:
            continue

        matched_paths: list[str] = []
        for raw_p in cfg["detect_paths"]:
            if home != Path.home() and raw_p.startswith("/"):
                continue
            exp = expand_path_for_home(raw_p, home, cfg)
            if exp.exists():
                matched_paths.append(str(exp))
        for marker in cfg.get("detect_project_markers", []):
            mp = cwd / marker
            if mp.exists():
                matched_paths.append(str(mp))

        found_binaries: dict[str, str] = {}
        for bin_name in cfg.get("detect_binaries", []):
            loc = find_agent_binary(bin_name, home=home, which_fn=which_fn)
            if loc:
                found_binaries[bin_name] = loc
        if not found_binaries and home == Path.home() and which_fn is None:
            if env_var := porch_bin_env.get(aid):
                override_bin = os.environ.get(env_var, "").strip()
                if override_bin:
                    cand_p = Path(override_bin).expanduser()
                    resolved_bin = str(cand_p) if cand_p.exists() else shutil.which(override_bin)
                    if resolved_bin:
                        found_binaries[Path(resolved_bin).name] = resolved_bin

        found_apps: list[str] = []
        for app_name in cfg.get("detect_apps", []):
            for adir in check_app_dirs:
                cand = adir / app_name
                if cand.exists():
                    found_apps.append(str(cand))

        found_extensions: list[str] = []
        for prefix in cfg.get("detect_extensions", []):
            plower = prefix.lower()
            for ename in ext_names:
                if ename == plower or ename.startswith(plower + "-") or ename.startswith(plower + "."):
                    if ename not in found_extensions:
                        found_extensions.append(ename)

        # Evaluate stub roots (non-/Applications dir roots holding ONLY skills/)
        stub_roots: list[str] = []
        dir_roots = [
            Path(p) for p in matched_paths
            if not p.endswith(".app") and Path(p).is_dir() and str(Path(p).absolute()) not in generic_parents
        ]
        if dir_roots:
            all_stubs = True
            for d in dir_roots:
                if not (d / "skills").is_dir():
                    all_stubs = False
                    break
                try:
                    children = [c.name for c in d.iterdir() if c.name != ".DS_Store"]
                except OSError:
                    all_stubs = False
                    break
                if children != ["skills"]:
                    all_stubs = False
                    break
            if all_stubs:
                stub_roots = [str(d) for d in dir_roots]

        # Gemini CLI shares ~/.gemini with Antigravity; verify it isn't just Antigravity state
        gemini_shared_parent_only = False
        if aid == "gemini-cli" and not found_binaries:
            gem_dir = home / ".gemini"
            if gem_dir.is_dir():
                try:
                    gem_items = {c.name for c in gem_dir.iterdir()}
                except OSError:
                    gem_items = set()
                non_agy_items = gem_items - {"antigravity", "antigravity-cli", "config", ".DS_Store"}
                if not non_agy_items:
                    gemini_shared_parent_only = True

        # Existing dedicated (non-~/.agents/skills) skill dirs configured for this agent
        dedicated_skill_dirs: list[str] = []
        for raw_sd in [cfg["global_dir"], *cfg.get("extra_global_dirs", [])]:
            sd = expand_path_for_home(raw_sd, home, cfg)
            sd_str = str(sd.absolute())
            if sd_str in shared_skill_dirs:
                continue
            if sd.exists() and sd_str not in dedicated_skill_dirs:
                dedicated_skill_dirs.append(sd_str)

        has_liveness_checks = bool(
            cfg.get("detect_binaries") or cfg.get("detect_apps") or cfg.get("detect_extensions")
        )
        if found_binaries or found_apps or found_extensions:
            status = "active"
            signals: list[str] = []
            if found_binaries:
                signals.append("bin:" + ",".join(sorted(found_binaries)))
            if found_apps:
                signals.append("app:" + ",".join(Path(a).name for a in found_apps))
            if found_extensions:
                signals.append("ext:" + ",".join(found_extensions))
            reason = "; ".join(signals)
        elif gemini_shared_parent_only:
            status = "shared-parent-only"
            reason = "~/.gemini holds only Antigravity state and no gemini binary is installed"
        elif not matched_paths and not dedicated_skill_dirs:
            status = "not-installed"
            reason = "neither binary/app nor config/skills directory exists"
        elif not has_liveness_checks:
            status = "unverified"
            reason = "no binary/app/extension probe defined for registry entry"
        elif stub_roots:
            status = "skills-only-stub"
            reason = f"no binary/app/extension found; root(s) hold only skills/ ({', '.join(stub_roots)})"
        else:
            status = "orphaned-agent"
            missing = []
            if cfg.get("detect_binaries"):
                missing.append("bin(" + "/".join(cfg["detect_binaries"]) + ")")
            if cfg.get("detect_apps"):
                missing.append("app(" + "/".join(cfg["detect_apps"]) + ")")
            if cfg.get("detect_extensions"):
                missing.append("ext(" + "/".join(cfg["detect_extensions"]) + ")")
            reason = f"residual config present, missing {' & '.join(missing)}"

        results[aid] = {
            "agent_id": aid,
            "display_name": cfg["display_name"],
            "status": status,
            "matched_paths": matched_paths,
            "found_binaries": found_binaries,
            "found_apps": found_apps,
            "found_extensions": found_extensions,
            "stub_roots": stub_roots,
            "dedicated_skill_dirs": dedicated_skill_dirs,
            "reason": reason,
        }
    return results


def hermes_reads_shared_global(home: Path | None = None) -> bool:
    """True if Hermes config declares ``~/.agents/skills`` in ``skills.external_dirs``."""
    hermes_cfg = AGENTS.get("hermes-agent")
    if home is not None:
        cfg_file = home / ".hermes" / "config.yaml"
    else:
        cfg_file = expand_path("~/.hermes/config.yaml", hermes_cfg)
    if not cfg_file.is_file():
        return False
    try:
        lines = cfg_file.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return False

    in_skills = False
    in_external = False
    skills_indent = -1
    ext_indent = -1
    for raw in lines:
        stripped = raw.split("#", 1)[0].rstrip()
        if not stripped.strip():
            continue
        indent = len(stripped) - len(stripped.lstrip(" "))
        text = stripped.strip()
        if not in_skills:
            if text.startswith("skills:"):
                in_skills = True
                skills_indent = indent
            continue
        if indent <= skills_indent:
            break
        if not in_external:
            if text.startswith("external_dirs:"):
                rest = text[len("external_dirs:"):].strip()
                if rest.startswith("[") and ".agents/skills" in rest:
                    return True
                in_external = True
                ext_indent = indent
            continue
        if indent <= ext_indent and not text.startswith("- "):
            in_external = False
            continue
        if ".agents/skills" in text:
            return True
    return False


def get_agent_config(agent: str) -> AgentConfig | None:
    """Get configuration for an agent by ID or alias (e.g. ``"claude-code"``, ``"agy"``)."""
    return AGENTS.get(canonical_agent_id(agent))


def validate_agent(agent: str) -> bool:
    """Check if an agent ID or alias resolves to a supported agent."""
    return canonical_agent_id(agent) in AGENTS


def get_project_skills_dir(agent: str, cwd: Path | None = None) -> Path | None:
    """Project-level skills directory for an agent, or None if the agent is unknown."""
    config = get_agent_config(agent)
    if not config:
        return None
    base = cwd or Path.cwd()
    return base / config["project_dir"]


def get_global_skills_dir(agent: str) -> Path | None:
    """Global (user-level) skills directory an install writes to, or None if unknown."""
    config = get_agent_config(agent)
    if not config:
        return None
    win_dir = config.get("global_dir_windows")
    if win_dir and os.name == "nt":
        return Path(os.path.expandvars(win_dir))
    return expand_path(config["global_dir"], config)


def get_all_global_skills_dirs(agent: str) -> list[Path]:
    """The install directory plus every further user-level directory the agent reads."""
    config = get_agent_config(agent)
    primary = get_global_skills_dir(agent)
    if not config or primary is None:
        return []
    dirs = [primary]
    for extra in config.get("extra_global_dirs", []):
        path = expand_path(extra, config)
        if path not in dirs:
            dirs.append(path)
    return dirs


def get_readable_global_skills_dirs(agent: str) -> list[Path]:
    """All user-level directories ``agent`` reads, including ``~/.agents/skills`` when enabled.

    Kept separate from ``get_all_global_skills_dirs`` so ``delete_skill.py`` does not
    remove entries from the shared ``~/.agents/skills`` root when targeting one agent.
    """
    config = get_agent_config(agent)
    if not config:
        return []
    dirs = list(get_all_global_skills_dirs(agent))
    reads_shared = bool(config.get("reads_shared_global"))
    if config["name"] == "hermes-agent" and hermes_reads_shared_global():
        reads_shared = True
    if reads_shared:
        shared = expand_path(SHARED_GLOBAL)
        if shared not in dirs:
            dirs.append(shared)
    return dirs


def get_all_project_skills_dirs(agent: str, cwd: Path | None = None) -> list[Path]:
    """Primary project skills directory plus any legacy/extra project dirs ``agent`` reads."""
    config = get_agent_config(agent)
    primary = get_project_skills_dir(agent, cwd)
    if not config or primary is None:
        return []
    base = cwd or Path.cwd()
    dirs = [primary]
    for extra in config.get("extra_project_dirs", []):
        path = base / extra
        if path not in dirs:
            dirs.append(path)
    return dirs


def detect_installed_agents(cwd: Path | None = None) -> list[str]:
    """IDs of agents whose home directory or project marker exists on this system."""
    base = cwd or Path.cwd()
    installed = []
    for agent_id, config in AGENTS.items():
        candidates = [expand_path(p, config) for p in config["detect_paths"]]
        candidates += [base / marker for marker in config.get("detect_project_markers", [])]
        if any(path.exists() for path in candidates):
            installed.append(agent_id)
    return installed


def get_skills_dir(agent: str, scope: str, cwd: Path | None = None) -> Path | None:
    """Skills directory for an agent and scope (``"project"`` or ``"global"``)."""
    if scope == "project":
        return get_project_skills_dir(agent, cwd)
    if scope == "global":
        return get_global_skills_dir(agent)
    return None


def find_skill_in_agent(
    name: str,
    agent: str,
    scope: str | None = None,
    cwd: Path | None = None
) -> tuple[Path | None, str | None]:
    """Find a skill by name in an agent's skills directories.

    Args:
        name: Skill name (directory name); a match needs a SKILL.md inside
        agent: Agent ID
        scope: Specific scope to search, or None for both
        cwd: Working directory for project scope

    Returns:
        Tuple of (skill_path, scope_name) or (None, None) if not found
    """
    scopes_to_check = []
    if scope is None or scope == "global":
        global_dir = get_skills_dir(agent, "global")
        if global_dir:
            scopes_to_check.append(("global", global_dir))
    if scope is None or scope == "project":
        project_dir = get_skills_dir(agent, "project", cwd)
        if project_dir:
            scopes_to_check.append(("project", project_dir))

    for scope_name, skills_dir in scopes_to_check:
        skill_path = skills_dir / name
        if skill_path.exists() and (skill_path / "SKILL.md").exists():
            return skill_path, scope_name

    return None, None


def resolve_skill(
    name: str | None = None,
    *,
    agent: str | None = None,
    scope: str | None = None,
    path: Path | None = None,
    cwd: Path | None = None,
    claude_finder=None,
) -> tuple[Path | None, str | None, str | None]:
    """Resolve a skill by explicit path, by agent+scope, or in Claude Code scopes.

    Returns ``(skill_dir, scope_label, error_message)``.
    """
    if path is not None:
        target = Path(os.path.abspath(Path(path).expanduser()))
        if target.is_file() and target.name == "SKILL.md":
            target = target.parent
        if not target.is_dir():
            return None, None, f"Skill path does not exist or is not a directory: {target}"
        if not (target / "SKILL.md").is_file():
            return None, None, f"No SKILL.md found in {target}"
        return target, "path", None

    if not name:
        return None, None, "Either skill name or --path is required"

    if agent is not None:
        if not validate_agent(agent):
            valid = ", ".join(sorted(AGENTS))
            return None, None, f"Unknown agent '{agent}'. Valid agents: {valid}"
        norm_scope = "global" if scope == "user" else scope
        if norm_scope not in (None, "global", "project"):
            return None, None, f"Invalid scope '{scope}' for agent '{agent}'"
        candidates: list[tuple[str, Path]] = []
        if norm_scope in (None, "global"):
            for global_dir in get_readable_global_skills_dirs(agent):
                candidates.append(("global", global_dir))
        if norm_scope in (None, "project"):
            for project_dir in get_all_project_skills_dirs(agent, cwd):
                candidates.append(("project", project_dir))
        for scope_name, skills_dir in candidates:
            skill_path = skills_dir / name
            if skill_path.exists() and (skill_path / "SKILL.md").is_file():
                return skill_path, scope_name, None
        scope_msg = f" in {norm_scope} scope" if norm_scope else ""
        return None, None, f"Skill '{name}' not found for agent '{agent}'{scope_msg}"

    if claude_finder is None:
        from claude_scopes import find_skill as claude_finder

    claude_scope = "user" if scope == "global" else scope
    if claude_scope not in (None, "user", "project"):
        return None, None, f"Invalid scope '{scope}'"
    skill_path, found_scope = claude_finder(name, claude_scope)
    if not skill_path:
        scope_msg = f" in {claude_scope} scope" if claude_scope else " in user or project scope"
        return None, None, f"Skill '{name}' not found{scope_msg}"
    return skill_path, found_scope, None


def agents_sharing_dir(skills_dir: Path, cwd: Path | None = None) -> list[str]:
    """Agent IDs whose global or project skills directory is ``skills_dir``.

    Several agents read the same directory (for example ``~/.agents/skills``), so a
    change there affects all of them.
    """
    wanted = os.path.abspath(skills_dir)
    sharing = []
    for agent in AGENTS:
        dirs = [*get_readable_global_skills_dirs(agent), *get_all_project_skills_dirs(agent, cwd)]
        if any(os.path.abspath(d) == wanted for d in dirs):
            sharing.append(agent)
    return sharing
