## A.19 - CharacteristicSpace & Dynamics Hook (A.CHR‑SPACE)

> **Type:** Kernel characteristic-space and dynamics-typing pattern
> **Status:** Stable

**Use this when.** Use this pattern when the current object is either a declared `CharacteristicSpace` or a reusable by-value `CharacteristicSpacePredicate` over that space: characteristics, scales, value sets, coordinate bindings, optional overlays, predicate operators and cuts, comparability and normalization boundaries, partial-observation handling, and the `U.Dynamics.stateSpace` hook.

**What goes wrong if missed.** Teams compare raw numbers from different scales, treat dashboards or scores as the space, hide thresholds inside state labels, silently change a predicate use's scope or evaluation window, smuggle method sequences into checklists, or give consumer patterns private space and predicate kinds.

**What this buys.** One declared space and one recoverable predicate form that make state, threshold, comparability, normalization, and dynamics-typing claims inspectable while leaving each evaluation, result, evidence use, gate, and selection occurrence with its subject pattern.

### A.19:0 - First use: declare a space and one predicate

Use A.19 when you need to say which Characteristics form one state space and what reusable condition can be tested on a state in that space.

**First move.** Name the `CharacteristicSpace` and list its slots. Each slot names one Characteristic, its subject or input roles, and one Scale with its admissible values. Add order, topology, distance, or a mapping only when a real use needs it.

**Smallest complete case.** A pump team declares `PumpOperatingSpace` with two slots:

| Slot | Characteristic and subject | Scale |
| --- | --- | --- |
| `coolantTemperature` | temperature of one Pump | degrees Celsius, `0..120` |
| `dischargePressure` | discharge pressure of one Pump | kilopascals, `0..1000` |

For Pump #37, the available Coordinate tuple is `(72 °C, 315 kPa)`. The reusable condition is:

> `ready(x) := 60 °C <= x.coolantTemperature <= 80 °C and x.dischargePressure >= 300 kPa`.

For this tuple, `ready(x)` is true. That is the practical result: a reader can recover the two meanings, inspect the current input, and repeat the test. The declaration does not by itself claim that the readings are current, authorize work, or pass a gate.

**Add only what the next use needs.**

- If the Characteristic, Scale, or measurement chain is not sound yet, start with A.17, A.18, or C.16.
- For normalization, indicator choice, scoring, aggregation, comparison, or selection, use A.19.UNM, A.19.UINDM, A.19.USCM, A.19.ULSAM or B.1, A.19.CPM, or A.19.SelectorMechanism respectively. G.0 checks whether the numeric operation is admissible.
- Use A.3.3 when the space types a dynamics model.
- Use A.19.CHR with A.15.3 or E.18 only for a planned suite or baseline, and E.20 only for a project specialization.
- Use the direct evaluation, gate, evidence, or assurance pattern for that separate use.

If none of those questions is current, stop with the space and predicate above.

**Boundary.** A.19 defines the space and reusable predicate. A subject binding, partial observation, evaluation, result, comparison, gate, evidence use, view, or publication remains a separate value or occurrence under its direct pattern.

### A.19:1 - Intent & Scope (Normative)

**Intent.** Establish two composable A.19 values. `U.CharacteristicSpace` is the declared space of characteristics, scales, genuine Scale value sets, Coordinate positions and groups, optional overlays, comparability boundaries, normalization boundaries, and typing hooks. `CharacteristicSpacePredicate` is a typed unary Boolean predicate over declared Coordinates in one such space. Partial observations and their absence statuses remain consumer inputs. For dynamics, `U.Dynamics.stateSpace` points to the declared space so a holon's change can be described as a trajectory in typed Coordinates. For epistemes, state remains governed by ESG; F-G-R are assurance coordinates, not an episteme state space.

`U.CharacteristicSpace` is the declared multi-characteristic space. `CharacteristicSpacePredicate` is a reusable predicate by value, not its wording, evaluation, or result. Consumer uses remain separate from both.

**Scope.** Pattern A.19 defines:
- the declared `U.CharacteristicSpace` value as a finite product of slot value sets under A.18;
- the slot construct that binds one `U.Characteristic` to one selected scale and value set;
- the typed unary `CharacteristicSpacePredicate` over declared Coordinates, including its input variable, domain and coordinate projection, Scale meanings, any A.19.UNM normalization used to obtain its inputs, Boolean expression, cut or band, composition, and polarity;
- optional order, topology, and distance overlays that downstream patterns may use when declared; and
- the typing hook `U.Dynamics.stateSpace : CharacteristicSpace`.

A.19 stops after the space, predicate, optional overlays, and dynamics typing hook. Use A.19.UNM for normalization, A.19.CPM for comparison, A.19.SelectorMechanism for selection, C.16 and A.10 for measurement and evidence, and A.3.3 for dynamics.

**Space-and-predicate versus consumer boundary.** A consumer reference such as `...SpaceRef` designates one declared space. A consumer use of a predicate separately binds its exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective `U.ReferenceScheme` and reference plane, application or evaluation window, available input or partial-input status, and evaluation operation. Those bindings are not fields of the space or predicate. They may change while the predicate remains the same; changing the predicate's input domain or coordinate projection, Scale meaning, normalization, Boolean expression, cut or band, composition, or polarity creates a different predicate. Any obtaining semantic Bridge, its bounded-use claim and reliance, and any applicable plane relation are separately identified for the consumer use; none identifies the predicate. A.19.CPM separately governs comparison relations, comparator applications, and their results.

`A.19.ECS` constructs an evaluation `CharacteristicSpace` for an object kind under improvement. `E.21`, `E.9.DA`, `E.2.DA`, and other evaluation patterns consume declared spaces and predicates for their own evaluated objects. A.19 supplies the reusable values; those patterns supply object-specific applicability, evaluation, result, evidence-use, stop, and receiving-work semantics.
### A.19:2 - Context (Informative)

