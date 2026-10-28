## C.2 - Epistemic holon composition (KD-CAL)

> **Status:** Stable

**Scope & exports.** A substrate-neutral calculus for composing **epistemic holons** (`U.Episteme`) and reasoning about their change and equivalence. Exports: (i) three distinct **assessment aspects**—**Formality F**, **ClaimScope G**, **Reliability R**—for one exact claim-bearing episteme and stated use; (ii) a **pairwise ladder** of **Congruence Levels (CL 0…3)**; (iii) four **Δ-moves** (*Formalise, Generalise/Specialise, Calibrate/Validate, Congrue*); (iv) **composition rules** (Γ_epist) for aggregates; and (v) propagation laws for CL through mappings and notation relations. C.2.1 identifies an episteme by its exact claim content, exact EntityOfConcern, and effective `U.ReferenceScheme` under `EpistemeConstitutionRelation`. Empirical grounding and edition are separate C.2.1 relations. Viewpoint selection and `U.View` conformance use E.17.0; mathematical or diagrammatic representation uses C.29 and A.6.3.RT; publication uses E.17/E.24.PUB; a carrier remains a distinct entity. Every F–G–R computation names the exact claim and its `U.ClaimScope`. If a path changes scope, notation, kind, reference plane, source-local meaning, model-use basis, or evidence basis, it names the actual relation traversed and applies only the loss that relation declares.

**Formality F** is the assessment of expression properties governed by **C.2.3**. KD-CAL uses the properties required by the receiving operation, with any local ordered summary explicitly declared. It supplies no universal rank of languages or logics.

### C.2:1 - Problem Frame

FPF fixes two archetypal sub-holons: **`U.System`** (physical/operational) and **`U.Episteme`** (knowledge holon). KD-CAL is the primary composition pattern for `U.Episteme`, giving engineers a way to say (a) which expression properties an episteme supplies for the receiving use (**F**), (b) where its exact claim is asserted to apply (**G**), (c) how well that claim is warranted by evidence or severe tests (**R**), and (d) how closely **two** epistemes coincide (**CL**). C.2.1 supplies the constitution test: exact claim content, one exact EntityOfConcern, and one effective `U.ReferenceScheme`. Grounding, edition, viewpoint, view, representation, publication, form, and carrier remain neighboring objects or relations under their direct patterns.

### C.2:2 - Problem

A proof is treated as evidence that an actual system meets its assumptions, or a program as if it entailed a theorem. Warrant becomes opaque when support and its applicable currentness conditions are not explicit. Attributing performed Work to a standard conceals the system that performs it. Aggregation can hide a missing necessary premise, erase complementary support, or conceal contrary evidence behind an unjustified score. KD-CAL keeps constitution, input meanings, scales, and support dependencies explicit.

### C.2:3 - Forces

* **Universality vs domain idioms.** One calculus must cover physics theories, legal codes, safety specs, algorithms, and formal proofs without flattening their differences.
* **Meaning vs materiality.** The same claims can appear on different carriers. When a historical use depends on a particular source, its provenance must remain recoverable.
* **Deductive vs empirical.** Axiomatic certainty and empirical trust have different evidence-continuity profiles; both must compose.
* **Abstraction vs enactment.** Epistemes constrain action; **systems** act. The calculus must keep the roles distinct.

### C.2:4 - Solution

#### C.2:4.1 - Coordinates, constitution, and neighboring relations

**KD-CAL assessments for one exact episteme and use.**

