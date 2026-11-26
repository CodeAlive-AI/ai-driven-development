## A.2.8.PER - Granted Permission, Exercise, and Non-Prohibition

> **Type:** Definitional ontic support pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2.8.PER:0 - Use this when

Use this pattern when a policy, approval, permit, system-role rule, boundary claim, readiness check, or later work use needs to distinguish five questions:

- whether a sufficiently complete current frame supports a `NonProhibitionFinding@Context`;
- whether a valid grant currently obtains as `GrantedPermissionRelation@Context`;
- whether dated matching work exercises it through `PermissionExerciseRelation@Context`;
- whether checked actual work supports a `NonViolationFinding@Context`; and
- whether an incompatible current grant and norm require `PermissionNormConflictFinding@Context`.

First establish what makes the action permissible for this beneficiary, scope and time. A standing rule may permit the action directly when its conditions hold. Apply that rule to the case. For a grant already issued to a class of beneficiaries, identify that grant and establish that the present beneficiary qualifies. A positive answer by either route can settle the practical question without issuing a fresh permit. An instrument can also grant one right to several named parties together. Apply its terms to their joint action (§4.2). Use §§4.3–4.6 for a grant, exercise or finding that satisfies the corresponding declaration.

**Not this pattern when.** Use `A.2.8` for one actual bearer's obligation, recommendation-as-duty, or prohibition; `A.2.9` for the communicative work that institutes or revokes a grant; `A.6.B` for L/A/D/E classification; `A.15.5` for work-entry readiness; `A.21` for gate decisions; and `A.15.1` for the identity and result of performed work.

When the account asserts a particular dated Work occurrence, identify its performer through A.13 and admit the Work independently through A.15.1. Use F.6 where the relevant declaration consumes precise attribution to a covering assignment; the grantor, beneficiary and decision branches below state those conditions.

### A.2.8.PER:1 - Problem frame

Permission-looking language often compresses unlike values. “No rule forbids it” may be an incomplete search result. “The permit allows it” may refer to a document, an issuing act, or an enduring relation. “We used the permit” may mean only that a badge was visible, while no matching work occurred. A green gate can also look as if it defeated a current prohibition.

Select the permission question for the beneficiary, action specification, normative-frame edition, ClaimScope, intended use and window. An affirmative rule and the facts that bring a beneficiary within it can establish a right directly. A search finding no prohibition supplies a different ground. The act, permit episteme, publication carrier, evidence relation, admissibility predicate, readiness relation, gate decision, actual Work, and work result remain distinct and are handled under their respective subject patterns.

### A.2.8.PER:2 - Problem

How can FPF represent positive permission without turning it into an obligation modality, absence-of-evidence claim, permit document, gate result, readiness label, capability, or performed action?

A conforming account must make weak and strong permission different, keep grant occurrence identity inspectable, connect only eligible matching work to a current grant, keep both exercise and non-exercise from establishing a frame-relative non-violation finding, and expose same-scope normative conflicts instead of resolving them by display or wording.

### A.2.8.PER:3 - Forces

| Force | Tension |
|---|---|
| Latitude vs duty | Permission makes an action allowable; it does not require the action. |
| Weak evidence vs world relation | A complete-frame search can support non-prohibition, while an incomplete search is unresolved. |
| Enduring grant vs instituting act | A speech act can ground a permission without being the continuing relation. |
| Beneficiary variety vs kind discipline | System-role kinds, exact assignment occurrences, and parties all occur in practice, but one generic beneficiary U-kind would erase their different eligibility tests. |
| Current grant vs actual exercise | A grant may obtain without work; work may occur without matching or exercising the grant. |
| Local policy vs visible artifacts | A permit or gate display is easy to see, but scope, window, currentness, revocation, and precedence decide use. |

### A.2.8.PER:4 - Solution

#### A.2.8.PER:4.1 - Keep the permission objects separate

Use the object warranted by the current claim:

- `NonProhibitionFinding@Context` is a frame-relative episteme returned before action when a sufficiently complete current normative frame contains no applicable prohibition.
- `GrantedPermissionRelation@Context` is an enduring strong permission instituted by the act or combination of acts an exact policy requires. An entitlement conferred directly by a standing rule can be established from that rule and the case facts without a claim about a separate grant.
- `PermissionExerciseRelation@Context` connects actual dated work to one obtaining grant occurrence when action and beneficiary eligibility match.
- `NonViolationFinding@Context` is a frame-relative episteme about actual work that instantiates no applicable prohibition in the checked frame.
- `PermissionNormConflictFinding@Context` is an episteme exposing an incompatible current grant and prohibition or commitment over matching content, scope, and window.

For an entitlement conferred directly by a standing rule, establish the applicable rule and the case facts. If the question concerns exercise, check who acted and whether the actual action met its conditions. When another applicable norm gives an incompatible answer, apply the governing precedence rule or an authorized resolution. Where neither settles the conflict, the answer for that use remains open. The grant-specific declarations below concern a permission instituted by an act. A finding of non-prohibition does not institute a grant. A grant alone leaves its exercise open. To establish a violation, identify the norm the action breached.

#### A.2.8.PER:4.2 - Use the closed beneficiary reference family

```text
PermissionBeneficiaryRef ::=
  exactly one branch is present:
    beneficiarySystemRoleKindRef?: U.KindRef resolving to one exact local system-role kind
    beneficiarySystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment
    beneficiaryPartyRef?: PartyRef
```

The entity designated by the grant is its beneficiary. Apply the exercise-eligibility test for its reference branch:

- `beneficiarySystemRoleAssignmentRef` names one assignment occurrence and its declared species and applies only to that occurrence.
- `beneficiarySystemRoleKindRef` names one exact local system-role kind; the policy states which current assignments to that kind make an actual performer eligible.
- `PartyRef` covers work only when its exact performer or on-behalf-of relation satisfies the policy. Shared naming or organizational membership is insufficient.

This closed reference union describes one beneficiary. An instrument can instead grant one right to several named parties jointly. Apply its conditions to the named parties and to the action required of them together. Use a common `PartyRef` when the instrument designates that party. Naming several parties in one instrument does not by itself entitle each to act alone. The applicable subject pattern governs a beneficiary meaning outside this union.

#### A.2.8.PER:4.3 - Record weak permission and non-violation as findings

```text
NonProhibitionFinding@Context <: U.Episteme
  beneficiaryRef: PermissionBeneficiaryRef
  permittedActionSpecificationRef: U.EpistemeRef
  normativeFrameRef: U.EpistemeRef
  frameCurrentnessResultRef: U.EpistemeRef
  frameCompletenessForUseResultRef: U.EpistemeRef
  scope: U.ClaimScope
  intendedUse:
  evaluationWindow: QualificationWindowPolicy
  checkedProhibitionAddresses: set<ClaimAddress>
  result: nonProhibited | unresolved
  evaluationWorkRef?: WorkRef             # when the account asserts this dated evaluation Work

NonViolationFinding@Context <: U.Episteme
  workRef: WorkRef
  performerSystemRoleAssignmentRefs?: set<U.RelationRef constrained to U.SystemRoleAssignment> # when the checked norm uses precise assignment attribution
  onBehalfOfRelationOccurrenceRef?: U.RelationRef constrained to the direct on-behalf-of relation kind # one mandate covering the relevant contribution
  representedContributions?: contributing performers, each linked to its part, the party represented and its applicable on-behalf-of relation(s)
  normativeFrameRef: U.EpistemeRef
  frameCurrentnessResultRef: U.EpistemeRef
  frameCompletenessForUseResultRef: U.EpistemeRef
  scope: U.ClaimScope
  intendedUse:
  evaluationWindow: QualificationWindowPolicy
  checkedProhibitionAddresses: set<ClaimAddress>
  result: nonViolating | unresolved
  evaluationWorkRef?: WorkRef             # when the account asserts this dated evaluation Work
```

`nonProhibited` and `nonViolating` are admissible only when the named frame is current and explicitly sufficiently complete for the intended use. Otherwise the finding is `unresolved`. Neither finding institutes permission or proves absence outside its frame.

