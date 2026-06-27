## F.9 - Alignment and Bridge across Contexts
> **Type:** Pattern
> **Status:** Stable

**"Translate across contexts; never collapse them."**

**Type:** Architectural pattern.
**Status:** Stable.
**Normativity:** Normative.
**Builds on:** E.10.D1 (context discipline: Context = `U.BoundedContext`); F.0.1 (`senseFamily` and status-modality guard; bridge-only crossing); F.1 (contexts fixed); F.2 and F.3 (SenseCells exist); F.7 (Concept-Set rows depend on bridges); F.8 (mint-or-reuse decision consumes bridge results without strengthening them).

**Coordinates with:** A.2, A.2.1, F.4, F.5, F.6, and A.15.1 for work-facing role, role-description, role-assignment, and performed-work claims; A.6.5 for relation-slot discipline; C.29 for mathematical-lens use; B.3 for assurance penalties; A.6.3.CSC for controlled coarsening; C.26.1 and C.26.2 for quantum-like export boundaries.

**Plain entry cues (informative).** Context-to-context translator; sense bridge.

### F.9:1 - Intent and applicability

**Intent.** Provide a conceptual discipline for relating `SenseCells` from different `U.BoundedContext`s. A Bridge states what relation holds, which direction matters, how much congruence is admitted by `CL`, what is lost, and which cross-context use remains admissible.

**Applicability.** Use this pattern when an author needs to compare local senses across contexts, reuse a familiar label, connect design-time and run-time senses, compare two standards' terms, or justify a row in the Concept-Set table.

**Primary EntityOfConcern in plain terms.** One Bridge Card relating two `SenseCells` across different `U.BoundedContext`s. The EoC is not a transport chain, not a work process, not a role assignment, and not one global meaning layer.

**Admissible move in plain terms.** Declare bridge kind, direction, `CL`, loss, and admitted use so cross-context sense use stays inspectable without collapsing local meanings into silent equivalence.

**Primary working reader.** An author, checker, or practitioner preparing one bridge card, comparative bridge note, or concept-set row that depends on cross-context sense use.

**Use this when.** Use F.9 when the same term, role name, quality label, status label, measurement label, method label, or structural label appears in more than one context and the team is about to treat that overlap as if it were already equivalence or safe substitution.

**What goes wrong if missed.** Teams fall back to shared labels, string-equals shortcuts, or informal analogies, then quietly smuggle equivalence, substitution, structural inference, or role assignment across contexts without stating kind, direction, `CL`, or loss.

**What this buys.** One explicit bridge discipline that lets a team compare contexts and reuse names while keeping direction, loss, and the limits of admissible substitution visible.

**Not this pattern when.** Not F.9 when the case is still only one local context, when the needed claim is a role assignment, performed-work attribution, evidence use, status use, source use, publication use, assurance claim, gate claim, decision claim, or mathematical-lens use. Use the direct governing pattern first; cite F.9 only when cross-context sense alignment itself is live.

**Recognition versus assurance note.** Intent, applicability, this boundary, and the first worked case are the recognition block. Bridge kinds, `CL`, conformance, and relation sections are assurance blocks; they tighten the same Bridge Card claim instead of widening F.9 into role assignment, work execution, governance, or one global meaning layer.

### F.9:2 - Problem frame

Cross-context work fails in predictable ways:

1. **String-equals fallacy.** Identical spellings such as "process", "role", "accuracy", or "ready" are taken as identical meaning.
2. **Scope creep.** A naming convenience is stretched into role assignment, status transfer, work attribution, evidence use, or structural inference.
3. **Design-run jumping.** Design artefacts are substituted for run-time occurrences, or run-time occurrences are treated as design definitions.
4. **Direction amnesia.** Narrower and broader relations are treated as symmetric.
5. **Loss blindness.** Differences in unit, granularity, precondition, time stance, enforcement locus, or viewpoint are left unstated.

F.9 answers these failures by making relation, direction, loss, `CL`, and admitted use explicit.

### F.9:2.1 - Problem

A shared label across contexts can look like identity, substitution permission, status transfer, evidence authority, role assignment, work attribution, or structural equivalence before any bridge relation is declared. The problem is to preserve useful cross-context comparison while stating the local senses, bridge kind, direction, confidence level, losses, and admitted use so the bridge does not silently become another governed claim.

### F.9:3 - Forces

| Force | Tension to resolve |
| --- | --- |
| Locality versus reuse | Senses are context-local, yet people need common labels and comparison points across contexts. |
| Simplicity versus fidelity | Few bridge kinds are teachable; too few hide material mismatches. |
| Admissibility versus usefulness | Cross-context reuse should be possible, but only at the use level the bridge actually admits. |
| `senseFamily` purity versus explanation | Substitution must preserve `senseFamily`; explanation may cross `senseFamily` boundaries without implying sameness. |
| Bridge discipline versus direct governing patterns | F.9 can bound cross-context sense alignment, but it must not create role assignments, work records, evidence relations, or status relations by itself. |

