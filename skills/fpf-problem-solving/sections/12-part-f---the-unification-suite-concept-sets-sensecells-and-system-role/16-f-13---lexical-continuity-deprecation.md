## F.13 - Lexical Continuity & Deprecation

**“Change names without changing history.”**
**Status.** Architectural pattern.
**Builds on:** F.1 **Question-Relative Source Selection**; F.2 **source-local term harvesting**; F.3 **source-local sense clustering**; F.5 **naming discipline**; F.7 **Concept-Set comparison displays**; F.8 **mint-or-reuse for a name**; F.9 **sense relations and bounded uses**; F.17 **exact cell and row identity**; F.18 **naming settlement and lineage**.
**Coordinates with.** Part C CALs when canon editions change (Sys/KD/Type/Method/LCA).
**Non‑goals.** No registries, workflows, editors, or storage formats. No by‑name Cross‑context equivalence. No silent rewrites of old texts.

### F.13:1 - Intent & applicability

**Intent.** Preserve historical reading when source-local expressions, Concept-Set row labels, or names of governed values and their descriptions change:

* new names **clarify** without erasing what earlier texts meant;
* aliases remain **local to Contexts**;
* a changed meaning is recovered under its defining rule and receives an explicit revision, replacement, split, merge or retirement disposition; a rename cannot supply that decision.

**Applicability.** Use this when changing a source-local expression, an external label or address of a SchemeSenseCell, a Concept-Set row label, or the name of a governed value or description. First say which of these is changing; their identity rules differ.

### F.13:2 - Problem frame

Unification efforts rot when names drift faster than senses or, worse, when senses change under a constant name.

* **Silent relabeling.** A new label is introduced as if nothing changed; readers cannot connect past to present.
* **Alias bloat.** Synonyms accumulate without discipline; reading becomes guesswork.
* **Cross‑context aliasing.** A single alias is made to stand for different Contexts (“global slang”), defeating locality.
* **Retroactive edits.** Old texts are silently rewritten to today’s names, corrupting provenance.

### F.13:3 - Forces

| Force                          | Tension to resolve                                                                           |
| ------------------------------ | -------------------------------------------------------------------------------------------- |
| **Continuity vs truthfulness** | Preserve readers’ continuity yet surface real sense changes (no paint‑over).                 |
| **Locality vs convenience**    | Keep aliases **inside Contexts** even when a catchy global name tempts reuse.                   |
| **Simplicity vs coverage**     | Avoid giant synonym lists while still catching the one or two legacy names people will meet. |
| **Didactics vs formality**     | Make the mapping teachable without inventing new low‑level artefacts or processes.           |

### F.13:4 - Core idea (didactic)

**Keep the named value, its meaning and its expression distinct.**
Recover the old and proposed expression, effective ReferenceScheme, local-sense claim, intended use and any independently governed value being named. When only wording changes, record the rename or alias and retain a path for interpreting the old text.

An F.17 SchemeSenseCell is the exact coordinate `<ReferenceScheme by value, LocalExpression, LocalSenseClaim>`. Changing `LocalExpression` creates another cell even when the `<ReferenceScheme, LocalSenseClaim>` projection stays the same. Retain both coordinates in the naming lineage; do not call them the same cell. An external display label or address can change while its unchanged target cell remains the same.

A Concept-Set row under F.7 displays established comparison content; the row does not constitute a Cross-context relation. A SystemRoleKindDescription under F.4 describes an independently identified exact system-role kind. Recover any continuity of the named value, description episteme, or F.17 UnifiedTermRow under its own rule. Changed identity-bearing claims require the corresponding later object or episteme.

If meaning changes, first apply that subject rule and settle the later naming use under F.18. Split or merge only when there are actually one-to-many or many-to-one senses or rows. A one-to-one revision needs its own subject-governed revision or replacement decision. Preserve the earlier meaning and read-path; when that decision is missing, stop the dependent continuity claim.

> **Keep aliases local.** Compare the exact `<ReferenceScheme, LocalSenseClaim>` projections. A different projection opens F.9 only when a current semantic correspondence is needed. Establish the relation and any bounded-use claim and reliance separately; shared names create none of them.

### F.13:5 - Minimal vocabulary (this pattern only)

