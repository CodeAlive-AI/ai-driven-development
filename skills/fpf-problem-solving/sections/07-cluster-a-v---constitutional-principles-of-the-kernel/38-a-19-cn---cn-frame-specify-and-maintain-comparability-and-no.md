## A.19.CN - CN-frame: Specify and Maintain Comparability and Normalization

> **Scope.** Use a CN-frame to state which values may be compared for one bearer and intended use. Declare the characteristic space, chart, normalization and comparison basis in CN-Spec; maintain its editions and apply the conditions for each proposed reuse.
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

* a **CN‑frame** = a selected **CharacteristicSpace (CS)** + **chart** (coordinate patch and value basis, with Units where applicable) + a referenced **Normalization mechanism (UNM)** for one named bearer, comparison basis, scope/window, and intended use. A.19.UNM defines directed normalization, its preservation/loss basis and any separately justified `≡_UNM` class use;
* **operators** (subspace, product, pullback/pushforward) and **comparability** (coordinatewise vs **normalization‑based (normalize‑then‑compare)**);
* **RSG touch‑points**: role readiness (**RSG** states) are **certified** against CS via **checklists** over observable characteristics;
* **entity/relational mixtures** across CN‑frames via minimal schemas and bridges.

**Terminology guard.** *CN‑frame* is the **lens** (I); *CN‑Spec* is the specification (S) that fixes the bearer, characteristic and scale editions, chart, comparison basis, scope/window, normalization references, comparability rule, aggregation choice, and intended use; *CN‑Description* is the didactic surface (D) with worked examples and anti-patterns. Mechanism-level term cards such as `NormalizationMethod`, `NormalizationMethodInstance`, `NCV`, `≡_UNM`, and `IndicatorChoicePolicy` remain defined by the corresponding **A.19.<MechId>** patterns and are only cited here.

**Normalization names.** Use A.19.UNM’s method and instance identifiers to identify the selected normalization. Ordinary mathematical “mapping” describes its function; it does not assert a specialized FPF `Map` kind or an F.9 Bridge. Resolve a legacy identifier through F.18 alias docking when needed.

A.19.CN makes this *operational and auditable*.

### A.19.CN:2 - Problem

Absent a governance layer, four failure modes recur:

1. **Chartless numbers.** Measures move between teams without units, reference states, or declared normalization → **illusory comparability**.
2. **Hidden normalization flips.** Re‑parameterisations (e.g., normalising by batch size) silently alter meaning; trend lines lie.
3. **CN‑frame sprawl.** Every initiative mints a new “dashboard dimension”; semantics diverge; assurance collapses.
4. **Un‑bridgeable reports.** Cross‑team roll‑ups average **incongruent** CN‑frames, without a justified common comparison/aggregation model under B.3.

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
    polarity        : up|down|target-range|none,
    // if needed: missingness?, admissible_domain? (MM‑CHR-consistent metadata)
  }]
  chart             : { reference_state, coordinate_patch, measurement_protocol_ref?, value_ascription_basis? }
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
  aggregation?      : { Γ_fold, selected WLNK/COMM/LOC/MONO claims, time_policy }
  alignment?        : [{ bridge_ref, direction, correspondence_rule, tolerated_loss, reliance_ref? }]
  maintenance       : { source_maintenance_assignment, DRR_links, deprecation_plan }
}
```

**Reading:** the CN-frame is the selected characteristic space and chart for one named bearer and use. `CN‑Spec` pins the editions, comparison basis, scope and window, normalization references, aggregation choice, and admission evidence that make that use auditable. A.19.UNM still defines normalization semantics, A.19.UINDM defines indicatorization, C.16 supplies measurement and evidence backing, and G.0 supplies admissibility gates. CN‑Spec records the values used; it does not make a source, scope, or Bridge into a universal container. An actual `Γ_fold` cites its law and applicability basis. Its property codes express only the claims needed by this use; A.9 supplies an unresolved law choice or property check, while ULSAM retains the actual CHR fold and admissibility rules.

**Mechanism-reference note.** `UNM_id` identifies the admitted normalization mechanism. `NormalizationMethodId` and `NormalizationMethodInstanceId` retain the meanings declared by A.19.UNM, and evidence for a relied-on instance remains with C.16. CN‑Spec neither redefines those terms nor implies transport or a cross-local relation.

**L‑CN‑Spec‑NORM‑IDs (by reference).** Cite the normalization identifiers defined by A.19.UNM. Reference fields follow A.6.5: `*Ref` names a reference field and `*Slot` names a SlotKind.

#### A.19.CN:4.2 - CN-frame registry and conditional independent certification

First identify whether the receiving claim or applicable control requires independent certification of this exact CN-Spec edition or admission basis. When it does, the holder certifying it must not have authored or materially selected that basis. Include relevant earlier authoring whose content the certified basis retains. Renaming an assignment or waiting until an authoring assignment ends does not satisfy this condition.

Recover the actual holders, their relevant Work, the exact edition or basis and the applicable history under A.2.1 and A.2.7. Distinct assignments do not establish distinct holders. Missing history leaves independence unresolved. Different holders can satisfy this non-self-certification condition while their assignment windows overlap; any stronger organizational-independence or commissioning control still applies. The certifier's authority and adequacy of examination require their own grounds.

When no independent-certification claim or control applies, an adequately grounded one-person comparison can remain explicitly uncertified. Its measurement, comparison and reliance requirements still apply.

One named registry edition may publish the CN-frame's names, exact editions, characteristic-space and bearer references, the maintenance assignment, and the deprecation relation. When certification affects the receiving use, it also makes the applicable control, relied-on edition, certification result and supporting references recoverable. Distinguish:

* an adequate comparison for the named use with independent certification not required and no such claim made;
* a certification condition satisfied for the exact edition, with the participation, authority and examination grounds;
* a required condition that is unmet or unresolved, with its consequence for the dependent use under the applicable control.

These are different conclusions, not interchangeable registry labels. The registry helps discovery and currentness; it supplies no missing comparison, independence or certification evidence. A changed comparison basis reopens only the certification and receiving conclusions that rely on that change. A display-only registry change does not reopen them.

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

The Bridge establishes only the exact sense relation. A claim that uses it for comparison, admission, or aggregation remains a separate C.2.1 use claim with its direction, rule, and tolerated loss, together with the A.10 provenance account and any B.3 assurance result required for that use. No Bridge follows from matching names, and no reverse direction follows automatically. B.3 supplies any current loss effect on assurance; CN‑Spec may add operational guards but does not redefine that calculus.

### A.19.CN:5 - Conformance Checklist (normative)

> **Pass these and your CN‑frames are fit for assurance and cross‑team composition.**

**CC‑A19.D1‑1 (Local identity and scope).** Every CN-frame **MUST** identify its name and edition, bearer, characteristic space, reference or comparison basis, intended use, and any scope/window that qualifies the readings. The same label under another scheme or edition is not evidence of the same frame.

**CC‑A19.D1‑2 (Scales, units and preferred direction).** Each characteristic slot in `cs_basis` **MUST** declare its Scale and value meanings, its Unit when that Scale has one, and the polarity or target rule used by the comparison. State when no simple preferred direction applies.

**CC‑A19.D1‑3 (Chart).** `chart` **MUST** name its reference state and coordinate patch. For measured values, cite the applicable measurement method and protocol under C.16; for evaluated or otherwise ascribed values, cite the rule and basis that establish those values.

**CC‑A19.D1‑4 (Normalization references, not redefinition).** `normalization` **MUST** (i) cite the UNM mechanism (`UNM_id?`) and (ii) provide the normalization references required by the A.19.UNM governing pattern (methods / invariants / fix, and instances when used) so that any normalization‑based comparison is auditable. This pattern does not define what a “NormalizationMethod” is — it requires that CN‑Spec can point to the governing pattern that does.

**CC‑A19.D1‑5 (Comparability mode).** `comparability.mode` **MUST** be either **coordinatewise** (same chart & units) or **normalization‑based** (“normalize‑then‑compare” via the declared **UNM**). Mixed/implicit modes are prohibited. A.19.UNM governs the directed result and any optional classes. The receiving comparison must retain its required distinctions; equality of normalized outputs alone establishes no operational congruence. CN-Spec pins the chosen result branch and its basis.

**CC‑A19.D1‑6 (Admission checklist).** `acceptance.checklist_for_admission` **MUST** be observable and time‑bounded; each datum admitted to the CN‑frame **SHALL** cite a **StateAssertion** or equivalent `U.Evaluation`.

**CC‑A19.D1‑7 (Aggregation discipline).** When aggregation is used, `aggregation.Γ_fold` **MUST** identify the declared scale-lawful fold, its applicable algebraic properties and any required time policy. G.0 and A.19.ULSAM govern admissibility and the fold; B.3 applies when the fold serves an assurance claim. Keep the values separate when no fold is needed.

**CC‑A19.D1‑8 (Relation and use discipline).** When reuse depends on different exact F.17 local senses, the receiving claim **MUST** cite an obtaining F.9 Bridge with exact endpoints, direction, correspondence rule, applicable use, and tolerated loss. The comparison or aggregation remains a separate C.2.1 use claim, with the A.10 provenance account and any B.3 assurance result required by that use. Coordinate-by-name without that relation and use account fails.

**CC‑A19.D1‑9 (Conditional non-self-certification).** When the receiving claim or control requires independent certification, the certifying holder **MUST NOT** have authored or materially selected the exact CN-Spec edition or admission basis being certified, including relevant retained earlier content. Apply §4.2 to holder/Work/history, required authority and examination. Unknown history is unresolved. An adequate use with no such requirement may remain explicitly uncertified.

**CC‑A19.D1‑10 (Maintenance, deprecation, and DRR).** Every CN-Spec **MUST** carry a **source-maintenance role assignment**, a **deprecation plan**, and links to **DRR** entries for rationale and changes (Part E.9).

**CC‑A19.D1‑11 (Evidence for the receiving use).** An admission later used for comparison or aggregation **SHALL** retain the independently established measurement or evaluation results and support relations that the receiving use needs, including applicable currentness and validity windows. Use A.10 to recover their provenance and bounded use. Add B.3 assurance lanes and an assurance result only when the receiving use makes that assurance claim. Missing required inputs have the disposition declared by the comparison or aggregation rule.

**CC‑A19.D1‑12 (Notation independence).** CN‑Spec content **MUST NOT** depend on a tool or file format; semantics precede notation (E.5.2 Notational Independence).

**CC‑A19.D1‑13 (Lexical guard‑rails).** characteristic names and role labels **MUST** follow the Part E lexical discipline (registers, twin labels; no overloaded “process/service/function”).

### A.19.CN:6 - Consequences (informative)

| Benefit                           | Why it matters                                                                                                        |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Auditable comparability**       | Chart + declared normalization (UNM + NormalizationMethods) make “same number” meaningful; silent re‑basings become explicit, reviewable choices.                   |
| **Safe roll‑ups**                 | Γ-folds preserve only the properties justified by the named quantity, operation and dependency model.                                    |
| **Pluralism without incoherence** | Bridges with CL and loss notes allow federation without pretending to global sameness.                                |
| **RSG‑ready**                     | Admission checklists let **RSG** states reference **CN‑frame‑backed** facts (e.g., *Ready* requires characteristics within bounds). |

### A.19.CN:7 - Rationale (informative)

A comparison depends on the meaning and basis of its values. Keeping that basis with the CN-Spec makes a changed chart, normalization or intended use visible to the receiver. A claimed aggregation also needs its justified model; a required assurance claim retains its applicable loss policy under B.3.

### A.19.CN:8 - Archetypal Grounding *(Tell‑Show‑Show)*

> **Same slots, three arenas; no tooling implied.** The examples below use plain-language normalization descriptions as placeholders; any normative use must cite A.19.UNM-governed ids/refs (A.19.UNM) and evidence pins (C.16), not invent new terminology here.

#### A.19.CN:8.1 - **Industrial line** — *Weld‑quality CN‑frame* (`AssemblyLine_2026`)

* `cs_basis`: *BeadWidth\[mm] (target 6.0±0.2)*, *Porosity\[ppm] (↓)*, *SeamRate\[1/min] (↑ until limit)*
* `chart`: reference jig, fixture ID, torch type; `MethodDescription#Weld_MIG_v3`
* `normalization`: affine rescale on gray‑level calibration → invariant = physical porosity
* `comparability`: **normalization‑based (UNM)** (calibration tables applied)
* `aggregation`: a minimum bound only for a declared bottleneck quality model; commutative count addition only for disjoint contributions; time = per-shift histograms
* **RSG hook**: `WelderRole.Ready` requires *Porosity ≤ 500 ppm* & *BeadWidth within ±0.2 mm* admitted by this CN‑frame.

