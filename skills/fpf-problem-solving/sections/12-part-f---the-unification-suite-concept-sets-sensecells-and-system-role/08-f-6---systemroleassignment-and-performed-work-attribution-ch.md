## F.6 - SystemRoleAssignment and Performed-Work Attribution Check

> **Type:** Boundary and use pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### F.6:0 - Use This When

**Plain name.** Check whether this already admitted Work was performed under this exact system-role assignment.

Use this pattern only after A.15.1 has independently admitted a dated `U.Work` occurrence. Use F.6 when deciding whether that already admitted Work was performed under a particular assignment occurrence from the `U.SystemRoleAssignment` family. When it was, the direct world-side performed-under-assignment relation obtains. A separate assertion or record can identify the two occurrences and state that relation.

Typical moments:

- a work record says “Alice reviewed”, “Robot-7 inspected”, or “the operations team approved”, but the assignment occurrence is missing;
- a MethodDescription names a system-role kind and the project must connect actual Work to the assigned performer;
- source wording says `RoleEnactment`, “played the role”, or `Holder#Role:Context@Window`;
- a stronger appointment has a commission, position, or locus participant and must retain that occurrence identity during attribution;
- a report, standard, dashboard, or access label is described with role wording although it did not perform Work;
- a corresponding kind or assignment from another context is cited without a current Bridge and local occurrence.

**Primary EntityOfConcern.** One obtaining `performedUnderAssignment` relation occurrence between a `U.Work` occurrence and an assignment occurrence whose species is declared under `U.SystemRoleAssignment`.

**Primary working reader.** An engineer, operator, Method author, manager, or FPF author deciding whether a performed-Work attribution is grounded strongly enough for the next use.

**First useful move.** Confirm that A.15.1 has already admitted the exact dated Work without using an F.6 conclusion. Name that Work and the assignment occurrence under which it is said to have been performed. Recover the assignment's declared species and participant values, then confirm that the actual performer already has the A.13 core for this action, scope, working situation, and window and that this is the same obtaining assignment. Evidence supports those core facts; a characteristic profile enters only for a consumed Grade, autonomy or profile result, criterion-dependent characteristic, or assurance use. Ask what direct case fact links the exact pair. Confirm holder equality and interval coverage; those checks alone do not create the link. If the case does not establish the pair, retain the Work and leave only the attribution unresolved. Otherwise say plainly that the holder System performed the Work under that assignment.

**What goes wrong if missed.** Assignment is treated as proof of Work, a label replaces the assignment occurrence, a generic assignment duplicate erases a stronger appointment, or a log or report is made the performer. When several assignments overlap, interval coverage then attributes the same Work to all of them even though the exact pair was never established.

**What this buys.** Attribution is one thin relation. The holder System remains the actor, the assignment occurrence remains linked to its species and participant values, and Work, Method, capability, state, result, evidence, publication, and cross-context use remain separate.

**Not this pattern when.** Use `A.2` for the system-role kind and classification, `A.2.1` for assignment species and occurrence identity, `A.2.5` for assignment state, `A.2.2` for capability, and `A.15.1` for the Work occurrence. Use the direct evidence, source-reliance, publication, access, authority, permission, responsibility, status, gate, or decision pattern when that relation is current. Use `E.10.ROLE` and `A.6.RSIR` when *role* denotes another object or relation position.

### F.6:1 - Problem Frame

`U.SystemRoleAssignment` and `U.Work` classify different world-side occurrences. An assignment occurrence belongs to a declared species, relates fixed participant values, and lasts for one maximal uninterrupted interval in which its predicate remains true. A `U.Work` occurrence is dated. Their existence does not establish the additional attribution relation.

Use F.6 to state that missing relation between the Work and assignment occurrences. Every assignment species declares a holder slot, and each assignment occurrence supplies its actual holder System. F.6 exposes that holder only so the attribution can compare it with the actual performer already recovered through A.13 and used by A.15.1 to admit the Work; it does not discover a performer. This preserves a commission-sensitive or otherwise stronger assignment instead of replacing it with a generic duplicate.

A roster can assert the assignment; a log can assert the Work and attribution; evidence can support either assertion. Those epistemes help a system know or use the claim. They do not become relation participants or make world-side attribution obtain merely by being stored.

This separation matters because assignment, classification, state, ability, performance, result, evidence, and acceptance vary independently. A system can hold an assignment and do no Work. It can perform poor Work under a valid assignment. A report can accurately describe the Work without performing it.

### F.6:2 - Problem

Without the direct attribution relation:

1. **Assignment becomes Work.** Current assignment is treated as evidence that a system performed one occurrence.
2. **Performer comes from a label.** `Reviewer` or `Operator` is used without a holder and assignment episode.
3. **A stronger assignment is flattened.** A commission-sensitive appointment is replaced by a weaker generic record.
4. **Episodes do not cover.** Work is attributed outside the interval in which the exact assignment predicate obtains.
5. **Support becomes constitution.** A log, report, standard, dashboard, or decision is treated as what makes attribution obtain.
6. **Enactment is duplicated.** `RoleEnactment` or `RoleEnactmentFact` becomes another object beside Work and attribution.
7. **Locality is hidden.** A context word replaces the exact local kind, assignment species, Work locus, scope, or selected model-use structure.

### F.6:3 - Forces

| Force | Tension |
| --- | --- |
| Readability vs exact identity | Ordinary prose should stay short, while reliance-bearing use may need exact Work and assignment occurrences. |
| Attribution-facing holder projection vs actual-performer recovery | F.6 may expose the assignment holder for an exact equality check, while A.13 and A.15.1 have already recovered the actual performer independently. The projection must preserve every additional assignment participant. |
| Assignment vs performance | An exact assignment can be a participant in Work attribution; its existence, holder, and temporal coverage neither make the Work happen nor establish the attribution relation. |
| World-side obtaining vs knowledge | Missing support makes reliance unresolved, not Work unperformed. |
| Local interpretation vs cross-context reuse | Similar names or Bridges do not retarget Work to another assignment. |
| Thin attribution vs neighboring checks | Capability, state, Method, result, acceptance, and evidence can matter without becoming attribution participants. |

### F.6:4 - Solution

Treat performed-Work attribution as one direct relation species under `U.Relation`.

#### F.6:4.1 - Direct Relation Declaration

```text
performedUnderAssignment : U.Relation
  WorkOccurrenceSlot: U.Work, U.EntityRef
  SystemRoleAssignmentSlot: U.SystemRoleAssignment, U.RelationRef

when performedUnderAssignment(W, RA) obtains:
  attributedPerformerSystem(W, RA) := RA.HolderSystemSlot
```

`WorkOccurrenceSlot` names a dated Work already admitted under A.15.1 from independently grounded performance history, A.13-qualified actual performer facts, Method, extent, and containment. The typed slot consumes that completed membership result; F.6 neither helps establish nor reopens `W : U.Work`. The declaration-local `SystemRoleAssignmentSlot` names one occurrence of an admitted assignment species declared under `U.SystemRoleAssignment`. Its `U.RelationRef` names that occurrence and is limited to `U.SystemRoleAssignment`. Filling the two slots, matching the holder, or finding temporal overlap does not establish that this Work was performed under this assignment; the case must independently establish that link.

For an obtaining attribution:

```text
S = attributedPerformerSystem(W, RA) = RA.HolderSystemSlot
```

`S` is the admitted System already recovered as an actual performer through A.13 and used by A.15.1 to admit `W`; F.6 does not discover it. `RA` is the assignment under which that Work is now attributed. The projection exposes the holder already carried by `RA` only to test equality with `S`; it creates neither performerhood, Work, attribution, classification, nor a generic assignment occurrence and discards none of RA's additional participants.

`performedBy` remains only a deprecated source relation name. Read it through the direct Work-assignment relation only after A.13 and A.15.1 have independently established the actual performer and admitted Work, and after holder equality is checked. New practitioner-facing claims say that the already recovered performer System performed the Work under the assignment, or name `performedUnderAssignment` when the relation name is needed; they never make the assignment the performer or use F.6 to discover one.

No evidence, log, status, MethodDescription, result, publication, context record, or assignment-state assertion is a generic attribution participant.

#### F.6:4.2 - Obtaining and Occurrence Identity

The direct Work-assignment attribution is a world-side fact, separate from any assertion or evidence. A positive check requires all of the following:

1. `W` is one exact dated `U.Work` occurrence already admitted under A.15.1 from its independently grounded candidate-action history, A.13-qualified actual performer basis, Method actually followed, temporal extent, and containing-System relation; that admission neither assumes nor depends on this F.6 relation;
2. the actual performer `S` has the A.13 core for this action, scope, working situation, and window: `S` is an admitted System, satisfies and is classified under one exact local agential system-role kind, and holds the same obtaining assignment `RA`; evidence supports those core facts, while a characteristic profile is required only for a consumed Grade, autonomy or profile result, criterion-dependent characteristic, or assurance use;
3. `RA` is one named assignment occurrence of a declared `U.SystemRoleAssignment` species, with all identity-bearing participants and its rule recovered;
4. the case establishes that `W` was performed under `RA`, rather than deriving that link from a label, common holder, assignment existence, or temporal overlap;
5. `RA.HolderSystemSlot = S`, the admitted System that actually performed `W`; and
6. RA's species predicate obtains throughout the attributed temporal extent of `W`.

