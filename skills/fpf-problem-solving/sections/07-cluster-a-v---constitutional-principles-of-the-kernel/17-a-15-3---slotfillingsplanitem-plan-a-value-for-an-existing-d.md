## A.15.3 - `SlotFillingsPlanItem`: Plan a Value for an Existing Declaration Member

> **Tech-name:** `SlotFillingsPlanItem`
> **Plain-name:** planned-filling plan item
> **Short code:** `SFPI`
> **Type:** WorkPlanning pattern
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

> **Builds on:** `C.2.1` episteme identity, `A.15.2 U.WorkPlan`, `A.6.5` relation-declaration SlotSpec discipline, `A.6.1` operation declarations, and the pattern that defines any other target member
> **Used by:** plans that must remember a chosen future relation participant, operation argument, expected result, or another value tied to an already declared member before work begins


**At a glance.** Use `SlotFillingsPlanItem` when a plan must preserve a concrete choice before Work begins—for example, `Robot_8_Ref` as the planned holder for a future system-role assignment, with the assignment species named separately, or `Pump_37_Ref` as the planned `candidate` in a recognition operation. Point to the declaration member that already defines that position, and record the planned value and conditions. When a later question asks whether the choice was used, compare the established actual facts with the preserved plan. A field name, compatible type, Method phrase, form position, or plan label is not such a declaration.

**Use this when.** Use this pattern only when the choice points to a member already defined in a `RelationSignature`, an A.6.1 `OperationDeclaration`, or another declaration whose own pattern states both the member's meaning and the rule for its later actual use. If the plan merely says *use this method*, *reserve this resource*, or *meet this threshold* without reusing such a member, keep ordinary A.15.2 plan content.

**First useful object.** One `PlanItem` inside an identified `U.WorkPlan` with at least one row that names the intended future use, declaration episteme, declaration-local member, planned value or designation, and the conditions under which that choice applies. The row follows the member's designation rule and semantic cardinality; it does not redefine either.

**Working use order.**

1. Identify the `U.WorkPlan` episteme and the future performance being planned. Keep the WorkPlan's already identified present EntityOfConcern unchanged.
2. Open the declaration that will be used later and choose one member it actually defines. Verify that the declaration's own pattern states both what that member means and what must hold for actual use.
3. Record the declaration episteme, its local member designator, and the planned value or designation. Do not substitute a description, record, form field, or matching label.
4. Apply the member's ValueKind, designation rule, and semantic cardinality. Add conditions and edition pins only when they can change which planned value is effective. State prohibitions, exclusions, and completeness as separate plan claims; omission is not prohibition.
5. When a later question requires comparison, establish each claimed relation participant or operation binding independently. Identify a dated Work under A.15.1 only when that occurrence claim is needed. Compare actual with planned under the applicable policy, preserving the plan as the baseline.

**Ordinary use.** One row is enough: declaration episteme, member designator, planned value or designation, and the condition under which it is intended. The declaration's own pattern must already define the member and its later actual-use rule.

**Reliance-bearing use.** Add concrete reference kinds, declaration or value episteme pins, alternative-selection conditions, target-declared cardinality, and a later comparison policy only when coordination, replay, audit, or work-entry preparation would change without them.

**Stop condition.** Finish with one of these results. (1) The row resolves to an existing declaration member, and the planned value meets its ValueKind, designation, cardinality, and condition rules. (2) No reusable member is needed, so the choice stays ordinary A.15.2 plan content. (3) Typed reuse is needed but the member, its meaning, its actual-use rule, or the pattern that defines them is missing; return `missing-governor` for that planned use. (4) Required planning information is missing or unresolved; name what must be recovered (§12b). Do not invent a SlotSpec, wrapper declaration, generic field, or actual-use relation here.

**What goes wrong if missed.** A plan silently turns method prose or a schema field into a slot, treats type compatibility as planned or actual participation, treats omission or an empty filler as a prohibition, or later edits the baseline to match what happened.

**What this buys.** The team can later say what it intended, what actually happened, and whether the two differ, while the declaration, plan, work, and actual participation remain separate objects.

**Not this pattern when.** Use the exact declaration predicate and ClaimGraph located through `A.6.5`, `A.6.1`, or another declared-member source when defining the member; use A.15.2 for ordinary intended work without a planned filling; use A.15.1 for dated work; and use the exact applicable predicates for actual relation participation, operation bindings, methods, evidence, assurance, gates, acceptance, results, publication, or representation.

