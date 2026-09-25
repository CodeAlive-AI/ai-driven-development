## E.2 - FPF's Eleven Pillars and Bitter-Lesson Preference (BLP)

### E.2:1 - Problem frame
Use the Eleven Pillars in §4 to assess whether an FPF rule or artifact meets its constitutional obligations. Use the separate BLP policy in §6 when a computational choice claims a scale/generalization advantage or invokes a declared local generality policy: start with C.19.1's cheap scale-claim probe. An ordinary bounded fixed procedure can stop with its task-specific justification; specialization alone creates no scale audit, heuristic-debt entry or waiver. Independently applicable assurance or oversight requirements retain their own checks.

Pattern E.1 set the FPF mission as an **operating system for thought**. To turn that mission into a durable architecture, FPF needs a small, explicit constitution - principles that remain stable while everything built on top of them can evolve. Without such invariants, domain silos, vocabulary drift, and tool-centric shortcuts quickly erode coherence and reproducibility across disciplines.

The pillars are also the first-principles basis of FPF. They are the minimal commitments from which pattern-level work derives: decisive structure, teachability, maturing formality, open kernel, layering, register discipline, practical payoff, cross-scale consistency, explicit state, open-ended evolution, and SoTA renewal. Later patterns can support this basis by making a concrete argument about pillar support more inspectable; they do not replace pillar authority.

### E.2:2 - Problem
Frameworks without binding first principles wobble between two extremes: rigid dogmas that kill adaptation and amorphous guidelines that invite cognitive chaos. In either case, reasoning fragments, auditability collapses, and physical impact suffers.

### E.2:3 - Forces
| Force                          | Tension                                                |
| ------------------------------ | ------------------------------------------------------ |
| **Foundational Stability**     | Immutable core ↔ perpetual adaptation to new knowledge |
| **Cognitive Load**             | Minimal elegance ↔ comprehensive coverage              |
| **Rigor vs Accessibility**     | Formal soundness ↔ intuitive entry for non‑specialists |
| **Universality vs Modularity** | Domain‑agnostic scope ↔ plug‑in extensibility          |
| **Pragmatic Grounding**        | Abstract invariants ↔ measurable, falsifiable outcomes |

### E.2:4 - Solution
FPF rests on **eleven non‑negotiable pillars**. Each pillar is a binding constraint that every artefact, pattern, and design‑rationale record (DRR) **must** honour. Together they form the load‑bearing structure that guarantees evolvability, cross‑scale coherence, and didactic clarity.

| ID       | Pillar                         | Essence                                                                                                                   |
| -------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **P‑1**  | **Cognitive Elegance**         | Highlight decisive structure, eliminate ornamental formalism; separate data governance from thinking.                     |
| **P‑2**  | **Didactic Primacy**           | Human comprehension outranks theoretical or tooling purity.                                                               |
| **P‑3**  | **Scalable Formality**         | A single artefact can mature step‑by‑step from informal guess to formally assured state without forks or rewrites.        |
| **P‑4**  | **Open‑Ended Kernel**          | The Kernel contains only meta‑concepts; all domain knowledge lives in external patterns.                       |
| **P‑5**  | **FPF Layering**           | Patterns are modular, declarative extensions that can be added, replaced, or removed without destabilising the core. |
| **P-6**  | **Lexical Stratification**     | Every core concept is expressible in four registers: plain name, technical term, admitted U-kind or governed value name, and mathematical symbol.  |
| **P‑7**  | **Pragmatic Utility**          | Proofs, metrics, and models exist to achieve real‑world objectives; falsification is rewarded over confirmation.          |
| **P‑8**  | **Cross‑Scale Consistency**    | Composition algebras (aggregation, boundary, emergence) are invariant across material systems, knowledge, and methods.    |
| **P‑9**  | **State Explicitness**         | Every artefact declares its state (`design‑time`, `run‑time`, etc.); transitions are cheap, traceable, auditable.         |
| **P‑10** | **Open‑Ended Evolution**       | Every entity is expected to evolve indefinitely; cycles must remain cheap, safe, and cognitively rewarding.               |
| **P‑11** | **State‑of‑the‑Art Alignment** | The kernel and extension domain-specific patterns track reliable contemporary knowledge and update when the SoTA advances.                     |

