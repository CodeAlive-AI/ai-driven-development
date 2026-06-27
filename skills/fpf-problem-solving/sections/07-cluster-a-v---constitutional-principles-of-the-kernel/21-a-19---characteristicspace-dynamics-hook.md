## A.19 - CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)

> **Type:** Kernel characteristic-space and dynamics-typing pattern
> **Status:** Stable

**Use this when.** Use this pattern when the current object is the declared `CharacteristicSpace` itself: characteristics, scales, value sets, coordinate slots, optional overlays, comparability boundaries, normalization boundaries, missingness, and the `U.Dynamics.stateSpace` hook.

**What goes wrong if missed.** Teams compare raw numbers from different scales, treat dashboards or scores as the space, hide thresholds inside state labels, smuggle method sequences into checklists, or give consumer patterns their own private space kinds.

**What this buys.** One declared space that makes state, threshold, comparability, normalization, and dynamics-typing claims inspectable without turning A.19 into a scoring, dashboard, evidence, gate, or evaluation pattern.

### A.19:0 - Problem frame - First use: `U.CharacteristicSpace` as the EoC (normative primer)

Use `A.19` when the current question is the space of characteristics itself: which characteristics are in scope, which scale is bound to each characteristic, what values are admissible, how coordinates are grouped, which optional order, topology, or metric overlays are declared, and where comparability, normalization, missingness, and evidence hooks belong.

First move: name the `CharacteristicSpace`, then write its basis as slot declarations. Each slot binds one `U.Characteristic` to one scale and value set under `A.17` and `A.18`; optional overlays and comparability boundaries attach to the space only when declared. `U.Dynamics.stateSpace` points to a declared `CharacteristicSpace`; A.19 does not supply the dynamic law, time base, evaluation use, dashboard, score, or portfolio that consumes the space.

Core boundary: the `CharacteristicSpace` is the EoC here. Consumer patterns may refer to it through `...SpaceRef` fields, use it for evaluation or CHR mechanisms, or publish views over it, but those consumer references, mechanism steps, publication forms, and source-set relations are not second space kinds.

Informative CHR pointer: when the question moves from the space to normalization, indicatorization, scoring, aggregation, comparison, or selection mechanisms, use the corresponding `A.19.<MechId>` pattern (`A.19.UNM`, `A.19.UINDM`, `A.19.USCM`, `A.19.ULSAM`, `A.19.CPM`, `A.19.SelectorMechanism`) and `A.19.CHR`. `C.16` carries measurement and evidence backing; `G.0` carries admissibility gates for numeric operations. A.19 may cite those patterns, but it does not govern their mechanism vocabulary.

Reader orientation sequence for a CHR-enabled plan or audit, when orientation is needed:

- measurement vocabulary: use `A.17`, `A.18`, and `C.16` for characteristic, scale, coordinate, unit, measure, and evidence backing;
- characteristic-space object: use this pattern for the declared `CharacteristicSpace`, basis slots, optional overlays, comparability boundaries, missingness, and `U.Dynamics.stateSpace` hook;
- admissibility of numeric operations: use `G.0` and the relevant `A.19.<MechId>` mechanism pattern; do not let A.19 become a second mechanism vocabulary;
- suite and planning boundary: use `A.19.CHR`, `A.15.3`, and `E.18` when a planned baseline, suite slot filling, or transformation-flow structure is current;
- one mechanism at a time: read `A.19.UNM`, `A.19.UINDM`, `A.19.USCM`, `A.19.ULSAM`, `A.19.CPM`, or `A.19.SelectorMechanism` only for the mechanism claim being made;
- specialization and reuse: use `E.20` when a project-specific mechanism variant is introduced.

Fast review entries: for a plan, start from the `A.19.CHR` planned-baseline hook and `A.15.3`; for semantic drift, start from the canonical mechanism target and then use `E.10` and `F.18`; for conformance, start from the `A.19.CHR` and relevant `A.19.<MechId>` checklists, then use `E.19` for review protocol.

### A.19:1 - Intent & Scope (Normative)

**Intent.** Establish `U.CharacteristicSpace` as the A.19 ontic head: a declared space of characteristics, scales, value sets, value meanings, coordinate positions, coordinate groups, optional overlays, missingness semantics, comparability boundaries, normalization boundaries, and evidence hooks where those hooks are part of the space declaration. For dynamics, `U.Dynamics.stateSpace` points to such a space so a holon's state changes can be described as trajectories in declared coordinates. For epistemes, state remains governed by ESG; F-G-R are assurance coordinates, not an episteme state space.

**E.24.UK settlement.** `U.CharacteristicSpace` is retained as the root durable value for a declared multi-characteristic space. Its slots bind `U.Characteristic` values to scale/value-set declarations under A.17 and A.18; optional overlays, topology, metric or distance structures, normalization boundaries, comparability boundaries, and missingness semantics are dependent declarations over the space, not separate U-kinds by label. C.16 measurement values may cite the space, but a score table, dashboard, evaluation result, or dynamics law is not the characteristic space.

The A.19 EoC is the characteristic space itself. It is not the filled evaluation, report, score table, dashboard, pattern-quality scale, DRR adequacy scale, FPF-level pillar scale, or improvement portfolio that uses the space.


**Scope.** Pattern A.19 **defines**:

-   the declared `U.CharacteristicSpace` value as a finite product of **slot value sets** (per A.18),
-   the **slot** construct for each factor (a pairing of a **Characteristic** with a chosen **Scale**),

-   minimal **structural overlays** (optional **order**, **topology**, **metric** hooks) that downstream patterns _may_ attach to a space, and

-   the **hook** `U.Dynamics.stateSpace : CharacteristicSpace` – i.e. the requirement that any dynamics model declare a CharacteristicSpace for its state space (typing only).

A.19 **does not** introduce any new measurement aspects, composite metrics, or **normalization semantics** (governed by **A.19.UNM**, with evidence and calibration under **C.16 (MM‑CHR)**), and it does not define how dynamics evolve over time or any predictive laws (see **A.3.3** for dynamics semantics). The focus here is purely on the _structure of state spaces_ and their comparability.

**Space-vs-consumer boundary.** Use A.19 to declare the `CharacteristicSpace` itself: characteristic slots, scale bindings, value sets, value meanings, coordinate groups, optional order, topology, metric, or product overlays, comparability boundaries, normalization boundaries, missingness semantics, and the `U.Dynamics.stateSpace` typing hook. Do not use A.19 to declare consumer-side reference positions that merely point to a declared space, and do not use it to declare relation kinds between several such references.

Accordingly, one field such as `...SpaceRef` is a reference to a declared `CharacteristicSpace`, not a second space kind, not a slot alias inside that space, and not a role claim. If a consumer pattern needs search-side versus outcome-side positions over declared spaces, an explicit relation between those references, a source-set relation, or an interpretive view over an already declared substrate-bearing line, source set, or set result, declare that in the consumer pattern or consumer declaration that uses the space rather than in A.19 itself.

`A.19.ECS` constructs an evaluation `CharacteristicSpace` for an object kind under improvement. `E.21`, `E.9.DA`, `E.2.DA`, and other evaluation patterns consume or specialize declared spaces for their own evaluated objects. A.19 supplies the space ontology; those patterns supply object-specific evaluation use, stop conditions, and value interpretation for their users.


**Lexical guard (“map”).** Follow the normalization lexical discipline governed by **A.19.UNM**. In this pattern, lowercase **map** is used only in the mathematical sense, while capitalized **Map** retains its Part‑G suffix meaning (e.g., `DescriptorMap`). Do not mint new normalization terminology here.

**Lexical guard for value sets.** In A.19, the set that supplies values to a slot is `ValueSet(slot)` or an underlying value set. Do not call that value set a publication form, symbol bearer, source, description, or persistence object.

### A.19:2 - Context (Informative)