### A.15.3:1 - Context

A WorkPlan may need more precision than *use this Method* or *perform this task*. An inspection plan may propose `Robot_8_Ref` for `HolderSystemSlot` in `InspectionRobotSystemRoleAssignmentSignature`; §5.1 shows the declaration needed for that typed choice. A recognition plan may need to remember that `Pump_37_Ref` is intended for the declaration-local `candidate` argument.

The declaration already states the participant, argument, or result meaning. The WorkPlan states the intention. A.15.3 joins them only as plan content.

### A.15.3:2 - Problem

The following five failures motivate this boundary:

1. **Generic slot creation.** Any description field named input, output, role, result, or parameter is treated as a SlotSpec.
2. **Declaration-family collapse.** RelationSignature SlotSpecs and operation arguments or results are placed in one undifferentiated slot schema.
3. **Plan-as-actual inference.** A planned value is treated as a participant in an obtaining relation or an actual operation binding.
4. **Description-as-declaration inference.** A `U.MethodDescription` that mentions an input or effect is treated as if it declared a reusable participant locus.
5. **Baseline rewrite.** Performed values are copied back into the plan, erasing substitution and variance.

### A.15.3:3 - Forces

| Force | Demand |
| --- | --- |
| Planning usefulness | Preserve the value or designation intended for later work. |
| Declaration locality | Read each member only inside the cited declaration episteme and the pattern that defines it. |
| Family separation | Keep RelationSignature participants distinct from A.6.1 operation arguments and results. |
| Intention versus actuality | Permit useful planned claims without asserting work or participation. |
| Replay versus burden | Pin only the editions and conditions that can change a later planning or comparison decision. |

### A.15.3:4 - Solution

#### A.15.3:4.0 - Planned-filling content and its identity

`SlotFillingsPlanItem` is a content form inside one `U.WorkPlan` ClaimGraph. Its item and row designators have meaning only within that WorkPlan episteme.

C.2.1 and A.15.2 identify the WorkPlan episteme. Changing an identity-bearing row creates different WorkPlan claim content and therefore another WorkPlan episteme. The two are historical editions only if an `EpistemeEditionRelation` predicate obtains between them; a shared file, label, carrier, or revision order does not supply that continuity. A reference may point to the WorkPlan and this content component, but it gives the PlanItem no separate identity or edition rule.

A **planned-filling claim** says: for this intended future performance and under these conditions, use this value or designation for this declared member. A.15.2 and A.15.3 state that intention. The member's own pattern still defines what the participant, argument, or result means and what must hold for its later actual use.

A **planned filling** states the intended designation. Establish later relation participation or an operation binding under the selected member's actual-use predicate. A later claim that the plan was fulfilled, missed, or changed belongs to A.15.2, A.6.RCD, or the applicable comparison pattern.

A planned-filling row states a positive intention. To prohibit or exclude a value, require its absence, or claim the list is complete, write a separate constraint or negative plan claim with its own applicability and polarity rule. Omission, an empty filler, and a negated reference do not express those claims.

#### A.15.3:4.1 - Use only members that a declaration already defines

Each row points to one member in one declaration episteme selected for the intended future use. First choose what is being planned; then open the pattern that defines that member and the rule for its actual use:

| Planned choice | Existing declaration member | What remains defined elsewhere |
| --- | --- | --- |
| participant in a future direct-relation claim | one `SlotSpec` in one `RelationSignature` episteme | the relation pattern defines participant meaning and the obtaining predicate; A.6.5 defines the local `SlotKind`, `ValueKind`, and `refMode`; A.15.3 records only the planned designation |
| argument in a future operation application | one `ArgumentDeclaration` in one A.6.1 `OperationDeclaration` | A.6.1 and the cited mechanism define the argument meaning, ValueKind, designation rule, binding predicate, and cardinality; A.15.3 records only the planned value |
| expected result of a future operation application | one `ResultDeclaration` in one A.6.1 `OperationDeclaration` | A.6.1 and the cited mechanism define result meaning and the result-binding predicate; an expected value is not a returned value |
| another declared future use | one declaration member whose own pattern defines both the member meaning and its actual-use predicate | cite that pattern and declaration; if either definition is absent, return `missing-governor` instead of inventing a target |

