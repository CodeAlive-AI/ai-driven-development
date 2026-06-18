# Decomposition Smells

Code smells that signal a block needs to be decomposed, with how to detect and fix each. Use during code review and when responding to "this code feels off — what's wrong?"

---

## D1: High Cyclomatic Complexity

**What it is**: A single method has more than seven independent pathways.

**How to detect**:
- Count: start at 1, add 1 for every `if`, `for`, `foreach`, `while`, `do`, `case`, and `??`.
- Run Visual Studio's built-in metrics calculator (or equivalent).
- The hex flower is full — no room for another chunk.

**Why it's bad**:
- Exceeds working-memory capacity; the reader must commit structure to long-term memory.
- Each new branch requires another unit test.
- Creeps upward unnoticed; past 15-20 the code is often unsalvageable.

**How to fix**:
- Extract cohesive sections into helpers.
- Replace chained Boolean checks with a parser that returns the validated value.
- Introduce Parameter Objects for clusters of related arguments.

**Example**:
```csharp
// Smell: cyclomatic complexity of 7, right at the ceiling
public async Task<ActionResult> Post(ReservationDto dto)
{
    if (dto is null) throw new ArgumentNullException(nameof(dto));
    if (!DateTime.TryParse(dto.At, out var d)) return new BadRequestResult();
    if (dto.Email is null) return new BadRequestResult();
    if (dto.Quantity < 1) return new BadRequestResult();
    // ...more branches, plus a ?? that also counts...
}

// Fixed: extract to a Validate method that returns the domain object
public async Task<ActionResult> Post(ReservationDto dto)
{
    if (dto is null) throw new ArgumentNullException(nameof(dto));
    Reservation? r = dto.Validate();
    if (r is null) return new BadRequestResult();
    // remaining logic operates on a guaranteed-valid Reservation
}
```

---

## D2: Long Method (80/24 Violation)

**What it is**: A method that does not fit in an 80 × 24 character box.

**How to detect**:
- Check line count; enable an 80-column ruler to catch wide lines.
- Methods approaching 20 lines in C# should already feel uncomfortable.

**Why it's bad**:
- Reader cannot see start and end together; correlates with higher cyclomatic complexity and variable count; prevents side-by-side viewing of test and implementation.

**How to fix**:
- Identify blank-line groupings — those are natural seams.
- Extract the first group that touches no class fields (lowest risk), then continue.

---

## D3: Too Many Variables

**What it is**: A method juggles more than seven distinct names — locals, parameters, and fields combined.

**How to detect**:
- Tally every local variable, every parameter, every class field or property touched by the method body.
- If the count approaches or exceeds seven, the method is overloaded.

**Why it's bad**:
- Each name occupies a memory slot; when you run out of slots, you lose track.
- Often predicts bugs, because the programmer has already lost track.

**How to fix**:
- Group related parameters into a Parameter Object.
- Split the method so each smaller method handles fewer names.
- Push computed data further along a sequential composition instead of holding it in local state.

---

## D4: Feature Envy

**What it is**: A method — often `static` — that reads one parameter's state but ignores its own class's members.

**How to detect**:
- Method takes a type as a parameter and uses only that parameter's properties.
- Compiler or analyser suggests `static` (e.g. C# rule CA1822: *Mark members as static*).
- Asking "what does this operate on?" yields a different class than the one it lives in.

**Why it's bad**:
- Couples two classes through a third location.
- Often signals that an abstraction has been split in the wrong place.

**How to fix**:
- Move the method onto the class whose features it envies.
- If the new member takes no input, has no preconditions, and cannot throw, make it a property (per .NET design guidelines).
- Keep it `internal` first; widen visibility only when justified.

**Example**:
```csharp
// Smell: static helper envies ReservationDto
private static bool IsValid(ReservationDto dto)
{
    return DateTime.TryParse(dto.At, out _)
        && !(dto.Email is null)
        && 0 < dto.Quantity;
}

// Fixed: moved onto ReservationDto as a property
internal bool IsValid
{
    get
    {
        return DateTime.TryParse(At, out _)
            && !(Email is null)
            && 0 < Quantity;
    }
}
```

---

## D5: Lost in Translation

**What it is**: A helper that abstracts too aggressively, forcing callers to redo work the helper already did.

**How to detect**:
- The helper returns `bool` but the caller later needs the parsed value anyway.
- The caller uses the null-forgiving operator `!` (or equivalent) to bypass compiler checks that the helper invalidated.
- Data is parsed, discarded, and re-parsed downstream.

**Why it's bad**:
- Duplicates work.
- Breaks compiler flow analysis (forces null-forgiving operators).
- Signals a weak abstraction: too much eliminated, too little amplified.

**How to fix**:
- Change the signature to return the stronger type (e.g. `Reservation?` instead of `bool`).
- Adopt Parse-Don't-Validate (covered in `encapsulation/`): projects DTO input into a domain object if preconditions hold.

---

## D6: Nested Composition Hiding Side Effects

**What it is**: A Query-looking method that performs side effects inside nested object graphs.

**How to detect**:
- Signature reads like a predicate (`Task<bool> Check(Reservation r)`) but the implementation also writes to a database or sends an email.
- X-ing out the method name leaves a signature that suggests asking, not acting.
- Calling code uses the return value only to choose an HTTP status — yet data is saved.

**Why it's bad**:
- Violates Command Query Separation.
- Cyclomatic complexity underestimates the real load because hidden effects add chunks.
- Each hidden effect is 14 percent of a seven-chunk memory budget.

**How to fix**:
- Split Commands from Queries; let the Query return data and have the caller perform the side effect.
- Re-compose sequentially. See `patterns.md`.

---

## D7: Low Cohesion Section Inside a Class

**What it is**: A contiguous block inside a class that does not touch any of that class's fields.

**How to detect**:
- Block uses only local variables and method parameters.
- Static analyser suggests the enclosing method could be `static`.
- Surrounding sections *do* use class fields — the low-cohesion block sticks out.

**Why it's bad**:
- Signals the block belongs somewhere else.
- These blocks are the safest and most rewarding extraction targets.

**How to fix**:
- Extract a helper; evaluate whether it belongs on a different class (see D4, Feature Envy).
- Kent Beck: "Things that change at the same rate belong together."

---

## Quick Detection Table

| ID | Smell | Key Indicator |
|----|-------|---------------|
| D1 | High cyclomatic complexity | Branch count + 1 > 7 |
| D2 | Long method | Does not fit in 80 × 24 |
| D3 | Too many variables | Locals + params + fields > 7 |
| D4 | Feature envy | Uses only one parameter's state; wants to be `static` |
| D5 | Lost in translation | Returns `bool` but caller re-parses |
| D6 | Nested side-effect Query | Predicate-shaped signature that secretly writes |
| D7 | Low-cohesion block | Section uses no class fields |
