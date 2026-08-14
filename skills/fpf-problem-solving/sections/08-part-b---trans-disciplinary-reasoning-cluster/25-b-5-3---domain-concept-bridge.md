## B.5.3 - Domain-Concept Bridge

### B.5.3:1 - **Problem Frame**

FPF keeps a small set of admitted U-kinds, ontics, slot relations, mechanisms, characteristics, methods, work values, epistemes, and publication-use relations. Working domains use their own words. A thermodynamicist says "system", "macrostate", "control volume", and "free energy"; a safety engineer says "hazard", "mitigation", and "assurance case"; a software team says "service", "endpoint", and "release".

Those words are useful. The problem starts when one local word is silently treated as a new root kind, a role assignment, a characteristic, a method, a work occurrence, an evidence relation, or a publication claim without saying which FPF value the claim uses.

### B.5.3:2 - **Problem**

How can FPF let project teams keep domain vocabulary while preserving the current FPF ontology? A dictionary-style alias is too weak because it only says that two labels are being associated. It does not say whether the claim concerns an entity, a kind, a slot filler, a characteristic coordinate, a role assignment, a method, a mechanism, a work plan, a performed work occurrence, an episteme, a publication-use relation, or an evidence-use relation.

### B.5.3:3 - **Forces**

| Force | Tension |
| :--- | :--- |
| **Domain fluency vs. ontological parsimony** | Teams need familiar words, but FPF must not grow a new root kind whenever a local term appears. |
| **Same word vs. different claim** | The same expression can make different local claims in different sources or schemes and can point to different FPF values. Spelling alone decides none of them. |
| **Meaning recovery vs. role overuse** | Some domain uses concern a system-role kind or assignment; many concern another value or relation. Recover the claim before choosing the terminology. |
| **Small result vs. hidden ontology** | The result should be as small as the use permits, yet still expose any real kind, relation, loss, and return condition instead of hiding them behind a synonym. |

### B.5.3:4 - **Solution**

Use the **Domain-Concept Bridge** as a bounded reasoning move, not as a new domain container or mandatory record.

1. Start from the exact expression, source, edition, and relevant passage. Use F.0.1 to recover the source-local claim. Create an F.17 cell and basis relation only when later durable reuse needs that address.
2. Ask which exact FPF value or relation the current claim needs, then use the pattern that defines or constrains it. For example, the answer may concern a System, characteristic, Method, Work occurrence, episteme, system-role assignment, or evidence-use relation; the list is illustrative, not a set of new bridge kinds.
3. If the use really needs a new kind, apply E.24.UK and C.3. A familiar expression, table row, or diagram label supplies no kindhood.
4. If the recovered source-local claim already answers the question, return it and stop. If a receiving use must relate two distinct local-sense claims, use F.9 to test whether an exact Bridge between their F.17 cells actually obtains. Shared spelling, a mapping table, or a completed card proves no such relation.
5. State the receiving use separately. Name the direction, scope or applicability boundary, tolerated loss, evidence or reliance basis, and reopen condition only when each changes that use. The semantic relation alone neither authorizes nor performs the use.
6. When *role* wording is material, use E.10.ROLE and A.2 to distinguish a local system-role kind, classification, assignment, participation, responsibility, or ordinary language before making the direct claim.

The practical result can be one readable sentence. Use a note, row, or card only when a later reader or tool needs durable packaging. The package describes the result; it does not create the FPF value, local meaning, relation, or permitted use.

An alias says only that `L` is another name for `V`. A completed B.5.3 move instead says what the exact source means here, which FPF value the current claim uses, whether any direct relation actually obtains, and what the named receiving use may rely on. Thus a component called "sensor" may lead to a System claim, measurement-capability claim, publication claim, or system-role-assignment claim; the expression alone chooses none of them.

### B.5.3:5 - **Archetypal Grounding**

A thermodynamics team models a heat engine.

* In the cited thermodynamics source, "thermodynamic system" names the engine under concern together with the boundary and state variables relevant to that local claim. Recover the same System already used elsewhere; the expression does not automatically name a kind or assignment.
* "Macrostate" makes a source-local claim about a state description or characteristic bundle over, for example, pressure, volume, temperature, and particle amount. State the effective scheme and units directly; create an F.17 cell only if durable reuse needs one.
* "Control volume" may name a boundary or region relation. The claim must say which entity is bounded and which exchanges cross the boundary.
* "Free-energy objective" may name an objective claim, characteristic, or selection criterion. The claim must say which FPF value the decision uses.
* If the engine control System is assigned a locally defined heat-source-controller system-role kind, establish a separate obtaining occurrence of the declared `U.SystemRoleAssignment` species. The source-local meaning, classification, assignment, Work, claim scope, and time window remain separate.

