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
> Resolve the unresolved naming issues using the git history
```

## What it does

Four modes:

| Mode | When | What loads |
|------|------|-----------|
| **Naming consultation** | Every time the agent names anything | `SKILL.md` (~590 lines) |
| **Thesaurus generation** | User asks to create/update the thesaurus | `references/generating-thesaurus.md` (~540 lines) |
| **Naming audit** | User asks to check naming consistency | `references/naming-audit.md` (~280 lines) |
| **History mining** (optional) | Unresolved naming ambiguities need evidence | `references/git-history-mining.md` (~425 lines) + `scripts/git_term_index.py` (~1310 lines) |

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

### History mining (optional, offered at the end of generation)

The `## Unresolved` section is the honest part of a mined thesaurus — the questions the
current tree cannot answer. Git history often can. After generation (and after an audit),
the skill **offers** to build a throwaway index of the repository's history and come back
with evidence-backed proposals per unresolved item.

```bash
python3 scripts/git_term_index.py build --repo-dir . --content
python3 scripts/git_term_index.py query Account Customer
python3 scripts/git_term_index.py pair User Customer
python3 scripts/git_term_index.py contexts Account
python3 scripts/git_term_index.py search 'rename account'
python3 scripts/git_term_index.py clean
```

The index is dependency-free Python 3.9+ (stdlib `sqlite3`, only `git` required) and lives
as a single SQLite file in `$TMPDIR`, **never in the working tree**. Commit messages go into
an FTS5 table so message search is ranked by **BM25 relevance**, not recency; identifiers
from every added/removed diff line go into an `identifier × commit × file` table with
add/delete counts. Each identifier carries a casing-independent normal form, so
`OrderLineItem`, `order_line_item` and `ORDER_LINE_ITEM` are one concept — which is what
makes a PascalCase thesaurus Identifier findable in a snake_case codebase.

**Per-file granularity is what makes the common case answerable.** One commit touches many
files, so commit-level co-occurrence cannot localise a name (measured: one identifier's
directory distribution was 74% "wherever the code is"). With per-file rows the tool answers
the flagship `## Unresolved` question — `Account` in `billing/` vs `auth/` — directly:
`contexts Account` shows the directory split, and `pair` reports `files: A in N, B in M,
both in K`. `both in 0` is evidence for two bounded contexts; shared files mean synonym
drift. It also sharpens renames: an exchange **inside one file** outranks "both names
appear somewhere in one commit".

**The whole diff history is indexed, not a recent window** — that is the difference between
"born" and "first seen in the last N commits". Measured: git.git's full 21-year history
builds in 111 s (232 MB), kubernetes' 12 years / 82 704 commits in 249 s (1 040 MB); queries
then run in 0.1–1.3 s. Walking history per-term with `git log -S` instead costs 4 s per term on
git.git and 84–98 s per term on kubernetes.

What that buys per ambiguity: **birth** (which spelling is the incumbent, and what the
introducing commit said), **dormancy** (nothing has touched this name in years → retired
vocabulary), **trajectory** (deletions ≫ additions = being phased out), **ranked swap
commits** (the commits that remove one name while adding the other, strongest exchange
first — these are the renames), **the path split** (do any files contain
both names? which directories does each occupy? — the bounded-context signal), and **stated
intent** from BM25-ranked messages and PR references.

`pair` ends in one labelled verdict — **RENAME (strong / probable / possible)**, **DRIFT**,
**NOT A RENAME**, or **COEXISTENCE** — with the direction inferred from the evidence rather
than from argument order.

**The thresholds behind those labels were set by falsification, not taste.** Every one was
added after a measured false positive on a real repository:

| Rule | The false positive that forced it |
|------|-----------------------------------|
| A swap needs a **net** exchange (≥3 each way), not any deletion + any addition | 105 of 174 commits touching two unrelated integrations were labelled rename candidates — including commits where *both* names were net-removed |
| Identifiers carry a casing-independent **normal form** | `query OrderLineItem` returned "never appears" on a snake_case repo — a false negative on the skill's own canonical input, since thesaurus Identifiers are PascalCase |
| Comparing two names uses **concepts, not families** | the `Account` set contained `BillingAccount`, so its additions cancelled `Account`'s deletions and masked the exchange |
| Exchanges must clear a **noise floor** (≥2 commits and ≥5% of shared commits) | `bisect`/`rebase` in git.git: 2 exchanges in 145 shared commits read as "drift" |
| Same-file exchanges clear a lower bar, but still a bar | making any same-file swap sufficient put `bisect`/`rebase` straight back to RENAME on 2 swaps in 111 commits |
| A rename announcement must name **both** sides | "Rename Telegram meeting wrapper" certified `club` → `meeting` |
| Dormancy measured from **last growth**, not last touch | git.git's `get_sha1` was last *touched* in 2026 by a commit deleting a stale comment; last *grown* in 2017 |
| Locale and changelog files excluded | `.po` files made "l10n: zh_CN …" the top rename candidate for unrelated terms |