* **Legacy label** — an earlier expression retained with its exact local meaning and use, or an earlier external label of an identified value, cell, description or row.
* **Preferred label** — the current label selected for that naming use under F.5 and, when a durable settlement is needed, F.18.
* **Alias** *(local to a naming use)* — a read-path from a legacy expression to the preferred one with the same effective scheme, local-sense claim and use, and the same governed value when one is being named. Writing uses the preferred label.
* **Continuity relation** — one of the descriptive relations below over exact label uses. It records a justified wording or historical-reading decision; it does not establish governed-object, cell, episteme or Bridge identity.
* **Epoch note** — an informative time marker attached to a legacy label when needed to interpret older text.

### F.13:6 - Solution — Continuity, not “registries”

Use the least-committing continuity relation that tells the truth after recovering the subject's identity or change under its own rule.

#### F.13:6.1 - Continuity relations (normative meanings)

1. **`renames(label_old → label_new)`** — wording changes while meaning and use remain unchanged.
   *Use when:* The effective scheme, local-sense claim and intended use remain the same, and the independently governed value remains the same when one is being named. For an external row or description label, recover its target under F.7, F.4 or F.17 as applicable.
   *Effect:* The legacy label becomes a local read-path to the preferred one. If `LocalExpression` changes, retain both exact F.17 cells; if a NameCard or row ClaimGraph changes, retain the earlier episteme and the corresponding later one. The rename itself proves none of those identities.

2. **`aliases(label_legacy ↔ label_pref)`** — a legacy synonym is kept for reading.
   *Use when:* The two exact label uses have the same scheme, local-sense claim, intended use and, where applicable, governed value.
   *Effect:* Keep a two-way read-path; writing uses `label_pref`. Keep at most one legacy alias per register. Distinct expressions need not be the same SchemeSenseCell.

3. **`splits(label_old ⇒ {label_A, label_B})`** — one earlier label covered several senses or rows that are now distinguished.
   *Use when:* F.3 recovers the distinct local senses, or F.7 establishes the required row refactor.
   *Effect:* Deprecate the old label for new writing and retain a disambiguating read-path. Neither new label is asserted to continue the whole earlier meaning.

4. **`merges({label_A, label_B} ⇒ label_new)`** — several labels are consolidated for one recovered naming use.
   *Use when:* The local label uses have the same scheme, local-sense claim and use, with the same governed value where applicable; or two F.7 rows are duplicate displays of the same named comparison or use, exact entries, independently established relations, losses, basis and receiving-use conclusion.
   *Effect:* Keep the old labels' epoch-qualified read-paths subject to the alias budget. This label or display consolidation does not merge source-local cells, named values or Bridge occurrences.

5. **`retires(label_old)`** — a name is withdrawn without one successor.
   *Use when:* The label misleads and no single successor preserves its earlier use.
   *Effect:* Keep a warning for historical reading and point to the relevant meanings or rows. A known single successor for an unchanged meaning belongs to rename, not retirement.

**Meaning-change boundary.** These five label relations do not exhaust changes to the things being named. For a one-to-one changed criterion, recover the revision or replacement under the subject's rule, preserve the exact earlier claim, and settle the later name under F.18. If the governing continuity decision is unavailable, state that missing decision instead of inventing a split or merge. A needed relation between different semantic projections is a separate F.9 question.

### F.13:7 - Invariants (normative)

1. **Locality of alias.** `aliases(-)` and `renames(-)` preserve the exact naming use's effective scheme, local-sense claim and any governed value. Distinct expressions may have distinct F.17 cells; an external row or description label keeps its independently recovered target.
2. **Truth over comfort.** If meaning changes, recover the corresponding revision, replacement, split, merge or retirement under the subject rule before settling the later name. A rename cannot hide that change.
3. **Non‑retroactivity.** Past texts remain phrased as written; continuity only **adds read‑paths**, never rewrites.
4. **Alias parsimony.** per Context and per row, keep **≤ 1** legacy alias per register (Tech/Plain); prefer the one readers will most likely encounter.
5. **Prefer present for writing.** In normative writing, use the **current preferred label** (F.5). Aliases are for **reading comprehension**.
6. **Bridge discipline.** A different `<ReferenceScheme, LocalSenseClaim>` projection is not an alias or pure rename. Use F.9 only for a needed semantic correspondence; recover any obtaining Bridge, bounded-use claim and reliance separately.
7. **Epoch honesty.** When declaring continuity, attach a **succinct epoch note** (“pre‑2023 usage”) if it aids readers.

### F.13:8 - Self‑checks (mental, not procedural)

