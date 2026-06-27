## A.2.5 - RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2.5:0 - Use This When

**Plain name.** Role-state space.

### A.2.5:0.1 - Kind Settlement

A.2.5 does not admit `U.RoleStateGraph` as a durable U-kind. The governed object is `RoleStateRelation@BoundedContext`: a selected context-local relation structure over `U.Role`, `U.BoundedContext`, role-state values, state predicates, state assertions, and work-admission relations. State-machine or graph notation is a mathematical or representation lens over that relation structure, not the object itself and not a new root beside `U.Role`.

Use this pattern when a project needs to decide whether a role assignment is currently in a state that admits a work claim, a method-step claim, an incompatibility claim, or a role-readiness claim.

Typical moments:

- a work record says that a person, team, device, service, agent, or machine acted as technical checker, operator, deployer, verifier, surgeon, sensor, or incident commander, but the current role state is unclear;
- a method description names a required role, and the project needs to state which role states admit the step;
- a role assignment is current, but the holder may be suspended, stale, uncalibrated, fatigued, not yet authorized, or otherwise not in an enactable state;
- a role-relation claim such as role-requirement substitution, incompatibility, or bundle expression depends on role states rather than labels alone;
- a source says "ready", "approved", "validated", "authorized", "active", "stale", or "blocked" and it is unclear whether this is a role state, an evidence or status relation around an episteme, an admission result, a capability value, or a work occurrence.

**Primary EntityOfConcern.** The EntityOfConcern is `RoleStateRelation@BoundedContext`: the selected context-local state-space relation for one `U.Role` in one `U.BoundedContext`. It names role states, state predicates, state-change predicates when current, and the subset of states that admit work through a `U.RoleAssignment`. It is a real FPF object, but it is not a new `U.*` kind beside `U.Role`; its identity is carried by the role value, bounded context, state set, state predicates, and work-admission relation.

**Primary working reader.** The first reader is an engineer-manager, analyst, safety checker, operations lead, or FPF author who needs to keep role assignment, role state, holder capability, method requirement, and performed work distinct while still deciding whether a work claim may proceed.

**First useful move.** Name the role and bounded context, list the states that matter for the current claim, mark which states admit work, and state what observation, evaluation, speech act, work record, or source relation can justify a `StateAssertion` for the relevant window.

**What goes wrong if missed.** A role label becomes a permission slip. A role assignment is treated as ability. A certificate, report, standard, status marker, or dashboard is treated as if it held a work-facing role. Separation-of-duties checks operate on labels instead of states. Source phrases such as "approved evidence role" or unlabeled readiness marks create a second role ontology.

**What this buys.** Role admission becomes inspectable without making forms heavy. The same role value can have different current states in different contexts and windows; method and work claims can ask only for the state evidence they need; episteme evidence and status uses stay with their direct patterns.

**Not this pattern when.**

- If the current claim is the role value itself, use `A.2`.
- If the current claim is the assignment relation linking holder, role, bounded context, and assignment window, use `A.2.1`.
- If the current claim is ability or operating envelope, use `A.2.2`.
- If the current claim is role-requirement substitution, incompatibility, or bundle expression independent of current state, use `A.2.7`.
- If the current claim is selected method, method description, work plan, or performed work, use `A.15` and the direct A.15 subpattern.
- If the current claim is an episteme used as evidence, source, standard, requirement, definition, explanation, publication, status bearer, assurance input, or admission input, use the direct pattern for that relation. Do not turn the episteme into a role holder or role state.

### A.2.5:1 - Problem Frame

Work-facing role assignment is not enough for safe work attribution. "Dana holds IncidentCommanderRole" may be true while Dana is off-duty, conflicted by another role assignment, outside the current assignment window, or missing a fresh authorization source. "Robot-7 holds InspectorRole" may be true while the robot is uncalibrated. "Thermometer T-17 holds ObserverRole" may be true while the calibration evidence is stale.

The project needs a small state space for each important role in each bounded context. That state space says which role states exist, which state predicates justify them, and which states admit work. It is not a method order, not a task list, not a capability, not a work log, and not an episteme status ontology.

A.2.5 therefore defines `RoleStateRelation@BoundedContext` as a selected relation structure around a `U.Role` and bounded context. It uses state-machine or graph notation only as a selected mathematical or representation lens where helpful. The FPF object is the role-state relation used for work admission and role-state claims.

### A.2.5:2 - Problem

Without this pattern:

1. **Assignment and state collapse.** A holder assigned to a role is treated as currently ready.
2. **Role and capability collapse.** A state label such as "ready" is treated as ability instead of a window-bounded state assertion.
3. **Role state and work collapse.** Being in a state is mistaken for having performed the work.
4. **State and source collapse.** A certificate, report, standard, model card, dashboard, or publication is treated as the state itself rather than as a source or evidence relation for a state assertion.
5. **Label-only incompatibility appears.** Incompatibility checks block or admit work by role names rather than by enactable states in a window.
6. **Context drift returns.** "Approved" or "Ready" travels across contexts without named state predicates or loss.
7. **Enactment reification survives.** `RoleEnactment` becomes a durable root value even though performed work is governed by `U.Work` and `U.RoleAssignment`.

### A.2.5:3 - Forces

| Force | Tension |
| --- | --- |
| Minimal use vs safety | Ordinary use needs a small state list; high-consequence work needs windowed state assertions and evidence. |
| Role assignment vs role state | `U.RoleAssignment` says who holds the role; `RoleStateRelation@BoundedContext` says what states that role can be in and which states admit work. |
| State-machine clarity vs method-order drift | State diagrams are useful, but this pattern does not encode method order or work-order structure. |
| Authorization words vs capability | "Authorized", "permitted", and "ready" can be role states, but they do not create capability. |
| Status words vs episteme use | "Approved standard" or "validated dataset" may be an episteme status-use relation, not a work-facing role state. |
| Context reuse vs local meaning | State names are memorable, but their predicates and admission effect stay local to one bounded context unless a bridge or comparison relation is declared. |

### A.2.5:4 - Solution

Use `RoleStateRelation@BoundedContext` for the state-space relation of one `U.Role` in one `U.BoundedContext`.

```text
RoleStateRelation:
  RoleValueRef:
  BoundedContextRef:
  RoleStateSet:
  EnactableStateSet:
  StatePredicateSet:
  StateChangePredicateSet:
  StateAssertionRelation:
  RoleRelationStructureHooks:
  UKindDisposition: non-U selected relation structure
```

This is a relation value. A role description, policy, register, diagram, checklist, or publication may describe or store the relation value. The description or register is not the role-state relation itself by default.

Do not promote this object to a separate `U.*` kind. `RoleStateRelation@BoundedContext` has action-facing use because it controls role-state admission, but the identity is reducible to slot and relation combinatorics over existing governed values: `U.Role`, `U.BoundedContext`, role-state values, state predicates, state assertions, and the work-admission relation through `U.RoleAssignment`. The durable U-kind remains `U.Role`; A.2.5 supplies the selected state relation inside the role `ontologicalNeighborhood`.

#### A.2.5:4.1 - Core SlotSpecs

| SlotKind | ValueKind | Slot-use disposition | Meaning |
| --- | --- | --- | --- |
| `RoleValueRef` | `U.Role` | identity slot | The role value whose states are being described. |
| `BoundedContextRef` | `U.BoundedContext` | identity slot | The context that gives state names and predicates their meaning. |
| `RoleStateSet` | finite set of context-local state values | identity slot | The named states relevant to this role in this context. |
| `EnactableStateSet` | subset of `RoleStateSet` | admission slot | The states that admit a work or method-step claim when a valid state assertion exists. Empty set is allowed when the role is never work-admitting in that context. |
| `StatePredicateSet` | predicates over role characteristics, observations, evaluations, work records, speech acts, source relations, or context values | recognition slot | The predicates used to assert that a holder is in a state for a window. |
| `StateChangePredicateSet` | predicates for entering, maintaining, or leaving states | consideration slot | Used when state change matters. It does not define method order. |
| `StateAssertionRelation` | relation from role assignment, state, window, and evidence values to an assertion verdict | currentness-required when role-state admission is claimed | The relation that justifies "this role assignment is in this state for this window." |
| `RoleRelationStructureHooks` | references to `A.2.7` role-requirement substitution, incompatibility, or bundle expressions | current when role relation structure affects admission | State-aware checks for role-requirement substitution, incompatibility, and bundles. |

The SlotSpecs are open-world. A casual role-state note may only name role, context, and a state. A safety-critical work claim may require state predicates, evidence, assignment window, role-state window, capability checks, and method-step relation. Missing relevant content lowers or blocks the stronger claim; it does not assert that the value cannot exist.

#### A.2.5:4.2 - State and State Assertion

**Role state.** A role state is a context-local value in the `RoleStateSet` for one `U.Role` and one bounded context. Names such as `Ready`, `Calibrated`, `Suspended`, `Authorized`, `Stale`, or `Blocked` are local labels until their predicates are named.

**Enactable state.** An enactable state is a role state admitted by `EnactableStateSet`. A method-step claim or work-attribution claim that requires the role can use that state only with a current `StateAssertion`.

