## A.2.1 - U.RoleAssignment - Contextual Work-Role Assignment

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2.1:0 - Use This When

**Plain name.** Work-role assignment.

Use this pattern when a project must say which system, organization, person, team, service, agent, device, or other acting holon holds which `U.Role` in which bounded context, and when that assignment is current enough to admit, check, plan, or attribute work.

Typical moments:

- a work record says that "Alice reviewed", "Robot-7 inspected", "CI bot deployed", or "the operations team approved" and the role, holder, bounded context, or assignment window is missing;
- a method or method description names required roles, but the project has not linked those roles to concrete performers;
- a role state, capability requirement, separation-of-duties rule, or work gate depends on who holds the role now;
- a source phrase gives an episteme an "evidence role", "standard role", "status role", or "requirement role" and the text must be normalized without making epistemes into work performers;
- a local notation such as `Holder#Role:Context@Window` is useful, but the notation must not replace the typed relation it abbreviates.

**Primary EntityOfConcern.** The EntityOfConcern is `U.RoleAssignment`: a typed work-facing assignment relation value. It links an admitted acting holder, a `U.Role`, a `U.BoundedContext`, and any assignment-currentness window or assignment source that is current for the claim.

**Primary working reader.** The first reader is an engineer-manager, analyst, or FPF author who needs work attribution, role admission, role-state checks, method requirements, or responsibility language to remain inspectable across contexts and editions.

**First useful move.** Recover the four core slots of the assignment relation: holder, role value, bounded context, and assignment window when current. Then recover any direct work-role qualifier, role-state admission, capability requirement, method requirement, work-plan relation, or work occurrence through its governing pattern.

**What goes wrong if missed.** Role labels float without holders or contexts. A method appears to have been enacted by a document. A work record names a person but not the role under which the work was admitted. A report or standard is treated as if it held a role because it is used as evidence or requirement source. The corpus then grows one role ontology for work and a second role ontology for epistemes.

**What this buys.** `U.RoleAssignment` gives one narrow relation for work-facing role holding. It keeps role values reusable, work attribution replayable, method requirements checkable, and episteme evidence or status uses outside the role-assignment relation.

**Not this pattern when.**

- If the current claim is the role value itself, role taxonomy, or role relation-neighborhood, use `A.2`.
- If the current claim is ability or operating envelope, use `A.2.2`.
- If the current claim is role state, role-state predicate, or enactable-state admission, use `A.2.5`.
- If the current claim is role-requirement substitution, incompatibility, qualification, or role bundle, use `A.2.7`.
- If the current claim is method, method description, work plan, performed work, or role-method-work alignment, use `A.15` and the direct A.15 subpattern.
- If the current claim is evidence, source, standard, requirement, definition, explanation, publication, status, assurance, gate, or decision use of an episteme, use the direct pattern for that relation. Do not make the episteme a `U.RoleAssignment` holder.
- If "role" means a relation position, use `A.6.5` SlotSpec discipline.

### A.2.1:1 - Problem Frame

Work-facing roles are useful only after they are connected to concrete holders in a bounded context. "Reviewer", "operator", "deployer", "inspector", "authorizer", and "coordinator" are not enough by themselves. The project needs to know which holder bears the role, in which context, for which window or current claim, and under which neighboring role-state, capability, method, plan, and work relations.

The assignment relation must be narrow. It should not absorb capability, method, work, evidence, status, or publication use. A standard used as a requirement source can constrain work, but it does not hold a work-facing role. A report can be used as evidence, but it does not perform the review that produced it. A method description can require `ReviewerRole`, but the method description is not the reviewer.

A.2.1 therefore defines `U.RoleAssignment` as a typed relation value using `A.6.5` SlotSpec discipline. The relation is work-facing: its holder is a `U.System` or acting holon admitted as system-like performer by the governing work or method pattern. Epistemes stay in evidence-use, status-use, source-use, publication-use, requirement-use, definition-use, explanation-use, assurance-use, gate-use, or decision-use relations.

### A.2.1:2 - Problem

Without this pattern:

1. **Role labels do not identify performers.** Work records name a role-like word, but not the holder and context needed for attribution.
2. **Assignment and role collapse.** The role value, the holder, the bounded context, and the assignment window become one label.
3. **Assignment and capability collapse.** A role assignment is treated as evidence of ability, even though capability has its own envelope and evidence.
4. **Assignment and method collapse.** Holding a role is treated as if the holder automatically has a method or has already performed work.
5. **Episteme-role drift returns.** Standards, reports, datasets, definitions, requirements, and model cards are described as role holders instead of being related through evidence, status, source, publication, requirement, or assurance relations.
6. **RoleEnactment becomes a second run-time object.** A derived performed-by fact is mistaken for a durable U-kind beside `U.Work`.
7. **Slot discipline is lost.** Holder, role value, context, window, justification, provenance, and qualifier positions are not recoverable as distinct SlotKinds.

### A.2.1:3 - Forces

| Force | Tension |
| --- | --- |
| Local meaning vs corpus reuse | Role assignments must be local to one bounded context, while the pattern must remain reusable across engineering, organizations, software, AI agents, laboratories, and governance work. |
| Traceability vs relation overreach | Work attribution needs a concrete assignment relation, but the assignment must not swallow method, capability, evidence, status, or publication semantics. |
| Open-world use vs heavy forms | Some assignment claims need only holder, role, and context; other claims need window, state assertion, assignment source, capability, or method details. Missing optional-in-use slots must not force dummy values. |
| Role state vs work occurrence | A role assignment can be current while the holder is not in an enactable role state; work occurrence is still a separate dated occurrence. |
| Ordinary notation vs ontology | `Holder#Role:Context@Window` is memorable, but it is notation for a typed assignment relation, not the relation's ontology. |
| Episteme use vs work performance | Epistemes can be used as evidence, standard, requirement, definition, explanation, status bearer, publication, or assurance input; they do not perform work by holding work-facing roles. |

### A.2.1:4 - Solution

Use `U.RoleAssignment` for the typed relation that assigns a work-facing `U.Role` to an admitted acting holder in one bounded context.

```text
RoleAssignmentCoreSlotSpec:
  HolderSlot:
  RoleValueSlot:
  BoundedContextSlot:
  AssignmentWindowSlot:
  AssignmentJustificationSlot:
  AssignmentProvenanceSlot:
```

This is a relation value. A record, registry row, publication, diagram, or file may describe, cite, or store the relation value. It is not the assignment itself by default.

#### A.2.1:4.1 - Core SlotSpecs

| SlotKind | ValueKind | Slot-use disposition | Meaning |
| --- | --- | --- | --- |
| `HolderSlot` | `U.System` or acting holon admitted as system-like performer by the governing work or method pattern | identity slot | The holder that bears the role in the bounded context. `U.Episteme` is not admitted here merely because it is used as evidence, source, standard, requirement, explanation, status bearer, publication, or assurance input. |
| `RoleValueSlot` | `U.Role` | identity slot | The context-bound role value governed by `A.2`. It is not a SlotKind and not a capability. |
| `BoundedContextSlot` | `U.BoundedContext` | identity slot | The context that gives the role value its local meaning. |
| `AssignmentWindowSlot` | assignment-currentness window, role-state window, or temporal-validity value governed by the temporal pattern current in the project | optional-in-use; currentness-required when the claim depends on current assignment validity | Missing window means not recovered or not current for the claim, not that no window exists. |
| `AssignmentJustificationSlot` | source, speech act, policy, gate, decision, rule, or evidence relation governed by its direct pattern | currentness-required when the assignment admission is challenged or relied upon | This slot points to why the assignment claim is admitted; it does not replace the governing speech-act, gate, policy, or evidence pattern. |
| `AssignmentProvenanceSlot` | provenance relation for issuing, recording, or refreshing the assignment claim | consideration slot; currentness-required when auditability or source order is current | This slot is not a bucket for target claim, evidence polarity, status value, evidence window, or publication form. |

Direct work-role patterns may declare additional work-role qualifier SlotSpecs. Evidence-use and status-use relation slots are not assignment qualifiers unless a direct work-role pattern explicitly makes that work-role claim.

