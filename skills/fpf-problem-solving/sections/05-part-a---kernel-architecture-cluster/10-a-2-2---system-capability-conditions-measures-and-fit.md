## A.2.2 - System Capability: Conditions, Measures and Fit
> **Status:** Stable

Capability is a System's ability to perform a work family or produce a result class under stated conditions, to a stated criterion of performance. Give attained bounds when the criterion calls for a measure.

**Use this when** planning, promising or admitting work requires a justified answer to “can this holder do what is needed here?” The holder may be a person, team, machine, deployed software System, organization or composite cell. Identify that System independently under A.1, then state its qualified ability. The claim needs no separate capability individual.

**Primary EntityOfConcern.** The holder System whose ability is being asserted. A capability statement that needs an identified account is an episteme under C.2.1; its subject is the holder, and its claims state what that holder can do. Actual ability, the assertion, its support, current qualification and fit to a receiving demand remain distinguishable.

**Working reader.** A practitioner deciding whether a holder can meet a Work, Method-step, service-promise or architecture need.

**First useful move.** What must the recipient obtain, and which part must this particular holder decide or perform? Identify the holder, its conditions of work and the evidence that it can meet the criterion with the help allowed. An existing assessment can settle that question. To assign several contributions, establish how they can be supplied together alongside work already promised. Section 2.1 distinguishes what the holder can do with help from what the helper supplies.

**What goes wrong if missed.** A practitioner may infer ability from an assignment, a MethodDescription, one successful run or a promise. An expired report can change reliance on the assessment while the holder retains its ability. Individually capable holders can depend on the same help at the same time.

**What this buys.** Planning can separate ability from its warrant and fit: change the demand without inventing a new capability, or reopen an actual ability claim when the holder's configuration changes. Independently required authority, assignment state, Method-side conditions and assurance remain separate receiving checks.

**Not this pattern when.**

- If the current claim is which admitted System is assigned to an exact local system-role kind, use `A.2.1`.
- If the current claim is whether that assignment is in an enactable state, use `A.2.5`.
- If the current claim is a local system-role kind, its classification, description, designation, exact assignment, relation structure, or bundle, use `A.2`, `A.2.1`, `F.4`, `F.18`, or `A.2.7` for that object.
- If the current claim is a way of doing, use `A.3.1`; if it is an episteme describing that way, use `A.3.2`.
- If the current claim is dated performed work or planned work, use `A.15`, `A.15.1`, or `A.15.2`.
- If the current claim is a promise to others, use the promise-content and commitment patterns.
- If the current claim is evidence, source, status, assurance, publication, or description use of an episteme, use the direct episteme-use pattern. Do not make the episteme a capability holder.
- If the current claim is one measured aspect with a declared scale, use `U.Characteristic` through `C.16.P`, `A.19`, and the applicable characteristic or Scale pattern.
- If the current claim is a composite quality family such as availability, resilience, security, or maintainability, use `C.25` Q-Bundle.
- If the current claim is an architecture-characteristic starter head, project criteria row, architecture eval reading, or architecture-description concern, use `C.32.HCS`, `C.32.ACS`, `C.32.ACE`, or `C.30` as applicable.

### A.2.2:1 - Problem Frame

These ordinary sentences make different claims about welding:

- "The welding robot is the welder on this line."
- "The welding robot can weld seam type W at 12 seams per minute."
- "The welding procedure says how to weld seam type W."
- "The robot welded batch B at 10:20."
- "The supplier promises 12 seams per minute."

Only the second sentence asserts the robot's ability. Its holder, work family, conditions and measure bounds must be recoverable before the claim can be compared with a demand. The assertion still needs support for the receiving use. The others may state a local system-role assignment, MethodDescription, performed Work, or promise content. When FPF collapses them, project reasoning becomes brittle:

1. **System-role assignment becomes fake ability.** “Assigned as verifier” is treated as “able to verify”.
2. **Method description becomes fake ability.** A recipe or algorithm is treated as sufficient evidence of the holder's ability.
3. **Past work becomes fake ability.** One successful work occurrence is treated as stable capacity.
4. **Promise content becomes fake ability.** A service promise hides the real system envelope and measured bounds.
5. **Description becomes fake holder.** A standard, report, model card, or dashboard is said to "have capability" because it is useful in a capability argument.
6. **Unbounded ability becomes unreviewable.** "Can machine titanium" does not name conditions, measures, version, calibration, or currentness.

### A.2.2:2 - Qualified Ability and Its Use Basis

The positive claim is that a named holder can perform the named work or produce the named result under the stated conditions and declared criterion of performance. If its truth depends on time, include that time in the claim. A reference to the holder identifies its subject; the other values qualify the proposition rather than identify another individual.

Use these values when the receiving comparison needs them:

| Value | Contribution |
|---|---|
| `capabilityHolderRef` | The independently admitted `U.System` whose ability is claimed. |
| `WorkFamilyOrResultClassRef` | What the holder can do or produce. A particular Method or independently admitted MethodDescription may constrain this claim when the use requires it. |
| `CapabilityEnvelope` | The inputs, environment, resources, configuration, version, calibration state, staffing and other conditions under which the ability is claimed. Its set-valued work-condition basis is `U.WorkScope` under A.2.6. |
| `CapabilityMeasureSet` | The claimed attainment on the criteria used for the holder. Give the success predicate or grade and, for a quantitative criterion, the bounds, units, scale and tolerances. Compare this with the performance the recipient requires. A Characteristic, Q-Bundle slot or architecture criterion can supply a measure. |
| Capability statement | An assertion of that proposition; use a C.2.1 episteme when the account itself needs identity. Recording it does not make it true. |
| Evidence and source-use relations | The tests, prior work, simulations, standards or other sources that warrant the assertion or constrain its use under their direct governors. |
| Qualification policy and currentness assessment | The rule for relying on that support now, and its dated assessment. A qualification window may expire while actual ability remains unchanged. |
| Capability-fit predicate | The comparison of the required conditions and performance criterion with the qualified claim about this holder. This is distinct from the ability proposition and its support. |

WorkScope describes work conditions, even when an episteme states them. That episteme's ClaimScope concerns its claims; the two scopes do not become interchangeable. Quantitative bounds and qualification policy remain separate from WorkScope membership. A time condition belongs in WorkScope only when it changes which work slices are covered; an evidence-age rule belongs in qualification.

These distinctions permit ordinary capability use without `U.Capability` as an additional kind. A separate kind question arises only if a concrete receiving use needs another individual's continuity or a useful stable classification beyond the holder and these claims; E.24.UK then requires that question's identity and membership facts.

#### A.2.2:2.1 - Method-relative capability: the structure the holder can use

Use this more detailed comparison when a person, machine or composite can produce part of a result, yet it is unclear which operation, distinction or connection of the Method it can use. A correct explanation, a supplied decision and successful execution with help can support different claims. Keep the ordinary ability-and-fit answer in :3 when it already settles the receiving question.

Select the Method organization that can change the decision: its consequential operations, distinctions, conditions and joins. Include recognizing when to select the Method, adapting it or composing it with another Method only when the promised contribution requires that. Choose a grain at which a missing relation changes the next action. Separate success at individual operations from success at their coordination.

**Usable Method structure** is the aspect of which selected operations and relations a specified System can bring to bear in named work under stated conditions. As an A.17 relational characteristic it has the ordered bearers `(holder System, Method)`, arity two. The selected structure and granularity, work family, success criteria, relevant time/configuration, ordinary tools, supplied help, execution budget and observation horizon qualify that comparison. A MethodDescription can supply the account or evidence; it does not replace the Method in this pair.

A **Method-relative capability profile** expresses the qualified ability claims at that grain. It can be ordinary prose: identify the supported contribution, the help that supplied another contribution, and the unresolved or contradicted claim. It is an account about the holder, not another capability individual. An unobserved operation remains unresolved rather than becoming zero ability. A successful trial grounds only the capability inference warranted by its conditions and evidence.

Compare profiles only on a compatible selection and conditions. If one covers another's supported organization and adds a consequential relation, it has greater supported structural coverage. Different strengths can remain incomparable. A count or fraction needs a fixed structural unit, denominator and inference rule; separately acquired actions do not add up to an acquired join. Use A.17/A.18 and C.16 for a declared scale or measurement. The resulting coverage is distinct from task value, a universal mastery rank or a bit estimate.

Make assistance part of the claim. If a specialist selects the right variant and the holder executes it, the occurrence does not yet support the holder's selection capability. Removing that specialist changes the tested conditions. Keep tools and references that the receiving work ordinarily provides. If the capable whole is an equipped System or ensemble, state the claim about that whole rather than distributing it to every participant.

Current usable structure says what the holder can do now. **Acquired structure** adds a history claim, requiring comparable before/after capability accounts; attribution to a particular intervention needs its own grounds. **Obtainable through learning** concerns a starting holder and a specified acquisition arrangement, including how later learning actions are chosen. Use E.23.CDI for that construction and E.23.CAE when access, expression or changed conditions remain plausible explanations of the observed difference. Those questions do not add an acquisition arrangement as a third bearer of the current characteristic.

### A.2.2:3 - Positive Solution

