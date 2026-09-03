# Windows QA Engineer Skill

Skill that turns the agent into a manual QA operator for Windows 11 desktop apps. Runs on the same desktop as the SUT — no mocks, no browser-only tricks.

## Tech Stack

| Layer | Technology | Role |
|-------|-----------|------|
| **UI Automation** | [Microsoft UFO](https://github.com/microsoft/UFO) | Windows UI automation framework. Provides `ControlInspectorFacade`, `ActionExecutor`, `AppPuppeteer`, `PhotographerFacade` for real control discovery and interaction |
| **Accessibility Backend** | [UI Automation (UIA)](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32) / [Win32](https://learn.microsoft.com/en-us/windows/win32/winauto/microsoft-active-accessibility) | OS-level accessibility APIs that UFO uses to inspect and manipulate UI controls. UIA is default; Win32 available as fallback |
| **MCP Servers** | UFO `UICollector` + `HostUIExecutor` + `AppUIExecutor` | UFO's built-in MCP servers (`ufo/client/mcp/local_servers/ui_mcp_server.py`) registered via `MCPRegistry`. Provide tools: `get_desktop_app_info`, `select_application_window`, `get_app_window_controls_info`, `click_input`, `set_edit_text`, `texts`, `capture_window_screenshot`, etc. |
| **Server Composition** | [FastMCP](https://github.com/jlowin/fastmcp) `mount()` | Composes UFO's 3 MCP servers into a single stdio endpoint so Claude Code needs only one `.mcp.json` entry |
| **Protocol** | [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) over stdio | Standard protocol connecting Claude Code to UFO's automation tools |
| **Target Apps** | WinForms, WPF, UWP, Win32 | Any Windows desktop app exposing an accessibility tree in the same interactive session |

## How It Works

```
Claude Code ──stdio──▶ FastMCP server ──mount()──▶ UFO UICollector
                                       ──mount()──▶ UFO HostUIExecutor
                                       ──mount()──▶ UFO AppUIExecutor
                                                         │
                                                    UIA / Win32
                                                         │
                                                   Windows Desktop
                                                    (real SUT)
```

The skill's MCP server (`scripts/ufo_windows_qa_mcp_server.py`) imports UFO's server factories via `MCPRegistry`, mounts all three into one `FastMCP` instance, and adds QA helper tools:

- **`qa_refresh_and_list_windows`** — refresh + list in one call
- **`qa_refresh_controls`** — re-collect control tree for selected window
- **`qa_wait_for_text_contains`** — polling assertion (avoids arbitrary sleeps)

## QA Workflow

```
1. Discover windows    →  qa_refresh_and_list_windows()
2. Select SUT          →  select_application_window(id, name)
3. Screenshot baseline →  capture_window_screenshot()
4. Collect controls    →  get_app_window_controls_info(field_list=[...])
5. Interact by id/name →  click_input / set_edit_text / keyboard_input
6. Assert              →  qa_wait_for_text_contains(id, name, expected)
7. Report              →  PASS/FAIL + screenshots + execution log
```

## Requirements

- Windows 11 or Windows Server 2025 with Desktop Experience
- Python 3.10.x (required by the currently pinned pandas/faiss Windows wheels)
- [Microsoft UFO](https://github.com/microsoft/UFO) — `git clone` + `pip install -r requirements.txt`
- [FastMCP](https://pypi.org/project/fastmcp/) — `pip install fastmcp`
- [Pydantic](https://pypi.org/project/pydantic/) — comes with FastMCP

## Install

### Via Skills CLI

```bash
npx skills add CodeAlive-AI/ai-driven-development@windows-qa-engineer -g -y
```

### Manual

1. Clone this repo
2. Copy `windows-qa-engineer/` to `~/.claude/skills/`
3. Add the MCP server config to your project `.mcp.json`:

```json
{
  "mcpServers": {
    "ufo-windows-qa": {
      "type": "stdio",
      "command": "C:\\Users\\<you>\\UFO\\.venv\\Scripts\\python.exe",
      "args": ["C:\\path\\to\\windows-qa-engineer\\scripts\\ufo_windows_qa_mcp_server.py"],
      "env": {
        "UFO_ROOT": "C:\\Users\\<you>\\UFO",
        "PYTHONPATH": "C:\\Users\\<you>\\UFO",
        "CONTROL_BACKEND": "uia",
        "SHOW_VISUAL_OUTLINE_ON_SCREEN": "true"
      }
    }
  }
}
```

4. Restart the MCP client and verify that the tools appear

Run the MCP client and the application under test in the same logged-in interactive Windows desktop session. A process started through SSH, WinRM, CI, or a Windows service runs headlessly and cannot provide a usable UIA window tree or screenshot.

For an end-to-end environment check, run `scripts/interactive_smoke_test.py` with UFO's venv Python from an interactive terminal. It launches Notepad, discovers and selects its window through the MCP server, captures a PNG, and writes a machine-readable report in the user's temporary directory.

## Usage

```
/windows-qa-engineer Calculator "verify 2+2=4"
```

Or describe what to test:

> "Test the login flow on MyApp — enter admin/password, click Login, verify the welcome screen"

## Skill Contents

```
windows-qa-engineer/
├── SKILL.md                              # Workflow instructions for Claude
├── scripts/
│   ├── ufo_windows_qa_mcp_server.py      # FastMCP server (UFO mount composition)
│   └── doctor.ps1                        # Environment validation
├── references/
│   ├── setup.md                          # UFO install + MCP config
│   └── qa-workflows.md                   # Examples + locator strategy
└── assets/
    └── test-case.md                      # Test case output template
```

## License

MIT