**State assertion.** A `StateAssertion` says that one `U.RoleAssignment` is in one role state for one window, with named evidence or source relations.

```text
StateAssertion:
  RoleAssignmentRef:
  RoleStateRef:
  AssertionWindow:
  PredicateEvaluation:
  EvidenceOrSourceUseRefs:
  AssertionStatus:
```

`PredicateEvaluation` is governed by the evaluation or evidence pattern that owns the claim. The assertion does not make the evidence episteme a role holder.

#### A.2.5:4.3 - Enactable-State Admission

Use this admission predicate when a method or work claim depends on role state:

```text
EnactableStateAdmission:
  requiredRole: U.Role
  roleAssignment: U.RoleAssignment
  requiredContext: U.BoundedContext
  workOrMethodClaim:
  window:
  admitted iff StateAssertion(roleAssignment, state, window)
              and state is in EnactableStateSet(requiredRole, requiredContext)
```

This predicate admits or blocks the work or method-step claim. It does not create work, select a method, grant capability, or prove that work occurred.

#### A.2.5:4.4 - State Predicates and State-Change Predicates

State predicates answer: **is this assignment in this state for this window?**

Examples:

- `CalibrationAge <= 30 days`;
- `AuthorizationDecision exists within the stated window`;
- `FatigueScore below threshold`;
- `IndependenceFrom(holder, conflictingAssignment) is true`;
- `ObservationProcedureActive and calibration trace is current`;
- `NoOpenIncident above declared severity`.

State-change predicates answer: **what evidence or event changes the state relation?** They may reuse the same observations or decisions, but their use is different. A predicate that says calibration expired can justify a `Stale` state assertion; it still does not prescribe the method order for recalibration work.

#### A.2.5:4.5 - Role Relation Structure Hooks

When `A.2.7` declares role-requirement substitution, incompatibility, or bundle expressions, A.2.5 adds state-sensitive admission.

| Role relation | State-sensitive reading |
| --- | --- |
| `AcceptedRoleForRequirement <= RequiredRole` | A state assertion for the accepted role can satisfy the required-role requirement only when the context declares a state refinement relation and enactability is preserved. |
| `RoleA incompatibleWith RoleB` | The conflict is usually about overlapping enactable states for one holder in one window, not about labels alone. |
| `RoleA plus RoleB` bundle | A work claim requiring both roles needs state assertions for both role assignments in the same window, unless the bounded context declares a composite role with its own `RoleStateRelation@BoundedContext`. |

Do not construct product state spaces by default. Product states are admitted only when the bounded context actually maintains a composite role value and gives it its own `RoleStateRelation@BoundedContext`. A graph or state-machine diagram may describe that relation; it is not the relation in life.

#### A.2.5:4.6 - Separation From Capability, Method, Work, Evidence, and Status

| Temptation | Recover as |
| --- | --- |
| "Assigned, therefore able" | Role assignment in `A.2.1` plus capability claim in `A.2.2`. |
| "Ready, therefore work happened" | State assertion here plus performed-work claim in `A.15.1` only if a `U.Work` occurrence is named. |
| "Authorized, therefore method selected" | Role-state or decision claim here; selected method remains governed by `A.3.1`, `A.3.2`, and `A.15`. |
| "Report has evidence role" | Evidence-use relation around an episteme, not a role state. |
| "Standard has normative role" | Requirement-use, standard-use, status-use, source-use, or publication-use relation around an episteme. |
| "Dashboard is monitoring role" | Publication, interface, source, or evidence relation for the dashboard; observing work belongs to a holder under `U.RoleAssignment`. |
| "`RoleEnactment` occurred" | Use `U.Work` with `performedBy = U.RoleAssignment`; use `RoleEnactmentFact` from `A.2.1` only as a derived fact when naming the fact helps. |

### A.2.5:5 - Worked Slices

#### A.2.5:5.1 - Incident Commander

Context: `SRE_Prod_Cluster_EU_2026`.

Role: `IncidentCommanderRole`.

States:

- `OffDuty` - not in the on-call assignment window;
- `OnCall` - assignment window and contact source are current;
- `Authorized` - escalation decision source is current;
- `Ready` - on call, authorized, not conflicted, attention-pressure indicator below threshold;
- `RunningIncident` - currently performing incident-command work;
- `Blocked` - conflicting assignment or missing source.

`Ready` and `RunningIncident` are enactable states for incident-command work in this context. A work record for "Declare severity level" may cite `performedBy = Dana#IncidentCommanderRole:SRE_Prod_Cluster_EU_2026`, but the work claim is admitted only when a `StateAssertion` puts that assignment in `Ready` or `RunningIncident` for the declaration window.