A `U.MethodDescription` is not a target merely because it mentions inputs, effects, parameters, bounds, or acceptance conditions. A table or form exposes an A.6.5 SlotSpec only when a cited `RelationSignature` actually contains that SlotSpec. Operation arguments and results stay in A.6.1 declarations; planning them does not turn them into A.6.5 SlotSpecs.

One item may contain several rows when they serve the same intended performance, baseline policy, and rule for revising the plan. Each row still resolves to its own declared member. Split the item when those three controls differ. The WorkPlan's present EntityOfConcern remains its C.2.1 identity discriminator; a merely possible future performance does not replace it.

#### A.15.3:4.2 - State one planned-filling row

A conforming item contains or resolves these values:

```text
SlotFillingsPlanItem:
  planItemDesignator
  workPlanRef
  intendedPerformanceDesignator
  plannedFillingRows:
    - rowDesignator
      targetDeclarationRef
      targetOperationDesignator?
      targetMemberDesignator
      targetMemberFamily:
        RelationSignatureSlotSpec |
        OperationArgumentDeclaration |
        OperationResultDeclaration |
        OtherDeclaredMember
      memberDefinitionPattern
      plannedValueOrDesignation
      planningConditions?
      declarationEditionPin?
      plannedValueEditionPin?
  baselinePolicyRef?
  laterComparisonPolicyRef?
```

This block represents WorkPlan claim content. `targetMemberFamily` is an open local dispatch vocabulary, not a public kind or closed inventory. For an operation argument or result, `targetOperationDesignator` is required so the member resolves inside the cited mechanism episteme; it stays absent for relation SlotSpecs. The `memberDefinitionPattern` field points to the pattern that defines the member and its actual-use predicate. A.15.3 still states only the plan's intention.

Read the designation rule from the selected member instead of copying it into the plan. An A.6.5 member uses its `refMode`; an A.6.1 member uses its `bindingDesignationRule`. A ByRef value must use the concrete reference kind required there and resolve to the declared ValueKind. A generic `Ref`, `SpecRef`, stored token, or merely compatible value does not pass.

Use the selected member's semantic cardinality. For a single-valued member, conditions and a resolution rule must make at most one planned value effective for one intended use. Alternatives need conditions and a rule that selects among them; row order supplies neither priority nor exclusivity. A multivalued member keeps the declaration's set, sequence, multiset, repetition, and ordering semantics. If the declaration and cited policy do not decide the needed cardinality, return `missing-governor` for the member cardinality or selection policy.

Omitting a row leaves that planned filling unstated by this item. It does not say the value or later participant is absent. Prohibition, exclusion, required absence, and closed-world completeness remain separate plan claims with their own applicability and polarity rules.

`intendedPerformanceDesignator` names the future use being planned. The enclosing WorkPlan keeps its already identified present EntityOfConcern under C.2.1 and A.15.2.

Include a planning condition only when changing it would change whether the planned value applies or which value is selected. For example, cite an independently established readiness result when readiness controls the planned use. `planningConditions` points to these separately established claims under their governing patterns.

When a baseline or comparison policy selects a planned value or judges a match, identify its kind, defining pattern, applicable episteme, conditions and reference scheme. A generic `PolicyRef` or shared label supplies no policy. Pin a declaration or value when another resolution could change the planned meaning, and make the reference and pin agree. Such a pin identifies the selected episteme; it asserts historical continuity only when the C.2.1 `EpistemeEditionRelation` is separately established.

#### A.15.3:4.3 - Plan a future relation participant

For a RelationSignature row:

1. open the relation pattern and its obtaining predicate;
2. choose the `RelationSignature` episteme the plan will use;
3. choose its declaration-local SlotSpec and `SlotKind`;
4. check the planned designation against the SlotSpec's `ValueKind` and `refMode`;
5. apply the declaration's semantic cardinality and participant constraints; and
6. record the row as a positive intended designation.

The row does not fill the SlotSpec. The SlotSpec remains reusable declaration content. The planned designation does not become the actual participant, and the direct relation does not obtain until its direct predicate is satisfied for independently identified participants.

#### A.15.3:4.4 - Plan a future operation argument or result

