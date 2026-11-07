## MA.1 - Build the Resource-Consumption and Cost Model

**Type:** Architectural

**Status:** Stable

### MA.1:0 - Use this when

Use this pattern when a cost report cannot explain what a proposed order, changed method or different workload would require. A quote below reported average cost, a claimed labor saving or a sudden rise in unit cost can expose this difficulty. Start by identifying the resource dependency that the existing account leaves unanswered.

The pattern governs a model relating work outputs to resource consumption and monetary amounts for a stated use. Its useful result is enough of that model to explain the relevant quantities, capacity conditions and money. The operating decision can then use [OPS.14][OPS] to compare options.

If an existing model already supplies adequate quantities and conditions, use it.

### MA.1:1 - Problem frame

A service can use a machine, qualified staff, consumables and a supplier's processing service to deliver one accepted result. Each resource has a different relationship to the work. The machine is occupied during setup and processing; staff may supervise only part of that time; consumables may be used on unsuccessful attempts as well as accepted units. A supplier may charge for an attempt, a completed batch or a reserved block.

The money follows further relationships. Stock consumed today may have been paid for last month. Salaried capacity may be available within unchanged pay. Another machine block may require a payment before the customer pays. An internal unit-cost report may also assign a share of the building and management costs. These amounts can all be meaningful while answering different questions.

Management accounting needs an explanation connecting those facts. The relevant boundary follows the work, resource behavior and receiving use; it need not coincide with the chart of accounts or an organizational department.

### MA.1:2 - Problem

A monetary total compresses the relations needed to explain a change. Multiplying average cost by a proposed quantity can miss available capacity, a setup, failed attempts or a supply threshold. It can also turn an allocation into an apparent payment consequence.

A model can cost more to construct and maintain than its additional detail contributes to the receiving use. Its apparent precision can also exceed what the underlying observations support. The working problem is to recover the dependencies that can change this answer and stop at a justified level of detail.

### MA.1:3 - Forces

Consumption, available capability and payment are connected but need different evidence. The person who supplies a credible processing-time estimate may not know the supplier's charging terms or the actual payment date. Bringing these facts together is useful even when each is already recorded elsewhere.

Grouping resources makes an account usable. It loses value when the group hides a capability requirement, a different response to demand or a payment threshold. More detailed observation can reduce a consequential uncertainty, but detailed tracking itself consumes resources and can encourage people to optimize what is easiest to count.

### MA.1:4 - Solution

#### MA.1:4.1 - Begin with the missing explanation

State the work being considered, the relevant result and the period over which the model must answer. Inspect the existing account with its user. Ask what it cannot presently explain: the resources required for another order, the effect of a changed batch size, the cost of unused provision or some other concrete dependency.

Use that question to choose the first observations. For a proposed order, obtain the actual processing route and the conditions under which it works. For a reusable product-cost account, obtain representative routes and the variation the account must retain. Ask the people who perform or arrange the work, and compare their explanation with available operating records. A ledger category locates recorded money; it does not by itself explain how the work consumes a resource.

#### MA.1:4.2 - Recover outputs and resource dependencies

Identify the accepted outputs and the intermediate results that materially consume resources. Recover setups, attempts, rework, inspection and handling where their resource demands differ. Distinguish quantities of accepted results from quantities of attempts: a charge on every processing attempt will not generally equal a charge on every accepted output.

For each relevant resource, express the dependency in meaningful units. A simple relationship may be:

> Required rig-hours = setup hours + processing attempts × rig-hours per attempt.

Other resources can require a table, interval, threshold or conditional rule. A one-time setup, a resource shared by simultaneous tasks and a failure-dependent repeat are not all linear per-unit demands. Preserve the conditions under which each relationship holds, including product type, qualification, batch size or equipment state when these matter.

Establish the reason for the relationship. Engineering knowledge, applicable terms and observations of the process can support different parts of it. Mark an estimate as an estimate and retain the assumption that makes it usable. An observed association between order value and staff expense may help prediction; it does not establish that an extra currency unit of sales consumes a particular staff quantity. When that distinction changes the decision, investigate the mechanism or return the missing dependency.

If the calculation is familiar but you cannot relate its quantities to the account being constructed, use [FPF B.1.5.EW][EW] to locate the missing modeling operation. Obtain that contribution or learn to perform it before relying on the calculation. Greater arithmetic precision does not recover an omitted resource dependency.

#### MA.1:4.3 - Keep resource quantities and supplied capacity distinct

A rig-hour, a qualified staff-hour and an elapsed hour measure different things. Recover what each resource must actually provide. Check that an estimate of machine occupation has not silently become an estimate of staff attendance.