* **Same-sense test.** Do the effective scheme, local-sense claim, intended use and any governed value stay the same? Then a rename or alias may be justified, with distinct cells when expressions differ. If meaning or the target changes, first recover that change under its subject rule.
* **Context test.** Are the semantic projections different, and is a current correspondence needed? If both hold, open F.9. Different context names alone establish no relation.
* **Reader test.** Which legacy string will a reader actually meet in each register? Keep at most one useful alias per Tech or Plain register, as required by §7.
* **History test.** Does your “continuity” require editing old claims? If yes, you’re attempting a **retroactive rewrite**—stop.
* **Didactic test.** Can the intended reader recover what changed and how to interpret the old label? If not, clarify that account or name the unresolved subject decision; sentence length alone diagnoses neither sameness nor change.

### F.13:9 - Micro‑examples (illustrative)

#### F.13:9.1 - Pure rename inside a local service vocabulary

*Constructed case:* Under the fixed `ServiceVocabulary-1` reference scheme, the local-sense claim is “a service indicator threshold together with its assessment window”. The old expression is **“SLO”**, the proposed expression is **“service-level objective”**, and both serve the same use of reading a service objective. No change to the objective or assessment rule is proposed.
**Relation:** `renames("SLO" → "service-level objective")`.
**Why:** The scheme, sense and use are unchanged; expansion improves recognition.
**Effect:** Retain the two exact cells `<ServiceVocabulary-1, "SLO", claim>` and `<ServiceVocabulary-1, "service-level objective", claim>` in the naming lineage. Old text retains its earlier expression and meaning; new writing uses the expansion. No Bridge is needed for these identical semantic projections.

#### F.13:9.2 - Alias for a common legacy synonym (Sys‑CAL)

*Illustrative premise:* A local state-space control vocabulary has independently established the same scheme, sense and use for **“control output”** and **“actuation”**. This premise requires source-local recovery in a real application; the words alone are insufficient.
**Relation:** `aliases("control output" ↔ "actuation")`.
**Effect:** Keep the distinct expression-bearing cells and one historical read-path. New text uses the locally selected preferred expression **“actuation”**.

#### F.13:9.3 - Split of a muddled local sense (Enactment)

*Context:* **BPMN 2.0**.
Legacy label **“process”** was used to mean both **“collaboration”** and **“executable process”** in a team’s prose.
**Relation:** `splits("process" ⇒ {"collaboration","executable‑process"})`.
**Effect:** The single Concept‑Set row becomes two; old label is deprecated with a disambiguation note.

#### F.13:9.4 - Merge duplicate comparison rows

Suppose the two Concept-Set rows labelled **“DBaaS”** and **“Database-Service”** display the same named comparison or use, exact entries, independently established relations, losses, basis and receiving-use conclusion. They are duplicate displays; combining them asserts no new sameness among their entries.
**Relation:** `merges({"DBaaS","Database‑Service"} ⇒ "Database‑Service")`.
**Effect:** “DBaaS” becomes a legacy alias with an epoch note.

#### F.13:9.5 - Not a rename: Cross‑context temptation (forbidden)

*Contexts:* **BPMN (design graph)** vs **PROV‑O (run activity)**.
Temptation: “Let’s rename *process* to *activity*.”
**Diagnosis:** Cross‑context; **different SenseCells**.
**Action:** Keep the labels and their exact meanings. If a semantic correspondence is needed, establish its F.9 relation and a separate bounded-use claim with current reliance. A design-to-run or production relation belongs under its direct subject rule.

### F.13:10 - Anti‑patterns & remedies