Conditions 1–3, 5, and 6 are five constraints on a valid attribution but do not establish it. F.6 reuses the obtaining A.13 assignment; it does not create the A.13 classification, assignment, evidence, optional profile, or Work. Failure of condition 4 or any constraint leaves `W : U.Work` intact and leaves only this exact assignment-bound attribution unasserted.
Two overlapping assignments held by the same System may satisfy all five constraints while the case links the Work to only one. Use that case fact; if it does not distinguish the assignments, leave the attribution unresolved rather than asserting both.

If attribution concerns only a temporal, episode, or operational part of a larger Work whole, first identify that part as its own `U.Work` occurrence under A.15.1. Do not hide an unidentified Work portion inside F.6.

When a receiver needs an explicit attribution occurrence:

```text
PerformedUnderAssignmentOccurrenceKey =
  <WorkOccurrenceSlot, SystemRoleAssignmentSlot>
```

This key identifies an already obtaining relation; it does not make one obtain. The attribution extent follows `W`. Extending an open Work interval or later recording its end does not create another attribution occurrence while both participants and the direct relation remain the same. Another Work occurrence, separately identified Work part, or assignment episode yields another possible pair whose relation must be checked independently.

An assertion can state the exact pair, and evidence can support reliance on that assertion. Neither the assertion nor its evidence constitutes the world-side relation. Missing evidence leaves reliance unresolved; missing pair grounding leaves the positive attribution unasserted. A demonstrated different performer, non-covering assignment, or false direct pair can support a stronger negative claim.

#### F.6:4.3 - Preserve the Exact Assignment Species

Before checking or relying on attribution, recover RA's declared species and occurrence. This distinguishes the assignment even when the final practitioner sentence omits its full declaration. Every species declares:

- a `HolderSystemSlot` whose `ValueKind` is `U.System`;
- a declaration-local `AssignedSystemRoleKindSlot` whose `ValueKind` is the exact local system-role-kind domain admitted for that species;
- every additional participant meaning and its `ValueKind`;
- the rule, applicability, and maximal uninterrupted occurrence identity.

An assignment occurrence supplies one participant value for each slot. In particular, it supplies one local system-role-kind value from the `AssignedSystemRoleKindSlot` domain; the value does not replace or narrow that declared domain.

A simple assignment may have only holder and kind. A project appointment may also have `ReviewCommissionSlot`. F.6 accepts both through the family ValueKind and holder projection while retaining the declared species and all participants that distinguish the assignment occurrence. Those participants and the assignment rule still do not establish that the Work was performed under the assignment; the case must establish that link separately. F.6 never creates a two-participant generic assignment beside the appointment.

Taxonomy, scheme, `KindSignature`, assertion, and `assignmentInterval` can interpret or describe RA without becoming participants by default. Verify temporal coverage from whether the assignment rule actually holds, not merely from a recorded interval.

Do not replace the species with one `Context` value. Recover what the source token denotes and use its direct pattern. It can denote a system or Work locus, claim scope, or selected `BoundedModelUseStructure`; those objects are neither interchangeable nor optional participants of generic assignment or attribution signatures.

#### F.6:4.4 - Attribution Check Sequence

1. Start from the exact `U.Work` occurrence already admitted by A.15.1 without an F.6 premise.
2. Recover the assignment occurrence, including its declared species, identity-bearing participants, rule, applicability, and time span.
3. Find the case fact that directly links this Work to this assignment; do not infer that link merely because the holder and interval match.
4. Confirm that the assignment holder is the actual performer.
5. Confirm that the assignment predicate obtains throughout the attributed Work interval.
6. When all five checks pass, state the F.6 relation or say plainly that the holder System performed the Work under that assignment. If the direct link, a participant, or a required constraint is missing, retain the admitted Work and leave only this assignment-bound attribution unresolved; do not select another covering assignment.
7. Keep assertions and evidence separate: they can support reliance on the attribution claim but do not make the relation obtain.
8. Send classification, assignment state, capability, Method, evidence, source use, result, acceptance, publication, bridge, responsibility, and authority questions to their subject patterns.

This sequence is application guidance, not a new check record or workflow object. Its first useful result is the readable exact relation, an unresolved exact pair with the missing fact named, or a corrected route to the direct neighboring claim.

#### F.6:4.5 - Method and Work Boundary

`performedUnderAssignment` has no Method participant. A separate claim may say that the Work enacts one exact semantic Method. The holder System performs the Work; the Work, not the performer or assignment, enacts the Method.

The assignment, system-role kind, capability, Method, and MethodDescription do not act or perform Work. Citing a description can identify, constrain, or support a receiving use of the Method, but it neither enacts the description nor establishes `D : U.MethodDescription`; use A.3.2 to test that membership separately.

#### F.6:4.6 - Direct Neighboring Relations