### F.9:4 - Solution

A Bridge is a declared correspondence between two local senses. It always names:

1. the two `SenseCells`,
2. bridge kind,
3. direction if direction matters,
4. `CL`,
5. Loss Notes,
6. counter-example or invariant evidence,
7. admitted use.

Some Bridges admit naming or bounded substitution of sense. Interpretation Bridges admit explanation only. A Bridge never creates a `U.RoleAssignment`, never attributes performed work, never turns an episteme into evidence by itself, and never admits a durable U-kind.

### F.9:5 - Minimal vocabulary

* **Context** - shorthand for `U.BoundedContext` per E.10.D1.
* **SenseCell** - the pair `(Context, Local-Sense)` from F.3.
* **Bridge** - a declared relation between two `SenseCells` with kind, direction, `CL`, Loss Notes, and admitted use.
* **CL (Congruence Level)** - ordinal congruence class `0..3` for one Bridge.
* **Admitted use** - what the Bridge lets a downstream claim do without overclaim.
* **Naming-only** - cross-context prose label or Concept-Set row label only.
* **Role-description naming** - a row or label may inform a `RoleDescription` name for one local `U.Role`; it does not assign that role and does not attribute performed work.
* **Type-structure** - structural inference across contexts; admissible only at `CL = 3` with named invariants.
* **Explanation-only** - interpretation relation across sense families; no row substitution and no direct role, status, work, evidence, gate, or decision effect.
* **senseFamily** - the local meaning family used by Part F, such as Role, Status, Measurement, Type-structure, Method, Work occurrence, Evidence-use, or Policy-use. A `senseFamily` label is not a durable U-kind by itself.

### F.9:6 - Bridge kinds

F.9 distinguishes substitution bridges from interpretation bridges.

#### F.9:6.1 - Substitution bridges

These relate `SenseCells` in the same `senseFamily` and may admit bounded substitution of sense.

1. **Equivalence** - near-identity of sense. Symmetric and rare.
   Use: may admit Type-structure rows only when `CL = 3` and invariants match.
   Loss Notes: none or profile-level differences, with the invariant evidence stated.

2. **Narrower-than and Broader-than** - proper inclusion of sense. Directional.
   Use: narrower-to-broader may admit Naming-only and, at `CL >= 2`, role-description naming or other same-family name reuse. Broader-to-narrower is not admitted unless a separate Bridge states it.
   Loss Notes: special cases, enforcement conditions, or local constraints that fail to carry.

3. **Partial-overlap** - non-empty intersection where neither sense includes the other.
   Use: Naming-only at best. It never admits role assignment, performed-work attribution, or Type-structure inference.
   Loss Notes: A-only sense and B-only sense.

4. **Disjoint** - explicit contrast.
   Use: contrastive explanation only.
   Loss Notes: not applicable; the claim is incompatibility.

#### F.9:6.2 - Interpretation bridges

These explain connections across `senseFamily` boundaries. They do not admit substitution or Concept-Set rows beyond local explanation.

5. **Design-spec-to-run-occurrence** - a design sense relates to a run-time occurrence sense.
   Example: `BPMN:Process` to `PROV:Activity`.
   Use: explain design-to-run correspondence.
   Loss Notes: process model versus occurrence, control structure versus temporal extent.

6. **Measurement-evidence-for** - a measurement sense evidences or quantifies another sense.
   Example: `SOSA:Observation` to `ITIL:SLO fulfilment`.
   Use: explain evaluation; direct evidence-use remains with A.10, B.3, E.17, F.10, or the local status pattern.

7. **Policy-constraint-on** - a policy or deontic sense constrains another sense.
   Example: `ODRL:Duty` to service behavior.
   Use: explain a constraint relation; direct policy, gate, or authority claims remain with the governing pattern.

8. **Viewpoint-correspondence** - one view, report, model, dashboard, or viewpoint-bound episteme corresponds to another view over an EntityOfConcern.
   Use: explain cross-view comparison; direct architecture-description, episteme, publication, or source-use claims remain with their governing patterns.

### F.9:7 - CL scale and admitted-use thresholds

| CL | Name | Intuition | Typical loss | Admitted use |
| --- | --- | --- | --- | --- |
| 0 | Opposed | Intentionally contrastive or disjoint | incompatibility | contrastive explanation only |
| 1 | Comparable | Shared label can orient readers, but senses differ materially | material sense divergence | Naming-only |
| 2 | Translatable | Bounded loss with examples and counter-examples | stated losses | Naming-only; role-description naming or other same-family name reuse; no direct assignment or work attribution |
| 3 | Near-identity | Invariants match; no material counter-example | profile-level only | Type-structure rows and other invariant-preserving same-family uses |

Thresholds:

* A Naming-only row requires `CL >= 1`.
* A Role-description naming row requires `CL >= 2`, the same Role `senseFamily`, and stated local-role losses. It still does not create a `U.RoleAssignment`.
* A Type-structure row requires `CL = 3` and matched invariants such as acyclicity, anti-symmetry, unit transform, cardinality, or signature-preserving relation shape.
* Interpretation Bridges remain Explanation-only regardless of `CL`.

B.3 may convert `CL` into an assurance penalty when a cross-context claim uses a Bridge.

### F.9:8 - Bridge Card

Use this compact record when a Bridge claim matters:

```text
BridgeCard:
  CellA:
  CellB:
  senseFamilyA:
  senseFamilyB:
  BridgeKind:
  Direction:
  CL:
  LossNotes:
  CounterExampleOrInvariantEvidence:
  AdmittedUse:
  NonAdmittedUse:
  DirectGoverningPatternIfNotF9:
  RevisionTrigger:
```

`AdmittedUse` states the strongest use the Bridge permits. `NonAdmittedUse` names the tempting overclaim, such as role assignment, work attribution, structural inference, source authority, or evidence use. `DirectGoverningPatternIfNotF9` points to the pattern that must govern that overclaim before it may become a claim.

`BridgeId` and policy or edition identifiers cited by a Bridge Card are registry references, not semantic symbols exported by signatures. Do not demand them through `SignatureManifest.provides`; validate that referenced registry entries exist and are edition-pinned when required.

### F.9:9 - Boundary to coarsening and quantum-like export

Use F.9 first when meaning, label, relation, field, record, model output, report, or representation crosses a bounded context or publication context. A bridge does not become quantum-like because it is lossy, approximate, contextual, or hard to translate. It becomes quantum-like only when the bridge or export claim still depends on order sensitivity, incompatible frames, a probe that changes represented state, or no faithful-enough export for the intended use.

Boundary sequence:

1. Build the ordinary Bridge Card first: cells, sense families, kind, direction, `CL`, loss, counter-example or invariant evidence, and admitted use.
2. State which state, relation, evidence, metric, option, or viability claim is said to survive the crossing.
3. State what the crossing omits, coarsens, re-keys, reframes, makes incomparable, or makes unsafe for the intended downstream use.
4. If the bridge or export claims to preserve action, intervention, manipulation, explanation, or cross-scale structure, state the causal-abstraction or approximate-causal-abstraction mapping before treating the coarsened bridge as a C.26 issue.
5. If asking, measuring, exporting, rendering, or bridging changes the represented state itself, coordinate with C.26.1.
6. If coordinated work or live state is not exported faithfully enough for the intended use by any one report or bridge, coordinate with C.26.2.
7. If the crossing is a state representation with declared source-loss mode or reduced recoverability, coordinate with A.6.3.CSC, A.6.3.RT, and C.26.

When the bridge result will be reused for decision, comparison, assurance, release, audit, or cross-context action, add a state-export line to the Bridge Card:

| Field | Ask |
| --- | --- |
| Surviving reading | Which state, relation, evidence, metric, option, or viability reading is claimed to survive the crossing? |
| Loss or change | What is omitted, coarsened, re-keyed, reframed, made incomparable, or no longer decision-safe? |
| Probe or frame condition | Does asking, measuring, exporting, rendering, or bridging change the represented state? |
| Admitted use | Which decision, explanation, triage, comparison, or orientation use remains supported? |
| Non-admitted use and return condition | Which stronger use still needs more support, and when must the source context, evidence carrier, or fuller representation be reopened? |

A lighter cross-context note may orient readers, but it is not a Bridge Card. Before any equivalence, substitution, Naming-only row, interoperability, release, audit, assurance, or action use, reopen the source-bearing episteme or source publication needed for the Bridge Card and publish the actual Bridge Card.

### F.9:10 - Invariants

1. **Locality first.** A Bridge relates `SenseCells`, never contexts as wholes and never strings alone.
2. **senseFamily discipline.** Substitution Bridges preserve `senseFamily`. Interpretation Bridges may cross `senseFamily` boundaries but remain Explanation-only.
3. **Direction clarity.** Directional kinds state direction explicitly.
4. **CL honesty.** `CL <= 2` needs at least one counter-example or boundary case. `CL = 3` needs invariant evidence.
5. **Loss visibility.** Every Bridge carries Loss Notes, even when the note is "none" at `CL = 3`.
6. **Weakest-link row discipline.** A Concept-Set row's admitted use is bounded by the weakest participating Bridge.
7. **No role-assignment by bridge.** A Bridge may inform RoleDescription naming or comparison; `U.RoleAssignment`, required-role satisfaction, and performed-work attribution remain with A.2.1, F.6, and A.15.1.
8. **No interpretation bridge substitution.** Interpretation Bridges cannot justify substitution rows.
9. **Design-run honesty.** If a context fixes a design-run distinction, the Bridge respects it or explicitly uses a design-spec-to-run-occurrence interpretation bridge.
10. **Kernel restraint.** Bridges do not promote ad hoc sameness into a durable U-kind; E.24.UK, A.11, and F.8 govern that decision.
11. **Non-inheritance of contexts.** Bridges do not imply is-a relations between contexts.

