## FDM.2 - Choose Party and Group Boundaries for Financial Modeling

**Type:** Architectural

**Status:** Stable


### FDM.2:0 - Use this when

Use this pattern when a financial question crosses companies, accounts, funds or groups and the chosen boundary could change the answer. A founder's portfolio and a reporting group can include different entities; identify separately which party must make the payment.

The pattern governs the party and grouping account used for a financial question. It returns identified underlying parties and positions, a grouping criterion and the aggregation or support relations warranted for that use.

Use an adequate established boundary directly. A different display arrangement alone need not reopen an undisputed debtor or reporting subject.

### FDM.2:1 - Problem frame

One fund tracks investments by individual legal entity. Another groups startups associated with the same founders. Both views can support useful work, yet a shared founder does not automatically combine their obligations or accounts.

The question determines the relevant relation. Payment feasibility concerns the debtor's timely usable resources. A portfolio analysis can concern shared exposures without any support between entities. A reporting aggregate follows its applicable inclusion and elimination rules. The model must retain these differences while allowing the useful views to connect.

### FDM.2:2 - Problem

A convenient group key is often used as if it settled control, liability, support and resource availability together. Adding the members' balances then conceals the very restriction that changes the financial answer.

Forcing every question into separate-entity accounts has a different cost: it can miss correlated exposure or an actual support arrangement. The practitioner needs the boundary warranted by this question, with enough underlying structure to prevent an aggregate from acquiring another meaning.

### FDM.2:3 - Forces

An aggregate makes comparison manageable. Its simplicity is useful only while the omitted distinctions do not change the intended conclusion. The relevant membership and support conditions can also change over time.

Some relations establish a duty or power; others support a prediction of voluntary action. Both may matter, but treating an expectation as committed funding gives the prediction an unwarranted institutional effect.

### FDM.2:4 - Solution

#### FDM.2:4.1 - Start with the financial consequence being examined

State whose payment, position, exposure, control or report is at issue and the relevant time. Identify the actual entities and accounts involved before selecting a group label.

For a payment, find the party that bears the obligation and the funds it can use by the due time. For a portfolio question, identify the investments or exposures being compared and the risk meaning of their aggregation. For a reporting result, establish the reporting framework adopted for the entity and period. The report's purpose and applicable authority select the rule family; a shared owner does not. Use [SIE.5][SIE] when the entities themselves or their continuity are disputed.

#### FDM.2:4.2 - State why these members belong together

State the question the grouping serves and its inclusion criterion. The criterion may concern a common founder, control, contractual support or inclusion in the consolidated accounts under the applicable reporting rule. Establish membership at the time relevant to that question. Preserve the underlying positions when a group view is produced.

Different criteria can produce overlapping groups. Keep them connected when the receiving use needs them. A single hierarchy need not carry every financial relation.

#### FDM.2:4.3 - Recover what connects the positions

For a proposed support or resource-availability conclusion, inspect the actual connecting relation. A guarantee, committed facility, permitted transfer, control relationship and expected voluntary payment answer different questions.

Establish the relevant parties, content, limits, conditions and timing. A guarantee can give the creditor a further conditional claim without placing cash in the primary debtor's account now. Permission to transfer does not establish a transfer obligation. A support commitment does not establish timely performance. Control can matter while restrictions still prevent a particular use of funds.

When support is merely expected, preserve it as a scenario assumption with the reason for that expectation. A risk account may reasonably consider it; an account of cash already available needs the stronger fact it claims.

#### FDM.2:4.4 - Build the warranted aggregate

Combine only amounts whose meaning, time, currency and inclusion rule are adequate for the receiving use. Preserve restrictions and conditional relations that can change the result.

For a reporting result, retrieve the relevant provisions for consolidation, recognition, measurement or elimination, with their scope and exceptions, or obtain the responsible accountant's supported treatment. If the boundary depends on an unresolved control determination, provide the ownership and decision-right facts needed for it and ask which entities enter this reporting boundary for this period. A request for a consolidated number cannot supply that missing conclusion.

Use the returned boundary and treatment to identify included entities, align the relevant accounting bases and perform required adjustments. Explain an unresolved difference rather than combining incompatible values. [MA.4][MA4] supplies the account-construction and reconciliation work once the responsible treatment is adequate. A valuation, conversion or netting operation likewise needs the rule appropriate to its actual use; the group label does not supply one.

A useful specialist return supplies the decisive treatment, the parties and period to which it applies, the conditions that change it and the resulting model operation. If only the applicable jurisdiction or reporting basis is missing, ask for that selection. Apply an already adequate treatment directly.

For a payment question, derive the debtor's usable funds at the payment time after other relevant receipts and obligations. Include another entity's support through the arrangement and conditions established in §4.3. For a risk question, retain the exposures and dependencies needed to understand adverse scenarios. Do not silently use the risk aggregate as the payment-feasibility balance.

#### FDM.2:4.5 - Return the boundary and its financial meaning

Return the relevant parties, membership rule, positions and justified aggregate or support conclusion. State what remains unresolved where it affects use: an entity identity, support condition, restriction, payment time or aggregation rule.

