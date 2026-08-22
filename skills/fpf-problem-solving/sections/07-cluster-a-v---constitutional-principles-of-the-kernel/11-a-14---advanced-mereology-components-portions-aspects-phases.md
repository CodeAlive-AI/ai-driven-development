## A.14 - Advanced Mereology: Components, Portions, Aspects & Phases
> **Type:** Kernel mereology and part-whole relation discipline pattern
> **Status:** Stable

**At a glance.** Use A.14 when a part-whole claim must distinguish component, member, portion, aspect, or phase before downstream architecture, work, assurance, or U-kind admission relies on that claim.

**Use this when.** Use this pattern when a text says that something is part of something else, a collection member, some amount of the same stuff, an aspect of one holon, or the same holon during a time interval, and a wrong relation kind would change identity, aggregation, responsibility, evidence, or structural grounding.

**What goes wrong if missed.** Teams count members as components, portions as components, aspects as separate wholes, or phases as separate objects; constructive traces and Working-Model relation claims then ground the wrong EntityOfConcern.

**What this buys.** One human-facing mereology catalogue that lets B.3.5 and C.13 ground structural claims without inventing a new public relation vocabulary.

**Not this pattern when.** Not this pattern when the current question is only a constructive trace (`C.13`), Working-Model assurance grounding (`B.3.5`), meta-holon transition (`B.2`), temporal dynamics without a phase-of claim, or a general U-kind admission question (`E.24.UK`).

### A.14:1 - Problem frame - why an advanced mereology?

FPF’s holonic modelling relies on **part–whole** relations to build *structural* and *conceptual* holarchies for admitted holons such as systems, epistemes, work occurrences, bounded contexts, disciplines, and methods. But `U.Holon` is **not** a synonym for every bounded object. A local system-role kind is an exact context-local `U.Kind` whose candidates are `U.System` values; it is neither a public root U-kind nor a holon kind by kind identity. `U.Method` is a non-agentive holon kind, but submethod assembly is handled by method-composition patterns, not by A.14 structural component mereology. `SystemRoleKindRelationStructure`, method relation structures, system-role-kind descriptions, method descriptions, work plans, and work occurrences enter A.14 only through their subject patterns and admitted carriers. Early drafts distinguished structural vs. conceptual parthood (e.g., **ComponentOf**, **ConstituentOf**) but practical modelling kept hitting two recurrent gaps:

1. **Quantities vs. parts.** Engineers routinely need “some of the fuel”, “the first 10 pages”, “a 30% subset of data”. This is not a component; it is a **portion** of a stuff‑like whole, governed by measures and conservation.

2. **Change vs. replacement.** “The prototype **before calibration**” may be a proper temporal restriction of one unchanged pump. By contrast, “v2 of the spec” first opens C.2.1 identity and, for two different epistemes, its independent edition-continuity test; “shift 1 vs. shift 2” first opens A.15.1 Work-part or occurrence law. None of those labels selects `PhaseOf` by itself.

This section introduces two **normative** sub‑relations of `partOf` that close those gaps and lock them to the rest of the kernel:

* **PortionOf** — metrical, measure‑preserving parthood of stuffs and other measurables.
* **PhaseOf** — temporal parthood of the *same* carrier across an interval.

It also restates guard-rails that keep local system-role kinds outside holon mereology by kind identity and keep **method values** outside A.14 structural component mereology, while allowing method holarchy through method patterns such as `A.3.1` and `B.1.5`. Describing epistemes such as `U.MethodDescription` and `U.WorkPlan` keep their C.2.1 identity: content or publication-unit inclusion may use ordinary episteme parthood, a proper interval of one unchanged episteme may use `PhaseOf`, and changed C.2.1 identity discriminators identify another episteme whose historical continuation is tested separately through `EpistemeEditionRelation`. It also clarifies how **MemberOf** fits: membership and collection-as-whole grounding start with A.14, C.13, and B.3.5 as appropriate; acting collective systems require `U.System` admission plus system-role assignment, method, work, and evidence patterns; whole reidentification uses B.2 only when existing-whole explanations fail.

