## E.16 - RoC‑Autonomy Budget & Enforcement

**Intent.** Make an autonomy claim testable and enforceable through a published **AutonomyBudgetDecl**, guarded enactment, override SpeechActs with separation of duties, and a Work-anchored **AutonomyLedger**.
**Rule (summary).** If a claim calls a local system-role kind, Method, or Service autonomous, read it as a claim about Work a System may perform without continuous human direction. Authors **MUST**: (i) publish an `AutonomyBudgetDecl` that names the claim, working situation, scope, window, policy, budget, and override rule; (ii) say whether it is prospective or bound to actual enactment; (iii) gate Method steps with `requiresAutonomyBudget`; (iv) write an `AutonomyLedgerEntry` for admitted Work; (v) block on depletion until a `ResumeAutonomy` SpeechAct passes the guards, the declared separation-of-duties check, and the independent authority check; and (vi) surface the autonomy fields in UTS rows.

**Builds on:** A.2 / A.2.1 / A.2.5 / A.2.7 / A.15 / A.21; B.3; C.16; E.8; E.10; E.18; F.4; F.6; F.8; F.15; F.17.
**Coordinates with:** A.13 (Agential Role) and A.17/A.18/A.19/C.16/A.10 for current agency characterization, measurement, and evidence; planned C.9 (Agency Characteristic Profile) only as future consolidation; C.24 (Agent-Tools-CAL) where applicable; G.4, G.5, G.8, G.9, and G.10 (method authoring, selection, and shipping).

### E.16:1 - Problem Frame

A System that performs Work without continuous human direction must stay within declared safety, risk, resource, and remit limits and yield through the stated override path. The same need can be declared prospectively for a Method or Service before a particular performer or Work item exists. Without a uniform rule, an autonomy claim drifts into tacit norms, cannot be benchmarked or audited, and undermines selection (Part G) and publication (Part F).

### E.16:2 - Problem

* **Opaque autonomy.** Patterns assert “autonomous” behavior with no **budget** or **enforcement**.
* **Un‑gated execution.** Methods can execute beyond authority or risk limits.
* **Ad‑hoc overrides.** No standard **SpeechAct** for pausing/de‑scoping; SoD is unclear.
* **Non‑portable publication.** **UTS (Unified Term Sheet)** rows cannot surface autonomy‑critical data for parity or selection.

### E.16:3 - Forces

| Force                          | Tension                                                                  |
| ------------------------------ | ------------------------------------------------------------------------ |
| **Creativity vs Safety**       | Exploration autonomy vs hard constraints and override duties             |
| **Locality vs Comparability**  | A budget stays bound to its claim, working situation, scope, window, policy, and override rule; actual holder, assignment, Work, and authority references appear only when the budget is enactment-bound. |
| **Simplicity vs Auditability** | Lightweight authoring vs ledger‑grade evidence                           |
| **Autonomy vs SoD**            | Helpful self‑action vs separation‑of‑duties and human‑in‑the‑loop points |

#### E.16:3.1 - Bias-Annotation

**Lenses tested:** `Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`. **Scope:** Universal when wording about a local system-role kind, Method, or Service says that a System may perform Work involving unsupervised decision or actuation, and that Work is admitted through an `AutonomyBudgetDecl` plus Green-Gate. It is **not** aimed at purely assistive suggestion-only tools where a human confirms every action at the point of execution.

* **Gov.** Bias toward enforceable oversight (hard gates, SoD, canonical override SpeechActs). Mitigation: exploration autonomy is still allowed, but only inside an explicit budget and time window.
* **Arch.** Bias toward gate‑and‑ledger structure (Green‑Gate + Work‑anchored `AutonomyLedger`). Mitigation: `telemetrySpecRef` can scope what is emitted when full deltas are unnecessary.
* **Onto/Epist.** Bias toward typed, testable constraints (MM‑CHR tokens, explicit admissibility checks). Mitigation: budgets are optional‑field (`?`) so low‑risk contexts can start minimal and tighten over time.
* **Prag.** Bias toward measurable quotas may under‑express “soft” autonomy goals. Mitigation: pair `decision_tokens` with `risk_bands` to capture non‑counting limits.
* **Did.** Bias toward explicit mechanics increases authoring surface area. Mitigation: provide a default `AutonomyBudgetDecl` template and minimal harness cases in **F.15**.