Every `ClaimAddress` in this pattern means the reusable `C.2.1 ClaimAddress`: an exact episteme-edition reference plus an intrinsic claim identity declared by that edition's ClaimGraph. A heading, row number, file location, or printed token is insufficient.

For a `NonViolationFinding@Context`, use the facts on which the checked prohibition turns. If it concerns representation, link each relevant contribution to the performer, the party represented and the independently established mandate covering that part. One on-behalf-of relation suffices when it covers the claim. A performer can act for different parties under different mandates. Cite a covering assignment and its declared species where the norm requires assignment-bound attribution. If only the conduct or resulting state matters, the evidence can establish that fact without identifying a representative. The Work under examination and the currentness and sufficient completeness of the frame still need grounds. Identify a separate evaluation Work when its occurrence is also asserted.

#### A.2.8.PER:4.4 - Declare the strong granted-permission relation

```text
GrantedPermissionRelation@Context <: U.Relation

RelationSignature:
  PermissionBeneficiarySlot:
    SlotKind: PermissionBeneficiarySlot
    ValueKind: U.Entity
    refMode: PermissionBeneficiaryRef
  PermittedActionSpecificationSlot:
    SlotKind: PermittedActionSpecificationSlot
    ValueKind: U.Episteme
    refMode: U.EpistemeRef

semanticDirection: PermissionBeneficiarySlot -> PermittedActionSpecificationSlot

RelationOccurrenceGroundAndQualifiers:
  // Use the direct fields for one act under one granting assignment, or the grouped form.
  ( institutingSpeechActRef: SpeechActRef,
    grantorSystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment
  | institutingActs: non-empty set of SpeechActRef, each with its granting contributions under A.2.9:4.1–4.5 )
  grantValidityPolicyRef: U.EpistemeRef
  scope: U.ClaimScope
  validityWindow: QualificationWindowPolicy
  revocationOrSupersessionRef?: SpeechActRef       // one act sufficient under the policy
  revocationOrSupersessionActs?: set<SpeechActRef>  // acts required together, when applicable
```

The beneficiary and permitted-action specification are participants. The instituting acts, granting capacities and authority, policy, ClaimScope, validity window and any effective revocation supply grounds or qualifiers.

Apply the current grant-validity rule to the actual communication. If one delegate can grant permission, establish the act and the mandate covering the delegated decision. If several participants issue one declaration, recover their joint performance under A.2.9. If distinct approvals are required together, identify each act and establish that their contents, order where material, scopes and times meet the same rule. Keep each required granting assignment and its holder with that holder’s act, including several assignments of one holder when relied on. Establish the authority each contribution needs. A record that merely transmits the decisions can supply evidence about them. Its sender is a grantor only if the rule gives that sender an effective granting contribution.

The relation obtains while beneficiary applicability, policy continuation, scope, and window hold and no valid revocation or supersession ends it.

Identify an occurrence from its policy-required instituting act or combination, exact beneficiary reference and reference kind, action-specification edition, policy edition, ClaimScope and effective interval. Use one act reference for a joint act even if several performers took part. The permission starts when all conditions for its effectiveness hold. Beneficiary change, renewal, materially changed action specification, a non-carried policy edition or effective revocation ends or splits the occurrence. A policy edition preserves it through an explicit satisfied carry-forward rule. Apply the policy's own conditions for revocation, including any required combination of acts.

#### A.2.8.PER:4.5 - Declare actual exercise

```text
PermissionExerciseRelation@Context <: U.Relation

RelationSignature:
  ExercisingWorkSlot:
    SlotKind: ExercisingWorkSlot
    ValueKind: U.Work
    refMode: WorkRef
  GrantedPermissionOccurrenceSlot:
    SlotKind: GrantedPermissionOccurrenceSlot
    ValueKind: U.Relation
    refMode: U.RelationRef constrained to GrantedPermissionRelation@Context
      // resolves to one exact obtaining grant occurrence

semanticDirection: ExercisingWorkSlot -> GrantedPermissionOccurrenceSlot

RelationOccurrenceQualifiers:
  // For a single exercising contribution, use its applicable direct reference.
  beneficiarySystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment
  onBehalfOfRelationOccurrenceRef?: U.RelationRef constrained to the direct on-behalf-of relation kind
  exercisingContributions?: qualifying performers, each with its part in the permitted action and the eligibility grounds the policy requires
  exerciseScope: U.ClaimScope
  exerciseInterval: QualificationWindowPolicy
```

