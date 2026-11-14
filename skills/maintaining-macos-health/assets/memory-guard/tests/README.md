`test.sh` compiles and runs the pure core tests with AddressSanitizer and
UndefinedBehaviorSanitizer, then builds a small helper and the native guard and
runs the child-only real-signal integration harness. Core coverage includes 23
named scenarios and 10,000 randomized steps. Integration cases feed fake metrics
to descendants of the harness; each helper allocates at most 8 MiB.

Run the sequential suite without creating real memory pressure:

```sh
skills/maintaining-macos-health/assets/memory-guard/test.sh
```

The integration harness checks ALERT freeze and CALM resume, EMERGENCY kill
ordering and tier gates, observe-mode no-signal behavior, SIGTERM cleanup, stale
process identity rejection, and recovery of a partially frozen process group.
