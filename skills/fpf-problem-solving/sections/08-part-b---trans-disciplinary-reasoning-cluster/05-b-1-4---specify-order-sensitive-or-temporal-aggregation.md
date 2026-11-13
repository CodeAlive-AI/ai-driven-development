## B.1.4 - Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)

> **Type:** B-family aggregation pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Use this when.** Use this pattern when the claim aggregates already recovered relations over a set of ordered positions, phases, or a time window, and the question is not just ordinary part-whole construction. Typical cues are ordered steps, order-sensitive argument chains, asset histories, proper temporal restrictions of one enduring carrier, rolling windows, use-bounded roll-ups, time-sliced evidence, or a bounded chronology over C.2.1 episteme identities and already obtaining edition relations.

**Not this pattern when.** If the question is ordinary part-whole or collection admission, use `B.1`, `A.14`, and `C.13`. If it is episteme identity or historical edition continuity, use `C.2.1` before any aggregation. If the question is the method as such, method description, work plan, dated work occurrence, or Work temporal part or episode, use `A.3.1`, `A.3.2`, `A.15.2`, or `A.15.1`. If the question is work-resource accounting, use `B.1.6`. If the question is changed identity, use the pattern that defines the subject's identity or change; for a clear whole-reidentification question, use `B.2` directly to test whether the existing whole suffices or a new whole must be reidentified. Use `B.2.P` first only when emergence-family wording hides the claim kind. If the question is temporal adequacy of a claim, use `C.27`.

**What goes wrong if missed.** A reader may mistake an ordering for parthood, a planned sequence for performed work, a phase for a new whole, or temporal coverage for evidence currentness.

**What this buys.** The practitioner can specify or compute the order-sensitive or temporal aggregate needed by a receiving use, with its combining rule and limits. Method, Work, transformation, work-resource, temporal-adequacy and MHT claims retain the patterns that define or test them.

### B.1.4:1 - Problem Frame

Many useful aggregates are not simple unordered wholes. A manufacturing sequence changes meaning when steps are swapped. An argument chain depends on which premise is used before which lemma. A turbine or another enduring individual with a stated identity rule may be considered across proper temporal restrictions. An unchanged paper or dataset episteme may also be restricted to a proper interval only while its complete C.2.1 identity triple remains fixed; changed claim content, EntityOfConcern, or effective ReferenceScheme identifies another episteme, with edition continuity tested separately. In these cases the aggregation concerns order or temporal coverage over already recovered relations.

`B.1.4` asks what result the receiving use needs, which inputs and independently established relations it uses, and which operation combines them. Order, temporal reference, window, coverage and overlap qualify that operation when they affect its result. A stronger claim keeps its subject grounds.

### B.1.4:1.1 - Problem

Confusing these relations produces four recurring errors. First, `SerialStepOf` or another ordered relation is read as ordinary parthood, so changing the order looks harmless even when the aggregate meaning changes. Second, a phase label is read as a new holon level or a new whole, so identity change is hidden instead of handled by whole reidentification. Third, design-time plans, possible method order, run-time histories, and evidence windows are folded together as one sequence. Fourth, a user treats mathematical notation as the represented object or relation, without establishing the correspondence needed for the bounded use.

The resulting aggregate is unusable for the proposed claim: the user cannot tell which carrier is being followed, which positions or phases are included, which relation is ordered, which time window is covered, whether gaps or overlaps matter, or which pattern must carry a stronger work, resource, transformation, evidence, or whole-reidentification claim.

### B.1.4:1.2 - Forces

| Force | Tension |
| --- | --- |
| Order sensitivity vs. ordinary parthood | Ordered positions must remain reviewable without recasting them as parts of one physical whole. |
| Temporal coverage vs. carrier identity | A phase aggregate needs useful time windows, but it must not hide that the carrier changed identity. |
| Design-time relation vs. run-time history | Method order, work plan, and performed work often share labels, but they are different claims. |
| Compact notation vs. ontology | `Gamma_ctx`, `Gamma_time`, graph, or algebra notation can make a relation easy to use, but cannot create a holon, method, work occurrence, or transformation. |
| Local aggregation vs. related claims | The aggregation account should remain compact while retaining links to the independent grounds for resource, evidence-currentness, transformation, and MHT claims. |

