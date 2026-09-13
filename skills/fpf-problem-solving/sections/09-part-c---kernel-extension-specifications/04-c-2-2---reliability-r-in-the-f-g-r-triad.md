## C.2.2 - Reliability R in the F–G–R triad

> Reliability (R) concerns the warrant for one typed claim under an explicit claim scope (G). Keep the support useful and its limitations visible. A numerical R needs a receiving model for its meaning, scale, inputs, and dependencies; no universal fold is supplied. On reuse, name the actual relation and apply only its warranted loss to **R**, not to F or G.

> **Type:** Architectural (A)
> **Status:** Stable

### C.2.2:1 - Problem frame

KD‑CAL asks a simple operational question: *“Where can I safely use this claim?”*
FPF answers with a minimal “epistemic location” built from three coordinates. Any relations traversed by a justification path are named separately:

* **F** (Formality) describes *how the claim is expressed* and how strongly it supports verification workflows (C.2.3).
* **G** (Claim scope) describes *where the claim is asserted to apply* as a set-like object (A.2.6).
* **R** (Reliability) describes *how strongly the claim is warranted* by linked evidence under that scope.
* **CL / CL^k / CL^plane** (Congruence Levels) describe fit or loss for the relation families that define them—for example, a semantic relation, kind relation, or reference-plane relation (B.3, C.3, F.9).
  A CL value belongs to the declared relation or traversal used by the path, not to the claim as a fourth coordinate. Shared wording about a "context" creates no relation and no loss value.
In practice, the triad is frequently used before it is made explicit:

* Authors implicitly “average” disparate evidence and report a single confidence.
* Teams treat higher formality (F) as if it automatically implies higher warrant (R).
* Scope growth is smuggled in through phrasing instead of explicit scope operators (A.2.6).
* A claim or its evidence is reused after a change of scope, kind, plane, notation, source-local meaning, model-use basis, or evidence basis without naming the actual relation and routing its declared loss into R.

This pattern makes **R** explicit in KD‑CAL and fixes the **triad discipline** required by Kind‑CAL (C.3) and the Trust & Assurance calculus (B.3).

### C.2.2:2 - Problem

FPF needs a reliability coordinate that is:

1. **Auditable.** A reader can trace the supported conclusion to its formal or empirical basis and see the effect of actual reuse limitations.
2. **Composable.** Support can be combined under its warranted meanings and dependencies without illegal scale arithmetic; where no aggregate is justified, the separate contributions remain usable.
3. **Orthogonal.** R is not conflated with F (expression) or G (scope).
4. **Relation-aware.** Any loss declared by an actual scope-translation, kind, plane, notation, source-local, model-use, or evidence-reuse relation is explicit and affects **R only**.
5. **Minimal.** The solution does not introduce new core types or new face-kinds.

### C.2.2:3 - Forces

| Force                                         | Tension                                                                                                            |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Single number vs multi-tradition evidence** | People want one scalar ↔ evidence comes from heterogeneous practices (proofs, tests, telemetry, expert review).    |
| **Rigor vs humility**                         | Claims need to be usable in decisions ↔ overconfident scores are dangerous and hard to unwind.                     |
| **Formal vs empirical warrant**               | Proof can be decisive in a formal theory ↔ real-world deployment requires empirical adequacy and drift management. |
| **Scope realism vs marketing scope** | Restricting a claim can remove an unsupported scope extension ↔ a smaller scope alone creates no new evidence or automatic R increase. |
| **Reuse vs relation-specific loss**           | Reuse is valuable ↔ a changed scope, kind, plane, notation, local meaning, model-use basis, or evidence basis can introduce a different and separately governed loss. |
| **Toolability vs expressive freedom**         | A validator needs crisp rules ↔ authors want flexible narratives and domain nuance.                                |

### C.2.2:4 - Solution

#### C.2.2:4.1 - Canonical triad relation

**Definition DEF‑C2.2‑1 (Epistemic location).**
An epistemic location for a claim `c` is the tuple:

`Loc(c) = ⟨F(c), G(c), R_eff(c)⟩`

where:

* `F(c)` is Formality (C.2.3), treated as an **ordinal**.
* `G(c)` is Claim scope (A.2.6), treated as a **set-like scope object**.
* `R_eff(c)` names the effective warrant for this claim and use. Its meaning and scale come from the B.3 receiving model, not from the letter R. A probability-like or ratio-scale value in `[0,1]` needs that model; an ordinal proxy keeps its declared ordinal meaning.
  If no common quantitative model is justified, report R as unquantified with the separate support and bounded conclusion, rather than substitute zero or invent a score. When a guard consumes a path-specific value, identify the actual PathId and its model (§4.8.A / G.6); a declared policy name alone does not warrant collapsing paths into one scalar.

A location always concerns one exact claim. `G` carries its `U.ClaimScope`; any stance, reference plane, effective scheme, model-use basis, working situation, evidence basis, or validity window is stated separately when it changes interpretation or use:
* No generic `K` or Context value is part of epistemic-location identity; the exact subject-specific values above remain independently governed.
* `S ∈ {design, run}` is the claim’s stance value; keep design-time and run-time assurance separate.
* `ReferencePlane` is declared where applicable; plane crossings apply `CL^plane` and penalize **R only**.
* When the claim is published on the Working‑Model surface, the author also declares `validationMode ∈ {postulate, inferential, axiomatic}` (E.14 / B.3).

**Mode-to-lane hint (informative).** `validationMode` sets the *default expectation* for which assurance lane carries the initial support load (B.3.3 or B.3.5).
It does **not** add a new characteristic and does **not** change the meaning of `R`:
* `axiomatic` → VA-dominant (constructive grounding or proof carriers); if `ReferencePlane=world`, LA may still be required.
* `inferential` → VA+TA-dominant (reasoned chain + typing/alignment assurance); LA is optional and scope-bound.
* `postulate` → LA-dominant (empirical validation with freshness/decay); VA is optional.
In all modes, **R remains warrant**, not ontological truth; “proof ⇒ R=1 in the world” is a category error.

**Formal-input rule.** Empirical R may be N/A for a strictly axiomatic claim. Preserve the proof and its conclusion under the stated axioms; **do not set `R_proxy := F` for an R fold**. The tag `line=formal`, a postulative mode, or rescaling F into [0,1] supplies no conversion model. A declared F-derived ordinal proxy is valid only for its own ordinal meaning. Any F-derived value used as another quantity needs a receiving model establishing its meaning, scale, conversion, assumptions, and warranted application; in particular, checkability alone does not establish a probability about a real system.

`⟨F,G,R⟩` is an **assurance tuple**, not a `U.CharacteristicSpace`; do not draw “trajectories” in `⟨F,G,R⟩`.

#### C.2.2:4.2 - What Reliability R means in KD‑CAL

**Definition DEF‑C2.2‑2 (Reliability as warrant).**
`R` is a conservative, evidence-bound indicator of how strongly the claim "holds as stated" under its declared `U.ClaimScope` and the separately named evidence and use conditions. It is interpreted as *warrant strength*, not as truth.

**Prophylactic clarification.**

* A higher `R` means stronger warrant only within the same declared quantity, scale, claim, and receiving model. A number from another model is not automatically comparable.
* A higher `F` means “the claim’s form is amenable to higher-formality checking and wider reuse,” but does not itself imply the claim is warranted.
* A larger `G` means “the claim applies to more cases,” but does not itself imply the claim is warranted in those cases.

#### C.2.2:4.3 - Dependence-sensitive support composition

**Definition DEF‑C2.2‑3 (Support composition).**
For claim `c`, identify the support actually needed by its receiving use. Distinguish indispensable premises, alternative sufficient arguments, complementary evidence for the same question, support for different scope slices, and counterevidence. A source's presence in the graph does not make it an indispensable premise. B.1.3 supplies the synthesis Method and its guidance and controller examples.

Let `SpineClaims(P)` name premises and lemmas actually required by argument `P`; `SpineRelations(P)` names the actual scope, kind, plane, notation, source-local, model-use, and evidence-reuse relations it traverses. Satellite citations are not required premises. Retain each contribution's source, assumptions, scope, and limitations, including shared datasets, duplicated evidence, and common bias.

**Choose the operation from the model.** B.3 requires the target quantity, compatible scales, dependency assumptions, and warranted operation before an aggregate is calculated. An indispensable weak premise can limit an inference, but `min` is not a universal probability or warrant fold. Two necessary independent conditions with probabilities 0.9 each give 0.81 for their conjunction; minimum 0.9 overstates it. Without independence, use the warranted conditional model or leave the joint probability unresolved. Monotonicity and boundedness of a proposed rule are insufficient.