Decide exercise from two questions. Did this dated Work instantiate the permitted action? Did the contribution or combination that counts as exercising the permission meet its beneficiary conditions?

For a `beneficiarySystemRoleAssignmentRef` grant, establish that the named assignment covers the relevant contribution and that its holder performed it. For a `beneficiarySystemRoleKindRef` grant, establish the eligible assignment to that kind for each contribution that the rule requires. For a `beneficiaryPartyRef` grant, establish action by the party or the policy-recognized on-behalf-of relation for its representative. Use the direct references for a single contribution. For joint exercise, group each exercising contribution with its performer, action and qualifying capacity. A contributor providing technical support can enable the exercise without needing the entitlement to exercise the right personally.

Test the action and beneficiary predicates over this Work, grant, action specification and the relevant performers and capacities. If either predicate fails, the exercise relation does not obtain. Cite a separate evaluation or evidence item when an assurance use requires it.

If an action requires several distinct grants, check coverage under each and the rule requiring them together. Each exercise relation still refers to one grant. The exercise relation obtains only when those two predicates hold, the grant obtains throughout the exercise interval, and the work remains in scope. The work is a satisfier of permitted action content. Judge any obligation-satisfaction or discharge claim under the separate evaluation or compliance rule (A.2.8:4.6). The work consumes the grant only when the named policy explicitly makes it single-use or quota-bound.

Non-exercise leaves a grant unused; it continues while the §4.4 conditions hold. Neither non-exercise nor exercise establishes `NonViolationFinding@Context` without the separate checked-frame evaluation. Work outside the action specification, beneficiary eligibility, scope or window does not exercise the grant; any further consequence follows from the applicable prohibition, commitment, admissibility or Work-related predicate.

When a decision is required, identify its result and use the relevant decision rule; an asserted dated decision Work follows the performer-and-Work route above and any assignment or authority conditions required by that rule.

#### A.2.8.PER:4.6 - Expose conflict without inventing precedence

```text
PermissionConflictResolutionResultRef ::= U.EpistemeRef
  // resolves only to PermissionConflictResolutionResult@Context

PermissionConflictResolutionResult@Context <: U.Episteme
  conflictFindingRef: U.EpistemeRef
  governingPrecedencePolicyRef: U.EpistemeRef
  // Direct fields for one decision by one authorized holder, or the grouped form.
  ( resolutionWorkRef: WorkRef,
    deciderSystemRef: U.EntityRef,
    deciderSystemRoleAssignmentRef: U.RelationRef constrained to U.SystemRoleAssignment,
    decisionAuthorityRelationOccurrenceRef: U.RelationRef constrained to the direct decision-authority relation kind
  | resolutionContributions: decision Work occurrences, each with its deciding performers, relied-on assignments and authority relations as required by the policy )
  selectedGrantOccurrenceRef?: U.RelationRef constrained to GrantedPermissionRelation@Context
  selectedNormClaimAddress?: ClaimAddress
  effectiveScope: U.ClaimScope
  effectiveWindow: QualificationWindowPolicy
  reopenConditionClaimAddress: ClaimAddress

PermissionNormConflictFinding@Context <: U.Episteme
  grantedPermissionOccurrenceRef: U.RelationRef constrained to GrantedPermissionRelation@Context
  conflictingNormClaimAddress: ClaimAddress
  overlapScope: U.ClaimScope
  overlapWindow: QualificationWindowPolicy
  governingPrecedencePolicyRef?: U.EpistemeRef
  applicablePrecedenceRuleAddress?: ClaimAddress
  decisionAuthorityRelationOccurrenceRef?: U.RelationRef constrained to the direct decision-authority relation kind
  resolutionWorkRef?: WorkRef   // optional single decision detail; the resolution result carries any joint basis
  resolutionResultRef?: PermissionConflictResolutionResultRef
  blockedWorkOrRelianceRef: U.EntityRef
  disposition: unresolved | settledByApplicableRule | settledByDecisionResult
  reopenConditionClaimAddress: ClaimAddress
```

