#!/usr/bin/env bash
# install.sh — idempotent installer for bash-guard.
#
# What it does:
#   1. Verifies Go is installed (>= 1.21).
#   2. Creates a symlink at ~/.claude/hooks/bash-guard and/or
#      ~/.codex/hooks/bash-guard pointing at this src/.
#   3. Triggers a first build (warms Go cache).
#   4. Patches Claude Code settings.json and/or Codex hooks.json to add the
#      bash-guard hook entry, preserving existing hooks. Uses jq for JSON-aware
#      editing.
#
# Re-running is safe: the symlink is recreated, the build is a no-op, and
# the settings.json patch is a no-op when our entry already exists.
#
# Modes:
#   --shadow    Add hook with BASH_GUARD_SHADOW=1 (logs only, never blocks).
#               This is the default for first-time installation.
#   --dry-run   Add hook with BASH_GUARD_DRY_RUN=1 (logs `would_decide`).
#   --live      Add hook with no env override (real enforcement).
#   --uninstall Remove our hook entry from settings.json AND delete the symlink.
#   --claude    Install for Claude Code (default).
#   --codex     Install for Codex CLI / Codex App.
#   --both      Install for both agents.

set -euo pipefail

usage() {
    cat <<EOF
Usage: $0 [--shadow|--dry-run|--live|--uninstall] [--claude|--codex|--both]

Default mode: --shadow (always-allow + log everything).
Default agent: --claude.
EOF
}

mode="shadow"
agent="claude"
replace_legacy=0
for arg in "$@"; do
    case "$arg" in
        --shadow)         mode="shadow" ;;
        --dry-run)        mode="dry-run" ;;
        --live)           mode="live" ;;
        --uninstall)      mode="uninstall" ;;
        --claude)         agent="claude" ;;
        --codex)          agent="codex" ;;
        --both)           agent="both" ;;
        --replace-legacy) replace_legacy=1 ;;
        -h|--help)        usage; exit 0 ;;
        *) echo "Unknown arg: $arg"; usage; exit 2 ;;
    esac
done

REPO_SRC_DIR="$(cd -- "$(dirname -- "$0")" && pwd)/src"
CLAUDE_HOOK_DIR="$HOME/.claude/hooks/bash-guard"
CLAUDE_SETTINGS="$HOME/.claude/settings.json"
CODEX_HOOK_DIR="$HOME/.codex/hooks/bash-guard"
CODEX_HOOKS="$HOME/.codex/hooks.json"

require_jq() {
    if ! command -v jq >/dev/null 2>&1; then
        echo "error: jq is required for safe settings.json editing" >&2
        echo "install:  brew install jq" >&2
        exit 1
    fi
}

require_go() {
    if ! command -v go >/dev/null 2>&1; then
        if [[ -x /opt/homebrew/bin/go ]]; then
            export PATH="/opt/homebrew/bin:$PATH"
        else
            echo "error: go toolchain not found" >&2
            echo "install: brew install go" >&2
            exit 1
        fi
    fi
}

backup_file() {
    local path="$1"
    if [[ -f "$path" ]]; then
        local ts
        ts="$(date +%Y%m%d-%H%M%S)"
        cp "$path" "$path.bak.$ts"
        echo "  backup: $path.bak.$ts"
    fi
}

create_symlink() {
    local hook_dir="$1"
    if [[ -e "$hook_dir" && ! -L "$hook_dir" ]]; then
        echo "error: $hook_dir exists and is not a symlink." >&2
        echo "       Move/remove it manually before installing." >&2
        exit 1
    fi
    if [[ -L "$hook_dir" ]]; then
        local current
        current="$(readlink "$hook_dir")"
        if [[ "$current" != "$REPO_SRC_DIR" ]]; then
            echo "  replacing existing symlink ($current -> $REPO_SRC_DIR)"
            rm "$hook_dir"
        else
            # Explicit return 0 — without it, `return` inherits the exit
            # status of the preceding `[[ ... ]]` test (1 when paths match)
            # and `set -e` then kills the script silently.
            return 0
        fi
    fi
    mkdir -p "$(dirname "$hook_dir")"
    ln -s "$REPO_SRC_DIR" "$hook_dir"
    echo "  linked: $hook_dir -> $REPO_SRC_DIR"
}

