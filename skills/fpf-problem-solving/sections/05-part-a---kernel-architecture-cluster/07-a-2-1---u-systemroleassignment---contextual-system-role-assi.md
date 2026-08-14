## A.2.1 - U.SystemRoleAssignment - Contextual System-Role Assignment

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2.1:0 - Use This When

**Plain name.** Assignment to a system role.

Use this pattern when another claim must rely on one obtaining assignment of an admitted `U.System` under one exact local system-role kind.

Typical moments:

- a MethodDescription names `InspectorSystemRole`, but no current assignment occurrence has been established;
- dated Work must be attributed through `performedUnderAssignment(W, RA)` and the exact assignment `RA` is still missing;
- the same system receives the same system-role kind during two separated episodes;
- two overlapping commissions or positions distinguish two assignments with the same holder and system-role kind;
- an appointment, installation locus, or work commission may be a real additional participant of one domain assignment species;
- a roster, configuration row, observation, decision, or evidence item supports an assignment claim without becoming an assignment participant.

**Primary EntityOfConcern.** One assignment occurrence whose relation species is declared directly under `U.SystemRoleAssignment`. Every species declares a holder participant with `U.System` as its domain, an assigned-kind participant drawn from one exact local system-role-kind domain, its own predicate and applicability, any real additional participant meanings, and its occurrence-identity rule. The occurrence supplies the actual participant values, including its holder System.

**Primary working reader.** An engineer-manager, analyst, Method author, or FPF author who must identify assignment and Work attribution without merging classification, capability, responsibility, authority, Method, Work, evidence, or publication into the assignment.

**First useful move.** Write the ordinary claim first: “Robot-7 is assigned as inspector for Shift-17.” Then identify the declared assignment species, the participant meanings and predicate it declares, and the participant values that satisfy that predicate in this case. Expose an occurrence reference only when another claim must distinguish or cite this episode.

**What goes wrong if missed.** A kind name is mistaken for an assignment, a permissive generic signature accepts arbitrary kinds, two real commissions collapse into one record, or a taxonomy and scheme become world-side participants. Work can then be attributed to the wrong occurrence while capability, authorization, and evidence hide as assignment fields.

**What this buys.** Simple assignments remain simple, stronger assignments retain their real participants, and every occurrence exposes its actual holder through the species-declared holder slot used by F.6. Repeated episodes are distinguishable without manufacturing a second generic assignment beside a stronger one.

**Not this pattern when.**

- Use `A.2` and C.3.2 for the system-role kind and one classification judgment.
- Use `A.2.2` for capability, `A.2.5` for assignment state, and `A.2.7` for relations among system-role kinds.
- Use `A.3`, `A.15`, and `A.15.1` for Method, MethodDescription, Work, and enactment.
- Use `F.6` for performed-Work attribution through an already identified assignment.
- Use the direct responsibility, commitment, permission, authority, access, decision, evidence, reliance, provenance, publication, external-rule, or currentness pattern when that relation is current.
- Use `E.10.ROLE` when the source word *role* has not yet been resolved; use `A.6.RSIR` when it means relation participation or a declaration place.

### A.2.1:1 - Problem Frame

A system-role kind does not assign itself. `InspectorSystemRole` can classify Robot-7 for one maintenance slice without any assignment occurrence. Conversely, an assignment can obtain while no Work occurs, and a local `KindSignature` can use or ignore that assignment when classifying the holder.

`U.SystemRoleAssignment` is the common relation family. It has no permissive root `RelationSignature`. Concrete domain species declare the participant law that their occurrences actually satisfy. A simple inspection assignment may need only the holder and assigned kind. A project-review appointment may also depend on one exact commission. The stronger occurrence itself is the assignment; it does not sit beside a weaker generic assignment with the same projection.

The holder can be any independently admitted `U.System`, including a person, team, organization, service, organism, or non-human technical object. Assignment establishes neither consciousness nor agency, capability, responsibility, commitment, permission, authority, access, gate passage, functioning, Method enactment, or performed Work.

