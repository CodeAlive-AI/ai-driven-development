## A.15.4 - Work-Relevant Appearance-Based Reliance Repair

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** Use `A.15.4` when a dashboard tile, credential view, copied approval, generated explanation, publication face, API response, source pointer, or weak indication is about to justify work or reliance, but the prerequisite for that use is unclear. Ask three questions: **What am I about to do or rely on? Which exact fact, relation, decision, or result would warrant that use? Can I open it and confirm that it covers this case and time now?** Keep the appearance at the lightest safe use until that prerequisite can be checked.

**Use this when.** Use this pattern only while appearance hides the direct object and test needed for one attempted use. If the direct question and the pattern that defines or tests it are already known, apply that pattern directly.

**First output.** Start with one ordinary sentence:

> This green tile points to `GateDecision-42`, but its link is stale. Use the tile only to find the current decision; do not deploy `Release-42` until that decision says `pass` for this release, target, scope, and window.

That sentence is a complete first result for this one-prerequisite use: it names the attempted use, the appearance, the missing prerequisite, the safe use now, the overread to block, and the observation that permits return. It is not a relation, record kind, U-kind, assignment, or project authority and needs no independent identity. If the prerequisite is recovered immediately, omit the note and use the direct relation or result.

When a short worksheet is useful, unpack the same result without adding ontology:

```text
Attempted use:
Appearance:
Missing prerequisite:
Safe use now:
Blocked overread:
Return when:
```

Use structured `RequiredPositionEntries` only when the attempted use has several independent prerequisites, when release, safety, compliance, external impact, or irreversibility makes the distinctions load-bearing, or when another person or system must inspect the result later. Then add one row per direct object:

```text
RequiredPositionEntries:
  - SubjectPatternLocator:
    DirectObjectKind:
    ProjectSideObjectRef:
    RequiredPostureOrCurrentness:
    DependencyOnAttemptedUse:
```

These are rows in the local note, not relation participants or a new prerequisite ontology. If the analysis itself must persist as a reusable claim, publish one bounded C.2.1 episteme whose exact EntityOfConcern is the subject of the attempted use and whose ClaimGraph contains the needed rows and disposition. Split it when the claims have different entities of concern.

**First repair use in practice.** State what the appearance may safely do now: orient attention, help find the required relation or result, preserve an early cue through `A.16.1`, support planning only through a `U.WorkPlan`, permit a bounded reversible probe, or block only the unsupported use.

**What goes wrong if missed.** The appearance starts acting as if it already proves approval, gate passage, evidence, assurance, performed Work, currentness, or release authorization. Work then proceeds or stops while the relation or result that must support the claim is missing, stale, revoked, or contradicted.

**Subject of the repair in plain terms.** The pattern handles one attempted-use question. It does not introduce a local repair relation. The appearance, attempted use, direct prerequisites, safe current use, and blocked overread retain the kinds and relations supplied by their own patterns.

**First repair checks.**
1. Name the appearance by its actual kind without treating it as the required relation or result.
2. Name the exact attempted use and the subject that use concerns.
3. Name the first direct prerequisite and the pattern that defines or tests it. For an ordinary one-prerequisite case, stop with the plain note.
4. Add typed rows only under the structured-use conditions above. Keep each independently required claim, instituted effect, relation occurrence, result, decision, assignment, evidence relation, currentness relation, or plan in its own row.
5. Before allowing the attempted use, check that every required relation obtains or every result passes its defined criterion, is current, covers the actual beneficiary, action, target, scope, and window, and has any evidence-use, source-currentness, or other source relation required by this reliance.
6. A relevant permission or norm conflict, gate decision, or work-entry-readiness result remains a separate prerequisite. An unresolved conflict blocks only the affected use and does not make an independently obtaining grant cease.