first_build() {
    ( cd "$REPO_SRC_DIR" && go build -o bash_guard.bin . )
    echo "  built: $REPO_SRC_DIR/bash_guard.bin"
}

# Build the JSON snippet for our hook entry. Mode determines env vars.
# Claude Code passes the command through `sh -c`, so env-var prefix works
# verbatim. We point directly at the .bin to avoid a wrapper layer that
# costs ~50 ms per invocation; rebuilds are explicit (`make build`).
hook_entry_json() {
    local target="$1"
    local adapter="$2"
    local entry
    case "$mode" in
        shadow)  entry="{\"type\":\"command\",\"command\":\"BASH_GUARD_ADAPTER=$adapter BASH_GUARD_SHADOW=1 $target\",\"timeout\":30,\"statusMessage\":\"Checking Bash command\"}" ;;
        dry-run) entry="{\"type\":\"command\",\"command\":\"BASH_GUARD_ADAPTER=$adapter BASH_GUARD_DRY_RUN=1 $target\",\"timeout\":30,\"statusMessage\":\"Checking Bash command\"}" ;;
        live)    entry="{\"type\":\"command\",\"command\":\"BASH_GUARD_ADAPTER=$adapter $target\",\"timeout\":30,\"statusMessage\":\"Checking Bash command\"}" ;;
    esac
    printf '%s' "$entry"
}