Taxonomy epistemes, reference schemes, `KindSignature`s, assertions, and interval descriptions can interpret or describe the assignment claim. They are not generic world-side assignment participants. A selected `BoundedModelUseStructure` belongs in the receiving assertion or use unless one separately admitted relation species makes that structure a required identity-bearing participant.

### A.2.1:2 - Problem

Without this pattern:

1. a system-role kind or familiar job label is used as if it identified an assignment episode;
2. one broad `U.Kind` slot admits physical, functional, assignment-occurrence, and arbitrary local kinds;
3. a root signature hides different participant laws behind optional fields;
4. a strong appointment is represented as one generic assignment plus another unrelated occurrence;
5. assignments with the same holder and kind but different commissions or separated episodes collapse;
6. taxonomy, scheme, context, interval, decision, and evidence become generic participants;
7. assignment is treated as classification, capability, authorization, responsibility, or Work;
8. a storage key replaces the predicate and uninterrupted occurrence identity.

### A.2.1:3 - Forces

| Force | Tension |
| --- | --- |
| Common attribution projection vs domain-specific assignment identity | F.6 needs the holder of every assignment, while domains can require different real participants. |
| Simple cases vs stronger appointments | A two-participant assignment should stay light; a real commission or position must not be hidden or downgraded. |
| Readable assertion vs explicit occurrence | Most readers need a sentence, while later attribution or state claims may need a stable assignment reference. |
| Stable participants vs repeated episodes | Identical participant values can recur after an interruption; time describes and distinguishes episodes without becoming a participant. |
| Interpretation vs world-side identity | Taxonomies, schemes, signatures, and evidence matter to claims but do not automatically participate in the assignment. |
| Assignment vs neighboring facts | Classification, capability, permission, responsibility, access, Method, and Work can vary independently. |

### A.2.1:4 - Solution

Declare each assignment relation species directly under `U.SystemRoleAssignment`. Do not give the family one universal participant signature. Every admitted species declares:

- `HolderSystemSlot : U.System`;
- one declaration-local `AssignedSystemRoleKindSlot` whose `ValueKind` is the exact local system-role-kind domain used by that species;
- its direct assignment predicate and applicability;
- every additional actual participant that changes the predicate or occurrence identity; and
- its occurrence-identity rule.

The `HolderSystemSlot` and `AssignedSystemRoleKindSlot` names are declaration-local SlotKinds. Their spelling does not create global slots. Their complete A.6.5 SlotSpecs state ValueKind, refMode, participant meaning, multiplicity, and any constraints.

#### A.2.1:4.1 - Simple Direct Species

A simple species has only the two common participants:

```text
JournalReviewAssignmentRelation <: U.SystemRoleAssignment

RelationSignature:
  HolderSystemSlot: U.System, U.EntityRef
  AssignedSystemRoleKindSlot: JournalReviewSystemRoleKindDomain, ByValue

predicate:
  the admitted holder is selected to supply the contribution denoted by
  the assigned system-role kind under JournalReview assignment conditions

applicability:
  JournalReview-2026 assignment episodes
```

`JournalReviewSystemRoleKindDomain` is the exact local C.3 domain defined by A.2. `CoolingPumpKind`, `ShortAssignmentKind`, and arbitrary local kinds cannot fill this species' assigned-kind slot merely because each is a `U.Kind`.

#### A.2.1:4.2 - A Stronger Species Retains Its Real Participants

When an appointment, organizational position, installation locus, or work commission changes the predicate or occurrence identity, the domain species declares that participant. For example, conditional on a domain pattern already admitting `ProjectReviewCommission` and its appointment predicate:

```text
ProjectReviewAppointmentAssignment <: U.SystemRoleAssignment

RelationSignature:
  HolderSystemSlot: U.System, U.EntityRef
  AssignedSystemRoleKindSlot: ProjectReviewSystemRoleKindDomain, ByValue
  ReviewCommissionSlot: ProjectReviewCommission, U.EntityRef

predicate:
  the holder is appointed under the identified commission to supply the
  contribution denoted by the assigned system-role kind
```

