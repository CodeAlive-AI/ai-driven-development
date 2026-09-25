## A.17 - Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured

### A.17:1 - Context

To have reproducibility and explainability there is a need to **measure** various aspects of systems or knowledge epistemes or publications. A dedicated measurement backbone (see **C.MM‑CHR**, Measurement & Metrics Characterization) already exists, prescribing the **CSLC discipline** – i.e. define a **Characteristic**, choose a **Scale** (with a **Unit** if applicable), record a **Level/Value**, and thus obtain a **Coordinate** on that scale, optionally mapping to a **Score** via a **ScoringMethod (USCM)**. However, historically multiple near-synonyms (“axis”, “dimension”, “property”, “feature”, "metric") have been used interchangeably for “what is being measured,” and often the _aspect itself_ gets conflated with _how it is expressed_ (units, ranges, labels). This pattern enters the FPF **Kernel lexicon** to **canonize a single term** for the measured aspect and enforce a clear separation between **what** is measured and **how** it is measured.

### A.17:2 - Problem

When measurement concepts are not kept rigorously distinct, several issues arise:

-   **Polysemy at the anchor.** Teams say “dimension” or “feature” but mean slightly different things, so the very trait being measured is ambiguous.

-   **Arity mistakes.** A relational quality (e.g. similarity between two items) might be treated as if it were an intrinsic property of one item, or vice versa, leading to logical errors.

-   **Expression conflation.** The aspect being measured is often mixed up with its expression – for example, using “scale” or “axis” to mean both the quality _and_ its unit or range. This leads to **unsafe arithmetic** (averaging ordinal ranks, comparing raw numbers from incompatible scales, etc.) because values get interpreted out of context.

In summary, projects lacking a canonical terminology for metrics risk miscommunication and pseudo-quantitative operations. Measurements of physical quantities, architectural attributes, or performance scores end up on **incommensurate rails** due to inconsistent naming and handling.

### A.17:3 - Forces

-   **F1 – Single anchor of meaning.** Any numeric value is meaningless unless one can ask “value of _what_?”. The measurement’s meaning must be anchored in a single clearly named aspect.

-   **F2 – Arity clarity.** Some characteristics apply to a single entity (e.g. its mass or length), while others inherently relate multiple entities (e.g. distance between two points, coupling between modules, agreement between judges). If arity isn’t explicit, claims and calculations become corrupted.

-   **F3 – Scale integrity.** Different kinds of scales permit different operations – e.g. you can average temperatures on a common interval or ratio scale but not ranks or grades (ordinal scale) without losing meaning. If one mixes values without regard to scale type or units, the result is nonsense (**pseudo-arithmetic**).

- **F4 - Combining measurements.** A measurement model relates quantities to obtain another quantity; a ScoringMethod combines values into a score for a declared evaluation. Each calculation needs its applicable relation and Scale operations. A common numerical encoding alone supplies neither.

-   **F5 – Transdisciplinarity.** The measurement framework should work for **any domain**. The same conceptual scaffold must serve physical science (e.g. lab temperature readings), software engineering (e.g. module cohesion ratings), and even subjective assessments (e.g. figure-skating scores) without bias. One vocabulary, many CG‑frames.

- **F6 - Revisable state descriptions.** Development can change the Characteristics and state distinctions that matter. The description should support the changes, returns and further questions needed by the practice, including revision of its state space or transition law.

### A.17:4 - Solution

**Establish “Characteristic” as the one canonical construct for “what is measured.”** In every FPF context, the _aspect or trait_ being measured MUST be referred to as a **Characteristic**. This term replaces “axis” or “dimension” when they are used as names for the measured aspect; Plain aliases must keep that mapping clear. By fixing a single name and schema, we cleanly separate a **Characteristic** from its **Scale** (and **Unit**), and from any observed **Value/Level** on that scale. The solution also differentiates single-entity vs multi-entity cases and binds all measurements to the standard CSLC sequence.

To enforce this solution, the following rules apply:

-   **A17-R1 (Canonical term).** In all normative models and specifications, the measured aspect **SHALL** be referred to as a **Characteristic**. “Axis” and “Dimension” are not technical substitutes for the measured aspect.

-   **A17-R2 (Entity vs. relation subtype).** Each Characteristic **MUST** declare its intended _arity_. An **Entity-Characteristic** applies to exactly one bearer (e.g. _Temperature_ of a reactor, _Evolvability_ of a software module), whereas a **Relation-Characteristic** applies to an ordered tuple of two or more bearers (e.g. _Distance_ between two sensors, _Coupling_ between modules, _Agreement_ among reviewers). The arity is part of the definition and **must be explicit** wherever it’s not obvious from naming.