Create the finding only when the grant and current prohibition or commitment concern the same beneficiary/action content, overlapping scope/window, and incompatible practical conclusions. Check that match directly from the two claims and their participants. Permission and an obligation to perform the same action are not automatically in conflict.

An unresolved finding may omit `governingPrecedencePolicyRef` when no governing precedence policy has been identified. Keep the disposition unresolved and retain the missing input and what would reopen the question. A settled finding identifies the governing policy and the applicable rule or independently grounded decision result. For a proposed action, `blockedWorkOrRelianceRef` identifies the action or its WorkPlan under the applicable subject rule; it does not designate a future Work occurrence.

Resolve the conflict through exactly one of two branches:

1. **The current policy already decides.** `applicablePrecedenceRuleAddress` cites the policy claim whose stated conditions match this beneficiary, action, scope, and window. Set `settledByApplicableRule` only when that rule itself selects which claim governs the blocked use.
2. **A decision is required.** Recover the decision or combination that the policy empowers to settle this conflict. Establish the deciding participants, their actual decision Work, and the capacities and mandates needed for each contribution. One authorised body may make one decision. Where distinct approvals are jointly required, establish each and their combination on the disputed use. The grounded result of the required Work must select the grant or the conflicting norm for the stated scope and window.

`PermissionConflictResolutionResult@Context` records that decision result. Exactly one of `selectedGrantOccurrenceRef` or `selectedNormClaimAddress` is filled. In the direct form, the named assignment must cover the decision Work and have the deciding system as holder. Establish the authority to make that decision independently. In the grouped form, associate each contribution with its actual Work and authority. Check that all the policy’s decision conditions obtain before using the combined result.

If no policy rule decides and no such current result exists, the disposition remains `unresolved`, even when a responsible office or system-role kind is named. Permit text, readiness, or a passing gate does not defeat the prohibition.

#### A.2.8.PER:4.7 - Keep the handshakes narrow

| Neighboring object | Handshake |
|---|---|
| Grant or revoke act | Use A.2.9 for each actual communicative Work and any assignment-bound attribution. A grant can require one declaration by several participants or several distinct approvals. Cite the separately obtaining grant in the applicable `institutes.permissions` entry when the rule-required combination is complete. Establish revocation from its own policy conditions. |
| Permit episteme and carrier | Use `C.2.1` for claims about the permission, `E.17` for a source-backed publication face, `G.11` for source currentness and publication refresh, and `A.10` for evidence used in reliance. Use `E.24.PUB` when the publication occurrence, form, or carrier identity matters. |
| Duty or prohibition | `A.2.8 U.Commitment`; permission remains outside its modality family. |
| Boundary claim or entry predicate | `A.6.B` classifies the claim; an `A-*` predicate may consume a separately established current permission result. |
| Work plan and readiness | `A.15.2` is the pattern for the `U.WorkPlan`; `A.15.5` may cite a separately established permission/conflict result as one readiness input. |
| Gate decision | Use `A.21` for a gate outcome, citing the separate current grant or conflict result whenever its profile requires one. |
| Work and result | Identify the dated Work under `A.15.1`. For an entitlement under a standing rule, establish who qualifies and whether the action met the rule. For a right conferred by an instrument, apply its scope, interval and conditions to what the named beneficiary or joint beneficiaries did. Use the §4.5 exercise relation for a grant represented under §4.4. Capability, readiness, safety, success and result quality require their own grounds. |

### A.2.8.PER:5 - Archetypal Grounding

**Assignment, permission, access, and authority.** `AdminAssignment` is a declared `U.SystemRoleAssignment` species. Occurrence `AdminAssignment-4` has admitted System `ServiceOperator-4` as holder and `AdminSystemRole` as assigned-kind value. That fact alone establishes no grant, access, or decision authority. A policy-valid speech act can separately institute one `GrantedPermissionRelation@Context` for `AdminSystemRole`, `RestartServiceActionSpec`, the declared scope, and the declared window. Matching dated Work exercises that grant only through a separate `PermissionExerciseRelation@Context`.

