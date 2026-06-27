## C.19.1 - Bitter‑Lesson Preference (BLP)

**One‑screen purpose (manager‑first).**
Establish, at **governing policy** level, the empirical **Bitter Lesson**: **prefer general, scale‑amenable solution bearers for admitted holons**. A scale-amenable bearer may be a method, module, platform, system, agent substrate, organization design, episteme-bearing practice, or other admitted holon structure that improves with more data, compute, capacity, usable resources, reuse, or freedom of action. Prefer it over bespoke narrow heuristics when safety, guard-rail fit, and admissibility are comparable. Exceptions require a transparent **Scale‑Audit** under the parity harness.

**Builds on.** C.19 (E and E‑LOG), C.24 (Agent‑Tools‑CAL; **ATC‑2**), B.3 (Assurance), E.3 (Precedence), E.5 (Guard‑Rails).
**Coordinates with.** G.5 (Selector), G.8 (SoS‑LOG Bundles), G.9 (Parity), G.11 (Refresh‑Telemetry), A.0 (On‑Ramp).
**Keywords.** general-solution preference; scale‑amenability; **BLP‑waiver**; iso‑scale parity; **Scale‑Audit**; slope vector; **alpha and delta tolerances**.

**Use this when.**
Use `C.19.1` when a project prefers a narrower special-purpose solution over a more general scale-amenable bearer, or when it claims that a general bearer should be preferred because it scales. In architecture synthesis, this includes a universal module, platform, reusable method family, agent substrate, organization design, episteme-bearing practice, or other admitted holon structure proposed to carry more functions or improve with scale. `C.19.1` supplies comparison and waiver discipline; it does not make the candidate architecture adequate.

When `E.23` selects between a general adaptive agent loop, a specialized object-family cycle, a simpler direct repair, or a reusable harness substrate, `C.19.1` governs only the scale-amenability and waiver claim. The `E.23` loop still must name the object under improvement, evaluation, cost and risk account, protected trade-offs, and stop or switch condition.

#### C.19.1:0.1 - What Goes Wrong If Missed

A team treats "more agentic", "more automated", "more specialized", or "works on this benchmark" as proof that one bearer should displace a more general scale-amenable bearer. Another team repeats the opposite error: it invokes the Bitter Lesson as permission to ignore safety, cost, task-family fit, or a narrow heuristic that actually wins inside the declared scale window. In both cases, the selector loses parity, waiver, and scale-window discipline.

#### C.19.1:0.2 - What This Buys

The practitioner gets one bounded comparison move: name the narrower bearer, the general bearer, the task family or admitted holon, the audited scale window, the parity basis, and the waiver or preference result. This makes a specialization admissible when it is genuinely justified, and makes a general substrate preference admissible when scale evidence, safety, and cost are comparable.

#### C.19.1:0.3 - Not This Pattern When

Do not use `C.19.1` to prove that an architecture candidate is adequate, to publish a selected set, to run the improvement loop, to plan or perform work, or to claim a gate decision. Use the direct owner for that question: `C.30`/`C.32` for architecture adequacy and synthesis, `G.5` for selected-set publication, `E.23` for object-version improvement, the A.15 family for work, and `A.21` for gate decisions.

#### C.19.1:0.4 - First Output

The first useful output is either a `Scale-Audit` pointer or a `BLP-waiver` record. It states the competing bearers, task family or holon scope, scale dimensions, comparator set, safety/admissibility posture, alpha and delta tolerances, and the reason the result is preference, waiver, or no BLP claim yet.

### C.19.1:1 - Problem frame

Bespoke heuristics can win locally while failing to scale. General solution bearers, including search, learning, planning, platforms, reusable modules, organization forms, and episteme-bearing practices, can improve with scale and transfer across declared bridges and planes. Without a standing policy, selectors drift toward bespoke local heuristics and single-winner leaderboards, violating parity and admissible order relations.

### C.19.1:2 - Policy clauses (normative; synchronized with Core)

