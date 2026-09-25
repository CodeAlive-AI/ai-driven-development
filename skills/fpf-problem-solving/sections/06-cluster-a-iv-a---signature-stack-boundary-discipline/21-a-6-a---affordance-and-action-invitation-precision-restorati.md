## A.6.A - Affordance and Action-Invitation Precision Restoration (ACT-INV)

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative (Core)

**Plain-name.** Affordance and action-invitation precision restoration.

**Use this pattern when** wording such as “affords”, “invites”, “calls for” or “actionable” leaves the intended claim or question unclear: who could do what, in which situation, on what grounds, and what the reader may do with that statement.

**What goes wrong if missed.** A physical opportunity, detected cue, proposed inquiry or interface prompt is read as a capability, duty, permission or completed action. The reader acts on the wording without recovering the claim that would justify that action.

**What this buys.** A sufficient statement of the actual opportunity, prompt, claim or question, with the participants, conditions and subject rule needed for its use. An unresolved rule or fact is returned as an exact gap. An ordinary sentence can be the complete result.

**First useful move.** Recover what the speaker means in this use. Compare the live alternatives—for example, an available physical action, detection of that opportunity, an operator prompt, or a proposed inquiry. State the supported interpretation or the question that distinguishes the remaining alternatives. Apply the recovered subject rule before asserting its result.

**Not this pattern when.** If the claim and its subject are already clear, use that subject pattern directly—for example, for a Method, MethodDescription, WorkPlan, actual Work, ability, duty, gate, evidence, evaluation or publication. A sufficient existing sentence needs no further recovery note.

**Governed move.** This pattern recovers the meaning of affordance-like and action-first wording. Its interpretation menu and optional recovery note do not define one common relation kind or a durable U-kind. Any actual opportunity, relation occurrence, Method, ability or Work that the result names keeps its own subject, obtaining conditions and identity rule.

**Intent.**
Provide a reusable discipline for repairing overloaded **affordance-like and action-first** language in FPF texts.

Use **A.6.P** when the recovered content is a relation claim. Other recovered results, including an open inquiry question, go directly to their governing patterns. The recurring repair is to recover meaning, relevant participants and conditions, then express the result sufficiently for the receiving use.
Preserve an insufficiently articulated cue through `A.16.1` or publish its possible continuations through `B.4.1`. A question can become clear enough for inquiry while its answer remains unknown.
When the recovered result selects a Method for enactment, identify that independently admitted `U.Method`; a cited MethodDescription is a separate C.2.1 episteme used to identify, constrain or justify it. A proposed action or question need not invent a Method merely to become expressible. Intended Work remains a `U.WorkPlan`, and actual enactment remains dated `U.Work` with exact `enactsMethod` under **A.15**.

It allows ecological-psychology, phenomenological, active-inference, control-theoretic, interface, engineering-operations, and robotics uses to coexist **without false identity by label**.

**Placement.**
Part A > cluster **A.6 Signature Stack & Boundary Discipline** > recovery of under-specified affordance-like and action-first language, using **A.6.P** for its relation-claim branch.

**Builds on.**
A.3, A.6, A.6.B, A.6.P, A.6.REL, A.6.RSIR, A.6.S, A.6.0, A.6.5, A.2.6, A.7, A.15, E.8, E.10, F.9, F.18.

**Coordinates with.**
**C.16.Q** for evaluative-language repair; **C.2.2a, A.16, A.16.1, A.16.2, and B.4.1** for language-state chart positions, articulation and closure coordination, admissible moves, early cue classification, next-use docking, and admissible retreat when a published recovery result must be reopened; use **A.16.0** only when lineage, branch, loss, or an actual responsibility-handoff history itself must be published as an explicit trajectory account; **B.5.2.0** when the recovered result is an explanatory question or candidate inquiry; **C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** for articulation, closure, anchoring, and representation-factor facets referenced but not governed here; **A.10** and **B.3** for evidence and assurance; **B.4** and **B.5** for anomaly-driven cycles; **E.17.0**, **E.17**, and **E.18** for viewpoint reference resolution, independent view conformance, and viewpoint publication; **F.9** for Bridges and bounded-use claims; **F.9.1** for optional stance notes about those claims; **C.3.3** for kind-bridge repair when endpoint kind mismatches appear.

**E.10.ARCH relation.**
A.6.A supplies the wording-recovery method when an `E.10` or `E.10.ARCH` use leaves an affordance-like or action-first phrase ambiguous. Recover the actual claim or question and then its direct governor. Evaluative content goes to `C.16.Q`; ability, Method, Work, duty, evidence, assurance, gate and decision claims use their own patterns. Keep a recovery note only when a later reader needs the interpretation or its grounds.

**Non-goal.**
This pattern does **not** assert that physical affordances, interface affordances, social affordances, epistemic probe moves, articulation-closure moves, latent policy cues, and control opportunities are one concept.

Its job is to publish a disciplined treatment of action-first language across those traditions, using a direct contrast when that is enough and an F.9 Bridge only for an exact cross-context semantic-correspondence claim, while preventing false identity by shared language.

The recovered meaning selects the next pattern:

* where the repaired statement is primarily **evaluative**, use **C.16.Q**;
* where it is primarily about **general capability**, capability wording, method wording, or method-description wording, use **A.6.F**, A.2.2 qualified holder capability, `U.Method`, or `MethodDescription` according to the claim being made;
* where it is primarily **deontic**, apply **A.6.B**;
* where it is primarily about **scheduled or executed enactment**, use the governing **A.15** pattern family: exact `U.Method`, separate `U.MethodDescription`, intended `U.WorkPlan`, and actual `U.Work` with exact `enactsMethod` once execution has occurred. Keep any wording-recovery note separate from those objects.

### A.6.A:1 - Problem frame

FPF repeatedly encounters a predictable precision failure mode around **affordance-like and action-first** language.

Authors say:

* “this handle affords pulling”
* “the interface invites confirmation”
* “the alarm calls for rollback”
* “this discrepancy suggests probing deeper”
* “the draft is ready for formalization”
* “the model wants to brake”
* “the situation is actionable”

…but the intended meaning is actually one of several different **action-oriented families**, for example:

1. **Physical affordance** — a physical or environmental configuration offers a bodily action to an embodied agent.
2. **Interface affordance** — an operator-interface element, operator panel, alarm, or publication face presents an operator move.
3. **Social affordance** — another agent or interactional setting invites a response or coordination move.
4. **Epistemic probe move** — a problem situation invites asking, comparing, measuring, testing, or instrumenting.
5. **Closure-advance move** — a situation invites naming, rescoping, proxy declaration, or formalization.
6. **Latent policy cue** — a learned or distributed state carries an action-oriented tendency not yet locally articulated.
7. **Control opportunity** — a closed-loop state invites braking, rollback, replan, isolate, escalate, or override.

The recurrent failure modes are:

* **Site confusion.** The invitation-bearing site is unclear: physical entity, scene, interface entity, description episteme, carrier, policy state, or problem episode.
* **Enactor confusion.** It is unclear **which `U.System`, collective system, or role assignment whose holder is a `U.System`** is invited to act: human operator, robot controller, research team, review service, or named automation system.
* **Action confusion.** The candidate action is hidden behind vague language like *actionable*, *calls for*, *ready for*, *natural next step*.
* **Invitation vs obligation collapse.** A situation that merely invites an action is rewritten as if it already created a duty.
* **Invitation vs capability collapse.** A local, situated action opportunity is rewritten as if it were a general capability claim.
* **Invitation vs work collapse.** Offered action is narrated as if it had already been executed.
* **Substrate confusion.** Ecological, embodied, latent-distributed, and symbolic-local action cues are silently collapsed.
* **Bridge illusion.** Similar language across traditions is mistaken for sameness.
* **Premature closure.** An early cue is published as if it were already a committed method, gate, or policy.

### A.6.A:2 - Problem

How can FPF let authors use the communicative convenience of **affordance-like and action-first** language while preventing category errors when the language crosses:

* ecological and phenomenological discourse,
* interface and operator-facing discourse,
* active-inference and world-model discourse,
* control, monitoring, and incident-response discourse,
* robotics and embodied-AI discourse,
* epistemic exploration and problem-framing discourse?

### A.6.A:3 - Forces

* **Action speed vs auditability.** Action-first language is attractive because it is fast; that same speed makes it unsafe at boundaries.
* **Situated opportunity vs its account.** A physical opportunity can depend on the agent and environment even when no current account detects it; an information-constituted opportunity follows its own subject rule.
* **Preconceptual cue vs later articulation.** Detection, verbal articulation and the obtaining of an opportunity can have different conditions.
* **Enactor specificity vs shared discourse.** A cue may be visible to one detector yet relevant to another would-be enactor.
* **Opportunity vs obligation.** Not every invitation is a gate or commitment.
* **Option plurality vs premature scalarisation.** Several candidate actions may co-exist without an admissible total ordering.
* **Cross-tradition dialogue vs false unification.** The framework should preserve parallels without asserting identity.
* **Progressive closure.** An action cue may later become an option, then a policy hook, and only later a formal gate or work plan.

### A.6.A:4 - Solution - Recover the claim, apply its subject rule and return sufficient wording

#### A.6.A:4.0 - Trigger rule

Use A.6.A when the intended claim or question remains unclear for the receiving use. The following cues help locate that ambiguity:

* the prose uses tokens such as **affords**, **invites**, **calls for**, **actionable**, **ready for**, **ripe for**, **natural next step**, **the model wants**, **the interface tells**, **this problem asks for**;
* a boundary, gate, incident note, design note, or review note uses such language for admission, selection, triage, or action guidance;
* different traditions are compared using the same action-first wording;
* a draft introduces *model affordance*, *interface affordance*, *actionable insight*, *policy invitation*, or *ready for formalization* without declared sense;
* the author intends the phrase to carry more than one of: situational action opportunity, latent cue, operator move, probe move, closure move, or control move.

#### A.6.A:4.0a - Operational repair sequence

1. **Recover the occurrence and receiving use.** Read the trigger sentence with its source context. State which interpretation, decision or action the reader needs it for.
2. **Compare the live interpretations.** Consider a physical opportunity, its detection, an operator prompt, a social response, a candidate inquiry, a proposed clarification, a learned policy tendency or a control option. Also consider an actual evaluation, ability, commitment or Work claim when the sentence supports that reading. Use §4.3 as a menu, not a required classification.
3. **Select what the grounds support.** State the intended interpretation and why a consequential rival is excluded. If the grounds do not choose, preserve the rival meanings and return the fact or question that would distinguish them. A short note is useful when a later decision needs those grounds; it is not a prerequisite to every repair.
4. **Recover the subject and relevant conditions.** Name the actual site, would-be actor, action and other participants only to the extent that they determine the claim. For an obtaining relation, recover its direct predicate and any needed occurrence identity under A.6.REL. For an inquiry, state the question and what an answer would resolve. A menu label supplies neither result.
5. **Express the first useful result.** Return a sufficient ordinary sentence, supported bounded claim, explicit question or exact missing basis. Use one of §4.5's optional forms only when the receiving use needs it. Separate a detector, viewpoint, source or representation when that distinction changes the result.
6. **Continue from that result.** Apply the subject pattern for a needed evaluation, Method selection, WorkPlan, actual Work, authority, gate or evidence claim. Use A.6.B for the actual boundary-bearing claim. Stop when the receiving question is answered; wording recovery creates no extra invitation occurrence to establish first.

#### A.6.A:4.1 - Recognition and assurance answer different questions

The first result is recognition of what the sentence means. Establishing the recovered claim then uses that subject's rule and evidence. An intelligible physical-opportunity claim can still lack support; an intelligible research question can be useful while its answer is unknown.

Use `A.16.1` or `B.4.1` when the cue cannot yet support a particular claim or question. When articulation is sufficient, express the recoverable content without requiring a relation record or a sense token. Any relevant `AE` or `CD` reading concerns the account and its next use; it does not establish a physical opportunity.

If an account later becomes unsupported, revise or withdraw it through the applicable subject pattern and A.16.2. With physical conditions fixed, changing its wording, carrier or detector establishes no beginning, ending or new occurrence of the physical opportunity. If information itself is constitutive under a source-specific relation predicate, use that predicate and its identity rule for the corresponding change.

#### A.6.A:4.1a - Optional recovery note

When a receiver needs a reusable account of the repair, a note may contain:

```text
trigger and source context
recovered statement or question
receiving use
participants and conditions that determine the result
subject rule and supporting sources, or the exact missing basis
material rival interpretations and their disposition, when needed
detector, viewpoint, representation and publication details, when relevant
next subject result or return, when one is needed
```

This is a way to express the result. It neither declares a common relation kind nor supplies an obtaining predicate. For an actual relation claim, its participants, direction, applicability, evidence requirements and same/new rule come from that relation's direct governor. Recover ref-backed participants and by-value content under A.6.5 when the note itself is changed.

Omit fields that do not change interpretation or use. A sufficient sentence remains a complete result. A particular receiving publication can require more structure under its own conditions; that requirement does not become a universal prerequisite to wording recovery.

**Viewpoint and view discipline.**
When `viewpointRef` is present, `effectiveReferenceScheme` is also explicit and the reference resolves under that scheme to one exact independently admitted `U.Viewpoint` episteme. `view` is a separate optional value: it names one independently identified C.2.1 episteme that already has `U.View` membership only because exact E.17.0 `EpistemeViewpointConformanceRelation(view, viewpoint)` obtains for at least one admitted viewpoint. The selected `viewpointRef` need not be the viewpoint to which an optional view conforms unless the record explicitly claims that relation. Including `viewpointRef` or `view` in a recovery note establishes neither `U.Viewpoint` nor `U.View` dependent-kind membership; it only cites already established objects. Detector, viewpoint selection, view membership, viewing construction and publication remain separate.

