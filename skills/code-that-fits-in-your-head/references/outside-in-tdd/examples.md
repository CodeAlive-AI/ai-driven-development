# Outside-In TDD Examples

Curated C# examples demonstrating outside-in TDD practices from the book. Each shows a concrete step along the vertical slice: starting a skeleton, driving behaviour from the boundary inward, using parametrised tests, and defeating the Devil's Advocate.

## Example 1: Walking Skeleton + Characterisation Test

This is the first test in the codebase. It targets the outermost boundary (HTTP) and asserts only the weakest stable property — a 2xx status. It was written after the project scaffolder ran, so it's a characterisation test, not red-green TDD.

```csharp
[Fact]
[SuppressMessage(
    "Usage", "CA2234:Pass system uri objects instead of strings",
    Justification = "URL isn't passed as variable, but as literal.")]
public async Task HomeIsOk()
{
    using var factory = new WebApplicationFactory<Startup>();
    var client = factory.CreateClient();

    var response = await client.GetAsync("");

    Assert.True(
        response.IsSuccessStatusCode,
        $"Actual status code: {response.StatusCode}.");
}
```

**Why it works**:
- One assertion, loosest possible — future changes to the body or status code won't break it unless the endpoint goes down entirely.
- AAA structure: factory + client (arrange), `GetAsync` (act), `Assert.True` (assert), separated by blank lines.
- Assertion message tells future readers what failed, not just "expected True but got False".
- `[SuppressMessage]` has a `Justification` explaining *why* the rule is suppressed here.

## Example 2: Boundary Test Driving a New Feature

The first test that drives behaviour, not just characterises. It posts a valid reservation as JSON and asserts success. Details of `PostReservation` are hidden in a helper method to amplify what matters: post a reservation, get a success.

```csharp
[Fact]
public async Task PostValidReservation()
{
    var response = await PostReservation(new {
        date = "2023-03-10 19:00",
        email = "katinka@example.com",
        name = "Katinka Ingabogovinanana",
        quantity = 2 });

    Assert.True(
        response.IsSuccessStatusCode,
        $"Actual status code: {response.StatusCode}.");
}
```

The hidden helper (a SUT Encapsulation Method / Test Utility Method):

```csharp
[SuppressMessage(
    "Usage", "CA2234:Pass system uri objects instead of strings",
    Justification = "URL isn't passed as variable, but as literal.")]
private async Task<HttpResponseMessage> PostReservation(object reservation)
{
    using var factory = new RestaurantApiFactory();
    var client = factory.CreateClient();

    string json = JsonSerializer.Serialize(reservation);
    using var content = new StringContent(json);
    content.Headers.ContentType.MediaType = "application/json";
    return await client.PostAsync("reservations", content);
}
```

**Why it works**:
- The test body reads like a specification of behaviour, not an HTTP tutorial.
- The helper encapsulates URL conventions; the API can later move to hypermedia without breaking tests.
- Only asserts `IsSuccessStatusCode` — happy path, light touch.

## Example 3: Unit Test with AAA and a Fake Object

Once the boundary test passes minimally, drive behaviour deeper with a unit test against `ReservationsController` directly. This is the inward step of outside-in.

```csharp
[Fact]
public async Task PostValidReservationWhenDatabaseIsEmpty()
{
    var db = new FakeDatabase();
    var sut = new ReservationsController(db);

    var dto = new ReservationDto
    {
        At = "2023-11-24 19:00",
        Email = "juliad@example.net",
        Name = "Julia Domna",
        Quantity = 5
    };
    await sut.Post(dto);

    var expected = new Reservation(
        new DateTime(2023, 11, 24, 19, 0, 0),
        dto.Email,
        dto.Name,
        dto.Quantity);
    Assert.Contains(expected, db);
}
```

**Why it works**:
- 2-2-2 balance across arrange / act / assert.
- `FakeDatabase` is a test-only `IReservationsRepository` that inherits from `Collection<Reservation>`, so `Assert.Contains` works for free.
- The `Reservation` domain type has structural equality, so `expected` equals the stored instance by value.
- DTO (`ReservationDto`) receives the wire format with nullable strings; `Reservation` (domain type) enforces invariants.

## Example 4: Parametrised Test with Devil's Advocate Counter-Case