The commission is a participant because this admitted species makes it one. A decision episteme, roster row, or evidence item about the appointment is not thereby the commission or another participant.

If no current pattern admits the proposed participant kind or direct predicate, return `A.6.RCD missing-governor` for that specialized assignment. Do not hide the gap in an optional field.

#### A.2.1:4.3 - Occurrence Identity

An occurrence of a declared species begins when that species' direct predicate starts obtaining for fixed participant values. It continues over the maximal uninterrupted predicate-true interval. It ends when a participant changes or the predicate ceases to obtain. A later resumption is another occurrence even when every participant value is the same.

The identity rule is not a database tuple. A context field ending in `...SystemRoleAssignmentRef` uses `U.RelationRef constrained to U.SystemRoleAssignment` and resolves to the exact occurrence while keeping its declared species recoverable. It does not create the occurrence or erase its species.

An assignment assertion or occurrence description can state `assignmentInterval` with a temporal reference, start, end or explicit open end, and continuity claim. Closing an open interval later refines the same description when world-side obtaining was uninterrupted. Missing evidence yields `unknown`; it does not split the occurrence. A demonstrated non-assignment interval ends it.

Keep ordinary interval content here. When a positive temporal aspect itself becomes a relied-on object—its temporal reference, validity or currentness window, duration, cadence, rhythm, or interval structure—use `C.27.TA` for that aspect and keep the assignment occurrence separate. Use `C.27` only for the different question of whether a temporal claim is adequate. Neither route creates or extends the assignment.

Taxonomy, scheme, `KindSignature`, assertion, interval description, and selected publication form can be cited when they matter to interpretation or evidence. Only the species' declared participants and predicate determine world-side occurrence identity.

#### A.2.1:4.4 - One Strong Occurrence, Not a Generic Duplicate

If Alice has overlapping `Commission-A` and `Commission-B`, then `ReviewAssignment-A` and `ReviewAssignment-B` are two `ProjectReviewAppointmentAssignment` occurrences even when holder and `ReviewerSystemRole` match. Their commission participants and predicates distinguish them.

“Alice is the reviewer” is a readable existential projection over any qualifying occurrence. It is not a third assignment occurrence. Do not create a generic two-participant assignment beside either appointment simply to support that sentence or F.6.

Every admitted species supplies the common projection:

```text
holderSystem(RA : U.SystemRoleAssignment) = RA.HolderSystemSlot
assignedSystemRoleKind(RA) = RA.AssignedSystemRoleKindSlot
```

The projection does not erase additional participants or assert that another occurrence exists.

#### A.2.1:4.5 - Assignment and Classification Are Independent

A C.3.2 judgment classifies one system under one local system-role kind for one signature edition and slice. An assignment occurrence relates participants under its species predicate. Either can be current without the other.

An assignment can be one membership feature only when the exact local `KindSignature` explicitly cites that independently obtaining predicate. `RoboticsAssignment-1` alone makes neither `RoboticsEngineerSystemRole` nor `EngineerSystemRole` true. A later `U.SubkindOf` result records monotonic implication among independently evaluated judgments; it creates no broader assignment.

#### A.2.1:4.6 - Demand-Driven Materialization

Ordinary use can stop at:

```text
During Shift-17, Robot-7 is assigned as inspector under
MaintenanceInspectionAssignment.
```

Expose an occurrence identifier only when a receiver must distinguish episodes, cite the assignment as a participant, compare assertions, or preserve provenance. If a required participant or the predicate cannot be recovered, lower the claim or return the exact missing governor. Never insert a dummy value or broaden the assigned-kind domain.

#### A.2.1:4.7 - Direct Neighboring Relations

