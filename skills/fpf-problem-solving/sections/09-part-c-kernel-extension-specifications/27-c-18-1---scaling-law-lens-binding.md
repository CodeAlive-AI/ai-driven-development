## C.18.1 - Scaling‑Law Lens Binding (SLL)

> **Status:** Stable
> **Type:** Pattern

**Use this pattern when.** Use C.18.1 when a generator, selector, method family, benchmark, or comparison claims that behavior changes with scale, budget, data, model capacity, iteration budget, freedom of action, or another monotone scale variable.

**What goes wrong if missed.** Teams compare unequal budgets, call coverage telemetry an objective, claim a knee without probe evidence, or assume more scale means linear improvement across a window where the behavior has already changed.

**What this buys.** A compact scale-law lens: declare the scale variables, ScaleWindow, probe points, elasticity class, parity notes, and policy thresholds before treating a scale claim as usable in selection, parity, refresh, shipping, or mathematical-lens work.

**One‑screen purpose (manager‑first).**
Make **generation/selection** scale‑savvy: at the level of **conceptual descriptors**, declare (a) **which monotone knobs** we would scale, (b) the **ScaleWindow** over which we claim behaviour, and (c) the **elasticity class** we observed—**without** imposing numeric fits or vendor tools at Core level. This surfaces knees early and keeps comparisons lawful and fair across families. (Parity is handled by **G.9**; illumination remains a **report-only telemetry** unless a CAL policy promotes it.)

**Builds on.** C.16 (MM‑CHR), C.17 (Creativity‑CHR), C.18 (NQD‑CAL); advisory: C.5 (Resrc‑CAL).
**Coordinates with.** C.19 (E/E‑LOG), G.5 (Selector & Registry), G.9 (Parity Harness), G.10 (Shipping), G.11 (Refresh‑Telemetry), C.24 (Agent‑Tools‑CAL).
**Keywords.** scaling law; **Scale Variables (S)**; ScaleWindow; knee; diminishing returns; **iso‑scale parity**; **UNM/NormalizationMethod‑based mapping**; **scale‑probe**; **DoE** (design‑of‑experiments); segmented regression; knee detection.

### C.18.1:1 - Problem frame

Teams often say a method “**scales**” without disclosing **which resources**, **across what window**, and **how** outcomes respond (convex rise → knee → plateau). Without that, parity is skewed (unequal budgets, unmatched windows), coverage/illumination report-metrics leak into dominance, and “knees” are found late. SLL supplies a notation‑independent **lens** to make scale behaviour explicit and comparable.

### C.18.1:2 - Problem

Omitting **Scale Variables** and the comparison window causes: (i) **unfair parity** (compute/data/FoA mismatched), (ii) **illumination/coverage report-metric  creep** into dominance by default, (iii) late detection of knees and budget waste. **G.9** already forbids scalarising mixed scales and mandates equal **FreshnessWindows**/**pinned editions**; SLL complements this with **ScaleWindow** & elasticity.

### C.18.1:3 - Forces

Notation independence vs useful scaling heuristics; local context vs cross‑context generality; **telemetry vs objectives** (illumination stays report‑only telemetry unless policy promotes it); early exploration vs reproducible policy.

### C.18.1:4 - Solution — *binding lens for generator/selector profiles* (normative)

#### C.18.1:4.1 - Types (aliases; ΔKernel = 0).
`SLL.Profile` is an **annotation** on a `MethodFamily/Generator` or a `Selector` profile; no durable U-kinds are minted (LEX discipline).

#### C.18.1:4.2 - Fields (conceptual descriptors).

* **S — Scale Variables.** Minimal set of **monotone knobs** for the Context: `compute` (steps/tokens/FLOPs/time/energy), `data` (size/quality), `model capacity` (params/branches), `iteration budget`, **`freedom‑of‑action (FoA)`**/**environment richness**, etc. Declare **units** via **Resrc‑CAL** and bind to a **ScaleWindow**. Where training/inference trade, **name the phase** the claim concerns.
* **ScaleWindow.** Declared range of `S` values for which behaviour claims hold (editioned). This is **distinct from** **FreshnessWindow** used by parity.
* **Scale‑Probe.** At least **two** (preferably **≥ 3**) **parity‑respecting** points in `S` within the ScaleWindow, recorded with **replicates/seeds** and **CI/error bars** to support elasticity classification. Pick points via a **small factorial or Latin‑hypercube** when multiple knobs vary.
* **ElasticityClass** `χ ∈ {rising, knee, flat, declining}` — a **qualitative** class; numeric exponents/fits live in domain annexes, not Core.
* **ParityNotes.** `iso‑scale parity?` flag and **loss notes** if not achieved, plus **Bridge**, **Φ**, and **Ψ** IDs when crossing contexts; penalties affect `R` only.

