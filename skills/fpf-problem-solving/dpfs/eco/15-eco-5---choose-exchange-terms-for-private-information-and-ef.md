## ECO.5 - Choose Exchange Terms for Private Information and Effort

> **Type:** Method pattern
> **Status:** Stable

### ECO.5:1 - Problem frame

Use this pattern when an exchange depends on quality, circumstances or future action that one party knows or controls and another cannot cheaply observe or verify. Begin with the consequential choice each party can make under the proposed terms. Compare terms that make the desired contribution worthwhile while leaving participation attainable.

The useful result is a proposed exchange with a stated incentive mechanism and its limits, or a reason the exchange cannot be made acceptable. An ordinary purchase with adequate known quality and established terms needs no new contract model.

### ECO.5:2 - Problem

A buyer can offer a price which attracts low quality while driving better suppliers away. A payment rule can reward a visible number instead of the contribution sought. Asking for a promise of care does not change what a provider gains from taking care. Conversely, forcing a provider to bear all uncertainty can drive away a capable participant.

### ECO.5:3 - Forces

Information has acquisition and verification costs. Incentives and risk sharing can conflict. A strong warranty or stake can make an offer credible while excluding a good provider without enough capital. Observable outcomes can depend on both effort and circumstances outside the performer's control.

### ECO.5:4 - Solution

#### ECO.5:4.1 - Locate the private fact or action

Name what matters to the exchange and who can know or control it. Existing quality, intended use or financial condition can be private information before agreement; maintenance, care or effort can be a later private action. Both can occur together, but changing the payment for an action does not automatically reveal an existing fact.

Describe the consequential alternatives available to each party: disclose, withhold, choose one offer, participate, change effort, manipulate a measure, withdraw or renegotiate. Use realistic available alternatives, not the assumption that every participant follows the author's preferred plan.

#### ECO.5:4.2 - Construct terms from the choices they must change

Begin with terms whose consequences the parties can realize. Candidates include payment after an interpretable acceptance test, a refund for a defined failure, an exposed deposit, or a menu of specified services. Recover the available observation, authority and means of carrying out the terms. Specify the payment or service attached to each available choice or observable event. Reuse an established rule when its effects are already adequate.

**For a private action, compare the participant's return from doing and not doing the wanted work.** Include each consequential alternative recovered in §4.1, including a way to improve the measure while neglecting the result. Change the part of the terms that makes those returns differ. Then check whether the resulting reward and exposure make entry worthwhile relative to the participant's available alternative. Participation and the choice after entry must hold together.

For a small risk-neutral comparison, let b be a payment received regardless of the test result, w an additional payment for passing, p the chance of passing under a particular action, and c that action's cost. The participant's expected return is b + p × w − c. Compare that expression for the wanted action and every relevant alternative. The difference in expected bonus between two actions is their difference in passing probabilities multiplied by w. Raising b equally for every action increases the return from participating but leaves the ranking of actions unchanged in this model. With risk aversion, wealth effects or different payment dates, that simplification need not hold: compare the relevant distributions and financing needs or obtain the bounded specialist result.

**For a private fact, compare what every relevant kind of participant would choose.** A seller can know the existing quality; a buyer can know its own need. The designer's possible cases are hypotheses about those facts, not knowledge of this participant's case. For each case, compare the same offer, every other available offer, and nonparticipation under that case's costs, benefits and exposure. Do not assign each case to the offer the designer intended for it.

A term can distinguish cases when it has different consequences for them. A credible failure refund costs a failure-prone seller more in expectation; different service packages can be worth different amounts to buyers. Use that difference to construct candidate terms. If you intend participants with one private fact to accept and others to decline or choose another offer, test each choice. If participants with different private facts would choose the same offer, acceptance does not distinguish those facts. The exchange can still be worthwhile under a supported mixed or conditional account, but the designer cannot use the intended separation as its basis. If participants can change their actions after selecting an offer, also perform the action comparison for those continuations.

**Find terms that satisfy the connected comparisons.** Vary a term that changes the comparison, such as the price, conditional amount or service, while retaining the observation and resource limits. Keep terms that support the needed participation and choices and leave an acceptable result for the other party. A boundary at which someone is indifferent establishes a tie; it does not establish the designer's preferred choice. Retain that uncertainty or obtain a reason for the choice. If no feasible terms meet the conditions, change the offered service, observation or allocation of risk, consider another participant, or decline the exchange. Increasing every payment cannot repair every failed incentive or selection condition.

