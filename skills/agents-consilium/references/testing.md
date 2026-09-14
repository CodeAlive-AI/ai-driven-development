# Testing

The default suite uses fake backend CLIs, is offline, and spends no model tokens:

```bash
scripts/tests/run.sh
```

It covers backend argv safety, exact profile selection, model/effort resolution, stdout/stderr separation, artifacts, Grok streaming success/failure, live progress, credential redaction, prompt purity, all review progress styles, invocation-specific keys, human-readable ids, steerable adapters/mailbox lifecycle, concurrent Grok queue/sendNow behavior, cancel/idempotency/cleanup, and shared runtime contracts.

Quota parsing is tested offline for Codex multi-bucket limits, Grok `/usage`
fields, fail-closed display drift, shell-safe remote paths, and one bounded retry
after a transient Grok transport failure.

The shared-runtime checks include the closed event schema and protocol-drift rejection, backend capability resolution, declarative workflow plans and concurrency defaults, prompt-layer purity, fail-closed mode policy, and debug tape bounds.

Orchestration regressions also cover observer timeouts and interruption without
worker cancellation, wait-any readiness and dead-process handling, failed-abort
replacement rejection, durable Codex native resume, preserved original records,
profile/root mismatches, concurrent continuations, and no replay after failure.
Run this focused suite with `PYTHONPATH=scripts/lib python3
scripts/tests/steer/test_orchestration.py` from the skill directory.

Group-wait checks cover retained acknowledged statuses without repeated wakeups,
elapsed times, unrelated-run exclusion, and rejection of invalid acknowledgements.
Backend environment checks ensure nested delegation cannot inherit the parent's
artifact destination while preserving registry and output-root routing.

Edge cases include backend startup failure beside a healthy peer, simultaneous
success/failure/cancellation, lock contention during dead-supervisor observation,
structured results without final text, Codex active-turn status, and streamed
message completion without duplicate progress text.

OpenCode regressions exercise a permission-blocked fake server through detached
launch and wait-any, retained failure details, tool command visibility, nested
foreign-session filtering, and SSE lines larger than 64 KiB with Unicode content.

Opt-in real smoke tests spend tokens:

```bash
CONSILIUM_STEER_SMOKE=1 bash scripts/tests/steer/smoke_real.sh -a grok
```

## Cross-platform checks

Run `python scripts/tests/platform_test.py -v` from the skill directory with
native Python (3.11+). These tests spend no model tokens and cover all steer
imports, non-destructive PID probes, locks shared by two processes, nonblocking
wait deadlines, exclusive session claims/no replay, process-tree cleanup,
terminal-guard shutdown, and native supervisor Codex continuation. Windows also
checks Python/shell/batch launcher argument handling. Symlink rejection is
checked where the OS permits creating symlinks.

GitHub Actions runs these checks on Windows, Linux, and macOS, plus LF-only
config output and CLI help. The full existing shell suite runs on Linux/macOS;
its POSIX path and executable assumptions are not a Windows gate yet.
