#!/usr/bin/env python3
"""
test_validate_command.py — adversarial unit tests for the apply-script
validator. This is the SAFETY-CORE GATE of maintaining-windows-health.

It is pure string/path logic (ntpath-based), so it runs and fully verifies the
Windows validator on ANY OS — including the macOS machine the skill is authored
on, where no NTFS volume exists. Run it before trusting the apply script:

    python3 test_validate_command.py

Exit code 0 = all cases pass; 1 = at least one regression.
"""
from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Synthetic Windows environment so the validator's allow/deny prefixes resolve
# deterministically regardless of host OS.
FAKE_ENV = {
    "SystemDrive": "C:",
    "SystemRoot": r"C:\Windows",
    "windir": r"C:\Windows",
    "ProgramFiles": r"C:\Program Files",
    "ProgramFiles(x86)": r"C:\Program Files (x86)",
    "ProgramW6432": r"C:\Program Files",
    "ProgramData": r"C:\ProgramData",
    "USERPROFILE": r"C:\Users\dev",
    "APPDATA": r"C:\Users\dev\AppData\Roaming",
    "LOCALAPPDATA": r"C:\Users\dev\AppData\Local",
    "TEMP": r"C:\Users\dev\AppData\Local\Temp",
    "TMP": r"C:\Users\dev\AppData\Local\Temp",
}


