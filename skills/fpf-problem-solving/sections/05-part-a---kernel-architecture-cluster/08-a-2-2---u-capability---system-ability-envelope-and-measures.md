## A.2.2 - U.Capability - System Ability Envelope and Measures
> **Status:** Stable

`U.Capability` is the FPF object for "can do within bounds".

Use this pattern when a project claim says that a person, team, machine, software service, organization, composite cell, or other system can produce a kind of result, perform a class of work, or meet a performance threshold. The claim is about a holder's capability instance, not about who is assigned, which method is described, which work occurred, or what was promised to another party.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Capability`: an `E.24.UK`-admitted dependent durable U-kind name for holder-dependent capability instances. An individual `U.Capability` instance is a holder-dependent concrete governed object of a named `U.System`, recognized as that system's ability to perform a work family or produce a result class within a declared envelope, measure set, qualification window, and currentness condition. A statement, report row, certification, evidence relation, source-use relation, dashboard display, or currentness assessment about that instance is a neighboring governed record or relation, not the capability instance itself.

**Primary working reader.** A manager, architect, engineer, safety assessor, scheduler, or model author who needs to decide whether a holder can be used for a work claim, method step, service promise, or architecture move without smuggling role assignment, method description, past work, evidence, or quality wording into the capability instance.

**First useful move.** Ask: who is the holder system, what work family or result class is the ability about, under what envelope, with what declared measures, during which qualification window, and which separate statement, evidence relation, source-use relation, or currentness assessment currently supports reliance on that capability?

**What goes wrong if missed.** A role label becomes a hidden proof of ability, a method description is treated as if it can perform work, a phrase such as "the system possesses algorithm A" is taken to admit an unspecified episteme as `U.MethodDescription`, a single successful run is generalized into a stable ability, or a promise is made without a measured capability behind it.

**What this buys.** Capability becomes checkable and reusable: a work-admission claim can test role assignment, role state, method-side admission conditions, and capability thresholds separately.

**Not this pattern when.**

- If the current claim is who holds a work-facing role in a bounded context, use `A.2.1`.
- If the current claim is whether that assignment is in an enactable state, use `A.2.5`.
- If the current claim is a role value, role description, role name, role relation structure, or role bundle, use `A.2`, Part F role patterns, or `A.2.7`.
- If the current claim is a way of doing, use `A.3.1`; if it is an episteme describing that way, use `A.3.2`.
- If the current claim is dated performed work or planned work, use `A.15`, `A.15.1`, or `A.15.2`.
- If the current claim is a promise to others, use the promise-content and commitment patterns.
- If the current claim is evidence, source, status, assurance, publication, or description use of an episteme, use the direct episteme-use pattern. Do not make the episteme a capability holder.
- If the current claim is one measured aspect with a declared scale, use `U.Characteristic` through `C.16.P`, `A.19`, and the current characteristic or scale owner.
- If the current claim is a composite quality family such as availability, resilience, security, or maintainability, use `C.25` Q-Bundle.
- If the current claim is an architecture-characteristic starter head, project criteria row, architecture eval reading, or architecture-description concern, use `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, or `C.30` as applicable.

### A.2.2:1 - Problem Frame

In ordinary work, the same sentence often carries several typed values:

- "The welding robot is the welder on this line."
- "The welding robot can weld seam type W at 12 seams per minute."
- "The welding procedure says how to weld seam type W."
- "The robot welded batch B at 10:20."
- "The supplier promises 12 seams per minute."

Only the second sentence can support a `U.Capability` instance when the holder, work family, envelope, measures, and currentness conditions are recoverable. The sentence itself is a statement about the capability instance. The others may be role assignment, method description, performed work, or promise content. When FPF collapses them, project reasoning becomes brittle:

1. **Role assignment becomes fake ability.** "Assigned as verifier" is treated as "able to verify".
2. **Method description becomes fake ability.** A recipe or algorithm is treated as if it can execute itself.
3. **Past work becomes fake ability.** One successful work occurrence is treated as stable capacity.
4. **Promise content becomes fake ability.** A service promise hides the real system envelope and measured bounds.
5. **Description becomes fake holder.** A standard, report, model card, or dashboard is said to "have capability" because it is useful in a capability argument.
6. **Unbounded ability becomes unreviewable.** "Can machine titanium" does not name conditions, measures, version, calibration, or currentness.

### A.2.2:2 - Kind and Boundary

`U.Capability` is retained as a dependent durable U-kind name under `E.24.UK`. A concrete `U.Capability` instance is the holder-dependent capability instance of a named `U.System`; its identity is grounded by the holder, work family or result class, envelope, measure set, qualification window, and currentness condition. The statement that asserts the ability, the evidence that supports reliance, and the fit predicate that tests work admission are separately governed records or relations rather than the `U.Capability` instance.

```text
CapabilityUKindAdmissionDecision:
  CandidateSpelling: U.Capability
  Disposition: retained as dependent durable U-kind name
  E24Settlement: dependent capability instance under the named U.System holder settlement, governed here by A.2.2
  RootSubjectUKind: U.System holder whose ability is being stated
  DependentInstance: holder-dependent concrete U.Capability instance
  semanticArea: system ability, work admission, capability planning, and method threshold use
  ontologicalNeighborhood: U.System holder, U.RoleAssignment, U.Method, U.MethodDescription, U.WorkPlan, U.Work, U.Characteristic, Q-Bundle, architecture-characteristic row, evidence relation, source-use relation, currentness assessment, and capability-fit predicate
  IdentityGroundingOrRecognitionRule: holder plus work family or result class plus envelope plus measure set plus qualification window plus currentness condition
  admissibleUse: state or test that a named holder can perform a work family or produce a result class within declared bounds for planning, promise support, role-method-work admission, or architecture move feasibility
  nonUseBoundary: do not use U.Capability for statements, reports, evidence, source-use relations, currentness assessments, characteristics, Q-Bundles, architecture-characteristic rows, fit predicates, role assignments, method descriptions, work plans, or work occurrences
  NonUSubstitutionBoundary: statements, evidence, source-use relations, currentness assessments, Q-Bundles, characteristics, architecture-characteristic rows, and fit predicates do not become U.Capability