If service access is claimed, cite its domain access predicate and participants; when no such predicate is available, return `A.6.RCD missing-governor[direct service-access relation]`. Permission, exercise, access, authority, assignment, and Work therefore remain separate.

**Strong grant and exercise.** `PlantPermissionGrantorAssignment` is a declared `U.SystemRoleAssignment` species. Occurrence `MaintenanceCoordinator-A@DayShift` has admitted System `MaintenanceCoordinator-A` as holder, and that System performs a policy-valid grant speech act under the assignment. The act institutes `MaintenanceCalibrationGrant-2026-07-19 : GrantedPermissionRelation@Context` for `MaintenanceTechnicianSystemRole` to run `CalibrationProcedure-v3` during one service window. Its beneficiary uses `beneficiarySystemRoleKindRef`.

`PlantCalibrationTechnicianAssignment` is another declared species. Occurrence `Tech-17@Shift-B` has admitted technician System `Tech-17` as holder and `MaintenanceTechnicianSystemRole` as assigned-kind value. `Tech-17` performs dated `CalibrationWork-17B` under that assignment. The Work instantiates `CalibrationProcedure-v3` within the grant's zone, window, and scope, so the action-match predicate holds. The assignment covers the Work and satisfies the policy's eligibility rule for that kind, so the beneficiary predicate holds.

`CalibrationExercise-17B : PermissionExerciseRelation@Context` therefore connects `CalibrationWork-17B` to `MaintenanceCalibrationGrant-2026-07-19`, cites `beneficiarySystemRoleAssignmentRef=Tech-17@Shift-B`, and states the Work interval and scope. The assignments supply holder and assigned-kind facts for the grant and Work attribution; any required authority relation obtains independently. The grant remains current for the rest of the window because the policy is not single-use. Claims about obligation, readiness, capability, gate passage, a safe result, or successful calibration need their own grounds.

Suppose instead that an archive and a foundation each control a right needed to exhibit the same recording. Their rule requires both approvals for this exhibition. An archive officer forwarding the foundation’s signed approval can establish receipt of that approval. To open the exhibition on this basis, establish the archive’s approval too, for the same edition, use and period. If both parties had empowered one delegate to authorize this exhibition, that delegate’s covered decision could suffice. A technician mounting the projector does not exercise either party’s granting power.

**Weak finding.** A policy reviewer checks a named, current, sufficiently complete plant-access frame and finds no prohibition applicable to the exact system-role kind, action specification, zone, and window. The result is `NonProhibitionFinding@Context(result=nonProhibited)`, not an instituted grant. If the emergency-policy register cannot be checked, the result is `unresolved`.

**Actual-Work non-violation.** After `CalibrationWork-17B` is performed, `CalibrationComplianceEvaluation-17B : U.Work` checks that Work against `PlantCalibrationNormativeFrame-2026-07-19-e3`, whose currentness and sufficient completeness for the technician, procedure, zone, and service-window use are named and whose applicable prohibitions are checked. The result is `NonViolationFinding@Context(workRef=CalibrationWork-17B, performerSystemRoleAssignmentRefs={Tech-17@Shift-B}, normativeFrameRef=PlantCalibrationNormativeFrame-2026-07-19-e3, evaluationWorkRef=CalibrationComplianceEvaluation-17B, result=nonViolating)`. The covering assignment already relates the performer system to the beneficiary system-role kind.

The separate exercise relation shows which grant the Work exercised; exercise alone does not establish non-violation, and non-exercise alone does not establish it either. If the frame is stale or insufficiently complete for this use, the non-violation result is `unresolved`.

**Conflict and non-use.** The system-role-kind-level calibration grant still obtains under §4.4 while `ContaminatedZoneEntryProhibition-7` forbids the same beneficiary and calibration action in Zone 7 during an overlapping interval. In the direct-rule case, `EmergencyCalibrationPrecedencePolicy-e5` contains applicable claim `CZ7-Prohibition-Overrides-CalGrant`. The rule's conditions match, so the finding is `settledByApplicableRule`, cites that rule, and returns “do not enter Zone 7” for the blocked Work.