FPF’s kernel already standardizes **what** is measured (a **Characteristic**, per A.17) and **how** it is measured (a **Scale** with units, via the **CSLC** Standard in A.18). We also have a measurement substrate (`U.DHCMethodRef`, `U.Measure`) to handle individual observations. What has been missing for modeling **dynamics** is a canonical “Context” in which **multiple Characteristics** can co-exist so that complex **states** (with many aspects) and their **trajectories** are well-typed and comparable. Without a formal CharacteristicSpace, teams either hard-code ad-hoc vectors (often with inconsistent assumptions) or fall back to informal lifecycle stories (“phases” or stages) that contradict the kernel’s open-ended, non-linear evolution paradigm. The Architectural patterns (A-cluster) expect that `U.Dynamics.stateSpace` will be a set of **declared Characteristics each with a declared Scale**. Pattern A.19 delivers exactly this capability, leveraging the CSLC measurement discipline without reinventing any arithmetic or unit-handling logic.

### A.19:3 - Problem (Informative)

-   **P1 — “Feature vector” drift.** In practice, teams often assemble state vectors or “feature” lists with implicit or mismatched units and scales. Without a formal space, one coordinate’s value can’t safely be compared or combined with another’s (e.g. mixing degrees Celsius with percentages). **CSLC** guarantees consistency **per Characteristic**, but a bundle of multiple “characteristics” remains under-specified if we lack a unified space definition.

-   **P2 — Lifecycle bias.** Absent a formal state space, system change tends to be described in terms of fixed **stages or phases** (design phases, maturity levels, etc.). This conflicts with FPF’s **open-ended** stance: in FPF a role-state relation (`RoleStateRelation@BoundedContext`, A.2.5) allows re-entry and refinement of states rather than one-way lifecycle stages with an “end.” We need a space model that treats evolution as continuous movement, not a one-directional sequence.

-   **P3 — Incoherence across CN‑frames.** Different modeling “CN‑frames” (architecture vs. epistemic vs. operational) often choose different sets of qualities to measure (different sets of characteristics). In composition or projection work, teams need to **compose** these models or **project** one into another. Without a kernel notion of how one state space can be a **subspace** of or **embedded** in another, any integration of models will be ad hoc and error-prone.

-   **P4 — Relational measurements.** Some Characteristics are inherently **relational** (e.g. a _Coupling_ between two components, or _Distance_ between points). Naïvely forcing such traits into a single-object feature vector loses critical information (arity, symmetry). The kernel already distinguishes single-entity vs multi-entity Characteristics (A.17); we must preserve that distinction in the state space so that a relational metric isn’t treated as an intrinsic one by mistake.

-   **P5 — The geometry temptation.** When defining a state space, it’s tempting to assume or inject additional structure (ordering of states, topologies for continuity, metrics for distance) as if inherent. But the kernel must remain minimal and domain-neutral: it should not **smuggle in** analysis methods or domain-specific norms under the guise of geometry. Any such structure should be added explicitly by specialized patterns, not baked into the core definition of a space.

### A.19:4 - Forces (Informative)

-   **F1 – CSLC integrity at scale.** When combining multiple measurements into a state, we must uphold the **CSLC discipline** for each component: each coordinate has a defined Characteristic, Scale type, unit, and (if applicable) polarity. We need to do this without redefining or duplicating that single-characteristic integrity – the multi-dimensional space should simply enforce CSLC per slot.

-   **F2 – Transdisciplinarity & lexical clarity.** The state space framework must work for **quantitative physical metrics** (ratio scales, continuous units), **qualitative assessments** (ordinal scales, tiers), and mixtures thereof. It must not be biased toward one domain’s notion of measurement. At the same time, to avoid confusion, the **lexicon must remain canonical**: we use _Characteristic_ (not “axis” or “dimension”) as the formal term for a measured aspect, regardless of domain, per A.17’s naming convention.

-   **F3 – Arity and semantics.** Lifting various Characteristics into a unified space should not obscure their nature. If a Characteristic is defined as a relation (multi-entity property), the state space must represent it appropriately (e.g. as a coordinate that is a tuple or a symmetric relation) rather than flattening it into an unrelated scalar. Entity-specific vs relational properties must remain clear in the space’s structure.

-   **F4 – Minimal core, extensible further.** The kernel should provide only the **bare essentials**: a typed state-space structure with declared Characteristics, Scales, ValueSets, and slot-value constraints. It should be possible to impose additional structure like order, topology, or metrics _if and when needed_ by downstream theories, but these must be **optional overlays**. The core space definition should be minimalistic to allow broad use, yet capable of extension for advanced needs.

-   **F5 – Composability of spaces.** We need well-defined operations to **project** a state space to a subspace (dropping some Characteristics), **embed** one space into a larger space (mapping coordinates from one context to another), and take **products** of spaces (combining different state spaces into a joint space). These operations are crucial for composing sub-models, comparing alternatives, or aligning different “CN‑frames” (for example, linking an architectural model’s state space with a metrics model’s space). The approach must allow such composition in a principled way.

-   **F6 - Alignment with role-state relations.** In FPF, formal **state certification** is done via checklists in `RoleStateRelation@BoundedContext` (A.2.5). Our state space concept must complement that: the **state** of a holon remains a criteria-defined state label, but those criteria are evaluated against the measurable **coordinates** in a CharacteristicSpace. The design must allow checklists to map observed coordinates to named states and enable re-certification as states evolve, rather than locking states into a static progression.

### A.19:5 - Solution

#### A.19:5.1 - `U.CharacteristicSpace`

##### A.19:5.1.1 - Type signature

Let **I** be a finite index set labeling a collection of **slots**. Each **slot** _i_ (for _i ∈ I_) is defined as a pair:

> **`slot_i = (Characteristic_i, Scale_i)`**,

where:

-   `Characteristic_i` is a `U.Characteristic` (with an explicit arity, i.e. either an entity-Characteristic or a relation-Characteristic as defined in A.17), and

-   `Scale_i` is a chosen **Scale** for that Characteristic (with a specified scale type and unit, per A.18 and the MM‑CHR rules).

Then a **CharacteristicSpace** (CS) is formally the Cartesian product of all slot **value sets**:

$\mathbf{CS} = \prod_{i \in I} \mathrm{ValueSet}(\mathrm{slot}_i)\,.$

In other words, a point (state) in the space consists of one coordinate value for each slot. A **state** _x_ in CS can be seen as a total function _x(i)_ that picks a value from each slot’s **ValueSet** (for every _i ∈ I_, _x(i) ∈ ValueSet(slot\_i)_). By kernel mandate, any `U.Dynamics.stateSpace` **SHALL** be bound to some instance of `CharacteristicSpace`, and all states or trajectories described by that dynamics model **MUST** lie within that space’s **value set**. (The actual dynamic **laws** and time progression are handled in A.3.3; A.19 only defines the state‑space container and its properties.)

##### A.19:5.1.2 - Slot discipline (invariants)

To ensure consistency and comparability, a CharacteristicSpace must obey the following invariants:

-   **A19-CS-1 (Exactly one per slot).** Each slot **binds exactly one** Characteristic to **exactly one** Scale (including a specific Unit or kind, if applicable). This mirrors the CSLC clause of “one aspect – one scale”: there are no ambiguous or compound mappings in a single slot. (If a Characteristic can be measured on multiple scales, only one is chosen for a given space; others would require separate slots or a different space.)

-   **A19-CS-2 (Named basis).** A CharacteristicSpace **SHALL** publish an ordered list of its slots as its **basis**. Each slot in the basis has a stable identifier that can be used in technical notations or data structures. These basis names should be treated as stable technical tokens (identifier-like); any human-friendly alias or description for a slot should be provided only in the Plain register as a non-normative aid (per E.10). In short, the identity and order of slots in the space are explicit and stable.

