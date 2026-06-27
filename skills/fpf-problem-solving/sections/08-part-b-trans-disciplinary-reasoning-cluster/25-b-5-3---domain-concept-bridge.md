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
| **Same word vs. different claim** | One word such as "sensor", "state", "process", or "role" can point to different FPF values in different bounded contexts. |
| **Bridge use vs. role overuse** | Some domain words really name role values or role assignments; many others name entities, characteristics, methods, descriptions, or evidence relations. |
| **Bridge record vs. hidden ontology** | A bridge must carry scope, loss, and return conditions rather than hiding them behind a synonym. |

### B.5.3:4 - **Solution**

Use a **Domain-Concept Bridge**. Start with the local word in its `U.BoundedContext`, then recover the FPF value that the project is actually using.

1. Establish the bounded context and local sense: use `F.1` to identify the domain family and authoritative sources, `F.2` to harvest terms with provenance, and `F.3` to cluster the local sense or SenseCell with counter-examples.
2. Ask what the local word is doing in the current claim: naming an entity, admitted U-kind, ontic slot filler, relation, characteristic coordinate, method, mechanism, work plan, performed work, role assignment, episteme, publication-use relation, evidence-use relation, or other governed value.
3. If the claim needs durable kindhood, use admission under `E.24.UK` and `C.3` and supply the ontic and slot relation that make the kind reviewable.
4. If the claim is only local vocabulary, keep it as a LocalSense or SenseCell and bridge it with scope and loss notes.
5. Use role vocabulary for system or holon role assignments in bounded work-facing contexts. Express meaning, status, evidence use, publication use, and domain interpretation through their own FPF values and relations.

The bridge record is therefore not an alias. It is a small typed settlement saying which FPF value the claim uses, what local wording points to it, where the bridge is admissible, and when the stronger source or direct governing pattern must be reopened.

Practical difference from an alias:

* An alias says "`L` is another name for `V`."
* A Domain-Concept Bridge says: in bounded context `K`, local wording `L` is being used for FPF value or relation `V` in the current claim; the bridge carries the constraints, units, role assignments, loss notes, and return conditions that make that use reviewable.
* If a component is called "sensor", the bridge can point to a system, a functional element, a measurement capability, a signal publication, or a role assignment. The claim decides which value is being used; the word "sensor" alone does not.

### B.5.3:5 - **Archetypal Grounding**

A thermodynamics team models a heat engine.

* "Thermodynamic system" names the engine as the entity under thermodynamic concern in the current bounded context. The bridge points to the same system or holon already used elsewhere, plus the thermodynamic boundary and state variables that matter here. It is not automatically a role.
* "Macrostate" names a state description or characteristic bundle over pressure, volume, temperature, and particle amount. The bridge records the reference scheme and units.
* "Control volume" may name a boundary or region relation. The bridge must say which entity is bounded and which exchanges cross the boundary.
* "Free-energy objective" may name an objective claim, characteristic, or selection criterion. The bridge must say which FPF value the decision uses.
* If the engine control system is assigned the role of heat-source controller in a work context, that is a separate `U.RoleAssignment(holderRef, roleRef, boundedContextRef)` claim.

What this achieves:

* Domain constraints become reviewable without turning every domain word into a root kind.
* Verification can use the governing pattern for the recovered value: boundary discipline for a control volume, characteristic-space discipline for state variables, role-assignment discipline for controller work, and publication-use or evidence-use discipline for reports and dashboards.
* The heat engine remains the same system or holon when a power-plant architecture, finance model, safety case, and thermodynamics model all discuss it. Bridges record which local meanings travel across those contexts and which losses block substitution.

The same local word can be reused in an architecture view, a requirements document, and a simulation model only after the bridge states whether those uses point to the same entity, the same characteristic, the same role assignment, or merely related descriptions.

**Conformance Checklist**

* **CC-B5.3.1 (Recover the FPF value used by the claim):** A bridge row names the current FPF value or slot relation before naming the preferred wording.
* **CC-B5.3.2 (No kindhood by spelling):** A local term, dotted name, table row, or diagram label does not become a U-kind unless admission under `E.24.UK` and `C.3` supplies the ontic and the needed slot relation.
* **CC-B5.3.3 (Role boundary):** Role language is used for system or holon role assignments in bounded work and method contexts; other uses are expressed through their own FPF values or relations.
* **CC-B5.3.4 (Scope and loss):** A bridge records context, scope, loss, and return conditions; it does not claim lossless sameness by name alone.
* **CC-B5.3.5 (Description boundary):** If the local word appears in a requirement, diagram, dashboard, report, or publication, the bridge keeps the described entity distinct from the description and publication form.

**Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | What it looks like | Better FPF move |
| :--- | :--- | :--- |
| **Subtype explosion** | Every domain term becomes a new root kind. | Keep the local term in its context unless admission under `E.24.UK` and `C.3` proves durable kindhood. |
| **Magic synonym** | A table says "sensor = component" with no scope or loss. | Write a bridge row naming the FPF value used by the claim, context, admissible use, and return trigger. |
| **Role-for-everything** | Evidence, status, domain interpretation, and document use are all called roles. | Use role assignment only for systems or holons in work-facing contexts; use episteme, publication, evidence-use, status-use, characteristic, method, or work vocabulary for the value being claimed. |
| **Description collapse** | A diagram label is treated as the entity, interface, or method itself. | Keep entity, description episteme, representation scheme, and publication form distinct. |

### B.5.3:6 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Domain language stays usable:** Experts keep familiar words without forcing every word into the kernel. | **Bridge overhead:** Load-bearing local terms need a small bridge record. Keep it short and reopen stronger patterns only when a claim becomes load-bearing. |
| **Kernel stays lean:** New kinds require explicit admission and ontic support. | **More precise modeling choices:** The bridge may reveal that one local word hides several FPF values. That is the point: split them before they drive work. |
| **Cross-document clarity:** Requirements, diagrams, dashboards, simulations, and reports can be compared without pretending they are the same artifact. | **Need for current context:** Bridges are context-scoped; do not move them across projects without checking scope and loss. |

### B.5.3:7 - **Rationale**

The bridge implements open-ended parsimony: FPF can talk with many domains without turning every useful domain word into a kernel kind. It keeps role vocabulary inside role-assignment ontology; domain vocabulary is mediated through local senses, bridge rows, admitted U-kinds, ontics, slot relations, and the FPF values governed by direct patterns.

### B.5.3:8 - **Relations**

* **Builds on:** `A.2`, `A.2.1`, `A.6.5`, `C.3`, `E.24.UK`, `F.1`, `F.2`, `F.3`, `F.5`, `F.8`, `F.18`.
* **Coordinates with:** `A.7`, `C.2.1`, `E.17`, `A.13`, `A.15`, `B.3.3`, `F.7`, `F.9`, and domain-specific CHR, LOG, and CAL patterns.
* **Used when:** a project term must be carried across bounded contexts, documents, diagrams, models, evidence records, or pattern applications without losing its governed FPF value.

### B.5.3:End

