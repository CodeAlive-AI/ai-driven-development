## E.5.4 - Cross‑Disciplinary Bias Audit

> **Status:** Stable

### E.5.4:1 - Problem frame
Use this pattern when authoring or reviewing a normative pattern's assumptions, examples and claimed scope. Wording and metaphors drawn from one domain can hide assumptions that readers in another domain need to recognize.

### E.5.4:2 - Problem
Bias in wording, examples, unit choices or principle weighting can make a rule appear applicable where its assumptions do not hold. This undermines **P-2 Didactic Primacy** and **P-8 Cross-Scale Consistency**. The author needs to justify the emphasis, repair the imbalance or state a narrower scope.


### E.5.4:3 - Forces

| Force | Tension |
|-------|---------|
| **Shared meaning** | How can an example be familiar to readers in its domain while keeping the pattern’s meaning clear to readers in other domains? |
| **Conciseness** | Audit guidance must be brief and must cover several types of bias. |
| **Longevity** | Guidance must remain usable as new domains emerge. |

### E.5.4:4 - Solution — Principle‑Taxonomy‑Guided Bias Audit

1. **Bias‑Lens set**
   Every normative pattern is assessed through **five lenses** that match the
   Principle classes from **E.3**:
   `Gov`, `Arch`, `Epist` (epistemological and ontological), `Prag`, `Did`.

2. **Equilibrium question**
   For each lens ask:
   *“Does the pattern give this class more weight than its use justifies, or omit a concern from this class that changes use?”*
   *Examples:*
   *   Over‑reliance on `Epist` precision may ignore `Prag` cost.
   *   An `Arch` metaphor may hide meaning the `Did` audience needs.

3. **Scope‑or‑Balance rule**
   * If an unjustified imbalance is found and universality is intended, revise the claims or explanation to correct the weighting or address the neglected concern.
   * If a domain‑specific pattern has an intentional imbalance, state its scope. For example, *“Applies primarily to thermodynamic systems.”*

4. **Bias annotation**
   The pattern carries a short **Bias-Annotation** reporting the result of the five-lens examination, including any material weighting, its justification, and the scope or correction needed for the intended use.

   Keep workflow checklists, reviewer metadata and other data outside the Core, along with tips on data formats and data governance.

### E.5.4:5 - Archetypal Grounding (System / Episteme)

| Bias lens | Example imbalance | Conceptual correction |
|-----------|------------------|-----------------------|
| `Arch` vs `Did` | A pump pattern uses abstract terms from category theory. | Add a plain-language account of the boundary or move the abstraction to an appendix. |
| `Epist` vs `Prag` | The definition of an episteme trust score uses complex logic but gives no guidance on empirical cost. | Add a note on the cost of collecting evidence or limit the pattern's scope. |

### E.5.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑BA.1** | Each Core pattern **SHALL** include a *Bias-Annotation* stating the material result of the five-lens examination and any justified scope limitation. | Makes the audit’s conclusion usable. |
| **CC‑BA.2** | A pattern labelled “universal” **MUST NOT** privilege a single lens without justification or scoping note. | Preserves trans‑disciplinary integrity. |
| **CC‑BA.3** | If scope is declared, the pattern **SHALL** state its rationale. When cross-domain translation is claimed or required, it **SHALL** reference the mapping or rationale supporting that translation and state its limits. | Keeps pathways open for other calculi. |
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
