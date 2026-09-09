## C.13 — Constructional Mereology (Compose‑CAL)
> **Status:** Stable
> **Type:** Pattern

**At a glance.** Use C.13 when a practitioner must show how identified entities and relations that obtain form one whole, collection, or aspect. The account explains how those facts support the whole, collection, or aspect; writing a `sum`, `set`, or `slice` expression does not create the entities or relations.

**Use this when.** Use this pattern after the direct relation patterns have identified the participants and relations that obtain, when you need a compact, inspectable account of how they assemble a whole, form a collection, or distinguish an aspect.

**First useful move.** Name the whole, collection, or aspect whose construction you must explain; then name its inputs, the constructive part relations or the collection's own belongs-to relations, and the rule by which those facts form it. Choose `sum`, `set`, or `slice` as the shortest truthful construction narrative.

**What goes wrong if missed.** A readable component, belongs-to, or aspect statement may lack its construction account; or the opposite mistake occurs and a diagram, list, or `Γ_m` expression is treated as if it created a whole, a relation, or a holon.

**What this buys.** A compact three-form construction discipline that keeps integrated assembly, collection, and aspect distinct while leaving relation conditions, whole identity, evidence, and public relation names with the patterns that define them.

**Not this pattern when.** Not this pattern when the current question is only relation vocabulary, evidence or assurance without a structural claim, epistemic representation, a selected dependent `U.Structure`, temporal phase without an aspect claim, public-kind admission, or transformation composition without a direct transformation-composition governor.

### C.13:1 - Intent

Provide one minimal calculus for narrating three kinds of construction: how constituents assemble an integrated whole, how entities form a collection under that collection's own belongs-to rule, and how an aspect is distinguished from one bearer under one facet. The calculus records how already identified entities and obtaining relations support that named whole, collection, or aspect. It is not a second source of relation obtaining and does not make any of them exist by notation.

Also known as *“Γₘ mereology”* and *“constructor-based composition”*.

**Layer.** *calculus.*
**Depends on.** A.14 and the direct relation patterns for participants, obtaining conditions, and occurrence identity; the direct kind pattern for the candidate whole and its identity or reidentification rule.
**Consumed by.** A.1 when candidate holon recognition needs constructive assembly, B.3.5 when a named assurance use needs a structural grounding account, and subject patterns that need a compact construction narrative.

Compose-CAL keeps exactly three narrative forms—`sum`, `set`, and `slice`. A materialized construction trace is a C.2.1 episteme about the construction facts. Its claims can designate entities, relation occurrences, rules, and identity conditions; the trace is neither the whole, collection, or aspect it describes nor a participant in the world-side relations.

### C.13:2 - Problem Frame

FPF needs both readable structural relations and a recoverable account of how constituents assemble a whole, entities form a collection under its belongs-to rule, or a facet distinguishes an aspect. A relation name alone may leave the construction opaque. A constructor expression alone can commit the opposite error by treating syntax as the source of entities, relation obtaining, or whole identity.

### C.13:2.1 - Problem

A bare list of `ComponentOf`, collection-specific belongs-to, or `AspectOf` claims does not say which assembly, collection rule, or facet makes them one construction. But a bare `sum`, `set`, or `slice` expression is no better: the same constituents can participate in different assemblies, a collection need not be an integrated holon, and an arbitrary facet label does not establish an aspect. The construction account must therefore name world-side facts and preserve the candidate's direct identity or reidentification rule.

### C.13:3 - Forces

* **Parsimony vs truth.** Three construction forms are easier to reuse than an open constructor catalogue, but no form may replace a missing direct relation or assembly rule.
* **Readable statement vs constructive account.** Practitioners need ordinary component, belongs-to, and aspect statements; reviewers may also need to inspect how those relations support the named whole, collection, or aspect.
* **Input set vs assembly.** The same entities can be assembled through different obtaining relations and can therefore yield different wholes.
* **Continuity vs extensional snapshots.** Constituents and part-relation occurrences can change while the same whole continues when its direct reidentification rule permits the phase change.
* **Construction vs evidence.** A trace states the construction account; evidence and assurance separately support or warrant the claim content.
* **Cross-domain reuse vs owner bypass.** Systems, epistemes, methods, and work occurrences can all need constructive grounding, but their direct patterns retain kind, part, and identity authority.

