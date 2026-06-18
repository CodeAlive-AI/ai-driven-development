# Decomposition Knowledge

Core concepts for when and how to split code so every block fits in a reader's short-term memory.

## Overview

Code bases are not born as legacy code — they rot gradually as complexity creeps past the thresholds a human brain can track. Decomposition is the discipline of actively splitting code before it crosses those thresholds, using concrete metrics (cyclomatic complexity, lines of code, variable count) to detect when a block has grown too big to fit in your head.

## Key Concepts

### Code Rot

**Definition**: Gradual accumulation of complexity that, if unmonitored, quietly carries a code base across the threshold of comprehensibility.

If you don't pay attention to a complexity metric, you pass 7 without noticing, then 10, then 15 and 20. By the time the code feels obviously bad, it is often too late to salvage. Rot works "like boiling the proverbial frog."

### The 7±2 Working Memory Limit

**Definition**: Human short-term memory holds roughly seven "chunks" of information simultaneously.

This is the symbolic anchor behind every threshold in this chapter. When a piece of code forces the reader to juggle more than seven things at once, it stops fitting in the brain and they must commit it to long-term memory — which is how code becomes legacy.

### Cyclomatic Complexity

**Definition**: A measure of the number of independent pathways through a piece of code.

**Key points**:
- Minimum value is 1 (straight-line code has one path).
- Start at 1, increment by 1 for each branching or looping keyword.
- In C# that means: `if`, `for`, `foreach`, `while`, `do`, each `case` in a `switch`, and `??` (null-coalescing counts as a branch).
- Useful because it doubles as a guide for unit-test coverage — you need at least one test per pathway.

### Lines of Code

**Definition**: The simplest predictor of complexity — the more lines, the worse the code base.

Preliminary research suggests raw LoC is the most pragmatic predictor of complexity. Lines of code is a productivity metric only if you count lines *deleted*.

### The 80/24 Rule

**Definition**: A method should fit in an 80-character-wide by 24-line-tall box, echoing the classic VT100 terminal.

**Key points**:
- 80-column width: long-established industry standard.
- 24-line height: the maximum size of a single method.
- Both numbers are arbitrary (a team could choose 120×40), but the point is *having* a threshold.
- Don't cheat by writing wider lines or stuffing multiple statements per line — that defeats the purpose.
- On modern screens, keeping methods small lets you view unit test and code side-by-side.

### Cohesion

**Definition**: How tightly the members of a class belong together. Kent Beck: "Things that change at the same rate belong together. Things that change at different rates belong apart."

**Key points**:
- Maximum cohesion: every method uses every class field.
- Minimum cohesion: each method uses a disjoint set of fields.
- A block that uses *no* class fields at all is an even stronger candidate for extraction — it doesn't belong in that class.

### Feature Envy

**Definition**: A method that is more interested in another class's data than its own.

A static helper that takes some other type as a parameter and reads only that parameter's state is the classic signature. The fix is to move the method onto the class whose data it envies.

### Fractal Architecture

**Definition**: An architecture where, at every zoom level, the code fits in the reader's brain — seven or fewer chunks at the top, seven or fewer inside each chunk, and so on all the way down.

**Key points**:
- Self-similar structure: trunk → ~7 branches → ~7 sub-branches → leaves.
- Lower-level details must collapse into a single abstract chunk when viewed from above.
- Higher-level details must be explicit — visible as method parameters or injected dependencies ("what you see is all there is").
- Does not happen by itself — it requires explicit, ongoing attention to complexity.

### Hex Flower

**Definition**: A visual metaphor placing the seven memory slots as hexagons in a flower shape; used to reason about whether the chunks of a method still fit in short-term memory.

Draw one hexagon per pathway (or variable, or chunk). If all seven hexagons are filled, adding more complexity will push the code out of your brain.

### Counting Variables

**Definition**: An alternate complexity lens — tally every distinct object touched by a method.

Include local variables, method parameters, *and* class fields/properties used. Helpful especially when deciding whether to add another parameter: four parameters sounds fine, but if they interact with five locals and three fields, that is twelve things to track.

### Referential Transparency / Pure Functions

**Definition**: A deterministic function with no side effects. Given the same input, it always produces the same output, and the act of calling it changes nothing observable.

**Key points**:
- A pure function call can be replaced by its return value — that is the definition of referential transparency.
- Pure functions compose freely: if the output type of one matches the input type of another, sequential composition always works.
- They eliminate the irrelevant (the algorithm) and amplify the essential (the result).
- They enable "functional core, imperative shell" — complex logic as pure functions, side effects pushed to the edges (Main, controllers, message handlers).

## Terminology

| Term | Definition |
|------|------------|
| Code rot | Gradual, unnoticed growth of complexity until the code becomes legacy. |
| Cyclomatic complexity | Count of independent paths through code; start at 1, add 1 per branch/loop. |
| 80/24 rule | Method fits in 80-column by 24-line terminal box. |
| Chunk | A single item occupying one short-term-memory slot. |
| Cohesion | Degree to which a class's members belong together. |
| Feature envy | Method more interested in another class's data than its own. |
| Hex flower | Seven-hexagon visualisation of memory capacity. |
| Fractal architecture | Code that fits in your head at every zoom level. |
| Pure function | Deterministic, side-effect-free function. |
| Referential transparency | Property allowing a call to be replaced by its result. |

## How It Relates To

- **Encapsulation**: Decomposition asks *where* to split; encapsulation (Ch 5) asks *what invariants* each resulting piece protects. Parse-Don't-Validate lives with encapsulation.
- **API Design (Ch 8)**: Once you decompose a block, Ch 8 tells you how to shape the new parts.
- **Separation of Concerns (Ch 13)**: Nested vs. sequential composition is how you put decomposed pieces back together.
- **Testing**: Cyclomatic complexity doubles as a lower bound on the number of unit tests a method needs.

## Common Misconceptions

- **Myth**: "Seven is a hard, scientific cap."
  **Reality**: Seven is a symbolic anchor for working-memory capacity. The value of the rule comes from *having* a threshold, not from the number itself.

- **Myth**: "Extracting a helper method always reduces complexity."
  **Reality**: It only reduces *perceived* complexity if the caller can treat the helper as a single chunk. A bad abstraction like a Boolean `IsValid` that forces re-parsing downstream just moves complexity around.

- **Myth**: "Cyclomatic complexity captures everything."
  **Reality**: Nested composition can hide side effects that the metric does not see. Counting variables and reading signatures matters too.

- **Myth**: "Lines of code is a productivity metric."
  **Reality**: More lines make the code worse. The only productive LoC metric is lines *deleted*.

## Quick Reference

| Concept | One-Line Summary |
|---------|-----------------|
| Code rot | Complexity creeps past thresholds unnoticed. |
| 7±2 | Short-term memory caps at roughly seven chunks. |
| Cyclomatic complexity | Count branches + 1; keep at or below 7. |
| 80/24 rule | Method fits in 80×24 character box. |
| Cohesion | Things that change together belong together. |
| Feature envy | Method wants another class's data — move it there. |
| Fractal architecture | Fits in your head at every zoom level. |
| Pure function | Deterministic and side-effect-free; replaceable by its result. |