ConcreteCapabilityInstance:
  CapabilityHolderRef: U.System
  WorkFamilyOrResultClassRef:
  CapabilityEnvelope:
  CapabilityMeasureSet:
  QualificationWindow:
  CapabilityCurrentnessCondition:
  DependentInstancePolicy: dependent on holder identity and declared envelope/measure/window boundary

SupportAndUseReferencesAroundCapability:
  CapabilityStatementRefs?: governed episteme or publication records that describe the instance
  EvidenceRelationRefs?: governed evidence relations that support reliance
  SourceUseRelationRefs?: governed source-use relations used to justify or constrain the statement
  CurrentnessAssessmentRefs?: dated assessment relations evaluating the currentness condition
  CapabilityFitConditionRefs?: admission predicates or gate relations that test this instance for a use
```

**CapabilityHolderRef.** The holder is a `U.System`: a physical system, cyber system, socio-technical system, organization, team, composite cell, software service as deployed system, or other acting holon admitted as system for the claim. A role assignment, method, method description, work record, episteme, publication, standard, or dashboard is not the capability holder merely because it appears in the sentence.

**WorkFamilyOrResultClassRef.** The ability is about a class of work the holder system can perform or a result class it can produce. The envelope may cite the exact `U.Method` that prospective Work occurrences would enact, or a separately identified `U.MethodDescription` whose claims constrain the capability use. Those references do not turn the Method or description into the holder, do not make the holder enact the Method, and do not establish that any candidate episteme is `U.MethodDescription`.

**CapabilityEnvelope.** The envelope states the bounded conditions under which the ability holds: input range, environment, resources, configuration, system version, calibration state, staffing composition, access constraints, safety limits, or other current conditions.

**CapabilityMeasureSet.** The measures state achieved or required bounds with units, scales, tolerances, success predicates, reliability, throughput, latency, precision, defect rate, or other declared characteristics. A measure may cite a `U.Characteristic`, Q-Bundle slot, or architecture-characteristic criteria row as an input for a capability-fit check, but that characteristic, Q-Bundle, or architecture row does not become the capability.

**QualificationWindow.** Capability is stable enough to plan with but not timeless. The instance may depend on software version, calibration horizon, team training state, wear, operating season, regulatory state, or other temporal currentness relation.

**CapabilityStatementRefs.** A `CapabilityStatement` is a governed episteme or publication-side record that says a capability instance exists, describes its holder, envelope, measures, and window, or cites it for planning. It is not `U.Capability`, but it is still a governed record under its own episteme or publication pattern.

**EvidenceRelationRefs and SourceUseRelationRefs.** Evidence, tests, certifications, prior work summaries, simulations, audit records, standards, and model results can justify a capability statement through direct evidence or source-use relations. These are governed relations or records. They do not become the capability and do not become its holder.

**CurrentnessAssessmentRefs.** A currentness assessment is a dated assessment relation saying whether the capability instance remains usable under its qualification window and current conditions. It is not the capability instance, but it is still a governed assessment relation. `CapabilityCurrentnessCondition` states what must remain true; an assessment evaluates that condition.

**CapabilityFitConditionRefs.** A capability-fit condition is an admission predicate, threshold, or gate relation that tests a holder capability and any declared characteristic, Q-Bundle, or architecture-characteristic inputs against a current role, method step, work plan, work occurrence, bounded context, or gate need. It is a governed relation or predicate. Unless a separate E.24.UK admission is written, it is not a `U.*` kind.

**Neighboring-term boundary.** When a neighboring pattern uses `U.WorkScope`, recover the set-valued condition part of `CapabilityEnvelope`: the inputs, environment, resources, configuration, and assumptions against which an intended work slice is checked. When it uses `U.WorkMeasures`, recover `CapabilityMeasureSet`. `JobSlice` names the intended work slice for a work-admission check. `QualificationWindow` names the temporal currentness relation for the capability instance. These are neighboring governed terms, not substitute names for `U.Capability`.



### A.2.2:3 - Positive Solution

Use `U.Capability` when the object under discussion is the holder's ability to achieve a result class within a declared envelope and measure set.

Minimal capability instance:

```text
ConcreteCapabilityInstance:
  holder: U.System
  canDo: WorkFamilyOrResultClass
  envelope: CapabilityEnvelope
  measures: CapabilityMeasureSet
  qualificationWindow: QualificationWindow
  currentnessCondition: CapabilityCurrentnessCondition