#### A.19.CN:8.2 - **Software/SRE line** — *Latency CN‑frame* (`SRE_Prod_Cluster_EU_2026`)

* `cs_basis`: *P50Latency\[ms] (↓)*, *P99Latency\[ms] (↓)*, *Load\[req/s]*
* `chart`: client vantage, trace sampler v4; `MethodDescription#HTTP_probe_v4`
* Before comparing a client end-to-end reading with a server processing reading, resolve their actual Characteristic and observation basis. Both may use ms yet answer different questions. Keep separate coordinates or obtain readings for the same declared characteristic and basis; a unit conversion alone cannot supply that match.
* `normalization`: monotone time‑warp compensation for collector skew; invariant = percentile order
* `comparability`: **normalization‑based (UNM)** with declared normalization
* `aggregation`: use a max-of-mins latency fold only when the declared service model justifies it; a WLNK bound needs its own bottleneck model. Neither follows from latency percentiles alone.
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
* `aggregation`: recombine subcohorts only under the declared population and weighting model; select the law or supported bound for each named safety outcome under its own justified dependency model.
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

#### A.19.CN:8.5 - Same basis, different holder and timing cases

For this worked case, the receiving comparison cites `CN-Spec E7`, and its commissioning control requires independent certification of E7's comparison basis. Alice authored that basis. After her stewardship assignment ends, she receives a certifier assignment and examines E7. The holder condition fails: the later assignment still certifies her own basis.

