## A.15.5 - Work-Entry Readiness and Full-Kit Preparation

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Judge whether an intended performance in a WorkPlan and PlanItem satisfies a local work-entry criterion at the stated time. Apply that criterion to the current inputs it requires. Identify a separate checking Work only when its dated occurrence is claimed. Keep the result and its grounds recoverable for the receiving use; readiness creates neither the intended Work nor its prerequisite facts.

**Use this when.** Use this pattern when a team is about to commit, release, launch, or admit intended work and needs to test its work-entry conditions against the available facts and preparations.

**Primary EntityOfConcern.** The C.2.1 readiness-result episteme has the `U.WorkPlan` being judged as its exact EntityOfConcern. Its ClaimGraph designates the relevant `PlanItem`, intended performance, criterion, evaluated facts, verdict, and applicability window. Preserve the plan's exact intended-work kind or work-family classification when that distinction is current; it remains ClaimGraph content and does not instantiate a dated `U.Work`. The plan names the target `U.Method`; cite a separately constituted `U.MethodDescription` episteme only when the readiness criterion or planned use relies on that exact description. The intended-performance designator, intended-work kind, plan item, method, and description are not a dated target `U.Work` occurrence.

**First output.** A readable result identifying the WorkPlan, PlanItem and intended performance; criterion and evaluation time; readiness value; consumed input propositions and their qualification intervals; reliance window; and stop or recheck condition. Add a checking-Work reference only when that occurrence matters. Inputs keep their own predicates and identities.

**Ordinary route.** Identify the plan content, criterion and evaluation time. Check the criterion against its current inputs and return `ready`, `readyWithKnownGaps`, `notReady` or `unknown`, with the reliance window and stop or recheck condition. Reuse applicable input results. Stop when this answers the receiving question; add a separate checking Work, result-episteme reference, gate, permission or assurance claim only when the use needs it.

When degraded support, handoff, or continuation-state evidence can change work entry, use the present-WorkPlan branch of `A.15.8` to test the proposed performer, support, and state configuration, then return here with its bounded result. Ordinary full-kit checking does not require `A.15.8`.

**What this buys.** A team can decide the next bounded move—start no work yet, prepare an exact missing input, recheck, or submit declared checks to a gate—under the criterion and the entry conditions actually required.

**Not this pattern when.** Use `A.15.2` for the work plan itself, `A.15.3` for planned slot fillers, `A.15.1` for dated performed work, `A.21` for gate decisions, `A.15.4` only when a reliance appearance is already being used as a reason for work or reliance before the subject pattern slot, relation, or project-side reference is named, `B.1.6` for resource aggregation after work, `E.18` for transformation-flow structure, and `E.18.1` for P2W carry-through from accepted problem-side material.

### A.15.5:1 - Problem Frame

Teams often say that work is "ready", "full-kitted", "committed", "green", "released", or "good to start." Those words can point to different FPF values: an intended WorkPlan, a PlanItem baseline, a performed preparation activity, a gate decision, a source-currentness relation, resource availability, or resulting performed work.

`A.15.5` gives the work-entry readiness question a local criterion and result semantics. A readiness judgement is pre-entry unless a recheck after launch or post-launch variance claim is explicitly current. It may use established preparation or checking Work as an input.

### A.15.5:2 - Problem

Without one explicit local work-entry readiness claim and result semantics:

1. Full-kit preparation becomes an attractive umbrella for planning, source relations, gate passage, and performed work.
2. A green tile or ready label is treated as a `GateDecisionResult`.
3. Declaration-local planned-filling content inside the WorkPlan is overread as evidence that the planned values were actually prepared or used.
4. Resource readiness is confused with resource consumption.
5. A committed item becomes "done" by position in a board, not by a separately established completion claim about dated `U.Work`.

### A.15.5:3 - Forces

| Force | Pressure |
| --- | --- |
| Work-entry speed | Teams need a short readiness result before work entry. |
| Open-world discipline | An input omitted from one criterion is not thereby absent; an unavailable required fact returns `unknown` unless an applicable explicit failure condition is established. |
| Plan and work split | A readiness claim can cite intended work and performed preparation or checking Work without becoming performed target Work. |
| Gate separation | An A.21 gate may consume a readiness result as a declared check input, but readiness does not publish a `GateDecisionResult`. |
| Full-kit usefulness | Full-kit thinking is valuable when it states what must be known, prepared, reserved, or checked before work starts. |

