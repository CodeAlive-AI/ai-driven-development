## F.18 - Local-First Unification Naming Protocol
> **Status:** Stable
*Pattern state: stable pattern. Audience: engineer-managers, lead architects, ontology editors, and authors who must make one name reusable without turning that name into a hidden ontology.*

### F.18:0 - Use This When

Use `F.18` when a name must become stable, public, Core-facing, reusable across contexts, or durable enough that later work can cite it without guessing. Typical cases:

- a local expression becomes a durable name for a role, relation, slot, method, work, characteristic, status value, architecture element, or other already governed value;
- two teams use different words for the same candidate sense and need one reusable term plus preserved local wording;
- one tempting head word is useful in one context but misleading in another;
- a role-derived, method-derived, status-like, evidence-like, interface-like, or slot-like name risks creating a second ontology by wording alone.

First useful move: recover the exact governed object or governed value before choosing the name. When relation-facing wording is current, distinguish a predicate-definition episteme, an admitted relation kind, an obtaining relation occurrence, a representation element, and a designator or reference; for a residual relation claim, cite the `A.6.RCD` settlement before naming. Other candidates—such as a role, method, work, characteristic, status value, architecture element, or claim-bearing episteme—stay under their direct owners rather than being forced into that relation-facing list. Then ask: under which effective by-value `U.ReferenceScheme`, by which governing pattern, for which use, and with which local sense is this exact object named? Only then decide whether a `NameCard` and, when public or cross-scheme use is current, a `UnifiedTermRow` are needed.

Do not use `F.18` for one-off wording repair. If the phrase is local and not becoming a reusable name, use `E.10`, `E.10.ARCH`, `A.6.P`, `A.6.RSIR`, `C.2.P`, or the governing pattern for the object being named.

### F.18:1 - Context

Names are handles for use, not creators of ontology. A good name lets people talk about a governed value without smuggling in extra role, capability, method, work, status, evidence, interface, or cross-context claims.

`FPFCoreReferenceScheme` is the by-value `U.ReferenceScheme` used to interpret current FPF Core Tech labels and relation names. A NameCard that uses it carries that reference-scheme value by value, consistent with `C.2.1`; F.18 does not introduce `U.ReferenceSchemeRef`. A name interpreted under another reference scheme carries that scheme by value. If its local sense also crosses `U.BoundedContext`, use `F.9` for the exact cross-context `SenseCell` bridge; a scheme change alone supplies neither that Bridge nor governed-value identity.

`F.18` supplies the naming discipline for Part F and for any FPF pattern that needs a durable public term. It coordinates with:

- `F.5` for type-name and role-description label form;
- `F.8` for mint-or-reuse decisions;
- `F.9` for cross-context bridges;
- `F.13` for renames, aliases, splits, and merges;
- `F.14` for anti-explosion control;
- `F.17` for public term-row publication;
- `A.6.5` and `A.6.RSIR` when relation, signature, interface, slot, or role wording hides the governed object; `A.6.P.WMR` when work/method-boundary wording still hides the exact relation; and `A.15.1` when a candidate performed-work name still lacks occurrence grounding.

The central EntityOfConcern is the naming relation around a governed value:

```text
NameCard:
  NameCardId
  GovernedValueRef
  GoverningPatternRef
  ReferenceScheme
  LocalSenseRef
  TechLabel
  PlainLabel
  CandidateSetRef
  SelectionRationale
  BridgeRefs?
  UnifiedTermRowRef?
  LineageEntries
```

The `NameCard` describes and governs the name. It does not create the governed value. A `UnifiedTermRow` publishes the selected name for public, Core-facing, durable, or cross-context use; it also does not create the governed value.

### F.18:2 - Problem

FPF texts fail when names are treated as if they carried ontology by themselves.

1. A short label appears in another context and gets treated as the same value, although no bridge says what survives.
2. A role-looking name quietly bundles role value, holder assignment, capability, method fit, work evidence, or authorization.
3. A status-like or evidence-like phrase becomes a fake role or fake type because the row says "evidence role", "status role", or similar wording.
4. A relation, declaration-local slot, interface, port, or signature name hides the exact governed object, relation-participant meaning, or direct pattern that should own the claim.
5. A term chosen for convenience becomes a permanent Core-facing name without candidate comparison, rejected alternatives, or lineage.
6. Local names proliferate until the corpus has several almost-synonyms and no recoverable reason for choosing one.

