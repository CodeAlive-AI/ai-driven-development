## A.15.4 - Work-Relevant Source Restoration

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**At a glance.** This A.15 cluster member tells an engineer-manager which exact project-side FPF kind and reference must be recovered before an encountered episteme, episteme publication, display, credential view, generated explanation, copied statement, provenance mark, dashboard tile, schema wording, API wording, or composed source chain may support a work claim or reliance claim.

**Use this when.** Use this pattern when a visible item is about to guide a work move, reliance move, or work-relevant P2W claim by appearance, and the acting user must recover the exact project-side FPF kind and reference before proceeding.

**First output.** One compact restoration note: encountered item; live work claim, reliance claim, or P2W load or position; governing FPF pattern; exact project-side FPF kind and reference needed; admissible next project move now; and blocked overread.

**What goes wrong if missed.** Teams treat a visible dashboard, credential view, copied approval, generated explanation, provenance mark, schema wording, API wording, publication, display, or cue as if it already carried approval, permission, gate passage, evidence, engineering justification, performed work, release permission, role support, or status support. Work then proceeds or stops on appearance while the governing FPF pattern and exact project-side FPF kind and reference that actually carry the claim or effect are missing, stale, revoked, or contradicted.

**Governed object in plain terms.** One source-restoration relation for one live work claim, reliance claim, or P2W load or position: encountered item, live claim or effect, governing FPF pattern, exact project-side FPF kind and reference needed, admissible next project move now, and blocked overread. It is not a new `authoritySourceRef` target, evidence source, gate record, engineering justification object, work occurrence, or generic publication kind.

**Governing move in plain terms.** Recover or name the governing FPF pattern and exact project-side FPF kind and reference before allowing the encountered item to guide work or reliance. When that support is absent or insufficient, narrow the move, reopen or refresh the source, run only a bounded reversible probe under a work plan, or block the unsupported claim or effect.

**Recognition block vs assurance block.** Read **At a glance**, **Use this when**, **First output**, **What goes wrong if missed**, **Governed object**, **Governing move**, **Working action path**, **Not this pattern when**, and **What this buys** as the primary recognition block. Read the field tables, lookup table, lint cues, stress cases, conformance checklist, SoTA alignment, and relations below as assurance and support blocks that tighten the same source-restoration claim; they do not widen this pattern into an evidence, gate, engineering-justification, speech-act, commitment, boundary, or work-occurrence pattern.

**Working action path.**
1. Name the encountered item kind and publication position without treating its appearance as source support.
2. Name the live work claim, reliance claim, or P2W load or position and the claim or effect that would be carried.
3. Recover the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect.
4. Choose the lightest admissible project move now: proceed inside recovered support, narrow the move, run a bounded reversible probe under `U.WorkPlan`, reopen or refresh the source, ask the accountable role assignment to expose or repair the missing source episteme, publication, register entry, or project record, or block only the unsupported claim or effect.
5. Return to `A.15` only when the remaining live question is `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation.

**Not this pattern when.** Stay in A.15 when the live problem is only `U.Role`, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` separation. Stay in E.17 when the live problem is only publication-face exposure or multi-view publication. Stay in A.10, B.3, A.20, A.21, A.2.8, A.2.9, A.6, or A.15.1 when evidence, currentness, engineering justification, gate validity, constraint validity, commitment, speech act, boundary claim, or work occurrence already governs the live claim or effect directly.

**What this buys.** The acting engineer-manager can keep work moving at the lightest admissible level: proceed inside recovered support, narrow the move, run a bounded reversible probe under a work plan, reopen the needed exact project-side FPF kind and reference, ask the role assignment accountable for that source to expose or repair it, or block only the unsupported claim or effect while preserving narrower admissible use.

### A.15.4:1 - Problem Frame

Dashboards, credential views, generated explanations, copied approvals, provenance labels, green tiles, schema wording, API wording, and composed source chains often look ready for action before the governing FPF pattern and exact project-side FPF kind and reference that make the action or reliance admissible have been recovered. The practical problem is not to classify the item in FPF; the problem is to decide what an engineer-manager may do in the project now without turning appearance into approval, gate passage, evidence, assurance, performed work, or release permission.

**Plain recognition line.** Let the visible cue point to the support; do not let it become the support that permits the work or reliance move.

### A.15.4:2 - Cluster Boundary


