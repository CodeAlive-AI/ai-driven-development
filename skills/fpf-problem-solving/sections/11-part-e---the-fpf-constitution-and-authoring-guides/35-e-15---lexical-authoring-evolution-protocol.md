## E.15 - Lexical Authoring & Evolution Protocol  (LEX‑AUTH)

> *Author patterns as evidence‑bearing epistemes, evolve them via governed open‑ended search, and publish an auditable trace that improves quality—not just compliance.*

### E.15:1 - Problem frame

FPF patterns are the **canon**: they define the generative rules that other artifacts depend on. Teams need to **change** patterns as the SoTA moves, but ad‑hoc edits lead to drift, low comparability, and brittle downstream updates. We need a **method** that (a) *generates* better alternatives, (b) *selects* them against explicit quality/assurance targets, and (c) *publishes* a machine‑ and human‑checkable **trace** that can be replayed, audited, and re‑run. (Built to cohere with **DRR (E.9)**, **LEX‑BUNDLE (E.10)**, **Canonical Evolution Loop (B.4)**, **NQD/E‑E (C.18 and C.19)**, **Evidence Graph Referring (A.10)**, **Trust (B.3)**, **F‑Suite validation (F.15)**.)

### E.15:2 - Problem

Without a disciplined authoring protocol:

* **One‑shot generation** dominates; there is no *evolutionary* path from vN → vN+1.
* “Trace” degenerates into a proof‑of‑work: *a method ran*, not *quality improved*.
* Pattern edits blur **lexicon vs. norms vs. examples**, breaking didactics and tool‑independence.
* SoTA content is cited but not **integrated** via Bridges & CL; claims get over‑ported.

### E.15:3 - Forces

| Force                                       | Tension we must resolve                                                           |
| ------------------------------------------- | --------------------------------------------------------------------------------- |
| **Generativity vs Assurance**               | Open‑ended idea generation must not erode safety/traceability.                    |
| **SoTA speed vs Canon stability**           | Frequent small updates must preserve conceptual integrity and roll‑up invariants. |
| **Local meaning vs durable reuse** | Recover meaning from the exact source and edition; use F.17 only for a durable local-sense address and F.9 only for an actual relation between distinct local senses. |
| **Notational independence vs Checkability** | Text must stay notation‑free yet be verifiable by Tooling harnesses.              |

### E.15:4 - Solution — A *governed evolutionary* authoring method with a publishable **LEX‑AUTH Trace (LAT)**

LEX‑AUTH defines **how** a pattern is **proposed, varied, selected, validated, and merged**, with artifacts and evidence fit to the FPF kernel.

#### E.15:4.1 - Method (design‑time choreography)

**Stage A — Frame and Scope (Question, Intended Use, Objectives, Invariants)**
**Historical record recovery.** Keep an old LAT, Context Card, and the claims it represents immutable under their original edition. When a current use relies on one, recover only the exact source and edition, effective `ReferenceScheme`, local claim, `ClaimScope`, and any method, model, criterion, or other subject-defined value that the use actually needs. Author a successor only from evidence. If an exact needed value cannot be recovered, return that value as unresolved; do not fill it from a card label or a newer edition. Reopen only the claims or actions that depended on the changed or missing value. An edition-number change alone does not reopen unrelated use.

1. **Frame** the exact pattern and edition, receiving question and intended use, applicable `ClaimScope`, and the selected scheme, source, model-use structure, or subject-specific situation only when it changes the work. Cite the applicable guardrails in **E.5.***, and state objectives for the change, such as clearer language, wider useful application, or lower assurance cost.
2. **Declare the Delta‑Class** (see §4.3) and **impact radius** (dependent patterns, bridges, tests).
3. **Fix acceptance targets** (see §4.4 Quality & SoTA metrics).

**Stage B — Generate candidates (SoTA + NQD)**
4. **Harvest SoTA** inputs (standards, rival patterns, lived domain idioms) and **bind** them as evidence through evidence-use relations with **claim/claim‑scope/timespan** and polarity (empirical vs deductive lines).
5. **Generate candidate variants** using **NQD‑CAL** engines (Novelty/Quality/Diversity) with an **E/E policy** (explore↔exploit governor) to populate a **Pareto front** of pattern phrasings/structures. *(No single shot; multiple candidate clauses compete.)*

