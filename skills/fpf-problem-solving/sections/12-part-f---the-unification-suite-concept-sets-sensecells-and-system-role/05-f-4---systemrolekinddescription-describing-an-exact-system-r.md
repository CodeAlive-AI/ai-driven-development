## F.4 - SystemRoleKindDescription — Describing an Exact System-Role Kind

> **Type:** Definitional (D)
> **Status:** Stable in the current FPF
> **Normativity:** Normative unless marked informative

### F.4:0 - Use This When

**Plain name.** Description of a system-role kind.

Use F.4 when a project needs a short, reusable description that makes one exact local system-role kind recognizable, teachable, and checkable. The described kind is a C.3 kind whose candidates must first be independently admitted as `U.System`. A candidate may be, for example, a person, team, organization, or non-human technical object; `SystemRole` does not mean “technical system only.”

Typical moments:

- a project has a durable kind name such as `ReviewerSystemRole`, `OperatorSystemRole`, `InspectorSystemRole`, `TransformerSystemRole`, or `ShipyardCoordinatorSystemRole`, but readers cannot recover the named practice or source boundary in which the kind is constituted, its stable work-facing contribution distinction, `KindSignature`, or work-facing boundary;
- a MethodDescription names a required system-role kind, but readers cannot tell which exact local kind must classify a candidate before an assignment can be checked;
- a kind name is starting to carry assignment, capability, Method, Work, permission, responsibility, evidence, publication, or status claims that belong elsewhere; or
- source prose says that a report, standard, dataset, theorem, dashboard, publication, or requirement has a “role”, and the writer must recover whether that wording denotes a system-role kind at all.

**Primary EntityOfConcern.** A `SystemRoleKindDescription` is one `U.Episteme` constituted under C.2.1. Its exact EntityOfConcern is one local system-role kind. Its ClaimGraph names the practice or source boundary in which the kind is constituted, its stable work-facing contribution distinction, current `KindSignature` edition, effective `U.ReferenceScheme`, and only the neighboring relations needed by the described use. The description is not the kind, a classification judgment, assignment occurrence, holder system, capability, MethodDescription, performed Work, status-use relation, or publication form.

**Primary working reader.** The first reader is an engineer-manager, analyst, Method author, or pattern author who must help people recognize the kind while keeping kind, candidate classification, assignment, capability, Method, Work, evidence use, status use, and publication use distinct.

**First useful move.** Name the exact local system-role kind, the practice or source boundary in which it is constituted, its stable work-facing contribution distinction, the current `KindSignature` edition, and the shortest recognition explanation needed by the next classification, assignment, Method, Work, naming, or cross-local claim.

**What goes wrong if missed.** A description card becomes a hidden procedure, staffing record, access policy, permission badge, responsibility claim, evidence relation, status assertion, or Work log. Then one word recreates a universal role ontology and a second role-like ontology for epistemes, publications, statuses, and relation positions.

**What this buys.** A project gets a compact, readable description while operational claims remain at their direct loci. The kind stays recognizable; classification and assignment stay checkable; capability, Method, Work, evidence, status, responsibility, and publication claims stay inspectable instead of being smuggled into the name.

**Not this pattern when.**

- If the current question is whether a local system-role kind exists, how it is identified, or whether one candidate satisfies it, use A.2 with C.3 and C.3.2.
- If the current question is whether one admitted system and one exact local kind participate in an obtaining assignment, use A.2.1.
- If one assignment may satisfy one state condition during a window, use A.2.5.
- If the current question concerns admission substitution, incompatibility, qualification, a bundle, or another relation among system-role kinds, use A.2.7.
- If the current question is capability, use A.2.2.
- If it is about a Method, MethodDescription, WorkPlan, or performed Work, use A.3 or A.15 and the direct neighboring pattern.
- If an episteme is used as evidence, source, standard, requirement, publication, assurance input, status bearer, gate input, or decision input, use the direct relation. Do not classify the episteme as a system-role holder by wording.
- If only a durable name is needed, use F.18.
- If the current question relates two exact local system-role kinds, use C.3.3. If it relates two exact source-local senses, address them as F.17 `SchemeSenseCell` values and use F.9. Scheme difference or shared spelling alone triggers neither relation.
- If bare *role* may mean a relation participant, declaration slot, representation position, ordinary wording, or another object, use E.10.ROLE and A.6.RSIR where relation recovery is needed.

