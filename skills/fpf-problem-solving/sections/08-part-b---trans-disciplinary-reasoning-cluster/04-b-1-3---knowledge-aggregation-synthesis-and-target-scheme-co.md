## B.1.3 - Knowledge Aggregation (Γ_epist): Synthesis and Target-Scheme Compilation

**At a glance.** Use B.1.3 to compose exact `U.Episteme` inputs into one knowledge aggregate while preserving provenance, conceptual fit, context, and the warrant each source actually contributes.

**Use this when.** Use this pattern when a named synthesis or compilation use depends on how claims, models, datasets, or arguments are combined, and the aggregation must keep source, mapping, conflict, order, and temporal qualifications inspectable.

**Not this pattern when.** Use C.2.1 for episteme identity and edition continuity, A.14 for a proper temporal restriction of one unchanged episteme, A.15.1 for Work parts or occurrences, B.1.4 for a bounded aggregation of already recovered order or temporal relations, and B.3 for the assurance claim that consumes the aggregate.

**What changes in practice.** Identify the target claim, each input's support role and dependencies before combining them. Return a justified calculation or a reasoned synthesis with its limitations; preserve provenance and conflicts. Return identity, edition, temporal restriction, Work, publication, and assurance questions to their subject patterns.

> **► decided‑by: A.14 Advanced Mereology**
**A.14/C.2.1 compliance —** Use **ConstituentOf** for semantic parts and **PortionOf** only for quantitative splits of texts/data with declared μ. Use `PhaseOf` only for a proper interval of one unchanged C.2.1 episteme. When a MethodDescription or document episteme's claim content, EntityOfConcern, or effective ReferenceScheme changes, identify another episteme and assert `EpistemeEditionRelation` only when its historical-continuation predicate obtains. Work segmentation uses A.15.1; no **ComponentOf** is used here.

> **Plain‑English headline.**
> **Γ\_epist** composes **epistemic holons** (claims, models, datasets, arguments) into a **single episteme** while preserving **provenance** and distinguishing the support, limitations, and conceptual mappings on which its conclusion depends. B.3 governs the meaning and model of any assurance calculation. This is a **semantic and evidential composition**, not a physical sum or a universal confidence fold.

### B.1.3:1 - Problem frame

* **Holonic foundation.** In the FPF, a `U.Episteme` is a holon whose identity is **knowledge-bearing** (A.1). It can be a **statement/claim**, a **model**, a **theory**, a **specification**, a **dataset with semantics**, or a **compiled claim-bearing synthesis**.
* **Strict Distinction (A.7).** We separate:
  **structure** (what the episteme comprises), **order** (argument flow), **identity and history** (C.2.1 identities and edition relations), **proper temporal restriction** (A.14), **work** (what was spent to produce/validate it), and **values** (objectives/criteria). Γ\_epist stays in the **structure/semantics** lane and calls out to Γ\_ctx/Γ\_time/Γ\_work only after their direct inputs are recovered.
* **Mereology (A.14).** For knowledge composition we primarily use **ConstituentOf** (logical or semantic parts), **UsageOf** or **ReferenceTo** (external reliance), and each collection's own belongs-to rule for collections such as anthologies or corpora. We do **not** use **ComponentOf** (physical) in Γ\_epist.
  `PhaseOf` may restrict the **same unchanged episteme** to a proper interval when its complete C.2.1 identity triple remains fixed. Distinct labelled versions or revisions require distinct C.2.1 identities when a discriminator changes and an independently obtaining `EpistemeEditionRelation` for any claimed historical continuation. Knowledge does not act and acquires neither a work-facing local system-role kind nor an assignment. Ordinary prose may say, for example, "the researcher synthesized the sources". If the receiving use does not identify that action as one particular dated `U.Work` occurrence, stop with the ordinary sentence. If it does, recover each actual performer's A.13 core and independently admit the occurrence under A.15.1. Add F.6 only when the receiving use also needs precise assignment-bound attribution; a short local projection may omit an unused assignment identifier only when every consumed relation remains recoverable.