| Current question | Direct exit | Why it stays separate |
| --- | --- | --- |
| Does the assignment obtain? | `A.2.1` | The declared species and predicate, the occurrence's participant values, and the occurrence-identity rule precede attribution but do not establish it. |
| Does the holder count under its system-role kind? | `A.2`, C.3.2 | Classification is not supplied by attribution. |
| Does the assignment satisfy a state predicate? | `A.2.5` | State has its own predicate, relation, window, assertion, and evidence. |
| Can the holder perform the Work? | `A.2.2` capability and fit | Ability is not actual performance. |
| Which Systems actually performed a top-level or child Work occurrence? | Recover each exact performer through `A.13`, then let `A.15.1` independently admit that Work occurrence; add one F.6 check per exact performer–assignment pair only when the receiving question also asks under which assignment the Work was performed. | A team lead, coordinator, member relation, or covering assignment cannot substitute for the full actual-performer set. Every child Work keeps its own A.13 performer basis, A.15.1 admission, and Work-part relation; assignment and F.6 are added only for an expressly consumed attribution. Missing or failed F.6 leaves the child Work intact. |
| Did a passive test article participate in Work? | the domain rule that defines passive participation; if no such rule is current, `A.6.RCD` returns `missing-governor` | Holding a test-subject assignment does not make the article a performer or establish passive participation. |
| Which Method did the Work enact? | `A.15.1`, `A.3.1`, and A.3.2 only for a separate description-membership question | Method, description, and assignment do not become performers. |
| What supports the attribution assertion? | `A.10` or the direct evidence relation | Support concerns knowledge or use, not relation obtaining. |
| Which encountered material is relied upon? | `A.15.4` | Reliance on a visible item is not attribution. |
| What changed, first existed, was measured, evaluated, delivered, or accepted? | `A.6.1` only when the claim consumes one exact operation application or returned-value binding; `A.15.PROD` plus the subject's identity rule for a produced entity or its inception; `C.2.1` for a result episteme; otherwise the exact change, measurement, evaluation, delivery, or acceptance pattern | Each claim follows its own pattern, and none supplies a performer-attribution participant. An operation binding alone establishes neither production nor a result episteme. |
| Does another context have a corresponding kind or assignment? | `C.3.3`, `F.9`, `A.6.9` | A Bridge merges neither kind nor assignment and does not retarget Work. |
| Does a selected model-use structure change this attribution interpretation? | `A.1.1` plus the receiving assertion or use | Generic assignment and attribution gain no optional structure participant. |

#### F.6:4.7 - Source Shorthand and `RoleEnactment`

`Holder#Role:Context@Window` is readable source notation only. Recover the actual system, local system-role kind, assignment species and occurrence, and the object denoted by `Context`. The source spelling is not a signature.

When source wording says `RoleEnactment` or `RoleEnactmentFact`, recover dated Work and `performedUnderAssignment`. Do not retain a second enactment kind, fact object, or relation occurrence.

#### F.6:4.8 - Lightweight Use

After the Work–assignment link and its necessary constraints are established, ordinary use can stop at:

```text
InspectionWork-17 was performed by Robot-7 under InspectionAssignment-17.
```

Expose declarations and occurrence keys only when a dependent use must distinguish occurrences, cite one as a participant, compare assertions, or preserve provenance. If the assignment cannot be recovered, lower the claim to “Robot-7 is named as performer in record R” and state the source, reliance, and evidence claims under their direct predicates.

Another pattern may require a **complete A.13/A.15.1/F.6 basis** when its receiving use needs both admitted Work and precise assignment-bound performer attribution, and may point here instead of repeating this declaration and check sequence. That combined basis has a fixed order: A.13 first supplies every performer's exact System, local agential kind and criterion, classification, obtaining assignment, needed scope, working situation, window, and adequate core evidence; A.15.1 independently admits the dated Work from its performance history, at least one obtaining `enactsMethod` relation, extent, and at least one obtaining locally declared Work-to-System containment relation; only then does F.6 test every required exact Work-assignment pair through the same obtaining A.13 assignment. The phrase is never an A.15.1 membership test. A missing F.6 relation preserves `W : U.Work` and leaves only the precise attribution unresolved. A characteristic profile remains conditional, and another enactment or containing-system relation is named only when the receiving use relies on it.

### F.6:5 - Invariants

