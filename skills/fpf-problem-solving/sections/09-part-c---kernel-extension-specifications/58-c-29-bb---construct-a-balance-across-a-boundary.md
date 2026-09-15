## C.29.BB - Construct a Balance across a Boundary

> **Type:** Method
> **Status:** Draft
> **Normativity:** Normative

### C.29.BB:1 - Problem frame

Use this pattern when a total changes and you need to construct the relation between that change, transfers across a chosen boundary, and creation or removal within it. The difficulty may be choosing what belongs inside, combining accounts for parts, or understanding why a balance changes after the boundary is redrawn.

Two tanks can gain less liquid than their external inflow minus outflow suggests because some liquid remains in their connecting line. A job moving between two stages changes their separate counts while leaving the total unfinished count unchanged. A computation can introduce a discrepancy if two cells use different amounts for their shared transfer.

The Method constructs a balance for a chosen additive quantity over a specified interval and collection of parts. Its first result can be a predicted total, a bound, a missing-transfer question, or a computational update that preserves the supplied balance. The construction may describe a physical region, a defined population or a mathematical partition; identify which one answers the working question.

The reader needs the quantity's meaning and enough arithmetic to combine amounts with signs. A physical application also needs the relevant storage and transfer laws. A rate or field calculation needs the calculus used by that model.

If a complete, applicable balance already answers the question, use it. This pattern is useful when the balance itself must be built or revised. Detailed transport laws, reaction models and numerical solvers remain contributions of their respective subject Methods.

### C.29.BB:2 - Problem

A plausible equation such as “change equals input minus output” can leave its subject undecided. The chosen parts may overlap, an intermediate store may be omitted, or two records may count the same transfer at different times. A selected quantity may also be created or removed within the boundary: the number of unfinished jobs changes when a job is completed, while the amount of a conserved material follows a different law.

Adding local equations works only after their quantities, intervals and shared transfers have been made compatible. Otherwise cancellation can hide a missing store or combine values that cannot be added.

### C.29.BB:3 - Forces

| Force | Tension |
| --- | --- |
| Useful total | A coarse amount can answer a capacity question while hiding the local peak needed by another decision. |
| Boundary choice | A smaller region is easier to observe; a larger one can turn uncertain exchanges into internal transfers. |
| Additivity | Summing parts is simple when the quantity has an additive meaning; overlapping populations or intensive variables require another construction. |
| Incomplete information | A bound may settle the decision even when individual transfers remain unknown. |
| Computational preservation | A model can obey a balance while its implementation uses incompatible transfer amounts. |

### C.29.BB:4 - Solution

Choose the quantity and boundary, account for changes in each included part, and combine only matching transfers. Use the resulting balance to answer the question at the needed resolution.

#### C.29.BB:4.1 - Choose an additive quantity and a common interval

Name the quantity Q, its unit or counting rule, the included parts S, and the start and end conditions. Define who or what belongs to each part. Use disjoint parts, or otherwise account for their overlap before summing.

For disjoint parts with amounts q_i, additivity means that Q(S) = sum q_i. The rule needs a basis in the selected model or counting definition. For a population, assigning each included job to one stage can provide it. For physical storage, use the appropriate physical quantity and law.

An average temperature is not an additive heat store. If the question concerns stored thermal energy, construct that quantity from the material and state relations; if it concerns the maximum temperature, preserve the local temperatures needed to obtain the maximum. Choosing a convenient sum changes the question unless the required result can be recovered from it.

Keep all amounts on the same interval. A transfer that leaves one store before the endpoint but reaches another afterward requires an in-transit store or separate boundary crossings. For snapshots at different times, first recover their relation to the requested interval.

#### C.29.BB:4.2 - Identify transfers and internal production or removal

For each included part, distinguish the amount crossing into it, the amount crossing out, and the change created or removed within it under the chosen quantity definition.

Orient each transfer once. When a transfer from part i to part j removes amount f from i and adds the same amount to j over the common interval, use -f and +f in their accounts. If a connector stores some of the quantity, its incoming and outgoing amounts can differ; represent that store or retain both crossings.

Production and removal depend on the quantity. A reaction can change the amount of one chemical species within a vessel. Completing a job removes it from the population of unfinished jobs. Determine those terms from the relevant physical or counting rule. Assign each contribution once: classify completion as a crossing out of the population or as removal under its counting rule, and use that convention throughout.

