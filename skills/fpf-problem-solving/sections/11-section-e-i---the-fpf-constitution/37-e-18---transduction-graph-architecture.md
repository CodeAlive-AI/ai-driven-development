## E.18 - Transduction Graph Architecture (E.TGA)

> **Tech‑name:** **E.TGA** (pattern label)
> **Plain‑name:** Architecture of the transduction graph
> **Twin labels:** Tech / Plain per E.10; faces emitted via E.17 MVPK (no schemas in Part E).

### E.18:1 - Intent

Provide a **notation‑independent** architecture for graphs whose vertices are **morphisms (transductions)** and whose edges are **typed transfers**. The architecture is **agnostic to the concrete morphism set** and equips the graph with **publication, comparability, crossing, and budget** disciplines so that **flows** are **valuations over paths** within the same graph object. Faces appear via **MVPK**; numeric/comparable publication carries **pins** with **Bridge/CL** notes; Φ/CL^plane penalties remain in **R**.
**Admissibility wording.** E.TGA criteria are model conditions: if the declared graph, path, crossing, or publication conditions hold, the E.TGA explanation applies; otherwise it does not apply. Duty verbs appear only in named conformance minima.

**Use this when.** Use E.TGA when the live question is whether a project description needs one transduction graph relation, one graph crossing, or one flow valuation over `U.Transfer` rather than an ordered work/method narrative.

**First useful move.** Name the graph object, the node kinds, the single `U.Transfer` edge kind, and the exact crossing or path slice whose pins are required.

**Smallest sufficient graph and path guidance.** Use the lightest graph and path guidance that preserves the next admissible practitioner move. Add extra pins, witnesses, `DecisionLog` detail, `CrossingBundle`, `PQG`/`RSCR`, or MIP-run material only when the live claim would otherwise become false, unsafe, non-replayable, or lack a named governing-definition locus.

**Minimum sufficient next move.** For the ordinary case, name `TransductionGraph`, the active `PathId` or `PathSliceId` when a path or slice is live, the node kinds, one `U.Transfer`, and only the crossings or pins that are live. If there is no crossing, comparison, launch, or refresh claim, do not open `CrossingBundle`, `GateProfile`, or `DecisionLog`.

**Do not escalate when.** Do not create a graph kind from semio wording, lineage metadata, tool-pipeline order, or reference-flow prose. Keep those as source wording or neighboring support unless a live `TransductionGraph`, path, flow valuation, or crossing relation is being governed here.

**Same problem, different live question.** For a TGA-looking problem, use `E.18` for graph/flow/crossing, `A.20` for internal step validity, `A.21` for gate-decision publication, and `E.20` for mechanism-meaning placement; do not open the other three until their own claim is live.

**Semantic repair return.** When E.TGA blocks a misleading word, face, alias, or source label, the repair returns to the enabled graph/path/crossing action: name the graph relation, path or flow valuation, or crossing boundary that remains admissible. Do not stop at a classification of vocabulary or publication faces.

**Governed-object and relation separation.** Keep the graph object and path or crossing relation (`E.18`), MVPK publication faces (`E.17`), internal CV status and witness (`A.20`), gate decision and `DecisionLog` (`A.21`), evidence or provenance relation (`A.10`/`G.6`), work plan or work occurrence (`A.15`), and mechanism-governing definition assignment (`E.20`) distinct. An MVPK face, `DecisionLog`, evidence carrier, MIP manifest, or work witness does not carry another pattern's project-side value unless that exact governing pattern consumes it for that relation.

**Smallest affected locus.** Localize the change to the smallest live locus: `PathSlice` or crossing in `E.18`, CV step in `A.20`, `GateDecision` equivalence class in `A.21`, or mechanism-governing definition in `E.20`. Do not widen to a whole flow or unrelated governed object when that locus is enough.

**Ordinary success.** For ordinary E.TGA use, success is that the graph object, path or slice, single transfer edge kind, and any live crossing boundary are placed without hidden work/method order or hidden scalarization. A full conformance pass is needed only when the downstream claim consumes expanded assurance or conformance material.

**Locality asymmetry.** `E.18` is graph-local, `A.20` is step-local, `A.21` is gate-local, and `E.20` is trigger-local. Do not normalize the four patterns into one assurance regime.

**Do not merge these pairs.** Keep `CV.Status` distinct from `GateDecision`, TGA `Check` distinct from `GateCheckKind`, MIP manifest distinct from `DecisionLog`, `ViewpointMap` distinct from graph semantics, `PathSlice` distinct from a work run, and `GateProfile=Lite` distinct from `PublishMode=Lite`.

**Field liveness.** Always core for E.TGA: graph object, node kinds, one `U.Transfer`, and the path or slice being governed. Conditional-live: `CrossingBundle`, `GateProfile`, `DecisionLog`, `ViewpointMap`, evidence carriers, refresh pins, and launch/work-boundary fields; open them only when the corresponding crossing, publication, evidence, refresh, gate, or work-boundary claim is live.

**Retrieval trap guard.** When excerpted alone, E.TGA vocabulary is not read as governing `GateCheckRef`, full viewpoint taxonomy, or gate publication semantics. `A.21` governs gate publication, `E.17` governs MVPK faces, and S12-style viewpoint material is conditional support, not the graph architecture itself.

**Anti-Goodhart guard.** Passing E.TGA conformance is not a substitute for the governed graph result: the graph still avoids hidden work/method order, hidden crossings, hidden scalarization, and unsupported path/slice currentness.

**Generative side.** E.TGA preserves open-ended action by keeping set-return, archive preservation, admissible loops, and budgeted refresh visible; these are not merely assurance checks, but the reason the graph can carry multiple future paths without collapsing them into one score or one pipeline.

**What goes wrong if missed.** A practitioner may treat a reference flow, a semio word such as `transition`, or a tool pipeline as a new graph kind or a second work/method order, then lose comparability, crossing evidence, and slice-local refresh boundaries.

**What this buys.** E.TGA lets the practitioner keep graph structure, publication pins, crossings, CV/GF separation, and refresh locality in one current architecture without turning every domain path into its own flow doctrine.

**Not this pattern when.** If the problem is only internal step constraint satisfaction, use `A.20`. If it is gate profile fit or gate decision aggregation, use `A.21`. If it is mechanism-intension meaning, citeable-token denotation, suite membership, planned-baseline pins, or wiring semantics, use `E.20`. If the text asserts that work occurred or should occur, use the work and enactment loci; `E.18` can locate entry to `U.WorkEnactment` as a crossing, but it does not assert work occurrence. If the text only uses semio wording such as `transition` without a live transduction relation and governed object, do not mint a graph kind; keep the phrase in the semio pattern or source-local wording that carries it.

### E.18:2 - Problem frame

Teams can produce many **valid flows** over the same capability: e.g., the P2W reference path
`U.FormalSubstrate → U.PrincipleFrame → U.Mechanism → U.ContextNormalization (UNM) → U.SelectionAndTuning ↔ U.WorkPlanning → U.Work → U.EvaluatingAndRefreshing`
is one **path** among many possible domain paths. Without a common **graph architecture**:

* flows look ad‑hoc and **non‑comparable**;
* cross‑Context **crossings** (plane/Context changes) are undocumented;
* MVPK faces carry **hidden arithmetic** or restate I/O;
* set‑returning selection is silently replaced by **single scores**;
* cycles lack **budget** discipline; refresh is **out‑of‑band**.

MVPK already fixes publication drift at the **single-arrow** scope; E.TGA lifts those **publication and comparability laws** to the **graph as a whole**.

### E.18:3 - Problem

1. **Morphisms ≠ Graph.** A catalog of morphism-scoped patterns (e.g., UNM, Selector, Work, Refresh) does not, by itself, explain **how the whole graph is built, constrained, and audited**.
2. **Flow proliferation.** Multiple “reference flows” can be declared; practitioners need **one graph discipline** that keeps them admissible and comparable **without privileging any single flow**.
3. **Unsafe publication.** Faces re‑list I/O, hide scalarization, or omit edition/plane pins; cross‑Context reuse lacks **Bridge/CL** citation; **plane penalties** appear in F/G instead of R.
4. **Cycles without norms.** Selection↔Planning loops run without explicit **budget (Γ_time)**, **FreshnessRequest**, or **slice‑scoped** refresh; `FinalizeLaunchValues` (launch‑value slot filling) is performed too early (outside `U.Work` (`U.WorkEnactment`)).

### E.18:4 - Forces

| Force                                            | Tension                                                                                                                                                                    |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Universality vs specialization**               | One architecture needs to cover supply chains, water networks, ML functionals, and the P2W first-principles-to-work path, **without** baking in any one morphism set. |
| **Publication neutrality vs auditability**       | Keep faces notation‑neutral and non‑mechanistic ↔ require **pins**, **ComparatorSet**, **Bridge/CL**, and **PublicationScope**.                                            |
| **Set-return discipline vs business pressure for totals** | Preserve **return sets and declared partial orders** ↔ stakeholders demand single numbers.                                                                                     |
| **Cross‑Context reuse vs safety**                | Enable reuse across `U.BoundedContext` ↔ require **Bridge/CL** with **R‑only penalties**.                                                                                  |
| **Agility vs reproducibility**                   | Permit evolving CG‑Spec/UNM/Comparator editions ↔ require **edition pins** and **re‑emission** on change.                                                                  |
| **Cycles vs convergence**                        | Allow Selection↔Planning iteration ↔ impose **budget** and **slice‑scoped** refresh to prevent thrash.                                                                     |

### E.18:5 - Solution - E.TGA graph model and relation disciplines
**Dominant Solution moves.** In ordinary E.TGA use, keep five moves primary: name one graph object; distinguish the graph from a flow valuation; place gates only on crossings or the `U.WorkEnactment` boundary; preserve normalize-before-compare and set-return discipline; and keep cycles under budget plus `PathSlice` refresh. S12 viewpoint mapping remains conditional support when engineering or publication viewpoint mapping is live.

#### E.18:5.1 - S1 - Graph object (conceptual)

Define a **typed, editioned, directed multigraph**
`TransductionGraph := (V, E, τ_V, τ_E, Γ_time, Bridge, CL, TransportRegistry^Φ)`
with:

* **Vertices `V`:** instances of `U.Morphism` (open world). Common specialisations **include but are not limited to** the P2W illustrative set: `U.FormalSubstrate`, `U.PrincipleFrame`, `U.Mechanism`, `U.ContextNormalization (UNM)`, `U.SelectionAndTuning`, `U.WorkPlanning`, `U.Work`, `U.EvaluatingAndRefreshing`. This list is **illustrative**, not exhaustive—the graph **does not depend** on this particular set.
* **Edges `E`:** a **single edge kind `U.Transfer`** (typed) carrying carrier refs and token refs; all **plane/Context/edition** changes occur **only at nodes via `OperationalGate(profile)`** with **Bridge + CL** annotations; penalties **→ R only**. Transport conversions pin **Φ‑policies** and editions.
* **Scopes:** `Γ_time` (budgets, horizons), `PublicationScope` for faces (E.17), and **slice ids** for refresh (G.11).

 **CtxState (PS‑projection; closed slots):** `CtxState = ⟨L, P, E⃗, D⟩` is the **projection of E.17 Publication Scope**.
 **Slot definitions (normative):**
  • `L := Locus` — an element of a partially ordered **ContextSlice** poset; addresses *where* claims apply (disciplinary / organizational / holonic slice).
  • `P := ReferencePlane` — the reference plane/units registry id; **no plane/unit declarations or translations** occur in CV; crossings remain gated (A.21).
  • `E⃗ := Edition vector` — a **partial map** `edition_key ↦ EditionId` over named families `{CG‑Spec, ComparatorSet, UNM.TransportRegistryΦ}` and optional `{DescriptorMapRef, DistanceDefRef, CharacteristicSpaceRef}` when cited.
  • `D := DesignRunTag` — `design(T^D)` or `run(T^R)`, used by **LaunchGate** and acceptance/telemetry duties.
 **Invariants.** Raw `U.Transfer` preserves `CtxState` (`⟨L,P,E⃗,D⟩`): it does **not** write/update any CtxState slot; any CtxState write/update (or entry to `U.WorkEnactment`) occurs at `OperationalGate(profile)`.
 **Extension discipline.** A conforming use registers any extra slot beyond ⟨L,P,E⃗,D⟩ in the **E.17/LEX “CtxState Extension Registry”** with slot‑id, intent, partial‑order law (neutral/absorbing), and SquareLaw compatibility; unregistered extensions are non‑conformant.
 **Data-shape location.** E.TGA names the graph and valuation obligations for `PathId`, `PathSliceId`, Γ-pins, and lineage: flow is a valuation over `U.Transfer`, raw transfer preserves `CtxState`, and path or slice evidence is carried through this pattern plus `A.20`, with `G.6` or `G.11` where evidence-path visibility or refresh wiring is live. Use these current loci for path and slice currentness.


 * **Kinds:** `U.Transduction(kind∈{Signature, Mechanism, Work, Check, StructuralReinterpretation})`.
  **Exact identification (no TGA‑local taxonomy):**
  — `Signature` **≡** **A.6.0** `U.Signature` (universal, law‑governed declaration).
  — `Mechanism` **≡** **A.6.1** `U.Mechanism` (law‑governed application over a SubjectKind/BaseType).
  — `Work` **≡** **A.15** `U.WorkEnactment` (world‑contact; `FinalizeLaunchValues` only here).
  — `Check` **≡** `OperationalGate(profile)` (universal **gate**; `A.21` governs gate profile, check aggregation, decision, and publication minima).
  — `StructuralReinterpretation` **≡** the E.TGA placement of **A.6.4** `U.EpistemicRetargeting` as a graph node; it is not a new retargeting kind. **All retargeting semantics** (slot-scoped discipline, `DescribedEntitySlot`/`GroundingHolonSlot` behaviour, invariants, Bridges, witnesses) come from **C.2.1** and **A.6.2–A.6.5**; E.TGA does **not** introduce a TGA-local variant of retargeting.

  `OperationalGate ≔ U.Transduction(kind=Check)` with DecisionLog aggregation.
  The only extra discipline E.TGA adds for `StructuralReinterpretation` is **graph-local**: CtxState and GateCrossing behaviour are governed by **CC-TGA-06-EX** and **CC-TGA-11** (projection-preserving w.r.t. `⟨L,P,E⃗,D⟩`, PathSlice-local, and "no plane/unit change without a gate"). `StructuralReinterpretation` is not a gate exception; it carries a recorded witness condition for saying no GateCrossing occurred. If any `CtxState` slot, plane/unit, edition, or design/run boundary changes, the case is a GateCrossing again.

> **MVPK integration (import).** Every vertex with an external publication face is published via **MVPK** faces (`PlainView`, `TechCard`, `AssuranceLane`, `InteropCard`) under a declared **PublicationScope** (E.17). E.TGA **reuses** MVPK’s publication laws (pins, declared-order discipline, “no new numeric claims / no I/O re‑listing”) and only adds graph-scope constraints in S3 and **CC‑TGA‑09/10**; it does **not** define a second, local publication semantics.

**GateCrossing (normative)**
**Definition.** A **GateCrossing** is the typed transition at a node that writes/updates any of:
  (i) `U.BoundedContext` (**Context**), (ii) **ReferencePlane**, (iii) any member of the **Edition vector** `E⃗` (e.g., `CG‑Spec`, `ComparatorSet`, `UNM.TransportRegistryΦ`, `DescriptorMapRef`, `DistanceDefRef`, `CharacteristicSpaceRef`), (iv) **DesignRunTag** (`T^D↔T^R`), or (v) **Kind/describedEntity** (only under `StructuralReinterpretation` subject to **CC‑TGA‑06‑EX**).
**Invariants.** Raw `U.Transfer` preserves `CtxState`; a GateCrossing occurs at exactly one `OperationalGate(profile)` (SquareLaw applies).
**Required pins (minimum).** `BridgeCard + UTS row`; `CL` for scope bridges; `CL^plane` for plane crossings; `CL^k` with `bridgeChannel=Kind` for kind transitions; `PublicationScopeId`; `PathSliceId`; Γ‑pins on compare/launch faces.
**Canonical reference.** `CrossingRef := ⟨GateId, channel, from, to, UTS.RowId, PathSliceId⟩`. Any DecisionLog entry whose rationale depends on a crossing cites `CrossingRef`.
**CrossingBundle (normative)**
**Definition.** A **CrossingBundle** is the published bundle that makes a GateCrossing **auditable and replayable** (crossing visibility). It includes:
* the canonical **`CrossingRef`**;
* the matching **UTS row** (**`UTS.RowId`**) for the crossing;
* the required pins **`PublicationScopeId`** and **`PathSliceId`**;
* where a Bridge is involved: the **BridgeCard** (F.9) and its disclosed fields (`BridgeId`, `bridgeChannel`, **CL** and loss notes; **`CL^k`** when `bridgeChannel=Kind`; **`ReferencePlane(src,tgt)`**);
* where planes differ: **`CL^plane`** and the active **`Φ_plane`** as a **`PolicyIdRef`** (policy-id + resolvable refs; F.8:8.1);
* the active penalty policy identifiers **`Φ(CL)`** (and **`Ψ(CL^k)`** if used) as **`PolicyIdRef`** bundles (policy-id + `PolicySpecRef` + `MintDecisionRef?`; F.8:8.1);
* any additional pins mandated by the active **GateProfile** / GateChecks (A.21) for this crossing.

**CrossingBundle rule.** Every **GateCrossing publishes its CrossingBundle**. Missing or non-conformant CrossingBundle is a **blocking** defect for downstream uses that rely on the crossing (selectors, acceptance, audits). A local descriptive graph with no downstream crossing consumption is not over-penalized by this CrossingBundle rule.

**Term separation.** **Transfer** denotes the sole edge kind `U.Transfer` (graph edges). **Transport** denotes Φ‑governed conversion **policies/registries** (**`TransportRegistry^Φ`** under UNM). Wording “reuse via Transport” refers to registries/policies, not to an additional graph edge.

#### E.18:5.2 - S2 - Flows as valuations (paths + state + guards)
* A **Flow** is a **valuation** `ν` over `U.Transfer` edges and cut-sets, paired with an **admissible path** `p = v0 -> ... -> vk`. The valuation assigns tokens or states under `CtxState` and records publication events under a declared `PublicationScopeId`. The concrete pins and identifiers (`PathId`, `PathSliceId`, Γ_time on compare and launch faces) are governed here as path and slice publication obligations and by `A.20` when CV witnesses are live; use `G.6` for evidence-path visibility and `G.11` for refresh wiring. This reflects the “graph != flow” norm (flow = valuation), with gates placed exactly on GateCrossings.
* **Admissible path (definition).** A path `p` is **admissible** iff:
  (a) node/edge types match the declared `τ_V, τ_E`;
  (b) any write/update to any member of `⟨L,P,E⃗,D⟩` (or kind‑retargeting under `StructuralReinterpretation`) appears at **exactly one** `OperationalGate(profile)`;
  (c) each GateCrossing on `p` has a **SquareLaw witness** (CC‑TGA‑23) and, where applicable, a **SquareLaw‑retargeting witness** (CC‑TGA‑06‑EX);
  (d) no hidden crossings occur across raw transfers;
  (e) Γ‑pins are present on compare/launch faces;
  (f) `T^D↔T^R` occurs **only** at `LaunchGate`.

* `U.Transfer` preserves `CtxState` (`⟨L,P,E⃗,D⟩`) and carries **Assurance‑operations** only (see S3b); any crossing of locus/plane/editions or `T^D↔T^R` is placed at `OperationalGate(profile)`.
* A **PathSlice** is a **slice‑scoped execution window** used for refresh/telemetry; faces pin `PathSliceId`; **re‑emission** happens when any pinned edition changes or `SliceRefresh` is triggered by sentinel rules.

> **Consequences.** The P2W reference flow is simply one `p` in `TransductionGraph`. Other domains (supply chain, water network, NN functional) instantiate different `p` on the **same architecture**.
>
**Why "flow = valuation" doesn't kill the "something is flowing" intuition**
There are two complementary perspectives:
* **Lagrangian (intuitive):** "water particles" run through pipes; you "track" tokens.
* **Eulerian (architectural):** you define a **function on edges** ("how much/what passes through each edge under a given regime"), with gate laws. E.TGA deliberately fixes the **Eulerian semantics of flow** at the architectural scope: "flow (= valuation) + publication log", while the dynamics of "movement" show up as **re-valuation** over a **PathSlice** (the execution/republishing window) under gate rules and the SquareLaw. This yields comparability, reproducibility, and slice-local refresh.

