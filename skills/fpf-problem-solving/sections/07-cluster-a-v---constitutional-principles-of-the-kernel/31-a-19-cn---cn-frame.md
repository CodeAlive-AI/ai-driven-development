## A.19.CN - CN‑frame (comparability & normalization)

> **Scope.** This CN‑frame Algebra & Normalization Discipline **extends A.19** by fixing the **governance Standard** for CN‑frames, defining a **conformance checklist** and **regression harness**, and providing **didactic one‑pagers** and **anti‑patterns** so teams can introduce CN‑frames without tool lock‑in. The mandatory pattern structure and authoring discipline from **Part E** (Style Guide, Tell‑Show‑Show, checklists, DRR, guard‑rails) are applied throughout.
>
> **Governing-pattern boundary (cite, don’t duplicate).** A.19.CN governs the **CN-frame governance card, registry, bridges, and checklist/harness** (`CN-Spec`, registry, bridges, checklist/harness). It does **not** govern any CHR-mechanism **intensions**, term cards, or method taxonomies. Those are governed by the corresponding mechanism-governing patterns: **A.19.UNM**, **A.19.UINDM**, **A.19.USCM**, **A.19.ULSAM**, **A.19.CPM**, and **A.19.SelectorMechanism**. Evidence/backing is governed by **C.16**; admissibility gates are governed by **G.0**. Therefore A.19.CN specifies *where the references live*, *what must be citeable for audit*, and *how governance changes trigger regression* — not mechanism semantics.
>
> **Reader guide (fast navigation).**
> - “What does `NormalizationMethodId/…InstanceId/≡_UNM/NormalizationFix` mean?” → **A.19.UNM**.
> - “What is an Indicator / `IndicatorChoicePolicy` and why NCV ≠ Indicator?” → **A.19.UINDM**.
> - “Why can we trust a normalization / where does calibration or evidence live?” → **C.16 (MM‑CHR)**.
> - “What is admissible to compare or aggregate, and what is `MinimalEvidence`?” -> **G.0 (CG-Spec)**.

### A.19.CN:1 - Context

A.19 established a substrate‑neutral picture:

* a **CN‑frame** = a selected **CharacteristicSpace (CS)** + **chart** (coordinate patch + units) + a referenced **Normalization mechanism (UNM)** for one named bearer, comparison basis, scope/window, and intended use. A.19.UNM defines the admissibility, invariants, and `≡_UNM` semantics;
* **operators** (subspace, product, pullback/pushforward) and **comparability** (coordinatewise vs **normalization‑based (normalize‑then‑compare)**);
* **RSG touch‑points**: role readiness (**RSG** states) are **certified** against CS via **checklists** over observable characteristics;
* **entity/relational mixtures** across CN‑frames via minimal schemas and bridges.

**Terminology guard.** *CN‑frame* is the **lens** (I); *CN‑Spec* is the specification (S) that fixes the bearer, characteristic and scale editions, chart, comparison basis, scope/window, normalization references, comparability rule, aggregation choice, and intended use; *CN‑Description* is the didactic surface (D) with worked examples and anti-patterns. Mechanism-level term cards such as `NormalizationMethod`, `NormalizationMethodInstance`, `NCV`, `≡_UNM`, and `IndicatorChoicePolicy` remain defined by the corresponding **A.19.<MechId>** patterns and are only cited here.

**Lexical guard (map/Map, by reference).** Follow the lexical discipline governed by **A.19.UNM**: avoid introducing new normalization tokens that use “map/Map/mapping” (because `…Map` is a Part‑G method‑type kind). In normalization contexts prefer **normalize / transform / re‑parameterize**. Legacy tokens (including retired κ‑notation) are handled via **alias docking** (F.18); A.19.CN applies this rule and does not redefine it.

A.19.CN makes this *operational and auditable*.

### A.19.CN:2 - Problem

Absent a governance layer, four failure modes recur:

1. **Chartless numbers.** Measures move between teams without units, reference states, or declared normalization → **illusory comparability**.
2. **Hidden normalization flips.** Re‑parameterisations (e.g., normalising by batch size) silently alter meaning; trend lines lie.
3. **CN‑frame sprawl.** Every initiative mints a new “dashboard dimension”; semantics diverge; assurance collapses.
4. **Un‑bridgeable reports.** Cross‑team roll‑ups average **incongruent** CN‑frames, violating the **weakest‑link (WLNK)** discipline from Γ and B.3.