The repair is not to choose prettier words. The repair is to recover the governed value and then publish a name whose kind, effective reference scheme, local sense, and intended use are visible.

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

1. Recover the governed value and its direct governing pattern.
2. Decide whether the name is only local wording or a durable reusable name.
3. If durable, create or update a `NameCard`.
4. Choose the Tech label and Plain label from a visible candidate set.
5. Record why the selected pair is better for the declared use than rejected candidates.
6. Use `F.17` only when the name needs public, Core-facing, durable, or cross-context publication.
7. Keep bridge, status, evidence, slot, role, method, work, and interface claims in their own governing patterns.

#### F.18:4.1 - Naming Invariants

Every durable name must satisfy these invariants.

| Invariant | Required content |
| --- | --- |
| Governed value first | Name the governed value or value family before naming the label. |
| Governing pattern visible | Cite the pattern that owns the value: for example `A.2` for role value, `A.2.1` for role assignment, `A.6.5` for relation slot discipline, `F.10` or `A.19.SPR` for status value use, `A.10` for evidence use. |
| Reference scheme visible | The NameCard carries the effective `U.ReferenceScheme` by value; a model-use structure, claim scope, project work, or other locality relation remains separate and appears only when the naming use needs it. |
| Local sense visible | The name resolves to a local sense, Concept-Set row, or direct-pattern value. |
| Two labels when reusable | The Tech label is precise; the Plain label helps ordinary readers. Both point to the same governed value. |
| Candidate comparison visible | At least two plausible head families are considered unless a cited external standard fixes the label. |
| Bridge only for cross-context sense alignment | A spelling match, shared reference scheme, or `F.9` Bridge does not establish governed-value identity; F.9 states only its exact sense correspondence and admitted use. |
| Lineage visible | Rename, split, merge, retirement, and alias decisions are recorded. |

#### F.18:4.2 - `NameCard` Fields

Use this compact form when a durable name is live:

```text
NameCard:
  NameCardId:
  GovernedValueRef:
  GoverningPatternRef:
  ReferenceScheme:
  LocalSenseRef:
  TechLabel:
  PlainLabel:
  CandidateSet:
  RejectedCandidates:
  SelectionRationale:
  BridgeRefs:
  UnifiedTermRowRef:
  LineageEntries:
  RefreshCondition:
```

Field discipline:

- `GovernedValueRef` resolves to the exact already-governed object or value being named. For relation-facing wording it resolves to exactly one of the objects distinguished in section 5.6; a field label, record, card, table row, or local phrase is not a proxy for that object.
- `GoverningPatternRef` names the pattern that decides the value, not the pattern that merely publishes or teaches the name.
- `ReferenceScheme` carries the effective `U.ReferenceScheme` by value. It is not a reference field and does not introduce `U.ReferenceSchemeRef`.

- `CandidateSet` records the plausible labels considered, grouped by head-term family.
- `RejectedCandidates` records why tempting names were not selected.
- `UnifiedTermRowRef` is present only when `F.17` term-row publication is current.
- `RefreshCondition` says when the name must be reconsidered: reference-scheme edition change, bridge change, governing-pattern change, or repeated reader error.

Names such as "foundational principle pattern set", "FPF Core", "domain principle framework", and "local practice framework" require ordinary `NameCard` work before public stabilization under an effective reference scheme. Source aliases such as `ZPF`, `SPF`, `TPF`, or broad `xPF` labels remain intake aliases until `F.18` has settled the governed value, by-value reference scheme, local sense, rejected candidates, and admissible short form.

#### F.18:4.3 - Candidate Selection

Do not pick a durable label in one stroke. Build a small candidate set, normally five to ten candidates, from at least two head-term families. Judge candidates on:

- semantic fidelity: does the label preserve the governed value without adding or losing required conditions?
- reader ergonomics: can the intended reader say and remember it?
- morphology fit: does the word shape fit the kind being named, for example role value, method, work, description, relation, slot, characteristic, or status value?
- alias risk: will a careful reader import a wrong sense from nearby FPF patterns or external practice?

