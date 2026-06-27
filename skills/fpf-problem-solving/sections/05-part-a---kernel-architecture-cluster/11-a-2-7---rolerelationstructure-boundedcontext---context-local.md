## A.2.7 - RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary
> **Status:** Stable
> **Type:** Ontic relation-structure pattern


### A.2.7:0.1 - Kind Settlement

**Use this pattern when** a project needs context-local role substitution, incompatibility, factor, qualification, or bundle relations without turning labels or role-algebra notation into a second ontology.

**What goes wrong if missed.** Role labels start carrying type, capability, method, work, evidence, or permission claims, and a representation lens starts replacing the role relation structure in life.

**What this buys.** Role-relation claims stay small, local, and inspectable while role assignment, capability, method, work, evidence, source, status, publication, and lens claims keep their own governing patterns.

A.2.7 does not admit `U.RoleAlgebra` as a durable U-kind. The governed object is `RoleRelationStructure@BoundedContext`: a selected context-local relation structure over role descriptions, `U.Role` values, role expressions, substitution, incompatibility, and bundle-expression relations. A role algebra, graph, matrix, embedding, distributed model, or neural representation is a mathematical or representation lens over that structure, not the structure itself and not an operation on holder systems.

`RoleRelationStructure@BoundedContext` is the FPF object for context-local relations among role descriptions, declared role values, local role expressions, role-bundle expressions, and role-assignment-admission uses. It is not a new `U.*` kind beside `U.Role`; it is a selected relation structure over role-side values inside one bounded context. When project prose calls this "role architecture", the FPF object is still the selected role-relation structure in life; a role-algebra, graph, matrix, embedding, distributed, or neural description is a lens over that structure, not the structure itself and not an operation on holder systems. Coupled method relations are governed symmetrically as `MethodRelationStructure@BoundedContext` under `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern when current; A.2.7 names the role-relation side and the bridge to role-method naming.

Use this pattern when a method, work-admission rule, staffing rule, safety case, governance rule, or role description needs to say that one role value can satisfy another role requirement, two roles cannot be held together by the same holder during the same window, a role expression has a factor or domain qualification, or a frequent conjunction of roles is worth naming.

**Primary EntityOfConcern.** The EntityOfConcern is `RoleRelationStructure@BoundedContext`: a context-local role-relation and role-expression structure in one `U.BoundedContext`. Algebraic notation, matrices, partial orders, products, graphs, embeddings, neural representations, or other mathematical or representation expressions are descriptions or lenses of that structure. The role architecture in life is the selected relation structure among role values and role expressions; the lens is not the holder, not the performed work, not the living system, not the method, and not the role assignment.

**Primary working reader.** A manager, architect, method author, safety assessor, or model author who needs role-requirement substitution, separation-of-duties, role-factor or qualification expression, role-bundle expression, or ordinary name guidance without turning the role relation structure into capability, method, holder, work, evidence, status, or kind hierarchy.

**First useful move.** Name the bounded context, the role descriptions or role values being related, the local role expression or relation being claimed, and the assignment, method, work-admission, naming, or bridge check that will use that relation. Use a role-algebra lens only when mathematical notation helps state or check that relation.

**What goes wrong if missed.** Role names start acting like type hierarchy, org-chart hierarchy, permission policy, capability model, method family, staffing plan, or cross-context translation. Then FPF grows a second ontology beside `U.Role`, `U.RoleAssignment`, `U.Capability`, and method or work patterns, or treats algebraic notation as if it were the object in life.

**What this buys.** Context-local role relation structure gives a small, replayable set of role relations for role assignment, method-step checks, naming, and bridge work while keeping ability, work, method, evidence, and status claims in their governing patterns. Role-algebra notation remains a lens for describing those relations, not a substitute ontology.

**Not this pattern when.**


- If the current claim is who holds a role, use `A.2.1`.
- If the current claim is whether an assignment is currently in a work-admitting state, use `A.2.5`.
- If the current claim is ability, use `A.2.2`.
- If the current claim is a method, method family, or method description, use `A.3.1` or `A.3.2`.
- If the current claim is performed work or planned work, use `A.15`, `A.15.1`, or `A.15.2`.
- If the current claim is cross-context naming or translation, use F-family context and naming patterns such as `F.9` and `F.18`.
- If the current claim is evidence, source, status, assurance, publication, or description use, use `C.2.1`, `A.10`, `B.3`, `E.17.*`, `E.24.PUB`, or `A.7` as the direct governing pattern for that episteme-use claim.

### A.2.7:1 - Problem frame

**Use this when** a method, work-admission rule, staffing rule, safety case, governance rule, or role description needs a declared context-local relation among role values, role expressions, or role-bundle expressions.

**What goes wrong if missed.** Role labels act as type hierarchy, org chart, permission, capability, method family, staffing plan, or cross-context equivalence; mathematical notation then starts replacing the role relation structure in life.

**What this buys.** Role-requirement substitution, incompatibility, role factors, and role bundles become inspectable local relations while role assignment, capability, method, work, evidence, source, status, and publication claims stay with their governing patterns.

Work governed by role values and role assignments often needs three small claims:

1. One role value can satisfy another role requirement in the same context when a role-requirement substitution relation is declared.
2. Two roles are incompatible for the same holder during overlapping windows.
3. A recurring conjunction of roles can be named as a role bundle expression.

Without a local role relation structure, teams usually encode those claims in the wrong objects:

- a role assignment says "senior inspector" and silently satisfies "inspector" without declared relation;
- a separation-of-duties rule is written as a deontic slogan rather than an incompatibility relation over assignments;
- a role bundle becomes a new holder, capability, work product, or method;
- a cross-context label match is treated as role equivalence;
- method requirements smuggle capability or work claims into role names.

A.2.7 keeps the role relation structure small and local. It says how role values, role descriptions, and role expressions relate; it does not say who holds them, whether holders are able, whether work happened, or whether an episteme proves something. Algebraic, graph, factor, embedding, distributed, neural, or other mathematical descriptions are optional lenses over that structure.

### A.2.7:1.0 - Problem

A combined role expression such as engineer-roboticist, inspector-auditor, or musician-teacher can hide several different claims: a local role-requirement substitution, a role bundle, an incompatibility, a holder assignment, a capability claim, or a method/work coupling. The problem is to recover the local role relation structure without minting a new universal role kind or treating an algebraic, graph, factor, embedding, or neural description as the role structure itself.

### A.2.7:1.1 - Forces

| Force | Tension |
|---|---|
| Local relation vs universal type | A role-requirement substitution is valid inside one bounded context; it must not become kind subsumption or a universal role taxonomy. |
| Life structure vs representation lens | Algebra, graph, matrix, embedding, or neural representation may describe the selected role relation structure; the lens is not the holder, role assignment, capability, method, or work. |
| Compact naming vs hidden bundle | Ordinary names such as engineer-roboticist can help when the context declares the relation or bundle; they hide work when they silently combine independent roles or methods. |
| Role-method coupling vs collapse | Role and method relation structures often appear together, but method, method family, work plan, and performed work keep their direct governing patterns. |

### A.2.7:2 - Solution - Core Role-Relation Structure

`RoleRelationStructure@BoundedContext` is a relation structure declared inside one `U.BoundedContext`. A role-algebra description may be attached when notation helps inspection, but the structure remains the governed object.

```text
RoleRelationStructure:
  BoundedContextRef:
  RoleDescriptionRefs?:
  RoleValueSet:
  RoleExpressionSet?:
  RoleRequirementSubstitutionSet:
  IncompatibilityRelationSet:
  FactorOrQualificationExpressionSet?:
  BundleExpressionSet:
  MathematicalOrRepresentationDescriptionRefs?:
  UseRelationRefs:
```

**BoundedContextRef.** The role relation structure is local. A relation declared in `HospitalOR_2026` does not automatically apply in `PlantMaintenance_2026` or another hospital's governance context.

**RoleDescriptionRefs.** Role descriptions may supply the recognized meaning of role values or role expressions. They are description epistemes, not the holder, not the assignment, and not the algebraic lens.

**RoleValueSet.** The structure ranges over `U.Role` values governed by `A.2`.

**RoleExpressionSet.** The structure may include context-local role expressions such as qualified roles, bundle expressions, or labels that ordinary prose uses before a durable role value is declared.

**RoleRequirementSubstitutionSet.** The context may declare `AcceptedRoleForRequirement <= RequiredRole` as a role-requirement substitution relation. This is a local admissibility relation for method, work-admission, staffing, safety, or governance checks. It is not kind subsumption, org-chart rank, capability evidence, source-label equivalence, or public naming.

**IncompatibilityRelationSet.** The context may declare `RoleA incompatibleWith RoleB`. This means the same holder cannot use overlapping role assignments for both roles in the same bounded context and window when that incompatibility is current for the work claim.

**FactorOrQualificationExpressionSet.** The context may declare that one ordinary label is a qualified role expression, such as engineer qualified by robotics domain, method family, practice, or work field. This does not automatically create a separate `RoboticistRole` or a combined role value.

**BundleExpressionSet.** The context may declare `RoleBundle := Role1 and Role2 and Role3` as a role-bundle expression. The expression is satisfied only by valid assignments to each component role under the same bounded context and required window. It does not create a composite holder, composite capability, or method.

**MathematicalOrRepresentationDescriptionRefs.** A mathematical or representation description may use order, product, factorization, graph, matrix, embedding, neural representation, distributed model, or another lens to express the selected role relation structure. This description is governed like any lens use: it names what it represents, what it preserves, what it loses, and what it must not be overread to prove.

**UseRelationRefs.** A method step, work-admission check, staffing rule, safety case, naming decision, or governance rule may cite the role relation it uses.

### A.2.7:3 - Role-Relation Expressions

#### A.2.7:3.1 - Role-Requirement Substitution

Use role-requirement substitution when one role value can satisfy another required role in the same bounded context.

```text
SeniorWeldingInspector <= WeldingInspector
```

Read this as: an assignment to `SeniorWeldingInspector` may satisfy a method or work-admission requirement for `WeldingInspector` when the bounded context declares that substitution and the assignment window is current.

The relation is not kind subsumption. `SeniorWeldingInspector` is not a subtype of a system kind; it is a role value related to another role value for local requirement satisfaction. It is also not capability evidence, public naming, or method identity. A senior inspector role may still require a separate capability claim under `A.2.2`, a method relation under `A.3.1`/`A.3.2`, or a naming settlement under `F.5`/`F.18`.

#### A.2.7:3.2 - Role Incompatibility

Use role incompatibility when the same holder cannot validly use overlapping assignments to two roles in the same context and window.

```text
SurgeryPerformer incompatibleWith SurgeryVerifier
```

This relation is often used for separation-of-duties or independence constraints. It does not create a commitment object, permission policy, or evidence record by itself. A work-admission check may use it to reject the proposed assignment combination.

#### A.2.7:3.3 - Role Bundle Expression

Use a role bundle expression when a frequent conjunction of roles is useful to name inside one context.

```text
IncidentLeadOnCall := IncidentCommander and Communicator and DecisionMaker
```

The bundle expression is satisfied by current assignments to all component roles under the same bounded context and required window. It is not a product of role values, not a new holder, not a method, and not a capability.

A bundle expression becomes a durable role value only when the bounded context declares it as a role with its own role description, role-state expectations, capability requirements, and method or work relations where current.

### A.2.7:4 - How Role Relation Structure Is Used

Role relation structure is normally used by neighboring patterns as one selected structure, sometimes informally called the local role architecture:

```text
MethodStepRequirement:
  requiredRole: WeldingInspector
  acceptedAssignmentRole: SeniorWeldingInspector
  substitutionRef: SeniorWeldingInspector <= WeldingInspector
