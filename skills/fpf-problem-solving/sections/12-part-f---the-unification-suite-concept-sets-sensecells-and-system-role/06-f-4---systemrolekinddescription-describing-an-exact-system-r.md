## F.4 - SystemRoleKindDescription — Describing an Exact System-Role Kind

> **Type:** Definitional (D)
> **Status:** Stable in the current FPF
> **Normativity:** Normative unless marked informative

### F.4:0 - Use This When

**Plain name.** Description of a system-role kind.

Use F.4 when a project needs a short, reusable description that makes one exact local system-role kind recognizable, teachable, and checkable. The described kind is a C.3 kind whose candidates must first be independently admitted as `U.System`. A candidate may be, for example, a person, team, organization, or non-human technical object; `SystemRole` does not mean “technical system only.”

Typical moments:

- a project has a durable kind name such as `ReviewerSystemRole`, `OperatorSystemRole`, `InspectorSystemRole`, `TransformerSystemRole`, or `ShipyardCoordinatorSystemRole`, but readers cannot recover which systems are candidates, what condition distinguishes members from relevant non-members, what change would make it another kind, the current `KindSignature`, or the work-facing boundary;
- a MethodDescription names a required system-role kind, but readers cannot tell which exact local kind must classify a candidate before an assignment can be checked;
- a kind name is starting to carry assignment, capability, Method, Work, permission, responsibility, evidence, publication, or status claims that belong elsewhere; or
- source prose says that a report, standard, dataset, theorem, dashboard, publication, or requirement has a “role”, and the writer must recover whether that wording denotes a system-role kind at all.

**Primary EntityOfConcern.** A `SystemRoleKindDescription` is one `U.Episteme` constituted under C.2.1. Its exact EntityOfConcern is one local system-role kind. Its ClaimGraph makes the C.3 recovery basis readable: the candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. It also names the current `KindSignature` edition, effective `U.ReferenceScheme`, useful source or practice provenance, and only the neighboring relations needed by the described use. Provenance helps readers locate and compare the definition; it does not identify the kind. The description is not the kind, a classification judgment, assignment occurrence, holder system, capability, MethodDescription, performed Work, status-use relation, or publication form.

**Primary working reader.** The first reader is an engineer-manager, analyst, Method author, or pattern author who must help people recognize the kind while keeping kind, candidate classification, assignment, capability, Method, Work, evidence use, status use, and publication use distinct.

**First useful move.** Name the exact local system-role kind, say in ordinary words which systems can count and what separates a member from a relevant non-member, cite the current `KindSignature`, and state the change that would make it another kind. Add source or practice provenance only to help readers find and compare the definition. Keep the recognition explanation no longer than the next classification, assignment, Method, Work, naming, or cross-local claim needs.

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

A local system-role kind often needs a recognizable description before people can classify a candidate, assign a system, compare kinds, or use the kind in a Method condition. A name such as `InspectorSystemRole` is not self-explanatory. Readers need to know which systems are candidates, what condition distinguishes intended members from relevant non-members, when that distinction continues, which `KindSignature` states it, and where neighboring claims begin. Source or practice provenance can help them locate and compare that definition; it cannot decide kind identity.

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
9. **Same-spelled kinds collapse or fragment.** Shared spelling is treated as proof of one kind, or a changed practice or source as proof of two, without comparing the candidate domains, operative membership conditions, member/non-member boundaries, and continuity rules.

### F.4:3 - Forces

| Force | Tension |
| --- | --- |
| Recognition versus ontology | A description must be easy to read but cannot replace the kind, classification judgment, assignment, capability, Method, or Work occurrence. |
| Kind continuity versus local reuse | The candidate domain, operative membership distinction, member/non-member boundary, and continuity rule decide whether one kind continues. A practice or source change only tells the reader where to compare definitions; a later use may still need a C.3.3 relation between distinct kinds or an F.9 relation between distinct F.17 local-sense cells. |
| Compactness versus completeness | A useful description is small, but a stronger receiving claim may need state, capability, Method, assignment, evidence, or status checks. |
| Open-world use versus form burden | Some uses need only a recognition paragraph; stronger uses need explicit neighboring references without pretending every possible relation is current. |
| Work-facing classification versus episteme use | An admitted system may satisfy a system-role kind and participate in an assignment. An episteme is instead used through evidence, source, publication, requirement, explanation, assurance, or status relations. |

### F.4:4 - Solution

