## F.17 - Unified Term Sheet
> **Type:** Lexical publication pattern (F)
> **Status:** Stable

Use this when a term decision is to become reader-facing, durable, public, Core-facing, or cross-context. Use it when a role name, status name, relation name, slot name, FPF kind name, local concept name, or bridgeable term set has outgrown one local repair and publication as one reviewed term row is current.

First useful move: identify the governed term decision, not the wording alone. Name the bounded context, the governed value and its kind, the local senses, the bridge claim if cross-context use is present, and the current direct pattern that owns the underlying value. Then publish only the term-row facts that are already governed there.

Primary EntityOfConcern: one durable reader-facing term decision published by one `UnifiedTermRow` in one bounded unification thread. The role, status value, relation, slot kind, local concept, demonstrated row, or other underlying governed value remains the EntityOfConcern of its direct pattern; F.17 publishes its term decision and does not reconstitute that value.

What goes wrong if missed: a public term sheet becomes a global glossary, a row turns into an ontology claim, a block name becomes a subtype, or a familiar label smuggles role, status, evidence, publication, or source authority into reuse.

What this pattern buys: a compact reader-facing row that preserves the governed object, direct pattern, local senses, bridge, selected names, admissible use, blocked use, and currentness condition without redoing the whole unification argument.

Do not use this pattern for one sentence repair, one private glossary note, one local synonym choice, or one attempt to make an object real by putting it into a table. A short local mantra that only keeps one pattern's Solution in attention remains Plain pattern-local wording and needs no UTS row. Use `E.10`, `A.6.P`, `C.2.P`, `F.18`, or the direct domain pattern first when the kind, relation, slot position, admissible use, or name-card decision is still unsettled.

### F.17:1 - Intent and applicability

`UnifiedTermSheet` is a reader-facing term publication for one bounded unification thread. It gives a careful reader one compact table of reviewed term rows: the chosen Tech and Plain names, the governed value and its kind, the local senses, the bridge relation when cross-context use is claimed, and the small rationale that makes the naming decision reviewable.

The pattern is useful when a team has already done enough local sense work that a name can be reused without redoing the whole unification argument each time. It is especially useful for:

- public or cross-context role names;
- status-family names and status-window labels;
- durable relation, slot, interface, or signature names;
- FPF kind names and local concept names that appear in more than one bounded context;
- term rows cited by examples, training material, project standards, or tool interfaces;
- Part G, architecture, transformation, and evaluation vocabulary whose row ids remain stable across editions.

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
| Reader memory vs full provenance | Keep one compact row for use, with enough references to reopen the sense, bridge, and name decision. |
| Local meaning vs cross-context reuse | Sense cells stay bounded-context local; bridge claims are explicit and governed by `F.9`. |
| Naming neutrality vs recognizability | `F.18` and `F.5` choose names that readers can use without smuggling one context's commitments into the row. |
| Didactic grouping vs ontology | Blocks help memory; blocks do not create subtypes, roles, statuses, or families. |
| Row stability vs edition change | Row ids survive reblocking and wording updates; edition-sensitive fields show what changed. |
| Compact table vs semio-bias | The table publishes term decisions without replacing the direct pattern that governs the object. |

### F.17:4 - Solution

A Unified Term Sheet is a table of term rows for one bounded unification thread.

Publish one term decision through this sequence:

1. Confirm that the direct pattern already governs the underlying value and its admissible use. If the kind, relation, slot position, or use is unsettled, return there before term publication.
2. Decide whether the name now needs durable reader-facing reuse: public publication, cross-context reuse, stable citation, training use, interface use, or editioned maintenance. Otherwise keep the wording local and stop.
3. Recover the bounded local senses and their context editions. Do not infer sameness from spelling.
4. Use F.18 and F.5 to select the Tech and Plain names for the governed value, and cite the resulting NameCard. If no NameCard decision is current, the term is not ready for F.17 publication.
5. When the row relates senses across contexts, cite the exact F.9 bridge, direction, congruence or loss, admitted use, and blocked reverse or stronger use. When no cross-context claim is made, add no bridge.
6. Publish one `UnifiedTermRow` with one governed term decision, direct pattern, selected names, senses, row rationale, admissible and blocked use, edition, and currentness condition. Split unlike governed values into separate rows.
7. Apply the static and regression checks, then stop at term publication. Any later object, evidence, authority, work, or subject-use claim returns to its direct pattern.

Each row has one primary term decision:

