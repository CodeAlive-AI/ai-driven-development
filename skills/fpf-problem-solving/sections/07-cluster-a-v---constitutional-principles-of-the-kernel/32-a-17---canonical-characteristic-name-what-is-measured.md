## A.17 - Canonical “Characteristic” (A.CHR-NORM): Name What Is Measured

> **Status:** Stable

**Use this when.** A measurement description leaves unclear what aspect is measured, which entities it concerns, or how its value differs from a Score. First name the Characteristic and its bearer or tuple; then recover the Scale and any calculation or preference used. An already clear domain description needs no extra terminology table.

### A.17:1 - Context

A measurement needs a recognizable aspect, its bearer or participants, and a way to express the result. C.16 supplies the CSLC discipline: define a **Characteristic**, choose a **Scale** and any applicable **Unit**, and report a **Level/Value** as a **Coordinate** on that Scale. A **ScoringMethod** may then map Coordinates to a **Score** for a declared evaluation. A.17 fixes the vocabulary and arity of the measured aspect so that terms such as axis, dimension, feature or metric do not hide these different meanings.

### A.17:2 - Problem

When measurement concepts are not kept rigorously distinct, several issues arise:

-   **Polysemy at the anchor.** Teams say “dimension” or “feature” but mean slightly different things, so the very trait being measured is ambiguous.

-   **Arity mistakes.** A relational quality (e.g. similarity between two items) might be treated as if it were an intrinsic property of one item, or vice versa, leading to logical errors.

-   **Expression conflation.** The aspect being measured is often mixed up with its expression – for example, using “scale” or “axis” to mean both the quality _and_ its unit or range. This leads to **unsafe arithmetic** (averaging ordinal ranks, comparing raw numbers from incompatible scales, etc.) because values get interpreted out of context.

### A.17:3 - Forces

- **F1 — Recoverable measured aspect.** A reported number needs the answer to “value of what?” before it can be interpreted as a measurement.

-   **F2 – Arity clarity.** Some characteristics apply to a single entity (e.g. its mass or length), while others inherently relate multiple entities (e.g. distance between two points, coupling between modules, agreement between judges). If arity isn’t explicit, claims and calculations become corrupted.

- **F3 — Scale integrity.** Scale types constrain meaningful operations. A numerical encoding of ordinal ranks does not by itself justify their arithmetic mean; interval and ratio values retain their applicable unit and transformation rules. A calculation also needs the relation or ScoringMethod that gives its result meaning.

- **F4 - Combining measurements.** A measurement model relates quantities to obtain another quantity; a ScoringMethod combines values into a score for a declared evaluation. Each calculation needs its applicable relation and Scale operations. A common numerical encoding alone supplies neither.

- **F5 — Disciplinary meanings.** The same distinctions can describe a lab temperature, a software-cohesion rating or a judged performance. Each retains its domain definition, bearer, Scale and conditions of assessment.

- **F6 - Revisable state descriptions.** Development can change the Characteristics and state distinctions that matter. The description should support the changes, returns and further questions needed by the practice, including revision of its state space or transition law.

### A.17:4 - Solution

**Establish “Characteristic” as the one canonical construct for “what is measured.”** In every FPF context, the _aspect or trait_ being measured MUST be referred to as a **Characteristic**. This term replaces “axis” or “dimension” when they are used as names for the measured aspect; Plain aliases must keep that mapping clear. By fixing a single name and schema, we cleanly separate a **Characteristic** from its **Scale** (and **Unit**), and from any observed **Value/Level** on that scale. The solution also differentiates single-entity vs multi-entity cases and binds all measurements to the standard CSLC sequence.

To enforce this solution, the following rules apply:

-   **A17-R1 (Canonical term).** In all normative models and specifications, the measured aspect **SHALL** be referred to as a **Characteristic**. “Axis” and “Dimension” are not technical substitutes for the measured aspect.