Open the cited A.6.1 mechanism episteme, choose its `operationDesignator`, then choose the `argumentDesignator` or `resultDesignator`. Apply that declaration's ValueKind, `bindingDesignationRule`, binding predicate, semantic cardinality, and the plan's stated conditions.

The row plans a value; it is not an application or binding. An actual argument binding needs an identified application whose argument-binding predicate holds. An actual result binding additionally needs that application to return the value under the declared result meaning. Type compatibility, an expected result, a method phrase, a ticket value, or a matching token establishes neither binding.

#### A.15.3:4.5 - Compare later use without changing the plan

When actual use is compared with the plan, establish the relation participation under its obtaining predicate or the operation argument/result binding under A.6.1. A plan row, matching label, type or value supplies none of those facts by itself. Add an independently admitted A.15.1 Work identity only when the comparison also consumes that dated occurrence claim.

If the team must state whether actual use matched the plan, name the comparison policy and the independently established actual facts. A one-off comparison may use A.6.RCD disposition 2 for a local compound assertion. Repeated parameterized comparisons may use disposition 3: keep a compound law subject-bounded when every reuse concerns one exact subject, or identify a reusable predicate-definition episteme when the rule is used across subjects. Do not admit a comparison relation kind unless a later calculation or decision needs distinct comparison occurrences as such; then name that use and follow relation-kind admission. None of these comparisons changes the WorkPlan or creates a universal planned-to-actual relation.

An unplanned participant is still an actual participant when the relation's obtaining predicate holds for the complete participant set. To say that a planned value was missing, excluded, or substituted, apply the comparison policy's closure or negative criterion to the case facts. An absent log, unresolved reference, or unavailable fact yields `missing-information`, not a negative use or variance result; absent authority yields `missing-governor`.

#### A.15.3:4.6 - Preserve revisions and replay

Pin a declaration episteme or edition-bearing planned value only when choosing another one could change the planned meaning. *Latest*, a mutable alias, a publication face, or an untyped policy label is not a reproducible reference.

When a newer declaration becomes available, establish which declaration the planned use selects and whether that selection remains admissible. Retain an unchanged earlier selection while it remains admissible. Revise the WorkPlan claim content when its intended member, value, conditions or selected declaration reference changes, including a change required by the governing rule. If the necessary rule or selection is unresolved, identify that gap before claiming the row is usable. An identity-bearing change creates another WorkPlan episteme; assert historical continuity only when `EpistemeEditionRelation` obtains. Preserve the earlier WorkPlan reference already cited by work or another actual use, and state substitution or variance separately. A carrier or representation change alone does not reidentify the plan while the C.2.1 discriminators stay fixed.

When presenting selected WorkPlan content, keep it traceable to the plan under the applicable publication rules. A new planned row, default, condition or baseline rule belongs in a revised WorkPlan under §4.0; it cannot acquire authority merely from that presentation.

### A.15.3:5 - Archetypal Grounding

These constructed cases supply illustrative planning facts; they do not report observed executions.

#### A.15.3:5.1 - Planned holder designation against one direct system-role-assignment species

An inspection team plans a future assignment of `Robot_8`. It proposes `InspectionRobotSystemRoleAssignment` as the species and `Robot_8_Ref` as the intended holder; `Robot_8_Ref : U.EntityRef` resolves to admitted `Robot_8 : U.System`. The proposed `InspectionRobotSystemRoleAssignmentSignature` names `HolderSystemSlot`, `InspectionRobotSystemRoleKindDomain` as the domain of its local assigned-kind slot, and `InspectionRobotSystemRole` as the required value. The enclosing A.15.2 WorkPlan separately states `InspectionRobotSystemRole` as the intended local system-role-kind condition.

**Planning result:** these inputs preserve the intended holder choice, but supply no resolving species declaration with its specific assignment predicate. A.2.1 states what each species must declare and the common occurrence-identity discipline; A.6.5 governs its declaration-local SlotKinds, ValueKinds and reference modes. Return `missing-governor` for the typed holder row until the domain declaration supplies the participant meanings, predicate, applicability and occurrence rule. The team can retain the intended holder as ordinary A.15.2 plan content.

With that declaration available, the typed row points to its `HolderSystemSlot` and records the planned holder designation under §4.3. A later affirmative assignment assertion requires the direct species predicate to hold for its complete real participant set and its occurrence law to be satisfied. Preserve the planned holder choice as the baseline when that predicate fails under a stated negative criterion or its satisfaction remains unresolved.

