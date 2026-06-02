## A.20 - U.Flow.ConstraintValidity — Eulerian

**Tech‑name.** `U.Flow.ConstraintValidity` (`U.Flow` genus)
**Plain‑name.** Flow constraint validity (Eulerian interpretation)
**Type / Status.** Architectural pattern — **normative** for flows governed by E.TGA (E.18) under the Eulerian operational interpretation

### A.20:0 - Intention

**One‑liner** Defines cross‑cutting **ConstraintValidity** rules for all `U.Flow` instances. `U.TransductionFlow` inherits these rules and may refine **CV class specializations** for transduction‑specific semantics (species‑binding only; genus rules remain unchanged). The CV core is **kind‑agnostic** and assumes an **open‑world** catalogue of node **species**; the enumeration of node **kinds** in E.TGA is a **minimal kind baseline**.
**Operational interpretation.** **Eulerian** stance: **flow = valuation** over `U.Transfer`; **CV is attached to transformations (steps)** and evaluated **before any GateFit**; edges carry **assurance‑only operations**; no token‑passing semantics are assumed.

**Use this when.** Use A.20 when the live question is whether one transformation step internally satisfies its declared constraints before any gate-profile fit is evaluated.

**First useful move.** Name the step, the CV class being checked, the `CV.Status`, and the witness or missing witness. Stop there unless a gate, comparator, bridge, freshness, or work-boundary question is actually live.

**Smallest sufficient CV guidance.** Use the lightest CV guidance that preserves the next admissible reader move. Add publication lexemes, witnesses, `DecisionLog` detail, `CrossingBundle`, `PQG`/`RSCR`, or MIP-run material only when the live CV claim would otherwise become false, unsafe, non-replayable, or lack a named governing-definition locus.

**Minimum sufficient next move.** For ordinary CV, `step + CV class + CV.Status + witness or refusal` is enough. Per-check publication lexemes are needed only when the CV result is carried into a publication face, gate relation, or assurance material.

**Do not escalate when.** Do not create `GateDecision`, `GateDecisionExplanation`, GateFit narrative, comparator law, bridge law, freshness claim, release-confidence claim, or work-boundary authority from `CV.Status`. Open those neighboring pattern relations only when their own live claim is present.

**Conformance-marker overread note.** Use this note when a conformance label, `CV.Status=pass`, release-screen status, dashboard cue, or CV-looking publication is being read as gate passage, release confidence, safety acceptance, assurance, work occurrence, work authorization, or performed work. The first A.20 move is to return to the local step, CV class, `CV.Status`, witness or refusal, and window governed here; then state the unsupported attempted use and open the receiving relation only if its live claim is present: `A.21` for gate decision, `B.3` for assurance, `A.10` for evidence/currentness, `A.15` for work, or the exact neighboring pattern that carries the live claim. Write `CV.Status=pass` when CV is meant; do not write plain `pass` near gate, release, safety, or work use. Plain wording remains ordinary unless it changes admissible use, support, evidence, gate, assurance, work, decision, or neighboring-pattern exit.

**Common wrong first reading.** `CV.Status=pass` means release, safety acceptance, or gate passage. First honest entry: `CV.Status` is local step constraint validity with witness or refusal; release, safety, gate, assurance, or work use exits to the receiving pattern only when that live claim is present.

Repaired anti-case: a manufacturing conformance label near release may support only the local CV or conformance relation it actually carries. If release permission, safety acceptance, or work authorization is attempted, state that unsupported use and open the receiving relation rather than treating the label as release support.

**Same problem, different live question.** For a TGA-looking problem, use `E.18` for graph/flow/crossing, `A.20` for internal step validity, `A.21` for gate-decision publication, and `E.20` for mechanism-meaning placement; do not open the other three until their own claim is live.

**Semantic repair return.** When A.20 blocks a misleading word, face, alias, or source label, the repair must return to the enabled CV action: name `CV.Status`, the applicable CV class, and the witness or refusal that remains admissible. Do not stop at a classification of vocabulary or publication faces.

**Governed-object and relation separation.** Keep the graph object and path or crossing relation (`E.18`), MVPK publication faces (`E.17`), internal CV status and witness (`A.20`), gate decision and `DecisionLog` (`A.21`), evidence or provenance relation (`A.10`/`G.6`), work plan or work occurrence (`A.15`), and mechanism-governing definition assignment (`E.20`) distinct. An MVPK face, `DecisionLog`, evidence carrier, MIP manifest, or work witness does not carry another pattern's project-side value unless that exact governing pattern consumes it for that relation.

**Smallest affected locus.** Localize the change to the smallest live locus: `PathSlice` or crossing in `E.18`, CV step in `A.20`, `GateDecision` equivalence class in `A.21`, or mechanism-governing definition in `E.20`. Do not widen to a whole flow or unrelated governed object when that locus is enough.

**Ordinary success.** For ordinary A.20 use, success is that the live CV class, `CV.Status`, and witness or refusal are placed for the step without implying gate passage, comparator admissibility, freshness, or launch readiness. A full conformance review is needed only when the downstream claim consumes expanded assurance or conformance material.

**Locality asymmetry.** `E.18` is graph-local, `A.20` is step-local, `A.21` is gate-local, and `E.20` is trigger-local. Do not normalize the four patterns into one assurance regime.

**Do not merge these pairs.** Keep `CV.Status` distinct from `GateDecision`, TGA `Check` distinct from `GateCheckKind`, MIP manifest distinct from `DecisionLog`, `ViewpointMap` distinct from graph semantics, `PathSlice` distinct from a work run, and `GateProfile=Lite` distinct from `PublishMode=Lite`.

