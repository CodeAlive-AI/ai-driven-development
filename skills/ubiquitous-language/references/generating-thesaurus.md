# Generating and Maintaining the Thesaurus

Read this when the user asks to create, generate, update, or audit the project thesaurus.
For naming consultation (the frequent case), the main SKILL.md has everything you need.

## Creating a New Thesaurus

**Derive the thesaurus from the codebase** — not from docs or specs.

### Step 0: Determine the thesaurus path

1. If the user specified a path — use it
2. Search the repo for an existing `THESAURUS.md`: `find . -name "THESAURUS.md" -not -path "*/node_modules/*"`
3. If found — use the existing location
4. Default: `docs/THESAURUS.md` (create `docs/` if it doesn't exist)

Use this resolved path throughout all subsequent steps.

### Step 1: Scan high-signal hubs (do NOT read the whole codebase)

An agent cannot scan an entire repository without exhausting context. Instead, target
**structural files that are dense with domain nouns** — 5-10 tool calls covers 80-90%:

1. **DB schemas and migrations** — ORM model definitions, schema files, migration scripts
2. **API contracts** — OpenAPI/Swagger specs, GraphQL schemas, route/controller definitions
3. **Domain layer** — aggregate/entity/value-object type declarations
4. **Directory structure** — `ls` top-level dirs to map product areas (cheap, zero-read)
5. **Symbol extraction** — grep for type/class/interface/struct declarations across source

**Stop conditions:**
- If the repo has multiple product areas, ask the user which to catalog first
- Stop when new scans mostly return terms already seen (diminishing returns)
- Default to one bounded area at a time, not the entire monorepo

**Do NOT rely on docs** — they're often outdated. If a README says "User" but the code
says "Customer" everywhere, the canonical term is "Customer".

**Scope the thesaurus to the problem.** Don't catalog every noun in the codebase —
catalog only terms that matter for the system's purpose. Include a term if: domain
experts use it, it appears in invariants/commands/events, ambiguity about it has caused
bugs, or multiple synonyms exist. Exclude purely technical infrastructure terms
(LogLevel, RetryPolicy, ConnectionPool). **Target: 15-40 terms per bounded context.**
Past 60 you're likely including infrastructure; fewer than 10 you're missing concepts.

### Step 2: Separate active from legacy/obsolete

Codebases accumulate dead weight. When scanning, classify each term:

- **Active**: Used in current code paths, referenced by live features
- **Legacy**: Still in codebase but deprecated, behind feature flags, or in migration layers. Mark with `[LEGACY]` prefix and note what replaces it
- **Obsolete**: Dead code, unused classes, abandoned tables. Don't add to thesaurus — just note for cleanup

**How to detect legacy/obsolete:**
- Classes/tables with `Legacy`, `Old`, `Deprecated`, `V1`, `V2` prefixes/suffixes
- Code behind `if (featureFlag)` guards or `#if LEGACY` preprocessor directives
- Methods marked `@Deprecated`, `[Obsolete]`, or with deprecation comments
- Database tables with zero recent writes (check with user)
- Modules that nothing imports anymore (check import graph)
- Names that only appear in test fixtures or migration scripts

**Ask the user** when classification is ambiguous: "I found `UserProfile` and `CustomerProfile` — which is the active concept? Is the other legacy?"

### Step 3: Cluster, identify conflicts, collect ambiguities

- Group synonyms and variants (same concept, different names)
- Identify polysemy (same name, different concepts in different places)
- Flag naming inconsistencies between active code and its tests/docs

**Don't stop on each ambiguity** — collect them all into the `## Unresolved` section
of the thesaurus. This lets you scan the entire codebase in one pass and gives the
user a complete picture to prioritize, rather than answering questions one by one.

For each ambiguity, record: what term, where it's found, what the question is,
how many files are affected, and possible resolutions if obvious.

### Step 4: Write the thesaurus

Write `THESAURUS.md` in the grep-first layout (Bootstrap Template below):
- YAML frontmatter first: `thesaurus-format: "2.0"`, `skill: ubiquitous-language`
- Keep the template's "Reconstructed, not authored" line in the header — this document
  was mined from code, not written by domain experts; names are evidence, definitions are
  reconstruction, and readers must know the difference
- Active terms → one `## Index` line each **and** one `### Term` entry under `## Terms`
- Synonyms, abbreviations, competing names → the `avoid:` list of their concept's line
- Weasel words and jargon you actually saw in the code → `## Forbidden` lines
- Deprecated names → `## Legacy` lines (one line each; no prose entries)
- All ambiguities → `## Unresolved` entries

**Write the Index first**, then the entries in the same alphabetical order. The Index is
what agents read on every naming task; the entries are what they grep into. Before
finishing, confirm the registry invariant: every name appears in exactly one registry
line — Index line, Forbidden line, Legacy line, or Unresolved header. A name that is both
under `avoid:` and in Legacy, or has an entry but no Index line, is a defect.

**Start with a flat thesaurus** — no `ctx:` tokens, no context sections. Most
projects don't need context separation. Only introduce bounded contexts later if Step 6
or Step 8 reveals genuine polysemy.

### Step 5: Surface unresolved issues

**This step is mandatory** — always runs right after writing the file.

After creating `THESAURUS.md`, explicitly present the `## Unresolved` section to the
user. Frame it as: "The thesaurus is ready, but there are N naming conflicts that
need your input — without resolving them, the thesaurus quality will suffer."

List each issue with its impact. Example output:

```
THESAURUS.md created with 24 terms, 3 legacy terms, and 5 unresolved issues:

1. `Account` — used as financial entity (billing/) AND user identity (auth/) — 18 files affected
2. `User` vs `Customer` — synonym drift between API and domain layers — 31 files
3. `Process` — means workflow in scheduler/, means OS process in runtime/ — 7 files
4. `Status` — enum with 12 values, some overlap with `State` enum — 15 files
5. `Service` — bare word used 40+ times, needs polysemy unpacking

Which would you like to resolve first?
```

As the user resolves each item, promote it from `## Unresolved` to an Index line + entry
(or a `## Legacy` line). Items the user defers stay as documented naming debt.

**Then offer Step 6** — before the user starts answering item by item, offer to mine the
git history first. Offer it once, as an option, never as a blocking question.

### Step 6 (optional): Resolve ambiguities from git history

**Offer this whenever `## Unresolved` is non-empty and the repo has real history.**
It is the one step that can answer unresolved items *without* the user answering them:
git history records which name came first, which one replaced which, and which is dying.

Ask, don't assume:

```
5 unresolved naming issues remain. Before you answer them one by one, I can mine the
git history — when each name was born, which replaced which, which is growing vs dying.
It builds a temporary index outside the repo (~1-3 min here, deleted afterwards) and
comes back with evidence-backed proposals per item. Want me to try that first?
```

Skip the offer when the repo has < ~50 commits, has no `.git`, starts from a squashed
import, or when the unresolved items are `[WHITE-SPOT]` tags (a concept nobody has named
yet leaves no trace in history).

If the user accepts, read [git-history-mining.md](git-history-mining.md) and follow its
protocol. In short:

1. `python3 scripts/git_term_index.py build --repo-dir . --content` — a throwaway index of
   commit messages, paths, renames, and diff-level identifiers, written to `$TMPDIR`,
   never into the working tree.
2. `query` each candidate name and `pair` the competing ones; confirm the few decisive
   commits with `git show` / `git log -S`.
3. Report one batch of **proposals with citations and confidence** — never silent edits.
4. Apply only what the user approves; cite the commit in the Legacy note or an entry
   `- **History**:` line; leave the rest in `## Unresolved` with what was ruled out.
5. `python3 scripts/git_term_index.py clean` and say the index is gone.

History is evidence of what happened, not authority on what the term *should* be. It
ranks candidates; the user decides.

### Step 7: Update project instructions

**This step is mandatory** — the thesaurus is only useful if the agent knows about it.

After creating the thesaurus, add a reference to it in **all** agent instruction files
found in the project. Check for and update whichever exist:

- `CLAUDE.md` (Claude Code)
- `GEMINI.md` (Gemini CLI)
- `AGENTS.md` (multi-agent)
- `.cursorrules` (Cursor)
- `.github/copilot-instructions.md` (GitHub Copilot)

Propose adding a section like (use the resolved path from Step 0):

```markdown
## Domain Language

This project maintains a domain thesaurus at `docs/THESAURUS.md`. It is grep-first:
one `## Index` line per concept — ``- **Term** `Identifier` kind:… avoid: `synonyms` ``.

- **Before naming anything** (class, method, variable, DB table, API endpoint, file),
  search `rg -n -i '<word>' docs/THESAURUS.md` for each name you are considering.
  - Hit in an Index line → use that line's `Identifier`, even if your word was under `avoid:`.
  - Hit in a `` - `word` use: `` (Forbidden) or `` - `word` → `` (Legacy) line → do not use it;
    the line names the replacement.
  - Hit in `## Unresolved` → open question; ask before deciding.
  - No hit → new concept: add an Index line and a `### Term` entry **before** using it in code.
- Useful: `rg 'kind:event'` · ``rg 'avoid:.*`Word`'`` · `rg -F '**Term**'` · `rg '^### Term( \(|$)'`.
- Never introduce a synonym for an existing Index term.
```

This ensures every agent session — even without the ubiquitous-language skill installed —
knows the thesaurus exists and should consult it.

### Step 8 (optional): Detect polysemy

**Do NOT pre-assign bounded contexts.** The agent cannot reliably determine context
boundaries — this is an architectural decision that requires deep domain knowledge.

Instead, look for **evidence of polysemy** — the same word meaning different things:
- Same class name in different modules/packages with different fields/methods
- Same DB column name with different semantics in different tables
- Same API term used inconsistently across endpoints
- User/team disagreement about what a term means

**When you find evidence**, don't decide — report it to the user:
"I found `Account` used in two different ways: as a financial entity in `billing/`
and as a user identity in `auth/`. Should these be separate bounded contexts, or is
one of them a legacy naming mistake?"

Only add `ctx:` tokens and context sections to the thesaurus after the user
confirms the separation. A wrong context boundary is worse than no boundary.

**The invariant test** (from FPF A.1.1): A bounded context is justified only when you
can name **at least one rule (invariant)** that is true inside the context but not
outside. Example: "An Order in Sales context can be cancelled; an Order in Fulfillment
context cannot be cancelled once shipped." If you can't name such a rule — it's just
a module, not a bounded context.

### Bootstrap Template

```markdown
---
thesaurus-format: "2.0"
skill: ubiquitous-language
---

# Project Thesaurus

> Domain glossary following DDD ubiquitous language. Every name in code, APIs, docs,
> and conversations comes from here. Add the term here BEFORE using it in code.
>
> **Reconstructed, not authored.** An AI agent mined this vocabulary from the codebase —
> the names are evidence found in code and are binding; the definitions are a
> reconstruction of what the code seems to mean and may be wrong until a domain expert
> confirms them. Maintained by the `ubiquitous-language` skill
> (https://github.com/CodeAlive-AI/ai-driven-development/tree/main/skills/ubiquitous-language).
>
> **How to use (grep-first):** `rg -n -i '<word>' THESAURUS.md` — the shape of the hit
> line tells you what to do:
> - ``- **Term** `Identifier` kind:… avoid: … `` (Index) → use the Identifier, even if
>   your word was under `avoid:`
> - ``- `Word` use: `X` `` (Forbidden) → banned; use `X`
> - ``- `Old` → `New` in: … `` (Legacy) → use `New` in new code
> - `### Term — …` under Unresolved → open question; ask before deciding
> - no hit → new concept: add an Index line + `### Term` entry first
> Handy: `rg 'kind:event'` · `rg 'ctx:Billing'` · `rg -F '**Term**'` · `rg '^### Term( \(|$)'`
>
> **Rules:** one canonical Identifier per concept; every name lives in exactly one
> registry line; `avoid:`/Forbidden/Legacy names never appear in new code; on rename,
> update code, docs, API, DB — and add a Legacy line.

## Index

- **[Term]** `[PascalCase]` kind:[aggregate|entity|value|event|command|query|service|role|process|state|policy|concept] avoid: `[synonym]`, `[abbrev]`

## Terms

### [Term]
- **Definition**: [What this means in the business domain — one sentence]
- **NOT**: [What this does NOT mean — the neighbouring term it is confused with]
- **Related**: [Other Index Terms, written exactly as in the Term field]

## Forbidden

> Words that MUST NOT appear in domain-layer names: implementation details, weasel
> words, bundle-collapse terms. `use:` always points at an Index Identifier.

- `Manager` use: [specific activity] — vague, hides responsibility
- `Handler` use: [what it handles] — generic
- `Service` use: [specific facet] — overloaded, see Polysemy Unpacking
- `Info`, `Data` use: [the term itself] — meaningless suffix

## Legacy

> Names still present in the codebase but deprecated. New code MUST use the name after
> `→`. `A + B` = the old name was split; `→ —` = retired with no single successor.

- `[OldName]` → `[Identifier]` in: [modules/files] — [what it meant; since when]

## Unresolved

> Naming ambiguities, contradictions, and open questions. Each needs a human decision
> before the name can enter the Index. Resolve top-down by impact.

### [Term] — [short description of the problem]
- **Found in**: [where this name appears with different meanings/usage]
- **Question**: [what needs to be decided]
- **Impact**: [how many files/modules are affected]
- **Options**: [possible resolutions, if known]

<!-- ONLY when confirmed polysemy requires bounded contexts:
  1. Add `ctx:<Context>` to every Index line that belongs to a context (after kind:)
  2. Headers become `### Term (Context)`; group entries under `## Terms: [Context]`
  3. Add the bridges section (one line per bridge, SKOS mapping vocabulary):

## Cross-Context Bridges

- **Account** Billing ↔ Identity: distinct — service accounts have no ledger; guest checkout has a ledger but no login
- **Customer** Sales ↔ Identity: closeMatch — one Customer may own several Identity Accounts; never join on spelling

  Mapping is one of: exactMatch · closeMatch · broadMatch · narrowMatch · relatedMatch · distinct
  (SKOS mapping properties + explicit `distinct` for homonyms). Never `sameAs`.
-->
```

## Migrating an Existing Thesaurus

Read the format stamp first: `rg -n '^thesaurus-format:' THESAURUS.md`. No stamp, or
`1.x`, means **format 1.0** — `### Term` entries carrying `**Synonyms to AVOID**` lines,
no `## Index`. An unstamped file that already has ``- **Term** `Id` kind: `` Index lines was
written by plugin 9.2.0 — it is format 2.0, only step 0 applies. (An unstamped file whose
`## Index` is a Markdown table is an interim pre-2.0 draft; migrate it like 1.0.) Migrate in one pass — the content is the same,
only the shape changes:

0. **Stamp** the result: YAML frontmatter at the top of the file —
   `thesaurus-format: "2.0"`, `skill: ubiquitous-language`
   (replace an older stamp if present; merge into existing frontmatter if the file has any).

1. **Build the Index lines** from the entries (or table rows): Term = header text;
   Identifier = PascalCase of the term (or the name the code actually uses — grep to
   confirm); `kind:` = infer from the definition, default `concept`; `avoid:` = the
   `Synonyms to AVOID` list (or Avoid column), each in backticks.
2. **Strip** `**Synonyms to AVOID**` lines from the entries; rename `**Related terms**`
   to `**Related**`.
3. **Convert `## Legacy Terms` entries (or Legacy table rows) to `## Legacy` lines**:
   `` `Old` → `Replacement` in: <still found in> — <note> ``.
4. **Rename** `## Forbidden Lexicon` → `## Forbidden`; one `` `Word` use: `X` — why ``
   line per word.
5. **Contexts**: `## Bounded Context: X` sections → `## Terms: X`, headers `### Term (X)`,
   `ctx:X` on the Index lines; a Bridges table → one line per bridge with a SKOS mapping.
6. **Check the registry invariant** (see the audit's Check 0) and show the user the
   diff before writing — migration must not change a single definition.

### Format history

| Format | Skill | What changed |
|--------|-------|--------------|
| 1.0 | ≤ 1.x (plugin ≤ 9.1.1) | Prose entries with `Synonyms to AVOID`, `## Legacy Terms` entries, `## Forbidden Lexicon` table; no stamp |
| 2.0 | 2.0.0 (plugin 9.3.0) | Grep-first: `## Index` lines (`kind:` `ctx:` `avoid:`), `use:` Forbidden lines, `→` Legacy lines, SKOS bridge mappings, format stamp |

Bump the format **major** only when 1.x readers would misparse the file (a changed line
grammar or section set). Adding an optional token is a **minor** bump: stamp `2.1`, keep
every 2.0 line valid.

## Polysemy Unpacking

Some terms are "bundle-collapse" words — they silently stand in for multiple distinct
concepts. The word "service" is the canonical example: it can mean a promise, a system,
an endpoint, a commitment, a delivery method, or a work episode — all at once.

**When you encounter an overloaded term**, unpack it into its facets:

1. **Identify the facets** — what distinct things does this word refer to?
2. **Create separate thesaurus entries** for each facet with qualified names
3. **Add the bare word to `## Forbidden`** — it must always be qualified
4. **Document which facet is meant** in each code location

### Example: Unpacking "Service"

The bare word "service" collapses at least these facets:

| Facet | What it means | Qualified name |
|-------|--------------|----------------|
| Promise | What is offered/contracted | ServiceOffering |
| Provider | Who is accountable | ServiceProvider |
| Endpoint | What you can call/address | ServiceEndpoint |
| Delivery System | What performs the work | ServiceSystem |
| Commitment | The binding obligation (SLA) | ServiceCommitment |
| Delivery Work | A fulfillment episode | ServiceRun |

**The "can you X it?" tests:**
- "Can you call/restart it?" → it's an **endpoint**, not a promise
- "Can it guarantee/must it?" → it's a **commitment**, not an endpoint
- "How does it work?" → it's a **system** or **method**, not a promise
- "Is it down/slow?" → it's an **endpoint** or **work episode**, with evidence

### When to Unpack

Flag a term for polysemy unpacking when:
- The same word appears as subject of incompatible verbs ("the X is deployed" AND "the X promises")
- Different team members mean different things by the same word
- Code uses the term in structurally different ways across modules
- You can't answer "what type is this?" with a single answer

## Bounded Contexts and Polysemy

The same word can mean different things in different bounded contexts. This is correct
DDD — don't fight it, document it.

> "Cross-context sameness is never inferred from spelling; cross-context alignment is
> represented only via explicit Bridges." — FPF A.1.1

### When the Same Word Means Different Things

Example: "Account" across three contexts:
- **Payment Context**: Financial account with a balance
- **Customer Context**: User login credentials and profile
- **Accounting Context**: Ledger entry in chart of accounts

**Rules:**
- Each context owns its own definition in the thesaurus
- One Index line per (Term, Context) pair; group entries by context, alphabetical within
- If code has `if` statements checking "which context am I in?" — the boundary is wrong
- Use Anti-Corruption Layers at context boundaries for term translation
- **Never assume sameness from spelling** — "Account" in Payment and "Account" in Customer are different concepts that happen to share a label

### Recognizing Context Boundaries

You've found a boundary when:
- Domain experts disagree on what a term means
- Translation logic between modules keeps growing
- The same class name appears with different structures in different packages
- Teams use different words for the same concept (this is a signal, not a problem)

### Cross-Context Bridges

When terms appear in multiple contexts, document the **bridge** explicitly — one line
per bridge under `## Cross-Context Bridges`:

```
- **<Term>** <Context A> ↔ <Context B>: <mapping> — <loss notes>
```

- **mapping** uses the SKOS mapping vocabulary, plus an explicit `distinct` for homonyms:
  `exactMatch` (interchangeable in practice) · `closeMatch` (interchangeable in some
  uses) · `broadMatch` / `narrowMatch` (A is more general / more specific than B) ·
  `relatedMatch` (associated, neither subsumes) · `distinct` (same spelling, different
  concept). Never `sameAs` — cross-context identity is never inferred from spelling.
- **loss notes** — what breaks if you treat them as the same. The most important field.

```markdown
## Cross-Context Bridges

- **Account** Billing ↔ Identity: distinct — service accounts have no ledger; guest checkout has a ledger but no login
- **Order** Sales ↔ Fulfillment: narrowMatch — Fulfillment Order adds prep steps and timing, loses pricing
```

### Documenting Cross-Context Terms

```markdown
## Index

- **Account** `Account` kind:aggregate ctx:Billing avoid: `Wallet`, `Purse`, `Balance`
- **Account** `Account` kind:aggregate ctx:Identity avoid: `User`, `Profile`, `Login`

## Terms: Billing

### Account (Billing)
- **Definition**: Financial account with balance, used for charging and refunds
- **NOT**: User identity or login credentials (that's Account in Identity)

## Terms: Identity

### Account (Identity)
- **Definition**: User's login identity — email, password, profile
- **NOT**: Financial balance (that's Account in Billing)
```

`rg -n '^### Account( \(|$)'` returns both entries with their context in the header;
`rg -n 'ctx:Billing'` lists everything one context owns.

## Term Relationships

Use these relationship types to connect terms (based on ISO 25964 / SKOS):

| Relationship | Meaning | Example |
|-------------|---------|---------|
| **Broader** | More general concept | Repository is broader than GitHubRepository |
| **Narrower** | More specific concept | GitHubRepository is narrower than Repository |
| **Part-of** | Composition | Commit is part-of Repository |
| **Related** | Associated, not hierarchical | Repository is related to Branch |
| **Synonym** | Same concept, different word (pick one, avoid the other) | Codebase = Repository (avoid Codebase) |

Synonyms go to the Index `avoid:` list; the hierarchical relations are optional entry
lines, added only when they carry real information. Write each relation on one side
only — `rg` gives the inverse; mirrored copies drift. SKOS rule: a pair is never both
`Broader` and `Related`, and `Broader` chains never cycle.
```markdown
### Repository
- **Definition**: A version-controlled code storage location
- **Broader**: Version Control System
- **Narrower**: GitHub Repository, GitLab Repository, Monorepo
- **Has parts**: Branch, Commit, File
- **Related**: Code Source, Indexed Analysis
```
Write related names exactly as in the Index Term field, so `grep -n 'Branch'` finds
both the Branch Index line and every entry that points at it.

## Consistency Audit

For a full naming audit protocol (9 checks, severity levels, report format), see
[naming-audit.md](naming-audit.md).

## Brownfield Language Adoption

When introducing ubiquitous language to a project that already has an established
(but imprecise) vocabulary:

1. **Don't try to change how people talk overnight.** Language habits are ingrained.
   Correcting colleagues mid-conversation creates friction, not alignment.
2. **Control what you can first:** new code uses thesaurus terms, docs get updated,
   new API endpoints use canonical names, tests use domain language.
3. **Let conversational language follow.** As people read correct terms in code and
   PRs, spoken language shifts gradually. This takes weeks, not days.
4. **Watch for technical terms masquerading as domain language.** Stakeholders using
   DB table names as domain terms ("the users table" instead of "Customer") is a
   common brownfield pattern. Map these as `## Legacy` lines.
5. **Pick battles by frequency.** Fix terms used 200 times across the codebase before
   terms used in 3 files.

## Legacy Code Migration

When migrating from inconsistent legacy naming:

### Phase 1: Anti-Corruption Layer
Keep legacy code as-is. Create adapter layer with correct naming:
```
Legacy: class UserManager → New: class Customer (domain) + LegacyUserAdapter (boundary)
```

### Phase 2: Gradual Rename
- New code always uses thesaurus terms
- Old classes get "Legacy" prefix only at migration boundaries
- Use interfaces to decouple: `IOrderRepository` stays stable while implementation changes
- Wire command handlers to new implementation first

### Phase 3: Cleanup
- Delete legacy classes once all consumers migrated
- Remove "Legacy" prefixes
- Final audit against thesaurus

**Rules:**
- Never rename across all layers at once
- Use interfaces to decouple
- Config flags to toggle old vs new implementation during migration