### F.9:11 - Micro-examples

1. **Participant versus Agent.**
   Cells: `BPMN:Participant` and `PROV:Agent`.
   Bridge: Partial-overlap, `CL = 2`.
   Loss: participation scope versus attribution scope.
   Admitted use: Naming-only label "actor"; no role assignment.

2. **Process design versus Activity occurrence.**
   Cells: `BPMN:Process` and `PROV:Activity`.
   Bridge: Design-spec-to-run-occurrence, `CL = 2`.
   Loss: model structure versus temporal occurrence.
   Admitted use: Explanation-only.

3. **Observation versus SLO fulfilment.**
   Cells: `SOSA:Observation` and `ITIL:SLO fulfilment`.
   Bridge: Measurement-evidence-for, `CL = 2`.
   Loss: sampling window and target definition.
   Admitted use: Explanation-only; direct evidence or status claim goes to A.10, B.3, F.10, or the local status pattern.

4. **Subtype across OWL and curated taxonomy.**
   Cells: `OWL:SubClassOf` and `TaxonomyX:is-a`.
   Bridge: Equivalence, `CL = 3` only when acyclicity, anti-symmetry, and class-level reasoning match.
   Admitted use: Type-structure row.

5. **Accuracy in metrology versus data quality.**
   Cells: `ISO80000:accuracy` and `ISO25024:accuracy`.
   Bridge: Partial-overlap, `CL = 2`.
   Loss: instrument perspective versus dataset perspective.
   Admitted use: Naming-only row "accuracy"; methods and measurements stay context-local.

### F.9:12 - Worked examples

#### F.9:12.1 - Service acceptance, executions, and observations

A service team uses an SLO, runtime observations, and an automation-process model.

Bridge Cards:

```text
BridgeCard:
  CellA: ITIL4:SLO@service-design
  CellB: SOSA:Observation(availability)@monitoring-run
  senseFamilyA: Status
  senseFamilyB: Measurement
  BridgeKind: Measurement-evidence-for
  Direction: CellB evidences CellA
  CL: 2
  LossNotes: sampling window; clock skew; target definition
  CounterExampleOrInvariantEvidence: an observation can be true while the service status claim remains under review
  AdmittedUse: Explanation-only
  NonAdmittedUse: do not treat the observation as the SLO status itself
  DirectGoverningPatternIfNotF9: F.10 or B.3 for status or assurance use
  RevisionTrigger: monitoring window or SLO definition changes
```

The same team may publish a Naming-only row for "availability" if each participating Bridge reaches `CL >= 1`, but no observation becomes the status target and no process design becomes a performed work occurrence by that row.

#### F.9:12.2 - Behavioral role versus access role

A process model has `BPMN:Participant`; an access-control catalogue has `NIST-RBAC:Role`.

Bridge Card result:

* Bridge kind: Partial-overlap.
* `CL`: 2.
* Loss Notes: assignment moment, enforcement locus, multiplicity, accountability boundary.
* Admitted use: Naming-only label "actor" and, if a local `U.Role` is separately recovered, role-description naming.
* Non-admitted use: no `U.RoleAssignment`, no required-role satisfaction, no performed-work attribution.

If a project wants an RBAC role to count for a work step, it must open A.2.1 or F.6 and recover a local `U.RoleAssignment`; F.9 supplies only the cross-context sense relation and the stated losses.

#### F.9:12.3 - Equivalence of subtype notions for structural rows

`OWL2:SubClassOf` and a curated taxonomy `is-a` relation can admit a Type-structure row only when the curated taxonomy is acyclic, anti-symmetric, and uses class-level reasoning compatible with the OWL profile being cited. If those invariants are absent, the Bridge is demoted to `CL = 2` and the admitted use falls to Naming-only or explanation.

#### F.9:12.4 - Setpoint versus service target

`CTRL:setpoint` and `ITIL:target` may look close because both are called targets. F.9 keeps them apart:

* `CTRL:setpoint` is a physical reference value in a control context.
* `ITIL:target` is a service objective or requirement-like status claim.
* Bridge kind is usually Disjoint or Partial-overlap, not Equivalence.

The result is didactic contrast or Naming-only orientation, not substitution in control or service calculations.

### F.9:19 - Archetypal Grounding

#### F.9:19.1 - Tell

A Bridge is not a synonym claim and not an enactment edge. It is a context-bounded correspondence record that tells a reader what may be named, compared, or inferred, and what is lost when a sense crosses context.

#### F.9:19.2 - Show: service lane

A service team may reuse the word `availability` across monitoring, SLO review, and architecture discussion. F.9 requires Bridge Cards that separate observation, status target, and architectural concern rather than treating the shared label as silent sameness. The practical gain is that naming convenience survives while substitution rights stay bounded by `senseFamily`, `CL`, and Loss Notes.