Use these as ordinal comparisons. Do not average them into one score. If a Pareto-front or quality-diversity method is used, the dimensions and dominance rule must be visible on the card.

One candidate can win even when it is not perfect, but the `SelectionRationale` must say what it buys and what risk remains.

#### F.18:4.4 - Public Term Rows

Use `F.17` when the name becomes public, Core-facing, durable across contexts, or cross-context. The term row carries the publication object:

- row id;
- governed object kind or governed value reference;
- direct governing pattern;
- Tech and Plain labels;
- sense cells;
- bridge references;
- edition and currentness condition.

The term row is not the governed value. A row for `ReviewerRole` publishes the role name; it does not create the role. A row for `EvidenceUseRelation` publishes a relation name; it does not make an episteme into a role. A row for `SlotKind` or `EndpointSlot` publishes slot vocabulary; it does not create a generic interface ontology.

### F.18:5 - Role, Assignment, Slot, and Status Naming Settlement

This settlement makes several naming boundaries explicit.

#### F.18:5.1 - Role Names

A durable role name names one governed `U.Role` value under an effective by-value `U.ReferenceScheme`. If one selected model-use structure, role-relation structure, claim scope, or project-work relation changes the naming use, cite that object separately; the name does not create it. Good role names normally use role morphology, for example `ReviewerRole`, `ShipbuilderRole`, or `ServiceProviderRole`.

A role name must not include:

- the holder that fills a role assignment;
- capability evidence or skill level;
- method or method-family selection;
- performed work;
- status value or gate result;
- source, evidence, publication, or assurance use.

If a phrase such as `SeniorReviewer`, `NightOperator`, or source wording like evidence role appears, recover the governed values first. The result may be a role value, a holder assignment, a status assertion, an evidence-use relation, a work admission condition, or a local source phrase. Do not force all of them into one role name.

#### F.18:5.2 - Holder Assignment Names

A holder assignment is governed by `A.2.1`, not by the role name itself. If the assignment needs a public name, name the assignment relation as such, for example:

```text
HolderAssignment:
  HolderRef:
  RoleRef:
  BoundedContextRef:
  AssignmentWindowRef:
```

`Holder#Role:Context@Window` may be used as a compact assignment notation where accepted by `A.2.1`. It is not a role name and not proof of capability.

#### F.18:5.3 - Capability, Method, and Work Names

Keep these separate:

- `ShipbuilderRole` names a role value;
- `ShipbuildingCapability` names a capability of a system or acting holon;
- `ShipbuildingMethod` names a method or method family;
- `HullAssemblyWork` names a work family or planning-level work label until an exact performed occurrence is current.

Role-derived or role-method-coupled method names are method names when the current governed value is a method, method family, method description, work plan, or work occurrence. They are governed by `A.3.1`, `A.3.2`, and `A.15`, with `F.18` only choosing the durable name. A role relation structure may constrain who may use or perform the method; it does not produce the method name.

Treat an action nominal such as `testing`, `assembly`, `maintenance`, `evaluation`, or `inspection` as a morphology cue, not a governed kind. Placement in function- or flow-structure prose identifies no `U.Function`. If the function-like use remains claim-bearing while its exact object or relation is hidden, apply `A.6.F`; if it is already recoverable, name the exact method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, performed-work occurrence, or other governed value under its direct pattern before F.18 selects a durable name. A WBS element, activity, or Work Package remains plan- or assignment-episteme content about intended work; none of these uses identifies a performed Work occurrence admitted under `U.Work`.

A durable name for exact performed work names one occurrence already grounded under `A.15.1`, not the action nominal or plan row. The current naming use must be able to recover the performer through an obtaining `U.RoleAssignment`, actual `enactsMethod`, temporal extent, exact containing system, affected referent, and the direct bindings and resource-use facts material to the occurrence. Add the exact continuity policy only when interruption, retry, changed method or bindings, or competing designators make occurrence identity material. Keep neighboring direct subject or resource-use claims, `A.15.PROD` production claims, measurement-result epistemes, evaluation results, `C.11` choices or decisions, delivery occurrences, acceptance verdicts, and downstream-effect claims separately named under their direct governors.

