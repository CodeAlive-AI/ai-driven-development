## A.21 — GateProfilization: `OperationalGate(profile)` (GateFit core)

**ID:** A.21
**Type:** Architectural pattern

**One-liner.** A single microkernel-style gate aggregates **GateChecks (CV + GF)** into an **order-independent** `GateDecision` via the `GateDecision` join-semilattice `abstain <= pass <= degrade <= block`, uses the **CV=>GF activation predicate** (and the LaunchGate pre-run barrier), applies profile-bound folds for `error|timeout|unknown`, and publishes replay-grade traces (MVPK + `DecisionLog` + `EquivalenceWitnessRef`).

**Use this when.** Use A.21 when the live question is whether a gate may publish a profile-bound `GateDecision` from declared GateChecks, folds, pins, and rationale.

**First useful move.** Name the `OperationalGate(profile)`, the active `GateProfile`, the effective `GateCheckRef` set, the aggregated CV status, and the `DecisionLogRef` that will carry the decision rationale.

**Smallest sufficient gate-publication guidance.** Use the lightest gate-publication guidance that preserves the next admissible reader move. Add crossing fields, launch fields, regulated fields, safety-critical fields, replay witnesses, `CrossingBundle`, `PQG`/`RSCR`, or MIP-run material only when the live gate-decision claim would otherwise become false, unsafe, non-replayable, or lack a named governing-definition locus.

**Minimum sufficient next move.** If there is only a guard, dashboard cue, explanation, or readiness-looking label and no `A.21` gate-decision relation, no gate is opened here. Once a gate is live, the low-risk publication minimum is `GateId + GateProfile + GateCheckRef set + CV aggregate + GateDecision + DecisionLogRef`; crossing, launch, regulated, and safety-critical fields appear only when those claims are live.

**Do not escalate when.** Do not turn cues, guards, narrative explanations, dashboard states, CV results, or readiness-looking labels into a `GateDecision`. Open A.21 only when a live gate-decision relation consumes check refs under an active `GateProfile`.

**Gate-looking display and conformance-label disposition.** A green tile, readiness badge, release screen, conformance label, `CV.Status`, safety-envelope note, or regulated-conformance phrase is not gate passage by resemblance. If the attempted use is gate passage, recover the active `OperationalGate(profile)`, `GateProfile`, effective `GateCheckRef` set, CV aggregate, `GateDecision`, `DecisionLogRef`, scope, and currentness/window. If those fields are not recoverable, keep the item as a display cue, source pointer, CV result, or evidence question and return to `A.10`, `A.20`, `B.3`, `E.19`, or the exact receiving pattern that carries the live claim. Safety envelope and assurance claims do not live in A.21 unless they are declared gate checks consumed under the active profile; their evidence and assurance support remain with `A.10` and `B.3`. Plain wording remains ordinary unless it changes admissible use, support, evidence, gate, assurance, work, decision, or neighboring-pattern exit.

**Common wrong first reading.** A green tile, readiness display, or release screen means `GateDecision=pass` exists. First honest entry: A.21 is live only when an active `OperationalGate(profile)` consumes declared checks and publishes a `GateDecision` with `DecisionLogRef`; otherwise the item remains a cue or source question.

Repaired anti-case: a release screen says all checks are green but no active `OperationalGate(profile)`, effective `GateCheckRef` set, `GateDecision`, or `DecisionLogRef` is recoverable. The display remains a cue or evidence question; the attempted gate-passage use has no supported current use until the A.21 gate-decision relation is recoverable.

**Same problem, different live question.** For a TGA-looking problem, use `E.18` for graph/flow/crossing, `A.20` for internal step validity, `A.21` for gate-decision publication, and `E.20` for mechanism-meaning placement; do not open the other three until their own claim is live.

**Semantic repair return.** When A.21 blocks a misleading word, face, alias, or source label, the repair must return to the enabled gate action: name the live gate-decision relation, active `GateProfile`, consumed `GateCheckRef` set, aggregate, `GateDecision`, and `DecisionLogRef` that remain admissible. Do not stop at a classification of vocabulary or publication faces.

**Governed-object and relation separation.** Keep the graph object and path or crossing relation (`E.18`), MVPK publication faces (`E.17`), internal CV status and witness (`A.20`), gate decision and `DecisionLog` (`A.21`), evidence or provenance relation (`A.10`/`G.6`), work plan or work occurrence (`A.15`), and mechanism-governing definition assignment (`E.20`) distinct. An MVPK face, `DecisionLog`, evidence carrier, MIP manifest, or work witness does not carry another pattern's project-side value unless that exact governing pattern consumes it for that relation.

**Smallest affected locus.** Localize the change to the smallest live locus: `PathSlice` or crossing in `E.18`, CV step in `A.20`, `GateDecision` equivalence class in `A.21`, or mechanism-governing definition in `E.20`. Do not widen to a whole flow or unrelated governed object when that locus is enough.

**Ordinary success.** For ordinary A.21 use, success is that the live gate-decision relation, active profile, check set, aggregated decision, and `DecisionLogRef` are placed without implying performed work or mechanism-intension truth. A full conformance review is needed only when crossing, launch, regulated, safety-critical, or replay claims consume expanded assurance or conformance material.

