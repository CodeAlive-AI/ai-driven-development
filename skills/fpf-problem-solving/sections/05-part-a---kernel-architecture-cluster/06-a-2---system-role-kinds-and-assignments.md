## A.2 - System-Role Kinds and Assignments

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2:0 - Use This When

**Plain name.** Work-facing system classification and assignment.

Use this pattern when one admitted `U.System` can contribute to different work or functioning without becoming a different system, and the current claim must say either:

- which locally constituted work-facing kind the system counts under now; or
- which system-role assignment actually obtains.

A system here is any individual independently admitted by A.1. It can be a person, team, organization, service, organism, or non-human technical object. The `SystemRole` head in a name such as `ReviewerSystemRole` says that candidates are systems; it does not admit the candidate, create an assignment, imply agency or capability, prove that Work occurred, or name a relation slot.

Typical moments:

- the same pump counts as a cooling circulator in plant operation and as a test article in qualification work;
- a project must decide whether Alice counts as a reviewer in one review slice;
- a relied-on claim says that a system holds a named system role but leaves the assignment occurrence unclear;
- ordinary wording says that a publication, method, capability, or relation participant “plays a role”, although the direct relation is still hidden;
- a proposed “part of a role” may instead be another kind, a relation among kinds, an assignment-state predicate, a capability condition, a responsibility or commitment relation, or a method or Work structure.

**Primary EntityOfConcern.** One exact local `U.Kind` whose candidates are `U.System` individuals and whose identity basis combines an explicit local practice or source boundary with one stable, assignable, work-facing contribution distinction. Such a kind is called a **system-role kind**. Assignment is a neighboring direct relation, not part of the kind.

**Primary working reader.** The first reader is an engineer-manager, analyst, or FPF author who must keep system identity stable while making classification and assignment inspectable. A later reader must be able to recover the local practice or source boundary, contribution distinction, declaration edition, candidate and slice, and any separately obtaining assignment and Work attribution.

**First useful move.** Start with the ordinary conclusion: “Alice counts as a reviewer for this submission” or “PumpUnit-3 is assigned as cooling circulator for this operating episode.” For classification, name the local system-role kind and evaluate the candidate with one `KindSignature` under C.3.2. Add a `U.SystemRoleAssignment` occurrence only when holding or assignment identity is actually claimed.

**Concern-word boundary.** *Concern* is Plain reader- or viewpoint-facing wording. It does not admit `U.Concern` or replace the exact EntityOfConcern, viewpoint episteme, kind, assignment, or receiving relation needed by the claim.

**What goes wrong if missed.** One label absorbs kind identity, classification, holder, assignment, capability, responsibility, and Work. Or every contribution is forced into a system role even when the real claim concerns evidence use, a relation participant, a declaration slot, or ordinary wording. In both cases readers cannot tell what exists, what merely describes it, and what actually happened.

**What this buys.** Systems retain their identities while work-facing classifications and assignments change. Membership is testable from the system features named by the membership rule rather than labels or circular hierarchy edges. Two local practices or sources can keep distinct kinds even when they use the same word, and ordinary contribution wording can stay readable without manufacturing an ontology.

**Not this pattern when.**

- Use `A.2.1` when the current object is a `U.SystemRoleAssignment` species or occurrence and its participant, predicate, or identity law matters.
- Use `A.2.2` for capability and `A.2.5` for assignment state.
- Use `A.2.7` for substitution, incompatibility, bundle, qualification, or another admitted relation among system-role kinds.
- Use `A.15` and its neighbors for method admission, planned Work, performed Work, and Work attribution.
- Use `E.24.UK` when a local system-role kind is proposed as a durable public FPF U-kind.
- Use `E.10.ROLE` when the source word *role* is ambiguous. If the recovered meaning is relation participation, a declaration place, an interface place, or a representation position, continue with `A.6.RSIR`.
- When an episteme rather than a system is current, recover its direct use, evidence, publication, external-rule, currentness, or reliance relation through the relevant subject pattern.

### A.2:1 - Problem Frame

One system can contribute in several ways while remaining the same system. `PumpUnit-3` remains the same pump when it counts under `CoolingCirculatorSystemRole` for plant operation and under `TestArticleSystemRole` for qualification. A person remains the same person while counting under author and verifier kinds in different slices and holding different assignments.

These are local typed distinctions, not durable universal kinds. Each system-role kind is constituted within an explicit local practice or source boundary and has a contribution-based identity. A `KindSignature` edition states how candidate features are evaluated. A C.3.2 judgment then answers whether one System counts under that kind in one slice. A separate assignment occurrence says that a System is assigned under its declared `U.SystemRoleAssignment` species.

