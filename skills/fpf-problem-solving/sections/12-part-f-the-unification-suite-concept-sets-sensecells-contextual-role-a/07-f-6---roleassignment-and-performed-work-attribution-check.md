## F.6 - RoleAssignment and Performed-Work Attribution Check

> **Type:** Boundary and use pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### F.6:0 - Use This When

**Plain name.** Role-assignment and work-attribution check.

Use this pattern when a project has a role description, role label, assignment notation, or work record and needs to decide whether it can make a work-facing `U.RoleAssignment` claim or attribute performed work through that assignment.

Typical moments:

- a method description names `ReviewerRole`, `OperatorRole`, `InspectorRole`, `TransformerRole`, or another required role, and the project must decide which holder bears that role in the bounded context;
- a work record says "Alice reviewed", "Robot-7 inspected", "the operations team approved", or "the CI service deployed", but the holder, role, bounded context, assignment window, or performed-by relation is not explicit;
- a source text uses `Holder#Role:Context@Window`, `RoleEnactment`, "assigned role", "played role", or "acted as" and the project must recover the typed assignment relation rather than preserve source notation as ontology;
- a status, evidence, requirement, source, standard, dashboard, model card, publication, or report is being described with role language, and the project must decide that this is not a work-facing role assignment;
- a cross-context role-like word appears, and the project must keep the local role assignment separate from any `F.9` bridge or `F.5` naming question.

**Primary EntityOfConcern.** The EntityOfConcern is the role-assignment and performed-work attribution check: a bounded check over a candidate `U.RoleAssignment` and, when current, a `U.Work` occurrence that may cite that assignment through `Work.performedBy` or `RoleEnactmentFact`. The check is not the role value, not the role description, not the work occurrence, not a status assertion, not evidence, and not a publication form.

**Primary working reader.** The first reader is an engineer-manager, analyst, method author, or FPF author who must keep a role label, role description, assignment relation, method requirement, work occurrence, status-use relation, and evidence-use relation from becoming one under-typed "enactment" claim.

**First useful move.** Recover the candidate holder, role value, bounded context, and assignment window or window disposition. Then decide whether the current claim is only assignment admission, performed-work attribution under an assignment, or a status, evidence, source, or publication claim governed outside F.6.

**What goes wrong if missed.** A role description becomes proof that a holder has a role. A work record names a person or label but not the role assignment that made the work attributable. A report, standard, requirement, or dashboard is made into a role holder because it constrained, evidenced, justified, displayed, or described work. Source `U.RoleEnactment` wording grows back into a second run-time ontology beside `U.Work` and `U.RoleAssignment`.

**What this buys.** The reader gets one small local check: who or what can bear the role, in which context and window, and whether a specific work occurrence may be attributed through that assignment. Status, evidence, source, publication, method, capability, and bridge claims remain with their direct patterns.

**Not this pattern when.**

- If the current claim is the role value itself, use `A.2`.
- If the current claim is the role-description episteme, use `F.4`.
- If the current claim is durable naming of a role or type label, use `F.5` or `F.18`.
- If the current claim is the `U.RoleAssignment` relation value itself and its SlotSpecs, use `A.2.1`.
- If the current claim is role state or enactable-state admission, use `A.2.5`.
- If the current claim is capability, use `A.2.2`.
- If the current claim is method, method description, work plan, performed work, or role-method-work alignment beyond the assignment check, use `A.15` and its subpatterns.
- If the current claim is status, evidence, source, standard, requirement, publication, assurance, gate, or decision use of an episteme, use the direct pattern for that relation, such as `F.10`, `A.10`, `B.3`, `C.28`, `E.17`, or `E.10.D2`.
- If the current claim is cross-context sameness, translation, or substitution, use `F.9`.
- If "role" means a relation position, use `A.6.5` SlotSpec discipline.

### F.6:1 - Problem Frame

Role assignment sits between a role description and performed work. A role description lets a reader recognize `InspectorRole` or `ReviewerRole`; it does not assign a holder. A work occurrence may be performed by a holder under a role assignment; it is not the assignment itself. A status value, evidence relation, standard-use relation, requirement-use relation, or publication cue may constrain, evidence, qualify, or display a work-admission relation; it is not a role holder and not performed work.