#### C.18.1:4.3 - Norms (SLL).

* **SLL‑1 (Declaration).** Any profile **claiming scale behaviour SHALL** declare `S` and a **ScaleWindow** for the Context.
* **SLL‑2 (Probe).** Early investigation **SHALL** include a **scale‑probe** (≥ 2 points in `S`, with replicates/CI) and record **χ**. Multi‑knob probes **SHALL** hold unspecified knobs fixed or pinned, and disclose invariants.
* **SLL‑3 (Parity).** Where `S` is declared, comparisons **SHALL** ensure **iso‑scale parity** and lawful **UNM/NormalizationMethod‑based mapping** across heterogeneous knobs (e.g., FLOPs↔tokens) **before** comparing outcomes; **FreshnessWindows/editions** must be equal/pinned per **G.9**. Record **seeds/replicates**, ComparatorSet, and policy‑ids in telemetry/SCR.
* **SLL‑4 (Selection lens).** Within the **same Context and ScaleWindow**, if other heads (N/U/C) are tied, selectors **MAY** use illumination as a tie‑breaker, but it **SHALL NOT** change default dominance; illumination remains **report‑only telemetry** unless a CAL policy promotes it.
* **SLL‑5 (Knee test).** A **knee** is **claimed** only where a monotone rise is followed by a **statistically significant** slope drop across adjacent probe points within the ScaleWindow; thresholds (e.g., Δslope & CI level) are **policy‑defined** (E/E‑LOG) and must be cited. Absent such evidence, classify as **rising**.
* **SLL‑6 (Telemetry invariants).** Probes **SHALL** export seeds/replicates, edition pins, policy‑ids, and Resrc‑CAL units to **G.11**.

#### C.18.1:4.4 - Method — minimal SoTA probe recipe (notation‑agnostic; informative).
1) **Choose knobs** `S` that are plausibly monotone in the Context (compute/data/capacity/FoA).
2) **Pick 3–5 probe points** per active knob (edge/mid/edge) under iso‑scale parity; use a **fractional factorial** if >2 knobs.
3) **Run replicates** (≥ 3 preferred) and **bootstrap** 95% CI on the primary objective(s); log seeds.
4) **Estimate local slopes** on a log‑log grid; apply **piecewise/segmented regression** or a **knee detector** (e.g., L‑curve/Kneedle) to support `χ`.
5) **Record invariants** (pinned knobs, safety envelope) and publish **SLL.Card@Context**.
6) **If χ changes** across the window, split the ScaleWindow and re‑classify per segment.

### C.18.1:5 - Consumer relation fields - minimal inputs and outputs (conceptual)

**G.9 parity planning and run evidence** consumes `S` and `ScaleWindow` to align budgets, **pin editions**, and perform **UNM** or **NormalizationMethod** mapping; **G.11** carries **policy-id**, **PathSliceId**, seeds and replicates, CI level, and edition pins per parity CC.

### C.18.1:9 - Archetypal Grounding (post-2015; informative)

* **LLM scaling.** Kaplan-style & **Chinchilla-optimal** regimes; **Mixture-of-Experts** and **retrieval-augmented** families shift effective capacity with different inference budgets; prompt-policies often transfer better than narrow pipelines.
* **RL/Planning.** Model-based optimization & general agents vs hand-tuned controllers; slopes reported wrt budget/FoA under safety envelopes.
* **QD/OEE.** MAP-Elites, **CMA-ME**, **DQD**, **QDax**; **POET/Enhanced-POET** families: coverage/illumination as telemetry metrics; parity uses fixed grids/spaces and edition pins.

### C.18.1:7 - Bias-Annotation

| Bias | Symptom | Correction |
| --- | --- | --- |
| Bigger-is-better bias | More compute, data, capacity, or freedom of action is treated as automatic improvement. | Declare `S`, ScaleWindow, and elasticity class before using the scale claim. |
| Telemetry-as-objective bias | Coverage or illumination is promoted into dominance by default. | Keep telemetry report-only unless the selector policy explicitly admits it. |
| Knee-by-story bias | A plateau or knee is asserted from one anecdote or one late observation. | Require scale-probe points, replicates or uncertainty, and a cited threshold policy. |

### C.18.1:6 - Conformance Checklist (CC-SLL)

1. `S` declared **or** `S = N/A` with rationale.
2. **Scale-probe** performed; **χ** recorded with **replicates and CI**; invariants disclosed.
3. **iso-scale parity** or **loss notes** + penalties **→ R only**; editions/seeds pinned; ComparatorSet cited.
4. If used as tie-breaker, the selector cites **χ** and **lens id** in **E/E-LOG** provenance.
5. Knee claims cite the **policy threshold** and CI level used.

