## C.2 - Epistemic holon composition (KD-CAL)

**Scope & exports.** A substrate-neutral calculus for composing **epistemic holons** (`U.Episteme`) and reasoning about their change and equivalence. Exports: (i) three **point-characteristics**—**Formality F**, **ClaimScope G**, **Reliability R**—that locate one exact claim-bearing episteme for a stated use; (ii) a **pairwise ladder** of **Congruence Levels (CL 0…3)**; (iii) four **Δ-moves** (*Formalise, Generalise/Specialise, Calibrate/Validate, Congrue*); (iv) **composition rules** (Γ_epist) for aggregates; and (v) propagation laws for CL through mappings and notation relations. C.2.1 identifies an episteme by its exact claim content, exact EntityOfConcern, and effective `U.ReferenceScheme` under `EpistemeConstitutionRelation`. Empirical grounding and edition are separate C.2.1 relations. Viewpoint selection and `U.View` conformance use E.17.0; mathematical or diagrammatic representation uses C.29 and A.6.3.RT; publication uses E.17/E.24.PUB; a carrier remains a distinct entity. Every F–G–R computation names the exact claim and its `U.ClaimScope`. If a path changes scope, notation, kind, reference plane, source-local meaning, model-use basis, or evidence basis, it names the actual relation traversed and applies only the loss that relation declares; no generic Context, slot umbrella, or Bridge stands in for those different relations.

**Formality F** is the rigor characteristic defined **normatively in C.2.3**. All KD‑CAL computations and guards **SHALL** use `U.Formality` (F0…F9) as specified there; **no parallel “mode” ladders** are allowed.

### C.2:1 - Problem Frame

FPF fixes two archetypal sub-holons: **`U.System`** (physical/operational) and **`U.Episteme`** (knowledge holon). KD-CAL is the primary composition pattern for `U.Episteme`, giving engineers a compact, testable way to say (a) how strictly an episteme is written (**F**), (b) where its exact claim is asserted to apply (**G**), (c) how well that claim is warranted by evidence or severe tests (**R**), and (d) how closely **two** epistemes coincide (**CL**). C.2.1 supplies the constitution test: exact claim content, one exact EntityOfConcern, and one effective `U.ReferenceScheme`. Grounding, edition, viewpoint, view, representation, publication, form, and carrier remain neighboring objects or relations under their direct patterns.

### C.2:2 - Problem

Teams routinely entangle **programs, specifications, proofs, and datasets**; a proof is treated as evidence that an actual system meets its assumptions, or a program as if it entailed a theorem. Warrant becomes opaque when support and its applicable currentness conditions are not explicit. Epistemes are anthropomorphised as actors (“the standard enforces…”), producing category errors at execution. Aggregation can hide a missing necessary premise, erase complementary support, or conceal contrary evidence behind an unjustified score. KD-CAL keeps constitution, input meanings, scales, and support dependencies explicit.

### C.2:3 - Forces

* **Universality vs domain idioms.** One calculus must cover physics theories, legal codes, safety specs, algorithms, and formal proofs without flattening their differences.
* **Meaning vs materiality.** Meaning must be independent of carrier, yet accountable to it historically.
* **Deductive vs empirical.** Axiomatic certainty and empirical trust have different evidence-continuity profiles; both must compose.
* **Abstraction vs enactment.** Epistemes constrain action; **systems** act. The calculus must keep the roles distinct.

### C.2:4 - Solution

#### C.2:4.1 - Coordinates, constitution, and neighboring relations

**KD‑CAL characteristics (single‑episteme, point‑values).**