1. **Identify the required work and whose ability matters.** Start with the proposed or required result for each recipient. Include any work already promised. Which operations, decisions or performances are entrusted to a particular holder? Which may be supplied by someone else? An organized team or a configured machine can be the holder when the required result depends on its parts working together. A claim about what one participant can do needs grounds for that participant's own part.
2. **State the qualified ability.** Name the work family, the criterion the holder meets and the configuration, tools, assistance and other conditions on which this depends. Use :2.1 if it matters who chose the Method or adapted it. A holder can carry out a decision supplied by a helper. Entrusting the decision itself to that holder requires grounds for its ability to choose.
3. **Recover sufficient grounds for this use.** Comparable earlier work, an applicable qualification, or an argument from how the System is organized may already establish what the holder can do. Check its relevance to the required action and the help that will actually be available. A first assignment under permitted supervision can be justified on those terms. Apply the receiving use's evidence and currency requirements. Preserve uncertainty when it could change the result.
4. **Compare the claim with the demand.** Use A.2.6 to test whether the declared WorkScope covers the proposed `JobSlice` and whether the holder meets the required performance criterion there. Apply any required units, bounds, translations and qualification policy. If the commission ends with this assessment, return the supported fit, the mismatch or the specific question still open.
5. **Establish what can be assigned together.** Recover the terms for the whole service. A result made once can serve several recipients if each can obtain it in time and the terms permit reuse. Separate performances, independent judgements or continuous coverage require their own provision. If the terms specify a minimum number or share, use the specified population, period and counting rule and preserve any promises to named recipients. A justified bound can settle the threshold.
6. **Test the arrangement against the conditions the promise covers.** Include existing obligations, shared help and other resources when the same means could be needed more than once. Who may allocate them, what will each decision maker know at the moment of choice, and can the required actions still finish in time? One feasible allocation can settle a choice entrusted to the planner. For a guarantee, establish that the same arrangement covers all combinations of demand, input conditions and availability allowed by the terms, including choices the recipients retain. Use the dependencies that make combinations possible. The arrangement may fix the allocation or choose later from information then available. If two situations are indistinguishable at an irreversible choice, the action taken then must work in both, possibly with different later actions. A risk allowance calls for grounds for the specified risk over its stated population and horizon. Use C.32.MWA.PP:4.7 to construct and compare arrangements when that work is needed.
7. **Return the decision its grounds warrant.** Identify the work the authorized party can assign now, or the conditions on which a later assignment depends. An allowed combination that defeats the proposed arrangement refutes its guarantee. To rule out every permitted arrangement, give grounds covering those alternatives. A shortage of shared provision can leave each holder's qualified ability intact. Use :5 for role, authority and admission, and A.15.1 for a claim about work that actually took place.

One possible statement-and-use record is shown below. It is a way to preserve the claims needed by this use, not a mandatory new entity or classification.

```text
CapabilityStatementRecord:
  capabilityHolderRef: U.System
  canDo: WorkFamilyOrResultClass
  workConditionBasis: U.WorkScope
  supportedPerformance: result criterion or grade met
  attainedMeasureBounds?:

  actualTimeOrConfiguration?:
  capabilityStatementRef?: C.2.1 episteme
  evidenceOrSourceUseRefs:
  qualificationPolicy:
  currentnessAssessmentRefs?:

CapabilityFitCheck:
  holderAbilityClaim: the qualified proposition above
  receivingJobSlice:
  requiredPerformance: receiving criterion
  requiredMeasureBounds?:

  evaluationTime:
  scopeCoverage:
  criterionSatisfied:
  measureComparison?:

  qualificationResult:
  result: fit, mismatch, or named unresolved premise
```

The record separates what is claimed about the System from the grounds for believing it and from what another use demands. The same supported ability may fit one demand and fail another.

### A.2.2:4 - Separation From Neighboring Values

| Source wording | Recovered FPF values |
|---|---|
| “Engineer role can approve the design.” | Treat bare *role* as an E.10.ROLE trigger. If it means classification, recover local kind `EngineerSystemRole` and a C.3.2 judgment for an admitted System. If assignment identity matters, name the assignment occurrence and its declared `U.SystemRoleAssignment` species. Do not infer permission, capability, action, responsibility, or approval Work from either claim; add a capability claim only for the ability of the holder System to meet the stated criterion under the qualified conditions, and use the permission and performed-Work relations when those claims are made. |
| “The robot is assigned as welder.” | Name an assignment occurrence with the robot as holder and its declared `U.SystemRoleAssignment` species, whose assigned-kind position has local domain `WelderSystemRoleKindDomain`; the occurrence supplies `WelderSystemRole` as the value admitted by that domain. Add a capability claim only if the claim also says that the robot can meet a welding envelope and measures. |
| "The solver has the scheduling algorithm." | First identify what the possession phrase claims: a deployed-software relation, a capability statement about the solver system, a reference to a `U.Method`, or a candidate claim-bearing episteme. Apply `A.3.2` only to the last candidate; it is `U.MethodDescription` only when its exact `EntityOfConcern` is one admitted Method and at least one substantive claim says how that Method is done. The phrase alone establishes none of these. |
| "The report has evidence capability." | Recover the report's evidence-use relation. A separate capability claim needs a system that can perform evidential work. |
| "The team did one successful run." | `U.Work` occurrence; a broader capability claim needs grounds for the required performance under the proposed conditions. |
| "We promise five-day close." | Promise content and commitment; the provider's qualified ability and its fit to the promised result need separate support. |
| "The architecture provides resilience capability." | Architecture-characteristic or Q-Bundle material under `C.30`, `C.32.HCS`, `C.32.ACS`, and `C.25`; add a capability claim only when it states a named holder System's ability to produce or maintain a result class within declared conditions and bounds. Resilience characteristics may constrain a capability-fit condition; they are not capability by name. |