**Blocked near-miss:** `Bearing_C isPartOf Pump_P` cannot supply a relation row. A.6.5:5.2 keeps `PartHolonSlot` and `WholeHolonSlot` hypothetical until a part-relation pattern defines their meanings, predicate, applicability, and occurrence identity. Return `missing-governor: planned part-relation participant designation for <Bearing_C, Pump_P>` or keep the choice as ordinary A.15.2 plan content; do not present the sketch as an admitted `RelationSignature`.

#### A.15.3:5.2 - Planned argument and expected result against A.6.1

A team plans one Pump #37 recognition evaluation. It expects the application to use Pump #37 as `candidate` and return `true` if the cited criterion, construction facts, reidentification rule, interpretation basis, and required fastening-relation fact are available and determine satisfaction. The condition reference records that expectation; it makes none of those claims true. `Pump37-Classification-Plan-E1_Ref` identifies the WorkPlan, `HolonRecognitionMechanism-E1_Ref` identifies the cited A.6.1:5.7 mechanism episteme, and `Pump37-ExpectedTrue-Conditions-E1_Ref` identifies the separate condition claims. The WorkPlan concerns the already admitted Pump #37, uses `PumpMaintenanceEvaluationScheme-E1`, and coordinates intended `HolonRecognitionEvaluation@FPF` during 10:00–10:15 UTC on 2026-07-21 with intended performer `RecognitionEvaluator_A`. These are planning claims; the later application below is established separately.

The WorkPlan carries this copyable planning content:

```text
SlotFillingsPlanItem:
  planItemDesignator: pump37-recognition-baseline
  workPlanRef: Pump37-Classification-Plan-E1_Ref

  intendedPerformanceDesignator: planned-pump37-recognition-use-01
  plannedFillingRows:
    - rowDesignator: candidate-pump37
      targetDeclarationRef: HolonRecognitionMechanism-E1_Ref
      targetOperationDesignator: recognizeAdmittedHolonCandidate
      targetMemberDesignator: candidate
      targetMemberFamily: OperationArgumentDeclaration
      memberDefinitionPattern: A.6.1
      plannedValueOrDesignation: Pump_37_Ref
      planningConditions: Pump37-ExpectedTrue-Conditions-E1_Ref
      declarationEditionPin: HolonRecognitionMechanism-E1
    - rowDesignator: expected-recognition-true
      targetDeclarationRef: HolonRecognitionMechanism-E1_Ref
      targetOperationDesignator: recognizeAdmittedHolonCandidate
      targetMemberDesignator: recognitionJudgment
      targetMemberFamily: OperationResultDeclaration
      memberDefinitionPattern: A.6.1
      plannedValueOrDesignation: true
      planningConditions: Pump37-ExpectedTrue-Conditions-E1_Ref
      declarationEditionPin: HolonRecognitionMechanism-E1
```

In that operation declaration, `candidate` accepts exactly one `U.Entity` through a `U.EntityRef`; `recognitionJudgment` returns exactly one carried-by-value member of `RecognitionJudgmentValue = {true, false, unknown}`. The rows cite those rules instead of redeclaring them.

Later, A.6.1 identifies `Pump37RecognitionApplication-2026-07-21T100000Z`. The application binds Pump #37 as `candidate`, but a required fastening-relation fact is unavailable, so it returns `unknown`. **Comparison result:** the plan expected `true` under its cited conditions; the actual application returned `unknown` because one availability condition failed. An A.6.RCD disposition-2 local compound assertion may state that comparison from the preserved plan episteme, application, result binding, and failed condition. It neither rewrites a row nor admits a universal planned-to-actual relation.

The plan keeps the expected `true`; A.6.1 supplies the separately established application and its returned `unknown`. Use A.1 for the recognition criterion and C.2.1 if a separate result episteme is needed. Evidence and assurance remain governed by their applicable patterns.

#### A.15.3:5.3 - Hardware-acceptance pseudo-slots rejected

A hardware acceptance method says to use a calibrated instrument, selected reference plane, calibration record or certificate, and threshold. That sentence describes a method; it declares no A.6.5 SlotSpecs. Keep those choices as ordinary A.15.2 plan content, each under the pattern that defines the plane, calibration or evidence reference, and threshold.

