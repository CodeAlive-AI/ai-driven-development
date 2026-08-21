---
name: ubiquitous-language
description: |
  Maintain a project thesaurus (domain glossary) following DDD ubiquitous language
  principles. Use PROACTIVELY when naming anything: variables, functions, classes,
  modules, database fields, API endpoints, events, files, or directories. Also use
  when the user asks to "create thesaurus", "update glossary", "add term", "rename
  to match domain", "check naming consistency", "what should I call this", "domain
  language", "ubiquitous language", or "naming conventions". Ensures all names in
  the codebase are consistent, descriptive, and aligned with the shared domain
  vocabulary. Not for general code style or linting — only for domain term
  consistency.
metadata:
  version: "2.0.0"
  thesaurus-format: "2.0"
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - Agent
  - AskUserQuestion
---

# Ubiquitous Language: Project Thesaurus Manager

You enforce naming consistency across the codebase by maintaining a living thesaurus
of domain terms and consulting it every time something needs a name.

**Three modes:**
- **Naming consultation** (frequent) — everything in this file
- **Thesaurus generation** (rare) — read [references/generating-thesaurus.md](references/generating-thesaurus.md)
- **Naming audit** (periodic) — read [references/naming-audit.md](references/naming-audit.md)

## Foundations

This skill combines two bodies of knowledge:

- **Domain-Driven Design (DDD)** by Eric Evans — ubiquitous language, bounded contexts, aggregate naming
- **[First Principles Framework (FPF)](https://github.com/ailev/FPF/blob/main/FPF-Spec.md)** — a transdisciplinary "operating system for thought" that provides formal tools for semantic precision: bounded contexts as declared semantic frames, polysemy unpacking, lexical firewalls, cross-context bridges with loss notes, term continuity relations, and anti-explosion naming control. References like "FPF F.5" or "FPF A.1.1" point to specific sections of the FPF specification.

## Core Principle

> "A project should use a single, shared vocabulary. Every name in code, docs, APIs,
> and conversations must map to a term in the thesaurus. If a concept isn't in the
> thesaurus — add it before naming anything."
>
> — Domain-Driven Design, Eric Evans

**The codebase is primary evidence, not automatic authority.** Use code to discover
which terms are currently in circulation. Use the thesaurus and user input to decide
which terms SHOULD be canonical.

- For **what exists today** — derive from code (classes, DB schemas, API routes, events)
- For **what should become the standard** — ask the user/domain expert
- If code contradicts the approved thesaurus — the thesaurus wins for new code
- If the user says "fix legacy naming" — the user's directive overrides the codebase;
  map existing code names to `## Legacy` lines and use the user's terms as canonical

**Tacit knowledge**: For areas not yet implemented, the most important domain knowledge
exists only in experts' heads, not in any artifact.

## Thesaurus File

**Locating the thesaurus:**
1. If the user specified a path — use it
2. If `THESAURUS.md` already exists somewhere in the repo — use that location
3. Default: `docs/THESAURUS.md`

Single source of truth for domain vocabulary.

### Versioning

The thesaurus declares its **format version** and the skill that maintains it in YAML
frontmatter — machine-readable, outside the body, still one grep away:

```markdown
---
thesaurus-format: "2.0"
skill: ubiquitous-language
---

# Project Thesaurus
```

Quote the version — unquoted `2.10` is the YAML float `2.1`.

- `rg -n '^thesaurus-format:' THESAURUS.md` → the version in one hit. **No key = 1.0**
  (the pre-index prose layout shipped before skill 2.0) — unless the file already has
  ``- **Term** `Id` kind: `` Index lines: that is an unstamped 2.0 file from plugin 9.2.0;
  just add the stamp.
- Format major = skill major (`metadata.version` in this file's frontmatter). Skill
  minor/patch releases never change the format.
- **Read** any format ≤ your own; **write** only the current one. A major gap means
  migration first (see generating-thesaurus.md); a minor gap means new optional tokens —
  older readers keep working, you may add the tokens as you touch lines.
- A thesaurus with a format **newer** than yours: read it, don't rewrite it — tell the user
  to update the skill.
- Only the format is versioned in the file. The skill's own version is not recorded there —
  it would go stale on every edit and `git log` already answers "who wrote this". `skill:`
  is a pointer, so an agent without the skill knows what to install.

| Format | Layout | Skill |
|--------|--------|-------|
| 1.0 | `### Term` entries with `Synonyms to AVOID`; `## Legacy Terms` entries; `## Forbidden Lexicon` table | ≤ 1.x (plugin ≤ 9.1.1) |
| 2.0 | grep-first: `## Index` lines with `kind:`/`ctx:`/`avoid:`, `use:` Forbidden lines, `→` Legacy lines, SKOS bridges | 2.x |

### Layout: grep-first

The file is designed so that **one `rg`/`grep` for any name answers "what do I do with
this name?"** without reading the surrounding text. Five sections, fixed order:

| Section | Shape | One line answers |
|---------|-------|------------------|
| `## Index` | one line per concept | "Is there a term for this? Which name is canonical? What is banned?" |
| `## Terms` | `### Term` entries | "What exactly does it mean / not mean / relate to?" |
| `## Forbidden` | one line per word | "Is this word banned from domain names?" |
| `## Legacy` | one line per old name | "This old name is in the code — what replaced it?" |
| `## Unresolved` | `### Term — problem` entries | "Is this name an open question?" |

**Registry invariant:** every name known to the project appears in **exactly one**
registry line — an Index line (as Term, Identifier, or avoid), a Forbidden line, a Legacy
line, or an Unresolved header. Each kind of registry line has its own shape, so the
*shape of the hit* tells you its status and the *line itself* tells you the canonical
name. No `-B`/`-A` context needed.

Registry lines are **bullet lines with labelled tokens**, not Markdown tables: tables
need `|` (an alternation in `rg`), match by column position, and get re-padded by
formatters. Tokens (`kind:`, `ctx:`, `avoid:`, `use:`, `in:`, `→`) are position-free,
formatter-proof, and need no escaping.

```markdown
# Project Thesaurus

## Index

- **Order** `Order` kind:aggregate avoid: `Purchase`, `Transaction`, `Buy`
- **Order Line Item** `OrderLineItem` kind:entity avoid: `LineItem`, `OrderItem`, `Item`
- **Order Placed** `OrderPlaced` kind:event avoid: `OrderCreated`, `NewOrder`

## Terms

### Order
- **Definition**: A customer's confirmed request to buy one or more products at agreed prices.
- **NOT**: A payment (that's `Payment`), a shipment, or a draft cart (that's `Cart`).
- **Related**: Order Line Item, Order Placed, Cart

## Forbidden

- `Manager` use: `OrderFulfillment` — hides responsibility; name the activity

## Legacy

- `UserManager` → `Customer` + `CustomerRegistration` in: `src/legacy/` — split in v3

## Unresolved

### Account — one word, two concepts (billing vs auth)
- **Found in**: `billing/Account.ts` (balance), `auth/Account.ts` (login)
- **Question**: Two bounded contexts, or one of them a naming mistake?
- **Impact**: 18 files
- **Options**: `BillingAccount` + `UserAccount`; or contexts Billing / Identity
```

### Index line

```
- **<Term>** `<Identifier>` kind:<kind> [ctx:<Context>] [avoid: `<name>`, `<name>`]
```

| Field | Content | Rules |
|-------|---------|-------|
| **Term** | Human name, as domain experts say it, in `**bold**` | May be multi-word or non-English. Also the `### ` header text of the entry |
| **Identifier** | PascalCase code form, in backticks | The thing you grep in code. All other casings derive from it mechanically (see Casing) |
| **kind:** | One of `aggregate` `entity` `value` `event` `command` `query` `service` `role` `process` `state` `policy` `concept` | Picks the naming rule below. `concept` when nothing fits |
| **ctx:** | Bounded context name | Only present once contexts are confirmed (see generating-thesaurus.md); the header then becomes `### Term (Context)` |
| **avoid:** | Banned synonyms and abbreviations, each in backticks, comma-separated | Last on the line because it is the only variable-length field. Omit when empty |

- **One line per concept.** All names for that concept live on that line — this is what
  makes reverse lookup (`rg Purchase` → "use `Order`") a single hit.
- **Backticks around every identifier-like name.** `` rg '`Order`' `` is an exact match;
  `rg Order` would also hit `OrderLineItem` and `Reorder`. `rg -F '**Order**'` is the
  exact Term.
- **Sorted alphabetically by Term.** Entries under `## Terms` follow the same order.
- **avoid lists live only here.** Entries do not repeat them — one place, no drift.

### Forbidden and Legacy lines

```
- `<Word>` use: `<Identifier>`[, `<Identifier>`] — <why>
- `<OldName>` → `<Identifier>`[ + `<Identifier>`] in: <files/modules> — <note>
- `<OldName>` → — (see `<X>`, `<Y>`) in: <files> — retired
```

`use:` always points at an Index Identifier. `→` is the legacy marker: `A + B` means the
old name was split; `→ —` means retired with no single successor.

### Entry

```markdown
### [Term]
- **Definition**: What this concept means in the business domain — one sentence
- **NOT**: What this term does NOT mean; name the neighbouring term it is confused with
- **Related**: Other Index Terms this connects to, written exactly as in the Term field
```

Optional lines when they carry real information: `**Broader**`, `**Narrower**`,
`**Part of**`, `**Has parts**`, `**Example**`. Write them on one side only — `rg` gives
the inverse for free, mirrored copies only drift. Minimal viable entry is one line:
`- **Definition**: …` — the Index line already holds the rest.

**Anchor grammar** (so lookups are one regex): the header is exactly `### <Term>` or
`### <Term> (<Context>)` — nothing else. Tags, status, and context prefixes belong in
the Index line, not in the header. Find an entry with `rg -n '^### Order( \(|$)'` —
`\b` alone is not enough, it would also match `### Order Line Item`.

**The thesaurus captures concepts, not behavior.** It's strong at nouns (entity names,
roles, process names) but won't replace behavioral specs for business rules. Don't try
to turn the thesaurus into a specification — keep entries short. If a concept has a
critical invariant, note it briefly in the definition, not as a separate section.

**Non-English domains**: If the business domain operates in a non-English language, the
**Term** uses the original language — the thesaurus should reflect how domain experts
actually speak. The **Identifier** carries the code form:
``- **Счёт-фактура** `Invoice` kind:entity``. This is exactly why both fields exist.

## Lookup Protocol

**Look up before inventing. This is the single most important step.** Most naming tasks
don't need a new term — the right name is already there.

1. **Locate** the thesaurus (see above). If absent, tell the user and offer generation.
   Check `rg -n '^thesaurus-format:'` — no key or `1.x` means the old layout: the
   protocol below still works by plain text search, but offer migration once, up front.
2. **Read the Index** if it has ≤ ~60 lines — it is the entire vocabulary at one line
   per concept, cheaper than any search. For larger files, search instead.
3. **Search every candidate name** you are considering, plus whatever the surrounding
   code already calls the thing. Use `rg` (the Grep tool) or `grep -E` — same patterns:

   ```bash
   rg -n -i 'invoice' docs/THESAURUS.md             # any role, any section
   rg -n '`OrderLineItem`' docs/THESAURUS.md        # exact identifier as seen in code
   rg -n -F '**Order**' docs/THESAURUS.md           # exact Term (not "Order Line Item")
   rg -n 'avoid:.*`Purchase`' docs/THESAURUS.md     # is this word a banned synonym?
   rg -n 'kind:event' docs/THESAURUS.md             # all terms of one kind
   rg -n 'ctx:Billing' docs/THESAURUS.md            # everything one context owns
   rg -n '`Basket` →' docs/THESAURUS.md             # legacy name and its replacement
   rg -n -A4 '^### Invoice( \(|$)' docs/THESAURUS.md  # the entry itself
   ```

   The only trap: `*` and `|` are regex metacharacters — use `-F` for `**Term**`, and
   never search for table pipes (there are none).

4. **Act on the shape of the line you hit:**

   | Hit line looks like | Meaning | Do |
   |---------------------|---------|----|
   | ``- **X** `X` kind:… `` — your word is the Term or Identifier | Concept exists | Use the Identifier exactly. Stop |
   | ``- **X** … avoid: … `your word` `` | You were about to use a banned synonym | Use that line's Identifier instead |
   | `` - `word` use: … `` | Word is banned from domain names | Pick the Identifier after `use:` |
   | `` - `word` → … `` | Old name still in code | Use the replacement after `→` for new code; don't spread the legacy name |
   | `### word — …` under `## Unresolved` | Open naming question | Don't decide silently — surface it, or ask the user |
   | `### ` header / entry text only | Related concept | Read the entry; it may inform composition |
   | No hit | New concept | Go to "If the concept is new" |

5. **Check the bounded context** if Index lines carry `ctx:` — the same word may be
   canonical in one context and banned in another.

**ALWAYS** run this before naming: classes, interfaces, types, enums, aggregates,
entities, value objects, functions, methods, commands, queries, domain events,
variables, constants, fields, parameters, DB tables/columns/collections, API endpoints
and response fields, files, directories, modules, packages, feature flags, config keys,
environment variables, and commit messages or PR titles that reference domain concepts.

## If the Concept Is New

**Before minting a new term, try four levers** (from FPF F.14 "Name less, express more"):

1. **Reuse** — does an existing term already cover this? Maybe the concept is a variant, not a new thing
2. **Compose** — can you combine existing terms? `OrderLineItem` reuses `Order` + `LineItem`
3. **Qualify** — is this the same concept in a different state/window? Don't create `NightOperator` — use `Operator` with a time qualifier
4. **Ask** — if still unclear: "I need to name [concept]. The thesaurus doesn't have a term for this. What does the domain call it?"
   **If the user doesn't have an answer either** — that's a white spot, not a dead end.
   Building a ubiquitous language is co-creation, not extraction. Add it to `## Unresolved`
   with a `[WHITE-SPOT]` tag in the header. Don't force a name for an undefined concept.

Only after all four fail, mint a new term:
1. **Name what the invariants make true** (FPF F.5) — don't name aspirationally. If the code doesn't enforce "Premium", don't call it `PremiumCustomer`
2. **Use minimal generality** — choose the narrowest name whose rules you actually enforce. Don't upgrade `Task` to `Activity` to sound universal
3. **Keep it to 1-3 words** — no rhetorical adjectives ("robust", "optimal", "advanced")
4. **Add it to the thesaurus**: an Index line (Term, Identifier, `kind:`, `avoid:` —
   omit `avoid:` when empty) **and** a `### Term` entry with at least a Definition. Keep both sorted
5. **Then** use the term in code

## If You Find an Inconsistency

When existing code uses a term that contradicts the thesaurus:
- Flag it: "Found `fetchPurchases()` but the Index line says `Order`, with `Purchase` under `avoid:`"
- Suggest a rename if scope is small
- For large-scale renames, note as tech debt and ask user how to proceed

## Naming Rules by DDD Construct

The Index `Kind` column selects the rule.

### Aggregates & Aggregate Roots (`aggregate`)
Use the business domain term. Singular. No technical suffixes.

```
GOOD: Order, Invoice, UserAccount, ShoppingCart
BAD:  OrderAggregate, OrderRoot, OrderAggregateImpl, OrderEntity
```

### Entities (`entity`)
Singular noun from the domain. Something with identity.

```
GOOD: OrderLineItem, PaymentTransaction, Customer
BAD:  OrderLineItemEntity, OrderLineItemImpl, OrderLineItemObj
```

### Value Objects (`value`)
Singular noun describing an immutable concept. Describes **what it is**, not what it does.

```
GOOD: Money, Email, PhoneNumber, Address, DateRange
BAD:  MoneyValue, EmailValidator, PriceInfo, AmountData
```

### Domain Events (`event`)
**Past tense verb + noun.** Something that happened.

```
GOOD: OrderPlaced, PaymentCaptured, InvoiceSent, InventoryReserved
BAD:  OrderEvent, OnOrderPlaced, CreateOrder (that's a command)
```

### Commands (`command`)
**Imperative verb + noun.** An action requested.

```
GOOD: CreateOrder, CancelInvoice, ProcessRefund, ReserveInventory
BAD:  OrderCreated (that's an event), NewOrder, OrderCommand
```

### Queries (`query`)
Question or retrieval. Verb + object or descriptive name.

```
GOOD: GetOrderById, FindInvoicesByCustomer, ListPendingOrders
BAD:  RetrieveOrderData, OrderQuery, GetterForOrder
```

### Domain Services (`service`)
Named after **business activities** the domain expert recognizes.

```
GOOD: InvoiceCalculator, OrderFulfillment, NotificationSender
BAD:  OrderManager, GenericService, HelperService
```

### Repositories
Repository suffix is acceptable — it's an infrastructure pattern. Repositories are not
thesaurus terms; they take the name of the aggregate they store.

```
GOOD: OrderRepository, InvoiceRepository, CustomerRepository
BAD:  OrderStorage, OrderPersistence, OrderFinder, OrderDao
```

### Methods on Aggregates

**Commands (change state):** Imperative verb, no "Get" prefix.
```
GOOD: order.Cancel(), order.AddLineItem(product, quantity), order.Recalculate()
BAD:  order.CancelOrderMethod(), order.GetCancelled(), order.DoCancelOrder()
```

**Queries (read-only):** Start with Get, Is, Has, Can, or a domain verb.
```
GOOD: order.GetTotal(), order.IsExpired(), order.CanBeShipped()
BAD:  order.FetchInfo(), order.CheckData()
```

## Naming Anti-Patterns to Detect and Flag

### Lexical Firewall: the `## Forbidden` section

The domain layer must be protected from transient jargon, vague terms, and
implementation details. The thesaurus's `## Forbidden` section lists words that MUST NOT
appear in domain names and must always be replaced with a specific domain term.

### Weasel Words (never use in domain layer)

| Weasel Word | Problem | Fix |
|-------------|---------|-----|
| `Info` | Meaningless suffix | Remove it: `UserInfo` -> `User` |
| `Data` | Says nothing about the concept | Use domain term: `OrderData` -> `Order` |
| `Manager` | Vague, hides responsibility | Split by actual responsibility |
| `Handler` | Generic, unclear intent | Name after what it handles |
| `Service` | Overused catch-all | Use specific domain activity name |
| `Base` | Technical distraction | Remove, use composition |
| `Item` | Too generic | Use domain term: `Item` -> `OrderLineItem`, `Product` |
| `Util` / `Helper` | Indicates bad design | Move logic to domain objects |
| `Object` / `Obj` | Never appropriate | Remove suffix |
| `Record` / `Model` | Database concept leaking into domain | Use domain term |
| `Config` / `Settings` | Generic container hiding a concept | `Config` -> `LoanProduct`, `Settings` -> `NotificationPreferences` |

### Technical Jargon in Domain Layer

Domain code must be free of implementation details:

```
BAD:  MongoOrder, SqlUserRepository, HttpOrderService, OrderDto, OrderEntity
GOOD: Order, OrderRepository (interface), PaymentGateway, Order (just Order)
```

Technical prefixes/suffixes belong ONLY in the infrastructure layer, and even there the
domain role should lead:
```
INFRASTRUCTURE LAYER (OK): MongoOrderRepository, RedisSessionCache, HttpPaymentClient
DOMAIN LAYER (NEVER):      MongoOrder, RedisSession, HttpPayment
NAME THE ROLE, NOT THE TECH: SessionStore not RedisCache, EventPublisher not KafkaProducer
```

**Framework caveat**: In frameworks that intentionally blend domain and persistence
(Active Record pattern, ORM-centric frameworks), the model IS the domain entity.
Keep the **domain noun clean** and let framework coupling live in inheritance,
annotations, or metadata — not in the class name. Flag technical jargon only when
it becomes part of the business-facing name or leaks outside its boundary.

### Synonym Drift

Same concept called different things in different parts of code:

```
PROBLEM: "Customer" in auth, "User" in API, "Account" in billing — all mean the same thing
FIX:     Pick ONE canonical term per bounded context. Put the others in that line's `avoid:` list.
```

### Abbreviation Boundary

Ban abbreviations in **durable, domain-bearing names**: types, exported functions,
modules, API fields, DB columns, events, config keys.

Allow **conventional short-lived local identifiers** when meaning is obvious in scope:
`i`, `j`, `ctx`, `req`, `res`, `err`, `tx`, `db`, `e` for events.

Allow **industry-standard acronyms** when they are the dominant term: `SKU`, `VAT`,
`URL`, `ID`, `OAuth`. Do NOT force unnatural expansions if experts use the acronym.

```
PROBLEM: usr, user, account, acct — competing abbreviations for the same durable concept
FIX:     Pick ONE canonical form for domain-bearing names. Short-lived locals are exempt.
```

### Translation Chain ("Telephone Game")

When different artifacts use different terms for the same concept across the
knowledge chain, information is lost at each translation:

```
SMELL: Domain expert says "Campaign" → PM writes "Promotion" in spec →
       Dev codes `marketing_push` → QA tests "advertising effort"
FIX:   Same term everywhere: expert, PM, dev, QA all say and write "Campaign"
```

This is worse than synonym drift because each translation also loses nuance and
business rules. **How to detect:** compare terms in requirements/specs/tickets
against code names. If they don't match, the ubiquitous language has a translation
gap — adopt the domain expert's term everywhere.

## Casing Conventions

The Index `Identifier` is PascalCase. Every other form is derived from it mechanically
using the project's conventions — never re-worded:

| Context | Convention | Example (Identifier: `OrderLineItem`) |
|---------|-----------|------------------------|
| Class/Type | PascalCase | `OrderLineItem` |
| Function/Method | Project convention | `addOrderLineItem` / `add_order_line_item` |
| Variable | Project convention | `orderLineItem` / `order_line_item` |
| Constant | UPPER_SNAKE | `MAX_ORDER_LINE_ITEMS` |
| Database table | Project convention | `order_line_items` |
| API endpoint | kebab-case or convention | `/orders/{id}/line-items` |
| Event/Message | PascalCase with past-tense verb | `OrderLineItemAdded` |
| File/Directory | Project convention | `order_line_item.py`, `OrderLineItem.cs` |

**Key rules:**
- Use the EXACT Identifier — don't abbreviate (`ord`), don't expand (`orderObject`), don't synonym (`purchase`)
- Compound names combine Identifiers: `OrderLineItem`, not `PurchaseLineItem`
- Technical suffixes for infrastructure roles are fine: `OrderRepository`, `OrderDTO` (in infra layer only)
- Multi-word Identifiers keep all words in every casing: `ProcessingStage` → `processing_stage`, never `proc_stage`
- Variables and parameters use full descriptive names: `totalAmount` not `amt`, `customerEmail` not `cEmail`

## Updating the Thesaurus

When changing terms, use the **least strong** relation that tells the truth (from FPF F.13):

| Operation | When | Effect on thesaurus |
|-----------|------|---------------------|
| **Add** | New concept | Index line + entry. Minimum: Identifier, `kind:`, Definition |
| **Rename** | Wording improved, sense unchanged | Change Term/Identifier in the Index line and header; old Identifier → `## Legacy` line `` `Old` → `New` ``; grep codebase, suggest renames |
| **Split** | One term covered two senses | Old line removed; two new lines + entries; old Identifier → `## Legacy` line `` `Old` → `A` + `B` ``; disambiguation in each `NOT` |
| **Merge** | Two terms are really one sense | Keep one line; the other Identifier moves into its `avoid:` list; entries merged |
| **Retire** | Term was misleading, no single successor | `## Legacy` line `` `Old` → — (see `X`, `Y`) `` |
| **Deprecate** | Concept being phased out | `## Legacy` line with `→` replacement and `in:` locations |

**Key test**: Can you point to the **same concept** before and after the change?
- Yes, same concept, better wording → **Rename** (keep as legacy alias for reading old code)
- No, the concept actually changed → **Split** or **Merge** (not a rename)

**Alias parsimony**: keep at most 1 legacy alias per term — the one readers will most
likely encounter in old code. **Registry invariant** still holds after every edit: a name
is under `avoid:` *or* in Legacy, never both.

**Old layout?** No `thesaurus-format` frontmatter key (or `1.x`) means the pre-index prose layout —
see "Migrating an Existing Thesaurus" in
[references/generating-thesaurus.md](references/generating-thesaurus.md).

## Quick Checklist Before Naming Anything

1. Did I grep the thesaurus for this name and its synonyms? Where did the hit land?
2. Would a domain expert recognize this name?
3. Does it contain a weasel word (Manager, Service, Handler, Info, Data, Item, Base, Util)?
4. Is it too generic (could mean multiple things in different contexts)?
5. Does it reveal infrastructure details (Mongo, Sql, Http, Dto, Entity, Model)?
6. Is it consistent with other uses of this term across the codebase?
7. Am I using the EXACT Identifier from the Index, or a synonym from its `avoid:` list?
8. Am I in the right bounded context for this term?
9. Does the name match its Kind — past tense for `event`, imperative for `command`?
10. Can I explain what this name represents in one sentence using domain language?
11. If the concept is new — did I add the Index line **and** the entry before using it?

If any answer raises a concern — stop and fix before proceeding.