A common source shape mixes these questions into one "role assignment and enactment cycle" with a status branch. That made the pattern convenient but ontologically noisy. A status assertion and a work-facing role assignment have different subjects, slots, evidence, windows, and direct governing patterns. Putting them into one cycle made status look like a kind of role assignment and made `RoleEnactment` look like a durable run-time object.

F.6 therefore becomes a check pattern. It asks whether the current local claim can use a recovered `U.RoleAssignment`, and whether a current `U.Work` occurrence can cite that assignment. If the current claim is status, evidence, source, publication, bridge, capability, or method, F.6 names the direct governing pattern and stops.

### F.6:2 - Problem

Without this pattern:

1. **Role-description proof.** A role-description episteme or role label is treated as proof that a holder bears the role.
2. **Assignment and work collapse.** A work occurrence is treated as if it were the assignment, or an assignment is treated as if work already happened.
3. **RoleEnactment reification.** `RoleEnactment` becomes a second durable U-kind beside `U.Work` and `U.RoleAssignment`.
4. **Status branch returns.** Status assertions are processed as if they were the same kind of result as role assignment.
5. **Episteme-role drift.** Standards, reports, datasets, requirements, model cards, dashboards, and publications become "role holders" because they are useful in project reasoning.
6. **Window and state loss.** A holder-role-context statement is used for current work without saying whether assignment currentness or role-state admission matters.
7. **Cross-context overreach.** A familiar role-like label from another canon is used to justify local assignment without a bridge.
8. **Notation replaces relation.** `Holder#Role:Context@Window` is copied as if the string were the assignment value.

### F.6:3 - Forces

| Force | Tension |
| --- | --- |
| Recognition vs admission | A role description and label help recognition, but assignment admission needs holder, role, context, and currentness. |
| Thin check vs full alignment | F.6 should be quick, while stronger work claims may need `A.15`, role state, method, capability, evidence, gate, or source patterns. |
| Assignment vs work | A holder can be assigned to a role without performing work; performed work can cite an assignment only when the work occurrence is current. |
| Local role meaning vs cross-context reuse | The assignment is local to one bounded context; cross-context role-like words need bridge discipline. |
| Episteme use vs acting holder | Epistemes can justify, evidence, constrain, publish, or classify; they do not hold work-facing roles merely because they are useful. |
| Open-world use vs form cost | A weak local mention should not force every related SlotSpec or relation slot, but missing currentness, state, or method information must lower or block stronger claims. |

### F.6:4 - Solution

Use F.6 as a local check over candidate assignment and optional work attribution.

```text
RoleAssignmentAttributionCheck:
  CandidateRoleDescriptionRef:
  CandidateHolderRef:
  CandidateRoleValueRef:
  BoundedContextRef:
  AssignmentWindowDisposition:
  HolderAdmissionDisposition:
  RoleStateAdmissionRef:
  CapabilityRequirementRef:
  MethodOrMethodDescriptionRef:
  WorkOccurrenceRef:
  PerformedByRelation:
  AssignmentJustificationRef:
  EvidenceOrSourceUseRefs:
  BridgeRef:
  NotCarried:
  Result:
```

This check is not a new root kind. It is an application relation over values governed elsewhere. `A.2.1` governs `U.RoleAssignment`; `A.15.1` governs the `U.Work` occurrence; `F.10`, `A.10`, `B.3`, `E.17`, `E.10.D2`, and direct governing patterns govern status, evidence, assurance, publication, and source-use relations.

#### F.6:4.1 - Slot Meanings

