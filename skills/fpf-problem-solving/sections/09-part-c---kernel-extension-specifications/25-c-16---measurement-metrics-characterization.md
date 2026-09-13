## C.16 - Measurement & Metrics Characterization (MM‑CHR)

> **Status:** Stable
> **Type:** Pattern

**Use this pattern when.** Use C.16 to make a reading interpretable or to construct the model needed for a proposed measurement. Start with what is being measured and how the procedure relates it to an indication.

**What goes wrong if missed.** Raw output, indication, actual subject state, measurement result, diagnosis, and criterion verdict collapse into one number; model and calibration assumptions disappear; uncertainty is laundered away; and a dashboard or evidence link is mistaken for work, result, assurance, or decision authority.

**What this buys.** A measurement model that connects indications to what is being measured, or a stated ambiguity that changes what to do next. For a performed measurement, the resulting account identifies the attributed values, uncertainty, conditions and work needed to interpret them.

### C.16:1 - Intent (Normative)

**Name.** *Measurement & Metrics Characterization (MM‑CHR).*

**Use this when.** A reading needs interpretation, or a proposed measurement needs a model. Ask what quantity or Characteristic is sought, how the procedure produces an indication, and what can be inferred from it under the measurement conditions.

**What changes in practice.** The practitioner constructs or recovers the relation that makes a reading informative about the subject. This can reveal an influence to include, an ambiguity to preserve, or an arrangement to change. When reporting a performed measurement, connect the attributed values and their uncertainty to the method, model, calibration and work that obtained them. A later diagnosis or decision uses that interpreted result.

**Not this pattern when.** Use A.17 for the Characteristic, A.18 for scale-operation legality, C.16.P while measurement wording is still ambiguous, A.19.CPM for comparison, A.19.SelectorMechanism for selection, C.28 for causal use, A.10/G.6 for provenance, B.3 for assurance, G.4 for an acceptance declaration, G.11 for currentness, and C.11 for a decision result. C.16 supplies none of those results by implication.

**Local designators.** `MeasurementSpecification`, `MeasurementMethod`, `MeasurementModel`, `MeasurementWork`, `MeasurementResult`, and `MeasurementResultEpisteme` name exact objects in one case; they are not new public U-kinds or universal relation types. `MeasurementMethod` is one exact `U.Method`; `MeasurementWork` is one dated `U.Work`; `MeasurementResultEpisteme` is one C.2.1 episteme.

**Compatibility with the retained measurement family.** `U.DHCMethod` remains the durable measurement-definition value that fixes the Characteristic, Scale and applicable unit and cites the method and model. A preference rule belongs to the evaluation that uses the result, when one is being made. `U.Measure` remains the durable reading claim: when persisted, it is the C.2.1 result episteme that states the C.16 measurement result. `U.Unit` carries quantity-kind and conversion semantics when the Scale requires them. `U.EvidenceStub` is only a compact locator into A.10/G.6 provenance; it is not the measurement result, an evidence carrier, a work record, or a relation that establishes measurement.

### C.16:2 - Scope and result boundary (Normative)

C.16 covers construction and use of measurement models. For a performed measurement, it keeps the following parts of the result account recoverable:

- one measurand or otherwise exact measurement subject;
- one Characteristic and one Scale, with Level or Coordinate and Unit when applicable;
- the reusable measurement specification, exact `U.Method`, measurement model, calibration requirements, and uncertainty treatment;
- dated measurement work with performer, actual bindings, resources, and time stance;
- the value or set of values attributed to the measurand together with relevant information, including uncertainty and interpretation basis; and
- direct comparability within the declared basis.

C.16 does not turn an instrument message, file, dashboard tile, ledger row, or evidence citation into a measurement result. It does not own the actual subject state, diagnosis, criterion verdict, acceptance action, assurance claim, causal conclusion, or decision. It introduces no universal measurement-result, work-result, evidence-use, common-scale, or criterion-participant relation.

### C.16:3 - Problem Frame

A measurement is often compressed to `subject → value`. That abbreviation hides the measurand, the quantity or characteristic intended to be measured, the model relating inputs to an output quantity, the calibration basis, the work occurrence, and the uncertainty carried into later use. It also makes raw instrument output, a displayed indication, an attributed measurement result, a diagnostic interpretation, and a criterion verdict look like one object.

The failure becomes visible when two readings are compared, when a detector output is treated as the state of the subject, or when a dashboard value is reused as evidence, assurance, acceptance, or decision authority. C.16 restores the measurement-specific objects before any receiving use is judged.

### C.16:4 - Forces

- **Interpretability vs convenience.** A compact value is easy to carry; a usable result needs its measurand, Characteristic, Scale, model, calibration, uncertainty, and time stance.
- **Model dependence vs objectivity rhetoric.** Measurement may use corrections, calibration coefficients, influence quantities, and inference. Hiding them does not make the result more direct.
- **Cross-domain reuse vs scale coercion.** Physics, software quality, architecture, survey, and judging cases need common discipline without one common scale.
- **Repeatability vs occurrence identity.** A reusable method and operation declaration do not establish that measurement work occurred or that actual participants were bound.
- **Result vs later interpretation.** A value attributed to a measurand is not by itself a diagnosis, conformance verdict, causal conclusion, assurance claim, or decision.

