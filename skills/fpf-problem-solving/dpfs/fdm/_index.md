# Financial Domain Modeling Principles Framework

**DocID:** `FDM` within **FPF Library**.

**Edition:** [FDM 1.0](15-fdm-sources-1---edition-record.md)

**Author:** Anatoly Levenchuk, with AI-assisted development and review

Use Financial Domain Modeling to establish whose financial position a model describes, which events can change it or how a service contributes to a participant’s result. Its five methods connect parties and their rights or obligations with contractual flows, actual events and the use of a service.

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

**[Financial modeling methods](_index.md#financial-modeling-methods)**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| 1 | [FDM.1 - Recover the Financial Position Behind a Record](09-fdm-1---recover-the-financial-position-behind-a-record.md) | Stable | Right, duty and record; score; loan position | A.2.8 and A.2.8.PER; FDM.2 for a disputed party. |
| 2 | [FDM.2 - Choose Party and Group Boundaries for Financial Modeling](10-fdm-2---choose-party-and-group-boundaries-for-financial-mode.md) | Stable | Debtor; entity; fund; founder group; guarantee; usable cash | FDM.1 for positions; SIE.5–6 for identity and composition. |
| 3 | [FDM.3 - Derive Events and Conditional Flows from Financial Contract Terms](11-fdm-3---derive-events-and-conditional-flows-from-financial-c.md) | Stable | Principal; accrued interest; payment allocation; calendar; guarantee trigger; conditional and actual flow | FDM.1–2 for terms and parties. Use FDM.4 to establish actual effects. |
| 4 | [FDM.4 - Establish What a Financial Action Changed](12-fdm-4---establish-what-a-financial-action-changed.md) | Stable | Approval; instruction; posting; payment; effect; residual obligation | Relevant positions, parties and terms from FDM.1–3 or existing sources. Applicable institutional rules and evidence for the event in question. |
| 5 | [FDM.5 - Trace a Financial Service to a Participant's Result](13-fdm-5---trace-a-financial-service-to-a-participant-s-result.md) | Stable | Score use; admission; financial benefit; service output | FDM.1–4 when financial meaning or effect is missing; relevant decision practice. |

# Financial Domain Modeling Readme

## Practical entries

Start with the question someone has to act on. When you are to construct the model, work from the actual request and its terms. Before using a prepared example as your model, decide what you must establish, for whom and by when. Set out your first account using the distinctions you judge necessary. For practice, you can use an open question from your work or revisit an earlier account you constructed. If an existing position or bound settles the question, give the answer and its grounds. If the request also calls for a particular payment, calculation or document, identify that deliverable. Use the Table of Contents to go directly to the method you need. The cases below illustrate choices made for two particular requests.

**FDM** is the reference code for this framework. FDM.3:4.2 identifies section 4.2 of pattern 3. An agent can explain a case or supply a model. When the choice of model belongs to you, use assistance for the work you delegate and justify the choices you make. In the two cases below the author supplies the question and much of the model. The examples stipulate their terms and facts. For an actual arrangement, use the applicable financial and institutional interpretation.

### FDM-E1 — A score is presented as a financial benefit

- **Situation:** A better score is reported as a benefit to a borrower, but the financial change is unclear.
- **Question:** What did the service change for this participant, and what remains unresolved?
- **First useful result or blocker:** A supported contribution to the participant's result, an unchanged financial outcome, or a missing term or event.
- **Start with:** FDM.5 to examine how the service was used. Use a position or event method if the claimed change depends on a question still open.
- **Stop or return:** Report the established contribution and any material limit. Reconsider a term, occurrence or link to the participant’s outcome when the conclusion depends on it.

A scoring team improves the accuracy of its output and wants to explain the benefit to a borrower. Use [FDM.5](13-fdm-5---trace-a-financial-service-to-a-participant-s-result.md) to identify how the score affects the decision. If the applicable rule gives this borrower the same decision and terms at both scores, the gain in accuracy produces no difference through that route. That can answer the question. A claim that the borrower spent less time supplying information requires its own comparison.

Suppose an authorized decision maker uses the new score and changes a lending decision. Use [FDM.1](09-fdm-1---recover-the-financial-position-behind-a-record.md) to identify any rights and obligations created under the applicable terms. If the lender’s or borrower’s identity is disputed, use [FDM.2](10-fdm-2---choose-party-and-group-boundaries-for-financial-mode.md) to resolve it. The agreement’s formation conditions determine which duties already exist before funding. To establish whether the funds are usable, follow the funding event.

In this example a valid agreement provides that successful funding of 100 creates a position with 105 due on day 30. Use [FDM.3](11-fdm-3---derive-events-and-conditional-flows-from-financial-c.md) to derive the contractual flows for each party and [FDM.4](12-fdm-4---establish-what-a-financial-action-changed.md) to determine what occurred and what it changed. Suppose 60 was paid and applied in full to the amount due, with no further interest or fees. The remaining obligation is 45. Reconcile a record showing 105 unpaid with that effect. The original contractual amount remains 105. If the evidence establishes only an instruction to pay 60, the payment and its effect remain open.

Use FDM.5 to explain what the financial service supplied. Funding may make the agreed proceeds usable even if the equipment bought with them never arrives. Report the funding and the failed delivery in their respective scopes. A later business benefit requires evidence that the financed work produced it.

For unclear terms, use FDM.1 or FDM.3. For a disputed occurrence, use FDM.4. For a gap between the service output and the participant’s result, use FDM.5. In each case, apply a sufficient existing result directly.

### FDM-E2 — A group's cash is used to justify one entity's payment

- **Situation:** A group's cash balance is used to claim that one member can pay a debt.
- Question: Can this entity meet its payment by the due date? If the recipient also needs to know which funds it can use, what gives this entity timely access to them?
- First useful result or blocker: A supported payment decision, the usable sources or amount requested, or the unresolved condition that could change the answer.
- **Start with:** FDM.2 for the payment boundary, then FDM.1 and FDM.3 for support terms and FDM.4 for what occurred. A usable lower bound can establish the debtor's ability to pay by the deadline even when the exact balance is unknown. If the holder of a common facility must choose the beneficiary in advance, consider what that holder will know then.
- Stop or return: Give the payment decision if the available funds or a sufficient bound settle it. If the recipient needs the sources or the exact amount, give those with their basis or identify what remains unresolved. Revisit a conclusion about availability or support if a relevant term or event changes.

X owes 100 on day 7 and has 20 of unrestricted cash available then, after all its other receipts and obligations. Y has 150. X and Y share a founder. Use [FDM.2](10-fdm-2---choose-party-and-group-boundaries-for-financial-mode.md) to distinguish exposure to the founder group from X’s ability to pay. On the supplied facts X is short of 80. Adding the two balances establishes no right or means for X to use Y’s cash.

Suppose Y undertakes to transfer 80 to X before day 7. Use FDM.1 to establish the obligation and its parties and FDM.3 to derive the conditions and timing of the transfer. A guarantee payable to the creditor after X fails and a valid demand is made gives the creditor a conditional recovery route. Performance of that guarantee would pay the creditor. It would not give X cash to make the original day-7 payment. If the terms leave the timing of support open, report that limit.

Use FDM.4 to examine the event that would make the funds usable. A support commitment, transfer permission or sent payment instruction can precede receipt. Suppose Y transfers 60 under its support obligation and X can use it before day 7, with nothing else in the cash account changed. X now has 80 and is short of 20. Y has performed 60 of its commitment of 80. Update X’s payment account with the confirmed receipt. If the deadline is still ahead, receiving the remaining 20 in time remains a conditional scenario until its outcome is established. Revise any conclusion inconsistent with the established events.

Return the eligibility of the sources, amount available or payment decision that the recipient requested. If receipt remains unknown, give what the available bounds establish. When a financing or payment choice is needed, the responsible party can use that result to compare its options. For portfolio risk, common dependence on the founder may matter even when X cannot use Y’s funds. Keep the group exposure distinct from the cash available to X.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Financial Domain Modeling Principles Framework Architectural Reference

- [FDM.Reference:1 - The working problem](01-fdm-reference-1---the-working-problem.md) (10 lines)
- [FDM.Reference:2 - How the methods connect](02-fdm-reference-2---how-the-methods-connect.md) (12 lines)
- [FDM.Reference:3 - Connect models by the financial question](03-fdm-reference-3---connect-models-by-the-financial-question.md) (27 lines)
- [FDM.Reference:4 - Parties, resources and several useful structures](04-fdm-reference-4---parties-resources-and-several-useful-struc.md) (12 lines)
- [FDM.Reference:5 - Practical gain, cost and evidence](05-fdm-reference-5---practical-gain-cost-and-evidence.md) (8 lines)
- [FDM.Reference:6 - Source choices and alternatives](06-fdm-reference-6---source-choices-and-alternatives.md) (8 lines)
- [FDM.Reference:7 - Using the connected account correctly](07-fdm-reference-7---using-the-connected-account-correctly.md) (10 lines)
- [FDM.Reference:End](08-fdm-reference-end.md) (2 lines)

### Financial modeling methods

- [FDM.1 - Recover the Financial Position Behind a Record](09-fdm-1---recover-the-financial-position-behind-a-record.md) (133 lines)
- [FDM.2 - Choose Party and Group Boundaries for Financial Modeling](10-fdm-2---choose-party-and-group-boundaries-for-financial-mode.md) (152 lines)
- [FDM.3 - Derive Events and Conditional Flows from Financial Contract Terms](11-fdm-3---derive-events-and-conditional-flows-from-financial-c.md) (230 lines)
- [FDM.4 - Establish What a Financial Action Changed](12-fdm-4---establish-what-a-financial-action-changed.md) (154 lines)
- [FDM.5 - Trace a Financial Service to a Participant's Result](13-fdm-5---trace-a-financial-service-to-a-participant-s-result.md) (138 lines)

### Financial Domain Modeling Principles Framework Sources and Edition Notes

- [Financial Domain Modeling Principles Framework Sources and Edition Notes](14-financial-domain-modeling-principles-framework-sources-and-e.md) (6 lines)
- [FDM.Sources:1 - Edition record](15-fdm-sources-1---edition-record.md) (4 lines)
- [FDM.Sources:2 - Source locators](16-fdm-sources-2---source-locators.md) (35 lines)
- [FDM.Sources:End](17-fdm-sources-end.md) (1 lines)
