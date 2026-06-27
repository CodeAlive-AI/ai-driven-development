## C.20 - Composition of `U.Discipline` (Discipline‑CAL)
> **Status:** Stable
> **Type:** Pattern

### E.24.UK settlement

`U.Discipline` is the root durable holon kind used for field-level practice-and-knowledge wholes. Its EntityOfConcern lets FPF users talk about a discipline as one reusable object without collapsing it into a domain label, bounded context, organization, publication set, or tradition name.

The identity of a `U.Discipline` is held by a composition relation over five required positions:

- **Episteme canon:** theories, models, reference works, definitions, proof traditions, benchmark descriptions, and other epistemes treated as canonical in the discipline;
- **standards and practices:** accepted methods, norms, standard procedures, measurement conventions, and admissible comparison rules;
- **organizational carriers:** journals, committees, curricula, professional bodies, labs, or institutional arrangements that carry and refresh the discipline without being identical to it;
- **bridge set:** F.9/F.17 bridge and term rows that state how the discipline is reused across bounded contexts and source traditions;
- **comparison governance:** characteristic, scale, evidence, and CG-Spec references that make comparisons inside or across disciplines admissible.

This makes `U.Discipline` a `U.Holon`: it is a whole with epistemic, organizational, practice, bridge, and comparison-governance parts. It is not a `U.System` by default; some organizational carriers are systems, but the discipline holon includes epistemes and practices as well. It is not merely a `U.Episteme`; the canon is only one position in the discipline composition.

Boundary: a **domain** names a subject area or catalog stitch; a **bounded context** names a local meaning frame; a **discipline** names the composed field-level holon that carries canon, practices, carriers, bridges, and comparison governance. Similar words across domains do not make one discipline; bridge and loss notes are required.

`U.AppliedDiscipline` and `U.Transdiscipline` are C.3-governed subkind values under `U.Discipline`, not separate root ontics. `U.Tradition` and `U.Lineage` are not root U-kinds in C.20 because they name variant, edition, school, or provenance structures inside or across disciplines; write them as ordinary auxiliary values or C.3 local kinds unless a direct governing pattern supplies their own identity relation, admissible use, and E.24.UK settlement.

**Builds on.** **C.2 KD-CAL** (F-G-R and the CL-to-R penalty rule), **A.19/G.0 CG-Spec** (comparability), **F.9 Bridges** (cross-context alignment), **E.10 LEX** (registers & twin labels). **Coordinates with.** **C.21** (Discipline-CHR, field health), **C.23** (Method-SoS-LOG), **F.17-F.18** (UTS).

### C.20:0 - Use This When

Use this pattern when a project must treat a discipline as a durable field-level object, not as a loose domain label or a list of documents. Typical cases include comparing safety engineering traditions, moving a practice across bounded contexts, judging whether a method family belongs to a field, or keeping a discipline edition stable while its canon and standards change.

**What goes wrong if missed.** A field name starts doing the work of canon, practice, institutional carrier, bridge, and comparison governance at once; cross-context reuse then looks valid while meanings, evidence lanes, and comparison rules have already drifted.

**What this buys.** The discipline name becomes a reviewable holon with named composition positions, bridges, and comparison rules, so users can compare, transport, steward, or edition a field without turning it into a document list or a domain label.

**Primary EntityOfConcern.** The EntityOfConcern is `U.Discipline`: a field-level practice-and-knowledge holon composed by canon epistemes, accepted practices and standards, organizational carriers, bridges, and comparison governance.

**First useful move.** State the five composition positions and the bridge/loss notes before using the discipline name in comparisons, selectors, or maturity claims.

**Not this pattern when.** A subject label alone belongs to domain/catalog work; local meaning belongs to bounded context; one theory or standard belongs to episteme/publication work; a school, edition, or lineage remains an auxiliary value unless a direct governing pattern admits it.

### C.20:1 - Problem Frame
Disciplines persist as *knowledge canons* (epistemes), *codified practices and standards*, and *institutional carriers* (journals, bodies, curricula). FPF needs a typed, provenance-preserving way to **compose** these into a reusable field-level holon that can be used across contexts *admissibly*. Composition must honour KD-CAL lanes and the CG-Spec Standard so that any numeric comparison or aggregation remains auditable and scale-admissible.

