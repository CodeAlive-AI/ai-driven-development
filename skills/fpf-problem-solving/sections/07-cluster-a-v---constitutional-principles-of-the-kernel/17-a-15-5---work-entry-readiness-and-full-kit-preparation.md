## A.15.5 - Work-Entry Readiness and Full-Kit Preparation

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** `A.15.5` governs `WorkEntryReadiness@Context`: the planning and gate-facing relation that says whether intended work is ready enough to enter a work boundary. It uses full-kit preparation, commitment, resource readiness, flow policy, planned slot-filling baselines, and gate refs without treating readiness as performed work.

**Use this when.** Use this pattern when a team is about to commit, release, launch, or admit intended work and needs to know whether the needed inputs, currentness refs, publication refs, resources, planned fillers, constraints, and gate conditions are ready enough for that work entry.

**Primary EntityOfConcern.** One `WorkEntryReadiness@Context` relation for one intended work item, target work plan, PlanItem, or work-boundary concern in one bounded context.

**First output.** One `WorkEntryReadiness@Context` record with its `FullKitCondition`, commitment disposition, prospective direct permission inputs (a current grant occurrence, non-prohibition finding, or permission-conflict finding), and any retrospective exercise/non-violation ref only through `PriorWorkEvidenceRefs` for a different exact already-dated work occurrence or an explicitly post-launch recheck whose target work is already actual; plus resource-readiness, WIP or flow-policy, planned-baseline, gate, and stop or degraded-use refs when current.

**Not this pattern when.** Use `A.15.2` for the work plan itself, `A.15.3` for planned slot fillers, `A.15.1` for dated performed work, `A.21` for gate decisions, `A.15.4` only when a reliance appearance is already being used as a reason for work or reliance before the governing pattern slot, relation, or project-side reference is named, `B.1.6` for resource aggregation after work, `E.18` for transformation-flow structure, and `E.18.1` for P2W carry-through from accepted problem-side material.

### A.15.5:1 - Problem Frame

Teams often say that work is "ready", "full-kitted", "committed", "green", "released", or "good to start." Those words can point to different FPF values: an intended WorkPlan, a PlanItem baseline, a performed preparation activity, a gate decision, a source-currentness relation, resource availability, or resulting performed work.

`A.15.5` gives the readiness relation one place without importing a management framework object as an FPF kind. Readiness is pre-work-entry unless a recheck after launch or post-launch variance claim is explicitly current. A readiness relation may cite preparation work, but it is not that preparation work and not the target performed work.

### A.15.5:2 - Problem

Without a separate work-entry readiness relation:

1. Full-kit preparation becomes an attractive umbrella for planning, source relations, gate passage, and performed work.
2. A green tile or ready label is treated as a `GateDecision`.
3. A `SlotFillingsPlanItem` baseline is overread as evidence that the planned values were actually prepared or used.
4. Resource readiness is confused with resource consumption.
5. A committed item becomes "done" by position in a board, not by dated `U.Work`.

### A.15.5:3 - Forces

| Force | Pressure |
| --- | --- |
| Work-entry speed | Teams need a short readiness result before work entry. |
| Open-world discipline | A missing field in the readiness record does not mean the corresponding concern does not exist; it means the current readiness claim did not use that slot. |
| Plan and work split | A readiness relation can cite intended work and preparation work without becoming performed target work. |
| Gate separation | A gate may consume readiness evidence, but the readiness relation does not itself publish a `GateDecision`. |
| Full-kit usefulness | Full-kit thinking is valuable when it states what must be known, prepared, reserved, or checked before work starts. |

### A.15.5:4 - Solution

Represent readiness as `WorkEntryReadiness@Context`, a dependent relation under the A.15 family and A.21 boundary.

E.24.UK settlement: this pattern does not introduce a root `U.Readiness`, root `U.Move`, imported TameFlow `MOVE` kind, or independent readiness ontic. The selected relation is a context readiness relation over existing values: `U.WorkPlan`, PlanItem, `SlotFillingsPlanItem`, intended work kind, target EntityOfConcern, commitment disposition, resource-readiness refs, gate refs, evidence refs, and performed `U.Work` only when that work has occurred. `FullKitCondition` is a condition inside this readiness relation, not a separate root kind.

#### A.15.5:4.1 - WorkEntryReadiness@Context

