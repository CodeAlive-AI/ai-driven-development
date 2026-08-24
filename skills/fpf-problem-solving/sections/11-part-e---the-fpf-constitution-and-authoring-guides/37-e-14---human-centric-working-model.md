## E.14 - Human‑Centric Working‑Model
> **Status:** Stable
> **Type:** Pattern

### E.14:0 - Use This When

Use this pattern when FPF text needs to stay readable as one human working model while heavier mapping, logical, constructive, or empirical assurance remains recoverable underneath it.

**What goes wrong if missed.** The working text either drifts into local jargon and slash labels or calcifies into proof machinery that practitioners cannot use in ordinary design, review, or management work.

**What this buys.** A working reader sees one small model first, while assurance readers can still recover mapping, logical, constructive, and empirical grounding without forcing that machinery back into the Working-Model vocabulary.

**Ordinary route.** Write the shortest practitioner sentence that says what the claim is about, what it claims, and what use it supports. If no assurance-bearing reliance question is current, let the reader stop there. When one is current, place only the needed Mapping, Logical, Constructive, or Empirical support underneath that sentence and cite the pattern that defines or tests each supporting claim.

**Not this pattern when.** Do not use E.14 to decide whether a relation obtains, Work occurred, a result was constituted, evidence or assurance passes, a method applies, work is ready, a gate passed, or permission is current. Use the pattern that defines or tests that claim. Use E.14 for the human-first publication order and the recoverability of support; it supplies none of those domain results.

### E.14:1 - Intent

Establish a **single, human‑centric Working‑Model** that practitioners can read, discuss, and evolve **without exposure to formal machinery**.
A direct Working-Model statement needs no assurance field simply because it is published. When a publication elects `B.3.5` or another named current assurance requirement applies, the author declares the posture that requirement calls for and attaches only the needed assurance shoulders — **Mapping**, **Logical**, **Constructive**, or **Empirical Validation**. Under `B.3.5`, covered claims declare `validationMode`; covered structural claims also carry the profile's constructive grounding. The posture and its supports justify or challenge the published claim; they create neither the chosen model value nor a world-side relation occurrence. A `postulate` remains a pragmatic working claim within its stated scope: the author should add brief empirical cues that would help later validation. Choosing it does not say that evaluation or measurement Work occurred or that a result exists. The complete Work, result, and provenance account enters only when evaluation or measurement actually occurred and the current assurance use relies on that result; another named current requirement keeps its own obligations. Assurance shoulders sit **beneath** the Working-Model and **never define its vocabulary**.

Put bluntly: *one model people work in; three assurance shoulders — plus empirical checks when the world is the judge.*

### E.14:2 - Problem Frame

Teams need **one shared Working-Model** to make decisions at speed. Historically this shared model either:

* **drifts into jargon** - different terms for one shared working-model value, slash-labels, partial overlaps; or
* **calcifies into machinery** - too formal for day-to-day design and review.

Both failure modes create friction between two audiences:
(1) **working users** (engineers, programme managers, policy owners) who need a **small, stable Working-Model text**, and
(2) **assurance authors** (ontologists, methodologists, auditors) who need **proofs that the Working-Model text is sound**.

E.14 resolves the impasse by **separating concerns**:

* A **Working-Model layer**: curated kinds and relations expressed in plain terms, with simple human rules for using them.
* An **Assurance stack** beneath it - **Mapping**, **Logical**, **Constructive** - that carries the heavy arguments and accounts (concept alignment, direct relation semantics, construction-trace epistemes) and **never leaks back** into the Working-Model narrative.

This pattern dovetails with the framework's unification stance (**small Working-Model text, rigorous foundations**) and with the constructional-mereology discipline that `sum`, `set`, and `slice` provide inspectable accounts of independently grounded assembly, collection, and aspect facts. Those forms do not create a relation occurrence or decide whole identity. The Kernel stays minimal and meta-only.

### E.14:2.1 - Problem

A reader may need to decide, design, review, or coordinate with FPF terms before they are ready to inspect mapping tables, constructive traces, evidence records, or proof arguments. If the working text exposes all of that machinery first, the model becomes unusable; if it hides the machinery completely, the model becomes arbitrary. E.14 keeps one human-facing Working-Model visible while making the assurance shoulders recoverable beneath it.

### E.14:3 - Forces

1. **Cognitive economy vs. semantic precision.**
   Managers and engineers must navigate with a handful of names and relations; assurance authors must still check that each name has one intended model value, each relation claim has the required world-side basis, and identity conditions are explicit.

2. **Speed of change vs. guarantees.**
   The Working‑Model must accommodate rapid iteration; the Assurance stack must **lag just enough** to check, without blocking practical progress.

3. **Parsimony vs. expressivity.**
   The Working‑Model should **not proliferate relation types or ad‑hoc categories**; fine‑grained distinctions live in the Assurance layers and are shown **only when they materially change a decision**.

4. **Downward grounding vs. upward contamination.**
   When grounding is attached, it flows **down** (Working-Model → Mapping, Logical, Constructive, or Empirical support). No dependence **up** is allowed: proofs and traces never dictate wording or layout in the Working-Model.

5. **Trans‑disciplinary unification vs. local dialects.**
   The Working‑Model must reconcile different disciplines’ habits **without erasing them**; Mapping captures dialects, while the Working‑Model exposes a **single usable choice**.

