# Measurement Commands

Executable ways to measure the complexity signals this skill's rules reference. Rules say *what* to check; this file says *how*. Prefer tools already present in the repository; install new ones only when the project owner agrees or the tool is disposable (run once, not committed).

**After choosing commands for a repository, record them in the project's agent instructions (`CLAUDE.md` / `AGENTS.md`) so every future session uses the same canonical commands and thresholds.** See `workflows/operationalize-finding.md`.

## Cyclomatic Complexity (rule: review above 15)

| Ecosystem | Command |
|---|---|
| Any language | `lizard -C 15 <path>` (supports C#, TS/JS, Python, Go, Java, C/C++, Rust, and more) |
| Python | `radon cc -n D <path>` or `ruff check --select C901` |
| JS/TS | ESLint rule `complexity: ["warn", 15]` |
| .NET | Roslyn analyzer `CA1502` (enable in `.editorconfig`), or `lizard` |
| Go | `gocyclo -over 15 .` |

## Dependency Cycles and Layer Violations (smell D8)

| Ecosystem | Command / tool |
|---|---|
| JS/TS | `madge --circular src/` ; `dependency-cruiser` with a rules file for layers |
| Python | `pydeps --show-cycles <pkg>` ; `import-linter` with layer contracts |
| .NET | `NetArchTest` assertions in a test project; project references already forbid cycles between projects |
| JVM | `ArchUnit` tests |
| Go | package cycles are a compile error; layer rules via `depguard` |

Splitting code into packages/projects turns cycle prevention into a compile error — the cheapest architecture test available.

## Duplication

| Scope | Command |
|---|---|
| Any language | `jscpd --min-tokens 50 <path>` |
| Before writing a new helper | `rg -i '<domain term>'` across the repo — search for an existing implementation first |

## Dead and Orphaned Code (smell D9)

| Ecosystem | Command |
|---|---|
| TS | `knip` (unused files, exports, dependencies) or `ts-prune` |
| Python | `vulture <pkg>` ; unused dependencies: `deptry .` |
| .NET | Roslyn `IDE0051`/`IDE0052` as errors; unused public API via `dotnet format analyzers` |
| Rust | compiler `dead_code` lint; unused deps: `cargo-udeps` |
| Any | for a symbol: `rg 'SymbolName'` — one hit (the definition) means it is dead |

## Hotspots and Change Coupling (behavioural analysis)

No product required — Git is the database:

```bash
# Churn: most frequently changed files in the last year
git log --since="1 year ago" --name-only --pretty=format: \
  | sort | uniq -c | sort -rn | head -30
```

```bash
# Hotspot candidates: cross churn with size (large AND frequently changed)
git log --since="1 year ago" --name-only --pretty=format: | sort | uniq -c | sort -rn \
  | awk '$1 > 10 {print $2}' | xargs wc -l 2>/dev/null | sort -rn | head -20
```

```bash
# Files that change together with a given file (change coupling)
git log --follow --name-only --pretty=format:__ -- <file> \
  | awk 'BEGIN{RS="__"} NF>1' | tr ' ' '\n' | grep -v '^$' \
  | sort | uniq -c | sort -rn | head -15
```

Hotspot = high complexity × high change frequency → prime refactoring target. Watch trends, not absolute numbers.

## Test-Oracle Strength (automated Devil's Advocate)

Mutation testing automates "would my tests notice deliberately wrong code":

| Ecosystem | Tool |
|---|---|
| JS/TS | Stryker (`npx stryker run`) |
| .NET | Stryker.NET (`dotnet stryker`) |
| Python | `mutmut run` or `cosmic-ray` |
| JVM | PIT |
| Rust | `cargo-mutants` |

Run on the touched module, not the whole repo — full-repo mutation runs are slow. Surviving mutants = missing test cases.

## Architecture Tests (make stable constraints executable)

When a boundary rule is stable and mechanically expressible, encode it once:

- **.NET**: `NetArchTest` — e.g. "Domain must not reference DataAccess".
- **JVM**: `ArchUnit` — layer and cycle assertions.
- **JS/TS**: `dependency-cruiser` rules file or `eslint-plugin-boundaries`.
- **Python**: `import-linter` contracts (`layers`, `forbidden`, `independence`).

An architecture test converts a review nag into a build failure. See `workflows/operationalize-finding.md` for when to add one.
