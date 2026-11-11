# Performance and waiting

Sources verified 2026-10-21.

## PF-01 — measurement

Source: [Web Vitals](https://web.dev/articles/vitals), Philip Walton / Google web.dev; published 2020-05-04, updated 2024-10-31. These are Google's official web benchmarks, not WCAG criteria and not a complete assessment of usability.

| Metric | What it characterizes | "Good" threshold |
|---|---|---|
| LCP | Appearance of the main large content | ≤ 2.5 s |
| INP | Responsiveness of interactions | ≤ 200 ms |
| CLS | Visual stability | ≤ 0.1 |

Assess the **75th percentile**, separating mobile and desktop. Do not substitute a single lab run for field data. Without field data, label a lab result as diagnostic. Use INP, not FID, as the current Core Web Vitals metric. Before making a claim about the current set of metrics, recheck the official source.

## Behavior while waiting: skill synthesis

Use DS08 and H01 together. Give a noticeable response to the action without declaring the operation complete before it is confirmed. During a local load, keep independent actions available. Show definite progress only when it is measurable; do not invent percentages or finish times. For a long process, consider cancellation, continuing in the background and returning to the result.

Reserve space for content that is loading to reduce unexpected shifts. Mark stale data if you show it during a refresh. On retry, account for the risk of duplication and for partial results. A skeleton or animation does not replace fixing the delay.

For a long wait, check progressive results, activity indicators, time estimates and cancellation where appropriate.

## Verification

Walk through the scenario with realistic latency, a network error and a repeated action. Check that input is preserved and that the flow continues after recovery. Record the device, connection, measurement conditions and metric; do not claim speed from a screenshot. Do not present the historical Doherty Threshold as a general SLA for an application.