**Stage C — Shape & Align (Structure, Bridges, USM)**
6. **Shape** top candidates into the standard **pattern template** (Problem frame → Problem → Forces → Solution → CC → Consequences → Rationale), obeying **LEX‑BUNDLE** (no tooling jargon; twin registers allowed).
7. **Relate local meanings only when needed.** Recover the exact source-local claims first. When the candidate actually relies on a relation between distinct F.17 cells, use F.9 to state that relation, its admitted use, and its loss or limits. A source import or shared word alone creates no Bridge.
8. **Type scopes** with **USM (A.2.6)**: keep **ClaimScope (G)** distinct from **WorkScope**; no “applicability/envelope” smuggling.

**Stage D — Validate & Decide (Assurance, Tests, DRR)**
9. **Run the harness**: update **SCR/RSCR** (F.15), lint lexical rules (E.10), run **Γ‑consistency** and **RSG/SoD** checks where relevant.
10. **Score** candidates on **Quality & SoTA metrics** (§4.4) and **assurance deltas** (Δ⟨F,G,R⟩).
11. Record a **DRR** (E.9) with *options considered*, *trade‑offs*, chosen candidate, *blast‑radius*.
12. **Merge** the winner; version pattern **SemVer** by Delta‑Class.

**Stage E — Publish & Monitor**
13. Publish the **LEX‑AUTH Trace (LAT)** (§4.2) as the separate authoring/evidence record for the change.

14. Schedule **evidence refresh** windows and an **evolution watchpoint** (B.4 loop): when metrics or SoTA inputs decay, reopen Stage B.

#### E.15:4.2 - The **LEX‑AUTH Trace (LAT)** — what it is and why it matters

A LAT is **not** “we ran a script.” It is a **structured episteme** that lets others **reproduce quality gains** and **re‑run** the search when SoTA shifts.

**LAT minimal contents (publish with the pattern):**

1. **Pattern and use identity** (pattern id and edition, intended use, `ClaimScope`, selected scheme or source, and any model-use structure that materially changes the use, plus SemVer and Delta-Class).
2. **Objective vector** (what we tried to improve: clarity, universality, assurance cost, etc.).
3. **SoTA pack** (sources bound through evidence-use relations with claim/scope/time and polarity).
4. **NQD settings** (emitters/lenses, diversity characteristics) + **E/E policy** used.
5. **Candidate set** (top K variants with NQD scores + short deltas from baseline).
6. **Cross-local relation account** (each actually consumed F.9 relation between distinct F.17 cells, with admitted use and loss notes; ordinary source imports need no fictitious Bridge).
7. **Assurance delta** (Δ⟨F,G,R⟩ from baseline; penalties from CL applied).
8. **Harness results** (checks passed/failed, test diffs).
9. **DRR link** (decision rationale id).
10. **Refresh policy** (evidence decay windows and triggers).

**Uses of the LAT:**
*Reproducibility* (re-run B-stages as SoTA changes), *assurance* (explicit impact on `F`, `G`, and `R`), *portfolio health* (diversity and coverage), *teaching* (didactic before-and-after), and *cross-local honesty* (no relation inferred from shared wording or source import).
Publish the pattern with its **DRR**, and publish the **LAT** as the separate authoring/evidence record for the change. The LAT carries the reproducible authoring trace and cites the DRR as the governing decision record. The DRR remains complete without LAT citations; it may summarize already-available decisive evidence by value when that evidence materially shaped the content choice. If later LAT or refresh evidence motivates a reopened or revised choice, carry that evidence into the successor DRR or other admissible decision record rather than retrofitting the accepted DRR.