| #       | Anti‑pattern               | Symptom in texts                                                      | Why it harms thinking                                          | Remedy (conceptual move)                                                                                                         |
| ------- | -------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **A1**  | **Cross‑context rename**      | “Let’s rename *process (BPMN)* to *activity (PROV)*.”                 | Erases Context boundaries; hides loss; violates locality.         | **Do not rename across Contexts.** Keep both labels; if you must relate them, declare a **Bridge** (F.9) with CL/loss.              |
| **A2**  | **Retroactive rewrite**    | Old passages silently updated to new names.                           | Breaks provenance; misleads readers about what was meant then. | **Non‑retroactivity.** Past texts stand; add **read‑paths** via `renames/aliases`; attach **epoch notes** when helpful.          |
| **A3**  | **Alias flood**            | Long lists of synonyms for comfort.                                   | Raises ambiguity; dilutes teaching signals.                    | **Alias parsimony.** Keep ≤ 1 legacy alias per register (Tech/Plain) **inside the same Context or row**.                            |
| **A4**  | **Paint‑over rename**      | Rename used where sense actually changed.                             | Confuses continuity with revision; hides splits.               | Recover the changed meaning under its subject rule, preserve the earlier claim, then settle the later name. Split or merge only when those relations actually hold.                |
| **A5**  | **Global alias**           | One catchy word reused as alias in several Contexts.                     | Creates a pseudo‑global dictionary; invites category errors.   | **Local aliases only.** If a word appears in many Contexts, treat it as **homonymous**; keep Context‑prefixed speech.                  |
| **A6**  | **Euphemism treadmill**    | Frequent cosmetic renames (“modernising” labels) with no gain.        | Cognitive noise; readers lose confidence in names.             | Apply the **Same‑sense test**. If gain is marginal, **do nothing**; if clarity improves materially, one **`renames`** is enough. |
| **A7**  | **Grandfather everything** | Never deprecate confusing legacy labels.                              | Drags ambiguity forward; blocks sharper distinctions.          | When a label truly misleads and has no single successor, **`retires`** with a short **pointer note** to Contexts/rows.              |
| **A8**  | **Row drift via rename**   | Concept‑Set row is relabeled while its membership silently changes.   | Hides that the set changed; breaks Cross‑context alignment.       | Recover the changed F.7 comparison content and its earlier/later displays. Rename only when the displayed comparison and receiving use are unchanged; split or merge only when warranted.                             |
| **A9**  | **Bridge‑by‑alias**        | Using an alias to hint two Contexts are “the same.”                      | Smuggles translation without CL/loss.                          | **No Cross‑context aliasing.** If similarity matters, **Bridge** explicitly (F.9) and keep labels separate.                         |
| **A10** | **Acronym absolutism**     | Treating acronyms as preferred labels everywhere (“SLO” in any Context). | Obscures Context‑specific senses; hurts didactics.                | Prefer **expanded** labels as preferred (F.5); keep acronym as context‑local **alias** only where historically dominant.            |
| **A11** | **Temporal fudge**         | Rename used to imply design↔run shift (“execution ≈ process”).        | Conflates time stances; erases important dualities.            | Keep **DesignRunTag** explicit on labels or glosses; if mapping is needed, do so in **F.9**.                                       |
| **A12** | **Over‑canonicalisation**  | Forcing a single “perfect” label across all rows/Contexts.               | Centralises language; breaks heterogeneity guard.              | Let each Context/row keep its **own preferred label**; put unification pressure only into **rows** and **Bridges**.                 |

### F.13:11 - Extended examples

#### F.13:11.1 - KD‑CAL × Services — *metric target* labels over time

* **Contexts:** *ITIL 4 (services, design)*; *SOSA/SSN (sensing, run)*.
* **Before:** An illustrative local service-objective description used **“SLO”** (plain “target”), and older texts also used **“service target”** for the same locally recovered meaning.
* **Move:** `renames("SLO" → "service‑level objective")` (Context: ITIL). Keep `aliases("service target" ↔ "service‑level objective")`.
* **Why:** The example assumes the same scheme, local-sense claim and use. Retain each expression's exact cell and the later naming settlement; SOSA/SSN labels are unchanged.
* **Pay‑off:** Runtime **Observations** (SOSA) are later compared to **service‑level objective** clauses (ITIL) without Cross‑context aliasing.

#### F.13:11.2 - Sys‑CAL × LCA‑CAL — separating *execution* vs *actuation*

* **Contexts:** *IEC 61131‑3 (run)*; *state‑space control texts (design)*.
* **Temptation:** Rename **“task execution”** to **“actuation”** “to sound control‑ish”.
* **Diagnosis:** Different Contexts; different SenseCells (program run vs control output).
* **Move:** **No rename.** Keep the labels. Establish any actual Work-to-signal production or output relation under its direct pattern, following F.11. Add F.9 only when a separate semantic correspondence between exact local senses is needed; then keep the bounded-use claim and reliance separate.
* **Pay‑off:** Plant narratives stop calling programs “actuators”; runtime vs control semantics stay crisp.

#### F.13:11.3 - Kind-CAL × method/work stack — false merge avoided

