## A.18 - Minimal CSLC in Kernel (Characteristic ⟷ Scale ⟷ Level ⟷ Coordinate) (A.CSLC‑KERNEL)

**Aliases (for narrative use only):** _“Axis”_ (≈ Characteristic), _“Point”_ (≈ Coordinate). _(These colloquial aliases may be used in Plain language **explanations**, but never in formal identifiers or normative text.)_

### A.18:1 - Problem Frame

We often need to **characterize some aspect** of a subject, whether the subject is one entity or a relationship between entities. Whether it’s recording a physical quantity, an architectural property, or a performance rating, the characterization must:

-   remain _domain-neutral_ (work for engineering metrics, subjective scores, etc.),

-   support direct magnitude comparison when values have the same Characteristic and Scale and compatible measurement conditions; a declared conversion may establish that common basis, and

-   accommodate both **ordered tiers** (qualitative levels like Low/Medium/High) and **numeric magnitudes** (continuous or interval values) without mixing them up.

In FPF’s kernel, the **CSLC pattern** (Characteristic–Scale–Level–Coordinate) provides the minimal vocabulary and constraints to achieve this. It defines how one **Characteristic** ties to one **Scale**, and how any measured **value** can be treated as a **Coordinate** on that scale (with an optional named **Level** if the scale is discrete or tiered). The context here is the need for a _unified Standard_ so that every single measurement can be interpreted and compared on common grounds.

### A.18:2 - Problem

**Uninterpretable values.** A raw number or label means nothing without knowing **what aspect it measures** and **how it is measured**. The string “4”, the label “High”, or the real number 9.81 convey no insight unless we know **which Characteristic** they pertain to and the **Scale** that gives them meaning. In cross-disciplinary work this ambiguity is magnified: a “5” could be a risk rank (ordinal), a length in meters (ratio), or a satisfaction score (perhaps interval). Common failure modes include:

-   In **ordinal settings** (e.g. expertise levels _Novice < Skilled < Expert_), one can **rank** values but not meaningfully add or average them. Treating ordinal labels like numbers (e.g. averaging _Novice=1, Expert=3_) produces invalid results.

-   In **cardinal settings** (e.g. seconds, meters, kelvins), arithmetic operations do make sense – but only if units are respected and zero is meaningful (for ratio scales). If we strip away units or mix scales (seconds vs. minutes), we again get nonsense.

Without a strict Standard, one team might treat “High” and “Medium” as having a numeric gap, another might average **4** (on a 5-star scale) with **4** (as 4 seconds) because both are “4”. **Inconsistent practices make cross-domain reasoning impossible.** We need a kernel-level solution that _fixes_: (a) the **aspect being measured**, (b) the **scheme by which it’s measured**, and (c) the **type of scale structure** (ordinal vs. metric), _and_ that ensures each reported value is bound to that scheme. At the same time, the Standard should _not_ force artificial numeric detail where it isn’t applicable (e.g. we shouldn’t assign meaningless numbers to purely qualitative tiers just to satisfy a structure).

### A.18:3 - Forces

-   **F1 – Transdisciplinarity.** The pattern must uniformly handle measurements in _physical domains_ (e.g. length, time, temperature), _system attributes_ (e.g. a module’s coupling or reliability), and _human judgments_ (e.g. user satisfaction scores). It needs to be neither overly quantitative (alienating softer domains) nor overly qualitative (lacking precision for hard science).

-   **F2 – Comparability vs. freedom.** We want to compare readings under a common Characteristic and Scale with the compatible measurement conditions required by C.16. At the same time, the system should allow **different Scales for the same Characteristic** when necessary (for example, one project might measure Quality on a 0–5 star scale, another on a 0–100 percentage scale). The pattern must permit such flexibility _without_ letting those differing scales be conflated.

-   **F3 – Ordinal vs. cardinal integrity.** The Standard should preserve the nature of the data: **order-only vs order+distance**. If something is ordinal (ranks, grades), the framework should prevent unwarranted numeric operations on it. If it’s cardinal (real-valued with units), the framework should enable arithmetic but still keep track of units and zero. In essence, it must protect ordinal data from “leaking” into interval arithmetic.

