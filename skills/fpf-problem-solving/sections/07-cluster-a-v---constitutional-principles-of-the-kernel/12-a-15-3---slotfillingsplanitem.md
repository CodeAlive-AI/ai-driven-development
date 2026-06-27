## A.15.3 - SlotFillingsPlanItem

> **Tech-name:** `SlotFillingsPlanItem`
> **Plain-name:** planned slot-fillings baseline item
> **Short code:** `SFPI`
> **Type:** Definitional WorkPlanning pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part A -> A.15 work family
> **Builds on:** `A.15.2 U.WorkPlan`, `A.15.1 U.Work`, `A.6.5 U.RelationSlotDiscipline`, `E.10.D2`, `E.17`, `E.18.1`, `E.20`, and `E.24`
> **Used by:** P2W work-planning slices, suite or kit planned baselines, work-entry readiness checks, Part G planned-baseline references, and performed-work variance records
> **One-line purpose:** name one planned baseline item that states which planned fillers are intended for which SlotKinds of one slot-bearing description before performed work occurs.

**At a glance.** Use `SlotFillingsPlanItem` when a `U.WorkPlan` needs more than a date, budget, or intended method: it needs a reproducible planned baseline saying which planned fillers are intended for one slot-bearing description's SlotKinds.

**Use this when.** Use this pattern when a P2W, work-planning, or work-entry-readiness slice needs planned references, policy pins, method-description refs, edition pins, evidence-reference pins, guard-preparation refs, or crossing-policy refs to stay fixed before performed `U.Work`.

**First output.** One `SlotFillingsPlanItem` naming exactly one `target_slot_bearing_description_ref`, one `bounded_context_ref`, the EntityOfConcern under planning, a time selector or time rule, authoritative planned-filling rows, and any guard-preparation, evidence-reference, readiness-preparation, edition, or crossing-policy refs needed before performed work.

**Working use order.**

1. Confirm that the current claim is a planned baseline inside a `U.WorkPlan`, not the slot-bearing description itself and not performed work.
2. Name the target slot-bearing description and use its SlotSpecs from the governing description pattern, with A.6.5 slot discipline.
3. Name the EntityOfConcern under planning and the bounded context; add a grounding holon only when the current claim needs one.
4. Write planned-filling rows from SlotKind to planned filler, with ByValue or concrete RefKind mode and edition pins when reproducibility depends on them.
5. Keep projections, views, evidence-reference pins, guard-preparation refs, and crossing-policy refs as secondary references. They do not add rows, create evidence, pass a gate, or finalize launch values.

**Ordinary use.** For a minimal baseline, use context, time selector, target slot-bearing description, EntityOfConcern ref, and planned-filling rows.

**Reliance-bearing use.** Use the fuller record when reproducibility, launch-guard preparation, crossing expectations, suite or kit reuse, Part G universalization, publication-view projection, or P2W carry-through depends on the baseline.

**Stop condition.** Stop once the planned rows are explicit enough for the work-planning use, or lower the claim to a plan cue, source-gap note, relation governed by another FPF pattern, or blocked kind-definition gap without claiming a conforming planned baseline.

**What goes wrong if missed.** Teams hide planned choices in mechanism prose, suite descriptions, generated cards, "latest" references, local checklists, or execution logs. Later nobody can tell what was planned, what was performed, which edition changed, or which variance belongs to performed work.

**What this buys.** A small planned-baseline record that lets later performed work cite the intended slot fillings and record variance without rewriting the plan after the fact.

**Not this pattern when.** Not this pattern when the current claim is the slot-bearing description itself (`A.6.5` plus the governing description pattern), a mechanism definition (`A.6.1` or `E.20`), a performed work occurrence (`A.15.1`), an ordinary work plan without slot-filling rows (`A.15.2`), work-entry readiness or full-kit condition (`A.15.5`), evidence or assurance (`A.10` or `B.3`), a gate or constraint decision (`A.20` or `A.21`), publication-use behavior (`E.17`), or a declarative representation overread as work control (`C.2.P.DR`).

