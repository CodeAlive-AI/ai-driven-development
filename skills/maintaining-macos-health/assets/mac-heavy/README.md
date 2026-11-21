# mac-heavy

`mac-heavy` coordinates CPU- and memory-heavy work on this Mac so busy jobs do not exhaust memory together. An idle holder can share the machine with another job.

Wrap local builds, lint, type checks, tests, package installs and land gates. Do not wrap version control, reading or searching, SSH, work running on the VM, uploads or downloads, or waiting for remote jobs or delegates. If something light is wrapped by mistake, it stops blocking once it is idle and its initial grace period has passed.

Run `mac-heavy command arguments...`. A busy holder or an ALERT memory guard makes new work wait; use a background shell job if you need to continue working. The default wait is 1800 seconds; `--wait 0` tries once. A timeout exits 75 and runs nothing. Use `--label text` to identify a job.

Run `mac-heavy --help` for usage and `mac-heavy status` to see holders, waiters, memory guard and recent ledger records. Use `--now` only on the owner's word for that invocation; it bypasses both queue and guard.

A holder is busy for its first 45 seconds, or when its process tree uses at least 50% CPU or 1024 MB RSS. Admission allows fewer than one busy holder. Processes that detach from the tree, such as build daemons, are not measured; the memory guard still covers them. The owner can override these thresholds using `MAC_HEAVY_GRACE`, `MAC_HEAVY_BUSY_CPU`, `MAC_HEAVY_BUSY_RSS_MB` and `MAC_HEAVY_MAX_BUSY`.

The ledger in `~/.local/state/mac-heavy/ledger.jsonl` records starts, ends, timeouts, basenames, project and label, but never command arguments or environment. It rotates at 10 MB or after one day and removes rotated files older than 30 days.

During transition, a live v1 `arai-heavy.lock` counts as a holder using its process tree and directory age. The v1 compatibility block can be removed after all v1 wrappers have exited.