**Publication note (Working-Model first).** Read A.14 together with **E.14 Human-Centric Working-Model**. Publish the direct relation claim in the **Working-Model** layer; it remains usable without an assurance profile. Only when the publication elects **B.3.5 CT2R-LOG** or a named current requirement demands that profile does the assertion also link to one current C.2.1 construction-trace episteme in the **Compose-CAL Γ_m** `sum`, `set`, or `slice` form and declare that profile's `validationMode`. The trace reports exact participants, direct relation occurrences, the applicable construction rule, and identity or reidentification conditions. It creates none of them; order and time remain outside mereology.

### A.14:2 - Problem — what breaks without these distinctions?

If we only have “generic partOf” (plus Component/Constituent), four classes of errors appear:

1. **Conservation errors.** Treating “20 L of fuel from Tank A” as a component leads to nonsense: adding and removing such “components” does not respect quantities; Γ\_sys proofs violate Σ‑balance.

2. **Temporal smearing.** Flattening “before/after” for one enduring carrier into a timeless whole collapses history; treating two changed epistemes or two Work occurrences as temporal pieces of that carrier collapses identity and occurrence history. Γ\_time and Γ\_method cannot repair either mistake after the fact.

3. **Identity confusion.** Modelling a “new version” as a component or phase lets a label decide identity. For an episteme, first compare the C.2.1 identity triple and then test edition continuity separately; for another enduring holon, apply its direct identity rule to determine whether the same individual persists or a reidentification question opens.

4. **System-role leakage.** A local system-role kind, assignment, or relation-position label is put into a part tree ("the PumpRole is part of the plant"), making structural reasoning brittle.

### A.14:3 - Forces

| Force                              | Tension                                                                                                         |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Expressiveness vs. Parsimony**   | We need new relations (Portion, Phase) ↔ we must keep the catalogue minimal and orthogonal.                     |
| **Universality vs. Domain nuance** | One set of rules must serve physical systems and epistemes ↔ measurement and time behave differently by domain. |
| **Identity vs. Change**            | Preserve “the same carrier through change” ↔ allow explicit re‑identification when invariants fail.             |
| **Static structure vs. Histories** | Part trees should be simple ↔ real work requires phased histories and measured slices.                          |

### A.14:4 - Solution — extend the mereology catalogue, keep it clean

**A.14 defines two additional sub-relations of `partOf`** and **re-affirms the firewall** between mereology and the system-role-kind and method layers:

1. **PortionOf** — for *measured* parts of a whole (stuffs and other extensives).
2. **PhaseOf** — for *temporal* parts of the same carrier.
3. **No local system-role kinds in holon mereology by kind identity; no method values in structural component mereology.** A local system-role kind is a context-local `U.Kind` for `U.System` candidates, not a holon kind. A system classified by that kind remains a `U.System` and may enter holon mereology on that independent basis. `U.Method` is a method holon, but use method-composition patterns for its submethod assembly, not A.14 `ComponentOf` or structural `partOf`. A `U.MethodDescription` is an **Episteme**: use C.2.1 for its identity and any distinct-edition relation, and A.14 for its content parthood or a proper temporal restriction of the unchanged episteme. `U.Work` parts and occurrence boundaries use A.15.1 relations rather than generic A.14 phasing; neither case replaces method holarchy.
4. **MemberOf stays, but collection identity and acting-collective claims use subject patterns.** `MemberOf` remains available to state exact collection-membership occurrences. After the collection, its identity rule, and those memberships are independently grounded, `Γ_m.set` may narrate their construction account and B.3.5 may link that account when publication assurance is current. Neither the gathering narrative nor its trace creates a membership. An acting collective system uses `U.System` admission plus system-role assignment, method, work, and evidence patterns. Whole reidentification uses B.2 only when existing-whole explanations fail.

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

#### A.14:5.3 - CT2R‑LOG & Compose‑CAL handshake *(normative link)*

