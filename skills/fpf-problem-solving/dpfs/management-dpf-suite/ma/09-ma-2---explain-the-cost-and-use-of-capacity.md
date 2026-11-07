## MA.2 - Explain the Cost and Use of Capacity

**Type:** Architectural

**Status:** Stable

### MA.2:0 - Use this when

Use this pattern when paid capacity, used capacity and apparently idle capacity have been treated as the same thing. A proposed efficiency saving, staff reduction or extra workload often exposes the difference.

The pattern governs an account of resource supply, usable capability, its use and its monetary consequences. It returns an explanation of what is available, what is used or reserved, and what action could change supply or payments.

Use an adequate capacity account directly. The operating choice about the constraint, reserve or feasible schedule belongs to the relevant [OPS][OPS] method.

### MA.2:1 - Problem frame

A team pays for a resource arrangement that supplies capability over time. Some provision can be unavailable for the relevant service; some usable capacity can support actual work; some can protect the service against variation. A remaining unused portion may offer another use or a possible supply change.

These quantities do not have one monetary meaning. Released time can increase available capability without changing the current payment. A supply reduction can save money while also removing capacity needed in another time window.

### MA.2:2 - Problem

An account that prices every unused hour as waste invites a reduction that may damage service. An account that treats every paid hour as available can promise work the resource cannot perform.

The working difficulty is to explain both use and monetary consequence without making an accounting classification decide the operational question.

### MA.2:3 - Forces

A simple utilization ratio is easy to communicate. Its denominator can hide unavailability, capability differences and reserve. A very detailed capacity account can become expensive while still failing to establish a feasible schedule.

A reserve consumes an opportunity to use capacity elsewhere. Its reason and size require an operating judgement; calling it protective cannot by itself justify keeping it indefinitely.

### MA.2:4 - Solution

#### MA.2:4.1 - Define the resource and relevant capacity quantity

Name the resource arrangement, capability, time window and receiving question. Recover the supplied quantity, the unit and the conditions under which it can serve the relevant work. Distinguish staff attendance, machine occupation and elapsed time.

Use the current operating account for availability, commitments and reserve. If those results are disputed, obtain the missing OPS result before attaching a monetary conclusion to them.

#### MA.2:4.2 - Explain the supplied, used and unused portions

Reconcile the supplied quantity with its relevant uses and restrictions. Identify unavailable or differently committed provision, actual or expected consumption, protected reserve and any remaining unused usable capacity. Keep the categories mutually interpretable for this account; reserve can be part of available capacity while being unavailable for ordinary commitment.

Investigate the reason for an apparently idle portion. It may reflect demand variation, a necessary skill mix, downtime, a minimum supplier block or inadequate demand. Preserve a disputed explanation as disputed. A utilization label is an entry cue, not a causal diagnosis.

#### MA.2:4.3 - Connect a capacity change to a supply action

Ask what action would change resource supply and on what terms. Recover notice periods, minimum blocks, alternative uses and consequential payments for the stated horizon.

A saved hour can be used elsewhere if capability and scheduling permit it. A payment saving requires an avoided or reduced payment within the stated horizon. A smaller assigned share of unchanged payroll establishes neither.

Retain the threshold. Removing five hours of work may leave the same supplied shift; adding five can require another whole block. [MA.1](08-ma-1---build-the-resource-consumption-and-cost-model.md) supplies a missing demand model.

#### MA.2:4.4 - Return the capacity and monetary account

Return the quantities, reasons and relevant supply options with their limits. If a unit cost is useful, state its denominator and purpose. Dividing the same payment by supplied, used or productive hours gives different rates.

Supply the supported quantities and payment conditions to OPS for the capacity or incremental decision. Keep uncertainty about the operating reserve separate from uncertainty about a supplier's terms.

### MA.2:5 - Archetypal Grounding

A service purchases 100 scheduled qualified staff-hours for 2,400 in a period. An adequate supplied operating account identifies 20 hours unavailable for the service, 50 used on service work, 10 held as justified reserve and 20 otherwise unused usable hours. The account reconciles **20 + 50 + 10 + 20 = 100**.

Dividing 2,400 by all 100 supplied hours gives 24 per supplied hour. Dividing it by the 50 service hours gives 48 per used service hour. Neither division establishes the payment avoided by releasing another hour.

A changed method releases two service hours. Pay remains 2,400 under the arrangement. The result is two hours of released capability, subject to their actual usefulness in the schedule. Multiplying two by 24 or 48 does not establish a cash saving.

Consider an extra request under the original arrangement, before the method change. It needs 25 hours in the same window. The supplied operating account permits ordinary commitment of only the 20 unused hours while retaining the reserve. A feasible additional block of 20 hours costs 500 under the supplied terms. The model returns the five-hour gap and the block's payment, or the question whether OPS should change the reserve or option. It does not silently consume the reserve to make the request fit.

### MA.2:6 - Bias-Annotation

A high-utilization target can conceal the value of protective capacity; the label “reserve” can conceal unnecessary provision. Examine the actual operating reason and consequence.

The period account does not establish a long-run staffing result. A later horizon can change demand, terms and the feasible supply action.

### MA.2:7 - Conformance Checklist

Examine whether the account identifies the resource, capability, unit and window; reconciles supply with relevant uses and restrictions; retains the operating basis of reserve; distinguishes released capability from changed payment; and names the action and conditions needed for a supply change.

These checks assess the explanation. The existence of paid capacity does not establish a feasible schedule or the adequacy of a reserve.

### MA.2:8 - Common Anti-Patterns and How to Avoid Them

**Booking every released hour as a saving.** Find the payment or opportunity that actually changes.

**Removing reserve because it appears unused.** Obtain the operational consequence of removing it, including the variation it was intended to absorb.

**Comparing utilization rates with different denominators.** Recover what each denominator includes before judging a difference.

### MA.2:9 - Consequences

The user can distinguish an efficiency improvement, unused provision and an avoidable payment. This improves the information supplied to a capacity decision.

The account may leave the operating choice unresolved. That is useful when its remaining question is explicit, such as the needed reserve or the feasibility of a replacement block.

### MA.2:10 - Architectural Rationale

Supply, capability and consumption are separated because each responds differently to action. A single hourly rate can support a defined account, but cannot carry all three meanings.

The accounting method explains quantities and money while OPS decides the operating arrangement. Combining them without preserving that boundary would let a chosen denominator decide what the service can safely promise.

### MA.2:11 - SoTA-Echoing

The selected line combines resource-based managerial costing with the distinction between productive, protective and excess capacity discussed in Tendon and Doiron's *Tame your Work Flow* (2020), chapter 7. It adapts the distinction to the actual operating account: the reason for reserve must be established, and elapsed flow time alone does not identify a constrained resource.

In the historical fixture example in Caspari and Caspari's *Management Dynamics* (2004), a fixture transfers work between stations: it saves five minutes per unit at one station but adds two at the station that limits production. Total processing time falls from 55 to 52 minutes, while wages remain unchanged. When demand uses the limiting station's capacity, increasing its work from 25 to 27 minutes per unit reduces possible output. These contributions inform §§4.2–4.3 and the released-hours example.

At the effort of reconciling one resource pool, this account exposes distinctions a utilization percentage hides. More detailed tracking is worthwhile when a capability or time boundary changes the decision. Reopen the account when those conditions or the supply terms change.

### MA.2:12 - Relations

MA.1 supplies resource demand. MA.3 uses adequate pool meanings for shared assignment; MA.4 reconciles monetary views. OPS supplies constraint, reserve, schedule and capacity decisions and consumes this account's supported quantities.

### MA.2:End