A sentence such as “X affords Y” needs repair when its intended action, participants or basis remain hidden for the receiving use. For a recovered relation claim, apply A.6.REL; for a recovered question, preserve the question. Earlier cue content may remain a cue pack, RoutedCueSet or another appropriate expression.

**Interpretation and enactment.**
The menu label records a candidate reading of the wording. It does not identify an occurrence or establish that different interpretations have one relation kind. A proposed action is not an actual `U.Work` or a `U.WorkPlan`. When the result selects a Method for enactment, name the exact independently admitted `U.Method`; any `methodDescriptionRef` remains a separate source episteme. Use **A.15.2** for intended-work planning and **A.15.1** for actual Work. Route an already returned result or Work consequence through **A.15.1 §4.6** or its direct result/measurement governor: distinguish the application result binding, returned value, any independently established evaluation Work, and a result episteme when one is needed. A Work-to-result claim needs its own declared domain predicate; a missing predicate returns the named gap while leaving an independently established application binding usable.

**A.7 boundary note.**
When the site affects interpretation, distinguish an EntityOfConcern-side participant, a Description episteme participant and any non-claim-bearing site kind. Name a participating publication face, publication form, carrier or rendering separately under A.7. An optional note may use `siteClassification` and `publicationOrCarrierParticipation` for these distinctions; ordinary wording can express them too.

**Separation note.**
`detector` and `invitedEnactor` are not synonyms.
When both matter, they SHALL be published separately.

**Enactor note.**
When the recovery result names an actual would-be enactor, that enactor SHALL resolve to a `U.System` or to a role assignment whose holder is a `U.System`. An episteme, description, publication face, or carrier may participate in the **site**, but not as the acting bearer.

**Episteme non-agency note.**
If the site is a Description episteme, any later enactment still occurs through carriers, acted-on systems, or both; the description itself never acts.

#### A.6.A:4.2 - Candidate interpretations

The `ActionInvitationSense` menu in §4.3 is a discovery aid. Its `AIS.*` labels can help compare interpretations or preserve search terms; using a label is optional. Choosing one label does not assert one common `actionInvitation` relation or impose common obtaining and identity conditions on the listed subjects.

For a consequential interpretation, recover the source-local meaning, the participants and action it concerns, the conditions under which the claim would hold, and the result the receiving use needs. Keep an unresolved interpretation as an alternative rather than assigning a default because the sentence occurs in an ecological, interface, control or research context.

If a local practice needs a named interpretation profile, it may specify applicable sites and actors, action structure, relevant substrate, admissible evidence, forms of expression, change conditions and cross-context use. Such a profile describes that local recovery use. A relation declaration, Method or commitment still needs its own independently applicable rule.

#### A.6.A:4.2a - A.16 articulation-token relation note

A recovery note may carry `articulationHint` as a **local articulation-cue field** when the receiving use needs it.

This field is deliberately **not** a new formality progression, **not** a maturity scale, and **not** a surrogate for **F**. Its only job is to preserve local articulation and closure cues until they can be related to `A.16` move logic and the explicit `C.2.4` and `C.2.5` governing facets.

Local `articulationHint` tokens SHALL be related to `A.16` move logic and to the explicit `C.2.4` and `C.2.5` governing facets one-for-one, and A.6.A SHALL treat them as local publication cues only.
Until then, local hints SHALL NOT be thresholded, aggregated, or compared across Contexts.

#### A.6.A:4.3 - Interpretation menu
Consider these candidate meanings and any source-local alternative that can change the result. The menu helps recover a claim; it does not select its truth conditions by classification.

| `ActionInvitationSense` token | Use when the action-first phrase means…                                                     |            Possible useful form | Typical substrate                                    | Must **not** be silently collapsed into                  |
| ----------------------------- | ------------------------------------------------------------------------------------------- | -----------------------------: | ---------------------------------------------------- | -------------------------------------------------------- |
| `AIS.PhysicalAffordance`      | a physical or environmental configuration offers a bodily action to an embodied agent       |    `CuePack` or `ActionOption` | `ecological-world-coupled` or `embodied-kinesthetic` | site-participant property alone, generic capability, executed work |
| `AIS.InterfaceAffordance`     | an operator-interface element, operator panel, alarm, or publication face presents an operator move | `ActionOption` or `PolicyHook` | `symbolic-local` or `hybrid`                         | duty or commitment, execution log                           |
| `AIS.SocialAffordance`        | another agent or social situation invites a response or coordination move                   |    `CuePack` or `ActionOption` | `embodied-kinesthetic` or `hybrid`                   | role assignment itself, deontic commitment               |
| `AIS.EpistemicProbe`          | a problem situation invites asking, contrasting, measuring, testing, or instrumenting       |  `ActionOption` or `OptionSet` | `hybrid`                                             | explanatory merit, evidence claim, finished method       |
| `AIS.ClosureAdvance`          | a situation invites naming, rescoping, proxy declaration, or formalization toward closure   |                 `ActionOption` | `symbolic-local` or `hybrid`                         | Formality **F**, acceptance status, quality ascription   |
| `AIS.LatentPolicyCue`         | a learned or distributed state carries an action-oriented tendency not yet locally articulated |       `CuePack` or `OptionSet` | `latent-distributed` or `hybrid`                     | explicit rationale, control adequacy, quality claim      |
| `AIS.ControlOpportunity`      | a closed-loop state invites braking, rollback, replanning, isolation, escalation, or override |    `OptionSet` or `PolicyHook` | `hybrid`                                             | bare “model wants”, obligation, work occurrence          |

**Using the menu.**

* In **ecological and embodied** contexts, consider the physical-opportunity reading, while checking whether the claim instead concerns its perception or detection.
* In **operator-interface, alarm, or operator-panel** contexts, consider the interface-prompt and control-option readings, retaining both only when the sentence makes both claims. If the wording instead claims module interface, functional port, API, protocol, signature, interface specification, or service-access compatibility, use `A.6.RSIR`, `A.6.M`, `A.6.F`, or `A.6.0` according to the recovered EoC rather than treating the cue as an action invitation.
* In **epistemic exploration** contexts, "this suggests probing, formalizing, or reframing" can mean an inquiry question, candidate investigation or proposed clarification. Recover that result directly.
* In **learned world-model, active-inference, or policy** contexts, consider a learned policy tendency and a control option as different readings. A model state does not by itself establish a control decision, duty or performed action.
* If the sentence is chiefly about **better, worse, fit, or merit**, use **C.16.Q** instead of A.6.A.

#### A.6.A:4.4 - Recover details that change the result

Use the following questions where their answer changes the recovered meaning or its use. They are not ten fields that every sentence must populate:

1. **Site tuple and site classification.**
   Site tuple members: named EntityOfConcern, scene, interface element or front-end element, Description episteme, episode, control state, or non-claim-bearing site kind - with publication or carrier participation stated separately when live.

2. **Invited enactor tuple.**
   Which `U.System`, collective system, or role assignment whose holder is a `U.System` is invited to act.

