# Testing

The default suite uses fake backend CLIs, is offline, and spends no model tokens:

```bash
scripts/tests/run.sh
```

It covers backend argv safety, exact profile selection, model/effort resolution, stdout/stderr separation, artifacts, Grok streaming success/failure, live progress, local/remote explore source resolution and cleanup, credential redaction, transport blocking, prompt purity, content-free exploration progress, all review progress styles, invocation-specific keys, human-readable ids, steerable adapters/mailbox lifecycle, concurrent Grok queue/sendNow behavior, cancel/idempotency/cleanup, and shared runtime contracts.

The shared-runtime checks include the closed event schema and protocol-drift rejection, backend capability resolution, declarative workflow plans and concurrency defaults, prompt-layer purity, fail-closed mode policy, and debug tape bounds.

Opt-in real smoke tests spend tokens:

```bash
CONSILIUM_STEER_SMOKE=1 bash scripts/tests/steer/smoke_real.sh -a grok
```