### C.16:5 - Solution - Construct and interpret a measurement (Normative)

To develop a measurement model, begin with §§5.1-5.4. A proposed relation can supply a conditional calculation or expose an ambiguity before any measurement is performed. An existing model that answers the question can be used directly.

When interpreting a performed measurement, recover one ordinary direct sentence:

> Dated measurement work `W` applied method `M` to measurand `x`, using model `f`, calibration basis `K`, and actual input bindings `X`, and obtained output quantity value `y` with stated uncertainty `u`; episteme `E` states that measurement result under its declared Characteristic, Scale, unit, time stance, and interpretation basis.

If a fact needed for that interpretation is unavailable, state which conclusion remains undetermined and what information could resolve it.

#### C.16:5.1 - Name the measurand and measurement subject

**M‑SUB‑1.** Name the measurand: the quantity or characteristic intended to be measured. When FPF uses a non-quantity Characteristic, name the exact subject and the Characteristic whose Scale position is being attributed.

**M‑SUB‑2.** Preserve arity. An entity Characteristic has one subject; a relation Characteristic has the exact ordered tuple required by A.17. A relation reading is not silently rewritten as a unary property of one participant.

**M‑SUB‑3.** Distinguish the measurand from the actual subject state. A measurement result attributes values under a method and model; it does not make the physical, social, architectural, or epistemic state identical to the result episteme.

#### C.16:5.2 - Fix Characteristic, Scale, unit and time stance

**M‑CSLC‑1.** One `U.DHCMethod` binds exactly one Characteristic to exactly one Scale. A discrete reading names its Level; another reading names its Coordinate or value on that Scale.

**M‑CSLC‑2.** When units apply, name the quantity kind and presentation Unit. Conversions are admissible only when they preserve the quantity kind and the Scale supports the operation. Nominal and ordinal labels do not acquire interval or ratio arithmetic by being encoded as numbers.

**M‑CSLC‑3.** Use the Scale's order to interpret the Characteristic: a higher temperature value means hotter. When a later evaluation asks which value is preferable, state its preference under A.17/A.18. A measurement or magnitude comparison needs no preferred direction.

**M‑CSLC‑4.** State the time stance: instantaneous or as-observed at `T`, aggregated over window `W`, or another exact temporal basis. A later value does not silently replace an earlier result.

#### C.16:5.3 - Separate method, description, model, calibration, and work

**M‑METH‑1.** `MeasurementMethod` is one exact `U.Method`. Its `U.MethodDescription` may state generic participants, parameters, effects, and measurement conditions; it contains no actual-participant slots and does not claim that measurement occurred.

**M‑MODEL‑1.** `MeasurementModel` relates input values and relevant influences to the values attributed to the measurand. In quantity measurement, these are input, influence and output quantities. Identify the model version, assumptions, corrections and domain of validity. Recover what its formula, software function or other expression represents. Use C.16.MR to construct that relation from the indication-producing procedure when it is missing or unsuitable; :5.3.1 connects the construction to interpretation and its next use.

**M‑CAL‑1.** Name the calibration basis required for the use: reference standard or comparison basis, dated calibration work and result when current, calibration coefficients or corrections, applicable interval, and uncertainty contribution. A calibration certificate or ledger row cites these facts; it does not establish them by being stored.

**M‑WORK‑1.** `MeasurementWork` is one exact dated `U.Work`. First recover every actual performer's A.13 core for the measurement action, including the same obtaining assignment; then independently admit the Work under A.15.1 from its performance history, at least one obtaining `enactsMethod` relation, temporal extent, and at least one obtaining locally declared containing-system relation. Add F.6 afterward only when the measurement claim also needs precise assignment-bound attribution. Name the exact measurand through its direct subject relation or an A.6.1 operation-application binding. Name another enacted Method, resource, or concrete participant only when the measurement claim uses its independently obtaining relation or binding. A plan, compatible signature, method description, instrument type, or retained reference establishes none of those actual facts.

##### C.16:5.3.1 - Construct the measurement relation