| Slot | Admitted value | Meaning |
| --- | --- | --- |
| `CandidateRoleDescriptionRef` | `F.4` role-description episteme or local role gloss | The description that makes the role recognizable. It is not the role value and not the assignment. |
| `CandidateHolderRef` | `U.System` or acting holon admitted by `A.2.1` | The candidate holder that may bear the role. Epistemes are not admitted here merely because they are used as evidence, source, standard, requirement, publication, or status bearer. |
| `CandidateRoleValueRef` | `U.Role` governed by `A.2` | The work-facing role value being assigned. |
| `BoundedContextRef` | `U.BoundedContext` | The local context that gives the role value meaning. |
| `AssignmentWindowDisposition` | filled, inherited, unknown, not asserted, or not current for this claim | Whether assignment currentness is recovered well enough for the claim being made. |
| `HolderAdmissionDisposition` | admitted, not admitted, lowered, or blocked with reason | Whether the holder kind and local predicates admit the assignment. |
| `RoleStateAdmissionRef` | `A.2.5` state assertion or absence disposition when current | Whether role state or enactable-state admission matters for current work. |
| `CapabilityRequirementRef` | `A.2.2` capability relation when current | Required ability or operating envelope; not proved by role name. |
| `MethodOrMethodDescriptionRef` | `A.3.1`, `A.3.2`, or `A.15` reference when current | The method or method-description claim that the role assignment may serve. |
| `WorkOccurrenceRef` | `U.Work` governed by `A.15.1` when current | The performed work occurrence being attributed. Missing work means no performed-work attribution claim is made. |
| `PerformedByRelation` | `Work.performedBy = RoleAssignment` or `RoleEnactmentFact` | The direct relation or named fact that links work to the assignment. |
| `AssignmentJustificationRef` | source, speech act, gate, decision, policy, evidence, or provenance relation governed by its direct pattern | Why the assignment claim is admitted or relied upon, when current. |
| `EvidenceOrSourceUseRefs` | direct evidence, source, status, publication, assurance, or requirement-use relation refs | Direct non-F.6 uses that may justify, challenge, or qualify the assignment or work claim. They do not become role assignments. |
| `BridgeRef` | `F.9` bridge when cross-context reuse is current | Cross-context explanation or substitution claim; not local assignment identity. |
| `NotCarried` | stronger claim not made by this check | Examples: status truth, gate passage, method validity, capability proof, work occurrence, evidence sufficiency, cross-context substitution. |
| `Result` | `assignmentAdmitted`, `assignmentBlocked`, `workAttributionAdmitted`, `workAttributionBlocked`, `claimGovernedOutsideF6`, or `claimLowered` | The local check result. |

#### F.6:4.2 - The Check Sequence

Use these questions in order. They are judgement questions, not a `U.WorkPlan`, registry procedure, or tool protocol.

1. **Role meaning recovered?** Does the role label point to a `U.Role` in one bounded context, usually through `F.4` and `A.2`?
2. **Holder admitted?** Is the candidate holder a system or acting holon admitted by `A.2.1` and by the local role description?
3. **Context and window adequate?** Is the bounded context explicit, and is the assignment window filled, inherited, unknown, not asserted, or not current for the claim?
4. **Related prerequisites current?** Does this use need role state, capability, method, method description, work plan, evidence, gate, decision, or source-currentness?
5. **Work occurrence current?** Is there a `U.Work` occurrence to attribute? If not, stop at assignment admission or blocker.
6. **Performed-by relation admissible?** Can the work occurrence cite the assignment by `Work.performedBy = RoleAssignment` or `RoleEnactmentFact`?
7. **Claim governed outside F.6?** If the current claim is status, evidence, source, publication, requirement, assurance, bridge, method, capability, or gate use, apply the direct governing pattern and do not encode that claim as role assignment.

#### F.6:4.3 - Assignment Result vs Work-Attribution Result

Keep two local results separate.

```text
AssignmentAdmission:
  CandidateHolderRef bears CandidateRoleValueRef in BoundedContextRef
  with AssignmentWindowDisposition and HolderAdmissionDisposition.
```

```text
PerformedWorkAttribution:
  WorkOccurrenceRef performedBy RoleAssignmentRef
  with RoleEnactmentFact only when a named fact is useful.
```

An assignment admission does not prove that work happened. A performed-work attribution does not prove that the method was valid, the capability was sufficient, the evidence is adequate, or the gate passed. Those claims use their governing patterns.

#### F.6:4.4 - `RoleEnactmentFact`

Use `RoleEnactmentFact` only as a name for the derived fact that a work occurrence was performed under a role assignment.

```text
RoleEnactmentFact:
  workOccurrence: U.Work
  performedBy: U.RoleAssignment
  methodTrace?: U.Method or U.MethodDescription reference when current
  window?: inherited from work occurrence or role assignment when current
```

Do not write `U.RoleEnactment` as a durable root kind. If a log, table, database row, or publication stores a role-enactment entry, treat it as a record of this fact unless a direct governing pattern admits record-as-value for that use.

#### F.6:4.5 - Status and Evidence Claims Governed Outside F.6

Status and evidence claims often sit next to role assignment. They do not become role assignment.