* A direct **structural relation claim** is usable without this assurance handshake. When the publication elects B.3.5 or a named current requirement demands it, the published claim **SHALL** link through `tv:groundedBy` to one current C.2.1 construction-trace episteme in the `Γ_m.sum | Γ_m.set | Γ_m.slice` form (see **B.3.5** and **C.13**) and carry the profile's declared `validationMode`. The exact relation predicate, current facts, and occurrence-identity rule determine whether the occurrence obtains and how it is identified; the candidate's direct identity or reidentification rule determines continuity. The trace only reports that basis.
* **PhaseOf** is **temporal parthood**; it **SHALL NOT** be grounded through `Γ_m`. Its assurance follows the same-carrier and proper-interval criteria, the separately declared selected-partition rule when one is claimed, and `Γ_time` ordering (B.1.4).
* **MemberOf** remains **non-mereological** (CC-MEM-2). A `set` trace is truthful only after one exact collection, its identity rule, and the exact direct membership occurrences are grounded; no **ComponentOf** inference follows.

Two quick identity tests apply before relying on a trace. The same listed constituents can form a different whole when their direct assembly relations or rule differ. Conversely, a permitted constituent replacement can preserve the same whole. An equal input list, a repeated trace, or `validationMode=axiomatic` decides neither case.

### A.14:6 - Choosing the right relation (decision table)

| You want to say…                                             | Use                  | Why                                                                                |
| ------------------------------------------------------------ | -------------------- | ---------------------------------------------------------------------------------- |
| “This is a *piece* of the same stuff (lower amount/extent).” | **PortionOf**        | Governed by a measure μ and conservation (Σ‑additive).                             |
| “This is a *discrete part* that sits *inside* the whole.”    | **ComponentOf**      | Structural parthood; boundary‑respecting, not measured by μ.                       |
| “This is a *logical part* in a conceptual whole.”            | **ConstituentOf**    | Sections, lemmas, clauses, conceptual assembly.                                    |
| “This is the *same entity* during a *sub‑interval*.”          | **PhaseOf**          | Temporal slicing with identity continuity.                                         |
| “This *item belongs to that collection/collective*.”         | **MemberOf**         | State the exact membership occurrence and the collection's identity rule. If assurance is current, C.13 may narrate the already grounded collection in a `Γ_m.set` trace and B.3.5 may link it; the gathering account does not create membership or component integration. |
| “This system *plays a Role or position*.” | local system-role-kind classification or `U.SystemRoleAssignment` (`A.2`/`A.2.1`), or a relation position under `A.6.5` | The kind, assignment occurrence, and relation position are not parts. |

> **Firewall reminder.** If the sentence is about system-role-kind classification or assignment, how action is done, or what happened when, use `A.2`/`A.2.1`, `A.3.1`, or `A.15.1` as appropriate. For an episteme, use A.14 for content parthood or a proper interval of one unchanged C.2.1 identity; changed claims, EntityOfConcern, or effective reference scheme identify another episteme, and any historical continuation uses C.2.1 `EpistemeEditionRelation` only when its predicate obtains.

### A.14:7 - Archetypal Grounding

| Relation                       | `U.System` example                                     | `U.Episteme` example                                        |
| ------------------------------ | ------------------------------------------------------ | ----------------------------------------------------------- |
| **PortionOf**                  | 50 L from a 200 L fuel tank (μ = volume).              | Pages 1–10 from a 120‑page report (μ = page/token count).   |
| **ComponentOf**                | Impeller **ComponentOf** PumpUnit.                     | Figure 2 **ComponentOf** Poster Layout (physical poster layout). |
| **ConstituentOf**              | Control law **ConstituentOf** Controller Design.       | Lemma A **ConstituentOf** Theorem Proof.                    |
| **PhaseOf**                    | PumpUnit\#3 *before*/*after* calibration (same serial and direct identity rule). | One unchanged theorem episteme restricted to τ₁ or τ₂ while its complete C.2.1 identity triple remains fixed. |
| MemberOf (for reference) | “is an element of a collection or collective”; use only after the exact collection, its identity rule, and the direct membership occurrence are grounded. A C.13 `Γ_m.set` trace can report that construction and B.3.5 can link it for assurance; neither the trace nor a gathering act creates membership. Acting-collective claims require separate `U.System` admission plus system-role-kind, assignment, method, work, and evidence patterns. | The same rule applies to collections of epistemes; listing or publishing them supplies no membership occurrence by itself. |

