## E.6 - Didactic Architecture of the FPF Specification

### E.6:1 - Problem frame
FPF addresses readers who differ in at least two respects:

* **Disciplinary** – systems engineers, knowledge scientists, ethicists.
* **Experience** – newcomers need intuition; experts need rigour.

Past drafts mixed governance mandates with domain examples, producing a
steep learning curve and repeated “forward‑reference” detours.

### E.6:2 - Problem
If core ideas are buried under formalism or scattered across parts,
readers either give up or misuse the framework. We need a didactic
macro-order that guides cognitive load from low to high while keeping
normative sections discoverable, without letting readers confuse
document order with one universal first-practical workflow.

### E.6:3 - Forces

| Force | Tension |
|-------|---------|
| **Cognitive Load** | Early clarity ↔ eventual formal depth. |
| **Conceptual Integrity** | Foregoing examples risks abstraction ↔ too many examples delay axioms. |
| **Didactic order vs practical entry** | Stable document macro-order ↔ truthful first-practical routes that may cross parts. |

### E.6:4 - Solution — Order the explanation and keep practical entry separate

#### E.6:4.0 - Document order is distinct from first-practical entry

The macro-order of the document is a didactic scaffold, not a universal practical workflow. Apply `E.11.PFP` to the compact opening and navigation. After the Table of Contents, the Readme offers recognizable working questions and direct entries; the Preface supplies the informal on-ramp. These informative navigation units and ToC cues may cross Parts when the reader's question requires it. Use `E.11` for practical entry and `I.2` for expanded entry-disambiguation cases.

Keep the main explanatory sequence recoverable:

1. **Readme and Preface.** The Readme helps a reader find a first useful result. The Preface builds intuition through concrete System and Episteme stories before the kernel exposition.
2. **Part A — Kernel Architecture.** Introduce the holonic ontology and acting-side externalization in A.12.
3. **Part B — Trans-disciplinary Reasoning.** Connect the general reasoning moves with applicable System and Episteme grounding under E.7.
4. **Part C — Kernel Extension Specifications.** Develop the calculi and extension patterns whose questions use those foundations.
5. **Part D — Multi-scale Ethics and Conflict Optimization.** Introduce the reflective ethical and conflict questions with the needed holonic distinctions available.
6. **Part E — Constitution and Authoring Guides.** Place framework governance and contributor guidance after the principal kernel and reasoning exposition so an ordinary first use need not begin with authoring rules.
7. **Part F — Unification Suite.** Keep concept-set, sense and system-role unification methods in their own Part; reach them directly when the question calls for them.
8. **Part G — Discipline SoTA Patterns Kit.** Keep the discipline source-synthesis, comparison and refresh methods in their own Part.
9. **Part H and Part I.** Part H remains reserved; Part I carries annexes and extended tutorials. Tooling guides and executable examples follow their separate family and lexical rules.

This publication order does not require readers to traverse every Part. Practical entries return to the pattern needed by the current question.

### E.6:5 - Archetypal Grounding (System / Episteme)

| Narrative layer | First sight of `U.System` | First sight of `U.Episteme` |
|-----------------|---------------------------|-----------------------------|
| Preface | Coffee‑machine story (pump as system). | Meta‑analysis story (study bundle as episteme). |
| Part A | Formal definition states the System criterion and applicable boundary conditions. | Formal definition states the Episteme criterion; F‑G‑R coordinates characterize a claim under the C.2.2 profile. |
| Part B Tell‑Show‑Show | Γ\_sys example: assemble pump. | Γ_epist example: merge study bundle. |

### E.6:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑DA.1** | Each Part **SHALL** open with a one‑paragraph situational “hook” before formal text. |
| **CC‑DA.2** | Every architectural pattern **MUST** supply the grounding required by E.7: applicable System and Episteme illustrations, or the explicit single-substrate scope and justification under CC‑AG.3. |
| **CC‑DA.3** | Governance patterns (**Part E**) **SHALL NOT** appear before the Kernel in the main document flow. |
| **CC‑DA.4** | Navigation aids **SHALL** distinguish document order from first-practical entry guidance; first-entry pattern-comparison guidance and expanded entry-disambiguation cases are informative and MAY cross Parts without implying a universal process history. |

### E.6:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Smooth learning curve; readers can stop at their needed depth. | Template discipline required; mitigated by authoring guide (E.8). |
| Reduces forward‑reference clutter; each concept is primed before formal use. | Preface evolves when new archetypes added; handled via On‑Ramp revision DRR. |

### E.6:8 - Rationale
Pairing an abstract rule with contrasting, applicable illustrations makes its intended application and scope inspectable. The document order and E.7 grounding rule provide those connections while leaving practical entries free to cross Parts. This implements **P‑2 Didactic Primacy** and **P‑1 Cognitive Elegance** without replacing the subject's reasoning or evidence.

### E.6:9 - Relations
* **Depends on:** `pat:constitution/guard‑rails` (GR‑1 ensures example jargon stays outside Core).
* **Constrains:** Placement of all Parts, patterns, and appendices.
* **Instantiates pillars:** P‑1, P‑2

### E.6:End