| Source sentence | F.6 result | Direct governing pattern |
| --- | --- | --- |
| "The standard plays the normative role for this method." | `claimGovernedOutsideF6`; no role assignment holder recovered. | standard-use, requirement-use, source-use, or `E.10.D2` |
| "The report has evidence role for claim C." | `claimGovernedOutsideF6`; evidence-use relation around an episteme. | `A.10`, `B.3`, or direct evidence-use pattern |
| "The dashboard says the service is ready." | `claimGovernedOutsideF6`; status-use, display, or source question. | `F.10`, `E.17`, gate or assurance pattern when current |
| "Alice reviewed report R as ReviewerRole." | candidate assignment plus work attribution may be current. | `A.2.1`, `A.15.1`, and F.6 check |
| "RBAC admin role allows access." | access or policy term first; work-facing role assignment only if actual work attribution is also current. | direct access, policy, status, or source-use pattern |

#### F.6:4.6 - Compact Notation and Shortcut Boundary

`Holder#Role:Context@Window` is allowed as a compact reading aid after the typed relation is recoverable.

Baseline relation:

```text
RoleAssignment:
  HolderSlot:
  RoleValueSlot:
  BoundedContextSlot:
  AssignmentWindowSlot:
```

Compact notation:

```text
Holder#Role:Context@Window
```

The compact notation saves reader effort in examples, tables, and short work records. It weakens the representation by hiding SlotSpec names and any current assignment justification, role state, capability, method, evidence, source, or provenance relation. Therefore it is admitted only for local reading, examples, and compact citations after the typed slots are either filled, inherited, or explicitly not current for the claim.

Do not use the compact notation as proof of assignment, proof of performed work, proof of capability, proof of method validity, proof of status, or proof of gate passage. If reliance-bearing use depends on any hidden slot, unfold the notation to the typed relation or lower the claim.

### F.6:5 - Invariants

1. **Role assignment is local.** Every assignment check names one `U.Role`, one admitted holder, and one `U.BoundedContext`.
2. **Role description is not assignment.** A role-description episteme may identify the role value; it does not assign a holder.
3. **Assignment is not work.** A `U.RoleAssignment` can be admitted without any `U.Work` occurrence.
4. **Work attribution is direct.** Performed work cites the role assignment through `Work.performedBy = RoleAssignment`; `RoleEnactmentFact` is only a named fact over that relation.
5. **No durable `U.RoleEnactment`.** Source `U.RoleEnactment` wording is repaired to direct performed-by wording or `RoleEnactmentFact`.
6. **Status is not a role branch.** Status-use statements are governed by `F.10` or the direct status pattern, not by F.6.
7. **Epistemes are not role holders by use.** Evidence, source, standard, requirement, definition, explanation, publication, assurance, and gate uses of epistemes go to their direct relations.
8. **Window honesty.** If a stronger claim depends on assignment currentness, role state, or work time, missing window content lowers or blocks that claim.
9. **Bridge restraint.** Cross-context role-like labels need `F.9`; a bridge does not mutate a local assignment.
10. **Notation restraint.** `Holder#Role:Context@Window` is source or shorthand notation for a typed assignment relation, not the relation's ontology.

### F.6:6 - Reasoning Primitives

```text
RoleDescription RD describes Role R in Context C
  and Holder H is admitted for R in C
  -> candidate RoleAssignment(H, R, C).
```

```text
RoleAssignment RA is admitted
  and Work W is a current U.Work occurrence
  and W performedBy RA is admitted
  -> RoleEnactmentFact(W, RA) may be named.
```

```text
Source episteme E is used as evidence, standard, requirement, source, publication, or status bearer
  -> no RoleAssignment holder is recovered from that use alone.
```

```text
Role-like label L comes from another bounded context
  -> no assignment substitution without F.9 bridge and local A.2.1 check.
```

### F.6:7 - Archetypal Grounding

#### F.6:7.1 - Robot Inspection

A maintenance line has a role-description episteme for `InspectorRole`. A shift note says Robot-7 inspected Pump-12.

F.6 recovers:

```text
CandidateHolderRef: Robot_7
CandidateRoleValueRef: InspectorRole
BoundedContextRef: MaintenanceLine_A
AssignmentWindowDisposition: filled by shift window
WorkOccurrenceRef: InspectionWork_2026-06-15-09
PerformedByRelation: InspectionWork_2026-06-15-09 performedBy Robot_7#InspectorRole:MaintenanceLine_A@shift
Result: workAttributionAdmitted, if A.2.1 and A.15.1 checks pass
```