**Locality asymmetry.** `E.18` is graph-local, `A.20` is step-local, `A.21` is gate-local, and `E.20` is trigger-local. Do not normalize the four patterns into one assurance regime.

**Do not merge these pairs.** Keep `CV.Status` distinct from `GateDecision`, TGA `Check` distinct from `GateCheckKind`, MIP manifest distinct from `DecisionLog`, `ViewpointMap` distinct from graph semantics, `PathSlice` distinct from a work run, and `GateProfile=Lite` distinct from `PublishMode=Lite`.

**Field liveness.** Always core for A.21 once a gate is live: `GateId`, `GateProfile`, effective `GateCheckRef` set, CV aggregate, `GateDecision`, and `DecisionLogRef`. Conditional-live: crossing pins, LaunchGate pre-run barrier fields, regulated or safety-critical evidence refs, equivalence witnesses, and replay/currentness fields; open them only when the corresponding crossing, launch, regulated, safety-critical, replay, or reuse claim is live.

**Retrieval trap guard.** When excerpted alone, A.21 DecisionLog fields must not be read as requiring a full regulated log for every cue, guard, or low-risk gate. The `DecisionLog` content follows the live `GateDecision`, active profile, and conditional field-liveness rules.

**Anti-Goodhart guard.** A complete gate record is not a substitute for the governed gate result: the gate must still publish the correct `GateDecision` under the active profile, and that decision does not prove performed work or mechanism-intension truth. `DecisionLog` completeness does not make an invalid check true; check truth remains with the receiving patterns.

**Generative side.** A.21 preserves open-ended action by publishing explicit `GateDecision=pass`, `GateDecision=degrade`, `GateDecision=block`, or `GateDecision=abstain` decisions with rationale, so downstream work can continue, narrow, retry, or stop under declared conditions instead of being hidden behind an unreviewable cue.

**What goes wrong if missed.** A guard can be mistaken for a GateCheck, a human-readable explanation can be mistaken for the decision or decision record, and a dashboard-like pass/fail cue can be treated as gate passage without the `A.21` decision relation.

**What this buys.** A.21 gives the reader one place to separate profile fit, decision aggregation, rationale, optional explanation, and decision-record reuse while keeping gate logic out of CV and planning.

**Not this pattern when.** If the question is internal step constraint satisfaction, use `A.20`. If the question is graph crossing or valuation, use `E.18`. If the question is performed work or work planning, use the work/enactment or planning loci. If the text only contains a guard, cue, explanation, dashboard state, lexical pseudo-gate, or readiness-looking label without an `A.21` gate-decision relation, do not infer gate passage.

### A.21:1 - Problem frame

#### A.21:1.1 - Intent & scope

This pattern is the governing locus for canonical gate-decision publication content for `OperationalGate(profile)`: `GateCheckRef` as the GateFit check-catalog boundary, gate aggregation, `GateDecision` terminology, `GateDecisionRationale`, `GateDecisionExplanation`, `DecisionLog` minima, profile-bound folds, and A.21 decision equivalence. A.20 governs CV class meaning; an A.21 gate-decision relation may consume referenced CV results but does not define CV class semantics. Receiving patterns govern the domain truth conditions of their checks.

Within that boundary, A.21:

* aggregates per-check outcomes into a single **published** `GateDecision` using the join lattice,
* states the **CV⇒GF** activation boundary: GateFit checks are inactive until `CV.Status=pass`,
* defines the minimal **publication faces** and `DecisionLog` content required to make gate outcomes auditable and replayable,
* applies **SWP at the gate**: `OperationalGate(profile)` and its `GateCheck`s are **ref-only** with respect to editions, registries, and domain publications or records; A.21 publishes **only** `GateDecision` + `DecisionLog` pins and refs, and MUST NOT declare or mutate edition families.
This pattern is **about the semantics of what is published** (and how it composes), not about procedural execution.

#### A.21:1.2 - Intensional object(s)

* **`OperationalGate(profile)`** — a gate node (`U.Transduction(kind=Check)`) that mediates any **GateCrossing**: any change in `CtxState = ⟨L,P,E⃗,D⟩` **or** entry to `U.WorkEnactment` (via `LaunchGate`).
* **`GateProfile`** — the profile-bound constraint of the partial function `CtxState_from -> CtxState_to`; this pattern carries the current binding and minimum profile semantics. Fuller project-local profile matrices are support material unless a current governing pattern explicitly admits them.
* **`GateCheckRef`** — the publication lexeme that binds a check to `(aspect, kind, edition, scope)`.
* **`GateDecision` / `GateDecisionRationale` / `GateDecisionExplanation`** — decision value, structured rationale, and optional narrative (non-decision).
* **`DecisionLog`** — append-only audit record linking decisions to check refs, rule anchors, and (where applicable) SquareLaw mismatches.

#### A.21:1.3 - CV vs GF boundary (what “activation” means)

