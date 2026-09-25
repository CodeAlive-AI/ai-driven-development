## A.9 - Choose and Check an Aggregation Law for the Intended Result

### A.9:1 - Context

**Use this when** a receiving decision needs a combined result, but the law that gives the proposed operation its meaning or preserves a needed property is unresolved. The same input values can support different operations: component success probabilities combine differently for “both succeed” and “at least one succeeds”. Reordering functions can change their result even when the notation looks like an ordinary fold.

The first useful result is a justified combining law with its applicable conditions, a supported limited result or bound, retained separate inputs, or the exact missing premise. Reuse an adequate domain law and its current applicability result without creating another A.9 record.

**Non-use boundary.** B.1 governs whole/part construction, C.29 governs mathematical representation and correspondence, and ULSAM performs an explicitly selected CHR fold over admitted measures. None supplies one universal aggregation algebra. Use their direct results when they already answer the question; A.9 supplies only the unresolved law-selection or property check. Composition of functions or Methods does not require a measured quantity merely to enter this pattern.

### A.9:2 - Problem

| Failure | Practical consequence |
|---|---|
| An operation is chosen from the numbers alone. | A sum, minimum or product answers a different question from the one the receiver needs. |
| A roll-up hides dependence, overlap or interaction. | Repeated evidence is counted as independent, or component claims are promoted to an unsupported whole claim. |
| Reordering or repartitioning is assumed harmless. | Ordered Methods or numerical computation return a different result. |
| Failure of an aggregation model is treated as a new whole. | A repairable model premise is confused with the independent identity question. |

### A.9:3 - Forces

| Force | Tension |
|---|---|
| Simple operation, faithful meaning | A compact formula must still express the intended result under the actual subject model. |
| Reuse, changed conditions | Retain a justified law while reopening the specific dependence or applicability premise that changed. |
| Local work, combined result | Parallel or separate computation helps only when its recombination preserves what the receiving use needs. |
| Useful answer, incomplete basis | A bound or separate inputs can be a better answer than an unsupported scalar. |

### A.9:4 - Solution — Select the Law Before Relying on Its Result

1. **Name the intended result and operands.** State what the combination must mean, which inputs contribute and what operation is proposed. For reliability, distinguish joint success from alternative success. For a composed Method or function, retain the intended order and participant meanings.
2. **Recover the subject model and conditions.** Identify dependence, overlap, interaction, grouping and numerical interpretation where they change the result. For quantities, also recover the Characteristic, Scale, units and measurement conditions. Use C.29 when the representation or its correspondence to the subject is unresolved; mathematical notation alone is not that correspondence.
3. **Select a justified law.** Use the direct domain source or Method that supports this operation for this result. Reuse its current applicability judgment when adequate. If no available law is justified, name the missing model or condition; do not pick a convenient average or a generic weakest-part rule.
4. **Check the property needed by the current action.** A requested reorder needs an order-invariance claim; a repartition needs valid decomposition and recombination; a bound needs the model that warrants it. For a numerical reproducibility claim, state whether the use requires the same exact value, the same bits, or an error bound before accepting a regrouping. Use the applicable argument or warranted test under those conditions. The table below supplies possible questions, not a compulsory set of five checks.
5. **Return the warranted answer and limit.** Apply the justified law, or return a supported bound, separate inputs or the exact missing/defeated premise. If a condition changes, withdraw only the conclusion that depended on it and recover the needed model. Pass an actual CHR measure fold to ULSAM when that mechanism use is current. Use B.3 only for a receiving claim that requires assurance.

Describing the choice does not perform the fold, establish parthood or authorize reliance. No additional record is needed when the law, inputs, conditions and answer are already recoverable in the working account.

#### A.9:4.1 - Select Only the Relevant Property

| Property or legacy code | Question and applicability |
|---|---|
| Singleton base case — **IDEM** | If the construction has this requirement, does a one-element input return the corresponding element? This differs from algebraic idempotence `x ⊕ x = x`. Repeated sources need their own dependence treatment. |
| Reordering — **COMM** | Does exchanging the operands preserve the intended result under the actual operation and model? Keep order when it is consequential. Commutativity alone does not establish independence of the observations. |
| Repartitioning or moving computation — **LOC** | Do the declared decomposition, recombination and numerical conditions preserve the required result? Exact arithmetic and floating-point implementations may answer differently. |
| Weakest-part bound — **WLNK** | Does the specified result and dependency model justify this bound? A bound need not be the exact result, and it is not a cap on every aggregate. |
| Monotonicity — **MONO** | Under which input/output order and side conditions can improving an input not worsen the result? Interactions can defeat the proposed claim. |

