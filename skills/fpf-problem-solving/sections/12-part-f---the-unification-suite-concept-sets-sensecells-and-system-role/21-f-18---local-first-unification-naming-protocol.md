## F.18 - Local-First Unification Naming Protocol
> **Status:** Stable
*Pattern state: stable pattern. Audience: engineer-managers, lead architects, ontology editors, and authors who must make one name reusable without turning that name into a hidden ontology.*

### F.18:0 - Use This When

Use `F.18` when a name must become stable, public, Core-facing, reusable under more than one named source, practice, or reference scheme, or durable enough that later work can cite it without guessing. Typical cases:

- a local expression becomes a durable name for a system-role kind, relation, slot, method, work, characteristic, status value, architecture element, or other already governed value;
- two teams use different words for the same candidate sense and need one reusable term plus preserved local wording;
- one tempting head word is useful under one recovered local meaning but misleading under another;
- a system-role-derived, method-derived, status-like, evidence-like, interface-like, or slot-like name risks creating a second ontology by wording alone.

**First useful move.**

1. Recover the exact value and the pattern containing its defining or testing rule.
2. Decide whether ordinary local wording is enough or later use really needs a durable name.
3. If a durable name is needed, compare the plausible names and record one Tech label, one Plain explanation, the selection reason, and the reopen condition in a `NameCard`.

If bare claim-bearing *role* still hides the object, use `E.10.ROLE`; if relation, slot, interface, port, or signature wording hides it, use section 5.6. Open section 4.4 only for a genuinely public, Core-facing, durable-across-context, or cross-context use. A public row is a later result, never part of the first naming move.

Do not use `F.18` for one-off wording repair. If the phrase is local and not becoming a reusable name, use `E.10`, `E.10.ARCH`, `A.6.P`, `A.6.RSIR`, `C.2.P`, or the pattern containing the rule for the object being named. In particular, say in ordinary words whether one exact Bridge is suitable for one named use; do not create a `NameCard`, public claim kind, or durable CamelCase head merely to abbreviate that C.2.1 claim. Reopen F.18 for that claim only when an independent later use actually needs a reusable name beyond the local statement.

### F.18:1 - Context

Names are handles for use, not creators of ontology. A good name lets people talk about a governed value without smuggling in an extra system-role kind, assignment, capability, method, work, status, evidence, interface, or cross-context claim.

`FPFCoreReferenceScheme` is the by-value `U.ReferenceScheme` used to interpret current FPF Core Tech labels and relation names; a name under another scheme carries that scheme by value. Most naming work stays within one `<ReferenceScheme, LocalSenseClaim>` projection and needs no Bridge. If one named use must relate different projections, follow the later cross-projection branch in section 4.4.1. Shared spelling, another scheme, or a selected model-use structure alone creates no Bridge, use claim, reliance, governed-value identity, or `U.BoundedContext`.

`F.18` supplies the naming discipline for Part F and for any FPF pattern that needs a durable public term. It coordinates with:

- `F.5` for type-name and system-role-kind-description label form;
- `F.8` for the prior decision that an expression should become a durable name rather than remain local, reused, or aliased;
- `F.9` for an actual sense Bridge between different `<ReferenceScheme, LocalSenseClaim>` projections;
- `F.13` for renames, aliases, splits, and merges;
- `F.14` for anti-explosion control;
- `F.17` only as a later public-row consumer whose current entry and result must accept the exact F.18 objects named below;
- `E.10.ROLE` when bare claim-bearing *role* hides its object; `A.6.5` and `A.6.RSIR` when relation, signature, interface, or slot wording hides the governed object; `A.6.P.WMR` when Work and Method boundary wording still hides the exact relation; and `A.15.1` when a candidate performed-work name still lacks occurrence grounding.

The central subject is one `F.18` naming settlement for one exact already-governed value. `F.18` supplies the candidate comparison, selected Tech and Plain designations, declared naming use, and reopen conditions. The value's direct pattern retains its kind, identity, obtaining, and other subject semantics.

Its complete claim graph records the selected designation expressions, exact local sense, covered and rejected alternatives, rationale, lineage, and reopen condition.

### F.18:2 - Problem

FPF texts fail when names are treated as if they carried ontology by themselves.

1. A short label appears in another context and gets treated as the same value although no obtaining Bridge establishes the exact sense relation, no separate claim says that Bridge suits this reuse, and no current reliance supports that claim.
2. A role-looking name quietly bundles a system-role kind, assignment occurrence, capability, method fit, work evidence, or authorization.
3. A status-like or evidence-like phrase becomes a fake role or fake type because the row says "evidence role", "status role", or similar wording.
4. A relation, declaration-local slot, interface, port, or signature name hides the exact governed object, relation-participant meaning, or rules that define or constrain the claim.
5. A term chosen for convenience becomes a permanent Core-facing name without candidate comparison, rejected alternatives, or lineage.
6. Local names proliferate until the corpus has several almost-synonyms and no recoverable reason for choosing one.

The repair is not to choose prettier words. Recover the governed value, then record a naming settlement whose kind, effective reference scheme, exact local sense, intended use, and selected designations remain visible. Publication is a separate later relation.

### F.18:3 - Forces

| Force | Naming tension |
| --- | --- |
| Local sense and reuse across different semantic-context projections | A name must be interpretable under one effective by-value `U.ReferenceScheme` while remaining bridgeable to a different `<ReferenceScheme, LocalSenseClaim>` projection without spelling-based identity. The projections can differ under one scheme. |
| Brevity and ontology recovery | A short label helps conversation, but the `NameCard` must keep governed kind, effective reference scheme, local sense, subject pattern, and intended use recoverable. |
| Continuity and correction | Readers need stable public names, while authors must be able to rename, split, merge, or retire names without erasing earlier uses. |
| Familiarity and precision | Familiar words are easier to adopt, but some familiar words import wrong prototypes from another discipline. |
| System-role recognition and ontology expansion | `SystemRole` morphology helps identify one exact local system-role kind, but it must not absorb assignment, capability, method, work, evidence, status, participant, declaration-place, or representation-position claims. |

### F.18:4 - Solution

Use a local-first naming protocol:

1. Recover the governed value, its kind, and its subject pattern.
2. Decide whether the expression should remain local or the current use needs a durable reusable name; apply `F.14` before adding a card, cell, or row.
3. For a durable name, constitute one `NameCard` episteme under `C.2.1`; keep the value, its kind, the card, selected designations, exact local sense, and any basis or Bridge relation distinct.
4. Choose the Tech and Plain labels from the smallest candidate set that covers the live head-term families and plausible neighbouring objects.
5. Record the covered alternatives, rejected candidates, selection reason, lineage, and the smallest condition that reopens the settlement.
6. Only for public, Core-facing, durable-across-context, or cross-context reuse, test the then-current `F.17` entry. It must accept the exact governed value and kind, NameCard episteme, by-value scheme, local sense, and any actual Bridge. Public or durable reuse alone creates no Bridge. When the named use relates different `<ReferenceScheme, LocalSenseClaim>` projections, F.17 must also accept the separate affirmative C.2.1 claim and current A.10 or B.3 reliance through the row rationale or notes rather than treating either as NameCard content. Its result must supply the required public row. If any required input or result is absent, retain the durable name and NameCard locally, mark the public row pending, and stop.
7. Keep the Bridge, the separate claim about its named use, A.10 or B.3 reliance, authorization, and any actual Work, assertion episteme, publication occurrence, direct relation, operation application, status, evidence, slot, system-role kind, assignment, method, or interface object under their direct rules. Only the naming settlement is in scope here.

#### F.18:4.1 - Naming Invariants

Every durable name must satisfy these invariants.

| Invariant | Required content |
| --- | --- |
| Governed value first | Name the governed value or value family before naming the label. |
| Direct pattern visible | Cite the pattern description containing the exact defining or constraining ClaimGraph for the value: for example A.2 with C.3 for a local system-role kind, A.2.1 for one system-role assignment species, A.6.5 for relation slot discipline, F.10 or A.19.SPR for status-value use, and A.10 for evidence use. |
| Reference scheme visible | The NameCard carries the effective `U.ReferenceScheme` by value; a model-use structure, claim scope, project work, or other locality relation remains separate and appears only when the naming use needs it. |
| Local sense visible | Every card states one exact local-sense claim under the effective scheme. A progressive-minimum card may state it directly as `LocalSenseRef`; an expanded card uses `LocalSenseCellRef` only when it resolves to the current F.17 scheme-based coordinate. Any basis episteme and local-sense basis relation remain separate. |
| Two labels when reusable | The Tech label is precise; the Plain label helps ordinary readers. Both point to the same governed value. |
| Candidate comparison visible | At least two plausible head families are considered unless a cited external standard fixes the label. |
| Bridge only between different semantic-context projections | Compare the exact `<ReferenceScheme, LocalSenseClaim>` pairs. Same scheme plus same claim plus another expression is a designation question and creates no Bridge. Same scheme plus another claim opens the F.9 question and, for a named use, the separate claim-and-reliance branch. Different scheme also opens only the Bridge question. No current correspondence use creates no Bridge or use claim regardless of scheme count. An obtaining Bridge establishes only the exact sense relation; it establishes neither governed-value identity nor authorization. |
| Lineage visible | Rename, split, merge, retirement, and alias decisions are recorded. |

#### F.18:4.2 - `NameCard` Fields

A NameCard is complete when its exact C.2.1 identity-bearing `U.ClaimGraph` is recoverable; completeness is not a field count. The accepted D11 progressive-minimum cards `NC-U-RELATION`, `NC-CROSS-CONTEXT-RELATION-STRUCTURE`, `NC-PROBLEM-CRITERION-APPLICABILITY-RELATION`, and `NC-PROBLEMATIC-FOR-RELATION` remain conforming. Each already states the governed value and subject pattern, effective scheme and local-sense claim, one selected Tech/Plain pair, candidate set, rejections, rationale, lineage, and reopen condition. Its subject pattern makes the governed kind unambiguous. These filled claims together constitute the card's complete claim graph; an omitted expanded field contributes no hidden claim. Section 4.2a carries the four current expanded bounded-model-use cards.

Use the expanded form only when the current naming use needs the additional position:

```text
NameCard:
  NameCardId:
  GovernedValueRef:
  GovernedValueKindRef: [add when the kind is not unambiguous from the value and subject pattern, or a consumer needs the exact kind reference]
  SubjectPatternLocator:
  ReferenceScheme:
  ClaimContent: [reference to the complete U.ClaimGraph constituted by all identity-bearing naming-settlement claims]
  LocalSenseCellRef: [add when a separately recoverable F.17 scheme-based SenseCell is current; otherwise LocalSenseRef carries the direct local-sense claim]
  LocalSenseBasisRelationRef: [add only for an actual separately governed basis relation]
  TechLabel:
  PlainLabel:
  CandidateSet:
  CandidateCoverage: [add when family coverage, an open alternative, or a forced exception must be explicit]
  RejectedCandidates:
  SelectionRationale:
  BridgeRefs: [add only for actual F.9 Bridge occurrences used to align exact local senses; no use direction, rule, tolerance, polarity, or reliance lives here]
  PublicRowStatus: [add when public-row use is current]
  UnifiedTermRowRef: [add only for a current row admitted under section 4.4]
  LineageEntries:
  RefreshCondition:
```

