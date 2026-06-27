## E.14 - Human‑Centric Working‑Model
> **Status:** Stable
> **Type:** Pattern

### E.14:0 - Use This When

Use this pattern when FPF text needs to stay readable as one human working model while heavier mapping, logical, constructive, or empirical assurance remains recoverable underneath it.

**What goes wrong if missed.** The working text either drifts into local jargon and slash labels or calcifies into proof machinery that practitioners cannot use in ordinary design, review, or management work.

**What this buys.** A working reader sees one small model first, while assurance readers can still recover mapping, logical, constructive, and empirical grounding without forcing that machinery back into the Working-Model vocabulary.

### E.14:1 - Intent

Establish a **single, human‑centric Working‑Model** that practitioners can read, discuss, and evolve **without exposure to formal machinery**.
Each statement **declares a justification stance** (`validationMode`) and, when assurance is sought, attaches **appropriate grounding** via one or more assurance shoulders — **Mapping**, **Logical**, **Constructive** — and **may additionally attach Empirical Validation** (evidence) as defined by the Trust & Assurance calculus. Empirical Validation can accompany any stance; it is **required** when the stance is *postulate*. Assurance shoulders sit **beneath** the Working‑Model and **never define its vocabulary**.

Put bluntly: *one model people work in; three assurance shoulders — plus empirical checks when the world is the judge.*

### E.14:2 - Problem Frame

Teams need **one shared Working-Model** to make decisions at speed. Historically this shared model either:

* **drifts into jargon** - different terms for one shared working-model value, slash-labels, partial overlaps; or
* **calcifies into machinery** - too formal for day-to-day design and review.

Both failure modes create friction between two audiences:
(1) **working users** (engineers, programme managers, policy owners) who need a **small, stable Working-Model text**, and
(2) **assurance authors** (ontologists, methodologists, auditors) who need **proofs that the Working-Model text is sound**.

E.14 resolves the impasse by **separating concerns**:

* A **Working-Model layer**: curated kinds and relations expressed in plain terms, governed by simple human rules.
* An **Assurance stack** beneath it - **Mapping**, **Logical**, **Constructive** - that carries the heavy arguments (concept alignment, relational semantics, generative traces) and **never leaks back** into the Working-Model narrative.

This pattern dovetails with the framework's unification stance (**small Working-Model text, rigorous foundations**) and with our constructional mereology commitments (**sum/set/slice** provide extensional identity), while keeping the Kernel minimal and meta-only.

### E.14:2.1 - Problem

A reader may need to decide, design, review, or coordinate with FPF terms before they are ready to inspect mapping tables, constructive traces, evidence records, or proof arguments. If the working text exposes all of that machinery first, the model becomes unusable; if it hides the machinery completely, the model becomes arbitrary. E.14 keeps one human-facing Working-Model visible while making the assurance shoulders recoverable beneath it.

### E.14:3 - Forces

1. **Cognitive economy vs. semantic precision.**
   Managers and engineers must navigate with a handful of names and relations; assurance authors must still certify that those names and relations **are unambiguous and extensional**.

2. **Speed of change vs. guarantees.**
   The Working‑Model must accommodate rapid iteration; the Assurance stack must **lag just enough** to check, without blocking practical progress.

3. **Parsimony vs. expressivity.**
   The Working‑Model should **not proliferate relation types or ad‑hoc categories**; fine‑grained distinctions live in the Assurance layers and are shown **only when they materially change a decision**.

4. **Downward grounding vs. upward contamination.**
   Grounding must always flow **down** (Working‑Model → Mapping → Logical → Constructive). No dependence **up** is allowed: proofs and traces never dictate wording or layout in the Working‑Model.

5. **Trans‑disciplinary unification vs. local dialects.**
   The Working‑Model must reconcile different disciplines’ habits **without erasing them**; Mapping captures dialects, while the Working‑Model exposes a **single usable choice**.

