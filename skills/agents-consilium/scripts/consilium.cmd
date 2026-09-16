@echo off
rem consilium.cmd — Windows-native entry point for agents-consilium.
rem
rem Pure-Python subcommands (sessions, quota) run directly on Windows.
rem review/delegate are bash pipelines and require Git Bash, MSYS2, or WSL;
rem this shim forwards them to `bash` when one is on PATH.
setlocal

set "SCRIPT_DIR=%~dp0"
set "LIB_DIR=%SCRIPT_DIR%lib"

if "%~1"=="" goto usage

set "CMD=%~1"
shift

if /i "%CMD%"=="sessions" goto python_lib
if /i "%CMD%"=="history" goto python_lib
if /i "%CMD%"=="quota"   goto python_lib
if /i "%CMD%"=="review"   goto bash_passthrough
if /i "%CMD%"=="delegate" goto bash_passthrough
if /i "%CMD%"=="-h" goto usage
if /i "%CMD%"=="--help" goto usage
if /i "%CMD%"=="--list-agents" goto bash_passthrough

echo Error: unknown command: %CMD% 1>&2
exit /b 5

:python_lib
rem Prefer python3 (python.org, py launcher shims), fall back to python.
where python3 >nul 2>nul && (set "PY=python3") || (set "PY=python")
if /i "%CMD%"=="quota" (set "MOD=quota.py") else (set "MOD=sessions.py")
"%PY%" "%LIB_DIR%\%MOD%" %*
exit /b %ERRORLEVEL%

:bash_passthrough
where bash >nul 2>nul || (
    echo Error: 'consilium %CMD%' needs bash. Install Git for Windows ^(Git Bash^) 1>&2
    echo or use WSL, then run: bash "%SCRIPT_DIR%consilium" %CMD% ... 1>&2
    exit /b 5
)
bash "%SCRIPT_DIR%consilium" %CMD% %*
exit /b %ERRORLEVEL%

:usage
echo consilium — multi-agent review and session-history CLI (Windows shim)
echo.
echo   consilium sessions roots^|list^|grep^|show^|turns^|flags^|stats [...]
echo   consilium quota [all^|codex^|grok]
echo   consilium review^|delegate ...   (runs through bash: Git Bash / MSYS2 / WSL)
echo.
echo Full help: bash "%SCRIPT_DIR%consilium" --help
exit /b 0