### C.20:2 - Problem
Without a **composition calculus** for disciplines:
* fields degenerate into labels; editions and rival **Traditions/Lineages** blur;
* cross-context reuse silently drops meaning when no Bridge and loss notes are present, or performs inadmissible aggregations (means on ordinals; unit mixing);
* selectors (Part G) cannot admissibly gate methods because maturity and evidence are not tied to a field's canon and carriers.

### C.20:3 - Forces
| Force | Tension |
|---|---|
| **Pluralism vs Cohesion** | Rival traditions must co-exist while a discipline holon presents a coherent public identity. |
| **Locality vs Federation** | Meaning is context‑local (rooms) ↔ reuse needs Bridges with CL and recorded loss notes. |
| **Rigor vs Agility** | CG-Spec admissibility and KD-CAL lanes need to remain usable during practical authoring and edition work. |
| **Didactic presentation vs Assurance depth** | Human-readable Discipline Card needs to remain tied to auditable F-G-R and provenance. |

### C.20:4 - Solution — the **Discipline holon** and Γ_disc

#### C.20:4.1 - U-kind settlement and registers
* **`U.Discipline`** — a **Holon** that composes an **EpistemeCanon**, **Standards/Practices**, and **Organisational Carriers** into a durable field-level EntityOfConcern.
* **`U.AppliedDiscipline`**, **`U.Transdiscipline`** — C.3-governed subkind values under `U.Discipline`; they are not separate root ontics.
* **Tradition and lineage values** — auxiliary holon-like values that organise variants or editions within a `U.Discipline`; write them without `U.` unless a direct governing pattern admits `U.Tradition` or `U.Lineage` by E.24.UK settlement.

**Placement and naming.** `U.Discipline` is governed by this pattern as the direct root durable U-kind. Its subkinds follow C.3/C.3.1 and F.5 naming discipline, E.10/F.17 register discipline, and A.11 parsimony. C.20 does not treat discipline names as candidate U-kinds merely because they appear in discipline-composition prose; a discipline kind needs the C.20 settlement plus ordinary U-kind admission evidence.

#### C.20:4.2 - What a `U.Discipline` is / is not
* A `U.Discipline` is **not** a `U.BoundedContext` and **not** a **Domain**. **Domain** remains a *catalog label* (stitched to D.CTX + UTS): **Discipline ≠ Domain** is enforceable via **E.10 LexicalCheck**; any cross-domain or cross-context reuse cites a **Bridge (F.9)** with **CL** and loss notes; penalties apply to **R** only; **F** and **G** remain invariant (USM/KD‑CAL).
* **Comparability** of a discipline is carried **only by** the discipline’s **CG-Spec** entries (no ad-hoc formulas).
* Cross-context or cross-tradition reuse uses **Bridges** with **CL** and loss notes; **CL penalties apply to R** (KD-CAL/B.3); **F** and **G** remain invariant.
* Public names obey **LEX** (EntityOfConcern, Description, specification-use, twin labels, banned heads); “discipline column” is **didactic only** and **carries no semantics** (enforced by LexicalCheck).

