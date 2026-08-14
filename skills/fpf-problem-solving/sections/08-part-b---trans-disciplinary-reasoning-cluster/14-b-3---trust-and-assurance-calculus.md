## B.3 - Trust and Assurance Calculus (F-G-R with Congruence)

> **Type:** Foundational (B)
> **Status:** Stable
> **Normativity:** Normative for FPF use that claims assurance, trust, readiness, compliance, safety, release confidence, `F`, `G`, `R`, or `CL` for a named claim.

> **Plain-English headline.**
> B.3 governs an assurance-result claim about one exact claim episteme for one named assurance use. It conservatively combines formality `F`, claim scope `G`, reliability `R`, and edge-scoped congruence `CL` without turning evidence, provenance, a dashboard, a status value, an assessment record, or a later decision into assurance by presence. The target fact, its direct result, the claim episteme, assessment work, evidence-use relations, assurance-result claim, witness, record, publication, and later reliance remain separately recoverable.

**Use this when.** Use `B.3` when a receiving work or reliance decision depends on assurance, trust, readiness, compliance, safety, release confidence, `F`, `G`, `R`, or `CL` for one exact claim episteme.

**What goes wrong if missed.** A label, dashboard, model card, credential, provenance mark, gate decision, status value, or evidence bundle starts raising trust or readiness without an exact target claim, assessment, evidence-use basis, scope, limitations, decay condition, and named assurance use.

**What this buys.** The user gets a conservative, contestable assurance-result claim whose inputs and limits can be replayed without changing the target fact or confusing assurance with status, approval, permission, gate passage, currentness, or actual reliance.

**First output.** Write one typed `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)` claim for exact target-claim episteme `E_C` and named assurance use `U_A`, or write an explicit no-assurance disposition. A publication face, rendering, cue, evidence pointer, wording issue, gate decision, role assertion, status-value assertion, commitment, or work occurrence is not itself an assurance result.

**Not this pattern when.** Stay with `A.2.4` when the question is how an episteme is used as evidence or status support, with `A.10`/`G.6` for source recovery and bounded reliance, with `G.11` when currentness changes admissible use, and with `F.10` for the status value and its use. When no assurance claim or material-reliance threshold is current, use the exact gate, permission, commitment, work, decision, or domain-result rule that defines or tests the claim actually being made; do not create a B.3 result merely to name its pattern.

**Assurance result selection.** Use the lightest result that decides the named assurance use. A cue or source pointer gets no B.3 tuple. A local, reversible, non-release, non-compliance, non-safety use may need only a compact bounded assurance-result claim naming `E_C`, `U_A`, the evidence-use/provenance refs, limit, and reopen condition. Reserve the full typed result for readiness, compliance, safety, release confidence, trust, explicit `F/G/R/CL`, material reliance, or reuse as an assurance input.

**Assurance claim over time.** An assurance-result claim is time-bounded and updateable: it can decay, reopen, narrow, or be withdrawn. Name the drift, monitoring, incident, evidence refresh, version change, policy change, gate change, or residual unsupported-use condition that reopens it. Such a change can alter warrant or admissible reliance while leaving the target fact and target claim identity unchanged.

### B.3:1 - Problem frame

When a non-trivial result in FPF—*a composed system is safe*, *a model is credible*, *a conclusion holds*—is reused for a consequential assurance purpose, the assurance-result claim must expose the exact result claim and the basis on which that use is warranted.

* For a claim whose EntityOfConcern is a **U.System** holon, assurance evaluates the exact capability, constraint, safety, or reliability claim under stated conditions; it is not a new system state.
* For a claim whose EntityOfConcern is a **U.Episteme** holon, assurance evaluates the exact content or model claim and its warrant for `U_A`; it is not an intrinsic quality conferred on the episteme by a citation or evidence item.

To make such claims comparable and auditable across domains, B.3 introduces a **Trust and Assurance Calculus** that:

* uses a **small typed assurance tuple** (F-G-R: `F` and `R` as characteristics plus `G` as scope value) governed by conservative propagation rules; this tuple is **not** a state space,
* accounts for **integration quality** via **Congruence Level (CL)** along the edges of a `DependencyGraph` (B.1.1, A.14),
* and composes these values only through current governing composition, transformation, temporal, and work operators while respecting their declared invariants.

B.3 is **conceptual and normative**: it defines *which assurance components must be published and how they propagate*. How those components improve (for example by formalizing, replicating, reconciling, or widening or narrowing scope under declared operation rules) is handled by KD-CAL improvement moves; those knowledge-dynamics references are descriptive, not required to read here.

**Mechanism linkage.** For law-governed operation families (for example **USM** and **UNM**) authored as **mechanisms**, use A.6.1 — U.Mechanism to publish **OperationAlgebra**, **LawSet**, **AdmissibilityConditions**, and the **Transport** clause (Bridge-only; `CL`, `CL^k`, and `CL^plane`). All such penalties reduce `R_eff` only; `F` and `G` remain invariant.

**Working-Model handshake (alignment with E.14, B.3.5, and C.13).**
Assurance consumes two inputs declared in the **Working-Model** assertion layer (CT2R-LOG, B.3.5): the **justification declaration** `validationMode ∈ {postulate, inferential, axiomatic}` and, where present, the **grounding link** `tv:groundedBy`. Structural claims that aspire to the strongest guarantees rely on **Constructive** grounding as a constructive-composition narrative referenced via `tv:groundedBy`. No assurance record or publication **defines** Working-Model wording or layout; dependence remains downward-only under E.14.

### B.3:2 - Problem

Without a disciplined calculus, four chronic failures appear:

1. **Trust inflation:** Averaging or summing heterogeneous “quality” tags yields aggregates that look better than their weakest parts, violating WLNK.
2. **Scale confusion:** Mixing ordinal and ratio scales (e.g., averaging `F` ordinal scale values with numeric reliabilities) produces meaningless numbers.
3. **Congruence blindness:** Integration quality (how well pieces fit) is invisible; brilliantly strong parts connected by weak mappings produce overconfident wholes.
4. **Scope drift:** Design-time formalism and run-time evidence are composed into a single score; dashboards then claim “assurance” for a blueprint using run-time data, or vice versa.

### B.3:3 - Forces

| Force                                    | Tension                                                                                                                             |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Conservatism vs. Synthesis**           | Avoid overclaiming (WLNK) ↔ recognize real gains from better integration (raise CL) or true emergence (B.2).                            |
| **Universality vs. Domain nuance**       | One calculus for systems and epistemes ↔ physics and epistemology use different primitives; keep them comparable but not identical. |
| **Simplicity vs. Fidelity**              | Keep the assurance tuple small and typed (A.11) ↔ capture enough structure to be informative and improvable by KD-CAL moves.           |
| **Static clarity vs. Dynamic evolution** | A score must be reproducible today ↔ tomorrow it should legitimately rise after formalization, replication, or reconciliation.      |

### B.3:4 - Solution — **Part 1: The assurance tuple and the universal aggregation skeleton**

B.3 defines **what** the assurance components are, **where** they are assigned on nodes and edges of the dependency graph, and the **shape** of the aggregation that any Γ-flavour must honor when producing an *assurance result*.

#### B.3:4.1 - The F-G-R assurance components (typed; `F` and `R` as CHR, `G` as USM)

We standardize **two claim-facing characteristics**, **one claim-scope value**, and **one integration-relation characteristic**. Every value still names its exact bearer, scheme, scope, window, and basis under B.3:4.2-4.3:

1. **Formality (F)** — *how constrained the reasoning is by explicit, proof-grade structure.*

   * **Scale kind:** **ordinal** (its scale values do not admit arithmetic).
   * **Canonical scale values (example):**
     `F0 Informal prose` - `F1 Structured narrative` - `F2 Formalizable schema` - `F3 Proof-grade formalism`.
   * **Monotone direction:** higher is better (never lowers assurance when all else fixed).

2. **ClaimScope (G)** — *the declared set of `U.ContextSlice` values where the result applies.*

   * **Type:** **set-valued USM scope value** (A.2.6), **not** a CHR characteristic.
   * **Well-typed operations:** **membership** and **set algebra** (`∈`, `⊆`, `∩`, `⋃`, `SpanUnion`, plus declared Bridge translation, widening, narrowing, or refit operation).
   * **Scalar proxy (report-only):** if a G scope report needs a number, it may publish an explicitly declared **CoverageMetric(G)**; such a proxy must not replace G in norms, gates, bridge semantics, or CL-bearing relation decisions.

3. **Reliability (R)** — *how likely the claim or behavior holds under stated conditions.*

   * **Scale kind:** **ratio** in `[0,1]` (or a conservative ordinal proxy when numeric modeling is unavailable).
   * **Monotone direction:** higher is better.

4. **Congruence Level (CL)** — *characteristic of one exact integration, mapping, calibration, interface, or other admitted relation occurrence: how well its participants fit for the named assurance use.*

   * **Scale kind:** **ordinal** with a **monotone penalty function** `Φ(CL)` where `Φ` decreases as CL increases.
   * **Canonical scale values (example):**
     `CL0 tentative guess` - `CL1 plausible mapping` - `CL2 validated mapping` - `CL3 verified equivalence`.
   * **Interpretation:** low CL reduces the credibility of the *integration itself* (not the parts), and therefore **penalizes** the aggregate **R**.