Bob's certifier assignment instead overlaps Alice's stewardship assignment. When Bob neither authored nor materially selected E7's basis, this local holder condition is satisfied despite the overlap. The receiver must still establish Bob's authority for E7, the required examination and any stronger organizational-independence condition from the commissioning control. Missing evidence for one of these conditions leaves that dependent certification conclusion open; different names alone do not establish it.

In an ordinary comparison with no independent-certification requirement or claim, Alice may use a sufficiently supported E7 basis and publish the comparison as uncertified. If E8 later changes the compared population or normalization basis, reopen only uses and certification claims depending on that changed basis. Correcting E7's registry display while its content and evidence stay fixed does not have that effect.

### A.19.CN:9 - Anti‑patterns (and the fix)

| Anti‑pattern            | Symptom                                   | Why it hurts                 | Fix (CN‑Spec slot)                           |
| ----------------------- | ----------------------------------------- | ---------------------------- | --------------------------------------- |
| **Chartless number**    | “Latency = 120”                           | No unit/vantage → untestable | Fill `cs_basis` + `chart`                          |
| **Normalization smuggling**     | Quiet “per‑unit” normalisation mid‑stream | Trend reversal               | Declare UNM normalization references (`NormalizationMethodId` / `NormalizationMethodInstanceId`) + named invariants (see A.19.UNM)        |
| **Bridge-by-name**      | Reusing equal labels under different schemes | False comparability | Establish the exact F.9 relation and state the separate receiving use and tolerated loss |
| **Free-hand averaging** | An arithmetic mean is used without a model for the intended risk result | The number can answer the wrong question | Use A.9 to select a justified law, bound or separate-input result; declare an actual `Γ_fold` only for the selected fold |
| **CN‑frame sprawl**        | Ten nearly‑identical CN‑frames               | Cognitive debt               | Use Registry + DRR; prefer reuse        |
| **Self-certification hidden by assignments** | A holder authors the basis and later certifies it under a new role | A required independent check still examines that holder's own basis | Apply §4.2 to actual participation in the exact edition; separate authority and examination, and keep uncertified use explicit when certification is not required |

### A.19.CN:10 - Didactic quick cards (one‑liners teams reuse)

1. **Numbers travel with their basis.** Cite the characteristic and scale editions, bearer, reference or comparison basis, scope/window, and result.
2. **If the normalization is not declared, the trend is fiction.**
3. **The intended result selects the law.** Use a weakest-part bound only when its declared dependency model justifies it; a safety label alone selects no fold.
4. **Admit → Assert → Act.** (CN‑frame admission → RSG StateAssertion → Method step).
5. **Relate before reuse.** When local meanings differ, establish the exact Bridge, then state the separate receiving use, direction, rule, and tolerated loss.
6. **When independence is required, check who made the basis.** A later role assignment does not remove self-certification; a sufficient uncertified comparison remains possible when no independent certification is required.
7. **Ground each chart value.** Name the reference state and coordinate patch. For measured values, cite the applicable measurement method and protocol; for evaluated or otherwise ascribed values, cite their rule and basis.
8. **Deprecate in the open.** CN‑frame cards carry DRR & retirement plans.
9. **Keep characteristics few, meanings sharp.** Prefer ≤ 7 characteristics per CN‑frame.
10. **Identify the normalization used.** Cite its method and instance under A.19.UNM; ordinary mathematical mapping language alone identifies neither.

### A.19.CN:11 - SCR / RSCR Harness (acceptance & regression)

