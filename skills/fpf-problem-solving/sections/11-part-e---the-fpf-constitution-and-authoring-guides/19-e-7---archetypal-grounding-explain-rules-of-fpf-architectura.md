## E.7 - Archetypal Grounding: Explain Rules of FPF Architectural Patterns through Cases

### E.7:1 - Problem frame
Universal rules are powerful only when readers can grasp them. In FPF the
Conceptual Core speaks in substrate‑agnostic language: `U.Holon`,
Γ‑aggregation, MHT emergence. Practitioners need to “see” those rules in
familiar matter—physical hardware or bodies of knowledge—before they can
reuse them.

### E.7:2 - Problem
A purely abstract statement risks two failures:

1. **Didactic failure** – readers dismiss the pattern as “too meta,”
   violating Pillar **P‑2 Didactic Primacy**.
2. **Hidden scope** – without unlike cases, a purportedly general rule
   can conceal the conditions needed in another use.

### E.7:3 - Forces

| Force | Tension |
|-------|---------|
| **Universality vs Concreteness** | Abstract law ↔ concrete example. |
| **Brevity vs Clarity** | Spec should stay concise ↔ dual examples add length. |
| **Rigour vs Accessibility** | Formal semantics ↔ intuitive narrative. |

### E.7:4 - Solution — mandatory *Archetypal Grounding* subsection

Every architectural pattern **SHALL** include a dedicated section titled **“Archetypal Grounding”** that shows the rule and its applicability through concrete cases. Use FPF's two canonical archetypes where the rule applies:

1. **`U.System`** — an acting physical or operational holon.
2. **`U.Episteme`** — a non-agentive claim-bearing holon.

When the rule applies across both, use the **Tell-Show-Show** sequence below. When it intentionally applies to only one substrate, supply that case and the scope justification required by CC-AG.3. The cases make application and limits inspectable; a wider universality claim needs its own proof or evidence.

| Stage | Content |
|-------|---------|
| **Tell** | `Solution` states the rule and its applicability conditions. |
| **Show #1** | `Archetypal Grounding` gives a concrete `U.System` case when applicable. |
| **Show #2** | The same section gives a parallel `U.Episteme` case when applicable. |

### E.7:5 - Archetypal Grounding (of this pattern itself)

| Universal rule | `U.System` instantiation | `U.Episteme` instantiation |
|----------------|--------------------------|----------------------------|
| “State what makes a claimed whole and its parts obtain.” | `B.1:5.1` recovers the pump-skid part–whole claim and returns to A.14 and C.13 for the actual part relations and construction. | `B.1:5.2` distinguishes an evidence collection from an integrated claim-bearing whole and requires the A.1 criterion before asserting the latter. |

### E.7:6 - Conformance Checklist

| ID | Requirement | Purpose |
|----|-------------|---------|
| **CC‑AG.1** | Every architectural pattern **SHALL** contain a section headed *“Archetypal Grounding”* under E.8's heading rules. | Keeps grounding findable across all Parts. |
| **CC‑AG.2** | The Archetypal Grounding section **MUST** illustrate the rule with both `U.System` and `U.Episteme` when it applies to both. A single-substrate rule follows CC‑AG.3. | Makes the claimed application and scope inspectable. |
| **CC‑AG.3** | If a rule intentionally applies to only one substrate, the subsection **SHALL** state the scope limitation and justify it against the five Principle‑Taxonomy lenses (`Gov`, `Arch`, `Epist` (epistemological and ontological), `Prag`, `Did`). | Prevents silent bias; links to Bias‑Audit guard‑rail. |
| **CC‑AG.4** | Patterns lacking a compliant Archetypal Grounding subsection **MAY NOT** progress to “Accepted” status. | Enforces discipline without referring to workflow mechanics. |

### E.7:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| **Immediate clarity** – readers see abstract laws in action. | Patterns grow by one short table; mitigated by consistent template snippet. |
| **Visible application and scope** – unlike cases expose how the rule applies and where another basis is needed. | Authors must construct cases that preserve the rule's actual conditions. |
| **Narrative cohesion** – recurring System/Episteme protagonists create a memorable storyline. | — |

### E.7:8 - Rationale
Tell-Show-Show places the rule next to applicable cases and makes their shared conditions and differences inspectable. Making that connection explicit implements **P‑2 Didactic Primacy** while **P‑1 Cognitive Elegance** keeps the grounding proportionate to the rule's actual scope. Linking scope‑justification to the five Principle lenses ties the
pattern to the **Taxonomy‑Guided Bias Audit** and keeps governance
language out of the Core.

### E.7:9 - Relations

* **Implements macro flow:** `pat:authoring/didactic‑architecture` (E.6)
* **References base types:** `pat:kernel/holon` (A.1) (`U.System`, `U.Episteme`)
* **Interacts with bias guard‑rail:** `pat:guard/bias‑audit` (E.5.4) via CC‑AG.3
* **Constrains:** Authoring template in `pat:authoring/pattern‑template` (E.8)

### E.7:End