#### E.18:5.3 - S3 - Publication discipline (faces)

E.TGA **imports E.17** wholesale **and associates MVPK faces with `PublicationScope` (USM)**.
**MVPK remains the normative source** for:
* the set of face kinds (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`),
* pin discipline and Publication Characteristics (PC),
* “no new numeric claims / no I/O re‑listing / no Γ‑semantics on faces”.

E.TGA **does not re‑specify** these laws; it only adds **graph-scope obligations** for faces emitted over transduction paths:

1. **Crossings on faces.** When a face participates in a GateCrossing (S1.b/S9), it cites `BridgeId + UTS row + CL` and publishes **Φ(CL)/Φ_plane RuleId**; **penalties remain in R‑lane**.
2. **Gate requirement on cited editions.** Any face that references editions of `CG-Spec`, `ComparatorSet`, or `UNM.TransportRegistryPhi` includes **`BridgeCard + UTS row`**; faces without this are treated as **non-consumable downstream**. Bridge and terminology-synchronization checks are received through `F.9`, `F.17`, `E.17`, and `E.18`; selection and comparator pressure stays with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, or `G.11` when live.
3. **ComparatorSet & set returns (graph‑scope).** Any `ComparatorSet` and `SetSemanticsRef` used along a transduction path carries **edition identifiers**; flows **re‑emit** faces on edition change; faces with comparison **return sets and declared partial orders** (no hidden scalarization), reusing MVPK’s declared-order discipline.
4. **Γ_time on compare and launch faces.** All compare and launch faces on E.TGA paths pin `Γ_time`; implicit *latest* is not admissible. `A.21` carries current GateProfile binding and minimum profile semantics; E.TGA paths include the pin. **CHR avoids acceptance thresholds** (*NoThresholdsInCHR*); thresholding and launches are carried by `A.21`, Part G, and `U.Work` where live. Unknowns remain tri-state (`pass|degrade|abstain`) and fold per the active GateProfile (`A.21`).

> **Reminder.** MVPK already bans “signature” on faces, I/O re‑listing, arithmetic on faces, and unpinned numeric content (E.17 §5.4–5.5). E.TGA **does not weaken or override** those rules; it only constrains how they are used along transduction paths.

**Lean publish‑mode (AssuranceLane‑Lite).** Lean changes **publication faces only** (`PlainView`/`AssuranceLane` minimal), not checks; publication shows `GateProfile`, `GateCheckRef[]`, and `DecisionLogRef`; the underlying GateChecks list remains unchanged.

**Decision stability & idempotency (gate-local).** Gate decisions are stable under a declared equivalence relation over the pins used by `A.21`; the witness is recorded as `DecisionLog` or `EquivalenceWitnessRef`, with `G.6` or `G.11` used when evidence-path visibility or refresh implications are live. E.TGA **does not** prescribe storage formats, key shapes, or hashing schemes.

**KindBridge admissibility (publication).**
Treat a step as a **describedEntity/kind** transition (including `StructuralReinterpretation` under CC‑TGA‑06‑EX) **iff** the **UTS row**:
  — satisfies the minimal bridge and terminology-synchronization obligations of `F.9`, `F.17`, `E.17`, and `E.18` where live (identity, `ReferencePlane`, `CL/CL^plane`, edition pins for `CG-Spec`, `ComparatorSet`, `UNM.TransportRegistryPhi`, `ComparatorSetRef`, `BridgeId`, and `Phi-RuleIds`), and
  — is additionally marked as a **KindBridge** per C.3 (`bridgeChannel=Kind`, `CL^k`, mapping or signature‑translation, order‑preservation claims, loss notes, definedness area, determinism).
Otherwise this KindBridge explanation does not apply (the step falls back to a gated crossing). When the crossing is gate-mediated, `CrossingRef` is cited and linked from the `DecisionLog`.

#### E.18:5.4 - S4 - Assurance‑operations on `U.Transfer` (counterfactual admissibility)
On `U.Transfer` edges, an operation is interpreted as a **declarative assurance‑operation** **iff** it is one of
`ConstrainTo(rule)` - `CalibrateTo(calibrationReference)` - `CiteEvidence(anchor)` - `AttributeTo(provenanceReference)`; otherwise this explanation does not apply.
Under this interpretation, `CtxState⟨L,P,E⃗,D⟩` is preserved.
If a claimed assurance operation would change plane or units, the assurance-operations explanation does not apply and the step is handled as a gated crossing (`OperationalGate(profile)+Bridge+UTS`).

If Φ assigns penalties, they appear in the R‑lane; otherwise no penalties appear here.

#### E.18:5.5 - S5 - Comparability & aggregation (normalize‑then‑compare; counterfactual form)

The comparison explanation applies under the following admissibility conditions:

* If a path segment intends to compare/aggregate, it is admissible as a comparison **only when** UNM precedes it; UNM is **method‑independent**, publishes **TransportRegistry^Φ** and **CG‑Spec** anchors, and faces cite those editions; otherwise this comparison explanation does not apply.
* If the comparator defines a **declared partial order**, then returns are **sets/archives** (Pareto/Archive); if a **total order** is declared, it is the one provided by the comparator; otherwise set semantics apply and covert scalarization is out of scope here.
* If a claim is **ordinal‑only**, then only comparison results are published; arithmetic transforms (e.g., means/z‑scores) are out of scope of this explanation and belong to declared comparators or downstream policy.

**Edition-aware set/archive publication records (e.g., QD archives) pin `DescriptorMapRef.edition`, `DistanceDefRef.edition`, and `CharacteristicSpaceRef.edition` when applicable; refresh is slice-local. Comparator, archive, and refresh checks are received through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` when live.**

#### E.18:5.6 - S6 - Cycle discipline (Selection ↔ Planning)

* The architecture centers the loop between `U.SelectionAndTuning` and `U.WorkPlanning`.
* The loop operates under a local **budget / max_iter** in `Γ_time`; at expiry, the selector emits the **current `CandidateSet`** and **`MethodTuning`** with a **partial‑optimality** flag; further improvement rolls into the **next `PathSlice`**.
* **UNM occurs before the loop**; if measurements are missing/stale, UNM emits a **FreshnessRequest** which is **planned** in `U.WorkPlanning` and **executed** in `U.Work`. Transfers, units, and calibrations are published as `CalibrateTo(calibrationReference)` and pinned to `TransportRegistry^Φ` (**R‑channel only** for penalties).
* **WorkEnactment is the only site for launch‑value slot filling** (`FinalizeLaunchValues / FinalizeLaunchValuesOnlyInWork`).
> **Refresh orchestration.** Telemetry from `U.WorkEnactment` and publications are **slice‑scoped**, editions re‑pinned, faces **re‑emitted**.

#### E.18:5.7 - S7 - Selector semantics (G.5) & parity harness (G.9)
E.TGA checks that set-return, archive preservation, and comparator refs remain visible along the path. It does not define selector, archive, dominance, or comparator semantics; those remain with `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` where live.

* **Selectors return sets.** Default **DominanceRegime** is `ParetoOnly`; **IlluminationSummary** (telemetry summary) and any coverage/regret telemetry quantities are **report-only telemetry** (reported), excluded from dominance **unless** a CAL policy promotes them as declared dominance inputs (policy-id in SCR).

If `PortfolioMode=Archive`, a **QD archive** can be returned; when generation is in scope, pairs `{environment, method}` are managed under declared **EnvironmentValidityRegion** and **TransferRulesRef**; parity records and `PathSliceId` are pinned on publication. Comparator semantics and archive pinning are received through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` when live.

#### E.18:5.8 - S8 - Guard aggregation assignment and handling (USM §1.2)
* **USM.CompareGuard**/**USM.LaunchGuard** **publish `GuardOwnerGateId`**. Guard failures are **events** aggregated by the declared gate (not GateChecks).
* **Aggregation-assignment rules:** (i) `USM.LaunchGuard.aggregationGate = LaunchGateId(U.WorkEnactment)`; (ii) inside a Subflow, `USM.CompareGuard.aggregationGate = OperationalGate(InSentinel)`; Join-nodes cannot be assigned as guard-pin aggregation gates.

**GateProfile data shape (cross-reference).** `A.21` carries the current GateProfile binding and minimum profile semantics. E.TGA names the structure only where graph crossings need it; fuller profile-matrix support is not a separate current authority unless a current governing pattern explicitly admits it.

**Bridge-aware guards (cross-reference).** USM guards apply bridge-translation semantics (`translate(Bridge, Scope)`) with CL penalties in R-lane; guard vocabulary is received through **A.2.6**, while gate aggregation remains in `A.21`.

**Error/timeout/unknown (profile-bound).** GateCheck errors/timeouts fold to **`degrade`** under `Lean\|Core` and to **`block`** under `SafetyCritical\|RegulatedX`; `unknown` follows the GateCheck's intensional rule (safety-default: `degrade`). The `A.21` DecisionLog record and equivalence witness carry decision stability; E.TGA does not define storage or key structures.

#### E.18:5.9 - S9 - Transport & crossings
* Cross‑Context or cross‑plane edges appear as **GateCrossings** that include a **Bridge** with **CL** policy; **Φ(CL)/Φ_plane** are published; penalties appear **in R only**; **Scope membership** (USM) is unchanged by crossings. **SquareLaw is checked within a single `DesignRunTag`; a `T^D↔T^R` change is modelled as a pair of coordinated gates with `DesignRunTagFrom/To` and the selected `A.15` work or publication locus for the live case.**
* When *describedEntity/kind* changes across a boundary, declare an explicit **KindBridge (`CL^k`)** in addition to plane/context CL; cross-context reuse of UNM uses `Transport`, with any `CL^plane` penalties published in **R-lane** only.

#### E.18:5.10 - S10 - Non‑mechanism boundary

* Publication is a **typed projection**, not execution. Any build/render/upload is **Work on carriers**; faces do **not** carry Γ-semantics.

#### E.18:5.11 - S11 - Coordination thread (optional)
Coordination wording may be published as **LexicalView** labels over `U.TransductionFlow__P2W`; it is orientation-only unless a bridge, crossing, work, or gate relation is explicitly live. It adds no current graph node kind, checks, or mechanisms. Crossings with production flow use **Bridge+UTS** and the current bridge or crossing loci.

#### E.18:5.12 - S12 - Viewpoint families → E.TGA constructs (neutral, holonic)
**S12 status.** S12 is secondary support for a live viewpoint-family mapping claim. It is not the ordinary E.TGA core for naming a graph object, flow valuation, path slice, or crossing.

E.TGA does not mint new viewpoint or view kinds. It **imports** the generic multi‑view machinery of E.17.0 `U.MultiViewDescribing`, bundles from E.17.1, and the TEVB engineering bundle from E.17.2. S12 only describes how these existing `U.Viewpoint` / `U.ViewpointBundle` ids are *used* in transduction graphs and in `UTS.ViewpointMap`; intent/concern semantics are governed by E.17.0–E.17.2.

**Two-part use of TEVB and MVPK (ISO 42010 summary, no local re‑definition).**

* **Engineering viewpoints.** For engineering holons, E.TGA assumes a TEVB bundle with `ViewFamilyId = VF.TEVB.ENG`. `EngineeringVPId` is one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`, and TEVB is the normative source for their semantics. E.TGA does not refine these viewpoints.
* **Publication viewpoints.** Publication viewpoints come from MVPK (E.17); `PublicationVPId` is a `MVPK.ViewpointId` that governs faces under a `PublicationScope`.
* **Architecture relation.** E.TGA can describe a flow/transduction-structure view of an `ArchitectureOf@Context` claim when `DescriptionContext`, described holon, bounded context, and structure kind are explicit. It does not define architecture itself, and a TGA graph is not the functional architecture by default. Use `C.30`, `C.30.ASV`, and `C.30.TGA-FLOW-REL` when the graph is used as architecture-description support. Crossings and penalties follow E.TGA gating rules (S9; CC-TGA-11/23) but do not change viewpoint semantics.
* **Separation of roles.** `VP.*` from TEVB are **EngineeringVPId** values only; they are not publication faces. `PublicationVPId` values live in MVPK. The mapping between them is entirely via ISO‑style correspondences and the `UTS.ViewpointMap`; E.TGA does not define a second notion of viewpoint.

**Entities‑of‑interest (summary).**

* **EoI‑ENG.** The engineering entity described by TEVB/E.TGA is a holon (`U.System` or `U.Episteme`) per TEVB’s `EoIClassSpec`. E.TGA does not broaden or narrow this set.
* **EoI‑PUB.** MVPK can treat the *architecture description* itself as an entity‑of‑interest; publication viewpoints for that AD are defined in MVPK, not here. E.TGA only checks that such faces honour MVPK discipline and E.TGA’s crossing rules.

**Naming rules (aligned with E.17.0/E.17.1/E.17.2).**
* `ViewFamilyId` is the `U.ViewpointBundle.viewFamilyId` (e.g. `VF.TEVB.ENG` for TEVB); its lexical and ontological discipline is governed by E.17.1.
* `EngineeringVPId : ViewpointId` is always a `U.ViewpointId` drawn from some bundle (for TEVB, one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`). E.TGA never defines new `VP.*` ids.
* `PublicationVPId : ViewpointId` is a `MVPK.ViewpointId` defined in E.17; TEVB viewpoints are **never** reused as publication viewpoints (per TEVB guard and MVPK).
* The unqualified field name `ViewpointId` is not valid in S12 rows. Use `EngineeringVPId` and/or `PublicationVPId` explicitly; any imported row with an unqualified `ViewpointId` is normalized to `PublicationVPId` before the row is used.

**Terminology guards (no local semantics).**
* Within S12, “viewpoint”, “view” and “correspondence” have exactly the meanings given in E.17.0; “publication face” means an MVPK face (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) under some `PublicationVPId`.
* Faces are **carriers for views**: a face is part of a view only when linked via an ISO‑style `CorrespondenceRef` to an engineering `U.View` under some `EngineeringVPId`; S12 does not add extra conditions beyond E.17.0/E.17.2.
* Labels such as “Functional view”, “Procedural view”, “Role‑Enactor view”, “Module‑Interface view” in this section are lexical aliases for TEVB viewpoints; they are not interpreted as extra viewpoint kinds or as publication-face types.

**Purpose.** Provide a neutral (F.18) mapping from TEVB engineering viewpoint families - bundle `VF.TEVB.ENG` with `VP.Functional / VP.Procedural / VP.RoleEnactor / VP.ModuleInterface` - to E.TGA constructs so that the same holon can be described through functional, procedural, role-enactor, or module-interface viewpoints while the E.TGA construct scope remains explicit. S12 does not introduce new `U.Viewpoint` or `U.View` kinds, and it does not claim that all such views share one underlying graph unless the graph, described entity, and correspondence refs are declared.

**Holon target.** The mapping applies to any holon, with the constraint that only `U.System` enacts `U.Work` (A.3/A.15). Supervisory and structural hierarchies remain distinct (B.2.5).

**Viewpoint family → primary E.TGA constructs (TEVB‑aligned)**
*All four families referenced below are TEVB engineering viewpoints; the “what …” clauses are interpretive glosses for how they *use* E.TGA constructs. Formal intent/concerns/allowed episteme kinds remain in TEVB (E.17.2).*
1) **Function‑Oriented View (`EngineeringVPId = VP.Functional`, capability‑flow)** — “what transformation is achieved under roles”
    * **Flow substrate:** `U.TransductionFlow__P2W` through nodes `U.FormalSubstrate → U.PrincipleFrame → U.Mechanism → U.ContextNormalization (UNM) → U.SelectionAndTuning ↔ U.WorkPlanning → U.Work → U.EvaluatingAndRefreshing`.
    * **Publication:** MVPK publication faces per E.17; comparable claims pin to `CG‑Spec/ComparatorSet` editions; crossings are published through `Bridge+UTS` and `CL/CL^plane` (penalties → **R‑lane** only).
    * **Checks:** A.20 (CV) inside transformations; A.21 (GateFit) at gates; comparator, set-return, and No-Hidden-Scalarization discipline is carried through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` when live.
    *  **Holonic note:** `U.Episteme` does not *act*; it is used by systems acting on carriers; `U.Work` appears only for `U.System`.
2) **Procedure‑Oriented View (`EngineeringVPId = VP.Procedural`, step/time storyboard)** — “what steps occur and when”
    * **FPF constructs:** `U.WorkPlan` (A.15.2) for intent/schedule; `U.WorkEnactment` for enactment.
    * **Boundary:** entry into `U.WorkEnactment` is via `OperationalGate(profile)` with `USM.LaunchGuard`; `DesignRunTag` separates design time from run time; `DesignRunTagFrom/To` appear only at gates.
    * **Holonic note:** Applies to any `U.System` scope (single holon or a supervised sub‑holon cluster); supervisory structure is handled by roles rather than structural mereology (B.2.5).
3) **Role‑Enactor / Device‑Structure View (`EngineeringVPId = VP.RoleEnactor`)** — “what carrier/ports/constraints exist; who typically enacts it”
    * **FPF constructs:** Module *interfaces* are `Signature` nodes; module realizations are `Mechanism` nodes; inter‑module dependencies traverse `U.Transfer`, with gates on crossings.

    * **Publication:** MVPK faces are **typed projections**, not `U.Work` records or execution carriers; faces add **no new numeric claims** (E.17). Constraints and compatibility appear as CV checks (A.20).
    * **Holonic note:** Structural mereology (part/whole of the carrier) is modeled in Part A; E.TGA ties interface/exposure semantics to morphisms and gates.
    * **Device‑View reading (Transduction↔Transductor).** The same capability‑flow can be read as a **device** that performs the transduction (**transductor**) without changing the declared E.TGA graph object: model with `Signature` + `Mechanism` only; do **not** introduce extra edge kinds. If describedEntity retargets (function↔element), use `StructuralReinterpretation` with a **`KindBridge (CL^k)`** on **UTS** and a **SquareLaw‑Retargeting witness**; preserve `⟨L,P,E⃗,D⟩` and treat it as a non‑crossing (**CC‑TGA‑06‑EX**; witness shape §4.7).
    * **Role‑label guard.** `TypicalEnactorRoleName` is **pedagogical only** and is not used as a GateFit role; GateFit uses `U.Role` (A.21).