> **These are concept‑level checks; notation‑agnostic.**

#### A.19.CN:11.1 - **SCR — Acceptance (first introduction)**

* **SCR‑A19.4‑S01 (Completeness).** CN-Spec has every applicable mandatory value. Each cs_basis position declares its Scale and value meanings, Unit when that Scale has one, and the comparison's polarity or target rule, including no preferred direction when appropriate. The chart names its reference state and coordinate patch; measured values cite their C.16 measurement method/protocol, while evaluated or otherwise ascribed values cite the rule and basis that establish them, as required by CC-A19.D1-2 and CC-A19.D1-3.
* **SCR‑A19.4‑S02 (Normalization clarity).** `normalization` cites the UNM mechanism (`UNM_id?`) and provides the normalization references required by the A.19.UNM governing pattern (methods / invariants / fix, and instances when used). If instances are referenced in assurance logs, their evidence/backing and validity constraints are handled by the governing evidence pattern (C.16), not by A.19.CN.
* **SCR‑A19.4‑S03 (Comparability test).** Provide one worked example showing **coordinatewise** or **normalization‑based** comparison end‑to‑end (with Evidence Graph Ref).
* **SCR‑A19.4‑S04 (Γ‑fold audit).** The aggregation rule states the intended result, law and applicability basis, with only the required property claims; the reviewer reconstructs the result on a toy set under that model.
* **SCR‑A19.4‑S05 (Required certification).** Identify the exact receiving claim/control and relied-on CN-Spec edition or admission basis. If independent certification is required, check the actual certifier against authoring/material-selection history, then the independently applicable authority and examination conditions. Replay both successive same-holder assignments and overlapping different-holder assignments. If certification is not required, keep the adequate comparison explicitly uncertified.
* **SCR‑A19.4‑S06 (bearer and anchors surfaced).** For each CN-Spec characteristic used in the worked example, cite its bearer, Characteristic and Scale editions, reference/comparison basis, scope/window, and the A.10 evidence anchors that support the reading.

#### A.19.CN:11.2 - **RSCR — Regression (on change)**

* **RSCR‑A19.4‑R01 (UNM edit).** When `normalization` changes, flag every comparison and Bridge-use claim that cites that normalization for affected-only reassessment, then rerun the corresponding worked comparisons.
* **RSCR‑A19.4‑R02 (Slot surgery/Basis surgery).** Adding/removing/renaming slot/basis requires a **new edition**; old data remain valid **for their edition**.
* **RSCR‑A19.4‑R03 (Chart drift).** Updating measurement protocol bumps edition; **historic Work** keeps old edition link.
* **RSCR‑A19.4‑R04 (Fold change).** Any change to `Γ_fold` invalidates cached roll‑ups; re‑compute or mark as superseded.
* **RSCR‑A19.4‑R05 (Bridge health).** After either endpoint's scheme, claim, or edition changes, revalidate the Bridge direction, correspondence, and loss before relying on it again; reopen only the claims that use it.
* **RSCR‑A19.4‑R06 (Deprecation rule).** On deprecating a CN‑frame, Registry lists its successor; bridges re‑targeted or retired.
* **RSCR‑A19.4‑R07 (Certification basis).** A change to the relied-on basis, relevant participation history or applicable control reopens only the certification and receiving conclusions it can change. A registry display change alone does not.

### A.19.CN:12 - Interaction summary (wiring to the rest of the kernel)

* **A.2 / A.2.5 (Roles / RSG).** RSG **checklists** quote **CN‑Spec.acceptance**; enactment gates rely on **admitted** CN‑frame data.
* **B.1 and A.9.** B.1 supplies any claimed whole/part construction; A.9 supplies an unresolved aggregation-law choice or property check. CN-Spec records the justified `Γ_fold`, including its model and time policy.
* **B.3 (Assurance).** Bridge CL enters the **R** term; a safety roll-up requires the law or bound justified for its named outcome and dependency model.
* **Current proof/inference support and the C.16/A.19 characterization stack.** Units, scales, and measurement templates come from C.16, A.17, A.18, and A.19. Claims about folds currently use C.2.1 for claim/episteme identity, A.10 for evidence and provenance, B.3 for assurance, and C.23 when method-family evidence or maturity is at issue. Planned C.6 LOG‑CAL may later consolidate proof-use semantics, but supplies no current governing force.

### A.19.CN:13 - Minimal CN‑Spec template (copy/paste, informational)