Open A.15.3 only when an A.6.1 declaration, a `RelationSignature` SlotSpec, or another declared member already defines both the position and its actual-use rule. Otherwise return `missing-governor` for typed reuse; do not wrap the method description or equipment card in a fictitious slot-bearing declaration. Measurement, evidence sufficiency, readiness, acceptance, and actual instrument use remain separate.

#### A.15.3:5.4 - Edition-sensitive selector or archive planning

A selector or archive plan may need to preserve a comparator, descriptor definition, distance definition, evidence policy, or another edition-sensitive choice. A suite description, archive card, or generated view does not make those labels declaration members.

If a cited declaration exposes an A.6.1 argument or result, a `RelationSignature` SlotSpec, or another member whose defining pattern supplies its meaning, actual-use predicate, and cardinality, record one A.15.3 row per chosen member and pin only editions that affect the plan. Otherwise keep the choice as ordinary A.15.2 content or return `missing-governor` for typed reuse. The later application, dated work, archive or selection result, evidence path, publication, and variance remain separate; a card used as a view conveys the selected plan rather than establishing additional planning claims.

### A.15.3:6 - Scope Declaration and Rationale

**Scope.** A.15.3 records positive planned designations against existing declared members inside one WorkPlan. When a later question requires comparison, establish actual-use claims under each member's predicate and compare the resulting facts under §4.5. Prohibitions, exclusions, required absence and completeness use separate plan claims under §4.0; other claims use the governing patterns named in §12.

**Rationale.** The practitioner gets a reusable planned baseline without another U-kind or universal slot relation. Each declaration family keeps its own member meanings and actual-use rules; A.15.3 adds only the planned choice.

### A.15.3:7 - Conformance Checklist

| ID | Requirement | Practical test |
| --- | --- | --- |
| CC-A15.3-01 | The item is declaration-local WorkPlan content. | Its designator resolves inside one cited WorkPlan episteme; no independent PlanItem identity or row authority is claimed. |
| CC-A15.3-02 | The WorkPlan keeps its already identified present EntityOfConcern; the item separately names the future performance being planned. | Use the intended-performance designator as plan content; the EntityOfConcern resolves to the already identified present subject. |
| CC-A15.3-03 | Every row points to one declaration episteme and member whose pattern defines both member meaning and actual-use predicate. | The declaration reference, local member designator, family, defining pattern, and predicate route all resolve; A.15.3 states only the intention. |
| CC-A15.3-04 | Relation rows use only conforming A.6.5 SlotSpecs inside cited `RelationSignature` epistemes. | Resolve `HolderSystemSlot` inside the particular species signature, including its predicate and participant meanings; the Robot_8 row in §5.1 awaits that declaration. Hypothetical `PartHolonSlot` and `WholeHolonSlot` retain their named blocker. |
| CC-A15.3-05 | Operation rows use A.6.1 argument or result declarations. | Mechanism episteme, operation designator, member designator, ValueKind, designation rule, binding predicate, and cardinality resolve together. |
| CC-A15.3-06 | Any other target has a pattern that explicitly defines it. | Missing member meaning, actual-use predicate, or defining pattern yields `missing-governor`, not a generic target. |
| CC-A15.3-07 | The planned value follows the member's ValueKind, designation rule, and cardinality. | A single-valued target has at most one effective planned value; conditions and a resolution rule select among alternatives, while multivalued and ordering semantics come from the declaration. |
| CC-A15.3-08 | A row states a positive intention. | Omission is open-world; prohibitions, exclusions, required absence, and completeness use separate plan claims rather than empty or negated fillers. |
| CC-A15.3-09 | Planned filling remains planned. | Read each row as the positive intention defined in §4.0, keeping its intended performance and applicability conditions explicit. |
| CC-A15.3-10 | Plan revision follows C.2.1 WorkPlan identity. | Changed identity-bearing content identifies another WorkPlan episteme; edition continuity is asserted only when `EpistemeEditionRelation` obtains, and PlanItems gain no separate edition ontology. |
| CC-A15.3-11 | Later actual facts are established independently. | Establish actual relation participation and operation bindings under their direct predicates. Identify Work under A.15.1 only when that dated occurrence claim is needed; none follows from a plan row. |
| CC-A15.3-12 | Later comparison preserves the cited baseline and polarity. | Substitution or variance uses a stated comparison policy; a missing-filler or negative result needs its closure or negative criterion and case facts. |
| CC-A15.3-13 | Edition, reference, and policy pins are concrete and decision-relevant. | No implicit *latest*, generic RefKind, generic PolicyRef, publication face, or conflicting pin controls a row. |
| CC-A15.3-14 | Conditions retain their own grounds; a view alone adds no plan authority. | Cite the governing conditions from their own patterns. Trace a view to its WorkPlan; any new planned row or rule requires the corresponding plan revision. |

