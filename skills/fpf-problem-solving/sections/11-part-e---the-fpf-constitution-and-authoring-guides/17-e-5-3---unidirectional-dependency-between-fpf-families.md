## E.5.3 - Unidirectional Dependency between FPF Families

> **Status:** Stable

### E.5.3:1 - Problem frame
Use this pattern when an FPF artefact imports or otherwise depends on another artefact. FPF separates the Conceptual Core, Tooling Reference and Pedagogical Companion under E.4. The dependency direction must preserve that separation while allowing the outer families to change.

### E.5.3:2 - Problem
A Core pattern can become dependent on a tutorial or helper feature introduced for a local need. Changes to that feature then require reconsidering Core content even when its conceptual subject is unchanged. A cycle prevents the layers from being revised independently and violates **P-5 FPF Layering**.


### E.5.3:3 - Forces

| Force | Tension |
|-------|---------|
| **Agility vs Stability** | Tooling must iterate quickly, while changes to Core must remain slow and deliberate. |
| **Reuse vs Isolation** | Authors want to reuse helper concepts, but Core cannot depend on volatile code. |
| **Simplicity** | The rule must be testable and unambiguous and must allow legitimate upward imports. |

### E.5.3:4 - Solution — One‑Way, Acyclic Imports
Define a strict **partial order** over FPF ecosystem families. Imports between families point only **upward** in stability. Also protect the direction of meaning flow under **E.10 V-1**: **no Core semantics** may derive from Tooling or Pedagogy. The Conceptual Core excludes linters and machine checking.

**`imports` expresses dependency. Specialisation is a separate relation (normative).** When an artefact exposes an `imports : [...]` list (e.g., `SignatureManifest.imports` in A.6.0), treat each dependency claim in the list as an edge of its `imports` graph. The graph MUST be **acyclic** (a DAG) and MUST respect the declared direction.

`imports` MUST NOT be used to encode *specialisation* (e.g., `⊑` / `⊑⁺` between mechanisms). Specialisation relations and any specialisation-chain claims are declared separately under their defining rules. For mechanism declarations, apply A.6.1:4.8 to the comparison claim. Use C.29 when a separate mathematical-representation choice, transfer or reliance question remains.

Pedagogical Companion  ⟶  Tooling Reference  ⟶  Conceptual Core

1. **Allowed edges**
   Dependencies between families **MAY** point **only upward** (toward greater semantic
   stability). Cycles are forbidden.

2. **No downward import**
   Conceptual Core patterns **SHALL NOT** import Tooling Reference or Pedagogical Companion family members.
   Tooling Reference family members **SHALL NOT** import Pedagogical Companion family members.

3. **Future layers**
   Any new family is inserted below an existing one or becomes part of
   the Tooling or Pedagogy strata. The ordering extends accordingly.

### E.5.3:5 - Archetypal Grounding (System / Episteme)

| Layer | `U.System` illustration | `U.Episteme` illustration |
|-------|------------------------|---------------------------|
| Core | Definition of `U.System` and boundary invariant. | Definition of F‑G‑R assurance components. |
| Tooling | The “Reference system‑profile” checks boundary flow and *imports* Core invariants. | The “Episteme‑scoring routine” calculates R‑score and *imports* Core characteristics. |
| Pedagogy | A tutorial uses the system‑profile to model a pump and *imports* the profile and Core term. | A case study explains R‑score evolution and *imports* the scoring routine and Core term. |
| **Forbidden** | Core pattern importing measurement script. | Core pattern importing R‑score web dashboard. |

### E.5.3:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC-UD.1** | Dependency graph among all FPF ecosystem family members **MUST** be acyclic. |
| **CC-UD.2** | A family member **SHALL** import only from its own family or any family above it in the order. |
| **CC‑UD.3** | A DRR that introduces a downward edge **SHALL** be automatically rejected. |

### E.5.3:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core stays free of tool churn and tutorial bias. | Authors must create abstraction layers in Tooling instead of inserting hooks into Core. |
| Tooling and Pedagogy can change without a Core release. | Slight duplication occurs when several tools target the same concept. Shared Core definitions mitigate it. |

### E.5.3:8 - Rationale
One-way dependencies keep changes in Tooling or Pedagogy from becoming prerequisites for interpreting Core claims. The rule implements **P-4 Open-Ended Kernel** and **P-5 FPF Layering** while allowing those families to evolve under the Core semantics they use.


### E.5.3:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)
* **References family definition:** `pat:constitution/fpf-ecosystem-family-architecture` (E.4)
* **Instantiates pillars:** P‑4, P‑5
* **Constrains:** All artefact imports recorded in DRRs or SCRs

### E.5.3:End
