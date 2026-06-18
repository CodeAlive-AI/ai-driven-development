# Hallucination Debugging (Agent-Native)

> ⚠️ **Not from the book.** This is an editorial amendment added to cover an agent-specific concern Seemann does not address. See `references/agent-native/README.md`.

A defect class Seemann's Ch 12 doesn't cover: confident-wrong output from an LLM agent.

## What Makes It Different

Seemann distinguishes non-deterministic defects (clock, random, threading, external state). Those are *stochastic* — same input may produce different output. Agent hallucinations are *statistical* — the agent produces output that is plausible given a training prior but wrong for this codebase or version.

| Class | Example | Root cause |
|-------|---------|-----------|
| Non-deterministic (book) | `DateTime.Now` in a test | Dependency on an external oracle |
| Hallucination (agent) | Calling `array.contains()` in Python | Wrong prior — language/library mixup |

They need different debugging techniques.

## Common Hallucination Classes

| Class | Symptom | Example |
|-------|---------|---------|
| **Invented API method** | `AttributeError` / "property does not exist" | `requests.fetch()` (it's `requests.get`) |
| **Outdated syntax** | Compile error on "correct-looking" code | Python 2 `print x` in Python 3 |
| **Misremembered import** | `ModuleNotFoundError` | `import numpy.array` (real: `from numpy import array`) |
| **Wrong argument order** | Runtime value error or wrong result | `str.replace(new, old)` instead of `(old, new)` |
| **Version-mismatched feature** | "Unknown option" / "unsupported" | React `use()` hook on React 17 |
| **Close-but-not** library name | Install fails or wrong package | `pip install lxml-html` (real: `lxml`) |
| **Phantom config key** | Silently ignored, no effect | `tsconfig` option that looks real but isn't |
| **Type lie** | Tests pass; prod breaks | Returning `User` but typed as `User | null` — caller doesn't null-check |

## Detection — Where Each Class Surfaces

| Tier | Catches |
|------|---------|
| Syntax parser | Outdated syntax |
| Typechecker | Invented methods, wrong argument types, phantom config keys (with strict schemas) |
| Import resolution | Misremembered imports, wrong package names |
| Runtime | Wrong argument order (if types allow), version mismatches |
| Integration test | Close-but-not API shapes |
| Production | Type lies (where runtime doesn't validate) |

**Rule**: the higher the tier where the hallucination surfaces, the more expensive the fix. Catch them as early as possible.

## Debugging Workflow

When a suspect failure occurs:

1. **Isolate the suspicious symbol.** Which exact method/import/option triggered the failure?
2. **Grep the codebase.** Does this symbol exist here, or did the agent invent it? `rg 'SymbolName'` in the repo and dependencies.
3. **Check the actual installed version.** `cat package.json`, `pip show X`, `cargo tree`. Not what the agent *thinks* the version is.
4. **Verify against docs for THAT version.** Generic Stack Overflow answers often don't apply. Pin the version, then check the version's docs.
5. **Replace with a verified-real equivalent.** Read actual library source / types if needed.
6. **Add a regression guard.** Typically a typecheck tightening, a schema validation, or a test that fails against the hallucinated symbol.

## Prevention Rules

1. **Grep-before-use.** Before using a symbol from the codebase, confirm it exists (`rg`, LSP, `cat`). Do not write from memory.
2. **Read-before-edit.** Before editing a function, read its current source. Don't edit from recall.
3. **Typecheck-before-commit.** Run strict typechecker on the touched files. Most hallucinations surface here if types are strict.
4. **Docs-for-this-version, not docs-in-general.** Pin library version, then look at its docs / types.
5. **When uncertain, run it.** Don't reason about what the code will do — execute it.
6. **Schema-validate all external responses.** Hallucinated JSON shapes pass through without schema checks.
7. **Install before import.** If an import is suspicious, check `package.json` / `requirements.txt` — the package may not even be installed.

## Antipatterns

| Pattern | Why it's bad |
|---------|--------------|
| "I remember this function exists" | Memory is the hallucination source; verify |
| "The failure is weird — probably flaky, let's retry" | Likely a hallucination, not flake |
| Suppressing a typecheck error with `any` | Hides the hallucination; moves the failure to runtime |
| Adding `try/except` around unknown failure | Swallows the symptom; agent keeps hallucinating |
| Installing a typo'd package because install succeeded | Typo-squatting supply chain risk |

## Agent-Specific Tooling

- **LSP / IDE integration**: auto-complete from real symbols only
- **Strict typecheckers** as first-line defense (`tsc strict`, `pyright strict`, `mypy --strict`)
- **Lockfiles**: `package-lock.json`, `poetry.lock`, `Cargo.lock` — without them, the "version the agent recalls" drifts from "version installed"
- **Runtime schema validation** at boundaries (Zod, Pydantic, JSON Schema)
- **Typo-safe package managers**: prefer managers that resolve to well-known registries; verify downloads

## Relation to the Book

Ch 12 on reproducing defects as tests still applies — once you isolate a hallucination, capture it as a failing test (or a failing type) so it can never slip back. Ch 5 on parse-don't-validate is the structural defense: hallucinated data shapes die at the parse boundary.