6. **Auditability vs. readability.**
   Any Working-Model statement can be **audited on request** under the pattern that defines or tests its direct claim and any assurance profile selected for the current use; day-to-day views **hide the scaffolding** unless summoned.

### E.14:4 - Solution

#### E.14:4.1 - Human-Centric principles

##### E.14:4.1.1 - Recognition text and assurance text
Human-facing patterns also need EntityOfConcern stability across the two reading-order text blocks. The working reader should not meet one object in the recognition text and a different ontological kind in the assurance text. If the pattern distinguishes an EntityOfConcern, the interpretive or operational move applied to that object, and the wider review or work process around it, those distinctions should be made explicit rather than hidden behind stylistic noun-swapping.

Working-Model-first drafting therefore also means subject-domain-first drafting. If a pattern is meant to help with a real review, design, cultural, research, or operational problem, the recognition text should open from that problem-owning moment before internal taxonomy or package architecture. If a broader umbrella and a narrower working branch are both live, say plainly what each names, what object is being discussed, what move the reader makes, and what wider work remains outside.

Under `F.18` local-first naming, the canonical pair here is **recognition text** and **assurance text**.
The earlier provisional `...shell` wording is retired.
These names refer to two reading-order text blocks inside one pattern, not to new publication-face kinds or authority kinds.

For human-facing canonical patterns, Working-Model-first discipline should appear in a two-part reading order.
The **recognition text** is the working text that a cold practitioner, manager, or researcher should be able to understand first: what situation this pattern is for, what it buys, what it is not for, and what ordinary mistake it helps prevent.
The **assurance text** is the heavier text that carries declaration, object discipline, modeling lens, law, return conditions, and other assurance work.

The assurance text may justify, tighten, or audit the working text, but it must not silently replace or strengthen the recognition-text claim.
Where episteme-publication-heavy or transform-heavy patterns need a compact ontological account, the assurance text should expose three things explicitly:
- the ontic target or EntityOfConcern;
- the modeling substrate or mathematical lens when one is load-bearing;
- the publication face or working text by which the claim is presented.

This is a reading-order rule rather than a demand that every reader consume the assurance text first.
The point is to keep the human-facing Working-Model text primary while preserving a recoverable, auditable assurance text beneath it.

When empirical evaluation is current, keep the same reading order. Put the ordinary subject claim first. Keep an intended evaluation in its `U.WorkPlan`, name the selected `U.Method`, and cite a `U.MethodDescription` only when the plan, execution claim, or interpretation relies on that edition. If evaluation actually occurs, point to its complete A.15.1/F.6 basis. In the assurance account, name every performer, the assignment link checked with F.6, and the Method the Work enacted; use A.2.1 for the assignment itself and test any local system-role-kind classification separately. The first sentence may omit identifiers or basis details it does not use, provided the facts remain recoverable. Only the performer System acts. A working model, pattern, plan, criterion, Method, MethodDescription, assignment, record, result, evidence path, provenance value, or assurance claim does not become Work, and its availability does not make Work occur.
> **E.14-P.1 – Working-Model first, assurance when current.**
> Operate one **Working-Model** for all human-facing discussion and state the direct claim first. If neither the publication nor a named current requirement calls for assurance, the author may stop there. When assurance is current, declare only the posture and shoulder or shoulders required by the applicable pattern: **Mapping** to align a term with the chosen model value it names; **Logical** to state label meaning, scope, constraints, and limits; **Constructive** to make independently grounded construction facts inspectable; or **Empirical Validation** to support a bounded reliance on a domain result. Under `B.3.5`, covered claims declare `validationMode`. For each selected shoulder, name only the objects, scope, and qualification window the current use consumes. None creates the model value, subject relation, Work occurrence, or result it supports.

> **E.14‑P.2 – Downward‑only dependency.**
> Information **may** flow from the Working‑Model down into any Assurance layer; **no Assurance layer may impose vocabulary or shape back upward** into the Working‑Model.
>
> **E.14‑P.3 – Small working text, big proof.**
> The Working-Model exposes a **minimal set** of names in the L-1 and L-2 registers and a compact family of relations used in everyday reasoning; the assurance text makes their meanings, basis, limits, and support inspectable below.

> **E.14‑P.4 – Human registers first.**
> Terms in the Working‑Model are deliberately curated for **human legibility** (register‑badged, synonym‑aware). Synonym capture and language variance belong to Mapping; **only the chosen canonical label appears in the Working-Model text**.

> **E.14-P.5 – Required assurance postures are explicit.**
> A Working-Model relation covered by an elected `B.3.5` profile **declares** `validationMode ∈ {axiomatic, inferential, postulate}`. Another named current assurance requirement may require its own declared posture. A direct relation outside such a profile needs no E.14 assurance field.
> _axiomatic_ means that the author relies on one linked Constructive account for this assertion; _inferential_ means that the author relies on a reasoned chain; _postulate_ means that the assertion remains a pragmatic working claim within a stated scope. For a postulate, the author should add brief empirical cues that show where the claim tends to hold or what would challenge it. The posture alone establishes no evaluation Work and no result. Empirical Validation may accompany any posture when observation is the right support. Mapping, Logical, Constructive, and Empirical assurance remain separate from the claim's direct ontology and from the currentness of every record involved.