Constitute one `SystemRoleKindDescription` through C.2.1. Its ClaimGraph describes one exact local system-role kind, and that kind is its EntityOfConcern. It makes the kind's candidate domain, operative membership condition, intended member/non-member boundary, continuity rule, current `KindSignature`, and effective `U.ReferenceScheme` recoverable. It may record source or practice provenance so readers can find and compare definitions, but provenance is not a kind-identity key. The description gives readers enough to recognize and check the kind while routing neighboring claims to their direct rules.

The following is a content checklist, not a relation signature or mandatory record.

**Always make recoverable:**

- the described local system-role kind;
- the candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule;
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

These are claims or references in an episteme. They are not `SlotSpec` declarations and add no participant to `U.SystemRoleAssignment` or another relation. A card, table row, Method appendix, or pattern section may express the description. When availability matters, a separate E.24.PUB occurrence makes the exact description edition available through its publication form and carrier.

#### F.4:4.1 - Content Meanings

| Content element | Meaning |
| --- | --- |
| Described system-role kind | The exact local `U.Kind` that is the episteme's EntityOfConcern. |
| Kind recovery basis | The candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule that distinguish this kind. Source or practice provenance may locate the definition but does not decide identity. |
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

1. Name the described local system-role kind and state its candidate domain, operative membership distinction, one useful member/non-member boundary, and continuity rule. Record source or practice provenance only when it helps the reader locate or compare the definition.
2. Name the current `KindSignature` edition and effective reference scheme.
3. Give one short recognition paragraph, including the broad A.1 system range when a cold reader could narrow it incorrectly.
4. State the smallest direct criteria or invariants that distinguish the kind.
5. State what the description does not assert about classification, assignment, capability, Method, Work, evidence, status, permission, responsibility, publication, or relation positions.
6. Add neighboring references only when the receiving use depends on them.
7. Use F.18 for a durable public name. Use C.3.3 only when an actual relation between exact local kinds is current; use F.9 only when the receiving claim relates distinct F.17 local-sense cells.

### F.4:5 - Invariants

1. **One described kind.** A `SystemRoleKindDescription` describes exactly one local system-role kind.
2. **Direct kind identity.** The candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule remain recoverable. A source, practice, taxonomy row, signature edition, or scheme helps locate, state, or interpret that basis; none decides identity by itself.
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

`PumpInspectorSystemRoleKindDescription` is a C.2.1 episteme whose EntityOfConcern is the kind currently named `PumpInspectorSystemRole`. The practical distinction is simple: an admitted system counts when it obtains readings for the named pump and declared condition characteristics in the applicable inspection situation and returns the named pre-maintenance judgment from those readings. A maintenance technician, inspection robot, or service team can be a member; a report, or a system missing either condition, is a relevant non-member. `PlantA-PumpInspector-KindSignature-v4` and `Plant-A-Maintenance-Scheme` state the current definition and interpretation. Plant A provenance locates that definition; it does not identify the kind. The same kind continues through an aligned edition while the candidate range and two-part distinction continue; a material change to either calls for another kind. Each predicate declaration supplies participant meanings and applicability, and the current case supplies the satisfying facts. Use `A.6.F` only if source wording first hides those claims behind *function*; it establishes neither predicate. If either predicate or its case facts cannot be recovered, record the exact A.6.RCD `missing-governor` or missing-information result instead of classifying the candidate.

The description says the kind concerns pump-condition inspection and does not itself denote repair. It may cite pump-inspection capability conditions or an inspection Method when a receiving Work claim needs them. Its boundary says that an inspection report is an episteme used through evaluation, evidence, source, or publication relations, not a system-role holder.

The description makes `PumpInspectorSystemRole` recognizable. It does not say that Robot-7 satisfies the kind, has an assignment, is capable of inspecting, has permission or readiness to inspect, enacted a Method, or performed Work. Those claims use C.3.2, A.2.1, A.2.2, A.2.8.PER, A.15, and the applicable evaluation or evidence relations.

#### F.4:7.2 - Reviewer System Role and Review Report

`ReviewerSystemRoleKindDescription` may describe the kind currently named `ReviewerSystemRole`. An admitted system counts when it compares the named pattern claims with each selected scale in the applicable review situation and returns the named reasoned judgment with the assessed values or defects. A person, team, or review service satisfying both conditions can be a member; a review report, or a system that merely comments without applying the scales, is a relevant non-member. `PatternReview-2026-Reviewer-KindSignature-v2` states the current condition. The PatternReview source locates that definition; it does not identify the kind. The same kind continues only while the candidate range and substantive-review distinction continue under aligned editions. `A.6.F` is used only to unpack still-ambiguous function wording and establishes neither claim. If a predicate is missing, record the A.6.RCD `missing-governor`; if case facts are missing, record the corresponding unresolved result. This condition can be checked without asserting that any review appointment or dated review Work already exists.

