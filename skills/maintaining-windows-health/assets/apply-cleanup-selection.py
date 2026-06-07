#!/usr/bin/env python3
r"""
apply-cleanup-selection.py — the ONLY sanctioned way to apply a cleanup
selection produced by render-cleanup-plan.py on Windows 11.

Why this exists
---------------
The maintaining-windows-health skill splits scan-and-plan from apply on purpose:
the user picks items in the HTML UI, the server writes a selection JSON, and
THIS script reads that JSON and executes each item's `command`. The skill
forbids hand-rolled `Remove-Item` blocks during apply, because they're how you
end up deleting items the user explicitly unchecked. The single-source-of-truth
is the selection JSON written by the UI server — nothing else.

This is a Windows-specific REWRITE of the macOS validator, NOT a translation.
The macOS validator's safety rested on POSIX assumptions that are individually
FALSE on Windows: a single root `/`, case-sensitivity, one path separator, `~`
HOME expansion, no drive letters, no UNC/device paths, no Alternate Data
Streams, no 8.3 short names, no non-filesystem providers (HKLM:, Env:, Cert:).
A naive "swap the prefixes" port silently fails open. So the validator below is
rebuilt around NTFS path canonicalization (`ntpath` mirrors Win32 `GetFullPath`
behavior even when this script is unit-tested on macOS).

Safety model (what `validate_command` enforces)
-----------------------------------------------
1. Reject command chaining / injection metacharacters outright: ; | & ` $( @( ::
   > < newline. PowerShell's metacharacter surface is far wider than bash, so a
   `command` like `docker ps; Remove-Item C:\Windows -Recurse` must never pass
   just because it starts with a trusted wrapper.
2. Two-tier wrapper model (Windows-specific):
   - SAFE wrappers (self-policing AND non-destructive): npm/pnpm/yarn/dotnet/
     nuget/pip/uv/cargo/go/gradle/mvn/docker/winget/cleanmgr/Clear-RecycleBin…
     -> trusted, no protection required.
   - TOOL wrappers (self-policing) whose destructive subcommands are
     irreversible: vssadmin delete/resize, Dism …/ResetBase, wevtutil cl,
     pnputil /delete-driver, powercfg /h off, Disable-ComputerRestore
     -> trusted to target correctly, BUT require `protected:true` +
     `protected_overrides` because the effect is irreversible. (The macOS model
     "wrapper == safe" is false on Windows.)
3. Bare delete (Remove-Item/del/rd/rmdir/erase): every path token is
   env-expanded -> rejected if it is a UNC/device path (\\?\, \\.\, \\server),
   an 8.3 short name (PROGRA~1), a non-filesystem provider (HKLM:, Env:, …), or
   carries an Alternate Data Stream (file.txt:hidden) -> canonicalized with
   ntpath.normpath + trailing dot/space stripping (Win32 behavior) -> required
   to be drive-absolute (`<letter>:\…`) and never a bare drive root -> classified
   against an allow-list and a deny-list using LONGEST-PREFIX-WINS so carve-outs
   resolve correctly (e.g. C:\Windows is denied but C:\Windows\Temp is allowed;
   C:\Users\me is allowed but C:\Users\me\.ssh is denied).
4. Non-FileSystem PowerShell providers are refused for any delete verb —
   registry "cleaning" is explicitly unsupported by Microsoft and out of scope.

Operations log: Mole-compatible TSV appended to
%LOCALAPPDATA%\win-health\operations.log.

Usage
-----
    apply-cleanup-selection.py <selection.json>                 # apply
    apply-cleanup-selection.py <selection.json> --dry-run
    apply-cleanup-selection.py <selection.json> --scan-root D:\projects   # repeatable

Exit codes
----------
    0  - all items applied (or dry-run completed)
    1  - bad input or fatal validation error
    2  - one or more items failed (others may have succeeded)
"""
from __future__ import annotations

import argparse
import json
import ntpath
import os
import re
import shlex
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Operations log — %LOCALAPPDATA%\win-health\operations.log (fallback to ~).
# ---------------------------------------------------------------------------
def _op_log_path() -> Path:
    base = os.environ.get("LOCALAPPDATA")
    if base:
        return Path(base) / "win-health" / "operations.log"
    return Path.home() / "AppData" / "Local" / "win-health" / "operations.log"