```text
WorkEntryReadiness@Context:
  WorkEntryConcernRef
  BoundedContextRef
  TargetWorkPlanRef?
  TargetPlanItemRef?
  TargetWorkKindRef?
  TargetEntityOfConcernRef?
  IntendedOutcomeOrValueRef?
  FullKitCondition?
  CommitmentDisposition?
  GrantedPermissionOccurrenceRef?     # prospective direct input when current
  NonProhibitionFindingRef?           # prospective direct input when current
  PermissionNormConflictFindingRef?   # prospective current-conflict input
  ResourceReadinessRefs?
  WIPPolicyRef?
  FlowPolicyRef?
  SlotFillingsPlanItemRefs?
  PreparationWorkRefs?
  PriorWorkEvidenceRefs?              # may cite exercise/non-violation only for a different exact already-dated work occurrence
  SourceCurrentnessRefs?
  LaunchGateRef?
  GateDecisionRef?
  EvidenceRefs?
  StopCondition
  DegradedUse?
  ReturnOrRecheckCondition?
  PostLaunchVarianceRef?              # target-work exercise/non-violation only in an explicit post-launch recheck after that work is actual
```

The record is filled according to the current readiness claim. It is not a demand to fill every slot. It is a checklist of concerns that must not be forgotten when those concerns are live.

#### A.15.5:4.2 - FullKitCondition

Use `FullKitCondition` when the readiness question depends on what must be known, prepared, reserved, gathered, communicated, or pinned before work entry.

```text
FullKitCondition:
  NeededInputRefs
  KnownInputRefs
  MissingInputRefs
  GoverningPatternForEachMissingValue
  PreparationWorkRef?          # only when preparation was performed
  PlannedBaselineRef?          # usually A.15.3 SlotFillingsPlanItem
  SourceCurrentnessRefs?
  PublicationRefs?
  ResourceReadinessRefs?
  StopOrDegradedUseRule
```

Full-kit preparation can include gathering information, coordinating roles, producing a missing source `U.Episteme` or source `U.EpistemePublication`, reserving a resource, pinning a planned filler, or creating shared understanding. Those activities are `U.Work` only when actually performed. The readiness record cites them; it does not become them.

**Boundary with planned fillers and appearance-based reliance.** A missing planned value in `FullKitCondition` stays with `A.15.3` as a planned slot-filling baseline or with the direct governing pattern when an evidence, currentness, publication, gate, or assurance relation is already known. Use `A.15.4` only when a reliance appearance, such as a dashboard label, copied approval, publication face, or credential view, is being used as the reason to treat the readiness or work-reliance claim as carried before that governing pattern slot or relation has been recovered.

#### A.15.5:4.3 - Commitment and Launch Boundary

`CommitmentDisposition` states the work-entry stance, such as `notReady`, `readyWithKnownGaps`, `readyForProbe`, `readyForCommitment`, `committed`, `blocked`, or `requiresGateDecision`.

Use `A.2.8.PER` when a pre-entry readiness check requires a current granted-permission occurrence, non-prohibition finding, or permission-conflict finding. `PermissionExerciseRelation@Context` and `NonViolationFinding@Context` require already dated actual work: cite either through `PriorWorkEvidenceRefs` only for a different exact work occurrence, or in an explicitly marked post-launch recheck only after the target work is actual; the latter is not evidence that the target was ready before entry. Prior exercise or non-violation proves none of a current grant, current capability, future exercise, future non-violation, readiness, gate passage, or target-work performance. Readiness does not institute permission, exercise it, resolve conflict, or turn non-prohibition into a grant; an unresolved current conflict blocks or degrades reliance according to `A.2.8.PER`. Use A.21 only when a current `OperationalGate(profile)` consumes declared checks and publishes a `GateDecision`. A readiness badge, green tile, full-kit label, or commitment board position is not gate passage unless A.21 fields are recoverable; gate passage creates none of the permission objects.

#### A.15.5:4.4 - Relation to A.15 Family

| Current claim | Governing pattern |
| --- | --- |
| Intended target work and horizon | `A.15.2 U.WorkPlan`. |
| Planned slot fillers before work | `A.15.3 SlotFillingsPlanItem`. |
| Preparation activity that actually happened | `A.15.1 U.Work`. |
| Target work that actually happened | `A.15.1 U.Work`. |
| Readiness before work entry | `A.15.5 WorkEntryReadiness@Context`. |
| Resource budgets or reservations before work | `A.15.5` with `B.1.6` refs when resource semantics are current. |
| Resource consumption by work | `B.1.6` plus `A.15.1`. |

