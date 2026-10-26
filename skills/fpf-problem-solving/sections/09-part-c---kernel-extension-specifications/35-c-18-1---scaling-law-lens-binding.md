## C.18.1 - Scaling‑Law Lens Binding (SLL)

> **Status:** Stable
> **Type:** Pattern

**Use this pattern when.** Use C.18.1 when a generator, selector, method family, benchmark, or comparison claims that behavior changes with scale—for example, with resource budget, data, model capacity, iteration budget or freedom of action. First name what is scaled, the window and the outcome being compared. Reuse an applicable probe account; new probing is needed only when the required scale claim remains unsupported. If no scale claim is needed, use the ordinary comparison directly.

**What goes wrong if missed.** Teams compare unequal budgets, call coverage telemetry an objective, claim a knee without probe evidence, or assume more scale means linear improvement across a window where the behavior has already changed.

**What this buys.** A compact scale-law lens: declare the scale variables, ScaleWindow, probe points, elasticity class, parity notes, and policy thresholds before treating a scale claim as usable in selection, parity, refresh, shipping, or mathematical-lens work.

**Purpose.** Declare which scale variables change, the ScaleWindow and the supported behavior class. Numeric fits remain domain work. G.9 governs parity, and a selector policy must admit any decision use of illumination.


**Keywords.** scaling law; **Scale Variables (S)**; ScaleWindow; knee; diminishing returns; **iso‑scale parity**; **UNM/NormalizationMethod‑based mapping**; **scale‑probe**; **DoE** (design‑of‑experiments); segmented regression; knee detection.

### C.18.1:1 - Problem frame

Teams often say a method “**scales**” without disclosing **which resources**, **across what window**, and **how** outcomes respond (convex rise → knee → plateau). Without that, parity is skewed (unequal budgets, unmatched windows), coverage/illumination report-metrics leak into dominance, and “knees” are found late. SLL supplies a notation‑independent **lens** to make scale behaviour explicit and comparable.

### C.18.1:2 - Problem

Omitting **Scale Variables** and the comparison window causes: (i) **unfair parity** (compute/data/FoA mismatched), (ii) **illumination/coverage report-metric  creep** into dominance by default, (iii) late detection of knees and budget waste. **G.9** already forbids scalarising mixed scales and mandates equal **FreshnessWindows**/**pinned editions**; SLL complements this with **ScaleWindow** & elasticity.

### C.18.1:3 - Forces

Notation independence vs useful scaling heuristics; local context vs cross‑context generality; **telemetry vs objectives** (illumination stays report‑only telemetry unless policy promotes it); early exploration vs reproducible policy.

### C.18.1:4 - Solution — *binding lens for generator/selector profiles* (normative)

#### C.18.1:4.1 - Profile annotation
`SLL.Profile` annotates a `MethodFamily/Generator` or `Selector` profile with the scale claim and its basis.

#### C.18.1:4.2 - Fields (conceptual descriptors).

* **S — Scale Variables.** Minimal set of adjustable variables with a declared order for the Context: `compute` (steps/tokens/FLOPs/time/energy), `data` (size/quality), `model capacity` (params/branches), `iteration budget`, **`freedom‑of‑action (FoA)`**/**environment richness**, etc. Declare each variable’s Characteristic and Scale, with a unit when applicable under **C.16**, and bind `S` to a **ScaleWindow**. Ordering the input does not assume a monotone improvement in the outcome; do not treat qualitative data quality or freedom of action as a ratio quantity without that measurement basis. Keep planned budget values with **A.15.2**; bind dated resource-use accounts to **A.15.1**, **B.1.6**, and **A.10**. Where training/inference trade, **name the phase** the claim concerns.
* **ScaleWindow.** Declared range of `S` values for which behaviour claims hold (editioned). This is **distinct from** **FreshnessWindow** used by parity.
* **Scale‑Probe.** At least **two** (preferably **≥ 3**) **parity‑respecting** points in `S` within the ScaleWindow, recorded with **replicates/seeds** and **CI/error bars** to support elasticity classification. Pick points via a **small factorial or Latin‑hypercube** when multiple knobs vary.
* **ElasticityClass** `χ ∈ {rising, knee, flat, declining}` — a **qualitative** class supported by the probe over the declared ScaleWindow. Leave `χ` unassigned when the observations and their uncertainty do not support a class, and state what remains unresolved. Numeric exponents/fits live in domain annexes, not Core.
* **ParityNotes.** `iso‑scale parity?` flag and **loss notes** if not achieved, plus applicable **Bridge**, **Φ**, and **Ψ** IDs for actual crossings under **G.9**; penalties affect `R` only.