### A.15.5:4 - Solution

State readiness as a domain-local result about the identified plan content. When the result needs its own reference, identify its C.2.1 episteme; retain a durable representation when later access requires it.

**Full-kit use.** Use the actual plan, input facts and readiness result needed by the work-entry question. The source contribution and limits of the TameFlow adaptation are stated in §11.

#### A.15.5:4.1 - One work-entry readiness claim

Start with one ordinary sentence:

> At evaluation time T, criterion C applied to intended performance I in PlanItem J of WorkPlan P yields readiness value R for use through window V; stop or recheck when Q occurs.

`P` is a WorkPlan episteme; `J` and `I` are its plan-local ClaimGraph content. A.15.3 applies when that content selects a member of an admitted declaration. `C` is the criterion episteme applicable to that item and evaluation time. `R` is one local `ReadinessResultValue`. If the account also identifies a dated checking occurrence W, admit it independently under §4.2's A.13/A.15.1 rule and add F.6 only for a consumed assignment-bound claim. The readiness verdict remains separate from that Work, a gate decision, permission or commitment.

The local value family is:

- `ready` — every input required by C is determined and satisfies C for V;
- `readyWithKnownGaps` — C explicitly admits the named gaps for this exact bounded use, every non-waived input is determined and satisfied, and V plus the stop condition expose the remaining risk;
- `notReady` — an applicable failure or closure condition in C is determined for this case; and
- `unknown` — one required fact, currentness result, predicate, or applicability basis cannot be determined, and no already determined applicable failure or closure condition settles the result as `notReady`. Absence of an assertion or persisted episteme is not by itself `notReady`.

When the result needs a separate identity, its C.2.1 episteme has P as EntityOfConcern and a ClaimGraph stating J, I, C, R, the evaluated facts, evaluation time, reliance window and recheck condition under the effective reference scheme. Include W only when its occurrence is a claimed input. C.2.1 supplies identity. For reusable predicate semantics use A.6.RCD's corresponding branch; open relation-kind admission only when a receiving use needs distinct readiness occurrences.

When reporting what a particular evaluation returned, identify its actual application and result binding or a direct evaluation-result predicate with its obtaining facts (A.15.1:4.6). Retain the ordinary result format when the receiving use asks for readiness itself.

The result episteme states the readiness judgement. If a current claim says that exact checking or preparation Work first constituted that episteme, recover that local entity-identity inception claim under A.15.PROD.

#### A.15.5:4.2 - Readiness criterion and full-kit inputs

Use one exact readiness criterion when the entry question depends on what must be known, prepared, reserved, gathered, communicated, assigned, or pinned before work starts. The criterion states:

- the exact WorkPlan and its present EntityOfConcern, PlanItem, intended-performance designator, any exact intended-work target and intended outcome or value claim current in the plan, any current intended-work kind or work-family classification, target `U.Method`, evaluation time, and applicability window it judges;
- each required positive or negative predicate, the allowed named gaps if any, and the rule for `ready`, `readyWithKnownGaps`, `notReady`, and `unknown`;
- which changed fact, expired interval, new conflict, source revision, or resource or assignment change ends reliance; and
- the stop, degraded-use, preparation, or recheck action for each non-ready result.

Full-kit thinking helps recognize possible inputs. Check only the input claims that C actually consumes:

1. exact A.15.2 plan content and any A.15.3 planned fillings, with the declaration member and conditions that give each filling meaning;
2. current information, source-currentness, publication, measurement, evidence, or assurance claims under their subject patterns;
3. exact resource-availability or reservation claims, intended performer Systems and local system-role-kind conditions, any already obtaining occurrence of an exact directly declared `U.SystemRoleAssignment` species when C requires an assignment, capability threshold or fit result, and exact commitment claims when C uses them; plus any exact current work-in-progress or load and flow-policy claims under the pattern that defines their counted work, boundary, threshold, and qualification window;
4. preparation or checking results required by C, and separately admitted preparation/checking Work only when its actual occurrence is consumed by the criterion;
5. exact prospective A.2.8.PER grant, non-prohibition, or conflict facts and their qualification windows when permission is current; and
6. an exact A.21 `GateDecisionResult` only when a current A.21 profile application governs the declared check applications and their mappings to that decision. The gate decision remains a separate result.