A.15 remains the kernel for separating `U.Role`, holder and context, `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and actual `U.Work`. A.15.4 starts only when an encountered item begins to support a work claim or reliance claim and the team must recover the exact project-side FPF kind and reference that carries that support. If the governing FPF pattern and project-side reference are already known, use them directly and keep A.15.4 as the bounded restoration step.

### A.15.4:3 - Work-Relevant Source Restoration

##### Core stress-case rule
**Ordinary source-restoration note.** In ordinary use, do not build a source dossier. The first useful note is:

`encountered item; live work claim or reliance claim; governing FPF pattern; exact project-side FPF kind and reference needed; admissible next project move now; blocked overread`

The encountered item may be a tile, credential view, approval-looking memo, generated explanation, copied review, provenance mark, API wording, functional-description publication, or composed source chain. The pattern asks whether the exact work claim or reliance claim is currently supported, not whether the item is impressive, fluent, or easy to read.

**Conditional source-support field set.** Use the fuller fields below only when release, safety, compliance, role, status, gate, assurance, contested source, external reliance, cross-context reuse, currentness, revocation, generated source support, or copied source support is live. These fields are local restoration aids, not a new record kind.

| Field | Working question |
| --- | --- |
| subject or actor | Who or what would perform the work, rely on the item, hold the status, or be affected by the claim? |
| role | Which `U.RoleAssignment` or role-context reading is live? |
| action or work target | Which selected method, method of work, `U.WorkPlan`, planned work, actual `U.Work`, work result, release move, reliance move, status, or effect is being guided? |
| resource or claim target | Which resource, claim, gate, credential, status, evidence, approval, or source finding with authority-reference relation is supposedly affected? |
| context | Which bounded context, environment, project slice, interface setting, protocol setting, or relying situation makes the claim live? |
| policy or gate version | Which policy, gate profile, constraint version, method version, or register edition is supposed to govern the claim? |
| time window | During which window is the support claimed to hold? |
| currentness or revocation status | Is the supporting source current, stale, revoked, superseded, expired, contradicted, or unknown? |
| issuer or source | Which issuer, exact project-side FPF kind and reference, register source, status source, speech act, gate decision, evidence path, or work-occurrence record carries the support? |
| verifier or relying context | Who is checking or relying on the claim, and in which context? |
| evidence or attestation path | Which `A.10` evidence, provenance, or attestation path, if any, supports the claim without itself becoming approval, gate passage, assurance, or work occurrence? |
| sourceSupportPosture | Which `E.17:5.1b` posture applies to the encountered item and required claim or use? |
| unsupported effect | Which requested work claim, reliance claim, or downstream effect remains unsupported and must be narrowed, repaired, reopened, probed, or blocked? |


Start with the A.15.4 working action path above when the encountered item is about to guide a work move, reliance move, or work-relevant claim. If the live issue is only evidence, currentness, gate validity, constraint validity, engineering justification, commitment, speech act, boundary wording, admissibility wording, credential proof, status proof, explanation, comparison, or carrier and front-end behavior, apply that governing FPF pattern and exact project-side FPF kind and reference directly; use A.15.4 only when that source must be restored before role, method, plan, work, work result, result measurement, or another work move or reliance move can proceed.

**Authority-looking source-backed work or reliance case.** Use A.15.4 when an approval-, permission-, gate-, command-, credential-, delegation-, revocation-, status-, provenance-, dashboard-, copied-review-, generated-explanation-, schema-, API-, or composed-chain case is about to be used as a work cue, reliance basis, release reliance basis, execution-evidence basis, approval claim basis, approval effect basis, role claim basis, status claim basis, or next work-relevant move. The recognition moment is that an encountered publication, display, credential view, wording, or explanation looks like permission, prohibition, readiness, or evidence for starting work; the governed question is still the live work claim, reliance claim, or P2W load or position plus the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect being read from, or through, the wording, display, publication face, carrier, or source-finding cue. It is not the wording alone. A.15.4 does not change the governed object of `A.15`; it governs only the source-restoration step before the encountered case can support work or reliance.

Here "authority-looking case" is only a recognition phrase for the encountered situation; it is not a `U.*` kind, not a profile, not a score, and not a new evidence source, governing pattern, or `authoritySourceRef` target. The source-backed object that permits, forbids, records, or supports the work may instead be a `GateDecision`, `SpeechAct`, `Commitment`, `RoleAssignment`, credential record, status record, `A.6.B`-governed claim, `A.10` evidence path, or `B.3` assurance claim. Use `E.17:5.1c` for the shared meanings of `orientation use`, `reliance use`, work claim, reliance claim, operative claim, unsupported downstream use, and `reopen trigger`; use `E.17:5.1d` when the primary live question may belong to another governing FPF pattern with its exact project-side FPF kind and reference.

The central behaviour is: name the live work claim, reliance claim, or P2W load or position; name the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect; keep the `U.Episteme` or `U.EpistemePublication` distinct from publication form, MVPK face, carrier, rendering, and source-finding cue; choose the minimum sufficient next move; recover only the exact project-side FPF kind and reference needed for that move; and do not raise the claim beyond that recovered support. If the named project record states the governing FPF relation, use that recorded relation directly rather than inferring support from wording.

**Positive repaired path.** An encountered `U.Episteme` publication, publication form, MVPK face, carrier, rendering, or source-finding cue may guide work or reliance only to the support carried by the recovered exact project-side FPF kind and reference, actor or role, live work claim, reliance claim, or P2W load or position, affected work target, context, window, and source-supported claim or effect. The repaired outcome is the smallest admissible work or reliance statement plus the unsupported work claim or reliance claim still blocked.


Load posture by governing FPF pattern and exact project-side FPF kind and reference:

| Work or reliance posture | Use when | Minimum useful record |
| --- | --- | --- |
| Orientation or source-finding note | The encountered item is only a publication face, carrier, rendering, cue, search handle, learning aid, or reversible local probe trigger. | `encountered item; required claim or effect not yet supported; source to reopen; stop condition`. |
| Routine reliance note | The team needs ordinary bounded reliance without release, safety, compliance, delegated status, contested source, or cross-context reuse. | Live work claim, reliance claim, or P2W load or position; required claim or effect; actor or role; affected work target, context, and window; visible source ref; and reopen condition. |
| Load-bearing reliance path | The required claim or effect is external-impact, irreversible, release-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, revoked, status-bearing, generated-source-mediated, copied-source-mediated, provenance-mediated, contested, or cross-context. | Exact project-side FPF kind and reference with the live `A.10`, `A.6`, `B.3`, `A.2.9`, `A.2.8`, `A.21`, `A.20`, or `A.15.1` support fields needed for that claim or effect. |

A small A.15.4 restoration note is enough for the first posture:

| Field | Value |
| --- | --- |
| live work claim, reliance claim, or P2W load or position | Name the live work claim, reliance claim, P2W load, or P2W position exactly: method-family selection, selected method, method of work, work plan, planned work, actual `U.Work`, work result, result-measurement, release reliance decision, or non-work reliance claim. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record; actual execution becomes `U.Work` only after it occurs and is recorded under `A.15.1`; work-result measurement belongs with the evidence or result-measurement source. This row is a local restoration label unless it cites an existing FPF kind or governing FPF relation. |
| governing FPF pattern and exact project-side FPF kind and reference | Approval, permission, gate passage, role or status currentness, work occurrence, evidence support, assurance claim, boundary claim, or other exact claim or effect needed before that load, position, or claim can be treated as supported. The governing relation must be carried by the named FPF pattern and recovered project-side reference, not by a new `A.15.4` kind. |
| actor or role | Who would act or rely. |
| affected work target, context, and window | Release, service, person, role holder, work item, claim, tenant, environment, physical batch, construction element, machine state, or validity window affected by that class or claim. |
| claim-bearing episteme or episteme publication | The claim-bearing FPF kind is `U.Episteme` or a species such as `U.EpistemePublication`; if the encountered item is only a publication form, MVPK face, carrier, rendering, `PublicationUnit`, dashboard tile, copied text, credential view, generated explanation, API wording, or cue, name that exact kind separately. |
| exact project-side FPF kind and reference needed or safe next move | Source `U.Episteme`, source `U.EpistemePublication`, register entry, or exact project-side FPF kind and reference to reopen; status to refresh; reversible probe; role assignment accountable for exposing or repairing the missing source; or narrower admissible use. |
| stop or reopen condition | What blocks the work claim or reliance claim and what would reopen it. |

**Borrowed episteme/publication discipline.** A.15.4 borrows the `C.2.1`, `E.17`, and `A.16.0` distinction rather than minting a new generic `U.*` kind. The claim-bearing FPF kind here is `U.Episteme`; `U.EpistemePublication` is used only when that episteme is available as a published episteme with MVPK-face references. Publication forms, MVPK faces, carriers, renderings, `PublicationUnit` instances, and source-finding cues are separate kinds or roles in the case. A planned baseline remains a `U.WorkPlan` or `U.WorkPlanning` plan record such as `SlotFillingsPlanItem`; launch values and finalization values remain their own project records, decision logs remain gate or decision records, execution evidence remains evidence, and actual work occurrences remain `A.15.1` or `U.Work` matters.

When the required exact project-side FPF kind and reference is incomplete, choose one admissible degraded-operation move after naming the live work claim, reliance claim, or P2W load or position and the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect; pick the lightest move that preserves practical work and source recoverability:

1. Use the encountered item only for orientation or source-finding.
2. Reopen the required source `U.Episteme`, source `U.EpistemePublication`, register entry, or exact project-side FPF kind and reference, or refresh status or currentness.
3. Narrow actor or role, requested operation or work class, affected target, context, and window until the recovered source really covers the move.
4. Run a bounded reversible probe under an explicit `U.WorkPlan` when no external-impact reliance is being made.
5. Ask the role assignment accountable for the issuer, gate decision, evidence path, role record, status record, or boundary claim set to expose or repair the missing source.
6. Repair the `U.WorkPlan`, `U.MethodDescription`, dashboard label, source link, or boundary wording that made the overread plausible.
7. Proceed only inside the recovered scope and window.
8. Block only the work claim or reliance claim that lacks source support.

##### Repair assignment rule

**Broken-source repair assignment.** If the required exact project-side FPF kind and reference is unavailable to the acting user, assign only prospective repair work, request work, decision work, work-plan work, or source-gap work to the role assignment accountable for the issuer record, gate decision, evidence path, role record, status record, or boundary claim set. The acting user records the blocked work claim or reliance claim and the missing source relation to expose or repair, then proceeds only with the safe narrowed move available under recovered support. The repair request or source-gap note is not past evidence, approval, gate passage, performed `U.Work`, release permission, or assurance.


An encountered item may be a `U.Episteme`, a `U.EpistemePublication`, a publication form, an MVPK face, a carrier, a rendering, a `PublicationUnit`, or only a source-finding cue. Name that kind before using it. Do not treat a file, display, dashboard tile, model card, credential view, generated text, `PublicationUnit`, publication face, or carrier as the source claim, effect, work occurrence, gate decision, role record, status record, evidence relation, or assurance claim by presentation alone. If the encountered item exposes an exact project-side FPF kind and reference, use the exposed `GateDecision`, `SpeechAct`, evidence path, credential source, status source, work-occurrence record, or other exact FPF source directly; do not infer that support from the display face itself.

**Adversarial misuse guard.** Do not let release pressure, delegated pressure, compliance pressure, unsourced green-dashboard pressure, copied wording, or generated wording convert a cue into work support or reliance support. A properly designed dashboard tile may guide release when it is a current view of the relevant `GateDecision` plus evidence path and currentness path; pressure or color alone does not replace that source.


##### Exact project-side FPF kind and reference lookup table

Exact project-side FPF kinds and references by required claim or effect kind:


- cue-only orientation: use only for attention or source-finding; stay with `A.16` or `A.16.1` for pre-articulation cues or `A.6.A` for `A.6.A`-governed invitation. Cue-only orientation is not work guidance, work plan, gate passage, approval, work occurrence evidence, or assurance.

- issuing, approval, authorization, delegation, or revocation act: cite `A.2.9` `U.SpeechAct` or `SpeechActRef`, including act type, actor, role, affected work target or claim target, judgement context, window, carrier reference, evidence reference when currentness matters, and instituted effects if claimed; because `U.SpeechAct <: U.Work`, the same act can satisfy dated work-occurrence evidence only for that communicative act itself. It does not evidence the deployment, release, repair, inspection, or other operational work that the act approved, ordered, or described;
- role or status reliance: cite `A.2.1` or `U.RoleAssignment`, a status-changing `U.SpeechAct`, a governing context-state record, a credential proof or status result under `A.10`, or an `A.21` `GateDecision` when the status is gate-governed; do not infer a status kind from a label;
- deontic permission, obligation, prohibition, or recommendation-as-duty: cite `A.2.8` `U.Commitment` and the instituting `SpeechActRef` when provenance matters; if "permission" means admissibility predicate, gate passage, authorization act, role effect, status effect, credential status, cue, or advice, use `A.6.B`, `A.21`, `A.2.9`, `A.2.1`, `A.10`, `A.16`, or `A.6.A` according to the actual claim or effect kind instead;
- boundary, policy, API, schema, "allowed", "authorized", "approved", "recommended", or "guaranteed" wording: split the statement through `A.6` or `A.6.B`; use `A.6.C`, `A.2.3`, `A.2.8`, and `A.2.9` for agreement-like guarantee, SLA, or promise wording before work use or reliance use;
- gate decision or gate passage: cite `A.21` `OperationalGate(profile)`, `GateDecision`, `GateDecisionRationale`, `DecisionLogRef`, gate profile, gate version, check set, scope, window, and replay or freshness pins;
- constraint or flow-validity witness: cite `A.20` `ConstraintValidity` status, witness, `GateCheckRef.aspect = ConstraintValidity`, path, window, sentinel, and pins as applicable; this is not identical to a gate decision;
- release, deployment, or rollback work occurred: cite `A.15.1` dated `U.Work` occurrence and the `A.10` evidence carrier path; a gate decision or command-like cue is not execution evidence;
- evidence, provenance, authenticity, currentness, copied-source, or generated-source support: apply `A.10`; evidence support does not approve, permit, execute, pass a gate, or raise assurance by itself;
- assurance, readiness, safety, compliance, trust, release confidence, `R`, `F`, `G`, or `CL` increase: apply `B.3`;
- generated explanation: use `E.17.EFP` for explanation faithfulness or source-finding relation, then require `A.10` claim-bound source support for every operative claim that will be relied on.
- approval claim or effect split: if approval means someone approved something, cite `A.2.9` `U.SpeechAct` or `SpeechActRef`; if the approval institutes a deontic binding, cite `A.2.8` `U.Commitment` and the instituting act; if it means a gate passed, cite `A.21` `GateDecision` or `DecisionLogRef`; if it is being used as evidence that release or other work occurred, cite `A.15.1` dated `U.Work` plus `A.10`; if it is only approval wording in boundary, API, policy, or schema prose, split through `A.6` or `A.6.B`; if it is evidence of approval, apply `A.10`; if it is confidence because something was approved, use `B.3` only when a typed assurance claim is live.
- permission claim or effect split: if permission is a deontic relation, cite `A.2.8` `U.Commitment` and the instituting source; if it is an admissibility predicate, cite the `A.6.B` `A-*` claim; if it means gate passage, cite `A.21`; if it means an authorization act, cite `A.2.9`; if it changes or depends on role or status, cite `A.2.1` or status-changing support; if it means credential status, use `A.10`; if it is only a UI label, badge, dashboard display, or permission-looking wording, treat it as orientation or source-finding until the required exact project-side FPF kind and reference is recovered.
- authorization claim or effect split: if authorization means a speech act authorizing, cite `A.2.9`; if it means a policy or admissibility predicate over subject, requested policy operation or work class, affected resource or work target, context, and policy version, split through `A.6.B`; if it means gate decision or gate passage, cite `A.21`; if it means access proof, credential proof, status proof, or currentness, use `A.10`; if it means role assignment, role effect, or status effect, cite `A.2.1` or status-changing support; if it is being used to say execution happened, do not use authorization as evidence of execution, cite `A.15.1` dated `U.Work` plus `A.10` instead.


Return products for loop closure:

| Governing source relation used | Return product for this A.15.4 restoration | What the return product does not hide |
| --- | --- | --- |
| `A.6` or `A.6.B` | Typed claim IDs (`L-*`, `A-*`, `D-*`, and `E-*`) plus the governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect. | Raw wording is not work support or reliance support. |
| `A.10` | Claim-bound evidence path, freshness posture, currentness posture, and admissible or non-admissible use for the attempted claim. | Evidence support is not approval, permission, gate passage, work occurrence, or assurance. |
| `B.3` | Typed assurance claim, no-assurance-use disposition, or rejected/downgraded assurance claim. | Assurance wording is not a generic trust label. |
| `A.21` | `OperationalGate(profile)`, `GateDecision`, `DecisionLogRef`, gate profile, gate version, scope, window, and replay or freshness pins. | Gate passage is not execution evidence or assurance. |
| `A.20` | `ConstraintValidity` status, witness, path, window, sentinel, and pins where live. | Constraint validity is not the gate decision itself. |
| `A.2.9` | `SpeechActRef` with act type, actor, role, affected work target or claim target, judgement context, window, and instituted effects if claimed. | A speech act is not deontic binding, gate passage, or operational work occurrence by itself; as work-occurrence evidence it supports only the communicative act that occurred. |
| `A.2.8` | `U.Commitment` deontic relation with accountable role, agent, content, object, window, and instituting source when needed. | Commitment is not proof that work occurred. |
| `A.15.1` | Dated `U.Work` occurrence plus evidence carrier path when relied on. | Work occurrence is not permission or assurance. |
| `E.17.EFP` | Explanation class, source-finding relation, and faithfulness relation over the source `U.Episteme` or source `U.EpistemePublication`. | Explanation is not operative source support without A.10 claim-bound evidence. |


Load-bearing work or reliance - especially external-impact, irreversible, release-bearing, role-bearing, status-bearing, gate-bearing, compliance-bearing, safety-bearing, delegated, contested, or assurance-bearing claim or effect - is admissible only for the actor, role, live work claim, reliance claim, P2W load, P2W position, affected work target or claim target, audience, scope, environment, version, policy context, operational mode, and time window for which required FPF-governed project support is recoverable. Cue-only, source-finding, learning, and bounded reversible probes stay lightweight and do not require a full source dossier.

Quick dispositions:


| Encountered case | First `A.15.4` disposition |
| --- | --- |
| Source-backed release dashboard tile | If the tile is a current dashboard view of `A.21` `GateDecision` or `DecisionLogRef` plus release target or work target, environment, scope, window, gate profile, gate version, and `A.10` evidence path, it may support gate-passage reliance for that release and environment. |
| Unsourced or stale release dashboard tile | Display or source-finding only until the current `GateDecision` or `DecisionLogRef`, release target or work target, scope, window, gate profile, gate version, and `A.10` evidence path are recoverable; use `B.3` only if an assurance claim is live. |
| Copied review summary or copied approval | Copied wording and copied-currentness posture at most; approval, authorization, permission, commitment, or work occurrence needs the original `A.2.9` `SpeechActRef`, `A.21` decision, `A.2.8` commitment, or `A.15.1` work source plus `A.10` evidence. |
| Delegation chain with forwarded approval | Each link names delegator, delegatee, delegated operation or work class, affected target, scope, window, source permitting delegation, subdelegation allowance if any, revocation state, currentness state, and evidence path. A forwarded approval is not delegated authority by copy alone. |
| Role, revocation, or status display | Resolve to role assignment, status-changing speech act, context-state record, credential proof or status result, or gate decision with freshness or revocation support; visual status cannot defeat a higher-priority revocation or supersession source. |
| Conflicting sources | Do not resolve by color, visual salience, copied wording, or apparent recency. Name source order, governing decision source, freshness policy, and supersession rule; the work claim, reliance claim, or effect is contested until resolved, while source-finding and bounded reversible probes remain available. |
| Credential badge or register-backed status view | Use the display as a publication of a credential source or status source, not the source itself. Find the governing status register or issuer, trust anchor, holder binding or subject binding, verifier context, relying context, proof or status result, revocation, freshness, and validity window. If the governing register entry itself creates or changes role, status, permission, duty, or gate state in the bounded context, cite that exact register or status-source entry and the `A.2.1`, `A.2.8`, `A.2.9`, `A.6.B`, or `A.21` source it depends on. Otherwise rely only on credential-currentness for that holder and context. |

| Rollback command-like cue | Treat as cue or `A.6.A`-governed invitation unless exact command, authorization, work occurrence, execution result, or gate support is recoverable. |
| Generated explanation says "authorized" | Explanation may help find sources; it does not issue, approve, revoke, commit, authorize, pass a gate, evidence execution, or raise assurance. A citation or source mention inside the explanation supports work use or reliance use only when the cited carrier supports that exact relied-on claim in the relying context under `A.10`. |

| Extracted source, rewrite, representation shift, explanation, then gate or release claim | Reopen the most directly claim-bearing exact project-side FPF kind and reference at the first lossy or non-commutative transform step; the gate claim or release claim waits for required transform, evidence, explanation, gate, or assurance support. |
| Repeated green-tile failures without recoverable source support | Treat recurrence as upstream source-system repair work: expose decision refs, fix dashboard semantics, add source links and currentness, revise boundary wording, or add review cues so the acting user is not repeatedly forced to reconstruct missing source support. |


##### Worked dashboard/approval examples

Worked dashboard and approval slice:

A release dashboard shows a green approval-looking tile for `Release-2026.05.08-prod`. If the tile is a current view of the relevant `GateDecisionRef` plus evidence path and currentness path, it may support bounded gate-passage reliance for that release target and window. Execution or deployment still requires an `A.15.1` work-occurrence source if the claim is that deployment happened. If the gate source is missing or stale, treat the tile as orientation and source-finding until the team can name the live release-work load, live release-work position, governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect, and exact project-side FPF kind and reference that carries the gate decision, evidence path, and currentness path.

| Step | Required move |
| --- | --- |
| Required project claim or effect kind | Release reliance, gate passage, compliance proof, assurance increase, evidence support, or currentness support. |
| Gate decision source | Cite the current `A.21` `GateDecision` or `DecisionLogRef`, gate profile, gate version, release target or work target, scope, window, and replay or freshness pins. Without that source, the tile is not release permission or gate passage. |
| Constraint or flow-validity source | Cite `A.20` `ConstraintValidity` status or witness only when the claim is about constraint or flow validity, not about the gate decision itself. |
| Evidence and currentness source | Use `A.10` for the dashboard query, carrier integrity, evidence refs, time, window, freshness stance, revocation stance, verifier context, relying context, and rival explanation such as stale display or copied status. |
| Assurance source | Use `B.3` only if the tile is being used to raise readiness, compliance, trust, safety, release confidence, `R`, `F`, `G`, or `CL`; otherwise no assurance tuple is live. |
| Admissible repaired use | With the decision and evidence path recovered, rely on gate passage only for the named release target or work target, environment, gate profile, gate version, time, and window; a claim that deployment happened still needs an `A.15.1` work-occurrence source. |
| Blocked overreads | The dashboard color does not create approval, permission, compliance proof, rollback success, work occurrence, or assurance by display. |

Approval memo green path:

An approval memo may support an approval claim when it exposes the `A.2.9` `SpeechActRef`, actor, role, affected release target or work target, judgement context, time, window, carrier refs, evidence refs, and instituted effect being claimed. That supports the bounded approval claim or effect only. It does not prove that release, deployment, rollback, or other work occurred; that execution claim still needs the dated `A.15.1` work-occurrence source plus any `A.10` evidence path required for the relying context.

Credential/status green path:

A credential or status response may support holder reliance, status reliance, or currentness reliance only inside the issuer or governing status register, holder binding or subject binding, verifier context, relying context, proof result or status result, revocation stance, freshness stance, and validity window that it exposes. It does not by itself support release, work occurrence, gate passage, engineering justification, evidence for underlying operational facts, or contextual permission; those uses require the exact project-side FPF kind and reference that governs that claim or effect.

Role prompts:

| Role in the situation | Prompt |
| --- | --- |
| Acting user | What can I safely do next without turning the encountered episteme or episteme publication into unsupported work support or reliance support? |
| Release engineer | Which `A.21` gate decision, decision log, release target, work target, and `A.15.1` work occurrence are separate here? |
| Issuer, gate, evidence, or role source | What source, status, decision ref, or evidence path must be exposed or repaired? |
| Auditor/reviewer | Which evidence path, decision ref, speech-act ref, commitment, work occurrence, or assurance claim must be recoverable? |
| Boundary author | Which words need typed claim IDs before they can guide work or reliance? |
| Manager | Is repeated ambiguity a source-system repair item rather than another manual check for the acting user? |
| LLM/tool user | Which exact project-side FPF kind and reference does the explanation help find, and which operative claims still need `A.10` support? |
| Security or compliance source | Which revocation, currentness, proof, status, source order, or supersession source must be exposed? |
| Model or data source | Which intended use, evaluation condition, version, window, limitation, and evidence path bound the model or data documentation? |
| Assurance reviewer | Which named claim is actually receiving an assurance posture, with what assurance tuple, evidence path, limitations, and reopen condition? |
Search aliases for A.15.4 include: approval, approval-looking display, authorization, authorization-looking display, permission, permission display, allowed wording, green dashboard, release tile, release readiness, model card, datasheet, data card, provenance, provenance mark, attestation, attestation label, credential, credential badge, generated explanation, copied review, copied approval, review summary, compliance-looking mark, delegation, delegation display, revocation, revocation status, gate passed, gate passage, rollback successful, rollback cue, and assurance label. These are search handles only; decide the carrying exact project-side FPF kind and reference and governing FPF pattern or source relation from the live work question or reliance question, not from the displayed word or carrier name or source name.

Work and reliance disposition map for authority-looking cases:

| Live question | Start in | First useful output |
| --- | --- | --- |
| Can this encountered episteme publication, publication face, carrier, rendering, or cue guide work or reliance? | `A.15.4` | Candidate next `U.WorkPlanning`, `U.Work`, or reliance move, governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect, minimum admissible next move, and exact project-side FPF kind and reference needed. |
| Is the problem boundary, policy, API, schema, or connector wording? | `A.6` or `A.6.B` | Typed `L-*`, `A-*`, `D-*`, and `E-*` claims before the work claim or reliance claim is used. |
| Is the problem evidence, currentness, provenance, credential status, generated-source support, copied-source support, or source-chain recovery? | `A.10` | Claim-bound evidence path, currentness path, and admissible or non-admissible use. |
| Is the problem assurance, readiness, safety, compliance, trust, release confidence, `R`, `F`, `G`, or `CL` posture? | `B.3` | Typed assurance claim, no-assurance-use disposition, or downgraded or rejected assurance use. |

Display guidance for bounded status: a visible status meant to guide work should expose source type, exact ref or link, freshness, window, scope, unsupported work claim, unsupported reliance claim, and unsupported effect. For example, prefer `Gate check passed; GateDecisionRef; release target; environment; window; not compliance proof, rollback success, or assurance increase` over a bare approval-looking label.

Incident-learning fields for authority-looking overread: encountered episteme or episteme publication, live work claim, reliance claim, P2W load, or P2W position, governing FPF pattern and exact project-side FPF kind and reference that carry that claim or effect, actor, role, affected work target or claim target, context, window, missing or stale source `U.Episteme`, source `U.EpistemePublication`, register entry, or exact project-side FPF kind and reference; governing FPF relation or role assignment accountable for exposing or repairing that missing source, plausible overread, safe disposition used now, and upstream repair item for the source, dashboard, explanation, credential view, boundary wording, publication face, or carrier.

Contestability and redress path: when an authority-looking case affects person or team status, access, assignment, responsibility, release blockage, compliance posture, or safety-impacting work, name the review path or redress path before the work claim or reliance claim hardens. The path should name the disputed source or claim, the role assignment accountable for refreshing or correcting that source, the evidence path or status path to reopen, the safe interim disposition, and the time and window for review.


Lintable overread cues:

| Lint signal | Exact governing exit |
| --- | --- |
| `approved`, `authorized`, `allowed`, `recommended`, or `guaranteed` in boundary, API, schema, or policy wording | Split through `A.6` or `A.6.B` into `L-*`, `A-*`, `D-*`, and `E-*`; use `A.6.C`, `A.2.8`, and `A.2.9` for agreement-like wording where live. |
| Dashboard tile, status color, or release tile used as release evidence or gate passage | Require `A.21` `GateDecision` or `DecisionLogRef` plus `A.10` evidence path and currentness path. |
| Credential screenshot or badge used as permission, authorization, role support, or status support | Require `A.10` issuer, holder, verifier, status, currentness, and relying-context support, then exact `A.2.8`, `A.2.9`, `A.2.1`, `A.6.B`, or `A.21` source for the required permission, authorization, role, status, gate claim, or gate effect. |
| Generated explanation uses `authorized`, `approved`, or similar wording | Use `E.17.EFP` for explanation relation and source-finding relation and `A.10` claim-bound source support; issue, approval, gate, and commitment claims still need `A.2.9`, `A.21`, or `A.2.8`. |
| Model card, datasheet, label, or note cited as readiness, safety, compliance, or release confidence | Require a typed `B.3` assurance claim, intended-use match, evaluation condition, limitations, and `A.10` evidence path. |
| Provenance or attestation label cited as truth, safety, release, or permission | Require `A.10` bounded provenance claim or process claim plus separate evidence for truth, safety, release, permission, or assurance. |
| Evidence, assurance, gate, or work-occurrence words without the exact project-side FPF kind and reference that carries that claim or effect | Recover the `A.10`, `B.3`, `A.21`, or `A.15.1` support fields respectively before the work claim or reliance claim is used. |

Stress cases for practice:

| Case | Expected A.15.4 disposition |
| --- | --- |
| Green release dashboard tile with no `GateDecisionRef`. | Source-finding only; recover `A.21` decision or decision log plus `A.10` evidence before gate-passage reliance. |
| Copied approval from last month. | Recover original `A.2.9` `SpeechActRef`, currentness, freshness, and any live `A.2.8` commitment or `A.21` gate source. |
| Credential badge screenshot after revocation. | Treat as contested credential-currentness; use `A.10` issuer, holder, verifier, status, and revocation path and do not infer permission. |
| Generated explanation says `authorized by policy`. | Use `E.17.EFP` for explanation and source-finding and `A.10` claim-bound support; issuing, gate, and commitment claims still need their own sources. |
| Boundary wording says `guaranteed approved for production`. | Split through `A.6` or `A.6.B`; if agreement-like or promise-bearing, unpack through `A.6.C`, `A.2.8`, and `A.2.9`. |
| Dashboard says green while decision log says blocked. | Treat as conflicting sources; name source order, governing decision source, freshness policy, and supersession rule before the work claim or reliance claim is used. |

### A.15.4:4 - Conformance Checklist

| ID | Requirement (Normative Predicate) | Purpose / Rationale |
| :--- | :--- | :--- |
| **CC-A15.4-1 (Work-relevant source restoration)** | Before an authority-looking case guides work or reliance, a conforming `A.15.4` use SHALL produce the ordinary source-restoration note: encountered item, live work or reliance claim, P2W load or position, governing FPF pattern, exact project-side FPF kind and reference needed, admissible next project move now, and blocked overread. It SHALL identify the neighboring FPF pattern and exact project-side FPF kind and reference that actually carry the requested approval, permission, status, evidence, gate, assurance, or work-occurrence support; if that source is absent or stale, mark only the unsupported reliance as orientation-only, contested, reopened, or blocked. Fuller source-support fields open only when the live use, dispute, or reliance case requires them. Any new repair request, future decision request, prospective work-plan entry, or explicit source-gap note is prospective and SHALL NOT be used as retroactive evidence, approval, gate passage, performed `U.Work`, release permission, or assurance. A conforming `A.15.4` use SHALL NOT absorb evidence, assurance, boundary wording, gate decision, role or status, commitment, speech-act, or work-occurrence semantics from `A.10`, `B.3`, `A.6`, `A.2.1`, `A.2.8`, `A.2.9`, `A.20`, `A.21`, or `A.15.1`. | Prevents displays, badges, copied text, generated explanations, and composed chains from becoming authority by appearance while keeping ordinary use cheap. |
| **CC-A15.4-2 (P2W publication use boundary)** | A principle scheme, functional diagram, scenario, screen, or explanation that makes a P2W chain readable SHALL NOT be used as performed `U.Work`, work authority, evidence, gate passage, engineering justification, or release permission by publication alone. | The project use names the exact `A.15` object it supports: method-family selection, selected method, `U.WorkPlan`, performed `U.Work`, work-result record, or result measurement; unsupported claims require their own exact project-side FPF kinds and references. |

### A.15.4:5 - Common Anti-Patterns and How to Avoid Them

- **Authority-looking case as source, work overread, role overread, or status overread.** Do not treat a dashboard tile, credential display, copied approval, generated explanation, provenance label, command-like cue, or composed source chain as approval, permission, gate passage, role currentness, status currentness, work occurrence, evidence, or assurance by appearance. First name the live work claim, reliance claim, P2W load, or P2W position, then recover the governing FPF pattern and exact project-side FPF kind and reference that actually carry the requested approval, permission, status, evidence, gate, assurance, or work-occurrence support, or block only that unsupported reliance.

### A.15.4:6 - SoTA Alignment

**SoTA alignment rule.** Read the row here as source idea -> local FPF invariant -> practical local test -> popular shortcut rejected. A source citation governs nothing by reputation; it counts only when the cited idea is translated into the Solution, conformance checks, boundary rules, worked slices, and relations of this pattern.

| Claim need | Source idea and current source | Current source reference | Local FPF invariant and practical local test | Adopted invariant, adapted invariant, and rejected shortcut |
| --- | --- | --- | --- | --- |
| Dynamic authorization or policy-response displays need exact operation, target, context, and window support. | Dynamic authorization practice separates subject, requested operation, affected target, context, and window before a relying move is allowed. | NIST Zero Trust and dynamic authorization practice; Cedar policy language; Zanzibar-style relation authorization; source maturity = current standards, specifications, and widely used technical practice. | The restoration note names the live work claim, reliance claim, P2W load, or P2W position, the affected work target or claim target, policy version, context, and time window before treating a visible allow response, deny response, or policy response as support. | **Adopt, adapt, reject.** Adopt bounded currentness and source-support invariants; adapt them through exact FPF project records; reject treating policy-looking output as permission or work authority by display. |
| Credential or register-backed status needs issuer, holder, verifier, status, currentness, and relying-context support. | Credential and status practice separates issuer, holder binding or subject binding, verifier context, relying context, proof result or status result, governing register entry, revocation, freshness, and validity window. | W3C Verifiable Credentials and digital identity or register-backed status practice; source maturity = current specifications and technical practice. | A credential view or status tile can support only the holder claim, status claim, or currentness claim whose issuer, register, proof result or status result, revocation, freshness, and relying context are recoverable. | **Adopt, adapt, reject.** Adopt status-currentness separation; reject reading a badge, screenshot, or register excerpt as role, status, permission, gate passage, or work support without the governing FPF pattern and exact project-side FPF kind and reference. |
| Provenance and attestation marks need source support and process support without becoming truth, release, or work evidence. | Provenance and attestation practice separates origin support, process support, build claim, supply-chain claim, and verification metadata from truth of downstream claims or release permission. | C2PA content provenance; SLSA and in-toto attestations; source maturity = current standards, specifications, and widely used practice. | A provenance or attestation mark remains source support or process support until `A.10`, `B.3`, `A.20`, `A.21`, `A.15.1`, or another exact source relation carries the downstream claim. | **Adopt, adapt, reject.** Adopt source traceability and process traceability; reject provenance-mark-as-truth, release permission, gate passage, assurance, or work occurrence. |
| Change, gate, release, and approval displays need decision, schedule, and executed-work separation. | Release and change practice separates approval acts, authorization acts, gate decisions, planned schedules, and executed work. | ITIL 4 Change Enablement and current release or change practice; source maturity = current practitioner guidance plus mature service practice. | A dashboard or approval-looking display must expose the `GateDecision`, `SpeechAct`, `Commitment`, `U.WorkPlan`, or `A.15.1` work-occurrence source that carries the exact claim or effect. | **Adopt, adapt, reject.** Adopt decision, schedule, and executed-work separation; reject a green tile, copied approval, or generated explanation as rollout, release, or work support by appearance. |

**Digital-identity and provenance boundary.** The W3C Verifiable Credentials, C2PA, SLSA, in-toto, Cedar-style, Zanzibar-style, NIST, and ITIL sources are used for currentness, status, provenance, authorization-support fields, and change-practice fields. They do not turn a visible credential, provenance label, attestation, policy response, register excerpt, or dashboard state into work occurrence, gate passage, permission, assurance, release, or project claim support without the exact project-side FPF kind and reference required by `A.15.4`, `A.15`, `A.10`, `B.3`, `A.20`, or `A.21`.

The nearest recovery anchors are the worked dashboard and approval examples, `CC-A15.4-1`, `CC-A15.4-2`, `A.10`, `B.3`, `A.20`, `A.21`, `A.2.8`, `A.2.9`, and `A.15.1`. If a SoTA row cannot be recovered through those local checks, do not let the source citation stand in for the local `A.15.4` rule.

### A.15.4:7 - Relations

* **Cluster relation:** `A.15.4` is a cluster member under `A.15` for work-relevant source restoration; it does not replace the A.15 role, method, plan, and work kernel.
* **Uses:** `E.17:5.1b` and `E.17:5.1c` source-support and use vocabulary, `E.17.EFP` for generated-explanation faithfulness and source-finding, `A.6`, `A.6.B`, and `A.6.C` for boundary, policy, API, and schema wording, `A.10` for evidence, currentness, provenance, and credential status, `B.3` for engineering justification claims, `A.20` for constraint validity, `A.21` for gate decisions, `A.2.8` for commitments, `A.2.9` for speech acts, and `A.15.1` for dated `U.Work` occurrences.
* **Returns to:** `A.15` when the remaining live question is role, method, plan, and work alignment rather than source restoration.

### A.15.4:7a - C.29 MLA relation

> If a mathematical lens appears in work-relevant source restoration, use `C.29` only to state why the lens helps expose or bound an encountered item such as a visible item, generated wording, dashboard cue, copied phrase, publication form, MVPK face, carrier, rendering, `PublicationUnit`, or source-finding cue. `A.15.4` still governs the exact source item, visible item, restoration or reopen condition, reliance support, and whether that item can support work. Method choice, plans, and performed work return to `A.15` and `A.15.1`; lens adequacy does not turn a cue, rendering, or diagnostic phrase into source support.

### A.15.4:End
