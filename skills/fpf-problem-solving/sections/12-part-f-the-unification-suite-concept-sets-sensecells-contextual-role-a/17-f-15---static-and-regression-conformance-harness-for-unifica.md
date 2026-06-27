## F.15 - Static and Regression Conformance Harness for Unification
> **Type:** Pattern
> **Status:** Stable

**"Prove locality and parsimony first; only then prove composition."**

**Type:** Architectural pattern.
**Status:** Stable.
**Normativity:** Normative.
**Builds on:** E.10.D1 for `U.BoundedContext` discipline; F.1 for context selection; F.2 and F.3 for term harvesting, Local-Sense, and SenseCell formation; F.4 for RoleDescription as description episteme for one local `U.Role`; F.5 for local naming discipline; F.7 and F.8 for Concept-Set rows and mint-or-reuse decisions; F.9 for Bridge Cards and `CL`; F.10 for status families, values, and windows; F.13 for aliases; F.14 for anti-explosion control; F.18 for durable naming.

**Coordinates with:** A.2, A.2.1, A.2.5, A.2.7, F.6, and A.15.1 for work-facing role, assignment, role state, role relation structure, and performed-work claims; A.10, B.3, E.17, and E.10.D2 for evidence, assurance, publication, source, and description-use claims; A.6.5 for relation-slot discipline.

**Plain entry cues (informative).** SCR and RSCR harness; unification slice check; context-bridge regression check.

### F.15:1 - Intent and applicability

**Intent.** Give one compact harness for checking whether a unification slice is locally sound now and remains sound across changes. F.15 does not define contexts, senses, rows, roles, status families, bridges, aliases, or names. It checks that the current slice uses those values under their direct patterns without collapsing them into one convenient table or one global meaning.

**Applicability.** Use F.15 when a project declares or revises a slice that contains several of these moving parts: `U.BoundedContext` cards, Local-Senses, SenseCells, Concept-Set rows, RoleDescriptions, Bridge Cards, status families or windows, aliases, or durable names.

**Primary EntityOfConcern in plain terms.** One unification slice under static and regression conformance check. The EoC is not a registry, not a work process, not a role assignment, not a status value, and not a publication.

**Admissible move in plain terms.** Check the slice against static conformance rules for the current snapshot and regression conformance rules for the changed snapshot, then treat any failed claim under the direct governing pattern.

**Primary working reader.** A terminology steward, method author, architect, manager, or checker who needs to decide whether a proposed unification row, bridge, role-description label, status window, or rename is safe enough to reuse.

**Use this when.** Use F.15 when a slice feels "almost unified" but one of these questions is still open:

1. Do all local senses still stay inside their own bounded contexts?
2. Does each RoleDescription still describe one local `U.Role` through one SenseCell?
3. Does a row really relate at least two contexts, or is it a row-shaped local note?
4. Does a Bridge Card state kind, direction, `CL`, loss, and admitted use?
5. Did an edition change, row change, rename, bridge change, or status-window change preserve the earlier commitments?

**What goes wrong if missed.** Local meanings become global by shared labels, rows multiply without real distinctions, role descriptions quietly become status or evidence templates, bridges become equivalence by habit, and changed editions rewrite earlier claims without a visible continuity decision.

**What this buys.** A small safety harness for Part F: context-local meaning remains local, cross-context use stays bridge-bound, role and status claims leave through direct patterns, and changes can be checked without turning the harness into a new governance format.

**Not this pattern when.** Not F.15 when the only question is one word, one role value, one role assignment, one status family, one bridge, one public term, one source relation, or one publication-use claim. Use the direct pattern first. Return to F.15 only when the slice combines several moving parts and their joint conformance is live.

**Recognition versus assurance note.** The recognition block is the unification slice and the current or changed moving parts. The assurance block is the static and regression rule set, the record, witnesses, and worked cases. Assurance text must not turn F.15 into a registry format, publication authority, role ontology, or status ontology.