- **A17-R3 (Characteristic space).** When several Characteristics form a declared space, identify their slots, Scales and admissible values under A.19. State the constraints and additional structure required by its use. Use A.3.3.CC when compatible combinations must be constructed: it selects variables and constraints and compares implicit descriptions, parametrizations and finite sets. A.3.3 completes the state and transition account when the question concerns modeled change.

- **A17-R4 (Lexical guardrails).** When naming the measured aspect, its scale, its value or position, or an evaluative result, normative text **SHALL** use the corresponding governed term: Characteristic, Scale, Unit, Level/Value, Coordinate, Score, Normalization or ScoringMethod. Do not use axis, dimension, metric, grade or property as an undeclared substitute for those constructs. A disciplinary term naming another defined subject keeps that meaning; a mathematical dimension or metric, for example, is not renamed Characteristic. A Plain alias may be used when its mapping is clear. Apply E.10 to an unresolved lexical question.

- **A17-R5 (Symbol policy).** **Γ** is reserved for holonic composition; **𝒢** denotes a ScoringMethod from Coordinates to a Score. Documents **SHALL NOT** reuse Γ for a ScoringMethod.

- **A17-R6 (Scale order and preference).** For an ordered Scale, use its order to compare values of the Characteristic: a higher temperature value means hotter. A use that ranks values by desirability **SHALL** declare its preference rule, such as higher-is-better, lower-is-better, a target or range, or another ordering. Describing or comparing magnitudes requires no preference rule.

- **A17-R7 (Scoring against preference).** A ScoringMethod **SHALL** state how its score order represents the declared preference. Where one input is higher-is-better or lower-is-better, improving that input while holding the others fixed **MUST NOT** worsen the score, for admissible inputs under the stated conditions. Target-based preference is checked against its declared target or loss rule; the preferred direction may change across the target. A quantity calculation or unit conversion uses its measurement relation and Scale rules under A.18/C.16.

- **A17-R8 (Arity declaration).** Authors **SHALL** mark a Characteristic as **`U.EntityCharacteristic`** (applies to exactly one bearer) or **`U.RelationCharacteristic`** (applies to an ordered tuple of two or more bearers). Examples: *Cohesion* → entity‑level; *Coupling* → relation‑level.

- **A17-R9 (Relational scale anchors).** For relation‑level cases, the Scale’s admissible values **SHALL** be defined over the **tuple** domain (e.g., distances, similarities, inter‑role latencies). Ambiguity that re‑reads a relational Characteristic as unary is **forbidden**.

- **A17-R10 (Intension vs Description).** The **Characteristic** remains the **Characteristic EntityOfConcern**; any rubric, catalogue of levels, or examples are **Description epistemes**. Keep the intensional Characteristic distinct from its descriptive episteme (cf. `U.Episteme` roles: Object–Concept–Symbol).

#### A.17:4.1 - CharacteristicSpace & Change Reasoning *(Normative/Clarifying)*

**R17 - State-space use.** When a change model uses a CharacteristicSpace, declare its Characteristics, Scales, units and admitted combinations under A.19. Add topology, distance or another structure when the inference relies on it.

**R18 - Allowed changes and state recognition.** For a model of change, state the allowed continuations and their conditions through A.3.3. Use a state predicate or checklist when the receiving use needs to recognize a condition. A.2.5 governs the particular case of a condition on an assignment to a system role; a gate or assurance use supplies its own required support.

**I7 — Vector interpretation.** A **U.Coordinate** vector may collect multiple coordinates for multi‑Characteristic reasoning; composition into a single Score, if desired, is an **explicit new 𝒢** on that vector.

### A.17:5 - Archetypal Grounding (System & Episteme Examples)

**In a physical system (`U.System`):** Consider a **Distance** Characteristic defined for a pair of physical objects. For example, two machines in a factory have a Distance of 3.5 meters between them. Here _Distance_ is a Relation-Characteristic (applies to the pair), with an associated Scale (e.g. a ratio scale in meters), and the measured 3.5 m is a **Coordinate** on that scale. If we instead look at an **Engine Temperature** Characteristic (unary), a particular engine might have a Temperature of 350 K at some moment – _Temperature_ (the Characteristic) is clearly separated from how it’s measured (Scale in Kelvin) and the reading (350, a Coordinate on that scale). A value of 360 K is hotter than 350 K. Whether it is preferable depends on the intended operation: heating and cooling can prefer opposite changes while using the same temperature Scale.

