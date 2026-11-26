## FDM.2 - Choose Party and Group Boundaries for Financial Modeling

**Type:** Architectural

**Status:** Stable


### FDM.2:0 - Use this when

Use this pattern when the boundary between companies, accounts, funds or groups could change the answer to a financial question. A founder’s portfolio and a reporting group can have different members. For a payment question, identify the party that must pay.

Identify the parties and underlying positions relevant to the question. Establish the grouping criterion, aggregate or support relation the use requires.

Use an adequate established boundary directly. A different display arrangement alone need not reopen an undisputed debtor or reporting subject.

### FDM.2:1 - Problem frame

One fund tracks investments by legal entity. Another groups startups that share founders. Both views can be useful. A common founder establishes that grouping but leaves each entity’s debts and accounts subject to its own terms.

Choose the relation for the question. To assess payment, establish the debtor’s timely usable resources. For portfolio risk, shared exposure can matter even where no entity supports another. For a consolidated report, apply its inclusion and elimination rules. Connect these views when the intended use needs more than one.

### FDM.2:2 - Problem

A convenient group key is often used as if it settled control, liability, support and resource availability together. Adding the members' balances then conceals the very restriction that changes the financial answer.

Separate-entity accounts can miss correlated exposure or an actual support arrangement. Choose a boundary that preserves the relation relevant to this question, and enough of the underlying positions to interpret the aggregate.

### FDM.2:3 - Forces

An aggregate simplifies comparison when it retains the distinctions that affect the conclusion. Check the membership or support used in the conclusion at the time the question concerns.

A relation can establish a duty or power, or support an expectation of voluntary action. State which applies. An expected transfer can inform a scenario. A claim of committed funding also needs evidence of the commitment.

### FDM.2:4 - Solution

#### FDM.2:4.1 - Start with the financial consequence being examined

Start with the consequence the recipient needs: the exposure of a group, the position of any one member, or what several holders can do under the same arrangement. A total can describe the first and leave the other two open. Hold one member's position fixed and consider a change in the other members' rights or draws. Then hold the total fixed and vary who can use it by the required time. Follow a difference down to the accounts, claims or rules that explain it. Stop at the group when its established account already answers the question.

For a payment, identify the obligor and the funds it can use by the due date. For a portfolio question, identify the investments or exposures and what their aggregation means for risk. For a report, identify the framework adopted or required for the entity and period. Use its purpose and applicable authority to select the rules. Use [SIE.5][SIE] if entity identity or continuity is disputed.

#### FDM.2:4.2 - State why these members belong together

Choose the relation that defines the group for this question, such as a common founder, control, contractual support or inclusion under a reporting rule. Establish membership at the relevant time to the extent the answer depends on it. A complete list calls for grounds for both inclusion and coverage. A supported total or restriction covering every admissible member can settle a threshold without naming them individually. A request for the list itself still calls for the list.

Different criteria can produce overlapping groups. Keep them connected when the receiving use needs them. A single hierarchy need not carry every financial relation.

#### FDM.2:4.3 - Recover what connects the positions

For a claim about support or resource availability, establish the relation that would justify it. A guarantee, committed facility, transfer permission, control relation and expected voluntary payment confer different rights or support different expectations.

Establish the parties, content, limits, conditions and timing that matter. A guarantee can give the creditor a conditional claim payable after default. It can leave the debtor without cash for the original due date. A permission allows a transfer. A commitment creates an undertaking to transfer under its terms. An actual timely transfer needs evidence of performance. Control may coexist with restrictions on the use of funds.

When a transfer is expected, state the reason for the expectation and its role in the scenario. A risk assessment can use that expectation. To include support in cash already available, establish that the debtor can use it by the relevant time.

#### FDM.2:4.4 - Build the warranted aggregate

Combine only amounts whose meaning, time, currency and inclusion rule are adequate for the receiving use. Preserve restrictions and conditional relations that can change the result.

