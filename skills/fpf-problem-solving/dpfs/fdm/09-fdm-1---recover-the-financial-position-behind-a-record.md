## FDM.1 - Recover the Financial Position Behind a Record

**Type:** Architectural

**Status:** Stable


### FDM.1:0 - Use this when

Use this pattern when a balance, agreement, score or label leaves unclear whose financial position it concerns or which terms apply. Identify the party and the question the record is being used to answer.

Establish the relevant right, obligation or other financial interest of the identified party under the conditions and at the time in question. Explain how the records and resources bear on that position.

Use an adequate account directly. If only the report layout has changed and the position is still established, the existing interpretation can suffice.

### FDM.1:1 - Problem frame

In financial records, “claim” can name an assertion in a report or a creditor’s right to receive something. A report may assert that a lender has such a right. Whether the right exists under the applicable terms is a separate question.

A loan agreement, a funded position, an account entry and proceeds available to the borrower can concern the same loan. Determine which of these the question requires you to establish.

### FDM.1:2 - Problem

A record's label and amount can make its financial interpretation appear settled. If the party, terms or time are wrong, a correctly copied number can still answer the wrong question. Treating the record as the position also prevents the practitioner from explaining a stale entry, disputed obligation or valid agreement that has not yet been funded.

### FDM.1:3 - Forces

Start with a sufficient existing account. If a field’s meaning, party or date is disputed and matters to the answer, recover that particular basis.

A right to future payment can be established while the payment itself remains uncertain. Qualify the account accordingly.

### FDM.1:4 - Solution

#### FDM.1:4.1 - State the financial question and relevant party

Start from what the recipient must be able to say or do. Whose claim would a payment discharge, whose duty would remain, or who could draw on the money? Follow the operative relation to its holder and to any other party whose position the answer depends on. If the named account could belong to an agent acting for someone else, ask whether substituting that holder would change the financial conclusion. An established holder can be used directly. Clarify a choice of perspective only when it matters and the request leaves it open.

If the answer depends on a disputed identity or group boundary, use FDM.2 or [SIE.5][SIE]. A trading name, group identifier or database key can locate records. Check the entity it identifies before relying on it to resolve the dispute.

#### FDM.1:4.2 - Recover the position from its applicable basis

Use the terms and institutional basis applicable to this question. Establish what right, duty or interest exists, who holds it, against whom when relevant, and with what content, conditions and timing. If its existence is disputed, state what the available basis establishes.

For a position governed by an agreement, identify the operative agreement for the parties and time in question. Include definitions, elections and amendments that affect the answer. Follow an incorporated reference when it contains a needed interest convention, guarantee notice procedure or other term. A proposal may carry the same commercial label as a concluded agreement. Check which document and status the claim relies on.

For a provision requiring or permitting action, establish who must act or may choose, what the action or election is, which condition activates it, and when it applies. Read the relevant definitions and exceptions. Preserve the provision’s location when a later user must inspect the derived rule. A few operative sentences can suffice for a simple agreement.

Where interpretation could change the result, identify the particular question. Does the weekend adjustment move the payment date alone or also the end of ordinary interest accrual for this installment? Apply an existing supported interpretation for the parties, date and use in question. If a new interpretation is needed, supply the operative text, parties, competing readings, date and intended use to a qualified interpreter, or interpret the provision within your own competence and authority. Use the supported result in the calculation. Where the reading remains open, retain the conditional results. Readings that give the same amount today can diverge at a later date.

An enforceable term can create a conditional obligation before money moves. Identify that obligation separately from the amount advanced, current principal and payments already due. Use the established position with FDM.3 when a flow question follows.

A document can provide evidence. Its execution or another recognized act can also institute a relation under the applicable rule. Establish the rule and event when the claim depends on them. A missing or stale database entry can leave an existing obligation unreported. A recording can itself have legal effect where the rule gives it that effect.

Use [FPF A.2.8][DUTY] to establish whether a particular duty exists. Use [FPF A.2.8.PER][PER] for a permission.

#### FDM.1:4.3 - Relate descriptions and resources to the position

Identify what each source describes, the time it concerns and any limitation affecting reliance. A contract description, a servicing record and a customer's statement can refer to the same loan while differing in date, purpose or evidential support.

When the question concerns resources, establish which of them the party can use at the required time. A borrower may still owe repayment after spending all the proceeds. A lender may have a right to payment even though the borrower cannot pay now. A displayed balance can be evidence when its account meaning, date and availability conditions support the claim.

Describe a prospective position under its conditions. A score or offer can inform a decision. A valid agreement can create duties at formation before disbursement. To establish a particular position, use the conditions that actually apply to it.

#### FDM.1:4.4 - Return what is warranted for this use