Calculate probabilities and monetary consequences only where their use is justified; otherwise compare supported cases or ranges and identify the difference that could reverse the choice. Include verification, enforcement, capital tied up and unpriced consequences. A warranty or deposit can discourage the unwanted choice while excluding a capable participant who cannot bear its exposure.

An observed result must contain useful information about the sought contribution. If the provider can improve the measured result by neglecting another important result, change the terms or the observation. If a signal mostly adds uncontrollable risk, using it can worsen participation without improving the action. Staging can limit exposure to nondelivery without identifying quality; each construction needs the effect actually claimed for it.

#### ECO.5:4.3 - Make the terms usable

Check that the proposed consequence can actually occur: the warranty provider can meet claims, an acceptance condition can be interpreted, a stake remains exposed, and the relevant parties can make the agreement. Obtain a bounded legal or specialist mechanism-design result when enforceability or a claimed guarantee depends on it. The economic comparison itself supplies neither.

Return the proposed terms, why they alter the important choice, and the unresolved condition. Reuse established terms when they already work. Do not collect additional information simply because it exists; compare the next attainable improvement with its burden.

### ECO.5:5 - Archetypal Grounding

#### ECO.5:5.1 - Care under an outcome-based payment

A constructed maintenance job has two available care choices. The example assumes a risk-neutral provider, no other relevant costs, and a valid functional test that cannot be cheaply manipulated. Low care costs €4 and passes with probability 0.5; high care costs €12 and passes with probability 0.9. The provider's feasible outside alternative gives €32.

Construct a contract with a nonnegative base payment b and an additional nonnegative passing bonus w. High care is strictly preferable to low care when (0.9 − 0.5) × w > €12 − €4, so w must exceed €20. To make high care strictly preferable to the outside alternative as well, b + 0.9 × w − €12 must exceed €32. Choose an available bonus of €30; the base must then exceed €17. A base of €20 meets both conditions. Next compare the buyer's result with its available alternative.

Expected provider receipts less care cost are €31 for low care and €35 for high care. The €12 increase in expected bonus exceeds the €8 increase in care cost. High care also exceeds the €32 outside return and attracts participation in this small model. A flat €35 payment would give €31 under low care and €23 under high care, so it would neither attract this provider nor reward the intended action.

For the risk-neutral buyer, suppose a passing result is worth €80, a failing result gives no benefit, and the same test and other costs apply to both offers. The proposed contract gives expected benefit €72 and payment €47, leaving €25. An available alternative provider charges a fixed €50 for the same 0.9 chance of success, leaving €22. The buyer therefore proposes the conditional contract, which the first provider also prefers to its outside alternative. If the passing result were worth only €40 and the buyer could leave the equipment idle without further loss, both offers would give negative expected net benefit; the buyer would decline them.

This establishes the direction of the constructed incentives, not an optimal contract or a prediction about every provider. If the test can be passed while leaving the equipment unreliable, the contract rewards the wrong result. If the provider cannot bear variable receipts, the participation conclusion must be reconsidered.

If the available terms cap the passing bonus at €15, the largest extra expected reward for high care is 0.4 × €15 = €6, below its €8 extra cost. No change to the common base payment repairs that action comparison under the stated assumptions. Retain the other provider if its complete offer remains acceptable, or reconsider the observation, work or available terms before promising high care.

#### ECO.5:5.2 - A warranty whose issuer cannot pay

Two sellers offer the same warranty, but one has no resources to honour a claim and can disappear after the sale. The words impose different expected consequences in the two arrangements. A deposit, credible guarantor, repeat relationship or different offer may help; merely lengthening the warranty text does not.

#### ECO.5:5.3 - Construct a quality offer and test who would accept

A buyer needs one refurbished component. In this constructed model, sellers know whether their component has a 0.1 or 0.5 chance of failure during a fixed warranty period; the buyer cannot identify the particular component's case. These chances are stipulated, cannot be changed by later care, and refer to the same verifiable failure. Each seller incurs €40 to supply the component. The more reliable seller's available alternative gives €50 net, and the less reliable seller's gives €30. Both parties are risk-neutral. Supply, administration and the required cash are available; no additional costs are assumed.

Propose a price P with a refund R on failure. A trusted administrator can retain the refund amount from the price until the period closes and pay it to the buyer if the specified failure occurs; the seller's cash needs remain affordable under that arrangement. The seller's expected net return is P − €40 − q × R, where q is its failure chance. To determine who would accept, compare the offer with each seller's actual alternative.

| Required choice | Comparison | Bound on price |
| --- | --- | --- |
| More reliable seller prefers this offer | P − €40 − 0.1 × R > €50 | P > €90 + 0.1 × R |
| Less reliable seller prefers its outside alternative | P − €40 − 0.5 × R < €30 | P < €70 + 0.5 × R |

