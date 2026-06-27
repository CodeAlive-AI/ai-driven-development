## E.10.ARCH - Wording-Use Ontological Precision Restoration Architecture

> **Type:** Architectural (E)
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Wording ontology repair architecture.

**Intent.**
Keep FPF wording-use precision restoration distributed without letting every pattern of concern or subject pattern grow its own first-stage wording-recognition table. `E.10` recognizes overloaded wording use; `E.10.ARCH` says which applicability rows exist, how one row selects the first applicable restoration or governing pattern, and when repeated repair-only prose should be extracted from a subject pattern.

`E.10.ARCH` is not a generic language-cleanup pattern. Its mechanism is ontological reconstruction: recover what kind of thing is being talked about, which adjacent EntityOfConcern values, relation records, claim records, current ontic slots, relation positions, use relations, claim kinds, and FPF kinds named by value or references are admissibly involved, which relation, source-use disposition, or state-family value is current, and, when plain ontology is not enough, which mathematical lens under `C.29` or which pattern-defined formal apparatus makes the candidate structure checkable. The output returns to wording only after that kind, position, and use structure is recoverable. When the kind is recoverable but phrase-level apparatus still hides it, use `F.19` for ontology-first plain technical rewriting.

**Use this pattern when** a recurring wording-use problem hides stable ontological recovery work that should be shared instead of copied into each subject pattern.

**What goes wrong if missed.** Subject patterns accumulate local wording-repair catalogues and stop foregrounding their own governed object, invariant, and first useful move.

**What this pattern buys.** One distribution architecture keeps recognition in `E.10`, recovery architecture in `E.10.ARCH`, and object-specific ontology in the direct governing or realization pattern.

**Rationale.** Precision restoration needs an ontology-first distribution rule because a recurring trigger word may hide different kinds, slots, relations, claims, publications, or mathematical lenses in different places.

**SoTA-Echoing.** The pattern follows FPF's current ontology-first restoration practice: typed object recovery, direct governing-pattern use when available, and thin pointers in subject patterns instead of repeated repair doctrine.

**Builds on.** `E.10`, `A.6.P`, `A.6.F`, `C.2.P`, `C.2.P.DR`, `C.30.STRAT`, `A.19.SPR`, `A.6.3.CSC`, `A.3.1`, `A.3.2`, `A.6.0`, `A.6.1`, `E.20`, `E.24`, `E.24.CD`, `E.24.PUB`, `F.18`, `E.8`, `E.19`, and `E.2`.

**Coordinates with.** `A.22`, `C.30`, `C.30.P`, `C.30.STRAT`, `C.30.ASV`, named `C.30.*` structure or view patterns, `C.16`, `A.17`, `A.18`, `A.19`, `C.25`, `C.27.TA`, `C.27`, `C.29`, `A.3.1`, `A.3.2`, `A.3.3`, `A.3.4`, `A.6.0`, `A.6.1`, `E.18`, `E.20`, `E.24`, `E.24.CD`, `E.24.PUB`, `A.15.2`, `A.15.1`, `A.10`, `F.19`, `E.21`, `E.11`, `I.2`, and evidence, assurance, gate, work, decision, causal-use, release, and publication patterns governing those claims when those claims are being made.

### E.10.ARCH:0 - Use This When

Use this pattern when a recurring FPF-governed wording-use problem cannot be closed by one local `E.10` rewrite because the wording hides a stable primary-EntityOfConcern use field set, a stable recovery shape, and a useful remaining reader use.

**Early failure cue.** FPF accumulates many small local wording-recognition lists, and subject patterns start teaching repair doctrine instead of their own EntityOfConcern, invariants, and first useful move.

**Early gain cue.** `E.10.ARCH` gives one architecture for distributing wording-use repair: `E.10` recognizes the row, this pattern selects the recovery architecture, and the governing subject pattern stays centered on its own object.

Use it especially when a subject or adequacy pattern contains repeated first-stage repair prose such as:

- architecture-vs-diagram, model, graph, ADR, dashboard, view, layer, level, tier, stack, block, expert, cache, router, or gate triage before the architecture, structure, control, module-interface, flow, scale, publication, or gate pattern can state its own invariant;
- axis, dimension, feature, property, metric, indicator, score, strong, weak, robust, level, coordinate, threshold, or scalar-quality triage before a characteristic or scale pattern can state its own invariant;
- quality-term repair that decides between relation construction, quality characterization, evaluative characterization, Q-bundle use, pattern-quality coordinate use, action invitation, bridge, or governing pattern;
- state-family wording such as state, status, posture, readiness, stance, or currentness before the bearer, state frame, value set, admissible use, or governing pattern is recovered;
- admissibility-like, legal, lawful, authority, validity, readiness, pass-looking, fail-looking, or conformance wording before bearer, claim kind, source relation, value frame, bounded use, and direct governing pattern are recovered;
- method, algorithm, program, proof, solver, workflow, process, procedure, access path, query plan, control strategy, or programming-paradigm wording before its current ontic slot, relation position, use relation, or claim kind is recovered as method, method description, formal substrate, mathematical-lens use, mechanism, work plan, dated work, evidence relation, or quote-only source wording;
- relation, signature, interface, role, assignment, enactment, slot, field, parameter, argument, endpoint, port, API, protocol, connector, capability, affordance, method, function, concern, or interest wording before the current governed object or claim kind is recovered and before the direct governing pattern can carry the recovered claim;

- graph, path, query, table, dashboard, checklist predicate, publication face, evidence-path wording, or pattern-relation wording overread as a route, call, dispatch, invocation, work sequence, permission, release, evidence result, or pattern application;
- source, publication, publication form, face, `PublicationUnit`, dashboard, documentation, or source-return wording whose project-side use is not yet recovered;
- relation-like, function-like, evidence-like, assurance-like, gate-like, work-like, decision-like, causal-use, release, or naming wording whose governing pattern is already known or must be recovered before the sentence is admitted.

**Failure shape.** FPF accumulates many small local wording-recognition lists. One pattern says "architecture is not a diagram", another says "metric is not proof", another says "quality is not one scalar", another says "a path is not a route", and a reader cannot tell which pattern carries the repair. The text looks more precise, but the reader does not get a stable first move.

**Architecture gain.** `E.10.ARCH` gives one architecture for distributing wording-use repair: `E.10` recognizes the wording-use row; `E.10.ARCH` selects the row and extraction criterion; a realization pattern or governing neighboring pattern recovers the ontology; the governing subject pattern carries its own primary `EntityOfConcern` and first useful move.

