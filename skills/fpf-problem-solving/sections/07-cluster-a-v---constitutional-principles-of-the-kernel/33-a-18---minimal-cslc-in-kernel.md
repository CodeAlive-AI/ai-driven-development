## A.18 - Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)

> **Status:** Stable

**Use this when.** A reported value or proposed calculation leaves its measured aspect, Scale or permissible interpretation unclear. Recover those meanings from an existing adequate measurement template, or define the missing parts below. CSLC makes the value interpretable; the receiving use still selects its measurement and inference rules.

**Aliases (for narrative use only):** _“Axis”_ (≈ Characteristic), _“Point”_ (≈ Coordinate). _(These colloquial aliases may be used in Plain language **explanations**, but never in formal identifiers or normative text.)_

### A.18:1 - Problem Frame

We often need to **characterize some aspect** of a subject, whether the subject is one entity or a relationship between entities. Whether it’s recording a physical quantity, an architectural property, or a performance rating, the characterization must:

-   remain _domain-neutral_ (work for engineering metrics, subjective scores, etc.),

-   support direct magnitude comparison when values have the same Characteristic and Scale and compatible measurement conditions; a declared conversion may establish that common basis, and

-   accommodate both **ordered tiers** (qualitative levels like Low/Medium/High) and **numeric magnitudes** (continuous or interval values) without mixing them up.

The CSLC pattern (Characteristic–Scale–Level–Coordinate) binds each measurement template to one Characteristic and one Scale. Each reported value belongs to that Scale; a named Level is optional for a discrete or tiered Scale. Reusing the declared meanings lets a receiving practitioner determine whether two readings can be compared.

### A.18:2 - Problem

**Uninterpretable measurements.** A reported “4”, “High” or “9.81” needs its Characteristic, Scale and measurement conditions to be interpreted as a measurement. Across disciplines, “5” could encode an ordinal risk rank, a length in meters or a satisfaction assessment under a stated model. Common failures include:

- In an ordinal Scale such as _Novice < Skilled < Expert_, the order is meaningful; assigning 1 and 3 to its labels supplies no distance that would justify their arithmetic mean.

- Interval and ratio calculations require compatible units, the Scale's transformation rules and the relation being calculated. Combining seconds and minutes requires conversion; a ratio calculation also depends on the meaning of zero.

A practitioner needs the measured aspect, its Scale and the rule for the proposed operation. Otherwise equal numerical encodings can hide incompatible meanings, such as a 4-star rating and 4 seconds. Qualitative tiers need no invented distances between their labels.

### A.18:3 - Forces

- **F1 — Disciplinary interpretation.** Physical measurements and human assessments can use the same structural distinctions while retaining their different domain assumptions and methods.

- **F2 — Comparability and alternative Scales.** Compare values under a common Characteristic and Scale with compatible conditions under C.16. The same Characteristic may use different Scales, such as temperature in Celsius or Kelvin; use a declared conversion when the comparison needs a common Scale.

- **F3 — Scale integrity.** Retain the distinction between category, order, interval and ratio structure. Numerical labels alone establish neither distances nor admissible arithmetic.

- **F4 — Optional named Levels.** A Scale can provide named tiers, such as Technology Readiness Levels or bond credit ratings. A continuous measurement needs no Level labels unless an explicit categorization is introduced.

- **F5 — Method agnosticism.** CSLC defines the Characteristic, Scale and value structure. The applicable domain patterns (e.g. Sys-CAL or KD-CAL) govern how values are obtained through sensing, simulation or expert judgement. C.16 and the receiving use supply the further measurement and comparability conditions.

### A.18:4 - Solution

**Bind each measurement template to one Characteristic and one Scale.** A Coordinate is one value on that Scale; a named Level is optional when the Scale supplies discrete categories or tiers. A performed measurement may attribute one value or a set of values, with uncertainty and measurement conditions under C.16. CSLC types those values; it does not require every observation to determine one exact Coordinate.

> **Exactly one Characteristic + exactly one Scale; each reported Coordinate belongs to that Scale, with an optional named Level.**

Concretely, the parts of this clause are defined as follows:

- **Characteristic:** the aspect being measured, such as Distance, Temperature or a defined quality or reliability aspect. It answers “What are we measuring?”

-   **Scale:** the organized set of possible values that the Characteristic can take, including the type of scale (_nominal_, _ordinal_, _interval_, or _ratio_), the measurement **Unit** (if applicable), and any bounds or structure. The Scale defines “_How are values represented, and which operations does the Scale permit?_” – e.g. “meters on a linear scale from 0 up to 1000” or “ratings 1 through 5 with ordering only”.