#### C.18.1:4.3 - Norms (SLL).

* **SLL‑1 (Declaration).** Any profile **claiming scale behaviour SHALL** declare `S` and a **ScaleWindow** for the Context.
* **SLL‑2 (Probe).** A scale-behavior investigation **SHALL** use an applicable **scale‑probe** (≥ 2 points in `S`, with replicates/CI) and record the supported **χ**, or the unresolved classification. An existing probe may supply this basis while its window, definitions and conditions remain applicable. Multi‑knob probes **SHALL** hold unspecified knobs fixed or pinned, and disclose invariants.
* **SLL‑3 (Parity).** A comparison claiming matched scale **SHALL** establish **iso‑scale parity**. When heterogeneous knobs such as FLOPs and tokens require a mapping, apply a justified **UNM/NormalizationMethod** mapping **before** comparing outcomes under **G.9**; their names alone supply no conversion. Keep **FreshnessWindows/editions** equal/pinned as required by G.9. If iso-scale parity cannot be established, state the loss and restrict the comparison to what its applicable rule admits. Loss notes alone do not make an otherwise unsupported comparison admissible. Record **seeds/replicates**, ComparatorSet and applicable policy ids in telemetry/SCR.
* **SLL‑4 (Selection lens).** Within the **same Context and ScaleWindow**, if novelty, use value and constraint fit are tied, selectors **MAY** use illumination as a tie-breaker when an applicable pinned policy admits that bounded use. This **SHALL NOT** change default dominance. Promotion into dominance needs its own explicit CAL policy; otherwise illumination remains report-only telemetry.
* **SLL‑5 (Knee test).** A **knee** is **claimed** only where a monotone rise is followed by a **statistically significant** slope drop across adjacent intervals formed by at least three distinct probe points within the ScaleWindow; thresholds (e.g., Δslope & CI level) are **policy‑defined** (E/E‑LOG) and must be cited. Failure to establish a knee leaves that claim unsupported. Report **rising**, **flat** or **declining** only when the probe supports that class; otherwise leave **χ** unassigned. Absence of a confirmed knee is not evidence of rising performance.
* **SLL‑6 (Telemetry invariants).** Probes **SHALL** export seeds/replicates, edition pins, policy‑ids, and resource-account units governed by **C.16** and **B.1.6**, with dated-work and provenance links under **A.15.1** and **A.10**, to **G.11**.

#### C.18.1:4.4 - Method — minimal SoTA probe recipe (notation‑agnostic; informative).
1) **Choose ordered scale variables** `S` for the Context, such as compute, data, capacity or FoA, under their declared measurement basis.
2) **Pick 3–5 probe points** per active knob (edge/mid/edge) under iso‑scale parity; use a **fractional factorial** if >2 knobs.
3) **Run replicates** (≥ 3 preferred) and **bootstrap** 95% CI on the primary objective(s); log seeds.
4) **Estimate local slopes** on a log‑log grid only where the declared Scale operations are admissible under **A.18** and the logged values are positive; apply **piecewise/segmented regression** or a **knee detector** (e.g., L‑curve/Kneedle) to support `χ`.
5) **Record invariants** (pinned knobs, safety envelope). Use **SLL.Card@Context** to keep the account reusable; an adequate existing account need not be recopied.
6) **If χ changes** across the window, split the ScaleWindow and re‑classify per segment.