**Example of a LAT‑stub**
```
LAT:
  pattern: F.15, basis: FPF/Core@<edition>, intended-use: <named use>, claim-scope: <scope>, semver: x.y+1, delta-class: Δ-2
  objectives: {clarity↑, universality↑, assurance-cost↓}
  SoTA-pack: {OpenAlex 2025‑Q3, SPECTER2‑23, DPP‑2019, MAP‑Elites‑2015+}
  NQD-settings: {CharacteristicSpace: domain‑family × …, grid: CVT@k=16}
  candidates: K=4 (wording of RSCR‑F04 & gates)
  bridge-ledger: none (intra‑canon refs only)
  assurance‑delta: ΔF=+, ΔG=+, ΔR=+ (after CL‑penalties=0)
  harness: LEX‑BUNDLE lint pass; F‑suite pass; Γ‑consistency ok
  DRR-id: DRR‑2025‑09‑DFCM‑roll‑in
  refresh: {source-cut-policy: <policy-id>@<edition>, reopen-on: [receiving question or use, relied source edition, known rival explanation, action-changing counterexample, transfer boundary]}
```

#### E.15:4.3 - What counts as “changed the pattern as a whole” — **Delta‑Classes & versioning**

Classify the intended change **before** work starts (declare it in the DRR framing; echo it in the LAT or evidence record when one is used):

* **Δ‑0 Lexical polish** — wording/ordering only; **no** change to CC or semantics. → *Patch* (x.y.**z**+1).
* **Δ‑1 Didactic restructure** — narrative/layout; **unchanged** Conformance Checklist (CC). → *Minor* (**x.y**+1.0).
* **Δ‑2 Normative refinement** — CC tightened/clarified; *semantics preserved* by test equivalence. → *Minor* (**x.y**+1.0) + **RSCR** required.
* **Δ‑3 Semantic change** — CC **adds/removes** requirements; downstream requirements shift. → *Major* (**x**+1.0.0) + **impact review** + **bridges refresh**.

> **Definition of “pattern changed as a whole”:** any **Δ‑2/Δ‑3** change (i.e., the **normative surface** or **semantics** changed) counts as a pattern change in the canonical corpus and triggers harness & bridge reviews.

#### E.15:4.4 - Quality & SoTA metrics (selection lenses)

**Mandatory lenses** (declare in LAT; higher is better unless noted):

* **Clarity** (readability; plain‑register score from didactic rubric).
* **Universality** (C‑1): *≥3 heterogeneous domains* anchored in the Archetypal section.
* **Lexical discipline** (E.10): 0 violations (DevOps lexicon, process/function conflations).
* **Assurance delta**: ΔF (formality), ΔG (scope clarity), ΔR (reliability after CL penalties).
* **Cross-local relation integrity**: when an actual F.9 relation between distinct local senses is consumed, name the relation, admitted use, loss notes, and applicable CL policy; penalties route to `R` only under B.3 and F.9, and the policy id is recorded in LAT.
* **Test conformance**: F‑suite pass; RSCR clean.
* **Exploration health** (NQD): diversity coverage > threshold; no premature convergence.
* **Didactic economy**: length vs density ratio within band; “Tell‑Show‑Show” present.

**Optional lenses** (selected for the subject and intended use): *ethical and separation-of-duties guard strength; cross-scale roll-up integrity; aggregation proofs present;* etc.

### E.15:5 - Conformance Checklist (normative)

**CC‑LA‑1 (Exact frame and intended use).**
Every authoring run **MUST** name the exact pattern and edition, receiving question and intended use, `ClaimScope`, Delta-Class, objectives, and acceptance lenses before generating candidates. It names a scheme, source, model-use structure, or subject-specific situation only when that value changes the work.

**CC‑LA‑2 (SoTA as evidence).**
External inputs **MUST** be bound through evidence-use relations around source epistemes with **claim, claim‑scope, polarity, timespan** (formal/empirical lines). No raw links.

**CC‑LA‑3 (Open‑ended generation).**
At least **K≥3** candidate variants **MUST** be generated via **NQD‑CAL** with a declared **E/E policy**; single‑shot edits violate LEX‑AUTH.

**CC‑LA‑4 (Bridges & CL).**
When a candidate actually relies on a relation between distinct F.17 local-sense cells, that relation **MUST** be stated through F.9 with its admitted use and loss notes. CL penalties apply to the R-lane when scoring. Shared wording, a source import, or an edition change alone does not establish a Bridge.

**CC‑LA‑5 (Harness).**
The candidate winner **MUST** pass **LEX‑BUNDLE** lint, **SCR/RSCR** tests, Γ‑consistency, and SoD/RSG gates where applicable.

