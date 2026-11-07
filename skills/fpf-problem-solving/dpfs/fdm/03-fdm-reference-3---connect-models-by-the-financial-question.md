## FDM.Reference:3 - Connect models by the financial question

Suppose a lending model stores “loan amount = 100” for the principal, while a payment model requires the amount payable at maturity. Equal-looking field names do not establish an adequate correspondence.

FDM.1 and FDM.2 identify the same lender, borrower and contract. FDM.3 supplies the terms: principal 100, contractual maturity payment 105 in the stated currency on day 30. [SIE.4][SIE] can now establish a qualified correspondence: the principal field supplies the principal input; the maturity amount follows from the applicable terms. Replacing the maturity value by 100 would lose the contractual difference of 5.

[SIE.5][SIE] preserves the relevant party and contract identities. [SIE.6][SIE] combines the statements with their meanings, currency and time. [SIE.3][SIE] asks whether the available models are sufficient for the receiving question and directs a necessary extension. The financial distinction and the general integration method have separate contributions.

For this constructed example, assume that the advance of 100 has actually occurred and is adequately established, creating the obligation to pay 105 on day 30 under the supplied terms.

| Receiving question | Financial statement needed | Meaning that a connection must preserve |
| --- | --- | --- |
| How much was advanced? | Principal advance of 100 under the supplied terms. | The amount advanced. |
| What is contractually due at maturity? | Payment of 105 on day 30. | The contractual amount and event conditions. |
| What was actually paid? | An adequately established payment of 60. | The actual occurrence, with its relevant dates. |
| What remains due after that payment? | 45 under the supplied application rule, with no further fees or interest. | The effect of payment on the obligation. |

FDM.4 supplies the answers about the actual advance, payment and remaining obligation; it does not rewrite the original contractual schedule as if only 60 had been due. A reporting or risk model can retain both the schedule and the observed outcome with their distinct meanings. The connection is complete when it answers the intended question adequately, including any material unresolved premise.

[FIBO][FIBO] supplies a reusable account of financial concepts and their relationships. [ACTUS][ACTUS] supplies a different contribution: logic relating contract terms to scheduled contractual events. A system may need either or both. The example above explains their possible roles; implementing a particular correspondence requires inspecting the chosen definitions, terms, encoding and results.
