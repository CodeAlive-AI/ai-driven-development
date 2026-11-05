## A.19.CN - CN-frame: Specify and Maintain Comparability and Normalization

> **Status:** Stable

> **Scope.** Use a CN-frame to state which values may be compared for one bearer and intended use. Declare the characteristic space, chart and comparison basis in CN-Spec, adding normalization when needed. Maintain editions retained for later reuse or shared use, and apply the conditions for each proposed reuse.
>
> **Use this when** readings need a recoverable comparison basis or a changed basis may affect their reuse. Keep the bearer, Characteristic and Scale meanings, observation or evaluation basis and intended comparison together. An already sufficient account can serve as CN-Spec; its notation is unrestricted. Apply the corresponding `A.19` mechanism pattern when normalization, indicatorization, scoring, aggregation, comparison or selection is actually needed. C.16 governs measurement backing and G.0 governs the applicable admission conditions.
>
> **Reader guide (fast navigation).**
> - “What does `NormalizationMethodId/…InstanceId/≡_UNM/NormalizationFix` mean?” → **A.19.UNM**.
> - “What is an Indicator / `IndicatorChoicePolicy` and why NCV ≠ Indicator?” → **A.19.UINDM**.
> - “Why can we trust a normalization / where does calibration or evidence live?” → **C.16 (MM‑CHR)**.
> - “What is admissible to compare or aggregate, and what is `MinimalEvidence`?” -> **G.0 (CG-Spec)**.

### A.19.CN:1 - Context

A.19 established a substrate‑neutral picture:

* a **CN‑frame** = a selected **CharacteristicSpace (CS)** + **chart** (coordinate patch and value basis, with Units where applicable) + a referenced **Normalization mechanism (UNM)** when the use needs normalization, for one named bearer, comparison basis, intended use, and any scope/window that qualifies it. A.19.UNM defines directed normalization, its preservation/loss basis and any separately justified `≡_UNM` class use;
* **operators** (subspace, product, pullback/pushforward) and **comparability** (coordinatewise vs **normalization‑based (normalize‑then‑compare)**);
* **RSG touch-points**: state predicates use observable characteristics; an evaluation establishes whether their conditions hold for the named bearer and window;
* **entity/relational mixtures** across CN‑frames, represented by the schemas in §8.4, with each required correspondence grounded under its own rule.

**Frame, specification and explanation.** A *CN‑frame* is the selected basis for interpreting and comparing the readings. Its *CN‑Spec* fixes the bearer, characteristic and scale editions, chart, comparison basis, comparability rule, intended use and qualifying scope/window, with normalization and aggregation choices when used. A *CN‑Description* explains that basis through worked examples and anti-patterns. Mechanism-level terms such as `NormalizationMethod`, `NormalizationMethodInstance`, `NCV`, `≡_UNM`, and `IndicatorChoicePolicy` retain the definitions supplied by the corresponding `A.19.<MechId>` patterns.

**Normalization names.** Use A.19.UNM’s method and instance identifiers to identify the selected normalization. Ordinary mathematical “mapping” describes its function; it does not assert a specialized FPF `Map` kind or an F.9 Bridge. Resolve a legacy identifier through F.18 alias docking when needed.

The practitioner can compare values within this declared basis and identify which conclusions need reconsideration when it changes.

### A.19.CN:2 - Problem

When the comparison basis is missing or changes silently, these failures can occur:

1. **Chartless numbers.** Measures move between teams without units, reference states, or declared normalization → **illusory comparability**.
2. **Hidden normalization changes.** Re-parameterisation, such as normalising by batch size, can change the quantity being compared while a trend line still appears continuous.
3. **CN-frame sprawl.** Unrelated dashboard definitions can leave receivers unable to establish a shared comparison basis.
4. **Incompatible roll-ups.** Cross-team roll-ups average **incongruent** CN-frames without a justified common comparison or aggregation model. Use B.3 when the result serves a named assurance claim.

### A.19.CN:3 - Forces

| Force                         | Tension we must balance                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------ |
| **Universality vs nuance**    | One Standard for robotics, safety, and finance, while each named source scheme retains its own exact meanings. |
| **Speed vs audit**            | A short sufficient comparison basis; further evidence when assurance or independent certification is required.                   |
| **Local truth vs federation** | Keep meanings tied to their exact schemes and claims; still allow explicit relations and bounded receiving uses. |
| **Minimalism vs safety**      | Few mandatory slots; enough structure to forbid silent normalization drift.                  |