Group resources only while the grouping preserves relevant capability, consumption and money. Two machines can share a pool if their interchangeable capability and behavior suffice for this use. A specialist machine that alone performs a required test needs its own boundary. Likewise, splitting identical consumables by invoice number may add detail without improving the answer.

Compare demand with the supplied capacity conditions for the required time window. Retain commitments to other work, unavailable time and protected reserve. Keep thresholds such as an additional shift, license tier, supplier block or specialist booking visible. Obtain an adequate operating result when feasibility, the constraint or the schedule is unresolved; the cost model uses that result rather than establishing a feasible schedule from a total number of hours. [MA.2](09-ma-2---explain-the-cost-and-use-of-capacity.md) deepens the account when the meaning or cost of capacity itself needs explanation.

#### MA.1:4.4 - Attach the relevant monetary meanings

Connect resource quantities to money through the relationship that actually applies. For each amount that could be misread, make clear whether it is:

- consumption valued for the account, such as materials issued from stock;
- the payment required to supply or obtain a resource, such as a whole additional shift;
- a payment at a particular time; or
- an assigned share under an allocation convention.

The distinction can be carried in ordinary columns or explanatory prose.

A supplied resource can be consumed without another payment in the period. Record the capability used and the account's warranted value without inventing a cash saving or expenditure. Conversely, obtaining a resource block may require paying for more capacity than the proposed work consumes. Use the charging rule for that block. An average rate multiplied by consumed hours does not reproduce every supply arrangement.

Preserve the horizon. A salaried hour whose payment is unchanged this week can still matter to a later staffing decision or to displaced work now. Stock consumption can trigger a replacement payment, use scarce inventory or have another relevant consequence even though the original purchase is sunk. Obtain those facts for the receiving comparison instead of classifying a cost as permanently fixed or variable.

When a shared assignment is the unresolved issue, use [MA.3](10-ma-3---assign-shared-costs-for-the-stated-use.md). When management, reporting and cash amounts appear inconsistent, use [MA.4](11-ma-4---reconcile-operating-reporting-and-cash-accounts.md). These are separate questions that can also be answered from adequate existing accounts.

#### MA.1:4.5 - Choose the detail that can change the answer

Ask which plausible differences could change feasibility, a payment threshold, the comparison or the assurance needed for this use. Split a resource group or obtain another observation when such a difference is concealed. Preserve a justified range when all values in it support the same relevant conclusion.

For example, a setup estimate of six to nine hours may be sufficient if every value requires exactly one additional ten-hour block and fits the supplied arrangement. Measuring setup to the minute adds little to that choice. If the estimate straddles the available capacity, its uncertainty matters: obtain a better bound, change the option or report unresolved feasibility.

This stopping rule applies to the stated use. A model sufficient for one order can be inadequate for a pricing policy, capital decision or assurance claim with a longer horizon. Reuse the established relations, then deepen only the part the new use needs. [FPF C.11.DUA][DUA] supplies the broader inquiry decision when the value of further information is itself disputed.

#### MA.1:4.6 - Return a model someone can use

Return the quantities and dependencies together with the conditions needed to interpret them. A short table can be enough. Make an unresolved premise visible at the point where it changes the result: required qualification, available block, rework rate, supplier terms or another specific issue.

For an operating option, supply the resource and monetary consequences to OPS.14. That method compares options, considers displacement and tests timing and funding. A favorable difference is a result of the comparison under its premises; building the model does not authorize the work or supply missing capacity.

Retain the observations worth reusing and the conditions that would reopen the account. Actual use of a different process, changed terms or a new demand range can require a revision.

When the design itself is unresolved, the model also identifies relationships that participants could change: accepted work to attempts, components to assembly, demand to provision blocks, or service conditions to later support. Distinguish the currently supported relationship from a proposed one. Return these design questions to MA.10 rather than substituting a desired cost for a resource quantity. Once an alternative changes the work or terms, reconstruct the affected relationships here; a model of the previous arrangement does not establish the new one.

### MA.1:5 - Archetypal Grounding

#### MA.1:5.1 - A test order below reported average cost

A test service considers an order for 100 accepted units at 12 currency units each. Its standard report assigns an average cost of 15 per unit. The manager first needs the resource model; the comparison follows from it. The following is a constructed case with supplied operating and contractual facts.

The resource owner supplies an adequate schedule, qualification and reserve account. There are 20 uncommitted usable rig-hours in the required window. Exactly one additional contiguous ten-hour block can be obtained for 240, subject to booking. Setup requires six to nine rig-hours, followed by 0.2 rig-hours per processed unit. One successful attempt per accepted unit is assumed.

