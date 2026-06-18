# Evolution Rules

Actionable rules for changing live software without breaking callers or stalling integration.

## Core Rules

### 1. Use Feature Flags to Split Deploy from Release

If a feature takes longer than a few hours of work, hide it behind a feature flag so you can keep merging to master. The flag's default in production is `false`; tests and local config set it to `true`.

- Wire the flag through configuration (appsettings, environment variables, config service).
- Default to off — missing config must mean "feature disabled".
- Drive the new behaviour with integration tests that flip the flag on.

**Example**:
```csharp
// In production config, EnableCalendar is absent, so this resolves to false
var calendarEnabled = new CalendarFlag(
    Configuration.GetValue<bool>("EnableCalendar"));
services.AddSingleton(calendarEnabled);
```

### 2. Remove Feature Flags After the Release Lands

A flag that outlives its purpose becomes a code smell. Delete the flag class/variable, then lean on the compiler to clean up every branch that referenced it. Deleting code is a feature.

- Schedule the cleanup as part of the release work, not "later".
- Don't keep flags around "just in case" — rollback is a separate concern (deployment-level, not code-level).

### 3. Replace Subsystems with the Strangler Pattern

Never change a widely-used method, class, or module in place if the edit will take more than a few hours. Instead:

1. Add the new method/class beside the old.
2. Migrate callers one at a time, committing after each.
3. Delete the old code once no caller remains.

- Every commit during this process must leave the system consistent and deployable.
- Aim to be within five minutes of a clean commit at all times.
- If two implementations can't legally coexist (e.g. C# return-type overloading), rename the old one temporarily (`ScheduleOcc` vs `Schedule`).

### 4. Use Semantic Versioning for Anything Others Depend On

`major.minor.patch`:

- **Major** bump for breaking changes (removed API, changed signature, altered behaviour contract).
- **Minor** bump for new features that don't break callers.
- **Patch** bump for bug fixes.

Even if you don't publish the version number, think in SemVer terms when reviewing diffs — it clarifies what clients will feel.

### 5. Give Users Advance Warning of Deprecations

If you must break a public API, deprecate first. For libraries with external consumers, 6+ months of advance warning is reasonable.

- Use the language's deprecation mechanism: `[Obsolete("...")]` in C#, `@Deprecated` in Java.
- Include a hint in the message pointing to the replacement.
- Only delete the deprecated API at the next major version.

**Example**:
```csharp
[Obsolete("Use Get method with restaurant ID.")]
[HttpGet("calendar/{year}/{month}")]
public Task<ActionResult> LegacyGet(int year, int month)
```

### 6. Update Dependencies on a Schedule

Don't wait for a CVE or a forced upgrade. Pick a rhythm — weekly, every sprint, every other month — and run updates then, regardless of whether anything "needs" updating.

- Attach the update to an existing cadence (e.g. first day of a new sprint).
- Never make it the *last* thing in a sprint — it'll be dropped for something urgent.
- Same discipline applies to language/runtime versions, TLS certificates, domain renewals, and backup-restore drills.

### 7. Be Aware of Conway's Law When Designing

If your system crosses a team boundary, expect an interface to form there, whether you plan one or not. If you want a particular architecture, organise teams to match it.

- A system that crosses three teams will have three modules whether the design document says so or not.
- Ad-hoc, entirely oral communication tends to produce spaghetti.
- Written, asynchronous collaboration (pull requests, reviews) tends to produce cleaner boundaries.

## Guidelines

- Prefer *weakening preconditions* over adding overloads when strangling a method. A range-of-dates reader can subsume a single-date reader; the reverse is not true.
- When you add a method to an interface, add it to every implementer in the same commit so the build stays green.
- Bundle multiple small breaking changes into one major release if that reduces caller pain — but not if each change forces massive rework on its own.
- Prefer avoiding breaking changes altogether. Stable libraries can live on the same major version for years.

## Exceptions

- **Monolith with no external API**: Breakage is cheap, so you can be less strict about SemVer. Still think in those terms for your own clarity.
- **Trivial change (< 1 hour, narrow blast radius)**: In-place edit is fine; Strangler is overkill.
- **Emergency CVE**: Update the vulnerable dependency immediately, out of rhythm.

## Quick Reference

| Rule | Summary |
|------|---------|
| Feature-flag long work | Hide incomplete behaviour; merge to master daily |
| Delete flags promptly | Never let flags rot in the codebase |
| Strangler for replacements | Add new, migrate, delete old |
| SemVer breaks = major | Breaking changes require a major bump |
| Deprecate before delete | Give callers advance warning |
| Update dependencies regularly | Schedule it; don't wait for pain |
| Mind Conway's Law | Team structure will show up in the code |
