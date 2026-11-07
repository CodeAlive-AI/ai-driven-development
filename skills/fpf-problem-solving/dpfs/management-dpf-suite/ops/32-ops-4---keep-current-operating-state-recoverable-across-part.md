## OPS.4 - Keep Current Operating State Recoverable Across Participants

> **Status:** Stable


### OPS.4:0 - Use This When

Use this pattern when people must coordinate continuing Work but act from stale, partial, conflicting, differently authorized, or differently grained accounts of the same operating subjects. Typical cues are “we need one source of truth”, a control room with no claim provenance, a board that hides field state, a case handoff that loses the next decision, or a dashboard whose users cannot tell what they may change.

The first useful move is to use or repair the account needed by one participant decision:

> For subjects `S` and commitments `C`, current claims `Q` at horizons `T` have support `E`, with the provenance and uncertainty needed by this decision. Preserve any consequential disagreement, missing condition, access or decision authority, next action and condition for updating the account.

Aligned attention does not require identical screens or consensus. It requires that participants can recover the subjects, qualified claims, evidence, permissions, disagreements, and next decision relevant to their Work.

Recognition is cheap: enter when a participant cannot resume, decide, or explain a material disagreement from the maintained account. Assurance is claim-specific: world state, evidence, authority, permission, Work, safety, stability, causal effect, and release or acceptance decisions keep their own governing patterns.

Do not use OPS.4 to build a generic dashboard, mandate transparency, create one shared mental model, replace specialist records, or declare state true because it is visible. If the current problem is a Work-performance configuration or recovery dependency after interruption or support loss, use `A.15.8` for that general question and keep the operation-specific state and commitments here.

#### OPS.4:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| current operating account | A participant-usable set of qualified claims tied to exact operating subjects, commitments, evidence, permissions, decisions, and refresh conditions. It is neither the operating System nor a universal database. |
| subject-state claim | A claim about one subject or relation at a stated time or horizon, with the scheme, conditions, provenance and uncertainty needed to use it; authority is a separate condition where the claim or action depends on it. |
| currentness | The condition under which a claim remains usable for a named decision and horizon. Recent timestamps alone do not establish it. |
| provenance | The source, observation, transformation, record, and responsibility facts needed to judge the claim's receiving use. Provenance does not make the claim true by itself. |
| uncertainty | Missing, estimated, conflicting, stale, or bounded information whose reach can change action. |
| disagreement | Two or more recoverable claims, interpretations, or decisions that cannot yet be used as one result. Visibility of disagreement is compatible with aligned attention. |
| permission and change authority | Separately supported relations governing who may read, write, approve, hold, release, or otherwise use account content. Visibility, responsibility, assignment, and capability imply none of one another. |
| next decision or permissible Work | The decision or Work option currently enabled, blocked, or awaiting a named condition. The account does not perform or authorize it by display. |
| participant view | A use-bounded representation of selected account claims for one participant action. Several views may coexist when subject and claim correspondence remain recoverable. |
| control representation | A view, loop diagram, dashboard, or control-room display representing selected control structures, relations, rates, or account claims. It establishes none of those facts by appearance. |
| attention-maintenance result | The smallest repaired current account, participant views, gaps, refresh rules, and next-decision returns that let the named participants coordinate. |

### OPS.4:1 - Problem Frame

Continuing operation needs a present account because the operation outlives one meeting, screen, shift, or model session. Claims arrive at different rates from field observations, cases, tests, providers, plans, queues, and specialist decisions. Different participants need different slices and hold different authority.

The aim is therefore not one display or total agreement. It is recoverable correspondence between exact subjects, qualified claims, evidence, permissions, disagreements, and the next decisions each participant must make.

### OPS.4:2 - Problem

Visibility without claim discipline amplifies error. A fresh dashboard can repeat stale field state, a green board can hide an unresolved service commitment, and an integrated twin can merge observations with predictions and planned states. Participants appear aligned until a decision exposes different referents, time horizons, or authority.

The opposite failure stores every record and overwhelms users. Important gaps, conflicts, and expiry conditions disappear in detail, so people reconstruct state from memory or private channels.

### OPS.4:3 - Forces

| Force | Tension |
| --- | --- |
| Speed | Participants need a quick current view, while rushed aggregation can erase provenance and uncertainty. |
| Several horizons | Field control, incident response, release, provider change, and finance update at unlike rates. |
| Several participants | People need different views and permissions, while divergence can hide conflicting claims. |
| Continuing Work | Handoffs and interruptions require recoverability, while an account cannot guarantee capability or performance. |
| Disagreement | Teams want one answer, while preserving a qualified conflict can be safer than premature consensus. |
| Representation | Dashboards and control rooms improve attention, while appearance can be mistaken for state, authority, or proof. |

