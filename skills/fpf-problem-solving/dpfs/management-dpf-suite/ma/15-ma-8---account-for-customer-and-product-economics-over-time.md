## MA.8 - Account for Customer and Product Economics Over Time

**Type:** Architectural

**Status:** Stable

### MA.8:0 - Use this when

Use this pattern when a current unit margin hides acquisition, later service, retention, returns or other consequential flows. Begin with the customer cohort or product use and the decision the account must support.

The pattern governs a time-related customer or product account. It returns observed and conditional resource and monetary flows over a stated horizon, with the assumptions needed to interpret acquisition, continuation and scale.

Use an adequate existing account directly. A lifetime valuation or financing decision uses the additional method required by the relevant financial practice.

### MA.8:1 - Problem frame

A service can earn a positive margin from an active customer this month while still failing to recover acquisition spending. Future service demand, retention and collection determine a different part of the account. An established customer's continuation also raises a different question from acquiring a new customer.

Products have their own time structure. Development, production, warranty, support and withdrawal can occur in different periods. A subscription-retention formula does not describe every product's later obligations.

### MA.8:2 - Problem

A single current margin or acquisition ratio compresses the period, population and resource behavior. Extending it across a lifetime can conceal churn, heterogeneous cohorts or an additional supply block.

Counting every historical cost again in a continuation choice produces the opposite error. The task is to preserve the whole account needed for understanding while supplying the future changes relevant to the actual choice.

### MA.8:3 - Forces

The account needs a useful horizon even when long-term behavior is uncertain. Early cohorts provide evidence, but their acquisition conditions and service mix may differ from later expansion.

A detailed lifetime model can look more authoritative than a modest period account. Added precision is useful only when its assumptions and evidence support the receiving conclusion.

### MA.8:4 - Solution

#### MA.8:4.1 - Define the unit, population and decision time

State whether the account concerns a customer, subscription, household, product, cohort or another justified unit. Define membership, the observation date and the horizon. Preserve differences in acquisition channel, tenure or use when they can change the answer.

Distinguish a prospective new customer from an existing one. Recover historical acquisition spending for the account, and identify which future acquisition or service payments the current decision can change.

#### MA.8:4.2 - Construct the dated product or service account

Recover receipts, refunds, acquisition, service, support and other consequential flows with their timing and account meaning. Use MA.1–MA.4 for missing resource, capacity, shared-cost or reconciliation results.

For a product, trace the work from development and preparation through production, sale, service and withdrawal. Start from the operating plan and the events that create obligations: a sale may create a later warranty requirement, and stopping sales may leave support or closure work to perform. For each relevant event, obtain the resource quantity and the date it is needed. MA.1–MA.2 relate those demands to actual capacity and supply arrangements. Use FDM when the obligation or the event that can change it is unresolved.

Distinguish a commitment about future work from resource consumption, accounting recognition and payment. An early design choice can constrain later costs before those costs are incurred. A later service obligation can survive the sales period or sales cessation. Apply MA.4's account rules to obtain the reporting result, and its settlement movements to obtain the cash dates; neither result can be read from the physical sequence alone.

Keep each underlying event once in the whole account. A common resource payment may serve several product phases or products. MA.3 can assign it for a stated reporting purpose, but those assignments do not create additional payments. Preserve historical observations separately from conditional future quantities and obtain an adequate supply or obligation assumption where a missing event would change the account.

State whether a reported margin includes allocated costs, resource consumption values or incremental flows. Reuse it only for the use those meanings support.

#### MA.8:4.3 - Put cohort activity on calendar time

For an observable subscription renewal, count the customers eligible for that renewal and those who renew. Divide renewals by that eligible population, using a completed observation window; customers not yet due to renew cannot establish that period's renewal outcome. Preserve age, channel or other group distinctions where pooling would change the result.

To project a cohort under supplied or supported successive renewal rates, multiply each period's remaining population by the rate for its next renewal. For example, a 100-customer cohort at 80% and then 70% gives 80 and then 56, not two separate reductions from the original hundred. An existing cohort begins with its current active population and tenure. Applying a new-customer lifetime formula to it would repeat time that has already passed.

Map each cohort's age to calendar dates before combining accounts. A cohort's month 1 may be another cohort's month 4. Put their service demand into the same calendar window, add the demands for each shared resource and only then apply that resource's supply threshold through MA.1–MA.2. Place acquisition, service payments and receipts at their actual dates, which need not coincide. This obtains a shared resource and cash account without charging the same supply payment once per cohort.

Use an appropriate supplied forecast through MA.5 when behavior needs estimation beyond this account construction. The operation above translates qualified rates into quantities; it does not establish those rates or turn non-purchase into an observed termination.

#### MA.8:4.4 - Establish the continuation and scale assumptions

Use a model appropriate to the actual relationship. A subscription can provide an observable renewal or termination event. A customer who makes no purchase this month may merely be between purchases; treat their future activity with an adequate model for that setting.