1. Every positive performed-Work attribution links one dated `U.Work` occurrence to one assignment occurrence of a declared `U.SystemRoleAssignment` species.
2. `SystemRoleAssignmentSlot` accepts the family and preserves the assignment's declared species, all participants, rule, applicability, and occurrence identity.
3. The actual performer is the admitted System in `RA.HolderSystemSlot`; the assignment and kind do not act.
4. RA's predicate obtains throughout the attributed Work interval; a declared window alone does not establish coverage.
5. The species declaration, occurrence participant identity, holder match, and time coverage constrain but do not establish the Work–assignment link.
6. Overlapping assignments are checked pair by pair; an unresolved basis never licenses attribution to every covering assignment.
7. Every positive precise assignment-bound performer attribution starts from an already admitted Work whose actual performer has the A.13 core for the exact action, scope, working situation, and window, then adds its own F.6 link through the same covering assignment occurrence. A characteristic profile remains conditional on its receiving use. A lead, team, member, coordination, allocation, or responsibility claim substitutes for none of these.
8. A passive assigned System is not thereby a performer. Any claimed passive participation needs a rule that defines it; otherwise A.6.RCD returns `missing-governor`.
9. Assignment does not prove performance, and attribution proves neither classification, capability, state, Method validity, result quality, responsibility, authority, nor acceptance.
10. `RoleEnactment` wording is repaired to Work plus `performedUnderAssignment`; no duplicate object remains.
11. Assertions, logs, rosters, evidence, identifiers, and publications can support or designate an attribution but do not constitute it.
12. Missing evidence leaves reliance unresolved; a missing case fact linking Work and assignment leaves the positive attribution unasserted.
13. An episteme does not fill `HolderSystemSlot` because it describes or supports Work.
14. Cross-context correspondence changes neither assignment identity nor Work attribution.
15. Reduced prose may omit only an assignment identifier unused by the receiving claim, and only after the complete Work–assignment basis remains recoverable.
16. The Method enacted by W remains a separate fact; only the admitted holder System performs W.

### F.6:6 - Reasoning Rules

- Accept the attribution only when the case establishes that `W` was performed under `RA`, `W` is a dated Work occurrence, `RA` is a named assignment occurrence with its participants and rule recovered, the assignment holder performed the Work, and the assignment rule covers the Work interval. A short account may then say that the holder System performed `W` under `RA`.
- If `W` and `RA` exist, the holder performed the Work, and the assignment covers the interval, do not infer the Work–assignment link. Check the case fact that establishes the link or leave it unresolved.
- If current support for an attribution statement is inadequate, reliance on that statement is unresolved. Do not infer that the Work was not performed under the assignment, and do not treat the statement or evidence as what makes the link true.
- If a source episteme merely names a performer or *role*, do not claim attribution until the Work and assignment are identified, the case establishes their link, the holder matches the performer, and coverage is checked.

### F.6:7 - Archetypal Grounding

#### F.6:7.1 - Robot Inspection

`MaintenanceInspectionAssignment` is a declared species under `U.SystemRoleAssignment`. Its participants include a `HolderSystemSlot` for the assigned System and a local `AssignedSystemRoleKindSlot` whose value is an `InspectorSystemRole`. Its rule applies within the Plant A maintenance scheme and says that the fixed holder is assigned under that kind to supply the inspection contribution; one occurrence is the maximal uninterrupted interval for which that rule stays true for the same participants.

```text
InspectionAssignment-17 : MaintenanceInspectionAssignment
  HolderSystemSlot: Robot-7
  AssignedSystemRoleKindSlot: InspectorSystemRole
  predicateTrueInterval: [2026-07-13T09:00, 2026-07-13T17:00]

InspectionWork-17 was performed under InspectionAssignment-17.
```

The case basis directly links that Work to that assignment; the matching holder and interval only confirm necessary conditions. Robot-7 is the actor. Separately, the inspection Work enacts `TurbineInspection@Maintenance-2026` as its Method. `InspectorSystemRole`, a sensor capability, algorithm-possession wording, the Method, and `TurbineInspectionProcedure-v3` do not perform the inspection. Use A.3.2 to decide whether that last episteme is a MethodDescription. Calibration state, Method adequacy, report quality, and acceptance remain separate.

#### F.6:7.2 - Two Review Commissions

`ProjectReviewAppointmentAssignment` is a declared species. It declares three participant positions: `HolderSystemSlot`, local assigned kind, and `ReviewCommissionSlot`. `ReviewAssignment-A` and `ReviewAssignment-B` are two occurrences with Alice and `ReviewerSystemRole` in common but different commissions, and both cover the same interval. The case says that Alice performed `ReviewWork-A` under assignment A and `ReviewWork-B` under assignment B; it does not establish either crossed pairing. If the facts say only that Alice performed review Work while both appointments covered the interval, leave the attribution unresolved. The readable projection “Alice is reviewer” selects neither assignment and creates no generic assignment.

#### F.6:7.3 - Reviewer and Review Report

`CommissionReviewAssignment` is a declared species. It declares three participant positions: holder, local reviewer kind, and commission. Its rule applies to admitted review commissions and says that the fixed holder is appointed under the identified commission to supply the review contribution; one occurrence is the maximal uninterrupted interval for which that rule stays true. `ReviewAssignment-82` is its occurrence for Alice and `Commission-82`, and it covers `ReviewWork-82`. The case identifies this as the assignment under which Alice performed that Work. `ReviewReport-82` is a separate `U.Episteme`; it may state the attribution, and evidence may support reliance on that statement, but neither creates the Work–assignment fact. Use A.15.PROD only for a current report-inception claim. The report is neither the performer nor the attribution.

