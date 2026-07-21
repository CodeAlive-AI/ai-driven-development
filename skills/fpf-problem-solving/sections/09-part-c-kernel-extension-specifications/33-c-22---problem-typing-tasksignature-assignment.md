## C.22 - Problem Typing & TaskSignature Assignment (Problem-CHR)
> **Status:** Stable
> **Type:** Calculus (C)

**Purpose.** Give FPF an admissible, minimal, and portable `TaskSignature@Context` declaration for selector-facing use after the problem-side representation is stable enough for Principles-to-Work, eligibility, acceptance, or policy-governed choice. `C.22.2` carries the first problem-framing episteme for a messy signal. `C.22` constructs one CHR-grounded `U.Signature` species and, when a receiving use is current, relates the exact problem-side episteme to that signature through `TaskSignatureAssignmentRelation@Context`. The signature is Context-local, evidence-relation-traceable, tri-state-aware, and bridge-visible.

**Body-level kind boundary.** `TaskSignature@Context` is a Context-local species of existing `U.Signature`, governed here and conformant to the A.6.0 four-row declaration; it is not a record format and introduces no new root U-kind. `TaskSignatureAssignmentRelation@Context` is the local `U.Relation` that assigns one such signature to one exact problem-side episteme for one receiving use. `ProblemCard@Context` is the C.22.2 problem-side episteme used before that assignment. `KindSet` contains C.3 `U.Kind` values for selected entities. Descriptor maps, telemetry hooks, policy ids, and selector fields remain local signature vocabulary or projection fields unless a direct governing pattern admits another kind.

**Primary EntityOfConcern.** The governed value in C.22 is one `TaskSignature@Context`, a Context-local `U.Signature` declaration that makes a typed task or work target usable by later eligibility, acceptance, and selector relations. `TaskSignatureAssignmentRelation@Context` is a separate dependent relation to the upstream problem-side episteme and receiving use. `TaskKind`, optional `TaskFamilyRef`, `KindSet`, characteristic bindings, and scope slices are content of the signature's four-row declaration. A later `SelectorOutcome` is a downstream result. A project-entity reference inside a scope relation identifies the entity addressed by the task; it is not the TaskSignature or its publication.

**Placement.** Part C (Kernel Extensions Specifications) -> Cluster C.I (Core CHRs and CALs).
**Depends on:** **C.16 MM-CHR** (measurement admissibility), **G.5** (selector S2 and S3), **G.0** (CG-Spec invariants).
**Coordinates with:** **G.4** (Acceptance and Evidence profiles), **C.23** (MethodFamily admissibility and maturity), **C.18 NQD‑CAL** (QD and illumination), **C.19 E/E‑LOG** (emitters and policies), **E.10** (LEX).

### C.22:0 - Use This When

Use this pattern when a stabilized problem-side episteme must be related to a selector-facing `TaskSignature@Context` for eligibility, acceptance, or policy-governed selection. Typical cases include solver choice, method-family eligibility, QD archive selection, open-ended generator selection, or specialization claims that need a declared task family or work target.

The working moment often sounds like this: "We are about to compare possible ways of doing, but which facts about this problem make a method family eligible, comparable, or unacceptable here?" Use C.22 to construct the smallest four-row `TaskSignature@Context` that a later selector can consume without selecting a method in advance, then assign it to the exact problem-side episteme and receiving use. If problem framing remains contested or stale, use `C.22.2`. If a sufficient signature and assignment already exist and the current question is selection, use `G.5`. If a method is selected and dated enactment is being prepared, use `A.15.2`.

**What goes wrong if missed.** A problem remains a paragraph: selector inputs drift, ordinals and units get mixed, unknowns are coerced, acceptance thresholds leak into CHR fields, and cross-context reuse happens by name instead of Bridge+CL.

**What this buys.** The downstream selection question gets one minimal `TaskSignature@Context` with typed vocabulary, laws, applicability, unknown handling, evidence relations, scope, freshness, and crossing conditions visible before any method family is admitted or compared. Its assignment to the problem-side episteme is replayable, while publication and serialization can vary without changing the signature.

### C.22:1 - Intent

Operationalise No-Free-Lunch discipline in selection by making each selector decision use a typed `TaskSignature@Context`, not a paragraph. A problem reaches C.22 when its problem-side episteme is stable enough to construct and assign that signature without selecting a method in advance. The signature is the smallest CHR-typed A.6.0 declaration sufficient to support eligibility, acceptance, and policy-governed selection without inadmissible arithmetic or silent coercions; the separate assignment relation states which problem-side episteme and receiving use rely on it.

#### C.22:1.1 - Term split used in this pattern

- `TaskSignature` assignment means relating one `TaskSignature@Context` value to one exact problem-side episteme and one receiving selection use through `TaskSignatureAssignmentRelation@Context`; it does not pre-bind a method.
- `ScopeSlice(G)` means the claim-bounding scope cut over `EntityOfConcernRef` and scope; it is not an evidence-path slice and not a baseline-set slice.
- `threshold` is not one undifferentiated family here:
  - articulation and closure thresholds stay with cue or prompt governing patterns such as `B.4.1` and `B.5.2.0`
  - acceptance-gate thresholds stay with `G.4`
  - the work-measure threshold target used in specialization claims is only the declared success mark for the current task family or work target

**Name and kind map for code-shaped heads.** The names below identify different structural positions; capitalization does not make them peer kinds.

| Head used in this pattern | Recoverable kind or position | Direct governance boundary |
| --- | --- | --- |
| `TaskSignature@Context` | Context-local species of `U.Signature` and this pattern's primary EntityOfConcern | C.22 governs its A.6.0 four-row specialization; E.17 governs its publications and carriers. |
| `ProblemSideRecordRef` and `ReceivingUseDescription` | Positions of `TaskSignatureAssignmentRelation@Context`, not content or identity positions of `TaskSignature@Context` | C.22.2 or the direct problem-side pattern governs the problem episteme; the receiving-use description does not prove that the use occurred. |
| `TaskKind` | TaskSignature position filled by one exact C.3 `U.Kind` value that types the current problem or work target | C.3 governs the kind value; the field does not mint `U.Task`. |
| `TaskFamilyRef` | Optional reference position for the comparison-relevant task family | C.22 and C.22.1 govern task-family anchoring; the reference is not the family or a selected method. |
| `ProblemProfile` | `C.2.1`-conformant `U.Episteme` that describes the stabilized problem and may reference the TaskSignature assignment | It is not the problem, TaskSignature, assignment relation, method, plan, or work occurrence. |
| `ScopeSlice(G)` | Local field position whose filler is the current claim-bounding scope relation over the project `EntityOfConcernRef` | A.2.6 governs the scope relation; the field is not an E.18 path slice or a new slice kind. |
| CHR field heads in `5.1` | TaskSignature positions filled by characteristics, scales, units, polarity values, scope values, evidence relations, and currentness conditions | C.16 and each direct subject pattern govern the fillers; C.22 only states why the positions are needed by selector-facing use. |
| QD and OEE extension heads in `5.1` | Optional TaskSignature positions filled by exact characteristic-space, archive, policy, telemetry, generator-family, validity-region, and transfer-rule values or references | C.18, C.19, G.5, G.11, and the named direct patterns keep authority over those fillers. `ArchiveConfig`, `TelemetryHooks`, and `GeneratorIntent` do not become root kinds here. |

