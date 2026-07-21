## A.2.8.PER - Granted Permission, Exercise, and Non-Prohibition

> **Type:** Definitional ontic support pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### A.2.8.PER:0 - Use this when

Use this pattern when a policy, approval, permit, role rule, boundary claim, readiness check, or later work use needs to distinguish five questions: whether a sufficiently complete current frame supports a `NonProhibitionFinding@Context`; whether a valid grant currently obtains as `GrantedPermissionRelation@Context`; whether dated matching work exercises it through `PermissionExerciseRelation@Context`; whether checked actual work supports a `NonViolationFinding@Context`; and whether an incompatible current grant and norm requires `PermissionNormConflictFinding@Context`.

The first useful move is to name the beneficiary reference, permitted-action specification or checked work, policy and bounded context, scope, window, and the exact result needed now. Return exactly the warranted `NonProhibitionFinding@Context`, `GrantedPermissionRelation@Context`, `PermissionExerciseRelation@Context`, `NonViolationFinding@Context`, or `PermissionNormConflictFinding@Context`; do not infer one from another.

**Not this pattern when.** Use `A.2.8` for an accountable obligation, recommendation-as-duty, or prohibition; `A.2.9` for the communicative work that institutes or revokes a grant; `A.6.B` for L/A/D/E classification; `A.15.5` for work-entry readiness; `A.21` for gate decisions; and `A.15.1` for the identity and result of performed work. This support pattern is not a method, gate, permit carrier, work plan, or generic authorization object.

The primary reader is a policy, boundary, work-planning, assurance, or operations practitioner who must decide exactly what a permission-looking claim can support. The performer of a grant speech act or later work remains an admitted system under a current role assignment; the reader position does not perform those acts.

### A.2.8.PER:1 - Problem frame

Permission-looking language often compresses unlike values. “No rule forbids it” may be an incomplete search result. “The permit allows it” may refer to a document, an issuing act, or an enduring relation. “We used the permit” may mean only that a badge was visible, while no matching work occurred. A green gate can also look as if it defeated a current prohibition.

The governed concern is the smallest exact permission result needed for one beneficiary, action specification, context, scope, and window. The act, permit episteme, publication carrier, evidence relation, admissibility predicate, readiness relation, gate decision, actual work, and work result keep their direct owners.

### A.2.8.PER:2 - Problem

How can FPF represent positive permission without turning it into an obligation modality, absence-of-evidence claim, permit document, gate result, readiness label, capability, or performed action?

A conforming account must make weak and strong permission different, keep grant occurrence identity inspectable, connect only eligible matching work to a current grant, keep both exercise and non-exercise from establishing a frame-relative non-violation finding, and expose same-scope normative conflicts instead of resolving them by display or wording.

### A.2.8.PER:3 - Forces

| Force | Tension |
|---|---|
| Latitude vs duty | Permission makes an action allowable; it does not require the action. |
| Weak evidence vs world relation | A complete-frame search can support non-prohibition, while an incomplete search is unresolved. |
| Enduring grant vs instituting act | A speech act can ground a permission without being the continuing relation. |
| Beneficiary variety vs kind discipline | Roles, assignments, and parties all occur in practice, but a generic beneficiary U-kind would erase their different eligibility tests. |
| Current grant vs actual exercise | A grant may obtain without work; work may occur without matching or exercising the grant. |
| Local policy vs visible artifacts | A permit or gate display is easy to see, but scope, window, currentness, revocation, and precedence decide use. |

### A.2.8.PER:4 - Solution

#### A.2.8.PER:4.1 - Keep the permission objects separate

Use exactly the object warranted by the current claim:

- `NonProhibitionFinding@Context` is a frame-relative episteme returned before action when a sufficiently complete current normative frame contains no applicable prohibition.
- `GrantedPermissionRelation@Context` is an enduring strong permission instituted under an exact policy.
- `PermissionExerciseRelation@Context` connects actual dated work to one obtaining grant occurrence when action and beneficiary eligibility match.
- `NonViolationFinding@Context` is a frame-relative episteme about actual work that instantiates no applicable prohibition in the checked frame.
- `PermissionNormConflictFinding@Context` is an episteme exposing an incompatible current grant and prohibition or commitment over matching content, scope, and window.

Absence of any one object does not imply another. In particular, no grant is inferred from a weak finding, no exercise is inferred from a grant, and work outside a grant is not called a violation of that grant.

#### A.2.8.PER:4.2 - Use the closed beneficiary reference family

```text
PermissionBeneficiaryRef ::= RoleRef | RoleAssignmentRef | PartyRef
```

The participant meaning is stable: the exact entity designated by the grant as beneficiary. The reference branch changes only the exercise-eligibility test:

- `RoleAssignmentRef` covers that exact current assignment.
- `RoleRef` covers current assignments that instantiate the role in the declared context under the grant policy; the role value itself does not perform work.
- `PartyRef` covers work only when its exact performer or on-behalf-of relation satisfies the policy. Shared naming or organizational membership is insufficient.

This is a closed ref union over admitted `U.Entity` values, not `U.PermissionBeneficiary`, `U.Authorization`, or another new U-kind. A materially different beneficiary meaning requires a separate direct-owner decision.

#### A.2.8.PER:4.3 - Record weak permission and non-violation as findings

```text
NonProhibitionFinding@Context <: U.Episteme
  beneficiaryRef: PermissionBeneficiaryRef
  permittedActionSpecificationRef: U.EpistemeRef
  normativeFrameRef: U.EpistemeRef
  frameCurrentnessResultRef: U.EpistemeRef
  frameCompletenessForUseResultRef: U.EpistemeRef
  boundedContextRef: U.BoundedContextRef
  scope: U.ClaimScope
  evaluationWindow: QualificationWindowPolicy
  checkedProhibitionRefs: set<ClaimIdRef>
  result: nonProhibited | unresolved
  evaluationWorkRef: WorkRef

NonViolationFinding@Context <: U.Episteme
  actionOrWorkRef: WorkRef
  beneficiaryPerformanceBindingRef: U.EpistemeRef
  normativeFrameRef: U.EpistemeRef
  frameCurrentnessResultRef: U.EpistemeRef
  frameCompletenessForUseResultRef: U.EpistemeRef
  boundedContextRef: U.BoundedContextRef
  scope: U.ClaimScope
  evaluationWindow: QualificationWindowPolicy
  checkedProhibitionRefs: set<ClaimIdRef>
  result: nonViolating | unresolved
  evaluationWorkRef: WorkRef
```

`nonProhibited` and `nonViolating` are admissible only when the named frame is current and explicitly sufficiently complete for the intended use. Otherwise the finding is `unresolved`. Neither finding institutes permission, proves absence outside its frame, or becomes a world-side relation.

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
  institutingSpeechActRef: SpeechActRef
  grantorAssignmentRef: RoleAssignmentRef
  grantValidityPolicyRef: U.EpistemeRef
  boundedContextRef: U.BoundedContextRef
  scope: U.ClaimScope
  validityWindow: QualificationWindowPolicy
  revocationOrSupersessionRef?: SpeechActRef
```

The beneficiary and permitted-action specification are participants. Grantor assignment, instituting act, policy, context, scope/window, and revocation are constructive ground or qualifiers, not collapsed participants.

The relation begins only when an exact grantor assignment performs a `U.SpeechAct` that satisfies the current policy's grant-validity predicate and institutes permission for the named participants. It obtains while beneficiary applicability, policy continuation, scope, and window hold and no valid revocation or supersession ends it.

One occurrence is identified by the instituting speech-act occurrence, exact beneficiary ref and ref kind, action-specification edition, policy/context, and effective interval. Beneficiary change, renewal, materially changed action specification, non-carried policy edition, or revocation ends or splits the occurrence. A policy edition preserves it only through an explicit satisfied carry-forward rule.

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
    refMode: U.EntityRef
      // resolves to one GrantedPermissionRelation@Context occurrence

semanticDirection: ExercisingWorkSlot -> GrantedPermissionOccurrenceSlot

RelationOccurrenceQualifiers:
  actionMatchFindingRef: U.EpistemeRef
  beneficiaryEligibilityFindingRef: U.EpistemeRef
  exerciseScope: U.ClaimScope
  exerciseInterval: QualificationWindowPolicy
```

The exercise relation obtains only when actual dated work instantiates the permitted-action specification, the performer relation satisfies the exact beneficiary branch, the grant obtains throughout the exercise interval, and the work remains in scope. The work is a satisfier of permitted action content. It does not satisfy or discharge an obligation and does not consume the grant unless the named policy explicitly makes it single-use or quota-bound.

Non-exercise leaves an obtaining grant unused and ordinarily still obtaining; it does not establish `NonViolationFinding@Context`. Exercise establishes only the exercise relation and likewise does not establish that finding without the separate checked-frame evaluation. Work outside the action specification, beneficiary binding, scope, or window does not exercise the grant; a separate prohibition, commitment, admissibility, or work owner decides any further consequence.

#### A.2.8.PER:4.6 - Expose conflict without inventing precedence

```text
PermissionNormConflictFinding@Context <: U.Episteme
  grantedPermissionOccurrenceRef: U.EntityRef
  conflictingNormClaimRef: ClaimIdRef
  beneficiaryAndActionMatchFindingRef: U.EpistemeRef
  overlapScope: U.ClaimScope
  overlapWindow: QualificationWindowPolicy
  policyOrPrecedenceOwnerRef: U.EpistemeRef
  blockedWorkOrRelianceRef: U.EntityRef
  disposition: unresolved | resolvedByNamedOwner
  resolutionOrReopenConditionRef: U.EpistemeRef
```

