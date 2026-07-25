## F.18 - Local-First Unification Naming Protocol
> **Status:** Stable
*Pattern state: stable pattern. Audience: engineer-managers, lead architects, ontology editors, and authors who must make one name reusable without turning that name into a hidden ontology.*

### F.18:0 - Use This When

Use `F.18` when a name must become stable, public, Core-facing, reusable across contexts, or durable enough that later work can cite it without guessing. Typical cases:

- a local expression becomes a durable name for a role, relation, slot, method, work, characteristic, status value, architecture element, or other already governed value;
- two teams use different words for the same candidate sense and need one reusable term plus preserved local wording;
- one tempting head word is useful in one context but misleading in another;
- a role-derived, method-derived, status-like, evidence-like, interface-like, or slot-like name risks creating a second ontology by wording alone.

First useful move: recover the exact governed object or governed value before choosing the name. When relation-facing wording is current, distinguish a predicate-definition episteme, an admitted relation kind, an obtaining relation occurrence, a representation element, and a designator or reference; for a residual relation claim, cite the `A.6.RCD` settlement before naming. Other candidates—such as a role, method, work, characteristic, status value, architecture element, or claim-bearing episteme—stay under their direct owners rather than being forced into that relation-facing list. Then ask: under which effective by-value `U.ReferenceScheme`, by which governing pattern, for which use, and with which exact local sense is this object named? Only then decide whether a local expression is enough or a `NameCard` is needed. A public row is a later step: create one only when public, Core-facing, durable-across-context, or cross-context reuse is current and the `F.17` entry/result gate in section 4 passes.

Do not use `F.18` for one-off wording repair. If the phrase is local and not becoming a reusable name, use `E.10`, `E.10.ARCH`, `A.6.P`, `A.6.RSIR`, `C.2.P`, or the governing pattern for the object being named.

### F.18:1 - Context

Names are handles for use, not creators of ontology. A good name lets people talk about a governed value without smuggling in extra role, capability, method, work, status, evidence, interface, or cross-context claims.

`FPFCoreReferenceScheme` is the by-value `U.ReferenceScheme` used to interpret current FPF Core Tech labels and relation names. A NameCard that uses it carries that reference-scheme value by value, consistent with `C.2.1`; F.18 does not introduce `U.ReferenceSchemeRef`. A name interpreted under another reference scheme carries that scheme by value. When a naming use must align two local senses, first identify each sense under its by-value reference scheme; name a `BoundedModelUseStructure` only when that selected structure changes the sense or the admitted use. Use `F.9` only if its current entry can take those two senses as endpoints and its result states the naming use that survives. Until then, keep the names local or record the unresolved alignment. A reference-scheme or model-use-structure difference alone supplies neither a Bridge nor governed-value identity, and it does not create `U.BoundedContext`.

`F.18` supplies the naming discipline for Part F and for any FPF pattern that needs a durable public term. It coordinates with:

- `F.5` for type-name and role-description label form;
- `F.8` for the prior decision that an expression should become a durable name rather than remain local, reused, or aliased;
- `F.9` for an actual cross-context sense Bridge;
- `F.13` for renames, aliases, splits, and merges;
- `F.14` for anti-explosion control;
- `F.17` only as a later public-row consumer whose current entry and result must accept the exact F.18 objects named below;
- `A.6.5` and `A.6.RSIR` when relation, signature, interface, slot, or role wording hides the governed object; `A.6.P.WMR` when work/method-boundary wording still hides the exact relation; and `A.15.1` when a candidate performed-work name still lacks occurrence grounding.

The central subject is one `F.18` naming settlement for one exact already-governed value. `F.18` governs the candidate comparison, selected Tech and Plain designations, declared naming use, and reopen conditions. The value's direct pattern still governs its kind, identity, obtaining, and other subject semantics.

Its complete claim graph records the selected designation expressions, exact local sense, covered and rejected alternatives, rationale, lineage, and reopen condition.

### F.18:2 - Problem

FPF texts fail when names are treated as if they carried ontology by themselves.

1. A short label appears in another context and gets treated as the same value, although no bridge says what survives.
2. A role-looking name quietly bundles role value, holder assignment, capability, method fit, work evidence, or authorization.
3. A status-like or evidence-like phrase becomes a fake role or fake type because the row says "evidence role", "status role", or similar wording.
4. A relation, declaration-local slot, interface, port, or signature name hides the exact governed object, relation-participant meaning, or direct pattern that should own the claim.
5. A term chosen for convenience becomes a permanent Core-facing name without candidate comparison, rejected alternatives, or lineage.
6. Local names proliferate until the corpus has several almost-synonyms and no recoverable reason for choosing one.

The repair is not to choose prettier words. Recover the governed value, then record a naming settlement whose kind, effective reference scheme, exact local sense, intended use, and selected designations remain visible. Publication is a separate later relation.

### F.18:3 - Forces

| Force | Naming tension |
| --- | --- |
| Local sense and cross-scheme reuse | A name must be interpretable under one effective by-value `U.ReferenceScheme` while remaining bridgeable under another without spelling-based identity. |
| Brevity and ontology recovery | A short label helps conversation, but the `NameCard` must keep governed kind, effective reference scheme, local sense, governing pattern, and intended use recoverable. |
| Continuity and correction | Readers need stable public names, while authors must be able to rename, split, merge, or retire names without erasing earlier uses. |
| Familiarity and precision | Familiar words are easier to adopt, but some familiar words import wrong prototypes from another discipline. |
| Role recognition and role explosion | Role morphology is useful for `U.Role` values, but it must not absorb holder assignment, capability, method, work, evidence, or status claims. |

### F.18:4 - Solution

Use a local-first naming protocol:

1. Recover the governed value, its kind, and its direct governing pattern.
2. Decide whether the expression should remain local or the current use needs a durable reusable name; apply `F.14` before adding a card, cell, or row.
3. For a durable name, constitute one `NameCard` episteme under `C.2.1`; keep the value, its kind, the card, selected designations, exact local sense, and any basis or Bridge relation distinct.
4. Choose the Tech and Plain labels from the smallest candidate set that covers the live head-term families and plausible neighbouring objects.
5. Record the covered alternatives, rejected candidates, selection reason, lineage, and the smallest condition that reopens the settlement.
6. Only for public, Core-facing, durable-across-context, or cross-context reuse, test whether the then-current `F.17` entry accepts the exact governed value and kind, NameCard episteme, by-value scheme, local sense, and any actual Bridge, and whether its result supplies the required public row. If either test fails, retain the durable name and NameCard locally, mark the public row pending, and stop.
7. Keep Bridge, publication, currentness, status, evidence, slot, role, method, work, and interface claims in their own governing patterns.

#### F.18:4.1 - Naming Invariants

Every durable name must satisfy these invariants.

| Invariant | Required content |
| --- | --- |
| Governed value first | Name the governed value or value family before naming the label. |
| Governing pattern visible | Cite the pattern that owns the value: for example `A.2` for role value, `A.2.1` for role assignment, `A.6.5` for relation slot discipline, `F.10` or `A.19.SPR` for status value use, `A.10` for evidence use. |
| Reference scheme visible | The NameCard carries the effective `U.ReferenceScheme` by value; a model-use structure, claim scope, project work, or other locality relation remains separate and appears only when the naming use needs it. |
| Local sense visible | Every card states one exact local-sense claim under the effective scheme. A progressive-minimum card may state it directly as `LocalSenseRef`; an expanded card uses `LocalSenseCellRef` when a separately recoverable `SenseCell` is current. Any basis episteme and local-sense basis relation remain separate. |
| Two labels when reusable | The Tech label is precise; the Plain label helps ordinary readers. Both point to the same governed value. |
| Candidate comparison visible | At least two plausible head families are considered unless a cited external standard fixes the label. |
| Bridge only for cross-context sense alignment | A spelling match, shared reference scheme, or `F.9` Bridge does not establish governed-value identity; F.9 states only its exact sense correspondence and admitted use. |
| Lineage visible | Rename, split, merge, retirement, and alias decisions are recorded. |

#### F.18:4.2 - `NameCard` Fields

A NameCard is complete when its exact C.2.1 identity-bearing `U.ClaimGraph` is recoverable; completeness is not a field count. The accepted D11 cards `NC-U-RELATION`, `NC-BOUNDED-MODEL-USE-STRUCTURE`, `NC-CROSS-CONTEXT-RELATION-STRUCTURE`, `NC-PROBLEM-CRITERION-APPLICABILITY-RELATION`, and `NC-PROBLEMATIC-FOR-RELATION` remain conforming progressive-minimum cards. Each already states the governed value and direct owner, effective scheme and local-sense claim, one selected Tech/Plain pair, candidate set, rejections, rationale, lineage, and reopen condition. Its direct owner makes the governed kind unambiguous. These filled claims together constitute the card's complete claim graph; an omitted expanded field contributes no hidden claim.

Use the expanded form only when the current naming use needs the additional position:

```text
NameCard:
  NameCardId:
  GovernedValueRef:
  GovernedValueKindRef: [add when the kind is not unambiguous from the value and direct owner, or a consumer needs the exact kind reference]
  GoverningPatternRef:
  ReferenceScheme:
  ClaimContent: [reference to the complete U.ClaimGraph constituted by all identity-bearing naming-settlement claims]
  LocalSenseCellRef: [add when a separately recoverable SenseCell is current; otherwise LocalSenseRef carries the direct local-sense claim]
  LocalSenseBasisRelationRef: [add only for an actual separately governed basis relation]
  TechLabel:
  PlainLabel:
  CandidateSet:
  CandidateCoverage: [add when family coverage, an open alternative, or a forced exception must be explicit]
  RejectedCandidates:
  SelectionRationale:
  BridgeRefs: [add only for actual F.9 Bridge occurrences admitted for this use]
  PublicRowStatus: [add when public-row use is current]
  UnifiedTermRowRef: [add only for a current row returned by section 4.4]
  LineageEntries:
  RefreshCondition:
```

Field discipline:

- The card is a `C.2.1` episteme. `GovernedValueRef` is its exact `EntityOfConcern`; the complete `U.ClaimGraph` constituted by all identity-bearing naming-settlement claims is its `ClaimContent`; and `ReferenceScheme` is the effective by-value `U.ReferenceScheme` under which that graph is interpreted. Changing any of those three identifies another card episteme. Changing only a graph designator, card designator, carrier, field order, or layout does not.
- In the expanded form, the `ClaimContent` field resolves to that complete graph; it is never a scalar summary beside other identity-bearing claims. The readable sibling fields designate graph nodes, edges, or projections. Changing a selected designation, declared use, local-sense claim, coverage, rejection, rationale, lineage, or reopen claim changes the graph and therefore the card episteme even if the displayed `ClaimContent` reference string stays the same.
- `NameCardId` designates the card episteme. It is not another identity discriminator and does not create a card kind.
- `GovernedValueRef` resolves to the exact already-governed object or value being named. `GovernedValueKindRef` is added when the kind is not already unambiguous from that value and its direct owner, or when a receiving use needs the exact kind reference. For relation-facing wording the value reference resolves to exactly one of the objects distinguished in section 5.6; a field label, card, table row, or local phrase is not a proxy for that object.
- `GoverningPatternRef` names the direct pattern that decides the value. `F.18` governs only the naming settlement recorded in the card; a pattern that merely presents or teaches the name governs neither the value nor this settlement.
- `LocalSenseRef` in a progressive-minimum card states the exact local-sense claim directly. `LocalSenseCellRef` in an expanded card resolves to a separately recoverable local sense under the effective scheme. `LocalSenseBasisRelationRef` is present only when a separately governed relation to a basis episteme is current; a source title, card field, or publication is not that relation.
- `CandidateSet` records the plausible labels considered by head-term family. When family coverage or an exception is not already recoverable from the set, rejections, and rationale, add `CandidateCoverage` to state which live families and neighbouring-object readings were tested and whether any plausible alternative remains open.
- `RejectedCandidates` records why tempting names were not selected. A usable alias is recorded in lineage as an alias, not left as a second selected Plain label.
- `BridgeRefs` contains only actual `F.9` Bridge occurrences whose current result admits this naming use; omit it when the settlement makes no Bridge claim.
- `PublicRowStatus` is exactly one of `localOnly`, `pending`, or `current` when public-row use is current. `UnifiedTermRowRef` separately resolves to the exact row and is present only when status is `current` after the section 4.4 `F.17` entry/result gate passes. Omission in an accepted progressive-minimum card claims no row. A pending public use does not imply that a row already exists.
- `RefreshCondition` names the smallest value, kind, scheme, local-sense, Bridge, governing-pattern, use, or repeated-reader-error change that reopens this exact settlement.