For example, a creditor asks whether two debts of 60 each are fully covered if both default and both demands qualify. The guarantees cover qualifying principal up to their stated limits. Each debt, considered alone, fits under a limit of 80. Do the contracts grant two independent limits or must both claims draw on one limit of 80 for the period? With one limit of 80 that cannot replenish between the two demands, at least 40 of the 120 lies outside that cover, even when the demands arrive on different days. Under two independent guarantees each covering its own debt up to 80, all 120 is within cover under those conditions. An answer about one named debt may also depend on priority, allocation or which demand has already consumed the available cover. To establish what the creditor has received, use evidence of payment. For the original question about full cover the terms and the joint limit suffice.

For a reporting result, use the provisions governing consolidation, recognition, measurement or elimination, including material exceptions, or a responsible accountant’s supported treatment. If control determines a disputed boundary, establish the relevant ownership and decision rights. Apply an available qualified determination or seek one for the entity and period if the result requires it. Until then, identify which aggregate remains unresolved.

Use an established reporting boundary and treatment to identify included entities, align their accounting bases and make required adjustments. If amounts remain incompatible, explain why they have to stay separate. Use [MA.4][MA4] for account construction and reconciliation. A valuation, conversion or netting operation needs its own applicable rule.

For a disputed treatment, identify the rule or judgement that determines the operation, the parties and period it covers, and conditions that could change it. Apply a sufficient existing treatment. Establish a missing jurisdiction or reporting basis from the available authority, or obtain a determination if one is still needed.

For a payment question, derive the debtor’s usable funds at the due time after other relevant receipts and obligations. Count support from another entity according to its terms and established availability under §4.3. For a risk question, retain shared exposures and dependencies relevant to the scenarios. An exposure aggregate and a payment balance require their own meanings.

Establish that the report and the applicable restrictions admit an allocation, then test the payment over the allocations they allow. If the total and the account limits conflict, identify the incompatible premises. A separately established limit on the debtor can still decide the payment on its own grounds. If all leave the debtor enough, the balance need only be bounded. To show that the report leaves payment open, find two permitted allocations with the same report, one sufficient and one short, or show why both exist. For a shared line, include the draws that can consume the same capacity before it is restored, the authority to allocate it and the time at which the allocator learns which account needs funding. For a promise to serve any eligible payee, a reservation made before the payee is known must cover whoever can still request service. For a service target expressed as a probability, use its population and criterion. A sufficient lower bound on timely service can settle that question. To establish that a particular payment occurred use the effective settlement or other evidence for it.

#### FDM.2:4.5 - Return the boundary and its financial meaning

Return the relevant parties and the boundary, aggregate or support conclusion they justify for this question. Identify any missing identity, term, restriction, time or aggregation rule that materially limits use.

Use [SIE.6][SIE] to combine claims once their financial meanings are established. The combined account may retain several claims, a conflict, non-comparability or an unresolved premise. Use FDM.3 to derive conditional support flows and FDM.4 to establish the effect of an actual transfer when the question requires them. An established boundary may suffice on its own.

### FDM.2:5 - Archetypal Grounding

#### FDM.2:5.1 - A founder group and one debtor

Suppose X must pay 100 on day 7. It has 20 in unrestricted cash available on that date after all other receipts and obligations, before this payment. Y holds 150 in its own account. X and Y share a founder.

The founder group includes both entities and their respective balances. X’s identified cash covers 20 of the 100 due. The cash gap is 80. A timely credit facility which X can draw could cover it. To establish inability to pay, the shortfall must persist even after combining the sources X can use together by the deadline. To count Y’s money towards that payment, establish how and when it becomes usable by X.

Suppose an effective arrangement requires Y to transfer 80 to X before day 7. That establishes a support obligation. Timely performance would close the gap. To count the full 80 of support in addition to X’s own 20, establish receipt or another effective means for X to use that support by the due date.

Suppose instead the guarantee can be called only after X fails to pay. Under those terms the creditor may have a further recovery route, but payment under this guarantee would come too late to fund X’s day 7 obligation. X’s other sources may still permit timely payment. Use FDM.3 for the trigger, timing and beneficiary of the guarantee.

If Y has no support commitment but the founder is expected to arrange a voluntary transfer, keep that event in the scenario that assumes it. For a portfolio-risk question, common dependence on that founder or on the same market can justify examining the members together even when no transfer is possible.