Field discipline:

- The card is a `C.2.1` episteme. `GovernedValueRef` is its exact `EntityOfConcern`; the complete `U.ClaimGraph` constituted by all identity-bearing naming-settlement claims is its `ClaimContent`; and `ReferenceScheme` is the effective by-value `U.ReferenceScheme` under which that graph is interpreted. Changing any of those three identifies another card episteme. Changing only a graph designator, card designator, carrier, field order, or layout does not.
- In the expanded form, the `ClaimContent` field resolves to that complete graph; it is never a scalar summary beside other identity-bearing claims. The readable sibling fields designate graph nodes, edges, or projections. Changing a selected designation, declared use, local-sense claim, coverage, rejection, rationale, lineage, or reopen claim changes the graph and therefore the card episteme even if the displayed `ClaimContent` reference string stays the same.
- `NameCardId` designates the card episteme. It is not another identity discriminator and does not create a card kind.
- `GovernedValueRef` resolves to the exact already-governed object or value being named. `GovernedValueKindRef` is added when the kind is not already unambiguous from that value and its subject pattern, or when a receiving use needs the exact kind reference. For relation-facing wording the value reference resolves to exactly one of the objects distinguished in section 5.6; a field label, card, table row, or local phrase is not a proxy for that object.
- `subjectPatternLocator` names the pattern description containing the exact ClaimGraph that defines or constrains the value. `F.18` defines only the naming-settlement predicate recorded in the card; a pattern that merely presents or teaches the name defines neither the value nor this settlement.
- `LocalSenseRef` in a progressive-minimum card states the exact local-sense claim directly under the card's by-value scheme. `LocalSenseCellRef` in an expanded card resolves to the current F.17 coordinate `<ReferenceScheme by value, LocalExpression, LocalSenseClaim>` and does not require a context holon. `LocalSenseBasisRelationRef` is present only when a separately governed relation to a basis episteme is current; a source title, card field, or publication is not that relation.
- `CandidateSet` records the plausible labels considered by head-term family. When family coverage or an exception is not already recoverable from the set, rejections, and rationale, add `CandidateCoverage` to state which live families and neighbouring-object readings were tested and whether any plausible alternative remains open.
- `RejectedCandidates` records why tempting names were not selected. A usable alias is recorded in lineage as an alias, not left as a second selected Plain label.
- `BridgeRefs` contains only actual F.9 Bridge occurrences whose relation-semantic profiles obtain for the exact endpoint senses. It carries no naming-use direction, use-specific rule, tolerated loss, polarity, reliance, or permission. When naming across different semantic-context projections relies on a Bridge, recover the separate C.2.1 claim and its current A.10 or B.3 reliance outside the NameCard; omit `BridgeRefs` when the settlement makes no Bridge claim.
- `PublicRowStatus` is exactly one of `localOnly`, `pending`, or `current` when public-row use is current. `UnifiedTermRowRef` separately resolves to the exact row and is present only when status is `current` after the section 4.4 `F.17` entry/result gate passes. Omission in an accepted progressive-minimum card claims no row. A pending public use does not imply that a row already exists.
- `RefreshCondition` names the smallest value, kind, scheme, local-sense, Bridge, subject-pattern, use, or repeated-reader-error change that reopens this exact settlement.

Names such as "foundational principle pattern set", "FPF Core", "domain principle framework", and "local practice framework" require ordinary `NameCard` work before public stabilization under an effective reference scheme. Source aliases such as `ZPF`, `SPF`, `TPF`, or broad `xPF` labels remain intake aliases until `F.18` has settled the governed value and kind, by-value reference scheme, exact local sense, rejected candidates, and admissible short form.

#### F.18:4.2a - Current Bounded-Model-Use NameCards

The four expanded cards below are the current `FPFCoreReferenceScheme` naming settlements consumed by F.17:12.4d-12.4e. Each resolves to one exact current scheme-based F.17 cell and its separately governed local-sense basis relation. They select, record, and make recoverable designations for already governed values; they create no kind, structure, relation occurrence, assertion, Work, Bridge, use, reliance, row-availability occurrence, or other receiving action.

```text
NameCard:
  NameCardId: NC-BOUNDED-MODEL-USE-STRUCTURE
  GovernedValueRef: BoundedModelUseStructure
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.1.1
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-BOUNDED-MODEL-USE-STRUCTURE.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseCellRef: SenseCell.BoundedModelUseStructure.FPFCore.2026-07-25
  LocalSenseBasisRelationRef: LocalSenseBasisRelation.BoundedModelUseStructure.FPFCore.2026-07-25
  TechLabel: BoundedModelUseStructure
  PlainLabel: bounded context
  CandidateSet: BoundedModelUseStructure; ModelApplicabilityStructure; ModelUseRelationStructure; BoundedContextStructure; U.BoundedContext
  CandidateCoverage: exact dependent-structure head; applicability-only neighbour; use-only neighbour; DDD retrieval head; false holon-kind neighbour; no plausible live head family remains untested
  RejectedCandidates: ModelApplicabilityStructure omits actual use and fixed-content expression coherence; ModelUseRelationStructure collapses the wider organization into one relation family; BoundedContextStructure hides what is bounded and invites a container reading; U.BoundedContext falsely claims another holon kind
  SelectionRationale: the Tech label names the A.1.1 dependent U.Structure specialization selected from one exact model edition, admitted model-use holons, obtaining applicability, actual-use, and fixed-content expression-coherence occurrences, exact applied constraint claims, and one named frame; the Plain label retains DDD retrieval without adding a context bearer or any crossing to that identity
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.BoundedModelUseStructure.FPFCore.2026-07-25
  LineageEntries: DDD bounded-context wording retained as the Plain retrieval label; U.BoundedContext holon, boundary-container, semantic-frame-bundle, and crossing-bearing readings retired; any crossing belongs only to a distinct A.22 structure over already identified bounded model-use structures
  RefreshCondition: reopen when the A.1.1/A.22 membership or continuity rule, one of the three direct relation kinds, the exact constituent, selected-occurrence, applied-constraint, or frame discriminator, FPFCoreReferenceScheme, the current F.17 cell or row, or repeated container or crossing overreading changes
```

```text
NameCard:
  NameCardId: NC-MODEL-APPLICABILITY-RELATION
  GovernedValueRef: ModelApplicabilityRelation
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.1.1
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-MODEL-APPLICABILITY-RELATION.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseCellRef: SenseCell.ModelApplicabilityRelation.FPFCore.2026-07-25
  LocalSenseBasisRelationRef: LocalSenseBasisRelation.ModelApplicabilityRelation.FPFCore.2026-07-25
  TechLabel: ModelApplicabilityRelation
  PlainLabel: this model applies to this holon within this claim scope
  CandidateSet: relation-kind heads {ModelApplicabilityRelation, ModelAppliesToRelation, ModelScopeRelation}; claim-or-predicate heads {ModelApplicabilityClaim, ModelApplicabilityPredicate}; temporal head {ModelApplicabilityInterval}
  CandidateCoverage: direct ternary relation kind; readable predicate direction; claim or predicate neighbour; scope-membership neighbour; derived temporal-extent neighbour; no plausible live head family remains untested
  RejectedCandidates: ModelAppliesToRelation suggests a binary relation and hides the participating claim scope; ModelScopeRelation mistakes A.2.6 scope membership for model applicability; ModelApplicabilityClaim and ModelApplicabilityPredicate name epistemic or semantic content; ModelApplicabilityInterval names the derived maximal continuous extent
  SelectionRationale: the Tech label names the direct relation kind over one model episteme, exact holon, and participating claim scope; the Plain sentence exposes the predicate; applicability holds only when the A.1.1 predicate is satisfied, and the A.1.1 identity rule reidentifies the maximal continuous occurrence, leaving scope membership, assertion, interval, and structure separate
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.ModelApplicabilityRelation.FPFCore.2026-07-25
  LineageEntries: retains the A.1.1 relation-kind label; earlier broad applicable-model and context-boundary wording is not an alias; ModelApplicabilityInterval remains a local derived extent
  RefreshCondition: reopen when A.1.1 changes the participant kinds, applicability predicate, scope-alignment or model-scheme interpretation rule, temporal occurrence identity, FPFCoreReferenceScheme, the current F.17 cell or row, or the public receiving use
```

```text
NameCard:
  NameCardId: NC-MODEL-USE-RELATION
  GovernedValueRef: ModelUseRelation
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.1.1
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-MODEL-USE-RELATION.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseCellRef: SenseCell.ModelUseRelation.FPFCore.2026-07-25
  LocalSenseBasisRelationRef: LocalSenseBasisRelation.ModelUseRelation.FPFCore.2026-07-25
  TechLabel: ModelUseRelation
  PlainLabel: this assignment's holder uses this model during this work concerning this holon
  CandidateSet: relation-kind heads {ModelUseRelation, ModelUsageRelation, ModelApplicationRelation}; work-or-assignment heads {ModelUseWork, ModelUserRoleAssignment}; claim-or-record heads {ModelUseClaim, ModelUseRecord}
  CandidateCoverage: direct actual-use relation; availability-or-usage neighbour; applicability neighbour; Work neighbour; assignment neighbour; claim or record neighbour; no plausible live head family remains untested
  RejectedCandidates: ModelUsageRelation invites availability, access-count, or generic usage readings; ModelApplicationRelation collides with applicability and can suggest applying a method; ModelUseWork and ModelUserRoleAssignment name participants; ModelUseClaim and ModelUseRecord name epistemes about use
  SelectionRationale: the Tech label names the direct relation kind over one system-role-assignment occurrence, model episteme, performed Work occurrence, and use-locus holon; the Plain sentence exposes actual use by the derived assignment holder without adding that system as a fifth participant, while A.1.1 keeps applicability, assignment, Work, method application, claim, and record distinct
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.ModelUseRelation.FPFCore.2026-07-25
  LineageEntries: retains the A.1.1 relation-kind label; availability, mention, method application, performed Work, system-role assignment, and use-claim readings remain separate and are not aliases
  RefreshCondition: reopen when A.1.1 changes the participant kinds, F.6 performed-under-assignment prerequisite, actual-use predicate, actor derivation, maximal-continuous-use identity, FPFCoreReferenceScheme, the current F.17 cell or row, or the public receiving use
```