**Not this pattern when.** Stay in A.15 when the question is only separation among the acting System, local system-role kind, classification judgment, direct `U.SystemRoleAssignment` species, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`. Stay in `A.15.2` for WorkPlan construction, `A.15.3` for declaration-local planned-filling content, and `A.15.5` for full-kit condition or work-entry readiness. Stay in `A.16.1` and `C.2.4` for pre-articulation cue preservation, `C.16.Q` for a dynamic-quality claim, `A.6.A` for an action invitation, and E.17 for publication-face exposure. When the direct evidence, gate, constraint, boundary, permission, authority, Work, or other claim is already known, use the pattern and test selected by the §3 lookup instead of A.15.4.

**What this buys.** The acting engineer-manager can keep work moving without trusting appearances: use the reliance appearance for orientation or source-finding when that is all it can carry, proceed only inside the recovered relation when that relation exists, and turn repeated ambiguity into source-relation repair work rather than repeated manual reconstruction.

### A.15.4:1 - Problem Frame

Dashboards, credential views, generated explanations, copied approvals, provenance labels, green tiles, schema wording, API wording, and composed source-relation chains often look ready for work or reliance before the record or relation that carries the claim is visible. The practical problem is to decide what an engineer-manager may do now without turning appearance into approval or permission, gate passage, evidence, assurance, performed Work, system-role-assignment currentness, assignment-state or credential-status currentness, responsibility, authority, or release authorization.

**Plain recognition line.** Let the dashboard tile, credential view, copied approval, generated explanation, publication face, API response, or pointer lead to the required relation or result and the check it must pass. Do not let the reliance appearance become the relation, slot filler, or project-side reference that authorizes work or reliance.

**Reliance-appearance and claim/effect-position discipline.** In this pattern, `source` is not a generic kind. The value required for the attempted use is an actual relation occurrence, decision/finding/status result, plan, Work occurrence, or claim about that object. Apply the criterion defined for that value. A project record may be a `U.Episteme` that names it, and a publication relation may expose that record; neither the record nor its display makes the relation obtain or the result pass. If no typed reference and applicable test can be recovered, keep the appearance at orientation, source-finding, cue-pack preservation, repair request, or bounded-probe use.

**How to read the optional note and typed rows.** `A.15.4` does not introduce `U.Source`, `U.RequiredValue`, `WorkReliancePremise`, a generic cue head, a generic visible-thing kind, or a repair relation. The following labels are worksheet prompts for values defined elsewhere:
- `RelianceAppearanceRef` names the dashboard tile, credential view, copied wording, generated explanation, publication face, carrier, display, API wording, source-finding pointer, or low-articulation indication whose appearance is tempting the work or reliance use. `RelianceAppearanceKind` states its actual kind rather than making these items one kind. If the live value is a preserve-worthy early cue, use `U.PreArticulationCuePack` under `A.16.1`.
- `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef` name the use being justified: intended work, reliance on a claim, reliance on performed work, a work-relevant P2W claim, or a P2W chain position. These fields select the current branch; they do not create a durable kind.
- `RequiredPositionEntries` is the sole prerequisite set and contains one row per independently required direct object. Every row states `SubjectPatternLocator`, `DirectObjectKind`, the native `ProjectSideObjectRef` required for that object, `RequiredPostureOrCurrentness`, and `DependencyOnAttemptedUse`. The locator points to the pattern whose content defines, constrains, or tests the direct object; a proxy or navigation pattern is insufficient. One row may point to a required claim, another to an instituting speech act, grant, conflict finding, gate decision, assignment, evidence/currentness relation, plan, or other direct object; the row set creates none of them and never turns a claim into an instituted effect.
- `AllowedUseNow` states what use remains admissible after repair, such as orientation, source-finding, bounded reversible probe, narrowed reliance, or proceed-inside-recovered-relation.
- `AppearanceOverreadBlocked` names the false use that the reliance appearance would create by appearance, for example treating a dashboard color as gate passage or a copied approval as a current speech act.
- `RecoveryOrStopCondition` names the first failed prerequisite and what must change. Before reopening, follow every typed ref and verify that the relation obtains or the result passes its defined criterion, is current, covers the attempted beneficiary/action/target/scope/window, and has the evidence or source relation required for this reliance. When a relevant conflict exists, its separate `PermissionNormConflictFinding@Context` row must carry the current disposition defined in `A.2.8.PER`; an `unresolved` or norm-selecting result blocks the affected use without changing grant currentness. A named or complete-looking record is not enough.

Here `evidence relation`, `attestation relation`, and `currentness relation` mean `A.10` evidence-provenance, attestation, or currentness relations named by value. They are not work-procedure elements and do not carry authorization by their wording.

### A.15.4:2 - Problem - Cluster Boundary

A.15 remains the kernel for separating an acting System, exact local system-role kind, classification judgment, direct `U.SystemRoleAssignment` species, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and dated `U.Work`. A.15.4 starts only when a reliance appearance begins to justify a work or reliance claim and the team still needs to recover the required relation or result, its project-side reference, and the rule or test that applies. If those are already known, use them directly; A.15.4 adds no enduring relation around them.

### A.15.4:2.1 - Forces

| Force | Tension |
| --- | --- |
| Work momentum vs. prerequisite recoverability | Teams need to keep work moving, but a reliance appearance can make the wrong claim look like work authorization while a required relation or result is still unnamed. |
| Cheap first note vs. high-impact reliance | Routine source-finding should stay light, while release, safety, compliance, exact system-role-assignment, credential-status, assignment-state, and gate cases need more fields. |
| Publication face vs. required value | The visible carrier may be useful for orientation, but the work or reliance claim belongs to the project-side FPF kind, relation or result, and reference named by value. |
| Neighboring claims vs. local repair | A.15.4 can recover a missing prerequisite for the attempted work or reliance use, but evidence, gate, assurance, boundary, work-occurrence, and the permission/authority object selected by the §3 branch use the patterns and tests that define them. |
| Repeated ambiguity vs. individual burden | Repeated ambiguity about a required claim, instituted effect, relation, result, or reference should become prerequisite-lookup or source-relation repair work, not repeated manual reconstruction by every acting practitioner. |

### A.15.4:3 - Solution - Work-Relevant Appearance-Based Reliance Repair

#### Core stress-case rule

**Ordinary local note.** Use the opening sentence or six-line note and stop after the first missing prerequisite. Do not build a full evidence, currentness, or provenance dossier for that case.

For several prerequisites, a high-impact use, audit, handoff, or later reliance, expand that note with `RequiredPositionEntries`, `AllowedUseNow`, `AppearanceOverreadBlocked`, and `RecoveryOrStopCondition`.

The reliance appearance may be a tile, credential view, approval-looking memo, generated explanation, copied review, provenance mark, API wording, functional-description publication, or composed source-relation chain. The A.15.4 check asks whether every direct object required by the attempted use resolves and meets the posture and currentness predicates defined for that object, not merely whether a project-side reference is named or the reliance appearance is impressive, fluent, easy to inspect, or visually salient.

**Conditional structured field set.** Use the fuller fields below only for several independent prerequisites, later handoff or audit, or release-, safety-, compliance-, gate-, or other high-impact reliance. Also use them when an exact prerequisite's own rule requires assignment identity, assignment state, credential status, assurance, currentness, revocation, or cross-context detail. Select the depth from the attempted use and those direct prerequisites. The fields are worksheet aids or C.2.1 ClaimGraph content when persisted, not a record kind.

| Field | Working question |
| --- | --- |
| acting or affected system | Which admitted System would perform the Work, rely on the appearance, or be affected by the claim? A system-role kind, system-role assignment, credential status, and assignment-state relation are not the acting system. |
| system-role-assignment claim | Which assignment occurrence is being claimed, and which `U.SystemRoleAssignment` species declares it? A context field ending in `...SystemRoleAssignmentRef` is typed by `U.RelationRef constrained to U.SystemRoleAssignment` and resolves the occurrence. Keep capability, authority, responsibility, and Work attribution in their own rows. |
| intended work or work target | Is the user planning intended work, relying on a dated `U.Work` occurrence or result, or making another reliance claim? Name that branch and its required relation or result before the reliance appearance guides it. |
| affected resource or claim | Which resource, claim, gate, credential, credential-status, system-role-assignment-state relation or assertion, evidence, approval, or source-finding pointer with an authority relation is supposedly affected? |
| context | Which bounded context, environment, project slice, API setting, connector setting, protocol setting, or relying situation makes the claim applicable? |
| policy or gate version | Which policy, gate profile, constraint version, method version, or register edition applies to the claim? |
| time window | During which window is the claim, effect, source relation, or recovered-use boundary claimed to hold? |
| currentness or revocation field | Is the source relation current, stale, revoked, superseded, expired, contradicted, or unknown? |
| issuer or required reference | Which issuer, project reference, register entry, source-currentness or credential-status record, speech act, gate decision, evidence relation, or work-occurrence record is required for the current use, and where is its criterion defined? |
| verifier or relying context | Who is checking or relying on the claim, and in which context? |
| evidence or attestation relation | Which `A.10` evidence, provenance, or attestation relation, if any, justifies the claim without itself becoming approval, gate passage, assurance, or work occurrence? |
| sourceRelationClass | Which `E.17:5.1b` source-relation class or claim-use class applies to the reliance appearance and required claim or use? |
| unsupported effect | Which requested work claim, reliance claim, required value, or downstream effect remains unsupported and needs narrowing, repair, reopening, probing, or blocking? |

Start with the A.15.4 first repair checks above when the reliance appearance is being used as a reason for intended work, reliance, or a work-relevant claim. If the direct question is already known, use the §3 lookup and test its exact predicate and subject assertion; permission or authority uses the single branch there. Use A.15.4 only when `SubjectPatternLocator` and the project-side reference must still be recovered before a system-role-assignment, method, plan, Work, work result, result measurement, or another work or reliance claim can proceed.

**When a reliance appearance seems to authorize work or reliance.** Use A.15.4 when a publication, display, credential view, wording, or explanation looks like permission, prohibition, readiness, or evidence for intended work or reliance. This is a recognition moment, not a new kind. The repair question remains: what does the user intend to do next, what relation or result would make that use admissible, and which project-side reference and test are required?

Here "authority-looking case" is only a recognition phrase for the encountered situation. The record, relation, slot filler, or project-side reference that authorizes, forbids, records, or supports the required relation is named by value under its FPF pattern. Use `E.17:5.1c` for the shared meanings of `orientation use`, `reliance use`, operative claim, unsupported downstream use, and `reopen trigger`; use `E.17:5.1d` when the primary question under repair belongs to another FPF rule or result.

The central behaviour is: name the work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair; name each required relation or result and its project-side reference; keep the selected `U.Episteme`, exact `EpistemePublicationRelation` occurrence when availability is material, publication form, MVPK face, publication carrier, rendering, and source-finding cue distinct; choose the minimum sufficient recovered use; and do not raise the claim beyond the recovered relation, source relation, or recovered use boundary. If a project record names a required relation or result, follow its typed ref and apply the criterion defined for it, including obtaining, result posture, currentness, scope, and evidence for this attempted use. Cite the exact defining or constraining `ClaimGraph` only when rule identity or edition changes the use or reliance; the record's statement does not make the relation obtain.

**Positive repaired disposition.** First name the attempted use and open each prerequisite through its typed ref. The appearance may guide that use beyond orientation only after every referenced relation actually obtains or result passes its defined criterion, is current, covers this beneficiary/action/target/scope/window, and has the evidence or source relation required for this reliance. When a relevant permission/norm conflict exists, its separate finding row must be current and settled for this use; an `unresolved` or norm-selecting disposition blocks the use without rewriting grant currentness. Then write what may happen next. The first failed row keeps only that unsupported work or reliance use blocked.

Reliance dispositions after prerequisite recovery:

| Work or reliance disposition | Use when | Minimum useful result |
| --- | --- | --- |
| Orientation or source-finding note | The reliance appearance is only a publication face, publication carrier, rendering, cue, retrieval cue, learning aid, or reversible local probe trigger. | Use the opening ordinary sentence or six-line note. Name the first missing direct object in plain language; add no `RequiredPositionEntries` row unless a structured-use condition applies. |
| Routine reliance note | The team needs ordinary bounded reliance without release, safety, compliance, delegated system-role-assignment claim, assignment-state claim, credential-status claim, contested source relation, or cross-context reuse. | For one prerequisite, use the opening ordinary result. If several prerequisites are independently required, add one typed row for each. Name the acting or affected System, target, situation, window, assignment occurrence, capability, authority, or responsibility only when this attempted use relies on that value; each stronger relation must obtain independently or return its exact missing governor. |
| High-impact reliance disposition | The attempted use is external-impact, irreversible, release-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, revoked, system-role-assignment-state-claim-bearing, credential-status-claim-bearing, generated-source-mediated, copied-source-mediated, provenance-mediated, contested, or cross-context; or one typed prerequisite row triggers high-impact conditions defined for that prerequisite. | Use the additional fields required by the attempted use and those exact `RequiredPositionEntries` rows. When permission or authority is current, choose exactly one row in the §3 branch rather than copying the whole catalogue here. |

For a structured use, add only the rows and fields that the attempted use actually needs:

| Field | Value |
| --- | --- |
| `RelianceAppearanceRef` | Name the appearance being relied on by value, such as the dashboard tile, credential view, copied text, generated explanation, publication face, publication carrier, rendering, or source-finding cue. |
| `RelianceAppearanceKind` | Name the encountered object or relation kind without granting authority by appearance: selected `U.Episteme`, exact `EpistemePublicationRelation` occurrence or reference, publication form, MVPK face, publication carrier, rendering, `PublicationUnit`, dashboard tile, credential view, generated wording, copied wording, or source-finding cue. |
| `WorkOrRelianceUseKind` and `WorkOrRelianceUseRef` | Name the use being justified by value: intended work, reliance on a claim, reliance on a dated `U.Work` occurrence, method-family selection, selected method, method of work, work plan, planned work, work result, result measurement, release reliance decision, non-work reliance claim, work-relevant P2W claim, or P2W chain position. A planned baseline remains claim content in one exact `U.WorkPlan`; performed work becomes `U.Work` only after it occurs and is identified under `A.15.1`; work-result measurement belongs with the evidence relation or result-measurement record that carries it. |
| `RequiredPositionEntries` | This is the sole prerequisite set. Add one row per independent direct object, whether it is a claim, instituted effect, relation occurrence, result with a pattern-defined criterion, gate decision, assignment, evidence/currentness relation, plan, or other prerequisite. Each row names its `SubjectPatternLocator`, exact `DirectObjectKind`, native typed `ProjectSideObjectRef`, `RequiredPostureOrCurrentness`, and `DependencyOnAttemptedUse`. The locator must identify the pattern whose content defines, constrains, or tests that direct object; never store several patterns, kinds, or refs as comma-separated prose, and never coerce the refs into one generic `U.EntityRef` list. |
| `AllowedUseNow` | State the safe current use. `proceed-inside-recovered-relation` is allowed only after every required entry passes its `RequiredPostureOrCurrentness` and exact-use match; otherwise retain orientation, source-finding, bounded probe, repair request, narrowed reliance, or blocked unsupported use. |
| `AppearanceOverreadBlocked` | State the overread being blocked, such as treating display color as gate passage, copied approval as a current speech act, a credential screenshot as permission, or a generated explanation as evidence. |
| `RecoveryOrStopCondition` | Write the first row that fails and the observation that would make it pass. Reopen only after following every typed ref and verifying that its relation obtains or its result passes the criterion defined for it, is current, covers the attempted use, and has any evidence-use, source-currentness, or other source relation required by this reliance. Include separately required current conflict-finding, gate, and work-entry-readiness rows; an unresolved conflict row blocks the affected use without changing grant currentness. |

**Borrowed episteme and publication discipline.** A.15.4 borrows the `C.2.1`, `E.17`, and `E.24.PUB` distinctions rather than minting a new generic `U.*` kind. The claim-bearing FPF kind here is `U.Episteme`. When availability of its selected edition matters, name the exact `EpistemePublicationRelation` occurrence or reference. Publication forms, MVPK faces, publication carriers, renderings, `PublicationUnit` instances, and source-finding cues are separate kinds or relation positions in the case; no publication-kind shortcut replaces them. A planned baseline remains one exact `U.WorkPlan` episteme; any A.15.3 planned-filling rows remain declaration-local ClaimGraph content inside it. Launch values and finalization values remain their own project records, decision logs remain gate or decision records, performed-work evidence remains evidence, and dated Work occurrences remain `A.15.1` matters.

When a required relation or result, its project-side reference, or its test is incomplete, choose one `A.15.4` disposition after naming the work or reliance use and the exact direct objects it requires in `RequiredPositionEntries`; pick the lightest disposition that preserves practical work and recoverability:

1. Use the reliance appearance only for orientation or source-finding.
2. Reopen the selected source `U.Episteme` for the current claim, the exact `EpistemePublicationRelation` occurrence when availability is the issue, the source-bearing relation, register entry, direct record, or direct relation; or refresh source-currentness, credential-status, system-role-assignment-state, context-state, or another currentness relation.
3. Narrow the acting or affected System, an exact context field ending in `...SystemRoleAssignmentRef` when assignment identity is current, requested operation or work class, affected work target, affected resource, affected claim, context, and effective window until the recovered record or relation really covers the recovered use. Check capability through A.2.2, Work attribution through F.6, and authority or responsibility through its separately admitted direct predicate or exact missing governor.
4. Run a bounded reversible probe under an explicit `U.WorkPlan` when no external-impact reliance is being made.
5. Separate finding or exposing the missing source from assigning its repair. For source finding, ask an identified issuer, maintainer, verifier, holder, publisher, source contact, or acting user to expose the source or record on the strength of the direct source, publication, register, communication, access, or contact fact already available; this request neither assigns Work nor implies responsibility. Assign prospective repair Work, or say who must repair, only when an applicable allocation, responsibility, commitment, permission, or authority relation selects the System. Without that stronger relation, return the exact A.6.RCD missing governor for the repair assignment while keeping the cheap information request available. Keep every additional missing gate, evidence, assignment, state, currentness, or boundary object in its own row.
6. Repair the `U.WorkPlan`, `U.MethodDescription`, dashboard label, source-relation link, or boundary wording that made the overread plausible.
7. Proceed only inside the recovered scope and window.
8. Block only the work claim or reliance claim that lacks the required relation.

#### Repair assignment rule

**Missing source exposure versus repair assignment.** If a required source or record is unavailable, first make the light request: ask an identified issuer, maintainer, verifier, holder, publisher, source contact, or acting user to expose or locate it using the available direct source, publication, register, communication, access, or contact fact. This request is source finding, not prospective Work allocation, and creates no duty, authority, or responsibility. If the current move instead assigns repair Work, decision Work, planning Work, or source-relation-gap Work, select the admitted System through an independently obtaining allocation, responsibility, commitment, permission, or authority relation. An exact system-role kind or assignment may be an applicability ground but supplies none of those stronger relations. Without one, record the exact A.6.RCD missing governor for the repair assignment while retaining the safe source-finding request and narrowed use.

**Reliance-appearance kind check.** First name the actual kind of the reliance appearance: episteme, publication occurrence, publication form, carrier, rendering, dashboard tile, credential view, generated/copied wording, or source-finding cue. If it exposes a typed ref, follow that ref to the required relation or result and apply the criterion defined in its `SubjectPatternLocator`. Resolve an exact defining or constraining `ClaimGraph` only when the rule identity or edition changes this use. If the appearance exposes only a face, carrier, wording, or record entry, use it for orientation/source-finding until the direct object and evidence/currentness relation are recovered.

**Source-relation guard.** Release urgency, delegated-claim urgency, compliance concern, color, salience, copied wording, or generated wording does not replace the source relation named by value. A dashboard tile may guide release only as a current view of the relevant `GateDecision` plus evidence relation, currentness relation, scope, and window.

#### Prerequisite lookup table

Patterns and checks by required direct-object kind:

- cue-only orientation: use only for attention, learning, source-finding, or a reversible local probe trigger; stay with `A.16`, `A.16.1`, or `A.6.A` when those claims are being made.

**Permission and authority branch — use only when that is the live claim.** Do not route from *approved*, *authorized*, *allowed*, *may*, or the look of a permit. Ask what is true now and choose one row.

| Plain question | Pattern and required object | What closes or blocks this branch |
| --- | --- | --- |
| Did an admitted system perform an approval, authorization, delegation, grant, or revocation communication under an assignment that covers the act? | `A.2.9`; one `SA : U.SpeechAct` occurrence. | Recover the speech-act occurrence, performer System, and—when F.6 attribution or policy requires it—the covering assignment occurrence and its declared `U.SystemRoleAssignment` species, plus context, time, act type, and evidence needed for reliance. The assignment does not supply authority. A `SpeechActRecord`, message, or carrier is not the act, and the act alone does not make an institutional effect obtain. |
| Does a policy-valid strong grant currently obtain for this beneficiary and action? | `A.2.8.PER`; one `GrantedPermissionRelation@Context` occurrence. | Match beneficiary, action specification, policy/context, scope/window, and instituting `SpeechActRef`. A valid revocation, supersession, or policy failure may prevent or end the grant. An unresolved same-case conflict can block this attempted use without making the grant cease to obtain; keep those results separate. This is the permission-side instituted effect. |
| Before action, did a current frame complete enough for this use contain no applicable prohibition? | `A.2.8.PER`; one `NonProhibitionFinding@Context`. | Name the frame, use, beneficiary/action, scope/window, and evaluation. A stale or incomplete frame returns `unresolved`, not permission. |
| Did dated Work actually exercise one obtaining grant? | `A.2.8.PER`; one `PermissionExerciseRelation@Context` occurrence. | The Work must match the grant's action and the actual performer must satisfy its beneficiary branch. No dated Work means no exercise; non-exercise is not violation. |
| After Work, did a current sufficiently complete frame find no applicable violation? | `A.2.8.PER`; one `NonViolationFinding@Context`. | Name the actual Work, evaluation Work, frame, scope/window, and result. Exercise or non-exercise alone settles nothing; a stale or incomplete frame returns `unresolved`. |
| Do an obtaining grant and a current norm reach incompatible conclusions for the same beneficiary/action and overlapping scope/window? | `A.2.8.PER`; one `PermissionNormConflictFinding@Context`. | Cite the applicable precedence rule or an authorized dated decision Work and current resolution result. Otherwise keep the conflict `unresolved` and block the affected use. |
| Is an actual system or separately governed party obliged, prohibited, or given a recommendation-as-duty? | `A.2.8`; one `U.Commitment`. | Name the actual duty bearer, direct predicate, modality, exact referents, scope and window, applicable constitutive policy and rule, and actual instituting basis. A system-role kind or assignment may satisfy a rule antecedent but is not the duty bearer or commitment. The utterance, record, and carrier are not the commitment. |

A gate or readiness result remains an additional `A.21` or `A.15.5` prerequisite; it creates none of these objects. If the issue is only wording, classify it through `A.6` or the single permission-word branch in `A.6.B`. If only a permit, badge, message, record, or tile is visible, stay at orientation or source finding until one row above passes its stated test.
- system-role-assignment reliance: use `A.2.1` and name the assignment occurrence and its declared species. Assignment-state reliance instead uses the A.2.5 `SystemRoleAssignmentStateRelation`; credential-status reliance uses the exact proof or status result under `A.10`; context-state reliance uses its applicable direct state pattern and record; and a state established by a gate decision keeps its separate A.21 `GateDecision`. Keep every required object in its own row.
- boundary, policy, API, schema, "allowed", "authorized", "approved", "recommended", or "guaranteed" wording: split the statement through `A.6` or `A.6.B`. When its live job is permission or authority, return to the branch above; the displayed word does not choose the object.
- gate decision or gate passage: cite `A.21` `OperationalGate(profile)`, `GateDecision`, `GateDecisionRationale`, `DecisionLogRef`, gate profile, gate version, check set, scope, window, and replay or freshness pins.
- Flow constraint-validity witness: cite `A.20` `ConstraintValidity` status, witness, `GateCheckRef.aspect = ConstraintValidity`, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim.
- release, deployment, repair, inspection, or rollback work occurrence: cite `A.15.1` dated `U.Work` occurrence and the `A.10` evidence or provenance relation when reliance on occurrence is needed.
- evidence, provenance, authenticity, currentness, copied-source, or generated-source relation: apply `A.10` and name the claim-bound evidence relation, currentness relation, and the use allowed or blocked by that relation.
- assurance, safety, compliance, trust, release confidence, or `R`, `F`, `G`, or `CL` increase: apply `B.3` and name the typed assurance claim plus its limitations and reopen condition. If the word `ready` names full-kit or work-entry readiness, use `A.15.5`; if it names a gate decision, use `A.21`.
- generated explanation: use `E.17.EFP` for explanation faithfulness or source-finding relation, then require `A.10` claim-bound source relation for every operative claim that will be relied on.
- ambiguous approval, permission, or authorization wording: use the permission and authority branch above and choose by the plain question it answers now, never by the displayed word.

Recovered prerequisites for A.15.4 closure:
| Pattern or relation used | Recovered output for this A.15.4 repair | A.15.4-local use |
| --- | --- | --- |
| `A.6` or `A.6.B` | Typed claim IDs (`L-*`, `A-*`, `D-*`, and `E-*`) plus the pattern that defines or constrains the current boundary claim or the current effect-bearing claim. | Use for wording, boundary, API, schema, or use-boundary recovery before intended work or reliance. |
| `A.10` | Claim-bound evidence relation, freshness field, currentness field, and the use allowed or blocked by that relation for the attempted claim. | Use for evidence, provenance, authenticity, credential-currentness, copied-source, or generated-source recovery. |
| `B.3` | Typed assurance claim, no-assurance-use disposition, or rejected or downgraded assurance claim. | Use only when the work or reliance claim under repair relies on a typed assurance claim. |
| `A.21` | `OperationalGate(profile)`, `GateDecision`, `DecisionLogRef`, gate profile, gate version, scope, window, and replay or freshness pins. | Use for gate-passage reliance in the named scope and window. |
| `A.20` | `ConstraintValidity` status, witness, `PathId` or `PathSliceId` when applicable, window, sentinel, and pins when those fields are needed for the claim. | Use for flow constraint-validity reliance. |
| Permission or authority is current | Use the single branch above and carry the native object named by the selected row with its own closing conditions. | Do not mint or cite a generic permission-result object. |
| `A.15.1` | Dated `U.Work` occurrence plus `A.10` evidence or provenance relation when relied on. | Use for reliance on performed work. |
| `E.17.EFP` | Explanation class, source-finding relation, and faithfulness relation over the selected source `U.Episteme`, with the exact `EpistemePublicationRelation` occurrence named separately when availability is material. | Use for generated-explanation faithfulness and source-finding before operative reliance. |

High-impact work or reliance - especially external-impact, irreversible, release-bearing, system-role-assignment-bearing, assignment-state-claim-bearing, credential-status-claim-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, contested, or assurance-bearing claim or effect - may guide work only for the acting or affected System, any exact `...SystemRoleAssignmentRef` whose assignment identity is current, the work or reliance claim under repair, work-relevant P2W claim under repair, P2W chain position under repair, affected work target or claim, audience, scope, environment, version, policy context, operational mode, and time window for which the required project-side source relation, evidence relation, gate decision, or assurance claim is recoverable. Capability, authority, responsibility, assignment, Work attribution, and permission remain separate prerequisite rows. Cue-only, source-finding, learning, and bounded reversible probes stay lightweight and do not require a full evidence, currentness, or provenance dossier.
Quick dispositions:

| Encountered case | First `A.15.4` disposition |
| --- | --- |
| Release dashboard tile exposing a source relation | If the tile is a current dashboard view of `A.21` `GateDecision` or `DecisionLogRef` plus release scope or work target, environment, scope, window, gate profile, gate version, and `A.10` evidence relation, it may carry gate-passage reliance for that release and environment. |
| Release dashboard tile without current gate or evidence relation | Use the tile only for display or source-finding until the current `A.21` `GateDecision` or `DecisionLogRef`, release scope or work target, environment or scope, time window, gate profile, gate version, and `A.10` evidence relation are recoverable. Open `B.3` only when an assurance claim is being made. |
| Copied review summary or copied approval | Treat it as copied wording and a currentness cue. If the intended use relies on permission or authority, use the single branch above and follow only the selected row. Gate passage still needs the `A.21` decision, performed work still needs the dated `A.15.1` occurrence, and reliance needs the applicable `A.10` evidence/currentness relation. |
| Delegation chain with forwarded approval | Each link names delegator, delegatee, delegated operation or work class, affected work target, affected resource, affected claim, scope, window, the delegation record or relation permitting delegation, subdelegation allowance if any, revocation relation, currentness relation, and evidence relation. A forwarded approval is not delegated authority by copy alone. |
| System-role-assignment, revocation, assignment-state, or credential-status display | Resolve an assignment claim to both its occurrence and declared `U.SystemRoleAssignment` species. Resolve the other claims to the assignment-state relation, state-changing speech act, context-state record, credential proof or credential-status result, or gate decision with freshness field, revocation relation, or revocation record; visual display cannot defeat a higher-priority revocation or supersession relation. |
| Conflicting source relations | Do not resolve by color, visual salience, copied wording, or apparent recency. Name source-relation order, the decision or rule establishing that order, freshness policy, and supersession rule; the work claim, reliance claim, or effect is contested until resolved, while source-finding and bounded reversible probes remain available. |
| Credential badge or register-backed credential-status view | Treat the display as a publication of a register-entry episteme. Before relying, recover separately: the register entry and its publication relation; the constitutive policy or rule; the admitted System and, if authorization depends on its assignment, the assignment occurrence and declared species; the matching Work for an exercise claim or the evaluation Work required for a finding; the relation or finding required by the selected §3 row; and the evidence, currentness, and revocation relations. Assignment does not supply authority or responsibility. The entry is authoritative source only under the named rule for the claim or effect covered by that rule. An institutional effect still needs the authorized Work that the rule makes constitutive; a finding still needs the evaluation defined for it. Inscription alone performs no Work, institutes no effect, and creates neither exercise nor non-violation. |
| Rollback command-like cue | Treat it as a cue, or use `A.6.A` when it is an action invitation, unless the command record, authorization, work occurrence, performed-work result, or gate decision is recoverable. |
| Generated explanation says "authorized" | Use the explanation only to find source publications, claim-bound source relations, or required relations and results. If permission or authority is the live claim, route through the single branch above. The explanation itself supplies none of that branch's objects and proves neither gate passage nor performed work. |
| Extracted source publication, rewrite, representation shift, explanation, then gate or release claim | Return to the selected source `U.Episteme` and, where the break concerns availability, its exact `EpistemePublicationRelation` occurrence, form, or carrier; otherwise return to the source-bearing relation, transform record, evidence relation, explanation relation, or required relation or result at the first lossy or non-commutative transformation operation. The gate claim or release claim waits for the required transform record, evidence relation, explanation relation, gate decision, or assurance claim. |
| Repeated green-tile failures without recoverable source relation | Treat recurrence as upstream source-relation repair work: expose decision refs, fix dashboard semantics, add claim-bound source relations and currentness, revise boundary wording, or add review cues so the acting user is not repeatedly forced to reconstruct missing source relation. |

### A.15.4:3.1 - Archetypal Grounding - Worked Dashboard And Approval Examples

Worked dashboard and approval slice:

A release dashboard shows a green approval-looking tile for `Release-2026.05.08-prod`. If the tile is a current view of the relevant `GateDecisionRef` plus evidence relation and currentness relation, it may carry bounded gate-passage reliance for that release scope and window. A claim that deployment happened still requires a dated `A.15.1` work occurrence plus the evidence or provenance relation needed for the relying context. If the gate reference is missing or stale, treat the tile as orientation and source-finding until the team can name the release-work claim under repair, release-work position under repair, `SubjectPatternLocator` for the claim or effect, and the required gate-decision, evidence, and currentness fields.

| Step | Required record or relation |
| --- | --- |
| Required project claim or effect kind | Release reliance, gate passage, compliance proof, assurance increase, evidence relation, or currentness relation. |
| Gate decision record | Cite the current `A.21` `GateDecision` or `DecisionLogRef`, gate profile, gate version, release scope or work target, scope, window, and replay or freshness pins. Without that record, the tile is not release authorization or gate passage. |
| Flow constraint-validity witness | Cite `A.20` `ConstraintValidity` status or witness only when the claim is about flow constraint validity, not about the gate decision itself. |
| Evidence and currentness relation | Use `A.10` for the dashboard query, publication-carrier integrity, evidence refs, time, window, freshness field, revocation relation or revocation record, verifier context, relying context, and rival explanation such as stale display or copied status. |
| Assurance claim | Use `B.3` only if the tile is being used to raise readiness, compliance, trust, safety, release confidence, `R`, `F`, `G`, or `CL`; otherwise no assurance tuple is being claimed. |
| Repaired gate-use reliance | With the decision and evidence relation recovered, rely on gate passage only for the named release scope or work target, environment, gate profile, gate version, time, and window; a claim that deployment happened still needs a dated `A.15.1` work occurrence plus the evidence or provenance relation needed for the relying context. |
| Blocked overreads | The dashboard color does not create approval, deontic permission, compliance proof, rollback success, work occurrence, or assurance by display. |

Approval memo green-tile case:

An approval memo may carry an approval claim when it exposes the `A.2.9` `SpeechActRef`, acting System, any exact `actingSystemRoleAssignmentRef : U.RelationRef constrained to U.SystemRoleAssignment` required for F.6 attribution or policy applicability, affected release scope or work target, judgement context, time, window, publication-carrier refs, evidence refs, and instituted effect being claimed. Authority remains a separate direct relation and is never supplied by the assignment. That supports only the bounded approval use defined in `A.2.9`. It does not prove that release, deployment, rollback, or other Work occurred; that performed-Work claim still needs the dated `A.15.1` Work occurrence plus any `A.10` evidence relation required for the relying context.

Credential-status and system-role-assignment-state green-tile case:

A credential, credential-status, or system-role-assignment-state response is a publication of a claim-bearing register entry, not the status, `SystemRoleAssignmentStateRelation`, or assertion itself. It may serve as authoritative source only when the named register rule identifies the exact entry, issuer, holder-and-assignment binding, relying context, freshness and window, authorized entry-producing Work, and exact direct effect for which that Work is constitutive. Apply the criterion named by the selected §3 row to decide whether the relation obtains or the finding is warranted, and use `A.10` for the evidence and currentness claims. The response never supplies release, Work occurrence, gate passage, permission, authority, or evaluation result merely by being present.

Situation viewpoint prompts:

| Viewpoint or repair concern | Prompt |
| --- | --- |
| Acting practitioner | What can I safely do next without turning the encountered episteme or episteme publication into unsupported work or reliance justification? |
| Release engineer | Which `A.21` gate decision, decision log, release scope, work target, and `A.15.1` work occurrence are separate here? |
| Source, gate, evidence, or assignment-record contact | Which source-currentness value, assignment-state relation or assertion, credential-status value, decision ref, or evidence relation needs exposure? Which direct source, publication, register, communication, access, or contact fact supports that request? Only if repair Work is being assigned: which allocation, responsibility, commitment, permission, or authority relation selects its performer? |
| Audit or peer-review viewpoint | Which prerequisite, object, and test in the §3 lookup must be recoverable? If permission or authority is current, which one row in that branch answers the live question? |
| Boundary claimant | Which words need typed claim IDs before they can guide work or reliance? |
| Manager | Is repeated ambiguity prerequisite-lookup or source-relation repair work rather than another manual check for the acting practitioner? |
| LLM user or tool user | Which required relation, result, or source relation does the explanation help find, and which operative claims still need an `A.10` claim-bound source relation? |
| Security or compliance source contact | Which revocation relation, currentness relation, proof, credential-status record, system-role-assignment-state assertion, source-relation order, or supersession relation needs exposure, and which direct source, register, communication, access, or contact fact supports asking for it? If repair Work is assigned, which independent allocation, responsibility, commitment, permission, or authority relation selects the performer, or which exact missing governor blocks only that stronger move? |
| Model or data documentation steward | Which intended use, evaluation condition, version, window, limitation, and evidence relation bound the model or data documentation? |
| Assurance viewpoint | Which named claim actually has a `B.3` assurance claim, with what assurance tuple, evidence relation, limitations, and reopen condition? |

Search cues for A.15.4 include: approval, approval-looking display, authorization, authorization-looking display, permission, permission display, allowed wording, green dashboard, release tile, release readiness, model card, datasheet, data card, provenance, provenance mark, attestation, attestation label, credential, credential badge, generated explanation, copied review, copied approval, review summary, compliance-looking mark, delegation, delegation display, revocation, revocation status, gate passed, gate passage, rollback successful, rollback cue, and assurance label. These are retrieval cues only; decide the required relation or result, the pattern whose content defines or tests it, and the project-side reference from the work or reliance question under repair, not from the displayed word, publication-carrier name, or source name.

Work and reliance disposition table for authority-looking cases:

| Question under repair | Start in | First useful output |
| --- | --- | --- |
| Can this episteme publication, publication face, publication carrier, rendering, or cue guide work or reliance by appearance? | `A.15.4` | Work or reliance use, required claim/effect, project-side reference, and minimum use supported by the recovered relation. |
| Is the problem boundary, policy, API, schema, or connector wording? | `A.6` or `A.6.B` | Typed `L-*`, `A-*`, `D-*`, and `E-*` claims before the work claim or reliance claim is used. |
| Is the problem evidence, currentness, provenance, credential-status, generated-source relation, copied-source relation, or source-chain recovery? | `A.10` | Claim-bound evidence relation, currentness relation, and the use allowed or blocked by the recovered relation. |
| Is the problem assurance, readiness, safety, compliance, trust, release confidence, or change in `R`, `F`, `G`, or `CL`? | `B.3` | Typed assurance claim, no-assurance-use disposition, or downgraded or rejected assurance use. |

Display guidance for bounded credential status or system-role-assignment state: a visible state label meant to guide Work should expose source type, reference or link named by value, freshness, window, scope, unsupported Work claim, unsupported reliance claim, and unsupported effect. For example, prefer `Gate check passed; GateDecisionRef; release scope; environment; window; not compliance proof, rollback success, or assurance increase` over a bare approval-looking label.

Incident-learning fields for authority-looking overread: encountered selected episteme, publication occurrence, form, or carrier; work or reliance claim under repair; required relation or result, its `SubjectPatternLocator`, and project-side reference; acting or affected System; a context field ending in `...SystemRoleAssignmentRef` only when assignment identity matters to F.6 attribution or another direct relation that independently obtains; separate capability, authority, and responsibility rows when current; affected target, context, and window; missing or stale source, publication occurrence, source-bearing relation, register entry, or project-side reference; the direct source, publication, register, communication, access, or contact fact supporting a cheap exposure request; and, only for prospective repair Work, the selecting allocation, responsibility, commitment, permission, or authority relation or exact A.6.RCD missing governor; plausible overread; safe disposition; and smallest upstream repair.

Contestability and redress relation: when an authority-looking case affects assignment state, credential status, access, assignment, responsibility, release blockage, compliance claim, or safety-impacting Work, name the available challenge, review, redress, communication, source, publication, register, access, or contact relation before the work claim or reliance claim hardens. Recover the disputed source relation or claim, affected use or harm, allowed evidence or argument, possible disposition change, outcome route, and reopen trigger. Keep cheap source exposure available even when no one yet bears responsibility for future repair. Only a claim that a System must conduct later review or repair Work needs its own allocation, responsibility, commitment, permission, or authority relation; if that relation is absent, its exact missing governor blocks that stronger duty claim, not the challenge itself.

Lintable overread cues:

| Lint signal | Required relation or result named by value |
| --- | --- |
| `approved`, `authorized`, `allowed`, `recommended`, or `guaranteed` in boundary, API, schema, or policy wording | Split through `A.6` or `A.6.B`; when permission or authority is the live claim, use the single branch above instead of routing from the word. |
| Dashboard tile, credential-status color, system-role-assignment-state color, or release tile used as release evidence or gate passage | Require `A.21` `GateDecision` or `DecisionLogRef` plus `A.10` evidence and currentness relations. A displayed assignment-state label is neither `SystemRoleAssignmentStateRelation` nor its assertion. |
| Register screenshot, badge, or entry used as permission, authority, system-role-assignment, assignment-state, or gate evidence | Require five separate recoveries: register-entry episteme and its publication relation; constitutive rule; authorized entry-producing Work, actual exercised Work, or evaluation Work as the selected §3 row requires; direct relation or finding under that row; and `A.10` evidence and currentness. The entry may be authoritative source for the rule's exact claim or effect, but inscription creates neither actual exercise nor a non-violation finding. |
| Generated explanation uses `authorized`, `approved`, or similar wording | Use `E.17.EFP` for explanation/source-finding and `A.10` for the claim-bound source relation; if permission or authority is current, choose one row in the single branch above. |
| Model card, datasheet, label, or note cited as readiness, safety, compliance, or release confidence | Require a typed `B.3` assurance claim, intended-use match, evaluation condition, limitations, and `A.10` evidence relation. Use `A.15.5` instead when the current claim is full-kit or work-entry readiness. |
| Provenance or attestation label cited as truth, safety, release, permission, or authority | Require the bounded `A.10` provenance/process-trace claim plus the applicable pattern and test for the relied-on truth, safety, release, permission, or authority claim. For the last two, use the single branch above; the label is not its result. |
| Evidence, assurance, gate, or work-occurrence words without the relation or result that carries that claim or effect | Recover the `A.10` evidence relation, `B.3` assurance claim, `A.21` gate decision, or `A.15.1` work-occurrence record respectively before the work claim or reliance claim is used. |

Stress cases for practice:

| Case | Expected A.15.4 disposition |
| --- | --- |
| Green release dashboard tile with no `GateDecisionRef`. | Source-finding only; recover `A.21` decision or decision log plus `A.10` evidence before gate-passage reliance. |
| Copied approval from last month. | Treat the copy as a source-finding cue; use the permission/authority branch above to choose the one live question, then recover currentness and evidence for that selected object. |
| Credential badge screenshot after revocation. | Recover the register-entry episteme, its publication relation, named status rule, authorized entry-producing Work, direct status relation, and evidence/currentness/revocation relation separately. The revoked direct relation blocks reliance even when the entry remains visible. |
| Register entry says `grant exercised; no violation`, but no dated matching Work or evaluation Work is recoverable. | Keep both claims blocked. For exercise, recover dated Work and show that its action and performer satisfy the obtaining grant. For non-violation, recover the evaluation Work and current sufficiently complete frame. Inscription establishes neither result. |
| Generated explanation says `authorized by policy`. | Use `E.17.EFP` for explanation/source-finding and `A.10` for the claim-bound source relation; if permission or authority is current, choose and verify one row in the single branch above. |
| Boundary wording says `guaranteed approved for production`. | Split the sentence through `A.6` or `A.6.B`; use `A.6.C` for agreement-like or promise-bearing content and the single permission/authority branch above only for the permission or authority claim that remains. |
| Dashboard says green while decision log says blocked. | Treat as conflicting source relations; name source-relation order, the decision or rule establishing that order, freshness policy, and supersession rule before the work claim or reliance claim is used. |
| CRISPR lab dashboard says the guide edit is ready. | Treat the dashboard as orientation or source-finding until the protocol publication or protocol record, approval record or gate record, exact direct system-role-assignment occurrence when assignment identity matters, evidence relation, current lab context record, and `U.WorkPlan` for the intended edit are recoverable. Recover capability, authority, responsibility, permission, and Work attribution separately when current. If the question is full-kit or work-entry readiness for the intended edit, use `A.15.5`; the readiness tile still does not create biological-intervention authorization, deontic permission, safety, or performed Work. |

### A.15.4:3.2 - Archetypal Grounding - High-Impact Reliance-Repair Slice

A lab manager sees a green tile for `CRISPR-guide-G42 ready` and a copied message saying the edit is approved. `A.15.4` does not ask the manager to decide whether the tile is a good UI. It asks what work or reliance claim is about to be made.

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
      DependencyOnAttemptedUse: the intended Work must use the applicable protocol edition
    - EntryId: B17-GRANT-ACT
      SubjectPatternLocator: A.2.9
      DirectObjectKind: U.SpeechAct occurrence
      ProjectSideObjectRef: B17-GrantSpeechAct
      RequiredPostureOrCurrentness: actual dated Work performed by an admitted system under the exact grantor assignment and recognized by the current grant policy
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
      DirectObjectKind: claim-bound evidence-provenance relation
      ProjectSideObjectRef: B17-ConflictFindingEvidence
      RequiredPostureOrCurrentness: supports only the current B17-InterventionPermissionNormConflictFinding disposition and the applicability of B17-ConflictPrecedenceRule-e2 to this exact attempted use
      DependencyOnAttemptedUse: supplies the evidence/currentness path for B17-CONFLICT without becoming the finding, rule, or grant
    - EntryId: B17-GATE
      SubjectPatternLocator: A.21
      DirectObjectKind: GateDecision
      ProjectSideObjectRef: B17-InterventionGateDecision-e2
      RequiredPostureOrCurrentness: current GateDecision=pass under the applicable GateProfile and DecisionLog
      DependencyOnAttemptedUse: the current lab policy separately requires gate passage; this decision does not create the grant
    - EntryId: B17-WORK-ENTRY
      SubjectPatternLocator: A.15.5
      DirectObjectKind: WorkEntryReadiness@Context relation
      ProjectSideObjectRef: B17-WorkEntryReadiness-e3
      RequiredPostureOrCurrentness: current relation for the exact B17-GeneEditIntervention, performer, kit, context, and entry window, with CommitmentDisposition=readyForCommitment and no triggered StopCondition
      DependencyOnAttemptedUse: the current lab policy separately requires work-entry readiness; readiness does not create the grant or gate decision
    - EntryId: B17-ASSIGNMENT
      SubjectPatternLocator: A.2.1
      DirectObjectKind: B17EditorSystemRoleAssignment, a direct species of U.SystemRoleAssignment
      ProjectSideObjectRef: B17-EditorAssignment
      RequiredPostureOrCurrentness: obtains, names the intended performer as holder, and covers the proposed Work window
      DependencyOnAttemptedUse: identifies the intended performer and the assignment context required by the beneficiary branch and F.6 attribution; it establishes neither capability, permission, authority, responsibility, nor Work
    - EntryId: B17-PROTOCOL-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: claim-bound evidence-provenance relation
      ProjectSideObjectRef: B17-ProtocolPublicationEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-ProtocolPublication-e5 obtains and exposes protocol edition e5 for this lab audience and intervention use throughout the decision window
      DependencyOnAttemptedUse: supplies the publication/currentness evidence required for B17-PROTOCOL without standing in for that publication relation
    - EntryId: B17-GRANT-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: claim-bound evidence-provenance relation
      ProjectSideObjectRef: B17-InterventionGrantEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-InterventionGrant obtains and is current for this beneficiary, action, batch, scope, and window, including the instituting act, policy, revocation, and supersession sources used by that claim
      DependencyOnAttemptedUse: supplies the evidence/currentness path required for B17-GRANT without creating or replacing the grant
    - EntryId: B17-GATE-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: claim-bound evidence-provenance relation
      ProjectSideObjectRef: B17-InterventionGateEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-InterventionGateDecision-e2 is the current GateDecision=pass for this attempted use under its GateProfile and DecisionLog
      DependencyOnAttemptedUse: supplies the evidence/currentness path required for B17-GATE without becoming gate passage
    - EntryId: B17-ASSIGNMENT-EVIDENCE
      SubjectPatternLocator: A.10
      DirectObjectKind: claim-bound evidence-provenance relation
      ProjectSideObjectRef: B17-EditorAssignmentEvidence
      RequiredPostureOrCurrentness: supports only the claim that B17-EditorAssignment obtains, has the intended performer as holder, and covers the proposed Work window
      DependencyOnAttemptedUse: supplies the evidence/currentness path required for B17-ASSIGNMENT without creating or extending the assignment
    - EntryId: B17-PLAN
      SubjectPatternLocator: A.15.2
      DirectObjectKind: U.WorkPlan
      ProjectSideObjectRef: B17-GeneEditWorkPlan-e4
      RequiredPostureOrCurrentness: current plan for the intended performer, intervention, sample batch, method, resources, and window; not actual Work or permission
      DependencyOnAttemptedUse: describes the Work that would be entered if every other prerequisite passes
  AllowedUseNow: source-finding and prerequisite refresh only; do not intervene while any entry is absent or fails its required posture or currentness
  AppearanceOverreadBlocked: tile color and copied message do not authorize biological work or prove safety
  RecoveryOrStopCondition: before intervention, follow every typed ref; reopen only when every listed relation obtains or result passes its stated criterion, is current for this beneficiary, action, sample batch, scope, and window, and has its required evidence or source relation; B17-CONFLICT must have a current grant-selecting disposition, the gate must say pass, and work-entry readiness must say readyForCommitment
```