> **EntityOfConcern and description strict distinction (A.7).**
>
> * Assurance components are recorded as **value and scope claim components**: `F` and `R` as characteristics, `G` as a scope value, while the governing composition, order, temporal, and work patterns keep **structure, order, and time** distinct.
> * Do not smuggle assurance components into structural edges; keep `F`, `R`, and `CL` explicit as CHR metadata and `G` explicit as a USM scope value.

> **Assurance shoulders (Working-Model split).**
> **Mapping** raises **TA** (typing, fit, and CL). **Logical** and **Constructive** contribute to **VA** (intended relation semantics; constructive-composition identity when its governor admits it). **Empirical Validation** contributes to **LA** through exact input-result and evidence-use relations under the named ReferenceScheme, ClaimScope, conditions, and window. These inputs may be cited from an E.14 Working-Model assertion layer, but B.3 does not make the layer, face, or record an assurance result.

#### B.3:4.2 - Assurance as a typed result claim

Begin with one exact C.2.1 target-claim episteme `E_C`: its ClaimGraph states the claim being assured, its EntityOfConcern identifies what that claim concerns, and its effective ReferenceScheme interprets the claim. Any measurement, causal, conformance, status, capability, safety, or other subject result asserted by that ClaimGraph remains with its direct governor. B.3 neither makes that result obtain nor changes claim truth.

For one named assurance use `U_A`, B.3 may constitute a separate assurance-result episteme whose ClaimGraph contains:

```text
AssuranceResult(E_C, U_A | RS_A, G_A, T_A)
  = <F_eff, G_eff, R_eff, CL_basis, disposition, limitations>
```

* `E_C` is the exact target-claim episteme, not a carrier, status tile, evidence item, result record, or bare holon label.
* `U_A` is the exact readiness, compliance, safety, release-confidence, model-credibility, trust, or other receiving assurance use; it is not proof that later work actually relied on the result.
* `RS_A` is the effective ReferenceScheme interpreting the assurance-result ClaimGraph. The target claim retains its own effective ReferenceScheme.
* `G_A` is the A.2.6-governed claim scope for this assurance result. Assumptions, environment, audience, operating conditions, and local sense constraints are stated by value rather than hidden in a generic context field.
* `T_A` is the declared design/run stance and exact applicability, evidence, or reliance window. Design and run results remain separate.

Keep the following objects distinct whenever they are current:

1. the world-side subject facts and domain-local result under their direct governors;
2. target-claim episteme `E_C` under C.2.1;
3. each exact A.2.4 evidence-use relation classifying an episteme for a target claim, scope, polarity, window, and intended assurance use;
4. the A.10/G.6 source-provenance path and local `RelianceDisposition` for the bounded evidence use;
5. dated assurance-assessment `U.Work`, its performer assignment, enacted method, and exact direct or A.6.1 application bindings;
6. formal, empirical, causal, measurement, conformance, comparison, or other input results and the C.2.1 epistemes that state them;
7. the B.3 assurance-result claim and its distinct C.2.1 episteme;
8. witnesses, calculation traces, an optional assurance record episteme, publication occurrence, form, rendering, and carrier; and
9. any later premise/use relation, reliance decision, F.10 status use, A.21 gate decision, permission, release decision, or performed action.

None of objects 3-9 makes the target fact true. An evidence change may change input availability, warrant, `F/G/R/CL`, the assurance disposition, or admissible reliance without changing the world-side result or `E_C`. Absence of evidence is therefore not a negative target result. A status value, successful check, record field, publication, or favorable assurance result likewise does not create the target, approve a release, grant permission, or establish actual use.

A minimally replayable assurance-result ClaimGraph designates:

```text
AssuranceResultClaim:
  TargetClaimEpistemeRef: E_C
  AssuranceUse: U_A
  EffectiveReferenceScheme: RS_A
  ClaimScope: G_A
  TimeStanceAndWindow: T_A
  AssumptionAndConditionRefs:
  F_eff:
  G_eff:
  R_eff:
  CongruenceOccurrenceRefs:
  AggregationRuleRef:
  InputResultClaimRefs:
  EvidenceUseRelationRefs:
  A10OrG6PathRefs:
  AssessmentWorkRef:
  AssessmentMethodAndApplicationRefs:
  WitnessOrCalculationTraceRefs:
  Disposition: pass | bounded | degrade | abstain | evidence-needed | reopen | blocked
  LimitationsAndNotCarried:
  DecayAndReopenCondition:
```

The ClaimGraph is claim content, not a work log or record schema that performs the assessment. `AssessmentWorkRef` and application refs must resolve outward to independently governed occurrences. Witnesses support replay; they are not result claims. An optional assurance record cites the result and its basis; it does not become the result or perform the work.

**Validation modes (preserved input distinction).** When a target claim is published through an E.14 Working-Model assertion, its declared `validationMode ∈ {postulate, inferential, axiomatic}` is one input to assurance reasoning. `postulate` calls for the declared empirical audit basis; `inferential` calls for the exact reasoning basis; `axiomatic` calls for the exact constructive identity and grounding basis under its direct governors. The declaration, `tv:groundedBy` pointer, assessment work, result claim, evidence use, and publication remain different objects.

**Design versus run (no chimeras).** Produce separate assurance-result claims when the target use, assumption set, scope, evidence window, or design/run stance differs. Compare them explicitly; do not compose blueprint formality and runtime evidence into one score.

#### B.3:4.2a - Authority-looking labels and dashboard tiles

A badge, label, score, dashboard tile, credential display, provenance mark, compliance-looking mark, model card, datasheet, data card, assurance document, attestation label, assurance-looking note, or generated confidence phrase does not enter assurance calculus or improve `F`, `G`, `R`, `CL`, readiness, safety, compliance, trust, release confidence, or assurance by display alone.

**Adversarial misuse guard.** Do not let dashboards with favorable labels, compliance-looking badges, old model cards, provenance labels, assurance-looking documents, or generated confidence phrases supply missing evidence, limitations, scope, decay, or argument for an assurance claim.

B.3 dispositions for such a source or publication face are:

| Disposition | Use when | Output |
| --- | --- | --- |
| No assurance use | The encountered source or publication face is only a cue, source pointer, evidence question, currentness question, gate decision, role assertion, status-value assertion, commitment, boundary wording, or work occurrence. | Use `A.15`, `A.10`, `A.6`, `A.21`, `A.20`, `A.2.1`, `A.2.8`, `A.2.9`, or `A.15.1`; no tuple is needed. |
| Compact bounded assurance-result claim | The target use is local, reversible, non-release, non-compliance, non-safety, not reused as assurance input, and does not affect a people or team status value. | Name `E_C`, `U_A`, the exact evidence-use/provenance refs, limit, disposition, and stop or reopen condition; do not turn the work record into the result. |
| Full assurance-result claim | The receiving use raises readiness, compliance, safety, release confidence, trust, explicit `F/G/R/CL`, or reused assurance input. | One typed `AssuranceResult(E_C, U_A &#124; RS_A, G_A, T_A)` claim with assessment basis, argument, evidence-use/provenance refs, limitations, disposition, and decay condition. |
| Rejected or narrowed assurance claim | Evidence, scope, argument, currentness, or limitations do not carry the attempted assurance claim. | State the assurance claim, work claim, or reliance claim that the current assurance tuple does not carry, then name the next legitimate formalization, evidence repair, scope narrowing, or claim narrowing move. |

Build a `B.3` assurance claim only when the next work occurrence or reliance use depends on a typed assurance claim. The typed assurance claim names:

| Field | Required content |
| --- | --- |
| Target claim and assurance use | Exact target-claim episteme `E_C`, its direct subject-result governor, and named `U_A`: readiness, release, audit, compliance, safety, model credibility, or another assurance use. |
| Interpretation, scope, conditions, and time | `RS_A`, `G_A`, `T_A`, exact assumption/condition refs, and the audience or relying role when human-facing. The target holon is reached through `E_C`'s EntityOfConcern, not copied into a generic context tuple. |
| Assessment work and condition | Dated assessment work, performer assignment, enacted method, exact rule/application bindings, and the method, policy, test, audit, or measurement conditions consumed. |
| Input results, evidence use, and provenance | Name the exact domain input-result claims; A.2.4 evidence-use relation refs with target, polarity, scope, window, and intended use; and the minimum A.10/G.6 provenance path. A proof or status result remains a separate domain result; its appearance in an assurance record neither makes it evidence nor raises assurance. Cite the exact defining or testing content only when the assurance argument depends on that interpretation. |
| Argument and assurance rationale | The exact aggregation/argument rule and why the cited input-result and evidence-use relations warrant the assurance-result claim for `E_C` and `U_A` under `RS_A`, `G_A`, and `T_A`, including assumptions, defeaters, and challenges. |
| Limitations and rival explanations | Scope limits, claims or uses not carried by the assurance tuple, stale display, spoofing, copied text, generated text, proxy-for-value substitution, provenance-only source relation, context shift, and known failure conditions. |
| Decay and reopen condition | Valid-until, revocation, policy version, gate version, model version drift, monitoring change, incident signal, evidence refresh, and contest or redress relation. |

