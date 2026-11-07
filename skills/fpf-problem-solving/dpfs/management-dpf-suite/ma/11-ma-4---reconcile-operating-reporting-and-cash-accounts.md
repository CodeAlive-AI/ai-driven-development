## MA.4 - Reconcile Operating, Reporting and Cash Accounts

**Type:** Architectural

**Status:** Stable

### MA.4:0 - Use this when

Use this pattern when the same work seems to produce incompatible profit, inventory or cash results in different accounts. Begin with the difference that changes a decision or interpretation.

The pattern governs an explanation connecting the relevant accounts while retaining each account's purpose and rules. Its result is a reconciled difference, or a located discrepancy requiring correction or specialist interpretation.

Use an adequate existing reconciliation directly. The method does not replace the applicable financial, tax or other reporting rules.

### MA.4:1 - Problem frame

Production, sale, recognition of an expense and payment can occur at different times. One management account can expense a supplied resource in the period; another account can include an eligible share in inventory until sale. An unpaid credit sale can increase reported revenue and create a customer receivable before cash arrives.

These accounts can disagree numerically without contradicting one another. They can also contain an error. The model must establish which explanation applies.

### MA.4:2 - Problem

A profit figure is often treated as cash generated, or a management restatement as a correction to an external report. That loses recognition, valuation or settlement conditions.

A reconciliation that merely inserts an unexplained balancing amount has the opposite defect: it makes totals agree while hiding the unresolved question. The practitioner needs an explicit explanation of the difference.

### MA.4:3 - Forces

Each account simplifies work for a purpose. Comparing them requires enough common subject and period information to retain their different rules. A detailed event reconstruction is costly when a small inventory or receivable bridge is sufficient.

A correct mathematical reconciliation can still use an inapplicable policy. Reporting adequacy and arithmetic therefore need different evidence.

### MA.4:4 - Solution

#### MA.4:4.1 - Recover what each account measures

Identify the entities, work, period, currency and intended use of each account. Recover the recognition and valuation rules relevant to the disputed amount. State whether the account concerns revenue, expense, inventory, resource consumption, payments or another quantity.

Use OPS.15 for an unresolved event or observation definition. Use the responsible reporting practice when the applicable policy is missing or disputed.

#### MA.4:4.2 - Build the movement account

Recover the opening balances and the events that change them during the period. Match the entities, goods or services, dates and currency to each view. The closing balance of the previous period normally supplies the next opening balance on that same basis. If a policy, boundary or opening amount changed, explain that change before comparing period results.

A sufficient source account can supply aggregate movements. Reconstruct individual events where aggregation hides the disputed term. For an ordinary purchase, production and credit-sale account, begin with these relationships:

| Balance | Movement through the period |
| --- | --- |
| Inventory | Opening inventory + eligible purchases or production cost − cost consumed or sold = closing inventory |
| Receivables | Opening receivables + recognized credit sales − customer settlements = closing receivables |
| Payables | Opening payables + purchases or resource supply on credit − supplier settlements = closing payables |

Use each account's actual recognition and valuation rules to fill the terms. Physical production can be the same in two views while the cost admitted to inventory differs. Carry opening inventory on the corresponding view's basis and apply its rule for identifying the cost released when goods are sold. Purchases, consumption and payment are separate events; equating them would erase the difference being explained.

Extend the movement account when other events occur. A write-down changes inventory without buying or selling units. A customer advance may create a liability before revenue is earned. An equipment purchase, depreciation or financing transaction needs its own balance and flow treatment. Obtain that treatment from the responsible reporting or financial practice. Locate an unexplained residual in the missing event, valuation, period or scope; an invented balancing entry cannot explain it.

#### MA.4:4.3 - Derive the connection between the views

Construct the result under each view from the common events and that view's rules. Then explain how its opening and closing balances connect the recognized flows to settlements.

In a bounded account containing only the ordinary inventory, credit-sale and supplier-payment events above, collections equal revenue less the increase in receivables. Resource costs acquired during the period equal costs recognized in the result plus the increase in inventory. Payments for those acquisitions equal their amount less the increase in payables. Combining these relationships gives:

**Cash movement = period result − increase in inventory − increase in receivables + increase in payables.**

