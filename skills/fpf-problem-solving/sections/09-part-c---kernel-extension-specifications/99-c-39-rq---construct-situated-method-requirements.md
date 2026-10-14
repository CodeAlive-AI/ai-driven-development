## C.39.RQ - Construct Situated Method Requirements

> **Type:** Method pattern
> **Status:** Stable

> **Primary working result:** one **situational Method-criteria result** that states the receiving Work and result, required Method contributions, performer capabilities, technical and organizational conditions, allowable variation, non-negotiable conditions, burden limits, evidence needs, and truthful acceptance or stop observations without selecting or admitting a Method. A question about one disputed criterion returns a supported recommendation to retain or change it, together with the criterion's current force and available amendment route.

### C.39.RQ:0 - Use This When

Use this pattern when a Method, an established-family or project-local grouping choice, or a proposed Method/Work/support structure may fail in the project's situation. Enter when the practical question concerns the receiving result, performer capabilities, technical or organizational conditions, variability, evidence, authority, or acceptable burden and those conditions are not yet explicit enough for individual qualification or architecture comparison.

Begin with the situation family, intended or current Work, receiving professional result, and the level of the Method decision. State the contributions that a Method or several Methods must make without preselecting which candidate supplies them. Place every resulting criterion with the Method, description, performer capability, covering Work assignment, permission relation, decision-authority relation, performed Work, decision result, support/access relation, responsibility, cultural subject, or receiving result it actually concerns.

The first useful result is a bounded set of criteria with subjects, allowed variation, evidence needs, satisfaction observations, and stops. A criterion can be ready for later use even when no candidate currently meets it. Enter also when the present question concerns the justification of a criterion itself. That use can finish with a supported requirement recommendation and the criterion's current force or amendment limit, without selecting a Method.

Do not use this pattern as a generic product-requirements template. Criteria do not identify, admit, select, qualify, or compose a Method or establish present or future fit. Product acceptance, Method identity, individual qualification, and architecture choice remain separate results.

#### C.39.RQ:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| situation family | The recurring class of receiving Work and conditions for which criteria are intended, with important variation and exclusions explicit. |
| receiving Work and result | The dated Work occurrence or intended occurrence and the professional result it must produce or preserve. They are not the Method. |
| required Method contribution | A reusable action, result, or preserved condition needed from one Method or from named Method relations, stated before assigning it to a candidate. |
| criterion subject | The actual object or relation constrained by a criterion: Method/account content, MethodDescription, performer capability, covering Work assignment, permission relation, decision-authority relation, performed Work, decision result, support/access, responsibility, cultural relation, or another domain subject. |
| performer capability | An ability needed to enact or judge a contribution. It is distinct from responsibility, access, assignment, permission, and decision authority. |
| Work assignment | A named assignment occurrence whose holder is one admitted System and whose scope and window cover specified Work. The assignment alone establishes neither permission, decision authority, performed Work, nor a decision result. |
| permission relation | An independently supported relation permitting a named System to perform a specified act within a stated subject, scope, window, and basis. It does not create an assignment, prove performance, or confer decision authority beyond that exact permission. |
| decision-authority relation | An independently supported direct relation under which a named System may issue a named decision result. Its subject, decision scope, window, basis, and evidence for reliance are explicit; assignment, performed Work, capability, responsibility, access, and acceptance need separate evidence. |
| allowable variation | A range or branch that may change while the receiving result and non-negotiable conditions remain protected. |
| burden limit | A bound on time, attention, capacity, delay, coordination, cost, or another named burden at its actual participant, scope, and window. |
| evidence need | The observation or record required before a later decision may rely on criterion satisfaction. It is not satisfaction by itself. |
| acceptance or stop observation | The observable condition under which the criterion can be passed to a later decision or must stop that route. It does not accept a Method or product by itself. |

### C.39.RQ:1 - Problem Frame

Situational Method Engineering asks practitioners to fit a way of working to its context. Engineering-design research adds useful questions about a Method's goal, procedure, rationale, framing, mindset, intended use, representation, tool, and ecosystem. A project also faces domain constraints that do not belong inside the Method: protected information, performer capability, authority, shared capacity, evidence timing, reversibility, and the acceptance conditions of the receiving result.

