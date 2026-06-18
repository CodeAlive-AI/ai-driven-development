# Decomposition Rules

Hard thresholds and decomposition heuristics drawn from Chapter 7 and §13.1. Use these to answer "is this function too complex?" and "should I split this class?"

## Core Rules

### 1. Keep cyclomatic complexity at or below 7

Count branches (start at 1, add 1 for each `if`, `for`, `foreach`, `while`, `do`, `case`, and `??` in C#). If the count exceeds 7, refactor before adding more branches. Seven echoes the brain's short-term memory limit.

- Treat 7 as a ceiling, not a target.
- When a method sits right at 7, refactor prophylactically — the next change will push it over.
- Enforce via CI if possible. Rejecting changes that exceed the threshold hacks the "what you measure is what you get" effect.

### 2. Keep every method inside an 80 × 24 box

- Line width: 80 characters maximum.
- Line height: 24 lines maximum per method.
- Don't game the limit by packing multiple statements per line or writing wider lines.
- Configure your editor with a vertical guide at column 80.

**Example**:
```csharp
// Bad: one line, three statements — defeats the 80/24 spirit
var foo = 32; var bar = foo + 10; Console.WriteLine(bar);

// Good: one statement per line, within the box
var foo = 32;
var bar = foo + 10;
Console.WriteLine(bar);
```

### 3. Count variables when complexity feels wrong

Sum local variables + parameters + class fields/properties the method uses. If the total approaches or exceeds 7, the method is juggling too much. Consider a Parameter Object before adding another parameter.

### 4. Prefer sequential composition to nested composition

When you decompose, chain Queries so the output of one becomes the input of the next. Nested composition (objects inside objects inside objects) hides side effects and multiplies the chunks a reader must hold in mind. See `patterns.md`.

### 5. Favour pure functions; push side effects to the edges

- Write complex logic as referentially-transparent functions (deterministic, no side effects).
- Concentrate nondeterminism (time, GUIDs, random, I/O) and side effects in `Main`, controllers, and message handlers.
- This is the *functional core, imperative shell* style, and it applies to object-oriented languages too.

### 6. Move a method to the class it envies

If a method (often marked `static`) uses none of its declaring class's members and reads only one parameter's state, it suffers from Feature Envy. Move it onto the parameter's class. Prefer a property if the new member takes no input, has no preconditions, and cannot throw.

### 7. Extract blocks that use no instance members first

When decomposing a long method, look for sections that touch no class fields — those are the easiest, lowest-risk candidates for extraction. Blank-line groupings often reveal the seams.

### 8. Replace Boolean validation with parsing that returns the validated object

Do not return `bool` from validation. Return the stronger type or `null`/`Maybe<T>`. A Boolean forces callers to re-parse or re-inspect the input, duplicating work and losing type-level guarantees. (Full coverage lives in `encapsulation/`.)

### 9. Each class/method must fit in your head at its own zoom level

Fractal architecture: at the trunk, ~7 branches; inside each branch, ~7 more. A newcomer should be able to open the entry point, see no more than seven chunks, and know where to drill down for any detail.

### 10. Refactor when a metric crosses its threshold — not later

Don't wait until the code "feels" bad. By then, the metric has drifted far past the threshold and cleanup is expensive. Treat threshold breaches as the signal that the refactor window is *now*.

## Guidelines

Less-strict recommendations:

- Prefer 20-line C# methods; become uncomfortable near 30.
- In denser languages (Haskell, F#) treat 24 lines as already huge.
- Constructors must not have side effects; treating them as Queries lets you reason about them like pure functions.
- Mind `static` helper methods — they are a code smell worth investigating.
- Count lines *deleted* as the productivity metric, not lines added.
- Use blank-line groupings inside a method to reveal natural seams for extraction.

## Exceptions

When these rules may be relaxed:

- **At the system edge**: Controllers and `Main` orchestrate side effects — they *will* juggle nondeterminism. Keep them small but allow them to be imperative.
- **Domain emergencies**: Breaking a threshold temporarily to fix a production incident is acceptable; schedule the cleanup so the code returns under the limit.
- **Language density**: If your team uses a denser language or prefers 120×40, honour that — the point is having *a* threshold, not this specific one.
- **Interfaces and abstract methods**: Variable counts and cyclomatic complexity do not apply (no implementation).

## Quick Reference

| Rule | Summary |
|------|---------|
| Cyclomatic complexity ≤ 7 | Count branches + 1; refactor at the limit. |
| 80 × 24 method size | Fits a VT100 screen — and your brain. |
| Count variables | Locals + params + fields ≤ 7. |
| Sequential over nested | Chain Queries; don't bury side effects. |
| Pure core, imperative shell | Push I/O and time to the edge. |
| Move feature-envious methods | Place them on the class they read. |
| Extract no-field blocks first | They are the loosest and safest to pull out. |
| Parse, don't Boolean-validate | Return the stronger type or nothing. |
| Fractal at every zoom | Seven chunks at each level, recursively. |
| Refactor on threshold breach | Don't wait until the code "feels" legacy. |