### A.19.CN:3 - Forces

| Force                         | Tension we must balance                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| **Universality vs nuance**    | One Standard for robotics, safety, and finance, while each named source scheme retains its own exact meanings. |
| **Speed vs audit**            | Light ceremony for on‑ramp; hard guarantees for assurance and SoD.                   |
| **Local truth vs federation** | Keep meanings tied to their exact schemes and claims; still allow explicit relations and bounded receiving uses. |
| **Minimalism vs safety**      | Few mandatory slots; enough structure to forbid silent normalization drift.                  |

### A.19.CN:4 - Solution — **The CN‑Spec** (CN‑Spec) + **Registry** + **Bridges**

#### A.19.CN:4.1 - The **CN‑Spec** (comparability and normalization specification)

A **CN‑frame** is described by a compact, notation-free specification. The specification names the bearer and the exact boundary within which its readings may be compared:

```
CN‑Spec {
  name              : CN‑frameName
  edition           : <edition>
  bearer_ref        : <evaluated bearer or bearer kind>
  characteristic_space_ref : <CharacteristicSpaceRef>
  scope_ref?        : <ClaimScopeRef>
  window?           : <qualification interval>
  reference_or_comparison_basis : <corpus, baseline, reference state, or declared comparison set>
  cs_basis          : [{
    slot_id         : <tech-token>,
    characteristic  : <U.Characteristic>,
    scale           : { type: nominal|ordinal|interval|ratio, unit?: <U.Unit>, bounds?: <…> },
    polarity        : up|down|target-range,
    // if needed: missingness?, admissible_domain? (MM‑CHR-consistent metadata)
  }]
  chart             : { reference_state, coordinate_patch, measurement_protocol_ref }
  normalization     : {
    UNM_id?,
    methods: [NormalizationMethodId],
    instances?: [NormalizationMethodInstanceId],
    method_descriptions: [NormalizationMethodDescriptionRef],
    admissible_reparameterizations,
    invariants,
    fix?: <NormalizationFixSpec>
  }
  comparability     : { mode ∈ {coordinatewise, normalization-based}, minimal_evidence }
  intended_use      : <claim, comparison, admission, or aggregation use>
  indicator_policy? : { IndicatorChoicePolicyRef, scope, edition }
  acceptance        : { checklist_for_admission, window, evidence_anchors }
  aggregation       : { Γ_fold, WLNK/COMM/LOC/MONO choices, time_policy }
  alignment?        : [{ bridge_ref, direction, correspondence_rule, tolerated_loss, reliance_ref? }]
  maintenance       : { source_maintenance_assignment, DRR_links, deprecation_plan }
}
```

**Reading:** the CN-frame is the selected characteristic space and chart for one named bearer and use. `CN‑Spec` pins the editions, comparison basis, scope and window, normalization references, aggregation choice, and admission evidence that make that use auditable. A.19.UNM still defines normalization semantics, A.19.UINDM defines indicatorization, C.16 supplies measurement and evidence backing, and G.0 supplies admissibility gates. CN‑Spec records the values used; it does not make a source, scope, or Bridge into a universal container.

**Mechanism-reference note.** `UNM_id` identifies the admitted normalization mechanism. `NormalizationMethodId` and `NormalizationMethodInstanceId` retain the meanings declared by A.19.UNM, and evidence for a relied-on instance remains with C.16. CN‑Spec neither redefines those terms nor implies transport or a cross-local relation.

**L‑CN‑Spec‑NORM‑IDs (by reference).** Use the stable normalization identifiers specified by A.19.UNM. Avoid generic “map” nouns and retired κ-notation except through F.18 alias docking. Reference fields follow A.6.5: `*Ref` names a reference field and `*Slot` names a SlotKind.

#### A.19.CN:4.2 - **CN‑frame Registry**

One named registry and edition may publish:

* canonical CN-frame names and editions together with their characteristic-space and bearer references;
* the source-maintenance and certification assignments, including their non-overlapping windows where separation of duties is required; and
* the deprecation relation: what replaces an edition and from when.

