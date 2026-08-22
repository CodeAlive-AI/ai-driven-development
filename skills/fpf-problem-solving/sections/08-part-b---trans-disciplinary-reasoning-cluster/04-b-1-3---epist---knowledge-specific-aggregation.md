## B.1.3 - Γ_epist - Knowledge‑Specific Aggregation

**At a glance.** Use B.1.3 to compose exact `U.Episteme` inputs into one knowledge aggregate while preserving provenance, conceptual fit, context, and conservative assurance bounds.

**Use this when.** Use this pattern when a named synthesis or compilation use depends on how claims, models, datasets, or arguments are combined, and the aggregation must keep source, mapping, conflict, order, and temporal qualifications inspectable.

**Not this pattern when.** Use C.2.1 for episteme identity and edition continuity, A.14 for a proper temporal restriction of one unchanged episteme, A.15.1 for Work parts or occurrences, B.1.4 for a bounded aggregation of already recovered order or temporal relations, and B.3 for the assurance claim that consumes the aggregate.

**What changes in practice.** Identify every input episteme and mapping before folding; preserve provenance and conflicts; and return identity, edition, temporal restriction, Work, publication, and assurance questions to their subject patterns.

> **► decided‑by: A.14 Advanced Mereology**
**A.14/C.2.1 compliance —** Use **ConstituentOf** for semantic parts and **PortionOf** only for quantitative splits of texts/data with declared μ. Use `PhaseOf` only for a proper interval of one unchanged C.2.1 episteme. When a MethodDescription or document episteme's claim content, EntityOfConcern, or effective ReferenceScheme changes, identify another episteme and assert `EpistemeEditionRelation` only when its historical-continuation predicate obtains. Work segmentation uses A.15.1; no **ComponentOf** is used here.

> **Plain‑English headline.**
> **Γ\_epist** composes **epistemic holons** (claims, models, datasets, arguments) into a **single episteme** while preserving **provenance**, applying **conservative trust bounds** (B.3 F/G/R), and penalizing **poor conceptual fit** via **congruence levels (CL)**. It is **not** a physical sum; it is a **semantic and evidential fold**.

### B.1.3:1 - Problem frame

* **Holonic foundation.** In the FPF, a `U.Episteme` is a holon whose identity is **knowledge-bearing** (A.1). It can be a **statement/claim**, a **model**, a **theory**, a **specification**, a **dataset with semantics**, or a **compiled claim-bearing synthesis**.
* **Strict Distinction (A.15).** We separate:
  **structure** (what the episteme comprises), **order** (argument flow), **identity and history** (C.2.1 identities and edition relations), **proper temporal restriction** (A.14), **work** (what was spent to produce/validate it), and **values** (objectives/criteria). Γ\_epist stays in the **structure/semantics** lane and calls out to Γ\_ctx/Γ\_time/Γ\_work only after their direct inputs are recovered.
* **Mereology (A.14).** For knowledge composition we primarily use **ConstituentOf** (logical/semantic parts), **UsageOf/ReferenceTo** (external reliance), and **MemberOf** for **collections** (anthologies, corpora). We do **not** use **ComponentOf** (physical) in Γ\_epist.
  `PhaseOf` may restrict the **same unchanged episteme** to a proper interval when its complete C.2.1 identity triple remains fixed. Distinct labelled versions or revisions require distinct C.2.1 identities when a discriminator changes and an independently obtaining `EpistemeEditionRelation` for any claimed historical continuation. Knowledge does not act and acquires neither a work-facing local system-role kind nor an assignment. Ordinary prose may say, for example, "the researcher synthesized the sources". If the receiving use does not identify that action as one particular dated `U.Work` occurrence, stop with the ordinary sentence. If it does, use the complete A.15.1/F.6 basis; a short local projection may omit an unused assignment identifier, but not the underlying assignment or attribution.