### A.15.3:1 - Context

`A.15.2` can already say that work is planned. Some plans also need to freeze a more specific relation: "for this planned work, this slot-bearing description will use these planned fillers in these SlotKinds under this bounded context and time rule."

That extra relation is not the target description, not the mechanism, not a publication view, and not the later performed work. It is a plan item inside work planning. `SlotFillingsPlanItem` gives that relation a stable place.

Typical situations:

- a CHR or CG-frame plan chooses comparator specs, normalization methods, indicator policies, or guard refs before work;
- a mechanism-suite plan chooses which suite description, method-description edition, or policy ref will be used later;
- a QD or archive plan fixes descriptor and distance-definition editions before selection work;
- a refresh or parity plan cites planned refs so later performed work can record variance rather than silently changing the plan.

### A.15.3:2 - Problem

Without an explicit `SlotFillingsPlanItem`, six failures recur:

1. **Plan and performed-work blur.** Planned fillers get treated as launch values or run-time actuals.
2. **Slot drift.** A SlotKind's meaning changes because the target description edition changed, but the plan still reads as if it meant the old description.
3. **Implicit latest.** Source text says "use latest" or "current best" without a time selector or pinned edition.
4. **View becomes authority.** A card, dashboard, or generated view becomes the de facto place where planned rows live.
5. **Mechanism prose hides planning.** Suite or mechanism text quietly carries chosen fillers even though those choices vary by plan instance.
6. **Variance disappears.** After work happens, the plan is edited to match the performed work, erasing the gap that audit or improvement needs.

### A.15.3:3 - Forces

| Force | Demand |
| --- | --- |
| WorkPlanning vs performed work | The baseline should be citeable before work without containing actuals, launch values, or gate outcomes. |
| Slot meaning stability | The plan can choose fillers; it cannot redefine the SlotKinds of the target description. |
| Edition and time honesty | References that matter for reproducibility need edition and time pins. |
| Suite and kit modularity | Suite descriptions can require planned baselines, but each plan instance still chooses its fillers separately. |
| Publication affordability | Cards and views help people read the baseline, but they cannot become a second canonical row source. |
| Audit and improvement | Later work needs a stable planned baseline so variance can be attributed and improved. |

### A.15.3:4 - Solution

#### A.15.3:4.0 - Planned slot-filling ontic

`A.15.3` governs the planned slot-filling ontic: a bounded planning relation in which one `U.WorkPlan.PlanItem` states which planned fillers are intended for which SlotKinds of one slot-bearing description before performed work occurs.

Keep three levels distinct:

- the planned slot-filling ontic: the E.24 ontic-level SlotRelation architecture for planned fillers of SlotKinds before performed work;
- `SlotFillingsPlanItem`: one filled `U.WorkPlan.PlanItem` value over that ontic for one bounded planning use;
- a card, table, view, schema, checklist, or document that publishes or projects a `SlotFillingsPlanItem` value.

By E.24 and E.24.UK, this is not an ontic without a kind settlement. The selected settlement reuses the root `U.WorkPlan` U-kind and admits `SlotFillingsPlanItem` as a dependent durable plan-item U-kind within `U.WorkPlan`; its filled instances are values inside a `U.WorkPlan`. The planned slot-filling ontic is the ontic-level SlotRelation that gives that dependent U-kind its identity and filler discipline. It does not introduce an independent root U-kind, a C.3 subkind claim, or a publication form. The stable identity is the planned-baseline relation among one work plan, one target slot-bearing description edition, one EntityOfConcern, one bounded context, one time selector or time rule when required, and one planned-filling row set. Changing the planned baseline before work creates a new PlanItem edition or a new PlanItem; performed-work variance does not rewrite the cited baseline.

The ontic keeps these objects distinct:

- `SlotFillingsPlanItem`: the dependent plan-item U-kind in this settlement; a filled value lives inside a `U.WorkPlan`, and the dependent U-kind does not introduce an independent root U-kind, the ontic-level SlotRelation itself, or a second slot ontology.
- `target_slot_bearing_description_ref`: the Description episteme whose SlotSpecs supply the SlotKinds being planned.
- `planned_fillings[]`: the row set that connects each selected SlotKind to a planned filler, filler mode, and edition pin when current.
- preparation refs: guard, evidence-reference, crossing-policy, time, context, or source-currentness refs that prepare later work without becoming evidence, a gate decision, or performed work.
- performed-work variance relation: the later `U.Work`, gate, evidence, result, archive, or variance relation that states what happened against the cited baseline.

Ontic-level `onticSlotRelation`:

| Slot group | Required or optional-in-use | Filler discipline |
| --- | --- | --- |
| Plan identity | Required | `plan_item_id`, `kind = SlotFillingsPlanItem`, `work_plan_ref`, and optional `plan_item_edition`; governed by `A.15.2` and this pattern. |
| Target slot-bearing description | Required | One Description episteme that exposes SlotSpecs; governed by the target description pattern and `A.6.5`. |
| EntityOfConcern, context, and time | Required for a conforming baseline | `entity_of_concern_ref`, `bounded_context_ref`, and `time_selector_ref` or `time_rule_ref` when reproducibility, currentness, or comparison depends on time. |
| Planned-filling rows | Required | Each row names a SlotKind from the target description, planned filler, ByValue or concrete RefKind mode, and edition pin when current; filler values keep their own governing patterns. |
| Preparation refs | Optional-in-use | Guard, readiness-preparation, evidence-reference, crossing-policy, source-currentness, bridge, or refresh refs; they prepare later relations but do not become `WorkEntryReadiness@Context`, gate decisions, evidence sufficiency, crossings, or performed work. |
| Derived projections | Optional-in-use | Cards, records, tables, views, indices, or summaries are E.17 publication or view-use projections; they are not the ontic and not row authority. |
| Variance policy | Required for reliance-bearing use | Names how later `U.Work`, gate, evidence, result, archive, or variance relations cite the baseline and record substitutions, missing fillers, extra fillers, launch values, or edition changes. |

A conforming instance fills only the slots that are current to the planning claim. Optional refs stay absent when the project does not rely on them. The open-world assumption is preserved: not writing an optional planned filler does not say that no such project value exists; it only says the current planned-baseline claim does not rely on it.

Use this ontic whenever a suite, kit, comparison, selector, archive, refresh, work-entry-readiness check, or P2W carry-through needs project-specific editions, policy ids, evidence-reference pins, bridge ids, method-description refs, or other planned fillers. Use the neighboring governing pattern when the current object is mechanism meaning, comparison result, selection result, work-entry readiness, performed work, evidence, gate passage, publication-use, source-currentness, or refresh.

This ontic is selected because dependent patterns need a shared settlement. Without it, suite, comparison, selector, archive, refresh, and P2W patterns would each invent a local baseline field, a local planned-pin phrase, or a local warning that planned values are not performed values. With this ontic, they cite `A.15.3` and keep their own EoC thin.

#### A.15.3:4.1 - Definition

`SlotFillingsPlanItem` is a kind of `U.WorkPlan.PlanItem` whose content is one planned slot-filling baseline for one slot-bearing description in one bounded context.

It is:

- produced inside work planning;
- tied to one target description episteme that supplies SlotSpecs;
- pinned enough to replay what was planned;
- cited later by performed `U.Work` when variance, substitutions, launch values, telemetry, or result records are written.

It is not:

- the target slot-bearing description;
- a `MechanismDefinitionRef`;
- a gate decision, evidence item, assurance result, publication truth, or performed-work occurrence;
- a second slot ontology beside A.6.5.

#### A.15.3:4.2 - Core fields

A conforming `SlotFillingsPlanItem` states these fields when the corresponding claim is current:

1. **Plan identity**
   - `plan_item_id`
   - `kind = SlotFillingsPlanItem`
   - `work_plan_ref`
   - optional `plan_item_edition`