The registry aids discovery and currentness. It does not supply the characteristic meanings, comparison basis, scope, or evidence recorded by each CN‑Spec.

#### A.19.CN:4.3 - **Bridges between exact local meanings**

When two CN-frame uses rely on different exact F.17 local senses, cite an obtaining F.9 Bridge between those cells. A compact record can expose the information needed by the receiving use:

```
Bridge <source F.17 cell> → <target F.17 cell>
  direction: <source-to-target use>
  correspondence_rule: <how the local claims correspond>
  applicable_use: <the receiving comparison or aggregation>
  kept_characteristics: [… ]
  lost_characteristics: [… ]
  tolerated_loss: <declared limit>
  transform: {pullback | pushforward | re-scaling | re-binning | … }
  plane_relation_ref?: <only when a separately defined plane relation obtains>
  extra_guards: {additional evidence, review assignment, or waiver speech act}
```

The Bridge establishes only the exact sense relation. A claim that uses it for comparison, admission, or aggregation remains a separate C.2.1 use claim with its direction, rule, and tolerated loss, together with the current A.10 evidence-use or B.3 assurance reliance required for that use. No Bridge follows from matching names, and no reverse direction follows automatically. B.3 supplies any current loss effect on assurance; CN‑Spec may add operational guards but does not redefine that calculus.

### A.19.CN:5 - Conformance Checklist (normative)

> **Pass these and your CN‑frames are fit for assurance and cross‑team composition.**

**CC‑A19.D1‑1 (Local identity and scope).** Every CN-frame **MUST** identify its name and edition, bearer, characteristic space, reference or comparison basis, intended use, and any scope/window that qualifies the readings. The same label under another scheme or edition is not evidence of the same frame.

**CC‑A19.D1‑2 (Units & polarity).** Each characteristic in `cs_basis` **MUST** declare **unit and scale** and **polarity** (↑ better, ↓ better, or target range). No unlabeled magnitudes.

**CC‑A19.D1‑3 (Chart).** `chart` **MUST** name the **reference state**, **coordinate patch** and **measurement protocol** (`U.MethodDescription`) to make numbers reproducible.

**CC‑A19.D1‑4 (Normalization references, not redefinition).** `normalization` **MUST** (i) cite the UNM mechanism (`UNM_id?`) and (ii) provide the normalization references required by the A.19.UNM governing pattern (methods / invariants / fix, and instances when used) so that any normalization‑based comparison is auditable. This pattern does not define what a “NormalizationMethod” is — it requires that CN‑Spec can point to the governing pattern that does.

**CC‑A19.D1‑5 (Comparability mode).** `comparability.mode` **MUST** be either **coordinatewise** (same chart & units) or **normalization‑based** (“normalize‑then‑compare” via the declared **UNM**). Mixed/implicit modes are prohibited. The semantics of `≡_UNM` and what counts as “same class” is governed by **A.19.UNM**; CN-Spec only pins the references needed to audit the choice.

**CC‑A19.D1‑6 (Admission checklist).** `acceptance.checklist_for_admission` **MUST** be observable and time‑bounded; each datum admitted to the CN‑frame **SHALL** cite a **StateAssertion** or equivalent `U.Evaluation`.

**CC‑A19.D1‑7 (Aggregation discipline).** `aggregation.Γ_fold` **MUST** specify WLNK/COMM/LOC/MONO choices and the **time policy** (e.g., average of rates vs integral of counts). **No free‑hand averages.** Folding admissibility and semantics are governed by **B.3** and **G.0** (and, when a folding mechanism is cited, by its mechanism-governing pattern); CN‑Spec only stores the governance pins.

**CC‑A19.D1‑8 (Relation and use discipline).** When reuse depends on different exact F.17 local senses, the receiving claim **MUST** cite an obtaining F.9 Bridge with exact endpoints, direction, correspondence rule, applicable use, and tolerated loss. The comparison or aggregation remains a separate C.2.1 use claim, with the current A.10 evidence-use or B.3 assurance reliance required by that use. Coordinate-by-name without that relation and use account fails.

**CC‑A19.D1‑9 (Separation of duties).** Editing CN-Spec and admitting data **MUST** be performed under distinct system-role assignments whose relevant windows do not overlap: `CN‑frameStewardAssignment ⊥ CN‑frameCertifierAssignment`.