#### C.20:4.3 - Constructor **Γ_disc** (CAL export)
*Signature.*
`Γ_disc : ⟨EpistemeCanon, StandardsSet, OrgCarriers, {Bridges}, Policy⟩ → U.Discipline`
*Intent.* Fold the three constituents into a `U.Discipline`, **preserving provenance**, publishing UTS cards, and enabling admissible comparability via referenced **CG‑Spec** rows.
*Obligations.*
1) **Provenance & lanes.** Each imported episteme/standard declares **A.10 anchors** and lane tags **{TA, VA, LA}**; freshness windows are recorded.
2) **Assurance fold.** Use KD‑CAL weakest‑link on R with **Φ(CL)** (and, where applicable, **Φ_plane** for ReferencePlane crossings) **table‑backed and monotone**; publish policy ids. For any independent justification line **P**, compute **`R_eff(P) = max(0, min_i R_i − Φ(CL_min(P)))`**; for parallel independent lines to the *same* claim take **`R(Γ) = max_P R_eff(P)`**; **`F(Γ)=min`** along the used lines. No thresholds inside CHR/CAL (Acceptance‑only). Unknowns propagate as {pass|degrade|abstain} to Acceptance.
3) **CG-Spec guard.** Any numeric comparison or aggregation in Discipline reports **MUST** cite the discipline’s **CG-Spec** with **ScaleComplianceProfile (SCP)**, **Γ-fold**, and **MinimalEvidence**; units, scale, and polarity admissibility via **MM-CHR/CSLC** precedes aggregation.
4) **Scale, unit, and polarity admissibility.** Before any comparison/aggregation, **establish admissibility via MM‑CHR/CSLC** and cite **CG‑Spec characteristic ids** used in the fold (A.17–A.19).
5) **ReferencePlane guard.** When crossings touch the world, concept, or episteme plane, apply **CL_meta** penalties to **R** only; record **plane** on the UTS row.
6) **Edition discipline.** Changes to canons or standards that alter computed ⟨F,G,R⟩ **create a new edition**; the rationale belongs in the edition-continuity record, and UTS records the transition.
7) **No stealth globalisation.** Cross-context mappings are **by Bridge only**; “by-name reuse” is forbidden even with similar labels.

#### C.20:4.4 - Discipline ESG (informative state view)

Export a **Discipline.ESG** with named states and guarded transitions (e.g., *Emerging → Consolidating → Codified → Fragmenting*), where **guards reference C.21 metrics** (CHR‑typed; **Scale/Unit/Polarity + freshness windows**) and cite **CG‑Spec ids**; **all thresholds live only in AcceptanceClauses** (G.4). ESG is **descriptive**; all gating remains in CHR/CAL/LOG packs.

### C.20:5 - Archetypal Grounding *(Tell–Show–Show)*

| Slot | **System** (safety code in a factory) | **Episteme** (discipline canon across editions) |
|---|---|---|
| **Object** | Production line with hazardous operations | “Safety engineering” as *entityOfConcern target* (accident models, tolerable risk) |
| **Concept** | Acceptance clauses & evaluation templates bound to rigs/windows | Canon texts: causality models, design rules, proofs/benchmarks (e.g., **formal knowledge bases**, **proof carriers**, **concept schemas**) |
| **Symbol** | Local SOP/notation sets for checklists | Notation packages (CLIF, RDF/TriG, proof scripts) |
| **Γ_disc assembly** | Fold {line‑specific standard, plant procedures, certifying unit} into **`Discipline: Safety‑Plant‑A`** | Fold {canon papers, formal models, journals/committee} into **`Discipline: Safety‑Engineering`** with **Traditions** (e.g., system safety vs resilience engineering) |
| **Evidence lanes** | LA test campaigns (freshness windows), VA design proofs, TA tool quals | VA proofs over kinds, LA replications/meta‑analyses; TA for checkers |

### C.20:6 - Bias-Annotation
**Lenses:** Governance (naming/UTS), Architecture (CAL+CHR split), Onto/Epist (discipline ≠ domain; triangle fidelity), Pragmatic (authoring/editions), Didactic (twin labels; System/Episteme scenes). **Scope:** context‑local; no “global discipline”.

