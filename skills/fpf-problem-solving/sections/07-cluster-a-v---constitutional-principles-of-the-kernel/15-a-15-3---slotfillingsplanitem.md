## A.15.3 - SlotFillingsPlanItem

> **Tech-name:** `SlotFillingsPlanItem`
> **Plain-name:** planned-filling plan item
> **Short code:** `SFPI`
> **Type:** WorkPlanning pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative
> **Placement:** Part A -> A.15 work family
> **Builds on:** `C.2.1` episteme identity, `A.15.2 U.WorkPlan`, `A.6.5` relation-declaration SlotSpec discipline, `A.6.1` operation declarations, and the direct pattern governing any other target declaration
> **Used by:** intended-work planning that must preserve exact desired participant, operation-argument, operation-result, or other explicitly governed declaration choices before performed work occurs
> **One-line purpose:** state a positive planned designation against one exact governed declaration member whose direct pattern owns the member's reusable participant, argument, or result meaning and corresponding later actual-use predicate; A.15.3 owns only the planning intention and makes nothing actual.

**At a glance.** Use `SlotFillingsPlanItem` when one exact `U.WorkPlan` must say that a future work use is intended to supply a particular value or designation under an exact declared participant, argument, or result meaning. The target's direct pattern owns that reusable meaning and its corresponding later actual-use predicate; A.15.2 and A.15.3 own the intended-use claim. A broad field name, compatible value kind, meaning-only declaration, method-description phrase, schema position, or plan label is not enough.

**Use this when.** Use this pattern when intended work depends on a planned participant designation for one `RelationSignature` SlotSpec, a planned value or designation for one A.6.1 `ArgumentDeclaration` or `ResultDeclaration`, or a planned filling for another exact declaration member whose direct pattern explicitly owns the member's reusable meaning and corresponding later actual-use predicate. The item preserves what was intended; it establishes no dated work, actual relation participant, operation application, returned value, change, result, delivery, or outcome.

**First useful object.** One `PlanItem` content component inside an exact `U.WorkPlan`, containing at least one planned-filling row whose intended-performance designator, target declaration edition, declaration-local member designator, direct owner of the member meaning and corresponding actual-use predicate, planned value or designation, effective designation rule, semantic cardinality, and planning conditions are recoverable.

**Working use order.**

1. Identify the exact `U.WorkPlan` edition, its already identified present EntityOfConcern, and the intended-performance designator under A.15.2.
2. For each planned filling, recover one exact declaration member and the direct pattern that owns the member's reusable participant, argument, or result meaning and corresponding later actual-use predicate.
3. Point to one exact declaration edition and one declaration-local member designator; do not point to a description or record merely because it displays an input, output, role, field, or slot.
4. State the positive planned value or designation under that member's declared ValueKind, designation rule, semantic cardinality, and exact planning conditions. Keep exclusions, prohibitions, and completeness claims as separately governed plan claims.
5. At later use, identify any dated work and every actual participant or binding independently under their direct patterns. Compare actual and planned claims without rewriting the plan.

**Ordinary use.** One row with an exact declaration reference, exact member designator, exact direct owner of the member meaning and corresponding actual-use predicate, positive planned value or designation, and the condition under which it is intended is enough.

**Reliance-bearing use.** Add declaration-edition pins, value-edition pins when the value is edition-bearing, concrete reference kinds, target-declared cardinality or alternative-selection conditions, and an exact later comparison policy only when coordination, replay, audit, or work-entry preparation depends on them.

**Stop condition.** Stop when every relied-on row resolves to one exact governed declaration member whose direct pattern owns the member's reusable meaning and corresponding later actual-use predicate, while A.15.3 supplies only the intended-use claim. If no reusable declaration member is needed, retain the choice as ordinary A.15.2 plan content. If a planned filling is needed but the declaration member, reusable meaning, corresponding actual-use predicate, or their direct owner is missing, record the exact missing-governor blocker; do not manufacture a SlotSpec, description wrapper, generic field declaration, or actual-use relation in this pattern.

**What goes wrong if missed.** A plan silently turns method prose or a schema field into a slot, treats type compatibility as planned or actual participation, treats omission or an empty filler as a prohibition, or later edits the baseline to match what happened.

**What this buys.** A compact, replayable account of what exact declaration use was intended, while declaration semantics, plan content, dated work, and actual participation remain independently recoverable.