### E.16:4 - Solution — **Rule‑of‑Constraints (RoC) for Autonomy**

This RoC **applies whenever** wording about a local system-role kind, Method, or Service claims that a System may perform Work involving unsupervised decision or actuation.

**E.16-S1 (Autonomy Budget - mandatory).**
Any autonomy claim **MUST** publish a named, versioned **AutonomyBudgetDecl**. A prospective declaration fixes what is being claimed and how later Work will be bounded; it does not pretend that a performer, assignment, Work item, or authority occurrence already exists. An enactment-bound declaration supplies those actual references before the Green-Gate admits Work.

```
AutonomyBudgetDecl {
  id, version
  bindingState: prospective | enactment-bound
  autonomyClaimRef: U.EpistemeRef
  budgetConsumerSystemRoleKindRef: U.KindRef        // exact local kind required for the Work
  workingSituation: plain statement of the intended Work and its admission condition
  applicablePolicyRef: PolicyIdRef
  scope: ClaimScope
  qualificationWindow: Γ_time
  budget: {                                          // all typed via MM-CHR (C.16)
    action_tokens?     : Unitful quota / rate
    decision_tokens?   : Unitful quota / rate
    risk_bands?        : CHR vector with acceptance bands
    resource_caps?     : set of unitful caps (Γ_work categories)
    time_window?       : Γ_time accounting window & cadence
  }
  AdmissibilityConditionsId: PolicyIdRef             // Aut-Guard policy naming gates & penalties
  overrideProtocolRef: U.EpistemeRef                  // SpeechActs for pause/resume/narrow/escalate
  overrideAuthority: {
    authorizedOverrideSystemRoleKindRef: U.KindRef
    authorityPolicyRef: PolicyIdRef
    authorityRelationOccurrenceRef?: U.EntityRef      // independently obtaining direct relation
    separationOfDutiesRelationRef: U.RelationRef      // exact A.2.7 incompatibility relation
  }
  enactmentBinding?: {
    budgetConsumerHolderSystemRef: U.EntityRef constrained to U.System
    budgetConsumerSystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
    budgetedWorkRef: U.EntityRef constrained to U.Work
    overrideAuthorityHolderSystemRef: U.EntityRef constrained to U.System
    overrideAuthoritySystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
  }
  telemetrySpecRef?: U.EpistemeRef                     // what to emit into AutonomyLedger
  editionPins: { systemRoleKindRefs, MethodDescRef?, CHR refs, policy refs, ... }
}
```

In `prospective` state, `enactmentBinding` and `authorityRelationOccurrenceRef` may be absent. Before actual Work is admitted, publish or select an `enactment-bound` edition with every field in `enactmentBinding` and a current authority-relation occurrence. If the override authority rotates, refresh that binding before relying on it. Do not create an assignment or authority occurrence merely to fill the declaration.

The holder Systems, local kinds, any separate System-classification judgments, assignment occurrences, Work, budget declaration, later override Work, authority relation, and separation-of-duties relation are different objects. A kind reference neither classifies a System nor creates an assignment; an assignment alone grants no authority.

**E.16‑S1.A (Scout / probe / commit partition for bounded specialization).**
When an autonomy-bearing method uses bounded specialization scouting, the budget declaration **MUST** keep scout budget, probe budget, and commit checkpoint as distinct control surfaces rather than collapsing them into one undifferentiated burn envelope. A successful probe does not by itself authorize a committed route, wider burn, or scope widening. Leaving probe state requires one explicit checkpoint decision through the declared guard or override path, with budget burn and residual budget recorded in the `AutonomyLedger`. `E.16` governs this budget partition plus guard and ledger enforcement; it does not replace the dyadic move of `A.15` or the `CheckpointReturn` plan semantics of `C.24`.
**E.16-S2 (Guarded enactment - Green-Gate).**
A **Method step** that requires autonomy **MUST** list the exact required local system-role kind and `requiresAutonomyBudget: AutonomyBudgetDecl.id`. A **Work** instance is admissible only when the declaration is `enactment-bound` and the gate has resolved the actual values rather than inferred them from labels:

* `budgetConsumerHolderSystemRef` identifies the performer System, and `budgetConsumerSystemRoleAssignmentRef` resolves to the exact obtaining A.2.1 assignment whose holder and assigned kind match the declaration;
* `budgetedWorkRef` is the Work now being admitted and matches the declared working situation, ClaimScope, and qualification window;
* the assignment is in an enactable A.2.5 state; any separate classification judgment required by the gate is checked separately;
* the named override-authority System and assignment are current, and the independent authority relation covers the override Work allowed by the protocol;
* the budget ledger shows tokens and limits remaining for this declaration in the accounting window; and
* every guard in `AdmissibilityConditionsId` passes.

Failing any gate blocks enactment. Missing actual bindings remain missing; they are not repaired by turning a prospective declaration into fictional Work or assignment data.

**E.16-S3 (Autonomy Ledger).**
Every admitted Work item **MUST** have an **AutonomyLedgerEntry**:

```
AutonomyLedgerEntry {
  entryKind: budgetedWork | overrideWork
  workRef: U.EntityRef constrained to U.Work
  performerSystemRef: U.EntityRef constrained to U.System
  performedUnderSystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
  budgetId, version, time
  deltas: { action_tokensΔ?, decision_tokensΔ?, riskΔ?, resourceΔ? }
  guardVerdicts: { name -> pass|fail }
  overrideAuthorityRelationOccurrenceRef?             // required for overrideWork
  separationOfDutiesCheckResultRef?                    // required for overrideWork
  pathIds: { PathId, PathSliceId }                     // for G-suite parity/refresh
}
```

The ledger is evidence about the Work. The Work, its performer System, its A.2.1 assignment, and the `performedUnderAssignment` attribution remain separately recoverable. Fold the resulting entries under **Γ_work** and **Γ_time** for reporting.

**E.16-S4 (Overrides - SpeechActs, authority, and separation of duties).**
Every budget **MUST** reference an `overrideProtocolRef` that defines the available SpeechActs:

* **PauseAutonomy(budgetId)** - stop autonomy-gated steps immediately;
* **ResumeAutonomy(budgetId)** - resume after the required checks;
* **NarrowAutonomy(budgetId, Δscope)** - apply stricter limits;
* **Escalate(budgetId)** - hand over through the declared override-authority path.

The declaration names the exact A.2.7 incompatibility relation between the consumer and override-authority local kinds. At each override, the checking System separately resolves the two exact A.2.1 assignment occurrences, their holder Systems, the target Work, and their overlap window, then applies that relation's declared predicate. The override fails when the actual pair satisfies the predicate's prohibited joint-allocation case. Different labels or merely different assignment IDs do not prove separation of duties.

The same check independently confirms that the declared direct authority relation currently authorizes the override Work. Neither the local kind, assignment, policy name, nor incompatibility relation supplies that authority by itself. Every override SpeechAct is Work and receives an `overrideWork` ledger entry, including zero or negative budget deltas as the policy specifies.

**E.16-S5 (Depletion behavior).**
When a budget depletes - no tokens remain, an envelope is exceeded, or a cap is breached:

* block further autonomy-gated steps in the same accounting window;
* emit a **DepletionNotice** SpeechAct and either **Escalate** or **Park** as the policy says; and
* reopen the gate only after an admitted System performs **ResumeAutonomy** under its exact override-authority assignment, the A.2.7 predicate check over both actual assignments passes, the independent authority relation is current, and the ordinary guards pass.

**E.16‑S6 (Publication in UTS).**
A UTS row that carries an autonomy claim about Work described through a local system-role kind, **Method**, **Service**, or **Selector** **MUST** include:

* `AutonomyBudgetDeclRef` (id and version) and `bindingState`;
* `Aut-Guard policy-id (PolicyIdRef)`;
* `OverrideProtocolRef`;
* declared **Scope (G)** and **Γ_time** window;
* edition pins for the referenced local system-role kind, Method, CHR, and policies; and, when enactment-bound, the actual binding references needed by the receiving use.
* *(optional, if a scale preference is declared)* `ScaleLensPolicyRef` and `ScaleLensOptIn ∈ {OptedIn, Neutral, OptedOut}`.