### C.18.1:5 - Consumer relation fields - minimal inputs and outputs (conceptual)

**G.9 parity planning** uses `S` and `ScaleWindow` to align budgets, **pin editions**, and declare any required **UNM** or **NormalizationMethod** mapping; run evidence records the applied mapping and pins. **G.11** carries **policy-id**, **PathSliceId**, seeds and replicates, CI level, and edition pins per parity CC.

### C.18.1:9 - Archetypal Grounding (post-2015; informative)

* **LLM scaling.** Historical Kaplan-style and **Chinchilla-optimal** regimes illustrate different compute/data allocations. **Mixture-of-Experts** and **retrieval-augmented** families require their own capacity and inference-budget account.
* **RL/Planning.** Model-based optimization & general agents vs hand-tuned controllers; slopes reported wrt budget/FoA under safety envelopes.
* **QD/OEE.** MAP-Elites, **CMA-ME**, **DQD**, **QDax**; **POET/Enhanced-POET** families: coverage/illumination as telemetry metrics; parity uses fixed grids/spaces and edition pins.

**Constructed classification case.** A matched-probe account supports unchanged performance across the declared resource window, with uncertainty small enough for the comparison's stated tolerance. Report `flat`; the absence of a knee does not turn it into `rising`. In a second account, the uncertainty still permits both an increase and a decrease that would matter to the choice. Leave `χ` unassigned and retain that limitation. A supported monotone increase without a confirmed slope drop can instead support `rising`. These supplied accounts illustrate classification and its limit; they are not empirical scaling results.

### C.18.1:7 - Bias-Annotation

| Bias | Symptom | Correction |
| --- | --- | --- |
| Bigger-is-better bias | More compute, data, capacity, or freedom of action is treated as automatic improvement. | Declare `S`, ScaleWindow, and elasticity class before using the scale claim. |
| Telemetry-as-objective bias | Coverage or illumination is promoted into dominance by default. | Keep telemetry report-only unless the selector policy explicitly admits it. |
| Knee-by-story bias | A plateau or knee is asserted from one anecdote or one late observation. | Require scale-probe points, replicates or uncertainty, and a cited threshold policy. |

### C.18.1:6 - Conformance Checklist (CC-SLL)

1. `S` declared **or** `S = N/A` with rationale.
2. **Scale-probe** performed; the supported **χ** or unresolved classification recorded with **replicates and CI**; invariants disclosed.
3. **iso-scale parity** or **loss notes**; any applicable penalties **→ R only**; editions/seeds pinned; ComparatorSet cited.
4. If illumination is used as a tie-breaker, the selector cites the admitting policy, **χ** and **lens id** in **E/E-LOG** provenance.
5. Knee claims cite the **policy threshold** and CI level used.

### C.18.1:8 - Common Anti-Patterns and How to Avoid Them

Hidden budget mismatches; averaging ordinals across families; **illumination in dominance by default**; unpinned editions; slope claims without **replicates/CI**; training/inference phase mixing → **cure** with **G.9** parity (equal windows/editions; normalize‑then‑compare; return sets), phase‑label the claim, and record slope uncertainty per Scale‑Audit discipline.

### C.18.1:10 - Payload — exports

`SLL.Card@Context` (UTS row; editioned):
`⟨S{knobs, units, phase}, ScaleWindow, Scale‑Probe{points≥2, design=one‑liner, seeds, CI}, ElasticityClass χ?, ParityNotes{iso‑scale?|loss, invariants}, BridgeIds?/Φ/Ψ, PolicyIds? (E/E‑LOG), PathSliceId?⟩`.

**UTS row template (conceptual; pencil‑ready).**
`SLL.Card@Context := S=(COMPUTE|DATA|CAPACITY|FOA; units=…; phase=TRAIN|INFER), ScaleWindow=[LOW…HIGH], Probe=(points=…, design=factorial|LHD, seeds=…, CI=…), χ?=rising|knee|flat|declining, ParityNotes=(iso=true|false; invariants=…), Bridge/Φ/Ψ=(…), PolicyIds=(…), PathSliceId=(…)`.