**Named-but-revoked grant near-miss.** Suppose `B17-InterventionGrant` and its complete-looking record are present, but policy-valid `B17-GrantRevocation` took effect before the intervention window. The `B17-GRANT` entry then fails `RequiredPostureOrCurrentness` because the grant no longer obtains. A current protocol, plan, `GateDecision=pass`, readiness result, and green tile do not repair that failure: `AllowedUseNow` remains source-finding and prerequisite repair, and the intervention stays blocked.

### A.15.4:4.1 - Bias-Annotation

A.15.4 corrects appearance-based reliance. A publication face, dashboard tile, credential view, generated explanation, copied approval, provenance mark, schema wording, or API response can look ready for work before the required relation or result and its project-side FPF reference are named. The repair keeps the reliance appearance separate from the source relation or other relation that supports the claim.

It also corrects over-repair bias. Follow the opening progressive path: stop with the ordinary result when one prerequisite is enough, and open structured rows or a durable episteme only under the stated structured-use conditions.

### A.15.4:4 - Conformance Checklist

| ID | Requirement (Normative Predicate) | Purpose and Rationale |
| :--- | :--- | :--- |
| **CC-A15.4-1 (One attempted use; proportionate prerequisite account)** | Before an appearance guides work or reliance, a conforming use names one exact attempted use and every independently required object. An ordinary one-prerequisite case may use the six-line plain note and stop. A structured case uses one `RequiredPositionEntries` row per direct object; every row supplies `SubjectPatternLocator`, the exact direct-object kind, native project-side ref, required posture and currentness, and dependency on the attempted use. It never stores comma-separated patterns, kinds, or refs or coerces them into a generic `U.EntityRef` list. If a required prerequisite is absent or fails its posture, `AllowedUseNow` stays at the safe narrowed use. | Keeps the ordinary path light and every structured prerequisite under the rule or test that defines it. |
| **CC-A15.4-2 (P2W publication use boundary)** | A principle scheme, functional diagram, scenario, screen, or explanation that exposes a P2W chain guides only the `A.15` work or planning kind selected by the project use: method-family selection, selected method, `U.WorkPlan`, dated `U.Work`, work-result record, or result measurement. Claims outside that selected use require their own relation or result and source relation named by value. | Keeps P2W publication use tied to the work use under repair instead of turning publication form into project authority. |
| **CC-A15.4-3 (Lowering and refresh)** | When a required relation or result, its `SubjectPatternLocator`, source-currentness relation, revocation relation, affected Work target, relying context, or time window cannot be recovered, the disposition is orientation, source-finding, contested use, bounded reversible probe, repair request, or blocked unsupported claim. The note states the return or refresh condition for the first failed prerequisite; a structured use keeps independently required currentness, decision, evidence, state, copied-source, generated-source, and publication objects in separate rows. | Keeps A.15.4 useful without admitting a repair relation or generic source kind. |
| **CC-A15.4-4 (Exact reopening judgment)** | Naming is only the first recovery step. Before `AllowedUseNow` permits the attempted use, follow every typed ref and verify that its relation obtains or its result says pass or ready under the criterion defined for it, is current, covers the beneficiary, action, target, scope, and window, and has any evidence-use, source-currentness, or other source relation required by this reliance. A relevant `PermissionNormConflictFinding@Context` has its own row and current `A.2.8.PER` disposition; an `unresolved` or norm-selecting result blocks the affected use but does not make a separately obtaining grant cease. Any separately required A.21 gate decision is current, and any separately required A.15.5 work-entry-readiness result says `ready` under its exact criterion and remains inside its reliance window. A named, recorded, but revoked or mismatched grant keeps the use blocked. | Prevents explicit records and green displays from substituting for current world-side or institutional conditions. |
| **CC-A15.4-5 (Register source is not the effect)** | A register-backed reliance keeps the register-entry episteme, its publication relation, constitutive rule, authorized entry-producing Work, actual exercised Work or evaluation Work when current, direct relation/finding, and evidence/currentness relation separate. The entry is authoritative source only for the exact claim or effect covered by the named rule. An institutional effect needs the authorized Work that the rule makes constitutive; exercise needs dated matching Work; a non-violation finding needs the evaluation defined for it. Inscription establishes none of them. | Prevents record-as-world and record-as-Work overread. |