Do not set an unobserved term to zero merely because the first diagram omitted it. Use a supplied law, a justified approximation, a bound, or an unresolved term according to what the answer needs.

#### C.29.BB:4.3 - Combine the local balances

Write each included part's change using the selected terms. Sum those equations. Matching internal transfers cancel, leaving

    Q(S, t1) - Q(S, t0)
        = total inward transfer - total outward transfer
          + internal production - internal removal.

The transfer terms are amounts over the interval. A rate must be integrated over that interval, or multiplied by its duration when the rate is constant. The signs follow the chosen boundary.

For a differentiable rate model, the corresponding instantaneous relation is

    dQ(S,t)/dt = inward rate - outward rate + production rate - removal rate.

Use the finite-interval form for discrete events or when a rate description adds no help. If the selected boundary moves, count crossings relative to that moving boundary using the appropriate transport relation.

A closed boundary eliminates crossing terms only when the model excludes those exchanges. Constancy of Q additionally requires net internal production and removal to cancel. Preserve that premise in any conservation conclusion.

#### C.29.BB:4.4 - Redraw the boundary by reclassifying the same exchanges

When enlarging S, include the added stores and their changes. Transfers between the old and added parts become internal only if both sides now refer to the same amount over the interval. The new exterior crossings remain.

When shrinking S, formerly internal transfers can become inputs or outputs. Recompute the requested total from the retained stores. A balance for a larger region supplies its total; obtaining a smaller region's value still needs the removed region's amount or a sufficient bound.

Check the two descriptions against each other: the larger total equals the sum of its disjoint parts, and their changes agree after shared transfers cancel. This comparison can expose an omitted connecting store without resolving every internal rate.

Changing the parts over time can also change membership. Include that effect through boundary crossings or a suitable population rule; keep it visible when comparing successive totals.

#### C.29.BB:4.5 - Use uncertainty or discrepancy to choose the next move

Substitute the available amounts and compute the requested consequence. If some terms are bounded, propagate the bounds through the signed sum. Preserve dependencies when independently combining endpoints would admit impossible combinations.

For observed values, define the discrepancy as observed change minus the change predicted by the included terms. A nonzero discrepancy establishes disagreement between those accounts. Its cause can lie in an omitted store or transfer, incompatible timing or units, a faulty observation, or an inadequate law. Use the working situation to choose a discriminating next observation or model change.

Resolve a remaining term only when it can change the answer enough to justify the work. A supported bound that settles the current decision is already a usable result. An unresolved cause can remain open when the decision tolerates the resulting uncertainty.

#### C.29.BB:4.6 - Preserve the balance in a computation and return its result

When implementing a partitioned calculation, represent a shared transfer consistently on both sides. Use the same orientation, interval and quantity conversion. Recover total amounts with the appropriate cell volumes or population weights before comparing them.

Derive the aggregate change from the proposed updates. If a numerical approximation changes the balance, determine whether the discrepancy fits the receiving use or repair the update. Balance preservation addresses one property of the computation; accuracy of the local solution requires its own approximation argument.

Return the total, bound or identified missing contribution with the quantity, boundary and assumptions needed to use it. A subsequent question about a local maximum, delay or possible action may require the retained component account. Keep that account available rather than treating the total as a substitute for every question.

### C.29.BB:5 - Archetypal Grounding

#### C.29.BB:5.1 - A transfer line changes which balance answers the tank question

Use a constant-density liquid, measured by volume in litres. At the start, tank A holds 30 L and tank B holds 10 L. Over the chosen interval, an external supply adds 12 L to A, and an external outlet removes 7 L from B.

First suppose the line transfers 15 L from A to B with no change in its liquid content. Then

    A: 30 + 12 - 15 = 27 L
    B: 10 + 15 - 7 = 18 L
    A+B: 40 + 12 - 7 = 45 L.

The internal 15 L cancels. The larger balance gives the combined amount without needing that internal transfer, while the separate balances give each tank's amount.

Now change the condition: the line begins empty, receives 15 L from A, delivers 13 L to B, and retains 2 L. The results become

    A: 27 L
    B: 10 + 13 - 7 = 16 L
    line: 0 + 15 - 13 = 2 L.