#### F.9:19.3 - Show: role lane

A process team and an access-control team both use `operator`. F.9 can admit a Naming-only row and may admit RoleDescription naming when the local `U.Role` remains clear. It cannot assign the access-control role to a work occurrence. That claim requires A.2.1 and F.6.

#### F.9:19.4 - Show: episteme lane

A comparative bundle may say that two traditions both discuss `readiness`. Under F.9, that statement remains explanatory until the author publishes the cells, bridge kind, direction, `CL`, Loss Notes, and counter-example. The Bridge then becomes auditable correspondence rather than rhetorical shortcut.

### F.9:20 - Bias-Annotation

Lenses tested: governance, architecture, ontology and episteme, pragmatics, didactics. Scope: universal for cross-context correspondence and reuse.

* **Governance bias.** F.9 raises the declaration bar by requiring explicit Bridge Cards. Mitigation: keep the card compact and use weakest-link discipline as the default review heuristic.
* **Architecture bias.** The pattern prefers typed bridge declarations over friendly synonym prose. Mitigation: allow Naming-only and Explanation-only cases so useful comparisons are not blocked.
* **Ontology and episteme bias.** F.9 is local-first and resists global meaning claims. Mitigation: reuse remains possible through explicit correspondence, direction, and Loss Notes.
* **Pragmatic bias.** Conservative `CL` assignment may feel slower than informal reuse. Mitigation: F.9 permits bounded use when the Bridge earns it; it blocks only silent overreach.
* **Didactic bias.** The short script can make Bridge Cards look simpler than they are. Mitigation: conformance tests, counter-examples, and weakest-link rules keep the teaching explanation tied to constraints.

### F.9:21 - Conformance Checklist

A Bridge publication conforms to F.9 iff:

1. **CC-F.9-1 - Well-typed Bridge declaration.** Every Bridge names two `SenseCells` bound to declared contexts and publishes kind, direction when needed, `CL`, Loss Notes, and admitted use.
2. **CC-F.9-2 - Substitution discipline.** Same-family substitution comes only from a substitution Bridge on the same `senseFamily`; Type-structure use requires `CL = 3` plus matched invariants.
3. **CC-F.9-3 - Interpretation embargo.** Interpretation Bridges remain Explanation-only and are not used to justify substitution or Concept-Set rows.
4. **CC-F.9-4 - CL honesty and loss visibility.** `CL <= 2` needs a counter-example or boundary case; `CL = 3` needs invariants; every Bridge has Loss Notes.
5. **CC-F.9-5 - Weakest-link row discipline.** Cross-context rows never claim a broader use or higher row-level `CL` than their Bridges admit.
6. **CC-F.9-6 - Role-boundary discipline.** Role-facing Bridges may inform RoleDescription naming or comparison, but actual `U.RoleAssignment`, required-role satisfaction, and performed-work attribution stay with A.2.1, F.6, and A.15.1.
7. **CC-F.9-7 - Registry-reference discipline.** `BridgeId` and cited policy pins are registry references, not signature-exported semantic symbols.
8. **CC-F.9-8 - Coarsened-note boundary.** A lighter note, summary, or comparison aid is not treated as a Bridge Card until the source-bearing episteme or publication needed for the Bridge Card is reopened and the Bridge is published.

### F.9:13 - Common Anti-Patterns and How to Avoid Them

| ID | Anti-pattern | Symptom | Why it breaks thinking | Repair |
| --- | --- | --- | --- | --- |
| AP-1 | String-equals becomes sense-equals | Same spelling used across contexts with silent identity claims. | Violates locality and invites false substitution. | State a Bridge kind; if unsure, default to Partial-overlap with Naming-only admitted use. |
| AP-2 | Stealth substitution | "Treat A like B for now." | Hidden policy with unknown loss; bridge result is used as role assignment, status transfer, or work attribution. | Publish a Bridge Card; then open the direct governing pattern for the non-F9 claim. |
| AP-3 | Stance jump by wording | "Activity is a Process." | Design sense and run occurrence are collapsed. | Use a design-spec-to-run-occurrence interpretation bridge and keep Explanation-only admitted use. |
| AP-4 | Symmetry hallucination | Directional bridges are treated as symmetric. | Narrower becomes broader or broader becomes narrower. | Record direction; only Equivalence is symmetric. |
| AP-5 | Disjoint but reused | `Disjoint` is declared, then a label or RoleDescription constraint is borrowed. | Declaration and use conflict. | Retract Disjoint, or stop reuse; if a thin comparison remains, mark contrastive explanation. |
| AP-6 | CL without counter-example | "These are CL=3" with no invariant check. | Inflates row scope. | For `CL = 3`, cite invariants; otherwise demote and add a counter-example. |
| AP-7 | Bridge inflation | Many near-duplicate Bridges between the same contexts. | Noise hides material alignments. | Prefer one Bridge per pair of cells per relevant `senseFamily`; fold variants into Loss Notes. |
| AP-8 | Row outruns Bridge | A Concept-Set row claims stronger use than the weakest participating Bridge admits. | Row scope exceeds the stated evidence. | Apply weakest-link discipline: row admitted use is no stronger than the weakest Bridge. |
| AP-9 | Bridge as durable U-kind | A Bridge is used to justify a new universal kind. | Re-globalizes meaning. | Keep kinds context-local unless E.24.UK, A.11, and F.8 admit a durable U-kind candidate. |
| AP-10 | Silent unit or scale mismatch | Measurements cross contexts without unit and scale notes. | Hidden dimensional error. | Put units and scales in Loss Notes; if they cannot be related, use Disjoint or Partial-overlap. |
| AP-11 | Coarsened note treated as Bridge Card | A summary or redacted comparison is used as if it made substitution admissible. | A bridge claim is smuggled through a lighter rendering. | Reopen the source-bearing episteme or publication and write the Bridge Card before bridge-bearing use. |

