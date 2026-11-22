## FDM.Reference:3 - Connect models by the financial question

Begin with the decision the financial model will support. Identify the party, position or instrument and the date that matter to that decision. Work out which financial situations are consistent with the available account and terms. If none is, resolve the incompatible premises or qualify the answer. Can two situations with the same account require different actions? If so, retain the distinguishing right, event or term, or obtain evidence for it. If the answer is the same throughout, use it even when the underlying histories differ.

When two models must work together, choose the detail on each side for the same decision. Two installments due to the same creditor in the same month can be combined for a question about the total due in that month, once their amounts, currency and inclusion are established. Before promising to pay each installment on time, connect its deadline to funds and an authorized payment route usable then. To establish timely performance, the total paid during the month can conceal a late first payment. Match the settlements and their effective times to the installments. A reliable statement that both were settled by their due times can answer directly. An explanation of how the payment service achieved that result also needs the actions that brought it about.

A model may group several entities, represent the other side of a contract or describe the position after settlement. To decide whether one model strictly refines another, fix the question and explain how the new model is read in the earlier one. Establish a feasible case of the new model, show that every such case satisfies the earlier assertions under that reading, and identify a formerly possible answer now excluded. Check the conditions attached to a sum. A replacement that allows payment without the security previously required can break the old rule even if it lists fewer payment amounts. When strict refinement holds, the earlier model is more abstract for that question. On returning to it, recheck any payment conclusion that relied on a condition the more abstract model leaves open. Two models can give the same yes or no about today's payment and permit different, even incomparable, sets of exact balances. [Compare models for refinement](../../sections/08-part-b---trans-disciplinary-reasoning-cluster/32-b-5-mr---compare-models-by-refinement-and-abstraction.md#b5mr42---test-preservation-and-strictness)

Suppose a lending model stores “loan amount = 100” for the principal, while a payment model requires the amount payable at maturity. Equal-looking field names do not establish an adequate correspondence.

For this principal-to-maturity calculation, use FDM.1 and FDM.2 to check that both models refer to the same lender, borrower and contract. The terms used with FDM.3 give principal of 100 and a payment of 105 in the stated currency on day 30. With [SIE.4][SIE], connect the principal field to the principal input and derive the maturity value from the terms. Copying 100 into the maturity field would understate the amount due by 5.

Use [SIE.5][SIE] to preserve the party and contract identities and [SIE.6][SIE] to combine statements with their meanings, currency and time. Use [SIE.3][SIE] to assess whether the models answer the receiving question or need an extension.

For this example, assume the advance of 100 has occurred and sufficient evidence establishes it. Under the supplied terms, funding creates an obligation to pay 105 on day 30.

| Receiving question | Financial statement needed | Meaning that a connection must preserve |
| --- | --- | --- |
| How much was advanced? | Principal advance of 100 under the supplied terms. | The amount advanced. |
| What is contractually due at maturity? | Payment of 105 on day 30. | The contractual amount and event conditions. |
| What was actually paid? | An adequately established payment of 60. | The actual occurrence, with its relevant dates. |
| What remains due after that payment? | 45 under the supplied application rule, with no further fees or interest. | The effect of payment on the obligation. |

If the requested statement depends on funding, payment or discharge, use the corresponding established event or effect. FDM.4 helps establish it when it is still in question. Keep the original contractual schedule alongside the observed performance when reporting or modeling risk needs both. The connection is adequate when it answers the receiving question or shows precisely which premise remains unresolved.

[FIBO][FIBO] describes financial concepts and their relations. [ACTUS][ACTUS] supplies logic for deriving scheduled contractual events from terms. A model may need either or both. To implement a correspondence, inspect the definitions, terms, encoding and outputs on which it relies.