When these unlike claims are placed in one “method requirements” list, description content becomes a Method part, culture becomes a performer property, authority becomes skill, and product requirements become proof of Method fit. A useful criteria result keeps the connected situation visible while returning each claim to its actual subject.

### C.39.RQ:2 - Problem

A universal checklist invites premature scoring. It may reward a well-written MethodDescription even when performers lack capability, declare a Method unsuitable because a provider arrangement fails, or hide an architecture-level peak-load conflict inside an individual candidate score.

The project then appears to have objective fit criteria, but nobody can say what must change: the Method account, the description, the support System, the covering Work assignment, a permission or decision-authority relation, the Work arrangement, or the receiving result's own acceptance rule.

### C.39.RQ:3 - Forces

| Force | Tension |
| --- | --- |
| Comparability | Shared questions help compare alternatives, while different subjects need different criteria and evidence. |
| Situation specificity | Local constraints change the decision, while a one-project list may overfit and block reuse. |
| Candidate neutrality | Criteria should expose viable alternatives, while familiar candidates can be smuggled into the wording. |
| Flexibility | Professional Work must adapt, while non-negotiable safety, evidence, authority, and burden bounds must hold. |
| Clarity | Source-side content prompts reveal omissions, while they can be mistaken for universal Method parts. |
| Economy | Cheap observable stops save effort, while high-consequence claims need stronger evidence. |

### C.39.RQ:4 - Solution

C.11 governs a choice among available options, and C.11.DUA appraises a disputed demand and worthwhile inquiry. The construction here precedes that choice when the required Method contribution is still unclear: connect the desired result and actual situation to criteria on the Method, its performers and its provision without treating them as one subject.

Build criteria from the receiving situation outward. State required contributions and conditions, assign each criterion to its actual subject, preserve allowed variation, and defer every fit or selection verdict to the pattern that evaluates the relevant subject or structure. For a disputed criterion, start with its existing context and the appraisal in §4.4; build or update other criteria only where that question needs them.

Recognition is cheap: recurring Work, a changed constraint, or one plausible capability, access, authority, evidence, or burden failure is enough to expose a criterion question. Assurance is later and row-specific: the named observation, edition, and window must support satisfaction before qualification or architecture work may rely on that row.

#### C.39.RQ:4.1 - Pattern-Use Unfolding

1. **Bound the situation family.** Name representative Work, receiving result, affected subjects, decision window, recurrence expected, important variants, and ordinary exclusions. Recover the subject of each project, process, or case claim under `A.15.6`; attach a criterion to the plan, Method, Work, result, or other subject it constrains. Several accounts concern one Work only when their claims support that reading.
2. **State required contributions before candidates.** Describe the reusable actions, results, or preserved conditions that one Method or named Method relations must contribute. Do not write a familiar candidate's current procedure as the requirement unless that exact feature is independently non-negotiable.
3. **Use source prompts without importing kinds.** Ask what goal, procedure, rationale, framing, mindset, intended use, representation, tool, scope, and adaptation conditions a source makes visible. Place the answer with its actual subject. A stated mindset may be description content; an obtaining capability or cultural relation needs separate evidence.
4. **Recover conditions around enactment.** State performer capabilities, technical and organizational conditions, inputs, support/provider access, responsibility, covering Work assignments, permission and decision-authority relations, evidence timing, reversibility, and other Work or result constraints. Keep these conditions distinct from one another and from the performed Work and its decision result.
5. **Separate variation from invariants.** Name lawful branches, substitutions, timing ranges, and local adaptations. Mark non-negotiable result, safety, confidentiality, authority, or evidence conditions explicitly. If a criterion's justification is the live question, use §4.4 to appraise it while retaining its current force. An already justified criterion needs no new appraisal.
6. **Set burdens at the right level.** Attach time, attention, capacity, delay, meeting, or cost limits to a participant, Work scope, and window. Keep individual burden distinguishable from combined peak demand and burden transferred to another participant or period.
7. **Name evidence and observations.** For every decision-changing criterion, state what record or observation a later evaluation needs, its edition or window when material, and what would count as satisfied, failed, or unknown. Do not turn the requested evidence into a fit verdict.
8. **State acceptance, stop, and reopen rules.** Say when the criteria set is adequate for its next use, which missing fact stops that route, and which situation or source change requires rebuilding it. A stop may route to capability, support, authority, product, or Work redesign rather than Method selection.
9. **Return without selecting.** Publish the criteria by subject and decision level. Send individual subject questions to A.3.1.QM and combined structure questions to C.32.MWA.PP only when their own entry conditions hold.