### A.2.2:5 - Work-Admission Use

A Method step or a proposed performance can require an exact system-role assignment as well as a qualified ability. Decide which authority is needed to allocate work today and when each holder's assignment and state must obtain for performance. A.2.1 and A.2.5 govern those facts. When different local role kinds must be filled together, apply the holder rule in A.2.7:4.5. When the same kind is needed for several performances, use the required performances, times and allowed substitutions. A.15.2 can express that plan and its shared means. A personnel recommendation can finish an assessment commission. An appointment takes effect under the rule and authority that establish it.

```text
WorkAdmissionCheck:
  systemRoleAssignmentCurrent: A.2.1 direct species under U.SystemRoleAssignment
  systemRoleAssignmentStateAdmitsWork: A.2.5
  methodStepRequires: A.3.1 or A.3.2
  holderAbilityClaim: A.2.2 qualified claim about the assignment holder
  capabilityFitCondition: admission predicate on the required performance and any declared measure, characteristic, Q-Bundle or architecture criterion the decision uses
  performedWorkRef?: A.15.1, only for a separately asserted dated Work occurrence
```

The checks are separate:

- one `U.SystemRoleAssignment` species defines the holder and assigned-kind participant meanings, the local system-role-kind domain, and any other participant meaning that changes the assignment predicate or occurrence identity; an occurrence supplies the holder System and other values for the case, and neither species nor occurrence establishes capability or Work;
- `SystemRoleAssignmentStateRelation` says whether that assignment satisfies the selected state predicate over the required window;
- one exact `U.Method` supplies the method-side condition, while an independently admitted `U.MethodDescription` or work-admission episteme may state the capability threshold used by the check;
- the ability claim states the result the holder can achieve under the declared conditions and to what standard;
- the capability-fit condition compares that qualified claim with the work conditions and the criterion the recipient requires;
- after execution, A.13 first recovers the actual performer and A.15.1 independently admits the dated Work occurrence.

  F.6 `performedUnderAssignment(W, RA)` is added only when this capability account or its receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment, while actual `enactsMethod(W, M)` separately relates the Work to the exact Method.

Do not put the threshold into the local system-role-kind name.

### A.2.2:6 - Worked Cases

#### A.2.2:6.1 - Manufacturing Cell

This constructed example states the robot's ability separately from its assignment:

```text
CapabilityStatement:
  holder: RobotArm_A
  canDo: Weld_MIG_v3 seam family
  envelope: steel grades S235-S355, ambient 18-30 C, argon mix 92-95 percent, torch T-MIG-07
  measures: bead width 6.0 mm plus or minus 0.2 mm, throughput up to 12 seams per minute, defect rate below 0.5 percent
  qualificationWindow: calibration valid through 2026-09-30
  qualificationPolicy: rely on the test and calibration support only within its declared validity
  actualCondition: the robot configuration and calibration state satisfy the claimed envelope
SupportAndUseBasis:
  evidenceOrSourceUse: latest welding test report and calibration source relation
```

`WeldingShiftAssignment` is a declared species under `U.SystemRoleAssignment`. Under A.2.1 its signature defines the holder and assigned-kind participant meanings and uses `WelderSystemRoleKindDomain` as the local assigned-kind domain; it adds another participant only if that participant changes the assignment predicate or occurrence identity. One occurrence has `RobotArm_A` as holder, `WelderSystemRole` as the assigned-kind value admitted by that domain, and an extent lasting while the predicate obtains without interruption for the same participants.

The assertion has exact claim content, EntityOfConcern, and effective ReferenceScheme; a ClaimScope, selected slice, interval, or qualification window is stated separately when it changes interpretation or validity. None of those values is another assignment participant. A separate Work or system-locus relation may place intended or performed welding at `AssemblyLine_2026` when that relation obtains.

