## C.19.1 - Bitter‑Lesson Preference (BLP)

**One-screen purpose (manager-first).**
State the empirical Bitter Lesson narrowly: in search, learning, planning, and related computational work, general methods able to use increasing compute or data have often displaced hand-engineered special cases. Treat that history as a comparison pressure, not as proof about every bearer. Here *bearer* names the candidate being compared under the scale claim or generality policy. A project may declare an analogous preference for a module, platform, organization design, evidence arrangement, or other bearer only as a separate local policy, with a scale predicate, objective vector, comparison basis, and evidence form appropriate to that bearer. Safety, cost, admissibility, uncertainty, and non-dominance remain visible; the word `general` creates no preference by itself.
**Builds on.** C.19 (E and E‑LOG), C.24 (Agent‑Tools‑CAL; **ATC‑2**), B.3 (Assurance), E.3 (Precedence), E.5 (Guard‑Rails).
**Coordinates with.** G.5 (Selector), G.8 (SoS‑LOG Bundles), G.9 (Parity), G.11 (Refresh‑Telemetry), A.0 (On‑Ramp).
**Keywords.** general-solution preference; scale‑amenability; **BLP‑waiver**; iso‑scale parity; **Scale‑Audit**; slope vector; **alpha and delta tolerances**.

**Use this when.**
Use `C.19.1` when a current choice or policy makes a scale claim or invokes a declared generality preference: a narrower special-purpose approach is preferred over a general alternative, or a general approach is preferred because its measured performance is expected to improve across a declared scale window. For search, learning, planning, and agent substrates, the empirical Bitter Lesson can supply the motivating line. For a module relation, platform, organization design, evidence-bearing episteme or work arrangement, or selected structure, state explicitly that the move is a local analogy or policy rather than an empirical Bitter-Lesson result.

The pattern governs only that scale-based comparison, preference, or waiver. It neither proves architecture adequacy nor turns a bearer label into a holon kind. If the project is merely using a bounded specialization and makes no scale advantage or durable generality claim, keep the use local under the bearer's direct pattern and stop here.

When comparing a general adaptive loop with a specialized cycle or direct repair for an `E.23` use, use `C.19.1` only if the decision relies on scale advantage or a declared generality policy. The `E.23` loop still names the object under improvement, evaluation, cost and risk account, protected trade-offs, and stop or switch condition.

#### C.19.1:0.1 - What Goes Wrong If Missed

A team treats "more agentic", "more automated", "more specialized", or "works on this benchmark" as proof that one bearer should displace a more general scale-amenable bearer. Another team repeats the opposite error: it invokes the Bitter Lesson as permission to ignore safety, cost, task-family fit, or a narrow heuristic that actually wins inside the declared scale window. In both cases, the selector loses parity, waiver, and scale-window discipline.

#### C.19.1:0.2 - What This Buys

The practitioner gets a cheap first probe before an expensive audit. It distinguishes a supported scale comparison, a declared local analogy or policy, a bounded use with no scale claim yet, and a high-stakes claim that justifies a fuller `Scale-Audit`. When comparison proceeds, task family, scale window, parity, uncertainty, cost, safety, and waiver remain explicit.

#### C.19.1:0.3 - Not This Pattern When

Apply the pattern that defines and tests the current question: `C.30` or `C.32` for architecture adequacy and synthesis, `G.5` for selected-set result declaration, `E.17` for a source-backed publication face and return to source, `E.24.PUB` for the publication occurrence and audience availability, `E.23` for repeated object-version improvement, the A.15 family for work, and `A.21` for gate decisions.

#### C.19.1:0.4 - First Output

Run one cheap scale-claim probe before selecting any `Scale-Audit`. In a short note, name the two bearer candidates and their direct patterns, the task family or receiving use, the proposed scale predicate, objective vector, comparison basis, feasible evidence form, safety boundary, and stakes. Return one of four results:

- `no scale claim yet`: use the bounded candidate under its direct pattern; no BLP preference or waiver follows;
- `local analogy or policy`: identify the non-computational bearer family, policy edition, and bearer-appropriate evidence still needed;
- `bounded scale comparison`: state the smallest parity and uncertainty method adequate for this use;
- `full Scale-Audit selected`: state why the claim, stakes, feasible evidence, and receiving use justify the added work.