6. **Auditability vs. readability.**
   Every Working‑Model statement must be **auditable on request**, yet day‑to‑day views **hide the scaffolding** unless summoned.

### E.14:4 - Solution

#### E.14:4.1 - Human-Centric principles

##### E.14:4.1.1 - Recognition text and assurance text
Human-facing patterns also need EntityOfConcern stability across the two reading-order text blocks. The working reader should not meet one object in the recognition text and a different ontological kind in the assurance text. If the pattern distinguishes an EntityOfConcern, the interpretive or operational move applied to that object, and the wider review or work process around it, those distinctions should be made explicit rather than hidden behind stylistic noun-swapping.

Working-Model-first drafting therefore also means subject-domain-first drafting. If a pattern is meant to help with a real review, design, cultural, research, or operational problem, the recognition text should open from that problem-owning moment before internal taxonomy or package architecture. If a broader umbrella head and a narrower operative branch are both live, the pattern should state that stack plainly enough that a cold reader can tell what the umbrella names, what branch is current, what object is governed, what move is being carried, and what wider work remains outside.

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
> **E.14‑P.1 – Working‑Model first, stance explicit.**  **
> Operate one **Working‑Model** for all human‑facing discussion. For **each** assertion, the author **SHALL declare** a justification stance (`validationMode`) and choose the **appropriate assurance shoulder(s)**: **Mapping** (term↔kind alignment via **Lang‑CHR** / D‑Projection), **Logical** (CT2R label-meaning rules, scope/constraints), **Constructive** (Γₘ generative trace), and **Empirical Validation** (an evidence-use relation for the claim, with scope, timespan, provenance, and declared `U.BoundedContext`).

> **E.14‑P.2 – Downward‑only dependency.**
> Information **may** flow from the Working‑Model down into any Assurance layer; **no Assurance layer may impose vocabulary or shape back upward** into the Working‑Model.
>
> **E.14‑P.3 – Small working text, big proof.**
> The Working‑Model exposes a **minimal set** of names (L‑1/L‑2 registers) and **a compact family of relations** used in everyday reasoning; precision and completeness are **proved below**.

> **E.14‑P.4 – Human registers first.**
> Terms in the Working‑Model are deliberately curated for **human legibility** (register‑badged, synonym‑aware). Synonym capture and language variance belong to Mapping; **only the chosen canonical label appears in the Working-Model text**.

> **E.14‑P.5 – Justification modes are explicit.**
> Each Working‑Model relation **declares** `validationMode ∈ {axiomatic, inferential, postulate}`.
> _axiomatic_ -> **Constructive** grounding (Γ_m trace via `tv:groundedBy`); _inferential_ -> **Logical** grounding (reasoned chain, often KD-CAL-backed for epistemic ties); _postulate_ -> **Empirical Validation** (evidence-use relation with scope and timespan). Empirical Validation (**LA**) may also accompany _inferential_ or _axiomatic_ claims as real-world confirmation. **Mapping** contributes **TA**, **Logical and Constructive** contribute **VA**, and **Empirical** contributes **LA** (per the Trust & Assurance calculus; no calculus variables appear in the Working-Model text).

> **E.14‑P.6 – Parsimony in the working text.**
> No new Working‑Model relation types are introduced if the existing Logical label-meaning rules plus Constructive grounding suffice to capture the intended meaning.

> **E.14‑P.7 – Evidence is first-class claim grounding.**
> When *postulate* is chosen, authors **SHALL** attach an **evidence pointer** (Empirical Validation) appropriate to the claim and context, governed as an evidence-use relation within a declared `U.BoundedContext`.

> **E.14‑P.8 – Working-model-first is not explanation-thin.**
> Human-facing parsimony does **not** license under-explained pattern prose. When a pattern claims a Working‑Model benefit, it **SHALL** still provide enough problem framing, rationale, and worked slices that readers can tell what the model clarifies, what remains on the assurance shoulders, and when a heavier review path is required.