FPF already standardizes what is characterized through A.17 and how one characteristic is scaled through A.18. Dynamics, evaluation, and comparison additionally need a declared common value space in which several characteristics coexist without losing scale, arity, or meaning. They also need reusable predicates whose semantic components remain recoverable independently of a criterion description, one evaluation occurrence, or one result. A.19 supplies those two values without inventing a generic semantic-locality container or duplicating consumer scope, time, evidence, and result relations.

### A.19:3 - Problem (Informative)

- **P1 - Feature-vector drift.** A list of values with implicit units, scales, subject/input arity, or partial-input handling cannot support a sound state or comparison claim.
- **P2 - Lifecycle bias.** Without a declared space, system change is narrated as one-way stages instead of typed trajectories and separately governed state or classification claims.
- **P3 - Semantic-locality collapse.** Different claim scopes, context slices, reference schemes, or reference planes may use different coordinate sets or meanings. Treating one umbrella context label as their common identity makes projection and comparison unverifiable.
- **P4 - Relational characteristics.** A multi-entity characteristic loses arity and direction when flattened into an intrinsic scalar.
- **P5 - Hidden predicate semantics.** A threshold label or criterion-description edition can conceal the actual input variable, Coordinate projection, Scale, Boolean operator, cut, polarity, and normalization or coordinate-mapping basis.
- **P6 - Geometry by implication.** An undeclared order, topology, distance, scalarization, or aggregation can silently decide a comparison or selection.

### A.19:4 - Forces (Informative)

- **F1 - Scale integrity at product size.** Every Coordinate retains its own Characteristic, Scale, unit, and admissible domain, while an observation's missing or censored status remains separate.
- **F2 - Transdisciplinarity with lexical clarity.** Quantitative, qualitative, intrinsic, and relational characteristics must compose without replacing the canonical A.17-A.18 vocabulary.
- **F3 - Minimal core with explicit overlays.** Order, topology, distance, normalization, scalarization, and aggregation are available only when declared under their subject patterns.
- **F4 - Predicate reuse without consumer collapse.** One semantic predicate should be reusable across state, comparison, acceptance, selection, and improvement uses, while each use retains its own scope, slice, plane, window, evaluation, result, and evidence relations.
- **F5 - Safe composition.** Projection, embedding, product, and declared coordinate transport must preserve exact coordinate and scale meaning and make losses explicit. Any semantic Bridge or plane relation remains separate from coordinate transport and is cited only by a consumer that needs it.
- **F6 - Ordinary usability.** An engineer should be able to state a space and criterion without first creating a publication record, evaluation occurrence, or generic result relation.

### A.19:5 - Solution

#### A.19:5.1 - `U.CharacteristicSpace`

##### A.19:5.1.1 - Type signature

Each slot `i` names one `U.Characteristic` and one chosen `Scale`:

> `slot_i = (Characteristic_i, Scale_i)`.

The Characteristic supplies its subject/input signature: the entity kinds and roles required when it is assigned a value. For a relation Characteristic the signature also gives the role order, or states that the relation is symmetric. A use of the slot binds that participant tuple separately. The tuple is not the Coordinate; the Coordinate is a value on the chosen Scale. C.16 uses the same separation between measurand or subject tuple and measured Coordinate.

The **CharacteristicSpace** is the Cartesian product of the slots' genuine Scale value sets:

> `CS = product_i ValueSet(Scale_i)`.

A point `x` in `CS` supplies one Coordinate `x(i)` from `ValueSet(Scale_i)` for every slot. Using that point for a subject separately binds a conforming subject/input tuple `b_i` and states or evaluates the characteristic assignment between `b_i` and `x(i)`. For example, the distance Characteristic may bind `(Machine-A, Machine-B)` while its Coordinate is `3.5 m`.

A complete state is total over the selected basis. An observation or evaluation input may instead be partial: it supplies Coordinates only for a subset of slots and records `missing`, `censored`, `unknown`, or another observation status separately. A consumer applies its own applicability and tri-state or error rule before treating such input as a state. `not-applicable` is normally an applicability fact, not a Scale value; a domain may use it as a genuine value only when the Scale explicitly defines that meaning.

Any `U.Dynamics.stateSpace` refers to a declared `CharacteristicSpace`, and its states and trajectories use points in that space. A.3.3 supplies the dynamic law, time base, observation relation, and prediction-use conditions.

##### A.19:5.1.2 - Slot discipline (invariants)

To ensure consistency and comparability, a CharacteristicSpace must obey the following invariants:

-   **A19-CS-1 (Exactly one per slot).** Each slot **binds exactly one** Characteristic to **exactly one** Scale (including a specific Unit or kind, if applicable). This mirrors the CSLC clause of “one aspect – one scale”: there are no ambiguous or compound mappings in a single slot. (If a Characteristic can be measured on multiple scales, only one is chosen for a given space; others would require separate slots or a different space.)

- **A19-CS-2 (Named basis).** A CharacteristicSpace declaration contains an ordered basis of slots. Each slot has a stable technical name and makes its Characteristic, Scale, position, and the Characteristic's subject/input signature recoverable. Plain-language aliases may aid recognition but do not change the basis.

- **A19-CS-3 (Stable meaning).** Do not silently change a slot's Characteristic, Scale, or position while claiming the same space. Declare the changed space and an explicit mapping from the earlier space. Call that mapping an embedding only when it is point-injective and preserves every named structure; use a lossy normalization or projection for deliberate coarse-graining.

- **A19-CS-4 (Arity preservation).** A slot for an entity Characteristic binds one subject. A slot for a relation Characteristic binds the exact ordered or unordered subject/input tuple required by that Characteristic. Direction and symmetry belong to this signature. In either case the Coordinate remains one value on the declared Scale; the participant tuple never substitutes for it.

