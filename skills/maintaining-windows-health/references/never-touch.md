# Never-touch list

Categories that **must not be deleted** even if the user asks, even elevated, even when desperate for space. Pushback expected: explain the consequence, suggest an alternative. The hard-protected prefixes below are kept in sync with the deny-list in `assets/apply-cleanup-selection.py` — if you edit one, edit both.

## Table of contents

- [Golden rule: clean with commands, not by deleting folders](#golden-rule-clean-with-commands-not-by-deleting-folders)
- [Hard-protected paths (system roots)](#hard-protected-paths-system-roots)
- [Paging / hibernation / crash files](#paging--hibernation--crash-files)
- [Boot, recovery & volume metadata](#boot-recovery--volume-metadata)
- [Credential & key stores](#credential--key-stores)
- [Cloud placeholders (Files On-Demand) & OneDrive KFM](#cloud-placeholders-files-on-demand--onedrive-kfm)
- [Per-app folders that LOOK like cache but hold state](#per-app-folders-that-look-like-cache-but-hold-state)
- [The registry is not a cleanup target](#the-registry-is-not-a-cleanup-target)
- [Windows-only dangers with no macOS analog](#windows-only-dangers-with-no-macos-analog)
- [How to handle pushback](#how-to-handle-pushback)

---

## Golden rule: clean with commands, not by deleting folders

Windows maintains several areas itself. Hand-deleting them corrupts the OS; the **supported command** does it safely. Memorize this mapping — most "free space" footguns are someone reaching for `Remove-Item` where a command was required:

| Area | NEVER `Remove-Item` | Use instead |
|---|---|---|
| Component Store (`WinSxS`) | manual delete = unbootable / un-updatable | `Dism /Online /Cleanup-Image /StartComponentCleanup` |
| Driver Store (`System32\DriverStore`) | breaks devices / driver rollback | `pnputil /delete-driver` (after export) |
| Shadow copies / restore points (`System Volume Information`) | loses all rollback | `vssadmin` / System Protection |
| Event Logs | loses forensics | `wevtutil epl` then `cl /bu:` |
| Windows Update store (`SoftwareDistribution`) | breaks WU | stop `wuauserv`+`bits`, rename, restart |
| MSI cache (`Installer`, `Package Cache`) | breaks uninstall/repair of every MSI app | leave it; uninstall apps via winget/Apps |
| pagefile / hiberfil | crash on delete | `powercfg`, System settings |
| Registry | instability up to reinstall | export + targeted edit only |

---

## Hard-protected paths (system roots)

Never delete inside these prefixes — one wrong path can brick the OS. (`%SystemRoot%` is normally `C:\Windows`; covers all of System32, SysWOW64, WinSxS, DriverStore, config, SoftwareDistribution, Installer, Minidump, Prefetch, servicing, assembly, Microsoft.NET, catroot/catroot2.)

```
%SystemRoot%                         (C:\Windows and everything under it)
%ProgramFiles%                       (C:\Program Files)
%ProgramFiles(x86)%                  (C:\Program Files (x86))
%ProgramW6432%
C:\ProgramData\Microsoft             (crypto, Defender, provisioning)
C:\ProgramData\Package Cache         (MSI/Burn bootstrapper — repair/uninstall)
```

The one carve-out inside `C:\Windows` that IS cleanable is `C:\Windows\Temp` (the validator allows it via longest-prefix-wins). Everything else under `%SystemRoot%` is off-limits to bare deletes.

## Paging / hibernation / crash files

Two separate swap files on Windows (macOS has one concept) — protect both:

```
C:\pagefile.sys       # classic page file — modified pages + crash dumps
C:\swapfile.sys       # UWP/Store app swap — separate from pagefile
C:\hiberfil.sys        # hibernation image — manage via powercfg /h
C:\DumpStack.log.tmp
%SystemRoot%\MEMORY.DMP, %SystemRoot%\Minidump   # forensics until the crash is triaged
```

`pagefile.sys` is **not junk**: it backs infrequently-used modified pages and is required for crash dumps. Size tracks peak commit + dump policy, not a "× RAM" formula. Leave it system-managed.

## Boot, recovery & volume metadata

A sudo-equivalent recursive delete can reach these even though they're hidden. **On a BitLocker volume, damaging boot/EFI/Recovery triggers a recovery-key prompt the user may not have** — doubly important.

```
EFI System Partition, \Boot, \EFI, bootmgr, \BCD
C:\$Recycle.Bin                  # use Clear-RecycleBin, never Remove-Item internals
C:\System Volume Information     # VSS shadow data + restore points + search index
C:\Recovery                      # WinRE.wim — recovery environment
C:\$WinREAgent                   # in-progress update rollback
C:\Config.Msi                    # transactional MSI rollback (lethal mid-install)
C:\PerfLogs
```

Also: never delete the **BitLocker recovery key** if escrowed locally.

## Credential & key stores

Tiny but irreplaceable. Cleaner tools that scan `$HOME` for "old hidden files" flag these — never include them, even in a "clean old dotfiles" pass. The validator denies them even though they sit under the allowed HOME root (deny beats allow via longest-prefix).

| Path | What it stores | Recovery if deleted |
|---|---|---|
| `%USERPROFILE%\.ssh` | private SSH keys | none — regenerate + redistribute pubkeys |
| `%USERPROFILE%\.gnupg` | GPG secret keyring | none |
| `%USERPROFILE%\.aws`, `.azure`, `.kube` | cloud access keys / kube contexts | re-issue / re-fetch |
| `%USERPROFILE%\.docker\config.json` | registry auth tokens | `docker login` again |
| `%USERPROFILE%\.netrc`, `.git-credentials` | plaintext credentials | from password manager |
| `%APPDATA%\Microsoft\Protect` | **DPAPI master keys** | deletion = all DPAPI-encrypted blobs unrecoverable |
| `%APPDATA%\Microsoft\Crypto`, `\SystemCertificates` | RSA/DSS keys, certs | none |
| `%APPDATA%\Microsoft\Credentials`, `%LOCALAPPDATA%\Microsoft\Credentials` | Credential Manager vault | none |
| `%APPDATA%\gh\hosts.yml` | GitHub CLI tokens | `gh auth login` |

Heuristic: any dotfile/dotfolder under `%USERPROFILE%` outside an explicit cache (e.g. `.cache`, `.npm\_cacache`, `.gradle\caches`) should be assumed credential- or config-bearing.

## Cloud placeholders (Files On-Demand) & OneDrive KFM

Detect by **file attribute**, not by path list — this generically covers OneDrive, Dropbox, Google Drive:

- Refuse to delete any item with `FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS`, `RECALL_ON_OPEN`, or `OFFLINE` set. These are dehydrated cloud placeholders; deleting the stub deletes the cloud original and propagates to every device.
- **OneDrive Known Folder Move (KFM):** `Desktop`, `Documents`, `Pictures` are frequently redirected into `%OneDrive%`. So "clean the Desktop" or "review Downloads" has different stakes there. Resolve those folders and check for a reparse point / `*OneDrive*` target before treating them as local (the audit script reports this). `Downloads` is usually NOT redirected; `Desktop`/`Documents` often ARE.

## Per-app folders that LOOK like cache but hold state

Windows has no bundle-ID namespace, so protection is **path-based** under `%APPDATA%` / `%LOCALAPPDATA%`. Only the cache-family subfolders (`Cache`, `Code Cache`, `GPUCache`, `Service Worker\CacheStorage`, `DawnCache`) are safe; everything else is state.

| App | Path | What it actually is |
|---|---|---|
| Telegram | `%APPDATA%\Telegram Desktop\tdata\` | full chat history + session keys — delete = logout + lost history |
| Slack | `%APPDATA%\Slack\storage\`, `IndexedDB\` | workspace prefs, draft messages |
| Notion | `%APPDATA%\Notion\...\IndexedDB\` | offline page data |
| Teams | `%APPDATA%\Microsoft\Teams\` (and the new Store app data) | account/auth + cached messages |
| Browsers | `...\User Data\Default\` (Edge/Chrome/Brave) | history, cookies, **extension state incl. password managers / MetaMask seed** |
| VS Code / Cursor | `%APPDATA%\Code\User\`, `globalStorage\` | settings, snippets, extension state |
| JetBrains | `%APPDATA%\JetBrains\<IDE><ver>\` | settings, project list, keymaps, licenses |
| WSL distros | `%LOCALAPPDATA%\Packages\<distro>\LocalState\ext4.vhdx` | the **entire Linux filesystem** — compact, never delete |
| Docker Desktop | `%LOCALAPPDATA%\Docker\wsl\...\*.vhdx` | images + volumes — compact, never delete |
| Password managers | `%LOCALAPPDATA%\1Password`, `%APPDATA%\Bitwarden` etc. | vault/session state |
| Crypto wallets | `%APPDATA%\Exodus`, `Ledger Live`, browser-extension state | encrypted wallet / seed-derived data |

When unsure for an AppData folder: only `Cache`/`Code Cache`/`GPUCache`/`Service Worker` subdirs are safe. Everything else, ask.

## The registry is not a cleanup target

Microsoft does not support registry cleaners; "registry bloat" is not a meaningful space or performance source. The apply-script **refuses any delete against a registry provider** (`HKLM:`, `HKCU:`, …). For a concrete fix, export the specific key (`reg export` / Registry Editor) and edit it by hand — never bulk-"optimize".

## Windows-only dangers with no macOS analog

These are easy to forget because macOS has no equivalent:

1. **Reparse points / junctions / symlinks.** `Remove-Item -Recurse` can follow a junction and delete the *target's* contents — the classic data-loss bug. Dev trees are full of junctions (npm/pnpm store, Docker, WSL). Always use `-LiteralPath`; never recurse through `FILE_ATTRIBUTE_REPARSE_POINT` (the audit script lists reparse points under scan roots).
2. **`Remove-Item` is permanent — no Recycle Bin.** Unlike dragging to the bin, `Remove-Item` deletes immediately. Users expect "delete = recoverable"; it isn't here. Prefer moving to a dated quarantine folder over `Remove-Item` when the user is unsure.
3. **Controlled Folder Access (ransomware protection).** If on, deletes in Documents/Pictures/Desktop fail with Access Denied **from Defender, not from permissions**. Distinguish a CFA block from a real error so the tool isn't blamed (`Get-MpPreference | Select EnableControlledFolderAccess`).
4. **System Restore / VSS.** `vssadmin delete shadows` frees space but destroys the user's rollback net (the analog of Time Machine local snapshots). Treat like the macOS `tmutil` rule: only via the supported tool, only after warning.
5. **MSI `Installer` cache + `Package Cache`.** Every "free space" tutorial wrongly recommends cleaning `C:\Windows\Installer` — it breaks uninstall/repair/patch for every MSI app. Hard no.
6. **Prefetch.** Cleaner-tool muscle memory reaches for it; deleting it slows boot for negligible space. Leave it.

## How to handle pushback

User says "I know it's risky, just delete it":

1. State the consequence concretely ("you'll lose every System Restore point and can't roll back this driver update", not "system data").
2. Offer an alternative: the supported command, an export/backup first, or move-to-quarantine instead of delete.
3. If they insist, document in chat: exact path, exact action, exact consequence. Make them say "yes, delete X which holds Y, I accept losing Z."
4. Even then prefer non-destructive: `Move-Item` to `%USERPROFILE%\.quarantine-YYYYMMDD\` over `Remove-Item`. Easy to recover if regretted.

Risk is asymmetric: false caution costs disk space; one bad delete costs weeks of work, an un-decryptable DPAPI vault, or an unbootable machine. Bias toward caution.
