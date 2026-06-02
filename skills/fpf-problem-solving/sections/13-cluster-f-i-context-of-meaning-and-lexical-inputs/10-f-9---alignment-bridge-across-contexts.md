## F.9 - Alignment & Bridge across Contexts

**“Translate across Contexts; never collapse them.”**
**Type.** Architectural pattern.
**Status.** Stable.
**Normativity.** Normative.
**Builds on:** E.10.D1 (Context discipline: Context = U.BoundedContext); **F.0.1 (senseFamily & StatusModality guard; Bridge-only crossing)**; F.1 (Contexts fixed); F.2/F.3 (Cells exist); F.7 (rows depend on Bridges); F.8 (thresholds and reuse choice).

**Coordinates with:** B.3 **Trust & Assurance Calculus** (uses CL penalties); **A.6.1 U.Mechanism** (Transport clause for cross-context use; penalties feed **R/R_eff** only; **F/G** invariant); Part C patterns (apply Bridges in formal claims); A.6.9 (RPR-XCTX for repairing umbrella “same/equivalent/align/map” prose into explicit Bridge Cards).
**Aliases (informative).** *Context-to-Context translator*; *Sense bridge*.

### F.9:1 - Intent & applicability

**Intent.** Provide a **conceptual discipline** for relating **SenseCells** from **different Contexts (U.BoundedContext)**. A **Bridge** states *what kind* of relationship holds, *how far* it holds (via **CL: Congruence Level**), and *what is lost* during the translation. Bridges **support carefully scoped reuse** (e.g., a Concept-Set row) while **rejecting silent equivalence**.

**Applicability.** Use **whenever** an author needs to **read across Contexts**—to reuse a familiar label, to connect design-time and run-time notions, to compare two standards’ terms, or to justify a row in the Concept-Set table. This pattern is **not** storage, enactment protocol, or governance; it codifies **thinking moves**.

**Non-goals.** No global meaning; no `PublicationSurface` semantics; no editor roles. Bridges are **semantic relations between local senses**, not transport chains, not processes.
**Governed object in plain terms.** One bridge card relating two `SenseCells` across different `U.BoundedContext`s; not a transport chain, not a workflow, and not one global meaning layer.
**Governing move in plain terms.** Declare relation kind, direction, `CL`, and loss between local senses so cross-context reading stays inspectable without collapsing them into silent equivalence.
**Primary working reader.** The primary working reader is an author, checker, or practitioner preparing one bridge card, one comparative mapping note, or one concept-set row that depends on cross-context reading without pretending the contexts have already collapsed.
**Use this when.** Use this pattern when two local senses from different contexts need one explicit bridge card before a team can admissibly reuse a label, justify a row, or compare the cases without pretending the senses are equivalent or substitutable.
**Start here when.** The same term, role, quality, or status label appears in more than one context and the team is about to treat that overlap as if it were already equivalence, safe substitution, or structure-preserving reuse.
**What goes wrong if missed.** Teams fall back to shared labels, string-equals shortcuts, or informal analogies, then quietly smuggle equivalence, substitution, or structure across contexts without publishing relation kind, `CL`, or loss.
**What this buys.** One explicit bridge discipline that lets a team reuse names, compare contexts, and publish bounded cross-context support without losing track of direction, loss, and the limits of admissible substitution.
**Not this pattern when.** Not this pattern when the case is still only a coarsened source-pinned rendering with no bridge claim yet, or when the real job is storage, enactment, governance, or one single local context rather than explicit cross-context alignment.

**Boundary to controlled coarsening.** This pattern is also the explicit boundary pattern when a simplified or coarsened cross-context rendering starts to imply equivalence, substitution, projection, or interoperability scope. If the case is still only a coarsened source-pinned rendering for narrower use, keep it with that rendering's own source tether, non-admissible-use line, and reopen condition, using `A.6.3.CSC Controlled Semantic Coarsening` when that narrower-use card is primary. A lighter cross-context note may support informal orientation talk, but that is not a formal `F.9` `Naming-only` row. Any bridge, substitution, row, or interoperability claim must reopen the source-bearing episteme or source publication needed for bridge support before a Bridge Card may be published under `F.9`.
**Recognition vs assurance note.** Read **Intent**, **Applicability**, **Non-goals**, and the `A.6.3.CSC` neighbor boundary above as the ordinary recognition block. Read Bridge kinds, `CL`, conformance, and Relations below as assurance blocks that tighten the same bridge-card claim; they do not widen the pattern into transport, workflow, or one global meaning layer.

### F.9:2 - Problem frame

Cross-context work fails in predictable ways:

1. **String-equals fallacy.** Identical spellings (“process”, “role”, “accuracy”) taken as identical meaning.
2. **Scope creep.** A naming convenience is stretched to assignment or structural claims.
3. **DesignRunTag jumping.** Design artefacts are substituted for run-time occurrences (or vice-versa).
4. **Direction amnesia.** Narrower/broader relations treated as symmetric.
5. **Loss blindness.** Differences (units, granularity, preconditions) are left unstated, contaminating downstream reasoning.

Bridges cure these by **making relation, direction, loss, and `CL` explicit**.


### F.9:3 - Forces

| Force                           | Tension to resolve                                                                       |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| **Locality vs reuse**           | Senses are context-local, yet people need a common label to talk across Contexts.              |
| **Simplicity vs fidelity**      | Few Bridge kinds are teachable; too few will hide real mismatches.                       |
| **Safety vs utility**           | Support bounded substitution when the bridge kind and `CL` license it; leave substitution unsupported when loss is unbounded. |
| **senseFamily purity vs explanation** | Substitution must preserve **senseFamily**; explanation may span **senseFamilies** without implying sameness. |


### F.9:4 - Core idea (didactic)

**A Bridge is a declared translator between two local senses.**
It always names **(a)** the two **SenseCells**, **(b)** a **Bridge kind** (what relation), **(c)** a **direction** (if non-symmetric), **(d)** a **CL** value, and **(e)** **Loss Notes** (what fails to carry). Some Bridges **support substitution** in limited scopes; others **support only explanation**.