**First useful move.** Decide whether the wording can close locally under `E.10`, already has a governing pattern, or needs one applicability row with stable `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, `ontologicalNeighborhood`, recovery apparatus, and remaining reader use.

**Not this pattern when.**

- If a sentence is repaired locally under `E.10`, stop there.
- If the governing pattern and primary `EntityOfConcern`, relation record, or claim record are already recoverable by value, use that governing pattern directly.
- If the kind under repair is evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens use, grounded architecture adequacy, structural-view adequacy, characteristic-space construction, Q-bundle construction, pattern-quality evaluation, method, mechanism, method description, formal substrate, graph path, evidence or provenance relation, publication face, or another FPF kind named by value, the governing pattern governs its own invariant. `E.10.ARCH` only governs the wording-use restoration distribution.
- If the wording problem is phrase-level apparatus around an already recoverable kind, use `F.19` rather than creating a new wording-use restoration row.

### E.10.ARCH:0.1 - Problem Frame

Precision restoration in FPF is ontology-first, not word-substitution-first. A recurring wording family is important only when it hides a stable governed object, relation position, claim kind, ontic slot, publication-use relation, source-use disposition, mathematical lens, or neighboring-pattern boundary.

### E.10.ARCH:0.2 - Problem

Without a shared distribution architecture, subject patterns collect first-stage repair catalogues and lose their object focus. The same false friend is then repaired differently in architecture, characteristic, evidence, publication, method, relation, and state-family patterns.

### E.10.ARCH:0.3 - Forces

| Force | Tension |
| --- | --- |
| Shared repair vs subject-pattern focus | FPF needs recurring trigger recognition, but each subject pattern must stay centered on its own EntityOfConcern. |
| Ontology-first repair vs lexical cleanup | The repair must recover kind, slot, relation, and use before choosing wording. |
| Direct governing pattern vs restoration detour | A direct pattern should govern when the object is already recoverable by value. |
| Local cue vs duplicated doctrine | Subject patterns may need one first-use cue, not a copied repair table. |
| Semantic area vs placement nest | A semantic area, ontological neighborhood, and pattern nest are different objects. |

### E.10.ARCH:0.4 - Solution

Use `E.10` for recognition, `E.10.ARCH` for the shared distribution architecture, and a direct governing or realization pattern for the recovered ontology. Add a new applicability row only when the recurring wording hides a stable field set, recovery apparatus, and remaining reader use that no direct governing pattern already carries.

### E.10.ARCH:1 - Primary EntityOfConcern and applicability-row scope

The primary `EntityOfConcern` for this pattern use is the local FPF architecture of `WordingUseRestorationApplicabilityRow` rows.

A `WordingUseRestorationApplicabilityRow` is a pattern-local row over one `semanticAreaBaseConcept`, one `semanticArea`, one `semanticAreaSenseFamily`, one recurring `entityOfConcernUseFields` field set, and one `ontologicalNeighborhood`. It states:

- the trigger source recognized by `E.10`;
- `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily`;
- the primary `EntityOfConcern` kind and encountered FPF kind or reference;
- the relation between the encountered FPF kind or reference and the primary `EntityOfConcern`;
- the FPF kind or relation named by value recovered when current;
- current-claim or admissible-use classification when current;
- source-use disposition when current;
- state-family value or governing-pattern result when current;
- sentence function;
- admissible use;
- non-use boundary;
- remaining reader use;
- first applicable restoration or governing pattern;
- recovery product;
- first return to the subject pattern.

`WordingUseRestorationApplicabilityRow` is not a `U.*` kind, not a conformance record, not a process task, not a deontic obligation, and not a durable project record by itself.

`WordingUseRestorationApplicabilityTable` is the pattern-local publication table of such rows. It is not a pattern cluster, workstream, campaign, module, semantic parent, or authority-bearing record.

`semanticAreaBaseConcept` is the Base concept, source-side phrase, or already settled row cue by which the reader first recognizes the candidate semantic unit.

`semanticArea` is the Part-F semantic unit used by one wording-use restoration row: one Concept-Set row, one UTS row, or an explicitly bounded row-set whose rows remain sense-uniform enough for one recovery apparatus.

`semanticAreaSenseFamily` is the Part-F `senseFamily` or FPF kind named by value-family discriminator that prevents the row from becoming a theme, domain, workstream, or pattern-nest label.

`ontologicalNeighborhood` means the FPF applicability neighborhood around that named `semanticArea`: primary `EntityOfConcern` kind, admissible adjacent FPF kinds or references, relations, descriptions, publication forms or carriers, source-use dispositions, state-family values, use boundaries, applicable FPF patterns, remaining reader use, and the stable apparatus that makes the recovery checkable. It is not the semantic unit by itself and is not textual proximity, filename proximity, ToC proximity, alphabetic proximity, workstream grouping, topic grouping, discipline column, domain label, or pattern-nest placement.

`pattern nest` means a numbering or placement grouping such as `A.6.*`, `C.16.*`, or `C.30.*`. One applicability row may point to a realization pattern in one pattern nest, but the row and the nest are not the same concept.

### E.10.ARCH:2 - Distribution architecture

The standing construction is:

1. `E.10` recognizes an FPF-governed wording use and either closes it locally or selects a governing pattern, controlled precision-reduction pattern, durable-name application, or fail-closed non-use disposition.
2. `E.10.ARCH` maintains the shared recovery algorithm and the `WordingUseRestorationApplicabilityTable`.
3. A realization pattern or retained governing pattern such as `A.6.RSIR`, `A.6.P`, `A.6.F`, `C.2.P`, `C.2.P.DR`, `C.30.P`, `C.30.STRAT`, `C.16.P`, `C.16.Q`, `A.19.SPR`, `A.3.1`, or a direct evidence, graph, method, mechanism, work, gate, authority, release, or publication-use governing pattern unpacks the wording according to the shared algorithm for one named `semanticArea` and its `ontologicalNeighborhood`.
4. Additional applicability rows, and only when needed additional realization patterns, appear when repeated FPF-governed wording hides a stable primary-EntityOfConcern use field set, a stable recovery shape, and a useful remaining reader use that no existing governing pattern already carries.
5. `E.8` governs publication-form and placement wording such as `pattern nest`, and requires authoring prose that uses `ontologicalNeighborhood` to expose the governing `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily` rather than treating neighborhood as the semantic unit.
6. `E.19` checks that authored pattern hosts preserve this distribution and do not keep rival first-stage repair doctrine.

This architecture keeps `E.10` compact. It also keeps subject patterns centered on their own primary EntityOfConcern values, decisions, characteristics, structures, mathematical lenses, consequences, and worked uses.

#### E.10.ARCH:2.1 - EntityOfConcern and recurring hidden-field distribution

For wording such as `EntityOfInterest`, `EoI`, `EoIClass`, `describedEntity`, `DescribedEntityRef`, and `primary described entity`, or for selected EntityOfConcern-family heads such as `EntityOfConcern`, `entityOfConcernRef`, `EntityOfConcernRef`, `EntityOfConcernClass`, and `publicationUnitPrimaryEntityOfConcern`, the repair is distributed by the current FPF-governed use:

`EntityOfInterest`, `EoI`, `EoIClass`, `describedEntity`, `DescribedEntityRef`, and `primary described entity` are active repair triggers. FPF-governed wording must recover the EntityOfConcern-family use named by value, publication-unit primary-EoC use, or local FPF kind, then rewrite to `EntityOfConcern`, `entityOfConcernRef`, `EntityOfConcernRef`, `EntityOfConcernClass`, `publicationUnitPrimaryEntityOfConcern`, or the local FPF kind named by value. If no use is recoverable by value, the wording remains quoted source or trigger wording and cannot be used for reliance.

- `C.2.1` carries the selected episteme slot and reference ontology: `EntityOfConcernSlot`, `entityOfConcernRef`, `EntityOfConcernRef`, `EntityOfConcernChangeMode`, and `EntityOfConcernClass`.
- `C.2.P` carries episteme, publication, and source-use precision restoration when the sentence still hides source wording, claim-bearing episteme, publication or publication-form construction, project-side reliance, pattern-application wording, or use or non-use disposition.
- `F.18` carries durable naming, selected head settlement, and source-string and durable-name discipline after the kind under repair and use are recovered.
- `E.17.AUD.OOTD` carries `publicationUnitPrimaryEntityOfConcern` for one bounded publication unit with one carried move and one outside-work boundary; it must not create a second C.2.1 slot.
- `A.6.3`, its retained `entityOfConcernRef`-preserving specializations, and `A.6.4` carry preservation or retargeting of the EntityOfConcern across episteme morphisms.
- Evidence, assurance, gate, work, decision, architecture, characteristic, mathematical-lens, or project-side patterns govern their own claim being made or admissible-use boundary directly when it is already recoverable.

This selected-family case is the standing example for recurring hidden-field architecture. When a new hidden-field family recurs, it is not solved by adding local warning prose to every subject pattern. It either uses an existing governing pattern, gets one applicability row in this table, or justifies a new realization pattern only when the hidden field set, recovery apparatus, and remaining reader use recur across FPF-governed texts.

#### E.10.ARCH:2.2 - Ontic-Level and Facet-Level Restoration Distribution

Use this distribution before adding or specializing a wording-use precision-restoration pattern.

`E.10` is the shared recognition scan. It recognizes an FPF-governed wording-use problem and selects the first applicable restoration or governing pattern. `E.10.ARCH` owns the distribution rule. A specialized restoration pattern owns only the stable ontological recovery for one selected ontic, semantic area, or high-pressure facet.

Use a direct governing pattern when the current kind, relation, claim, current ontic slot, relation position, use relation, or claim kind is already recoverable by value. A direct `A.3.4`, `A.6.F`, `C.29`, `E.18`, `C.30`, `A.15`, `A.10`, gate, decision, publication, or evidence use does not need a restoration detour only because a familiar trigger word appears.

`A.6.RSIR` is the selected first-level realization pattern for the relation-signature-interface-role-slot cluster. Use it only when wording such as relation, signature, interface, role, assignment, enactment, slot, field, parameter, argument, endpoint, port, API, protocol, connector, capability, affordance, method, function, concern, or interest hides which governed object or claim kind is current. The first-level product is not a new ontology; it is a compact recovery of project concern, current EntityOfConcern or claim kind, selected direct governing pattern, slot-discipline need, retained source-label use, and blocked overread. After that selection, the direct pattern owns the repair.


Use an ontic-level restoration pattern only when recurring wording hides a small ontic or ontic-neighborhood: several linked slots, adjacent governed fillers, and admissible neighboring patterns must be recovered before ordinary wording repair is possible. The pattern should recover the ontic, its current slot or filler, and the governing pattern that applies to the recovered value; it should not become a second copy of every slot-specific repair table.

Use `E.24.CD` only when the recurring wording may need an ontic candidate decision: the material clusters around one EntityOfConcern family, reusable slot relation, stable semantic area, ontological neighborhood, and action-facing gain that no direct governing pattern already carries. Use `E.24.PUB` only when the repair must distinguish ontic, ontic-description episteme, publication form, view, record, card, table, schema, data-structure expression, rendering, or source relation. If the subject ontology is already governed by a pattern such as `A.22`, `A.19`, `C.30`, `A.3.4`, or `C.2.1`, use that pattern directly and cite `E.24.CD` or `E.24.PUB` only as the relevant thin boundary reference.

Use a facet or slot-neighborhood restoration pattern
 only when one recurring facet cuts across several ontics or subject patterns and has its own stable ambiguity. Function-like wording under `A.6.F` is the standing example: function wording may point to transformation behavior, transformer-side bearer material, mathematical function, module allocation, capability, quality, role, work, method, evidence, assurance, gate, or decision. That facet is too broad to duplicate inside every ontic-level restoration pattern and too specific to leave as ordinary prose.

Do not create one precision-restoration pattern per slot. A slot gets a separate restoration pattern only when the same slot-neighborhood ambiguity recurs across several patterns, changes the governing FPF kind or relation, and would otherwise force subject patterns to carry repeated first-stage repair prose. Otherwise, keep the slot inside the governing ontic pattern or apply the direct governing pattern for the filled value.

When both an ontic-level restoration pattern and a facet restoration pattern are applicable, apply them by recovered question, not by word order. The ontic-level pattern asks which ontic, slot, filler, and neighboring governing pattern are current. The facet pattern asks how the overloaded facet word is assigned after that recovery. For example, transformation wording that includes `function`, `functional`, or `functioning` may use a transformation-ontic restoration pattern to recover `U.Transformation`, `TransformationFlowStructure`, transformer-side filler, input boundary, output boundary, or `FunctioningRef?`; detailed function-kind discrimination remains with `A.6.F`.

A conforming specialized restoration pattern states:

- the ontic, semantic area, or facet-neighborhood under repair;
- the recognition wording family selected by `E.10`;
- the recovered kind, current ontic slot, relation position, use relation, filler, claim kind, and governing pattern;
- any direct governing pattern that should apply instead when the value is already recoverable;
- any facet restoration pattern that owns a narrower recurring ambiguity;
- the temporary recovery product and the retained user-facing move after wording repair.

### E.10.ARCH:3 - Shared recovery algorithm

#### E.10.ARCH:3.1 - Method, work, and P2W governing-pattern constellation in wording restoration

Use this branch when one source label, project handle, or project concern points to changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern` rather than to one typed FPF value.