An exact post-launch variance or recheck result may enter only after the target Work is actual and only through the measurement, comparison, evaluation, resource, temporal, acceptance, or other pattern that defines that exact result. Name the target Work, comparison or evaluation rule, local result, qualification window, and subject pattern. It may trigger or inform an explicitly marked recheck; it neither proves that readiness held before entry nor rewrites the earlier readiness result.
For each input, name the subject pattern, exact proposition or relation occurrence, and the interval or currentness result on which this readiness check relies. A generic input, evidence, context, resource, assignment, or policy reference supplies none of those facts. Omission says only that the current criterion did not consume that input; it does not prove absence.

Full-kit preparation can include gathering information, coordinating intended performer Systems and local system-role-kind conditions, producing a missing source `U.Episteme` or source publication, reserving a resource, pinning a planned filling, or creating shared understanding. When a dated occurrence is claimed as `U.Work`, actual performance and the admission basis below must be established. Plan the preparation beforehand; cite its actual result or admitted Work only after the corresponding facts are established.

For every cited preparation or readiness-checking Work occurrence, apply the complete A.15.1:4.0–4.1 admission test. Establish the common A.1:4.2 construction of that same candidate, each actual performer's A.13 core, grounded performance history following at least one identified Method, temporal extent, and the factual conditions of a locally declared relation containing the complete occurrence within a System boundary. Admit the candidate, then state its typed Method-enactment and containing-System relations. Only when the readiness claim needs precise assignment-bound attribution, establish F.6 afterward through the same obtaining A.13 assignment and keep its declared species, participants, holder, coverage, and exact Work-assignment link recoverable. Name another enacted Method, boundary, direct participant relation, or A.6.1 binding when the readiness claim uses it. A planned preparation task remains A.15.2 content until the occurrence facts obtain.

**Boundary with planned fillers and appearance-based reliance.** An ordinary missing plan choice stays with A.15.2. Use A.15.3 when the proposed choice is declaration-local planned-filling content: recover the actual declaration member and its meaning and use conditions. A known evidence, currentness, publication, gate, permission or assurance claim goes directly to its subject pattern. Use A.15.4 while an appearance is being relied on before the required predicate and its basis have been recovered.

#### A.15.5:4.3 - Commitment and Launch Boundary

Keep commitment facts separate from the readiness value. The criterion may consume exact current commitment claims and their qualification intervals, but `ready`, `readyWithKnownGaps`, `notReady`, or `unknown` does not mean `committed`, institute a commitment, discharge one, or authorize entry. State the practical next move—stop, prepare, probe, seek a separately governed commitment, submit to a gate, launch only under its separately satisfied entry conditions, or recheck—as the result's bounded use and return condition, not as another ontic status family. The older labels `readyForProbe`, `readyForCommitment`, `committed`, `blocked`, and `requiresGateDecision` therefore resolve to a local readiness value plus an explicit next move, commitment claim, stop, or gate question; they are not additional `ReadinessResultValue` members.

Use `A.2.8.PER` when a pre-entry readiness criterion consumes permission material. Name each value and its own qualification: a current `GrantedPermissionRelation@Context` occurrence with its beneficiary, permitted-action specification, `U.ClaimScope`, and `validityWindow`; a distinct `NonProhibitionFinding@Context` with its frame and `evaluationWindow`; and any `PermissionNormConflictFinding@Context` with its `overlapWindow` and disposition. For a settled conflict, retain the applicable precedence rule and its qualification, or the current resolution result and `effectiveWindow`, according to A.2.8.PER:4.6. Non-prohibition is not a grant, and a grant does not itself settle a conflict. An unresolved conflict limits the readiness use under C; the affected action remains blocked under the permission rule. Cite `PermissionExerciseRelation@Context` or `NonViolationFinding@Context` only for already dated Work: either as evidence about a different Work occurrence or in an explicitly marked post-launch recheck after the target Work is actual, retaining its own `exerciseInterval` or `evaluationWindow`. Those retrospective findings support their named past claims; prospective grant, capability, readiness and entry claims need their own current grounds. Use A.21 when a current profile application governs the declared check applications and their mappings to a distinct `GateDecisionResult`. Keep that result, scope, currentness and qualification window recoverable. Use `DecisionLogRef` when a log supplies the access, audit or replay path or the applicable policy requires it.