```

```text
WorkAdmissionCheck:
  holderRef: SurgeonA
  proposedAssignments: SurgeryPerformer, SurgeryVerifier
  incompatibilityRef: SurgeryPerformer incompatibleWith SurgeryVerifier
  window: AssignmentWindow
```

The role relation structure supplies one relation used by the check. The method, method family, method relation structure, work plan, performed work, capability envelope, and evidence use remain governed by their direct patterns. When a method relation or method composition structure also needs to be named, the current object is `MethodRelationStructure@BoundedContext` under `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern when current; method-algebra notation is a lens over that structure, not a hidden product of roles.

#### A.2.7:4.1 - Naming role-relation and role-method expressions

Role relation work may leave behind something people need to name in ordinary project prose. The named object is not always an atomic `U.Role` value. It may be a holder-in-role statement, a context-local role expression, a role-requirement substitution relation, an incompatibility relation, a role-bundle expression, a durable combined role value, a coupled role-method expression, a method name, or a work name.

Recover the named object before choosing the label:

| Source wording | Recovered object | Ordinary wording consequence |
| --- | --- | --- |
| "Vasya is an engineer" | holder-in-role claim: Vasya has a current assignment to an engineering role value in the bounded context | ordinary prose may say "engineer" without `Role`; the FPF record still separates holder, role value, assignment, and window |
| "robotics engineer" or "engineer-roboticist" | engineering role value or local engineering-role expression qualified by robotics domain, robotics-engineering method family, practice, or governed work field | ordinary label may stay "robotics engineer" or "engineer-roboticist"; `RoboticsEngineerRole` is optional Tech-register spelling only when durable reference needs it |
| "engineer and roboticist" | two independent role values and two assignments, if `RoboticistRole` is current separately from `EngineerRole` | use only when the project really needs two independent roles |
| "engineer-roboticist and musician" | one robotics-qualified engineering role expression or role value plus one independent musician role value | preferred ordinary wording when robotics qualifies engineering, while musician is separate |
| "engineer-roboticist-musician" | one declared combined role value or one named role-bundle expression | use only when the bounded context declares that combined value or bundle name; otherwise it hides independent assignments |
| "robot engineering", "music performance", or "teaching robots music" | method, method family, work, or work family | name under `A.3.1`, `A.3.2`, or `A.15`; these are not role-relation products merely because their labels share role words |
| "role algebra", "role graph", "role matrix", or "role embedding" | mathematical or representation description of selected role relation structure | name the lens or representation only when that description is the governed value; otherwise name the recovered role relation, role expression, assignment, method, or work |