* **Contexts:** *OWL 2 (types, design)*; *SPEM 2.0 (methods, design)*.
* **Issue:** A row labeled **“Class”** tried to absorb **“WorkProductKind”** by a `renames`.
* **Diagnosis:** Not same sense; different calculi (type vs artefact category).
* **Move:** **Split the row**: `splits("class" ⇒ {"type‑class","work‑product‑category"})`.
* **Pay-off:** Later descriptions can cite the exact local meaning they use. Any SystemRoleKindDescription still describes its independently recovered system-role kind under F.4; a source-cell pointer does not establish that kind.

#### F.13:11.4 - Enactment × KD‑CAL — replacing a misleading metaphor

* **Context:** *BPMN 2.0 (design)*.
* **Legacy:** Team jargon **“heartbeat”** used for a **timer event**. Newcomers confuse it with **sensor heartbeats** (KD‑CAL).
* **Move:** `renames("heartbeat" → "timer event")` for the team’s unchanged BPMN timer-event meaning. Keep a local historical read-path; the sensor-liveness use remains a different local meaning.
* **Pay‑off:** Two different ecosystems stop colliding on the same catchy word.

#### F.13:11.5 - Concept‑Set row refactor after duplicate comparison is established

* **Rows:** `{“DBaaS”, “Database‑Service”}` representing service notions across several Contexts.
* **Comparison basis:** Both rows display the same named comparison or use, exact source-local entries, independently established relations, losses, basis and receiving-use conclusion. Only the duplicate display is combined; no source meanings or Bridge occurrences are merged.
* **Move:** `merges({"DBaaS","Database‑Service"} ⇒ "Database‑Service")` at **row level**. Both legacy labels become row‑local aliases with epoch notes.
* **Pay‑off:** One clearer row label; old articles still understandable.

### F.13:12 - Reasoning primitives (judgement schemas, notation‑free)

> Each judgement is a **pure thought**: premises ⇒ safe conclusion. No storage, no workflow, no roles.

Let `meaningOf(ℓ)` recover the exact `<ReferenceScheme, LocalSenseClaim>` projection for one local label use; let `useOf(ℓ)` recover its intended naming use. Where a value is being named, recover it independently under its subject rule. `pref(t)` denotes the preferred expression for that exact naming use, not a global preferred word.

#### F.13:12.1 - Same‑sense & same‑place

Two expressions with the same `meaningOf`, intended use and independently governed value where applicable may receive a rename. A changed `LocalExpression` still changes the exact F.17 cell. An external label change preserves a cell only when the target coordinate itself is unchanged.

#### F.13:12.2 -Local alias

Under the same conditions, a legacy expression may remain a read-path to `pref(t)`. Retain its own exact coordinate and any source basis; aliasing is not cell identity.

#### F.13:12.3 - Split detection

If one label covered several independently recovered local senses or rows, record the split and prefer the precise later labels. Keep the earlier use resolvable through a disambiguation note.

#### F.13:12.4 - Merge admission

Consolidate local labels only after recovering their common semantic projection and use, with the same governed value where applicable. Consolidate comparison-row labels only after establishing duplicate F.7 comparison content. Neither move merges distinct cell coordinates or subject entities.

#### F.13:12.5 - Retirement

Retire a misleading label when no single successor preserves its earlier use. Point historical readers to the relevant meanings or rows.

#### F.13:12.6 - Cross‑context guard

Different `meaningOf` projections do not support a pure rename or alias. A needed semantic correspondence goes to F.9; relation obtaining, a bounded-use claim and reliance are separate questions.

#### F.13:12.7 - Writing discipline

Use the current preferred expression for the exact naming use. Keep aliases for historical reading.

#### F.13:12.8 - Reading resolution

Resolve a legacy label to its earlier meaning and use first, then to any justified present-name read-path. Include an epoch when it changes interpretation. A successor's changed meaning must not replace the old one retroactively.

#### F.13:12.9 - Alias budget

Keep at most one useful legacy alias per register for one naming use.

#### F.13:12.10 - Row‑level continuity

A Concept-Set display label may change while the exact comparison content and receiving use remain unchanged. Recover changed row content under F.7 first. When an F.17 UnifiedTermRow's identity-bearing claims change, retain the earlier and corresponding later epistemes under C.2.1/F.17; a stable row designator is not identity proof.

### F.13:13 - Relations

**Builds on:**
F.1 selects the question-relative sources; F.2 and F.3 recover source-local expressions and meanings. F.5, F.8 and F.18 govern naming choices. F.7 governs comparison displays; F.9 governs exact sense relations and bounded uses. F.17 fixes SchemeSenseCell and UnifiedTermRow identity. F.4 and the direct subject patterns govern any described or named values; F.15 checks the resulting continuity claims.