A `BLP-waiver` is needed only when an actual declared generality preference would otherwise decide the use.

### C.19.1:1 - Problem frame

Bespoke computational heuristics can win locally while failing to exploit larger compute, data, or search budgets. General methods can improve across a declared scale window, but the empirical record is strongest for computational search, learning, and planning. A module organization, institution, work arrangement, or episteme does not inherit that empirical result by analogy. A project may still adopt a broader policy, but it must state the bearer-specific scale relation and evidence rather than treating all growth, reuse, or generality as one phenomenon.

Without this separation, teams either repeat the Bitter Lesson as a slogan or impose a costly machine-learning experiment recipe on bearers for which seeds, FLOPs, compute slopes, or data sweeps have no meaning.

### C.19.1:2 - Policy clauses (normative)

**BLP-1 — Probe first; select audit depth by claim and risk.**
Every BLP use starts with the cheap scale-claim probe. A scale claim is current only when the exact bearer kind and direct pattern, a recoverable scale predicate, an objective vector, a comparison basis, an evidence form, and a named receiving use are present. If any of those is absent, return `no scale claim yet`; if a local analogy or policy remains useful, label it as such and do not present it as an empirical conclusion or manufacture a `Scale-Audit`.

When the scale claim is current, choose evidence proportional to the bearer, stakes, feasible observations, and receiving use. A selector-facing superiority claim, durable reusable-bearer policy, safety-material override, or expensive irreversible choice normally justifies a fuller audit. A reversible local probe may need only a small matched comparison. The method shall preserve:

(a) **Parity and admissibility:** comparable task family or use, safety boundary, budget basis, current editions, and set-returning Pareto comparison unless a declared policy lawfully selects another operation.
(b) **Bearer-appropriate scale dimensions:** compute, data, model capacity, or freedom of action for computational methods when they actually vary; for another bearer, state its own capacity, resource, reuse, throughput, coordination, or other exact scale predicate and explain why it provides a comparable scale basis for the two candidates.
(c) **Uncertainty appropriate to the evidence:** repeated seeds or bootstrap intervals for repeatable stochastic trials when useful; measurement error, interval estimates, case comparison, or another justified form for other bearers. Do not demand seeds from an organization design or FLOPs from an episteme.
(d) **Cost, resource, and safety visibility:** report the accounts material to the decision through their direct patterns. Add B.3 only for a named assurance claim and receiving use, including when a material-reliance threshold requires such a claim.
(e) **Objective honesty:** keep quality, risk, cost, and any policy-promoted coverage or illumination coordinates separate unless their Scale permits the declared operation.
(f) **Risk-selected design:** choose a design that can answer this claim. Fractional factorial, Latin-hypercube, three-level sweeps, heteroscedasticity treatment, and repeated-seed designs are options for suitable multi-knob experiments, not a universal minimum. Record why the selected design is adequate and what it cannot establish.
(g) **Claim-matched tests:** use knee or budget-constrained regret tests only when the asserted advantage depends on a knee or dominance inside the audited window.

**BLP-2 — Preference rule with alpha and delta tolerances.**
Among admissible options with comparable assurance within `delta` and budget within `alpha`, a scale-based preference for one option over another is warranted when the first option's response over the audited range Pareto-dominates the second's, with uncertainty accounted for. If no option dominates within the evidence bounds, `C.19.1` returns `no scale-based preference`; it does not turn greater generality into an empirical winner. A separately declared project policy may break that tie in favor of a more general bearer, but the result shall be labeled as that local policy or analogy, not as the empirical Bitter Lesson, and its E/E-LOG tie-breaker and edition shall be cited. Agentic uses keep any alpha and delta values in their current `ATC.Policy`.
> **BLP‑2.1 — Valid waiver grounds (override transparency).**
> Overrides of a declared local generality preference are allowed **only** when:
> • **Admissibility override:** guard rails, ethics, or precedence make the general bearer inadmissible (`E.5`, `E.3`).
> • **Scale‑probe overturn:** under **iso‑scale parity** in the declared **ScaleWindow**, the heuristic **sustainedly outperforms** with uncertainty accounted for.
> • **Complementary bias:** the heuristic is an **inductive bias** that **improves** the general method **without blocking scale** (graceful degradation as `S` grows).
> All overrides record a **BLP-waiver** with rationale, admitted review System, direct waiver-review responsibility relation or exact A.6.RCD missing governor, and expiry or review in the DRR. Any system-role kind or assignment needed by the review Work is cited separately.