2. **Target slot-bearing description**
   - `target_slot_bearing_description_ref`
   - The target is a Description episteme that declares SlotSpecs, such as a suite description, kit description, method-description family, or other description governed by its own pattern.
   - Do not target `MechanismDefinitionRef` directly. If a mechanism-level baseline is needed, introduce or cite a description that exposes the slots being planned.
   - When the target description's SlotSpecs are edition-sensitive, the target ref is edition-pinned.

3. **EntityOfConcern and context**
   - `entity_of_concern_ref`
   - `bounded_context_ref`
   - optional `grounding_holon_ref` when the EntityOfConcern is not itself a holon and the current comparison or reference-plane claim needs grounding;
   - optional `reference_plane_ref` only when the governing measurement, CHR, or comparison pattern defines that field.

4. **Time selector or time rule**
   - `time_selector_ref` or `time_rule_ref`
   - Use this when "current", "latest", reproducibility, comparability, launch preparation, or source-currentness matters.
   - When time is required, use exactly one of the two forms; both-present and both-absent baselines are nonconforming.

5. **Planning scope refs**
   - optional `cg_frame_ref`, `p2w_carry_through_ref`, `publication_scope_ref`, `suite_ref`, or `kit_ref` when those relations are current;
   - these refs locate the planned baseline, but they do not add planned rows by themselves.

6. **Guard-preparation refs**
   - optional expected guard or policy refs, such as compare-guard or launch-guard preparation refs;
   - these refs name what later work or gate checks should be prepared to use;
   - the PlanItem records preparation, not the guard result.

7. **Evidence-reference pins**
   - optional concrete pin refs naming where evidence is expected to be placed or cited later;
   - a pin ref is not evidence and does not create evidence sufficiency.

8. **Crossing-preparation refs**
   - optional refs for expected cross-context or cross-plane bridge or crossing relations, such as BridgeCard refs, policy-id refs, reference-plane refs, or already-published CrossingBundle baseline refs;
   - these refs state expected bridge or crossing relations only;
   - they are not crossing witnesses, do not embed CL/Phi/Psi tables, and do not claim that a crossing occurred.

9. **Authoritative planned-filling rows**
   - `planned_fillings[]`, each row with:
     - `row_id`;
     - `slot_kind`, taken from the target description's SlotSpecs;
     - `planned_filler`, written ByValue or ByRef with a concrete RefKind;
     - optional `edition_pin`;
     - optional `planning_note`.
   - If the target SlotSpec is single-valued, there is at most one row for that SlotKind.
   - If both a row and its referenced filler carry edition pins, they agree or the baseline is nonconforming.

10. **Derived projections**
   - optional cards, views, indices, or summaries;
   - each projection is derivable from `planned_fillings`;
   - any projection that adds rows, defaults, or semantics is a publication-use or view-use error under E.17.

11. **Variance policy**
   - how later performed `U.Work` cites this baseline;
   - how substitutions, missing fillers, extra fillers, launch values, or edition changes are recorded in the performed-work or gate relation.

#### A.15.3:4.3 - Compact record form

```text
SlotFillingsPlanItem:
  plan_item_id:
  kind: SlotFillingsPlanItem
  work_plan_ref:
  target_slot_bearing_description_ref:
  entity_of_concern_ref:
  bounded_context_ref:
  time_selector_ref or time_rule_ref:
  planning_scope_refs:
  guard_preparation_refs:
  evidence_reference_pins:
  crossing_preparation_refs:
  planned_fillings:
    - row_id:
      slot_kind:
      planned_filler:
      filler_mode: ByValue | ByRef(<ConcreteRefKind>)
      edition_pin:
      planning_note:
  derived_projection_refs:
  variance_policy:
```

#### A.15.3:4.4 - Relation to performed work

A `SlotFillingsPlanItem` is not a launch-value finalization witness and not a record that work occurred.

