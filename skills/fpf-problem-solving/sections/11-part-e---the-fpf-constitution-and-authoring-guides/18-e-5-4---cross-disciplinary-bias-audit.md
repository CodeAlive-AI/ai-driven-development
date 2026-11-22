## E.5.4 - Cross‑Disciplinary Bias Audit

> **Status:** Stable

### E.5.4:1 - Problem frame
Use this pattern when you write or review a normative pattern and need to check its assumptions, explain an established rule to its readers, or decide where the rule applies. A familiar example can conceal who makes a decision, which parts have to work together or what a record actually establishes. The audit helps you find such assumptions. To recommend the rule in another discipline, establish what entitles a practitioner there to take the proposed action or draw the proposed conclusion.

### E.5.4:2 - Problem
Bias in wording, examples, unit choices or principle weighting can make a rule appear applicable where its assumptions do not hold. This undermines **P-2 Didactic Primacy** and **P-8 Cross-Scale Consistency**. The author needs to justify the emphasis, repair the imbalance or state a narrower scope.


### E.5.4:3 - Forces

| Force | Tension |
|-------|---------|
| **Shared meaning** | How can an example be familiar to readers in its domain while keeping the pattern’s meaning clear to readers in other domains? |
| **Conciseness** | Audit guidance must be brief and must cover several types of bias. |
| **Longevity** | Guidance must remain usable as new domains emerge. |

### E.5.4:4 - Solution — Principle‑Taxonomy‑Guided Bias Audit

**Examine the rule from all five classes in E.3.** Gov asks who can decide or change what the rule relies on. Arch asks which parts, interfaces or invariants the result depends on. Epist asks what the terms refer to and what supports the inference. Prag asks whether the work is feasible and worth doing for its intended use. Did asks what the reader needs to recognize and do in their role, with the help available for the intended use. If independent performance is promised, check which choices the reader must make. For each, ask whether the emphasis is justified and whether an omission would change how someone uses the rule. E.3:4.1 assigns a principle to one class for precedence. Here the same rule is examined from all five. Give each concern the weight its effect on use warrants.

**State what carries across disciplines.** Express the rule without its example. Name the action or conclusion it licenses and the conditions it relies on. For each discipline in which you claim it applies, explain what plays the relevant parts there and how its practice supplies the conditions. One argument can cover several disciplines when their definitions or work arrangements establish the same relation. A case can illustrate how to use that argument. A shared word, an attractive analogy or successful joint work can suggest a transfer to investigate.

Match the grounds to the conclusion. A derivation together with a warranted interpretation can establish what follows under specified conditions. For a predicted change in performance, use an adequate comparison in the receiving practice or explain why evidence from elsewhere bears on the effect under the receiving conditions. Account for material differences such as workload or case mix. To say who may act, recover the decision or rule that gives that authority. Where a condition is unknown, state what the recipient can already conclude and what they would have to establish for the further use.

**Test the boundary.** If a plausible alternative gives a different conclusion, try a case that decides between the two. A derivation can already settle the claim throughout the stated scope. If an instance meets the stated conditions and contradicts a factual conclusion asserted for every such instance, revise that claim. For a normative rule, distinguish breaking the rule from a valid exception to it. An unauthorized release can show a violation. An authorized exception can disprove the claim that every release requires the same approval. To retain a narrower rule, name a condition the practitioner can establish independently of the promised result and show why the conclusion follows within it. A case outside the conditions can expose a limit to use. It can also defeat a separate promise that every intended recipient will meet those conditions. For a claim about frequency or average effect, examine what the observations support about that frequency or effect.

**Report the material result.** The Bias-Annotation records the justified emphasis and any repair or scope limit that changes use. If a local rule is intended for one practice, explain the local condition that matters. For universal-core placement of a durable U-kind, A.8:3 and E.24.UK govern the projections into at least three foundationally different domain families and the other admission conditions. Workflow checklists, reviewer metadata and data-format advice belong outside Core.

### E.5.4:5 - Archetypal Grounding (System / Episteme)

When can an earlier check help settle a later acceptance criterion? Combine what it established with the other evidence available for the relevant item and state. First check that at least one situation fits the evidence. Conflicting records may need reconciliation. If all the possibilities that fit meet the criterion, the receiver can accept that aspect. If they all fail it, the receiver can reject it. If both remain possible, report the established part or obtain the observation that decides between them. An applicable risk rule may also authorize action on incomplete evidence. Other acceptance criteria and the authority to release the item keep their own force.

In mechanical inspection, the gauge reads 20.01 mm on an identified shaft. For this check the inspection procedure warrants an absolute error bound of 0.01 mm. The whole interval fits a receiving tolerance of 19.95–20.05 mm. If the measurement is valid for the shaft in its present state, the inspector can accept its diameter. A reading of 20.20 mm with the same bound settles rejection. Two checks can also settle acceptance together, one establishing the lower limit and the other the upper limit for that shaft in the same state. A requirement for performance under load still calls for evidence about the loaded assembly. Suppose the shaft passes the diameter check but a damaged keyway lets the assembly slip during its rated-load test. That outcome defeats the stronger rule that passing the diameter check guarantees performance under load. The diameter finding still holds.

In archival description, the receiving question might be which date the accession register gives for a photograph. A verified link from the photograph's identifier to its register entry and a legible entry giving the date settle that question. Dating the exposure itself requires grounds for interpreting the entry as a reliable record of the exposure date. An accession date can be entirely correct and still answer a different question. These two disciplines support the same conditional principle. Whether either team saves time by reusing checks is a further empirical question.

A reader who can follow the inspection example may still need help recognizing which archival date matters. Explain the receiving criterion in the archivist's vocabulary. The distinction between what the record establishes and what the next decision requires survives that change of wording.

### E.5.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑BA.1** | Each Core pattern **SHALL** include a *Bias-Annotation* stating the material result of the five-lens examination and any justified scope limitation. | Makes the audit’s conclusion usable. |
| **CC‑BA.2** | A pattern labelled “universal” **MUST NOT** privilege a single lens without justification or scoping note. | Preserves trans‑disciplinary integrity. |
| **CC‑BA.3** | The pattern **SHALL** justify its declared scope, give or cite the correspondence and its limits for any claimed or required translation between domains, and give the interpretation and grounds for the receiving action or inference for any claimed or required use in another discipline. | A reader can check an identifier translated between two collections in one discipline as well as a rule applied across disciplines. |
| **CC‑BA.4 Universality claim and applicable evidence** | A pattern labelled **“universal”** identifies the ClaimScope for that claim, the population or bearer it covers, its qualification window, and its intended use. When the claim is universal-core placement for a durable U-kind candidate governed by **E.24.UK**, apply **A.8:3**'s complete cross-domain projection test. `Diversity_P` or `IlluminationSummary` supports that test only through its governing C.17, C.19, or direct pattern. Neither is a standalone gate. | Keeps the claimed scope and its applicable evidence explicit. |

### E.5.4:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Readers can identify the claim's scope and the assumptions that constrain transfer. | Authors must examine the five lenses and explain a declared limitation. |
| The audit can expose domain-specific assumptions during drafting. | — |

### E.5.4:8 - Rationale
Using the Principle Taxonomy classes as the audit lenses keeps the guard‑rail **concept‑driven**. Review-board procedures, CI jobs, and workflow checklists belong in Tooling. This separation satisfies **GR‑1** (Firewall) and supports Pillars **P‑2, P‑7 Pragmatic Utility, P‑8**.

### E.5.4:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)
* **Depends on:** `pat:constitution/principle‑taxonomy` (E.3)
* **Constrains:** All normative patterns claiming universality

### E.5.4:End