### F.9:14 - Reasoning primitives

All judgements here are conceptual. They admit or reject specific cross-context sense-use moves; they are not work-enactment records.

#### F.9:14.1 - Bridge declaration

```text
Bridge(A@ContextA, B@ContextB) :
  senseFamilyA,
  senseFamilyB,
  kind,
  direction,
  CL,
  LossNotes,
  admittedUse
```

Interpretation: there is a declared Bridge between two local senses with stated attributes.

#### F.9:14.2 - Naming-only scope

```text
Bridge(A,B) with kind in {Equivalence, Narrower-than, Broader-than, Partial-overlap}
and CL >= 1
=> A and B may share a label in prose or a Naming-only Concept-Set row.
```

Interpretation: the shared label remains a label; it carries no structural, role-assignment, status, evidence, or work effect.

#### F.9:14.3 - Same-family substitution of sense

```text
Bridge(A,B) with same senseFamily,
kind in {Equivalence, Narrower-than, Broader-than},
declared direction A -> B,
CL >= 2,
and stated LossNotes
=> A may stand in for B only for the admitted same-family sense use.
```

Interpretation: same-family substitution is bounded by direction, `CL`, loss, and admitted use. For role material, this reaches RoleDescription naming or comparison only; role assignment itself remains with A.2.1 and F.6.

#### F.9:14.4 - Type-structure scope

```text
Bridge(A,B) with same Type-structure senseFamily,
kind = Equivalence,
CL = 3,
and matched invariants
=> A and B may participate in a Type-structure row.
```

Interpretation: Type-structure use is the strongest F.9 row use and requires invariant evidence.

#### F.9:14.5 - Interpretation embargo

```text
Bridge(A,B) with interpretation kind
=> Explanation-only.
```

Interpretation: design-spec-to-run-occurrence, measurement-evidence-for, policy-constraint-on, and viewpoint-correspondence Bridges explain relations across sense families but do not admit substitution.

#### F.9:14.6 - Weakest-link rule

```text
Row R uses {Bridge_i}
=> admittedUse(R) <= min_i(admittedUse(Bridge_i))
and CL(R) <= min_i(CL(Bridge_i)).
```

Interpretation: a row is never stronger than its weakest Bridge.

#### F.9:14.7 - Direction guard

```text
Bridge kind = Narrower-than with direction A -> B
=> not(B may stand in for A).
```

Interpretation: narrower-to-broader does not invert.

#### F.9:14.8 - Loss accumulation

```text
A -> B with Loss L1
B -> C with Loss L2
=> A -> C only if the same senseFamily is preserved;
   CL becomes min(CL1, CL2);
   Loss accumulates as L1 plus L2.
```

Interpretation: chained cross-context substitution is rare. If used, loss and `CL` degrade rather than disappear.

### F.9:16 - Revision law

1. **Edition shift in a context.** Re-evaluate affected cells; if sense moved, split the Bridge or lower `CL`.
2. **New mismatch evidence.** Add a counter-example; decrease `CL` or change kind.
3. **Convergence.** Raise `CL` only when invariants demonstrably match and counter-examples no longer apply.
4. **senseFamily correction.** If a cell's `senseFamily` was mistyped, fix the cell first in F.3, then revisit Bridges.
5. **Row overreach.** If a row's use exceeds the weakest Bridge, split the row or lower its admitted use.
6. **Bridge sprawl.** Consolidate near-duplicates into one Bridge with richer Loss Notes.

### F.9:17 - Acceptance tests

#### F.9:17.1 - Static conformance

