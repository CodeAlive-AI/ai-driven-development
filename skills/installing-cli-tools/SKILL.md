---
name: installing-cli-tools
description: Install, upgrade, configure, and verify developer CLI tools safely. Use when a user asks to install a new CLI, command-line app, SDK tool, package-manager binary, GitHub release binary, language runtime tool, or AI/vendor CLI; configure shell PATH/completions; run first login; set API keys, tokens, or env variables for a CLI; migrate an existing CLI install; or troubleshoot a CLI installation while avoiding secret leakage.
---

# Installing CLI Tools

## Overview

Use this skill to take a CLI from "not installed" to "usable and verified" without exposing credentials in chat, logs, shell history, or repo files. Treat installation and secret setup as separate phases.

## Workflow

1. Identify the exact CLI, target OS/architecture, intended use, and whether authentication is required.
2. Check current state with narrow commands such as `command -v tool`, `tool --version`, package-manager queries, and existing config file paths only when needed.
3. Research current official installation docs before acting unless the user supplied an exact trusted source. Prefer official docs, package registry pages, signed release notes, or the upstream GitHub release.
4. Choose the least surprising install method:
   - Existing project manager (`brew`, `npm`, `pipx`, `uv tool`, `cargo install`, `go install`) when official and maintained.
   - Vendor installer only when it is the official path and its behavior is understood.
   - Manual binary install only after verifying architecture, checksum/signature when available, permissions, and destination.
5. Install to a user-writable, reversible location when possible. Avoid `sudo` unless the install path truly requires it and the user has agreed.
6. Wire PATH/completions only as narrowly as needed. Never edit shell startup files to add secrets.
7. Configure authentication through a safe channel.
8. Verify with `tool --version`, `tool doctor` or equivalent, and a non-destructive authenticated command if relevant.
9. Report what changed, where files were placed, how to undo it, and whether any restart/new shell is needed.

## Secret Handling

Never read, print, summarize, grep, or search for existing secret values in `.env`, shell rc files, keychains, SSH keys, cloud credential files, or password-manager vaults. Do not run broad commands like `env`, `printenv`, or recursive token searches.

For new credentials, use the safest supported option in this order:

1. Browser/device OAuth or official `tool auth login`.
2. The platform's secure setup flow or connector for that provider.
3. OS credential store, such as macOS Keychain, through commands that accept the secret via stdin or hidden prompt.
4. Tool-specific config command that prompts interactively and does not echo the input.
5. A local secrets manager such as `op`, `bw`, `pass`, `gopass`, or `direnv` with a secret backend, if the user already uses it.
6. A plaintext env file only when the user explicitly asks for it or the CLI has no safer option; write placeholders by default and set mode `0600`.

Do not put secret values in command arguments, chat messages, shell history, logs, generated docs, git commits, package manager config, MCP config, or shell startup files. If a command needs a value, prefer an interactive prompt, stdin, or a temporary file with `0600` permissions that is removed immediately after use.

Before accepting a credential from the user, state the destination and persistence model in one sentence, for example: "This will store the token in macOS Keychain under service `example-cli`; I will not print it back." If the current environment cannot safely accept hidden input, stop and ask the user to run the official login command locally.

## Installation Checks

Use precise commands and avoid noisy discovery. Good checks:

```sh
command -v example
example --version
brew list --versions example
npm view example-cli version
python3 -m pipx list
```

For GitHub release binaries, verify the asset matches OS and CPU architecture. Use `shasum -a 256` when upstream publishes checksums. Prefer signed or notarized macOS artifacts when available.

For installer scripts fetched over the network, do not pipe directly into a shell unless the user explicitly requests that official install style. Prefer downloading to a temporary file, reading the script enough to understand what it changes, then running it.

## Shell Integration

Modify shell files only for PATH, completions, aliases requested by the user, or non-secret configuration. Before editing, identify the active shell and target file. Keep edits idempotent and bounded by clear comments when adding a block.

Do not add API keys, tokens, passwords, or provider credentials to `.zshrc`, `.bashrc`, `.profile`, `.config/fish/config.fish`, or project shell hooks. For env variables that point to non-secret paths or feature flags, explain why they are safe.

## Verification

Verify both installation and authentication without destructive actions:

- Installation: `tool --version`, `tool help`, or package-manager metadata.
- PATH: open a fresh shell or source only the changed file when safe.
- Auth: `tool auth status`, `whoami`, `account show`, or a read-only API call.
- Failure: capture exact non-secret error text and classify whether the issue is PATH, missing dependency, architecture, permissions, network, or authentication.

If verification requires a paid operation, mutation, or secret display command, do not run it. Use the vendor's status command or ask the user for permission to run a specific safe alternative.

## Rollback

Track install actions as you go. When finishing, include the uninstall command or manual rollback path:

- Package manager uninstall command.
- Files, symlinks, launch agents, or completions created.
- Shell file block added.
- Credential entry name only, never the value.

For failed installs, clean temporary files and partial symlinks when that is clearly safe. Ask before deleting user-owned config, caches, or credentials.