* **ConstraintValidity (CV)** evaluates *internal step validity*;
* **GateFit (GF)** is an aspect label on `GateCheckRef` for checks that evaluate *external admissibility vs `GateProfile`* (planes/crossings, freshness, evidence, roles/channels, regulator conformance, etc.). It is not a `U.Type`, node, record family, module, queue, or stage in the flow.

* **Ordering & activation.** CV is evaluated before GateFit; **while `CV.Status != pass`, all GateFit checks return `abstain`.**

#### A.21:1.4 - Failure cases (diagnostic lens)

* **CV ✔ / GF ✖**: internally valid transformation, but wrong gate/profile/role/timing/evidence.
* **CV ✖ / GF ?**: fix mechanism validity first; GF is inactive.
* **CV ✔ / GF ✔**: the gate may publish admissibility for the declared crossing; for `LaunchGate`, this is admissibility of crossing into `U.WorkEnactment`, not actual work occurrence.

#### A.21:1.5 - Non-goals

* No procedural semantics (no scheduling, no API formats, no automation narratives).
* No “second process order” outside the graph: every **check-point** is an `OperationalGate(profile)` node in the same transduction graph; its **pluggable GateChecks** are declared on the node (no floating checks), and only the declared check set + reaction rules vary across gates.
* No key/hash/cache *formats*: A.21 constrains **equivalence + invalidation conditions**, but not key materialization.
* No lexical “pseudo-gating”: a lexical alias view is non-decisional and MUST NOT be modeled as a GateCheckKind.

### A.21:2 - Problem

Without a unified GateFit core:

* Gate admissibility becomes ad-hoc, **order-dependent**, and hard to audit (especially with multiple independent checks).
* Gate logic enters CV (planes/comparators/freshness/roles appear “inside steps”), collapsing the CV/GF separation.
* “Unknown / timeout / error” behavior becomes implicit and inconsistent across cases, undermining reproducibility and safety.
* Publication faces drift into “extra semantics” (computed scalars / tool encodings) rather than pins + refs, breaking MVPK discipline.

### A.21:3 - Forces

* **Separation vs convenience.** Keeping CV internal and GF profile-bound keeps the boundary explicit, but demands a crisp activation boundary.
* **Determinism vs incompleteness.** Gate decisions stay deterministic even when evidence is missing or partial (`unknown`).
* **Safety vs throughput.** Some profiles treat ambiguity as `block`, others as `degrade`.
* **Human comprehension vs formal minimality.** Optional narratives help readers, but SHALL NOT be used as decisions.
* **Reuse vs freshness.** Decisions may be reusable only under explicit equivalence; otherwise re-aggregation is mandatory.
* **Scope granularity vs complexity.** Checks are declared with scopes (`lane|locus|subflow|profile`) and merged; duplicates preserve evidence rather than overwrite it.

### A.21:4 - Solution

#### A.21:4.1 - Gate = microkernel of checks

> **Note (guards are not GateChecks).** `USM.CompareGuard` and `USM.LaunchGuard` are **not** `GateCheckKind`s; they may emit `GuardFail` events which are aggregated by the gate referenced by the existing aggregation-assignment field `GuardOwnerGateId` under the active profile (`degrade|block`) and recorded in `DecisionLog`. Guard vocabulary is received through `A.2.6`; gate aggregation remains here.
`OperationalGate(profile)` is treated as a microkernel: checks are **pluggable** `GateCheck`s; the gate core **aggregates** their outputs **conceptually**, without procedural semantics and without mutating the transduction graph.

#### A.21:4.2 - Publication lexemes and register discipline

**Per-check reference lexeme.**
`GateCheckRef := { aspect, kind, edition, scope }`, where:
* `aspect ∈ {ConstraintValidity, GateFit}`,
* `scope ∈ {lane|locus|subflow|profile}`.

**Short-form shorthand (not publication-valid).**
If a local short form `{ kind, edition, scope }` appears in prose, it is interpreted only as a projection of the normative record with `aspect` supplied explicitly at the point of publication. Any published face or `DecisionLog` entry MUST use the full `GateCheckRef` with `aspect`.

**Decision terminology separation.**

* `GateDecision` is the published lattice value.
* `GateDecisionRationale` is the minimal structured support of that decision (check outcomes, folds, witness refs).
* `GateDecisionExplanation` is optional, human-readable, derived from the rationale; it **does not carry decision status** and MUST NOT be used as one.

**Register discipline.** Tech labels are ASCII and twin-labeled where the plain form uses symbolic notation.
(Example: use `CLPlane` / “CL^plane”, `CLKind` / “CL^k”, `UNM.TransportRegistryPhi` / “UNM.TransportRegistryΦ”, `GammaTimeRule` / “Γ_timeRule”.)

#### A.21:4.3 - CV⇒GF activation predicate (counterfactual boundary)

GateFit checks are *defined* as inactive unless `CV.Status=pass`:
* Let `CV.Status` be the join-aggregate of all `GateCheckRef` with `aspect=ConstraintValidity`.
* For any `GateCheckRef` with `aspect=GateFit`:
  **If `CV.Status ≠ pass`, the GateFit check outcome is `abstain`.**