| Current question | Direct exit | Why it stays separate |
| --- | --- | --- |
| Does the holder count under the system-role kind? | `A.2`, `C.3.2` | Classification is a four-input judgment, not assignment obtaining. |
| Can the holder do the Work? | `A.2.2` capability and fit | Assignment does not create ability. |
| Does the assignment satisfy a state predicate? | `A.2.5` | State has its own predicate, relation occurrence, and truth interval. |
| Which Method admits or organizes the Work? | `A.3`, `A.15` | Method and MethodDescription do not assign a holder. |
| Was Work performed under this assignment? | `A.15.1`, `F.6` | Work is a dated occurrence and attribution is another relation. |
| Does a decision or installation help constitute this species? | the direct domain relation and species predicate | It matters only when the admitted species says so; an episteme is not a generic participant. |
| Is the holder responsible, committed, permitted, authorized, or able to access something? | the admitted direct domain predicate, `A.2.8`, `A.2.8.PER`, or `missing-governor` | The assignment can be an applicability ground without being the result or bearer. |
| What supports use of the assignment claim? | evidence, reliance, provenance, source-use, or publication pattern | Support concerns the assertion; it does not make the relation obtain. |
| Does a model-use structure change this receiving interpretation? | `A.1.1` plus the receiving assertion or use | It is not an optional participant of the assignment family. |

Assignment-establishing world-side relations and epistemic support are not interchangeable. A constituting decision or installation occurrence affects a species only when its direct predicate says so. Evidence can support relying on the assertion without constituting the assignment.

#### A.2.1:4.8 - Performed-Work Attribution

F.6 retains one direct attribution with the renamed family:

```text
performedUnderAssignment(W : U.Work, RA : U.SystemRoleAssignment)
actualPerformerSystem(W, RA) = RA.HolderSystemSlot
```

`SystemRoleAssignmentSlot` in F.6 accepts any admitted assignment species because its `ValueKind` is the family `U.SystemRoleAssignment`. It is not a union of a generic relation and stronger non-assignment values. `ReviewWork-A` can be attributed to `ReviewAssignment-A`, and `ReviewWork-B` to `ReviewAssignment-B`, without creating generic duplicates.

Assignment does not prove that Work occurred. Work does not alter assignment identity. Source wording such as `RoleEnactment` is recovered as the dated Work occurrence, exact assignment, admitted performer system, and `performedUnderAssignment` relation; no duplicate run-time kind or occurrence is introduced.

#### A.2.1:4.9 - Source Context Shorthand

`Holder#Role:Context@Window` is source notation, not the assignment ontology. Apply E.10.ROLE to recover the system-role kind or another meaning. Recover the object denoted by `Context` and its direct relation separately. It can be an actual system or Work locus, a claim scope, or a selected `BoundedModelUseStructure`; these have different kinds and uses.

If one assignment species genuinely depends on a structure or locus, its direct pattern declares that participant and stronger identity law. Otherwise keep the recovered object in the receiving assertion or use; never invent a generic context participant.

### A.2.1:5 - Archetypal Grounding

#### A.2.1:5.1 - Robot Assigned for One Inspection Shift

The maintenance domain declares a simple species and an occurrence:

```text
MaintenanceInspectionAssignment <: U.SystemRoleAssignment
  HolderSystemSlot: U.System, U.EntityRef
  AssignedSystemRoleKindSlot: MaintenanceSystemRoleKindDomain, ByValue

InspectionAssignment-17:
  HolderSystemSlot: Robot-7
  AssignedSystemRoleKindSlot: InspectorSystemRole
  assignmentInterval: [2026-07-13T09:00, 2026-07-13T17:00]
```

The two fields designate the species participants. The interval is assertion content about the occurrence extent. `MaintenanceSystemRoleVocabulary-2026`, its effective scheme, and the relevant `KindSignature` can be cited to interpret the claim without becoming participants. Sensor capability, assignment state, inspection Method, and any performed inspection Work remain separate.

#### A.2.1:5.2 - Repeated Assignment Episodes