### E.14:5 - Layer Standard & Downward Flow (Working‑Model → Assurance)

This section defines **what each layer is for**, **what it guarantees**, and **how a single Working‑Model statement is carried down**.

#### E.14:5.1 - Working‑Model (what humans see)

**Purpose.** A small, curated graph of kinds and relations that a mixed team can read at a glance.

**Elements.**

* **Kinds** — one **chosen concept** per node (no slash‑labels).
* **Relations** — a short list intelligible to non‑specialists (e.g., *Component‑of*, *Member‑of*, *Aspect‑of*, plus a small number of cross‑disciplinary ties such as *Interface‑of* or *Constituent‑of*).
* **Language register badges** — labels shown in the Working-Model are L‑1 or L‑2; L‑3/L‑4 remain in Mapping as synonyms or symbols.

**Obligations.**

* Every Working‑Model edge and node is **grounded downward** (see below).
* The Working‑Model **does not display** constructor jargon, proof terminology, or evidence identifiers; those live in Assurance and are **available on demand**.

#### E.14:5.2 - Assurance-1: Mapping (from words to chosen governed values)

**Purpose.** Consolidate human labels from varied sources and **bind them to the chosen governed values** used on the Working-Model, including admitted U-kinds where kindhood is live.

**Guarantee.** For any Working-Model label, there exists a **stable alignment** to exactly one chosen governed value in the current scope; synonyms, abbreviations, locales, and registers are recorded here, **not** in the displayed Working-Model. Mapping primarily raises **Concept-Bridge Assurance (CBA)** by consolidating synonyms/registers and binding tokens/labels to the chosen governed value; calculus-level metrics live outside Part E.

**Deliverable.** A compact alignment table per scope that makes it obvious which **one label** the Working‑Model will show and which background source labels are recognized only as source wording.

*(Rationale: Working teams speak many dialects; the Working‑Model speaks one. Mapping is the interpreter.)*

#### E.14:5.3 - Assurance‑2: Logical (from Working‑Model relations to label semantics)

**Purpose.** Give each Working-Model relation **one precise intended meaning** and **its admissible use cases**, keeping the Working-Model vocabulary small.

**Guarantee.** A Working‑Model edge such as *Component‑of* or *Aspect‑of* **carries one intended reading** (transitivity/antisymmetry expectations, scope notes), sufficient for auditors to assess whether the **use is legitimate** in a given context.

**Deliverable.** A short set of label-meaning rules: “When an edge is labeled *Component‑of* in the Working-Model text, it intends the structural reading that construction can verify when assurance is live.” The Logical layer is **the Standard** that ties human labels to accepted meanings (CT2R label rules); it primarily contributes **Verification Assurance (VA)**. Calculus-level symbols are not used in E-patterns.

*(Rationale: logical label alignment protects the small Working-Model text from relation proliferation while keeping meanings crisp.)*

#### E.14:5.4 - Assurance‑3: Constructive (from meanings to generative traces)

**Purpose.** Provide **extensional guarantees** by **constructing** the wholes, collections, and slices that Working-Model relations speak about.

**Guarantee.** For structural edges, **there exists a constructional narrative** (e.g., *sum*, *set*, *slice*) that, if told, would recreate the whole from its parts or the aspect from its bearer; this makes identity and containment **trackable and testable** across scales.

**Deliverable.** A **single generative story** per structural link (axiomatic justification). For non-structural ties in the Working-Model text (e.g., epistemic links), Constructive may be absent; Logical/Empirical take the lead. Constructive contributes **VA** (extensional identity via Γₘ); for **structural** edges, `tv:groundedBy` **MUST** reference exactly one Γₘ trace.

*(Rationale: constructional grounding turns everyday part‑whole talk into statements whose identity conditions are not left to taste.)*

#### E.14:5.5 - Assurance‑4: Empirical Validation (from claims to observed world)