```

Separate supporting record:

```text
CapabilityStatementRecord:
  describedCapabilityRef: ConcreteCapabilityInstance
  statementSourceRef:
  evidenceOrSourceUseRefs:
  currentnessAssessmentRefs?:
```

Plain sentence form:

```text
<System> can perform <work family or result class>
within <envelope>
at <measures>
during <qualification window>,
with <evidence or source-use relation>.
```

This sentence form is a publication or statement about the capability instance. It is deliberately not a method description. It does not list the step order or algorithm. It also does not assign the holder to a role, assert that a work occurrence happened, prove an architecture characteristic, or make the evidence relation into the capability.

### A.2.2:4 - Separation From Neighboring Values

| Source wording | Recovered FPF values |
|---|---|
| "Engineer role can approve the design." | `U.Role` for the role value and exact `U.RoleAssignment` for the admitted holder, role value, role-taxonomy episteme, effective reference scheme, and obtaining extent. Do not infer permission, capability, action, or approval Work from that wording; add `U.Capability` only for a measured and qualified ability of the holder system, and use the direct authorization and performed-work relations when those claims are current. |
| "The robot is assigned as welder." | `U.RoleAssignment`; add `U.Capability` only if the claim also says the robot can meet a welding envelope and measures. |
| "The solver has the scheduling algorithm." | First identify what the possession phrase claims: a deployed-software relation, a capability statement about the solver system, a reference to exact `U.Method`, or a candidate claim-bearing episteme. Only the last candidate enters `A.3.2`, and it is `U.MethodDescription` only when its exact `EntityOfConcern` is one admitted Method and at least one substantive claim says how that Method is done. The phrase alone establishes none of these. |
| "The report has evidence capability." | Evidence-use relation around an episteme; no capability holder unless a system can perform evidential work. |
| "The team did one successful run." | `U.Work` occurrence; capability only after a separate capability instance is established with envelope, measures, and currentness. |
| "We promise five-day close." | Promise content and commitment; capability is the holder-dependent capability instance that makes the promise credible. |
| "The architecture provides resilience capability." | Architecture-characteristic or Q-Bundle material under `C.30`, `C.32.HCS`, `C.32.ACS`, and `C.25`; add `U.Capability` only when a named holder system has a capability instance to produce or maintain a result class within a capability envelope. Resilience characteristics may constrain a capability-fit condition; they are not capability by name. |

### A.2.2:5 - Work-Admission Use

A method step or work claim may require both role and capability conditions.

```text
WorkAdmissionCheck:
  roleAssignmentCurrent: A.2.1
  roleStateAdmitsWork: A.2.5
  methodStepRequires: A.3.1 or A.3.2
  holderCapabilityRef: A.2.2
  capabilityFitCondition: admission predicate over declared capability measures and any named characteristic, Q-Bundle, or architecture-characteristic inputs
  performedWorkRecord: A.15.1 after execution