Robot-7 is assigned again on the next day under the same species and kind. The predicate does not obtain continuously across the two shifts, so the second shift is another `U.SystemRoleAssignment` occurrence. Reusing one staffing-row identifier cannot collapse the episodes.

#### A.2.1:5.3 - Motor Assigned as Drive

For a current equipment assignment, declare the species and identify its occurrence: `Motor-M1` is the holder and `DriveMotorSystemRole` is the assigned-kind value. `PumpAssembly-A` remains the actual assembly System and Work locus rather than a generic context participant. If installation in that exact assembly distinguishes assignment identity, the domain species must declare a real installation-locus participant and predicate, and the occurrence must supply its actual value.

The separate claim “Motor-M1 drives PumpAssembly-A during PumpRun-17” is not established by assignment. Until a domain predicate supplies its participants, applicability, and identity, return `missing-governor` for the motor-drive-functioning relation. Torque capability, installation Work, pumping Work, and the assignment remain usable independently.

#### A.2.1:5.4 - DDD Model-Use Structure Changes a Receiving Interpretation

Two software contexts each use `ApproverSystemRole`. `ApprovalService-2` can hold an assignment that obtains in the fulfilment context; name both the occurrence and its declared species. A receiving interpretation use can cite both the assignment-occurrence reference and `Orders-Fulfilment-ModelUseStructure` when the selected structure changes that use.

The structure was independently recovered under A.1.1. It neither assigns the service nor performs approval Work, and it does not enter the generic family. A future species that truly depends on it must declare the structure as a required participant and state the stronger predicate and identity law.

#### A.2.1:5.5 - Two Review Commissions

Alice is independently admitted as `U.System`. `Commission-A` and `Commission-B` satisfy the admitted `ProjectReviewCommission` kind. Two overlapping `ProjectReviewAppointmentAssignment` occurrences have the same holder and `ReviewerSystemRole` but different commission participants.

`ReviewWork-A` is attributed to `ReviewAssignment-A`; `ReviewWork-B` is attributed to `ReviewAssignment-B`. “Alice is the reviewer” can remain a recognition sentence, but it does not merge the appointments or identify which Work belongs to which occurrence.

#### A.2.1:5.6 - Reviewer and Review Report

`ReviewService-4` holds an exact review assignment and performs `ReviewWork-82` under it through F.6. `ReviewReport-82` is a separately identified `U.Episteme`. When the Work first constitutes that episteme and the inception claim matters, A.15.PROD recovers the relation among Work, change, and identity. A later evidence relation can use the report; the report never fills `HolderSystemSlot` merely because it is useful.

### A.2.1:6 - Bias Annotation

| Bias risk | Failure | Repair |
| --- | --- | --- |
| Record-first bias | A roster row or identifier is treated as the assignment occurrence. | State the species predicate and uninterrupted occurrence identity; keep the row as an assertion or publication. |
| Universal-signature bias | One broad root signature hides several participant laws. | Admit direct species with exact local domains and real participants. |
| Generic-duplicate bias | A stronger appointment is accompanied by a weaker assignment occurrence. | Let the specialized occurrence itself satisfy `U.SystemRoleAssignment` and use its common holder projection. |
| Universal-context bias | Every assignment receives a context or optional model-use participant. | Keep context-denoted objects in their direct relation; declare a required participant only in a genuinely dependent species. |
| Assignment-as-classification drift | Assignment is used as proof of kind membership. | Evaluate the C.3.2 judgment; use assignment only if the signature names its independently obtaining predicate. |
| Assignment-as-Work drift | Current assignment is treated as completed Work. | Name `W : U.Work`, exact `RA`, and `performedUnderAssignment(W, RA)`. |
| Episteme-as-holder drift | A standard, report, model, or dataset fills `HolderSystemSlot`. | Keep the episteme in its evidence, reliance, external-rule, source-use, or publication relation. |
| Responsibility or authority drift | The kind or assignment is treated as the responsibility or authority result. | Cite the direct admitted predicate and actual bearer, or return `missing-governor`. |