> **E.14‑P.6 – Parsimony in the working text.**
> No new Working‑Model relation types are introduced if the existing Logical label-meaning rules plus Constructive grounding suffice to capture the intended meaning.

> **E.14‑P.7 – A postulate is not completed evaluation.**
> When *postulate* is chosen, authors **SHALL** state the claim and its scope and **SHOULD** give brief empirical cues — where it tends to hold or what would challenge it — to ease later validation. This posture by itself requires no dated Work, result, complete A.15.1/F.6 basis, provenance path, or assurance claim. If evaluation or measurement actually occurred and the current assurance use relies on its result, authors **SHALL** name the scope and qualification window that use consumes, the domain result and result episteme, and the A.10 evidence-provenance relation; they keep the complete A.15.1/F.6 basis recoverable under §5.5. If an assurance claim is made or B.3's material-reliance threshold is met, the current B.3 assurance claim remains separate and required for that assurance-bearing use. Another named current assurance requirement supplies its own obligations.

> **E.14‑P.8 – Working-model-first is not explanation-thin.**
> Human-facing parsimony does **not** license under-explained pattern prose. When a pattern claims a Working‑Model benefit, it **SHALL** still provide enough problem framing, rationale, and worked slices that readers can tell what the model clarifies, what remains on the assurance shoulders, and when a heavier review path is required.

### E.14:5 - Layer Standard & Downward Flow (Working‑Model → Assurance)

This section defines **what each layer is for**, **what it guarantees when selected**, and **how purpose-selected support is carried down** from a direct Working-Model statement.

#### E.14:5.1 - Working‑Model (what humans see)

**Purpose.** A small, curated graph of kinds and relations that a mixed team can read at a glance.

**Elements.**

* **Kinds** — one **chosen concept** per node (no slash‑labels).
* **Relations** — a short list intelligible to non‑specialists (e.g., *Component‑of*, *Member‑of*, *Aspect‑of*, plus a small number of cross‑disciplinary ties such as *Interface‑of* or *Constituent‑of*).
* **Language register badges** — labels shown in the Working-Model are L-1 or L-2; L-3 and L-4 remain in Mapping as synonyms or symbols.

**Obligations.**

* A Working-Model edge or node whose use elects an assurance profile keeps that profile's required support recoverable downward. A direct claim outside such a profile can stand on its direct meaning and truth conditions; E.14 adds no assurance field or separate support account.
* The Working‑Model **does not display** constructor jargon, proof terminology, or evidence identifiers; those live in Assurance and are **available on demand**.

#### E.14:5.2 - Assurance-1: Mapping (from words to chosen model values)

**Purpose.** Consolidate human labels from varied sources and **bind them to the chosen model values** used in the Working-Model, including admitted U-kinds where kindhood is live.

**Guarantee.** When Mapping assurance is selected, the Working-Model label has a **stable alignment** to one chosen model value in the current scope; synonyms, abbreviations, locales, and registers are recorded here, **not** in the displayed Working-Model. Mapping primarily raises **Concept-Bridge Assurance (CBA)** by consolidating synonyms and registers and binding tokens and labels to the chosen value; calculus-level metrics live outside Part E.

**Deliverable.** When the current use needs source-word alignment, provide a compact alignment table for that scope. It makes obvious which **one label** the Working-Model shows and which background labels remain source wording.

*(Rationale: Working teams speak many dialects; the Working‑Model speaks one. Mapping is the interpreter.)*

#### E.14:5.3 - Assurance‑2: Logical (from Working‑Model relations to label semantics)

**Purpose.** Give each Working-Model relation **one precise intended meaning** and **its admissible use cases**, keeping the Working-Model vocabulary small.

**Guarantee.** When Logical assurance is selected, a Working-Model edge such as *Component-of* or *Aspect-of* carries one stated reading, including the scope and relation properties needed for the current use, so an auditor can assess whether that use is legitimate.

**Deliverable.** When the current use needs an explicit label-meaning account, give a short rule such as: “When an edge is labeled *Component-of* in the Working-Model text, it intends the direct structural reading whose participants, relation occurrence, construction rule, and identity conditions must be recovered before the assertion is accepted.” The Logical shoulder ties the human label to that accepted meaning; it does not make the relation obtain. Calculus-level symbols are not used in E-patterns.

*(Rationale: logical label alignment protects the small Working-Model text from relation proliferation while keeping meanings crisp.)*

#### E.14:5.4 - Assurance-3: Constructive (from a structural claim to its inspectable construction account)

**Purpose.** Make the construction basis of a published structural claim inspectable without turning the assurance account into the relation or the whole.

**Guarantee.** When Constructive assurance is selected, one truthful construction trace names the exact whole, collection, or aspect; its participants; the direct relation occurrences that obtain; the applicable assembly, collection, or facet rule; and the direct identity or reidentification conditions. The same inputs under another assembly may form another whole, while a permitted constituent replacement may preserve the same whole. The trace decides neither case.

**Deliverable.** For a structural assertion covered by an elected `B.3.5` profile, keep the readable claim first, link it through `tv:groundedBy` to one current C.2.1 construction-trace episteme in the C.13 `sum`, `set`, or `slice` form, and declare `validationMode=axiomatic`. If another named current assurance requirement calls for a construction account, follow that requirement and use C.13 for the trace content. Outside those conditions, the direct structural claim has no E.14 mode, link, or trace obligation. Creating, revising, publishing, or losing a trace changes the account or its availability, not the relation occurrence or whole identity. The trace edition, its warrants and evidence, and the temporal status of the described direct facts retain their own currentness.

