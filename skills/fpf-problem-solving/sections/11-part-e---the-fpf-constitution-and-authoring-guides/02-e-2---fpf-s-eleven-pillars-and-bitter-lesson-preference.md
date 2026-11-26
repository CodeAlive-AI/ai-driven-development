## E.2 - FPF's Eleven Pillars and Bitter-Lesson Preference (BLP)

> **Status:** Stable

### E.2:1 - Problem frame
Use the Eleven Pillars in §4 to assess whether an FPF rule or artifact meets its constitutional obligations. Use the separate BLP policy in §6 when a computational choice claims a scale/generalization advantage or invokes a declared local generality policy: start with C.19.1's cheap scale-claim probe. An ordinary bounded fixed procedure can stop with its task-specific justification; specialization alone creates no scale audit, heuristic-debt entry or waiver. Independently applicable assurance or oversight requirements retain their checks.

E.1 sets the aim of making reliable reasoning accessible across disciplines through shared grounds, reusable Core methods and suitable domain methods. To turn that aim into a durable architecture, FPF needs a small, explicit constitution - principles that remain stable while everything built on top of them can evolve. Without such invariants, domain silos, vocabulary drift, and tool-centric shortcuts quickly erode coherence and reproducibility across disciplines.

The pillars are also the first-principles basis of FPF. They are the minimal commitments from which pattern-level work derives: decisive structure, teachability, maturing formality, open kernel, layering, register discipline, practical payoff, cross-scale consistency, explicit state, open-ended evolution, and SoTA renewal. Later patterns can support this basis by making a concrete argument about pillar support more inspectable; they do not replace pillar authority.

### E.2:2 - Problem
Without binding first principles, contributors cannot distinguish commitments that proposals must preserve from choices they may revise. Treating every choice as fixed blocks adaptation; treating every commitment as optional leaves incompatible rules without a basis for resolution.

### E.2:3 - Forces
| Force                          | Tension                                                |
| ------------------------------ | ------------------------------------------------------ |
| **Foundational Stability**     | Stable commitments ↔ adaptation to new knowledge |
| **Cognitive Load**             | Minimal elegance ↔ comprehensive coverage              |
| **Rigor vs Accessibility**     | Formal soundness ↔ intuitive entry for non‑specialists |
| **Universality vs Modularity** | Domain‑agnostic scope ↔ plug‑in extensibility          |
| **Pragmatic Grounding**        | Abstract invariants ↔ measurable, falsifiable outcomes |

### E.2:4 - Solution
FPF rests on **eleven binding pillars**. Follow the proposed change through the work it would affect. An organization may use a rule to decide, and a service may use it to route a request. When people are to understand or apply that rule, examine what it enables them to do with the support available to them. P‑2 governs human comprehension in that use. Which decisions, explanations or obligations would change, and under which conditions? Use those consequences to identify the applicable pillar constraints below. Where several uses are claimed, establish which grounds extend to them together and where their conditions differ. E.3 resolves conflicting provisions. A DRR for a normative change records its impact on the pillars. E.2.DA serves the broader commission to evaluate how FPF realizes them.

| ID       | Pillar                         | Essence                                                                                                                   |
| -------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **P‑1**  | **Cognitive Elegance**         | Highlight decisive structure, eliminate ornamental formalism; separate data governance from thinking.                     |
| **P‑2**  | **Didactic Primacy**           | Human comprehension outranks theoretical or tooling purity.                                                               |
| **P‑3**  | **Scalable Formality**         | Strengthen formality as the use requires, preserving meaning and traceable grounds. A changed meaning may require an explicit rewrite or branch.        |
| **P‑4**  | **Open‑Ended Kernel**          | The Kernel contains only meta‑concepts; all domain knowledge lives in external patterns.                       |
| **P‑5**  | **FPF Layering**           | Patterns are modular, declarative extensions that can be added, replaced, or removed without destabilising the core. |
| **P-6**  | **Lexical Stratification**     | Every core concept is expressible in four registers: plain name, technical term, admitted U-kind or governed value name, and mathematical symbol.  |
| **P‑7**  | **Pragmatic Utility**          | Proofs, metrics, and models exist to achieve real‑world objectives; falsification is rewarded over confirmation.          |
| **P‑8**  | **Cross‑Scale Consistency**    | Preserve shared distinctions and state what composition preserves or loses across scales and bearers; qualify each algebra for its material-system, knowledge, or Method use.    |
| **P‑9**  | **State Explicitness**         | Make states, editions and transition conditions explicit when they change use or reliance. Keep transitions traceable and assess their cost and risk.         |
| **P‑10** | **Open‑Ended Evolution**       | Keep justified improvement, revision, replacement and branching possible. Choose continuation under the use’s cost and safety constraints; permit retention, local stopping and retirement with explicit reasons and reopen conditions.               |
| **P‑11** | **State‑of‑the‑Art Alignment** | The kernel and extension domain-specific patterns track reliable contemporary knowledge and update when the SoTA advances.                     |