### A.19.CN:4 - Solution — Specify the comparison basis and maintain it when reused

#### A.19.CN:4.1 - The **CN‑Spec** (comparability and normalization specification)

A **CN‑frame** is described by a compact, notation-free specification. The specification names the bearer and the exact boundary within which its readings may be compared:

```
CN‑Spec {
  name              : CN‑frameName
  edition           : <edition>
  bearer_ref        : <evaluated bearer or bearer kind>
  characteristic_space_ref : <CharacteristicSpaceRef>
  characteristicSpaceDescriptionRef? : <U.EpistemeRef to the exact defining/description episteme>
  scope_ref?        : <ClaimScopeRef>
  window?           : <qualification interval>
  reference_or_comparison_basis : <corpus, baseline, reference state, or declared comparison set>
  cs_basis          : [{
    slot_id         : <tech-token>,
    characteristic  : <Characteristic defined under A.17>,
    scale           : { type: nominal|ordinal|interval|ratio, unit?: <measurement unit under A.18/C.16>, bounds?: <…> },
    polarity?       : <preference rule when ranking desirability; e.g. up, down or target-range>,
    // if needed: missingness?, admissible_domain? (MM‑CHR-consistent metadata)
  }]
  chart             : { reference_state, coordinate_patch, measurement_protocol_ref?, value_ascription_basis? }
  normalization?    : {
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
  acceptance        : { checklist_for_admission, window?, evidence_anchors }
  aggregation?      : { Γ_fold, selected WLNK/COMM/LOC/MONO claims, time_policy }
  alignment?        : { semantic_uses?: <Bridges and separate bounded-use claims under §4.3>, plane_relation_refs?: <applicable plane relations> }
  maintenance?      : { responsibility, DRR_links?, applicable_deprecation_arrangement }
}
```

**Reading:** the CN-frame is the selected characteristic space and chart for one named bearer and use. The normalization block is needed for normalization-based comparison; direct coordinatewise comparison can omit it. Add maintenance arrangements when the specification is retained for later reuse or maintained as a shared edition. `CN‑Spec` fixes the editions, comparison basis, qualifying scope/window and admission evidence needed by that use, with normalization references and aggregation choices when used. A.19.UNM defines normalization semantics, A.19.UINDM defines indicatorization, C.16 supplies measurement and evidence backing, and G.0 supplies the applicable admission conditions. An actual `Γ_fold` cites its law and applicability basis. Its property codes express only the claims needed by this use; A.9 supplies an unresolved law choice or property check, while ULSAM retains the actual CHR fold and admissibility rules.

The space reference selects the space itself. Add `characteristicSpaceDescriptionRef` when the selected use needs one exact definition or description edition; UNM and UINDM require this pin for their applications. Resolve the pair under A.19:5.1.1.1 and check that the description supplies the basis of that same space. An unchanged space may have a different description episteme, and a changed basis may require a different space even when the description retains its familiar title.

**Mechanism-reference note.** `UNM_id` identifies the admitted normalization mechanism. `NormalizationMethodId` and `NormalizationMethodInstanceId` retain the meanings declared by A.19.UNM, and evidence for a relied-on instance remains with C.16. CN‑Spec neither redefines those terms nor implies transport or a cross-local relation.

**L‑CN‑Spec‑NORM‑IDs (by reference).** Cite the normalization identifiers defined by A.19.UNM.

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

When a comparison or reuse needs a semantic correspondence or difference between two exact F.17 local senses, test the direct F.9 predicate. Cite a Bridge only when it obtains; otherwise retain the actual F.9 exit and its reason. A use that needs an absent or unresolved correspondence remains unsupported. A coordinate mapping or plane relation keeps its own grounds. A compact account may show an obtaining Bridge and its separate bounded-use claim together:

```
Bridge: <obtaining occurrence between exact source and receiving F.17 cells>
  predicate_profile: <relation kind, endpoint readings and obtaining condition>
BoundedUseClaim:
  applicable_use: <the receiving comparison, admission or aggregation>
  direction: <source-to-receiving use>
  correspondence_rule: <how the local claims are used together>
  tolerated_loss: <declared limit for this use>
  polarity: affirmative | negative
  grounds: <kept/lost distinctions and other support or counterevidence>
  coordinate_transform?: <separately justified pullback, pushforward, re-scaling, re-binning, etc.>
  plane_relation_ref?: <only when a separately defined plane relation obtains>
  reliance_ref?: <required reliance judgement for this use>
  assurance_ref?: <result for a current named assurance claim>
  extra_guards?: {additional evidence, required review, or an authorized exception within its applicable scope}
```