#### C.22:1.2 - ProblemCard@Context relation

`ProblemCard@Context` is the `C.22.2` problem-side record shape for stabilizing one context-bound problem representation before downstream Principles-to-Work (P2W).

A `ProblemCard@Context` episteme can be used to prepare the `TaskKind`, scope, and characteristic bindings for a candidate `TaskSignature@Context`. Assignment is admitted only when one signature is adequate for the named receiving use. If several signatures remain plausible, keep them as candidates under the selection or problem-framing pattern rather than asserting one `TaskSignatureAssignmentRelation@Context`.

`TaskSignatureAssignmentRelation@Context` does not move problem-card claims into the TaskSignature. The signature keeps only its four-row task declaration. `ProblemCard@Context` remains the reviewable problem-side episteme that explains why this problem can proceed to characterization, comparison, search, refresh, retirement, or another governing pattern.

The corresponding claims are governed by their named governing patterns.

### C.22:2 - Problem Frame (DesignRunTag split; crossing-visible)

**Selector-facing problem case**
For selector-facing C.22 use, a problem case applies when the problem-side episteme is stable enough to construct a minimal `TaskSignature@Context` and assert its `TaskSignatureAssignmentRelation@Context` for eligibility, acceptance, or policy-governed selection. Method absence or contestability is a common downstream reason, but not the ontology of problemhood. When the live question remains a symptom, contested framing, stale context, set-derived candidate, opportunity cue, or preselected work item, use C.22.2 before asserting one assignment. When selection becomes current, cite the A.19.SelectorMechanism relation and exact G.5 policy refs rather than moving selection policy into the signature.
**Unknown-first discipline.** Author S2 with `unknown` traits rather than coercions. Name the exact downstream policy that interprets a live unknown for the receiving use. C.22 introduces no universal outcome enum; C.23, G.4, G.5, or another direct pattern governs the resulting eligibility, acceptance, or selection disposition.

Untyped "problems" collapse into **informal prose**; selectors cannot **filter or abstain** admissibly; acceptance-gate thresholds leak into scoring; cross-Context reuse is by name, not Bridge. We need a Context-local descriptor that (i) establishes **MM-CHR admissibility** for Scale, Unit, and Polarity before aggregation, (ii) records **Assurance lanes TA, VA, and LA** per **A.10** and **ReferencePlane**, (iii) carries **tri-state unknowns** explicitly, and (iv) records crossing attestations (**BridgeCard plus UTS row**) with **Φ(CL) and Φ_plane** policy ids.

### C.22:3 - Problem

Without typed descriptors, **Eligibility and Acceptance** degenerate into prose; **inadmissible operations** creep in (ordinal means; unit mixing); **cross-plane comparisons** lose **CL and Φ** penalty assignment (**penalties to R_eff only**).

### C.22:4 - Forces

| Force                        | Tension                                                                                                                           |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Parsimony vs sufficiency** | Fewer fields to avoid ceremony **vs** enough to drive admissible gating.                                                              |
| **Unknowns**                 | Many traits are **unknown** in the initial problem record → tri-state semantics propagate to Acceptance without silent coercions.                |
| **CHR admissibility**             | **No mean on ordinals; no unit mixing**; aggregation is admissible only after polarity and scale type are declared.                             |
| **Locality vs portability**  | The problem is **in-room**; cross-context reuse proceeds **through Bridges**, with **CL** and (if planes differ) **CL^plane** penalties → **R** only. |

### C.22:5 - Solution — Problem CHR, `TaskSignature@Context`, and assignment relation

**Local TaskSignature mantra.** *Stabilize the problem; name the receiving selection question and task kind; keep only traits that can change eligibility, acceptance, or selection; type each live trait; preserve unknowns, evidence relations, scope, and currentness; declare the TaskSignature, assign it to the problem-side episteme for that use, and stop before selecting a method.* This is a short repeatable rendering of the C.22 Solution. It is not a selector algorithm, method recommendation, work plan, dated selection occurrence, or `DemonstrativeUnfoldingSlice@Context`.

Apply that formula as follows:

1. Confirm that the problem-side representation is stable enough for selector-facing use; otherwise return to `C.22.2`.
2. Name the receiving eligibility, acceptance, or selection question and the `TaskKind`, optional task family, or work target that the signature will declare.
3. Include only the problem traits whose values can change that receiving use. Leave a non-current optional extension absent.
4. Type each live characteristic by scale, unit, polarity, reference plane, and admitted comparison relation before aggregation or comparison.
5. Preserve a live but unknown value as `unknown`; include or reference the exact scope, evidence relation, freshness or edition condition, and crossing relation on which later use relies.
6. Close with one minimal `TaskSignature`. Pass later eligibility and acceptance claims to `C.23` and `G.4`, and actual method-family selection to `G.5`; do not put their outcomes back into the signature as if they were problem traits.

#### C.22:5.0a - Positive closure, bounded non-use, and local return

Close the C.22 use positively when the four-row TaskSignature declaration is complete and `TaskSignatureAssignmentRelation@Context` recovers the stabilized problem-side episteme, bounded Context, exact signature edition, and receiving use. Each live characteristic has its scale, unit, polarity, reference plane, admitted comparison relation, and value or explicit `unknown`; every relied-on evidence, freshness, edition, or crossing relation is named. A downstream selector can now consume the assigned signature without guessing, but no eligibility verdict, acceptance result, method recommendation, selector outcome, work plan, or dated work is claimed.

Close by bounded non-use when problem framing is not stable enough for a TaskSignature declaration, when no selector-facing receiving use is current, or when the current question has already become eligibility, acceptance, selection, planning, or performed work. A non-current optional extension remains absent. If several signatures or assignment relations remain plausible, preserve them as candidates under the governing problem or selection pattern rather than asserting one assignment.

Return to the smallest affected TaskSignature position when its receiving question, Context, `TaskKind`, task-family or work-target reference, project subject or scope, characteristic meaning, scale, unit, polarity, reference plane, unknown status, evidence relation, freshness condition, edition, or crossing relation changes. Keep the upstream `ProblemCard@Context` and downstream selection history unchanged unless the changed relation actually invalidates them under their own governing patterns.

