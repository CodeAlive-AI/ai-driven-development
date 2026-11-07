# Management Accounting Principles Framework

**DocID:** `MA` within **FPF Library**.

**Edition:** [MA 1.0](19-ma-sources-1---edition-record.md)

**Author:** Anatoly Levenchuk, with AI-assisted development and review

Management Accounting develops and uses economic knowledge of an organization's activity: what its results require, whom its resource use and commitments affect, and how different arrangements can sustain the intended work. It helps a controller, accountant or manager explain what happened, anticipate consequences, construct economically supportable changes, and arrange the use of information in decisions. A small account can be sufficient. A cost ceiling defines a condition; participants still need a feasible way of doing the work.

# Table of Contents

**Reader entry**

| § | Publication unit | Use |
| --- | --- | --- |
| R | [Management Accounting Readme](_index.md#management-accounting-readme) | Find an entry for an economic explanation, forecast, activity design or use of information. |
| P | [Management Accounting Principles Framework Architectural Reference](_index.md#management-accounting-principles-framework-architectural-reference) | Understand the connected methods, alternatives and limits. |
| MA.Reference:1 | [The working problem](01-ma-reference-1---the-working-problem.md) |  |
| MA.Reference:2 | [How the methods connect](02-ma-reference-2---how-the-methods-connect.md) |  |
| MA.Reference:3 | [A model that changes the next decision](03-ma-reference-3---a-model-that-changes-the-next-decision.md) |  |
| MA.Reference:4 | [Correct use, evidence and effort](04-ma-reference-4---correct-use-evidence-and-effort.md) |  |
| MA.Reference:5 | [Why this organization of methods](05-ma-reference-5---why-this-organization-of-methods.md) |  |
| MA.Reference:6 | [Sources, qualifications and changed conditions](06-ma-reference-6---sources-qualifications-and-changed-conditio.md) |  |
| MA.Sources:1 | [Edition record](19-ma-sources-1---edition-record.md) |  |
| MA.Sources:2 | [Source locators](20-ma-sources-2---source-locators.md) |  |
| MA.Sources | [Management Accounting Principles Framework Sources and Edition Notes](18-management-accounting-principles-framework-sources-and-editi.md) |  |

**Patterns**

| § | ID & Title | Status | Keywords & Search Queries | Dependencies |
| --- | --- | --- | --- | --- |
| 1 | [MA.1 - Build the Resource-Consumption and Cost Model](08-ma-1---build-the-resource-consumption-and-cost-model.md) | Stable | Resource demand; setup; additional order; cost model detail | OPS.14 uses the model; OPS.15 supplies needed account definitions. |
| 2 | [MA.2 - Explain the Cost and Use of Capacity](09-ma-2---explain-the-cost-and-use-of-capacity.md) | Stable | Paid and usable capacity; reserve; released hours; payment savings | MA.1 for missing demand; OPS for the operating capacity decision. |
| 3 | [MA.3 - Assign Shared Costs for the Stated Use](10-ma-3---assign-shared-costs-for-the-stated-use.md) | Stable | Shared cost; allocation; segment closure; tracing | MA.1–MA.2 for resource meaning; OPS.14 for a closure comparison. |
| 4 | [MA.4 - Reconcile Operating, Reporting and Cash Accounts](11-ma-4---reconcile-operating-reporting-and-cash-accounts.md) | Stable | Profit versus cash; opening and closing balances; inventory; reporting bridge | MA.1–MA.3 and OPS.15; applicable reporting rules. |
| 5 | [MA.5 - Construct and Update an Operating Forecast](12-ma-5---construct-and-update-an-operating-forecast.md) | Stable | Booked and residual demand; scenarios; supply threshold; forecast update | MA.1–MA.4 for assumptions; MA.6 for conflicting number uses. |
| 6 | [MA.6 - Separate Forecasts, Targets and Resource Requests](13-ma-6---separate-forecasts-targets-and-resource-requests.md) | Stable | Expected, targeted, requested and authorized; budget bias | MA.5 for the expectation; MA.1–MA.2 for resource conversion. |
| 7 | [MA.7 - Explain a Cost or Margin Difference](14-ma-7---explain-a-cost-or-margin-difference.md) | Stable | Variance; intermediate accounts; mix; volume; usage; price; causal explanation | MA.1–MA.4 for comparable meanings; the relevant response method. |
| 8 | [MA.8 - Account for Customer and Product Economics Over Time](15-ma-8---account-for-customer-and-product-economics-over-time.md) | Stable | Cohort age; calendar time; acquisition; product life; later obligations; future difference | MA.1–MA.5; FDM for missing financial terms; finance for valuation. |
| 9 | [MA.9 - Design and Examine the Use of Management Accounting Information](16-ma-9---design-and-examine-the-use-of-management-accounting-i.md) | Stable | Decision information; shared consequences; reporting timing; unit-cost target; incentive | MA.1–MA.8 for consequences; OCE for a wider organizational change. |
| 10 | [MA.10 - Develop an Activity Design from an Economic Requirement](17-ma-10---develop-an-activity-design-from-an-economic-requirem.md) | Stable | Target cost; economic feasibility; offer and process redesign; funded service; whole-life consequence | Relevant MA accounts; MKT.2; SYSE.2 and SYSE.8; ECO.2–ECO.4; OPS.14 and OPS.19; FIN.2 and FIN.6. |

# Management Accounting Readme

## Practical entries

Begin with the work that needs to become understandable or possible. You may need an explanation of cost, an outlook, an economically supportable product or service arrangement, or information that helps people coordinate their decisions. These questions lead to different combinations of methods. Management Accounting connects the intended results, work, resource provision, monetary consequences and use of information; the responsible operating, engineering, financial and organizational practices contribute their own constructions and decisions.

These are selected connected examples. Enter where the explanation is missing; reuse an adequate model or account. The [Table of Contents](_index.md#table-of-contents) gives direct access to the methods, and the [Architectural Reference](_index.md#management-accounting-principles-framework-architectural-reference) explains the repertoire. You can ask an assisting agent to explain a pattern or comment on your case in the language of your work, without framework jargon. In MA.4:5, 4 identifies the pattern and 5 its section.

The calculations below are constructed cases under supplied operating, contractual and accounting premises. When applying them, obtain the applicable facts, reporting rules and decisions from the responsible practitioners.

### MA-E1 — An order is priced below reported average cost

- **Situation:** A proposed order looks loss-making in the standard report, but its resource demands, capacity conditions and payments may tell a different story.
- **Question:** What does accepting the work change, and can its payments and operating demands be met when required?
- **First useful result or blocker:** A usable resource and monetary model, then an operating comparison and the remaining capacity or funding question.
- **Start with:** [MA.1 - Build the Resource-Consumption and Cost Model](08-ma-1---build-the-resource-consumption-and-cost-model.md) when the dependencies are missing. Use an adequate model directly; enter MA.2 or MA.3 for a disputed capacity or assignment meaning.
- **Stop or return:** Supply the supported quantities and conditions to OPS.14 for the comparison. An unresolved schedule, financial term or funding question returns to the practice that can settle it.

1. **Recover what the order consumes.** In MA.1's test-order case, an order for 100 accepted units would bring 1,200 of receipts while the report assigns 1,500 of cost. Under the supplied one-attempt premise, six to nine setup hours plus twenty processing hours require 26–29 rig-hours. The operating account establishes twenty uncommitted hours and one obtainable ten-hour block. The interval already settles the one-block question; a more precise setup measurement would not change it.
2. **Attach payments through the actual supply arrangement.** [MA.2 - Explain the Cost and Use of Capacity](09-ma-2---explain-the-cost-and-use-of-capacity.md) keeps occupied hours, supplied blocks and payment changes distinct. The extra block costs 240; fourteen qualified staff-hours fit the supplied sixteen with unchanged pay. Materials cost 200 and the supplier 100, so the model returns 540 of additional payments. If the reported amount is instead disputed as a shared assignment, [MA.3 - Assign Shared Costs for the Stated Use](10-ma-3---assign-shared-costs-for-the-stated-use.md) recovers its tracing or convention. Changing that assignment does not establish a changed payment.
3. **Use the model for the receiving comparison and funding question.** With no displaced contribution and all other flows unchanged, OPS.14 compares 1,200 with 540 and obtains 660. The whole cash position answers a different question. Without the order, 500 would remain available through day 28 after all other receipts and obligations. Paying the order's 440 now leaves sixty, but the supplier's 100 is due on day 7 and the customer pays on day 28. The funding gap of forty remains despite the favorable comparison. An additional receipt of fifty common to both options before day 7 would close that gap without changing the 660 difference.
4. **Return a changed premise to the result it affects.** An eleven-hour setup makes demand 31 hours, beyond the supplied thirty. Reopen the resource model and operating feasibility; the earlier one-block result no longer applies. A later change in payment terms instead reopens the timed account. Neither requires rebuilding an unchanged part of the model.

### MA-E2 — Profit and cash movement disagree

- **Situation:** A positive reported result coexists with falling cash, and a lower unit-cost figure may be encouraging additional production.
- **Question:** Which differences belong to the accounts' meanings, and which actual action or use of the account may need to change?
- **First useful result or blocker:** A reconciled explanation of the accounts; if their use is the problem, a supported change to that use or the unresolved behavioral explanation.
- **Start with:** [MA.4 - Reconcile Operating, Reporting and Cash Accounts](11-ma-4---reconcile-operating-reporting-and-cash-accounts.md). Use [MA.9 - Design and Examine the Use of Management Accounting Information](16-ma-9---design-and-examine-the-use-of-management-accounting-i.md) directly when the monetary meanings are adequate and the unresolved question concerns behavior.
- **Stop or return:** A sufficient reconciliation can finish the request. A funding decision needs the whole timed cash position; changing rewards or authority needs the responsible organizational decision.

1. **Put the views on their actual event and policy bases.** MA.4's case starts with zero inventory, receivables and payables and includes only the transactions described below. Producing 100 units costs 200 in materials and 300 in resource supply, all paid; sixty units sell for 600, of which 400 is received and 200 remains receivable. Under the supplied full-production-cost policy, cost of sales is 300, closing inventory 200 and the reported result 300. Cash movement is −100.
2. **Carry the reconciliation to its user.** The internal account values inventory at materials only and expenses the 300 resource-supply payment, giving a result of 180 and inventory of eighty. Thus 300 − 200 inventory − 200 receivables and 180 − 80 inventory − 200 receivables both give −100. The 120 difference between results is retained production-resource cost, not another receipt. Preserve each view for its warranted use. If an event or policy is unresolved, obtain that answer from OPS.15 or the responsible reporting practice.
3. **Use the explanation to examine a consequential choice.** Suppose management considers producing 120 units with the same 300 resource payment and unchanged sales of sixty. MA.9 compares the account and the resulting resource use: unit cost falls from five to 4.5, but materials consume forty more in cash and unsold quantity rises from forty to sixty. This establishes the divergence the measure conceals. Whether an actual production increase followed that incentive, anticipated demand or another reason remains a separate question.
4. **Repair only the supported problem and return changed conditions.** If the account's use is the established problem, the responsible manager can stop treating lower unit cost alone as improved performance and consider demand, inventory and resource consequences together. Preserve the legitimate reporting account. Evidence of a warranted future requirement could instead support the extra production. A changed measurement or allocation basis returns to MA.4 or MA.3 before a performance comparison; [MA.7 - Explain a Cost or Margin Difference](14-ma-7---explain-a-cost-or-margin-difference.md) uses comparable meanings to separate the consequential difference from its still-unresolved cause.
5. **Carry the account into the next period when needed.** MA.4:5.2 starts from the remaining forty units and receivable, then derives the next closing balances. Results of 320 and 340 both connect to cash movement of 400. The changed result difference follows the release of earlier inventory cost; the explanation requires opening as well as closing values.

### MA-E3 — The forecast has become a resource negotiation

- **Situation:** One number is expected to serve as demand outlook, ambition, resource request and authorization, concealing the decision needed when they differ.
- **Question:** Which expectation should remain visible, and which actual action or resource decision could change the outlook?
- **First useful result or blocker:** Distinguishable expectations, ambitions, requests and authorizations, connected to the resource or management decision that matters.
- **Start with:** [MA.6 - Separate Forecasts, Targets and Resource Requests](13-ma-6---separate-forecasts-targets-and-resource-requests.md) for mixed meanings; [MA.5 - Construct and Update an Operating Forecast](12-ma-5---construct-and-update-an-operating-forecast.md) when the meanings are settled and the outlook needs construction or revision.
- **Stop or return:** Keep an adequate expectation visible. A resource request, its authorization and usable provision remain different results.

1. **Recover the use of each number.** MA.6's case has demand expected at 100 units, an ambition of 120, a request for provision covering a possible surge to 130, and authorization covering 110 under the supplied mix and scheduling assumptions. The authorization neither changes expected demand to 110 nor makes the ambition feasible.
2. **Connect the gap to the result that can resolve it.** MA.5 constructs or obtains the warranted demand outlook and its uncertainty. Its MA.5:5.1 example joins sixty booked units with forty further units estimated on a nonoverlapping basis; a sufficient supplied forecast can be used directly. Where conversion is missing, MA.1 and MA.2 relate demand to resource quantities and payments, using the adequate operating capacity account. The responsible manager can then decide about provision, scope or ambition. When the ambition or its comparison lacks a meaningful basis, [OPS.21](../ops/55-ops-21---choose-operating-aims-targets-and-comparisons.md) constructs that missing result; an adequate supplied target can remain. Keep a proposed addition in the scenario where it occurs; do not make it available by editing the forecast.
3. **Propagate the actual change.** If a market action warrants a new expectation of 115, MA.5 updates that outlook and its assumptions. The gap against authorized capability is five units on the same basis; the target remains 120 and authorization 110 until their responsible participants change them. A fixed resource payment stays fixed under its terms even when demand changes.
4. **Use the later result without rewriting the earlier prediction.** Retain the earlier forecast's premises when learning from outcomes. MA.7 constructs comparable intermediate accounts to explain the difference. If product mix changed, MA.7:5.2 shows how to replace an aggregate usage term with mix and within-product usage; action taken in response may account for part of the observed change. If the reward or negotiation arrangement still suppresses unwelcome expectations, MA.9 examines that specific use and returns any wider organizational change to its responsible practice. The clarified accounts may already resolve the question. If the attained result still needs a performance judgement, [OPS.22](../ops/56-ops-22---interpret-operating-performance-and-decide-the-resp.md) examines target difficulty, changed conditions, action and joint effects before choosing a response. The [repair cooperative case (Engineering.Reference:7)](../../engineering-dpf-suite/suite-reference/09-engineering-reference-7---how-should-we-set-a-target-and-jud.md) develops that continuation through an actual change in the local review rule.

### MA-E4 — Two customer cohorts share one paid service team

- **Situation:** A proposed cohort appears to contribute money, but it will share capacity and payment dates with an existing cohort.
- **Question:** What does adding it change after their demands are combined, and can the work and payments be met?
- **First useful result or blocker:** A joint resource account, the new cohort's future monetary difference and the whole dated cash position, with unresolved capacity or later flows kept visible.
- **Start with:** [MA.8 - Account for Customer and Product Economics Over Time](15-ma-8---account-for-customer-and-product-economics-over-time.md) when population or time is unclear. Use adequate supplied cohort quantities directly, then obtain missing resource and supply relationships through MA.1–MA.2.
- **Stop or return:** OPS.14 uses feasible future consequences for the operating comparison. An unknown obligation returns to FDM, a funding question to the relevant financial practice, and a sufficient supported account can finish the accounting request.

1. **Put both populations into the same calendar.** In this separate teaching case, the supplied active-customer quantities for months 2–4 are 80, 60 and 45 for the existing cohort, and 40, 20 and 10 for the proposed cohort. They are conditional scenario inputs. MA.8 explains how to obtain the calendar quantities from cohort age when they are not already supplied.

2. **Construct the shared resource demand.** Each cohort requires two setup hours per month plus 0.25 qualified service hour per active customer. The cohorts share 26 usable hours for an unchanged monthly payment of 240. One further nine-hour block can be obtained in each month for 180, paid at that month's start. Scheduling is supplied as feasible whenever the demands fit those quantities.

   | Calendar month | Existing cohort hours | Proposed cohort hours | Joint demand | Additional block needed |
   | --- | ---: | ---: | ---: | --- |
   | 2 | 2 + 80 × 0.25 = 22 | 2 + 40 × 0.25 = 12 | **34** | **One** |
   | 3 | 2 + 60 × 0.25 = 17 | 2 + 20 × 0.25 = 7 | **24** | None |
   | 4 | 2 + 45 × 0.25 = 13.25 | 2 + 10 × 0.25 = 4.5 | **17.75** | None |

   Each cohort would fit the basic capacity alone, but their month-2 total requires the extra block. Both setups remain because the supplied work requires them. A proposed shared setup needs an operating basis before either is removed. The payment of 240 is for the common supply arrangement and appears once in the whole account.

3. **Distinguish the future difference from assigned and historical amounts.** The proposed cohort costs 600 to acquire before month 2. It pays 3 per active customer for service at month start and receives 15 per active customer at month end. Receipts total 15 × (40 + 20 + 10) = **1,050** and direct service payments total 3 × 70 = **210**. The added capacity payment is 180, so the future difference is **1,050 − 210 − 180 − 600 = 60**, with other flows unchanged.

   The existing cohort's acquisition payment of 2,000 is historical. A report assigns eight of team cost per active customer to the new cohort, totaling 560 over these months. MA.3 can explain that assignment; it is not another payment on top of the actual supply arrangements. The +60 concerns only this three-month alternative under the supplied conditions. Later flows and the responsible decision criteria remain outside that calculation.

4. **Restore the whole cash position at each payment date.** Without the new cohort, 900 would be available at every relevant date after all existing receipts and obligations, including the unchanged team payment. Acquisition reduces that position to 300. Add the new flows cumulatively to this baseline:

   | Date | Additional payment or receipt at this date | Whole cash position |
   | --- | ---: | ---: |
   | Before month 2: acquisition | −600 | **300** |
   | Month 2 start: service and block | −120 − 180 | **0** |
   | Month 2 end: receipts | +600 | **600** |
   | Month 3 start: service | −60 | **540** |
   | Month 3 end: receipts | +300 | **840** |
   | Month 4 start: service | −30 | **810** |
   | Month 4 end: receipts | +150 | **960** |

   Thus the positive difference coexists with zero cash buffer at the month-2 start. No unchanged payment is subtracted again after it has entered the baseline. MA.4 supplies a needed reconciliation to reported results, which can recognize amounts at different times.

5. **Reopen only the changed condition and its consequences.** Suppose evidence now bounds service effort for each active customer between 0.25 and 0.30 hour, without establishing one common rate for all customers. Add these individual bounds while keeping both setups. Joint demand is **34–40**, **24–28** and **17.75–20.5** hours. Month 2 may exceed the maximum supplied 35; month 3 may need the extra block above 26; month 4 fits.

   Obtain only the aggregate information that can resolve those thresholds, or a feasible revised operating arrangement. Precise measurement of every customer's effort is unnecessary if a supported aggregate bound settles the question. For a feasible month-2 branch, the future difference remains **60** when month 3 fits the basic supply, or becomes **−120** when month 3 also needs its 180 block. The month-2 receipts remain conditional while service feasibility is unresolved. Do not invent a second block or promise unchanged receipts for work that cannot be performed.

The combined capacity, dates and remaining uncertainty determine whether the whole account can be used, even when every local multiplication is correct.

### MA-E5 — The required economics has no supported design

- **Situation:** A product has a credible price and required margin, or a service has a funding ceiling, but no supported arrangement yet delivers the required result within those conditions.
- **Question:** Which changes in the offer, work and provision could produce an economically supportable arrangement?
- **First useful result or blocker:** Joint activity-design alternatives with their whole consequences and remaining conditions, or a supported conflict between the required result and available means.
- **Start with:** [MA.10 - Develop an Activity Design from an Economic Requirement](17-ma-10---develop-an-activity-design-from-an-economic-requirem.md). It connects the requirement to changeable dependencies and helps the responsible participants construct and examine alternatives.
- **Stop or return:** If supported alternatives already exist, use the adequate account and receiving comparison directly. Return an unresolved technical, market, resource or funding condition to the practice that can establish it.

MA.10:5 contrasts a product and support redesign with a funded service whose access and qualified capacity constrain the possible changes.

### MA-E6 — People need information before they can coordinate action

- **Situation:** People need to make a joint service commitment, but their existing information does not support the required coordination. A harmful metric effect need not have occurred.
- **Question:** What account and comparison must reach which participants in time for them to choose and carry out the needed action?
- **First useful result or blocker:** An information arrangement connecting the decision, participants, actions and timing, or an unresolved condition preventing its use.
- **Start with:** [MA.9 - Design and Examine the Use of Management Accounting Information](16-ma-9---design-and-examine-the-use-of-management-accounting-i.md). Its shared-service case exposes a capacity conflict before a promise is made.
- **Stop or return:** Retain an adequate arrangement. Use observations of whether people receive, understand and act on the information to identify a specific repair; return a missing capacity or authority decision to its responsible participants.

---

## Files of this publication

Generated by the skill's splitter: one file per section, in reading order.


### Management Accounting Principles Framework Architectural Reference

- [MA.Reference:1 - The working problem](01-ma-reference-1---the-working-problem.md) (46 lines)
- [MA.Reference:2 - How the methods connect](02-ma-reference-2---how-the-methods-connect.md) (26 lines)
- [MA.Reference:3 - A model that changes the next decision](03-ma-reference-3---a-model-that-changes-the-next-decision.md) (8 lines)
- [MA.Reference:4 - Correct use, evidence and effort](04-ma-reference-4---correct-use-evidence-and-effort.md) (10 lines)
- [MA.Reference:5 - Why this organization of methods](05-ma-reference-5---why-this-organization-of-methods.md) (12 lines)
- [MA.Reference:6 - Sources, qualifications and changed conditions](06-ma-reference-6---sources-qualifications-and-changed-conditio.md) (14 lines)
- [MA.Reference:End](07-ma-reference-end.md) (2 lines)
- [MA.1 - Build the Resource-Consumption and Cost Model](08-ma-1---build-the-resource-consumption-and-cost-model.md) (205 lines)
- [MA.2 - Explain the Cost and Use of Capacity](09-ma-2---explain-the-cost-and-use-of-capacity.md) (116 lines)
- [MA.3 - Assign Shared Costs for the Stated Use](10-ma-3---assign-shared-costs-for-the-stated-use.md) (114 lines)
- [MA.4 - Reconcile Operating, Reporting and Cash Accounts](11-ma-4---reconcile-operating-reporting-and-cash-accounts.md) (174 lines)
- [MA.5 - Construct and Update an Operating Forecast](12-ma-5---construct-and-update-an-operating-forecast.md) (164 lines)
- [MA.6 - Separate Forecasts, Targets and Resource Requests](13-ma-6---separate-forecasts-targets-and-resource-requests.md) (121 lines)
- [MA.7 - Explain a Cost or Margin Difference](14-ma-7---explain-a-cost-or-margin-difference.md) (159 lines)
- [MA.8 - Account for Customer and Product Economics Over Time](15-ma-8---account-for-customer-and-product-economics-over-time.md) (176 lines)
- [MA.9 - Design and Examine the Use of Management Accounting Information](16-ma-9---design-and-examine-the-use-of-management-accounting-i.md) (154 lines)
- [MA.10 - Develop an Activity Design from an Economic Requirement](17-ma-10---develop-an-activity-design-from-an-economic-requirem.md) (146 lines)

### Management Accounting Principles Framework Sources and Edition Notes

- [Management Accounting Principles Framework Sources and Edition Notes](18-management-accounting-principles-framework-sources-and-editi.md) (6 lines)
- [MA.Sources:1 - Edition record](19-ma-sources-1---edition-record.md) (4 lines)
- [MA.Sources:2 - Source locators](20-ma-sources-2---source-locators.md) (45 lines)
- [MA.Sources:End](21-ma-sources-end.md) (1 lines)