4) **Module‑Interface View (`EngineeringVPId = VP.ModuleInterface`, physical/logical module structure)** — “what modules exist and how they specify commitments and constraints across interfaces”
    * **FPF constructs:** Module *interfaces* are `Signature` nodes; module realizations are `Mechanism` nodes; inter‑module dependencies traverse `U.Transfer`, with gates on crossings.
    * **describedEntity note:** Functional-view-to-element-structure reinterpretation follows the **Device‑View reading** rule above (Role‑Enactor family) and **CC‑TGA‑06‑EX**; see **§4.7** for the retargeting witness shape and CV witness linkage.
    * **Holonic note:** The same module can appear as a holon in multiple views; supervisory loops (B.2.5) remain orthogonal to structural composition.
This is an expandable list of viewpoint families; TGA is intentionally viewpoint‑neutral. Additional engineering bundles beyond TEVB (safety, mission, information, …) are introduced as separate `U.ViewpointBundle` species via E.17.1/E.17.2; S12 does not define them.

**Alias families for transduction species (LEX‑only).**
*Scope.* A pattern or domain profile can declare `AliasesInViewFamilies[]` for `U.Transduction` species so practitioners can recognise familiar engineering view families. All semantics come from the referenced bundles (typically TEVB) and MVPK; aliases are purely lexical.