* While `CV.Status ≠ pass` **(or the active profile suppresses narratives)**, any GateFit-oriented `GateDecisionExplanation` **does not apply**.

This keeps the boundary crisp: CV explains internal validity; GF explains profile-fit **only in the counterfactual world where `CV.Status=pass` holds**.

**LaunchGate pre‑run barrier (work‑boundary special case).**

For the unique `LaunchGate` at the entry of each `U.Work`/`U.WorkEnactment`, let `Prev.CV.Status` denote the aggregate over the declared ingress predecessor set or ingress cut-set for the addressed `PathSlice`. In a linear path this may be one predecessor; where graph or fan-in semantics are live, it is not reduced to one immediately preceding step.

* If `Prev.CV.Status ≠ pass`, then (i) all GateFit-scoped LaunchGate checks return `abstain` by activation, and (ii) the **overall LaunchGate** decision is forced to `block` (pre‑run barrier). The rationale MUST record the predecessor CV status and the forced-block rule in `DecisionLog`.

This is a publication-safety invariant: it constrains what may be admitted at the work boundary without specifying evaluation order or execution scheduling. Actual launch values and work occurrences remain governed by `A.15`.

#### A.21:4.4 - Decision algebra: join-semilattice (“worst wins”)

A.21 adopts order-independent aggregation, not a universal policy language or a one-size-fits-all safety rule. The gate core does not define the domain truth of checks; it aggregates declared check outcomes under the active profile.

**Decision domain.** `GateDecision ∈ {abstain, pass, degrade, block}`.

**Aggregation rule.** Aggregation over all applicable checks is the **idempotent, commutative, associative join** on
`GateDecision` values `abstain <= pass <= degrade <= block`, with **neutral = `abstain`** and **absorbing = `block`**.

Publications carry only:

1. the aggregated `GateDecision`, and
2. its `GateDecisionRationale` recorded in the `DecisionLog`.

#### A.21:4.5 - Profile-bound folds for `error|timeout|unknown`
A check may encounter `error`, `timeout`, or evidence-scoped `unknown`. These do **not** become new decision values; they are folded into the decision lattice **by profile and check policy**.
**Normative minimum folds (tri-state).**

> **Naming note.** Some conformance tables use **Lean** as a label for the `GateProfile=Lite` gating posture. Treat this as an alias only, and do not confuse it with `PublishMode=Lite` (a publication-face reduction mode).

| Active `GateProfile` | `error` fold | `timeout` fold | `unknown` fold (evidence-scoped) |
| -------------------- | -----------: | -------------: | ------------------------------: |
| `Lite`               |    `degrade` |      `degrade` | per `GateCheck` policy (`abstain` or `degrade`) |
| `Core`               |    `degrade` |      `degrade` | per `GateCheck` policy (`abstain` or `degrade`) |
| `SafetyCritical`     |      `block` |        `block` | per `GateCheck` policy (safety-default: `degrade`) |
| `RegulatedX`         |      `block` |        `block` | per `GateCheck` policy (safety-default: `degrade`); X identity and edition are recorded in `DecisionLog` |

Where a `GateCheck` declares an evidence-scoped `unknown` strategy, that strategy is part of the check’s intensional definition; the fold applied and its justification are recorded in `DecisionLog`.

#### A.21:4.6 - GateProfiles: current binding and minimum profile semantics

A.21 binds the following *functional role* of `GateProfile`:

> **Terminology (avoid `Lite`/`Lean` confusion).** `GateProfile=Lite|Core|SafetyCritical|RegulatedX` is the **gating posture** that determines the effective GateCheck set and fold policies. `PublishMode=Lite` is a **publication-face reduction mode** (AssuranceLane‑Lite / TechCard‑Lite) and MUST NOT be interpreted as a reduced-obligation `GateProfile`.

* A `GateProfile` is an attribute of a **branch or `PathSlice`**; the default is `Core`.
* Local overrides may change the active profile for the current GateCrossing and its subordinate scope **but cannot reduce** the already-effective set of `GateCheckKind`s; only additions are allowed. Weakening SHALL use a new `PathSlice` via sentinel.
* `PublishMode=Lite` changes *face reduction only* and does **not** weaken the check set or aggregation rule.

#### A.21:4.7 - Scope and merge semantics (`lane|locus|subflow|profile`)

* Each `GateCheckRef` declares its scope; `subflow` scope is bounded by a sentinel bridge (restart / refresh boundary).
* The effective check set is formed by **union across all declared scopes**; duplicates by `kind` merge by the same join rule (“worst wins”), and **all rationales are preserved** in `DecisionLog`.
  * For `RegulatedConformance(X)`, the identity of **X** and its rule/edition reference are part of the rationale record; multiple `RegulatedConformance(X{…})` may coexist in one gate.
* A check outside its scope reports `abstain`.

#### A.21:4.8 - Publication repeatability, caching, and re-aggregation triggers
**Repeatability (publication).** Gate decisions MUST be replayable from declared pins/refs: no implicit “latest/now”. Any time basis is made explicit via `Γ_time` (or a `Γ_timeRule` that resolves to a concrete basis), and the resolved basis is recorded in `DecisionLog`.