def _load_validator():
    spec = importlib.util.spec_from_file_location(
        "apply_cleanup_selection", HERE / "apply-cleanup-selection.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# Each case: (command, expect_ok, expect_requires_protection, scan_roots, note)
CASES = [
    # ---- Allowed bare deletes -------------------------------------------------
    (r"Remove-Item -LiteralPath 'C:\Users\dev\AppData\Local\Temp\foo' -Recurse -Force",
     True, False, [], "user TEMP"),
    (r'Remove-Item -LiteralPath "C:\Users\dev\Downloads\old.iso" -Force',
     True, False, [], "Downloads under HOME"),
    (r"del C:\Windows\Temp\stale.tmp", True, False, [], "C:\\Windows\\Temp carve-out"),
    (r"Remove-Item -LiteralPath '%TEMP%\bar' -Recurse", True, False, [], "env-expanded TEMP"),
    (r"Remove-Item -LiteralPath 'C:\Users\dev\source\repos\proj\node_modules' -Recurse -Force",
     True, False, [], "project artifact under HOME"),
    (r"Remove-Item -LiteralPath 'D:\projects\app\target' -Recurse",
     True, False, [r"D:\projects"], "scan-root opt-in"),

    # ---- Denied bare deletes --------------------------------------------------
    (r"Remove-Item -LiteralPath 'C:\Windows\System32\drivers\x' -Recurse",
     False, False, [], "System32"),
    (r"Remove-Item -LiteralPath 'C:\Windows\WinSxS' -Recurse", False, False, [], "WinSxS"),
    (r"Remove-Item -LiteralPath 'C:\Windows' -Recurse", False, False, [], "Windows root"),
    (r"Remove-Item -LiteralPath 'C:\Program Files\App' -Recurse", False, False, [], "Program Files"),
    (r"Remove-Item -LiteralPath 'C:\Program Files (x86)\App' -Recurse",
     False, False, [], "Program Files x86"),
    (r"Remove-Item -LiteralPath 'C:\ProgramData\Microsoft\X' -Recurse",
     False, False, [], "ProgramData\\Microsoft"),
    (r"Remove-Item -LiteralPath 'C:\ProgramData\Package Cache\X' -Recurse",
     False, False, [], "Package Cache"),
    (r"Remove-Item -LiteralPath 'C:\Users\dev\.ssh' -Recurse",
     False, False, [], "credential dir beats HOME allow"),
    (r"Remove-Item -LiteralPath 'C:\Users\dev\.aws\credentials' -Force",
     False, False, [], "AWS creds"),
    (r"Remove-Item -LiteralPath 'C:\Users\dev\AppData\Roaming\Microsoft\Protect\S-1-5' -Recurse",
     False, False, [], "DPAPI master keys"),
    (r"Remove-Item -LiteralPath 'C:\pagefile.sys' -Force", False, False, [], "pagefile"),
    (r"Remove-Item -LiteralPath 'C:\swapfile.sys' -Force", False, False, [], "swapfile"),
    (r"Remove-Item -LiteralPath 'C:\hiberfil.sys' -Force", False, False, [], "hiberfil"),
    (r"Remove-Item -LiteralPath 'C:\System Volume Information\x' -Recurse",
     False, False, [], "VSS/restore store"),
    (r"Remove-Item -LiteralPath 'C:\$Recycle.Bin\S-1-5\x' -Recurse",
     False, False, [], "recycle bin internals"),
    (r"Remove-Item -LiteralPath 'C:\' -Recurse", False, False, [], "bare drive root"),
    (r"Remove-Item -LiteralPath 'D:\randomstuff\x' -Recurse",
     False, False, [], "outside zones, no scan-root"),

    # ---- Canonicalization / spoofing attempts (must all be denied) -----------
    (r"Remove-Item -LiteralPath 'c:\windows\system32\x' -Recurse",
     False, False, [], "case-insensitive deny"),
    (r"Remove-Item -LiteralPath 'C:/Windows/System32/x' -Recurse",
     False, False, [], "forward slashes normalized"),
    (r"Remove-Item -LiteralPath 'C:\Users\dev\..\..\Windows\System32\x' -Recurse",
     False, False, [], "dot-dot traversal collapses into Windows"),
    (r"Remove-Item -LiteralPath 'C:\WINDOWS.\System32\evil' -Recurse",
     False, False, [], "trailing-dot component stripped"),
    (r"Remove-Item -LiteralPath 'C:\PROGRA~1\App' -Recurse",
     False, False, [], "8.3 short name refused"),
    (r"Remove-Item -LiteralPath 'C:\Users\dev\file.txt:hidden' -Force",
     False, False, [], "alternate data stream refused"),
    (r"Remove-Item -LiteralPath '\\server\share\x' -Recurse",
     False, False, [], "UNC refused"),
    (r"Remove-Item -LiteralPath '\\?\C:\Windows\..\Windows\System32\x' -Recurse",
     False, False, [], "\\\\?\\ device path refused"),
    (r"Remove-Item -Path HKLM:\Software\Foo -Recurse",
     False, False, [], "registry provider refused"),
    (r"Remove-Item -Path Env:\Foo", False, False, [], "Env provider refused"),

    # ---- Command-injection / chaining (must all be denied) -------------------
    (r"docker ps; Remove-Item C:\Windows -Recurse", False, False, [], "semicolon chaining"),
    (r"Remove-Item C:\Windows -Recurse | Out-Null", False, False, [], "pipe chaining"),
    (r"Remove-Item C:\Windows -Recurse & whoami", False, False, [], "ampersand chaining"),
    (r"[IO.Directory]::Delete('C:\Windows')", False, False, [], ".NET static call (::)"),
    (r"Remove-Item $(Get-Evil)", False, False, [], "subexpression"),

    # ---- Safe wrappers (ok, no protection) -----------------------------------
    (r"dotnet nuget locals all --clear", True, False, [], "nuget cache"),
    (r"docker system prune -af", True, False, [], "docker prune"),
    (r"Clear-RecycleBin -Force", True, False, [], "recycle bin cmdlet"),
    (r"cleanmgr /sagerun:1", True, False, [], "disk cleanup profile"),
    (r"npm cache clean --force", True, False, [], "npm cache"),
    (r"winget uninstall --id Some.App", True, False, [], "winget uninstall"),
    (r"Dism.exe /Online /Cleanup-Image /AnalyzeComponentStore",
     True, False, [], "DISM analyze (read-only)"),
    (r"vssadmin list shadowstorage", True, False, [], "vssadmin list (read-only)"),

    # ---- Tool wrappers, destructive => require protection ---------------------
    (r"Dism.exe /Online /Cleanup-Image /StartComponentCleanup /ResetBase",
     True, True, [], "DISM /ResetBase irreversible"),
    (r"vssadmin delete shadows /for=C: /oldest", True, True, [], "delete shadow copies"),
    (r"wevtutil cl Application", True, True, [], "clear event log"),
    (r"pnputil /delete-driver oem42.inf /uninstall", True, True, [], "driver removal"),
    (r"powercfg /h off", True, True, [], "disable hibernation"),

    # ---- Neither delete nor wrapper => refused -------------------------------
    (r"Stop-Service WSearch", False, False, [], "arbitrary cmdlet refused"),
    (r"Format-Volume -DriveLetter D", False, False, [], "format refused"),
    (r"", False, False, [], "empty command"),
]


def main() -> int:
    os.environ.update(FAKE_ENV)
    mod = _load_validator()
    passed = failed = 0
    for command, exp_ok, exp_prot, scan_roots, note in CASES:
        ok, reason, prot = mod.validate_command(command, scan_roots)
        good = (ok == exp_ok) and (prot == exp_prot if exp_ok else True)
        if good:
            passed += 1
        else:
            failed += 1
            print(f"FAIL [{note}]")
            print(f"     cmd      = {command!r}")
            print(f"     expected = ok={exp_ok} prot={exp_prot}")
            print(f"     got      = ok={ok} prot={prot} reason={reason!r}")
    print()
    print(f"=== {passed} passed | {failed} failed | {len(CASES)} total ===")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
