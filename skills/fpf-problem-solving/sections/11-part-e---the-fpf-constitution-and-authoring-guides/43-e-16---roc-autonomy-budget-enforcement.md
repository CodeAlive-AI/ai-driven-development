## E.16 - RoC‑Autonomy Budget & Enforcement

**Intent.** Make an autonomy claim testable and enforceable through a published **AutonomyBudgetDecl**, guarded enactment, override SpeechActs with separation of duties, and a Work-anchored **AutonomyLedger**.
**Rule (summary).** If a claim calls a local system-role kind, Method, or Service autonomous, read it as a claim about Work a System may perform without continuous human direction. Authors **MUST**: (i) publish an `AutonomyBudgetDecl` that names the claim, working situation, scope, window, policy, budget, and override rule; (ii) say whether it is unscheduled/prospective, bound to a proposed action, or bound to actual enactment; (iii) gate Method steps with `requiresAutonomyBudget`; (iv) write an `AutonomyLedgerEntry` for admitted Work; (v) block on depletion until a `ResumeAutonomy` SpeechAct passes the guards, the declared separation-of-duties check, and the independent authority check; and (vi) surface the autonomy fields in UTS rows.

**Builds on:** A.2 / A.2.1 / A.2.5 / A.2.7 / A.15 / A.21; B.3; C.16; E.8; E.10; E.18; F.4; F.6; F.8; F.15; F.17.
**Coordinates with:** A.13 (Agential Role) and A.17/A.18/A.19/C.16/A.10 for current agency characterization, measurement, and evidence; planned C.9 (Agency Characteristic Profile) only as future consolidation; C.24 (Agent-Tools-CAL) where applicable; G.4, G.5, G.8, G.9, and G.10 (method authoring, selection, and shipping).

### E.16:1 - Problem Frame

A System that performs Work without continuous human direction must stay within declared safety, risk, resource, and remit limits and yield through the stated override path. The same need can be declared prospectively for a Method or Service before a particular performer or Work item exists. Without a uniform rule, an autonomy claim drifts into tacit norms, cannot be benchmarked or audited, and undermines selection (Part G) and publication (Part F).

### E.16:2 - Problem

* **Opaque autonomy.** Patterns assert “autonomous” behavior with no **budget** or **enforcement**.
* **Un‑gated execution.** Systems can perform Work beyond authority or risk limits.
* **Ad‑hoc overrides.** No standard **SpeechAct** for pausing/de‑scoping; SoD is unclear.
* **Non‑portable publication.** **UTS (Unified Term Sheet)** rows cannot surface autonomy‑critical data for parity or selection.

### E.16:3 - Forces

| Force                          | Tension                                                                  |
| ------------------------------ | ------------------------------------------------------------------------ |
| **Creativity vs Safety**       | Exploration autonomy vs hard constraints and override duties             |
| **Locality vs Comparability**  | A budget stays bound to its claim, working situation, scope, window, policy, and override rule; actual holders, assignments and authority enter a scheduled action check; a Work reference appears only when performance independently qualifies under A.15.1. |
| **Simplicity vs Auditability** | Lightweight authoring vs ledger‑grade evidence                           |
| **Autonomy vs SoD**            | Helpful self‑action vs separation‑of‑duties and human‑in‑the‑loop points |

#### E.16:3.1 - Bias-Annotation

**Bias considerations:** `Gov`, `Arch`, `Onto/Epist`, `Prag`, `Did`. **Scope:** Universal when wording about a local system-role kind, Method, or Service says that a System may perform Work involving unsupervised decision or actuation, and that Work is admitted through an `AutonomyBudgetDecl` plus Green-Gate. It is **not** aimed at purely assistive suggestion-only tools where a human confirms every action at the point of execution.