- **A19-CS-5 (No hidden normalization, preference, or aggregation).** A `CharacteristicSpace` carries no implicit normalization, polarity preference, threshold, formula, or aggregation. A `CharacteristicSpacePredicate` may declare polarity, operator semantics, and a cut or band over that space. Normalizing, indicatorizing, scoring, folding, comparing, and selecting remain explicit operations under their subject patterns; the space declaration itself performs none of them. A.19.UNM governs normalization semantics and admissibility; C.16 governs relied-on measurement and calibration claims.
- **A19-CS-6 (Value and absence discipline).** Each slot declares its admissible Scale domain. Missing, censored, unknown, and inapplicable input states stay with the observation, record, or evaluation use rather than entering the ontic Scale value set. `not-applicable` is a Scale value only when that domain explicitly gives it a subject-side meaning.

- **A19-CS-7 (Space-versus-consumer boundary).** A `CharacteristicSpace` declaration contains only its basis, optional overlays, and typing hooks. A consumer separately declares references to the space, relation positions, source use, views, publication details, applicability, partial-input handling, and evaluation results.

##### A.19:5.1.3 - Minimal structure hooks (optional overlays)

A CharacteristicSpace has no default order, topology, or distance. Declare only the structure that a real use needs:

- **Order overlay.** `OrderOverlay = (D, preceq, laws, applicability)`, where `D` is a stated subset of `CS`, `preceq` is a typed binary relation on `D`, and `laws` say whether it is a preorder, partial order, or another named order. The declaration explains how the relation respects each participating Scale.
- **Topology overlay.** `TopologyOverlay = (D, tau, construction, applicability)`, where `tau` is a topology on `D`. The construction may cite a product topology or give another basis; the name alone supplies no continuity claim.
- **Distance overlay.** `DistanceOverlay = (D, d, distanceLaws, parameters, applicability)`, where `d : D x D -> nonnegative values`. `distanceLaws` states exactly which separation, symmetry, direction, and triangle conditions hold; parameters include any weights, units, normalization basis, and validity conditions.

The declaration of every overlay is optional. Once a consumer relies on one, however, it names the exact overlay and stays within its domain and applicability conditions; any claimed order preservation, continuity, convergence, sensitivity, robustness, or stability must satisfy the laws of that overlay. An overlay adds analysis structure and cannot redefine a slot's Characteristic, Scale, admissible operations, or Coordinate meaning.

Here **distance** means a mathematical distance function, not a performance measure or a C.16 measurement method. Use `U.DHCMethod` or `U.DHCMethodRef` for measurement templates.

##### A.19:5.1.4 - Dynamics hook (typing only)

Any model of change or dynamics in FPF must declare the state space it operates over. Formally, `U.Dynamics.stateSpace` **SHALL** be specified as a reference to a `CharacteristicSpace`. This creates a typing requirement: the dynamic model can only produce states and trajectories of states that belong to the given space. All predicates or predictions in such a dynamics model are understood to **quantify over** sequences of points in that CharacteristicSpace (with time semantics governed by A.3.3’s time base and laws). **Note:** A.19 defines only the structure of the state space; it deliberately **does not** fix any time base or dynamic law. Those remain the responsibility of the dynamics pattern (A.3.3). A.19 simply ensures there is a well-defined space in which states are located, so that dynamics are decoupled from any narrative “stage” and instead treat evolution as movement through this space.

##### A.19:5.1.5 - Lexical discipline (Normative)

In all **normative references, definitions, and identifiers** related to this pattern, the specification uses the canonical measurement terminology: **Characteristic**, **Scale**, **Level**, **Coordinate**, **CharacteristicSpace**, **slot**, **basis**. Legacy terms like “axis”, “dimension”, or “point” are **forbidden** in Technical and Formal registers of the spec (per A.17’s lexical rules). They may appear _at most once_ in explanatory **Plain** language as mapped aliases to aid understanding (and if used, must be explicitly identified as equivalent to the official terms). In this pattern, we consistently use “slot” or “basis element” (never “axis”) to refer to a component of a space, and “Characteristic” (never “dimension”) to refer to the measured aspect. This lexical discipline ensures clarity and consistency across the framework (see A.17 and C.16 L-rules for the formal policy on terminology).

##### A.19:5.1.6 - Quotients & NormalizationFix (Normative)

**Subject-pattern note.** `≡_UNM` and `NormalizationFix` are defined in **A.19.UNM**. This section constrains only how they are **cited** when used in state‑space reasoning.

**Design rule — read invariants, not labels.** Any checklist, acceptance predicate, equality check, join, or comparability claim over a `CharacteristicSpace` that depends on representation choice (chart, unit, reference plane, normalization choice, or label) **SHALL** be evaluated on **quotients by ≡_UNM** or on explicitly **Normalization‑fixed** charts, not on raw labels.
*Minimal obligations:*
1) **Name the quotient or fix.** If a checklist predicates over a **normalization‑variant** property, it **MUST** name the **NormalizationFix** (including the referenced **UNM** and the relevant `NormalizationMethodInstance`(s), by reference) and thus the **≡_UNM** class.
2) **Declare NormalizationMethod class.** Every normalization used **MUST** name its method‑class token and validity window **as defined in A.19.UNM** (do not restate the class taxonomy here).
3) **Join and equality only on invariants.** Equality checks and joins across spaces **MUST** target invariant forms (the **≡_UNM** quotient or a declared **Normalization-fixed** representation), never raw un-fixed coordinates.

##### A.19:5.1.7 - Overlay use, sensitivity, and calibration (Normative)

Use the weakest declared overlay that the argument needs. Declaring an order or distance does not make every predicate monotone, every map non-expansive, or either property necessary or sufficient for acceptance. Bands, target regions, and Boolean cuts are valid even when they are not isotone or continuous.

When a consumer makes a sensitivity, robustness, continuity, stability, or prediction-use claim, that consumer states:

1. the exact function, predicate evaluation, or transition map and the overlay it uses;
2. the domain, codomain, applicability conditions, and claimed property;
3. any bound, margin, approximation, uncertainty, or error allowance required by the consumer's policy; and
4. the evidence or argument needed for that use.