### F.4:1 - Problem Frame

A local system-role kind often needs a recognizable description before people can classify a candidate, assign a system, compare local kinds, or use the kind in a Method condition. A name such as `InspectorSystemRole` is not self-explanatory. Readers need the practice or source boundary in which the kind is constituted, its stable work-facing contribution distinction, current `KindSignature`, effective scheme, first recognition cues, and boundary to neighboring claims.

The recurring failure is to make the description carry too much. A compact card is tempting: put kind, status, permission, responsibility, evidence, capability, Method, assignment, Work, and publication cues into one “assignable” template. That convenience creates duplicate ontology. A standard used as a requirement source becomes a “standard role”; a report used as evidence becomes an “evidence role”; an access-control label becomes a system-role kind; a kind name becomes proof of capability or performed Work.

F.4 instead treats the description as an episteme about one exact local kind. It may cite neighboring relations but does not absorb them.

### F.4:2 - Problem

Without this pattern:

1. **Description and kind collapse.** The description is treated as the local system-role kind.
2. **Description and classification collapse.** A card is treated as proof that one candidate satisfies the kind criterion.
3. **Description and assignment collapse.** A kind name or card is treated as proof that one system has an assignment.
4. **Description and capability collapse.** A kind name is treated as evidence that a system can do the Work.
5. **Description and Method collapse.** Kind criteria become a hidden procedure or MethodDescription.
6. **Description and performed Work collapse.** A card is treated as evidence that Work happened.
7. **Status and episteme uses become system roles.** Publications, standards, datasets, claims, and statuses acquire fake system-role classifications because they matter to reasoning.
8. **Relation positions become system roles.** Participant meanings, declaration slots, interface places, and representation positions are mistaken for system-role kinds.
9. **Same-spelled local kinds collapse.** Shared spelling is treated as one kind although two named practices or sources constitute two exact local kinds and no C.3.3 relation between them has been established.

### F.4:3 - Forces

| Force | Tension |
| --- | --- |
| Recognition versus ontology | A description must be easy to read but cannot replace the kind, classification judgment, assignment, capability, Method, or Work occurrence. |
| Local identity versus reuse | A system-role kind is distinguished by its explicit practice or source boundary and stable work-facing contribution, while a later use may need a C.3.3 relation between exact local kinds or an F.9 relation between exact F.17 local-sense cells. |
| Compactness versus completeness | A useful description is small, but a stronger receiving claim may need state, capability, Method, assignment, evidence, or status checks. |
| Open-world use versus form burden | Some uses need only a recognition paragraph; stronger uses need explicit neighboring references without pretending every possible relation is current. |
| Work-facing classification versus episteme use | An admitted system may satisfy a system-role kind and participate in an assignment. An episteme is instead used through evidence, source, publication, requirement, explanation, assurance, or status relations. |

### F.4:4 - Solution

Constitute one `SystemRoleKindDescription` through C.2.1. Its ClaimGraph describes one exact local system-role kind, and that kind is its EntityOfConcern. The ClaimGraph names the practice or source boundary in which the kind is constituted, its stable work-facing contribution distinction, current `KindSignature` edition, and effective `U.ReferenceScheme`. The description gives readers enough to recognize and check the kind while routing neighboring claims to their direct rules.

The following is a content checklist, not a relation signature or mandatory record.

**Always make recoverable:**

- the described local system-role kind;
- the practice or source boundary in which it is constituted and its stable work-facing contribution distinction;
- the current `KindSignature` edition and effective reference scheme;
- a short recognition explanation;
- the full A.1 range of possible candidate systems, using examples only when helpful;
- the smallest direct-feature criteria or invariants needed by the current use; and
- the explicit boundary: the description asserts no classification, assignment, capability, Method, Work, evidence, status, permission, responsibility, publication, or relation-position occurrence.

**Add only when the current use depends on them:**

- a `SystemRoleAssignmentStatePredicate` or state-relation reference under A.2.5;
- capability-condition references under A.2.2;
- Method or MethodDescription references under A.3 and A.15;
- durable-name or lineage references under F.18;
- C.3.3 or F.9 Bridge references; and
- a selected `BoundedModelUseStructure` only when that structure changes the described interpretation or receiving use.

These are claims or references in an episteme. They are not `SlotSpec` declarations and add no participant to `U.SystemRoleAssignment` or another relation. A card, table row, Method appendix, or pattern section may publish the description; the publication form and carrier remain separate from the episteme.