1. **Start with what is being measured and why.** Specify the subject, Characteristic, conditions and required range of interpretation under §§5.1-5.2. Separate what is already known from values the proposed measurement must resolve.
2. **Follow how the indication is produced.** Describe the procedure connecting the subject to the indication. Recover the measurement principle, applicable calibration relation, or combination of both that connects the quantities. Include intermediate conversions when they change the answer. Physical laws, assessment models and instrument-specific relations come from the relevant subject knowledge; B.5:4.2 helps recover their construction.
3. **Include influential conditions.** Consider how the apparatus interacts with the subject, what it samples or averages, and its resolution and operating range. Include an influence when its omission could change the interpretation needed for this use. Explain a correction through the relation that gives its direction and magnitude. Retain an unknown influential quantity as unknown, using available bounds or distributions when justified.
4. **Determine what the relation resolves.** With actual or proposed indications, derive the compatible sought values and their uncertainty under §5.4. If different sought values can produce the same indication, identify that ambiguity. Work a small case or limiting case to expose an omitted influence, inconsistent units or a failed inversion. C.16.IR constructs the joint cases and distinguishes feasible alternatives from bounds that may include unattainable values.
5. **Choose the useful return.** Supply the interpreted value, interval or conditional result when it answers the question. Otherwise identify which change could resolve the remaining ambiguity: refine the relation, change the measurement arrangement, obtain an applicable calibration or narrow the conclusion. Choose further observation by the distinction it can resolve and the work it demands, using C.11.DUA when that choice needs deliberation. C.16.RM compares changes to models, arrangements and calculation, then carries the selected repair through the interpretation while retaining the wanted quantity.

When an observed discrepancy matters, compare its plausible sources in the subject account, measurement relation and actual arrangement. Change the contribution that can alter the answer; sometimes removing an unwanted influence from the arrangement is more useful than modeling it in greater detail. A model-development result states the relation and what it would establish. A claim about a performed measurement also identifies the work and obtained result under §§5.3-5.5.

#### C.16:5.4 - Recover input quantities, output quantity, and uncertainty

**M‑IO‑1.** Name each actual input quantity used by the model, including indications, repeated observations, environmental or other influence quantities, reference values, calibration coefficients, and applied corrections when current. Name the exact output quantity whose value is attributed to the measurand. These are measurement-model roles, not a universal work input-output ontology.

**M‑UNC‑1.** State the uncertainty associated with the attributed value or values whenever it affects interpretation or use. Identify the contributing input uncertainties, correlations or covariance when relevant, propagation method, coverage or interval interpretation, and significant model inadequacy. An uncertainty number without its interpretation is not complete.

**M‑UNC‑2.** Propagation follows the declared measurement model. Linearized propagation, sampling, interval, set-valued, or another method is admissible only under its own assumptions. Combining provenance pointers is not uncertainty propagation, and more cited grounds do not monotonically guarantee lower uncertainty.

#### C.16:5.5 - State one measurement result and one result episteme

**M‑RES‑1.** `MeasurementResult` is the value or set of values attributed to the measurand together with relevant information needed to interpret them. At minimum, recover the measurand, Characteristic, Scale, attributed value or values, Unit when relevant, uncertainty, method, model, calibration basis, time stance, and exact measurement work.

**M‑RES‑2.** `MeasurementResultEpisteme` is one exact C.2.1 episteme. Its ClaimGraph states the C.16 result, subject, interpretation basis, polarity or domain status when current, and uncertainty. `U.Measure` may designate this retained reading claim. The episteme is not the measurand, actual subject state, raw output, indication, diagnosis, or criterion verdict.

**M‑RES‑3.** When exact work and governed actual changes first establish the episteme's identity and that inception matters, A.15.PROD supplies the local entity-identity inception claim. C.16 does not introduce a work-to-result relation.

#### C.16:5.6 - Keep comparability and scoring bounded

**M‑CMP‑1.** Direct comparability is conservative: two readings cite the same `U.DHCMethodRef`, Characteristic, Scale and Unit semantics, compatible model and calibration regime, and a compatible time or population basis. Similar labels or units are insufficient.

**M‑CMP‑2.** Cross-template conversion, normalization, scoring, aggregation, comparison, selection, or cross-context transport names its method, declaration, and loss or uncertainty consequence under the pattern for that operation. Name an F.9 Bridge when cross-context semantic correspondence is required. C.16 does not mint a common scale or corpus-wide migration relation.

**M‑SCORE‑1.** A Score is another declared Scale reading. Its scoring method and actual application remain under their direct Method, Work, and operation-binding patterns. A score does not overwrite its source measurement results.

#### C.16:5.7 - Route provenance and later use outward

`U.EvidenceStub` may carry a type-of-ground and identifier that lead to the exact A.10/G.6 provenance path. The path can cite the method description, model, calibration, work, inputs, output, result episteme, source publications, and transformations. Neither the stub nor a graph edge establishes those objects or their obtaining relations.

A later comparison, diagnosis, criterion evaluation, acceptance action, or decision is separate dated work. It uses the result episteme through an exact premise, reference, operation-argument, decision-use, or other direct relation. Currentness belongs to G.11; bounded reliance to A.10 or B.3 under their entry conditions.

#### C.16:5.8 - Lexical and neighboring-pattern discipline

Use **measurand**, **measurement subject**, **Characteristic**, **Scale**, **Level**, **Coordinate**, **value**, **Unit**, **measurement method**, **measurement model**, **calibration**, **uncertainty**, **measurement work**, and **measurement-result episteme** for their exact jobs. Plain-register *metric*, *reading*, *score*, and *output* are acceptable after first-use mapping. Do not use *measurement result*, *evidence*, *validation*, or *verification* as umbrella terms for several governed objects.