The two tanks contain 43 L. Their boundary excludes the line, so 15 L leaves that boundary and 13 L re-enters. The combined tank change is 12 - 7 - 15 + 13 = 3 L. Including the line gives 45 L and recovers the five-litre increase from the external exchanges alone.

If the line's increase is known only to lie between 0 and 2 L, the final tank total lies between 43 and 45 L. This bound settles a request for at least 42 L in the tanks. A request for at least 44 L needs a tighter bound or the line's actual content. No additional observation is required for the first request.

#### C.29.BB:5.2 - Moving and reworking a job preserve one count but change its distribution

Count accepted jobs that have not yet been completed. Each job occupies one of two stages, including any processing position in that stage. Initially A contains 6 jobs and B contains 4.

During an interval, 12 new jobs arrive at A, 9 move from A to B, and 7 are completed at B. With no other arrivals, completions or membership changes,

    A at end = 6 + 12 - 9 = 9
    B at end = 4 + 9 - 7 = 6
    unfinished total at end = 10 + 12 - 7 = 15.

A limit of 12 unfinished jobs is therefore exceeded at the endpoint. Determining whether the limit was exceeded earlier requires the event history or a bound on its prefixes.

If 2 of B's remaining jobs return to A for rework before the endpoint, the stage totals become 11 and 4; the unfinished total remains 15. The extra work is consequential, but moving the same jobs changes their distribution rather than their count.

If the question instead counts separately created work orders, specify that new population and its creation rule. A parent job and two newly opened orders cannot be mixed into the earlier job count without changing its meaning. The next operations-management question may need workload or completion-time modeling in addition to this balance.

#### C.29.BB:5.3 - One shared transfer preserves the computational total

Two computational cells store amounts 10 and 20. One step adds 5 from outside to cell A, removes 2 from cell B, and transfers 3 from A to B. Using one transfer amount gives

    A' = 10 + 5 - 3 = 12
    B' = 20 + 3 - 2 = 21
    A' + B' = 33 = 30 + 5 - 2.

Suppose A subtracts 3 but B adds 2.9. The resulting total is 32.9; the inconsistent interface updates lose 0.1 in that step. Repairing the shared amount restores the aggregate balance. Whether the transfer approximates the intended transport well remains a separate question.

Now let both sides use 2.9. The result is A'=12.1, B'=20.9 and total 33. The aggregate balance holds, but the supplied transfer of 3 requires the local values 12 and 21. Agreement between the two interface amounts preserves the total; their accuracy must still be established for the requested local result.

If the cells store average densities, first multiply by their volumes to obtain the amounts. Summing unequal-volume cells' densities would test another quantity.

### C.29.BB:6 - Bias-Annotation

The storage examples make additivity easy to see. Apply it elsewhere only with a corresponding quantity definition. For a count of file copies inside the chosen boundary, making one additional copy adds one through internal production.

The job example is a pathwise counting account. It introduces no arrival distribution, steady-state condition or claim that all jobs require equal effort. Those assumptions become relevant only for further questions that use them.

### C.29.BB:7 - Conformance Checklist

- [ ] The quantity, units or counting rule, included parts and common interval are sufficient to identify the requested total.
- [ ] Additivity is justified for those parts, with overlap or in-transit storage accounted for where present.
- [ ] Each crossing and internal production or removal term has its meaning and sign; only matching internal transfers cancel.
- [ ] A changed boundary includes the added or removed stores and reclassifies the affected exchanges.
- [ ] The returned value or bound supports the stated question. Any unresolved discrepancy retains its uncertainty instead of being assigned an unsupported cause.
- [ ] When a computation is used, its aggregate update has been derived with the correct weights and shared transfers.

### C.29.BB:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
| --- | --- |
| **The connector disappears.** The tanks are combined while the line's changing content is omitted. | Include the line or retain its two crossings and storage difference. |
| **Similar numbers are added.** Temperatures or overlapping job populations are summed as a stored amount. | Construct an additive quantity or retain the local values required by the question. |
| **A discrepancy is named a leak.** Incompatible endpoints or transfer observations are never examined. | Compare the accounts and choose a discriminating check when its result matters. |
| **Local updates disagree.** The two sides of a computational interface use different transferred amounts. | Share the amount or provide a compatible conversion, then derive the aggregate update again. |

### C.29.BB:9 - Consequences

