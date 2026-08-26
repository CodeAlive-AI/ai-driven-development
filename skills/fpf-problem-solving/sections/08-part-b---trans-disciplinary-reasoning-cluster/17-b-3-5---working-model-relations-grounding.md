## B.3.5 - Working-Model Relations & Grounding (CT2R-LOG)
> **Status:** Stable
> **Type:** Pattern

**At a glance.** Use B.3.5 when a human-facing structural relation or a collection's own belongs-to relation has been selected for an additional assurance account without exposing constructive machinery as the public vocabulary.

**Use this when.** Use this assurance profile only when a publication choice or named current requirement elects it for a direct relation claim. State the readable relation first. After election, structural parthood and collection belonging follow separate trace and `validationMode` obligations. The trace reports independently grounded facts for inspection; it creates neither the relation occurrence nor the entity it describes.

**What goes wrong if missed.** The readable relation and its assurance account collapse: authors either lose usable relation sentences, treat collection belonging as parthood, prohibit separately grounded parthood by label, or make a trace look like the cause of the claim.

**What this buys.** Working-Model relations stay readable, while an elected assurance branch supplies the right inspectable account without changing the direct relation kind.

**Not this pattern when.** Not this pattern when a direct relation claim is sufficient and no publication choice or current requirement elects this assurance profile. Also not this pattern when the current question is how to construct the trace (`C.13`), which mereology relation kind is intended (`A.14`), whether a new holon exists (`B.2`), or whether a candidate name deserves durable U-kindhood (`E.24.UK`).

> **One‑line summary.**
> CT2R-LOG keeps **ComponentOf**, ordinary belongs-to sentences, **PortionOf**, and **AspectOf** readable while respecting their different relation kinds. When this assurance profile is elected, structural parthood uses its applicable construction account; collection belonging uses a current `C.13 set` trace. Neither branch changes what makes the direct relation obtain, and neither trace decides whether a separate part relation is possible.

### B.3.5:1 - Intent

*Provide a single, human-facing family of **Working-Model** relations as the **public relation layer**, with explicit hooks for (G) grounding and (R) reliability, without exposing constructor jargon or overloading day-to-day authors.*

**What you get (manager/engineer view).**
 The same relations you already know (e.g., **ComponentOf**) remain the **public relation vocabulary**.

**What changes when the profile is elected (auditor/ontologist view).**
* Each covered published edge carries two additional commitments:

  1. **`tv:groundedBy`** → points to the support required by the relation's branch: the applicable `sum` or `slice` trace for structural parthood, one current `C.13 set` trace for the collection's belongs-to relation, or an admissible argument or evidence object for another permitted claim.
  2. **`validationMode ∈ {axiomatic, inferential, postulate}`** → declares how the author justifies the assertion.

The pattern that defines the relation still decides when it obtains. CT2R-LOG records the public alias, the branch-specific support link, and the declared assurance posture; Lang-CHR supplies the labels.

### B.3.5:2 - Problem Frame

B.3.5 exists where a readable Working-Model relation must remain usable by practitioners while assurance readers still need a grounding relation and declared validation stance. The EntityOfConcern is not a notation, trace file, or tool output. It is the relation-use discipline that keeps the public relation layer and assurance grounding layer distinct.

### B.3.5:3 - Problem

Working-Model relations such as **ComponentOf** and an ordinary belongs-to sentence are easy to use but not self-justifying. Their declarations alone do not show which participants and occurrences obtain, which rule defines the relation, or what identifies the whole or collection. Conversely, exposing construction traces everywhere makes the graph unreadable to non-specialists.

**We need**: a stable **public relation layer** for relations and, where this profile is elected, a required, **reconstructible** **grounding channel** plus a visible **validation intent** that downstream assurance can reason about. The direct relation layer does not depend on electing the profile.

### B.3.5:3.1 - Forces

* **Two audiences, one dial.** Project managers want **one relation family** and stable views; assurance readers want an inspectable construction account with explicit direct facts and identity conditions.
* **Parsimony constraint.** The Kernel stays minimal; construction is **outside** the Kernel.
* **Unification inside FPF.** We already unify external vocabularies; the same discipline is applied **internally** so patterns that publish structural claims can reuse one three-form construction-account discipline and one readable relation façade without making that account a second ontology.

### B.3.5:4 - Solution (thumbnail)

CT2R‑LOG introduces a **two‑link discipline** around each canonical edge:

1. **Alias link (concept‑level).**
   **Working-Model relations** (e.g., `ut:ComponentOf`) are the public names for their exact direct relation principles. **`tv:AliasOf`** may point from the public relation kind to that principle for comparison and reuse; the alias defines neither an occurrence nor a whole.