```text
NameCard:
  NameCardId: NC-MODEL-EXPRESSION-COHERENCE-RELATION
  GovernedValueRef: ModelExpressionCoherenceRelation
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.1.1
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-MODEL-EXPRESSION-COHERENCE-RELATION.ClaimGraph — complete C.2.1 U.ClaimGraph constituted by all identity-bearing naming-settlement claims designated below
  LocalSenseCellRef: SenseCell.ModelExpressionCoherenceRelation.FPFCore.2026-07-25
  LocalSenseBasisRelationRef: LocalSenseBasisRelation.ModelExpressionCoherenceRelation.FPFCore.2026-07-25
  TechLabel: ModelExpressionCoherenceRelation
  PlainLabel: this model content and this expression content satisfy this declared coherence criterion under this comparison scheme
  CandidateSet: relation-kind heads {ModelExpressionCoherenceRelation, ModelConformanceRelation, ModelImplementationRelation, ModelExpressionAlignmentRelation}; predicate-or-assessment heads {ModelExpressionCoherencePredicate, ModelExpressionCoherenceAssessment}
  CandidateCoverage: direct fixed-content relation; conformance neighbour; implementation or realization neighbour; weaker alignment neighbour; local predicate-value neighbour; evaluation or result neighbour; no plausible live head family remains untested
  RejectedCandidates: ModelConformanceRelation invites compliance or status readings and hides the declared criterion and permitted loss; ModelImplementationRelation suggests realization, production, or causation; ModelExpressionAlignmentRelation is weaker than the declared Boolean condition; ModelExpressionCoherencePredicate names the five-part criterion participant; ModelExpressionCoherenceAssessment names evaluation Work or a result episteme
  SelectionRationale: the Tech label names the participant-determined direct relation over one model episteme, expression episteme, admitted five-part predicate value, and comparison scheme; the Plain sentence exposes the truth test after either the same-scheme branch or the predicate-declared bridged branch is established, while maintenance, transformation, evaluation, result, evidence, and assertion remain separate
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.ModelExpressionCoherenceRelation.FPFCore.2026-07-25
  LineageEntries: retains the A.1.1 relation-kind label; earlier maintenance-alignment and implementation wording is narrowed to separate Work, transformation, evaluation, result, evidence, and assertion objects
  RefreshCondition: reopen when A.1.1 changes the participant kinds, five-part predicate-value membership, same-scheme or bridged-comparison branch, permitted-loss rule, participant-determined identity, FPFCoreReferenceScheme, the current F.17 cell or row, or the public receiving use
```

All four current cards use one `FPFCoreReferenceScheme` cell apiece and therefore add no Bridge or use claim. If a named current use relates different `<ReferenceScheme, LocalSenseClaim>` projections, apply the F.9 predicate to the possible Bridge, identify the affirmative bounded-use claim separately under C.2.1, and apply A.10 or B.3 to the relied-on evidence or assurance claim; without that use, add no Bridge or use claim. For `ModelExpressionCoherenceRelation`, an A.1.1 predicate may require an obtaining Bridge in its bridged interpretation branch; a receiving assertion or structure selection that relies on that occurrence still needs its own bounded-use claim and reliance path. None of those objects becomes part of a NameCard or public row.

#### F.18:4.2b - Current Role-Precision NameCards

The eight cards below make the accepted Core-facing names recoverable without making any named value obtain. They share `FPFCoreReferenceScheme` and use no Bridge: each card settles two designations for one value already defined or constrained by its subject pattern. Each card cites the stable E.10 token-class, allowed-use, and collision rules it actually consumes; a dated corpus audit or candidate-conformance result is publication evidence, not a NameCard currentness dependency.