A well-constructed boundary can remove the need to know complicated internal exchanges. A second boundary can locate where missing storage or transfer information matters. The same construction supports physical balances, defined counts and numerical preservation tests.

The total compresses information. Local capacity, spatial extremes, causal response and completion time can remain unresolved even when the aggregate balance is sufficient for its own question. Retaining the component account makes those further inquiries possible.

### C.29.BB:10 - Architectural Rationale

The independent difficulty is constructing what is added and what cancels. Once compatible local equations are supplied, summing them is elementary; selecting parts, quantities and shared exchanges is the substantive work that makes the sum useful.

A.3.3.TR constructs state-change rules and already demonstrates cancellation of internal forces. This pattern develops the choice and revision of a balance boundary across different quantities and descriptions. C.29.1 handles result transfer between mathematical accounts; the present construction explains why one particular aggregation preserves a total and what must be restored for a smaller-boundary question.

The finite-interval relation is the first construction because it works for discrete events as well as physical storage. Differential and field forms require the subject's regularity and transport assumptions. This separation keeps an elementary count accessible while leaving richer physical and numerical constructions available.

### C.29.BB:11 - SoTA-Echoing

[OpenStax, University Physics Volume 1, §14.5](https://openstax.org/books/university-physics-volume-1/pages/14-5-fluid-dynamics) derives fluid continuity from mass flow and uses constant density to pass to volume flow. Adopt the need for a physical quantity basis; adapt the simple equal-flow case by retaining changing storage in the selected region.

[Sonin, On Choosing and Using Control Volumes (2001), Methods 1–6](https://ocw.mit.edu/courses/2-25-advanced-fluid-mechanics-fall-2013/1657c64b3737c8d35e5905ea21702c6b_MIT2_25F13_On_Choo_and_Usi.pdf) compares fixed and moving boundaries for the same piston-driven flow. The constructions obtain the same exit speed while changing accumulation and crossing terms; a boundary through the piston makes one formulation require a density-discontinuity treatment. Use this established control-volume Method when its continuum quantities and mathematical preparation fit the question. The finite construction in :4 also serves event counts and partitioned computational updates.

[Ketcheson, LeVeque and del Razo, Riemann Problems and Jupyter Solutions, “Finite volume methods”](https://www.clawpack.org/riemann_book/html/Approximate_solvers.html#Finite-volume-methods) obtains aggregate conservation by weighting cell averages and canceling neighboring fluxes. Adopt compatible interface transfer in a numerical update. The book's approximate-solver construction supplies additional transport and approximation methods beyond this balance test.

For the changed tank question, compare two adequate accounts with the same supplied interval amounts and elementary arithmetic. Direct accounting at the tank boundary uses the line's 15 L departure and 13 L arrival to obtain 43 L. Accounting over tanks plus line gives 45 L; recovering the tank amount then needs the line's final 2 L store. Choose the account whose needed quantities are available. Applying only the outside exchange to A+B gives the wrong 45 L answer because it omits the line's increase. If an applicable balance already answers the question, another account adds no benefit.

The boundary-revision procedure and the tank and job continuations are a conceptual synthesis of additive accounting, physical storage and computational conservation. Detailed continuum transport, chemical reaction accounting and stochastic queue models need their own subject Methods.

Reconsider the quantity, boundary or balance form when membership changes, needed storage information is unavailable, boundary motion changes the crossing law, or a cheaper adequate construction becomes available.

### C.29.BB:12 - Relations

- **C.29 - Mathematical Lens Use:** identifies the subject correspondence and the consequences that may be carried back from the mathematical balance.
- **A.3.3.TR - Construct a Rule for State Change:** supplies the broader construction of state evolution; this pattern develops an additive change account.
- **C.29.1 - Mathematical Result Transfer:** preserves operations and requested results when changing mathematical accounts, including an aggregation that loses local values.
- **C.29.2 - Computational Formulation:** constructs the computation and its approximation conditions; the balance test here checks its aggregate update.
- **B.5.MPC.R:** coordinates a changed question across physical, mathematical and computational accounts when revising the balance requires more than an arithmetic update.
- **E.18.2 - Transformation Flow Mathematical Description:** applies when the balance mathematically describes a selected transformation-flow structure or network.
- **C.11.DUA:** helps decide whether resolving a remaining discrepancy or term can improve the available action enough to justify the effort.

### C.29.BB:End