Report whose financial relation is at issue, what it provides, the conditions under which it holds and the time to which the finding applies. Relate the material records to the finding and identify any discrepancy or premise the available evidence leaves open.

Use FDM.3 when the question needs conditional events and flows. Use FDM.4 when it asks whether an actual action changed the position. An established position can itself answer a report or decision question.

### FDM.1:5 - Archetypal Grounding

Suppose a lender considers advancing 100 to a borrower. The example stipulates currency, valid agreement formation and terms under which successful funding creates a position with 105 due on day 30. Identify the lender’s right, the borrower’s duty and the proceeds made available on funding.

The lender has a score of 0.72 produced by a scoring method. To interpret it as a probability, establish the meaning and scale the method assigns to it. Establish a lending decision or repayment obligation from the relevant decision and formation evidence.

Suppose the signed arrangement also obliges the lender to advance funds once a specified condition is met. This is a separate pre-funding duty under the stipulated terms. It can matter before any disbursement. If formation or the term is disputed in an actual case, report what the uncertainty leaves open.

Now suppose the advance of 100 has occurred and 105 is due on day 30. A payment of 60 is established. If all 60 applies to that obligation and no further interest or fees arise, 45 remains due. Use FDM.4 to establish that effect. The original contractual payment is still 105. Investigate a servicing record showing all 105 as unpaid when the discrepancy matters to the requested result.

### FDM.1:6 - Bias-Annotation

System designers may prefer facts represented in their own application; a contract specialist may emphasize the agreement while overlooking settlement or usable resources. Compare the accounts around the receiving financial question.

For an ownership interest or a conditional instrument, establish the relation and terms governing that interest. The lender–borrower example grounds a debt case.

### FDM.1:7 - Conformance Checklist

Check whether the proposed interpretation meets these criteria.

1. The question and the scope of the party or parties whose position matters are clear. A claim identifying a particular holder is supported at that level.
2. The account gives adequate grounds for the position asserted, its absence or the limits of a finding, with the conditions and time on which that conclusion depends.
3. Assertions and records about the position remain distinguishable from the position itself.
4. Claims about available resources or expected future performance have the grounds they require in addition to the established position.
5. The result supplies an adequate answer or names the particular identity, term, rule or evidence still missing.

### FDM.1:8 - Common Anti-Patterns and How to Avoid Them

**Treating “claim” as one unambiguous object.** State whether the sentence concerns an assertion or a creditor's right. Then relate them where the report is evidence about the right.

**Making the database constitutive by default.** Establish what rule, if any, gives the relevant recording act that effect. A stale or missing entry otherwise remains a recording question.

**Deferring every duty until funds move.** Inspect the actual formation and conditional-performance terms. A valid unfunded arrangement can already have consequences.

### FDM.1:9 - Consequences

The recipient can use an amount with its financial meaning and can distinguish uncertainty about a position from uncertainty about payment. The model also makes a disagreement between records intelligible.

Recovering terms and relations concealed by a label takes work. An adequate existing account reduces that cost. An unresolved institutional interpretation limits the conclusion the model can supply.

### FDM.1:10 - Architectural Rationale

The financial position is the central subject because it is what the record is commonly used to infer. Beginning with the receiving question limits the reconstruction to distinctions that matter.

A dictionary can settle a shared term when that is the question. To establish a particular party’s right or duty, use the applicable terms and facts. Trace a financial service only when the receiving question also needs its contribution.

### FDM.1:11 - SoTA-Echoing

To interpret a financial record, distinguish what an institution establishes from what the record asserts. Apply that distinction in §§4.2–4.3 by identifying the applicable relation and connecting the relevant descriptions and resources to it.

Use FIBO to clarify a financial concept or relation obscured by a local label. Evidence that a particular party holds a right comes from its institutional basis. Recovering that basis can reveal a missing formation condition or date that renaming the field would leave open.

FINOS CDM’s [Legal Agreements model][CDM-LEGAL] distinguishes agreement identification, elections, amendments and related agreements. These distinctions help locate terms hidden by a single agreement field. For their effect in the particular case, use a supported interpretation under §4.2.

Revisit an interpretation when a change in terms, party identity or evidence could affect the account of the position. Distinguish a change in what is known from a change in the position itself.

### FDM.1:12 - Relations

FDM.2 resolves the party or group boundary; FDM.3 derives contractual behavior; FDM.4 establishes actual changes. FDM.5 uses an adequate position model when tracing a service's contribution.

Use A.2.8 for an individual duty, A.2.8.PER for permission and A.2.9 for communicative work when its occurrence matters. Use [ADM.2 through ADM.4][ADM] for the corresponding administrative participant, effectivity and account questions. SIE supplies general identity and correspondence methods. Use the applicable financial terms for the financial interpretation.

### FDM.1:End