-   **A19-CS-3 (Immutability of meaning).** Once a space is in use, the meaning of each slot is fixed. A slot’s `(Characteristic, Scale)` pair **MUST NOT** be retroactively altered. If requirements change (e.g. a different scale or a revised definition of the Characteristic), one **MUST** define a new version of the space (or a new slot) rather than silently changing the existing one. When a space is versioned or a slot replaced, an explicit **embedding** (mapping from the old space to the new space) should be published to relate historical states to the new coordinates. This ensures past data remains interpretable and prevents semantic drift.

-   **A19-CS-4 (Arity preservation).** If a `Characteristic_i` is defined as a **relation** (multi-entity characteristic), then slot _i_ represents a relationship among multiple entities. The coordinate value at such a slot is a **tuple** (with the appropriate entity types) rather than a simple scalar. The slot’s declaration **SHALL** indicate the relation’s symmetry or directionality as part of its meaning (this should align with how the Characteristic was originally defined in its template). In essence, relational Characteristics retain their arity in the space, so that we don’t confuse, say, “Coupling between X and Y” with an intrinsic property of X or Y alone.

 -  **A19-CS-5 (No hidden normalizations or aggregations).** A CharacteristicSpace itself carries **no implicit normalizations or formulas** for combining coordinates. It is a _descriptive_ structure, not a scoring mechanism. Any computation that combines or transforms coordinates (e.g., **normalizing**, **indicatorizing**, **scoring**, **Γ‑folding**, **comparing**, or **selecting**) must be defined outside the core space—typically as an explicit **CHR mechanism step** and cited from its designated mechanism-governing pattern (`A.19.UNM`, `A.19.UINDM`, `A.19.USCM`, `A.19.ULSAM`, `A.19.CPM`, `A.19.SelectorMechanism`).
   *Normalization semantics and admissibility* are governed by **A.19.UNM**; *evidence and calibration backing* is governed by **C.16 (MM‑CHR)**.
   In particular, any handling of **polarity** (which way “better” is), weighting, or cross-slot aggregation happens in those external mechanisms and policies, not inside the space definition. The space provides the raw coordinates; the logic to interpret or aggregate them is added by domain-specific layers with explicit disclosure of how it is done.

 - **A19-CS-6 (Slot meta completeness).** Where applicable, each slot **SHALL** declare `admissible_domain` and **missingness semantics** (e.g., codes for *missing*, *censored*, *not-applicable*), consistent with the Characteristic’s Scale and with MM‑CHR. This prevents silent domain drift and clarifies how absent values participate in predicates and comparisons.

 - **A19-CS-7 (Space-vs-consumer boundary).** A `CharacteristicSpace` publishes only its own slot basis, optional overlays, and typing hooks. Ref-typed consumer fields that point to a declared space, explicit relation kinds between such refs, source-set wiring, interpretive-view organization, and publication metadata are **outside** the space object and **MUST** be declared in the consumer pattern or consumer declaration that uses the space. This prevents `CharacteristicSpace` from being silently widened into ref-position semantics, selector semantics, source-set semantics, publication-form semantics, or interpretive-view semantics.

##### A.19:5.1.3 - Minimal structure hooks (optional overlays)

By default, a CharacteristicSpace has no assumed ordering or metric structure – it is just a Cartesian product of value sets. However, a space **MAY** declare certain structural attributes _as opt-in metadata_ (i.e. informative annotations that patterns can rely on, but not enforced by the kernel). These optional **overlays** include:

-   **Product topology.** A **topology** on the space, typically the product topology when slots that are quantitative (interval or ratio scales) need continuity considerations. Declaring a topology is useful if continuity or convergence arguments are relevant (e.g. to say a sequence of states approaches a limit state). By default, without declaration, no topological structure is assumed on the space.

_Lexical note:_ Here **“distance metric”** strictly means a mathematical distance function (or a generalized distance such as a **pseudometric** or **quasi-metric**) on the state space. This is **not** to be confused with *metrics* as performance measures in MM-CHR. In the **Tech** register, avoid the noun **metric**; refer to **`U.DHCMethod` or `U.DHCMethodRef`** for measurement templates (see **C.16**). Any distance overlay on a CharacteristicSpace must not conflict with scale semantics; it is an additional analysis structure, not a redefinition of measurement meaning.

These overlays are entirely **optional** and have no effect on the core meaning of the space - they exist only to enable particular reasoning such as **dominance**, **continuity**, or **distance** reasoning in models that require it. If needed, they should be added deliberately by an architectural theory rather than assumed. This way, any ordering or metric properties of states are made **explicit** instead of relying on hidden or default arithmetic. _(Rationale:_ The CSLC and MM‑CHR rules already govern what operations are allowed on each scale; A.19’s approach is to let neighboring theories add an order, topology, or metric when appropriate, so nothing is taken for granted tacitly in multi-dimensional arithmetic._)_

##### A.19:5.1.4 - Dynamics hook (typing only)

Any model of change or dynamics in FPF must declare the state space it operates over. Formally, `U.Dynamics.stateSpace` **SHALL** be specified as a reference to a `CharacteristicSpace`. This creates a typing requirement: the dynamic model can only produce states and trajectories of states that belong to the given space. All predicates or predictions in such a dynamics model are understood to **quantify over** sequences of points in that CharacteristicSpace (with time semantics governed by A.3.3’s time base and laws). **Note:** A.19 defines only the structure of the state space; it deliberately **does not** fix any time base or dynamic law. Those remain the responsibility of the dynamics pattern (A.3.3). A.19 simply ensures there is a well-defined space in which states are located, so that dynamics are decoupled from any narrative “stage” and instead treat evolution as movement through this space.

##### A.19:5.1.5 - Lexical discipline (Normative)

In all **normative references, definitions, and identifiers** related to this pattern, the specification uses the canonical measurement terminology: **Characteristic**, **Scale**, **Level**, **Coordinate**, **CharacteristicSpace**, **slot**, **basis**. Legacy terms like “axis”, “dimension”, or “point” are **forbidden** in Technical and Formal registers of the spec (per A.17’s lexical rules). They may appear _at most once_ in explanatory **Plain** language as mapped aliases to aid understanding (and if used, must be explicitly identified as equivalent to the official terms). In this pattern, we consistently use “slot” or “basis element” (never “axis”) to refer to a component of a space, and “Characteristic” (never “dimension”) to refer to the measured aspect. This lexical discipline ensures clarity and consistency across the framework (see A.17 and C.16 L-rules for the formal policy on terminology).

##### A.19:5.1.6 - Quotients & NormalizationFix (Normative)

**Governing-pattern note.** `≡_UNM` and `NormalizationFix` are defined in **A.19.UNM**. This section constrains only how they are **cited** when used in state‑space reasoning.

**Design rule — read invariants, not labels.** Any checklist, acceptance predicate, equality check, join, or comparability claim over a `CharacteristicSpace` that depends on representation choice (chart, unit, reference plane, normalization choice, or label) **SHALL** be evaluated on **quotients by ≡_UNM** or on explicitly **Normalization‑fixed** charts, not on raw labels.
*Minimal obligations:*
1) **Name the quotient or fix.** If a checklist predicates over a **normalization‑variant** property, it **MUST** name the **NormalizationFix** (including the referenced **UNM** and the relevant `NormalizationMethodInstance`(s), by reference) and thus the **≡_UNM** class.
2) **Declare NormalizationMethod class.** Every normalization used **MUST** name its method‑class token and validity window **as defined in A.19.UNM** (do not restate the class taxonomy here).
3) **Join and equality only on invariants.** Equality checks and joins across spaces **MUST** target invariant forms (the **≡_UNM** quotient or a declared **Normalization-fixed** representation), never raw un-fixed coordinates.

##### A.19:5.1.7 - Metric discipline & calibration (Normative)

Use the **weakest safe structure** required by the argument (pre‑order → semi‑metric → metric).
* **If a distance overlay is declared**, any acceptance predicate or KPI defined over a CharacteristicSpace **SHALL be non‑expansive** (Lipschitz ≤ 1) w.r.t. the published `d` on the **declared domain** (raw coordinates or NCVs, as specified), or else state an explicit margin that absorbs any expansion.
* **If only an order overlay is declared**, any acceptance predicate or KPI **SHALL be isotone** w.r.t. the declared product order.