Do not name a new recovery object. Recover the project concern first only to find the linked relation positions. Then recover the typed FPF values separately through their governing patterns. Typical filled values include `U.Method`, `U.MethodDescription`, `U.Mechanism`, formal-substrate declaration, mathematical-lens use, `U.WorkPlan`, dated `U.Work`, evidence relation, source relation, gate relation, result relation, publication relation, and temporal relation when current.

When the recovered project concern is not one method but a relation among methods or method families, recover `MethodRelationStructure@BoundedContext`: serial composition, parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, selector relation, fallback relation, or another method-side relation. Govern it through `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern when current. Treat algebraic, graph, categorical, process-calculus, effect-calculus, matrix, embedding, distributed, or neural notation as `C.29` mathematical-lens use or method-description representation, not as `U.MethodAlgebra`.

This branch selects relation positions among already governed typed values. It publishes no new recovery object or super-kind; it only keeps the project concern, relation positions, and separately recovered FPF values from being collapsed into one umbrella value.

A compact local restoration note records how wording restoration found those typed values: affected entity, bounded context, change or maintained-condition statement, state or delta predicates when current, and references to the governing method, description, mechanism, work, evidence, source, gate, result, publication, or temporal patterns. If a project needs a project record, evidence record, gate record, method, work plan, work occurrence, or ontic, use that direct governing pattern instead of treating the restoration note as the project value.

Each filled reference remains governed by its own pattern. `A.15` carries the role-method-plan-work alignment part; `A.3.1`, `A.3.2`, `A.6.0`, `C.29`, `A.6.1`, `E.20`, `A.10`, gate, source, result, publication, temporal, and evidence patterns carry their own typed values. Do not assign one typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits that dual typing. Ontic-slot labels and relation-position labels do not create alternate ontology.

If a current `U.*` name in the constellation looks like only an ontic-slot label or relation-position label, apply `E.24`: retain the `U.*` name only when an existing governing pattern gives it standalone `EntityOfConcern` identity, stable identity criterion, and action-facing gain. If not, demote that use to a SlotKind or relation label rather than keeping the U-kind by inertia. If repeated method, work, and process material actually needs a durable ontic, open an E.24 ontic-introduction decision and write the governing head pattern before citing that ontic as current FPF ontology.
Use this recovery order for FPF-relevant wording-use restoration cases. Each realization pattern may publish a compact local form, but the order stays shared.

1. **Trigger and bounded text.** Name the bounded text span or publication unit, trigger span, local sentence function, register classification, and whether the text is conformant FPF, project text deliberately using FPF-governed terms, pattern references, relation names, or conformance claims, or source text being unpacked for possible FPF use.
2. **Cheap local closure.** Check whether the wording has no FPF-governed use or only a small local head, register, or morphology repair. If yes, repair locally under `E.10`, state the remaining reader use, and stop.
3. **Head kind and candidate ontology.** Recover the head kind, register classification, EntityOfConcern and Description-episteme boundary, specification-use gate when specification use is current, candidate referents, candidate EntityOfConcern values, relation records named by value, claim records, candidate relations, candidate ontic slots, candidate relation positions, candidate use relations, candidate carriers or publications, and scope, time, viewpoint, or context facets. Include literal and intended candidates when metonymy or compression is plausible.
4. **Semantic area, ontological neighborhood, and governing-pattern selection.** State `semanticAreaBaseConcept`, `semanticArea`, and `semanticAreaSenseFamily`; then select the `ontologicalNeighborhood` and first applicable governing pattern by primary `EntityOfConcern` kind and admissible adjacent FPF kinds, references, or relations: relation construction, function-like kind and relation recovery, episteme, publication, source-use, selected structure or architecture description, characteristic or scale construction, quality characterization, evidence, assurance, gate, work, decision, causal-use, naming, controlled coarsening, or another governing FPF pattern.
5. **Formal apparatus or stable substrate.** State the stable apparatus that makes the repair checkable: relation or signature slots under `A.6.0`, `A.6.5`, and `A.6.P`; publication relation set; source-use disposition; selected structure; architecture question; characteristic or scale construction; quality bundle; mathematical lens under `C.29`; evidence or provenance relation; gate record; work occurrence; decision record; assurance argument; causal-use record; or governing-pattern field set. When the same object is used in several relation, signature, or lens positions, record the object kind and current ontic slot, relation position, or use relation separately and cite the governing pattern; `E.10.ARCH` selects the restoration architecture rather than duplicating that pattern's ontology.
6. **Normalized ontology and lexical projection.** Produce the repaired wording, compact repair note, record-shaped value, governing-pattern application, or non-use disposition. Do not replace one umbrella word with another. The replacement candidate is itself a bounded wording use until it passes the `E.10` trigger scan or is demoted to ordinary wording, quote-only wording, reduced-use cue, blocked use, or incomplete rewrite.
7. **Admissible use and remaining reader use.** State the admissible use, non-admissible claim escalation or adjacent use, and one useful reader use. If the wording is type-correct but inert, the repair is incomplete.

Perform a terminology-source audit only when the wording imports a source ontology that can change the recovered object, kind, relation, current ontic slot, relation position, use relation, admissible use, or governing pattern. For slot-shaped material, use `E.24` slot-language unless a governing boundary or interface pattern makes interface meaning current. Do not turn stable ordinary prose into type annotation merely because the repair can name its ontology.

The sequence is shared; each wording-use restoration case differs by `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, primary `EntityOfConcern` use fields, current ontic slot, relation position, and use-relation field set, `ontologicalNeighborhood`, governing pattern, substrate, and result.