Names such as "foundational principle pattern set", "FPF Core", "domain principle framework", and "local practice framework" require ordinary `NameCard` work before public stabilization under an effective reference scheme. Source aliases such as `ZPF`, `SPF`, `TPF`, or broad `xPF` labels remain intake aliases until `F.18` has settled the governed value and kind, by-value reference scheme, exact local sense, rejected candidates, and admissible short form.

#### F.18:4.3 - Candidate Selection

Do not pick a durable label in one stroke or work toward a fixed candidate count. Build the smallest set that covers at least two live head-term families and every plausible neighbouring-object reading that could change the decision. Stop when each live family has a representative and no untested plausible alternative could overturn the selection. If a deadline forces closure while a plausible family or alternative remains untested, record that exception in `CandidateCoverage` and make it part of `RefreshCondition`.

Judge candidates on:

- semantic fidelity: does the label preserve the governed value without adding or losing required conditions?
- reader ergonomics: can the intended reader recognize, say, and remember it in the current situation?
- morphology fit: does the word shape fit the kind being named, for example role value, method, work, description, relation, slot, characteristic, or status value?
- alias risk: will a careful reader import a wrong sense from nearby FPF patterns or external practice?

Use these as ordinal comparisons. Do not average them into one score. If a Pareto-front or quality-diversity method is used, the dimensions and dominance rule must be visible on the card.

One candidate can win even when it is not perfect, but the `SelectionRationale` must say what it buys, what risk remains, and why the covered set is sufficient for this use.

#### F.18:4.4 - Public Term Rows

A durable local name needs no row. When public, Core-facing, durable-across-context, or cross-context reuse is current, test the then-current `F.17` entry with the exact objects already recovered here. The entry must accept separate references to the governed value and its kind, direct pattern, NameCard episteme, selected Tech and Plain designations, effective by-value reference scheme, exact local `SenseCell`, any separate local-sense basis relation, and any actual `F.9` Bridge. Its result must return one row for one naming decision with the admitted and blocked use visible. If it cannot, keep the durable name and NameCard local and mark the public row pending. Do not repair or emulate the missing row inside F.18.

When that gate passes, keep these positions distinct:

- `GovernedValueRef`: the exact already-governed value;
- `GovernedValueKindRef`: its exact kind, never an alternative to the value reference;
- direct governing pattern;
- NameCard episteme and selected designation expressions;
- exact local-sense and basis-relation references;
- any actual Bridge occurrence;
- the row or row episteme, its edition, admitted use, blocked use, and currentness condition.

The row is neither the governed value nor an agent of publication. When availability is needed, an `E.24.PUB` `EpistemePublicationRelation` occurrence makes the exact row-episteme edition available to a declared audience for a bounded use through a distinct publication form and presentation carrier. The form does not publish itself, and the row's currentness claim or relation remains separate from the availability occurrence.

A row for `ReviewerRole` points to the role value and its selected names; it neither creates the role nor makes an assignment obtain. A row for `EvidenceUseRelation` points to the admitted relation kind or other exact governed object; it does not make an episteme into a role or make the relation obtain. A row for `SlotKind` or `EndpointSlot` carries or designates selected vocabulary only after the exact slot object is governed; it neither makes that row edition available nor creates a generic interface ontology.

### F.18:5 - Role, Assignment, Slot, and Status Naming Settlement

This settlement makes several naming boundaries explicit.

#### F.18:5.1 - Role Names

A durable role name names one governed `U.Role` value interpreted through one named role-taxonomy episteme under its effective by-value `U.ReferenceScheme`. If one selected model-use structure, role-relation structure, claim scope, or project-work relation changes the naming use, cite that object separately; the name does not create it. Good role names normally use role morphology, for example `ReviewerRole`, `ShipbuilderRole`, or `ServiceProviderRole`.

A role name must not include:

- the holder that fills a role assignment;
- capability evidence or skill level;
- method or method-family selection;
- performed work;
- status value or gate result;
- source, evidence, publication, or assurance use.

If a phrase such as `SeniorReviewer`, `NightOperator`, or source wording like evidence role appears, recover the governed values first. The result may be a role value, a holder assignment, a status assertion, an evidence-use relation, a work admission condition, or a local source phrase. Do not force all of them into one role name.

#### F.18:5.2 - Holder Assignment Names

A holder-assignment name denotes one already recoverable obtaining `U.RoleAssignment` occurrence governed by `A.2.1`; the role name itself does not identify that occurrence. Before naming it, recover its four actual participants: the admitted holder system, role value, role-taxonomy episteme, and effective reference scheme. Also recover the uninterrupted assignment episode. The currently known `AssignmentInterval` remains assertion- or occurrence-description content, not a fifth participant. A durable name uses a `NameCard` whose `GovernedValueRef` resolves to that occurrence. If public or cross-context reuse is needed, apply the section 4.4 gate; until it passes, retain the card locally and mark the row pending. Neither a name, card, row, nor publication occurrence makes the assignment obtain.

`Holder#Role:Context@Window` is source notation only. Recover the exact referent behind `Context`, its kind, and the direct relation that makes it relevant. A selected `BoundedModelUseStructure` stays in the receiving assertion or use and appears only when it changes interpretation. The token is neither a role name nor proof of assignment, capability, or performed work.

#### F.18:5.3 - Capability, Method, and Work Names

Keep these separate:

- `ShipbuilderRole` names a role value;
- `ShipbuildingCapability` names a capability of an admitted `U.System`, including an acting holon admitted as a system for that capability claim;
- `ShipbuildingMethod` names a method or method family;
- `HullAssemblyWork` names a work family or planning-level work label until an exact performed occurrence is current.