*Norms.*
1. Each `U.Transduction` species can publish `AliasesInViewFamilies[]` — an open list of records
   `{ ViewFamilyId, EngineeringVPId?, Alias : TechASCII }`.
   * If `ViewFamilyId = VF.TEVB.ENG`, then `EngineeringVPId` is one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` (TEVB; CC‑TEVB‑1/6).
   * Other `ViewFamilyId` values denote `U.ViewpointBundle` instances defined elsewhere (e.g. safety/assurance/information bundles), not ad‑hoc local families.
2. Aliases are LEX‑only: **no arithmetic, no new claims, no check participation, no `CtxState` slot writes/updates (incl. `DesignRunTag`)**. They do not create MVPK faces.
3. Aliases are not used as `PublicationVPId`; publication viewpoints remain in MVPK.
4. Twin registers are allowed (Tech/Plain) per E.10; naming follows F.18 local‑first discipline.
5. Do not name transductions by operands or output states (operation != operand or output state).

6. `TypicalEnactorRoleName` can be added for pedagogy; it is not used as a GateFit role (GateFit uses `U.Role` only).
7. Morphology: ASCII TitleCase; conjunctions via `And`; for composite actions use `XingAndYing` (or `XAndYing` if grammar calls for it).
8. The P2W illustrative species row (`U.FormalSubstrate` … `U.EvaluatingAndRefreshing` with functional/procedural aliases and `TypicalEnactorRoleName`) is **informative** and does not change kind or viewpoint semantics.

**Conditional deliverable — `UTS.ViewpointMap` (TEVB-aligned when live).**
Publish a UTS block named `ViewpointMap` only when an engineering or publication viewpoint-family mapping claim is made or consumed. Ordinary E.TGA use does not require `UTS.ViewpointMap` when the live question is only the graph object, flow valuation, path slice, or crossing.

*Minimum row schema (per row, when `ViewpointMap` is live).*
* `ViewFamilyId` — `U.ViewpointBundle.viewFamilyId` (e.g. `VF.TEVB.ENG` for TEVB, or another bundle id).
* `EngineeringVPId : ViewpointId` — a viewpoint from that bundle (for TEVB, one of `{VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`).
* `PublicationVPId : ViewpointId?` — MVPK publication viewpoint id that governs faces implementing this engineering view (optional if not publishing).
* `TargetHolon ∈ {U.System, U.Episteme}` *(extended species can add `{U.PromiseContent|U.MethodFamily}`; if `TargetHolon ≠ U.System`, no `U.Work` enactment appears).*
* `PrimaryTGAConstructs` — nodes/edges/gates actually used for this `(ViewFamilyId, EngineeringVPId, TargetHolon)` (typically one of the four families above).
* `Crossings{BridgeId, CL/CL^plane?}` — crossings involved; penalties appear in R-lane only.
* `EditionPins{...}` whenever comparable claims appear (bind to CG-Spec/ComparatorSet editions; any face citing editions includes `BridgeCard + UTS` row per MVPK/UNM).
* `SenseCells[]` (at least two per row), each citing Context name + edition (F.17/E.10 discipline; UTS-wide coverage rules still apply).
* *(REQUIRED when publishing)* `CorrespondenceRef[]` — ISO 42010 correspondences linking emitted faces to the engineering view(s) they implement; can cross architecture descriptions.
* *Optional support* `ConcernsCovered[]` — ISO 42010 stakeholder concerns addressed by this row via GateProfiles/check catalogues.

**Conformance (S12-scoped, only when `ViewpointMap` is live).**
(i) `UTS.ViewpointMap` exists when a viewpoint-family mapping claim is made or consumed.
(ii) For each holon that claims TEVB alignment, there are at least four rows whose `{ViewFamilyId, EngineeringVPId}` cover `{VF.TEVB.ENG × {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}}` (per CC-TEVB-1/6).
(iii) Rows that carry edition identifiers also include `BridgeCard + UTS` rows through `F.9`, `F.17`, `E.17`, and `E.18`; edition-bearing faces that lack such rows are not admissible for downstream consumption.
(iv) Each row has at least two `SenseCells` and the sheet meets global UTS coverage rules.
(v) Any `TargetHolon = U.System` that reaches `U.Work` shows `LaunchGate` with `DesignRunTag` consistency.
(vi) Crossings referenced in `ViewpointMap` follow CC-TGA-11; comparability along the mapped paths follows CC-TGA-10.
(vii) Rows do not use an unqualified `ViewpointId`; they use `EngineeringVPId` and/or `PublicationVPId` explicitly.
(viii) When faces are published, `CorrespondenceRef[]` is present and resolvable to `U.Viewpoint` ids.
(ix) Additional bundles (e.g. assurance, information, mission) can appear as extra `ViewFamilyId` values but are declared as `U.ViewpointBundle` species; they do not extend `VF.TEVB.ENG`.

### E.18:6 - Archetypal Grounding (Tell–Show–Show; concise)

*Tell (P2W reference path).* A first-principles-to-work path is one path through the graph, not the graph itself: substrate, principle frame, mechanism, normalization, selection, planning, work enactment, and refresh become nodes linked by one `U.Transfer` edge kind, with crossings pinned where context, plane, edition, or design/run state changes.

*Show-A (Supply chain).* Nodes: procurement -> inbound QC (UNM) -> selection (supplier set; declared order) <-> planning (lotting/schedule; budget) -> execution (receipts; **WorkEnactment enacts (world-contact)**) -> refresh (quality telemetry; re-emit faces). Crossings: vendor Context via **Bridge/CL**; penalties appear **in R only**; comparators pinned to CG-Spec edition.

*Show-B (Neural-net functional).* Nodes: formal substrate (typed tensor ops) -> mechanism (combinator algebra) -> UNM (dataset normalization; **TransportRegistry^Phi**) -> selection (architecture/hyperparam set; Pareto set over accuracy@ratio and FLOPs@ratio) <-> planning (compute budget horizon) -> Work (training runs; Delta anchored) -> refresh (parity inserts; slice-scoped). Faces pin **DescriptorMapRef.edition** and **DistanceDefRef.edition** when QD telemetry values are shown; illumination remains **report-only telemetry** by default.

**Cross-pattern boundary slice (QD archive).** A QD selector emits an archive. `E.18` says: this is one `PathSlice` in one `TransductionGraph`; selection returns a set/archive, not a hidden scalar. `A.20` says: the archive insertion or update step has a live CV class, `CV.Status`, and witness or refusal; no acceptance is inferred. `A.21` says: a comparability gate or `LaunchGate` can publish a `GateDecision` only when that gate relation is live and consumes the relevant CV result. `E.20` says: if a new selector mechanism intension is introduced, the mechanism-governing definition is the locus for the meaning while suites and wiring only cite or bind it. These are four governed objects, not one prescribed work order.

> *Post-2015 SoTA echoes (illustrative):* **TAMP and MPC**, **MAP-Elites / QD (incl. CMA-ME)**, **refinement-typed stacks**, **profunctor optics**. Worked examples and Tell-Show-Show vignettes for P2W, comparator/archive, and refresh specializations stay outside this graph-architecture core unless a current pattern explicitly selects them.

### E.18:7 - Conformance — **Unified checklist (normative)**

**Conformance use.** This checklist is evidence for the graph/flow/crossing action guidance already stated in the Solution. It is not the first entry text for ordinary use and not a full audit regime by default; an item is applied only when its corresponding graph, crossing, publication, gate, refresh, or assurance move is live. Before applying any item, name the Solution move it tests; if no such practitioner move is live, treat the item as support-only or not applicable rather than expanding the applied assurance or conformance material.

**Conformance groups.** Ordinary graph/path use starts with graph object, single edge kind, node typing, `CtxState` preservation, and flow valuation. Crossing/launch items apply only when a GateCrossing, `LaunchGate`, `StructuralReinterpretation`, or work-boundary crossing is live. Publication/assurance items apply only when MVPK faces, edition pins, evidence carriers, decision logs, or replay are live. Extension/change items apply only when node-kind scope, budget/refresh behavior, or UNM/comparator editions are being changed or consumed downstream.

| ID | Requirement | Practical test |
|----|-------------|----------------|
| **CC‑TGA‑01 — Single edge kind** | The graph uses exactly one edge kind `U.Transfer`; all plane/Context/edition transitions occur only at nodes via `OperationalGate(profile)`. | Model lint finds no auxiliary edge kinds for unit/plane changes; crossings sit on declared gates. |
| **CC-TGA-02 — Nodes are morphisms** | Nodes are intensional `U.Transduction(kind in {Signature, Mechanism, Work, Check, StructuralReinterpretation})`. This enumeration is a **minimal kind baseline**. **Domain-specific species are open-world** and non-exhaustive; they bind to one of these kinds. Adding a **new kind** uses an explicit E.TGA update. `StructuralReinterpretation` nodes are **projection-preserving** (no mutation of `⟨L,P,E⃗,D⟩`) and carry CV/GF obligations per `A.20`, `A.21`, `A.6.4`, and E.TGA. The enumeration is **not** a TGA-local taxonomy: `Signature -> A.6.0`, `Mechanism -> A.6.1`, `Work -> A.15`, `Check -> A.21 OperationalGate`, and `StructuralReinterpretation -> A.6.4 plus E.TGA/A.20` where CV is live. | Type registry shows at least the listed kinds; additional species map to one of them; checks realized as `OperationalGate` (see CC-TGA-06-EX/11). **Lint:** registry/table exposes `{species -> {kind, KindDefinition}}`; missing or mismatched `KindDefinition` fails. |
| **CC‑TGA‑03 — Identity, composition, functorial faces** | Identities exist; path composition associative; publication is functorial: `Emit_s(t₂∘t₁)=Emit_s(t₂)∘Emit_s(t₁)`. | Pick two‑step path; MVPK faces commute (Square witness). |
| **CC‑TGA‑04 — Graph spec** | Spec declares `τ_V, τ_E`, `Γ_time`, Transport/Bridge registries. | Spec file shows typed registries and Γ policy. |
| **CC‑TGA‑05 — CtxState pins** | `CtxState=⟨L,P,E⃗,D⟩` is pinned on ports/tokens; raw `U.Transfer` does **not** write/update it. | Along a raw transfer, ⟨L,P,E⃗,D⟩ is preserved. |
| **CC‑TGA‑06 — Operational gates only** | Any write/update to any member of ⟨L,P,E⃗,D⟩ or entry into `U.WorkEnactment` is mediated by `OperationalGate(profile)` with aggregated `DecisionLog`. | Diff CtxState across edges; if any member differs, exactly one gate exists with DecisionLog. |
| **CC‑TGA‑06‑EX (strictly limited) — Projection retargeting without gate** | A node of kind **`StructuralReinterpretation`** retargets the **published projection** without invoking `OperationalGate` **only if all hold**: **(a)** `⟨L,P,E⃗,D⟩` is preserved; **(b)** any **describedEntity** change has a **KindBridge** (`CL^k`) entry on MVPK/**UTS**; **(c)** a **SquareLaw‑retargeting witness** is present (on UTS); **(d)** the operation is **PathSlice‑local** (`PathSliceId` pinned); **(e)** **no plane/unit change** occurs (plane/unit changes remain gated); **(f)** **CV.ReinterpretationEquivalence** (A.20) is `pass`; **(g)** **NoHiddenScalarization** — if the step concerns a comparable return shape, set/partial‑order semantics are preserved and comparators remain ref‑only (current comparator and set-return loci). | UTS row includes `bridgeChannel=Kind` and `CL^k`; SquareLaw‑retargeting witness present; PathSliceId pinned; CV status recorded; no scalarization detected. |
| **CC‑TGA‑07 — CV⇒GF activation predicate** | Until **aggregated `ConstraintValidity` = `pass`**, all **GateFit** checks return `abstain`. | Simulate CV failure ⇒ GateFit `abstain`. |
| **CC‑TGA‑08 — LaunchGate discipline (incl. pre‑run barrier)** | Each `U.WorkEnactment` has exactly one `LaunchGate` assigned as the aggregator for `USM.LaunchGuard`; **mandatory** checks: `FreshnessUpToDate`, `DesignRunTagConsistency`. If preceding step’s CV ≠ `pass`, LaunchGate decision is `block` (cause logged). | Aggregation assignment `GuardOwnerGateId = LaunchGateId(U.WorkEnactment)`; CV≠pass ⇒ `block` with log. |
| **CC‑TGA‑09 — MVPK publication discipline** | Every published node uses MVPK; faces carry `PublicationScopeId`, presence‑pins, **edition ids**, Γ pins; **no I/O duplication** or arithmetic; faces add no new numeric claims. | Cards show `PublicationScopeId`; pins present; no “signature”/math on faces. |
| **CC‑TGA‑10 — Normalize→Compare (CSLC)** | Any comparison cites **UNM/CG‑Spec** editions and **ComparatorSetRef**; ordinal claims are compare‑only; partial orders return sets; edition‑aware set/archive publication records (QD/archives) pin `{DescriptorMapRef, DistanceDefRef, CharacteristicSpaceRef?}.edition`; **any face citing editions includes `BridgeCard + UTS row`**. **NoHiddenScalarization — detection criteria:** (1) return shape is **set/poset**, not scalar; (2) `ComparatorSetRef` is present and edition‑pinned; (3) MVPK faces add **no new numeric claims**; (4) any summarisation is **order‑preserving & set‑valued**; otherwise conformance fails. | Faces show comparator pins; archive pins present; linter rejects edition cites without UTS; scalarisation checks pass. |
| **CC‑TGA‑11 — Crossings gated** | Cross-Context or cross-plane crossings publish **BridgeId + UTS + CL/CL^plane** and are mediated by `OperationalGate(profile)`; **Φ/Φ_plane penalties appear in R-lane only**; describedEntity change publishes **KindBridge (CL^k)**. **Exception (StructuralReinterpretation):** a **projection‑only** describedEntity retargeting is recorded **without** a gate **iff** **CC‑TGA‑06‑EX** holds; then the UTS row includes `bridgeChannel=Kind`, `CL^k`, and a **retargeting witness**; any plane/unit change falls back to a gated crossing; `PathSliceId` is pinned; UNM reuse cross‑context continues via `Transport`. | The crossing record shows Bridge/UTS/CL pins; penalty placement audited. |
| **CC‑TGA‑12 — Set‑returning selection** | `U.SelectionAndTuning` returns sets/archives under declared comparators (`ParetoOnly` by default) — no covert scalarization. | Selector output is a set/archive; policy id present if escalated. |
| **CC‑TGA‑13 — Budgeted Selection↔Planning loop** | The loop declares **budget / max_iter**; on expiry selector publishes partial‑optimal set + `MethodTuning`; next **PathSlice** scheduled. | Logs show budget stop and slice rollover. |
| **CC‑TGA‑14 — UNM before loop and FreshnessTicket state change** | UNM runs before selection; stale/missing inputs produce **FreshnessTicket/FreshnessRequest** planned in `WorkPlanning` and executed in `WorkEnactment`; calibrations appear as `CalibrateTo(calibrationReference)` with Φ pins. | Ticket state machine Issued→Planned→Executed→Closed; calibrations pinned. |
| **CC‑TGA‑15 — FinalizeLaunchValues only in WorkEnactment** | Only `U.WorkEnactment` performs `FinalizeLaunchValues` and fills launch‑value slots. | Any earlier attempt blocks at LaunchGate; a `FinalizeLaunchValues` witness is present in Work. |
| **CC‑TGA‑16 — Guard aggregation assignment & semantics** | `USM.CompareGuard`/`USM.LaunchGuard` publish the gate assigned to aggregate guard failures; guards are **events**, not GateChecks; failures are aggregated by that gate per profile. | Guard pins show the assigned gate; GuardFail recorded in that gate's DecisionLog. |
| **CC‑TGA‑17 — Assurance ops on Transfer** | On `U.Transfer` only `ConstrainTo/CalibrateTo/CiteEvidence/AttributeTo`; none write/update `⟨L,P,E⃗,D⟩`. | Edge audit shows ops; CtxState unchanged across the edge. |
| **CC-TGA-17a — Assurance operation specifications (normative)** | **ConstrainTo(region/policy)**: tightens declared region/policy; **pre**: region subset current; **post**: `⟨L,P,E⃗,D⟩` unchanged; **idem.** and **monotone** under composition. **CalibrateTo(calibrationReference)**: attaches an **editioned** calibration reference, such as a map or standard, with Phi-policy id; admissible per cited `CG-Spec`; **post**: `⟨L,P,E⃗,D⟩` unchanged; **idem.** on same edition; penalties appear **in R only**. **CiteEvidence(anchor)**: binds carriers via **SCR/RSCR**; adds no numeric claims; **idem.**; missing carriers => **abstain**. **AttributeTo(provenanceReference)**: provenance only; decision algebra unaffected; **idem.** Hidden GateChecks, plane/unit changes, or edition writes on edges are **forbidden**. | Operation specifications visible on edge audit; violations fail lint. |
| **CC-TGA-18 — Flow = valuation & slice-local refresh** | A flow declares valuation `ν` over `U.Transfer` plus `PublicationScopeId` and `PathSliceId`; refresh is bounded to the addressed slice; re-emit on edition change or selected refresh rule. | Flow publication shows `ν`; refresh trigger causes slice-local recompute. |
| **CC‑TGA‑19 — Γ_time on compare/launch** | All compare/launch faces pin `Γ_time`; no implicit *latest*. | Face audit shows Γ pins; LaunchGate blocks on stale. |
| **CC‑TGA‑19a — Γ_time pin shape (normative)** | The `Γ_time` pin is one of: `snapshot(t)`, `interval[t1,t2]` (closed), or `policy(Γ_timeRuleId)` that resolves to either; CV computations record the **resolved time basis** in `DecisionLog` and do not widen Γ at publication time. | DecisionLog shows basis; linter rejects missing/implicit Γ. |
| **CC‑TGA‑20 — Lean publish‑mode ≠ weaken** | `AssuranceLane‑Lite` changes publication faces only; required GateChecks for the active profile remain intact. | Gate in Lean/Core shows minimal pins; GateChecks list unchanged. |
| **CC-TGA-21 — Decision stability & idempotency witness** | Gate decisions are stable under the equivalence relation recorded by `A.21`; a **witness of equivalence** is present on the DecisionLog record; any change that breaks equivalence triggers re-aggregation. **Minimum lexeme (CV-relevant witness):** `EquivalenceWitness := { keys, E⃗, Γ_time(basis), PathSliceId?, ReturnShapeClass, ComparatorSetRef?, profile }`. | Modify any input outside the declared equivalence => re-aggregation; DecisionLog records the witness; lexeme present. |
| **CC‑TGA‑21a — Decision join (publication algebra)** | Aggregation over GateChecks is the **idempotent, commutative, associative join** on the lattice `abstain ≤ pass ≤ degrade ≤ block` with **neutral = `abstain`** and **absorbing = `block`**. The algebra is conceptual; publications carry only (i) the aggregated **GateDecision** and (ii) its **GateDecisionRationale** recorded in the **DecisionLog**. A **GateDecisionExplanation** is an optional human‑readable narrative derived from the GateDecisionRationale; it is **not** a decision and is not used as one. If aggregated `ConstraintValidity ≠ pass` or the active profile suppresses narratives, any GateFit‑oriented GateDecisionExplanation **does not apply**. | Review a gate with multiple GateChecks: the aggregated decision matches the lattice join; no per‑check arithmetic is introduced on faces. |
| **CC‑TGA‑22 — Errors/unknowns fold by profile** | Errors/timeouts fold to `degrade` under `Lean/Core` and to `block` under `SafetyCritical/RegulatedX`; `unknown` folds per GateCheck policy (safety‑default: `degrade`). | DecisionLog shows folds; profile switch changes fold behavior accordingly. |
| **CC‑TGA‑23 — SquareLaw on crossings** | For every GateCrossing, `gate_out ∘ transfer = transfer' ∘ gate_in`; LaunchGate case is mandatory. | MVPK shows commuting square; inconsistency yields `block/degrade` per profile. |
| **CC‑TGA‑24 — UNM declaration locus** | `CG‑Spec`, `ComparatorSet`, `UNM.TransportRegistryΦ` editions are declared only through the UNM governing locus (others ref‑only). | Declaration records show UNM as the governing locus; others have refs only. |
| **CC‑TGA‑25 — Evidence lanes & DecisionLogs** | AssuranceLane carries GateProfile, GateCheckRef list, edition pins, aggregated decision, `DecisionLogRef`; **evidence pins follow a two-part scheme**: **carriers** are pinned via **`SCR/RSCR`**, and **value annotations** are carried under **`VALATA (VA/LA/TA)`**. | Gate publication faces include these pins; logs retrievable. |
> **Coupling note.** `CC‑TGA‑07 (CV⇒GF)` and `CC‑TGA‑21a (Decision join)` together ensure that any GateFit‑scoped GateCheckRef **returns `abstain`** until the aggregated CV status equals `pass`; CV/GF separation remains intact.
> **Scope note (E.TGA vs neighbor patterns):** Detailed mechanism-scoped checks and publication obligations are governed by the current neighbor patterns named in this pattern's Relations. E.TGA fixes only graph-architecture obligations: single transfer edge, gate crossings, valuation, publication pins, CV/GF boundary, and slice-local refresh.

**Glossary (additions)**
* *Open‑world species* — non-exhaustive domain-scoped specializations of `U.Transduction` that map to the minimal kind set.
* *Signature (TGA kind)* — `U.Transduction(kind=Signature)`; **identical to** **A.6.0** `U.Signature` (universal block). **Not** a `C.3.2 KindSignature`.
* *KindSignature (C.3.2)* — intensional definition of a `U.Kind` (intent/extent, F); **unrelated** to TGA kinds; never a `genus`.
* *Species (domain-scoped)* — typed specialisations `speciesOf(kind=...)` that declare `KindDefinition=<current governing pattern id>` (e.g., `kind=Mechanism; KindDefinition=A.6.1`).
* *KindBridge (`CL^k`)* — a compatibility note on UTS for describedEntity/kind transitions; required by CC‑TGA‑06‑EX and crossings (CC‑TGA‑11).
* *Eulerian interpretation* — operational stance where a flow is treated as a valuation over `U.Transfer` and edges perform assurance‑only operations (no token‑passing semantics).
* **GateCheckKind boundary.** `GateCheckKind` is a publication/check lexeme used inside `GateCheckRef`, not a TGA node kind. No `GateCheckKind` becomes `U.Transduction(kind=Check)` unless an `OperationalGate(profile)` node is actually present.

* **GateCheckRef shape (publication lexeme received from A.21).** Where graph faces carry GateChecks, a **GateCheckRef** is a record
  received from `A.21`; E.TGA constrains only where graph faces carry such refs along TGA paths.

`GateCheckRef := { aspect, kind, edition, scope }` with:
  `aspect ∈ {ConstraintValidity, GateFit}`, `kind ∈ GateCheckKind`, `edition ∈ Editions`, and `scope ∈ {lane | locus | subflow | profile}`.
* **GateDecision / GateDecisionRationale / GateDecisionExplanation (terminology).**
  — **GateDecision** — the aggregated lattice value produced by `OperationalGate(profile)` for a specific `{GateProfile, GateCheckRef[]}`.
  — **GateDecisionRationale** — the minimal structured support **for that GateDecision**: per‑check outcomes, profile‑bound folds, and published evidence or witness references on the DecisionLog; it records **why the GateDecision is admissible** under the active profile.
  — **GateDecisionExplanation** — an optional human‑readable narrative derived from the GateDecisionRationale; it **does not carry decision status**. While aggregated `ConstraintValidity ≠ pass`, GateFit‑scoped checks return `abstain`; any GateFit‑oriented GateDecisionExplanation **does not apply**.
> **Clarity note.** **GateDecision ≠ GateDecisionExplanation**; narratives are optional and derivative of GateDecisionRationale.

* **GateFit (aspect, not an entity).** GateFit names the **aspect** of checks that evaluate **profile‑fit**; there is no separate GateFit entity. “Gate decision under GateFit” means “the gate’s decision computed from GateChecks with `aspect=GateFit`”.

  This shape is publication-only; it introduces no new execution steps and no arithmetic on faces.  (Couples to A.20/A.21 without duplicating their check catalogs.)
* *VALATA (VA/LA/TA)* — value-annotation scheme used on **AssuranceLane**; **carriers** are referenced via **SCR/RSCR**; detailed evidence obligations live in `A.10` and the named evidence, publication, or crossing pattern for the live case. Included here so evidence pins are self-describing in Part E texts.
* *Transfer vs Transport* — **Transfer** = the sole graph edge kind `U.Transfer`. **Transport** = Φ‑policy/registry‑defined conversions (`TransportRegistry^Φ`) referenced by UNM; “reuse via Transport” refers to the latter.
* *GateCrossing* — a typed node transition that writes/updates a CtxState slot or the kind‑channel; see **S1.b** for the normative list and required pins.
* *Admissible path* — a typed path obeying the GateCrossing discipline (no hidden crossings; witnesses present), Γ‑pinned on compare/launch, and `T^D↔T^R` only at `LaunchGate`; see **S2**.

### E.18:8 - Gating Profiles (applied to E.TGA)
This table is an architectural coverage table for E.TGA graph crossings and path slices. It is not the source of `GateProfile` semantics. `A.21` governs gate decision semantics, folds, `DecisionLog` minima, and the GateFit check-catalog boundary.

> Gating is expressed as **publication‑gating** per E.17 profiles. The graph model aligns with the **CC items** listed for the chosen profile; broader obligation profiles include all narrower-profile items.

| Profile                          | Required CC‑items                                         | Additional notes                                                                               |
| -------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Lean**                         | 01–06, 08–09, 11–12, 15, 19–21, 25                                                                                                           | Minimal MVPK presence; LaunchGate keeps `FreshnessUpToDate` & `DesignRunTagConsistency`. |
| **Core**                         | **Lean** + 07, 10, 13–14, 16–18, 22–23, 24                                                                                                  | Adds CV⇒GF order, CSLC pins, budgeted loop, guards, valuation/sentinel refresh, error folds, SquareLaw, and the UNM declaration locus. |
| **Safety‑Critical / RegulatedX** | **Core** + profile‑specific GateChecks (safety envelope, regulator id/editions) with stricter folds per **CC‑TGA‑22**; SquareLaw audits tightened | — |

**Recommended defaults (non-normative, tie-in to `A.21` and `G.11`).** Profiles inherit along a `PathSlice`; local overrides only **add** GateChecks; weakening uses a new `PathSlice` and refresh wiring through the current `G.11` locus when live.

### E.18:9 - TGA LEX discipline (registration)
Register Tech tokens (ASCII) used by this architecture with twin‑labels: `U.TransductionGraph`, `U.TransductionFlow`, `StructuralReinterpretation`, `OperationalGate`, `GateProfile`, `GateCheckRef`, **`GateCheckKind`**, `DecisionLog`, `USM.CompareGuard`, `USM.LaunchGuard`, `KindBridge`, `SubflowRef`, `FlowEmbed`, `SentinelId`, `PathSliceId`, `SliceRefresh`, `FinalizeLaunchValues`, `VALATA`. Add an ASCII alias **`CLKind`** ↔ Plain `CL^k` (cf. `CLPlane` ↔ `CL^plane`). Reference MVPK E.17 naming for faces.
**CtxState Extension Registry.** Register any extra CtxState slot beyond ⟨L,P,E⃗,D⟩ with: slot id, informal intent, partial‑order law (with neutral/absorbing), SquareLaw compatibility note, and the owning Gate profile(s) that may change it. Absence of registration ⇒ **non‑conformant**.

### E.18:10 - Consequences

**Benefits.**

1. **Universality with discipline:** one edge kind and explicit gates eliminate second hidden work/method orders and make cross-domain flows (ML, supply-chain, TAMP and MPC, scientific work graphs) uniformly analyzable and auditable.
2. **Comparability & replayability:** CSLC and edition‑pinned comparators prevent covert scalarization and enable declared set returns and reproducible decisions.
3. **Locality of change:** sentinel subflows restrict refresh to affected `PathSlice`s; large graphs remain stable under frequent edition bumps.
4. **Clean DesignRunTag fold:** LaunchGate and `DesignRunTagConsistency` stop premature launch‑value slot filling; acceptance and telemetry live where they occur (`U.Work`).
5. **Assurance visibility:** MVPK makes GateProfile/DecisionLog records locally checkable and cacheable for the same `{PathSlice, GateChecks, Editions}`.

**Trade‑offs.**
a) **Higher upfront modeling cost:** explicit Bridge/UTS pins and GateProfiles demand care; mitigated by Lean profile and templates.
b) **Longer edge face sets:** MVPK faces are verbose by design; lean face sets can be used for low‑risk segments.
c) **Tooling alignment:** some incumbent DAG‑only orchestrators conflict with budgeted cycles and set‑return semantics; adapters project E.TGA semantics to their interop boundary (never the other way round).

