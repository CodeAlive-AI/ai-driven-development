## MA.2 - Explain the Cost and Use of Capacity

**Type:** Architectural

**Status:** Stable

### MA.2:0 - Use this when

Use this pattern when paid capacity, used capacity and apparently idle capacity have been treated as the same thing. A proposed efficiency saving, staff reduction or extra workload often exposes the difference.

Use the account to explain a payment, determine how much work the resource can support or assess a proposed change. The terms of a paid shift may already settle its price. A promise about the same shift can depend on who may call on it and how soon it can be made available.

Use an adequate capacity account directly. Use the relevant [OPS][OPS] method when deciding about the constraint, reserve or feasible schedule.

### MA.2:1 - Problem frame

A team pays for a resource arrangement that supplies capability over time. Some provision can be unavailable for the relevant service; some usable capacity can support actual work; some can protect the service against variation. A remaining unused portion may offer another use or a possible supply change.

These quantities do not have one monetary meaning. Released time can increase available capability without changing the current payment. A supply reduction can save money while also removing capacity needed in another time window.

### MA.2:2 - Problem

An account that prices every unused hour as waste invites a reduction that may damage service. An account that treats every paid hour as available can promise work the resource cannot perform.

For a question about payment, establish what the supply terms charge. For a question about use or a further commitment, establish the relevant operating conditions. A proposed saving may require both accounts.

### MA.2:3 - Forces

A simple utilization ratio is easy to communicate. Its denominator can hide unavailability, capability differences and reserve. A very detailed capacity account can become expensive while still failing to establish a feasible schedule.

A reserve can displace other valuable work. Count the opportunity forgone when that work could have used the capacity and the reserve prevents it. Some arrangements permit work that can release the resource in time. Consider that use when judging how much reserve to protect and for how long.

### MA.2:4 - Solution

#### MA.2:4.1 - Define the resource and relevant capacity quantity

Name the resource arrangement, capability, time window and receiving question. Recover the supplied quantity, the unit and the conditions under which it can serve the relevant work. Distinguish staff attendance, machine occupation and elapsed time.

Use the operating account for availability, commitments and reserve when the conclusion depends on them. For example, a completed shift payable at a fixed 1,000 costs 1,000 even if use of its two reserve hours was never recorded.

#### MA.2:4.2 - Explain the supplied, used and unused portions

Reconcile the supplied time by counting each interval once. Establish what happened in it when use matters. A reservation also says who can call on the resource and with what notice. During two hours reserved for urgent calls, staff may do work they are permitted and able to interrupt. For a proposed promise, check whether they can release the resource in time for a call and still meet the terms offered for the other work. A promise of two uninterrupted hours needs a different basis from permission to work until a call arrives.

When the cause of apparent idleness matters to the account, investigate it. It may reflect demand variation, a necessary skill mix, downtime, a minimum supplier block or inadequate demand. If the cause is in dispute, say what remains unresolved.

#### MA.2:4.3 - Connect a capacity change to a supply action

Ask what action would change resource supply and on what terms. Recover notice periods, minimum blocks, alternative uses and consequential payments for the stated horizon.

A saved hour can be used elsewhere if capability and scheduling permit it. A payment saving requires an avoided or reduced payment within the stated horizon. A smaller assigned share of unchanged payroll establishes neither.

Retain the threshold. Removing five hours of work may leave the same supplied shift; adding five can require another whole block. [MA.1](08-ma-1---build-the-resource-consumption-and-cost-model.md) supplies a missing demand model.

#### MA.2:4.4 - Return the capacity and monetary account

Return the payment, use or available provision the recipient asked about, with the conditions supporting it. If a unit cost is useful, state its denominator and purpose. Dividing the same payment by supplied, used or productive hours gives different rates.

Supply the supported quantities and payment conditions to OPS for the capacity or incremental decision. Keep uncertainty about the operating reserve separate from uncertainty about a supplier's terms.

### MA.2:5 - Archetypal Grounding