### E.10.ARCH:4 - Applicability table

| Semantic area and ontological neighborhood | First applicable pattern | Trigger family | Required recovery apparatus | Typical recovery product |
| --- | --- | --- | --- | --- |
| Relation construction; primary recoverable use is relation use or relation-bearing claim | `A.6.P` and retained A.6 relation specializations | Relation, endpoint, qualifier, slot, scope, time, viewpoint, evidence-use relation distinction when evidence use is current, basedness, service, bridge wording, whole or part, mapping, comparison, dependency, or evaluative ascription when the hidden claim is relation construction. | `RelationKind`, slot discipline, `QualifiedRelationRecord`, endpoint facets, qualifiers, L, A, D, and E hooks, and retained relation specializations named by value. | relation rewrite, relation record, candidate-set note, retained specialization application named by value, or fail-closed Plain disposition. |
| Relation-signature-interface-role-slot semantic area; primary recoverable use is hidden among relation, relation slot, signature, interface claim, role value, role assignment, role description, port, boundary claim bundle, neighboring candidate value, or reduced-use source label | `A.6.RSIR` when the direct governing pattern is not already clear; direct governing pattern when recovered by value | Relation, signature, interface, role, assignment, enactment, slot, field, parameter, argument, endpoint, port, API, protocol, connector, capability, affordance, method, function, concern, interest, role-holder grammar, or close source wording. | Project concern, current EntityOfConcern or claim kind, slot discipline under `A.6.5` when current, direct governing pattern selection, retained source-label use, blocked overread, and stop condition. Direct governing patterns include `A.6.P`, `A.6.5`, `A.6.0`, `A.2`, `A.2.1`, `A.15`, `A.6.M`, `A.6.F`, `A.6.A`, method, work, publication, evidence, status, gate, problem, and characteristic-space patterns named by value. | `RSIRRepairNote`, direct governing-pattern application, reduced-use source label, quote-only cue, blocked-use disposition, or stop. |
| Function-like wording; primary recoverable use is the FPF kind named by value, relation, or claim hidden by `function`, `functional`, `functionality`, `effect`, or similar wording | `A.6.F` first when the FPF kind named by value, relation, or claim is not already recovered; direct governing pattern when it is recovered by value | Functional architecture, required transformation or effect, method, work occurrence or result, role expectation, mathematical function, relation, loss, objective, quality or functionality claim, module allocation, interface or signature relation, or evidence, assurance, gate, or decision overread. | `FunctionUseRepair`, kind and relation recovery, false-kind list, governing-pattern reference, `C.30` or `C.30.ASV` functional-structure boundary, `C.29` mathematical-lens boundary, `C.16` or `C.25` quality boundary, `A.6.M` module-interface relations and A.6 signature or slot applications. | FPF kind or relation named by value assignment, governing-pattern application, `FunctionFlowModuleAlignmentNote`, mathematical-lens application, quality or characteristic application, `A.6.M` module-interface application, ordinary-prose demotion, or stop. |
| Episteme, publication, and source-use; encountered entity or construction may be source span, publication form, face, publication, `PublicationUnit`, EntityOfConcern-like head, old EntityOfConcern-family wording, or text-work evaluation cue | `C.2.P` first; evaluation pattern governing the recovered evaluation claim after recovery when the corresponding claim is being made | Source-expression, episteme or publication wording, FPF-governed wording, `EntityOfConcern` or `describedEntity`-family wording, and `reading`, `read`, or `quality-read` wording when the word could mean source interpretation, publication use, FPF-governed use, or evaluation hidden inside text work. | source-expression clarification, FPF-governed use, claim-bearing episteme, EntityOfConcern, publication, view, face, publication-form relation when that relation is being made, `PublicationUnit`, `publicationUnitPrimaryEntityOfConcern` when that publication relation is current, use disposition, project-side kind named by value or reference, sentence function, and evaluation claim or bundle named by value when current. | local rewrite, compact epistemic precision-restoration row, full check, recovered-by-value, reduced-use, blocked-use disposition, neighboring-pattern application, or evaluation-pattern application such as `E.22`, `E.21`, or `E.9.DA`. |
| Ontic candidate and publication-form confusion; primary recoverable use is a candidate ontic, slot relation, semantic area, ontological neighborhood, ontic-description episteme, or publication form hidden behind record, card, schema, table, data-structure, view, or source-material wording | `E.24.CD` for candidate detection; `E.24.PUB` for ontic-description and publication-form boundary; direct subject pattern when the ontic or governing pattern is already recovered | ontic, concept cluster, semantic area, ontological neighborhood, slot relation, slot-relation expression, schema, record, card, table, data structure, publication form, description, view, or source-material wording. | candidate EntityOfConcern, reusable slot relation, stable semantic area, ontological neighborhood, publication-form boundary, direct subject pattern, admissible use, blocked overread, and remaining reader use. | ontic-candidate note, direct `E.24` or subject-pattern application, `E.24.PUB` boundary note, ordinary-prose demotion, quote-only cue, reduced-use cue, blocked-use disposition, or stop. |
| Admissibility-like, legality-like, authority, validity, readiness, pass-looking, fail-looking, and conformance wording; primary recoverable use is bearer, claim kind, source relation, value frame, bounded use, and governing pattern, not a generic admissibility object | Direct governing pattern when the claim is recoverable by value; `A.19.SPR` only when a hidden state-family bearer and value frame are the problem; `A.6.P` only when relation construction is hidden | `admissible`, `lawful`, `legal`, `legality`, `allowed`, `permitted`, `authorized`, `valid`, `pass`, `fail`, `ready`, `conformant`, `eligible`, and close compounds. | bearer, claim kind, source relation, value frame, admissible use, non-admissible overread, validity window or reopen condition when current, and direct governing pattern for mechanism admissibility predicate, signature applicability, evidence, assurance, gate, work, decision, authority-bearing record, release, temporal validity, or source-use disposition. | direct governing-pattern application; state-family repair note only when hidden state wording is current; recovered gate, evidence, authority, temporal, mechanism, or source-use boundary; quote-only cue; reduced-use cue; blocked-use disposition; or stop. |
| Method, algorithm, program, solver, proof, recipe, workflow, process, procedure, access path, query plan, control strategy, method algebra, method graph, selector calculus, or programming-paradigm wording; primary recoverable use is a current ontic slot, relation position, use relation, claim kind, or method relation structure in the method-description-work-mechanism chain | `A.3.1` first when method-like wording hides the slot, relation position, use relation, claim kind, or method relation structure; direct governing pattern after recovery; `C.2.P.DR` first when representation overread is the current problem | algorithm, program, solver, proof, recipe, method, workflow, process, procedure, access path, query plan, control strategy, imperative, functional, logical, constraint, object-centric event, effect-handler, pipeline, orchestration, method algebra, method graph, selector calculus, fallback composition, or similar wording. | current ontic slot, relation position, use relation, claim kind, or method-side relation: context-local semantic way of doing (`A.3.1`), `MethodRelationStructure@BoundedContext` when composition, refinement, substitution, iteration, guarded choice, decomposition, parameterization, method-family membership, selector relation, or fallback relation is current, episteme describing a method or method relation structure (`A.3.2`), formal-substrate declaration (`A.6.0`) and mathematical-lens use (`C.29`) when current, mechanism declaration or realization governed by `A.6.1` and `E.20`, planned work (`A.15.2`), dated work (`A.15.1`), method-family registry or selector outcome (`G.5`), evidence relation (`A.10`), source relation, gate relation, result relation, direct governing pattern, or quote-only source wording. If one source label or project-side name points to changing, producing, selecting, deriving, controlling, or maintaining an `EntityOfConcern` rather than to one typed value, use the existing method, work, and P2W governing-pattern constellation through `E.10.ARCH:3.1`; then recover linked typed FPF values separately. Do not assign the same typed value as both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits such dual typing. Do not mint `U.MethodAlgebra`; algebraic or graph notation is a lens or representation unless the governing pattern states a different object by value. Ontic-slot labels and relation-position labels do not create alternate ontology. | `U.Method` statement, `MethodRelationStructure@BoundedContext` statement, `U.MethodDescription` relation, formal-substrate or mathematical-lens application, `U.Mechanism` or MIP application, WorkPlan or Work application, G.5 selector or registry application, evidence relation, source relation, gate relation, or result relation, direct governing-pattern application, quote-only cue, reduced-use cue, blocked-use disposition, or stop. |
| Declarative representation and imperative-metaphor overread; primary recoverable use is a representation, relation, predicate, graph object, publication face, evidence relation, or pattern relation being treated as action, route, call, dispatch, permission, release, work, or evidence result | `C.2.P.DR` when no direct governing pattern already closes the claim; direct governing pattern when recovered by value | graph path, `PathSlice`, flow valuation, state predicate, checklist predicate, SQL-like query, table, dashboard, publication face, evidence-path wording, pattern relation, representation, route, path, workflow, lifecycle, dispatch, exit, receiver, call, invoke, run, flow, send, move, or `EvidencePath` wording. | encountered representation, representation kind, represented object or claim, source-expression or publication relation when current, tempting imperative overread, recovered governing pattern, admissible use now, non-admissible overread, stop or reopen condition, and graph, evidence, publication, method, work, gate, or authority pattern named by value when current. | `DeclarativeRepresentationRepair`, graph or path application under `E.18`, evidence or provenance relation under `A.10`, state-family repair under `A.19.SPR`, publication-face use under `E.17`, mathematical-lens use under `C.29`, method, method-description, work, gate, or authority direct application, quote-only cue, reduced-use cue, blocked-use disposition, or stop. |
| Architecture and structure; primary recoverable use is selected structure, `ArchitectureOf@Context` relation, conditional `ArchitectureDescription@Context` use, structural view, or named C.30 subcase | `C.30.P` | Architecture-heavy or structure-heavy wording whose EntityOfConcern under repair, relation, or claim is not yet recoverable. | `A.22` selected structure and structural-view discipline, `C.30` `ArchitectureOf@Context`, `C.30.ASV` structural-view and structure-kind discipline, named C.30 subpattern applications, and `C.30.AD` only when full architecture-description mechanism is current. | architecture-structure repair note, repaired wording, selected-structure naming, architecture question, source-return condition, governing-pattern result, ordinary-prose demotion, or stop. |
| Stratification and source labels; primary recoverable use is hidden behind `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, `gate`, or close engineering source labels | `C.30.STRAT` when the governing pattern is not already recovered; direct governing pattern when it is recovered by value | Engineering, mathematical, publication, project, control, module, neural-network, or architecture prose uses a source label as if it named the FPF kind directly. | Source label, literal source wording, candidate primary EntityOfConcern, recovered FPF kind, recovered relation, recovered claim-use, recovered source-use disposition, governing-pattern selection, admissible use, non-use boundary, and adjacent governing-pattern applications to `C.30.P`, `C.30.LCA`, `A.6.M`, current Architecture Transformation-Flow Structure Relation (`C.30.TFS-REL`), `E.18`, `C.16.P`, `C.29`, `C.2.P`, gate, work, or decision patterns, or ordinary source label. | `StratificationSourceLabelRepairNote`, direct governing-pattern application, ordinary-prose demotion, quote-only, reduced-use, or blocked-use disposition, or stop. |
| Characteristic and scale; primary recoverable use is characteristic, scale, coordinate, score, comparison, indicator role, or characteristic-space construction | `C.16.P` | Characteristic, scale, coordinate, value, score, indicator, threshold, comparison, metric, axis, dimension, feature, property, level, strong, weak, robust, or benchmark wording whose construction is not yet recoverable. | `A.17` Characteristic, `A.18` CSLC, `C.16` measurement, unit, evidence stub, `A.19` `CharacteristicSpace`, `C.25` Q-bundle, `C.29` mathematical-lens boundary, and `E.21` pattern-quality coordinate discipline. | characteristic-scale repair note, declared `Characteristic`, `Scale`, `Coordinate`, `Value`, and `Score` construction, non-comparability, non-measurement, blocked-gate disposition, governing-pattern result, ordinary-prose demotion, or stop. |
| Quality characterization and evaluative characterization; primary recoverable use is quality characterization, Q-bundle use, or pattern-quality coordinate use | `C.16.Q` | Quality or evaluative characterization wording when the hidden claim is not relation construction. | `C.16.P` where bearer or scale construction is hidden, `C.25` Q-bundle, `E.21` pattern-quality coordinates, and characterization or relation applications named by value. | quality-term repair note, quality-bundle or pattern-quality coordinate use, relation or bridge split when current, blocked scalar, gate, or release overread, governing-pattern result, ordinary-prose demotion, or stop. |
| State-family hidden claim; primary recoverable use is a bearer with a state-like value, status, readiness, currentness, or local finite field whose frame is hidden | `A.19.SPR` | State, status, posture, readiness, stance, currentness, validity, stable, accepted, blocked, candidate, admissible, ready, degraded, or close state-family compounds. | bearer kind, state frame or governing pattern, value set or classification source, admissible use, non-admissible overread, validity window or reopen condition, and direct governing-pattern application for source, evidence, assurance, gate, work, decision, temporal, lens-use, pattern-quality, or process cases. | state-family repair note, retained local field with bearer, value set, and admissible use named by value, direct governing-pattern application, quote-only cue, reduced-use cue, blocked use, ordinary-prose demotion, or stop. |
| Neighboring claim or admissible-use boundary already recoverable by value | Evidence, assurance, gate, work, decision, causal-use, release, mathematical-lens, naming, controlled-coarsening, action-invitation, `A.6.M` module-interface, or another governing-pattern application | Any trigger family whose recovered FPF kind, relation, claim-use, source-use disposition, or admissible-use boundary is already recoverable by value. | The governing pattern's own ontology and conformance fields. | Direct governing-pattern application; no detour through a new restoration pattern. |

### E.10.ARCH:5 - Direct known governing-pattern rule

If the governing pattern and its primary `EntityOfConcern`, relation record, claim record, current ontic slot, relation position, use relation, or claim kind are already recoverable by value, use that governing pattern directly. Do not put direct `C.30`, `C.16`, `C.29`, `E.21`, `E.18`, `A.10`, `A.3.1`, `A.3.2`, `A.6.0`, `A.6.1`, `E.20`, evidence, assurance, gate, work, decision, causal-use, release, naming, controlled-coarsening, action-invitation, `A.6.M` module-interface, publication-face, or mathematical-lens cases through a restoration pattern only because a familiar trigger word appears.

Apply `A.6.RSIR`, `A.6.P`, `A.6.F`, `C.2.P`, `C.2.P.DR`, `C.30.P`, `C.30.STRAT`, `C.16.P`, `C.16.Q`, `A.19.SPR`, or `A.3.1` only when wording hides the EntityOfConcern under repair, relation, role assignment, signature, interface claim, slot, characteristic, scale, score, quality characterization, comparison reference set, source-use disposition, state-family value, method-like slot, declarative-representation use, admissible use, or remaining reader use.

### E.10.ARCH:6 - Admission and extraction criterion

Add or retain a `WordingUseRestorationApplicabilityRow` when all of the following are true:

- the wording recurs across FPF-governed texts or project text deliberately using FPF-governed terms, pattern references, relation names, or conformance claims;
- the hidden primary-EntityOfConcern use field set is stable;
- the recovery apparatus or field set is stable enough to teach;
- repeated in-place repair distracts from the subject pattern's primary EntityOfConcern and first useful move;
- a useful remaining reader use survives after overread removal;
- no existing governing pattern already carries the row without duplicating repair-only doctrine inside subject patterns.

Do not add a new realization pattern when an existing governing pattern such as `A.6.F`, `A.6.A`, `A.6.M`, `A.15.4`, `A.6.6`, `A.6.3.CSC`, `A.10`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.28`, or another governing pattern already carries the EntityOfConcern under repair, relation, claim, or field. Record that pattern as the `governingPattern`.