The work requires 14 qualified staff-hours; 16 usable hours are already available and pay is unchanged. Materials for this order must be bought now at 2 per unit. A supplier charges 1 per processed unit.

| Recovered dependency | Quantity or amount | What the receiving comparison can use |
| --- | --- | --- |
| Setup plus processing occupies the rig. | 6–9 + 100 × 0.2 = **26–29 rig-hours**. | The supplied 20 hours are insufficient; one extra ten-hour block makes the supplied arrangement adequate. |
| Qualified staff support the work. | **14 staff-hours** within the supplied 16. | The option uses capability, with no additional wage payment under these terms. |
| Materials are consumed and purchased for the order. | 100 × 2 = **200**. | A payment of 200 now. |
| The supplier charges per processing attempt. | 100 × 1 = **100**. | A payment of 100 under the one-attempt premise. |
| Extra rig capacity is sold as one block. | **240** for the ten-hour block. | A payment of 240, although the extra occupation is only six to nine hours. |
| The existing report assigns average cost. | 100 × 15 = **1,500**. | A reported amount whose assignment basis remains available for its own use. |

The model supplies **540** in additional payments. OPS.14 compares the 1,200 receipt with those payments: the difference is **660**, over a horizon that includes both, with all other flows unchanged and no displaced contribution. The reported 1,500 does not establish this incremental amount.

Payment time changes what is feasible. Without the order, unrestricted cash available for these payments would remain **500 through day 28 after all other receipts and obligations**. Materials and the block require 440 now, leaving 60. The supplier's 100 is due on day 7; the customer pays on day 28. There is therefore a **40 funding gap on day 7**. The operating or finance decision must resolve that gap before treating the option as funded.

If an additional receipt of 50, unchanged between accepting and declining the order, instead arrives before day 7, cash after both payments is **10**. The order's incremental difference remains 660. The unchanged receipt cancels from that difference but changes the whole cash position used to establish payment feasibility.

The setup interval is sufficient for the one-block question: 26–29 hours always lies within the supplied 30. A new product requiring an eleven-hour setup would require **31 hours**. That case reopens feasibility and the resource model; the earlier result cannot be extended by merely changing the sales quantity. Failed attempts, different staff qualifications or changed supplier terms likewise require attention where they affect the dependencies.

#### MA.1:5.2 - A faster method with unchanged wages

A repair method reduces salaried technician attendance from six hours to four for one job. The two released hours become usable capability if the schedule and qualification allow their use. Pay this week remains unchanged.

The model returns the two-hour reduction and the unchanged payment. If another valuable job can use the released time, OPS.14 can compare the resulting options. If no work is displaced and no payment changes, the model provides no current cash saving. For a later staffing question, construct the relevant demand and supply relationship over that later horizon.

#### MA.1:5.3 - Correct arithmetic in an incomplete resource account

Return to the test order with a nine-hour setup. Suppose obtaining 100 accepted units now requires 20 additional unsuccessful attempts. Each of the 120 attempts occupies the rig for 0.2 hours, and there is no extra setup. Counting only accepted units gives 9 + 100 × 0.2 = 29 hours; retaining every attempt gives **9 + 120 × 0.2 = 33 hours**. The supplied 30 hours are insufficient. The supplier's charge also rises from 100 to 120 under its per-attempt rule. A revised payment comparison must retain this change as well as the unresolved capacity.

While doing that multiplication, the accountant is deriving rig demand and constructing the order's resource account. The accepted-output requirement governs which attempts must enter the calculation. A colleague may supply the process relationship when the accountant cannot establish it; the accountant still needs to understand how that contribution affects the model. Repeating multiplication exercises would not supply the missing relationship.

The observed production attempts belong to the work being modeled. They are not constituent acts of the accountant's model construction.

Return the changed demand to the operating comparison. [OPS.11.1][OPS] can recover the routing, shared-resource and completion conditions when a different operating arrangement is needed. Recalculating existing assignments or changing an authorized allocation is an operating question. [OCE][OCE] becomes relevant if the proposed repair changes who may commit resources or other organizational arrangements.

### MA.1:6 - Bias-Annotation

An accountant may favor categories already present in the ledger; an operator may favor the resource easiest to observe. Both can miss the relation that changes the answer. Compare their accounts around the actual work and keep different units explicit.

The order example concerns a commercial service and a short horizon. Its arithmetic does not establish that profit is every organization's purpose or that all long-run choices can be made from short-run payments. Public and internal services can use the same construction to explain required resources while obtaining their objectives and decision criteria from the responsible practice.