### C.13:4 - Solution

#### C.13:4.1 - Solution sketch

Use the coarsest of three construction narratives that fits the named whole, collection, or aspect. In each case, write the shorthand only after the required facts are recoverable.

| Form | Practical reading | Facts required before the trace is truthful | What the form does not establish |
| --- | --- | --- | --- |
| `Γ_m.sum(parts)` | These exact constituents are assembled as this integrated whole. | one exact candidate whole; exact constituent entities; exact obtaining constructive part-relation occurrences; the assembly rule or method and its applicability; the candidate's identity or reidentification rule | that proximity, one drawing, a parts list, or the constituent set alone makes the whole; that every constituent change ends the whole |
| `Γ_m.set(elems)` | These entities belong to this collection under the collection's own rule. | one identified collection; identified entities; the belongs-to occurrences that obtain; the collection's belongs-to and identity rules | that the notation creates the collection or relation; component integration, acting-system organization, agency, A.1 holonhood, constructive parthood, or transitive belonging |
| `Γ_m.slice(entity, facet)` | This exact aspect is distinguished from this bearer under this facet. | one exact bearer; one exact aspect; the governed facet; an exact obtaining aspect or portion relation and its identity rule | an arbitrary view, time window, selected concern, or label becoming a world-side part |

The familiar argument lists are readable shorthand, not complete ontological signatures. A complete use names the whole, collection, or aspect and states the direct facts beside the shorthand. Input order does not matter to the list of designated inputs, but assembly relations, rules, facets, and identity conditions do matter. The same input set under a different assembly can yield another whole.

A construction may obtain in the world even when no trace episteme has been written. When another piece of work needs an inspectable trace, materialize a C.2.1 episteme whose claim content names the whole, collection, or aspect; its constituents, entities that belong, or bearer; the relation occurrences that obtain; the construction rule; and the identity conditions. Creating, editing, publishing, or losing that episteme changes the account or its availability, not the past or present construction facts.

Do not add a fourth constructor merely to carry time, execution order, parallelism, representation, evidence, or a domain label. Keep those claims with their direct patterns beside the construction account.

#### C.13:4.2 - Normative Standard (high‑level)

* **C13-N1 — Direct facts first.** A C.13 trace is conformant only when every named constituent or collection entity and every named part, collection-belonging, or aspect occurrence is independently identified under its direct pattern.
* **C13-N2 — Whole identity stays direct.** The candidate whole follows its direct identity and reidentification rule. Equality of an input list or trace does not decide whether the existing whole continues or a new whole must be identified; a permitted constituent replacement can preserve one whole, while the same constituents under another assembly can form another whole.
* **C13-N3 — Construction form.** `sum`, `set`, and `slice` are the only C.13 forms. Reordering or duplicate designation does not change the listed inputs; it does not merge distinct entities or relation occurrences and does not erase assembly or facet differences.
* **C13-N4 — Mereological discipline.** Direct part patterns and A.14 govern acyclicity, antisymmetry, transitivity where applicable, recurrence, and occurrence identity. C.13 does not strengthen a direct relation by calculus convention.
* **C13-N5 — Trace separation.** A materialized trace is a C.2.1 episteme. It creates none of the following: the whole, collection, or aspect it describes; the inputs; the relation occurrences; the construction rule; the identity conditions; or holonhood.
* **C13-N6 — A collection account is not component assembly.** `set` supports a collection account; it does not imply integrated assembly, `ComponentOf`, system agency, or A.1 recognition. Use `sum` only when constructive part relations and assembly are independently grounded.
* **C13-N7 — Elected assurance grounding stays with B.3.5.** A direct structural Working-Model edge may be published without a C.13 trace. When that publication elects B.3.5 or a named current requirement demands the profile, follow B.3.5 for the required `tv:groundedBy` link and declared `validationMode`; C.13 supplies the reconstructible trace content. Evidence, warrant, currentness, and reliance remain separate, and neither the link nor the mode replaces the direct construction or identity facts.
* **C13-N8 — Subject owners remain authoritative.** Method, work, and discipline construction may use C.13 only after their direct patterns identify actual parts and whole-forming relations. A selected dependent `U.Structure` does not become a whole, collection, aspect, or holon by selection or name.
* **C13-N9 — Transformation composition stays fail-closed.** A C.13 entity-construction trace, method decomposition, work decomposition, common changed referent, or temporal subdivision establishes neither transformation parthood nor a composite transformation. Without a direct transformation-composition governor, retain the independently identified changes and the exact blocker; infer neither composition nor atomism.