When the underlying boundary wording still hides the relation, apply `A.6.P.WMR`. `F.18` starts only after an exact governed value and its use are recovered through a direct subject relation, an exact `A.6.1` application binding, or an exact local `A.15.PROD`/`A.6.RCD` claim. An exact non-assertability result independently records `factually unsupported`, `missing-information`, or `missing-governor`; none authorizes durable naming, and only `missing-governor` is an ontology blocker that names the affected use and future owner. This section selects and tests a name. It does not define a second work-occurrence or work-result recovery algorithm.

Method-relation and method-composition names are method-side names too. If a phrase names serial composition, parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, fallback, or dispatch among methods, recover `MethodRelationStructure@BoundedContext` under `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern when current. Algebraic, graph, categorical, process-calculus, matrix, embedding, distributed, or neural notation names the lens or representation only when that lens is the governed value.

#### F.18:5.4 - Role-Relation, Method-Relation, Role-Method, and Lens Names

Role-relation expressions remain expressions or relations unless the direct role pattern admits a durable role value and the NameCard settles its by-value reference scheme and local sense. A role-algebra, graph, matrix, embedding, distributed, or neural description is a lens over the selected role relation structure; it is not automatically the named role, holder, method, or work.

First recover what the name is for:

| Expression or source phrase | What can be named | Naming rule |
| --- | --- | --- |
| `R1 <= R2` | role-requirement substitution relation between role values or local role expressions | Name a new role only when the direct role pattern admits that role value and its NameCard settles the reference scheme and local sense. Otherwise name the relation or cite it inside the governing method criterion, A.2.7 role-relation record, or work-admission check. |
| `R1 incompatibleWith R2` | incompatibility relation for exact assignments in one declared qualification window | Name the relation or constraint, not a new role. |
| `R1 and R2` | independent role values and assignments, when both remain current separately | Use "and" in ordinary prose; do not hide independent assignments by hyphenating them. |
| `R1 bundle R2` or `RoleBundle := R1 and R2` | role-bundle expression or durable bundle role value, if admitted | Keep it as an expression unless a direct role pattern admits a durable bundle value and its NameCard settles the reference scheme and local sense. |
| `R1` qualified by domain, practice, method family, or work field | local qualified role expression such as robotics-qualified engineering role | Ordinary labels may be `robotics engineer` or `engineer-roboticist`; `Role` suffix is optional Tech-register disambiguation. |
| method-like phrase derived from a role label | method, method family, method description, work plan, or work occurrence | Name under `A.3.1`, `A.3.2`, or `A.15`; cite the role relation separately when it constrains who may use or perform the method. |
| algebraic, graph, matrix, embedding, distributed, or neural representation of roles | mathematical or representation description of selected role relation structure | Name the lens only when the representation itself is the governed value; otherwise name the recovered role relation, role expression, method, or work. |
| method algebra, method graph, method matrix, process calculus, selector calculus, or method embedding | mathematical or representation description of selected `MethodRelationStructure@BoundedContext` | Name the lens only when the representation itself is the governed value; otherwise name the selected method relation structure, method family, method description, work plan, work occurrence, or neighboring relation. |
Ordinary speech can omit `Role` and `Method` suffixes when the current record, governed kind, reference scheme, and local sense keep the distinction recoverable. Formal suffixes are useful when the name becomes cross-scheme, public, or easy to confuse with a method, capability, work occurrence, status, publication, or policy term.

#### F.18:5.5 - Status, Evidence, Source, and Publication Names

Status-like and evidence-like wording must go to direct patterns:

- status value or status assertion: `F.10` or `A.19.SPR`;
- evidence-use relation: `A.10`;
- assurance use: `B.3`;
- source use: `E.10.D2` or source-use patterns;
- publication or description use: `E.17` and `C.2.1`;
- gate or admission result: the relevant gate, decision, or assurance pattern.

Do not name these as `U.Role` values unless a work-facing role value is actually current. "This standard plays the role of evidence" is repaired to the appropriate evidence-use, source-use, or status-use relation; it is not a work-role assignment for the standard.

#### F.18:5.6 - Relation, Slot, Interface, Port, and Signature Names

If a name touches relation, slot, interface, port, boundary, protocol, API, or signature wording, use `A.6.RSIR` and direct governing patterns.

- `A.6.5` governs relation slot discipline and SlotSpecs.
- `A.6.0` governs signatures and rule-governed declarations.
- `A.6.M` and architecture patterns govern module interfaces and architecture interfaces.
- `A.6.F`, transformation, and architecture patterns govern functional ports and functional structures.
- `A.6.C`, protocol, service-access, and commitment patterns govern API, protocol, and service-access cases.
- `E.17` governs publication or description interfaces.

Before naming a relation-facing object, keep these settlements distinct:

| Object to name | Required prior settlement |
| --- | --- |
| reusable predicate-definition episteme | `A.6.RCD` has selected reusable definition and `C.2.1` gives it one truthful exact `EntityOfConcern`; the name denotes the definition, not a relation kind |
| derived or primitive relation kind | `A.6.RCD`, `E.24`, and `E.24.UK` have admitted the kind and its direct subject pattern states obtaining, applicability, and occurrence identity |
| one obtaining relation occurrence | the direct owner establishes obtaining and `A.6.REL` applies the admitted kind's identity rule |
| formula, query, path, graph, diagram, or other representation element | `C.29` states what it represents and the relevant correspondence; its name does not name the represented relation by default |
| designator or reference | the exact designation or reference relation resolves to the already settled object under its reference scheme |

One token may be reused only where the reference scheme and local sense preserve these distinctions; it cannot collapse definition, kind, occurrence, representation, and designator into one object.

`F.18` can publish a durable name for the recovered value. It does not decide which value the interface word names.

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

A shipyard team wants one public name for "shipbuilder".

Recovered values:

- `ShipbuilderRole` in `ShipyardProductionContext`;
- holder assignment for a named worker or team under `A.2.1`;
- `ShipbuildingCapability` with envelope and measures under capability patterns;
- `ShipbuildingMethod` or method family under `A.3.1` and `A.3.2`;
- `HullAssemblyWork` under work patterns.

Here `HullAssemblyWork` is a work-family label or a label in a plan or assignment episteme. A designator such as `HullAssemblyWork-42@2026-07-15T09:10/11:35` names performed work only when the current record recovers its obtaining performer assignment, enacted method, temporal extent, containing system, affected hull referent, material bindings and resource-use facts, plus an applicable continuity policy when disambiguation is current. A changed hull state, measurement result, evaluation verdict, delivery occurrence, or acceptance verdict remains a separately governed and separately named value.

F.18 settlement:

```text
NameCard:
  GovernedValueRef: ShipbuilderRole@ShipyardProductionContext
  GoverningPatternRef: A.2
  ReferenceScheme: FPFCoreReferenceScheme

  TechLabel: ShipbuilderRole
  PlainLabel: shipbuilder role
  RejectedCandidates: ShipbuilderCapability; HullAssemblyWorker; CertifiedShipbuilder
  SelectionRationale: selected label names the role value without claiming capability, holder assignment, or performed work