When a pillar-impact argument relies on mathematical structure, scale behavior, optimization, uncertainty, invariance, obstruction, or other first-principles modeling support, the applicable mathematical-lens use support path is `C.29`. The pillar claim remains governed by `E.2`; `C.29` only states the mathematical lens, preserved and lost structure, admissible use, neighboring-pattern exits, and stop condition that make the pillar support inspectable.

> Any DRR that contradicts a pillar must first amend this constitutional pattern.

### E.2:5 - Conformance Checklist

| ID         | Requirement                                                                                                                       | Purpose                               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **CC‑P‑1** | Every architectural pattern **must** list which pillar(s) it instantiates or refines.                                             | Guarantees constitutional grounding.  |
| **CC‑P‑2** | Every DRR proposing a normative change **must** include a “Pillar Impact Analysis.”                                               | Makes constitutional review explicit. |
| **CC‑P‑3** | Tooling and pedagogical artefacts **should** document which pillar(s) shape their design.                                         | Upholds P‑2 (Didactic Primacy).       |
| **CC‑P‑4** | A pattern is conformant only if its invariants reference **≥ 3** pillars; the substance of each claimed alignment must be assessed separately. | Requires explicit pillar links without treating their count as evidence of adequate realization.   |
| **CC‑P‑5** | When a choice claims scale/generalization advantage in a computational domain, or invokes a separately declared local generality policy, authors **MUST** apply BLP to the usable response over its declared budget range and receiving conditions. Ordinary bounded specialization alone activates no scale audit, debt entry or waiver. | Keeps scale preference tied to usable performance and its actual claim. |
| **CC‑P‑6** | A pillar-impact analysis that relies on mathematical structure, scale behavior, optimization, uncertainty, invariance, obstruction, or other first-principles modeling support is complete only when that support is ordinary accepted local theory, a cited `C.29` output, or a named neighboring-pattern output for evidence, causal, bridge, assurance, measurement, work, decision, publication, or admission claims. | Keeps mathematical support for pillars inspectable without letting `C.29` revise pillar authority. |

### E.2:6 - Policy — Bitter‑Lesson Preference (BLP)

**Intent and activation.** In search, learning, planning and related computational work, investigate a claimed advantage from increased compute, data or search capacity under C.19.1. The empirical Bitter Lesson motivates that comparison; it does not decide every choice between a specialized and a general approach. An analogy or generality preference for another bearer needs a separately declared local policy, receiving purpose, scale predicate and evidence basis. Ordinary bounded specialization can stop with its task-specific justification.

**BLP-1 — Claim-matched comparison and audit.** Begin an activated BLP use with C.19.1's cheap scale-claim probe. Name the candidate, task/use, scale variable, objective, usable budget range, receiving conditions and evidence form. Missing comparison premises return `no scale claim yet`; select evidence depth by claim and risk. An independently activated profile can require a fuller Scale-Audit. That audit retains:

* (a) **Parity and admissibility:** comparable tasks, budget basis, editions, freshness and risk/safety envelope. Use G.5/G.9 when their selector/parity contracts apply. Pareto comparison is the default over the declared objective vector; another comparison needs a lawful declared policy under E.3.
* (b) **Usable budgets:** vary the dimensions actually relevant to the claim—compute, data or freedom of action where applicable—and pin held conditions. Compare only over the range available to the receiving use; extrapolation needs its own basis.
* (c) **Response and uncertainty:** report performance over that range with an uncertainty treatment appropriate to the evidence. Slopes may characterize response but cannot replace its level, admissibility or receiving floor. Repeatable stochastic trials retain seeds/replicates and confidence intervals where used; deterministic derivations retain their assumptions and validity bounds.
* (d) **Resources and assurance:** retain decision-material resource accounts through A.15.1, A.15.2, B.1.6, C.16 and A.10 as applicable. A named assurance claim uses B.3; independently applicable assurance and oversight requirements remain binding.
* (e) **Objectives and tolerances:** declare quality, risk, cost and any illumination coordinate promoted by an explicit CAL policy. State units and the budget/assurance tolerances α/δ used by the comparison. Publish the actual audit's edition and policy pins through G.11.

