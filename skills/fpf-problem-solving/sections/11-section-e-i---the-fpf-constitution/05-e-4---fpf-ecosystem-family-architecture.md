## E.4 - FPF Ecosystem Family Architecture

### E.4:1 - Problem frame

The FPF ecosystem contains three maintained families: the normative Conceptual Core, executable or machine-checking Tooling Reference material, and learning-oriented Pedagogical Companion material. If these families are mingled without a clear architectural separation, the ecosystem becomes difficult to navigate, govern, and maintain. Users cannot easily distinguish binding rules from helpful advice, and the entire framework's release cycle becomes coupled to its most volatile component.

### E.4:2 - Problem

How can we structure the FPF ecosystem to ensure a clean separation of concerns between normative concepts, didactic materials, and executable tooling? A formal architecture is required to maintain conceptual purity, enable independent evolution of components, and provide a clear map for all stakeholders.

### E.4:3 - Forces

| Force | Tension |
| :--- | :--- |
| **Stability vs. Agility** | The conceptual core must evolve slowly and deliberately ↔ tools and tutorials must iterate quickly to keep pace with technology and user needs. |
| **Authority vs. Accessibility** | Users need to know which rules are normative and binding ↔ they also need accessible, non-normative guides to help them learn. |
| **Modularity vs. Cohesion** | The different FPF ecosystem families must be able to evolve independently <-> they must remain part of a single, coherent FPF ecosystem. |

### E.4:4 - Solution

The FPF ecosystem is formally stratified into three canonical **FPF ecosystem families**. Each family has a distinct purpose and is governed by different rules, ensuring a clear separation of concerns. The interaction between these families is governed by the **Unidirectional Dependency Principle** (see Guard-Rail E.5.3).

1.  **The Conceptual Core (The Canon):** This family contains the **normative** FPF patterns, kernel definitions, rules, and invariants. It is the canonical FPF pattern set for universal FPF content. It is defined to be tool-agnostic and notation-independent.

2.  **The Tooling Reference:** This family contains executable tools and machine-checkable support publications that implement or verify the normative rules of the Core. This includes reference linters, simulators, and data schemas. This family makes Core rules operational without becoming the Core pattern set.

3.  **The Pedagogical Companion:** This family contains **non-normative, didactic publications** designed to help humans learn and apply FPF. This includes tutorials, worked examples, and playbooks. This family explains the Core and the Tooling Reference without changing Core meaning.

### E.4:5 - Archetypal Grounding (System / Episteme)

*   **For a `U.System`:**
    *   **Conceptual Core:** Defines the universal pattern `U.System`.
    *   **Tooling Reference:** Provides a modeling language profile or a serialization schema for modeling systems.
    *   **Pedagogical Companion:** Provides a tutorial on how to model a water pump using that profile.

*   **For an `U.Episteme`:**
    *   **Conceptual Core:** Defines `U.Episteme` and the F-G-R assurance tuple components (`F/R` characteristics plus `G` as ClaimScope).
    *   **Tooling Reference:** Provides the reference linting tool to automatically score epistemes.
    *   **Pedagogical Companion:** Provides a case study on how a scientific theory's R-score evolves over time.

### E.4:6 - Conformance Checklist

| ID | Requirement |
| :--- | :--- |
| **CC-E.4.1** | Every FPF pattern, support publication, tool, or pedagogical publication **MUST** declare which of the three families (Core, Tooling, Pedagogy) it belongs to. |
| **CC-E.4.2** | The content of each family member **MUST** be consistent with the defined purpose of its family (e.g., no normative rules in the Pedagogical Companion). |
| **CC-E.4.3** | Tooling Reference and Pedagogical Companion family members SHALL NOT be imported by Conceptual Core patterns. |

### E.4:7 - Consequences

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Clear Separation of Concerns:** Users and contributors can immediately identify the nature and authority of any given FPF pattern, support publication, tool, or learning publication. | **Requires Discipline:** Authors must be careful to place new content in the correct ecosystem family. |
| **Decoupled Release Cycles:** The Core can maintain a stable, slow release cadence, while the Tooling Reference and Pedagogical Companion families can evolve rapidly. | - |
| **Architectural Clarity:** Provides a simple, powerful mental model for navigating the entire FPF ecosystem. | - |

### E.4:8 - Rationale

This pattern establishes the macro-architecture of the entire FPF ecosystem. By separating the normative Core from executable Tooling Reference material and learning-oriented Pedagogical Companion material, it creates a system that is simultaneously stable, agile, and accessible. This layered architecture is a proven pattern in large-scale systems, from the OSI model in networking to the structure of modern operating systems, and it is essential for FPF's long-term health and scalability.

### E.4:9 - Relations

*   **Instantiates:** **P-5 (FPF Layering)** at a macro-level.
*   **Is Constrained by:** **E.5.3 (Unidirectional Dependency)**.
*   **Is Foundation For:** The entire authoring and governance model, as it defines the "territories" where different rules apply.

> *“A canon without a rationale is scripture; a rationale without a canon is gossip. FPF keeps both, fused in patterns.”*

### E.4:End