-   **F4 – Named tiers vs. continuous magnitudes.** In many domains, **named Levels** (tiers or grades) are useful – e.g. Technology Readiness Levels or bond credit ratings – whereas in others, a continuous scale is needed. The pattern should support **optional Level labels** (for tiered scales) _without forcing_ every scale to have such labels. In other words, Levels are an add-on for discrete/tiered scales, not a requirement for truly continuous measures.

-   **F5 – Method agnosticism.** The kernel Standard should say _what_ must be defined (Characteristic, Scale, etc.) but **not prescribe how measurements are obtained**. Whether a value comes from a sensor reading, a simulation, or an expert judgment is up to the respective patterns (e.g. Sys-CAL vs. KD-CAL). The pattern must not bake in any process or scoring methodology; it types the reported values, while C.16 and the receiving use supply the further measurement and comparability conditions. This avoids locking in any particular assessment method.

### A.18:4 - Solution

**Bind each measurement template to one Characteristic and one Scale.** A Coordinate is one value on that Scale; a named Level is optional when the Scale supplies discrete categories or tiers. A performed measurement may attribute one value or a set of values, with uncertainty and measurement conditions under C.16. CSLC types those values; it does not require every observation to determine one exact Coordinate.

> **Exactly one Characteristic + exactly one Scale; each reported Coordinate belongs to that Scale, with an optional named Level.**

Concretely, the parts of this clause are defined as follows:

-   **Characteristic:** the aspect or feature being measured (the “CG‑frame” along which comparison is made). It answers “_What are we measuring?_” – e.g. _Distance, Temperature, Quality, Reliability_.

-   **Scale:** the organized set of possible values that the Characteristic can take, including the type of scale (_nominal_, _ordinal_, _interval_, or _ratio_), the measurement **Unit** (if applicable), and any bounds or structure. The Scale defines “_How are values represented, and which operations does the Scale permit?_” – e.g. “meters on a linear scale from 0 up to 1000” or “ratings 1 through 5 with ordering only”.

- **Coordinate:** one value in the declared Scale's value domain, numeric or categorical. A measurement result may attribute one Coordinate or a set of admissible Coordinates to its subject; C.16 supplies the model, uncertainty and conditions for that attribution. Examples of individual Coordinates are 7.4 on a meter Scale or Expert on the declared expertise Scale.

-   **Level (optional):** a named **tier or category** on the scale, used only if the scale is tiered or discretized. For example, an ordinal scale might have Levels _Low, Medium, High_. A Level is essentially a human-friendly label for certain coordinates or ranges. On purely continuous scales, **Level** is not used.

This CSLC structure makes the measured Characteristic and the Scale of each value recoverable, with an optional Level label. Interpreting an actual measurement additionally uses its C.16 model, conditions and uncertainty. Notably, this pattern _forbids bundling multiple characteristics into one metric_ – each metric template is one-characteristic-per-template to keep semantics crisp. If something needs to assess multiple factors, it should be modeled as multiple CSLC metrics or an explicit composite over several CSLC metrics (see §8 below). This one-aspect-one-scale rule makes the value meaning recoverable; comparison additionally requires compatible measurement conditions.

Finally, the solution ensures **tier optionality**: If a domain uses named Levels, we include them; if not, we don’t force it. For example, one can have a _Bug Severity_ Characteristic with Levels {Minor, Major, Critical} on an ordinal scale, whereas a _Length_ Characteristic would have a continuous scale (no predefined levels, just units). Both fit the pattern.

#### A.18:4.1 - Characteristic-space support must stay declared

