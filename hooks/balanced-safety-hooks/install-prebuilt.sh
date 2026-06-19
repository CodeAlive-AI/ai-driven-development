#!/usr/bin/env bash
# install-prebuilt.sh — install bash-guard from a GitHub release without a Go
# toolchain. Detects OS/arch, downloads the matching binary + SHA256SUMS,
# verifies the checksum, drops the binary at ~/.claude/hooks/bash-guard/ and/or
# ~/.codex/hooks/bash-guard/, and patches Claude Code settings.json and/or
# Codex hooks.json with a PreToolUse[matcher=Bash] entry.
#
# Pipe-friendly:
#   curl -fsSL https://raw.githubusercontent.com/CodeAlive-AI/ai-driven-development/main/hooks/balanced-safety-hooks/install-prebuilt.sh | sh
#
# With args (note `sh -s --` to forward args through the pipe):
#   curl -fsSL …install-prebuilt.sh | sh -s -- --shadow
#
# Pin a specific release:
#   BASH_GUARD_VERSION=bash-guard-v0.1.0 curl -fsSL …install-prebuilt.sh | sh
#
# Modes:
#   --live        Real enforcement — emits ask for risky commands. Default.
#   --shadow      Logs every decision, never prompts. For tuning safe paths.
#   --dry-run     Same as shadow with a distinct log label.
#   --uninstall   Remove the hook entry from settings.json and delete the binary.
#   --claude      Install for Claude Code (default).
#   --codex       Install for Codex CLI / Codex App.
#   --both        Install for both agents.

set -euo pipefail

REPO="CodeAlive-AI/ai-driven-development"
CLAUDE_BIN_DIR="$HOME/.claude/hooks/bash-guard"
CLAUDE_BIN_PATH="$CLAUDE_BIN_DIR/bash_guard.bin"
CLAUDE_SETTINGS="$HOME/.claude/settings.json"
CODEX_BIN_DIR="$HOME/.codex/hooks/bash-guard"
CODEX_BIN_PATH="$CODEX_BIN_DIR/bash_guard.bin"
CODEX_HOOKS="$HOME/.codex/hooks.json"

mode="live"
agent="claude"
for arg in "$@"; do
    case "$arg" in
        --live)      mode="live" ;;
        --shadow)    mode="shadow" ;;
        --dry-run)   mode="dry-run" ;;
        --uninstall) mode="uninstall" ;;
        --claude)    agent="claude" ;;
        --codex)     agent="codex" ;;
        --both)      agent="both" ;;
        -h|--help)
            sed -n '2,/^$/p' "$0" | sed 's/^# \{0,1\}//'
            exit 0
            ;;
        *) echo "error: unknown arg: $arg" >&2; exit 2 ;;
    esac
done

require() {
    command -v "$1" >/dev/null 2>&1 || {
        echo "error: $1 is required" >&2
        [[ -n "${2:-}" ]] && echo "install: $2" >&2
        exit 1
    }
}

detect_platform() {
    local os arch
    os="$(uname -s | tr '[:upper:]' '[:lower:]')"
    arch="$(uname -m)"
    case "$os" in
        darwin|linux) ;;
        *) echo "error: unsupported OS: $os (need darwin or linux)" >&2; exit 1 ;;
    esac
    case "$arch" in
        x86_64|amd64)  arch="amd64" ;;
        arm64|aarch64) arch="arm64" ;;
        *) echo "error: unsupported arch: $arch (need amd64 or arm64)" >&2; exit 1 ;;
    esac
    echo "${os}-${arch}"
}

# Resolve which release tag to install. Honour an explicit pin first, then
# fall back to the newest tag whose name starts with `bash-guard-v` so that
# unrelated releases in this monorepo (other skills, etc.) don't get picked up.
resolve_tag() {
    if [[ -n "${BASH_GUARD_VERSION:-}" ]]; then
        echo "$BASH_GUARD_VERSION"
        return
    fi
    local tag
    tag="$(curl -fsSL "https://api.github.com/repos/${REPO}/releases?per_page=50" \
        | grep -oE '"tag_name":[[:space:]]*"bash-guard-v[^"]*"' \
        | head -1 \
        | sed -E 's/.*"(bash-guard-v[^"]*)"/\1/')" || true
    if [[ -z "$tag" ]]; then
        echo "error: no bash-guard-v* release found in $REPO" >&2
        exit 1
    fi
    echo "$tag"
}

download_and_verify() {
    local platform="$1" tag="$2"
    local asset="bash-guard-${platform}"
    local base="https://github.com/${REPO}/releases/download/${tag}"
    local tmp_bin tmp_sums expected actual sum_tool
    tmp_bin="$(mktemp)"
    tmp_sums="$(mktemp)"
    trap 'rm -f "$tmp_bin" "$tmp_sums"' RETURN

    echo "  downloading ${asset} (${tag})…"
    curl -fsSL "${base}/${asset}" -o "$tmp_bin"
    curl -fsSL "${base}/SHA256SUMS" -o "$tmp_sums"

    expected="$(awk -v a="$asset" '$2 == a { print $1 }' "$tmp_sums")"
    if [[ -z "$expected" ]]; then
        echo "error: ${asset} not listed in SHA256SUMS" >&2
        exit 1
    fi

    if   command -v shasum    >/dev/null 2>&1; then sum_tool="shasum -a 256"
    elif command -v sha256sum >/dev/null 2>&1; then sum_tool="sha256sum"
    else echo "error: need shasum or sha256sum to verify the download" >&2; exit 1
    fi
    actual="$($sum_tool "$tmp_bin" | awk '{print $1}')"

    if [[ "$actual" != "$expected" ]]; then
        echo "error: checksum mismatch for ${asset}" >&2
        echo "  expected: $expected" >&2
        echo "  got:      $actual"   >&2
        exit 1
    fi

    install_verified_binary "$tmp_bin"
}

