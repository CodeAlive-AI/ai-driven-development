package main

import "strings"

// GitRule covers git operations that lose work, rewrite history, or change
// the agent's working context in ways the user must opt into:
//
//   - push -f / --force / --force-with-lease / +<refspec>  → force push
//   - push --delete / push -d / push origin :<branch>      → remote ref deletion
//   - reset --hard                                         → working-tree wipe
//   - clean -f[d|x]                                        → untracked-file wipe
//   - checkout . / -- . / -- <file>                        → working-tree wipe via pathspec
//   - restore .  (without --source / --staged)             → working-tree wipe
//   - branch -D / --delete --force                         → force-delete unmerged branch
//   - stash drop / clear                                   → stash loss
//   - stash (no verb) / push / save                        → silently sweeps the user's
//     uncommitted work into a stash
//     that's easy to forget
//   - checkout -b / -B <name> / switch -c / -C <name>      → creates a new branch and
//     switches off the user's branch
//   - filter-branch / filter-repo                          → history rewrite
//   - bfg (BFG Repo-Cleaner)                               → history rewrite
//
// Rationale: each of these is one keystroke from "lost work" or "I'm not
// where I thought I was" — uncommitted changes, untracked files, unmerged
// branches, stashed work, commits removed from shared history, or a branch
// silently swapped out from under the user. They're rare in normal flow and
// almost always intentional; an ask costs one click. The lossy edges of git
// are exactly where banner-blindness Allow-mashing hurts most.
type GitRule struct{}

func (GitRule) Name() string { return "git" }

func (GitRule) Triggers() []string {
	return []string{"git", "bfg"}
}

func (r GitRule) Check(cmd ExecutedCommand, _ *RuleEnv) *Decision {
	switch cmd.Name {
	case "bfg":
		// BFG Repo-Cleaner exists only to rewrite history. Carve out the
		// no-op invocations so plain --help doesn't pester users.
		for _, a := range cmd.Args {
			if a == "--help" || a == "-h" || a == "--version" {
				return nil
			}
		}
		return mkAsk(r.Name(), "git.history_rewrite",
			"BFG Repo-Cleaner rewrites git history", argv(cmd))

	case "git":
		verb := firstNonFlag(cmd.Args)
		switch verb {
		case "push":
			return r.checkPush(cmd)
		case "reset":
			if hasArg(cmd.Args, "--hard") {
				return mkAsk(r.Name(), "git.reset_hard",
					"git reset --hard discards uncommitted changes (and any commits past the target ref)", argv(cmd))
			}
		case "clean":
			// `-f` is required for clean to actually delete; without it the
			// command is a no-op (or refuses to run, depending on config).
			for _, a := range cmd.Args {
				if a == "--force" {
					return mkAsk(r.Name(), "git.clean_force",
						"git clean --force removes untracked files", argv(cmd))
				}
				if isShortFlagBundleContaining(a, 'f') {
					return mkAsk(r.Name(), "git.clean_force",
						"git clean -f removes untracked files", argv(cmd))
				}
			}
		case "checkout":
			// Trigger on pathspec form: `.` (wipe everything) or `--`
			// (anything after `--` is a filesystem-side wipe). Plain branch
			// switches (`git checkout main`) pass through.
			if hasArg(cmd.Args, ".") || hasArg(cmd.Args, "--") {
				return mkAsk(r.Name(), "git.checkout_pathspec",
					"git checkout with pathspec discards working-tree changes", argv(cmd))
			}
			// `-b <name>` / `-B <name>` create a new branch. The agent should
			// not silently invent a branch without the user's say-so.
			for _, a := range cmd.Args {
				if a == "-b" || a == "-B" {
					return mkAsk(r.Name(), "git.branch_create",
						"git checkout -b creates a new branch; confirm with the user first", argv(cmd))
				}
			}
		case "switch":
			// `-c <name>` / `-C <name>` create a new branch. Plain
			// `git switch main` switches between existing branches and is fine.
			for _, a := range cmd.Args {
				if a == "-c" || a == "-C" {
					return mkAsk(r.Name(), "git.branch_create",
						"git switch -c creates a new branch; confirm with the user first", argv(cmd))
				}
			}
		case "restore":
			// `git restore .` wipes the working tree to HEAD. `--source=...`
			// and `--staged` are the safe / intentional variants — let them
			// through. We only ask on the catastrophic `.` form.
			if !hasArg(cmd.Args, ".") {
				return nil
			}
			for _, a := range cmd.Args {
				if a == "--source" || strings.HasPrefix(a, "--source=") || a == "-s" {
					return nil
				}
				if a == "--staged" || a == "--cached" {
					return nil
				}
			}
			return mkAsk(r.Name(), "git.restore_pathspec",
				"git restore . discards working-tree changes", argv(cmd))
		case "branch":
			// `-D` is force-delete (drops unmerged commits). Plain `-d` is
			// safe — refuses on unmerged. `--delete --force` together is the
			// long-form equivalent of `-D`.
			delForce := false
			hasDelete := false
			hasForce := false
			for _, a := range cmd.Args {
				if a == "--delete" {
					hasDelete = true
				}
				if a == "--force" {
					hasForce = true
				}
				if isShortFlagBundleContaining(a, 'D') {
					delForce = true
				}
			}
			if delForce || (hasDelete && hasForce) {
				return mkAsk(r.Name(), "git.branch_force_delete",
					"git branch -D force-deletes a branch (drops unmerged commits)", argv(cmd))
			}
		case "stash":
			// `drop` / `clear` lose stashed work.
			// Bare `git stash`, `git stash push`, `git stash save` silently
			// sweep the user's uncommitted work into a stash that's easy to
			// forget about — ask before doing it. `pop`, `apply`, `list`,
			// `show`, `branch` are safe.
			rest := cmd.Args[indexOf(cmd.Args, "stash")+1:]
			second := firstNonFlag(rest)
			if second == "drop" || second == "clear" {
				return mkAsk(r.Name(), "git.stash_loss",
					"git stash "+second+" discards stashed work", argv(cmd))
			}
			if second == "" || second == "push" || second == "save" {
				verb := second
				if verb == "" {
					verb = "<implicit push>"
				}
				return mkAsk(r.Name(), "git.stash_create",
					"git stash "+verb+" sweeps the user's uncommitted work into a stash; confirm first", argv(cmd))
			}
		case "filter-branch":
			return mkAsk(r.Name(), "git.history_rewrite",
				"git filter-branch rewrites history", argv(cmd))
		case "filter-repo":
			// `--analyze` is read-only — generates a report, no rewrite.
			if hasArg(cmd.Args, "--analyze") {
				return nil
			}
			return mkAsk(r.Name(), "git.history_rewrite",
				"git filter-repo rewrites history", argv(cmd))
		}
	}
	return nil
}