**Key relations.** C.16 uses A.17 and A.18 for Characteristic and Scale legality; A.6.1 for declaration-local positions and operation bindings; A.13 for each actual performer; A.15.1 for independent admission of the dated Work; and F.6 afterward only when precise assignment-bound attribution is needed. If claim-bearing source wording still says only “role,” use E.10.ROLE first, then use A.2 or A.2.1 only when an exact local system-role kind, classification, or assignment has actually been recovered. C.2.1 covers the result episteme; A.10/G.6 provenance; G.11 currentness; B.3 assurance; and the exact pattern for the next diagnosis, acceptance, causality, comparison, selection, or decision question.

### C.16:6 - Scale-type admissibility quick reference (Informative)

> **Didactic note.** This table is a memory aid for engineers and managers. It does **not** introduce new admissibility rules. Normative admissibility of operations by scale type is governed by **A.18 (CSLC)** and, where mechanized in CG‑frames, by the relevant admissibility profiles.
> If any row below conflicts with A.18, treat it as an illustrative example and follow A.18.

| Scale type   | Comparisons    | Location          | Differences        | Ratios                   | Admissible summaries                                  | Typical unsupported anti-patterns                                   |
| ------------ | -------------- | ----------------- | ------------------ | ------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------- |
| **Nominal**  | =, ≠           | mode, frequencies | —                  | —                        | counts, proportions                                   | averaging labels; ordering categories without a declared order      |
| **Ordinal**  | <, =, > (rank) | median, quantiles | **not meaningful** | —                        | order‑respecting summaries (median rank, percentiles) | arithmetic mean of ranks; variance on ranks; linear blends of ranks |
| **Interval** | <, =, >        | mean location     | Δ meaningful       | ratio **not** meaningful | mean, sd of **differences**, correlation              | ratio claims (“twice as hot” in °C); geometric mean                 |
| **Ratio**    | <, =, >        | mean location     | Δ meaningful       | ratios meaningful        | arithmetic/geometric means, cv, growth rates          | adding heterogeneous units; log on nonpositive values               |

**Reminders (informative; see A.18 for normative rules).**
G‑1 (Order). On ordinal, transforms should be **monotone**.
G‑2 (Differences). On interval or ratio, **Δ** is meaningful; on ordinal or nominal, it is undefined.
G‑3 (Ratios). Only ratio Scales admit **x/y** semantics; interval, ordinal, or nominal do not.
G‑4 (Unit coherence). Interval or ratio arithmetic presumes compatible units (or a declared conversion).
G‑5 (Target polarity). If polarity is targeted, comparisons use distance‑from‑target semantics as declared by the relevant subject pattern, template, and cited method or mechanism.

*(These rules line up with the MM‑CHR exposition of CSLC and term discipline; A.17 fixes the lexical side.)*

### C.16:7 - Provenance and use semantics (Normative)

#### C.16:7.1 - What an EvidenceStub is and is not

`U.EvidenceStub` is an optional compact locator from the reading claim to an exact provenance path. It may identify a source publication, calibration record, instrument output, model edition, work occurrence, transformation, or other ground, but A.10/G.6 govern the path and its citations.

- The stub is not evidence in the abstract, a result, an instrument output, a work record, an assurance claim, or a provenance-as-result object.
- Several stubs form a list of locators, not a measurement algebra. Their union is not uncertainty propagation and does not guarantee stronger warrant.
- A provenance edge may be asserted only after its direct source relation, work fact, participation, production, representation, or citation relation is independently established.
- A later user states the exact relied-on claim and local `RelianceDisposition`; use B.3 when an actual named assurance claim is current. Mere availability, citation, or graph membership does not establish actual use.

### C.16:8 - Measurement-result boundaries (Normative)

Keep the following objects distinct even when one carrier displays several of them:

| Object | Governing question |
| --- | --- |
| Raw instrument output | What signal, bytes, count, image, trace, or other emitted entity exists? |
| Indication | What displayed or decoded value did the instrument provide under its indication semantics? |
| Actual subject state | What obtains for the physical, social, architectural, or epistemic subject independently of the record? |
| Measurement result | What value or values are attributed to the measurand, with relevant method, model, calibration, uncertainty, and time information? |
| Measurement-result episteme | What durable C.2.1 claim states that result and its interpretation basis? |
| Diagnosis or causal conclusion | What later domain interpretation is supported under its own method and result algebra? |
| Criterion or acceptance verdict | Did the exact criterion application return pass, fail, or unknown? |
| Decision result | What did separate C.11 decision work decide? |

The carrier, dashboard, ledger, criterion clause, and evidence path may represent or cite several rows. None collapses their identities or establishes another row by presence alone.

### C.16:8.3 - Archetypal Grounding