#### C.13:4.3 - Scope, applicability, terms & notation

Use Compose-CAL when the current claim concerns the construction of one exact system, episteme, method, work occurrence, discipline, collection, or aspect and its direct part patterns already supply the required participants and obtaining relations. Do not apply it merely because a sentence contains `part`, a diagram groups nodes, or a selected structure organizes relations.

- **`Γ_m`** — the three-form notation for a C.13 construction narrative.
- **construction trace** — claim content that names the whole, collection, or aspect; its inputs; the direct relations that obtain; its construction rule; and its identity conditions; when materialized, it is a C.2.1 episteme.
- **constructive part relation** — an exact world-side relation occurrence governed by its direct pattern; it is designated by the trace but not created by it.
- **assembly rule or method** — the rule by which the named constituents assemble the whole, the members form the collection, or the bearer and facet distinguish the aspect; a rule-description episteme is not the assembly, collection, or aspect itself.
- **identity or reidentification rule** — the direct rule that identifies the whole, collection, or aspect and says which changes preserve or end it.

**Alias readiness.** These are common readable projections only when their direct relation meanings match the case:

- `ComponentOf` may accompany a `sum` construction;
- an ordinary belongs-to sentence may accompany a `set` construction; the collection's own pattern supplies its meaning, occurrence history, and any recurrence rule;
- `AspectOf` may accompany a `slice` construction;
- `PortionOf` needs the direct portion relation and metrical semantics in A.14, not a facet spelling alone;
- `ConstituentOf` needs the direct logical or content-part relation; material mixtures use their exact portion or component owner.

The readable label and the trace answer different questions. The label states which direct relation obtains; the trace explains how the exact relation set supports this construction. Neither one is evidence merely by being present.

#### C.13:4.4 - Structural CT2R Typing-Grounding Use

When a target kind or logical representation must reuse both a `Γ_m` construction account and an independently grounded Working-Model relation, use `StructuralCT2RTypingGroundingUnfoldingStructureBlock` from `B.3.5`. C.13 contributes the account of the subject-side relations that actually obtain and states which mereological structure the target preserves or loses inside that B.3.5-governed local `A.22.CGUS` structure specialization. C.13 does not create separate unfolding-structure authority and does not by itself supply a bridge, kind intent, proof, empirical evidence, or admissible reuse. Apply `A.7.1`, rather than this structural CT2R block, when an inadequate working account must be diagnosed against the subject construction.

Use this split especially when a readable relation label such as ComponentOf, a collection's belongs-to predicate, AspectOf, ConstituentOf, or RepresentationOf is being reused beyond what its sentence warrants. The label does not by itself prove constructive grounding or a wider structural projection. Name the construction trace and Working-Model relation, the target kind or logical representation, any bridge used, the structure preserved and collapsed, and the proof or evidence relation required by the stronger claim. If the evidence instead diagnoses a mismatch that requires revision of the working ontology, apply `A.7.1`.

### C.13:5 - Archetypal Grounding

#### C.13:5.1 - Pump Skid: Integrated Assembly, Not A Parts List

PumpSkid #7 is assembled from exact Pump, Motor, Baseframe, Manifold, enclosure, pipe, cable, and connector entities. The direct mechanical, electrical, and fluid part-relation patterns identify the exact fastening, coupling, enclosure, terminal, flange, and seal occurrences. The skid assembly method or rule states how those facts form the candidate, and the skid reidentification rule says which replacements preserve PumpSkid #7.