Here an increase means closing balance minus opening balance within the same view. A decrease therefore has the opposite effect. Use a full-cost result with full-cost inventory, and an internal result with that internal account's inventory values. Mixing the result of one policy with the balance of another creates a spurious cash difference.

The formula's scope matters. If the result includes a noncash charge, explain its effect without inventing a payment; if equipment is purchased, include its dated payment separately. For an advance received before revenue, carry the corresponding liability movement. Reconstruct the material additional terms from their events rather than assuming the inventory/receivable/payable bridge covers them. A direct receipt-and-payment account can supply an independent arithmetic comparison.

When one policy retains a production-resource cost in inventory and another expenses it, compare the amount retained at both ends of the period. The difference between the period results is the increase in that retained amount, under otherwise matching recognition. Releasing earlier stock can reverse the result difference even while the policies themselves stay unchanged. State whether the explanation concerns recognition, valuation or settlement; those changes need not occur together.

Show enough intermediate amounts to expose an omitted term and reconcile to the same cash movement where both views describe the same events. The movement is not the closing cash balance. Funding uses opening available cash and the other receipts and obligations at the dates when they occur.

#### MA.4:4.4 - Return the reconciled views and any discrepancy

Preserve each account for its warranted use and return the explanation connecting them. If a source is wrong, identify the correction for its responsible process. A management model does not silently amend a statutory account.

Supply the required monetary basis to the receiving operating or financial method. If funding is at issue, use the whole timed cash position, including other relevant receipts and obligations.

### MA.4:5 - Archetypal Grounding

#### MA.4:5.1 - One period with zero opening balances

A constructed service-manufacturing account starts with zero inventory, receivables and payables and includes only the transactions described below. During the period it produces 100 units, spending 200 on materials and 300 on production-resource supply. All 500 is paid in the period. It sells 60 units at 10, recognizes revenue of 600 under the supplied policy and receives 400; the remaining 200 is receivable.

Under the example's supplied full-production-cost policy, eligible cost is 500, or 5 per unit. Cost of the 60 units sold is 300, closing inventory is 200 and the reported result is **600 − 300 = 300**. The cash movement is **400 − 500 = −100**.

An internal throughput-style account carries only materials in inventory and expenses the 300 resource supply in the period. Materials in the 60 sold units cost 120; closing material-valued inventory is 80. Its result is **600 − 120 − 300 = 180**.

The accounts connect explicitly:

| Connection | Calculation | Result |
| --- | --- | ---: |
| Internal result to the supplied full-cost result | 180 + 120 of production-resource cost retained in closing inventory | **300** |
| Full-cost result to cash movement | 300 − 200 increase in inventory − 200 increase in receivables | **−100** |
| Internal result to cash movement | 180 − 80 increase in material-valued inventory − 200 increase in receivables | **−100** |

The 120 difference is a recognition and valuation effect under the supplied policies. It is not another cash receipt. The unpaid customer balance and closing inventory explain why either positive result coexists with negative cash movement.

An actual reporting use must establish the applicable capitalization, recognition and measurement rules. The example supplies its policies to demonstrate the reconciliation.

#### MA.4:5.2 - Continue through the next period

The next period opens with forty units: full-cost inventory of 200 and internal material-valued inventory of 80. Opening receivables are 200 and opening payables are zero. The same physical opening stock therefore supplies different monetary amounts to the two views.

Produce sixty new units using materials of 120 and production-resource supply of 300. Both are invoiced by suppliers on credit. The supplied full-cost policy admits all 420 to the new inventory, or 7 per new unit, and uses FIFO to identify the cost sold. The internal policy admits only materials, or 2 per unit, and expenses the 300 resource supply. There are no other events, taxes, noncash charges or financing flows in this constructed period.

Sell eighty units for 800 on credit, collect the old receivable of 200 and 500 of the new sales, and pay suppliers 300. Build the accounts from those events:

| Quantity | Full-cost view | Internal view |
| --- | ---: | ---: |
| Opening inventory | 200 | 80 |
| Inventory additions | 420 | 120 |
| Cost of the eighty units sold | 200 for forty old units + 280 for forty new units = **480** | 80 + 120 − 40 = **160** |
| Closing inventory: twenty new units | **140** | **40** |
| Resource supply expensed outside inventory | 0 | **300** |
| Period result | 800 − 480 = **320** | 800 − 160 − 300 = **340** |