### A.15.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
| --- | --- | --- |
| Generic slot-bearing description | Any description with fields is treated as a reusable declaration. | Point to a declared `RelationSignature` SlotSpec, A.6.1 argument or result, or another member whose pattern defines its meaning and actual use. |
| Dependent PlanItem U-kind | A ClaimGraph component receives a rival identity and ontic settlement. | Keep `SlotFillingsPlanItem` as declaration-local WorkPlan content. |
| Planned SlotRelation | The plan claim is reified as an obtaining world-side relation. | Keep planned filling as positive claim content; open an actual relation only under its direct predicate. |
| Declaration/plan responsibility blur | The declaration pattern is said to make the planning intention, or A.15.3 is said to define actual use. | Let the declaration pattern define member meaning and actual-use predicate; let A.15.2 and A.15.3 state the intention. |
| Method-description slot | Generic method wording is mistaken for a declaration member. | Keep it as ordinary plan content or return `missing-governor` when typed reuse is required. |
| Relation/operation collapse | A.6.1 arguments and results are written as A.6.5 SlotSpecs. | Dispatch by target family and keep each declaration vocabulary local. |
| Row-count cardinality | Row count or order silently defines multiplicity, alternatives, or sequence. | Use the declaration's cardinality; for alternatives, state conditions and a resolution rule. |
| Empty filler as prohibition | Omission, null, or a negated reference is read as *must not use*. | State prohibition, exclusion, required absence, or completeness as a separate plan claim. |
| Plan-as-actual | A planned value is treated as actual participation or a returned result. | Establish the relation or application binding independently; identify Work separately when that occurrence claim is needed. |
| Generic reference or policy | `Ref`, `SpecRef`, `PolicyRef`, or a shared label is treated as sufficient. | Use the concrete RefKind and identify the policy's kind, defining pattern, episteme, applicability, and reference scheme. |
| Latest-as-baseline | A mutable label stands for a declaration or value episteme. | Pin the selected episteme when another resolution could change the planned or comparison result. |
| Backfilled plan | Actual values replace planned rows after work. | Preserve the cited plan episteme and state a neighboring substitution or variance claim. |

### A.15.3:9 - Consequences

| Benefit | Cost and control |
| --- | --- |
| Planned choices remain replayable. | Each row must point to a declared member and the pattern that defines it. |
| Declaration families remain coherent. | Planners must dispatch relation participants and operation values separately. |
| Actual-use claims have separate grounds. | A matching plan row supplies neither relation participation nor an application binding; add Work admission only when the claim consumes it. |
| Missing declared semantics becomes visible. | Return the specific missing-governor result when the member or actual-use rule is absent; distinguish missing planning information under §12b. |

### A.15.3:10 - Rationale

Planning needs a way to preserve intended values without turning every planning field into ontology. Existing `RelationSignature` SlotSpecs, A.6.1 operation declarations, and other declarations already define reusable member meanings and actual-use predicates. A.15.3 records only the intended use of those members inside one WorkPlan.

The split is concrete: the declaration pattern defines member meaning and actual-use rule; A.6.5 or A.6.1 defines the applicable declaration form; the WorkPlan records intention under C.2.1 and A.15.2. Establish a later application, relation occurrence, result or comparison under its own predicate. Identify dated Work only when its occurrence is claimed. The planning row supplies none of those actual-use facts by itself.

### A.15.3:11 - SoTA-Echoing