### C.20:7 - Conformance Checklist (normative)
| ID | Requirement | Purpose |
|---|---|---|
| **CC‑C20‑1 (CG‑Spec linkage).** | A `U.Discipline` **SHALL** declare the **CG‑Spec** ids and **CHR characteristic ids** behind any comparison/aggregation; thresholds live only in **Acceptance** clauses referenced by those CG‑Specs. | Auditable comparability; no inadmissible operations. |
| **CC‑C20‑2 (Bridge-only reuse).** | Any cross-context or cross-tradition use **SHALL** cite **Bridge id + CL + loss notes**; penalties **apply to R only**; **F** and **G** remain invariant. | Prevent silent globalisation; align with KD-CAL. |
| **CC-C20-3 (ReferencePlane).** | For any crossing touching the world, concept, or episteme plane, publish plane and apply **Φ(CL)** and, where applicable, **Φ_plane**. Both penalty policies must be monotone, bounded, and table-backed; unknowns propagate as `{pass|degrade|abstain}` into Acceptance with an SCR note, with no silent `unknown -> 0`. | Keeps cross-plane comparison explicit and prevents hidden reliability collapse. |
| **CC‑C20‑4 (Γ_disc integrity).** | `Γ_disc` **MUST** record lane tags and freshness windows for all imported evidence; **Φ(CL)** **MUST** be monotone and table‑backed per policy. | Deterministic assurance; hygiene of penalties. |
| **CC‑C20‑5 (Edition & DRR).** | Discipline editions **SHALL** be recorded via **UTS edition-continuity records** with DRR links; no silent rewrites or renames. | Traceable evolution. |
| **CC‑C20‑6 (LEX/I‑D‑S).** | `U.Discipline` names **SHALL** follow **LEX** (twin labels; registers; banned heads). **Domain** mentions are catalog‑only. | Register hygiene; avoid “Domain = Discipline”. |
| **CC-C20-7 (Crossing visibility hooks).** | Any **cross-stance, cross-context, or cross-plane** reference in Discipline materials **SHALL** publish a **CrossingBundle** for the crossing (**E.18**; Bridge and UTS through **F.9**, **F.17**, **E.17**, and **E.18**) and expose it via `Expose_CrossingHooks` (**G.10-3**). Published crossings **MUST** be checkable for **LanePurity** (CL to R only; F and G invariant; Φ tables present) and **Lexical SD** (**E.10**) under the active GateProfile and GateChecks (**A.21**). | Prevents implied crossings; makes provenance auditable and replayable. |
| **CC-C20-8 (Discipline column is didactic).** | Any use of a “discipline column” in tables is **didactic only**; semantics are carried by **UTS rows and Bridges**; **Domain** remains a catalog stitch (**E.10/F.17**). | Prevent table headings from becoming hidden ontology. |
| **CC-C20-9 (Lexical firewall).** | Normative sections remain **notation-neutral and tool-neutral**; vendor/tool tokens are avoided (see **E.5.1**). | Keep discipline composition independent from one notation or tool family. |

### C.20:7.1 - Common Anti-Patterns and How to Avoid Them
* “TDD discipline” → **`Tradition: Test‑Driven`** *(Plain twin keeps “Tradition”)*.
* “Safety Discipline Owner” → **`Holder#DisciplineStewardRole:Safety‑Context`**.
* “ClinicalSafetyDomain Governance” → **`DisciplineSpec: Clinical‑Safety`** with comparability in **CG‑Spec**; the **Domain** mention remains a **D.CTX + UTS** catalog stitch.

### C.20:8 - Consequences
**Benefits.** Auditable field composition; admissible federation across traditions; selector-ready maturity/evidence linkage; didactic presentation for stewardship.
**Trade‑offs.** Discipline authoring requires CG‑Spec literacy and Bridge hygiene; paid back by safe reuse and clearer governance.

### C.20:9 - Rationale
The calculus keeps **entityOfConcern local**, **comparability admissible**, and **assurance explicit**. It aligns with KD‑CAL’s weak‑link folds and CL-to-R penalty rule, with CG‑Spec’s **ScaleComplianceProfile (SCP)** and **Γ‑fold** rules, and with LEX twin‑label governance. It avoids “phlogiston disciplines” by tying fields to measurable CHRs (C.21) and evidence lanes.

### C.20:9.1 - SoTA-Echoing
Discipline-composition practice is used here only when it preserves plural traditions, explicit bridges, characteristic health readings, and evidence lanes. C.20 adopts weak-link composition, scale-compliance, and bridge hygiene; it rejects universal field scores, charisma labels, and discipline names that cannot return to measurable CHRs and source evidence.

### C.20:10 - Relations
**Builds on.** KD‑CAL (C.2); CG‑Spec (A.19/G.0); Bridges (F.9); LEX (E.10).
**Coordinates with.** C.21 (field‑health CHRs), C.22 (Problem‑CHR), C.23 (Method‑SoS‑LOG).
**Constrains.** G.2 **MUST** publish **TraditionCards**/**BridgeMatrix** sufficient for `Γ_disc` to assemble **≥2 Traditions** and **≥3 `U.BoundedContext`** per SoTA synthesis to avoid monoculture. G.5 selector **SHALL** cite Discipline **CG‑Spec ids** and **EvidenceGraph** rows when admitting families.

### C.20:End

