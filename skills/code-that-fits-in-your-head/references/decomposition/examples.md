# Decomposition Examples

Before/after refactorings drawn from Chapter 7 and §13.1 of the restaurant reservation code base.

## Example 1: Extracting a Low-Cohesion Guard-Clause Block

### Before

The original `Post` method (listing 6.9) has cyclomatic complexity 7 and fills an 80 × 24 box exactly. It mixes validation (no class fields) with repository I/O (uses `Repository`). The first section is the best extraction candidate because it uses no instance members.

### After

```csharp
// Step 1: extracted helper. No class fields used → marked static.
private static bool IsValid(ReservationDto dto)
{
    return DateTime.TryParse(dto.At, out _)
        && !(dto.Email is null)
        && 0 < dto.Quantity;
}

// Step 2: caller shrinks to 22 lines, cyclomatic complexity 5.
public async Task<ActionResult> Post(ReservationDto dto)
{
    if (dto is null)
        throw new ArgumentNullException(nameof(dto));
    if (!IsValid(dto))
        return new BadRequestResult();
    var d = DateTime.Parse(dto.At!, CultureInfo.InvariantCulture);
    var reservations =
        await Repository.ReadReservations(d).ConfigureAwait(false);
    int reservedSeats = reservations.Sum(r => r.Quantity);
    if (10 < reservedSeats + dto.Quantity)
        return new StatusCodeResult(
            StatusCodes.Status500InternalServerError);
    var r =
        new Reservation(d, dto.Email!, dto.Name ?? "", dto.Quantity);
    await Repository.Create(r).ConfigureAwait(false);
    return new NoContentResult();
}
```

### Changes Made

1. Extracted the first guard-clause block (no class fields) into `IsValid` — chosen because its low cohesion with the controller's fields made it the most conspicuous seam.
2. `IsValid` is marked `static` because a code analyser detected no instance-member usage; this is already a hint of Feature Envy (see Example 2).
3. The hex flower for the caller drops from seven chunks to five — the three validation branches collapse into the single chunk `!IsValid`.

---

## Example 2: Fixing Feature Envy by Moving the Method

### Problem with Example 1

`IsValid` takes a `ReservationDto` parameter and reads only that parameter's state. It envies `ReservationDto`'s features. Also, the `static` marker is itself a code smell in object-oriented design.

### After

```csharp
// IsValid moved onto the class it envied, turned into a property
// because it takes no input, has no preconditions, and can't throw.
internal bool IsValid
{
    get
    {
        return DateTime.TryParse(At, out _)
            && !(Email is null)
            && 0 < Quantity;
    }
}

// Controller call site becomes:
if (!dto.IsValid)
    return new BadRequestResult();
```

### Changes Made

1. Moved the method onto `ReservationDto` — the class whose features it used.
2. Converted method to a property per .NET Framework Design Guidelines (no input, no preconditions, no exceptions).
3. Kept visibility `internal` for now; widen later if other modules need it.
4. Removed the `static` smell.

### Still Not Good Enough

Even after this fix, the surrounding `Post` method must use the null-forgiving operator `!` on `dto.At` and `dto.Email`, and must re-parse `dto.At`. That is the *Lost in Translation* smell (D5) — the Boolean `IsValid` eliminated too much. The real fix belongs in `encapsulation/` under Parse-Don't-Validate: replace the Boolean with a method that returns the validated `Reservation?`.

---

## Example 3: Sequential Composition in a Domain Query

### The `WillAccept` Pipeline

`WillAccept` decides whether a restaurant can accept a reservation. It composes four Queries sequentially — constructor, `Where` + `Overlaps`, `Allocate`, `Any` + `Fits` — none of which has side effects.

