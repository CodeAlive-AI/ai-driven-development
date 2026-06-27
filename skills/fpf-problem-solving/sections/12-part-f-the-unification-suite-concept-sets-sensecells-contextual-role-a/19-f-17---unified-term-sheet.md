## F.17 - Unified Term Sheet
> **Type:** Pattern
> **Status:** Stable

Use this when a term decision must become reader-facing, durable, public, Core-facing, or cross-context. Use it when a role name, status name, relation name, slot name, FPF kind name, local concept name, or bridgeable term set has outgrown one local repair and must be shown as one reviewed term row.

First useful move: identify the governed term decision, not the wording alone. Name the bounded context, the governed FPF kind or governed object kind, the local senses, the bridge claim if cross-context use is present, and the current direct pattern that owns the underlying object. Then publish only the term-row facts that are already governed there.

What goes wrong if missed: a public term sheet becomes a global glossary, a row turns into an ontology claim, a block name becomes a subtype, or a familiar label smuggles role, status, evidence, publication, or source authority into reuse.

What this pattern buys: a compact reader-facing row that preserves the governed object, direct pattern, local senses, bridge, selected names, admissible use, blocked use, and currentness condition without redoing the whole unification argument.

Do not use this pattern for one sentence repair, one private glossary note, one local synonym choice, or one attempt to make an object real by putting it into a table. Use `E.10`, `A.6.P`, `C.2.P`, `F.18`, or the direct domain pattern first when the kind, relation, slot position, admissible use, or name-card decision is still unsettled.

### F.17:1 - Intent and applicability

`UnifiedTermSheet` is a reader-facing term publication for one bounded unification thread. It gives a careful reader one compact table of reviewed term rows: the chosen Tech and Plain names, the specified governed kind or governed value, the local senses, the bridge relation when cross-context use is claimed, and the small rationale that makes the naming decision reviewable.

The pattern is useful when a team has already done enough local sense work that a name can be reused without redoing the whole unification argument each time. It is especially useful for:

- public or cross-context role names;
- status-family names and status-window labels;
- durable relation, slot, interface, or signature names;
- FPF kind names and local concept names that appear in more than one bounded context;
- term rows cited by examples, training material, project standards, or tool interfaces;
- Part G, architecture, transformation, and evaluation vocabulary where row ids must stay stable across editions.

`F.17` does not create `U.Role`, `U.Status`, `U.Evidence`, `U.Method`, `U.Work`, `U.Episteme`, `U.Relation`, `U.SlotKind`, or any other underlying object. It publishes a term row for an already governed object, relation, slot, or local concept. The direct pattern remains responsible for the object and its admissible use.

### F.17:2 - Problem frame

Unification work often succeeds locally and then fails in reuse. A term looks stable in one section, but another reader cannot see which bounded context, local sense, bridge, name-card decision, or direct governing pattern was used. Teams then invent new labels, import a local tradition as if it were universal, or treat a teaching block as if it were an ontology.

The damage is practical:

- local meanings become global slogans;
- one row silently mixes a role, a role description, a status value, a capability claim, and a work assignment;
- public names drift because no row id, edition, or name-card reference stays stable;
- cross-context sameness is asserted by spelling rather than by an `F.9` bridge;
- examples in other patterns cite a term but not the term decision that makes the example portable.

`F.17` fixes this by making the term row itself reviewable. Each row says what kind of thing is being named, where the local senses came from, what bridge is claimed, which name was selected, and which direct pattern owns the underlying object.

### F.17:2.1 - Problem

A public term row can make a local word look reusable while hiding the governed object, bounded context, bridge, direct pattern, admissible use, currentness condition, or blocked overread. The problem is to publish a compact term decision that travels across examples, training material, interfaces, and projects without turning the sheet itself into an ontology or authority source.

### F.17:3 - Forces