```text
NameCard:
  NameCardId: NC-U-SYSTEM-ROLE-ASSIGNMENT
  GovernedValueRef: U.SystemRoleAssignment
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.2.1
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-U-SYSTEM-ROLE-ASSIGNMENT.ClaimGraph
  LocalSenseCellRef: SenseCell.U.SystemRoleAssignment.FPFCore.2026-08-09
  TechLabel: U.SystemRoleAssignment
  PlainLabel: assignment to a system role
  CandidateSet: U.SystemRoleAssignment; U.RoleAssignment; U.SystemAssignment; U.SystemRoleHoldingRelation
  RejectedCandidates: U.RoleAssignment leaves role ambiguous; U.SystemAssignment loses the assigned kind; U.SystemRoleHoldingRelation suggests possession
  SelectionRationale: Assignment names the relation family and SystemRole identifies the assigned local-kind family
  DeclaredUse: Core-facing citation of the retained direct assignment family and its directly declared species
  NonAdmissibleUse: no system-role kind, assignment record, field, occurrence, authority, responsibility, or Work follows from the name or card
  LexicalPrerequisiteRefs: E.10:7.5b KernelToken classification and allowed-use rule for U.SystemRoleAssignment; E.10:7.5a reserved-name collision rule
  BridgeRefs: none
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.U.SystemRoleAssignment.FPFCore.2026-08-09
  LineageEntries: U.RoleAssignment is retired as a positive Tech designation and remains only in marked lineage, rejection, or historical evidence
  RefreshCondition: reopen when A.2.1 changes the family, direct-species grammar, or participant rule; when FPFCoreReferenceScheme, the E.10 token classification or allowed-use rule, or the current F.17 cell or row changes; when a new collision appears under E.10:7.5a; or when repeated reader interpretation changes

NameCard:
  NameCardId: NC-KIND-USE-ADAPTATION-DECLARATION
  GovernedValueRef: KindUseAdaptationDeclaration
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: C.3.4
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-KIND-USE-ADAPTATION-DECLARATION.ClaimGraph
  LocalSenseCellRef: SenseCell.KindUseAdaptationDeclaration.FPFCore.2026-08-09
  TechLabel: KindUseAdaptationDeclaration
  PlainLabel: declaration of a local use of a kind
  CandidateSet: RoleMask; KindUseMask; KindUseProfile; KindUseAdaptationDeclaration
  RejectedCandidates: RoleMask suggests a system-role object; Mask hides the declaration episteme; Profile suggests a container or another governed kind
  SelectionRationale: the selected head exposes a declaration that adapts one named use of one exact base kind
  DeclaredUse: Core-facing citation of the C.3.4 declaration episteme family
  NonAdmissibleUse: no kind, assignment, scope, profile, system role, guard decision, or candidate judgment follows from the name or card
  LexicalPrerequisiteRefs: E.10:7.5b KernelToken classification and allowed-use rule for KindUseAdaptationDeclaration; E.10:7.5a reserved-name collision rule
  BridgeRefs: none
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.KindUseAdaptationDeclaration.FPFCore.2026-08-09
  LineageEntries: RoleMask is retired as a positive designation and remains only in marked lineage, rejection, or historical evidence
  RefreshCondition: reopen when C.3.4 changes the declaration identity, pinned inputs, or guard use; when FPFCoreReferenceScheme, the E.10 token classification or allowed-use rule, or the current F.17 cell or row changes; when a new collision appears under E.10:7.5a; or when reader interpretation changes

NameCard:
  NameCardId: NC-KIND-USE-ADAPTATION-CORRESPONDENCE-DECLARATION
  GovernedValueRef: KindUseAdaptationCorrespondenceDeclaration
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: C.3.4
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-KIND-USE-ADAPTATION-CORRESPONDENCE-DECLARATION.ClaimGraph
  LocalSenseCellRef: SenseCell.KindUseAdaptationCorrespondenceDeclaration.FPFCore.2026-08-09
  TechLabel: KindUseAdaptationCorrespondenceDeclaration
  PlainLabel: declaration of how two local ways of using kinds correspond and what is lost
  CandidateSet: MaskAdapter; KindUseAdaptationAdapterDeclaration; KindUseAdaptationMappingDeclaration; KindUseCorrespondenceDeclaration; KindUseAdaptationCorrespondenceDeclaration
  RejectedCandidates: Adapter suggests execution; Mapping can name a Method or representation; KindUseCorrespondenceDeclaration loses the endpoint family
  SelectionRationale: Correspondence names the declared rule and loss while Declaration keeps the object epistemic
  DeclaredUse: Core-facing citation of the C.3.4 cross-context declaration episteme family
  NonAdmissibleUse: no obtaining F.9 Bridge, executable adapter, mapping Method, representation correspondence, assignment, or target truth follows from the name or card
  LexicalPrerequisiteRefs: E.10:7.5b KernelToken classification and allowed-use rule for KindUseAdaptationCorrespondenceDeclaration; E.10:7.5a reserved-name collision rule
  BridgeRefs: none
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.KindUseAdaptationCorrespondenceDeclaration.FPFCore.2026-08-09
  LineageEntries: MaskAdapter is retired as a positive designation and remains only in marked lineage, rejection, or historical evidence
  RefreshCondition: reopen when C.3.4 changes the endpoint families, correspondence or loss content, or non-Bridge boundary; when FPFCoreReferenceScheme, the E.10 token classification or allowed-use rule, or the current F.17 cell or row changes; when a new collision appears under E.10:7.5a; or when reader interpretation changes

NameCard:
  NameCardId: NC-KIND-USE-ADAPTATION-JUDGMENT
  GovernedValueRef: KindUseAdaptationJudgment
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: C.3.4
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-KIND-USE-ADAPTATION-JUDGMENT.ClaimGraph
  LocalSenseCellRef: SenseCell.KindUseAdaptationJudgment.FPFCore.2026-08-09
  TechLabel: KindUseAdaptationJudgment
  PlainLabel: judgment of whether a candidate fits a local use of a kind
  CandidateSet: masked judgment; J_mask; KindUseJudgment; KindUseAdaptationJudgment
  RejectedCandidates: masked judgment and J_mask retain the old metaphor; KindUseJudgment loses the adaptation-declaration reading
  SelectionRationale: the selected name identifies the exact three-valued judgment family; J_kindUse remains local notation
  DeclaredUse: Core-facing citation of the C.3.4 three-valued result family
  NonAdmissibleUse: no declaration, candidate, guard disposition, evidence result, or kind-membership relation follows from the name or card
  LexicalPrerequisiteRefs: E.10:7.5b KernelToken classification and allowed-use rule for KindUseAdaptationJudgment; E.10:7.5a reserved-name collision rule
  BridgeRefs: none
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.KindUseAdaptationJudgment.FPFCore.2026-08-09
  LineageEntries: masked judgment and J_mask are retired positive designations; J_kindUse is declaration-local notation and receives no row
  RefreshCondition: reopen when C.3.4 changes the pinned inputs, truth-value set, or judgment identity; when FPFCoreReferenceScheme, the E.10 token classification or allowed-use rule, or the current F.17 cell or row changes; when a new collision appears under E.10:7.5a; or when reader interpretation changes

NameCard:
  NameCardId: NC-SYSTEM-ROLE-KIND-DESCRIPTION
  GovernedValueRef: SystemRoleKindDescription
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: F.4
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-SYSTEM-ROLE-KIND-DESCRIPTION.ClaimGraph
  LocalSenseCellRef: SenseCell.SystemRoleKindDescription.FPFCore.2026-08-09
  TechLabel: SystemRoleKindDescription
  PlainLabel: description of a system-role kind
  CandidateSet: RoleDescription; SystemRoleDescription; SystemRoleKindDescription; SystemRoleKindDescriptionEpisteme
  RejectedCandidates: RoleDescription is trigger-ambiguous; SystemRoleDescription leaves kind and assignment readings open; the Episteme suffix repeats the Description head
  SelectionRationale: Kind identifies the exact EntityOfConcern and Description identifies the episteme
  DeclaredUse: Core-facing citation of the F.4 description-episteme construction
  NonAdmissibleUse: no described kind, assignment, NameCard, row, publication form, or carrier follows from the name or card
  LexicalPrerequisiteRefs: E.10:7.5b KernelToken classification and allowed-use rule for SystemRoleKindDescription; E.10:7.5a reserved-name collision rule
  BridgeRefs: none
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.SystemRoleKindDescription.FPFCore.2026-08-09
  LineageEntries: RoleDescription is retired as a positive Tech designation and remains only in marked lineage, rejection, or historical evidence
  RefreshCondition: reopen when F.4 changes the described EntityOfConcern or description identity; when FPFCoreReferenceScheme, the E.10 token classification or allowed-use rule, or the current F.17 cell or row changes; when a new collision appears under E.10:7.5a; or when reader interpretation changes

NameCard:
  NameCardId: NC-SYSTEM-ROLE-ASSIGNMENT-STATE-RELATION
  GovernedValueRef: SystemRoleAssignmentStateRelation
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.2.5
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-SYSTEM-ROLE-ASSIGNMENT-STATE-RELATION.ClaimGraph
  LocalSenseCellRef: SenseCell.SystemRoleAssignmentStateRelation.FPFCore.2026-08-09
  TechLabel: SystemRoleAssignmentStateRelation
  PlainLabel: this assignment to a system role satisfies this state condition
  CandidateSet: RoleStateRelation; SystemRoleStateRelation; AssignmentStateRelation; SystemRoleAssignmentStateRelation
  RejectedCandidates: RoleStateRelation and SystemRoleStateRelation lose the assignment occurrence; AssignmentStateRelation is too broad
  SelectionRationale: the name identifies the direct relation between one exact assignment occurrence and one predicate value
  DeclaredUse: Core-facing citation of the A.2.5 direct relation kind and its exact occurrences
  NonAdmissibleUse: no state assertion, displayed status, predicate value, assignment, or obtaining occurrence follows from the name or card
  LexicalPrerequisiteRefs: E.10:7.5b KernelToken classification and allowed-use rule for SystemRoleAssignmentStateRelation; E.10:7.5a reserved-name collision rule
  BridgeRefs: none
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.SystemRoleAssignmentStateRelation.FPFCore.2026-08-09
  LineageEntries: RoleStateRelation is retired as a positive Tech designation and remains only in marked lineage, rejection, or historical evidence
  RefreshCondition: reopen when A.2.5 changes the relation participants, predicate, or identity; when FPFCoreReferenceScheme, the E.10 token classification or allowed-use rule, or the current F.17 cell or row changes; when a new collision appears under E.10:7.5a; or when reader interpretation changes

NameCard:
  NameCardId: NC-SYSTEM-ROLE-ASSIGNMENT-STATE-PREDICATE
  GovernedValueRef: SystemRoleAssignmentStatePredicate
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.2.5
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-SYSTEM-ROLE-ASSIGNMENT-STATE-PREDICATE.ClaimGraph
  LocalSenseCellRef: SenseCell.SystemRoleAssignmentStatePredicate.FPFCore.2026-08-09
  TechLabel: SystemRoleAssignmentStatePredicate
  PlainLabel: state condition for an assignment to a system role
  CandidateSet: RoleStatePredicate; SystemRoleStatePredicate; AssignmentStatePredicate; SystemRoleAssignmentStatePredicate
  RejectedCandidates: RoleStatePredicate and SystemRoleStatePredicate name the wrong subject; AssignmentStatePredicate is too broad
  SelectionRationale: the name identifies the truth-condition family over exact system-role assignments
  DeclaredUse: Core-facing citation of the A.2.5 predicate-value family
  NonAdmissibleUse: no relation occurrence, assertion, displayed result, state label, or assignment follows from the name or card
  LexicalPrerequisiteRefs: E.10:7.5b KernelToken classification and allowed-use rule for SystemRoleAssignmentStatePredicate; E.10:7.5a reserved-name collision rule
  BridgeRefs: none
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.SystemRoleAssignmentStatePredicate.FPFCore.2026-08-09
  LineageEntries: RoleStatePredicate is retired as a positive Tech designation and remains only in marked lineage, rejection, or historical evidence
  RefreshCondition: reopen when A.2.5 changes the truth condition, value family, or relation use; when FPFCoreReferenceScheme, the E.10 token classification or allowed-use rule, or the current F.17 cell or row changes; when a new collision appears under E.10:7.5a; or when reader interpretation changes

NameCard:
  NameCardId: NC-SYSTEM-ROLE-KIND-RELATION-STRUCTURE
  GovernedValueRef: SystemRoleKindRelationStructure
  GovernedValueKindRef: U.Structure
  SubjectPatternLocator: A.2.7
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NC-SYSTEM-ROLE-KIND-RELATION-STRUCTURE.ClaimGraph
  LocalSenseCellRef: SenseCell.SystemRoleKindRelationStructure.FPFCore.2026-08-09
  TechLabel: SystemRoleKindRelationStructure
  PlainLabel: structure of relations among system-role kinds
  CandidateSet: RoleRelationStructure; SystemRoleRelationStructure; SystemRoleKindRelationStructure; SystemRoleAssignmentRelationStructure
  RejectedCandidates: RoleRelationStructure is ambiguous; SystemRoleRelationStructure loses the kind substrate; SystemRoleAssignmentRelationStructure names the wrong substrate
  SelectionRationale: Kind identifies the substrate and Structure identifies the selected organization of exact obtaining relations
  DeclaredUse: Core-facing citation of the selected A.2.7 U.Structure construction
  NonAdmissibleUse: no assignment configuration, taxonomy episteme, graph, table, system collection, or structure occurrence follows from the name or card
  LexicalPrerequisiteRefs: E.10:7.5b KernelToken classification and allowed-use rule for SystemRoleKindRelationStructure; E.10:7.5a reserved-name collision rule
  BridgeRefs: none
  PublicRowStatus: current
  UnifiedTermRowRef: UTS.SystemRoleKindRelationStructure.FPFCore.2026-08-09
  LineageEntries: RoleRelationStructure is retired as a positive Tech designation and remains only in marked lineage, rejection, or historical evidence
  RefreshCondition: reopen when A.2.7 changes the substrate or selected-relation identity; when FPFCoreReferenceScheme, the E.10 token classification or allowed-use rule, or the current F.17 cell or row changes; when a new collision appears under E.10:7.5a; or when reader interpretation changes
```

Each card has one exact governed value and one selected Tech/Plain pair. No card is created for the `SystemRole` morphology, `J_kindUse`, a declaration-local slot, or a context field.

#### F.18:4.2c - Demonstrative wording without a fabricated value or scheme


A.22.CGUS:4.4 permits one exact C.2.1 episteme to show a traversal through an already qualified CGUS. It does not define a demonstrative-slice `U.Kind`, and `DemonstrativeUnfoldingSlice@Context` does not identify an exact slice by itself. The current sources also do not constitute `FPFSeminarTeachingReferenceScheme-2026-07-11` as a second by-value scheme whose interpretation differs from `FPFCoreReferenceScheme`.

Keep *demonstrative walkthrough* as ordinary readable wording when a sentence already makes the exact shown slice clear. Keep *mantra* as bounded seminar or pattern-local recall wording when repetition and attention are the point. Do not manufacture two NameCards, SenseCells, a Bridge, a bounded-use claim, or current F.17 rows from those phrases. No naming settlement or public-row status is current here.

If a later use needs stable citation of one exact slice, first recover that C.2.1 episteme from its claim content, the qualified CGUS it concerns, and its effective scheme. Then make one NameCard only if durable naming is useful. Add another card and a Bridge only if a second exact scheme-and-sense projection materially changes interpretation and one named correspondence use is current. Availability remains a separate E.24.PUB operation. `mantra move` stays E.10.MOVE Plain wording for a shown E.11.PUA continuation description; it is not a durable value or a second scheme.

#### F.18:4.2d - Pending R7 rule-content NameCard candidates
The following are candidate inputs, not current `NameCard` epistemes. Each uses the exact by-value `FPFCoreReferenceScheme`, keeps the governed `U.NameToken` separate from the R7 predicate or designation value it names, and creates no Bridge because the current comparison is within one scheme. E.10's exact TokenClass, reserved-name, and allowed-scope prerequisites remain unresolved, so `PublicRowStatus = pending` for all three and no `UnifiedTermRowRef` exists.

| Candidate expression | Exact local sense and governed value | Covered head families and rejected overread | Three-arena invariance | Reopen/close condition |
| --- | --- | --- | --- | --- |
| `SelectedRuleContentSubgraphDesignation` | use-relative designation resolving the exact nonempty base subgraph selected in one identified derivation or criterion-selection claim; governed node `SelectedRuleContentSubgraphDesignation@RuleContentBasisFindingDefinition-R7` | selected subgraph/designation, selected basis/reference, and rule-bearing classifier families were compared; reject intrinsic `RuleBearing...`, generic `Base`, and reference-only heads because the value is selection-relative and by-value | manufacturing assembly-rule selection; healthcare protocol-premise selection; cloud deployment-policy criterion selection | close only when exact `LEX.TokenClass`, `LEX.Reserved-Names`, and `LEX.AllowedScopes` values and assertions pass under `FPFCoreReferenceScheme`; reopen on R7 semantic or scheme change |
| `derivedUsingRuleContent` | predicate true only when an identified derivation claim used exact base content as a formal premise under a declared inference rule/application to produce exact dependent content; governed node `derivedUsingRuleContent@RuleContentBasisFindingDefinition-R7` | derived-using, derived-from, supported-by, and based-on families were compared; reject `derivedFrom` because source/provenance and semantic derivation are broader, and reject `supportedBy`/`basedOn` because they hide actual formal-premise use | manufacturing configuration derivation; healthcare dosage derivation with evidence kept separate; cloud configuration derivation | same lexical prerequisites as above, plus exact R7 predicate identity |
| `evaluatedAgainstRuleContent` | predicate true only when an identified criterion-selection claim selected exact base content for one bounded evaluation claim concerning exact dependent content; governed node `evaluatedAgainstRuleContent@RuleContentBasisFindingDefinition-R7` | evaluated-against, assessed-under, governed-by, and checked-with families were compared; reject `governedBy` and generic `checkedWith` because they hide criterion selection and can imply authority, Work, or tool use | manufactured configuration evaluation; healthcare protocol-conformance evaluation; cloud release evaluation against deployment policy while operational Work stays separate | same lexical prerequisites as above, plus exact R7 predicate identity |