**Alternative and complementary support.** An actually sufficient argument may be usable without the others. A maximum can select the best attested argument value under a model whose result has that meaning; it does not measure combined corroboration. Complementary evidence may strengthen or qualify a conclusion by addressing different rival explanations or limitations, even when neither source is sufficient alone. Count neither publications nor method names as independent confirmation. A shared bias may leave apparent agreement uninformative. There is no universal “never exceed the best source” cap and no entangled-source fallback to minimum.

**Scope and conflict.** Retain different `G_path` slices under A.2.6; do not use maximum to hide unsupported regions. For overlapping-scope `p` and `¬p`, preserve credible contrary evidence. Separate claims only by distinctions established by the sources; otherwise narrow, qualify, or withhold the affected conclusion. An uninformative study, a lack of decisive support, and evidence against the claim are not interchangeable.

**Useful non-aggregate result.** If there is no warranted common model, retain separate support and limitations and give a bounded reasoned synthesis. This may finish the receiving question without a score, penalty table, extra study, or a record merely certifying their omission. The feasibility and worth of further inquiry are separate C.11/C.19.2 questions; their cost does not alter what the current evidence supports.

#### C.2.2:4.4 - Relation-specific congruence penalties route to R only

A reused claim may traverse more than one independently governed relation. Before calculating `R_eff`, state what actually changed and use the rule for that change. A.2.6 owns claim-scope operations; C.3/C.3.3 owns kind relations; F.9 owns a semantic Bridge between exact local-sense cells; notation, reference-plane, model-use, and evidence-reuse relations keep their own definitions. None is a universal crossing relation.

**Invariant INV-C2.2-1 (R-only penalty routing).** For each traversed relation `r` whose rule declares a congruence loss:

`F_out = F_in`
`G_out = translate(r, G_in)` only when `r` is an applicable A.2.6 scope translation; otherwise `G_out = G_in`
`R_out ≤ R_in` on the named ordered warrant scale for a loss-only transformation, with any numerical penalty justified by that relation's receiving model

A scope translation may narrow or re-express `G`; it never widens the claim silently. A change in formality is a new episteme or explicit ΔF move, not a transport penalty. A semantic Bridge changes neither kind nor scope by itself. A kind or plane relation supplies no semantic correspondence unless that separate relation also obtains. Evidence reuse changes warrant only through its own evidence-use or reliance claim.

There is no implicit crossing. If a reuse depends on a changed value and its required relation or operation is absent, unresolved, or outside its applicability, the reuse is non-conformant. This keeps guard macros simple: each path records the relations it actually traverses and routes their declared losses to `R`, while every other coordinate changes only under its own rule.

#### C.2.2:4.4.A - Worked micro-example: scope revision and evidence reuse

A materials-lab claim says:

> `c_lab:` "Adhesive X retains ≥85% tensile strength on Al6061 for 2 h at 120–150 °C."

Its declared scope is `G_lab := {substrate=Al6061, temp∈[120,150]°C, dwell≤2h, evidenceWindow=1y, rig=Calib-v3}`. A plant engineer proposes a narrower claim for Plant B. Two different moves are required.

1. **State the plant claim and its scope.** Here `temp` in `G_lab` is actual adhesive temperature. For this illustration, assume the plant calibration rule supplies a worst-case error bound `|T_actual − T_reported| ≤ 2 °C` throughout the declared use (C.16). Under A.2.6 the engineer retains `G_lab` and adds the condition `T_reported∈[122,148]°C`: under that bound, actual temperature is within `[120,150]°C`. This changes `G`; it is not an F.9 semantic Bridge and is not inferred from the words "lab" and "plant".
2. **Judge reuse of the lab evidence.** The exact A.10 or B.3 evidence-use and reliance claim names the lab evidence, plant claim, calibration edition, validity window, and intended use. A declared fit `CL=2` records the relation's fit, not a probability decrement. State the actual reuse limitation. Calculate a numerical `R_eff` only if a receiving model establishes the R quantity and this loss; otherwise keep the separate support and qualified plant conclusion. This judgement does not perform the scope edit.

If lab and plant use distinct local meanings for a material term, F.9 separately tests a Bridge between their exact F.17 cells. Its semantic loss is not the calibration correction or the evidence-reuse result. A further safety narrowing of that reported-temperature interval to `[125,145]°C` is another explicit A.2.6 ΔG− decision.