**CC‑A19.D1‑10 (Maintenance, deprecation, and DRR).** Every CN-Spec **MUST** carry a **source-maintenance role assignment**, a **deprecation plan**, and links to **DRR** entries for rationale and changes (Part E.9).

**CC‑A19.D1‑11 (Anchors & lanes for comparability).** Any **admission** into a CN‑frame that is later **used for comparison/aggregation** **SHALL** cite the corresponding **A.10 evidence-provenance anchors** or **A.2.4 evidence-use relation slots** for each characteristic, with **assuranceUse lane** tags {TA, VA, LA} and **validity windows** (where applicable), so that the **SCR** can report lane‑separated contributions and freshness (B.3). Absence of anchors for a required characteristic renders items **incomparable**.

**CC‑A19.D1‑12 (Notation independence).** CN‑Spec content **MUST NOT** depend on a tool or file format; semantics precede notation (E.5.2 Notational Independence).

**CC‑A19.D1‑13 (Lexical guard‑rails).** characteristic names and role labels **MUST** follow the Part E lexical discipline (registers, twin labels; no overloaded “process/service/function”).

### A.19.CN:6 - Consequences (informative)

| Benefit                           | Why it matters                                                                                                        |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Auditable comparability**       | Chart + declared normalization (UNM + NormalizationMethods) make “same number” meaningful; silent re‑basings become explicit, reviewable choices.                   |
| **Safe roll‑ups**                 | Γ‑folds with WLNK/COMM/LOC/MONO stop optimistic averaging and preserve invariants.                                    |
| **Pluralism without incoherence** | Bridges with CL and loss notes allow federation without pretending to global sameness.                                |
| **RSG‑ready**                     | Admission checklists let **RSG** states reference **CN‑frame‑backed** facts (e.g., *Ready* requires characteristics within bounds). |

### A.19.CN:7 - Rationale (informative)

The CN‑Spec aligns A.19.CN with **Part E**: it packages Tell‑Show‑Show, Conformance Checklists, and DRR‑backed change, while honouring **DevOps Lexical Firewall**, **Unidirectional Dependency**, and **Notational Independence** so that semantics never depend on tooling.  It also operationalises B.3 **Trust & Assurance** by making CL penalties and WLNK folds first‑class.

### A.19.CN:8 - Archetypal Grounding *(Tell‑Show‑Show)*

> **Same slots, three arenas; no tooling implied.** The examples below use plain-language normalization descriptions as placeholders; any normative use must cite A.19.UNM-governed ids/refs (A.19.UNM) and evidence pins (C.16), not invent new terminology here.

#### A.19.CN:8.1 - **Industrial line** — *Weld‑quality CN‑frame* (`AssemblyLine_2026`)

* `cs_basis`: *BeadWidth\[mm] (target 6.0±0.2)*, *Porosity\[ppm] (↓)*, *SeamRate\[1/min] (↑ until limit)*
* `chart`: reference jig, fixture ID, torch type; `MethodDescription#Weld_MIG_v3`
* `normalization`: affine rescale on gray‑level calibration → invariant = physical porosity
* `comparability`: **normalization‑based (UNM)** (calibration tables applied)
* `aggregation`: WLNK on quality (min‑bound), COMM on counts, time = per‑shift histograms
* **RSG hook**: `WelderRole.Ready` requires *Porosity ≤ 500 ppm* & *BeadWidth within ±0.2 mm* admitted by this CN‑frame.

#### A.19.CN:8.2 - **Software/SRE line** — *Latency CN‑frame* (`SRE_Prod_Cluster_EU_2026`)

* `cs_basis`: *P50Latency\[ms] (↓)*, *P99Latency\[ms] (↓)*, *Load\[req/s]*
* `chart`: client vantage, trace sampler v4; `MethodDescription#HTTP_probe_v4`
* `normalization`: monotone time‑warp compensation for collector skew; invariant = percentile order
* `comparability`: **normalization‑based (UNM)** with declared normalization
* `aggregation`: MONO on latency (max of mins), WLNK across services
* **RSG hook**: `DeployerRole.Active` gated if **P99** < declared SLO over the admission window.