### F.9:5 - Minimal vocabulary (this pattern only)

* **Context** — shorthand for **U.BoundedContext** (per E.10.D1).
* **SenseCell** - the pair *(Context, Local-Sense)* from F.3.
* **Bridge** — a conceptual relation between two SenseCells with kind, direction, CL, and loss notes.
* **CL (Congruence Level)** — ordinal congruence class (0…3) of a Bridge (see §7).
* **Scope** — the **Bridge-supported use** of a cross-context reading (as in F.7/F.8):

* **Naming-only** (talk consistently),
* **Role Assignment & Enactment-eligibility** (assignable constraints/roles/status reuse),
* **Type-structure** (safe structural inference).
* **senseFamily** — the semantic category (Role, Status, Measurement, Type-structure, Method, Execution…) per F.0.1 (normative Part F guard).


### F.9:6 - Bridge kinds (senseFamily-aware)

> **Two families** of Bridges: **Substitution Bridges** (senseFamily-preserving; can support Concept-Set rows) and **Interpretation Bridges** (explanatory; **not** for substitution).

#### F.9:6.1 - Substitution Bridges (sense-preserving)

These relate **SenseCells of the same senseFamily** and may support **limited substitution**:

1. **Equivalence** - *near-identity of sense*. Symmetric. Rare.
   *Use:* May support **Type-structure** rows when CL=3 and invariants match.
   *Loss Notes:* usually “none” or “profiling differences”.

2. **Narrower-than / Broader-than** - *proper inclusion of sense*. Directional.
  *Use:* Safe to substitute **narrower > broader** in **Naming-only** and sometimes **Role Assignment & Enactment**; **broader > narrower** is unsafe.
   *Loss Notes:* “loses special cases X”.

3. **Partial-overlap** - *non-empty intersection, neither includes the other*.
  *Use:* **Naming-only** at best. **Never** justifies Role Assignment & Enactment / Type-structure.
   *Loss Notes:* “A-only senseFamily”, “B-only senseFamily”.

4. **Disjoint** - *explicit contrast*.
   *Use:* For **didactic warnings**; not reuse support.
   *Loss Notes:* n/a (it asserts incompatibility).

#### F.9:6.2 - Interpretation Bridges (cross-senseFamily, explanatory)

These **do not support substitution** but **explain connections** across senseFamilies:

5. **Design-spec -> Run-trace** - a design concept relates to its run-time occurrence.
   *Example:* *BPMN\:Process* -> *PROV\:Activity*.
   *Use:* Explain design-to-execution correspondence. No Concept-Set rows.
   *Loss Notes:* “graph vs event”, “control-flow vs temporal extent”.

6. **Measure-of / Evidence-for (->)** — a measurement SenseCell evidences or quantifies another **senseFamily** (e.g., a Requirement clause).
   *Example:* *SOSA\:Observation* -> *ITIL\:SLO fulfilment*.
   *Use:* Explain evaluation. No substitution.

7. **Policy-implies / Obliges (->)** — a deontic statement constrains another **senseFamily**.
   *Example:* *ODRL\:Duty* -> *Service behaviour*.
   *Use:* Explain constraint propagation.

> **Rule of thumb.** If you want **rows** or **substitution**, you need a **Substitution Bridge** on the **same senseFamily**. If you want to **explain** why artefacts relate without claiming sameness, use **Interpretation Bridges**.


### F.9:7 - CL scale and scope thresholds

CL expresses how safely meaning carries over.

| CL    | Name              | Intuition                                            | Typical loss             | Row scope supported (thresholds) |
| ----- | ----------------- | ---------------------------------------------------- | -------------------- | -------------------------------- |
| **0** | **Opposed**       | Intentionally contrastive or disjoint                | n/a                  | none                             |
| **1** | **Comparable**    | Talk under a shared label; senses differ materially  | material sense divergence | **Naming-only** (`CL >= 1`) |
| **2** | **Translatable**  | Bounded loss; consistent examples & counter-examples | small, stated losses     | **Role Assignment & Enactment-eligibility** (`CL >= 2`) |
| **3** | **Near-identity** | Invariants match; no material counter-example        | profile-level only       | **Type-structure** (`CL = 3`) |

* **Thresholds (normative):**

  * Publishing a **Naming-only** row requires **CL >= 1** across the row's Cells.
  * Publishing a **Role Assignment & Enactment-eligible** row requires **CL >= 2**, the **same senseFamily**, and compatible stance.
  * Publishing a **Type-structure** row requires **CL = 3** **and** matched invariants (acyclicity, anti-symmetry, units, etc.).

* **Penalty use (informative):** B.3 may convert **CL** into an assurance penalty when a cross-context claim is made.


### F.9:8 - The Bridge Card (compact sketch)

> A **thought-format** (not a form). Every bullet can be said in a sentence.

* **Cells.** `A@contextA` - `B@contextB`.
* **senseFamily.** *Role, Status, Measurement, Type-structure, Method, or Execution ...*
* **Kind.** *Equivalence / Narrower-than / Broader-than / Partial-overlap / Disjoint / Design-spec -> Run-trace / Measure-of / Policy-implies*.
* **Direction.** *A -> B* (if non-symmetric) or *A <-> B*.
* **CL.** *0–3* with a short **why**.
* **Loss Notes (bullets).** What fails to carry (units, scope, granularity, preconditions, time stance).
* **Counter-example.** The crispest case where substitution would mislead.
* **Supported use.** *Naming-only / Role Assignment & Enactment-eligible / Type-structure / Explanation-only*.
* **Didactic hook.** The helpful sentence a careful engineer can remember.

*If it does not fit on a screen, you are describing the Contexts, not the Bridge.*

**Registry-reference note (normative).** `BridgeId` and any policy/edition identifiers cited by a Bridge Card are **registry references** (keys into registries), not semantic symbols exported by signatures. Therefore they MUST NOT be demanded via `SignatureManifest.provides` (or "satisfied" via `imports` closure); conformance is checked by validating that the referenced registry entries exist and, where required, are edition-pinned (see F.15).