#### F.4:4.1 - Content Meanings

| Content element | Meaning |
| --- | --- |
| Described system-role kind | The exact local `U.Kind` that is the episteme's EntityOfConcern. |
| Local identity basis | The named practice or source boundary and stable work-facing contribution distinction that distinguish this kind from same-spelled local kinds. |
| Kind criterion | The exact current `KindSignature` edition used to judge candidates directly. |
| Effective scheme | The by-value interpretation scheme used for the description's vocabulary; it is not a kind-identity authority. |
| Recognition explanation | A first-minute explanation that distinguishes this kind from neighboring kinds and objects. |
| Candidate-system range | Candidates must first be admitted as `U.System`; people, teams, organizations, and non-human technical objects are possible examples, not four subkinds declared here. |
| Conditional neighboring references | Add neighboring references for assignment state, capability, Method, naming, and Bridges only when the receiving use depends on them. |
| Non-inference boundary | Explicit separation from classification, assignment, Work, evidence, status, permission, responsibility, publication, and relation-position claims. |

A quick local description may stop after the always-recoverable content. A consequence-bearing Work-admission use requires only the neighboring relations it actually needs.

#### F.4:4.2 - Description versus Neighboring Values

| Current question | Direct locus |
| --- | --- |
| What local system-role kind is this, and does a candidate satisfy it? | A.2 with C.3 and C.3.2 |
| Which admitted system is assigned to it, and for which uninterrupted occurrence? | A.2.1 |
| Does this assignment satisfy this state condition during the required window? | A.2.5 |
| Can the system do the relevant Work? | A.2.2 |
| Which Method, MethodDescription, WorkPlan, or Work occurrence is current? | A.3, A.15, A.15.1, and A.15.2 |
| Which substitution, incompatibility, qualification, bundle, or other relation among kinds obtains? | A.2.7 |
| What durable name should the kind or description have? | F.18 and F.5 |
| How are two exact local kinds related? | C.3.3, only when its predicate obtains |
| How are two exact source-local senses related? | F.9 between exact F.17 `SchemeSenseCell` values, only when its predicate obtains |
| How is an episteme used in evidence, source, requirement, status, publication, or assurance claims? | The exact direct relation |
| Which relation position admits which filler kind? | A.6.5 and A.6.RSIR |

F.4 points to these loci; it does not copy their ontology.

Keep the description episteme, the exact local system-role kind it describes, the `KindSignature` that states the membership criterion, the effective scheme used to read the description, and any classification judgment about a candidate separate. Add an F.17 `SchemeSenseCell` only when a later use needs a stable local-sense address; cite a `LocalSenseBasisRelation` only when that relation actually obtains. An ordinary F.4 description requires neither.

#### F.4:4.3 - Positive Construction Rule

Write a description in this order:

1. Name the described local system-role kind, the practice or source boundary in which it is constituted, and its stable work-facing contribution distinction.
2. Name the current `KindSignature` edition and effective reference scheme.
3. Give one short recognition paragraph, including the broad A.1 system range when a cold reader could narrow it incorrectly.
4. State the smallest direct criteria or invariants that distinguish the kind.
5. State what the description does not assert about classification, assignment, capability, Method, Work, evidence, status, permission, responsibility, publication, or relation positions.
6. Add neighboring references only when the receiving use depends on them.
7. Use F.18 for a durable public name. Use C.3.3 only when an actual relation between exact local kinds is current; use F.9 only when the receiving claim relates distinct F.17 local-sense cells.

### F.4:5 - Invariants

1. **One described kind.** A `SystemRoleKindDescription` describes exactly one local system-role kind.
2. **Direct kind identity.** The practice or source boundary and stable work-facing contribution distinction remain recoverable; taxonomy rows and schemes are evidence or interpretation aids, not identity authorities.
3. **Description boundary.** The description is a `U.Episteme`; it is not the kind, candidate, classification judgment, assignment, holder system, capability, Method, Work, or status-use relation.
4. **System range.** A candidate must independently pass A.1 as `U.System`. No description or kind name performs that admission, and `SystemRole` does not narrow the candidate to non-human technical systems.
5. **No hidden assignment.** Classification under a local kind neither creates nor proves a `U.SystemRoleAssignment` occurrence.
6. **No hidden capability.** Capability requirements may be cited, but the description proves no capability.
7. **No hidden Method.** Method requirements may be cited, but the description is not a MethodDescription.
8. **No hidden Work.** The description may support later Work-attribution checks, but it is not evidence that Work occurred.
9. **No status or episteme-use fusion.** Status, evidence, source, requirement, publication, and assurance uses remain direct relations, not another description branch.
10. **Position discipline.** Bare *role* that denotes participation, a declaration slot, interface place, or representation position is recovered through E.10.ROLE and A.6.RSIR rather than made a system-role kind.
11. **Name after meaning.** Durable naming follows F.18 only after the exact kind, description, scheme, and local sense are recovered.