**CC‑LA‑6 (Assurance deltas).**
The LAT **MUST** publish Δ⟨F,G,R⟩ relative to baseline, explicitly accounting for CL penalties and any narrowed scopes.

**CC‑LA‑7 (DRR).**
A **DRR** entry is mandatory for Δ‑2/Δ‑3 changes; it records options considered, rationale, and impact radius.

**CC‑LA‑8 (Refresh plan).**
Empirical evidence in the LAT **MUST** carry a **decay/refresh** window; a watchpoint **MUST** be scheduled in the Canonical Evolution Loop.

**CC‑LA‑9 (Publication).**
Publish the **pattern + LAT** together; past LATs are immutable. New runs produce new LATs.

### E.15:6 - Consequences

**Benefits.**
*Evolutive quality*: patterns improve through **search + selection**, not edits by fiat. *Auditability*: a re-runnable **LAT** shows *why* the chosen variant won. *Safety*: actually consumed cross-local relations are explicit and proportionately checked. *Comparability*: Delta-classes and SemVer let downstream readers predict blast radius.

**Trade‑offs.**
Some ceremony (LAT/DRR, NQD lenses) and maintenance (evidence refresh, bridge upkeep). These costs buy reproducibility and SoTA tracking.

### E.15:7 - Rationale & Links (informative)

LEX-AUTH extends the FPF constitution by **operationalising pattern evolution**: it plugs **B.4 Canonical Evolution Loop** into **E.9 DRR**, binds **SoTA** through evidence-use relations and **KD-CAL**, drives candidate generation with **C.18 NQD-CAL** under **C.19 E/E-LOG**, enforces lexical discipline via **E.10 LEX-BUNDLE**, and validates with **F.15** regression harnesses. When the work consumes an actual relation between distinct source-local meanings, F.9 carries that relation and B.3 carries any assurance penalty. The whole remains notation-independent (E.5.2) and stays within the Core → Tooling → Pedagogy dependency rule (E.5.3).

### E.15:8 - Operators (authoring deltas you are allowed to apply)

* **Refine** (tighten CC without changing acceptance meaning).
* **Split/Merge** (factor patterns; preserve links; update Bridges).
* **Generalise/Constrain** (expand/restrict ClaimScope (G) with proofs or loss notes).
* **Rephrase** (clarify language; leave CC untouched).

Each operator carries a default **Delta‑Class** and test obligations.

### E.15:9 - Self‑application Work Log (how this very pattern was authored)

> *This is **not** chain‑of‑thought; it is the required **`U.Work` evidence** for LEX‑AUTH.*

**Historical run basis.** The original run recorded `FPF/Core` as its Context; retain that field as historical wording under that LAT edition. A current reliance recovers the exact FPF/Core edition and only the source, scheme, claim, scope, and other values it needs. **Delta-Class:** Δ-2 (normative refinement by addition of method and CCs).
**Objectives.** Add an *evolutionary* authoring method; make trace *useful* (quality‑bearing); align with SoTA machinery already in spec.
**SoTA pack (evidence bound).** Prior FPF kernel commitments to **DRR (E.9)**, **E.10 LEX‑BUNDLE**, **B.4 Evolution**, **C.18 and C.19** NQD/E‑E, **F.15** harness, **F.9** Bridges, **B.3** Trust; these are treated as the authoritative internal SoTA for the Canon here.
**NQD/E‑E.** Generated ≥3 alternative Solution sections; finalist chosen for clearer Δ‑classes and actionable LAT contents.
**Bridges.** No cross‑external mapping; intra‑canon references only (CL=3).
**Harness.** LEX‑BUNDLE lint (no tooling jargon), CCs unique/atomic, didactic “Tell‑Show‑Show” via Self‑application log, Universality criterion met by cross‑kernel applicability.
**Assurance Δ.** F: + (explicit method & CCs); G: + (scope separation & Δ‑classes); R: + (LAT obligations + bridge penalties).
**DRR.** Recorded: alternatives considered (lighter trace vs full LAT), chosen design (full LAT).
**Refresh.** Reopen when SoTA (e.g., G‑suite authoring kit or CHR templates) evolves or when LAT misuse is seen in reviews.

### E.15:End

