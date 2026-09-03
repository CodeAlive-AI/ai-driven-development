## A.14 - Advanced Mereology: Components, Portions, Aspects & Phases
> **Type:** Kernel mereology and part-whole relation discipline pattern
> **Status:** Stable

**At a glance.** Use A.14 when wording such as *part*, *member*, *portion*, *aspect*, or *phase* could hide different claims. Recover whether the subject is a constructive part, belongs to a collection, is an amount of the same stuff, is one aspect, or is the same carrier during a proper time interval before downstream architecture, Work, assurance, or U-kind admission relies on it.

**Use this when.** Use this pattern when a text says that something is part of something else, belongs to a collection, is some amount of the same stuff, is an aspect of one holon, or is the same holon during a time interval, and choosing the wrong relation would change identity, aggregation, responsibility, evidence, or structural grounding.

**What goes wrong if missed.** Teams count members as components, portions as components, aspects as separate wholes, or phases as separate objects; constructive traces and Working-Model relation claims then ground the wrong EntityOfConcern.

**What this buys.** One human-facing relation catalogue that keeps constructive components and constituents, measured portions, bearer-dependent aspects, proper temporal phases, and collection belonging under each collection's own rule distinct without inventing a catch-all *aspect* or *member* vocabulary.

**Not this pattern when.** Not this pattern when the current question is only a selected Characteristic (`C.16`/`A.19`), viewpoint or view (`E.17.0`/`E.17.1`), representation or projection (`C.29` or its direct projection pattern), temporal claim without a `PhaseOf` relation (`C.27.TA`), constructive trace (`C.13`), Working-Model assurance grounding (`B.3.5`), meta-holon transition (`B.2`), or general U-kind admission (`E.24.UK`).

### A.14:1 - Problem frame - why an advanced mereology?

Before choosing a relation, identify the candidate part and whole, or the entity and collection. Use their normal identity rules. A local system-role kind, Method, Work occurrence, view, or trace does not become a structural part merely because the text calls it one; use its own pattern unless a separate part claim is established.

Four recurring questions then matter:

1. **Quantities vs. parts.** Engineers routinely need “some of the fuel”, “the first 10 pages”, or “a 30% subset of data”. This is not a component; it is a **portion** of a stuff-like whole, governed by measures and conservation.

2. **Selected concern vs. structural aspect.** Engineers also say “the thermal aspect”, “the safety view”, or “the inspection slice”. A Characteristic, viewpoint, representation, selected partition, or time window does not become a world-side part by that wording. `AspectOf` is used only for a bearer-dependent structural part distinguished under a named facet rule.

3. **Change vs. replacement.** “The prototype **before calibration**” may be a proper temporal restriction of one unchanged pump. By contrast, “v2 of the spec” first opens C.2.1 identity and, for two different epistemes, its independent edition-continuity test; “shift 1 vs. shift 2” first opens A.15.1 Work-part or occurrence law. None of those labels selects `PhaseOf` by itself.

4. **Belonging vs. construction.** “Vehicle 12 belongs to Fleet North” uses the fleet's own rule. That sentence alone makes neither the vehicle a constructive part nor the fleet an acting System, and it does not prohibit either separate claim.

### A.14:2 - Problem — what breaks without these distinctions?

If we only have “generic partOf” plus Component/Constituent, five classes of errors appear:

1. **Conservation errors.** Treating “20 L of fuel from Tank A” as a component leads to nonsense: adding and removing such “components” does not respect quantities; Γ_sys proofs violate Σ-balance.

2. **Aspect creation by wording.** A selected Characteristic, view, projection, partition rule, dashboard slice, or concern label is turned into a world-side part without identifying the aspect, bearer, facet rule, or identity condition.

3. **Temporal smearing.** Flattening “before/after” for one enduring carrier into a timeless whole collapses history; treating two changed epistemes or two Work occurrences as temporal pieces of that carrier collapses identity and occurrence history. Γ_time and Γ_method cannot repair either mistake after the fact.

4. **Identity confusion.** Modelling a “new version” as a component or phase lets a label decide identity. For an episteme, first compare the C.2.1 identity triple and then test edition continuity separately; for another enduring holon, apply its direct identity rule to determine whether the same individual persists or a reidentification question opens.

5. **System-role leakage.** A local system-role kind, assignment, or relation-position label is put into a part tree (“the PumpRole is part of the plant”), making structural reasoning brittle.

### A.14:3 - Forces

| Force | Tension |
| --- | --- |
| **Expressiveness vs. parsimony** | Portion, aspect, and phase claims need usable direct relations, while the catalogue must not turn every concern word into a part kind. |
| **World-side structure vs. analysis** | A real bearer-dependent aspect must be stateable, while Characteristics, views, projections, partitions, and time windows keep their own meanings. |
| **Universality vs. domain nuance** | One relation discipline must serve physical systems and epistemes, while measurement, facet rules, and time behave differently by subject. |
| **Identity vs. change** | Preserve the same bearer or carrier through allowed change, while making reidentification explicit when its rule fails. |
| **Readable claim vs. assurance** | The ordinary relation sentence must stand on its own, while a named assurance use may require a `sum`, `slice`, or `set` account. |

### A.14:4 - Solution — extend the mereology catalogue, keep it clean

**A.14 defines three direct sub-relations of `partOf`** and re-affirms the firewall between mereology and neighboring claims:

1. **PortionOf** — a measured part of a whole under one extensive measure and boundary rule.
2. **AspectOf** — a bearer-dependent structural part distinguished under a named facet rule.
3. **PhaseOf** — the same carrier restricted to a proper time interval.
4. **Keep local kinds, Methods, and Work out of structural part trees.** Do not treat a local system-role kind or a Method as a structural part. A separately identified System or Episteme may have its own direct part relation; use method-composition patterns for submethods and A.15.1 for Work parts and occurrences.
5. **Use the collection's own belongs-to rule.** State who or what may belong, what makes belonging begin and end, and how recurrence and past belonging are handled. FPF does not use one public `MemberOf` relation for unlike collections. Belonging alone establishes neither holonhood nor parthood, and it does not rule out a separately grounded constructive part relation after all six A.1 matters pass.

The classical pair **ComponentOf** (structural, discrete) and **ConstituentOf** (conceptual, logical/epistemic) remain as in the kernel; A.14 only clarifies **how to tell them apart from Portion/Phase** (§ 6).

### A.14:5 - Formal cores (normative semantics)

#### A.14:5.1 - PortionOf — metrical part of a measurable whole

**Intent.** Capture “some of the same stuff/extent”, governed by a measure that adds up.

**Applicability.** Any `U.Holon` that carries an **extensive** measure μ on the chosen scope
(examples: mass, volume, length‑of‑text, byte size, wall‑time budget).

**Primitive.** `PortionOf(x, y)` means: *x is the same kind of stuff/content as y, but less*.

**Axioms (A14‑POR‑\*)**

* **POR‑1 (Partial order).** PortionOf is reflexive, antisymmetric, transitive on its domain.
* **POR‑2 (Metrical dominance).** If `x ProperPortionOf y` then `0 < μ(x) < μ(y)` for the agreed μ.
* **POR‑3 (Additivity on disjoint portions).** If `PortionOf(x,y)`, `PortionOf(z,y)`, and `x ⟂ z` (the two portions do not overlap), and their join is admitted under the same measure and boundary rule, then `μ(x ⊔ z) = μ(x)+μ(z)` and `PortionOf(x ⊔ z,y)`. `ProperPortionOf` additionally requires the joined measure to remain strictly below `μ(y)`; a join equal to the whole is `PortionOf` but not `ProperPortionOf`.
* **POR‑4 (Kind integrity).** x and y must share the same **measure kind** and **unit** (or a declared conversion).
* **POR‑5 (Boundary compatibility).** For physical wholes, the whole’s boundary encloses the union of its portions; cross‑boundary “leaks” are interactions, not portions.

**Didactic tests.**
✔ “5 kg from a 20 kg billet” — PortionOf.
✔ Two disjoint 5 kg cuts from the same 20 kg billet have a 10 kg join under the same mass unit and boundary rule; that join is still a ProperPortionOf the billet.
✔ “Pages 1–10 of the report” — PortionOf (μ = page or token count).
✘ “The pump module of the plant” — **ComponentOf**, not PortionOf.
✘ “The Methods section of the paper” — **ConstituentOf**, not PortionOf.

#### A.14:5.2 - PhaseOf — temporal part of the same carrier

**Intent.** Capture “the same holon during a sub‑interval”, preserving identity through change.

**Applicability.** Any `U.Holon` that persists across time with a recognised **carrier identity**.

**Primitive.** `PhaseOf(x, y)` means: *x is y restricted to a proper time interval*.

**Axioms (A14‑PHA‑\*)**

* **PHA‑1 (Strict temporal parthood).** `PhaseOf` is irreflexive, asymmetric, and transitive on proper temporal restrictions of one unchanged carrier. In particular, `PhaseOf(y,y)` is false: a whole-lifetime or self-reference is not a proper temporal part.
* **PHA‑2 (Proper interval and same carrier).** `PhaseOf(x,y)` requires the interval of x to be a proper sub-interval of y's interval and the carrier-identity rule to hold throughout both. It does not require x to be a maximal cell of a partition.
* **PHA‑3 (Nesting and overlap are allowed).** Temporal restrictions of the same carrier may nest or overlap. A week may be part of a year-long phase, and a diagnostic window may overlap a calibration window. Those facts are not contradictions and do not by themselves select an aspect or partition.
* **PHA‑4 (Selected partition is an additional claim).** When a use needs exhaustive non-overlapping cells, declare one carrier, one interval to be covered, one analysis aspect or partition rule, and the selected family of `PhaseOf` values. Only cells of that same explicitly selected partition must be pairwise non-overlapping and jointly cover the declared interval. Another aspect or rule may select a different, overlapping family.
* **PHA‑5 (Identity through change).** Properties may vary between phases, but the carrier’s identity criteria hold continuously (e.g., same serial number, same legal identity, same theorem statement).
* **PHA‑6 (Escalation to MHT).** If identity criteria break (e.g., metamorphosis with new objectives), **declare a Meta‑Holon Transition (B.2)** rather than a PhaseOf.