```

The rejected candidates are not "worse synonyms." They name different governed values.

#### F.18:7.2 - Engineer-Roboticist and Musician

A lab says: "Vasya is an engineer, does robot engineering, is therefore an engineer-roboticist. These are musical robots, and Vasya is also a musician, performs music, and teaches robots music."

Recovered values:

- Vasya as holder in `MusicalRobotLab_2026`;
- engineering role value or local engineering-role expression;
- robotics as domain, practice, method-family, or work-field qualification of the engineering role expression;
- `MusicianRole` as an independent role value when music performance matters separately;
- robot-engineering method or work, music-performance work, and robot-music-teaching method or work under method and work patterns;
- optional role-algebra, graph, matrix, embedding, or neural representation only if the project actually uses such a lens to describe the role relation structure.

F.18 settlement:

```text
NameCard:
  GovernedValueRef: robotics-qualified engineering role expression in MusicalRobotLab_2026
  GoverningPatternRef: A.2.7 plus A.2 and F.4 when a durable role value is declared
  ReferenceScheme: FPFCoreReferenceScheme

  TechLabel: RoboticsEngineerRole only if durable Tech disambiguation is needed
  PlainLabel: engineer-roboticist or robotics engineer
  RejectedCandidates: engineer and roboticist; engineer-roboticist-musician; RobotEngineeringMethod
  SelectionRationale: selected ordinary label keeps robotics as a qualification of engineering, leaves musician as a separate role assignment, and does not turn method names or work names into role names