The shorthand `Γ_m.sum{Pump, Motor, Baseframe, Manifold, ...}` is truthful only with those facts beside it. It records an integrated-assembly construction; it does not make the relations obtain. The composition sustains skid-level boundary, interface, load-envelope, and operating characteristics not attributable to one constituent alone.

The same parts unconnected on a pallet do not form the skid. A bill of materials and drawing are epistemes about intended or possible assembly. They do not substitute for actual part relations, assembly, or identity. The same part set connected under a different governed assembly may constitute another whole.

#### C.13:5.2 - Collection And Aspect

A fleet register can identify one collection and the vehicles that belong to it under the registration rule. `Γ_m.set{Vehicle-1, Vehicle-2, ...}` reports that collection only after the fleet identity, registration rule, and each belongs-to fact have been established. It creates neither the fleet nor those facts. It establishes no vehicle integration, constructive parthood, collective agency, acting system, or A.1 holonhood. If the same candidate later passes all six A.1 matters, a separate `sum` account may report its independently grounded constructive parts and assembly.

Reuse the filled Reactor-7 case in `A.14:5.3`: `Γ_m.slice(Reactor-7, thermal-boundary)` reports ThermalEnvelope-7, the insulation panels, seals, and boundary interfaces picked out by the thermal-boundary rule, the obtaining `AspectOf` occurrence, and the enclosure identity and ending conditions. A permitted panel replacement can preserve the aspect while requiring a current trace; dismantling the enclosure, changing the facet rule, or reidentifying Reactor-7 ends the reported occurrence. The slice reports these facts and creates none of them. A dashboard view, selected concern, or time window is not that aspect by display.

#### C.13:5.3 - Episteme, Method, Work, And Discipline Holons

A theory episteme may use C.13 only after C.2.1 identifies the episteme and an exact direct episteme-part or claim-composition pattern identifies the constituent entities, the part relations that obtain, and the assembly and reidentification rule. C.2.1 claim-graph content helps constitute the episteme but does not thereby supply a C.13 part predicate. A definition, derivation, diagram, representation, publication, or evidence relation likewise does not become a part merely because it states, shows, publishes, or supports the theory; include it in a `sum` trace only when an exact direct part predicate independently obtains. The trace then reports the claim-bearing assembly rather than creating it.

A composite method may use C.13 after B.1.5 or another direct method-composition pattern identifies exact submethods, whole-forming relations, constraints, and the whole-method reidentification rule. A dated work occurrence may use C.13 only after the direct work-mereology owner identifies exact work parts and whole-forming relations. Step labels, a recipe, work-plan items, a WBS, co-occurrence, or common performer do not supply those facts.

A discipline may use C.13 only after C.20 and its direct relation owners identify whatever constituent entities the case actually requires, the whole-forming relations that obtain among them, and the discipline identity or reidentification rule. Do not infer parts from C.20 card positions or from objects merely associated with the discipline. A canon item, practice, organization, carrier, bridge, comparison relation, field name, bibliography, curriculum, or publication collection enters a `sum` trace only when an exact direct part predicate independently obtains.

#### C.13:5.4 - Selected Structure And Transformation Stops

A selected `BoundedModelUseStructure` organizes exact model-use relations for a use. Selection does not give the dependent structure constituents, parthood, agency, holonhood, or an MHT. C.13 can discuss construction of an underlying system, episteme, method, or work whole when its direct facts are available; it does not turn the selected relation organization into that whole.

Mounting, wiring, fluid-connection, and configuration changes may each be independently identified `U.Transformation` occurrences. A skid entity-construction trace does not make those changes constituents of one composite transformation. If a use requires transformation contribution, parthood, composite identity, or holonhood and no direct governor supplies the relevant compatibility and reidentification law, retain the separate changes and the exact blocker. Missing composition facts establish neither composition nor indivisibility.

#### C.13:5.5 - Scope Justification

The same three forms work across mechanical, biological, informational, Method, Work, and Discipline cases because they keep three questions apart: integrated assembly, collection belonging, and aspect distinction. Using them does not replace the patterns that define the particular entities and relations. Order and timing remain with Method and temporal patterns; evidence and warrant remain with assurance patterns; public kind admission remains with E.24.UK; the direct identity rule decides whether the existing whole continues or a new whole must be identified, with B.2 used when reidentification is current.

