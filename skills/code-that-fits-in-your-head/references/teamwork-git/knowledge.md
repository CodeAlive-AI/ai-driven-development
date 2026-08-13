# Teamwork and Git Knowledge

> **Source note:** This book-derived theme includes 2026 editorial reframing for agent-authored changes. Agent-specific additions are not from Seemann.

How teams use Git, integrate work, and share ownership so no single person or long-lived branch becomes a bottleneck.

## Overview

Version control and team workflow are levers for manoeuvrability and quality, not paperwork. Git used tactically lets a team experiment safely, integrate continuously, and keep ownership collective. Process is a proxy for outcome: understand the motivation, and you know when to apply or bend it.

## Key Concepts

### Continuous Integration (the practice, not the server)

CI is frequent merges with the mainline so the team stays converged — not owning a build server. Cadence depends on concurrency, risk, and verification cost; a fixed number of hours is not the definition. Integrate or synchronise often enough to prevent expensive divergence. Feature flags or branch-by-abstraction let incomplete behaviour integrate safely. Writing everything on `master` is not CI: it confuses branch names with concurrent edits.

### Coherent Commits and Manoeuvrability

Preserve coherent known-good states so you can diagnose, discard, reorder, resume, or recover. A "Death Star" commit mixes concerns and is unverifiable; a systematic migration may be large while still having one transformation, clear evidence, and a useful recovery point. The history should be a series of working-software snapshots — not arbitrary per-file microcommits.

### Collective Code Ownership

At least two active maintainers should be comfortable changing any part of the code. Exclusive single ownership is a bus-factor risk and blocks cross-boundary refactoring. Weak ownership (a natural owner, anyone may change) is fine. Pairing and mobbing count as human review when participants understand the change.

### Code Review Latency

Review finds defects only when latency is short. Long waits produce firefighting after the author has moved on. Keep latency low enough that context and mainline compatibility are not lost; risk and architecture matter more than a universal review stopwatch. Anchor reviews to existing daily rhythms.

### Pull Requests and Discipline

Even when self-merge is possible, require someone else to sign off. One PR has one coherent outcome (a systematic change may touch many files). Do not mix reformatting with substantive changes. Decline when architecture or evidence cannot be evaluated; do not rubber-stamp generated bulk. Be extra polite in written review — tone is easy to lose.

## How It Relates To

- **Checklists**: Git is the first item on a new-code-base checklist.
- **Testing**: Verified checkpoints align with red-green-refactor and recovery.
- **Feature flags**: Escape hatch that lets unfinished work integrate without breaking mainline.

## Common Misconceptions

- **Myth**: "We have a CI server, so we do Continuous Integration."
  **Reality**: CI is frequent merges to mainline, not a server. A server without the practice is just a build tool.

- **Myth**: "CI means no branches — work directly on master."
  **Reality**: The problem is concurrent edits, not branch names. Short-lived branches that merge frequently are still CI.

- **Myth**: "Git fixes merge hell."
  **Reality**: Merge hell comes from long-lived divergence, not the tool.

- **Myth**: "Code review slows us down."
  **Reality**: It shifts defect cost earlier. Skipping review creates unplanned firefighting later.

- **Myth**: "A commit message should describe what changed."
  **Reality**: The diff shows *what*. The message explains *why*.