*(Rationale: constructive assurance makes the facts and identity tests behind ordinary part-whole talk inspectable; it does not substitute an author narrative for those facts.)*

#### E.14:5.5 - Assurance-4: Empirical Validation (from claims to observed world)

**Purpose.** Make the empirical basis and bounded admissible use of one Working-Model claim inspectable without turning evidence, provenance, or an assurance record into the subject result.

**Guarantee.** A `postulate` remains a scoped working claim: state its target and scope and supply the brief empirical cues that B.3.5 calls for. It does not establish that evaluation or measurement Work occurred or that a result exists. When evaluation or measurement did occur and the current assurance use relies on its result, name the target claim, `U.ClaimScope`, qualification window, and the pattern that defines or tests the result, and keep the complete A.15.1/F.6 basis recoverable. The assurance account then names the dated Work, every performer `U.System`, and the Method the Work enacted; it uses F.6 to check each Work-assignment link and A.2.1 for the assignment itself. Cite a relied-on `U.MethodDescription` only when current, test any local system-role-kind classification separately, and name the participants or A.6.1 bindings, domain-local result, and C.2.1 result episteme that the claim uses. Use A.10 for the evidence-provenance path and reliance disposition, and B.3 for any assurance claim. These objects can support or qualify the Working-Model claim but create neither the subject fact nor one another. Another named current assurance requirement retains its own obligations.

**Deliverable.** Keep the ordinary Working-Model sentence first. For a postulate with no relied-on completed result, state the scope and brief empirical cues, then stop. When the current use relies on an actual evaluation or measurement result, expose only the exact result, Work, provenance, currentness, and assurance relations that use consumes. Intended evaluation remains in `U.WorkPlan` until dated Work occurs. If a claim that evaluation Work first constituted the result episteme is separately current, A.15.PROD alone recovers that local entity-identity inception claim; no universal work-result, evidence-result, or production relation is implied. Expiry, evidence ageing, or changed source, method, calibration, result, qualification window, provenance, or assurance basis ends only the reliance that consumes that support and requires the affected reliance claim to be re-evaluated under its applicable pattern. In B.3 terms Empirical Validation contributes on the LA shoulder; B.3 alone computes any effect on reliability R or claim scope G, and G cannot extend beyond the exact supported scope and qualification window.

#### E.14:5.6 - Purpose-selected support for a single Working-Model statement

Start with the direct Working-Model arrow **A –Component-of→ B**. If no assurance-bearing reliance question is current, the author may stop there. If a profile or named current requirement is active, add only the support it calls for:

1. **Mapping**, when source-word alignment matters, shows that *A* and *B* are the chosen labels for their model values and records background labels without making them Working-Model names.
2. **Logical**, when the relation reading needs assurance, states what **Component-of** means here and the boundaries of that use.
3. **Constructive**, when `B.3.5` is elected for this structural assertion, links the readable claim to one current C.2.1 trace episteme that reports the participants, direct relation occurrences, construction rule, and identity conditions in a `sum`, `set`, or `slice` form; the author declares `validationMode=axiomatic`. The direct relation and identity tests remain decisive.
4. **Empirical Validation**, when the current reliance needs observation, names the empirical claim and scope, domain result and result episteme, dated evaluation or measurement Work, actual bindings required by the measurement rule, qualification window, A.10 evidence-provenance path, and any separately current B.3 assurance claim. Those objects support this bounded use; they do not create the result or make the structural relation obtain.

The selected support stays below the readable claim. It makes the needed basis inspectable without forcing unused assurance machinery into the Working-Model.

### E.14:6 - Archetypal Grounding *(System and Episteme cases)*

> **Tell–Show–Show.** The principle is stated once, then shown on a `U.System` case (structural) and on a `U.Episteme` case (knowledge‑bearing), in line with the authoring template.

#### E.14:6.1 - `U.System` — Working‑Model first, Constructive grounding available

* **Publication (Working‑Model).** Authors state structure using familiar relations (e.g., *Impeller* **ut\:ComponentOf** *Pump*; *Pump* **ut\:ComponentOf** *Skid*). Nothing else is required for readers to follow the design.
* **Assurance (downward grounding).** When the publication elects `B.3.5`, first recover the exact skid, parts, direct fastening, coupling, enclosure, terminal, flange, and seal occurrences, the applicable skid assembly rule, and the skid reidentification rule. Then link the readable claim to one current C.2.1 `sum` trace that reports those facts and declare `validationMode=axiomatic`. If another named current requirement calls for a construction account, follow its stated obligations instead of borrowing `B.3.5` automatically. The account remains below the Working-Model; order and time stay in their own relation families.
* **Canonization move.** Readers continue to see Working‑Model relations as the primary Working-Model text; the constructive story is *supporting*, not *defining*.

#### E.14:6.2 - `U.Episteme` - Working-Model first; Logical, Mapping, and exact empirical support as appropriate