For a full threshold-bearing assurance result, retain the dated assessment `U.Work`, capable performer and assignment, enacted Method, and application bindings when their identity bears on replay, competence, conflict, timing, reproducibility, contest, or redress. If evidence was produced by a material analysis or test, keep that evidence-production Work and its result distinct from the assurance-assessment Work and assurance result. A method description, record, witness, publication, or favorable result performs neither work and establishes no later reliance.

**Assurance evidence minimization.** Cite only the A.2.4 evidence-use relations and minimum A.10/G.6 paths needed for `E_C` and `U_A`. Use redacted, hashed, scoped, or role-mediated refs when raw material exposes personal data, secrets, privileged logs, tenant identifiers, security-sensitive traces, incident details, or unnecessary identities; a compact pointer must still preserve enough recoverability to replay the warrant.

Viewpoint prompts for assurance use:

| Role in the situation | Prompt |
| --- | --- |
| Assurance steward | Which exact `E_C`, named `U_A`, and `AssuranceResult(E_C, U_A &#124; RS_A, G_A, T_A)` claim are being assessed or revised? |
| Audit role | Which assessment-work/application refs, input-result claims, evidence-use/provenance refs, witnesses, argument, limitations, decay condition, and reopen condition must be recoverable? |
| Manager or release role | Which desired decision or work or reliance use is outside B.3 and must instead use `A.15`, `A.21`, `A.10`, or another named source? |
| Model or data steward | Which documented bounded-use statement or external intended-use field, evaluation condition, version, window, limitation, drift, and incident condition bound the model or data documentation? |
| Evidence source-maintenance role assignment | What evidence ref or scoped pointer must be exposed without turning documentation presence into an assurance claim? |

Display guidance for assurance labels: a readiness, safety, compliance, trust, release-confidence, or assurance display should expose `E_C`, `U_A`, assessment/result ref, evidence-use/provenance refs, scope, window, limitation, disposition, decay and reopen conditions, and the status, work, gate, permission, decision, or reliance claims not carried. Display is a representation/publication of the result, not the result, assessment, or later use.

Incident-learning fields for assurance overread: visible label, documentation record, attempted assurance claim, missing tuple or evidence-provenance field, assurance claim, work claim, or reliance claim not carried by the assurance tuple, limitation or decay condition that defeated the claim, next legitimate formalization, evidence repair, scope narrowing, or claim narrowing move, and upstream repair record for documentation, evidence refs, assurance label wording, monitoring, or reopen trigger.

Contestability and redress relation: when the B.3 material-reliance threshold is met, the B.3 result should name the claim being contested, evidence-provenance path, limitation or decay condition, contest forum or decision forum, safe interim disposition, and what evidence or scope change would reopen the assurance claim.

If those fields are missing, the encountered publication face, rendering, or cue remains an orientation label, source pointer, evidence pointer, documentation record, or unsubstantiated confidence cue. Use `A.15` when the question is whether that lane may guide work or reliance, `A.10` when the question is evidence, currentness, or provenance, and `A.6` when the question is mixed policy, API, or schema wording.

**Positive repaired assurance statement.** When the named use and required fields are present, state the smallest `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)` claim that can guide the use, with assessment ref, exact input-result and evidence-use/provenance refs, argument, limitations, disposition, decay, and reopen condition. It warrants only `U_A`; any gate, status, permission, performed work, decision, or later reliance remains separately governed.
Constructive assurance moves:

- narrow `G` to the evidenced or rule-bounded scope;
- raise `F` by formalizing argument structure or method-description fields, or by naming the exact method-side relations used in composition, fallback, selection, or a method family; when the assurance question depends on their organization, use A.22's structure-selection criterion to select the structure for that use and call it `MethodRelationStructure`;
- raise `R` by adding validation, replication, more probative, repeated, current, or more relevant evidence;
- improve `CL` by repairing mappings, units, interfaces, or integration edges;
- separate design assurance from run assurance;
- add limitations, assumptions, defeaters, monitoring, drift, and reopen triggers;
- reject or downgrade the assurance use when those moves are not available.

Negative controls:

| Visible source or publication face | Bounded source or assurance use | Unsupported use without a typed assurance claim |
| --- | --- | --- |
| Source-backed release dashboard tile | If the tile is a current view of `A.21` `GateDecision` or `DecisionLogRef` plus an `A.10` evidence-provenance path, it may carry gate-passage reliance outside B.3 for the named release and environment. B.3 is used only when the tile is also asked to raise readiness, safety, compliance, trust, or release-confidence assurance. | Release approval by display, compliance proof, rollback success, work occurrence, or assurance increase without a typed assurance claim. |
| Credential, compliance, or provenance label | Bounded source, holder, status value, history, or documentation source relation when evidenced. | Safety, truth, permission, gate passage, readiness, or assurance claim by label presence. |
| Model card, datasheet, data card, assurance document, or assurance-looking note | Scoped documentation for a named claim, documented bounded-use statement or external intended-use field, evaluated condition, limitation, version, and window. | Higher `R`, broader `G`, higher `F`, better `CL`, readiness, compliance, safety, or release confidence by document presence. |
| Generated confidence phrase | Source-finding or explanation relation when grounded. | Assurance increase, authority, approval, or evidence by wording alone. |

Model cards, datasheets, data cards, assurance documents, and assurance-looking notes are external documentation records or source records unless they are mapped into existing `FPF` claims and publication faces. They do not add MVPK face kinds and do not bypass `B.3` when the use under repair is an assurance claim.

**Lint trigger.** A model card, datasheet, or data card cited as readiness, safety, compliance, release confidence, or assurance proof requires an exact target-claim episteme, intended-use match, assessment condition, limitations, A.2.4 evidence-use refs, an A.10/G.6 path, and one typed `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)` claim. Otherwise return `no assurance use`, a rejected result, or a narrower bounded result.

Positive repaired example: a model card may expose an exact model-claim episteme, intended-use statement, evaluated condition, version, window, limitations, evidence-use refs, A.10/G.6 path, and a separately constituted `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)`. That result may warrant only the named evaluated model use; the card still does not create another deployment claim, gate passage, release work, status, or compliance result.

#### B.3:4.2b - Minimum reliance safety assurance record

Use this B.3 section when the B.3 material-reliance threshold is met: reliance on a visible carrier, source reference, publication face, or display may materially change behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people or team status value, operational action, or controlled-entity regulation. The first B.3 move is to decide whether an assurance claim is being made; if it is, write the minimum reliance safety assurance record for the named reliance use. Mere attention shift, learning, orientation, source-finding, or source-wording correction is not enough.

`RelianceSafetyCase` is the local Tech label for this B.3 assurance-record form. The plain phrase is **minimum reliance safety assurance record**. The label is not a new FPF pattern, Core kind, safety authority, gate, policy source, approval, certificate, compliance method, or general safety-case ontology.

Assurance-record use: the trigger/non-trigger table is a recognition aid, the minimum-record table is a local form aid, and the worked slices are examples. They are not a universal checklist, sign-off sequence, status vocabulary, assessment work, or replacement for `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)`. The record cites the assurance-result claim and its independently governed basis; filling it makes no relation obtain.

Affordability card: orientation or source-finding stays outside B.3; bounded local reliance stays with the local evidence, explanation, CV, gate, or pattern-quality relation unless an assurance claim is being made; threshold reliance uses the minimum reliance safety assurance record only when the B.3 material-reliance threshold is met. Plain wording remains ordinary unless it changes a bounded use, source relation, evidence use, gate, assurance claim, work, or decision. Stop after naming the concrete use or relation that changed; no selected pattern locator is required.

Common wrong first classification: a safety-looking note, safety case, compliance-looking label, or dashboard warning is a certificate, approval, or gate. First honest entry: state one typed B.3 assurance claim with A.10 evidence-provenance path, assumptions, limitations, defeaters, residual uncertainty, monitoring or stop condition, contest and redress relation, bounded assurance use, and unsupported attempted use.

First B.3 move: name the reliance use, the assurance claim, the affected context or audience, the trigger that meets the B.3 material-reliance threshold, the A.10 evidence-provenance path, the argument, limitations, defeaters, contest and redress relation, stop or monitoring condition, bounded assurance use, and unsupported attempted use. If those pieces are absent, use `A.10`, `E.17.EFP`, `A.20`, `A.21`, `E.19`, or the local relation that actually governs the source use rather than inventing assurance by label.

Trigger and non-trigger cases:

| Encountered source use | B.3 disposition | Minimum response |
| --- | --- | --- |
| Ordinary source-backed report, citation, model card, datasheet, data card, or documentation record with no assurance use and no met B.3 material-reliance threshold | No B.3 assurance use. | Stay in `A.10` with claim, source record or publication face, evidence-provenance path, window, bounded evidence use, unsupported attempted use, and reopen trigger. |
| Generated explanation, generated summary, or didactic reconstruction used only for source-finding or learning | No B.3 assurance use. | Stay in `E.17.EFP` unless operative claims are relied on through `A.10` evidence-provenance paths or another source relation that carries or exposes the source basis for the operative claim. |
| Local conformance label, `CV.Status`, benchmark result, or score near a release conversation but not used to raise assurance | No B.3 assurance use. | Keep `CV.Status` in `A.20`, gate-decision publication in `A.21`, pattern-quality result in `E.19`, measurement or marker relation in `C.16` or `A.10`, and no assurance tuple unless an assurance claim is being made. |
| Confidence, calibration, prediction interval, or abstention reason tied to one reversible local act | Compact bounded assurance claim only when the act depends on assurance; otherwise no B.3 use. | State act, context, window, calibration condition, stop condition, bounded evidence use, and unsupported attempted use; use `C.27` or `G.11` when time, expiry, refresh, or monitoring changes the action. |
| Safety-looking note, compliance-looking label, public warning, dashboard value, generated operational explanation, or status-value display is intended or reasonably foreseeable to meet the B.3 material-reliance threshold: reliance materially changes behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people or team status value, operational action, or controlled-entity regulation. | Minimum reliance safety assurance record is required. | Build the B.3 assurance record with A.10 evidence-provenance path and any relevant `A.20`, `A.21`, `E.19`, `C.27`, `G.11`, `B.2.5`, or representation and retargeting dependency. |