A role-derived or role-method-coupled expression is only a naming cue. First recover the exact value it refers to. If that value is an exact method or method family under `A.3.1`, choose a method name. If it is an exact `U.MethodDescription`, `U.WorkPlan`, or dated `U.Work` occurrence, name that description episteme, plan episteme, or occurrence separately under `A.3.2`, `A.15.2`, or `A.15.1`; those names are not method names. If the expression refers to another value, use that value's direct owner. `F.18` chooses a durable name only after this recovery. A role relation may constrain who may use the method or perform the work; it neither creates nor names the method, description, plan, or work occurrence.

Treat an action nominal such as `testing`, `assembly`, `maintenance`, `evaluation`, or `inspection` as a morphology cue, not a governed kind. Placement in function- or flow-structure prose identifies no `U.Function`. If the function-like use remains claim-bearing while its exact object or relation is hidden, apply `A.6.F`; if it is already recoverable, name the exact method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, performed-work occurrence, or other governed value under its direct pattern before F.18 selects a durable name. A WBS element, activity, or Work Package remains plan- or assignment-episteme content about intended work; none of these uses identifies a performed Work occurrence admitted under `U.Work`.

A durable name for exact performed work names one occurrence already grounded under `A.15.1`, not the action nominal or plan row. The current naming use must be able to recover the performer through an obtaining `U.RoleAssignment`, actual `enactsMethod`, temporal extent, exact containing system, affected referent, and the direct bindings and resource-use facts material to the occurrence. Add the exact continuity policy only when interruption, retry, changed method or bindings, or competing designators make occurrence identity material. Keep neighboring direct subject or resource-use claims, `A.15.PROD` production claims, measurement-result epistemes, evaluation results, `C.11` choices or decisions, delivery occurrences, acceptance verdicts, and downstream-effect claims separately named under their direct governors.

When the underlying boundary wording still hides the relation, apply `A.6.P.WMR`. `F.18` starts only after an exact governed value and its use are recovered through a direct subject relation, an exact `A.6.1` application binding, or an exact local `A.15.PROD`/`A.6.RCD` claim. An exact non-assertability result independently records `factually unsupported`, `missing-information`, or `missing-governor`; none authorizes durable naming, and only `missing-governor` is an ontology blocker that names the affected use and future owner. This section selects and tests a name. It does not define a second work-occurrence or work-result recovery algorithm.

Method-relation and method-composition names are method-side names too. If a phrase names serial composition, parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, fallback, or dispatch among methods, first decide which object the phrase names.

- If admitted submethods make one composite way of doing, name the composite `U.Method`. `A.3.1` governs that Method, and its exact composition relation stays with `B.1.5` or another direct composition owner.
- If the phrase names relations among methods without making one whole Method, select a `U.Structure` under `A.22` and designate it `MethodRelationStructure@BoundedContext`. Each included composition, refinement, substitution, iteration, decomposition, family-membership, selector, fallback, description, or work-use relation stays with its direct `A.3.1`, `G.5`, `A.15`, or composition owner.
- If the current object is a separately identified episteme that describes one exact admitted Method, `A.3.2` may classify it as `U.MethodDescription`; F.18 names that episteme separately from the Method.
- If an episteme instead describes the selected relation structure, `C.2.1` keeps that structure as its exact `EntityOfConcern`; the episteme is not thereby a `U.MethodDescription`.

F.18 settles a durable name only after one of those exact objects has been recovered. Algebraic, graph, categorical, process-calculus, matrix, embedding, distributed, or neural notation names the lens or representation only when that lens is the governed value.

#### F.18:5.4 - Role-Relation, Method-Relation, Role-Method, and Lens Names

Role-relation expressions remain expressions or relations unless the direct role pattern admits a durable role value and the NameCard settles its by-value reference scheme and local sense. A role-algebra, graph, matrix, embedding, distributed, or neural description is a lens over the selected role relation structure; it is not automatically the named role, holder, method, or work.

First recover what the name is for:

| Expression or source phrase | What can be named | Naming rule |
| --- | --- | --- |
| `R1 <= R2` | one exact `RoleAdmissionSubstitutionRelation` occurrence between two interpreted role values under its receiving-use predicate, taxonomy episteme, by-value scheme, and qualification window | Name or cite the exact relation occurrence or selected `RoleRelationStructure`; keep any assertion or policy record, current assignment, receiving check, and outcome separate. Name a new role only when the direct role pattern independently admits that value. |
| `R1 incompatibleWith R2` | one exact `RoleIncompatibilityRelation` occurrence between two interpreted role values under its by-value incompatibility predicate and qualification window | Name or cite the relation occurrence or selected `RoleRelationStructure`, not a new role. Exact assignment occurrences, holder/work/time conditions, the receiving check, and its admit/reject/defer result remain in the predicate or neighbouring objects; they are not substituted for the two role-value positions. |
| `R1 and R2` | independent role values and assignments, when both remain current separately | Use "and" in ordinary prose; do not hide independent assignments by hyphenating them. |
| `R1 bundle R2` or `RoleBundle := R1 and R2` | role-bundle expression or durable bundle role value, if admitted | Keep it as an expression unless a direct role pattern admits a durable bundle value and its NameCard settles the reference scheme and local sense. |
| `R1` qualified by domain, practice, method family, or work field | local qualified role expression such as robotics-qualified engineering role | Ordinary labels may be `robotics engineer` or `engineer-roboticist`; `Role` suffix is optional Tech-register disambiguation. |
| method-like phrase derived from a role label | method, method family, method description, work plan, or work occurrence | Name under `A.3.1`, `A.3.2`, or `A.15`; cite the role relation separately when it constrains who may use or perform the method. |
| algebraic, graph, matrix, embedding, distributed, or neural representation of roles | mathematical or representation description of selected role relation structure | Name the lens only when the representation itself is the governed value; otherwise name the recovered role relation, role expression, method, or work. |
| method algebra, method graph, method matrix, process calculus, selector calculus, or method embedding | mathematical or representation description of selected `MethodRelationStructure@BoundedContext` | Name the lens only when the representation itself is the governed value; otherwise name the selected method relation structure, method family, method description, work plan, work occurrence, or neighboring relation. |
Ordinary speech can omit `Role` and `Method` suffixes when the governed kind, named role-taxonomy episteme where a role is current, effective reference scheme, exact local sense, and direct claim keep the distinction recoverable. Formal suffixes are useful when the name becomes cross-scheme, public, or easy to confuse with a method, capability, work occurrence, status, publication, or policy term.