- When one front, archive, shortlist, or derived tradition view is discussed in one space, declare the object kind and the relevant characteristic space explicitly.
- Use one `SpaceRef` only when the text truly needs to recover which space or typed feature family is carrying the comparison.
- One declared space does not imply that every neighboring line must use the same space.
- Different declared spaces may coexist for the same family when they answer different comparison questions, but the active one must stay recoverable.
- If one atlas-like reading uses several declared spaces over the same palette, front, archive, or shortlist family, say which `SpaceRef` is active in the current reading rather than letting the atlas label hide that choice.
- If one outcome-side declared space/ref is materially different from one representation-side or search-side declared space/ref, keep that difference explicit rather than calling both simply `space`.
- `OutcomeMapRef` is warranted only when the text needs one declared map from the current set result into one outcome-side or effect-side declared space/ref.
- When `OutcomeMapRef` is cited for one atlas-like or cross-scale reading, keep the source set result and the projected outcome-side declared space/ref visible together so the map stays support for the view rather than a replacement default.

#### A.18:4.2 - Scale order, preference and calculation

For a magnitude comparison, interpret values under the Characteristic and Scale, including the meaning of their order and units. For a judgement about which value is better, state the preference for that use: higher, lower, a target or range, or another declared rule. A nominal Scale supplies labels without an intrinsic order; a receiving use can still express a preference among them. A descriptive measurement needs no preferred direction.

A mathematical relation can combine quantities into another quantity, as a measurement model does in C.16. Identify that relation, its conditions and the Scale of the resulting quantity. A unit conversion expresses the same quantity on another compatible Scale. A ScoringMethod instead supplies a Score for a declared evaluation and follows A.17-R7's preference rule. For example, multiplying resistance by current gives voltage; ranking designs by cost and reliability requires a choice of preference.

For evaluative comparison or combination across different CSLC templates, the ScoringMethod must declare a bounded output range for its Score.

### A.18:5 - Archetypal Grounding (System & Episteme Examples)

**In a physical scenario (`U.System`):** Consider an athlete’s long jump. We define a Characteristic **Jump Distance** with a Scale “meters (m)” ranging from 0 upward (ratio scale with meters as the unit). When the athlete jumps and lands at 7.45 m, we record a **Coordinate** of _7.45 m_ for the Jump Distance Characteristic. Here, Jump Distance is the Characteristic, the meter-scale is the declared Scale, and _7.45 m_ is the value (Coordinate). Because this is a cardinal measurement, we can meaningfully say one jump is 1.5 m longer than another, etc. Now consider another metric in the system: **Battery Health** of a device, which might be categorized qualitatively. We could define an ordinal Scale with Levels like _Good, Fair, Poor_ for the Battery Health Characteristic. If a particular device is rated “Poor”, that is a Coordinate on the Battery Health scale (with _Poor_ as the Level name). No arithmetic is done on these labels, but we can order devices by health (Good > Fair > Poor). Both examples illustrate the one-characteristic-one-scale rule: the jump’s distance is not combined with any other aspect; the battery’s health is evaluated on its own defined scale.

**In a knowledge context (`U.Episteme`):** Consider measuring an author’s expertise in a certain domain. We introduce a Characteristic **Expertise Level** for a person, with an ordinal Scale defining tiers such as _Novice, Competent, Expert_. Alice might be assessed at _Expert_ level in software engineering – that’s a **Coordinate** on the Expertise Level scale for the Characteristic “Software Engineering Expertise”. Bob might be at _Competent_. We cannot average Alice’s and Bob’s levels, but we can say the scale is ordered (_Expert_ > _Competent_ > _Novice_). For a more quantitative episteme example, consider a Characteristic **Hypothesis Confidence** for a scientific claim, with a Scale 0–1 (or 0–100%) representing probability or confidence level (ratio scale). One hypothesis might have a confidence of 0.95, another 0.7; these are Coordinates on the Confidence scale. We can compare them numerically (0.95 is higher than 0.7, and 0.95 _implies_ higher confidence), and we could even combine multiple confidence values through Bayesian formulas (if justified) – but crucially, we would only do so in a way that respects their scale (probabilities combined properly, not treated as arbitrary scores). The Expertise Level and Hypothesis Confidence examples show how the CSLC pattern accommodates both an ordinal qualitative measure and a continuous quantitative measure in the knowledge domain, each with one Characteristic and one defined Scale.

### A.18:6 - Bias-Annotation

The CSLC structure supports physical measurements and human assessments by keeping the Characteristic, Scale and reading distinguishable. The chosen measurement procedure supplies the domain assumptions. Scale order describes the Characteristic; an evaluation states which values it prefers for its use. This separation allows a descriptive reading to remain interpretable when the evaluation changes.