```

If the current sentence is for ordinary project communication, "Vasya is our engineer-roboticist and musician" is admissible. If the current record is a method record, name `RobotEngineeringMethod` or the relevant method family under `A.3.1`/`A.3.2`. If the current record is performed work, name the work occurrence under `A.15.1`. Do not make one compressed label carry all of these values.

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

F.18 settlement: no durable role name is minted. If a public term is needed, name the relation, for example `ModelCardEvidenceUse`, with `A.10` as governing pattern and `F.17` publication only when the term row is current.

#### F.18:7.4 - Interface-Like Source Phrase

A software team says "the payment interface owns customer identity".

Recovered candidates:

- module interface under `A.6.M`;
- API description or protocol under `A.6.C`;
- signature or SlotSpecs under `A.6.0` and `A.6.5`;
- publication or description interface under `E.17`;
- responsible role assignment under `A.2.1`.

F.18 settlement: do not mint `PaymentInterfaceRole`. First recover which governed value the phrase names. Then name that value through its governing pattern.

#### F.18:7.5 - Cross-Context Name

Two teams use `component`, `module`, and `unit` for nearby meanings.

Recovered values:

- structural component under architecture and part-whole patterns;
- deployable module under module-interface patterns;
- management unit under organizational patterns.

F.18 settlement: choose a Tech label only for the governed value under the declared by-value reference scheme and local sense. Use `F.9` only when cross-context `SenseCell` correspondence is current; a changed reference scheme by itself is handled in the NameCard and establishes no governed-value identity. Use `F.17` only if a public term row is needed.

### F.18:8 - Anti-Patterns And Repairs

| Anti-pattern | Ontological failure | Repair |
| --- | --- | --- |
| "Same spelling means same value." | Treats string identity or a sense bridge as governed-value identity. | Use `F.9` only to state exact cross-context sense correspondence and admitted use; apply the direct object owner for any identity claim, or keep the values separate. |
| "Evidence role" for a report, source, or standard. | Turns an episteme or source-use relation into a work-facing role. | Recover evidence-use, source-use, status-use, publication-use, or assurance-use relation. |
| "Night operator role" when only schedule differs. | Bakes temporal admission into role identity. | Keep role value; put time window in assignment, status, or work plan. |
| "Certified engineer role" when certification is evidence or admission. | Bakes capability evidence or admission into role name. | Keep `EngineerRole`; record capability evidence, admission, or status relation separately. |
| "Role-derived method" treated as a role-relation result. | Confuses role expression with method identity. | Name method or method family under `A.3.1` and `A.3.2`; cite role requirement separately. |
| "Method algebra" treated as the method or plan. | Confuses mathematical or representation lens with method relation structure, method description, work plan, or performed work. | Recover `MethodRelationStructure@BoundedContext`, method description, `C.29` lens use, work plan, or work occurrence by direct governing pattern before naming. |
| Action nominal, WBS element, or Work Package treated as performed work. | Function/method morphology or intended-work content is mistaken for one dated occurrence; a nearby result is folded into the work name. | Recover the exact `A.15.1` occurrence basis, apply `A.6.P.WMR` if the relation is still hidden, and name neighboring production claims, measurement results, evaluation results, delivery occurrences, and acceptance verdicts separately. |
| Role-looking interface wording for API, port, or boundary. | Uses role morphology to avoid recovering port, signature, boundary, or interface-specific relation. | Use `A.6.RSIR` and the direct governing pattern; name the recovered relation, signature, port, or bounded interface value only when that pattern admits it. |
| "Unscoped glossary." | Publishes words without governed value, by-value reference scheme, local sense, and bridge. | Use `NameCard`; use `F.17` term row when publication is current. |

### F.18:9 - Conformance Checks

Use these checks before a durable name enters a pattern or `UnifiedTermSheet`.

| Check | Passing condition |
| --- | --- |
| Governed value | The named value is recoverable and belongs to a direct governing pattern. |
| Interpretation | The effective `U.ReferenceScheme` is carried by value and the local sense is named; model-use structure, claim scope, project work, and other locality relations remain separate. |
| Kind | The kind is stated as governed value kind, not inferred from spelling. |
| Candidate set | Rejected plausible labels are visible with reasons. |
| Role boundary | Role, role assignment, holder, capability, method, work, evidence, and status claims are not collapsed. |
| Relation-object boundary | Predicate-definition episteme, admitted relation kind, obtaining occurrence, representation element, and designator are named only after their separate governing settlements; relation slot, interface, port, and signature names cite direct governing patterns. |
| Public row | `F.17` is used only for term-row publication; the row is not the value. |
| Bridge | `F.9` governs exact cross-context sense correspondence and admitted use, not governed-value identity; cross-scheme interpretation alone does not create an F.9 Bridge. |
| Lineage | Renames, aliases, splits, merges, and retirements are recorded under `F.13`. |
| Reader use | A practitioner can tell what to say, what not to infer, and where to go if the name is not enough. |
| Work-name boundary | An action nominal remains a morphology cue: a hidden claim-bearing function-like use goes through `A.6.F`, while an already recovered method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, or other value is named only under its direct pattern. A WBS/Work Package label remains plan- or assignment-episteme content, and a performed-work name is accepted only for one occurrence grounded under `A.15.1`; neighboring production claims, measurement results, evaluation results, decisions, delivery occurrences, and acceptance verdicts stay under their direct governors. |

Regression checks:

- When the effective reference-scheme edition changes, re-check local sense and bridge claims.
- When a role description changes, re-check role name and any holder-assignment name.
- When a method, capability, work, evidence, or status pattern changes, re-check any name that borrowed morphology from that area.
- When repeated reader errors occur, reopen candidate comparison instead of adding aliases indefinitely.

### F.18:10 - SoTA-Echoing

F.18 uses current terminology and naming practice as source material, but keeps the FPF ontology primary.

| Practice line | What F.18 takes | What F.18 rejects |
| --- | --- | --- |
| ISO 704:2022 terminology work and ISO 1087:2019 vocabulary discipline | concept-oriented term formation, definitions, designation discipline, and recordable term decisions | dictionary substitution as enough for FPF ontology |
| Knowledge-organization practice such as thesauri and SKOS | preferred label, alternative label, scope note, and relation discipline | treating a vocabulary entry as the governed object |
| Public naming, controlled-vocabulary, schema, or editioning practice | stable public names, compatibility expectations, and edition-aware change discipline | assuming software API practice is the general ontology of interface |
| Quality-diversity and multi-objective search | keeping several good candidate names visible until a selection reason is available | using optimization vocabulary as proof that a name is ontologically correct |
| Safety, assurance, and standards writing | making terms auditable where action depends on them | hiding admission, evidence, or responsibility inside the label |

### F.18:11 - Relations

Builds on `F.0.1`, `F.1`, `F.2`, `F.3`, `F.5`, `F.8`, `F.9`, `F.13`, `F.14`, `F.15`, and `F.17`.

Coordinates with:

- `A.2`, `A.2.1`, `A.2.5`, `A.2.7`, `A.15`, and `A.15.1` for role value, role assignment, role state, role relation structure, role-algebra lens use, role-method-work alignment, and exact performed-work occurrence grounding;
- `A.3.1` and `A.3.2` for method and method-family names;
- `A.6.P`, `A.6.P.WMR`, `A.6.RCD`, `A.6.REL`, `A.6.5`, `A.6.RSIR`, `A.6.0`, `A.6.M`, `A.6.F`, and `A.6.C` for relation-claim settlement, work/method-boundary relation recovery, relation-kind and occurrence boundaries, slot, signature, interface, port, and protocol names;
- `A.10`, `B.3`, `F.10`, `E.10.D2`, `E.17`, and `C.2.1` for evidence-use, assurance-use, status-use, source-use, publication-use, and description-use names;
- `C.16`, `C.18`, and Part G search patterns when candidate comparison uses Pareto or quality-diversity vocabulary.

Constrained non-use:

- `F.18` does not create `U.Role`, `U.RoleAssignment`, `U.Status`, `U.Method`, `U.Work`, `U.Episteme`, `U.Relation`, `U.Signature`, generic interface kinds or values, `U.SlotKind`, or any other governed value.
- `F.18` does not decide whether two values are the same across contexts; it requires the bridge or direct pattern that decides that claim.
- `F.18` does not turn a publication row, card, table, or glossary entry into the thing being named.

### F.18:End