# ---------------------------------------------------------------------------
# Command classification heads (lowercased).
# ---------------------------------------------------------------------------
# Self-policing AND non-destructive to user data. Trusted, no protection needed.
SAFE_WRAPPER_HEADS = {
    "npm", "pnpm", "yarn", "bun",
    "dotnet", "nuget",
    "pip", "pip3", "uv", "poetry", "pipenv",
    "cargo", "go",
    "gradle", "gradlew", "gradlew.bat",
    "mvn", "maven",
    "docker", "docker-compose",
    "winget",
    "cleanmgr", "cleanmgr.exe",
    "clear-recyclebin",
    "delete-deliveryoptimizationcache",
    "optimize-vhd", "optimize-volume",
    "brew",  # harmless cross-platform passthrough (no-op on Windows)
}

# Self-policing tools whose *destructive* subcommands are irreversible.
# Recognized as wrappers (so they skip bare-path validation) but flagged as
# requiring protection when the subcommand is destructive.
TOOL_WRAPPER_HEADS = {
    "dism", "dism.exe",
    "vssadmin",
    "wevtutil",
    "pnputil", "pnputil.exe",
    "powercfg",
    "disable-computerrestore",
    "checkpoint-computer",
}

# Bare delete verbs / aliases (filesystem). Each gets full path validation.
BARE_DELETE_HEADS = {
    "remove-item", "remove-item.exe", "ri", "rm", "rmdir", "rd", "del", "erase",
}

# Substrings that, if present anywhere in the command, indicate chaining,
# redirection, sub-expression evaluation, .NET static calls, or device/provider
# qualifiers. Any of these => reject. (`&&`/`||` are covered by `&`/`|`.)
FORBIDDEN_SUBSTRINGS = (";", "|", "&", "`", "$(", "@(", "::", ">", "<", "\n", "\r")

# Markers of an irreversible TOOL-wrapper invocation (lowercased command).
_DESTRUCTIVE_TOOL_PATTERNS = (
    ("vssadmin", "delete"),
    ("vssadmin", "resize"),
    ("dism", "/resetbase"),
    ("wevtutil", "cl "),
    ("wevtutil", "clear-log"),
    ("pnputil", "/delete-driver"),
    ("pnputil", "-d "),
    ("powercfg", "/h off"),
    ("powercfg", "/hibernate off"),
    ("disable-computerrestore", ""),
)


# ---------------------------------------------------------------------------
# Path helpers (ntpath everywhere so behavior matches Win32 even on macOS CI).
# ---------------------------------------------------------------------------
def _env(name: str, default: str = "") -> str:
    return os.environ.get(name, default)


def _expandvars(token: str) -> str:
    """Expand %VAR% / $VAR using ntpath semantics (Windows-style), regardless
    of the host OS this validator runs on (so unit tests on macOS match)."""
    return ntpath.expandvars(token)


def _norm(path: str) -> str:
    """Canonicalize like Win32 GetFullPath: unify separators, collapse `..`/`.`,
    and strip trailing dots/spaces from every component (NTFS truncates them)."""
    p = path.replace("/", "\\")
    p = ntpath.normpath(p)
    drive, rest = ntpath.splitdrive(p)
    parts = [seg.rstrip(" .") for seg in rest.split("\\")]
    return drive + "\\".join(parts)


def _under(path_low: str, prefix_low: str) -> bool:
    """True if path_low == prefix_low or is a child of it (component-aware)."""
    if path_low == prefix_low:
        return True
    sep = "" if prefix_low.endswith("\\") else "\\"
    return path_low.startswith(prefix_low + sep)