Minimum assurance record:

| Field | Required content |
| --- | --- |
| Reliance use and assurance claim | The behavior, safety, release, compliance, public or protocol behavior, access, resource allocation, people or team status value, operational action, or controlled-entity regulation that would materially change, and the assurance claim being made about that change. |
| Scope, conditions, audience, and affected systems | Exact ReferenceScheme and ClaimScope, environment and condition refs, time window, user group or public audience, relying and affected Systems, any exact local system-role kinds and separately obtaining assignments required by the use, tenant, release line, service, and receiving Work or use relation. Assignment does not establish authority or responsibility. |
| Source relation or carrier record and evidence kind | The visible carrier, source reference, publication face, record, cue, marker, conformance label, dashboard, explanation rendering, score, warning, or status-value display, plus the evidence kind being used. |
| A.10 evidence-provenance path | Claim, source record or source relation, producer or Method trace, currentness and window, and admitted source-maintenance System. When maintenance is admitted Work, A.15.1 identifies it and F.6 identifies the assignment under which each performer acted; include an assignment identifier only when the assurance claim uses it. Also state the direct source-maintenance responsibility relation or exact missing governor, evidence relation, rival explanation, bounded evidence use, unsupported attempted use, and reopen trigger. |
| Argument and assurance relation | Why this evidence-provenance path carries the assurance claim under the context; include assumptions, limitations, defeaters, residual uncertainty, and unacceptable-harm or risk-tolerance condition when relevant. |
| Dependencies | Any relevant `A.20` CV status, `A.21` gate decision, `E.19` pattern-quality result, `C.27` temporal claim, `G.11` refresh and decay relation, `B.2.5` control relation, or representation and retargeting relation. |
| Monitoring, rollback, or stop condition | What observation, incident, drift, contest, expiry, changed C.28 identification or realizability profile, changed A.21 gate profile, changed evaluation condition, changed source record, or failed check stops, narrows, reopens, or withdraws the reliance. |
| Contest and redress | The disputed claim or disposition, affected use or harm, admitted review System, any exact review-system-role kind or assignment needed by the work context, direct review-responsibility relation or exact missing governor, challenge evidence admitted by the contest relation, possible disposition change, outcome record, and reopen trigger. |
| Public and protected evidence boundary | Public summary, protected evidence reserved for the admitted review System under its access relation, affected-party contestable minimum, and any scoped, redacted, hashed, or mediated evidence ref needed to preserve recoverability without overexposure. A system-role kind or assignment does not supply access or authority. |

Positive repaired assurance result: when the threshold is met and the record is sufficient, constitute the smallest assurance-result claim for `E_C` and `U_A`, with exact scope/conditions/window, assessment-work ref, input-result and evidence-use/provenance refs, argument, limitations, dependencies, monitoring or stop condition, contest/redress relation, disposition, and unsupported use. The record then cites that result. If insufficient, narrow, degrade, abstain, request evidence, reopen, or block; polished documentation is not safety acceptance.

A safety case is accepted only as a bounded assurance argument for the named reliance use. It remains contestable by defeaters, changed evidence, changed context, monitoring failure, residual-uncertainty breach, or affected-party challenge admitted by the contest relation. Stop when the named reliance use, unsupported attempted use, limitations, defeaters, contest and redress relation, monitoring or rollback condition, and reopen condition are sufficient for this threshold trigger; do not expand the record into a general safety dossier.

A review label, system-role kind, or assignment is insufficient by itself. Review responsibility counts here only through an admitted direct domain predicate whose actual System and applicability are explicit; if none is current, record the exact missing governor. The contest relation must still be able to change the disposition, record the outcome, and leave the bounded assurance use, unsupported attempted use, and reopen condition inspectable.

Misuse guard: an incoming or attempted-reliance `RelianceDisposition=safety-case-required` must name the trigger that meets the B.3 material-reliance threshold. A source producer, dashboard-value publisher or maintainer, model producer, documentation producer, or status-value label issuer cannot self-clear a threshold-bearing reliance by attaching the label. Where the threshold is met, the assurance record must expose an admitted review System, a separately obtaining assignment only when the work context needs it, a direct review-responsibility relation or exact missing governor, and a contest relation capable of changing the disposition.

Affected-party contestable minimum: public and protected evidence separation is sufficient only if the affected party can see enough of the claim, source class, disposition, affected use, admitted review System, direct review-responsibility relation, and challenge evidence admitted by the contest relation to challenge the result. Protected evidence may stay protected under a separate access relation, but protection cannot make redress non-contestable while the assurance use still claims contest or assurance. A blocked, abstained, degraded, or evidence-needed assurance use is not final if admitted challenge evidence, missing affected-party evidence, changed source, changed context, monitoring failure, or redress can materially change the disposition.

Worked reliance-threshold slices:

| Slice | B.3 move | Boundary |
| --- | --- | --- |
| A public-service or access status-value display changes who receives access, assistance, or review. | Use the minimum reliance safety assurance record for the named status-value-changing reliance, with contest and redress and unsupported attempted use. | The display is not approval, safety, fairness, compliance, or resource authority by itself. |
| An SRE dashboard changes incident behavior or resource allocation. | Use B.3 only when the dashboard is asked to raise assurance or safety-bearing reliance; keep ordinary evidence and currentness in A.10. | Use B.2.5 only for a control relation being claimed and A.21 only for a gate decision being claimed. |
| A public warning or synthetic-content label changes perceived meaning but there is no evidence that it changed the behavior claimed to change, release risk, safety claim, or control relation. | Keep the label as A.10 evidence or source-finding and orientation cue; require audience-effect or behavior-effect evidence before B.3 reliance. | Do not infer safety, compliance, behavior change, or control effect from label presence alone. |
| A manufacturing conformance label appears near release. | Keep local CV or conformance evidence in `A.20`, `A.21`, `C.16`, or `A.10`; use B.3 only when assurance, safety, compliance, or release-confidence reliance is being claimed. | Conformance presence is not safety acceptance or release permission. |
| A software supply-chain attestation is cited as runtime safety. | Use `A.10` for origin, build, and process claims and B.3 only for the named assurance claim with argument, limitations, defeaters, and stop condition. | Build provenance is not runtime safety or operational permission. |
| A people or team status-value badge changes permissions, resources, or review priority. | Require an assurance record that names affected and relying Systems, any exact system-role kind or assignment needed by the context, the evidence-provenance path, direct review-responsibility relation or exact missing governor, contest relation, and disposition-change condition. | The badge issuer cannot self-clear the status-value-changing reliance by issuing the badge, and assignment does not establish authority or responsibility. |
| A standards-document clause is reused as approval. | Use `A.10` for evidence of the clause; use the named approval, commitment, gate, or assurance relation only when that relation is being claimed by value. | A cited clause is not project approval, gate passage, or assurance by quotation. |

Do not treat the assurance record as a graded scale, standalone status value, universal assurance checklist, release certificate, or new safety-case disposition family. B.3 consumes the assurance record only as typed assurance input for the named claim and reliance use.

#### B.3:4.3 - Where the values are assigned (and where they are not)

* **On exact assurance inputs:** every `F_i`, `G_i`, or `R_i` designates the exact target or input claim to which it applies, its bearer under the current characteristic/scope governor, effective ReferenceScheme, scope, time stance/window, and input-result or evidence-use basis. A node, row, label, source file, or evidence item does not receive a value merely by appearing in a graph.
* **On exact integration relations:** every `CL` value qualifies one independently established integration, mapping, calibration, interface, or other direct relation occurrence. A drawn edge or Bridge description does not create that occurrence.
* **On the assurance result:** the aggregation rule yields `F_eff`, `G_eff`, and `R_eff` in the B.3 assurance-result ClaimGraph for `E_C` and `U_A`. It does not overwrite the input values, the subject result, or the target claim.
* **Not inside Γ:** Γ consumes its own admitted inputs and produces its own composed result or holon under the applicable composition pattern. B.3 only evaluates assurance for the named claim about that result; it does not become the composition operator.
* **Not work, evidence, status, or a state space:** `⟨F,G,R⟩` is neither assessment work, an evidence-use relation, a provenance path, a status value, nor a `U.CharacteristicSpace`. Do not draw trajectories in it; use ESG and the assurance-trace hooks for separately identified changes in assurance-result claims.

#### B.3:4.4 - Universal aggregation skeleton (domain‑neutral)

When a B.3 assessment consumes results organized by a Γ-flavour, its assurance-result claim **must** adopt the following conservative skeleton; the Γ record itself neither emits nor performs assurance:

1. **Formality:**

   ```
   F_eff = min_i F_i
   ```

   *Rationale:* the least formal piece caps the formality of the whole (WLNK on F).
   *Monotone:* raising any `F_i` cannot reduce `F_eff`.

2. **ClaimScope (G):**

   ```
   G_eff(path)  = intersection({G_i | i is essential on the dependency path})
   G_eff(claim) = SpanUnion({G_eff(path_j)}) only across independently evidenced paths
   ```

   * Along an essential dependency path, every required evidence relation must hold on the same slice, so the effective claim scope is the intersection of the required scopes. Empty intersection means the path does not evidence the claim on any slice.
   * Across independent evidence lines for the same claim, B.3 may publish a `SpanUnion` of the path scopes, but only when the independence assumption and evidence relation are explicit.
   * **Constraint:** any region not covered by the required evidence relation for its path is dropped. A raw union of node scopes is never the default law for `G`.
   * *Monotone:* adding an independently evidenced path may widen the published claim scope; adding a new essential dependency may narrow it.

3. **Reliability (penalized by integration):**

   ```
   R_raw = min_i R_i                       # Weakest-link cap
   R_eff = max(0, R_raw − Φ(CL_min))       # Congruence penalty
   ```

   * `CL_min` is the **lowest** Congruence Level (`CL`) value on any edge in the declared proof path or critical integration subgraph for the claim `C`.
   * `Φ` is **monotone decreasing** and **bounded** (never makes negative values).
   * *Monotone:* increasing any `R_i` or any `CL` cannot lower `R_eff`.

4. **Evidence-source notes:**
   * The aggregation yields values in the assurance-result ClaimGraph. An optional assurance record separately cites all contributing input claims and exact integration relations, their F/G/R/CL values and bearers, assessment-work/application refs, evidence-use/provenance refs, and witnesses. Use A.10 and G.6 for the descriptive paths and G.11 for any currentness result.
   * The record also cites `E_C`'s ClaimGraph, EntityOfConcern, effective ReferenceScheme, and any separately obtaining empirical-grounding relation; it may present separable TA, VA, and LA input breakdowns, decay/valid-until marks, and the Epistemic-Debt tally without making those presentation fields target facts or evidence-use occurrences.
   * If order or time mattered for the claim, attach the OrderSpec or TimeWindow identifiers (B.1.4).

This skeleton is **mandatory**. Domain‑specific patterns may add **refinements** (e.g., separate epistemic “replicability” vs. “calibration”) as long as they **do not violate** WLNK or MONO and preserve scale kinds.

#### B.3:4.5 - System vs. Episteme - same shape, different interpretations

For **systems**:

  * `F` means **engineering discipline** (from ad-hoc method to verified specification).
  * `G` means **operational envelope coverage**.
  * `R` means **assured reliability** for the exact system claim under the named requirements, environment, test basis, scheme, scope, and time window.
  * `CL` covers interface verification or integration verification.

For **epistemes**:

  * `F` means **logical formality or semantic formality** (from prose to proof).
  * `G` means **domain span** (concepts, populations, conditions).
  * `R` means **evidential relation quality** (replication quality, measurement integrity).
  * `CL` covers vocabulary mapping quality and ontology mapping quality.

#### B.3:4.6 - Scale discipline (CHR guard‑rails)

To prevent silent misuse:

* **Ordinal scales (F, CL):** never average or subtract; use only `min`, `max`, thresholds, and monotone comparisons defined for ordinal scale values.
* **Coverage scales (G):** use union and intersection in a declared domain space; do not “average” sets. If a numeric proxy is used (e.g., coverage ratio), it **must** be derived from a set operation, not vice versa.
* **Ratio scales (R):** may be combined with `min`, `max`, or explicitly justified conservative functions; do not combine values across different target claims, effective ReferenceSchemes, scopes, assumption sets, or windows without an exact admitted comparison/translation rule.

#### B.3:4.7 - What improves the tuple (improvement-pattern overview)

B.3 remains neutral about *how* improvement happens, but for didactic clarity:

* **Raise F:** formalize narratives (specifications, machine‑checked models).
* **Raise G:** enlarge evidence-covered span (new test regimes, new populations) with adequate evidence.
* **Raise R:** replicate, calibrate, tighten measurement error, reduce bias.
* **Raise CL:** reconcile vocabularies, align units, formalize mappings, verify interface Standards.

Each improvement may involve an admitted System, one local system-role kind, an assignment occurrence and its declared `U.SystemRoleAssignment` species, a `U.Method` or `U.MethodDescription` change, evidence-producing `U.Work`, and an improvement move. Keep those values separate: the assignment establishes neither Work, capability, authority, nor responsibility. Their run-time counterparts are covered by temporal evidence and work-cost evidence under the relevant temporal and Work patterns.

#### B.3:4.8 - Prohibition (normative) — F–G–R is not a CharacteristicSpace

Do not treat `⟨F,G,R⟩` as a `U.CharacteristicSpace` and do not define geometric **trajectories** over it. Use **ESG** for episteme state and the **assurance‑trace** hooks for trends in assurance tuples.

#### B.3:4.9 - Assurance consequence for unsupported causal-use claims

`B.3` consumes `CausalUseSupportVerdict`, `CausalEvidenceSupportBasis`, and relevant profile refs from `C.28` and `A.10` when an assurance claim depends on a `C.28` causal-use verdict:

```text
CausalUseSupportVerdict = supported | bounded | unsupported | abstain
```

`CausalAssuranceTupleTrigger` is narrower than local causal-use repair. A local `C.28` downgrade, redirection to a relation governing the asserted use, or abstain disposition does not require a new `B.3` assurance tuple by itself. Create or update a `B.3` tuple only when the causal-use claim is assurance-bearing, publication-bearing, release-bearing, or reused as an input to assurance, trust, certification, risk acceptance, or downstream selection. Exploratory causal wording, local causal wording repair, or a `C.28` cheap stop remains outside `B.3` until it changes assurance or publication use.

An unsupported causal-use shift lowers, blocks, or abstains from `R` for the affected causal-use claim. If `CounterfactualSamplingRealizabilityProfile.verdict = nonrealizable`, `B.3` lowers or blocks `R` for claims that require direct counterfactual-comparison sampling evidence. If `CounterfactualSamplingRealizabilityProfile.verdict = unknown`, direct-realization claims are unsupported, while identified, bounded, or simulation-only bounded use may remain available when `C.28` declares the bounded use and unsupported use.

Verdict consequences:

| `CausalUseSupportVerdict` | Assurance consequence | Bounded assurance wording |
| --- | --- | --- |
| `supported` | The causal-use claim contributes to `R` only inside the named `CausalUseSupportStatement`, scope `G`, `CausalEvidenceSupportBasis`, and cited profile refs. | "Supported only for the declared causal use under the cited `CausalEvidenceSupportBasis`, profile refs, and scope." |
| `bounded` | `R` is bounded to the declared bounded-use limit; assurance prose must name the bound, the `CausalUseSupportStatement`, and the `CausalUseUnsupportedStatement`, and must not imply unqualified causal use outside them. | "Bounded causal-use claim for the declared regime, population, policy, model, or window; unsupported outside that bound." |
| `unsupported` | The causal-use claim cannot raise `R`; it becomes `CausalUseUnsupportedStatement`, is downgraded, removed, or blocks the assurance claim when the causal use is necessary. | "Causal use unsupported for this assurance claim; use association-only, metric-only, or simulation-only wording or block the causal assurance claim." |
| `abstain` | No causal-use conclusion contributes to `R`; the assurance tuple either proceeds only on named non-causal grounds or abstains from the affected causal claim. | "No causal-use conclusion is used; assurance proceeds only on named non-causal grounds or abstains from this causal claim." |

What changes in practice: assurance prose cannot say "high confidence that the policy caused improvement" when the evidence-provenance path only evidences association or simulation-only counterfactual output; the unsupported causal-use step must degrade, abstain, or block the causal-use claim.

What this does not authorize: `B.3` does not determine the `C.28` target `CausalityLadderRung`, estimand, causal identification, evidence design, or realizability profile; it applies assurance consequences to the `CausalUseSupportVerdict` supplied by `C.28` and the evidence-provenance path supplied by `A.10`.

### B.3:5 - Proof obligations for an assurance-result claim

These obligations adapt the current B.1 and B.1.1 dependency-structure and relation-grounding checks for B.3 outputs. They are checks applied in dated assurance-assessment work; their pass/fail claims, witnesses, and optional record remain distinct from both the work and the assurance-result claim. Each Γ-flavour whose result is consumed by a B.3 assurance assessment supplies the applicable basis below; Γ does not emit assurance by itself.

#### B.3:5.1 - Common obligations (all Γ-flavours)

* **ASS-CLM (Exact target claim and use).**
  Name `E_C`, its ClaimGraph, EntityOfConcern, effective ReferenceScheme and direct subject-result governor; then name `U_A`, `G_A`, assumption/condition refs, and `T_A`. Do not use a title, carrier, holon label, generic context, or status value as the target claim.

* **ASS-WRK (Assessment and result separation).**
  Name the dated assessment work, performer assignment, enacted method, exact rule/application bindings, input-result claims, assurance-result episteme, witnesses or calculation traces, and any optional record/publication separately. A rule, record, or witness does not perform the check or become the result.