#### C.39.RQ:4.2 - Record the Result

Use the rows that carry the present result. For a disputed criterion, retain the relevant existing context and return the recommendation described in §4.4.

| Result position | Content for the present use |
| --- | --- |
| use and situation family | Receiving Work/result, decision level, scope, window, representative variations, and exclusions. |
| required contributions | Candidate-neutral Method contributions and the result or preserved condition each must support. |
| criterion rows | Criterion ID, actual subject/relation, requirement or bound, allowed variation, non-negotiable status, and decision level. |
| capability, assignment, permission, and authority | Required performer capabilities; separate responsibility and access conditions; covering Work assignments; permission and direct decision-authority relations; and evidence for each. |
| technical and organizational conditions | Inputs, support/provider conditions, evidence timing, reversibility, coordination, and other situated constraints. |
| burden limits | Participant, Work scope, time window, bound, measurement basis, and transferred-burden warning. |
| evidence and disposition | Required observation or record and the condition for `satisfied`, `failed`, or `unknown` in later use, without a fit or selection verdict. |
| disputed requirement, when this question is live | Supported retention or change recommendation, the protection and burden that justify it, current force, and the available amendment route or limit needed by its recipient. |
| stop and reopen | Missing fact or failed non-negotiable that stops a route, adequate-next-use condition, and situation/source change that reopens the set. |

#### C.39.RQ:4.3 - What Changes in Practice

Teams stop asking whether a methodology “fits the context” as one opaque question. They can see whether the live issue is a Method contribution, a description gap, missing capability, covering assignment, permission, decision authority, provider access, Work timing, receiving-result condition, or combined burden. Later qualification and architecture comparison receive explicit conditions instead of a precomputed winner.

#### C.39.RQ:4.4 - Appraise a Disputed Criterion

Use C.11.DUA §4.3 when the practitioner needs to decide whether a Method criterion or protective requirement is justified. Recover the person, system or receiving result it protects, the particular failure or exposure, the governed activity or quantity, the evidence and threshold basis, and the protection the requirement adds under these conditions. Compare that contribution with the burden, delay and displaced protective work. Use the relevant domain judgement and measurement or causal analysis where the question needs them; a label such as safety does not supply that basis.

Return supported retention, tightening, revision, replacement or removal only among meaningful alternatives. Keep the requirement's current force and the authority and time needed to change it explicit where they determine the feasible continuation. A recommendation can be complete while amendment remains unavailable. Continue under the current allowed options until the governing authority or agreement changes the requirement; if none meets the receiving need within the window, return that limitation. A later amendment does not restore an opportunity already lost.

Carry the useful reason and limit in the same criteria or recommendation result. Finish when it answers the present question at a supported strength. Choose a further study only when its obtainable result could change that answer enough to warrant the full burden.

### C.39.RQ:5 - Archetypal Grounding — EC-417 Situational Criteria

The situation family is a safety-relevant controller change combining firmware and supplier-originated harness geometry under a fixed release calendar. The intended Work produces one released change with traceable affected requirements, implementation revisions, verification results, evidence status, and human release authority. Some cases have signed supplier evidence before integration; others have only versioned provisional evidence until later. AI support may suggest trace links but may not receive confidential geometry or decide release.