Receivables close at **200 + 800 − 700 = 300**. Payables close at **0 + 420 − 300 = 120**. Direct cash movement is **700 − 300 = 400**. Each view reaches that amount using its own inventory movement:

- Full cost: **320 − (140 − 200) − (300 − 200) + (120 − 0) = 400**.
- Internal: **340 − (40 − 80) − (300 − 200) + (120 − 0) = 400**.

The full-cost result is now twenty lower than the internal result. Full-cost inventory retains 100 more production-resource cost at closing, compared with 120 more at opening. The change, **100 − 120 = −20**, explains the reversal. Using only closing inventory would miss the release of the previous period's cost.

If customers instead settle another 100 before period end, closing receivables fall to 200 and cash movement rises to 500. Both period results stay unchanged under these recognition premises. If that 100 is instead an advance for future work, its event and liability treatment must be obtained; it cannot be subtracted from these existing receivables merely to make the bridge balance.

MA.5 can project the same movements through future periods. Keep a revised collection date in the cash forecast, while retaining the recognition and valuation assumptions that still hold.

### MA.4:6 - Bias-Annotation

An internal decision maker can prefer the view that supports a proposal; an external-reporting practitioner can treat a required account as adequate for every internal choice. Retain the purposes and rules of both.

A familiar bridge can also conceal a new item. An unexplained residual remains a discrepancy rather than evidence that the reconciliation is complete.

### MA.4:7 - Conformance Checklist

Examine whether the accounts' subjects, periods, currency and purpose are clear; relevant recognition and valuation rules are established; opening values and events support the comparison; differences reconcile without an unexplained residual; and corrections are distinguished from valid alternative views.

Arithmetic establishes the connection under those premises. Policy applicability and actual settlement require their own support.

### MA.4:8 - Common Anti-Patterns and How to Avoid Them

**Reading profit as available cash.** Reconcile inventories, unsettled balances and other relevant movements, then establish the timed cash position.

**Correcting one legitimate account into another.** Explain the policy and purpose difference before changing a source.

**Hiding the gap in “other”.** Locate the unresolved event, period or valuation item.

### MA.4:9 - Consequences

The user can explain apparently conflicting accounts and choose the monetary basis the receiving decision needs. An actual error becomes distinguishable from a valid difference in purpose or timing.

The work can require specialist interpretation of a reporting policy. A completed management bridge does not confer that reporting authority or supply missing event evidence.

### MA.4:10 - Architectural Rationale

The method connects views through their subjects, events and rules because a shared monetary unit does not give them a shared meaning. It preserves the views instead of manufacturing one universal profit number.

A small bridge is preferable when a few known balance movements explain the difference. Event-level reconstruction becomes worthwhile when the aggregate no longer locates the discrepancy.

### MA.4:11 - SoTA-Echoing

The method distinguishes internal from externally required accounts and uses the inventory bridge discussed in Bragg's *Throughput Accounting* (2007), printed pp.111–112. It adapts that explanation to explicit policies and actual settlements rather than treating a management view as a substitute for required reporting.

[IAS 2][IAS2] provides a relevant external-reporting comparator: inventory cost and its later recognition as expense have rules that differ from simply recording cash paid. Its applicability and detailed requirements belong to the reporting question. Here that distinction changes §§4.1–4.3 and the inventory example.

The movement account makes the same connection reusable across periods: the opening inventory and unsettled amounts survive into the next calculation, while policy determines which cost enters the result. The two-period example explains why the difference between results calculated under the two policies can change sign from one period to the next while the policies remain unchanged. Reopen the bridge when policies, balances, event meanings or the receiving period changes.

### MA.4:12 - Relations

MA.1–MA.3 supply resource and assignment meanings. MA.5 uses reconciled assumptions in a forecast; MA.7 investigates differences; MA.9 examines behavior encouraged by a particular view. OPS.15 supplies operating-account definitions and events. OPS.14 and the relevant financial practice consume the monetary basis their decisions require.

### MA.4:End