#### A.19.CN:8.3 - **Clinical/episteme line** — *Trial‑outcome CN‑frame* (`Cardio_2026`)

* cs_basis:
  - slot_id: ΔBP
    characteristic: BloodPressureChange
    scale: { type: ratio, unit: mmHg }
    polarity: down
  - slot_id: AdverseRate
    characteristic: AdverseEventRate
    scale: { type: ratio, unit: "%" }
    polarity: down
  - slot_id: Age
    characteristic: Age
    scale: { type: ratio, unit: years }
    polarity: neutral
* `chart`: cohort definition; `MethodDescription#TrialProtocol_v5`
* `normalization`: case‑mix adjustment (propensity score); invariant = adjusted ΔBP
* `comparability`: **normalization‑based (UNM)** (post‑adjustment)
* `aggregation`: LOC on subcohorts; WLNK on safety outcomes
* **RSG hook**: evidence-use validation of an admission requires CN‑frame acceptance; **Assurance** pulls CL from any Bridge used.

#### A.19.CN:8.4 - Worked mini-schemas (entity and relation mixtures across CN-frames, informative)

The three small schemas below show an operations use, an assurance use, and an alignment use. They are explanatory representations, not storage requirements. Each keeps the bearer, system-role kind and assignment, measurement or evaluation result, source-local relation, and evidence use distinct.

##### A.19.CN:8.4.1 - Operations CN‑frame — runtime gating and enactment

_Entity graph view:_

```
System ── classifiedAs ──> SystemRoleKind
System + SystemRoleKind + scope/window ── assignment ──> SystemRoleAssignment
Role-state graph ── lists ──> State
Checklist ── tested by evaluation Work ──> StateAssertion
Work ── performedBy ──> assigned System
Work ── enacts ──> Method
```

The System is classified under one exact local system-role kind and participates in an obtaining assignment for the stated scope and window. A role-state graph lists states such as Ready, Waiting, or Degraded. Evaluation Work applies the state checklist and supports a StateAssertion. Operational Work may proceed only when the relied-on assertion says that an enactable state obtains; the Work, Method, assignment, and result remain different objects.

_Relational stub:_

| Table | Key columns (essential) |
|---|---|
| **ROLE_ASSIGNMENT** | `RA_ID`; `HOLDER_SYSTEM_ID`; `SYSTEM_ROLE_KIND_ID`; `REFERENCE_SCHEME_ID`; `SCOPE_REF?`; `WINDOW_FROM`; `WINDOW_TO` |
| **RCS_SNAPSHOT** | `SNAP_ID`; `RA_ID`; `WINDOW_FROM`; `WINDOW_TO`; `CHAR_ID`; `VALUE`; `UNIT`; `SCALE_TYPE`; `RESULT_REF` |
| **RSG_STATE** | `STATE_ID`; `SYSTEM_ROLE_KIND_ID`; `NAME`; `ENACTABLE` |
| **CHECKLIST** | `CHK_ID`; `STATE_ID`; `PREDICATE_TYPE`; `PREDICATE_SPEC` |
| **STATE_ASSERTION** | `SA_ID`; `RA_ID`; `STATE_ID`; `CHK_ID`; `WINDOW_FROM`; `WINDOW_TO`; `VERDICT`; `NORMALIZATION_INSTANCE_ID?`; `BRIDGE_USE_CLAIM_REF?` |
| **WORK** | `WORK_ID`; `PERFORMER_SYSTEM_ID`; `METHOD_ID`; `WINDOW_FROM`; `WINDOW_TO`; result and evidence refs as needed |

The RCS snapshot keeps the characteristic, value, unit, scale, window, and result identity visible. A StateAssertion separately identifies any normalization instance and any claim that uses a Bridge. An enactment query can therefore ask whether the latest admissible assertion for this assignment has an enactable state and a passing verdict without treating a role label, CN-frame, or Bridge as the acting System.

##### A.19.CN:8.4.2 - Assurance CN‑frame — evidence freshness and related local meanings

_Entity graph view:_

```
NormalizationMethodInstance ── used for ──> characteristic re-expression
F.9 Bridge ── relates ──> exact source and target F.17 cells
ComparisonClaim ── cites ──> normalization instance and/or Bridge-use claim
RelianceClaim ── cites ──> evidence status and assurance limits
```