```text
UnifiedTermRow:
  UTSRowId
  UnificationThreadId
  Block
  GovernedValueRef: U.EntityRef
  GovernedValueKindRef: U.KindRef
  DirectGoverningPatternRef: U.EntityRef, referencing one U.MethodDescription
  UnifiedTechName
  UnifiedPlainName
  NameCardRef: U.EntityRef, referencing one F.18 NameCard
  SenseCellRefs[]: SenseCellAddressRef, each resolving one F.3 SenseCell(ContextId, Local-SenseId) coordinate
  BridgeRefs[]: U.EntityRef, referencing F.9 Bridges
  RowRationale
  AdmissibleUse
  BlockedUse
  RowEdition
  CurrentnessCondition
  Notes?
```

The row may cite several local senses and several bridges, but it does not fuse their underlying objects. If a source phrase points toward multiple typed FPF values, split the row or cite the direct pattern that keeps the values distinct.

### F.17:5 - Minimal vocabulary

#### F.17:5.1 - Local-sense basis relation

A local sense is not grounded merely because its expression has an accepted name. When a `SenseCell` relies on a public pattern, publication expression, seminar expression, or another episteme, use the following local relation species. It is a relation about support for one bounded local-sense line, not evidence that the governed subject claim is true.

```text
LocalSenseBasisRelation@Context <: U.Relation
SlotSpecs:
  LocalSenseCellSlot:
    ValueKind: F.3 SenseCell coordinate = (U.BoundedContext, Local-Sense); this is a direct governed coordinate value, not a U-kind
    RefKind: SenseCellAddressRef, the F.17-local reference form resolving either SenseCell(ContextId, Local-SenseId) or ContextId:LocalLabel under E.10.D1
    Field: localSenseCellRef
  BasisEpistemeSlot:
    ValueKind: U.Episteme
    RefKind: U.EpistemeRef
    Field: basisEpistemeRef
  BasisEpistemeKindSlot:
    ValueKind: U.Kind
    RefKind: U.KindRef
    Field: basisEpistemeKindRef
    Constraint: resolves to the exact kind of basisEpistemeRef
  BasisPublicationUnitSlot?:
    ValueKind: PublicationUnit under E.17.AUD
    RefKind: PublicationUnitRef
    Field: basisPublicationUnitRef
  BoundedContextSlot:
    ValueKind: U.BoundedContext
    RefKind: U.BoundedContextRef
    Field: boundedContextRef
RelationRefKind: U.EntityRef constrained to LocalSenseBasisRelation@Context
Direction: basisEpistemeRef -> localSenseCellRef
Dependence: the relation depends on the named bounded-context edition, the current basis-episteme edition, and the cited PublicationUnit when present
Identity: <localSenseCellRef, basisEpistemeRef, basis episteme edition, boundedContextRef, basisPublicationUnitRef if present>

LocalSenseBasisRelationDescription@Context <: U.Episteme:
  entityOfConcernRef: U.EntityRef, referencing one LocalSenseBasisRelation@Context
  entityOfConcernKindRef: U.KindRef, referencing LocalSenseBasisRelation@Context
  boundedContextRef: U.BoundedContextRef
  viewpointRef: U.ViewpointRef
  subjectRef: U.SubjectRef, decoding to <entityOfConcernRef, boundedContextRef, viewpointRef>
  groundingHolonRef?: U.HolonRef
  claimGraph: U.ClaimGraph by value, carrying the supported-sense claim, admitted-use claim, and non-admitted-use claim
  referenceScheme: U.ReferenceScheme by value
  editionId
```

`SenseCellAddressRef` addresses the F.3 coordinate without minting a SenseCell U-kind; resolving it yields the exact `(U.BoundedContext, Local-Sense)` pair and context edition. `basisPublicationUnitRef` has RefKind `PublicationUnitRef` and narrows a relied-on pattern or publication to the exact bounded unit when that precision matters. It does not turn a file, slide carrier, or rendering into the supporting episteme.

The relation says only that the named basis episteme, optionally at one publication unit, is the basis for the named SenseCell coordinate in the bounded context. `LocalSenseBasisRelationDescription@Context` says which local-sense claim is supported and which uses are admitted or blocked. Changing only the NameCard reopens the selected expression. Changing the SenseCell address, basis episteme edition, bounded context, or cited publication unit reopens the relation. Changing only the supported-sense claim or use boundary creates a new relation-description edition while preserving the relation when its identity tuple remains unchanged.