| Force | F.17 settlement |
| --- | --- |
| Reader memory vs full provenance | Keep one compact row for use, but require enough references to reopen the sense, bridge, and name decision. |
| Local meaning vs cross-context reuse | Sense cells stay bounded-context local; bridge claims are explicit and governed by `F.9`. |
| Naming neutrality vs recognizability | `F.18` and `F.5` choose names that readers can use without smuggling one context's commitments into the row. |
| Didactic grouping vs ontology | Blocks help memory; blocks do not create subtypes, roles, statuses, or families. |
| Row stability vs edition change | Row ids survive reblocking and wording updates; edition-sensitive fields show what changed. |
| Compact table vs semio-bias | The table is a publication about term decisions; it must not replace the direct pattern that governs the object. |

### F.17:4 - Solution

A Unified Term Sheet is a table of term rows for one bounded unification thread.

Each row has one primary term decision:

```text
UnifiedTermRow:
  UTSRowId
  ThreadContextRef
  GovernedObjectKindOrValueRef
  DirectGoverningPatternRef
  UnifiedTechName
  UnifiedPlainName
  NameCardRef?
  SenseCells[]
  BridgeRefs[]
  RowRationale
  RowEdition
  CurrentnessCondition
  Notes?
```

The row may cite several local senses and several bridges, but it does not fuse their underlying objects. If a source phrase points toward multiple typed FPF values, split the row or cite the direct pattern that keeps the values distinct.

### F.17:5 - Minimal vocabulary

`UnifiedTermSheet` is the whole reader-facing term table for one bounded unification thread.

`UnifiedTermRow` is one row in that sheet. It publishes one reviewed term decision.

`ThreadContextRef` names the bounded context and edition in which the sheet is current.

`GovernedObjectKindOrValueRef` names the specified kind, local concept, relation, slot kind, status family, role, or other governed value being named. Use an admitted durable U-kind, C.3 `U.Kind`, or direct governed value kind only when that is the recovered object. Do not force local concepts, slot kinds, relation kinds, status values, or role assignments into a generic kind container.

`DirectGoverningPatternRef` names the pattern that owns the underlying object or claim. `F.17` owns the term-row publication, not the object.

`SenseCell` is a bounded-context local sense reference. It names the context, edition, local expression, local sense, and source reference when source use is current.

`BridgeRef` cites an `F.9` bridge when one row uses senses from more than one bounded context or when sameness, near-identity, retargeting, or loss matters.

`UnifiedTechName` and `UnifiedPlainName` are the selected names governed by `F.5` and `F.18`. Extra aliases belong in the name-card or local lexicon material, not as rival unified names in the row.

`BlockPlan` is the didactic grouping of rows. A block is a memory and teaching device, not an ontological parent.

### F.17:6 - When to create or update a UTS row

Create or update a UTS row when at least one condition is present:

- the name will be public, Core-facing, or reused across bounded contexts;
- a row id is needed for later examples, checks, dashboards, training material, or tool interface labels;
- a role name, status-family name, slot name, relation name, or local concept name is being reused outside the immediate local repair;
- a bridge claim is being used for cross-context term reuse;
- a name-card decision from `F.18` needs a compact reader-facing term row;
- a direct pattern changes the governed object in a way that changes the name, local sense, bridge, or admissible use.

Do not create a row only because a word was noticed. First recover the kind, relation, slot position, and admissible use under the direct governing pattern.

### F.17:7 - Row schema

Use these columns unless the sheet has a justified specialization.

| Column | Required | Meaning |
| --- | --- | --- |
| `UTSRowId` | yes | Stable row id. It survives row movement between blocks. |
| `Block` | yes | Didactic block name. It has no subtype force. |
| `Governed kind or value` | yes | Exact FPF kind, local concept, relation kind, slot kind, role, status family, characteristic, or other governed value. |
| `Direct pattern` | yes | Pattern that governs the underlying object or claim. |
| `Unified Tech name` | yes | Technical name selected under `F.5` and `F.18`. |
| `Unified Plain name` | yes | Plain-language twin selected under `F.5` and `F.18`. |
| `NameCardRef` | when durable naming is current | Link to the `F.18` name-card decision. |
| `SenseCells` | yes | Local senses by bounded context and edition. |
| `BridgeRefs` | when cross-context use is current | `F.9` bridge ids with congruence level and loss note. |
| `Row rationale` | yes | One sentence explaining why this row is one term decision. |
| `Admissible use` | yes | What this row may be cited for. |
| `Not this use` | yes | The most tempting blocked use or misuse that this row does not permit. |
| `Row edition` | yes | Edition of the row. |
| `Currentness condition` | yes | What direct-pattern or source change requires row review. |
| `Notes` | optional | Short teaching or homonym warning only. |