### A.15.4:5 - Common Anti-Patterns and How to Avoid Them

- **Appearance as source relation.** A dashboard tile, credential display, copied approval, generated explanation, provenance label, command-like cue, or composed source-relation chain is used as if presentation itself carried the work-relevant source relation. First name the work or reliance claim under repair, work-relevant P2W claim under repair, or P2W chain position under repair, then recover the required relation or result, its `SubjectPatternLocator`, and project-side reference. If that value is missing, lower only the unsupported reliance.

### A.15.4:6 - Consequences

| Consequence | Trade-off and cost | Mitigation |
| --- | --- | --- |
| Work can continue at the lightest use supported by a recovered relation instead of stopping on every suspicious display. | The practitioner names the claim being made and the required relation or project reference before relying on the appearance. | Follow the opening progressive path; add structured rows only when its stated conditions apply. |
| Appearance-based approval, evidence, assurance, gate, and work-occurrence overreads are blocked. | Some convenient dashboard or copied-text shortcuts become unusable until source-currentness relation is recovered. | Keep orientation, source-finding, and bounded reversible probes available when no external-impact reliance is being made. |
| Repeated ambiguity becomes prerequisite-rule or source-relation repair work rather than repeated manual heroics. | The repair may reveal missing register entries, stale selected source epistemes, non-current or unresolved `EpistemePublicationRelation` occurrence refs, or underspecified gate and evidence relations. | Assign only prospective repair work or source-relation gap work; do not backdate evidence, gate passage, work occurrence, or assurance. |