#### A.2.5:5.2 - Thermometer Observer

Context: `Metrology_Thermo_2026`.

Role: `ThermometerObserverRole`.

States:

- `Unqualified` - no traceable calibration source;
- `Calibrated` - calibration source current;
- `Synchronized` - time relation within threshold;
- `InRange` - drift and environment predicates hold;
- `Measuring` - observation procedure is active;
- `Stale` - calibration or synchronization window expired;
- `Quarantined` - suspected contamination or bias.

`Measuring` is the only enactable state for the "record temperature" work claim. `Calibrated` and `Synchronized` are useful role states, but they do not by themselves admit observation work.

#### A.2.5:5.3 - Standard or Dataset With "Status Role" Source Wording

A source may say that a standard has an "approved role" or a dataset has an "evidence role." Do not make a `RoleStateRelation@BoundedContext` for the episteme unless a direct work-facing role is actually current. Usually the repair is:

- standard or requirement source: requirement-use, status-use, source-use, or publication-use relation;
- dataset or report: evidence-use, source-use, measurement, benchmark, freshness, or provenance relation;
- claim about the worker who approved, measured, verified, or published it: `U.Work` performed by a holder under `U.RoleAssignment`, with A.2.5 used only for that holder's role state.

### A.2.5:6 - Archetypal Grounding

**System side.** A role-state relation can govern a person, team, machine, service, software agent, laboratory instrument, organization, or other acting holon through `U.RoleAssignment`. The holder is still governed by `A.2.1`; capability by `A.2.2`; performed work by `A.15.1`.

**Episteme side.** A role-state relation may be described by an episteme, and evidence for a state assertion may be an episteme. That does not make the episteme a role holder. If the EntityOfConcern is a report, standard, dataset, requirement, proof, model card, or publication, the current relation is usually evidence-use, status-use, source-use, requirement-use, definition-use, explanation-use, publication-use, assurance-use, or admission-use.

### A.2.5:7 - Bias-Annotation

This pattern resists four common biases:

- **status-word bias:** treating `Approved`, `Ready`, or `Validated` as self-explanatory instead of context-local state predicates;
- **role-label bias:** treating a role assignment as current ability or performed work;
- **semio-bias:** making the pattern about records, certificates, diagrams, or publications rather than the role-state relation they describe or evidence;
- **IT-bias:** reducing role states to access-control states for software users. Software access is one case; the same ontology applies to surgery, metrology, plant operations, teams, AI agents, and organizations.

### A.2.5:8 - Conformance Checklist

| Check | Question |
| --- | --- |
| `CC-A2.5-01` | Is the current EntityOfConcern a `RoleStateRelation@BoundedContext`, not a capability, method, work occurrence, evidence episteme, status assertion, or publication form? |
| `CC-A2.5-02` | Are `RoleValueRef` and `BoundedContextRef` named or inherited? |
| `CC-A2.5-03` | Is `RoleStateSet` finite enough for the current use, with state names local to role and context? |
| `CC-A2.5-04` | Is `EnactableStateSet` explicit, including the empty-set case when the role cannot admit work? |
| `CC-A2.5-05` | Does every work-admission claim name or inherit a current `StateAssertion` window? |
| `CC-A2.5-06` | Do state predicates use observable or reviewable values, evaluations, work records, speech acts, or source relations? |
| `CC-A2.5-07` | Are state-change predicates kept separate from method order and work planning? |
| `CC-A2.5-08` | Are capability requirements governed by `A.2.2`, with method claims and work claims governed by `A.15` and A.15 subpatterns? |
| `CC-A2.5-09` | Do evidence use, status use, source use, and publication use around epistemes remain governed by their direct patterns instead of becoming work-facing role states? |
| `CC-A2.5-10` | Do role-relation hooks preserve state-sensitive role-requirement substitution, incompatibility, and bundle boundaries without product-state explosion by default? |

### A.2.5:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Assignment-as-readiness | "She is assigned as verifier, so the verification work is admitted." | Keep `U.RoleAssignment`; add `StateAssertion` for an enactable state if the work claim needs it. |
| Capability-as-role-state | "The robot is in Ready because it has the inspection capability." | Capability stays in `A.2.2`; role state predicates may refer to capability evidence only when the relation is explicit. |
| Method-order drift | State-change predicates list the tasks in a procedure. | Move ordering to method description or work plan. Keep A.2.5 to state recognition and admission. |
| Evidence-role drift | A report, standard, dataset, or model card receives a role state. | Recover evidence-use, status-use, source-use, requirement-use, or publication-use relation around the episteme. |
| Label-only incompatibility | Two role labels conflict everywhere even when one assignment is suspended or non-enactable. | Declare incompatibility over enactable states and windows where the risk actually appears. |
| Product-state explosion | A bundle role creates every combination of states across component roles. | Use separate state assertions unless a composite role with its own `RoleStateRelation@BoundedContext` is maintained. |

