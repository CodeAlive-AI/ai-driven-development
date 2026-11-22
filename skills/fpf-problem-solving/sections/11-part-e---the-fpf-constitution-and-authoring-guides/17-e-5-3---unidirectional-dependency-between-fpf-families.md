## E.5.3 - Unidirectional Dependency between FPF Families

> **Status:** Stable

### E.5.3:1 - Problem frame
Use this pattern to decide whether one FPF member may rely on another member, in the same family or a different one, for a definition, rule or procedure. Name the work that needs the supplier and what that work takes from it. A reader who follows a link for an optional illustration can use the original rule independently. For an assertion about two framework editions, establish the dependency under E.4.PFR:3.4.

### E.5.3:2 - Problem
A tutorial may teach a Core term using a helper. If the helper's output becomes the only way to tell what the Core term means, changing the helper can change the term for every Core reader. A cycle of imports also prevents an author from supplying one member on the declared basis independently of the others in the cycle. Pillar P-5 governs this separation.


### E.5.3:3 - Forces

| Force | Tension |
|-------|---------|
| **Independent revision** | Tool authors need room to change an implementation while Core readers can still interpret the rule it checks. Either publication may be revised frequently. |
| **Reuse** | A guide can teach a Core rule directly or teach a procedure that also uses a tool. The two uses rely on different suppliers. |
| **Assurance** | An import list makes cycles visible. Establishing which claims a user needs takes a reading of the content. |

### E.5.3:4 - Solution — One‑Way, Acyclic Imports
Read a dependency arrow from the member that needs content for a stated use to the member that supplies it. The **strict partial order** on distinct families constrains the permitted direction of cross-family imports. The actual imports connect particular members. A family may have several permitted suppliers and need only one for the work at hand.

**`imports` expresses dependency. Specialisation is a separate relation (normative).** When an artefact exposes an `imports : [...]` list (e.g., `SignatureManifest.imports` in A.6.0), treat each dependency claim in the list as an edge of its `imports` graph. The graph MUST be **acyclic** (a DAG) and MUST respect the declared direction.

`imports` MUST NOT be used to encode *specialisation* (e.g., `⊑` / `⊑⁺` between mechanisms). Specialisation relations and any specialisation-chain claims are declared separately under their defining rules. For mechanism declarations, apply A.6.1:4.8 to the comparison claim. Use C.29 when a separate mathematical-representation choice, transfer or reliance question remains.

**Permitted suppliers for Core, Tooling and Pedagogy**

| Family of the receiving member | That member may import directly from members of these families |
| --- | --- |
| Conceptual Core | Conceptual Core |
| Tooling Reference | Tooling Reference, Conceptual Core |
| Pedagogical Companion | Pedagogical Companion, Tooling Reference, Conceptual Core |

Each row lists permitted suppliers. Use the ones needed for the member’s stated work. A guide can take a definition directly from Core. An intermediary is needed when its contribution is required for that use.

The acyclicity rule applies within each family as well as across families. Before adding an import, follow the existing imports from the proposed supplier. If a path reaches the receiving member, the new import would close a cycle. Keep Core meanings independent of Tooling, Pedagogy and domain or local frameworks (E.10 V-1, E.4). Linters and other executable checks of Core conformance belong in Tooling. Core states the conditions they check. For Core, DPF and LPF editions, apply the edition rules in E.4.PFR:3.4. An LPF may depend directly on a DPF, and either may depend directly on Core. E.4.DPF also permits a DPF to rely on a contribution from another DPF when it fits the receiving use. The discipline to which a Method belongs, the order of chapters and the level of abstraction of a model each need their own grounds (E.4:4.2.2, B.5.MR).

**Extending the order.** Classify a proposed tool or teaching publication by the use it supplies. It can join an existing family under that family's rules. For a genuinely new family, use E.4.PFAD and E.9 to decide both who may supply it and who may import from it. Under the current extension rule, place it on the receiving side of at least one existing family. Follow the proposed directions through the existing order. Reject a loop even if nobody has yet exercised any of the permissions. Specify any change in what existing families may obtain from one another and seek the amendment needed before an existing prohibition can change. Families without a direct or transitive ordering relation can remain incomparable. A permitted direction need not yet have an actual import. A proposal outside the extension rule requires a change to that rule before admission.