A pillar-impact argument can use ordinary accepted mathematical theory. Use `C.29` when a separate question remains about choosing a mathematical representation, transferring a result, or relying on the represented structure. State the correspondence, preserved and lost structure, and limits needed for that use; `E.2` continues to govern the pillar claim.

> A proposed FPF rule that conflicts with a pillar can be revised to respect it. To proceed with the conflicting proposal, the body empowered to change the constitution must enact the pillar amendment first. The DRR states the grounds and Pillar Impact Analysis.

### E.2:5 - Conformance Checklist

| ID         | Requirement                                                                                                                       | Purpose                               |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **CC‑P‑1** | An architectural pattern names the Pillars whose realization or conflict changes its design or use, with the substantive grounds required by CC‑P‑4. | Makes material constitutional relations recoverable. |
| **CC‑P‑2** | Every DRR proposing a normative change **must** include a “Pillar Impact Analysis.”                                               | Makes constitutional review explicit. |
| **CC‑P‑3** | Tooling and pedagogical artefacts **should** document which pillar(s) shape their design.                                         | Upholds P‑2 (Didactic Primacy).       |
| **CC‑P‑4** | Assess the substance of every applicable Pillar constraint and any material conflict. Name the Pillars whose realization changes the pattern’s design or use; no minimum link count substitutes for that argument. | Grounds conformance in the obligations that matter to the pattern. |
| **CC‑P‑5** | A claim of scale or generalization advantage in computational work, or a choice invoking a local generality policy, begins with the scale-claim check in C.19.1. An empirical comparison evaluates usable performance over the declared budget range and receiving conditions. For a choice made under a project rule, identify the condition that makes the rule applicable. A bounded specialization alone calls for no audit, debt entry or waiver. | Connects the choice to its empirical or policy grounds. |
| **CC‑P‑6** | A pillar-impact analysis that relies on mathematical structure, scale behavior, optimization, uncertainty, invariance, obstruction, or other first-principles modeling support is complete only when that support is ordinary accepted local theory, a cited `C.29` output, or a named neighboring-pattern output for evidence, causal, bridge, assurance, measurement, work, decision, publication, or admission claims. | Keeps mathematical support for pillars inspectable without letting `C.29` revise pillar authority. |

### E.2:6 - Policy — Bitter‑Lesson Preference (BLP)

**Intent and activation.** In search, learning, planning and related computational work, investigate a claimed advantage from increased compute, data or search capacity under C.19.1. The empirical Bitter Lesson motivates that comparison; it does not decide every choice between a specialized and a general approach. An analogy or generality preference for another bearer needs a separately declared local policy, receiving purpose, scale predicate and evidence basis. Ordinary bounded specialization can stop with its task-specific justification.

**BLP-1 — Claim-matched comparison and audit.** Begin an activated BLP use with C.19.1's cheap scale-claim probe. Name the candidate, task/use, scale variable, objective, usable budget range, receiving conditions and evidence form. Missing comparison premises return `no scale claim yet`; select evidence depth by claim and risk. An independently activated profile can require a fuller Scale-Audit. That audit retains:

* (a) **Parity and admissibility:** comparable tasks, budget basis, editions, freshness and risk/safety envelope. Use G.5/G.9 when their selector/parity contracts apply. Pareto comparison is the default over the declared objective vector; another comparison needs a lawful declared policy under E.3.
* (b) **Usable budgets:** vary the dimensions relevant to the claim—compute, data or freedom of action where applicable—and pin held conditions. Compare only over the range available to the receiving use; extrapolation needs its own basis.
* (c) **Response and uncertainty:** report performance over that range with an uncertainty treatment appropriate to the evidence. Slopes may characterize response but cannot replace its level, admissibility or receiving floor. Repeatable stochastic trials retain seeds/replicates and confidence intervals where used; deterministic derivations retain their assumptions and validity bounds.
* (d) **Resources and assurance:** retain decision-material resource accounts through A.15.1, A.15.2, B.1.6, C.16 and A.10 as applicable. A named assurance claim uses B.3; independently applicable assurance and oversight requirements remain binding.
* (e) **Objectives and tolerances:** declare quality, risk, cost and any illumination coordinate promoted by an explicit CAL policy. State units and the budget/assurance tolerances α/δ used by the comparison. Publish the audit's edition and policy pins through G.11.