The Bridge is only the exact sense relation. The separate C.2.1 claim states whether it suits the named use, direction, rule and tolerated loss. For reliance on an affirmative claim, obtain or reuse the A.10 disposition required by F.9:4.2; a negative or unresolved claim supplies no positive use basis. Add a B.3 result only for a current named assurance claim. Matching names establish no Bridge, and a reverse use needs its own justified direction. B.3 determines any assurance consequence under the selected argument or model; CN-Spec may state additional receiving-use conditions.

### A.19.CN:5 - Conformance Checklist (normative)

> These checks establish the declared comparison basis. Assurance and cross-team reuse still require the evidence and relation conditions of their receiving claims.

**CC‑A19.D1‑1 (Local identity and scope).** Every CN-frame **MUST** identify its name and edition, bearer, characteristic space, reference or comparison basis, intended use, and any scope/window that qualifies the readings. The same label under another scheme or edition is not evidence of the same frame.

**CC‑A19.D1‑2 (Scales, units and preference).** Each characteristic slot in `cs_basis` **MUST** declare its Scale and value meanings, and its Unit when that Scale has one. A comparison that ranks values by desirability **MUST** state its preference rule. Descriptive comparisons need no preference rule.

**CC‑A19.D1‑3 (Chart).** `chart` **MUST** name its reference state and coordinate patch. For measured values, cite the applicable measurement method and protocol under C.16; for evaluated or otherwise ascribed values, cite the rule and basis that establish those values.

**CC‑A19.D1‑4 (Normalization references, not redefinition).** When normalization is used, `normalization` **MUST** identify the admitted mechanism and provide the normalization references required by the A.19.UNM governing pattern (methods / invariants / fix, and instances when used) so that any normalization‑based comparison is auditable. This pattern does not define what a “NormalizationMethod” is — it requires that CN‑Spec can point to the governing pattern that does.

**CC‑A19.D1‑5 (Comparability mode).** `comparability.mode` **MUST** be either **coordinatewise** (same chart, Scales and applicable Units) or **normalization‑based** (“normalize‑then‑compare” via the declared **UNM**). Mixed/implicit modes are prohibited. A.19.UNM governs the directed result and any optional classes. The receiving comparison must retain its required distinctions; equality of normalized outputs alone establishes no operational congruence. CN-Spec pins the chosen result branch and its basis.

**CC‑A19.D1‑6 (Admission checklist).** `acceptance.checklist_for_admission` **MUST** state testable conditions and any interval needed for the intended use. Each admitted datum **SHALL** have the measurement, evaluation or other value-ascription basis required by that use. Cite a StateAssertion when a state claim is being made; a datum is not automatically such a claim.

**CC‑A19.D1‑7 (Aggregation discipline).** When aggregation is used, `aggregation.Γ_fold` **MUST** identify the declared scale-lawful fold, its applicable algebraic properties and any required time policy. G.0 and A.19.ULSAM govern admissibility and the fold; B.3 applies when the fold serves an assurance claim. Keep the values separate when no fold is needed.

**CC‑A19.D1‑8 (Relation and use discipline).** When reuse depends on a semantic correspondence or difference between two exact F.17 local senses, test the F.9 predicate and cite a Bridge only when it obtains. To use an obtaining Bridge, the receiving C.2.1 claim **MUST** separately state the use, direction, correspondence rule, tolerated loss and polarity. Reliance on an affirmative claim requires the A.10 disposition under F.9:4.2; a named assurance use also requires its B.3 result. Missing or unresolved required correspondence blocks the dependent use. A coordinate mapping and any applicable plane relation retain their separate grounds.

**CC‑A19.D1‑9 (Conditional non-self-certification).** When the receiving claim or control requires independent certification, the certifying holder **MUST NOT** have authored or materially selected the exact CN-Spec edition or admission basis being certified, including relevant retained earlier content. Apply §4.2 to holder/Work/history, required authority and examination. Unknown history is unresolved. An adequate use with no such requirement may remain explicitly uncertified.