### F.4:6 - Reasoning Primitives

Use these schemas as thinking checks.

```text
SystemRoleKindDescription D describes local system-role kind K
  -> D is a C.2.1 episteme about K; D is not K or a classification judgment.
```

```text
Candidate system X satisfies the current KindSignature of K
  -> this may support a classification judgment about X and K;
     it creates neither an assignment nor performed Work.
```

```text
Assignment A relates admitted holder system X to K
  -> A is an occurrence of an exact species under U.SystemRoleAssignment;
     D establishes neither A nor X's system admission.
```

```text
D cites capability requirement CapReq or Method requirement MReq
  -> apply A.2.2 or the direct Method pattern; the citation proves neither result.
```

```text
Source says “episteme X has role Y”
  -> use E.10.ROLE to recover the direct episteme-use relation or ordinary wording
     before considering any system-role kind or assignment.
```

### F.4:7 - Worked Cases

#### F.4:7.1 - Pump Inspector System Role

`PumpInspectorSystemRoleKindDescription` is a C.2.1 episteme whose EntityOfConcern is `PumpInspectorSystemRole@PlantAMaintenance`. Its contribution identity is supplying the pump-condition inspection judgment used before a Plant A maintenance decision. The description names `PlantA-PumpInspector-KindSignature-v4` and `Plant-A-Maintenance-Scheme`. Under that signature, a candidate counts only when it is already admitted as a `U.System` and two Plant A domain claims obtain: the reading predicate says that this System obtains readings for the named pump and declared condition characteristics in the applicable inspection situation; the judgment predicate says that this System returns the named pre-maintenance judgment from those readings. Each predicate declaration supplies participant meanings and applicability, and the current case supplies the satisfying facts. Use `A.6.F` only if source wording first hides those claims behind *function*; it establishes neither predicate. If either predicate or its case facts cannot be recovered, record the exact A.6.RCD `missing-governor` or missing-information result instead of classifying the candidate. A maintenance technician, inspection robot, or service team is only an example until those same conditions are checked.

The description says the kind concerns pump-condition inspection and does not itself denote repair. It may cite pump-inspection capability conditions or an inspection Method when a receiving Work claim needs them. Its boundary says that an inspection report is an episteme used through evaluation, evidence, source, or publication relations, not a system-role holder.

The description makes `PumpInspectorSystemRole` recognizable. It does not say that Robot-7 satisfies the kind, has an assignment, is capable of inspecting, has permission or readiness to inspect, enacted a Method, or performed Work. Those claims use C.3.2, A.2.1, A.2.2, A.2.8.PER, A.15, and the applicable evaluation or evidence relations.

#### F.4:7.2 - Reviewer System Role and Review Report

`ReviewerSystemRoleKindDescription` may describe `ReviewerSystemRole@PatternReview-2026`, the local kind identified by the contribution of supplying a reasoned pattern-review judgment against the declared scales. Under `PatternReview-2026-Reviewer-KindSignature-v2`, a candidate counts only when it is already admitted as a `U.System` and two review-domain claims obtain: the comparison predicate says that this System compares the named pattern claims with each selected scale in the applicable review situation; the result predicate says that it returns the named reasoned judgment with the assessed values or defects. Each declaration supplies participant meanings and applicability, and the current case supplies the satisfying facts. `A.6.F` is used only to unpack still-ambiguous function wording and establishes neither claim. If a predicate is missing, record the A.6.RCD `missing-governor`; if case facts are missing, record the corresponding unresolved result. This condition can be checked without asserting that any review appointment or dated review Work already exists.

Alice's classification under that kind, any review appointment she holds, any dated review Work she performs, and any report used as evidence remain four separate claims. This compact description names none of their occurrence identities.

Use:

- A.2 with C.3 for the local kind and direct classification;
- F.4 for the description episteme;
- A.2.1 when a particular review assignment must be identified;
- A.15.1 and F.6 when a particular dated review Work occurrence and the assignment under which it was performed must be identified; and
- A.10, B.3, G.6, or another direct relation for the report's evidence or assurance use.

The report is not a system-role holder and does not acquire an “evidence role.”

#### F.4:7.3 - Standard Used as a Specification or Source

The sentence “Standard S has the architecture-standard role in this Work” is unsafe if it classifies the standard episteme as a system-role holder. Rewrite the actual claim: the exact edition of Standard S is used as a specification, external rule, premise, or source for named claims. A standard may constrain or support a claim through that direct relation. No system-role kind or assignment is needed unless a separately admitted system really satisfies and is assigned to one.

#### F.4:7.4 - Access Role Is Not Automatically a System Role

RBAC *role* often names a permission grouping. If the current claim concerns permission or access standing, use the direct policy, deontic, access, or status relation. Treat a local access term as a system-role kind only when its own C.3 identity and criterion are current and a receiving Work claim actually needs that classification. Even then, permission and assignment remain separate.

### F.4:8 - Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Description as kind admission | A card is treated as if it constituted the local kind. | Establish the kind under A.2 with C.3; keep F.4 for its description. |
| Description as classification | “The card lists Alice, so Alice is a reviewer.” | Evaluate the exact candidate under the current `KindSignature`. |
| Description as assignment | “The inspector is assigned” appears without an exact holder, kind, direct species, and assignment occurrence. | Use A.2.1; keep F.4 for description of the kind. |
| Description as capability proof | “ReviewerSystemRole can verify formal models.” | Put capability under A.2.2; F.4 may cite the requirement. |
| Description as Method | The description contains a procedure. | Move the procedure to Method or MethodDescription patterns. |
| Description as Work evidence | A card is cited as proof that review occurred. | Recover the exact `U.Work` occurrence and evidence relation. |
| Episteme as system-role holder | A report, standard, dataset, theorem, dashboard, or publication is said to hold a role. | Recover the exact evidence, source, standard, requirement, publication, status, or assurance relation. |
| Status-template fusion | A status, permission, or evidence standing becomes another kind-description branch. | Use the direct status, policy, permission, or evidence relation. |
| Relation position as system role | “The subject role in this relation …” | Recover participant meaning, `SlotKind`, `ValueKind`, and `RefKind` under A.6.RSIR and A.6.5. |
| Bridge by label | Shared spelling in two practices or sources is treated as one local kind. | Keep two kinds. Use C.3.3 only when an actual relation between those exact kinds obtains. If a separate wording or local-sense relation is current, address the exact F.17 cells and use F.9; shared spelling triggers neither relation. |

### F.4:9 - Consequences

**Benefits.**

- Descriptions stay short enough for practice while preserving the ontology.
- Part F naming and Bridge patterns can cite descriptions without inheriting classification, assignment, capability, Method, Work, evidence, or status claims.
- Episteme-use relations stay direct and do not become a parallel system-role ontology.
- Method and Work checks may cite the description without treating it as Work evidence.

**Costs.**

- Former “role-or-status template” material must move to F.10, A.2.4, B.3, A.10, E.17, G.6, or another direct relation.
- A stronger claim may require several neighboring patterns instead of one overloaded card.
- Public, Core-facing, or durable cross-local names require F.18.

### F.4:10 - SoTA-Echoing and Source Use

| Practice line | What FPF takes | Practical implication |
| --- | --- | --- |
| Foundational-ontology work distinguishes a locally constituted classification, its bearer, dependence, capability, function, and participation. | F.4 keeps one local kind and its description separate from the candidate system, classification judgment, assignment, capability, Method, and Work. | A readable description creates none of its neighboring world-side facts. |
| Terminology and interoperability practice distinguishes a referent, its description, designation, scheme, and any explicit relation to another local referent. | Use F.4 to name the local kind and its scheme-relative description, C.3.3 for an actual relation between exact local kinds, and F.9 only for an actual relation between distinct local-sense cells. | Same spelling does not identify the same kind across local practices or sources. |
| FPF episteme and publication ontology separates the described entity, description episteme, publication form, and carrier. | A `SystemRoleKindDescription` is an episteme about one exact local kind; a card or table may express it. | Editing or publishing the form does not change the kind or create an assignment. |
| FPF relation-declaration discipline distinguishes participant meaning, actual participants, declaration slots, and representations. | Bare *role* in those uses is recovered through E.10.ROLE and A.6.RSIR. | A relation position does not become a system-role kind. |