When a performed `U.Work` occurrence uses the baseline, the work record cites the PlanItem edition and records launch values, performed values, substitutions, missing planned fillers, extra fillers, telemetry, outcomes, and variance under A.15.1 or the governing gate, evidence, result, or archive pattern.

Do not backfill the plan to match what happened. If the plan changed before the work, create a new PlanItem edition or new PlanItem as appropriate. If the work differed from the plan, record variance in the performed-work relation.

#### A.15.3:4.5 - Relation to suites, kits, and mechanism introduction

A suite, kit, or mechanism-introduction pattern may require a planned-baseline ref. That requirement does not make the suite or mechanism text the baseline.

Use:

- the suite or kit pattern for the meaning of the suite or kit;
- A.6.5 for SlotSpec discipline inside the target description;
- A.15.3 for the plan instance that chooses planned fillers;
- A.15.1 for performed work and variance;
- `A.20` and `A.21`, `A.10` and `B.3`, or `E.17` when gate, evidence, assurance, or publication-use claims become current.

#### A.15.3:4.6 - Variants

Specialized PlanItem kinds are allowed only when the target governing pattern needs extra planned fields.

Example:

```text
CHRMechanismSuiteSlotFillingsPlanItem <: SlotFillingsPlanItem
  target_slot_bearing_description_ref = CHRMechanismSuiteDescriptionRef
  required_slots = {NormalizationMethodSlot, IndicatorPolicySlot, ComparatorSpecSlot}
```

The specialization may add fields needed by that suite, but it still inherits the WorkPlanning-only boundary: no performed-work actuals, no launch-value witnesses, no gate decisions, and no publication-view semantics.

#### A.15.3:4.7 - Local boundaries

| Source wording | A.15.3 recovery |
| --- | --- |
| "Use the latest spec" | Lower to a plan cue until time selector and edition-pinned target or filler refs are named. |
| "The mechanism uses this comparator" | Use the mechanism or suite pattern for mechanism meaning; use A.15.3 only if this is a planned filler for a plan instance. |
| "The card says the planned refs" | Use E.17 for the publication-use or view-use relation; the card is only a projection unless the PlanItem rows are present. |
| "The gate passed" | Use `A.20` and `A.21` or the gate pattern. The PlanItem can prepare refs for later gate use but does not pass the gate. |
| "Evidence pin" | Use A.15.3 only for the planned pin ref. Evidence-use and sufficiency are governed by `A.10`, `B.3`, `G.6`, or another governing evidence pattern. |
| "The work used different fillers" | Use A.15.1 for performed work and variance; do not rewrite the cited plan to erase the difference. |

### A.15.3:5 - Archetypal Grounding

#### A.15.3:5.1 - CHR suite planned baseline

**Tell.** A team plans characterization work over a CG-frame using a CHR mechanism suite. The suite description declares SlotKinds for normalization method, indicator policy, comparator spec, and selector policy.

**Show without A.15.3.** The plan says "use the latest CG-Spec and current best comparator." Later the comparator set changes. Later audit readers cannot tell whether the work used the intended comparator or a later one.

**Show with A.15.3.** The `SlotFillingsPlanItem` targets the CHR suite description edition, names the bounded context and time selector, and writes rows:

```text
planned_fillings:
  - slot_kind: NormalizationMethodSlot
    planned_filler: ByRef(UNMDescriptionRef:2026-06)
    edition_pin: 2026-06
  - slot_kind: ComparatorSpecSlot
    planned_filler: ByRef(ComparatorSpecRef:CG42-v3)
    edition_pin: v3
  - slot_kind: SelectorPolicySlot
    planned_filler: ByValue(SetReturningSelectionPolicy)
```

If the later work uses `ComparatorSpecRef:CG42-v4`, the work record states variance or crossing witness. The PlanItem remains the planned baseline.

#### A.15.3:5.2 - Archive and QD selection

**Tell.** A project plans to return an archive rather than one winner. Descriptor definitions and distance functions are edition-sensitive.

