## F.18 - Local-First Unification Naming Protocol
> **Status:** Stable
*Pattern state: stable pattern. Audience: engineer-managers, lead architects, ontology editors, and authors who must make one name reusable without turning that name into a hidden ontology.*

### F.18:0 - Use This When

Use `F.18` when a name must become stable, public, Core-facing, reusable across contexts, or durable enough that later work can cite it without guessing. Typical cases:

- a local expression becomes a durable name for a role, relation, slot, method, work, characteristic, status value, architecture element, or other already governed value;
- two teams use different words for the same candidate sense and need one reusable term plus preserved local wording;
- one tempting head word is useful in one context but misleading in another;
- a role-derived, method-derived, status-like, evidence-like, interface-like, or slot-like name risks creating a second ontology by wording alone.

First useful move: recover the governed object or governed value before choosing the name. Ask: what already-governed value is being named, in which bounded context, by which governing pattern, for which use, and with which local sense? Only then decide whether a `NameCard` and, when public or cross-context use is current, a `UnifiedTermRow` are needed.

Do not use `F.18` for one-off wording repair. If the phrase is local and not becoming a reusable name, use `E.10`, `E.10.ARCH`, `A.6.P`, `A.6.RSIR`, `C.2.P`, or the governing pattern for the object being named.

### F.18:1 - Context

Names are handles for use, not creators of ontology. A good name lets people talk about a governed value without smuggling in extra role, capability, method, work, status, evidence, interface, or cross-context claims.

`F.18` supplies the naming discipline for Part F and for any FPF pattern that needs a durable public term. It coordinates with:

- `F.5` for type-name and role-description label form;
- `F.8` for mint-or-reuse decisions;
- `F.9` for cross-context bridges;
- `F.13` for renames, aliases, splits, and merges;
- `F.14` for anti-explosion control;
- `F.17` for public term-row publication;
- `A.6.5` and `A.6.RSIR` when relation, signature, interface, slot, or role wording hides the governed object.

The central EntityOfConcern is the naming relation around a governed value:

```text
NameCard:
  NameCardId
  GovernedValueRef
  GoverningPatternRef
  BoundedContextRef
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
4. A relation, slot, interface, port, or signature name hides the relation position or governed pattern that should own the claim.
5. A term chosen for convenience becomes a permanent Core-facing name without candidate comparison, rejected alternatives, or lineage.
6. Local names proliferate until the corpus has several almost-synonyms and no recoverable reason for choosing one.

The repair is not to choose prettier words. The repair is to recover the governed value and then publish a name whose scope, kind, context, and use are visible.

### F.18:3 - Forces

| Force | Naming tension |
| --- | --- |
| Local sense and cross-context reuse | A name must be usable in one bounded context while remaining bridgeable elsewhere without spelling-based identity. |
| Brevity and ontology recovery | A short label helps conversation, but the `NameCard` must keep kind, context, governing pattern, and sense recoverable. |
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
| Bounded context visible | The name lives in one bounded context or in a declared cross-context publication row. |
| Local sense visible | The name resolves to a local sense, Concept-Set row, or direct-pattern value. |
| Two labels when reusable | The Tech label is precise; the Plain label helps ordinary readers. Both point to the same governed value. |
| Candidate comparison visible | At least two plausible head families are considered unless a cited external standard fixes the label. |
| Bridge only for cross-context sameness | A spelling match does not establish sameness. |
| Lineage visible | Rename, split, merge, retirement, and alias decisions are recorded. |

#### F.18:4.2 - `NameCard` Fields

Use this compact form when a durable name is live:

```text
NameCard:
  NameCardId:
  GovernedValueRef:
  GoverningPatternRef:
  BoundedContextRef:
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

- `GovernedValueRef` names the value, relation, slot, claim record, or local concept being named. It is not a row id by default.
- `GoverningPatternRef` names the pattern that decides the value, not the pattern that merely publishes or teaches the name.
- `CandidateSet` records the plausible labels considered, grouped by head-term family.
- `RejectedCandidates` records why tempting names were not selected.
- `UnifiedTermRowRef` is present only when `F.17` term-row publication is current.
- `RefreshCondition` says when the name must be reconsidered: context edition change, bridge change, governing-pattern change, or repeated reader error.