**BLP‑1 — Scale‑Audit requirement.**
Any DRR that selects a **narrower hand‑engineered** method, module, platform, system form, organization form, episteme-bearing practice, or other solution bearer over a **general scale-amenable** alternative while claiming scale advantage, BLP override, selector-facing preference, publication-facing superiority, or durable project-side preference **MUST** include a **Scale‑Audit**:
(a) **Parity harness**: equal **FreshnessWindows**, a common **ComparatorSet**, replicate counts, seed records, and **set-returning** evaluation; **Dominance = ParetoOnly** unless a CAL policy says otherwise (policy‑id cited).
(b) **Budget sweeps**: vary **compute**, **data**, and **FoA** within a fixed safety envelope; **pin** any unsweepable knob and record the invariant.
(c) **Slopes and uncertainty**: report ∂quality over ∂compute, ∂quality over ∂data, and, where applicable, ∂coverage over ∂FoA, with **confidence intervals, error bars, edition pins, and policy pins** in telemetry. Use **bootstrapped confidence intervals** or repeated‑seed estimates; disclose heteroscedasticity handling.
(d) **Resources**: publish **Resrc‑CAL** accounts for time, energy, FLOPs, and assurance deltas under B.3.
(e) **Objective vector**: list quality, risk, cost, and only policy-promoted illumination or coverage telemetry metrics.
(f) **DoE recipe**: for ≥2 active knobs, apply a **fractional factorial** or **Latin‑hypercube** with ≥ 3 levels per knob to avoid aliasing; justify any lower design.
(g) **Knee & regret tests**: if claiming a heuristic wins, show either (i) a **knee** inside the audited window for the general method (per SLL‑5 policy thresholds) or (ii) **budget‑constrained regret** over the sweep where the heuristic dominates within CI.

**BLP‑2 — Preference rule with alpha and delta tolerances.**
Among admissible options with comparable assurance within **delta** and budget within **alpha**, prefer the bearer whose **slope vector** **Pareto‑dominates** over the audited range; if no dominance within error bounds, prefer the **more general** bearer; otherwise resolve by the **E and E‑LOG** tie‑breakers declared in policy. Agentic contexts implement this as **ATC‑2**; **BLP_delta_alpha_delta** values live in **ATC.Policy**.

> **BLP‑2.1 — Valid waiver grounds (override transparency).**
> Overrides of BLP‑2 are allowed **only** when:
> • **Admissibility override:** guard rails, ethics, or precedence make the general bearer inadmissible (`E.5`, `E.3`).
> • **Scale‑probe overturn:** under **iso‑scale parity** in the declared **ScaleWindow**, the heuristic **sustainedly outperforms** with uncertainty accounted for.
> • **Complementary bias:** the heuristic is an **inductive bias** that **improves** the general method **without blocking scale** (graceful degradation as `S` grows).
> All overrides record a **BLP‑waiver** with rationale, responsible role, and expiry or review in the DRR.

**BLP‑2.2 — Task-family specialization compatibility.**
A bounded specialization remains **BLP-compatible** when it is produced by a **general, scale-amenable substrate**, when it acts as a complementary bias that does not block scale, or when it survives the ordinary **BLP** comparison discipline on the same declared task family and work target. The specialization may be a method, module, platform variant, system form, organization form, agent behavior, or episteme-bearing practice. If the user is not claiming scale advantage or overriding a general bearer, a bounded specialization may be used with explicit task family, work target, budget guard rails, and evidence source or evidence locus. Full **Scale-Audit** is triggered by scale-advantage, override, selector-facing publication, publication-facing superiority, or durable reusable-bearer claim, not by the mere existence of specialization. `BLP` therefore governs whether the narrower current bearer was generated, compared, audited, waived, and overridden admissibly; it does **not** require the final local behavior at every moment to look maximally generic.

Low-human-overlap or newly discovered approaches remain admissible when the task family, budget guard rails, and evidence source or evidence locus are explicit by value and the same `Scale‑Audit`, alpha and delta, waiver, and override discipline is preserved.
**BLP‑3 — Minimal‑prescription default.**
Author **rules‑as‑prohibitions** (negative constraints) instead of stepwise scripts; encode limits in **Φ policy tables** and **Φ_plane** and allow agents to **sequence autonomously** within those constraints. Scripts are permissible only when mandated by safety or regulation, or with compelling DRR evidence reviewed under E.3 and E.5.

**BLP‑4 — Heuristic‑Debt register (mandatory).**
Record **Heuristic Debt** only when an admitted heuristic functions as reusable solution-family policy, selector-facing preference, durable override of a general scale-amenable alternative, DRR-backed scale waiver, or project-side choice that claims scale advantage or BLP override. Ordinary local bounded tactics that make no reusable-bearer, scale-advantage, selector-facing, or override claim may remain local and bounded without Heuristic Debt publication. `BLP.HeuristicDebtEntry` is a `C.19.1`-local or `G.11`-linked policy and debt entry; it is not a universal `U.*` record kind unless separately admitted through `F.18`, `C.3`, and `E.9`. For a live debt entry, record scope, responsible role, expiry or review window, and a de-hardening plan; track in **CalibrationLedger** or **BCT** and cite in SCR.