**E.16‑S7 (Scale & selection — optional lens).**
When autonomy interacts with open‑ended search (C.18 and C.19), **budget consumption** and **guard violations** are **selection lenses** in Part G (G.5/G.9). Applying a **Scale‑Lens / Bitter‑Lesson** preference is **OPTIONAL**. Authors **MAY** declare a **ScaleLensPolicy** for the autonomy claim; when declared, it **MUST** state:
* **Trigger criteria** — evidence that expected utility‑of‑scale is monotonic/non‑saturating on held‑out tasks, and a threshold at which scaling beats structured heuristics.
* **Budget fit** — compute/latency/cost targets **within** the declared `AutonomyBudgetDecl` (Γ_time, resource_caps).
* **Safety invariants** — guards and SoD remain **non‑weakened** under scaling; no policy may bypass E.16 gates.
* **Fallback** — a degrade‑gracefully plan if scaling fails to clear the trigger criteria within budget.
If no **ScaleLensPolicy** is declared, selection remains **neutral** with respect to Bitter‑Lesson; RoC does **not** authorize ignoring scale‑safety guards under any policy.

### E.16:5 - Archetypal grounding (Tell-Show-Show; human-centric)

**Show-A (enactment-bound mobile robot).**
The autonomy claim names navigation Method `Navigate_v3`. Its enactment-bound budget names `NavigatorSystemRole` as the consumer kind, robot `Robot_R7` as holder, exact assignment `R7-NavigatorAssignment-2026`, and the current warehouse-navigation Work item. It also names the warehouse policy, ClaimScope and shift window, `FloorSupervisorSystemRole` as the override-authority kind, supervisor System `Mina`, her exact assignment, and the independently obtaining authority relation for pause and resume Work.

The declared A.2.7 relation is `NavigatorSupervisorIncompatibility`; its predicate prohibits the same System from holding both assignments for the same navigation Work during overlapping windows. The gate resolves both A.2.1 assignments and their holders and admits the override path because the actual pair does not match that prohibited case and the independent authority relation is current. The budget then supplies `action_tokens=10 k steps/day`, `risk_bands={maxSpeed <= 1.2 m/s, minDist >= 0.5 m}`, and `resource_caps={battery >= 20%}`. Ledger entries decrement the action budget and record distance checks. Depletion stops autonomous movement; it does not make either assignment or the incompatibility relation act.

**Show-B (prospective, then enactment-bound deployment).**
A prospective deployment budget names the autonomy claim, `DeployerSystemRole` and `ReleaseAuthorizerSystemRole`, the production-promotion situation, deployment policy, ClaimScope, daily window, guard set, and the exact A.2.7 incompatibility relation. It leaves holder Systems, assignments, deployment Work, and authority-relation occurrence empty because no release has been scheduled. Nothing is invented to make the template look complete.

When a release is scheduled, an enactment-bound edition names the deployment service System, its exact deployer assignment, the release Work, the authorizer System and assignment, and the independently obtaining release-authority relation. The receiving check tests the two assignments against the declared predicate for holder, same Work, overlap, and applicability; it then applies `decision_tokens=3/day`, `error-budget burn <= 2%/day`, and the ordinary deployment guards. A kind label or the notation `role A perpendicular role B` would not close either check.

### E.16:6 - Conformance Checklist (SCR - E.16-CC)