Names such as "foundational principle pattern set", "FPF Core", "domain principle framework", and "local practice framework" require ordinary `NameCard` work before public stabilization in a concrete context. Source aliases such as `ZPF`, `SPF`, `TPF`, or broad `xPF` labels remain intake aliases until `F.18` has settled the governed value, bounded context, rejected candidates, and admissible short form.

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

A durable role name names a `U.Role` value in a bounded context. Good role names normally use role morphology, for example `ReviewerRole`, `ShipbuilderRole`, or `ServiceProviderRole`.

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
- `HullAssemblyWork` names work or a work family.

Role-derived or role-method-coupled method names are method names when the current governed value is a method, method family, method description, work plan, or work occurrence. They are governed by `A.3.1`, `A.3.2`, and `A.15`, with `F.18` only choosing the durable name. A role relation structure may constrain who may use or perform the method; it does not produce the method name.

Method-relation and method-composition names are method-side names too. If a phrase names serial composition, parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, fallback, or dispatch among methods, recover `MethodRelationStructure@BoundedContext` under `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern when current. Algebraic, graph, categorical, process-calculus, matrix, embedding, distributed, or neural notation names the lens or representation only when that lens is the governed value.

#### F.18:5.4 - Role-Relation, Method-Relation, Role-Method, and Lens Names

Role-relation expressions remain expressions or relations unless the bounded context creates a durable role value through `A.2`, `A.2.7`, role description, and `F.18` naming. A role-algebra, graph, matrix, embedding, distributed, or neural description is a lens over the selected role relation structure; it is not automatically the named role, holder, method, or work.

First recover what the name is for:

| Expression or source phrase | What can be named | Naming rule |
| --- | --- | --- |
| `R1 <= R2` | role-requirement substitution relation between role values or local role expressions | Name a new role only when the bounded context introduces that role value. Otherwise name the relation or cite it inside the governing method requirement, A.2.7 role-relation record, or work-admission check. |
| `R1 incompatibleWith R2` | incompatibility relation for assignments in one bounded context and window | Name the relation or constraint, not a new role. |
| `R1 and R2` | independent role values and assignments, when both remain current separately | Use "and" in ordinary prose; do not hide independent assignments by hyphenating them. |
| `R1 bundle R2` or `RoleBundle := R1 and R2` | role-bundle expression or durable bundle role value, if declared | Keep it as an expression unless a role description and context make a durable role value. |
| `R1` qualified by domain, practice, method family, or work field | local qualified role expression such as robotics-qualified engineering role | Ordinary labels may be `robotics engineer` or `engineer-roboticist`; `Role` suffix is optional Tech-register disambiguation. |
| method-like phrase derived from a role label | method, method family, method description, work plan, or work occurrence | Name under `A.3.1`, `A.3.2`, or `A.15`; cite the role relation separately when it constrains who may use or perform the method. |
| algebraic, graph, matrix, embedding, distributed, or neural representation of roles | mathematical or representation description of selected role relation structure | Name the lens only when the representation itself is the governed value; otherwise name the recovered role relation, role expression, method, or work. |
| method algebra, method graph, method matrix, process calculus, selector calculus, or method embedding | mathematical or representation description of selected `MethodRelationStructure@BoundedContext` | Name the lens only when the representation itself is the governed value; otherwise name the selected method relation structure, method family, method description, work plan, work occurrence, or neighboring relation. |
Ordinary speech can omit `Role` and `Method` suffixes when the current record or context makes the kind recoverable. Formal suffixes are useful when the name becomes cross-context, public, or easy to confuse with a method, capability, work occurrence, status, publication, or policy term.

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

F.18 settlement:

```text
NameCard:
  GovernedValueRef: ShipbuilderRole@ShipyardProductionContext
  GoverningPatternRef: A.2
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

