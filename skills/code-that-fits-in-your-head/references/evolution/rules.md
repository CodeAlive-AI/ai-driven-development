# Evolution Rules

Actionable rules for changing code that other code depends on, without breaking callers or stalling integration. Changing a live schema, contract or stored format, and planning a rollout or rollback, are design questions: see `pragmatic-architecture`.

## Core Rules

### 1. Give Every Temporary Path an Owner and a Removal Step

A feature flag, a bridge method, a temporary rename, an adapter or a second implementation kept "for now" is scaffolding. Each one adds a branch the next reader must hold in mind, so it leaves with the change that needed it.

- Introduce it together with its exit: who removes it, and after which event.
- Default a switch to the old behaviour: missing configuration must mean "new path off".
- Remove it by deleting the switch or the old symbol first, then let the compiler or a search find every branch that referenced it. Deleting code is a feature.
- Do not keep it "just in case". Going back to an old version is a deployment and data question, not a code branch.

Whether a change needs a flag, a staged rollout or coexisting versions at all, and what switching it off really restores, is a design decision. That is `pragmatic-architecture` (its change-path reference), not this skill.

### 2. Replace Methods and Classes with the Strangler Pattern

When replacing a widely used method, class or module, prefer the Strangler pattern when side-by-side migration reduces blast radius or makes verification and rollback safer. Do not choose it solely from estimated implementation time. A subsystem with its own stored data or outside clients needs a designed migration path first (`pragmatic-architecture`); Strangler is then how each caller moves.

1. Add the new method/class beside the old.
2. Migrate callers one at a time, committing after each.
3. Delete the old code once no caller remains.

- Every commit during this process must leave the system consistent and deployable.
- Preserve recoverable, verified migration checkpoints appropriate to the system.
- If two implementations can't legally coexist (e.g. C# return-type overloading), rename the old one temporarily (`ScheduleOcc` vs `Schedule`).

### 3. Use Semantic Versioning for Anything Others Depend On

`major.minor.patch`:

- **Major** bump for breaking changes (removed API, changed signature, altered behaviour contract).
- **Minor** bump for new features that don't break callers.
- **Patch** bump for bug fixes.

Even if you don't publish the version number, think in SemVer terms when reviewing diffs — it clarifies what clients will feel.

### 4. Give Users Advance Warning of Deprecations

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

### 5. Update Dependencies on a Schedule

Don't wait for a CVE or a forced upgrade. Pick a rhythm — weekly, every sprint, every other month — and run updates then, regardless of whether anything "needs" updating.

- Attach the update to an existing cadence (e.g. first day of a new sprint).
- Never make it the *last* thing in a sprint — it'll be dropped for something urgent.
- Same discipline applies to language/runtime versions, TLS certificates, domain renewals, and backup-restore drills.

For agent-authored dependency changes, verify package identity, provenance, locked version, compatibility, and removal of obsolete transitive workarounds. See `../agent-native/hallucination-debugging.md`.

## Guidelines

- Prefer *weakening preconditions* over adding overloads when strangling a method. A range-of-dates reader can subsume a single-date reader; the reverse is not true.
- When you add a method to an interface, add it to every implementer in the same commit so the build stays green.
- Bundle multiple small breaking changes into one major release if that reduces caller pain — but not if each change forces massive rework on its own.
- Prefer avoiding breaking changes altogether. Stable libraries can live on the same major version for years.

## Exceptions

- **Monolith with no external API**: Breakage is cheap, so you can be less strict about SemVer. Still think in those terms for your own clarity.
- **Narrow, easily verified change**: In-place editing is fine when blast radius and rollback are clear; Strangler would add needless machinery.
- **Emergency CVE**: Update the vulnerable dependency immediately, out of rhythm.

## Quick Reference

| Rule | Summary |
|------|---------|
| Temporary paths leave | A flag, bridge or second implementation has an owner and a removal step |
| Strangler for replacements | Add new, migrate, delete old |
| SemVer breaks = major | Breaking changes require a major bump |
| Deprecate before delete | Give callers advance warning |
| Update dependencies regularly | Schedule it; don't wait for pain |