### F.9:8a - State export and quantum-like boundary note

Use F.9 first when meaning, label, relation, field, record, model output, report, or representation crosses a bounded context or publication plane. A bridge does not become quantum-like because it is lossy, approximate, contextual, or hard to translate. It becomes quantum-like only when the bridge/export claim still depends on order sensitivity, incompatible frames, a probe that changes the represented state, or no faithful-enough export supports the intended use.

Action path:

1. Build the ordinary Bridge Card first: cells, sense family, kind, direction, CL, loss notes, counter-example, and Bridge-supported use.
2. Ask what state, relation, evidence, metric, option, or viability reading is claimed to survive the crossing.
3. State what the crossing omits, coarsens, re-keys, reframes, makes incomparable, or makes unsafe for the intended downstream use.
4. If the bridge or export claims to preserve action, intervention, manipulation, explanation, or cross-scale structure, state the causal-abstraction or approximate-causal-abstraction mapping before treating the coarsened bridge as a QL issue.
5. Ask whether asking, measuring, exporting, rendering, or bridging changes the represented state itself. If yes, coordinate with `C.26.1`.
6. Ask whether coordinated work or live state is not exported faithfully enough for the intended use by any one report or bridge. If yes, coordinate with `C.26.2`.
7. Ask whether the crossing is a state representation with declared source-loss mode or reduced recoverability. If yes, coordinate with CSC/RT and the C.26 coarsening support section.
8. State Bridge-supported use and return-to-source trigger before the bridge result is reused.

Add this row to the Bridge Card only when the bridge result will be reused for decision, comparison, assurance, release, audit, or cross-context action. For a local orientation note, state the export loss and return-to-source trigger in prose without treating the note as a Bridge Card extension.


| Field | Question |
| --- | --- |
| State reading claimed to survive | What state, relation, evidence, metric, option, or viability reading is claimed to survive the crossing |
| State lost or transformed | What is omitted, coarsened, re-keyed, re-framed, made incomparable, or no longer decision-safe |
| Probe / frame condition | Whether the act of asking, measuring, exporting, or rendering changes the represented state |
| Bridge-supported use | Which decision, explanation, triage, comparison, or orientation use remains supported after the crossing |
| Bridge-non-admissible use | Which substitution, release, audit, assurance, or action use requiring additional support is not supported by the Bridge card |
| Return-to-source trigger | When the bridge result is no longer enough and the source context, evidence carrier, or fuller representation must be reopened |

Useful outputs:

- an ordinary Bridge Card when translation/loss is the whole issue;
- a C.26.1 note when the export/probe changes represented state;
- a C.26.2 note when coordinated state has no faithful-enough export for the intended use;
- a CSC, RT, or C.26 coarsening handoff when the exported representation intentionally carries reduced detail, reduced recoverability, or narrower use.

### F.9:9 - Invariants (normative)


1. **Locality first.** A Bridge relates **SenseCells**, never Contexts or strings.
2. **senseFamily discipline.** **Substitution Bridges must be senseFamily-preserving**. **Interpretation Bridges** may cross senseFamilies but **never** support substitution.
3. **Direction clarity.** If the kind is directional, state direction explicitly.
4. **CL honesty.** Assign **CL** only if you can state at least one **counter-example** for `CL <= 2` or explain its absence with invariants for `CL = 3`.
5. **Loss visibility.** Every Bridge carries **Loss Notes** (even “none”).
6. **Row dependence.** A Concept-Set row’s **scope** is **bounded by the weakest CL** among its participating Bridges (F.7/F.8).
7. **No senseFamily jump by stealth.** You **must not** use an Interpretation Bridge to justify a **row** or **substitution**.
8. **Time DesignRunTag honesty.** If a Context fixes **DesignRunTag**, the Bridge must respect that distinction or explicitly declare a bridge such as `Design-spec -> Run-trace`.
9. **Kernel restraint.** Bridges **cannot** be used to promote ad-hoc sameness into a new **U.Type**; A.11 applies.
10. **Non-inheritance of Contexts.** Bridges **do not** imply -is-a- between Contexts (E.10.D1).
11. **Coarsened-note restraint.** A lighter cross-context note, comparative aid, redacted view, or surrogate **SHALL NOT** be treated as a Bridge Card or as bridge or substitution support by convenience. If bridge-bearing use is still wanted, the source-bearing episteme or source publication needed for bridge support must be reopened and the bridge must be declared explicitly with kind, direction, `CL`, and loss notes.


### F.9:10 - Micro-examples (illustrative, one-liners)

1. **Participant vs Agent (process model vs provenance)**
   *Cells:* `BPMN:Participant` - `PROV:Agent` - *senseFamily:* Role - *Kind:* `Partial-overlap` - *CL:* 2 - *Loss:* participation vs attribution scopes differ - *Use:* **Naming-only** ("actor").

2. **Process (design) vs Activity (run)**
   *Cells:* `BPMN:Process` -> `PROV:Activity` - *senseFamily:* Method / Execution - *Kind:* **Design-spec -> Run-trace** - *CL:* 2 - *Loss:* graph vs event; concurrency vs temporalization - *Use:* **Explanation-only**.

3. **Observation vs SLO check**
   *Cells:* `SOSA:Observation` -> `ITIL:SLO-fulfilment` - *senseFamily:* Measurement / Status - *Kind:* `Measure-of` - *CL:* 2 - *Loss:* sampling window; target definition - *Use:* **Explanation-only**.

4. **Subtype across OWL and curated taxonomy**
   *Cells:* `OWL:SubClassOf` - `TaxonomyX:is-a` - *senseFamily:* Type-structure - *Kind:* `Equivalence` - *CL:* 3 *(only if TaxonomyX is acyclic and anti-symmetric)* - *Loss:* profile differences - *Use:* **Type-structure** rows supported.