// checkPush handles destructive `git push` flavors:
//   - --force / -f / --force-with-lease[=…] / +<refspec> → force push
//   - --delete / -d / refspec starting with `:`          → remote ref deletion
//
// Order of checks inside the loop matters only for which reason_code wins
// when multiple destructive flags appear (e.g. `-fd`); force_push wins.
func (r GitRule) checkPush(cmd ExecutedCommand) *Decision {
	for _, a := range cmd.Args {
		// --- Force push ---
		if a == "--force" || a == "-f" || a == "--force-with-lease" {
			return mkAsk(r.Name(), "git.force_push",
				"git push --force overwrites remote history", argv(cmd))
		}
		if strings.HasPrefix(a, "--force-with-lease=") {
			return mkAsk(r.Name(), "git.force_push",
				"git push --force-with-lease overwrites remote history", argv(cmd))
		}
		// `+HEAD` / `+refs/heads/main` refspec is force-push for that ref.
		if strings.HasPrefix(a, "+") && len(a) > 1 {
			return mkAsk(r.Name(), "git.force_push",
				"git push with `+refspec` force-overwrites remote ref", argv(cmd))
		}
		// Short-flag bundles. `-f` covered above; here we catch `-fu`, `-df`, …
		if isShortFlagBundleContaining(a, 'f') {
			return mkAsk(r.Name(), "git.force_push",
				"git push force flag in short-flag bundle", argv(cmd))
		}
		// --- Remote ref deletion ---
		if a == "--delete" {
			return mkAsk(r.Name(), "git.push_delete",
				"git push --delete removes remote ref", argv(cmd))
		}
		if isShortFlagBundleContaining(a, 'd') {
			return mkAsk(r.Name(), "git.push_delete",
				"git push -d deletes remote ref", argv(cmd))
		}
		if strings.HasPrefix(a, ":") && len(a) > 1 {
			return mkAsk(r.Name(), "git.push_delete",
				"git push refspec `:<ref>` deletes remote ref", argv(cmd))
		}
	}
	return nil
}

// isShortFlagBundleContaining checks whether arg is a short-flag bundle
// (starts with single `-`, not `--`) that contains the given flag character.
// Examples: `-f` matches 'f'; `-fdx` matches 'f', 'd', 'x'; `--force` does
// NOT match (long flag); `-` (bare dash) does NOT match.
func isShortFlagBundleContaining(arg string, flag rune) bool {
	if len(arg) < 2 || arg[0] != '-' || arg[1] == '-' {
		return false
	}
	return strings.ContainsRune(arg, flag)
}