*Minimal obligations:*
1) **Publish the metric (if used).** If a distance overlay is used, the space **MUST** publish the distance function `d` (including any weights and parameters) and its declared domain of applicability.
2) **Bound expansion.** Any acceptance predicate or KPI that relies on `d` **MUST** be shown **non-expansive** (Lipschitz ≤ 1); otherwise an explicit **expansion bound** and compensating **margin** **MUST** be stated.
3) **State error and commutation.** If a metric is used together with **NormalizationFix**, the specification **MUST** state (a) the maximum tolerated measurement and calibration error and (b) whether `d` **commutes** with the **NormalizationFix** (or provide a disclaimer and additional guard if it does not).

#### A.19:5.2 - State Spaces & Comparability

> **Memory hook:** _We compare **only what lies in the same space** (or is translated into a common space via a declared mapping), and we only certify a holon’s **state** based on **observable coordinates** in that space (using a defined checklist). Anything else is just storytelling._

To make state-space reasoning practical across different contexts and models, this section provides the key **operators and criteria** related to CharacteristicSpaces:

1.  **Space operations** – how to derive a **Subspace**, establish an **Embedding**, or form a **Product** of spaces. These enable us to restrict a space to fewer slots, to map one space into another (with unit conversions, etc.), or to combine spaces (e.g. for composite models).

2.  **Comparability regimes** – two allowable ways to compare states: (a) **coordinatewise**, which requires strict sameness of space and units; or (b) **normalization-based**, which uses declared transformations to reconcile differences. We define when each applies and how to apply it properly.

3.  **Role-state-relation integration** – how formal **state certification** (via checklists in `RoleStateRelation@BoundedContext`) ties into the CharacteristicSpace: ensuring that whenever we declare a system “Ready” or “Degraded”, it’s based on snapshot coordinates in a space. We also outline how to push or pull state definitions along space embeddings (so different contexts can translate states).

4.  **Archetypal examples** – “worked mini-schemas” illustrating typical usage in complementary CN‑frames (Operational, Assurance, Alignment). These examples show minimal models mixing entity and relational slots, how data might be structured, and how cross-context alignment works in practice.

> **Terminology note:** We often denote a CharacteristicSpace abstractly as **CS**. Formally, one can describe a CS as a tuple `⟨I, basis⟩` where _I_ is the index set of slots and _basis_ is the set (or ordered list) of `slot_i` pairs. When a CharacteristicSpace is attached to a specific **Role** in a specific **Context** (see A.2, A.2.5), call it a **RoleCharacteristicSpace**: the state space used by that role-state relation within that bounded context. Individual **states** of a role belong to `RoleStateRelation@BoundedContext`, and a **StateAssertion** is a certified claim that at a given time window, the holon’s RoleCharacteristicSpace coordinates satisfy the checklist for a particular state.

##### A.19:5.2.1 - CS Operators (notation-neutral, context-local)

To enable model composition, we define operations on CharacteristicSpaces in a notation-independent way (so these can be implemented in any tooling or notation). All these operations are assumed to occur **within a single context** (within one `U.BoundedContext`) unless otherwise noted:

###### A.19:5.2.1.1 - Subspace – **Projection** `π_S : CS → CS|_S`.
Given a CharacteristicSpace CS with basis _I_ (slots) and a chosen subset of slot indices $S \subseteq I$, one can form the **subspace** $CS|_S$ which includes only the slots in _S_ and omits all others. The projection map `π_S` takes any state _x_ in the original space and **projects** it onto the coordinates indexed by _S_, effectively discarding the other coordinates. This operation is straightforward: if $S = \{i_1, i_2, … \}$, then $CS|_S$ has those slots, and any state in $CS|_S$ corresponds to a state in CS with the other coordinates ignored.
**Properties:** Projection is **idempotent** (`π_S ∘ π_S = π_S`) and, if an order or other structure is defined solely on the subspace’s slots, `π_S` preserves that structure (e.g. it will reflect any order that depends only on slots in _S_).

###### A.19:5.2.1.2 Embedding – **Injection** `ι : CS₁ ↪ CS₂`.
An **embedding** is a structure-preserving **injection** from one space CS₁ into another space CS₂. It consists of two parts: (a) an injective **slot correspondence** from CS₁ to CS₂, and (b) (only where needed) cited **normalization instances** that make the correspondence semantically safe. Formally, let CS₁ have basis _I₁_ and CS₂ have _I₂_. An embedding declares an injective function _m: I₁ → I₂_ that identifies each slot of CS₁ with a corresponding slot in CS₂.

For each slot _i ∈ I₁_ where the scale or unit differs from the target slot _m(i)_ in CS₂, the embedding **MUST cite** a `NormalizationMethodInstanceId` (per **A.19.UNM**) that re-expresses values from `ValueSet(slot_i)` into `ValueSet(slot_{m(i)})` within the declared invariants and validity window. The embedding does **not** define normalization semantics; it only references the required instances.

Intuitively, an embedding says: “Any coordinate tuple from CS₁ can be interpreted as a coordinate tuple in CS₂, possibly after converting units or re‑scaling, and without losing any information except what the declared **NormalizationMethods** intentionally **coarse‑grain**.” If there is no loss at all (**NormalizationMethods** are identity or strict conversions), the embedding is essentially an inclusion of one space into a larger one; if there is some information loss (e.g., converting a fine‑grained scale to a coarse one), that loss is explicit in the **NormalizationMethodDescription**. **Locality:**

Embeddings are defined **within a single `U.BoundedContext`** (i.e., both CS₁ and CS₂ are in the same context). Using an embedding across contexts requires an **Alignment Bridge** (see F.9) and **MUST** be declared via the relevant mechanism’s **A.6.1 Transport** clause (BridgeId + channel + `ReferencePlane(src,tgt)` + any `CL^plane`; no implicit crossings).

**Normalization declaration duties (MUST):** Each cited `NormalizationMethodInstanceId` **MUST** satisfy the declaration and admissibility obligations governed by **A.19.UNM** (including method-class token and validity window). If such normalization method instances or declarations are used for gating or assurance, their evidence and calibration backing and waiver rules are governed by **C.16 (MM-CHR)**. In other words, you cannot assume one context’s space fits into another’s without an explicit Bridge; any attempt to do so must treat it as a cross-context alignment with potential loss.

###### A.19:5.2.1.3 Product – **Combination** `CS₁ ⊗ CS₂ = CS⊗`.
The **product** of two spaces CS₁ and CS₂ is a new space **CS⊗** that effectively contains all slots of CS₁ and all slots of CS₂. If CS₁ has index set _I₁_ and basis slots {slot₁…} and CS₂ has _I₂_, then $CS⊗$ has index set $I\_⊗ = I₁ ⊎ I₂$ (disjoint union) with each slot’s definition carried over from its original space. In practical terms, any state in the product space is a pair _(x₁, x₂)_ where _x₁_ is a state of CS₁ and _x₂_ is a state of CS₂ (assuming the two spaces pertain to possibly different aspects or roles). **Use cases:** Product spaces allow modeling **multi-role scenarios** or bundling an entity’s state with some environmental or contextual state. For example, one might take a space of internal capability metrics and ⊗ with a space of external conditions to form a combined space for “readiness under conditions.” **Note:** When combining scores or coordinates from a product space, one must be mindful of scale incommensurability. Cross‑slot aggregation **SHALL** proceed only via a declared **Γ‑fold** (B.1) and, where needed, explicitly declared **NormalizationMethods**; naïve arithmetic is forbidden. The product operation itself doesn’t perform any aggregation; it only sets the stage.

##### A.19:5.2.2 - Comparability of **States** (two admissible regimes)

