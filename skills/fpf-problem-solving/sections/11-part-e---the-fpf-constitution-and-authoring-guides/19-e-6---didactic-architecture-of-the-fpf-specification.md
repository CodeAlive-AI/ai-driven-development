## E.6 - Didactic Architecture of the FPF Specification

> **Status:** Stable

### E.6:1 - Problem frame
Use this pattern when arranging the specification's explanation and practical entry. Readers differ in at least two respects:

* **Disciplinary background** — for example, systems engineering, knowledge science or ethics.
* **Preparation** — some readers need help seeing a relation in use. Others can enter through the definition or operation that answers their question.

### E.6:2 - Problem
The publication needs an explanatory order in which readers can find the grounds needed for later claims. A practical question may require entry into a later Part. Document order must not become a compulsory workflow.


### E.6:3 - Forces

| Force | Tension |
|-------|---------|
| **Cognitive Load** | Formal detail supplies grounds for later reasoning, but too much detail at the outset can obscure the opening explanation. |
| **Conceptual Integrity** | A general account must preserve the distinctions its reader needs. A concrete case can reveal one of them while supplying a choice that the reader needs to learn to make. |
| **Didactic order vs practical entry** | The order of Parts is stable, while a first practical route that fits the reader’s question may cross Parts. |

### E.6:4 - Solution — Order the explanation and keep practical entry separate

#### E.6:4.0 - Document order is distinct from first-practical entry

The document's macro-order organizes explanation. It does not prescribe one practical workflow. Apply `E.11.PFP` to the compact opening and navigation.

After the Table of Contents, the Readme offers recognizable working questions and direct entries. The Architectural Reference explains the whole pattern language, its cross-cutting ideas, connections and architectural choices, including introductory explanation.

Choose the opening from the reader’s question. What are they trying to understand, do or construct? Which whole, constituent or relation is the question about, and what must the model let them distinguish? Begin where the reader can obtain the first grounds or perform the first operation they need. Follow its contribution to the promised result across Parts when necessary. E.11 helps when several plausible entries would lead to different work.

Keep the main explanatory sequence recoverable:

1. **Readme and Architectural Reference.** The Readme helps the reader find a first useful result. The Architectural Reference shows how to connect contributions when the reader needs a conclusion about a whole arrangement. In FPF.Reference:16.1, a promising result for one review activity leads to a question about the feasibility of the complete review.
2. **Part A — Kernel Architecture.** Introduce the holonic ontology and acting-side externalization in A.12.
3. **Part B — Trans-disciplinary Reasoning.** Explain the reasoning moves and their grounds for the kinds of things each question concerns. Use E.7 to show how the reasoning applies.
4. **Part C — Kernel Extension Specifications.** Develop the calculi and extension patterns whose questions use those foundations.
5. **Part D — Multi-scale Ethics and Conflict Optimization.** Introduce the reflective ethical and conflict questions with the needed holonic distinctions available.
6. **Part E — Constitution and Authoring Guides.** Place framework governance and contributor guidance after the principal kernel and reasoning exposition so an ordinary first use need not begin with authoring rules.
7. **Part F — Unification Suite.** Keep concept-set, sense and system-role unification methods in their own Part. Reach them directly when the question calls for them.
8. **Part G — Discipline SoTA Patterns Kit.** Keep the discipline source-synthesis, comparison and refresh methods in their own Part.

Part H remains reserved. Examples and extended explanations belong with the pattern whose contribution they explain. Tooling guides and executable examples follow their separate family and lexical rules.

This publication order does not require readers to traverse every Part. Practical entries return to the pattern needed by the reader’s question.

### E.6:5 - Archetypal Grounding (System / Episteme)

An author preparing a reading route first needs to know what the reader will use the conclusion for. In FPF.Reference:16.1 a team wants to know whether it can rely on a proposed report-review arrangement. The early trial timed extraction. The author leads the reader from that finding to the work still required for checking and final review. For the specified weekly workload, the three activities are estimated to require 15 hours from an engineer with 10 available. Even another five hours for that same engineer would leave a missing checker if that person must be independent of the extractor. Those relations explain why improving extraction alone cannot settle the team's question.

For a question about constituents, choose the definition and application that let the reader reach the needed conclusion.

| Reader’s question | Where to obtain the distinction | What the reader can decide with it |
|---|---|---|
| What belongs to the pump skid being aggregated? | A.1:4.4 gives the System criterion. B.1.2:5.1 distinguishes installed parts from dependencies across the skid boundary. | The pump can enter the skid inventory. The external supply can matter to operation even when it is outside that inventory. For a conclusion about operation the reader must also account for this dependency. |
| What guidance does a bundle of studies support? | A.1:4.5 gives the Episteme criterion. B.1.3:5.1 shows how study claims and their conditions enter a synthesis. | The reader can qualify the guidance where the results apply under different conditions or conflict. A count of the studies alone cannot establish which conclusion holds. Use C.2.2 when the grounds for reliance on a claim need separate assessment. |

A direct entry suffices when the question ends with the distinction it gives. For a question about relying on the whole, carry the result back to that decision and follow any still-missing dependency.

### E.6:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC‑DA.1** | Each Part **SHALL** open with a one-paragraph situational introduction before formal text. |
| **CC‑DA.2** | Every architectural pattern **MUST** ground its rule under E.7 in the practitioner's question, the kinds of things it concerns and the relation that warrants the answer. |
| **CC‑DA.3** | Governance patterns (**Part E**) **SHALL NOT** appear before the Kernel in the main document flow. |
| **CC‑DA.4** | Navigation aids **SHALL** distinguish document order from first-practical entry guidance. First-entry pattern-comparison guidance and expanded entry-disambiguation cases are informative and MAY cross Parts without implying a universal process history. |

### E.6:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Readers can choose introductory explanation or direct entry to the pattern they need. | Authors must maintain the explanation and entry guidance under E.8. |
| Grounding can be read beside the claims it explains. | When an introductory route changes, follow it to the indicated application and check what the reader can now conclude there. |

### E.6:8 - Rationale
A reader needs grounds for using the rule in the work at hand. A direct demonstration can establish them. A contrasting application earns its place when it reveals a condition that the first leaves open. The document order and E.7 make those grounds accessible while practical entries can cross Parts. This serves **P‑2 Didactic Primacy** and **P‑1 Cognitive Elegance**.

### E.6:9 - Relations
* **Depends on:** `pat:constitution/guard‑rails` (GR-1 governs implementation detail and necessary subject syntax).
* **Constrains:** Placement of Parts, patterns, and their explanatory examples.
* **Instantiates pillars:** P‑1, P‑2

### E.6:End