* **Formality F.** The relevant properties of the expressed claim or argument: terms, predicates, semantics and inferences. Litmus: *does this expression supply what the receiving interpretation, execution or check needs?* An expressed derivation and evidence that it passed a checker remain distinguishable.
* **Claim scope (G), a set‑valued applicability over `U.ContextSlice`, with ∩/SpanUnion/translate algebra; CL penalties apply to R, not to F/G.** Litmus: *how wide is the declared scope, and under what minimal assumptions does the claim hold?*
* **Reliability R.** Warrant for this exact claim and receiving use. Litmus: *what supports this conclusion, under which assumptions, and what limits it?* **R-claims MUST bind to their actual formal or empirical support.** A numerical R requires the B.3/C.2.2 meaning, scale, and model; otherwise retain separate support and a bounded reasoned conclusion. A proof under axioms needs no empirical score, and F cannot be substituted for R. Relevance windows and B.3.4 currentness rules apply where the relied-on support consumes them.

 **Congruence Level (CL), pairwise ladder.**
 `CL‑0` **Opposed/Disjoint** (contrastive; no substitution); `CL‑1` **Comparable / Naming‑only** (label similarity; no substitution); `CL‑2` **Translatable** (structure‑preserving correspondence in a declared fragment with **stated loss**); `CL‑3` **Near‑identity** (the declared invariants match). *CL is a characteristic of a relation between two epistemes; it is not a fourth member of the F–G–R assurance tuple and it is not a characteristic space of its own.* **KD-CAL substitution constraint:** plane preservation and **CL ≥ 2** are necessary for a substitution under this calculus; substituting **type‑structure** additionally requires **CL = 3**. These conditions do not establish suitability for the proposed use. State the exact substitution, direction, correspondence rule, and tolerated loss under the direct receiving pattern, and establish reliance separately. When local meanings cross semantic contexts, first test the F.9 Bridge predicate on exact F.17 cells; keep the obtaining Bridge, bounded-use claim, and reliance result distinct. A CL value establishes no local system-role-kind membership or assignment.

**Constitution and neighboring relations.** For a KD-CAL F–G–R assessment, recover F, G, and R for one exact claim and use of one C.2.1 episteme. The episteme's exact claim content, EntityOfConcern, and effective `U.ReferenceScheme` identify the episteme through `EpistemeConstitutionRelation`. F characterizes the claim's form; G is the separate `U.ClaimScope`; R relies on exact evaluation, evidence-use, and assurance relations. Empirical grounding and edition remain separate C.2.1 relations. Viewpoint selection and view conformance remain under E.17.0; notation and other representation structure remain under C.29/A.6.3.RT; publication occurrence, form, and carrier remain under E.17/E.24.PUB. Multiple notations are allowed only when their exact representation or notation relation is explicit and any declared loss is applied to R rather than hidden in an omnibus episteme field.

#### C.2:4.2 - Four Δ‑moves (epistemic motion)

* **ΔF — Formalise.** Make the expression property needed by the receiving use explicit or stricter: resolve terms, supply a predicate or semantics, or express a required derivation. Name the changed property; a different calculus alone establishes no increase.
* **ΔG — Generalise / Specialise.** Widen or narrow the **claim scope** (assumptions & scope). Changes to decomposition granularity are an **orthogonal view** and do not change **G** unless they alter the envelope.
* **ΔR — Calibrate / Validate.** Revise warrant through support that actually bears on the claim: proof or reasoning, calibration, severe tests, or monitoring as applicable. State what the contribution changes. A formalization alone is ΔF, not an R increase; choosing new inquiry is a separate decision.
* **ΔCL — Congrue.** Establish or revise the congruence relation between **two** epistemes and state its warranted level (CL 0…3) under the declared correspondence rule.
  Moves compose into **paths**. A CL chain minimum retains only the ordered congruence meaning justified by the relation family; it is not a numerical reliability loss.

#### C.2:4.3 - Composition (Γ_epist) and propagation

Let **Γ_epist** compose exact epistemes `{Eᵢ}` for one declared claim and use. B.1.3 supplies the synthesis/compilation Method; B.3 and C.2.2 govern warrant and scale discipline.

* **R (Reliability).** First distinguish indispensable premises, alternative sufficient arguments, complementary evidence, different scope slices, and counterevidence. Identify duplicated data and shared assumptions or bias. A numerical fold requires warranted input meanings, compatible scales, dependencies, and a receiving model. Neither series nor parallel syntax supplies a default minimum or maximum, and there is no universal cap at the best support line. Where no common model is justified, retain separate contributions and limitations in a bounded reasoned synthesis.
* **F (Formality).** Assess the expression properties needed from the essential constituents and their connecting inferences under C.2.3:15.1. The composition must preserve the claimed properties. A minimum is only a conditional bound on a shared local ordered scale with an established composition rule, not a universal value for the whole. Formalization changes its stated properties; neither an axiomatic mode nor a `line=formal` tag converts them into empirical warrant.
* **G (ClaimScope).** Required premises compose only on their overlapping scope. Distinct supported slices may form `SpanUnion({G_path})` under A.2.6 and C.2.2's type-before-scope rule; retain their support separately and drop unsupported regions. A new source does not by itself generalise the claim. Scope change remains an explicit ΔG± move.
* **CL (Congruence).** Keep each traversed mapping and the ordered meaning of its declared CL visible. A chain minimum is usable where that relation's congruence rule justifies it. A notation, scope-translation, kind, plane, source-local, model-use, or evidence-reuse relation contributes only its own warranted loss. A numerical Φ needs its receiving model; a monotone table or clipped output does not supply one.