If a Method step requires an obtaining `WeldingShiftAssignment` whose local kind is `WelderSystemRole` and bead-width tolerance below 0.2 mm, the assignment and capability are both checked. The declared ±0.2 mm bound does not establish the stricter tolerance, so this capability statement alone cannot support admission of the step.

**Shared boundary case — Robot-7 possesses an inspection algorithm.** `InspectionReleaseAssignment` is a declared species under `U.SystemRoleAssignment`; under A.2.1 its signature defines the holder and assigned-kind participant meanings and uses `InspectorSystemRoleKindDomain` as the local assigned-kind domain. Occurrence `InspectionAssignment-17` has `Robot-7` as holder and `InspectorSystemRole` as the assigned-kind value admitted by that domain. This simple species declares no taxonomy, reference-scheme, generic-context, or interval participant. An assertion about the occurrence may cite `MaintenanceRoles-2026`, `Maintenance-Scheme-A`, and the candidate inspection interval as interpretation and description content.

`Robot7-TurbineInspectionStatement-2026` is an assertion about `Robot-7`: that System can perform turbine-inspection Work within the stated sensor, calibration, input and measure bounds. Qualification governs current reliance on its support. A statement that Robot-7 “possesses inspection algorithm A” does not by itself identify that capability claim, Method `TurbineInspection@Maintenance-2026`, a deployed-software relation, or a MethodDescription episteme.

Dispatch the phrase by claim: use A.2.2 only for the bounded ability; A.3.1 for the Method; a deployed-software or possession relation when that is the claim; and A.3.2 for candidate episteme `TurbineInspectionProcedure-v3` only after its `EntityOfConcern` resolves to that Method and one substantive claim says how it is done.

Assignment and capability still do not prove execution. If `InspectionWork-17` occurs, A.13 first recovers `Robot-7` as the actual performer through obtaining `InspectionAssignment-17`, and A.15.1 independently admits the Work.

Because this example expressly states assignment-bound attribution, F.6 afterward establishes `performedUnderAssignment(InspectionWork-17, InspectionAssignment-17)` through that same assignment; F.6 identifies neither assignment nor performer, and failed attribution leaves the Work intact. The Work occurrence separately stands in `enactsMethod(InspectionWork-17, TurbineInspection@Maintenance-2026)`.

#### A.2.2:6.2 - Software Service as Deployed System

`PlannerService_v4` is a deployed System. In this constructed example, its claimed ability is to return feasible job-shop schedules for 50–500 jobs and 5–40 machines in less than 20 ms in `PlantScheduling_2026`, with makespan at most `1.05 × L_ref`. Makespan is the elapsed time from the common start to the last job completion; `L_ref > 0` is the makespan of the declared feasible reference schedule for the same instance. With `L_ref = 100 min`, 104 min passes this quality bound and 106 min fails. The reference is a comparison baseline, not a proved optimum.

The deployed System is the holder; the algorithm paper and MethodDescription are descriptions. Version, dependencies and input range qualify the ability claim. Measurements can support that claim, and their age can limit current reliance without itself changing the System's ability.

#### A.2.2:6.3 - Organization or Team

`FinanceDept` can close books for eight legal entities under IFRS with ERP v12, staffing at or above six qualified people, and close duration below five business days. That is a capability of the organizational system.

The monthly-close service promise is a promise-content claim. The actual close for March 2026 is performed Work. Staff assignments and their `SystemRoleAssignmentStateRelation` occurrences are neighboring claims. The capability statement keeps the department's ability measurable; a management report asserting it is an episteme about the department.

Suppose two divisions ask the department to close eight separate entities each in the same five-day period. Its established ability covers eight. If both requests are allowed to fall due together, accepting each on that basis leaves the promise of sixteen open. If the documented ability covers any permitted mix of up to eight, a binding common limit of eight can make a joint promise possible. The allocation must follow an authorized rule and reach the department in time to act. Its staff must be available under the conditions of the assessment. If the evidence covers only the original eight entities, coverage of a different mix remains open. If the divisions instead need copies of the same close for the same eight entities, one close can serve both once the terms permit reuse and each can receive its copy by its deadline.

#### A.2.2:6.4 - Episteme Anti-Case

"ISO 26262 has safety capability" is not an ability claim about a holder System. The standard is an episteme used as source, requirement, or assurance input. A safety engineering team or toolchain may have a capability to perform safety-case work using that standard within a declared envelope.

#### A.2.2:6.5 - A recovered rule and a usable transition

Consider a constructed rhythmic case with eight pulses and audible attacks at pulses 0, 3 and 6. One Method alternates left and right on audible attacks; another alternates on every pulse, including silent ones. Both yield L,R,L in the first cycle. In the next cycle, attack-wise alternation yields R,L,R, while pulse-wise alternation yields L,R,L again. The first cycle therefore cannot distinguish control of these two state-update rules.

