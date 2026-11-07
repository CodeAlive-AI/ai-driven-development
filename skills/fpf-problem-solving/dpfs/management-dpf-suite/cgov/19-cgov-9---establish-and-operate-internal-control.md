## CGOV.9 - Establish and Operate Internal Control

> **Type:** Method pattern
> **Status:** Stable

### CGOV.9:1 - Problem frame

Use this pattern when a corporation's objectives depend on controls that do not operate, leave a consequential exposure untreated, impose needless burden or give governing participants an unreliable picture of what happens.

Start from the objective and the work in which failure could arise. Select controls that address the exposure, provide the means to perform them, and examine their operation and interaction. Return the controls actually established, what is known about their functioning, and the remaining limitations or correction.

Internal control spans operations, reporting and compliance. This pattern governs their connection to corporate objectives and oversight. Particular statistical, accounting, technical or administrative operations retain their own methods. An adequate existing control can continue without redesign.

### CGOV.9:2 - Problem

A policy can require two approvals while one person controls both accounts. A reconciliation can detect a discrepancy after the recipient can no longer recover the money. A board can receive only the count of completed checks, although nobody has established that they address the exposure.

The opposite failure adds approvals to every ordinary action. Delay and diverted attention grow while the important bypass remains. The practitioner needs a control that changes what can happen or what can be detected and corrected, with a burden the corporation can sustain.

### CGOV.9:3 - Forces

Controls should improve the prospect of achieving an objective while preserving useful work. Earlier prevention may reduce exposure but impede operations; later detection can be cheaper while allowing an irreversible loss. Separation of duties can help but may exceed a small team's available capacity.

Some controls are required by applicable rules. Others are design choices. Their present force, practical effectiveness and justification are separate questions; criticizing a requirement does not amend it.

### CGOV.9:4 - Solution

Connect the objective, failure mechanism, control action and response. Then make that connection work in the corporation's actual arrangement.

#### CGOV.9:4.1 - Identify the objective and exposure

State the objective in terms that let practitioners recognize success and failure. For example, pay the entitled counterparty once, report the corporation's commitments faithfully or prevent an unauthorized release.

Follow a representative operation through its participants, information, decisions and resulting change. Identify where an error, misuse, collusion or override could defeat the objective. Use existing knowledge and incidents where they answer the question. A complete risk inventory is unnecessary before correcting a known, consequential weakness.

Retain the conditions that matter: transaction population, authority, technology, timing and the consequence of a failure. A control appropriate for a reversible small purchase may be inadequate for an irreversible large payment.

#### CGOV.9:4.2 - Choose a useful control and response

For each important exposure, determine what action would prevent it, detect it soon enough or limit and correct its consequences. Name who performs the action, what information it uses and what happens when it identifies an exception.

Compare credible alternatives, including a sufficient existing control and a narrower correction. Consider the likely reduction in exposure alongside staffing, access, delay, false alarms, displaced work and maintenance. Remove a discretionary duplicate that adds no useful protection or information.

Where duties should be separated, check the actual access and influence. Two names on a chart do not provide separation if the same person can approve both steps. When separation is impractical, identify an allowed alternative and the exposure it leaves. If an applicable rule requires separation, a cheaper alternative needs the appropriate authorized change before it can replace that requirement.

#### CGOV.9:4.3 - Establish the ability to perform it

Fit the chosen control into the work that produces the exposure. Provide the needed authority, competent participants, access, time and supporting information. Recover dependencies on software configuration or outside providers where a failure there would disable the control.

Use the actual operational method. ADM can establish entitlement, authorization and reconciliation for administrative provision; OPS.18 can manage an operating-quality or reliability problem. The corporate control question is whether those contributions address this objective together, under an accountable arrangement.

Make exception handling usable. A performer needs to know what can continue, what must be held and who may decide an unresolved case. A monitoring message without a capable recipient and response leaves the exposure untreated.

A design may be the first useful result when implementation has not been assigned. Keep it as a design. A claim that the control is established requires the necessary changes to have taken effect.

#### CGOV.9:4.4 - Examine operation and interaction

Determine whether the control works in the circumstances for which reliance is proposed. A walkthrough can reveal a missing step or access conflict. Observed executions can show whether the action was performed. Different claims require different support; one successful demonstration does not establish sustained effectiveness.

Examine combinations as well as individual steps. Does the first operation give the next one usable information? Can a person bypass both? Does the response arrive within the interval in which it can still help? Does the incentive arrangement encourage participants to hide the exception?

Reuse adequate observations and current results. Select another test only when it can change the control or the conclusion about it and warrants its burden, or when the governing requirement calls for it. Preserve unresolved exposure instead of treating absent failures as proof that the arrangement is effective.