### A.2.1:7 - Working Guidance

1. State the assignment claim in ordinary language.
2. Select or admit the direct assignment species; do not start from a universal root signature.
3. Confirm the holder and exact local system-role-kind domain.
4. Declare every real additional participant and the species predicate; reject placeholder fields.
5. Decide whether a receiver needs explicit occurrence identity. Stop at the readable assertion when it does not.
6. Distinguish repeated episodes by uninterrupted predicate obtaining, not by storage identifiers.
7. Keep classification, capability, state, Method, Work, responsibility, commitment, permission, authority, access, evidence, reliance, and publication under their direct patterns.
8. Use context fields ending in `...SystemRoleAssignmentRef` only with `U.RelationRef constrained to U.SystemRoleAssignment` and an exact recovered occurrence.
9. For source shorthand, recover each hidden value by kind and relation before relying on it.

### A.2.1:8 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-A2.1-1` | `U.SystemRoleAssignment` has no permissive root `RelationSignature`; every occurrence belongs to one directly declared species. |
| `CC-A2.1-2` | Every species declares `HolderSystemSlot : U.System` and one declaration-local `AssignedSystemRoleKindSlot` with an exact local system-role-kind domain. |
| `CC-A2.1-3` | Every additional participant changes the predicate or occurrence identity and has an admitted kind and complete SlotSpec. |
| `CC-A2.1-4` | The direct predicate, applicability, and occurrence-identity rule are explicit. |
| `CC-A2.1-5` | One occurrence is the maximal uninterrupted predicate-true interval for fixed participant values; a demonstrated gap creates another occurrence. |
| `CC-A2.1-6` | `assignmentInterval` describes known extent and is not a participant or proof of obtaining. Ordinary interval content stays local; a relied-on positive temporal aspect uses `C.27.TA`, while temporal-claim adequacy uses `C.27`. |
| `CC-A2.1-7` | Taxonomy, scheme, signature, assertion, evidence, publication, and model-use structure are not generic assignment participants. |
| `CC-A2.1-8` | A specialized occurrence is itself a `U.SystemRoleAssignment`; no weaker generic duplicate is created. |
| `CC-A2.1-9` | Every species declares the common holder slot by which F.6 projects the actual holder from an occurrence, without erasing additional participants. |
| `CC-A2.1-10` | Classification and assignment remain independent; assignment is a criterion feature only when the signature explicitly says so. |
| `CC-A2.1-11` | Performed Work uses `performedUnderAssignment(W, RA)` and the actual performer is `RA.HolderSystemSlot`. |
| `CC-A2.1-12` | A `...SystemRoleAssignmentRef` field is typed by `U.RelationRef constrained to U.SystemRoleAssignment`, resolves to one exact occurrence, and keeps its declared species recoverable. |
| `CC-A2.1-13` | Missing evidence yields unresolved or `unknown`; only demonstrated predicate failure ends the occurrence. |
| `CC-A2.1-14` | Reduced use stops before explicit individuation when no receiver needs an assignment reference. |

### A.2.1:9 - Common Anti-Patterns

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| `Alice is reviewer`, used as assignment identity | It names neither species nor occurrence. | Recover the direct species and the obtaining occurrence needed by the receiver. |
| One universal binary assignment relation over `U.Kind` | It admits arbitrary kinds and hides stronger participant laws. | Use one exact local assigned-kind domain in every direct species. |
| Generic assignment plus appointment occurrence | One world-side episode receives two competing identities. | Make the appointment species a subtype of `U.SystemRoleAssignment`; use its holder projection. |
| One assignment row reused for every shift | Storage identity collapses repeated occurrences. | Distinguish maximal uninterrupted predicate-true intervals. |
| Assignment proves Work | Holding is confused with dated performance. | Name exact Work and the F.6 relation. |
| Durable `RoleEnactment` object | It duplicates Work and attribution. | Recover the source wording to Work, assignment, performer, and `performedUnderAssignment`. |
| Report holds a system-role assignment | An episteme is made a holder by usefulness. | Use its direct evidence, result, source-use, or publication relation. |
| Optional `ContextSlot` everywhere | Unrelated locality, scope, structure, and locus meanings collapse. | Recover the denoted object and declare it only when a direct species truly depends on it. |

