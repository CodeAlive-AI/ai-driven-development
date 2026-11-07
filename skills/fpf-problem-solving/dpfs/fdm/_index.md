# Financial Domain Modeling Principles Framework

**DocID:** `FDM` within **FPF Library**.

**Edition:** [FDM 1.0](15-fdm-sources-1---edition-record.md)

**Author:** Anatoly Levenchuk, with AI-assisted development and review

Financial Domain Modeling helps a financial practitioner, business modeler or service designer establish whose financial position a model describes, what events can change it and how a service contributes to a participant's result. Its five methods connect parties, rights and obligations, contractual flows, actual effects and service use.

# Table of Contents

**Reader entry**

| § | Publication unit | Use |
| --- | --- | --- |
| R | [Financial Domain Modeling Readme](_index.md#financial-domain-modeling-readme) | Connect service use, financial positions, conditional events and actual effects. |
| P | [Financial Domain Modeling Principles Framework Architectural Reference](_index.md#financial-domain-modeling-principles-framework-architectural-reference) | Understand the connected methods, alternatives and limits. |
| FDM.Reference:1 | [The working problem](01-fdm-reference-1---the-working-problem.md) |  |
| FDM.Reference:2 | [How the methods connect](02-fdm-reference-2---how-the-methods-connect.md) |  |
| FDM.Reference:3 | [Connect models by the financial question](03-fdm-reference-3---connect-models-by-the-financial-question.md) |  |
| FDM.Reference:4 | [Parties, resources and several useful structures](04-fdm-reference-4---parties-resources-and-several-useful-struc.md) |  |
| FDM.Reference:5 | [Practical gain, cost and evidence](05-fdm-reference-5---practical-gain-cost-and-evidence.md) |  |
| FDM.Reference:6 | [Source choices and alternatives](06-fdm-reference-6---source-choices-and-alternatives.md) |  |
| FDM.Reference:7 | [Using the connected account correctly](07-fdm-reference-7---using-the-connected-account-correctly.md) |  |
| FDM.Sources:1 | [Edition record](15-fdm-sources-1---edition-record.md) |  |
| FDM.Sources:2 | [Source locators](16-fdm-sources-2---source-locators.md) |  |
| FDM.Sources | [Financial Domain Modeling Principles Framework Sources and Edition Notes](14-financial-domain-modeling-principles-framework-sources-and-e.md) |  |

**Patterns**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| 1 | [FDM.1 - Recover the Financial Position Behind a Record](09-fdm-1---recover-the-financial-position-behind-a-record.md) | Stable | Right, duty and record; score; loan position | A.2.8 and A.2.8.PER; FDM.2 for a disputed party. |
| 2 | [FDM.2 - Choose Party and Group Boundaries for Financial Modeling](10-fdm-2---choose-party-and-group-boundaries-for-financial-mode.md) | Stable | Debtor; entity; fund; founder group; guarantee; usable cash | FDM.1 for positions; SIE.5–6 for identity and composition. |
| 3 | [FDM.3 - Derive Events and Conditional Flows from Financial Contract Terms](11-fdm-3---derive-events-and-conditional-flows-from-financial-c.md) | Stable | Principal; accrued interest; payment allocation; calendar; guarantee trigger; conditional and actual flow | FDM.1–2 for terms and parties; actual effects use FDM.4. |
| 4 | [FDM.4 - Establish What a Financial Action Changed](12-fdm-4---establish-what-a-financial-action-changed.md) | Stable | Approval; instruction; posting; payment; effect; residual obligation | FDM.1–3; applicable institutional rule and event evidence. |
| 5 | [FDM.5 - Trace a Financial Service to a Participant's Result](13-fdm-5---trace-a-financial-service-to-a-participant-s-result.md) | Stable | Score use; admission; financial benefit; service output | FDM.1–4 when financial meaning or effect is missing; relevant decision practice. |

# Financial Domain Modeling Readme

## Practical entries

The examples below show how the five methods connect a financial question to a usable answer. A service question may need a position or event model; a changed payment may require revising an earlier availability claim. Enter with the results already established and obtain only the missing contribution. Use the Table of Contents for a direct pattern question or a different application.

**FDM** is the reference code for this framework. In FDM.3:4.2, 3 identifies the pattern and 4.2 its section. You can ask an assisting agent to explain or apply the methods in the language of your work, without framework jargon. The cases use supplied terms and facts; actual arrangements require their applicable financial and institutional interpretation.

### FDM-E1 — A score is presented as a financial benefit

- **Situation:** A better score is reported as a benefit to a borrower, but the financial change is unclear.
- **Question:** What did the service change for this participant, and what remains unresolved?
- **First useful result or blocker:** A supported contribution to the participant's result, an unchanged financial outcome, or a missing term or event.
- **Start with:** FDM.5 for the service's use, then the position and event methods needed to establish the claimed change.
- **Stop or return:** Finish with the supported contribution. Return to the terms, event or outcome connection when its premise fails.

A scoring team has improved its output and wants to describe the benefit to a borrower. [FDM.5](13-fdm-5---trace-a-financial-service-to-a-participant-s-result.md) locates the decision that uses the score. If an established rule gives the same decision and terms for the old and new score, improved accuracy alone establishes no change in this borrower's financial outcome. That answer can finish the question. A different proposed benefit, such as less information-gathering effort, needs its own comparison.

Suppose instead that an adequately authorized decision arrangement uses the score to change a lending decision. [FDM.1](09-fdm-1---recover-the-financial-position-behind-a-record.md) identifies the resulting rights and obligations under the supplied terms; [FDM.2](10-fdm-2---choose-party-and-group-boundaries-for-financial-mode.md) resolves a disputed lender or borrower identity if necessary. The score, agreement and usable funds answer different questions about the service. An actual agreement's formation conditions determine which duties exist before funding.

The constructed loan supplies valid formation and terms under which successful funding of 100 creates a funded position with 105 due on day 30. [FDM.3](11-fdm-3---derive-events-and-conditional-flows-from-financial-c.md) derives the contractual flows for each party. [FDM.4](12-fdm-4---establish-what-a-financial-action-changed.md) determines what actually occurred and changed. If a payment of 60 is established, all 60 applies to the due amount, and no further interest or fees arise, 45 remains due. A record still showing 105 unpaid must be reconciled with that effect; the original contractual amount remains 105. If the evidence establishes only an instruction to pay 60, the reduction remains unresolved. Correct subtraction cannot settle whether payment occurred.

FDM.5 uses these effect results to explain what the service supplied. Funding can make the agreed proceeds usable even if the equipment bought with them later fails to arrive. The contribution account then identifies the failed delivery step without erasing the funding result. Whether the financed work produces a later business benefit is a further question. A wider outcome claim can therefore be narrowed while the supported service contribution is retained.

The return depends on the failure: ambiguous terms return to FDM.1 or FDM.3, a disputed occurrence to FDM.4, and an unsupported connection to the participant's result to FDM.5. An adequate existing answer can be reused at any of these points.

### FDM-E2 — A group's cash is used to justify one entity's payment

- **Situation:** A group's cash balance is used to claim that one member can pay a debt.
- **Question:** Which funds can this entity actually use by the due date?
- **First useful result or blocker:** An availability and shortfall account for the entity, or an unresolved support condition or receipt.
- **Start with:** FDM.2 for the payment boundary, then FDM.1 and FDM.3 for support terms and FDM.4 for what occurred.
- **Stop or return:** Finish when the payment question is answered; revise affected availability or support assumptions when an event or term changes.

X owes 100 on day 7 and has 20 of unrestricted cash available then, after all other receipts and obligations. Y holds 150, and the two entities share a founder. [FDM.2](10-fdm-2---choose-party-and-group-boundaries-for-financial-mode.md) distinguishes the founder-group view from X's payment question. Under these supplied facts, X has an 80 shortfall; adding the two balances does not make Y's funds available to X.

Now suppose a support arrangement requires Y to transfer 80 before day 7. FDM.1 establishes the relevant obligation and its parties; FDM.3 derives the conditions and timing that would make the support useful. If the arrangement instead guarantees payment only after X's failure and a valid demand, that is a different conditional route. It cannot be counted as an already available day-7 transfer. If the timing terms are insufficient, the model returns that unresolved condition.

FDM.4 then examines the event that would make the funds usable. A support commitment, transfer permission or sent payment instruction does not establish timely receipt. Suppose a later, adequately established transfer makes 60 usable by X before day 7 and nothing else in the supplied cash account changes. X now has 80 available and a remaining shortfall of 20. This actual result updates FDM.2's payment account and any FDM.3 scenario that assumed full support. The earlier 80 commitment and the 60 performance remain distinct.

The model can finish with that availability answer, or with the unresolved event when receipt is unknown. The responsible financial practice uses it to compare financing or payment actions. For a different portfolio-risk question, common dependence on the founder may still make the group view useful even when transfer is unavailable. Preserving that view alongside the payment account avoids replacing one question's answer with another's aggregate.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Financial Domain Modeling Principles Framework Architectural Reference

- [FDM.Reference:1 - The working problem](01-fdm-reference-1---the-working-problem.md) (8 lines)
- [FDM.Reference:2 - How the methods connect](02-fdm-reference-2---how-the-methods-connect.md) (12 lines)
- [FDM.Reference:3 - Connect models by the financial question](03-fdm-reference-3---connect-models-by-the-financial-question.md) (21 lines)
- [FDM.Reference:4 - Parties, resources and several useful structures](04-fdm-reference-4---parties-resources-and-several-useful-struc.md) (8 lines)
- [FDM.Reference:5 - Practical gain, cost and evidence](05-fdm-reference-5---practical-gain-cost-and-evidence.md) (8 lines)
- [FDM.Reference:6 - Source choices and alternatives](06-fdm-reference-6---source-choices-and-alternatives.md) (8 lines)
- [FDM.Reference:7 - Using the connected account correctly](07-fdm-reference-7---using-the-connected-account-correctly.md) (8 lines)
- [FDM.Reference:End](08-fdm-reference-end.md) (2 lines)
- [FDM.1 - Recover the Financial Position Behind a Record](09-fdm-1---recover-the-financial-position-behind-a-record.md) (135 lines)
- [FDM.2 - Choose Party and Group Boundaries for Financial Modeling](10-fdm-2---choose-party-and-group-boundaries-for-financial-mode.md) (150 lines)
- [FDM.3 - Derive Events and Conditional Flows from Financial Contract Terms](11-fdm-3---derive-events-and-conditional-flows-from-financial-c.md) (226 lines)
- [FDM.4 - Establish What a Financial Action Changed](12-fdm-4---establish-what-a-financial-action-changed.md) (150 lines)
- [FDM.5 - Trace a Financial Service to a Participant's Result](13-fdm-5---trace-a-financial-service-to-a-participant-s-result.md) (140 lines)

### Financial Domain Modeling Principles Framework Sources and Edition Notes

- [Financial Domain Modeling Principles Framework Sources and Edition Notes](14-financial-domain-modeling-principles-framework-sources-and-e.md) (6 lines)
- [FDM.Sources:1 - Edition record](15-fdm-sources-1---edition-record.md) (4 lines)
- [FDM.Sources:2 - Source locators](16-fdm-sources-2---source-locators.md) (35 lines)
- [FDM.Sources:End](17-fdm-sources-end.md) (1 lines)