**CC‑A19.D1‑10 (Maintenance, deprecation, and DRR).** A CN-Spec maintained for later reuse or as a shared edition **MUST** make its maintenance responsibility, applicable deprecation arrangement and consequential decisions recoverable. Use E.9 for decisions that need a DRR. A one-use comparison need not invent a maintenance assignment or retirement plan.

**CC‑A19.D1‑11 (Evidence for the receiving use).** An admission later used for comparison or aggregation **SHALL** retain the independently established measurement, evaluation or other value-ascription results and support relations that the receiving use needs, including applicable currentness and validity windows. Use A.10 when their provenance or bounded reliance must remain replayable. Add B.3 assurance lanes and an assurance result only when the receiving use makes that assurance claim. Missing required inputs have the disposition declared by the comparison or aggregation rule.

**CC‑A19.D1‑12 (Notation independence).** CN‑Spec content **MUST NOT** depend on a tool or file format; semantics precede notation (E.5.2 Notational Independence).

**CC‑A19.D1‑13 (Recoverable names).** Characteristic names and role labels **MUST** preserve the distinctions required by the comparison. Apply Part E lexical guidance and F.18 where a durable name or alias is needed.

### A.19.CN:6 - Consequences (informative)

| Benefit                           | Why it matters                                                                                                        |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Auditable comparability**       | Chart and any required normalization expose the basis on which equal numbers may be compared; changes to that basis remain visible.                   |
| **Safe roll‑ups**                 | Γ-folds preserve only the properties justified by the named quantity, operation and dependency model.                                    |
| **Pluralism without incoherence** | Obtaining Bridges and separately grounded use claims support the stated cross-local reuse. Retain the observed losses and required reliance; use CL only as optional evidence shorthand. |
| **RSG‑ready**                     | Admission checklists let **RSG** states reference **CN‑frame‑backed** facts (e.g., *Ready* requires characteristics within bounds). |

### A.19.CN:7 - Rationale (informative)

A comparison depends on the meaning and basis of its values. Keeping that basis with the CN-Spec makes a changed chart, normalization or intended use visible to the receiver. A claimed aggregation also needs its justified model; a required assurance claim retains its applicable loss policy under B.3.

### A.19.CN:8 - Archetypal Grounding

> The cases use plain-language normalization descriptions to illustrate the choices. Applying a selected normalization requires its A.19.UNM method and instance references and the backing required by C.16.

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
    polarity: none
* `chart`: cohort definition; `MethodDescription#TrialProtocol_v5`
* `normalization`: the named propensity-score case-mix adjustment uses its declared covariates and target population to estimate the specified ΔBP contrast. Preserve the estimand, adjustment assumptions and residual limitations; the adjusted estimate is an output, not an invariant guaranteed by the method name.
* `comparability`: **normalization‑based (UNM)** (post‑adjustment)
* `aggregation`: recombine subcohorts only under the declared population and weighting model; select the law or supported bound for each named safety outcome under its own justified dependency model.
* **RSG hook**: evidence-use validation of an admission requires CN-frame acceptance. A named assurance claim uses B.3 and the relation or bounded-use evidence its argument needs; CL may summarize that evidence but supplies no automatic assurance result.

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

The System is classified under the exact local system-role kind and participates in the obtaining assignment used by this RSG account. A deliberately asserted evaluation or operational Work additionally needs the complete A.13 core: the performing System, exact local agential-role kind and its membership criterion, and an obtaining assignment of its declared direct species for the relevant scope and time. A.15.1 independently admits the Work; F.6 applies afterward only when precise assignment-bound attribution is needed. The schema abbreviates these grounds; its arrows do not establish them. A role-state graph lists states such as Ready, Waiting, or Degraded. Evaluation applies the state checklist and supports a StateAssertion. In this gating use, operational enactment requires an admissible assertion that an enactable state obtains; the Work, Method, assignment, and result remain different objects.

_Relational stub:_

