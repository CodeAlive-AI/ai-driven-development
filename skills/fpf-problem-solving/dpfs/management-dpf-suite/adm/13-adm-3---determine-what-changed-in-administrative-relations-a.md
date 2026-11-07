## ADM.3 - Determine What Changed in Administrative Relations and When It Takes Effect

**Type:** Architectural\
**Status:** Stable

### ADM.3:0 - Use this when

Use this pattern when an administrative decision depends on whether an appointment, grant, obligation or other organizational condition has begun, continues, is suspended or has ended. It also applies when a changed record is being treated as a changed relation.

The subject is the particular organizational relation or condition at the time relevant to the action. The first result states what changed, when the change matters and what that permits the handler to conclude. A missing rule or fact remains an explicit question to the person able to resolve it.

If an adequate supplied result already establishes the condition for the intended time, use it. Reconstruct a history only when another date, episode or disputed change can alter the decision.

### ADM.3:1 - Problem frame

An organization can approve an appointment before it takes effect. A directory can be updated before or after that date. A handler can learn about the appointment later still. These moments matter to different claims.

The same issue occurs with payment, delegation, cancellation and suspension. A payment instruction can exist before its effect is known. A corrected amount in a report can change what the organization claims without changing the earlier transfer. Some governing rules, however, make a particular registration or notice part of the act that changes the relation. The handler must recover that rule rather than assume that records are always constitutive or always merely descriptive.

### ADM.3:2 - Problem

How can a handler determine the organizational condition applicable to one action without turning a record date, a later discovery or an intended future change into a present fact?

The wrong time can cause premature access, an incorrect refusal or a claim that a later correction retrospectively supplied missing authority. A useful answer identifies both the relevant state and the next action warranted by the available basis.

### ADM.3:3 - Forces

Current handling needs a quick usable answer. Historical disputes may require a more precise account of what was effective and what participants could then know. A convenient latest record reduces search but can conceal future applicability or a gap between two episodes.

Time detail also has a cost. Dates, time zones and interval boundaries matter only as finely as the receiving decision requires. The governing rule determines the relevant precision; adding timestamps without identifying the changed relation creates false exactness.

### ADM.3:4 - Solution

#### ADM.3:4.1 - Fix the relation and the time of the intended use

State the condition the administrative action depends on. If the relation or participants are unclear, use ADM.2. Name the time being asked about: eligibility for a request on 25 September, a grant during a session, or an outstanding obligation after a particular payment.

Keep the time of the intended action separate from the time at which someone now examines the case. Later evidence may improve a historical account. It does not by itself change which rule or relation applied at the earlier moment.

#### ADM.3:4.2 - Recover what can make the condition change

Use the applicable rule to identify the relevant act or event and its conditions. The rule may make an authorized decision effective on a stated date, require another participant's acceptance, require a registration, or give a cancellation effect only after notice. Obtain the qualified interpretation when that requirement is unresolved.

Recover the actual case facts needed by that rule. An appointment document may be adequate evidence of its stated decision and effective date. A future plan supplies an intended change, not a completed change. An unconfirmed event remains unresolved for any conclusion that depends on it.

A.6.REL supplies the distinction between relation change and assertion or description change. Apply the direct relation's obtaining and continuity conditions; the record's location or revision date does not replace them.

#### ADM.3:4.3 - Separate the relevant times

Distinguish these times when their difference can change the next action:

| Time question | What it identifies |
| --- | --- |
| When did the relevant act or event happen? | The decision, notice, transfer or other occurrence relied on. |
| When does the relation or condition begin, change or end? | The effective boundary under the applicable rule. |
| When was the event observed or learned about? | The evidence or participant knowledge available at that moment. |
| When was the record created or corrected? | The history of the assertion or description used to represent the condition. |

This is a set of different questions, not a requirement to create four database fields. If the same supplied fact answers several of them and no distinction changes the use, say so simply. Where a deadline crosses time zones or a suspension begins within a day, recover the rule's actual time basis before judging the boundary.

#### ADM.3:4.4 - Determine whether the condition holds at the requested time

Apply the rule to the facts for the requested time. State whether the relevant condition holds, does not hold, or remains unresolved on the available basis. A supported negative result settles that condition for the stated participants, basis and time. Do not relabel it as unresolved merely because the requested action cannot proceed on that basis. Conversely, an unresolved claim is not a positive or negative finding about the relation merely because the form requires one status value.

For a later history that must distinguish episodes, use the direct same-versus-new-occurrence rule under A.6.REL. The same person and role can participate again after an earlier appointment ended. A new record alone does not establish another episode; a reused identifier alone does not establish continuity.

When only the description was corrected, update the account and retain the correction history needed for its use. A claimed cancellation, suspension or new grant requires the corresponding governing act and conditions.