* **Assurance (B.3).** Knowledge carries **F**, **G**, **R** (Formality, ClaimScope, Reliability). Integration edges carry **CL** (congruence level) that penalizes poor fit. Γ\_epist **must** preserve provenance and apply **conservative** bounds: no “truth averaging,” no silent context hops. **Obligations here are mode/assurance‑gated per C.2.1.**  # [M‑0]
* **Order/time flavours.** Argument sequences may need **Γ_ctx** (non-commutative ordering of premises to conclusion). Knowledge evolution first uses C.2.1 to identify exact epistemes and any obtaining edition relations; B.1.4/**Γ_time** may then aggregate already recovered temporal restrictions, relation order, deprecation, or update windows for a bounded use. The aggregation creates neither identity nor continuity. Open B.2 only if the synthesis leaves a genuine whole-reidentification question after the existing-whole explanation check and identifies an exact candidate new whole; new wording or explanatory gain alone is not MHT.

### B.1.3:2 - Problem

Naive aggregation of knowledge holons causes recurring failures:

1. **Trust inflation by averaging.** Averaging confidences of conflicting claims creates a falsely “reliable” whole; violates **WLNK** and **B.3** conservatism.
2. **Provenance erasure.** Merges that drop sources, methods, or links break **A.10 Evidence Graph Referring** and make results unauditable.
3. **Semantic drift.** Folding across mismatched concepts without explicit **mappings** (and their **CL**) yields incoherent composites that look formal but mean nothing.
4. **Order blindness.** Arguments with essential **dependency order** (premise ⇒ lemma ⇒ conclusion) are treated as sets; non‑commutativity is lost and results become non‑reproducible.
5. **Semantic-context chimeras.** Combining claims whose local senses or reference schemes differ, without exact mappings and—when meanings cross—an F.9 Bridge plus a separately warranted bounded-use claim, silently corrupts claims and inflates **R**.
6. **Category errors.** Importing **Γ\_sys** rules (e.g., “sum truth,” “avg formality”) into knowledge composition produces physically sounding but epistemically nonsensical models.

### B.1.3:3 - Forces

| Force                                      | Tension                                                                                                                      |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Conservatism vs. Synthesis**             | Keep **reliability** bounded by the weakest supported link ↔ allow genuine explanatory integration when it actually emerges. |
| **Universality vs. Domain nuance**         | One operator across math, science, engineering specs ↔ domain‑specific semantics and evidence patterns differ.               |
| **Provenance fidelity vs. Cognitive load** | Keep the **full trail** of sources and methods ↔ avoid overwhelming authors with bookkeeping.                                |
| **Order/time discipline vs. Flow** | Respect argument **order**, exact episteme identity and edition relations, and any proper temporal restriction ↔ keep composition usable for day-to-day synthesis. |
| **Parsimony vs. Fit**                      | Small rule set (A.11) ↔ explicit **congruence** penalties and **context** rebasing when needed.                              |

### B.1.3:4 - Solution — **Terms, operator family, invariant Standard, core rules**

#### B.1.3:4.1 - Terms (didactic recap)

* **U.Episteme** — a claim-bearing knowledge holon. C.2.1 identifies it through the participant-determined `EpistemeConstitutionRelation` over `<claim content, exact EntityOfConcern, effective ReferenceScheme>`. `ClaimGraphSlot`, `EntityOfConcernSlot`, and `ReferenceSchemeSlot` name participant meanings only inside that relation's reusable declaration; they are not internal slots of the episteme. Empirical grounding uses the separate `EpistemeEmpiricalGroundingRelation`, while text, code, figures, datasets, SCR/RSCR references, publication forms, and presentation carriers remain separately governed provenance, representation, publication, or carrier material.
* **Evidence/Provenance Graph** — edges like **evidences**, **derivesFrom**, **usesMethod**, **isMeasuredBy** with anchors (A.10).
* **Semantic mapping** — the exact correspondence rule used by this fold. When it crosses semantic contexts, identify the source and receiving F.17 `SchemeSenseCell` values and an obtaining F.9 `Bridge`; keep the proposed use, direction, use-specific rule, permitted loss, reliance, and **CL** evidence summary separate. F.9 does not require CL for every Bridge, but B.1.3 admits a mapping into its reliability fold only when that summary is present. CL can lower the estimate and never grants the use.
* **SCR** — a `U.SCR` that lists all symbol carriers included in the aggregate; **never dropped**.
* **Semantic context** — Plain shorthand for the local interpretation basis recovered from one exact F.17 `SchemeSenseCell` as `<ReferenceScheme, LocalSenseClaim>`. It is not another operation argument or entity. Crossing between two such contexts uses F.9 and the separate bounded-use and reliance steps above.

> **Didactic reminders.**
> • Knowledge does **not** act. A researcher or engineer may use it while performing Work. Recover the exact System and Work only when the receiving claim consumes them; use A.12 only when the acting-side distinction is itself current.
> • **MemberOf** creates **collections**; it is not a semantic argument link. Use **ConstituentOf** for logical/evidential composition.
> • `PhaseOf` is only a proper temporal restriction of one unchanged episteme. Changed C.2.1 discriminators identify another episteme; test `EpistemeEditionRelation` separately. Use MHT only for a remaining whole-reidentification question, not as a substitute for C.2.1 identity.

#### B.1.3:4.2 - The operator family (companion flavours)

To keep **design vs run** clean (A.15), Γ_epist has two companion flavours that share the same algebra but answer different semantic questions. Their declarations contain only the values on which the result depends. A performer, local system-role kind, or assignment is therefore not an operator argument: the same fold can be specified before staffing and can be applied in Work performed by different Systems without changing its result semantics.

When one particular operation application matters, use A.6.1 for that application and its argument and result bindings. A practitioner sentence may still say "the engineer compiled the guidance". If no particular dated `U.Work` claim is current, that ordinary sentence needs no classification or assignment apparatus. If one is current, its complete A.15.1/F.6 basis keeps every actual performer System, the covering assignment occurrence and attribution for each performer, the enacted Method, temporal extent, and containing System recoverable. A short B.1.3 projection may omit an assignment identifier that its receiver does not use; the assignment occurrence and F.6 relation do not become optional. An operation result binding says which value the application returned; it establishes neither production nor first existence of that value, publication, release, acceptance, nor a carrier. Open A.15.PROD or the publication patterns only when one of those separate questions is current.

**Synthesis (design-time semantic fold).** Compose exact input epistemes into a draft aggregate.

```
Γ_epist^synth : ( D_know : DependencyGraph< U.Episteme > ) → U.Episteme
```

* **Domain.** `D_know` designates exact source epistemes and their governed **ConstituentOf**, **UsageOf/ReferenceTo**, **evidences/derivesFrom**, and optional **MemberOf** relations, together with the mappings used by the fold. The graph represents those objects and relations; it does not make them obtain.
* **Result.** One synthesized episteme whose claim content, exact EntityOfConcern, and effective reference scheme satisfy C.2.1. Its ClaimGraph integrates the retained conceptual and symbolic content; its provenance and SCR keep every contributing source and carrier traceable; and its provisional F/G/R values use the declared CL inputs. **Gating:** at **M-mode** only tuple placeholders are required; numeric scoring may be omitted (`[M-0/M-1]`). At **F-mode** the tuple **MUST** be computable under the result's effective reference scheme (`[F-*,L1+]`). # [M/F]

**Compilation (target-scheme fold).** Map one synthesized episteme into one exact target reference scheme.

```
Γ_epist^compile : ( E_synth    : U.Episteme,
                    TargetScheme : U.ReferenceScheme ) → U.Episteme
```

* **Domain.** One synthesized episteme and the exact target reference scheme used to read the compiled claims—for example, the scheme used by a journal, standard, or program specification. For every meaning that crosses semantic contexts, the fold also relies on exact source and receiving `SchemeSenseCell` values, an obtaining F.9 Bridge, and a separately stated bounded-use claim; any relied-on use must pass A.10 or B.3.
* **Result.** One compiled, target-scheme episteme with explicit mapping and loss information and a C.2.1 identity determined by its claim content, exact EntityOfConcern, and effective reference scheme. The result is not thereby a publication, release, carrier, or accepted artifact.

**Relationship to Γ_ctx / Γ_time.**
If the knowledge fold explicitly depends on **argument order** (for example, a derivation), the internal fold uses **Γ_ctx** for the sequence. If a **temporal storyline** matters, first identify each exact episteme and any obtaining C.2.1 edition relation; then use B.1.4/**Γ_time** to aggregate only the recovered temporal restrictions, relation order, or applicability windows required by the use. Γ_epist composes exact selected episteme inputs, not a label-defined current slice. If the result changes claim content, EntityOfConcern, or effective reference scheme, C.2.1 identifies another episteme. Use B.2 only when exact construction facts leave a separate existing-whole versus candidate-new-whole question.

#### B.1.3:4.3 - Invariant Standard (how the Quintet applies; **math by level**)

* **IDEM (Idempotence).** Folding a single episteme returns itself; no accidental “upgrade.”
* **COMM/LOC (Local commutativity / locality).** For **independent** subgraphs (no logical/evidential dependency), fold order/location is irrelevant; when dependencies exist, **Γ\_ctx** controls order explicitly.
* **WLNK (Weakest‑link bound).** Aggregate **Reliability (R)** is bounded by the **weakest supported link** along any justification path, **after** considering the **lowest CL** on mappings used by that path.
* **MONO (Monotonicity).** Strengthening a part (raising **R** with valid evidence or raising **CL** on a needed mapping) cannot lower aggregate **R**. Adding **contradictory** evidence is **not** an improvement; it triggers conflict handling (below), not MONO.

**Reliability fold.** Along any support spine, **R\_raw = min\_i R\_i**; apply congruence penalty Φ(CL\_min) → **R\_eff = max(0, R\_raw − Φ(CL\_min))**. *No averaging; weakest-link.*
**Math by level:**
- `[M‑0/M‑1]` allow **ordinal** comparisons only (no arithmetic on R); Φ may be stated qualitatively (“low/med/high”).
- `[M‑2/L1]` require a numeric Φ table (default in §4.4) and a reproducibility tag on empirical edges.
- `[F‑*,L1/L2]` require formal derivability of the fold rules from LOG‑CAL; constructive mode annotates `proof.kind=constructive`. # [M/F]

#### B.1.3:4.4 - Core rules for epistemic aggregation (design‑time synthesis)

When computing **Γ_epist^synth(D_know)**:

**1. Provenance preservation.**
   The **provenance/evidence graph** is **unioned with de‑duplication**; every claim in the aggregate remains traceable to its sources and methods. No source, method, or dataset that supports a retained claim may be dropped.

**2. SCR construction.**
   Build a **U.SCR** that lists all symbol carriers (texts, code, figures, datasets) that materially participate in the aggregate. Provenance nodes must be mappable to SCR entries.

**3. Object alignment.**
   Identify the result's one exact **EntityOfConcern**. Reuse the same already identified entity when the inputs concern it. A governed least common ancestor in a domain taxonomy may support that identification, but the calculation does not create the entity. If the claim requires a collection, relation occurrence, or other joint subject, identify that entity under its direct pattern and show that its identity rule obtains. A list, dependency graph, shared label, or mapping cannot create a joint subject; if none is governed, stop with the missing composition governor instead of inventing a generic composite entity. Record the semantic mappings and their **CL** evidence summaries without silently merging homonyms.

**4. Concept integration with CL penalty.**
   Compute provisional **F/G/R** of the aggregate:

   * **F\_eff** = min(F\_i) (formality is as strong as the least formal constituent actually used).
   * **G\_eff** = function of coverage; typically **monotone** in included scope, capped by weakest definitional fit.
   * **R\_eff** = min over justification paths of { R\_i along the path } **penalized** by the lowest **CL** used by that path: `R_eff := max(0, min_path( min_claimR(path) − Φ(CL_min(path)) ))`, where **Φ** is the normative penalty function defined below.
      If a mapping with **CL < threshold** is essential to a path, mark the claim **provisional**.
**5. Normative Penalty Function Φ (v1.0).**
The penalty function `Φ` quantifies the loss of reliability due to poor conceptual alignment between parts.

| Congruence Level `CL_min` | 0 | 1 | 2 | 3 |
| :--- | :--- | :--- | :--- | :--- |
| **Penalty Φ(CL_min)** | 1.5 | 1.0 | 0.5 | 0.0 |

*A domain profile **MAY** provide an alternative table but **MUST** preserve monotonic decrease (a lower `CL` cannot have a smaller penalty). The default values are derived from empirical fits in KD-CAL Bench 0.3.*

**6. Conflict detection (no averaging).**
    Detect contradictions (for example, `p` and `¬p` with overlapping scope). Do **not** average. Either (i) separate them by exact claim scope or interpretation basis, (ii) mark the affected claim **provisional** with explicit conflict edges, or (iii) if exact construction facts leave a whole-reidentification question after the existing-whole explanation check, open B.2 for that separate question.

**7. Handling of Axiomatic vs. Postulative Epistemes.**
   In alignment with ADR-028, the computation of `R_eff` depends on the episteme's declared `mode`.

*   For an input episteme `E_i` with **`mode: axiomatic`**, empirical `R` is N/A; take `R_i_eff = F_i`. **Tag:** `line=formal`.  # `[F‑*]`
*   For **`mode: postulative`**, use declared `R_i` with decay; **Tag:** `line=empirical`.  # [M‑1/M‑2/F]
*   The aggregate `E_eff` **MUST** also declare a mode. If all inputs are `axiomatic`, the output is `axiomatic`. If any input is `postulative`, the output **MUST** be `postulative`.
*   **Constructive note.** Under **F‑constructive**, equivalence claims use **isomorphism/equivalence** in the chosen UF library; **CL=2** means proof‑reconstructed alignment, not mere model‑theoretic appeal.  # [F‑constructive]

**8. Order-aware arguments (optional).**
   If the argument requires premise ordering, embed a **Γ\_ctx** fold inside Γ\_epist; record the **OrderSpec** for reproducibility (NC‑1..3).
   **Gating:** OrderSpec is **recommended** at **M‑1** and **required** at **M‑2/F**.  # [M‑1→F]

**9. No costs here.**
   Any compute/collection effort is **Γ\_work**; attach references but do not mix costs into epistemic aggregation.

#### B.1.3:4.5 - Core rules for target-scheme compilation

When computing **Γ_epist^compile(E_synth, TargetScheme)**:

**1. Reference-scheme bindings.** # [M-1+]
   Map every operative concept, unit, and claim into **TargetScheme** and record the exact mapping and its **CL** evidence summary. For a meaning that crosses semantic contexts, name the source and receiving `SchemeSenseCell` values, the obtaining F.9 Bridge, the proposed use, direction, use-specific rule, and permitted loss; establish reliance separately. C.2.1 identifies the compiled episteme from its resulting claims, exact EntityOfConcern, and target scheme. A changed identity discriminator identifies another episteme; it does not by itself open a whole-reidentification question.

**2. Assurance baseline (gated).**
   Recalculate the **assurance tuple** (B.3) under **TargetScheme**: F and R may change with formalization, mapping evidence, and loss; G is re-expressed in the target scheme's scope.
   **Gating:**
* **\[M‑0]** narrative justification only;
* **\[M‑1]** qualitative tuples allowed;
* **\[M‑2/L1]** numeric tuple required;
* `[F‑*/L2]` tuple **and** proof obligations on weight/penalty model selection.  # [M/F]

**3. Compilation trace.**
   Produce the compiled episteme's SCR and the carrier hashes needed to reconstruct this application; at **L2** require independent re-hash verification. This trace establishes neither publication nor release. # [M-1/L2]
**4. Order/time hooks.**
   If the compiled episteme includes an internal derivation, carry the **OrderSpec**. If it selects knowledge for a time-bounded use, name the exact C.2.1 episteme identity and link to the already recovered proper temporal restriction, edition relation order, applicability window, or B.1.4/**Γ_time** aggregation actually used.

### B.1.3:5 - Archetypal grounding (worked, didactic)

#### B.1.3:5.1 - Episteme — **Meta‑analysis into a guidance statement**

* **Inputs (U.Episteme):**
  `E₁` randomized trial (R=0.84, F=3, G=medium), `E₂` observational study (R=0.55, F=2, G=wide), `E₃` mechanistic model (R=0.60, F=3, G=narrow).
  Mappings: dosage units (mg ↔ IU), outcome definitions (pain scale variants), each with declared **CL** (e.g., unit mapping CL=3, outcome alignment CL=2).

* **Γ\_epist^synth:**

  * **Provenance preservation:** all study protocols, datasets, analysis scripts listed in the **SCR**.
  * **Object alignment:** “acute low‑back pain within 6 weeks” via taxonomy LCA; non‑aligned chronic cohorts excluded or mapped with low CL and flagged.
  * **Concept integration:** compute provisional `R_eff` along each justification path, penalized by **Φ(CL_min(path))**; aggregate `R_eff` as the minimum over paths.
  * **Conflict handling:** `E₂` contradicts `E₁` in a subgroup; kept as **provisional** with explicit conflict edge and scope note (different baseline severity).

* **Γ_epist^compile (target journal scheme):**
  Map outcomes to the journal's required scheme through the exact sense mappings used by the fold, recalculate F/G/R with mapping penalties, and produce the compilation SCR and hashes. The result is the target-scheme episteme "Guidance Statement v1.0" with conservative `R`; any later journal publication is a separate publication occurrence.


* **Why not averaging?**
  Averaging would inflate `R` and hide low‑CL outcome mappings; Γ\_epist enforces pathwise **min** + **CL** penalty.

#### B.1.3:5.2 - Episteme — **Safety case from heterogeneous evidence**

* **Inputs:** requirement spec (F=3, R=0.7), hazard analysis (F=2, R=0.6), test logs (F=1, R=0.8), formal proof of controller property (F=3, R=0.9).

* **Γ\_epist^synth:**

  * Provenance union; **SCR** includes requirements, proof carrier, test datasets.
  * Concept integration: controller proof applies only under assumptions A; test logs violate A in edge case → **CL** low for mapping “test scenario ≡ proof assumption.”
  * `R_eff` bounded by the weakest justification path after **Φ(CL\_min)**; claim on “system‑level safety” marked **provisional** until assumption alignment is demonstrated.

* **Γ_epist^compile (target certification scheme):**
  Map the claims to the regulatory vocabulary. Where local meanings differ, identify exact source and receiving `SchemeSenseCell` values, test the F.9 Bridge, state the bounded certification use and permitted loss, and establish any relied-on use separately. C.2.1 identifies the resulting target-scheme episteme; a certification publication occurrence or acceptance verdict remains separate.

#### B.1.3:5.3 - Contrast (didactic)

| Aspect          | **Γ\_epist (Knowledge)**                                         | **Γ\_sys (Physical)**                       |
| --------------- | ---------------------------------------------------------------- | -------------------------------------------- |
| What is folded? | Claims, models, datasets, arguments                              | Components, materials, assemblies            |
| Conservatism    | **Pathwise min** of R + penalty **Φ(CL)**                        | WLNK via **weakest part** (strength, rating) |
| Fit             | **Mappings** with declared **CL**                                | **Interfaces/BIC** compatibility             |
| Order/time | Optional **Γ\_ctx** for argument order; C.2.1 for distinct episteme identities and edition relations; A.14 for a proper restriction of one unchanged episteme; B.1.4/**Γ\_time** for bounded aggregation of recovered temporal relations | Γ\_ctx for workflows; Γ\_time for phases of directly governed enduring carriers |
| Work/cost       | External in **Γ\_work** (compute, curation)                      | External in **Γ\_work** (energy, labour)     |

### B.1.3:6 - Proof obligations (normative)

**At synthesis (Γ\_epist^synth):**

1. **PO‑SYN‑PROV.** The **provenance/evidence graph** MUST be preserved (union with de‑duplication); every retained claim is traceable to sources/methods in the **SCR**.
2. **PO-SYN-OBJ.** The result **MUST** name one exact EntityOfConcern already identified under its direct pattern. If the synthesis depends on several inputs as a joint subject, its collection, relation, or whole identity **MUST** be independently governed; a list, graph, label, or mapping is insufficient. Every semantic mapping used by the fold **MUST** be declared with its **CL** evidence summary.
3. **PO-SYN-CL.** Every semantic mapping used by the reliability fold **MUST** have a **CL** evidence summary; the chosen penalty **Φ** **MUST** decrease monotonically as CL rises. Thresholds for marking a claim **provisional** **MUST** be stated. The summary neither establishes an F.9 Bridge nor grants the mapped use.
4. **PO‑SYN‑R.** `R_eff` MUST be computed as **min over justification paths** of (claim reliabilities along the path **minus** `Φ(CL_min(path))`). No arithmetic mean is allowed for reliability.
5. **PO-SYN-CONFLICT.** Contradictions **MUST** be separated by exact claim scope or interpretation basis, marked **provisional** with explicit conflict edges, or—only when exact construction facts leave a separate whole-reidentification question—sent to B.2.
6. **PO‑SYN‑ORDER.** If order matters, the **OrderSpec** MUST be recorded and Γ\_ctx **NC‑1..3** (determinism, context hash, partial‑order soundness) MUST hold.
7. **PO‑SYN‑NOWORK.** Resource spending, yields, and dissipation MUST NOT be computed here; instead, attach references to the aligned **Γ\_work** composition.

**At compilation (Γ\_epist^compile):**

1. **PO-COMP-SCHEME.** The exact target reference scheme **MUST** be declared. Every active concept and unit **MUST** have an explicit mapping; a cross-context meaning use **MUST** name the exact F.9 Bridge, separate bounded-use claim, permitted loss, and any relied-on A.10 or B.3 result.
2. **PO-COMP-ASSUR.** The assurance tuple (F/G/R) **MUST** be recomputed under the target scheme with the applied mapping and loss penalties.
3. **PO-COMP-SCR.** The compiled episteme **MUST** retain an SCR with the hashes, versions, and dates required to reconstruct the application. This obligation does not assert release or publication.
4. **PO-COMP-ID.** The output **MUST** be identified through its C.2.1 claim content, exact EntityOfConcern, and effective target scheme. A changed discriminator identifies another episteme. B.2 is opened only for an independently current existing-whole versus candidate-new-whole question, never as a substitute for this identity rule.
5. **PO‑COMP‑ORDER/TIME.** If derivational order is essential, the **OrderSpec** MUST be referenced. If temporal selection is essential, name the exact C.2.1 episteme identity and reference the already recovered proper restriction, edition-relation order, applicability window, and B.1.4/**Γ\_time** aggregation actually consumed.

### B.1.3:7 - Conformance Checklist (normative)

| ID            | Requirement                                                                                                                                                         | Purpose                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **CC‑B1.3.1** | Inputs to Γ\_epist MUST be `U.Episteme` holons; **ComponentOf** is forbidden; use **ConstituentOf / UsageOf / ReferenceTo**; **MemberOf** only for **collections**. | Prevent category errors.       |
| **CC‑B1.3.2** | Provenance and **SCR** MUST be preserved in the aggregate; dropping sources or methods is non‑conformant.                                                      | Enforce Evidence Graph Referring.    |
| **CC‑B1.3.3** | Aggregate **R** MUST follow the **pathwise min** rule with **Φ(CL\_min)** penalties; no averaging of reliability.                                                   | Guard conservatism (WLNK).     |
| **CC-B1.3.4** | Contradictions MUST NOT be smoothed by arithmetic; handle them by exact scope or interpretation-basis separation, **provisional** status, or B.2 only for a separately grounded whole-reidentification question. | Keep incoherence visible. |
| **CC‑B1.3.5** | Every `U.Episteme` serving as an input to `Γ_epist` **MUST** declare its `mode` (`axiomatic` or `postulative`). An aggregate holon's mode **MUST** be `postulative` if any of its constituents is `postulative`. | Prevent category errors in reliability calculation. |
| **CC-B1.3.6** | A cross-context meaning use names explicit mappings, exact source and receiving F.17 cells, an obtaining F.9 Bridge, a separate bounded-use claim and permitted loss, and any reliance result the fold consumes. **CL** alone never grants the use. | Make semantic crossing inspectable. |
| **CC‑B1.3.7** | If order matters, Γ\_ctx **NC‑1..3** MUST hold. If an episteme history matters, exact C.2.1 endpoint identities and any obtaining `EpistemeEditionRelation` MUST be named; any proper restriction or B.1.4/**Γ\_time** aggregation MUST cite only already recovered temporal relations. | Preserve order, identity, continuity, and temporal integrity. |
| **CC-B1.3.8** | Keep design-time synthesis, target-scheme compilation, one actual operation application and its returned value, dated Work, performer and any relied-on assignment, production or first existence, publication, carrier, release, and acceptance separately governed. | Preserve semantic and practical boundaries. |

### B.1.3:8 - Anti‑patterns & repairs

| Anti‑pattern             | Symptom                                           | Repair                                                                                     |
| ------------------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Truth‑averaging**      | Averaging confidence of conflicting claims        | Apply **pathwise min** with **CL** penalties; separate scopes or mark **provisional**.     |
| **Provenance amnesia**   | Sources/methods disappear in the aggregate        | Rebuild **SCR**; re‑run Γ\_epist with provenance union.                               |
| **Homonym merge** | Different concepts with the same name are silently merged | Declare the exact mapping. For cross-context meanings, identify and test the F.9 Bridge, state the bounded use and permitted loss, and keep low-CL or unresolved uses separate or **provisional**. |
| **Silent semantic crossing** | Local senses or schemes are mixed without a tested correspondence and use boundary | Declare the exact mappings; for cross-context meanings identify the F.9 Bridge, separate bounded-use claim, permitted loss, and any relied-on A.10 or B.3 result. |
| **Version soup** | Labels or time slices mix unchanged epistemes, distinct epistemes, edition continuity, publication, and Work history | Apply the C.2.1 identity triple first; test `EpistemeEditionRelation` separately; use A.14 only for a proper restriction of one unchanged episteme and A.15.1 for Work. Then aggregate only the exact recovered temporal relations the current use needs. |
| **Work stuffing**        | Compute/curation cost blended into reliability    | Move costs to **Γ\_work**; keep R based on evidence, not spend.                            |
| **Orderless proof**      | Derivation steps treated as a set                 | Add **OrderSpec**; compose with Γ\_ctx inside Γ\_epist.                                    |
| **Synergy by narrative** | A new theory or whole is claimed from explanatory gain alone | First identify the synthesized episteme through C.2.1. Open B.2 only if exact construction and identity facts leave an existing-whole versus candidate-new-whole question. |

### B.1.3:9 - Consequences

**Benefits**

* **Auditability by construction.** Every retained claim remains tied to its sources; **SCR** guarantees reconstructability.
* **Safe synthesis.** **R** cannot be inflated; **CL penalties** make conceptual misfit explicit.
* **Target-scheme results.** Compiled epistemes are aligned with one declared reference scheme; any release or publication remains separately governed.
* **Didactic clarity.** Separates **semantic folding** (Γ\_epist) from **order** (Γ\_ctx), **time** (Γ\_time), **spend** (Γ\_work), and **emergence** (B.2).

**Trade‑offs**

* **Mapping overhead.** Declaring mappings and **CL** costs time; it prevents silent incoherence.
* **Conservative stance.** Results may look pessimistic; this is deliberate (WLNK). Use B.2 only when exact construction and identity facts leave a genuine whole-reidentification question.

### B.1.3:10 - Rationale (informative)

* **Epistemic composition is not physical addition.** Reliability must be bounded by the **weakest justified path**, not averaged; conceptual misalignment must **reduce** confidence, not be ignored.
* **Provenance is part of meaning.** Dropping sources/methods changes what the episteme **is**; Γ\_epist treats provenance and **SCR** as first‑class.
* **Interpretation matters.** Exact reference schemes and local senses prevent quiet reinterpretation. F.9 governs any cross-context Bridge; C.2.1 governs the resulting episteme identity.
* **Parsimony with power.** A small set of rules (provenance preservation, CL‑penalized pathwise min, order/time hooks, context discipline) is enough to model scientific and engineering knowledge without importing domain‑specific tool jargon.

### B.1.3:11 - Relations

* **Builds on:** C.2.1 (episteme identity and independently obtaining edition relations), A.6.1 (semantic operation declarations and exact application bindings), A.14 (ConstituentOf, MemberOf, and proper temporal restriction of one unchanged carrier), and A.15/A.15.1 (Strict Distinction and Work-temporal law). A.12 is used only when an acting-side distinction is current. An ordinary actor sentence needs no classification apparatus; any particular dated synthesis or compilation `U.Work` has the complete A.15.1/F.6 basis, even when its short local projection omits an assignment identifier unused by the receiver.
* **Coordinates with:** B.1.1 dependency-structure and relation-grounding checks, B.1.4 (Γ\_ctx/Γ\_time inside knowledge folds), B.1.6 (Γ\_work for compute/collection spend).
* **Coordinates with:** F.9 for exact cross-context Bridges and bounded-use claims; A.10 or B.3 for reliance; A.15.PROD when production, first existence, or completion is current; and E.17/E.24.PUB for publication, form, and carrier. B.2 is used only when exact construction facts leave a separate whole-reidentification question after the existing-whole explanation check.
* **Used by:** B.3 assurance uses `F/G/R` and **CL** baselines computed here as inputs to trust calculations.

> **One‑sentence takeaway.**
> **Γ\_epist** preserves provenance, penalizes poor conceptual fit, forbids reliability averaging, and makes context explicit—so that knowledge aggregates are conservative, auditable, and genuinely coherent.

### B.1.3:End