**Not this pattern when.** Not this pattern when the current object is the declaration itself (`A.6.5`, `A.6.1`, or its direct pattern), an ordinary intended-work claim with no planned filling (`A.15.2`), dated performed work (`A.15.1`), an actual relation participant or operation-application binding, a method or method description (`A.3.1` or `A.3.2`), evidence or assurance (`A.10` or `B.3`), a gate or acceptance verdict, a result episteme, publication use, or a representation field.

### A.15.3:1 - Context

A work plan may need more precision than “use this method” or “perform this task.” It may need to preserve that a particular future relation use is intended to designate `Bearing_C` under `PartHolonSlot`, or that a particular future operation application is intended to bind `Pump_37` under `candidateArgument`.

The declaration already owns the participant, argument, or result meaning. The WorkPlan owns the intention. A.15.3 joins them only as plan content. It neither changes the declaration nor makes the planned value participate.

### A.15.3:2 - Problem

Without this boundary, five failures recur:

1. **Generic slot creation.** Any description field named input, output, role, result, or parameter is treated as a SlotSpec.
2. **Declaration-family collapse.** RelationSignature SlotSpecs and operation arguments or results are placed in one undifferentiated slot schema.
3. **Plan-as-actual inference.** A planned value is treated as an obtaining relation participant or actual operation binding.
4. **Description-as-declaration inference.** A `U.MethodDescription` that mentions an input or effect is treated as if it declared a reusable participant locus.
5. **Baseline rewrite.** Performed values are copied back into the plan, erasing substitution and variance.

### A.15.3:3 - Forces

| Force | Demand |
| --- | --- |
| Planning usefulness | Preserve the exact value or designation intended for later work. |
| Declaration locality | Interpret every target member only inside its exact declaration edition and direct owner. |
| Family separation | Keep RelationSignature participants distinct from A.6.1 operation arguments and results. |
| Intention versus actuality | Permit useful planned claims without asserting work or participation. |
| Replay versus burden | Pin only the editions and conditions on which the receiving planning use relies. |

### A.15.3:4 - Solution

#### A.15.3:4.0 - The governed object and ontic boundary

`SlotFillingsPlanItem` names a declaration-local `PlanItem` content form inside one exact `U.WorkPlan` ClaimGraph. It is not a U-kind, a dependent durable kind, a `U.Relation` occurrence, an ontic `SlotRelation`, an independent record, or a second slot ontology. Its item and row designators are interpreted only within that WorkPlan edition.

C.2.1 and A.15.2 keep the WorkPlan episteme identity. Changing an identity-bearing planned-filling row changes the WorkPlan ClaimGraph and lets C.2.1 identify the resulting episteme edition. A separate reference may resolve the WorkPlan and the designated content component, but the reference does not give the PlanItem an independent identity rule.

Here a **planned-filling claim** is WorkPlan claim content saying that, for one intended-performance designator and under exact planning conditions, a future use of one exact declaration member is intended to carry or designate one exact value or target-declared collection of values. A.15.2 and A.15.3 govern that positive intended-use claim. The declaration member's direct pattern separately owns its reusable participant, argument, or result meaning and the corresponding later actual-use predicate. Neither owner substitutes for the other.

The phrase **planned filling** does not mean that a declaration is filled, a relation obtains, an operation application occurs, or a value is actually bound. The row itself needs no relation kind or relation occurrence: A.15.3 is the direct pattern for this plan-content form. A later fulfilment, substitution, missing-filler, or variance claim remains a neighboring claim under A.15.2, A.6.RCD, or another exact comparison owner.

A planned-filling row is positive intention content. A prohibition, excluded value, required absence, or closed-world completeness claim needs its own exact constraint or negative-claim governor and cannot be encoded by omission, an empty filler, or a negated reference.

#### A.15.3:4.1 - Admit only exact governed declaration targets

Each planned-filling row targets exactly one member of one exact applicable declaration edition:

| Planned meaning | Exact target | Direct owner and boundary |
| --- | --- | --- |
| participant designation for a future direct-relation claim | one `SlotSpec` in one exact `RelationSignature` edition | the direct relation pattern owns the reusable participant meaning and obtaining predicate; A.6.5 owns the declaration-local `SlotKind`, `ValueKind`, and `refMode`; A.15.3 owns only the intended designation |
| argument value or designation for a future operation application | one `ArgumentDeclaration` in one exact A.6.1 `OperationDeclaration` | A.6.1 and the exact mechanism declaration own argument meaning, ValueKind, binding designation rule, binding predicate, and cardinality; A.15.3 owns only the intended value or designation |
| expected result value or designation for a future operation application | one `ResultDeclaration` in one exact A.6.1 `OperationDeclaration` | A.6.1 and the exact mechanism declaration own result meaning and the actual result-binding predicate; an expected value is not a returned value |
| another explicitly declared planned filling | one exact declaration member whose direct pattern owns its reusable participant, argument, result, or analogous member meaning and corresponding later actual-use predicate | cite that pattern and declaration by value; if either the reusable meaning or corresponding predicate lacks that owner, stop with the exact missing-governor blocker |

`U.MethodDescription` is not an admissible target merely because its claims describe generic inputs, effects, parameters, bounds, or acceptance conditions. A suite description, kit description, table, schema, card, checklist, interface form, or database field likewise exposes no A.6.5 SlotSpec unless one exact `RelationSignature` contains that SlotSpec. Operation arguments and results remain A.6.1 declaration content and never become A.6.5 SlotSpecs by being planned.

One `SlotFillingsPlanItem` may contain several rows when they serve the same intended-performance designator, baseline policy, and revision route inside one WorkPlan. Every row still resolves independently to its exact declaration member. Split the item when rows concern different intended performances, baseline policies, or revision routes. The WorkPlan's present EntityOfConcern remains a WorkPlan-level C.2.1 discriminator and is not replaced by the merely possible performance designator.

#### A.15.3:4.2 - State one planned-filling row

A conforming item makes these values recoverable:

```text
SlotFillingsPlanItem:
  planItemDesignator
  exactWorkPlanRef
  intendedPerformanceDesignator
  plannedFillingRows:
    - rowDesignator
      targetDeclarationRef
      targetMemberDesignator
      targetMemberFamily:
        RelationSignatureSlotSpec |
        OperationArgumentDeclaration |
        OperationResultDeclaration |
        OtherDirectlyGovernedDeclaration
      directOwnerPattern
      plannedValueOrDesignation
      planningConditions?
      declarationEditionPin?
      plannedValueEditionPin?
  baselinePolicyRef?
  laterComparisonPolicyRef?
```

The block is a representation of WorkPlan claim content, not an ontic record schema or a second row authority. `targetMemberFamily` is an open local dispatch vocabulary, not a public kind or a closed inventory. `directOwnerPattern` names by value the subject pattern that owns the target member's reusable meaning and corresponding actual-use predicate; it is not a generic reference kind. A.15.3 remains the owner of the planned intention.

The effective designation rule is resolved from the exact target member rather than copied into a competing plan-side declaration. For an A.6.5 target this is its `refMode`; for an A.6.1 target it is the `bindingDesignationRule`. A ByRef designation uses the concrete governed reference kind required there and resolves to a referent of the declared ValueKind; a generic `Ref`, `SpecRef`, stored token, or compatible value does not suffice.

The target member's semantic cardinality governs the planned choice. For a single-valued target, the exact baseline or selection policy must make at most one planned value or designation effective for any one intended use. Several alternatives require exact conditions and an exact resolution rule; layout supplies neither exclusivity nor priority. A multivalued member follows the target-declared set, sequence, multiset, repetition, and ordering semantics; row count or row order supplies none of them. If the target declaration and applicable policy do not settle the cardinality needed by the planned use, return the missing declaration or policy governor instead of inferring it from layout.

Omitting a possible row is not a negative claim that no such value, designation, or later participant exists. It means only that the current WorkPlan ClaimGraph does not rely on that filling. A prohibited or excluded value and any closed-world completeness claim remain separate governed plan claims with their own applicability and polarity basis.

`intendedPerformanceDesignator` is plan content, not a reference that makes a future Work occurrence or another future entity exist. The already identified present EntityOfConcern stays on the enclosing WorkPlan under C.2.1 and A.15.2.

Time, location, capability, readiness, gate, evidence, source-currentness, bridge, publication, or other conditions enter only through exact separately governed plan claims when the receiving use depends on them. This is an open recognition palette of neighboring claim families, not an unnamed kind or a generic field bundle. `planningConditions` cites those claims; it does not create them.