#### A.15.5:4.4 - Relation to A.15 Family

| Current claim | Subject pattern |
| --- | --- |
| Intended target work and horizon | `A.15.2 U.WorkPlan`. |
| Planned fillings before work | A.15.3 declaration-local planned-filling content inside the exact `U.WorkPlan`. |
| Preparation activity that actually happened | `A.15.1 U.Work`. |
| Target work that actually happened | `A.15.1 U.Work`. |
| Readiness before work entry | `A.15.5` local result claim; C.2.1 identifies a result episteme when that content needs its own reference. |
| Resource budgets or reservations before work | `A.15.2` plan content plus the exact predicate and source for the current resource-availability or reservation claim; A.15.5 cites the current claim only when the criterion consumes it. |
| Resource consumption by work | `B.1.6` plus `A.15.1`. |

#### A.15.5:4.5 - Relation to P2W and Pattern Use

When `E.18.1` carries accepted problem-side material to a readiness question, `E.18.1` names that carry-through relation and cites `A.15.5` for the readiness result. When a user needs to know which pattern to use before readiness is current, use `E.11.PUR`.

### A.15.5:5 - Archetypal Grounding - Worked Slices

The following constructed cases stipulate their project facts and illustrate the separate readiness, occurrence and reliance questions.

#### A.15.5:5.1 - Fixture deformation test

**Situation.** An accepted cooling-fixture ProblemCard has been carried through E.18.1 into `WorkPlan-LAB-043 : U.WorkPlan`; that P2W carry-through creates neither readiness nor target Work. Its `PlanItem-TEST-043` designates possible future performance `planned-fixture-deformation-test-043`, classifies the intended work as fixture-deformation testing under the plan's current scheme, selects `FixtureDeformationTestMethod-E2 : U.Method`, and relies on `FixtureDeformationTestProcedure-E5 : U.MethodDescription` with that admitted Method as its exact EntityOfConcern and substantive setup-limit claims under A.3.2. The plan records specimen and instrument choices labeled `SFI-043`. To use them as A.15.3 planned-filling rows, recover the selected declaration, its members and their actual-use conditions; until those are recovered, retain the ordinary plan choices and leave their declaration-local filling interpretation unresolved. The plan also records planned resource reservation `FixtureBayReservation-043` and intended performer-system and `FixtureTestTechnicianSystemRole` conditions. These choices remain content of this WorkPlan.

`FixtureTestEntryCriterion-E2` requires, for the proposed 09:00–09:30 UTC start window on 2026-07-27, a resolved specimen identity, heat-flow invariant claim, boundary-condition plan, sensor-calibration result, selected fixture-drawing edition, resource-availability claim, and fixture-test-technician assignment, all current for this use. The assignment basis is explicit once: `FixtureTestTechnicianAssignment` is a directly declared `U.SystemRoleAssignment` species. It defines the holder and assigned-kind positions, uses `FixtureTestSystemRoleKindDomain`, requires `FixtureTestTechnicianSystemRole`, and applies to this laboratory test. Its obtaining occurrence `FixtureTestTechnicianAssignment-043` has `FixtureTechnicianSystem-043` as holder and covers the proposed start window. `SFI-043` preserves the planned specimen and instrument choices; their actual preparation or use needs its own facts. The calibration result, its A.10 evidence path and currentness result, and the E.17 drawing-edition publication use remain separate inputs. The criterion explicitly treats known expiry or a recorded unresolved required-input status as failure and returns `notReady`. If the input or its status cannot be determined and no such failure is established, return `unknown`. A change to a consumed input, assignment coverage, resource availability or start window reopens the affected readiness conclusion; unchanged applicable input results remain reusable.