-   **A17-R2 (Entity vs. relation subtype).** Each Characteristic **MUST** declare its intended _arity_. An **Entity-Characteristic** applies to exactly one bearer (e.g. _Temperature_ of a reactor, _Evolvability_ of a software module), whereas a **Relation-Characteristic** applies to an ordered tuple of two or more bearers (e.g. _Distance_ between two sensors, _Coupling_ between modules, _Agreement_ among reviewers). The arity is part of the definition and **must be explicit** wherever it’s not obvious from naming.

- **A17-R3 (Characteristic space).** When several Characteristics form a declared space, identify their slots, Scales and admissible values under A.19. State the constraints and additional structure required by its use. Use A.3.3.CC when compatible combinations must be constructed: it selects variables and constraints and compares implicit descriptions, parametrizations and finite sets. A.3.3 completes the state and transition account when the question concerns modeled change.

- **A17-R4 (Lexical guardrails).** When naming the measured aspect, its scale, its value or position, or an evaluative result, normative text **SHALL** use the corresponding governed term: Characteristic, Scale, Unit, Level/Value, Coordinate, Score, Normalization or ScoringMethod. Do not use axis, dimension, metric, grade or property as an undeclared substitute for those constructs. A disciplinary term naming another defined subject keeps that meaning; a mathematical dimension or metric, for example, is not renamed Characteristic. A Plain alias may be used when its mapping is clear. Apply E.10 to an unresolved lexical question.

- **A17-R5 (Symbol policy).** The **Γ_** prefix is reserved for algebraic operators under E.10:8.3 and E.10.P. Each operator retains its defining laws, including those for holonic composition or a declared scale-lawful fold under A.19.ULSAM. **𝒢** denotes a ScoringMethod from Coordinates to a Score. Documents **SHALL NOT** reuse Γ for a ScoringMethod.

- **A17-R6 (Scale order and preference).** For an ordered Scale, use its order to compare values of the Characteristic: a higher temperature value means hotter. A use that ranks values by desirability **SHALL** declare its preference rule, such as higher-is-better, lower-is-better, a target or range, or another ordering. Describing or comparing magnitudes requires no preference rule.

- **A17-R7 (Scoring against preference).** A ScoringMethod **SHALL** state how its score order represents the declared preference. Where one input is higher-is-better or lower-is-better, improving that input while holding the others fixed **MUST NOT** worsen the score, for admissible inputs under the stated conditions. Target-based preference is checked against its declared target or loss rule; the preferred direction may change across the target. A quantity calculation or unit conversion uses its measurement relation and Scale rules under A.18/C.16.

- **A17-R8 (Arity declaration).** Authors **SHALL** mark a Characteristic as **`U.EntityCharacteristic`** (applies to exactly one bearer) or **`U.RelationCharacteristic`** (applies to an ordered tuple of two or more bearers). Examples: *Cohesion* → entity‑level; *Coupling* → relation‑level.

- **A17-R9 (Relational scale anchors).** For relation‑level cases, the Scale’s admissible values **SHALL** be defined over the **tuple** domain (e.g., distances, similarities, inter‑role latencies). Ambiguity that re‑reads a relational Characteristic as unary is **forbidden**.

- **A17-R10 (Characteristic and description).** Distinguish the Characteristic from an episteme that describes it. A rubric, catalogue of levels or examples can contribute to that description; identify a separate episteme under C.2.1 when the receiving use needs its claim content, EntityOfConcern and effective ReferenceScheme.

#### A.17:4.1 - CharacteristicSpace & Change Reasoning *(Normative/Clarifying)*

**R17 - State-space use.** When a change model uses a CharacteristicSpace, declare its Characteristics, Scales, units and admitted combinations under A.19. Add topology, distance or another structure when the inference relies on it.

**R18 - Allowed changes and state recognition.** For a model of change, state the allowed continuations and their conditions through A.3.3. Use a state predicate or checklist when the receiving use needs to recognize a condition. A.2.5 governs the particular case of a condition on an assignment to a system role; a gate or assurance use supplies its own required support.