#### F.6:7.4 - Standard Used during Safety Work

A safety MethodDescription cites a standard, and source prose says that the standard has a “normative role”. Do not create an assignment for the standard. The standard remains an episteme in the external-rule, source-use, specification-use, or evidence relation selected by the claim.

A safety engineer or tool System can separately hold a covering safety-analysis assignment and perform dated safety Work. Attribution names the assignment occurrence and the case fact linking it to the Work; it does not use the standard as performer.

#### F.6:7.5 - Access Label and Approval Work

An access directory says Alice has `DB-Admin`. That entry describes an access or policy relation under its own scheme; it is not automatically an `ApproverSystemRole` assignment.

`ApprovalCommissionAssignment` is a declared species. It declares three participant positions: holder, local approver kind, and `ApprovalScopeSlot`. Its rule applies to admitted release scopes and says that the fixed holder is commissioned to supply approval within the identified scope; one occurrence is the maximal uninterrupted interval for which that rule stays true. `ApprovalAssignment-481` is its occurrence for Alice and the current release scope. If it covers `ApprovalWork-481` and the case identifies it as the assignment under which Alice performed that Work, the attribution is grounded. The directory entry may support a separate authorization claim but cannot substitute for the assignment or its link to the Work.

#### F.6:7.6 - Distributed Performers and Child Work

A.13 first recovers `ReviewTeam-9` and `Alice` as the two exact actual performers through `TeamReviewAssignment-9` and `MemberReviewAssignment-A9`, and A.15.1 independently admits `JointReviewWork-9`. Because this example expressly represents assignment-bound attribution for each performer, F.6 afterward establishes one relation for each Work-assignment pair through those same assignments. Neither assignment identifies or stands for the other performer. If `AliceFindingCheckWork-9` is separately admitted as child Work after its own A.13/A.15.1 basis passes, add its covering assignment and F.6 link only because this example also expressly attributes that child Work, and keep its Work-part relation to `JointReviewWork-9` separate.

#### F.6:7.7 - Passive Test Article

`TestArticle-7`, admitted as a `U.System`, holds `TestSubjectAssignment-7` throughout `ValidationWork-7`. `ValidationRig-2`, also admitted as a `U.System`, actually performs the Work under its own `ValidationPerformerAssignment-7`; only that Work-attribution link is established. The test article's assignment and presence during the interval do not make it a performer. If the project needs to say that the article participated passively in the validation, use the domain rule that defines that participation; while no such rule is current, return the A.6.RCD `missing-governor` result rather than treating the assignment as participation.

### F.6:8 - Bias Annotation

| Bias risk | Failure | Repair |
| --- | --- | --- |
| Record-first bias | A log or roster identifier is treated as a world-side relation. | Recover Work and assignment occurrences; keep the record as assertion or publication. |
| Generic-duplicate bias | F.6 demands a weaker assignment beside a stronger appointment. | Accept the family ValueKind and project the holder from the assignment occurrence through its declared species. |
| Universal-context bias | One context field replaces kind, species, extent, scope, locus, and model-use selection. | Recover each object and direct relation; add no optional generic participant. |
| Enactment reification | `RoleEnactmentFact` duplicates Work and attribution. | Use `performedUnderAssignment`. |
| Support-as-constitution | Evidence becomes an attribution participant. | Keep it in the relation supporting the assertion. |
| Assignment-as-performance | Staffing is treated as completed Work. | Name dated `U.Work` before attribution. |
| Bridge overreach | A corresponding kind or assignment licenses local attribution. | Recover the local assignment and preserve Work's exact attribution. |

### F.6:9 - Conformance Checklist

1. `WorkOccurrenceSlot` names one dated `U.Work` occurrence already admitted by A.15.1 without relying on F.6; its actual performers already have the A.13 core for the exact action, scope, working situation, and window, and any characteristic profile is required only by its own Grade, autonomy, criterion-dependent, profile, or assurance use.
2. `SystemRoleAssignmentSlot` names one assignment occurrence of a declared species under `U.SystemRoleAssignment` through `U.RelationRef`.
3. The assignment's declared species, all identity-bearing participants, rule, applicability, and uninterrupted occurrence identity remain recoverable. Each species keeps its SlotSpec `ValueKind` domains distinct from the participant values supplied by the occurrence; `AssignedSystemRoleKindSlot` takes one kind value from its declared local system-role-kind domain.
4. The case establishes that W was performed under RA; the assignment's existence, matching holder, and temporal overlap do not establish that link.
5. The assignment holder is the System that actually performed W.
6. The assignment predicate covers the selected Work interval; attribution to a Work part first identifies that part as `U.Work`.
7. Checks 2, 3, 5, and 6 constrain a valid attribution but do not by themselves establish it.
8. Overlapping assignments are distinguished by all their participants and by checking each Work–assignment link from the case; an unresolved case yields no blanket attribution.
9. Every positive precise attribution for a top-level or child Work occurrence has its own covering assignment and F.6 link to that already admitted Work; lead, team, member, allocation, coordination, and responsibility claims do not substitute.
10. A passive assigned System receives no performer attribution from assignment or overlap; any claimed passive participation uses the rule that defines it or returns the A.6.RCD `missing-governor` result.
11. F.6 uses `performedUnderAssignment` and introduces no `RoleEnactmentFact` or generic assignment duplicate.
12. Assertions and evidence may support reliance on the attribution claim but do not make it true.
13. Classification, assignment state, capability, Method, result, evidence, source reliance, publication, responsibility, authority, gate, and decision claims use direct patterns.
14. Any selected model-use structure is designated by the receiving assertion or use, not by an optional generic slot.
15. Missing evidence leaves reliance unresolved rather than proving non-attribution; missing pair grounding leaves the positive relation unasserted.
16. Source shorthand is unfolded before a receiver depends on hidden values.
17. The Method enacted by W remains a separate fact, and no kind, assignment, capability, Method, or description is made the actor.
18. A short practitioner sentence may omit declaration and occurrence detail only after the Work–assignment link and its constraints are established.