* **Gov.** Bias toward enforceable oversight (hard gates, SoD, canonical override SpeechActs). Mitigation: exploration autonomy is still allowed, but only inside an explicit budget and time window.
* **Arch.** Bias toward gate‑and‑ledger structure (Green‑Gate + Work‑anchored `AutonomyLedger`). Mitigation: `telemetrySpecRef` can scope what is emitted when full deltas are unnecessary.
* **Onto/Epist.** Bias toward typed, testable constraints (MM‑CHR tokens, explicit admissibility checks). Mitigation: budgets are optional‑field (`?`) so low‑risk contexts can start minimal and tighten over time.
* **Prag.** Bias toward measurable quotas may under‑express “soft” autonomy goals. Mitigation: pair `decision_tokens` with `risk_bands` to capture non‑counting limits.
* **Did.** Bias toward explicit mechanics increases authoring surface area. Mitigation: provide a default `AutonomyBudgetDecl` template and minimal harness cases in **F.15**.

### E.16:4 - Solution — **Rule‑of‑Constraints (RoC) for Autonomy**

This RoC **applies whenever** wording about a local system-role kind, Method, or Service claims that a System may perform Work involving unsupervised decision or actuation.

**E.16-S1 (Autonomy Budget - mandatory).**
Any autonomy claim **MUST** publish a named, versioned **AutonomyBudgetDecl**. A prospective declaration fixes what is being claimed and how later Work will be bounded; it does not pretend that a performer, assignment, Work item, or authority occurrence already exists. An action-bound declaration supplies the proposed-action and actual allocation references for A.21 permission to start. An enactment-bound declaration additionally refers to already admitted actual Work.