### C.13:6 - Bias-Annotation *(cognitive anti-patterns and counter-moves)*

| Bias | Symptom | Counter-move |
| --- | --- | --- |
| **Constructor-centrism** | The trace is treated as the real structure and the direct relation as decorative. | Recover exact entities and obtaining direct relations first; use the trace only as their construction account. |
| **Declaration-centrism** | A readable part edge is accepted without identifying the assembly, collection rule, facet, or identity conditions. | Name the whole, collection, or aspect and its construction facts, then add the shortest truthful trace. |
| **Collection mistaken for composition** | A belongs-to statement or `set` trace is used to infer an integrated assembly or acting system. | Keep collection identity and belonging separate; use `sum` only with independently obtaining constructive part relations and an assembly. The same candidate may have both accounts when both claims pass. |
| **Snapshot extensionalism** | Any constituent replacement is taken to end the whole, or the same input set is taken to guarantee the same whole. | Apply the candidate's direct identity and reidentification rule; include assembly relations and conditions. |
| **Temporal leakage** | Sequence, phase, or work order is encoded as structural construction. | Keep order and time with their direct method and temporal patterns. |
| **Evidence-created structure** | A current drawing, trace, or evidence record is taken to make the assembly obtain. | Keep construction facts, trace claims, evidence, currentness, and receiving reliance separate. |
| **Subject-owner bypass** | Method steps, work items, a selected structure, or several changes are declared parts by generic C.13 notation. | Require their direct composition owner; stop before structure holonhood or transformation composition when that governor is missing. |

### C.13:7 - Conformance Checklist *(normative, calculus‑level)*

The following regulate a C.13 use.

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-C13-1 — Three forms.** | Use only `sum`, `set`, or `slice` for the C.13 construction narrative. | Preserve a small cross-domain calculus. |
| **CC-C13-2 — Exact direct basis.** | Name the whole, collection, or aspect; its inputs; the direct relation occurrences that obtain; its construction rule; and its identity or reidentification rule. | Prevent notation-created entities and relations. |
| **CC-C13-3 — Assembly-sensitive identity.** | Do not infer the identity of a whole, collection, or aspect from the input list alone; preserve assembly relations, rule conditions, and the direct reidentification law. | Distinguish the same inputs under different assemblies, and one whole surviving a permitted constituent change. |
| **CC-C13-4 — No order or time by constructor.** | Keep execution order, parallelism, temporal coverage, and phase with their direct patterns. | Preserve the boundary among structural construction, temporal extent, and method order. |
| **CC-C13-5 — Narratability.** | State the construction in ordinary language before or beside the shorthand. | Keep the construction usable without notation. |
| **CC-C13-6 — Direct-relation discipline.** | Use ComponentOf, a collection's own belongs-to predicate, AspectOf, PortionOf, or ConstituentOf only with the meaning defined for that relation; the trace defines none of them. | Keeps public relation meanings with the patterns that define them. |
| **CC-C13-7 — Trace separation.** | Treat a materialized trace as a C.2.1 episteme about construction; creating, publishing, losing, or revising it does not create or end the whole, collection, or aspect it describes. | Keep ontology and epistemics separate. |
| **CC-C13-8 — Collection belonging is not component parthood.** | A `set` construction establishes no integrated assembly, acting eligibility, or holonhood. | Prevent collection-to-system drift. |
| **CC-C13-9 — Facet explicitness.** | A `slice` use names the exact aspect, bearer, governed facet, direct relation, and identity rule; a temporal window is not a structural facet here. | Prevent arbitrary slicing. |
| **CC-C13-10 — Subject owner.** | Apply C.13 to method, work, or discipline holons only after their direct patterns identify exact parts and whole-forming relations. | Permit accepted holon construction without generic decomposition. |
| **CC-C13-11 — Published-edge boundary.** | A direct structural Working-Model edge remains usable without a trace. If its publication elects B.3.5 or a named current requirement demands that profile, the edge follows B.3.5 for the required trace link and validation mode; C.13 does not treat that publication apparatus as the world-side relation, assembly, or identity rule. | Keep direct use, construction, and elected publication assurance distinct. |
| **CC-C13-12 — Dependent structure stop.** | A selected `U.Structure` is not a holon, agent, or a new whole named by an MHT claim merely by selection, label, or diagram. | Preserve the dependent-structure boundary. |
| **CC-C13-13 — Transformation stop.** | Do not infer transformation composition, parthood, holonhood, or atomism from entity construction, method or work decomposition, timing, or missing part facts. | Preserve the missing-governor boundary. |