def _allow_prefixes(scan_roots: list[str]) -> list[str]:
    sysdrive = _env("SystemDrive", "C:")
    sysroot = _env("SystemRoot", _env("windir", sysdrive + "\\Windows"))
    userprofile = _env("USERPROFILE", str(Path.home()))
    temp = _env("TEMP", _env("TMP", ""))
    localappdata = _env("LOCALAPPDATA", userprofile + "\\AppData\\Local")
    prefixes = [
        userprofile,                     # broad: most dev work lives under HOME
        sysroot + "\\Temp",              # C:\Windows\Temp carve-out inside C:\Windows
        localappdata + "\\Temp",
    ]
    if temp:
        prefixes.append(temp)
    # Extra scan roots: CLI --scan-root plus WIN_HEALTH_SCAN_ROOTS (`;`-separated).
    env_roots = _env("WIN_HEALTH_SCAN_ROOTS", "")
    for r in list(scan_roots) + [x for x in env_roots.split(";") if x.strip()]:
        prefixes.append(r)
    out = []
    for p in prefixes:
        if not p:
            continue
        out.append(_norm(_expandvars(p)).lower())
    return [p for p in out if p]


def _deny_prefixes() -> list[str]:
    sysdrive = _env("SystemDrive", "C:")
    sysroot = _env("SystemRoot", _env("windir", sysdrive + "\\Windows"))
    pf = _env("ProgramFiles", sysdrive + "\\Program Files")
    pfx86 = _env("ProgramFiles(x86)", sysdrive + "\\Program Files (x86)")
    pf6432 = _env("ProgramW6432", pf)
    programdata = _env("ProgramData", sysdrive + "\\ProgramData")
    userprofile = _env("USERPROFILE", str(Path.home()))
    appdata = _env("APPDATA", userprofile + "\\AppData\\Roaming")
    localappdata = _env("LOCALAPPDATA", userprofile + "\\AppData\\Local")
    raw = [
        # OS roots (covers System32, SysWOW64, WinSxS, DriverStore, config,
        # SoftwareDistribution, Installer, Minidump, MEMORY.DMP, Prefetch, …).
        sysroot,
        # Program installs.
        pf, pfx86, pf6432,
        programdata + "\\Microsoft",
        programdata + "\\Package Cache",
        # Boot / recovery / volume metadata.
        sysdrive + "\\$Recycle.Bin",
        sysdrive + "\\System Volume Information",
        sysdrive + "\\Recovery",
        sysdrive + "\\$WinREAgent",
        sysdrive + "\\Config.Msi",
        sysdrive + "\\PerfLogs",
        sysdrive + "\\Boot",
        sysdrive + "\\EFI",
        # Paging / hibernation / crash files (file-level).
        sysdrive + "\\pagefile.sys",
        sysdrive + "\\swapfile.sys",
        sysdrive + "\\hiberfil.sys",
        sysdrive + "\\DumpStack.log.tmp",
        # Credential / key stores under HOME (deny beats the broad HOME allow).
        userprofile + "\\.ssh",
        userprofile + "\\.gnupg",
        userprofile + "\\.aws",
        userprofile + "\\.azure",
        userprofile + "\\.kube",
        userprofile + "\\.docker",
        userprofile + "\\.netrc",
        userprofile + "\\.git-credentials",
        appdata + "\\Microsoft\\Crypto",
        appdata + "\\Microsoft\\Protect",
        appdata + "\\Microsoft\\Credentials",
        appdata + "\\Microsoft\\SystemCertificates",
        appdata + "\\gh\\hosts.yml",
        localappdata + "\\Microsoft\\Credentials",
    ]
    return [_norm(_expandvars(p)).lower() for p in raw]


def _classify(path_low: str, allow: list[str], deny: list[str]) -> tuple[str, str]:
    """Longest-prefix-wins. Returns ('deny'|'allow'|'none', matched_prefix)."""
    best_allow = max((p for p in allow if _under(path_low, p)), key=len, default=None)
    best_deny = max((p for p in deny if _under(path_low, p)), key=len, default=None)
    if best_deny is not None and (best_allow is None or len(best_deny) >= len(best_allow)):
        return "deny", best_deny
    if best_allow is not None:
        return "allow", best_allow
    return "none", ""


def _unquote(tok: str) -> str:
    if len(tok) >= 2 and tok[0] == tok[-1] and tok[0] in "\"'":
        return tok[1:-1]
    return tok


def _looks_like_path(tok: str) -> bool:
    if tok.startswith(("\\\\", "%", "$", "~")):
        return True
    if re.match(r"^[A-Za-z][A-Za-z0-9]*:", tok):  # drive (1 letter) or provider (more)
        return True
    return "\\" in tok or "/" in tok