Create the finding only when the grant and current prohibition or commitment concern the same beneficiary/action content, overlapping scope/window, and incompatible practical conclusions. Permission and an obligation to perform the same action are not automatically in conflict. Until the named owner resolves a real conflict, work-entry reliance is unresolved; permit text, readiness, or a passing gate does not silently defeat the prohibition.

#### A.2.8.PER:4.7 - Keep the handshakes narrow

| Neighboring object | Exact handshake |
|---|---|
| Grant/revoke act | `A.2.9 U.SpeechAct <: U.Work`; `institutes.permissions` cites the grant occurrence. The act is not the enduring relation. |
| Permit episteme and carrier | `C.2.1`, `E.17`, `G.11`, and `A.10` may assert, publish, carry, or evidence the relation; readable form neither institutes nor equals it. |
| Duty or prohibition | `A.2.8 U.Commitment`; permission remains outside its modality family. |
| Boundary claim or entry predicate | `A.6.B` classifies the claim; an `A-*` predicate may consume a current permission result but does not create one. |
| Work plan and readiness | `A.15.2` owns the `U.WorkPlan`; `A.15.5` may cite a permission/conflict result as one readiness input. Neither creates permission. |
| Gate decision | `A.21` publishes a gate outcome. It neither creates permission nor resolves a permission conflict. |
| Work and result | `A.15.1` owns the dated work. Exercise requires the direct relation above; permission supplies no capability, readiness, safety, success, or result quality. |

### A.2.8.PER:5 - Archetypal Grounding

**Strong grant and exercise.** A policy-valid grant speech act institutes `GrantedPermissionRelation@Context` for `MaintenanceTechnicianRole` to run `CalibrationProcedure-v3` during one service window. Its beneficiary is a `RoleRef`. Assignment `Tech-17@Shift-B` instantiates that role and performs dated calibration work that matches the action specification within scope. A `PermissionExerciseRelation@Context` obtains from that work to the still-current grant. The grant remains current for the rest of the window because the policy is not single-use. No obligation, readiness, capability, gate passage, safe result, or successful calibration is inferred.

**Weak finding.** A policy reviewer checks a named, current, sufficiently complete plant-access frame and finds no prohibition applicable to the role, action specification, zone, and window. The result is `NonProhibitionFinding@Context(result=nonProhibited)`, not an instituted grant. If the emergency-policy register cannot be checked, the result is `unresolved`.

**Actual-work non-violation.** After `CalibrationWork-17B` is performed, a compliance reviewer evaluates that exact work against `PlantCalibrationNormativeFrame-2026-07-19-e3`, whose currentness and sufficient completeness for the technician, procedure, zone, and service-window use are named and whose applicable prohibitions are checked. The result is `NonViolationFinding@Context(actionOrWorkRef=CalibrationWork-17B, normativeFrameRef=PlantCalibrationNormativeFrame-2026-07-19-e3, result=nonViolating)`. The separate exercise relation shows which grant the work exercised; exercise alone does not establish non-violation, and non-exercise alone does not establish it either. If the frame is stale or insufficiently complete for this use, the non-violation result is `unresolved`.

**Conflict and non-use.** The role-level calibration grant remains published while an emergency prohibition forbids entry into the contaminated zone during an overlapping interval. `PermissionNormConflictFinding@Context` names both exact claims and the emergency-policy precedence owner; work entry remains unresolved. A visible permit and green readiness tile cannot repair it. If no calibration work occurs, the permission is neither exercised nor violated.

### A.2.8.PER:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: permission-specific support across boundary and work uses.

The chief bias is document-and-display authority: a readable permit, badge, policy response, or green gate looks stronger than its recoverable relation. The repair is exact ground, participants, policy/currentness, scope/window, and separate evidence. A second bias is obligation-shaped deontics; the exercise and non-exercise rules preserve permission as latitude.

### A.2.8.PER:7 - Conformance Checklist