### C.13:7.1 - Common Anti-Patterns and How to Avoid Them

* **Constructor as public relation.** A `Γ_m` trace is shown as the relation the working reader should use. Keep the exact direct relation in ordinary prose and use the trace only for the construction account.
* **Trace as cause.** A diagram, formula, parts list, or trace publication is said to create the assembly. Recover the actual inputs, obtaining relations, assembly, and identity rule.
* **Item in a collection treated as a component.** A `set` construction is used to infer integrated assembly structure. Keep collection belonging distinct; use `sum` only after constructive part relations and assembly independently obtain.
* **Same parts, same whole.** Two assemblies with the same component names are treated as one whole. Compare their obtaining relations, assembly rules, boundaries, and identity conditions.
* **Temporal constructor drift.** A phase, schedule, or assembly order is modeled as a Compose-CAL constructor. Keep temporal and method claims in their own planes.
* **Method or work shortcut.** Recipe steps, plan items, or WBS rows are called parts of an actual method or work occurrence. Use the direct method- or work-composition owner first.
* **Transformation shortcut.** Changes of constituents are called parts of one transformation because the entity was assembled. Return the exact missing transformation-composition governor and retain the separately identified changes.

### C.13:8 - Consequences

**Benefits**

- **Inspectable construction.** A practitioner can recover which exact inputs, relations, and rule support one assembly, collection, or aspect.
- **Identity clarity.** The account distinguishes the input list from the assembly and keeps whole reidentification with the direct identity rule.
- **Human-first use.** Ordinary ComponentOf, belongs-to, and AspectOf sentences remain readable; notation is optional shorthand for a named construction use.
- **Plane separation.** Order, time, evidence, representation, kind admission, and receiving reliance keep their direct owners.
- **Cross-domain reuse.** The same three forms can describe system, episteme, method, work, discipline, collection, and aspect cases without claiming one universal part relation.
- **Truthful stops.** Missing direct part or transformation-composition governors remain visible instead of being hidden by a trace.

**Costs and mitigations**

- A truthful trace needs more than a parts list: exact relations, assembly, and identity conditions must be named. Reuse a direct pattern's existing facts rather than duplicating them.
- A world-side construction can obtain before anyone writes a trace, and its direct relation claim can remain usable without an assurance profile. When its publication elects B.3.5 or a named current requirement demands it, materialize the required trace and validation mode without treating publication as the cause of construction.
- The same inputs can support different assemblies, and one whole can survive permitted replacements. Always carry the direct reidentification rule.

> **One-line takeaway.** `sum`, `set`, and `slice` explain an already grounded construction; they do not create its entities, relations, identity, evidence, or holonhood.

### C.13:9 - Rationale (informative)

**Why exactly three forms?**

`sum`, `set`, and `slice` keep three recurring practitioner questions apart:

- `sum` asks how exact constituents and constructive relations assemble an integrated whole;
- `set` asks which entities belong to a collection under that collection's identity and belongs-to rule;
- `slice` asks which exact aspect is distinguished from one bearer under a governed facet.

The forms are intentionally small, but their inputs do not determine ontology by themselves. An assembly is more than a set of part names; a collection is not automatically a holon or agent; and a facet label is not an aspect occurrence. The direct patterns provide relation obtaining and occurrence identity, while the candidate's direct pattern decides whether the existing whole continues or a new whole must be identified.