**Caching constraint (publication).** A gate decision may be cached **only** per
`{PathSliceId, GateProfile, GateChecks.editions, editions{…}}`, where `GateChecks.editions` denotes the canonicalized, order-independent listing of the **effective** `GateCheckRef{aspect,kind,edition,scope}` (including their `edition`s) for this gate instance. Cache reuse is valid only while the declared freshness/evidence window remains valid under the active profile.

**Re-aggregation triggers (non-exhaustive, normative).** Re-aggregation is required if any of the following changes (slice-local; no execution method implied):

* any component of `editions{…}` changes (any `edition_key ↦ EditionId` bump),
* any `GateCheckRef.edition` changes (including regulator X editions for `RegulatedConformance(X)`),
* the declared `Γ_time` basis changes or resolves differently,
* a relevant `FreshnessTicket` expires/changes or TOCTOU window constraints change,
* a sentinel-bounded `subflow` refresh adds an SCR/RSCR carrier to the `DecisionLog` rationale-anchor set,

* any input breaks the declared `A.21` equivalence witness.

Decision stability is under the `A.21` equivalence relation; a witness is recorded on the `DecisionLog` (see §4.10). A.21 constrains equivalence + invalidation conditions but does not fix key formats.

#### A.21:4.9 - MVPK faces for `OperationalGate(profile)` (minimum pins)

The gate publishes faces to record **what is declared**, not “how it executes”. Faces remain **pins + refs** (no new numeric claims; no I/O re-listing).

**Minimum pins (PlainView / TechCard / AssuranceLane where applicable).**

* View scope: `PublicationScopeId` (with MVPK profile: `Min|Lite|SetReady|Max`)
* Identity: `GateId`, `BridgeId`, `PathId`, `PathSliceId`
* Temporal: `DesignRunTagFrom`, `DesignRunTagTo`
* Profile: `GateProfile` (`PublishMode` changes only face reduction)

* Checks: list of `GateCheckRef` (`aspect`, `kind`, `edition`, `scope`)
* CV: aggregated `ConstraintValidityStatus` and optional `ConstraintValidityWitnessRef` (refs only)
* Editions: `editions{…}` vector + `EditionPins{CGSpec, ComparatorSet, UNM.TransportRegistryPhi}`
  * **Gate-requirement on edition refs.** Any face that cites `CGSpec`, `ComparatorSet`, or `UNM.TransportRegistryPhi` editions also includes `BridgeCard + UTS row` through `F.9`, `F.17`, `E.17`, and `E.18`; otherwise downstream consumption is non-conformant.
* ReferencePlane and CL: source `ReferencePlane` pins and target `ReferencePlane` pins; `CLPlane` / “CL^plane” (for non-crossings `CL^plane = none` is allowed, but pins are still explicit); any Φ penalties are published as rule refs and appear in the **R-channel only**
* Freshness: declared `GammaTime` / “Γ_time” pin and presence/absence of `FreshnessTicket` (refs)
* Evidence: SCR/RSCR carrier anchors (refs) + VALATA (VA/LA/TA) presence on AssuranceLane
* Guards: `USM.CompareGuard` / `USM.LaunchGuard` applicability pins (presence-only; GuardFail uses the `A.2.6` guard vocabulary and is aggregated here by the gate referenced by the existing aggregation-assignment field `GuardOwnerGateId`)
* Decision: aggregated `GateDecision` and `DecisionLogRef`

**Lean face (PublishMode=Lite).** It MAY fold to `GateProfile / GateChecks / EditionPins / GateDecision + DecisionLogRef`, but:

* it MUST keep `GateProfile` and `DecisionLogRef`,
* it MUST not weaken GateChecks or the aggregation algebra, and
* if `EditionPins` are present, it still includes `BridgeCard + UTS row` through `F.9`, `F.17`, `E.17`, and `E.18` and preserves the crossing boundaries (explicit `ReferencePlane`, `CLPlane`, and Φ -> R-channel only).

#### A.21:4.10 - DecisionLog (minimum composition)

`DecisionLog` is an append-only record of reasons and references:

* gate identity + `PathSliceId` (+ `PublicationScopeId` when the log is published via a face bundle)
* each `GateCheckKind`, its `GateCheckRef.edition`, and its folded outcome (`pass|degrade|block|abstain`) including the applied `error|timeout|unknown` fold
* rule anchors / evidence anchors (SCR/RSCR carriers + VALATA bindings); SquareLaw mismatched pins appear only when the crossing check is live

* policy-id dependencies used by checks (as `PolicyIdRef` bundles per F.8:8.1); `Φ(CL)`, `Φ_plane`, and `Ψ(CL^k)` appear only when bridge or crossing is live, while gate-local policy ids appear only when consulted by the active profile

* `GuardFail` events only when guard events exist; if present, they are received from `USM.Guards` and aggregated by the gate referenced by the existing aggregation-assignment field `GuardOwnerGateId` with the applied profile rule (`degrade|block`)

