## A.15.4 - Work-Relevant Appearance-Based Reliance Repair

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `A.15.4` when a display, copied approval or generated explanation is about to justify work or reliance, but the prerequisite for that use is unclear. Ask three questions: **What am I about to do or rely on? Which fact, relation, decision, or result would warrant that use? Can I check that it holds for this case and time?** Keep the appearance at the lightest safe use until that prerequisite can be checked.

**Use this when.** Use this pattern only while appearance hides the direct object and test needed for one attempted use. If the direct question and the pattern that defines or tests it are already known, apply that pattern directly.

**First output.** Start with one ordinary sentence:

> This green tile points to `GateDecision-42`, but its link is stale. Use the tile only to find the current decision; do not deploy `Release-42` until that decision says `pass` for this release, target, scope, and window.

That sentence is a complete first result for this one-prerequisite use: it identifies the attempted use, appearance, missing prerequisite, allowed use now and return condition. If the prerequisite is recovered immediately, omit the note and apply its direct rule.

When a short worksheet is useful, unpack the same result without adding ontology:

```text
Attempted use:
Appearance:
Missing prerequisite:
Safe use now:
Blocked overread:
Return when:
```

Keep each independently required object, its subject pattern and test, required posture or currentness, and dependency on the attempted use separately recoverable. Keep a native reference when its governing rule or the receiving use requires one; an ordinary statement may identify its participants directly. Retain a sufficient existing note or accessible source account. Use `RequiredPositionEntries` when rows help compare or inspect the prerequisites; in that layout, use one row per direct object:

```text
RequiredPositionEntries:
  - SubjectPatternLocator:
    DirectObjectKind:
    ProjectSideObjectRef:
    RequiredPostureOrCurrentness:
    DependencyOnAttemptedUse:
```

These rows represent prerequisites defined by their subject patterns. When the analysis needs a separately referable claim, identify the C.2.1 episteme whose EntityOfConcern and ClaimGraph carry it; use an existing sufficient account when available. Split claims with different entities of concern. For a separated handoff, include the interpretation and source return the recipient would otherwise lose; a link is sufficient when that recipient can access and use it.

**First repair use in practice.** Choose the sufficient supported continuation: orientation or source finding, preservation of an early cue under A.16.1, ordinary planning, a bounded reversible probe, narrowed reliance, or a stop on the unsupported use. Admit WorkPlan content under A.15.2 only when that coordination claim is made.

**What goes wrong if missed.** The appearance is treated as proof of approval, gate passage, evidence, assurance, performed Work, currentness, or release authorization. Work then proceeds or stops while the relation or result that must support the claim is missing, stale, revoked, or contradicted.

**Subject of the repair in plain terms.** The pattern handles one attempted-use question. The appearance, attempted use, direct prerequisites, safe current use, and blocked overread retain the kinds and relations supplied by their own patterns.

**First repair checks.**
1. Name the appearance by its actual kind without treating it as the required relation or result.
2. Name the exact attempted use and the subject that use concerns.
3. Name the first missing prerequisite and the pattern that defines or tests it. A note stopping the unsupported use can finish there; a decision to proceed still requires every prerequisite consumed by that use.
4. Keep each independently required claim, instituted effect, relation occurrence, result, decision, assignment, evidence relation, currentness relation, or plan separately recoverable. Choose typed rows when their arrangement helps comparison or inspection.
5. Before allowing the attempted use, establish each required relation or result under its own criterion and match its applicable participants, scope, time and reliance basis to this case. Reuse an applicable established result; recheck what is changed, missing or expired.
6. A relevant permission or norm conflict, gate decision, or work-entry-readiness result remains a separate prerequisite. An unresolved conflict blocks only the affected use and does not make an independently obtaining grant cease.