**Field liveness.** Always core for A.20: step, applicable CV class, `CV.Status`, and witness or refusal. Conditional-live: `GateCheckRef(aspect=ConstraintValidity)`, MVPK face pins, bridge/UTS refs, comparator/set-return refs, refresh refs, and SquareLaw or retargeting witnesses; open them only when the corresponding publication, gate, bridge, comparator, refresh, or `StructuralReinterpretation` claim is live.

**Retrieval trap guard.** When excerpted alone, A.20 must not be read as requiring every CV class or a Lipschitz certificate for every step. CV classes are applicability-triggered, and `CV.Status` does not create gate passage, launch readiness, comparator admissibility, or a reusable `GateDecision`.

**Anti-Goodhart guard.** CV completeness is not a substitute for the governed step result: the step must still satisfy the applicable internal constraint, and CV conformance does not create gate fit, freshness, comparator admissibility, or launch readiness.

**Generative side.** A.20 preserves open-ended action by letting internally valid steps, set publications, and archives remain usable without premature gate, ranking, or launch claims; CV is local support for future admissible moves, not only an assurance stop.

**What goes wrong if missed.** Readers may treat internal constraint satisfaction as gate passage, launch readiness, freshness, comparator admissibility, or decision reuse. That collapses CV into GateFit and hides the `A.21` gate decision relation.

**What this buys.** A.20 lets a reader keep mechanism constraint status local to the step and move to `A.21` only when gate fit or gate decision aggregation is really the live question.

**Not this pattern when.** If the question is profile fit, gate decision, gate-decision reuse, gate explanation, or pass/fail gate publication, use `A.21`. If the question is graph crossing or flow valuation, use `E.18`. If the question is comparator admissibility, set-return, archive, or refresh policy, use the current neighboring loci named in Relations.

### A.20:1 - Problem frame

In E.TGA, *nodes = morphisms* and the graph uses a *single edge kind* (`U.Transfer`). **GateFit** checks aggregate only in `OperationalGate(profile)` with the activation predicate **CV => GF**: until aggregated **`CV.Status=pass`**, all **GateFit** checks return **abstain**. Equivalently, while **`CV.Status != pass`**, any GateFit-oriented explanation **does not apply**. To keep flows comparable and auditable, this pattern delimits **internal step constraints** (CV) from **external gate fit** (GF), preventing any second process order beside the graph.

### A.20:2 - Problem

Without a clear CV core:

* internal step laws (domains/ranges, invariants, units coherence, Lipschitz/stability) bleed into gate **profile**;
* plane or comparator declarations sneak into mechanisms;
* freshness and DesignRunTag concerns appear inside mechanisms;
* reproducibility suffers because transfers start carrying hidden semantics beyond `⟨L,P,E⃗,D⟩`.

Under this pattern, CV is evaluated **inside** transformations. **If** a check declares planes/units/comparators or depends on an active `GateProfile`, **then** it is treated as **GateFit at gates** and the CV explanation **does not apply**.

### A.20:3 - Forces

* **Separation of concerns.** Internal mechanism laws vs. external profile fit.
* **Auditability.** MVPK faces include pins/references only; no new numeric claims; editions and Γ are pinned where applicable.
* **Graph discipline.** One edge kind; all crossings mediated by gates; SquareLaw on every crossing.
* **Reproducible valuation.** Flow = valuation over `U.Transfer`, with slice‑local refresh bounded by sentinels.
* **LEX hygiene.** ASCII Tech labels, twin Tech/Plain registers, registered tokens.

### A.20:4 - Solution

#### A.20:4.1 - Intent & Scope

**Intent.** Establish the **ConstraintValidity core** for the **`U.Flow` genus**: the normative set of **internal step constraints** and how their status and witnesses are carried and aggregated, **independent of GateFit profiles** (publication follows MVPK without adding new numeric claims). Where CV speaks about admissibility, phrase criteria **counterfactually**: *“If the admissibility conditions hold, then the CV explanation applies; otherwise this explanation does not apply.”* Avoid duty verbs unless stating the **normative** CC minima.

**Scope (genus).** CV covers **intra‑step** properties checkable from the transformation’s own signature/mechanism. The canonical CV classes are **genus-scoped and non-exhaustive**:
`MechanismUnitsCoherence`, `LawSetInvariants`, `AdmissibilityConditionsSatisfaction`, `LipschitzBounds`, `TypeDomainRange`, and—only for **`StructuralReinterpretation`**—`ReinterpretationEquivalence` (correspondence/reversibility witness).

**Species binding (`U.TransductionFlow`).** The above classes bind to `U.Transduction(kind in {Signature, Mechanism, Work, Check, StructuralReinterpretation})` with **`OperationalGate = kind=Check`**; no additional CV classes are introduced here. Species-specific examples and broader flow specializations stay outside this CV core; `StructuralReinterpretation` semantics are received through `E.18`, `A.6.4`, and this pattern where CV is live.

**Out‑of‑scope (CV):** declaring/translating `ReferencePlane/Units/ComparatorSet`; CSLC comparability beyond internal step preservation; Freshness; Role/Channel; Regulated-X; `DesignRunTagConsistency`. These leave CV and use `E.18`/`A.21` or the named comparator, selector, archive, refresh, evidence, work, safety, or temporal locus when that relation is live.

#### A.20:4.2 - Intensional object(s)

