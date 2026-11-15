## FDM.Reference:3 - Connect models by the financial question

Suppose a lending model stores “loan amount = 100” for the principal, while a payment model requires the amount payable at maturity. Equal-looking field names do not establish an adequate correspondence.

Use FDM.1 and FDM.2 to check that both models refer to the same lender, borrower and contract. The terms used with FDM.3 give principal of 100 and a payment of 105 in the stated currency on day 30. With [SIE.4][SIE], connect the principal field to the principal input and derive the maturity value from the terms. Copying 100 into the maturity field would understate the amount due by 5.

Use [SIE.5][SIE] to preserve the party and contract identities and [SIE.6][SIE] to combine statements with their meanings, currency and time. Use [SIE.3][SIE] to assess whether the models answer the receiving question or need an extension.

For this example, assume the advance of 100 has occurred and sufficient evidence establishes it. Under the supplied terms, funding creates an obligation to pay 105 on day 30.

| Receiving question | Financial statement needed | Meaning that a connection must preserve |
| --- | --- | --- |
| How much was advanced? | Principal advance of 100 under the supplied terms. | The amount advanced. |
| What is contractually due at maturity? | Payment of 105 on day 30. | The contractual amount and event conditions. |
| What was actually paid? | An adequately established payment of 60. | The actual occurrence, with its relevant dates. |
| What remains due after that payment? | 45 under the supplied application rule, with no further fees or interest. | The effect of payment on the obligation. |

Use FDM.4 to establish the advance, the payment and what remains due. Keep the original contractual schedule alongside the observed performance when reporting or modeling risk needs both. The connection is adequate when it answers the receiving question or shows precisely which premise remains unresolved.

[FIBO][FIBO] describes financial concepts and their relations. [ACTUS][ACTUS] supplies logic for deriving scheduled contractual events from terms. A model may need either or both. To implement a correspondence, inspect the definitions, terms, encoding and outputs on which it relies.