### A.18:7 - Conformance Checklist

When defining a new metric template or using measurements, practitioners **SHALL** verify the following:

1.  **One characteristic, one scale:** Each metric **template** binds exactly **one Characteristic** to exactly **one Scale**. If you find a metric trying to cover multiple things at once, split it into separate metrics.

2. **Order and preference:** Is the Scale's order interpretable for the Characteristic? When the use judges which value is preferable, is that preference stated? A descriptive magnitude comparison requires only the measurement interpretation. A target-based evaluation states its target and how deviations are compared.

3.  **Unit and level clarity:** If the Scale is quantitative, specify the **Unit** (e.g. _seconds, meters, %_) and make sure all values include or assume that unit. If the Scale has named Levels, list them clearly and use them consistently. Do **not** use the same label to mean different things on different scales, and avoid using unit terms in Characteristic names (the unit belongs with the scale).

4.  **Scale-appropriate operations only:** Only perform those comparisons or calculations that are valid for the given scale type. For a nominal scale, the Scale supplies equality but no intrinsic order; a use-dependent preference is a separate rule. For an ordinal scale, you can order or rank values but not do math like “A minus B.” For interval scales, an operation must respect the Scale's admissible changes of origin and unit; differences and appropriate means can be meaningful, while ratios of raw values generally are not. For ratio scales, ratios are meaningful, but further calculation still needs the applicable quantity or scoring relation and its conditions, with compatible units. This check prevents logical errors (e.g. averaging “High” (3) and “Medium” (2) and getting 2.5 — which is meaningless).

5.  **No bare numbers:** Never present a raw number or value without its context of Characteristic and Scale. If someone sees “42” in your output, they should _also_ see or know “42 of what, measured how.” A reader who is not aware of the metric’s template should not be left guessing what a given value signifies. In practice, this means labeling reports and data with the metric name or identifier so that values can be traced back to their meaning.

6. **Cross-template operations:** For a conversion, recover the relation between compatible Scales, including units. For a quantity calculation, recover the model and its conditions under C.16. For an evaluative comparison or combination, state the ScoringMethod, its preference under A.17-R7 and its bounded Score output range. For example, converting 0.5 minutes to 30 seconds preserves duration; combining cost and reliability into a score needs an evaluation rule.

7.  **Level optionality respected:** If your Characteristic doesn’t naturally have tiers, don’t force it to have **Level** names (you can leave the Level concept unused). Conversely, if your Characteristic is commonly described in categories, it’s fine to define Levels for clarity. The key is to use the Level field intentionally: either not at all (for truly continuous measures) or in a fixed, **non-overlapping** way (for discrete categories). Do not use “Level” for something that behaves like a continuous value (it would be confusing to assign a label where a number would do, or vice versa).
8. **Comparability test:** For a direct magnitude comparison, use the same Characteristic and Scale, with compatible measurement conditions under C.16. A declared conversion can establish that common basis. A preference judgement additionally uses its declared preference; changing that preference alone does not change the measurement Scale.

_(The above serve as normative checkpoints. Many of these are automatically supported by using the standard metric templates in software: e.g. the system will enforce one Characteristic per template, require a unit for ratio scales, etc. The **Lexical rules** from A.17/E.10 are assumed: use canonical names and notations for all parts of the metric.)_

### A.18:8 - Consequences

Adopting the minimal CSLC Standard in the kernel yields a number of benefits:

- **Recoverable value meaning:** Each reported value names or resolves its Characteristic and Scale, with Unit and Level when applicable. C.16 supplies the measurement model, conditions and uncertainty needed to interpret a performed reading.

- **Interpretable comparison and calculation:** A magnitude comparison retains the Characteristic, Scale and measurement conditions that make the values comparable. A valid unit conversion preserves that basis across presentations. A derived quantity uses its measurement model; a composite Score adds the evaluation rule. Readers can therefore question a scoring choice separately from the measurement it uses.