| ID            | Requirement |
| ------------- | ----------- |
| **E.16-CC-1** | Every autonomy claim **MUST** reference a named, versioned **AutonomyBudgetDecl** that states its binding state and identifies the claim, consumer local kind, working situation, policy, ClaimScope, qualification window, budget, override-authority local kind and policy, and exact A.2.7 separation-of-duties relation. A prospective declaration may omit actual holders, assignments, Work, and authority occurrence; all become mandatory in an enactment-bound edition before Work admission. |
| **E.16-CC-2** | A Method step that depends on autonomy **MUST** name the exact required local kind and `requiresAutonomyBudget`. Green-Gate **MUST** resolve the performer System, exact A.2.1 assignment, target Work, scope and window, assignment state, budget, and guards; any required classification judgment is separate. |
| **E.16-CC-3** | Work admitted under autonomy **MUST** have an `AutonomyLedgerEntry` that identifies the Work, performer System, exact assignment, budget edition, deltas, and guard verdicts. |
| **E.16-CC-4** | An override **MUST** be SpeechAct Work performed by an admitted System under an exact A.2.1 assignment. The receiving check **MUST** apply the named A.2.7 incompatibility predicate to both actual assignments, holders, target Work, overlap window, and applicability, reject a prohibited joint allocation, and independently confirm the authority relation. Kind labels or `role perpendicular role` notation are insufficient. |
| **E.16-CC-5** | Depletion **MUST** block autonomy-gated steps until `ResumeAutonomy` passes the actual-assignment separation-of-duties check, independent authority check, and ordinary guards. |
| **E.16-CC-6** | A UTS row that carries an autonomy claim about Work described through a local system-role kind, Method, or Service **MUST** include `AutonomyBudgetDeclRef`, binding state, Aut-Guard policy id, `OverrideProtocolRef`, ClaimScope, and Γ_time window; an enactment-bound row also exposes the actual binding references needed by its receiving use. |
| **E.16-CC-7** | When bounded specialization scouting is in scope, scout budget, probe budget, and commit checkpoint **MUST** stay explicit, and a successful probe **SHALL NOT** count as automatic committed rollout. |

### E.16:7 - Consequences

* **Testability.** Autonomy is measurable (tokens/envelopes), audit‑ready (ledger), and stoppable (SpeechActs).
* **Comparability.** UTS surfaces autonomy metadata for fair selection & parity.
* **Safety.** Guards are hard gates; depletion halts further autonomy‑gated Work.

#### E.16:7.1 - SoTA‑Echoing (post‑2015 practice alignment)

> Each item states **Adopt / Adapt / Reject**, and why. Vendor/tool tokens are kept as *informative*, not normative.

1. **Corrigibility & safe interruptibility (2016→).**
   **Adopt/Adapt.** Work on safe interruption and “off‑switch” incentives argues that capable systems should remain *stoppable* and should not be rewarded for resisting oversight (Orseau & Armstrong, 2016; Hadfield‑Menell et al., 2017). E.16 adapts this into canonical **PauseAutonomy / ResumeAutonomy** SpeechActs plus **SoD** and *hard* gating on depletion.

2. **AI safety as concrete operational hazards (2016→).**
   **Adopt.** “Concrete Problems in AI Safety” pushes instrumentation and testable safety constraints over informal assurances (Amodei et al., 2016). E.16 mirrors this by turning “autonomy” into a **budget + ledger + guards** specification that can be benchmarked and audited.

3. **SRE error budgets & “stop the line” operations (2016→).**
   **Adopt/Adapt.** Error‑budget practice treats reliability as a measurable envelope that gates risky change when depleted (Beyer et al., *Site Reliability Engineering*, 2016; Höller et al., *The Site Reliability Workbook*, 2018). E.16 adapts the idea into `risk_bands` and depletion behavior that blocks autonomy‑gated steps until governed resume.

4. **Risk management frameworks for AI systems (2023→).**
   **Adopt/Adapt.** Contemporary risk frameworks emphasize governance, continuous measurement, and traceable controls (NIST AI RMF 1.0, 2023; ISO/IEC 23894, 2023). E.16 adapts these into **UTS publication** + **Work‑anchored ledger evidence** for parity and audit.

5. **Policy‑as‑code and provenance gating (2019→).**
   **Adopt.** Modern supply‑chain integrity systems emphasize *policy‑checked actions with verifiable provenance* (in‑toto, 2019→; SLSA, 2021→). E.16 echoes the same principle for autonomy: **no autonomy‑gated enactment without passing declared guards and emitting ledger evidence** (without importing any specific tooling).

6. **Scaling laws & the Bitter Lesson (2019→).**
   **Adapt/Reject.** Empirical scaling work and the Bitter Lesson motivate considering compute‑heavy search when returns are monotonic (Sutton, 2019; Kaplan et al., 2020). E.16 adapts this into an **optional** ScaleLensPolicy (E.16‑S7) constrained by the *same* budgets and guards, and **rejects** any interpretation that lets “scale” bypass safety gates.