Measured after those fixes: **18 negative controls across three repositories → zero false
rename verdicts** (the worst of them reaches 6 same-file exchanges in 1 193 shared commits
and no naming subject), while every known rename — including kubernetes' `Minion`→`Node`,
which lands with 35 same-file swaps and 6 announcing subjects — still lands as RENAME — strong.

Other defaults from measurement: HEAD only (side branches carry release notes and imported
trees — on git.git, `--all` dated `oid_array` to a status email three days before the actual
rename commit), vendored/generated/minified paths excluded, merges excluded. Shallow clones,
truncated windows, and names present in the oldest indexed commit are each flagged in every
report rather than silently producing a confident wrong date.

**Known limits, stated in the skill:** `pair` compares identifiers, so a rename that only
moved files surfaces in `query`'s file-renames section instead; and polysemy — one word
meaning two things in two modules, the most common real `## Unresolved` entry — is the
weakest case for history mining, which will honestly return COEXISTENCE and leave the
decision to the user.

Findings are reported in one batch with a confidence level and the commits behind each
proposal; nothing is applied until the user approves, and each applied decision cites its
commit (`— renamed in a41f2c9` on the Legacy line, or a `- **History**:` entry line).
History is treated as evidence of what happened, never as authority on what a term should
be — it ranks candidates, the user decides. Squashed imports, shallow clones, bulk
reformatting commits, and vendored code are called out as the failure modes they are.

### Naming audit (periodic)

9-check protocol: thesaurus integrity (registry invariant, Index ↔ Terms), synonym violations, forbidden words, technical jargon leaks, synonym drift, polysemy, translation chains, abbreviation inconsistency, orphan terms. The Index is the audit's work-list. Produces a structured report grouped by severity (Critical / Warning / Info) with recommended fix priority.

## Key features

- **Grep-first thesaurus** — one labelled line per concept, registry invariant, exact-match backticks; built for agents that navigate by `rg`, not by reading whole files
- **Codebase is primary evidence, not automatic authority** — supports both "as-is" (document current naming) and "to-be" (define target vocabulary) modes
- **Flat-first thesaurus** — no bounded contexts by default; only introduced when polysemy is confirmed by the user with the invariant test
- **Forbidden list** (lexical firewall) — maintained list of words banned from the domain layer (weasel words, implementation details)
- **Polysemy unpacking** — detects overloaded terms and forces disambiguation into explicit facets
- **Cross-context bridges** — when bounded contexts exist, one line per bridge with a SKOS mapping (`exactMatch` … `relatedMatch`, `distinct`) and loss notes
- **Git-history mining for ambiguities** — a throwaway SQLite index (built outside the repo, deleted after) over the *full* diff history: BM25-ranked commit messages, renames, and every identifier's birth, dormancy and swap commits; proposes rename / deprecate / two-concepts / drift verdicts with citations and confidence, never silently
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
- **History as evidence, not authority**: mining is an *offer* made after the Unresolved list is shown, not an automatic step, and it produces ranked hypotheses with commit citations — the user still makes every call. The index is deliberately throwaway (temp dir, one command to delete) rather than a committed artifact: it is derived data, it goes stale on the next commit, and nothing in a repository should be generated into the working tree
- **No format change**: history provenance rides in existing free-text — the note tail of a `## Legacy` line, or an optional `- **History**:` entry line — so `thesaurus-format` stays `2.0` and no migration is needed

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

## Versioning

- **Skill**: `metadata.version` in `SKILL.md` frontmatter (semver). Current: **2.1.0**.
- **Thesaurus format**: stamped in every `THESAURUS.md` as YAML frontmatter —
  `thesaurus-format: "2.0"`, `skill: ubiquitous-language`. One `rg '^thesaurus-format:'` tells an agent which grammar to expect; a missing key means format 1.0 (the pre-index prose layout).
- Format major = skill major. The skill reads any format ≤ its own and writes only the current one; a major gap triggers the one-pass migration, a minor gap only adds optional tokens.
- Format history lives in `references/generating-thesaurus.md` → "Format history".

## File structure

```
ubiquitous-language/
├── SKILL.md                         # Naming consultation (loaded on every trigger)
├── README.md                        # This file
├── references/
│   ├── generating-thesaurus.md      # Thesaurus generation workflow
│   ├── naming-audit.md              # 9-check naming audit protocol
│   └── git-history-mining.md        # Resolving `## Unresolved` items from git history
└── scripts/
    └── git_term_index.py            # Throwaway SQLite/FTS5 history index (build/query/pair/contexts/search/clean)
```

## License

MIT