**Purpose.** Record when and where a Working-Model claim meets reality.
**Guarantee.** Every empirical binding names a **`U.BoundedContext`**, a **target claim/scope**, and a **timespan**; **staleness/refresh** are managed per context policy.
**Deliverable.** An evidence-use relation or provenance/evidence pointer anchored into the Evidence-Provenance chain; it names the target claim, scope, bounded context, timespan, and provenance anchors. Empirical Validation contributes **LA** (raises empirical **R** and constrains **G** to its validated envelope).

#### E.14:5.6 - The downward grounding for a single Working-Model statement

Consider a Working‑Model arrow **A –Component‑of→ B**:

1. **Mapping** shows that the words *A* and *B* are the chosen labels for their kinds; it records background source labels without making them displayed Working-Model names.
2. **Logical** confirms that **Component‑of** in the Working-Model text means the **structural reading** with its ordinary mereological expectations; if the Working-Model text used *Member‑of* instead, Logical would similarly certify the intended reading and its boundaries.
3. **Constructive** exhibits the **constructional narrative** (e.g., a _sum_ of parts resulting in **B** with **A** among them), which yields **axiomatic justification** for the structural edge, sets `validationMode=axiomatic`, and binds the edge via **`tv:groundedBy → Γₘ.sum|set|slice`**.
4. **Empirical Validation** records the **evidence pointer** and scope that make the claim auditable within its `U.BoundedContext` (required for *postulate*; optional reinforcement for other stances).

Together, these assurance shoulders and empirical evidence-use relation **ground the human arrow without leaking their machinery upward**. The Working‑Model remains simple; the Assurance stack carries the proof.

### E.14:6 - Archetypal Grounding *(System / Episteme)*

> **Tell–Show–Show.** The principle is stated once, then shown on a `U.System` case (structural) and on a `U.Episteme` case (knowledge‑bearing), in line with the authoring template.

#### E.14:6.1 - `U.System` — Working‑Model first, Constructive grounding available

* **Publication (Working‑Model).** Authors state structure using familiar relations (e.g., *Impeller* **ut\:ComponentOf** *Pump*; *Pump* **ut\:ComponentOf** *Skid*). Nothing else is required for readers to follow the design.
* **Assurance (downward grounding).** When a higher-assurance claim is sought, the same author **narrates** the constructive story of the whole as a composition of parts and, where appropriate, attaches a downward grounding to that narrative (sum, set, or slice). The narrative remains concept-level and notation-neutral; order and time stay out of structure and are expressed in their own relation families.
* **Canonization move.** Readers continue to see Working‑Model relations as the primary Working-Model text; the constructive story is *supporting*, not *defining*.

#### E.14:6.2 - `U.Episteme` - Working-Model first; Logical and Mapping preferred; Empirical evidence as appropriate

* **Publication (Working‑Model).** Authors connect meaning-bearing epistemes or publications using knowledge relations (e.g., **RepresentationOf**, **UsageOf**) in the same human‑oriented style.
* **Assurance (downward grounding).** Here assurance typically uses the **Logical** or **Mapping** shoulders (reasoned argument; type/lexical alignment). **Empirical Validation** is used where observation is the right currency: an episteme, observation, or work result is used in an evidence-use relation for a target claim with explicit scope, context, time, and provenance. Constructive grounding is optional and used only where a structural interpretation is genuinely intended.
* **Canonization move.** Again, Working‑Model text is the public form; assurance is attached deliberately and separately, without leaking method or time semantics into structure.

**6.3 - Pattern lesson (both cases)**
The **Working-Model layer remains the canonical publication face** for authors and assurance readers; **assurance layers** (Mapping, Logical, and Constructive) are **opt-in** and used purposefully, with grounding flowing **downwards** from the Working-Model to the appropriate shoulder. This presentation respects the authoring template's *Archetypal Grounding* requirement and keeps notational choices illustrative rather than defining.

### E.14:7 - Bias-Annotation *(what to watch for, and the counter-moves)*