For `SenseCells`, cite the bounded context and edition. If the source is a publication or source text, cite the source through the source-governing pattern; do not let the source title substitute for the local sense.

### F.17:8 - Block plan

A UTS must declare its block plan. Blocks should be few enough for a careful reader to remember and specific enough to make row search easy.

Example block plan for a role, method, work, and status thread:

- Context and governed values.
- Roles and role descriptions.
- Role assignments and performed work.
- Methods, method descriptions, and work plans.
- Status families and status windows.
- Relation, slot, interface, and bridge terms.
- Evidence, assurance, source, and publication terms when those are the governed values.

This example is not a required ontology. It is a didactic grouping. The sheet may use different blocks when the unification thread is about architecture, transformation flows, evaluation characteristics, Part G search packs, or another area.

### F.17:9 - Layouts

F.17 admits two common layouts.

Layout A, context-first: keep the left rail fixed and add one bounded-context column per selected context. Use this when the reader must compare local senses across named contexts.

```text
UTSRowId | Block | Governed kind or value | Direct pattern
Unified Tech name | Unified Plain name | NameCardRef
Context A, edition | Context B, edition | Context C, edition
BridgeRefs | Row rationale | Admissible use | Not this use
Row edition | Currentness condition | Notes
```

Layout B, comparison-column: keep context and edition inside `SenseCells` and use a smaller set of comparison columns such as tradition, discipline, language, or project family. Use this for teaching when the direct bounded-context cells would be too wide. The comparison columns are presentation aids; they have context authority only when each cell still cites the bounded context and edition.

Never mix a context column and a discipline column as if they had the same kind. A bounded context is a meaning scope; a discipline column is a didactic comparison view.

### F.17:10 - Static conformance rules for a UTS

Use these checks before citing a UTS row outside its local sheet.

| Rule | Check |
| --- | --- |
| UTS-SCR-01 | Every row has row id, block, governed kind or value, direct pattern, Tech name, Plain name, sense cells, row rationale, admissible use, blocked use, row edition, and currentness condition. |
| UTS-SCR-02 | A row names one governed term decision. If the wording hides multiple typed values, split the row or cite the direct pattern that keeps them distinct. |
| UTS-SCR-03 | Every local sense is scoped to bounded context and edition. |
| UTS-SCR-04 | Every cross-context sameness, near-identity, retargeting, or loss claim cites `F.9`. |
| UTS-SCR-05 | The Tech and Plain names satisfy `F.5` and `F.18`; they are not lifted from one local context unless the bridge and rationale justify that choice. |
| UTS-SCR-06 | A role row names `U.Role` or a governed role value; it does not treat RoleDescription, RoleAssignment, capability, method, or work as the same value. |
| UTS-SCR-07 | A status row names the status-family or status-window value governed by `F.10` or `A.19.SPR`; it does not create a role. |
| UTS-SCR-08 | Evidence, assurance, source, publication, and description-use rows cite their direct patterns and do not become generic "evidence roles". |
| UTS-SCR-09 | Blocks remain didactic. No subtype, part-of, role, status, or priority claim follows from block placement. |
| UTS-SCR-10 | The sheet as a whole shows enough context breadth for its claim. If breadth is narrow, the sheet says so. |

### F.17:11 - Regression and stability rules

Recheck only the rows affected by the changed object, name, bridge, or source.