A **state label** like "Ready", "Authorized", "Degraded", etc., in a `RoleStateRelation@BoundedContext` is a criteria-defined category (defined by a checklist of conditions; see A.2.5). Determining whether the **states of two holons** are comparable (e.g. whether one is “better” or “worse” than the other in some multi-criteria sense) depends on **where** their state coordinates are located and **how** we map those coordinates to a common basis. There are two admissible comparability regimes in FPF:

###### A.19:5.2.2.1 Coordinatewise comparability (`≼_coord`)

Two states can be compared **coordinatewise** only under strict conditions. Essentially, we require the states to be expressed in the **same measurement space**, with the **same units and scales**, and using the **same state definitions**. Formally, coordinatewise comparison is allowed **only if all of the following hold**:

-   **Same space.** The two holders’ state snapshots lie in the **same CharacteristicSpace by value** (and, if relevant, the same RoleCharacteristicSpace attached to a Role in a given Context). It’s not enough that they have similarly named characteristics; they must share the actual defined space (same slots with same definitions).

-   **Scale congruence.** For each slot being compared, the scale type, unit, and polarity orientation are **identical**. For example, if comparing temperature values, both must be on the same scale (say, °C on a ratio scale with “higher = hotter” orientation). No unit mismatches or differing interpretations can be present.

-   **State-definition congruence.** The states or status labels themselves must be defined in terms of the **same checklist criteria applied in the same space**. In other words, if we are comparing whether one system is “Ready” and another is “Ready”, both instances of “Ready” must derive from the same formal definition (same characteristic-space predicates, same checklist logic) over those coordinates. If one context’s "Ready" means something different, you cannot assume they correspond.

When these conditions are met, one can define a **coordinatewise preorder** over states. Common patterns include:

- **Dominance:** For a given set of “higher is better” slots, we say state *x* **≼<sub>coord</sub>** state *y* if and only if for *every relevant slot a*, the coordinate $a(x) \le a(y)$ (**after orienting all slots to the declared polarity for that slot**). In other words, *y* is as good or better on all enforced criteria. This defines a Pareto-like ordering (often partial, not total).

-   **Predicate band inclusion:** If states are defined by satisfying declared predicate bands (e.g. State _Y_ means declared coordinates stay above specific levels), then we might say _x_ **≼<sub>coord</sub>** _y_ if _x_ satisfies every predicate that defines _y_’s state. For instance, if state _y_ = “High Performance” requires speed > 100 and accuracy > 90%, then _x_ is “no less than y” if _x_ also satisfies those predicates.

By default, **no comparability** is assumed unless proven. If any of the above congruence conditions fails, one must **not** fall back to ad-hoc comparisons (like matching by name or normalizing without declaration). Either switch to a **normalization-based regime** or declare the states **incomparable**.

###### A.19:5.2.2.2 Normalization‑based comparability (`≼_normalization`)

When two state vectors do not meet the strict conditions for coordinatewise comparison (e.g. they come from different spaces, or the “same” Characteristics are measured on different scales or units), the only sanctioned way to compare them is: **normalize, then compare**.

Concretely: if we have state _x_ in CS₁ and state _y_ in CS₂, a normalization‑based comparison is permitted only if the model can cite a set of `NormalizationMethodInstanceId`(s) under a chosen **UNM** (per **A.19.UNM**) that lands the relevant coordinates of _x_ into CS₂ (or lands both into a declared common target space). The result is understood as **NCVs** (or an `≡_UNM` quotient class) per A.19.UNM.

**Comparability rule (normalize-then-compare).** We say _x_ **≼<sub>normalization</sub>** _y_ only if, after applying the cited normalization instances to produce a representation of _x_ in CS₂ (or a common target), the mapped state can be compared **coordinatewise** under `≼_coord`. In other words, we never compare raw _x_ and _y_; we compare *after mapping into a common, well-typed space*.

If the normalization crosses context boundaries (i.e., CS₁ and CS₂ are in different bounded contexts), then by FPF policy this mapping MUST be treated as a formal **Alignment Bridge** (F.9) with an associated **congruence‑loss (CL)** level and MUST be declared via the relevant mechanism’s **A.6.1 Transport** (BridgeId + channel + `ReferencePlane(src,tgt)`; no implicit crossings). In such cases, any conclusions drawn carry an assurance penalty per **B.3** (`Φ(CL)`).

**Auditability.** Each cited `NormalizationMethodInstanceId` used for comparison SHOULD be transparent via its referenced description or edition (per **A.19.UNM**). Evidence, calibration backing, and waiver discipline are governed by **C.16 (MM‑CHR)**. The key here is that **no comparison is magic** - if values differ in scale or context, the normalization choice and its limitations must be explicit.

> **Mnemonic:** _“Never compare before both values are mapped into the same well-typed space.”_ In other words, always map measurements to a common basis (same CharacteristicSpace and units) before attempting to say one state is ≥ or ≤ another. Directly comparing raw numbers from different scales or contexts is not allowed.

##### A.19:5.2.3 - Neighboring State-Assertion Touch-Points

A.19 does not define `StateAssertion`, role-state certification, Green-Gate enactment, evidence records, assurance penalties, or operational data stubs. Those claims are governed by `A.2.5`, `A.15`, `C.16`, `B.3`, temporal patterns, and any certification-interface pattern that is current for the case.

A.19 contributes only the `CharacteristicSpace` side of such claims: the role or holon state predicate must name the `CharacteristicSpace`, slot basis, normalization instances, overlays, window, and bridge relation needed to make the coordinate claim inspectable. If a checklist or StateAssertion is translated across an embedding, A.19 requires that the space mapping and normalization references be declared; the validity of the assertion, the evidence window, and the permission to enact work remain neighboring claims.

Didactic state-assertion slice: a role-state claim such as "pump is Ready" is not itself a `CharacteristicSpace`. A.19 supplies the declared coordinates and mapping discipline: a snapshot or window over a role or holon characteristic space, slot basis, normalization instances, optional overlays, and bridge relation. A neighboring checklist, state-assertion, evidence, temporal, gate, assurance, or work pattern owns the predicate, evidence window, permission to act, and enacted work.

For example, a `Ready` checklist may require temperature below a declared threshold and pressure above a declared threshold for a declared window. A.19 requires those predicates to cite declared slots, scales, normalization instances, overlays, and window; it does not define the `StateAssertion` or the permission to proceed with work.

Characteristic-space predicate settlement: a threshold is not a `Characteristic` and not a measured value by itself. It is a predicate over one or more declared coordinates in a `CharacteristicSpace`, with polarity, comparison operator, cut value or band, window when current, normalization or bridge relation when cross-space, and the neighboring pattern that uses the predicate. The predicate may be a single coordinate cut, band or region membership, a conjunction or disjunction over coordinates, a dominance or non-dominated-set condition under a declared order overlay, a lexicographic rule, or a scalarized rule only when a scalarization policy is explicitly governed. Role-state, gate, acceptance, assurance, release, selection, improvement-loop, and decision patterns may consume such predicates; A.19 supplies only the characteristic-space side.

When a checklist or assertion is translated across an embedding, the space mapping must be explicit. Pulling a checklist into another space and pushing an assertion into a larger or different space require declared normalization and a proof, accepted bridge relation, or governing waiver. Otherwise the comparison or reuse remains incomparable for the current claim.

Operational examples and minimal data stubs, when needed, belong to the certification-interface pattern or the consumer pattern that uses the declared space. A.19 remains persistence-agnostic and identifier-scheme agnostic.

##### A.19:5.2.4 - Cross-context comparability & assurance hooks

When comparing states or metrics **across different bounded contexts** (different “context of meaning”), additional rules apply to maintain semantic integrity:

###### A.19:5.2.4.1 Direction & loss (Bridges).
Suppose we want to claim that “Holon X in Context B is in state _Ready_ as defined in Context A.” This requires an explicit **Alignment Bridge** declaration that maps the RoleCharacteristicSpace of _(Role, Context B)_ to the RoleCharacteristicSpace of _(Role, Context A)_ (or maps State B to State A). Such a Bridge (see F.9) will specify the correspondence of Characteristics (and the necessary **NormalizationMethods under UNM**) and a **congruence‑loss (CL)** level indicating how much fidelity is lost in translation. Critically, these Bridges are **one-directional** mappings unless explicitly made bidirectional. Just because we can interpret B’s state as an A-state does not mean we can go the other way without another mapping. The Bridge makes the mapping and any loss explicit. Without a declared Bridge, cross-context state comparisons or substitutions are not valid – there is no implicit global state space. The statement above, for instance, would only hold if we have something like “Bridge B→A (with defined NormalizationMethods) such that X@B can be viewed in A’s terms.” The **direction matters**: “B satisfies A’s Ready” does **not** imply the converse unless another bridge (A→B) is defined.

###### A.19:5.2.4.2 Confidence penalties for mapped comparisons.
Whenever a **normalization-based comparison** crosses Contexts (via a Bridge), assurance **MUST** apply the penalty **Φ(CL)** as **defined in B.3** (CL is **ordinal** there). For episteme-specific compositions, **B.1.3** instantiates the same policy. This pattern does **not** restate the scale or Φ; it uses **B.3** for the scale and penalty policy. For example, a safety argument that relies on a cross-context comparison might need to downgrade its certainty or include an extra safety margin. This penalty **MUST** be declared as part of the assurance argument for the comparison (stating the Bridge used and its CL), so that the Φ(CL) discount can be reasoned and applied. No implementation-level persistence format or identifier is mandated by this pattern.

###### A.19:5.2.4.3 Declare “incomparable” when appropriate.
If for some critical Characteristic there is **no valid NormalizationMethod** to translate measurements between two contexts (e.g. the scale types are fundamentally different, or the measurement’s meaning doesn’t carry over), then the framework insists that we declare the states or metrics **incomparable** rather than attempting any fudge. No comparison should ever default to “close enough by name” or other heuristics. For instance, if one context measures “User Satisfaction” qualitatively and another quantitatively, and no monotonic mapping can be justified, one must simply say a user satisfaction state in context A cannot be compared to one in context B. Mark it incomparable and avoid any misleading conclusions. This rule guards against the natural temptation to compare things just because they have the same label or general intent, when in fact their measurement basis is different.

##### A.19:5.2.5 - Characteristic-Space Reference Chain

When a consumer pattern evaluates a checklist, StateAssertion, gate, assurance argument, or decision through a declared `CharacteristicSpace`, keep the space-related references distinct:

`raw coordinates -> NormalizationMethodInstance -> quotient or NormalizationFix -> optional indicator choice -> optional order or distance overlay -> neighboring checklist, assertion, gate, assurance, or decision claim`

The left side of this chain is A.19-facing: declared space, normalization reference, quotient or fixed chart, and declared overlay. The right side is governed by the consumer pattern. Co-implementation in software or records does not collapse the conceptual references.

#### A.19:5.3 - Operator library (notation‑neutral)

**Spaces:** `Sub` (projection), `Emb` (embedding), `Prod` (product), `Quot` (quotient by declared equivalence), `NormalizationFix` (fix to a named chart or edition).

**State-criteria transport:** `Pull` (pull checklist via embedding and NormalizationMethodInstance), `Push` (push assertion along embedding with proof or waiver), `Indicatorize` (apply **IndicatorChoicePolicy** to select Indicators), `Align_B` (cross‑context alignment via Bridge with CL), `Fold_Γ` (admissible aggregation or accumulation per B.1, with WLNK and MONO constraints).

**OP‑1 (Normative).** If `Align_B` is used in **gating**, the **Bridge used** and its **CL** **MUST** be declared in the assurance argument; the corresponding Φ(CL) penalty is applied per B.3. Silent cross-context reuse is forbidden. (A.19 does not mandate any persistence identifier scheme.)

#### A.19:5.4 - Typed set views and optional neighboring transition-sensitive selection interpretation

- `TypedSetViews` name declared views over already declared set results such as one palette, one front, one archive, or one shortlist.
- A typed set view is one optional neighboring interpretive qualifier for interpretation or shipping; it does not become a new public head for the set and it does not redefine the current minimal core question by itself.
- `SelectionSlot` still returns one selected set result, and `Shortlist` remains the public head when a selected set is emitted.
- If one atlas-like interpretation uses several typed set views over the same source set, each view should keep its active source set and typed question recoverable instead of speaking as though one default view already settles the whole family.
- In source-set and space-role interpretive prose, `SearchSpaceRef` and `OutcomeSpaceRef` are role-specific refinements of the older `SpaceRef` idiom. Do not let umbrella `SpaceRef` wording hide which space-ref role the current typed-set-view interpretation depends on.
- Use one `SpaceMetricRef` only when a comparison, neighborhood, spread, or crowding claim truly depends on one declared space metric or comparison rule.
- Use one `TransitionRelationRef` only when the text must say how transition or trajectory relations behave across one declared level shift, normalization choice, or aggregation step. One covariance-style model is one admissible subtype of `TransitionRelationRef`, not the only one.
- If one typed set view also cites one such role-specific space ref or `OutcomeMapRef`, keep those refs as declared qualifiers for that view rather than as one new public set head.
- If one selector or comparison reads one derived tradition view through one typed set view, keep the underlying declared source set recoverable at the same time.
- Different typed set views may coexist for the same source set; keep that plurality visible rather than pretending one metric or transition formalism already settles every neighboring comparison.

### A.19:6.1 - Archetypal Grounding

**System state.** A pump readiness state uses temperature, vibration, pressure, and calibration-window coordinates. A.19 declares the space, slot basis, scale bindings, threshold predicates, window, and normalization references. Gate permission, work enactment, and evidence remain with their neighboring patterns.

**Episteme evaluation.** A method-description review uses clarity, evidence recoverability, source currentness, and relation precision coordinates. A.19 supplies the declared characteristic space; the evaluation pattern owns the stop condition, rating interpretation, and improvement decision.

**Cross-context comparison.** A built-asset team wants to compare readiness in two contexts with different measurement conventions. A.19 requires a declared bridge or normalization relation before coordinatewise comparison; the bridge and assurance implications stay with their governing patterns.

### A.19:6.2 - Bias-Annotation

A.19 corrects feature-vector bias: a list of numbers, labels, or dashboard fields is not yet a `CharacteristicSpace`. The space exists only when each slot binds a `U.Characteristic` to a scale and value set with declared meaning, comparability, missingness, and optional overlays.

It also corrects consumer-pattern bias. A gate, evaluation, selector, assurance, dashboard, or portfolio may use a declared space, but that use does not create another space kind. The consumer pattern owns its predicate, score, decision, assurance, or publication use; A.19 owns only the characteristic-space side.

### A.19:6 - Conformance Checklist (normative) — **CC‑A19**

**Formality references and operational segregation (normative).** A.19 aligns with **C.2.3 Unified Formality Characteristic (F)**. Use **F** directly instead of tier labels such as **T0**, **T1**, and **T2**, and treat operations separately (see **E.10** for registers).
— **F-Declaration baseline (recommended F ≥ F3).** Obligations are **declarability** and **arguability**: the author can **name** the CharacteristicSpace (basis and slots as *(Characteristic, Scale)* pairs), **state** the comparability regime (coordinatewise or normalization-based), and **express** a state’s checklist in observable coordinates. No persistence formats, identifiers, or operational provenance are required.
— **F-Predicates (F ≥ F4 when predicate-like).** As above, plus **explicit slot and NormalizationMethod names** and **stated overlays** (order or metric). When acceptance conditions are written as **typed predicates over coordinates**, declare **F ≥ F4**. Remains **notation-neutral** and **persistence-agnostic**.
— **Operational bindings (not part of F).** When automatic checking or assurance is required, use **A.19.CN**, **C.16**, and **B.3** for identifiers, validity windows, waivers, and logs. These raise **R** and **TA** in the trust calculus and **do not change F** unless the **expression form** changes (see C.2.3 orthogonality).