### F.6:10 - Common Anti-Patterns and Repairs

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Assignment proves Work | Holding is confused with dated performance. | Name the Work and assignment, then establish from the case that the Work was performed under that assignment. |
| Holder plus interval constructs attribution | Any covering assignment held by the performer is treated as the assignment under which W occurred. | Treat the matching holder and interval coverage as necessary checks; establish from the case which assignment the Work was performed under. |
| Overlap attributes to every commission | Two assignments with a common holder and interval both receive the same Work. | Recover all participants; establish only the Work–assignment link supported by the case, or leave it unresolved. |
| Lead or team assignment covers everyone | One assignment substitutes for the actual performer set. | Recover every exact actual performer of top-level or child Work through A.13 and let A.15.1 independently admit each Work occurrence. When precise assignment-bound attribution is current, give each performer its own same A.13 assignment and later F.6 link to the already admitted Work; missing attribution leaves Work intact. |
| Passive article becomes performer | A test-subject assignment and overlap are read as Work attribution or passive participation. | Attribute Work only to actual performers; use the rule that defines passive participation or return the A.6.RCD `missing-governor` result. |
| Work attributed by a system-role label | The holder and assignment occurrence are unavailable. | Recover the declared assignment occurrence, all its participants, and its holder. |
| F.6 creates a generic assignment | A stronger appointment is flattened or duplicated. | Keep RA's declared species and let `SystemRoleAssignmentSlot` consume the family. |
| Non-covering assignment | Work lies outside RA's predicate-true episode. | Use the covering assignment only when the case also links it to the Work; otherwise leave attribution unresolved. |
| `RoleEnactmentFact` retained | A duplicate object competes with Work and attribution. | Replace it with the F.6 relation between the Work and assignment. |
| Assertion or evidence creates the pair | A report or support path is treated as what makes the Work–assignment fact true. | Keep the assertion and evidence in their own relations; use them only to support reliance on the attribution claim. |
| Report as performer | A result or evidence episteme fills holder position. | Keep the report in its result, evidence, source, or publication relation. |
| Context shorthand becomes ontology | `Context` is inserted as a universal participant. | Recover the denoted object and the relation that actually applies. |

### F.6:11 - Consequences

**Benefits.** Assignment and Work remain independently identifiable, while attribution becomes a direct relation that can be cited, supported, corrected, or left unresolved. People, teams, organizations, machines, services, and software systems use the same pattern because every assignment occurrence exposes its admitted holder through the species-declared holder slot.

**Costs.** Reliance-bearing use must recover both the assignment occurrence and its declared species rather than stop at a familiar label. A compact sentence can split into assignment assertion, Work occurrence, attribution, Method enactment, change or production claim, result episteme, and evidence relation when the receiving use needs them.

**Limits.** F.6 determines neither classification, capability, readiness, Method validity, Work success, result acceptance, permission, authorization, responsibility, access, nor evidence sufficiency. It governs only attribution of one Work occurrence through one assignment occurrence.

### F.6:12 - Rationale

The direct relation is needed because assignment and Work have different occurrence identities. `performedUnderAssignment` is an additional world-side fact, not a field stored inside either participant. A separate assertion can say that the assignment obtains, the Work occurred, or their attribution relation obtains.

Using the family ValueKind in F.6 does not license a family-wide assignment signature. It lets F.6 project the actual holder from each occurrence through its species-declared holder slot while preserving any commission, position, locus, or other real participant. Creating a generic assignment for F.6 would duplicate the episode and weaken attribution identity.