F.18 settlement: choose a Tech label only for the governed value in its bounded context. Use `F.9` bridges for cross-context comparison. Use `F.17` only if a public term row is needed.

### F.18:8 - Anti-Patterns And Repairs

| Anti-pattern | Ontological failure | Repair |
| --- | --- | --- |
| "Same spelling means same value." | Treats string identity as value identity. | Use `F.9` bridge with loss notes or keep separate rows. |
| "Evidence role" for a report, source, or standard. | Turns an episteme or source-use relation into a work-facing role. | Recover evidence-use, source-use, status-use, publication-use, or assurance-use relation. |
| "Night operator role" when only schedule differs. | Bakes temporal admission into role identity. | Keep role value; put time window in assignment, status, or work plan. |
| "Certified engineer role" when certification is evidence or admission. | Bakes capability evidence or admission into role name. | Keep `EngineerRole`; record capability evidence, admission, or status relation separately. |
| "Role-derived method" treated as a role-relation result. | Confuses role expression with method identity. | Name method or method family under `A.3.1` and `A.3.2`; cite role requirement separately. |
| "Method algebra" treated as the method or plan. | Confuses mathematical or representation lens with method relation structure, method description, work plan, or performed work. | Recover `MethodRelationStructure@BoundedContext`, method description, `C.29` lens use, work plan, or work occurrence by direct governing pattern before naming. |
| Role-looking interface wording for API, port, or boundary. | Uses role morphology to avoid recovering port, signature, boundary, or interface-specific relation. | Use `A.6.RSIR` and the direct governing pattern; name the recovered relation, signature, port, or bounded interface value only when that pattern admits it. |
| "Contextless glossary." | Publishes words without governed value, context, and bridge. | Use `NameCard`; use `F.17` term row when publication is current. |

### F.18:9 - Conformance Checks

Use these checks before a durable name enters a pattern or `UnifiedTermSheet`.

| Check | Passing condition |
| --- | --- |
| Governed value | The named value is recoverable and belongs to a direct governing pattern. |
| Context | The bounded context and local sense are named. |
| Kind | The kind is stated as governed value kind, not inferred from spelling. |
| Candidate set | Rejected plausible labels are visible with reasons. |
| Role boundary | Role, role assignment, holder, capability, method, work, evidence, and status claims are not collapsed. |
| Slot boundary | Relation slot, interface, port, signature, and relation names cite direct governing patterns. |
| Public row | `F.17` is used only for term-row publication; the row is not the value. |
| Bridge | Cross-context sameness uses `F.9`, not spelling. |
| Lineage | Renames, aliases, splits, merges, and retirements are recorded under `F.13`. |
| Reader use | A practitioner can tell what to say, what not to infer, and where to go if the name is not enough. |

Regression checks:

- When a context edition changes, re-check local sense and bridge claims.
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

- `A.2`, `A.2.1`, `A.2.5`, `A.2.7`, and `A.15` for role value, role assignment, role state, role relation structure, role-algebra lens use, and work-role alignment;
- `A.3.1` and `A.3.2` for method and method-family names;
- `A.6.5`, `A.6.RSIR`, `A.6.0`, `A.6.M`, `A.6.F`, and `A.6.C` for relation, slot, signature, interface, port, and protocol names;
- `A.10`, `B.3`, `F.10`, `E.10.D2`, `E.17`, and `C.2.1` for evidence-use, assurance-use, status-use, source-use, publication-use, and description-use names;
- `C.16`, `C.18`, and Part G search patterns when candidate comparison uses Pareto or quality-diversity vocabulary.

Constrained non-use:

- `F.18` does not create `U.Role`, `U.RoleAssignment`, `U.Status`, `U.Method`, `U.Work`, `U.Episteme`, `U.Relation`, `U.Signature`, generic interface kinds or values, `U.SlotKind`, or any other governed value.
- `F.18` does not decide whether two values are the same across contexts; it requires the bridge or direct pattern that decides that claim.
- `F.18` does not turn a publication row, card, table, or glossary entry into the thing being named.

### F.18:End