* **Formality F.** From free prose to **machine‑checkable proof/specification**. Litmus: *would a machine reject it if wrong?*
* **Claim scope (G), a set‑valued applicability over `U.ContextSlice`, with ∩/SpanUnion/translate algebra; CL penalties apply to R, not to F/G.** Litmus: *how wide is the declared scope, and under what minimal assumptions does the claim hold?*
* **Reliability R.** Warrant for this exact claim and receiving use. Litmus: *what supports this conclusion, under which assumptions, and what limits it?* **R-claims MUST bind to their actual formal or empirical support.** A numerical R requires the B.3/C.2.2 meaning, scale, and model; otherwise retain separate support and a bounded reasoned conclusion. A proof under axioms needs no empirical score, and F cannot be substituted for R. Relevance windows and B.3.4 currentness rules apply where the relied-on support consumes them.

 **Congruence Level (CL), pairwise ladder.**
 `CL‑0` **Opposed/Disjoint** (contrastive; no substitution); `CL‑1` **Comparable / Naming‑only** (label similarity; no substitution); `CL‑2` **Translatable** (structure‑preserving correspondence in a declared fragment with **stated loss**); `CL‑3` **Near‑identity** (the declared invariants match). *CL is a characteristic of a relation between two epistemes; it is not a fourth member of the F–G–R assurance tuple and it is not a characteristic space of its own.* **KD-CAL substitution constraint:** plane preservation and **CL ≥ 2** are necessary for a substitution under this calculus; substituting **type‑structure** additionally requires **CL = 3**. These conditions do not establish suitability for the proposed use. State the exact substitution, direction, correspondence rule, and tolerated loss under the direct receiving pattern, and establish reliance separately. When local meanings cross semantic contexts, first test the F.9 Bridge predicate on exact F.17 cells; keep the obtaining Bridge, bounded-use claim, and reliance result distinct. A CL value establishes no local system-role-kind membership or assignment.

**Constitution and neighboring relations.** State F, G, and R for one exact claim of one C.2.1 episteme. Its exact claim content, EntityOfConcern, and effective `U.ReferenceScheme` identify the episteme through `EpistemeConstitutionRelation`. F characterizes the claim's form; G is the separate `U.ClaimScope`; R relies on exact evaluation, evidence-use, and assurance relations. Empirical grounding and edition remain separate C.2.1 relations. Viewpoint selection and view conformance remain under E.17.0; notation and other representation structure remain under C.29/A.6.3.RT; publication occurrence, form, and carrier remain under E.17/E.24.PUB. Multiple notations are allowed only when their exact representation or notation relation is explicit and any declared loss is applied to R rather than hidden in an omnibus episteme field.

#### C.2:4.2 - Four Δ‑moves (epistemic motion)

* **ΔF — Formalise.** Rewrite for stricter calculi/grammars; raise proof obligations.
* **ΔG — Generalise / Specialise.** Widen or narrow the **claim scope** (assumptions & scope). Changes to decomposition granularity are an **orthogonal view** and do not change **G** unless they alter the envelope.
* **ΔR — Calibrate / Validate.** Revise warrant through support that actually bears on the claim: proof or reasoning, calibration, severe tests, or monitoring as applicable. State what the contribution changes. A formalization alone is ΔF, not an R increase; choosing new inquiry is a separate decision.
* **ΔCL — Congrue.** Establish and record the sameness relation between **two** epistemes (ladder 0→3).
  Moves compose into **paths**. A CL chain minimum retains only the ordered congruence meaning justified by the relation family; it is not a numerical reliability loss.

#### C.2:4.3 - Composition (Γ_epist) and propagation

Let **Γ_epist** compose exact epistemes `{Eᵢ}` for one declared claim and use. B.1.3 supplies the synthesis/compilation Method; B.3 and C.2.2 govern warrant and scale discipline.

* **R (Reliability).** First distinguish indispensable premises, alternative sufficient arguments, complementary evidence, different scope slices, and counterevidence. Identify duplicated data and shared assumptions or bias. A numerical fold requires warranted input meanings, compatible scales, dependencies, and a receiving model. Neither series nor parallel syntax supplies a default minimum or maximum, and there is no universal cap at the best support line. Where no common model is justified, retain separate contributions and limitations in a bounded reasoned synthesis.
* **F (Formality).** `F(Γ) = minᵢ F(Eᵢ)` over the essential formal constituents of the claim. This is an ordinal formality statement, not an R calculation. Raise F by the actual ΔF move; neither an axiomatic mode nor a `line=formal` tag converts F into empirical warrant.
* **G (ClaimScope).** Required premises compose only on their overlapping scope. Distinct supported slices may form `SpanUnion({G_path})` under A.2.6 and C.2.2's type-before-scope rule; retain their support separately and drop unsupported regions. A new source does not by itself generalise the claim. Scope change remains an explicit ΔG± move.
* **CL (Congruence).** Keep each traversed mapping and the ordered meaning of its declared CL visible. A chain minimum is usable where that relation's congruence rule justifies it. A notation, scope-translation, kind, plane, source-local, model-use, or evidence-reuse relation contributes only its own warranted loss. A numerical Φ needs its receiving model; a monotone table or clipped output does not supply one.