Any baseline or later-comparison policy reference states its concrete governed kind, direct owner, effective edition, applicability, and reference scheme when relied upon. A generic `PolicyRef` or shared label supplies no policy semantics. Pin a declaration edition or edition-bearing planned value only when another resolution could change the meaning relied on by the receiving use; the exact target reference and any explicit pin must agree.

#### A.15.3:4.3 - Read relation-declaration rows

For a RelationSignature row:

1. resolve the exact direct relation pattern and its corresponding obtaining predicate;
2. resolve the exact `RelationSignature` edition;
3. resolve the exact SlotSpec and its declaration-local `SlotKind`;
4. check the planned value or designation against the SlotSpec's `ValueKind` and `refMode`;
5. apply the exact semantic cardinality and participant constraints supplied by the direct relation pattern and declaration; and
6. retain the row as positive plan content.

The row does not fill the SlotSpec. The SlotSpec remains reusable declaration content. The planned designation does not become the actual participant, and the direct relation does not obtain until its direct predicate is satisfied for independently identified participants.

#### A.15.3:4.4 - Read operation-declaration rows

For an A.6.1 row, resolve the exact mechanism edition, `operationDesignator`, and `argumentDesignator` or `resultDesignator`. Apply that declaration's ValueKind, `bindingDesignationRule`, binding predicate, semantic cardinality, and planned conditions.

The row is not an operation application or operation-application binding. An actual argument binding requires one exact application occurrence and satisfaction of the declared argument binding predicate. An actual result binding requires that application to return the exact value under the declared result meaning. Type compatibility, an expected result, a method-description phrase, a ticket value, or a matching token establishes neither binding.

#### A.15.3:4.5 - Keep plan, work, and actual use separate

At later use, identify exact `W : U.Work` under A.15.1 only when dated performed work is actually current. Whether or not Work is part of the case, establish every actual relation participant through its obtaining direct predicate and every operation argument or result through the exact A.6.1 application-binding predicate. Work, WorkPlan, PlanItem, matching label, declaration compatibility, and shared value establish none of those actual facts by themselves.

A neighboring comparison claim may compare the planned row with the independently governed actual participant or binding under an exact comparison policy. One case may stop at A.6.RCD disposition 2's local compound assertion over the cited plan edition, exact actual-use facts, and substrate-admitted policy. Repeated parameterized semantics may stop at disposition 3's predicate-definition episteme. Only a named occurrence-facing need can open relation-kind admission; the comparison never enters the WorkPlan's identity-bearing content or creates a universal planned-to-actual relation.

Unplanned actual participation remains actual when its own predicate obtains. Conversely, a claim that a planned value was missing, excluded, or substituted needs the comparison policy's applicable closure or negative criterion plus exact case facts. An absent log, unresolved reference, or unavailable fact is `missing-information`, not a negative actual-use or variance result; absent authority is `missing-governor`.

#### A.15.3:4.6 - Revision and replay

Pin a declaration edition or edition-bearing planned value only when a different resolution could change the meaning relied on by the receiving use. “Latest,” a mutable alias, a publication face, or an untyped policy label is not a reproducible declaration, value, or policy reference.

If a declaration member changes before the planned use, revise the WorkPlan claim content and let C.2.1 identify the resulting edition. If work or another actual use has already relied on the prior plan edition, preserve that cited edition and state any substitution or variance in a neighboring governed claim. A changed representation or carrier alone does not revise the plan when the C.2.1 discriminators remain fixed.

A card, table, view, index, or generated summary may project selected WorkPlan claim content under its publication-use governor. It is not a second row authority and may not add planned fillings, defaults, declaration meanings, cardinality, conditions, or baseline semantics.

### A.15.3:5 - Archetypal Grounding

#### A.15.3:5.1 - Planned participant designation against a RelationSignature

A maintenance WorkPlan carries the planning claim that replacement bearing `Bearing_C` is intended to participate as the part in a future part-whole claim about `Pump_P`. Its positive planned-filling rows target `PartHolonSlot` and `WholeHolonSlot` in one exact part-relation `RelationSignature` edition and carry `Bearing_C_Ref` and `Pump_P_Ref` under their declared RefKinds.

Before installation, those rows assert neither `Bearing_C isPartOf Pump_P` nor an actual participant pair. After the exact relation predicate obtains, a separate affirmative assertion may designate the actual participants under those SlotSpecs. The plan remains the intended baseline.