Extract repair-only material from a subject pattern when the material is only wording-recognition lists, false-friend rows, anti-umbrella prose, or repair fields that must run before the subject pattern can state its own invariant. Leave a narrow first-use cue or governing-pattern relation in the subject pattern.

Keep material in the subject pattern when it states the subject pattern's own invariant, worked case, conformance condition, characteristic construction, structural construction, mathematical lens, source-return condition, or user action.

### E.10.ARCH:7 - Subject-pattern thin-pointer rule

Subject patterns keep at most one local first-use cue when the EntityOfConcern under repair, relation, claim, or field is hidden, then name the selected precision-restoration pattern as a pattern through ordinary references or `Relations`. They do not turn that reference into local reference boilerplate, and they do not copy:

- the full `E.10` wording-recognition table;
- this shared algorithm;
- the `WordingUseRestorationApplicabilityTable`;
- broad false-friend lists whose only job is first-stage repair;
- past placement or repair history written in place of current architecture prose.

A thin pointer is acceptable when it helps the working reader choose the right first move, for example:

- use `C.30.P` when architecture or structure wording hides whether the use under repair is selected structure, architecture-description use, structural-view use, source, model, diagram, graph, dashboard, or ordinary prose;
- use `C.30.STRAT` when `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, `gate`, or a close source label hides whether the use under repair is a control-layer relation, module-interface relation, architecture-to-`TransformationFlowStructure` relation, scale or coarse-graining relation, publication relation set, gate relation, neighboring use named by value, ordinary source label, quote-only cue, or blocked use;
- use `C.16.P` when metric, score, axis, dimension, feature, property, indicator, strong, weak, robust, level, coordinate, threshold, or comparison wording hides characteristic or scale construction;
- use `C.16.Q` when quality or evaluative characterization wording hides Q-bundle, pattern-quality coordinate, relation construction, action-invitation, bridge, or characterization use named by value;
- use `A.19.SPR` when state, status, posture, readiness, stance, currentness, or a local state-like field hides bearer, state frame, value set, admissible use, or governing pattern;
- use `C.2.P` when source, publication, publication form, face, `PublicationUnit`, dashboard, documentation, or text-work wording hides source-currentness relation or project-side reliance;
- use `A.3.1` when method, algorithm, program, proof, solver, workflow, process, procedure, access-path, query-plan, control-strategy, method-algebra, method-graph, selector-calculus, or programming-paradigm wording hides whether the current slot is method, method relation structure, method description, formal substrate, mathematical-lens use, mechanism, work plan, dated work, evidence relation, or quote-only source wording;
- use `A.6.RSIR` when relation, signature, interface, role, assignment, enactment, slot, field, parameter, argument, endpoint, port, API, protocol, connector, capability, affordance, method, function, concern, or interest wording hides the current governed object or claim kind and no direct governing pattern is yet clear;

- use `C.2.P.DR` when a declarative representation, graph relation, evidence-path wording, publication face, checklist predicate, query, dashboard, or pattern relation is being overread as an imperative route, call, dispatch, work sequence, permission, release, evidence result, or pattern application;
- use the direct governing pattern, with `A.19.SPR` only when hidden state-family wording remains, when admissibility-like, legal, lawful, validity, pass-looking, fail-looking, readiness, conformance, or authority wording already recovers its bearer, claim kind, source relation, value frame, and admissible use.

### E.10.ARCH:8 - Name and placement discipline

`semanticArea` is the selected Part-F Tech term for the semantic unit used by a wording-use restoration row. Plain speech may say "semantic area" or "meaning area" only as a gloss for that declared Part-F row or bounded row-set.

`meaning area`, `theme`, `pattern area`, `pattern cluster`, `workstream`, `campaign`, `module`, and `branch` are not selected as Tech architecture terms for this distribution. Tech prose must resolve those cues into `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, `entityOfConcernUseFields`, `ontologicalNeighborhood`, `governingPattern` named by value, and realization pattern.