Ordinary language also uses *role* to mean contribution or position. A design method can use a standard publication as a source for a constraint; a report can participate in an evidence relation; and a value can fill a relation slot. Those useful claims make neither the episteme nor the slot filler a system-role kind or assignment participant. The current relation must be recovered before the wording carries an FPF technical claim.

### A.2:2 - Problem

Without this pattern:

1. one system's changing contributions are modeled as changes of system identity;
2. a familiar label or taxonomy row is treated as a kind and as proof of membership;
3. kind identity and the membership criterion are treated as the same thing;
4. an assignment is used as a family-wide membership rule, or classification is used to manufacture an assignment;
5. the holder, kind, assignment interval, capability, responsibility, and Work are compressed into one record;
6. matching labels across local practices, sources, or editions are treated as identity or permission for reuse;
7. proposed subkind edges or extension rows create their own membership evidence;
8. ordinary *role* wording turns epistemes, slots, positions, or interfaces into system-held roles.

### A.2:3 - Forces

| Force | Tension |
| --- | --- |
| Stable system identity vs changing contribution | The candidate remains one system while classifications, assignments, participation, and Work change. |
| Local typed use vs public ontology growth | A project needs reusable work-facing kinds without admitting `U.Role` or another universal root. |
| Kind identity vs membership | The continuing contribution distinction identifies the kind; a current criterion decides whether one system counts under it in a slice. |
| Classification vs assignment | A judgment classifies a system. An assignment is a direct relation occurrence and can exist or end independently. |
| Readable wording vs exact technical claims | “Alice is reviewer” is useful; a receiving decision may still need the exact kind, judgment, assignment, or Work attribution. |
| Useful factorization vs false role mereology | Capability, responsibility, commitment, state, and Work remain separately governed rather than becoming parts of a role. |

### A.2:4 - Solution

Use an exact local `U.Kind` for each stable assignable work-facing contribution distinction. Identify it through the explicit practice or source boundary in which that distinction is constituted together with the distinction itself. Give a live technical name the `SystemRole` head, such as `ReviewerSystemRole` or `CoolingCirculatorSystemRole`. Do not introduce `U.SystemRole`; the concrete value is already a local `U.Kind` under C.3.

Then keep four moves separate:

1. identify the local system-role kind;
2. declare or select the `KindSignature` edition used for membership;
3. evaluate one system, kind, signature edition, and slice under C.3.2;
4. add a directly declared `U.SystemRoleAssignment` species and occurrence only when an assignment actually obtains.

Capability, assignment state, method admission, performed Work, responsibility, commitment, permission, authority, evidence, reliance, and publication remain direct neighboring claims.

#### A.2:4.1 - Recognize a System-Role Kind

A local kind is a system-role kind only when all four conditions hold:

1. the local practice or source boundary in which the distinction is constituted is explicit;
2. its identity basis includes one stable, assignable, work-facing contribution distinction within that boundary;
3. its candidate `ValueKind` is `U.System`; and
4. its `KindSignature` tests directly governed features of the candidate without treating a label, taxonomy row, description, assignment record, classification judgment, extension row, or proposed `U.SubkindOf` edge as the feature by form.

The **identity basis** answers which contribution distinction the kind continues to denote. The **membership criterion** answers whether a system counts under it now. A compatible declaration or interpretation edition can preserve one kind. A change from substantive-review contribution to release-decision authority identifies another kind even if both editions use `ReviewerSystemRole` as displayed text.

`CoolingPumpKind` is not thereby a system-role kind. Its identity can be a physical or functional pump distinction rather than an assignable work-facing contribution. `ShortAssignmentKind`, if declared to classify assignment occurrences by duration, is also not a system-role kind because its candidates are assignments rather than systems.

#### A.2:4.2 - Evaluate Membership without a Circular Shortcut

Each membership clause names the candidate feature's subject pattern, predicate or governed feature, applicability, dependencies, and slice. The classification has four explicit inputs:

```text
J(candidateSystem, systemRoleKind, kindSignatureEdition, contextSlice)
  -> true | false | unknown
```

An assignment may be one feature only when the local `KindSignature` explicitly uses that independently obtaining assignment predicate. There is no family-wide rule that assignment means membership. The judgment being computed, a broader-kind judgment, an extension row, or the proposed `U.SubkindOf` occurrence cannot be a premise of the same judgment.

Missing a required feature or dependency yields `unknown`, not `false`. Evidence supports a claim about the governed feature; it does not create that feature or the membership result.