install_one_binary() {
    local src="$1" bin_dir="$2" bin_path="$3"
    # Replace any prior symlink (from source-based install) with a real dir.
    if [[ -L "$bin_dir" ]]; then
        rm "$bin_dir"
    fi
    mkdir -p "$bin_dir"
    cp "$src" "$bin_path"
    chmod +x "$bin_path"
    echo "  installed: $bin_path"
}

install_verified_binary() {
    local src="$1"
    case "$agent" in
        claude|both) install_one_binary "$src" "$CLAUDE_BIN_DIR" "$CLAUDE_BIN_PATH" ;;
    esac
    case "$agent" in
        codex|both) install_one_binary "$src" "$CODEX_BIN_DIR" "$CODEX_BIN_PATH" ;;
    esac
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

hook_entry_json() {
    local target="$1"
    local adapter="$2"
    case "$mode" in
        shadow)  printf '{"type":"command","command":"BASH_GUARD_ADAPTER=%s BASH_GUARD_SHADOW=1 %s","timeout":30,"statusMessage":"Checking Bash command"}'  "$adapter" "$target" ;;
        dry-run) printf '{"type":"command","command":"BASH_GUARD_ADAPTER=%s BASH_GUARD_DRY_RUN=1 %s","timeout":30,"statusMessage":"Checking Bash command"}' "$adapter" "$target" ;;
        live)    printf '{"type":"command","command":"BASH_GUARD_ADAPTER=%s %s","timeout":30,"statusMessage":"Checking Bash command"}'                       "$adapter" "$target" ;;
    esac
}

patch_claude_settings_install() {
    backup_file "$CLAUDE_SETTINGS"
    [[ -f "$CLAUDE_SETTINGS" ]] || { mkdir -p "$(dirname "$CLAUDE_SETTINGS")"; echo '{}' > "$CLAUDE_SETTINGS"; }

    local hook_entry tmp
    hook_entry="$(hook_entry_json '~/.claude/hooks/bash-guard/bash_guard.bin' claude)"
    tmp="$(mktemp)"
    jq --argjson entry "$hook_entry" '
      .hooks //= {} |
      .hooks.PreToolUse //= [] |
      .hooks.PreToolUse |=
        ( map( if .matcher == "Bash" then
                 .hooks //= [] |
                 .hooks |= ( map(select((.command // "") | test("bash-guard") | not)) + [$entry] )
               else . end ) ) |
      ( if any(.hooks.PreToolUse[]?; .matcher == "Bash") then .
        else .hooks.PreToolUse += [{"matcher":"Bash","hooks":[$entry]}] end )
    ' "$CLAUDE_SETTINGS" > "$tmp"
    mv "$tmp" "$CLAUDE_SETTINGS"
    echo "  patched: $CLAUDE_SETTINGS"
}

patch_codex_hooks_install() {
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

patch_selected_install() {
    case "$agent" in
        claude|both) patch_claude_settings_install ;;
    esac
    case "$agent" in
        codex|both) patch_codex_hooks_install ;;
    esac
}

patch_claude_settings_uninstall() {
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

uninstall_selected() {
    case "$agent" in
        claude|both)
            patch_claude_settings_uninstall
            if [[ -f "$CLAUDE_BIN_PATH" ]]; then
                rm "$CLAUDE_BIN_PATH"
                rmdir "$CLAUDE_BIN_DIR" 2>/dev/null || true
                echo "  removed: $CLAUDE_BIN_PATH"
            fi
            ;;
    esac
    case "$agent" in
        codex|both)
            patch_codex_hooks_uninstall
            if [[ -f "$CODEX_BIN_PATH" ]]; then
                rm "$CODEX_BIN_PATH"
                rmdir "$CODEX_BIN_DIR" 2>/dev/null || true
                echo "  removed: $CODEX_BIN_PATH"
            fi
            ;;
    esac
}

case "$mode" in
    live|shadow|dry-run)
        echo "Installing bash-guard ($mode mode, prebuilt, agent: $agent)"
        require curl
        require jq "brew install jq  (macOS)  /  apt install jq  (Linux)"
        platform="$(detect_platform)"
        tag="$(resolve_tag)"
        download_and_verify "$platform" "$tag"
        patch_selected_install
        echo
        echo "Done."
        echo "  Claude selftest: $CLAUDE_BIN_PATH --selftest"
        echo "  Codex selftest:  $CODEX_BIN_PATH --selftest"
        echo "  Audit:           tail -f ~/.claude/logs/bash-guard.jsonl | jq '.'"
        echo "  Restart the agent. In Codex CLI/App, open /hooks and trust the new hook if prompted."
        ;;
    uninstall)
        echo "Uninstalling bash-guard (agent: $agent)"
        require jq "brew install jq  (macOS)  /  apt install jq  (Linux)"
        uninstall_selected
        echo "Done."
        ;;
esac