`UnifiedTermSheet` is the whole reader-facing term table for one bounded unification thread.

`UnifiedTermRow` is one local F.17 publication-row form in that sheet. It publishes one reviewed term decision and is not a root U-kind or the underlying governed value.

`UnificationThreadId` identifies the bounded naming thread that groups this row with related term decisions. It is a sheet-local identifier, not a `U.BoundedContext`; bounded contexts and their editions remain explicit in `SenseCellRefs`, while `RowEdition` identifies the row edition.

`GovernedValueRef` references the exact value being named. `GovernedValueKindRef` separately references its kind. When the term names a kind token, such as `DemonstrativeUnfoldingSlice@Context`, the governed value is that token and its kind is `U.Kind`; the direct subject pattern states which kinds of instances the token admits. When the term names a role value, relation value, status value, slot kind, or local concept, the two positions reference that value and its exact governed kind. No union field or generic kind container substitutes for this pair.

`DirectGoverningPatternRef` names the pattern that owns the underlying value or claim. `F.17` owns the term-row publication, not that value.

`SenseCell` is a bounded-context local sense coordinate from `F.3`. It names the context, edition, local expression, and local sense. `SenseCellAddressRef` is the F.17-local RefKind for that coordinate; it does not mint a SenseCell U-kind. A `NameCardRef` may accompany the cell when its local expression relies on an `F.18` naming settlement. A separate `LocalSenseBasisRelationRef` relates the SenseCell coordinate to the episteme that supports it; the relation description carries the supported-sense and use-boundary claims, and the NameCard fills neither position.

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

| Column | Presence condition | Meaning |
| --- | --- | --- |
| `UTSRowId` | yes | Stable row id. It survives relocation of the row between blocks. |
| `Unification thread` | yes | Sheet-local identifier of the bounded naming thread; it does not replace any SenseCell bounded context. |
| `Block` | yes | Didactic block name. It has no subtype force. |
| `Governed value` | yes | Exact value being named, including a kind token when the name is for that token. |
| `Governed value kind` | yes | Exact kind of the governed value; use `U.Kind` when the governed value is itself a kind token. |
| `Direct pattern` | yes | Pattern that governs the underlying object or claim. |
| `Unified Tech name` | yes | Technical name selected under `F.5` and `F.18`. |
| `Unified Plain name` | yes | Plain-language twin selected under `F.5` and `F.18`. |
| `NameCardRef` | yes | Link to the `F.18` NameCard that selected or documented the published names. |
| `SenseCellRefs` | yes | References to local senses by bounded context and edition. |
| `BridgeRefs` | when cross-context use is current | `F.9` bridge ids with congruence level and loss note. |
| `Row rationale` | yes | One sentence explaining why this row is one term decision. |
| `Admissible use` | yes | What this row may be cited for. |
| `Not this use` | yes | The most tempting blocked use or misuse that this row does not permit. |
| `Row edition` | yes | Edition of the row. |
| `Currentness condition` | yes | Which direct-pattern or source change opens row review. |
| `Notes` | optional | Short teaching or homonym warning only. |

For `SenseCellRefs`, cite the bounded context and edition. If the local expression relies on a naming settlement, cite its `NameCardRef`. If the local sense relies on a publication or another episteme, cite a `LocalSenseBasisRelation@Context` with an exact `U.EpistemeRef` and, when needed, the exact publication-unit ref. Do not let a source title, file name, or NameCard substitute for the local sense or its basis relation.

### F.17:8 - Block plan

A UTS is complete only with a declared block plan. Blocks stay few enough for a careful reader to remember and specific enough to make row search easy.

Example block plan for a role, method, work, and status thread:

- Context and governed values.
- Roles and role descriptions.
- Role assignments and performed work.
- Methods, method descriptions, and work plans.
- Status families and status windows.
- Relation, slot, interface, and bridge terms.
- Evidence, assurance, source, and publication terms when those are the governed values.

This example does not define an ontology. It is a didactic grouping. The sheet may use different blocks when the unification thread is about architecture, transformation flows, evaluation characteristics, Part G search packs, or another area.

### F.17:9 - Layouts

F.17 admits two common layouts.

Layout A, context-first: keep the left rail fixed and add one bounded-context column per selected context. Use this when the reader's current comparison concerns local senses across named contexts.

```text
UTSRowId | Unification thread | Block | Governed value | Governed value kind | Direct pattern
Unified Tech name | Unified Plain name | NameCardRef
Context A, edition | Context B, edition | Context C, edition
BridgeRefs | Row rationale | Admissible use | Not this use
Row edition | Currentness condition | Notes
```