A useful bound need not be `Lipschitz <= 1`; its admissible value comes from the named use and policy. Claim isotonicity only when the use depends on order preservation. Claim commutation with normalization only when that exact composition matters. C.16 governs relied-on measurement and calibration claims. A.3.3 governs prediction error, horizon, and model applicability; A.20, A.21, G.4, and the direct authority pattern govern their own constraint, gate, criterion, and decision consequences. Non-expansiveness or commutation alone grants no gate, release, assurance, or work authority.

##### A.19:5.1.8 - `CharacteristicSpacePredicate` (by-value)

A `CharacteristicSpacePredicate` is a typed unary predicate over one declared space:

> `P : D_P -> Boolean`, where `D_P` is a declared subset of `CS`.

Its input variable denotes one state. The predicate declares which coordinates it reads and any projection used to obtain them. Its complete by-value meaning contains:

- the exact `CharacteristicSpace`, input variable, domain, and coordinate projection;
- each read Coordinate's Scale and value interpretation;
- any exact coordinate projection or A.19.UNM normalization instance used to obtain those inputs;
- the operators, cuts, bands, regions, or unary subpredicates used in its Boolean expression; and
- the polarity that says which outcome satisfies the predicate.

Thresholds, bands, and regions are unary predicates of this kind. Compose predicates with logical operators only after their input bindings and domains are aligned; otherwise give the composition an explicit binding that makes the conversion visible. A dominance or other comparison between two states is instead a typed binary comparison relation such as `R : D_left x D_right -> Boolean`, governed by A.19.CPM or another direct comparison pattern. Its comparator application and result are not components of a unary `CharacteristicSpacePredicate`. Use a genuinely n-ary predicate only when its full variable roles, domains, projections, and result type are declared.

An arbitrary condition relation is not automatically a state or Coordinate. A use binds either a direct characteristic assignment or an explicit governed projection from its subject/input tuple to the predicate input. When the affected entity differs from the condition participants, the consumer also states that direct relation. An F.9 Bridge relates two exact local senses; it is not this subject-to-input binding.

The predicate carries no applicability, assessment, observation, evidence, or evaluation window. A consumer separately binds the exact `U.ClaimScope`, relevant `U.ContextSlice` membership, effective reference scheme and plane, application or evaluation window, available input, and evaluation operation. An evaluation may return `unknown`, `not-applicable`, or `error` when input or applicability is unresolved; those consumer results do not enlarge the predicate's Boolean codomain or the space's Scale value sets. A dated evaluation is `U.Work`; its operation application and result remain separate from the predicate.

Predicate identity changes when one of these semantic components changes. Wording, notation, carrier, publication, identifier, or description-edition changes alone do not create another predicate. A consumer may evaluate the same predicate in another scope or window, but may not silently change its space, projection, Scale, normalization, expression, cut, band, composition, or polarity. An obtaining semantic Bridge or plane relation may be cited by one consumer use without becoming part of predicate identity.

**Minimally viable case.** In a pump space with `batteryVoltage` on the volt Scale, `batteryReady(x) := x.batteryVoltage >= 24 V` is a unary predicate with Boolean result. A maintenance check separately binds Pump #37, its current measured input and window, and the evaluation result. Comparing two pumps by voltage would be a separate binary comparison relation, not a second reading of `batteryReady`.

#### A.19:5.2 - State Spaces & Comparability

> **Memory hook:** Compare only values already in the same declared space or carried into one common space through an exact coordinate mapping. Reusing a predicate also requires the same semantic predicate. If the use also claims a relation between two exact F.17 local senses, cite an F.9 Bridge only after its predicate obtains and state the bounded-use claim and reliance separately. If the ReferencePlane changes, cite the applicable plane relation. Scope and window remain separate in either case.

This section supplies space projection, embedding, product, and two coordinate-comparability regimes. It does not perform a CPM comparison or a SelectorMechanism selection. A consumer that names a state or category cites the declared space and predicate, then keeps its own scope, evaluation, result, evidence, and work relations.

A CharacteristicSpace may be written abstractly as `CS = ⟨I, basis⟩`, where `I` indexes slots and `basis` is the ordered set of `(Characteristic, Scale)` bindings. A consumer-specific label for a space does not create another A.19 kind; the consumer instead states the exact use or relation position, entity, claim scope, context-slice membership, effective reference scheme and plane, and predicate relevant to that use.

##### A.19:5.2.1 - CS Operators (notation-neutral, reference-scheme-local)

To enable model composition, define operations on CharacteristicSpaces independently of notation. Every operation states its effective `U.ReferenceScheme` and reference plane. Those values locate the operation but create no correspondence. When a use relates two exact F.17 local senses, test the direct F.9 predicate and cite the Bridge only when it obtains; state the bounded-use claim and any reliance separately. A ReferencePlane crossing cites its applicable plane relation. A scheme or plane difference alone establishes neither relation.

###### A.19:5.2.1.1 - Subspace — projection

For a space `CS_I` with basis `I` and a subset `S`, the projection `pi_S^I : CS_I -> CS_S` keeps the Coordinates in `S` and discards the others. The type-correct laws are `pi_I^I = identity_CS_I` and, for `T subseteq S subseteq I`, `pi_T^S after pi_S^I = pi_T^I`. A projection preserves an order, topology, or other structure only when that fact follows from the named overlays; projection alone makes no such promise.

###### A.19:5.2.1.2 - Embedding and lossy mapping

An embedding `iota : CS_1 -> CS_2` is point-injective and preserves every structure named by its declaration. It gives an injective slot correspondence and an injective value map for each corresponding slot. Identity maps and exact, reversible unit conversions can support an embedding when they preserve the declared Scale meaning. The declaration states its domain, image, preserved structures, and any A.19.UNM instances used.

