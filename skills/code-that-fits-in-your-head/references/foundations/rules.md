# Foundations Rules

Actionable rules for writing sustainable, humane code and maintaining the personal rhythm that supports it.

## Core Rules

### 1. Write Code for the Next Reader

You spend more time reading code than writing it. Every line is read many times.

- Optimise for readability, not typing speed.
- Treat every minute spent on readability as a tenfold future saving.
- When in doubt about a clever trick vs. plain code, choose plain code.
- Never accept "more code faster" as a win — it is more maintenance.

### 2. Keep Active Concepts Under Seven

Short-term memory tops out around seven items. The computer does not care, but you do.

- Limit dependencies per class/module to under seven.
- Keep cyclomatic complexity at most seven.
- Limit arguments per function.
- Write small, self-contained functions.
- If you cannot hold all the relevant state for a function in your head, the function is too big.

### 3. Make All Relevant Context Visible Locally

System 1 only reasons about information that is activated — what is on the screen right now. What You See Is All There Is.

- Place related code close together: dependencies, variables, and decisions required to understand a block should be visible simultaneously.
- Avoid global variables — they are off-screen state System 1 will not account for.
- Avoid hidden side effects — if a function touches state not in its signature, readers will miss it.
- Prefer explicit arguments and return values over ambient context.

### 4. Treat Code as a Liability, Not an Asset

More code means more to read, more to test, more places for bugs to hide.

- Delete aggressively; do not hoard code "in case".
- Resist generating large amounts of boilerplate or templated code.
- Before adding code, ask whether an existing abstraction could handle it.
- Prefer fewer, clearer lines over more lines that "do more".

### 5. Aim for Sustainability, Not Just Value

Some work (security, architecture, internal quality) has no measurable value — only measurable absence.

- Do not reject refactoring or quality work because it has no immediate business metric.
- Use checklists and treat warnings as errors to prevent cruft from forming.
- Expect to rely on experience and judgment — heuristics guide, they do not guarantee.
- Reject the "worse is better" impulse when it trades long-term survival for short-term speed.

### 6. Slow Down

Typing faster produces more code, not more value.

- Deliberately slow down when adding code.
- Prefer one well-considered change over several rushed ones.
- Treat "I need to slow down" as a neutral fact, not a criticism.

### 7. Time-Box Your Work

Work in 25-minute intervals with 5-minute breaks.

- Keep a countdown timer visible (kitchen timer, tray app, etc.).
- Use the visible timer to resist "just checking" Twitter / email / chat.
- Starting a big task is the hard part; tell yourself "I can look at this for 25 minutes".
- When the timer goes off, stop — even if you are in the zone.

### 8. Take Real Breaks

The 5-minute break only works if it is a real break.

- Get out of the chair. Leave the room if possible.
- Get away from the computer — physical movement matters.
- Breaks surface wasted work: better to waste 15 minutes than 3 hours.
- Insight arrives away from the keyboard, not at it. Plan for that.

### 9. Use Time Deliberately

Do not let the day happen to you.

- Reserve fixed blocks for learning (e.g. two 25-minute boxes per morning).
- Study textbooks, do exercises, answer others' questions — teaching is learning.
- Limit meetings: ask for an agenda; many meetings cancel themselves.
- Write things down — documentation scales, meetings do not.
- Do not work long hours; past a point, productivity goes negative.

### 10. Touch Type

Typing is not the bottleneck; the eyes are.

- Learn to touch type (a few weeks at one hour per day is enough).
- The point is not speed — it is keeping your eyes on the screen.
- Modern IDEs give constant feedback; hunt-and-peck typists miss it all.
- Let statement completion and IDE hints "do the typing" so your attention stays on code.

## Guidelines

Less strict recommendations:

- Prefer well-packaged libraries (sorting, hashing, databases) over reinventing computer science.
- Expect System 1 errors — double-check trivial-looking calculations and inferences.
- Take breaks that combine physical activity with being outdoors when possible.
- Do not try to learn a new programming language every year — spread learning across languages, testing, algorithms, design patterns, etc.

## Exceptions

When these rules may be relaxed:

- **Exploratory spike**: Early prototypes can sacrifice readability if thrown away immediately afterwards.
- **Fixed external contracts**: You cannot always reduce argument counts on externally defined APIs.
- **Genuine emergency**: An outage may justify long hours once — not as a pattern.

## Quick Reference

| Rule | Summary |
|------|---------|
| Read > Write | Optimise code for reading, not writing |
| Under seven | Dependencies, complexity, arguments all stay small |
| Visible context | All state a reader needs must be on screen |
| Code = liability | Less code is better |
| Sustainability | Long-term quality over short-term metric |
| Slow down | Typing speed is not productivity |
| 25-minute boxes | Work in intervals with visible countdown |
| Real breaks | Leave the chair, move, change scene |
| Deliberate time | Fixed learning blocks, minimal meetings, written docs |
| Touch type | Keep eyes on the screen, not the keyboard |