Layout B, comparison-column: keep context and edition inside `SenseCellRefs` and use a smaller set of comparison columns such as tradition, discipline, language, or project family. Use this for teaching when the direct bounded-context cells would be too wide. The comparison columns are presentation aids; they have context authority only when each cell still cites the bounded context and edition.

Never mix a context column and a discipline column as if they had the same kind. A bounded context is a meaning scope; a discipline column is a didactic comparison view.

### F.17:10 - Static conformance rules for a UTS

Use these checks before citing a UTS row outside its local sheet.

| Rule | Check |
| --- | --- |
| UTS-SCR-01 | Every row has row id, unification-thread id, block, governed value, governed value kind, direct pattern, Tech name, Plain name, sense-cell refs, row rationale, admissible use, blocked use, row edition, and currentness condition. |
| UTS-SCR-02 | A row names one governed term decision. If the wording hides multiple typed values, split the row or cite the direct pattern that keeps them distinct. |
| UTS-SCR-03 | Every local sense is scoped to bounded context and edition. |
| UTS-SCR-04 | Every cross-context sameness, near-identity, retargeting, or loss claim cites `F.9`. |
| UTS-SCR-05 | The Tech and Plain names satisfy `F.5` and `F.18`; they are not lifted from one local context unless the bridge and rationale justify that choice. |
| UTS-SCR-06 | A role row names `U.Role` or a governed role value; it does not treat RoleDescription, RoleAssignment, capability, method, or work as the same value. |
| UTS-SCR-07 | A status row names the status-family or status-window value governed by `F.10` or `A.19.SPR`; it does not create a role. |
| UTS-SCR-08 | Evidence, assurance, source, publication, and description-use rows cite their direct patterns and do not become generic "evidence roles". |
| UTS-SCR-09 | Blocks remain didactic. No subtype, part-of, role, status, or priority claim follows from block placement. |
| UTS-SCR-10 | The sheet as a whole shows enough context breadth for its claim. If breadth is narrow, the sheet says so. |

Passing the row schema is not the value criterion. A row succeeds only when its intended readers can recover the correct governed value and direct pattern for the declared use and avoid the blocked use. Row count, filled-cell count, label uniformity, block neatness, and stable identifiers are maintenance aids, not evidence that the term decision is useful or semantically adequate.

### F.17:11 - Regression and stability rules

Recheck only the rows affected by the changed object, name, bridge, or source.

| Rule | Trigger | Response when triggered |
| --- | --- | --- |
| UTS-RSCR-01 | Bounded context edition changes | Keep old sense cells addressable and add or revise cells for the new edition. |
| UTS-RSCR-02 | Direct governing pattern changes the underlying value kind or admissible use | Recheck governed value, governed value kind, direct pattern, admissible use, and blocked use. |
| UTS-RSCR-03 | `F.18` changes the selected name or name-card decision | Recheck Tech name, Plain name, NameCardRef, aliases, and rationale. |
| UTS-RSCR-04 | `F.9` changes bridge kind, congruence level, loss, or direction | Recheck BridgeRefs, row rationale, and cross-context use. |
| UTS-RSCR-05 | Row relocation between blocks | Keep the row id stable and state that relocation between blocks has no ontological force. |
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

A sheet has a row labelled `Evidence role`. F.17 repairs the row by recovering the governed object instead of treating that label as a U-kind. If the claim is that an episteme is being used as evidence for another claim, `A.10`, `B.3`, or `A.2.4` governs the evidence relation. If the claim is that a system performs evidence-producing work, `A.2.1`, `F.6`, and `A.15.1` govern role assignment and performed work. The UTS may publish names for these values; a generic evidence-role row that fuses them is not admitted.

#### F.17:12.4a - Manufacturing batch across material and planning contexts

A furnace team uses `batch` for one physically handled set of shafts that shares a heat-treatment run and traceability basis. A planning dashboard uses `batch` for a grouping of intended PlanItems. Spelling does not make these one governed value. Recover the physical batch under the direct material or production DPF pattern, including its identity and part-whole treatment when current; recover the planning grouping under A.15.2 and its direct planning relation. Publish separate rows unless an F.9 Bridge states a narrower comparison or traceability relation with direction and loss. A `batch` row cannot turn a PlanItem grouping into a physical holon or make the physical batch a WorkPlan.