**Worked local repair.** A machining TaskSignature originally records surface finish as an ordinal visual grade. The receiving use later adopts measured roughness `Ra` on a ratio scale in micrometres with a named measurement and evidence relation. Repair the affected characteristic head, scale, unit, admitted comparisons, and evidence relation. Keep the machining `TaskKind`, unaffected constraints, scope, and prior work history. Reopen eligibility, acceptance, or method-family selection only when its earlier result relied on the replaced finish head; the direct downstream pattern decides the new result.

#### C.22:5.0b - Apparatus proportionality

Use the lightest signature declaration and assignment relation that the named receiving use can consume:

1. **Minimal selector-facing use.** Materialize one TaskSignature with only the live fields needed by the current eligibility, acceptance, or selection question. This is the ordinary positive result of C.22.
2. **Reliance-bearing use.** Add an addressable `ProblemProfile` episteme only when delayed feedback, audit, transfer, automation, expensive reversal, or another named use relies on replay beyond the local assignment relation. Pin the exact problem-side episteme and edition, TaskSignature edition, receiving use, every field-basis relation with its direct governing pattern, qualification window, review trigger, and any current evidence, currentness, or crossing relation.
3. **Extension-bearing use.** Add QD, OEE, archive, generator, parity, or specialization positions only when that exact downstream relation is current and its direct pattern requires those values.

More fields, publication packaging, name cards, or telemetry do not make the problem better formulated, the TaskSignature more true, or a method more suitable. If no selector-facing receiving use needs a TaskSignature, close by bounded non-use rather than publishing a thin declaration for its own sake.

#### C.22:5.1 - Minimal CHR fields (tri‑state aware).
**Selector-side field boundary.** The fields below are live only after problem framing has been stabilized enough to ask eligibility, acceptance, selection, method-family, or policy-governed choice questions. They are not a universal problem-framing checklist and do not replace the `C.22.2` Thin `ProblemCard@Context` pass for a messy signal. Each live characteristic field is **CHR-typed** by Characteristic, Scale, Unit, and Polarity under MM-CHR discipline. A live predicate may preserve `unknown` when its direct pattern admits that value; the cited downstream policy governs what follows. This aligns G.4 and G.6 without making their results C.22 values.

**Optional extension absence rule.** If QD, OEE, archive, generator, parity, specialization, or another optional relation is not live for the current case, the corresponding optional fields are absent, not `unknown`. Use `unknown` only for a live field whose value is currently unknown. An absent non-live extension triggers no downstream disposition.

* **`DataShape`** — data regime and admissible transforms (e.g., tabular, sequence, graph; density; stationarity claims).
* **`NoiseModel`** — uncertainty class and robustness envelope (e.g., iid Gaussian; heavy‑tailed; adversarial budget).
* **`ObjectiveProfile`** — objective heads (**Scale, Unit, Polarity** and **ReferencePlane** declared), polarity, and **admissible order relations** (lexicographic, Pareto, medoid or median where admissible). **Weighted sums across mixed scale types are inadmissible**; ordinal heads use order-only guards. For QD tasks, explicitly enumerate quality heads, diversity or descriptor-space heads, and any policy-authorized QD contribution heads; see **DominanceRegime** below. Do not introduce a default QD score. If a scalar or set-scalarization policy is live, cite the governing CAL policy and keep dominance and telemetry roles explicit.
* `RegularityTraits` — method-relevant structure (**convexity, differentiability, separability, monotonicity**) as CHR-typed predicates with guard macros (for example, `ORD_COMPARE_ONLY`, `UNIT_CHECK`, `POLARITY_CHECK`). Include `ConditionClass` such as stiffness or kappa proxies where applicable.
* **`Constraints`** — explicit hard and soft constraint classes (feasibility predicates; **ResourceEnvelope** and **RiskEnvelope**). **Acceptance-gate thresholds live in `G.4` only; never inside CHR or code paths.**
* `ShiftClass` and stationarity — CHR‑typed claims about regime stability (iid | covariate‑shift | concept‑drift | adversarial). Default=`unknown`. The cited acceptance or selector policy governs the consequence of that unknown for its receiving use.
* `EvidenceGraphRef (A.10)` — evidence carriers and **lane tags TA, VA, and LA** with **freshness windows**; **no self-evidence**; default Γ-fold = **weakest-link** unless CAL establishes an alternative.
* `ScopeSlice(G)` — the **USM claim-bounding scope cut** over **EntityOfConcernRef and scope** (discipline governance in **CG‑Spec**; Domain is a catalog mark only).
* `SizeAndConditionProfile` — size and condition proxies (**n, m, kappa, sparsity**) with **declared units**; a unit mismatch makes the current comparison unsupported until the direct acceptance or selector policy supplies its governed result.
* **`Freshness`** — validity window for descriptors.
* `Missingness` — **MCAR, MAR, or MNAR** (or mapped equivalents) per **CHR.Missingness**; Acceptance and flow use preserve the declared missingness semantics.
* `KindSet` — selected C.3 `U.Kind` values for the entities addressed by the TaskKind; separates **EntityOfConcern kind** from **Scope (USM)**.

**QD and Illumination extensions (normative; ties to C.18 and C.19).**

Use this extension block only when QD, illumination archive, set-return, or OEE generator relation is live for the current case. It is not part of every `TaskSignature`.

