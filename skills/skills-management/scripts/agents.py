#!/usr/bin/env python3
"""Shared agent definitions for multi-agent skill management.

The single source of truth for where each AI coding agent reads Agent Skills.

Baseline: the Skills CLI registry, ``src/agents.ts`` in vercel-labs/skills at
commit b716f9d (2026-11-12), https://github.com/vercel-labs/skills/blob/b716f9dc2ba36b6aa8f0080615e5a3a6caeac63b/src/agents.ts
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
    _agent("adal", "AdaL", ".adal/skills", "~/.adal/skills", ["~/.adal"]),
    _agent("aider-desk", "AiderDesk", ".aider-desk/skills", "~/.aider-desk/skills", ["~/.aider-desk"]),
    _agent("amp", "Amp", SHARED_PROJECT, SHARED_GLOBAL, ["~/.config/amp"],
           extra_global_dirs=["~/.config/agents/skills", "~/.config/amp/skills"],
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
           source=DOCS_NOV26 + "https://antigravity.google/docs/skills; agy-customizations SKILL.md"),
    _agent("antigravity-cli", "Antigravity CLI", SHARED_PROJECT, "~/.gemini/config/skills",
           ["~/.gemini/antigravity-cli"],
           extra_project_dirs=[".agent/skills", "_agents/skills", "_agent/skills"],
           extra_global_dirs=["~/.gemini/antigravity-cli/skills", "~/.gemini/skills"],
           reads_shared_global=True,
           source=DOCS_NOV26 + "https://antigravity.google/docs/skills; agy 1.5.16 changelog; " + UPSTREAM + " (fe7ff9a)"),
    _agent("augment", "Augment", ".augment/skills", "~/.augment/skills", ["~/.augment"]),
    _agent("autohand-code", "Autohand Code CLI", ".autohand/skills", "~/.autohand/skills",
           ["~/.autohand"], home_env=("AUTOHAND_HOME", "~/.autohand")),
    _agent("bob", "IBM Bob", ".bob/skills", "~/.bob/skills", ["~/.bob"]),
    _agent("claude-code", "Claude Code", ".claude/skills", "~/.claude/skills", ["~/.claude"],
           home_env=("CLAUDE_CONFIG_DIR", "~/.claude"),
           source=DOCS + "https://code.claude.com/docs/en/skills; CLAUDE_CONFIG_DIR from " + UPSTREAM),
    # Deliberately differs from upstream, which treats Cline as universal (#440, #441):
    # Cline's docs list only .cline/skills, .clinerules/skills, .claude/skills and
    # ~/.cline/skills, and never .agents/skills.
    _agent("cline", "Cline", ".cline/skills", "~/.cline/skills", ["~/.cline"],
           source=DOCS + "https://docs.cline.bot/customization/skills"),
    _agent("codearts-agent", "CodeArts Agent", ".codeartsdoer/skills", "~/.codeartsdoer/skills",
           ["~/.codeartsdoer"]),
    _agent("codebuddy", "CodeBuddy", ".codebuddy/skills", "~/.codebuddy/skills", ["~/.codebuddy"],
           detect_project_markers=[".codebuddy"]),
    _agent("codemaker", "Codemaker", ".codemaker/skills", "~/.codemaker/skills", ["~/.codemaker"]),
    _agent("codestudio", "Code Studio", ".codestudio/skills", "~/.codestudio/skills", ["~/.codestudio"]),
    _agent("codex", "Codex", SHARED_PROJECT, SHARED_GLOBAL, ["~/.codex", "/etc/codex"],
           home_env=("CODEX_HOME", "~/.codex"),
           source=DOCS + "https://learn.chatgpt.com/docs/build-skills"),
    _agent("command-code", "Command Code", ".commandcode/skills", "~/.commandcode/skills",
           ["~/.commandcode"]),
    _agent("continue", "Continue", ".continue/skills", "~/.continue/skills", ["~/.continue"],
           detect_project_markers=[".continue"]),
    _agent("cortex", "Cortex Code", ".cortex/skills", "~/.snowflake/cortex/skills",
           ["~/.snowflake/cortex"]),
    _agent("crush", "Crush", ".crush/skills", "~/.config/crush/skills", ["~/.config/crush"]),
    _agent("cursor", "Cursor", SHARED_PROJECT, SHARED_GLOBAL, ["~/.cursor"],
           extra_global_dirs=["~/.cursor/skills"],
           home_env=("CURSOR_CONFIG_DIR", "~/.cursor"),
           source=DOCS_NOV26 + "https://cursor.com/docs/context/skills; porch cursor_config.py"),
    _agent("deepagents", "Deep Agents", SHARED_PROJECT, SHARED_GLOBAL, ["~/.deepagents"],
           extra_global_dirs=["~/.deepagents/agent/skills"]),
    # Devin CLI reads .agents/skills and .devin/skills in a project, and
    # ~/.agents/skills and ~/.config/devin/skills globally; ~/.devin/skills is not
    # a documented location. The shared project dir avoids a second copy.
    _agent("devin", "Devin CLI / Desktop", SHARED_PROJECT, "~/.config/devin/skills",
           ["~/.config/devin"], global_dir_windows="%APPDATA%\\devin\\skills",
           reads_shared_global=True,
           source=DOCS + "https://docs.devin.ai/cli/extensibility/skills/overview"),
    _agent("dexto", "Dexto", SHARED_PROJECT, SHARED_GLOBAL, ["~/.dexto"]),
    # Droid reads .agents/skills and ~/.agents/skills as compatibility locations;
    # ~/.factory/skills holds skills placed by earlier installers.
    _agent("droid", "Droid", SHARED_PROJECT, SHARED_GLOBAL, ["~/.factory"],
           extra_global_dirs=["~/.factory/skills"],
           source=DOCS + "https://docs.factory.com/cli/configuration/skills"),
    _agent("firebender", "Firebender", SHARED_PROJECT, SHARED_GLOBAL, ["~/.firebender"],
           extra_global_dirs=["~/.firebender/skills"]),
    _agent("forgecode", "ForgeCode", ".forge/skills", "~/.forge/skills", ["~/.forge"]),
    _agent("fx", "fx", SHARED_PROJECT, SHARED_GLOBAL, ["~/.fx"]),
    _agent("gemini-cli", "Gemini CLI", SHARED_PROJECT, SHARED_GLOBAL, ["~/.gemini"],
           extra_global_dirs=["~/.gemini/skills"],
           source=DOCS + "https://geminicli.com/docs/cli/skills/"),
    _agent("github-copilot", "GitHub Copilot", SHARED_PROJECT, SHARED_GLOBAL, ["~/.copilot"],
           extra_global_dirs=["~/.copilot/skills"],
           source=DOCS + "https://docs.github.com/en/copilot/concepts/agents/about-agent-skills"),
    # Goose 1.25+ (Summon extension) recommends .agents/skills and ~/.agents/skills;
    # ~/.config/goose/skills is the 1.16-1.24 location. Upstream still uses .goose/skills.
    _agent("goose", "Goose", SHARED_PROJECT, SHARED_GLOBAL, ["~/.config/goose"],
           extra_global_dirs=["~/.config/goose/skills"],
           source=DOCS + "https://goose-docs.ai/docs/guides/context-engineering/using-skills"),
    # Grok reads ~/.agents/skills too, but not a project .agents/skills. GROK_HOME
    # comes from upstream only; the xAI page does not mention it.
    _agent("grok", "Grok Build", ".grok/skills", "~/.grok/skills", ["~/.grok"],
           home_env=("GROK_HOME", "~/.grok"),
           reads_shared_global=True,
           source=DOCS + "https://docs.x.ai/build/features/skills-plugins-marketplaces; " + UPSTREAM),
    # Hermes reads ~/.agents/skills only when listed in skills.external_dirs, and
    # project skills only in a repository trusted with `hermes skills trust`.
    # HERMES_HOME (profile home) comes from upstream.
    _agent("hermes-agent", "Hermes Agent", ".hermes/skills", "~/.hermes/skills", ["~/.hermes"],
           home_env=("HERMES_HOME", "~/.hermes"),
           supports_nested_categories=True,
           source=DOCS_NOV26 + "https://hermes-agent.nousresearch.com/docs/user-guide/features/skills; " + UPSTREAM),
    _agent("iflow-cli", "iFlow CLI", ".iflow/skills", "~/.iflow/skills", ["~/.iflow"]),
    _agent("inference-sh", "inference.sh", ".inferencesh/skills", "~/.inferencesh/skills",
           ["~/.inferencesh"]),
    _agent("jazz", "Jazz", ".jazz/skills", "~/.jazz/skills", ["~/.jazz"],
           detect_project_markers=[".jazz"]),
    _agent("junie", "Junie", ".junie/skills", "~/.junie/skills", ["~/.junie"]),
    # .kilocode is Kilo's legacy config directory.
    _agent("kilo", "Kilo Code", SHARED_PROJECT, SHARED_GLOBAL, ["~/.kilo", "~/.kilocode"],
           extra_global_dirs=["~/.kilo/skills", "~/.kilocode/skills"],
           source=DOCS + "https://kilo.ai/docs/customize/skills; .kilocode from " + UPSTREAM),
    _agent("kimchi", "Kimchi", ".kimchi/skills", "~/.config/kimchi/harness/skills",
           ["~/.config/kimchi"]),
    # Renamed upstream from kimi-cli (eaad526); global dir moved off ~/.config/agents/skills.
    _agent("kimi-code-cli", "Kimi Code CLI", SHARED_PROJECT, SHARED_GLOBAL,
           ["~/.kimi-code", "~/.kimi"],
           extra_global_dirs=["~/.config/agents/skills", "~/.kimi/skills"],
           home_env=("KIMI_CODE_HOME", "~/.kimi-code"),
           source=DOCS_NOV26 + "https://moonshotai.github.io/kimi-cli/en/customization/skills.html; "
           + UPSTREAM + " (eaad526)"),
    _agent("kiro-cli", "Kiro CLI", ".kiro/skills", "~/.kiro/skills", ["~/.kiro"]),
    _agent("kode", "Kode", ".kode/skills", "~/.kode/skills", ["~/.kode"]),
    _agent("lingma", "Lingma", ".lingma/skills", "~/.lingma/skills", ["~/.lingma"]),
    _agent("loaf", "Loaf", SHARED_PROJECT, SHARED_GLOBAL, ["~/.loaf"]),
    _agent("mcpjam", "MCPJam", ".mcpjam/skills", "~/.mcpjam/skills", ["~/.mcpjam"]),
    _agent("minimax-code", "MiniMax Code", ".minimax/skills", "~/.minimax/skills",
           ["~/.minimax", "/Applications/MiniMax Code.app"]),
    _agent("mistral-vibe", "Mistral Vibe", ".vibe/skills", "~/.vibe/skills", ["~/.vibe"],
           home_env=("VIBE_HOME", "~/.vibe")),
    _agent("moxby", "Moxby", ".moxby/skills", "~/.moxby/skills", ["~/.moxby"]),
    _agent("mux", "Mux", ".mux/skills", "~/.mux/skills", ["~/.mux"]),
    _agent("neovate", "Neovate", ".neovate/skills", "~/.neovate/skills", ["~/.neovate"]),
    _agent("omp", "Oh My Pi", ".omp/skills", "~/.omp/agent/skills", ["~/.omp", "~/.omp/agent"],
           extra_project_dirs=[SHARED_PROJECT],
           extra_global_dirs=["~/.omp/skills", "~/.omp/agent/managed-skills"],
           reads_shared_global=True,
           source=DOCS_NOV26 + "https://github.com/can1357/oh-my-pi"),
    _agent("ona", "Ona", ".ona/skills", "~/.ona/skills", ["~/.ona"]),
    # The project dir is the repository's own skills/ folder; ~/.clawdbot and
    # ~/.moltbot are pre-rename homes (upstream reads the first that exists).
    _agent("openclaw", "OpenClaw", "skills", "~/.openclaw/skills",
           ["~/.openclaw", "~/.clawdbot", "~/.moltbot"],
           extra_global_dirs=["~/.clawdbot/skills", "~/.moltbot/skills"]),
    _agent("opencode", "OpenCode", SHARED_PROJECT, SHARED_GLOBAL, ["~/.config/opencode"],
           extra_global_dirs=["~/.config/opencode/skills"],
           source=DOCS + "https://opencode.ai/docs/skills/"),
    _agent("openhands", "OpenHands", ".openhands/skills", "~/.openhands/skills", ["~/.openhands"]),
    # Pi reads .agents/skills up the tree and ~/.agents/skills globally
    # (https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/skills.md).
    _agent("pi", "Pi", SHARED_PROJECT, SHARED_GLOBAL, ["~/.pi/agent"],
           extra_global_dirs=["~/.pi/agent/skills"],
           source=UPSTREAM + " (2a286c7); pi-mono docs/skills.md"),
    _agent("pochi", "Pochi", ".pochi/skills", "~/.pochi/skills", ["~/.pochi"]),
    _agent("posit-assistant", "Posit Assistant", ".posit/assistant/skills",
           "~/.posit/assistant/skills", ["~/.posit/assistant", "~/.positai"]),
    _agent("qoder", "Qoder", ".qoder/skills", "~/.qoder/skills", ["~/.qoder"]),
    _agent("qoder-cn", "Qoder CN", ".qoder/skills", "~/.qoder-cn/skills", ["~/.qoder-cn"]),
    _agent("qwen-code", "Qwen Code", ".qwen/skills", "~/.qwen/skills", ["~/.qwen"]),
    _agent("reasonix", "Reasonix", ".reasonix/skills", "~/.reasonix/skills", ["~/.reasonix"],
           home_env=("REASONIX_HOME", "~/.reasonix"),
           global_dir_windows="%APPDATA%\\reasonix\\skills"),
    # Replit is detected by a project's .replit file, not by a home directory. Its
    # docs describe only project skills (/.agents/skills); the global dir is upstream's.
    _agent("replit", "Replit", SHARED_PROJECT, SHARED_GLOBAL, [],
           extra_global_dirs=["~/.config/agents/skills"], detect_project_markers=[".replit"],
           source=DOCS + "https://docs.replit.com/core-concepts/agent/skills; global from " + UPSTREAM),
    _agent("roo", "Roo Code", ".roo/skills", "~/.roo/skills", ["~/.roo"]),
    _agent("rovodev", "Rovo Dev", ".rovodev/skills", "~/.rovodev/skills", ["~/.rovodev"]),
    _agent("sarvam-code", "Sarvam Code", SHARED_PROJECT, SHARED_GLOBAL, ["~/.sarvam"],
           home_env=("SARVAM_HOME", "~/.sarvam")),
    _agent("tabnine-cli", "Tabnine CLI", ".tabnine/agent/skills", "~/.tabnine/agent/skills",
           ["~/.tabnine"]),
    _agent("terramind", "Terramind", ".terramind/skills", "~/.terramind/skills", ["~/.terramind"]),
    _agent("tinycloud", "Tinycloud", ".tinycloud/skills", "~/.tinycloud/skills", ["~/.tinycloud"]),
    _agent("trae", "Trae", ".trae/skills", "~/.trae/skills", ["~/.trae"]),
    _agent("trae-cn", "Trae CN", ".trae/skills", "~/.trae-cn/skills", ["~/.trae-cn"]),
    _agent("warp", "Warp", SHARED_PROJECT, SHARED_GLOBAL, ["~/.warp"]),
    # Windsurf docs now redirect to Devin Desktop, which still reads .windsurf/skills
    # (legacy) and ~/.codeium/<channel>/skills.
    _agent("windsurf", "Windsurf", ".windsurf/skills", "~/.codeium/windsurf/skills",
           ["~/.codeium/windsurf"],
           source=DOCS + "https://docs.devin.ai/cli/extensibility/skills/overview; " + UPSTREAM),
    _agent("zcode", "ZCode", ".zcode/skills", "~/.zcode/skills",
           ["~/.zcode", "/Applications/ZCode.app"]),
    _agent("zed", "Zed", SHARED_PROJECT, SHARED_GLOBAL, ["~/.config/zed"],
           source=DOCS + "https://zed.dev/docs/ai/skills"),
    _agent("zencoder", "Zencoder", ".zencoder/skills", "~/.zencoder/skills", ["~/.zencoder"]),
    _agent("zenflow", "Zenflow", ".zencoder/skills", "~/.zencoder/skills", ["~/.zencoder"]),
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