#### F.17:12.4b - Clinical discharge wording

A clinical publication proposes one row for `discharge` and `discharge-ready`. First separate the governed values. A patient-state classification uses A.19.SPR plus the clinical DPF pattern for its bearer, state frame, evidence, qualification window, and use. An accountable discharge decision remains a decision relation under its direct pattern. A completed discharge is dated Work under A.15.1. Publish distinct rows and connect them only through relations actually governed in the clinical context. One familiar label does not make state, decision, and Work interchangeable.

#### F.17:12.4c - Demonstrative walkthrough, mantra, and mantra move

These rows publish naming decisions already governed and named in A.22.CGUS. They cover only the CGUS-demonstrative use of `mantra` and `mantra move`; they do not define the broader Plain practice of giving one pattern a short repeatable local mantra. F.17 publishes the bounded terms; it does not govern the demonstrated structures, rows, or pattern-local formulas.

```text
UTSRowId: UTS.DemonstrativeUnfoldingSlice.FPFPublic
UnificationThreadId: DemonstrativeExplanationTerminology.2026-07-11
Block: Pattern use and teaching
GovernedValueRef: DemonstrativeUnfoldingSlice@Context
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: A.22.CGUS
UnifiedTechName: DemonstrativeUnfoldingSlice@Context
UnifiedPlainName: demonstrative walkthrough
NameCardRef: NameCard.DemonstrativeUnfoldingSlice.FPFPublic
SenseCellRefs: SenseCell.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11
BridgeRefs: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11, CL=2, CellB-to-CellA only
RowRationale: this row names one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure for a cold public reader
AdmissibleUse: public naming of the governed demonstrative episteme
BlockedUse: actual traversal, method order, work order, performed work, or teaching-medium identity
RowEdition: 2026-07-11
CurrentnessCondition: review when the governed value, public bounded context, NameCard, local-sense basis relation, bridge loss, or reader evidence changes

UTSRowId: UTS.DemonstrativeUnfoldingSlice.SeminarTeaching
UnificationThreadId: DemonstrativeExplanationTerminology.2026-07-11
Block: Pattern use and teaching
GovernedValueRef: DemonstrativeUnfoldingSlice@Context
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: A.22.CGUS
UnifiedTechName: DemonstrativeUnfoldingSlice@Context
UnifiedPlainName: mantra
NameCardRef: NameCard.DemonstrativeUnfoldingSlice.SeminarTeaching
SenseCellRefs: SenseCell.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11
BridgeRefs: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11, CL=2, CellB-to-CellA only
RowRationale: the bounded teaching alias adds repeated speech and attentional use while naming the same governed demonstrative episteme
AdmissibleUse: repeated English-language FPF seminar speech that helps participants hold the demonstrated solution structure in attention
BlockedUse: ritual authority, slogan, method, plan, work, fixed order, or reverse substitution from every public walkthrough
RowEdition: 2026-07-11
CurrentnessCondition: review when the seminar context, governed value, NameCard, local-sense basis relation, bridge loss, dictionary evidence, or reader evidence changes

UTSRowId: UTS.DemonstratedPatternUseRow.SeminarTeaching
UnificationThreadId: DemonstrativeExplanationTerminology.2026-07-11
Block: Pattern use and teaching
GovernedValueRef: DemonstratedPatternUseRow@Context
GovernedValueKindRef: U.Kind
DirectGoverningPatternRef: A.22.CGUS
UnifiedTechName: DemonstratedPatternUseRow@Context
UnifiedPlainName: mantra move
NameCardRef: NameCard.DemonstratedPatternUseRow.SeminarTeaching
SenseCellRefs: SenseCell.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11
BridgeRefs: none; expression and governed-row use are local to the same bounded seminar context
RowRationale: this row names one shown conditional pattern use with its Solution, expected result, and current condition inside a mantra
AdmissibleUse: bounded seminar reference to one demonstrated result-bearing continuation
BlockedUse: root Move, physical movement, operation, fixed serial step, PlanItem, performed Work, or continuation detached from its slice
RowEdition: 2026-07-11
CurrentnessCondition: review when the demonstrated-row schema, NameCard, local-sense basis relation, seminar context, or reader interpretation changes
```

The two senses of the same demonstrative value remain distinct:

```text
SenseCell.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  Context: FPF English public publication, edition 2026-07-11
  LocalExpression: demonstrative walkthrough
  LocalSense: one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure
  senseFamily: DemonstrativeExplanation
  NameCardRef: NameCard.DemonstrativeUnfoldingSlice.FPFPublic
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11

SenseCell.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  Context: English-language FPF seminar teaching, edition 2026-07-11
  LocalExpression: mantra
  LocalSense: a short repeatable explanatory walkthrough used to hold the whole solution structure in attention
  senseFamily: DemonstrativeExplanation
  NameCardRef: NameCard.DemonstrativeUnfoldingSlice.SeminarTeaching
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11

SenseCell.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11:
  Context: English-language FPF seminar teaching, edition 2026-07-11
  LocalExpression: mantra move
  LocalSense: one shown pattern-use continuation with its Solution, expected result, and current condition inside a mantra
  senseFamily: DemonstratedPatternUseContinuation
  NameCardRef: NameCard.DemonstratedPatternUseRow.SeminarTeaching
  LocalSenseBasisRelationRefs: LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11

LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  localSenseCellRef: SenseCell(FPF-English-Public-2026-07-11, DemonstrativeUnfoldingSlice-public)
  basisEpistemeRef: A.22.CGUS
  basisEpistemeKindRef: U.MethodDescription
  basisPublicationUnitRef: A.22.CGUS:4.3.3-Ordinary-bounded-use
  boundedContextRef: FPF English public publication, edition 2026-07-11

LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
  boundedContextRef: FPF English public publication, edition 2026-07-11
  viewpointRef: FPFPublicReaderViewpoint
  subjectRef: <LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11, FPF English public publication 2026-07-11, FPFPublicReaderViewpoint>
  claimGraph:
    supportedSenseClaim: one readable demonstration of admissible continuations through a wider constraint-governed unfolding structure
    admittedUseClaim: support the public local-sense line for this SenseCell
    nonAdmittedUseClaim: no evidence, authority, work-order, or naming decision follows from this relation
  referenceScheme: F.3 SenseCell and F.17 local-sense-basis interpretation
  editionId: 2026-07-11

LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  localSenseCellRef: SenseCell(FPF-Seminar-Teaching-2026-07-11, DemonstrativeUnfoldingSlice-mantra)
  basisEpistemeRef: SeminarExpression.FPFPracticalUse.2026-07-11
  basisEpistemeKindRef: U.EpistemePublication
  basisPublicationUnitRef: SeminarExpression.FPFPracticalUse.2026-07-11.Slides8-10
  boundedContextRef: English-language FPF seminar teaching, edition 2026-07-11

LocalSenseBasisRelationDescription.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
  boundedContextRef: English-language FPF seminar teaching, edition 2026-07-11
  viewpointRef: FPF Seminar Participant Viewpoint
  subjectRef: <LocalSenseBasisRelation.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11, English-language FPF seminar teaching 2026-07-11, FPF Seminar Participant Viewpoint>
  claimGraph:
    supportedSenseClaim: a short repeatable explanatory walkthrough used to hold the whole solution structure in attention
    admittedUseClaim: support the bounded teaching sense from the seminar expression
    nonAdmittedUseClaim: the slide carrier does not become the sense, naming settlement, method, plan, or work
  referenceScheme: F.3 SenseCell and F.17 local-sense-basis interpretation
  editionId: 2026-07-11

LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11:
  localSenseCellRef: SenseCell(FPF-Seminar-Teaching-2026-07-11, DemonstratedPatternUseRow-mantra-move)
  basisEpistemeRef: SeminarExpression.FPFPracticalUse.2026-07-11
  basisEpistemeKindRef: U.EpistemePublication
  basisPublicationUnitRef: SeminarExpression.FPFPracticalUse.2026-07-11.Slides61-62
  boundedContextRef: English-language FPF seminar teaching, edition 2026-07-11

LocalSenseBasisRelationDescription.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11:
  entityOfConcernRef: LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11
  entityOfConcernKindRef: LocalSenseBasisRelation@Context
  boundedContextRef: English-language FPF seminar teaching, edition 2026-07-11
  viewpointRef: FPF Seminar Participant Viewpoint
  subjectRef: <LocalSenseBasisRelation.DemonstratedPatternUseRow.SeminarTeaching.2026-07-11, English-language FPF seminar teaching 2026-07-11, FPF Seminar Participant Viewpoint>
  claimGraph:
    supportedSenseClaim: one shown pattern-use continuation with its Solution, expected result, and current condition inside a mantra
    admittedUseClaim: support the bounded teaching sense of mantra move
    nonAdmittedUseClaim: the slide carrier does not become the row, pattern use, plan, or performed work
  referenceScheme: F.3 SenseCell and F.17 local-sense-basis interpretation
  editionId: 2026-07-11
```