### B.1.4:2 - Solution

Start with the receiving question and the result it needs. An already adequate aggregation rule and ordinary explanation can be used directly.

1. **Recover the inputs and relations.** Identify the included positions, values, intervals or phases and the objects they concern. Keep their identity and relations grounded in the subject facts and applicable rules. For a temporal input, recover its bearer, temporal reference and interval; relate different references only through a justified conversion.
2. **Choose the combining rule and result.** State the operation and what it returns: for example, an ordered relation structure, a combined value, the union of covered intervals or their elapsed span. Supply the order, join, independence, coverage and overlap conditions that this operation uses. If the rule needed by the question is missing, retain that gap rather than naming an unsupported aggregate.
3. **Obtain the requested result.** A specification can be sufficient when the task asks how the aggregation is to be performed. When a computed result is needed, apply the selected operation and interpret its result under those conditions. Distinguish an order structure from the result of applying the operations it represents. Section :5 shows why the same inputs can support different warranted results.
4. **Bound the use and stop.** State the supported use and any condition whose failure or uncertainty changes it. Narrow the result or leave the affected conclusion unresolved when its required basis is missing. Use another pattern when a distinct claim needs that pattern's contribution. Stop with the sufficient ordinary answer.

When the receiving use needs an inspectable account, reuse an adequate account or materialize a `ContextTemporalAggregation@Context` record. It describes the independently established inputs, rule and result; it does not establish their subject facts:

```text
ContextTemporalAggregation@Context:
  aggregationConcernRef
  aggregatedEntityOfConcernRef
  aggregationMode: contextualOrder | temporalAggregation
  combiningRuleOrOperator
  resultOrResultSpecification
  includedPositionRefs?
  includedIntervalRefs?
  includedPhaseRefs?
  claimScopeRef?: U.ClaimScope
  orderedRelationRefs?
  temporalRelationRefs?
  phaseRelationRefs?
  orderSpecRef?
  temporalReference?
  timeWindowRef?
  carrierIdentityRefs?
  independenceOrJoinConditionRefs?
  coverageAndOverlapPolicyRefs?
  boundaryCrossingRelationRefs?
  relatedMethodRefs?
  relatedMethodDescriptionRefs?
  relatedWorkOccurrenceRefs?
  relatedWorkResourceAggregationRefs?
  relatedTransformationRefs?
  relatedWholeReidentificationRefs?
  evidenceOrSourceRefs?
  admissibleUse
  stopOrReturnCondition?
  nonAdmissibleOverread?
  strongerSourceReturnCondition?
```

The aggregation concern is the receiving question; the EntityOfConcern is the independently identified subject of the aggregation claim. Included inputs retain their bearers and identities. Add each optional value when it changes that claim or its use. Facts and evidence needed to warrant the result remain necessary whether or not a reference field is written.

`stopOrReturnCondition?` states an action-changing limit; `strongerSourceReturnCondition?` is used only for a distinct stronger claim that the receiving work needs. Include `nonAdmissibleOverread?` only when it passes F.19's plausible-reader test; `groundedNonAdmissibleOverread?` is an alias for that same optional value.

#### B.1.4:2.1 - Two Aggregation Modes

| Mode | Object | Required relation discipline | Typical use |
| --- | --- | --- | --- |
| Contextual order aggregation | Positions and relation facts whose order, partial order or join structure matters to the stated use. | Included inputs, combining rule and required result, `OrderSpec`, ordered relation refs, join or independence conditions when used, and ClaimScope when needed. | Ordered method relation, order-bound argument chain, staged construction description, controlled sequence. |
| Temporal aggregation | Interval or time-indexed facts about named bearers or occurrences. | Input identities and temporal relations, temporal reference or justified conversion, `TimeWindow`, combining rule, coverage and overlap policy. The proper-phase profile additionally requires one continuing carrier and the phase relation. | Work-interval union or elapsed span, asset phases, observation windows, or chronology over episteme identities. For proper phases of one episteme, its complete C.2.1 identity triple stays fixed; distinct editions require their identities and any claimed edition relation. |

