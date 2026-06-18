# Decomposition Patterns

Recomposition strategies: once you split a block, how do you put the pieces back together so the whole still fits in your head?

## Pattern: Sequential Composition

### Intent

Chain Queries so the output of one becomes the input of the next. Use instead of nesting objects inside objects, which hides side effects and inflates the chunk count.

### When to Use

- The method performs a pipeline of transformations over data.
- You can express each step as a Query (no side effect, returns data).
- You want the reader to see the full pipeline without drilling into dependencies.

### Structure

```csharp
var a = StepOne(input);
var b = StepTwo(a);
var c = StepThree(b);
return Finalise(c);
```

### Example

```csharp
// From the restaurant code base: WillAccept composed sequentially from
// constructor, Where + Overlaps, Allocate, Any + Fits — all Queries.
var seating = new Seating(SeatingDuration, candidate);
var relevantReservations = existingReservations.Where(seating.Overlaps);
var availableTables = Allocate(relevantReservations);
return availableTables.Any(t => t.Fits(candidate.Quantity));
```

### Benefits

- The reader can trace data flow top-to-bottom.
- Each step is testable in isolation.
- No hidden side effects — because no step has any.

### Considerations

- Requires that each step be a Query. If a step has side effects, push it outward.
- Works best when types chain cleanly; introduce small value objects when signatures don't line up.

---

## Pattern: Nested Composition (Use Sparingly)

### Intent

Compose objects by embedding one inside another (Composite, most Gang-of-Four patterns). Shown here so you recognise it and know when *not* to reach for it.

### Why It's Problematic

Every nested object adds side effects to what the reader must remember. By the outer shell you are tracking eight or nine chunks — past the memory limit. Query-looking methods at the top may hide Commands deep in the tree (smell D6).

### When It Is Acceptable

- Domain *is* a tree (UI widgets, filter chains, AST nodes).
- You deliberately want polymorphic substitution at a node.
- Otherwise prefer sequential composition and keep any tree shallow.

---

## Pattern: Functional Core, Imperative Shell

### Intent

Implement complex logic as pure functions; concentrate nondeterminism (time, GUIDs, random, I/O) and side effects at the system's edge.

### When to Use

- Any non-trivial domain logic.
- Controllers, message handlers, and `Main` — these are the shell.
- Whenever you want a function to be easy to test and free of mocks.

### Structure

```csharp
// Shell: gather inputs (nondeterministic), call pure core, apply side effect.
public async Task<ActionResult> Handle(SomeDto dto)
{
    var now = DateTime.Now;                       // nondeterministic
    var id = Guid.NewGuid();                      // nondeterministic
    var state = await repo.Read(...);              // I/O

    var decision = PureCore(now, id, state, dto); // pure

    if (decision.IsAccepted)
        await repo.Write(decision.Result);         // side effect
    return decision.ToResponse();
}
```

### Example

```csharp
// The WillAccept pure function decides; the Post shell performs the I/O.
[HttpPost]
public async Task<ActionResult> Post(ReservationDto dto)
{
    if (dto is null) throw new ArgumentNullException(nameof(dto));
    var id = dto.ParseId() ?? Guid.NewGuid();
    Reservation? r = dto.Validate(id);
    if (r is null) return new BadRequestResult();

    var reservations = await Repository
        .ReadReservations(r.At)
        .ConfigureAwait(false);

    if (!MaitreD.WillAccept(DateTime.Now, reservations, r))
        return NoTables500InternalServerError();

    await Repository.Create(r).ConfigureAwait(false);
    return Reservation201Created(r);
}
```

### Benefits

- Pure core is trivial to test (no mocks, no fakes).
- Shell stays thin; side effects are visible at a glance.
- Aligns with fractal architecture — the shell is the trunk, the core is where the branches live.

### Considerations

- Requires discipline to keep the core pure; resist injecting clocks or random generators into it — pass those values in.
- Works in C# just as well as in functional languages.

---

## Pattern: Referential Transparency Replacement

### Intent

Reason about a pure function call by mentally replacing it with its return value, collapsing arbitrary internal complexity to a single chunk.

### When to Use

- Reading or reviewing code that calls a pure function.
- Deciding whether a helper can be treated as one chunk — it can, if it is pure.

### Structure

```csharp
// Once you know Foo(x, y) returns 42, treat the expression as 42.
var result = Bar(Foo(x, y), z);   // in your head: Bar(42, z)
```

### Benefits & Considerations

- Works only if the function is deterministic *and* side-effect-free.
- Breaks the moment a "pure" function starts reading wall-clock time or mutating shared state.
- Pure functions always compose when output and input types line up.

---

## Pattern: Hex Flower (Decomposition Heuristic)

### Intent

A thinking tool: draw seven hexagons, label each with one chunk (a branch, a variable, a hidden side effect). If all seven are full and you are about to add more, decompose now.

### When to Use

- Before adding a new branch to a method at the threshold.
- When a method feels heavy but the metric is still within limits.
- When picking the first block to extract.

### Example

For the `Post` method after extracting `Validate()`, only four hexagons fill: `dto NULL`, `Validate NULL`, `TOO LITTLE CAPACITY`, `HAPPY PATH`. Three slots remain as headroom.

### Considerations

- Heuristic, not a metric. Use alongside cyclomatic complexity and variable counts.
- Catches hidden chunks (side effects buried in Queries) that metrics miss.

---

## Pattern Selection Guide

| Situation | Recommended Pattern |
|-----------|--------------------|
| Pipeline of data transformations | Sequential Composition |
| Controller or message handler | Functional Core, Imperative Shell |
| Complex domain logic | Pure functions + Referential Transparency Replacement |
| Method feels crowded | Hex Flower diagnosis |
| You are tempted to nest objects deeply | Reconsider — prefer sequential |