A coarse-graining, binning, many-to-one normalization, or dropped-coordinate operation is not an embedding. Declare it as a lossy mapping or projection, state the preserved and lost distinctions, and let each consumer decide whether that loss is admissible for its comparison, prediction, gate, or assurance use. When the use relates two exact F.17 local senses and the F.9 predicate obtains, cite that Bridge and a separate bounded-use claim. A ReferencePlane change instead cites its applicable plane relation. The coordinate mapping, semantic relation, plane relation, and C.16 calibration or measurement backing remain separate.

###### A.19:5.2.1.3 Product – **Combination** `CS₁ ⊗ CS₂ = CS⊗`.

The **product** of two spaces CS₁ and CS₂ is a new space **CS⊗** whose basis is the disjoint union of both bases, so even same-named slots retain their source identity. Its state is a pair `(x₁, x₂)`. For example, a product can combine internal capability Coordinates with external-condition Coordinates for a readiness use. The product does not aggregate them: any cross-slot aggregation uses a declared B.1 `Gamma` fold and any needed A.19.UNM normalization.

##### A.19:5.2.2 - Comparability of **States** (two admissible regimes)

A label such as `Ready`, `Authorized`, or `Degraded` is a consumer-side category, not a space or comparison result. Its subject pattern states the predicate and evaluation use. Comparing two coordinate states depends on the declared spaces, mappings, scales, and comparison scope; A.19 permits only the following two coordinate regimes.

###### A.19:5.2.2.1 Coordinatewise comparability (`≼_coord`)

Two states can be compared **coordinatewise** only under strict conditions. Essentially, we require the states to be expressed in the **same measurement space**, with the **same units and scales**, and using the **same state definitions**. Formally, coordinatewise comparison is allowed **only if all of the following hold**:

-   **Same space.** Both coordinate values lie in the same `CharacteristicSpace` by value. Similar names, shared storage, or a common model-use label are insufficient.

-   **Scale congruence.** For each slot being compared, the scale type, unit, and polarity orientation are **identical**. For example, if comparing temperature values, both must be on the same scale (say, °C on a ratio scale with “higher = hotter” orientation). No unit mismatches or differing interpretations can be present.

-   **Predicate and use congruence.** When comparison depends on a category predicate, both values use the same `CharacteristicSpacePredicate` by value. CPM still states the exact comparison scope, comparator, reference plane, and evaluation window; A.19 does not infer them from matching labels.

When these conditions are met, one can define a **coordinatewise preorder** over states. Common patterns include:

- **Dominance:** For a given set of “higher is better” slots, we say state *x* **≼<sub>coord</sub>** state *y* if and only if for *every relevant slot a*, the coordinate $a(x) \le a(y)$ (**after orienting all slots to the declared polarity for that slot**). In other words, *y* is as good or better on all enforced criteria. This defines a Pareto-like ordering (often partial, not total).

-   **Predicate band inclusion:** If states are defined by satisfying declared predicate bands (e.g. State _Y_ means declared coordinates stay above specific levels), then we might say _x_ **≼<sub>coord</sub>** _y_ if _x_ satisfies every predicate that defines _y_’s state. For instance, if state _y_ = “High Performance” requires speed > 100 and accuracy > 90%, then _x_ is “no less than y” if _x_ also satisfies those predicates.

By default, **no comparability** is assumed unless proven. If any of the above congruence conditions fails, one must **not** fall back to ad-hoc comparisons (like matching by name or normalizing without declaration). Either switch to a **normalization-based regime** or declare the states **incomparable**.

###### A.19:5.2.2.2 Normalization‑based comparability (`≼_normalization`)

When two state vectors do not meet the strict conditions for coordinatewise comparison (e.g. they come from different spaces, or the “same” Characteristics are measured on different scales or units), the only sanctioned way to compare them is: **normalize, then compare**.

Concretely: if we have state _x_ in CS₁ and state _y_ in CS₂, a normalization‑based comparison is permitted only if the model can cite a set of `NormalizationMethodInstanceId`(s) under a chosen **UNM** (per **A.19.UNM**) that lands the relevant coordinates of _x_ into CS₂ (or lands both into a declared common target space). The result is understood as **NCVs** (or an `≡_UNM` quotient class) per A.19.UNM.

**Comparability rule (normalize-then-compare).** We say _x_ **≼<sub>normalization</sub>** _y_ only if, after applying the cited normalization instances to produce a representation of _x_ in CS₂ (or a common target), the mapped state can be compared **coordinatewise** under `≼_coord`. In other words, we never compare raw _x_ and _y_; we compare *after mapping into a common, well-typed space*.

If a normalization use also spans different reference schemes or planes, keep the decisions separate. The A.19.UNM instance supplies the coordinate mapping. Cite an F.9 Bridge only when the use relates two exact F.17 local senses and its direct predicate obtains; state the bounded-use claim and reliance separately, with `CL` only as optional evidence shorthand. A ReferencePlane crossing cites its applicable plane relation. CPM supplies the comparison scope and evaluation window, and B.3 enters only for an actual assurance use. None of these relations or consequences follows from the scheme or plane difference alone.

**Inspectability.** Each normalization instance used for comparison is recoverable through its A.19.UNM declaration. C.16 governs measurement and calibration backing. When values differ in scale, reference scheme, or plane, keep the normalization, any independently obtaining semantic Bridge with its separate use claim, any applicable plane relation, and their limitations explicit.

> **Mnemonic:** Never compare before both values are carried into the same well-typed space; never claim the same predicate, scope, plane, or window merely from matching labels.

##### A.19:5.2.3 - Predicate-use and state-assertion boundary

A.19 defines the space and `CharacteristicSpacePredicate`; it does not define a state assertion, applicability relation, dated evaluation work, gate, evidence relation, assurance result, or permission to act.