A collision-free text search is useful evidence but does not substitute for the missing governed lexical values. Until closure, authors may quote these candidate spellings when discussing the R7 declaration, but must not cite a current NameCard or public term row.

#### F.18:4.3 - Candidate Selection

Do not pick a durable label in one stroke or work toward a fixed candidate count. Build the smallest set that covers at least two live head-term families and every plausible neighbouring-object reading that could change the decision. Stop when each live family has a representative and no untested plausible alternative could overturn the selection. If a deadline forces closure while a plausible family or alternative remains untested, record that exception in `CandidateCoverage` and make it part of `RefreshCondition`.

Judge candidates on:

- semantic fidelity: does the label preserve the governed value without adding or losing required conditions?
- reader ergonomics: can the intended reader recognize, say, and remember it in the current situation?
- morphology fit: does the word shape fit the kind being named, for example an exact local system-role kind, method, work, description, relation, slot, characteristic, or status value?
- alias risk: will a careful reader import a wrong sense from nearby FPF patterns or external practice?

Use these as ordinal comparisons. Do not average them into one score. If a Pareto-front or quality-diversity method is used, the dimensions and dominance rule must be visible on the card.

One candidate can win even when it is not perfect, but the `SelectionRationale` must say what it buys, what risk remains, and why the covered set is sufficient for this use.

#### F.18:4.4 - Public Term Rows

A durable local name needs no row. When public, Core-facing, durable-across-context, or cross-context reuse is current, test the then-current F.17 entry with the exact objects already recovered here. Public or durable reuse alone creates no Bridge.

The F.17 entry must be able to recover:

- the governed value and its kind;
- the locator for the pattern containing its defining or testing rule;
- the NameCard episteme and selected Tech and Plain designations;
- the effective by-value reference scheme, exact F.17 scheme-based SenseCell, and any separate local-sense basis relation;
- any F.9 Bridge that actually obtains.

If the row use relates different `<ReferenceScheme, LocalSenseClaim>` projections, its rationale or notes must cite the separate affirmative C.2.1 claim for the exact action, direction, rule, and tolerance, plus that claim's current A.10 or B.3 reliance. The result must contain one row for one naming decision and show both supported and blocked citation uses. If the entry cannot do this, keep the durable name and NameCard local and mark the public row pending. Do not repair or emulate the missing row inside F.18.

#### F.18:4.4.1 - Cross-Projection Use and Reliance

Open this branch only when one named reuse must relate different `<ReferenceScheme, LocalSenseClaim>` projections. Compare the exact F.17 cells. Another expression under the same projection is a designation question and gets no Bridge. Different projections open the F.9 question; a different scheme is only one way projections can differ and proves no relation. Test the F.9 predicate and cite a Bridge only when it actually obtains. With no current correspondence use, create no Bridge or use claim regardless of scheme count.

State the proposed naming use in a separate current C.2.1 claim whose EntityOfConcern is that Bridge. Record the action, direction, correspondence rule, tolerated loss, and polarity.

Then choose the reliance route. For ordinary bounded reliance below B.3's threshold and with no assurance claim, use the exact A.10 evidence-provenance relation and `RelianceDisposition=pass`. When an assurance claim is made or the B.3 threshold is met, follow B.3's first-claim decision: require a current positive claim with sufficient record or a disposition that stops or narrows the use. The threshold creates no positive claim. Neither route authorizes the use or proves that it occurred.

If the reuse did occur, recover its actual Work under A.15.1, assertion episteme under C.2.1, publication occurrence under E.24.PUB, direct relation under its own predicate, operation application under A.6.1, or other exact result under its direct rule. Name a `BoundedModelUseStructure` only when that selected structure changes the sense or naming use. Until the Bridge, separate claim, and required reliance are current, keep the names local or record the unresolved alignment. A reference-scheme or model-use-structure difference alone supplies neither a premise nor governed-value identity.

### F.18:5 - System-Role-Kind, Assignment, Slot, and Status Naming Settlement


This settlement keeps naming aligned with the object already recovered. Bare *role* is a trigger handled by `E.10.ROLE`, not a reusable kind head.

#### F.18:5.1 - System-Role-Kind Names

A durable system-role-kind name designates one exact local kind admitted through C.3 and A.2. Recover that kind through its candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. A practice or source reference can locate the definition or signal that two definitions should be compared; it does not identify the kind. Candidates are entities already admitted under A.1 as `U.System`, including a person, team, organization, or non-human technical object. The Tech designation normally ends in `...SystemRole`, for example `ReviewerSystemRole`, `ShipbuilderSystemRole`, or `ServiceProviderSystemRole`. `SystemRole` is compound morphology, not a universal governed value. The name creates no system admission, kind membership, assignment, agency, capability, or Work.

A system-role-kind name must not include:

- the holder of an assignment or the assignment occurrence;
- capability evidence or skill level;
- method or method-family selection;
- performed Work;
- status value or gate result;
- source, evidence, publication, or assurance use.

If a phrase such as `SeniorReviewer`, `NightOperator`, or source wording such as *evidence role* appears, recover the current claim first. The result may be an exact local system-role kind, one direct assignment occurrence, a status assertion, an evidence-use relation, a Work admission condition, another governed value, or a local source phrase. Do not force all of them into one system-role-kind name.

#### F.18:5.2 - System-Role-Assignment Names

A system-role-assignment name designates one already recoverable obtaining occurrence of an exact direct species under `U.SystemRoleAssignment` and A.2.1; the system-role-kind name does not identify that occurrence. Recover the admitted holder system, the exact assigned local system-role kind, and only additional participants needed to distinguish that direct species. A taxonomy, reference scheme, description, display, or generic context episteme is not a mandatory assignment participant. Assignment extent follows uninterrupted predicate truth; an assertion or occurrence-description episteme may state a known interval separately. A durable assignment name uses a `NameCard` whose `GovernedValueRef` resolves to that occurrence. If public or cross-context reuse is needed, apply section 4.4; until it passes, retain the card locally and mark the row pending. Neither a name, card, row, nor publication occurrence makes the assignment obtain.

`Holder#Role:Context@Window` is source notation only. Recover the holder System, local system-role kind, assignment occurrence and its declared species when one exists, and any separately applicable context, schedule, interpretation, or Work relation. The source token is neither a Tech name nor proof of assignment, capability, or performed Work.

#### F.18:5.3 - Capability, Method, and Work Names

Keep these separate:

- `ShipbuilderSystemRole` names one exact local system-role kind;
- `ShipbuildingCapability` names a capability of an admitted `U.System`, including an acting holon admitted as a system for that capability claim;
- `ShipbuildingMethod` names a method or method family;
- `HullAssemblyWork` names a work family or planning-level work label until an exact performed occurrence is current.

A role-derived or role-method-coupled expression is only a naming cue. First recover the exact value it refers to. If that value is an exact Method or Method family under A.3.1, choose a Method name. If it is an exact `U.MethodDescription`, `U.WorkPlan`, or dated `U.Work` occurrence, name that description episteme, plan episteme, or occurrence separately under A.3.2, A.15.2, or A.15.1; those names are not Method names. If the expression refers to another value, use the rule that defines or tests that value. Only then use F.18 to choose a durable name. An exact relation involving a system-role kind or assignment may constrain who may use a Method or perform Work; it neither creates nor names the Method, description, plan, or Work occurrence.

Treat an action nominal such as `testing`, `assembly`, `maintenance`, `evaluation`, or `inspection` as a morphology cue, not a governed kind. Placement in function- or flow-structure prose identifies no `U.Function`. If the function-like use remains claim-bearing while its exact object or relation is hidden, apply `A.6.F`; if it is already recoverable, name the exact method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, performed-work occurrence, or other governed value under the rule that defines or tests it. Only then use F.18 to choose a durable name. A WBS element, activity, or Work Package remains plan- or assignment-episteme content about intended work; none of these uses identifies a performed Work occurrence admitted under `U.Work`.

A durable name for performed Work points to one dated occurrence already grounded under `A.15.1`. An action word, plan row, local work-family label, or `U.WorkPlan` does not create that occurrence or an assignment.

Every system claimed as a performer must already be admitted as a `U.System`. For each performer, a current assignment covers the Work interval, names that system as its holder, and retains every participant required by its declared `U.SystemRoleAssignment` species. F.6 links the Work to that assignment. The Method actually used, temporal extent, containing system, affected referent, and material bindings and resource-use facts are also recoverable. A compact naming account cites only the identities needed by its receiving use; leaving an identity out of the account does not make the underlying fact optional. Add a continuity policy only when interruption, retry, a changed Method or binding, or competing designators make occurrence identity material.

Keep neighbouring direct subject and resource-use claims, `A.15.PROD` production claims, measurement-result epistemes, evaluation results, `C.11` choices or decisions, delivery occurrences, acceptance verdicts, and downstream-effect claims separately named under their direct patterns.
When the underlying boundary wording still hides the relation, apply `A.6.P.WMR`. Use `F.18` only after an exact governed value and its use are recovered through a direct subject relation, an exact `A.6.1` application binding, or an exact local `A.15.PROD`/`A.6.RCD` claim. An exact non-assertability result independently records `factually unsupported`, `missing-information`, or `missing-governor`; none authorizes durable naming, and only `missing-governor` is an ontology blocker that names the affected use and future subject pattern or relation declaration. This section selects and tests a name. It does not define a second work-occurrence or work-result recovery algorithm.

Method-relation and method-composition names are method-side names too. If a phrase names serial composition, parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, fallback, or dispatch among methods, first decide which object the phrase names.

- If admitted submethods make one composite way of doing, name the composite `U.Method`. Use A.3.1 for that Method and B.1.5 or another direct composition pattern for its exact composition relation.
- If the phrase names relations among methods without making one whole Method, name the relations first. When a named use depends on how several such relations are organized, select that `U.Structure` under A.22 and designate it `MethodRelationStructure`; state the question and prohibited overread that bound the selection. Identify and constrain each included method-side relation—for example, composition, refinement, substitution, iteration, decomposition, family membership, selection, or fallback—through its A.3.1, G.5, or other defining rule. A claim-bearing episteme that describes such a relation remains separate under C.2.1, and any Work-use relation remains under A.15.
- If the current object is a separately identified episteme that describes one exact admitted Method, `A.3.2` may classify it as `U.MethodDescription`; F.18 names that episteme separately from the Method.
- If an episteme instead describes the selected relation structure, `C.2.1` keeps that structure as its exact `EntityOfConcern`; the episteme is not thereby a `U.MethodDescription`.