### A.14:8 - Bias-Annotation

A.14 corrects parthood bias: ordinary words such as part, member, phase, aspect, section, version, module, function, role, and ingredient can all sound like "part of" while naming different kinds or relations. The repair is not a larger part tree. Recover the EntityOfConcern and decide whether the source means component, constituent, portion, phase, member, classification by a local system-role kind, `U.SystemRoleAssignment`, method description, work occurrence, evidence relation, or transformation relation.

It also corrects representation bias. A BoM row, figure, graph edge, table row, document section, dashboard item, or architecture view may publish a part-whole claim, but the publication form is not the part-whole relation itself. The live A.14 claim is about the relation between holons, epistemes, carriers, portions, phases, or collection members, with mathematical or publication descriptions kept in their own slots.

### A.14:9 - Conformance Checklist - type guards

#### A.14:8.1 - Global firewall and scope

| ID            | Requirement                                                                                 | Purpose                                                 |
| ------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **CC-A14-0** | A local system-role kind **MUST NOT** occur as a node in any `partOf` chain by kind identity; a `U.System` classified by that kind remains eligible for holon mereology on its independent system identity. `U.Method` **MUST NOT** occur in A.14 structural `ComponentOf` or structural `partOf` chains by method identity alone; A.3.1 and B.1.5 define submethod assembly. If an exact admission predicate establishes a different carrier, such as a `SystemRoleKindDescription`, Work occurrence, `U.SystemRoleAssignment` occurrence, `SystemRoleKindRelationStructure`, method relation structure, or episteme, name that carrier, assertion, and subject-pattern locator. | Keeps local system-role kinds out of holon mereology by kind identity and keeps method holarchy out of structural component mereology while preserving admitted carriers. |
| **CC‑A14‑0a** | `U.MethodDescription` / `U.WorkPlan` and other describing epistemes **MAY** participate in `partOf` only as `U.Episteme` nodes: content `ConstituentOf`, measured text `PortionOf`, or `PhaseOf` for a proper interval of one unchanged C.2.1 identity. A changed C.2.1 discriminator identifies another episteme; connect two such identities only through an independently obtaining `EpistemeEditionRelation`. They **MUST NOT** be asserted as `ut:StructPartOf` of any `U.System`. | Allows episteme structure and legitimate temporal restriction without smuggling Methods or automatic edition continuity into structure. |
| **CC‑A14‑0b** | `MemberOf` **MUST NOT** imply, entail, or be auto‑rewritten into any `partOf` sub‑relation. | Separates collections/collectives from parthood.        |
| **CC‑A14‑0c** | `SerialStepOf` / `ParallelFactorOf` **MUST NOT** appear in any `partOf` chain or table in A.14; model order and concurrency potential via **A.15** and direct method-composition patterns such as `B.1.5`. If a node linked by those relations is also a submethod, state that `U.Method` claim separately before using method holarchy. | Prevents the “order‑as‑structure” and “edge-as-part” category errors.       |

#### A.14:8.2 - PortionOf guards

| ID                                 | Requirement                                                                                                                                                               | Purpose                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **CC‑POR‑1 (Domain)**              | `PortionOf(x,y)` is valid only if the modelling scope declares at least one **extensive measure** μ for y (mass, volume, token count, byte size, wall‑time budget, etc.). | Prevents “portion” without a measure.   |
| **CC‑POR‑2 (Kind)**                | x and y **SHALL** share the same μ‑kind and compatible units (or an explicit conversion).                                                                                 | Prevents apples‑to‑oranges addition.    |
| **CC‑POR‑3 (Monotone additivity)** | For disjoint portions `x ⟂ z` with `PortionOf(-,y)`: μ(x ⊔ z) = μ(x)+μ(z).                                                                                                | Secures Σ‑reasoning and Γ\_sys proofs. |
| **CC‑POR‑4 (Boundary)**            | For physical systems, the whole’s boundary encloses the union of portions; cross‑boundary flows are **not** portions.                                                     | Distinguishes stock vs flow.            |
| **CC‑POR‑5 (Non‑replacement)**     | “Replacing 20% of y by v” **MUST** be modelled as **PortionOf** removal + **Component/Constituent** insertion, not as a single PortionOf rewrite.                         | Avoids silent identity change.          |