### A.2.5:10 - Consequences

Good consequences:

- work admission becomes reviewable without making every role assignment a large form;
- role relation structure can use current state rather than labels alone;
- role descriptions can publish state predicates without turning descriptions into states;
- evidence and status around epistemes no longer create shadow role kinds;
- cross-context role-state comparison becomes explicit rather than label-based.

Costs:

- high-consequence work needs state predicates and currentness windows;
- projects need to decide which role states actually admit work;
- role-state design can become too detailed if authors encode method order instead of admission predicates;
- cross-context reuse needs explicit mapping or comparison when state predicates differ.

#### A.2.5:10.1 - Lowering and Reopen Conditions

Lower a role-state claim or reopen A.2.5 when any of these changes:

- the role assignment, assignment window, or bounded context changes;
- the state predicates, state-change predicates, or enactable-state set change;
- a `StateAssertion` window expires, is contested, or loses the evidence or source relation that made it current;
- a method description changes its required roles or required role states;
- a capability claim changes the holder envelope needed by a state predicate;
- a role-relation structure changes role-requirement substitution, incompatibility, or bundle admission;
- an episteme previously used as evidence, source, standard, requirement, publication, or status value is reclassified by its direct pattern.

The smallest repair is normally local: update the state predicate, state assertion, window, role-relation-structure hook, or neighboring capability, method, work, evidence, or status relation that changed. Do not rewrite the whole role value or role assignment when only one role-state claim changed.

### A.2.5:11 - Rationale

FPF keeps role state separate because the surrounding values have different kinds and different failure modes. A role assignment can be valid while the role state is not work-admitting. A holder can be capable while the assignment window is stale. A method can require a role while no current holder has an enactable state. A publication can describe or evidence any of these without becoming the holder, the role, or the state.

The state-machine lens is useful because finite named states, guarded change, and state assertions are easy to inspect. But the pattern does not make every role claim executable behavior. It uses the state lens only where the project needs role-state recognition, admission, currentness, and state-aware role relation structure.

### A.2.5:12 - SoTA-Echoing

| Practice line | What A.2.5 adopts | Boundary kept |
| --- | --- | --- |
| Statecharts, SCXML, and UML state-machine practice | Finite named states, guarded transitions, and explicit state configurations are good lenses for role-state design. | A.2.5 is not an executable behavior language and does not encode method order. |
| Runtime verification over finite-state models | Windowed state assertions and observable predicates make current role claims replayable and checkable. | Verification of the larger work system stays with the pattern that owns that claim. |
| Zero-trust and dynamic access practice | Admission depends on current subject, context, source, and resource-related attributes rather than static labels. | Cybersecurity access is only one specialization; FPF keeps capability, role assignment, role state, method, and work distinct. |
| Agentic AI task-based authorization research | For AI agents, role-state admission may need task intent, tool relation, current assignment, and semantic check values. | The agentic-AI case does not turn all role-state admission into IT access control. |

### A.2.5:13 - Relations

| Related pattern | Relation |
| --- | --- |
| `A.2` | Governs the role value whose state space is being described. |
| `A.2.1` | Governs `U.RoleAssignment`, the relation referenced by `StateAssertion`. |
| `A.2.2` | Governs capability and operating envelope; role state may depend on capability evidence but does not replace capability. |
| `A.2.7` | Governs role-requirement substitution, incompatibility, and bundle expressions; A.2.5 adds state-sensitive admission when current. |
| `A.15`, `A.15.1`, `A.15.2` | Govern method, work plan, performed work, and `performedBy = U.RoleAssignment`. |
| `A.6.5` | Governs SlotSpec discipline used to keep role-state relation slots distinct. |
| `A.6.RSIR` | Recovers whether confusing source words point to role, role assignment, role state, signature, interface, slot, evidence, status, capability, method, or another governed object. |
| `A.10`, `B.3`, `C.2.1`, `C.28`, `E.17`, `F.10`, `G.6`, `E.10.D2` | Govern direct evidence-use, status-use, source-use, publication-use, assurance-use, and episteme-boundary cases that do not become role-state ontology. |
| `C.27` and temporal patterns | Govern windows, currentness, freshness, and stale-state claims when those are current. |

### A.2.5:End

