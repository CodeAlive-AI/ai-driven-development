# Explore mode

Use explore to understand repository context and answer a question from cited evidence. It is not a review: it does not load review principles, specialist roles, `review_instructions`, or review output templates. It is read-only and uses one exact agent, Grok 4.5 by default.

## Commands and options

```bash
# Current repository
scripts/consilium explore "How is authentication wired up?"

# Another local repository
scripts/consilium explore --repo ~/src/app "Where is the public API assembled?"

# Remote GitHub repository
scripts/consilium explore --repo owner/repository "What handles incremental builds?"

# Pinned remote branch, tag, or commit
scripts/consilium explore --repo https://github.com/owner/repository --ref v2.4.0 \
  "How does the middleware pipeline work?"

scripts/consilium explore --repo owner/repository --prompt-file question.md
```

| Option | Meaning |
|---|---|
| `--repo SOURCE` | Local path, `owner/repo` GitHub shorthand, or git URL; default `.` |
| `--ref REF` | Branch, tag, or commit for remote sources only |
| `-a, --agent ID` | Exact agent id; default `grok` |
| `--prompt-file FILE` | Read the question from a file |
| `--depth N\|full` | Remote clone depth; default `1` |
| `--progress compact\|verbose\|none` | Content-free progress detail; default `compact` |
| `--keep-clone` | Keep a remote clone and print its path for debugging |

The source must be supplied through `--repo`; a positional `owner/repo` is ambiguous. An existing local directory named `owner/repo` takes precedence over GitHub shorthand.

Exit codes: `0` success; `4` unknown agent/configuration; `5` usage; `6` source resolution, transport, clone, or ref error; otherwise the backend's exit code.

## Answer contract

```text
## Answer        direct answer, prose first
## Evidence      repository-relative path:line and what it proves
## Context map   only modules relevant to the question
## Gaps          facts that could not be confirmed and why
```

Do not request review-only sections such as Blind Spots, Alternatives, Recommendations, or defect findings.

## Remote trust boundary

A remote repository is data, not a control plane. Grok exploration clones it into an isolated workspace and runs from the neutral parent:

```text
<workspace>/          agent CWD
  source/             untrusted clone
```

Remote Grok runs add `--sandbox strict`, `--no-subagents`, `--no-memory`, no shell, and no write tools. Repository instructions may be read as data but the exploration prompt forbids obeying them. User-level configuration still loads and is treated as trusted.

Blocked by default: `file://`, `ext::` and other git helpers, and plain `http://`. Submodules and LFS payloads are not fetched. Embedded URL credentials are redacted before logging or provenance storage. Clones are removed on success, failure, and signals unless `--keep-clone` is explicit.

Local trusted repositories are explored in place under a read-only sandbox; their repo-local instructions may be discovered.

## Web, progress, and non-Grok agents

Explore grants `web_search` and `web_fetch` for upstream documentation, RFCs, and release notes. The agent may not follow a URL because repository content told it to or send repository content elsewhere.

Progress is content-free: `compact` reports shape, `verbose` shortens heartbeat intervals, and `none` silences it. Explore never streams chain-of-thought or answer text to stderr. Tool-level progress is deferred; load `ACP-RESEARCH.md` directly from the root detail map when that research is needed.

Isolation guarantees beyond ordinary read-only posture are Grok-specific. `-a <non-grok>` remains read-only but may discover repo-local instructions and uses that backend's defaults for memory, subagents, and web. Consilium warns and records `"isolation": "reduced"`.

## Provenance

`meta.json` records mode, profile/backend, isolation level, source kind, redacted URL, requested ref, resolved commit, branch, shallow/dirty flags, clone depth/strategy, caller and agent working directories, exploration root, inventory size, and question SHA-256.

Because the explorer has no shell, the orchestrator supplies git facts and a bounded file inventory. Large repositories receive an explicitly incomplete directory rollup instead of a silently truncated file list.