def _validate_path_token(tok: str, allow: list[str], deny: list[str]) -> tuple[bool, str]:
    expand = _expandvars(tok)
    if expand.startswith("\\\\"):
        return False, f"UNC/device path not allowed: {tok!r}"
    if re.search(r"~\d", expand):
        return False, f"8.3 short name not allowed: {tok!r}"
    m = re.match(r"^([A-Za-z][A-Za-z0-9]*):", expand)
    if m and len(m.group(1)) > 1:
        return False, f"non-filesystem provider not allowed: {tok!r}"
    if ":" in expand[2:]:  # any colon past the drive letter == Alternate Data Stream
        return False, f"alternate data stream not allowed: {tok!r}"
    low = _norm(expand).lower()
    if not re.match(r"^[a-z]:\\", low):
        return False, f"path is not drive-absolute: {tok!r} -> {low!r}"
    if re.match(r"^[a-z]:\\?$", low):
        return False, f"refuses bare drive root: {low!r}"
    decision, matched = _classify(low, allow, deny)
    if decision == "deny":
        return False, f"targets a protected prefix ({matched!r}): {low!r}"
    if decision == "none":
        return False, f"outside allowed zones (HOME/TEMP/scan-roots): {low!r}"
    return True, ""


def _is_destructive_tool(cmd_low: str) -> bool:
    for head, needle in _DESTRUCTIVE_TOOL_PATTERNS:
        if cmd_low.startswith(head) and (needle == "" or needle in cmd_low):
            return True
    return False


def validate_command(command: str, scan_roots: list[str] | None = None
                     ) -> tuple[bool, str, bool]:
    """Return (ok, reason, requires_protection)."""
    scan_roots = scan_roots or []
    cmd = command.strip()
    if not cmd:
        return False, "empty command", False

    for bad in FORBIDDEN_SUBSTRINGS:
        if bad in cmd:
            label = bad.replace("\n", "\\n").replace("\r", "\\r")
            return False, f"command contains forbidden metacharacter {label!r}", False

    try:
        toks = [_unquote(t) for t in shlex.split(cmd, posix=False)]
    except ValueError as exc:
        return False, f"unparseable command ({exc})", False
    if not toks:
        return False, "no tokens", False

    head = toks[0].lower()
    cmd_low = cmd.lower()

    if head in SAFE_WRAPPER_HEADS:
        return True, "", False
    if head in TOOL_WRAPPER_HEADS:
        return True, "", _is_destructive_tool(cmd_low)

    if head not in BARE_DELETE_HEADS:
        return False, f"only delete verbs or vetted wrappers allowed, got {toks[0]!r}", False

    allow = _allow_prefixes(scan_roots)
    deny = _deny_prefixes()
    path_tokens = [t for t in toks[1:] if _looks_like_path(t)]
    if not path_tokens:
        return False, "delete command without a target path", False
    for t in path_tokens:
        ok, reason = _validate_path_token(t, allow, deny)
        if not ok:
            return False, reason, False
    return True, "", False


# ---------------------------------------------------------------------------
# Reporting helpers.
# ---------------------------------------------------------------------------
def human_size(num_bytes: int) -> str:
    if num_bytes is None or num_bytes == 0:
        return "0 B"
    n = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if abs(n) < 1024.0:
            return f"{int(n)} {unit}" if unit == "B" else f"{n:3.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} PB"


def log_op(action: str, path: str, size: str, status: str) -> None:
    op_log = _op_log_path()
    op_log.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    row = f"{ts}\tapply-selection\t{action}\t{path}\t{size}\t{status}\n"
    with op_log.open("a", encoding="utf-8") as f:
        f.write(row)