**Genus.** `U.Flow` leaves step‑kinds abstract; CV/GF separation applies to any admissible instantiation.
**Species (`U.TransductionFlow`).** `U.Transduction(kind) ∈ {Signature, Mechanism, Work, Check, StructuralReinterpretation}`; this set of **kinds** is a **minimum kind baseline** defined in E.TGA. The **species** space (e.g., UNM declaration and use, `SelectionAndTuning`, `WorkPlanning`, `EvaluatingAndRefreshing`, …) is **open‑world** and non‑exhaustive. `OperationalGate = U.Transduction(kind=Check)`. `StructuralReinterpretation` is **projection-preserving** (no mutation of `⟨L,P,E⃗,D⟩`) and may retarget **describedEntity** under CC-TGA-06-EX; see `E.18` and `A.6.4`.

**`AdmissibilityConditionsSatisfaction`** — **If** the declared admissibility conditions hold on the step’s inputs and context, **then** the CV explanation **applies**; **otherwise** this explanation **does not apply**.
**`LipschitzBounds`** — **If** inputs vary within the stated domain \(X\) and perturbations/noise \(≤ ε\), **then** the step’s estimate remains within **δ** of the reference; **otherwise** this explanation **does not apply**.
**`MechanismUnitsCoherence / TypeDomainRange`** — **If** units/types/domains match the mechanism’s signature and closed‑world assumptions for the step, **then** the CV explanation **applies**; **otherwise** this explanation **does not apply**.

**Terminology & bindings (normative)**
* **Status/witness lexicon (E.10 discipline).** In CV scope, publications use **Status/Witness** terminology; **GateDecision…** lexemes belong to GateFit (A.21) and do **not** apply to CV.
* **describedEntity = KindBridge.** Any CV mention of “describedEntity” is read via **`KindBridge (CL^k)`** on **UTS** under `F.9`, `F.17`, `E.17`, `E.18`, and `C.3.3` where live. CV **does not** declare or translate planes/units/comparators.
* **retargeting/witness binding.** For `U.Transduction(kind=StructuralReinterpretation)`, the CV class **`ReinterpretationEquivalence`** SHALL carry **`CV.WitnessRef := ReinterpWitness`** over the addressed `PathSliceId`; the UTS **`SquareLaw‑retargeting` witness** is referenced from MVPK/UTS and **linked** from the CV witness without duplication.
* **`ReinterpWitness` record shape.** The record shape is defined once in A.20:4.7.

#### A.20:4.3 - MVPK Faces (PlainView - TechCard - InteropCard - AssuranceLane)

Minimum pins on faces that carry CV outcomes (**Lean publication** allowed by profile but without weakening checks):

* **CtxState pins.** `⟨L,P,E⃗,D⟩` on ports/tokens; raw `U.Transfer` preserves them.
* **Path pins.** `PathId` and `PathSliceId` appear where slice-local refresh or reinterpretation witnesses are relevant; valuation semantics are carried by `E.18` plus `A.20`, with `G.11` when refresh wiring is live.
* **CV pins.** `CV.Status ∈ {abstain, pass, degrade, block}`, `CV.WitnessRef?` (refs only).
* **Edition pins.** If a face cites `CG-Spec`, `ComparatorSet`, or `UNM.TransportRegistryPhi`, the face **includes** the compatibility reference (`BridgeCard + UTS row`, with `CL/CL^plane`) under `F.9`, `F.17`, `E.17`, and `E.18` for downstream consumption. A.20 references this requirement; it does not introduce or modify Bridge/UTS formats.
* **Face scope.** Each face includes `PublicationScopeId` with an **MVPK profile** (Min/Lite/SetReady/Max) — no new publication-face kinds.
* **Register discipline.** Tech names ASCII; twin labels; required LEX tokens follow E.10 (e.g., `SentinelId`, `PathSliceId`, `SliceRefresh`).

> **No new numeric claims.** MVPK faces carry refs, `CV.Status`, and witness or refusal references only; they do **not** introduce fresh computed scalars beyond what the mechanism already entails (MVPK functoriality).

**CV reference names.** In ordinary A.20 prose, an unpublished CV record may be called `CVRef` or `CVCheckRef` as a plain local convenience. When the record is carried on an `A.21` or `E.18` publication face, use the publication lexeme:
`GateCheckRef := { aspect=ConstraintValidity, kind, edition, scope }` with `scope ∈ {lane|locus|subflow|profile}`. This adds no execution steps and introduces no numeric claims on faces; it records what CV classes were considered and under which editions. `GateCheckRef(aspect=ConstraintValidity)` is a publication lexeme only; it does not make CV a gate. A.20 retains CV class meaning; A.21 consumes only referenced CV results when a gate relation is live.

#### A.20:4.4 - GateChecks (table) — CV only

**Activation predicate (in E.TGA).** *Until aggregated `CV.Status=pass`, all GateFit checks return `abstain` (CV=>GF).*
**Role/Channel Fit guard (GateFit scope).** GateFit checks that involve roles SHALL use **Kernel `U.Role` tokens** (domain = `U.System`) and SHALL NOT consume `TypicalEnactorRoleName` strings from alias tables.

| CV class | Applies when | Publication minimum |
| --- | --- | --- |
| `TypeDomainRange` | The step has a typed signature, declared domain/range, or SlotKind boundary. | `CV.Status + witness/refusal` for the typed relation. |
| `AdmissibilityConditionsSatisfaction` | The mechanism declares admissibility conditions. | `CV.Status + condition ref + witness/refusal`. |
| `LawSetInvariants` | The mechanism has a law or invariant set. | `CV.Status + invariant ref + witness/refusal`. |
| `MechanismUnitsCoherence` | Quantities, scales, units, or reference planes are actually used. | `CV.Status + quantity/unit/plane refs`; CV may check coherence against already-governed unit/plane refs, but may not author, translate, bridge, or change units or planes. |