5. **Accuracy (metrology vs data-quality)**
   *Cells:* `ISO80000:accuracy` - `ISO25024:accuracy` - *senseFamily:* Measurement - *Kind:* `Partial-overlap` - *CL:* 2 - *Loss:* instrument vs dataset perspective - *Use:* **Naming-only** row -accuracy-; methods stay context-local.

### F.9:11 - Anti-patterns & remedies

| ID    | Anti-pattern | Symptom | Why it breaks thinking | Remedy (conceptual move) |
| --------- | -------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **AP-1** | **String-equals = sense-equals** | Same spelling used across Contexts with silent identity claims. | Violates locality; invites false substitution. | Always state a **Bridge kind**; if unsure, default to **Partial-overlap** with **Naming-only** scope. |
| **AP-2**  | **Stealth substitution**         | “We’ll just treat A like B for now.”                                              | Hidden policy with unknown loss; leaks into Role Assignment & Enactment.    | Publish a **Bridge Card** with **Loss Notes** and **CL**; if CL<2, substitution remains **unsupported**.      |
| **AP-3** | **Stance jump by wording** | -Activity (PROV) is a Process (BPMN).- | DesignRunTag confusion; swaps graphs for events. | Use a **Design-spec -> Run-trace** Interpretation Bridge, not a substitution bridge; keep **Explanation-only** scope. |
| **AP-4** | **Symmetry hallucination** | Treating directional bridges as if they were symmetric. | Narrows broadened, broadens narrowed; unsafe reuse. | Record **direction** explicitly; only **Equivalence** is symmetric. |
| **AP-5** | **Disjoint but reused** | Declare `Disjoint` and still borrow labels or Role Description constraints (RCS/RSG). | Contradiction between declaration and use. | Either retract `Disjoint` or stop reuse; if a thin thread exists, rename it as **contrastive explanation** (no row). |
| **AP-6** | **CL without counter-example** | -These are CL=3- with no invariant check. | Inflates trust; over-supports structural rows. | For **CL=3**, cite the **matching invariants**; otherwise, demote to **CL=2** and add a counter-example. |
| **AP-7** | **Bridge inflation** | Dozens of nearly identical Bridges between the same Contexts. | Noise masks the few material alignments. | Prefer **one Bridge per pair of Cells per senseFamily**; fold variants into **Loss Notes**. |
| **AP-8** | **Row outruns Bridge** | A Concept-Set row claims Role Assignment & Enactment-eligibility where some participating Bridges are `CL = 1`. | Row scope exceeds the weakest link. | Apply the **weakest-link rule** (F.7/F.8): row scope <= `min(CL)`; otherwise split the row. |
| **AP-9** | **Bridge as new U.Type** | Using a Bridge to justify minting a new universal Type. | Re-globalises meaning; breaks A.11 parsimony. | Keep Types context-local; where reuse is needed, use **rows** + Bridges, not new primitives. |
| **AP-10** | **Silent unit-and-scale mismatch** | Transporting measurements without unit and scale notes. | Hidden dimensional error. | Record units and scales in **Loss Notes**; if units cannot be related, use **Disjoint** or **Partial-overlap** with **Naming-only** scope. |
| **AP-11** | **Coarsened note treated as bridge support** | A summary, redacted comparison, or partner-facing simplification is used as if it already supported substitution or interoperability claims. | A bridge claim is being smuggled through a coarsened rendering that only made lighter review or orientation admissible. | Reopen the source-bearing episteme or source publication needed for bridge support and publish the actual Bridge Card before any bridge-bearing or substitution use. |


### F.9:12 - Worked examples (didactic)

#### F.9:12.1 - Service acceptance (design) vs executions & observations (run)

* **Cells & Contexts**
  `ITIL4:SLO` *(Status, design)* <- `SOSA:Observation(availability)` *(Measurement, run)*
  `BPMN:Process` *(Method, design)* -> `IEC61131:Task-Execution` *(Execution, run)*
* **Narrative**
  Availability SLOs are **evaluated** by observations of task executions. No substitution follows: an SLO is not an observation, and a process is not an execution occurrence.
* **Bridge Cards (sketch)**
  *ITIL\:SLO <- SOSA\:Observation* - **CL=2** - Loss: sampling window, clock skew.
  *BPMN\:Process -> IEC\:Execution* - **CL=2** - Loss: control-flow vs temporalization, concurrency collapse.
* **Supported use**
  Explanation-only; Concept-Set rows may be **Naming-only** ("availability") with **CL >= 1** label coherence across Contexts.


#### F.9:12.2 - Behavioural role vs access role

* **Cells & Contexts**
  `BPMN:Participant` *(Role)* - `NIST-RBAC:Role` *(Status)*
* **Narrative**
  Both talk about -who acts-, but one is a **behavioural mask** in a process model, while the other is an **authorization grouping**.
* **Bridge**
  **Kind:** `Partial-overlap`, **CL=2**; Loss: assignment moment, enforcement placement, multiplicity.
* **Supported use**
* **Naming-only** row “actor”; **no Role Assignment & Enactment reuse** across senseFamilies.


#### F.9:12.3 - Equivalence of subtype notions for structural rows

* **Cells & Contexts**
  `OWL2:SubClassOf` *(Type-structure)* - `TaxX:is-a` *(Type-structure curated)*
* **Bridge**
  **Kind:** `Equivalence`, **CL=3** **iff** the curated taxonomy is **acyclic and anti-symmetric** and uses class-level reasoning.
* **Supported use**
  **Type-structure** rows supported (`CL = 3`); Loss: OWL profile limitations (RL/EL/QO).


#### F.9:12.4 - Accuracy (metrology) vs accuracy (data-quality)

* **Cells & Contexts**
  `ISO80000:measurement-accuracy` *(Measurement)* - `ISO25024:data-accuracy` *(Measurement)*
* **Bridge**
  **Kind:** overlap, **CL=2**; Loss: “true value” notion differs (instrument vs dataset), scale transformations.
* **Supported use**
  **Naming-only** row “accuracy” used for reports; no shared methods.


#### F.9:12.5 - Setpoint (control) vs target (service)