Suppose a performer draws both traces correctly and performs the second rule while following a teacher, but reverts to attack-wise alternation without that demonstration. The comparison preserves the correct explanation as a recovery result. Its capability conclusion concerns execution with the demonstration; independent control of the silent-pulse transition remains unsupported. A pulse reference may remain if the receiving performance normally provides it.

If the receiving work still needs a way to obtain correct execution of the pulse-wise rule, use E.23.CDI to decide how to develop the holder's ability, supply the missing contribution through another arrangement, or combine the two.

A digital controller can be compared on the same selected relation using its input/output traces, but that comparison supplies neither a human learning mechanism nor evidence that either holder acquired the rule through training.

### A.2.2:7 - Reconsider the Claim, Its Support or Its Fit

Reopen the value whose governing conditions changed. A different holder changes the subject. Configuration, calibration, wear, staffing, training or environment may change actual ability; evidence and qualification affect warranted reliance; the receiving demand affects fit. Assignment state and authority can separately defeat Work admission while ability remains.

The following constructed cases keep those changes apart:

| Change | Result |
|---|---|
| A new test supports the same measured performance under the same conditions. | Support changes; no changed ability is inferred. |
| A holder has supported throughput 10 units/min; demand rises from 8 to 12 under the same conditions. | The earlier demand fits that bound and the later demand does not. The holder's ability claim is unchanged. |
| Recalibration or configuration changes what precision the holder can attain while its old report remains. | Actual ability may change; reassess the predicate and the report's applicability. Unchanged paperwork does not fix the truth. |
| A fault makes the named ability predicate false at t1; repair restores it at t2. | State loss and recovery for the same holder under those times and conditions. No capability-individual continuity decision is needed. |
| RobotArm_A is replaced by RobotArm_B. | The assertion has a different subject; support for A does not automatically establish B's ability. |

A qualification window expiring may require new support or narrower reliance. An input outside the declared WorkScope defeats this fit basis. A changed Method can change the required bounds without changing the holder. A development intervention may be performed while its target remains unmet; a later successful comparison alone does not establish which intervention caused improvement. Use E.23.CDI and E.23.CAE for those development and attribution questions.

### A.2.2:8 - Composite Capability

A composite system may have a capability that none of its parts has alone. Treat the composite as the holder.

```text
CapabilityStatement:
  holder: Cell_3
  canDo: place 12 PCB per minute
  envelope: feeder, vision, head, controller, and operator conditions
  measures: placement tolerance, throughput, fault rate
  actualCondition: the claimed component configuration and calibration state
  qualificationPolicy: rely on the supporting assessment only within its declared validity
  dependencyNotes: feeder and vision subsystem conditions
```

The claim is about `Cell_3`. Justify its attained bounds under the stated component and coordination conditions; component claims alone do not establish the composite's ability. A changed dependency can reopen that claim even while each component retains its own qualified ability.

### A.2.2:9 - Checklist

| Check | Question |
|---|---|
| `CC-A2.2-01` | Is the holder an admitted `U.System` under A.1 for this claim? |
| `CC-A2.2-02` | Does the capability claim name the work family or result class? |
| `CC-A2.2-03` | Does the capability claim name the envelope: inputs, environment, configuration, resources, constraints, or conditions? |
| `CC-A2.2-04` | Does the comparison apply the required performance criterion? Where the criterion is quantitative, are attained bounds, units and scale recoverable from the appropriate measure or characteristic? |
| `CC-A2.2-05` | Are the claim's actual time and conditions distinguished from its qualification policy, support window and dated currentness assessment? |
| `CC-A2.2-06` | Are statements, evidence, source-use relations, certifications, reports, dashboards, and currentness assessments expressed as neighboring support records or relations, without treating the records as holders or their existence as proof of ability? |
| `CC-A2.2-07` | Are the exact system-role assignment, `SystemRoleAssignmentStateRelation`, Method-side admission or fit condition, performed Work, and promise content kept separate? |
| `CC-A2.2-08` | For Work admission, are the exact system-role assignment, capability claim, and capability-fit predicate all visible when all are current? |
| `CC-A2.2-09` | For composite holders, is the capability stated at the whole whose ability is being claimed? |
| `CC-A2.2-10` | When conditions change, is it clear which ability proposition, assertion, evidence relation, currentness assessment or fit predicate needs reconsideration? |
| `CC-A2.2-11` | When wording says that a holder possesses an algorithm, did the use dispatch separately to capability, exact Method, deployed-software or possession relation, or candidate episteme, and apply A.3.2's exact-Method `EntityOfConcern` plus substantive-claim threshold before admitting `U.MethodDescription`? For a dated Work claim, are the actual performer and Work independently established through A.13 and A.15.1, with F.6 added only when precise assignment-bound attribution is needed and Method enactment kept separate? |
| `CC-A2.2-12` | When a Method-relative profile is used, are the selected Method relations, holder, help, comparison conditions and supported claims explicit, with unresolved evidence and acquisition history kept distinct from current ability? |
| `CC-A2.2-13` | When work is entrusted to one or several holders, what do the grounds for each one's capability establish about the result due to the recipients under the permitted choices, help and obligations? |