**BLP-2 — Usable-performance preference.** Among admissible options under the receiving conditions, with comparable assurance within δ and budget within α when those tolerances are used, prefer the option whose response over the usable audited range Pareto-dominates the other's, accounting for uncertainty. If neither dominates, return `no scale-based preference`. A preference for greater generality can then follow only from a separately declared project policy under E.3; label that basis and its costs instead of reporting an empirical winner.

**BLP-3 — Task-appropriate prescription.** Positive procedures and prohibitions are both available under their actual task or control needs. A mandated safety procedure keeps its force. Minimal prescription and autonomous sequencing need their own justified policy, authority and guards; neither follows from a scale comparison. Ordinary use of a positive procedure requires no BLP waiver solely because a general search alternative exists.

**BLP-4 — Conditional heuristic debt.** Apply C.19.1's debt branch when an admitted heuristic carries a durable scale/generality preference, reusable solution-family policy, selector-facing preference or override within an activated BLP use. Retain scope, review responsibility, expiry/review window, replacement target and de-hardening plan in CalibrationLedger/BCT and SCR as applicable. A bounded task-specific tactic that makes none of those claims is not debt merely because it is specialized.

**BLP-5 — Separately authorized adaptation.** Enable, require or prohibit adaptation under the product's objective, evidence, permission, change authority and risk/Guard-Rail conditions. A fixed method needs no BLP adaptation waiver solely for remaining fixed. A product policy that actually requires adaptation or its review retains that obligation and its exception rule.

**BLP‑6 — Precedence & Safeguards.** BLP combines governance and architectural principles; classify each compared principle under E.3 rather than assigning one class to the whole policy. It is instantiated by Pillars **P‑10 (Open‑Ended Evolution)**, **P‑11 (SoTA Alignment)**, **P‑7 (Pragmatic Utility)**, and **P‑1 (Cognitive Elegance)**. It does **not** override applicable safety and ethics requirements, **E.5** Guard‑Rails, or E.3 precedence rulings; where BLP conflicts with Guard‑Rails, **Guard‑Rails prevail**. When **NQD/E/E‑LOG** elevates illumination to dominance for exploration mandates, BLP **adopts that lens** rather than overriding it.

*Informative SoTA contexts (post‑2015):* set-returning selection across **LLM prompt‑programming vs fine‑tuned task models**; **preference‑learning families (RLHF ↔ DPO)**; **QD archives (MAP‑Elites/CMA‑ME/DQD/QDax)**; **open‑ended environment–method co‑evolution (POET‑class)**; **offline RL vs Decision Transformer parity**; and beyond ML, **optimization/control** (model‑based planning vs hand‑tuned controllers) and **simulation‑based inference** in the sciences. These are **illustrative only**; use the parity harness instead of single‑winner leaderboards.

### E.2:7 - Conformance Checklist — BLP

| ID            | Requirement                                                                                                     | Purpose                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **CC‑BLP.1** | An activated comparison declares the α/δ tolerances, units and receiving conditions it actually uses, directly or through a policy profile. | Makes the comparison reproducible. |
| **CC‑BLP.2** | A Scale-Audit is required only when selected by the claim/risk or an independently applicable profile; it retains BLP-1a–e responses, uncertainty and pins. | Matches audit burden to the claimed use. |
| **CC‑BLP.3** | A scale-based selection cites BLP-2 and the applicable precedence rules; non-dominance yields no scale preference unless a separate local policy decides it. | Separates evidence from policy preference. |
| **CC‑BLP.4** | A heuristic meeting BLP-4's activated debt conditions is logged with scope, review, expiry and de-hardening plan. | Keeps real durable overrides inspectable. |
| **CC‑BLP.5** | Prescription form follows the task/control requirement; adaptation follows its product policy, permission, change authority and guards. | Preserves warranted procedures and bounded autonomy. |
| **CC‑BLP.6** | Decision-material resource accounts use A.15.1, A.15.2, B.1.6, C.16 and A.10; an assurance claim uses B.3. A separately activated stronger profile retains its required accounts and oversight. | Preserves applicable resource and assurance duties. |
| **CC‑BLP.7** | The response comparison records evidence-appropriate uncertainty; stochastic trial claims retain the actual replicate/seed and interval basis. | Prevents unsupported superiority. |