Three views describe the same release Work. The project view exposes dates, allocations, and authority; the process view exposes recurring supplier-evidence, integration, verification, and release-result correspondences; the case view exposes how new evidence changes the next decision for one release. These views help find criteria. They create neither additional Work nor a Method.

Required Method contributions are stated without selecting an architecture: produce the affected hardware verification result; integrate the implementation against an explicitly versioned evidence state; produce signed supplier approval or an explicit missing-approval stop; and return release, withhold, or next-slot authorization under named human authority. Evidence reconciliation and trace review are additional candidate contributions, not pre-admitted Methods.

The alternative labels refer to [the timing and capacity comparison in C.32.MWA.PP §5.3](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#c32mwapp53---possible-future-alternatives-a-b-and-b2). In A, the team waits for signed supplier evidence before integrating the software. In B2, it integrates from a versioned provisional edition and reconciles it with signed evidence before safety closure. Most preparation of the changes between those editions goes to the supplier-configuration role, keeping the safety engineer within the peak limit. A is a choice before integration; recovery R applies when closure fails after B2 integration.

The case admits three human Systems and keeps their decision Work, assignments, permissions, authority, and results explicit:

| Admitted human System | Performed decision Work and result | Covering Work assignment | Independently obtaining permission or direct decision-authority relation |
| --- | --- | --- | --- |
| `TraceReviewer-17` | named `W-TraceAcceptReject-17` occurrences issue one accept/reject result for each AI trace suggestion | `ASG-TraceReview-17` covers that Work for EC-417 from `D-21` through `D0` | `PERM-TraceAcceptReject-17` permits subject `TraceReviewer-17` to accept or reject EC-417 AI trace suggestions in that window, on the basis of `TraceReviewCharter-17`; reliance requires a current matching entry in `DecisionRightsRegister-17` and the linked human-decision record |
| `SafetyReviewer-17` | `W-SafetyEvidenceDecision-17` issues accept/reject of the evidence conditions for B2 entry, safety closure, or recovery | `ASG-SafetyReview-17` covers that Work from `D-21` through the next authorized slot | `AUTH-SafetyEvidence-17` is the direct decision-authority relation for subject `SafetyReviewer-17`, that evidence-decision scope, and that window, on the basis of `SafetyDecisionCharter-17`; reliance requires a current matching `DecisionRightsRegister-17` entry and linked safety-decision record |
| `ReleaseDecider-17` | `W-ReleaseDecision-17` issues the branch-entry and release, withhold, or next-slot decision results | `ASG-ReleaseDecision-17` covers that Work from the `D-21` checkpoint through the next authorized slot | `AUTH-ReleaseDecision-17` is the direct decision-authority relation for subject `ReleaseDecider-17`, selection of `A` or authorization of at most three `B2` trials and the named release disposition, and that window, on the basis of `ReleaseDecisionCharter-17`; reliance requires a current matching `DecisionRightsRegister-17` entry and linked release-decision record |

Assignments, permission relations, and authority relations each need their own basis. Each performed Work occurrence and decision result also needs its own record; none is established by an assignment, permission, or authority relation alone. Responsibility, access, capability, assignment, permission, authority, performed Work, and decision result therefore remain separately testable. The AI provider is a separate System and is holder or subject of none of these assignments or relations.

| Criterion | Actual subject and decision level | Requirement, variation, and bound | Evidence needed and truthful stop |
| --- | --- | --- | --- |
| `SC-TRACE-01` | EC-417 receiving result and its requirement/implementation/verification correspondence | every affected safety requirement links to one or more named current implementation revisions and one or more named verification results; every correspondence link remains inspectable, while representation format may vary | versioned trace record; an affected requirement with no current implementation-revision link or no verification-result link is `failed` and stops safety closure |
| `SC-CONF-01` | supplier-geometry information and AI-provider access relation | confidential supplier geometry stays outside the AI provider; using no AI is allowable | access configuration and handling record; any provider exposure is `failed` and stops the AI-supported route |
| `SC-ASSIGN-01` | the three admitted human Systems, their decision Work, and `ASG-TraceReview-17`, `ASG-SafetyReview-17`, and `ASG-ReleaseDecision-17` | every performed decision-Work occurrence has a named System that matches the holder, Work scope, and window of its covering assignment | assignment and Work records; a missing assignment, holder mismatch, uncovered Work, or out-of-window occurrence is `failed` without erasing the Work occurrence |
| `SC-AUTH-01` | `PERM-TraceAcceptReject-17`, `AUTH-SafetyEvidence-17`, `AUTH-ReleaseDecision-17`, and the governed decision results | every AI suggestion receives `TraceReviewer-17` accept/reject within the permission scope; safety and release decisions remain within their named subjects, scopes, windows, and bases; the AI provider has no release authority | current matching `DecisionRightsRegister-17` entries plus linked human, safety, and release decision records; missing permission or authority, an unnamed result, an out-of-scope decision, or authority delegated to the AI provider is `failed` |
| `SC-EVID-01` | provisional and signed hardware-evidence inputs, their relation, and the safety-closure guard | provisional evidence may be used before closure only with explicit edition and uncertainty; signed evidence supersedes it for safety-closure reliance, while the provisional edition, uncertainty, earlier Work use, and relation to the later signed evidence remain traceable | version/uncertainty fields, earlier-use record, signed supplier evidence, and inspectable provisional-to-signed relation; missing signed evidence at closure stops release |
| `SC-REV-01` | integration Work and the implementation state | rollback remains possible within one hour until `D-1`; the project may choose a signed-first or provisional-first branch before entry | replayable rollback demonstration for the current toolchain; inability to restore within one hour is `failed` for an early-integration route |
| `SC-CAP-01` | hardware-verification and safety-evidence capabilities of the named performers | hardware verification and safety evidence judgment require current capability for the named controller, rig, and safety scope; capability grants neither assignment, permission, nor release authority | current capability evidence for each named performer; the separate assignment, permission, and decision-authority conditions must also hold, and missing capability stops the contribution that needs it |
| `SC-TECH-01` | PLM/CI support, pinout schema, test-rig access, and their relations to Work | the evidence version used by integration remains recoverable; required verification has a named rig/access route; equivalent tools are allowed when they preserve the same result and evidence conditions | configuration, schema-edition, and access records; an unknown input edition or unavailable verification route is `unknown` and blocks reliance |
| `SC-BURDEN-01` | safety-engineer allocation on the peak safety day | safety demand stays at or below `0.40` of an eight-hour day (`3.20 h`); burden shifted to another performer remains visible rather than disappearing | allocation and time estimate for the selected day; demand above `0.40` is `failed` for the proposed structure, not proof that any one Method is unfit |
| `SC-BOARD-01` | each joint-board Work occurrence | each board lasts at most 45 minutes; one or two boards are allowable when the evidence and burden criteria remain satisfied | calendar and actual-duration record; a planned board above 45 minutes fails the coordination-burden criterion |
| `SC-STOP-01` | `W-ReleaseDecision-17`, its covering assignment, `AUTH-ReleaseDecision-17`, and the receiving result | no release occurs without signed evidence, required verification, a covering assignment, and the direct release-decision authority relation; delay to a later authorized slot is allowable | release record citing evidence, assignment, authority relation, and decision result; any missing non-negotiable yields withhold or next-slot, not silent waiver |

The criteria leave serious alternatives open. A signed-first alternative may wait for supplier evidence; a provisional-first alternative may integrate earlier and reconcile later; preparation may sit with the safety engineer or with the supplier-configuration role. C.39.RQ does not choose among them. A later individual qualification may apply contribution, capability, access, and evidence criteria to each identified Method or candidate account. A later architecture comparison must inspect combined peak demand, timing, covering assignments, permission and decision-authority relations, provider access, and burden transfer. Passing one row or staying below `0.40` does not establish fit of the whole proposed structure.

The criteria set is adequate for its next use when every non-negotiable row has an observable test, the remaining variations are explicit, and unknowns are routed to their actual subject. It stops the current route immediately on missing signed evidence at closure, confidential geometry exposure, a missing or mismatched covering assignment, permission, or direct decision-authority relation, unavailable required capability or verification route, rollback beyond one hour for an early-integration proposal, peak safety demand above `0.40`, or a joint board above 45 minutes. Reopen when the change class, supplier information boundary, evidence timing, toolchain, performer assignment, release authority, capacity window, or receiving-result acceptance rule changes.

#### C.39.RQ:5.1 - Retain Approval and Question a Duplicate Trace Record

Consider two disputed requirements in the same release situation. The supplier's signed approval establishes which pinout the supplier endorses; the provisional file alone leaves a material possibility of implementing an unendorsed connection. That protective contribution supports retaining the approval condition for release. A cheaper trace procedure does not supply the missing supplier decision, and the present release authority still withholds release when the required approval is absent.

The other requirement is a second manual copy of every trace link. In this constructed case, the versioned authoritative trace already exposes the same links and failed correspondences to the review, and the duplicate copy adds no check or independent information. Producing it consumes time needed to inspect a changed safety requirement. On those supplied facts, the criteria author can finish with a recommendation to remove the duplicate-copy obligation while preserving the trace and review that detect the actual defect. A different case in which the second check detects a consequential omission can support retention.

The recommendation names the governing trace-record rule and the authority needed to amend it. It does not treat the release decider's authority as authority to change that rule. If timely amendment is unavailable, the current rule remains in force and the release arrangement must use a permissible continuation or a later slot. The present recommendation and its limit are complete; a new experiment is selected only if an obtainable result could change the appraisal enough to warrant its full burden.

### C.39.RQ:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| universal-checklist bias | One source model becomes the criterion set for every situation. | Use source models as prompts and build only decision-changing situated rows. |
| candidate-shaped criteria | Requirements restate the familiar candidate's current procedure. | State the contribution or protected condition before assigning a candidate. |
| description-reification bias | Goal, rationale, framing, or mindset text becomes a world-side Method part or capability fact. | Place each answer with the description, account, capability, or cultural subject it actually concerns. |
| capability-assignment-authority collapse | A capable System is assumed assigned and authorized, or an authority holder is assumed capable and assigned. | Record capability, responsibility, access, assignment, permission, authority, performed Work, and decision result separately. |
| scalar-fit bias | Unlike safety, evidence, burden, and authority rows collapse into one score. | Preserve non-negotiable stops, unknowns, and decision levels. |
| local-burden blindness | A passing individual estimate hides a combined peak or burden moved to another participant. | Attach burden to participant, scope, and window; route combined structures to C.32.MWA.PP. |

### C.39.RQ:7 - Conformance Checklist

Apply these questions to the criteria being established or appraised and to the present use of the result. Existing relevant context can supply the answer.

- [ ] The criteria name a situation family, receiving Work/result, decision level, scope, window, variations, and exclusions.
- [ ] Required Method contributions are stated before candidate assignment.
- [ ] Every criterion names its actual subject or relation rather than hiding it under “method fit”.
- [ ] Method/account content, MethodDescription, performer capability, responsibility, support/access, covering Work assignment, permission relation, decision-authority relation, performed Work, decision result, culture, and receiving-result claims remain distinct.
- [ ] Capability, assignment, permission, and decision authority imply none of one another; an assignment or authority relation does not prove performed Work or its decision result.
- [ ] Allowable variation and non-negotiable conditions are explicit.
- [ ] When a criterion's justification is disputed, the recommendation compares its actual protective contribution and burden and distinguishes that judgement from current force and the feasible amendment route.
- [ ] Every burden limit names participant, Work scope, time window, bound, and measurement basis.
- [ ] Every decision-changing row names evidence and `satisfied | failed | unknown` observations.
- [ ] The result states acceptance-for-next-use, stop, and reopen conditions without selecting or admitting a Method.
- [ ] Individual and combined structure questions are routed to different later results.

### C.39.RQ:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “Our five Method Content Theory fields are the Method requirements.” | Use the five fields as source questions, then place each answer with its actual subject. |
| “The product requirement proves this Method fits.” | Keep the receiving-result condition separate and evaluate the Method contribution later. |
| “The team is experienced, so assignment, authority, and access are covered.” | Record capability, responsibility, provider access, covering assignment, permission, direct decision authority, performed Work, and decision result as separate conditions with evidence. |
| “Candidate A satisfies more criteria, so it wins.” | Preserve non-negotiable failures, unknowns, and trade-offs; use the applicable decision Method after qualification. |
| “Each Method stays within its burden, so the architecture fits.” | Compare combined peak demand, overlap, and transferred burden in C.32.MWA.PP. |

### C.39.RQ:9 - Consequences

The project obtains criteria that say what must hold and where, rather than a generic context score. Missing capability can trigger preparation, an access failure can trigger support redesign, a product stop can withhold release, and an architecture burden can remain open without blaming an individual Method.

The cost is more explicit subject placement and fewer easy rankings. Some criteria remain unknown until evidence or a candidate account is available, and a complete criteria set still makes no selection.

### C.39.RQ:10 - Rationale

A fit claim is bounded by a particular use, subject, situation, evidence basis, and time. Criteria are inputs to that later claim, not the claim itself. Returning every condition to its actual subject prevents a well-written description from standing in for capability, a provider arrangement from standing in for a Method, or one management view from standing in for the Work.

Method Content Theory and the design-method ecosystem line are complementary because they ask different source-side questions. This pattern connects situational criteria for Methods, Work, descriptions, capability, tools, culture and variants while keeping their subjects distinct. Project, process and case accounts can expose different requirements; their direct subjects determine where those requirements belong, whether the accounts concern one Work or several related subjects.

### C.39.RQ:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Daalhuizen and Cash, [Method Content Theory](https://doi.org/10.1016/j.destud.2021.101018) | Goal, procedure, rationale, framing, and mindset questions and their alignment. | Static content questions from a bounded initial population are prompts, not FPF kinds, universal criteria, capability facts, or effectiveness evidence. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Intended use, scope, representation, procedure, tool, ecosystem, and adaptation conditions. | The conceptual elements complement rather than replace Method Content Theory and FPF subject placement. |
| Tsai, Zdravkovic, and Söder, [situational Method Engineering in a digital business ecosystem](https://doi.org/10.1007/s10270-022-01068-z) | Empirical action-research evidence for situational requirements, construction, and selection in an ecosystem. | One action-research setting does not establish a universal criterion set or cross-domain fit. |
| Bender, [context-specific embedded-analytics process selection](https://doi.org/10.1007/s10257-024-00675-1) | Context-specific requirement and selection questions with practical constraints. | The application population and source-local process terms do not determine Method identity or general applicability. |
| Current FPF `A.3.1` and `A.15.6` | Method identity and applicability; project-relative subject recovery. | Criteria describe the desired contribution and conditions; they do not establish the identity of a Method or project subject. |

Reopen when a source model changes a decision-bearing prompt, a later evaluation exposes a criterion whose subject or decision level was wrong, a recurring architecture failure can be prevented by one affordable criterion, or the situation family, receiving result, variation, evidence window, performer, support, authority, or burden regime changes.

### C.39.RQ:12 - Relations

- C.39.MF or an equivalent result supplies the Method, family/local-grouping, or relation focus. C.39.RP may supply inspectable alternatives and source limits. When equivalent content already exists, C.39.MF and C.39.RP need not be applied first.
- `A.3.1` governs Method identity and applicability. C.39.RQ criteria identify or admit no Method.
- `A.15.6` supplies project-subject distinctions. When building situational criteria, distinguish the Method, Work, description, capability, tool or support arrangement, and viewpoint.
- A.3.1.QM qualifies one identified Method or candidate account against applicable rows without turning the criteria into admission or whole fit.
- C.32.MWA.PP compares combined Method, Work, allocation, support, authority, description, subject, capability, or cultural structures when several-structure relations change the decision.
- `C.11` or the applicable domain decision Method may consume later qualification and architecture results. The C.39.RQ criteria set itself selects nothing.

### C.39.RQ:End