* **ASS-EVD (Evidence-use and warrant separation).**
  Cite each exact A.2.4 evidence-use relation and the minimum A.10/G.6 path needed for `U_A`. State polarity, scope, window, rival explanation, reliance disposition, and unsupported use. Evidence availability or loss may change warrant without changing target truth.

* **ASS-SCA (Scale discipline).**
  Declare the scale kind and exact bearer for each value: `F` ordinal, `G` set-valued scope, `R` ratio or declared conservative ordinal proxy, and `CL` ordinal on an exact integration relation. Confirm that every aggregation operation is defined for that scale kind.

* **ASS-WLNK (Weakest-link basis).**
  Identify the exact cutset or the declared premise/lemma path, distinguish them when both are used, and cite the input result/evidence-use refs that cap `F`, `G`, and `R`; graph membership alone supplies none of them.

* **ASS-CL (Congruence on integration dependency).**
  Identify every direct integration relation occurrence on the relevant path and the exact `CL_min` used in `Φ(CL_min)`. A mapping label, Card, or description is insufficient.

* **ASS-MAN (Replayable assurance record).**
  If a reusable record is needed, let it cite `E_C`, `U_A`, `RS_A`, `G_A`, `T_A`, all input result claims and evidence-use refs, F/G/R/CL values and bearers, assessment work and application refs, witnesses, limitations, decay, and an A.10/G.6 path. Include exact `OrderSpec` or `TimeWindow` refs when current. The record neither performs the assessment nor creates result truth, assurance, currentness, status, or later reliance.

* **ASS-MONO (Declared monotone characteristics).**
  List the characteristics along which a local input improvement cannot reduce the aggregate, and state the exact target/input identity and scope conditions under which that monotonicity claim holds.

#### B.3:5.2 - Γ\_sys (systems) — additional obligations

* **CORE‑BIC (Interface congruence).**
  Reference the **Boundary‑Inheritance Standard** (BIC) from **B.1.2** and record any interface mismatches; these contribute to `CL_min`.

* **CORE‑ENV (Operating envelope).**
  Specify the domain used for **G** (e.g., load–temperature region) and how coverage is computed (set union constrained by evidence relation).

#### B.3:5.3 - Γ\_epist (epistemes) — additional obligations

* **EPI‑SPN (Entailment path/subgraph).**
  Identify the exact **premise or lemma path/subgraph** for the claim, including its premises or nodes, inference edges, claim endpoint, scope, and rule selecting that path/subgraph; `R_raw = min R_i` is taken only over that declared object, not over arbitrary satellites.

* **EPI‑MAP (Semantic mapping congruence).**
  Point to the exact vocabulary/ontology mapping relation occurrences and the direct assessment results used to assign their `CL` values; a verification status label alone supplies neither the relation nor `CL`.

#### B.3:5.4 - Γ\_ctx and Γ\_method (order‑sensitive) — additional obligations

* **CTX‑ORD (OrderSpec).**
  Attach the partial or total order `σ` and any **join-soundness** conditions (types, preconditions, and postconditions).
  (See B.1.4 for NC‑1..3 invariants; B.1.5 adds duration/capability typing.)

#### B.3:5.5 - Γ\_time (temporal) — additional obligations

* **TIME-COV (Coverage and identity).**
  Show that `PhaseOf` intervals cover the declared window without overlap for the **same phased entity**; justify any gap or overlap explicitly.

> **Note on Γ\_work.**
> Resource spending and efficiency belong in **Γ_work**. Their *measurement integrity* can influence **R** for a claim (e.g., if a reliability figure depends on calibrated energy input), but **costs themselves are not assurance**; keep them in Γ_work and cite their **measurement assurance** as inputs here.

### B.3:6 - Archetypal grounding (worked examples)

#### B.3:6.1 - System archetype — **Battery pack safety claim**

* **Claim `C`:** *Pack P meets discharge current L with thermal safety margin δ in environment K.*
* **Target and assurance use:** exact pack-safety claim episteme under the engineering ReferenceScheme; `G_A` is the load/temperature/airflow/duty-cycle envelope; `T_A = run` for the named operational-safety use.
* **Graph:** Cells `ComponentOf` modules `ComponentOf` pack; BIC exposes main power and thermal interface.
* **Inputs:**

  * `F` for exact module-spec and cell-test claim inputs: module spec F2, cell test F1 → `F_eff = F1`.
  * `G`: operating envelope regions; union constrained by evidence relationed test regimes.
  * `R`: per‑module reliability from test data; cutset is **hot‑spot path** near weakest cell.
  * `CL`: interface congruence (sensor calibration CL2; thermal contact CL1).
* **Aggregation:**

  * `R_raw = min R_i` along the thermal cutset.
  * `R_eff = max(0, R_raw − Φ(CL_min=CL1))`.
  * `G_eff`: union of evidence-covered (L,T) rectangles, dropping regions lacking validated thermal data.
  * `F_eff = min(F_cell=F1, F_module=F2) = F1`.
* **Assessment and record boundary:** dated safety-assessment work consumes the exact calibration/test input-result claims and A.2.4 evidence-use refs; its B.3 result episteme states the tuple, witnesses show the calculation, and an optional record cites the BIC and A.10/G.6 path.
* **Improvement move:** raise `CL` (better thermal interface verification), raise `F` (formal thermal model), add evidenced envelope -> **R_eff** and **G_eff** increase monotonically.

#### B.3:6.2 - Episteme archetype — **Meta-analysis claim**

* **Claim `C`:** *Intervention X reduces outcome O by Δ on population P.*
* **Target and assurance use:** exact meta-analysis claim episteme under the analysis ReferenceScheme; inclusion/exclusion criteria and measurement protocol are condition refs, `G_A` is population/scope, and `T_A = design` for the named evidential-credibility use.
* **Graph:** Studies `MemberOf` evidence corpus; effect models `ConstituentOf` synthesis; mappings align different outcome scales.
* **Inputs:**

  * `F`: two RCTs at F3, one observational at F2 -> `F_eff = F2`.
  * `R`: replication quality per study -> weakest R on the declared entailment path/subgraph caps `R_raw`.
  * `CL`: mapping of scales (CL1 vs CL3).
  * `G`: populations union, but unevidence-covered sub-populations are dropped.
* **Aggregation:**

  * `F_eff = F2` from the weakest study-design evidence relation in the synthesis.
  * `R_eff = max(0, min(R_RCT1, R_RCT2, R_OBS) - Φ(CL_min=CL1))`.
  * `G_eff`: union of evidence-covered sub-populations; out-of-scope groups excluded.
  * `CL_min = CL1` for the exact scale-mapping relation; cite the mapping witness and weakest-link input claim in the assurance record, while the assurance-result episteme remains separate.
* **Assessment and record boundary:** dated credibility-assessment work consumes the exact study/effect input-result claims, A.2.4 evidence-use refs, scale-mapping occurrences, bias result, and any constructive equivalence result; the B.3 result episteme, calculation witness, optional record, and A.10/G.6 provenance path remain distinct.
* **Improvement move:** upgrade mapping verification to CL2 or CL3; increase `F` via registered analysis plan; replicate lagging study.

#### B.3:6.3 - Order-sensitive manufacturing-sequence assurance

* **Claim `C`:** *The domain manufacturing sequence `R`, mapped to an order-sensitive Method/Work sequence with an `OrderSpec`, meets output defect rate <= epsilon.*
* **Target and assurance use:** exact sequence-defect claim episteme; materials and equipment class are condition refs, the manufacturing envelope is `G_A`, and `T_A = run` for the named process-reliability use.
* **Γ_ctx records:** `OrderSpec σ` for the method/work sequence; declared independent branches; join conditions at inspection.
* **Assurance:**

  * `R_raw = min R_step` along the declared order-sensitive dependency path (including inspection effectiveness).
  * Penalty from poor join soundness `CL_min`.
  * Improvement via faster but **verified** inspection (increase `R_step`) or tighter join spec (increase `CL`).

#### B.3:6.4 - Temporal archetype — **Model credibility across exact episteme identities**

* **Claims `C_i`:** each exact model episteme `M_i` carries its own prediction claim and declared applicability window; a receiving assurance use may additionally ask whether the selected claims jointly support prediction within ±δ over τ.
* **Target and assurance use:** each exact model claim keeps its own effective ReferenceScheme and window; the selected data regime and drift tolerance are condition refs, and the joint prediction-credibility use declares its own `G_A` and `T_A = run`.
* **C.2.1 identity and continuity:** compare the exact claim content, EntityOfConcern, and effective ReferenceScheme for the items labelled v1, v2, and v3. A changed discriminator identifies another episteme. Assert `EpistemeEditionRelation(M_v1,M_v2)` or `EpistemeEditionRelation(M_v2,M_v3)` only when each ordered pair satisfies C.2.1's independent historical-continuation predicate; labels, revision Work, provenance, publication order, and common lineage establish neither occurrence.
* **Temporal aggregation:** a B.1.4/Γ\_time record may order those already recovered edition relations, applicability windows, or publication windows for the bounded assurance use. It does not turn the distinct epistemes into `PhaseOf` slices. If one exact episteme instead remains unchanged and the use needs proper interval restrictions, A.14 `PhaseOf(M@τ_i,M)` remains available and B.3 `TIME-COV` applies to that same phased entity.
* **Assurance:**

  * compute `R_raw = min(R_C1, R_C2, R_C3)` only when the named assurance use actually consumes all three exact edition-specific claims and their evidence relations;
  * apply the declared penalty when the mapping or calibration congruence between the edition-specific prediction/evidence bases is low;
  * re-calibration or a new validation campaign may improve the exact supported claim, mapping, or evidence relation, but creates neither episteme identity, edition continuity, currentness, nor publication availability; and
  * a non-continuing replacement receives an independent assurance assessment and inherits no `F`, `G`, `R`, `CL`, evidence, or reliance result by label.

