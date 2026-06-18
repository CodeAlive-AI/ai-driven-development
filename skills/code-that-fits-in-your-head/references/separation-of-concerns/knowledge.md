# Separation of Concerns Knowledge

Core concepts for keeping cross-cutting concerns out of business logic and for weighing legibility against raw performance.

## Overview

Some concerns (logging, caching, auth, fault tolerance) cut across many features. If you scatter them through the code they drown out the domain logic. The Decorator pattern lets you add these behaviours without editing the classes they wrap. A related discipline is knowing when *not* to optimise: correctness and legibility come first, and performance claims without measurement are guesses.

## Key Concepts

### Cross-Cutting Concern

**Definition**: A concern that applies to many features, not just one. Once you need it, you need it in many places.

Common examples:
- Logging
- Performance monitoring
- Auditing
- Metering
- Instrumentation
- Caching
- Fault tolerance (e.g. Circuit Breaker)
- Security

Rule of thumb: if the concern appears next to the domain logic in every feature, it is cross-cutting and belongs in a Decorator.

### Decorator Pattern

**Definition**: An object that implements an interface and also wraps another instance of the same interface, delegating each call to the inner object while adding behaviour around it.

Sometimes called "Russian dolls" because Decorators nest inside each other. Each Decorator:
- Implements the interface fully (so any method can be delegated trivially to `Inner`)
- Gets a chance to run code before and after each call
- Stays unaware of what it is wrapping or who is wrapping it

### Logging (Minimum)

**Definition**: Writing enough runtime data to a log that you can understand and reproduce what happened when something went wrong.

**Key points**:
- At minimum, unhandled exceptions must be logged (ASP.NET does this automatically).
- Treat every exception in the log as a defect; the ideal count is zero.
- Defects manifest not just as crashes but as wrong behaviour (e.g. overbooking, swapped fields), so exception logs alone are not enough.

### Structured Logging

**Definition**: Logging with named parameters (e.g. `{method}`, `{id}`, `{output}`) rather than by interpolating into a single string.

Structured entries can be queried, filtered, and indexed by field. Unstructured entries can only be grep'd. Example from the book:

```csharp
Logger.LogInformation(
    "{method}(id: {id}) => {output}",
    nameof(ReadReservation),
    id,
    JsonSerializer.Serialize(output?.ToDto()));
```

### Repeatability ("Goldilogs")

**Definition**: Logging just enough to be able to reproduce any execution — not too little, not too much.

You cannot predict future defects, so rather than over-logging, log what you cannot recompute. If every impure action is captured, you can replay execution and understand any problem.

### Legibility vs Performance

**Definition**: Most modern performance worry is legacy. Modern CPUs are fast enough that the 10-vs-100-nanosecond difference is noise next to a database call. Correctness and readability dominate; performance is secondary and must be measured, not guessed.

**Key points**:
- You cannot reason about performance. Compilers inline, reorder, and optimise in ways that do not match your mental model.
- Performance depends on hardware, installed software, concurrent processes, and more.
- A fast wrong program is worthless: "If the program doesn't have to work, I can write one that takes one millisecond per card."

## Terminology

| Term | Definition |
|------|------------|
| Cross-cutting concern | Behaviour needed across many features (logging, caching, etc.) |
| Decorator | Object wrapping another object behind the same interface |
| Inner | The wrapped instance inside a Decorator |
| Structured log | Log entry with named, machine-queryable fields |
| Goldilogs | Just-right logging; enough to reproduce execution, no more |
| Read-through cache | Cache Decorator that falls back to the real source on miss |
| Functional core, imperative shell | Architecture that isolates impure actions at the edges |

## How It Relates To

- **Decomposition**: Decorators are a decomposition technique; each Decorator is one concern.
- **Encapsulation**: By not editing the core class, the Decorator preserves its invariants.
- **Functional core / imperative shell**: Pure functions do not need logging; impure actions do. The cleaner the split, the less logging you need.
- **Troubleshooting**: Logs are the primary tool for post-mortems; Decorators make them cheap to add.

## Common Misconceptions

- **Myth**: Cross-cutting concerns need AOP frameworks or inheritance hierarchies.
  **Reality**: A plain Decorator class plus DI registration covers almost all cases with no framework magic.

- **Myth**: More logging is always safer.
  **Reality**: Over-logging obscures the signal. Log impure actions; skip pure ones.

- **Myth**: You should optimise as you write code ("performance-first").
  **Reality**: Make it work, then measure. Optimise only proven bottlenecks.

- **Myth**: Shaving microseconds off a method matters.
  **Reality**: Not if you then hit a database. Optimise the slow link, not the fast one.

## Quick Reference

| Concept | One-Line Summary |
|---------|-----------------|
| Cross-cutting concern | Same behaviour needed in many features |
| Decorator | Wrap an interface, delegate, add behaviour |
| Structured logging | Named fields, not string interpolation |
| What to log | Impure actions; skip pure functions |
| Performance | Correctness first, measure second, optimise last |
