# Skill deduplication and installation preflight

## Contents

- [Invariant](#invariant)
- [Discovery topology](#discovery-topology)
- [Classification](#classification)
- [Choosing the canonical source](#choosing-the-canonical-source)
- [Audit workflow](#audit-workflow)
- [Installation workflow](#installation-workflow)
- [Plugins](#plugins)
- [Removal and registry cleanup](#removal-and-registry-cleanup)
- [Update commands](#update-commands)
- [Verification](#verification)

## Invariant

Aim for one active implementation of a frontmatter `name` per consumer's discovery
topology. Count real directories and enabled plugin sources, not labels alone.

- One real directory exposed through several symlinks is an **alias**, not several
  maintained copies.
- Byte-identical folders in agent-specific roots are **replicas**. Keep them only when
  those agents cannot share one root.
- A plugin skill and a standalone skill may be namespaced, but they are still duplicate
  workflows for a user who wants one maintained implementation.
- Never decide freshness from mtime alone. Establish source ownership and update path.

## Discovery topology

Inventory only bounded skill locations; do not recursively search the whole home folder.

- Codex user skills: `$HOME/.agents/skills`.
- Codex repository skills: `.agents/skills` from the working directory up to repo root.
- Agent-specific user/project roots from `scripts/agents.py`.
- Local plugin source `skills/` when a repo contains `.claude-plugin/plugin.json`.
- Enabled plugin caches from the relevant plugin manager.
- System/admin skills are read-only distribution layers; report but do not delete them.

Codex follows symlinked skill directories. It does not merge different skills that share
one `name`; both may appear in selectors. Plugin-provided skills are namespaced, which
prevents an identifier collision but does not answer which workflow should be maintained.

## Classification

| Class | Evidence | Default action |
|---|---|---|
| `alias` | Same resolved real path | Keep one canonical link topology |
| `replica` | Different paths, identical directory hash | Keep only replicas required by different consumers |
| `stale-backup` | Same name plus backup/old/copy directory | Remove from discovery root; archive outside it if needed |
| `namespaced-divergent` | Enabled plugin plus standalone, different hashes | Compare lifecycle and plugin-only capabilities |
| `managed-plugin-*` | Versions/copies entirely inside manager-owned plugin caches | Informational; update/disable through the manager |
| `divergent` | Same name, different content | Stop installation and choose a canonical source |

Run `scripts/audit_skill_duplicates.py --format json` when programmatic evidence is
needed. Use `--fail-on-conflict` in CI or preflight checks.

## Choosing the canonical source

Use this priority order as evidence, not as an automatic deletion rule:

1. A repository that declares itself canonical beats a repository marked archived,
   moved, consolidated, or read-only.
2. A maintained tracked source with a documented sync/update process beats an anonymous
   copied directory.
3. A managed plugin may beat a standalone copy when it also supplies required hooks,
   subagents, MCP configuration, or assets.
4. A current standalone upstream may beat a stale plugin cache when the plugin has no
   needed extra capability or cannot be updated safely.
5. An explicit user-maintained fork beats upstream only when its divergence is intentional
   and documented.

Check repository remotes, current upstream HEAD, release/plugin version, lock metadata,
Git history, moved/archive notices, enabled state, and local modifications. Do not overwrite
a dirty plugin marketplace or tracked working tree merely to make versions match.

## Audit workflow

1. Run the duplicate auditor and group by frontmatter `name`.
2. Resolve symlinks and compare full directory hashes.
3. Identify the consumer that sees each root; do not treat every physical replica as a
   selector conflict.
4. Establish the source and update mechanism for each divergent copy.
5. Inspect plugin manifests and enabled state. A plugin cache is not a normal source tree.
6. Choose one canonical active implementation.
7. Prefer update, disable, unlink, or move-to-trash operations over irreversible deletion.
8. Audit again and open a new task/restart when the current session cached skill metadata.

## Installation workflow

Before every install:

1. Inspect the candidate's `SKILL.md` and extract its frontmatter `name`.
2. Run:

   ```bash
   python3 scripts/audit_skill_duplicates.py --candidate /path/to/skill --fail-on-conflict
   ```

3. If the name already exists, update or reuse the canonical copy. Do not install first
   and deduplicate afterward.
4. For locally maintained sources, share one real directory with
   `install_skill.py --link --allow-duplicate-name`. If a consumer cannot follow symlinks,
   document why an intentional replica is required before using a copy.
5. After installation, run the full audit again.

For a remote ecosystem source, inspect its skill list or clone it to a temporary directory
before `npx skills add`. If the candidate name cannot be known without installing, snapshot
the current inventory first and immediately audit the delta afterward.

## Plugins

- Never manually edit or delete a plugin cache to resolve a duplicate; an update can restore
  it and cache edits can corrupt plugin state.
- Audit enabled plugin installs, not every historical cache directory. Multiple versions
  wholly inside a manager-owned cache are informational, not standalone-install conflicts.
- Compare the installed cache version with upstream and the marketplace source.
- Update the plugin when safe. If its source tree is dirty, preserve local changes and stop.
- If the standalone copy is canonical, disable the stale plugin rather than uninstalling it
  when the plugin contains useful hooks/subagents or local changes.
- If the plugin is canonical, remove the standalone install through its package manager.
- Confirm before uninstalling a plugin because that removes more than its bundled skill.

## Removal and registry cleanup

Use the manager that created the copy. Prefer `npx skills remove` for ecosystem installs and
the plugin manager for plugins. Backups must live outside every discovery root.

After removal, inspect manager lock files for orphaned entries. If the manager cannot remove
an orphan because its directory is already absent, delete only the exact stale JSON object,
then validate the file with `jq empty`. Never broadly rewrite a lock file or remove unrelated
entries sharing a source repository.

## Update commands

Treat `npx skills check` as **potentially mutating**. Some Skills CLI versions perform updates
during `check`, and even `check --help` may enter the update workflow. Do not run it as a
read-only probe unless mutation is already authorized. Capture the CLI version and observe
actual behavior; use repository/lock inspection for a read-only freshness check.

After a managed update, audit duplicate names again: update tools can recreate removed
copies or follow a stale lock entry from an archived source.

## Verification

- Duplicate audit reports no unresolved `stale-backup`, `namespaced-divergent`, or
  `divergent` groups.
- Candidate preflight blocks an already-discoverable name by default.
- Canonical source path exists and its update channel is documented.
- Disabled/uninstalled plugin state matches the decision.
- Lock files parse and contain no orphaned source aliases.
- Unrelated working-tree and plugin-source changes remain untouched.