Every `U.SubkindOf` proposal evaluates the aligned narrower and broader signatures independently for the same candidate and slice. Admit the order only when the C.3.1 monotonicity condition holds. The edge records an already established implication; it never produces either classification judgment.

#### A.2:4.3 - Keep Kind Identity, Declaration, and Extension Separate

The system-role kind is not its `KindSignature`, taxonomy episteme, reference scheme, classification judgment, or `KindExtension`. Same-kind continuity across declaration editions requires an explicit C.3.1 decision that preserves both the named local practice or source boundary and the stable contribution distinction. A compatible criterion or scheme edition can preserve the kind while later judgments cite the edition actually used. A changed boundary or identity-defining contribution yields another kind.

An old role taxonomy or scheme can provide evidence for recovering the local practice or source boundary, contribution distinction, or criterion. Its label or identifier does not decide sameness. A selected `BoundedModelUseStructure` can qualify one receiving interpretation when that independently established organization matters; it is designated in the receiving assertion or use and is stored neither on the kind nor as an optional participant of a generic assignment or kind relation. A genuinely structure-dependent relation species instead declares the structure as a required participant, uses the stronger predicate, and states the resulting occurrence-identity law.

Use `A.1.1` before citing that structure. Select `BoundedModelUseStructure` only when exact model applicability, actual model use in assigned Work, fixed-content expression coherence, exact applied constraints, and one named selection-use frame jointly change the receiving decision. If the direct kind, relation, assertion, or Bridge already answers the question, stop there; neither a model-use label nor a wish for more background selects the structure.

#### A.2:4.4 - Admit Only Exact System-Role-Kind Domains

`U.Kind` is too broad as the assigned-kind participant domain of an assignment species. Each bounded system-role vocabulary declares one local domain whose candidates are local kinds satisfying the four recognition conditions. For example:

```text
JournalReviewSystemRoleKindDomain : U.Kind
  localPracticeOrSourceBoundary: JournalReview-2026
  candidateValueKind: U.Kind
  criterion:
    the candidate kind has U.System candidates and a recoverable,
    assignable work-facing contribution identity in JournalReview-2026
```

A direct assignment species uses that local domain as the `ValueKind` of its declaration-local `AssignedSystemRoleKindSlot`. The slot therefore rejects `CoolingPumpKind`, `ShortAssignmentKind`, and arbitrary local kinds. This is local C.3 typed use, not admission of `U.Kind` as a durable public root.

#### A.2:4.5 - Assignment Boundary

`A.2.1` defines the `U.SystemRoleAssignment` family. The family contains directly declared relation species rather than one permissive universal signature. Every species declares:

- `HolderSystemSlot : U.System`;
- a declaration-local `AssignedSystemRoleKindSlot` whose `ValueKind` is one exact local system-role-kind domain;
- any additional real participants needed to distinguish that species; and
- its own obtaining predicate, applicability, and occurrence-identity rule.

A simple species can declare only the holder and assigned-kind participant meanings. A stronger appointment, authorization, or work arrangement can declare another participant meaning when its actual value changes occurrence identity. The specialized occurrence itself remains a `U.SystemRoleAssignment`; do not keep a second generic occurrence beside it merely for projection.

An assignment occurrence begins when its predicate starts obtaining for the fixed participants, continues over the maximal uninterrupted predicate-true interval, and ends when a participant changes or the predicate ceases to obtain. A taxonomy episteme, reference scheme, `KindSignature`, assertion, or interval description can interpret or describe the claim without becoming another world-side participant.

Assignment does not prove classification unless the kind's signature uses that independently obtaining relation as a feature. Classification does not create an assignment. Neither one proves capability, agency, responsibility, authority, commitment, permission, functioning, method enactment, or performed Work.

#### A.2:4.6 - Relations around the Kind and Assignment

| Current claim | Subject pattern | Kept distinct |
| --- | --- | --- |
| Local kind, declaration, classification, and extension | `C.3`, `C.3.1`, `C.3.2` | system-role kind, `KindSignature`, four-input judgment, optional extension, and kind-continuity decision |
| System-role assignment | `A.2.1`, `A.6.5`, `A.6.REL` | direct species, exact participants, predicate, applicability, and uninterrupted occurrence identity |
| Assignment state | `A.2.5` | exact assignment occurrence, `SystemRoleAssignmentStatePredicate`, `SystemRoleAssignmentStateRelation` occurrence, and its maximal truth interval; target evaluation window, assertion polarity, evidence, and reliance remain separate |
| Capability | `A.2.2` | holder, capability instance, envelope, measures, currentness, and fit predicate |
| Relations among system-role kinds | `A.2.7`, `C.3.1` | exact kind participants and substitution, incompatibility, bundle, or monotonic qualification relation |
| Description and naming | `F.4`, `F.5`, `F.18` | kind, `SystemRoleKindDescription`, names, and publication or access carrier |
| Method and Work | `A.3`, `A.15`, `F.6` | Method, MethodDescription, performer system, assignment, Work occurrence, and attribution |
| Responsibility, commitment, permission, or authority | direct domain pattern, `A.2.8`, `A.2.8.PER`, or `missing-governor` | actual bearer, exact relation participants, predicate, and instituting or permission basis |
| Evidence, reliance, or publication | `A.10`, `A.15.4`, `B.3`, `C.2.1`, `E.17`, `F.10` | episteme, evidenced claim, reliance, provenance, currentness, and publication relation |