* **SCR-F9-S01 (Well-typed).** Every Bridge names two `SenseCells`, each bound to a context from F.1, and states `senseFamily`, kind, direction when needed, `CL`, Loss Notes, and admitted use.
* **SCR-F9-S02 (senseFamily discipline).** Any substitution Bridge preserves `senseFamily` and uses Equivalence, Narrower-than, or Broader-than.
* **SCR-F9-S03 (Loss visibility).** Every Bridge has non-empty Loss Notes. "None" is valid only with `CL = 3` and stated invariants.
* **SCR-F9-S04 (Counter-example hygiene).** Bridges with `CL <= 2` carry at least one counter-example or boundary case; Bridges with `CL = 3` cite invariants.
* **SCR-F9-S05 (Row compliance).** Every Concept-Set row shows an admitted use no greater than the weakest participating Bridge.
* **SCR-F9-S06 (Role boundary).** Any role-facing Bridge states that role assignment and performed-work attribution remain with A.2.1, F.6, and A.15.1.

#### F.9:17.2 - Regression checks

* **RSCR-F9-E01 (Edition churn).** When a context edition changes, revalidate all Bridges touching it.
* **RSCR-F9-E02 (Counter-example drift).** New counter-examples lower `CL`; deleting examples does not automatically raise it.
* **RSCR-F9-E03 (senseFamily drift).** If a cell's `senseFamily` changes, all Bridges crossing that cell are retyped.
* **RSCR-F9-E04 (Weakest-link enforcement).** Adding a lower-CL Bridge to a row lowers the row's admitted use or forces a split.
* **RSCR-F9-E05 (Role-boundary preservation).** No Bridge revision creates a `U.RoleAssignment` or performed-work attribution without the direct governing pattern.

### F.9:18 - Didactic distillation

A Bridge translates between local senses from different contexts. It declares relation kind, direction, `CL`, loss, and admitted use. Substitution of sense requires the same `senseFamily` and enough `CL`; Type-structure use needs `CL = 3` with invariants; interpretation Bridges explain but do not substitute. Rows obey the weakest Bridge. Role-description naming is not role assignment. Translate across contexts; never collapse them.

### F.9:22 - Consequences

**Benefits.** F.9 lets FPF compare, translate, and partially reuse ideas across contexts without collapsing them into one vocabulary. It gives downstream rows, claims, and assurance reasoning an explicit Bridge Card instead of relying on prose similarity.

**Costs.** The pattern adds explicit bridge declaration and can feel heavier than informal comparison. Mitigation: use Naming-only or Explanation-only when that is enough, and reserve higher-scope uses for Bridges that carry the required `CL`, invariants, and direct-pattern boundaries.

**Failure mode avoided.** A Bridge can no longer be used as a quiet substitute for role assignment, status transfer, evidence authority, publication authority, or performed-work attribution.

### F.9:23 - Rationale

The core move of F.9 is simple: cross-context work is unavoidable, but silent sameness is unacceptable. A Bridge therefore does two jobs at once:

* it preserves practical comparison and bounded reuse where the relation is genuinely available,
* it keeps non-identity visible through direction, Loss Notes, `CL`, and weakest-link use.

Without that discipline, every shared label becomes a hidden ontology merger. With it, cross-context comparison stays teachable, auditable, and compatible with direct governing patterns.

### F.9:24 - SoTA-Echoing

**SoTA note.** This section does not create a second bridge rule track. It stays truthful only when Bridge kinds, `CL`, Loss Notes, weakest-link use, the A.6.3.CSC boundary, and the review matrix below still tell the same story about admissible cross-context sense use.

| Claim need | SoTA practice | Primary source | Alignment with F.9 | Adoption status |
| --- | --- | --- | --- | --- |
| Shared labels across contexts are not enough for cross-context reuse. | Terminology and ontology practice distinguishes objects, concepts, definitions, designations, and typed relations instead of treating a shared string as identity. | ISO 704:2022; ISO 1087:2019; ISO/IEC 21838-2:2021 (BFO). | F.9 requires typed `SenseCells`, bridge kind, direction where needed, `CL`, and Loss Notes rather than string-equals identity. | Adopt and adapt explicit term, concept, and relation discipline into Bridge Cards. |
| Viewpoint and context boundaries must stay explicit when descriptions are reused. | Architecture-description practice distinguishes entity of interest, architecture description, viewpoint, view, model kind, concern, and correspondence. | ISO/IEC/IEEE 42010:2022. | F.9 binds every Bridge to declared contexts and forces rows to obey weakest-link use instead of outrunning correspondences. | Adopt boundary-explicit correspondence discipline. |
| Data, catalog, and validation practice separates metadata, validation conditions, and exchange from substitution authority. | Web-data and semantic-web standards make metadata, provenance, structural constraints, validation, and catalog federation explicit without turning metadata into the data itself. | W3C Data on the Web Best Practices (2017); W3C SHACL (2017); W3C DCAT v3 (2024). | F.9 separates explanatory bridges from substitution bridges and keeps Bridge publication distinct from coarsened notes or catalog-style discovery aids. | Adapt explicit metadata and validation practice; reject discovery or gloss as substitution authority. |
| Model-based engineering uses traceable model elements and formal semantics, but interoperability is not semantic identity. | Current MBSE practice improves precision, traceability, and interoperability through explicit model elements, libraries, APIs, and formal semantics. | OMG SysML v2.0 Language Specification (2025); OMG KerML v1.0 Specification (2025). | F.9 uses Bridge Cards as reviewable relations whose `CL` and loss fields remain narrower than any tool interchange claim. | Adapt traceable relation discipline; reject interchange success as proof of same meaning. |