| Rule | Trigger | Required response |
| --- | --- | --- |
| UTS-RSCR-01 | Bounded context edition changes | Keep old sense cells addressable and add or revise cells for the new edition. |
| UTS-RSCR-02 | Direct governing pattern changes the underlying object kind or admissible use | Recheck governed kind or value, direct pattern, admissible use, and blocked use. |
| UTS-RSCR-03 | `F.18` changes the selected name or name-card decision | Recheck Tech name, Plain name, NameCardRef, aliases, and rationale. |
| UTS-RSCR-04 | `F.9` changes bridge kind, congruence level, loss, or direction | Recheck BridgeRefs, row rationale, and cross-context use. |
| UTS-RSCR-05 | Row movement between blocks | Keep row id stable and state that block movement has no ontological force. |
| UTS-RSCR-06 | A role, status, evidence, source, publication, or description row is reused in another context | Recheck the direct governing pattern and the bridge before reuse. |

### F.17:12 - Archetypal Grounding - worked cases

#### F.17:12.1 - Role name becomes public across two project contexts

A project has `ReviewerRole@DesignReview` and `ReviewerRole@ExternalAudit`. The local expressions both say "reviewer", but one concerns a system-in-role performing design review work and the other concerns an assurance actor producing an audit report.

The UTS row does not declare one universal reviewer. It either creates two rows or one row with an explicit `F.9` bridge and loss note. Each row cites the direct role pattern, the RoleDescription when current, and the `F.18` NameCardRef. If evidence or assurance is current, `A.10` or `B.3` governs that separate row or note.

#### F.17:12.2 - Status label looks like a role name

A team proposes `BlockedReviewer` as a public label. F.17 does not accept it as a row until the direct patterns are separated. `Reviewer` is a role value; `blocked` is a status-family value or status-window value. The sheet may publish `Reviewer` as a role row and `Blocked` as a status row, with a note that a local UI may render them together. The table does not create a role called "blocked reviewer".

#### F.17:12.3 - Relation and slot names become reusable

An architecture pattern needs public names for `interfaceSlot`, `providedPort`, and `requiredPort`. The UTS row cites `A.6.5` for slot discipline, `A.6.RSIR` when the relation-signature-interface boundary is current, and `F.18` for durable names. The row does not treat a slot name as a component, role, or capability. If a project context uses `port` differently, the UTS row keeps the local sense and bridge explicit.

#### F.17:12.4 - Misleading evidence-role row

A sheet has a row labelled `Evidence role`. F.17 repairs the row by recovering the governed object instead of treating that label as a U-kind. If the claim is that an episteme is being used as evidence for another claim, `A.10`, `B.3`, or `A.2.4` governs the evidence relation. If the claim is that a system performs evidence-producing work, `A.2.1`, `F.6`, and `A.15.1` govern role assignment and performed work. The UTS may publish names for these values, but it must not keep a generic evidence-role row that fuses them.

### F.17:12.5 - Bias-Annotation

F.17 blocks table-bias: a row does not make the named object real, global, reusable, equivalent, or authoritative. It also blocks label-bias: the public name is a designation for a governed value, relation, slot, or local concept, not a substitute for the direct pattern, bounded-context sense, bridge, admissible-use statement, or currentness condition.

### F.17:13.5 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-F17-1` | The row names the governed kind or value and the direct governing pattern before naming choices are published. |
| `CC-F17-2` | Local senses are bounded-context and edition scoped; cross-context use names the bridge and loss. |
| `CC-F17-3` | Tech and Plain names are selected under naming patterns after the governed value is stable. |
| `CC-F17-4` | Admissible use, blocked use, row edition, and currentness condition are present. |
| `CC-F17-5` | Role, status, evidence, source, publication, description, method, work, relation, slot, interface, and characteristic claims remain under direct patterns. |