**Why traces remain epistemic.** A construction can obtain before anyone writes its account. A materialized trace is claim-bearing content used to inspect, communicate, or support that account. Evidence and assurance may warrant the claim, G.11 may govern the selected edition's currentness, and the account may be relied on in receiving work or declined for that use. None of those epistemic results changes the world-side assembly by itself.

**Why order, time, selected structure, and transformation composition are outside.** Method order and temporal extent answer different questions from parthood. A selected `U.Structure` is an organization of relations for a use, not automatically another holon. Entity construction also supplies no law by which several actual changes compose into one transformation. Keeping these stops explicit prevents an economical notation from becoming an ungoverned ontology.

### C.13:9.1 - SoTA-Echoing

Constructional ontology and applied mereology both require explicit choices about constructors, dependence, identity, and the relation between a construction account and the object constructed. C.13 adopts that pressure by requiring exact inputs, obtaining direct relations, assembly, and reidentification. It rejects the stronger shortcut that a term, graph, extensional input set, or written constructor expression alone settles the existence or identity of the whole.

Model-based engineering likewise separates a readable structural model from the physical, operational, informational, method, or work organization it describes. C.13 keeps that model useful while routing representation, evidence, assurance, and currentness to their direct patterns.

`A.14:14` supplies the source decision used by the `set` and `slice` forms. For `set`, it requires the collection's own belongs-to rule and blocks both automatic parthood and the conclusion that separate parthood is impossible. For `slice`, it requires an obtaining `AspectOf` relation with its bearer, facet rule, and identity conditions; a Characteristic, view, projection, partition, or time window does not substitute. If that A.14 source account changes, recheck only the affected `set` or `slice` contract, normative row, and link to A.14 here. An ordinary change to a collection rule or occurrence, aspect or bearer, facet rule, identity condition, or materialized trace reopens only that construction account and the claim it reports.

### C.13:10 - Relations

**Builds on**

- **A.14 and the patterns for each relation.** They define and test the participants, conditions, recurrence, and occurrence identity for component, collection-specific belongs-to, aspect, portion, constituent, and other constructive relations.
- **C.2.1.** It governs the identity of a materialized construction-trace episteme.

**Coordinates with**

- **B.3.5.** Governs the required trace link and validation mode only for a structural Working-Model edge covered by an elected profile or named current requirement. Its publication and assurance apparatus does not create the construction or decide whole identity.
- **A.1 and B.2.** A.1 consumes constructive assembly as one component of holon recognition; B.2 consumes exact construction and direct reidentification facts when the question is whether the existing whole continues or a new whole must be identified. C.13 decides neither public-kind recognition nor whole reidentification.
- **B.1.5 and direct method-composition patterns.** Supply exact submethods, whole-forming relations, constraints, and whole-method reidentification before a method construction is narrated.
- **A.15 and direct work-mereology patterns.** Supply exact work parts and whole-forming relations before a dated work construction is narrated.
- **C.20 and direct discipline-composition relations.** Supply exact discipline constituents, whole-forming relations, and identity conditions before a discipline construction is narrated.
- **A.22 and A.1.1.** Keep selected relation organization and bounded model use distinct from construction of the underlying holon.
- **A.3.4.** Identifies each actual bounded change independently; C.13 supplies no transformation-composition law.
- **C.29.** Keeps formulas, graphs, diagrams, and traces as representations of independently recovered objects when representation is current.
- **A.7.1 and A.22.CGUS.** Handle diagnostic return and the wider structural projection from construction to a target kind or logical representation when those uses are current.

**Constrains**

- A pattern that relies on a constructive whole states that whole, its constituents, the part relations that obtain, the assembly rule, and the identity rule rather than relying on a list or diagram.
- Collection, aspect, method, work, discipline, selected-structure, and transformation cases keep their direct owners and stop at missing governors.
- New construction forms require a separate parsimony and use argument; ordinary time, order, evidence, representation, and domain labels do not justify one.

**Provides**

- the three construction narratives `Γ_m.sum`, `Γ_m.set`, and `Γ_m.slice`;
- a plain-language discipline for connecting those narratives to exact direct facts without making the trace their cause;
- explicit unassembled-collection, selected-structure, existing-whole continuity or new-whole identification, and transformation-composition stop conditions.

### C.13:End