patch_claude_settings_install() {
    require_jq
    backup_file "$CLAUDE_SETTINGS"
    [[ -f "$CLAUDE_SETTINGS" ]] || { mkdir -p "$(dirname "$CLAUDE_SETTINGS")"; echo '{}' > "$CLAUDE_SETTINGS"; }

    local hook_entry
    hook_entry="$(hook_entry_json '~/.claude/hooks/bash-guard/bash_guard.bin' claude)"

    # 1. Make sure hooks.PreToolUse exists.
    # 2. Find or create the {matcher: "Bash", hooks: [...]} block.
    # 3. Drop any existing bash-guard entries (idempotent re-install) and
    #    append our current one.
    local tmp
    tmp="$(mktemp)"
    jq --argjson entry "$hook_entry" '
      .hooks //= {} |
      .hooks.PreToolUse //= [] |
      .hooks.PreToolUse |=
        ( map( if .matcher == "Bash" then
                 .hooks //= [] |
                 .hooks |= ( map(select((.command // "") | test("bash-guard") | not)) + [$entry] )
               else . end ) ) |
      # If no Bash matcher block existed at all, add a new one.
      ( if any(.hooks.PreToolUse[]?; .matcher == "Bash") then .
        else .hooks.PreToolUse += [{"matcher":"Bash","hooks":[$entry]}] end )
    ' "$CLAUDE_SETTINGS" > "$tmp"
    mv "$tmp" "$CLAUDE_SETTINGS"
    echo "  patched: $CLAUDE_SETTINGS"
}

patch_codex_hooks_install() {
    require_jq
    backup_file "$CODEX_HOOKS"
    [[ -f "$CODEX_HOOKS" ]] || { mkdir -p "$(dirname "$CODEX_HOOKS")"; echo '{"hooks":{}}' > "$CODEX_HOOKS"; }

    local hook_entry tmp
    hook_entry="$(hook_entry_json '~/.codex/hooks/bash-guard/bash_guard.bin' codex)"
    tmp="$(mktemp)"
    jq --argjson entry "$hook_entry" '
      .hooks //= {} |
      .hooks.PreToolUse //= [] |
      .hooks.PreToolUse |=
        ( map( if .matcher == "^Bash$" or .matcher == "Bash" then
                 .hooks //= [] |
                 .hooks |= ( map(select((.command // "") | test("bash-guard") | not)) + [$entry] ) |
                 .matcher = "^Bash$"
               else . end ) ) |
      ( if any(.hooks.PreToolUse[]?; .matcher == "^Bash$" or .matcher == "Bash") then .
        else .hooks.PreToolUse += [{"matcher":"^Bash$","hooks":[$entry]}] end )
    ' "$CODEX_HOOKS" > "$tmp"
    mv "$tmp" "$CODEX_HOOKS"
    echo "  patched: $CODEX_HOOKS"
}

# Remove legacy shell-hook entries that bash-guard now supersedes.
# Files on disk are NOT deleted — only the settings.json references.
# Easy rollback: restore from $SETTINGS.bak.<timestamp>.
patch_settings_remove_legacy() {
    require_jq
    [[ -f "$CLAUDE_SETTINGS" ]] || return
    local legacy_pattern='safety-net-ask|validate-rm|supabase-safety|bw-permission-check|docker-prune-permission|infra-safety'
    local tmp
    tmp="$(mktemp)"
    jq --arg pat "$legacy_pattern" '
      if .hooks.PreToolUse then
        .hooks.PreToolUse |=
          map( if .matcher == "Bash" then
                 .hooks |= map(select((.command // "") | test($pat) | not))
               else . end )
      else . end
    ' "$CLAUDE_SETTINGS" > "$tmp"
    mv "$tmp" "$CLAUDE_SETTINGS"
    echo "  removed legacy shell-hook entries from $CLAUDE_SETTINGS"
}

patch_claude_settings_uninstall() {
    require_jq
    [[ -f "$CLAUDE_SETTINGS" ]] || return
    backup_file "$CLAUDE_SETTINGS"
    local tmp
    tmp="$(mktemp)"
    jq '
      if .hooks.PreToolUse then
        .hooks.PreToolUse |=
          map( if .matcher == "Bash" then
                 .hooks |= map(select((.command // "") | test("bash-guard") | not))
               else . end )
      else . end
    ' "$CLAUDE_SETTINGS" > "$tmp"
    mv "$tmp" "$CLAUDE_SETTINGS"
    echo "  removed bash-guard from $CLAUDE_SETTINGS"
}

patch_codex_hooks_uninstall() {
    require_jq
    [[ -f "$CODEX_HOOKS" ]] || return
    backup_file "$CODEX_HOOKS"
    local tmp
    tmp="$(mktemp)"
    jq '
      if .hooks.PreToolUse then
        .hooks.PreToolUse |=
          map( if .matcher == "^Bash$" or .matcher == "Bash" then
                 .hooks |= map(select((.command // "") | test("bash-guard") | not))
               else . end )
      else . end
    ' "$CODEX_HOOKS" > "$tmp"
    mv "$tmp" "$CODEX_HOOKS"
    echo "  removed bash-guard from $CODEX_HOOKS"
}

install_selected_agents() {
    case "$agent" in
        claude|both)
            create_symlink "$CLAUDE_HOOK_DIR"
            patch_claude_settings_install
            if [[ "$replace_legacy" == 1 ]]; then
                patch_settings_remove_legacy
            fi
            ;;
    esac
    case "$agent" in
        codex|both)
            create_symlink "$CODEX_HOOK_DIR"
            patch_codex_hooks_install
            ;;
    esac
}

uninstall_selected_agents() {
    case "$agent" in
        claude|both)
            patch_claude_settings_uninstall
            if [[ -L "$CLAUDE_HOOK_DIR" ]]; then
                rm "$CLAUDE_HOOK_DIR"
                echo "  removed symlink: $CLAUDE_HOOK_DIR"
            fi
            ;;
    esac
    case "$agent" in
        codex|both)
            patch_codex_hooks_uninstall
            if [[ -L "$CODEX_HOOK_DIR" ]]; then
                rm "$CODEX_HOOK_DIR"
                echo "  removed symlink: $CODEX_HOOK_DIR"
            fi
            ;;
    esac
}

case "$mode" in
    shadow|dry-run|live)
        echo "Installing bash-guard ($mode mode, agent: $agent)"
        require_go
        first_build
        install_selected_agents
        echo
        echo "Done."
        echo "  Claude verify: jq '.hooks.PreToolUse' $CLAUDE_SETTINGS"
        echo "  Codex verify:  jq '.hooks.PreToolUse' $CODEX_HOOKS"
        echo "  Selftest: $REPO_SRC_DIR/bash_guard.bin --selftest"
        echo "  Restart the agent. In Codex CLI/App, open /hooks and trust the new hook if prompted."
        ;;
    uninstall)
        echo "Uninstalling bash-guard (agent: $agent)"
        uninstall_selected_agents
        echo "Done."
        ;;
esac