### B.3:6.5 - Bias-Annotation

B.3 deliberately biases assurance toward conservative aggregation and explicit reliance use. This prevents dashboards, labels, badges, credentials, model cards, provenance marks, or generated confidence phrases from raising trust by appearance. The cost is that assurance claims need typed evidence, scope, limitations, decay, and contestability when they are used for readiness, safety, compliance, release confidence, or other material reliance.

### B.3:7 - Conformance checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| **CC-B3.1** | The assurance result is a C.2.1 claim episteme stating `AssuranceResult(E_C, U_A &#124; RS_A, G_A, T_A)` for one exact target-claim episteme and use. | Prevent target, use, interpretation, scope, and time drift. |
| **CC-B3.2** | `F` is ordinal and uses thresholds or `min`; `G` is a USM scope value and uses membership, intersection along essential paths, and `SpanUnion` only across independent evidence lines; `R` is ratio and uses `min` plus conservative operations. | Preserve scale integrity (CHR and USM). |
| **CC-B3.3** | Each `CL` qualifies one exact admitted integration relation occurrence; `Φ(CL)` is monotone decreasing and bounded (`R_eff ≥ 0`). | Make integration quality first-class without letting a graph edge or label create it. |
| **CC-B3.4** | `R_eff = max(0, min_i R_i - Φ(CL_min))` for the relevant integration dependency paths, unless a stricter domain-specific rule is justified. | Enforce WLNK and penalize low-CL integrations. |
| **CC-B3.5** | For `G`, essential dependency paths compose by intersection; `SpanUnion` applies only across explicitly independent evidence lines to the same claim and only over evidenced slices. | Prevent over-generalization. |
| **CC-B3.6** | Any reusable assurance record cites target/input claims, value bearers, exact integration relations, assessment work/application refs, evidence-use/provenance refs, witnesses, scope/window, limitations, decay, and currentness refs; the record performs no work and creates no result. | Keep replay, result, work, evidence, and currentness distinct. |
| **CC-B3.7** | Agency-characteristic values under A.13 and the A.17/A.18/A.19/C.16/A.10 characterization-and-evidence stack do not override WLNK or `Φ(CL)` penalties; if agency grade change alters capabilities, model it as a Meta-Holon Transition. Planned C.9 may later consolidate the profile but supplies no current governing force. | Preserve safety; keep agency separate. |
| **CC-B3.8** | Design and run assurance uses have separate `T_A`, condition sets, scopes, evidence windows, assessments, and result claims; compare rather than merge them. | Avoid design/run chimeras. |
| **CC-B3.9** | If an assurance claim depends on a `C.28` causal-use verdict, it consumes `CausalUseSupportVerdict`, `CausalEvidenceSupportBasis`, and relevant profile refs from `C.28` or `A.10`; a causal-use claim whose C.28 verdict is unsupported degrades, blocks, or abstains rather than raising `R`. | Prevent assurance prose from certifying unsupported causal claims. |
| **CC-B3.10** | A local C.28 downgrade, redirected use, or abstention is not a new B.3 assessment/result trigger unless the exact claim is assurance-, publication-, release-bearing, or reused as an assurance input. | Keep cheap causal triage from becoming assurance ceremony. |
| **CC-B3.11** | A label, badge, dashboard, credential, provenance mark, model/data card, assurance document, attestation, or generated phrase raises no assurance unless exact `E_C`, `U_A`, assessment, input-result and A.2.4 evidence-use refs, A.10/G.6 path, argument, limitations, disposition, decay, and reopen condition support a typed assurance-result claim. | Block visible authority from supplying target truth or assurance. |
| **CC-B3.12** | When reliance may materially change behavior, safety, release, compliance, access, resources, people/team status use, operational action, or controlled-entity regulation, constitute the assurance-result claim or explicitly narrow, degrade, abstain, request evidence, reopen, or block; an optional `RelianceSafetyCase` record only cites that result and basis. | Keep consequential assurance concrete without turning the record into authority. |
| **CC-B3.13** | Target/world-side result, target-claim episteme, assessment work, input results, assurance-result episteme, witnesses, record, publication, and later reliance/status/gate/decision remain independently recoverable. | Prevent result and process collapse. |
| **CC-B3.14** | Evidence availability, provenance, or a successful check may alter warrant and assurance disposition but does not create target truth; absence of evidence is not a negative target result. | Preserve the world/claim/warrant boundary. |
| **CC-B3.15** | F.10 defines the status value and its use; cite any domain-specific status rule only for the concrete contribution it makes. Assurance does not define the target, approve a standard, satisfy a requirement, pass a gate, grant permission, or prove actual reliance. | Preserve the assurance/status/use boundary. |

### B.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Averaging assurance** | Mean of `R_i` reported as system reliability | Use `min R_i` on the cutset, then apply `Φ(CL_min)`. |
| **Ordinal arithmetic** | Averaging `F` or `CL` to produce “2.3” | Use `min` or `max` or thresholds; never average ordinals. |
| **Coverage as centroid** | Replacing `G` union with a single “typical point” | Keep `G` as set and coverage; if a numeric proxy is needed, derive it from the set. |
| **Ignoring congruence** | No penalty for low-CL mappings or interfaces | Assign `CL` to integration edges and apply `Φ(CL_min)`. |
| **DesignRunTag chimera** | “One score” mixing blueprint and telemetry | Split into `S=design` and `S=run` tuples; compare explicitly. |
| **Agency override** | Claiming higher assurance because a controller is “clever” | Agency may justify how improvements are achieved; it cannot remove WLNK or `Φ`. |
| **MemberOf as stock** | Using `MemberOf` to sum reliabilities | Keep `MemberOf` for collections; reliability comes from the relevant Γ composition, such as the Γ_sys cutset. |
| **False assurance by display** | A badge, dashboard color, credential, provenance label, model/data card, assurance document, attestation, or phrase is used as assurance. | Keep it as orientation/source material unless an exact assessment and typed assurance-result claim cite the necessary input-result, A.2.4 evidence-use, and A.10/G.6 provenance refs. |
| **Minimum reliance safety assurance record inflation** | Ordinary evidence, source-finding explanation, local CV, documentation, or reversible local calibration use is forced into a safety assurance record; or the record is used as approval, release permission, gate passage, safety acceptance, or compliance proof. | State the material-reliance trigger. If absent, return the case to the exact evidence, source, status, gate, comparison, or local-use rule that answers it. If met, constitute only the assurance-result claim and minimum record/contest-redress support needed for `U_A`. |
| **Evidence creates truth** | Evidence arrival is said to make the target result obtain, or evidence loss is called falsity. | Keep target facts and direct result with their governor; revise only evidence use, warrant, assurance disposition, or reliance unless the subject facts changed. |
| **Assessment-record collapse** | A checklist, calculation, record, witness, or publication is treated as assessment work or its result. | Name dated work/application, result-claim episteme, witness, record, and publication separately. |
| **Status as assurance** | Approved/current/ready/compliant status defines the target, satisfies a requirement, or proves assurance and release. | Use F.10 for the status value and its use; cite another domain-specific status rule only for its concrete contribution, and constitute a separate B.3 result only when assurance is actually assessed. |

### B.3:9 - Consequences

**Benefits**

* **Comparable, conservative, improvable.** The tuple ⟨F, G, R⟩ with **edge-scoped Congruence Level (`CL`) values** gives a compact, auditable view that improves monotonically under targeted moves (formalize, replicate, reconcile).
* **Cross-scale coherence.** Works for assemblies and arguments, methods and histories, without leaking order, time, or cost into structure.
* **Clear improvement moves.** It is obvious what to do to raise each component: raise `F`, `G`, or `R` locally, or raise `CL` on the integration edge.

**Trade‑offs**

* **More explicit metadata.** You must state scale kinds, cutsets, and mapping congruence; this is intentional transparency.
* **Conservatism may feel pessimistic.** True synergy appears only via **MHT** or after raising CL—never by arithmetic optimism.

### B.3:10 - Rationale

B.3 combines a conservative weakest-supported-part calculus with current assurance-case and assurance-documentation practice. The current comparators below govern only the decisions B.3 actually imports; older and popular sources remain lineage rather than authority by recency, prestige, or display.

### B.3:10.1 - SoTA-Echoing