#### A.2.1:4.2 - Well-Formedness Constraints

Use these constraints as predicates over a filled assignment relation.

```text
Invariant RA-S1 (Local role):
  RoleValueSlot content is a U.Role admitted in the BoundedContextSlot content.

Invariant RA-S2 (Holder admission):
  HolderSlot content is a U.System or an acting holon admitted as system-like performer by the governing work or method pattern.

Invariant RA-S3 (No role-as-holder):
  HolderSlot content is not U.Role and not U.RoleAssignment.

Invariant RA-S4 (No episteme holder by use):
  U.Episteme is not admitted as HolderSlot content merely because the episteme is used as evidence, source, standard, requirement, definition, explanation, publication, status bearer, or assurance input.

Invariant RA-S5 (Context locality):
  Cross-context assignment reuse requires a named bridge or direct context relation; shared labels do not create sameness.

Invariant RA-S6 (Window honesty):
  A claim that depends on current assignment validity names AssignmentWindowSlot content, inherits a declared bounded-context default, or states that the window is unknown, not recovered, not asserted, or blocking for the stronger claim.
```

Do not express these predicates with RFC-style deontics unless the sentence is imposing a duty on an author, validator, or published record.

#### A.2.1:4.3 - Open-World Slot Disposition

The SlotSpecs are a thinking discipline, not a demand to fill a form for every casual use.

Use these dispositions:

- **filled:** the relation instance names the slot filler or reference;
- **inherited:** the role definition or bounded-context rule fixes the value for the current claim;
- **unknown or not recovered:** the slot is relevant, but the project has not recovered it;
- **not asserted:** the text deliberately makes no claim about this slot;
- **not current for this claim:** the slot exists in the model, but the present claim does not depend on it;
- **claim lowering or blocker:** a stronger claim depends on the slot, so missing content lowers or blocks that claim.

For example, a quick staffing note may only need holder, role, and context. A safety-critical work attribution claim needs the assignment window, role-state admission, and method or work relation that the note omitted.

#### A.2.1:4.4 - Role State and Role-Description Characterization Hooks

`U.RoleAssignment` does not contain a role-state relation or a role-state description. The `U.Role` and its role description may be linked to:

- RoleCharacteristicSpace, the characteristic space used to describe role variants or role requirements in one bounded context;
- Role State Relation, the state-family relation used to decide whether a role assignment is in an enactable state;
- state assertions or evaluations governed by `A.2.5` and the relevant evidence or evaluation pattern.

A work attribution claim may depend on those neighboring values. The assignment relation names the holder, role, context, and window; `A.2.5` governs whether the assignment is in an enactable state for the current work.

#### A.2.1:4.5 - Role Assignment and Work

Work is not performed by the role value. Work is performed by the holder under a role assignment.

Use the direct relation:

```text
Work.performedBy = RoleAssignment
```

Then check neighboring claims:

- the work occurrence is governed by `A.15.1`;
- the selected method is governed by `A.3.1`;
- the method description or required-role declaration is governed by `A.3.2` and `A.15`;
- the work plan is governed by `A.15.2`;
- role-state admission is governed by `A.2.5`;
- capability is governed by `A.2.2`.

A `U.Work` record may cite `performedBy = some U.RoleAssignment`. That citation does not make the work record the assignment and does not make the assignment a work occurrence.

#### A.2.1:4.6 - RoleEnactmentFact

Source text may name `U.RoleEnactment` or `RoleEnactment`. In FPF, role enactment is a derived relation or fact over `U.Work` and `U.RoleAssignment`, not a durable U-kind.

Use this named fact only when a named relation is clearer than direct `performedBy` wording:

```text
RoleEnactmentFact:
  workOccurrence: U.Work
  performedBy: U.RoleAssignment
  methodTrace?: U.Method or U.MethodDescription reference when current
  window?: inherited from work occurrence or role assignment when current
```

If a database, log, table, or publication stores a role-enactment entry, it stores a record of the fact unless a direct governing pattern admits record-as-value for that use.

#### A.2.1:4.7 - Episteme Evidence, Status, Source, and Publication Uses