3. **Candidate action tuple.**
   What action or inquiry the phrase concerns. If the result selects a Method for enactment, identify its exact `U.Method`; keep any MethodDescription, WorkPlan and actual Work separate under their direct rules.

4. **Intended meaning.**
   Which interpretation the context supports, and which consequential rival remains or is excluded. An `AIS.*` label is optional.

5. **Coupling frame.**
   The actual conditions and, where applicable, coupling relation on which the recovered claim depends; recover their rule rather than treating their names as proof.
   Examples: reach envelope, interface state, incident horizon, control horizon, probe pack, open issue set.

6. **Detector, viewpoint reference, and independent view.**
   Who or what detected the cue; which exact viewpoint episteme `viewpointRef` resolves to under the effective reference scheme when a viewpoint is selected; and, independently, which already-conforming `view : U.View` is cited when a view itself participates. None follows from another.

7. **Normal form and `articulationHint`.**
   Whether a particular expression form or articulation cue changes what the receiver can recover or do.

8. **Scope and time when relevant.**
   `U.Scope` and `Γ_time` SHALL be explicit when omission changes meaning.

9. **Representation substrate when relevant.**
   Especially when comparing ecological, embodied, latent-distributed, and symbolic-local treatments.

10. **Witness mode and evidence references.**
    Exemplars, sensory traces, probe notes, kinematic data, interface events, controller traces, run logs, or review notes.

#### A.6.A:4.5 - Normal-form discipline

Use a sufficient ordinary sentence first. The four forms below are optional ways to preserve cues, present a candidate, compare alternatives or refer to an existing policy. Select one only when it contributes to the receiving use; no sense token requires a default form.

**Docking note.**
Where the recovered result selects a Method for enactment, cite the existing exact `U.Method` ref. A current `U.MethodDescription` ref remains a separate C.2.1 source for identifying, constraining or justifying that Method or intended Work; existing `U.WorkPlan` and `U.Work` refs remain separate when those objects already exist. `PolicyHook` SHALL always be a hook over pre-existing gate, method, or protocol publications; it does not mint a new Method, execution, admissibility, or deontic ontology.

**ANF-1 — `CuePack`.**
Use when preserving an early or incompletely articulated cue is the useful result, including `AIS.PhysicalAffordance`, `AIS.SocialAffordance`, and many cases of `AIS.LatentPolicyCue`.

A conforming `CuePack` publishes:

* exemplar or contrast episodes, sensory traces, or probe cues,
* site conditions,
* enactor descriptor or enactor constraints,
* a small gloss set of candidate actions,
* optional ordinal urgency or salience summaries,
* explicit warning that the cue is **not yet** a commitment, a selected method, a gate, or work,
* explicit note that witness-bearing does **not** by itself make the hinted action correct, required, or selected.

**ANF-2 — `ActionOption`.**
Use when one candidate action tuple is explicit.

A conforming `ActionOption` publishes:

* one candidate action tuple,
* invited enactor and role assignment when live,
* local guard sketch,
* expected near-field effect,
* an exact `U.Method` ref when the option selects that Method for enactment, plus a separate optional `U.MethodDescription` ref or `U.WorkPlan` ref only when that independently existing object is current,
* explicit note that the option is **not yet selected**, **not yet obligatory**, and **not yet executed**.

**ANF-3 — `OptionSet`.**
Use when several candidate actions coexist.

A conforming `OptionSet` publishes:

* explicit action members,
* any local comparator, triage rule, or partial order,
* admissible incomparability if no total order is admissible,
* prohibition on hidden scalarisation.

**ANF-4 — `PolicyHook`.**
Use when the receiving use needs an explicit reference to an existing controller, gate, playbook, Method or override protocol.

A conforming `PolicyHook` publishes:

* referenced policy, method, gate, and protocol ids (pre-existing governing FPF patterns or `authoritySourceRef` named sources only),
* applicable guard or trigger conditions,
* admitted acting or maintaining System; any exact system-role kind or assignment needed by the hook's work context; the direct responsibility relation that selects that System, or the exact A.6.RCD missing governor; and any separate `authoritySourceRef` source,
* escalation or override references when relevant,
* explicit note that the hook is a **binding publication** over existing semantics, not itself a commitment, an admissibility rule, or a work occurrence.

#### A.6.A:4.6 - Separation from quality, capability, commitment, and work

A.6.A SHALL prevent the collapse of action invitation language into neighbouring families.

* A statement about **better, worse, fit, or merit** belongs to **C.16.Q**.
* A statement about **what a system can do in general** belongs to capability wording, method wording, or method-description wording under **A.6.F** and the subject pattern for the asserted capability, method, or method-description claim.
* A statement about **what must be done** belongs to **A.6.B** when the wording asserts an A-classified admissibility claim or a D-classified commitment claim.
* A statement about **what was actually done** belongs to **A.15** and exact dated `U.Work`, whose `enactsMethod` relation points to the exact `U.Method`.
* A result that selects a Method identifies that Method without becoming a plan or occurrence; any `methodDescriptionRef` remains auxiliary. A proposed action can remain a proposal without inventing its Method. A Description episteme never acts and is never what Work enacts.
* When a sentence carries both evaluative and action-oriented content, make the two claims and their respective grounds distinguishable. Use linked records only when the receiving use needs them.

Two clear clauses or sentences may suffice.

Examples:

* “This scene is good for grasping” can combine a physical-opportunity claim with an evaluation under a particular criterion. Recover each claim and its rule.
* “This alarm requires rollback” needs the actual gate or duty rule, if that is the intended claim.
* “The robot can grasp this handle” can concern ability under conditions or a situated physical opportunity. Recover which result the reader needs and apply its rule.
* “The operator clicked rollback” is work, not invitation.

#### A.6.A:4.7 - Bridge discipline across traditions

Whenever two traditions are compared using action-first language, first ask whether the comparison asserts or relies on semantic correspondence between exact senses in different semantic contexts. If it does, resolve those senses and test F.9; cite an obtaining Bridge only when its direct predicate is true, and state a separate bounded-use claim only when a proposed use is live. That claim carries the use, direction, correspondence rule, tolerated loss, and polarity. If the comparison does not assert or rely on that correspondence, use E.17.ID.CR for bounded comparative review or the exact direct relation that supplies the contrast, then stop. Add an F.9.1 stance note only as optional reader help for an already constituted bounded-use claim.

Useful stance labels include, for example:

* **`localRename`**
* **`operationalizes`**
* **`partialAnalogy`**
* **`projection`**
* **`nonEquivalent`**

Examples:

* A named comparison between `AIS.PhysicalAffordance` and `AIS.InterfaceAffordance` may remain a direct bounded contrast under E.17.ID.CR or another exact direct relation. If it asserts cross-context semantic correspondence, any bounded partial analogy needs an obtaining F.9 Bridge and a matching use claim. An optional `partialAnalogy` note helps reject identity; the label alone establishes nothing.
* `AIS.EpistemicProbe` and `AIS.ClosureAdvance` usually need the direct progression-by-closure relation that is actually claimed. If their senses cross semantic contexts, apply F.9 before adding any optional stance note.
* A named use from `AIS.LatentPolicyCue` toward `AIS.ControlOpportunity` needs F.9 only when it relies on cross-context semantic correspondence; then any operationalization or projection reading follows the obtaining Bridge and the use claim's direction, rule, and tolerated loss. Otherwise the exact direct relation must supply the proposed contrast or use.
* A robotics comparison from `AIS.PhysicalAffordance` toward `PolicyHook` may remain a direct contrast. If it relies on cross-context semantic correspondence, a projection reading requires the obtaining F.9 Bridge and a matching bounded-use claim under the controller frame; an F.9.1 note only explains that existing claim.
* Action invitation and quality ascription may co-occur, but co-occurrence is **not** identity.

#### A.6.A:4.8 - Change lexicon

When a recovery note changes, state what changed. The following verbs are useful descriptions, not a required common operation signature:

* **`publishRecovery(...)`** — publish the recovered claim, question or missing basis.
* **`withdrawRecovery(...)`** — withdraw that account.
* **`retargetSite(...)`** — change the named site in the account, applying the subject identity rule separately when an occurrence claim changes.
* **`retargetInvitedEnactor(...)`** — change the invited enactor tuple when that slot is ref-backed.
* **`reviseAction(...)`** — change the candidate action tuple by value (or split into the corresponding `retargetParticipant(...)` form if the account declares that action slot as ref-backed).
* **`reviseSense(...)`** — change the interpretation attributed to the wording; state the resulting change in the claim.
* **`reArticulate(...)`** — change the articulation cue while preserving the recovered meaning.
* **`reFrame(...)`** — change coupling frame.
* **`reGuard(...)`** — change guard sketch or hook condition.
* **`rePolicyHook(...)`** — change policy, gate, or method hook details.
* **`reView(...)`** — change detector publication, ref-backed viewpoint selection, or independent view inclusion under the declared ref-vs-value discipline. Changing `viewpointRef` does not mutate the viewpoint episteme; adding or replacing `view` does not establish E.17.0 conformance.
* **`rescope(...)`** — change `U.Scope`.
* **`retime(...)`** — change `Γ_time`.
* **`refreshWitnesses(...)`** — refresh witness bindings.
* **`changeRelationKind(...)`** — use only when an actual relation-kind claim changes under its direct governor. A different interpretation of wording need not be a change of relation kind.

These operations describe changes to the account or its publication. For any claim that the opportunity itself began, ended or became a different occurrence, apply its direct obtaining and identity rule; record declaration, withdrawal, wording and detector changes do not supply that result. A silent move from invitation to commitment, capability, or work is a breaking semantic change.

**A.6.P rewrite note.**
`retargetSite(...)` and `retargetInvitedEnactor(...)` describe participant retargeting in an account and SHALL be used only when the corresponding slots are ref-backed. `reviseAction(...)`, `reviseSense(...)`, `reArticulate(...)`, `reFrame(...)`, `reGuard(...)`, and `rePolicyHook(...)` are by-value revisions unless the account explicitly declares the corresponding slot as ref-backed, in which case the text SHALL use the matching `retargetParticipant(...)` form. This preserves A.6.5’s ref-vs-value discipline.

#### A.6.A:4.8a - Classify the recovered boundary-bearing claim

When the recovered claim is boundary-bearing, use its actual A.6.B classification:

* **L** — the rule that defines or constrains the recovered subject, including an actual relation predicate when that is the claim; applicable enactor/site discipline and the F.9/F.9.1 boundary retain their direct governors.
* **A** — admissibility conditions for the recovered result in selection, triage, automation or publication.
* **D** — a generic prescription with its exact normative episteme and applicable content, such as the rule to name the invited actor or required authority/override source. An asserted individual duty or commitment additionally needs its own obtaining basis; a generic prescription does not invent that individual occurrence.
* **E** — an exact adjudicable claim about actual Work, an evaluation or observation result, or a produced carrier’s condition under A.6.B. Cite the relevant sensory result, event, probe or log as its evidence; a list of trace or carrier references is not itself the E claim.

Do not let bare action-first language carry L-, A-, D-, or E-classified claims, admissible-use consequences, or evidence consequences by itself.

#### A.6.A:4.9 - Lexical guardrails

In **Tech prose and normative prose**:

* bare **affords, invites, calls for, actionable, ready for, ripe for, natural next step, the model wants, or the interface tells** MUST NOT appear without immediate repair;
* **actionable insight** MUST be made precise as the actual claim, candidate action, question or missing basis; use **C.16.Q** when the claim is evaluative;
* **affordance** MUST NOT be treated as a monadic property of a site participant without enactor, site, and coupling frame;
* an invitation MUST NOT be presented as if it were already a duty, gate, or work occurrence;
* a latent policy cue MUST NOT be presented as if it were already an explanation;
* `articulationHint` MUST NOT be treated as **F**, as acceptance status, or as a replacement for `A.16` grounding references;
* generic `Surface` facet tokens MUST NOT be introduced inside A.6.A; publication face, publication form, interop publication form, carrier, or rendering participation must be declared under A.7 and publication-face and publication-form discipline, not by widening the site classification;
* hidden enactor language inside adjectives such as *graspable*, *deployable*, *actionable*, *ready* SHALL be unpacked;
* quoted metalinguistic uses are allowed, but SHALL be marked as token-under-discussion.

#### A.6.A:4.10 - Elaborate only for the next use

Start with the recovered statement or question. Add participants, conditions, supporting sources, rival interpretations and expression structure only when the next use needs them. If further inquiry changes the interpretation, reopen it; elaboration is not a compulsory progression from cue to option to policy.

A move from a cue to a proposed action, from alternatives to a selection, or from a description to a Method, WorkPlan or Work claim requires that receiving subject's grounds. State the result of that move rather than silently upgrading the wording. Use §4.7 for a consequential comparison across traditions and A.6.B for an actual boundary-bearing claim.

#### A.6.A:4.10a - Continue from the recovered subject

Once the result identifies an actual authority, relation, Method, WorkPlan, Work, gate or inquiry question, continue through its direct pattern if further work is needed. A declaration-local planned-filling row is addressed through its WorkPlan. Preserve a separate recovery note only when a reader needs the interpretation or grounds; there is no common invitation occurrence to establish before continuing.

### A.6.A:5 - Archetypal Grounding

#### A.6.A:5.1 - Tell

Read an affordance-like sentence as a question about its intended meaning. The result can be an ordinary supported claim, a proposed action, an inquiry question, or an exact gap. Keep the subject conditions that make that result usable. An optional record can express the result but does not give different subjects one obtaining predicate.

#### A.6.A:5.2 - Show (System case)

**Draft:** “The alarm calls for rollback.”

**Repair A — control and incident line**