**Constrains:**

* **F.5 (Naming):** may select preferred labels **only** after applying these continuity relations.
* **F.7 (Rows):** relabel unchanged comparison content directly; recover changed entries, relations or receiving use before deciding revision, split or merge.
* **F.9 (Bridges):** Cross‑context changes must **not** be expressed as renames/aliases.

**Used by.**
All Part C patterns when editions shift; all examples and tutorials when teaching with legacy terminology.

### F.13:14 - Migration notes (conceptual playbook)

1. **Recover the same meaning and use first.** Distinguish the expression from its exact cell and governed value. Use `renames` only for unchanged meaning and use; recover any subject change before settling the later name.
2. **Keep aliases local.** Different semantic projections open F.9 only for a needed correspondence; the difference itself establishes no Bridge.
3. **Prefer clarity over fashion.** Rename only when the new label **removes a real ambiguity** (F.5 criteria), not to chase style.
4. **Limit nostalgia.** Admit **one** legacy alias in each register that readers will most likely meet; leave the rest to footnotes in examples.
5. **Keep historical reading clear.** For a rename, point from the legacy label to its preferred successor. For retirement without a single successor, point to the relevant meanings or rows.
6. **Rows before names.** If a rename request coincides with a shift in what the row covers, **refactor rows** (F.7) first, then choose labels.
7. **Edition changes.** Compare the affected definitions. If meaning changes, recover the subject-governed revision, replacement, split, merge or retirement and preserve the earlier claim. If meaning and use stay unchanged, rename only for a concrete recognition gain.
8. **Teach the delta.** In primers, show a **mini table** with legacy → preferred pairs only where readers will encounter both.

### F.13:15 - Acceptance tests (SCR/RSCR — concept‑level)

#### F.13:15.1 - Static conformance (SCR)

* **SCR-F13-S01 (local continuity).** Every `renames/aliases` preserves the exact semantic projection, intended use and any independently governed value. An external row or description label resolves its target under the applicable rule.
* **SCR-F13-S02 (Truthfulness).** Each rename retains its exact old and new expressions. A changed LocalExpression has a distinct F.17 cell even when meaning is unchanged. Any claim of governed-value or episteme continuity satisfies that subject's rule.
* **SCR‑F13‑S03 (Alias budget).** For any one thing and register, the number of deprecated aliases is **≤ 1**.
* **SCR‑F13‑S04 (Non‑retroactivity).** No requirement or suggestion to rewrite past texts is present; continuity is expressed as **read‑paths**.
* **SCR-F13-S05 (Row integrity).** A display-label rename preserves the exact comparison content and receiving use. Changed row content receives its warranted revision, split or merge under F.7; changed F.17 identity-bearing claims receive the corresponding later row episteme.
* **SCR‑F13‑S06 (Bridge discipline).** No alias/rename is used to imply Cross‑context sameness; any such relation belongs under **F.9**.

#### F.13:15.2 - Regression (RSCR)

* **RSCR-F13-E01 (Edition drift audit).** Compare affected earlier/later definitions and naming uses. Stable meaning can support a rename with distinct expression-bearing cells; changed meaning requires the subject-governed revision, replacement, split, merge or retirement before fresh naming settlement.
* **RSCR‑F13‑E02 (Alias creep check).** Periodically ensure alias budgets remain within **≤ 1 per register**; surplus aliases are pruned.
* **RSCR-F13-E03 (Bridge leak check).** A claimed correspondence between different semantic projections is tested under F.9 only when a current use needs it. Retain exact meanings and an honest unresolved result when obtaining is unestablished; do not create a Bridge by rewriting a note.
* **RSCR‑F13‑E04 (Didactic continuity).** Sampling of examples shows that readers can **resolve** legacy labels to current ones without confusion (via the continuity notes).

### F.13:16 - Didactic distillation (60‑second script)

> **Preserve what the old words meant.** For unchanged meaning and use, record a local rename or alias. A changed expression has a distinct F.17 cell; keep its naming lineage. If meaning or the named value changes, recover that change under its subject rule before settling the later name. Split or merge only when those relations hold. Keep at most one useful legacy alias per register, preserve the earlier text, and give readers the exact historical meaning and any justified path to the present name.

### F.13:End