When a use combines order and temporal claims, distinguish what each contributes and state the correspondence on which the joint result relies; one sufficient account may contain both. A Method may have an ordered relation structure. Work that enacts it may have A.15.1 temporal parts, episodes, operational parts or separate occurrences, while C.27.TA supplies any independently declared overlap or other interval relation. Aggregate those inputs under the chosen rule. Use `PhaseOf` only for the proper-phase profile of one enduring carrier, not as a substitute for Work or temporal relations.

#### B.1.4:2.2 - Where Stronger Claims Go

| Claim | Pattern to use |
| --- | --- |
| Method as semantic way of doing | `A.3.1` |
| Method-description membership or a description-use question | `A.3.2` defines membership and description boundaries. For SOPs, code or simulator configurations, use A.3.2 when the question is whether the identified episteme has an admitted Method as its exact EntityOfConcern and makes a substantive claim about it as a way of doing; representation form alone does not select the branch. Use the applicable subject or publication pattern for another claim. |
| Work plan | `A.15.2` |
| Dated work occurrence, performed episode, or evidence that work happened | `A.15.1` |
| Work-resource roll-up, spent resource, cost, effort, energy, material, or comparable ledger | `B.1.6` |
| Episteme identity and historical continuity between distinct epistemes | `C.2.1`; aggregate only identities and an already obtaining `EpistemeEditionRelation` when the bounded use needs their chronology |
| Proper `PhaseOf`, portion, membership, or other parthood relation for a non-Work carrier | `A.14`, `B.1`, and `C.13` as appropriate; Work temporal and part relations remain with `A.15.1` |
| Holon delimitation or boundary-crossing relation | `A.1`, `B.1`, `A.12`, `A.3.4`, or the pattern that defines the relation |
| Bounded change under conditions | `A.3.4` |
| Whole reidentification, emergence-family wording, MHT, MET, MFT, synergy, or metric-mirage wording | Use `B.2.P` when emergence-family wording hides the claim kind. If a whole-reidentification question remains, including one raised by an autonomy or capability change, use `B.2`; `B.2.2` and `B.2.3` handle System and Episteme result recognition, and `B.2.4` is the capability/functioning decision bridge. Use `B.2.5` separately for a two-sided supervisor-subholon feedback claim, whether or not whole reidentification is current. |
| Architecture structural view or selected structure | `C.30.ASV`, `A.22`, or the pattern that defines or tests the architecture claim |
| Mathematical order, graph, algebraic notation, graph path or morphism used as expression | Use the applicable mathematical or subject rule directly when it supplies the result. Use `C.29` for a separate unresolved representation-choice, transfer or reliance question. Use `E.18` when its selected transformation-flow structure is the subject, and `E.18.2` for a mathematical description of that TFS or a selected TFS network. |

### B.1.4:3 - Optional Operator Notation

`Gamma_ctx` and `Gamma_time` are optional notation for a selected aggregation operation and its result. A specification may state such an application without claiming that its result has already been computed.

```text
Gamma_ctx(selectedInputs, combiningRule, orderSpec, joinOrIndependenceConditions?)
  -> contextual aggregation result

Gamma_time(selectedTemporalInputs, combiningRule, temporalReference, timeWindow, coverageAndOverlapPolicy)
  -> temporal aggregation result
```

The notation expresses the selected operation; it supplies no default combining rule. Temporal inputs retain the values and temporal facts consumed by that rule. An optional account can provide the argument values and describe the result. Establish the represented objects and relations under their patterns, and check the operation's conditions before relying on that result.

Keep an ordinary statement about who prepared the aggregation ordinary. If the use asserts one dated sequencing, combining, measuring or auditing Work, recover the performer's A.13 core and admit the Work independently under A.15.1. Use A.3.4 for a separate transformation claim, B.1.6 for resource aggregation, and A.10 to recover provenance and bounded reliance on independently established results. Writing the record does not identify its writer as the transformer of the EntityOfConcern.

### B.1.4:4 - Admissible Checks

For contextual order aggregation:

- the ordered relation refs are named by value;
- the `OrderSpec` is declared as total order, partial order, or another named relation;
- independence, branch, or join conditions are named when parallel factors are used;
- the claim identifies its included inputs, combining rule, result or result specification, ClaimScope when needed, and admissible use; any holon-boundary crossing it uses has its relation basis;
- method, method-description, work, transformation, and resource claims use the patterns that define or test them.