`pattern nest` is allowed for ID and placement grouping such as `A.6.*`, `C.16.*`, or `C.30.*`. It is not a semantic parent relation and not an authority relation.

`SelectedLocusObligationClosure` is the current `E.9.DA` coordinate name for selected-locus obligation closure. Do not reintroduce `ReceivingLocusObligationClosure` as a general obligation kind, locus kind, pattern role, or restoration vocabulary.

### E.10.ARCH:9 - Examples and near misses

| Wording | Applicable result | Blocked overread |
| --- | --- | --- |
| "The architecture is the diagram." | `C.30.P` recovers whether the diagram is publication form, structure view, architecture description, source relation, or ordinary source cue; then `C.30` or `C.30.ASV` applies only after the selected architecture or structural-view use is recovered. | diagram-as-architecture; diagram-as-proof; diagram-as-gate. |
| "`ArchitectureOf@PlantOps` is defined over structures S1 and S2 under context C." | Direct `C.30`; no `C.30.P` unless selected structure, architecture-description use, structural-view use, source use, model use, diagram use, graph use, dashboard use, or ordinary prose remains hidden. | unnecessary restoration detour. |
| "The model has three layers." | `C.30.STRAT` treats `layers` as a source label until the recovered FPF kind, relation, claim-use, or source-use disposition is recovered: control-layer relation, neural-network block sequence, publication relation set, mathematical scale or coarse-graining relation, or ordinary source wording. Then the governing pattern applies to the recovered result. | layer-as-universal-kind; source label as proof of structure. |
| "The query plan calls the next pattern." | `C.2.P.DR` recovers whether the query plan is a representation, method description, formal substrate, evidence or provenance relation, or ordinary source wording; if a pattern relation is current, the relation is stated declaratively rather than as a call. | query-as-work sequence; pattern relation as invocation. |
| "The evidence path authorizes release." | If a provenance relation for a claim is current, use `A.10`; if authorization or release is current, use the authority, gate, or release pattern. `C.2.P.DR` applies only when `path` wording turns the relation into an action route or permission. | evidence path as permission; graph relation as release. |
| "The solver algorithm is the mechanism." | `A.3.1` first recovers whether the current slot is method, method description, formal substrate, mathematical-lens use, mechanism declaration or realization, work, evidence, or quote-only wording. Use `A.6.1` and `E.20` only when operation algebra, laws, admissibility predicates, transport, audit, or governing-definition assignment is current. | algorithm-as-default-method; method-as-mechanism by vocabulary. |
| "This record is admissible." | Recover bearer, claim kind, source relation, value frame, admissible use, and governing pattern. Use `A.19.SPR` only if hidden state-family wording remains; otherwise use the direct evidence, gate, mechanism, temporal, authority, release, or source-use pattern. | admissible-as-generic status; pass-looking word as gate. |
| "This score proves readiness." | `C.16.P` recovers characteristic, scale, value, score, threshold, comparison reference set, and gate, evidence, and decision pattern applications. | score-as-proof; score-as-release permission. |
| "This source supports the claim." | `C.2.P` is used if source-currentness relation or publication relation set is current; relation slice applies `A.6.P`; final use states recovered relation or non-use disposition. | source-as-proof; support-as-generic relation. |
| "Quality improved." | `C.16.Q` recovers quality characterization or evaluative characterization, or names the `C.16.P`, `C.25`, `E.21`, `A.6.P`, action, work, or bridge pattern application governing the recovered claim. | quality-as-one scalar; quality-as-gate. |
| "The function improved maintainability." | `A.6.F` first recovers the FPF kind named by value, relation, or claim when hidden; quality or maintainability wording is then governed by `C.16.P`, `C.16.Q`, `C.25`, or the quality pattern governing the current claim. | function-as-default-architecture; maintainability-as-unscaled verdict. |
| "Read this pattern for improvement proposals." | Recover whether the current FPF-governed use is source-publication use, bounded comparative review unit, or improvement-oriented evaluation. Use `E.22` only for improvement-oriented quality review under a declared pattern-under-improvement evaluation. | generic reading as a pattern. |
| "This summary is enough for action." | `E.10` checks whether the wording is precision restoration or controlled precision reduction. If coarsened source-to-rendering use is current, `A.6.3.CSC` names source-bearing side, loss mode, narrower admissible use, non-admissible downstream use, and reopen condition. | summary-as-full source; coarsening without declared loss. |

