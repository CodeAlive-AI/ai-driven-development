## FDM.1 - Recover the Financial Position Behind a Record

**Type:** Architectural

**Status:** Stable


### FDM.1:0 - Use this when

Use this pattern when someone relies on a balance, agreement, score or financial label without being able to say whose position it describes and under which terms. Begin with the party and the financial question the record is being used to answer.

The pattern governs an account of a financial position: the relevant right, obligation or other financial interest of an identified party under stated conditions and at a relevant time. It returns the warranted position and its relation to the records and resources involved.

Use an already adequate account directly. A cosmetic change to a report does not require recovering an undisputed position from the beginning.

### FDM.1:1 - Problem frame

Financial systems hold statements about parties and their positions. The word “claim” can refer either to an assertion in a report or to a creditor's right to receive something. Those meanings have different consequences. A report can assert that a lender has a right; the assertion and that right remain distinguishable.

Similarly, a loan agreement, a funded loan position, an account entry and the proceeds available to the borrower are connected without being the same subject. The receiving use determines which of these must be established.

### FDM.1:2 - Problem

A record's label and amount can make its financial interpretation appear settled. If the party, terms or time are wrong, a correctly copied number can still answer the wrong question. Treating the record as the position also prevents the practitioner from explaining a stale entry, disputed obligation or valid agreement that has not yet been funded.

### FDM.1:3 - Forces

A practitioner needs an answer quickly enough to support work. Reconstructing every institution and document is excessive when an adequate established account is available. Yet a material gap cannot be supplied merely by trusting a familiar field name.

The position can be clear while its future performance is uncertain. The model must retain that difference: a right to a future payment is not an assurance that the payment will occur.

### FDM.1:4 - Solution

#### FDM.1:4.1 - State the financial question and relevant party

Ask what someone intends to conclude from the record: who owes, who may receive, who bears a loss, what is available or another specific result. Identify the actual party whose position matters and the counterparty or other participant required to interpret it.

Resolve a material identity or grouping uncertainty through FDM.2 or [SIE.5][SIE]. A common trading name, group identifier or database key can help locate the party but cannot settle a disputed entity boundary.

#### FDM.1:4.2 - Recover the position from its applicable basis

Obtain the terms and institutional basis adequate for this question. Establish what right, duty or financial interest they provide, to whom, against whom where relevant, with what content, conditions and time.

For a position governed by an agreement, locate the operative agreement for the identified parties and time, together with the incorporated definitions, elections and amendments that can change the answer. Follow a reference when the referring clause leaves a needed operation elsewhere: a loan schedule may name an interest convention defined in another document, or a guarantee may use a notice procedure in a master agreement. A proposal and a concluded agreement can have the same commercial label while supporting different claims.

When a provision requires or permits an action, recover the party that must act or may choose, what it must do or can elect, the condition that activates that consequence, and the time at which the consequence applies. Read the provision together with its definitions and exceptions. Keep its location beside a derived rule when a later user must be able to inspect why that rule was selected. Keep the reconstruction to provisions that can affect the answer; a small adequate agreement may need only a few sentences.

When interpretation is unresolved, formulate the question at the point where it changes the model. Instead of “please confirm the contract,” ask, for example: “Does the weekend adjustment move only the payment date, or also the end of ordinary interest accrual for this installment?” Give the interpreter the parties, operative text, proposed alternatives, relevant date and intended use. Obtain the supported interpretation and its applicable conditions. Use it to complete the affected calculation, or retain the alternative results while the question remains open. Keep different readings distinct when a later date would distinguish their effects, even if they give the same amount today.

A term can already create a conditional obligation before money moves. Separate that relation from the amount advanced, current principal and payments already due. The resulting position supplies the starting basis for FDM.3.

A document can provide evidence and, under an applicable rule, its execution or another recognized act may help institute a relation. Recover that rule and event when they matter. Do not infer the existence or absence of an obligation solely from whether a database entry is present.

[FPF A.2.8][DUTY] supplies the question whether an individual duty actually obtains. A permission uses [FPF A.2.8.PER][PER].

#### FDM.1:4.3 - Relate descriptions and resources to the position

Identify what each source describes, the time it concerns and any limitation affecting reliance. A contract description, a servicing record and a customer's statement can refer to the same loan while differing in date, purpose or evidential support.

Distinguish the position from resources actually available. A borrower can owe repayment while proceeds have already been spent. A lender can have a funded right to payment while the borrower cannot currently pay. A displayed balance can be evidence about these facts, but its interpretation still needs the relevant account and availability conditions.

Retain a prospective position as prospective. A score or offer can inform a decision without establishing an agreement. Conversely, applicable terms can establish duties at valid formation before disbursement. Examine the actual conditions rather than imposing one universal sequence.

#### FDM.1:4.4 - Return what is warranted for this use