| Table | Key columns (essential) |
|---|---|
| **ROLE_ASSIGNMENT** | `RA_ID`; `HOLDER_SYSTEM_ID`; `SYSTEM_ROLE_KIND_ID`; `REFERENCE_SCHEME_ID`; `SCOPE_REF?`; `WINDOW_FROM`; `WINDOW_TO` |
| **RCS_SNAPSHOT** | `SNAP_ID`; `RA_ID`; `WINDOW_FROM`; `WINDOW_TO`; `CHAR_ID`; `VALUE`; `UNIT?`; `SCALE_TYPE`; `RESULT_REF` |
| **RSG_STATE** | `STATE_ID`; `SYSTEM_ROLE_KIND_ID`; `NAME`; `ENACTABLE` |
| **CHECKLIST** | `CHK_ID`; `STATE_ID`; `PREDICATE_TYPE`; `PREDICATE_SPEC` |
| **STATE_ASSERTION** | `SA_ID`; `RA_ID`; `STATE_ID`; `CHK_ID`; `WINDOW_FROM`; `WINDOW_TO`; `VERDICT`; `NORMALIZATION_INSTANCE_ID?`; `BRIDGE_USE_CLAIM_REF?` |
| **WORK** | `WORK_ID`; `PERFORMER_SYSTEM_ID`; `METHOD_ID`; `WINDOW_FROM`; `WINDOW_TO`; result and evidence refs as needed |

The RCS snapshot keeps the characteristic, value, any applicable unit, scale, window, and result identity visible. A StateAssertion separately identifies any normalization instance and any claim that uses a Bridge. An enactment query can therefore ask whether the latest admissible assertion for this assignment has an enactable state and a passing verdict without treating a role label, CN-frame, or Bridge as the acting System.

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
| **BRIDGE** | `BRIDGE_ID`; `SOURCE_CELL_REF`; `TARGET_CELL_REF`; `PREDICATE_PROFILE` |
| **BRIDGE_USE_CLAIM** | `BOUNDED_USE_CLAIM_ID`; `BRIDGE_ID`; `DIRECTION`; `CORRESPONDENCE_RULE`; `APPLICABLE_USE`; `TOLERATED_LOSS`; `POLARITY` |
| **COMPARISON_USE** | `USE_CLAIM_ID`; `RESULT_REF`; `NORMALIZATION_INSTANCE_ID?`; `BRIDGE_USE_CLAIM_REF?`; `EVIDENCE_USE_REF`; `ASSURANCE_REF?` |
| **ASSURANCE_EVENT** | `AE_ID`; `USE_CLAIM_ID`; `EFFECT`; `DETAILS`; `WINDOW` |

The table can express the relevant claims and their audit path; its presence supplies no missing evidence. A changed assurance result, stale normalization instance, or revised evidence can reopen only the comparisons whose grounds it changes.

##### A.19.CN:8.4.3 - Alignment CN‑frame — design-time reuse across local schemes

_Entity graph view:_

```
Checklist for target state ← re-expression (N when normalization is used) ─ Checklist for source state
source F.17 cell ── obtaining Bridge under its predicate profile ──> receiving F.17 cell
SystemRoleKind' ── stated refinement relation ──> SystemRoleKind
```

A checklist re-expression cites the normalization instance when it uses normalization. When it also needs a semantic correspondence or difference between exact local senses, apply §4.3: test the F.9 predicate, retain any missing or unresolved required correspondence, and separately ground the use of an obtaining Bridge. A stated refinement between system-role kinds records how their state distinctions correspond; it must preserve the entailment needed for enactability rather than relying on similar role names.

_Relational stub:_

| Table | Key columns (essential) |
|---|---|
| **RSG_REFINEMENT** | `REFINEMENT_ID`; `SOURCE_SYSTEM_ROLE_KIND_ID`; `TARGET_SYSTEM_ROLE_KIND_ID`; `SOURCE_STATE_ID`; `TARGET_STATE_ID`; `ENTAILMENT_RULE`; `EVIDENCE_REF` |
| **CHECKLIST_REEXPRESSION** | `REEXPRESSION_ID`; `SRC_STATE_ID`; `TGT_STATE_ID`; `NORMALIZATION_INSTANCE_ID?`; `BRIDGE_USE_CLAIM_REF?`; `SOURCE_EDITION`; `TARGET_EDITION`; `VALIDITY_WINDOW?` |

At least one enactable source state must correspond under the stated rule to an enactable target state when that is the promised refinement. The re-expression record fixes the two editions and any validity window required by the re-expression or receiving use, so later changes can reopen the affected alignment rather than silently changing an old checklist. A referenced UNM instance retains its required validity window.

#### A.19.CN:8.5 - Same basis, different holder and timing cases

For this worked case, the receiving comparison cites `CN-Spec E7`, and its commissioning control requires independent certification of E7's comparison basis. Alice authored that basis. After her stewardship assignment ends, she receives a certifier assignment and examines E7. The holder condition fails: the later assignment still certifies her own basis.