A consumer use recovers: the exact subject or input; any direct characteristic assignment or projection from that subject; the A.19 space and predicate; one set-valued `U.ClaimScope`; relevant A.2.6 `U.ContextSlice` membership; effective `U.ReferenceScheme` and reference plane; application or evaluation window; and, only when current, any obtaining F.9 Bridge with its separate bounded-use claim and reliance, plus any applicable plane relation. The consumer identifies the exact evaluation-operation application and its typed result under the applicable evaluation or assertion rule. A.10 provenance, G.11 currentness, measurement backing, assurance, and receiving-work disposition remain separate.

For a `Ready` claim requiring temperature below a cut and pressure above a cut, A.19 supplies the two declared coordinates, scales, normalization or coordinate-mapping basis, operators, cuts, polarity, and conjunction. The actual state assertion binds the pump, scope, slice, evaluation interval, inputs, result, and evidence use. Any semantic Bridge or plane relation needed by that use remains separate. Changing the evaluation interval does not change the predicate; changing either cut does.

Transporting a predicate into another space or transporting an assertion across spaces requires the exact Coordinate correspondence. Use an embedding only for point-injective structure-preserving transport; use a declared lossy mapping or projection when normalization discards distinctions. If the use relates two exact F.17 local senses and the F.9 predicate obtains, cite that Bridge and its separate bounded-use claim. If the ReferencePlane changes, cite the applicable plane relation. A scheme or plane difference alone establishes neither relation. If the required correspondence is absent, the current use is incomparable or unevaluable rather than approximately valid.

##### A.19:5.2.4 - Cross-reference-scheme and cross-plane comparability

A comparison across reference schemes or planes follows the relations the case actually needs. When it relates two exact F.17 local senses and the F.9 predicate obtains, cite that Bridge and a separate bounded-use claim; `CL` is optional evidence shorthand. A plane crossing cites its applicable plane relation. Keep the coordinate mapping and A.19.UNM instances explicit. A context, scheme, or plane difference alone establishes no Bridge or comparison admissibility, and a reverse comparison needs its own justified direction.

A comparison may reuse a predicate only when its complete by-value meaning is unchanged. When a coordinate mapping is needed, it must preserve every predicate component required by this use. If the reuse also relates two exact local senses through an obtaining Bridge, a separate bounded-use claim states that semantic use and any required reliance passes. CPM separately binds comparison scope, comparator, input values, effective reference plane, and evaluation window. The Bridge alone copies neither predicate content, scope, nor time, and a common label establishes none of them.

B.3 or the direct assurance pattern contains the defining content for any confidence or margin consequence. Report the values as incomparable for the use when a critical coordinate lacks an admissible normalization or coordinate mapping; a separately needed semantic Bridge, bounded-use claim, or plane relation is absent; any required reliance does not pass; or the predicate, plane, scope, or window cannot be held fixed.

##### A.19:5.2.5 - Characteristic-Space Reference Chain

When a consumer pattern evaluates a checklist, StateAssertion, gate, assurance argument, or decision through a declared `CharacteristicSpace`, keep the space-related references distinct:

`declared Coordinates -> [normalization or quotient, when used] -> [indicator choice, when used] -> [order, topology, or distance overlay, when used] -> neighboring predicate evaluation, assertion, gate, assurance, or decision claim`

Only the branches actually used are present. A.19 supplies the declared space and any named mapping, quotient, or overlay; the consumer supplies applicability, operation, result, and consequence. Co-implementation in software or records does not collapse these values.

#### A.19:5.3 - Operator library (notation‑neutral)

**Spaces:** `Sub` (projection), `Emb` (embedding), `Prod` (product), `Quot` (quotient by declared equivalence), `NormalizationFix` (fix to a named chart or edition).

**Predicate and assertion transport:** `Pull` transports a predicate through a declared embedding or lossy mapping; `Push` transports an assertion with proof or waiver under its subject pattern; `Indicatorize` applies an `IndicatorChoicePolicy`; and `Fold_Gamma` performs admissible aggregation under its subject pattern. `Align_B` is not a space operator: when retained as a consumer mnemonic, it names only an already obtaining F.9 Bridge between two exact F.17 local senses. A ReferencePlane relation remains separate.

**OP-1 (Normative).** Use `Align_B` only after the direct F.9 predicate obtains. The consumer cites that exact Bridge, a separate bounded-use claim, and the reliance required for the named gate, comparison, or assurance use; `CL` remains optional evidence shorthand. A ReferencePlane crossing cites its applicable plane relation and does not use `Align_B` unless an independently obtaining semantic Bridge is also current. The consumer separately binds scope, evaluation window, and result; any assurance consequence requires a separately current B.3 assurance result.

#### A.19:5.4 - Set-view, comparison, and selection boundary

A view, comparison result, selection, portfolio, distance-based neighborhood, or transition-sensitive interpretation is a consumer value. It may cite an A.19 space, predicate, order, distance, or transition relation, but its identity and result remain with the direct view, comparison, selection, or transition pattern.

### A.19:5.5 - Further worked uses

**More coordinates.** A pump condition may add vibration or calibration Coordinates to the two-slot example. Add each slot only with its Characteristic, subject/input signature, Scale, and genuine value domain; then extend the predicate explicitly.

**Episteme evaluation.** A method-description review uses clarity, evidence recoverability, source currentness, and relation precision coordinates. A.19 supplies the declared characteristic space; the evaluation pattern contains the defining content for the stop condition, rating interpretation, and improvement decision.

**Cross-scheme comparison.** A built-asset team compares readiness values expressed under different measurement conventions. It first names an admissible normalization into one declared target space. If the use also relates two exact F.17 local senses, it tests the direct F.9 predicate and cites the Bridge only when it obtains, with a separate bounded-use claim and reliance. If the ReferencePlane changes, it cites the applicable plane relation. A separate A.19.CPM application then binds the compared states, comparator, scope, window, and result.

### A.19:5.6 - Bias-Annotation

A.19 corrects feature-vector bias: a list of numbers, labels, or dashboard fields is not yet a `CharacteristicSpace`. The space exists only when each slot binds a `U.Characteristic` to a Scale and genuine Scale value set with declared meaning and optional overlays. Partial-observation and applicability statuses remain with the consumer.