#### A.15.3:5.2 - Planned argument and expected result against A.6.1

A classification-work plan carries the claim that one exact recognition-evaluation operation is intended to assess `Pump_37`. One row targets its `candidateArgument` declaration and plans `Pump_37_Ref`; another targets its `judgmentResult` declaration and states expected value `true` under the local `RecognitionJudgmentValue` kind.

Neither row identifies an evaluation application, binds Pump #37, returns `true`, proves the candidate-side criterion, creates an evaluation-result episteme, or makes evidence sufficient. Those claims remain with A.6.1, A.1, C.2.1, and the exact evidence or assurance patterns when their predicates are current.

#### A.15.3:5.3 - Hardware-acceptance pseudo-slots rejected

An acceptance-method description says to use a calibrated instrument, a selected reference plane, a calibration record or certificate, and a threshold. That prose describes one method but exposes no A.6.5 SlotSpecs. The planner may cite the method description, selected plane, calibration or evidence-reference claim, and threshold as separately governed ordinary plan content under A.15.2.

A.15.3 opens only if an exact A.6.1 operation declaration, RelationSignature SlotSpec, or other exact governed declaration member has one direct pattern that owns the member's reusable meaning and corresponding later actual-use predicate. Otherwise return the exact missing-governor blocker for typed reuse; do not wrap the method description or fixture card in a fictitious slot-bearing description. Later measurement, evidence sufficiency, readiness, acceptance, and actual instrument use remain with their direct owners.

#### A.15.3:5.4 - Edition-sensitive selector or archive planning

A selector or archive plan may need to preserve intended comparator, descriptor-definition, distance-definition, evidence-policy, or other edition-sensitive choices. A suite description, archive card, or generated view does not make those labels planned-filling targets.

If one exact applicable declaration edition exposes a corresponding A.6.1 argument or result declaration, RelationSignature SlotSpec, or other directly governed member with its actual-use predicate and cardinality, the WorkPlan may use one A.15.3 row per target member and pin only the relied-on editions. Otherwise the choices remain ordinary A.15.2 plan claims, or typed reuse returns the exact missing-governor blocker. The later operation application, dated Work, selected set or archive result, evidence-provenance path, publication, and any variance claim remain independent; a card is only a read-only projection of selected plan content.

### A.15.3:6 - Scope Declaration and Rationale

**Scope.** A.15.3 governs only positive planned designation against exact declaration members inside one WorkPlan. It does not govern declaration admission, prohibitions or negative constraints, work identity, actual participation, operation application, later comparison, evidence, readiness, gates, results, production, delivery, acceptance, publication, or downstream effects.

**Rationale.** The pattern gives practitioners a reusable planned-baseline move without admitting another U-kind or universal slot relation. Dispatching each row to its declaration family preserves both practical replay and ontological locality.

### A.15.3:7 - Conformance Checklist

| ID | Requirement | Practical test |
| --- | --- | --- |
| CC-A15.3-01 | The item is declaration-local WorkPlan content, not a U-kind, record, or relation occurrence. | Its designator resolves inside one exact WorkPlan edition; no independent PlanItem identity rule or row authority is claimed. |
| CC-A15.3-02 | The enclosing WorkPlan retains one already identified present EntityOfConcern, while the item names an intended-performance designator. | No possible future performance is treated as an existing entity, reference target, or dated Work merely because it is planned. |
| CC-A15.3-03 | Every row targets one exact declaration edition and member with one direct owner of the reusable member meaning and corresponding actual-use predicate. | Declaration ref, member designator, family, direct-owner pattern, and predicate route are recoverable; A.15.3 owns only the intended-use claim. |
| CC-A15.3-04 | Relation-participant rows target only A.6.5 SlotSpecs inside exact RelationSignatures. | A method description, schema field, plan field, or operation argument is never called a SlotSpec. |
| CC-A15.3-05 | Operation rows target exact A.6.1 ArgumentDeclarations or ResultDeclarations. | Mechanism edition, operation designator, member designator, binding rule, predicate, and cardinality resolve together. |
| CC-A15.3-06 | Any other target has an explicit direct declaration owner. | Missing reusable meaning, corresponding actual-use predicate, or owner yields a blocker rather than a generic target. |
| CC-A15.3-07 | Planned value or designation follows the target member's ValueKind, designation rule, and semantic cardinality. | For a single-valued target, exact conditions and a resolution rule make at most one planned value effective; multivalued and ordering semantics come only from the target declaration, not row count or layout. |
| CC-A15.3-08 | The row is a positive intended-use claim. | Omission is open-world; prohibition, exclusion, required absence, and completeness are separate governed plan claims rather than empty or negated fillers. |
| CC-A15.3-09 | Planned filling remains planned. | No row establishes dated work, direct-relation obtaining, operation application, argument binding, returned result, change, production, delivery, acceptance, or outcome. |
| CC-A15.3-10 | Plan revision follows C.2.1 WorkPlan identity. | Changing identity-bearing row content identifies the resulting plan episteme edition; no standalone PlanItem edition ontology is invented. |
| CC-A15.3-11 | Later actual facts keep direct governors. | Work, relation participants, and A.6.1 bindings are independently identified rather than inferred from a plan row. |
| CC-A15.3-12 | Later comparison preserves the cited baseline and truthful polarity. | Substitution or variance is a neighboring governed claim; missing-filler or negative results require an applicable closure or negative criterion rather than absent records. |
| CC-A15.3-13 | Edition, reference, and policy pins are use-driven and concrete. | No implicit “latest,” generic RefKind, generic PolicyRef, publication face, or incompatible duplicate pin controls a reliance-bearing row. |
| CC-A15.3-14 | Conditions and projections stop at their direct owners. | Time, location, readiness, evidence, gate, bridge, publication, and comparison claims are cited rather than absorbed; cards and views add no rows or semantics. |