```

The checks are separate:

- role assignment identifies which admitted holder system holds which role value under the exact role-taxonomy episteme and effective reference scheme throughout its obtaining extent; it does not say that the holder is acting;
- role state says whether that assignment is in a work-admitting state;
- one exact `U.Method` supplies the method-side condition, while an independently admitted `U.MethodDescription` or work-admission episteme may state the capability threshold used by the check;
- capability names the holder system's ability within the envelope, measure set, and window;
- capability-fit condition tests whether that instance meets the current threshold or gate need;
- after execution, A.15.1 identifies the dated Work occurrence, F.6 `performedUnderAssignment(W, RA)` attributes it to the exact assignment whose holder system actually performed it, and actual `enactsMethod(W, M)` relates the Work to the exact Method.

Do not put the threshold into the role name. Do not treat a role assignment as proof of ability or action. Do not let a role value, capability instance, Method, or MethodDescription perform the work. Do not treat a fit predicate, Q-Bundle, architecture-characteristic row, evidence relation, or currentness assessment as the capability instance. An algorithm-possession phrase is only a dispatch cue; it establishes neither dated performance nor `U.MethodDescription` membership.

### A.2.2:6 - Worked Cases

#### A.2.2:6.1 - Manufacturing Cell

`RobotArm_A` is the admitted holder in one exact assignment occurrence with `WelderRole`, `FactoryProductionRoles-2026`, and `Factory-Line-B-Role-Scheme`; the assignment's actual extent follows uninterrupted obtaining for those four fixed participants. A separate work or system-locus relation may place intended or performed welding at `AssemblyLine_2026` when that relation obtains. The assignment says only that the holder system holds that role under the named taxonomy and scheme during its extent; it proves neither permission, ability, action, nor performed work.

The capability instance is separate; a statement or record may describe it:

```text
ConcreteCapabilityInstance:
  holder: RobotArm_A
  canDo: Weld_MIG_v3 seam family
  envelope: steel grades S235-S355, ambient 18-30 C, argon mix 92-95 percent, torch T-MIG-07
  measures: bead width 6.0 mm plus or minus 0.2 mm, throughput up to 12 seams per minute, defect rate below 0.5 percent
  qualificationWindow: calibration valid through 2026-09-30
  currentnessCondition: calibration and configuration remain inside the qualification window
SupportAndUseReferencesAroundCapability:
  evidenceOrSourceUse: latest welding test report and calibration source relation