* **`CharacteristicSpaceRef`** — reference to **`U.CharacteristicSpace`**, with declared **d≥2**; **characteristics are CHR‑typed**; **ReferencePlane** per characteristic; pin edition via **`CharacteristicSpaceRef.edition`**.
* **`ArchiveConfig`** — archive **topology** (grid, CVT, or graph), **resolution** (bins or centroids), **K‑capacity**, **`InsertionPolicyRef`** (elite replacement, dedup, or novelty), and **`DistanceDefRef.edition`** (declare **metric or pseudometric** status and invariances; normalisation is admissible only when the applied scale transform is admitted by **CG-Spec**); admissibility follows CG‑Spec.
* **`EmitterPolicyRef`** — reference to the emitter policy governed by C.19 and applicable to this TaskSignature; **edition id** recorded.
* **`DominanceRegime`** — `{ParetoOnly | ParetoPlusIllumination}`. **Default = `ParetoOnly`** (illumination remains report‑only telemetry unless CAL explicitly authorises `ParetoPlusIllumination`, policy‑id cited).
* **`IlluminationSummary`** — a **telemetry summary over `Diversity_P`**; reported by default; excluded from dominance unless a CAL enables `ParetoPlusIllumination` (policy‑id cited).
* **`IlluminationMap`** *(parity-run)* — parity-run publication is complete when an **IlluminationMap publication** (grid, CVT, or graph per `ArchiveConfig`) records coverage per niche or cell with `DescriptorMapRef` and `DistanceDefRef.edition`. A single-score leaderboard does not satisfy this comparison use; compare under the declared CG-frame.
* **`PortfolioMode`** — `{Pareto | Archive}`. **Default = `Archive`**: selectors preserve archive evidence (QD archives) rather than a single “best” set; ε‑fronts remain admissible for local decisions under CG‑Spec.
* **`Budgeting`** — evaluation, time, and batch **budgets**, including **E/E‑LOG exploration budget** id; units declared (CG‑Spec).
* **`TelemetryHooks`** — `PathSliceId` only when an E.18 path-slice reference is current, plus **decay and refresh policy ids**, **edition counters**, descriptor-map updates, and **policy-id** updates upon illumination gains.
* **`GeneratorIntent`** (OEE) — optional intent to use a registered **`GeneratorFamily`** (G.5), with pointers to **`EnvironmentValidityRegion`**, **`TransferRulesRef`**, and **coverage and regret** reporting expectations.

**Admissibility.** Before any numeric comparison or aggregation, establish CSLC admissibility for Scale, Unit, and Polarity and cite **CG-Spec.Characteristics**; record **ReferencePlane**. Preserve `unknown` for the downstream policy; do not coerce it to `0` or `false`, and do not invent a C.22-local disposition.

#### C.22:5.2 - `TaskSignature@Context` declaration and assignment

`TaskSignature@Context` is a Context-local species of A.6.0 `U.Signature`. It uses the canonical four-row block rather than a flat record schema. Because eligibility, acceptance, and selector patterns import or cite it, its A.6.0 `SignatureManifest` supplies a stable `SignatureId`, edition, imports, and provided names without adding a fifth semantic row.

```text
TaskSignature@Context <: U.Signature

SubjectBlock:
  SubjectKind = TaskKind, one exact C.3 U.Kind value
  RangedValueKind = U.Entity
  SliceSet = declared A.2.6 subject-scope slices
  ExtentRule = entities admitted by KindSet inside those scope slices
  ResultKind = absent; selector outcomes are not TaskSignature values

Vocabulary:
  TaskFamilyRef?
  KindSet
  characteristic bindings with Scale, Unit, Polarity, ReferencePlane, admitted comparison relation, and value or admitted unknown
  constraint relation references
  evidence-relation references
  optional QD, OEE, archive, generator, parity, budget, telemetry, and specialization vocabulary only when current

Laws:
  include only positions that can change eligibility, acceptance, or selection for the declared use
  preserve admitted unknown and distinguish it from absent non-current vocabulary
  apply CHR scale, unit, polarity, ReferencePlane, and comparison legality before aggregation
  keep acceptance verdicts, selector outcomes, selected methods, plans, work, and performed results outside the signature
  keep each reliance-bearing field connected to its exact basis relation and direct governing pattern

Applicability:
  bounded Context and declared subject scope
  qualification, freshness, edition, and evidence-use conditions on which use relies
  named Bridge and crossing conditions for cross-context or cross-plane use
```

The field families in C.22:5.1 are projections of the `Vocabulary` and `Applicability` rows. They are not extra conceptual rows and do not redefine A.6.0.

The assignment to one problem-side episteme and receiving use is a separate relation:

```text
TaskSignatureAssignmentRelation@Context <: U.Relation:
  BoundedContextSlot = <TaskSignatureAssignmentContextSlot, U.BoundedContext, U.BoundedContextRef>
  ProblemSideRecordSlot = <ProblemSideRecordSlot, U.Episteme, U.EpistemeRef>
  TaskSignatureSlot = <TaskSignatureSlot, U.Signature, U.EntityRef constrained to TaskSignature@Context>
  ReceivingUseDescriptionSlot = <ReceivingUseDescriptionSlot, U.Episteme, U.EpistemeRef>
  direction = ProblemSideRecordSlot -> TaskSignatureSlot for ReceivingUseDescriptionSlot
```

These SlotSpecs and direction are the exact RelationSignature. Relation identity is determined by bounded context, problem-side episteme edition, TaskSignature identity and edition, and receiving-use description. Changing only a publication carrier or serialization changes neither the TaskSignature nor its assignment relation.

**TaskSignature identity and publication.** The signature's `SignatureId`, edition, and four-row semantic content determine its identity. A semantic change to SubjectBlock, Vocabulary, Laws, or Applicability creates a revised signature edition. Two E.17 publications, database records, cards, or files may serialize the same TaskSignature edition when they resolve to that same identity and introduce no new claim. `ProblemProfile` may reference the signature and assignment relation, but it does not contain or become either one.

**Minimality rule.** The signature contains only the declaration positions needed to determine eligibility, acceptance, or admissible selection for the named use. Additional traits remain outside its Vocabulary unless a later use makes them current. Their mere availability does not expand the signature.

Values are CHR-typed and tied to the exact measurement, evidence-use, source-use, representation, or scope relation that justifies their use when such a relation is current. Each reliance-bearing field basis names that relation and its direct governing pattern; generic provenance or support wording is not a replay basis. Traits may be inferred from admitted CHR, CAL, and A.2.6 scope relations. Unknowns preserve their direct Missingness semantics.

**TaskSignature invariants.** A positive assignment satisfies all six conditions:

1. The TaskSignature exposes conformant SubjectBlock, Vocabulary, Laws, and Applicability rows.
2. The assignment relation recovers its Context, exact problem-side episteme edition, exact TaskSignature edition, and receiving-use description.
3. Every live field has an admitted filler kind or scale discipline and, under reliance, an exact basis relation with a direct governing pattern.
4. A live but unrecovered value is `unknown` only where the field's direct pattern admits it and a downstream policy ref states how the receiving use handles it.
5. A non-current optional extension is absent; absence and unknown are not interchangeable.
6. Eligibility verdicts, acceptance results, selected methods, selector outcomes, work plans, and work occurrences are absent from the TaskSignature and remain with their direct patterns.

#### C.22:5.2a - Lowering and withdrawal conditions

Withdraw `TaskSignatureAssignmentRelation@Context` for the current receiving use when its problem-side episteme, Context, TaskSignature edition, or receiving-use description cannot be recovered. The TaskSignature may remain a valid declaration for another assignment. Return to `C.22.2` only when the problem-side representation itself is no longer stable enough.