| Bias (name)                       | Symptom in drafts                                                                           | Conceptual counter‑move                                                                                                                        | Where this is governed                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Formalism capture**             | Treating a constructive narrative as “the real thing,” with **ut:\*Of** reduced to a label. | Re‑assert Working‑Model primacy: publish in **ut:\*Of**; attach assurance **downwards** only when needed.                                      | E.8 template; Notational‑Independence guard‑rail.                    |
| **Canonical inversion**           | Demanding constructive grounding for epistemic links by default.                            | Keep the **progressive** stance: prefer Logical/Mapping assurance for knowledge claims; raise to Constructive only when structure is at issue. | Authoring template; Working‑Model pattern family.                    |
| **Layer leakage (order/time)**    | Encoding sequence or phase as part-whole to "strengthen" claims.                            | Keep **order** and **time** in their governing relation families; do not smuggle them into structure.                                                                   | Style/structure guidance in Part E; flavour separation in Γ-family.  |
| **Collection ↔ Composition swap** | Using **MemberOf** as if it implied **ComponentOf** identity.                               | Keep collections (*set*) distinct from assemblies (*sum*); do not upgrade membership to component status.                                      | Working‑Model mereology guidance (Part B/C linkage).                 |
| **Notation lock‑in**              | Letting a diagram or syntax define meaning.                                                 | Apply **Notational Independence**: define semantics in prose (maths if needed); treat renderings as informative.                               | Notational‑Independence guard‑rail.                                  |
| **Backwards dependency**          | Letting an assurance publication or record redefine public terms.                                        | Preserve **unidirectional dependence**: Working-Model terms do not derive their meaning from assurance publications or records.                              | Part E guard‑rails (dependency discipline).                          |
| **Silent stance**                 | Publishing claims with no declared assurance stance.                                        | Declare the stance explicitly (e.g., working claim vs reasoned vs constructive).                                                               | Style/authoring discipline in Part E.                                |

> **Reading reminder.** Bias checks are *conceptual* reading aids; they never introduce notational or tooling mandates.

### E.14:8 - Conformance Checklist *(normative; author‑facing duties for thought and prose)*