### A.15.4:7 - Rationale

A.15.4 exists because Work often first meets a source expression, selected source `U.Episteme`, exact publication occurrence, source-bearing relation, or composed source-relation chain through a display, publication face, generated explanation, copied statement, credential view, dashboard tile, schema wording, or API wording before the required relation or result and project-side reference are visible. Using A.15.4 lets the practitioner keep Work moving with orientation or bounded source-finding while preventing that appearance from becoming approval, evidence, assurance, gate passage, performed Work, release authorization, system-role-assignment currentness, assignment-state currentness, responsibility, authority, or credential-status currentness by appearance.

The repair is deliberately local and creates no new authority relation. Once the exact evidence, gate, assurance, system-role assignment, assignment state, Work, publication, boundary, permission, or authority object selected in §3 is recovered, apply the predicate defined for it through `SubjectPatternLocator`. Resolve an exact defining or constraining `ClaimGraph` only when rule identity or edition changes this use; an ordinary PatternID is otherwise enough.

### A.15.4:8 - SoTA-Echoing

**SoTA alignment rule.** Interpret each row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and relations of this pattern.

| Claim need | Source idea and current named object | Current object or relation ref | Local FPF invariant and practical local test | Adopted invariant, adapted invariant, and rejected shortcut |
| --- | --- | --- | --- | --- |
| Dynamic authorization or policy-response displays need requested operation named by value, affected resource or work target, situation, and window. | Dynamic authorization practice separates subject, requested operation, affected resource or work target, situation, and window before a relying use is allowed. | NIST SP 800-207 Zero Trust Architecture; Cedar Policy Language Reference Guide v4.5; OpenFGA authorization-modeling docs; source maturity = current standards, specifications, and widely used technical practice. | The local note names the attempted work or reliance use, affected resource or work target, policy version, situation, and time window before treating a visible allow or deny response as a source for work or reliance. | **Adopt, adapt, reject.** Adopt bounded currentness, source-relation, and bounded-use invariants; adapt them through FPF project records named by value; reject treating policy-looking output as permission or work-relevant source relation by display. |
| Register-backed credential status or system-role-assignment state needs source and effect separation. | Current identity practice separates register entry, publication, issuer–holder binding, constitutive rule, authorized update or evaluation Work, direct status relation or finding, verifier and relying context, revocation, and freshness. | W3C Verifiable Credentials Data Model v2.0 Recommendation and current digital identity or register-backed status practice; source maturity = current specifications and technical practice. | Treat the entry as authoritative source only under the named rule for its exact effect; test the direct relation or finding and the evidence and currentness claims separately. | **Adopt, adapt, reject.** Adopt register authority and currentness checks; reject entry or display presence as the status, assignment-state relation, Work, exercise, non-violation, gate passage, permission, or authority itself. |
| Provenance and attestation marks need source relation and process-trace relation without becoming truth, release, or work evidence. | Provenance and attestation practice separates origin relation, process traceability relation, build claim, supply-chain claim, and verification metadata from truth of downstream claims, release authorization, or deontic permission. | C2PA Specifications 2.4 content provenance and attestations; SLSA v1.2 provenance; in-toto Statement v1 attestations; source maturity = current standards, specifications, and widely used practice. | A provenance or attestation mark remains source relation or process-trace relation until `A.10`, `B.3`, `A.20`, `A.21`, `A.15.1`, or another source relation named by value carries the downstream claim. | **Adopt, adapt, reject.** Adopt source traceability and process traceability; reject provenance-mark-as-truth, release authorization, deontic permission, gate passage, assurance, or work occurrence. |
| Change, gate, release, and approval displays need decision, schedule, and performed-work separation. | Release and change practice separates approval/authorization acts, permission and authority objects, gate decisions, planned schedules, and performed work. | ISO/IEC/IEEE 15288:2023 and ISO/IEC/IEEE 12207:2017 life-cycle process separation; ITIL 4 Change Enablement and current release and change practice; source maturity = current life-cycle standards plus mature service-management practice. | An approval-looking display supports reliance only when it exposes the exact §3 branch object, `GateDecision`, `U.WorkPlan`, or dated `A.15.1` Work occurrence required by the attempted use, plus the evidence/currentness relation needed for reliance. | **Adopt, adapt, reject.** Adopt decision, permission/authority, schedule, and performed-work separation; reject a green tile, copied approval, or generated explanation as any of those by appearance. |

