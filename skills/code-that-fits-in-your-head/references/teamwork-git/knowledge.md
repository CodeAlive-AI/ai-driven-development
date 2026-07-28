# Teamwork and Git Knowledge

> **Source note:** This book-derived theme includes 2026 editorial reframing for agent-authored changes. Agent-specific additions are not from Seemann.

Core concepts for how teams use Git, integrate work, and share code ownership.

## Overview

Version control and team workflow are not paperwork — they are levers for manoeuvrability and quality. Git, used tactically, lets a team experiment safely, integrate continuously, and share code ownership so no single person becomes a bottleneck. Process is a proxy for outcome: understand the motivation, and you know when to apply or bend it.

## Key Concepts

### Git as the Default VCS

**Definition**: A distributed version control system, typically paired with a centralised service (GitHub, Azure DevOps, GitLab, Bitbucket/Stash).

Most teams treat Git as little more than a way to push their code to a shared remote. That squanders its real value: tactical manoeuvrability. Because commits live on your hard drive until you push, you can experiment freely, edit local history, and only publish a coherent trail.

**Key points**:
- Initialise a Git repo as the first thing in a new code base (`git init`).
- Preserve enough Git understanding to inspect, recover, and automate history independently of a particular UI.

### Continuous Integration (the practice, not the server)

**Definition**: A working practice where every developer frequently merges their code with the mainline so the team stays converged.

Owning a CI server is not Continuous Integration. CI is the practice of keeping work compatible with the shared mainline. The appropriate cadence depends on concurrency, risk, and verification cost; a fixed number of hours is not the definition.

**Key points**:
- Integration means merging to mainline, not running a build server.
- Integrate or synchronize often enough to prevent expensive divergence.
- Writing everything on `master` is not CI — it confuses branch names with the actual problem (concurrent edits).
- Use feature flags or branch-by-abstraction when incomplete behavior must integrate safely.

### Coherent Commits and Manoeuvrability

**Definition**: Preserving coherent known-good states so you can diagnose, discard, reorder, resume, or recover work.

The problem with a "Death Star" commit is mixed concerns and unverifiable architecture, not raw size. A systematic migration may be large while still having one transformation, clear evidence, and a useful recovery point.

**Key points**:
- The commit history should be a series of snapshots of working software.
- Keep published checkpoints useful; avoid arbitrary per-file commits that obscure the change.
- Tactical manoeuvrability: change direction quickly, reset cheaply, keep side-branch experiments around.

### Collective Code Ownership

**Definition**: A team arrangement where at least two active maintainers are comfortable changing any part of the code base.

If a single person "owns" a module, they are a single point of failure — vacations, sickness, or leaving stalls the team. It also blocks refactoring across ownership boundaries. Collective ownership doesn't forbid specialisation; it requires overlap so more than one person knows any given area.

**Key points**:
- Raise the bus factor (also called lottery factor): how many people can be lost before development halts.
- The core question to answer "yes" to: *Does the team contain more than one person comfortable working with this part of the code?*
- Weak code ownership (natural owner, but everyone is allowed to change it) is acceptable; strong exclusive ownership is not.

### Pair Programming

**Definition**: Two developers collaborating in real time on the same problem, typically at one workstation.

Pair work produces continuous, on-the-go code review. A commit from a pair already represents agreement between two people, which is the most informal approval process possible and has minimal latency.

**Key points**:
- Rotate pairs across areas to prevent knowledge silos; pairing alone doesn't guarantee collective ownership.
- Not every developer thrives on it (it is exhausting for introverts and needs schedule sync), so it is usually mixed with other practices.

### Mob/Ensemble Programming

**Definition**: Three or more developers collaborating on the same problem at the same time, usually in a shared room or call.

Productivity is not typing speed. Mobbing is especially effective for knowledge transfer, coaching, and onboarding; teams that mobbed on test-driven practices kept doing them after the coach left. Diminishing returns kick in at large group sizes.

### Code Review Latency

**Definition**: The elapsed time between a change being ready and a reviewer reading it.