### F.9:25 - Bridge Card publication discipline

#### F.9:25.1 - Minimal declaration

A usable Bridge Card makes visible:

* the two typed `SenseCells`,
* bridge kind,
* direction when direction matters,
* declared `senseFamily` for each cell,
* `CL`,
* Loss Notes,
* counter-example or invariant evidence,
* admitted use and non-admitted use.

If any of these fields is absent, readers are forced back into inference by prose similarity, which F.9 blocks.

#### F.9:25.2 - One-pair default rule

The default declaration discipline is one primary Bridge per cell pair per relevant `senseFamily`, with richer Loss Notes rather than many near-duplicate cards. Local exceptions are admissible only when the cards genuinely differ in bridge kind, direction, `CL`, or admitted use.

#### F.9:25.3 - Revision over silent drift

If evidence changes bridge `CL`, direction, loss, or admitted use, revise the Bridge Card explicitly. Do not leave the Bridge in place while surrounding prose quietly changes its practical scope.

### F.9:26 - Bundle and endpoint interaction

Viewpoint bundles, quality bundles, dashboards, reports, and endpoint bundles may cite Bridges, but they do not absorb bridge semantics. F.9 remains the pattern for cross-context alignment, while the citing bundle keeps its own ontology.

When a quality-family claim crosses contexts, bridge loss and `CL` affect what may be compared or reused, but they do not retype the quality family itself. Any resulting assurance penalty feeds B.3 rather than changing the ontology of the quality bundle.

A `F.9.1` stance overlay may help readers interpret a Bridge, but the Bridge Card remains primary. If the overlay overstates bridge kind, direction, `CL`, Loss Notes, or admitted use, narrow or remove the overlay.

### F.9:27 - C.29 mathematical-lens use relation

When meaning, substitution, sense cells, direction, `CL`, or admitted use crosses context, write the F.9 Bridge Card first. Add the applicable C.29 output only for mathematical-lens use: candidate mathematical object, `LensMappingMode`, preserved and lost structure, exposed invariants or distinctions, lens-use admissibility value, admissible and non-admissible use, and stop condition. Do not duplicate Bridge semantics inside MathLensUse. A Bridge may make a mathematical lens interpretable across contexts without making it substitution-safe.

### F.9:28 - Review matrix

A reader can test bridge integrity with seven questions:

1. Are the two cells and contexts explicit?
2. Is the bridge kind the least-committing truthful kind rather than the friendliest one?
3. Does `CL` match the published counter-example or invariant evidence?
4. Are Loss Notes specific enough that the admitted use is really bounded?
5. If a row or bundle cites the Bridge, does it stay within the Bridge's admitted use?
6. If a stance overlay exists, does it stay within the Bridge Card's kind, direction, `CL`, Loss Notes, and admitted use?
7. If a role, status, evidence, source, publication, assurance, gate, decision, method, work, or mathematical-lens claim appears, has the direct governing pattern been opened instead of letting F.9 carry that claim?

Repair from same, equivalent, align, and map prose should therefore recover the Bridge Card first, then any row use, then any optional stance overlay. Doing it in the opposite order recreates silent equivalence under new vocabulary.

### F.9:15 - Relations

**Builds on:** E.10.D1, F.0.1, F.1, F.2, F.3, F.7, and F.8.

**Coordinates with:**

* **F.4 and F.5.** RoleDescription labels and durable names may cite F.9, but only after the local `U.Role` remains clear.
* **A.2.1, F.6, and A.15.1.** Role assignment, required-role satisfaction, and performed-work attribution are direct work-role claims, not bridge results.
* **F.8.** Mint-or-reuse decisions consume Bridge Cards and choose local phrase, alias, row, RoleDescription label, policy id, direct-pattern name, or block-or-lower decision without strengthening the Bridge.
* **A.6.5.** Relation-position labels and SlotSpec claims are governed by slot discipline, not by F.9.
* **C.29.** Mathematical-lens use may cite F.9 when the lens crosses contexts; C.29 still governs the mathematical object, preserved structure, lost structure, and lens-use admissibility.
* **C.34.** Structural correspondence, equivalence, or morphism adequacy may cite F.9 when the preservation claim crosses bounded contexts, source traditions, or local sense families. C.34 states preserved and lost architecture structure for the declared use; F.9 governs the Bridge Card, bridge kind, local sense loss, and cross-context admissibility.
* **B.3.** Assurance may apply `CL` penalties to cross-context claims.
* **A.6.3.CSC, C.26.1, and C.26.2.** Coarsened renderings and quantum-like state export need these patterns when export loss, probe effects, or no faithful-enough report becomes the live concern.

### F.9:End