This does not prove the robot's sensor capability, the inspection method's adequacy, or the quality of the result. Those claims use capability, method, evidence, and assurance patterns.

#### F.6:7.2 - Review Report and Reviewer

A review report is an episteme. The reviewer is a person, service, or team modeled as an acting holon.

The sentence "Report R has reviewer role" is repaired by asking two questions:

- Who or what performed the review work under `ReviewerRole`?
- How is report R being used now: as evidence, source, publication, or result?

The reviewer holder may be assigned a `U.RoleAssignment`. The report does not hold the role. Evidence use of the report goes to the evidence-use pattern.

#### F.6:7.3 - Standard Used in Safety Work

A safety method description cites ISO 26262. The source phrase says that the standard has the "normative role" in the safety case.

F.6 result:

```text
Result: claimGovernedOutsideF6
NotCarried: no HolderSlot, no U.RoleAssignment, no performed work
```

The standard is an episteme used through standard-use, source-use, requirement-use, or specification-use relations. A safety engineer or tool service may separately hold `SafetyAnalystRole` when performing work with that standard.

#### F.6:7.4 - Access Label and Actual Approval Work

An RBAC directory says Alice has `DB-Admin`. That directory state is an access or policy status in its own bounded context. It is not automatically a work-facing `ApproverRole`.

If Alice approves a database migration, F.6 can check a separate assignment and work attribution:

```text
Alice#ApproverRole:MigrationApprovalContext@approval-window
ApprovalWork_481 performedBy Alice#ApproverRole:MigrationApprovalContext@approval-window
```

The RBAC status may justify or constrain the approval only through the direct access, policy, evidence, source, or gate pattern that admits that use.

### F.6:8 - Bias Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Semio-bias | The pattern starts explaining reports, standards, dashboards, model cards, logs, or publications instead of checking role assignment and work attribution. | Keep the primary check on holder, role, context, window, and performed-by relation. Send episteme uses to direct patterns. |
| Status-role drift | Status values are treated as a branch of role assignment because both can have holders, subjects, windows, or evidence. | Status-use statements go to `F.10` or the direct status pattern. F.6 handles work-facing role assignment only. |
| Enactment reification | `RoleEnactment` becomes a separate root kind or object that competes with `U.Work`. | Use direct `Work.performedBy = RoleAssignment`; use `RoleEnactmentFact` only as a named derived fact. |
| Notation authority | A compact string is treated as if it were the relation. | Recover the typed SlotSpecs through `A.2.1`; the string is only shorthand or source wording. |
| Bridge overreach | Cross-context similarity licenses local assignment. | Keep assignment local; use `F.9` only for the cross-context bridge claim. |

### F.6:9 - Conformance Checklist

Use this checklist when applying F.6.

1. The candidate role is a `U.Role` in one bounded context, not only a source label.
2. The candidate holder is a system or acting holon admitted by `A.2.1`.
3. The assignment window is filled, inherited, unknown, not asserted, or not current for this claim.
4. If role state matters, an `A.2.5` role-state admission or blocker is named.
5. If capability matters, an `A.2.2` capability relation or blocker is named.
6. If method or method description matters, `A.3.1`, `A.3.2`, or `A.15` is named.
7. If actual work is claimed, the `U.Work` occurrence is named under `A.15.1`.
8. Performed work uses `Work.performedBy = RoleAssignment` or `RoleEnactmentFact`, not `U.RoleEnactment`.
9. Status, evidence, source, standard, requirement, publication, assurance, gate, and decision uses are not encoded as role assignment.
10. Cross-context role-like reuse is represented by `F.9` and does not mutate the local assignment.
11. Compact notation is unfolded to typed assignment slots before reliance-bearing use.
12. `NotCarried` names the strongest tempting overclaim that this F.6 check does not make.