**BLP‑5 — Continuous-learning discipline.**
Where product policy allows, enable **feedback‑driven adaptation** (preference learning, critique loops) within Guard‑Rails and privacy controls; disabling adaptation requires DRR justification and review date.

**BLP‑6 — Precedence & safeguards.**
BLP is constitutional (instantiates **P‑10**, **P‑11**, **P‑7**, and **P‑1**), but **does not supersede Guard‑Rails (E.5) or precedence rulings (E.3)**. Where **NQD** or **C.19 E‑LOG** promotes illumination into dominance, **BLP adopts that lens** for the audited window.

**BLP‑7 — Publication discipline.**
Scale‑Audit artefacts **SHALL** be exported to **G.11** with edition pins, CI level, alpha and delta tolerances, ComparatorSet, and **BLP.Policy@Context** reference so downstream selectors can reuse evidence without re‑running audits.

### C.19.1:3 - Conformance Checklist (CC‑BLP)

1. **Alpha and delta tolerances** declared in DRR or via policy profile, with CI level stated.
2. DRR includes a **Scale‑Audit** (BLP‑1a through BLP‑1g) with slopes, confidence intervals, edition pins, policy pins, and Resrc‑CAL.
3. Selection cites **BLP‑2** and precedence checks.
4. Any heuristic that meets the BLP‑4 trigger is recorded as a `BLP.HeuristicDebtEntry` with scope, responsible role, expiry or review window, and de‑hardening plan; ordinary local bounded tactics do not create a debt entry.
5. Authoring defaults to **rules‑as‑prohibitions**; deviations are DRR‑justified and safety-bounded.
6. **Resrc‑CAL** accounts and assurance deltas reported.
7. **Replicate counts, seed records, and confidence intervals** recorded for slope estimates; heteroscedasticity handling disclosed.
8. Audit artefacts exported to **G.11** with **BLP.Policy@Context** id.

9. When a narrower specialist bearer is selected or returned for one declared task family, the record names the task family, work target, holon structure under comparison when current, and the Scale‑Audit, waiver, or override ground that keeps the choice BLP‑compatible.

### C.19.1:4 - Anti‑patterns & remedies

Single‑winner leaderboards; hidden budget mixing; promoting illumination into dominance **without policy**; missing edition pins; heuristics without expiry; slope estimates without CI or with aliased designs → **remedy** with G.9 parity + edition pins, explicit **policy‑ids**, DRR publication, **Heuristic‑Debt** entries, and BLP‑1f DoE discipline.

**Elegant-math override.** A specialized or elegant mathematical lens is selected over a more general or scale-amenable alternative because of elegance or prestige while scale advantage is live. Remedy: use BLP scale-audit when the claim is scale advantage; otherwise mark the lens as local and bounded by `C.29` stop condition.

### C.19.1:5 - Archetypal grounding (post-2015; informative)

Source-use relation and source-currentness: this section is informative grounding for scale-amenable bearer comparison, not a current SoTA table. A concrete BLP claim still needs the local context, comparator set, alpha and delta tolerances, budget, assurance boundary, and source-currentness row named by the applying pattern or parity harness.

* **LLMs:** prompt programs, **retrieval-augmented** policies, and **MoE** policies compared with narrow task-specific pipelines; set-returning selection across editions and budgets.
* **RL and planning:** model-based optimization and general agents compared with hand-coded controllers, subject to alpha and delta tolerances and safety.
* **Preference learning:** **RLHF <-> DPO** families.
* **QD and OEE:** MAP-Elites, **CMA-ME**, **DQD**, and **QDax**; **POET** and **Enhanced-POET**; illumination remains **report-only telemetry** unless policy promotes it.

### C.19.1:5.1 - SoTA-Echoing

