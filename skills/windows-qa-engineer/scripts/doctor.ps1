$ErrorActionPreference = 'Stop'

Write-Host '== Windows QA + UFO Doctor ==' -ForegroundColor Cyan

$ufoRoot = if ($env:UFO_ROOT) { $env:UFO_ROOT } else { Join-Path $env:USERPROFILE 'UFO' }
$python = Join-Path $ufoRoot '.venv\Scripts\python.exe'

if (-not (Test-Path $python)) {
    throw "UFO virtual environment was not found at $python"
}

$env:UFO_ROOT = $ufoRoot
$env:PYTHONPATH = $ufoRoot

Push-Location $ufoRoot
try {
    @'
import platform
import ufo
from ufo.client.mcp.local_servers import load_all_servers
from ufo.client.mcp.mcp_registry import MCPRegistry

print("Platform:", platform.platform())
print("UFO import OK")
load_all_servers()
registered = MCPRegistry.list()
print("Registered:", registered)
for required in ("UICollector", "HostUIExecutor", "AppUIExecutor"):
    assert required in registered, f"Missing {required} in {registered}"
print("OK: all required UI servers registered")
'@ | & $python -
    if ($LASTEXITCODE -ne 0) {
        throw "UFO doctor failed with exit code $LASTEXITCODE"
    }
} finally {
    Pop-Location
}