The normalization instance identifies the declared re-expression and its validity window. The Bridge identifies only an obtaining relation between two exact local senses. A comparison that relies on either one says so in its own use claim; its evidence and assurance limits remain explicit.

_Relational stub:_

| Table | Key columns (essential) |
|---|---|
| **NORMALIZATION_METHOD** | `NORMALIZATION_METHOD_ID`; `KIND`; `DESCRIPTION_REF` |
| **NORMALIZATION_INSTANCE** | `NORMALIZATION_INSTANCE_ID`; `NORMALIZATION_METHOD_ID`; `SRC_CHAR_ID`; `TGT_CHAR_ID`; `FORMULA_SPEC_OR_LUT_REF`; `VALIDITY_WINDOW`; `EVIDENCE_REF` |
| **BRIDGE** | `BRIDGE_ID`; `SOURCE_CELL_REF`; `TARGET_CELL_REF`; `DIRECTION`; `CORRESPONDENCE_RULE`; `APPLICABLE_USE`; `TOLERATED_LOSS` |
| **COMPARISON_USE** | `USE_CLAIM_ID`; `RESULT_REF`; `NORMALIZATION_INSTANCE_ID?`; `BRIDGE_ID?`; `EVIDENCE_USE_REF`; `ASSURANCE_REF?` |
| **ASSURANCE_EVENT** | `AE_ID`; `USE_CLAIM_ID`; `EFFECT`; `DETAILS`; `WINDOW` |

The tables make an audit path possible without assigning meaning to the table itself. A low-assurance relation, stale normalization instance, or refreshed evidence can be recorded as a distinct event and can reopen only the comparisons that rely on it.

##### A.19.CN:8.4.3 - Alignment CN‑frame — design-time reuse across local schemes

_Entity graph view:_

```
Checklist for target state ← re-expressed by N ─ Checklist for source state
source F.17 cell ── Bridge with direction and loss ──> target F.17 cell
SystemRoleKind' ── stated refinement relation ──> SystemRoleKind
```

A checklist from one source scheme may be re-expressed for another only through the named normalization instance and, when its local meaning changes, an obtaining F.9 Bridge plus a separate use claim. A stated refinement between system-role kinds records how their state distinctions correspond; it must preserve the entailment needed for enactability rather than relying on similar role names.

_Relational stub:_

| Table | Key columns (essential) |
|---|---|
| **RSG_REFINEMENT** | `REFINEMENT_ID`; `SOURCE_SYSTEM_ROLE_KIND_ID`; `TARGET_SYSTEM_ROLE_KIND_ID`; `SOURCE_STATE_ID`; `TARGET_STATE_ID`; `ENTAILMENT_RULE`; `EVIDENCE_REF` |
| **CHECKLIST_REEXPRESSION** | `REEXPRESSION_ID`; `SRC_STATE_ID`; `TGT_STATE_ID`; `NORMALIZATION_INSTANCE_ID`; `BRIDGE_USE_CLAIM_REF?`; `SOURCE_EDITION`; `TARGET_EDITION`; `VALIDITY_WINDOW` |

At least one enactable source state must correspond under the stated rule to an enactable target state when that is the promised refinement. The re-expression record fixes the two editions and validity window so later changes can reopen the affected alignment rather than silently changing an old checklist.

### A.19.CN:9 - Anti‑patterns (and the fix)

| Anti‑pattern            | Symptom                                   | Why it hurts                 | Fix (CN‑Spec slot)                           |
| ----------------------- | ----------------------------------------- | ---------------------------- | --------------------------------------- |
| **Chartless number**    | “Latency = 120”                           | No unit/vantage → untestable | Fill `cs_basis` + `chart`                          |
| **Normalization smuggling**     | Quiet “per‑unit” normalisation mid‑stream | Trend reversal               | Declare UNM normalization references (`NormalizationMethodId` / `NormalizationMethodInstanceId`) + named invariants (see A.19.UNM)        |
| **Bridge-by-name**      | Reusing equal labels under different schemes | False comparability | Establish the exact F.9 relation and state the separate receiving use and tolerated loss |
| **Free‑hand averaging** | Arithmetic mean on bounded risks          | Violates WLNK                | Declare `Γ_fold` with WLNK              |
| **CN‑frame sprawl**        | Ten nearly‑identical CN‑frames               | Cognitive debt               | Use Registry + DRR; prefer reuse        |
| **Role conflation**     | Same person edits CN‑Spec & certifies data     | SoD breach                   | Enforce `CN‑frameSteward ⊥ CN‑frameCertifier` |