Making a log, status, decision, or evidence item a participant would confuse attribution with knowledge of attribution. Creating `RoleEnactmentFact` would duplicate Work and the same relation. Treating a matching holder and temporal coverage as enough would instead attribute one Work to every overlapping assignment held by its performer. The two-participant relation avoids both errors: the case fact linking Work to assignment is checked separately, while assertions and evidence can change without rewriting the Work, assignment, or their link.

### F.6:13 - SoTA-Echoing and Source Use

**Internal basis, not an external SoTA claim.** A.2.1 and A.6.5 supply the declaration-local slot, domain, and participant-value discipline. A.2.5 keeps assignment state distinct from the assignment occurrence. A.6.REL supplies relation obtaining and occurrence identity. A.15.1 supplies dated Work and the actual-performer basis. F.6 uses these as its governing FPF neighbours; they do not replace comparison with external work.

| Source and status | Decision for F.6 | What F.6 uses and does not import | Affected loci and smallest source-driven revisit |
| --- | --- | --- | --- |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint — current ontology comparator for this narrow question | **Adapt.** Use its separation of classification, relational aspects, and relation occurrences to test whether F.6 keeps a system-role kind, an assignment species, an assignment occurrence, and Work–assignment attribution distinct. | Keep the distinctions. Do not import gUFO's category hierarchy, OWL commitments, reified-aspect design, or a direct identity between a gUFO category and an FPF kind. | §§4.1–4.3 and the assignment examples. Revisit them if this source materially changes the distinctions used here or a better direct Work–assignment account preserves more of FPF's identity and use requirements without greater practitioner burden. |
| W3C [PROV-O](https://www.w3.org/TR/prov-o/), 2013 Recommendation — representation lineage | **Adapt as a representation contrast.** Its qualified association keeps activity, agent, role, and plan separately addressable. | Use the separation when checking reports and provenance. Do not treat a PROV association as an FPF assignment occurrence, its role as a system-role kind, its activity as dated Work, or a provenance record as proof that attribution obtains. | §§4.2, 4.5, and §7.3. Revisit only if the qualified-association meaning used in this contrast changes materially. |
| [OCEL 2.0 Specification](https://www.ocel-standard.org/2.0/ocel20_specification.pdf), 2023 — event-log stress test | **Adapt as a logging stress test.** Its separate events, objects, and qualified relations test whether an exported log can preserve the identities F.6 needs. | Use the separation, not the log's identities as the world-side ontology. An event is not thereby FPF Work, a qualifier is not thereby an assignment or system-role kind, and a row does not establish that attribution obtains. | §§4.2, 7.2, and 7.3. Revisit only if the event/object/qualified-relation structure used by this test changes materially. |

The comparison is qualified on 2026-08-15 for this question and these source editions. gUFO is the current comparator because it directly addresses the classification–relational-aspect–occurrence separation at issue; PROV-O and OCEL answer narrower representation and logging questions and therefore serve as lineage and stress tests. A new edition number, publication status, or harmless wording change does not reopen the comparison. A material change to a distinction used above, or a competitor that offers a better direct Work–assignment attribution solution with at least the same exactness, readability, and use cost, reopens only the affected row and F.6 loci.

**Refresh by meaning, not by publication.** If A.2.1 or A.6.5 changes how an assignment species declares slot domains or how an occurrence supplies participant values, revisit §§4.3, 5, 7.1, and 9. If A.6.REL changes relation obtaining or occurrence identity, revisit §§4.1–4.2, 5, 7, and 9. If A.15.1 changes the actual-performer or covering-assignment basis, revisit §§4.4–4.6, 7, and 9. If a better direct Work–assignment solution changes the source decision, revisit §13 and only the solution or examples that depend on it. Wording or publication changes that leave these meanings intact require no refresh.

### F.6:14 - Relations

**Builds on:** `A.6.REL` for relation obtaining and occurrence identity; `A.2` for system-role kinds; `A.2.1` for direct assignment species; and `A.15.1` for dated Work.

**Uses when current:** `A.2.5` for assignment state; `A.2.2` for capability; `A.3` and `A.15` for Method and Work alignment; `A.10` for evidence; `A.15.4` for encountered-material reliance; `C.3.3`, `F.9`, and `A.6.9` for cross-context use; and `A.1.1` only when a selected model-use structure changes the receiving interpretation.

**Coordinates with:** `F.4` for system-role-kind descriptions; `F.5` and `F.18` for names; `E.17` for publication; and `E.10.ROLE` for ambiguous source wording.

### F.6:15 - Completion Conditions

F.6 use is complete when the reader has one of these results:

- one direct `performedUnderAssignment` relation between exact Work and assignment occurrences;
- an unresolved attribution assertion naming the missing exact-pair fact, assignment species or participant, coverage, performer, or support claim; or
- a corrected route because the current claim concerns classification, assignment, state, capability, Method, evidence, source reliance, result, publication, permission, authority, responsibility, access, gate, or decision rather than performed-Work attribution.

### F.6:End