7. **Budgeted specialist acquisition and checkpointed exploitation (2024→).**
   **Adopt/Adapt.** Recent agentic tool-use, self-play, and open-ended search lines reinforce that the competition variable is time or budget to threshold plus fast exploitation after a viable route is found. E.16 adapts this into distinct scout/probe/commit control surfaces and rejects any reading where early probe success authorizes rollout without an explicit checkpoint.

#### E.16:7.2 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
| --- | --- | --- | --- |
| **Autonomy-by-label** | “Autonomous” is claimed but there is no `AutonomyBudgetDecl` or ledger | Autonomy becomes opaque; cannot be audited or compared | Require **E.16‑S1/S3**; reject publication without `AutonomyBudgetDeclRef` + version |
| **Soft gates** | Budget/guards only warn; enactment proceeds anyway | Violates Safety and SoD; makes budgets non-enforceable | Make Green‑Gate **blocking** on Core surface (**E.16‑S2**) |
| **Self-override** | The actual consumer and override assignments are missing, or their holder, Work, and window facts match the prohibited joint-allocation case in the declared A.2.7 predicate. | A label pair or two different assignment IDs does not establish separation of duties. | Resolve both exact A.2.1 assignments, apply the declared incompatibility predicate, reject a prohibited pair, and check the independent authority relation (**E.16-S4**). |
| **Budget bypass via “scale”** | Scaling preference relaxes guards or ignores caps | Undermines declared limits; breaks comparability | In ScaleLensPolicy, **guards/SoD must remain non‑weakened** (**E.16‑S7**) |
| **Untyped quotas** | Tokens/caps are recorded without units, or units are mixed | Ledger becomes non-comparable; audits become meaningless | Type budgets and deltas via **MM‑CHR (C.16)**; keep unitful rates/quotas |
| **Ledger-as-logging** | Logs exist but are not Work‑anchored (no workId/budgetId/version/pins) | Evidence is non-portable; cannot support parity/refresh | Require `AutonomyLedgerEntry` attached to `U.Work` with ids, versions, and edition pins |

### E.16:8 - Rationale & E‑/F‑/G‑links

* **E.8** — follows the pattern template (Context → Problem → Forces → Solution → Grounding → CC → Consequences).
* **E.10** — uses LEX‑BUNDLE: Scope via **ClaimScope (G)**, time via **Γ_time**, no “validity/process/actor/agent‑as‑noun” language; new lexical rule **L‑AUTO** added in edits below.
* **Mint/reuse authority (policy-ids).** Mint/reuse authority is expressed via **F.8:8.1** (`PolicyIdRef`: `PolicySpecRef` + `MintDecisionRef?`) and explicit **GateCrossing** checks (**E.18**) evaluated by the active **GateProfile/GateFit** (**A.21**); no tier ladder is required.
* **Part F** — integrates with **F.4** Role Description (RCS includes *AgencyLevel*; RSG gates), **F.6** Role Assignment & Enactment (Green‑Gate), **F.15** SCR/RSCR (harness includes depletion/override tests), **F.17** UTS (columns, incl. optional ScaleLens fields).
* **Part G** — **G.4/G.5**: method authors must declare budgets & guards; **G.9** parity includes autonomy consumption & violations; **G.10** shipping requires UTS autonomy fields.

### E.16:9 - Mini conformance checklist (cross-E-F; author's quick use)

1. **Declare the boundary:** name the autonomy claim, consumer local kind, working situation, policy, ClaimScope, window, budget, override-authority kind, and exact A.2.7 incompatibility relation.
2. **Bind only when real:** mark an early declaration `prospective`; before admitting Work, use an `enactment-bound` edition with actual holder Systems, A.2.1 assignments, Work, and authority-relation occurrence. Invent none of them.
3. **Gate the Work:** resolve the exact performer, assignment, Work, state, remaining budget, and guards.
4. **Record the Work:** emit an `AutonomyLedgerEntry` with performer and assignment attribution for every admitted budgeted or override Work item.
5. **Check override separately:** apply the A.2.7 predicate to both actual assignments and the target Work and window, reject a prohibited joint allocation, and independently test override authority.
6. **Publish what users need:** expose the budget edition, binding state, policy, override protocol, scope, and window in the UTS row.

These steps are the smallest complete route for a working Part F test harness; optional telemetry and selection lenses remain optional.

### E.16:End