### A.2.2:10 - Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
|---|---|---|
| System-role-kind-as-capability | “The inspector role can detect this defect.” | Treat bare *role* through E.10.ROLE; retain the exact local system-role kind and any independently obtaining assignment, then state capability for the holder System only when the bounded capability claim and current support justify it. |
| Assignment-as-capability | "Assigned, therefore able." | Use A.2.1 for assignment and A.2.2 for the qualified holder ability. |
| Capability attributed to a procedure | "The procedure has capability" | Keep capability with the holder system. |
| Unjustified `U.MethodDescription` admission | Treating "the solver has the algorithm" as sufficient for `U.MethodDescription` admission. | Treat procedure or algorithm wording as a cue to one candidate episteme only when that is the object; admit it as `U.MethodDescription` through A.3.2 only after its exact `EntityOfConcern` is an admitted Method and a substantive claim says how that Method is done. |
| Work-as-capability | "We did it once, so we can." | Record the work occurrence. For a capability claim, establish what the holder can deliver, with which help and under which conditions, using grounds applicable to this work. |
| Promise-as-capability | "The SLA is our capability." | Recover what was promised. Establish the holder’s ability separately, then check how the proposed arrangement can supply the promised work. |
| Episteme-as-holder | "The report has assessment capability." | Use evidence, source, status, or assessment relation for the episteme; capability holder remains a system. |
| Unbounded capability | "The tool can machine titanium." | State the material grade and performance bounds needed by the receiving use, with the operating conditions and qualification basis that support them. |
| Capability threshold in system-role-kind name | `HighPrecisionWelderSystemRole` hides a measured threshold. | Keep the system-role-kind name free of the threshold; put precision in the Method-side admission or fit condition and the holder capability claim. |
| Characteristic-as-capability | "Low latency is a capability." | Use `U.Characteristic` with declared scale for latency; add a capability claim only when a named holder can produce a result class within an envelope that includes the latency measure. |
| Q-Bundle-as-capability | "Resilience is our capability." | Use `C.25` for the quality family. If a capability is claimed, state what the holder can maintain or produce under specified conditions and bounds; use a relevant bundle slot in the fit comparison when the receiving demand calls for it. |
| Architecture-row-as-capability | "Maintainability row gives capability." | Use `C.32.ACS` for the architecture-characteristic criteria row; it may constrain a capability-fit condition but does not establish the holder's ability. |

### A.2.2:11 - Consequences

**Benefits.**

- Planning separates "can do" from "is assigned now".
- Method steps can name capability thresholds without putting extra meaning into system-role-kind names.
- Work records can be judged against the capability claim and fit predicate current at the time of work.
- The holder, operating conditions and grounds for each contribution to the promise are explicit.
- Composite-system ability can be stated at the right holder instead of scattered across parts.

**Costs.**

- A relied-on ability claim must make its operating conditions, supported performance and qualification basis recoverable, including attained bounds for a quantitative criterion.
- Teams need to stop using system-role labels or assignments as shortcuts for ability.
- Some old "function", "service", "process", and "algorithm" sentences need kind recovery before they can be used in FPF.

These distinctions let practitioners check authorization, ability, method, and performance separately.

### A.2.2:12 - SoTA-Echoing

**Practice question.** When can measured performance support a new job, and which change calls for reconsidering the holder's ability, the qualification of its assertion, or its fit to that job?