#### E.2:7.1 - Usable response and ordinary non-use

These constructed cases distinguish the rule; they are not empirical findings about real methods.

* **Bounded arithmetic:** summing one known finite list with a fixed procedure makes no scale or generality claim. Use the correct arithmetic and task budget; no scale audit, heuristic-debt entry or adaptation waiver follows from the availability of a general learner.
* **Positive safety procedure:** a product's applicable isolation-and-verification procedure remains required for the named maintenance action. Its task/control basis warrants its positive steps. BLP neither replaces it with prohibitions nor demands a waiver merely for its form.
* **Response versus slope:** for budget b in [1,10], A(b)=10+2b ranges from 12 to 30, while B(b)=90+0.1b ranges from 90.1 to 91. With the receiving quality floor 80, A fails everywhere despite its larger slope. B satisfies that floor; any broader preference still respects the other declared objectives, uncertainty and admissibility conditions. The floor is this use's condition, not a BLP constant.
* **Non-dominance:** at the same declared task, one admissible option has quality 95 and cost 10; another has quality 85 and cost 2. With quality maximized and cost minimized, neither dominates. BLP returns no scale-based preference. A declared generality policy may choose only within the options left lawful by higher rules and must identify that policy basis.

### E.2:8 - Relations
* **Instantiates pillars:** P‑10, P‑11, P‑7, P‑1.
* **Depends on:** **G.5/G.9** (admission/comparator/selector and parity harness), **G.11** (refresh telemetry), **A.15.1** (dated Work), **A.15.2** (planned work and budgets), **B.1.6** (resource aggregation), **C.16** (resource and cost measurement), and **A.10** (provenance), **C.18** (NQD-CAL), **C.19** (E/E-LOG), and **F.7/F.9** (Bridges, CL/Φ/Ψ). Planned **C.5** (Resrc-CAL) may later consolidate resource-use and work-cost guidance but supplies no current governing semantics.
* **Constrained by:** **E.5** Guard‑Rails (DevOps Lexical Firewall; Notational Independence; Unidirectional Dependency; Cross‑Disciplinary Bias Audit) and **E.3** precedence.

### E.2:9 - Definitions
**α (budget tolerance)** may be relative or absolute; declare units (e.g., % cost, wall‑time, energy). **δ (assurance tolerance)** is the permissible delta in assurance under **B.3**; declare measure and floor(s).

### E.2:10 - Consequences

*Positive*

* Provides an explicit “north star” for every contributor.
* Delivers a falsifiable checklist for evaluating proposals.
* Builds trust in high‑assurance domains through transparency.

*Trade‑offs*

* Constitutional review adds friction to rapid, informal changes.
* Amending the pillar set itself demands high‑bar governance.

### E.2:11 - Rationale

The pillars are distilled from systems engineering, philosophy of science, software architecture, and ontology design. They interlock: *Cognitive Elegance* (P‑1) enables *Didactic Primacy* (P‑2); *Open‑Ended Kernel* (P‑4) and *FPF Layering* (P‑5) make *Open‑Ended Evolution* (P‑10) and *SoTA alignment* (P‑11) feasible; *Cross‑Scale Consistency* (P‑8) provides the algebraic backbone for *Scalable Formality* (P‑3). This minimal yet sufficient set balances stability with change, rigor with accessibility, and abstraction with measurable impact.

`C.29` is a downstream support pattern for this constitution when mathematical first-principles structure is part of an argument about pillar support. It makes the structure, loss, and stop condition explicit while `E.2` remains authority over what counts as a pillar.

### E.2:12 - Relations

* **Depends on:** `E.1` – pillars operationalise the mission.
* **Refined by:** All subsequent patterns in the Core Specification.
* **Mathematical support path:** `C.29` supports pillar-impact arguments only for adequacy of mathematical lenses used to express first-principles structure. It does not amend pillar content, priority, or conformance.
* **Governs:** Every DRR, tool, and pedagogical artefact linked to FPF.

*These pillars are not a cage but the load‑bearing columns of a workshop where ideas can be safely built, dismantled, and evolved.*

### E.2:End