**Didactic tests.**
✔ “PumpUnit\#3 **before** calibration” — PhaseOf(Pump\#3\_pre, Pump\#3).
✔ If `PhaseOf(Pump#3@week-32, Pump#3@2026)` and `PhaseOf(Pump#3@2026, Pump#3)`, transitivity also gives `PhaseOf(Pump#3@week-32, Pump#3)`. A high-vibration diagnostic window may overlap a calibration window for the same pump; neither is thereby a cell of one selected partition.
✔ “Specification episteme E during τ₂”, with the C.2.1 identity triple unchanged and a proper interval current — PhaseOf(E@τ₂, E). ✘ “Spec v2” — if a C.2.1 discriminator changed, identify another episteme and test `EpistemeEditionRelation(E_v1,E_v2)` separately; the label proves neither identity nor continuity.
✘ “Shift 1 of the same batch run” — use A.15.1 `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, or another exact Work-part or occurrence relation whose predicate obtains.
✘ “Prototype vs. production unit” — likely **different carriers**; use ComponentOf/ConstituentOf or MHT per criteria.

#### A.14:5.3 - AspectOf — bearer-dependent structural part under one named facet rule

**Intent.** State that one identified bearer-dependent part is an aspect of its bearer without turning a Characteristic, viewpoint, representation, concern, partition, or time window into a part.

**Participants and qualifier.** `x` and `y` occupy the `U.Holon` parthood domain: `x` is the aspect and `y` its bearer. Each must already satisfy its applicable holon-kind and identity rule; `AspectOf` does not grant systemness, agency, or independent-whole status. The qualifier `f` names the facet rule used in this occurrence; it does not introduce a universal `U.Facet` kind.

**Primitive.** `AspectOf(x, y; f)` means: *x is the bearer-dependent structural part of y distinguished under facet rule f*. The notation shows the required qualifier; the public sentence may remain “x is an aspect of y under the f rule.”

**Obtaining conditions and properties (A14-ASP-*).**

- **ASP-1 (Identified occurrence).** Name x, y, f, the relation occurrence, and the aspect-identity rule. The facet rule states what distinguishes x from the rest of y and what change preserves or ends this aspect.
- **ASP-2 (Structural dependence).** `AspectOf(x,y;f)` implies `ut:StructPartOf(x,y)`, `x != y`, and asymmetry for that occurrence. It implies none of ComponentOf, ConstituentOf, PortionOf, PhaseOf, collection belonging, or independent systemhood.
- **ASP-3 (Facet-local and non-transitive).** An occurrence under f gives no occurrence under another facet. `AspectOf` is not assumed transitive through another bearer or facet; state every relied-on relation directly.
- **ASP-4 (Bearer and aspect identity).** If the bearer is reidentified, or f and the aspect-identity rule no longer identify x, the old occurrence ends. A changed view, diagram, name, or measurement does not by itself change the world-side occurrence.
- **ASP-5 (Neighbor boundary).** A measured quality routes to `C.16`/`A.19`; a viewpoint or view to `E.17.0`/`E.17.1`; a representation or projection to `C.29` or its direct projection pattern; a selected temporal window to `PhaseOf` or `C.27.TA`; a selected partition to the pattern governing that structure. None creates `AspectOf` by selection alone.

**Didactic tests.**

- ✓ In Reactor-7, the thermal-boundary rule distinguishes ThermalEnvelope-7 as the connected enclosure of insulation panels, seals, and boundary interfaces that constrains heat transfer across the reactor boundary. ThermalEnvelope-7 is identified by the continuing enclosure under that rule, not by a fixed panel list. `AspectOf(ThermalEnvelope-7, Reactor-7; thermal-boundary)` obtains while that enclosure and Reactor-7 continue. Replacing one panel under the same rule preserves the aspect; dismantling the enclosure, replacing the facet rule with a different boundary, or reidentifying Reactor-7 ends the occurrence. A changed temperature reading or dashboard view does not.
- ✗ “Safety is an aspect of the design” when *safety* is only a Characteristic, concern, viewpoint, or heading. Recover that actual claim first.
- ✗ “Pump-7 during warm-up is its thermal aspect.” Use `PhaseOf` for the proper temporal restriction and `A.19` for a measured thermal Characteristic when those claims obtain.

#### A.14:5.4 - CT2R-LOG and Compose-CAL handshake

- A direct structural parthood claim is usable without this assurance handshake. If the publication elects B.3.5 or a named current requirement demands it, link the claim through `tv:groundedBy` to its applicable current C.2.1 `Γ_m.sum` or `Γ_m.slice` construction-trace episteme and declare `validationMode=axiomatic`. The direct relation pattern decides whether the occurrence obtains and how it is identified; the relevant entity pattern decides identity through change. The trace only reports that basis.
- **AspectOf** uses one current `C.13 slice` trace when that assurance branch is elected. The trace names the aspect, bearer, facet rule, relation occurrence, and identity conditions; it creates none of them.
- **PhaseOf** is temporal parthood and shall not be grounded through `Γ_m`. Its assurance follows the same-carrier and proper-interval criteria, the separately declared selected-partition rule when one is claimed, and `Γ_time` ordering (`B.1.4`).
- A collection's own belongs-to relation remains distinct from constructive parthood (`CC-MEM-2`). State its participants, what makes it obtain, and whether later belonging is the same occurrence or a new one under the collection's pattern. A direct claim needs no B.3.5 fields. If B.3.5 assurance is elected, link `validationMode=axiomatic` to one current `C.13 set` trace that reports the relation that already obtains. The trace supports neither a ComponentOf inference nor a universal prohibition on separately grounded parthood.

Two quick identity tests apply before relying on a trace. The same listed constituents can form a different whole when their direct assembly relations or rule differ. Conversely, a permitted constituent replacement can preserve the same whole. An equal input list, a repeated trace, or `validationMode=axiomatic` decides neither case.

### A.14:6 - Choosing the right relation (decision table)

| You want to say... | Use | Why |
| --- | --- | --- |
| “This is a piece of the same stuff or extent.” | **PortionOf** | One extensive measure and conservation rule govern the claim. |
| “This is a discrete structural part inside the whole.” | **ComponentOf** | The part is structurally integrated; amount and facet selection do not decide it. |
| “This is a logical or content part of a conceptual whole.” | **ConstituentOf** | The claim concerns conceptual or epistemic assembly. |
| “This dependent structural part is one aspect of this bearer under this facet rule.” | **AspectOf** | Name the aspect, bearer, facet rule, occurrence, and identity rule; a Characteristic, view, projection, partition, or time window is not enough. |
| “This is the same entity during a proper sub-interval.” | **PhaseOf** | The same carrier and its identity rule hold over a proper temporal restriction. |
| “This item belongs to that collection.” | **The belongs-to rule defined for that collection** | Name the entity and collection, state what makes belonging begin and end, and distinguish recurrence. Belonging establishes neither parthood nor its impossibility. |
| “This System holds a local work-facing kind or relation position.” | local system-role-kind classification, `U.SystemRoleAssignment`, or an A.6.5 relation position | Kind classification, assignment occurrence, and relation participation are not parts. |

> **Firewall reminder.** If the sentence is about system-role-kind classification or assignment, how action is done, or what happened when, use `A.2`/`A.2.1`, `A.3.1`, or `A.15.1` as appropriate. For an episteme, use A.14 for content parthood or a proper interval of one unchanged C.2.1 identity; changed claims, EntityOfConcern, or effective reference scheme identify another episteme, and any historical continuation uses C.2.1 `EpistemeEditionRelation` only when its predicate obtains.

### A.14:7 - Archetypal Grounding

| Relation | `U.System` example | `U.Episteme` example or boundary |
| --- | --- | --- |
| **PortionOf** | 50 L from a 200 L fuel tank under volume μ. | Pages 1-10 from a 120-page report under page or token count. |
| **ComponentOf** | Impeller ComponentOf PumpUnit. | Figure 2 ComponentOf a physical poster layout. |
| **ConstituentOf** | Control law ConstituentOf Controller Design. | Lemma A ConstituentOf Theorem Proof. |
| **AspectOf** | ThermalEnvelope-7 AspectOf Reactor-7 under the thermal-boundary rule; `A.14:5.3` shows the bearer, enclosure, occurrence, identity, preservation, and ending conditions. | A selected view, concern, heading, or projection of an episteme is not AspectOf. Use this relation only if a bearer-dependent structural aspect, facet rule, occurrence, and aspect identity are independently established. |
| **PhaseOf** | PumpUnit-3 before calibration, with the same carrier identity. | One unchanged theorem episteme restricted to a proper interval while its C.2.1 identity remains fixed. |
| **Collection belonging** | “Vehicle 12 belongs to Fleet North under its registration rule.” The rule supplies beginning, ending, recurrence, and history; the claim establishes neither holonhood nor parthood. | The same discipline applies to collections of epistemes. Listing or publishing them creates no occurrence. |

### A.14:8 - Bias-Annotation

A.14 corrects parthood bias: ordinary words such as *part*, *member*, *phase*, *aspect*, *section*, *version*, *module*, *function*, *role*, and *ingredient* can hide different objects or relations. Recover whether the source means component, constituent, measured portion, bearer-dependent aspect, proper temporal phase, collection belonging, local system-role-kind classification, assignment, Method, Work, evidence, or transformation.

It also corrects analysis and representation bias. A Characteristic, viewpoint, view, projection, selected partition, dashboard slice, diagram, table row, or time window may describe or foreground something about a bearer without becoming a world-side structural aspect. `AspectOf` begins only after the aspect, bearer, facet rule, relation occurrence, and aspect identity are established. Publication or construction traces report such a claim; they do not create it.

### A.14:9 - Conformance Checklist - type guards

#### A.14:9.1 - Global firewall and scope

| ID            | Requirement                                                                                 | Purpose                                                 |
| ------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **CC-A14-0** | A local system-role kind **MUST NOT** occur as a node in any `partOf` chain by kind identity; a `U.System` classified by that kind remains eligible for holon mereology on its independent system identity. `U.Method` **MUST NOT** occur in A.14 structural `ComponentOf` or structural `partOf` chains by method identity alone; A.3.1 and B.1.5 define submethod assembly. If an exact admission predicate establishes a different carrier, such as a `SystemRoleKindDescription`, Work occurrence, `U.SystemRoleAssignment` occurrence, `SystemRoleKindRelationStructure`, method relation structure, or episteme, name that carrier, assertion, and subject-pattern locator. | Keeps local system-role kinds out of holon mereology by kind identity and keeps method holarchy out of structural component mereology while preserving admitted carriers. |
| **CC‑A14‑0a** | `U.MethodDescription` / `U.WorkPlan` and other describing epistemes **MAY** participate in `partOf` only as `U.Episteme` nodes: content `ConstituentOf`, measured text `PortionOf`, or `PhaseOf` for a proper interval of one unchanged C.2.1 identity. A changed C.2.1 discriminator identifies another episteme; connect two such identities only through an independently obtaining `EpistemeEditionRelation`. They **MUST NOT** be asserted as `ut:StructPartOf` of any `U.System`. | Allows episteme structure and legitimate temporal restriction without smuggling Methods or automatic edition continuity into structure. |
| **CC‑A14‑0b** | A collection-belonging relation **MUST NOT** be inferred or auto-rewritten as any `partOf` sub-relation. This non-inference does not prohibit a separately grounded constructive part relation for the same entities. | Separates collection belonging from parthood without assuming they can never coexist. |
| **CC‑A14‑0c** | `SerialStepOf` / `ParallelFactorOf` **MUST NOT** appear in any `partOf` chain or table in A.14; model order and concurrency potential via **A.15** and direct method-composition patterns such as `B.1.5`. If a node linked by those relations is also a submethod, state that `U.Method` claim separately before using method holarchy. | Prevents the “order‑as‑structure” and “edge-as-part” category errors.       |

#### A.14:9.2 - PortionOf guards

| ID                                 | Requirement                                                                                                                                                               | Purpose                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **CC‑POR‑1 (Domain)**              | `PortionOf(x,y)` is valid only if the modelling scope declares at least one **extensive measure** μ for y (mass, volume, token count, byte size, wall‑time budget, etc.). | Prevents “portion” without a measure.   |
| **CC‑POR‑2 (Kind)**                | x and y **SHALL** share the same μ‑kind and compatible units (or an explicit conversion).                                                                                 | Prevents apples‑to‑oranges addition.    |
| **CC‑POR‑3 (Monotone additivity)** | For disjoint portions `x ⟂ z` with `PortionOf(-,y)`: μ(x ⊔ z) = μ(x)+μ(z).                                                                                                | Secures Σ‑reasoning and Γ\_sys proofs. |
| **CC‑POR‑4 (Boundary)**            | For physical systems, the whole’s boundary encloses the union of portions; cross‑boundary flows are **not** portions.                                                     | Distinguishes stock vs flow.            |
| **CC‑POR‑5 (Non‑replacement)**     | “Replacing 20% of y by v” **MUST** be modelled as **PortionOf** removal + **Component/Constituent** insertion, not as a single PortionOf rewrite.                         | Avoids silent identity change.          |

#### A.14:9.3 - PhaseOf guards

| ID                                    | Requirement                                                                                                                                                      | Purpose                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **CC‑PHA‑1 (Proper interval & carrier identity)** | `PhaseOf(x,y)` requires `x ≠ y`, a proper sub-interval of y's interval, and an explicit identity criterion for y valid throughout both restrictions (e.g., serial number, legal identity, theorem statement). | Excludes self/whole-lifetime phasing and prevents re-identification by stealth. |
| **CC‑PHA‑2 (Nesting & overlap)** | Nested or overlapping `PhaseOf` values for one carrier **MAY** obtain. Do not infer a partition, aspect difference, or carrier difference merely from overlap. | Keeps universal temporal parthood consistent and permits ordinary windows. |
| **CC‑PHA‑3 (Selected partition)** | If a claim selects an exhaustive partition, it **MUST** name one carrier, covered interval, aspect or partition rule, and family of phase cells. Only cells of that same selected partition are required to be pairwise non-overlapping and jointly cover the declared interval. | Makes coverage and non-overlap local to the claim that needs them. |
| **CC‑PHA‑4 (Escalation)**             | If identity criteria fail during change, declare a **Meta‑Holon Transition** (B.2) instead of PhaseOf.                                                           | Makes re‑identification explicit.      |
| **CC-PHA-5 (Episteme & Work boundary)** | `PhaseOf` **MAY** restrict one unchanged `U.MethodDescription` episteme to a proper interval only after its C.2.1 identity triple remains fixed. Changed description epistemes use `EpistemeEditionRelation` only when C.2.1's historical-continuation predicate obtains. Work intervals, episodes, performed parts, retries, resumptions, and later occurrences **SHALL** use A.15.1's exact relations; generic `PhaseOf` is not their substitute. `PhaseOf` never applies to a local system-role kind by kind identity or to `U.Method`. | Keeps episteme identity, edition continuity, and Work-temporal law with their subject patterns. |

#### A.14:9.4 - AspectOf guards

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-ASP-1 (Participants and rule)** | Name the aspect and bearer in the `U.Holon` parthood domain, the facet rule, the relation occurrence, and the aspect-identity rule. The relation grants neither systemness nor independent-whole status. | Prevents an aspect label from admitting its own object. |
| **CC-ASP-2 (Obtaining)** | The facet rule must state what distinguishes the aspect and what change preserves or ends it. A chosen concern, Characteristic, viewpoint, view, projection, partition, label, or temporal window establishes no `AspectOf` occurrence. | Keeps selection and description from becoming world-side parthood. |
| **CC-ASP-3 (Relation properties)** | `AspectOf(x,y;f)` implies one asymmetric `ut:StructPartOf(x,y)` occurrence with `x != y`. Infer neither another facet occurrence, transitivity, ComponentOf, ConstituentOf, PortionOf, PhaseOf, collection belonging, nor independent systemhood. | Keeps the relation facet-local and non-omnibus. |
| **CC-ASP-4 (Identity and assurance)** | Bearer reidentification or failure of the facet and aspect-identity rule ends the old occurrence. A direct claim needs no B.3.5 fields; after profile election it uses one current `C.13 slice` trace and `validationMode=axiomatic`. | Keeps occurrence identity and optional assurance separate. |

#### A.14:9.5 - Grounding and validation (normative)

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-GND-1** | A direct `ut:StructPartOf` assertion is usable without this assurance profile. When its publication elects B.3.5 or a named current requirement demands that profile, the assertion must use `validationMode=axiomatic` and link through `tv:groundedBy` to its applicable current C.2.1 `sum` or `slice` construction trace. The trace reports independently grounded participants, direct relation occurrences, the construction rule, and identity or reidentification conditions; it creates none of them. | Makes an elected assurance basis inspectable without making it the relation's truth-maker. |
| **CC-GND-2** | For epistemic edges (`ut:EpiPartOf` and its sub-types), `tv:groundedBy` is optional; instead supply `ev:evidence` and set `validationMode in {axiomatic, postulate, inferential}`. | Harmonises evidence treatment for epistemic edges. |
| **CC-GND-3** | The public query Standard remains `?x ut:PartOf+ ?y`; every result still depends on its direct relation semantics and identity. Alias, trace, or validation mode creates or reidentifies no occurrence. | Preserves one query surface without moving authority into assurance apparatus. |

*Note.* Property names and trace semantics are defined in CT2R-LOG and Compose-CAL.

#### A.14:9.6 - Collection belonging and separately grounded parthood

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-MEM-1** | State collection belonging with the predicate defined for that subject. Name the entity, collection, collection identity rule, what makes belonging begin and end, whether it can recur, and how past belonging is said. | Keeps unlike fleets, corpora, communities, populations, products, and Suites under their own rules. |
| **CC-MEM-2** | From collection belonging alone infer neither a constructive part relation nor holonhood. Also do not infer that either is impossible. | Separates non-implication from universal prohibition. |
| **CC-MEM-3** | If the same collection independently passes all six `A.1` matters and a constructive part relation obtains, publish that second claim under its direct pattern. A direct belonging sentence needs no B.3.5 fields. When B.3.5 assurance is elected for it, use `validationMode=axiomatic` and one current `C.13 set` trace; the trace reports the collection, entities, relation occurrences, rule, and identity conditions and creates none of them. | Keeps collection belonging, constructive parthood, assurance, and collective action separate. |

#### A.14:9.7 - CT2R‑LOG handshake (Working‑Model → Assurance)

| ID                 | Requirement                                                                                                                                                              | Purpose                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **CC-A14-10** | A published direct relation may remain usable without B.3.5 fields. When its publication elects B.3.5, follow the relation's branch: structural parthood links its current `sum` or `slice` construction trace, while collection belonging links one current `C.13 set` trace under the collection's own rule; both declare `validationMode=axiomatic`. The direct relation and identity tests remain decisive; trace and mode create neither occurrence nor identity. | Keeps direct use lightweight while making an elected assurance posture inspectable. |
| **CC‑A14‑11**      | **PhaseOf** edges **SHALL NOT** use Γ_m for grounding. The relation record **SHALL** provide identity and proper-interval criteria per **CC‑PHA‑1/2**; a selected exhaustive partition additionally follows **CC‑PHA‑3** and references **Γ_time** when ordering matters. | Keeps temporal parthood distinct from construction and partition-specific constraints.       |

#### A.14:9.8 - Relation-use decision procedure

**Step 0 — Recover the claim.** If the sentence concerns system-role-kind classification or assignment, Method, Work, evidence, a Characteristic, viewpoint, view, projection, partition, or temporal claim without parthood, use that direct pattern. A.14 is not selected merely because ordinary speech says *part* or *aspect*.

**Step 1 — Is it measured stuff or extent?** If yes, use **PortionOf**. Declare μ, unit, boundary, and additivity conditions.

**Step 2 — Is it a discrete integrated or conceptual part?** If yes, use **ComponentOf** or **ConstituentOf**. Do not use PortionOf merely because the part can also be measured.

**Step 3 — Is it the same carrier during a proper sub-interval?** If yes, use **PhaseOf** after the carrier-identity and interval tests. Another episteme or Work occurrence uses its own identity and relation patterns.

**Step 4 — Is it a bearer-dependent structural aspect?** Use **AspectOf** only after naming the aspect, bearer, facet rule, relation occurrence, and aspect-identity rule. If the source names only a Characteristic, viewpoint, view, projection, selected partition, concern, or time window, return that actual claim instead.

**Step 5 — Does the entity belong to a collection?** Use the belongs-to rule defined for that collection after naming the entity, collection, beginning, ending, recurrence, and history conditions. Infer neither part nor holonhood and do not infer that separately grounded parthood is impossible. If collective action is current, apply all six A.1 matters separately.

**Quick spot-tests.**

| Smell | Likely error | Fix |
| --- | --- | --- |
| “20% of the chassis” | Structure is treated as stuff. | Use ComponentOf for the chassis part; use PortionOf only for material stock under one measure. |
| “Chapter 2 is 15% of the book” | Content assembly and text measure are collapsed. | Use ConstituentOf for the chapter and a separate PortionOf measurement statement. |
| “Safety is an aspect of the design.” | Characteristic, concern, viewpoint, or structural aspect remains unresolved. | Recover the actual claim. Use AspectOf only with an identified aspect, bearer, facet rule, occurrence, and identity condition. |
| “The dashboard slice is an aspect of the reactor.” | A view or projection is made into a world-side part. | Use the view, publication, or representation pattern; add AspectOf only for an independently established reactor aspect. |
| “Spec v2 overlaps v1.” | A version label is asked to decide identity and phase. | Compare C.2.1 identities and test edition continuity; use PhaseOf only for one unchanged episteme over a proper interval. |
| “Team is part of the project.” | Collection belonging is confused with constructive parthood. | State the affiliation rule. If an integrated whole is also claimed, apply all six A.1 matters and state the part relation separately. |

#### A.14:9.9 - Interplay with Γ‑flavours (how these relations behave under aggregation)

| Γ‑flavour                    | Mereological hooks (what A.14 supplies)                                                                                                                | Key effect                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Γ\_sys (B.1.2)** | Treat PortionOf as additive stocks; ComponentOf respects boundary integration; AspectOf remains facet-local structural parthood and is not a separate aggregation operator; PhaseOf is not aggregated here. | Conserves extensive measures and prevents facets from becoming system decompositions. |
| **Γ\_epist (B.1.3)** | PortionOf of text or data uses a declared measure; ConstituentOf composes arguments or sections; AspectOf is available only for an independently admitted episteme-dependent structural aspect under a declared facet rule. A viewpoint, view, heading, or projection remains with E.17 or C.29. PhaseOf may restrict one unchanged episteme to a proper interval. | Preserves provenance and prevents description choices from creating episteme parts. |
| **Γ\_ctx / Γ\_time (B.1.4)** | **PhaseOf** supplies proper temporal restrictions, including nested or overlapping windows. A separately selected partition supplies non-overlap and coverage only for its own cells. Order/dependencies live in **Γ\_ctx** and method graphs (A.15/B.1.5). **PortionOf** is orthogonal (quantities inside steps/runs). | Ensures chronological consistency without turning every temporal restriction into one partition. |
| **Γ\_method (B.1.5)** | Γ\_method composes Methods rather than A.14 structural parts. A recipe-labelled claim-bearing episteme is a **MethodDescription** only when its `EntityOfConcern` is one admitted `U.Method` and at least one substantive way-of-doing claim obtains under A.3.2; any graph form is a representation handled by C.29, not evidence that the Method belongs to a collection. When a recipe refers to stuff-like inputs, those are **PortionOf** statements on resources. | Separates recipe composition from structure. |
| **Γ\_work (B.1.6)**          | Only **Work** carries resource deltas; when logging “consumed 5 kg from Tank A”, model it as **PortionOf** relation to the stock prior to consumption. | Makes Σ‑balance explicit; aligns with CC‑POR‑3/4.                                             |

### A.14:10 - Common Anti-Patterns and How to Avoid Them

- **Member as component.** A person, team, document, or object belongs to a collection and is then counted as structurally integrated.
- **Aspect by label.** A Characteristic, concern, viewpoint, view, projection, partition, heading, dashboard slice, or time window is called an aspect and entered into a part tree. Recover the actual claim; require the full AspectOf occurrence when structural parthood is intended.
- **System-role expression as part.** A local kind, assignment, or relation position is put into a part tree instead of using its direct pattern.
- **Method as part.** A Method, recipe, or algorithm is treated as a structural component instead of using Method, MethodDescription, Work, or transformation patterns.
- **Portion without measure.** Some fuel, data, time, or text is named as a portion without measure kind, unit, boundary, and additivity conditions.
- **Phase as replacement or lineage.** Another episteme, version label, or Work segment is treated as PhaseOf without applying C.2.1 or A.15.1.
- **Diagram or trace as relation.** A breakdown, graph, table, construction trace, or validation mode is used as proof that parthood or identity obtains.

### A.14:11 - Pedagogy aids (non-normative)

**Two-minute checklist for practitioners**

1. What subject and relation does the sentence claim?
2. Does every PortionOf have a declared extensive measure, unit, boundary, and additivity condition?
3. Does every AspectOf name the aspect, bearer, facet rule, occurrence, and identity rule—and avoid replacing a Characteristic, view, projection, partition, or time window?
4. Is every PhaseOf a proper interval of one unchanged carrier rather than another episteme or Work occurrence?
5. Does every collection claim use its own belongs-to rule without inferring or prohibiting a separate part relation?
6. Are local system-role kinds, assignments, Methods, Work, views, and traces kept outside the part tree unless an independently admitted carrier and direct part relation are current?

### A.14:12 - Consequences

**Benefits**

- **Predictable composition.** Additive portions, facet-local aspects, same-carrier phases, and explicit collection rules keep unlike claims separate.
- **Analysis does not create ontology.** Characteristics, viewpoints, views, projections, partitions, and time windows remain usable without being turned into structural parts.
- **History without confusion.** Aspect and phase identity changes are explicit; collection history stays with the collection's rule.
- **Readable first use.** A practitioner can state the direct component, constituent, portion, aspect, phase, or belongs-to sentence before any elected assurance account.

**Trade-offs and mitigations**

- **More distinctions.** Authors must name a measure for PortionOf, a facet and identity rule for AspectOf, or a proper interval and carrier identity for PhaseOf. The decision table and two-minute checklist keep the first move short.
- **Aspect judgement.** Distinguishing a structural aspect from a Characteristic, view, projection, or temporal claim requires judgement; neighboring patterns provide the stop and route.
- **Optional assurance effort.** `sum`, `slice`, and `set` traces are added only when B.3.5 or another named current requirement elects them.
- **Escalation discipline.** When bearer or carrier identity fails, use the direct reidentification pattern rather than preserving an AspectOf or PhaseOf occurrence by label.

### A.14:13 - Rationale

A.14 exists because part-whole words carry identity, aggregation, measure, facet, time, and assurance commitments. The pattern keeps those commitments in the direct relation instead of letting everyday nouns, concerns, views, diagrams, or breakdown tables decide ontology. Component, constituent, portion, bearer-dependent aspect, proper phase, and collection-belonging claims can then support downstream work without smuggling Characteristics, viewpoints, local kinds, assignments, Methods, Work, or publication claims into mereology.

### A.14:14 - SoTA-Echoing

This edition's collection-belonging rule follows the current constructional line: first identify what is being constructed and what gives it identity, then state the relation that actually obtains. It does not import a ready-made universal membership predicate.

| Source line | Useful contribution | Limit | A.14 decision and destination |
| --- | --- | --- | --- |
| Partridge et al., [the constructional turn](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/partridge-et-al-taking-a-constructional-turn-to-radically-enrich-a-top-ontologys-foundation.pdf), and [BORO C-FORS 2025](https://research.borosolutions.net/boro-ontology/) | Set, sum, tuple, and assembly constructors have different outputs, dependence, and identity conditions. | BORO's extensional, 4D, and unrestricted-composition commitments are not FPF defaults. | **Adapt.** Solution item 5 and `CC-MEM-1` distinguish a collection's own belongs-to rule from a `C.13 sum`; `CC-MEM-2/3` require a separate constructive-part claim rather than deriving or prohibiting it from belonging. |
| Florio and Linnebo, [constructional ontology](https://www.utwente.nl/en/eemcs/fois2024/resources/papers/florio-linnebo-introduction-to-constructional-ontology.pdf), and Borgo and Righetti, [applied constructional ontology](https://doi.org/10.3233/FAIA250480) | Givens, constructors, inputs, and construction processes must be distinguished; set, sum, and ordered-pair constructions are not interchangeable. | The applied work is exploratory and does not supply FPF's domain-facing identity, admission, use, or history rules. Its plural membership is not a world-side belongs-to predicate. | **Adopt the explicit-choice obligation; reject predicate import.** The decision table and Step 5 ask for the entity, collection, and its own beginning, ending, recurrence, and history conditions. |
| Kit Fine, [*Towards a Theory of Part*](https://doi.org/10.5840/jphil20101071139) | Composition comes before derived part claims, and different operations have different application, identity, presence, and character principles. | Fine's broad use of *part* can also cover set elements or sequence places; that umbrella is too broad for a practitioner-facing FPF relation. | **Adopt operational priority; narrow the public result.** `CC-MEM-2` blocks both the inference from belonging to parthood and the inference that parthood is impossible; `CC-MEM-3` admits the second claim only after all six `A.1` matters pass. |
| Kit Fine, [*The Identity of Social Groups*](https://doi.org/10.5334/met.45) | Structured groups can persist through changing manifestations, and the same participants need not identify the same group. | An identity-through-change rule does not make a register, corpus, product series, or Suite a structured whole. | **Adopt the identity questions, not automatic embodiment.** `CC-MEM-1` requires the collection's identity and belonging history; the A.1 gate remains separate. |

#### Aspect branch application

For AspectOf, the BORO and CCO rows above supply the constructor-sensitive question: which bearer, facet rule, dependent aspect, and identity conditions make this structural part? Fine's composition-first pressure blocks a bare *aspect* label from deciding parthood. A.14 adapts that line in `A.14:5.3`, the decision procedure, and `CC-ASP-1` through `CC-ASP-4`; `C.13 slice` remains an optional report, not the constructor of the aspect. The serious alternatives are routed rather than renamed: measured Characteristic (`C.16`/`A.19`), viewpoint or view (`E.17`), representation or projection (`C.29` or its direct pattern), selected partition, and temporal restriction (`PhaseOf`/`C.27.TA`). This route is no worse for correctness and cheaper for a cold reader than a universal *aspect* kind; its cost is that the author must identify the actual relation before reusing the word.

The resulting collection alternatives are deliberately distinct:

- **Selected:** an ordinary subject-specific belongs-to sentence plus the collection's own rule.
- **Rejected:** one generic `MemberOf`, because it collapses formal inclusion, classification, participation, collection belonging, and constructive parthood.
- **Rejected for present public use:** one qualified generic collection-belonging predicate, because its qualifiers must recreate every subject rule and make the first move harder.
- **Retained as a separate possible claim:** constructive parthood, but only when its direct relation obtains and all six `A.1` matters pass.

At comparable correctness and temporal adequacy, the selected answer is no worse than the qualified or separately named alternatives and is cheaper for a cold reader and maintainer. A generic predicate looks cheaper only because it omits decisive conditions. The real cost is that A.14 supplies no immediate cross-domain query key for all belongs-to relations; use `F.18` to name a narrower relation when repeated query, comparison, or declaration use justifies that extra vocabulary.

The rest of the catalogue retains its own governing source lines:

- **Metrical mereology** advances motivate **PortionOf** with explicit μ and Σ-laws, preventing the classic “stuff as components” fallacy.
- **Temporal parts and identity through change** motivate **PhaseOf** as transitive proper temporal parthood, with nesting and overlap allowed, partition-specific coverage and non-overlap, and escalation when identity criteria fail.
- **Engineering product models**, including the ISO 15926 family, pressure authors to keep functional classification, physical product breakdown, and stocks or consumables distinct; A.14 routes those claims to their direct relations instead of one part tree.
- **Knowledge-episteme edition histories** in contemporary MBSE and open-science practice motivate explicit endpoint identities and provenance-preserving composition. FPF uses the C.2.1 identity triple and independently obtaining `EpistemeEditionRelation` for distinct editions; A.14 retains `PhaseOf` only for a proper temporal restriction of one unchanged episteme.

The net effect is a minimal-sufficient catalogue: direct component, constituent, portion, bearer-dependent aspect, phase, and collection-belonging claims stay distinct, while a separately grounded constructive part claim remains possible without another universal relation vocabulary.

Treat this source account as current for this edition. Reopen only the affected A.14 rule if a cited constructional source changes a distinction used here, a newer relation architecture provides the same claim correctness and history at lower reader or maintenance cost, or a direct consumer needs a meaning that the current rule cannot express. Recheck `A.14:5.3` and `CC-ASP-1` through `CC-ASP-4` for an AspectOf change; recheck Solution item 5 and `CC-MEM-1` through `CC-MEM-3` for a collection-belonging or separately grounded parthood change. An ordinary change to a bearer, facet rule, aspect occurrence, collection rule, belonging occurrence, or optional trace reopens only that claim and its support, not this source decision.

### A.14:15 - Relations

- **Builds on:** `A.1`, `A.7`, `B.1`, `B.2`, `C.13`, and `B.3.5` for holon identity, strict distinction, gamma-flavour separation, meta-holon transition, constructive grounding, and Working-Model assurance.
- **Coordinates with:** `C.16` and `A.19` for measured Characteristics; `E.17.0`/`E.17.1` for viewpoints and views; `C.29` and direct projection patterns for representations; `C.27.TA` for temporal claims; and `A.2`, `A.2.1`, `A.3.1`, `A.3.2`, `A.15`, `A.15.1`, and `A.3.4` when wording concerns a local kind, assignment, Method, Work, or transformation rather than parthood.
- **Used by:** architecture, description, evidence, and U-kind admission patterns when their structural claim depends on a clean parthood relation.

### A.14:End