* `EquivalenceWitness` (or `EquivalenceWitnessRef`) as an `A.21` publication item, minimally: `{ keys, E⃗, Γ_time(basis), PathSliceId?, ReturnShapeClass, ComparatorSetRef?, profile }`; use `G.6` or `G.11` where evidence-path visibility or refresh implications are live
* the declared publish reaction for `degrade|block` only when that outcome has a declared publication consequence, including any local “degrade mode” notes when permitted by profile

* for `RegulatedConformance(X)`, only when `RegulatedConformance(X)` is active: the identity of X and the rule/edition references used

#### A.21:4.11 - GateChecks admissibility (GateFit-only catalog boundary)

**Mandatory on LaunchGate.** `FreshnessUpToDate`, `DesignRunTagConsistency`.
**Allowed GateFit checks (non-exhaustive, normative minima).**

* `DesignRunTagConsistency` (mandatory on LaunchGate; may appear elsewhere)
* `FreshnessUpToDate` (mandatory on LaunchGate; may appear elsewhere)
* `ReferencePlaneCrossing`
* `ComparatorConstraintRules (CSLC)`
* `EvidenceCompleteness`
* `SafetyEnvelope`
* `RegulatedConformance(X)` (X identity plus edition and rule refs are recorded in `DecisionLog`)
* `Role/ChannelFit` (roles are Kernel `U.Role` tokens, not alias strings)
* `EquivalencePreservation`
* `OutflowAudit`
* `SnapshotConsistency`

**Receiving-pattern truth examples (informative).** A.21 names and aggregates the check; it does not decide the domain truth condition. `EvidenceCompleteness` returns to `A.10`, `G.6`, or `B.3`; `Role/ChannelFit` returns to `A.2`, `A.15`, or `A.2.6`; `ReferencePlaneCrossing` returns to `E.18`, `F.9`, `F.17`, and UNM; `ComparatorConstraintRules` returns to `A.19`, `G.0`, `G.5`, `C.18`, `C.19`, `G.9`, or `G.11` where comparator, archive, parity, set-return, or refresh claims are live; `SafetyEnvelope` and `RegulatedConformance(X)` return to the safety or regulatory pattern that governs the envelope or rule.

**Forbidden (hard boundary).**

* Modeling CV classes “as GateFit” (CV classes remain CV; GF remains GF).
* Any “LEX gate checks” or lexical pseudo-checking (lexical views do not participate in decisions).

#### A.21:4.12 - SquareLaw compatibility at crossings
For every GateCrossing, the SquareLaw constraint SHALL hold:
`gate_out ∘ transfer = transfer' ∘ gate_in`.

Profile selection/inheritance does not weaken this requirement; inconsistency yields `block|degrade` within the active profile and is recorded in the DecisionLog. LaunchGate is a work-boundary GateCrossing case, so SquareLaw is mandatory there as well.

#### A.21:4.13 - Lexical mediation (optional trace, non-decisional)

A gate MAY publish a `LexicalResolutionRef` / `LexicalView` for traceability of alias resolution, but:

* it does **not** participate in aggregation, and
* it is not a `GateCheck` input and cannot change `GateDecision`.

### A.21:5 - Archetypal Grounding

#### A.21:5.1 - System vignette — “Regulated release gate”

**Show 0 (green cue, no gate decision).** A dashboard tile says “ready” because a source system returned green. No `OperationalGate(profile)`, `GateCheckRef` set, `GateDecision`, or `DecisionLogRef` is named. The tile remains orientation or source-finding only; it is not gate passage and does not open A.21 decision reuse.

**Tell.** A flow reaches a `LaunchGate` just before a `U.WorkEnactment` that can finalize binding. The active profile is `RegulatedX`. The gate publishes a single `GateDecision` and a `DecisionLog` that explains *why* the release is admissible (or not), without encoding any execution method.

**Show A (CV ✔, GF ✖).** `CV.Status=pass`, activating GateFit. `RegulatedConformance(X)` is present but evidence anchors are incomplete (`EvidenceCompleteness` folds to `degrade` under `Core/RegulatedX` policy), so the join yields `GateDecision=degrade`. The DecisionLog records which `GateCheckRef` caused the fold and the declared publish reaction for degraded release.

**Show B (CV ✖, GF n/a).** CV aggregate is `degrade`. All GateFit checks return `abstain` by activation, and any GateFit-oriented explanation is inapplicable. The gate’s published decision is driven by CV; the DecisionLog shows CV status and the “inactive GF” boundary rather than a fabricated GF narrative.

#### A.21:5.2 - Episteme vignette — “Cross-plane comparability gate”

**Tell.** A flow reaches a comparability-critical step (CSLC). The gate publishes `BridgeId + UTS + CLPlane` and edition pins for downstream consumers, and remains stable under the `A.21` equivalence witness.

**Show A (Core, clean crossing).** The gate publishes `EditionPins{CGSpec, ComparatorSet, TransportRegistryPhi}`, `ComparatorSetRef`, `CL/CLPlane`, and a `GateDecision=pass` with a rationale that cites the relevant `GateCheckRef`s and editions.

