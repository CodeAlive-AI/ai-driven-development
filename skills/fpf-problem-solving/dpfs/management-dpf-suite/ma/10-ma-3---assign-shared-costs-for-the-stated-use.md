## MA.3 - Assign Shared Costs for the Stated Use

**Type:** Architectural

**Status:** Stable

### MA.3:0 - Use this when

Use this pattern when a shared cost must be assigned to products, customers or units, or when an assigned amount is being interpreted as something its recipient caused or can avoid.

For a shared-cost assignment, return the requested charges under the applicable source pool and rule. For a claim that a payment will disappear if one activity stops, establish what the provider’s terms and resource decisions would actually change. A full allocation is due when the recipient needs charges for the whole pool.

If the current assignment is adequate for its use, retain it. An incremental choice can often use actual changed flows without allocating every shared cost.

### MA.3:1 - Problem frame

A shared resource supports several recipients. Some consumption can be traced to a recipient; some sustains the group or cannot be separated at warranted effort. A reporting, pricing, charging or responsibility question can still require a distributed total.

The need to assign money does not establish that one assignment rule answers all those purposes. A contractual charging convention can be valid for billing while being inadequate as evidence of avoidable cost.

### MA.3:2 - Problem

An allocation makes an account add up, which can give the assigned number an unwarranted causal meaning. Closing a segment can then appear to avoid a payment even when the payment for the shared resource stays unchanged and only its allocation among the remaining segments changes.

When the receiving use requires an assignment, supply it and explain what the assigned amounts mean.

### MA.3:3 - Forces

Tracing can improve the account but has a measurement cost. Convenient drivers are cheap and can be misleading. More precise allocation does not establish a payment consequence when the shared supply remains unchanged.

Recipients can influence both the rule and recorded use. An apparently technical choice can therefore change incentives or who bears a charge.

### MA.3:4 - Solution

#### MA.3:4.1 - Establish the receiving purpose and source total

Start with the decision and the amount in question. If the manager asks how much of a supplier payment would disappear, follow the payment terms through the proposed change. A fixed payment throughout the horizon can settle that question. To assign a charge to a product, customer or unit, identify the rule, source pool, period and resource meaning relevant to that assignment.

Separate pools where their cost behavior or accounting treatment matters. To distribute an entire pool, reconcile its total and account for any residual. For an individual charge, apply the governing rule to the facts it actually uses. A contract can fix a charge per member, per unit used or as a share of the pool. Each basis calls for different information.

#### MA.3:4.2 - Trace what the evidence supports

Trace the consumption attributable to each recipient when the inquiry or charging rule uses consumption. A fixed charge for connection can be established from the agreement and membership alone. Use MA.1 for missing resource dependencies and MA.2 for a disputed supply or capacity meaning.

Retain joint or sustaining costs at the level their explanation supports when the receiving purpose allows it. A sales-value percentage can be an allocation convention; it does not establish resource consumption merely because it correlates with a recipient's size.

#### MA.3:4.3 - Make a necessary convention explicit

When the receiving purpose requires distribution beyond supported tracing, select or obtain the rule appropriate to that purpose. State the basis and why it is usable here. An applicable agreement or reporting rule may determine it.

Apply the rule consistently to the defined source total and recipients. Retain rounding, excluded items or residuals where they affect reconciliation. Distinguish a change in the total from a change in its assignment.

Where plausible rules could change a consequential interpretation, show that sensitivity or return the disputed rule.

#### MA.3:4.4 - Return the assignment with its warranted interpretation

Return the amount or bound the recipient asked for, how it was established and the period it covers. For an assignment, show which part follows from traced use and which follows from a convention. For a full distribution, include its reconciliation to the source total.

If someone proposes an avoidance or closure conclusion, identify which payments or opportunities that claim concerns. An unchanged contract can settle the question about one charge. Use MA.1–MA.2 and OPS.14 when the full decision depends on further changes. MA.9 examines the assignment's behavioral consequences when they are the unresolved question.

### MA.3:5 - Archetypal Grounding

A shared support arrangement costs 1,200 per period. Its supplied terms keep the payment unchanged if either segment closes during this horizon. A required internal charge uses observed support-hours: six for A and four for B. The agreed assignment is therefore **720 to A and 480 to B**.

A has revenue 900 and other avoidable payments of 300. B has revenue 700 and other avoidable payments of 200. After the shared assignment, A shows **−120** and B **20**; together they show **−100**.

If A closes and all other conditions remain unchanged, the group loses its 600 contribution while the shared payment remains 1,200. B's remaining account is **700 − 200 − 1,200 = −700**. The assigned loss of 120 did not identify a 720 payment saving.

If a permitted supply change instead avoids 300 of the shared payment in the relevant horizon, include that changed amount. The comparison now differs by **−600 + 300 = −300**, under the stated remaining premises. Use OPS.14 to make the choice with any further displacement, timing and feasibility consequences. Reallocating the same 1,200 does not supply this change.

### MA.3:6 - Bias-Annotation

A recipient can prefer a driver that lowers its charge. An analyst can prefer measurable activity even when it poorly explains the resource pool. Show the purpose of the assignment and the evidence for its driver.

The example uses an agreed internal convention.

### MA.3:7 - Conformance Checklist

For a charge, can the recipient establish the period, the rule and the facts that determine its amount? For a full distribution, do the assigned amounts and explicit residuals reconcile to the pool?

For a question about an avoidable payment, does its amount or a sufficient bound follow from the change in the relevant terms and work? Making a decision about closing a whole activity can require additional consequences.

### MA.3:8 - Common Anti-Patterns and How to Avoid Them

**Saving an allocated share by deleting its recipient.** Inspect which payments and opportunities disappear.

**Calling a convenient driver causal.** Establish the consumption relationship or label the warranted convention.

**Forcing every sustaining cost onto a unit.** Retain its supported level when the receiving purpose permits; allocate further only for a use that needs it.

### MA.3:9 - Consequences

The user obtains an assignment that can be reconciled and interpreted. Different accounts can serve their stated purposes. An assigned share alone does not show which payments or opportunities would change.

The rule can distribute burden and affect behavior. Its maintenance and measurement cost must be justified by the use it serves.

### MA.3:10 - Architectural Rationale

Purpose precedes the assignment rule because tracing, internal charging and a required reporting allocation have different standards of adequacy. Reconciliation preserves the total; the explanation preserves the assigned amounts' meaning.

A single stable driver is adequate when it serves the agreed purpose. A more detailed model becomes useful when heterogeneity changes that use. Neither removes the need to establish actual changed flows for a closure decision.

### MA.3:11 - SoTA-Echoing

The selected line uses managerial costing's separation of supported consumption from attribution and the throughput-accounting warning about average or allocated amounts in an incremental choice. Bragg's *Throughput Accounting* (2007), printed pp.44–47, supplies historical pricing and allocation examples; MA.1 supplies the quantitative resource construction used here.

The adaptation retains an allocation when the receiving purpose needs it, while withholding an unsupported avoidance interpretation. In the segment example, compare the contribution lost on closure with any shared payment that can be avoided. The assigned charge alone gives neither amount. Reopen the assignment when its purpose, source pool, consumption evidence or applicable rule changes.

### MA.3:12 - Relations

MA.1–MA.2 supply consumption and capacity meanings. MA.4 reconciles different accounts; MA.7 explains a changed assignment or cost; MA.9 examines resulting incentives. OPS.14 uses actual incremental consequences for the operating comparison.

### MA.3:End