`LabMetrologySystem-2` and `LabOperationsCoordinatorSystem-1` are independently admitted Systems. For this constructed case, `CalibrationCheckingSystemRole` requires condition-sensitive calibration checking, and `ReadinessCheckingSystemRole` requires selection of readiness/preparation actions against the entry criterion; the stipulated observations support both classifications for this checking scope and window. The directly declared `LabMetrologyAssignment` and `LabOperationsCoordinationAssignment` species establish their holder/kind meanings, and case facts make `RA-LabMetrology-2-E7` and `RA-LabOperationsCoordinator-1-E4` obtain for those Systems and local kinds throughout 08:40–08:50 UTC on 2026-07-27.

The performance history identifies candidate occurrences `CalibrationCurrentnessCheck-043` during 08:40–08:45 and `FixtureEntryReadinessCheck-043` during 08:46–08:50 on that date, following `CalibrationCurrentnessCheckMethod-E1` and `FixtureEntryReadinessEvaluationMethod-E2` respectively. For each complete candidate, this constructed case stipulates the independently established A.1:4.2 construction. The local `LabCheckingWorkOccursWithinService@LAB043` declaration requires the complete checking occurrence to lie within admitted `LabQualityServiceSystem-043`'s declared calibration/readiness-checking boundary throughout its checking interval; the stipulated performance histories satisfy that condition. Together with each performer's established A.13 basis, these premises admit both candidates under A.15.1. Their typed `enactsMethod` and containing-System relations then obtain on those same grounds. Their separate F.6 attributions use the same obtaining assignments and the case's Work-assignment facts. Neither is the intended fixture test.

For this constructed case, the laboratory defines two local evaluation-result predicates. `calibrationExpiryReported(W, X, T)` holds when W's actual performer compares calibration result X's governing validity end with T, determines that it is no later than T, and completes that check by reporting `expired`. `fixtureReadinessReturned(W, R)` holds when W's actual performer evaluates the named plan item and proposed start window under `FixtureTestEntryCriterion-E2`, using the identified input facts, and completes that check by reporting R as its readiness verdict. Each claim concerns one terminal report in one checking episode; a recheck is another episode.

The constructed history stipulates that the calibration result's validity ended at 08:30 UTC on 2026-07-27. During `CalibrationCurrentnessCheck-043`, `LabMetrologySystem-2` makes that comparison and reports `expired` at 08:45. During `FixtureEntryReadinessCheck-043`, `LabOperationsCoordinatorSystem-1` evaluates `PlanItem-TEST-043` in `WorkPlan-LAB-043` for the proposed 09:00–09:30 start window. It uses the established calibration expiry and the recorded unresolved drawing-edition status, applies the criterion's explicit failure rule, and reports `notReady` at 08:50.

The C.2.1 episteme `FixtureTestEntryReadinessResult-E1`, whose exact EntityOfConcern is `WorkPlan-LAB-043`, reports that readiness verdict and its grounds for `PlanItem-TEST-043`: the calibration result is expired and the fixture-drawing edition remains unresolved. Its stop is `do not start planned-fixture-deformation-test-043`; its return condition is `obtain a current calibration result, select the drawing edition, and rerun the readiness check`. The preparation and checking Work occurred; the target test did not. No A.21 gate decision or A.2.8.PER permission result follows from this readiness result.

**What changes in practice.** The team withholds the target test and prepares the current calibration and selected drawing. After those inputs are available, it reapplies the criterion and reuses other unchanged applicable grounds. Any assignment of that preparation has its own allocation basis; the readiness result itself supplies no duty or target Work.

#### A.15.5:5.2 - Documentation Repair Probe

Situation: an assisting agent can run a reversible documentation probe to find source-currentness gaps.

Use A.15.5 for the probe only if its work-entry decision needs a readiness criterion; an ordinary sufficient reversible probe needs no automatic formal plan or readiness result. When that branch is selected, apply the criterion to the probe's WorkPlan and return the bounded value. If the account later claims the performed probe as a dated Work, recover its A.13 core and independent A.15.1 admission, adding F.6 only for precise attribution. A target-repair readiness question is then evaluated separately; the probe plan, readiness, actual occurrence and target-repair result establish different claims.

#### A.15.5:5.3 - Release screen with separate readiness, gate, and permission windows