Select only the objects needed by the current claim. A large neighborhood is not a larger kind, and none of these values is a “part of the role”.

`SystemRoleKindDescription` is an F.4 description episteme whose exact EntityOfConcern is one system-role kind. An episteme about an assignment or a relation among kinds has that assignment or relation as its EntityOfConcern instead. Teaching from, storing, or publishing any such description does not make it the described kind or occurrence.

#### A.2:4.7 - Recover Contribution Wording before Formalizing It

The phrase “the role of X” often means that X contributes to a use. Apply `E.10.ROLE` first. If X is an admitted system and the claim needs a work-facing classification, recover the local system-role kind and C.3.2 judgment; add an assignment only when holding is claimed. Otherwise keep X in its actual kind and name the direct relation or declaration place.

| Ordinary wording | Governed repair |
| --- | --- |
| `RFC 9110 plays a normative role in this design` | Keep the publication as an episteme and state the current external-rule, constraint, source-use, or publication relation selected by the design claim. |
| `this dataset plays the benchmark role` | Keep the dataset as an episteme and state the measurement, evidence, benchmark, source-use, or currentness relation that actually obtains. |
| `this parameter has the control role` | Recover the Method or model parameter, or an A.6.5 participant slot, from the direct declaration. |
| `this interface plays the integration role` | Recover the selected module-interface, port, signature, or protocol relation under its governor. |

The alternatives are recognition probes, not a union kind. If no direct relation can yet be named, return the exact `missing-governor` rather than minting a system-role kind.

#### A.2:4.8 - System-Role Vocabularies and Relations among Kinds

A system-role-vocabulary or taxonomy episteme can publish local kind names, declarations, and selected relation claims under an effective reference scheme. It creates no kind, membership result, or assignment by publication. Each live kind still needs its bounded identity; each judgment cites its actual signature edition.

Use `A.2.7` to state one selected `SystemRoleKindRelationStructure` over exact local system-role kinds and admitted relations among them. A receiving use can cite an assertion about substitution, incompatibility, bundle, qualification, or another residual relation alongside separately stated assignments, state, capability, and Work. Systems and assignments are not participants of the kind-relation structure.

Algebraic, graph, matrix, embedding, or neural representations are mathematical lenses over that selected structure when a project declares the lens use. They neither create the kinds nor make a relation obtain.

| System-role kind | Recognition case | Boundary |
| --- | --- | --- |
| `CoolingCirculatorSystemRole` | A pump supplies a circulation contribution in plant operation. | Capability, assignment, functioning, and performed Work remain separate. |
| `TestArticleSystemRole` | The same pump is selected for qualification use. | The classification or assignment does not change pump identity. |
| `VerifierSystemRole` | A person, team, organization, service, or non-human technical system supplies verification contribution under its local criterion. | A verification report is an episteme, not the classified system. |
| `TransformerSystemRole` | A system is classified for a transformation-facing contribution. | The system performs Work; the kind and assignment do not act. |

#### A.2:4.9 - Reduced Use and Stronger Claims

Ordinary “Alice is reviewer” or “this component plays a control role” wording can remain Plain when no decision, attribution, admission, or reliance depends on another technical distinction. Do not materialize a kind, judgment, or assignment merely to decorate the sentence.

When a stronger claim appears, add only the needed object:

- the local kind and judgment when classification matters;
- the assignment occurrence when who holds what and when matters;
- the direct state, capability, method, Work, responsibility, commitment, permission, evidence, reliance, or publication relation when that relation carries the claim;
- the exact C.3.3 kind relation and, when local meanings differ, F.9 relation needed for cross-local use, without merging the kinds or creating assignments.

The earlier Plain sentence is not evidence for a stronger claim.

### A.2:5 - Archetypal Grounding

#### A.2:5.1 - Reviewer Membership and a Non-Circular Subkind

The JournalReview practice declares one local kind from its practice boundary, contribution distinction, and direct holder features:

```text
ReviewerSystemRole : U.Kind
  localPracticeOrSourceBoundary: JournalReview-2026
  localIdentityBasis:
    the assignable contribution distinction “can supply a substantive review judgment
    meeting the current JournalReview acceptance conditions”

KindSignature@ReviewerSystemRole/e3:
  EntityOfConcern: ReviewerSystemRole
  candidateValueKind: U.System
  membershipCriterion:
    one current A.2.2 capability instance has the candidate system as holder,
    names substantive-review Work or its review-judgment result class,
    and satisfies its declared envelope, measures, and currentness;
    the current JournalReview capability-fit predicate confirms the submission,
    review-phase, and judgment-quality conditions for this slice
  sliceApplicabilityConditions:
    the submission, review phase, and temporal selector
  effectiveReferenceScheme: JournalReview-Scheme-2026/e3
  assumptionsAndDependencies:
    the capability instance, currentness condition, and capability-fit predicate
```

The capability and fit predicate are governed under A.2.2. They are features used by the criterion, not substitutes for the kind or judgment. One application can therefore state:

```text
J(Alice, ReviewerSystemRole, KindSignature@ReviewerSystemRole/e3, ReviewSlice-17) = true
J(Alice, ReviewerSystemRole, KindSignature@ReviewerSystemRole/e3, LaterSlice-18) = false
```

The later result follows only from a known failed currentness or fit condition. Ending an assignment alone changes neither judgment because this signature does not use assignment as a feature. If a dependency is unavailable, the result is `unknown`.

For `RoboticsEngineerSystemRole U.SubkindOf EngineerSystemRole`, evaluate the two aligned signatures independently for every admitted candidate and slice needed by the declared domain. Only after every defined true narrower judgment implies a true broader judgment may C.3.1 admit the relation. The proposed edge proves neither judgment. An independently obtaining robotics assignment also proves neither judgment unless the relevant signature explicitly uses it as a non-circular feature.

#### A.2:5.2 - Pump in a Cooling Loop

`CoolingCirculatorSystemRole` is a local kind in `PlantOperations-2026`. Its identity is the assignable plant-operation contribution, while its `KindSignature` tests the directly governed circulation features needed by that contribution. `PumpUnit-3` is judged against that exact edition and slice; the judgment does not change pump identity.

When the plant also claims an assignment, it uses a directly declared species:

```text
PlantCoolingSystemRoleAssignment : U.SystemRoleAssignment
  HolderSystemSlot: U.System
  AssignedSystemRoleKindSlot: PlantOperationsSystemRoleKindDomain
  predicate:
    the holder is selected for the assigned plant-operation contribution
    under the declared operating conditions

PlantCoolingAssignment@PumpUnit3:
  HolderSystemSlot: PumpUnit-3
  AssignedSystemRoleKindSlot: CoolingCirculatorSystemRole
  assignmentInterval: [2026-06-01, open]
```

The interval is assertion content about the known extent; the occurrence continues only while the species predicate obtains without interruption for the same participants. `PlantOperationsSystemRoleVocabulary-2026`, its reference scheme, and the relevant signature can be cited as interpretation evidence. They are not extra assignment participants.

Closing the open interval later refines the same occurrence description when uninterrupted identity is preserved; the stated interval neither makes the relation obtain nor becomes another participant.

The assignment proves neither circulation capability over every operating region nor performed circulation or maintenance Work. Those claims use A.2.2, A.15.1, and the applicable Method, transformation, measurement, and evidence relations.

#### A.2:5.3 - A Standard Used in Design Work

An engineering team uses RFC 9110 while designing an HTTP service. Keep these claims separate:

1. `DesignTeam-2` independently counts under `ProtocolDesignerSystemRole` in the current slice when its signature criterion is satisfied.
2. One design-assignment occurrence may obtain as an instance of a declared `U.SystemRoleAssignment` species.
3. The RFC publication is the source episteme in the direct source-use or external-rule relation selected by the design claim.
4. Dated design Work is performed by `DesignTeam-2` under the exact assignment through F.6 and may produce a MethodDescription or SystemDescription.

The publication neither counts under the system-role kind nor performs the Work.

#### A.2:5.4 - The Same Label in Two Local Practices

An editorial-review practice and a safety-assurance practice can each declare a `ReviewerSystemRole`. They remain two local kinds because the constituting practice boundary and stable contribution distinction together form each identity basis. A shared label, vocabulary source, or reference-scheme spelling establishes neither sameness nor a Bridge.