**Show B (SquareLaw mismatch).** A crossing attempts to change plane pins without the commutative-square witness; the SquareLaw check yields `block` (or `degrade` under a profile with a less strict fold policy), and the DecisionLog records the mismatched pins as the reason.

### A.21:6 - Bias-Annotation

This pattern’s built-in biases are stated across the five Principle-Taxonomy lenses (Gov, Arch, Onto/Epist, Prag, Did).

* **Gov.** Bias toward auditability and explicit responsibility (DecisionLog + profile-bound folds). Risk: gate-stewardship roles become de facto governors; mitigation: keep profiles explicit, inheritable, and pinned to `PathSliceId` for reviewable replay.
* **Arch.** Bias toward a microkernel of checks (pluggable GateChecks + join aggregation). Risk: “check sprawl”; mitigation: scope discipline + forbidden LEX pseudo-checking + CC-based profile minima.
* **Onto/Epist.** Bias toward a 4-value admissibility lattice and explicit “does not apply” boundaries. Risk: oversimplifying nuanced epistemic uncertainty; mitigation: preserve structured rationales and allow check-scoped `unknown` policies rather than inventing new global decision values.
* **Prag.** Bias toward determinism and replayability (cache invalidation by pinned vectors). Risk: higher publication overhead; mitigation: PublishMode=Lite for faces (never for weakening checks).
* **Did.** Bias toward explicit separation (CV vs GF) and “what is published” clarity. Risk: more concepts to learn; mitigation: archetypal grounding + stable minimal pins across faces.

### A.21:7 - Conformance Checklist

**Conformance use.** This checklist is evidence for the gate-decision publication guidance already stated in the Solution. It is not the first entry text for ordinary use and not a full audit regime by default; an item is applied only when its corresponding gate, check set, decision, crossing, launch, publication, or assurance move is live. Before applying any item, name the Solution move it tests; if no such reader move is live, treat the item as support-only or not applicable rather than expanding the applied assurance or conformance material.

**Conformance groups.** Ordinary gate use starts with the active gate, check set, CV aggregate, `GateDecision`, and `DecisionLogRef`. Crossing/launch items apply only when the gate is a GateCrossing or `LaunchGate`. Publication/assurance items apply only when MVPK faces, evidence carriers, decision stability, or replay are live. Extension/change items apply only when lexical tokens, profile variants, or neighboring policy/evidence loci are being changed or consumed.

Minimum unified conformance for A.21 (and any flow that claims GateFit discipline):

#### A.21:7.1 - Core gate semantics

* [ ] **CC‑TGA‑06**: all GateCrossings (CtxState changes, and work-boundary crossings via LaunchGate) are mediated by `OperationalGate(profile)` and have a `DecisionLog`.
* [ ] **CC‑TGA‑07**: CV=>GF activation predicate holds (`CV.Status!=pass => GF=abstain`).
* [ ] **CC-TGA-21**: decision stability witness is present on the `DecisionLog` record as an `A.21` `EquivalenceWitness` or `EquivalenceWitnessRef`.
* [ ] **CC‑TGA‑21a**: aggregation is the join on `GateDecision` values `abstain <= pass <= degrade <= block`; `GateDecisionExplanation` is optional and non-decisional.
* [ ] **CC‑TGA‑22**: `error|timeout` folds are profile-bound; `unknown` folds per GateCheck policy.
* [ ] **Gate-looking display boundary**: a dashboard state, green tile, readiness badge, conformance label, CV result, safety-envelope note, or release screen is not gate passage unless active `OperationalGate(profile)`, effective `GateCheckRef` set, aggregate, `GateDecision`, `DecisionLogRef`, scope, and currentness/window are recoverable.

#### A.21:7.2 - LaunchGate discipline (pre-run barrier)

* [ ] **CC‑TGA‑08**: every `U.WorkEnactment` has exactly one `LaunchGate` with mandatory `FreshnessUpToDate` + `DesignRunTagConsistency`; **pre‑run barrier:** if `ConstraintValidityStatus!=pass` over the declared ingress predecessor set or ingress cut-set for the addressed `PathSlice`, then all LaunchGate GateFit checks are `abstain` and the overall `GateDecision=block` (logged).

* [ ] **Pre‑Run barrier** is satisfied for any `U.Work` where `FinalizeLaunchValues` is possible.

#### A.21:7.3 - Publication and evidence

* [ ] **CC‑TGA‑20**: `PublishMode=Lite` changes face reduction only; required GateChecks remain intact.

* [ ] **CC‑TGA‑25**: AssuranceLane carries `GateProfile`, `GateCheckRef` list, edition pins, `GateDecision`, and `DecisionLogRef` with the two-part evidence scheme (SCR/RSCR + VALATA).

#### A.21:7.4 - Cross-boundary additions (when the gate is a crossing)

* [ ] **CC‑TGA‑11**: crossings publish `BridgeId + UTS + CLPlane/CL^plane`, penalties appear in the R-channel only.
* [ ] **CC‑TGA‑23**: SquareLaw holds on crossings; mismatch yields `block|degrade` per profile and is logged.

#### A.21:7.5 - Lexical norms (E.10 discipline)

