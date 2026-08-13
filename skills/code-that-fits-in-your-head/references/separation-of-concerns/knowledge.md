# Separation of Concerns Knowledge

Core concepts for keeping cross-cutting concerns out of business logic.

## Overview

Some concerns (logging, caching, auth, fault tolerance) cut across many features. Scattered through domain code they drown out the logic. The Decorator pattern adds those behaviours without editing the classes they wrap.

## Key Concepts

### Cross-Cutting Concern

A concern that applies to many features, not just one. Once you need it, you need it in many places.

Common examples:

- Logging
- Performance monitoring / instrumentation
- Auditing and metering
- Caching
- Fault tolerance (e.g. Circuit Breaker)
- Security

Rule of thumb: if the concern appears next to domain logic in every feature, it is cross-cutting and belongs in a Decorator (or equivalent explicit seam).

### Decorator Pattern

An object that implements an interface and wraps another instance of the same interface, delegating each call while adding behaviour around it. Decorators nest ("Russian dolls"): each fully implements the interface, runs code before/after, and stays unaware of what it wraps. Full treatment lives in `patterns.md`.

### Structured Logging

Log with named parameters (e.g. `{method}`, `{id}`, `{output}`) rather than interpolating into a single string. Structured entries can be queried and filtered by field; unstructured entries can only be grepped. At minimum, unhandled exceptions must be logged; treat every exception in the log as a defect.

### Repeatability ("Goldilogs")

Log just enough to reproduce any execution — not too little, not too much. Log what you cannot recompute: if every impure action is captured, you can replay execution. Pure functions need little or no logging.

## Common Misconceptions

- **Myth**: Cross-cutting concerns need AOP frameworks or inheritance hierarchies.
  **Reality**: A plain Decorator class plus DI registration covers almost all cases with no framework magic.

- **Myth**: More logging is always safer.
  **Reality**: Over-logging obscures the signal. Log impure actions; skip pure ones.

- **Myth**: You should optimise as you write code ("performance-first").
  **Reality**: Make it work, then measure. Optimise only proven bottlenecks (see `rules.md` rules 6–7).