* **Assurance (B.3).** Keep **F** (Formality), **G** (ClaimScope), and **R** (Reliability) distinct. Identify the meaning, scale, and receiving use of each value before calculating with it. A mapping's **CL** summarizes one relation's fit; its ordinal rank is not a numerical loss of reliability. Preserve provenance and make any unsupported inference or semantic crossing visible. Formality or mode does not supply a missing warrant model.
* **Order/time flavours.** Argument sequences may need **Γ_ctx** (non-commutative ordering of premises to conclusion). Knowledge evolution first uses C.2.1 to identify exact epistemes and any obtaining edition relations; B.1.4/**Γ_time** may then aggregate already recovered temporal restrictions, relation order, deprecation, or update windows for a bounded use. The aggregation creates neither identity nor continuity. Open B.2 only if the synthesis leaves a genuine whole-reidentification question after the existing-whole explanation check and identifies an exact candidate new whole; new wording or explanatory gain alone is not MHT.

### B.1.3:2 - Problem

Naive aggregation of knowledge holons causes recurring failures:

1. **Unsupported confidence folds.** Averaging incomparable scores can hide conflict; a compulsory minimum can discard useful complementary support or overstate the probability of several necessary conditions. Both violate B.3 when their inputs and dependency model are unjustified.
2. **Provenance erasure.** Merges that drop sources, methods, or links break **A.10 Evidence Graph Referring** and make results unauditable.
3. **Semantic drift.** Folding across mismatched concepts without explicit **mappings** (and their **CL**) yields incoherent composites that look formal but mean nothing.
4. **Order blindness.** Arguments with essential **dependency order** (premise ⇒ lemma ⇒ conclusion) are treated as sets; non‑commutativity is lost and results become non‑reproducible.
5. **Semantic-context chimeras.** Combining claims whose local senses or reference schemes differ, without exact mappings and—when meanings cross—an F.9 Bridge plus a separately warranted bounded-use claim, silently corrupts claims and inflates **R**.
6. **Category errors.** Importing **Γ\_sys** rules (e.g., “sum truth,” “avg formality”) into knowledge composition produces physically sounding but epistemically nonsensical models.

### B.1.3:3 - Forces

| Force                                      | Tension                                                                                                                      |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| **Conservatism vs. Synthesis** | Refuse unsupported assurance gains ↔ retain the real contribution of complementary and alternative support. |
| **Universality vs. Domain nuance**         | One operator across math, science, engineering specs ↔ domain‑specific semantics and evidence patterns differ.               |
| **Provenance fidelity vs. Cognitive load** | Keep the **full trail** of sources and methods ↔ avoid overwhelming authors with bookkeeping.                                |
| **Order/time discipline vs. Flow** | Respect argument **order**, exact episteme identity and edition relations, and any proper temporal restriction ↔ keep composition usable for day-to-day synthesis. |
| **Parsimony vs. Fit** | Small rule set (A.11) ↔ explicit mappings, use-specific limitations, and justified loss models where needed. |

### B.1.3:4 - Solution — **Terms, operator family, invariant Standard, core rules**

#### B.1.3:4.1 - Terms (didactic recap)

* **U.Episteme** — a claim-bearing knowledge holon. C.2.1 identifies it through the participant-determined `EpistemeConstitutionRelation` over `<claim content, exact EntityOfConcern, effective ReferenceScheme>`. `ClaimGraphSlot`, `EntityOfConcernSlot`, and `ReferenceSchemeSlot` name participant meanings only inside that relation's reusable declaration; they are not internal slots of the episteme. Empirical grounding uses the separate `EpistemeEmpiricalGroundingRelation`, while text, code, figures, datasets, SCR/RSCR references, publication forms, and presentation carriers remain separately governed provenance, representation, publication, or carrier material.
* **Evidence/Provenance Graph** — an A.10 descriptive account whose edges cite independently established direct support, source, measurement or use relations. Display labels such as `evidences` do not create generic relation kinds.
* **Semantic mapping** — the exact correspondence rule used by this composition. When it crosses semantic contexts, identify the source and receiving F.17 `SchemeSenseCell` values and an obtaining F.9 `Bridge`; keep the proposed use, direction, use-specific rule, permitted loss, reliance, and **CL** evidence summary separate. F.9 does not require CL for every Bridge; B.1.3 requires the summary for a mapping used in its support account. CL alone neither grants the use nor supplies a numerical penalty.
* **SCR** — a `U.SCR` that lists all symbol carriers included in the aggregate; **never dropped**.
* **Semantic context** — Plain shorthand for the local interpretation basis recovered from one exact F.17 `SchemeSenseCell` as `<ReferenceScheme, LocalSenseClaim>`. It is not another operation argument or entity. Crossing between two such contexts uses F.9 and the separate bounded-use and reliance steps above.

> **Didactic reminders.**
> • Knowledge does **not** act. A researcher or engineer may use it while performing Work. Recover the exact System and Work only when the receiving claim consumes them; use A.12 only when the acting-side distinction is itself current.
> • A collection's own rule establishes which epistemes belong to it; belonging is not a semantic argument link and does not by itself make a holon. Use **ConstituentOf** for logical or evidential composition.
> • `PhaseOf` is only a proper temporal restriction of one unchanged episteme. Changed C.2.1 discriminators identify another episteme; test `EpistemeEditionRelation` separately. Use MHT only for a remaining whole-reidentification question, not as a substitute for C.2.1 identity.

#### B.1.3:4.2 - The operator family (companion flavours)

To keep **design vs run** clean (A.15), Γ_epist has two companion flavours that share the same algebra but answer different semantic questions. Their declarations contain only the values on which the result depends. A performer, local system-role kind, or assignment is therefore not an operator argument: the same fold can be specified before staffing and can be applied in Work performed by different Systems without changing its result semantics.

When one particular operation application matters, use A.6.1 for that application and its argument and result bindings. A practitioner sentence may still say "the engineer compiled the guidance". If no particular dated `U.Work` claim is current, that ordinary sentence needs no classification or assignment apparatus. If one is current, recover every actual performer System's A.13 core and independently admit the Work under A.15.1 from its performance history, enacted Method, temporal extent, and containing System. Add F.6 afterward only when precise assignment-bound attribution is current. A short B.1.3 projection may omit an assignment identifier unused by its receiver only when every relation it consumes remains recoverable. An operation result binding says which value the application returned; it establishes neither production nor first existence of that value, publication, release, acceptance, nor a carrier. Open A.15.PROD or the publication patterns only when one of those separate questions is current.

**Synthesis (design-time semantic fold).** Compose exact input epistemes into a draft aggregate.

```
Γ_epist^synth : ( D_know : DependencyGraph< U.Episteme > ) → U.Episteme
```

* **Domain.** `D_know` designates exact source epistemes and the governed **ConstituentOf**, **UsageOf**, **ReferenceTo**, **evidences**, **derivesFrom**, and collection-specific belongs-to relations that obtain among them, together with the mappings used by the fold. The graph represents those objects and relations; it does not make them obtain.
* **Result.** One synthesized episteme whose claim content, exact EntityOfConcern, and effective reference scheme satisfy C.2.1. Its ClaimGraph integrates the retained content; provenance and SCR keep contributing sources and carriers traceable. State its formal basis, scope, and supported conclusion with limitations. Calculate an aggregate R only where B.3 and C.2.2 establish the input meanings, scales, and dependency model. Otherwise keep support separate and return a bounded reasoned synthesis. Neither a higher formality level nor an axiomatic mode requires an invented numerical score or an irrelevant empirical study.

**Compilation (target-scheme fold).** Map one synthesized episteme into one exact target reference scheme.

```
Γ_epist^compile : ( E_synth    : U.Episteme,
                    TargetScheme : U.ReferenceScheme ) → U.Episteme
```

* **Domain.** One synthesized episteme and the exact target reference scheme used to read the compiled claims—for example, the scheme used by a journal, standard, or program specification. For every meaning that crosses semantic contexts, the fold also relies on exact source and receiving `SchemeSenseCell` values, an obtaining F.9 Bridge, and a separately stated bounded-use claim; any relied-on use must pass A.10 or B.3.
* **Result.** One compiled, target-scheme episteme with explicit mapping and loss information and a C.2.1 identity determined by its claim content, exact EntityOfConcern, and effective reference scheme. The result is not thereby a publication, release, carrier, or accepted artifact.

**Relationship to Γ_ctx / Γ_time.**
If the knowledge fold explicitly depends on **argument order** (for example, a derivation), the internal fold uses **Γ_ctx** for the sequence. If a **temporal storyline** matters, first identify each exact episteme and any obtaining C.2.1 edition relation; then use B.1.4/**Γ_time** to aggregate only the recovered temporal restrictions, relation order, or applicability windows required by the use. Γ_epist composes exact selected episteme inputs, not a label-defined current slice. If the result changes claim content, EntityOfConcern, or effective reference scheme, C.2.1 identifies another episteme. Use B.2 only when exact construction facts leave a separate existing-whole versus candidate-new-whole question.

#### B.1.3:4.3 - Invariant Standard (how the Quintet applies)

* **IDEM (singleton identity and source-repetition discipline).** Folding a single episteme without a change of claim or scheme returns itself. Repeating the same source or data creates no additional evidence or accidental assurance upgrade.
* **COMM/LOC (Local commutativity / locality).** Reordering genuinely independent contributions does not change a result under its declared model. A derivation or other order-dependent argument uses **Γ_ctx**; source order does not establish statistical independence.
* **WLNK (Weakest-link bound).** An unsupported indispensable premise limits the conclusion that needs it. A numerical minimum is appropriate only when the named quantity and dependency model justify a bottleneck or lower-bound interpretation. WLNK does not impose minimum over every cited source or every argument.
* **MONO (Monotonicity).** A monotonicity claim names the support change and the model under which it holds. Duplicate data, a contrary result, a changed target population, or the failure of a necessary assumption is not simply “more support”.

**No universal reliability fold.** B.3 governs the quantity, scale, dependency assumptions, and calculation. For two necessary independent conditions with probabilities 0.9 each, the conjunction has probability 0.81, not 0.9. Without independence, use a warranted conditional model or leave that joint probability unresolved. A minimum or maximum can be useful under its own declared meaning; monotonicity and boundedness alone do not establish that meaning.

**Formality and calculation.** Ordinal comparisons remain ordinal. A quantitative calculation requires commensurate inputs and a model for the proposed operation, including any mapping loss; a table of numbers alone is insufficient. Formal derivations state their logic and assumptions, and constructive derivations their proof basis. When no common aggregate is justified, a qualitative synthesis can still give a complete, useful answer to a bounded question.

#### B.1.3:4.4 - Core rules for epistemic aggregation (design‑time synthesis)

When computing **Γ_epist^synth(D_know)**:

**1. Provenance preservation.**
   The **provenance/evidence graph** is **unioned with de‑duplication**; every claim in the aggregate remains traceable to its sources and methods. No source, method, or dataset that supports a retained claim may be dropped.

**2. SCR construction.**
   Build a **U.SCR** that lists all symbol carriers (texts, code, figures, datasets) that materially participate in the aggregate. Provenance nodes must be mappable to SCR entries.

**3. Object alignment.**
   Identify the result's one exact **EntityOfConcern**. Reuse the same already identified entity when the inputs concern it. A governed least common ancestor in a domain taxonomy may support that identification, but the calculation does not create the entity. If the claim requires a collection, relation occurrence, or other joint subject, identify that entity under its direct pattern and show that its identity rule obtains. A list, dependency graph, shared label, or mapping cannot create a joint subject; if none is governed, stop with the missing composition governor instead of inventing a generic composite entity. Record the semantic mappings and their **CL** evidence summaries without silently merging homonyms.

**4. Recover the support relation before combining.**
   For the exact claim and scope, distinguish:

   * **Indispensable premises:** the conclusion requires each named premise. A missing or defeated premise blocks that inference, not every narrower conclusion.
   * **Alternative sufficient arguments:** each actually sufficient argument can support the conclusion; expose shared premises, datasets, assumptions, and failure causes. Different argument names do not prove independence.
   * **Complementary evidence:** a source may constrain a rival explanation, magnitude, uncertainty, or applicability without being a necessary premise. A limited additional study need not lower the existing support.
   * **Different scope slices:** retain their populations, outcomes, conditions, and time extents separately unless an explicit transport or combination rule supports the joint claim.
   * **Counterevidence:** retain credible results that conflict with the proposed conclusion. Weak support, absence of decisive support, an uninformative study, and evidence against a claim have different consequences.

   Deduplicate actual evidence, not just citations. Account for overlapping data and shared biases before treating agreement as additional corroboration. State what each live limitation changes in the resulting claim.

**5. Compose under the receiving model, or synthesize without a score.**
   Keep F ordinal under C.2.3; any minimum for essential formal constituents concerns that formality claim, not R. Form G through the applicable C.2.2/A.2.6 scope rules; adding a study does not by itself extend applicability. For R, name the target quantity, compatible scales, dependencies, and warranted operation under B.3/C.2.2. This can justify a bottleneck minimum, a sufficient-argument choice, a probabilistic calculation, or a statistical synthesis; none is the universal default.

   For a relied-on mapping, retain its CL summary and the actual limitation. A numerical loss function needs a receiving model that establishes its meaning, units, calibration or derivation, and assumptions. An ordinal CL rank, a monotone penalty table, or clipping to [0,1] supplies none of these. If no such calculation is justified, retain the separate support and mapping limitations in a reasoned synthesis; no penalty table or new study is required merely to return that result. A receiving assurance threshold applies only to the quantity and use for which it was justified.

**6. Conflict detection and disposition.**
   Detect contradictions, including overlapping-scope `p` and `¬p`. Resolve a scope or interpretation difference only when the source facts establish it; do not explain away a credible contrary result by an invented subgroup story. Otherwise narrow, qualify, or withhold the affected conclusion and retain explicit conflict edges. A numerical synthesis may represent disagreement only under its justified model, not conceal it. Open B.2 only if exact construction facts leave a separate whole-reidentification question after the existing-whole explanation check.

**7. Handling axiomatic and world-facing support.**
   Retain each episteme's declared mode and actual support:

* For an **axiomatic** input, empirical R may be N/A. Keep the proof, its conclusion under the stated axioms, and its formal validity; `line=formal` is a useful tag, not a conversion rule. **Do not set R to F.** An ordinal F-derived proxy describes only its declared ordinal meaning. Any value proposed for an R calculation needs a receiving model establishing meaning, scale, conversion, and assumptions; rescaling F into [0,1] is insufficient.
* For a **postulative** input, retain its actual warrant and empirical or other support as applicable. Apply a B.3.4 currentness or decay policy only to the support whose use consumes that policy; changing the mode creates neither evidence nor a conversion model.
* The aggregate declares its mode. If all its operative inputs are axiomatic, it is axiomatic; if an operative input is postulative, it is postulative. Keep any formal subclaim separately usable. A proof about a model supports a claim about a real system only with the needed model-to-world assumptions; evidence violating those assumptions remains visible.
* **Constructive derivations.** State the chosen proof basis and the correspondence needed by the conclusion. An induction proof may use its stated non-UF foundation. A UF-based equivalence claim supplies the required equivalence or isomorphism witness and the structure that the receiving theorem needs preserved. A lossy mapping cannot transport a theorem that depends on an erased distinction. If the required proof basis or correspondence is unavailable, leave that inference unresolved while retaining independently supported conclusions. A CL summary describes mapping evidence; it establishes neither equivalence nor theorem transport.

**8. Order-aware arguments (optional).**
   If the argument requires premise ordering, embed a **Γ\_ctx** fold inside Γ\_epist; record the **OrderSpec** for reproducibility (NC‑1..3).
   **Condition:** state the `OrderSpec` whenever the conclusion depends on premise or derivation order; use B.1.4 for the bounded aggregation of those recovered order relations. No unspecified maturity level determines this requirement.

**9. No costs here.**
   Any compute/collection effort is **Γ\_work**; attach references but do not mix costs into epistemic aggregation.

#### B.1.3:4.5 - Core rules for target-scheme compilation

When computing **Γ_epist^compile(E_synth, TargetScheme)**:

**1. Reference-scheme bindings.** # [M-1+]
   Map every operative concept, unit, and claim into **TargetScheme** and record the exact mapping and its **CL** evidence summary. For a meaning that crosses semantic contexts, name the source and receiving `SchemeSenseCell` values, the obtaining F.9 Bridge, the proposed use, direction, use-specific rule, and permitted loss; establish reliance separately. C.2.1 identifies the compiled episteme from its resulting claims, exact EntityOfConcern, and target scheme. A changed identity discriminator identifies another episteme; it does not by itself open a whole-reidentification question.

**2. Re-express the assurance basis.**
   Re-express F, G, and the support account in **TargetScheme**. Preserve the formal conclusion and empirical limitations separately. Recalculate R or a mapping loss only if the target use has the required meanings, scales, and model under B.3/C.2.2; a change of vocabulary or increased formality is not additional warrant. Without a justified aggregate, carry the separate support and bounded synthesis. A quantitative or formal application proves the calculations or derivations it actually claims, not a fictitious tuple imposed by its mode.

**3. Compilation trace.**
   Produce the compiled episteme's SCR and the carrier hashes needed to reconstruct this application; at **L2** require independent re-hash verification. This trace establishes neither publication nor release. # [M-1/L2]
**4. Order/time hooks.**
   If the compiled episteme includes an internal derivation, carry the **OrderSpec**. If it selects knowledge for a time-bounded use, name the exact C.2.1 episteme identity and link to the already recovered proper temporal restriction, edition relation order, applicability window, or B.1.4/**Γ_time** aggregation actually used.

### B.1.3:5 - Archetypal grounding (worked, didactic)

#### B.1.3:5.1 - Episteme — **Heterogeneous evidence into a guidance statement**

This is a didactic evidence-composition case, not a clinical recommendation. The receiving question concerns a treatment's pain outcome for an identified acute low-back-pain population within six weeks. The exact population and outcome, not a label or taxonomy operation, identify the subject.

* **Inputs:** `E₁` is a randomized trial, `E₂` an observational study, and `E₃` a mechanistic model. Retain their designs, findings, uncertainty, assumptions, and scope. A bare “R=0.84/0.55/0.60” list has no declared common quantity here and cannot support a numerical aggregate. Likewise, “medium/wide/narrow” is not a substitute for actual ClaimScope.
* **Synthesis:** retain protocols, datasets, analysis scripts, and other participating carriers in the SCR. Establish any dosage or outcome mapping from its actual measurement basis; units named mg and IU do not themselves establish a conversion. Keep chronic cohorts and different outcomes separate unless a warranted transport relation supports the receiving claim.
* **Necessary-premise case:** if the proposed inference requires an outcome mapping that is unsupported, withhold that mapped inference. Retain the trial's narrower source-scale conclusion rather than discard every source.
* **Complementary case:** a limited `E₂` may help assess a confounding explanation left open by `E₁`; `E₃` may constrain a mechanism without establishing the clinical effect size. Explain those contributions and their limits. The minimum of three unexplained scores neither captures them nor defeats the existing trial conclusion.
* **Dependence case:** if two reports reuse a cohort or share an outcome-measurement bias, do not count them as two independent confirmations. Different designs alone are insufficient to establish different biases.
* **Contrary-result case:** a credible `E₂` result conflicts with `E₁` in an overlapping subgroup. Keep the disagreement. Different baseline severity is a possible explanation only to the extent supported by the sources. Narrow or qualify the guidance claim; do not silently average the conflict away or call it an uninformative study.
* **Completion:** return the bounded guidance statement with its distinct supporting contributions, contrary result, scope, and unresolved interpretation. No common quantitative model has been supplied, so no aggregate R is returned. Whether another study is feasible and worth its total burden is a separate C.11/C.19.2 decision, not a condition for completing this synthesis.

For **Γ_epist^compile**, map the retained claims into the journal's scheme, carry the same limitations and any justified recalculation, and produce the compilation SCR and required hashes. C.2.1 identifies the target-scheme episteme “Guidance Statement v1.0”; later journal publication remains a separate occurrence.

#### B.1.3:5.2 - Episteme — **Controller proof and a real protective function**

* **Inputs:** a requirement specification, hazard analysis, test logs, and a proof of controller property P under assumptions A. Preserve each source's actual formal basis and support. No common R scale follows from four labels or formality levels.
* **Formal receiving question:** “Does A entail P in the stated model?” Retain the valid proof and its assumptions as the useful result. An empirical study is not needed to turn that result into an invented empirical R; F describes checkability, not the probability that the actual controller is safe.
* **World-facing receiving question:** “Does the installed controller deliver the protective function in these operating conditions?” Expose the reliance on A, the implementation/model correspondence, and the actual operating scope. If A is unsupported for this use, the proof alone does not establish the world-facing claim. If logs show an edge case violating A, retain that counterevidence and withhold the stronger assurance while preserving the theorem A ⇒ P.
* **Threshold case:** a receiving acceptance clause requires a justified probability of at least 0.95 for the real protective function. Substituting a high F or its rescaled value cannot meet it. A declared ordinal checkability comparison remains usable as an ordinal comparison. A numerical acceptance result requires the model and evidence that warrant that particular probability; otherwise return the narrower formal conclusion and the unresolved actual-system assurance.
* **Positive quantitative case:** if a receiving model actually establishes two necessary independent conditions, each with probability 0.9, their conjunction is 0.81. A 0.85 threshold is not met by replacing 0.81 with min(0.9, 0.9). If independence is unavailable, the joint probability needs the actual conditional model or remains unresolved; the formal proof is unchanged.

For **Γ_epist^compile**, map the retained claims to the certification scheme. Where local meanings differ, identify exact source and receiving `SchemeSenseCell` values, test the F.9 Bridge, state the bounded certification use and permitted loss, and establish relied-on use separately. C.2.1 identifies the resulting episteme. Certification, authorization, a publication occurrence, and actual system protection remain separate claims.

#### B.1.3:5.3 - Contrast (didactic)

| Aspect          | **Γ\_epist (Knowledge)**                                         | **Γ\_sys (Physical)**                       |
| --------------- | ---------------------------------------------------------------- | -------------------------------------------- |
| What is folded? | Claims, models, datasets, arguments                              | Components, materials, assemblies            |
| Conservatism | Support roles, dependence, and mapping limits under the named B.3 model; no invented aggregate | WLNK for a quantity whose physical model justifies a weakest-part bound |
| Fit             | **Mappings** with declared **CL**                                | **Interfaces/BIC** compatibility             |
| Order/time | Optional **Γ\_ctx** for argument order; C.2.1 for distinct episteme identities and edition relations; A.14 for a proper restriction of one unchanged episteme; B.1.4/**Γ\_time** for bounded aggregation of recovered temporal relations | Γ\_ctx for workflows; Γ\_time for phases of directly governed enduring carriers |
| Work/cost       | External in **Γ\_work** (compute, curation)                      | External in **Γ\_work** (energy, labour)     |

### B.1.3:6 - Proof obligations (normative)

**At synthesis (Γ\_epist^synth):**

1. **PO‑SYN‑PROV.** The **provenance/evidence graph** MUST be preserved (union with de‑duplication); every retained claim is traceable to sources/methods in the **SCR**.
2. **PO-SYN-OBJ.** The result **MUST** name one exact EntityOfConcern already identified under its direct pattern. If the synthesis depends on several inputs as a joint subject, its collection, relation, or whole identity **MUST** be independently governed; a list, graph, label, or mapping is insufficient. Every semantic mapping used by the fold **MUST** be declared with its **CL** evidence summary.
3. **PO-SYN-CL.** Every mapping used in the support account **MUST** retain its CL evidence summary and actual use limitation. A numerical loss **MUST** have a receiving model establishing its meaning, scale, derivation or calibration, and assumptions; ordinal ranks and monotonicity alone are insufficient. The summary neither establishes an F.9 Bridge nor grants use.
4. **PO‑SYN‑R.** The result **MUST** distinguish indispensable premises, sufficient alternatives, complementary support, scope slices, and counterevidence where present. An aggregate R **MUST** have warranted input meanings, scales, dependencies, and an operation under B.3/C.2.2. Otherwise retain separate support and a reasoned bounded synthesis. Neither F nor a mode tag supplies an R conversion.
5. **PO-SYN-CONFLICT.** The result **MUST** retain credible contrary evidence and distinguish an established scope or interpretation difference from an unresolved conflict. Narrow, qualify, or withhold the affected conclusion accordingly. B.2 applies only to a separately grounded whole-reidentification question.
6. **PO‑SYN‑ORDER.** If order matters, the **OrderSpec** MUST be recorded and Γ\_ctx **NC‑1..3** (determinism, context hash, partial‑order soundness) MUST hold.
7. **PO‑SYN‑NOWORK.** Resource spending, yields, and dissipation MUST NOT be computed here; instead, attach references to the aligned **Γ\_work** composition.

**At compilation (Γ\_epist^compile):**

1. **PO-COMP-SCHEME.** The exact target reference scheme **MUST** be declared. Every active concept and unit **MUST** have an explicit mapping; a cross-context meaning use **MUST** name the exact F.9 Bridge, separate bounded-use claim, permitted loss, and any relied-on A.10 or B.3 result.
2. **PO-COMP-ASSUR.** The formal basis, scope, and support account **MUST** be re-expressed in the target scheme without losing their limitations. Any recalculated R or loss **MUST** satisfy the receiving model; otherwise preserve the separate support and bounded conclusion.
3. **PO-COMP-SCR.** The compiled episteme **MUST** retain an SCR with the hashes, versions, and dates required to reconstruct the application. This obligation does not assert release or publication.
4. **PO-COMP-ID.** The output **MUST** be identified through its C.2.1 claim content, exact EntityOfConcern, and effective target scheme. A changed discriminator identifies another episteme. B.2 is opened only for an independently current existing-whole versus candidate-new-whole question, never as a substitute for this identity rule.
5. **PO‑COMP‑ORDER/TIME.** If derivational order is essential, the **OrderSpec** MUST be referenced. If temporal selection is essential, name the exact C.2.1 episteme identity and reference the already recovered proper restriction, edition-relation order, applicability window, and B.1.4/**Γ\_time** aggregation actually consumed.

### B.1.3:7 - Conformance Checklist (normative)

| ID            | Requirement                                                                                                                                                         | Purpose                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **CC‑B1.3.1** | Inputs to Γ\_epist MUST be `U.Episteme` holons; **ComponentOf** is forbidden; use **ConstituentOf**, **UsageOf**, or **ReferenceTo** for their different claims; use a collection's own belongs-to predicate only for collections. | Prevent category errors. |
| **CC‑B1.3.2** | Provenance and **SCR** MUST be preserved in the aggregate; dropping sources or methods is non‑conformant.                                                      | Enforce Evidence Graph Referring.    |
| **CC‑B1.3.3** | Any aggregate R MUST follow the justified input meanings, scales, support dependencies, and receiving model. No default min, max, or F-to-R conversion is supplied; absent a common model, retain a bounded synthesis and separate support. | Prevent unsupported assurance and preserve useful non-aggregate results. |
| **CC-B1.3.4** | Contrary evidence MUST remain visible. An established scope or interpretation difference may separate claims; an unresolved conflict must qualify, narrow, or defeat the affected conclusion. Use B.2 only for a separately grounded whole-reidentification question. | Keep the practical effect of disagreement visible. |
| **CC‑B1.3.5** | Every `U.Episteme` serving as an input to `Γ_epist` **MUST** declare its `mode` (`axiomatic` or `postulative`). An aggregate holon's mode **MUST** be `postulative` if any of its constituents is `postulative`. | Prevent category errors in reliability calculation. |
| **CC-B1.3.6** | A cross-context meaning use names explicit mappings, exact source and receiving F.17 cells, an obtaining F.9 Bridge, a separate bounded-use claim and permitted loss, and any reliance result the fold consumes. **CL** alone never grants the use. | Make semantic crossing inspectable. |
| **CC‑B1.3.7** | If order matters, Γ\_ctx **NC‑1..3** MUST hold. If an episteme history matters, exact C.2.1 endpoint identities and any obtaining `EpistemeEditionRelation` MUST be named; any proper restriction or B.1.4/**Γ\_time** aggregation MUST cite only already recovered temporal relations. | Preserve order, identity, continuity, and temporal integrity. |
| **CC-B1.3.8** | Keep design-time synthesis, target-scheme compilation, one actual operation application and its returned value, dated Work, performer and any relied-on assignment, production or first existence, publication, carrier, release, and acceptance separately governed. | Preserve semantic and practical boundaries. |

### B.1.3:8 - Anti‑patterns & repairs

| Anti‑pattern             | Symptom                                           | Repair                                                                                     |
| ------------------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Unsupported folding** | Incomparable scores are averaged, minimized, maximized, or converted from F | Identify support roles, scales, dependencies, and the receiving model. If none warrants aggregation, retain separate support and a bounded synthesis; do not hide counterevidence. |
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
* **Qualified synthesis.** Useful formal and complementary support is retained; dependency assumptions, contrary evidence, and mapping limitations constrain the resulting claim.
* **Target-scheme results.** Compiled epistemes are aligned with one declared reference scheme; any release or publication remains separately governed.
* **Didactic clarity.** Separates **semantic folding** (Γ\_epist) from **order** (Γ\_ctx), **time** (Γ\_time), **spend** (Γ\_work), and **emergence** (B.2).

**Trade‑offs**

* **Mapping overhead.** Declaring mappings and **CL** costs time; it prevents silent incoherence.
* **No forced single score.** Heterogeneous support may remain separate. This makes some comparisons less compact but avoids fictitious assurance and preserves a useful bounded conclusion. B.2 remains specific to a genuinely unresolved whole-reidentification question.

### B.1.3:10 - Rationale (informative)

* **Epistemic composition is not physical addition.** A missing necessary premise, a complementary study, and a contrary result do different work. The receiving claim and dependency model determine their combination; minimum is not universally conservative.
* **Provenance is part of meaning.** Dropping sources/methods changes what the episteme **is**; Γ\_epist treats provenance and **SCR** as first‑class.
* **Interpretation matters.** Exact reference schemes and local senses prevent quiet reinterpretation. F.9 governs any cross-context Bridge; C.2.1 governs the resulting episteme identity.
* **Parsimony with power.** Provenance, support roles and dependencies, exact mappings, and order/time hooks suffice for a useful synthesis without imposing a common score. [Gutierrez, Glymour and Davey Smith, *Evidence triangulation in health research* (2025)](https://link.springer.com/article/10.1007/s10654-024-01194-6) supports comparing design assumptions and shared biases, checking target-question comparability, and using qualitative comparison when quantitative pooling is unwarranted. This methodological contribution does not supply a universal R formula or make a further study mandatory.

### B.1.3:11 - Relations

* **Builds on:** C.2.1 (episteme identity and independently obtaining edition relations), A.6.1 (semantic operation declarations and exact application bindings), A.14 (ConstituentOf, collection belonging under each collection's own rule, and proper temporal restriction of one unchanged carrier), A.7 (Strict Distinction), and A.15/A.15.1 (Method/Work alignment and Work-temporal law). A.12 is used only when an acting-side distinction is current. An ordinary actor sentence needs no classification apparatus. Any particular dated synthesis or compilation `U.Work` first reuses each performer's A.13 core and is independently admitted under A.15.1; F.6 follows only when the receiving claim also needs precise assignment-bound attribution. A short local projection may omit an assignment identifier unused by the receiver only when every consumed relation remains recoverable.
* **Coordinates with:** B.1.1 dependency-structure and relation-grounding checks, B.1.4 (Γ\_ctx/Γ\_time inside knowledge folds), B.1.6 (Γ\_work for compute/collection spend).
* **Coordinates with:** F.9 for exact cross-context Bridges and bounded-use claims; A.10 or B.3 for reliance; A.15.PROD when production, first existence, or completion is current; and E.17/E.24.PUB for publication, form, and carrier. B.2 is used only when exact construction facts leave a separate whole-reidentification question after the existing-whole explanation check.
* **Used by:** B.3 assurance uses the aggregate's exact formal basis, scope, and support account, including any justified R calculation and mapping limitations; C.11 and C.19.2 govern a separately selected inquiry or action decision.

> **One‑sentence takeaway.**
> **Γ\_epist** preserves provenance, distinguishes what each source contributes, and combines support only as its meanings and dependencies warrant—returning a useful bounded synthesis when no common score is justified.

### B.1.3:End