For temporal aggregation:

- each input interval and its bearer or occurrence are identified; a proper-phase claim additionally preserves the one carrier's identity under its rule;
- the temporal reference, any required conversion and the selected time window are established;
- the selected combining rule and coverage/overlap policy hold; handle allowed overlaps and gaps as that rule requires, or narrow the use;
- a changed identity is represented as a distinct input when appropriate, rather than hidden as another phase of the same carrier;
- work-resource claims use `B.1.6`; positive temporal-aspect claims use `C.27.TA`, while a separate temporal-claim adequacy question uses `C.27`. Currentness uses `G.11`, and `A.10` recovers provenance and bounded reliance when needed.

**B.1 invariant carry-through.** Apply an algebraic law only when the recovered relation and selected operator justify it. A unique computed contextual result requires the operation, permitted order and join or independence conditions to determine that result. If admissible orders give different outcomes, retain the supported alternatives or establish the additional ordering or selection needed by the use. An order structure can be a sufficient aggregate without asserting a unique execution outcome.

Temporal aggregation follows its selected rule, temporal reference, coverage and overlap policy; one-carrier continuity is additionally required by the proper-phase profile.

A repeated designation creates no additional occurrence or relation by itself; retain distinct occurrences and ordered positions when the claim distinguishes them. State any singleton or idempotence law for the operator.

Weakest-link and monotonicity claims name the characteristic and model being bounded or improved; an aggregation record alone establishes no performance, safety or assurance result.

#### B.1.4:4.1 - Aggregation obligations

| Obligation | What must be named | Why it matters |
| --- | --- | --- |
| Independence and joins | For branches used in the aggregate, name their relation refs, any join refs and the condition under which they may be combined. | Prevents an ordered aggregate from treating dependent branches as independent evidence or work. |
| Order specification | Total order, partial order, precedence relation, or another named relation over the selected positions. | Keeps order-sensitive claims from being read as unordered collection claims. |
| Decisive dependency relation | For a weakest-link claim, name the relation that makes one position, delay or missing step decisive for the aggregate use. | Keeps that claim dependent on its model and relation. |
| Bearer identity and phase continuity | Identify each temporal input's bearer. For the proper-phase profile, state which carrier remains the same and under which identity rule. | Keeps separate occurrences distinguishable and prevents a phase account from hiding identity change. |
| Temporal coverage | Temporal reference, time window, intervals or phase refs, combining rule and coverage/overlap policy. | Distinguishes covered time from elapsed span and exposes how gaps and overlaps affect the result. |
| Chronological discipline | State whether the claim uses chronological, logical, publication or performed-work order, and the correspondence needed when more than one is used. | Keeps a document sequence, argument sequence and work occurrence sequence from substituting for one another. |
| Monotone characteristic | For a monotonicity claim, name the characteristic, comparison and model under which adding inputs preserves or improves the result. | Blocks generic monotonicity claims over an unspecified aggregate. |

### B.1.4:5 - Archetypal Grounding (Worked Slices)

**Manufacturing sequence.** A frame is prepared, welded, inspected, painted and packed. For a planning or comparison question, specify the selected steps, precedence, any joins used and the required result. That order specification can be the sufficient B.1.4 result. Shop-floor Work occurrences use `A.15.1`; energy and material roll-ups use `B.1.6`; a changed frame state uses `A.3.4`.

**Paper edition history.** When draft, reviewed and camera-ready texts change claim content, EntityOfConcern or effective ReferenceScheme, C.2.1 identifies distinct epistemes and tests each claimed `EpistemeEditionRelation` independently. B.1.4 can return a bounded chronology over those identities, obtaining relations and relevant applicability or publication windows. The editions retain their distinct identities. If one unchanged episteme is needed over a proper interval, A.14 `PhaseOf` states that restriction. Source-currentness and publication-use claims use `A.10`, `G.11` and `E.17` as applicable; chronology establishes none of them.

**Cross-regime evidence window.** A dashboard combines observations from two operating regimes. Identify the observation sets, their subject populations or carriers, temporal reference and aggregation window. Choose the operation and the claim it is meant to support. Under `C.16`, establish the measurement meanings, specification, scale and unit semantics, model/calibration conditions and population or time basis needed for direct comparability.