It also corrects consumer-pattern bias. A.19 is the pattern for the reusable space and semantic predicate values. Each current gate, evaluation, comparison, selection, assurance, dashboard, or portfolio claim binds its own application, scope, window, result, evidence use, and publication consequences under the applicable pattern; consuming the A.19 values creates no private space or predicate kind.

### A.19:6 - Conformance checks

Start with the base declaration. If the current job is only to declare a local space, or that space plus one predicate, stop after these checks.

**Base declaration**

1. The ordered basis names every slot's Characteristic, Scale, admissible value set, position, and subject/input signature.
2. A complete point contains one genuine Coordinate from each Scale. Missing, censored, unknown, and inapplicable inputs remain separate observation or evaluation statuses.
3. No order, topology, distance, normalization, indicator, aggregation, or comparison is implied. Any one that is present is named explicitly.
4. When a `CharacteristicSpacePredicate` is present, its input variable, domain, Coordinate projection, Boolean expression, cut or band, composition, and polarity are recoverable. A binary comparison remains separate.
5. The declaration contains no hidden evaluation result, gate decision, evidence relation, publication object, or permission to act.

**Triggered additions**

Apply a row only when its trigger is present.

| Trigger | Additional check |
| --- | --- |
| Subspace or product | List the carried slots and Scale meanings. Projection uses the type-correct composition law; a product performs no aggregation. |
| Embedding or lossy mapping | An embedding is point-injective and preserves every named structure. A many-to-one normalization, binning, dropped Coordinate, or other coarse-graining is a lossy mapping or projection with preserved and lost distinctions stated. |
| Normalization, quotient, equality, or join across spaces | Cite the admissible A.19.UNM instance, Scale conditions, domain, and validity window. Compare in one declared target space. Use a quotient or fixed chart when the claimed equality or join depends on normalization invariance; otherwise report the values as incomparable. |
| Same-space state comparison | Compare Coordinates directly only when both states use the same declared space, slot meanings, Scale metadata, and state definition. A.19.CPM separately binds the comparator, scope, plane, window, application, and result. |
| Indicator use | Cite the `IndicatorChoicePolicy`; a normalized value is not automatically an indicator. |
| Cross-reference-scheme or cross-plane use | Cite an F.9 Bridge only for two exact F.17 local senses when its predicate obtains, and state the bounded-use claim separately; `CL` is optional. Cite the applicable plane relation separately. Name matching, context/scheme/plane difference, and an expired mapping establish neither relation nor admissibility. |
| Predicate evaluation or state assertion | Bind the actual subject/input tuple and available Coordinates or governed projection. The consumer separately states its scope, relevant slice, reference scheme and plane, applicability or evaluation window, operation application, typed result, and partial-input rule. |
| Changed predicate, mapping, or overlay | Keep earlier assertions tied to the earlier values. A new declaration does not retroactively rewrite a historical assertion or result. |
| Sensitivity, robustness, continuity, stability, or order-preservation claim | Name the exact function or predicate use, overlay, domain, assumptions, and bound or law required by the consumer's policy. Add C.16 uncertainty and calibration limits when measured Coordinates are relied on. |
| Dynamics prediction used in comparison or gating | Apply A.3.3 and the direct consumer's policy for model edition, domain, horizon, currentness, error or uncertainty, observation, sensitivity, stability, and normalization-composition conditions. No one regularity property grants authority. |
| Gate, permission, evidence, or assurance use | Use the direct gate, authority, evidence, and assurance patterns for their applications and results. A.19 contributes only the cited space, predicate, mapping, or overlay and requires no persistence identifier or log by itself. |

Choose the needed expression form through C.2.3. Automation or assurance can require more explicit identifiers and records under their direct patterns, but it does not enlarge the base A.19 declaration.

### A.19:7 - Common Anti-Patterns and How to Avoid Them

_The following are common modeling mistakes (“anti-patterns”) related to measurement spaces, and how to correct them:_

-   **“Same label ⇒ comparable.”**
    ✗ Assuming two `Ready` labels or two same-named coordinates are comparable across different reference schemes or planes.
  ✓ Normalize into one declared target space. Cite an F.9 Bridge only when its predicate obtains between two exact F.17 local senses, state the bounded-use claim and reliance separately, and cite the applicable plane relation for a ReferencePlane crossing. Let CPM state the comparison scope, comparator, plane, and window.

-   **“Compare before common-space mapping.”**
    ✗ Comparing values directly across different scales, e.g. _Drift\_A = 5°C vs Drift\_B = 5°F_ as if they were the same.
  ✓ **Normalize to common units first:** e.g., apply the Fahrenheit-to-Celsius **NormalizationMethod** _m_(T_F) = (T_F - 32) × 5/9 to convert all data to °C, **then** compare the drift values. Always **normalize into one space** before comparing magnitudes.

- **“Checklist = method sequence.”**
  - Wrong: `Ready` means “do Step 1, then Step 2.”
  - Repair: let the checklist state the conditions that must hold. Put the way of reaching them in a separate Method or MethodDescription, planned occurrences in a WorkPlan, and what actually happened in Work. Evidence separately supports an assertion or evaluation result; it is not the condition itself.

-   **“Retro-fix past assertions.”**
    ✗ Going back to edit or reinterpret old StateAssertions after changing a threshold or NormalizationMethod (e.g. “We updated the criteria, let’s ‘fix’ last quarter’s records to match”).
    ✓ **Never alter historical assertions:** **Leave history as-is.** If criteria change, issue new assertions under the new criteria going forward, and if needed, explicitly **version** the **NormalizationMethod** or **UNM** declaration or checklist. Past assertions remain valid for the old version and their time; new ones apply henceforth. This ensures auditability and avoids erasing or rewriting what was true under earlier standards.

**C.27 temporal-claim relation.**