### A.15.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Generic slot-bearing description | Any description with fields becomes a reusable declaration. | Resolve one exact RelationSignature SlotSpec, A.6.1 argument/result declaration, or other directly governed declaration member. |
| Dependent PlanItem U-kind | A ClaimGraph component receives a rival identity and ontic settlement. | Keep `SlotFillingsPlanItem` as declaration-local WorkPlan content. |
| Planned SlotRelation | The plan claim is reified as an obtaining world-side relation. | Keep planned filling as positive claim content; open an actual relation only under its direct predicate. |
| Planned-meaning owner blur | The target's direct pattern is said to own the planning intention. | Let the target owner govern reusable member meaning and corresponding actual-use predicate; let A.15.2/A.15.3 govern intended-use content. |
| Method-description slot | Generic method semantics are mistaken for declaration members. | Cite the method description as ordinary plan content or return a missing declaration governor for typed reuse. |
| Relation/operation collapse | A.6.1 arguments and results are written as A.6.5 SlotSpecs. | Dispatch by target family and keep each declaration vocabulary local. |
| Row-count cardinality | Repeated rows or their order silently define multiplicity, alternatives, or sequence. | Apply the target declaration's semantic cardinality and an exact policy whose conditions and resolution rule determine the effective planned value. |
| Empty filler as prohibition | Omission, null, or a negated reference is treated as “must not use.” | State prohibition, exclusion, required absence, or completeness as a separate governed plan claim. |
| Plan-as-actual | A planned value is treated as actual participation or a returned result. | Identify work and actual relation or application bindings independently. |
| Generic reference or policy | `Ref`, `SpecRef`, `PolicyRef`, or a shared label is treated as sufficient. | Use the concrete governed RefKind and exact policy kind, owner, edition, applicability, and reference scheme. |
| Latest-as-baseline | A mutable label stands for the declaration or value edition. | Pin the exact edition when the receiving use depends on it. |
| Backfilled plan | Actual values replace planned rows after work. | Preserve the cited plan edition and state a neighboring substitution or variance claim. |

### A.15.3:9 - Consequences

| Benefit | Cost and control |
| --- | --- |
| Planned choices remain replayable. | Each relied-on row needs an exact declaration owner and member designator. |
| Declaration families remain coherent. | Planners must dispatch relation participants and operation values separately. |
| Actual-use claims remain honest. | A matching plan row cannot substitute for grounding the Work occurrence and the independently obtaining relations involving it. |
| Missing ontology becomes visible. | An unowned filling returns a precise blocker instead of a convenient generic slot. |

### A.15.3:10 - Rationale

Planning needs a way to preserve intended values without turning every planning field into ontology. RelationSignature SlotSpecs, A.6.1 operation declarations, and other direct declarations already supply reusable member meanings and corresponding later actual-use predicates. A.15.3 contributes only the positive intended use of those members in one WorkPlan.