At 10:00 UTC on 2026-07-27, the evaluator applies `ReleaseEntryCriterion-E3` to `ReleasePlan-E7` and `PlanItem-Deploy-12`. The result says `ready` for reliance only in `[10:00, 10:30)` and requires recheck when a consumed source, resource, assignment, permission or gate input changes. All times below use UTC on that date.

At `10:05`, the current A.21 application of profile `Release-Core-E4` consumes that readiness result through one identified `GateCheckApplicationResult`, cited by its `GateCheckRef`, among the complete effective check set. The gate returns a `GateDecisionResult` with `decisionValue=pass` for `[10:05, 10:20)`; `DecisionLogRef=ReleaseGateLog-12` cites the separate log recording that result. That gate result is not the readiness result and does not institute permission.

Separately, exact A.2.8.PER `GrantedPermissionRelation@Context` occurrence `DeployGrant-12` covers the named beneficiary and deployment action for `[09:00, 11:00)`. `DeployNonProhibitionFinding-E2` reports `nonProhibited` from its named current frame, explicitly complete for this use, in evaluation window `[10:00, 10:15)`; it is not the grant. A `PermissionNormConflictFinding@Context`, if an incompatible current norm is established over the same content and window, would be a third permission-side input and an unresolved disposition would stop the use. A policy that requires readiness, gate passage, a current grant, and the frame-relative non-prohibition result may rely on those distinct inputs at `10:10`; it must re-evaluate the relevant branch when any window ends or a conflict appears. None of them proves that deployment Work occurred. A.15.1 identifies that Work only after its dated occurrence basis obtains.

If a dashboard shows green but the readiness result or its reliance window, the current A.21 profile application and gate result, or the required permission value and qualification window cannot be recovered, keep the display at source finding under A.15.4. Recover the gate result directly or through `ReleaseGateLog-12`; loss of the log alone need not block reliance on a fully recoverable result. Open the A.10 evidence-provenance and currentness question when that basis for a consumed claim is unresolved.

### A.15.5:6 - Bias-Annotation

- **Ready-label bias.** A green tile, ready label, release screen, or commitment board position can look stronger than the recoverable claim. Recover whether the current object is readiness, appearance-based reliance repair under `A.15.4`, gate decision, work authorization, or performed work.
- **Full-kit umbrella bias.** Full-kit preparation is useful, but it can hide planned baselines, performed preparation work, resource readiness, source currentness, and target work. Keep each current value in its subject pattern.
- **Baseline-as-actuals bias.** Planned fillers and readiness references do not prove launch values, performed values, variance, or results.

### A.15.5:7 - Conformance Checklist

| ID | A conforming readiness use... | Check |
| --- | --- | --- |
| `CC-A15.5-1` | names the exact WorkPlan, PlanItem, intended performance, criterion, and evaluation time. | The readiness result cannot float free of the plan content and bounded entry question it judges. |
| `CC-A15.5-2` | separates readiness from performed work. | No target `U.Work` occurrence is asserted unless dated work evidence is current. |
| `CC-A15.5-3` | separates full-kit inputs, checking results and preparation/checking Work. | A readiness claim need not identify a separate checking Work. Every dated Work it does assert needs A.13 and independent A.15.1 admission; F.6 applies only to a consumed precise assignment-bound claim. |
| `CC-A15.5-4` | cites planned baselines without rewriting them. | A.15.3 planned-filling rows remain declaration-local content inside the exact WorkPlan. |
| `CC-A15.5-5` | keeps gate decisions in A.21. | Readiness labels do not create `GateDecisionResult` without A.21 fields. |
| `CC-A15.5-6` | keeps resource readiness and resource aggregation distinct. | Planned reservations and actual consumption are not merged. |
| `CC-A15.5-7` | states stop, degraded-use, or recheck condition. | The reader can identify the next supported action; committing or launching still requires its separately satisfied conditions. |
| `CC-A15.5-8` | keeps prospective and retrospective permission inputs temporally typed and non-productive. | A current grant uses its `validityWindow`; non-prohibition uses its `evaluationWindow`; conflict uses its `overlapWindow` and any subject-pattern resolution `effectiveWindow`. Exercise and non-violation appear only for different dated Work or an explicit post-launch recheck, with their own intervals. None proves another permission value, readiness, gate passage, capability, or target-work performance. |
| `CC-A15.5-9` | keeps the readiness result, domain-local inputs, provenance, assurance, and any inception claim under their subject patterns. | C.2.1 identifies the readiness-result episteme; each measurement, evaluation, resource, permission, gate, or other input keeps its own result algebra; use A.10 for provenance and state any assurance result separately under B.3, and A.15.PROD is opened only for a separately current local entity-identity inception claim. |