The example therefore preserves one simple rule: name each changed value and relation once, change `G` only through the scope rule, and reduce `R` only through the loss rule that actually applies.

#### C.2.2:4.5 - Effective reliability under reuse: a justified loss model

**Definition DEF‑C2.2‑4 (Effective reliability under reuse).**
A relied-on relation may introduce loss in the support for the receiving claim. Name that relation and its scope, semantic, notation, model-use, evidence-reuse, kind, or reference-plane rule. The corresponding `CL`, `CL^k`, or `CL^plane` is an ordinal summary belonging to that relation family; the ranks are not amounts to subtract from R.

A quantitative loss model names the receiving quantity and scale, input meanings, dependencies, loss interpretation, derivation or calibration, and applicability assumptions under B.3. If the model uses functions `Φ`, `Ψ`, `Φ_plane`, and a combining operation `Π`, cite their actual definitions and versions. A policy identifier, table, monotonicity, boundedness, or clipping to [0,1] does not by itself justify any of them.

For a loss-only interpretation on an ordered scale, worsening fit cannot by itself count as an improvement in warrant. The model must justify any pathwise CL minimum, repeated-loss treatment, or neutral term for an absent relation. Preserve separately justified ordinal chain-congruence operations in C.3.3; they do not provide a numerical R penalty.

**Positive quantitative illustration, not a default.** Suppose a receiving claim requires events A and B. An applicable model and evidence establish `P(A) ≥ 0.82` and `P(¬B) ≤ 0.15` for the same use. The probability bound `P(A ∩ B) ≥ max(0, 0.82 − 0.15) = 0.67` follows without an independence assumption. Here 0.67 is a lower bound, not a point estimate or a generic confidence score. The 0.15 term comes from the stated bound on failure of B, not a CL rank. If those event meanings or bounds are unavailable, the calculation is unavailable.

**Reuse conditions.** Apply a relation's justified admissibility or protection condition to the named use before relying on it; neither this pattern nor a bare CL rung creates a universal waiver obligation. If the condition is unsupported, limit or stop that reliance while retaining any independently supported source conclusion.

#### C.2.2:4.5.A - Formality and scale discipline

* Ordinal F, CL, and ordinal R proxies permit only operations justified for their ordered meanings, not arithmetic pretending they are ratio-scale measurements.
* A numerical R requires a justified receiving model even at high formality. A complete formal proof remains useful with empirical R marked N/A; a missing empirical score does not demote the theorem.
* When support has no common numerical model, publish its separate contributions, limitations, and the bounded conclusion. Use validity windows, empirical reproducibility information, and B.3.4 decay only where the claim actually consumes them.

#### C.2.2:4.6 - Evidence lanes are not new characteristics

KD‑CAL does not add new global coordinates beyond F–G–R. Instead, it requires that reliability be *explainable* via **assurance lanes** (B.3.3):

* **TA** (Typing assurance): semantic/type alignment sufficient for transport and composition.
* **VA** (Verification assurance): logical/algorithmic checking, proof, model checking, static guarantees.
* **LA** (Validation assurance): empirical adequacy under declared conditions, tests, benchmarks, telemetry.

Lane reporting is how KD-CAL supports the common research distinction between logical soundness and empirical adequacy **without introducing new global characteristics**.
Lanes remain **separable** in SCR/Notes; they are not averaged into a “single tradition score”.

#### C.2.2:4.7 - Scope operations are kind-safe (and use the ClaimScope algebra)

Reliability is meaningless if scope operations are applied to ill-typed entities.

**Well-formedness constraint WFC‑C2.2‑1 (Type before scope).**
Let `G1` and `G2` be claim scopes for claims about entities of kinds `K1` and `K2`. A scope operation that combines them—such as `G1 ∩ G2` for serial intersection or `SpanUnion({G_i})` for parallel coverage—is defined only if:

* `K1 = K2`; or
* an exact C.3/C.3.3 kind relation or cast makes the operation well typed for these participants and this direction.

An A.2.6 scope translation changes `G` only under its own rule. A kind relation does not translate scope. If distinct source-local meanings also matter, an actual F.9 Bridge and its bounded-use claim are separate; neither repairs an ill-typed scope operation.
This constraint prevents “type-by-scope” anti-patterns where scope manipulation is used to hide type mismatch.

#### C.2.2:4.8 - Minimal authoring recipe

A minimal, conforming KD‑CAL authoring flow for reliability is:

1. **Fix the typed claim.** State the claim as a typed proposition about an EntityOfConcern (Kind‑CAL, C.3).
2. **Declare claim scope.** Write `G` explicitly using A.2.6 operators; avoid scope-by-wording.
3. **Declare interpretation conditions.** State design or run stance, `ReferencePlane`, effective scheme, model-use basis, working situation, and `validationMode ∈ {postulate, inferential, axiomatic}` only where each changes this claim or its use. `G` already carries claim scope; do not add a generic Context identifier.
4. **Bind evidence.** Attach evidence stubs and lane tags (TA/VA/LA) and validity windows / decay policy where applicable (B.3.3, B.3.4).
5. **Identify support roles and dependence.** Distinguish required premises, sufficient alternatives, complementary support, scope slices, and counterevidence. Identify duplicated data, shared assumptions, and plausible common biases.
6. **Choose a justified calculation or a non-aggregate synthesis.** Name the receiving quantity, compatible scales, assumptions, and model before any numerical fold. Otherwise retain separate support and a reasoned bounded conclusion; do not substitute a universal min or max.
7. **Name actual relations on reuse.** Use A.2.6 for an applicable scope translation, C.3/C.3.3 for a kind relation, F.9 for a semantic relation between exact local-sense cells, and the direct pattern for notation, plane, model-use, or evidence reuse. Record the fit or loss declared by each traversed relation. If a required relation is absent or unresolved, stop that reuse; a generic cross-context Bridge cannot substitute for it.
8. **Return the usable result.** State F, G, and the supported conclusion with its warrant and limitations. Publish R numerically only under the justified receiving model, with the actual calculation and relied-on loss definitions. A formal conclusion does not require an empirical score. Inquiry or action choice, if needed, remains separate.


#### C.2.2:4.8.A - Authoring template: claim-local support summary

When publishing a path-specific R for a guard or decision, include enough of the support summary to identify its actual quantity, model, inputs, and use. G.6 PathId references can carry this information; no new Core type or mandatory table is introduced.

| PathId | Receiving claim and support | Quantity and model | R result | Fit and limitations | Lane tags | Validity |
| --- | --- | --- | --- | --- | --- | --- |
| P-1 | A ∩ B; the two bounds in §4.5 | Probability lower bound; union-bound argument for the stated events | ≥0.67, not a point estimate | No numerical penalty follows from a CL rank; both input bounds must apply to this same use | Applicable TA/VA/LA references | Intersection of the actual input-bound validity conditions |

Retain actual CL summaries where their relation uses them; any chain minimum needs that relation's ordinal meaning. Empirical time limits and the fixed theory version of a proof remain different conditions. If several paths are consumed, retain their distinct scopes and models and cite the actual PathId(s). A non-aggregate synthesis may instead give its separate contributions and limitations in ordinary prose.

### C.2.2:5 - Archetypal Grounding

Informative; non-binding.

#### C.2.2:5.1 - System illustration

**System.** A brake controller `S` has a claim:

> `c1:` “For road friction μ ∈ [0.2, 0.9] and vehicle mass m ∈ [900, 2200] kg, wheel slip stays in [0.05, 0.25] under ABS control.”

* `F(c1)=F5` because the controller and constraints are expressed as a machine-checkable model plus executable test harness (C.2.3).
* `G(c1)` has the stated μ/m bounds, but this illustration leaves the speed domain and admissible tire set unspecified. Under A.2.6, those domains and any coupled restrictions are needed to decide membership of a slice satisfying the stated bounds; that membership remains unresolved here. A product set in `(μ, m, speed, tire)` space is justified only if its scope predicate admits every combination of the selected domains.
* Evidence:

  * VA: model-checking of a simplified plant/controller model (strong, but only for the simplified plant).
  * LA: HIL simulation + track tests under sampled conditions with recorded telemetry windows (freshness required).
  * TA: typed alignment between “μ” in simulations, “μ” in the estimation pipeline, and “μ” inferred from real-world sensors.

If track telemetry is used as evidence for the road claim, establish the exact A.10 or B.3 evidence-use and reliance claim, including the road claim, telemetry edition, operating scope, validity window, and intended use. Apply only the fit or loss declared for that evidence reuse; `G(c1)` changes only through a separate A.2.6 scope revision.

#### C.2.2:5.2 - Episteme illustration

**Episteme.** A paper asserts two claims about an algorithm `A`:

* `c2:` “A terminates for all inputs in domain D.” (axiomatic / proof-carrying)
* `c3:` “A achieves ≥ 0.92 F1 on dataset family F under deployment preprocessing P.” (empirical)

`c2` can achieve high VA with a proof carrier; its LA lane may be N/A, but its TA lane remains relevant because the intended meaning of “domain D” must align with the implementation’s input model.
`c3` requires LA evidence and a freshness or shift policy because dataset and preprocessing drift can change both scope and warrant. For production use, state the exact dataset/preprocessing relation and the A.10 or B.3 evidence-reuse claim, then apply its declared loss to `R_eff`; change `G` separately if the production claim has another scope.

### C.2.2:6 - Bias-Annotation

Informative; non-binding.


* **Onto/Epist bias:** High formality is often mistaken for high warrant (“proof therefore true in the world”). This pattern mitigates by forcing LA/TA visibility and by routing transport loss into R rather than mutating the claim.
* **Prag bias:** Teams may Goodhart R by narrowing scope or selecting easy tests. This pattern mitigates by requiring explicit scope declaration and by making scope changes first-class (A.2.6).
* **Gov bias:** Overconfident reuse after a changed scope, scheme, model use, evidence basis, kind, or plane is a recurring failure. This pattern requires the actual relation and its declared loss instead of one generic crossing label.
* **Did bias:** A single scalar is seductive; it hides what kind of warrant exists. Lane reporting keeps the scalar honest.

### C.2.2:7 - Conformance Checklist

Normative.

| ID                                            | Requirement                                                                                                                                                                                                                 | Purpose                                                                       |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **CC‑C.2.2‑1 (Triad publication).** | Authors of a KD-CAL location SHALL attach formal basis, G, and warrant to one exact claim. A numerical R requires the receiving model; otherwise identify unquantified support and the bounded conclusion. | Keeps warrant attached to its claim without inventing a score. |
| **CC‑C.2.2‑2 (R-only penalty routing).**      | A conforming implementation of KD‑CAL reuse **SHALL** satisfy **INV‑C2.2‑1**.                                                                                                                                                | Ensures declared relation losses reduce warrant without silently mutating expression or scope. |
| **CC‑C.2.2‑3 (Support composition).** | A conforming composition SHALL satisfy DEF‑C2.2‑3: identify support roles, compatible scales, and dependencies, and use the justified receiving model or a non-aggregate synthesis. There is no default min or max. | Prevents both overstated assurance and loss of useful complementary support. |
| **CC‑C.2.2‑4 (Relation visibility for reuse).** | Authors **SHALL** name every scope-translation, kind, plane, notation, source-local, model-use, or evidence-reuse relation traversed by the path and cite the fit or loss rule that affects `R_eff`.                                      | Makes each actual reuse loss auditable without inventing one crossing kind.   |
| **CC‑C.2.2‑5 (Loss model visibility).** | Any numerical reuse loss SHALL identify its receiving quantity, scale, assumptions, derivation or calibration, and actual functions and versions, including Π where used. | Makes the calculation reproducible and its meaning inspectable. |
| **CC‑C.2.2‑6 (Type before scope).**           | Authors and validators **SHALL** enforce **WFC‑C2.2‑1** for scope composition operations.                                                                                                                                   | Prevents ill-typed scope algebra from creating incoherent reliability claims. |
| **CC‑C.2.2‑7 (Evidence binding).**            | Authors **SHALL** bind any asserted `R_eff` to evidence references that enable TA/VA/LA inspection, consistent with the assurance lane discipline (B.3.3) and evidence decay discipline (B.3.4).                            | Keeps R grounded and updateable.                                              |
| **CC‑C.2.2‑8 (No ordinal arithmetic).** | Validators SHALL reject arithmetic that treats ordinal F, CL, or an ordinal R proxy as ratio-scale values. A receiving conversion model must establish meaning, scale, conversion, and assumptions; a penalty table or rescaling alone is insufficient. Formal validity never supplies empirical reliability by itself. | Preserves scale legality and useful formal conclusions. |
| **CC‑C.2.2‑9 (Interpretation conditions declared).** | Authors **SHALL** distinguish design- and run-time assurance and declare `ReferencePlane`, effective scheme, model-use basis, working situation, and `validationMode` where each changes the claim or use.                               | Makes interpretation auditable without a generic Context identity field.     |
| **CC‑C.2.2‑10 (Dependence and scope).** | Authors SHALL expose actual shared premises, data, assumptions, and biases. Any assumed independence must be justified for the model and use; different path labels do not suffice. Keep distinct scope slices and counterevidence visible; do not fall back to minimum for entangled support. | Prevents double-counting without erasing complementary evidence. |

