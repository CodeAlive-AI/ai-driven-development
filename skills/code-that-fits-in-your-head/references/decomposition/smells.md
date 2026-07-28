# Decomposition Smells

> **Source note:** D1–D7 derive from the book theme; system-wide sprawl and current thresholds are 2026 editorial adaptations.

Code smells that signal a block needs to be decomposed, with how to detect and fix each. Use during code review and when responding to "this code feels off — what's wrong?"

---

## D1: High Cyclomatic Complexity

**What it is**: A single method has more than 15 independent pathways, or fewer paths whose interaction is still difficult to explain and verify.

**How to detect**:
- Count: start at 1, add 1 for every `if`, `for`, `foreach`, `while`, `do`, `case`, and `??`.
- Run Visual Studio's built-in metrics calculator (or equivalent).
- Use the project's configured metric when it has one; otherwise use 15 as a review trigger.

**Why it's bad**:
- Makes behavior and test coverage harder to reason about when paths interact.
- Each new branch requires another unit test.
- Often indicates mixed responsibilities, nested decisions, or duplicated conditions.

**How to fix**:
- Extract cohesive sections into helpers.
- Replace chained Boolean checks with a parser that returns the validated value.
- Introduce Parameter Objects for clusters of related arguments.

**Example**:
```csharp
// Smell: validation, parsing, policy, and persistence branches are mixed
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

## D2: Unfocused Method

**What it is**: A method that mixes responsibilities, abstraction levels, or effects so its purpose cannot be summarized precisely.

**How to detect**:
- Name the distinct reasons the method might change.
- Look for interleaved validation, policy, persistence, formatting, or transport logic.
- Check whether the reader must jump between unrelated concepts to explain the flow.

**Why it's bad**:
- Mixed responsibilities make changes spread and cause unrelated behavior to regress.
- Length alone is not the problem: a long cohesive transformation may be clearer than many tiny helpers.

**How to fix**:
- Extract a boundary only when it represents a meaningful responsibility or effect.
- Preserve cohesive algorithms and avoid helper chains that merely move lines elsewhere.

---

## D3: Too Many Variables

**What it is**: A method coordinates too many unrelated values, mutable states, or dependencies at once.

**How to detect**:
- Tally every local variable, every parameter, every class field or property touched by the method body.
- Group the names by domain concept; the smell is many interacting groups, not a universal count.

**Why it's bad**:
- Unrelated live values make invariants and update ordering difficult to track.
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
- Hidden effects make the signature an unreliable guide to behaviour and increase the state a reader must reconstruct.

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

## D8: System-Wide Sprawl

**What it is**: A locally simple change requires edits across unrelated modules, adds a dependency cycle, duplicates an existing rule, or extends a temporary migration path.

**How to detect**:
- Inspect dependency direction and cycles.
- Search for equivalent rules or abstractions before adding another.
- Review change history for files repeatedly modified together.
- Identify flags, adapters, and parallel implementations without a removal condition.

**Why it's bad**:
- Local method metrics can stay green while the architecture becomes a Big Ball of Mud.
- Future changes lose a predictable home and accumulate more cross-module coordination.

**How to fix**:
- Restore a clear ownership boundary and dependency direction.
- Consolidate duplicated rules.
- Complete or remove stale migration paths.
- Add an architecture check when the constraint is stable and mechanically expressible.

---

## Quick Detection Table

| ID | Smell | Key Indicator |
|----|-------|---------------|
| D1 | High cyclomatic complexity | Branch count + 1 > 15, or paths interact opaquely |
| D2 | Unfocused method | Mixed responsibilities, levels, or effects |
| D3 | Too much interacting state | Too many unrelated live concepts |
| D4 | Feature envy | Uses only one parameter's state; wants to be `static` |
| D5 | Lost in translation | Returns `bool` but caller re-parses |
| D6 | Nested side-effect Query | Predicate-shaped signature that secretly writes |
| D7 | Low-cohesion block | Section uses no class fields |
| D8 | System-wide sprawl | Cycles, duplicated rules, broad change surface, stale migration paths |