#### A.14:8.3 - PhaseOf guards

| ID                                    | Requirement                                                                                                                                                      | Purpose                                |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **CC‑PHA‑1 (Proper interval & carrier identity)** | `PhaseOf(x,y)` requires `x ≠ y`, a proper sub-interval of y's interval, and an explicit identity criterion for y valid throughout both restrictions (e.g., serial number, legal identity, theorem statement). | Excludes self/whole-lifetime phasing and prevents re-identification by stealth. |
| **CC‑PHA‑2 (Nesting & overlap)** | Nested or overlapping `PhaseOf` values for one carrier **MAY** obtain. Do not infer a partition, aspect difference, or carrier difference merely from overlap. | Keeps universal temporal parthood consistent and permits ordinary windows. |
| **CC‑PHA‑3 (Selected partition)** | If a claim selects an exhaustive partition, it **MUST** name one carrier, covered interval, aspect or partition rule, and family of phase cells. Only cells of that same selected partition are required to be pairwise non-overlapping and jointly cover the declared interval. | Makes coverage and non-overlap local to the claim that needs them. |
| **CC‑PHA‑4 (Escalation)**             | If identity criteria fail during change, declare a **Meta‑Holon Transition** (B.2) instead of PhaseOf.                                                           | Makes re‑identification explicit.      |
| **CC-PHA-5 (Episteme & Work boundary)** | `PhaseOf` **MAY** restrict one unchanged `U.MethodDescription` episteme to a proper interval only after its C.2.1 identity triple remains fixed. Changed description epistemes use `EpistemeEditionRelation` only when C.2.1's historical-continuation predicate obtains. Work intervals, episodes, performed parts, retries, resumptions, and later occurrences **SHALL** use A.15.1's exact relations; generic `PhaseOf` is not their substitute. `PhaseOf` never applies to a local system-role kind by kind identity or to `U.Method`. | Keeps episteme identity, edition continuity, and Work-temporal law with their subject patterns. |

#### A.14:8.4 - Grounding and validation (normative)

| ID              | Requirement                                                                                                      | Purpose                                           |
| ----------------| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **CC-GND-1**   | A direct `ut:StructPartOf` assertion is usable without this assurance profile. When its publication elects B.3.5 or a named current requirement demands that profile, the assertion **MUST** carry a `tv:groundedBy` link to one current C.2.1 construction-trace episteme in a C.13 `sum`, `set`, or `slice` form and the profile's declared `validationMode`. The trace names independently grounded participants, direct relation occurrences, construction rule, and identity or reidentification conditions. | Makes an elected assurance basis inspectable without making it the relation's truth-maker. |
| **CC-GND-2**   | For **epistemic** edges (`ut:EpiPartOf` and its sub-types), `tv:groundedBy` is **OPTIONAL**; instead supply **`ev:evidence`** and set **`validationMode in {axiomatic, postulate, inferential}`**. | Harmonises evidence treatment for epistemic edges. |
| **CC-GND-3**   | The public query Standard remains `?x ut:PartOf+ ?y`; each returned occurrence still depends on its direct relation semantics and identity. `tv:AliasOf`, a construction trace, or `validationMode` may make the publication inspectable but **MUST NOT** create or reidentify the occurrence. | Preserves the one-query experience without moving relation authority into assurance apparatus. |

*Note.* Property names and trace semantics are defined in the CT2R‑LOG / Compose‑CAL.

#### A.14:8.5 - MemberOf minimal semantics (non‑mereological)