#### A.15.5:4.5 - Relation to P2W and Pattern Use

When `E.18.1` carries accepted problem-side material to a readiness question, `E.18.1` names that carry-through relation and cites `A.15.5` for the readiness result. When a user needs to know which pattern to use before readiness is current, use `E.11.PUR`.

### A.15.5:5 - Archetypal Grounding - Worked Slices

#### A.15.5:5.1 - Fixture Deformation Work

Situation: a cooling-fixture team plans a deformation test. The ProblemCard is accepted, P2W has carried a heat-flow distinction into a work-planning question, and the team asks whether the test is ready to start.

```text
WorkEntryReadiness@Context:
  WorkEntryConcernRef: cooling-fixture deformation test
  BoundedContextRef: lab test before comparator run
  TargetWorkPlanRef: WorkPlan-LAB-043
  TargetPlanItemRef: PlanItem-TEST-043
  FullKitCondition:
    NeededInputRefs: specimen id, heat-flow invariant note, boundary-condition plan, sensor calibration record or certificate, fixture drawing edition
    KnownInputRefs: specimen id, heat-flow invariant note
    MissingInputRefs: sensor calibration record or certificate, fixture drawing edition
    GoverningPatternForEachMissingValue: A.15.3 for planned calibration-record filler, A.10 when calibration evidence or currentness is claimed, E.17 for drawing publication edition
    PlannedBaselineRef: SlotFillingsPlanItem-SFI-043
    StopOrDegradedUseRule: no launch until calibration and drawing edition are pinned
  CommitmentDisposition: blocked
  LaunchGateRef: LaunchGate-LAB-043
  StopCondition: do not start target test work
```

The readiness result blocks target work entry. It does not say the lab test occurred.

#### A.15.5:5.2 - Documentation Repair Probe

Situation: an assisting agent can run a reversible documentation probe to find source-currentness gaps.

Use `WorkEntryReadiness@Context` only for the readiness of the probe or repair work. If the probe is actually run, record the probe as `U.Work` under `A.15.1` and then recheck readiness for the target repair.

#### A.15.5:5.3 - Release Screen

Situation: a release dashboard shows a green readiness badge.

If the current claim is "the release gate passed", use A.21 and recover `OperationalGate(profile)`, declared checks, aggregate, `GateDecision`, `DecisionLogRef`, scope, currentness, and window. If those fields are not recoverable, the display may be a reliance appearance for `A.15.4`, an evidence question, or a readiness indication. It is not gate passage by appearance.

### A.15.5:6 - Bias-Annotation

- **Ready-label bias.** A green tile, ready label, release screen, or commitment board position can look stronger than the recoverable claim. Recover whether the current object is readiness, appearance-based reliance repair under `A.15.4`, gate decision, work authorization, or performed work.
- **Full-kit umbrella bias.** Full-kit preparation is useful, but it can hide planned baselines, performed preparation work, resource readiness, source currentness, and target work. Keep each current value in its governing pattern.
- **Baseline-as-actuals bias.** Planned fillers and readiness references do not prove launch values, performed values, variance, or results.

### A.15.5:7 - Conformance Checklist

| ID | A conforming readiness use... | Check |
| --- | --- | --- |
| `CC-A15.5-1` | names the target intended work or work-boundary concern. | The readiness relation is not floating without a target concern. |
| `CC-A15.5-2` | separates readiness from performed work. | No target `U.Work` occurrence is asserted unless dated work evidence is current. |
| `CC-A15.5-3` | separates full-kit condition from preparation work. | `PreparationWorkRef` is used only when preparation was performed. |
| `CC-A15.5-4` | cites planned baselines without rewriting them. | `SlotFillingsPlanItem` remains a plan-item baseline under A.15.3. |
| `CC-A15.5-5` | keeps gate decisions in A.21. | Readiness labels do not create `GateDecision` without A.21 fields. |
| `CC-A15.5-6` | keeps resource readiness and resource aggregation distinct. | Planned reservations and actual consumption are not merged. |
| `CC-A15.5-7` | states stop, degraded-use, or recheck condition. | The reader can tell whether to stop, probe, commit, launch, or return to a missing governing pattern value. |
| `CC-A15.5-8` | keeps prospective and retrospective permission inputs temporally typed and non-productive. | A current grant, non-prohibition finding, or conflict finding may be a prospective direct input; exercise/non-violation appears only in `PriorWorkEvidenceRefs` for different dated work or in an explicit post-launch recheck after the target work is actual. Neither prior result proves current grant, capability, future exercise/non-violation, readiness, gate passage, or target-work performance; unresolved current conflict blocks or degrades reliance under `A.2.8.PER`. |