A layered-control contract may state a reference signal, guaranteed tracking error and cycle time. Check the needed composition property under its control model. Possessing that contract alone proves neither reordering nor repartitioning valid.

#### A.9:4.2 - Keep Whole Reidentification Separate

If observations defeat a law's premise, reopen the model, applicability conditions and resulting claim. B.2 is needed only when the current question also concerns whether the existing whole still satisfies its identity rule. A failed aggregation model alone neither identifies a new whole nor establishes a Meta-Holon Transition.

### A.9:5 - Archetypal Grounding

These six cases are constructed model checks, not empirical performance reports. Read each row from the intended result through its model to the warranted answer.

| Intended result and stated model | Selected law, result and limit |
|---|---|
| Total of disjoint exact resource contributions 2 and 3 on one additive quantity scale | Addition gives `2 + 3 = 5` under B.1.6. No weakest-part cap applies to this total; exceeding either part creates no new whole. |
| Probability that both independent components succeed, with probabilities .9 and .8 | The joint-success model selects multiplication: `.9 × .8 = .72`. A minimum would not calculate that probability. |
| Probability that at least one of those same independent components succeeds | The alternative-success model selects `1 - (1-.9)(1-.8) = .98`. Identical marginals and unchanged components support a different law because the intended event changed. |
| Compose `f(x)=x+1` and `g(x)=2x` in the required order | `g(f(x))=2x+2` differs from `f(g(x))=2x+1`. Keep the order; no Characteristic or measurement Scale is required for this function-composition claim. |
| Reorder or repartition disjoint exact additive resource contributions | Exact addition permits the stated reorder and regrouping. That argument establishes neither arbitrary floating-point regrouping nor independence of repeated-source evidence. Check the actual numerical and source conditions when they matter. |
| New evidence defeats independence in the reliability cases, while the assembly retains its identity | Withdraw the .72/.98 computations that used independence. Obtain a justified dependence model or return only a supported bound or the separate marginals. The same assembly remains the subject unless its independent identity rule requires a different conclusion. |

For the additive construction, the singleton base case returns 2 from the one-element input `[2]`. It does not claim `2 + 2 = 2`. Nor does writing the same observation twice create two independent observations.

### A.9:6 - Conformance Checklist

| ID | Requirement | Purpose |
|---|---|---|
| **CC-A9-1** | Name the intended result, inputs, operation, subject model, applicability conditions and justified law. Add Characteristic, Scale, units and measurement conditions for the quantitative branch. | Recover what the result means without excluding non-quantitative composition. |
| **CC-A9-2** | Select only the property needed by the current action and supply its applicable argument or warranted test. Distinguish singleton identity from idempotence and repeated-source handling. | Avoid a compulsory universal algebra. |
| **CC-A9-3** | Claim order or partition independence only under the actual model and recombination/numerical conditions. | Preserve lawful sequential or parallel composition. |
| **CC-A9-4** | Use a weakest-part bound only for a result and dependency model that justify it; distinguish a bound from a calculated value. | Prevent both unsupported optimism and a false universal cap. |
| **CC-A9-5** | Return the warranted result, bound, separate inputs or missing premise; reopen the conclusion when its supporting condition fails. | Make incomplete evidence usable without inventing a scalar. |
| **CC-A9-6** | A claimed Meta-Holon Transition satisfies B.2's existing-whole comparison and the candidate whole's identity rule. | Keep reidentification independent of a model failure. |

### A.9:7 - Consequences

The practitioner can explain why the chosen operation answers the actual question and what would defeat it. A combined result remains usable only while the stated model and conditions apply. Lawful reordering or repartitioning can support distributed calculation; it does not guarantee that independently developed Systems will integrate without other work.

The cost is recovering the domain meaning, dependencies and any property required by the action. A sufficient existing law can make this cheap. When its basis is absent, a qualified bound or retained inputs preserves useful information and exposes the missing premise. New-whole recognition remains a separate B.2 decision.