**Calibrated detector receiver.** The detector emits raw counts. Its processing yields an indication of `41.8 kPa`. The measurand is gas pressure at port P over the stated sampling window; Characteristic is Pressure; Scale is a ratio quantity scale; Unit is kPa. Measurement model `PressureModel-4` uses counts, reference offset, temperature, and calibration coefficients as inputs and pressure as output. Dated measurement work names its performer, detector, port, resources, bindings, calibration basis, and uncertainty propagation. The C.16 result attributes `41.8 kPa ± 0.6 kPa` to the measurand under that basis; one C.2.1 episteme states it. The raw counts, displayed indication, actual pressure, result episteme, a later leak diagnosis, and a pressure-limit verdict remain different objects.

**Internal-combustion-engine test bench.** One dated test-bench work occurrence binds the engine, dynamometer, fuel batch, ambient conditions, method, model, and calibration records. Torque, exhaust temperature, and emissions are three Characteristics with separate Scales and result epistemes; their input quantities, output quantities, covariance where relevant, and uncertainties remain separately recoverable. Aggregation work may later construct a declared performance summary, and evaluation work may apply an emissions criterion. Neither the summary nor the pass/fail verdict is the torque or emissions measurement result.

**Architecture coupling.** The measurand is the exact ordered module pair under a declared dependency census window, not either module alone. The Characteristic is Coupling on an ordinal Scale. The method description defines generic dependency classes; dated work binds the actual codebase edition and pair. The result episteme states the Level and basis. A later release decision may rely on it, but the dashboard tile and decision record do not establish the census work.

#### C.16:8.3.1 - A voltmeter changes the voltage it reads

The sought quantity is the open-circuit voltage E of a source. Model the source as an ideal voltage E in series with resistance R_s; the connected voltmeter has input resistance R_m. The meter closes the circuit. Ohm's law gives current I=E/(R_s+R_m), and the indication is V=I R_m. The measurement relation is therefore E=V(1+R_s/R_m).

For E=10 V and R_s=R_m=1 megohm, the indication is 5 V. The known resistance ratio recovers the open-circuit value as 10 V. The difference comes from the measurement interaction.

If both E and R_s are unknown, one indication leaves several pairs compatible with it. For V=5 V, R_m=1 megohm and an available bound 0.8≤R_s≤1.2 megohm, the conditional voltage interval is 9≤E≤11 V. That interval may answer the question. When a narrower answer is needed, a second indication with a different known input resistance supplies another equation, provided the source stays unchanged and the circuit model still applies. Repeating the original arrangement supplies the same relation and leaves this ambiguity.

These calculations use an ideal circuit. For an obtained measurement result, include uncertainty in the indications and resistances and any model inadequacy that affects the use.

#### C.16:8.3.2 - Interpreting an assessment of independent performance

The sought quantity p is the fraction of a population able to perform a specified action independently under stated conditions. An applicable assessment calibration supplies a, the probability of a positive test when the capability is present, and b, the probability when it is absent. Partitioning the population by that capability gives the expected positive fraction q=ap+b(1-p).

With a=0.9 and b=0.1, the relation is q=0.1+0.8p. An observed positive fraction 0.7 gives the estimate p=0.75 under this model. Sampling uncertainty, uncertainty in the calibrated rates and their applicability determine how precisely that estimate can be used. When a=b, the expected positive fraction is independent of p, so this test supplies no such distinction.

Now allow hints during the assessment. The earlier a and b may no longer describe the procedure. With the changed rates unknown, the positive fraction alone no longer determines p. If the independent-performance claim is still needed, return to that performance condition or obtain a calibration applicable to the changed procedure. The model explains which inference is available; it uses the subject's account of the capability and its assessment.

### C.16:9 - Bias-Annotation

| Bias | Symptom | Correction |
| --- | --- | --- |
| Number-as-fact | A displayed value lacks measurand, Characteristic, Scale, model, calibration, uncertainty, or time stance. | Rebuild the complete C.16 chain. |
| Instrument realism | Raw output or indication is asserted as the actual subject state. | Separate output, indication, attributed result, and subject state. |
| Uncertainty laundering | A point estimate is carried forward while model and calibration uncertainty disappear. | Recover input uncertainties, correlations, propagation, and interpretation. |
| Dashboard authority | A tile or score is reused as diagnosis, assurance, acceptance, or decision authority. | Route the later use to the exact patterns for its Work, result, provenance, currentness, and reliance claims. |
| Common-scale pressure | Distinct scales are normalized merely because comparison is desired. | Require an exact transformation and receiving comparison pattern; otherwise preserve incomparability. |

### C.16:10 - Conformance Checklist (Normative)

For a proposed model, apply the subject, scale, model and applicable calibration checks. Apply work and result checks when asserting a performed measurement, and later-use checks when making that later claim.