In a discretionary Zone 8 case, `PlantSafetyDecisionAssignment` is a declared `U.SystemRoleAssignment` species. Occurrence `SafetyDirector-3@EmergencyShift` has admitted System `SafetyDirector-3` as holder, and that System performs `CalibrationConflictDecisionWork-8` under the assignment. The separately obtaining `PlantEmergencyExceptionAuthority-8` relation authorizes that decision, and current `CalibrationConflictResolutionResult-8` selects the prohibition claim for the stated scope and window. Only then is the finding `settledByDecisionResult`.

A second Zone 8 request that merely names the Safety Director but has no dated decision Work or current result remains `unresolved`. A visible permit and green readiness tile cannot repair either gap. If no calibration Work occurs, the permission is neither exercised nor violated.

### A.2.8.PER:6 - Bias-Annotation


The chief bias is document-and-display authority: a readable permit, badge, policy response, or green gate looks stronger than its recoverable relation. The repair is to recover the grounds, participants, policy and its currentness, scope, window, and separate evidence. A second bias is obligation-shaped deontics; the exercise and non-exercise rules preserve permission as latitude.

### A.2.8.PER:7 - Conformance Checklist

| ID | Check |
|---|---|
| `CC-A2.8.PER-1` | Support a rule-based entitlement by the applicable affirmative rule and case facts. For a right granted to several parties jointly, use the instrument and the conditions on their joint action in §4.2. When reporting a `GrantedPermissionRelation@Context`, its §4.5 exercise relation, or a finding declared in §§4.3–4.6, establish the conditions of the corresponding declaration. |
| `CC-A2.8.PER-2` | For a single beneficiary within the §4.2 reference union, select exactly one of `beneficiarySystemRoleKindRef : U.KindRef`, `beneficiarySystemRoleAssignmentRef : U.RelationRef constrained to U.SystemRoleAssignment`, or `beneficiaryPartyRef : PartyRef`, with its branch-specific eligibility test. For an entitlement held jointly, apply the instrument to the participants and their required action together (§4.2). The branch record introduces no beneficiary U-kind. |
| `CC-A2.8.PER-3` | A strong grant identifies its participants, effective scope and interval, current policy and the act or combination that instituted this occurrence. Each grant-making contribution meets the authority and assignment conditions that the rule requires. Several contributors to one act and several required acts remain distinguishable. |
| `CC-A2.8.PER-4` | Weak findings require a current frame explicitly complete enough for the intended use; incompleteness returns `unresolved`. |
| `CC-A2.8.PER-5` | For exercise of a right conferred by an instrument, identify the dated Work and establish the match to the beneficiary or joint beneficiaries, authorized action, scope and time. The exercise relation in §4.5 identifies the exact §4.4 grant occurrence. Establish the eligibility of the contributions required by the instrument. A support provider may contribute without holding the right. |
| `CC-A2.8.PER-6` | Neither exercise nor non-exercise establishes `NonViolationFinding@Context`; non-exercise does not violate the grant, exercise alone does not establish obligation satisfaction, and exercise does not consume a grant without an explicit policy. |
| `CC-A2.8.PER-7` | A same-scope conflict is settled when a current applicable rule selects the outcome, or when decision Work supplies the result the precedence policy requires. In the decision branch, each required deciding contribution and its authority are established for this issue, scope and time. A named office with authority leaves its actual decision open. |
| `CC-A2.8.PER-8` | Permit episteme, carrier, evidence, admissibility, readiness, gate, capability, Work, and result remain distinct and are handled under their respective subject patterns. |