Revise the TaskSignature edition when one of its SubjectBlock, Vocabulary, Laws, or Applicability claims changes. Lower or remove one vocabulary position when its filler kind, scale, unit, polarity, reference plane, direct basis relation, or governing pattern cannot support the claimed use. Preserve `unknown` only when the position remains live and admitted. If a selected method, selector outcome, acceptance result, plan, or work occurrence appears inside the signature, split that value into its direct governing pattern.

A changed or invalid signature position reopens an earlier downstream result only when that result relied on the changed position. The downstream pattern repairs or supersedes its own result. A revised signature does not imply that the problem disappeared or that prior work did not occur.

#### C.22:5.2b - Evolution and currentness boundaries

C.22 revises the smallest affected four-row position and issues a new TaskSignature edition when semantic content changes. A changed problem formulation returns to `C.22.2` before a replacement assignment is made. `G.11` governs relied-on source edition, freshness, decay, telemetry, and currentness relations; its result may trigger signature review but does not rewrite the signature by itself. `C.18` and `C.19` govern archive, front, lineage, and live-pool evolution. `G.5` governs selected-set and method-family selector results. `E.23` governs repeated object-version improvement. C.22 introduces no local refresh object and does not rewrite earlier selector results or dated work without an explicit dependency.

`TaskKind` fills SubjectKind. `TaskFamilyRef?` names one comparison-relevant family in the Vocabulary when specialization, transfer, or parity is live. `KindSet` and the A.2.6 scope slices determine the ranged extent. None is a record-format field, selected method, or selector result.

**DesignRunTag hygiene.** Do not mix DesignRunTag in one signature edition; record GateCrossings as CrossingBundles under their direct patterns when design-time claims are reused in run-time work.

##### C.22:5.2.1 - Specialization-claim reference discipline (normative)
A claim that one holder, dyad, team, or explicitly scoped specialist portfolio acquired usable specialization is complete only when it states one declared `TaskFamilyRef` or `TaskSignature@Context`, one named work-measure threshold target, an adaptation budget, and the freshness or provenance basis for reuse. A method may be selected, refined, or retired as part of that story, but the method is not the bearer of the specialization claim. The TaskSignature declaration and assignment relation stay rich enough for the same task family and work target to remain admissible in `C.22.1` adaptation signatures, `G.5` specialization profiles, and `G.9` adaptation parity without reconstructing the claim from narrative prose.

Low-human-overlap or newly discovered task families remain admissible when those task-family or signature references are explicit by value.
#### C.22:5.3 - Provenance & planes.
Record **Context** and **ReferencePlane** for each value; on any cross-Context or cross-plane reuse, attach BridgeDescription plus UTS row and apply **CL** and, when planes differ, **CL^plane** penalties to **R_eff only**. The governing policy admits **Φ(CL)** and **Φ_plane** only when they are **monotone, bounded, and table-backed**. Do not use “distance” language; penalties never mutate F and G. Record policy ids in SCR and cite Bridge ids on crossings.

#### C.22:5.4 - Attachment & use.

The bullets below state the contract expected by downstream uses of the assigned TaskSignature. C.22 does not execute eligibility, acceptance, selection, archive treatment, or generator-family choice. Their verdicts and returned sets remain results of the named direct patterns.

* **Eligibility** gates read TaskSignature against each **MethodFamily.Eligibility** (C.23) and **CG‑Spec.MinimalEvidence** for referenced characteristics.
* **Acceptance** clauses (G.4) use these fields for **acceptance-gate threshold predicates** (acceptance-gate thresholds live in Acceptance only).
* **Selection kernel** (G.5.S3) applies an **admissible order** (often partial); **weighted sums across mixed scale types are inadmissible**. If only a partial order remains, **return a Pareto (non‑dominated) set** with tie notes. If `PortfolioMode=Archive`, the selector **may** return a **QD archive** (per `ArchiveConfig`) **in addition to** or **instead of** a Pareto set. **Illumination** enters dominance **only** if `DominanceRegime=ParetoPlusIllumination` is **enabled by CAL** (policy id cited); otherwise, QD telemetry values are **reported** but **excluded** from dominance.
* When `GeneratorIntent` is present, G.5-governed selection may use a registered **`GeneratorFamily`** (POET‑class); the selection domain becomes **pairs** `{environment, method}`, with Environment guarded by **`EnvironmentValidityRegion`** and **`TransferRulesRef`** (C.23 wiring). Report **`IlluminationSummary`** as a **telemetry summary over `Diversity_P`** (report‑only by default) in telemetry; dominance remains unaffected unless policy changes as above.

#### C.22:5.5 - Unknowns.
An identity position needed for positive closure cannot be replaced by `unknown`. A live characteristic or predicate may preserve `unknown` when its direct pattern admits it. The TaskSignature cites the downstream policy that governs the consequence; C.22 performs no implicit coercion and declares no universal outcome set.

#### C.22:5.6 - Publication.
When a named receiving use needs an addressable publication episteme, output a `C.2.1`-conformant **ProblemProfile** that carries the bound TaskSignature and only the evidence, currentness, crossing, and representation relations on which that use relies. Apply F.18 and F.17 Name Cards when a durable new name is actually being admitted; do not create name cards merely because a local field is present. Keep any vendor or tool examples in Plain explanatory use rather than letting them become normative selector inputs. When no publication reliance is current, the TaskSignature closes without a separate ProblemProfile.

#### C.22:5.7 - Open‑Ended tasks (GeneratorFamily) *(normative)*.
When **open-ended generation** of tasks or environments is current, S2 is complete only when it includes `GeneratorIntent` with pointers to **`EnvironmentValidityRegion`** (admissible region for generated environments), **`TransferRulesRef`** (cross‑environment transfer constraints), and **coverage and regret** telemetry expectations. Selector outputs are then declared sets over **{environment, method}**; **coverage and regret** are reported telemetry values and **IlluminationSummary** is a **telemetry summary** (reported), excluded from dominance unless a **CAL** policy promotes them (policy‑id recorded in SCR; see `DominanceRegime`). Edition increments of **CharacteristicSpaceRef.edition**, **DescriptorMapRef.edition**, **DistanceDefRef.edition**, and (OEE) **`TransferRulesRef.edition`**, and the **policy id** associated with an illumination increase form part of the SCR change record.

### C.22:6 - Archetypal Grounding (Tell–Show–Show)

*Tell–Show–Show hook (per E.8):* label examples as **Show‑1 (continuous ODE)** and **Show‑2 (MIP)** and cite CHR guard‑macros in‑line so engineers can see **which field supplied which Eligibility or Acceptance input**.  **Explicitly annotate which S2 fields triggered each Eligibility and Acceptance decision** (e.g., `service_level@ordinal → ORD_COMPARE_ONLY`, `budget@ratio → unit alignment check`).