Alice's classification under that kind, any review appointment she holds, any dated review Work she performs, and any report used as evidence remain four separate claims. This compact description names none of their occurrence identities.

Use:

- A.2 with C.3 for the local kind and direct classification;
- F.4 for the description episteme;
- A.2.1 when a particular review assignment must be identified;
- A.13 followed by independent A.15.1 admission when a particular dated review Work occurrence is identified, and F.6 afterward when the claim also identifies the assignment under which that Work was performed; and
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
| Bridge by label | Shared spelling, or a changed practice or source, is treated as proof of kind sameness or difference. | Compare the exact C.3 definitions first. Reuse one kind when its candidate domain and operative distinction continue; identify two only when those distinctions differ. Use C.3.3 only when an actual relation between two exact kinds obtains. Use F.9 only for an actual relation between distinct F.17 local-sense cells. |

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

### F.4:10 - SoTA Decision for a Readable Kind Description

Source use was checked on 2026-08-20. The bounded question is: **how can one work-facing kind be described for recognition without confusing the kind with its bearer, a classification judgment, assignment, capability, Method, Work, designation, or publication?** The comparison assumes the effort of authoring one project pattern, not adopting a whole upper ontology.

| Current line | Strong contribution | Limit at comparable pattern-authoring effort | FPF decision and receiving locus |
| --- | --- | --- | --- |
| Almeida, Guizzardi, Sales, and Fonseca, [*gUFO: A Gentle Foundational Ontology for Semantic Web Knowledge Graphs*](https://arxiv.org/abs/2603.20948), 2026 preprint | It distinguishes kinds of types, things, qualities, relations, and situations; this helps expose confusion among classification, the thing classified, a dependent feature, and participation. | Importing the full typology first adds a foundational-ontology mapping and can choose a source category before the FPF receiving use, local kind, and direct relations are known. | **Adapt** the warning against collapsing classification, bearer, function-like aspects, and participation in sections 4.2, 5, and 8. **Reject** automatic import of gUFO categories or labels as the F.4 kind or description. |
| Current [BFO 2020 artifacts](https://github.com/BFO-ontology/BFO-2020), maintained for the ISO/IEC 21838-2 line | Separates enduring things from processes and distinguishes dependence, roles, and dispositions. | A whole upper-ontology commitment is expensive for a short recognition description and still does not decide the identity of the local FPF kind, its assignment occurrence, Method, Work, or publication package. | **Adopt** the warnings that dependence is not parthood and that role/disposition/process readings must not be fused. **Reject** BFO classification or standard status as the local kind-identity or description gate. This constrains sections 4.2, 7, and 8. |
| [ISO 704:2022](https://www.iso.org/standard/79077.html) together with W3C OntoLex-Lemon's [lexical entry, sense, and reference model](https://www.w3.org/2016/04/ontolex/) | ISO separates object, concept, definition, and designation; OntoLex separates lexical form and sense from the ontology referent. | Neither line establishes an FPF system-role kind, classifies a candidate, makes an assignment obtain, proves capability or Work, or makes a description edition available. | **Adopt** description/designation/referent separation in sections 4.1 and 4.2. **Reject** a definition, label, lexical sense, or row as a fact about the described work. F.4 adds the direct neighboring exits and publication boundary in sections 4, 7, and checklist 12. |

**Selected non-dominated contribution.** gUFO and BFO offer richer foundational categorization, but at higher mapping effort and without deciding the project-local recognition use. ISO 704 and OntoLex keep description and designation separate at lower effort, but leave assignment, capability, Method, Work, and publication outside their answer. F.4 takes the smallest useful middle path: one C.2.1 episteme about one already recovered C.3 kind, a short ordinary-language recognition distinction, and explicit exits for stronger neighboring claims. At the effort of one pattern description, it preserves the needed ontology while remaining usable by a cold project reader.

SysML is intentionally not a SoTA comparator, lineage source, or ontology authority for this question. Its modeling notation does not supply the kind-identity, classification, assignment, description, or Work rules being compared; search visibility or standard status does not make it a content rival.

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
| `CC-F4-02` | Are the candidate domain, operative membership condition, intended member/non-member boundary, continuity rule, current `KindSignature`, and effective scheme recoverable, with source or practice provenance used only to locate or compare definitions? |
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

- “description of the local kind currently named `ReviewerSystemRole`; JournalReview-2026 locates the definition”;
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