#### ADM.3:4.5 - Return the effect on the actual request

Give the handler the conclusion for the relevant action and time, its decisive basis and any remaining condition. A small timeline is useful when the ordering itself explains the answer.

Return the established positive or negative result to the handler, who applies the service rule for the response or case decision it actually requires. If another basis, a disputed interpretation or an exception is a live unresolved question, name that question and the source or authorized person able to resolve it. The negative result alone does not create such a question. Correcting the account and deciding whether any earlier handling needs a remedy are separate tasks; the appropriate policy owner or decision maker supplies a remedy when the applicable conditions call for one.

This inquiry can finish with an established positive or negative result, or a precisely bounded unresolved claim. A later eligibility or transition decision is a distinct result when the actual service or change question requires one.

#### ADM.3:4.6 - What changes in practice

When a familiar operation does not give a usable temporal answer, recover how it performs the required check. [FPF B.1.5.EW][EW] helps identify that connection, its conditions and a constituent operation to learn, obtain or correct. The worked case in §5.4 applies this question to choosing and comparing dates. An understood connection can be used directly.

The handler can use a future appointment for the interval it actually covers, preserve a valid relation despite delayed recording, and distinguish a corrected report from a changed institutional condition. The next question concerns the missing rule, event or effective boundary instead of an undirected request for more documents.

### ADM.3:5 - Archetypal Grounding

#### ADM.3:5.1 - An appointment recorded before it is effective

In this constructed case, the supplied appointment rule makes an authorized appointment effective on the date stated in the decision; entry in the directory reports it. The archive's eligibility rule requires an effective appointment. The case supplies these facts:

| Local date | Fact | Consequence for the access question |
| --- | --- | --- |
| 20 September | The competent person makes Mara's appointment decision, stating an effective date of 1 October. | The decision exists; its stated appointment condition concerns the later interval. |
| 22 September | The directory is updated with that appointment and effective date. | The record is available; updating it has not advanced the stated effective date. |
| 25 September | Mara requests access for that day. | The supplied appointment does not satisfy the effective-appointment condition for this date. |
| 1 October | The appointment becomes effective under the supplied rule and facts. | It can supply the appointment condition for a later request within its scope. |

The handler returns: “This appointment begins on 1 October and does not meet the effective-appointment condition for 25 September.” With only the supplied appointment and rule, that negative result completes the temporal inquiry. The handler uses the applicable service instruction for the required response to the request. The appointment's effective date is not an unresolved question, and the temporal result does not itself replace any separately required service decision.

Now add a different fact: Mara claims a second appointment, said to begin on 20 September, but its issuing decision and scope are unavailable. The October appointment's negative result remains established. The handler asks the issuing appointment office to confirm whether the separately claimed appointment covers Mara, the relevant work and 25 September. This request concerns the missing alternative basis; it is not a mandatory further inquiry in the first case.

For a request on 2 October, the appointment condition can be adequate. A separate valid read grant and actual usable access still matter to that action. If both institutional inputs are already supplied and login fails, the provider receives the technical provision problem.

#### ADM.3:5.2 - A late record and a constitutive registration are different cases

Suppose the same appointment rule applies, but the directory is not updated until 3 October. The authorized decision and its 1 October effective date are adequately evidenced. The handler can establish the appointment condition for 2 October and correct the directory's account. The delay in recording does not move the appointment's effective date under this rule.

Now consider a different, explicitly supplied rule for a resource reservation: the reservation becomes effective only when the authorized allocation is entered into the designated registry. The case supplies an approved allocation at 12:00 and the required registration at 13:00, with all other conditions met. Before 13:00 the rule's constitutive condition is incomplete; afterward it is complete. Here registration matters because the rule assigns it that role.

The handler therefore asks what the actual rule makes effective. “The record is missing” alone cannot distinguish absent evidence, incomplete constitution and a reporting defect.

#### ADM.3:5.3 - The same participants after a gap

A history query asks whether Mara was appointed continuously through November. The supplied rule and records establish an appointment ending on 31 October and a later appointment beginning on 1 December. The same person, organization and role do not fill the November gap. The handler retains the separate intervals needed for the historical decision and obtains any different claimed basis for November instead of inferring continuity from the matching name.

#### ADM.3:5.4 - The date comparison within request examination

While examining Mara's 25 September request, the handler compares that date with the appointment's 1 October effective date. This comparison performs the temporal part of checking the required appointment condition. Through that check, the handler performs part of examining the access request. The supplied rule, Mara's appointment and the time of intended use connect those operations.

A handler might instead compare 25 September with the directory's 22 September entry. The calendar comparison can be correct while failing to answer whether the appointment condition holds. The repair is to recover which event and date the applicable rule makes decisive, then repeat the temporal check using that basis. Reuse the already adequate appointment decision. Someone who cannot make this rule-to-fact connection needs to learn that operation or obtain a qualified interpretation they can use in the check.