**BLP-2 — Usable-performance preference.** Among admissible options under the receiving conditions, with comparable assurance within δ and budgets within α when those tolerances apply, prefer the option whose usable performance is shown to Pareto-dominate across the audited range. Evaluate uncertainty in the performance contrast, including dependence between paired observations. Return `no scale-based preference` when the comparison establishes equivalence, establishes a trade-off, or leaves the ordering open. Say which outcome the evidence supports. A project policy under E.3 can decide the cases covered by its terms. Cite that policy and the cost of applying it for the resulting choice.

**BLP-3 — Task-appropriate prescription.** Positive procedures and prohibitions are both available under their task or control needs. A mandated safety procedure keeps its force. Minimal prescription and autonomous sequencing need their justified policy, authority and guards; neither follows from a scale comparison. Ordinary use of a positive procedure requires no BLP waiver solely because a general search alternative exists.

**BLP-4 — Conditional heuristic debt.** Apply C.19.1's debt branch when an admitted heuristic carries a durable scale/generality preference, reusable solution-family policy, selector-facing preference or override within an activated BLP use. Retain scope, review responsibility, expiry/review window, replacement target and de-hardening plan in CalibrationLedger/BCT and SCR as applicable. A bounded task-specific tactic that makes none of those claims is not debt merely because it is specialized.

**BLP-5 — Separately authorized adaptation.** Enable, require or prohibit adaptation under the product's objective, evidence, permission, change authority and risk/Guard-Rail conditions. A fixed method needs no BLP adaptation waiver solely for remaining fixed. A product policy that requires adaptation or its review retains that obligation and its exception rule.

**BLP‑6 — Precedence & Safeguards.** BLP combines governance and architectural principles; classify each compared principle under E.3 rather than assigning one class to the whole policy. It is instantiated by Pillars **P‑10 (Open‑Ended Evolution)**, **P‑11 (SoTA Alignment)**, **P‑7 (Pragmatic Utility)**, and **P‑1 (Cognitive Elegance)**. It does **not** override applicable safety and ethics requirements, **E.5** Guard‑Rails, or E.3 precedence rulings; where BLP conflicts with Guard‑Rails, **Guard‑Rails prevail**. When **NQD/E/E‑LOG** elevates illumination to dominance for exploration mandates, BLP **adopts that lens** rather than overriding it.

BLP applies to comparisons such as prompt programming versus fine-tuning and model-based planning versus hand-tuned control when they make the scale or generality claims specified above. Their tasks and receiving conditions determine the comparison; G.5/G.9 apply when their selector/parity contracts hold.

### E.2:7 - Conformance Checklist — BLP

| ID            | Requirement                                                                                                     | Purpose                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **CC‑BLP.1** | An activated comparison declares the α/δ tolerances, units and receiving conditions it uses, directly or through a policy profile. | Makes the comparison reproducible. |
| **CC‑BLP.2** | A Scale-Audit is required only when selected by the claim/risk or an independently applicable profile; it retains BLP-1a–e responses, uncertainty and pins. | Matches audit burden to the claimed use. |
| **CC‑BLP.3** | A scale-based comparison identifies the BLP-2 result and the applicable precedence rules. Retain `no scale-based preference` and its grounds when equivalence or a trade-off is established or the ordering remains open. If a local rule also decides the choice, record that decision and its separate basis. | Keeps the performance comparison available after the project chooses. |
| **CC‑BLP.4** | A heuristic meeting BLP-4's activated debt conditions is logged with scope, review, expiry and de-hardening plan. | Keeps durable overrides inspectable. |
| **CC‑BLP.5** | Prescription form follows the task/control requirement; adaptation follows its product policy, permission, change authority and guards. | Preserves warranted procedures and bounded autonomy. |
| **CC‑BLP.6** | Decision-material resource accounts use A.15.1, A.15.2, B.1.6, C.16 and A.10; an assurance claim uses B.3. A separately activated stronger profile retains its required accounts and oversight. | Preserves applicable resource and assurance duties. |
| **CC‑BLP.7** | The response comparison records evidence-appropriate uncertainty; stochastic trial claims retain the replicate/seed and interval basis. | Prevents unsupported superiority. |