**Digital-identity and provenance boundary.** The cited identity, provenance, policy, and change sources supply currentness, credential-status, system-role-assignment-state, provenance, and change-practice checks. They do not turn a credential, provenance label, attestation, policy response, register excerpt, or dashboard display into Work, gate passage, permission, authority, assurance, release, or another project relation. Use §3 to recover the exact relation or result and its applicable test before relying.

The nearest recovery references are the worked dashboard case, the permission and authority branch in §3, `CC-A15.4-1`, `CC-A15.4-2`, and the direct `A.10`, `B.3`, `A.21`, and `A.15.1` checks named in the prerequisite lookup. If a SoTA row cannot be recovered through those local checks, do not let its citation stand in for the local `A.15.4` rule.

### A.15.4:9 - Relations

* **Cluster relation:** `A.15.4` is a cluster member under `A.15` for work-relevant appearance-based reliance repair; it does not replace the A.15 system-role-kind, assignment, Method, plan, and Work kernel.
* **Uses:** `E.17`, `E.17:5.1b`, `E.17:5.1c`, and `E.17:5.1d` for source-relation and use-boundary vocabulary; `E.17.EFP` for explanation faithfulness and source-finding; `A.16.0` for source transfer; `A.6`, `A.6.B`, and `A.6.C` for boundary wording; `A.10` for evidence and currentness; `B.3` for assurance; `A.15.5` for work-entry readiness; `A.20` for constraint validity; `A.21` for gate decisions; `A.2.1` for exact system-role assignments; `A.2.5` for assignment-state relations; `A.15.1` and `F.6` for dated Work and its attribution; and `A.2.8`, `A.2.8.PER`, and `A.2.9` only through the single permission and authority branch in §3.
* **E.10 and E.10.MOVE relation-selection rule:** When source-relation, permission or authority, readiness, system-role-assignment or assignment-state, green-tile, generated or copied wording, provenance, dashboard, or move-like wording is being used as a reason for Work or reliance, `E.10.MOVE` first repairs hidden work-entry or readiness wording and `E.10.ARCH` assigns the direct evidence, assurance, readiness, gate, constraint, boundary, system-role-assignment, assignment-state, Work, publication, transfer, or explanation question. Permission or authority uses the single §3 branch. `A.15.4` starts only while a required relation or result is still hidden by the reliance appearance.
* **A.15 boundary relation:** use `A.15` directly when the remaining question under repair is system-role-kind, assignment, Method, plan, and Work alignment rather than a reliance appearance being used as a reason for Work or reliance.