Here `χ?` means that the class is omitted when unresolved; uncertainty is not a fifth behavior class. Keep the probe account and its limitation available to the receiving comparison. An unassigned class cannot support a class-dependent preference.

### C.18.1:11 - Consequences

**Benefits.** SLL prevents scale claims from becoming rhetoric. A comparison can show which knobs were scaled, what window is covered, how much probe evidence supports the slope class, and what parity or normalization losses are declared, with any assurance penalties affecting `R` only rather than silently changing dominance.

**Trade-offs.** A supported scale claim needs observations at at least two scale points and recoverable invariants, phase, seeds, uncertainty and any applicable policy thresholds. Reuse of an applicable account can avoid new probing. The gain is that selectors, parity harnesses, refresh telemetry, and mathematical-lens uses can cite one bounded scale claim instead of guessing whether the observed behavior transfers.

**Stop condition.** Stop at C.18.1 when the scale variable, ScaleWindow, probe basis, supported class or explicit classification limit, and parity notes suffice for the receiving question. An unresolved class can finish this inquiry while leaving a scale-dependent preference unsupported. Select further probing only when its attainable contribution to the decision warrants its burden; use C.11.DUA if that choice needs resolution. Move to `G.9`, `C.19`, `G.11`, `C.29`, or a domain annex when parity, selector policy, telemetry refresh, mathematical lens, or numeric fit becomes the live object.

### C.18.1:12 - Rationale

C.18.1 exists because scale claims are easy to overread as universal improvement claims. The pattern keeps scale behavior bounded by a declared scale variable, scale window, probe basis, uncertainty, elasticity class, and parity notes before the claim is reused.

### C.18.1:12.1 - SoTA-Echoing

Current scaling-law practice in machine learning, quality-diversity, optimization, planning, and resource-aware experimentation treats scale behavior as windowed and regime-dependent rather than as one universal “scales well” label. C.18.1 adapts that line into FPF by requiring scale variables, windows, probe points, uncertainty, and elasticity classes before scale claims are reused.

The pattern also keeps SoTA scaling practice from overriding FPF ontology. Scaling-law fits, knee detectors, segmented regressions, and experimental-design methods are mathematical or methodological support for the scale claim; they do not replace `C.16` measurement construction, `G.9` parity, selector policy, or `C.29` mathematical-lens admissibility.

### C.18.1:13 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a claim that more review capacity, tool calls, tokens, data, model capacity, parallelism, freedom of action, sprints, or another declared scale variable changes rate, learning, recovery, throughput, stabilization, or improvement.
- This pattern keeps: scale variable, scale window, scale probes, and elasticity value.
- Non-admissible use: more scale does not by itself establish linear improvement, and a scale word does not create a C.27 rate-change claim by itself.
- Neighboring-pattern use: if comparison or benchmark use is current, cite G.9 for parity; if linear improvement is merely assumed, name the scale variable and scale window or state the improvement claim as an assumption.

**Builds on:** C.16/17/18. **Coordinates with:** C.19 (lenses/policies), **G.5** (set‑returning selector), **G.9** (parity; **ParetoOnly** default; UNM/NormalizationMethod‑based mapping), **G.10** (shipping). Use C.24 when the scale claim concerns agent/tool budgets or freedom of action.

> *Pedagogical cue.* **Say what is scaled, use the probe basis and steer only by the behavior it supports.**

### C.18.1:13a - C.29 mathematical-lens use relation

> `C.18.1` supplies scale-window and scaling-law evidence for `C.29` when a mathematical lens claims scale behavior, universality, knees, exponents, coarse-graining validity, or diminishing returns. `C.29` cannot treat mathematical compression as scalable without an SLL or BLP-compatible scale-window account where scale is load-bearing. If no scale claim is live, `C.29` uses a local stop condition rather than opening scale-law work.

### C.18.1:End