| ID                                         | Requirement                                                                                                                                                                      | Purpose                                                       |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| **CC‑E14‑1 (Working‑Model primacy).**      | Authors **SHALL** publish claims in **Working‑Model** form (human‑oriented **ut:\*Of** relations or equivalent domain statements) as the canonical publication face for readers.          | Preserve human‑first canon and didactic clarity.              |
|**CC-E14-2 (Downward grounding).** | When assurance is attached, grounding **SHALL** flow **downwards** from the Working-Model to the appropriate assurance shoulder (**Mapping, Logical, Constructive, or Empirical**) and **SHALL NOT** impose vocabulary back onto the Working-Model. | Maintain relation-family separation and cognitive economy. |
| **CC‑E14‑3 (Stance declaration).**         | For any claim where assurance matters, the author **SHALL** declare `validationMode` (*postulate / inferential / axiomatic*).                                                    | Make assurance intent explicit and readable.                  |
| **CC-E14-4 (No order/time in structure).** | Authors **SHALL NOT** encode execution order, parallelism, or temporal coverage as part-whole; keep them adjacent in their own relation families.                                           | Prevent layer leakage and category errors.                    |
| **CC‑E14‑5 (Collection ≠ Composition).**   | Authors **SHALL** keep **membership** claims distinct from **component** claims; no implicit upgrade from collection to assembly.                                                | Guard extensional identity and reader expectations.           |
| **CC‑E14‑6 (Notational independence).**    | Core meaning **MUST NOT** hinge on a specific diagram or syntax; any rendering present **SHALL** be marked informative.                                                          | Ensure longevity and cross‑discipline portability.            |
| **CC‑E14‑7 (Layer direction).**            | Authors **SHALL** avoid back-defining Working-Model terms by their assurance publications or records; dependence is one‑way (Working‑Model → Assurance).                                       | Preserve unidirectional dependence of layers.                 |
| **CC‑E14‑8 (Template compliance).**        | Sections **SHALL** follow the canonical pattern order; *Archetypal Grounding* is mandatory for architectural patterns.                                                                            | Keep patterns comparable and auditable by reading.            |
| **CC‑E14‑9 (Progressive formality).**      | Authors **SHOULD** escalate assurance deliberately (from working claim to reasoned to constructive), and use **Empirical Validation** where observation is the right currency.    | Support staged formality without overloading early drafts.  |
|**CC-E14-10 (Structural grounding handshake).** | For **structural** edges on the Working-Model, authors **SHALL** set `validationMode=axiomatic` and provide **Constructive** grounding with `tv:groundedBy → Γₘ.sum|set|slice` (see **Compose-CAL** and **CT2R-LOG**). Exactly **one** Γₘ trace is permitted per edge (CI rule alignment). | Aligns E.14 with CT2R-LOG and Compose-CAL; ensures extensional identity. |
| **CC‑E14‑11 (Empirical bindings).**        | When `validationMode=postulate` (or when adding real-world confirmation), authors **SHALL** bind evidence through an evidence-use relation in a declared `U.BoundedContext`, with an explicit target claim, scope, **timespan**, and provenance anchors. | Aligns with Evidence Graph Referring and empirical ageing policies. |
| **CC-E14-12 (F-declaration).**             | Normative Working-Model publications **SHALL** declare `U.Formality = Fk` per **C.2.3** (**recommended F ≥ F3** for readable publications). Assurance publications or records **MAY** carry higher F; **min-F** applies to composites. | Aligns E.14 with the unified Formality characteristic; avoids obsolete “tiers/modes”. |
| **CC‑E14‑13 (Light records, not thin prose).** | Authors **SHALL NOT** use the Working‑Model-first stance as a reason to strip problem framing, rationale, or worked slices out of the pattern text. Ordinary use may stay light, but readers **MUST** still be able to understand the pattern without nearby project notes. | Keeps human-facing economy from collapsing into under-explained prose. |
| **CC‑E14‑14 (Recognition text before assurance text).** | When a pattern claims a Working‑Model or other human-facing benefit, authors **SHALL** keep recognition-first working text distinct from the heavier assurance text. The assurance text **MAY** refine and justify the working text, but it **SHALL NOT** silently change the recognition-text claim. If the pattern claims broad or transdisciplinary reach, the working text **SHOULD** show heterogeneous situations early, preferably through an `F.16`-style example matrix or an equally explicit alternative. | Keeps Working‑Model-first drafting from collapsing into either thin prose or late-only universality. |

*All obligations above are **conceptual** and apply to thought and prose; they introduce no notational or data‑processing requirements.*

**E — Conceptual Examples (no notation, no data handling)**

1. **Assembly from parts → “Component Of”**
   A pump skid is agreed to be nothing over and above its pump, frame, reservoir, and valve set considered together. Because the whole is conceptually *constructed* from those parts, the team may safely speak of each part as *Component Of* the skid. The justification is the construction itself: if any listed part were removed, the very same skid would no longer exist as that whole. This keeps identity extensional and makes the engineer-facing label (“Component Of”) truthful rather than conventional.

2. **Parallel elements gathered → “Member Of”**
   A test rig has four identical cartridges used in parallel. The rig treats them as a conceptual *gathering*; membership is fixed by inclusion in that gathering, not by sequence or timing. Speaking of each cartridge as *Member Of* the rig’s cartridge bank is then licensed by the same gathering act. Engineers can keep saying “member,” while architects know the warrant is the underlying construction of the bank as a collection, not an accidental tagging.

3. **Focused facet carved → “Aspect Of”**
   When the team talks about the *thermal envelope* of a reactor, they are not multiplying entities; they are taking the already‑agreed reactor and conceptually *carving out* its thermal facet for focused reasoning. Calling that carve‑out an *Aspect Of* the reactor is justified because the aspect owes its identity to the parent and the chosen facet, and nothing else. This licenses disciplined talk about “boundary,” “interface,” or “envelope” without mistaking them for independent systems.

