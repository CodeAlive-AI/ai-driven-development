## E.5.4 - Cross‑Disciplinary Bias Audit

> **Status:** Stable

### E.5.4:1 - Problem frame
Use this pattern when authoring or reviewing a normative pattern's assumptions, examples and claimed scope. Wording and metaphors drawn from one domain can hide assumptions that readers in another domain need to recognize.

### E.5.4:2 - Problem
Bias in wording, examples, unit choices or principle weighting can make a rule appear applicable where its assumptions do not hold. This undermines **P-2 Didactic Primacy** and **P-8 Cross-Scale Consistency**. The author needs to justify the emphasis, repair the imbalance or state a narrower scope.


### E.5.4:3 - Forces

| Force | Tension |
|-------|---------|
| **Shared meaning** | Cross-domain interpretation ↔ relatable domain examples. |
| **Conciseness** | Audit guidance must be brief ↔ must cover multiple bias types. |
| **Longevity** | Guidance must survive emergence of new domains. |

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
   * If imbalance is intentional (domain‑specific pattern), mark the
     scope explicitly: *“Applies primarily to thermodynamic systems.”*

4. **Bias annotation**
   The pattern carries a short **Bias‑Annotation** paragraph naming the five lenses and any scoping statement. Keep workflow checklists,
   reviewer metadata and other data outside the Core, along with tips on data formats and data governance.

### E.5.4:5 - Archetypal Grounding (System / Episteme)

| Bias lens | Example imbalance | Conceptual correction |
|-----------|------------------|-----------------------|
| `Arch` vs `Did` | Pump pattern uses abstract category theory terms. | Add plain‑language boundary narrative or move abstraction to appendix. |
| `Epist` vs `Prag` | Episteme trust score defined with complex logic but no guidance on empirical cost. | Add pragmatic note on evidence collection cost or scope the pattern. |

### E.5.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑BA.1** | Each Core pattern **SHALL** include a *Bias‑Annotation* listing the five lenses and any declared scope limitation. | Ensures explicit reflection on bias. |
| **CC‑BA.2** | A pattern labelled “universal” **MUST NOT** privilege a single lens without justification or scoping note. | Preserves trans‑disciplinary integrity. |
| **CC‑BA.3** | If scope is declared, the pattern **SHALL** state its rationale. When cross-domain translation is claimed or required, it **SHALL** reference the mapping or rationale supporting that translation and state its limits. | Keeps pathways open for other calculi. |
| **CC‑BA.4 Universality claim and applicable evidence** | A pattern labelled **“universal”** states the exact ClaimScope, population or bearer, qualification window, and intended use of that claim. When the claim is universal-core placement for a durable U-kind candidate admitted through **E.24.UK**, apply **A.8:3**'s complete cross-domain projection test. `Diversity_P` or `IlluminationSummary` supports that test only through its governing C.17, C.19, or direct pattern; it is not a standalone gate. | Keeps the claimed scope and its applicable evidence explicit. |

### E.5.4:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Readers can identify the claim's scope and the assumptions that constrain transfer. | Authors must examine the five lenses and explain a declared limitation. |
| The audit can expose domain-specific assumptions during drafting. | — |

### E.5.4:8 - Rationale
Coupling the audit directly to the Principle Taxonomy keeps the guard‑rail
**concept‑driven**. Review-board procedures, CI jobs, and workflow
checklists belong in Tooling. This separation satisfies
**GR‑1** (Firewall)
and supports Pillars **P‑2, P‑7 Pragmatic Utility, P‑8**.

### E.5.4:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)
* **Depends on:** `pat:constitution/principle‑taxonomy` (E.3)
* **Constrains:** All normative patterns claiming universality

### E.5.4:End