### OPS.4:4 - Solution

Maintain the smallest decision-specific account that lets named participants recover exact subjects, current qualified claims, commitments, evidence, uncertainty, permissions, disagreements, next decisions, and refresh conditions. Present several views when needed, but keep claim and subject correspondence explicit.

#### OPS.4:4.1 - Pattern-Use Unfolding

1. **Name participants and decisions.** State who must resume, coordinate, hold, release, escalate, or perform next Work; name the horizon and useful stop for each action.
2. **Import exact subjects and relations.** Use the OPS.3 operating-subject account. Do not let a dashboard row, case file, queue position, or control diagram replace the subject or obtaining relation.
3. **Select only decision-changing claims.** For each subject or commitment, state the current claim, effective scheme, conditions, time or horizon, and action it can change.
4. **Attach evidence and provenance.** Preserve the source and support needed for the claim and receiving use, including the observation or result, carrier, transformation, version, reach and uncertainty where they affect reliance. Reuse that basis from the current account. Keep prediction, plan, observation and decision claims distinct.
5. **Expose conflict and absence.** Preserve incompatible claims, missing observations, stale evidence, unknown authority, and unresolved specialist returns. Do not average them into false agreement.
6. **Recover applicable permissions and authority.** For a restricted access, account change or operating decision, establish who may act, on what and under which conditions. Preserve the existing basis when current. Keep assignment, capability, responsibility, permission and authority separate. A factual observation can support a state claim without itself granting permission to alter that state or a commitment.
7. **State next decisions and permissible Work.** Name what is enabled, blocked, awaiting evidence, or returned to a specialist; include the condition and participant that can advance it.
8. **Construct participant views.** Select the smallest representation for each action. Preserve subject identity and claim correspondence; show what the view omits and where claims conflict, and provide a return to the owning account. Do not require one screen.
9. **Qualify a selected control view.** Relate its depicted observation and intervention to the actual participants, evidence and authority. Obtain stronger control claims, such as stability or rate adequacy, from their direct analysis; the picture cannot supply them.
10. **Test interruption and handoff when current.** Use `A.15.8` for the general Work or WorkPlan performance-configuration question. Ask a representative next participant to recover the bounded question, current claims, evidence, disagreements, permissions, next Work, and stop without private memory.
11. **Keep the account current for its use.** Identify the source or event that changes a relied-on claim and how affected participants will receive the update. Specify cadence, expiry, supersession or conflict handling where the claim or its use requires them. Reopen only the affected claim, view or decision.

#### OPS.4:4.2 - Maintain the Usable Account

Reuse existing specialist records and participant views. Keep the content below to the extent needed for the selected decisions, access conditions and continuing use.

| Result position | Content for the receiving use |
| --- | --- |
| use boundary | Participants, actions or decisions, horizons, first useful result, and truthful stops. |
| subjects and commitments | Exact OPS.3 subjects and direct relations; commitment parties, content, conditions, status, and authority. |
| current claims | Claim content, effective scheme, time/horizon, conditions, uncertainty, and receiving action. |
| evidence and provenance | Sources, observations/results, carriers, transformations, versions, reach, and missing evidence. |
| permissions and authority | Applicable access, account-change and operating-decision relations, with their scope and basis. |
| disagreement and gaps | Conflicting or missing claims, affected decisions, specialist returns, and non-admissible compression. |
| next decisions and Work | Enabled, blocked, awaiting, or returned actions; required condition and responsible participant. |
| participant views | Selected claims, subject correspondence, explicit scope of omitted material, conflict cues, return route, and access limits. |
| refresh and recovery | Update or expiry conditions, handoff/recovery observation when current, and smallest reopen rule. |

#### OPS.4:4.3 - What Changes in Practice

Participants stop asking whether everyone sees the same dashboard. They ask whether each participant can recover the exact subjects, claims, evidence, permissions, disagreements, and next action needed for that participant's decision. A visible conflict or honest unknown becomes a usable coordination result. A record update no longer masquerades as changed world state.

### OPS.4:5 - Archetypal Grounding — PumpWorks Current Operating Account

The weekly release decision uses a small account rather than one status board:

| Account claim | Evidence, uncertainty, and authority | Next decision or Work |
| --- | --- | --- |
| `FieldIncident-I73` may affect controller behavior at `FieldPumpInstallation-P4`. | Field-engineer report and telemetry record are current to different times; lab reproduction is absent; service-impact extent is disputed. Field service may update observations but cannot accept product safety. | Continue bounded diagnosis, obtain lab evidence, and keep release effect unresolved. |
| `ReleaseCandidate-R42` passed tests `T1–T8`; `T9` remains blocked by rig access. | Signed test results identify candidate and fixture versions; the test-rig booking is current but does not prove a completed test. Release authority remains separate. | Await exact rig access and `T9`; no release from card status. |
| `SafetyQuestion-S19` has no current specialist decision. | The issue record contains a question and evidence request, not a safety verdict. Only the named safety authority can return the needed result. | Hold the affected release use or narrow its scope under the current authority rule. |
| `ProviderChange-P8` changes model-artifact access after the current window. | Contract and technical-access records disagree on effective date. | Resolve the access relation or choose the supported incumbent route. |
| Weekly evidenced-release commitment is at risk. | Incident, test, provider, and release claims have different horizons and authority. The account displays the relation without collapsing them into one status. | Release, hold, rollback, narrow, or renegotiate only through the corresponding authority and evidence. |

The product-side control view separately represents `FieldTelemetryObserver-O4`, `DeployedController-C17`, plant `FieldPumpInstallation-P4`, `FieldModeSupervisor-S1`, and their direct relations where supported. The operating-supervision view separately represents reports from `PumpWorks-ControlServiceOps` and constraints returned by `ReleaseSupervisorTeam-S2`. The separately qualified temporal claims concern sub-second product control, minute-to-hour field observation, daily incident triage, weekly release, and slower provider change.

For a shift or model-session handoff, the next participant must recover the operating question, five subject claims above, evidence versions, unresolved conflicts, permissions, next permissible Work, and stop. If recovery requires private memory or an unrecorded chat, `A.15.8` returns the exact missing carrier, update/use relation, cue, or support condition. OPS.4 then repairs the operation-specific account claim or view.

Reopen only the affected claim when new telemetry arrives, `T9` completes, safety authority returns a decision, provider access changes, a commitment is renegotiated, or a participant view can no longer support its action.

#### OPS.4:5.1 - Recover after a late observation

At 10:10 a participant receives a field report observed at 09:00. Its stated currentness window ended at 10:00. It cannot replace a 10:05 observation merely because it arrived later. The incident lead keeps the report as evidence about 09:00, marks the present field condition unknown where no current observation exists, and asks the field owner for a refresh. T1–T8's laboratory evidence remains valid for its separate tested configuration and claim.

The next coordinator cannot open the raw field source. The handoff therefore includes the qualified claim, observation and receipt times, the source owner's reachable confirmation route and the unverified present condition. The receiver acknowledges that the live-field decision is blocked; read access to the shared document does not resolve it. If the maintained incident document already carries these facts and this handoff, it is the OPS.4 account—no parallel register is required.

### OPS.4:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| single-source-of-truth bias | One database or screen is treated as the world and final authority. | Preserve exact claims, provenance, conflicts, permissions, and receiving decisions. |
| visibility-as-alignment bias | Everyone can see the board, so coordination is assumed. | Test whether each participant can recover the next decision and disagreement. |
| consensus bias | Conflicting qualified claims are forced into one status. | Keep disagreement explicit with evidence reach and resolution condition. |
| freshness bias | The newest timestamp is assumed current for every horizon. | State claim-specific currentness and expiry for the receiving use. |
| access-authority bias | The ability to edit or view is treated as authority to decide. | Recover permission and decision authority separately. |
| representation-as-control bias | A loop or control room is treated as feedback closure or operating Method. | Recover actual relations and keep view, account, rates, and stronger claims distinct. |
| memory-repair bias | People or models are told to remember more after handoff failure. | Use A.15.8 to recover the missing state, carrier, update/use relation, cue, or support condition. |

### OPS.4:7 - Conformance Checklist

- [ ] The account begins from named participants, decisions/actions, horizons, and useful stops.
- [ ] Exact OPS.3 subjects, commitments, and direct relations remain recoverable in every relied-on view.
- [ ] Each current claim states content, scheme, time/horizon, conditions, evidence/provenance, uncertainty, and receiving action.
- [ ] Observation, prediction, plan, record, decision, and world-state claims remain distinct.
- [ ] Disagreements, missing observations, stale evidence, and specialist returns remain visible with their decision reach.
- [ ] Read, write, annotate, accept, hold, release, responsibility, capability, and authority relations are not inferred from one another.
- [ ] Next decisions and permissible Work name their enabling or blocking conditions.
- [ ] Participant views preserve subject and claim correspondence, make omitted scope and claim conflicts visible, and provide a return to the owning account.
- [ ] Any selected control view returns to the actual observation/intervention relations and to the direct support for its stronger claims.
- [ ] Participants can recover updates that affect their use; applicable expiry, supersession, conflict and recovery conditions are retained.