2. **Grounding link (assurance level).**
   Each relation assertion covered by this elected profile carries `tv:groundedBy` according to its direct relation kind:

   * **Structural parthood** (`ComponentOf`, `PortionOf`, or `AspectOf`) requires one current C.2.1 construction-trace episteme in the applicable `sum` or `slice` form and `validationMode=axiomatic`. `postulate` is not available for this branch.
   * **Collection belonging under the collection's own rule** requires one current C.2.1 `C.13 set` trace and `validationMode=axiomatic`. The trace reports the collection, the entity, the already established relation, the rule for belonging, and the identity conditions. It does not make the entity a constructive part, make belonging obtain, or prove that separately grounded parthood is impossible.
   * **Other epistemic or constitutive edges** may use an admissible evidence object or logical argument under `validationMode ∈ {inferential, postulate}` when no constructive trace is appropriate.

3. **Validation flag (author intent).**
   Every relation or aggregation rule covered by this profile carries `tv:validationMode` with one of:
   * **`postulate`** — pragmatic working claim backed by observations;
   * **`inferential`** — reasoned consequence with a followable argument; or
   * **`axiomatic`** — one inspectable construction account is the declared assurance basis.

The direct branch above selects which modes and grounding targets are allowed. The flag is an assurance posture, not a species of world-side relation and not an identity or timelessness guarantee.