**Template note (refs-only).** This template shows *slot placement* for governance. Token semantics for normalization belong to the A.19.UNM governing pattern (A.19.UNM); indicatorization semantics belong to the indicatorization governing pattern (e.g., A.19.UINDM); evidence/backing semantics belong to C.16; admissibility/evidence gates belong to G.0.

```
CN‑frame: <Name>      Edition: <edition>      Bearer: <bearer ref>
ComparisonBasis: <corpus, baseline, reference state, or declared comparison set>
ScopeAndWindow: <scope ref and qualification interval, when used>
IntendedUse: <claim, comparison, admission, or aggregation use>
characteristics:
  - <CharacteristicName> : <Scale; Unit when applicable>  [Polarity: up|down|target-range|none]
Chart:
  reference_state: <text>
  coordinate_patch: <domain/subset>
  measurement_protocol_ref?: <applicable measurement MethodDescriptionId>
  value_ascription_basis?: <applicable evaluation rule and evidence>
Normalization:
  UNM: <UNMId?>
  methods: [<NormalizationMethodId>… ]
  method_descriptions: [<NormalizationMethodDescriptionRef>… ]
  invariants: [<property>… ]           # what the selected transformation preserves; name losses too (A.19.UNM)
  fix?: <NormalizationFixSpec>          # only for an established class whose receiving use needs a representative (A.19.UNM)
Indicators (optional):
  policy_ref: <IndicatorChoicePolicyRef>
  resulting_indicators: [<IndicatorId>… ] // selection is policy‑defined; NCVs alone do not make an Indicator (see A.19.UINDM)
Comparability:
  mode: coordinatewise | normalization-based
  minimal_evidence: <what must be observed to compare>  # admissibility/evidence gate surface (see G.0 and C.16)
Aggregation:
  fold: <Γ_fold expr>   time_policy: <window, statistic>
  WLNK/COMM/LOC/MONO: <only selected property claims, with their model and applicability basis>
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

### A.19.CN:14 - SoTA-Echoing — enough basis to compare coordinate values

**Practice question.** What must accompany two chart values before a practitioner treats them as comparable? The selected best-known line identifies the bearer/property, value-producing procedure or evaluation rule, relevant time and result basis alongside Scale/Unit meanings. A serious smaller alternative is to carry only the quantity kind, value and unit, converting units before comparison.

The [QUDT quantity model](https://www.qudt.org/pages/QUDToverviewPage.html) is the useful comparator: it separates Quantity, QuantityKind, QuantityValue and Unit and supports precise quantity descriptions. **Adopt** that discipline where a Unit applies. Using only that portion is cheaper and sufficient when the same property, procedure and observation basis are already fixed outside the record. **Reject** treating it alone as evidence that two independently obtained readings answer the same question; this is a limit of that reduced use, not a claim that QUDT forbids richer descriptions.

The [SOSA/SSN 2023-edition working draft of 24 September 2026](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20260924/) supplies the compared observation/procedure line: it distinguishes the feature, observed property, procedure, result and temporal qualifications. **Adapt** that separation in CN-Spec's bearer, cs_basis and chart, CC-A19.D1-1/-3/-11, and SCR-S01. The source is work in progress and does not establish FPF admission, Scale lawfulness, certification independence or a Bridge; those retain their direct rules. An evaluated coordinate keeps its actual rule and basis rather than acquiring a fictive measurement or Unit.

At comparable effort, both alternatives start from the same pair of readings and existing method records. The selected line adds the references that can change this comparison, reusing common frame-level values rather than repeating a full observation history for every cell. The SRE case in §8.2 shows the gain: equal millisecond units cannot make client end-to-end latency and server processing latency the same Characteristic. Keep them separate or obtain values for the same declared characteristic and observation basis. The added references cost more than a bare numeric pair; that cost is accepted when the basis is not already common and recoverable.

Reopen when a proposed comparison changes the property, value-producing rule, reference state or relevant window, or when a smaller representation demonstrably retains all the distinctions needed by that use. These sources support the compared representational choices; they do not validate every CN-frame or make its registry self-certifying.

### A.19.CN:Close

A.19.CN makes comparability operational: a one-page *CN-Spec*, a registry for edition, status, supersession, and deprecation records, explicit relations and receiving-use claims for cross-local reuse, and a checklist plus harness for audit. It remains tool-agnostic and keeps every reading tied to its characteristic and scale editions, bearer, comparison basis, scope/window, evidence, and intended use.

### A.19.CN:End