For example, two necessary independent conditions with probabilities 0.9 each have conjunction probability 0.81, not minimum 0.9. Conversely, a limited complementary source need not reduce the support already available. A credible contrary result changes the affected conclusion. A theorem A ⇒ P remains valid as a formal result while evidence violating A can defeat its use as assurance of an actual system.

Γ remains defined on holons and respects the core's identity and boundary discipline. Its support account establishes neither a new action permission nor the worth of acquiring further evidence.

#### C.2:4.4 - What **must not** be conflated (normative guards)

* **Representation structure ≠ carrier.** Files, PDFs, or repositories are **carriers** outside the episteme; they never count as parts of `U.Episteme` (**see C.2.1 EP‑1; CC‑EPI‑2/3**).
* **Epistemes do not act.** Only **systems** perform Work. Epistemes carry claim content and can participate in constitution, grounding, edition, description, evidence-use, reliance, viewing, representation, and publication relations under their direct patterns.
* **CL is not a score.** It is a **qualitative ladder** of preservation classes; do not average it.

### C.2:5 - ✱ Archetypal Grounding (Tell–Show–Show)

**Universal rule (tell).** *Compose knowledge by Γ_epist with explicit support roles, dependence, scope, and justified input scales. Use the receiving model for any R calculation, or return a bounded non-aggregate synthesis. Identify the episteme by exact claim content, EntityOfConcern, and effective reference scheme; keep empirical grounding, edition, viewpoint selection, view conformance, representation, publication form, publication occurrence, and carrier in their own direct relations.*

**System (show, current physical-system lens).** Consider a **battery-pack thermal subsystem** integrating a physics model of heat flow and an operating envelope for fast-charge. As a **system**, it composes pumps, sensors, and controllers through the system, composition, boundary, state, and dynamics guidance in `A.1`, `A.14`, `A.22`, and `A.3.4`, with conservation constraints made explicit; `B.1.6` and `C.16` govern resource and measurement claims as applicable. Planned `C.1` (Sys-CAL) may later consolidate that guidance, but it supplies no current governing semantics. The assurance story depends on epistemes about the model and envelope; the system **acts**, epistemes constrain. (Archetypes and boundary discipline per core.)

**Episteme (show, KD-CAL lens).** Consider a **CMIP-class climate projection episteme** (post-2015 generation): its exact claim content covers PDEs and parameterisations; its EntityOfConcern identifies what the projection claims concern; and its effective reference scheme supplies the interpretation rules. A separate `U.ClaimScope` names historical forcings, resolution, and assumptions. Any empirical-grounding occurrence names the grounding holon and covered claim subgraph separately. Its representation may include domain equations and a tabular schema linked by an explicit notation or representation relation with stated loss. When composing radiation, cloud, and ocean-mixing contributions, identify which assumptions the particular projection requires and what each hindcast actually tests. Shared models or data do not establish independent confirmation. An aggregate R needs the domain quantity and dependency model; otherwise retain the separate tests, assumptions, scope limits, and any disagreements. F remains an ordinal account of the essential formal constituents.

### C.2:6 - Bias‑Annotation

* **Metric worship.** Treating `[F,G,R]` as ends rather than means; mitigation: require **evidence bindings** and narrative of limits in the claim scope and grounding envelope.
* **Category slip.** Equating a notation, view, publication form, or carrier with claim content, EntityOfConcern, effective reference scheme, or an empirical-grounding participant; mitigation: apply C.2.1 constitution and then the direct neighboring relation pattern.
* **Analogy inflation.** Presenting CL‑0/1 as identity; mitigation: always name the **CL rung** for cross‑mappings.

### C.2:7 - Conformance Checklist