**BLP-2.2 — Task-family specialization compatibility.**
A bounded specialization that makes no scale-advantage, selector-facing superiority, durable generality, or override claim may be used under its direct pattern with an explicit task family, work target, budget guard rails, and evidence locus. It needs neither a full `Scale-Audit` nor a BLP waiver merely because it is specialized.

If a scale claim becomes current, run the cheap probe first. Select a full audit only when the claim, stakes, feasible evidence, and receiving use justify it. A specialization produced by a general substrate or described as a complementary bias is not automatically compatible: state the exact non-blocking scale relation and evidence when that fact is relied on. Low-human-overlap or newly discovered approaches remain admissible under the same bounded-use, parity, safety, cost, and evidence rules; novelty neither proves nor defeats scale amenability.

**BLP-3 — Prescription architecture is a separate question.**
The Bitter Lesson establishes no universal preference for prohibitions over positive instructions and no general right to autonomous sequencing. For tool-call planning, use `C.24` with its budget, stop, replan, and Guard-Rail rules. For another WorkPlan or normative constraint, use the A.15 planning family, `E.3`, `E.5`, and the direct policy or commitment pattern. A project may adopt a minimal-prescription policy only with its own trigger, safety boundary, evidence, and review condition; it is not a consequence of a BLP comparison.
**BLP‑4 — Heuristic‑Debt register (mandatory).**
Record **Heuristic Debt** only when an admitted heuristic functions as reusable solution-family policy, selector-facing preference, durable override of a general scale-amenable alternative, DRR-backed scale waiver, or project-side choice that claims scale advantage or BLP override. Ordinary local bounded tactics that make no reusable-bearer, scale-advantage, selector-facing, or override claim may remain local and bounded without Heuristic Debt publication. `BLP.HeuristicDebtEntry` is a `C.19.1`-local or `G.11`-linked policy and debt entry; it is not a universal `U.*` record kind unless separately admitted under `E.24.UK`, with `F.18` for naming, `C.3` for Kind semantics, and `E.9` for the decision record. For a live debt entry, record scope, admitted review System, direct debt-review responsibility relation or exact A.6.RCD missing governor, expiry or review window, and a de-hardening plan; any exact system-role kind or assignment needed by review Work remains separate. Track the entry in **CalibrationLedger** or **BCT** and cite it in SCR.

**BLP-5 — Adaptation policy is a separate question.**
The Bitter Lesson does not by itself require feedback-driven adaptation or make disabling adaptation a waiver. When adaptation is current, use `C.22.1` for the task-family adaptation claim, `E.23` for repeated object-version improvement, and `C.24` for tool-call planning and replanning, together with the applicable privacy and Guard-Rail patterns. A product policy may require or prohibit adaptation, but that result needs its own objective, evidence, risk boundary, and review date.
**BLP‑6 — Precedence & safeguards.**
BLP is constitutional (instantiates **P‑10**, **P‑11**, **P‑7**, and **P‑1**), but **does not supersede Guard‑Rails (E.5) or precedence rulings (E.3)**. Where a declared **NQD** or **C.19 E‑LOG** policy promotes illumination into dominance, use that lens for the audited window.

**BLP‑7 — Publication discipline.**
When a durable `Scale-Audit` is actually performed, its artifacts **SHALL** be exported to **G.11** with the used edition pins, uncertainty method, alpha and delta tolerances when current, ComparatorSet, policy reference, and qualification window. A `no scale claim yet` or local bounded-use exit creates no audit package.

### C.19.1:3 - Conformance Checklist (CC-BLP)