### A.9:8 - Rationale

A common Γ notation locates a construction but cannot choose between joint success, alternative success, additive accounting and ordered composition. Those results have different laws even when some inputs or symbols coincide. Selecting the receiving meaning before the operation prevents a syntactically valid calculation from answering the wrong question.

Checking only the needed property also keeps the burden proportionate. A request to reorder exact additive contributions requires a different argument from a safety bound or a floating-point reproducibility claim. Retaining that distinction preserves a supported result while a different property remains unknown.

### A.9:9 - Relations

| Pattern | Contribution and boundary |
|---|---|
| A.1 and B.1 | Identify the whole, parts and construction when those are the subjects; they supply no universal aggregation algebra. |
| A.7 | Keeps the mathematical operation, its subject, performed Work and claims about its result distinct. |
| A.8 | Tests a proposed durable U-kind's universal-core placement only when that separate admission question is live. |
| C.29 | Governs the mathematical representation and its subject correspondence; domain theory supplies the application law. |
| A.19.CN, A.19.CHR and A.19.ULSAM | CN records the selected characteristic basis and aggregation claim; ULSAM operates the selected CHR fold under its own admissibility and scale rules. A.9 settles an unresolved choice or needed property before reliance. |
| B.1.5 and B.1.6 | Supply direct Method-composition and resource-accounting rules for those uses. |
| B.3 | Supplies assurance when the receiving claim requires it. |
| B.2 | Governs whole reidentification independently of aggregation-law failure. |

### A.9:10 - Application situations

Apply the method to an unresolved choice in resource combination, joint or alternative reliability, control composition, numerical regrouping or ordered Methods. Use the actual subject source for the intended result and its applicability; the examples establish no universal cross-scale guarantee or empirical performance benefit.

### A.9:11 - SoTA-Echoing

**Practice question.** Which law, and which property check, preserve the intended result when dependence, order or numerical interpretation matters?

The selected line separates the subject model from the permitted computation. For the reliability branch, the NIST/SEMATECH *e-Handbook*, [§8.1.8.2, series model](https://www.itl.nist.gov/div898/handbook/apr/section1/apr182.htm), and [§8.1.8.3, parallel model](https://www.itl.nist.gov/div898/handbook/apr/section1/apr183.htm), supply concrete competing laws with their independence and failure-event assumptions. **Adopt** that event-first choice in §4 steps 1–3 and §5's .72/.98 cases. With the same component data, neither a familiar product nor a minimum answers both questions. A minimum can still supply a bound where the intended event warrants it. These sources support those non-repairable or first-failure reliability models; they establish no law for every aggregate.

For computation, [MPI 5.0, §7.9.1, Reduce](https://www.mpi-forum.org/docs/mpi-5.0/mpi50-report/node132.htm), supplies the practical comparison. Its reduction contract permits regrouping under associativity and, where applicable, reordering under commutativity. It also recognizes that floating-point addition can change under those freedoms and advises enforcing an evaluation order when the application requires it. The source supplies both a serious parallel-reduction default and an explicit-order alternative, not proof that a caller's domain operation has the assumed properties.

**Adapt** this contract distinction in §4 step 4 and the `LOC` question. Given the same operands and required result, first check only the property needed for the proposed rearrangement. A tree reduction is appropriate when that property or an adequate error bound holds. An explicit ordered fold is the stronger answer when a particular evaluation order is part of the required result. It preserves that result at the possible cost of parallelism; it does not become the most accurate summation algorithm merely by fixing order. **Reject** treating acceptance by a reduction interface as evidence that rearrangement is harmless.

For a constructed binary64 calculation with round-to-nearest, ties-to-even, `(10^16 + (-10^16)) + 1` yields `1`, while `10^16 + ((-10^16) + 1)` yields `0`. The inputs, two additions and operand order are the same; grouping alone changes the answer. If the receiver requires the left-associated result, the second calculation fails that requirement. If a justified receiving tolerance permits both, this example alone does not forbid regrouping. Both candidates can be compared from the same operands and result requirement before choosing an implementation.

Reopen the selected law when the intended event or dependence model changes. Reopen only the affected computation claim when the numeric representation, allowed error, grouping or order changes. A stronger reduction method matters when it preserves the required result with a preferable cost; its speed alone does not establish the domain law.

### A.9:End
