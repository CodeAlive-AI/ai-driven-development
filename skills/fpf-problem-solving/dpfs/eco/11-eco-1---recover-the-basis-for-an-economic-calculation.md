## ECO.1 - Recover the Basis for an Economic Calculation

> **Type:** Method pattern
> **Status:** Stable

### ECO.1:1 - Problem frame

Use this pattern when a calculation ranks production or service plans but you cannot tell whether its prices and other weights represent exchanges and resource uses available to the people who must act. Start with the quantity that could reverse the choice and ask what transaction, displaced use or stated valuation gives it meaning. The result is a comparison with usable economic grounds, or a conditional choice with the missing ground exposed.

An adequate current quotation and resource account can be used as supplied.

### ECO.1:2 - Problem

An optimizer can solve the problem it receives while its numbers conceal the decisive difficulty. An internal transfer price may express a management policy; an old purchase price records a past exchange; a shadow price expresses a marginal trade-off within a particular optimization problem. Substituting one for another can rank alternatives which nobody can actually obtain.

Economic calculation also has a scope. Monetary results describe consequences under particular exchange conditions and rights. They do not add different people's satisfactions into a common measure or establish physical feasibility.

### ECO.1:3 - Forces

The calculation must be simple enough to use but faithful to the alternatives actually open. Prices help coordinate heterogeneous resources without collecting everyone's knowledge. Novel arrangements may have no established price; withholding every decision until they do can be as costly as inventing a market quotation.

### ECO.1:4 - Solution

#### ECO.1:4.1 - Recover the decision and the consequential numbers

Name the actor's choice, the useful result sought and the period in which resources must be available. Separate alternatives that produce different results or leave different obligations. Reuse the resource and cash-flow account already prepared by MA or FIN.

Follow only numbers whose interpretation can change that choice. For each, ask what it denotes: an offered exchange, a past transaction, a budget allocation, an anticipated future exchange, a forgone alternative or a weight in a model. Recover the quantity, quality, location, time and access conditions that matter. “Steel at 500” is not yet a price for a specified supply.

#### ECO.1:4.2 - Connect the comparison to feasible exchange and use

For an offered exchange, determine what can be obtained at the stated terms and by whom. A quotation for an incompatible specification or unavailable delivery window cannot supply this plan. A supplier's offer remains an offer until the relevant commitment is made.

For a resource already controlled, identify the alternative use actually displaced. Its historic cost and its current economic consequence may differ. For a novel resource or arrangement, use a comparable offer only after stating the difference that matters; otherwise retain a conditional value or compare physical alternatives and purposes directly.

Keep a model's weights attached to its objective and constraints. A shadow price can show which constraint is costly within that model. Calling it money does not establish a buyer, a supplier, an exchange or a right to obtain resources at that amount.

#### ECO.1:4.3 - Return the comparison that the grounds support

Pass the usable quantities and timing to the existing accounting or financial calculation. State separately any important result that is not represented in the monetary account, such as preserving access for an affected community. The decision may use several criteria and leave alternatives incomparable.

If a missing price could change the answer, choose an attainable next move: seek a relevant offer, propose an exchange through ECO.3, compare a bounded range, or choose from already sufficient physical and purpose-based grounds. Additional investigation is justified by the decision it can change. Stop when the current choice is supported at the needed scope, including an explicit conditional choice where that is the useful result.

### ECO.1:5 - Archetypal Grounding

#### ECO.1:5.1 - A cheap plan priced in internal credits

In a constructed repair-depot case, purchasing a compatible part costs €90 delivered this week. A spreadsheet values making it internally at 40 machine credits plus €30 of material. It silently treats a credit as a euro, although credits allocate booked machine time and cannot purchase extra time. The machine has no available slot this week.

The practitioner removes the unsupported €70 comparison. A nearby provider offers the required machining this week for €65, using the depot's €30 material. The usable comparison is therefore €95 for that route against €90 for the delivered part, subject to equivalent fit and warranty. If no matching offer exists, the internal-credit plan remains unavailable this week; solving its allocation model again cannot make it available.

The repair does not reject credits as a scheduling aid. It stops a claim about monetary cost and availability that the credits did not support.

#### ECO.1:5.2 - A choice without a market quotation

A community can repair one of two paths with the same already available volunteer time. It has no defensible monetary value for each improvement. The group can still choose by access needs and the repair each alternative permits. Reporting that choice as a financial return would add an unsupported claim; postponing it until every benefit has a price would add unnecessary work.

#### ECO.1:5.3 - A useful marginal value inside a model

A workshop has ten usable machine-hours and demand for up to twelve identical one-hour jobs. Each completed job contributes €30 after the other relevant variable costs; the remaining inputs and commitments permit any of these jobs. The model's best contribution rises from €300 at ten hours to €330 at eleven and €360 at twelve. A thirteenth hour adds nothing under that demand limit.

Thus €30 is the modeled value of each of the next two usable hours. It helps set the terms worth considering: an available matching offer at €20 per hour would leave €10 more per added job. The modeled value itself does not supply that offer or make another operator available. A changed demand limit, job mix or needed complement requires a new calculation of the affected margin. The workshop can keep the conditional comparison without investigating every possible capacity supplier.

### ECO.1:6 - Bias-Annotation

A convenient numeric column can acquire more authority than the exchange or constraint it represents. Conversely, criticism of a monetary comparison can become a blanket refusal to calculate. Preserve the useful calculation and repair the unsupported interpretation.

### ECO.1:7 - Conformance Checklist

Can the receiver identify what the consequential quantities mean, who can obtain the resources, and when? Does the comparison retain the relevant alternative uses and obligations? Can the receiver distinguish a monetary consequence from a physical constraint or an unpriced concern, and make the next choice without filling in an invented exchange?

### ECO.1:8 - Common Anti-Patterns and How to Avoid Them

- **A computed price is treated as an available offer.** Return to the model's objective and constraints, then establish the actual supply condition.
- **An unpriced consequence is set to zero.** Keep it as a separate decision consideration or a stated constraint.
- **No complete price system, therefore no action.** Use the comparison that the available physical, contractual and purpose-based grounds already support.

### ECO.1:9 - Consequences

The practitioner can use calculation without overstating its reach. Some rankings become conditional; some apparently cheap alternatives disappear because they cannot be obtained. A limited calculation can still be enough to act.

### ECO.1:10 - Architectural Rationale

An economic comparison needs both a method of calculating and a basis for interpreting its inputs. Separating those contributions preserves mathematical and accounting methods while making missing exchange conditions visible. A universal score of social value would require grounds that ordinary monetary calculation does not supply.

### ECO.1:11 - SoTA-Echoing

[Mises, Economic Calculation, §2](https://mises.org/online-book/economic-calculation-socialist-commonwealth/2-nature-economic-calculation) is the historical anchor for comparing heterogeneous productive means through exchange relations, and for the limits of money calculation outside those relations. This pattern adapts that issue to a bounded working decision; it does not infer that every choice lacking a market price is impossible.

The competing move is to optimize with assumed weights. That remains useful for conditional planning: the output is a consequence of those assumptions. The added operation here tests whether the assumption can support the receiving economic claim. Reopen the comparison when access, exchange terms, available alternatives or the use of the model changes.

### ECO.1:12 - Relations

MA.1 constructs the resource-and-cost account; FIN.6 compares investments using grounded cash flows. ECO.1 supplies the interpretation and attainable exchange conditions they need when those are disputed. ECO.2 responds to changed prices; ECO.3 can form a previously unavailable exchange. C.11.DUA helps choose whether resolving a remaining uncertainty is worth its attainable contribution.

### ECO.1:End