| ID           | Requirement                                                                                       | Purpose                               |
| ------------ | ------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **CC‑MEM‑1** | `MemberOf` domain/range are open: any `U.Holon` may be a member of a collection/collective holon. | Allows mixed collections when needed. |
| **CC‑MEM‑2** | From `MemberOf(x,C)` it is **forbidden** to infer any property of C to x via parthood rules.      | Prevents “set‑as‑whole” errors.       |
| **CC-MEM-3** | Before a collection construction is narrated, one exact collection, its identity rule, and every used `MemberOf` occurrence **MUST** be independently grounded. C.13 may then provide a `Γ_m.set` account and B.3.5 may link it when assurance is current; neither creates membership. Acting-collective claims still require `U.System` admission and separate system-role-kind, assignment, method, work, and evidence patterns. | Keeps collection identity, membership, assurance, and acting-system claims separate. |

#### A.14:8.6 - CT2R‑LOG handshake (Working‑Model → Assurance)

| ID                 | Requirement                                                                                                                                                              | Purpose                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| **CC-A14-10**      | A published structural Working-Model assertion **MAY** remain a direct relation claim without B.3.5 fields. When its publication elects B.3.5 or a named current requirement demands that profile, it **SHALL** declare the profile's `validationMode` and link to one current C.2.1 construction-trace episteme with `tv:groundedBy -> Γ_m.sum\|set\|slice`. The direct relation and reidentification tests remain decisive; the trace and mode create neither occurrence nor identity and guarantee no timelessness. | Keeps direct use lightweight while making an elected assurance posture inspectable. |
| **CC‑A14‑11**      | **PhaseOf** edges **SHALL NOT** use Γ_m for grounding. The relation record **SHALL** provide identity and proper-interval criteria per **CC‑PHA‑1/2**; a selected exhaustive partition additionally follows **CC‑PHA‑3** and references **Γ_time** when ordering matters. | Keeps temporal parthood distinct from construction and partition-specific constraints.       |

### A.14:9.1 - Relation-use decision procedure

**Step 0 — Firewall check.**
If the sentence is about system-role-kind classification or assignment, how action is done, or what happened when, you are **not** in A.14 merely because ordinary speech names a thing. Use `A.2`/`A.2.1`, `A.3.1`, `A.15.1`, or the evidence pattern as appropriate. For an episteme, A.14 may participate in content parthood or a proper temporal restriction of one unchanged C.2.1 identity. Changed episteme content, EntityOfConcern, or effective reference scheme opens another episteme and the separate C.2.1 edition-continuity test; a dated Work part stays under A.15.1.

**Step 1 — Is it measured stuff?**
If yes, pick **PortionOf**. Confirm μ is declared (CC‑POR‑1/2). Test additivity on a toy split (CC‑POR‑3). If flows cross a boundary, remodel as interactions, not portions (CC‑POR‑4).

**Step 2 — Is it a discrete inside part?**
If yes, pick **ComponentOf** (physical) or **ConstituentOf** (conceptual). Do **not** use PortionOf here.

**Step 3 — Is it the same carrier restricted to a proper time slice?**
If yes, pick **PhaseOf**. Verify that the proposed part is not the whole carrier, its interval is a proper sub-interval, and carrier identity holds (CC‑PHA‑1/2). Nested and overlapping restrictions are allowed. Only when the use selects an exhaustive partition must its cells follow the one declared aspect or partition rule, pairwise non-overlap, and coverage condition (CC‑PHA‑3). A whole-lifetime or self-reference needs no phase object. If identity criteria break, escalate to **B.2** (CC‑PHA‑4).

**Step 4 — Is it a membership statement?**
Use **MemberOf** only; avoid any part-inferences (CC-MEM-2). If you need a **collection as a whole**, use **C.13** (`Γ_m.set`) and **B.3.5** when assurance grounding is current. If you need **collective action**, first admit an acting collective `U.System`, then use the system-role-kind, assignment, method, work, and evidence patterns.

**Quick spot-tests.**