* **Cells & Contexts**
  `CTRL:text:setpoint` *(Status/Control)* - `ITIL:target` *(Status/Service)*
* **Bridge**
  **Kind:** `Disjoint` - Rationale: physical reference value vs business objective; different target kinds (control parameters vs requirement clause).
* **Supported use**
  Didactic contrast only; prevents accidental substitution in SLO calculus.

#### F.9:12.6 - Role substitution & CL gating (RoleAssignment/enactment scope)

> **Use.** A worked, role-focused restatement of Bridge usage for the recurring question:
> “May `Role_B@B` satisfy `Role_A@A` for `requiredRoles` / enactment checks-”

**Rule.** **No cross-context substitution by name.** If a step in **Context A** needs `Role_A`, and the performer only holds `Role_B` in **Context B**, an explicit **Bridge** **MUST** state how `Role_B@B` relates to `Role_A@A`, with direction, **CL**, and Loss Notes.

##### F.9:12.6.1 - Directional substitution (role-oriented shorthand)

A Bridge may assert, *directionally*:

* **`substitutesFor(Role_B@B > Role_A@A)`** with a CL and a list of **kept** and **lost** characteristics (for roles: typical losses are RCS characteristics and/or RSG nuances).
* The reverse direction **does not** follow unless declared (F.9:13.7).

##### F.9:12.6.2 - CL > gating policy (didactic default)

| **CL** | Meaning (intuitive)                     | **Supported scope** | **Extra condition**                                                                  | **Unsupported by default** |
| :----: | --------------------------------------- | :--------: | ------------------------------------------------------------------------------------ | :-------: |
|  **3** | Near-isomorphic sense; no material loss | Yes | None beyond ordinary gates (e.g., window + RSG state) | - |
|  **2** | Close but with stated losses            |    Yes     | Require **extra evidence** (e.g., additional checklist item) **or** a named checker |     —     |
|  **1** | Distant analogy; risky                  | Exception  | Only by explicit **Waiver SpeechAct** naming the Bridge + loss rationale             |  Default  |
|  **0** | Incompatible                            |     No     | —                                                                                    |    Yes    |

*Notes.* The **substitution scope** is defined in **F.9:13.2-13.3** (Role-Assignment/Enactment-eligible substitution requires **CL >= 2**; Naming-only is **CL >= 1**).
CL penalties feed assurance (R) per **B.3**; safety-critical policies may require **CL >= 2** by default (D.2).

##### F.9:12.6.3 - Typical bridges (worked patterns)

* **BPMN Task - PROV Activity.**
  `substitutesFor(Task@BPMN > Activity@PROV)` with **CL=2**; **lost:** BPMN control-flow guards; **kept:** “bounded occurrence consuming/producing entities.”
  *Effect.* A Work logged as `Activity@PROV` may satisfy a step requiring a `Task@BPMN` **iff** an extra guard enforces the BPMN pre-/post-conditions.

* **Essence Alpha-State - RoleStateGraph state.**
  `substitutesFor(“Alpha.State:Ready”@Essence > “Ready”@RSG)` with **CL=2**; **lost:** Alpha-specific narrative criteria; **kept:** checklist-based readiness.
  *Effect.* A team may reuse Essence states as labels in RSG, but still maintains local checklists as **StateAssertions**.

* **ITIL Service Owner - RBAC Administrator.**
  Typically **CL=1** and **directional** (Administrator\@RBAC > ServiceOwner\@ITIL) **rejected** unless a policy Bridge enumerates compensating controls.
  *Effect.* Prevents “ops admin = service-accountability role” conflations without an explicit waiver.

##### F.9:12.6.4 - Bridge invariants (role-relevant reminders)

* **Local first.** Substitution never overrides in-Context role algebra (its own role relations, guards, and exclusions).
* **Loss honesty.** If a Bridge’s loss notes indicate that a dropped characteristic is required by a step, substitution is invalid (regardless of CL).
* **No silent inversion.** Direction is explicit; substitution does not reverse unless declared (F.9:13.7).

### F.9:13 - Reasoning primitives (judgement schemas)

> **All judgements are conceptual.** They support or reject specific *thinking moves*-not enactment steps and not process-enactment records.

#### F.9:13.1 - Bridge declaration

`Bridge(A@RA, B@RB) : senseFamily, kind, dir, CL, Loss, scope`

*Reading:* There exists a declared Bridge between SenseCells `A` and `B` with stated attributes.


#### F.9:13.2 - Substitution scope (senseFamily-preserving)

`Bridge(A,B): same senseFamily f, kind in {Equivalence, Narrower-than, Broader-than}, dir A->B, CL>=2, Loss L -> A may stand in for B at senseFamily f (Role-Assignment/Enactment-eligible)`

*Reading:* A **Substitution Bridge** on the same senseFamily with **CL >= 2** supports **Role-Assignment/Enactment-level** substitution **in the stated direction**. (`Type-structure` requires **CL = 3**.)


#### F.9:13.3 - Naming-only scope

`Bridge(A,B): kind in {Equivalence, Narrower-than, Broader-than, Partial-overlap}, CL>=1 -> A and B may share a label (Naming-only)`

*Reading:* A Bridge with **CL >= 1** supports using a shared label in prose or Concept-Set **Naming-only** rows, without structural or Role Assignment & Enactment commitments.


#### F.9:13.4 - Prohibition by kind

`Bridge(A,B): kind=Disjoint -> no substitution and no shared row`

*Reading:* **Disjoint** supports neither substitution nor rows; only contrastive teaching remains supported.


#### F.9:13.5 - Interpretation embargo

`Bridge(A,B): kind in {Design-spec -> Run-trace, Measure-of, Policy-implies} -> Explanation-only`

*Reading:* **Interpretation Bridges** never support substitution or rows.


#### F.9:13.6 - Weakest-link rule for rows

`row R uses {Bridge_i} -> scope(R) = min_i(scopeSupported(Bridge_i)) and CL(R) = min_i(CL_i)`

*Reading:* The **row scope** and **row CL** are bounded by the weakest participating Bridge.