`SeminarExpression.FPFPracticalUse.2026-07-11` names the published seminar content as a `U.EpistemePublication`; the `.pptx` and extracted Markdown are separate carriers or renderings. The public relation instead relies on the current `A.22.CGUS` pattern episteme and narrows that reliance to the ordinary-use publication unit.
The cross-context relation is complete by value. `DemonstrativeExplanation` is an F.9 local `senseFamily` label, not a U-kind.

```text
BridgeCardId: Bridge.DemonstrativeUnfoldingSlice.SeminarTeaching-To-FPFPublic.2026-07-11
BridgeCard:
  CellA: SenseCell.DemonstrativeUnfoldingSlice.FPFPublic.2026-07-11
  CellB: SenseCell.DemonstrativeUnfoldingSlice.SeminarTeaching.2026-07-11
  senseFamilyA: DemonstrativeExplanation
  senseFamilyB: DemonstrativeExplanation
  BridgeKind: Narrower-than
  Direction: CellB is narrower than CellA; only CellB-to-CellA use is admitted
  CL: 2
  LossNotes: the broader public sense does not include repeated speech, remembered replay, or the seminar attentional function
  CounterExampleOrInvariantEvidence: a public demonstrative walkthrough may be read once and understood without being repeated or used as a mnemonic
  AdmittedUse: naming-only; a seminar use of mantra may point to the public demonstrative-walkthrough term and its governed value
  NonAdmittedUse: no CellA-to-CellB substitution; no claim that every public walkthrough is a mantra; no inference of method, plan, order, authority, work, or teaching-medium identity
  DirectGoverningPatternIfNotF9: none; F.9 governs this substitution Bridge
  RevisionTrigger: either bounded-context edition changes, reader tests change the observed loss, or the selected local label or governed value changes
```

The bridge is directional because the seminar sense adds repetition and attentional use. Shared reference to one governed value does not erase that sense difference. `CL=2` is admitted only with the explicit counterexample; it does not admit reverse substitution or structural inference.

The seminar deck and its textual extraction establish the teaching problem and observed concept use. They do not establish English lexical admissibility by themselves. Current English dictionary evidence supports the repeated-formula and watchword senses of `mantra`, while its Sanskrit analysis as an instrument of thought supplies the attentional rationale. F.18 and reader-use evidence decide whether that English candidate fits this bounded FPF context. This row does not claim that every local pattern mantra is a `DemonstrativeUnfoldingSlice@Context`; a pattern-local formula is interpreted from that pattern's Solution unless a stronger governed value is claimed. This row makes no cross-language sameness claim; a term published in another language needs its own bounded NameCard, evidence, and F.17 sense relation.

No F.17 row is published for `working product`. The phrase has no single governed value across physical entities, changed states, capabilities, relations, and epistemes. Technical text uses the exact subject-governed result name; ordinary explanation may say `result produced by work`, or `first useful result` when firstness and receiving-use value have been established.

### F.17:12.5 - Bias-Annotation


F.17 blocks table-bias: a row does not make the named object real, global, reusable, equivalent, or authoritative. It also blocks label-bias: the public name is a designation for a governed value, relation, slot, or local concept, not a substitute for the direct pattern, bounded-context sense, bridge, admissible-use statement, or currentness condition.

### F.17:13.5 - Conformance Checklist

| Check | Passing condition |
| --- | --- |
| `CC-F17-1` | The row names the governed value, its exact kind, and the direct governing pattern before naming choices are published. |
| `CC-F17-2` | Local senses are bounded-context and edition scoped; cross-context use names the bridge and loss. |
| `CC-F17-3` | Tech and Plain names are selected under naming patterns after the governed value is stable. |
| `CC-F17-4` | Admissible use, blocked use, row edition, and currentness condition are present. |
| `CC-F17-5` | Role, status, evidence, source, publication, description, method, work, relation, slot, interface, and characteristic claims remain under direct patterns. |
| `CC-F17-6` | A SenseCell uses `NameCardRef` only for its naming settlement and separately cites every relied-on local-sense basis through `LocalSenseBasisRelation@Context` with exact value-kind and ref-kind pairs. |

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