Current physical-system claims in this example use `A.1` for system identity, `A.14` and `A.22` for composition and boundary relations, `A.3.4` for state and dynamics, `B.1.6` for work-resource aggregation, and `C.16` for measured characteristics. Planned `C.1` (Sys-CAL) may later consolidate that guidance; it is not a current governor.


What this achieves:

* Domain constraints become reviewable without turning every domain word into a root kind.
* Verification can use the direct pattern for the recovered value: boundary discipline for a control volume, characteristic-space discipline for state variables, system-role-assignment discipline when an assignment is claimed, and publication-use or evidence-use discipline for reports and dashboards.
* The heat engine remains the same System when a power-plant architecture, finance model, safety case, and thermodynamics model all discuss it. Any actual F.9 relation states how two distinct local meanings correspond; the named receiving-use claim states which losses block that use.

The same expression can be reused in an architecture view, a requirements document, and a simulation model only after each local claim identifies its actual value. If the claims use distinct local meanings, test any required F.9 relation and its receiving use separately.

**Conformance Checklist**

* **CC-B5.3.1 (Recover the FPF value used by the claim):** The result names the exact FPF value or relation used by the current claim before treating a preferred expression as reusable.
* **CC-B5.3.2 (No kindhood by spelling):** A local expression, dotted name, table row, or diagram label does not become a U-kind. A needed durable kind requires its own E.24/E.24.UK and C.3 settlement from independent ontic and membership evidence.
* **CC-B5.3.3 (Role boundary):** When *role* wording changes the claim, E.10.ROLE first recovers whether it means a local system-role kind, classification, assignment, participation, responsibility, or ordinary language. Each resulting claim then uses its own FPF pattern.
* **CC-B5.3.4 (Relation and use boundary):** Claim an F.9 Bridge only when its exact endpoint cells and predicate make it obtain. State the receiving use, direction, applicable scope, tolerated loss, evidence or reliance basis, and return condition separately; shared spelling proves none of them.
* **CC-B5.3.5 (Description boundary):** If the local expression appears in a requirement, diagram, dashboard, report, or publication, use the direct description and publication patterns to keep the described entity, description episteme, publication form, and carrier distinct.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | What it looks like | Better FPF move |
| :--- | :--- | :--- |
| **Subtype explosion** | Every domain expression becomes a new root kind. | Keep the source-local claim as wording unless E.24.UK and C.3 establish a needed kind from independent ontic evidence. |
| **Magic synonym** | A table says "sensor = component" and is treated as identity or permission. | Recover each exact local claim and the FPF value used. If two distinct cells must be related, test the actual F.9 relation and judge the named use separately. |
| **Role-for-everything** | Evidence, status, local meaning, responsibility, and document use are all called roles. | Apply E.10.ROLE, then name the actual value or relation and use its direct pattern. A local system-role kind or assignment is only one possible result. |
| **Description collapse** | A diagram label is treated as the entity, interface, or method itself. | Keep entity, description episteme, representation scheme, and publication form distinct. |

### B.5.3:6 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Domain language stays usable:** Experts keep familiar words without forcing every word into the kernel. | **Recovery overhead:** A load-bearing expression needs its exact source-local claim and governed value. Keep the returned explanation short; open F.17 or F.9 only when durable or cross-local use actually needs it. |
| **Kernel stays lean:** New kinds require explicit admission and ontic support. | **More precise modeling choices:** The bridge may reveal that one local word hides several FPF values. That is the point: split them before they drive work. |
| **Cross-document clarity:** Requirements, diagrams, dashboards, simulations, and reports can be compared without pretending they are the same artifact. | **Need for an exact use boundary:** Do not reuse a source-local claim or semantic relation in another project, scheme, scope, or action without checking the actual changed values, tolerated loss, and reliance basis. |

### B.5.3:7 - **Rationale**

This pattern implements open-ended parsimony: FPF can use many domain vocabularies without turning every useful expression into a kernel kind. It recovers the source-local claim first, routes the needed FPF value to its direct pattern, and introduces an F.9 Bridge only for an actual relation between distinct local senses.

### B.5.3:8 - **Relations**

* **Builds on:** `A.2`, `A.6.5`, `C.3`, `E.24.UK`, `F.0.1`, `F.1`, `F.2`, `F.3`, `F.5`, `F.8`, and `F.17`.
* **Coordinates with:** `A.7`, `C.2.1`, `E.10.ROLE`, `E.17`, `A.13`, `A.15`, `B.3.3`, `F.7`, `F.9`, and the direct domain-specific CHR, LOG, and CAL patterns.
* **Used when:** a project must recover what an exact source expression means for one FPF claim, or must relate two distinct local meanings for a named receiving use without confusing the wording, governed value, semantic relation, and use.

### B.5.3:End