**Show without A.15.3.** The published archive card lists descriptors and distances, but the original planned descriptor edition is gone. The card becomes a mutable publication face rather than a planned-baseline relation.

**Show with A.15.3.** The PlanItem rows pin descriptor description refs, distance-definition refs, and time rule. The published card is a projection of those rows. If the archive generation later changes descriptors, performed work and result records cite the baseline and state the variance.

#### A.15.3:5.3 - Hardware acceptance fixture

**Tell.** A hardware team plans acceptance work for a fixture. The slot-bearing description is an acceptance-method description with slots for reference plane, measurement method, calibration source, and acceptance threshold.

**Show with A.15.3.** The planned baseline pins the reference-plane description, calibration source ref, and threshold edition. The performed acceptance work later records actual measurements and substitutions. The PlanItem does not become the measurement evidence.

### A.15.3:6 - Scope Declaration and Rationale

`SlotFillingsPlanItem` has a deliberate explicitness bias. It asks for target description, context, time, and planned rows because those are the smallest fields that keep planned slot filling separate from performed work and publication views.

The pattern does not try to make every work plan heavy. Ordinary plans stay in A.15.2. A.15.3 opens only when slot-filling choices themselves are the planned baseline that later work, gates, evidence, or publication projections will rely on.

The anti-bias guard is locality: if the current issue is mechanism meaning, work-entry readiness, evidence sufficiency, gate passage, source restoration, publication use, or performed work, use that governing pattern and bring only the returned planned-baseline relation back here.

### A.15.3:7 - Conformance Checklist

| ID | A conforming `SlotFillingsPlanItem`... | Check |
| --- | --- | --- |
| CC-A15.3-01 | is a `U.WorkPlan.PlanItem` with `kind = SlotFillingsPlanItem`. | It contains planned rows, not logs, actuals, or step logic. |
| CC-A15.3-02 | targets exactly one slot-bearing description. | `target_slot_bearing_description_ref` names a Description episteme with SlotSpecs; multiple targets use multiple PlanItems. |
| CC-A15.3-03 | keeps mechanism identity outside the PlanItem. | `MechanismDefinitionRef` is not the target unless a governing description wrapper exposes the planned slots. |
| CC-A15.3-04 | names EntityOfConcern and bounded context. | The baseline says what it is about and where the planned use is bounded. |
| CC-A15.3-05 | names a time selector or time rule when currentness, latest, reproducibility, or launch preparation matters. | No implicit "latest" controls a reliance-bearing baseline. |
| CC-A15.3-05a | uses exactly one time selector form when time is required. | Both-present and both-absent time baselines are nonconforming for reliance-bearing use. |
| CC-A15.3-06 | uses planned-filling rows as the authoritative row source. | Views, cards, and indices are derivable projections only. |
| CC-A15.3-07 | uses concrete RefKinds for ByRef fillers. | No generic `Ref`, generic `SpecRef`, or untyped placeholder carries the planned filler. |
| CC-A15.3-08 | preserves target SlotKind meaning. | The PlanItem chooses fillers; it does not redefine SlotKinds. |
| CC-A15.3-09 | keeps guard-preparation refs separate from gate results. | Later gate passage is recorded under the gate pattern. |
| CC-A15.3-10 | keeps evidence-reference pins separate from evidence-use. | Later evidence and assurance are governed by A.10, B.3, G.6, or the current evidence pattern. |
| CC-A15.3-11 | keeps crossing-preparation refs separate from crossing witnesses. | Crossing refs cite expected Bridge, policy, reference-plane, or published-baseline references only; they do not embed `CL`, `Phi`, or `Psi` tables or claim that a crossing occurred. |
| CC-A15.3-12 | keeps launch values and actuals out of the plan. | Performed work records launch values, substitutions, and variance. |
| CC-A15.3-13 | preserves cited baselines after work. | A changed plan becomes a new edition or new PlanItem; performed work records variance against the cited baseline. |
| CC-A15.3-14 | gives lowering and refresh conditions. | Missing target description, exposed SlotKind set, context, time, RefKind, edition pin, guard ref, evidence pin, crossing-policy ref, or variance relation lowers or reopens the claim. |
| CC-A15.3-15 | may be cited by `A.15.5` but does not decide readiness. | Readiness-preparation refs and planned fillers can be cited by `WorkEntryReadiness@Context`; the readiness relation is governed by `A.15.5`. |

