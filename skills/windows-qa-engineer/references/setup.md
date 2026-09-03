# Setup: UFO + MCP Server

## Table of Contents
- [Install UFO](#install-ufo)
- [Configure MCP in Claude Code](#configure-mcp-in-claude-code)
- [Verify](#verify)
- [Backend Selection](#backend-selection)

## Install UFO

Prerequisites: Windows 11 or Windows Server 2025 with Desktop Experience, Python 3.10.x, and Git. The pinned UFO requirements currently need Python 3.10 on Windows: `faiss-cpu==1.8.0` is unavailable for Python 3.13 and `pandas==1.4.3` is unavailable for Python 3.11.

```powershell
cd $env:USERPROFILE
git clone https://github.com/microsoft/UFO.git
cd UFO
py -3.10 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Quick check:
```powershell
python -c "from ufo.client.mcp.local_servers import load_all_servers; load_all_servers(); print('OK')"
python -c "from ufo.client.mcp.mcp_registry import MCPRegistry; print(MCPRegistry.list())"
```

Expected: UICollector, HostUIExecutor, AppUIExecutor registered.

## Configure MCP in Claude Code

Add to your project `.mcp.json`:

```json
{
  "mcpServers": {
    "ufo-windows-qa": {
      "type": "stdio",
      "command": "C:\\Users\\<you>\\UFO\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\path\\to\\windows-qa-engineer\\scripts\\ufo_windows_qa_mcp_server.py"
      ],
      "env": {
        "UFO_ROOT": "C:\\Users\\<you>\\UFO",
        "PYTHONPATH": "C:\\Users\\<you>\\UFO",
        "CONTROL_BACKEND": "uia",
        "MAXIMIZE_WINDOW": "false",
        "SHOW_VISUAL_OUTLINE_ON_SCREEN": "true",
        "RUN_CONFIGS": "true"
      }
    }
  }
}
```

Replace `<you>` and the skill path with absolute paths, restart the MCP client, and confirm that the tools are available.

## Verify

Run the doctor script from any directory; it selects UFO's venv and working directory automatically:
```powershell
.\.claude\skills\windows-qa-engineer\scripts\doctor.ps1
```

Or check in Claude Code that these tools appear:
`get_desktop_app_info`, `select_application_window`, `get_app_window_controls_info`,
`click_input`, `set_edit_text`, `texts`, `capture_window_screenshot`,
`qa_refresh_and_list_windows`, `qa_refresh_controls`, `qa_wait_for_text_contains`.

The doctor verifies imports and MCP registration but cannot create an interactive desktop. For an end-to-end check, run the MCP client and the application under test in the same logged-in Windows session, call `qa_refresh_and_list_windows()`, select a visible app such as Notepad, and capture its screenshot. An empty window list from SSH or a service session is expected and does not verify desktop automation.

The bundled smoke test performs that complete Notepad workflow and writes a PNG plus JSON report under the user's temporary directory:

```powershell
& "$env:USERPROFILE\UFO\.venv\Scripts\python.exe" `
  "<skill-dir>\scripts\interactive_smoke_test.py" `
  --project-dir "<project-root>"
```

Run it from a terminal inside the same interactive desktop session, not through SSH or a service.

## Backend Selection

- `CONTROL_BACKEND=uia` (default, recommended for WinForms/WPF stability)
- `CONTROL_BACKEND=win32` (fallback if UIA fails for a specific SUT)

Set via the `env` block in `.mcp.json`.