Bob's certifier assignment instead overlaps Alice's stewardship assignment. When Bob neither authored nor materially selected E7's basis, this local holder condition is satisfied despite the overlap. The receiver must still establish Bob's authority for E7, the required examination and any stronger organizational-independence condition from the commissioning control. Missing evidence for one of these conditions leaves that dependent certification conclusion open; different names alone do not establish it.

In an ordinary comparison with no independent-certification requirement or claim, Alice may use a sufficiently supported E7 basis and publish the comparison as uncertified. If E8 later changes the compared population or normalization basis, reopen only uses and certification claims depending on that changed basis. Correcting E7's registry display while its content and evidence stay fixed does not have that effect.

### A.19.CN:9 - Anti‑patterns (and the fix)

| Anti‑pattern            | Symptom                                   | Why it hurts                 | Fix (CN‑Spec slot)                           |
| ----------------------- | ----------------------------------------- | ---------------------------- | --------------------------------------- |
| **Chartless number**    | “Latency = 120”                           | No unit/vantage → untestable | Fill `cs_basis` + `chart`                          |
| **Normalization smuggling**     | Quiet “per‑unit” normalisation mid‑stream | Trend reversal               | Declare UNM normalization references (`NormalizationMethodId` / `NormalizationMethodInstanceId`) + named invariants (see A.19.UNM)        |
| **Bridge-by-name** | Reusing equal labels under different schemes | False comparability | Test the needed F.9 predicate; cite a Bridge only when it obtains, then ground the separate receiving-use claim and reliance. An unsupported required correspondence blocks that use. |
| **Free-hand averaging** | An arithmetic mean is used without a model for the intended risk result | The number can answer the wrong question | Use A.9 to select a justified law, bound or separate-input result; declare an actual `Γ_fold` only for the selected fold |
| **CN‑frame sprawl** | Overlapping definitions obscure which comparison basis to use | Avoidable reconstruction and maintenance | Reuse a sufficient basis and retain differences that change the use. A registry supports maintained editions; use E.9 when a consequential decision needs a DRR. |
| **Self-certification hidden by assignments** | A holder authors the basis and later certifies it under a new role | A required independent check still examines that holder's own basis | Apply §4.2 to actual participation in the exact edition; separate authority and examination, and keep uncertified use explicit when certification is not required |

### A.19.CN:10 - Didactic quick cards (one‑liners teams reuse)

1. **Numbers travel with their basis.** Cite the characteristic and scale editions, bearer, reference or comparison basis, any qualifying scope/window, and result.
2. **Expose a normalization used by the trend.** An undisclosed change leaves the comparison basis unresolved.
3. **The intended result selects the law.** Use a weakest-part bound only when its declared dependency model justifies it; a safety label alone selects no fold.
4. **Ground an RSG-based Work-admission decision.** Establish the required state assertion before relying on it for admission; establish the other Work-admission conditions separately under A.15.1.
5. **Ground the semantic correspondence needed by reuse.** Test the F.9 predicate between exact local senses; use an obtaining Bridge only through the separate bounded-use claim and required reliance. Retain a false or unresolved result when no positive relation is established.
6. **When independence is required, check who made the basis.** A later role assignment does not remove self-certification; a sufficient uncertified comparison remains possible when no independent certification is required.
7. **Ground each chart value.** Name the reference state and coordinate patch. For measured values, cite the applicable measurement method and protocol; for evaluated or otherwise ascribed values, cite their rule and basis.
8. **Make deprecation recoverable.** A maintained edition identifies its retirement conditions and any supported successor relation.
9. **Keep the characteristics needed by the use.** Omit irrelevant coordinates; retain every distinction that changes the comparison.
10. **Identify the normalization used.** Cite its method and instance under A.19.UNM; ordinary mathematical mapping language alone identifies neither.

### A.19.CN:11 - SCR / RSCR Harness (acceptance & regression)

> **These are concept‑level checks; notation‑agnostic.**

#### A.19.CN:11.1 - **SCR — Acceptance (first introduction)**

