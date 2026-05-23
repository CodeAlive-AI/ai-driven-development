package main

import "strings"

// hasNoOpDryRunFlag returns true when argv explicitly selects a no-op dry-run
// mode. Last matching flag wins, matching common CLI option semantics.
func hasNoOpDryRunFlag(args []string) bool {
	dryRun := false
	for _, a := range args {
		switch {
		case a == "--dry-run" || a == "--dryrun":
			dryRun = true
		case a == "--no-dry-run" || a == "--no-dryrun":
			dryRun = false
		case strings.HasPrefix(a, "--dry-run="):
			dryRun = dryRunValueIsNoOp(strings.TrimPrefix(a, "--dry-run="))
		case strings.HasPrefix(a, "--dryrun="):
			dryRun = dryRunValueIsNoOp(strings.TrimPrefix(a, "--dryrun="))
		}
	}
	return dryRun
}

func dryRunValueIsNoOp(v string) bool {
	switch strings.ToLower(v) {
	case "", "0", "false", "no", "none":
		return false
	default:
		return true
	}
}

func hasFlywayDryRunOutput(args []string) bool {
	for _, a := range args {
		if a == "-dryRunOutput" ||
			strings.HasPrefix(a, "-dryRunOutput=") ||
			a == "--dry-run-output" ||
			strings.HasPrefix(a, "--dry-run-output=") {
			return true
		}
	}
	return false
}