The Devil implemented `Post` with a hard-coded branch on `if (dto.Email == "shli@example.org") return 500`. Adding one `[InlineData]` row that posts from that email into an *empty* database rejects the stupid implementation.

```csharp
[Theory]
[InlineData(
    "2023-11-24 19:00", "juliad@example.net", "Julia Domna", 5)]
[InlineData("2024-02-13 18:15", "x@example.com", "Xenia Ng", 9)]
[InlineData("2023-08-23 16:55", "kite@example.edu", null, 2)]
[InlineData("2022-03-18 17:30", "shli@example.org", "Shanghai Li", 5)]
public async Task PostValidReservationWhenDatabaseIsEmpty(
    string at, string email, string name, int quantity)
{
    var db = new FakeDatabase();
    var sut = new ReservationsController(db);

    var dto = new ReservationDto { At = at, Email = email, Name = name, Quantity = quantity };
    await sut.Post(dto);

    var expected = new Reservation(
        DateTime.Parse(dto.At, CultureInfo.InvariantCulture),
        dto.Email, dto.Name ?? "", dto.Quantity);
    Assert.Contains(expected, db);
}
```

**Why it works**:
- Adding the fourth `[InlineData]` line is the safest kind of test-code edit (pure append).
- It forces the production code off a constant branch and toward considering the wider state (existing reservations).
- Same test method, same assertions, just more data — no risk of weakening postconditions elsewhere.

## Example 5: Strengthening Postconditions by Adding Assertions

A test initially asserts only the status code. Later, to prevent false negatives (any unrelated 500 would pass), append more assertions.

Before:

```csharp
Assert.Equal(
    HttpStatusCode.InternalServerError,
    response.StatusCode);
```

After:

```csharp
Assert.Equal(
    HttpStatusCode.InternalServerError,
    response.StatusCode);
Assert.NotNull(response.Content);
var content = await response.Content.ReadAsStringAsync();
Assert.Contains(
    "tables",
    content,
    StringComparison.OrdinalIgnoreCase);
```

**Why it works**:
- Purely additive — no existing assertion touched, no assertion deleted.
- Strengthens postconditions: random 500s (e.g. a missing connection string) no longer pass.
- Analogous to Liskov's "subtypes may strengthen postconditions" — moving forward in time is like moving to a subtype.

## Example 6: Test Spy Refactored in Isolation

Adding `EmailReservationDeleted` to `IPostOffice` forces the spy to distinguish which method was called. Refactor the spy alone — stash production changes, change the spy, make sure tests compile and pass, then `git stash pop` and continue.

Before (captures only reservations, not which method was called):

```csharp
public class SpyPostOffice : Collection<Reservation>, IPostOffice
{
    public Task EmailReservationCreated(Reservation reservation)
    {
        Add(reservation);
        return Task.CompletedTask;
    }
}
```

After (captures both method kind and reservation):

```csharp
internal class SpyPostOffice :
    Collection<SpyPostOffice.Observation>, IPostOffice
{
    public Task EmailReservationCreated(Reservation reservation)
    {
        Add(new Observation(Event.Created, reservation));
        return Task.CompletedTask;
    }

    public Task EmailReservationDeleted(Reservation reservation)
    {
        Add(new Observation(Event.Deleted, reservation));
        return Task.CompletedTask;
    }

    internal enum Event { Created = 0, Deleted = 1 }
}
```

**Why it works**:
- The refactor touches only test code — production code stayed stashed.
- The spy's assertions had to be rewritten (collection element type changed) but in a separate, reviewable commit.
- Eliminates the category of errors where a test-code refactor inadvertently strengthens preconditions and papers over bugs.

## Changes Made (across the vertical slice)

1. Scaffolder produced a working "Hello World" endpoint.
2. Added a characterisation test and CI build script.
3. Added a boundary test posting JSON — failed, then added an MVC controller to pass it.
4. Dropped inward to a unit test of the controller — triggered creation of DTO, domain model, repository interface, and Fake Object.
5. Added a real SQL implementation as a Humble Object (untested at unit level).
6. Added further parametrised test cases to defeat Devil's Advocate implementations, then refactored to a clean `Sum` once red-green-refactor opened up.