### A.15.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better use |
| --- | --- | --- |
| Ready label as authorization | A label is treated as permission, conflict resolution, work authorization, or gate passage. | Use `A.2.8.PER` for the exact permission/conflict result, A.21 for gate decision, or A.15.4 when a reliance appearance is being used as a reason for work or reliance before the subject pattern slot, relation, or project-side reference is named. |
| Full kit as work done | Prepared inputs are treated as target work completion. | Record preparation work separately and target work only when it occurs. |
| Baseline as actuals | Planned slot fillers are treated as launch or performed values. | Keep planned fillers in A.15.3 and record variance after work. |
| MOVE imported as kind | TameFlow source wording becomes an FPF object. | Recover intended work, commitment, readiness, gate, preparation work, or performed work under FPF patterns. |

### A.15.5:9 - Consequences

Benefits:

- Teams can inspect work-entry readiness without flattening plan, preparation, gate, resource, and performed-work claims.
- The adapted pre-entry Full-Kitting distinctions supply a recognition palette for a local readiness criterion; neither TameFlow nor its source vocabulary governs FPF readiness.
- The result exposes the exact input claims and qualification intervals on which a later gate or work-entry decision may rely.

Costs:

- Some "ready" claims become incomplete until the target work, missing inputs, and stop condition are named.
- A full-kit check may expose missing preparation Work or inputs that need their own plan, subject-pattern currentness, evidence-provenance, publication, resource, or assignment claims.

### A.15.5:10 - Rationale

The readiness question is practical and recurrent: should this intended work enter the work boundary now? FPF already has the kinds needed to answer it. One local criterion and result claim keep the answer inspectable without collapsing the plan, its inputs, the checking Work, gate, permission, or target Work into one object.

The result depends on the inputs actually consumed by its criterion. It may use an immediate A.15.4 disposition without making that note a new formal object. Later reliance needs the claim and its grounds recoverable under the relevant access and currentness conditions; a durable representation is one way to provide that access. A missing input may need preparation, clarification or a direct subject-pattern check, rather than automatically becoming a source-repair problem.

### A.15.5:11 - SoTA-Echoing

| Source family | Bounded source contribution | Local adoption |
| --- | --- | --- |
| Steve Tendon, [*The Book of TameFlow: Theory of Constraints Applied to Knowledge-Work Management*](https://leanpub.com/tameflow) | Adapt only the pre-entry Full-Kitting distinctions used to recognize minimum outcome or value, target scope, commitment, WIP pressure, and preparation inputs. Reject source `MOVE` or Full-Kitting as an FPF kind or universal readiness ontology; the source remains scoped to knowledge-work management. | Use the adapted distinctions only as inputs to an FPF-local readiness criterion and result; keep WorkPlan, PlanItem, gate, preparation Work, resource, assignment, permission, and performed-Work claims under their subject patterns. |





### A.15.5:12 - Relations

- **Builds on:** `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, `A.15.4`, `A.21`, `B.1.6`, `E.18`, `E.18.1`, and `E.24`; consumes current `A.2.8.PER` grant/non-prohibition/conflict refs as prospective inputs, and exercise/non-violation refs only as evidence about different dated work or in an explicit post-launch recheck after target work is actual.
- **Coordinates with:** `E.11.PUR` for recommended pattern use before readiness is selected, `E.10.MOVE` for readiness wording repair, `C.32.P2S` when readiness prepares work that realizes architecture-selected structures, and `A.3.4.P` when workflow or process wording is primarily transformation-situation wording.
- **Does not replace:** target `U.WorkPlan`, its declaration-local planned-filling content, `U.Work`, `GateDecisionResult`, the A.15.4 reliance question and note, resource aggregation, or transformation-flow structure.


### A.15.5:End