Recover the proposed use: OpsTeam_Phoenix is considering RollbackMethod_R41 on Release_R41 in ProdCluster_EU_1 during RunWindow_RW. RollbackRunbook_R41 describes that Method. AlarmBundle_AB9 exposes the cue about ServiceState_S7; AnomalyPolicy_AP7 detected it. AlertTrace_91 and ErrorBudgetSeries_4 are candidate evidence for applying IncidentPolicy_IP2 over Horizon_H15m.

The first useful statement is: “Check whether the current incident-policy guard and authority permit this team to use RollbackMethod_R41 on Release_R41 in this window; the alarm alone does not settle that question.” If the rule and facts establish a required rollback, state that independently grounded duty or gate result. Otherwise retain the proposed action or the precise missing condition. Nothing in these supplied names asserts a performed rollback.

If the receiving operational review uses `VP.OperationsControl`, resolve its `U.ViewpointRef` under `OperationsControlScheme_2026`. `OperationsRollbackView_9` remains an independently identified C.2.1 episteme and a `U.View` only if its exact E.17.0 conformance obtains. These are optional, separately established references, not additional requirements to understand the alarm sentence.

**Recognizable near misses.** A runbook reference alone does not identify the Method selected for enactment. A viewpoint field does not make a dashboard a `U.View`. The alarm, a recovery note or a `PolicyHook` does not prove duty, gate passage or performed Work.

**Repair B — ecological and robot line**

**Draft:** “This handle affords pulling.”

Recover the proposed physical claim: ServiceRobot_R2 can pull DoorHandle_17 along Axis_A1 in Window_W1 while the door is closed, under the actual reach, grip and clearance conditions described by ReachEnvelope_RE2, GripClass_G1 and ClearanceProfile_CP3. The reach description is not the physical reach condition itself. PerceptionStack_PS4 is the detector; DepthFrame_883 and ContactModelRun_17 are candidate evidence.

**Result with the supplied information.** These names identify the question but provide neither the physical obtaining predicate nor its required readings. Return: “Can R2 pull this handle along A1 in W1 under the specified grip, clearance and reach conditions? The applicable physical rule and its supported inputs are still needed.” A rule that requires sufficient contact force or a collision-free path must say so and be supported by the relevant measurements or model result. Naming G1, CP3 or a model run does not establish those conditions.

When that subject rule and the evidence support the claim, return the qualified physical statement directly. If the receiving task instead needs an executable manipulation plan and already has a suitable domain method, use its required observations and constraint representation. Reuse any adequate existing interpretation; producing another recovery note adds nothing by itself. With the same robot, grip, clearance, reach and door facts, changing PS4 can change detection without changing the physical opportunity. Changing an operator cue can likewise change what the operator notices. Withdrawing the description changes its availability; it does not close the door or remove the opportunity. A different, information-constituted relation must be assessed under its own predicate rather than inferred from this physical case.

#### A.6.A:5.3 - Show (Episteme case)

**Draft:** “This problem asks for a better question.”

**Repair A — epistemic probe line**

`ProblemFramingEpisode_PF3` is the framing account, `ResearchTeam_A` the intended inquirer and `Reviewer_A1` the detector of the problem. Keep `ExemplarPack_EP3`, `OpenIssueSet_O2`, `EpisodeNotes_3` and `CounterexampleCard_2` as its named source context.

For this worked case, take EP3 to compare detected and missed handle opportunities with the robot, grip and clearance facts fixed. O2 asks whether a changed physical opportunity or a changed detector explains the discrepancy. CounterexampleCard_2 records the same physical configuration with a different detection result. The recovered question is: “With the physical conditions held fixed, does changing PS4's detection configuration change which pulling opportunities are detected?” The counterexample motivates that inquiry; it does not already establish its answer or a general detector effect.

This question is the first useful result. If further question construction is needed, the team can select the already admitted `ContrastiveQuestioningMethod_Q2`; `ContrastiveQuestioning_Q2` is its separate MethodDescription. An explanatory prompt follows B.5.2.0 when its conditions hold. Choosing the inquiry, scheduling it and actually performing it remain separate claims. No invitation occurrence or compulsory `OptionSet` precedes the question.

**Repair B — closure-advance line**

**Draft:** “The draft is ready for formalization.”

Recover the proposed clarification: `AuthorCollective_C1` would express `DraftHypothesis_H7` using `TypedInvariantSet_V1` within `ClaimScope_G1`. `ReviewPanel_R4` points to `AmbiguityMemo_8` and `ReviewCommentSet_5` as grounds for that move.

Return the actual question: “Which unresolved claims in H7 can V1 express under G1, and which ambiguities would remain?” If the receiving rule establishes readiness, state its qualified result and the proposed action. The named memo and comments alone establish neither readiness, Formality F, acceptance nor performed formalization. A sufficient question can remain open without becoming a generic invitation record.

### A.6.A:6 - Bias-Annotation

* **Gov bias:** this pattern may tempt authors to smuggle decisions into invitation language.
  *Mitigation:* explicit A.6.B claim classification and obligation barrier.
* **Arch bias:** an interpretation menu can be mistaken for one ontology of all action-oriented claims.
  *Mitigation:* recover each subject and its rule; make the menu and recovery record optional.
* **Ontology and episteme bias:** this pattern insists on separating invitation from evaluation, capability, commitment, and work.
  *Mitigation:* first separate a direct contrast from a cross-context semantic-correspondence claim; test F.9 only for the latter, and keep any bounded-use claim and optional F.9.1 reading note separate.
* **Prag bias:** it favors enactor, site, and action explicitness, which raises authoring cost.
  *Mitigation:* stop at a sufficient sentence; recover only details that change the receiving result.
* **Did bias:** repeated rewrites make the pattern teachable, but may over-formalize early cues.
  *Mitigation:* preserve an early cue or open question without requiring a sense token, record or closed answer.

### A.6.A:7 - Conformance Checklist (CC-A.6.A)

A text or pattern conforms to A.6.A iff:

1. **CC-A.6.A-1 — Recoverable claim or question.**
   The intended claim or question and the participants and conditions needed for its use are recoverable. Apply a direct obtaining predicate when an actual relation is claimed; no common relation kind or sense token is required. An ordinary sentence may suffice, and an unresolved question may be the result.
2. **CC-A.6.A-2 — Explicit site and site-facet relation binding.**
   When the site changes the meaning, identify it; distinguish EntityOfConcern, Description episteme, publication and carrier participation where the claim depends on that distinction.

3. **CC-A.6.A-3 — Explicit invited enactor.**
   Identify the would-be enactor when the claim or question depends on it.

4. **CC-A.6.A-4 — Enactor discipline.**
   When the invited enactor is meant as the actual would-be enactor, it resolves to a `U.System` or role assignment with system holder.

5. **CC-A.6.A-5 — Recoverable action and independently identified Method when selected.**
   State the action or inquiry being discussed. If the result selects a Method for enactment, identify its exact `U.Method` and keep any MethodDescription separate. A proposed action need not invent a Method, WorkPlan or actual Work.