`Role` and `Method` suffixes are optional Tech-register disambiguators. They are not ordinary-name requirements and they do not create the FPF kind. A user-facing sentence may say "Vasya is an engineer-roboticist and musician" without saying "role" when the FPF record or surrounding context lets a reader recover the role expression, role values, holder assignments, methods, and work separately.

Hyphenation is not algebra by itself. Use a hyphenated ordinary label when it helps a reader see a recovered factor, domain, practice, method-family qualification, or combined role expression. Use "and" when the current point is multiple independent role assignments. Do not mechanically concatenate operands into a Tech label.

The math-lens boundary is narrow. A role-algebra, graph, matrix, embedding, distributed, or neural representation is a lens over role values, role-requirement substitution relations, incompatibility relations, role-factor or qualification expressions, and role-bundle expressions. The lens is not itself the role, holder, assignment, method, work, or capability. The name attaches to the recovered object or expression, not to the notation that helped recover it.

### A.2.7:5 - Archetypal Grounding - Worked Cases

#### A.2.7:5.1 - Role-Requirement Substitution Without Capability Smuggling

`PlantMaintenance_2026` declares:

```text
SeniorHydraulicsTechnician <= HydraulicsTechnician
```

A method step requiring `HydraulicsTechnician` may accept an assignment to `SeniorHydraulicsTechnician`. This does not prove that the technician has the pressure-test capability. The method step may separately require `PressureTestCapability` under `A.2.2`.

#### A.2.7:5.2 - Incompatibility for Independence

`SafetyCase_2026` declares:

```text
HazardAnalysisAuthor incompatibleWith HazardAnalysisApprover
```

The same holder cannot use overlapping assignments for both roles when approving the same hazard analysis. If a source sentence says "the approver role is independent", A.2.7 recovers the role incompatibility relation; evidence of independence, approval work, and approval records stay in their direct patterns.

#### A.2.7:5.3 - Bundle Expression Without New Capability

`IncidentOps_2026` declares:

```text
IncidentLeadOnCall := IncidentCommander and Communicator and DecisionMaker
```

This is a reusable role-bundle expression for method requirements. It does not state that one person has incident-management capability; that remains a capability claim. It does not state that incident work happened; that remains a work claim.

#### A.2.7:5.4 - Naming Engineer-Roboticist and Musician

A project says: "Vasya is an engineer, does robot engineering, is therefore an engineer-roboticist. These are musical robots, and Vasya is also a musician, performs music, and teaches robots music."

Good ordinary rewrite:

> Vasya is our engineer-roboticist and musician: he works on robot engineering, and in the musical-robots project he also performs music and teaches robots music.

This ordinary sentence is admissible because a reader can recover the separate FPF values behind it:

```text
BoundedContextRef: MusicalRobotLab_2026
HolderRef: Vasya
EngineeringRoleExpression: EngineerRole qualified by robotics domain, robotics-engineering method family, practice, or work field
OrdinaryRoleLabel: engineer-roboticist or robotics engineer
IndependentRoleValue: MusicianRole
HolderAssignmentRefs: Vasya assigned to the robotics-qualified engineering role expression or declared RoboticsEngineerRole; Vasya assigned to MusicianRole
MethodOrWorkRefs: robot-engineering method or work; music-performance work; robot-music-teaching method or work
RepresentationLensRefs?: role-algebra, graph, matrix, embedding, or neural representation only if the project explicitly uses such a description of the role relation structure
```