Suppose a staffing dashboard proposes `u-reviewer-display`: show assignments from both practices in one `Reviewer` column. First recover the two exact local kinds and any F.17 cells needed by the displayed expressions; then establish only the C.3.3 kind relation and F.9 local-sense relation that the display actually consumes. State a separate C.2.1 bounded-use assertion with direction `d-safety-to-editorial-display`, rule `r-preserve-reviewer-differences`, and tolerance `t-shared-label-only`, plus polarity and effective scheme. The rule keeps the practices' admission, independence, evidence, and completion fields separate and tolerates only the shared display label.

Current A.10 provenance and `RelianceDisposition=pass` can support that display use. They do not justify substitution between assignments or merge the two kinds. If the use makes an assurance claim or crosses B.3's material-reliance threshold, only a current positive B.3 claim carrying this same use and sufficient minimum reliance safety assurance supports it; no-assurance, insufficient-record, narrowed, rejected, withdrawn, abstaining, or blocked dispositions stop or narrow the use. A Bridge Card can package the Bridge, bounded-use assertion, evidence, and disposition, but it grants no assignment, eligibility, capability, use suitability, or performed-Work inference. A selected `BoundedModelUseStructure` is cited only in the receiving use whose interpretation it changes.

#### A.2:5.5 - A Relation Participant Slot Named `role`

An external notation may call one relation position `role`. Apply E.10.ROLE and A.6.RSIR to recover the participant meaning and declaration-local SlotKind. Its `ValueKind` is the participant kind. The external label creates neither a system-role kind nor an assignment. A System participates in the relation as declared; it holds a system-role assignment only through a separate occurrence of a declared assignment species.

### A.2:6 - Bias Annotation

| Bias risk | Failure | Repair |
| --- | --- | --- |
| Lexical bias | A familiar role label is treated as a kind, judgment, or assignment. | Recover the named practice or source boundary, stable contribution distinction, signature, candidate, and slice; keep ordinary wording Plain when no technical object is needed. |
| Document bias | A taxonomy, description, card, or publication is treated as the kind or assignment. | Keep the episteme and publication relation separate from the governed world-side values. |
| Episteme-as-agent drift | A standard, report, dataset, or model is said to perform Work. | Name the performer system and Work occurrence; keep the episteme in its evidence, reliance, external-rule, source-use, or publication relation. |
| Global-label bias | Matching names are treated as matching kinds or sufficient permission for cross-local use. | Keep local identities separate and establish only the C.3.3 kind relation, any F.9 local-sense relation, and the bounded-use claim that actually obtain. |
| Assignment-membership circularity | Assignment proves classification or classification creates assignment. | Evaluate direct features first; use assignment only when the signature explicitly cites an independently obtaining assignment predicate. |
| Slot-role drift | A relation participant becomes a system-held role because a source labels the position `role`. | Recover the exact participant meaning, SlotKind, and ValueKind under A.6.RSIR. |
| Capability-role drift | Assignment or kind membership is treated as proof of ability. | Use A.2.2 and a separate capability-fit predicate. |
| Method-role drift | A system-role kind is treated as the Method or MethodDescription used for Work. | Keep Method, MethodDescription, admission condition, assignment, and Work occurrence under A.3 and A.15. |
| Responsibility-role drift | A system-role kind or assignment is treated as the responsibility result. | Cite the admitted responsibility predicate and actual bearer, or return `missing-governor`. |
| Role mereology | State, capability, responsibility, or Work is modeled as a part of a role. | Recover another kind, relation among kinds, or the direct neighboring object and relation. |

### A.2:7 - Working Guidance

1. Identify the candidate and confirm its independent A.1 admission as `U.System`.
2. Name the local practice or source boundary and one stable assignable contribution distinction that together identify the local kind.
3. Declare or select the exact `KindSignature` edition and its direct governed feature criteria.
4. Evaluate the candidate, kind, signature edition, and slice as `true`, `false`, or `unknown`.
5. Add an assignment only when an occurrence of a declared assignment species actually obtains.
6. State each claim about state, capability, Method, Work, responsibility, commitment, permission, authority, evidence, or reliance through the pattern that defines or constrains it.
7. Evaluate every subkind proposal from independently obtained aligned judgments; never use the proposed edge as a membership premise.
8. For cross-local use, keep both kinds and their assignments distinct and establish only the C.3.3 kind relation, F.9 local-sense relation, and bounded-use claim actually needed.
9. If the source uses *role* for another object, apply E.10.ROLE and continue with the recovered subject pattern; stop at `missing-governor` when no relation is yet admitted.