-   **Flexibility across domains:** The pattern is **transdisciplinary**. It doesn’t matter if the measurement is temperature in Kelvin, length in inches, code complexity in “abstract points,” or user satisfaction on a five-level Likert scale – all are handled uniformly. This makes it easier to plug new patterns for new domains into FPF, since they don’t need special rules for their metrics; they just instantiate the CSLC template in their context.

-   **Ordinal and cardinal handled with equal rigor:** By explicitly classifying scales, the pattern gives ordinal data the respect it deserves (no pretending it’s numeric) and gives ratio data the formal context it needs (units, zero, etc.). This balance means both qualitative assessments and quantitative measurements live side by side, each with their constraints respected. Domains that lean heavily on categorical ratings benefit from the **Level** concept (with no pressure to assign fake numbers), and domains that use real measurements benefit from unit enforcement and type-aware computations.

- **Interpretable multi-factor scoring:** A ScoringMethod exposes how its input Coordinates contribute to the Score. Its preference, score order and declared output range allow the reader to examine the weighting or formula and judge whether it represents the intended evaluation.

-   **Methodological neutrality (and innovation):** Because the kernel imposes no method for obtaining the values – only how to frame them once obtained – patterns and tool builders are free to innovate in how they measure things. The Standard just ensures that once they do, everyone else can understand and use the results correctly. This separation of concerns (what vs. how) accelerates multi-disciplinary collaboration: a social scientist’s observational scale can feed into a systems model without any confusion, as long as it’s couched in the CSLC terms.

Defining a Characteristic, Scale and measurement method takes work that can be reused. When an existing definition answers the question, use it. When two presentations differ, determine whether a unit conversion supplies a common measurement basis or a different model is needed. Introduce a ScoringMethod when the intended result is an evaluative Score.

Neighboring patterns can reuse the declared Characteristic and Scale meanings. The receiving measurement, comparison, calculation, evaluation or assurance use still applies its own conditions; CSLC conformance alone does not establish measurement adequacy, valid evidence combination or assurance.

### A.18:9 - Rationale

The rationale behind A.18 is to enforce _semantic clarity_ at the data level, thereby solving many downstream problems. Without this pattern, one must constantly ask, “What does this number mean? Can I combine these two values?” – questions that have led to many project errors. By building the answers into the framework (“every number knows its unit, scale, and aspect”), we front-load the work and eliminate ambiguity. The solution directly addresses each force:

-   **Transdisciplinarity:** We include both ordinal and cardinal mechanisms so that no discipline’s metrics are left out. This was informed by observing multi-disciplinary teams: e.g., in a single project, a human factors specialist might rate usability (ordinal) while an engineer measures throughput (ratio). A.18 gives them a common language and prevents one from misusing the other’s data. It embodies the idea that _universal structure enables local freedom_: everyone’s metric can plug in, as long as they specify it properly.

- **Comparability vs. freedom:** Measurement comparison needs a common interpretation of the Characteristic, Scale and measurement conditions. A unit conversion can establish that interpretation across compatible presentations. Preference answers a further question: which result serves the intended use? The same temperature Scale supports identifying the hotter sample, choosing a cooling intervention or maintaining a target. Only the latter uses add a preferred direction or target rule.

-   **Ordinal vs. cardinal separation:** The rationale here is guided by measurement theory: we want to preserve information content. Treating ordinal data with only order operations preserves all its information; doing more (like adding them) injects false information. The pattern’s strictness on scale types forces modelers to be honest about what their data can and cannot do. This not only prevents errors but also encourages **best practices** (e.g. if you find you desperately want to average an ordinal score, perhaps you should refine it into an interval scale in your methodology). The outcome is a framework that respects both the **qualitative** and **quantitative** realms appropriately, aligning with **FPF’s Pillar of Pragmatism** – use formalism where it’s justified, but not beyond its limits.