### E.10.ARCH:9.1 - Archetypal Grounding

| Situation | E.10.ARCH move | Boundary |
| --- | --- | --- |
| Architecture text repeatedly says diagrams, ADRs, dashboards, and views are not architecture. | Use the architecture/structure row and `C.30.P`/`C.30.AD` boundary. | C.30 remains about architecture and selected structures, not a generic diagram-warning pattern. |
| Method text uses algorithm, workflow, solver, proof, and program as one family. | Use the method/work/P2W constellation row and recover method, method description, formal substrate, mechanism, work plan, dated work, or evidence relation separately. | Do not assign one typed value to several kinds because one source label was shared. |
| A dashboard or evidence-path wording is treated as permission or release. | Use the declarative-representation row or the direct evidence, gate, authority, or release pattern. | Graph and provenance relations remain legitimate when they are not overread as routes, calls, permissions, or releases. |

### E.10.ARCH:9.2 - Bias-Annotation

This pattern blocks semio-bias in two directions. It prevents subject patterns from becoming patterns about descriptions, records, and wording guards. It also prevents word-replacement bias by requiring recovery of the ontological neighborhood, direct governing pattern, and admissible reader use before a new term is selected.

### E.10.ARCH:10 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-E10ARCH-1` | `E.10` remains the compact trigger-and-applicability pattern; `E.10.ARCH` carries the shared algorithm and applicability-row architecture. |
| `CC-E10ARCH-2` | Each `WordingUseRestorationApplicabilityRow` names `semanticAreaBaseConcept`, `semanticArea`, `semanticAreaSenseFamily`, primary EntityOfConcern kind and use fields, `ontologicalNeighborhood`, first applicable restoration or governing pattern, recovery product, non-use boundary, and remaining reader use. |
| `CC-E10ARCH-3` | Direct known governing-pattern cases use the governing pattern directly instead of creating a restoration detour. |
| `CC-E10ARCH-4` | A new realization pattern is added only when no existing governing pattern carries the stable recovery shape without duplicating repair-only doctrine inside subject patterns. |
| `CC-E10ARCH-5` | Subject patterns of concern keep their primary `EntityOfConcern` and first useful move central and carry only thin first-use cues to precision restoration when wording is hidden. Generic guards about description and publication use are kept in a named description and publication-use boundary section or description-publication pattern governing that use; they do not become the subject Solution. |
| `CC-E10ARCH-6` | `reading`, `read`, and `quality-read` wording remains trigger wording and does not mint `ReadingPrecisionRestoration`. |
| `CC-E10ARCH-6a` | EntityOfConcern-like hidden fields follow the selected distribution: `E.10` recognizes the wording-use row, `C.2.1` carries slot and reference ontology, `C.2.P` restores episteme, publication, and source-use wording, `F.18` settles durable heads and source-string decisions, `E.17.AUD.OOTD` carries publication-unit primary entity of concern, and governing patterns carry their own claim being made or admissible-use boundary. |
| `CC-E10ARCH-6b` | State-family wording follows the selected distribution: `E.10` recognizes the wording-use row, `A.19.SPR` realizes recurring hidden bearer, state-frame, value, and use recovery, and governing patterns carry already-recovered evidence, assurance, gate, work, decision, temporal, mathematical-lens, pattern-quality, source-use, or process cases directly. |
| `CC-E10ARCH-6c` | Stratification and source-label wording follows the selected distribution: `E.10` recognizes the wording-use row, `C.30.STRAT` realizes recurring source-label repair, and governing patterns carry already-recovered control-layer, module-interface, architecture-to-`TransformationFlowStructure`, scale or coarse-graining, publication relation set, gate, work, decision, or ordinary non-use cases directly. |
| `CC-E10ARCH-6d` | Admissibility-like, legal, lawful, validity, pass-looking, fail-looking, readiness, conformance, and authority wording does not mint a generic admissibility object. The repair recovers bearer, claim kind, source relation, value frame, admissible use, non-admissible overread, and the direct governing pattern; `A.19.SPR` is used only when hidden state-family wording remains. |
| `CC-E10ARCH-6e` | Method-like and algorithm-like wording first recovers the project concern and then recovers separately governed typed values through the existing method, work, and P2W governing-pattern constellation. `A.3.1` governs the semantic way of doing, `A.3.2` governs descriptions of that way, `A.6.0` and `C.29` govern formal-substrate and mathematical-lens use, `A.6.1` and `E.20` govern mechanism meaning, and work, plan, evidence relation, source relation, gate relation, result relation, or quote-only cases go to their direct governing patterns. One source label may link several typed values, but no typed value is both `U.Method` and `U.Mechanism` unless a governing pattern explicitly admits dual typing. Slot-position labels do not create alternate ontology. |
| `CC-E10ARCH-6f` | Declarative representation overread follows `C.2.P.DR` unless a direct graph, evidence, publication, method, work, gate, authority, or pattern-relation pattern already governs the recovered claim by value. Graph paths remain legitimate graph relations when that is the current claim; evidence-path wording is legitimate only after recovery as an evidence or provenance relation. They become repair triggers when read as routes, calls, dispatches, permissions, releases, work sequences, or evidence results by metaphor. |
| `CC-E10ARCH-6g` | Terminology-source audit is bounded: source-ontology labels are recovered when they affect object, kind, relation, current ontic slot, relation position, use relation, admissible use, or governing-pattern selection; otherwise stable ordinary prose stays ordinary. Slot-shaped material follows `E.24` slot-language, and `interface` is used only under a governing boundary, module-interface, signature, port, publication, or source-label disposition. |
| `CC-E10ARCH-6h` | Relation-signature-interface-role-slot wording follows the selected two-level architecture: `E.10` recognizes the trigger row, `E.10.ARCH` places the row, `A.6.RSIR` recovers project concern and current EntityOfConcern or claim kind only until a direct governing pattern is clear, and the direct pattern owns the final repair. Do not mint generic `U.Interface`, a standalone role-slot ontic, `U.Concern`, `U.Interest`, or episteme-role ontology. |

| `CC-E10ARCH-7` | `function`, `functional`, `functionality`, and `effect` wording keeps `A.6.F` as first unpacker when the FPF kind named by value, relation, claim record, view, or governing-pattern application is hidden and does not default to architecture. |
| `CC-E10ARCH-8` | `semanticArea`, `ontologicalNeighborhood`, and `pattern nest` follow `E.8` placement discipline: `semanticArea` is the Part-F semantic unit, `ontologicalNeighborhood` is its applicability neighborhood, and `pattern nest` is placement. None of them becomes workstream, campaign, module, or authority-bearing record. |
| `CC-E10ARCH-9` | Repair removes overread and preserves one useful admissible reader use. Type-correct but inert wording is not recovered by value. |
| `CC-E10ARCH-10` | Validation checks cover duplicate wording-recognition tables, stale quality-term-restoration links, broad `U.*` heads, shadow restoration apparatus, and entry or index drift. |