* **SCR‑A19.4‑S01 (Completeness).** CN-Spec has every applicable mandatory value. Each cs_basis position declares its Scale and value meanings, Unit when that Scale has one, and any preference rule used for desirability ranking. Descriptive comparisons need no preference rule. The chart names its reference state and coordinate patch; measured values cite their C.16 measurement method/protocol, while evaluated or otherwise ascribed values cite the rule and basis that establish them, as required by CC-A19.D1-2 and CC-A19.D1-3.
* **SCR‑A19.4‑S02 (Normalization clarity).** When normalization is used, `normalization` identifies the admitted mechanism and provides the normalization references required by the A.19.UNM governing pattern (methods / invariants / fix, and instances when used). If instances are referenced in assurance logs, their evidence/backing and validity constraints are handled by the governing evidence pattern (C.16), not by A.19.CN.
* **SCR‑A19.4‑S03 (Comparability test).** Provide one worked coordinatewise or normalization-based comparison and the source/evaluation basis needed for its result. Use an Evidence Graph reference when that is how the required basis is represented.
* **SCR‑A19.4‑S04 (Γ‑fold audit).** When aggregation is used, the rule states the intended result, law and applicability basis, with only the required property claims; the reviewer reconstructs the result on a toy set under that model.
* **SCR‑A19.4‑S05 (Required certification).** Identify the exact receiving claim/control and relied-on CN-Spec edition or admission basis. If independent certification is required, check the actual certifier against authoring/material-selection history, then the independently applicable authority and examination conditions. Replay both successive same-holder assignments and overlapping different-holder assignments. When neither an independent-certification claim nor a control applies, keep the sufficiently grounded comparison; add a certification status only when it matters to the receiving use.
* **SCR‑A19.4‑S06 (Bearer and basis recoverable).** For each CN-Spec characteristic used in the worked example, retain its bearer, Characteristic and Scale editions, reference/comparison basis, any qualifying scope/window, and the measurement, evaluation or other value-ascription grounds required for the reading. Shared frame-level values need not be repeated for every characteristic. Use A.10 when provenance or bounded reliance must remain replayable.

#### A.19.CN:11.2 - **RSCR — Regression (on change)**

* **RSCR‑A19.4‑R01 (UNM edit).** When `normalization` changes, flag every comparison and Bridge-use claim that cites that normalization for affected-only reassessment, then rerun the corresponding worked comparisons.
* **RSCR‑A19.4‑R02 (Slot or basis change).** A changed definition receives a new edition. Preserve old results with their original basis; their present admissibility still depends on their evidence and intended use. A display-only correction that preserves the definition is handled as such.
* **RSCR‑A19.4‑R03 (Chart drift).** Updating measurement protocol bumps edition; **historic Work** keeps old edition link.
* **RSCR‑A19.4‑R04 (Fold change).** A changed fold requires reassessment of roll-ups that rely on the changed rule. Recompute dependent results; reuse unaffected results and retain historical outputs with their original rule.
* **RSCR‑A19.4‑R05 (Changed relation or use basis).** After either endpoint or its relation-semantic basis changes, test the applicable F.9 predicate for the new candidate. Reassess the separate use direction, correspondence rule, loss tolerance and reliance when their grounds change; reopen only dependent claims.
* **RSCR‑A19.4‑R06 (Deprecation rule).** On deprecating a CN-frame, the registry gives any supported successor relation, or states that no successor is established when that matters to reuse. Reconsider affected Bridges and uses; preserve historical relations instead of silently changing their endpoints.
* **RSCR‑A19.4‑R07 (Certification basis).** A change to the relied-on basis, relevant participation history or applicable control reopens only the certification and receiving conclusions it can change. A registry display change alone does not.

### A.19.CN:12 - Interaction summary (wiring to the rest of the kernel)

* **A.2 / A.2.5 (Roles / RSG).** RSG **checklists** quote **CN‑Spec.acceptance**; enactment gates rely on **admitted** CN‑frame data.
* **B.1 and A.9.** B.1 supplies any claimed whole/part construction; A.9 supplies an unresolved aggregation-law choice or property check. CN-Spec records the justified `Γ_fold`, including its model and time policy.
* **B.3 (Assurance).** For a named assurance claim, retain the relation and use evidence consumed by its argument. CL may serve as evidence shorthand; any quantitative effect needs a declared Scale and model. A safety roll-up requires the law or bound justified for its named outcome and dependency model.
* **Current proof/inference support and the C.16/A.19 characterization stack.** Scales, applicable Units and measurement guidance come from C.16, A.17, A.18 and A.19. Claims about folds use C.2.1 when claim/episteme identity matters, A.10 when evidence or provenance must remain replayable, B.3 for a named assurance claim, and C.23 when method-family evidence or maturity is at issue.

### A.19.CN:13 - Minimal CN‑Spec template (copy/paste, informational)