def _run(command: str) -> subprocess.CompletedProcess:
    """Execute one validated command via PowerShell (no profile, non-interactive)."""
    return subprocess.run(
        ["powershell.exe", "-NoProfile", "-NonInteractive",
         "-ExecutionPolicy", "Bypass", "-Command", command],
        capture_output=True, text=True, timeout=900,
    )


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description="Apply a cleanup selection JSON (Windows)")
    ap.add_argument("selection", help="path to cleanup-selection-<ts>.json")
    ap.add_argument("--dry-run", action="store_true", help="print actions, don't execute")
    ap.add_argument("--scan-root", action="append", default=[],
                    help="additional absolute root where bare deletes are allowed (repeatable)")
    ap.add_argument("--continue-on-error", action="store_true",
                    help="keep going if an item fails (default: stop on first error)")
    args = ap.parse_args(argv[1:])

    sel_path = Path(args.selection)
    if not sel_path.is_file():
        print(f"selection file not found: {sel_path}", file=sys.stderr)
        return 1
    try:
        sel = json.loads(sel_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"invalid selection JSON: {exc}", file=sys.stderr)
        return 1

    items = sel.get("selected_items", []) or []
    if not items:
        print("selected_items is empty — nothing to do", file=sys.stderr)
        return 0

    protected_overrides = set(sel.get("protected_overrides", []) or [])
    total_bytes = sum(it.get("size_bytes", 0) or 0 for it in items)

    print(f"=== Applying selection from {sel_path.name} ===")
    print(f"Items: {len(items)} | Estimated: {human_size(total_bytes)}")
    print(f"Protected overrides: {len(protected_overrides)}")
    print(f"Mode: {'DRY-RUN' if args.dry_run else 'APPLY'}")
    print()

    if not args.dry_run:
        log_op("APPLY-START", "-", "-", "START")

    ok = skipped = failed = 0

    for idx, item in enumerate(items, 1):
        item_id = item.get("id", "?")
        label = item.get("label", item_id)
        path = item.get("path", "")
        command = item.get("command")
        size_bytes = item.get("size_bytes", 0) or 0
        protected = bool(item.get("protected", False))
        prefix = f"[{idx:>2}/{len(items)}]"

        if not command:
            print(f"{prefix} SKIP (no command): {label}")
            log_op("SKIP", path or item_id, human_size(size_bytes), "NO-COMMAND")
            skipped += 1
            continue

        valid, reason, needs_protection = validate_command(command, args.scan_root)
        if not valid:
            print(f"{prefix} SKIP (validation: {reason}): {label}")
            log_op("SKIP", path or item_id, human_size(size_bytes), f"VALIDATION-FAILED:{reason}")
            skipped += 1
            continue

        effective_protected = protected or needs_protection
        if effective_protected and item_id not in protected_overrides:
            why = "protected" if protected else "irreversible-tool"
            print(f"{prefix} SKIP ({why}, not overridden): {label}")
            log_op("SKIP", path or item_id, human_size(size_bytes), "PROTECTED-NOT-OVERRIDDEN")
            skipped += 1
            continue

        flag = " [OVERRIDE]" if effective_protected else ""
        print(f"{prefix} {label}{flag} — {human_size(size_bytes)}")
        print(f"          -> {command}")

        if args.dry_run:
            ok += 1
            continue

        try:
            proc = _run(command)
            if proc.returncode == 0:
                log_op("PROTECTED-OVERRIDE" if effective_protected else "REMOVED",
                       path or item_id, human_size(size_bytes), "OK")
                ok += 1
            else:
                stderr_tail = (proc.stderr or "").strip()[-300:]
                print(f"          FAIL exit={proc.returncode}: {stderr_tail}")
                log_op("REMOVE", path or item_id, human_size(size_bytes),
                       f"FAIL-EXIT-{proc.returncode}")
                failed += 1
                if not args.continue_on_error:
                    print("Stopping on first error. Re-run with --continue-on-error to override.")
                    break
        except subprocess.TimeoutExpired:
            print("          TIMEOUT after 900s")
            log_op("REMOVE", path or item_id, human_size(size_bytes), "TIMEOUT")
            failed += 1
        except Exception as exc:
            print(f"          ERROR: {exc}")
            log_op("REMOVE", path or item_id, human_size(size_bytes), f"ERROR:{exc}")
            failed += 1

    print()
    print(f"=== Done: {ok} ok | {skipped} skipped | {failed} failed ===")
    if not args.dry_run:
        log_op("APPLY-END", "-", "-", f"OK={ok} SKIP={skipped} FAIL={failed}")
    return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