### F.15:2 - Problem frame

Unification work fails when composition is claimed before locality and continuity have been checked:

1. **Locality leak.** A same-spelled label is treated as one meaning across contexts.
2. **Row sprawl.** Concept-Set rows grow laterally with near-duplicates.
3. **Role or status inflation.** Adjectival, temporal, or source-looking variants become new role or status types.
4. **Silent rewrite.** An edition or rename changes meaning while keeping the old row or name.
5. **Bridge hardening.** A weak Bridge is later used as equivalence without a new witness set.
6. **Register split.** Unified Tech and Plain labels drift apart and no longer refer to the same local sense.

F.15 catches these failures before the slice is used for cross-context reuse, naming, assurance, or downstream claims.

### F.15:2.1 - Problem

A unification slice can look stable because labels, rows, bridges, aliases, role descriptions, status windows, or public names are already arranged in one table. The problem is that reuse may still outrun locality, bridge strength, edition continuity, direct governing patterns, or witness evidence; F.15 makes the static and regression checks explicit before the slice is used downstream.

### F.15:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| Parsimony versus coverage | Keep vocabularies and rows small while preserving real distinctions. |
| Locality versus reuse | Local meanings should remain local, yet projects need cross-context comparison and reusable names. |
| Stability versus change | Editions, names, rows, and bridges evolve, but earlier commitments should remain recoverable. |
| Clarity versus apparatus | The check must be teachable in minutes and still precise enough to catch kind drift. |
| Composition versus direct patterns | F.15 checks a combined slice; it must not replace F.4, F.9, F.10, F.17, F.18, A.2.1, F.6, or A.15.1. |

### F.15:4 - Solution

The harness has two families of rules.

1. **Static Conformance Rules (SCR).** Check the current snapshot. Contexts, Local-Senses, SenseCells, rows, RoleDescriptions, bridges, windows, aliases, and names must satisfy their direct local rules now.
2. **Regression and Stability Conformance Rules (RSCR).** Check a changed snapshot against the earlier snapshot. The rule asks what stayed the same, what changed, what must be forked, what must be retired, and which bridge or name needs a fresh witness.

Both families are judgement schemas over content claims. They do not prescribe storage, implementation, team responsibility, or publication format.

### F.15:5 - Minimal vocabulary

* **Unification slice** - the small set of contexts, senses, rows, RoleDescriptions, bridges, windows, aliases, and names being checked together.
* **Static Conformance Rule (SCR)** - a check that must hold in the current snapshot.
* **Regression and Stability Conformance Rule (RSCR)** - a check that compares an earlier and later snapshot.
* **Check claim** - one content assertion such as "this row spans two contexts" or "this RoleDescription refers to one SenseCell".
* **Witness** - one small example, counterexample, invariant, or edition note that makes the check inspectable.
* **Moving part** - any context, local sense, row, role-description label, bridge, status window, alias, or public name whose change could affect the slice.
* **Failed conformance** - a check result that makes the claim governed by the direct pattern before reuse.

### F.15:6 - Objects under check

F.15 may check these values together, but does not redefine them:

1. `U.BoundedContext` cards from F.1.
2. Local-Senses from F.2 and F.3.
3. SenseCells, meaning `(Context, Local-Sense)`.
4. Concept-Set rows from F.7.
5. RoleDescriptions from F.4, each describing one local `U.Role` through one SenseCell.
6. Bridge Cards from F.9.
7. Status families, values, confidence, and windows from F.10 or the direct status pattern.
8. Aliases from F.13.
9. Candidate names and durable names from F.5, F.8, F.14, F.17, and F.18.

If the slice contains role assignments, performed work, evidence use, source use, publication use, assurance, gate, decision, method, capability, or policy claims, F.15 records that those claims leave the harness for direct governing patterns. It does not absorb them.

### F.15:7 - Unification conformance record

Use this record when several moving parts are being checked together.