Code review is one of the few practices with documented effectiveness at finding defects, but only if the latency is short. Long waits lead to bugs discovered well after the author has moved on, producing unplanned firefighting work, missed deadlines, and crunch mode. Short latency makes defect prevention part of the rhythm instead of part of the problem.

**Key points**:
- Anchor reviews to existing daily rhythms (morning, post-lunch).
- Keep latency low enough that context and mainline compatibility are not lost. Risk and architecture matter more than a universal review stopwatch.

### Pull Requests and GitHub Flow

**Definition**: A lightweight workflow where you branch locally and issue a pull request (PR) on a central service to merge into `master`.

Even when you could self-merge, team policy should require someone else to review and sign off. PR review is a code review conducted asynchronously in writing, which means tone is easy to lose — be extra polite.

**Key points**:
- One PR has one coherent outcome. A systematic change may touch many files.
- Don't mix reformatting with substantive changes (unless reformatting *is* the change).
- Decline a change when architecture or evidence cannot be evaluated; do not rubber-stamp generated bulk.

## Terminology

| Term | Definition |
|------|------------|
| Commit-message policy | Repository convention for accurate, searchable rationale. |
| Continuous Integration | The practice of controlling divergence from shared mainline. |
| Merge hell | Painful conflicts caused by diverging long-lived branches. |
| Coherent commit | A known-good state with one explainable purpose. |
| Bus factor / lottery factor | The number of people the team can lose before development halts. |
| Collective code ownership | Every part of the code has at least two comfortable maintainers. |
| Weak code ownership | A "natural" owner exists, but anyone is allowed to change the code. |
| GitHub flow | Branch-and-PR workflow built on top of a centralised Git service. |
| Done done | Feature is complete and running in production, not merely "finished" locally. |
| Sunk cost fallacy | Accepting a bad change set because its author already spent days on it. |

## How It Relates To

- **Checklists (Ch 2)**: Using Git is the first item on the new-code-base checklist.
- **Readability**: The review question "will I be okay maintaining this?" is really "does this fit in my brain?".
- **Testing**: Verified, coherent checkpoints align naturally with red-green-refactor and provide useful recovery points.
- **Feature flags (Ch 10)**: The escape hatch that lets you integrate unfinished work without breaking mainline.

## Common Misconceptions

- **Myth**: "We have a CI server, so we do Continuous Integration."
  **Reality**: CI is a working practice (frequent merges to mainline), not a server. A server without the practice is just a build tool.

- **Myth**: "CI means no branches — work directly on master."
  **Reality**: The problem is concurrent edits, not branch names. Short-lived branches that merge frequently are still CI.

- **Myth**: "Git fixes merge hell."
  **Reality**: It doesn't. Merge hell comes from long-lived divergence; the tool is the same problem as any concurrent edit on a shared resource.

- **Myth**: "Pair programming halves productivity."
  **Reality**: Productivity is not keystrokes per hour. Pairs produce pre-reviewed, pre-approved code; evidence suggests it is efficient.

- **Myth**: "Code review slows us down."
  **Reality**: It shifts defect cost earlier, where it is cheap. Skipping review creates unplanned firefighting later, which is where deadlines actually die.

- **Myth**: "A commit message should describe what changed."
  **Reality**: The diff already shows *what*. The message is the best place to explain *why* — that is the highest-value question in software.

## Quick Reference

| Concept | One-Line Summary |
|---------|-----------------|
| Git tactically | Use local manoeuvrability: experiment, reset, edit history before push. |
| CI | Integrate according to divergence and risk; keep the mainline verifiably healthy. |
| Coherent commits | Record useful, known-good checkpoints without manufacturing microcommits. |
| Collective ownership | ≥2 people comfortable in every part of the code. |
| Pair programming | Real-time review + approval built-in, low latency. |
| Review evidence | Make architecture, intent, verification, and residual risk inspectable. |
| Large change sets | Accept systematic, well-specified work; reject incoherent or unverifiable bulk. |
| PR discipline | One thing per PR, tests passing, proper commit messages. |