| `LipschitzBounds / stability` | A perturbation, sensitivity, robustness, continuity, safety-envelope, or stability claim is load-bearing. | Bound or certificate ref under declared assumptions; no universal Lipschitz certificate demand. |
| `ReinterpretationEquivalence` | The step is `StructuralReinterpretation`. | `CV.Status + ReinterpWitness` scoped to the addressed `PathSliceId`. |
| `ReferencePlaneCrossing`, CSLC, Freshness, Role/Channel, Regulated-X, `DesignRunTagConsistency` | A gate, crossing, comparator, freshness, role/work, safety, or design/run relation is live. | Not CV-only; use GateFit/A.21 or the named neighboring locus. |
CV **SHALL NOT** declare or translate `Units`, `ReferencePlane`, or `ComparatorSet`. Gate-mediated crossings and gate-consumed CSLC checks use `E.18`/`A.21` with UNM declaration and bridge discipline. Comparator admissibility, ranking, selection, set-return, archive semantics, and refresh remain with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.11`, or `A.21` only where those live claims are actually present.

#### A.20:4.5 - SWP matrix (declaration-locus discipline)

* **Writes (faces).** `CV.Status` (and optional `CV.WitnessRef`) only.
* **Reads (ref‑only).** Any `CG‑Spec/ComparatorSet/TransportRegistryΦ` editions (when referenced); their declarations remain governed by the UNM declaration locus per CC‑TGA‑24.

#### A.20:4.6 - CtxState & GateCrossing

* **Crossings only at `OperationalGate(profile)`** (plane/unit/context) with a **strict exception** for **`StructuralReinterpretation`**: a **projection‑only retargeting** MAY occur without a gate **iff** `⟨L,P,E⃗,D⟩` is preserved, **KindBridge (`CL^k`)** and a **SquareLaw‑retargeting witness** are present on MVPK/UTS, and the action is **PathSlice‑local** (`PathSliceId` pinned).
* **Projection and describedEntity source.** For `StructuralReinterpretation`, A.20 may state the CV witness needed for the step, but it does not define a second semantics of projection, published view, describedEntity, or retargeting. Read those terms through `A.6.4`, `C.2.1`, `C.2.P`, and the relevant UTS `KindBridge (CL^k)` rows under `F.9`, `F.17`, `E.17`, `E.18`, and `C.3.3` where live.
* **Projection/describedEntity normalization (CV use only).** In that imported reading, projection is a change of published view coordinates only, and describedEntity is a Kind-channel change under `CL^k`. A “no unit/plane change” test SHALL verify that `ReferencePlane(src)=ReferencePlane(tgt)` and `CL^plane` is absent (or `= ⊤`), otherwise the step is a gated crossing.
* **Assurance operations on edges.** `ConstrainTo/CalibrateTo/CiteEvidence/AttributeTo` reside on `U.Transfer` and do **not** alter `⟨L,P,E⃗,D⟩`; plane/unit changes occur only at gates; Φ/`CL^plane` penalties appear in **R-lane**. describedEntity/kind transitions are recorded as **`KindBridge (CL^k)`** on **UTS** under `F.9`, `F.17`, `E.17`, `E.18`, and `C.3.3`; under CC-TGA-06-EX this may appear without a gate only when it is projection-preserving and PathSlice-local.

Terminology for this crossing slice is defined in A.20:4.2, and `ReinterpWitness` shape is defined in A.20:4.7; A.20:4.6 only applies those bindings to CtxState and GateCrossing.

#### A.20:4.7 - SquareLaw

For any gate‑mediated crossing adjacent to CV‑checked steps:
`gate_out ∘ transfer = transfer' ∘ gate_in`.
For **projection retargetings** under `StructuralReinterpretation`, a **SquareLaw‑retargeting witness** shows that the **view retargeting commutes** with transfers on the PathSlice. Inconsistencies lead to `degrade`/`block` per active profile (GateFit decision).

**retargeting witness shape (normative, UTS-scoped).** A **SquareLaw‑retargeting witness** is a witness record that demonstrates commutativity of a published‑projection retargeting over the addressed **`PathSliceId`**:
  1) identifies **`PathSliceId`** and **`PublicationScopeId`**;
  2) presents a **bidirectional view mapping** between projections either as an **iso** or as a **profunctor optic** (`get : A→B`, `put : (B×A)→A`) satisfying **Put‑Get / Get‑Put** laws;
  3) enumerates the **commuting squares** for the cut‑set edges considered (ids of transfers before/after the retargeting);
  4) declares properties (**invertible?**, **idempotent?**) and the **definedness area**;
  5) cites the **UTS.RowId** and links the **DecisionLog** entries that rely on this witness.
Realizations via **profunctor optics (post‑2017)** are permitted; the optic/lens laws serve as the proof template of commutativity.

**CV witness for reinterpretation (normative, CV-scoped).** `CV.ReinterpretationEquivalence` SHALL carry a **ReinterpretationEquivalenceWitness** distinct from the UTS retargeting witness and scoped to the mechanism state over the same **`PathSliceId`**:
  — `PathSliceId`, `PublicationScopeId`, and **definedness region** (domain constraints);
  — a **pair of internal transformations** (or an optic) with **Put‑Get / Get‑Put** obligations **over mechanism state** (not faces);
  — a **list of commuting squares** for the **adjacent raw transfers** (before/after reinterpretation) showing SquareLaw at CV boundary;
  — an explicit **NoHiddenScalarization assertion** (see §4.9) for any comparable return shape;
  — **edition neutrality**: no new editions are declared; only refs/pins appear.