F.18 settles a durable name only after one of those exact objects has been recovered. Algebraic, graph, categorical, process-calculus, matrix, embedding, distributed, or neural notation names the lens or representation only when that lens is the governed value.

#### F.18:5.4 - System-Role-Kind Relations, Method Relations, System-Role–Method Relations, and Lens Names

System-role-kind-relation expressions remain ordinary expressions or direct relations unless their exact local kinds and relation predicates are already admitted. An algebraic, graph, matrix, embedding, distributed, or neural description is a lens over the selected `SystemRoleKindRelationStructure`; it is not automatically the named kind, holder, assignment, Method, or Work.

First recover what the name is for:

| Expression or source phrase | What can be named | Naming rule |
| --- | --- | --- |
| `R1 <= R2` | one exact directional admission-substitution relation occurrence between two independently admitted local system-role kinds, identified by the ordered kinds, receiving-use rule, applicability, and only meaning-changing semantic-basis editions | Name or cite the exact relation occurrence or a selected `SystemRoleKindRelationStructure`; keep any assertion or policy record, current assignment, receiving check, and outcome separate. Admit another system-role kind only when its own C.3 identity and membership basis warrant it. |
| `R1 incompatibleWith R2` | one exact symmetric incompatibility relation occurrence between two independently admitted local system-role kinds, identified by the unordered pair, same- or different-holder rule, Work identity, overlap test, applicability, and only meaning-changing semantic basis | Name or cite the exact relation occurrence or a selected `SystemRoleKindRelationStructure`, not another system-role kind. Exact assignments and the receiving Work remain separate inputs and do not replace the two kind participants. |
| `R1 and R2` | two independently admitted system-role kinds; any assignment occurrences are separate and are required only when the receiving sentence also claims them | Use “and” in ordinary prose. Keep the two kind claims recoverable, and do not infer assignments or make a compound kind by hyphenating the labels. |
| `R1 bundle R2`, or quoted source shorthand `RoleBundle := R1 and R2` | one order-insensitive finite-set relation among exact system-role kinds, with a joint-admission and holder-allocation predicate | Keep it as a bundle relation. A convenient bundle name does not admit a compound system-role kind; such a kind would need its own independent C.3 identity and use. |
| `R1` qualified by a domain, practice, Method family, or ordinary work field | either one independently admitted local system-role kind or a residual A.2.7 qualification relation between two kinds | Before naming a kind, recover its C.3 candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. A domain, practice, ordinary work field, Method, Work family, or performed Work occurrence remains a separate value or comparison cue. Keep a non-monotonic restriction as its exact relation and do not infer admission substitution. |
| Method-like phrase derived from a system-role label | Method, Method family, MethodDescription, WorkPlan, or Work occurrence | Name the recovered object through `A.3.1`, `A.3.2`, or `A.15`; cite the exact system-role-kind relation separately when it constrains admission or performance. |
| algebraic, graph, matrix, embedding, distributed, or neural representation of system-role kinds or their relations | mathematical or representation description of a selected `SystemRoleKindRelationStructure` | Name the lens only when the representation itself is the object being named; otherwise name the recovered kind, relation occurrence, selected structure, Method, assignment, or Work. |
| Method algebra, Method graph, Method matrix, process calculus, selector calculus, or Method embedding | mathematical or representation description of exact method-side relations or their selected `MethodRelationStructure` | Name the lens only when the representation itself is the object being named; otherwise name the exact relation, selected structure, Method family, MethodDescription, WorkPlan, Work occurrence, or neighboring relation. |

Ordinary speech may say “surgeon”, “reviewer”, or “operator” when the local sentence makes the intended system-role kind or assignment obvious. Use the concrete `...SystemRole` designation when stable technical reference to the kind is needed. Do not infer kind identity, assignment, relation, Method, capability, or Work from the ordinary word alone. Add a qualifier only when it distinguishes a live neighboring reading.

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

Do not name these as system-role kinds or assignments unless that separate work-facing classification or direct assignment occurrence is actually current. “This standard plays the role of evidence” is repaired to the appropriate evidence-use, source-use, or status-use relation; it is not an assignment of the standard.

#### F.18:5.6 - Relation, Slot, Interface, Port, and Signature Names

If a name touches relation, slot, interface, port, boundary, protocol, API, or signature wording, use `A.6.RSIR` and subject patterns.

- Use A.6.5 for relation slot discipline and `SlotSpec` declarations.
- Use A.6.0 for signatures and law-defined declarations.
- `A.6.M` and architecture patterns define or constrain module interfaces and architecture interfaces.
- `A.6.F`, transformation, and architecture patterns define or constrain functional ports and functional structures.
- `A.6.C`, protocol, service-access, and commitment patterns define or constrain API, protocol, and service-access cases.
- Use C.2.1 for the identity and content of a claim-bearing interface-description episteme.
- Use E.17 for a multi-view publication face or form.
- Use E.24.PUB for availability of the selected edition and for the separate form-expression and carrier-bearing relations.

Before naming a relation-facing object, keep these settlements distinct:

| Object to name | Required prior settlement |
| --- | --- |
| reusable predicate-definition episteme | An `A.6.RCD` result records a reusable definition and `C.2.1` gives it one truthful exact `EntityOfConcern`; the name denotes the definition, not a relation kind |
| derived or primitive relation kind | `A.6.RCD`, `E.24`, and `E.24.UK` have admitted the kind and its direct subject pattern states obtaining, applicability, and occurrence identity |
| one obtaining relation occurrence | the subject pattern establishes obtaining and `A.6.REL` applies the admitted kind's identity rule |
| formula, query, path, graph, diagram, or other representation element | `C.29` states what it represents and the relevant correspondence; its name does not name the represented relation by default |
| designator or reference | the exact designation or reference relation resolves to the already settled object under its reference scheme |

One token may be reused only where the reference scheme and local sense preserve these distinctions; it cannot collapse definition, kind, occurrence, representation, and designator into one object.

`F.18` can settle a durable name for the recovered value. It does not decide which value the interface word names, create a public row, or make that row available.

Words such as *member*, *membership*, *belongs to*, and *in* do not by themselves identify one reusable relation. First use `E.10` to recover whether the sentence concerns mathematical inclusion, kind classification, relation participation, collection belonging, or constructive parthood. For a collection, an ordinary sentence such as “this edition belongs to this product series” is enough unless another use needs a reusable relation name. Name a reusable predicate only under the pattern that states who or what may belong, what makes belonging begin and end, and how recurrence and past belonging are handled. Do not create a `NameCard` or public name for generic `MemberOf` merely to abbreviate the ordinary sentence.

### F.18:6 - What Belongs In The Label

Belongs in the label:

- a head word that helps readers recognize the governed value;
- a stable qualifier that is part of the local sense;
- `SystemRole` morphology only when the governed value is one exact local system-role kind;
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

#### F.18:7.1 - System-Role Kind, Assignment, Capability, Method, and Work

A shipyard team wants one reusable name for the local system-role kind used in shipbuilding Work. It first separates the values that the source word *shipbuilder* could hide.

Recovered values:

- `ShipbuilderSystemRole`, one local C.3 kind whose admitted-system candidates count when they satisfy the current shipbuilding condition; the member/non-member probes and continuity rule expose the boundary, while the ShipyardProduction source only locates the definition;
- one direct assignment occurrence under A.2.1 whose admitted holder system and assigned `ShipbuilderSystemRole` kind are explicit, while any work area, schedule, interpretation, or reference scheme remains separate unless that direct species needs it for occurrence identity;
- `ShipbuildingCapability` with envelope and measures under the capability pattern;
- `ShipbuildingMethod` or a method family under A.3.1; if a separately identified `ShipbuildingMethodDescription : U.MethodDescription` episteme is current, name it separately under A.3.2 only when its exact `EntityOfConcern` is that Method;
- `HullAssemblyWork` under the Work patterns.

Here `HullAssemblyWork` is a work-family label or a label in a plan or assignment episteme. A designator such as `HullAssemblyWork-42@2026-07-15T09:10–11:35` names performed Work only when the record recovers the complete occurrence. Every named performer is an admitted system. For each performer, a current assignment covers the Work interval, names that system as its holder, and retains every participant required by its declared `U.SystemRoleAssignment` species. F.6 links the Work to that assignment. The record also recovers the Method actually used, temporal extent, containing system, affected hull referent, material bindings and resource-use facts, plus an applicable continuity policy when disambiguation is current. The compact naming account may cite only identities needed by the current use, but the omitted facts must still be true. A changed hull state, measurement result, evaluation verdict, delivery occurrence, or acceptance verdict remains a separately defined and separately named value.

The local card is:

```text
NameCard:
  NameCardId: NameCard.ShipbuilderSystemRole.ShipyardProduction.2026
  GovernedValueRef: ShipbuilderSystemRole
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.2 with C.3
  ReferenceScheme: Shipyard-Production-Scheme
  ClaimContent: NameCard.ShipbuilderSystemRole.ShipyardProduction.2026.ClaimGraph
  LocalSenseRef: local expression `shipbuilder (system role)`; sense claim: the C.3 kind whose admitted-system candidates satisfy the current shipbuilding condition, member/non-member boundary, and continuity rule; ShipyardProduction provenance locates this settlement but does not identify the kind
  LocalSenseBasisRelationRef: absent; no independent local-sense basis relation is current
  TechLabel: ShipbuilderSystemRole
  PlainLabel: shipbuilder (system role)
  CandidateSet: ShipbuilderSystemRole; ShipbuilderRole; ShipbuilderSystemRoleKind; ShipbuildingCapability; HullAssemblyWorker; CertifiedShipbuilder
  CandidateCoverage: system-role-kind head; ambiguous role head; redundant kind suffix; capability head; holder-or-work head; certification-or-status head
  RejectedCandidates: ShipbuilderRole; ShipbuilderSystemRoleKind; ShipbuildingCapability; HullAssemblyWorker; CertifiedShipbuilder
  SelectionRationale: the selected label designates the already recovered local kind without claiming admission, assignment, capability, performed Work, or certification
  BridgeRefs: absent; this local settlement makes no semantic-correspondence claim
  PublicRowStatus: localOnly
  UnifiedTermRowRef: absent
  LineageEntries: `ShipbuilderRole` is retained only as predecessor wording; source word `shipbuilder` remains ordinary where no stable kind reference is needed
  RefreshCondition: reopen if the local kind identity changes or repeated readers infer a non-human-only system, admission, assignment, agency, capability, or Work from the name
```