| Smell                          | Likely error                      | Fix                                                                                                                          |
| ------------------------------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| “20% of the chassis”           | Treating structure as stuff       | Use **ComponentOf**; if truly laminar material, PortionOf applies to **material stock**, not the assembled chassis.          |
| “Chapter 2 is 15% of the book” | Mixing measures and constituents  | Use **ConstituentOf**; the 15% is **length‑of‑text** as a separate statement.                                                |
| “Spec v2 overlaps v1” | A version label is asked to decide episteme identity and temporal parthood | Compare the exact C.2.1 identity triples. If they differ, identify two epistemes and test `EpistemeEditionRelation` separately; use A.15.1 for overlapping drafting Work. If one unchanged episteme is merely referenced at two times, no second episteme or phase object follows without a proper-interval use. |
| “Team is part of the project”  | Member vs part confusion          | Use **MemberOf(Team, ProjectCollective)**, not partOf.                                                                       |

### A.14:9.2 - Interplay with Γ‑flavours (how these relations behave under aggregation)

| Γ‑flavour                    | Mereological hooks (what A.14 supplies)                                                                                                                | Key effect                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| **Γ\_sys (B.1.2)**          | Treat **PortionOf** as Σ‑additive stocks; **ComponentOf** must respect boundary integration; **PhaseOf** is not aggregated here.                       | Conserves extensive measures and keeps structural WLNK (weakest‑link) on components.          |
| **Γ\_epist (B.1.3)** | **PortionOf** of texts/data uses μ = token/byte count; **ConstituentOf** composes arguments/sections; `PhaseOf` may restrict one unchanged episteme to a proper interval. Distinct MethodDescription or document epistemes use C.2.1 identity and `EpistemeEditionRelation` only when its predicate obtains. | Preserves provenance and avoids both trust inflation and label-based identity or continuity. |
| **Γ\_ctx / Γ\_time (B.1.4)** | **PhaseOf** supplies proper temporal restrictions, including nested or overlapping windows. A separately selected partition supplies non-overlap and coverage only for its own cells. Order/dependencies live in **Γ\_ctx** and method graphs (A.15/B.1.5). **PortionOf** is orthogonal (quantities inside steps/runs). | Ensures chronological consistency without turning every temporal restriction into one partition. |
| **Γ\_method (B.1.5)**          | Γ\_method composes Methods rather than A.14 structural parts. A recipe-labelled claim-bearing episteme is a **MethodDescription** only when its exact `EntityOfConcern` is one admitted `U.Method` and at least one substantive way-of-doing claim obtains under A.3.2; any graph form is a C.29-governed representation, not membership evidence. When a recipe refers to stuff‑like inputs, those are **PortionOf** statements on resources. | Separates recipe composition from structure.                                                  |
| **Γ\_work (B.1.6)**          | Only **Work** carries resource deltas; when logging “consumed 5 kg from Tank A”, model it as **PortionOf** relation to the stock prior to consumption. | Makes Σ‑balance explicit; aligns with CC‑POR‑3/4.                                             |

### A.14:10 - Common Anti-Patterns and How to Avoid Them

* **Member as component.** A person, team, document, or object belongs to a collection and is then counted as if it were structurally integrated into the whole.
* **Role expression as part.** A system is said to "play a role", and the label is placed inside a part tree instead of being resolved as a local system-role kind, a `U.SystemRoleAssignment`, or a relation position.
* **Method as part.** A method value, recipe, or algorithm is treated as a component instead of using method, method-description, work, or transformation patterns.
* **Portion without measure.** Some amount of fuel, data, time, or text is named as a portion without a measure kind, unit, and additivity condition.
* **Phase as replacement or lineage.** A proper restriction of one enduring carrier is treated as another component, or a changed episteme, version label, or Work segment is treated as `PhaseOf` without applying C.2.1 or A.15.1 first.
* **Diagram or trace as relation.** A visual breakdown, graph, table, construction trace, or `validationMode` is used as proof that parthood obtains or that the whole has one fixed identity. Recover the direct relation occurrence and the candidate's identity or reidentification rule first; use the publication and trace only as inspectable accounts.

### A.14:11 - Pedagogy aids (non-normative)

**Two‑minute checklist for practitioners**

