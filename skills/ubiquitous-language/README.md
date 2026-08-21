# ubiquitous-language

Maintain a project thesaurus (domain glossary) following DDD ubiquitous language principles. Ensures all names in the codebase are consistent, descriptive, and aligned with the shared domain vocabulary.

## Install

```bash
npx skills add CodeAlive-AI/ai-driven-development@ubiquitous-language -g -y
```

## Quick start

After installing, try these in your project:

```
> Create a domain thesaurus for this project
> What should I call the entity that tracks user payments?
> Audit naming consistency in this codebase
```

## What it does

Three modes:

| Mode | When | What loads |
|------|------|-----------|
| **Naming consultation** | Every time the agent names anything | `SKILL.md` (~495 lines) |
| **Thesaurus generation** | User asks to create/update the thesaurus | `references/generating-thesaurus.md` (~470 lines) |
| **Naming audit** | User asks to check naming consistency | `references/naming-audit.md` (~270 lines) |

### Naming consultation (frequent)

Before proposing any name, the agent greps the project's `THESAURUS.md` for every candidate name and acts on the shape of the hit line (Index, Forbidden, Legacy, Unresolved, or nothing). If the concept is new, it tries four levers before minting a new term: Reuse, Compose, Qualify, Ask. Includes DDD naming rules for aggregates, entities, value objects, events, commands, queries, services, and repositories.

### The grep-first thesaurus layout

`THESAURUS.md` is shaped so that **one `rg` for any name answers "what do I do with this name?"**. Registry sections are one-line-per-item bullet lists with labelled tokens — not Markdown tables, because `|` is an alternation in ripgrep (the Grep tool of most agents), tables match by column position, and formatters re-pad them.

```markdown
## Index                      ← one line per concept, every name for it
- **Order** `Order` kind:aggregate avoid: `Purchase`, `Transaction`, `Buy`
- **Account** `Account` kind:aggregate ctx:Billing avoid: `Wallet`, `Balance`

## Terms                      ← `### Term` entries: Definition / NOT / Related
## Forbidden                  ← - `Manager` use: `OrderFulfillment` — hides responsibility
## Legacy                     ← - `Basket` → `Cart` in: `api/v1/basket.ts` — renamed v2
## Unresolved                 ← `### Term — problem` entries awaiting a decision
```

```bash
rg -n -i 'basket'            # any role — the shape of the hit line tells you the section
rg -n 'avoid:.*`Purchase`'   # banned synonym → the canonical Identifier is at line start
rg -n 'kind:event'           # all events;  rg 'ctx:Billing' → everything one context owns
rg -n -F '**Order**'         # exact Term, not "Order Line Item"
rg -n '^### Order( \(|$)'    # the entry itself
```

- **Registry invariant**: every name appears in exactly one registry line, so the *shape* of a hit gives its status and the *line* gives the canonical name — no `-B`/`-A` context reading.
- `Identifier` is the PascalCase code form — what agents actually see in code and grep for; `Term` stays in the domain's own language (``**Счёт-фактура** `Invoice` ``).
- Backticks around every name make `` rg '`Order`' `` an exact match that skips `OrderLineItem`.
- `kind:` selects the DDD naming rule; `ctx:` appears only once bounded contexts are confirmed.
- Existing thesauri (prose-only or table-index) are migrated in one pass without changing a definition.

### Thesaurus generation (rare)

Scans high-signal structural files (DB schemas, API contracts, domain layer, directory structure) to extract domain terms. Separates active from legacy/obsolete terms. Collects ambiguities into an `## Unresolved` section, then surfaces them to the user for resolution. Updates agent instruction files (`CLAUDE.md`, `GEMINI.md`, etc.) so the thesaurus is used even without the skill installed.

### Naming audit (periodic)

9-check protocol: thesaurus integrity (registry invariant, Index ↔ Terms), synonym violations, forbidden words, technical jargon leaks, synonym drift, polysemy, translation chains, abbreviation inconsistency, orphan terms. The Index is the audit's work-list. Produces a structured report grouped by severity (Critical / Warning / Info) with recommended fix priority.

## Key features

- **Grep-first thesaurus** — one labelled line per concept, registry invariant, exact-match backticks; built for agents that navigate by `rg`, not by reading whole files
- **Codebase is primary evidence, not automatic authority** — supports both "as-is" (document current naming) and "to-be" (define target vocabulary) modes
- **Flat-first thesaurus** — no bounded contexts by default; only introduced when polysemy is confirmed by the user with the invariant test
- **Forbidden list** (lexical firewall) — maintained list of words banned from the domain layer (weasel words, implementation details)
- **Polysemy unpacking** — detects overloaded terms and forces disambiguation into explicit facets
- **Cross-context bridges** — when bounded contexts exist, one line per bridge with a SKOS mapping (`exactMatch` … `relatedMatch`, `distinct`) and loss notes
- **Legacy term tracking** — continuity relations (rename/split/merge/retire/deprecate) with alias parsimony
- **Framework-aware** — doesn't fight Active Record patterns; distinguishes domain noun from framework coupling
- **Language-agnostic** — works with any programming language, no framework-specific rules
- **Non-English domain support** — uses the domain's original language for canonical terms

## Sources and methodology

This skill was built through a structured research and review process:

### Primary sources

