## A.2.2 - U.Capability - System Ability Envelope and Measures
> **Status:** Stable

`U.Capability` is the FPF object for "can do within bounds".

Use this pattern when a project claim says that a person, team, machine, software service, organization, composite cell, or other system can produce a kind of result, perform a class of work, or meet a performance threshold. The claim is about ability, not about who is assigned, which method is described, which work occurred, or what was promised to another party.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Capability`: a dispositional property of a `U.System` that states the system's ability to perform or produce a class of work results within a declared envelope and measured bounds.

**Primary working reader.** A manager, architect, engineer, safety assessor, scheduler, or model author who needs to decide whether a holder can be used for a work claim, method step, service promise, or architecture move without smuggling role assignment, method description, or past work into the ability claim.

**First useful move.** Ask: who is the holder system, what work family or result class is claimed, under what envelope, with what measures, during which qualification window, and by which current evidence or source-use relation?

**What goes wrong if missed.** A role label becomes a hidden proof of ability, a method description is treated as if it can perform work, a single successful run is generalized into a stable ability, or a promise is made without a measured capability behind it.

**What this buys.** Capability becomes checkable and reusable: a work-admission claim can test role assignment, role state, method requirements, and capability thresholds separately.

**Not this pattern when.**

- If the current claim is who holds a work-facing role in a bounded context, use `A.2.1`.
- If the current claim is whether that assignment is in an enactable state, use `A.2.5`.
- If the current claim is a role value, role description, role name, role relation structure, or role bundle, use `A.2`, Part F role patterns, or `A.2.7`.
- If the current claim is a way of doing, use `A.3.1`; if it is an episteme describing that way, use `A.3.2`.
- If the current claim is dated performed work or planned work, use `A.15`, `A.15.1`, or `A.15.2`.
- If the current claim is a promise to others, use the promise-content and commitment patterns.
- If the current claim is evidence, source, status, assurance, publication, or description use of an episteme, use the direct episteme-use pattern. Do not make the episteme a capability holder.

### A.2.2:1 - Problem Frame

In ordinary work, the same sentence often carries several typed values:

- "The welding robot is the welder on this line."
- "The welding robot can weld seam type W at 12 seams per minute."
- "The welding procedure says how to weld seam type W."
- "The robot welded batch B at 10:20."
- "The supplier promises 12 seams per minute."

Only the second sentence is a `U.Capability` claim. The others may be role assignment, method description, performed work, or promise content. When FPF collapses them, project reasoning becomes brittle:

1. **Role assignment becomes fake ability.** "Assigned as verifier" is treated as "able to verify".
2. **Method description becomes fake ability.** A recipe or algorithm is treated as if it can execute itself.
3. **Past work becomes fake ability.** One successful work occurrence is treated as stable capacity.
4. **Promise content becomes fake ability.** A service promise hides the real system envelope and measured bounds.
5. **Description becomes fake holder.** A standard, report, model card, or dashboard is said to "have capability" because it is useful in a capability argument.
6. **Unbounded ability becomes unreviewable.** "Can machine titanium" does not name conditions, measures, version, calibration, or currentness.

### A.2.2:2 - Kind and Boundary

`U.Capability` is a system-side ability claim.

```text
Capability:
  CapabilityHolderRef: U.System
  WorkFamilyOrResultClassRef:
  CapabilityEnvelope:
  CapabilityMeasureSet:
  QualificationWindow:
  EvidenceOrSourceUseRefs:
  CapabilityCurrentnessPredicate:
```

**CapabilityHolderRef.** The holder is a `U.System`: a physical system, cyber system, socio-technical system, organization, team, composite cell, software service as deployed system, or other acting holon admitted as system for the claim. A role assignment, method, method description, work record, episteme, publication, standard, or dashboard is not the capability holder merely because it appears in the sentence.

**WorkFamilyOrResultClassRef.** The ability is about a class of work results or a method family the holder can enact. It may refer to a `U.Method`, `U.MethodDescription`, method family, result class, or work family, but the reference does not turn the method or description into the holder.

**CapabilityEnvelope.** The envelope states the bounded conditions under which the ability is claimed: input range, environment, resources, configuration, system version, calibration state, staffing composition, access constraints, safety limits, or other current conditions.

**CapabilityMeasureSet.** The measures state the achieved or required bounds with units, scales, tolerances, success predicates, reliability, throughput, latency, precision, defect rate, or other characteristics.

**QualificationWindow.** Capability is stable enough to plan with but not timeless. A claim may depend on software version, calibration horizon, team training state, wear, operating season, regulatory state, or other temporal currentness relation.

**EvidenceOrSourceUseRefs.** Evidence, tests, certifications, prior work summaries, simulations, audit records, standards, and model results can justify a capability claim through direct evidence or source-use relations. They do not become the capability.

**CapabilityCurrentnessPredicate.** The claim states what keeps the ability current and what lowers or reopens it.

**Neighboring-term boundary.** When a neighboring pattern uses `U.WorkScope`, recover the set-valued condition part of `CapabilityEnvelope`: the inputs, environment, resources, configuration, and assumptions against which an intended work slice is checked. When it uses `U.WorkMeasures`, recover `CapabilityMeasureSet`. `JobSlice` names the intended work slice for a work-admission check. `QualificationWindow` names the temporal currentness relation for the capability claim. These are neighboring governed terms, not substitute names for `U.Capability`.



### A.2.2:3 - Positive Solution

Use `U.Capability` when the object under discussion is the holder's ability to achieve a result class within a declared envelope and measure set.

Minimal capability statement:

```text
CapabilityStatement:
  holder: U.System
  canDo: WorkFamilyOrResultClass
  envelope: CapabilityEnvelope
  measures: CapabilityMeasureSet
  qualificationWindow: QualificationWindow
  evidenceOrSourceUse: EvidenceOrSourceUseRefs
```

Plain sentence form:

```text
<System> can perform <work family or result class>
within <envelope>
at <measures>
during <qualification window>,
with <evidence or source-use relation>.
```

This form is deliberately not a method description. It does not list the step order or algorithm. It also does not assign the holder to a role or assert that a work occurrence happened.

### A.2.2:4 - Separation From Neighboring Values

| Source wording | Recovered FPF values |
|---|---|
| "Engineer role can approve the design." | `U.Role` and `U.RoleAssignment` for who may act; `U.Capability` only if the holder's ability to approve is being measured or qualified. |
| "The robot is assigned as welder." | `U.RoleAssignment`; add `U.Capability` only if the claim also says the robot can meet a welding envelope and measures. |
| "The solver has the scheduling algorithm." | `U.MethodDescription` or deployed software-system relation; `U.Capability` only for the deployed system's ability to produce schedules within bounds. |
| "The report has evidence capability." | Evidence-use relation around an episteme; no capability holder unless a system can perform evidential work. |
| "The team did one successful run." | `U.Work` occurrence; capability only after a separate ability claim with envelope, measures, and currentness. |
| "We promise five-day close." | Promise content and commitment; capability is the internal holder ability that makes the promise credible. |
| "The architecture provides resilience capability." | Architecture or structure claim plus capability claim for the relevant system or composite, with measured resilience characteristics. |

### A.2.2:5 - Work-Admission Use

A method step or work claim may require both role and capability conditions.

```text
WorkAdmissionCheck:
  roleAssignmentCurrent: A.2.1
  roleStateAdmitsWork: A.2.5
  methodStepRequires: A.3.1 or A.3.2
  holderCapabilityMeets: A.2.2
  performedWorkRecord: A.15.1 after execution
```

The checks are separate:

- role assignment says who is acting in which context;
- role state says whether that assignment is in a work-admitting state;
- method or method description says what capability threshold is required;
- capability says whether the holder can meet that threshold within the envelope and window;
- performed work says what actually happened.

Do not put the threshold into the role name. Do not treat a role assignment as proof of ability. Do not let a capability claim perform the work.

### A.2.2:6 - Worked Cases

#### A.2.2:6.1 - Manufacturing Cell

`RobotArm_A` is assigned as `WelderRole` on `AssemblyLine_2026`. That assignment alone says who is eligible to act in the line context.

The capability claim is separate:

```text
Capability:
  holder: RobotArm_A
  canDo: Weld_MIG_v3 seam family
  envelope: steel grades S235-S355, ambient 18-30 C, argon mix 92-95 percent, torch T-MIG-07
  measures: bead width 6.0 mm plus or minus 0.2 mm, throughput up to 12 seams per minute, defect rate below 0.5 percent
  qualificationWindow: calibration valid through 2026-09-30
  evidenceOrSourceUse: latest welding test report and calibration source relation