This CV witness links to the UTS `SquareLaw‑retargeting` witness when present, but does not duplicate UTS fields.

**CV witness binding (normative).** For the CV class **`ReinterpretationEquivalence`**, the witness **SHALL** be a `ReinterpWitness` record:
`ReinterpWitness := { PathSliceId, PublicationScopeId, mapping: {kind: iso|optic, laws: PutGet/GetPut}, commutingSquares: [TransferId], definedOn: PathSliceId, properties: {invertible?: bool, idempotent?: bool}, UTS.RowId, NoHiddenScalarization: true }`.
The record is **PathSlice‑local** and does not declare or translate planes/units or comparators.

#### A.20:4.8 - Sentinel & PathSlice (path‑local refresh)

* Flows are **valuations** over `U.Transfer`, re-emitting **slice-locally** under explicit refresh rules or edition bumps carried through `E.18`, `A.20`, and `G.11` where refresh wiring is live. CV contributes to the **prepare/refresh** conditions but does not expand scope beyond the addressed `PathSliceId`.
* **Delimitation & planning (normative).** A `PathSlice` **closes** on: (i) any pinned edition change, (ii) Γ‑window boundary relevant to the face, (iii) `GateProfile` change along the path, or (iv) an explicit sentinel rule. **Concurrency:** at most **one active recompute** per `{PathSliceId}`; parallel recomputes are permitted across **distinct** `PathSliceId`s.
* **CV‑triggered refresh (minimum list).** Re‑emit the addressed `PathSliceId` when any holds: (a) `CV.Status` changes across the lattice; (b) `ReinterpWitness` is added/updated/withdrawn; (c) `AdmissibilityDecl.edition` or `LipschitzBoundRef.edition` changes; (d) updates arrive from `F.9`, `F.17`, `E.17`, or `E.18` bridge and UTS loci, or from `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11` comparator and refresh loci; (e) error/timeout transitions to `CV.Status=pass` for a previously `abstain|degrade` CV class.

* **CV‑to‑refresh triggers (normative).** A **SliceRefresh(PathSliceId)** SHALL be scheduled when any of the following occurs:
  (`CVRefreshTrigger.StatusFlip`) a **CV status flip** on the slice (`pass↔degrade`, `pass↔block`, or `error/timeout→{degrade|block}` under profile rules);
  (`CVRefreshTrigger.ReinterpretationWitness`) arrival of a new **ReinterpretationEquivalenceWitness** or a change in its **definedness region**;
  (`CVRefreshTrigger.AdjacentFactUpdate`) updates to adjacent **UTS** or **Bridge** facts for the slice (e.g., `CL^k`, `BridgeId`, `Φ`/`Ψ` policy-ids) under `F.9`, `F.17`, `E.17`, or `E.18`;
  (`CVRefreshTrigger.ReferencedEditionChange`) edition changes referenced by comparator or selection loci on the slice (`A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11` when live) (`ComparatorSetRef.edition`, `DescriptorMapRef.edition`, `DistanceDefRef.edition`, …);
  (`CVRefreshTrigger.FreshnessTicketChange`) **FreshnessTicket** or freshness-support state changes that alter the slice window under `A.21`, `B.3`, or `G.11` when live;

  (`CVRefreshTrigger.SentinelRule`) sentinel rules explicitly attached to the **PathSliceId**.
Scheduling is **slice‑local**; recompute does not fan‑out beyond the addressed `PathSliceId`.

  **Id‑scheme:** `PathSliceId := PathId × Γ_time selector × ReferencePlane × SentinelFingerprint × IterationCounter`.
  **Locking for replay:** within a recompute, the effective `E⃗` is **frozen**; outputs carry a **replay fingerprint** resolvable via `DecisionLog`.

#### A.20:4.9 - ReturnShape & CSLC (comparability discipline)