### E.10.ARCH:11 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Classification without repair | The text says "this belongs under `A.6.P`" or "this belongs under `C.2.P`" but leaves no recovered wording, record, source-use disposition, direct governing-pattern application, or blocker. | Apply the selected pattern or fail closed. |
| Trigger registry copying | `E.19`, `C.30.P`, `C.16.P`, `C.16.Q`, or a subject pattern copies the full `E.10` trigger list. | Keep one thin cue in the subject pattern of concern and cite `E.10` and `E.10.ARCH` through ordinary references or `Relations`. |
| Umbrella-to-umbrella replacement | `support` becomes `basis`, `surface` becomes `view`, `reading` becomes `evaluation`, or `function` becomes `role` without recovered kind and use. | Recover kind, relation, apparatus, admissible use, and remaining reader use; otherwise demote or block. |
| Source-ontology smuggling | `interface`, `schema`, `record`, `profile`, `path`, or another familiar source-domain word is used because it sounds precise, but the recovered slot, relation, boundary, or object kind is different. | Recover the source ontology and the FPF current ontic slot, relation position, use relation, or claim kind first; keep the source word only when its governing pattern makes that meaning current. |
| Over-annotated restoration | A clear subject sentence is expanded into type labels or source-ontology commentary even though no object, kind, relation, slot, admissible use, or governing pattern changes. | Keep the ordinary wording; annotate only the claim-governing term under repair and use `F.19` if phrase apparatus remains. |
| Sterile precision | The wording is ontologically well-formed but no working reader can tell why the distinction matters or what reader use remains. | Restore the didactic or recognition function in admissible wording, or classify as reduced-use cue, quote-only, blocked use, or incomplete rewrite. |
| Shadow precision-restoration pattern | A subject pattern contains its own first-stage repair algorithm beside this distribution. | Extract repair-only material to the applicable realization pattern and leave a first-use cue. |
| Reference boilerplate in subject pattern | A subject pattern explains where the repair belongs, why the package was split, or what this text does not contain instead of stating the subject pattern's own repaired wording or first move. | Move architecture-placement rationale to `DRR` or architecture notes; replace routing prose with a normal pattern id, citation, or `Relations` row. |
| Apparatus-preserving paraphrase | A repair changes wording but keeps phrase-level apparatus around a recoverable kind. | Apply `F.19` first; return to `E.10.ARCH` only for remaining word, head, or use precision. |
| History placement as pattern prose | Past placement or old naming text explains history instead of current use. | Keep only current entry or repair rows where needed; write current pattern prose in the selected placement. |

### E.10.ARCH:9.3 - Consequences

**Benefits.** Wording-use restoration stays distributed but coherent; subject patterns stay object-centered; recurring hidden-field families get one recovery architecture instead of many local catalogues.

**Costs.** Authors must decide whether the current case is local `E.10`, a direct governing pattern, an existing restoration row, or a new row with a stable recovery shape.

**Risks avoided.** The main avoided risks are semio-bias in subject patterns, lexical substitution without kind recovery, and pattern-nest or placement language masquerading as semantic-area architecture.

### E.10.ARCH:2a - Rationale

This distribution is selected because the recurring failure is not "too few word rules". The failure is that repair-only trigger prose migrates into subject patterns and begins to compete with their primary `EntityOfConcern` and first useful moves. A common symptom is a non-semio pattern whose Solution mainly teaches that a description, view, publication, record, card, diagram, source, or file is not a permission, promise, prescription, evidence record, assurance verdict, decision, gate passage, release, work occurrence, or authority source. Those guards are often correct, but their ontology is publication pragmatics, description pragmatics, and neighboring-pattern assignment, not the subject matter of the architecture, method, role, evidence, or characterization pattern. A workable FPF answer therefore needs three separations at once: a cheap shared trigger scan in `E.10`, a shared recovery architecture in `E.10.ARCH`, and local realization only where a named `semanticArea` has stable row identity, a stable field set, an `ontologicalNeighborhood`, and a remaining reader use.


### E.10.ARCH:2a.1 - SoTA-Echoing

| Source or practice line | Source-use function or relation | What the line changes in `E.10.ARCH` |
| --- | --- | --- |
| Current FPF distribution: `E.10`, `E.10.ARCH`, `A.6.P`, `A.6.F`, `C.2.P`, `C.30.P`, `C.30.STRAT`, `C.16.P`, `C.16.Q`, `A.19.SPR`, `F.18`, `E.8`, `E.19`, `E.11`, and `I.2`. | Current FPF-internal architecture source line for the selected distribution. | Keeps `E.10` compact, puts the shared recovery algorithm in `E.10.ARCH`, assigns relation, source-use, architecture, stratification-source-label, characteristic, quality, state-family, function-like, naming, entry-distribution, and expanded entry-disambiguation cases to realization or governing patterns named by value, and gives `E.19` a distribution-preservation check. |
| Pattern-language locality and FPF primary-EntityOfConcern discipline in `E.8` and `E.19`. | Current FPF authoring and review source line; not an external standard imported as ontology. | Forces thin governing-pattern pointers and blocks local wording-recognition-table copies inside patterns of concern whose real work is architecture, structure, characteristic, quality, evidence, gate, work, decision, state-family precision, or release. |
| Terminology and controlled-vocabulary practice named in `E.10:11a` only where it concerns designations, labels, discoverability, and controlled vocabulary publication. | Current-standard and reference-use source line; it does not define FPF kind ontology. | Provides explicit recovered heads and reusable-name discipline, but rejects a central word list or controlled vocabulary as the solution to every wording-use repair. |
| Current governing-pattern coverage in FPF. | Applicability boundary for this architecture, not evidence that E.10.ARCH owns every wording-use case. | Uses the direct governing pattern when that pattern can carry the EntityOfConcern under repair, relation, claim, or local field directly; reopens E.10.ARCH only when the shared distribution rule itself no longer fits. |

The selected architecture is lowered or reopened when one of those source lines changes: if `E.10` can close the issue locally, if a new governing pattern removes the need for a restoration row, if a realization pattern needs a different stable field set, or if subject patterns again start carrying duplicated first-stage trigger registries.

### E.10.ARCH:12 - Relations

- `E.10` recognizes and closes local wording issues or selects the applicable row.
- `A.6.RSIR` realizes first-level recovery for the relation, signature, interface, role, and slot cluster only until the direct governing pattern is clear.
- `A.6.P` realizes the shared algorithm for relation construction and retained relation specializations.

- `A.6.F` realizes function-like kind and relation recovery.
- `C.2.P` realizes source-expression, episteme, publication, and FPF-governed-use recovery.
- `C.2.P.DR` realizes declarative representation and imperative-metaphor overread repair.
- `A.3.1` governs `U.Method` and method-like slot recovery when semantic way of doing is hidden.
- `A.3.2` governs `U.MethodDescription` when an episteme describes a method.
- `A.6.0`, `C.29`, `A.6.1`, and `E.20` govern formal-substrate declarations, mathematical-lens use, mechanism meaning, and mechanism-governing-definition assignment when those claims are current.
- `A.15.2`, `A.15.1`, and `A.10` govern planned work, dated work, and evidence or provenance relations that method-like or path-like wording may otherwise hide.
- `E.18` governs graph paths, path slices, flow valuations, and graph relations over selected `TransformationFlowStructure` when the graph claim is current.
- `C.30.P` realizes architecture and structure wording recovery.
- `C.30.STRAT` realizes stratification and source-label wording recovery for `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, `gate`, and close source labels before return to the governing pattern.
- `C.16.P` realizes characteristic and scale wording recovery.
- `C.16.Q` realizes quality characterization and evaluative characterization wording recovery.
- `A.19.SPR` realizes state-family wording recovery when bearer, state frame, value set, admissible use, or governing pattern is hidden.
- `F.18` governs durable reusable naming after the kind under repair or relation is known.
- `F.19` governs phrase-level ontology-first plain technical rewriting after the kind under repair is recovered or while proving it is still hidden.
- `E.8` governs pattern-form and placement wording.
- `E.19` checks distribution preservation during review and refresh.
- `E.11` governs entry-distribution and assigns broad or old-term entry cases to README scenarios, ToC query cues, local Problem frames, or `I.2` expanded entry-disambiguation cases.

### E.10.ARCH:End