### A.15.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Plan-as-execution | The plan contains launch values, witnesses, decision logs, or actual fillers. | Record actuals under performed `U.Work`, gate, evidence, or result records; leave planned rows in A.15.3. |
| Latest-as-baseline | "Latest" is used where replay needs a pinned edition or time rule. | Add time selector and edition pins, or lower to a plan cue. |
| View-as-baseline | A card, dashboard, or generated page becomes the row source. | Make the PlanItem rows authoritative and treat the view as E.17 projection. |
| Mechanism-prose baseline | Suite or mechanism prose hides plan-instance choices. | Put suite meaning in the suite pattern and planned fillers in A.15.3. |
| Generic ref placeholder | `SpecRef`, `PolicyRef`, or `GateRef` is used without concrete RefKind. | Use the concrete RefKind defined by the governing pattern, or block until one exists. |
| Backfilled plan | Performed work edits the plan after the fact so variance disappears. | Preserve the cited PlanItem; record variance, substitution, or crossing witness in performed work or the governing gate, evidence, result, or variance relation. |

### A.15.3:9 - Consequences

| Benefit | Cost and control |
| --- | --- |
| Planned choices become replayable. | More explicit planning fields; use the minimal record when reliance is low. |
| Performed-work variance becomes attributable. | Teams preserve cited baselines rather than editing history. |
| Suite and kit reuse becomes cleaner. | Specialized PlanItems may be needed, but only under the suite or kit governing pattern. |
| Publication views remain affordable. | Views can be generated, but they are projections, not the planned rows themselves. |
| P2W carry-through and work-entry readiness get a stable planned-baseline relation. | P2W and `A.15.5` still do not prescribe a project method, work plan, or performed work from the baseline alone; they only cite a recovered planned-baseline relation when current. |

### A.15.3:10 - Rationale

The pattern exists because planned slot fillings are neither generic plan text nor performed work. They are relation-bearing plan items: one target description supplies SlotKinds, the plan chooses fillers, and later work records what happened.

A.6.5 prevents a common type explosion. `slot_kind`, `planned_filler`, and RefKind fields are not new U-kinds. They are positions and fillers inside one relation-bearing PlanItem. E.17 prevents a second row source by keeping views and cards as projections. A.15.1 prevents plan backfilling by keeping performed-work actuals and variance outside the plan.

This split is especially useful in P2W and Part G work because many downstream records need the same planned baseline without copying suite semantics, mechanism definitions, gate decisions, evidence claims, or publication views into the plan.

### A.15.3:11 - SoTA-Echoing

| Current practice line | Adoption in A.15.3 | Rejected shortcut |
| --- | --- | --- |
| ISO/IEC/IEEE 12207:2017 and ISO/IEC/IEEE 15288:2023 keep life-cycle processes adaptable and distinguish process descriptions, planning, execution, and information items without prescribing one method or documentation form. | Adopt the process-information separation: A.15.3 is one planned-baseline information item inside work planning, not the work and not one universal process model. | Treating a process-tooling layout, stage model, or checklist as the FPF baseline ontology. |
| SLSA v1.2 provenance and in-toto Statement v1 separate build definition, run details, subjects, predicates, and resolved dependencies for software-supply-chain replay. | Use this only as an analogy for reproducibility and provenance separation: planned fillers and refs are recorded before work, while performed work, provenance, evidence, subject claims, and output claims remain separate FPF relations. | Importing supply-chain ontology as FPF ontology, or treating provenance, evidence, or an attestation record as the planned baseline itself. |
| Nix flakes and `flake.lock` practice show current dependency pinning: unlocked inputs are resolved to locked revisions and content hashes for reproducibility. | Adopt explicit pinning discipline for planned fillers, edition pins, and time rules when replay depends on them. | Saying "latest" or relying on a generated view when a bounded plan needs pinned planned rows. |
| Contemporary reproducible-build and supply-chain practice favors small attributable deltas and stable refs over mutable hidden defaults. | A.15.3 keeps planned rows stable, then lets performed work record variance, substitution, and crossing witnesses. | Editing the plan after execution so that no variance remains. |