#### F.18:5.5 - Status, Evidence, Source, and Publication Names

Status-like and evidence-like wording must go to direct patterns:

- status value or status assertion: `F.10` or `A.19.SPR`;
- evidence-use relation: `A.10`;
- assurance use: `B.3`;
- source use: `E.10.D2` or source-use patterns;
- description-episteme identity: `C.2.1`;
- multi-view publication face or form: `E.17`;
- availability of one selected edition, expression by a form, and bearing by a carrier: `E.24.PUB`;
- gate or admission result: the relevant gate, decision, or assurance pattern.

Do not name these as `U.Role` values unless a work-facing role value is actually current. "This standard plays the role of evidence" is repaired to the appropriate evidence-use, source-use, or status-use relation; it is not a work-role assignment for the standard.

#### F.18:5.6 - Relation, Slot, Interface, Port, and Signature Names

If a name touches relation, slot, interface, port, boundary, protocol, API, or signature wording, use `A.6.RSIR` and direct governing patterns.

- `A.6.5` governs relation slot discipline and SlotSpecs.
- `A.6.0` governs signatures and rule-governed declarations.
- `A.6.M` and architecture patterns govern module interfaces and architecture interfaces.
- `A.6.F`, transformation, and architecture patterns govern functional ports and functional structures.
- `A.6.C`, protocol, service-access, and commitment patterns govern API, protocol, and service-access cases.
- `C.2.1` governs a claim-bearing interface-description episteme.
- `E.17` governs a multi-view publication face or form.
- `E.24.PUB` governs availability of the selected edition and the separate form-expression and carrier-bearing relations.

Before naming a relation-facing object, keep these settlements distinct:

| Object to name | Required prior settlement |
| --- | --- |
| reusable predicate-definition episteme | `A.6.RCD` has selected reusable definition and `C.2.1` gives it one truthful exact `EntityOfConcern`; the name denotes the definition, not a relation kind |
| derived or primitive relation kind | `A.6.RCD`, `E.24`, and `E.24.UK` have admitted the kind and its direct subject pattern states obtaining, applicability, and occurrence identity |
| one obtaining relation occurrence | the direct owner establishes obtaining and `A.6.REL` applies the admitted kind's identity rule |
| formula, query, path, graph, diagram, or other representation element | `C.29` states what it represents and the relevant correspondence; its name does not name the represented relation by default |
| designator or reference | the exact designation or reference relation resolves to the already settled object under its reference scheme |

One token may be reused only where the reference scheme and local sense preserve these distinctions; it cannot collapse definition, kind, occurrence, representation, and designator into one object.

`F.18` can settle a durable name for the recovered value. It does not decide which value the interface word names, create a public row, or make that row available.

### F.18:6 - What Belongs In The Label

Belongs in the label:

- a head word that helps readers recognize the governed value;
- a stable qualifier that is part of the local sense;
- role morphology when the governed value is a role;
- relation, slot, method, work, or characteristic morphology when those kinds are current.

Does not belong in the label:

- numbers and thresholds;
- temporary admission state;
- holder identity;
- capability evidence;
- method fit unless the governed value is a method or method family;
- work occurrence;
- gate result;
- source or evidence authority;
- context label used as if it were universal.

Quick check: if removing the word changes only current admission, holder, evidence, date, or gate use, it does not belong in the durable label.

### F.18:7 - Worked Cases

#### F.18:7.1 - Role, Holder, Capability, Method, And Work

A shipyard team wants one reusable name for the role used in shipbuilding work. It first separates the values that the source word "shipbuilder" could hide.

Recovered values:

- `ShipbuilderRole`, interpreted through the role-taxonomy episteme `ShipyardProductionRoles-2026` under `Shipyard-Production-Scheme`;
- one holder-assignment occurrence under `A.2.1`, with its holder system, role value, taxonomy episteme, and scheme as participants and its known assignment interval stated separately;
- `ShipbuildingCapability` with envelope and measures under capability patterns;
- `ShipbuildingMethod` or method family under `A.3.1`; if a separately identified `ShipbuildingMethodDescription : U.MethodDescription` episteme is current, name it separately under `A.3.2` only when its exact `EntityOfConcern` is that Method;
- `HullAssemblyWork` under work patterns.

Here `HullAssemblyWork` is a work-family label or a label in a plan or assignment episteme. A designator such as `HullAssemblyWork-42@2026-07-15T09:10/11:35` names performed work only when the current record recovers its obtaining performer assignment, enacted method, temporal extent, containing system, affected hull referent, material bindings and resource-use facts, plus an applicable continuity policy when disambiguation is current. A changed hull state, measurement result, evaluation verdict, delivery occurrence, or acceptance verdict remains a separately governed and separately named value.

F.18 settlement:

```text
NameCard:
  NameCardId: NameCard.ShipbuilderRole.ShipyardProduction.2026
  GovernedValueRef: ShipbuilderRole
  GovernedValueKindRef: U.Role
  GoverningPatternRef: A.2
  ReferenceScheme: Shipyard-Production-Scheme
  ClaimContent: NameCard.ShipbuilderRole.ShipyardProduction.2026.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseCellRef: SenseCell.ShipbuilderRole.ShipyardProductionRoles-2026 — local expression `shipbuilder role`; sense: the ShipbuilderRole value interpreted by ShipyardProductionRoles-2026 under Shipyard-Production-Scheme
  LocalSenseBasisRelationRef: absent; no independently admitted local-sense basis relation is current for this case
  TechLabel: ShipbuilderRole
  PlainLabel: shipbuilder role
  CandidateSet: ShipbuilderRole; ShipbuildingCapability; HullAssemblyWorker; CertifiedShipbuilder
  CandidateCoverage: role head; capability head; holder-or-work head; certification-or-status head; no plausible live head family remains untested
  RejectedCandidates: ShipbuildingCapability; HullAssemblyWorker; CertifiedShipbuilder
  SelectionRationale: selected label names the role value without claiming capability, holder assignment, performed work, or certification
  BridgeRefs: absent; this local settlement claims no cross-context correspondence
  PublicRowStatus: localOnly; change to pending only if public or cross-context reuse opens and section 4.4 does not yet pass
  UnifiedTermRowRef: absent
  LineageEntries: initial durable settlement; source word "shipbuilder" split from capability, holder-or-worker, performed-work, and certification readings
  RefreshCondition: reopen if A.2 changes the role value, the taxonomy episteme or scheme edition changes its local sense, or repeated readers infer capability, assignment, work, or certification
```

The four candidates execute the section 4.3 stopping rule: each live head family is represented, and the already recovered method and work objects are not plausible alternative labels for this role value. The rejected candidates are not "worse synonyms." They name different governed values or add conditions not carried by this role value. If public, Core-facing, durable-across-context, or cross-context reuse becomes current, apply the section 4.4 gate. Until it passes, keep this card local and do not imply a row or publication occurrence.

#### F.18:7.2 - Engineer-Roboticist and Musician

A lab says: "Vasya is an engineer, does robot engineering, is therefore an engineer-roboticist. These are musical robots, and Vasya is also a musician, performs music, and teaches robots music."

Recovered values:

- Vasya as the admitted holder system; `MusicalRobotLab_2026` is the lab and work locus in its direct relations, not a participant added to `U.RoleAssignment`;
- `MusicalRobotLabRoles-2026` as the role-taxonomy episteme and `MusicalRobotLab-Scheme` as its effective reference scheme;
- an engineering role value or local engineering-role expression;
- robotics as a domain, practice, method-family, or work-field qualification of that engineering role expression;
- `MusicianRole` as an independent role value when music performance matters separately;
- robot-engineering method or work, music-performance work, and robot-music-teaching method or work under method and work patterns;
- an optional role-algebra, graph, matrix, embedding, or neural representation only if the project actually uses such a lens to describe the selected role relation structure.

If a durable qualified role value has been admitted, its naming settlement can be:

```text
NameCard:
  NameCardId: NameCard.RoboticsEngineerRole.MusicalRobotLab.2026
  GovernedValueRef: RoboticsEngineerRole
  GovernedValueKindRef: U.Role
  GoverningPatternRef: A.2
  ReferenceScheme: MusicalRobotLab-Scheme
  ClaimContent: NameCard.RoboticsEngineerRole.MusicalRobotLab.2026.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseCellRef: SenseCell.RoboticsEngineerRole.MusicalRobotLabRoles-2026 — local expressions `engineer-roboticist` and `robotics engineer`; sense: the admitted engineering role qualified by the robotics work field under MusicalRobotLab-Scheme
  LocalSenseBasisRelationRef: absent; no separate source-bearing basis relation is current for this use
  TechLabel: RoboticsEngineerRole
  PlainLabel: engineer-roboticist
  CandidateSet: RoboticsEngineerRole; engineer-roboticist; robotics engineer; engineer and roboticist; RobotEngineeringMethod; engineer-roboticist-musician
  CandidateCoverage: Tech role head; two ordinary role-expression forms; method neighbour; compressed multi-role neighbour; no plausible live head family remains untested
  RejectedCandidates: engineer and roboticist; engineer-roboticist-musician; RobotEngineeringMethod
  SelectionRationale: Tech `RoboticsEngineerRole` and Plain `engineer-roboticist` are selected for this source-preserving lab use; robotics remains a qualification of engineering, musician remains a separate role assignment, and method or work names do not become role names
  BridgeRefs: absent; the card claims no cross-context correspondence
  PublicRowStatus: localOnly; change to pending only if public or cross-context reuse opens and section 4.4 does not yet pass
  UnifiedTermRowRef: absent
  LineageEntries: initial durable qualified-role settlement; `robotics engineer` retained as a Plain alias for the same value, scheme, sense, and declared use, not as a second selected PlainLabel; earlier local wording retained when no durable role value is admitted
  RefreshCondition: reopen if A.2 changes the role value, A.2.7 changes the qualification relation, the taxonomy episteme or scheme changes, or readers merge musician assignment, method, or work into this role name
```

The robotics qualification relation remains separately governed by `A.2.7`; the card does not absorb it into role identity. If no durable qualified role value is admitted, keep `engineer-roboticist` as local ordinary wording rather than filling the card. In ordinary project communication, "Vasya is our engineer-roboticist and musician" is admissible when the two assignments remain recoverable. If the current object is a method, name `RobotEngineeringMethod` or the relevant method family under `A.3.1`. If a separately identified `RobotEngineeringMethodDescription : U.MethodDescription` episteme is current, name it separately under `A.3.2` only when its exact `EntityOfConcern` is that Method. If the current object is performed work, name the work occurrence under `A.15.1`. If public reuse becomes current, apply section 4.4; do not infer a current F.17 row from this local card.

#### F.18:7.2a - Method Relation Structure and Method Algebra Name

A lab says: "Use the robot-engineering method algebra: choose scouting, then calibration, then training; fall back to teleoperation if training fails."

Recovered values:

- one or more robot-engineering methods or method families under `A.3.1`;
- a method-family registry or selector outcome under `G.5` when the family registry or selector result is current;
- `MethodRelationStructure@MusicalRobotLab_2026` when the current claim is serial composition, guarded fallback, or family selection among methods;
- a method description when the source notation describes that structure;
- a `C.29` mathematical-lens use when "algebra" is the selected representation for checking composition, fallback, or preserved/lost structure;
- work plan or dated work only when a concrete plan or occurrence is current.

F.18 settlement: `RobotEngineeringMethod` names a method or method family only when that is the governed value. `RobotEngineeringMethodRelationStructure` may be a Tech-register name for the selected method relation structure when durable naming is needed. `RobotEngineeringMethodAlgebra` names the lens only when the algebraic representation itself is the governed value. Do not use a role label such as `RoboticsEngineerRole` to name the method relation structure, and do not use "method algebra" to hide a work plan or performed work.