### A.2:8 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-A2.1` | Every system-role kind is one local `U.Kind`; no `U.Role` or universal `U.SystemRole` is introduced. |
| `CC-A2.2` | The explicit local practice or source boundary, stable assignable contribution distinction, and `U.System` candidate kind are recoverable and jointly identify the local kind. |
| `CC-A2.3` | Kind identity, `KindSignature`, classification judgment, extension, vocabulary episteme, and reference scheme remain distinct. |
| `CC-A2.4` | Each judgment names one system, system-role kind, signature edition, slice, and `true`/`false`/`unknown` result. |
| `CC-A2.5` | Membership clauses use directly governed candidate features; labels, records, judgments, extensions, and proposed subkind edges are not features by form. |
| `CC-A2.6` | An assignment is a membership feature only when the signature cites its independently obtaining predicate; no family-wide assignment-membership law exists. |
| `CC-A2.7` | Every assignment occurrence belongs to one directly declared `U.SystemRoleAssignment` species with an exact local system-role-kind domain. |
| `CC-A2.8` | Taxonomy, scheme, signature, assertion, and interval description are interpretation or claim content rather than generic assignment participants. |
| `CC-A2.9` | Capability, state, Method, Work, responsibility, commitment, permission, authority, evidence, reliance, and publication remain separately governed. |
| `CC-A2.10` | A `U.SubkindOf` claim follows independently evaluated aligned signatures and C.3.1 monotonicity. |
| `CC-A2.11` | Same spelling across local practices, sources, or editions does not decide kind identity; continuity and actual relations are explicit. |
| `CC-A2.12` | Relation-position or ordinary contribution wording creates no system-role kind or assignment by itself. |
| `CC-A2.13` | A proposed decomposition is resolved through exact relations among kinds or neighboring subject patterns, not `partOf` over a system-role kind. |
| `CC-A2.14` | Cross-local use keeps both kinds distinct, cites the exact C.3.3 kind relation and any F.9 local-sense relation, and states the bounded use, direction, preservation rule, tolerated loss, polarity, effective scheme, and current reliance needed by the receiver; a Bridge Card is not a use licence. |
| `CC-A2.15` | A selected model-use structure appears only in the receiving claim it changes; it neither classifies nor assigns a system and never enters a generic relation as an optional participant. |

### A.2:9 - Common Anti-Patterns

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| `PumpAsCoolingCirculator` as a new system subtype | One contribution is mistaken for system identity. | Keep the pump kind stable; use a local `CoolingCirculatorSystemRole` classification and a separate assignment when it obtains. |
| `PumpUnit-3#CoolingCirculatorSystemRole:Plant-A@Window` | The compact token hides the kind declaration, assignment species and occurrence, and the kind of Plant A while suggesting a mandatory context participant. | State the local kind and judgment; when assignment matters, name the A.2.1 occurrence and its declared species, and keep Plant A as the plant System or Work locus. |
| `ReviewerSystemRole` means “assigned reviewer” | Kind membership and assignment occurrence are collapsed. | Evaluate the signature; state the assignment independently. |
| Membership means “an assignment to this kind obtains” | Broader classification would require a broader assignment and subkind order would create world-side facts. | Use direct governed system features; assignment can be one explicitly declared feature. |
| One generic assignment signature accepts `U.Kind` | Arbitrary kinds enter the assigned-kind slot and stronger appointments lose their participant law. | Declare a direct species with an exact local system-role-kind domain. |
| Taxonomy and scheme are assignment participants | Interpretation editions become world-side identity changes. | Keep them in declarations, assertions, or evidence about the predicate. |
| `AssistantReviewerSystemRole partOf ReviewerSystemRole` | No constructive whole or part relation is established. | Test an exact qualification, substitution, incompatibility, bundle, or another local kind and direct relation. |
| `The PDF enforced the rule` | An episteme replaces the system and Work that performed enforcement. | Name the performer and Work; state the PDF's source-use, external-rule, evidence, or reliance relation separately. |
| Same label, therefore same kind or assignment | Spelling establishes neither local identity, Bridge, nor obtaining relation. | Recover the two kinds and establish the exact C.3.3 and, when needed, F.9 result consumed by the use. |

### A.2:10 - Consequences

| Gain | Cost or tradeoff |
| --- | --- |
| Systems retain stable identity while contribution classifications and assignments change. | Relied-on classification must identify the local kind, its practice or source boundary, and the signature edition used. |
| Membership can be checked without circular assignment or hierarchy premises. | Direct candidate features and unavailable dependencies must be distinguished. |
| Assignment identity remains available through direct species and uninterrupted obtaining. | A stronger appointment needs its real participants and predicate rather than a generic record. |
| Local vocabularies remain reusable without a universal role root. | Cross-local sameness and use require explicit continuity, an obtaining C.3.3 kind relation, or an F.9 local-sense relation, as applicable. |
| Ordinary sentences remain readable. | A stronger receiving claim must still expose the exact kind, judgment, assignment, or relation it consumes. |
| Episteme use, capability, responsibility, Method, and Work remain independently testable. | Contribution wording must be resolved before it carries another technical inference. |