1. **Domain-Driven Design** by Eric Evans — ubiquitous language, bounded contexts, aggregate naming, anti-corruption layers
2. **Learning Domain-Driven Design** by Vlad Khononov — practical DDD patterns including brownfield adoption strategy, co-creation (not extraction) of domain language, tacit knowledge handling, translation chain anti-pattern, thesaurus scoping heuristics
3. **[First Principles Framework (FPF)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md)** — formal tools for semantic precision:
   - A.1.1 `U.BoundedContext` — bounded contexts as declared semantic frames with the invariant test for justification
   - A.6.8 Service Polysemy Unpacking — "can you X it?" disambiguation tests for overloaded terms
   - A.6.9 Cross-Context Sameness Disambiguation — bridges with loss notes, direction, and relationship types
   - E.5.1 DevOps Lexical Firewall — protecting domain vocabulary from transient implementation jargon
   - F.2 Term Harvesting & Normalisation — context-local harvesting discipline
   - F.5 Naming Discipline — "name what the invariants make true", minimal generality
   - F.13 Lexical Continuity & Deprecation — five continuity relations (rename/alias/split/merge/retire)
   - F.14 Anti-Explosion Control — "four levers before minting a new name"
4. **ISO 25964 / SKOS** — label model (prefLabel / altLabel / notation), BT/NT/RT relations and their integrity rules, mapping vocabulary for cross-context bridges — see Standards alignment
5. **Martin Fowler**, **Vaughn Vernon** — bounded context maps, anti-corruption layers, context boundaries as language boundaries

### Web research

- DDD ubiquitous language best practices and common failures (synonym drift, naming chaos, acronym problems)
- Domain glossary/thesaurus management formats and standards
- DDD naming rules by construct type (aggregates, entities, value objects, events, commands)
- Naming anti-patterns in domain code (weasel words, technical jargon leaks, implementation-driven naming)
- Codebase auditing approaches for naming consistency

### Multi-agent review

The skill was reviewed by external AI agents (OpenAI Codex CLI / GPT-5.4 and Google Gemini CLI / Gemini 3.1 Pro) via the [agents-consilium](../agents-consilium/) skill for independent, unbiased assessment. The review identified 6 critical operational issues:

1. **Scanning impossibility** — original instructions assumed whole-codebase scanning; replaced with bounded high-signal hub strategy
2. **O(N^2) audit check** — field-overlap comparison replaced with grep-friendly stem+suffix heuristics
3. **External system assumptions** — translation chain check rewritten for local-only filesystem access (git log, test descriptions, local docs)
4. **Missing language idiom exceptions** — added durability boundary: DDD naming for domain-bearing identifiers, standard idioms (`err`, `ctx`, `i`) exempt
5. **Source of truth dogma** — "trust the code" replaced with "code is evidence, not authority" with explicit brownfield/legacy override
6. **Framework antagonism** — added caveat for Active Record patterns where domain and persistence are intentionally blended

### Design decisions

- **Progressive disclosure**: SKILL.md (naming consultation) loads on every trigger; references load only on demand — saves ~700 lines of context on the common path
- **Grep-first over read-everything**: agents consult the thesaurus on every naming task, so lookup cost matters more than prose quality. The Index (one line per concept) is cheap to read whole; everything else is reached by a single `rg` whose hit is self-describing. Avoid lists live only in the Index so there is one place to drift from — none
- **Labelled lines, not tables, for registry data**: Index, Forbidden (`use:`) and Legacy (`→`, `in:`) are one-line facts with position-free tokens — greppable without escaping `|`, immune to formatter re-padding, and each line's shape reveals its section. Definitions and open questions stay as prose entries
- **Non-English domains get two columns, not a compromise**: `Term` holds the experts' word, `Identifier` the code form, so the thesaurus is greppable from either side
- **Flat-first thesaurus**: bounded contexts are opt-in, not default — the agent cannot reliably determine context boundaries, so it surfaces evidence and asks the user
- **Unresolved section**: ambiguities collected during scanning, surfaced as a batch after file creation — no blocking questions during generation
- **Agent instruction updates**: after creating the thesaurus, the skill updates CLAUDE.md/GEMINI.md/etc. so the thesaurus works even without the skill installed

## Standards alignment

The layout is a plain-Markdown projection of a SKOS concept scheme (ISO 25964-compatible) — exportable to RDF/JSON-LD if ever needed, without being written in it.

| Thesaurus | SKOS / ISO 25964 |
|-----------|------------------|
| `**Term**` | `skos:prefLabel` — one per concept and context |
| `` `Identifier` `` | `skos:notation` — machine code, distinct from the label |
| `avoid:` | `skos:altLabel` + `skos:hiddenLabel` (ISO 25964: `UF`, use-for) |
| `Definition` / `NOT` | `skos:definition` / `skos:scopeNote` |
| `Broader` / `Narrower` / `Related` | `BT` / `NT` / `RT` — written on one side only, `rg` gives the inverse |
| `### Term (Context)` | ISO 25964 homograph qualifier |
| Legacy `` `Old` → `New` `` | `owl:deprecated` + `skos:historyNote`; `A + B` = compound equivalence |
| Bridge mapping | `skos:exactMatch` … `relatedMatch` (+ explicit `distinct`); never `owl:sameAs` |
| Unresolved → Index → Legacy | concept status: candidate → approved → deprecated |

Deliberately not borrowed: `ConceptScheme`/`Collection`, facets, OWL axioms, RDF serialisation — `kind:`/`ctx:` and prose `NOT` cover the need without the weight.

## File structure

```
ubiquitous-language/
├── SKILL.md                         # Naming consultation (loaded on every trigger)
├── README.md                        # This file
└── references/
    ├── generating-thesaurus.md      # Thesaurus generation workflow
    └── naming-audit.md             # 9-check naming audit protocol
```

## License

MIT