**In an epistemic context (`U.Episteme`):** Consider a **Formality** Characteristic to rate a documentation episteme's rigor. We might define an ordinal Scale with named Levels such as _Informal_, _Semi-formal_, _Formal_. A given specification document can then be said to have _High Formality_ – meaning it occupies the “Formal” **Level** on the Formality Scale. Here _Formality_ (Characteristic) captures _what_ we measure about the document, while the tiered Scale (with qualitative levels) expresses _how_ we categorize it. Because we use an ordinal scale, we can rank documents by Formality, but we would not average “Semi-formal” and “Formal” (avoiding meaningless arithmetic on an ordinal metric). In another knowledge context example, one could define a Characteristic **Reliability** for a knowledge source with a percentage Scale from 0 to 100%. An article’s reliability might be 85% – which is only interpretable by knowing it refers to “Reliability” on a 0–100% Scale (i.e. a specific Coordinate on that Characteristic’s scale).

### A.17:6 - Bias-Annotation

A shared term can conceal different measured aspects. When adapting a disciplinary term, recover its bearer or tuple, Characteristic and Scale before reusing a value. Quantitative and qualitative measurements retain the different operations their Scales allow. Development may require revising the selected Characteristics and the model relating their changes; A.3.3 supplies that construction.

### A.17:7 - Conformance Checklist

When authoring or reviewing FPF-compliant metrics, use the following checklist to ensure **Characteristic normalization** is applied:

1.  **Declared Characteristic:** Have you explicitly named a **Characteristic** for each aspect being measured, instead of using generic terms? (e.g. use _“Reliability”_ as a Characteristic name rather than saying “this dimension”).

2.  **Arity Explicit:** Is it clear whether the Characteristic is unary or relational? If a metric involves a relationship, are the participating entities (pair, tuple, etc.) identified in its definition?

3.  **Separate Scale/Unit:** For each Characteristic, have you defined the **Scale** (and **Unit**, if applicable) separately, rather than embedding units or ordinal terms in the name of the Characteristic? (e.g. _“Length (m)”_ should be captured as Characteristic = _Length_, Unit = _meter_).

4.  **Scale-appropriate operations:** Are you only performing comparisons or calculations that make sense for the declared scale type? (No averaging of ranks, no mixing of units – ensure **ordinal** Characteristics aren’t treated like numbers, and **interval/ratio** values respect zero and units.)

5. **Calculation or scoring:** Does a quantity calculation use a stated relation with compatible quantities and Scale operations? If values are combined into an overall Score, does the ScoringMethod state the preference it represents and preserve the declared preference in its score order?

6. **Canonical terminology in use:** Do formal descriptions distinguish Characteristic, Scale, Level/Value, Coordinate, Score, ScoringMethod and Unit, with any Plain alias explicitly mapped? Keep disciplinary terms that name different defined subjects instead of mechanically renaming them Characteristic.

7. **State use:** When Characteristics describe modeled change, are their admitted combinations and the transition law sufficient for the question under A.3.3? If a state condition is being recognized, is its predicate and required support determined by that receiving use?

_(Failure to satisfy the above indicates a violation of this pattern’s intent. The **LEX-BUNDLE** rules in E.10 provide automated checks for term usage, and MM-CHR templates enforce explicit Characteristic/Scale definitions.)_

### A.17:8 - Consequences

By instituting **Characteristic** as the single term and enforcing the CSLC structure, this pattern yields several positive outcomes:

-   **Unambiguous metrics:** Every measurement has a single, well-defined anchor of meaning – the Characteristic – eliminating guesswork about “what is this number about?”.

-   **Separation of concerns:** We cleanly separate _what_ is measured from _how_ it’s represented. The Characteristic names the quality of interest, while the Scale/Unit defines the expression. A raw value now **means nothing by itself** – it must be read as “X units on the Y scale of Z Characteristic,” which greatly reduces misinterpretation.

-   **Unary vs. relational clarity:** The explicit distinction between Entity-Characteristic and Relation-Characteristic ensures that relational properties (like “distance between A and B” or “consistency among experts”) aren’t mistakenly treated as inherent properties of a single object. This guards against logical errors and data modeling mistakes.

-   **Cross-domain comparability:** All measurements, regardless of domain, follow the same **CSLC** rails. This means a temperature in Kelvin and a reliability score in percent can each be traced through Characteristic → Scale → Coordinate. They can’t be directly compared unless designed to be, which is _good_: any composite scoring must be done via an explicit **SCP** mapping to a common **Score** scale. The pattern thus enables interoperability (through well-defined Score bridges) while preventing illegitimate comparisons.

- **Revisable change accounts:** Characteristic meanings and Scales remain explicit as a state model changes. Revising a constraint, input or law can change which states are reachable; adding a Characteristic can supply predictive information that an earlier description omitted.

There are few downsides. One consequence is that modelers must learn the canonical terms and possibly refactor existing documentation (a short-term effort). Also, enforcing scale integrity means quick-and-dirty aggregate scores are not allowed unless justified via a SCP – this introduces a healthy “pause” to ensure composite metrics are well-founded. Overall, the benefits in clarity and correctness far outweigh the overhead. Teams gain a _lingua franca_ for metrics, and the risk of metric abuse (mixing apples and oranges) is significantly reduced.