**Template note.** This example arranges the information needed to specify the comparison basis. A.19.UNM defines normalization terms; A.19.UINDM defines indicatorization; C.16 governs measurement and evidence backing; G.0 supplies the applicable admission conditions.

```
CN‑frame: <Name>      Edition: <edition>      Bearer: <bearer ref>
ComparisonBasis: <corpus, baseline, reference state, or declared comparison set>
ScopeAndWindow: <scope ref and qualification interval, when used>
IntendedUse: <claim, comparison, admission, or aggregation use>
characteristics:
  - <CharacteristicName> : <Scale; Unit when applicable>  [Polarity, when used: <preference rule>]
Chart:
  reference_state: <text>
  coordinate_patch: <domain/subset>
  measurement_protocol_ref?: <applicable measurement MethodDescriptionId>
  value_ascription_basis?: <applicable evaluation rule and evidence>
Normalization (when used):
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
  minimal_evidence: <basis required for this comparison>  # admission conditions under G.0; measurement/evidence backing under C.16
Aggregation (when used):
  fold: <Γ_fold expr>   time_policy: <window, statistic>
  WLNK/COMM/LOC/MONO: <only selected property claims, with their model and applicability basis>
Acceptance:
  checklist: [<observable criterion>… ]
  window?: <qualification interval when required>
  evidence_anchors: [<required observation, evaluation or other support refs>… ]
Alignment (optional):
  semantic_uses: [<obtaining Bridge, separate use claim, required reliance, kept/lost distinctions, applicable guards, optional CL>… ]
  plane_relations: [<applicable plane relation>… ]
MaintenanceAndDeprecation (for a maintained edition):
  responsibility: <responsible holder or maintenance arrangement>
  DRR_links?: [<DRR ids for decisions that need them>… ]
  deprecation_plan: <short note>
```



### A.19.CN:14 - SoTA-Echoing — enough basis to compare coordinate values

**Practice question.** What must accompany two chart values before a practitioner treats them as comparable? The selected comparison basis identifies the bearer/property, value-producing procedure or evaluation rule, relevant time and result basis alongside Scale/Unit meanings. A serious smaller alternative is to carry only the quantity kind, value and unit, converting units before comparison.

The [QUDT quantity model](https://www.qudt.org/pages/QUDToverviewPage.html) is the useful comparator: it separates Quantity, QuantityKind, QuantityValue and Unit and supports precise quantity descriptions. **Adopt** that discipline where a Unit applies. Using only that portion is cheaper and sufficient when the same property, procedure and observation basis are already fixed outside the record. **Reject** treating it alone as evidence that two independently obtained readings answer the same question; this is a limit of that reduced use, not a claim that QUDT forbids richer descriptions.

The [SOSA/SSN 2023-edition working draft of 24 September 2026](https://www.w3.org/TR/2026/WD-vocab-ssn-2023-20260924/) supplies the compared observation/procedure line: it distinguishes the feature, observed property, procedure, result and temporal qualifications. **Adapt** that separation in CN-Spec's bearer, cs_basis and chart, CC-A19.D1-1/-3/-11, and SCR-S01. The source is work in progress and does not establish FPF admission, Scale lawfulness, certification independence or a Bridge; those retain their direct rules. An evaluated coordinate keeps its actual rule and basis rather than acquiring a fictive measurement or Unit.

At comparable effort, both alternatives start from the same pair of readings and existing method records. The selected line adds the references that can change this comparison, reusing common frame-level values rather than repeating a full observation history for every cell. The SRE case in §8.2 shows the gain: equal millisecond units cannot make client end-to-end latency and server processing latency the same Characteristic. Keep them separate or obtain values for the same declared characteristic and observation basis. The added references cost more than a bare numeric pair; that cost is accepted when the basis is not already common and recoverable.

Reopen when a proposed comparison changes the property, value-producing rule, reference state or relevant window, or when a smaller representation demonstrably retains all the distinctions needed by that use. These sources support the compared representational choices; they do not validate every CN-frame or make its registry self-certifying.



### A.19.CN:Close - Closing perspective


A CN-Spec keeps the comparison basis with the readings. Reuse it while that basis remains sufficient; revise it and the dependent conclusions when the Characteristic, chart, normalization or intended use changes. A registry supports maintained editions. Cross-local reuse retains the coordinate mapping, semantic relation or plane relation it actually needs, with any separate bounded-use claim and required reliance.

### A.19.CN:End