Do not use `U.RoleAssignment` for an episteme merely because the episteme is useful in a project relation.

| Source phrase | Recover as |
| --- | --- |
| "this report has evidence role for Claim A" | evidence-use relation with evidence episteme, target claim, claim scope, polarity, and relevance window when current. |
| "the standard has normative role" | standard-use, requirement-use, source-use, publication-use, or status-use relation under the direct pattern. |
| "the dataset plays the role of benchmark" | dataset-use, evidence-use, measurement, benchmark, or source-use relation under the direct pattern. |
| "the model card is the approver" | publication, evidence, assurance, or source relation for the model card; any approving work is performed by a system or acting holon through a role assignment. |
| "the dashboard role is monitoring" | publication or interface description use for the dashboard; observing work belongs to an observer holder under a role assignment. |

The repair is not to find a nicer role word. The repair is to recover the current relation and its slot fillers.

#### A.2.1:4.8 - Shorthand Notation

The compact notation is:

```text
Holder#Role:Context@Window
```

Use it only as a readable notation for the typed assignment relation.

Examples:

- `Robot_7#InspectorRole:MaintenanceLine_A@2026-06-15T09:00..2026-06-15T11:00`
- `OpsTeam#IncidentCommanderRole:PlantIncident_2026@open`
- `CI_Service#DeployerRole:ReleaseTrain_2026@2026-Q2`

If the notation is missing the window, the current text must still say whether the window is inherited, unknown, not asserted, or not current for this claim when the claim depends on assignment currentness.

### A.2.1:5 - Archetypal Grounding

#### A.2.1:5.1 - Industrial Inspection Work

A maintenance line assigns an inspection role to a robot for one shift.

```text
Robot_7#InspectorRole:MaintenanceLine_A@2026-06-15T09:00..2026-06-15T11:00
```

The holder is a system. The role value is `InspectorRole`. The bounded context is `MaintenanceLine_A`. The assignment window covers the planned inspection shift.

This does not assert that the robot has the required sensor capability. Capability stays under `A.2.2`. It does not assert that inspection work already occurred. Performed work stays under `A.15.1`. It only gives later method, plan, role-state, and work-attribution claims a typed assignment relation to cite.

#### A.2.1:5.2 - Software Deployment

A release train has a deployment method description with a step requiring `DeployerRole`.

```text
CI_Service#DeployerRole:ReleaseTrain_2026@2026-Q2
Work DeploymentRun_418 performedBy CI_Service#DeployerRole:ReleaseTrain_2026
```

The assignment relation admits a candidate performer. The work occurrence still needs the method or method-description relation, the assignment window, and any enactable role-state assertion required by `A.2.5`. A green test suite, ticket approval, or policy rule may justify the assignment or the work gate, but those are neighboring evidence, gate, or policy relations, not hidden role values.

#### A.2.1:5.3 - Review Report and Reviewer

A human reviewer or review service can hold `ReviewerRole` in a review context. The review report produced by that work is an episteme.

Later, another team may use the report as evidence for a claim. That later relation is evidence-use around the report. The report does not hold `ReviewerRole`; the reviewer holder did.

#### A.2.1:5.4 - Standard Used in Safety Work

The source sentence "ISO 26262 has the normative standard role in this safety case" is repaired as a standard-use or requirement-use relation around an episteme. If a safety engineer performs work using that standard, the engineer or engineering team may hold a work-facing role assignment. The standard constrains, defines, or supplies source material; it does not perform work and does not become a holder in `U.RoleAssignment`.

### A.2.1:6 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Semio-bias | The pattern starts talking mainly about reports, standards, records, cards, and publication forms. | Keep `U.RoleAssignment` as the primary EntityOfConcern. Treat descriptions and publications as neighboring epistemes. |
| Episteme-as-agent drift | A standard, report, dataset, proof, or model card is treated as if it performed work. | Use direct evidence-use, source-use, status-use, publication-use, requirement-use, definition-use, explanation-use, assurance-use, gate-use, or decision-use relations. |
| Slot-role drift | Holder, role value, context, window, justification, or provenance words become untyped fields. | Use `A.6.5` SlotSpec discipline and keep the filled values under their governing patterns. |
| Work-admission shortcut | A role assignment is treated as permission, gate passage, capability, or completed work. | Recover the direct work-admission, gate, capability, method, plan, or work claim before acting. |
| Notation bias | `Holder#Role:Context@Window` is treated as the ontology. | Use the notation only after the assignment relation and core slots are recoverable. |