The reservation case in §5.2 changes the connection: its supplied rule makes registration at 13:00 decisive. Copying the appointment case's treatment of registration would now produce the wrong condition. Being able to compare times does not supply the ability to identify their institutional meaning.

These are connected descriptions of the handler's work; count that work once. A permission decision can subsequently use the temporal conclusion. The archive provider's configuration and the researcher's work with the document have their own relations to the handling; neither explains how the handler performs this check.

### ADM.3:6 - Bias-Annotation

The latest convenient record can dominate the account even when it describes a future state or was corrected late. Conversely, a participant's recollection can be treated as decisive without the applicable rule. Keep both the facts needed to determine the relation and the evidence limits needed to rely on the account.

A retrospective reader has knowledge that the original handler may not have had. Distinguish the relation that applied then from the information available then when judging the earlier action.

### ADM.3:7 - Conformance Checklist

For the requested time, examine whether:

1. The relation or condition and its participants are clear.
2. The applicable rule identifies what makes it begin, change, continue or end.
3. The relevant act or event and its effective boundary are supported or explicitly unresolved.
4. Observation and record times remain separate where they change interpretation.
5. A later correction, repeated name or reused identifier has not supplied an unsupported continuity or historical-authority claim.
6. The return states the consequence for the actual request and identifies any missing result and competent resolver.

The same result can be reused while the relation, time, governing conditions and relied-on facts remain adequate.

### ADM.3:8 - Common Anti-Patterns and How to Avoid Them

**Treating future registration as present eligibility.** A directory shows next month's appointment. Apply the effective date to the intended action.

**Assuming that every record merely reports.** A reservation rule expressly requires entry in a designated registry before the reservation is effective. Inspect that constitutive condition rather than copying an appointment example's different rule.

**Repairing history by overwriting the latest row.** A corrected report makes an earlier decision appear authorized without identifying any valid earlier basis. Preserve the difference between correcting the account and establishing what actually applied.

**Inferring continuity from the same participants.** A later appointment repeats the same person and role after a gap. Apply the relation's episode rule for the history being asked about.

### ADM.3:9 - Consequences

A time-specific answer can prevent premature action and avoid refusing a valid current relation merely because its usual record lags. It makes historical disagreement more precise: a dispute can concern the effective event, the evidence available then or a later description.

The cost is recovering the rule and enough history for the receiving decision. When that basis is missing, return the precise unresolved condition. The pattern does not create the authority to change or retrospectively validate the relation.

### ADM.3:10 - Architectural Rationale

The relation and requested time come first because they select which events and records matter. A full chronology would otherwise collect details that cannot change the action. Separate time questions become useful only when their answers differ consequentially.

Using the latest status alone is adequate when it reliably states the condition for the relevant interval and no live contrary fact remains. It is inadequate for future changes, delayed reporting or contested episodes. The additional timeline is a response to those difficulties, not a universal administrative data model.

### ADM.3:11 - SoTA-Echoing

The practice question is how to distinguish an effective organizational change from a change in what participants know or record. The selected line adopts A.6.REL's direct obtaining and continuity rules, and adapts the laboratories' relation/record distinction to administrative applicability.

One alternative is “use the latest row as the current state”. Its advantage is low handling effort. It fails when recording time is taken as effective time without the governing rule—for example, by treating a future appointment as already effective or delayed reporting as a delay in the relation itself. Under a different rule, registration can constitute the relation. Sections 4.2–4.4 and the paired registration cases retain the rule that determines which interpretation applies. The practitioner can still use an adequate latest account directly; a timeline is added only when it resolves an action-changing difference.

The May laboratory's relation/record discussion and the later ADM source pack's effective-condition distinctions supply failure reasoning and synthesis inputs. A.6.REL supplies the general method for relation change and optional occurrence identity. [FPF B.1.5.EW][EW] supplies the explanation of constituent and encompassing work applied in §5.4.

Reconsider the instruction when a governing relation uses an additional constitutive condition, when repeated episodes cannot be distinguished for the required history, or when a new record arrangement changes what evidence a handler can obtain.

### ADM.3:12 - Relations

ADM.2 supplies the relevant participants and relation when those are not already established. ADM.4 receives a source-account disagreement that remains after the time questions are explicit. ADM.1 supplies the intended administrative condition and deadline when they are unclear.

A.6.REL supplies the relation's obtaining, continuity and conditional occurrence-identity discipline. The qualified policy or relation source supplies the actual constitutive and effective conditions. The existing service instruction receives the result for the requested time; a competent decision maker receives any unresolved eligibility or remedy question.

### ADM.3:End