### A.2:11 - Rationale

System-role kinds solve a local classification problem. System-role assignments solve a relation-occurrence problem. The pump does not become another system because its contribution changes, and a kind does not become an assignment because one system currently counts under it.

The architecture therefore keeps these levels separate:

1. the local system-role kind, its practice or source boundary, and its contribution distinction;
2. the `KindSignature` and one C.3.2 judgment over a system and slice;
3. any directly declared `U.SystemRoleAssignment` occurrence;
4. direct neighboring relations for state, capability, Method, Work, responsibility, commitment, permission, authority, evidence, reliance, description, and publication.

A system-role kind is not a holon merely because its description has internal fields. Proposed “parts” repeatedly resolve into other kinds, relation predicates, assignments, Method or Work structures, or parts of description epistemes. The useful structure is the exact relation structure governed by A.2.7, not role mereology.

Semantic locality needs no universal context participant. The explicit practice or source boundary together with the stable contribution distinction identifies the local kind; declaration content carries the classification criterion. An assignment species declares only its real participants. A receiving assertion or use can cite a selected model-use structure when that structure actually changes interpretation.

### A.2:12 - SoTA-Echoing

| Practice line | Source and status | FPF mutation | Practical consequence |
| --- | --- | --- | --- |
| Current foundational-ontology work separates role-like classification, relation participation, aspects, and situations instead of treating them as one category. | Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint; current comparator, not an imported hierarchy. | Use local C.3 kinds for work-facing classification, direct relation species for assignments, A.6.5 for participant slots, and separate state and episteme-use relations. | Different classifications and assignments do not create system subtypes or role parts. |
| DOLCE separates endurants, perdurants, qualities, abstracts, dependence, and constitution but does not itself settle FPF system-role-kind or assignment identity. | DOLCE 2022 axiomatization; bounded comparator. | Preserve system, kind, relation occurrence, Work, quality, and episteme distinctions under their FPF governors. | A borrowed category label cannot replace the local identity and predicate law. |
| DDD makes model applicability local and Context Mapping a method applied to actual model-use boundaries. | Evans, *Domain-Driven Design Reference* (2015) and current context-mapping practice. | Use a selected `BoundedModelUseStructure` only in the receiving claim it changes; keep the Method and performed Work separate. | A plant assignment needs its local kind and species, not a universal context participant. |
| FPF relation and episteme discipline separates description and publication from evidence, reliance, source use, and the systems performing Work. | Current C.2.1, A.6.REL, A.10, A.15.4, and E.17 line. | Require an admitted system for system-role classification and keep each episteme in the relation that makes its use relevant. | A team can use a standard as a constraint source without making the standard a performer or role holder. |

SysML is not used as a SoTA authority or lineage here. A modeling notation does not decide the identity of a system-role kind, classification judgment, assignment occurrence, participant slot, responsibility relation, or Work.

### A.2:13 - Relations

**Builds on:** `A.1` for system admission; `A.1.1` for selecting a `BoundedModelUseStructure` only when its complete decision-relevant relation organization, applied constraints, and named selection-use frame are current; `C.3`, `C.3.1`, and `C.3.2` for local kind identity, declaration, classification, extension, subkind, and continuity; `A.6.0`, `A.6.5`, and `A.6.REL` for assignment declarations and occurrences; `C.2.1` for interpretation and assertion epistemes.

**Governs with:** `A.2.1` for system-role assignments; `A.2.2` for capability; `A.2.5` for assignment state; `A.2.7` for relations among system-role kinds; `A.15` and `F.6` for Method-Work alignment and attribution; `F.4`, `F.5`, and `F.18` for description and naming.

**Crosses locality through:** `C.3.3` for exact local kinds, `F.9` for relations between exact F.17 cells, and `A.6.9` for ambiguous sameness wording across local boundaries, followed by a bounded-use assertion and current reliance when the receiving action needs them. A matching name, Bridge, card, or selected model-use structure creates neither identity nor assignment.

**Keeps separate from:** responsibility, commitment, permission, authority, state, capability, Method, Work, evidence, reliance, publication, external-rule, and currentness relations. Apply `E.10.ROLE` to ambiguous wording and `A.6.RSIR` only when relation participation or its declaration must be recovered.

### A.2:End