### F.17:13 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Global glossary row | Removes bounded-context meaning. | Add context and edition to each sense cell. |
| One row for role and status | Fuses work-capable role with a state-family value. | Split into role row and status row; cite `F.10` or `A.19.SPR` for status. |
| Evidence role bucket | Turns evidence use, source use, assurance, and work into one pseudo-kind. | Recover each claim and cite `A.10`, `B.3`, `E.17`, `E.10.D2`, or role-work patterns. |
| Block as ontology | Treats didactic placement as subtype or part-of claim. | Keep block names as memory aids only. |
| Borrowed context name as Tech name | Imports one tradition's commitments into the unified row. | Use `F.18` and bridge rationale before selecting the unified name. |
| Row without direct pattern | Lets F.17 govern the object instead of the term-row publication. | Add direct pattern or mark the row not ready for public reuse. |

### F.17:14 - Closure conditions

A UTS row is ready for ordinary reuse only when:

- the governed kind or value is explicit;
- the direct pattern is named;
- Tech and Plain names are selected under `F.5` and `F.18`;
- local senses are bounded-context and edition scoped;
- cross-context claims cite `F.9`;
- the row names admissible use and blocked use;
- currentness conditions are stated;
- any role, status, evidence, source, publication, description, method, work, relation, slot, interface, or characteristic claim remains under its direct pattern.

### F.17:14.1 - Consequences

**Benefits.** A UTS row gives readers a stable place to recover a term decision without treating a table as an ontology. It supports public reuse, examples, training material, interface labels, and cross-context comparison while preserving local senses and direct pattern authority.

**Costs.** A tempting public label may wait until local sense, bridge, naming, admissible use, and currentness conditions are settled.

**Failure avoided.** F.17 prevents global glossary drift, row-shaped ontology claims, block-as-subtype mistakes, label-based sameness, and evidence or role authority smuggled through a public term.

### F.17:14.2 - Rationale

Terms travel farther than the reasoning that produced them. F.17 keeps that travel safe by making the term-row publication carry the minimum reopening hooks: governed object, direct pattern, local senses, bridge, names, admitted use, blocked use, and currentness. The row is compact because the direct patterns still own the underlying objects.

### F.17:16 - SoTA-Echoing

| Practice family | What F.17 takes | Practical consequence |
| --- | --- | --- |
| ISO 704:2022 terminology work | A term entry separates object, concept, definition, and designation. | UTS rows keep names separate from the governed object and from source wording. |
| ISO 25964 and W3C SKOS knowledge-organization practice | Concepts, labels, notes, and typed cross-vocabulary mappings are distinct. | F.17 uses `F.9` bridge references for sameness, near-identity, and loss instead of inferring them from spelling. |
| Public naming, controlled-vocabulary, schema, or editioning practice | Public names need stability, editioning, and deprecation discipline. | UTS rows have row ids, row editions, and currentness conditions. |
| Safety and assurance writing | Reader-facing labels must not overclaim authority, evidence, or admissible use. | Each row states admissible use and the tempting misuse it blocks. |

Currentness rule: when `F.5`, `F.8`, `F.9`, `F.10`, `F.15`, `F.18`, `A.2`, `A.2.1`, `A.2.7`, `A.6.5`, `A.10`, `B.3`, `E.17`, or `E.10.D2` changes the governed value, admissible use, bridge, source-use boundary, status-family boundary, role boundary, or naming decision, recheck only the affected UTS rows and examples.

### F.17:15 - Relations

Builds on: `F.1`, `F.2`, `F.3`, `F.5`, `F.7`, `F.8`, `F.9`, `F.15`, and `F.18`.

Coordinates with: `A.2`, `A.2.1`, `A.2.7`, `A.6.5`, `A.6.P`, `A.10`, `A.15.1`, `A.19.SPR`, `B.3`, `C.2.P`, `E.10`, `E.10.D2`, `E.17`, `F.4`, `F.6`, `F.10`, and `F.14`.

Constrains: any public, Core-facing, durable, or cross-context term sheet row that cites FPF vocabulary, local concepts, relation names, slot names, role names, status names, or bridgeable sense clusters.

### F.17:17 - Didactic distillation

A Unified Term Sheet is not the ontology and not the object. It is the table that lets people reuse the naming decision without guessing. Each row says: what kind of thing is named, which direct pattern governs it, which local senses were used, which bridge is claimed, which Tech and Plain names were selected, and what use the row permits.

### F.17:End

