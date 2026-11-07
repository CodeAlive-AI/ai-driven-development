## MA.7 - Explain a Cost or Margin Difference

**Type:** Architectural

**Status:** Stable

### MA.7:0 - Use this when

Use this pattern when a cost, margin or other account differs from a comparison value and the explanation could change a response. Begin with the actual difference before attributing it to performance.

The pattern governs an explanation of an accounting difference. It returns a comparable basis, an adequate decomposition and supported or unresolved explanations of the causes that matter.

Use an adequate existing explanation directly. A small immaterial difference need not trigger a wider investigation unless another obligation requires it.

### MA.7:1 - Problem frame

A period's material cost can rise because more units were produced, the mix changed, more material was consumed per accepted unit or the price changed. A margin can also change because of recognition, shared assignment or capacity use.

An arithmetic decomposition helps locate the difference. It does not by itself establish why the quantities changed or which participant could have acted differently.

### MA.7:2 - Problem

Calling every adverse difference “inefficiency” can direct action at the wrong cause. Comparing unlike periods or definitions can create a variance that has no performance meaning.

A decomposition with many small terms can also hide the consequential explanation. The task is to recover the comparison and investigate the causes that can change the response.

### MA.7:3 - Forces

Management wants an early explanation. A provisional decomposition can be useful before causal evidence is complete, provided its status remains clear.

Several factors can interact, so the amount assigned to each arithmetic component can depend on the decomposition convention. A convenient order is usable for explanation when that convention is visible.

### MA.7:4 - Solution

#### MA.7:4.1 - Restore a comparable account

Identify the two values, their subjects, periods, units and purposes. Recover the definitions, recognition, valuation and allocation rules that produced them. Use MA.4 for a view difference and MA.3 for a changed assignment.

Separate a genuine work or price change from a changed measurement or account boundary. Keep an unresolved comparison problem visible before interpreting a variance as performance.

#### MA.7:4.2 - Construct the intermediate accounts

Choose the adequate resource and monetary relationship that produces both totals. For materials this may be output by product, material requirement per product and material price. For margin, use the corresponding recognized revenue less the included costs on the same account basis. MA.1 supplies a missing consumption relationship; MA.3–MA.4 resolve an assignment or recognition difference.

Start with the reference account and change the factors in a stated order until the model reaches the actual account. At each transition, change the selected factor while holding the other stated values fixed. Calculate the new total, then subtract the preceding total. These adjacent differences add to the overall change because each intermediate total enters once positively and once negatively.

For an activity and product-mix explanation, construct the following comparisons:

1. **Reference activity and composition.** Recover the original output quantities, resource requirements and prices.
2. **Actual total activity at reference composition.** Apply the original product proportions to actual total output, retaining reference consumption and prices. This isolates volume under that convention. Use a meaningful common activity unit; incompatible products may need separate families or another supported activity measure.
3. **Actual composition at reference requirements.** Insert actual output by product, still using the reference resource requirement for each product and reference prices. The difference from the preceding account is the mix component.
4. **Actual consumption at reference prices.** Insert the material or other resource quantities actually consumed. Compare them with the requirements of the actual product mix. This leaves a within-product usage question instead of attributing every change in the aggregate average to waste.
5. **Actual consumption and actual prices.** Insert the actual prices to reach the actual monetary total. Any remaining recognition or measurement difference must be explained on its own account basis.

The model determines which comparisons are useful. A paid block, reserve or commitment can remain unchanged over several activity levels, then change at a threshold. Recalculate that supply relationship at each stage instead of multiplying every payment by a volume ratio. If changing one factor while retaining another would describe an incoherent or unsupported combination, use an adequately supported combined component or leave that separation unresolved. A convenient table does not make an impossible comparison meaningful.

Reconcile the components to the total. Keep a residual visible if the model or observations cannot explain it. When more detail explains a component, replace that parent component with its subdivisions in the total; do not count both. A smaller decomposition is sufficient when further separation cannot change the response.

Preserve the original plan or forecast when that is the comparison being explained. A reference account recalculated at actual volume helps locate a difference; it does not retroactively change what was originally expected. A later revised forecast is a separate comparison with its own information basis.

#### MA.7:4.3 - Test the explanation behind the arithmetic

Ask what actually changed each consequential component. Compare operating evidence, terms and relevant conditions. Higher material use per accepted unit might follow a harder product mix, failed attempts, a measurement change or a process defect.

Distinguish association and assigned arithmetic effect from a supported causal explanation. Investigate the rival explanations that would lead to different actions. If adequate evidence is unavailable, return the bounded uncertainty and the next observation or specialist result that could resolve it.

#### MA.7:4.4 - Return the explanation and appropriate response question

Supply the total difference, its adequate decomposition and the supported causes or remaining uncertainty. Keep controllability and responsibility claims at the scope their evidence warrants.

Use the relevant operating, commercial or financial method for the response. MA.5 updates a future outlook when the changed condition is expected to persist; MA.9 examines incentives that may be influencing the account or behavior. If a supported explanation invalidates the economic basis of the current activity design, return the changed relationship to MA.10. A different accounting convention can instead require reconciliation while leaving that design intact.

### MA.7:5 - Archetypal Grounding

#### MA.7:5.1 - Locate the aggregate difference

A constructed material-consumption account planned 100 accepted units, two material units per accepted unit and a price of 3 per material unit. Planned cost was **100 × 2 × 3 = 600**.

The actual comparable account has 120 accepted units, 2.5 material units per accepted unit and a price of 4. Actual cost is **120 × 2.5 × 4 = 1,200**, a difference of **600**.

Using the stated order volume, usage, then price:

| Component | Calculation | Amount |
| --- | --- | ---: |
| Volume at planned usage and price | (120 − 100) × 2 × 3 | **120** |
| Usage at actual volume and planned price | 120 × (2.5 − 2) × 3 | **180** |
| Price at actual volume and usage | 120 × 2.5 × (4 − 3) | **300** |
| Total difference | 120 + 180 + 300 | **600** |

The decomposition is complete arithmetically. It does not establish that the extra 0.5 material units were waste. If the actual workload included a different product mix legitimately requiring more material, the comparison needs that distinction. If the mix is unchanged and adequate records identify failed attempts, the process question becomes more specific. A changed measuring convention would instead require repairing the account.

Another valid decomposition order can assign interaction amounts differently. Retain the chosen convention rather than using a component's exact size as independent evidence of causal responsibility.

#### MA.7:5.2 - Reconstruct the comparison when product mix changes

Suppose the original 100 units comprised fifty A requiring one material unit each and fifty B requiring three. Their reference requirement was 50 × 1 + 50 × 3 = **200** materials. Actual output is thirty A and ninety B. Under unchanged requirements within each product, those outputs require 30 × 1 + 90 × 3 = **300** materials.

The planned and actual totals are still 600 and 1,200, but the intermediate accounts now expose a different explanation:

| Account | Material quantity | Price | Cost | Difference from preceding account |
| --- | ---: | ---: | ---: | ---: |
| Planned 50 A and 50 B | 200 | 3 | **600** | — |
| Actual volume 120 at original 50:50 mix: 60 A and 60 B | 240 | 3 | **720** | **120 volume** |
| Actual mix: 30 A and 90 B, at reference requirements | 300 | 3 | **900** | **180 mix** |
| Actual material consumption | 300 | 3 | **900** | **0 within-product usage** |
| Actual price | 300 | 4 | **1,200** | **300 price** |

Thus 120 + 180 + 0 + 300 = **600**. The earlier 180 aggregate usage component is now replaced by 180 mix plus zero within-product usage. Adding a further 180 mix to the old decomposition would double count it. The aggregate average rose from two to 2.5 because the output composition changed; this account supplies no evidence of increased waste.

Now change actual consumption to **324** materials on that same actual mix. At the reference price, consumption costs 972, so usage contributes 972 − 900 = **72**. Actual price gives 1,296 and a price component of **324**. The total difference is 1,296 − 600 = **696**, reconciled as 120 volume + 180 mix + 72 usage + 324 price. Investigate the additional twenty-four materials through the operating records and competing explanations; their arithmetic cost does not establish a defect or assign responsibility.

If evidence supports a persistent move toward product B, MA.5 can update the future composition and its resource consequences. The earlier forecast remains available for learning. A different decomposition order can move interaction amounts between components, while the total and the need for causal evidence remain.

### MA.7:6 - Bias-Annotation

A manager can prefer an explanation outside their control; an evaluator can prefer one inside it. Test explanations against actual conditions and evidence.

### MA.7:7 - Conformance Checklist

Examine whether the comparison uses adequate subjects, periods and account rules; consequential components reconcile to the total; the decomposition convention is clear where needed; causal claims have support beyond arithmetic; and unresolved explanations lead to a useful next question.

A zero arithmetic residual establishes numerical closure under the model. It does not establish causal closure.

### MA.7:8 - Common Anti-Patterns and How to Avoid Them

**Calling a usage variance waste before checking mix.** Recover the actual resource requirement and alternative explanations.

**Counting a variance and its subdivisions together.** Replace the parent component when the more detailed explanation is used.

**Assigning responsibility from the decomposition order.** Distinguish the arithmetic convention from evidence about cause and control.

**Balancing an unexplained residual into “efficiency”.** Keep the residual visible and investigate the missing relation.

### MA.7:9 - Consequences

The user can respond to a difference with a more specific question and can avoid mistaking account changes for operating performance. A provisional explanation can support useful inquiry.

The result may stop short of a causal conclusion. Its next evidence demand should be proportionate to the decision the explanation can change.

### MA.7:10 - Architectural Rationale

Comparison, decomposition and explanation are separated because each can fail independently. An account can be comparable yet poorly decomposed, or perfectly decomposed yet causally misunderstood.

A routine variance report is sufficient when its definitions and explanations remain adequate. A deeper resource model or inquiry is justified when a plausible alternative would change the response.

### MA.7:11 - SoTA-Echoing

The selected line combines resource-based accounting with explicit numerical decomposition and causal inquiry. Caspari and Caspari's opening fixture case supplies a historical reason to question local performance readings: a changed activity time can have a different consequence at the system constraint. MA.1 supplies the quantitative model; the applicable inquiry method supplies further evidence when a causal question remains.

ACCA's [flexible-budget treatment](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/budgeting1.html) develops the reference account at actual activity while retaining fixed and stepped behavior. Its [materials mix and yield treatment](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/mat-yield.html) develops intermediate accounts and the relation of a variance to its subdivisions. That treatment concerns the mix of input materials; §5.2 applies the accounting construction to the mix of output products. The objects and reference requirements must remain explicit.

§§4.1–4.3 separate comparable values, the construction of arithmetic components and supported explanations. The five intermediate accounts expose when an apparent usage problem is fully explained by output mix. Their construction warrants the numerical division, while a cause or responsibility judgement requires further evidence. Reopen the explanation when changed mix, definitions or operating evidence defeats its comparison or cause.

### MA.7:12 - Relations

MA.1–MA.4 supply model and account meanings. MA.5 consumes supported changed assumptions; MA.9 examines behavioral explanations. An established resource or demand change can also invalidate an activity design: MA.10 then reconstructs an economically supportable alternative. The arithmetic difference alone does not establish that such a redesign is needed. OPS.15 supplies event and observation definitions, and the relevant operating or financial method decides the response. C.11.DUA supports a disputed further-inquiry choice.

### MA.7:End