The following checklist summarizes the normative requirements introduced by Pattern A.19. An implementation or model **conforms** to A.19 if and only if all these conditions are met:

**Spaces & mappings**
**CC‑A19.1.** Any defined **Subspace**, **Embedding**, or **Product** of CharacteristicSpaces **MUST** explicitly list the involved slots and their metadata (scale type, unit, polarity). No comparability or merging is allowed purely by matching names or assuming correspondence – it must be declared.
**CC‑A19.2.** Every **Embedding** `ι: CS₁ ↦ CS₂` **MUST** cite a well‑defined `NormalizationMethodInstance` (per **A.19.UNM**) for each slot where `CS₁`’s slot differs in scale or unit from `CS₂`’s. The cited instances MUST satisfy the admissibility and declaration obligations governed by **A.19.UNM** (including monotonicity w.r.t. polarity, validity window, and method-class token). When the embedding is used for gating or assurance, **C.16** and the governing gate or assurance pattern own the evidence-backed claim. (Identity suffices where scales are identical.)
**CC‑A19.2a.** **Scale‑class guard (by reference).** The scale‑class requirements for admissible normalizations are governed by **A.19.UNM** (and must remain CSLC‑consistent per **A.18**). This checklist item is satisfied by citing a `NormalizationMethodInstance` whose declared class token meets those requirements; do not restate the taxonomy here.

**Comparability**
**CC‑A19.3.** **Coordinatewise comparability** (`≼_coord`) is **permitted only** when the states being compared share the **same CharacteristicSpace**, with **identical scale metadata** on each compared slot, and using the **same state definition criteria**. If these conditions aren’t fully satisfied, an implementation **MUST NOT** attempt direct coordinatewise comparison; it should either apply a **normalization‑based** method or report the items as **incomparable**.
**CC‑A19.3a.** Use of **Indicators** in any checklist or assertion **MUST** cite an **IndicatorChoicePolicy** edition. Treating any **NCV** as an Indicator **without** a declared policy is **forbidden**.

**CC‑A19.4.** **Normalization‑based comparability** (`≼_normalization`) **MUST** be done by first normalizing all relevant coordinates of the source state into the target state’s space via declared admissible `NormalizationMethodInstance`(s) (see **A.19.UNM**), and **only then** comparing in that common space. In other words, two states can be compared under `≼_normalization` only by producing an image of one in the other’s space (`N(x)`) and using `≼_coord` on the result. No implicit or “on the fly” conversions are permitted.
**CC‑A19.5.** Any cross-context state comparison or substitution **MUST** cite a corresponding **Alignment Bridge** (F.9) with an explicit **CL (congruence-loss) level**. If such a Bridge is used in an assurance or decision-making context, the model **MUST** apply the appropriate confidence reduction (`Φ(CL)` penalty per B.3) to reflect the loss. Cross-context comparisons without a Bridge (i.e. assuming equivalence by name or convention) are **forbidden**.

**Neighboring certification references**
**CC‑A19.6.** When a neighboring `StateAssertion`, checklist, gate, assurance, or decision claim uses a `CharacteristicSpace`, A.19 requires only the space-facing references: the state or coordinate set, the associated checklist or criteria set, the observation window, and any `NormalizationMethodInstance` or Bridge used for cross-space mapping. The assertion, evidence, gate, assurance, and decision claims remain governed by their own patterns; A.19 does not mandate any identifier or persistence scheme.

**CC‑A19.7.** If a Green-Gate or enactment rule uses coordinates from a `CharacteristicSpace`, the gate pattern and role-method-work pattern govern permission to act; A.19 only requires that any translated state or coordinate claim cite declared Embeddings and Bridges rather than untracked inferences.
**CC‑A19.8.** Checklist definitions that use a `CharacteristicSpace` must use observable predicates over declared coordinates and context events. If temporal order or multi-step processes matter, use explicit method and work patterns or aggregation logic outside A.19 rather than hiding a method sequence inside the state-space declaration. **Use of Indicators in any checklist MUST cite an IndicatorChoicePolicy edition; treating any NCV as an Indicator without policy is forbidden.**

**Anti‑drift**
**CC‑A19.9.** If a **NormalizationMethod** or **UNM** declaration, space overlay, or state checklist is updated or calibrated differently in a new version, previous StateAssertions are not retroactively modified by A.19. The governing assertion or record pattern closes or versions those claims; A.19 requires only that the old and new space-facing referents remain inspectable.
**CC‑A19.10.** If any **critical slot** in a comparison lacks an **admissible** `NormalizationMethodInstanceId` (per **A.19.UNM**) to translate that slot between the relevant spaces (within the declared validity window), then the comparison **MUST** be reported as **incomparable**. The model must not attempt unofficial workarounds (e.g., name‑matching, silent dropping of the slot, or ad‑hoc coercions). This rule applies even if all other slots have admissible normalization instances, unless a policy explicitly accepts the loss via a declared Bridge with stated limitations.

**Quotients & Normalization‑fix (QNT)**
**CC‑A19.11.** Equality checks and joins across spaces **MUST** target invariant forms (on a **quotient** or declared **NormalizationFixed** chart), not raw coordinates.
**CC‑A19.12.** If a checklist predicates on a normalization‑variant property, it **MUST** name the **NormalizationFix** (which UNM.NormalizationMethod or chart is assumed).
**CC‑A19.13.** All used **method‑class tokens** for cited `NormalizationMethodInstanceId`(s) **MUST** be named in the bounded context’s glossary (per the taxonomy governed by **A.19.UNM**). Do not restate the class taxonomy here.

**Metric discipline & calibration (MET)**
**CC‑A19.14.** If a distance overlay is used, acceptance predicates or KPIs over a CS **SHALL** be **non-expansive** (Lipschitz ≤ 1) w.r.t. the published `d` on the declared domain (raw coordinates or NCVs), or declare a compensating margin; otherwise they **SHALL** be isotone w.r.t. the declared product order.
**CC‑A19.15.** Any distance used in state or acceptance checks **MUST** carry max tolerated error and, where claimed, a **Lipschitz bound** for the **NormalizationMethod** composition in use.
**CC‑A19.16.** Cross‑CN‑frame inputs **SHALL** name the **normalization transform** and its **validity window**; expired transforms are invalid for gating unless waived explicitly.

**Dynamics and time**
**CC‑A19.17.** Every temporal guard **MUST** specify the window `[t_from, t_to]` and `evidence_kind ∈ {observation, prediction}`; if `prediction` is used for gating, the conditions in **§ 5.2.3.1 (Evidence kind & window)** **MUST** hold.
**CC‑A19.18.** Any dynamics map `Φ_{Δt}` used in comparison or gating **MUST** be **non-expansive** (Lipschitz ≤ 1) under the declared distance overlay **and** commute with **NormalizationFix**; otherwise **observation** is required.

**Neighboring certification use**
**CC‑A19.19.** StateAssertions that use a `CharacteristicSpace` must name the current **NormalizationMethod** or **UNM** declaration and overlay definitions used; assertion validity, waiver speech acts, evidence kind, and gate validity are governed by the assertion, evidence, waiver, and gate patterns. A.19 imposes no requirement on identifiers or persistence formats.
**CC‑A19.20.** The space-facing references in a neighboring certification use - normalization declaration, quotient or fixed chart, overlay, and coordinate predicate - are logically distinct and must be reconstructable in the argument or review. The neighboring consumer pattern owns evaluation, assertion, gate, assurance, and decision semantics.

**Operators (OP)**
**CC‑A19.21.** Use of `Align_B` in a gate or assurance claim must declare the Bridge used; the assurance pattern owns CL propagation and penalties. Cross-context comparison without a Bridge remains inadmissible for A.19 space comparability. A.19 imposes no requirement to store an identifier.