### F.6:10 - Common Anti-Patterns and Repairs

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Role description as assignment | A role card or label is cited as proof that someone holds the role. | Recover `U.RoleAssignment` through `A.2.1`; keep the card as role-description episteme under `F.4`. |
| Assignment as work | "Assigned reviewer" is used as evidence that review happened. | Name the `U.Work` occurrence under `A.15.1` or lower the claim to assignment only. |
| Work without assignment | A work log names "reviewed" but gives no holder-role-context assignment. | Recover holder, role, context, and window; if missing, block performed-work attribution. |
| `U.RoleEnactment` revival | A log or pattern names a durable role-enactment object. | Use `Work.performedBy = RoleAssignment`; name `RoleEnactmentFact` only when a fact label is useful. |
| Evidence role | A report, dataset, model card, or standard is made a role holder. | Use evidence-use, source-use, standard-use, requirement-use, status-use, or publication-use relation. |
| Status branch | `Approved`, `Ready`, `Satisfied`, or `Valid` is handled as a role. | Use `F.10` or the direct status-use pattern. |
| Access role as work role | RBAC or permission label is used as proof of work-facing role assignment. | Recover the access or policy relation first; create a work-facing role assignment only if actual work attribution is current. |
| Cross-context role reuse | BPMN participant, RBAC role, PROV activity, or local team role are treated as one role. | Keep local assignment; use `F.9` for bridge or substitution claims. |

### F.6:11 - Consequences

Using F.6 makes role-assignment reasoning narrower and more reliable. A project can still use compact assignment strings and familiar role words, but reliance-bearing claims must expose the holder, role, bounded context, assignment-currentness disposition, and performed-by relation when actual work is claimed.

The cost is one extra split. A source sentence that says "role enacted" may become two or three typed statements: assignment admitted, work performed by that assignment, and evidence or status relation used for downstream reliance. That split is intentional. It prevents duplicate role ontologies and makes audit, bridge, capability, method, and status checks local.

### F.6:12 - Rationale

`U.RoleAssignment` is first-class because work attribution needs a stable holder-role-context relation. `RoleEnactmentFact` is not first-class because the fact is derived from a work occurrence and its `performedBy` assignment. Status-use and evidence-use relations are not branches of role assignment because their EntityOfConcern and slot discipline differ: they qualify claims, epistemes, standards, requirements, publications, gates, or decisions rather than assigning acting holders to work-facing roles.

The pattern is deliberately thinner than `A.15`. It does not rebuild the full role-method-work alignment. It gives Part F a local check that keeps role-description, naming, bridge, status, and work-attribution uses from crossing wires.

### F.6:13 - SoTA-Echoing and Source-Use

External traditions such as RBAC, BPMN, PROV, service management, safety standards, and process-notation traditions use "role", "activity", "participant", "status", "approval", and "execution" in different ways. F.6 does not treat any one tradition as semantic authority. The FPF role-assignment ontology recovers the bounded context and local role value first; assigns acting holders only through `U.RoleAssignment`; represents performed work through `U.Work`; and represents evidence, status, source, publication, and bridge claims through their own patterns.

When a source tradition is current, cite it through the direct source-use or bridge relation. Do not let source prestige, familiar vocabulary, or a popular notation collapse FPF kinds.

### F.6:14 - Relations

**Builds on:** `A.2` for `U.Role`, `A.2.1` for `U.RoleAssignment`, `F.4` for role-description epistemes, and `F.5` for role and type naming.

**Uses when current:** `A.2.5` for role-state and enactable-state admission; `A.2.2` for capability; `A.15`, `A.15.1`, `A.3.1`, and `A.3.2` for method, method description, work plan, and performed work; `A.6.5` when role-like words are relation positions.

**Direct governing patterns:** `F.10`, `A.10`, `B.3`, `C.28`, `E.17`, `E.17.0`, `E.17.2`, `E.10.D2`, gate, decision, publication-use, source-use, standard-use, requirement-use, and assurance patterns when the current claim is not work-facing role assignment or performed-work attribution.

**Coordinates with:** `F.9` for cross-context bridge claims; `F.18` for durable public names; `E.10` and `E.10.ARCH` for wording-use recovery when source language hides the current kind.

### F.6:15 - Footer Marker

F.6 closes when the project knows whether the current local claim is:

- an admitted or blocked `U.RoleAssignment`;
- an admitted or blocked performed-work attribution through `Work.performedBy = RoleAssignment` or `RoleEnactmentFact`;
- a lowered claim with missing holder, role, context, window, role state, capability, method, work, or source-currentness;
- or a non-F.6 status, evidence, source, publication, bridge, method, capability, gate, decision, or assurance claim.

### F.6:End