#### E.2:7.1 - Usable response and ordinary non-use

These constructed cases distinguish the rule; they are not empirical findings about real methods.

* **Bounded arithmetic:** summing one known finite list with a fixed procedure makes no scale or generality claim. Use the correct arithmetic and task budget; no scale audit, heuristic-debt entry or adaptation waiver follows from the availability of a general learner.
* **Positive safety procedure:** a product's applicable isolation-and-verification procedure remains required for the named maintenance action. Its task/control basis warrants its positive steps. BLP neither replaces it with prohibitions nor demands a waiver merely for its form.
* **Response versus slope:** for budget b in [1,10], A(b)=10+2b ranges from 12 to 30, while B(b)=90+0.1b ranges from 90.1 to 91. With the receiving quality floor 80, A fails everywhere despite its larger slope. B satisfies that floor; any broader preference still respects the other declared objectives, uncertainty and admissibility conditions. The floor is this use's condition, not a BLP constant.
* **Non-dominance:** at the same declared task, one admissible option has quality 95 and cost 10; another has quality 85 and cost 2. With quality maximized and cost minimized, neither dominates. BLP returns no scale-based preference. A declared generality policy may choose only within the options left lawful by higher rules and must identify that policy basis.

### E.2:8 - Relations

The relations in this section govern the Bitter-Lesson Preference.
* **Instantiates pillars:** P‑10, P‑11, P‑7, P‑1.
* **Depends on:** **G.5/G.9** (admission/comparator/selector and parity harness), **G.11** (refresh telemetry), **A.15.1** (dated Work), **A.15.2** (planned work and budgets), **B.1.6** (resource aggregation), **C.16** (resource and cost measurement), and **A.10** (provenance), **C.18** (NQD-CAL), **C.19** (E/E-LOG), and **F.7/F.9** (Bridges, CL/Φ/Ψ).
* **Constrained by:** **E.5** Guard‑Rails (DevOps Lexical Firewall; Notational Independence; Unidirectional Dependency; Cross‑Disciplinary Bias Audit) and **E.3** precedence.

### E.2:9 - Definitions
**α (budget tolerance)** may be relative or absolute; declare units (e.g., % cost, wall‑time, energy). **δ (assurance tolerance)** is the permissible delta in assurance under **B.3**; declare measure and floor(s).

### E.2:10 - Consequences

*Positive*

* Gives contributors explicit constitutional obligations.
* Delivers a falsifiable checklist for evaluating proposals.

*Trade‑offs*

* Constitutional review adds friction to rapid, informal changes.
* Amending the pillar set demands high‑bar governance.

### E.2:11 - Rationale

The pillars interlock: *Cognitive Elegance* (P‑1) enables *Didactic Primacy* (P‑2); *Open‑Ended Kernel* (P‑4) and *FPF Layering* (P‑5) make *Open‑Ended Evolution* (P‑10) and *SoTA alignment* (P‑11) feasible; *Cross‑Scale Consistency* (P‑8) provides the algebraic backbone for *Scalable Formality* (P‑3). Together the pillars balance stability with change, rigor with accessibility, and abstraction with measurable impact.

`C.29` supports a pillar-impact argument when its mathematical representation choice, transfer, or reliance remains unresolved. It states the relevant correspondence, loss and use condition; `E.2` remains authority over the pillars.

### E.2:12 - Relations

* **Depends on:** `E.1` – pillars operationalise the mission.
* **Applied by:** Later Core patterns use the pillars relevant to their decisions. When a pattern also claims strict model refinement, compare the two models for the same inquiry. The proposed model must admit a feasible completion, preserve the earlier commitments in every completion and exclude a formerly admissible answer. [B.5.MR:4.2](../08-part-b---trans-disciplinary-reasoning-cluster/32-b-5-mr---compare-models-by-refinement-and-abstraction.md#b5mr42---test-preservation-and-strictness) gives the test when the models use different languages.
* **Mathematical support path:** `C.29` supports pillar-impact arguments only for adequacy of mathematical lenses used to express first-principles structure. It does not amend pillar content, priority, or conformance.
* **Governs:** FPF proposals and artifacts where a pillar sets a condition of conformance. A team using an FPF publication can identify which provisions it has adopted for its own work.



### E.2:End