1. Do I see "process", "procedure", "policy", or "script" used to mean enactment? — then **A.15/A.15.1**. If it names an episteme, use A.14 only for its content parthood or a proper interval of the unchanged C.2.1 identity; use C.2.1 for another episteme and any edition-continuity claim.
2. Does every PortionOf have a declared μ and unit?
3. Is this an ordinary proper temporal restriction, where nesting or overlap is allowed, or one explicitly selected exhaustive partition, whose cells alone must not overlap and must cover the declared interval?
4. Are any roles/recipes appearing as parts? If yes, stop and refactor.

### A.14:12 - Consequences

**Benefits**

* **Predictable composition.** Σ‑additivity for portions, same-carrier temporal parthood, and explicit partition rules make Γ‑proofs inspectable.
* **History without confusion.** Temporal slicing is explicit; nested and overlapping windows remain legal, while non-overlap and coverage are claimed only for a selected partition.
* **Cleaner integration with roles and recipes.** The firewall prevents “functional object” creep into structure.
* **Compatibility with engineering practice.** Mirrors *product breakdown* (components) vs *functional breakdown* (roles) vs *material stocks* (portions) vs proper temporal restrictions of one enduring carrier (phases), while leaving episteme editions and Work segmentation to their subject patterns.

**Trade‑offs / mitigations**

* **Modelling energy.** Authors must pick μ and declare units; provide a short μ‑catalog per project.
* **More relation names.** Two extra sub‑relations increase vocabulary; mitigated by the decision table (§ 6) and spot‑tests (§ 9).
* **Escalation discipline.** Deciding PhaseOf vs MHT requires judgement; A.14 provides criteria, and B.2 captures true re‑identification.

### A.14:13 - Rationale

A.14 exists because part-whole words carry identity, aggregation, measure, time, and assurance commitments. The pattern keeps those commitments in the relation kind instead of letting everyday nouns, diagrams, or breakdown tables decide ontology. Component, constituent, portion, phase, and member claims can then support holon, episteme, architecture, and evidence work without smuggling system-role-kind classification or assignment, method, work, or publication claims into mereology.

### A.14:14 - SoTA-Echoing

* **Metrical mereology** advances (e.g., recent work on quantity‑based parthood and additivity) motivate **PortionOf** with explicit μ and Σ‑laws, preventing the classic “stuff as components” fallacy.
* **Temporal parts & identity through change** (renewed treatments in analytic metaphysics and formal ontology) motivate **PhaseOf** as transitive proper temporal parthood, with nesting and overlap allowed, partition-specific coverage/non-overlap, and escalation when identity criteria fail.
* **Engineering ontologies (BORO lineage, Core Constructional practice, ISO 15926 family)** keep a strict separation between **functional breakdowns** (our Roles) and **product breakdowns** (our Components), with **stock/consumable** modelling (our Portions) handled by quantities, not by component trees.
* **Knowledge-episteme edition histories** in contemporary MBSE and open-science practice motivate explicit endpoint identities and provenance-preserving composition. FPF uses the C.2.1 identity triple and independently obtaining `EpistemeEditionRelation` for distinct editions; A.14 retains `PhaseOf` only for a proper temporal restriction of one unchanged episteme.
* The net effect is a **minimal‑sufficient** catalogue: two added sub‑relations close real modelling gaps while preserving **parsimony**, **didactic clarity**, and **Γ‑compatibility** across domains.

### A.14:15 - Relations

- **Builds on:** `A.1`, `A.7`, `B.1`, `B.2`, `C.13`, and `B.3.5` for holon identity, strict distinction, gamma-flavour separation, meta-holon transition, constructive grounding, and Working-Model assurance.
- **Coordinates with:** `A.2`, `A.2.1`, `A.15`, `A.15.1`, `A.3.1`, `A.3.2`, and `A.3.4` when the source wording is about a system-role kind or assignment, method, work, or transformation rather than parthood.
- **Used by:** architecture, description, evidence, and U-kind admission patterns when their structural claim depends on a clean parthood relation.

### A.14:End