6. **CC-A.6.A-6 — Explicit coupling frame.**
   Recover the actual conditions or coupling relation that determine the claim, when applicable; named configuration objects alone do not establish it.

7. **CC-A.6.A-7 — Detector, viewpoint reference, and view separation.**
   When current, `detector`, ref-backed `viewpointRef`, its effective reference scheme, and independent optional `view` are not silently collapsed. The reference resolves to an exact admitted viewpoint episteme; a cited view already passes E.17.0 independently.

8. **CC-A.6.A-8 — Lawful normal form.**
   When the receiving use needs one of §4.5's forms, apply its discipline. A sufficient ordinary sentence, claim or question has no additional record requirement.

9. **CC-A.6.A-9 — Articulation-hint discipline.**
   If omission changes meaning, `articulationHint` is explicit and is not treated as **F** or as an acceptance state.

10. **CC-A.6.A-10 — No invitation-as-obligation.**
    An invitation is not silently published as a duty or gate.

11. **CC-A.6.A-11 — No invitation-as-work.**
    An invitation is not silently published as a work occurrence.

12. **CC-A.6.A-12 — No capability collapse.**
    A situated invitation is not silently rewritten as a general capability claim.

13. **CC-A.6.A-13 — No site-participant-property collapse.**
    Affordance language is not published as a monadic site-participant property when enactor, site, and coupling frame matter.

14. **CC-A.6.A-14 — No hidden scalarisation.**
    `OptionSet` publication does not introduce a hidden comparator value or ranking without an explicit comparator or policy.

15. **CC-A.6.A-15 — No silent sense rewrite.**
    State what interpretation changed and how that changes the claim or its use. The optional verbs in §4.8 can express that change.

16. **CC-A.6.A-16 — No silent relation-family switch.**
    A changed interpretation or an additional quality, ability, commitment or Work claim is made explicit under its own governor. Use a relation-kind change only when an actual relation-kind claim changes; two distinguishable sentences need no mandatory pair of records.

17. **CC-A.6.A-17 — Bridge accountability.**
    A cross-tradition comparison first states whether it asserts or relies on semantic correspondence between exact senses in different semantic contexts. If yes, it cites an obtaining F.9 Bridge only after the predicate passes and adds a matching bounded-use claim only when a proposed use is live. If no, it uses E.17.ID.CR or the exact direct relation that supplies the contrast. Any F.9.1 stance note remains optional reader help for an already constituted claim.

18. **CC-A.6.A-18 — Boundary-claim hook when needed.**
    If the recovered claim bears on admissibility, commitment, publication or automation, its applicable L, A, D or E classification and grounds are explicit.

19. **CC-A.6.A-19 — Lexical firewall.**
    Bare action-first trigger tokens are absent from Tech prose and normative prose except as quoted metalinguistic discussion.

20. **CC-A.6.A-20 — Direct semantics for an actual relation claim.**
    An obtaining relation or individuated occurrence uses its own predicate and any needed identity rule under A.6.REL. A recovery note, menu label, detector change or publication event does not supply those semantics or establish world-side change.

21. **CC-A.6.A-21 — Material alternatives remain recoverable.**
    If a different interpretation changes a decision, retain the rival and the ground that excludes it, or return the missing discriminating question. Use a separate note only when the receiving use needs one.

22. **CC-A.6.A-22 — Record inclusion grants no dependent-kind membership.**
    `viewpointRef` resolves under the effective reference scheme to an independently admitted `U.Viewpoint`; optional `view` names an independently identified episteme whose `U.View` membership follows only from exact E.17.0 conformance. Neither field nor a recovery note establishes either membership.

### A.6.A:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern                   | Symptom                                                                                     | Why it fails                                           | How to avoid or repair                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------------------------- |
| **Site-participant-property affordance** | "The site participant is actionable" with no enactor or coupling frame | collapses relationality into monadic property language | publish site, enactor, action, and coupling frame |
| **Invitation-as-obligation**   | "This calls for rollback" is treated as if rollback is already required                     | hides A-classified or D-classified claim status and accountability | recover the actual claim and apply its duty or gate rule through A.6.B |
| **Invitation-as-work**         | “The system reacted” is used where only a cue or option exists                              | confuses offer with execution                          | keep invitation separate from A.15 and `U.Work`                   |
| **MethodDescription as invited Method** | `Enact(methodDescriptionRef=Runbook)` supplies no exact Method | makes a C.2.1 episteme the world-side way of doing | select exact `methodRef -> U.Method`; keep the description auxiliary |
| **Viewpoint or view by record inclusion** | a field name or bundle row is treated as proof of `U.Viewpoint` or `U.View` | bypasses reference resolution and E.17.0 dependent-kind rules | resolve `viewpointRef` under the effective scheme and establish any view's conformance independently |
| **Capability-as-invitation**   | “The robot can do X” stands in for a situated affordance                                    | destroys local enactor and site conditions             | separate capability description from action invitation          |
| **Latent cue as explanation**  | a model tendency is narrated as if it were already an explicit rationale                    | overstates articulation and evidence                   | state the supported model tendency; use a cue pack or option set only when that form helps the receiving use     |
| **Premature automation**       | a cue without required witness records is wired directly into gates or controllers with no explicit hook `authoritySourceRef` named source or guard | creates unsafe action-to-automation coupling                         | apply the existing controller or gate rule, recover authority and evidence, and use an explicit hook when its interface requires one                |
| **ArticulationHint as F proxy**| `hook-explicit` is treated as "more formal"                                                | recreates a forbidden second formality characteristic          | keep F in C.2.3; reserve articulation and closure semantics for `A.16` |

### A.6.A:9 - Consequences

**Benefits.**
This pattern turns ambiguous action-oriented wording into a usable subject claim, question or exact gap. It preserves the distinctions needed for embodied, ecological, learned-policy, interface and control uses while avoiding a compulsory intermediate record.

It also complements C.16.Q cleanly: C.16.Q repairs **evaluative** ambiguity, while A.6.A repairs **action-inviting** ambiguity.

**Trade-offs and mitigations.**
The pattern adds authoring overhead and can feel heavy in early exploration.

Mitigation: allow bare action-first language in Plain exploratory notes, but require repair before it enters Tech prose, normative prose, boundary, automation, assurance, or publication use.

### A.6.A:10 - Rationale

Physical opportunities, their detection, operator prompts and inquiry questions can share an action-oriented sentence shape while having different obtaining and identity conditions. Recovering their meaning is a reusable method; their common grammar does not supply a common relation kind.

A universal invitation record would add an intermediate object whose truth conditions the menu cannot establish. A complete sum of independently specified relation kinds could serve a particular receiver, but it would require those actual predicates, identity rules and a receiving use. Wording recovery can usually stop earlier, at the supported subject claim or question. This reduces representation work while preserving consequential distinctions.

Use `C.16.Q` for an evaluative repair, `A.6.B` for the actual boundary-bearing claim, `A.15` for Method/Work distinctions and `A.16` for a needed account transition. `C.2.3` remains the direct governor of Formality F. A physical-opportunity statement, an open inquiry and a policy decision need not pass through the same intermediate relation.