* **Publication (Working-Model).** Authors connect meaning-bearing epistemes or publications using exact knowledge relations (for example, **RepresentationOf** or **UsageOf**) in the same human-oriented style.
* **Assurance (downward grounding).** If the direct knowledge relation is sufficient, stop after the readable claim. When interpretation or alignment needs assurance, select Logical or Mapping support. When observation is the right currency, name the target claim, scope and window, dated evaluation or measurement Work, every performer System, and the Method the Work enacted. Say which assignment the Work was performed under and check that link with F.6; use A.2.1 for the assignment itself. Keep the rest of the complete A.15.1/F.6 basis recoverable. Cite a MethodDescription or local system-role-kind classification only when the claim uses it. Then name the participants or A.6.1 bindings, domain-local result and result episteme, A.10 evidence-provenance path, and any B.3 assurance claim that the assurance use consumes. A record, provenance value, assignment, or assurance tuple is not the observation, Work, performer, or result.
* **Canonization move.** Working-Model text remains the public form; the exact result and support chain stays available underneath without leaking method, record, or time semantics into the subject claim.

#### E.14:6.3 - Pump-vibration measurement: short recognition, exact assurance underneath

**Recognition text.** `Pump-37 vibration at 09:00 was 2.1 mm/s with stated uncertainty 0.2 mm/s under the current inspection method.` A maintenance reader can use that bounded statement and stop before the machinery below. It does not by itself say the pump passes a maintenance criterion, that work may start, or that any gate or permission is current.

**Assurance text.** This worked slice elects empirical assurance for a current reliance question. `Pump37InspectionPlan-E3`, admitted as a `U.WorkPlan`, had designated the intended measurement and selected `PumpVibrationMeasurementMethod-E2`, admitted as a `U.Method`; it cited `PumpVibrationProcedure-E5`, admitted as a `U.MethodDescription`, only for the setup and calibration claims used by the plan.

The measurement domain declares `PumpVibrationMeasurementAssignment` as the assignment species for this work. `RA-ConditionMonitoring-7-E4` is its occurrence, is held by `ConditionMonitoringSystem-7`, and covers the measurement interval. That System performed the admitted Work `Pump37VibrationMeasurement-2026-07-31T0900` under the assignment, and the Work enacted `PumpVibrationMeasurementMethod-E2`. Check the Work and enacted Method with A.15.1, and the Work-assignment attribution with F.6. The applicable A.6.1 bindings identify `Pump-37`, the sensor indication, calibration coefficients, and returned measurement value. Classification of the System under `PumpVibrationMeasurementSystemRole` is a separate claim.

Use C.16 to characterize the domain-local measurement result by its exact Characteristic, Scale, unit, uncertainty, time stance, and interpretation basis. C.2.1 identifies `Pump37VibrationResult-E4`, the episteme that states that result. A.10 path `Pump37MeasurementProvenancePath-E6` cites the calibration, Work, bindings, and source publications; B.3 assurance claim `Pump37MeasurementAssurance-E2` qualifies only the stated use and window. Neither provenance nor assurance is the measurement result. No A.15.PROD claim is needed merely because the result episteme exists; open that pattern only if a separately current question asks whether the exact measurement Work first constituted that episteme.

**What changes in practice.** A reader sees the usable statement first, can inspect the exact Work, result, and support chain when reliance matters, and uses the applicable maintenance-criterion, readiness, gate, or permission pattern if the next decision asks one of those different questions.

#### E.14:6.4 - Pattern lesson

The **Working-Model layer remains the canonical publication face** for authors and assurance readers. A direct claim outside an elected profile carries no E.14 assurance fields. When assurance is current, Mapping, Logical, Constructive, and Empirical support remain purpose-selected shoulders beneath the claim. They preserve a short recognition route while keeping the facts, Work, local results, provenance, assurance, and currentness consumed by that use recoverable through the patterns that define them.

### E.14:7 - Bias-Annotation *(what to watch for, and the counter-moves)*

| Bias (name) | Symptom in drafts | Conceptual counter-move | Where to check this |
| --------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Formalism capture**             | Treating a constructive narrative as “the real thing,” with **ut:\*Of** reduced to a label. | Re‑assert Working‑Model primacy: publish in **ut:\*Of**; attach assurance **downwards** only when needed.                                      | E.8 template; Notational‑Independence guard‑rail.                    |
| **Canonical inversion**           | Demanding constructive grounding for epistemic links by default.                            | Keep the **progressive** stance: prefer Logical/Mapping assurance for knowledge claims; raise to Constructive only when structure is at issue. | Authoring template; Working‑Model pattern family.                    |
| **Layer leakage (order and time)** | Encoding sequence or phase as part-whole to "strengthen" claims. | Keep **order** and **time** in their own relation families; do not smuggle them into structure. | Temporal and ordering patterns. |
| **Collection and composition swap** | Using **MemberOf** as if it implied **ComponentOf**, or treating a `set` narrative as the source of membership. | Keep direct collection identity and membership occurrences separate from integrated assembly; a C.13 account reports those facts and creates none of them. | Working-Model mereology guidance in Parts B and C. |
| **Notation lock‑in**              | Letting a diagram or syntax define meaning.                                                 | Apply **Notational Independence**: define semantics in prose (maths if needed); treat renderings as informative.                               | Notational‑Independence guard‑rail.                                  |
| **Backwards dependency**          | Letting an assurance publication or record redefine public terms.                                        | Preserve **unidirectional dependence**: Working-Model terms do not derive their meaning from assurance publications or records.                              | Part E guard‑rails (dependency discipline).                          |
| **Silent assurance posture** | A claim covered by an elected assurance profile omits the posture required by that profile. | Keep the readable claim first, then declare only the posture and support required for the covered use. A direct claim outside a profile needs no E.14 mode. | Applicable assurance profile; `B.3.5` for CT2R-LOG. |