> **Notes across the examples**
> • Everyday labels (*Component Of, Member Of, Aspect Of*) remain the only labels engineers need to see; their truth is grounded by prior constructional choices.
> • Structural links draw on **Constructive** grounding; **epistemic links**—like “Representation Of” or “Usage Of”—may instead rely on **Empirical Validation** (evidence-use relations) or **Logical** grounding appropriate to the claim.

**F — Resulting Context (after you apply the pattern)**

**What improves**

* **Single dial for containment.** Teams can ask one plain question, “what is inside what?”, and trust that all structural talk reduces to shared constructional choices rather than ad-hoc relation lists. Ontologists keep rigorous warrants without overloading day-to-day readers.
* **Extensional identity by default.** Wholes are the wholes they are because of the parts gathered; collections are the collections they are because of their members; aspects inherit identity from their parent and facet. This prevents silent drift when labels change.
* **Layer harmony.** Engineer-facing labels live at the same level as other relation names, while their warrants live one step below, keeping human language clean and the generative basis auditable.

**What to watch**

* **Discipline for structural relation kinds.** A structural link that lacks a constructional warrant is conceptually unsafe. Conversely, forcing epistemic links to pretend they are structural over-physicalises knowledge claims; for those, evidence or argument is the right currency.
* **Author workload moves, not grows.** Day-to-day model authors stay with working labels; specification authors carry the responsibility for ensuring every structural statement really follows from a sum, a gathering, or a carve-out. This is a conscious shift of complexity away from operations and into the pattern's foundation.

**Invariants you must preserve**

* **Parsimony of constructors.** Build wholes by summing parts; build banks by gathering elements; focus facets by carving aspects. Do not invent extra generative acts for parallelism or time‑slicing; those concerns belong to other conceptual services.
* **Two-relation-kind justification.** Structural talk rides on construction; epistemic talk rides on evidence or proof. Keep the boundary sharp so that downstream reasoning (about reliability, compliance, or policy) remains clear.

**Known consequences**

* **Stable queries, fewer surprises.** Because working labels are backed by shared constructions, teams from different disciplines can interoperate without renegotiating meanings at hand-off.
* **Audit trail without jargon.** Reviewers can trace every structural claim to a prior constructional choice, while everyday collaborators keep using familiar relation names.

### E.14:9 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Machinery-first working text | The reader meets constructor traces, proof apparatus, or evidence ids before the working model. | Put the recognition text and chosen Working-Model labels first; keep assurance below. |
| Assurance leakage upward | Mapping, proof, or empirical records rename the public working vocabulary. | Preserve downward grounding: Working-Model terms are not back-defined by assurance publications. |
| Slash-label compromise | Several source labels are displayed because no chosen governed value was selected. | Use Mapping to record source labels and show one chosen Working-Model label. |
| Structure-time collapse | Order, phase, or execution is encoded as part-whole structure. | Keep time and order in their governing relation families. |
| Forever-light prose | Human-facing prose becomes so small that the reader cannot recover the problem, payoff, or assurance boundary. | Keep recognition text concise but still include problem framing, rationale, and worked slices. |

### E.14:10 - Consequences

| Benefits                                                                                                                                                      | Trade‑offs / Mitigations                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Human‑first clarity.** Readers see the **Working‑Model layer** as the canonical publication form; Assurance layers remain optional and purpose‑driven.      | **Extra author discipline.** Declaring the stance and (when needed) a short grounding narrative takes effort; mitigated by the authoring template and style guide.           |
| **Progressive assurance.** Teams can start light and raise strictness deliberately (Mapping → Logical → Constructive) without changing the visible relations. | **Risk of “forever‑light.”** Some models may remain in low‑assurance stances; mitigated by formal maturity checks and assurance prompts to escalate where risk warrants.  |
| **Layer hygiene.** Order/time remain outside mereology; structural identity is neither overloaded nor diluted.                                                | **Split attention.** Authors must learn to keep relation families distinct; mitigated by the Tell-Show-Show pedagogy across architectural patterns.                                             |
| **Spec cohesion.** The same section order and safety subsections (Bias‑Annotation, Conformance Checklist) keep patterns comparable and auditable.             | **Tighter prose.** Patterns grow by a few concise checks; mitigated by the canonical template.                                                                               |

