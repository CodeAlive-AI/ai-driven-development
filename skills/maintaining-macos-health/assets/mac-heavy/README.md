# mac-heavy

A cooperative single slot for resource-intensive work **already authorized** to run on the Mac. Builds, Docker, e2e and broad suites still belong on the dev VM unless the owner grants a specific exception. No PATH shim is installed; light commands such as `dotnet --version` run unchanged.

```sh
mac-heavy pnpm check:quick app
mac-heavy --label unit-tests -- pnpm exec vitest run path/to/test
mac-heavy --wait 0 -- pnpm exec vitest run path/to/test
mac-heavy status
```

`--wait` defaults to 1800 seconds and accepts 0–21600; 0 tries once. Queue ordering is not guaranteed. Wait output identifies the holder and its state; stopped holders retain the slot. Timeout exits 75 and does not run the command. Ctrl-C while waiting cancels the wait. The guard is the pressure source: fresh CALM permits entry; ALERT/EMERGENCY wait. A missing, invalid, wrong-boot or 10-second-old status produces a warning and slot-only admission. An inherited matching `MAC_HEAVY_LEASE` makes nested calls inline. A stale or foreign lease is reported and ignored. This marker coordinates cooperating processes; it is not a security boundary and is not a quota for jobs started in parallel under one lease.

**Agents:** shell tools often time out before the 30-minute queue. Start `mac-heavy` with the tool's background/long-running mode (Claude Code `run_in_background`, Codex background/long-running command), then inspect progress; or use `--wait 0` and retry later. Do not hold the slot while waiting for a detached or remote delegate that cannot inherit the lease.

`mac-heavy --now -- command ...` explicitly bypasses both slot and pressure and logs `bypass=true`. Agents use it only on the owner's explicit instruction for that invocation. It does not authorize otherwise prohibited local work.

`status` displays the holder, best-effort waiters, guard snapshot and last five ledger entries. Logs under `~/.local/state/mac-heavy/ledger.jsonl` contain command basenames, project and labels, never arguments, environment or lease. Labels must not contain secrets. Logging errors are visible but do not stop the job. Files rotate at 10 MiB or one day and old rotations are deleted after 30 days.

If the holder is suspended, inspect `mac-heavy status` and the memory guard log. Do not remove a live holder's lock or resume a guard-stopped job. A dead holder, changed process start identity or different boot is reclaimed; a missing PID gets five seconds. Old versions of arai's `heavy.sh` have their own unsafe stale-cleanup and do not understand nested leases. Drain old jobs and update every active workspace before migrating; never nest an old wrapper inside this one. A different `TMPDIR` is reported and ignored for this wrapper; a legacy wrapper using that different path is a separate lock. Shell background jobs that outlive the command are not supervised and must not be used to escape the slot.

The child stays in the wrapper's process group and shares its terminal. Bash 3.2 ignores interrupts for background commands without job control, so a standard Perl `exec` trampoline restores the child's normal INT/QUIT dispositions before starting it. Terminal Ctrl-C reaches both; TERM and HUP sent to the wrapper are forwarded once to the child. A stopped supervisor or child can block waiters until their deadline; the wrapper never changes the guard's safety policy.

Reclaimer identity is stored in a short-lived mutex; a dead, reused or sufficiently old identity can be reclaimed. A kernel advisory lock serializes recovery and is released on process death. Ledger appends and rotation use a separate kernel advisory lock. If it remains busy for two seconds, the best-effort ledger warns and skips that event rather than allowing overlapping writers.