- **Coordinate:** one value in the declared Scale's value domain, numeric or categorical. A measurement result may attribute one Coordinate or a set of admissible Coordinates to its subject; C.16 supplies the model, uncertainty and conditions for that attribution. Examples of individual Coordinates are 7.4 on a meter Scale or Expert on the declared expertise Scale.

- **Level (optional):** a named tier or category within a Scale, such as _Low, Medium, High_ on an ordinal Scale. When a continuous measurement is categorized, define the category boundaries; an uncategorized continuous Scale needs no Level labels.

Keep distinct reported Characteristics in separate templates. A quantity calculation or ScoringMethod may combine input values under §4.2; keep each reported output's Characteristic, Scale and governing relation recoverable.



#### A.18:4.1 - Characteristic-space support must stay declared

When a comparison uses a declared space, make the subject kind and active CharacteristicSpace recoverable. Use `SpaceRef` when its identity matters. Different questions about the same subjects may use different spaces; a shared display or atlas label does not determine which one applies.

Keep outcome-side, representation-side and search-side spaces distinct when their difference affects the comparison. Use `OutcomeMapRef` only when the receiving use needs a declared map from a set result into an outcome or effect space. Identify that source result and target space together; the map supplements the view's interpretation rather than selecting a universal space for it.

#### A.18:4.2 - Scale order, preference and calculation

For a magnitude comparison, interpret values under the Characteristic and Scale, including the meaning of their order and units. For a judgement about which value is better, state the preference for that use: higher, lower, a target or range, or another declared rule. A nominal Scale supplies labels without an intrinsic order; a receiving use can still express a preference among them. A descriptive measurement needs no preferred direction.

A mathematical relation can combine quantities into another quantity, as a measurement model does in C.16. Identify that relation, its conditions and the Scale of the resulting quantity. A unit conversion expresses the same quantity on another compatible Scale. A ScoringMethod instead supplies a Score for a declared evaluation and follows A.17-R7's preference rule. For example, multiplying resistance by current gives voltage; ranking designs by cost and reliability requires a choice of preference.

For evaluative comparison or combination across different CSLC templates, the ScoringMethod must declare its Score Scale and output range. Supply finite bounds when the method or receiving use requires boundedness, as specified in A.19.USCM; do not invent bounds for a lawfully unbounded score.

#### A.18:4.3 - Preserve value meaning through change

A Scale is identified by its interpreted values and their domain, the equality or order structure it supplies, and, where applicable, its unit, reference and origin. A label or numeral alone supplies none of these. A Level denotes a value or declared category within that Scale; changing its spelling can preserve the Level, while moving a category boundary changes what it denotes. A Coordinate is a value of that particular Scale, not an independently measured object or the content that attributes the value to a subject. Keep the declared Scale recoverable when writing, comparing or passing Coordinates.

A measurement unit is an adopted reference for expressing quantities of the applicable kind. Its symbol is a representation of that reference. A change of unit can preserve the quantity through an established conversion while changing the Scale-specific Coordinate; an unchanged symbol does not establish that the unit, quantity kind or Scale is the same. A changed measurement model or calibration can change the attributed result without changing the Scale. Recover which interpretation or assertion changed before revising a dependent calculation.

For a proposed replacement, establish the required correspondence of Characteristics and Scales, then apply the conversion or evaluation rule actually used by the receiver. Being a Coordinate on some Scale is insufficient for filling a position on another Scale. Where no classification decision is needed, this exact declaration and correspondence suffice; recurring typed receivers can use the content and space ranges in C.16:5.5.1 and A.19:5.1.1.1. Membership in those ranges does not establish comparability or authorize arithmetic.

### A.18:5 - Archetypal Grounding (System & Episteme Examples)

**In a physical scenario (`U.System`):** Consider an athlete’s long jump. We define a Characteristic **Jump Distance** with a Scale “meters (m)” ranging from 0 upward (ratio scale with meters as the unit). When the athlete jumps and lands at 7.45 m, we record a **Coordinate** of _7.45 m_ for the Jump Distance Characteristic. This ratio Scale permits interpreting a 1.5 m distance difference between comparable jumps.