```text
UnificationConformanceRecord:
  SliceRef:
  BoundedContextRefs:
  ContextEditionRefs:
  SenseCellRefs:
  ConceptSetRowRefs:
  RoleDescriptionRefs:
  BridgeCardRefs:
  StatusFamilyOrWindowRefs:
  AliasRefs:
  CandidateNameOrRowDecisions:
  StaticRuleResults:
  RegressionRuleResults:
  Witnesses:
  NonAdmittedUses:
  DirectGoverningPatternRefs:
  ReopenTrigger:
```

`StaticRuleResults` and `RegressionRuleResults` name only the checks that matter for the current slice. `NonAdmittedUses` names the tempting claim that the slice does not permit, such as direct role assignment, performed-work attribution, evidence use, source authority, publication authority, status transfer, or bridge-based equivalence.

### F.15:8 - Static conformance rules for local material

All local rules stay inside one `U.BoundedContext`.

**SCR-F15-S1 (Context in view).**
`Seed sigma has context C -> C is among the slice contexts.`
Every harvested seed lives in a bounded context that is deliberately in view for this slice.

**SCR-F15-S2 (Attestation currentness).**
`Occurrence omega attests seed sigma -> omega states edition and locus.`
A Local-Sense can be reconstructed from attestations rather than from memory or a fashionable label.

**SCR-F15-S3 (In-context clustering).**
`Local-Sense lambda clusters seeds sigma_i -> every sigma_i belongs to context(lambda).`
No cross-context items are hidden inside one Local-Sense.

**SCR-F15-S4 (Two registers).**
`Local-Sense lambda -> Unified Tech label and Plain label both refer to lambda.`
The two labels differ in register, not in kind or sense.

**SCR-F15-S5 (Minimal gloss).**
`gloss(lambda) -> states only the needed local meaning.`
The gloss does not smuggle behavior, permission, evidence, source authority, publication status, or global sameness.

**SCR-F15-S6 (Context-local normal form).**
`normalize_C(sourceExpression) = n -> n is used only inside C unless F.9 or F.17 admits wider use.`
Normalization inside one context does not create a global name.

### F.15:9 - Static conformance rules for cross-context material

Cross-context rules connect local material without collapsing locality.

**SCR-F15-S7 (Single-cell RoleDescription).**
`RoleDescription tau -> refersTo(tau, one SenseCell) and describes(tau, one local U.Role).`
A RoleDescription is not a status template, evidence template, source template, publication template, or role assignment.

**SCR-F15-S8 (Name discipline).**
`RoleDescription tau or NameCard n -> name obeys F.5, F.8, F.14, and F.18 as applicable.`
Naming follows kind recovery before durable naming.

**SCR-F15-S9 (Row spans contexts).**
`Row rho lists cells cell_i -> at least two distinct contexts occur.`
A row of one context is not cross-context unification.

**SCR-F15-S10 (Row purity).**
`Row rho -> each listed item is one SenseCell.`
No cell is a pre-merged bundle, hidden bridge, or global meaning.

**SCR-F15-S11 (Reuse before minting).**
`Proposed row rho2 overlaps intended use of row rho -> reuse rho or record the F.8 mint decision.`
New rows need a visible difference, not merely a new label.

**SCR-F15-S12 (Bridge explicitness).**
`C1 != C2 and relation asserted between cells -> BridgeCard states cells, kind, direction, CL, loss, witness, and admitted use.`
A cross-context relation appears as a Bridge Card before it is consumed by rows, names, assurance, or downstream claims.

**SCR-F15-S13 (Bridge locality).**
`BridgeCard beta -> beta relates cells from different contexts.`
Within one context, use clustering or local relation discipline rather than a bridge.

**SCR-F15-S14 (Status window honesty).**
`Status family Sigma varies by time, scale, phase, confidence, or use -> F.10 names value or window; no new status family by adjective alone.`
Temporal and scale variation does not create status ontology by suffix.