#### CGOV.9:4.5 - Correct and return the governing result

Send a material deficiency to the participant able to correct it and to the governing recipient who needs it. Distinguish an implementation error, inadequate design, missing capability and an objective that is no longer attainable under the assumed conditions.

Apply a correction within existing authority when available. Use CGOV.11 for a corporate decision that the correction actually requires, and CGOV.14 if the governance arrangement itself must change. Routine reassignment under adequate existing powers need not become a constitutional change.

Return which controls are operating, the conditions under which they are relied on and the deficiencies that remain. Keep proposed corrections separate from completed changes. Choose follow-up by the failure and receiving decision.

### CGOV.9:5 - Archetypal Grounding

#### CGOV.9:5.1 - Two approvals that use one unverified instruction

In a constructed payment operation, a clerk can change a supplier's bank details. A second employee approves the payment but checks only the invoice amount. Both rely on the same incoming message for the new account. The identified exposure is payment to an account that the supplier did not designate.

Adding a third amount approval leaves that exposure. The selected control instead confirms a bank-detail change through a previously established supplier contact and separates that confirmation from release of the payment. The confirmer needs the established contact information and authority to hold the change; the releaser needs the confirmed result.

A walkthrough reveals that confirmation uses the new contact number entered from the same change request. The confirmer could therefore reach a destination supplied by the unverified instruction. The team restores use of the previously established supplier contact and protects its update route before relying on the control. After implementation, observed operation can support the bounded claim that this route is used.

#### CGOV.9:5.2 - Detection after the useful response window

A small organization reviews payment discrepancies monthly. A new service makes payments irreversible within hours. The existing review can still explain a past discrepancy, but its timing cannot provide the intended early containment.

The practitioner separates those uses. Retain the review where it remains useful, and compare a permitted pre-release control or timely alert and response for the irreversible exposure. If no feasible permitted response meets the needed protection, report that limitation before treating the new service as adequately controlled.

### CGOV.9:6 - Bias-Annotation

Visible paperwork can make a weak control look reliable. Recent absence of loss can make it seem unnecessary. Examine how the control changes the exposure and what the observation actually supports. Include the cost imposed on ordinary work and the possibility that several controls share the same failure.

### CGOV.9:7 - Conformance Checklist

Is the objective clear? Does the control address a specified failure mechanism? Can the assigned participants perform it and respond within the useful interval? Do the controls work together? Are design, implementation, observed operation and stronger effectiveness claims supported separately? Is the remaining burden justified?

### CGOV.9:8 - Common Anti-Patterns and How to Avoid Them

- **Completed checks stand in for controlled exposure.** Follow the control's action and consequence.
- **Several approvals repeat one unverified input.** Repair the shared source or dependence.
- **Detection is called prevention.** Compare the response time with the consequence being prevented.
- **The auditor becomes the operator of the control.** Keep management's operation and independent assessment appropriately separated.

### CGOV.9:9 - Consequences

The corporation can retain controls that help, correct specific weaknesses and remove unnecessary discretionary work. Some exposure remains because judgement, outside events, override or collusion can defeat an arrangement. A useful conclusion states that remaining limit rather than promising certainty.

### CGOV.9:10 - Architectural Rationale

A control is valuable through its effect in the work and its connection to a corporate objective. Its description and the observation of its operation play different roles. The arrangement must therefore connect control design, enabling conditions, actual execution and the governing response without using any one of them as proof of the others.

### CGOV.9:11 - SoTA-Echoing

[COSO's Internal Control—Integrated Framework, Executive Summary](https://www.coso.org/_files/ugd/3059fc_1df7d5dd38074006bce8fdf621a942cf.pdf) distinguishes design, operation and interacting components, recognizes limits on assurance and allows elimination of ineffective controls.

This method concentrates those concerns on a selected exposure and its operating response. It does not claim that the examples implement the entire COSO framework. A policy catalogue can aid discovery, while a matter-specific walkthrough exposes how the chosen control is supposed to work. Changed operations, objectives, access or failure mechanisms reopen the affected control.

### CGOV.9:12 - Relations

CGOV.3 identifies relevant powers. CGOV.4 helps design the needed governing contributions, and CGOV.8 identifies the corporate information duties that a control may need to support. CGOV.10 obtains a separately scoped audit or assurance conclusion; CGOV.13 uses material control findings in continuing oversight.

OPS.18 supplies operating-quality and reliability interventions. ADM supplies the relevant administrative operations. B.1.5.EW and CGOV.16 help recover constituent and encompassing work when a control succeeds locally but fails in its combination.

### CGOV.9:End
