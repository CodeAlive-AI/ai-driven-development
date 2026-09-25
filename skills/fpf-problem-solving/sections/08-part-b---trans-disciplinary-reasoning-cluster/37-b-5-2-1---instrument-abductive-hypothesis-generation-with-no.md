## B.5.2.1 - Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)

**Status.** Normative binding to **B.5.2 Abductive Loop**. The local **NQD-Generate** Method in §4, or an equivalent declared generator, constructs the candidates. **C.18** supplies generation, archive and front records; **C.19** supplies the applicable exploration/exploitation policy.

**Non-duplication & parsimony.** Reuse A.17/A.18 for Characteristics and A.3.1/A.3.2 for the Method and its description. The local Method supplies candidate construction without adding a kernel operator. Distinguish its input and seed conditions, conditions for any actual generation Work, and the generated candidate’s later admission to comparison. C.18 records the identified generator and its results; filling that record performs no generation.
**Terminology discipline.** Use **NQD** consistently (Novelty–Quality–Diversity). Treat **S**/**I** as *secondary* metrics unless explicitly promoted by policy (see §3, §5).

### B.5.2.1:1 - **Problem Frame**
* **Conceptual binding:** **B.5.2 Abductive Loop** (this pattern specifies the *how* for Steps 2–3).
* **FPF pattern:** a domain‑neutral **Creativity‑CHR** (C‑cluster) that declares the **Characteristics** used here (see §2). (No change to Γ/LOG.) This binding uses **C.18** for generation/archive/front records and **C.19 E/E-LOG** for EmitterPolicy.
* **Manager’s mental model (informative):** “We add measurable characteristics for *newness*, *spread*, and *fit*, then use a generator that explores widely and returns a **front over the declared Q components** together with retained exploration/archive evidence when the policy asks for it, not a single winner and not one bundled `{Q,N,D}` default.”
* **Operational loops:** compatible with **B.4 Canonical Evolution Loop** (ideas generated here flow into Run→Observe→Refine→Deploy) and with **B.5 Canonical Reasoning Cycle**, which selects the reasoning contribution needed by the current question.
* **Decision-subject note.** Later choices are attributed to one declared `DecisionSubject` at explicit `DecisionSubjectGranularity`. **Contexts publish** measurement spaces and admissible policies as **semantic frames**; they do **not** enact choices.

### B.5.2.1:2 - Intent & Problem

**Intent.** Turn Step 2 (*generate*) and Step 3 (*filter*) of the Abductive Loop from ad‑hoc brainstorming into a **disciplined, instrumented exploration** that can (i) *produce many* distinct, plausible hypotheses and (ii) *surface the few worth pursuing*—*without* bloating the kernel or forcing a specific creative method.

**Problem.** Unstructured ideation routinely fails on two fronts: it either produces *too little variety* (pet ideas win by seniority) or *too little plausibility* (grand theories with no testable predictions). **B.5.2** names these failure modes; this pattern adds a minimal, measurable counter‑mechanism aligned to FPF’s assurance lanes and state machine.

### B.5.2.1:3 - The **Creativity‑CHR** (references only; no re‑definitions here)

This binding **references** the context‑local **Creativity‑CHR** (see **C.17**) and **does not** restate measurement templates. The primary coordinates are:
- **`Novelty@context`** (C.17 §4.1), • **`ΔDiversity_P`** (marginal; C.17 §5.1), and • **`Q` components** (per A.18).
Surprise is an optional coordinate; IlluminationSummary is a retained-set telemetry report under C.17. Use either in comparison only when the C.19 policy names that use and its constituted basis; promotion into dominance requires an explicit policy.
**`Use‑Value`** (*alias:* `ValueGain`) is **informative for decision lenses** (Decsn‑CAL) and **MUST NOT** enter NQD dominance by default (see C.17 §4.2).

For each coordinate actually used, declare its bearer, Characteristic, Scale, polarity, admissible operations, scope, window and evidence basis under C.17. Cite a constituted C.16 measurement result when the coordinate was measured, or a C.2.1 ascription under its declared rule. Candidate must-constraint eligibility and the conditions for performing generation are separate questions.

> **Lexical discipline.** The items above are **Characteristics** in the sense of **A.17/A.18**; avoid reserved names such as “validity” or “operation.”
> **Comparison basis.** Compare each Q coordinate under its declared Scale, polarity and admissible order. Different units across coordinates do not by themselves require normalization for componentwise Pareto comparison. If the chosen comparator requires a transformation, declare it and preserve the order distinctions on which dominance depends (see CC-B.5.2.1-6).
> **D and I.** D = ΔDiversity_P(h | Pool) is a marginal retained-set reading under the same declared measurement policy. It is outside primary dominance unless explicitly promoted. IlluminationSummary reports the retained set; it is not a per-hypothesis primitive coordinate. A C.19 policy may name a tie-break or promoted use with the corresponding report and basis.
> **Measurement invariants.** Distances, grids, and transforms MUST be declared once per run, versioned, and referenced from provenance (§3, §5).

### B.5.2.1:4 - Solution — **NQD-Generate and its C.18 records**

**Method name (Plain/Unified Tech).** *NQD‑Generate* — a **U.Method** that, given (i) a **HypothesisSpace** and (ii) a **CharacteristicSpace** with a **CoverageGrid**, returns a *finite* candidate package: a current **front over the declared `DominanceSet`** plus the retained archive/tie-break telemetry needed to keep diversity and novelty reviewable without making them default dominance dimensions.

**Minimal signature.**

* **Inputs (declared in MethodDescription):**
 `HypothesisSpace`, `CharacteristicSpace`, `Seeds?`, `Budget (time/compute)`, `EmitterPolicy` (**E/E-LOG policy id**), `QualityMeasures (Q components)`, `NoveltyMetric`, `CoverageGrid/Granularity`, `CellCapacity K? (default=1)`, `EpsilonDominance ε? (default=0)`, `TieBreakPolicy? (S/I)`, `DedupThreshold?`, `Policy(TimeWindow)`, `DeterminismSeed?`

* **Outputs:**
  CandidateSet = {h_i: (desc_i, Q_i, N_i?, D_i?:=ΔDiversity_P(h_i | Pool), S_i?, UseValue_i?), genealogy_i?, provenance_i (including **DHCMethodRef.edition** and **policyId** from E/E-LOG)} where `Q_i` is a vector and `provenance_i` captures generator settings and evaluation sources. The coordinate entries cite the constituted results actually used. When illumination is reported, carry IlluminationSummary separately as a report about its declared retained set. Unused optional readings need not be produced. If Use-Value is present, identify its objective or acceptance criterion and scope. For a gain claim, also identify the baseline and comparison or counterfactual Method; for a predicted reading, identify the model edition and assumptions under C.17. Note: `N`, `D`, `S`, and `I` are archive, tie-break, telemetry, or policy-promoted signals by default; only the declared `DominanceSet` enters the current front. `Use-Value` is decision-side/supporting unless the current Context explicitly declares it inside the active `Q` tuple / `DominanceSet`; when it is only recorded as a side measure, keep it outside dominance.

**Strategy (notation‑neutral).**

1. **Seeding and constructors.** Declare the explanatory question, hypothesis space and permitted variation operators in the MethodDescription. Initialize with admissible seeds: known explanations, random draws under that grammar or prior hypothesis-bearing epistemes with their grounds and limits. Name how an operator constructs a changed explanatory claim, for example by replacing a proposed mechanism or combining two mechanisms under a stated interaction assumption. When there are no seeds, use the declared finite enumeration or sampling rule.
2. **Construct and assess.** Apply the selected variation operators to the seeds or retained candidates within the budget; record each resulting hypothesis and its parent/operator provenance. Then test candidate must-constraints for comparison and evaluate each required Q component. Keep an excluded candidate and its reason distinguishable from a candidate not yet generated. Maintain up to K retained entries per declared cell; obtain only the N, ΔDiversity_P and Surprise readings actually used under C.17, and any required retained-set illumination report. Deduplicate under the declared rule and threshold.
3. **Budget‑bounded loop.** Iterate until budget or coverage‑convergence; return the **(ε‑)Pareto front** over the declared `DominanceSet`. When the Context consumes the ordinary default, that means the declared `Q` components under `DefaultId.DominanceRegime`, not one fresh local doctrine. Keep `N`, `D=ΔDiversity_P`, `Surprise`, and `IlluminationSummary` as archive/tie-break/telemetry signals unless one Context policy explicitly promotes one of them into dominance and records the policy id. `Use-Value` enters dominance only when the current Context explicitly declares it inside the active `Q` tuple; otherwise it may appear as one decision-side/supporting side note.
4. **Traceability.** Emit a **Design Rationale Record (DRR)**: grids/metrics versions, seed(s), policy and `TimeWindow`, which cells were filled, why items were dominated (list **Characteristics**), and how the final set was produced (including `ε`, `K`, and dedup). (Lightweight DRR is permitted per B.4 guidance.)
5. **Algorithmic freedom (informative).** Implementations MAY use MAP‑Elites/illumination, novelty search with local competition, Bayesian/surrogate‑assisted search, or deterministic enumerations; ε‑dominance or knee‑point thinning MAY be used *after* recording the full front in provenance.

> **No kernel growth.** This is a method/work use of `A.3`, `A.15`, and `B.1.5` plus a characteristic-space import; **no new Γ‑operator** is added (per **A.11**).

### B.5.2.1:5 - Implementation & Binding into **B.5.2** (two injection points)

**Step 2 — Generate candidates.**
**Before generation.** Establish the Method’s applicable input/seed conditions. For actual generation Work, satisfy its independently applicable authority, assignment, scope, window, budget and permission conditions, including USM coverage and an enactable RSG state when the governing use requires them. A theoretical candidate comparison does not acquire a fictional performer or permission gate. A generated candidate’s ConstraintFit is assessed after construction and controls its admission to the specified comparison.

When the pattern is imported, use NQD-Generate for the selected generation contribution. Its candidate package carries conjectural content and the constituted coordinate results and provenance actually used. Report diversity to the extent supported by its declared reading; generation assigns no assurance level.

**Step 3 — Plausibility filters.** Apply B.5.2’s plausibility criteria, now with explicit hooks:

* **Falsifiability / probeability** → require an interpretable implication or possible discriminating contrast under B.5.2. Keep a meaningful conjecture distinguishable from the present availability or worth of its check.
* **Explanatory power** → prioritize candidates whose *Q‑improvements* (and attached rationales) align with the framed anomaly.

Apply B.5.2 to return a qualified prime conjecture when its comparison warrants one, or an explicit abort, defer or split result. Deduction, evidence acquisition and action choice remain separate questions.

Primary dominance test: compute the (ε-)Pareto front over the declared `DominanceSet`. When the Context consumes the ordinary default, that means the declared `Q` components. For tie-breaking, use only the constituted Novelty, ΔDiversity_P, Surprise or IlluminationSummary results named by the active C.19 policy. Optional archive or telemetry readings retain their own declared use; promotion into dominance requires an explicit policy. `Use-Value` remains non-dominant unless the active `Q` tuple explicitly includes it.

**Ordinary fallback posture when no narrower local policy is specified**
> Do not mint one local dominance doctrine here. Consume the ordinary default `DefaultId.DominanceRegime` from `G.Core/G.5` together with the active `C.19` policy-side defaults; in ordinary Q-front use this means the declared `Q` components, with `ConstraintFit=pass` as the **candidate admission condition for that front**, assessed after generation.
> **Tie-breakers:** use only the constituted `Novelty@context`, `ΔDiversity_P` or `Surprise` results named by the active C.19 policy. `IlluminationSummary` remains report-only unless that policy names a tie-break or promoted use. Unused optional readings need not be produced.
> **Archive:** `K=1`, `ε=0`, deduplication in `CharacteristicSpace`.
> **Policy family:** one uncertainty-aware explore policy family with one declared regime key; `UCB`-class with moderate temperature and `explore_share ≈ 0.3–0.5` is one didactic starter profile, not the semantic default family.
> **Provenance (minimum):** record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `EmitterPolicyRef`, `TimeWindow`, `Seeds`.

“**Scope‑of‑claim annotation (descriptive).** Record the **BoundedContext** and **TimeWindow** that delimit where each **N/Q/D** measurement is intended to hold; this is for reasoning traceability only (no operational gates).”

Note — Status `Surprise` (scope and default role):
Use `Surprise` as a secondary tie-break only when the active C.19 policy names that use, among candidates otherwise Pareto-equivalent on the declared primary characteristics. A policy may explicitly promote `Surprise` into dominance with its constituted basis. If the policy does not use `Surprise`, omit that reading.

### B.5.2.1:5.1 - Creative-generation consistency with the declared dominance doctrine

- When candidate generation speaks about fronts, use the declared `DominanceSet` for the front and keep archive retention separate when archive mode is active.
- Do not write novelty or diversity terms into the front definition merely because they are important to archive quality or exploration value.
- If one generator emits both a front-facing result and an archive-facing result, say which surface each result belongs to.
- If one generator speaks about selected results, keep that language in the shortlist family rather than silently reusing front language.
- Prefer wording like `front over the declared DominanceSet, plus the corresponding ExplorationArchive when archive mode is active` over wording that folds `Q`, novelty, and diversity into one default front by habit.
- The local generation story should stay consistent with the declared `Front`, `Archive`, and `Shortlist` language so comparison stays intelligible and lawful.

### B.5.2.1:6 - Conformance Checklist (normative)

**CC‑B.5.2.1‑1 (CHR discipline).** If this pattern is applied in a Context, that Context **SHALL** declare the Creativity‑CHR **Characteristics** with **A.18**‑style templates (type, unit/range, polarity). No new kernel terms are introduced.
**CC‑B.5.2.1‑2 (Instrumented generation).** Step 2 of **B.5.2** **SHALL** either (a) invoke *NQD‑Generate* or (b) justify a Context‑specific generator of equivalent effect (diversity + quality + novelty with measurable **Characteristics**).
**CC-B.5.2.1-3 (Diversity coupling).** Whenever a `D` reading is used, it SHALL be `ΔDiversity_P` computed against the current candidate Pool using the C.17 definition of `Diversity_P` under the same Context, CharacteristicSpace, kernel and TimeWindow.
**CC-B.5.2.1-Eligibility.** The MethodDescription SHALL state applicable input/seed conditions. Any actual generation Work SHALL meet its independently governed authority, assignment, scope/window and permission conditions. Assess each generated candidate’s must-constraints before admitting it to the comparison/front that consumes ConstraintFit; a result about that candidate SHALL NOT be a precondition for creating it. Preserve exclusions and their reasons.
**CC‑B.5.2.1‑4 (Non‑dominated candidate front).** The *CandidateSet* **MUST** include the **Pareto front** over the declared `DominanceSet`. If the Context consumes the ordinary default, cite that consumed `DefaultId.DominanceRegime` rather than restating one local default doctrine. Every exclusion SHALL retain its actual reason. A dominance exclusion names the dominating candidate and declared coordinates; deduplication cites its equivalence or distance rule; archive retention and post-front thinning cite their policies. Preserve the complete computed front before thinning and label a thinned result separately. `N`, `D=ΔDiversity_P`, `Surprise`, `IlluminationSummary`, and similar signals enter dominance only under an explicit recorded promotion policy; otherwise they remain archive, tie-break, or telemetry signals.
**CC‑B.5.2.1‑4a (Archive companion when retained exploration is in scope).** If the active policy depends on retained exploration, stepping-stone retention, or open-ended search, the emitted candidate package **MUST** include the corresponding `ExplorationArchive` or cite one explicit policy id that says archive mode is disabled for that run.
**CC-B5.2.1-5 (Hypothesis-led testing).** Before claiming empirical corroboration, the practitioner SHALL derive the consequences needed to interpret the test and retain how the tested hypothesis was obtained. Generation SHALL NOT assign an assurance level, require a new experiment or prescribe the next reasoning contribution independently of the receiving question.
**CC-B.5.2.1-6 (Coordinate comparability).** Dominance SHALL use compatible readings on each declared coordinate and its polarity. Any required transformation SHALL be explicit and preserve the comparator's relevant order distinctions; heterogeneous units across different coordinates alone SHALL NOT trigger mandatory normalization.
**CC‑B.5.2.1‑7 (Use‑Value separation). ** If Use‑Value (C.17 §4.2) is recorded outside the active `DominanceSet`, it SHALL remain outside Assurance scores and MAY inform decision lenses (Decsn‑CAL). If the current Context explicitly places `Use-Value` inside the active `Q` tuple, record that declaration together with its objective id / acceptanceSpec. Do not alter **R/G** semantics based on side-measure Use‑Value. (see **C.17 §4.2** for `Use-Value` and `ValueGain` definitions)
**CC‑B.5.2.1‑8 (Provenance).** Each `h_i` in the *CandidateSet* **MUST** reference its `provenance_i` sufficient to reproduce scores given the same `Policy(TimeWindow)`, score/metric versions, and `DeterminismSeed?`.
**CC‑B.5.2.1‑9 (Secondary metrics).** **I (illumination)** and **S (surprise)** SHALL be used only for tie‑breaking/reporting unless explicitly promoted by policy; the **primary dominance test uses the declared `DominanceSet`**, which under the ordinary default means the context-declared `Q` components.
**CC‑B.5.2.1‑10 (Cell capacity & ε).** If `K>1` or `ε>0` are used, the values MUST be declared and recorded in provenance; any thinning AFTER recording the front SHALL be documented in the DRR.
**CC-B.5.2.1-11 (Dominance set).** If the Context consumes the ordinary default `DefaultId.DominanceRegime`, the active dominance set **SHALL be the declared `Q` components** and provenance **SHALL** cite that consumed default plus the active C.19 policy or lens id. Any `Novelty@context` or `ΔDiversity_P` tie-break SHALL be named by that policy and use a constituted result on a compatible basis; an unused optional reading need not be produced. Promotion into dominance SHALL be explicit and recorded with the policy id.

### B.5.2.1:7 - Cognitive Load & Kernel Growth Budget

**For engineers/managers (user cognitive load).**

* *Added steps:* selecting descriptor **Characteristics** & granularity; reading a Pareto table (**non‑statisticians tip:** scan the “front” row; ignore dominated rows).
* *Mitigations:* provide a one‑screen “NQD Cards” template analogous to RSG cards; default grids and metrics per Context. (Keep ≤ 7 visible **Characteristics**—mirrors RSG human‑scale guidance.)
* *Reader quickstart (engineer‑manager):* (1) Pick 2–3 **Q** characteristics aligned to the anomaly + a simple **CharacteristicSpace** (2–4 dimensions). (2) Accept defaults for `NoveltyMetric`, grid granularity, and `K=1`. (3) Run **NQD‑Generate** to a fixed budget; read the *front row* first. (4) Apply Step 3 filters; log decisions in the DRR.

**For the framework (kernel growth).**

* *Zero* new primitives; only a CHR import and a **Method**. Passes **A.11** minimal‑sufficiency.

### B.5.2.1:8 - Placement in the Reasoning Cycle (ADI)

This pattern structures candidate hypothesis exploration within B.5.2. A receiving use determines whether deduction, evidence acquisition, assurance or action choice is needed next. Actual development transitions meet B.5.1's project and domain conditions; a conjecture does not itself make that transition.

### B.5.2.1:9 - Context‑Level KPIs (optional, informative)

Contexts *may* monitor these—*not* as gates, but to improve practice:

1. **Profile-specific assurance progression (optional).** When a receiving domain uses an assurance-level profile, report the fraction of cycles whose candidate meets a named level under that profile within the policy window. Name the claim, use and satisfying evidence; omit this KPI when no such profile is used.
2. **Frontier‑Hit Rate (FHR).** % of cycles where the chosen candidate lies on the **Pareto front** over the declared `DominanceSet` at selection time; track novelty/diversity contribution separately as archive, tie-break, or policy-promoted evidence.
3. Coverage Gain (ΔI, report). Change in the *illumination summary* (coverage map/%filled cells) per cycle (how much of the descriptor space is now “lit”).
4. **Exploration Cost Ratio (ECR).** Compute/time spent in NQD‑Generate divided by downstream Shape/Evidence cost saved (tracks whether the pattern pays for itself).
5. **Refutation Learning Yield (RLY).** Among *refuted* candidates, % that added new coverage or raised SurpriseScore—turning “failures” into map‑building.

### B.5.2.1:10 - Worked micro-example: explanatory rivals and a separate next action

**Question and case facts.** In a constructed service case, O1 is a latency rise above eight concurrent requests, O2 an increase in blocked threads, O3 a higher cache-miss rate, and O4 normal latency in a serial replay. The question is what explains this contrast. These are stipulated teaching inputs, not empirical results about a real service.

**Construction.** Declare hypothesis grammar v1 with three mechanism flags: lock contention, cache churn and scheduler stalls. The seeds are A, a lock-contention explanation, and B, a cache-churn explanation. NQD-Generate enumerates two declared variations: combine A with B to construct C, an interacting lock/cache explanation; replace A’s mechanism with scheduler stalls to construct D. The finite budget is four hypotheses including the seeds. Provenance records each seed, constructor and resulting claim. The comparison’s must-constraints are that a candidate addresses these service observations using the declared mechanism grammar and makes a discriminating prediction. All four pass after construction.

**Coordinates and comparison.** Q has two ordered count Scales: predicted observations among O1–O4, maximized, and auxiliary assumptions not established by the case facts, minimized. Prediction coverage is calculated under each candidate’s stated auxiliary assumptions; it is not independent confirmation. A predicts O1/O2/O4 with one unverified lock-scope assumption. The seed cache model B predicts O1/O3 from the stipulated inputs with no additional assumption. C predicts all four using the lock-scope and lock/cache-coupling assumptions. D predicts O1/O4 using unverified scheduler-threshold and recovery assumptions. Their complete comparison is:

| Hypothesis | Descriptor (lock, cache, scheduler) | Predicted observations ↑ | Unverified auxiliaries ↓ | Novelty | Front result |
| --- | --- | ---: | ---: | ---: | --- |
| A: lock contention | (1,0,0) | 3 | 1 | 0 | retained |
| B: cache churn | (0,1,0) | 2 | 0 | 2 | retained |
| C: interacting lock/cache | (1,1,0) | 4 | 2 | 1 | retained |
| D: scheduler stalls | (0,0,1) | 2 | 2 | 2 | dominated by A, B and C |

The declared DominanceSet is exactly the two Q coordinates, with ε=0. Novelty is Hamming distance on the three Boolean flags to the preceding archive containing A only; it is an integer count from 0 to 3 and stays outside dominance. The descriptor grid has one cell per flag tuple, K=1. Exact duplicate claims are removed; none of these four is a duplicate. D’s scheduler cell is retained under the stated stepping-stone policy even though D is dominated. No D, Surprise or IlluminationSummary reading is needed in this example.

The complete front is {A,B,C}: each trades prediction coverage against auxiliary assumptions. C.18 records that front separately from the retained archive {A,B,C,D}, and its generation record names this NQD-Generate procedure and the seed/operator provenance. No front thinning is applied.

**Qualified abductive result.** For the present question about blocked threads, B.5.2 compares candidates that explain O2 with at most one unverified auxiliary assumption. A meets that stated plausibility criterion; C needs two, while B and D leave O2 unexplained. A is the qualified prime conjecture, conditional on the lock-scope assumption. Evidence that the blocked threads never wait on that lock would defeat it. Generation and the coordinate counts supply no assurance level or empirical corroboration.

**Next-use choice.** The separate C.11 question is which available diagnostic action fits a one-hour budget. Reading the existing lock traces takes one hour and addresses A’s open assumption; the combined intervention needed for C takes three hours. Under the declared criterion of addressing the current blocked-thread question within that budget, choose the trace reading and decline C’s intervention for this action. C remains a front member and D remains an archive stepping stone. This choice authorizes no performance beyond its independently applicable permission conditions.

### B.5.2.1:10a - Trade‑offs & mitigations

* **Cognitive effort.** Interpreting Pareto sets and coverage maps adds thinking overhead. *Mitigation:* standard “NQD Card” + default grids; keep **Characteristics** small in number (≤ 7). *Manager shortcut:* pick 2–3 **Q** characteristics that reflect the anomaly, then run with defaults.
* **Locality.** Novelty/diversity are **context‑local**; Cross‑context reuse requires **re‑measurement or an explicit mapping**. This pattern **does not define** Cross‑context operational controls.
* **Not a magic idea machine.** Abduction remains human/agentic; the pattern *structures* search, it does not automate insight. B.5.2 supplies the explanatory-hypothesis contribution; B.5 selects the next needed reasoning contribution.
* **Metric gaming & collinearity.** Avoid making **N** and **S** redundant by policy; when strong collinearity is detected, freeze one as informative only and record rationale in the DRR.

### B.5.2.1:11 - Related Patterns

* **Extends:** **B.5.2 Abductive Loop** (Step 2/3 operationalization).
* **Driven by / feeds:** **B.5 Canonical Reasoning Cycle**, **B.4 Evolution Loop** (Observe/Refine).
* **Uses:** **A.17/A.18** for characteristic discipline and **B.5** for choosing reasoning contributions. **May** refer to Context‑specific MAP‑Elites/novelty‑search implementations in the MethodDescription. **Independent conditions for actual Work remain applicable; this pattern adds no universal gate to theoretical comparison.** C.17 (Use‑Value / ValueGain, normative definition).
* **Respects:** **A.11** (no kernel growth beyond CHR template import + Method).

### B.5.2.1:End

---