### MA.1:7 - Conformance Checklist

For the model's stated use, examine whether:

1. The work, output and horizon are clear enough to choose the relevant dependencies.
2. Attempts, setups, resource units and capability boundaries are retained wherever they can change the answer.
3. The relationships have adequate support, with material estimates and unresolved assumptions identifiable.
4. Capacity conclusions use an adequate supplied operating account, including commitments, reserve and relevant thresholds.
5. Consumption values, supply payments, timing and allocations can be distinguished where their meanings affect use.
6. The chosen detail preserves the consequential variation, and the returned result names any premise still needed by its recipient.

A plausible entry cue establishes a reason to inspect the account. These questions assess the model and its warranted use; observing actual consumption, obtaining a resource and achieving the business result require their own evidence.

### MA.1:8 - Common Anti-Patterns and How to Avoid Them

**Rejecting an order from the average-cost multiplication alone.** Recover what changes when the order is undertaken, including the capacity and payment conditions. Keep the original report's meaning available.

**Valuing every released hour as an avoided wage payment.** State the released capability and the action, if any, that changes payment or displaced work. An unchanged salary cannot be saved merely by assigning it fewer hours.

**Refining a harmless decimal while concealing a threshold.** Preserve the supply block or qualification boundary first. Add measurement detail only where its plausible variation can change the use.

**Using paid capacity as proof of timely availability.** Obtain the actual usable and committed capacity for the required window. Payment for a resource does not establish the schedule.

### MA.1:9 - Consequences

The user can explain why a proposed workload consumes particular resources and why its monetary consequences differ from a report. The result supports a small first decision and can be extended when another use needs more detail.

The model also exposes missing operational or contractual facts that accounting categories previously concealed. Recovering those facts has a cost. Keeping only consequential detail reduces maintenance, while explicit conditions make later reuse more demanding than copying a single unit-cost number.

### MA.1:10 - Architectural Rationale

The construction begins with work and quantitative dependencies because a money total cannot recover a lost capability requirement or setup. Monetary interpretation follows the relevant resource relation. This order also lets an existing operating account supply a sufficient quantity directly.

A report based on a stable average can be adequate for the question it was designed to answer. Replacing it is justified when its aggregation conceals an answer-changing relation. A comprehensive activity model can support repeated heterogeneous decisions, but its collection and maintenance burden is unnecessary for a small case whose decisive relations are already known.

Keeping the model separate from the option comparison makes both usable independently. The same model can support a forecast or variance explanation; the same comparison method can use an already adequate model. A longer horizon or different decision changes the needed relationships rather than making one cost label universally correct.

### MA.1:11 - SoTA-Echoing

The practical question is how much resource and monetary structure an internal account needs to support its use. The selected line combines causal management-cost modeling with the constraint-accounting distinction between consumed capability and payments. It adapts IMA's [Developing an Effective Managerial Costing Model][IMA2019]: model resources and their quantitative dependencies, distinguish their monetary treatment, and choose sophistication for the decision. Here those contributions change the construction and detail decision in §§4.2–4.5.

At the effort of recovering a few consequential relationships, this line can distinguish the extra capacity block from a reported average that obscures it. A detailed activity or time-driven model becomes preferable when repeated decisions need the distinctions it supplies and their maintenance is worthwhile. Its use still needs adequate capacity and monetary premises.

Bragg's *Throughput Accounting* (2007), printed pp.44–47 and 84–86, supplies historical examples and assumptions behind short-run comparisons. The pattern retains their attention to changed payments and capacity, while including supplier charges, setup supply and other changed flows when actual terms require them. Caspari and Caspari's *Management Dynamics* (2004), printed pp.1–11, supplies the counterexample in which local time reduction need not improve the constrained system or reduce wages. These sources inform the returned quantities and the faster-method case.

Reconsider the model when observed work, relevant terms or the receiving use defeats its dependency, capacity or detail assumptions.

### MA.1:12 - Relations

[OPS.14][OPS] consumes adequate resource quantities, monetary consequences and conditions for its incremental comparison. The relevant OPS capacity and scheduling methods supply an unresolved operating result. [OPS.15][OPS] supplies operating-account definitions and source events where those are missing.

MA.2 explains capacity use and its cost; MA.3 resolves shared assignment; MA.4 reconciles differing accounts. MA.5 can reuse the dependencies in a forecast, MA.7 in a variance explanation and MA.8 in a cohort or product account. Each is entered for its own unresolved question.

[FPF C.16][MEAS] supplies measurement discipline when a quantity's meaning or evidence is disputed. C.11.DUA supplies the inquiry decision when further information could change the action.

### MA.1:End