Any cross-basis conversion or comparison retains its operation rule and loss or uncertainty conditions. Use `C.29` when a separate mathematical correspondence or reliance question remains. If the required compatibility is unestablished, retain separate results or narrow the claim rather than pool them as one supported aggregate.

**Order-dependent calculation.** In this constructed case, start with `x = 1` and combine `f(x) = x + 1` and `g(x) = 2x` by sequential application. Applying f then g gives `g(f(1)) = 4`; applying g then f gives `f(g(1)) = 3`. An OrderSpec permitting both orders does not establish one numerical answer or the independence needed to ignore order. If the use needs a unique answer, establish the required precedence or a justified operator property that makes all permitted orders equivalent. Otherwise retain the two supported outcomes. If the task needs only the partial-order specification, that specification already answers it.

**Work-interval aggregate.** In this constructed case, independently admitted Work occurrences W1 and W2 occupy `[0,2)` and `[3,5)` hours under one declared clock reference, within window `[0,5)`. For covered time, take the union `[0,2) ∪ [3,5)`: its duration is 4 hours. For elapsed span from first start to last end, take the convex hull `[0,5)`: its duration is 5 hours, including the gap. These are different warranted answers to different questions, following the A.15.1:9.1 Work-interval profile.

Union counts a shared instant once when intervals overlap. Its set-based policy and the hull policy are idempotent for duplicate input and independent of input order; another operator needs its laws. The two occurrences keep their separate identities and require no invented common Work or `PhaseOf` relation.

### B.1.4:5.1 - Bias-Annotation

| Bias risk | Failure | Mitigation |
| --- | --- | --- |
| Notation becomes ontology | `Gamma_ctx`, `Gamma_time`, graph, or algebra wording is treated as the in-life object or relation. | Recover the ordered or temporal relation first, then treat notation as a selected expression. |
| Sequence becomes work | A method order, plan order, document order, or performed-work history is treated as the same thing. | Name the claim and use the applicable method, description, work-plan, dated-Work, or evidence pattern. |
| Phase becomes level | A phase label is used as a new system level or a new whole. | Recover the subject first: C.2.1 identity/edition law for an episteme, A.15.1 for Work, or the carrier's identity rule and proper `PhaseOf` for another enduring individual. Open whole reidentification only when that question remains current. |
| Coverage becomes authority | A complete-looking timeline is treated as sufficient evidence or currentness. | Use the applicable evidence, source-currentness, and temporal-adequacy patterns when those claims are current. |

### B.1.4:6 - Conformance Checklist

| ID | Requirement | Purpose |
| --- | --- | --- |
| CC-B1.4-1 | The aggregation claim identifies its subject, included inputs and relations, combining rule, required result, aggregation mode, ClaimScope when needed, temporal reference/window when relevant, and admissible use. | Makes the aggregation usable without requiring a separate record when an ordinary answer suffices. |
| CC-B1.4-2 | Contextual aggregation identifies its ordered relations and OrderSpec. Temporal aggregation identifies its intervals, bearers, temporal reference and TimeWindow; the proper-phase profile also establishes one-carrier identity and the phase relations. | Keeps order, temporal aggregation and proper-phase claims distinguishable. |
| CC-B1.4-3 | Independence, join, coverage, and overlap-policy conditions are present when the claim uses them. | Keeps local composition reviewable. |
| CC-B1.4-4 | Method, method-description, work-plan, work-occurrence, work-resource, transformation, and whole-reidentification claims use the patterns that define or test them. | Prevents B.1.4 from absorbing neighboring objects. |
| CC-B1.4-5 | Mathematical notation is treated as a selected lens or expression, not as the in-life object or relation. | Keeps `Gamma_ctx`, `Gamma_time`, graph, and algebra language bounded. |
| CC-B1.4-6 | Use stays within the established operation, identity and coverage conditions. When a required condition fails or remains unknown, narrow the result or retain the unresolved conclusion; use the subject pattern for a distinct identity, change or whole-reidentification question. | Preserves stops without requiring a stronger claim merely to finish an ordinary aggregate. |