**SCR-F15-S15 (Role-relation preservation).**
`role bundle or incompatibility expression is live -> A.2.7 states it; no fused RoleDescription is minted by convenience.`
Role-relation expressions are not role assignments and do not prove performed work.

**SCR-F15-S16 (Direct-pattern boundary for non-unification claims).**
`Slice contains assignment, work, evidence, source, publication, assurance, gate, decision, method, capability, or policy claim -> cite the direct governing pattern.`
F.15 checks whether the slice is safe to compose; it does not decide those claims.

**SCR-F15-S17 (Public or cross-context naming admission).**
`Name is public, cross-context, or term-sheet-facing -> F.17 and F.18 admit it after kind recovery.`
Public reuse is not created by repeated local labels.

### F.15:10 - Twin-register checks

Use these checks when a Unified Tech label and Plain label are both present.

**SCR-F15-T1 (Same local sense).**
`TechLabel t and PlainLabel p -> both resolve to the same SenseCell or NameCard target.`

**SCR-F15-T2 (Same kind).**
`TechLabel t names kind K -> PlainLabel p does not suggest another kind.`

**SCR-F15-T3 (Ambiguous head guarded).**
`PlainLabel p has a high-risk head -> first use includes a kind head or short gloss.`

**SCR-F15-T4 (No normative displacement).**
`PlainLabel p is reader-facing -> it does not replace the Unified Tech label in normative Core claims.`

**SCR-F15-T5 (Bridge before copying).**
`PlainLabel p is reused in another context -> F.9 Bridge Card or F.17 public term-sheet row exists first.`

### F.15:11 - Regression and stability rules

The RSCR family compares an earlier snapshot `@t0` and a later snapshot `@t1`.

#### F.15:11.1 - Contexts and editions

**RSCR-F15-E1 (No silent replacement).**
`Context C@t0 edition e0, Context C@t1 edition e1, e1 != e0 -> new context or explicit recency decision.`
A new edition becomes a new context when sense changes; otherwise the recency decision is visible.

**RSCR-F15-E2 (Known confusion check).**
`C@t1 derives from C@t0 -> known confusion cases from C@t0 are rechecked or explicitly retired.`
Old traps do not disappear merely because an edition changed.

#### F.15:11.2 - Local-Senses and SenseCells

**RSCR-F15-E3 (Reconstructible Local-Sense).**
`Local-Sense lambda@t0 changes attestations -> lambda@t1 remains reconstructible from attestations@t1.`

**RSCR-F15-E4 (SenseCell context stability).**
`SenseCell (C, lambda)@t0 -> (C2, lambda2)@t1 -> same cell only if C2 = C and lambda2 preserves local sense.`
A SenseCell does not migrate across contexts through edits.

#### F.15:11.3 - Concept-Set rows

**RSCR-F15-E5 (Row identity).**
`Row rho@t0 with cells cell_i -> row rho@t1 is same row only if each cell preserves its local sense.`
If a cell changes sense, mint a new row and retire the old row.

**RSCR-F15-E6 (Add or retire before silent mutation).**
`Row rho loses or gains a cell because an edition split occurred -> preserve old row and add or retire rows explicitly.`

#### F.15:11.4 - RoleDescriptions

**RSCR-F15-E7 (Single-cell continuity).**
`RoleDescription tau@t0 -> tau@t1 -> refersTo(tau@t1, one SenseCell) and same cell or justified switch.`

**RSCR-F15-E8 (Alias for rename, new RoleDescription for meaning change).**
`name(tau@t0) -> name(tau@t1) -> alias if only label changed; new RoleDescription if described role or local sense changed.`

#### F.15:11.5 - Bridges

**RSCR-F15-E9 (Recheck Bridge on endpoint movement).**
`Bridge beta@t0 and either endpoint cell changes -> beta is rechecked; CL, loss, admitted use, and witness may change.`