### A.15.4:9.1 - C.29 mathematical-lens use relation

> If a mathematical lens appears in work-relevant appearance-based reliance repair, use `C.29` only to state why the lens helps expose or bound a reliance appearance such as generated wording, dashboard cue, copied phrase, publication form, MVPK face, publication carrier, rendering, `PublicationUnit`, or source-finding cue. Use `A.15.4` for the reliance appearance, required relation or result named by value, return or reopen condition, reliance relation, and whether that appearance can guide work under a recovered relation. Use `A.15` and `A.15.1` for method choice, plans, and performed work when those claims are being made; a `C.29` lens-use result does not turn a cue, rendering, or diagnostic phrase into source relation.

### A.15.4:9.2 - P2W Result-Related Source Boundary

When a P2W use under `E.18.1` produces result wording, use this pattern only when a reliance appearance such as publication, dashboard, generated explanation, copied statement, provenance mark, schema wording, API wording, or composed source-relation chain is about to justify result-related work or reliance by appearance. No generic `WorkResult` kind is admitted.

Recover the required relation or result and its project-side reference before relying on any result-related cue: result artifact, resource ledger, launch-values-bound record, substitution record, telemetry, acceptance record, quality-evaluation record, done-state update, feedback pin, result measurement, evidence relation, assurance claim, parity relation, refresh relation, or system-role-assignment enactability claim. If the applicable rule, relation, or result is missing, use the reliance appearance only for orientation or source-finding and block only the unsupported result-related work or reliance.