1. **C2-1 (Episteme constitution and neighbors).** Every `U.Episteme` **MUST** satisfy C.2.1 constitution through exact claim content, one exact EntityOfConcern, and one effective `U.ReferenceScheme`. Empirical grounding and edition are stated through their separate C.2.1 relations. Viewpoint selection and `U.View` conformance use E.17.0; representation uses C.29/A.6.3.RT; publication occurrence, form, and carrier use E.17/E.24.PUB. None is treated as an episteme slot or identity component merely because a record or notation places it beside the constitution values.
2. **C2‑2 (Coordinates).** Each episteme **SHALL** declare `[F,G,R]` for its exact claim and use with a brief rationale; where R has no justified numerical model, retain its unquantified support and bounded conclusion. Formal validity needs no empirical score; **F** is `U.Formality ∈ {F0…F9}` per **C.2.3**, **exactly one episteme‑level F** computed as the **min over essential parts**. CL is declared for **pairs only**. A named notation scheme **MAY** use sub‑anchors (e.g., `F4[OCL]`, `F7[HOL]`), which **MUST** preserve the global order and **map to their parent anchor** from C.2.3.
3. **C2‑3 (Composition).** Authors **SHALL** identify support roles and dependencies under B.1.3/C.2.2 before combining inputs. Any numerical R or loss **MUST** have justified meanings, scales, assumptions, and a receiving model under B.3; no universal min/max or F-to-R conversion applies. Otherwise return separate support and a bounded synthesis. F uses the minimum over essential formal constituents; G uses applicable path intersections and supported SpanUnion under A.2.6. Every reuse **MUST** name the actual direct relation and retain its warranted limitation; do not hide contrary evidence or unsupported scope.
4. **C2‑4 (NotationBridge).** Multi‑notation representation components **SHOULD** register `NotationBridge` edges with CL and loss note; any cross‑notation reasoning **MUST** cite the bridge’s CL.
5. **C2‑5 (No action).** Epistemes **MUST NOT** be assigned actions; work is executed by systems in role.

### C.2:8 - Consequences

**Benefits.** A compact map for knowledge epistemes; visible support dependencies and limitations; useful formal and qualitative results alongside justified calculations; disciplined reuse across domains with explicit CL; consistent separation of meaning from material carriers.
**Trade-offs.** Authors must identify the support relation and any calculation model; multi-notation work keeps its relation-specific basis. Some useful syntheses have no common scalar. *Mitigation:* the C.2.1 constitution test and direct neighboring patterns keep the ordinary entry brief while preserving recoverable precision.

### C.2:9 - Rationale

KD-CAL turns the coarse legacy semiotic picture into **holonic composition** over exact C.2.1 epistemes and their claims. Exact claim content, EntityOfConcern, and effective reference scheme keep episteme identity stable; formal structure and claim scope (**F,G**), evidence (**R**), and pairwise congruence (**CL**) remain visible and composable without an omnibus slot relation. Direct grounding, edition, view, representation, publication, and carrier patterns prevent category collapse. The resulting characteristics remain **manager-readable** and **formalisation-ready**, with **G** grounded in scope/envelope rather than part count.

### C.2:10 - Relations

* **Depends on:** `C.2.1 U.Episteme: Constitution, Empirical Grounding, and Edition Relations` for episteme identity, the constitution relation, and the separate grounding and edition relations; `E.17.0` for viewpoint selection and `U.View` conformance; `C.29` and `A.6.3.RT` for representation; and `E.17`/`E.24.PUB` for publication occurrence, form, and carrier.
* **Peers:** planned **Sys-CAL** (`C.1`) may later consolidate physical-system guidance; current system composition, boundary, state, conservation, resource, and measurement claims use `A.1`, `A.14`, `A.22`, `A.3.4`, `B.1.6`, and `C.16` as applicable. KD-CAL composes **epistemes** and feeds assurance lenses in Part B.
* **Constrained by authoring:** Architectural patterns must include Tell–Show–Show with **Archetypal Grounding** (this section).

### C.2:11 - Worked mini‑examples (post‑2015 flavours)

* **Formal lift (ΔF).** Recasting a 2019 **variational free‑energy** narrative into a typed calculus raises **F**, clarifies scope, and enables CL‑2 bridges between biological and ML formulations—*without* claiming empirical gain (**R** unchanged).
* **Complementary hindcast evidence.** Two hindcast lines supporting a climate projection may address different errors, reuse data, or cover different conditions. Identify those relations before combining them; a maximum may select one attested argument only under that declared meaning, not measure their combined corroboration. Keep disagreement and unsupported scope visible. This illustration supplies no climate-specific reliability model.
* **Notation bridge (CL drop).** A 2021 **type‑theoretic specification** rendered in a semi‑formal DSL requires a `NotationBridge` with a CL<3 note; any theorem transported across must respect the bridge’s declared preservation.

*(No tooling is implied; these are conceptual moves within the calculus.)*

### C.2:End