* [ ] Tech names are ASCII and twin-labeled; required token classes are registered under LEX (including `GateProfile`, `GateCheckKind`, `GateCheckRef`, `DecisionLog`).
* [ ] Any lexical alias view is trace-only and cannot change `GateDecision`.

### A.21:8 - Consequences

**Benefits**

* **Deterministic gating.** Join-semilattice aggregation makes decisions order-independent and idempotent (modulo declared equivalence), enabling consistent audit and replay.
* **Clean CV/GF separation.** Activation boundary keeps profile concerns out of mechanism validity.
* **Profile clarity.** Fold policies (`error|timeout|unknown`) are explicit and profile-bound, making safety posture reviewable.
* **Publication hygiene.** MVPK faces remain pins+refs (no new numeric claims), and DecisionLog captures rationale without procedural commitments.

**Trade-offs**

* **More decision records to publish.** Decisions are not “just pass/fail”: they require rationales, pins, and logs.
* **Two-stage reasoning.** Users need the rule “GF does not apply until `CV.Status=pass` holds”; mitigated by explicit inapplicability rules and optional narratives only when applicable.
* **Scope complexity.** Multi-scope merge semantics can feel heavy; mitigated by union + worst-wins + preserved rationales.

### A.21:9 - Rationale

* The microkernel framing preserves a single graph semantics: checks are nodes and publications, not an external pipeline; this keeps a second hidden process order outside the gate core.
* The join lattice provides a minimal, monotone aggregation that supports:

  * early absorption at `block` without specifying execution strategy, and
  * deterministic publication semantics (commutative + associative + idempotent).
* CV⇒GF activation is the mechanism that keeps orthogonality strict while still publishing a single gate decision publication: GF results do not replace CV failures.
* Explicit folds for `error|timeout|unknown` make safety posture reviewable and profile-specific without inventing new decision values.

### A.21:10 - SoTA-Echoing

Anchors (post-2015) that this pattern **adopts/adapts/rejects**, consistent with the TGA goal of assured lanes, open graph composition, and join-semantics.

* **Adopt.** *Join-semilattice aggregation as deterministic, profile-bound merge* (distributed systems / CRDT literature, e.g., Kleppmann 2017; Kleppmann & Beresford 2017): A.21 uses the algebraic idea only so declared gate-check outcomes fold to the same `GateDecision` under the same active profile and equivalence witness. It does not import CRDT architecture or use CRDT as prestige terminology.

* **Adapt.** *Compositional reasoning with commuting diagrams* (applied category theory, e.g., Fong & Spivak 2019): A.21 adapts the intuition by making SquareLaw a gate-audited invariant on crossings, while keeping publications human-first and pin-based.
* **Adapt.** *Supply-chain provenance / policy gating via attestations* (software supply-chain security, e.g., in-toto 2019; SLSA v1.2 current specification for provenance and VSA attestation formats): A.21 adapts the attestation-shaped evidence discipline as MVPK pins plus `DecisionLog`, not DevOps workflow, tool-specific methods, or runtime scripts.

* **Reject.** *Narrative-as-authority.* Any approach where human-readable explanations function as decision-bearing records is rejected; in A.21, narratives remain optional derivatives of structured rationales and are explicitly non-decisional.

Action result from the gate-publication and attestation practice basis: green tiles, readiness badges, release screens, conformance labels, safety-envelope notes, CV results, and gate-looking explanations do not become gate passage, release permission, safety acceptance, assurance, work occurrence, or work authorization by appearance. The local A.21 result is an active `OperationalGate(profile)`, active `GateProfile`, effective `GateCheckRef` set, CV aggregate, `GateDecision`, `DecisionLogRef`, scope, and currentness/window, or else the item remains a cue, source pointer, CV result, evidence question, or neighboring-pattern exit. Reopen the gate result when the active profile, check set, CV aggregate, decision, rationale, scope, currentness/window, equivalence witness, or consuming neighboring relation changes.

### A.21:11 - Relations

* **E.TGA →coordinates→ A.21.** GateFit-scoped GateChecks are aggregated by `OperationalGate(profile)`; enumeration and publication shape of GateChecks live here.
* **A.20 →couples_to→ A.21 via CV=>GF.** CV is evaluated inside transformations; while `CV.Status!=pass`, GF is `abstain` and GF explanations do not apply.
* **A.21 GateProfile binding.** A.21 carries the current profile binding, inheritance boundary, and minimum mandatory check-set semantics. Fuller matrix support is not a separate current authority unless a current governing pattern explicitly admits it.
* **E.18 / G.11 →provide→ scope and refresh boundaries.** `subflow` scope is bounded and restartable through PathSlice and refresh wiring where live; weakening check sets SHALL use a new `PathSlice`.
* **F.9 / F.17 / E.17 / E.18 →required_by→ any edition-citing face.** Whenever gate faces cite editions, the compatibility reference (BridgeCard + UTS + `CL/CLPlane`) is required for downstream consumption.
* **A.21 / G.6 / G.11 →define→ equivalence for decision stability.** Gate decisions are stable only under the declared equivalence witness; evidence-path or refresh implications use `G.6` or `G.11` where live.

### A.21:End