For repeatable production, the strongest answer in this comparison is to retain a condition-bound description of performance and compare it with the receiving specification. The NIST/SEMATECH *e-Handbook of Statistical Methods*, [§3.4.5](https://www.itl.nist.gov/div898/handbook/ppc/section4/ppc45.htm), requires stability before this process-capability use. Its [§6.1.6](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc16.htm) compares specification limits with the process distribution, distinguishes spread-only `Cp` from centering-sensitive `Cpk`, and treats estimation uncertainty and non-normal data separately. These sections supply the substantive practice answer and its limits, not an FPF classification of a capability holder.

An alternative is a `Cp` width screen: it usefully answers whether the process spread could fit the tolerance if centered. For an actual job, however, the same available mean, spread and limits permit a `Cpk` comparison without another production run. Retaining the mean removes the extra centering assumption. **Adopt** that condition-sensitive comparison; **reject** a spread-only score as sufficient evidence of actual fit when centering is unresolved. This choice costs one additional comparison, while preserving the width screen's useful information.

In a constructed drilling case, take a stable normal diameter distribution with known mean `10.04 mm` and standard deviation `0.02 mm`, and demand `9.90–10.10 mm`. Then `Cp = 1.67`, but `Cpk = 1.00`. A local rule requiring an index of at least `1.33` therefore gives different answers: the width screen passes, while the centering-sensitive fit fails. The threshold is this example's demand, not a universal NIST rule. Real sample estimates would also need the uncertainty treatment required by that rule.

**Adapt** this separation in §§2–3: state the holder's attained performance and conditions, retain its support, and compare the particular demand separately. Tightening the diameter tolerance changes fit without physically changing the drill. Changed calibration can change attained performance; an expired qualification assessment instead changes warranted reliance. Those differences determine which §7 question to reopen. This adaptation does not impose normal distributions, statistical stability or capability indices on every human, software or organizational ability.

Reopen this selection when instability or a changed distribution defeats the retained measurement model, when the decision needs a different loss or uncertainty criterion, or when a rival method distinguishes the same relevant failures with less required evidence. A changed job specification alone calls for a new fit comparison, not a new ability claim or a new method survey.

### A.2.2:13 - Relations

| Pattern | Relation |
|---|---|
| `A.1` | Supplies holon and system grounding. |
| `A.2` | Use for exact local system-role kinds and C.3.2 classification judgments; neither carries capability by label. |
| `A.2.1` | Use for directly declared species under `U.SystemRoleAssignment`; an assignment's holder System may separately have capability. |
| `A.2.5` | Use for `SystemRoleAssignmentStateRelation` and Work-admitting state conditions; assignment state is not capability. |
| `A.2.7` | Use for `SystemRoleKindRelationStructure`; admission substitution or incompatibility among system-role kinds does not create capability. |
| `A.3.1` | Governs `U.Method`; method may require capability thresholds. |
| `A.3.2` | Governs membership of one already identified claim-bearing episteme in `U.MethodDescription`; algorithm, procedure, or possession wording is only a cue until the exact admitted Method `EntityOfConcern` and substantive way-of-doing claim are recovered. An admitted method description may separately state required capability. |
| `A.3.3` | Governs `U.Dynamics`, the state-space and transition-law episteme; dynamics may explain or predict capability but is not the qualified holder ability. |
| `A.15`, `A.15.1`, `A.15.2` | Govern method, plan, and performed work alignment; capability is one input to work admission, not work itself. |
| `A.6.5` | Governs SlotSpecs when an independently needed relation declaration is current; the capability statement can remain ordinary prose. |
| `A.6.F` | Repairs function and functionality wording that may hide capability, method, work, math function, or functional-architecture claims. |
| `A.6.RSIR` | Use it to recover relation, signature, interface, system-role, participation, declaration-position, and slot wording before capability repair when the source sentence is mixed; use E.10.ROLE to select the branch for bare *role*. |
| `C.27.TA`, `C.27` | Use C.27.TA when a positive temporal aspect of capability—currentness, window, rhythm, or drift—is itself relied on; use C.27 for temporal-claim adequacy. |
| `C.2.1`, `A.10`, `B.3`, `C.28`, `F.10`, `E.17` | Govern episteme, evidence, assurance, counterfactual, status, and publication-use relations that may justify or qualify a statement or reliance use about a capability claim. |
| `C.16.P`, `A.19` | Govern characteristic, scale, and characteristic-space recovery when capability measures depend on declared measured aspects. |
| `A.17`, `A.18`, `C.16` | Govern the relational characteristic, a declared coverage scale and an actual measurement of usable Method structure in :2.1. |
| `C.2.8` | Governs structure recoverable from an expressed account; that recovery can inform a Method-relative profile without establishing enactment capability. |
| `E.23.CDI`, `E.23.CAE` | E.23.CDI develops the acquisition or provision choice; E.23.CAE distinguishes apparent loss or failed use from a supported capability change. |
| `C.25` | Governs composite quality families and Q-Bundles that may supply slots for capability-fit checks. |
| `C.30`, `C.32.HCS`, `C.32.ACS`, `C.32.ACE` | Govern architecture-characteristic material, project criteria rows, and eval readings that may constrain capability use without thereby establishing the holder's ability. |
| Promise-content and commitment patterns | Govern outward promise and commitment relations; a promise or commitment claim may cite a qualified capability claim, but capability does not become promise or commitment. |

### A.2.2:14 - Neighboring Claims

Use the direct pattern for any additional claim that the ability or fit decision consumes. Section 4 distinguishes common ambiguous wordings, and section 13 identifies their governors. Keep the neighboring value's own identity and the contribution it makes to the ability claim, its support or the receiving comparison.

### A.2.2:End