**A. Differential equations (continuous systems, solver choice).**
*ProblemProfile.* `DataShape=ODE, stiff?=unknown, SizeAndConditionProfile={n≈10^3}, ObjectiveProfile={↓error@ratio, ↑throughput@ratio}, ConstraintRefs={budget-envelope relation, safety-predicate relation}, RegularityTraits={Lipschitz known?=unknown, Jacobian sparsity=high}, Missingness=MAR`.
*Attachment.* Selector consumes TaskSignature; **eligibility** filters MethodFamilies whose acceptance conditions include known stiffness or differentiability, with unknown yielding **degrade or abstain** per family. **Acceptance** treats `safety_gate` as an **ordinal predicate**, not an average (`ORD_COMPARE_ONLY`), and treats budgets with **unit-aligned sums** on ratio scales. The selector returns a **Pareto set**; no cross-ordinal weighting.

**B. Mixed‑integer optimisation (planning and scheduling).**
*ProblemProfile.* `DataShape=MIP, NoiseModel=deterministic, ObjectiveProfile={↓cost@ratio, ↑service_level@ordinal}, Constraints={SLA hard, workforce soft}, RegularityTraits={convex_relaxation=available}, SizeAndConditionProfile={vars~10^5}, Missingness=MCAR`.
*Attachment.* **CG‑Spec** forbids means over **service\_level** (ordinal); **Acceptance** holds acceptance-gate thresholds; **Eligibility** checks convex‑relaxation availability; **Selection** applies **lexicographic** guard (assumption‑fit ≻ evidence‑fit ≻ resource), compute **R\_eff** with Γ‑fold, apply **CL** penalty to **R** only; if partial order remains, return a **Pareto set**.