SysML is intentionally not used as an authority for this ontology. A modeling notation does not decide the identities of a local system-role kind, candidate system, assignment, participation, permission, or Work.

Currentness and reopen condition: reopen F.4 when A.2, C.3, A.2.1, A.2.5, A.2.7, A.15, A.6.5, A.6.RSIR, C.2.1, F.9, F.10, F.18, or the accepted episteme-use discipline changes enough that the described-kind or non-inference boundary would be stated differently.

### F.4:11 - Relations

**Builds on.** A.2, C.3, C.3.2, A.6.5, A.6.RSIR, A.7, C.2.1, E.10.ROLE, E.10.D2, and E.24.

**Coordinates with.** A.2.1, A.2.2, A.2.5, A.2.7, A.15, A.15.1, A.15.2, F.5, F.9, F.10, F.14, F.15, F.18, and direct evidence, status, source, publication, requirement, permission, responsibility, and assurance relations.

**Constrains.**

- F.5 names a `SystemRoleKindDescription` only after the described local kind, current criterion, effective scheme, and local sense are recovered.
- Use F.8 to decide durable name minting or reuse without turning status or episteme use into a system-role-kind description.
- F.14 keeps bundles and separation-of-duties relations separate from kind descriptions.
- Use F.15 to check the single-kind and non-inference boundaries.

### F.4:12 - Conformance Checklist

| Check | Question |
| --- | --- |
| `CC-F4-01` | Is the exact C.2.1 EntityOfConcern one local system-role kind? |
| `CC-F4-02` | Are the practice or source boundary in which the kind is constituted, its stable work-facing contribution distinction, current `KindSignature`, and effective scheme recoverable? |
| `CC-F4-02a` | Are the description episteme, local kind, `KindSignature`, effective scheme, optional F.17 cell and basis relation, and candidate-classification judgment kept separate, with optional values added only when the receiving use needs them? |
| `CC-F4-03` | Is the description separate from the kind, classification judgment, NameCard, public row, publication form, and carrier? |
| `CC-F4-04` | Does first entry preserve the full A.1 range of possible systems rather than imply only non-human technical systems? |
| `CC-F4-05` | Are classification and assignment handled separately under C.3.2 and A.2.1? |
| `CC-F4-06` | Are capability claims handled under A.2.2? |
| `CC-F4-07` | Are Method, plan, and Work claims handled under A.3, A.15, and their direct neighbors? |
| `CC-F4-08` | Are evidence, source, standard, requirement, publication, assurance, status, permission, and responsibility claims sent to exact direct relations? |
| `CC-F4-09` | Are bare-*role* participant, declaration, interface, and representation uses recovered through E.10.ROLE and A.6.RSIR? |
| `CC-F4-10` | Are durable public names handled through F.18 and actual cross-local relations handled through C.3.3 or F.9 according to their endpoints? |
| `CC-F4-11` | Are missing neighboring values left `unknown`, unresolved, not asserted, or not current rather than forced into the card? |

### F.4:13 - Phrasebook

Prefer:

- “description of `ReviewerSystemRole@JournalReview-2026`, one local system-role kind”;
- “candidate-system admission is established under A.1; classification and any assignment are separate”;
- “capability requirement cited by the description”;
- “Method requirement cited by the description”;
- “review report used as evidence for this claim”;
- “standard used as a requirement source”; and
- “relation position declared by this `SlotSpec`.”

Avoid as live Tech vocabulary:

- “evidence role” for an episteme;
- “status role” for a status or status-use relation;
- “standard role” for a standard used as a source;
- “holder” for a publication, report, standard, dataset, or theorem unless the exact entity is independently admitted as `U.System` and an exact `U.SystemRoleAssignment` names it as holder;
- “role” for a `SlotKind`; and
- “role description” for a Method, capability, Work record, access policy, or status-use relation.

### F.4:14 - Didactic Memory

A `SystemRoleKindDescription` is the readable episteme that tells people what one exact local system-role kind means. It helps a reader classify, assign, name, or compare the kind. It does not admit the kind or a candidate system, produce the classification judgment, create an assignment, prove capability, define a Method, perform Work, grant permission, establish responsibility, carry evidence, publish itself, or turn every useful episteme into a system-role holder.

### F.4:End