### B.1.4:7 - Common Anti-Patterns and How to Avoid Them

| Overread | Repair |
| --- | --- |
| A sequence is treated as physical parthood. | Recover ordered relation refs and use contextual aggregation; use part-whole patterns only for part-whole claims. |
| A phase label is treated as a new system level. | Recover the carrier identity and phase relation. If a clear whole-reidentification question remains, use `B.2` directly; use `B.2.P` first only when emergence-family wording hides the claim kind. |
| A planning order is treated as performed work. | Use `A.15.2` for work plan and `A.15.1` for dated work occurrence. |
| A resource total is inferred from temporal coverage without its resource-accounting rule. | Establish the resource claim under `B.1.6`. One account may state both the independently supported temporal and resource results. |
| A diagram or table substitutes for the independently represented object or relation. | Establish that subject and the representation correspondence. A diagram or table may present or return the aggregate result; its form alone establishes neither the represented facts nor their identity. |

### B.1.4:8 - Consequences

The practitioner obtains the aggregation specification or result needed by the receiving use, with its rule and conditions recoverable in a sufficient ordinary explanation or an inspectable account. `Gamma_ctx` and `Gamma_time` remain optional expressions. Recovering the inputs and conditions takes work, but makes the result distinguishable from claims about performed Work, resources, transformation and whole reidentification.

### B.1.4:8.1 - Rationale

Order-sensitive and temporal aggregation combine already grounded inputs under a selected operation. One continuing carrier may be considered through proper phases; separate Work occurrences or observations may supply intervals for a different temporal aggregate; and an order structure may be the desired result or an input to a further calculation.

Each case keeps its grounds: carrier identity and `PhaseOf` for proper phases, C.2.1 identity and obtaining edition relations for episteme history, A.15.1 for Work, C.27.TA for temporal facts, and the ordered relations, operation and conditions for the aggregate. Resource, transformation, evidence and whole-reidentification claims retain their rules.

Distinguish design-time possible order from run-time history. When both contribute to one use, state the correspondence between their claims; keep one or several accounts according to what that use needs.

### B.1.4:8.2 - SoTA-Echoing

For the question "which aggregate answers this receiving use?", B.1.4 adopts A.15.1:9.1's Work-interval distinction: union answers covered time, while convex hull answers elapsed span. C.27.TA:0 and :4.2 explain how to state the bearer, temporal reference and interval on which either calculation relies. The operation and its conditions, rather than a generic total or operator label, decide the result.

In the Work-interval case above, the same inputs give a justified 4-hour covered duration and a justified 5-hour elapsed span. Either can be sufficient for its question; using an unqualified total would hide which question was answered. The order-dependent calculation similarly distinguishes a usable partial-order specification from a unique numerical result that its permitted orders do not yet determine. Sections :2-:4 therefore require the rule, result kind and applicable conditions while allowing the ordinary sufficient answer.

The additional burden is recovering those inputs, rules and conditions; an inspectable record is needed only for a receiving use that consumes it. These constructed comparisons support the stated mathematical and subject distinctions. They do not establish empirical effectiveness or a ranking of external engineering notations. Reopen the operation or result choice when the receiving question, input identities, temporal reference, relation facts or applicable operation law changes.

### B.1.4:9 - Relations

- Builds on `B.1`, `A.14`, and `C.13` for part-whole, phase, and constructive grounding discipline.
- Coordinates with `C.2.1` for episteme identities and independently obtaining edition relations; with `A.3.1`, `A.3.2`, `A.15.2`, and `A.15.1` for method, method description, work plan, dated work occurrence, and Work-temporal relations.
- Coordinates with `B.1.6` for work-resource aggregation.
- Coordinates with `A.3.4` for transformation. Use `B.2` directly for a clear whole-reidentification question; use `B.2.P` first only when emergence-family wording hides the claim kind. The relevant subject pattern defines or constrains the recovered claim.
- Coordinates with `C.27.TA` for positive temporal-aspect facts and `C.27` for a separate temporal-claim adequacy question. Use `C.29` when mathematical representation-choice, transfer or reliance remains unresolved. `E.18` governs a selected transformation-flow structure; `E.18.2` governs its mathematical description or that of a selected TFS network.

### B.1.4:End