> **F–G–R alignment.**
> **F** (the published relation claim): `:PumpA ut:ComponentOf :Skid12`.
> **G** (its inspectable grounding account): the assertion links to `:trace_Γm_sum_456`, a C.2.1 episteme about the exact direct construction facts.
> **R** (the author's declared assurance posture): `tv:validationMode=axiomatic` → one input to B.3.3's **AssuranceLevel** assessment; it does not alter F.

#### B.3.5:4.1 - Structural CT2R Typing-Grounding Unfolding Structure Block

When a constructive trace, working-model relation, and target kind or logical representation must be carried together across contexts, use this block or cite an equivalent `A.22.CGUS` specialization. The block is useful when the reader must see the passage from constructional material to a typed or logical claim without treating a readable relation label as proof.

```text
StructuralCT2RTypingGroundingUnfoldingStructureBlock:
  unfoldingStructureRef: current StructuralCT2RTypingGroundingUnfoldingStructure record
  workingModelOrConstructiveRepresentationRef:
  targetKindOrLogicalRepresentationRef:
  bridgeRef?:
  constructiveTraceRef?:
  preservedStructure:
  lostOrCollapsedStructure:
  CL_or_CLk:
  admissibleReuse:
  blockedSubstitution:
  evidenceOrProofLinkageRef?:
```

`unfoldingStructureRef` names the current local structure record. `StructuralCT2RTypingGroundingUnfoldingStructure` is a local `A.22.CGUS` `U.Structure` specialization whose block is governed by B.3.5 only for structural construction-to-typed/logical projection; the A.22-level relation to that narrower specialization, when needed, is `specializedStructureRef?` on the generic CGUS record. It is not a root U-kind, proof, empirical evidence, work plan, decision, or general ontology-return structure. `C.13` contributes constructive-trace loci; `C.3` contributes kind intent, extent, subkind, and bridge loci; neither creates separate authority for this block.

When an inadequate working account requires general diagnostic recovery of the exact subject construction, use `A.7.1`. That return may stop at a direct relation, system-role assignment, state or capability, Work occurrence, holon recognition, or the pattern for another subject without opening this structural CT2R specialization.

`workingModelOrConstructiveRepresentationRef` names the relation, trace, model, or representation being carried. `targetKindOrLogicalRepresentationRef` names the typed or logical target. `bridgeRef` and `CL_or_CLk` are mandatory when cross-context or kind-level movement is current. `preservedStructure` and `lostOrCollapsedStructure` state what survives the passage and what the published relation no longer carries. Evidence linkage remains with B.3 evidence and assurance subject patterns; proof linkage remains with the proof or mathematical subject pattern that is current. The unfolding block only makes the structure of the passage inspectable.

### B.3.5:5 - Vocabulary & notation (normative)

* **Working-Model relations (front‑stage).**
 `ut:ComponentOf`, `ut:PortionOf`, and `ut:AspectOf` are publication-grade structural relations under their direct A.14 rules. A collection uses the belongs-to predicate defined by the pattern for that collection; FPF has no public generic `ut:MemberOf` relation. Belonging is not a sub-property of `ut:PartOf`, `ut:StructPartOf`, or `ut:EpiPartOf`, but the same entities may separately stand in a constructive part relation when its own rule and all six A.1 matters pass.

* **Alias principle (lexical).**
  `tv:AliasOf` links a **public relation type** to the exact direct relation principle whose reading it carries (for example, `ComponentOf` points to the direct structural-component principle). The alias supports comparison; it neither defines an occurrence nor says that a `sum` expression produced the relation.

* **Grounding (per‑edge).**
 When this profile is elected for structural parthood, `tv:groundedBy` points to the applicable current C.2.1 construction trace and `validationMode=axiomatic`. When elected for collection belonging, it points to one current `C.13 set` trace under the collection's own rule and also uses `validationMode=axiomatic`. Other epistemic or constitutive claims may use a logical argument or evidence object under their permitted mode. Every target supports replay of the assertion's basis; it creates neither the direct occurrence nor entity identity.

* **Trace family.**
  `Γ_m.sum`, `Γ_m.set`, and `Γ_m.slice` are the C.13 forms used by the covered branches. `sum` and `slice` report structural-parthood constructions; `set` reports an already grounded collection and the belongs-to occurrences established under its own rule. No form creates the facts it reports, and no temporal or workflow form is added.

* **Validation flag.**
 `tv:validationMode ∈ {postulate, inferential, axiomatic}` is required on every claim covered by this elected profile. Structural parthood and collection belonging use `axiomatic` with their branch-specific current trace. A direct relation outside the profile has no B.3.5 field obligation.

### B.3.5:6 - Archetypal Grounding - Running example

> **Story.** A refinery team publishes `:PumpA ut:ComponentOf :Skid12`.

* **Publication — Working-Model relation layer.**
  They mint one edge with the **Working-Model** relation **ComponentOf** and declare the published edge's `U.Formality` (typically **F≈F3**, controlled narrative). Only the Working-Model relation is visible to readers.

* **Constructive grounding (Γₘ).**
  In the background, the published assertion links to `:trace_Γₘ_sum_456`, a C.2.1 episteme that names the exact pump and skid, the direct fastening, coupling, enclosure, terminal, flange, and seal occurrences that obtain, the applicable skid assembly rule, and the skid reidentification rule. An auditor replays that account to inspect the assertion's basis. The same listed parts under a different assembly can form another whole, while a permitted pump replacement can preserve Skid12; the direct relations and reidentification rule, not the trace or input list, decide.

* **Assurance stance & R-lane.**
 Because the assertion is linked to an inspectable construction account, authors set `tv:validationMode=axiomatic`. This records their assurance posture; it does not strengthen the direct relation, fix identity, or make either timeless. B.3.3 reads the flag together with the actual grounding, warrants, evidence, and their currentness to assess the appropriate **R** lane. **F**, **G**, and **R** remain orthogonal.

* **Contrast (epistemic).**
When the same team asserts `:MassFlowRepresentation RepresentationOf :FlowModel`, they declare `validationMode=postulate` and attach a calibration dataset (Empirical Validation) instead of a **Γₘ** trace. The edge remains publishable, but reviewers record a lower-confidence stance, and B.3.4’s **evidence ageing** policy will decay its trust over time.

Result: **one** visible relation for engineers, **two** assurance references for reviewers.

**Collection case — Fleet North.** First publish the ordinary sentence: “Vehicle 12 belongs to Fleet North under its registration rule.” Under that rule, the occurrence begins when Fleet North accepts the vehicle's registration, ends on withdrawal or transfer, and a later accepted registration begins another occurrence. If no current publication choice or requirement elects this profile, the direct sentence is sufficient and the author stops.

Here the fleet publication elects the profile. It links the assertion to one current C.13 `Γ_m.set` trace that names Fleet North and its identity rule, Vehicle 12, the obtaining registration occurrence, the registration rule, and its ending and recurrence conditions; it declares `validationMode=axiomatic`. If a vehicle enters or leaves the fleet, or the rule changes, the earlier trace remains an account of its earlier state but is not current support for the later assertion. The register and trace report the relation; neither creates it. They prove neither `ComponentOf` nor that a separately grounded constructive part relation is impossible.

### B.3.5:7 - Author Standard (at a glance)

When you add or import a relation edge:

1. **Pick a Working-Model relation sentence** such as “Impeller ComponentOf Pump” or “Vehicle 12 belongs to Fleet North under its registration rule”; avoid raw `ut:PartOf` unless you are drafting meta-level axioms. If no current publication choice or requirement elects CT2R-LOG, publish that direct claim and stop.

2. **When CT2R-LOG is elected, attach `tv:groundedBy`**:

   * Structural parthood → the applicable current construction trace and `validationMode=axiomatic`.
   * Collection belonging under the collection's own rule → one current `C.13 set` trace and `validationMode=axiomatic`.
   * Another permitted epistemic or constitutive claim → the branch's logical argument or evidence object and allowed mode.
3. **Declare the selected `tv:validationMode`** for every covered claim.


> **What managers see:** nothing new in the graph picture.
> **What auditors get:** a reliable trail from every edge covered by the elected profile back to its inspectable construction or evidence account.

### B.3.5:8 - Compatibility & cross‑references

* **B.3.2 (LOG‑use).** CT2R‑LOG supplies the **places to hang proofs/evidence** that B.3.2 formalizes.
* **B.3.3 (Assurance levels).** `validationMode` + presence/quality of `tv:groundedBy` are the **inputs** to compute `AssuranceLevel (L0–L2)`.
* **B.3.4 (Evidence ageing and currentness).** A relation assertion, its construction-trace episteme, and the warrants or evidence used for it retain their own editions and currentness. `validationMode=axiomatic` does not freeze a trace or make described world-side facts timeless; changed participants, relations, rules, or identity conditions require direct reinspection.

### B.3.5:9 - Rule‑set — CT2R‑LOG (conceptual, human‑first)

**Intent (one line).** Make **Working-Model** relations the canonical relation vocabulary for authors, while providing a clean, purpose-selected bridge to assurance through aliasing and grounding semantics; the bridge is required only for the published assertions covered by an elected B.3.5 profile or named current requirement.

#### B.3.5:9.1 - Vocabulary and meanings in this pattern

* **Working-Model relation.** A human-oriented direct relation statement using a public name such as `ut:ComponentOf`, `ut:PortionOf`, or `ut:AspectOf`, or an ordinary sentence such as “this edition belongs to this product series.” It is the canonical public layer for readers; the direct pattern keeps the relation meaning fixed.

* **Assurance Layer.** Three complementary assurance modes an author MAY attach:

  * **Constructive** grounding: an inspectable account in one of the three C.13 forms (`Γ_m.sum | Γ_m.set | Γ_m.slice`). It names independently grounded participants, direct relation occurrences, the applicable construction rule, and identity or reidentification conditions. No formal notation is required, and the account does not create the relation it reports.
  * **Logical** grounding: a *reasoned* chain (think KD‑CAL style arguments) that shows why the relation follows from stated premises.
  * **Mapping** grounding: a *relation-label alignment* that shows the domain label truly denotes the intended Working-Model relation (Kind-CAL / Lang-CHR stance).
    These three assurance modes are *complementary*, not exclusive.

* **Empirical Validation.** How a published relation meets reality (observations, calibration scenarios). It lives beside, not inside, the relation. (See B.3 family.)

* **Grounding vocabulary (`tv:`).**

  * `tv:AliasOf` — declares that a Working‑Model relation is the **canonical projection** of a more general pattern (its “principle of use”).
  * `tv:groundedBy` — points to the **author's grounding account** (Constructive, Logical, or Mapping, as applicable). When a construction trace is recorded, it is a C.2.1 episteme with its own edition and currentness.
    The `tv:` namespace is part of the Core conceptual lexicon; it is **notation‑agnostic** and **tool‑agnostic**.

* **`tv:validationMode ∈ {postulate, inferential, axiomatic}`.** A **declaration by the author** of the *confidence stance* for a relation instance:
  *postulate* — a pragmatic working claim;
  *inferential* — a reasoned consequence;
  *axiomatic* — the author declares that a constructive account is the assurance basis for this assertion. The mode does not classify the world-side relation and guarantees neither identity nor timelessness.

> **Authoring note.** This pattern defines *meanings*, not formats. The words above SHALL be used consistently and without reference to any specific notations or execution environments (Guard‑Rails: Notational Independence).

#### B.3.5:9.2 - Normative rules (MUST/SHALL clauses for thinking‑and‑writing)

**S‑1 (Working-Model first).**
Authors **SHALL** state each covered direct relation claim in Working-Model form. Assurance accounts remain below that public layer. Electing this profile adds branch-specific trace and mode obligations; it is not a precondition for direct use.

**S‑2 (Alias declaration).**
If a Working‑Model relation follows a known general principle, the author **SHOULD** declare `tv:AliasOf <Principle>`, thereby making the intended *use‑pattern* explicit for reviewers and future readers. (This improves comparability without introducing extra formality.)

**S‑3 (Grounding by mode).**
For every relation instance covered by an elected B.3.5 profile, the author **MUST** set `validationMode` and follow the corresponding grounding stance:

* **S‑3.a `postulate`.** For a branch that permits it, the author may omit constructive grounding, state the working scope, and give the empirical cues that would challenge the claim.

* **S‑3.b `inferential`.** For a branch that permits it, the author gives a short reasoned chain from admitted statements that a peer can follow.

* **S‑3.c `axiomatic`.** The author links the assertion to the current C.2.1 trace episteme required by its branch. A competent peer can recover the exact participants, direct relation occurrence, applicable rule, and identity or reidentification conditions. The account supports inspection; it creates none of those facts.

* **S‑3.d Structural parthood.** A covered `ComponentOf`, `PortionOf`, or `AspectOf` assertion requires `validationMode=axiomatic` and the applicable current C.13 construction account; `postulate` is not available.

* **S‑3.e Collection belonging.** A covered belongs-to assertion uses the rule defined for that collection and requires `validationMode=axiomatic` and one current C.13 `set` trace. The trace reports already established belonging and collection identity. A logical argument or evidence object may support the inclusion decision separately, but neither substitutes for the elected set trace, turns belonging into parthood, or prohibits a separately grounded part claim.

**S-4 (Relation-kind sense-making).**
* For structural `ComponentOf`, `PortionOf`, and `AspectOf` claims, the elected profile requires the applicable current construction account and `validationMode=axiomatic`.

* For collection belonging, the elected profile requires one current `C.13 set` trace and `validationMode=axiomatic`. The collection's own rule still decides whether the occurrence obtains.

* For other epistemic or constitutive links, constructive grounding remains optional and the branch may prefer inferential or postulate reasoning with empirical cues.

**S‑5 (Order and time are not mereology).**
Authors **SHALL NOT** encode execution order, parallelism, or temporal slicing as part‑whole. Such concerns belong to `Γ_method` and `Γ_time` families and **SHOULD** appear as method/time statements adjacent to, not inside, Working‑Model structure. (This prevents conceptual leakage between planes.)

**S‑6 (Unidirectional dependence).**
CT2R‑LOG may *consume* Compose‑CAL and KD‑CAL conceptually; it **SHALL NOT** redefine them. Meaning flows **downward only** (Kernel → Extention → Context → Instance).

**S‑7 (Register discipline).**
When naming principles in `tv:AliasOf`, authors **SHOULD** use Tech/Plain *twin labels* where available and obey minimal‑generality and rewrite rules (LEX‑BUNDLE), so that aliases are recognisable across context of meaning.

**S‑8 (No tool talk).**
Core prose **MUST NOT** introduce CI/CD terms, file formats, APIs, or machine‑oriented notations in place of concepts. If examples are needed, they **MAY** be plain‑language narratives or domain vignettes. (This pattern is conceptual by Standard.)

#### B.3.5:9.3 - Scope & Non‑Goals (to keep the plane clean)

* **In scope.**
  Canonical publication of relations for humans; alias‑to‑principle clarity; conceptual grounding stories; author‑declared *validationMode*; separation of structure vs order/time.

* **Out of scope.**
  Any machinery that *executes* checks; any binding to specific notations; any process/workflow mechanics; any discussion of file formats. (Those belong to tooling publications, pedagogy publications, and companion records; they SHALL NOT be imported by the Conceptual Core.)

* **Edge placements.**
  When a claim is chiefly about *naming fit* across Contexts, prefer **Mapping** grounding (Kind-CAL/Lang‑CHR stance). When it is chiefly about *why* it follows, prefer **Logical** grounding. When it is about *what the whole is, from its parts*, prefer **Constructive** grounding. (Authors MAY combine them.)

#### B.3.5:9.4 - Author’s working moves (micro‑playbook, notation‑free)

**M‑1.** State the relation in **Working‑Model** form (e.g., “Impeller `ComponentOf` Pump”).
**M‑2.** If a publication choice or named current requirement elects this profile, pick `validationMode`; otherwise keep the direct relation claim and stop:

* For a permitted exploratory claim, choose **postulate** and state scope plus challenge cues.
* For a permitted conclusion from known statements, choose **inferential** and list the short argument.
* For structural parthood covered by the profile, choose **axiomatic** and link the applicable current construction account.
* For collection belonging covered by the profile, choose **axiomatic** and link one current `C.13 set` trace that reports the already established relation under the collection's own rule.

**M‑3.** Add `tv:AliasOf` only when a named direct relation principle helps reviewers recognize the intended reading; do not alias the relation to a constructor result.
**M‑4.** Keep *order/time* adjacent, not embedded: if you need “assembled in two parallel lines”, write that as a **method/time** statement next to the structure, not as a part‑of edge.
**M‑5.** Stop when the selected readable relation and remaining non-use boundary are clear and, if this profile is elected, its validation mode and required current support are recoverable without guessing.

### B.3.5:10 - Bias-Annotation (auditable, human-first)

The purpose of this section is to make **typical cognitive slips** visible and name the **counter-moves** an author or assurance reader should apply **in thought**—not with tools. These biases are generic; the remedies point to neighboring FPF guard-rails and patterns.

| Bias (name)                     | Symptom in the model                                                                                                          | Cognitive counter‑move (conceptual only)                                                                                                                                                                          | Where to check                                                       |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **Formalism capture** | A trace, constructor expression, or `validationMode` is treated as the source of the direct relation or whole identity. | Recover the exact participants, direct relation occurrences, construction rule, and identity or reidentification rule first. Treat the trace as a current C.2.1 account and the mode as the author's assurance posture. | CC‑CT2R‑1, CC‑CT2R‑2, CC‑CT2R‑3; C.13 trace separation. |
| **Canonical inversion** | B.3.5 fields are demanded before direct use, or one assurance branch is imposed on every relation. | Use the direct claim first. After election, use the applicable branch: structural parthood or collection belonging takes its required axiomatic trace; other permitted claims may use inferential or postulate support. | CC-CT2R-2, CC-CT2R-3, CC-CT2R-5. |
| **Order/time leakage**          | Encoding sequence or phase as part‑whole edges.                                                                               | Apply **Strict Distinction**: order/time belong to Γ\_method and Γ\_time, not to mereology or CT2R relations.                                                                                                       | B.3 “keep order/time in their own lanes”; cross‑ref Γ\_ctx/Γ\_time.  |
| **Notation lock‑in**            | Letting a diagram or syntax define the meaning (“it’s true because the diagram says so”).                                     | Enforce **Notational Independence**: meaning is defined in prose/maths; renderings are illustrative only.                                                                                                         | Part E guard‑rail on notational independence.                        |
| **Congruence blindness**        | Composing strong parts through weak mappings without acknowledging the fit penalty.                                           | Make **edge‑fit first‑class**: reason about Congruence Level (CL) on connections; penalise low fit conceptually.                                                                                                  | B.3 universal aggregation skeleton (Φ(CL)); anti‑patterns list.      |
| **Collection/composition swap** | A belongs-to predicate is used as `PartOf`, or a part claim is used as collection belonging, and reliability is carried over as if both were one construction. | State collection belonging and constructive parthood separately under A.14. When both obtain, keep both claims and their different `set` and `sum` accounts. | A.14 and C.13. |
| **DesignRunTag chimera**          | Mixing design‑time and run‑time evidence into one “assurance” line.                                                           | Split the **scope** of the claim: `S ∈ {design, run}`; compare side‑by‑side rather than merging.                                                                                                                  | B.3 typed claim tuple & anti‑pattern “DesignRunTag chimera”.           |

> **Reader reminder.** Bias audit is a **reading aid**. It never licenses tooling talk in Core; use the guard‑rails in Part E to keep semantics primacy and unidirectional dependence of layers.

### B.3.5:11 - Conformance Checklist (normative, author-facing)

The following obligations regulate **how to think and write** CT2R content. They are **notation‑agnostic** and purely conceptual.

| ID                                              | Requirement                                                                                                                                                                                                                                   | Purpose                                                                   |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **CC-CT2R-1 (Canonical-first).**                | A relation published for readers **SHALL** be stated in Working-Model terms (`ut:*Of`) as the canonical form; any constructive or logical justification is recorded as **grounding** (not as the definition).                                         | Preserve human-first canon and didactic primacy.                          |
| **CC‑CT2R‑2 (Mode declaration).**               | For every relation or rule covered by an elected B.3.5 profile, the author **SHALL** declare `tv:validationMode ∈ {postulate, inferential, axiomatic}` in prose. A direct relation outside the profile needs no B.3.5 mode. | Make elected assurance intent explicit without taxing ordinary direct use. |
| **CC‑CT2R‑3 (Structural axiomatic grounding).** | A covered structural parthood assertion uses `validationMode=axiomatic` and links to its applicable current C.2.1 `sum` or `slice` construction trace. The account reports independently grounded participants, occurrences, rule, and identity conditions; it creates none. | Make elected structural assurance inspectable without turning it into a truth-maker. |
| **CC‑CT2R‑4 (No order/time in parts).**         | Authors **SHALL NOT** encode order (`Serial/Parallel`) or phase/time as part‑whole relations; handle them via `Γ_method` / `Γ_time` when relevant to the claim.                                                                               | Maintain the structure/order/time firewall.                               |
| **CC‑CT2R‑5 (Collection vs part).** | Authors keep collection belonging under the collection's own rule distinct from every `PartOf` branch. A direct claim needs no profile fields; after B.3.5 election it uses `validationMode=axiomatic` and one current `C.13 set` trace. If constructive parthood also obtains, state and support that claim separately. | Prevent category errors without taxing ordinary belongs-to prose or prohibiting a stronger independently grounded claim. |
| **CC‑CT2R‑5a (Set trace reports).** | The elected set trace names the collection, the entity said to belong, the already established occurrence, the collection's own belongs-to rule, and the identity conditions. It creates none of them and supplies no structural-composition reliability. | Keeps optional assurance from becoming ontology. |
| **CC‑CT2R‑6 (Fit is explicit).** | Where mappings or alignments matter, the author **SHALL** reason about fit explicitly and acknowledge that weak fit reduces the effective reliability of a composed claim. | Keep integration quality first-class. |
| **CC‑CT2R‑7 (Notational independence).**        | Core meaning **MUST NOT** hinge on any specific diagram or syntax; illustrative renderings, if present, are labelled *informative*.                                                                                                           | Ensure longevity and cross‑discipline portability.                        |
| **CC‑CT2R‑8 (Layer direction).**                | Grounding flows **downwards** from Working‑Model to Assurance layers (Mapping/Logical/Constructive). Authors **SHALL** avoid back‑defining the canonical relation by its Mapping, Logical, Constructive, or Empirical grounding.                                                  | Preserve unidirectional dependence of layers.                             |
| **CC‑CT2R‑9 (Scope split).**                    | When assurance is discussed, authors **SHALL** state the **typed claim** and **scope** `S ∈ {design, run}` and keep them distinct in reasoning.                                                                                               | Prevent DesignRunTag chimeras.                                              |

### B.3.5:12 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Trace as relation or truth-maker | A `Gamma_m` trace is treated as the public relation, as proof that the relation obtains, or as the source of whole identity. | Keep the Working-Model relation canonical; recover the direct relation facts and reidentification rule independently; attach the trace only as their inspectable C.2.1 account. |
| Unchecked relation label or mode | A familiar relation label or `axiomatic` flag is published as though either settled relation obtaining or identity. | State and test the direct relation first. When B.3.5 is elected, add the branch-specific mode and support account. Stop when a fact required by the direct pattern is missing. |
| Order/time leakage | Assembly sequence, phase, or parallel work is encoded as a part-whole edge. | Keep order, method, and temporal claims adjacent to the structural edge; do not turn them into mereology. |
| Assurance by notation | A diagram, graph display, or data format is treated as if it made the relation true. | Treat representations as publication forms; keep the relation claim, grounding relation, and validation mode explicit. |

### B.3.5:13 - Consequences (benefits, trade-offs, mitigations)

**Benefits**

* **Cognitive clarity for authors and readers.** Working-Model relations remain canonical while assurance accounts stay beneath them. Every claim covered by the elected profile carries only its branch-specific support account; ordinary direct claims remain lightweight. CT2R preserves a path to higher assurance while keeping collection belonging distinct from constructive parthood and order and time outside structure.
* **Progressive assurance without tooling commitments.** The *postulate → inferential → axiomatic* assurance-posture progression lets teams raise assurance deliberately, matching their context and risk, in line with B.3.3’s maturity logic.
* **Explicit fit management.** Treating edge‑fit (CL) as a first‑class concern prevents silent over‑confidence: weak mappings visibly cap reliability of composed claims.
* **Cleaner separation of concerns.** Distinguishing collections from compositions and keeping sequence/time in Γ\_method and Γ\_time prevents recurrent category errors and preserves Γ‑algebra reviewability.

**Trade‑offs & mitigations**

* **Extra prose discipline.** Declaring `validationMode` and writing a short grounding narrative (when *axiomatic*) adds authoring effort. *Mitigation:* reuse local templates; keep narratives concise and Γ\_m‑oriented by idea rather than notation.
* **Temptation to stay “forever postulate.”** Teams may stop at Working‑Model relations. *Mitigation:* use B.3.3’s subtypes/levels as a **planning aid** to decide where *axiomatic* or *inferential* grounding is worth the cost.
* **Perceived conservatism.** Acknowledging weak fit (CL) may lower effective reliability of otherwise strong parts. *Mitigation:* treat CL as a guide to improvement (reconcile terms, align units, verify declared links) rather than a punishment.

> **One‑line takeaway for managers.**
> CT2R lets you **talk in natural, domain‑meaningful relations** while preserving a clear, optional path to formal grounding and empirical checking—so confidence can grow deliberately without dragging your model into tooling or syntax.

### B.3.5:14 - Rationale (informative)

**14.1 Why canonical‑first?**
CT2R-LOG treats the **human-readable, task-appropriate relation** (e.g., `ut:ComponentOf`) as the **canonical publication form** because that is what engineers and managers actually use to reason, decide, and communicate. The formal layers **ground** that form; they do not replace it. This is consistent with the authoring Standard in Part E (pattern template and style guide), which privileges **clarity, purpose and didactics** over premature formalism in the body text. Authors write *for people first*, then point to the kind of assurance they are invoking.

**14.2 Why two `tv:` links—and why concept‑only?**
`tv:AliasOf` and `tv:groundedBy` name **conceptual bridges** from a public Working-Model relation to its direct principle and assurance account. They mandate no notation. They keep authors explicit about the relation reading, the support being invoked, and when that support must be current, without letting an alias, trace, or mode define the world-side occurrence.

**14.3 Why a triad of `validationMode`?**
The triad **{postulate, inferential, axiomatic}** expresses staged formality compatible with the FPF stance on staged assurance: start with what the team can responsibly claim now, then move to stricter justification where risk or context demands it. That gives reviewers a shared vocabulary for the declared assurance posture of a claim without changing the canonical relation itself.

**14.4 Why keep order/time out of mereology?**
CT2R‑LOG aligns with A.14’s **firewall**: structure (parthood) is distinct from **order** and **temporal coverage**. The former is published as `ut:StructPartOf` sub‑relations; the latter live in `Γ_method` / `Γ_time` and must **not** be smuggled into part‑trees. This separation avoids classic modelling failures (temporal smearing, pseudo‑components for quantities) and keeps reasoning crisp across the Γ‑family.

**14.5 Why point to `Γ_m.sum | set | slice` (Compose‑CAL) for constructive grounding?**
The three C.13 forms—**sum, set, slice**—are sufficient to report the recurring construction accounts for integrated assemblies, collections, and aspects without expanding the kernel. They are not identity functions. A truthful account carries exact participants, direct relation occurrences, the applicable rule, and identity or reidentification conditions: the same inputs under another assembly can form another whole, while a permitted replacement can preserve one whole.

**14.6 Why mental obligations rather than process mandates?**
Part E requires that patterns define or constrain **thinking** and **authoring**; enforcement and automation, if any, are external concerns. CT2R‑LOG therefore states obligations as **self‑contained cognitive checks**: declare your mode; tell the constructive story only when you claim *axiomatic* strength; keep order/time in their places. This keeps the core specification **evergreen and tool‑agnostic**, as required.

### B.3.5:14.7 - SoTA-Echoing

Checked 2026-08-25. Three source lines change this pattern's method; none supplies its ontology wholesale.

| Source line | Adopt, adapt, or reject | Change in B.3.5 |
| --- | --- | --- |
| A.14's current constructional comparison | **Adopt** construction and identity before relation choice. **Reject** both a universal collection-membership predicate and any inference from belonging either to parthood or to the impossibility of parthood. | `S-3.d/e`, `CC-CT2R-3/5/5a`, and the Fleet North case keep collection belonging and a separately grounded part claim distinct. |
| [ISO/IEC/IEEE 15026-2:2022, *Assurance case*](https://www.iso.org/standard/80625.html) | **Adapt** its separate, maintained assurance-case structure: an elected support account stays inspectable and current beside the claim it supports. **Reject** a mandatory full assurance case for every direct relation. The FPF-specific `validationMode` triad is only the author's declared posture; the standard is not cited as its source. | The Solution, `S-2/S-3`, B.3.4 currentness relation, and conformance rows require support only after profile election and keep claim, support, and posture separate. |
| NIST's current [Digital Thread for Manufacturing](https://www.nist.gov/programs-projects/digital-thread-manufacturing) programme | **Adapt** traceable model-based information, validation, and conformance across engineering, manufacturing, and quality. **Reject** a shared model, thread, exchange, or passing syntax check as proof of a world-side relation. | `tv:groundedBy`, the trace-family rule, and the two worked cases keep the support account versioned and inspectable while the direct relation and its own rule decide what obtains; a trace or evidence item creates neither the relation nor its identity. |

At comparable correctness and currentness, always exposing the heavier account costs more to write and read, while a bare direct sentence cannot meet an elected assurance need. B.3.5 therefore starts with one readable relation and adds one branch-specific account only when the publication elects the profile. The cost is that the relation assertion and its support must be checked for currentness separately.

Reopen only the affected source row and rule if A.14 changes the construction/belonging decision, a later ISO 15026-2 edition changes assurance-case structure or maintenance, or newer model-based-engineering evidence demonstrates a lower-effort way to retain direct meaning, declared posture, traceability, and independent currentness. A changed member, rule, trace, or evidence item instead reopens the affected assertion; it does not by itself reopen this architecture.

### B.3.5:15 - Relations

**Builds on**
- **A.14 Advanced Mereology** — supplies direct structural relations and the discipline for collection belonging under each collection's own rule and separately grounded parthood; B.3.5 adds only the assurance branch elected for the relation.
- **A.11 Ontological Parsimony (C‑5)** — constructive grounding lives in a calculus; the kernel remains minimal.
- **B.1 Universal Γ** — shared invariants and the placement of order/time in their respective Γ‑flavours.
- **Part E authoring rules** — canonical pattern template and notational independence, which CT2R‑LOG explicitly follows.

**Coordinates with**
- **Compose-CAL (`Γ_m`) and `C.13`** — supply current construction accounts for structural parthood and the `set` account for elected assurance of collection belonging. Each trace reports facts whose meanings and conditions come from the pattern that defines the relation.
- **A.22.CGUS / StructuralCT2RTypingGroundingUnfoldingStructureBlock** — provides the local structural CT2R unfolding block when a constructive trace, working-model relation, target kind or logical representation, bridge, preserved structure, and loss must be inspected together; `A.7.1` is the pattern for general diagnostic return to a subject construction.
- **KD‑CAL** — provides the **logical** shoulder (inferential justification) when authors pick `validationMode = inferential`.
- **Kind-CAL / Lang-CHR** — provide the **mapping** shoulder (kind and relation-label alignment) governing alias policies without altering Working-Model relations.

**Constrained by**
- **Notational Independence (E.5.2)** — CT2R‑LOG refuses to prescribe formats, keeping all obligations conceptual.

**Specialises / feeds**
- **B.3.1–B.3.4** — supplies the publication discipline (Working-Model relations, declared **relation kind** and **validationMode**; **F** per C.2.3 where relevant) that B.3’s trust calculus expects; interacts with ageing and assurance-level assessments without changing the relations themselves.

**Non‑relations**
**No introduction of order/time** — CT2R‑LOG does **not** define `SerialStepOf` / `ParallelFactorOf` / temporal **phases**; those belong to **Method‑CAL** and **Sys‑CAL (TemporalPart)** respectively.

### B.3.5:End