For example, two necessary independent conditions with probabilities 0.9 each have conjunction probability 0.81, not minimum 0.9. Conversely, a limited complementary source need not reduce the support already available. A credible contrary result changes the affected conclusion. A theorem A ⇒ P remains valid as a formal result while evidence violating A can defeat its use as assurance of an actual system.

Γ remains defined on holons and respects the core's identity and boundary discipline. Its support account establishes neither a new action permission nor the worth of acquiring further evidence.

#### C.2:4.4 - What **must not** be conflated (normative guards)

* **Representation structure ≠ carrier.** Files, PDFs, or repositories are **carriers** outside the episteme; they never count as parts of `U.Episteme` (**see C.2.1:4.1–4.2, :4.6, and :11 item 11**).
* **Work and guidance.** **Systems** perform Work. Epistemes can guide or constrain that Work through their claim content; keep the guiding content distinct from its performer.
* **CL is not a score.** It is a **qualitative ladder** of preservation classes; do not average it.

### C.2:5 - ✱ Archetypal Grounding (Tell–Show–Show)

**Universal rule (tell).** *Compose knowledge by Γ_epist with explicit support roles, dependence, scope, and justified input scales. Use the receiving model for any R calculation, or return a bounded non-aggregate synthesis. Identify the episteme by exact claim content, EntityOfConcern, and effective reference scheme; keep empirical grounding, edition, viewpoint selection, view conformance, representation, publication form, publication occurrence, and carrier in their own direct relations.*

**System (show, current physical-system lens).** Consider a **battery-pack thermal subsystem** integrating a physics model of heat flow and an operating envelope for fast-charge. As a **system**, it composes pumps, sensors, and controllers through the system, composition, boundary, state, and dynamics guidance in `A.1`, `A.14`, `A.22`, and `A.3.4`, with conservation constraints made explicit; `B.1.6` and `C.16` govern resource and measurement claims as applicable. Planned `C.1` (Sys-CAL) may later consolidate that guidance, but it supplies no current governing semantics. The assurance story depends on epistemes about the model and envelope; the system **acts**, epistemes constrain.

**Episteme (show, KD-CAL lens).** Consider a **CMIP-class climate projection episteme**: its exact claim content covers PDEs and parameterisations; its EntityOfConcern identifies what the projection claims concern; and its effective reference scheme supplies the interpretation rules. A separate `U.ClaimScope` names historical forcings, resolution, and assumptions. Any empirical-grounding occurrence names the grounding holon and covered claim subgraph separately. Its representation may include domain equations and a tabular schema linked by an explicit notation or representation relation with stated loss. When composing radiation, cloud, and ocean-mixing contributions, identify which assumptions the particular projection requires and what each hindcast actually tests. Shared models or data do not establish independent confirmation. An aggregate R needs the domain quantity and dependency model; otherwise retain the separate tests, assumptions, scope limits, and any disagreements. F describes the required expression properties of the essential constituents and their connections, including the interpretation of the coupled equations.

### C.2:6 - Bias‑Annotation

* **Metric worship.** Treating `[F,G,R]` as ends rather than means; mitigation: require **evidence bindings** and narrative of limits in the claim scope and grounding envelope.
* **Category slip.** Equating a notation, view, publication form, or carrier with claim content, EntityOfConcern, effective reference scheme, or an empirical-grounding participant; mitigation: apply C.2.1 constitution and then the direct neighboring relation pattern.
* **Analogy inflation.** Presenting CL‑0/1 as identity; mitigation: always name the **CL rung** for cross‑mappings.

### C.2:7 - Conformance Checklist