#### F.9:13.7 - Direction guard

`Bridge kind=Narrower-than with dir A->B -> not(B may stand in for A)`

*Reading:* Narrower>Broader does **not** invert; only A may substitute into B under the stated scope.


#### F.9:13.8 - SenseFamily purity

`Bridge scope=Role Assignment & Enactment-eligible -> same senseFamily(A,B) and same stance(A,B)`

*Reading:* Role Assignment & Enactment-level substitution requires **same senseFamily** and same stance (run-time or design time).


#### F.9:13.9 - Loss accumulation

`A->B with Loss L1 and B->C with Loss L2 -> A->C is supported only if the same senseFamily is preserved, CL=min(CL1,CL2), and Loss accumulates as L1 union L2`

*Reading:* Chained substitution is rarer; if used, **accumulate Loss** and respect the **minimum CL**. When in doubt, avoid chaining across Contexts.


### F.9:14 - Relations

**Builds on:** E.10.D1 (Context discipline: Context = U.BoundedContext); **F.0.1 (senseFamily guard; Bridge-only crossing)**; F.1 (Contexts fixed); F.2/F.3 (Cells exist); F.7 (rows depend on Bridges); F.8 (thresholds and reuse choice).

**Coordinates with:** `F.9.1` for stance overlays that remain subordinate to bridge cards; `E.17.1` when viewpoint bundles need explicit cross-family correspondence; `C.16.Q` / `C.25` when evaluative endpoints or bundle-shaped quality families cite bridge cards without absorbing bridge semantics.

**Constrains:**

* **F.7 Concept-Set Table:** each cross-context row must name supporting **Bridges**; row scope <= the weakest supporting Bridge.
* **F.8 Mint or Reuse:** reuse choices reference **CL** and **kind**; no reuse without a Bridge.
* **Part C patterns:** formal claims that span Contexts cite Bridges and respect senseFamily/StatusModality & CL constraints.
* **B.3 Trust & Assurance Calculus:** may interpret **CL** as a penalty factor in Cross-context reasoning.


### F.9:15 - Migration notes (conceptual)

1. **Edition shift in a Context.** Re-read affected **Cells**; if sense moved, split the Bridge or **lower CL**; keep the older Bridge for historical claims.
2. **New evidence of mismatch.** Add a **counter-example**; decrease `CL` or change bridge kind (for example from `Equivalence` to `Partial-overlap` or `Disjoint`).
3. **Convergence over time.** When invariants demonstrably match, and counter-examples evaporate, **raise CL** cautiously; for **CL=3**, cite invariants.
4. **senseFamily refactor.** If a Cell’s senseFamily was mis-typed, fix the senseFamily first in F.3, then revisit Bridges; **Interpretation** is safer than forced substitution.
5. **Row under-protected.** If a row’s scope exceeds the weakest Bridge, either **split the row** by Context or **downgrade scope** to Naming-only.
6. **Bridge sprawl.** Consolidate near-duplicates into one Bridge with richer **Loss Notes**; retire the rest.


### F.9:16 - Acceptance tests (SCR/RSCR — concept-level)

#### F.9:16.1 - Static conformance (SCR)

* **SCR-F9-S01 (Well-typed).** Every Bridge names **two SenseCells**, each bound to a **Context** from F.1, and states **senseFamily**, **kind**, **dir** (if needed), **CL**, **Loss**, and **scope**.
* **SCR-F9-S02 (senseFamily discipline).** Any Bridge that supports **Role/Enactment-eligible** substitution is **senseFamily-preserving** and has kind in {`Equivalence`, `Narrower-than`, `Broader-than`}.
* **SCR-F9-S03 (Loss visibility).** Every Bridge has **non-empty Loss Notes** (the word "none" is valid only with **CL=3** and stated invariants).
* **SCR-F9-S04 (Counter-example hygiene).** Bridges with **CL <= 2** carry at least one **counter-example**; Bridges with **CL=3** cite **matching invariants**.
* **SCR-F9-S05 (Row compliance).** Every Concept-Set row shows a **scope** no greater than the **minimum CL** across its supporting Bridges; no row relies on **Interpretation** Bridges.

#### F.9:16.2 - Regression (RSCR)

* **RSCR-F9-E01 (Edition churn).** When a Context's edition changes, re-validate all Bridges touching it; flag `CL` drift and update rows' scopes if needed.
* **RSCR-F9-E02 (Counter-example drift).** New counter-examples lower **CL**; deletions do not automatically raise **CL**.
* **RSCR-F9-E03 (senseFamily drift).** If a Cell's `senseFamily` is corrected, all Bridges crossing that Cell are re-typed; any substitution that would now cross senseFamilies is invalidated.
* **RSCR-F9-E04 (Weakest-link enforcement).** Adding a low-CL Bridge to a row reduces the row's scope; if the row's published scope would exceed the new minimum, split or downgrade the row.


### F.9:17 - Didactic distillation (90-second script)

> A **Bridge** translates between **local senses** from different **Contexts**. It always declares **what relation** holds (`Equivalence`, `Narrower-than`, `Broader-than`, `Partial-overlap`, `Disjoint`, or an interpretation such as `Design-spec -> Run-trace`), **which CL value applies** (`CL 0-3`), **which way** (when direction matters), and **what is lost**. **Substitution** is supported only on the **same senseFamily** and only with **CL >= 2**; **Type-structure** needs **CL = 3**. **Interpretation Bridges** explain, never substitute. Rows in the Concept-Set table obey the **weakest-link**: their scope cannot exceed the lowest `CL` among their Bridges. When editions change or counter-examples appear, lower `CL` or change bridge kind; if two senses truly converge and invariants match, raise to **CL = 3**, rarely and with reasons. Translate across Contexts; never collapse them.

#### F.9:17.1 - Bridge stance overlay compatibility
A bridge card may carry a `F.9.1` Bridge Stance Overlay such as `localRename`, `operationalizes`, `partialAnalogy`, `projection`, or `nonEquivalent`. The overlay is a local interpretive annotation and **does not replace** the underlying bridge kind, direction, `CL`, or loss notes.