1. The cheap scale-claim probe names the bearer kind and direct pattern, task family or receiving use, scale predicate, objective vector, comparison basis, feasible evidence, safety boundary, and stakes.
2. The result says `no scale claim yet`, `local analogy or policy`, `bounded scale comparison`, or `full Scale-Audit selected`; it does not hide the choice of audit depth.
3. A performed comparison uses parity, current editions, explicit uncertainty, material resource and safety accounts, and lawful Pareto or declared policy operations.
4. The evidence method fits the bearer. Compute/data sweeps, seeds, bootstraps, and factorial or Latin-hypercube designs appear only when they answer the actual claim.
5. Non-dominance returns no empirical scale preference. Any generality tie-break is identified as a separately declared local policy.
6. A waiver identifies the policy it overrides, rationale, admitted review System, direct responsibility relation or exact missing governor, and expiry or review window.
7. A live Heuristic Debt entry meets the bounded `BLP-4` trigger; ordinary local tactics create no debt record.
8. Prescription architecture and adaptation policy are routed through their direct patterns rather than reported as consequences of BLP.
9. An actual durable audit is exported to `G.11`; a bounded-use or no-claim exit is not padded into an audit artifact.
10. A narrower specialist bearer names its task family, work target, and the exact scale, waiver, or bounded-use ground relied on.

### C.19.1:4 - Anti-patterns & remedies

- **Slogan as evidence.** `General`, `agentic`, or `Bitter Lesson` is treated as proof. Repair with the cheap probe and an actual comparison basis.
- **Analogy as empirical result.** A module relation, organization, or episteme is assigned compute/data scaling semantics. State a local analogy or policy and use a bearer-appropriate predicate and evidence form.
- **Universal experiment recipe.** Every claim receives seeds, FLOPs, and a multi-factor design. Select the smallest method that can answer the actual risk-bearing claim.
- **General wins by non-dominance.** Error bars overlap, so the more general option is declared superior. Return no empirical scale preference or cite a separate tie-break policy.
- **Single-winner leaderboard.** Hidden budget mixing or scalarization replaces Pareto comparison. Restore comparable windows, objective coordinates, uncertainty, and policy identifiers.
- **Debt without trigger.** A local bounded tactic is entered into Heuristic Debt. Apply the `BLP-4` trigger before creating the entry.
- **Elegant-math override.** A specialized mathematical lens is selected because of elegance or prestige while scale advantage is live. Use the proportionate BLP comparison; otherwise keep the lens local under the `C.29` stop condition.

### C.19.1:5 - Archetypal grounding (post-2015; informative)

Source-use relation and source-currentness: the following example groups are informative grounding for computational scale comparison, not a current SoTA table and not evidence for non-computational bearer families. A concrete BLP claim still needs its task family or receiving use, comparator set, current alpha and delta tolerances when used, budget, material safety and admissibility boundary, any current assurance boundary, and source-currentness row named by the applying pattern or parity harness.

* **LLMs:** prompt programs, **retrieval-augmented** policies, and **MoE** policies compared with narrow task-specific pipelines; set-returning selection across editions and budgets.
* **RL and planning:** model-based optimization and general agents compared with hand-coded controllers, subject to alpha and delta tolerances and safety.
* **Preference learning:** comparisons between **RLHF** and **DPO** families.
* **QD and OEE:** MAP-Elites, **CMA-ME**, **DQD**, and **QDax**; **POET** and **Enhanced-POET**; illumination remains **report-only telemetry** unless policy promotes it.

### C.19.1:5.1 - SoTA-Echoing

| Source or source family | Adopted FPF move | Rejected overread | Practitioner implication |
|---|---|---|---|
| Yousefi and Collins, `Learning the Bitter Lesson: Empirical Evidence from 20 Years of CVPR Proceedings`, arXiv:2410.09649, as current empirical pressure around Sutton's 2019 Bitter Lesson. | Treat scale-amenable computational approaches in machine learning as a live empirical comparison pressure. | The same empirical result automatically governs modules, organizations, work arrangements, epistemes, or every other bearer. | For a computational claim, test the declared task family and scale window. For another bearer, label the move as local analogy or policy and provide its own scale predicate and evidence. |
| Kaplan et al., `Scaling Laws for Neural Language Models`, arXiv:2001.08361, and Hoffmann et al., `Training Compute-Optimal Large Language Models`, arXiv:2203.15556. | Keep compute, data, model size, budget, and scale-window relations explicit when a bearer is claimed to improve with scale. | Parameter count, compute spend, or one benchmark substitutes for the audited objective vector. | State the swept dimensions, alpha and delta tolerances when used, CI or another justified uncertainty form, and budget window before preferring the general bearer. |
| Lu et al., `The Bitter Lesson of Diffusion Language Models for Agentic Workflows: A Comprehensive Reality Check`, arXiv:2601.12979. | Treat current agentic-substrate claims as evaluation-sensitive and task-family-sensitive, especially when efficiency hype competes with reliability. | "More agentic" or "more efficient backbone" proves better workflow performance. | For agent-loop or substrate selection, use `G.9` for parity, `C.19.1` for a current scale-advantage or declared generality-policy claim, and `E.23` only for repeated object-version improvement; preserve task-family evaluation, protected trade-offs, and stop/switch conditions. |