Inspect whether behavior changes with tenure, cohort, channel or proposed scale. A constant rate can be a supplied scenario assumption; an aggregate historical rate does not establish that it applies to every customer or future period.

Check how scale changes acquisition and resource supply. A larger audience may cost more to reach, while a new server, service team or warranty obligation can change the cost pattern. Neither falling unit cost nor rising acquisition cost is a universal law.

#### MA.8:4.5 - Compare the whole account and the future change

Calculate the observed and conditional period results on the stated basis. Preserve the acquisition boundary, relevant survival or purchasing assumptions and timing. If a limited horizon is used, state what lies outside it; do not call a three-month total a complete lifetime value.

Test the plausible changes that could alter the decision: retention, service intensity, refunds, collection, acquisition cost or a supply threshold. A valuation use obtains the applicable discounting and risk treatment from the relevant financial method.

For a continuation or expansion choice, establish the future baseline without the proposed action, including obligations already created. Construct the alternative with its changed quantities, supply and obligations at the same dates. Subtract the baseline from the alternative to obtain the future difference. Historical development, acquisition or production can explain cumulative recovery without becoming an avoidable payment. An obligation common to both futures cancels from their difference but remains in each whole cash account.

Supply the qualified future differences to OPS.14 or the responsible financial practice. Use the whole dated cash account for liquidity, including unchanged obligations and other receipts. Discounting, taxes, risk and financing require the applicable financial method; an undiscounted operating total does not decide those questions.

If the whole product or customer account fails a required economic condition and a suitable alternative is not yet known, use MA.10 to construct one with the responsible design practices. This can change the offer, population, service model or provision rather than merely improve a cost number. Rebuild the affected time and obligation account here. If an adequate alternative is already supplied, this account construction and the receiving comparison can suffice.

### MA.8:5 - Archetypal Grounding

#### MA.8:5.1 - Keep acquisition and cohort continuation distinct

A constructed subscription cohort acquires 100 customers at 20 each, paid initially: **2,000**. The scenario assumes 80% renewal into each next month, and 10 of receipt less relevant service payments per active customer per month. Its three-month account is:

| Month | Active customers under the scenario | Period net service flow |
| --- | ---: | ---: |
| 1 | 100 | **1,000** |
| 2 | 80 | **800** |
| 3 | 64 | **640** |

The three-month service total is **2,440**, leaving **440 after acquisition spending** on this undiscounted basis. These are conditional flows, with no other changing flows under the supplied scenario. This account omits flows after month 3.

Before month 2, the original acquisition payment is already spent. Count the original 2,000 once in the cumulative account. Compare continuation with stopping using the future flows that change and the applicable obligations.

Suppose a proposed new cohort costs 35 per customer to acquire, contributes only 6 per active customer per month and has a supplied 60% monthly renewal scenario. Its corresponding three-month service flow is **600 + 360 + 216 = 1,176** against **3,500** acquisition, leaving **−2,324** on the same limited basis. Copying the earlier cohort's ratio would conceal the changed expansion conditions.

#### MA.8:5.2 - Carry a product through sales and later obligations

A product can require a different model. Suppose an already sold product carries a supplied obligation to provide a service module in year 2 at an expected resource cost of 400. Include that later requirement even if current unit margin omits it. Stopping new sales does not by itself cancel the supplied obligation. Use [Financial Domain Modeling (FDM.1 and FDM.3)][FDM] to recover an unclear obligation or its required events, and FDM.4 to establish what an actual change did to it.

Extend that product into a complete constructed account. Development of 1,200 was paid before year 1. One hundred units sold in year 1 for 3,000, all received, with production payments of 1,600 in that year. The supplied service obligation requires payment of 400 in year 2 and closure requires 200 in year 3. Assume those amounts cover the relevant flows, with no other taxes, financing or resource payments in this teaching case.

| Phase and payment time | Receipts | Payments | Net flow |
| --- | ---: | ---: | ---: |
| Development before year 1 | 0 | 1,200 | **−1,200** |
| Production and sales in year 1 | 3,000 | 1,600 | **1,400** |
| Service in year 2 | 0 | 400 | **−400** |
| Closure in year 3 | 0 | 200 | **−200** |
| Whole account | **3,000** | **3,400** | **−400** |

The sales-period production margin of 1,400 therefore coexists with a whole undiscounted total of **−400**. This table is a payment account under the supplied premises. Applicable recognition rules can place expenses differently; MA.4 supplies the reporting comparison. Neither a margin nor the timing table alone determines the appropriate product decision.

Now stand at the end of year 1. The development and production payments, and the original sales receipts, are history. The existing 400 service and 200 closure remain payable under both futures. A feasible additional sixty-unit option would receive 1,800 later in year 2, pay 960 for production at the start of year 2 and create 240 of further service payments in year 3. Assume adequate supplied capacity and unchanged old obligations.