A service purchases 100 scheduled qualified staff-hours for 2,400 in a period. An adequate supplied operating account identifies 20 hours unavailable for the service, 50 used on service work, 10 held idle as justified reserve and 20 otherwise unused usable hours. The account reconciles **20 + 50 + 10 + 20 = 100**.

Dividing 2,400 by all 100 supplied hours gives 24 per supplied hour. Dividing it by the 50 service hours gives 48 per used service hour. Neither division establishes the payment avoided by releasing another hour.

A changed method releases two service hours. Pay remains 2,400 under the arrangement. Whether the two released hours can be used elsewhere depends on the schedule. Multiplying two by 24 or 48 does not establish a cash saving.

Consider an extra request under the original arrangement, before the method change. It needs 25 hours in the same window. The supplied operating account permits ordinary commitment of only the 20 unused hours while retaining the reserve. A feasible additional block of 20 hours costs 500 under the supplied terms. The model returns the five-hour gap and the block's payment, or the question whether OPS should change the reserve or option. The existing reserve stays protected unless the operating decision changes it.

### MA.2:6 - Bias-Annotation

A high-utilization target can conceal the value of protective capacity; the label “reserve” can conceal unnecessary provision. Examine whether the service needs the reserve and what would happen if it were reduced.

The period account does not establish a long-run staffing result. A later horizon can change demand, terms and the feasible supply action.

### MA.2:7 - Conformance Checklist

What settles the recipient’s question about the specified resource and period? Check a payment against its terms and a total of supplied time against distinct intervals. Where the same interval is reserved and partly occupied, examine both facts for a capacity claim. For an additional commitment, check who may release the resource, how quickly and which promises still hold after an interruption.

These checks assess the explanation. The existence of paid capacity does not establish a feasible schedule or the adequacy of a reserve.

### MA.2:8 - Common Anti-Patterns and How to Avoid Them

**Booking every released hour as a saving.** Find the payment or opportunity that actually changes.

**Removing reserve because it appears unused.** Obtain the operational consequence of removing it, including the variation it was intended to absorb.

**Comparing utilization rates with different denominators.** Recover what each denominator includes before judging a difference.

### MA.2:9 - Consequences

The user can distinguish an efficiency improvement, unused provision and an avoidable payment. Supply those distinctions to whoever makes the capacity decision.

The account may leave the operating choice unresolved. That is useful when its remaining question is explicit, such as the needed reserve or the feasibility of a replacement block.

### MA.2:10 - Architectural Rationale

Supply, capability and consumption are separated because each responds differently to action. A single hourly rate can support a defined account, but cannot carry all three meanings.

The accounting method explains quantities and money. Those responsible for operations use OPS to decide what service the available resources can safely provide. The chosen utilization denominator does not establish that capacity.

### MA.2:11 - SoTA-Echoing

The selected line combines resource-based managerial costing with the distinction between productive, protective and excess capacity discussed in Tendon and Doiron's *Tame your Work Flow* (2020), chapter 7. In the operating account, a claim about the protection a reserve affords needs grounds for that protection. A fixed shift charge can be known from the terms of supply. Elapsed flow time alone does not identify a constrained resource.

In the historical fixture example in Caspari and Caspari's *Management Dynamics* (2004), a fixture transfers work between stations: it saves five minutes per unit at one station but adds two at the station that limits production. Total processing time falls from 55 to 52 minutes, while wages remain unchanged. When demand uses the limiting station's capacity, increasing its work from 25 to 27 minutes per unit reduces possible output. These contributions inform §§4.2–4.3 and the released-hours example.

Reconciling one resource pool exposes distinctions a utilization percentage hides. More detailed tracking is worthwhile when a capability or time boundary changes the decision. Reopen the account when those conditions or the supply terms change.

### MA.2:12 - Relations

MA.1 supplies resource demand. MA.3 uses adequate pool meanings for shared assignment; MA.4 reconciles monetary views. OPS supplies constraint, reserve, schedule and capacity decisions and consumes this account's supported quantities.

### MA.2:End