- the governed value and its exact kind are explicit;
- the direct pattern is named;
- Tech and Plain names are selected under `F.5` and `F.18`;
- local senses are bounded-context and edition scoped;
- each relied-on local-sense basis is separate from its naming settlement and is cited through `LocalSenseBasisRelation@Context`;
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

| Current source and status | Adopted or adapted move | Effect in F.17 | Limitation and reopen condition |
| --- | --- | --- | --- |
| Current FPF naming and unification set dated 2026-07-11: `F.18`, `F.9`, `F.15`, `F.10`, `E.10`, and the direct subject patterns | Start from a governed value and kind; select names through a NameCard; use directional Bridges with loss for cross-context reuse; keep static and regression checks local; separate status and role claims; return stronger use to the direct pattern. | Determines the seven-step Solution, mandatory NameCardRef, value-kind pair, SenseCellRefs, BridgeRefs, admitted and blocked use, stable row id, local regressions, and direct-pattern boundary. | This is the current governing basis, not external proof that a proposed row works for readers. Reopen the affected row when one of these patterns changes its kind settlement, naming decision, Bridge use, status boundary, or regression rule. |
| Zhu, Reinecke, and Mitra, ["Language Scent: Exploring Cross-Language Information Navigation"](https://arxiv.org/abs/2604.03604), arXiv:2604.03604, 2026 preprint | Treat recognizability of a label as context-sensitive navigation support rather than evidence of cross-context equivalence. Preserve in-situ cues while keeping their governed value and sense boundary recoverable. | Changes the local-sense, reader-use, and blocked-substitution checks for Plain names such as `mantra`; supports contextual labels and explicit F.9 Bridges rather than one global label. | The study is small and cross-language. It neither establishes FPF ontology nor proves one label works in every context. Reopen when stronger reader evidence changes the observed cue value or loss. |
| W3C, [*SKOS Simple Knowledge Organization System Reference*](https://www.w3.org/TR/skos-reference/), W3C Recommendation 2009, current stable reference accessed 2026-07-11 | Keep concepts, lexical labels, documentation notes, collections, and typed mapping relations distinct; do not infer transitivity or equivalence from a generic related or matching label. | Supplies a stable external reference for separating labels, notes, collections, and mappings. F.17 strengthens it with direct FPF value kinds, F.9 direction and loss, NameCards, admissible and blocked use, and row currentness. | SKOS is a stable web vocabulary model, not current best-known FPF authoring methodology and not a source of FPF kinds. Reopen this adaptation if W3C supersedes the Recommendation or a newer mapping practice changes the selected distinction. |

The current best problem-solving line for F.17 is the current FPF naming, bridge, status, and regression architecture. The 2026 language-scent study changes contextual cue handling subject to its evidence limits. SKOS remains a stable reference model for label and mapping separation; its age and stability do not make it the method that governs FPF term decisions.

Currentness rule: when `F.5`, `F.8`, `F.9`, `F.10`, `F.15`, `F.18`, `A.2`, `A.2.1`, `A.2.7`, `A.6.5`, `A.10`, `B.3`, `E.17`, or `E.10.D2` changes the governed value, admissible use, bridge, source-use boundary, status-family boundary, role boundary, or naming decision, recheck only the affected UTS rows and examples.

### F.17:15 - Relations

Builds on: `F.1`, `F.2`, `F.3`, `F.5`, `F.7`, `F.8`, `F.9`, `F.15`, and `F.18`.

Coordinates with: `A.2`, `A.2.1`, `A.2.7`, `A.6.5`, `A.6.P`, `A.10`, `A.15.1`, `A.19.SPR`, `B.3`, `C.2.P`, `E.10`, `E.10.D2`, `E.17`, `F.4`, `F.6`, `F.10`, `F.14`, and `G.11`. Row-local review after a changed value, name, sense, Bridge, or edition remains with the direct pattern, F.18, F.9, F.15, and these F.17 regression rules. Use G.11 only when an actual refresh plan, edition orchestration, telemetry, freshness, or decay claim is current.

Constrains: any public, Core-facing, durable, or cross-context term sheet row that cites FPF vocabulary, local concepts, relation names, slot names, role names, status names, or bridgeable sense clusters.

### F.17:17 - Didactic distillation

A Unified Term Sheet is not the ontology and not the object. It is the table that lets people reuse the naming decision without guessing. Each row says: what kind of thing is named, which direct pattern governs it, which local senses were used, which bridge is claimed, which Tech and Plain names were selected, and what use the row permits.

### F.17:End