Do not write "engineer and roboticist and musician" unless `EngineerRole`, `RoboticistRole`, and `MusicianRole` are three independent role values with separate assignments.

Do not write "engineer-roboticist-musician" unless the bounded context declares one durable combined role value or one named role-bundle expression with its own role description and naming settlement. Without that declaration, the label hides that musician is a separate role assignment.

Robot-engineering, music performance, and teaching robots music are method or work names when those values are current. They are not produced by a role-algebra lens merely because their labels share words with role names. The role relation structure and a `MethodRelationStructure@BoundedContext` can be coupled in the same working sentence, but the FPF record keeps their typed values distinct.

### A.2.7:6 - Cross-Context Boundary

Role relation structure is context-local. Matching role labels across contexts are not enough.

`ArticleAssessorRole:JournalContext` and `SafetyAssessorRole:SafetyCaseContext` may share a source label, but a role-requirement substitution or incompatibility relation in one context does not transfer to the other context by label. Cross-context reuse, bridge, translation, public naming, or semantic alignment uses F-family context and naming patterns.

### A.2.7:6.1 - Bias-Annotation

A.2.7 blocks two biases. The first is role nominalism: a convenient role label starts carrying ability, permission, method, work, evidence, or status claims that belong elsewhere. The second is representation bias: a role algebra, graph, matrix, embedding, or neural representation is mistaken for the role relation structure in life. Recover the relation in the bounded context first; then use a representation lens only for the properties it preserves.

### A.2.7:7 - Conformance Checklist

| Check | Question |
|---|---|
| `CC-A2.7-01` | Is the bounded context named? |
| `CC-A2.7-02` | Are the related values `U.Role` values governed by A.2? |
| `CC-A2.7-03` | Is each `<=` claim framed as same-context role-requirement substitution rather than kind hierarchy or generic specialization? |
| `CC-A2.7-04` | Is incompatibility checked over role assignments, holders, and overlapping windows rather than over labels alone? |
| `CC-A2.7-05` | Is a bundle expression kept separate from holder, capability, method, and performed work? |
| `CC-A2.7-06` | Do capability requirements use A.2.2? |
| `CC-A2.7-07` | Do assignment and state checks use A.2.1 and A.2.5? |
| `CC-A2.7-08` | Do method claims use A.3 patterns and work claims use A.15 patterns? |
| `CC-A2.7-09` | Do cross-context equivalence and translation claims use F-family patterns? |
| `CC-A2.7-10` | Does any evidence, source, approval, status, assurance, publication, description, or strict-distinction claim use `C.2.1`, `A.10`, `B.3`, `E.17.*`, `E.24.PUB`, or `A.7` rather than expressed as role relation structure or a lens over it? |

### A.2.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Role relation structure as type hierarchy | `EngineerRole <= HumanSystem`. | Keep role relation over `U.Role` values; use kind taxonomy only for kinds. |
| Role relation structure as org chart | "Manager is above Engineer, therefore satisfies Engineer." | Declare same-context role-requirement substitution only when that role-requirement relation is intended. |
| Role-requirement substitution as capability model | "Senior role implies precision capability." | Keep the substitution relation separate; add `U.Capability` claim for measured ability if current. |
| Bundle as new holder | `IncidentLeadOnCall` is treated as a person or team. | Treat it as role-bundle expression unless a role value or holder is separately declared. |
| Incompatibility as slogan | "Approver is independent" without relation. | State the incompatible role values, holder relation, bounded context, and overlapping window condition. |
| Cross-context label equivalence | Same role label in two contexts is treated as the same role relation structure. | Use F-family bridge or naming patterns; do not import role relations by label. |
| Episteme as role relation structure | A standard, report, or dashboard is put into role relation structure. | Use `C.2.1`, `A.10`, `B.3`, `E.17.*`, `E.24.PUB`, or `A.7` for the source, evidence, status, assurance, publication, description, or strict-distinction claim being made. |

### A.2.7:9 - Consequences

**Benefits.**