> **Reading reminder.** Bias checks are *conceptual* reading aids; they never introduce notational or tooling mandates.

### E.14:8 - Conformance Checklist *(normative; author‑facing duties for thought and prose)*

| ID                                         | Requirement                                                                                                                                                                      | Purpose                                                       |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑E14‑1 (Working‑Model primacy).**      | Authors **SHALL** publish claims in **Working‑Model** form (human‑oriented **ut:\*Of** relations or equivalent domain statements) as the canonical publication face for readers.          | Preserve human‑first canon and didactic clarity.              |
|**CC-E14-2 (Downward grounding).** | When assurance is attached, grounding **SHALL** flow **downwards** from the Working-Model to the appropriate assurance shoulder (**Mapping, Logical, Constructive, or Empirical**) and **SHALL NOT** impose vocabulary back onto the Working-Model. | Maintain relation-family separation and cognitive economy. |
| **CC-E14-3 (Assurance posture).** | For a claim covered by an elected `B.3.5` profile or another named current assurance requirement, the author **SHALL** declare the posture required there. Under `B.3.5`, covered claims declare `validationMode`; a direct claim outside such a profile needs no E.14 mode. | Make selected assurance intent explicit without taxing ordinary direct use. |
| **CC-E14-4 (No order or time in structure).** | Authors **SHALL NOT** encode execution order, parallelism, or temporal coverage as part-whole; keep them adjacent in their own relation families. | Prevent layer leakage and category errors. |
| **CC‑E14‑5 (Collection differs from composition).** | Authors **SHALL** keep exact membership occurrences and collection identity distinct from component relations and integrated assembly. A gathering description or `set` trace creates neither membership nor component status. | Preserve the direct relation and identity boundaries. |
| **CC‑E14‑6 (Notational independence).**    | Core meaning **MUST NOT** hinge on a specific diagram or syntax; any rendering present **SHALL** be marked informative.                                                          | Ensure longevity and cross‑discipline portability.            |
| **CC‑E14‑7 (Layer direction).**            | Authors **SHALL** avoid back-defining Working-Model terms by their assurance publications or records; dependence is one‑way (Working‑Model → Assurance).                                       | Preserve unidirectional dependence of layers.                 |
| **CC‑E14‑8 (Template compliance).**        | Sections **SHALL** follow the canonical pattern order; *Archetypal Grounding* is mandatory for architectural patterns.                                                                            | Keep patterns comparable and auditable by reading.            |
| **CC‑E14‑9 (Progressive formality).**      | Authors **SHOULD** escalate assurance deliberately (from working claim to reasoned to constructive), and use **Empirical Validation** where observation is the right currency.    | Support staged formality without overloading early drafts.  |
| **CC-E14-10 (Structural grounding handshake).** | When a publication elects `B.3.5` for a structural assertion, the author **SHALL** keep the readable claim first, declare `validationMode=axiomatic`, and link through `tv:groundedBy` to exactly one current C.2.1 construction-trace episteme in a C.13 `sum`, `set`, or `slice` form. Another named current assurance requirement governs its own obligations. Outside those conditions, a direct structural claim has no E.14 mode, link, or trace obligation. In every case, the direct relation pattern and the candidate's identity or reidentification rule decide occurrence and continuity; a trace and mode create neither. | Makes selected construction assurance inspectable while keeping ordinary use, ontology, identity, and currentness separate. |
| **CC‑E14‑11 (Postulate and empirical-result bindings).** | For `validationMode=postulate`, authors **SHALL** state the target claim and scope and **SHOULD** supply brief empirical cues that would ease later validation. That posture alone requires no dated Work, result, complete basis, provenance path, or assurance claim. When evaluation or measurement actually occurred and the current assurance use relies on its result, authors **SHALL** keep one complete A.15.1/F.6 basis recoverable and name the target claim, scope, qualification window, dated Work, every performer System, and at least one Method the Work enacted. They **SHALL** use F.6 to establish each Work-assignment attribution; the assignment species and occurrence remain separate A.2.1 claims. Any current MethodDescription or local system-role-kind classification, direct participants or A.6.1 bindings, domain-local result and result episteme, A.10 evidence-provenance path, and B.3 assurance claim remain separate. Expose only identities the bounded assurance use consumes; another named current assurance requirement keeps its own obligations. | Keeps a scoped working claim distinct from completed empirical Work while preserving replayable support when a result is actually used. |
| **CC-E14-12 (F-declaration).**             | Normative Working-Model publications **SHALL** declare `U.Formality = Fk` per **C.2.3** (**recommended F ≥ F3** for readable publications). Assurance publications or records **MAY** carry higher F; **min-F** applies to composites. | Aligns E.14 with the unified Formality characteristic; avoids obsolete “tiers/modes”. |
| **CC‑E14‑13 (Light records, not thin prose).** | Authors **SHALL NOT** use the Working‑Model-first stance as a reason to strip problem framing, rationale, or worked slices out of the pattern text. Ordinary use may stay light, but readers **MUST** still be able to understand the pattern without nearby project notes. | Keeps human-facing economy from collapsing into under-explained prose. |
| **CC‑E14‑14 (Recognition text before assurance text).** | When a pattern claims a Working‑Model or other human-facing benefit, authors **SHALL** keep recognition-first working text distinct from the heavier assurance text. The assurance text **MAY** refine and justify the working text, but it **SHALL NOT** silently change the recognition-text claim. If the pattern claims broad or transdisciplinary reach, the working text **SHOULD** show heterogeneous situations early, preferably through an `F.16`-style example matrix or an equally explicit alternative. | Keeps Working‑Model-first drafting from collapsing into either thin prose or late-only universality. |