For both strict comparisons to hold, R must exceed €50. With an available refund of €80, the price must be above €98 and below €110. Choose €100. The more reliable seller obtains €52 rather than €50; the less reliable seller would obtain €20 rather than €30 and declines. The proposed separation follows from both choices under these assumptions, not from asking sellers to declare their quality.

The buyer values a working component at €150 and a failed component at zero. With the selected component, expected value plus refund less price is 0.9 × €150 + 0.1 × €80 − €100 = €43. An available verified alternative has the same 0.1 failure chance, costs €120 and carries no refund, leaving €15 in expectation. The buyer and the more reliable seller therefore both prefer this exchange to their available alternatives. In this case the refund reallocates the loss; the selected component's failure chance remains 0.1.

Suppose the available arrangement can instead secure only a €20 refund. The reliable seller now requires a price above €92, while excluding the less reliable seller requires a price below €80. No price meets both conditions. Raising the price to attract the reliable seller also attracts the other seller, so the buyer cannot retain the former quality inference. It can use the verified alternative, obtain another credible arrangement, or compare an offer that explicitly allows both qualities if enough is known about the resulting mix. Missing information about that mix is a remaining premise, not the old 0.1 failure chance.

Reopen the comparison when a seller's outside option, ability to finance the retained amount, failure observation or competing offer changes. If only one kind can finance the arrangement, acceptance can reflect access to capital as well as quality. Reconsider the claimed inference before using it to procure the component.

### ECO.5:6 - Bias-Annotation

Formal-looking incentives can conceal disputed probabilities, power or a mismeasured result. Labelling a party dishonest can also distract from a payment rule that makes the unwanted action attractive to ordinary participants. Model the available choices before attributing motives.

### ECO.5:7 - Conformance Checklist

Does the proposed term change the consequential choice? Can the necessary party participate under its available alternatives and exposure? Can the receiver distinguish private information from private action and test the claimed observation or enforcement mechanism? Are numerical conclusions limited to their stated assumptions?

### ECO.5:8 - Common Anti-Patterns and How to Avoid Them

- **Paying for a proxy is treated as paying for the result.** Trace how the performer can improve the proxy and whether that supplies the result.
- **A written promise is treated as a credible consequence.** Recover the means and conditions that make its consequence effective.
- **Only incentives are optimized.** Retain participation, risk bearing, verification and exclusion costs.

### ECO.5:9 - Consequences

Some exchanges become feasible without making all private facts public. Others need simpler terms, a different participant or no exchange. More elaborate terms can introduce new gaming and interpretation costs; complexity is justified only by the contribution it preserves.

### ECO.5:10 - Architectural Rationale

Terms change a participant's feasible and attractive choices. Information gathering is one way to improve an exchange, but rearranging its consequences can sometimes do so more economically. Participation and behavior after entry are distinct tests of that construction.

### ECO.5:11 - SoTA-Echoing

[Akerlof (1970), §IV](https://www.sfu.ca/~allen/Ackerlof.pdf) identifies arrangements such as guarantees that respond to hidden quality. [Rothschild and Stiglitz (1976), §I.1, I.3 and I.6](https://economia.uc3m.es/docencia/MicroII/Rothschild-Stiglitz%201976.pdf) examine selection through offered contracts: the preferred contract for one kind of participant must also be examined as an available choice for another. That comparison informs the private-fact branch here; the insurance-market equilibrium conclusions are not transferred to this procurement example.

[Holmström (1979), §2 and concluding remarks](https://gwern.net/doc/economics/1979-holmstrom.pdf) constrains contract choice by both participation and the action the participant will select, while examining information and risk sharing. These are historical analytical foundations. The finite risk-neutral examples here demonstrate feasible terms. They do not solve that paper's risk-averse optimization problem.

The rival is an ordinary contract plus direct observation. Keep it when sufficiently inexpensive and informative. This pattern adds a comparison of feasible terms when observation is incomplete or costly. It does not turn a mechanism's mathematical possibility into actual enforceability or proven field effectiveness. Reopen when participation, available actions, signal quality or enforcement changes.

### ECO.5:12 - Relations

ECO.4 uses these terms in complementary venture commitments. ECO.6 addresses dependence that emerges after investment, which can remain even with a well-designed initial payment. FPF E.13 helps when a proxy substitutes for the intended result; MMP supplies a needed mathematical model. Applicable legal rules and CGOV supply authority or corporate decisions only when those questions arise.

### ECO.5:End