**RSCR-F15-E10 (No drift to equivalence).**
`Bridge beta kind is not equivalence at t0 and equivalence is claimed at t1 -> new witness set is required.`
Equivalence is rare and cannot arrive by gradual wording drift.

#### F.15:11.6 - Status windows and role relation structure

**RSCR-F15-E11 (Window stability).**
`Status family windows@t0 -> windows@t1 -> changed only when variance of meaning or use is shown.`

**RSCR-F15-E12 (Role-relation stability).**
`role incompatibility, bundle, qualification, or role-requirement substitution@t0 -> @t1 -> preserved, retired, or restated before assignment or naming use.`
No later RoleDescription fuses roles that were kept distinct by A.2.7.

#### F.15:11.7 - Public naming

**RSCR-F15-E13 (Public name continuity).**
`Public or term-sheet-facing name changes -> F.17 or F.18 records lineage, alias, split, merge, or retirement.`
Local rename is not enough when the name already faces other contexts.

### F.15:12 - Reasoning primitives

```text
staticSliceOK(slice)
  only if all triggered SCR rows hold for the current moving parts.
```

Interpretation: F.15 checks only triggered rows. It does not require every possible object slot to be present.

```text
changedSliceOK(slice@t0, slice@t1)
  only if every changed moving part has an RSCR result.
```

Interpretation: a change that matters to context, sense, row, RoleDescription, Bridge, status window, alias, or name must be stated.

```text
failedRule(rule, claim)
  -> direct governing pattern must govern the claim before reuse.
```

Interpretation: a failed Bridge rule is governed by F.9; a failed RoleDescription rule is governed by F.4; a failed status-window rule is governed by F.10; a failed naming rule is governed by F.8, F.17, or F.18.

```text
bridgeAdmitsUse(beta, use)
  -> downstream claim may use beta only at that admitted use.
```

Interpretation: a Bridge may admit naming, explanation, or type-structure use. It does not admit role assignment, work attribution, or evidence use by itself.

### F.15:13 - Archetypal Grounding - worked cases

#### F.15:13.1 - Activity and task in two run contexts

Contexts: `PROV-O run context` and `IEC 61131-3 run context`.

Local senses: `activity` in the first context and `task` in the second.

F.15 result:

* SCR-F15-S9 passes only if a Concept-Set row lists both SenseCells.
* SCR-F15-S12 requires a Bridge Card. The admitted use may be comparison or explanation, not direct substitution.
* A RoleDescription named `ExecutionRole` may use one local SenseCell only. It does not describe both senses at once.
* If a later edition makes the `task` sense cyclic while the `activity` sense remains non-periodic, RSCR-F15-E9 rechecks the Bridge and may lower `CL`.

#### F.15:13.2 - Service availability row across service and observation contexts

Contexts: `ITIL service-management context` and `SOSA observation context`.

Row: `ServiceAvailability` with one SLO SenseCell and one uptime-observation SenseCell.

F.15 result:

* SCR-F15-S9 passes because two contexts are present.
* SCR-F15-S12 requires Bridge kind, direction, `CL`, loss, and admitted use.
* SCR-F15-S16 treats evidence and assurance claims under A.10 and B.3; the row itself does not make the observation adequate evidence.
* SCR-F15-S14 treats time-window and confidence variation under F.10.

#### F.15:13.3 - Rename a RoleDescription without changing meaning

Slice: `IncidentReviewerRoleDescription` is renamed to `ServiceIncidentReviewerRoleDescription`, while the described local `U.Role` and SenseCell stay the same.

F.15 result:

* RSCR-F15-E7 checks single-cell continuity.
* RSCR-F15-E8 admits an alias because only the label changed.
* F.18 updates durable naming if the name is reusable outside the local context.
* If the described role changed, F.15 rejects alias-only treatment; F.4, F.8, and F.18 govern the repaired claim.

#### F.15:13.4 - Weak bridge later claimed as equivalence

Slice: a Bridge between an OWL subclass sense and an FCA order-edge sense was partial overlap at `CL = 2`. A later formal result claims equivalence inside one constrained fragment.