#### FDM.2:5.2 - A reporting group and an internal amount

Suppose the reporting practitioner has established the reporting basis and period and determined that P and S are consolidated for that report. Their aligned standalone accounts include P's receivable of 40 from S and S's corresponding payable of 40. The supplied consolidation treatment eliminates that internal pair in the group view.

Keep P’s right to receive 40 and S’s obligation to pay 40 available for a question about S’s payment. Eliminating the internal amount from a consolidated report does not discharge S’s debt. If the reporting boundary is unresolved, use an existing determination or establish it from the applicable basis. Seek a qualified decision when one is required. A common founder alone does not establish the elimination.


### FDM.2:6 - Bias-Annotation

An investor may track shared founders while a reporting system uses a legal identifier. Test the chosen grouping against the financial consequence the question concerns.

Evidence of past voluntary support can inform an expectation. It does not by itself establish a present obligation or remove the possibility that support will arrive too late.

### FDM.2:7 - Conformance Checklist

Check the following for the stated use of the boundary.

1. The financial question, relevant time and scope of the parties or positions are clear. A conclusion about joint use preserves any common limit and conditions of allocation on which it depends.
2. Group membership follows an identified criterion adequate for that question.
3. Liability, control, support, permission and expected behavior remain distinct where their differences matter.
4. An aggregate retains the necessary time, currency, restrictions and applicable composition rule.
5. A claim of available funding has adequate support for timely usability, and unresolved premises remain visible.

### FDM.2:8 - Common Anti-Patterns and How to Avoid Them

**Funding X by summing X and Y.** Identify any relation and event that would make Y’s funds available to X. If none is established, keep their balances separate for X’s payment question.

**Reading a guarantee as cash in advance.** Use the actual trigger, beneficiary and payment conditions. The guarantee may answer a recovery question while leaving the immediate funding question open.

**Rejecting a useful risk group because its members are separate debtors.** Keep the debtor accounts and model the shared exposure for the risk use that needs it.

### FDM.2:9 - Consequences

Different group views can reveal shared exposure while preserving which party owes an amount and whether support is available in time. A single grouping can suffice for one of those questions.

Maintain several structures when their different uses justify the work, such as a consolidated report and a separate-entity payment account.

### FDM.2:10 - Architectural Rationale

The method begins with the consequence because there is no single group boundary that settles every financial question. It retains underlying positions so that aggregation can be interpreted and revised.

A single reporting tree is adequate when its rule and the receiving use match. Separate-entity accounts suffice for an isolated debtor question. Several connected views become useful when support, exposure and reporting differ. Their connection uses SIE's existing identity and composition methods, with the financial relations supplied here.

### FDM.2:11 - SoTA-Echoing

C.32.MWA explains how several useful structures can coexist. In a financial model, membership by founder, control or support can differ. Use SIE.5–6 when identifying the entities or composing their claims requires further work.

In §§4.1–4.4, select the boundary for the financial question, preserve the member positions and support conditions on which the requested conclusion depends. Identifying the debtor and any support relation can expose a shortfall hidden by the founder-group total. Extend the model when another material relation is needed.

[AASB 10 §19 and B86–B88][AASB10] illustrate the reporting operation. Consolidated statements on that basis require consistent accounting policies and adjustments eliminating intragroup balances. Apply the provisions that govern the report once its boundary is established. A different reporting basis calls for its own treatment.

In the X–Y example, common group membership and an obligation to provide support produce different financial conclusions. Revisit an affected conclusion when membership, support terms, restrictions, reporting basis or the receiving question changes.

### FDM.2:12 - Relations

FDM.1 supplies positions, FDM.3 their conditional flows and FDM.4 actual changes. FDM.5 uses the relevant participant boundary when examining a service result.

Use SIE.5 for an unresolved identity and SIE.6 to compose claims. Use [FPF C.32.MWA][MWA] for a financial-practice architecture question involving several structures, starting from representative performed work or a prospective case. For a disputed reporting, liability or aggregation rule, obtain the applicable accounting, legal or financial interpretation.

### FDM.2:End