#### F.18:7.3 - Evidence-Like Source Phrase

A review table contains the phrase "model card evidence role".

Recovered values:

- a model-card episteme;
- an evidence-use relation to a target claim;
- possible source-currentness and assurance-use relations;
- no work-facing role unless an acting system is assigned one.

F.18 settlement: no durable role name is minted. If a public term is needed, first name the exact evidence-use relation, for example `ModelCardEvidenceUse`, with `A.10` as governing pattern. Then apply the section 4.4 gate; until it passes, retain the durable relation name and NameCard locally and mark the public row pending.

#### F.18:7.4 - Interface-Like Source Phrase

A software team says "the payment interface owns customer identity".

Recovered candidates:

- module interface under `A.6.M`;
- API description or protocol under `A.6.C`;
- signature or SlotSpecs under `A.6.0` and `A.6.5`;
- claim-bearing interface description under `C.2.1`;
- multi-view publication face or form under `E.17`;
- publication availability, form expression, or carrier bearing under `E.24.PUB`;
- responsible role assignment under `A.2.1`.

F.18 settlement: do not mint `PaymentInterfaceRole`. First recover which governed value the phrase names. Then name that value through its governing pattern.

#### F.18:7.5 - Cross-Context Name

Two teams use `component`, `module`, and `unit` for nearby meanings.

Recovered values:

- structural component under architecture and part-whole patterns;
- deployable module under module-interface patterns;
- management unit under organizational patterns.

F.18 settlement: choose a Tech label only for the governed value under the declared by-value reference scheme and exact local sense. Use `F.9` only when its current entry accepts the exact `SenseCell` endpoints and its result supplies the correspondence needed by this naming use; a changed reference scheme by itself establishes neither a Bridge nor governed-value identity. If public or cross-context reuse is needed, apply the section 4.4 `F.17` gate. If that gate fails, keep the name and card local and mark the public row pending; if no public use is current, stop with the local settlement.

### F.18:8 - Anti-Patterns And Repairs

| Anti-pattern | Ontological failure | Repair |
| --- | --- | --- |
| "Same spelling means same value." | Treats string identity or a sense bridge as governed-value identity. | Use `F.9` only to state exact cross-context sense correspondence and admitted use; apply the direct object owner for any identity claim, or keep the values separate. |
| "Evidence role" for a report, source, or standard. | Turns an episteme or source-use relation into a work-facing role. | Recover evidence-use, source-use, status-use, publication-use, or assurance-use relation. |
| "Night operator role" when only schedule differs. | Bakes temporal admission into role identity. | Keep role value; put time window in assignment, status, or work plan. |
| "Certified engineer role" when certification is evidence or admission. | Bakes capability evidence or admission into role name. | Keep `EngineerRole`; record capability evidence, admission, or status relation separately. |
| "Role-derived method" treated as a role-relation result. | Confuses role expression with method identity. | Name the method or method family under `A.3.1`. If a separately identified `U.MethodDescription` episteme is current, name it separately under `A.3.2` only when its exact `EntityOfConcern` is that Method; cite the role requirement separately. |
| "Method algebra" treated as the method or plan. | Confuses mathematical or representation lens with method relation structure, method description, work plan, or performed work. | Recover `MethodRelationStructure@BoundedContext`, method description, `C.29` lens use, work plan, or work occurrence by direct governing pattern before naming. |
| Action nominal, WBS element, or Work Package treated as performed work. | Function/method morphology or intended-work content is mistaken for one dated occurrence; a nearby result is folded into the work name. | Recover the exact `A.15.1` occurrence basis, apply `A.6.P.WMR` if the relation is still hidden, and name neighboring production claims, measurement results, evaluation results, delivery occurrences, and acceptance verdicts separately. |
| Role-looking interface wording for API, port, or boundary. | Uses role morphology to avoid recovering port, signature, boundary, or interface-specific relation. | Use `A.6.RSIR` and the direct governing pattern; name the recovered relation, signature, port, or bounded interface value only when that pattern admits it. |
| "Unscoped glossary." | A glossary episteme carries or lists words without an exact governed value and kind, by-value reference scheme, local sense, and any actually needed Bridge. | Use a `NameCard` for a durable local settlement. Open a public row only through the section 4.4 gate. When availability is current, use an `E.24.PUB` publication occurrence to make the selected row or glossary edition available through a distinct form and carrier. |

### F.18:9 - Conformance Checks

Use these checks before a durable name is reused in a pattern. If an F.17 row is current, run its own row checks after the section 4.4 gate; these F.18 checks neither create that row nor establish a publication occurrence for it.

| Check | Passing condition |
| --- | --- |
| Governed value | The named value is recoverable and belongs to a direct governing pattern. |
| Interpretation | The effective `U.ReferenceScheme` is carried by value and the local sense is named; model-use structure, claim scope, project work, and other locality relations remain separate. |
| Kind | The kind is stated as governed value kind, not inferred from spelling. |
| Candidate set | The smallest set covers at least two live head families and every plausible neighbouring-object reading; any forced untested exception is explicit in `CandidateCoverage` and `RefreshCondition`. |
| Role boundary | Role, role assignment, holder, capability, method, work, evidence, and status claims are not collapsed. |
| Relation-object boundary | Predicate-definition episteme, admitted relation kind, obtaining occurrence, representation element, and designator are named only after their separate governing settlements; relation slot, interface, port, and signature names cite direct governing patterns. |
| Public row | A durable local card is enough unless public, Core-facing, durable-across-context, or cross-context reuse is current. The section 4.4 gate passes before any F.17 row is cited; the row is neither the value nor the publication occurrence. |
| Bridge | `F.9` governs exact cross-context sense correspondence and admitted use, not governed-value identity; cross-scheme interpretation alone does not create an F.9 Bridge. |
| Lineage and reopen | Rename, alias, split, merge, and retirement history is recorded under `F.13`, and the card names the smallest value, scheme, sense, owner, use, or reader-error change that reopens this settlement. |
| Reader use | A practitioner can tell what to say, what not to infer, and where to go if the name is not enough. |
| Work-name boundary | An action nominal remains a morphology cue: a hidden claim-bearing function-like use goes through `A.6.F`, while an already recovered method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, or other value is named only under its direct pattern. A WBS/Work Package label remains plan- or assignment-episteme content, and a performed-work name is accepted only for one occurrence grounded under `A.15.1`; neighboring production claims, measurement results, evaluation results, decisions, delivery occurrences, and acceptance verdicts stay under their direct governors. |