Return the party, financial relation, content, conditions and time at enough detail to answer the question. Relate the material records to that account and name any discrepancy or missing premise.

Use FDM.3 when the receiving question needs the event and flow consequences. Use FDM.4 when an actual action may have changed the position. If the position is already sufficient for a routine report or decision, supply it without expanding the model.

### FDM.1:5 - Archetypal Grounding

A lender considers advancing 100 to a borrower. In this constructed arrangement, valid formation, currency and the applicable terms are supplied: successful funding creates the stated funded position, with 105 contractually due on day 30. The model distinguishes the lender and borrower, their respective right and duty, and the proceeds made available on funding.

An earlier score of 0.72 is a produced assertion under its scoring method. Its scale and meaning must be known before it is interpreted even as a probability. The score alone establishes neither a lending decision nor the borrower's repayment obligation.

Suppose the signed arrangement also obliges the lender, before funding, to advance the amount once a specified condition is met. That supplied term gives the practitioner a separate pre-funding duty to examine. Waiting for disbursement before recognizing every obligation would lose it. If the actual formation or term is disputed, the model returns that exact uncertainty.

Now assume that the advance of 100 has occurred and the resulting obligation to pay 105 is established. After an adequately established payment of 60, the original agreement still describes the contractual payment of 105. FDM.4 can establish the remaining 45 under the example's application rule and absence of further fees or interest. A servicing record that still shows an unpaid 105 is now a discrepancy to investigate, not proof that the payment had no effect.

### FDM.1:6 - Bias-Annotation

System designers may prefer facts represented in their own application; a contract specialist may emphasize the agreement while overlooking settlement or usable resources. Compare the accounts around the receiving financial question.

The loan is a debt example. Other financial interests require their actual relation and governing terms; do not force an ownership interest or conditional instrument into a simple lender–borrower account merely because that example is familiar.

### FDM.1:7 - Conformance Checklist

For the proposed interpretation, examine whether:

1. The actual party and financial question are identifiable.
2. The right, obligation or other interest has an adequate basis, content, conditions and time.
3. Assertions and records about the position remain distinguishable from the position itself.
4. Actual resources and expected future performance are not inferred from a position alone.
5. The result supplies an adequate answer or names the particular identity, term, rule or evidence still missing.

### FDM.1:8 - Common Anti-Patterns and How to Avoid Them

**Treating “claim” as one unambiguous object.** State whether the sentence concerns an assertion or a creditor's right. Then relate them where the report is evidence about the right.

**Making the database constitutive by default.** Establish what rule, if any, gives the relevant recording act that effect. A stale or missing entry otherwise remains a recording question.

**Deferring every duty until funds move.** Inspect the actual formation and conditional-performance terms. A valid unfunded arrangement can already have consequences.

### FDM.1:9 - Consequences

The recipient can use an amount with its financial meaning and can distinguish uncertainty about a position from uncertainty about payment. The model also makes a disagreement between records intelligible.

The cost is recovering material terms and relations that a label had concealed. Adequate existing accounts reduce that cost; unresolved institutional interpretation limits the conclusion the model can supply.

### FDM.1:10 - Architectural Rationale

The financial position is the central subject because it is what the record is commonly used to infer. Beginning with the receiving question limits the reconstruction to distinctions that matter.

A dictionary-only account is sufficient when the issue is a shared term and the actual position is already known. It is inadequate when an individual party's right or duty remains unsettled. Starting instead with the complete financial-service chain can impose unnecessary work on a narrow position question.

### FDM.1:11 - SoTA-Echoing

The practice question is how to give a financial record a warranted interpretation. The method uses FPF's distinction between an actual institutional relation and claims about it to interpret financial records. This changes §§4.2–4.3: establish the applicable relation and then connect the descriptions and resources.

FIBO is useful for financial concepts and relations that a local label obscures. It supplies reusable meaning rather than evidence that this particular party has this particular right. At the effort of clarifying one disputed label, a position account can expose a missing formation or time premise that a field renaming would retain.

FINOS CDM's [Legal Agreements model][CDM-LEGAL] offers an implementation comparison: it separates an agreement's identification, elections, amendments and related agreements. This helps locate terms that a single agreement field hides. It does not determine their legal effect; §4.2 obtains that interpretation for the actual question.

Reopen the interpretation when actual terms, party identity or event evidence changes the position being described.

### FDM.1:12 - Relations

FDM.2 resolves the party or group boundary; FDM.3 derives contractual behavior; FDM.4 establishes actual changes. FDM.5 uses an adequate position model when tracing a service's contribution.

A.2.8 governs the individual-duty question, A.2.8.PER the permission question and A.2.9 communicative work where its occurrence matters. [ADM.2 through ADM.4][ADM] supply the corresponding administrative participant, effectivity and account questions. SIE supplies general identity and correspondence methods without replacing the financial terms.

### FDM.1:End