### A.2.1:7 - Conformance Checklist

| ID | Check |
| --- | --- |
| `CC-A2.1-1` | A `U.RoleAssignment` identifies holder, role value, and bounded context. |
| `CC-A2.1-2` | The holder is a `U.System` or acting holon admitted as system-like performer by the governing work or method pattern. |
| `CC-A2.1-3` | No `U.Role`, `U.RoleAssignment`, or `U.Episteme` is used as holder merely because source language says "role". |
| `CC-A2.1-4` | Any claim depending on current assignment validity names the assignment window, inherits a declared bounded-context default, or lowers or blocks the stronger claim. |
| `CC-A2.1-5` | The assignment relation is not used as evidence of capability, selected method, planned work, performed work, gate passage, commitment, permission, or evidence-use relation. |
| `CC-A2.1-6` | `Work.performedBy` points to a concrete `U.RoleAssignment` when work attribution depends on role holding. |
| `CC-A2.1-7` | Any named `RoleEnactmentFact` is stated as derived over `U.Work` and `U.RoleAssignment`, not as a durable U-kind. |
| `CC-A2.1-8` | Evidence-use and status-use of epistemes are expressed through direct evidence, status, source, publication, requirement, definition, explanation, assurance, gate, or decision relations, not through `U.RoleAssignment`. |
| `CC-A2.1-9` | Role state and enactable-state admission are governed by `A.2.5`; role relation structure is governed by `A.2.7`; capability is governed by `A.2.2`; method and work are governed by `A.15` and A.15 subpatterns. |
| `CC-A2.1-10` | Shorthand notation is not used unless the typed relation and any current missing-slot disposition are recoverable. |

### A.2.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Contextless assignment: "Alice is reviewer" | No bounded context, role identity, or assignment window is recoverable. | Recover `Alice#ReviewerRole:ReviewContext` and state window disposition when current. |
| Episteme as holder: "The report has EvidenceRole" | The report is being used in an evidence relation, not holding a work-facing role. | Use evidence-use relation with target claim, scope, polarity, and relevance window when current. |
| Assignment as capability | The role assignment is treated as evidence that the holder can perform the work. | Use `A.2.2` for capability and connect capability evidence only when the claim depends on it. |
| Assignment as work | The assignment is treated as if work already happened. | Use `A.15.1` for dated work and cite `performedBy = RoleAssignment`. |
| `U.RoleEnactment` as root object | A derived performed-by fact becomes a second run-time ontology. | Use `RoleEnactmentFact` only as a named fact over work and assignment, or write direct `Work.performedBy` relation. |
| Window omitted in a time-sensitive claim | Currentness is assumed by silence. | Fill, inherit, mark unknown, mark not asserted, or lower the stronger claim. |
| Evidence and status slots hidden in assignment provenance | Evidence polarity, target claim, status value, or status window is buried under assignment source. | Use direct evidence-use or status-use SlotSpecs; keep assignment provenance only for the assignment claim. |

### A.2.1:9 - Consequences

`A.2.1` makes work attribution and role admission replayable. A reader can ask: who is the holder, what role value is assigned, which bounded context gives that role meaning, and which window or source is current for the claim?

The benefit is compactness. FPF can keep one role-assignment relation for work-facing roles instead of multiplying role kinds for documents, standards, reports, dashboards, interfaces, method descriptions, and relation arguments.

The cost is discipline. Authors must recover neighboring claims instead of putting them into assignment prose. Capability, role state, method, work plan, performed work, evidence, status, publication, assurance, gate, and decision claims each keep their governing pattern.