**I7 — Vector interpretation.** A **U.Coordinate** vector may collect multiple coordinates for multi‑Characteristic reasoning; composition into a single Score, if desired, is an **explicit new 𝒢** on that vector.

### A.17:5 - Archetypal Grounding (System & Episteme Examples)

**In a physical system (`U.System`):** Consider a **Distance** Characteristic defined for a pair of physical objects. For example, two machines in a factory have a Distance of 3.5 meters between them. Here _Distance_ is a Relation-Characteristic (applies to the pair), with an associated Scale (e.g. a ratio scale in meters), and the measured 3.5 m is a **Coordinate** on that scale. If we instead look at an **Engine Temperature** Characteristic (unary), a particular engine might have a Temperature of 350 K at some moment – _Temperature_ (the Characteristic) is clearly separated from how it’s measured (Scale in Kelvin) and the reading (350, a Coordinate on that scale). A value of 360 K is hotter than 350 K. Whether it is preferable depends on the intended operation: heating and cooling can prefer opposite changes while using the same temperature Scale.

**In an epistemic context (`U.Episteme`):** Consider a local Characteristic describing which requirements of a specification-expression rubric are met. Its ordered levels can require stable terms; stable terms plus explicit acceptance predicates and interpretation; and all those conditions plus expressed derivations for specified obligations. The criteria are nested by declaration. A specification at the last level satisfies the earlier expression requirements, but this supplies neither a universal rank of languages nor evidence that its derivations were checked. C.2.3 governs the formality assessment and any mapping to this local summary. The Characteristic names what is assessed, the Scale defines its levels and order, and the Coordinate reports the document's assessed level. Comparisons use that same rubric; its ordinal encoding alone does not justify averaging the levels. For a quantitative example, define the local Characteristic as the proportion of an article's reviewed claims meeting a stated verification criterion. If 85 of 100 reviewed claims meet it, the Coordinate is 85% on the proportion Scale. Retain the reviewed set, criterion and assessment method; this result does not by itself estimate the reliability of unreviewed claims.

### A.17:6 - Bias-Annotation

A shared term can conceal different measured aspects. When adapting a disciplinary term, recover its bearer or tuple, Characteristic and Scale before reusing a value. Quantitative and qualitative measurements retain the different operations their Scales allow. Development may require revising the selected Characteristics and the model relating their changes; A.3.3 supplies that construction.

### A.17:7 - Conformance Checklist

When authoring or reviewing FPF-compliant measurements, check the following:

1.  **Declared Characteristic:** Have you explicitly named a **Characteristic** for each aspect being measured, instead of using generic terms? (e.g. use _“Reliability”_ as a Characteristic name rather than saying “this dimension”).

2.  **Arity Explicit:** Is it clear whether the Characteristic is unary or relational? If a metric involves a relationship, are the participating entities (pair, tuple, etc.) identified in its definition?

3.  **Separate Scale/Unit:** For each Characteristic, have you defined the **Scale** (and **Unit**, if applicable) separately, rather than embedding units or ordinal terms in the name of the Characteristic? (e.g. _“Length (m)”_ should be captured as Characteristic = _Length_, Unit = _meter_).

4.  **Scale-appropriate operations:** Are you only performing comparisons or calculations that make sense for the declared scale type? (An ordinal encoding alone licenses no arithmetic mean; interval/ratio calculations retain their transformation and unit conditions.)

5. **Calculation or scoring:** Does a quantity calculation use a stated relation with compatible quantities and Scale operations? If values are combined into an overall Score, does the ScoringMethod state the preference it represents and preserve the declared preference in its score order?

6. **Canonical terminology in use:** Do formal descriptions distinguish Characteristic, Scale, Level/Value, Coordinate, Score, ScoringMethod and Unit, with any Plain alias explicitly mapped? Keep disciplinary terms that name different defined subjects instead of mechanically renaming them Characteristic.