> *Current practice anchor:* the 2026 [SciML Problem Interface](https://docs.sciml.ai/DiffEqDocs/stable/basics/problem/) constructs an immutable problem value before solver use and supports explicit `remake` when problem fields change. C.22 adapts only that problem-before-selector separation; it does not import Julia types as FPF ontology.

**C. Quality-Diversity archive and declared set (illumination).**
*ProblemProfile.* `DataShape=policy‑search; ObjectiveProfile={↑reward@ratio, ↑coverage@ratio (report‑only)}, DominanceRegime=ParetoOnly, PortfolioMode=Archive, CharacteristicSpaceRef(d=3, characteristics=CHR‑typed), ArchiveConfig(grid, res=32×32×16, K=1, InsertionPolicyRef=elite‑replace, DistanceDefRef.edition=v1), EmitterPolicyRef=v2, Budgeting{eval=1e6}, TelemetryHooks{PathSliceId=…}`.
*Selection result.* Selector may return an **archive**; **coverage and illumination** are **reported** but **excluded** from dominance (default). Any change of `DistanceDefRef.edition` or Emitter policy is **editioned** and logged in SCR.

**D. Open‑ended environment generation (POET‑class).**
*ProblemProfile.* `GeneratorIntent{GeneratorFamilyRef=…, EnvironmentValidityRegion=… (CHR‑typed), TransferRulesRef=…, CoverageMetric=…}`, `PortfolioMode=Archive`.
*Selection result.* Selector outputs **{environment, method}** pairs that pass Eligibility; **TransferRules** govern cross‑environment policy reuse; telemetry reports **coverage and regret** and **IlluminationSummary** with **edition and policy‑id** when improved.

**E. Physical manufacturing method-family eligibility.**
*Problem-side record.* A shop must finish a declared alloy-part family inside one machine and inspection context. The receiving question is which available finishing-method families can be compared without presuming one of them.
*TaskSignature.* `TaskKind=surface-finishing work`, `ProblemSideRecordRef=accepted part-family problem card`, `ScopeSlice(G)=declared part family and production window`, `ObjectiveProfile={surface roughness Ra@ratio in micrometres with downward polarity, throughput@ratio}`, `ConstraintRefs={geometric-tolerance relation, heat-distortion relation, resource-envelope relation}`, and material-hardness condition as a live `unknown` with an explicit measurement relation and unknown-handling policy. The TaskSignature makes eligibility reviewable; it does not select grinding, honing, polishing, or another method and does not establish that any part was finished.

**F. Clinical rehabilitation method-family eligibility.**
*Problem-side record.* A rehabilitation service has a bounded patient cohort and must compare admissible intervention families for a stated capability-change question under clinical safety constraints.
*TaskSignature.* `TaskKind=rehabilitation-method-family comparison`, `ProblemSideRecordRef=accepted cohort problem record`, `ScopeSlice(G)=declared cohort and care setting`, outcome characteristics with their actual scale kinds and follow-up windows, contraindication and resource constraints, current evidence relations, and unknown tolerance or comorbidity values preserved as unknown. C.22 makes the comparison inputs explicit. It does not diagnose a person, recommend treatment, authorize care, prove benefit, or record performed clinical work; those claims remain with their clinical, evidence, gate, role, and work patterns.

### C.22:7 - Bias-Annotation (lexical and discipline guards)

* **Selector and policy relation precision.** When a source calls selection behavior a strategy, keep the Plain wording only for recognition. The governed claim cites the A.19.SelectorMechanism relation and the exact G.5 criteria, policy ref, or `SelectorOutcome`; no durable `Strategy` U-kind is introduced.
* **Transdiscipline vs domain.** Comparability flows through **`U.Discipline` CG‑Spec**; “Domain” is a catalog mark stitched to D.CTX + UTS; do **not** attach norms to Domain labels.
* **Plain twins and head selection.** Use Description and Spec morphology correctly (I, D, S; E.10.D2).

### C.22:9 - Conformance Checklist (normative)

0. **Minimal four-row S2.** `TaskSignature@Context` exposes an A.6.0 `SignatureManifest` plus SubjectBlock, Vocabulary, Laws, and Applicability. The manifest supplies stable identity and dependency metadata, not a fifth semantic row; the four-row declaration contains only content needed for eligibility, acceptance, or selection.
1. **Signature and assignment present.** Every exported selector-facing case names one TaskSignature identity and edition plus one `TaskSignatureAssignmentRelation@Context` whose problem-side episteme, receiving-use description, and bounded Context are recoverable. Current characteristic bindings are CHR-typed; a live unknown preserves `unknown`, while a non-current optional vocabulary item remains absent.
1a. **Publication does not define identity.** Two E.17 publications or serialized records that resolve to the same SignatureId, edition, and four-row semantic content describe the same TaskSignature. Carrier, layout, or serialization change alone does not create a new signature edition or assignment relation.
2. **CHR admissibility proven.** Any numeric comparison or aggregation **cites CG-Spec** by **Characteristic id** and proves **CSLC admissibility**; **no mean on ordinals; no unit mixing**.
3. **Unknowns remain typed.** A live unknown remains `unknown`, cites the direct downstream policy, and is not coerced. The acceptance, eligibility, or selector pattern records its own governed result.
4. **Evidence lanes.** **A.10 evidence relations**, **Assurance lanes TA, VA, and LA**, and **freshness windows** are recorded; **Gamma-fold** defaults to weakest-link unless the governing CAL establishes an alternative.
5. **ReferencePlane guarded.** ReferencePlane is noted **per value and per ObjectiveProfile head**; crossings apply **CL** and **CL^plane** when planes differ. **Φ(CL) and Φ_plane** are **monotone, bounded, table-backed, and documented in the `CG-Spec`**; penalties affect **R_eff only**, preserving F and G invariants.
6. **Acceptance thresholds live in CAL.** No acceptance-gate thresholds in CHR or code paths; only in **G.4 AcceptanceClauses**.
7. **Selector-use support.** The TaskSignature exposes the scales, units, polarities, and admitted order relations needed by `G.5`; it carries no mixed-scale scalarization or local selector verdict. `G.5` governs any Pareto-set result when its admissible relation remains partial.
8. **Crossings visible.** Any cross-stance or cross-Context reuse records **BridgeCard or BridgeDescription plus UTS row** with CL notes and, when planes differ, CL^plane plus Φ_plane.
9. **UTS twin labels.** All exported cards include **Name Cards** with twin labels; Bridges carry loss notes.
10. **GateCrossing checks.** Exported TaskSignature and referenced crossings satisfy: (i) stance tagging when used, as informative only; (ii) **CrossingBundle** presence and consistency under **E.18**, **F.9**, **F.17**, **E.17**, and **A.21** when gate checks are live; (iii) **LanePurity**, with CL affecting R only, F and G invariants preserved, and Φ tables present; and (iv) **Lexical SD** under **E.10**. Failures return a blocking gate result under the active GateProfile and GateChecks governed by A.21.
11. **QD fields (when QD is in scope).** A `TaskSignature` with `PortfolioMode=Archive` or QD heads is complete only when it carries CHR-typed **CharacteristicSpaceRef** (d>=2), **ArchiveConfig** (topology, resolution, K, `InsertionPolicyRef`, `DistanceDefRef.edition`), and **EmitterPolicyRef** fields; every characteristic declares its **ReferencePlane**.
12. **DominanceRegime default.** `DominanceRegime` defaults to `ParetoOnly`. Illumination enters dominance only through a cited **CAL.Acceptance policy** enabling that relation; the SCR records the policy id.
13. **Telemetry.** The telemetry record carries **PathSliceId** when an E.18 path slice is current, the applicable **decay and refresh policy ids**, and edition counters for **CharacteristicSpaceRef**, **DistanceDefRef**, and **EmitterPolicyRef**. An illumination increase is traceable to the policy id that admitted it.
14. **GeneratorIntent (when OEE is in scope).** A TaskSignature supports the claimed OEE generator-family use only when `GeneratorIntent` cites **`EnvironmentValidityRegion`** and **`TransferRulesRef`** with ids resolvable in G.5 and C.23. Any downstream abstention is their result, not a C.22 output.
15. **Budgets.** When `Budgeting` is live, its evaluation, time, and batch values carry declared units and the applicable E/E-LOG exploration-budget id.
16. **Archive-comparison support.** A TaskSignature supports the claimed archive comparison only when `DistanceDefRef.edition` and the applied novelty measures are CSLC-admissible and editioned. The archive or selector pattern governs any downstream abstention or returned-set result.
17. **Planes.** QD heads and characteristics carry a declared **ReferencePlane**; a plane crossing applies **Phi_plane** as a penalty to **R** only.
18. **Unknown QD values.** A live unknown QD field remains `unknown`, cites the policy governing its downstream use, and is not coerced or mapped by C.22 itself.

19. **Specialization claims referenced.** A declared specialization on this TaskSignature is complete when it names the task family and work target, work-measure threshold target, adaptation budget, freshness or provenance basis for reuse, and the exact TaskSignature edition and assignment relation needed for the same claim to remain admissible in `C.22.1`, `G.5`, and `G.9` use.

### C.22:8 - Common Anti-Patterns and How to Avoid Them

| Countercase | Repair |
| --- | --- |
| A preferred method or strategy name is inserted into S2 before eligibility is tested. | Remove the method value, restore the exact problem traits, and let A.19, C.23, G.4, and G.5 govern later comparison and selection. |
| A live unknown is encoded as `false`, `0`, or an empty value. | Restore `unknown`, name the direct basis relation and receiving-use policy, and let the downstream pattern produce the result governed by that policy. |
| Ordinal values or values with unlike units are averaged into one score. | Recover scale, unit, polarity, reference plane, and admitted order for every head; use only a directly governed admissible comparison or leave the candidate set partially ordered. |
| One TaskSignature mixes design-time traits, later run observations, and incompatible DesignRunTag positions. | Split the claims by their actual work and relation positions; retain only the traits current in this signature edition and use E.18 crossing relations when the receiving use relies on the crossing. |
| A new file, card, or database row is treated as a new TaskSignature. | Resolve SignatureId and edition and compare the four-row semantic content. Reuse the same identity when only the publication or serialization changed; issue a new edition only for a semantic row change. |
| A broad domain label is used as if it supplied scope, measurement, evidence, or selection rules. | Recover the exact bounded context, A.2.6 scope relation, `U.Discipline`, characteristic rules, and direct selector or policy relations that the use actually needs. |
| Data shift is assumed away because the old profile used `iid`. | State the current `ShiftClass` or `unknown`, cite its evidence and currentness relation, and let the acceptance or selector pattern decide the changed use. |
| A vendor, tool, or fashionable method label is treated as a normative selector input. | Keep it only as a Plain example or recover the exact method-description, capability, evidence, and selector relations on which comparison relies. |

### C.22:10 - Selector Fields And Evidence Relations

*Inputs.* `ProblemProfile` (...Description), CG-Spec ids, Evidence Graph Ref (A.10), D.CTX; CharacteristicSpaceRef, ArchiveConfig, and EmitterPolicyRef configs when QD is live; GeneratorIntent when OEE is live.
*Produces.* One `TaskSignature@Context` value, declared as the Context-local `U.Signature` species specified in C.22:5.2. When a receiving use is current, C.22 also produces one separate `TaskSignatureAssignmentRelation@Context` relating that signature edition to the exact problem-side episteme and receiving-use description. `TaskSignature@Context` is neither a new root U-kind nor a record kind: SubjectBlock, Vocabulary, Laws, and Applicability determine its semantic edition, while carrier and serialization remain outside its identity. Optional QD, archive, generator, `PortfolioMode`, and telemetry vocabulary appears only when current.
*Used by.* **G.5** (Eligibility and Selection kernel), **G.4** (Acceptance and Evidence), **C.23** (admit, degrade, and abstain rules and method-family maturity checks).

### C.22:11 - Consequences (informative)

* **Admissible selection.** Selection is **explainable** and **inspectable**; every admission or rejection reason cites TaskSignature fields, CG-Spec rows, and Gamma-fold contributors.
* **Local first, Bridge-portable.** Context-local semantics are primary; Bridges make portability **deliberate and costed** (penalties to **R** only).
* **Frictionless downstream.** G.1-G.5 use one **single, typed** TaskSignature; thresholds are cleanly separated into **Acceptance**; unknowns are not guessed.
* **QD and OEE-ready.** Typed QD and GeneratorIntent fields make **declared returned-set structure** and **open-ended** generation contexts **explicit**, with admissible dominance, editioned distances, and policy-aware illumination.

### C.22:12 - Rationale

C.22 exists because method selection before eligibility, acceptance, evidence, unknown-handling, and admissible comparison relations are explicit invalidates the selector-facing problem record.

### C.22:12.1 - SoTA-Echoing

Wolpert and Macready's ["No Free Lunch Theorems for Optimization"](https://doi.org/10.1109/4235.585893), 1997, remains historical lineage for the warning that method superiority is distribution-dependent. It does not by itself supply the current C.22 field set, a selector policy, or evidence that one TaskSignature is adequate. The current sources below change the pattern by value.

| Current source and status | Adopted or adapted move | Effect in C.22 | Limitation and review condition |
| --- | --- | --- | --- |
| Roger Jiao, ["Towards rigorous problem formulation for engineering design research: from motivations to measurable claims via metric-measure-method"](https://doi.org/10.1080/09544828.2026.2633289), *Journal of Engineering Design* 37, 2026; Szajnfarber, Lifshitz, and Tushman, ["Beyond translation: how context work during problem formulation enables effective solving by outsiders"](https://doi.org/10.1080/09544828.2026.2633491), 2026 research article. | Adopt problem-before-method formulation, explicit context, operational characteristics and measures, and a named decision or action that will use the result. Adapt context work into the signature's SubjectBlock, Vocabulary, and Applicability plus the problem-side and receiving-use slots of `TaskSignatureAssignmentRelation@Context`. | Changes the working question, local mantra, signature content, assignment relation, reliance replay, and the manufacturing and clinical transfer cases. A fashionable method or available dataset cannot define the TaskSignature or its assignment. | These sources study engineering research formulation and outsider problem solving; they do not establish FPF kinds or one universal signature schema. Review the adaptation if later cross-domain evidence overturns the role of context or measurable problem characteristics. |
| Cenikj, Kudela, Tuba, and Eftimov, ["Evaluating Real-World Generalizability of Algorithm Selection Models"](https://arxiv.org/abs/2606.02016), current June 2026 conference-linked paper and arXiv version. | Adopt measurable problem characteristics as selector inputs and the empirical warning that transfer between benchmark and real-world landscapes can fail. | Changes `ScopeSlice(G)`, evidence and currentness relations, crossing discipline, unknown handling, and the rule that an old selector result reopens only when it depended on a changed field. | The study concerns optimization landscapes and algorithm-selection models, not all methods or sectors. Do not infer universal transfer failure or a complete TaskSignature field list from its benchmark set. |
| Qin et al., ["A survey on Quality-Diversity optimization: Approaches, applications, and challenges"](https://doi.org/10.1016/j.swevo.2025.102240), *Swarm and Evolutionary Computation* 100, 2026; Lin et al., ["Quality-Diversity Optimization as Multi-Objective Optimization"](https://arxiv.org/abs/2602.00478), current 2026 preprint. | Adopt collection-valued QD results, user-declared behavior or characteristic space, explicit containers and policies, and set-aware comparison. Adapt the MOO reformulation as one current option rather than the definition of QD. | Changes the optional QD positions, `DominanceRegime`, report-only illumination boundary, archive case, and refusal of one default scalar score. | The survey is broad but QD-specific; the MOO reformulation is a current preprint and one competing approach. Neither authorizes every diversity measure to enter dominance. Review when stronger comparative evidence changes container, metric, or scalarization treatment. |
| SciML, ["Problem Interface"](https://docs.sciml.ai/DiffEqDocs/stable/basics/problem/) and ["Common Solver Options"](https://docs.sciml.ai/DiffEqDocs/stable/basics/common_solver_opts/), living documentation generated in June 2026. | Adapt the practical separation between a constructed problem value and later solver dispatch, plus explicit problem remake when fields change. | Changes the ODE case and the smallest-repair rule: a semantic field change revises the TaskSignature edition, and a changed problem-side or receiving-use position revises the assignment relation before selector replay; solver implementation does not become the problem or TaskSignature. | This is current software practice, not a transdomain ontology and not evidence that every project needs an immutable software record. Review on material interface or dispatch changes; preserve the general separation only while it continues to improve the declared use. |

### C.22:13 - Relations
**Builds on:** **C.16 MM-CHR**, **G.0 CG-Spec**. **Coordinates with:** **G.4 Acceptance**, **G.5 Selector**, **C.18 NQD-CAL**, **C.19 E/E-LOG**, **C.23 Method-SoS-LOG**, and `C.32.P2S` when typed problem pressure continues into architecture selected structures and synthesis. **Constrained by:** **E.10 (selected `EntityOfConcern`, Description-episteme, specification-use, and publication-lane wording)**, **E.18 (GateCrossing visibility and publication gating)**.

### C.22:14 - Practical Use Checks

- If two candidate approaches are answering different `TaskKind`s or different `ScopeSlice(G)` cuts, a direct comparison is not admissible yet.
- If specialization is the live specialization question, the task-family reference, threshold target, adaptation budget, and provenance basis should already be recoverable from the assigned `TaskSignature@Context` edition.
- If crossing, normalization, or missingness changes what comparison means, state that in the signature and its cited refs rather than hiding it in code, local memory, or explanatory prose.
- If `QD` or `OEE` heads are in scope, archive and generator fields belong in the same typed signature rather than in a detached explanatory appendix.

### C.22:15 - Goldilocks Hook (design-time)

When generating candidate solutions for a **TaskKind**, aim for **“goldilocks”** slots (feasible‑but‑hard) so that the TaskSignature is informative (neither trivial nor impossible); this aligns with **G.1** (goldilocks target, abductive provenance) and ensures the **TaskSignature is informative** (neither trivial nor impossible) for **G.5** selection.

### C.22:End