### C.19.1:6 - Payload - exports

`BLP.Policy@Context` is an editioned local policy row, not a universal kind. It records:

`<scopeBranch={empirical-computational | declared-local-analogy}, PreferenceDefault={neutral | declared-prefer-general}, alpha?, delta?, scaleProbeResult?, proportionateComparisonMethod?, fullScaleAuditRef?, WaiverRegister?, E-LOG policyIds?, G.11 telemetryPins?>`.

The row omits fields that are not current. `PreferenceDefault=declared-prefer-general` identifies a local tie-break policy, not an empirical conclusion. A full audit reference appears only after the risk-selected audit exists.

### C.19.1:7 - Relations

**Depends on:** **G.5** and **G.9** (selector and parity), **G.11** (refresh telemetry), **A.15.1** for dated work, **A.15.2** for work plans, **B.1.6** for resource and cost aggregation, **C.16** for measurement, and **A.10** for provenance, **C.18** (NQD‑CAL), **C.19** (E and E‑LOG), **F.7** and **F.9** (bridges, CL, Φ, and Ψ). **Constrained by:** **E.5** Guard‑Rails and **E.3** precedence.

#### C.19.1:7.1 - C.32 architecture-synthesis use relation

When using `C.32` to generate candidate architectures, `C.19.1` applies only if a claim about a candidate asserts scale advantage or invokes a declared local generality policy. For a universal module relation, platform, organization design, evidence arrangement, or selected structure, that branch is a project analogy or policy: the empirical machine-learning literature is not proof. Name the exact bearer and its direct pattern, the holon under change when one is current, the bearer-specific scale predicate, objective vector, comparison basis, feasible evidence, admissibility boundary, and intended receiving use.

BLP neither selects the architecture nor turns method-family, practice, role-side, or culture wording into a holon kind. If the candidate merely removes parts, carries several functions, or is described as reusable, with no recoverable scale claim or declared generality-policy claim, keep the question in `C.32` and `C.31`; return `no scale claim yet` rather than manufacturing an audit. A TRIZ-style ideality move enters BLP only when the declared comparison actually relies on scale amenability inside a named window.

#### C.19.1:7.2 - C.29 mathematical-lens use relation

When a mathematical lens is chosen over a general, scale-amenable bearer because it is elegant, specialized, or theoretically prestigious, and a scale-advantage or declared generality-policy claim is current, `C.19.1` governs the scale-advantage and preference claim. A `C.29` application may state `CandidateMathObject`, `LensMappingMode`, `PreservedStructure`, `LostStructure`, `LensUseBoundaryValue`, `declaredLensUse`, and `StopCondition`, with optional `blockedLensOverread?` for an overread that passes F.19's plausible-reader test; it does not supply BLP compatibility, scale dominance, or waiver evidence.

If scale advantage or a declared generality policy is live, start with the cheap probe and cite the resulting bounded comparison, risk-selected `Scale-Audit`, or applicable `BLP-waiver`. If neither is live, keep the mathematical lens local and bounded by its `C.29` stop condition.

> *Memory hook.* **Test what scales; label policy when evidence does not decide.**

When choosing between a general adaptive loop, a specialized object-family cycle, or a mixed operation-family set for an `E.23` use, `C.19.1` applies only when the decision relies on scale advantage or a declared generality policy. Start with the cheap probe. Compare the declared characteristic values for material resources, tools and instruments, adaptation attempts, skilled attention, rework or delay, risk exposure, and avoided loss on their admitted scales; keep them separate, reject a dominated option, and use the declared project policy to choose or hold when no option dominates. Net-cost arithmetic is permitted only after every term has been converted to one declared unit through an admissible conversion whose basis, uncertainty, and scope remain visible. Repeated automation alone does not satisfy BLP; the record still names the object under improvement, evaluation, protected trade-offs, bounded cost and risk condition, and stop or switch condition. If neither a scale claim nor a declared generality policy is current, `E.23` proceeds without a BLP audit or waiver.

### C.19.1:End