For another physical measurement, consider **Battery Health** of a device, which might be categorized qualitatively. We could define an ordinal Scale with Levels like _Good, Fair, Poor_ for the Battery Health Characteristic. If a particular device is rated “Poor”, that is a Coordinate on the Battery Health scale (with _Poor_ as the Level name). No arithmetic is done on these labels, but we can order devices by health (Good > Fair > Poor).

**In knowledge-related assessment:** A person's expertise may be assessed on a declared ordinal Scale _Novice < Competent < Expert_. Alice is assessed as Expert in software engineering and Bob as Competent. Their Coordinates are ordered by that rubric; numerical labels alone supply no mean expertise. The bearer here is the person, not the description of the assessment.

For an episteme-related example, a stated probabilistic model and conditioning evidence may assign probabilities 0.95 and 0.7 to two non-exclusive hypotheses. The Characteristic is the probability assigned to each hypothesis under those conditions, and the Scale is [0,1]. A higher value means a higher assigned probability under that model. Combining the values requires the model's joint or conditional relations. Using their product as the probability that both hypotheses hold requires independence under the stated conditioning information. A probability and a statistical confidence level retain their different interpretations; the same numerical encoding does not make them one Characteristic.

### A.18:6 - Bias-Annotation

The CSLC structure supports physical measurements and human assessments by keeping the Characteristic, Scale and reading distinguishable. The chosen measurement procedure supplies the domain assumptions. Scale order describes the Characteristic; an evaluation states which values it prefers for its use. This separation allows a descriptive reading to remain interpretable when the evaluation changes.

### A.18:7 - Conformance Checklist

When defining a new metric template or using measurements, practitioners **SHALL** verify the following:

1. **One Characteristic, one Scale:** Each metric template binds exactly one Characteristic to exactly one Scale. Keep different reported Characteristics in separate templates. A calculated quantity or composite Score may use multiple inputs under §4.2.

2. **Order and preference:** Is the Scale's order interpretable for the Characteristic? When the use judges which value is preferable, is that preference stated? A descriptive magnitude comparison requires only the measurement interpretation. A target-based evaluation states its target and how deviations are compared.

3. **Unit and Level clarity:** State the applicable Unit or dimensionless-value convention and make it recoverable for each quantitative value. Define named Levels within their Scale. A label may occur on different Scales, but the receiving use must be able to recover which meaning applies. Keep the Unit separate from the Characteristic name.

4.  **Scale-appropriate operations only:** Only perform those comparisons or calculations that are valid for the given scale type. For a nominal scale, the Scale supplies equality but no intrinsic order; a use-dependent preference is a separate rule. For an ordinal Scale, its order alone does not justify arithmetic differences between numerical labels. For interval scales, an operation must respect the Scale's admissible changes of origin and unit; differences and appropriate means can be meaningful, while ratios of raw values generally are not. For ratio scales, ratios are meaningful, but further calculation still needs the applicable quantity or scoring relation and its conditions, with compatible units. For example, encoding High as 3 and Medium as 2 supplies no interpretation of their mean, 2.5.

5.  **No bare numbers:** Never present a raw number or value without its context of Characteristic and Scale. If someone sees “42” in your output, they should _also_ see or know “42 of what, measured how.” A reader who is not aware of the metric’s template should not be left guessing what a given value signifies. In practice, this means labeling reports and data with the metric name or identifier so that values can be traced back to their meaning.

6. **Cross-template operations:** For a conversion, recover the relation between compatible Scales, including units. For a quantity calculation, recover the model and its conditions under C.16. For an evaluative comparison or combination, state the ScoringMethod, its preference under A.17-R7 and its Score Scale and output range, including any required bounds. For example, converting 0.5 minutes to 30 seconds preserves duration; combining cost and reliability into a score needs an evaluation rule.

7. **Level optionality:** Use named Levels when they help express the selected Scale's discrete values or non-overlapping categories. Define the categories and their boundaries; leave Level unused for an uncategorized continuous measurement.
8. **Comparability test:** For a direct magnitude comparison, use the same Characteristic and Scale, with compatible measurement conditions under C.16. A declared conversion can establish that common basis. A preference judgement additionally uses its declared preference; changing that preference alone does not change the measurement Scale.

A.17 and E.10 supply the vocabulary. A template can expose missing fields; it does not establish that the declared meanings, measurement model or resulting inference are adequate.

### A.18:8 - Consequences

Adopting the minimal CSLC Standard in the kernel yields a number of benefits:

- **Recoverable value meaning:** Each reported value names or resolves its Characteristic and Scale, with Unit and Level when applicable. C.16 supplies the measurement model, conditions and uncertainty needed to interpret a performed reading.

- **Interpretable comparison and calculation:** A magnitude comparison retains the Characteristic, Scale and measurement conditions that make the values comparable. A valid unit conversion preserves that basis across presentations. A derived quantity uses its measurement model; a composite Score adds the evaluation rule. Readers can therefore question a scoring choice separately from the measurement it uses.

- **Reuse across domains:** temperature, length, code complexity and satisfaction assessments can expose their Characteristic, Scale and Coordinate through the same structure. Their methods and interpretation still need the applicable domain rules.

- **Explicit Scale limits:** categorical assessments and quantitative measurements retain the operations their Scales allow. Named Levels can expose categories without pretending that their numerical labels measure equal distances.

- **Interpretable multi-factor scoring:** A ScoringMethod exposes how its input Coordinates contribute to the Score. Its preference, score order and declared output range allow the reader to examine the weighting or formula and judge whether it represents the intended evaluation.

- **Method selection remains with the measurement:** CSLC can express results obtained by sensing, simulation or judgement. The receiving use still needs the method's assumptions, uncertainty and applicable evidence before relying on a result.

Defining a Characteristic, Scale and measurement method takes work that can be reused. When an existing definition answers the question, use it. When two presentations differ, determine whether a unit conversion supplies a common measurement basis or a different model is needed. Introduce a ScoringMethod when the intended result is an evaluative Score.

Neighboring patterns can reuse the declared Characteristic and Scale meanings. The receiving measurement, comparison, calculation, evaluation or assurance use still applies its own conditions; CSLC conformance alone does not establish measurement adequacy, valid evidence combination or assurance.

### A.18:9 - Rationale

Defining a measurement template makes the aspect, Scale and value meaning available for later use. The receiving practitioner can reuse that definition instead of reconstructing it from the reported number. The following choices support that result:

- **Shared structure, distinct domain rules:** a usability rating and a throughput measurement both identify an aspect, Scale and reading. Their common structure exposes the difference rather than supplying a common calculation or evidence rule.

- **Comparability vs. freedom:** Measurement comparison needs a common interpretation of the Characteristic, Scale and measurement conditions. A unit conversion can establish that interpretation across compatible presentations. Preference answers a further question: which result serves the intended use? The same temperature Scale supports identifying the hotter sample, choosing a cooling intervention or maintaining a target. Only the latter uses add a preferred direction or target rule.

- **Preserved information:** an ordinal Scale states order without asserting distances. An interval or ratio model can support further calculations only when its additional assumptions are justified; wanting an average is not a reason to assume such a model.

- **Optional Levels:** named tiers make category boundaries recoverable where the Scale uses them. A continuous measurement needs no Level labels unless an explicit categorization is introduced.

- **Separate structure and method:** the same CSLC structure can describe measurements made through different methods. Domain measurement patterns supply their procedures, applicability and evidence conditions; sharing the template does not make those methods interchangeable.

### A.18:10 - Relations

- **Extends A.17:** uses its Characteristic vocabulary and entity/relation arity distinction, then binds each template to a Scale and its reported values. A.17 supplies the participant and naming rules; A.18 supplies the CSLC structure.

- **Used by C.16 and A.19:** C.16 supplies measurement methods, models, conditions and uncertainty; A.19 and A.19.CHR use Characteristic and Scale meanings in spaces and characterization templates. CSLC is the shared value structure, not a storage or computation implementation.

- **Supports dynamic reasoning:** A.3.3 uses Characteristics and Scales to specify state variables. Linking a five-level performance rating to a probability needs a justified model or correspondence between their meanings. A ScoringMethod is appropriate when the result is an evaluative Score.

- **Coordinates with assurance patterns:** A receiving assurance or trust claim may use measurements or Scores whose Characteristic, Scale, model conditions and uncertainty are recoverable. CSLC conformance does not establish comparability merely because values share a 0–1 or percentage encoding. Apply B.3 to the named assurance claim; a cross-domain comparison, normalization or aggregation additionally needs its own declared rule and applicable evidence.

- **Lexical and external correspondence:** E.10 governs the measurement vocabulary; A.18 applies A.17's distinction between measurement interpretation and use-dependent preference to CSLC templates. Defined scale types and units make the terms used in quantity measurement recoverable for an F.9 correspondence with external measurement standards.

### A.18:End

---