This split preserves four authorities and identities: the target direct pattern owns the reusable member meaning and actual-use predicate; A.6.5 or A.6.1 owns the relevant declaration discipline; the WorkPlan remains one C.2.1 episteme whose A.15.2/A.15.3 claim content states the intention; and any later Work, application binding, relation occurrence, result, or comparison is independently identified. A row reference connects those objects for planning but constitutes none of them.

### A.15.3:11 - SoTA-Echoing

| Current practice line | Adoption in A.15.3 | Rejected shortcut |
| --- | --- | --- |
| ISO/IEC/IEEE 12207:2017 and ISO/IEC/IEEE 15288:2023 distinguish process descriptions, planning, execution, and information items while allowing local life-cycle adaptation. | Preserve the declaration, intended-use plan content, and performed work as separate governed objects. | Treating a process-tooling layout or checklist field as an FPF declaration. |
| SLSA v1.2 provenance and in-toto Statement v1 separate build definition, run details, subjects, predicates, and resolved dependencies. | Use exact planned declaration and edition references when replay depends on them; keep run, provenance, result, and evidence claims separate. | Importing a supply-chain record schema as a universal slot or result ontology. |
| Nix flake-lock practice makes selected dependency revisions explicit for reproducibility. | Pin declaration or value editions only when a mutable resolution would change the relied-on planned meaning. | Saying “latest” when later comparison needs one exact edition. |

### A.15.3:12 - Relations

- **Builds upon:** C.2.1 and A.15.2 for WorkPlan identity, present EntityOfConcern, intended-performance designators, and intended-work content; A.6.5 for SlotSpecs inside exact RelationSignatures; A.6.1 for operation argument and result declarations; and the direct pattern governing any other admissible target declaration.
- **Coordinates with:** A.15.1 for dated Work; direct relation patterns for actual participation; A.6.1 for actual operation applications and bindings; A.6.RCD for later local fulfilment or variance claims when no current direct comparison relation closes the use; A.15.5 for work-entry readiness; and exact evidence, gate, evaluation, result, production, delivery, acceptance, publication, and currentness patterns only when those claims become current.
- **Does not replace:** a declaration, method or method description, WorkPlan, dated Work, actual participant or binding, constraint or negative plan claim, comparison result, result episteme, evidence, gate, production, or publication object.

### A.15.3:12a - P2W planned-filling use

When P2W reaches intended work and one planned value depends on a reusable declaration admissible under A.15.3:4.1, carry the exact WorkPlan, intended-performance designator, target declaration edition, declaration member, direct owner, positive planned value or designation, and relied-on conditions or pins. The declaration's direct pattern must own the member's reusable meaning and corresponding later actual-use predicate; A.15.2 and A.15.3 own the intended-use claim. P2W defines neither the declaration nor the plan claim and turns no row into an actual participant or application binding.

If no reusable member is needed, carry ordinary A.15.2 plan content. If typed planned use is needed but the declaration member, reusable meaning, corresponding actual-use predicate, or direct owner is absent, carry the exact missing-governor blocker. If the source wording also carries performed-work, readiness, evidence, gate, result, measurement, publication, refresh, delivery, acceptance, exclusion, or completeness meaning, recover each separately under its direct governor.

### A.15.3:12b - Lowering, repair, and refresh conditions

Lower the claim to ordinary A.15.2 plan content when no reusable declaration member is needed. Block the typed planned filling when the intended-performance designator, participant, argument, result, declaration edition, member designator, effective designation rule, semantic cardinality, corresponding later actual-use predicate, or direct pattern owning the reusable member meaning and predicate cannot be recovered. The acceptable return names the missing governor and intended future use; it is not a generic slot-bearing description.

Route a prohibition, exclusion, required absence, or completeness claim to its exact plan-constraint or negative-claim owner rather than encoding it as omission or an empty filler. Route any later missing-filler, substitution, or variance result to an exact comparison policy and require its applicable closure or negative criterion plus case facts.

Repair the exact WorkPlan ClaimGraph when a planned target member, positive planned value or designation, intended-performance designator, planning condition, or relied-on edition changes. Preserve any edition already cited by performed work or another actual use. Refresh only the exact declaration, reference resolution, policy, or plan edition on which the receiving use relies, and route any actual-use change to its direct relation or A.6.1 owner.

### A.15.3:End