The candidates execute the section 4.3 stopping rule: each live head family is represented, and the recovered Method and Work objects are not synonyms for the local kind. If public or cross-context reuse becomes current, apply section 4.4; until it passes, keep this card local.

#### F.18:7.1a - Reviewer in a Journal Context

`ReviewerSystemRole` designates the local kind whose admitted-system candidates count when they supply a substantive review judgment that meets the current JournalReview acceptance conditions. The candidate range, operative condition, member/non-member probes, and continuity rule recover the kind; JournalReview-2026 provenance only locates the definition. A review assignment, responsibility, authority, capability, permission, and performed review Work remain separate claims.

```text
NameCard:
  NameCardId: NameCard.ReviewerSystemRole.JournalReview.2026
  GovernedValueRef: ReviewerSystemRole
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.2 with C.3
  ReferenceScheme: FPFCoreReferenceScheme
  ClaimContent: NameCard.ReviewerSystemRole.JournalReview.2026.ClaimGraph
  LocalSenseRef: local expression `reviewer (system role)`; sense claim: the C.3 kind whose admitted-system candidates satisfy the current substantive-review condition, member/non-member boundary, and continuity rule; JournalReview-2026 provenance locates this settlement but does not identify the kind
  TechLabel: ReviewerSystemRole
  PlainLabel: reviewer (system role)
  CandidateSet: ReviewerSystemRole; ReviewerRole; ReviewerSystemRoleKind; ReviewerSystemWorkRole; reviewer
  RejectedCandidates: ReviewerRole; ReviewerSystemRoleKind; ReviewerSystemWorkRole
  SelectionRationale: `SystemRole` exposes the system-classification reading; `Kind` is already stated by `U.Kind`, while `Work` would add a false occurrence claim
  BridgeRefs: absent
  PublicRowStatus: localOnly
  UnifiedTermRowRef: absent
  LineageEntries: `ReviewerRole` is predecessor wording only; ordinary `reviewer` remains available when no stable technical reference is needed
  RefreshCondition: reopen on a changed local kind or repeated non-human-only, admission, assignment, agency, capability, participation, or Work overread
```

No F.17 row is created without a named public or cross-local reader use.

#### F.18:7.2 - Engineer-Roboticist and Musician

A lab says: “Vasya is an engineer, does robot engineering, is therefore an engineer-roboticist. These are musical robots, and Vasya is also a musician, performs music, and teaches robots music.”

Recovered values:

- Vasya as an admitted system; `MusicalRobotLab_2026` is the lab and Work locus in its direct relations, not a generic assignment participant;
- `RoboticsEngineerSystemRole`, one local system-role kind whose admitted-system candidates count when they satisfy the current robotics-engineering condition, boundary probes, and continuity rule; MusicalRobotLab provenance locates the definition but does not identify the kind;
- robotics as the qualification that distinguishes this local engineering kind, with any non-monotonic restriction retained as a separate A.2.7 relation;
- `MusicianSystemRole` as another exact local kind when its own music-performance condition and boundary matter separately;
- any current engineering or musician assignments as occurrences of their declared A.2.1 species;
- robot-engineering Method or Work, music-performance Work, and robot-music-teaching Method or Work under their direct patterns;
- an optional algebraic, graph, matrix, embedding, or neural representation only if the project actually uses that lens to describe the selected system-role-kind relation structure.

If the exact robotics-qualified local kind has been admitted, its local naming settlement is:

```text
NameCard:
  NameCardId: NameCard.RoboticsEngineerSystemRole.MusicalRobotLab.2026
  GovernedValueRef: RoboticsEngineerSystemRole
  GovernedValueKindRef: U.Kind
  SubjectPatternLocator: A.2 with C.3 and A.2.7 for the separately current qualification relation
  ReferenceScheme: MusicalRobotLab-Scheme
  ClaimContent: NameCard.RoboticsEngineerSystemRole.MusicalRobotLab.2026.ClaimGraph
  LocalSenseRef: local expression `engineer-roboticist`; sense claim: the C.3 kind whose admitted-system candidates satisfy the current robotics-engineering condition, member/non-member boundary, and continuity rule; MusicalRobotLab provenance locates this settlement but does not identify the kind
  LocalSenseBasisRelationRef: absent; no separate source-bearing basis relation is current for this use
  TechLabel: RoboticsEngineerSystemRole
  PlainLabel: engineer-roboticist
  CandidateSet: RoboticsEngineerSystemRole; RoboticsEngineerRole; engineer-roboticist; robotics engineer; engineer and roboticist; RobotEngineeringMethod; engineer-roboticist-musician
  CandidateCoverage: system-role-kind head; ambiguous role head; two ordinary expressions; method neighbour; compressed multi-kind neighbour
  RejectedCandidates: RoboticsEngineerRole; engineer and roboticist; engineer-roboticist-musician; RobotEngineeringMethod
  SelectionRationale: the Tech label exposes one local system-role kind; the Plain label preserves recognizable lab speech; musician classification or assignment, Method, and Work remain separate
  BridgeRefs: absent; the card makes no semantic-correspondence claim
  PublicRowStatus: localOnly
  UnifiedTermRowRef: absent
  LineageEntries: `RoboticsEngineerRole` is predecessor wording only; ordinary `robotics engineer` remains available in local prose when no stable technical reference is needed
  RefreshCondition: reopen if the local kind or A.2.7 qualification changes, or readers merge musician classification or assignment, Method, or Work into this name
```

If no durable qualified kind is admitted, keep *engineer-roboticist* as local ordinary wording rather than filling the card. Ordinary project communication may say “Vasya is our engineer-roboticist and musician” when the separate claims about his engineering and musicianship remain recoverable; any assignment is another claim. Name a current Method, MethodDescription, or performed Work through A.3.1, A.3.2, or A.15.1. If public reuse becomes current, apply section 4.4; do not infer an F.17 row from this local card.

#### F.18:7.2a - Method Relation Structure and Method Algebra Name

A lab says: "Use the robot-engineering method algebra: choose scouting, then calibration, then training; fall back to teleoperation if training fails."

Recovered values:

- one or more robot-engineering methods or method families under `A.3.1`;
- a method-family registry or selector outcome under `G.5` when the family registry or selector result is current;
- `MethodRelationStructure` for the named `MusicalRobotLab_2026` use when the current claim concerns serial composition, guarded fallback, or family selection among exact methods;
- a method description when the source notation describes that structure;
- a `C.29` mathematical-lens use when "algebra" is the selected representation for checking composition, fallback, or preserved/lost structure;
- work plan or dated work only when a concrete plan or occurrence is current.

F.18 settlement: `RobotEngineeringMethod` names a Method or method family only when that is the governed value. `RobotEngineeringMethodRelationStructure` may name the selected method relation structure when durable naming is needed. `RobotEngineeringMethodAlgebra` names the lens only when the algebraic representation itself is the governed value. Do not use a system-role-kind label such as `RoboticsEngineerSystemRole` to name the method relation structure, and do not use *method algebra* to hide a WorkPlan or performed Work.

#### F.18:7.3 - Evidence-Like Source Phrase

A review table contains the phrase "model card evidence role".

Recovered values:

- a model-card episteme;
- an evidence-use relation to a target claim;
- possible source-currentness and assurance-use relations;
- no system-role kind, assignment, or acting system merely because the episteme is used as evidence.

F.18 settlement: no system-role-kind or assignment name is minted. If a public term is needed, first name the exact evidence-use relation, for example `ModelCardEvidenceUse`, with A.10 as its direct pattern. Then apply the section 4.4 gate; until it passes, retain the durable relation name and NameCard locally and mark the public row pending.

#### F.18:7.4 - Interface-Like Source Phrase

A software team says "the payment interface owns customer identity".

Recovered candidates:

- module interface under `A.6.M`;
- API description or protocol under `A.6.C`;
- signature or SlotSpecs under `A.6.0` and `A.6.5`;
- claim-bearing interface description under `C.2.1`;
- multi-view publication face or form under `E.17`;
- publication availability, form expression, or carrier bearing under `E.24.PUB`;
- a system-role assignment under A.2.1 only when an occurrence belongs to a declared species, has an admitted System as holder, and has the local kind as assigned-kind value; any responsibility or authority relation remains separate.

F.18 settlement: do not mint `PaymentInterfaceRole`. First recover which governed value the phrase names. Then name that value through its subject pattern.

#### F.18:7.5 - Cross-Context Name

Two teams use `component`, `module`, and `unit` for nearby meanings.

Recovered values:

- structural component under architecture and part-whole patterns;
- deployable module under module-interface patterns;
- management unit under organizational patterns.

F.18 settlement: first keep the three recovered values and their local labels separate. If only local speech is needed, stop there; do not name a claim merely because one team wants to explain the difference. If a public term use is proposed between different `<ReferenceScheme, LocalSenseClaim>` projections, identify the exact source and receiving F.17 cells and test the F.9 Bridge predicate between them. The same scheme with different `LocalSenseClaim` values qualifies; a different scheme only opens the question and never establishes the relation. When the Bridge obtains, state in ordinary C.2.1 wording whether it is suitable for this naming use, naming the direction, label-correspondence rule, tolerated loss, and polarity, and establish the current A.10 or B.3 reliance required by section 1. The Bridge does not choose the Tech label, the claim does not identify the governed value, and neither authorizes or performs publication. Only after those objects are current should the practitioner apply F.17 as specified in section 4.4. If the F.17 gate fails, keep the name and card local and mark the row pending; if no correspondence use is current, stop with the local settlement and create no Bridge or use claim regardless of scheme count.

### F.18:8 - Anti-Patterns And Repairs