### A.15.3:12 - Relations

- **Builds upon:** `A.15.2` for `U.WorkPlan` and PlanItem discipline; `A.15.1` for performed `U.Work`; `A.6.5` for SlotKind, ValueKind, RefKind, and SlotSpec discipline; `E.24` for ontic introduction and slot-relation discipline; `E.10.D2` for EntityOfConcern vs Description episteme vs specification-use; `E.17` for publication-use and view-use projection; `E.18.1` for P2W carry-through; `E.20` for mechanism-introduction boundaries.
- **Coordinates with:** `A.15.5` for work-entry readiness and full-kit preparation; `A.20` and `A.21` for gates and constraint decisions; `A.10`, `B.3`, and `G.6` for evidence, assurance, and provenance; `C.27.TA` and `G.11` for currentness and refresh; Part G patterns when planned baselines are used by kits, packs, or refresh plans.
- **Does not replace:** target description patterns, mechanism definitions, suite definitions, gate records, evidence relations, publication views, performed work, or source restoration.

### A.15.3:12a - P2W planned-baseline use relation

When `E.18.1` reaches a planned-baseline question, `SlotFillingsPlanItem` records the planned relation between one slot-bearing description's SlotKinds and the fillers intended for a future work-planning or work-entry-readiness use.

When `A.15.5` checks full-kit condition, it may cite `SlotFillingsPlanItem` for planned fillers, target description edition, required refs, and time selector. That citation does not make the planned baseline a readiness verdict; `A.15.5` states the readiness relation and any missing-input or degraded-use condition.

If the same source phrase also carries launch-value, performed-work, evidence, gate, result, measurement, publication-use, source-restoration, or refresh meaning, name that separate current relation before using the PlanItem downstream.

### A.15.3:12b - Planned-baseline to performed-work boundary

A performed `U.Work` occurrence may cite a `SlotFillingsPlanItem` as the planned baseline for slot fillers. The performed-work record states launch values, actual fillers, substitutions, variance, telemetry, and result-related records under A.15.1 and the current gate or evidence relation.

The work-planning record preserves what was intended. The performed-work record preserves what happened.

### A.15.3:12c - Lowering, repair, and refresh conditions

Lower a `SlotFillingsPlanItem` claim when the item cannot name exactly one target slot-bearing description, concrete SlotKinds from that description, EntityOfConcern, bounded context, time selector or time rule, authoritative planned-filling rows, concrete RefKinds for ByRef fillers, or required edition pins. The lowered result is a plan cue, source-gap note, relation governed by another FPF pattern, or blocked kind-definition gap.

Repair the PlanItem when a source-currentness change alters the target description edition, exposed SlotKind set, planned filler, concrete RefKind, edition pin, context, time rule, evidence-reference pin, guard-preparation ref, crossing-policy ref, or expected gate relation. If performed `U.Work` already cited the PlanItem as a baseline, preserve the cited baseline and record variance or crossing witness in the work-governed relation.

Refresh before the PlanItem is used for performed-work preparation, work-entry readiness, launch-guard preparation, cross-context comparison, suite or kit reuse, Part G universalization, publication-view projection, evidence-reference use, or P2W carry-through. Stop the refresh at the smallest changed relation: the PlanItem, target slot-bearing description, concrete RefKind, cited source edition, readiness relation, performed-work variance record, or related gate, evidence, bridge, or publication relation.

### A.15.3:End