**Not this pattern when.** Stay in A.15 when the question is only separation among the acting System, local system-role kind, classification judgment, direct `U.SystemRoleAssignment` species, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`. Stay in `A.15.2` for WorkPlan construction, `A.15.3` for declaration-local planned-filling content, and `A.15.5` for full-kit condition or work-entry readiness. Stay in `A.16.1` and `C.2.4` for pre-articulation cue preservation, `C.16.Q` for a dynamic-quality claim, `A.6.A` for an action invitation, and E.17 for publication-face exposure. When the direct evidence, gate, constraint, boundary, permission, authority, Work, or other claim is already known, use the pattern and test selected by the §3 lookup instead of A.15.4.

**What this buys.** The practitioner can keep a useful source-finding or limited-use continuation while withholding an unsupported stronger conclusion. Repeated ambiguity can then be repaired in the source or presentation that causes it.

### A.15.4:1 - Problem Frame

A display or copied claim can look sufficient for a decision while the required fact, relation or result remains hidden. The practitioner must recover the prerequisite for that particular use and decide which continuation its grounds support.

**Plain recognition line.** Follow the displayed claim or pointer to the required relation or result and its test. A recoverable native reference can serve that purpose; appearance alone establishes no authorization or other relied-on fact.

**Reliance-appearance and claim/effect-position discipline.** Recover the value required for the attempted use: an actual relation occurrence, decision/finding/status result, plan, Work occurrence, or claim about that object. Apply the criterion defined for that value. A project record may be a `U.Episteme` that names it, and a publication relation may expose that record; inspect its content under the governing predicate. Use a typed reference when the governing rule or receiving use needs that identity. If the prerequisite or its applicable test cannot be recovered, keep the appearance at orientation, source-finding, cue-pack preservation, repair request, or bounded-probe use.

**How to read the optional note and rows.** The labels below are worksheet prompts for objects and relations defined by their own patterns:
- `RelianceAppearanceRef` names the dashboard tile, credential view, copied wording, generated explanation, publication face, carrier, display, API wording, source-finding pointer, or low-articulation indication whose appearance is tempting the work or reliance use. `RelianceAppearanceKind` states its actual kind rather than making these items one kind. If the live value is a preserve-worthy early cue, use `PreArticulationCuePack` under `A.16.1`.
- `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef` name the use being justified: intended work, reliance on a claim, reliance on performed work, a work-relevant P2W claim, or a P2W chain position. These fields select the current branch; they do not create a durable kind.
- When the worksheet is selected, `RequiredPositionEntries` carries the prerequisite set for the attempted use, with one row per independently required direct object. Every row states `SubjectPatternLocator`, `DirectObjectKind`, the native `ProjectSideObjectRef` required for that object, `RequiredPostureOrCurrentness`, and `DependencyOnAttemptedUse`. The locator points to the pattern whose content defines, constrains, or tests the direct object; a proxy or navigation pattern is insufficient. One row may point to a required claim, another to an instituting speech act, grant, conflict finding, gate decision, assignment, evidence/currentness relation, plan, or other direct object; the row set creates none of them and never turns a claim into an instituted effect.
- `AllowedUseNow` states what use remains admissible after repair, such as orientation, source-finding, bounded reversible probe, narrowed reliance, or proceed-inside-recovered-relation.
- `AppearanceOverreadBlocked` names the false use that the reliance appearance would create by appearance, for example treating a dashboard color as gate passage or a copied approval as a current speech act.
- `RecoveryOrStopCondition` names the failed prerequisite and what must change. On return, recheck that premise and affected dependents; every prerequisite still needs an applicable result under its own criterion, currentness and reliance conditions. Reuse unchanged applicable results. A relevant `PermissionNormConflictFinding@Context` retains its separately recoverable A.2.8.PER disposition; an unresolved or norm-selecting result blocks the affected use without changing grant currentness.

Here evidence, attestation, provenance, and currentness relations retain their direct predicates and identity rules. A.10 makes the independently established relations, their sources, and the bounded reliance on them recoverable in a descriptive account; it defines no universal evidence-provenance relation. That account supplies no authorization by itself.

### A.15.4:2 - Problem - Cluster Boundary

A.15 remains the kernel for separating an acting System, exact local system-role kind, classification judgment, direct `U.SystemRoleAssignment` species, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and dated `U.Work`. A.15.4 starts only when a reliance appearance begins to justify a work or reliance claim and the team still needs to recover the required relation or result and the rule or test that applies. Recover a project-side reference when that rule or use needs one. If the question and its rule are already known, use them directly.

### A.15.4:2.1 - Forces

| Force | Tension |
| --- | --- |
| Work momentum vs. prerequisite recoverability | Teams need to keep work moving, but a reliance appearance can make the wrong claim look like work authorization while a required relation or result is still unnamed. |
| Cheap first note vs. high-impact reliance | Routine source-finding should stay light, while release, safety, compliance, exact system-role-assignment, credential-status, assignment-state, and gate cases need the distinctions and evidence required by their direct rules. |
| Publication face vs. required value | The visible carrier may be useful for orientation, but the work or reliance claim belongs to the project-side FPF kind, relation or result, and reference named by value. |
| Neighboring claims vs. local repair | A.15.4 can recover a missing prerequisite for the attempted work or reliance use, but evidence, gate, assurance, boundary, work-occurrence, and the permission/authority object selected by the §3 branch use the patterns and tests that define them. |
| Repeated ambiguity vs. individual burden | Repeated ambiguity about a required claim, instituted effect, relation, result, or reference should become prerequisite-lookup or source-relation repair work, not repeated manual reconstruction by every acting practitioner. |

### A.15.4:3 - Solution - Work-Relevant Appearance-Based Reliance Repair



#### A.15.4:3.3 - Core stress-case rule


**Ordinary local note.** The opening sentence or six-line note can stop at the first missing prerequisite when its result is a bounded stop or source-finding continuation. A decision to proceed must still satisfy all prerequisites required for that use.

For several prerequisites, a high-impact use, audit, handoff, or later reliance, keep each prerequisite separately recoverable together with the allowed use, blocked overread, and recovery or stop condition. Use a sufficient note, exact accessible source account, or worksheet selected for comparison or inspection.

The reliance appearance may be a tile, credential view, approval-looking memo, generated explanation, copied review, provenance mark, API wording, functional-description publication, or composed source-relation chain. The A.15.4 check asks whether every direct object required by the attempted use resolves and meets the posture and currentness predicates defined for that object, not merely whether a project-side reference is named or the reliance appearance is impressive, fluent, easy to inspect, or visually salient.

**Choose the worksheet detail by use.** The questions below help recover the distinctions required by the attempted use and each prerequisite's own rule. Such a rule may require assignment identity, assignment state, credential status, assurance, currentness, revocation, or cross-context detail. Keep that detail available in whichever expression serves the use. The fields can help an ordinary note or a separately identified C.2.1 account.

| Field | Working question |
| --- | --- |
| acting or affected system | Who would act, rely on the appearance or be affected? Use ordinary practitioner wording unless a precise System, Agent or dated Work claim is needed; then recover the applicable A.1, A.13 and A.15.1 basis. |
| system-role-assignment claim | Which assignment occurrence is being claimed, and which `U.SystemRoleAssignment` species declares it? A context field ending in `...SystemRoleAssignmentRef` is typed by `U.RelationRef constrained to U.SystemRoleAssignment` and resolves the occurrence. Keep capability, authority, responsibility, and Work attribution separately recoverable. |
| intended work or work target | Is the user planning intended work, relying on a dated `U.Work` occurrence or result, or making another reliance claim? Name that branch and its required relation or result before the reliance appearance guides it. |
| affected resource or claim | Which resource, claim, gate, credential, credential-status, system-role-assignment-state relation or assertion, evidence, approval, or source-finding pointer with an authority relation is supposedly affected? |
| context | Which bounded context, environment, project slice, API setting, connector setting, protocol setting, or relying situation makes the claim applicable? |
| policy or gate version | Which policy, gate profile, constraint version, method version, or register edition applies to the claim? |
| time window | During which window is the claim, effect, source relation, or recovered-use boundary claimed to hold? |
| currentness or revocation field | Is the source relation current, stale, revoked, superseded, expired, contradicted, or unknown? |
| issuer or required reference | Which issuer, project reference, register entry, source-currentness or credential-status record, speech act, gate decision, evidence relation, or work-occurrence record is required for the current use, and where is its criterion defined? |
| verifier or relying context | Who is checking or relying on the claim, and in which context? |
| evidence or attestation relation | Which independently established evidence, provenance, or attestation relation does the A.10 account cite for this claim and bounded use? |
| sourceRelationClass | Which `E.17:5.1b` source-relation class or claim-use class applies to the reliance appearance and required claim or use? |
| unsupported effect | Which requested work claim, reliance claim, required value, or downstream effect remains unsupported and needs narrowing, repair, reopening, probing, or blocking? |

Start with the A.15.4 first repair checks above when the reliance appearance is being used as a reason for intended work, reliance, or a work-relevant claim. If the direct question is already known, use the §3 lookup and apply its predicate; permission or authority uses the single branch there. Use A.15.4 while the required object, applicable test or basis for the attempted use still needs recovery.

**When a reliance appearance seems to authorize work or reliance.** Use A.15.4 when a publication, display, credential view, wording, or explanation looks like permission, prohibition, readiness, or evidence for intended work or reliance. Ask what the user intends to do next, what relation or result would make that use admissible, and which test and supporting facts that claim requires.

Name the record or relation that authorizes, forbids, records, or supports the required claim under its subject pattern. Use `E.17:5.1c` for the shared meanings of `orientation use`, `reliance use`, operative claim, unsupported downstream use, and `reopen trigger`; use `E.17:5.1d` when the primary question under repair belongs to another FPF rule or result.

Name the attempted use, recover each required object and apply its governing predicate. Keep episteme, publication and display distinct when those differences affect access or reliance. Follow a record's reference and inspect the content needed for obtaining, applicability, currentness and evidence. Cite the defining ClaimGraph when its identity changes the use; an ordinary pattern citation is otherwise sufficient.

**Positive repaired disposition.** After recovering every prerequisite consumed by the attempted use, confirm that each satisfies its own criterion, applicability, currentness and required evidence or source relation. Reuse unchanged applicable results. A permission/norm conflict retains its separate A.2.8.PER disposition: an unresolved or norm-selecting result blocks the affected use without cancelling an independently obtaining grant. State the next supported action; a failed prerequisite blocks only the use depending on it.

Reliance dispositions after prerequisite recovery:

| Work or reliance disposition | Use when | Minimum useful result |
| --- | --- | --- |
| Orientation or source-finding note | The reliance appearance is only a publication face, publication carrier, rendering, cue, retrieval cue, learning aid, or reversible local probe trigger. | Use a sufficient ordinary sentence or note. Name the first missing direct object in plain language; choose `RequiredPositionEntries` only when rows help the current comparison or inspection. |
| Routine reliance note | The team needs ordinary bounded reliance without release, safety, compliance, delegated system-role-assignment claim, assignment-state claim, credential-status claim, contested source relation, or cross-context reuse. | Keep each independently required object separately recoverable in a sufficient note, accessible source account, or selected rows. Name the acting or affected System, target, situation, window, assignment occurrence, capability, authority, or responsibility only when this attempted use relies on that value. Establish each claimed relation under its own rule and case facts; §3.4 distinguishes a missing rule, missing information and a failed test. |
| High-impact reliance disposition | The attempted use is external-impact, irreversible, release-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, revoked, system-role-assignment-state-claim-bearing, credential-status-claim-bearing, contested, or cross-context; or one prerequisite triggers high-impact conditions defined for it. | Keep the additional distinctions required by the attempted use and each prerequisite available in the selected expression. When permission or authority is current, choose exactly one row in the §3 branch rather than copying the whole catalogue here. |

If the worksheet helps, use only the rows and fields that the attempted use actually needs:

| Field | Value |
| --- | --- |
| `RelianceAppearanceRef` | Name the appearance being relied on by value, such as the dashboard tile, credential view, copied text, generated explanation, publication face, publication carrier, rendering, or source-finding cue. |
| `RelianceAppearanceKind` | Name the encountered object or relation kind without granting authority by appearance: selected `U.Episteme`, exact `EpistemePublicationRelation` occurrence or reference, publication form, MVPK face, publication carrier, rendering, `PublicationUnit`, dashboard tile, credential view, generated wording, copied wording, or source-finding cue. |
| `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef` | Name the use being justified by value: intended work, reliance on a claim, reliance on a dated `U.Work` occurrence, method-family selection, selected method, method of work, work plan, planned work, work result, result measurement, release reliance decision, non-work reliance claim, work-relevant P2W claim, or P2W chain position. A planned baseline remains claim content in one exact `U.WorkPlan`; performed work becomes `U.Work` only after its exact actual performer is identified and that performer's A.13 core basis is independently recovered and the dated occurrence is independently admitted through `A.15.1`; work-result measurement belongs with the evidence relation or result-measurement record that carries it. |
| `RequiredPositionEntries` | In this worksheet, use one row per independent direct object, whether it is a claim, instituted effect, relation occurrence, result with a pattern-defined criterion, gate decision, assignment, evidence/currentness relation, plan, or other prerequisite. Each row names its `SubjectPatternLocator`, exact `DirectObjectKind`, native typed `ProjectSideObjectRef`, `RequiredPostureOrCurrentness`, and `DependencyOnAttemptedUse`. The locator must identify the pattern whose content defines, constrains, or tests that direct object. Do not pack several independent prerequisites into one row or coerce their native refs into one generic `U.EntityRef` list. |
| `AllowedUseNow` | State the safe current use. `proceed-inside-recovered-relation` is allowed only after every required entry passes its `RequiredPostureOrCurrentness` and exact-use match; otherwise retain orientation, source-finding, bounded probe, repair request, narrowed reliance, or blocked unsupported use. |
| `AppearanceOverreadBlocked` | State the overread being blocked, such as treating display color as gate passage, copied approval as a current speech act, a credential screenshot as permission, or a generated explanation as evidence. |
| `RecoveryOrStopCondition` | Name the failed prerequisite and what would restore the required basis. Before proceeding, revisit that result and any dependencies affected by the change; reuse unchanged applicable grounds. Apply each direct object's criterion and keep separately required conflict, gate and readiness results recoverable. |

**Borrowed episteme and publication discipline.** A.15.4 borrows the `C.2.1`, `E.17`, and `E.24.PUB` distinctions. The claim-bearing FPF kind here is `U.Episteme`. When availability of its selected edition matters, name the exact `EpistemePublicationRelation` occurrence or reference. Publication forms, MVPK faces, publication carriers, renderings, `PublicationUnit` instances, and source-finding cues are separate kinds or relation positions in the case; no publication-kind shortcut replaces them. A planned baseline remains one exact `U.WorkPlan` episteme; any A.15.3 planned-filling rows remain declaration-local ClaimGraph content inside it. Launch values and finalization values remain their own project records, decision logs remain gate or decision records, performed-work evidence remains evidence, and dated Work occurrences remain `A.15.1` matters.

When a required relation or result, its project-side reference, or its test is incomplete, choose one `A.15.4` disposition after naming the work or reliance use and the exact direct objects it requires. Pick the lightest disposition that preserves practical work and recoverability:

1. Use the reliance appearance only for orientation or source-finding.
2. Reopen the selected source `U.Episteme` for the current claim, the exact `EpistemePublicationRelation` occurrence when availability is the issue, the source-bearing relation, register entry, direct record, or direct relation; or refresh source-currentness, credential-status, system-role-assignment-state, context-state, or another currentness relation.
3. Narrow the acting or affected System, an exact context field ending in `...SystemRoleAssignmentRef` when assignment identity is current, requested operation or work class, affected work target, affected resource, affected claim, context, and effective window until the recovered record or relation really covers the recovered use. Check capability through A.2.2, precise assignment-bound Work attribution through F.6, and authority or responsibility through its separately admitted direct predicate or exact missing governor.
4. Use a bounded reversible probe when its own conditions permit it. Add a WorkPlan only when coordination of that probe needs one; reversibility supplies no missing permission or safety condition.
5. Separate finding or exposing the missing source from assigning its repair. For source finding, ask an identified issuer, maintainer, verifier, holder, publisher, source contact, or acting user to expose the source or record using the direct source, publication, register, communication, access, or contact fact already available. For an allocation or duty to repair, apply §3.4 to that distinct claim. Keep the supported information request available and every additional missing gate, evidence, assignment, state, currentness, or boundary object separately recoverable.
6. Repair the `U.WorkPlan`, `U.MethodDescription`, dashboard label, source-relation link, or boundary wording that made the overread plausible.
7. Proceed only inside the recovered scope and window.
8. Block only the work claim or reliance claim that lacks the required relation.



#### A.15.4:3.4 - Repair assignment rule


**Missing source exposure versus repair assignment.** If a required source or record is unavailable, ask an identified issuer, maintainer, verifier, holder, publisher, source contact, or acting user to expose or locate it using the available direct source, publication, register, communication, access, or contact fact. Assign repair work through the applicable allocation rule and its case facts. A claim of responsibility, commitment or duty, permission, or authority needs its own predicate, participants and grounds: permission to repair does not by itself allocate the work, and allocation does not by itself institute a duty. Use A.2.8 for an asserted commitment or duty and the §3.5 permission branch when that claim is current. A system-role kind or assignment contributes only the applicability ground consumed by the particular rule.

Keep the reason for an unresolved repair claim precise under A.6.RCD: use `missing-governor` when the needed predicate or governing condition is absent, `missing-information` when a deciding fact is unavailable, and `factually unsupported` when sufficient facts fail the positive test. A failed positive test alone does not establish a negative claim. These limits apply to the affected allocation, duty or other stronger claim; retain a source-finding request or narrowed use whose own conditions are satisfied.

**Reliance-appearance kind check.** First name the actual kind of the reliance appearance: episteme, publication occurrence, publication form, carrier, rendering, dashboard tile, credential view, generated/copied wording, or source-finding cue. If it exposes a typed ref, follow that ref to the required relation or result and apply the criterion defined in its `SubjectPatternLocator`. Resolve an exact defining or constraining `ClaimGraph` only when the rule identity or edition changes this use. If the required object and its grounds remain unrecoverable, retain only the supported orientation or source-finding use. A record's content may supply those grounds even though its form alone does not.

**Source-relation guard.** A dashboard tile may guide release when its content exposes the applicable `GateDecisionResult`, scope and window, with the evidence and currentness grounds required for this reliance. Release urgency, display color, copied wording or fluency cannot supply a missing prerequisite.



#### A.15.4:3.5 - Prerequisite lookup table


Patterns and checks by required direct-object kind:

- cue-only orientation: use only for attention, learning, source-finding, or a reversible local probe trigger; stay with `A.16`, `A.16.1`, or `A.6.A` when those claims are being made.

**Permission and authority branch — use only when that is the live claim.** Do not route from *approved*, *authorized*, *allowed*, *may*, or the look of a permit. Ask what is true now and choose one row.

| Plain question | Pattern and required object | What closes or blocks this branch |
| --- | --- | --- |
| Did an admitted system perform an approval, authorization, delegation, grant, or revocation communication? | `A.2.9`; one `SA : U.SpeechAct` occurrence. | Identify the System that actually performed the communication and independently recover its A.13 core basis, then let A.15.1 admit the speech-act Work independently. If the reliance claim must also identify the assignment that covered the communication, or the policy makes that assignment material, name the assignment already used in the A.13 account and use F.6 to compare its holder with the performer. For a grant or revocation under A.2.8.PER:4.7, recover the required grantor assignment and the act performed under it, including its F.6 attribution; authority retains its separate grounds. Add the context, time, act type, and evidence needed for reliance. The assignment supplies neither performerhood nor authority. A `SpeechActRecord`, message, or carrier is not the act, and the act alone does not make an institutional effect obtain. |
| Does a policy-valid strong grant currently obtain for this beneficiary and action? | `A.2.8.PER`; one `GrantedPermissionRelation@Context` occurrence. | Match beneficiary, action specification, policy/context, scope/window, and instituting `SpeechActRef`. A valid revocation, supersession, or policy failure may prevent or end the grant. An unresolved same-case conflict can block this attempted use without making the grant cease to obtain; keep those results separate. This is the permission-side instituted effect. |
| Before action, did a current frame complete enough for this use contain no applicable prohibition? | `A.2.8.PER`; one `NonProhibitionFinding@Context`. | Name the frame, use, beneficiary/action, scope/window, and evaluation. A stale or incomplete frame returns `unresolved`, not permission. |
| Did dated Work actually exercise one obtaining grant? | `A.2.8.PER`; one `PermissionExerciseRelation@Context` occurrence. | Identify the actual performer, independently recover its A.13 core basis, and use A.15.1 to admit the dated Work. Match its action and scope to the grant, which must obtain throughout the exercise interval. An assignment beneficiary requires the named covering assignment with that performer as holder. A kind beneficiary requires a covering assignment with that holder, the named kind in its declared kind slot, and satisfaction of the policy's eligibility rule. For a party beneficiary, the performer must be that party or act under the obtaining on-behalf-of relation licensed by policy. Use F.6 when the receiving claim additionally needs precise assignment-bound attribution. No dated Work means no exercise; non-exercise is not violation. |
| After Work, did a current sufficiently complete frame find no applicable violation? | `A.2.8.PER`; one `NonViolationFinding@Context`. | Independently admit the acted-on Work under A.13/A.15.1. Recover the checked frame, its sufficient completeness and currentness, applicable prohibitions, evaluation and finding. Identify a separate dated evaluation Work only if that occurrence is asserted; then it needs its own admission basis. Add F.6 only for a consumed assignment-bound claim. Exercise or non-exercise alone settles no violation result; a stale or incomplete frame returns `unresolved`. |
| Do an obtaining grant and a current norm reach incompatible conclusions for the same beneficiary/action and overlapping scope/window? | `A.2.8.PER`; one `PermissionNormConflictFinding@Context`. | For `settledByApplicableRule`, cite the policy rule whose conditions match and which selects the governing claim. For `settledByDecisionResult`, recover the current `PermissionConflictResolutionResult@Context`, its `resolutionWorkRef`, `deciderSystemRef`, covering `deciderSystemRoleAssignmentRef`, independently obtaining `decisionAuthorityRelationOccurrenceRef`, selected grant or norm, scope/window and reopen condition. Independently admit that decision Work through A.13/A.15.1, then use F.6 for the required assignment-bound attribution. The direct result relation must connect that Work to the resolution result. If neither branch resolves the conflict, keep it `unresolved` and block the affected use. |
| Is an actual system or separately governed party obliged, prohibited, or given a recommendation-as-duty? | `A.2.8`; one `U.Commitment`. | Name the actual duty bearer, direct predicate, modality, exact referents, scope and window, applicable constitutive policy and rule, and actual instituting basis. A system-role kind or assignment may satisfy a rule antecedent but is not the duty bearer or commitment. The utterance, record, and carrier are not the commitment. |

A gate or readiness result remains an additional `A.21` or `A.15.5` prerequisite; it creates none of these objects. If the issue is only wording, classify it through `A.6` or the single permission-word branch in `A.6.B`. If only a permit, badge, message, record, or tile is visible, stay at orientation or source finding until one row above passes its stated test.
- system-role-assignment reliance: use `A.2.1` and name the assignment occurrence and its declared species. Assignment-state reliance instead uses the A.2.5 `SystemRoleAssignmentStateRelation`; credential-status reliance uses the exact proof or status result under `A.10`; context-state reliance uses its applicable direct state pattern and record; and a state established by a gate decision keeps its separate A.21 `GateDecisionResult`. Keep every required object separately recoverable.
- boundary, policy, API, schema, "allowed", "authorized", "approved", "recommended", or "guaranteed" wording: split the statement through `A.6` or `A.6.B`. When its live job is permission or authority, return to the branch above; the displayed word does not choose the object.
- gate decision or gate passage: cite `A.21` `GateDecisionResult` (the result referenced by the local `GateDecisionRef` used below), its `gateRef`, `profileApplicationRef`, `rationale`, gate profile and version, complete effective check set, check-application results and mappings, decision and action consequence, scope/window and recheck condition. Keep the native A.21:4.1 content recoverable. Use `DecisionLogRef` when a log supplies the access, audit or replay path or the applicable policy requires it; retain replay or freshness pins when the claim requires them.
- Flow constraint-validity witness: cite `A.20` `ConstraintValidityResult`, its evaluation state, outcome when present, and `witnessOrReason`. Keep `PathId` or `PathSliceId`, window, sentinel and pins when applicable to the claim. When an A.21 gate consumes that result, also recover the `GateCheckRef` resolving to the `GateCheckApplicationResult` that cites it through `sourceResultRef`.
- release, deployment, repair, inspection, or rollback work occurrence: cite the actual performer's A.13 basis, one dated `U.Work` occurrence independently admitted under `A.15.1`, and the direct evidence or provenance relation recovered through `A.10` when reliance on the occurrence is needed. If the reliance claim must also identify the assignment under which the Work was performed, check that relation separately through F.6.
- evidence, provenance, authenticity, currentness, copied-source, or generated-source relation: recover each independently established direct relation under its defining pattern. Use A.10 for the descriptive claim-bound account, currentness and bounded RelianceDisposition; the account cites the relations and their basis rather than creating them.
- an actual named assurance claim: apply B.3 to that claim and its limitations and reopen condition. A safety, compliance, trust, release, or characteristic claim first uses the direct pattern that defines or tests it; use B.3 only when that use separately requires assurance. Work-entry readiness uses A.15.5 and gate decisions use A.21.
- generated explanation: use `E.17.EFP` for explanation faithfulness or source-finding relation, then require the independently established source relation recovered through `A.10` for every operative claim that will be relied on.
- ambiguous approval, permission, or authorization wording: use the permission and authority branch above and choose by the plain question it answers now, never by the displayed word.

Recovered prerequisites for A.15.4 closure:
| Pattern or relation used | Recovered output for this A.15.4 repair | A.15.4-local use |
| --- | --- | --- |
| `A.6` or `A.6.B` | The recovered claim and its quadrant, with the pattern that defines or constrains it. A.6.B recommends stable `L-*`, `A-*`, `D-*`, and `E-*` IDs; material dependencies require an ID or canonical-location reference. A one-off sentence needs no separate Claim Register. | Use for wording, boundary, API, schema, or use-boundary recovery before intended work or reliance. |
| `A.10` | A descriptive claim-bound evidence-provenance account, the direct relations and currentness facts it cites, and its RelianceDisposition for the attempted use. | Use for evidence, provenance, authenticity, credential-currentness, copied-source, or generated-source recovery. |
| `B.3` | Typed assurance claim, no-assurance-use disposition, or rejected or downgraded assurance claim. | Use only when the work or reliance claim under repair relies on a typed assurance claim. |
| `A.21` | `GateDecisionResult` with its A.21:4.1 content, including `gateRef`, `profileApplicationRef`, check-application results and rationale, decision and action consequence, scope/window and recheck condition. Recover `DecisionLogRef` and replay or freshness pins when the actual use requires them. | Use for gate-passage reliance in the named scope and window. |
| `A.20` | `ConstraintValidityResult` with its evaluation state, outcome when present, and `witnessOrReason`, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim. | Use for flow constraint-validity reliance. |
| Permission or authority is current | Use the single branch above and carry the native object named by the selected row with its own closing conditions. | Do not mint or cite a generic permission-result object. |
| `A.13` and `A.15.1`; F.6 when the assignment matters | Identify the actual performer from the performance facts and independently recover its A.13 core basis; A.15.1 independently admits the dated `U.Work` occurrence. If this reliance must also state under which assignment the Work was performed, F.6 checks that separate relation. Add the direct evidence or provenance relation recovered through `A.10` when the reliance uses it. | Use for reliance on performed Work without turning the assignment check into a Work premise. |
| `E.17.EFP` | Explanation class, source-finding relation, and faithfulness relation over the selected source `U.Episteme`, with the exact `EpistemePublicationRelation` occurrence named separately when availability is material. | Use for generated-explanation faithfulness and source-finding before operative reliance. |

For a consequential reliance claim, keep every participant, condition and evidence basis required by its governing rules recoverable. The preceding lookup identifies their separate sources; it does not impose all listed objects on every case. A sufficient orientation, source-finding or reversible-probe result can stop at its narrower boundary.
Quick dispositions:

| Encountered case | First `A.15.4` disposition |
| --- | --- |
| Release dashboard tile exposing a source relation | If the tile is a current dashboard view of `A.21` `GateDecisionResult` with `decisionValue=pass` (recovered directly or through a `DecisionLogRef` that cites it) plus release scope or work target, environment, scope, window, gate profile, gate version, and direct support relation recovered through `A.10`, it may carry gate-passage reliance for that release and environment. |
| Release dashboard tile without current gate or evidence relation | Use the tile only for display or source-finding until the current `A.21` `GateDecisionResult` (recovered directly or through a `DecisionLogRef` that cites it), release scope or work target, environment or scope, time window, gate profile, gate version, and direct support relation recovered through `A.10` are recoverable. Open `B.3` only when an assurance claim is being made. |
| Copied review summary or copied approval | Treat it as copied wording and a currentness cue. If the intended use relies on permission or authority, use the single branch above and follow only the selected row. Gate passage still needs the `A.21` decision. Performed Work still needs its actual performer identified and that performer's A.13 core basis independently recovered and the dated occurrence independently admitted through `A.15.1`; if the relied-on account must also identify the assignment, check it separately through F.6. Reliance still needs the applicable direct evidence/currentness relation recovered through `A.10`. |
| Delegation chain with forwarded approval | Each link names delegator, delegatee, delegated operation or work class, affected work target, affected resource, affected claim, scope, window, the delegation record or relation permitting delegation, subdelegation allowance if any, revocation relation, currentness relation, and evidence relation. A forwarded approval is not delegated authority by copy alone. |
| System-role-assignment, revocation, assignment-state, or credential-status display | Resolve an assignment claim to both its occurrence and declared `U.SystemRoleAssignment` species. Resolve the other claims to the assignment-state relation, state-changing speech act, context-state record, credential proof or credential-status result, or gate decision with freshness field, revocation relation, or revocation record; visual display cannot defeat a higher-priority revocation or supersession relation. |
| Conflicting source relations | Do not resolve by color, visual salience, copied wording, or apparent recency. Name source-relation order, the decision or rule establishing that order, freshness policy, and supersession rule; the work claim, reliance claim, or effect is contested until resolved, while source-finding and bounded reversible probes remain available. |
| Register-backed credential-status view | Recover the entry episteme, publication and the rule under which the register is authoritative for this claim. Then test only the direct status, assignment, grant, exercise or finding that the attempted use consumes, with its evidence/currentness and revocation conditions. Any asserted Work needs A.13 and independent A.15.1 admission; add F.6 only when assignment-bound attribution is needed. The entry may be authoritative under its rule, but presence alone establishes neither exercise nor non-violation. |
| Rollback command-like cue | Treat it as a cue, or use `A.6.A` when it is an action invitation, unless the command record, authorization, work occurrence, performed-work result, or gate decision is recoverable. |
| Generated explanation says "authorized" | Use the explanation only to find source publications, claim-bound source relations, or required relations and results. If permission or authority is the live claim, route through the single branch above. The explanation itself supplies none of that branch's objects and proves neither gate passage nor performed work. |
| Extracted source publication, rewrite, representation shift, explanation, then gate or release claim | Return to the selected source `U.Episteme` and, where the break concerns availability, its exact `EpistemePublicationRelation` occurrence, form, or carrier; otherwise return to the source-bearing relation, transform record, evidence relation, explanation relation, or required relation or result at the first lossy or non-commutative transformation operation. The gate claim or release claim waits for the required transform record, evidence relation, explanation relation, gate decision, or assurance claim. |
| Repeated green-tile failures without recoverable source relation | Treat recurrence as upstream source-relation repair work: expose decision refs, fix dashboard semantics, add claim-bound source relations and currentness, revise boundary wording, or add review cues so the acting user is not repeatedly forced to reconstruct missing source relation. |

### A.15.4:3.1 - Archetypal Grounding - Worked Dashboard And Approval Examples

Constructed dashboard case:

At 09:20 UTC on 2026-05-08, a green tile for `Release-2026.05.08-prod` points to an unavailable gate decision. The immediate question is whether the release gate passed; the engineer uses the tile for source finding and withholds that claim. The source now yields `GateDecision-May08-prod`: `pass` for that release in production during 09:00–10:00 UTC, under the applicable GateProfile, with its required evidence and currentness basis. Matching the release, environment and window supports gate-passage reliance. It establishes neither deployment nor any separate permission or readiness prerequisite. A later superseding `block` decision reopens this reliance and the decisions depending on it. The repair exposes the decision reference, scope and window on the tile, so the next receiver can follow that decision directly.

| Step | Required record or relation |
| --- | --- |
| Question in this case | Whether the release gate passed for the named release, environment and window. The rows below identify the needed gate basis and separately conditional neighboring claims. |
| Gate decision record | Cite the current `A.21` `GateDecisionResult` (recovered directly or through a `DecisionLogRef` that cites it), gate profile, gate version, release scope or work target, scope, window, and replay or freshness pins. Without that record, the tile is not release authorization or gate passage. |
| Flow constraint-validity witness | Cite `A.20` `ConstraintValidityResult` and its `witnessOrReason` only when the claim is about flow constraint validity, not about the gate decision itself. |
| Evidence and currentness relation | Use `A.10` for the dashboard query, publication-carrier integrity, evidence refs, time, window, freshness field, revocation relation or revocation record, verifier context, relying context, and rival explanation such as stale display or copied status. |
| Assurance claim | Use B.3 when the attempted use requires a separately named assurance claim, with its target, evidence basis, limitations, and reopen condition. Safety, compliance, trust, release confidence, or a characteristic label alone does not establish that requirement. Use A.15.5 for work-entry readiness and A.21 for a gate decision. |
| Repaired gate-use reliance | With the decision and evidence relation recovered, rely on gate passage only for the named release scope or work target, environment, gate profile, gate version, time, and window. A claim that deployment happened still needs its actual performer identified and that performer's A.13 core basis independently recovered, the dated Work independently admitted through A.15.1, and the evidence or provenance relation needed for the relying context. If that claim must also identify the assignment under which deployment was performed, check the assignment separately through F.6. |
| Blocked overreads | The dashboard color does not create approval, deontic permission, compliance proof, rollback success, work occurrence, or assurance by display. |

Approval memo green-tile case:

An approval memo may carry an approval claim when it exposes the `A.2.9` `SpeechActRef`, the identified actual performer, that performer's independently recovered A.13 core basis, and the A.15.1 account that independently admits the speech-act Work. If the approval use must also identify the grantor assignment, or that assignment changes policy applicability, add `actingSystemRoleAssignmentRef : U.RelationRef constrained to U.SystemRoleAssignment` and use F.6 to compare its holder with the already identified performer. Keep affected release scope or work target, judgement context, time, window, publication-carrier refs, evidence refs, and the instituted effect separate. Authority is never supplied by the assignment. The memo supports only the bounded approval use defined in `A.2.9`; release, deployment, rollback, or other performed Work needs its own A.13/A.15.1 basis and any independently established support relation recovered through A.10 for reliance.

Credential-status and system-role-assignment-state green-tile case:

For a register-backed credential or assignment-state response, identify the entry episteme and its publication separately from the status assertion or `SystemRoleAssignmentStateRelation`. Apply the named register rule to determine which claim the entry supports, with the issuer/holder binding, relying situation, freshness and window it requires. Recover authorized entry-producing Work only when that rule or the current claim consumes it. Test the direct status relation or finding and its evidence under the selected §3 rule. A response's presence alone supplies no further Work, gate, permission or evaluation result.

Situation viewpoint prompts:

| Viewpoint or repair concern | Prompt |
| --- | --- |
| Acting practitioner | What can I safely do next without turning the encountered episteme or episteme publication into unsupported work or reliance justification? |
| Release engineer | Which gate decision is current, and does this question also require a separately established deployment Work or other prerequisite? |
| Source, gate, evidence, or assignment-record contact | Which source-currentness value, assignment-state relation or assertion, credential-status value, decision ref, or evidence relation needs exposure? Which direct source, publication, register, communication, access, or contact fact supports that request? For an allocation or duty to repair, apply §3.4 to its distinct predicate and case facts. |
| Audit or peer-review viewpoint | Which prerequisite, object, and test in the §3 lookup must be recoverable? If permission or authority is current, which one row in that branch answers the live question? |
| Boundary claimant | Is the operative claim clear? If wording still hides its predicate or governed value after F.19, use A.6 or A.6.B to recover it. |
| Manager | Is repeated ambiguity prerequisite-lookup or source-relation repair work rather than another manual check for the acting practitioner? |
| LLM user or tool user | Which required relation, result, or source relation does the explanation help find, and which operative claims still need an independently established source relation recovered through `A.10`? |
| Security or compliance source contact | Which revocation relation, currentness relation, proof, credential-status record, system-role-assignment-state assertion, source-relation order, or supersession relation needs exposure, and which direct source, register, communication, access, or contact fact supports asking for it? For a repair allocation or duty, use §3.4 to recover that claim's rule and grounds and distinguish missing information from a failed test. |
| Model or data documentation steward | Which intended use, evaluation condition, version, window, limitation, and evidence relation bound the model or data documentation? |
| Assurance viewpoint | Which named claim actually has a `B.3` assurance claim, with what assurance tuple, evidence relation, limitations, and reopen condition? |

Search cues for A.15.4 include: approval, approval-looking display, authorization, authorization-looking display, permission, permission display, allowed wording, green dashboard, release tile, release readiness, model card, datasheet, data card, provenance, provenance mark, attestation, attestation label, credential, credential badge, generated explanation, copied review, copied approval, review summary, compliance-looking mark, delegation, delegation display, revocation, revocation status, gate passed, gate passage, rollback successful, rollback cue, and assurance label. These are retrieval cues only; decide the required relation or result, the pattern whose content defines or tests it, and the project-side reference from the work or reliance question under repair, not from the displayed word, publication-carrier name, or source name.

Use the prerequisite lookup in §3.5 once the direct question is clear; return to A.15.4 only if an appearance still hides that question or its basis.

For a state label intended to guide action, expose the source reference and the scope, time and currentness needed by that action. For example: `Gate decision: pass; GateDecisionRef; release; environment; window`. Add a denied overread only when it is locally plausible and changes the use; F.19 governs that wording decision.

For incident learning, retain only the content needed to explain or repair the overread: encountered selected episteme, publication occurrence, form, or carrier; work or reliance claim under repair; required relation or result, its `SubjectPatternLocator`, and project-side reference; acting or affected System; a context field ending in `...SystemRoleAssignmentRef` only when assignment identity matters to F.6 attribution or another direct relation that independently obtains; separately recoverable capability, authority, and responsibility claims when current; affected target, context, and window; missing or stale source, publication occurrence, source-bearing relation, register entry, or project-side reference; the direct source, publication, register, communication, access, or contact fact supporting a cheap exposure request; and, only for an allocation or duty to repair, its distinct rule, case facts and any unresolved ground under §3.4; plausible overread; safe disposition; and smallest upstream repair.

Contestability and redress relation: when an authority-looking case affects assignment state, credential status, access, assignment, responsibility, release blockage, compliance claim, or safety-impacting Work, name the available challenge, review, redress, communication, source, publication, register, access, or contact relation before the work claim or reliance claim hardens. Recover the disputed source relation or claim, affected use or harm, allowed evidence or argument, possible disposition change, outcome route, and reopen trigger. Keep source exposure available under its own access conditions. A claim that a System has a duty to conduct later review or repair needs that duty's bearer, predicate and instituting basis; allocation and permission remain separate claims under §3.4. An unresolved duty limits that assertion, while a challenge can continue under its own established conditions.

Lintable overread cues:

| Lint signal | Required relation or result named by value |
| --- | --- |
| Ambiguous `approved`, `authorized`, `allowed`, `recommended` or `guaranteed` wording | First read the full claim under F.19. If its governed meaning remains unclear, use A.6/A.6.B; route a permission or authority question through the branch above. A word alone selects no object. |
| Dashboard tile, credential-status color, system-role-assignment-state color, or release tile used as release evidence or gate passage | Require `A.21` `GateDecisionResult` (recovered directly or through a `DecisionLogRef` that cites it) plus direct evidence and currentness relations recovered through `A.10`. A displayed assignment-state label is neither `SystemRoleAssignmentStateRelation` nor its assertion. |
| Register screenshot or entry used as status, permission, assignment or gate evidence | Recover the entry and publication, applicable register rule, direct object or finding, and required evidence/currentness. Identify any entry-producing, exercised or evaluation Work only when the rule or occurrence claim requires it, then apply A.13/A.15.1 and conditional F.6. A register entry may support the rule's exact claim; its presence alone establishes neither actual exercise nor non-violation. |
| Generated explanation uses `authorized`, `approved`, or similar wording | Use `E.17.EFP` for explanation/source-finding and `A.10` to recover the independently established source relation for the claim; if permission or authority is current, choose one row in the single branch above. |
| Model card, datasheet, label, or note cited as readiness, safety, compliance, or release confidence | Recover the direct readiness, safety, compliance, or release claim and its criterion, intended-use match, evidence, and limits. Use A.15.5 for work-entry readiness, A.21 for a gate decision, and B.3 only for an independently current named assurance claim. |
| Provenance or attestation label cited as truth, safety, release, permission, or authority | Require the bounded `A.10` provenance/process-trace claim plus the applicable pattern and test for the relied-on truth, safety, release, permission, or authority claim. For the last two, use the single branch above; the label is not its result. |
| Evidence, assurance, gate, or work-occurrence words without the relation or result that carries that claim or effect | Recover the independently established support relation through A.10, the separately named B.3 assurance claim, A.21 gate decision, or A.15.1 work-occurrence account as required by the attempted use. |

Stress cases for practice:

| Case | Expected A.15.4 disposition |
| --- | --- |
| Green release dashboard tile with no `GateDecisionRef`. | Source-finding only; recover the `A.21` `GateDecisionResult`, directly or through a decision log that cites it, plus `A.10` evidence before gate-passage reliance. |
| Copied approval from last month. | Treat the copy as a source-finding cue; use the permission/authority branch above to choose the one live question, then recover currentness and evidence for that selected object. |
| Register-backed credential badge screenshot after revocation. | Recover the entry, publication, status rule, direct status and required evidence/currentness/revocation basis. Add entry-producing Work only when the rule consumes it. A valid revocation blocks reliance even while the old entry remains visible. |
| Register entry says `grant exercised; no violation`, but matching actual Work is unavailable. | Keep those claims unresolved. Recover the acted-on Work under A.13/A.15.1, the exercise predicate and the sufficiently complete current checked frame. A separate evaluation Work is needed only when that occurrence is claimed; it then needs its own basis. Add F.6 only for consumed attribution. Entry presence establishes neither result. |
| Generated explanation says `authorized by policy`. | Use `E.17.EFP` for explanation/source-finding and `A.10` to recover the independently established source relation for the claim; if permission or authority is current, choose and verify one row in the single branch above. |
| Boundary wording says `guaranteed approved for production`. | Split the sentence through `A.6` or `A.6.B`; use `A.6.C` for agreement-like or promise-bearing content and the single permission/authority branch above only for the permission or authority claim that remains. |
| Dashboard says green while decision log says blocked. | Treat as conflicting source relations; name source-relation order, the decision or rule establishing that order, freshness policy, and supersession rule before the work claim or reliance claim is used. |
| CRISPR lab dashboard says the guide edit is ready. | Treat the dashboard as orientation or source-finding until the protocol publication or protocol record, approval record or gate record, exact direct system-role-assignment occurrence when assignment identity matters, evidence relation, current lab context record, and `U.WorkPlan` for the intended edit are recoverable. Recover capability, authority, responsibility, permission, and Work attribution separately when current. If the question is full-kit or work-entry readiness for the intended edit, use `A.15.5`; the readiness tile still does not create biological-intervention authorization, deontic permission, safety, or performed Work. |

### A.15.4:3.2 - Archetypal Grounding - High-Impact Reliance-Repair Slice

In this constructed case, a lab manager sees `CRISPR-guide-G42 ready` and a copied approval. The intended use is to determine the next permitted preparation or intervention step. The local policy separately requires the following prerequisites; this is not a universal kit for all appearance-repair cases.

```text
A.15.4 structured local note:
  RelianceAppearanceRef: B17-G42-GreenTile plus B17-CopiedApprovalMessage
  RelianceAppearanceKind: dashboard display plus copied wording
  WorkOrRelianceUseKind: intended work
  WorkOrRelianceUseRef: B17-GeneEditIntervention
  RequiredPositionEntries:
    - EntryId: B17-PROTOCOL
      SubjectPatternLocator: E.24.PUB
      DirectObjectKind: EpistemePublicationRelation
      ProjectSideObjectRef: B17-ProtocolPublication-e5
      RequiredPostureOrCurrentness: obtains; protocol edition e5 is currently available to the B-17 lab audience for this intervention use
      DependencyOnAttemptedUse: supplies availability of edition e5; selecting that edition for the intended Work also requires the intervention's protocol-applicability rule and case facts
    - EntryId: B17-GRANT-ACT
      SubjectPatternLocator: A.2.9
      DirectObjectKind: U.SpeechAct occurrence
      ProjectSideObjectRef: B17-GrantSpeechAct
      RequiredPostureOrCurrentness: actual performer identified; performer's A.13 core basis independently recovered; speech-act Work independently admitted through A.15.1; the grantor assignment required by A.2.8.PER:4.7 is recoverable and F.6 establishes that the act was performed under it, with its holder matching the performer; recognized by the current grant policy
      DependencyOnAttemptedUse: grounds B17-InterventionGrant; the act itself is not permission
    - EntryId: B17-GRANT
      SubjectPatternLocator: A.2.8.PER
      DirectObjectKind: GrantedPermissionRelation@Context occurrence
      ProjectSideObjectRef: B17-InterventionGrant
      RequiredPostureOrCurrentness: obtains and is current for the exact beneficiary, intervention action, sample batch, scope, and window, with no valid revocation or supersession ending the grant
      DependencyOnAttemptedUse: the intervention requires this strong grant
    - EntryId: B17-CONFLICT
      SubjectPatternLocator: A.2.8.PER
      DirectObjectKind: PermissionNormConflictFinding@Context
      ProjectSideObjectRef: B17-InterventionPermissionNormConflictFinding
      RequiredPostureOrCurrentness: current disposition=settledByApplicableRule; B17-ConflictPrecedenceRule-e2 matches this beneficiary, intervention action, sample batch, scope, and window and selects the grant for this attempted intervention
      DependencyOnAttemptedUse: an unresolved or norm-selecting disposition blocks AllowedUseNow for this intervention; the finding neither revokes nor ends B17-InterventionGrant
    - EntryId: B17-CONFLICT-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: C.2.1 episteme carrying an A.10 evidence-provenance account
      ProjectSideObjectRef: B17-ConflictFindingEvidence
      RequiredPostureOrCurrentness: supports only the current B17-InterventionPermissionNormConflictFinding disposition and the applicability of B17-ConflictPrecedenceRule-e2 to this exact attempted use
      DependencyOnAttemptedUse: supplies the evidence/currentness path for B17-CONFLICT without becoming the finding, rule, or grant
    - EntryId: B17-GATE
      SubjectPatternLocator: A.21
      DirectObjectKind: GateDecisionResult
      ProjectSideObjectRef: B17-InterventionGateDecision-e2
      RequiredPostureOrCurrentness: current GateDecisionResult with decisionValue=pass under the applicable GateProfile application, with its DecisionLog recoverable
      DependencyOnAttemptedUse: the current lab policy separately requires gate passage; this decision does not create the grant
    - EntryId: B17-WORK-ENTRY
      SubjectPatternLocator: A.15.5
      DirectObjectKind: C.2.1 result episteme carrying an A.15.5 readiness claim
      ProjectSideObjectRef: B17-WorkEntryReadiness-e3
      RequiredPostureOrCurrentness: current A.15.5 readiness claim for the exact plan item and intended B17-GeneEditIntervention in B17-GeneEditWorkPlan-e4, performer, kit, context, and entry window; ReadinessResultValue=ready, seeking a separately governed commitment is its stated next move, and no StopCondition is triggered
      DependencyOnAttemptedUse: the current lab policy separately requires work-entry readiness; readiness does not create the grant or gate decision
    - EntryId: B17-ASSIGNMENT
      SubjectPatternLocator: A.2.1
      DirectObjectKind: B17EditorSystemRoleAssignment, a direct species of U.SystemRoleAssignment
      ProjectSideObjectRef: B17-EditorAssignment
      RequiredPostureOrCurrentness: obtains, names the intended performer as holder, and covers the proposed Work window
      DependencyOnAttemptedUse: supplies the holder-and-kind condition consumed by the grant beneficiary branch; any later precise Work attribution requires its own F.6 check after Work admission
    - EntryId: B17-PROTOCOL-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: C.2.1 episteme carrying an A.10 evidence-provenance account
      ProjectSideObjectRef: B17-ProtocolPublicationEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-ProtocolPublication-e5 obtains and exposes protocol edition e5 for this lab audience and intervention use throughout the decision window
      DependencyOnAttemptedUse: supplies the publication/currentness evidence required for B17-PROTOCOL without standing in for that publication relation
    - EntryId: B17-GRANT-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: C.2.1 episteme carrying an A.10 evidence-provenance account
      ProjectSideObjectRef: B17-InterventionGrantEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-InterventionGrant obtains and is current for this beneficiary, action, batch, scope, and window, including the instituting act, policy, revocation, and supersession sources used by that claim
      DependencyOnAttemptedUse: supplies the evidence/currentness path required for B17-GRANT without creating or replacing the grant
    - EntryId: B17-GATE-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: C.2.1 episteme carrying an A.10 evidence-provenance account
      ProjectSideObjectRef: B17-InterventionGateEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-InterventionGateDecision-e2 is the current GateDecisionResult with decisionValue=pass for this attempted use under its GateProfile application, with its DecisionLog recoverable
      DependencyOnAttemptedUse: supplies the evidence/currentness path required for B17-GATE without becoming gate passage
    - EntryId: B17-ASSIGNMENT-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: C.2.1 episteme carrying an A.10 evidence-provenance account
      ProjectSideObjectRef: B17-EditorAssignmentEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-EditorAssignment obtains, has the intended performer as holder, and covers the proposed Work window
      DependencyOnAttemptedUse: supplies the evidence/currentness path required for B17-ASSIGNMENT without creating or extending the assignment
    - EntryId: B17-PLAN
      SubjectPatternLocator: A.15.2
      DirectObjectKind: U.WorkPlan
      ProjectSideObjectRef: B17-GeneEditWorkPlan-e4
      RequiredPostureOrCurrentness: current plan for the intended performer, intervention, sample batch, method, resources, and window; not actual Work or permission
      DependencyOnAttemptedUse: coordinates intended Work; after the other entry prerequisites pass, seek the separately governed commitment required by this case before starting
  AllowedUseNow: source-finding and prerequisite refresh only; do not intervene while any entry is absent or fails its required posture or currentness
  AppearanceOverreadBlocked: tile color and copied message do not authorize biological work or prove safety
  RecoveryOrStopCondition: revisit each missing or failed prerequisite and its affected dependencies; retain unchanged applicable results. The conflict must have a current grant-selecting disposition, the gate must pass, and readiness must be ready for this use. Before the stated commitment-seeking next move, the selected protocol must also be applicable under the rule for this intervention. Intervention remains blocked until the separately required commitment and all other entry conditions obtain.