### A.2.1:10 - Consequences

| Gain | Cost or tradeoff |
| --- | --- |
| Simple assignments keep two participants. | Each bounded vocabulary must define its exact system-role-kind domain. |
| Strong appointments preserve their real identity. | A domain must admit every additional participant and predicate it relies on. |
| All species support F.6 through one holder projection. | Receivers must preserve both the assignment occurrence and its declared species rather than replace them with a generic record. |
| Repeated episodes remain distinguishable. | Reliance-bearing use must recover uninterrupted predicate history, not just a row key. |
| Interpretation and evidence remain separate from world-side participants. | Assertions must cite their actual semantic and evidence basis when the receiver needs it. |
| Ordinary prose remains lightweight. | Authors must decide when explicit occurrence identity is required. |

### A.2.1:11 - Rationale

The family is needed because system classification and assignment occurrence answer different questions. Direct species are needed because the participant law for a simple shift assignment differs from the law for an appointment tied to a real commission, position, or locus.

One root signature would either reject legitimate stronger assignments or hide them behind optional slots. A generic occurrence beside a stronger one would duplicate the world-side episode and make F.6 choose between competing identities. Subtyping the direct species under `U.SystemRoleAssignment` preserves one assignment identity and one common holder projection.

Predicate obtaining, assertion, explicit individuation, identifier assignment, evidence, and publication also answer different questions. Keeping them separate lets evidence be corrected without rewriting the occurrence and lets ordinary recognition text remain shorter than a full relation declaration.

### A.2.1:12 - SoTA-Echoing

| Practice line | Source and status | FPF mutation | Practical consequence |
| --- | --- | --- | --- |
| Current foundational ontology distinguishes role-like classification, relation aspects, and explicit relation occurrences. | Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint; current comparator, not imported hierarchy. | Keep local system-role kinds, direct assignment species, SlotKinds, and performed Work distinct under FPF identity laws. | The same system can receive several assignments without becoming several systems. |
| Relation modeling distinguishes a family from concrete relation signatures with different participant laws. | Current A.6.0, A.6.5, and A.6.REL line. | Let directly declared species carry the exact participant and predicate law while the family provides the common ValueKind used by receivers. | A commission-sensitive appointment remains usable by F.6 without a duplicate generic relation. |
| DDD makes interpretation local to an actual model-use organization. | Evans, *Domain-Driven Design Reference* (2015) and current context-mapping practice. | Cite a selected `BoundedModelUseStructure` only in a receiving claim it changes, unless a separately admitted species truly requires it. | Ordinary physical and organizational assignments gain no fabricated context participant. |

### A.2.1:13 - Relations

**Builds on:** `A.2` for system-role kinds and their exact local domains; `A.6.REL` for relation obtaining and occurrence identity; `A.6.5` for complete SlotSpecs; and `C.2.1` for assertions and interpretation epistemes.

**Coordinates with:** `A.2.2` for capability; `A.2.5` for assignment state; `A.2.7` for relations among system-role kinds; `A.3` and `A.15` for Method and Work; `A.15.1` and `F.6` for performed-Work attribution.

**Uses when current:** `A.1.1` for a selected model-use structure; `C.27.TA` when a positive temporal aspect is itself relied on; `C.27` for temporal-claim adequacy; `C.3.3`, `F.9`, and `A.6.9` for cross-context use; and direct responsibility, commitment, permission, authority, access, decision, evidence, reliance, provenance, currentness, and publication patterns.

**Does not replace:** a local system-role kind, a separate System-classification judgment, assignment state, capability, Method, Work, responsibility, commitment, permission, authority, access, assignment decision, evidence, publication, or their descriptions.

### A.2.1:End