### C.2.2:8 - Common Anti-Patterns and How to Avoid Them

Informative; non-binding.

| Anti-pattern               | Symptom                                                                                       | Why it fails                                                     | How to avoid / repair                                                                                    |
| -------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Unsupported assurance fold** | A mean, minimum, maximum, or weighted sum is reported as confidence without its model | Boundedness and monotonicity do not warrant the input scale or dependency interpretation | Identify support roles and a justified receiving model; otherwise return separate support and a bounded synthesis. |
| **Truth-by-score**         | `R=0.9` is treated as “the claim is true.”                                                    | R is warrant strength, not ontological truth.                    | Require explicit evidence links and scope; treat R as decision warrant only.                             |
| **Scope laundering**       | The claim’s applicability grows by wording changes while `G` is unchanged.                    | It silently widens scope, making comparisons meaningless.        | Use A.2.6 operators and treat scope changes as explicit revisions.                                       |
| **Relation laundering**    | A claim or its evidence is reused after a changed scope, kind, plane, notation, local meaning, model use, or evidence basis, while `R` is carried over unchanged. | It hides the actual change and its relation-specific loss. | Name the direct relation or scope operation and recompute `R_eff` from its declared loss; stop if that relation is missing. |
| **DesignRunTag chimera**     | Design-time proofs and run-time telemetry are mixed as if they were the same evidence object. | Evidence belongs to different stances and decays differently.    | Separate lanes and validity windows; treat crossings explicitly.                                         |
| **Ordinal arithmetic** | F or CL ranks become a probability or loss merely by tagging, tabulating, or rescaling them | Ordered categories are not calibrated ratio quantities | Retain the ordinal meaning; any receiving conversion needs its actual model, meaning, scale, and assumptions. |
| **Counting support labels** | More reports are treated as independent confirmation, or one weak additional study automatically defeats the whole | Duplicates, shared bias, complementary information, and counterevidence contribute differently | Recover their actual dependencies and effects on the claim; use neither study count nor a universal min/max fallback. |

### C.2.2:9 - Consequences

Informative; non-binding.

| Benefits                                                                                                     | Trade-offs and mitigations                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Conditional comparability.** Claims can be compared when their R meanings and models are compatible and F and G are explicit. | **No forced score.** Some useful syntheses retain heterogeneous support rather than invent numerical comparability. |
| **Auditability.** Relation-specific reuse loss is visible and localised to R.                                | **Overhead.** Declaring the relations actually traversed and the evidence links is work; mitigate with templates and reuse of standard lane schemas. |
| **Revisable warrant.** New support or counterevidence can change the bounded conclusion under its actual model. | **Scalar temptation.** Keep distinct support contributions and their limitations visible behind any numerical result. |

### C.2.2:10 - Rationale

A triad only works if each coordinate has a single job.

* **G states applicability.** It states where the claim is asserted to apply. If G is implicit, teams argue about “what was meant” instead of updating scope.
* **F carries checkability.** It states how much the claim’s form supports mechanised scrutiny and reuse. If F is conflated with R, formalisation becomes a rhetorical weapon.
* **R carries warrant.** It describes support for this exact claim and use under a named meaning and scale. Its inputs must not erase the distinction between a necessary premise, complementary evidence, and a credible contrary result.

Routing a traversed relation's declared congruence loss into **R only** prevents a subtle failure: a change of scope, kind, plane, notation, source-local meaning, model-use basis, or evidence basis cannot silently rewrite the claim or carry its old warrant forward.

No universal fold is conservative for every support model. Minimum can overstate a conjunctive probability and can also suppress useful complementary evidence. The small common rule is to establish input meanings and dependencies, calculate only what they warrant, and otherwise preserve a useful bounded synthesis.

### C.2.2:11 - SoTA-Echoing

Normative.

**SoTA pack binding note.** If a G.2 SoTA Synthesis Pack has sources that bear on reliability under the exact changed claim scope, kind, reference plane, notation, source-local meaning, model use, or evidence basis in this case, cite the relevant ClaimSheet IDs and CorpusLedger entries. Cite a `BridgeMatrix` row only when the current path actually uses an F.9 cross-local semantic Bridge represented by that row. Otherwise record `SoTA-Pack: TBD/none` and treat this section as the seed; neither a generic Context nor a generic transport package is required.