* **Assurance by weakest link** reflects reliability engineering and safety cases in complex systems; composing assurance evidence by minima prevents over‑statement.
* **Formality and verifiability** mirror advances in model‑based engineering and formal verification, where raising F turns subjective arguments into verifiable records.
* **Coverage as set and measure** follows evidence synthesis and validation practice that treat applicability as a domain region, not a scalar to “average.”
* **Congruence on edges** captures what meta‑analysis, interface control, and ontology alignment have repeatedly shown: integration quality is often the real bottleneck. Penalizing low‑CL is a principled way to prevent silent over‑confidence while rewarding verified reconciliation.
* **Assurance documentation, provenance, and release-status practice** treats labels, model cards, datasheets, C2PA provenance marks, SLSA and in-toto attestations, credential displays, generated confidence phrases, and dashboards as scoped documentation or source pointers, not automatic assurance claims. B.3 adopts claim, argument, and evidence discipline and scoped assurance-documentation use, adapts model cards, datasheets, data cards, attestations, provenance marks, dashboards, and generated confidence phrases as possible documentation or evidence inputs for a named assurance claim, and rejects visible-label promotion into readiness, compliance, safety, trust, `R`, `F`, `G`, `CL`, or release confidence without a typed tuple and A.10 evidence-provenance path.

**Decision-bearing currentness account (qualified through 2026-08-04).**

| Practice question | Current comparator and alternative status | Adopt, adapt, or reject; concrete B.3 mutation | Smallest reopen trigger |
| --- | --- | --- | --- |
| What must an assurance or safety case contribute to a reliance claim? | ISO/IEC/IEEE 15026-2:2022, edition 2, is the published current assurance-case structural standard and replaced the withdrawn 2011 edition. The Safety-Critical Systems Club identifies the *GSN Community Standard* v3 (2021) as its latest notation and current-best-practice guidance for engineering arguments; ISO 15026-2:2011 and GSN v1-v2 are lineage, while a diagram or document merely called a safety case is only a popular form. | **Adopt** explicit claims, arguments, evidence, and maintenance. **Adapt** them into the typed B.3 result, F-G-R and edge-scoped CL, the threshold-bounded minimum record in 4.2b, and the proof obligations in 5. **Reject** case-document appearance as target truth, approval, gate passage, permission, release, or safety acceptance. | Reopen this row if a successor edition changes the required claim-argument-evidence structure or maintenance relation in a way that conflicts with B.3, or if current use evidence shows that one field or branch of the minimum record is necessary, invalid, or misleading for the named reliance use. |
| What may an assurance-documentation, provenance, or attestation artifact establish? | C2PA Content Credentials 2.4 (April 2026), SLSA 1.2 (approved, November 2025), and the in-toto Attestation Framework 1.2 (March 2026) are the current engineering comparators for the narrow provenance-and-attestation question. Model Cards (2019), Datasheets for Datasets (2021), Data Cards (2022), badges, dashboards, and credential displays remain useful documentation lineages or popular presentation forms, not current assurance verdicts. | **Adopt** exact subjects, sources, bindings, authenticated statements, provenance, and verification against declared expectations. **Adapt** those artifacts in 4.2a-4.2b as possible documentation or A.10 evidence-provenance inputs to one named B.3 claim. **Reject** a valid signature, manifest, attestation, card, badge, or display as automatic F, G, R, CL, target truth, safety, compliance, readiness, or release. | Reopen only the affected documentation branch if a successor specification changes the property actually warranted or the boundary between artifact, verifier expectation, and reliance, or if validated practice evidence shows that one named documentation kind itself supplies—or cannot supply—a required typed contribution for the declared use. |

Practical result from that safety-case and assurance-documentation practice: safety notes, compliance-looking labels, assurance documents, dashboards, provenance marks, model cards, datasheets, data cards, and generated confidence phrases do not become certificates, approvals, gates, safety acceptance, or assurance by appearance. The local B.3 output is one typed assurance-result claim plus, only when useful, a minimum reliance safety assurance record that cites its assessment, A.2.4 evidence-use and A.10/G.6 provenance basis, assumptions, limitations, defeaters, residual uncertainty, monitoring or stop condition, contest/redress relation, bounded assurance use, unsupported use, and exact reopen conditions.

This arrangement preserves **A.11 Parsimony** and aligns with **A.14**, **A.7**, and **A.15** while leaving each domain to supply its exact ReferenceScheme, ClaimScope, conditions, windows, subject results, and use relations without breaking the calculus invariants.

### B.3:11 - Relations

* **Builds on:** C.2.1 for target and assurance-result epistemes; A.2.4 for exact evidence-use classification; A.10/G.6 for source-provenance paths and bounded reliance; A.15.1/A.6.1 for assessment work and applications; B.1/B.1.1 and the current system-composition, temporal, work, and relation patterns for exact input structures and occurrences; A.2.6 for ClaimScope; C.16/C.16.Q for scale/value discipline where applicable; and C.13 for Compose-CAL.
* **Coordinates with:** **E.14 (Human‑Centric Working‑Model)** for publication-facing assertion discipline and **B.3.5 (CT2R‑LOG)** for Working‑Model relation label-meaning and grounding (`tv:*`, `validationMode`).
* **Coordinates with:** `C.28` for `CausalUseSupportVerdict`, `CausalityLadderRung`, `CausalEvidenceSupportBasis`, identification profile refs, realizability profile refs, supported causal use, and unsupported causal use; `A.10` for the evidence-provenance graph path carrying causal-evidence refs.
* **Coordinates with:** `F.10` for status values and their use; `G.11` for currentness; `A.15` for work/reliance disposition; `A.21` for gates; `A.20` for constraint-validity results; permission, commitment, release, and decision patterns for their own results; E.17/E.24.PUB and C.29 for publication/representation; and A.15.PROD only when a separately current inception claim is needed. Cite another domain definition or test only for the concrete contribution it makes to the assurance argument. B.3 governs the assurance-result claim, not those neighboring objects.
* **Used by:** KD-CAL improvement patterns (to plan improvements), B.4 (Evolution loops that raise `F`, `G`, `R`, or `CL` over time).
* **Triggers:** B.2 (Meta‑Holon Transition (MHT): Recognizing Emergence and Re‑identifying Wholes) when genuine new capabilities emerge that change the applicable cutsets or envelopes.

> **One‑page takeaway.**
> Report assurance as a distinct `AssuranceResult(E_C, U_A | RS_A, G_A, T_A)` claim with **⟨F, G, R⟩** and exact edge-scoped `CL` basis; keep the target fact, evidence use, assessment work, witness, record, publication, status, and later reliance separate.
> Improve assurance by raising **F**, **G**, **R**, or **CL**—and keep order, time, and cost in their own lanes.

### B.3:11a - Assurance relation for quantum-like claims

Quantum-like wording does not raise the claim-assurance requirement by default. A local `C.26` modeling note can remain lightweight when it only prevents a representational mistake and is not used for a work-guiding use, reliance use, audit-closure claim, readiness-certification claim, or empirical-superiority claim.

Assurance-relation checks:

1. Decide the claim-assurance requirement before building assurance machinery.
2. If the QL note only prevents a local misinterpretation, keep it as QL-lite with ordinary evidence.
3. If the claim will be reused, state the exact target-claim episteme, named use, local stop condition, A.2.4 evidence-use relations, and A.10/G.6 provenance refs. Add the concrete domain definition, comparison rule, or currentness test only when it changes the reusable claim.
4. If the reuse is for release, readiness, audit, compliance, safety, assurance, or other threshold-bearing reliance, perform the B.3 assessment and constitute a separate assurance-result claim over the exact input results, evidence uses, scope, time window, argument, limitations, disposition, and reopen condition.
5. If the claim says QL is better, faster, more accurate, or uniquely necessary, compare rival models, baseline, claimed mechanism, scope, and loss.
6. State decay conditions and reopen conditions so an old QL-evidenced assurance claim does not silently stay current after new validation observations, changed source records, changed evidence refs, or scope change.

| Claim-use requirement | B.3 expectation | Output |
| --- | --- | --- |
| Local modeling note | No assurance tuple beyond the ordinary pattern and evidence note | QL-lite note with local stop |
| Reusable example or pattern-facing note | Name the concrete domain definition, comparison rule, or currentness test only when it changes the reusable claim; keep the local stop condition and evidence-use or evidence-provenance condition explicit. | Reusable example with bounded source and use relations |
| Decision, release, audit, readiness, or compliance use | Provide exact target/use, assessment, `F/G/R`, congruence-occurrence refs, evidence-use/provenance refs, rival explanations, decay, and reopen condition | Assurance-result claim plus optional citing record |
| Comparative superiority claim | Add rival-model comparison, baseline, claimed mechanism, and scope limits | Bounded superiority claim or apply the FPF pattern that defines or constrains the comparison being claimed |

Useful outputs:

- no B.3 assurance use when QL is only a local representational lens;
- a compact bounded assurance claim statement when reuse is modest;
- a full assurance-result claim only when consequence severity or explicit F/G/R/CL reuse demands it;
- a rejected, narrowed, or withdrawn claim when evidence does not carry the claimed assurance use or relying context.

### B.3:11b - C.29 mathematical-lens use relation

> If a mathematical lens is used as input to assurance, readiness, reliability, release confidence, safety, trust, or engineering justification, B.3 constitutes a separate assurance-result claim for the exact lens-result claim and named use, citing the relevant A.2.4 evidence-use and A.10/G.6 provenance refs plus residual-use limits. A `C.29` output remains a lens-use result; mathematical elegance, validation regime, or a declared structure-preserving mapping does not raise assurance by itself. Measurement construction and comparability remain `C.16`.

### B.3:End