```

If a method step requires `WelderRole` and bead width tolerance below 0.2 mm, the role assignment and the capability are both checked. The assignment does not supply the tolerance, and the capability does not assign the robot to the shift.

#### A.2.2:6.2 - Software Service as Deployed System

`PlannerService_v4` is a deployed system. It may have capability to generate job-shop schedules for 50-500 jobs and 5-40 machines, with benchmark optimality above 0.95 and latency below 20 ms in `PlantScheduling_2026`.

The algorithm paper and method description are not the capability. The deployed system has the capability only while its version, dependencies, input range, and operational measurements keep the claim current.

#### A.2.2:6.3 - Organization or Team

`FinanceDept` can close books for eight legal entities under IFRS with ERP v12, staffing at or above six qualified people, and close duration below five business days. That is a capability of the organizational system.

The monthly-close service promise is a promise content claim. The actual close for March 2026 is performed work. Staff assignments and role states are neighboring role claims. The capability claim keeps the ability of the department visible and measurable.

#### A.2.2:6.4 - Episteme Anti-Case

"ISO 26262 has safety capability" is not a capability claim. The standard is an episteme used as source, requirement, or assurance input. A safety engineering team or toolchain may have a capability to perform safety-case work using that standard within a declared envelope.

### A.2.2:7 - Capability Currentness and Lowering

Lower or reopen a capability claim when any of these changes:

- the holder system changes composition, version, calibration, staffing, training state, toolchain, or environment;
- the envelope no longer covers the intended work slice;
- measures no longer meet the required threshold;
- the qualification window expires or becomes contested;
- evidence, source-use, test, audit, or simulation relations become stale or are reclassified;
- the method or method description changes the required capability threshold;
- the role assignment or role state changes, causing a work-admission claim to fail even though capability remains true;
- a composite holder changes dependency conditions.

Repair the smallest value that changed. A stale calibration window lowers the capability claim; it does not rewrite the role value. A failed role assignment lowers work admission; it does not by itself lower the holder's measured ability.

### A.2.2:8 - Composite Capability

A composite system may have a capability that none of its parts has alone. Treat the composite as the holder.

```text
Capability:
  holder: Cell_3
  canDo: place 12 PCB per minute
  envelope: feeder, vision, head, controller, and operator conditions
  measures: placement tolerance, throughput, fault rate
  qualificationWindow: current configuration and calibration window
  dependencyNotes: feeder and vision subsystem conditions