**When a needed import would be forbidden**, keep the contingent claim with the family that can warrant it. If Core readers need a transdisciplinary rule, supply the rule and grounds they can use independently. A guide can receive credit for the discovery. Copying a guide's convention leaves Core dependent on that convention whenever the argument still requires it. If two members would have to import one another, look for a common definition they can both use from a permitted supplier. Where two definitions must be given together, consider one defining account and check its imports. Printing two mutually dependent members in one file leaves their cycle intact.

### E.5.3:5 - Archetypal Grounding (System / Episteme)

| Family | `U.System` illustration | `U.Episteme` illustration |
|-------|------------------------|---------------------------|
| Core | Definition of `U.System` and boundary invariant. | Definition of F‑G‑R assurance components. |
| Tooling | The “Reference system‑profile” checks boundary flow and *imports* Core invariants. | The “Episteme‑scoring routine” calculates R‑score and *imports* Core characteristics. |
| Pedagogy | A tutorial uses the system‑profile to model a pump and *imports* the profile and Core term. | A case study explains R‑score evolution and *imports* the scoring routine and Core term. |
| **Forbidden** | Core pattern importing measurement script. | Core pattern importing R‑score web dashboard. |

A guide teaches the boundary invariant from Core and links to a profile checker for practice. Readers can establish a boundary from the published rule with the checker unavailable. One exercise accepts any report satisfying a separately published format. Another generator can supply it if its report meets the acceptance conditions. A separate exercise requires a report signed by the named checker in the agreed format. This exercise relies on the checker as well as the Core rule. If the available checker can no longer produce an acceptable signed report, use a compatible edition whose signature the recipient accepts for the named checker. If none can supply an acceptable report, revise that exercise. Readers can continue to work from the Core definition. Recheck their explanation if its definition or the argument used to teach it changes.

### E.5.3:6 - Conformance Checklist

| ID | Requirement |
|----|-------------|
| **CC-UD.1** | The graph of actual imports among FPF ecosystem family members **MUST** be acyclic, including imports within a family. |
| **CC-UD.2** | The permitted directions for distinct families **SHALL** form a strict partial order, including after an extension. Each cross-family import must follow that order. A same-family import must satisfy CC-UD.1. |
| **CC‑UD.3** | Reject an import forbidden by the governing order. A DRR can resolve the design without that import or propose an amendment under E.3 and E.9. The amendment must take effect before the import can be admitted. |

### E.5.3:7 - Consequences

| Benefits | Trade‑offs / Mitigations |
|----------|-------------------------|
| Core can supply meanings independently as tools change. | A tool-specific convention may still be useful in the tooling or teaching material that relies on it. |
| Different families can revise their contributions independently where the uses allow it. | A change to a shared claim may reach several readers. Follow that claim to each affected use under E.4.PFR:3.4. |

### E.5.3:8 - Rationale
Under P‑5 FPF Layering, an author can replace a tool or a teaching example while readers continue to use the Core claim on its own grounds. P‑4 Open‑Ended Kernel keeps a convention that depends on a particular practice with its proper supplier. P‑10 Open‑Ended Evolution allows a warranted proposal to change the family order. Until the competent authority enacts such a change, the current order governs every import.


### E.5.3:9 - Relations
* **Parent umbrella:** `pat:constitution/guard‑rails` (E.5)
* **References family definition:** `pat:constitution/fpf-ecosystem-family-architecture` (E.4)
* **Instantiates pillars:** P‑4, P‑5 and P‑10
* **Constrains:** Actual imports between FPF ecosystem members. A manifest, DRR or SCR may record an import. A required claim can still create a dependency when its source is unacknowledged.

### E.5.3:End