-   **Optional Levels:** Requiring Levels in every case would have been too rigid (not everything has named tiers), but not supporting them would fail domains that rely on them (like maturity models or grading systems). The rationale for making Level _optional_ is to accommodate both. We saw in practice that many metrics naturally form tiers (e.g. technology readiness levels TRL 1–9) and giving them a slot in the model (instead of burying them in definitions) makes those metrics much easier to work with and integrate. Meanwhile, continuous metrics carry no baggage of unused fields. This design was checked against existing standards (like ISO 25024 for quality measures) to ensure we aren’t deviating from industry expectations: indeed, separating the concept (Characteristic) from the scheme (Scale) aligns well with standards, and including an optional categorization aligns with common practice in capability maturity models, etc.

-   **Method neutrality:** The decision to _not_ include any measuring procedures in A.18 (no specific formulas, no mandated evidence type) comes from the principle of separation of concerns. The kernel should provide the _what_ and _how (structurally)_, while neighboring measurement or method patterns provide method-side constraints and evidence expectations. This keeps the kernel lean (**P‑1 Cognitive Elegance**) and allows domain experts to implement whatever method is appropriate, merely committing to wrap their results in the CSLC form. By doing so, we avoid any bias toward empirical vs analytical, or manual vs automated measurements – FPF welcomes all, as long as they conform to the schema. This was rationalized by examining case studies: e.g., some reliability metrics come from formal proofs (analysis), others from testing (empirical) – the kernel can carry both result kinds identically, requiring only that each result says what it measured and on what scale.

In essence, A.18 is the _infrastructure of meaning_ for metrics. It may appear as a simple template, but it’s profoundly enabling. It forces clarity at creation time, so we don’t have to infer or debate meaning at usage time. The pattern’s practical payoff lies in preventing errors that _don’t have to happen_. It encodes lessons from both metrology (the science of measurement) and everyday data science (where unit errors and mis-comparisons are infamous issues). The rationale is backed by these lessons: **fix the interpretation rules in the design, and you eliminate entire classes of confusion and mistakes.** By having this in the kernel, every mechanism – from knowledge scoring to system performance – benefits immediately, and their results become interoperable to a degree that would be impossible without a common structure.

### A.18:10 - Relations

-   **Extends/Uses:** **A.17 (CHR-NORM)** – A.18 explicitly builds on the canonical terminology established in A.17. It uses the term **Characteristic** as defined there (and no other synonyms) and keeps “axis/dimension” from substituting for the measured aspect unless their alias meaning is explicit. It also leverages the Entity-vs-Relation Characteristic distinction from A.17: Section 7.4 of this pattern references tests for disambiguating relational metrics. Essentially, A.17 provides the **lexical and conceptual groundwork** (what a Characteristic is, and the basic vocabulary), while A.18 provides the **structural and normative rules** for linking Characteristics to measurements.

-   **Core foundation for metrics:** This pattern underpins the **Measurement & Metrics Characterization spec (C.MM‑CHR)** – the pattern that implements metric storage and computation. In MM-CHR, every `U.DHCMethodRef` and `U.Measure` follows the CSLC format defined by A.18. By lifting CSLC rules to the kernel, we ensure all FPF patterns (like **KD-CAL** for knowledge dynamics, **Sys-CAL** for systems, or any custom CAL/CHR) share a common approach to metrics. A.18 also informs **A.19 CharacteristicSpace**, **A.19.CHR**, and **C.16 MM-CHR**, which carry measurable property templates and composite characterizations.

- **Supports dynamic reasoning:** A.3.3 uses Characteristics and Scales to specify state variables. Linking a five-level performance rating to a probability needs a justified model or correspondence between their meanings. A ScoringMethod is appropriate when the result is an evaluative Score.

- **Coordinates with assurance patterns:** A receiving assurance or trust claim may use measurements or Scores whose Characteristic, Scale, model conditions and uncertainty are recoverable. CSLC conformance does not establish comparability merely because values share a 0–1 or percentage encoding. Apply B.3 to the named assurance claim; a cross-domain comparison, normalization or aggregation additionally needs its own declared rule and applicable evidence.

- **Lexical and external correspondence:** E.10 governs the measurement vocabulary; A.18 applies A.17's distinction between measurement interpretation and use-dependent preference to CSLC templates. Defined scale types and units make the terms used in quantity measurement recoverable for an F.9 correspondence with external measurement standards.

### A.18:End

---