| Source contribution | Adoption in A.15.3 | Rejected shortcut |
| --- | --- | --- |
| [ISO/IEC/IEEE 12207:2017](https://www.iso.org/standard/63712.html) describes software life-cycle processes, activities and tasks; it is retained as a historical anchor, withdrawn on 29 April 2026 and superseded by [12207:2026](https://www.iso.org/standard/90219.html). [ISO/IEC/IEEE 15288:2023](https://www.iso.org/standard/81702.html) provides system life-cycle process descriptions without prescribing a specific life-cycle model and refers detailed information-item content to ISO/IEC/IEEE 15289. | Keep the declaration, intended plan content, and performed work separate. | Treating a process-tooling layout or checklist field as an FPF declaration. |
| [SLSA v1.2 build provenance](https://slsa.dev/spec/v1.2/build-provenance) separates build definition, including resolved dependencies, from run details; [in-toto Statement v1](https://github.com/in-toto/attestation/blob/main/spec/v1/statement.md) separates subjects from the typed predicate content. | Cite declaration and edition only when replay depends on them; keep run, provenance, result, and evidence claims separate. | Importing a supply-chain record schema as a universal slot or result ontology. |
| The [Nix 2.26 manual’s lock-file mechanism](https://nix.dev/manual/nix/2.26/command-ref/new-cli/nix3-flake.html#lock-files) records resolved dependency inputs in `flake.lock`, including revisions where applicable and content hashes. An existing, up-to-date lock file preserves the selected direct and transitive dependencies for repeatable input resolution. | Pin the selected declaration or value episteme when another resolution could change the planned meaning. | Saying *latest* when a later comparison needs one edition. |

### A.15.3:12 - Relations

- **Builds upon:** C.2.1 and A.15.2 for WorkPlan identity, present EntityOfConcern, intended-performance designators, and intended-work content; A.6.5 for SlotSpecs inside `RelationSignature` epistemes; A.6.1 for operation argument and result declarations; and the pattern that defines any other admissible declaration member.
- **Coordinates with:** A.15.1 for dated Work; relation patterns for actual participants; A.6.1 for applications and bindings; A.6.RCD for local fulfilment or variance claims when no comparison relation is already defined; A.15.5 for work-entry readiness; and the evidence, gate, evaluation, result, production, delivery, acceptance, publication, and currentness patterns when those claims are made.

### A.15.3:12a - P2W planned-filling use

When P2W reaches intended work and a planned value reuses a member already declared under §4.1, carry the WorkPlan, intended-performance designator, declaration episteme, member designator, defining pattern, planned value, and each condition or pin whose change would alter the effective planned value or later comparison. The declaration pattern defines the member and actual-use rule; A.15.2 and A.15.3 state the intention.

If no reusable member is needed, carry ordinary A.15.2 plan content. If typed planned use is needed but the member, its meaning, its actual-use predicate, or its defining pattern is absent, carry `missing-governor` for that intended use. For an incomplete or unresolved plan, name the planning information to recover (§12b). The row may cite a separately established condition when it controls the planned choice. Establish other claims under their own patterns—for example, A.15.1 identifies performed Work and A.15.5 decides work-entry readiness.

### A.15.3:12b - Lowering, repair, and refresh conditions

Use ordinary A.15.2 plan content when no reusable declaration member is needed. For typed use, name any missing or unresolved planning information, including the intended-performance designator, declaration episteme or member designator; an operation argument or result also requires its operation designator. Recover that information so the row identifies the intended use and resolves to an existing declaration member. Return `missing-governor` only when the needed member or its defining pattern does not exist, or the member's meaning, designation rule, cardinality, or actual-use predicate has not been defined. Do not replace that blocker with a generic slot-bearing description.

State prohibitions, exclusions, required absence, and completeness under their plan-constraint or negative-claim patterns instead of using omission or an empty filler. A later missing-filler, substitution, or variance result needs a comparison policy whose closure or negative criterion applies to the case facts.

Apply §4.6 to decide whether the selected declaration must change. Revise the WorkPlan ClaimGraph when its selected target member, planned value, intended-performance designator, condition, or relied-on declaration reference changes. If a C.2.1 identity discriminator changes, identify another WorkPlan episteme and relate it to the earlier one only when `EpistemeEditionRelation` obtains. Preserve the earlier WorkPlan reference already cited by work or another actual use. Refresh only a declaration, reference resolution, policy, or WorkPlan episteme whose changed resolution would alter the later decision; re-evaluate an actual-use change under its relation predicate or A.6.1 application predicate.


### A.15.3:End