### A.15.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Better use |
| --- | --- | --- |
| Ready label as authorization | A label is treated as permission, conflict resolution, work authorization, or gate passage. | Use `A.2.8.PER` for the exact permission/conflict result, A.21 for gate decision, or A.15.4 when a reliance appearance is being used as a reason for work or reliance before the governing pattern slot, relation, or project-side reference is named. |
| Full kit as work done | Prepared inputs are treated as target work completion. | Record preparation work separately and target work only when it occurs. |
| Baseline as actuals | Planned slot fillers are treated as launch or performed values. | Keep planned fillers in A.15.3 and record variance after work. |
| MOVE imported as kind | TameFlow source wording becomes an FPF object. | Recover intended work, commitment, readiness, gate, preparation work, or performed work under FPF patterns. |

### A.15.5:9 - Consequences

Benefits:

- Teams can inspect work-entry readiness without flattening plan, preparation, gate, resource, and performed-work claims.
- TameFlow full-kitting contributes useful criteria without importing TameFlow `MOVE` as an FPF kind.
- Gate and work evidence remain auditable because readiness only cites them when they are current.

Costs:

- Some "ready" claims become incomplete until the target work, missing inputs, and stop condition are named.
- A full-kit record may expose preparation work that needs its own plan, currentness, evidence, publication, and resource records.

### A.15.5:10 - Rationale

The readiness question is practical and recurrent: should this intended work enter the work boundary now? FPF already has the kinds needed to answer that question, but without a small readiness relation the same words pull in too many objects at once.

`WorkEntryReadiness@Context` is deliberately dependent. It preserves `U.WorkPlan`, `SlotFillingsPlanItem`, `U.Work`, A.21 gate decisions, B.1.6 resource relations, and A.15.4 appearance-based reliance repair while giving the practitioner one inspectable pre-work-entry record. A readiness record may cite an `A.15.4` repair result; it does not turn every missing input into a source problem.

### A.15.5:11 - SoTA-Echoing

| Source family | Use in this pattern | Local adoption |
| --- | --- | --- |
| TameFlow `MOVE` and Full-Kitting material | Supplies minimal outcome-value effort, target scope, commitment, WIP pressure, and pre-entry full-kit criteria. | Adopt as external distinctions; adapt into FPF `WorkEntryReadiness@Context`, WorkPlan, PlanItem, gate, preparation work, resource, and performed-work relations. |
| Current A.15 work-family settlement | Separates intended work, planned baseline, and dated performed work. | Reuse the split directly; readiness cites but does not replace those values. |
| Current A.21 gate-publication discipline | Separates readiness-looking displays from gate decisions. | Readiness may feed a gate, but gate passage belongs to A.21. |

### A.15.5:12 - Relations

- **Builds on:** `A.15`, `A.15.1`, `A.15.2`, `A.15.3`, `A.15.4`, `A.21`, `B.1.6`, `E.18`, `E.18.1`, and `E.24`; consumes current `A.2.8.PER` grant/non-prohibition/conflict refs as prospective inputs, and exercise/non-violation refs only as evidence about different dated work or in an explicit post-launch recheck after target work is actual.
- **Coordinates with:** `E.11.PUR` for recommended pattern use before readiness is selected, `E.10.MOVE` for readiness wording repair, `C.32.P2S` when readiness prepares work that realizes architecture-selected structures, and `A.3.4.P` when workflow or process wording is primarily transformation-situation wording.
- **Does not replace:** target `U.WorkPlan`, `SlotFillingsPlanItem`, `U.Work`, `GateDecision`, `A.15.4` local repair relation, resource aggregation, or transformation-flow structure.

### A.15.5:End