### A.17:9 - Rationale

The distinction between Scale order and preference follows the different questions they answer. [VIM3 §1.27](https://jcgm.bipm.org/vim/en/1.27.html) orders quantity values by magnitude. Evaluation adds a judgement about which values are desirable for a use. [VIM3 §1.22](https://jcgm.bipm.org/vim/en/1.22.html) supplies the separate notion of a relation between quantities. FPF adopts these measurement distinctions and places use-dependent preference with A.19.ECS and the applicable comparison or scoring Method.

The Canonical Characteristic pattern is a direct response to recurring measurement pitfalls. By insisting on “one precise name per concept”, it upholds **Strict Distinction (A.7)**, ensuring that the framework never treats two different ideas as one. For instance, earlier practice might label both a requirement category and its score as “dimension,” causing confusion; with A.17, the _aspect_ is a Characteristic and its _score_ is separate, so each idea has its place. This clarity is pedagogically vital (**P‑2 Didactic Primacy**): readers and contributors immediately know what a term means and how to interpret any value associated with it.

The solution also draws on fundamentals of measurement theory (Stevens’ levels of measurement) to prevent misuse. By encoding scale types and unit handling into our patterns, we avoid the “pseudo-quantitative” fallacies – no more averaging things like _risk levels_ or adding up _grades_ as if they were true numbers. In effect, A.17 puts a safeguard around **P‑1 Cognitive Elegance and P‑7 Ontological Parsimony**: we use a minimal, universal set of measurement constructs, and we avoid bloating the conceptual space with domain-specific or redundant terms. One canonical set of terms also makes the framework more teachable and **composable across contexts**, since patterns and projects aren’t inventing new synonyms that others must decipher.

Distinguishing entity and relation Characteristics keeps the bearer of a measurement recoverable. A.3.3 can use the declared Characteristics to describe a state; an assurance argument can name the aspect for which it uses a measurement. Quantity calculations use their mathematical relation and applicability conditions; evaluative scores additionally need the preference that the scoring method represents. This lets a reader distinguish a derived physical value from a judgement about that value.

The question determines the required state description. A model may need repeated states, several continuations or a stopping condition. Development can revise that model and open new questions. A state-recognition checklist serves a use that needs such recognition; it does not supply the transition law.

In summary, A.17 is the linchpin that turns a loose collection of measurement practices into a **coherent, principle-driven system**. It rationalizes the language, thereby rationalizing thought: by speaking in one clear voice about measurements, FPF ensures that every number in the system can be trusted to answer “value of what, on what scale, relative to what context.” This rationale is reflected in improved model integrity and cross-domain trust in the meaning of metrics.

### A.17:10 - Relations

-   **Builds on / Elaborates:** _FPF Core Measurement Schema_ (as outlined in C.16). A.17 lifts the metric template concepts from C.16 into a kernel-level rule. It also reinforces **A.7 Strict Distinction**, by giving each measurement concept a unique name and forbidding overloaded terms.

-   **Constrains:** All other patterns that define or use metrics. For example, **A.3.3 `U.Dynamics`** (system dynamics) must name its state variables as Characteristics with proper scales (it cannot refer to them loosely as “KPIs” without context). Similarly, any **service-level targets / SLO clauses (A.2.3 `U.PromiseContent.acceptanceSpec`)** or **assurance calculations (B.3, D.3 patterns)** that involve measurements are governed by this canonical terminology (no unwarranted synonyms or unit confusion per ISO/IEC 80000, ISO/IEC 25024, QUDT, SOSA/SSN best practices). The pattern’s lexical rules are part of the **LEX-BUNDLE** (E.10) – any FPF-conformant context must adhere to these naming conventions.

-   **Coordinates with:** **A.18 (CSLC-KERNEL)**, which defines the minimal **Characteristic/Scale/Level/Coordinate** Standard in detail. A.17 provides the vocabulary and basic distinctions (what is a Characteristic, and its arity), while A.18 applies this to ensure each measurement template is well-formed. Also coordinates with **C.2 KD-CAL** and the **A.19/C.16 characterization stack**; those patterns use the Characteristic/Scale constructs to build domain-specific metrics (e.g. knowledge quality scores) and rely on A.17’s canon for consistency.

-   **Anticipates:** **E.10 Lexical Discipline** rules – A.17’s enforcement of a single term and controlled aliases is a concrete instance of the lexical uniformity mandated in E.10. It also paves the way for **F.7 Concept-Set Bridges** in Unification patterns, since external ontologies for quantities (ISO 80000, QUDT, etc.) can be mapped cleanly onto FPF Characteristics now that the term is fixed. In short, A.17 is a foundational lexicon pattern that a) ensures internal consistency and b) simplifies alignment with external standards for measurable properties.

### A.17:End