> **Quotable closer.** *“One layer to speak, three layers to justify—only when needed.”*

### E.14:11 - Rationale

**Why Working-Model is canonical.** FPF privileges **human-oriented relations** as the primary language and working representation for thinking and communication. This satisfies didactic primacy while preserving conceptual integrity: formal work serves the human layer, not the other way around. The canonical template and style principles institutionalise this choice without inviting notation lock-in.

**Why grounding flows downward.** Mapping, Logical, Constructive, and Empirical supports are **assurance shoulders** that sit *beneath* the Working‑Model claim. Authors select the shoulder(s) that fit purpose and risk: type/lexical alignment (**TA**), reasoned consequence (**VA**), constructive reconstruction (**VA**), and real‑world confirmation (**LA**). This keeps the Kernel small, avoids plane‑mixing, and provides a clear path to higher-assurance guarantees when warranted.

**Why patterns teach before they tighten.** The Tell‑Show‑Show requirement couples each universal rule with System/Episteme illustrations, reducing cognitive load and preventing premature formalism. It is the didactic mechanism that makes Human‑Centric Canonization practical across disciplines.

**Why no notation talk in Core.** Guard‑rails and the style guide prohibit tool jargon and notation dependence inside normative prose; meanings are given in words and mathematics, with any renderings treated as illustrative only. This preserves longevity and cross‑disciplinary portability.

### E.14:12 - SoTA-Echoing

| Source line | What E.14 adopts | Boundary |
| --- | --- | --- |
| Human-centered design and cognitive ergonomics | Working readers need a small, usable model before assurance apparatus. | Usability does not license vague or under-explained prose. |
| Formal methods and model-based assurance | Heavy justification can remain available below the working text. | Assurance artifacts do not define the public Working-Model vocabulary. |
| Ontology engineering and mapping practice | Source labels, synonyms, and registers are captured in mapping rather than shown as slash labels. | Mapping is not a second public vocabulary. |
| Constructive ontology and constructional mereology | Structural claims can be grounded by construction when identity matters. | Construction is used when structure is live, not as a default for every epistemic relation. |

### E.14:13 - Relations

**Builds on:**

* **E.8 Authoring Conventions & Style Guide** — section order, style principles, and mandatory safety subsections used here.
* **E.7 Archetypal Grounding** — the Tell‑Show‑Show rule applied in this pattern’s own Grounding section.
* **C.2.3 Unified Formality Characteristic (F)** — declares the **F** scale and **ΔF** moves for progressive rigor; Working-Model publications **SHALL** declare **F** and remain notation-agnostic.

**Coordinates with.**

* **CT2R‑LOG — Working‑Model Relations & Grounding** — label-meaning rules and `tv:groundedBy` Standard for edges grounded in Γₘ.
* **Compose‑CAL (Constructional Mereology)** — provides the constructive shoulder (Γₘ: **sum | set | slice**) used to ground structural edges.
* **E.10 Lexical Discipline & Stratification** — ensures naming discipline and register hygiene when the human layer is published.

**Constrains:**

* All architectural patterns that publish relations **SHALL** present them in the Working-Model layer and **MAY** attach assurance only as needed, preserving relation-family separation and notational independence. (Template conformance as per E.8.)

**Informs.**

* Part F unification practices (context of meaning, bridges, fit levels) by reinforcing the preference for human‑readable labels with explicit alignment notes rather than silent formal substitutions.

### E.14:End