| ID | Check |
|---|---|
| `CC-A2.8.PER-1` | The current result is exactly `NonProhibitionFinding@Context`, `GrantedPermissionRelation@Context`, `PermissionExerciseRelation@Context`, `NonViolationFinding@Context`, or `PermissionNormConflictFinding@Context`. |
| `CC-A2.8.PER-2` | Beneficiary uses only `RoleRef | RoleAssignmentRef | PartyRef`, with its exact eligibility branch. |
| `CC-A2.8.PER-3` | A strong grant names participants, instituting act, grantor assignment, policy/context, scope/window, currentness, and occurrence identity. |
| `CC-A2.8.PER-4` | Weak findings require a current frame explicitly complete enough for the intended use; incompleteness returns `unresolved`. |
| `CC-A2.8.PER-5` | Exercise names dated work, one current grant occurrence, action match, beneficiary eligibility, scope, and interval. |
| `CC-A2.8.PER-6` | Neither exercise nor non-exercise establishes `NonViolationFinding@Context`; non-exercise is not violation, and exercise is not obligation satisfaction and does not consume a grant without an explicit policy. |
| `CC-A2.8.PER-7` | A same-scope conflict names its direct policy/precedence owner and blocks only the unresolved work or reliance use. |
| `CC-A2.8.PER-8` | Permit episteme, carrier, evidence, admissibility, readiness, gate, capability, work, and result retain their direct owners. |

### A.2.8.PER:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| `MAY` stored as a `U.Commitment` modality | Recover whether the claim is a strong grant, weak finding, entry predicate, or ordinary prose; use the exact owner. |
| No prohibition found, therefore permission | Require currentness and frame completeness; otherwise return `unresolved`. |
| Permit document as permission | Recover the instituting act, current grant occurrence, policy, scope/window, and evidence relation. |
| Gate pass as authorization | Keep `GateDecision` in `A.21`; cite a separate grant/conflict result when the gate actually consumes one. |
| Permission as readiness or capability | Keep readiness in `A.15.5` and capability in `A.2.2`; permission supplies neither. |
| Work “violates permission” | Test exercise coverage and any separately governed prohibition; uncovered work is not a permission violation by default. |
| Hidden generic beneficiary kind | Keep the closed reference union and branch-specific eligibility checks. |

### A.2.8.PER:9 - Consequences

Permission becomes inspectable without being inflated into a universal authorization ontology. Practitioners can distinguish a tentative frame-relative result from an enduring grant and from actual exercise, and can stop on unresolved conflict without letting a gate or permit display choose precedence. The cost is recording enough policy, identity, scope, window, and eligibility detail to support the intended use.

### A.2.8.PER:10 - Rationale

Positive permission has different satisfaction and failure behavior from obligation. A grant can obtain while unused; non-use ordinarily violates nothing; matching action can exercise the grant without discharging a duty. Separating weak findings, strong grants, and exercise preserves these practical consequences while using existing episteme, relation, speech-act, policy, work, and evidence owners.

### A.2.8.PER:11 - SoTA-Echoing

| Practice question | Current practice and source | FPF alignment | Disposition |
|---|---|---|---|
| How do weak and strong permission differ? | Moltmann (2024) distinguishes modal objects, strong permission, weak non-violation, and action satisfiers. | Separate frame-relative findings, instituted grants, and actual exercise; retain direct FPF owners. | **Adapt.** Do not import modal objects, truthmakers, or possible worlds as U-kinds. |
| How should permission, duty, and prohibition remain distinct? | W3C ODRL 2.2 (2018) models permission, prohibition, duty, assignee, action, constraint, and policy separately. | Keep beneficiary, action specification, policy, scope/window, and duty/prohibition owners explicit. | **Adapt.** FPF uses direct relations and epistemic findings rather than importing the ODRL information model wholesale. |
| What makes a policy decision usable? | NIST SP 800-207 (2020) and current policy-as-code practice separate subject, requested action, resource/context, current policy, and decision evidence. | Exercise eligibility and conflict use are bounded by exact beneficiary, action, context, scope/window, and current policy. | **Adapt.** A policy response or gate display is not itself an enduring grant. |
| How should digital permit evidence be relied on? | W3C Verifiable Credentials Data Model 2.0 (2025) separates issuer, holder, verifier, status, proof, and relying context. | Permit publications enter `A.10` evidence/currentness paths and do not replace the grant relation. | **Adapt.** Credential form supplies neither permission nor exercise by itself. |

These sources change the practical record and its failure results. They do not license a generic authorization kind, beneficiary kind, permit-as-relation shortcut, or automatic precedence rule.

### A.2.8.PER:12 - Relations

- **Coordinates with:** `A.2.8` for obligations, recommendations-as-duty, and prohibitions; `A.2.9` for instituting/revoking speech acts; `A.6.B` and `A.6.C` for deontic claim classification and contract unpacking.
- **Supplies inputs to:** `A.15.5` readiness and direct mechanism/gate checks only when their own predicates explicitly consume a current grant, finding, or conflict result.
- **Relates to work through:** `A.15.1` for dated `U.Work` identity and `PermissionExerciseRelation@Context` for the separate exercise claim.
- **Uses evidence from:** `A.10` and publication/currentness owners without turning evidence or a permit carrier into the permission relation.
- **Does not replace:** role assignment, capability, plan, gate, admissibility, policy precedence, evidence, performed work, result, safety, assurance, or commitment owners.

### A.2.8.PER:End