```

The capability belongs to `Cell_3`, not to every part and not to the method description. Dependencies may be named, but the whole-system capability remains a property of the composite holder.

### A.2.2:9 - Checklist

| Check | Question |
|---|---|
| `CC-A2.2-01` | Is the holder a `U.System` or acting holon admitted as system for this claim? |
| `CC-A2.2-02` | Does the capability statement name the work family or result class? |
| `CC-A2.2-03` | Does it name the envelope: inputs, environment, configuration, resources, constraints, or conditions? |
| `CC-A2.2-04` | Does it name measurable bounds with units, scales, thresholds, or predicates? |
| `CC-A2.2-05` | Does it name the qualification window or other currentness predicate? |
| `CC-A2.2-06` | Are evidence and source-use relations expressed as neighboring episteme-use values, not as capability holders? |
| `CC-A2.2-07` | Are role assignment, role state, method requirement, performed work, and promise content kept separate? |
| `CC-A2.2-08` | For work admission, are role and capability checks both visible when both are current? |
| `CC-A2.2-09` | For composite holders, is the capability stated at the whole whose ability is being claimed? |
| `CC-A2.2-10` | Are lowering and reopen conditions local enough to change only the affected value? |

### A.2.2:10 - Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Role-as-capability | "The inspector role can detect this defect." | Keep the role value and role assignment; state capability for the holder system if measured detection ability is current. |
| Assignment-as-capability | "Assigned, therefore able." | Use A.2.1 for assignment and A.2.2 for the ability claim. |
| Method-description-as-capability | "The procedure has capability." | Use `U.MethodDescription` for the episteme; use `U.Capability` for the system that can enact the method within bounds. |
| Work-as-capability | "We did it once, so we can." | Keep the work occurrence; add a separate capability claim only when envelope, measures, and currentness are justified. |
| Promise-as-capability | "The SLA is our capability." | Use promise content or commitment for what is offered; capability is the internal measured ability that makes the promise credible. |
| Episteme-as-holder | "The report has assessment capability." | Use evidence, source, status, or assessment relation for the episteme; capability holder remains a system. |
| Unbounded capability | "The tool can machine titanium." | Add material grade, tolerances, feed range, environment, version, qualification window, and measurement evidence. |
| Capability threshold in role name | `HighPrecisionWelderRole` hides a measured threshold. | Keep role name clean; put precision threshold in method requirement and holder capability. |

### A.2.2:11 - Consequences

**Benefits.**

- Planning separates "can do" from "is assigned now".
- Method steps can name capability thresholds without putting extra meaning into role names.
- Work records can be judged against the capability claim current at the time of work.
- Promise content becomes less magical because the internal ability and measured envelope are explicit.
- Composite-system ability can be stated at the right holder instead of scattered across parts.

**Costs.**

- Capability tables need envelope, measures, and currentness fields.
- Teams need to stop using role labels as shortcuts for ability.
- Some old "function", "service", "process", and "algorithm" sentences need kind recovery before they can be used in FPF.

The cost is intentional: without it, FPF cannot distinguish authorization, ability, method, and performance.

### A.2.2:12 - SoTA-Echoing

| Current practice or research line | What FPF takes | Practical implication |
|---|---|---|
| Capability-based planning in defense and enterprise architecture keeps ability, mission need, activities, systems, and portfolio planning separate. | `U.Capability` is ability with envelope and measures; it is not a role, method, work record, or promise. | A capability claim can be compared across candidate systems without selecting the implementation too early. |
| Current model-based systems engineering, including SysML v2 work, increases semantic precision and traceability between system model elements, requirements, measures, and stakeholder concerns. | Capability claims name holder, result class, envelope, measures, evidence, and currentness as separate typed values. | The reader can see which value changed when a requirement, holder, measure, or context changes. |
| Current uncertainty and verification work for cyber-physical and autonomous systems treats operating conditions and currentness as first-class modeling concerns. | Qualification windows, evidence or source-use refs, and lowering triggers are part of the capability pattern, not later paperwork. | A stale calibration, changed version, or out-of-envelope input lowers the capability claim locally. |
| Modern access-control and zero-trust practice separates subject, role or attribute relation, current state, policy decision, and resource action. | A role assignment or role state may admit a work attempt, but it does not grant capability. | "Allowed to act" and "able to achieve the measured result" remain separate checks. |

Source-currentness note: DoDAF and TOGAF are used here as stable capability-planning practice lineage, not as the full current frontier. Current pressure comes from SysML v2 and 2025-2026 MBSE work on semantic precision, uncertainty, stakeholder-context formalization, and model integration. The NIST zero-trust line is used only for the split between current authorization and measured ability.

### A.2.2:13 - Relations

| Pattern | Relation |
|---|---|
| `A.1` | Supplies holon and system grounding. |
| `A.2` | Governs `U.Role`; role values do not carry capability by label. |
| `A.2.1` | Governs `U.RoleAssignment`; assignment relation can cite a holder that separately has capability. |
| `A.2.5` | Governs role states and enactable-state admission; role state is not capability. |
| `A.2.7` | Governs role relation structure; role-requirement substitution or incompatibility does not create capability structure. |
| `A.3.1` | Governs `U.Method`; method may require capability thresholds. |
| `A.3.2` | Governs `U.MethodDescription`; a method description can describe required capability. |
| `A.3.3` | Governs `U.Dynamics`, the state-space and transition-law episteme; dynamics may explain or predict capability but is not the holder ability. |
| `A.15`, `A.15.1`, `A.15.2` | Govern method, plan, and performed work alignment; capability is one input to work admission, not work itself. |
| `A.6.5` | Supplies SlotSpec discipline for capability relation fields and capability-use relations. |
| `A.6.F` | Repairs function and functionality wording that may hide capability, method, work, math function, or functional-architecture claims. |
| `A.6.RSIR` | Recovers relation, signature, interface, role, and slot wording before capability repair when the source sentence is mixed. |
| `C.27` | Governs temporal currentness, windows, rhythm, and drift when capability timing is material. |
| `C.2.1`, `A.10`, `B.3`, `C.28`, `F.10`, `E.17` | Govern episteme, evidence, assurance, counterfactual, status, and publication-use relations that may justify or qualify a capability claim. |
| Promise-content and commitment patterns | Govern outward promise and commitment relations; a promise or commitment claim may cite a capability relation, but capability does not become promise or commitment. |

### A.2.2:14 - Excluded Objects

Do not use `U.Capability` as the current object for:

- role value, role assignment, role state, role relation structure, or role description;
- method, method family, method description, or algorithm description;
- work plan, work occurrence, run record, or measurement trace;
- evidence graph, source record, model card, standard, report, dashboard, publication, or specification-use relation;
- promise content, commitment, permission, authority relation, or policy decision;
- structural part, module, interface, port, or functional structure unless the current claim is the ability of a holder system expressed through that structure.

These values may be related to a capability claim. They do not become the capability by adjacency.

### A.2.2:End