F.15 result:

* RSCR-F15-E10 requires a new witness set for equivalence.
* SCR-F15-S12 updates kind, direction, loss, and admitted use.
* C.29 may govern the mathematical-lens claim; F.15 only checks that the changed Bridge is not silently strengthened.

#### F.15:13.5 - Peak-hours status proposal

Slice: a team proposes `PeakHoursAvailabilityStatus` as a new status family.

F.15 result:

* SCR-F15-S14 fails if the only difference is a time window.
* F.10 governs the status-family and window claim.
* F.14 and F.18 block a new durable name unless a new recovered status family is present.

### F.15:13.6 - Bias-Annotation

F.15 blocks unification-bias: the temptation to treat one shared label, one table row, one bridge, one alias, or one changed edition as if it already proved a common meaning. It also blocks kind-transfer bias: a role description, status window, evidence claim, publication-use claim, or source relation inside a slice does not become governed by F.15 merely because the slice mentions it. The failed claim returns to the direct governing pattern.

### F.15:14.5 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-F15-1` | Name the unification slice and the current or changed moving parts before applying SCR or RSCR rows. |
| `CC-F15-2` | Check local contexts, Local-Senses, SenseCells, rows, RoleDescriptions, bridges, status windows, aliases, and public names under their direct patterns. |
| `CC-F15-3` | Treat a failed rule as a return to the direct governing pattern, not as permission for F.15 to absorb that pattern's object. |
| `CC-F15-4` | Require bridge kind, direction, `CL`, loss, admitted use, and witness before cross-context reuse. |
| `CC-F15-5` | Recheck only the changed moving parts when an edition, row, bridge, role description, alias, name, or status window changes. |

### F.15:14 - Common Anti-Patterns and How to Avoid Them

| Code | Anti-pattern | Symptom | Why it breaks | Harness catch and repair |
| --- | --- | --- | --- | --- |
| H1 | Row of one | A Concept-Set row spans one context | Fake unification | SCR-F15-S9 fails; drop the row or add the second SenseCell |
| H2 | Bridge by label | Same name is assumed across contexts | Imports meaning and hides loss | SCR-F15-S12 fails; write a Bridge Card or withdraw the claim |
| H3 | Silent edition swap | A new edition keeps the old context without a recency decision | Retcons earlier claims | RSCR-F15-E1 fails; declare new context or explicit recency |
| H4 | Locality blur | A Local-Sense mixes contexts | Cross-context clustering | SCR-F15-S3 fails; split back by context |
| H5 | Window as type | A time or scale variant becomes a new status type | Status-family inflation | SCR-F15-S14 or RSCR-F15-E11 fails; use F.10 value or window |
| H6 | Role fusion by convenience | A bundle or incompatibility becomes one RoleDescription | Hides role relation structure and assignment checks | SCR-F15-S15 fails; use A.2.7, A.2.1, F.6, and A.15.1 |
| H7 | Alias as merge | Alias hides meaning change | Loses history | RSCR-F15-E8 fails; mint new RoleDescription or row |
| H8 | CL optimism | Bridges quietly strengthen over time | Over-trusts reuse | RSCR-F15-E9 or E10 fails; recheck witnesses and admitted use |
| H9 | Plain label drift | Plain label suggests another kind | Reader imports wrong prototype | SCR-F15-T2 or T3 fails; repair label or add kind head and gloss |

### F.15:15 - Closure conditions

A unification slice is locally admissible for reuse when:

1. every triggered static conformance rule holds for the current snapshot;
2. every changed moving part has a regression result;
3. each failed rule names the direct governing pattern before reuse;
4. at least one witness exists for each live Bridge, row, RoleDescription rename, status-window change, or public naming change;
5. the record names tempting non-admitted uses such as role assignment, performed-work attribution, source authority, publication authority, status transfer, and evidence use.