```

If a method step requires `WelderRole` and bead width tolerance below 0.2 mm, the role assignment and the capability are both checked. The assignment does not supply the tolerance, and the capability does not assign the robot to the shift.

**Shared boundary case — Robot-7 possesses an inspection algorithm.** `RoleAssignment-17` has four exact participants: admitted holder system `Robot-7`, `InspectorRole`, `MaintenanceRoles-2026`, and `Maintenance-Scheme-A`; its separately described extent covers the candidate inspection interval. `Robot7-TurbineInspectionCapability-2026` is the holder-dependent capability instance for turbine-inspection work within its declared sensor, calibration, input, measure, and qualification bounds. A statement that Robot-7 "possesses inspection algorithm A" does not by itself identify that capability instance, an exact Method, a deployed-software relation, or a method-description episteme. Dispatch the phrase by claim: use A.2.2 only for the bounded ability; A.3.1 for exact `TurbineInspection@Maintenance-2026 : U.Method`; a direct deployed-software or possession relation when that is the actual claim; and A.3.2 for candidate episteme `TurbineInspectionProcedure-v3` only after its exact `EntityOfConcern` resolves to that Method and one substantive claim says how it is done.

Assignment and capability still do not prove execution. If `InspectionWork-17` actually occurs, Robot-7 is the actor and performs it under `RoleAssignment-17` through F.6 `performedUnderAssignment(InspectionWork-17, RoleAssignment-17)`; the Work occurrence separately stands in `enactsMethod(InspectionWork-17, TurbineInspection@Maintenance-2026)`. `InspectorRole`, the capability instance, the possession phrase, the Method, and `TurbineInspectionProcedure-v3` do not act or perform the inspection.

#### A.2.2:6.2 - Software Service as Deployed System

`PlannerService_v4` is a deployed system. It may have capability to generate job-shop schedules for 50-500 jobs and 5-40 machines, with benchmark optimality above 0.95 and latency below 20 ms in `PlantScheduling_2026`.

The algorithm paper and method description are not the capability. The deployed system has the capability only while its version, dependencies, input range, and operational measurements satisfy the declared currentness condition; a benchmark report or model card is support for a statement about that instance.

#### A.2.2:6.3 - Organization or Team

`FinanceDept` can close books for eight legal entities under IFRS with ERP v12, staffing at or above six qualified people, and close duration below five business days. That is a capability of the organizational system.

The monthly-close service promise is a promise content claim. The actual close for March 2026 is performed work. Staff assignments and role states are neighboring role claims. The capability instance keeps the ability of the department visible and measurable; the management report describing it is a statement about that instance.

#### A.2.2:6.4 - Episteme Anti-Case

"ISO 26262 has safety capability" is not a capability statement about a holder-dependent capability instance. The standard is an episteme used as source, requirement, or assurance input. A safety engineering team or toolchain may have a capability to perform safety-case work using that standard within a declared envelope.

### A.2.2:7 - Capability Currentness and Lowering

Lower or reopen a capability instance, or lower reliance on a statement about it, when any of these changes:

- the holder system changes composition, version, calibration, staffing, training state, toolchain, or environment;
- the envelope no longer covers the intended work slice;
- measures no longer meet the required threshold;
- the qualification window expires or becomes contested;
- evidence, source-use, test, audit, or simulation relations become stale or are reclassified, lowering the support or currentness assessment rather than becoming the capability;
- the method or method description changes the required capability threshold;
- the role assignment or role state changes, causing a work-admission claim to fail even though capability remains true;
- a composite holder changes dependency conditions.

Repair the smallest object that changed. A stale calibration window lowers the capability currentness assessment and may lower reliance on the capability instance; it does not rewrite the role value. A failed role assignment lowers work admission; it does not by itself lower the holder's measured ability. A stale report lowers a statement or evidence relation before it lowers the capability instance itself.

### A.2.2:8 - Composite Capability

A composite system may have a capability that none of its parts has alone. Treat the composite as the holder.

```text
ConcreteCapabilityInstance:
  holder: Cell_3
  canDo: place 12 PCB per minute
  envelope: feeder, vision, head, controller, and operator conditions
  measures: placement tolerance, throughput, fault rate
  qualificationWindow: current configuration and calibration window
  dependencyNotes: feeder and vision subsystem conditions