When a declared comparable, set-valued, archive, or partially ordered return shape is live, CV checks that the step did not internally destroy that return shape; **no hidden scalarization**. If no declared return shape is live, do not open a ReturnShape or NoHiddenScalarization check. Any comparator citation is **ref-only** and, if editions are cited, SHALL include `Bridge+UTS` through the current bridge and terminology loci (`F.9`, `F.17`, `E.17`, `E.18`). Comparator admissibility, ranking, selection, archive semantics, and refresh remain with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.11`, or GateFit (`A.21`) where live. CV only checks preservation of the already-declared return shape inside the current step.

Under **`StructuralReinterpretation`**, **projection changes MUST NOT introduce hidden scalarization**; set‑return semantics remain intact; comparator cites stay ref‑only with UTS discipline.

**Detectable indicators of hidden scalarization (normative checklist).** A face **SHALL** be flagged when any holds:
  (H1) introduction of a **new scalar** not entailed by the mechanism, or any **cardinality‑reducing** fold of a set return (e.g., argmax/best‑of) without a cited **ComparatorSetRef**;
  (H2) omission of a required **ComparatorSetRef** or its **edition pins** where comparison is implied;
  (H3) presence of an **order-imposing coordinate** without a **CoordinatePolicy** and admissibility annotations (scale, units, or inadmissible operations);
  (H4) cross‑plane/units numeric combination without a **Bridge+UTS** row;
  (H5) for `StructuralReinterpretation`, any change of return **plane/units** (violates “projection‑only”).
Failing (H1–H5) degrades or blocks per GateProfile (§4.4/CC‑TGA‑21a).

#### A.20:4.10 - Γ‑windows / Freshness

* No implicit *latest*. Any face expected to be consumed at compare or launch pins `Γ_time`; freshness checks occur at gates; CV neither issues Freshness tickets nor evaluates staleness. Use `A.21`, `B.3`, `C.27`, or `G.11` when a live freshness, temporal-claim, or refresh relation is present.
* **Granularity of Γ (normative).** Γ SHALL be one of: **snapshot** (`effective_at=t`) or **interval** (`[t₀,t₁)` with a named folding policy). Faces SHALL carry the selector used.
* **CV time‑stamping.** Each CV computation records `t_cv` and the **Γ selector** it assumed; replay binds `t_cv` to `PathSliceId`.
* **Temporal policy types (binding).** Γ‑pins refer to the **canonical selectors** of §22 (*`effective_at`*, *`latest_effective_before`*, *`windowed(W, policy)`*) and to **folding policies** that are **IDEM/MONO/WLNK‑safe**. Units/time scales **SHALL** be explicit. Overrides of the default **weakest‑link** fold **SHALL** cite CAL proofs of monotonicity and boundary behavior.

#### A.20:4.11 - Unknown/Timeout/Error policy

Each CV class yields one `CV.Status` value: `abstain | pass | degrade | block`. Errors/timeouts at CV stage imply **`CV.Status != pass`**; therefore GateFit abstains by the global activation predicate and any GateFit‑oriented explanation **does not apply**. The aggregated `CV.Status` uses the join on `abstain <= pass <= degrade <= block` (neutral = `abstain`; absorbing = `block`).
**Minimal default (profile‑bound, normative):** **Lean/Core ⇒ `error|timeout → degrade`**, **SafetyCritical/RegulatedX ⇒ `error|timeout → block`**; `unknown` folds per GateCheck policy (safety‑default: `degrade`). (Consistent with **CC‑TGA‑22**.)

#### A.20:4.12 - Idempotency / congruence discipline

Any publication consumed by an `A.21` gate decision uses the `A.21` decision-stability witness for input equivalence and idempotency; use `G.6` or `G.11` where evidence-path visibility or refresh implications are live. A.20 does not introduce keys, hashes, or cache policies.

**Minimal lexeme set for CV‑adjacent equivalence (normative).** Where an `A.21` gate decision consumes CV outcomes, the **equivalence witness** SHALL identify at least: `{PathSliceId, GateProfileId, Γ selector (+window bounds if interval), E⃗ editions vector for cited registries, ReturnShape kind (if comparable), CV class/kind set considered}`. Changing any of these breaks equivalence and triggers re-aggregation.

### A.20:5 - Archetypal Grounding (Tell–Show–Show)  ✱

**Tell (internal step, not gate passage).**
CV answers whether a transformation step satisfies its own declared constraints: units, laws, admissibility conditions, stability bounds, type/domain/range, and, for `StructuralReinterpretation`, reinterpretation equivalence. If `CV.Status != pass`, GateFit does not get to rescue the step; if `CV.Status=pass`, ranking, acceptance, launch, and profile-fit still belong outside CV.

**Show‑0 (`CV.Status=pass`, no gate opened).**
A normalization step has declared units, domain/range, and invariant refs; the CV check returns `CV.Status=pass` with a `CV.WitnessRef`. No comparison, launch, crossing, freshness, or profile-fit claim is live, so no `GateDecision`, GateFit narrative, or `DecisionLog` is opened. The admissible result is only: this step is internally valid under its declared constraints.

**Show‑1 (compiler build → run).**

A typed module `M` exposes `f : State_d → BuildOutput_d` under a declared `LawSet` (e.g., determinism under fixed toolchain) and `TypeDomainRange`. **CV** checks: (i) `MechanismUnitsCoherence` (toolchain/flags units coherent), (ii) `LawSetInvariants` (reproducible outputs under same `E⃗`), (iii) `Admissibility` (inputs well-typed), and (iv) optional Lipschitz/stability surrogate (bounded perturbation in sandbox). `CtxState` is preserved along raw transfers. Entering `U.Work(run)` uses `LaunchGate` with `FreshnessUpToDate` and `DesignRunTagConsistency` - **GateFit**, not CV.

**Show‑2 (selection archive in QD/AutoML).**
A mechanism emits a **set** (`Front`, `Archive`, or another declared set publication). **CV** checks only: valid descriptor ranges, declared continuity bounds over named metric spaces, and archive invariants (idempotent insert). No ranking or acceptance thresholds are introduced at CV; comparators and acceptance policies bind at gates via `A.21` plus the current comparator and set-publication loci (`A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11`) where live. Edition-aware pins on faces carry `DescriptorMapRef.edition` only with `Bridge+UTS`.

**Anchors.** Algebraic effects & handlers separate signatures from handlers (Koka/Effekt, 2015+); reproducible pipelines isolate mechanism constraints from deployment **profiles** (Bazel/Nix); optics/profunctors and open/hypergraph categories motivate composition on open graphs without adding facts on faces; QD/MAP-Elites/CMA-ME/DQD motivate **set-return and declared order relations** (2015-2022).

### A.20:6 - Bias‑Annotation

The pattern constrains *how* CV status and witnesses are carried; it does not encode profile‑bound thresholds or Role/Channel fit — those sit in GateFit. This separation keeps profile concerns out of mechanism semantics.

### A.20:7 - Conformance Checklist  ✱

**Conformance use.** This checklist is evidence for the internal-step CV guidance already stated in the Solution. It is not the first entry text for ordinary use and not a full audit regime by default; an item is applied only when its corresponding CV class, witness, publication face, or neighboring relation is live. Before applying any item, name the Solution move it tests; if no such reader move is live, treat the item as support-only or not applicable rather than expanding the applied assurance or conformance material.

**Conformance groups.** Ordinary CV use starts with step, applicable CV class, `CV.Status`, and witness or refusal. Crossing/launch items apply only when a CV-checked step is adjacent to a live gate, crossing, or launch boundary. Publication/assurance items apply only when the CV result is carried on MVPK faces or consumed by downstream replay/audit. Extension/change items apply only when species binding, valuation/refresh, or neighboring selector/comparator loci are being changed or consumed.

**Static lint (graph and faces)**

* CC‑TGA‑01: only `U.Transfer` edges; crossings appear only on gates.
* CC‑TGA‑05: `⟨L,P,E⃗,D⟩` unchanged across raw transfers.
* CC‑TGA‑09: MVPK faces present; edition & Γ pins where expected; no new numeric claims on faces (E.17).

**CV discipline**

 * CV classes present exactly as {UnitsCoherence, LawSetInvariants, Admissibility, LipschitzBounds, TypeDomainRange}; **plus** `ReinterpretationEquivalence` when the node kind is `StructuralReinterpretation`. None declare/translate planes/comparators.
 * **Open‑world species.** Any node **species** binds to one of the minimal kinds; adding a new **kind** is out of scope for A.20 and belongs in an E.TGA update.
* Aggregated **CV.Status** computed; errors/timeouts imply `CV.Status != pass`.
* Any support-looking use beyond the local step names the receiving relation. `CV.Status` is not gate passage, release confidence, assurance, safety acceptance, work occurrence, or work authorization.

**Gate coupling**

* CC‑TGA‑07: when **`CV.Status != pass`**, all GateFit checks report **abstain**.
* CC‑TGA‑23: SquareLaw witnesses present on crossings adjacent to CV‑checked steps.
* Any edition citation on faces includes `Bridge+UTS` through `F.9`, `F.17`, `E.17`, and `E.18`; comparator or set-return implications use `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11` when live.

**UNM declaration locus**

* CC‑TGA‑24: `CG‑Spec`, `ComparatorSet`, and `TransportRegistryΦ` declarations are governed by UNM; CV is ref‑only.

**Valuation & refresh**

* CC‑TGA‑18/19: Flow publishes valuation with `PublicationScopeId`/`PathSliceId`; Γ pinned at compare and launch faces; sentinel triggers slice‑local refresh.

### A.20:8 - Consequences

**Benefits.**
*Clarity & composability.* Mechanism descriptions remain limited to internal laws; gates are the sole policy junction.

*Replayability.* With valuation plus MVPK pins, re-runs under fixed `E⃗` are comparable and slice-scoped through `E.18`, `A.20`, and `G.11` when refresh wiring is live.
*Didactic hygiene.* Readers can see what is internal mechanism constraint status vs. gate policy.

**Trade‑offs.**

* Two places to look (CV vs. GF) impose placement discipline; mitigated by the activation predicate and MVPK links.

### A.20:9 - Rationale

E.TGA coordinates A.20 and A.21 as orthogonal cores: CV **inside** transformations; GF **at** gates with join‑aggregation and DecisionLog. This mirrors effects/handlers (signature vs. handler), and reproducible build vs. deployment‑profile separation.

### A.20:10 - SoTA-Echoing (post-2015)

| SoTA source idea | FPF invariant | Reader move | Rejected shortcut |
| --- | --- | --- | --- |
| Algebraic effects, refinement, and certified-computation practice separate local constraint satisfaction from handler or deployment policy. | CV is internal step validity with `CV.Status` plus witness or refusal; GateFit (`A.21`) may consume the CV result only when a gate relation is live. | Name the step, the applicable CV class, and the witness or refusal before making any gate claim. | Treating `CV.Status=pass` as gate passage, launch readiness, comparator admissibility, or a release-confidence claim. |
| Reproducible-pipeline practice keeps mechanism constraints distinct from release or deployment profiles. | A.20 records assumption-bound status and witnesses; it does not define build tooling, cache keys, storage formats, or release policy. | Keep release and profile questions outside CV unless the neighboring pattern is live. | Treating a validation checklist as release readiness. |
| Optics, profunctors, and open or hypergraph categories support disciplined reinterpretation without adding new face facts. | `ReinterpretationEquivalence` uses imported retargeting semantics and a CV-scoped witness over the addressed `PathSliceId`; projection and describedEntity semantics stay with their governing loci. | Require the relevant witness before allowing `StructuralReinterpretation` `CV.Status=pass`. | Letting A.20 define a second semantics of projection, view, describedEntity, or retargeting. |
| Quality-Diversity, MAP-Elites, CMA-ME, and DQD practice preserve set-return and archive visibility. | CV may check that the step did not internally destroy a declared set, archive, or partially ordered return shape; comparator, ranking, archive, and refresh decisions remain outside CV. | Preserve no-hidden-scalarization inside the step and return comparator or archive use to the neighboring loci named in Relations. | Letting CV select, rank, accept, or refresh set-return outputs. |

Action result from the local-constraint and reproducible-pipeline practice basis: `CV.Status`, conformance labels, validation checklists, and CV-looking publications do not become gate passage, launch readiness, release confidence, safety acceptance, assurance, work occurrence, work authorization, comparator admissibility, or refresh authority. The local A.20 result is step, CV class, `CV.Status`, witness or refusal, unsupported attempted use, and the named receiving relation when a gate, release, assurance, work, comparator, or refresh claim is live. Reopen the local result when the CV status, witness, governing definition, assumption, edition, window, path slice, or consuming neighboring relation changes.
### A.20:11 - Relations

 * **Governed by E.TGA.** Nodes are morphisms; only `U.Transfer` edges; **open‑world species over a minimal kind set**; CV⇒GF activation; MVPK faces; SquareLaw on crossings; CC‑TGA‑06‑EX for `StructuralReinterpretation`.
* **A.21 (GateProfilization).** Sole point for GateFit checks and profile‑bound folds.
* **E.18 (flow valuation and PathSlice currentness).** Declares the graph and valuation semantics used by this flow family.
* **F.9 / F.17 / E.17 / E.18 (Bridge+UTS loci).** Boundary-publication requirement whenever faces cite editions.
* **A.19.SelectorMechanism / C.18 / C.19 / G.5 / G.11.** Comparability, set-return, archive, and refresh discipline; CV does not compare; it only checks internal readiness for declared comparison.
* **A.21 / G.6 / G.11.** Gate decision stability, equivalence witness references, evidence-path visibility, and refresh implications when gate decisions consume CV-adjacent publications.
* **E.10 (LEX).** Token classes and ASCII Tech names; twin labels and aliasing for Γ/CL/Φ as per LEX‑BUNDLE.

### A.20:Appendix A — CV Class Gloss (normative)

* **MechanismUnitsCoherence.** Internal unit and scale coherence within the step when quantities, scales, units, or reference planes are actually used; no declarations or translations of units/planes occur in CV.
* **LawSetInvariants.** Mechanism-declared invariants hold (e.g., mass/energy balance in a model, determinism under fixed editions).
* **AdmissibilityConditionsSatisfaction.** Inputs lie within admissible windows/guards declared by the mechanism's **AdmissibilityConditions**; failure yields `degrade` or `abstain` per class policy.
  **Minimum declaration (normative):**
  `AdmissibilityDecl := { domains: {name: set/poset}+, guards: [predicate_id]*, windows: {Γ_time: snapshot|interval|policy}, observables: [signal_id]*, edition: EditionId }`.
  The declaration is published on MVPK as references only; it introduces no arithmetic on faces.
  **Minimal declaration template (normative):**
  `AdmissibilityConditions := { Domains[]{var, type, range, units, plane}, Guards[]{predicate, editionRefs}, ObservationWindows[]{Γ selector, freshness window}, ObservableSigns[]{name, detection rule}, Editions{...} }`
  — **No unit/plane declaration or translation** here; only references. Γ selectors SHALL be explicit.
* **LipschitzBounds / stability.** Bounded sensitivity under a declared metric, used only when a perturbation, sensitivity, robustness, continuity, safety-envelope, or stability claim is load-bearing.
  **Publication ref shape (normative):**
  `LipschitzBoundRef := { method ∈ {spectral_norm|CROWN|IBP|rand_smoothing|other}, metric_space: {X: norm_id, Y: norm_id}, bound: value_or_interval, units/plane: P, validity_window: Γ_time(basis), edition: EditionId, certificateRef?: LipschitzCertificateId }`.
  **Referenced evidence/certificate object (normative):**
  `LipschitzCertificate := { metricId (with units and plane), bound L, methodId, methodRef (e.g., spectral estimate or certified robustness bound), validity region (inputs and state), proof sketch or reference }`.
  The method MUST be cited; units/plane of the metric MUST be explicit; proofs and witness records are referenced; bounds are ref-only at CV; any acceptance action remains GateFit.
* **TypeDomainRange.** Well-typedness and type, domain, and range consistency for the transformation signature; refs point to the governing definitions.
* **ReinterpretationEquivalence (StructuralReinterpretation only).** Existence of a correspondence/reversibility witness between source and retarget projections; preservation of `⟨L,P,E⃗,D⟩`; no comparator/plane/unit declaration or translation at CV.
  **Witness (normative):** `ReinterpWitness` / `ReinterpretationEquivalenceWitness` (see §4.7) with: `(i)` `PathSliceId`, `PublicationScopeId`, `(ii)` bidirectional mapping (iso/optic) with Put-Get/Get-Put obligations, `(iii)` commuting squares for adjacent raw transfers, `(iv)` **NoHiddenScalarization** assertion when comparable, and `(v)` definedness region.
  The witness is PathSlice-local and supports idempotence and reversibility within the addressed slice. Any describedEntity change SHALL have `KindBridge (CL^k)` on UTS.

#### A.20:Appendix B — LEX discipline (summary)

Register token classes (Tech) include: `U.TransductionFlow`, `U.TransductionGraph`, `OperationalGate`, `GateProfile`, `GateCheckKind`, `GateCheckRef`, `DecisionLog`, `FreshnessTicket`, `FinalizeLaunchValues`, `SubflowRef`, `FlowEmbed`, `SentinelId`, `PathSliceId`, `SliceRefresh`, `VALATA`; discriminators use `Base__P2W`, `Base__EvaluatingAndRefreshing`; Tech names are ASCII; aliases `GammaTimeRule/Plane`, `CLPlane`, `Phi` follow E.10. A.20 references these tokens; it does not introduce additional LEX classes. **For each published CV check, `GateCheckRef.aspect` is fixed to `ConstraintValidity`.** *MVPK minima for CV faces also include `PathId/PathSliceId` where slice-local refresh applies through `E.18`, `A.20`, and `G.11` when live.*

### A.20:End