### A.19.CN:10 - Didactic quick cards (one‑liners teams reuse)

1. **Numbers travel with their basis.** Cite the characteristic and scale editions, bearer, reference or comparison basis, scope/window, and result.
2. **If the normalization is not declared, the trend is fiction.**
3. **WLNK beats wishful means.** Use weakest‑link folds for safety.
4. **Admit → Assert → Act.** (CN‑frame admission → RSG StateAssertion → Method step).
5. **Relate before reuse.** When local meanings differ, establish the exact Bridge, then state the separate receiving use, direction, rule, and tolerated loss.
6. **Steward writes, Certifier admits.** (SoD by design.)
7. **Charts are recipes.** Name the `MethodDescription` that made the number.
8. **Deprecate in the open.** CN‑frame cards carry DRR & retirement plans.
9. **Keep characteristics few, meanings sharp.** Prefer ≤ 7 characteristics per CN‑frame.
10. **No tooling names in Core.** Semantics first; notation later.
11. **Use method/instance IDs; avoid generic “map” nouns.** Prefer `NormalizationMethodId`/`NormalizationMethodInstanceId` (see the **A.19.UNM** lexical guard).

### A.19.CN:11 - SCR / RSCR Harness (acceptance & regression)

> **These are concept‑level checks; notation‑agnostic.**

#### A.19.CN:11.1 - **SCR — Acceptance (first introduction)**

* **SCR‑A19.4‑S01 (Completeness).** **CN‑Spec has **all** mandatory slots; `cs_basis` include **unit, scale, and polarity**; `chart` references a `MethodDescription`.
* **SCR‑A19.4‑S02 (Normalization clarity).** `normalization` cites the UNM mechanism (`UNM_id?`) and provides the normalization references required by the A.19.UNM governing pattern (methods / invariants / fix, and instances when used). If instances are referenced in assurance logs, their evidence/backing and validity constraints are handled by the governing evidence pattern (C.16), not by A.19.CN.
* **SCR‑A19.4‑S03 (Comparability test).** Provide one worked example showing **coordinatewise** or **normalization‑based** comparison end‑to‑end (with Evidence Graph Ref).
* **SCR‑A19.4‑S04 (Γ‑fold audit).** Aggregation rule spells out WLNK/COMM/LOC/MONO choices; reviewer reconstructs result on a toy set.
* **SCR‑A19.4‑S05 (SoD).** Distinct `RoleAssignments` for `CN‑frameStewardRole` and `CN‑frameCertifierRole` exist; windows do not overlap.
* **SCR‑A19.4‑S06 (bearer and anchors surfaced).** For each CN-Spec characteristic used in the worked example, cite its bearer, Characteristic and Scale editions, reference/comparison basis, scope/window, and the A.10 evidence anchors that support the reading.

#### A.19.CN:11.2 - **RSCR — Regression (on change)**

* **RSCR‑A19.4‑R01 (UNM edit).** When `normalization` changes, flag every comparison and Bridge-use claim that cites that normalization for affected-only reassessment, then rerun the corresponding worked comparisons.
* **RSCR‑A19.4‑R02 (Slot surgery/Basis surgery).** Adding/removing/renaming slot/basis requires a **new edition**; old data remain valid **for their edition**.
* **RSCR‑A19.4‑R03 (Chart drift).** Updating measurement protocol bumps edition; **historic Work** keeps old edition link.
* **RSCR‑A19.4‑R04 (Fold change).** Any change to `Γ_fold` invalidates cached roll‑ups; re‑compute or mark as superseded.
* **RSCR‑A19.4‑R05 (Bridge health).** After either endpoint's scheme, claim, or edition changes, revalidate the Bridge direction, correspondence, and loss before relying on it again; reopen only the claims that use it.
* **RSCR‑A19.4‑R06 (Deprecation rule).** On deprecating a CN‑frame, Registry lists its successor; bridges re‑targeted or retired.

