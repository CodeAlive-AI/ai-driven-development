# Types as Primary Guardrails (Agent-Native)

> ⚠️ **Not from the book.** This is an editorial amendment. The book *touches* these ideas (parse-don't-validate, always-valid) but does not frame them as the primary agent guardrail, and actively recommends the opposite "moderation of static analysis" stance. See `references/agent-native/README.md`.

Upgrade for agent-written code: types, tests, and explicit specs are THE primary defense — not one heuristic among many.

## Why the Upgrade

For humans, parse-don't-validate (Ch 5, §7.2.5) is one tool among many. A careful human can write good code with loose types and zero tests. An agent, even when producing plausible code, is statistically likely to invent, misremember, or version-confuse (see `hallucination-debugging.md`). Types and tests convert those likely mistakes into compile- or test-time errors *before* they become production defects.

**The triad**:

| Layer | Catches | Cost |
|-------|---------|------|
| **Types** | Invented symbols, wrong signatures, null-handling gaps, contract drift | Low (one-time type annotation) |
| **Tests** | Wrong logic, regressions, edge cases | Medium (ongoing authoring) |
| **Explicit specs** (docstrings with examples, JSON Schema, OpenAPI, type stubs for external APIs) | Drift between caller and callee, integration shape mismatches | Low-medium |

Each layer catches a different failure class. For agent-heavy workflows, **all three** are closer to necessity than to luxury.

## Rules

1. **Strict from line 1.** Enable the strictest mode the toolchain offers (TypeScript strict + noImplicitAny + noUncheckedIndexedAccess; Python with pyright strict or mypy --strict; Rust `#![deny(warnings)]`). Do NOT adopt Seemann's "moderation of static analysis" / start-lax-tighten-later stance for agent-heavy work — every loosened rule is a hallucination-sized hole.

2. **Every public function has a typed signature.** No implicit `any`, no untyped Python parameters. The signature is the agent's contract with itself.

3. **Total data types.** Prefer explicit union types / tagged unions / `Result<T,E>` / `Option<T>` over null/undefined/exceptions. "This field might or might not exist" must be in the type, not in a comment.

4. **Schema-validate at boundaries.** Every external input (HTTP request, file, env var, API response) goes through a schema validator (Zod / Pydantic / JSON Schema / Rust serde) before reaching domain code. Hallucinated shapes die at the boundary.

5. **Specs live in code, not prose.** Docstrings can be skipped; types cannot. If a contract matters, express it as a type or a test, not as a paragraph.

6. **Examples are tests, not comments.** A docstring example that doesn't run will drift. Doctests, property tests, or runnable snippets survive.

7. **Fail closed.** When a type is uncertain, prefer the narrower, more restrictive option. `string | null` > `string`; `User | "anonymous"` > `User`.

## Agent-Friendliness Ranking

Environments ranked by how much they protect an agent from its own statistical errors:

| Rank | Stack | Why |
|------|-------|-----|
| 1 | **Rust** | Compiler is the tightest guardrail in mainstream use; ownership + exhaustive matching |
| 2 | **TypeScript with `strict: true`** | Near-universal, flexible, with excellent agent-tooling support |
| 3 | **Python + Pydantic + mypy/pyright strict** | Types at runtime boundary + static check |
| 4 | **Go** | Simple type system, good tooling, no null-safety (weaker than 1-3 for this) |
| 5 | **Kotlin** with explicit nullability | Null-safety helps; JVM ecosystem adds complexity |
| 6 | **Java** (modern, with `jspecify` nullness) | Verbose; nullness awkward |
| 7 | **Python without types, JavaScript without TypeScript** | Hallucination-prone environments |
| 8 | **Ruby, old-style dynamic JS** | Agent-hostile — most mistakes surface only at runtime |

Ranking isn't moral — a skilled team in Ruby is more productive than an unskilled team in Rust. But the ranking reflects *how much rope an agent gets before it hangs itself*.

## When You Can't Have All Three

Pragmatic fallback order if the stack limits you:

1. **No types available?** Add tests. Unit tests + integration tests cover a lot of what types would catch.
2. **No tests feasible?** Add explicit specs — docstrings with runnable examples, JSON Schema for data shapes, OpenAPI for HTTP surfaces.
3. **No specs possible?** Constrain by examples — write one known-good example near the code and let the agent extrapolate from it.
4. **Only examples?** Accept higher error rate; invest in tight review loops (cf. `reviewability.md`).

## Antipatterns

| Pattern | Why it's bad |
|---------|--------------|
| `any` / `// @ts-ignore` to unblock a failing typecheck | Opens a hallucination-sized hole |
| "I'll add types later" | Types retrofit poorly; the agent has already written untyped call sites that resist change |
| Types without schema validation at HTTP boundary | Runtime shape mismatches pass through |
| Pydantic models with `extra = "allow"` | Accepts hallucinated fields; defeats the point |
| Asserting in tests instead of validating at boundary | Tests are optional runs; boundary validation is mandatory |

## Relation to the Book

This extends and sharpens Ch 5 (Encapsulation), §7.2.5 (Parse, Don't Validate), and §5.2.4 (Postel's Law). Seemann's always-valid principle + parse-don't-validate + Postel's Law were the book's core type-driven ideas. For agent-written code they move from "good practice" to "first-line defense."

Seemann's moderation-of-static-analysis advice (Ch 4.2.3) was calibrated for humans who find strict mode annoying. Reverse it for agent work — strict is cheaper for the agent than for a human, and it catches more.