| Source or source family | Adopted FPF move | Rejected overread | Practitioner implication |
|---|---|---|---|
| Yousefi and Collins, `Learning the Bitter Lesson: Empirical Evidence from 20 Years of CVPR Proceedings`, arXiv:2410.09649, as current empirical pressure around Sutton's 2019 Bitter Lesson. | Treat general scale-amenable approaches as a live preference pressure that must be tested through declared comparison, not as folklore. | "General" or "Bitter Lesson" is proof without task-family, safety, cost, and scale-window evidence. | Use `Scale-Audit` or `BLP-waiver` before turning the slogan into selector-facing preference. |
| Kaplan et al., `Scaling Laws for Neural Language Models`, arXiv:2001.08361, and Hoffmann et al., `Training Compute-Optimal Large Language Models`, arXiv:2203.15556. | Keep compute, data, model size, budget, and scale-window relations explicit when a bearer is claimed to improve with scale. | Parameter count, compute spend, or one benchmark substitutes for the audited objective vector. | State the swept dimensions, alpha and delta tolerances, CI, and budget window before preferring the general bearer. |
| Lu et al., `The Bitter Lesson of Diffusion Language Models for Agentic Workflows: A Comprehensive Reality Check`, arXiv:2601.12979. | Treat current agentic-substrate claims as evaluation-sensitive and task-family-sensitive, especially when efficiency hype competes with reliability. | "More agentic" or "more efficient backbone" proves better workflow performance. | Keep agent-loop or substrate selection under `E.23`, `G.9`, and `C.19.1` with task-family evaluation, protected trade-offs, and stop/switch conditions. |

### C.19.1:6 - Payload — exports

`BLP.Policy@Context` (UTS row; editioned):
`<PreferenceDefault, alpha and delta tolerances plus CI, Scale-Audit recipe (G.9 link; DoE), WaiverRegister{reason, responsibleRoleRef, expiry}, E-LOG lens policy-ids, ATC.PolicyRef? (agentic), G.11.TelemetryPins>`.

**UTS row template (conceptual; pencil‑ready).**
`BLP.Policy@Context := PreferenceDefault=(prefer-general or neutral), tolerances=(alpha=..., delta=..., CI=...), Scale-Audit=(parity=G.9; sweep=S={...}; DoE=factorial or LHD; kneeTest=policy-tau), WaiverRegister=[{reason=..., responsibleRoleRef=..., expiry=...}], E-LOG=(policyIds=...), ATC.PolicyRef=(...), TelemetryPins=(edition=..., seeds=..., comparatorSet=...)`.

### C.19.1:7 - Relations

**Depends on:** **G.5** and **G.9** (selector and parity), **G.11** (refresh telemetry), **C.5** (Resrc‑CAL), **C.18** (NQD‑CAL), **C.19** (E and E‑LOG), **F.7** and **F.9** (bridges, CL, Φ, and Ψ). **Constrained by:** **E.5** Guard‑Rails and **E.3** precedence.

#### C.19.1:7.1 - C.32 architecture-synthesis use relation

When `C.32` generates candidate architectures, `C.19.1` applies to claims that one general bearer, universal module, platform, method family, agent substrate, organization design, episteme-bearing practice, or other admitted holon structure can carry more functions or improve with scale. BLP does not select the architecture. It requires the candidate to name the holon under change, function-bearing transfer, selected structure changed, architecture characteristics improved and worsened, scale window, admissibility boundary, and waiver or audit basis.

For TRIZ-style ideality, BLP supports the move only when the general bearer remains scale-amenable inside the declared window. If the candidate merely removes parts, it belongs to `C.32` and `C.31` until it has a scale claim; it is not a BLP proof.

#### C.19.1:7.2 - C.29 mathematical-lens use relation

When a mathematical lens is chosen over a general, scale-amenable bearer because it is elegant, specialized, or theoretically prestigious, `C.19.1` governs the scale-advantage and preference claim. A `C.29` application may state `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `LensUseAdmissibilityValue`, `admissibleUse`, `nonAdmissibleUse`, and `StopCondition`; it does not supply BLP compatibility, scale dominance, or waiver evidence.

If scale advantage is live, cite a `Scale-Audit` or `BLP-waiver`. If scale advantage is not live, keep the mathematical lens local and bounded by its `C.29` stop condition.

> *Memory hook.* **Prefer what scales; explain when you don’t.**

When `E.23` selects between a Ralph-like general adaptive loop, a specialized object-family cycle, or a mixed operation-family set, `C.19.1` governs the BLP comparison and waiver discipline. The local `E.23` cost and risk prompt `token_or_compute_cost + tool_cost + adaptation_attempt_cost + human_supervision_cost + rework_cost - avoided_loss_value` is not a scalar quality score; it is a practical accepted-work cost account for deciding whether the next pass, added operation, or method-family switch is BLP-compatible. Repeated automation alone does not satisfy BLP; the record must still name the object under improvement, object-under-improvement evaluation, protected trade-offs, bounded cost and risk condition, and stop or switch condition.

### C.19.1:End