### OPS.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Build one dashboard for everyone.” | Start from participant actions and select claims and views for each, with correspondence and return. |
| “Green means done.” | Recover the subject state, commitment, evidence, acceptance or fulfilment result, and authority. |
| “Latest update wins.” | Apply claim-specific currentness, source reach, conflict, and supersession rules. |
| “Make everyone agree.” | Preserve qualified disagreement and name the evidence or authority needed for resolution. |
| “If it is editable, the team owns it.” | Separate access, permission, responsibility, assignment, and decision authority. |
| “The control room closes the loop.” | Recover the in-life relation sides and rate claims; treat the display as a representation. |
| “The handoff failed because attention was low.” | Identify the missing subject claim, carrier, update/use relation, cue, permission, or stop. |

### OPS.4:9 - Consequences

The pattern improves continuation across shifts, tools, teams, and interruptions without requiring one representation or consensus. It makes uncertainty and disagreement actionable and lets views change without losing subject identity.

The cost is explicit provenance, permission, conflict, and refresh maintenance. Some attractive dashboards become secondary because they cannot preserve the claim and authority distinctions needed by the decision.

### OPS.4:10 - Rationale

Shared attention is an operating achievement when participants can coordinate from qualified claims about the same subjects and commitments. That achievement is weaker than universal agreement and stronger than common visibility. A small decision-specific account preserves the distinction, while FPF continues to govern epistemes, evidence, Work-performance recovery, structures, and control claims.

### OPS.4:11 - SoTA-Echoing

The question is whether the next participant can act from a current, qualified operating account. A competent incumbent is SRE incident practice with separated responsibilities, a maintained live incident document, communications and an acknowledged handoff. [Google SRE, “Managing Incidents”](https://sre.google/sre-book/managing-incidents/) develops those mechanisms, including a usable document when the affected service cannot host it. OPS adopts this arrangement.

At PumpWorks, a good incident document can already identify I73, its commander, current actions and next handoff. When that account also distinguishes field-observation time from receipt time, laboratory evidence from current installation state, and release authority from document access, it suffices. Sections 4.1–4.3 ask for those distinctions only where they affect a recipient's action. The residual in section 5.1 is concrete: an expired field claim cannot supply the current evidence required for a live intervention, yet the laboratory results remain usable. A receiver lacking raw-source access needs an effective confirmation or an explicit blocker, not a second copy labelled current.

The extra work is qualifying the few decision-bearing claims, maintaining their different expiry conditions, and testing that the recipient can recover them. Frequent rechecking can itself consume scarce attention and delay response. Use the shortest refresh and handoff arrangement that preserves the decision, keep a qualified unknown instead of fabricating certainty, and reuse the incumbent's document and roles. If those provisions already exist, adding an OPS template would be pure maintenance burden.

FPF `C.2.1`, `A.15.8`, `A.10` and `C.27.TA` supply account, recovery, evidence and temporal distinctions. [OCEL](https://www.ocel-standard.org/specification/overview/) and object-centric methods help retain different event-object histories, but a log cannot alone establish current state. Control relations matter only for an actual observation-and-intervention question. DORA and agent-runtime sources remain bounded software-use comparisons, not a general theory of attention. Reopen this selection when a stronger existing account gives the same recoverable decisions more cheaply, or a failed handoff exposes an omitted claim, permission or source-access condition.

### OPS.4:12 - Relations

- `OPS.3` supplies exact subjects, direct relations, records, state claims, provenance, conflicts, permissions, and gaps. `OPS.2` supplies selected participant and control views plus correspondence obligations.
- `C.2.1` governs the claim-bearing account episteme; `A.10` governs evidence reliance; `A.15.8` governs the general Work/WorkPlan performance-configuration and recovery question.
- `C.30.LCA`, `B.2.5`, `C.27.TA`, `C.27`, and `A.3.3` govern the conditional control structure, relation, and rate/dynamics claims. OPS.4 retains operation-specific commitments, state, intervention, authority/evidence, and consequences.
- `OPS.5` later consumes current eligible demand, commitments, and uncertainty for admission. `OPS.6` consumes case state and permissible next Work. `OPS.15` and `OPS.18` remain separate inspectability and operating quality/reliability decisions.
- Security, privacy, law, safety, medicine, product engineering, finance, governance, and other specialists retain their evidence, permission, authority, and decision results.

### OPS.4:End