Use [SIE.6][SIE] to combine the relevant claims into a qualified answer once their financial meanings are established. Its result can retain several claims or report conflict, non-comparability or an unresolved premise. FDM.3 develops conditional support flows; FDM.4 establishes the effects of an actual transfer. A sufficient ordinary boundary can be used without constructing every other group view.

### FDM.2:5 - Archetypal Grounding

#### FDM.2:5.1 - A founder group and one debtor

X must pay 100 on day 7. Its unrestricted cash available on that date, after all other receipts and obligations but before this payment, is 20. Y holds 150 in its own account. They share a founder. These are supplied facts of a constructed case.

The founder-group view can show both members and their balances. It does not settle X's ability to pay. X has an **80 shortfall** under the stated cash premise.

Suppose a duly established support arrangement requires Y to transfer 80 to X, with conditions that make it due before day 7. The model now contains a support obligation whose timely performance could close the gap. Until adequate evidence establishes the transfer or another means of timely availability, “support committed” remains different from “funds available”.

If the arrangement instead provides only a guarantee exercisable after X fails to pay, the creditor may have a further route under those supplied terms. X still lacks day-7 cash in the facts given. FDM.3 models the guarantee's actual trigger and timing; the model must not describe it as an earlier transfer.

If Y has no support commitment but the founder is expected to arrange a voluntary transfer, keep that event in the scenario that assumes it. For a portfolio-risk question, common dependence on that founder or on the same market can justify examining the members together even when no transfer is possible.

#### FDM.2:5.2 - A reporting group and an internal amount

Suppose the reporting practitioner has established the reporting basis and period and determined that P and S are consolidated for that report. Their aligned standalone accounts include P's receivable of 40 from S and S's corresponding payable of 40. The supplied consolidation treatment eliminates that internal pair in the group view.

Preserve the two entities' own claims for a separate question about S's payment. The reporting adjustment does not discharge S's obligation. If the reporting boundary has not been determined, ask for the missing determination; do not infer the same elimination merely because P and S share a founder.


### FDM.2:6 - Bias-Annotation

An investor may view a founder group as one economic story; a reporting system may prefer one legal identifier. Test both against the actual consequence being claimed.

Evidence of past voluntary support can inform an expectation. It does not by itself establish a present obligation or remove the possibility that support will arrive too late.

### FDM.2:7 - Conformance Checklist

For the boundary's stated use, examine whether:

1. The financial question, relevant time and underlying parties are clear.
2. Group membership follows an identified criterion adequate for that question.
3. Liability, control, support, permission and expected behavior remain distinct where their differences matter.
4. An aggregate retains the necessary time, currency, restrictions and applicable composition rule.
5. A claim of available funding has adequate support for timely usability, and unresolved premises remain visible.

### FDM.2:8 - Common Anti-Patterns and How to Avoid Them

**Funding X by summing X and Y.** Recover the relation and event that make Y's resources usable for X's payment.

**Reading a guarantee as cash in advance.** Use the actual trigger, beneficiary and payment conditions. The guarantee may answer a recovery question while leaving the immediate funding question open.

**Rejecting a useful risk group because its members are separate debtors.** Keep the debtor accounts and model the shared exposure for the risk use that needs it.

### FDM.2:9 - Consequences

The user can compare group views without erasing the party that bears an obligation or the conditions of support. This exposes both false funding comfort and overlooked shared exposure.

The model can require more than one structure. Maintaining those structures is justified by their uses; unused groupings add cost without improving the financial answer.

### FDM.2:10 - Architectural Rationale

The method begins with the consequence because there is no single group boundary that settles every financial question. It retains underlying positions so that aggregation can be interpreted and revised.

A single reporting tree is adequate when its rule and the receiving use match. Separate-entity accounts suffice for an isolated debtor question. Several connected views become useful when support, exposure and reporting differ. Their connection uses SIE's existing identity and composition methods, with the financial relations supplied here.

### FDM.2:11 - SoTA-Echoing

The practice question is which party and group account makes a financial consequence intelligible. For financial groupings, the method adapts C.32.MWA's idea that several useful structures need not coincide. SIE.5–6 supply identity and composition methods.

This changes §§4.1–4.4: choose the boundary by the consequence, retain the members' positions and examine support separately. At the effort of naming the debtor and the support relation, it can expose a payment shortfall that a founder-group total hides. A larger organizational model is useful only when another material relation needs it.

[AASB 10 §19 and B86–B88][AASB10] illustrate that reporting choice: preparing consolidated statements involves consistent accounting policies and adjustments that eliminate intragroup balances. They give a practitioner using that basis rules for §4.4 once the reporting boundary is established. If the report uses another basis, retrieve its treatment instead.

The X–Y example demonstrates the difference between grouping entities and establishing support under its supplied conditions. Reopen the boundary when actual membership, support terms, restrictions, reporting basis or the receiving financial question changes.

### FDM.2:12 - Relations

FDM.1 supplies positions, FDM.3 their conditional flows and FDM.4 actual changes. FDM.5 uses the relevant participant boundary when examining a service result.

SIE.5 supplies unresolved identity work and SIE.6 composition. Use [FPF C.32.MWA][MWA] when a financial-practice architecture question spans several structures, starting from representative performed work or a prospective use case. The relevant accounting, legal or financial practice supplies a disputed reporting, liability or aggregation rule.

### FDM.2:End