### A.15.4:9.3 - Lowering, Repair, and Refresh Conditions

Lower an `A.15.4` use when the attempted Work or reliance claim, required relation or result, relying context or window, or one required evidence, gate, assurance, system-role assignment, assignment state, Work, publication, boundary, permission, or authority object selected in §3 cannot be recovered. The lowered use is orientation, source-finding, contested use, bounded reversible probe, repair request, or blocked unsupported claim.

Repair the local note or persisted claim when its appearance, source currentness, revocation, source order, dashboard or credential publication, copied or generated source relation, boundary wording, or work-result cue changes. Repair the recovered value through the applicable evidence, assurance, gate, constraint, system-role-assignment, assignment-state, Work, publication, boundary, permission, or authority pattern named in §3; A.15.4 does not replace the repair defined there.

Refresh before allowing the reliance appearance to guide release, safety, compliance, a delegated system-role-assignment or assignment-state claim, contested source relation, cross-context reuse, work-result reliance, external-impact reliance, or irreversible Work. Stop at the smallest changed prerequisite or source relation: reliance appearance, selected source `U.Episteme` for the current claim, exact `EpistemePublicationRelation` occurrence when availability is material, publication form or carrier when either changed, required relation or result, source-currentness relation, system-role-assignment-state assertion or its evidence or currentness relation, credential-status record, context-state record, revocation record, gate relation, evidence relation, assurance relation, copied-source relation, generated-source relation, or Work relation.

### A.15.4:End