```

The concrete capability instance is asserted for `Cell_3`, not for every part and not for the method description. Dependencies may be named, but the bounded capability claim is about the composite holder.

### A.2.2:9 - Checklist

| Check | Question |
|---|---|
| `CC-A2.2-01` | Is the holder a `U.System` or acting holon admitted as system for this claim? |
| `CC-A2.2-02` | Does the capability instance name the work family or result class? |
| `CC-A2.2-03` | Does the capability instance name the envelope: inputs, environment, configuration, resources, constraints, or conditions? |
| `CC-A2.2-04` | Does the measure set bind measurable bounds to units, scales, thresholds, predicates, declared `U.Characteristic` values, Q-Bundle slots, or architecture-characteristic rows without making those inputs the capability? |
| `CC-A2.2-05` | Does the capability instance name the qualification window and currentness condition, while dated currentness assessments remain separate relations? |
| `CC-A2.2-06` | Are statements, evidence, source-use relations, certifications, reports, dashboards, and currentness assessments expressed as neighboring support records or relations, not as `U.Capability` or capability holders? |
| `CC-A2.2-07` | Are role assignment, role state, method-side admission or fit condition, performed work, and promise content kept separate? |
| `CC-A2.2-08` | For work admission, are role, capability instance, and capability-fit predicate all visible when all are current? |
| `CC-A2.2-09` | For composite holders, is the capability stated at the whole whose ability is being claimed? |
| `CC-A2.2-10` | Are lowering and reopen conditions local enough to change only the affected capability instance, statement, evidence relation, currentness assessment, or fit predicate? |
| `CC-A2.2-11` | When wording says that a holder possesses an algorithm, did the use dispatch separately to capability, exact Method, deployed-software or possession relation, or candidate episteme, and apply A.3.2's exact-Method `EntityOfConcern` plus substantive-claim threshold before admitting `U.MethodDescription`? Does only the admitted holder system perform dated Work under exact assignment while the Work separately enacts the Method? |

### A.2.2:10 - Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
|---|---|---|
| Role-as-capability | "The inspector role can detect this defect." | Keep the role value and role assignment; state capability for the holder system only when a currentness assessment supports reliance on the measured detection capability instance. |
| Assignment-as-capability | "Assigned, therefore able." | Use A.2.1 for assignment and A.2.2 for the holder-dependent capability instance. |
| Method-description-as-capability | "The procedure has capability" or "the solver has the algorithm, therefore this file is a method description." | Keep capability with the holder system. Treat procedure or algorithm wording as a cue to one candidate episteme only when that is the actual object; admit it as `U.MethodDescription` through A.3.2 only after its exact `EntityOfConcern` is an admitted Method and a substantive claim says how that Method is done. |
| Work-as-capability | "We did it once, so we can." | Keep the work occurrence; add a separate capability instance only when envelope, measures, and currentness are justified. |
| Promise-as-capability | "The SLA is our capability." | Use promise content or commitment for what is offered; capability is the internal measured ability that makes the promise credible. |
| Episteme-as-holder | "The report has assessment capability." | Use evidence, source, status, or assessment relation for the episteme; capability holder remains a system. |
| Unbounded capability | "The tool can machine titanium." | Add material grade, tolerances, feed range, environment, version, qualification window, and measurement evidence. |
| Capability threshold in role name | `HighPrecisionWelderRole` hides a measured threshold. | Keep role name clean; put the precision threshold in the method-side admission or fit condition and the holder capability instance. |
| Characteristic-as-capability | "Low latency is a capability." | Use `U.Characteristic` with declared scale for latency; add `U.Capability` only when a named holder can produce a result class within an envelope that includes the latency measure. |
| Q-Bundle-as-capability | "Resilience is our capability." | Use `C.25` for the composite quality family; cite a capability only when a currentness assessment supports reliance on a holder-dependent capability instance and a fit predicate tests the relevant bundle slot. |
| Architecture-row-as-capability | "Maintainability row gives capability." | Use `C.32.ACS` for the architecture-characteristic criteria row; it may constrain a capability-fit condition but is not `U.Capability`. |

### A.2.2:11 - Consequences

**Benefits.**

- Planning separates "can do" from "is assigned now".
- Method steps can name capability thresholds without putting extra meaning into role names.
- Work records can be judged against the capability instance and fit predicate current at the time of work.
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
| Capability-based planning in defense and enterprise architecture keeps ability, mission need, activities, systems, and portfolio planning separate. | The `U.Capability` name governs holder-dependent capability instances with envelope and measures; each instance is not a role, method, work record, promise, statement, evidence record, or quality bundle. | A capability instance can be compared across candidate systems without selecting the implementation too early. |
| Current model-based systems engineering, including SysML v2 work, increases semantic precision and traceability between system model elements, requirements, measures, and stakeholder concerns. | Capability instances name holder, result class, envelope, measures, and qualification window; statements, evidence, and currentness assessments remain separate typed values. | The reader can see which object changed when a requirement, holder, measure, source, or context changes. |
| Current uncertainty and verification work for cyber-physical and autonomous systems treats operating conditions and currentness as first-class modeling concerns. | Qualification windows and lowering triggers are part of the capability instance boundary; evidence, source-use refs, and currentness assessments support or lower reliance without becoming capability. | A stale calibration, changed version, or out-of-envelope input lowers the currentness assessment or capability instance locally. |
| Modern access-control and zero-trust practice separates subject, role relation, current state, policy decision, and resource action. | A role assignment or role state may admit a work attempt, but it does not grant capability. | "Allowed to act" and "able to achieve the measured result" remain separate checks. |

Source-currentness note: DoDAF and TOGAF are used here as stable capability-planning practice lineage, not as the full current frontier. Current pressure comes from SysML v2 and 2025-2026 MBSE work on semantic precision, uncertainty, stakeholder-context formalization, and model integration. The NIST zero-trust line is used only for the split between current authorization and measured ability.

### A.2.2:13 - Relations

| Pattern | Relation |
|---|---|
| `A.1` | Supplies holon and system grounding. |
| `A.2` | Governs `U.Role`; role values do not carry capability by label. |
| `A.2.1` | Governs `U.RoleAssignment`; assignment relation can cite a holder that separately has capability. |
| `A.2.5` | Governs role states and enactable-state admission; role state is not capability. |
| `A.2.7` | Governs role relation structure; role-admission substitution or incompatibility does not create capability structure. |
| `A.3.1` | Governs `U.Method`; method may require capability thresholds. |
| `A.3.2` | Governs membership of one already identified claim-bearing episteme in `U.MethodDescription`; algorithm, procedure, or possession wording is only a cue until the exact admitted Method `EntityOfConcern` and substantive way-of-doing claim are recovered. An admitted method description may separately state required capability. |
| `A.3.3` | Governs `U.Dynamics`, the state-space and transition-law episteme; dynamics may explain or predict capability but is not the holder-dependent capability instance. |
| `A.15`, `A.15.1`, `A.15.2` | Govern method, plan, and performed work alignment; capability is one input to work admission, not work itself. |
| `A.6.5` | Supplies SlotSpec discipline for capability relation fields and capability-use relations. |
| `A.6.F` | Repairs function and functionality wording that may hide capability, method, work, math function, or functional-architecture claims. |
| `A.6.RSIR` | Recovers relation, signature, interface, role, and slot wording before capability repair when the source sentence is mixed. |
| `C.27` | Governs temporal currentness, windows, rhythm, and drift when capability timing is material. |
| `C.2.1`, `A.10`, `B.3`, `C.28`, `F.10`, `E.17` | Govern episteme, evidence, assurance, counterfactual, status, and publication-use relations that may justify or qualify a statement or reliance use about a capability instance. |
| `C.16.P`, `A.19` | Govern characteristic, scale, and characteristic-space recovery when capability measures depend on declared measured aspects. |
| `C.25` | Governs composite quality families and Q-Bundles that may supply slots for capability-fit checks. |
| `C.30`, `C.32.HCS`, `C.32.ACS`, `C.32.ACE` | Govern architecture-characteristic material, project criteria rows, and eval readings that may constrain capability use without becoming `U.Capability`. |
| Promise-content and commitment patterns | Govern outward promise and commitment relations; a promise or commitment claim may cite a capability relation, but capability does not become promise or commitment. |

### A.2.2:14 - Excluded Objects

Do not use `U.Capability` as the current object for:

- role value, role assignment, role state, role relation structure, or role description;
- method, method family, method description, or algorithm description;
- work plan, work occurrence, run record, or measurement trace;
- evidence graph, source record, model card, standard, report, dashboard, publication, or specification-use relation;
- promise content, commitment, permission, authority relation, or policy decision;
- `U.Characteristic`, scale row, coordinate, score, metric, indicator, or threshold;
- `C.25` Q-Bundle, quality-family label, mechanism, status, or evidence slot;
- architecture-characteristic starter head, project criteria row, eval program, eval reading, selected-structure adequacy claim, or architecture-description concern;
- capability-fit predicate, gate, admission relation, or work-entry readiness record;
- structural part, module, interface, port, or functional structure unless the current claim is the ability of a holder system expressed through that structure.

These values may be related to a capability instance, a statement about it, or a fit check over it. They do not become the capability by adjacency. Name the neighboring value, record, relation, or predicate through its own governing pattern when that neighboring claim is current.

### A.2.2:End