```

The note identifies the publication prerequisite; the protocol-selection rule and its case facts remain to be recovered. Keep that applicability question separate and add its prerequisite to the account when recovered. The present result remains source finding. Once all prerequisites for the next move are satisfied, follow the readiness result's stated commitment-seeking action; the commitment has its own rule and instituting basis.

**Named-but-revoked grant near-miss.** Suppose `B17-InterventionGrant` and its complete-looking record are present, but policy-valid `B17-GrantRevocation` took effect before the intervention window. The `B17-GRANT` entry then fails `RequiredPostureOrCurrentness` because the grant no longer obtains. A current protocol, plan, `GateDecisionResult` with `decisionValue=pass`, readiness result, and green tile do not repair that failure: `AllowedUseNow` remains source-finding and prerequisite repair, and the intervention stays blocked.

### A.15.4:4.1 - Bias-Annotation

A.15.4 corrects appearance-based reliance. A publication face, dashboard tile, credential view, generated explanation, copied approval, provenance mark, schema wording, or API response can look ready for work before the required relation or result and its project-side FPF reference are named. The repair keeps the reliance appearance separate from the source relation or other relation that supports the claim.

It also corrects over-repair bias. Retain a sufficient ordinary result, choose rows when they help comparison or inspection, and persist the analysis as a reusable claim only when a later use needs it.

### A.15.4:4 - Conformance Checklist

| ID | Requirement (Normative Predicate) | Purpose and Rationale |
| :--- | :--- | :--- |
| **CC-A15.4-1 (One attempted use; proportionate prerequisite account)** | Before an appearance guides work or reliance, a conforming use names one exact attempted use and every independently required object. A sufficient ordinary note or accessible source account may carry these prerequisites. Keep their subject predicate and test, participants, required posture/currentness and dependency on the attempted use recoverable, with the kind and native project-side reference detail required by the governing rule or receiving use. If `RequiredPositionEntries` is selected, keep its five named fields matched to each direct object; use one row per object and retain native reference types rather than coercing them into a generic `U.EntityRef` list. If a prerequisite is absent or fails its posture, `AllowedUseNow` stays at the safe narrowed use. | Keeps the ordinary path light and every prerequisite under the rule or test that defines it. |
| **CC-A15.4-2 (P2W publication use boundary)** | A principle scheme, functional diagram, scenario, screen, or explanation that exposes a P2W chain guides only the `A.15` work or planning kind selected by the project use: method-family selection, selected method, `U.WorkPlan`, dated `U.Work`, work-result record, or result measurement. Claims outside that selected use require their own relation or result and source relation named by value. | Keeps P2W publication use tied to the work use under repair instead of turning publication form into project authority. |
| **CC-A15.4-3 (Lowering and refresh)** | When a required relation or result, its `SubjectPatternLocator`, source-currentness relation, revocation relation, affected Work target, relying context, or time window cannot be recovered, the disposition is orientation, source-finding, contested use, bounded reversible probe, repair request, or blocked unsupported claim. The note states the return or refresh condition for the first failed prerequisite; independently required currentness, decision, evidence, state, copied-source, generated-source, and publication objects remain separately recoverable in the selected form. | Preserves a supported narrower use while the required prerequisite is recovered. |
| **CC-A15.4-4 (Exact reopening judgment)** | Before allowing the attempted use, establish each consumed prerequisite under its own criterion and applicability, currentness and evidence rules. Recheck changed or failed premises and their dependents; retain unchanged applicable results. Keep permission/norm conflict separate from grant currentness: an unresolved or norm-selecting result blocks the affected use. A separately required gate and readiness result must satisfy their direct rules; neither substitutes for permission or a required commitment. | Prevents named records and green displays from replacing the current basis of the attempted use. |
| **CC-A15.4-5 (Register source and effect)** | For register-backed reliance, distinguish the entry episteme, publication, authoritative-source rule and the direct relation or finding. Recover entry-producing, exercised or evaluation Work only when the rule or occurrence claim consumes it; each asserted Work needs A.13 and independent A.15.1 admission. Add F.6 only for assignment-bound attribution. A failed F.6 test alone leaves independent Work admission intact; recheck any admission premise also affected by that finding. Use the entry only for claims supported under its rule and evidence/currentness basis. | Preserves rule-governed register authority while rejecting inference from entry presence alone. |

### A.15.4:5 - Common Anti-Patterns and How to Avoid Them

- **Appearance as source relation.** A dashboard tile, credential display, copied approval, generated explanation, provenance label, command-like cue, or composed source-relation chain is used as if presentation itself carried the work-relevant source relation. First name the work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair, then recover the required relation or result, its `SubjectPatternLocator`, and project-side reference. If that value is missing, lower only the unsupported reliance.

### A.15.4:6 - Consequences

| Consequence | Trade-off and cost | Mitigation |
| --- | --- | --- |
| Work can continue at the lightest use supported by a recovered relation instead of stopping on every suspicious display. | The practitioner names the claim being made and the required relation or project reference before relying on the appearance. | Retain a sufficient ordinary result; use rows when they help comparison or inspection. |
| Appearance-based approval, evidence, assurance, gate, and work-occurrence overreads are blocked. | Some convenient dashboard or copied-text shortcuts become unusable until source-currentness relation is recovered. | Keep orientation, source-finding, and bounded reversible probes available when no external-impact reliance is being made. |
| Repeated ambiguity becomes prerequisite-rule or source-relation repair work rather than repeated manual heroics. | The repair may reveal missing register entries, stale selected source epistemes, non-current or unresolved `EpistemePublicationRelation` occurrence refs, or underspecified gate and evidence relations. | Assign only prospective repair work or source-relation gap work; do not backdate evidence, gate passage, work occurrence, or assurance. |

### A.15.4:7 - Rationale

Practitioners often encounter a claim through a display, generated explanation, copy or credential view before its basis is recoverable. A.15.4 connects that encountered expression to the predicate and evidence required for the attempted use. The practitioner can retain a useful source-finding continuation while withholding an unsupported stronger claim.

Once the required §3 relation or result is recovered, apply its own predicate and test. Resolve a defining or constraining `ClaimGraph` only when rule identity or edition changes this use; an ordinary PatternID is otherwise enough.

### A.15.4:8 - SoTA-Echoing



| Claim need | Source contribution | Named source | FPF application | Shortcut rejected |
| --- | --- | --- | --- | --- |
| Dynamic authorization or policy-response displays need the requested operation and the policy conditions relevant to this use. | NIST SP 800-207 recommends resource access per session under dynamic policy. Cedar 4.5 evaluates a principal–action–resource–context request against policies and entity data. OpenFGA checks a user's modeled relation to an object using an authorization model and relationship tuples, with conditions and request context where applicable. | [NIST SP 800-207 Zero Trust Architecture](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf); [Cedar Policy Language Reference Guide v4.5](https://github.com/cedar-policy/cedar-docs/blob/ad5f61e979dbdb124c664ac9890da246a10aa0cf/docs/collections/_auth/authorization.md); [OpenFGA authorization concepts](https://openfga.dev/docs/concepts). | Name the attempted work or reliance use and the policy inputs it consumes, including the affected resource or work target, situation, policy edition and qualification window when material. Recover the direct permission or authority result required by that use. | Apply the actual policy, currentness and bounded-use conditions; reject treating policy-looking output as permission or authority by display alone. |
| Register-backed credential status or system-role-assignment state needs source and effect separation. | Verifiable Credentials Data Model 2.0 distinguishes issuer claims, holder presentations, credential verification and purpose-specific validation. Its `credentialStatus` property provides information for checking status under a selected scheme. Bitstring Status List v1.0 specifies how to retrieve and verify the referenced status-list credential and read the relevant status entry. | [W3C Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/); [Bitstring Status List v1.0](https://www.w3.org/TR/vc-bitstring-status-list/) as one status scheme. | Treat the entry as authoritative source only under the named rule for its exact effect; test the direct relation or finding and the evidence and currentness claims separately. | Use the register under its named authority and status rule; verify issuer/holder binding, current status and the particular claim the intended use consumes. |
| Provenance and attestation marks need a checked link to the underlying assertions and a defined scope for using those assertions as evidence. | C2PA 2.4 binds provenance assertions to assets through signed claims and defines validation of their bindings and signatures. SLSA v1.2 build provenance describes a build's inputs, builder and execution; verification checks the artifact and provenance against trusted identities and expected values. in-toto Statement v1 binds a typed predicate to artifact subjects identified by digest. | [C2PA Specifications 2.4](https://spec.c2pa.org/specifications/specifications/2.4/specs/C2PA_Specification.html); [SLSA v1.2 build provenance](https://slsa.dev/spec/v1.2/build-provenance) and [artifact verification](https://slsa.dev/spec/v1.2/verifying-artifacts); [in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md). | Follow the mark to the independently established provenance or process-trace relation. Use A.10 for bounded reliance on it and the direct subject pattern for any further truth, release, permission, gate or Work claim. | Use validated provenance as evidence within its supported scope; reject inferring truth, release authorization, deontic permission, gate passage, assurance or work occurrence from a mark alone. |
| Change, gate, release, and approval displays need decision, schedule, and performed-work separation. | ISO/IEC/IEEE 15288:2023 describes system life-cycle processes; the historical ISO/IEC/IEEE 12207:2017 describes software life-cycle processes, activities and tasks. ITIL 4 Change Enablement addresses change-risk assessment, authorization and scheduling. ITIL 4 Release Management addresses making new or changed services available under organizational policies and agreements with service consumers. | [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html) and the historical [ISO/IEC/IEEE 12207:2017](https://www.iso.org/standard/63712.html) life-cycle process frameworks; the latter was superseded by [12207:2026](https://www.iso.org/standard/90219.html). [ITIL 4 Change Enablement](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-4-practitioner-change-enablement-3794) and [Release Management](https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/ITIL-1/itil-4-practitioner-release-management-3798). | An approval-looking display supports reliance only when it exposes the exact §3 branch object, `GateDecisionResult`, `U.WorkPlan`, or dated `A.15.1` Work occurrence required by the attempted use, plus the evidence/currentness relation needed for reliance. | Adopt decision, permission/authority, schedule, and performed-work separation; reject a green tile, copied approval, or generated explanation as any of those by appearance. |

**Source scope and FPF application.** The FPF applications and rejected shortcuts above are this pattern's adaptation of the cited contributions. Use §3 to identify the relation or result required for the intended reliance, then inspect the relevant content and case facts under its authority, evidence and currentness conditions. Verified provenance may support a Work claim within its recorded scope; a visible mark alone is insufficient.



### A.15.4:9 - Relations

* **Cluster relation:** `A.15.4` is a cluster member under `A.15` for work-relevant appearance-based reliance repair; it does not replace the A.15 system-role-kind, assignment, Method, plan, and Work kernel.
* **Uses:** `E.17`, `E.17:5.1b`, `E.17:5.1c`, and `E.17:5.1d` for source-relation and use-boundary vocabulary; `E.17.EFP` for explanation faithfulness and source-finding; `A.16.0` when source lineage, branches, retirement, loss or a responsibility handoff needs reviewable history; `A.6`, `A.6.B`, and `A.6.C` for boundary wording; `A.10` for evidence and currentness; `B.3` for assurance; `A.15.5` for work-entry readiness; `A.20` for constraint validity; `A.21` for gate decisions; `A.2.1` for exact system-role assignments; `A.2.5` for assignment-state relations; A.13 for actual performers' core agency bases; A.15.1 for independently admitted dated Work; F.6 only when the receiving result must also identify the assignment under which that Work was performed; and `A.2.8`, `A.2.8.PER`, and `A.2.9` only through the single permission and authority branch in §3.
* **E.10 and E.10.MOVE relation-selection rule:** When the direct question is already known, apply its subject pattern directly or use the §3 lookup. Use `E.10.MOVE` when work-entry or readiness wording still hides the governed claim. Use `E.10.ARCH` when the distinction among a world-side fact, reusable declaration, claim or report, and representation remains unresolved. Permission or authority uses the single §3 branch. `A.15.4` starts only while a required relation or result is still hidden by the reliance appearance.
* **A.15 boundary relation:** use `A.15` directly when the remaining question under repair is system-role-kind, assignment, Method, plan, and Work alignment rather than a reliance appearance being used as a reason for Work or reliance.

#### A.15.4:9.1 - C.29 mathematical-lens use relation

> Use C.29 when choosing or transferring a mathematical representation could answer the reliance question or expose a limit on the proposed inference. Select the mathematical object and its correspondence to the situation, identify preserved and omitted distinctions and assumptions, and derive the consequence for the prerequisite test. State what would defeat that use. An adequate local calculation needs no additional lens account. For a Method, MethodDescription, plan or performed Work claim, use A.3.1, A.3.2, A.15.2 or A.15.1 respectively; A.15 explains their alignment.

#### A.15.4:9.2 - P2W Result-Related Source Boundary

When a P2W use under `E.18.1` produces result wording, use this pattern only when a reliance appearance such as publication, dashboard, generated explanation, copied statement, provenance mark, schema wording, API wording, or composed source-relation chain is about to justify result-related work or reliance by appearance.

Recover the required relation or result and its project-side reference before relying on any result-related cue: result artifact, resource ledger, launch-values-bound record, substitution record, telemetry, acceptance record, quality-evaluation record, done-state update, feedback pin, result measurement, evidence relation, assurance claim, parity relation, refresh relation, or system-role-assignment enactability claim. If the applicable rule, relation, or result is missing, use the reliance appearance only for orientation or source-finding and block only the unsupported result-related work or reliance.

#### A.15.4:9.3 - Lowering, Repair, and Refresh Conditions

Lower an `A.15.4` use when the attempted Work or reliance claim, required relation or result, relying context or window, or one required evidence, gate, assurance, system-role assignment, assignment state, Work, publication, boundary, permission, or authority object selected in §3 cannot be recovered. The lowered use is orientation, source-finding, contested use, bounded reversible probe, repair request, or blocked unsupported claim.

Repair the local note or persisted claim when its appearance, source currentness, revocation, source order, dashboard or credential publication, copied or generated source relation, boundary wording, or work-result cue changes. Repair the recovered value through the applicable evidence, assurance, gate, constraint, system-role-assignment, assignment-state, Work, publication, boundary, permission, or authority pattern named in §3; A.15.4 does not replace the repair defined there.

Before a consequential reliance use, confirm that the needed grounds remain applicable and sufficiently current. Reopen a changed, missing or expired prerequisite and every dependent use affected by it; retain unchanged applicable results. Apply the direct pattern to repair the failed premise, then reconsider the narrow disposition under A.15.4.


### A.15.4:End