```csharp
// Overlaps: a Query that tests whether two seatings overlap.
internal bool Overlaps(Reservation other)
{
    var otherSeating = new Seating(SeatingDuration, other);
    return Start < otherSeating.End && otherSeating.Start < End;
}

// Allocate: another Query, returning the remaining available tables.
private IEnumerable<Table> Allocate(
    IEnumerable<Reservation> reservations)
{
    List<Table> availableTables = Tables.ToList();
    foreach (var r in reservations)
    {
        var table = availableTables.Find(t => t.Fits(r.Quantity));
        if (table is { })
        {
            availableTables.Remove(table);
            if (table.IsCommunal)
                availableTables.Add(table.Reserve(r.Quantity));
        }
    }
    return availableTables;
}
```

### Why It Works

- Every step is a Query (Command Query Separation holds).
- The output of one Query is the input of the next (`Where` → `Allocate` → `Any`).
- Once `WillAccept` returns, nothing else has changed in the world — the reader can forget how it reached the result.
- No mocks or fakes are required to test any individual step.

---

## Example 4: Replacing Nested Composition with Sequential Composition

### Before (Bad — do not write code like this)

```csharp
// Cyclomatic complexity 4, 17 lines, only 4 objects "activated".
// But one of those objects is an injected IRestaurantManager that
// hides Manager.TrySave — a method that BOTH saves to the database
// AND returns a bool. The Query-looking Check actually performs I/O.
public IRestaurantManager Manager { get; }
public async Task<ActionResult> Post(ReservationDto dto)
{
    if (dto is null)
        throw new ArgumentNullException(nameof(dto));
    Reservation? r = dto.Validate();
    if (r is null)
        return new BadRequestResult();
    var isAccepted =
        await Manager.Check(r).ConfigureAwait(false);
    if (!isAccepted)
        return new StatusCodeResult(
            StatusCodes.Status500InternalServerError);
    return new NoContentResult();
}
```

The hidden side effect inside `Manager.Check` violates CQS, eliminates something essential, and adds a chunk the reader does not see in the metric.

### After

```csharp
// Sequentially composed: each step is explicit in the caller.
// Nondeterminism (DateTime.Now, Guid.NewGuid) and side effects
// (Repository.Read/Create) live on the imperative shell; the pure
// WillAccept decision lives in the functional core.
[HttpPost]
public async Task<ActionResult> Post(ReservationDto dto)
{
    if (dto is null)
        throw new ArgumentNullException(nameof(dto));
    var id = dto.ParseId() ?? Guid.NewGuid();
    Reservation? r = dto.Validate(id);
    if (r is null)
        return new BadRequestResult();
    var reservations = await Repository
        .ReadReservations(r.At)
        .ConfigureAwait(false);
    if (!MaitreD.WillAccept(DateTime.Now, reservations, r))
        return NoTables500InternalServerError();
    await Repository.Create(r).ConfigureAwait(false);
    return Reservation201Created(r);
}
```

### Changes Made

1. Removed the nested `IRestaurantManager` indirection that hid the write behind a Boolean.
2. Made nondeterminism explicit (`DateTime.Now`, `Guid.NewGuid`) so the reader sees every input to the decision.
3. Pushed the side effect (`Repository.Create`) to the edge, after a pure-function decision from `MaitreD.WillAccept`.
4. The reader can now see the entire pipeline without following dependencies into other classes.

---

## Example 5: Hex Flower Before and After

### Before (Original `Post`, listing 6.9)

All seven hexagons filled: `dto NULL`, `At INVALID`, `Email NULL`, `Name NULL`, `Quantity INVALID`, `TOO LITTLE CAPACITY`, `HAPPY PATH`. No headroom for additional complexity.

### After `Validate` Extraction

Only four hexagons filled: `dto NULL`, `Validate NULL`, `TOO LITTLE CAPACITY`, `HAPPY PATH`. Three slots free — room to grow.

### Zooming Into `Validate`

Inside `Validate`, five hexagons are filled: `At INVALID`, `Email NULL`, `Quantity INVALID`, `Name NULL` (via `??`), `HAPPY PATH`. Below the seven-chunk limit.

### What This Shows

The refactor reduced cyclomatic complexity (7 → 4 at the top) without removing any logic. It simply distributed chunks across two hex flowers at two zoom levels — the signature of fractal architecture. Both levels now fit in the reader's brain.