### A.6.A:11 - SoTA-Echoing — choose wording recovery or a domain form by the receiving task

**Practice question.** For §5.2's “This handle affords pulling,” should the receiver first recover the supported claim or directly produce a domain-specific action representation? The selected answer for ambiguous documentation is §4.0a's six-step recovery, stopping at the useful statement, inquiry or missing basis. The serious alternative is to apply the source's established interpretation and manipulation method directly. **Adopt** that shorter route when the intended meaning and receiving interface are already settled. **Reject** choosing an operational form merely because the sentence contains “affords.”

[ReKep, PMLR 270 (2025)](https://proceedings.mlr.press/v270/huang25g.html) supplies a concrete form-and-method alternative: language instructions and RGB-D observations can be converted into constraints over 3D keypoints, then used in optimization for robot actions. It is a serious alternative for an actual manipulation task, not a proposed general theory of wording. **Adapt** its explicit interface demand to the last branch in §5.2: use the representation when the receiver needs that plan and has the required inputs. Its manipulation results do not establish the truth of this pattern's handle claim or validate the six-step recovery.

Compare one author pass over the same supplied handle case and receiving question; do not compare that pass with a robot experiment or count absent observations as free inputs:

| Receiving task and available basis | Direct source-specific method or form | Recovery-first choice and accepted cost |
| --- | --- | --- |
| Explain whether the supplied R2/G1/CP3 names support pulling; the physical rule and readings are absent. | A domain expert can immediately name the missing physical grounds. Attempting a manipulation representation requires additional observations and still leaves that evidential question to its domain rule. | §5.2 returns the bounded question and missing grounds. The six steps add interpretation work for a reader who has not yet distinguished opportunity, detection and command; no speed advantage over the informed expert is claimed. |
| Produce actions from an already understood instruction, with the domain method and required observations available. | Apply the method's representation and planning procedure directly. | Reuse the established interpretation and continue to that method. Another recovery note has no required role. The ordinary sentence alone does not deliver the executable plan. |
| Explain differing detections with physical handle facts held fixed, as in §5.3. | A manipulation-command form serves a different output; a source-specific inquiry method is suitable if it preserves that question. | Return the detector question first, then use an inquiry method only if further construction is needed. This avoids silently replacing inquiry with a movement target. |

This is a **local inference** about the stated tasks, supplied information and required outputs. It motivates §4.0a steps 1/5/6, the optional forms in §4.5, and the explicit domain-method continuation in §5.2. It establishes neither a robot effect nor a measured reduction in author effort. The deliberate trade-off is some interpretive work before committing to a form, with that work omitted when an adequate interpretation already exists.

The supporting sources constrain different claims:

* **Hansen (2024), §2**, distinguishes action possibilities from obligations and allows possibilities to escape immediate perception. **Adopt** those distinctions for the physical case; his account of perception supplies no universal ontology for metaphorical invitations. ([Frontiers][1])
* **Vauclin and colleagues (2023)** review attunement and action calibration in human person-plus-object systems. **Adapt** the distinction to the question about changed detection versus changed capabilities or physical conditions. The human findings do not establish the robot case; its physical rule and evidence remain necessary. ([Springer][2])
* **Pezzulo and colleagues**, in *Neural representation in active inference*, distinguish roles of generative models in action-perception, planning and imagination. **Adapt** that distinction when recovering a model-side claim from “the model wants”; the model tendency establishes no duty, explicit rationale or performed Work. ([UCL Discovery][3])
* **MOKA (2024)** supplies a compact point-based interface between image predictions and robot manipulation. **Adopt** the principle of an intermediate form with an actual receiver. Its robot-interface use neither makes such a form compulsory for an inquiry nor provides one obtaining predicate for every invitation. ([Robotics: Science and Systems][4])

Reopen the affected recovery when a source-specific meaning or physical criterion changes the supported interpretation, when new observations answer the named gap, or when the receiver now needs an executable interface. Recompare the method if a serious alternative preserves these distinctions with less required work. A new source's date, another field in a record, or shared terminology alone changes none of those conditions.

### A.6.A:12 - Relations

* **Uses:** **A.6.P** when the recovered content is a relation claim; **A.6.REL** for its direct predicate and any needed occurrence identity.
* **Builds on:** **A.3** and **A.7** for enactor discipline and EntityOfConcern and Description-episteme plus publication and carrier separation; **A.15** for keeping invitation distinct from enactment; **A.6.B** for boundary claim classification; **E.17.0**, **E.17**, and **E.18** for viewpoint reference resolution, independent view conformance, and viewpoint publication.
* **Works alongside:** **C.16.Q** for evaluative language; the two are siblings, not substitutes.
* **Coordinates with:** **C.2.2a, A.16, A.16.1, A.16.2, and B.4.1** for language-state chart positions, admissible moves before post-threshold repair, and retreat when a published recovery result must be reopened; use **A.16.0** only when lineage, branch, loss, or an actual responsibility-handoff history itself must be published as an explicit trajectory account; **B.5.2.0** for probe-question cases that are still prompt-shaped; **C.2.LS, C.2.4, C.2.5, C.2.6, and C.2.7** for language-state facet governance.
* **Must not replace:** **C.2.3** as the single subject pattern for **F**.
* **Uses for shared naming:** **E.10, F.17, and F.18** when an interpretation label or reusable recovery designation needs a shared name.

[1]: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1388852/full "https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1388852/full"
[2]: https://link.springer.com/article/10.3758/s13423-023-02319-w "https://link.springer.com/article/10.3758/s13423-023-02319-w"
[3]: https://discovery.ucl.ac.uk/10191719/3/Friston_Neural%20representation%20in%20active%20inference.pdf "https://discovery.ucl.ac.uk/10191719/3/Friston_Neural%20representation%20in%20active%20inference.pdf"
[4]: https://roboticsconference.org/2024/program/papers/62/ "https://roboticsconference.org/2024/program/papers/62/"

#### A.6.A:12.1 - Early cues and recovered meanings
Use this method when the wording can support a useful interpretation or a question that distinguishes alternatives. Earlier cues may remain with `A.16.1` or `B.4.1`. A recovered inquiry can remain open, and a recovered physical claim can return its exact missing rule or fact.

#### A.6.A:12.2 - Continue from the recovered result
Apply `A.6.B` when the recovered claim is boundary-bearing and `A.15` when a Method, plan or performed Work question is live. Keep an alert-intervention or operator-intervention reading distinguishable from a generic interface cue when human factors, authority or the policy rule change the result. A common invitation record is not a prerequisite.

#### A.6.A:12.3 - Governance boundary
This pattern may cite an F.9 Bridge and bounded-use claim, an optional F.9.1 stance note, an A.16 articulation-state result, authority-reference fields, or language-state facet characteristics from `C.2.LS`, `C.2.4`, `C.2.5`, `C.2.6`, and `C.2.7`; it does not redefine any of them.

### A.6.A:End