### E.18:11 - Rationale

E.TGA states **strict separation of concerns** (graph-architecture scope only); **specialized semantics are governed by the current neighboring patterns named below**:

* **What the graph is:** typed intensional morphisms and the single graph edge kind `U.Transfer`.
* **Where/when it crosses contexts:** **only** at `OperationalGate(profile)`, with Bridge+UTS, CL/CL^plane, and Φ published in R-lane.
* **How comparability works:** UNM is the single governing locus for unit, plane, and transport declarations, and selectors operate **only** on normalized, edition-pinned comparators, returning sets or archives rather than totals. Edition-aware pins and archive semantics are checked through `A.19.SelectorMechanism`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` when live.
* **How change propagates:** sentinel‑bounded `PathSlice` refresh; editions are monotone; LaunchGate is the only binder of launch‑values.

This arrangement gives checkable conditions for **functorial publication** (commuting squares on crossings) and **orthogonality** of inner technical validity (ConstraintValidity) to context fit (GateFit), which in turn keeps gate aggregation **order-independent** under the CV=>GF activation predicate.

### E.18:12 - SoTA‑Echoing (post‑2015, multi‑Tradition)

> Each row states the source idea, the FPF invariant E.TGA adopts, the practitioner move it changes, and the shortcut it rejects. Vendor, tool, and literature tokens are informative; the invariant and practitioner move carry the pattern explanatory work.

| SoTA source idea | FPF invariant | Practitioner move | Rejected shortcut |
|---|---|---|---|
| **Applied category theory / compositional open systems** (Fong & Spivak, *Seven Sketches in Compositionality*, 2019) | Use one `TransductionGraph` whose nodes are typed morphism/transduction bindings and whose edges use the single graph edge kind `U.Transfer`; publication faces preserve composition rather than inventing a second publication meaning. | Name the graph object, node kinds, one `U.Transfer`, and any live path or crossing before drawing an ordered work/method sequence. | Treating category-theory prestige, tool pipelines, lineage packages, or work/method narratives as graph semantics. |
| **Operads, wiring diagrams, and hypergraph categories** (Spivak, *Operads of Wiring Diagrams*, 2021; Baez & Fong, *A Compositional Framework for Passive Linear Circuits*, 2015) | Typed ports and interface junctions motivate Bridge/CL/Phi pins at crossings; E.TGA adapts the math by requiring publication pins that the math alone does not supply. | When an interface or boundary crossing matters, publish the Bridge, UTS row, CL/CL^plane, and R-lane penalty placement instead of leaving an unpinned junction. | Reading an interface diagram, wiring diagram, or decorated cospan as sufficient crossing evidence. |
| **Open-graph and string-diagram rewriting** (Bonchi et al., *Graphical Linear Algebra*, 2019; Kissinger survey lineage) | Rewrites and subflow refactors are admissible only with edition bumps, sentinel scopes, and `PathSlice` locality sufficient for replay. | Localize the rewrite to the affected subflow or slice, pin editions, and re-emit the affected faces. | Treating a global rewrite as replay-safe because the diagram still looks equivalent. |
| **Research-package portability / RO-Crate-style research packaging** (RO-Crate 1.2; Soiland-Reyes et al., *Packaging research artefacts with RO-Crate*, 2022, as lineage) | Portable package descriptions belong in MVPK faces and InteropCards; packages and lineage metadata do not define graph semantics. | Publish package, provenance, and source refs as publication support while keeping graph meaning in the node/gate definitions. | Treating a crate, package, file bundle, or lineage record as the semantic authority for the graph. |
| **Reproducibility and content addressability** (Di Cosmo et al., *Referencing Source Code Artifacts: a Separate Concern in Software Citation*, 2020) | Stable identifiers become edition pins and entries in `E⃗`; they make references checkable but do not decide node, gate, or mechanism meaning. | Pin the exact editions of code, comparator, transport registry, descriptor map, or distance definition used by a face or path. | Treating an identifier, hash, or content-addressed source ref as semantic authority. |
| **TAMP and MPC planning and control practice** (Garrett, Lozano-Perez, Kaelbling 2021 as lineage; Zhao et al., *A Survey of Optimization-based Task and Motion Planning*, 2024, as a TAMP survey anchor; named MPC survey or named reference used when MPC is the live claim) | Iteration is allowed only as a budgeted Selection-Planning loop with freshness checks and launch values bound in `U.WorkEnactment`. | Declare the loop budget, freshness/request boundary, next `PathSlice`, and Work-only launch-value filling. | Turning E.TGA into an ordered work-method narrative, an unbounded loop, or pre-Work launch-value filling. |
| **Quality-Diversity / illumination search** (MAP-Elites and CMA-ME as lineage; QDax JMLR 2024 for QD library support; QDHF 2023/ICML 2024 or QDAIF 2023 refs only when feedback-guided QD is live) | Set and archive returns stay visible; E.TGA treats covert scalarization to one winner as non-conformant while leaving selector, archive, dominance, and comparator semantics to neighboring loci. | Return the set/archive, pin comparator and descriptor/distance editions, and cite the selector/comparator loci when live. | Collapsing a partially ordered or archive-like result into a single best score. |
| **Profunctor optics / modular projection practice** (Pickering, Gibbons, Wu, *Profunctor Optics*, 2019) | MVPK faces are projections of graph/morphism information; they carry views without adding new numeric or mechanism claims. | Publish views as MVPK faces with correspondence refs and pins, while leaving transformations and checks in their governing patterns. | Treating a view, projection, screen, or explanation as a transformation, evidence result, or gate decision. |

*Cross-tradition note.* Rows 1-3 (compositional graph practice), rows 4-5 (publication and reproducibility practice), row 6 (controls/robotics), row 7 (evolutionary search), and row 8 (PL/semantics) jointly anchor E.TGA across multiple traditions per E.8, but each row is retained only because it changes a practitioner move or rejected overread.

### E.18:13 - Bias‑Annotation (per E.8 SG‑bias slot)

* **Acyclic‑bias risk.** Tooling accustomed to DAGs may discourage admissible feedback loops; E.TGA explicitly permits loops with budget/sentinel controls (CC‑TGA‑13,‑18).
* **Scalarization-bias risk.** Cultural defaults to single-score rankings can suppress Pareto/QD sets; E.TGA keeps declared order relations and return sets visible (CC-TGA-10, CC-TGA-12).
* **Interop‑dominance risk.** File/format ecosystems (CWL/RO‑Crate/lineage) can be mistaken for semantic sources; E.TGA places them in **InteropCard** and keeps intensional semantics in nodes/gates.
* **Over‑formalization risk.** Category‑theoretic formalisms can obscure operational guard‑rails; E.TGA grounds crossings in Bridge/UTS/CL/Φ pins and SquareLaw audits (CC‑TGA‑11,‑17).
* **Retrospective rewrite risk.** Global rewrites break replay; E.TGA confines them to edition bumps and slice‑local refresh (CC‑TGA‑16).

**Mitigations.** Profile‑gated publication, audit of `DecisionLog`, mandatory edition pins, Lean‑to‑Core upgrade paths, and conformance tests tied to PathSlice replay.

### E.18:14 - Relations (explicit pattern‑to‑pattern edges)

> Directed edges (→) are typed as **builds_on / constrains / coordinates / specializes / publishes_on / requires / provides_checks_for**.

**Foundations**
* **E.TGA →builds_on→ E.17 MVPK (for Morphisms).** Faces, pins, lanes, functorial publication, Lean/Core/Regulated profiles.
* **E.TGA →builds_on→ A.6.0 U.Signature / A.6.1 U.Mechanism.** Node kinds and intensional content boundaries.
* **E.TGA →builds_on→ A.7 Strict Distinction (described-entity, description, and carrier separation).** No new claims on faces; publication faces project morphisms.

**Flow semantics & checks**
* **E.TGA →coordinates→ A.20 U.Flow (ConstraintValidity scope).** CV checks live inside transformations; no declaration/translation of planes/units in CV; **error/timeout/unknown folds** follow **CC‑TGA‑22** as the **minimum default** (profiles can be stricter).
  **Terminology discipline (A.20 boundary).** In CV scope, publications use **status/witness** language; **GateDecisionRationale/GateDecisionExplanation** are reserved for gating and do not apply to CV.
* **E.TGA →coordinates→ A.21 GateProfilization (GateFit scope).** **GateFit-scoped GateChecks** are aggregated by `OperationalGate(profile)` with CV⇒GF activation; the **enumeration and publication shape** of GateChecks live in **A.21**. **Equivalently:** a GateFit decision different from `abstain` appears only when aggregated `ConstraintValidity = pass`; otherwise the **GateDecisionExplanation (GateFit‑oriented)** does not apply.
* **E.TGA →uses→ USM.CompareGuard and USM.LaunchGuard.** Guards publish scope and responsible gate; guard failures are handled by the declared gate.
* **E.TGA -> constrains -> F.9/F.17 bridge and terminology-synchronization loci (Bridge+UTS, CL/CL^plane, Phi -> R).** A transition is treated as a **Crossing** iff `Bridge+UTS` and the appropriate `CL/CL^plane` are published; otherwise this crossing explanation does not apply. Where Phi defines penalties, they appear in the R-lane only.
* **Operational interpretation (default): Eulerian.** A flow is a **valuation** over `U.Transfer`; edges carry **assurance‑only operations** (see CC‑TGA‑17); no token‑passing semantics are assumed.

**UNM & comparability**
* **E.TGA →constrains→ UNM declaration and use loci.** `CG‑Spec`, `ComparatorSet`, and `UNM.TransportRegistryΦ` declarations are governed by UNM; normalize-then-compare is mandatory.
* **E.TGA →constrains→ G.5 SelectionAndTuning.** Set‑returning, comparator‑pinned decisions, no hidden scalarization; `MethodTuning` without launch‑value slot filling.
* **E.TGA →constrains→ G.11 EvaluatingAndRefreshing.** EditionBumpProposal, two-phase update through the UNM declaration locus, path-local refresh.

**Work boundary**
* **E.TGA →coordinates with→ A.15 U.WorkEnactment (`FinalizeLaunchValuesOnlyInWork`).** Single point of `FinalizeLaunchValues`; `FreshnessUpToDate` hard at LaunchGate; acceptance/telemetry published here.

**Structure & reuse**
* **E.TGA →specializes→ U.TransductionFlow (and its family).** The graph architecture is the common substrate on which flow patterns (e.g., P2W, EvaluatingAndRefreshing) are defined; E.TGA provides coherence checks for their crossings, guards, and MVPK faces.
* **E.TGA -> coordinates with -> C.30.TGA-FLOW-REL.** When a TGA graph is used as architecture-description support, `C.30.TGA-FLOW-REL` records the relation between flow/transduction structure and `ArchitectureOf@Context`; E.TGA keeps graph, crossing, and flow-valuation discipline.
* **E.TGA →publishes_on→ E.17 MVPK views** (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`) for every edge/node where publication occurs; Lean mode allowed only as per profile.