Regression checks:

- When the effective reference-scheme edition changes, re-check local sense and bridge claims.
- When a role description changes, re-check role name and any holder-assignment name.
- When a method, capability, work, evidence, or status pattern changes, re-check any name that borrowed morphology from that area.
- When repeated reader errors occur, reopen candidate comparison instead of adding aliases indefinitely.

### F.18:10 - SoTA-Echoing

Source use was checked on 2026-07-23. F.18 uses only the following decision-governing lines; source prestige does not select an FPF value or name.

| Current source and status | Adopted or adapted move | Exact F.18 effect | Limitation and smallest reopen condition |
| --- | --- | --- | --- |
| [ISO 704:2022](https://www.iso.org/standard/79077.html), published International Standard, and [ISO 1087:2019](https://www.iso.org/standard/62330.html), confirmed current in 2025 | Distinguish objects, concepts, definitions, and designations; make term formation and terminology decisions inspectable. | Governs the value-before-label rule in 0 and 4.1, the separate value/kind/designation fields in 4.2, and the rejection of dictionary substitution in 8. | The standards govern terminology work, not FPF ontic identity. Reopen only 4.1-4.3 and affected cases if a superseding ISO edition changes the selected concept/designation or term-formation distinction. |
| W3C, [*SKOS Simple Knowledge Organization System Reference*](https://www.w3.org/TR/skos-reference/), W3C Recommendation 2009, latest Recommendation checked 2026-07-23 | Keep concepts, preferred or alternative lexical labels, notes, collections, semantic relations, and mapping relations distinct. | Strengthens 4.2, 7.5, 8, and 9: a label, card, row, shared spelling, or generic mapping does not become the governed value or an F.9 Bridge. | SKOS is a stable web-vocabulary model, not the FPF naming method or a source of FPF kinds. Reopen those four loci if W3C supersedes the Recommendation or changes the label/mapping distinction used here. |
| Zhu, Reinecke, and Mitra, [*Language Scent: Exploring Cross-Language Information Navigation*](https://arxiv.org/abs/2604.03604), arXiv:2604.03604, 2026 preprint | Adapt contextual cues and in-situ recognizability as evidence for reader ergonomics; reject any inference from recognizability to cross-context equivalence. | Changes the reader-ergonomics probe in 4.3 and supports the conditional local labels in 7.2 and 7.5 while leaving exact value, local sense, and Bridge recovery mandatory. | The study is small, cross-language, and navigation-focused. Reopen only those probes and examples if stronger reader evidence reverses the observed value of contextual cues or exposes a new loss. |
| Current FPF `C.18` front and archive discipline | Keep non-dominated candidates, archive members, and selection reasons distinct; expose dimensions and dominance when those methods are actually used. | Governs the optional ordinal-comparison sentence in 4.3; it does not require QD apparatus for an ordinary four-candidate naming decision. | This is comparison discipline, not proof that a label is ontologically correct. Reopen only 4.3 if the FPF front, dominance, or protected-dimension rule changes. |

Currentness rule: when a direct value owner, `C.2.1`, `F.9`, or `E.24.PUB` changes the value/card/sense/Bridge/publication boundary, reopen only the affected invariant, field, case, or check. A future F.17 edition is consumed only through section 4.4; its change does not reopen local NameCards unless their admitted public use or object references change.

### F.18:11 - Relations

Builds on `F.0.1`, `F.1`, `F.2`, `F.3`, `F.5`, `F.8`, `F.9`, `F.13`, `F.14`, `F.15`, `C.2.1`, and `E.24.PUB`.

Coordinates with:

- `A.2`, `A.2.1`, `A.2.5`, `A.2.7`, `A.15`, and `A.15.1` for role value, role assignment, role state, exact role relation occurrences and selected `RoleRelationStructure`, role-algebra lens use, role-method-work alignment, and exact performed-work occurrence grounding;
- `A.3.1` for method and method-family names; `A.3.2` for a separately identified `U.MethodDescription` episteme whose exact `EntityOfConcern` is that Method, and for the description episteme's separate name;
- `A.6.P`, `A.6.P.WMR`, `A.6.RCD`, `A.6.REL`, `A.6.5`, `A.6.RSIR`, `A.6.0`, `A.6.M`, `A.6.F`, and `A.6.C` for relation-claim settlement, work/method-boundary relation recovery, relation-kind and occurrence boundaries, slot, signature, interface, port, and protocol names;
- `A.10`, `B.3`, `F.10`, `E.10.D2`, and `C.2.1` for evidence-use, assurance-use, status-use, source-use, and description-episteme names;
- `E.17` for multi-view publication-face and publication-form use;
- `F.17` only after its current entry accepts the exact F.18 value/kind/card/sense/Bridge result and its result supplies the required public row; otherwise the local NameCard remains sufficient and the public row stays pending;
- `E.24.PUB` for the separate occurrence, form, carrier, audience, bounded-use, and currentness objects needed when an exact row-episteme edition is actually made available;
- `C.16`, `C.18`, and Part G search patterns when candidate comparison uses Pareto or quality-diversity vocabulary.

Constrained non-use:

- `F.18` admits no new U-kind and creates none of the governed role, assignment, status, method, work, relation, signature, slot, interface, or other subject values it names. A `NameCard` is a separately constituted `U.Episteme` under `C.2.1`, not a kind minted by F.18.
- `F.18` does not decide whether two values are the same across contexts; it requires the bridge or direct pattern that decides that claim.
- `F.18` does not turn a publication row, card, table, or glossary entry into the thing being named.

### F.18:End