### A.19.CN:12 - Interaction summary (wiring to the rest of the kernel)

* **A.2 / A.2.5 (Roles / RSG).** RSG **checklists** quote **CN‑Spec.acceptance**; enactment gates rely on **admitted** CN‑frame data.
* **B.1 (Γ‑algebra).** CN‑Spec’s `Γ_fold` instantiates Γ\_ctx/Γ\_time/WLNK/MONO choices explicitly.
* **B.3 (Assurance).** Bridge CL enters the **R** term; WLNK protects safety roll‑ups.
* **Current proof/inference support and the C.16/A.19 characterization stack.** Units, scales, and measurement templates come from C.16, A.17, A.18, and A.19. Claims about folds currently use C.2.1 for claim/episteme identity, A.10 for evidence and provenance, B.3 for assurance, and C.23 when method-family evidence or maturity is at issue. Planned C.6 LOG‑CAL may later consolidate proof-use semantics, but supplies no current governing force.

### A.19.CN:13 - Minimal CN‑Spec template (copy/paste, informational)

**Template note (refs-only).** This template shows *slot placement* for governance. Token semantics for normalization belong to the A.19.UNM governing pattern (A.19.UNM); indicatorization semantics belong to the indicatorization governing pattern (e.g., A.19.UINDM); evidence/backing semantics belong to C.16; admissibility/evidence gates belong to G.0.

```
CN‑frame: <Name>      Edition: <edition>      Bearer: <bearer ref>
ComparisonBasis: <corpus, baseline, reference state, or declared comparison set>
ScopeAndWindow: <scope ref and qualification interval, when used>
IntendedUse: <claim, comparison, admission, or aggregation use>
characteristics:
  - <CharacteristicName> : <Unit/Scale>  [Polarity: up|down|target-range]
Chart:
  reference_state: <text>
  coordinate_patch: <domain/subset>
  measurement_protocol_ref: <MethodDescriptionId>
Normalization:
  UNM: <UNMId?>
  methods: [<NormalizationMethodId>… ]
  method_descriptions: [<NormalizationMethodDescriptionRef>… ]
  invariants: [<property>… ]           # what ≡_UNM preserves (token semantics: see A.19.UNM)
  fix?: <NormalizationFixSpec>          # canonical representative of the ≡_UNM class (token semantics: see A.19.UNM)
Indicators (optional):
  policy_ref: <IndicatorChoicePolicyRef>
  resulting_indicators: [<IndicatorId>… ] // selection is policy‑defined; NCVs alone do not make an Indicator (see A.19.UINDM)
Comparability:
  mode: coordinatewise | normalization-based
  minimal_evidence: <what must be observed to compare>  # admissibility/evidence gate surface (see G.0 and C.16)
Aggregation:
  fold: <Γ_fold expr>   time_policy: <window, statistic>
  WLNK/COMM/LOC/MONO: <declared choices>
Acceptance:
  checklist: [<observable criterion>… ]
  window: <ISO 8601 interval>
  evidence_anchors: [<Observation/Evaluation ids>… ]
Alignment (optional):
  bridges: [<BridgeId, CL, kept/lost characteristics, extra guards>… ]
MaintenanceAndDeprecation:
  source_maintenance_role_assignment: <RoleAssignmentRef>
  DRR_links: [<DRR ids>… ]
  deprecation_plan: <short note>
```

**Implementation note (non‑normative): conceptual audit fields.** (For implementation completeness only; not part of the CN‑Spec normative surface.) The goal is *auditability*: any implementation should be able to cite the relevant refs (CN‑Spec edition, evidence anchors, UNM instance refs, Bridge ids) when producing a `StateAssertion`. The normative semantics of normalization and evidence/backing are governed by the corresponding mechanism and evidence patterns (e.g., A.19.UNM and C.16). A.19.CN does not prescribe storage formats.

### A.19.CN:Close

A.19.CN makes comparability operational: a one-page *CN-Spec*, a registry for edition, status, supersession, and deprecation records, explicit relations and receiving-use claims for cross-local reuse, and a checklist plus harness for audit. It remains tool-agnostic and keeps every reading tied to its characteristic and scale editions, bearer, comparison basis, scope/window, evidence, and intended use.

### A.19.CN:End