The additional option changes the future account by **1,800 − 960 − 240 = 600**. Without it, the remaining old obligations produce net future flow of −600; with it, total future flow over years 2–3 is zero. The favorable **difference** does not erase either obligation. Nor does it settle liquidity: production is paid before the new receipts, so the whole account by payment date is needed.

An alternative design requires another 300 before that production and reduces the new service payment from 240 to 120 in year 3. Against the original additional-sales option, it changes this limited undiscounted account by **−300 + (240 − 120) = −180**. Any further claim for quality, revenue or risk reduction needs its own supported consequence. A lower later service cost alone does not make the whole alternative better.

Changing the payment date returns to the timed account. Changing an obligation returns to FDM; changing the required work or capacity returns to MA.1–MA.2 and the operating decision. The historical account remains useful for understanding the product's full result while the current comparison uses what the choice can still change.

### MA.8:6 - Bias-Annotation

Successful early cohorts can bias an expansion forecast. Acquisition channel, customer mix and capacity may change as the service grows.

A short account can understate later value or cost. Extending the horizon without supported continuation assumptions can instead overstate what is known. Name the actual horizon and decision use.

### MA.8:7 - Conformance Checklist

Examine whether the unit, cohort and decision time are clear; the horizon and account basis are explicit; cohort ages align to calendar periods; acquisition, product phases and later obligations have adequate meanings and timing; continuation and scale assumptions are warranted or qualified; and historical spending is distinguishable from future changes.

A conditional account supports the stated scenario. Actual retention, causal marketing effects and financial valuation require their corresponding evidence and methods.

### MA.8:8 - Common Anti-Patterns and How to Avoid Them

**Calling a short-period total lifetime value.** State the horizon and retain any material omitted continuation.

**Using non-purchase as proof of departure.** Obtain an activity model appropriate to the relationship.

**Copying an early cohort's economics without checking the expansion conditions.** Examine changed acquisition, mix, retention and resource thresholds.

**Charging sunk acquisition or development again to the continuation choice.** Preserve the historical account and supply the actual future differences.

**Ending the product account when sales stop.** Carry surviving service and closure obligations into the future baseline.

### MA.8:9 - Consequences

The user can see why current margin, cumulative recovery and future continuation differ. The account supports a more specific growth, service or product question.

Longer horizons increase dependence on behavioral and resource assumptions. A qualified short account can be more useful than an apparently precise lifetime number with unsupported premises.

### MA.8:10 - Architectural Rationale

The method organizes flows around the population and time of the decision because acquisition and continuation do not concern identical future consequences. Resource modeling reveals when serving more customers changes capacity needs and payments.

A simple cohort table is adequate for a bounded scenario. A richer purchasing, retention or product-life model is justified when its distinctions can change the use and can be supported. The account supplies financial inputs without replacing valuation or financing methods.

### MA.8:11 - SoTA-Echoing

The method connects acquisition, customer and scale questions to explicit period flows. It uses the relevant resource and payment relationships and interprets ROI, ROMI and customer-value ratios under their stated definitions.

Fader and Hardie's [2014 CLV note][CLV] qualifies the lifetime label, customer-age boundary and contractual versus noncontractual setting. Their later [duration-dependence work with colleagues][RETENTION] extends a model based solely on customer heterogeneity, showing why changing aggregate retention does not directly identify changing individual behavior. These contributions require explicit population, tenure and continuation assumptions in §§4.1–4.4. The 2014 note, pp.2–4, supports the successive conditional-rate and existing-customer distinctions; the simple worked rates remain supplied scenarios.

ACCA's [life-cycle costing discussion](https://www.accaglobal.com/uk/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/target-lifestyle.html) connects early product choices with later production, warranty and closure costs and distinguishes commitment from incurrence. §§4.2 and 4.5 carry that connection into the whole dated account and the future alternative. The amount constrained by design depends on the product; no fixed percentage is presumed. A whole-life allocated cost per unit also does not establish the payment changed by another sale.

The short cohort table exposes unrecovered acquisition; the product continuation explains why whole recovery and an additional-sale comparison can differ. Reopen the affected account when the population, horizon, obligations, resource behavior or supported continuation model changes. For capital-project valuation, use [Value Capital Projects (FIN.6)][FIN6] in the Corporate Finance Principles Framework for the additional financial cash and valuation treatment.

### MA.8:12 - Relations

MA.1–MA.4 supply resource and account meanings, MA.5 the conditional outlook and MA.7 explanations of observed differences. [Financial Domain Modeling (FDM)][FDM] supplies a missing financial position or obligation through FDM.1 and a contractual event or conditional-flow model through FDM.3; FDM.4 establishes the effect of an actual event. OPS.14 and the relevant financial practice consume the future consequences for their comparisons and valuations.

### MA.8:End