*All obligations above are **conceptual** and apply to thought and prose; they introduce no notational or data‑processing requirements.*

**E — Conceptual Examples (no notation, no data handling)**

1. **Exact skid assembly -> “Component Of”**
   For PumpSkid 7, recover the pump, frame, reservoir, valve set, and other constituents; the direct fastening, coupling, enclosure, terminal, flange, and seal occurrences that obtain; the applicable skid assembly rule; and the skid reidentification rule. The team may publish each truthful **Component Of** claim and stop there. If the publication elects `B.3.5`, keep that readable claim first, link it to one current C.2.1 `sum` trace that reports the basis, and declare `validationMode=axiomatic`. The same parts unconnected or assembled differently do not thereby form PumpSkid 7. A permitted pump replacement may preserve PumpSkid 7. The direct relations and reidentification rule decide; the trace and posture do not.

2. **Exact collection memberships -> “Member Of”**
   For a four-cartridge bank, identify the exact collection, its collection-identity rule, and each direct membership occurrence. A C.13 `set` trace can then report that construction for assurance. Parallel use, physical proximity, a list, or an author's gathering act does not license **Member Of**, does not imply **Component Of**, and does not make the bank an acting system.

3. **Exact bearer, facet, and aspect -> “Aspect Of”**
   For the thermal envelope of one reactor, identify the reactor bearer, the thermal-envelope aspect, the thermal facet being used, the **Aspect Of** occurrence, and the aspect's identity rule. A C.13 `slice` trace can report those facts. Selecting a view, naming a facet, carving a diagram, or choosing a time window creates no aspect occurrence and no independent system.

> **Notes across the examples**
> • Everyday labels (*Component Of, Member Of, Aspect Of*) remain the only labels engineers need to see; direct relation facts make them true or false. When an assurance profile calls for a construction account, the linked trace makes that basis inspectable.
> • Structural assertions covered by an elected `B.3.5` profile use Constructive assurance. Direct structural claims outside the profile can stand without E.14 assurance fields; epistemic assertions such as “Representation Of” or “Usage Of” use the direct logical or evidence relation appropriate to the claim.

**F — Resulting Context (after you apply the pattern)**

**What improves**

* **One readable structural vocabulary.** Teams can ask which relation obtains—component, member, aspect, or another direct kind—without exposing assurance machinery in ordinary work. When a profile calls for support, assurance readers can also recover the participants, direct relation facts, construction rule, and identity conditions behind the published assertion.
* **Explicit identity tests.** Input lists and traces do not decide identity. Different assembly relations can make the same listed inputs another whole; an admitted replacement can preserve one whole. Collections use their own identity rule and exact memberships; aspects use the exact bearer, facet, direct relation, and aspect identity.
* **Layer harmony.** Engineer-facing labels live at the same level as other relation names, while their warrants and construction accounts live one step below, keeping human language clean and the claim basis auditable.

**What to watch**

* **Discipline for structural relation kinds.** A published structural assertion is unsafe when its direct relation basis or identity test is missing, even if a trace or `axiomatic` flag exists. Conversely, forcing epistemic links to pretend they are structural over-physicalises knowledge claims; for those, a direct logical or evidence relation is the right currency.
* **Author workload moves, not grows.** Day-to-day model authors stay with working labels; specification authors must recover the direct relation occurrence and identity test and keep one current construction account when this publication policy requires it. The account supports review; it does not repair missing world-side facts.

**Invariants you must preserve**

* **Parsimony of construction accounts.** Use `sum` to report integrated assembly, `set` to report a collection, and `slice` to report an aspect. Do not treat them as generative acts or add forms for parallelism or time-slicing; order and time remain with their own patterns.
* **Relation-kind-specific justification.** A direct structural claim needs grounded relation occurrences and its applicable identity test. It needs an inspectable construction account only when an elected profile or named current requirement calls for one. Epistemic claims use the logical or evidence relations they actually need. No assurance route changes the relation kind being claimed.

**Known consequences**

* **Stable queries, fewer surprises.** Working labels retain one direct meaning across disciplines. When a structural assertion is covered by an assurance profile, readers can also follow it to the facts and identity conditions reported in its construction account.
* **Audit trail without jargon.** When construction assurance is current, reviewers can follow a structural claim to its participants, direct relation occurrences, construction rule, identity conditions, and trace edition while everyday collaborators keep using familiar relation names.