### F.9:18 - Archetypal Grounding

#### F.9:18.1 - Tell

A Bridge is not a synonym claim and not an enactment edge. It is a context-bounded correspondence record that tells a reader what may be reused, what may only be explained, and what is lost when meaning is transported.

#### F.9:18.2 - Show (System lane)

A service team may reuse the word *availability* across monitoring, SLO review, and architecture discussion. F.9 requires the team to publish Bridge Cards that separate observation, status target, and architectural concern rather than treating the shared label as silent sameness. The benefit is that naming convenience survives while substitution rights stay bounded by `senseFamily`, `CL`, and Loss Notes.

#### F.9:18.3 - Show (Episteme lane)

A comparative bundle may say that two traditions both discuss *readiness* or *capability*. Under F.9, that statement is only explanatory until the author publishes the two SenseCells, the Bridge kind, direction, `CL`, and the counter-example that marks where the comparison stops. The Bridge then becomes an auditable correspondence rather than a rhetorical shortcut.

#### F.9:18.4 - Coarsened cross-context note is not yet a Bridge Card

A service or review bundle may circulate a short cross-context note such as `the vendor bulletin is basically the same readiness signal as our rollback worksheet`. That note may be useful as informal orientation talk, but it is not yet an admissible Bridge Card and not yet a formal `F.9` `Naming-only` row.

Before any substitution, equivalence, `Naming-only` row, or interoperability claim is made, the source-bearing episteme or source publication needed for bridge support must be reopened and an explicit Bridge Card must publish the two SenseCells, bridge kind, direction, `CL`, Loss Notes, and admissible use. Friendly summary prose does not carry bridge support by itself.

### F.9:19 - Bias-Annotation


Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: **Universal** for cross-context correspondence and reuse.

* **Gov bias:** F.9 raises the declaration bar by requiring explicit Bridge Cards.
  *Mitigation:* keep the card compact and teach weakest-link discipline as the default review heuristic.
* **Arch bias:** the pattern prefers typed bridge declarations over friendly synonym prose.
  *Mitigation:* allow Naming-only scope and explanatory Interpretation Bridges so useful comparisons are not blocked.
* **Onto/Epist bias:** F.9 is local-first and resists global meaning claims.
  *Mitigation:* reuse remains possible, but only through explicit correspondence, direction, and Loss Notes.
* **Prag bias:** conservative `CL` assignment may feel slower than informal reuse.
  *Mitigation:* the pattern still supports bounded substitution when the evidence is good enough; it only blocks silent overreach.
* **Did bias:** the didactic script can make Bridge Cards look simpler than they are.
  *Mitigation:* Conformance, counter-examples, and weakest-link rules keep the teaching explanation tied to real constraints.

### F.9:20 - Conformance Checklist (CC-F.9)

A Bridge publication conforms to F.9 iff:

1. **CC-F.9-1 - Well-typed Bridge declaration.**
   Every Bridge names two SenseCells bound to declared Contexts and publishes kind, direction (if needed), `CL`, Loss Notes, and Bridge-supported use.
2. **CC-F.9-2 - Substitution discipline.**
   Any substitution or row support comes only from a Substitution Bridge on the same `senseFamily`; Role Assignment & Enactment-level substitution requires `CL >= 2`, and Type-structure substitution requires `CL = 3` plus matched invariants.
3. **CC-F.9-3 - Interpretation embargo.**
   Interpretation Bridges remain explanation-only and are not used to justify substitution or Concept-Set rows.
4. **CC-F.9-4 - CL honesty and loss visibility.**
   Bridges with `CL <= 2` publish a counter-example or explicit boundary case; Bridges with `CL = 3` publish the invariants that justify the higher-scope use; all Bridges publish Loss Notes.
5. **CC-F.9-5 - Weakest-link row discipline.**
   Cross-context rows never claim a broader scope or higher row-level `CL` than the participating Bridges support.
6. **CC-F.9-6 - Overlay non-collapse.**
   If a `F.9.1` Bridge Stance Overlay is used, it remains an annotation and does not replace bridge kind, direction, `CL`, or Loss Notes.
7. **CC-F.9-7 - Registry-reference discipline.**
   `BridgeId` and cited policy pins are treated as registry references, not as signature-exported semantic symbols.

8. **CC-F.9-8 - Coarsened cross-context note is not treated as a Bridge Card.**
   If bridge-bearing reuse begins from a lighter note, summary, or comparison aid, the source-bearing episteme or source publication needed for bridge support is reopened and a full Bridge Card is published before any equivalence, substitution, `Naming-only` row, interoperability, or other row support is claimed.

### F.9:21 - Consequences


**Benefits.**
F.9 lets FPF compare, translate, and partially reuse ideas across Contexts without collapsing them into one vocabulary. It gives downstream rows, claims, and assurance reasoning an explicit Bridge Card record instead of relying on prose intuition.

**Trade-offs / mitigations.**
The pattern adds explicit bridge declaration and may feel heavier than informal comparison. Mitigation: use Naming-only scope when explanation is enough, and reserve higher-scope uses for Bridges that carry the required `CL` and invariants.

### F.9:22 - Rationale

The core move of F.9 is simple: cross-context work is unavoidable, but silent sameness is unacceptable. A Bridge therefore does two jobs at once:

* it preserves practical reuse where bounded transport is genuinely available, and
* it keeps non-identity visible through direction, Loss Notes, `CL`, and weakest-link scope.

Without that discipline, every shared label becomes a hidden ontology merger. With it, cross-context comparison stays teachable, auditable, and compatible with the rest of FPF.

### F.9:23 - SoTA-Echoing

**SoTA note.** This section does not mint an independent second bridge rule track. It stays truthful only when Bridge kinds, `CL`, Loss Notes, weakest-link scope, the `A.6.3.CSC` neighbor boundary, and the review matrix below still tell the same story about admissible cross-context reading.