Closure is local to the slice and current use. A later context edition, row change, Bridge endpoint change, RoleDescription change, public-name change, or status-window change reopens the relevant RSCR rows.

### F.15:15.1 - Consequences

**Benefits.** F.15 makes locality, bridge strength, and edition continuity visible before a slice is reused. It lets terminology, role-description, status-window, bridge, and naming patterns remain direct owners of their objects while still giving the combined slice one checkable harness.

**Costs.** A slice that looks unified by label or table shape may fail until witness rows, bridge cards, local contexts, and direct-governing-pattern returns are explicit.

**Failure avoided.** F.15 prevents row-shaped local notes, alias-only rewrites, bridge optimism, role/status inflation, and source/evidence/publication claims from becoming hidden global meanings.

### F.15:15.2 - Rationale

Unification needs a harness because cross-context reuse is useful only after locality, parsimony, bridge strength, and regression continuity are preserved. F.15 therefore checks the joint slice without becoming a new ontology for contexts, roles, statuses, bridges, evidence, publications, or names.

### F.15:17 - SoTA-Echoing

| External or FPF tradition | Useful pressure | F.15 settlement |
| --- | --- | --- |
| Local-context terminology and controlled vocabulary practice | Meaning is local before it is reused across a wider audience. | Context, Local-Sense, SenseCell, and Concept-Set row checks precede public naming. |
| Model and standard edition management | Edition changes can alter meaning even when the label stays familiar. | RSCR rows require new context, recency, retirement, or explicit continuity. |
| Assurance and evidence practice | Reuse strength should not exceed the weakest bridge or changed witness. | Bridge `CL`, loss, admitted use, and fresh witnesses bound downstream claims. |
| FPF role and status repair | Source labels often hide role, status, evidence, or publication claims. | F.15 keeps each failed claim under its direct pattern instead of becoming a second ontology. |

Currentness rule: treat the current Part F and role-method-work patterns named in `Builds on` and `Coordinates with` as the source of governing interpretation. If F.4, F.9, F.10, F.17, F.18, A.2.1, F.6, A.15.1, A.10, B.3, E.17, or E.10.D2 changes a governed value, relation, admitted use, or boundary, recheck only the affected SCR or RSCR rows and the worked case that exercises the changed boundary.

### F.15:16 - Relations

* **F.1, F.2, F.3.** Provide contexts, terms, Local-Senses, and SenseCells checked by SCR-F15-S1 through S6.
* **F.4, A.2, A.2.1, F.6, A.15.1.** Govern RoleDescription, role assignment, and performed-work claims that F.15 must not absorb.
* **F.7 and F.8.** Govern rows and mint-or-reuse decisions checked by SCR-F15-S9 through S11 and RSCR-F15-E5 through E6.
* **F.9 and B.3.** Govern Bridge Cards, `CL`, loss, and assurance penalties.
* **C.34.** Provides architecture-specific preservation or equivalence adequacy when a later slice claims that selected architecture structures still correspond after renaming, bridging, projection, coarsening, or conformance strengthening. F.15 checks regression; C.34 names the preserved and lost structure for the architecture use.
* **F.10.** Governs status family, value, confidence, and window claims.
* **F.13, F.17, F.18.** Govern aliases, public term sheets, and durable names.
* **F.14.** Governs anti-explosion before names are minted for role-like and status-like families.
* **A.10, E.17, E.10.D2.** Govern evidence, publication, source, and description-use claims when they appear inside a slice.

### F.15:18 - Didactic distillation

Use F.15 as a small check over a slice, not as a new vocabulary machine. First, check locality: contexts are named, local senses are inside their contexts, rows really cross contexts, RoleDescriptions describe one local role, bridges state kind and loss, and status variation stays with status windows. Then check change: editions, rows, bridges, role descriptions, aliases, names, and status windows either preserve their earlier meaning or state the change. When a check fails, do not patch the label. Treat the claim under the direct governing pattern and repair the value.

### F.15:End