- Method requirements can accept declared role substitutions without encoding taxonomy in every method step.
- Separation-of-duties and independence claims become inspectable relations over assignments and windows.
- Frequent role conjunctions can be named without creating fake holders or capabilities.
- Role relation structure remains small enough to use in ordinary project work.

**Costs.**

- Contexts need to declare their role relations instead of relying on job-title intuition.
- Some role-like source labels need F-family cross-context repair before role relation structure can be reused.
- Capability and method requirements need separate claims when role labels used to hide them.

### A.2.7:10 - Rationale

A.2.7 keeps role relation structure as a selected relation structure rather than a new U-kind because the durable object is still `U.Role` and its contextual use through assignments, states, methods, and work claims. This preserves ordinary role naming while preventing algebraic notation or organizational labels from becoming a second ontology.

### A.2.7:10.1 - SoTA-Echoing

| Practice line | What FPF takes | Practical implication |
|---|---|---|
| Role-based access-control and separation-of-duties practice supplies stable relations among roles, users, sessions, and constraints. | A.2.7 keeps the role-relation part but does not turn access-control policy into general role ontology. | Role substitution and incompatibility are declared relations, not labels or permissions. |
| Attribute-based and zero-trust authorization practice separates role-like attributes, current context, policy decision, and resource action. | Role relation structure is one input to a check; capability, state, policy, and work remain separate. | "Has role" does not prove ability, currentness, permission, or performed work. |
| Organizational design and safety practice uses separation of duties and independence constraints beyond IT. | Incompatibility is stated over role assignments and windows in any bounded context. | Safety, audit, laboratory, governance, and operations examples do not become software-only. |
| Current FPF slot-relation and ontic discipline keeps relation positions from becoming kinds. | Role relation structure relates role values; it does not create a new role-slot ontic or reduce role to SlotKind. | A.2.7 can cite A.6.5 and E.24 without duplicating them. |

Source-currentness note: RBAC and separation-of-duties are stable lineage, not the full current frontier. Current practice adds attribute and zero-trust authorization, context and currentness checking, policy-as-code practice, and FPF's newer slot-relation discipline. A.2.7 therefore keeps only the role-relation part and leaves currentness, policy decision, capability, method, work, and evidence to their direct patterns.

### A.2.7:11 - Relations

| Pattern | Relation |
|---|---|
| `A.1.1` | Supplies `U.BoundedContext`, the locality boundary for role relation structure. |
| `A.2` | Governs `U.Role` values ranged over by role relation structure. |
| `A.2.1` | Governs `U.RoleAssignment`, the relation checked when role-requirement substitutions, incompatibilities, or bundles are used for real holders. |
| `A.2.2` | Governs capability; role relation structure does not grant ability. |
| `A.2.5` | Governs role state and enactable-state admission; role relation structure does not prove current state. |
| `A.3.1`, `A.3.2`, `A.15`, `A.15.1`, `A.15.2` | Govern method, method description, plan, and performed work uses that may cite a role relation. |
| `A.6.5` | Supplies relation-slot discipline for role-relation declarations and use relations. |
| `A.6.RSIR` | Recovers role, slot, relation, signature, and interface source wording before role-relation repair when the source sentence is mixed. |
| `F.5`, `F.9`, `F.17`, `F.18` | Govern naming, cross-context bridge, public naming, and durable local names for role values, role expressions, role-method expressions, or bundle expressions when current. |
| `C.27` | Governs temporal windows and currentness when overlapping assignments or validity windows are material. |
| `C.2.1`, `A.10`, `B.3`, `E.17.*`, `E.24.PUB`, `A.7` | Govern episteme slot relation, evidence, assurance, publication, description, and strict-distinction uses that may justify a role-relation declaration or a check using it. |
| `C.29` | Governs mathematical-lens fit if a role-algebra, graph, matrix, embedding, distributed, or neural representation is itself under evaluation. |

### A.2.7:12 - Excluded Objects

Do not use `RoleRelationStructure@BoundedContext` or a role-algebra lens as the current object for:

- holder taxonomy, system kind hierarchy, or org chart hierarchy;
- capability model, skill model, performance threshold, or operating envelope;
- method family, algorithm family, or work procedure;
- work plan, work occurrence, approval act, or audit record;
- evidence graph, source record, standard, report, dashboard, publication, or model card;
- cross-context translation, public naming, or bridge claim.

Those values may cite or justify a role relation. They do not become role relation structure by adjacency.

### A.2.7:End