1. **C2-1 (Episteme constitution and neighbors).** Every `U.Episteme` **MUST** satisfy C.2.1 constitution through exact claim content, one exact EntityOfConcern, and one effective `U.ReferenceScheme`. Empirical grounding and edition are stated through their separate C.2.1 relations. Viewpoint selection and `U.View` conformance use E.17.0; representation uses C.29/A.6.3.RT; publication occurrence, form, and carrier use E.17/E.24.PUB. None is treated as an episteme slot or identity component merely because a record or notation places it beside the constitution values.
2. **C2-2 (Assessment meaning).** When a KD-CAL F–G–R assessment is stated or used, `[F,G,R]` **SHALL** be recoverable for one exact claim and use, with a brief rationale. Identifying or publishing an episteme does not by itself require this tuple. F names the relevant expression-property assessment under C.2.3; a local rank requires its declared scale and mapping and is not a global F value. Where R has no justified numerical model, retain its unquantified support and bounded conclusion. Formal validity needs no empirical score. CL is declared for **pairs only**.
3. **C2‑3 (Composition).** Authors **SHALL** identify support roles and dependencies under B.1.3/C.2.2 before combining inputs. Any numerical R or loss **MUST** have justified meanings, scales, assumptions, and a receiving model under B.3; no universal min/max or F-to-R conversion applies. Otherwise return separate support and a bounded synthesis. F requires the properties of the essential constituents and their connections to support the claimed whole under C.2.3; G uses applicable path intersections and supported SpanUnion under A.2.6. Every reuse **MUST** name the actual direct relation and retain its warranted limitation; do not hide contrary evidence or unsupported scope.
4. **C2‑4 (NotationBridge).** Multi‑notation representation components **SHOULD** register `NotationBridge` edges with CL and loss note; any cross‑notation reasoning **MUST** cite the bridge’s CL.
5. **C2‑5 (Work performer).** The performer of `U.Work` **MUST** be a System. Keep any guiding episteme distinct from that performer.

### C.2:8 - Consequences

**Benefits.** A compact map for knowledge epistemes; visible support dependencies and limitations; useful formal and qualitative results alongside justified calculations; disciplined reuse across domains with explicit CL; consistent separation of meaning from material carriers.
**Trade-offs.** Authors must identify the support relation and any calculation model; multi-notation work keeps its relation-specific basis. Some useful syntheses have no common scalar. *Mitigation:* the C.2.1 constitution test and direct neighboring patterns keep the ordinary entry brief while preserving recoverable precision.

### C.2:9 - Rationale

KD-CAL composes C.2.1 epistemes through the relations among their claims and support. Exact claim content, EntityOfConcern, and effective reference scheme keep episteme identity stable; formal structure and claim scope (**F,G**), evidence (**R**), and pairwise congruence (**CL**) remain distinct in composition. Direct grounding, edition, view, representation, publication, and carrier patterns prevent category collapse. **G** concerns the claim’s applicability; changing decomposition detail changes G only if it changes that applicability.

### C.2:10 - Relations

* **Depends on:** `C.2.1 U.Episteme: Constitution, Empirical Grounding, and Edition Relations` for episteme identity, the constitution relation, and the separate grounding and edition relations; `E.17.0` for viewpoint selection and `U.View` conformance; `C.29` and `A.6.3.RT` for representation; and `E.17`/`E.24.PUB` for publication occurrence, form, and carrier.
* **Peers:** planned **Sys-CAL** (`C.1`) may later consolidate physical-system guidance; current system composition, boundary, state, conservation, resource, and measurement claims use `A.1`, `A.14`, `A.22`, `A.3.4`, `B.1.6`, and `C.16` as applicable. KD-CAL composes **epistemes** and feeds assurance lenses in Part B.

### C.2:11 - Worked mini‑examples

* **Formalization (ΔF).** Recasting a **variational free-energy** narrative into a typed calculus can make its variables, assumptions and inferential relations explicit. State those changes and any corrected scope. A correspondence between biological and ML formulations still needs its own mapping and preservation basis; formalization alone establishes neither that correspondence nor an empirical gain (**R**).
* **Complementary hindcast evidence.** Two hindcast lines supporting a climate projection may address different errors, reuse data, or cover different conditions. Identify those relations before combining them; a maximum may select one attested argument only under that declared meaning, not measure their combined corroboration. Keep disagreement and unsupported scope visible. This illustration supplies no climate-specific reliability model.
* **Notation bridge (CL drop).** Rendering a **type‑theoretic specification** in a semi‑formal DSL that omits a declared source invariant requires a `NotationBridge` stating those losses and a CL<3 value. Any transported theorem must respect the bridge’s declared preservation.

### C.2:End