1. **Subject:** one exact measurand or measurement subject is named, with correct entity or relation arity.
2. **CSLC:** Characteristic, Scale, Level or Coordinate, applicable Unit and time stance are interpretable. Add a preference rule only for a use that judges which values are preferable.
3. **Method/model:** the method, model version, inputs, output quantity, assumptions and validity domain are recoverable. When the relation had to be constructed, §5.3.1 explains how the procedure produces the indication and what sought values it can distinguish. Keep a proposed model separate from a claim of performed measurement.
4. **Calibration:** applicable calibration work/result, reference basis, coefficients or corrections, validity interval, and uncertainty contribution are cited when required.
5. **Work:** every actual performer has the A.13 core; the dated `U.Work` is independently admitted under A.15.1; F.6 is added afterward only when precise assignment-bound attribution is current. The exact measurand relation or A.6.1 binding is present; further enacted Methods, resources, or participant bindings are present only when the measurement claim uses them.
6. **Result:** one C.16 measurement result attributes value or values to the measurand with uncertainty and relevant information; one C.2.1 episteme states it.
7. **Separation:** raw output, indication, actual subject state, result, result episteme, diagnosis, verdict, and decision are not collapsed.
8. **Comparability:** direct or transformed comparison names its exact basis and does not upgrade the Scale or mint a common scale.
9. **Provenance/use:** A.10/G.6 provenance, G.11 currentness, bounded reliance, assurance, and later work remain under their subject patterns.
10. **Boundary:** no method description, plan, signature, carrier, ledger row, evidence edge, or stored reference is used to infer actual participation, work, or result identity.

### C.16:11 - Common Anti-Patterns and How to Avoid Them

- **Template as occurrence.** A reusable `U.DHCMethod`, model, signature, or calibration procedure is treated as proof that work occurred. Ground dated work and actual bindings.
- **Generic result field.** A record has `result=...` without saying whether it is output, indication, measurement result, diagnosis, verdict, or decision. Name the direct result kind and governor.
- **Evidence algebra.** Evidence locators are unioned as though idempotence or count determined uncertainty or warrant. Use measurement-model uncertainty propagation and exact A.10/B.3 reliance separately.
- **Scale drift.** A template id survives changed Scale, model, unit, or calibration semantics. Publish a successor and state the relation; do not mutate historical readings.
- **Arithmetic on ordinal.** Encoded levels are averaged or ratio-compared. Stay with order-preserving operations or introduce a separately governed scoring method and Scale.
- **Multi-Characteristic stuffing.** One reading carries a vector while pretending to be one measurement. Create separate results and declare any later aggregation.
- **Result-to-verdict shortcut.** A value inside a tolerance is called accepted without performed criterion evaluation. Ground the separate evaluation work, exact clause application, verdict episteme, and later decision.

### C.16:13 - Consequences

**Benefits.** Measurement results become interpretable and reusable without pretending to be raw reality or later judgment. A practitioner can inspect the measurand, Scale, method, model, calibration, work, uncertainty, episteme, and provenance, then enter the smallest pattern for the next question—comparison, diagnosis, acceptance, assurance, causality, or decision.

**Trade-offs.** The chain is longer than a dashboard field. Model assumptions, calibration status, and uncertainty can make a formerly crisp number conditional or set-valued. That cost is the information needed to avoid false precision and hidden result substitution.

**Failure containment.** Missing model validity, stale calibration, ungrounded work, absent actual bindings, or unreported uncertainty narrows or blocks the measurement claim. It does not authorize a generic evidence, result, or acceptance relation as fallback.

### C.16:14 - Rationale

Measurement is not merely reading a carrier. It is performed work under a method and model that attributes one or more values to a measurand and supplies the information required to interpret those values. That architecture explains why indication, actual subject state, measurement result, result episteme, diagnosis, and verdict must remain distinct.

### C.16:14.1 - SoTA-Echoing

Recheck the affected source-use decision before relying on it after 2027-07-30 or following an earlier change to the source edition, amendment, correction, Recommendation status, or normative definition. External terms guide the bounded C.16 rules named below; no source imports its ontology wholesale or establishes a measurement, work occurrence, result, episteme, calibration fact, or later-use relation.