```
AutonomyBudgetDecl {
  id, version
  bindingState: prospective | action-bound | enactment-bound
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
  actionBinding?: {
    workEntryClaimRef: U.EpistemeRef                  // prospective A.21 decision subject
    boundedProposedActionRef: governed action or WorkPlan/action locator
    proposedActionIdentityRuleRef: exact local rule, including rescheduling/continuation
    intendedWindow: bounded intended execution/allocation window
    budgetConsumerHolderSystemRef: U.EntityRef constrained to U.System
    budgetConsumerSystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
    overrideAuthorityHolderSystemRef: U.EntityRef constrained to U.System
    overrideAuthoritySystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
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

An unscheduled `prospective` budget may omit actionBinding, enactmentBinding, nonexistent assignments and authority occurrences. Permission to start a scheduled action uses `action-bound` with its exact proposed action, work-entry claim, real holders/assignments and current independent authority. Use A.2.7's separately declared prospective incompatibility species for that allocation check. `enactment-bound` adds actual Work only after A.15.1 admission, retaining the applicable action/permission match. A request, schedule or pass result creates no Work. If authority rotates or a permission-relevant action/window changes, recheck before relying on the permission.

The holder Systems, local kinds, any separate System-classification judgments, assignment occurrences, Work, budget declaration, later override Work, authority relation, and separation-of-duties relation are different objects. A kind reference neither classifies a System nor creates an assignment; an assignment alone grants no authority.

**E.16‑S1.A (Scout / probe / commit partition for bounded specialization).**
When an autonomy-bearing method uses bounded specialization scouting, the budget declaration **MUST** keep scout budget, probe budget, and commit checkpoint as distinct control surfaces rather than collapsing them into one undifferentiated burn envelope. A successful probe does not by itself authorize a committed route, wider burn, or scope widening. Leaving probe state requires one explicit checkpoint decision through the declared guard or override path, with budget burn and residual budget recorded in the `AutonomyLedger`. `E.16` governs this budget partition plus guard and ledger enforcement; it does not replace the dyadic move of `A.15` or the `CheckpointReturn` plan semantics of `C.24`.
**E.16-S2 (Guarded enactment - Green-Gate).**
A Method step requiring autonomy **MUST** name the exact required local kind and `requiresAutonomyBudget: AutonomyBudgetDecl.id`. Green-Gate decides permission for the A.21 prospective work-entry claim and bounded action. It resolves:

* the action's artifact/subject, operation, target and intended window under its exact identity/continuation rule;
* the real prospective performer System and obtaining A.2.1 assignment whose holder/kind match the declaration, with the required A.2.5 state and any separate classification judgment;
* the actual authorizer/override-authority System and assignment, the applicable prospective incompatibility result, and the independent authority covering this action;
* applicable ClaimScope, qualification/accounting windows, remaining budget and every required guard.

A known prohibited allocation blocks the action before performance. Keep every required check present with its source outcome, including missing information, `unknown` or `notRun`, then apply the exact A.21 profile mapping. A required missing or unrun result may map only to `degrade` or `block` under an explicit rule; an unknown result retains its uncertainty and the policy-qualified consequence. Any accepted uncertainty must name its subject, tolerance, permitted bounded action, consequence and recheck/expiry condition. Reserve `abstain` for a gate that actually makes no decision and states the remaining decision route. Aggregate only after these mappings are known; a pass permits only the bounded action under the checked conditions. Resubmitting the same action changes no action identity. Rescheduling reopens window-sensitive permission even when the action-continuation rule preserves a continuing action. Work is admitted separately from actual performance history under A.15.1.

**E.16-S3 (Autonomy Ledger).**
Every actual Work item admitted under this budget **MUST** have an **AutonomyLedgerEntry**:

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

Existing budget and performance records may supply this declaration and ledger when they retain the required meanings, identities and references; no duplicate accounting store is required. The ledger is evidence about actual Work. When prior permission is relied on, cite its exact result and the policy-supported match from this performance to the previously bounded action; a shared request label is insufficient. The Work, its performer System, its A.2.1 assignment, and the `performedUnderAssignment` attribution remain separately recoverable. For reporting, use **Γ_work** (B.1.6) for the recorded resource values under the applicable accounting and overlap policy, and **Γ_time** (B.1.4) for the recovered temporal relations among the Work occurrences.

**E.16-S4 (Overrides - SpeechActs, authority, and separation of duties).**
Every budget **MUST** reference an `overrideProtocolRef` that defines the available SpeechActs:

* **PauseAutonomy(budgetId)** - stop autonomy-gated steps immediately;
* **ResumeAutonomy(budgetId)** - resume after the required checks;
* **NarrowAutonomy(budgetId, Δscope)** - apply stricter limits;
* **Escalate(budgetId)** - hand over through the declared override-authority path.

The declaration names the exact A.2.7 incompatibility species and its predicate. Before a proposed pause, resume, narrowing or escalation, identify that bounded override action, its real holder/assignment and independent authority. The target navigation Work may already exist; the proposed override is not yet override Work. Apply the actual-Work species when its condition concerns the existing target Work, or the separately declared prospective species when the policy concerns allocation to the proposed override action. Resolve both actual assignments, holders, relevant subject identity, windows and applicability; reject a known prohibited joint allocation. Different labels or assignment IDs alone do not establish separation.

Check authority for the proposed override independently. Once the override is actually performed and admitted under A.15.1, record its `overrideWork` ledger entry and policy-specified zero, negative or other budget delta. Match that performance to prior permission by the policy's exact action rule. The proposal and its pass result remain distinct from that performed SpeechAct Work.

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
* edition pins for the referenced local system-role kind, Method, CHR, and policies; and, when action-bound, its proposed-action and real allocation refs; when enactment-bound, the additional actual Work refs needed by the receiving use.
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

The declared A.2.7 relation is `NavigatorSupervisorIncompatibility`; its predicate prohibits the same System from holding both assignments for the same navigation Work during overlapping windows. The gate resolves both A.2.1 assignments and their holders and admits the override path because the actual pair does not match that prohibited case and the independent authority relation is current. The budget then supplies `action_tokens=10 k steps/day`, `risk_bands={maxSpeed <= 1.2 m/s, minDist >= 0.5 m}`, and `resource_caps={battery >= 20%}`. Ledger entries decrement the action budget and record distance checks. Depletion stops autonomous movement.

For a proposed pause/resume of that current navigation Work, name the override action and check its permission before it occurs. The navigation Work and its existing ledger remain unchanged by the proposal. Only the performed, independently admitted override adds override Work and its actual budget delta.

**Show-B (unscheduled, action-bound, then performed release).**
An unscheduled budget names the deployment/authorizer local kinds, policy, limits and prospective incompatibility species without inventing assignments or release Work. When release promotion is proposed, its local action rule fixes artifact `Release-E7`, target `Production-East`, operation `promote`, and intended window 14:00–14:15. Use its existing WorkPlan action locator if available; the rule otherwise identifies those values directly. Duplicate request IDs for these same values name the same proposed action.

`ReleaseDutyProspectiveIncompatibility` has the unordered kind pair {DeployerSystemRole, ReleaseAuthorizerSystemRole}. Under its adopted policy it prohibits the same actual holder's obtaining assignments to those kinds for the same proposed release action during overlapping allocation windows. Its applicability and meaning-changing policy edition are explicit. The kind relation obtains independently of whether anyone attempts a prohibited allocation. The illustrative `ReleaseEntryProfile-E1` requires allocation, authority, budget and the action’s other declared guards. It maps known prohibition, unknown allocation, and missing/unrun required allocation checks to `block`; satisfactory current results map to `pass`. Its hold consequence is to establish the allocation facts and recheck within the proposed action window. This is the case’s explicit profile, not an A.21 default.

| Case | Receiving result |
| --- | --- |
| No release scheduled | The budget remains prospective; no action or nonexistent assignments are filled. |
| Two distinct assignment IDs have the same System holder for this action and overlapping windows | The prospective predicate finds the prohibited allocation; the profile maps it to `block` before any release performance. Passing authority or budget cannot override it. |
| The overlap result is `unknown`, while authority and budget pass | `ReleaseEntryProfile-E1` maps unknown allocation to `block`; the aggregate of block, pass and pass is block. Hold promotion and establish the missing overlap facts. |
| The required allocation check has no result or was not run | Keep the missing/`notRun` check in the required set. This profile maps it to `block`; run or recover the check before reevaluating. |
| Different permitted holders, current independent authority, budget and all other required guards pass | A.21 permits the bounded promotion. No release Work is yet claimed. |
| The rejected release is resubmitted under a new request ID | The same-action rule preserves the subject, so the allocation check is not bypassed. |
| The window changes to 15:00–15:15 | The explicit continuation rule may retain the continuing release action when artifact, target and operation are unchanged and rescheduling is linked. Permission for 14:00–14:15 does not extend; evaluate the new window and allocation. |
| The permitted promotion is performed | A.15.1 identifies actual Work from its performance grounds. The ledger records that Work and policy-defined budget delta; a separate exact action match connects it to the applicable prior permission. |

The declaration's `decision_tokens=3/day` and `error-budget burn <= 2%/day` remain typed limits checked under their policy. This branch neither weakens the actual-Work incompatibility species nor treats a gate as Work admission.

### E.16:6 - Conformance Checklist (SCR - E.16-CC)

| ID            | Requirement |
| ------------- | ----------- |
| **E.16-CC-1** | Each autonomy claim cites a named/versioned budget with claim, consumer kind, situation, policy, scope/window, limits, override rule and exact A.2.7 species. Prospective budgets may omit actions/assignments; action-bound permission resolves the proposed action and real allocation/authority; enactment-bound adds independently admitted actual Work. |
| **E.16-CC-2** | Green-Gate decides the A.21 prospective work-entry claim and bounded action, resolving its identity/continuation, real holder/assignment/state, authority, scope/window, remaining budget, incompatibility and guards. Changed permission-relevant windows require recheck; request respelling does not create another action. |
| **E.16-CC-3** | Work admitted under autonomy **MUST** have an `AutonomyLedgerEntry` that identifies the Work, performer System, exact assignment, budget edition, deltas, and guard verdicts. |
| **E.16-CC-4** | A proposed override passes its applicable A.2.7 species and independent authority check before performance. An existing target Work is distinct from that proposal. Only a performed, A.15.1-admitted override is recorded as overrideWork with the applicable delta and policy-supported match to prior permission. |
| **E.16-CC-5** | Depletion **MUST** block autonomy-gated steps until `ResumeAutonomy` passes the actual-assignment separation-of-duties check, independent authority check, and ordinary guards. |
| **E.16-CC-6** | A UTS autonomy row carries the budget edition/state, guard policy, override protocol, scope/window, action/allocation refs when action-bound and actual Work refs when enactment-bound. |
| **E.16-CC-7** | When bounded specialization scouting is in scope, scout budget, probe budget, and commit checkpoint **MUST** stay explicit, and a successful probe **SHALL NOT** count as automatic committed rollout. |

### E.16:7 - Consequences

* **Testability.** Budget use is checkable against declared tokens/envelopes; Work-anchored ledger entries support audit; **PauseAutonomy** stops autonomy-gated steps.
* **Comparability.** UTS surfaces autonomy metadata for fair selection & parity.
* **Safety.** Guards are hard gates; depletion halts further autonomy‑gated Work.

#### E.16:7.1 - SoTA-Echoing — bind a budget decision to the proposed action

**Practice question.** Is an existing release policy and error-budget ledger enough to permit an autonomous promotion or override? The selected line reuses those controls while checking the proposed action, current allocation and authority, available budget and applicable guards before performance. It then records the actual Work and consumption. A serious lighter alternative gates releases solely by the existing service-level error-budget policy and records their effects afterward. That is sufficient when the release policy already supplies every action/authority condition needed by the use.

The [Google SRE Workbook's Example Error Budget Policy, 2018](https://sre.google/workbook/error-budget-policy/) is the concrete comparator: its four-week budget can freeze changes, explicitly excepts P0/security fixes and supplies an escalation route. **Adopt** policy-bound depletion and explicit exception handling in S2, S4 and S5. **Adapt** the budget to the exact autonomous action and current authority in S1–S2, rather than inferring those facts from the remaining service budget. The cited example is a bounded release policy, not a general autonomy standard or proof of the completeness of a particular gate.

Show-B gives the decisive case: a release can be within its error budget while the required allocation overlap remains unknown. Budget-only permission would miss that unresolved premise; the explicit ReleaseEntryProfile-E1 blocks until it is established. A changed window reopens the affected permission, while S3 records consumption only after actual performance. Show-A adds a real pause/resume authority and depletion stop. The same existing policy, ledger and allocation records can supply these inputs; a second accounting system adds no value when their meanings and exact references are already present. The extra work is resolving a current action/allocation question, not copying the budget into another form.

**Reject** treating a declared pause interface as proof that a learning agent has no incentive to resist interruption. [Orseau and Armstrong's Safely Interruptible Agents, revised October 2016](https://intelligence.org/files/Interruptibility.pdf) supplies the distinct learning-theoretic question and results under stated agent and learning assumptions. It does not establish E.16's runtime enforcement or override authority. S4 requires an effective override path; any stronger incentive or learning claim needs its own applicable analysis. Scout/probe/commit partitioning in S1.A is a local budget-control rule, with no claim here that unnamed agentic-search research proves its effectiveness.

At comparable operational effort, the selected line wins only when an action-sensitive premise could change permission: it uses the same budget evidence and adds that check before harm can follow the proposed action. For a policy already covering it, reuse the existing decision and accounting basis while respecting their currentness. Reopen when the action rule, authority/allocation policy, budget window or override mechanism changes, or when evidence shows a bypass or a cheaper control retaining the same required distinctions. No error-budget policy, interface declaration or interruption theorem alone establishes general autonomous-system safety.

#### E.16:7.2 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Why it fails | Repair |
| --- | --- | --- | --- |
| **Autonomy-by-label** | “Autonomous” is claimed but there is no `AutonomyBudgetDecl` or ledger | Autonomy becomes opaque; cannot be audited or compared | Require **E.16‑S1/S3**; reject publication without `AutonomyBudgetDeclRef` + version |
| **Soft gates** | Budget/guards only warn; enactment proceeds anyway | Violates Safety and SoD; makes budgets non-enforceable | Make Green‑Gate **blocking** on Core surface (**E.16‑S2**) |
| **Self-override** | The actual consumer and override assignments are missing, or their holder, actual-Work or proposed-action identity under the selected species, and window facts match the prohibited joint-allocation case in the declared A.2.7 predicate. | A label pair or two different assignment IDs does not establish separation of duties. | Resolve both exact A.2.1 assignments, apply the declared incompatibility predicate, reject a prohibited pair, and check the independent authority relation (**E.16-S4**). |
| **Budget bypass via “scale”** | Scaling preference relaxes guards or ignores caps | Undermines declared limits; breaks comparability | In ScaleLensPolicy, **guards/SoD must remain non‑weakened** (**E.16‑S7**) |
| **Untyped quotas** | Tokens/caps are recorded without units, or units are mixed | Ledger becomes non-comparable; audits become meaningless | Type budgets and deltas via **MM‑CHR (C.16)**; keep unitful rates/quotas |
| **Ledger-as-logging** | Logs exist but are not Work‑anchored (no workRef/budgetId/version or recoverable edition pins) | Evidence is non-portable; cannot support parity/refresh | Require `AutonomyLedgerEntry` attached to `U.Work` with workRef, budgetId, version, and the referenced declaration's edition pins |

### E.16:8 - Rationale & E‑/F‑/G‑links

* **E.10** — uses LEX‑BUNDLE: Scope via **ClaimScope (G)**, time via **Γ_time**, and **L‑AUTO** for autonomy wording.
* **Mint/reuse authority (policy-ids).** Mint/reuse authority is expressed via **F.8:8.1** (`PolicyIdRef`: `PolicySpecRef` + `MintDecisionRef?`) and explicit **GateCrossing** checks (**E.18**) evaluated by the active **GateProfile/GateFit** (**A.21**); no tier ladder is required.
* **Part F** — integrates with **F.4** Role Description (RCS includes *AgencyLevel*; RSG gates), **F.6** for exact performed-Work attribution after independent A.15.1 admission, **F.15** SCR/RSCR (harness includes depletion/override tests), **F.17** UTS (columns, incl. optional ScaleLens fields).
* **Part G** — **G.4/G.5**: method authors must declare budgets & guards; **G.9** parity includes autonomy consumption & violations; **G.10** shipping requires UTS autonomy fields.

### E.16:9 - Mini conformance checklist (cross-E-F; author's quick use)

1. **Declare the boundary:** name the autonomy claim, consumer local kind, working situation, policy, ClaimScope, window, budget, override-authority kind, and exact A.2.7 incompatibility relation.
2. **Identify the proposed action:** keep an unscheduled budget prospective; use action-bound for a scheduled action, its work-entry claim, real assignments/holders and independent authority. Apply the declared action identity and continuation rule.
3. **Gate permission to start:** apply the appropriate prospective allocation test, budget and guards to the bounded action. Recheck permission-relevant changes. A pass is not performed Work.
4. **Record actual Work:** after independent A.15.1 admission, emit the Work-anchored ledger entry, attribution and actual delta; relate it to prior permission through the exact policy-supported action match.
5. **Check override separately:** distinguish the existing target Work from the proposed override; apply the selected actual-Work or prospective-action species to the real assignments and applicable window, and independently test authority before performance.
6. **Publish what users need:** expose the budget edition, binding state, policy, override protocol, scope, and window in the UTS row.

These steps are the smallest complete route for a working Part F test harness; optional telemetry and selection lenses remain optional.

### E.16:End