| Practice claim                                                                                                      | Post‑2015 source anchor                                                                   | Alignment to this pattern                                                                                                                                                           | Adoption status                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Verification and validation should be distinguished and tied to evidence quality, not rhetoric. | ASME V&V 40-2018 (model credibility assessment; historical anchor). | Keep VA and LA separate and attach warrant to evidence, claim, and use. | **Adapt** this distinction; this source is not a justification for a universal KD-CAL minimum. |
| Trustworthiness depends on intended use, affected risks, operating conditions, and explicit limits.              | NIST AI Risk Management Framework 1.0 (2023).                                             | This pattern makes claim limits explicit through `G` and applies CL penalties only through the actual relation used by a reuse path.                                               | **Adapt**, because FPF treats declared relation loss as an epistemic penalty, not only as an organisational risk statement. |
| Safety arguments should make claims, evidence, and assumptions explicit and reviewable. | UL 4600 (2020) and related assurance-case practice in autonomous systems. | This pattern treats `R` as an auditable warrant signal whose inputs are explicit evidence items; any reuse names the exact relation traversed and its declared loss. | **Adopt**, while remaining notation-independent and avoiding tool mandates. |
| Empirical results should be accompanied by structured provenance and usage conditions to enable reuse and critique. | “Datasheets for Datasets” (Gebru et al., 2018) and “Model Cards” (Mitchell et al., 2019). | Scope discipline and lane reporting make empirical warrant reusable only when the exact evidence, claim, use, conditions, and any evidence-reuse or dataset relation are explicit; that relation's declared loss routes to `R_eff` only. | **Adopt**, with relation-specific congruence penalties as the reuse control mechanism. |
| Reproducibility requires packaging evidence and making it re-checkable by others. | ACM Artifact Review and Badging (updated practices post-2015) and The Turing Way (2019). | This pattern treats evidence as inspectable across TA/VA/LA lanes and lets reliability decay when evidence becomes stale or non-replayable. | **Adapt**, because FPF treats freshness and relation-specific reuse losses as first-class calculus inputs. |
| Strong inference needs evidence that discriminates against live rival explanations. | Mayo (2018) on severity in statistical inference (historical anchor). | Keep the limitation or rival explanation that a test actually addresses visible. | **Adapt** the methodological concern, not an asserted derivation of minimum or any universal R formula. |

The current methodological comparison is [Gutierrez, Glymour and Davey Smith, *Evidence triangulation in health research* (2025)](https://link.springer.com/article/10.1007/s10654-024-01194-6): compare target questions, design assumptions and possible shared biases; use qualitative synthesis where quantitative combination is unwarranted. **Adapt** those distinctions for heterogeneous support. The paper supplies neither a universal R scale nor a requirement to commission another study for every useful conclusion.

### C.2.2:12 - Relations
**Builds on:** C.2 (KD-CAL overview), A.2.6 (claim scope and scope revision), C.2.3 (Formality F), B.3 and B.3.3/B.3.4 (assurance, evidence lanes, and refresh), B.1.3 (Γ-fold patterns), C.3.3 (cross-kind use), G.6 (EvidenceGraph PathId discipline), C.29/A.6.3.RT (notation and representation relations), A.1.1 (selected model-use structure), and A.10/B.3 for exact evidence-use and reliance relations. F.9 is used only when an obtaining relation between distinct local meanings, reference schemes, or reference planes is part of the path.
**Coordinates with:** C.16 for measurement claims, E.14 for working-model assertions, F.17 for optional local-meaning addresses, and E.18/E.17/A.21 when their own transfer, publication, or gate objects are current. G.2 supplies relevant source-pack entries; G.7 remains the conditional calibration path for its declared cross-Tradition/F.9 Bridge use, not a universal calibration owner.
**Used by:** C.3.3 for cross-kind reuse discipline, guard macro bundles in C.3.A and C.21, and acceptance or gating logic that consumes `R_eff` while preserving `F` and `G`.
**Clarifies:** the KD-CAL meaning of reliability implicit in C.2:4.1 and the relation-specific reuse claims referenced across B.3 and C.3; it does not create a universal transport relation.

### C.2.2:End