| Exact source and source-use decision | Visible C.16 mutation | Rejected overread | Smallest source-change replay |
| --- | --- | --- | --- |
| [JCGM 200:2012, VIM3, online entry 2.9 `measurement result`](https://jcgm.bipm.org/vim/en/2.9.html), including the online corrections/annotations as of 2026-07-30 — **adopt** the attributed-values-plus-relevant-information boundary. | `M-RES-1`, `M-RES-2`, the calibrated-detector case, and checklist items 6–7 keep measurand, attributed values, uncertainty/relevant information, and result episteme distinct. | A displayed indication, raw output, actual subject state, diagnosis, verdict, or decision is not the measurement result. | Reopen only `M-RES-1/2`, the calibrated-detector result paragraph, and checklist items 6–7 if VIM changes the result/measurand boundary. |
| [JCGM GUM-6:2020, *Developing and using measurement models*](https://doi.org/10.59161/JCGMGUM-6-2020) — **adapt** its model/input/output/model-adequacy and uncertainty discipline to the C.16 measurement chain. | `M-MODEL-1`, `M-IO-1`, `M-UNC-1/2`, the engine-test case, and checklist items 3–4 make model edition, actual inputs, output quantity, assumptions, calibration, covariance, propagation, and validity domain recoverable. | Model input/output roles are not universal work relations; more provenance pointers do not reduce uncertainty; a formula or function does not prove that measurement work occurred. | Reopen only `M-MODEL-1`, `M-IO-1`, `M-UNC-1/2`, the engine-test uncertainty paragraph, and checklist items 3–4 if GUM changes model construction, adequacy, or propagation requirements. |
| [ISO 80000-1:2022, *Quantities and units — Part 1: General*](https://www.iso.org/standard/76921.html) and [ISO/IEC 25024:2015, confirmed current in 2022](https://www.iso.org/standard/35749.html) — **Bridge-only** for quantity/unit names and data-quality-measure alignment. | They may populate a Concept-Set/Bridge used by `M-CSLC-2` or a receiving data-quality measure; they do not change C.16's separation between Characteristic/Scale and measurement result. | Standard quantity, unit, or quality-measure labels do not authorize arithmetic, comparability, acceptance, or a C.16 result. | Reopen only the affected Bridge row plus `M-CSLC-2` and checklist item 2; reopen no measurement case unless the mapped term was load-bearing there. |
| [QUDT Schema 3.4.0, June 2026 catalogue](https://www.qudt.org/catalog/qudt-catalog.html) — **Bridge-only** for citable quantity-kind, unit, dimension, and datatype identifiers. | A C.16 record may cite a QUDT identifier after the F-pattern Bridge establishes the correspondence; `M-CSLC-2` still governs admissible C.16 use. | A shared URI does not prove same measurand, Scale, model, calibration regime, or direct comparability. | Reopen only the cited Bridge mapping, `M-CSLC-2`, and checklist items 2 and 8 when the mapped QUDT graph or identifier changes. |
| [W3C/OGC SOSA/SSN Recommendation 19 October 2017](https://www.w3.org/TR/vocab-ssn/) — **Bridge-only** for sensor, observation, procedure, feature-of-interest, and observed-property terms. The [2023 Edition First Public Working Draft of 16 September 2025](https://www.w3.org/TR/vocab-ssn-2023/) is watch-only until it reaches a governing publication status. | A Bridge may align an external observation/procedure record with C.16's measurand, method, work, indication, and result boundaries; it never replaces `M-WORK-1` or `M-RES-1/2`. | An SOSA/SSN observation graph does not by itself establish FPF work identity, actual bindings, measurement result, result episteme, or later use. | Reopen only the affected SOSA/SSN Bridge, `M-WORK-1`, the external-record case that uses it, and checklist items 5–7 when the Recommendation changes or the 2023 Edition advances with a conflicting normative separation. |

**Constructing and revising the model.** GUM-6:2020, §§7, 9-10 and 12, supplies the distinction between the measurement principle, effects of implementation and adequacy for use. Section :5.3.1 turns that distinction into a construction and an ambiguity test. The circuit and assessment cases work this instruction using their stated subject models.

[Dounas-Frazer and Lewandowski (2018), §2](https://arxiv.org/pdf/1805.10334), distinguishes models of the phenomenon and measurement equipment and allows revision of either model or either physical arrangement. C.16 adopts those different returns. Its stopping question is the intended use of the measurement: a sufficient interval can end the work, while a consequential discrepancy can require further investigation. B.5 and C.11.DUA supply the wider inquiry and choice.

Other lineage and domain examples are informative comparators. A source change reopens the contribution that relies on it; extend that comparison when a changed premise also affects another use.

### C.16:15 - Relations - Placement *(Informative)*

**Measurement-relation construction.** C.16.MR derives a relation from the sought property, measuring arrangement and consequential influences, and obtains a first conditional result. This construction can support a proposed measurement. For a result from an actual measurement, use the conditions above for the performed work and its interpretation.

**Indication interpretation.** C.16.IR begins with an available measurement relation and determines which values or comparisons an indication supports. Use it when influential unknowns, lost distinctions or uncertainty can change the requested answer. It can return a sufficient bound while other quantities remain unknown.

**Measurement repair.** C.16.RM begins when an existing measurement disagrees with an expectation or cannot resolve the distinction needed for use. It chooses which model, arrangement or calculation to change, recovers a result from the available observations when possible, and tests the changed contribution at the scope of the receiving question.

**Architecture measurement boundary.** `C.32.P2S`, `C.32.PAD`, and `C.32.ADA` may cite C.16 readings only after the characteristic, bearer, scale, coordinate, value, unit when relevant, and admissible use are declared. C.16 readings do not become architecture characteristics, decision criteria, eval programs, evidence, gates, or decision authority by themselves.

**Structural-information measurement boundary.** `C.33`, `C.34`, and `C.35` may name captured structure, lost structure, similarity, preservation, entropy, epiplexity estimate, compression, generated-carrier adequacy, or search-output context. When a claim about any of those uses a value, score, coordinate, threshold, dashboard reading, or eval result, state the measurement construction and admissible-use assertions under the exact C.16 and evaluation/criteria predicates, with their subject patterns used as locators.

**Precision-restoration relation.** `C.16.P` is the first-stage wording-use restoration pattern for characteristic, scale, coordinate, score, metric, axis, dimension, and related characterization wording when the measurement object is not yet recoverable. Once the wording is resolved, use C.16 for the measurement-chain question or the pattern for the recovered non-measurement claim.
**C.27 temporal-claim relation.**

- C.27 may flag: a rate/rate-change reading whose admissible use depends on admissible measurement construction, evidence, sampling window, or finite-difference method.
- This pattern keeps: measurand and measurement-subject identity, method, model, calibration, input/output quantities, uncertainty, dated work, measurement result, result episteme, comparability basis, units, sampling window, and provenance routing.
- Non-admissible use: a rate-change label is not a measurement template, and temporal words such as velocity, acceleration, throughput, cadence, or recovery speed are not admissible measures by themselves.
- Neighboring-pattern use: when load-bearing, the claim cites `baseCharacteristicRef`, the relevant measure reference, sampling window, construction method such as `DHCMethodRef`, and `C16RouteRef`; C.27 keeps only the temporal-claim adequacy question.

**C.28 causal-use relation.** C.16 governs measurement construction, result interpretation, uncertainty, and direct comparability. C.28 governs the causal-use relation when the same result episteme is used to claim effect, intervention success, causal fairness, policy optimality, counterfactual comparison, off-policy causal evaluation, causal-RL evaluation, or causal method superiority. A C.16-admissible measurement result is therefore not by itself admissible for causal use under C.28.

**Evidence, currentness, and assurance.** Use A.10 and G.6 for source recovery and provenance for the exact method, model, calibration, Work, inputs, result episteme, and later use. Use G.11 for currentness and B.3 when an actual named assurance claim is current. Evidence, provenance, currentness, and assurance do not by themselves establish the C.16 measurement result.

**Kernel.** MM‑CHR *imports* the canonical Characteristic vocabulary and the CSLC discipline fixed by A.17 and A.18; it does not redefine them. CharacteristicSpace reasoning (for change) lives in the patterns that consume MM‑CHR readings.

**Using patterns.** KD‑CAL, Arch‑CAL, G.4, and other consumers cite C.16 measurement-result epistemes and then ground their own comparison, evaluation, acceptance, aggregation, or decision work. They do not produce a measurement merely by naming a template, score field, criterion, or evidence profile.

**Unification (F‑cluster).** External standards (e.g., ISO 80000 quantity types; W3C SOSA/SSN observable properties; QUDT units/quantity kinds) are related via Concept‑Set rows and Bridges; MM‑CHR treats those alignments as context supplied by F‑patterns, not as local re‑definitions.

### C.16:15a - Measurement and probe note for quantum-like readings

Use C.16 first when the live object is a sensor reading, survey response, dashboard value, score, probe result, or state coordinate. Noise, probability, discreteness, gaming, or difficult interpretation does not by itself make a case quantum-like.

Recover the ordinary measurement chain first:

1. name the measurand or subject, Characteristic, Scale, value or Level, applicable Unit and time stance; identify preference only when the use evaluates the result;
2. separate reusable method and model from dated work and actual bindings;
3. name input quantities, output quantity, calibration basis, uncertainty propagation, and one measurement-result episteme;
4. distinguish emitted output, indication, actual subject state, measurement result, result episteme, diagnosis, criterion verdict, and decision; and
5. attach provenance through A.10/G.6 and state the exact supported and unsupported later uses.

Only after that repair ask whether the probe order, frame, publication, or export changes the state or the inferences that remain admissible. If it does, C.26 may govern that residual contextual or probe-order question. If it does not, remain in C.16 and the ordinary evidence, assurance, or receiving-use patterns.

Minimum probe note:

| Field | Required content |
| --- | --- |
| Measurand and Characteristic | What exact subject quantity or characteristic is intended to be measured? |
| Scale and time stance | On what Scale and Unit, at what time or window, is the value attributed? |
| Method, model, calibration | What reusable method/model and applicable calibration basis govern the reading? |
| Work and bindings | Which dated Work occurred, who performed it, and which resource or argument bindings does this measurement claim use? |
| Inputs, output, uncertainty | Which model inputs determine the output quantity, and how is uncertainty propagated? |
| Result episteme | Which C.2.1 episteme states the attributed value and interpretation basis? |
| Boundary | Which raw output, indication, subject state, diagnosis, verdict, or decision remains separate? |
| Use | Which exact later use is supported, degraded, deferred, or unsupported? |

### C.16:15b - C.29 mathematical-lens use relation

If a mathematical lens depends on a measurement, recover the C.16 measurand, Scale, model, calibration, work, uncertainty, result episteme, and comparability basis first. C.29 may then state the lens-use admissibility claim; it does not construct the measurement, make values comparable, or provide provenance. A.10/G.6 retain provenance and B.3 retains assurance.

### C.16:End