### A.19:7 - Common Anti-Patterns and How to Avoid Them

_The following are common modeling mistakes (“anti-patterns”) related to measurement spaces, and how to correct them:_

-   **“Same label ⇒ comparable.”**
    ✗ _Assuming_ **Ready@contextA ≥ Ready@contextB** _just because both states are called "Ready"._
  ✓ **Explicitly normalize and bridge contexts:** Define an Alignment **Bridge (B→A)** and appropriate **NormalizationMethods** for the underlying metrics. Then compare by first translating one state’s coordinates (compute **N(x)** as NCVs in the target space) and using `≼_coord` on the result.

-   **“Compare before common-space mapping.”**
    ✗ Comparing values directly across different scales, e.g. _Drift\_A = 5°C vs Drift\_B = 5°F_ as if they were the same.
  ✓ **Normalize to common units first:** e.g., apply the Fahrenheit-to-Celsius **NormalizationMethod** _m_(T_F) = (T_F - 32) × 5/9 to convert all data to °C, **then** compare the drift values. Always **normalize into one space** before comparing magnitudes.

-   **“Checklist = method sequence.”**
    ✗ Defining a state’s checklist with an implied sequence: _“State ‘Ready’ requires doing Step 1 then Step 2…”_
    ✓ **Keep checklists declarative:** A **Checklist** should represent a state of the system (a condition) – essentially **state evidence** – not a sequence of actions. If order or process matters, model that explicitly via a **MethodDescription** or by using a **Γ** (Gamma) aggregator for process logic. In other words, state = “Ready” might require conditions A and B to be true (regardless of how you got there), whereas the procedure to get ready (do Step1 then Step2) should be a separate method or playbook.

-   **“Retro-fix past assertions.”**
    ✗ Going back to edit or reinterpret old StateAssertions after changing a threshold or NormalizationMethod (e.g. “We updated the criteria, let’s ‘fix’ last quarter’s records to match”).
    ✓ **Never alter historical assertions:** **Leave history as-is.** If criteria change, issue new assertions under the new criteria going forward, and if needed, explicitly **version** the **NormalizationMethod** or **UNM** declaration or checklist. Past assertions remain valid for the old version and their time; new ones apply henceforth. This ensures auditability and avoids erasing or rewriting what was true under earlier standards.

**C.27 temporal-claim relation.**

- C.27 may flag: a rate or rate-change claim that needs base characteristic, scale and unit, time base or sampling window, transformation or finite-difference method, evidence, and admissible use.
- This pattern keeps: CharacteristicSpace coordinate discipline and the measurement-coordinate relation carried with C.16.
- Non-admissible use: derivative-like words such as velocity, acceleration, throughput, cadence, or recovery speed do not make a free characteristic, metric, or measurement template.
- Use boundary: when the interpretation governs the current claim, cite `baseCharacteristicRef`, the relevant measure reference, sampling window, construction method such as `DHCMethodRef`, and the C.16 measurement or construction relation reference; C.27 does not define a parallel measurement system.

**A.19.ECS object-under-improvement evaluation construction relation.**

- A.19 defines `CharacteristicSpace` as an ontological structure: slots, characteristics, scales, value sets, overlays, and comparability boundaries.
- A.19.ECS governs the construction of one object-under-improvement evaluation `CharacteristicSpace` for an object being improved. It is used before `E.22` and `E.23` when no adequate object-under-improvement evaluation exists.
- Existing object-under-improvement evaluation patterns such as `E.21`, `E.9.DA`, `E.2.DA`, and the naming vector inside `F.18` are examples of this construction shape for object kinds under improvement. They keep their own coordinate, value-meaning, and stop-condition definitions.

### A.19:8 - Consequences

| Consequence | Benefit | Cost or boundary |
| --- | --- | --- |
| Coordinate claims become inspectable | A reader can recover slot, characteristic, scale, value set, missingness, window, and normalization references. | Declaring the space takes more work than naming a feature vector or dashboard column. |
| Consumer patterns stay bounded | Gates, evaluations, assurance claims, dashboards, and selectors use declared spaces without becoming space-defining patterns. | A.19 must refuse attractive shortcuts where a consumer label looks like a coordinate kind. |
| Dynamics has a typed state space | A dynamics model can say which space its state belongs to without letting A.19 define the dynamic law or time base. | Dynamic laws, evidence, and work consequences must still be governed elsewhere. |

### A.19:9 - Rationale

A characteristic space is the minimal object that keeps multi-characteristic claims from becoming loose feature lists. The pattern binds each characteristic to a scale and value set, then lets neighboring patterns consume the declared space for state predicates, thresholds, comparisons, gates, evaluations, assurance, dashboards, and dynamics models.

The separation matters because thresholds, scores, dashboards, and decisions are not the space. They are predicates, computations, publications, or consumer claims over a declared space. A.19 keeps the coordinate ontology stable while allowing different consumers to state their own admissible use and evidence obligations.

### A.19:10 - SoTA-Echoing

Measurement and evaluation practice requires explicit variable definitions, scales, units, value ranges, missingness treatment, normalization, and comparability before multi-criteria comparison is meaningful. A.19 adapts that discipline to FPF by treating the characteristic space as the declared ontic object and by moving scoring, indicator choice, normalization, and assurance use to their governing patterns.

Dynamical-systems and state-space practice supplies the useful hook: a dynamics model needs a declared state space, but the state space does not itself define the law, time base, observation model, or intervention. FPF keeps that boundary so that characteristic-space declarations can be reused across system, episteme, evaluation, and architecture work without smuggling consumer semantics into the space.

### A.19:12.1 - C.29 mathematical-lens use relation

> If topology, order, distance, product, subspace, embedding, or metric is only a `CharacteristicSpace` overlay, stay in `A.19` and write the space, coordinate, normalization, and comparability declaration there. If the overlay is used as a mathematical lens to explain, predict, bridge, assure, publish, compare across contexts, or carry a reusable explanation claim beyond local declaration, add the applicable `C.29` lens-use result for the stated lens use. Do not move the space declaration out of `A.19`; `C.29` names only what the mathematical lens preserves, loses, makes visible, and cannot license.

### A.19:12.2 - Source Role and Currentness

A.19 is primarily internal-kernel doctrine, not an external SoTA-import pattern. Its authority for `U.CharacteristicSpace` comes from the accepted FPF chain: `A.17` for `U.Characteristic`, `A.18` for scale and value discipline, `C.16` for measurement and coordinate evidence, `A.19.UNM` for normalization methods, `C.29` when a mathematical lens is being used beyond local space declaration, and `E.24` for ontic-head and slot-relation discipline.

Currentness is therefore inherited through that chain. Reopen A.19 when any governing pattern in that chain changes characteristic identity, scale semantics, value-set meaning, missingness semantics, normalization admissibility, comparability, bridge discipline, mathematical-lens boundary, or ontic slot discipline. Do not reopen A.19 merely because one consumer pattern adds a new score table, dashboard, evaluation report, certification interface, or portfolio view that uses a declared `CharacteristicSpace`.

### A.19:13 - Relations - Ontic Relations and Consumer Boundary

- **Builds on:** `E.24` for ontic-head discipline, `A.6.5` for slot relation discipline, `A.17` and `A.18` for characteristic and scale discipline, and `C.16` for measurement and coordinate evidence.
- **Coordinates with:** `A.19.ECS` for constructing evaluation characteristic spaces for object kinds under improvement; `E.21`, `E.9.DA`, and `E.2.DA` for pattern, DRR, and FPF-level evaluation use; `E.24.PUB` when a score table, dashboard, report, or publication form is confused with the characteristic space itself.
- **Does not replace:** CHR mechanism-governing patterns, consumer patterns that use a declared space, source-set relations, publication-form patterns, or mathematical-lens use under `C.29`.

### A.19:End