Reopen `A.2.1` only when the core assignment relation changes: admitted holder kinds, SlotSpecs, assignment-currentness discipline, direct work-role qualifiers, or the treatment of `RoleEnactmentFact`. Reopen neighboring patterns when the dispute is about capability, role state, method, work, evidence, status, source, publication, assurance, gate, or decision use.

### A.2.1:10 - Rationale

The role `ontologicalNeighborhood` needs both role values and assignment relations. `A.2` keeps `U.Role` as a compact context-bound value. `A.2.1` gives that value a typed relation to a holder and context. `A.15` then lets work cite the assignment.

The selected ontology prevents two common explosions. First, it prevents every context-local role from becoming a system subtype. Second, it prevents every evidence or status use of an episteme from becoming another role assignment.

The open-world slot model is deliberate. FPF should not require dummy windows or provenance entries for low-risk recognition text. It should also not permit stronger claims to rely on missing windows, missing role-state admission, or missing assignment source. The slot is considered when the claim needs it.

### A.2.1:11 - SoTA-Echoing

| Practice line | Current source line | FPF adoption |
| --- | --- | --- |
| OntoUML and UFO role modeling treat roles as context-dependent classifications rather than intrinsic substance kinds. | UFO and OntoUML work through the 2020s, including the 2026 gUFO line, keeps role-like and relation-like structures explicit rather than turning every slot filling, relation position, or use relation into a new object kind. | Adopt the holder-role separation: the same holder can bear different roles in different contexts without becoming a new system kind. |
| Bounded-context practice in domain-driven design and distributed-system architecture treats names as local to a context and requires explicit translation across boundaries. | Modern DDD and microservice architecture practice keeps role names local to a model boundary and treats cross-boundary sameness as a bridge, not as label equality. | Adopt context-local role meaning and require bridges or direct context relations for cross-context role reuse. |
| Modern identity, access-management, zero-trust, and policy-as-code practice separates subject, role or attribute relation, policy decision, and resource action. | NIST SP 800-207 (2020) separates authentication and authorization functions before resource access; NIST SP 800-53 Rev. 5 and its 2025 update expose control, assessment, authorization, and control-currentness material explicitly. | Adapt this separation: `U.RoleAssignment` is not capability, permission, gate passage, policy decision, or performed work; those claims stay in direct neighboring patterns. |
| Safety, quality, and security assurance practice uses traceable responsibility and separation-of-duties checks rather than role labels alone. | Current security and assurance control practice keeps accountability, assessment, authorization, and monitoring as checkable relations over systems and records rather than as names alone. | Adopt the replay chain from work occurrence to role assignment, role value, context, role-state admission, and evidence when current. |
| Provenance and evidence graph practice separates the work that produced a report from later evidence-use of the report. | Contemporary provenance and evidence-graph practice distinguishes event or work occurrence, produced episteme, and later evidence or assurance use. | Adopt the episteme boundary: reports, standards, datasets, and model cards participate through evidence, status, source, publication, requirement, or assurance relations, not as role-assignment holders. |

### A.2.1:12 - Relations

**Builds on.**

- `A.1` and `A.1.1` for holons, systems, and bounded contexts.
- `A.2` for `U.Role` identity, taxonomy, and role relation-neighborhood.
- `A.6.5` for SlotSpec discipline.

**Coordinates with.**

- `A.2.2` for capability.
- `A.2.5` for role state, role-state relation, role characterization, and enactable-state admission.
- `A.2.7` for context-local role relation structure.
- `A.15`, `A.15.1`, and `A.15.2` for method, work plan, work occurrence, and performed-by relation.
- `A.3.1` and `A.3.2` for method and method-description required-role relations.
- `A.10`, `B.3`, `C.2.1`, `C.28`, `F.10`, `G.6`, `E.17`, and `E.10.D2` for evidence-use, status-use, source-use, publication-use, assurance, causal-use, and description-boundary cases that source text tries to express as episteme roles.

**Does not replace.**

- `U.Work`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Capability`, evidence relations, status assertions, gate decisions, commitments, permissions, or publication forms.
- `A.6.5` relation-slot discipline. A.2.1 uses it for this assignment relation; it does not become a second slot discipline.

### A.2.1:End

