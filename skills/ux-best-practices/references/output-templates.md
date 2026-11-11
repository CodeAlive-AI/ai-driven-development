# Output formats

Choose a template and shorten it to fit the request. This is the skill's own working format, not the standard of an external organization.

## Severity scale

Use the team's own scale if it has one; otherwise use this internal scale of the skill:

- **S3, critical:** a key task is impossible, or significant data loss or a serious wrong action is possible.
- **S2, major:** an error, a workaround or a likely misunderstanding makes the task noticeably harder.
- **S1, moderate:** extra effort, but the task can still be completed.
- **S0, improvement:** visual or editorial polish with no established obstacle.

Keep severity, reach and cost of fix apart. Do not derive severity from the name of a WCAG criterion. If reach or frequency is unknown, say so. Do not invent numeric ratings.

## UX audit

**Context:** task, audience, platform, materials and assumptions.

**Key findings:** the most significant obstacles and the expected practical effect of the fixes, without invented percentages.

| ID / location | Observation and status | Impact on the task | S0–S3 / confidence | Change | Basis | Verification |
|---|---|---|---|---|---|---|
| UX-01 / screen, step, component | What is visible or reproducible; what is assumed | The specific obstacle | Severity; high/medium/low with the reason | Text, structure, behavior | ID and exact link; SC number where needed | Action and expected result |

**Order of work:** what to fix first, what to verify before implementation, dependencies. State reach and effort in words or actual data, not invented scores.

**Verified:** only the actions performed, with their conditions. **Still to verify:** inaccessible states and research. **What already works:** decisions to keep, if that helps avoid unnecessary rework.

## Flow specification

- **Task and success:** the intent and the observable outcome.
- **Main path:** entry → actions → result; significant branches.
- **Information structure:** objects, sections, labels, content priority.
- **States:** applicable variants and transitions.
- **Copy:** actions, instructions, errors and completion.
- **Accessibility:** semantics, keyboard/focus, sizes, contrast for the platform.
- **Trade-offs:** assumptions, alternatives, need for verification.
- **Acceptance:** scenarios, states and verifiable criteria.

| State | What the person sees | Available action | Data / focus | Exit condition |
|---|---|---|---|---|
| For example, submission error | An explanation tied to the field | Fix or retry safely | Input preserved; predictable focus | Data accepted or cancelled |

The row illustrates the form of a specification; it is not an observation about a real product.

## Hypothesis validation plan

**Question:** what is unknown? **Hypothesis:** what change will help, and why? **Audience:** whom and which context to study? **Method and sample:** why do they fit the question? **Task:** a neutral instruction. **Metric and decision rule:** what counts as an improvement, which consequences are unacceptable? **Limitation:** what the check will not establish?

## Implementation summary

Report: what changed; which obstacle was removed; where behavior changed; what was verified; which limitations remain. Add links to the changed artifacts if the environment allows. For a local fix, do not write a large report unless necessary.