### E.14:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Machinery-first working text | The reader meets constructor traces, proof apparatus, or evidence ids before the working model. | Put the recognition text and chosen Working-Model labels first; keep assurance below. |
| Assurance leakage upward | Mapping, proof, or empirical records rename the public working vocabulary. | Preserve downward grounding: Working-Model terms are not back-defined by assurance publications. |
| Slash-label compromise | Several source labels are displayed because no model value was chosen. | Use Mapping to record source labels and show one chosen Working-Model label. |
| Structure-time collapse | Order, phase, or execution is encoded as part-whole structure. | Keep time and order in their own relation families. |
| Forever-light prose | Human-facing prose becomes so small that the reader cannot recover the problem, payoff, or assurance boundary. | Keep recognition text concise but still include problem framing, rationale, and worked slices. |

### E.14:10 - Consequences

| Benefits | Trade-offs and mitigations |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Human-first clarity.** Readers see the **Working-Model layer** as the canonical publication form. Direct claims carry no assurance fields by default; selected assurance remains purpose-driven and below the claims. | **Extra author discipline only when assurance is current.** Declaring the required posture and writing a short grounding account takes effort; the authoring template and style guide keep that addition bounded. |
| **Progressive assurance.** Teams can start with the direct claim and add Mapping, Logical, Constructive, or Empirical support deliberately without changing the visible relation. | **Risk of “forever-light.”** Some models may remain weakly assured; formal maturity checks and assurance prompts show where risk warrants more support. |
| **Layer hygiene.** Order and time remain outside mereology; structural identity is neither overloaded nor diluted. | **Split attention.** Authors must learn to keep relation families distinct; mitigated by the Tell-Show-Show pedagogy across architectural patterns. |
| **Spec cohesion.** The same section order and safety subsections (Bias‑Annotation, Conformance Checklist) keep patterns comparable and auditable.             | **Tighter prose.** Patterns grow by a few concise checks; mitigated by the canonical template.                                                                               |

> **Quotable closer.** *“One layer to speak, three layers to justify—only when needed.”*

### E.14:11 - Rationale

**Why Working-Model is canonical.** FPF privileges **human-oriented relations** as the primary language and working representation for thinking and communication. This satisfies didactic primacy while preserving conceptual integrity: formal work serves the human layer, not the other way around. The canonical template and style principles institutionalise this choice without inviting notation lock-in.

**Why grounding flows downward.** The direct claim stands on the pattern that defines or tests it. When assurance is current, Mapping, Logical, Constructive, and Empirical support sits beneath that claim, and the applicable profile or requirement says what must be declared. Authors select only the support that fits purpose and risk: type and lexical alignment (**TA**), reasoned consequence (**VA**), constructive reconstruction (**VA**), or real-world confirmation (**LA**). This keeps the Kernel small, keeps different kinds of claim apart, and provides a path to higher assurance when warranted.

**Why patterns teach before they tighten.** The Tell‑Show‑Show requirement couples each universal rule with System and Episteme cases, reducing cognitive load and preventing premature formalism. It is the didactic mechanism that makes Human‑Centric Canonization practical across disciplines.

**Why no notation talk in Core.** Guard‑rails and the style guide prohibit tool jargon and notation dependence inside normative prose; meanings are given in words and mathematics, with any renderings treated as illustrative only. This preserves longevity and cross‑disciplinary portability.

### E.14:12 - SoTA-Echoing

| Source line | What E.14 adopts | Boundary |
| --- | --- | --- |
| Human-centered design and cognitive ergonomics | Working readers need a small, usable model before assurance apparatus. | Usability does not license vague or under-explained prose. |
| Formal methods and model-based assurance | Heavy justification can remain available below the working text. | Assurance artifacts do not define the public Working-Model vocabulary. |
| Ontology engineering and mapping practice | Source labels, synonyms, and registers are captured in mapping rather than shown as slash labels. | Mapping is not a second public vocabulary. |
| Constructive ontology and constructional mereology | Structural claims can carry an inspectable account of independently grounded construction facts when identity matters. | The account creates neither the direct relation nor whole identity and is not the default assurance route for epistemic claims. |

### E.14:13 - Relations

**Builds on:**

* **E.8 Authoring Conventions & Style Guide** — section order, style principles, and mandatory safety subsections used here.
* **E.7 Archetypal Grounding** — the Tell‑Show‑Show rule applied in this pattern’s own Grounding section.
* **C.2.3 Unified Formality Characteristic (F)** — declares the **F** scale and **ΔF** moves for progressive rigor; Working-Model publications **SHALL** declare **F** and remain notation-agnostic.

**Coordinates with.**

* **CT2R-LOG — Working-Model Relations and Grounding** — supplies the optional elected profile that adds `validationMode` and, for covered structural assertions, `tv:groundedBy`; direct relations outside the profile need neither field.
* **Compose-CAL (Constructional Mereology)** — supplies the `sum`, `set`, and `slice` trace content when construction assurance is selected; the trace does not define the Working-Model relation or its identity.
* **E.10 Lexical Discipline & Stratification** — ensures naming discipline and register hygiene when the human layer is published.

**Constrains:**

* All architectural patterns that publish relations **SHALL** present the readable Working-Model claim first. A direct relation outside an elected assurance profile needs no E.14 assurance field. When `B.3.5` or another named current requirement applies, attach only its required support below the claim while preserving relation-family separation and notational independence. (Template conformance as per E.8.)

**Informs.**

* Part F unification practices (context of meaning, bridges, fit levels) by reinforcing the preference for human‑readable labels with explicit alignment notes rather than silent formal substitutions.

### E.14:End