| Anti-pattern | Ontological failure | Repair |
| --- | --- | --- |
| "Same spelling means same value." | Treats string identity or a sense Bridge as governed-value identity and lets the Bridge silently license reuse. | Compare the exact `<ReferenceScheme, LocalSenseClaim>` projections. Same projection plus another expression stays with designation. Different projections open the F.9 question; only an obtaining Bridge can then support a separate C.2.1 naming-use claim with current A.10 or B.3 reliance. Apply the direct object subject pattern for any governed-value identity claim, or keep the values separate. |
| “Evidence role” for a report, source, or standard. | Turns an episteme or source-use relation into a work-facing classification or assignment. | Recover evidence-use, source-use, status-use, publication-use, or assurance-use relation. |
| “Night operator role” when only schedule differs. | Bakes temporal admission into local-kind identity. | Keep the exact operator system-role kind; put the time window in the assignment, status, or WorkPlan. |
| “Certified engineer role” when certification is evidence or admission. | Bakes capability evidence or admission into the kind name. | Keep `EngineerSystemRole` only when that exact local kind is admitted; record capability evidence, admission, or status relation separately. |
| “Role-derived method” treated as a role-relation result. | Confuses role wording with Method identity. | Name the Method or Method family under A.3.1. If a separately identified `U.MethodDescription` episteme is current, name it separately under A.3.2 only when its exact `EntityOfConcern` is that Method; cite the exact system-role-kind or assignment requirement separately when it is current. |
| "Method algebra" treated as the method or plan. | Confuses a mathematical or representation lens with exact method-side relations, their optional A.22-selected `MethodRelationStructure`, a MethodDescription, WorkPlan, or performed Work. | Before naming, recover the exact relation, optional selected structure, method description, `C.29` lens use, work plan, or work occurrence through the rule that identifies or tests that value. |
| Action nominal, WBS element, or Work Package treated as performed work. | Function/method morphology or intended-work content is mistaken for one dated occurrence; a nearby result is folded into the work name. | Recover the exact `A.15.1` occurrence basis, apply `A.6.P.WMR` if the relation is still hidden, and name neighboring production claims, measurement results, evaluation results, delivery occurrences, and acceptance verdicts separately. |
| Role-looking interface wording for API, port, or boundary. | Uses role morphology to avoid recovering port, signature, boundary, or interface-specific relation. | Use `A.6.RSIR` and the subject-pattern locator; name the recovered relation, signature, port, or bounded interface value only when its exact admission predicate is satisfied. |
| "Unscoped glossary." | A glossary episteme carries or lists words without an exact governed value and kind, by-value reference scheme, local sense, and any actually needed Bridge. | Use a `NameCard` for a durable local settlement. Open a public row only through the section 4.4 gate. When availability is current, use an `E.24.PUB` publication occurrence to make the selected row or glossary edition available through a distinct form and carrier. |

### F.18:9 - Conformance Checks

Use these checks before a durable name is reused in a pattern. If an F.17 row is current, run its own row checks after the section 4.4 gate; these F.18 checks neither create that row nor establish a publication occurrence for it.

| Check | Passing condition |
| --- | --- |
| Governed value | The named value is recoverable and belongs to a subject pattern. |
| Interpretation | The effective `U.ReferenceScheme` is carried by value and the local sense is named; model-use structure, claim scope, project work, and other locality relations remain separate. |
| Kind | The kind is not inferred from spelling, source, or practice. A system-role kind is already recoverable through its candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. |
| Candidate set | The smallest set covers at least two live head families and every plausible neighbouring-object reading; any forced untested exception is explicit in `CandidateCoverage` and `RefreshCondition`. |
| System-role boundary | System-role kind, classification, assignment, holder, capability, Method, Work, evidence, status, participant meaning, declaration place, and representation position are not collapsed. |
| Relation-object boundary | Predicate-definition episteme, admitted relation kind, obtaining occurrence, representation element, and designator are named only after their separate settlements; relation slot, interface, port, and signature names cite the applicable direct patterns. |
| Public row | A durable local card is enough unless public, Core-facing, durable-across-context, or cross-context reuse is current. The section 4.4 gate passes before any F.17 row is cited; the row is neither the value nor the publication occurrence. |
| Bridge and bounded use | Apply the F.9 predicate only to exact local senses whose `<ReferenceScheme, LocalSenseClaim>` projections differ. Same projection plus another expression is designation; same scheme plus another claim can open the F.9 question; scheme difference opens only the question; no current correspondence use creates no Bridge or use claim. A separate C.2.1 claim says whether an obtaining Bridge suits the named naming use, and A.10 or B.3 supplies the reliance rule. None authorizes or proves that reuse occurred. |
| Local-plain non-use | A one-off claim about whether an exact Bridge suits a named use stays in ordinary wording. No `NameCard`, public claim kind, or durable CamelCase name is created unless an independent later reuse need reopens F.18. |
| Lineage and reopen | Rename, alias, split, merge, and retirement history is recorded under `F.13`, and the card names the smallest value, scheme, sense, subject pattern, use, or reader-error change that reopens this settlement. |
| Reader use | A practitioner can tell what to say, what not to infer, and where to go if the name is not enough. |
| Work-name boundary | An action nominal remains a morphology cue: a hidden claim-bearing function-like use goes through A.6.F, while an already recovered Method, MethodDescription, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, or other value is named only under its direct pattern. A WBS or Work Package label remains plan- or assignment-episteme content. A performed-Work name is accepted only for one occurrence grounded under A.15.1 and attributed under F.6 as stated in section 5.3; a compact naming account may omit unused references, not the facts. Neighbouring production claims, measurement results, evaluation results, decisions, delivery occurrences, and acceptance verdicts stay under their direct patterns. |

Regression checks:

- When either the effective reference-scheme edition or the `LocalSenseClaim` changes, compare the resulting semantic-context projections. Re-check any obtaining Bridge, the separate claim about the named use between different projections, and that claim's current reliance; same-projection expression changes stay with designation, and no current correspondence use creates no Bridge or use claim.
- When a system-role-kind description changes in a way that may alter the C.3 candidate domain, membership distinction, member/non-member boundary, continuity, or the naming settlement's reader meaning, re-check the local kind name and any assignment name that depends on it. A provenance-only edit does not split the kind.
- When a method, capability, work, evidence, or status pattern changes, re-check any name that borrowed morphology from that area.
- When repeated reader errors occur, reopen candidate comparison instead of adding aliases indefinitely.

### F.18:10 - SoTA-Echoing

Source use was checked on 2026-08-20. F.18 uses only the following lines in this decision; source prestige does not select an FPF value or name.

| Current source and status | Adopted or adapted move | Exact F.18 effect | Limitation and smallest reopen condition |
| --- | --- | --- | --- |
| [ISO 704:2022](https://www.iso.org/standard/79077.html), published International Standard, and [ISO 1087:2019](https://www.iso.org/standard/62330.html), confirmed current in 2025 | Distinguish objects, concepts, definitions, and designations; make term formation and terminology decisions inspectable. | Supplies the value-before-label rule in 0 and 4.1, the separate value, kind, and designation fields in 4.2, and the rejection of dictionary substitution in 8. | The standards guide terminology work, not FPF ontic identity. Reopen only 4.1-4.3 and affected cases if a superseding ISO edition changes the selected concept and designation or term-formation distinction. |
| W3C, [*SKOS Simple Knowledge Organization System Reference*](https://www.w3.org/TR/skos-reference/), W3C Recommendation 2009, latest Recommendation checked 2026-07-23 | Keep concepts, preferred or alternative lexical labels, notes, collections, semantic relations, and mapping relations distinct. | Strengthens 4.2, 7.5, 8, and 9: a label, card, row, shared spelling, or generic mapping does not become the governed value or an F.9 Bridge. | SKOS is a stable web-vocabulary model, not the FPF naming method or a source of FPF kinds. Reopen those four loci if W3C supersedes the Recommendation or changes the label/mapping distinction used here. |
| Zhu, Reinecke, and Mitra, [*Language Scent: Exploring Cross-Language Information Navigation*](https://arxiv.org/abs/2604.03604), arXiv:2604.03604, 2026 preprint | Adapt contextual cues and in-situ recognizability as evidence for reader ergonomics; reject any inference from recognizability to cross-context equivalence. | Changes the reader-ergonomics probe in 4.3 and supports the conditional local labels in 7.2 and 7.5 while leaving exact value, local sense, and Bridge recovery mandatory. | The study is small, cross-language, and navigation-focused. Reopen only those probes and examples if stronger reader evidence reverses the observed value of contextual cues or exposes a new loss. |
| Current FPF `C.18` front and archive discipline | Keep non-dominated candidates, archive members, and selection reasons distinct; expose dimensions and dominance when those methods are actually used. | Supplies the optional ordinal-comparison rule in 4.3; it does not require QD apparatus for an ordinary four-candidate naming decision. | This is comparison discipline, not proof that a label is ontologically correct. Reopen only 4.3 if the FPF front, dominance, or protected-dimension rule changes. |

Currentness rule: when the pattern containing a value's direct rule, `C.2.1`, `F.9`, `A.10`, `B.3`, or `E.24.PUB` changes the value, card, sense, Bridge, bounded-use claim, reliance, or publication boundary, reopen only the affected invariant, field, case, or check. A future F.17 edition is consumed only through section 4.4; its change does not reopen local NameCards unless their supported public citation use or object references change.

### F.18:11 - Relations

Builds on `F.0.1`, `F.1`, `F.2`, `F.3`, `F.5`, `F.8`, `F.9`, `F.13`, `F.14`, `F.15`, `C.2.1`, and `E.24.PUB`.

Coordinates with:

- `A.2`, `A.2.1`, `A.2.5`, `A.2.7`, `A.15`, `A.15.1`, and `F.6` for system-role kinds, system-role assignments, assignment-state predicates and direct state relations, relations among system-role kinds and selected `SystemRoleKindRelationStructure`, system-role–Method–Work alignment, performed-Work occurrence grounding, and the separate Work-to-assignment attribution;
- `A.3.1` for method and method-family names; `A.3.2` for a separately identified `U.MethodDescription` episteme whose exact `EntityOfConcern` is that Method, and for the description episteme's separate name;
- `A.6.P`, `A.6.P.WMR`, `A.6.RCD`, `A.6.REL`, `A.6.5`, `A.6.RSIR`, `A.6.0`, `A.6.M`, `A.6.F`, and `A.6.C` for relation-claim settlement, work/method-boundary relation recovery, relation-kind and occurrence boundaries, slot, signature, interface, port, and protocol names;
- `A.10`, `B.3`, `F.10`, `E.10.D2`, and `C.2.1` for evidence-use, assurance-use, status-use, source-use, and description-episteme names;
- `E.17` for multi-view publication-face and publication-form use;
- `F.17` only after its current entry accepts the exact F.18 value, kind, card, and sense result and, for reuse between different semantic-context projections, the separate obtaining Bridge, affirmative C.2.1 use claim, and current A.10 or B.3 reliance; otherwise the local NameCard remains sufficient and the public row stays pending;
- `E.24.PUB` for the separate occurrence, form, carrier, audience, bounded-use, and currentness objects needed when an exact row-episteme edition is actually made available;
- `C.16`, `C.18`, and Part G search patterns when candidate comparison uses Pareto or quality-diversity vocabulary.

Constrained non-use:

- `F.18` admits no new U-kind and creates none of the governed system-role kinds, assignments, statuses, methods, Work, relations, signatures, slots, interfaces, or other subject values it names. A `NameCard` is a separately constituted `U.Episteme` under C.2.1, not a kind minted by F.18.
- Do not use `F.18` to decide whether two locally interpreted values are identical. A Bridge between exact F.17 cells can obtain only under the F.9 predicate; a separate C.2.1 claim states one proposed naming use between those cells, A.10 or B.3 supplies its reliance rule, and any governed-value identity claim must independently satisfy the direct value rules.
- `F.18` does not turn a publication row, card, table, or glossary entry into the thing being named.

### F.18:End