7. **State use:** When Characteristics describe modeled change, are their admitted combinations and the transition law sufficient for the question under A.3.3? If a state condition is being recognized, is its predicate and required support determined by that receiving use?

Lexical checks can locate inconsistent terms; deciding the measured aspect, admissible operation and applicability requires the corresponding semantic rules.

### A.17:8 - Consequences

The distinctions support the following uses:

- **Recoverable measurement meaning:** a reader can identify the Characteristic to which a reported value belongs.

- **Separate aspect and expression:** the Characteristic names what is measured; the Scale defines its admissible values and structure, with a Unit where applicable.

- **Recoverable participants:** unary and relational Characteristics expose whether a value concerns one bearer or a tuple, such as the distance between two objects.

- **Cross-domain construction:** temperature and a verified-claim proportion can each be described through Characteristic → Scale → Coordinate. Their shared structure supplies no common desirability order. Combining them into a Score requires an explicit ScoringMethod with its preference and applicability conditions under A.19.USCM.

- **Revisable change accounts:** Characteristic meanings and Scales remain explicit as a state model changes. Revising a constraint, input or law can change which states are reachable; adding a Characteristic can supply predictive information that an earlier description omitted.

The cost is identifying disciplinary meanings and revising ambiguous descriptions. A shared term reduces one source of confusion; it does not establish measurement accuracy, evidence quality or a justified scoring model.

### A.17:9 - Rationale

The distinction between Scale order and preference follows the different questions they answer. [VIM3 §1.27](https://jcgm.bipm.org/vim/en/1.27.html) orders quantity values by magnitude. Evaluation adds a judgement about which values are desirable for a use. [VIM3 §1.22](https://jcgm.bipm.org/vim/en/1.22.html) supplies the separate notion of a relation between quantities. FPF adopts these measurement distinctions and places use-dependent preference with A.19.ECS and the applicable comparison or scoring Method.

A.7 keeps the measured aspect distinct from its description and result. For example, a requirement category, a measured Characteristic and an evaluative Score may all have been called a dimension; identifying their different functions lets the reader select the corresponding rule.

The historical distinction among nominal, ordinal, interval and ratio Scales identifies which transformations preserve the represented meaning. FPF uses those distinctions to constrain calculations. A domain model or ScoringMethod may justify an additional operation; a shared numerical encoding alone cannot.

Distinguishing entity and relation Characteristics keeps the bearer of a measurement recoverable. A.3.3 can use the declared Characteristics to describe a state; an assurance argument can name the aspect for which it uses a measurement. Quantity calculations use their mathematical relation and applicability conditions; evaluative scores additionally need the preference that the scoring method represents. This lets a reader distinguish a derived physical value from a judgement about that value.

The question determines the required state description. A model may need repeated states, several continuations or a stopping condition. Development can revise that model and open new questions. A state-recognition checklist serves a use that needs such recognition; it does not supply the transition law.

### A.17:10 - Relations

- **Builds on:** C.16 for measurement construction and A.7 for the distinctions among a Characteristic, its description and its result.

- **Constrains:** measurement claims in other patterns. A.3.3 state variables, A.2.3 promise acceptance conditions and B.3/D.3 assurance calculations retain the Characteristic, Scale, participants and applicable calculation rule required for their use.

-   **Coordinates with:** **A.18 (CSLC-KERNEL)**, which defines the minimal **Characteristic/Scale/Level/Coordinate** Standard in detail. A.17 provides the vocabulary and basic distinctions (what is a Characteristic, and its arity), while A.18 applies this to ensure each measurement template is well-formed. Also coordinates with **C.2 KD-CAL** and the **A.19/C.16 characterization stack**; those patterns use the Characteristic/Scale constructs to build domain-specific metrics (e.g. knowledge quality scores) and rely on A.17’s canon for consistency.

- **Coordinates with:** E.10 for governed terms and clear Plain aliases; F.7 for displaying source-local comparisons; F.9 for any justified cross-context alignment or Bridge. A common name alone establishes no equivalence between disciplinary meanings.

### A.17:End