### C.18.1:8 - Common Anti-Patterns and How to Avoid Them

Hidden budget mismatches; averaging ordinals across families; **illumination in dominance by default**; unpinned editions; slope claims without **replicates/CI**; training/inference phase mixing → **cure** with **G.9** parity (equal windows/editions; normalize‑then‑compare; return sets), phase‑label the claim, and record slope uncertainty per Scale‑Audit discipline.

### C.18.1:10 - Payload — exports

`SLL.Card@Context` (UTS row; editioned):
`⟨S{knobs, units, phase}, ScaleWindow, Scale‑Probe{points≥2, design=one‑liner, seeds, CI}, ElasticityClass χ, ParityNotes{iso‑scale?|loss, invariants}, BridgeIds?/Φ/Ψ, PolicyIds? (E/E‑LOG), PathSliceId?⟩`.

**UTS row template (conceptual; pencil‑ready).**
`SLL.Card@Context := S=(COMPUTE|DATA|CAPACITY|FOA; units=…; phase=TRAIN|INFER), ScaleWindow=[LOW…HIGH], Probe=(points=…, design=factorial|LHD, seeds=…, CI=…), χ=rising|knee|flat|declining, ParityNotes=(iso=true|false; invariants=…), Bridge/Φ/Ψ=(…), PolicyIds=(…), PathSliceId=(…)`.

### C.18.1:11 - Consequences

**Benefits.** SLL prevents scale claims from becoming rhetoric. A comparison can show which knobs were scaled, what window is covered, how much probe evidence supports the slope class, and whether parity or normalization losses only affect assurance rather than silently changing dominance.

**Trade-offs.** Early work must spend probes on at least two scale points and record invariants, phase, seeds, uncertainty, or policy thresholds. The gain is that selectors, parity harnesses, refresh telemetry, and mathematical-lens uses can cite one bounded scale claim instead of guessing whether the observed behavior transfers.

**Stop condition.** Stop at C.18.1 when the scale variable, ScaleWindow, probe basis, elasticity class, and parity notes are enough for the current comparison. Move to `G.9`, `C.19`, `G.11`, `C.29`, or a domain annex when parity, selector policy, telemetry refresh, mathematical lens, or numeric fit becomes the live object.

### C.18.1:12 - Rationale

C.18.1 exists because scale claims are easy to overread as universal improvement claims. The pattern keeps scale behavior bounded by a declared scale variable, scale window, probe basis, uncertainty, elasticity class, and parity notes before the claim is reused.

### C.18.1:12.1 - SoTA-Echoing

Current scaling-law practice in machine learning, quality-diversity, optimization, planning, and resource-aware experimentation treats scale behavior as windowed and regime-dependent rather than as one universal “scales well” label. C.18.1 adapts that line into FPF by requiring scale variables, windows, probe points, uncertainty, and elasticity classes before scale claims are reused.

The pattern also keeps SoTA scaling practice from overriding FPF ontology. Scaling-law fits, knee detectors, segmented regressions, and experimental-design methods are mathematical or methodological support for the scale claim; they do not replace `C.16` measurement construction, `G.9` parity, selector policy, or `C.29` mathematical-lens admissibility.

### C.18.1:13 - Relations

**C.27 temporal-claim relation.**

- C.27 may flag: a claim that more review capacity, tool calls, tokens, data, model capacity, parallelism, freedom of action, sprints, or another declared scale variable changes rate, learning, recovery, throughput, stabilization, or improvement.
- This pattern keeps: scale variable, scale window, scale probes, and elasticity value.
- Non-admissible use: more scale is not linear improvement, and a scale word does not create a C.27 rate-change claim by itself.
- Neighboring-pattern use: if comparison or benchmark use is current, cite G.9 for parity; if the statement is only a linear effort fantasy, name the scale variable and scale window or downgrade.

**Builds on:** C.16/17/18. **Coordinates with:** C.19 (lenses/policies), **G.5** (set‑returning selector), **G.9** (parity; **ParetoOnly** default; UNM/NormalizationMethod‑based mapping), **G.10** (shipping).

> *Pedagogical cue.* **Say what you would scale, probe it twice, and use the slope‑class to steer.**

### C.18.1:13a - C.29 mathematical-lens use relation

> `C.18.1` supplies scale-window and scaling-law evidence for `C.29` when a mathematical lens claims scale behavior, universality, knees, exponents, coarse-graining validity, or diminishing returns. `C.29` cannot treat mathematical compression as scalable without an SLL or BLP-compatible scale-window account where scale is load-bearing. If no scale claim is live, `C.29` uses a local stop condition rather than opening scale-law work.

### C.18.1:End