### A.2.8.PER:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| `MAY` stored as a `U.Commitment` modality | Recover whether the claim is a strong grant, weak finding, entry predicate, or ordinary prose; use the applicable subject pattern. |
| No prohibition found, therefore permission | Return `nonProhibited` only for a current frame sufficiently complete for the use; otherwise return `unresolved`. Neither result establishes a grant. |
| Permit document as permission | Establish what the operative rule makes sufficient. A permit can evidence an existing grant. Check its applicability, current scope and window, and the instituting act or combination when the question depends on that history. |
| Gate pass as authorization | Keep `GateDecisionResult` in `A.21`; cite a separate grant/conflict result when the gate consumes one. |
| Permission as readiness or capability | Keep readiness in `A.15.5` and capability in `A.2.2`; permission supplies neither. |
| Work “violates permission” | Test exercise coverage and any separately governed prohibition; uncovered work is not a permission violation by default. |
| Unnecessary evaluation records for action match or beneficiary eligibility | Test the Work against the action specification and the performer against the beneficiary branch; cite the already obtaining assignment or on-behalf-of relation and add separate evaluation evidence only when a receiving use needs it. |
| Precedence “owner” as resolution | Apply the rule when it selects the outcome. When a decision is needed, establish the authorised decision or combination of decisions and the result for this conflict. |
| Hidden generic beneficiary kind | Keep the closed reference union and branch-specific eligibility checks. |

### A.2.8.PER:9 - Consequences

Permission becomes inspectable. Practitioners can distinguish a frame-relative result from an enduring grant and from actual exercise, and can stop on unresolved conflict without letting a gate or permit display choose precedence. The cost is recording enough policy, identity, scope, window, and eligibility detail to support the intended use.

### A.2.8.PER:10 - Rationale

Positive permission has different satisfaction and failure behavior from obligation. A grant can obtain while unused. Non-use does not violate that grant, but a separate duty may be violated; matching action can exercise the grant without discharging a duty. Separating weak findings, strong grants and exercise preserves these consequences through the existing episteme, relation, speech-act, policy, Work and evidence-use patterns.

### A.2.8.PER:11 - SoTA-Echoing

| Practice question | Source or practice | FPF alignment | Boundary |
|---|---|---|---|
| How do weak and strong permission differ? | Moltmann (2024) distinguishes modal objects, strong permission, weak non-violation, and action satisfiers. | Separate frame-relative findings, instituted grants, and actual exercise; retain FPF subject patterns. | Do not import modal objects, truthmakers, or possible worlds as U-kinds. |
| How should permission, duty, and prohibition remain distinct? | W3C ODRL 2.2 (2018) models permission, prohibition, duty, assignee, action, constraint, and policy separately. | Keep beneficiary, action specification, policy, scope/window, and duty/prohibition predicates and pattern locations explicit. | FPF uses direct relations and epistemic findings rather than importing the ODRL information model wholesale. |
| What makes a policy decision usable? | NIST SP 800-207 (2020) and policy-as-code practice separate subject, requested action, resource and operating facts, current policy, and decision evidence. | Exercise eligibility and conflict use are bounded by the exact beneficiary, action, normative-frame and policy editions, ClaimScope, window, and intended use. | A policy response or gate display is not itself an enduring grant. |
| How should digital permit evidence be relied on? | W3C Verifiable Credentials Data Model 2.0 (2025) separates issuer, holder, verifier, status, proof, and relying context. | Permit publications enter `A.10` evidence/currentness paths and do not replace the grant relation. | Credential form supplies neither permission nor exercise by itself. |


### A.2.8.PER:12 - Relations

- **Coordinates with:** `A.2.8` for obligations, recommendations-as-duty, and prohibitions; `A.2.9` for instituting or revoking speech acts; and `A.6.B` and `A.6.C` for deontic claim classification and agreement-like boundary-language unpacking.
- **Supplies inputs to:** `A.15.5` readiness and direct mechanism/gate checks only when their own predicates explicitly consume a current grant, finding, or conflict result.
- **Relates to work through:** `A.15.1` for dated `U.Work` identity and `PermissionExerciseRelation@Context` for the separate exercise claim.
- **Uses evidence from:** `A.10` and publication/currentness patterns for claims about the permission relation and its permit carriers.
- **Does not replace:** system-role kind or assignment, capability, plan, gate, admissibility, policy precedence, evidence, performed Work, result, safety, assurance, responsibility, authority, access, or commitment patterns.

### A.2.8.PER:End
