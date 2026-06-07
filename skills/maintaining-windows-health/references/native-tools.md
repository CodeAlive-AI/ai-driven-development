# Native tools & the safety floor

macOS has Mole (`mo`) as a community-vetted safety floor. **Windows has no mature equivalent** — so the safety floor here is two things working together: (1) **native Microsoft-supported tooling** for everything the OS maintains itself, and (2) **the apply-script validator** (`assets/apply-cleanup-selection.py`) for bare deletes. On Windows the validator is the *only* line behind project-artifact purge, not a second line behind a vetted tool. Treat it accordingly.

## Table of contents

- [Native tooling = first choice](#native-tooling--first-choice)
- [Marker → target map for project-artifact purge](#marker--target-map-for-project-artifact-purge)
- [Age thresholds](#age-thresholds)
- [Path-validation rules (what the validator enforces)](#path-validation-rules-what-the-validator-enforces)
- [Operational logging](#operational-logging)
- [Safe-purge harness (when scripting by hand)](#safe-purge-harness-when-scripting-by-hand)
- [Third-party tools — optional, with caveats](#third-party-tools--optional-with-caveats)

## Native tooling = first choice

| Tool | For | Notes |
|---|---|---|
| **Storage Sense** | ongoing temp/Recycle Bin/cloud dehydration | per-user; configurable via Settings, or Intune/CSP/GPO in a fleet |
| **Cleanup recommendations** | one-shot GUI audit | Settings → System → Storage; temp, large/unused, cloud-synced, unused apps |
| **cleanmgr** | scripted/legacy cleanup | `/sageset:N` defines a profile, `/sagerun:N` runs it on all drives |
| **DISM** | Component Store (WinSxS) | `/AnalyzeComponentStore` then `/StartComponentCleanup`; `/ResetBase` is discuss-first |
| **pnputil** | Driver Store | `/enum-drivers`, `/export-driver` (back up), `/delete-driver` |
| **vssadmin** | shadow copies / restore | `list`/`delete`/`resize shadowstorage` |
| **wevtutil** | Event Logs | `epl`/`al` (export) before `cl` (clear) |
| **powercfg** | hiberfil / power state | `/h off`, `/h /type reduced`, `/a` |
| **Clear-RecycleBin** | Recycle Bin | cmdlet, safe by construction |
| **winget** | install/update/uninstall apps | `winget uninstall` is the clean app-removal path |

These are the **wrapper** commands the validator trusts. The destructive subset (`vssadmin delete`, `Dism …/ResetBase`, `wevtutil cl`, `pnputil /delete-driver`, `powercfg /h off`) still requires an explicit protected-override even though the tool self-polices — because the effect is irreversible.

## Marker → target map for project-artifact purge

Find dev projects by marker files; remove regenerable build/dependency dirs only. All targets must be **`LastWriteTime` ≥ 7 days old**.

| Marker | Tooling | Targets |
|---|---|---|
| `package.json`, `pnpm-lock.yaml`, `yarn.lock` | npm/pnpm/yarn | `node_modules`, `.next`, `.nuxt`, `.output`, `dist`, `build`, `.turbo`, `.parcel-cache` |
| `*.csproj`, `*.fsproj`, `*.vbproj`, `*.sln` | .NET | `bin`, `obj` (only with a sibling project file) |
| `Cargo.toml` | Rust | `target` |
| `pom.xml` | Maven | `target` |
| `build.gradle(.kts)` | Gradle | `build`, `.gradle` |
| `pyproject.toml`, `requirements.txt` | Python | `__pycache__`, `.venv`, `venv`, `.pytest_cache`, `.mypy_cache`, `.ruff_cache`, `.tox` |
| `composer.json` | PHP Composer | `vendor` (Go/Rails `vendor` is protected — hand-curated) |
| `pubspec.yaml` | Flutter/Dart | `.dart_tool`, `build` |
| `go.mod` | Go | `go clean -cache`/`-modcache` (don't delete `vendor`) |
| `angular.json` / `svelte.config.*` / `astro.config.*` | frameworks | `.angular` / `.svelte-kit` / `.astro` |
| any project | universal | `coverage`, `.cache` |

Default scan roots (under HOME): `%USERPROFILE%\source`, `\repos`, `\dev`, `\Projects`, `\GitHub`, `\Code`, `\work`. External drives must be passed explicitly (`--scan-root D:\projects`) — the validator denies bare deletes outside HOME/TEMP/scan-roots by default.

### Guards (mirror Mole's)

- **`bin`/`obj`**: only if a sibling `*.csproj`/`*.fsproj`/`*.vbproj` exists (avoids deleting Go binaries / generated CLI dirs).
- **`vendor`**: only with `composer.json`.
- **Project root**: a marker file present and `.git` nearby.
- **Reparse points**: never recurse into a junction/symlink (`FILE_ATTRIBUTE_REPARSE_POINT`) — recursive delete can escape into the target.

## Age thresholds

```
temp files / caches : LastWriteTime ≥ 7 days
crash dumps         : keep until triaged (forensics) — never age-delete blindly
project artifacts   : LastWriteTime ≥ 7 days
orphan app data     : ≥ 30 days
```

Always include the age filter in any `Get-ChildItem | Where-Object LastWriteTime -lt …` sweep. This single rule eliminates 90% of "I just built that yesterday" surprises.

## Path-validation rules (what the validator enforces)

`assets/apply-cleanup-selection.py` is the safety core. It is a Windows **rewrite**, not a translation of the macOS validator, because NTFS/PowerShell give five separate ways to spell a protected path that a naive `startswith` misses. For every bare-delete command it:

1. Rejects chaining/redirection metacharacters outright: `;  |  &  \`  $(  @(  ::  >  <` and newlines (PowerShell's injection surface is far wider than bash).
2. Expands `%VAR%`/`$VAR`, then per path token rejects: UNC/device paths (`\\?\`, `\\.\`, `\\server`), 8.3 short names (`PROGRA~1`), non-filesystem providers (`HKLM:`, `Env:`, `Cert:`), and Alternate Data Streams (`file.txt:hidden`).
3. Canonicalizes like Win32 `GetFullPath` (unify separators, collapse `..`, strip trailing dots/spaces), then requires a drive-absolute path and refuses a bare drive root.
4. Classifies the path against an allow-list (HOME, TEMP, `%SystemRoot%\Temp`, scan roots) and a deny-list (the `never-touch.md` hard-protected prefixes) using **longest-prefix-wins**, so carve-outs resolve correctly (`C:\Windows` denied but `C:\Windows\Temp` allowed; `C:\Users\me` allowed but `C:\Users\me\.ssh` denied).
5. Refuses any registry-provider delete entirely.

Wrappers are trusted to self-police; the irreversible-destructive ones additionally require a protected-override. The adversarial test suite (`assets/test_validate_command.py`) pins all of this and runs on any OS — run it after any edit to the validator.

## Operational logging

Every applied operation is appended (TSV, append-only) to `%LOCALAPPDATA%\win-health\operations.log`:

```
TIMESTAMP \t apply-selection \t ACTION \t PATH \t SIZE \t STATUS
2026-06-07 09:12:43  apply-selection  REMOVED  C:\Users\dev\proj\node_modules  1.1 GB  OK
```

It's the audit trail when "what did we delete?" comes up later. Keep the same format for any hand-rolled sweep.

## Safe-purge harness (when scripting by hand)

If you must sweep without the apply script, port these guards:

```powershell
function Invoke-SafeRemove {
    param([Parameter(Mandatory)][string]$Target)
    $full = [System.IO.Path]::GetFullPath([Environment]::ExpandEnvironmentVariables($Target))
    if ($full -notmatch '^[A-Za-z]:\\') { return }                       # drive-absolute only
    $item = Get-Item -LiteralPath $full -Force -EA SilentlyContinue
    if (-not $item) { return }
    if ($item.Attributes -band [IO.FileAttributes]::ReparsePoint) { return }   # never follow junctions
    $low = $full.ToLowerInvariant()
    foreach ($deny in @("$env:SystemRoot","$env:ProgramFiles","${env:ProgramFiles(x86)}",
                        "$env:USERPROFILE\.ssh","$env:APPDATA\Microsoft\Protect")) {
        $d = ([System.IO.Path]::GetFullPath($deny)).ToLowerInvariant()
        if ($low -eq $d -or $low.StartsWith($d + '\')) { return }
    }
    Remove-Item -LiteralPath $full -Recurse -Force -EA SilentlyContinue
}

# Apply with an age filter:
Get-ChildItem $root -Recurse -Depth 4 -Directory -Force -EA SilentlyContinue |
  Where-Object { $_.Name -eq 'node_modules' -and $_.LastWriteTime -lt (Get-Date).AddDays(-7) -and
                 -not ($_.Attributes -band [IO.FileAttributes]::ReparsePoint) } |
  ForEach-Object { Invoke-SafeRemove $_.FullName }
```

This is the minimal harness; the full apply-script validator is stricter (8.3/ADS/UNC/provider/longest-prefix). Prefer it.

## Third-party tools — optional, with caveats

Use these as an *overlay* for user/app caches, never as a replacement for native tooling. Several have a real CLI:

| Tool | CLI | Use | Caveat |
|---|---|---|---|
| **BleachBit** | `bleachbit_console.exe --preview --preset` then `--clean` | transparent cache/temp/browser cleaning | always `--preview` first; permanent |
| **BCUninstaller** | console interface | bulk app removal with leftovers | review the leftover list |
| **WizTree** | `wiztree64.exe C: /export=...` | fast disk audit (read MFT) | audit only, not a cleaner |
| **Autorunsc** | `autorunsc -accepteula -a * -c` | startup inventory | disabling entries is the change, not deletion |
| **winget** | `winget uninstall` | clean app removal | preferred over manual folder delete |

**Avoid as a primary choice on a work machine:**

- **Mole for Windows** — the author's own Windows branch is flagged "currently not mature" and "do not use" on machines with important data. Interesting for a test box; not the safe default here. Prefer `cleanmgr` / Storage Sense / DISM + the apply script.
- **CCleaner Registry Cleaner** — registry cleaning is unsupported by Microsoft and can destabilize the system. If CCleaner is used at all, restrict to **Custom Clean** and disable the registry feature.
- Any **"RAM optimizer" / "memory booster"** — purging working sets/standby lists degrades performance. For memory problems, diagnose causes (RAMMap/Autoruns/Task Manager), don't "free RAM".