| Claim need | SoTA practice (post-2015) | Primary source (post-2015) | Alignment with `F.9` | Adoption status |
| --- | --- | --- | --- | --- |
| Shared labels across contexts are not enough for supported cross-context reuse. | Terminology and ontology practice distinguishes objects, concepts, definitions, designations, and typed relations instead of treating the same string as identity. | ISO 704:2022; ISO 1087:2019; ISO/IEC 21838-2:2021 (BFO). | `F.9` requires typed SenseCells, bridge kind, direction where needed, `CL`, and Loss Notes rather than string-equals identity. | **Adopt/Adapt.** Adopt explicit term/concept/relation discipline; adapt it into Bridge Cards; reject lexical sameness as reuse support. |
| Viewpoint and context boundaries must stay explicit when descriptions are reused. | Architecture-description practice distinguishes an entity of interest, architecture description, viewpoint, view, model kind, concern, and correspondence. | ISO/IEC/IEEE 42010:2022. | `F.9` binds every Bridge to declared Contexts and forces downstream rows to obey weakest-link scope instead of outrunning the supporting correspondences. | **Adopt.** Adopt boundary-explicit architecture-description discipline and apply it to FPF cross-context bridge cards. |
| Data/catalog/validation practice separates metadata, validation conditions, and exchange support from substitution authority. | Web-data and semantic-web standards make metadata, provenance, structural constraints, validation, and catalog federation explicit without turning metadata into the data itself. | W3C Data on the Web Best Practices (2017); W3C SHACL (2017); W3C DCAT v3 (2024). | `F.9` separates explanatory/interpretive bridges from substitution bridges and keeps bridge publication distinct from coarsened notes or catalog-style discovery aids. | **Adapt/Reject.** Adapt explicit metadata and validation practice; reject treating discovery, gloss, or validation support as substitution support. |
| Model-based engineering uses traceable model elements and formal semantics, but tool interoperability is not itself semantic identity. | Current MBSE practice improves precision, traceability, and interoperability through explicit model elements, libraries, APIs, and formal semantics. | OMG SysML v2.0 Language Specification (2025); OMG KerML v1.0 Specification (2025). | `F.9` uses Bridge Cards as human-readable, reviewable relations whose `CL` and loss fields remain narrower than and do not replace any hidden tool or model interchange claim. | **Adapt.** Adopt traceable relation discipline; reject tool or interchange success as proof of same meaning. |

**Worked-slice docking.** The nearest practical recovery anchors here are the micro-examples in `F.9:10`, the worked examples in `F.9:12`, the revision law in `F.9:14`, and the review matrix in `F.9:26`. If the SoTA claim cannot be recovered through those explicit bridge-card anchors, do not let the alignment rationale stand in for live bridge law.

**Local stance.** Best-known current practice supports a narrow rule: cross-context reuse is admissible only when correspondence is typed, directional where needed, explicit about loss, and narrower than silent lexical identity or convenience equivalence.

### F.9:24 - Bridge Card Publication Discipline

#### F.9:24.1 - Minimal bridge-card declaration
A usable Bridge Card should make visible:

- the two typed SenseCells,
- the bridge kind,
- direction where direction matters,
- declared `senseFamily`,
- `CL`,
- explicit Loss Notes,
- and the Bridge-supported use or row consequence.

If any of these fields is absent, later readers are forced back into inference by prose similarity, which is exactly what `F.9` is supposed to block.

#### F.9:24.2 - One-pair default rule
The default declaration discipline is one primary Bridge per cell pair per relevant `senseFamily`, with richer Loss Notes rather than many near-duplicate cards. Local exceptions are admissible only when the cards genuinely differ in bridge kind, direction, or admissible use.

#### F.9:24.3 - Revision over silent drift
If later evidence changes bridge `CL`, direction, or loss, the Bridge Card should be revised explicitly. It should not be left in place while surrounding prose quietly changes the practical scope.

### F.9:25 - Bundle and Endpoint Interaction Law

#### F.9:25.1 - Viewpoint and bundle interaction
Viewpoint bundles, quality bundles, and other endpoint bundles may cite Bridges, but they do not absorb bridge semantics. `F.9` remains the pattern for cross-context alignment, while the citing bundle keeps its own ontology.

#### F.9:25.2 - Quality-family interaction
When a quality family claim crosses contexts, bridge loss and `CL` affect what may be compared or reused, but they do not retype the quality family itself. Any resulting assurance penalty feeds `R` rather than changing the ontology of `F`, `G`, or the Q-Bundle head.

#### F.9:25.3 - Overlay interaction rule
A `F.9.1` stance overlay may help readers interpret a bridge, but the bridge card remains primary. If the overlay overstates the bridge kind, direction, `CL`, or Loss Notes, the card wins and the overlay should be narrowed or removed.

### F.9:26 - Review Matrix and Migration Tests

A reader can test bridge integrity with six questions:

1. **Are the two cells and contexts explicit?**
2. **Is the bridge kind the least-committing truthful kind rather than the friendliest one?**
3. **Does `CL` match the published counter-example or invariant evidence?**
4. **Are Loss Notes specific enough that the Bridge-supported use is really bounded?**
5. **If a row or bundle cites the bridge, does it stay within the Bridge-supported use?**
6. **If a stance overlay exists, does it stay within the bridge card's kind, direction, `CL`, and Loss Notes?**

Migration from legacy "same/equivalent/align/map" prose should therefore recover the Bridge Card first, then any row support, then any optional stance overlay. Doing it in the opposite order recreates silent equivalence under new vocabulary.
### F.9:14a - C.29 MLA relation

> When meaning, substitution, sense cells, direction, `CL`, or Bridge-supported use crosses context, write the `F.9` Bridge Card first. Add the applicable `C.29` output only for mathematical-lens adequacy: candidate mathematical object, lens-mapping posture, preserved and lost structure, exposed invariants or distinctions, support posture, use-rights, and stop condition. Do not duplicate Bridge semantics inside MLA. A Bridge may make a mathematical lens interpretable across contexts without making it substitution-safe.

### F.9:End