### E.18:15 - Conformance evidence (how to show you comply)

1. **Model lint:** run static checks for CC‑TGA‑01…25 (edge kind, gates on crossings, CV⇒GF, guard aggregation assignment, UNM declaration locus, SquareLaw).
2. **Publication audit:** sample a commuting square and a sentinel‑bounded subflow; verify pins and DecisionLog behavior on *block/degrade*.
3. **Replay test:** hold editions fixed; re‑run selection on a PathSlice; observe identical return‑sets; apply a bump; see only affected `PathSlice`s refresh.
4. **StructuralReinterpretation probe:** construct a minimal reinterpretation step; confirm `CL^k` with `bridgeChannel=Kind` on UTS, a SquareLaw‑retargeting witness on UTS, `PathSliceId` pinned, **CV.ReinterpretationEquivalence=pass**, and absence of hidden scalarization.

[20]: https://webstore.ansi.org/preview-pages/ISO/preview_ISO%2B23247-1-2021.pdf?srsltid=AfmBOooAUXpg38IpkTlUFtcCpaMVOjivkewJWDIUd1VemIJO91abNEkG "INTERNATIONAL STANDARD ISO 23247-1"

Does not replace: `A.20` constraint-validity checks, `A.21` gate decisions and GateProfile semantics, `E.20` mechanism-meaning placement, `E.17` MVPK publication faces and viewpoint bundles, `A.15` work plans or work enactments, `G.5` selector and set-return semantics, `G.11` refresh orchestration, `A.10`/`G.6` evidence support, `C.30` architecture-description adequacy, `C.30.ASV` structural-view adequacy, or `C.30.TGA-FLOW-REL` architecture-flow relation support.

### E.18:End