- C.27 may flag: a rate or rate-change claim that needs base characteristic, scale and unit, time base or sampling window, transformation or finite-difference method, evidence, and admissible use.
- This pattern keeps: CharacteristicSpace coordinate discipline and the measurement-coordinate relation carried with C.16.
- Non-admissible use: words such as velocity, acceleration, throughput, cadence, or recovery speed do not by themselves establish a Characteristic, Scale, or measurement method.
- Use boundary: when the interpretation governs the current claim, cite `baseCharacteristicRef`, the relevant measure reference, sampling window, construction method such as `DHCMethodRef`, and the C.16 measurement or construction relation reference; C.27 does not define a parallel measurement system.

**A.19.ECS object-under-improvement evaluation construction relation.**

- A.19 defines `CharacteristicSpace` as an ontological structure: slots, characteristics, scales, value sets, overlays, and comparability boundaries.
- A.19.ECS governs the construction of one object-under-improvement evaluation `CharacteristicSpace` for an object being improved. It is used before `E.22` and `E.23` when no adequate object-under-improvement evaluation exists.
- Existing object-under-improvement evaluation patterns such as `E.21`, `E.9.DA`, `E.2.DA`, and the naming vector inside `F.18` are examples of this construction shape for object kinds under improvement. They keep their own coordinate, value-meaning, and stop-condition definitions.

### A.19:8 - Consequences

| Consequence | Benefit | Cost or boundary |
| --- | --- | --- |
| Coordinate and observation claims become inspectable | A reader can recover the subject/input tuple, slot, Characteristic, Scale, value set, actual Coordinate, partial-input status, window, and mapping references. | Declaring the space and its use takes more work than naming a feature vector or dashboard column. |
| Predicate meaning remains reusable | A criterion survives description, evaluation, scope, and window changes when its semantic components are unchanged. | Authors must name coordinates, scales, operator, cut or band, polarity, and normalization or coordinate-mapping basis. Any semantic Bridge and plane relation are cited separately by the consumer; the bounded-use claim and reliance remain separate from both. |
| Consumer patterns stay bounded | Gates, evaluations, comparisons, selectors, assurance claims, and dashboards use declared spaces and predicates without redefining them. | Each consumer must still declare its own scope, slice, plane, window, result, and evidence use. |
| Dynamics has a typed state space | A dynamics model can say which space its state belongs to without letting A.19 define the dynamic law or time base. | Dynamic laws, evidence, and work consequences must still be governed elsewhere. |

### A.19:9 - Rationale

A characteristic space is the minimal object that keeps multi-characteristic claims from becoming loose feature lists. The pattern binds each characteristic to a scale and value set, then lets neighboring patterns consume the declared space for state predicates, thresholds, comparisons, gates, evaluations, assurance, dashboards, and dynamics models.

The separation matters because a threshold or region is not the space, yet its semantic predicate is reusable before and after any one evaluation. A.19 is the pattern for that by-value predicate; comparison, acceptance, selection, assertion, evidence-use, publication, and decision occurrences and results require their own current claims under the applicable patterns.

### A.19:10 - SoTA-Echoing

Measurement and evaluation practice requires explicit variable definitions, subject/input roles, Scales, units, value ranges, partial-input treatment, normalization, and comparability before multi-criteria comparison is meaningful. A.19 adapts that discipline by treating the CharacteristicSpace and its genuine Coordinate values as the declared ontic object, while observation absence, scoring, indicator choice, normalization use, and assurance remain with their direct patterns.

Dynamical-systems and state-space practice supplies the useful hook: a dynamics model needs a declared state space, but the state space does not itself define the law, time base, observation model, or intervention. FPF keeps that boundary so that characteristic-space declarations can be reused across system, episteme, evaluation, and architecture work without smuggling consumer semantics into the space.

### A.19:12.1 - C.29 mathematical-lens use relation

> If topology, order, distance, product, subspace, or embedding is only a `CharacteristicSpace` overlay or operation, stay in A.19. If that mathematical structure is used to explain, predict, assure, compare across reference schemes or planes, relate independently governed values, or carry a reusable explanation, add the applicable C.29 lens-use result. C.29 does not replace the A.19 space or predicate declaration.

### A.19:12.2 - Source-use basis and currentness

A.19 is primarily internal-kernel doctrine, not an external SoTA-import pattern. The accepted FPF basis for `U.CharacteristicSpace` is the chain of `A.17` for `U.Characteristic`, `A.18` for scale and value discipline, `C.16` for measurement and coordinate evidence, `A.19.UNM` for normalization methods, `C.29` when a mathematical lens is used beyond local space declaration, and `E.24` for ontic-head and slot-relation discipline.

Currentness is inherited through that chain. Reopen A.19 when a subject pattern changes Characteristic identity, Scale semantics, value-set meaning, subject/input arity, partial-observation discipline, normalization admissibility, comparability, Bridge discipline, mathematical-lens boundary, or ontic slot discipline. Do not reopen A.19 merely because one consumer adds a score table, dashboard, evaluation report, certification interface, or portfolio view that uses the space.

### A.19:13 - Relations - Ontic Relations and Consumer Boundary

- **Builds on:** `E.24` for ontic-head discipline, `A.6.5` for declaration SlotSpecs, `A.17` and `A.18` for characteristic and scale discipline, `A.2.6` for `U.ClaimScope` membership over exact `U.ContextSlice` values, and `C.16` for measurement and coordinate claims.
- **Coordinates with:** `A.19.CPM` for comparator and comparison scope; `A.19.SelectorMechanism` for explicit selection conditions; `G.4` and other direct consumers for typed predicate evaluation; `F.9` only for an obtaining semantic Bridge between two exact F.17 local senses; the applicable plane pattern for a plane relation; `A.10` and G.11 for provenance and currentness; and `C.2.1` when a predicate description or evaluation assertion is itself an episteme.
- **Does not replace:** a consumer's evaluation, comparison, selection, evidence use, gate, assurance, view, or publication.

### A.19:End

