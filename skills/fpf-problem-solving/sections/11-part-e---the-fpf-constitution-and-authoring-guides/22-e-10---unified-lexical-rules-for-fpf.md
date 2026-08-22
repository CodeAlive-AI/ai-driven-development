## E.10 - Unified Lexical Rules for FPF
> **Type:** Part E lexical-governance pattern
> **Status:** Stable
> **Normativity:** Definitional pattern; normative for text that claims FPF-governed wording use.

**Status and placement.** Part E.10 (“Lexical Discipline and Stratification”); complements **E.10.D1 — Recovering What “Context” Means in Use**, **E.10.D2 (EntityOfConcern and Description-episteme boundary and specification-use gates)**, the **DesignRunTag and CtxState boundary discipline** (**A.15**; **E.18**), `E.10.ARCH` wording-use restoration architecture, `E.10.ROLE` for recovery from bare claim-bearing *role*, `A.6.P` relation precision restoration, `C.2.P` epistemic precision restoration, `A.19.SPR` state-family precision restoration, and `F.18` local-first naming. `E.10:0.2` is the shared lexical trigger scan. The detailed LEX sections below supply register, naming, morphology, and local rewrite checks only for the selected wording problem; they are not a second wording-recognition table and do not replace `E.10.ARCH`, the selected precision-restoration realization patterns, the patterns that define, constrain, or test the recovered claim, or `F.18`.

**Builds on:** A.7 **Strict Distinction (Clarity Lattice)**; E.5 Guard-Rails (DevOps Lexical Firewall; Notational Independence; Unidirectional Dependency); F.5 **Naming Discipline for U-kind Names and SystemRoleKindDescription Labels**.
**Coordinates with.** `E.10.D1` for action-changing uses of *context*; `E.10.ROLE`, A.2, and A.2.1 for system-role kinds and assignments; A.15 and F.6 for Method, Work, and performed-Work attribution; A.10 for evidence use; B.1 and B.3 for Γ‑algebras and assurance; and F.17 with F.9 for source-local meaning and Bridges.

### E.10:0 - Use this when

**What goes wrong if missed.** Precision repair turns into taste or synonym replacement. A broad head such as `support`, `surface`, `carrier`, `route`, `mapping`, `kind`, `basis`, `force`, `load`, `bearing`, `object`, or `record` is replaced by another broad head, while the relation, source-use relation, admissible use, or the FPF pattern that supplies the applicable rule remains unrecovered.

**What this buys.** `E.10` gives one cheap trigger scan before heavier repair. Ordinary wording stays ordinary, local lexical mistakes close locally, and the practitioner uses the smallest applicable pattern to recover the object, relation, claim, admissible use, and remaining reader use. The result is precise enough to compose with FPF without replacing one umbrella word with another or turning every phrase into a new pattern, card, or review artifact.

Use `E.10` when a word, head, or local phrase in conformant FPF text is starting to hide what kind it names, which register it belongs to, which subject-defined boundary makes it meaningful—for example, a scheme, scope, situation, or use—or which relation or action claim it carries.

**First useful lexical scan.** Restore the head kind and register of the local wording. If no FPF-governed use remains, make the small local rewrite under `E.10` and stop. If an `E.10:0.2` row identifies an applicable precision-restoration pattern or another named pattern, apply that pattern instead of inventing a synonym. If the repaired wording becomes a durable reusable head, apply `F.18` after the selected branch has recovered the kind and use. Cite a neighboring FPF pattern only after the EntityOfConcern, relation, claim, admissible use, project-side reference, or non-use is recoverable, and say what that pattern contributes: a definition, constraint, test, method, or lookup.

**Cheap stop.** If one local lexical repair restores kind, relation, and admissible use without changing the normative meaning of FPF, stop with the repaired wording; do not create or use a Name Card, DRR, review profile, or larger epistemic precision restoration note by habit. Ordinary application starts at `E.10:0.2`, applies only the row selected by the sentence under repair, and then stops at local repair, the result obtained by applying the selected rule, controlled precision reduction, or `F.18` when a durable reusable head is actually being minted. Later LEX sections are detailed checks for the selected case, not a universal interpretation sequence.

**Not this pattern when.** Do not use `E.10` to supply the domain rule for the recovered claim. If the use under repair is evidence, assurance, work, gate, decision, causal use, publication, relation precision, or epistemic precision, use the FPF pattern for that claim and state the rule, result, or test it contributes; `E.10` contributes only the wording-problem classification. For non-FPF source prose, use `C.2.P` source-expression unpacking mode and borrow `E.10` only as a repair test, not as a conformance verdict.

#### E.10:0.0a - One-screen ordinary use

Ordinary `E.10` use is one bounded FPF-governed wording repair, not a full lexical audit. The bounded complete accepted result is:

1. `BoundedTextSpan`: the exact sentence, row, section, pattern version, `DRR` slice, or project text deliberately using FPF-governed terms, pattern references, relation names, or conformance claims under repair.
2. `TriggerSpan`: the word or phrase that carries possible FPF-governed use.
3. `SelectedInterpretation`: one applicable repair-path classification from this closed value set—ordinary no FPF-governed use, local head repair, register repair, morphology repair, context-word recovery through `E.10.D1`, bare-role meaning recovery through `E.10.ROLE`, relation-like precision restoration, episteme precision restoration, publication precision restoration, source-use relation or source-ref target recovery, durable naming, or not-triggered false positive.
4. `FinalWordingOrBlocker`: the accepted local wording, the result returned by the selected repair or pattern, or the blocker that remains.
5. `StopBackToSubstance`: once the final wording or blocker is written, return to the domain question that made the phrase matter. Further lexical classification is non-use unless another phrase still hides an FPF-governed claim.

**Plain branch rule for relation-like wording.** Start with the ordinary sentence the reader needs to write, then select one branch. Do not make the reader classify all four.

1. **World fact.** If the sentence asserts that two or more world-side things are related, name those things and say what direct relation obtains: for example, `Pump P feeds tank T`. Apply the pattern that defines or constrains that predicate. Name a separate relation occurrence only when a later claim must refer to that same occurrence, compare or qualify it, track its change or continuity, or use it as a participant of another relation. A `feeds` column or an arrow labelled `feeds` is a near-miss: neither makes the fact obtain.
2. **Reusable relation declaration.** If the text tells later authors what the same relation means across several claims or consumers, state that reusable meaning and its participant meanings, then map them to one `RelationSignature` and its A.6.5 `SlotSpec` declarations. One fact such as `P feeds T` is a near-miss: it does not declare a reusable predicate or participant vocabulary.
3. **Relation claim or report.** If the text records that somebody or some source claims a relation, name the C.2.1 claim-bearing episteme and its participant designations: for example, `Inspection note N states that P feeds T`. The note is not a participant in the feeding relation, and recording the claim does not make feeding obtain.
4. **Representation.** If a field, table cell, graph element, or formula stands for something, name the representation element, represented object, and correspondence. Use C.29 when a mathematical-lens use is current; otherwise use the applicable representation pattern. A column position, argument place, or drawn arrow with no stated correspondence is a near-miss: its shape creates no participant, `SlotSpec`, kind, or obtaining relation.

If none of these branches applies, keep ordinary or quoted wording, name the other object and—when needed—the pattern that defines, constrains, or tests it, or leave an explicit blocker. The visible result is one readable domain sentence, one reusable declaration, one claim-bearing episteme, one representation with its correspondence, or an explicit non-use or blocker—not a catalogue of all possible subject patterns.

The detailed tables below are reference material for triggered cases, not a fixed interpretation sequence. For a modest repair, one sentence, one trigger span, one selected interpretation, and one final wording or blocker is enough only when it discharges every FPF-governed use in that span.

**Minimal first-use example.** The sentence `The candidate basis is required before pattern use` has one trigger span: `required`. Here the sentence is about whether the candidate basis is ready for use, not about an accountable undertaking. Use the ordinary E.11 contribution and write: `Use E.11 to identify the candidate-basis information needed for this use; provide it before relying on the candidate.` This states the practical action, retains an ordinary PatternID citation, creates no general Requirement object, and closes the E.10 use. Stop and continue with the candidate-pattern-use question.

**Identity-sensitive replay, only when needed.** If a named later use must reproduce or compare the exact public-template position or its completeness rule, name that later use and the live alternative first; then record the exact E.11 template reference and, when that rule identity is needed, `CandidatePatternUseBasisCompletenessCondition@FPFReadme`. Reopen the ordinary wording only if the E.11 contribution it uses changes or if the project statement acquires an accountable subject and authority relation; the latter case applies A.2.8 rather than the completeness construction.

When `E.10` is applied beyond one sentence, add a bounded-text line: exact accepted `DRR` named by value, FPF pattern, monolith section, extracted host, review packet, pattern section, source span, or other named text span; trigger spans or grouped trigger locations; selected interpretation; repair boundary; and expected non-use boundary. This prevents accidental whole-corpus sweeps and makes change impact inspectable.

When a wording-repair note needs formal fields, record one `plainIntent` and the selected branch from `E.10:0.0a` before the technical fields. Keep `triggerSpan`, `boundedTextSpan`, `selectedInterpretation`, `LEX.TokenClass?`, `register`, `USM.Scope?`, `EntityOfConcern and Description-episteme boundary and specification use?`, `patternRef?`, and `finalWordingOrBlocker`; add `patternRef` only when pattern identity changes the result. Add an exact assertion, predicate, or `ClaimGraph` only when the current claim or a named later use depends on that identity. Otherwise name the concrete object and the ordinary claim. Do not use `slotOrUsePosition` as a union field for actual participants, A.6.5 `SlotSpec` values, participant designations, or representation places.

Local patterns may cite the relevant `E.10` recognition row, but they should not reproduce large wording-recognition lists or create local lexical registries unless a named local application profile has its own primary `EntityOfConcern`, first useful output, and claim boundary. Add a new recurring wording family to `E.10` only when it recurs across FPF-governed texts and cannot be handled by one local pattern; specialized patterns carry the detailed ontology when the problem is no longer lexical. Stale or overly broad recognition rows are narrowed or retired.

Self-application is bounded. When `E.10` is under improvement, use `E.10` only for its own wording-trigger repairs; use `E.21` for pattern-quality evaluation, `E.22` for improvement-oriented quality-evaluation framing, `E.23` for the improvement loop, `E.2.DA` for FPF-level Pillar effect, and the relevant pattern for relation, episteme, publication, source-use, naming, or quality-word claims.

#### E.10:0.1 - Scope split

`E.10` applies to lexical conformance in FPF pattern text, extracted pattern hosts, `FPF-Spec` monolith text, FPF governing documents, accepted `DRR` text, and any project, product, research, engineering, or review text that deliberately uses FPF terms, pattern references, FPF relation names, FPF kind claims, FPF admissibility claims, or claims FPF conformance.

For ordinary source text, intake notes, seminar transcripts, external reviews, project documents, source publications, tool outputs, or other text that does not itself claim FPF-governed use, use `C.2.P` source-expression unpacking mode. That use may borrow tests or rules from `E.10`, `A.6.P`, `A.6.6`, `F.18`, or another relevant pattern, but it does not judge the source text as failed FPF wording.

#### E.10:0.2 - Problem and applicability table

`E.10` is a lexical trigger scan and conformance pattern. Its primary `EntityOfConcern` for one pattern use is one wording use in conformant FPF text as a lexical or register sign: the head, register, morphology, local label, name candidate, kind-reference, relation-bearing cue, or replacement candidate used by the sentence.

Use `E.10` to recognize which wording-use problem the sentence raises and to select the first applicable closure disposition. The E.10 text does not become the ontology for the recovered relation, episteme, evidence, work, gate, decision, publication, architecture, characteristic, quality, or project-side FPF kind and reference named by value.

The full shared recovery order and applicability-row architecture are in `E.10.ARCH`. One E.10 use contains the cheap scan, local rewrite option, already-known-pattern rule, compact applicability table, bounded complete result rule, and fail-closed non-use boundary.

`exact` is not a precision marker by itself. It is admissible only for literal identity or bounded source identity: an exact sentence, source passage, trigger span, formula, episteme edition whose claims define that formula, same referent, or same declared `CharacteristicSpace`. When `exact`, `direct`, `current`, `subject`, `owner`, `defining`, or a similar qualifier modifies an FPF pattern, kind, relation, record, object, field, use, claim, gate, or source, name the live alternative it distinguishes and write the ordinary identity claim. For relation-like wording, select the applicable `E.10:0.0a` branch. Add a pattern reference, source-use relation, claim kind, value set, scope, assertion, predicate, or `ClaimGraph` only when omitting it would change truth, action, stop, publication, reuse, or reliance. An ordinary PatternID citation does not require that formal expansion. If recovery fails, use a quote-only, reduced-use, blocked-use, or incomplete-rewrite disposition.

Classification is not closure. A conforming result ends in one of these by-value outcomes:

- local wording accepted or locally rewritten;
- selected precision-restoration pattern applied;
- applicable FPF pattern used because the primary `EntityOfConcern`, obtaining direct relation and actual participants, receiver-needed relation occurrence, reusable A.6.5 declaration, claim-bearing episteme and any participant designations, or C.29 representation and explicit correspondence are already recoverable;
- controlled precision-reduction result with declared loss and reopen condition;
- `F.18` durable-name application after the kind under repair or relation is known;
- quote-only, reduced-use cue, blocked use, incomplete rewrite, ordinary prose, or not-triggered disposition.

**Grouping-mark self-application.** Slash marks, paired-register marks, `and`, `plus`, `&`, and compact grouping marks are triggers only when the grouping itself carries FPF-governed meaning. Retain conventional notation, formula symbols, ratios, discipline abbreviations, path-like quoted source tokens, product names, titles, URLs, or pattern-reference notation when the sentence's use is only notational; examples include `CI/CD`, `1/2`, `≡/⋈/⊂/⟂`, and exact source tokens. Rewrite claim-bearing grouped heads into explicit lists that keep unlike kinds separate; explicit alternative cases; obtaining direct relations with actual participants; reusable relation-declaration sets with their `RelationSignature` and A.6.5 `SlotSpec` values; claim-bearing epistemes; C.29 tuple or other representation elements with explicit represented objects and correspondences; or selected FPF kinds named by value. Do not let a slash hide one kind choice, an unresolved alternative, a relation claim, an admissible-use boundary, or a missing rule.

**Modifier, compound-head, and enumeration-as-kind self-application.** A modifier without a recovered head, a compound whose head word is only a vague carrier such as `source`, `support`, `basis`, `note`, `record`, `field`, `condition`, or `use`, or a repeated enumeration that starts acting like one kind is an `E.10` trigger when it carries FPF-governed use. First expand the phrase into one ordinary sentence. For relation-like wording, select one `E.10:0.0a` branch and recover only that branch's result; otherwise name the head kind, closed value set, explicit alternatives, or non-use. If a relevant pattern is known, state the definition, constraint, or test it contributes. If source-ref target wording, publication, carrier, or project-side reference is still hidden, use `C.2.P`; if move, step, action, or readiness wording is current, use `E.10.MOVE`; if architecture or stratification source-label wording is current, use `E.10.ARCH`, `C.30.P`, or `C.30.STRAT`. If no concrete result can be written, lower the phrase to ordinary prose, quote-only wording, a reduced-use cue, split alternatives, or blocked use; do not close by inventing a broader umbrella name.

**Source-to-use continuity prompt.** When the trigger word is `source` or a source-like modifier, conforming final wording preserves the source-to-use relation, not only the recovered head kind. Check five questions before closing: which concrete source expression, selected source `U.Episteme`, `EpistemePublicationRelation` occurrence or reference when availability is material, publication form, publication face, carrier relation, source-ref target, source-currentness relation, source-bearing relation, project-side FPF kind and reference, declared-use boundary, or explicit non-use is current; which entity is used now; which source-to-use, transformation, rendering, or other relation carries it forward; which use is admissible; and which claim must be reconsidered if the use becomes stronger. Name an exact assertion or `ClaimGraph` only when return, comparison, publication, or reuse depends on that identity. A source-ref marker alone is not a repair result: if its target kind or a declaration-local `SlotSpec` is needed but not recoverable, close as source-finding, quote-only, reduced-use, or blocked use. If the answer is hidden, use `C.2.P`, `A.6.3.CSC`, `E.17`, `A.10`, or the pattern that defines the needed rule rather than accepting a precise but unhelpful noun.

`source-return condition` is not this whole prompt. It is a narrower reverse or escalation condition used when a derivative, coarsened, extracted, compressed, rendered, or reused carrier has already moved away from a named source expression, selected source `U.Episteme`, exact publication occurrence when availability is material, source-bearing relation, transform record, evidence relation, or exact defining ClaimGraph and a stronger use opens return to that named endpoint or reconsideration of the exact subject assertion under its predicate. Use `source-to-use path` or the direct source relation when the current sentence is about departure from a source expression, source publication, or source-bearing relation into use.

| FPF-governed use found by `E.10` | First applicable repair or pattern contribution | Closure result |
| --- | --- | --- |
| No FPF-governed use after the wording-use check | Keep ordinary prose, quote, didactic phrase, or not-triggered text. | No precision-restoration pattern is applicable. |
| Local lexical or register ambiguity only | Local rewrite under `E.10`. | Repaired wording plus remaining reader use, or ordinary-prose demotion. |
| *Context* wording that hides subject-defined content whose boundary changes the action—for example, a scheme, scope, model-use boundary, situation, design-time or run-time referent, architecture, environment, domain subject, or local-practice use | Apply `E.10.D1`; then apply only the pattern needed for the recovered value or relation. | One repaired statement names the content hidden by *context* and gives the next subject-matter action or stop. It creates no generic Context participant, `ContextId`, or two-part `SenseCell(Context, LocalSense)`. |
| Modifier-without-head, vague compound head, or enumeration-as-kind wording whose governed head, declaration, direct relation, representation, alternatives, or applicable rule is hidden | Apply `E.10` head-kind recovery first, then use the relevant pattern if it is already known. Otherwise use the selected restoration branch: `A.6.P` for relation construction, `C.2.P` for source-ref target, publication, carrier, or project-side reference recovery, `E.10.MOVE` for move, step, action, or readiness wording, `E.10.ARCH` plus `C.30.P` or `C.30.STRAT` for architecture or stratification source-label wording, `E.24` when a real ontic candidate decision is current, or `F.18` only after the governed kind and use are recovered. | Selected FPF kind or alternative-case set; obtaining direct relation and actual participants; receiver-needed relation-occurrence identity; reusable `RelationSignature` with A.6.5 `SlotSpec` values only when declaration is current; claim-bearing episteme and participant designations only when an assertion is current; C.29 representation element and explicit correspondence only when representation is current; ordinary-prose demotion; reduced-use cue; blocked use; or incomplete-rewrite disposition. No list or compound head becomes a kind by itself. |
| Relation-like wording or relation-bearing use | Apply `A.6.P` or a retained A.6 relation specialization. Only when exact participants are recovered and no current direct relation closes the named receiving claim, handle the residual under `A.6.RCD`. | State the obtaining named direct relation, actual participants, and qualifier values. Distinguish one relation occurrence only for a named receiving use; add a reusable `RelationSignature` and A.6.5 participant or qualifier `SlotSpec` values only when declaration is current; keep a row that states the claim as a claim-bearing episteme with participant designations, and keep any graph, tuple, field, or table element as a C.29 representation with explicit correspondence. Otherwise the exact residual is one of these `A.6.RCD` results: disposition 2, a local compound claim; disposition 3, a reusable predicate-definition episteme, optionally continuing to a derived-kind candidate plus its proposed direct subject settlement only when a named receiver additionally needs stable occurrence semantics; or disposition 4, a primitive-kind candidate plus its candidate standalone direct pattern. `E.24` and `E.24.UK` retain admission, and `A.6.0` declaration follows only after admission. Every branch preserves admissible relation use, blocked overread, and remaining reader use. |
| Bare claim-bearing *role* whose current object or relation is not already clear | Apply `E.10.ROLE`. First write the ordinary sentence with its recognizable object and action or relation; then use `A.2` and C.3 for an exact local system-role kind, `A.2.1` for one exact direct assignment species, `A.6.RSIR` for direct participation, declaration, interface, operation, or representation recovery, or the direct pattern for another recovered object or relation. | One exact recovered object or relation and its pattern; ordinary or quoted non-use; or the exact blocker. Bare *role* has no default Tech reading and creates no system admission, classification, assignment, agency, capability, participation, responsibility, Work, or episteme use. |
| Relation-like, declaration-like, or interface-like wording whose object or claim kind is hidden—for example, *relation*, *signature*, *interface*, *assignment*, *enactment*, *slot*, *field*, *parameter*, *argument*, *endpoint*, *port*, *API*, *protocol*, *connector*, *capability*, *affordance*, *method*, *function*, *concern*, or *interest* | Apply `A.6.RSIR` only when the relevant pattern is not already clear. If a world-side relation use is current, recover its participants and existing direct relation through `A.6.P`; use `A.6.RCD` only when those participants are exact but no current direct relation closes the named receiving claim. If the current object is already recovered, use the concrete pattern instead: `A.6.P`, `A.6.5`, `A.6.0`, `A.2`, `A.2.1`, `A.15`, `A.6.M`, `A.6.F`, `A.6.A`, or the method, work, publication, episteme, evidence, status, or gate pattern for the claim. | Recovered project concern, EntityOfConcern or claim kind, selected pattern and concrete contribution, direct relation and participants when relation use is current, `A.6.RCD` disposition only when its residual route is triggered, declaration need, retained source-label use, blocked overread, and stop before minting generic `U.Interface`, `U.Concern`, `U.Interest`, or a standalone slot ontology. |
| Source-expression, publication, publication form, face, carrier, rendering, `PublicationUnit`, framework publication or access carrier, FPF-governed use, or `reading`, `read`, or `quality-read` wording whose entity or construction is not yet recovered | Apply `C.2.P` first. If the recovered construction is only publication or access exposure, use `E.17`, `E.17.AUD`, or `E.4.*` as applicable; if it is evidence, source-currentness, generated-output admission, work-reliance repair, architecture use, or structure use, use `A.10` or `G.11`, `C.35`, `A.15.4`, `C.30.P`, `C.33`, or `C.34` after `C.2.P` recovers the carrier relation set. If the recovered entity or construction is evaluation for improvement, use `E.22`, `E.21`, `E.9.DA`, or the pattern for that evaluation claim. | Source-local meaning, publication and carrier relation set, publication-form relation when it is being made, EntityOfConcern, project-side FPF kind, use disposition, the downstream pattern and its contribution when the carrier serves evidence, currentness, generation, framework publication or access, work-reliance repair, architecture use, structure use, or evaluation, adjacent overread blocked, and remaining reader use. |
| Ontic, ontic candidate, concept cluster, semantic area, ontological neighborhood, slot relation, schema, data structure, record, card, table, or publication-form wording whose EntityOfConcern and publication boundary are hidden | Apply `E.24.CD` when repeated material may call for an ontic candidate decision; apply `E.24.PUB` when the confusion is among ontic, ontic-description episteme, publication form, view, record, card, table, schema, or data-structure expression. Use `E.24` or the already identified pattern when the ontic object is recovered. | Candidate ontic cluster, EntityOfConcern, and the selected pattern contribution; only after durable settlement, the E.24 `onticSlotRelation` and its actual participants; or, under their separate rules, an ontic-description episteme, reusable `RelationSignature` and A.6.5 `SlotSpec` values, publication form, C.29 representation element and explicit correspondence, or source relation. Preserve admissible use, blocked publication-form overread, and remaining reader use. |
| Admissibility-like, external-rule-looking, authority-looking, readiness-looking, validity-looking, pass-looking, fail-looking, or conformance-looking wording whose bearer, claim kind, source relation, value frame, bounded use, or rule is hidden | Use the claim-specific pattern when recoverable. If `readiness` or `ready` still hides which governed value is meant, use `E.10.MOVE`; it may then exit to `A.19.SPR` for a hidden bearer and state frame, `A.2.5` for an assignment-state condition, `A.15.5` for work-entry readiness, `A.21` for a distinct gate decision, or another direct pattern. For other unresolved trigger wording use `E.10.ARCH` and the claim-specific pattern; do not mint a generic admissibility object. | Exact object and claim, value frame or decision class, direct pattern, bounded use and any material stop or reopen condition; otherwise quote-only, reduced-use, or blocked-use. |
| Method-like wording—for example, method, practice, technique, algorithm, program, solver, proof, recipe, workflow, process, procedure, access-path, query-plan, control-strategy, method algebra, method graph, selector calculus, or programming-paradigm wording whose method-side object or relation is hidden | Recover that object or relation before rewriting. Use `A.3.1` for one `U.Method`. If the sentence concerns a method-side relation, name that relation itself—for example, composition, substitution, iteration, fallback, selection, or family membership—and use the rule that defines or constrains it. Only when a named use depends on how several such relations are organized should the practitioner use A.22's criterion to select the structure; call that local structure `MethodRelationStructure`. If another object is meant, follow the rule that defines or tests it. It may be, for example, one `U.MethodDescription` episteme, an A.6.0 formal-substrate declaration, a C.29 mathematical-lens use, an A.6.1 mechanism-application binding or E.20 mechanism claim, `U.WorkPlan`, dated `U.Work`, a local system-role kind or assignment recovered through `E.10.ROLE`, an A.1.1 `BoundedModelUseStructure`, a discipline position, cultural-evolution wording, method-family registry or selector outcome, evidence relation, or quote-only source wording. | The recovered value or relation and, when material, the contribution from its pattern—for example, one `U.Method`, direct method-side relation, optional A.22-selected `MethodRelationStructure`, one-method `U.MethodDescription` episteme, formal-substrate declaration, C.29 representation and correspondence, mechanism binding or claim, plan, dated Work, system-role kind and classification, assignment occurrence, relation among system-role kinds, transformation, result, or model-use structure—plus admissible use, blocked overread, and remaining reader use. Do not replace one umbrella with `method`, `practice`, `mechanism`, `algorithm`, `workflow`, or `method algebra` by taste. |
| Input, raw-material, source-data, source-material, output, result, outcome, deliverable, handoff, or reusable work-name wording whose exact relation involving a Work occurrence or exact occurrence basis is hidden | For epistemic source data or source material, use `C.2.P` first and then `A.6.P.WMR` for a separately current claim involving a Work occurrence; use the pattern for the relevant physical relation when physical raw material is current. Otherwise apply `A.6.P.WMR` after generic relation recovery. Use `F.18` only for a durable name after the governed value and use are recovered. | First recover the exact entity under its own admitted kind and the exact related object. Keep claim subject, modality and exact temporal extent, polarity, and recovery/support state separate, then return exactly one family: exact direct subject-relation claim, positive or governed negative; exact `A.6.1` operation-application binding; exact local `A.15.PROD`/`A.6.RCD` claim; or exact non-assertability result. Select `factually unsupported` for the failed known `EpistemeUsedByReviewWorkAsReference` predicate, `missing-information` for the unavailable ETL receiving-use fact under a known governor, and `missing-governor` for the absent `Patient_8472` / `HE-8472` health-effect relation kind and defining pattern or declaration. Only the last branch names the affected use and future subject pattern or relation declaration; none supplies opposite polarity. A performed-work name additionally rests on its `A.15.1` occurrence basis, and other results remain separate. |
| Transformation, change, pipeline, dataflow, flow, network, circuit, path, slice, workflow, process, operation, or close change-situation wording whose changed object, direct relation, declaration-local operation binding, or representation place is hidden | Apply `A.3.4.P` first. If `U.Transformation`, `TransformationFlowStructure`, mathematical description, method, method description, mechanism, work plan, dated work, functioning relation, temporal aspect, evidence, source, publication, gate, decision, assurance, changed referent, declaration-local operation-result binding, measurement-result episteme, evaluation result, `C.11` `ChoiceResult` or decision record, or quote-only source wording is already recovered, use the pattern for that claim. | Recovered transformation identity or non-transformation value; changed referent and any obtaining direct relation with actual participants; declaration-local operation-result binding only when that A.6.1 declaration is current; C.29 representation and explicit correspondence when source wording names a representation place; separate measurement, evaluation, choice, decision, or other claim when current; retained use; blocked overread; and remaining reader use. Do not replace one source label with `flow`, `network`, `process`, `method`, `function`, or `transformation` by taste. |
| Move-like wording such as first move, working move, next move, pattern move, project move, architecture move, or local move, and readiness-like wording such as `readiness`, `ready`, `full kit`, `work entry`, or `launch-ready`, whose governed text and value are hidden | Apply `E.10.MOVE` first unless a local pattern has already recovered the object. | Recovered value under its direct pattern: for example, pattern-use recommendation, demonstrated continuation, evaluation-result prediction, P2W carry-through, WorkPlan, A.15.5 work-entry readiness result, A.2.5 assignment-state claim, A.21 gate decision, dated `U.Work`, language-state move, next planned action, architecture candidate use, ordinary prose, quote-only wording, or blocker. Do not mint root `U.Move` or a universal readiness relation. |
| Declarative representation wording overread as imperative action, method, work, deontic permission, work authorization, release authorization, evidence, or pattern dispatch: graph path, path slice, flow valuation, evidence-path wording, state predicate, SQL-like query, checklist predicate, table, dashboard, publication face, mathematical representation, method-description representation, source-chain relation, file path, or FPF pattern relation | Apply `C.2.P.DR` unless a defining or testing rule already resolves the claim. Accepted cases include `E.18` graph path or `PathSlice`, `A.10` evidence relation, `A.19.SPR` state predicate or value, `E.17` publication face, `C.29` mathematical-lens use, `A.3.1` method, `A.3.2` method description, `A.15.2` work plan, `A.15.1` work occurrence, carrier file path, source-chain relation, and declarative pattern relation under `E.8` or `F.19`. | Visible expression or artifact; current direct object, claim, or relation; representation use or explicit correspondence, or `none`; and the stronger action or inference that stays blocked. When current, also name the source or publication relation, the direct pattern contribution, retained use, non-admissible overread, and stop or reopen trigger. A visible artifact is not classified as a representation merely by its form. |
| Architecture or structure wording with a hidden selected structure, obtaining `ArchitectureRelation`, `ArchitectureClaim` episteme, architecture-description use, structural-view use, source-return condition, or named C.30 subcase | Apply `C.30.P`. If `A.22`, `C.30`, `C.30.ASV`, `C.30.AD`, or a named C.30 subpattern is already recoverable, use it directly. | Recovered selected structure; obtaining `ArchitectureRelation` with its holon and structure participants; separate `ArchitectureClaim`; architecture-description episteme when that use is current; structural view; source-return condition; result obtained by applying the selected rule; or stop. |
| Holon, system, episteme-as-holon, collection, part-whole, multilevel, interlevel, boundary, interaction, functioning, capability, emergence, BOSC, MHT, MET, MFT, `post`-like, or promotion-like wording whose object kind, part-whole relation, boundary-crossing relation, transformation relation, architecture relation, ethical conflict relation, or admissible-use boundary is hidden | Recover the object and decision at issue first. Use `A.1.SCR` only when the relied-on claim depends on which exact system acts, is intended to change, carries a capability, persists, or is explicitly designated as a project target and that proposed subject remains hidden. First use `A.1.SCR` to check whether a non-system subject already answers the decision, and apply the complete `A.1` criterion only while systemhood remains load-bearing; `E.24.UK` supplies the one-time public-kind admission predicate. Service/access wording follows the independent `L-SERV` row and does not justify using A.1.SCR merely because an exact bearer may later be recovered. Otherwise recover the exact subject predicate and assertion. Use `B.2.P` only for emergence-family, MHT-family, MET-family, MFT-family, synergy, metric-mirage, whole-reidentification, and collection wording entangled with those ambiguities. After recovery use the predicates and assertions located through `A.1` for a holon/system claim, `C.2.1` or the named publication pattern for episteme/publication claims, the exact part-whole or collection predicate, `B.2` for whole reidentification, `B.2.2` for result-system MHT, `B.2.3` for result-episteme MHT, `B.2.4` for capability/functioning-whole reidentification, `B.2.5` for supervisor-subholon feedback, `A.3.4.P` for transformation wording, `A.6.F` for functioning/capability wording, `C.30`, `C.30.ASV`, `C.30.LCA`, `C.30.ILC`, `C.30.STRAT`, `D.2`, `D.3`, `D.4`, or another named predicate from the pattern that defines or constrains it. | Work, Method, capability, transformation, episteme, structure, or relation result when that closes the decision; otherwise the exact A.1.SCR acting/changed-system result, recovered holon/system, collection, part-whole relation, boundary-crossing relation, architecture relation, supervisor-subholon feedback relation, interlevel ethical conflict, mediation use, source-label repair, admissible use, non-admissible overread, or stop. Do not mint `U.Level`, `U.SystemLevel`, `U.HolonLevel`, `U.Frustration`, `U.Emergence`, a candidate kind, or procedural control flow merely because a pattern was selected. |
| Culture-like wording—for example, culture, cultural evolution, style, tradition, genre, scene, technique, practice, platform, regime, measurement regime, attractor, developmental machinery, or close cultural-evolution wording whose current object is hidden | Immediate disposition: recover the current object or relation first. Possible values include a method family, work family, ordinary or quoted *role* wording, or—after `E.10.ROLE`—a local system-role kind and its classification, an obtaining `U.SystemRoleAssignment` occurrence, or a relation among system-role kinds. Other values include a discipline, canon or memory episteme, recognition or selection regime, mediation system or architecture, measurement or visibility relation, publication label, variant set, dynamics or mathematical-lens claim, exact source or practice boundary, A.1.1 `BoundedModelUseStructure`, development-loop relation, or cultural-evolution case. Use the method-like row above when `practice` or `technique` is just the ordinary word for a way of doing; use `C.36` when a collective-holon or discipline-facing cultural-evolution case is current; use `C.36.P` for repeated wording-use recovery; use `F.17`, `F.18`, and `F.9` for durable terms and bridges; for every recovered object or relation, use the rule that defines, constrains, or tests it. | One root cultural ontology by source word, root `U.Culture`, `U.Style`, `U.Tradition`, `U.Practice`, `U.Platform`, `U.PlatformRegime`, `U.MeasurementRegime`, `U.DevelopmentalMachine`, loose style-as-attractor ontology, default role ontology, or one umbrella replacement word. |
| External holon-class or Holon Graph Architecture (HGA) graph-expression wording such as `AgentHolon`, `OrganisationHolon`, `DataHolon`, `ProcessHolon`, `Portal`, `Projection`, event envelope, provenance, target holon, projection envelope, projected content, envelope, payload, RDF graph, node, edge, traversal, or boundary-governed payload whose FPF object is hidden | Recover the claim before importing the source label. Use `A.1` for admitted system or holon claims; `C.2.1`, `E.17`, architecture-description, publication, source-relation, or evidence patterns for data, document, projected content, description, publication, view, or evidence claims; `A.10`, source-relation, evidence-relation, dated-work, or publication patterns for event and provenance claims; and `A.3.4.P`, method, work-plan, or Work patterns for process-like wording. Portal, access, traversal, service-access, protocol, and agreement-like words do not select peer routers. While their object remains hidden, use `A.6.RSIR`; after recovery, use `E.17` or the pattern for the publication claim, `C.29` or the pattern for the representation and correspondence, `A.6.0` plus `A.6.5` for a reusable signature and its slots, `A.6.M` for a module-interface claim, the pattern for the policy claim, and `A.10` or the pattern for the evidence claim. Use `A.6.P:4.11a` only when a relied-on service or access phrase hides its concrete subject or direct relation; use `A.6.C` only when recovered service-term, SLA, protocol, or agreement-like wording bundles promise, utterance or publication, governance, Work or consequence, or evidence claims; use general `A.6.P` only for another under-specified direct relation. For graph, RDF, node, edge, or traversal expression claims, use `C.29`, `A.22`, `C.30.ASV`, `C.30.AD`, `E.17`, or the pattern for the recovered source or publication relation; use `A.6.B` only for L, A, D, or E statement classification inside a boundary package. | W3C Community Group Holon Graph Architecture (HGA) vocabulary is retained as a serious source-finding cue or comparison term only after the recovered FPF object is named and differences from FPF are explicit. Do not mint source-class U-kinds such as `U.AgentHolon`, `U.DataHolon`, `U.ProcessHolon`, `U.Portal`, `U.Projection`, `U.Envelope`, or `U.Payload`; do not turn semantic-web class names or graph-expression vocabulary into FPF ontology. |
| Markov blanket, Markov border, computational boundary, boundary leak, or active-inference boundary wording whose object kind or claim kind is hidden | Recover whether the source-bearing external phrase names accepted local Markov dynamics, a mathematical or probabilistic lens, holon delimitation, boundary-crossing relation, relation precision, signature or slot declaration, interface, interface module, functional element, physical component, boundary description or publication, boundary-package statement classification, or agency-threshold claim. | Use `A.3.3`, `C.29`, `C.26`, `C.26.3`, `A.1`, the pattern for the recovered relation, `A.6.RSIR`, `A.6.P`, `A.6.0`, `A.6.5`, `A.6.M`, `A.6.F`, `A.14`, `C.13`, `B.3.5`, `C.30.AD`, `E.17`, `A.13`, `A.19`, or `C.16` according to recovered claim; use `A.6.B` only for L, A, D, or E statement classification inside a boundary package. Do not mint `U.MarkovBlanket`, generic `U.Boundary`, generic `U.Interface`, or binary `U.Agent`; do not collapse statistical separation, physical boundary, interface module, description, boundary-package classification, and agency threshold. |
| Stratification or structure-source-label wording such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` when the FPF kind, relation, claim-use, or source-use is not yet recovered | Apply `C.30.STRAT` first. If a control-layer relation, module-interface relation, architecture-to-`TransformationFlowStructure` relation, mathematical scale relation, coarse-graining relation, publication relation set, gate relation, or other use is already recovered, use its pattern directly. | Recovered FPF kind, relation, claim-use, source-use, and the selected pattern contribution; `StratificationSourceLabelRepairNote`; ordinary source label; quote-only, reduced-use, or blocked-use disposition; or stop. |
| Characteristic, scale, score, coordinate, metric, indicator, threshold, comparison, or scalar-quality wording with hidden construction | Apply `C.16.P`. If `A.17`, `A.18`, `C.16`, `A.19`, `C.25`, `C.29`, `E.21`, or another applicable pattern is already recoverable, use it directly. | Recovered `Characteristic`, Scale, Coordinate, Value, Score, unit, scoring method, comparison basis, indicator role, applicable pattern result, or stop. |
| State-family wording with hidden bearer, state frame, value set, or applicable rule: `state`, `status`, `posture`, `stance`, `currentness`, or close compounds | Apply `A.19.SPR`. For `readiness` or `ready`, use `E.10.MOVE` first unless the exact direct claim is already known; return to A.19.SPR only when a hidden bearer and state frame remain. | Exact object and claim or value under its direct pattern; a predicate only when that pattern defines or needs one; otherwise ordinary-prose, quote-only, reduced-use, or blocked-use disposition. |
| Quality or evaluative characterization wording | Apply `C.16.Q`, `C.25`, `E.21`, or the pattern for that characterization claim after any needed `C.16.P` repair. If the found problem is relation construction, apply `A.6.P` instead. | Quality-term repair, Q-bundle or pattern-quality coordinate use, relation split or bridge split when that relation or bridge claim is being made, and blocked scalar, gate, or release overread. |
| Function-like wording with hidden FPF kind, relation, claim, view, or relevant pattern application: `function`, `functional`, `functionality`, `effect`, or close compounds | Apply `A.6.F` first when kind and relation recovery is needed. If the FPF kind or pattern relation is already recovered by value, use that pattern directly. | FPF kind or relation named by value, application of the named pattern, mathematical-lens use, quality-pattern application, characteristic-pattern application, module-interface-pattern application, ordinary-prose demotion, or stop. |
| Intentional loss of precision for a narrower admissible use | Apply the controlled precision-reduction pattern, normally `A.6.3.CSC`, with `E.17.*`, `A.6.3.RT`, `F.9`, or `C.29` when that relation is being made. | Source-bearing side, declared loss, narrower admissible use, blocked downstream use, and reopen condition. |
| Durable reusable head, lineage label, concept-set row, cross-local name use, or UTS-facing name | Apply `F.18` after the selected repair has recovered what the name would name. | Name card or naming row only for durable naming need; one-off local wording closes locally. |
| Trigger found but kind, relation, substrate, applicable pattern, admissible use, or remaining reader use cannot be recovered | Fail closed. | Quote-only wording, reduced-use cue, blocked use, incomplete rewrite, ordinary prose, or not FPF-governed wording. |

`reading`, `read`, and `quality-read` are trigger wording only when the sentence uses the word to carry interpretation, publication use, source-use assignment, evaluation, comparison, evidence, gate, work, decision, release, assurance, or admissibility claim. Do not create `ReadingPrecisionRestoration`. Recover the actual EntityOfConcern; the exact publication, carrier, or source-use relation and its actual participants; the evaluation claim or bundle; an obtaining direct relation and actual participants; a world-side Work occurrence; or a separate claim-bearing episteme about one, then apply `C.2.P`, `E.17.ID.CR`, `E.22` plus object-under-improvement evaluation named by value, `A.6.P`, or the FPF pattern for that claim.

`function`, `functional`, `functionality`, and `effect` are trigger wording when the FPF kind, relation, claim, view, or application of the pattern for that claim is hidden. Do not assign the wording by architecture default. `A.6.F` remains the function-like wording unpacker; mathematical function, mapping, relation, loss, objective, value functional, or operator goes to `C.29` when mathematical-lens use is being claimed. Functional-architecture use goes to `C.30` or `C.30.ASV` when the architecture or structural-view claim is recovered by value; architecture-to-`TransformationFlowStructure` use goes to `C.30.TFS-REL`.

`layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, and `gate` are source labels when they first arrive from engineering, mathematical, publication, or project prose without a recovered FPF kind. Do not mint `U.Layer`, `U.Level`, `U.Tier`, `U.Stack`, or a universal stratification kind. Use `C.30.STRAT` to recover the relevant rule, or apply the rule for the already recovered kind, relation, claim-use, or source-use: `C.30.LCA` for control-layer relations, `A.6.M` for module-interface relations, `C.30.TFS-REL` for architecture-to-`TransformationFlowStructure` claims, `E.18` for selected transformation-flow structure, `C.16.P` or `C.29` for scale, coarse-graining, or mathematical use, `C.2.P` for publication or source use, and gate, work, or decision patterns when those claims are being made.

Description, publication, and representation mediation source words need the same recovery discipline. Treat `stack`, `lane`, `profile`, `mediation`, `binding`, `representation`, `publication`, `model`, `space`, `graph`, `latent`, `weights`, `embedding`, `vector store`, `carrier`, `dashboard`, `posture`, `route`, `path`, `surface`, and close compounds as trigger wording when the sentence has FPF-governed use and the object, obtaining relation, reusable declaration, claim-bearing episteme, or representation correspondence is hidden. Recover the current EntityOfConcern, relation and participants, declaration, or representation and correspondence; then state the applicable pattern contribution only when it is needed, plus admissible use, blocked overread, and remaining reader use. Do not replace the trigger with another umbrella head; do not mint a durable name unless `F.18` is explicitly selected.

Local patterns may cite the relevant `E.10` recognition row. They do not reproduce the wording-recognition table or create local lexical registries unless a named local application profile has its own primary `EntityOfConcern`, first useful output, and claim boundary. Specialized restoration patterns carry the detailed ontology when the problem is no longer lexical.

#### E.10:0.2a - Bounded complete result and already-known-pattern rule

The already-known-pattern rule is:

> If the applicable pattern and the current `EntityOfConcern`, obtaining direct relation and actual participants, receiver-needed relation occurrence, reusable A.6.5 declaration, claim-bearing episteme and any participant designations, or C.29 representation and correspondence are already recoverable by value, use that pattern directly and state its concrete contribution.

Apply a precision-restoration realization pattern such as `A.6.P`, `A.6.F`, `C.2.P`, `C.30.P`, `C.30.STRAT`, `C.16.P`, `C.16.Q`, or `A.19.SPR` only when wording hides the EntityOfConcern under repair, relation, characteristic, scale, score, quality characterization, source-use disposition, state-family field, admissible use, or remaining reader use.

The bounded complete result is the shortest result that fully recovers the kind under repair and remaining reader use. Shortest is not lowest effort: every FPF-governed use has a by-value disposition, and `not triggered` or ordinary prose is stated as such with the checked span.

- local rewrite for a one-sentence local ambiguity;
- compact repair note or row when one precision-restoration pattern is needed;
- pattern application when the FPF kind, relation, claim-use, source-use, or admissible-use boundary is already recoverable;
- full restoration check only when several claims being made, admissible-use cases, source-currentness relations, cross-pattern authority, or downstream reliance remain under repair;
- fail-closed non-use when recovery is not possible.

After kind and applicable-pattern recovery, state the remaining admissible reader use: what the reader may now do, why the distinction matters, or which FPF pattern now carries the claim. If the repaired wording is kind-correct but inert, the repair is incomplete.

**Value-substitution check.** A wording repair also fails when it optimizes lexical purity while making the working text worse: less readable for its declared reader, less affordable to apply, less semantically composable with named patterns, less clear about the primary `EntityOfConcern`, relation, declaration, claim-bearing episteme, representation, or less action-guiding. In that case, narrow the repair, keep ordinary wording with a recovery note that states the recovered kind and use, use the relevant pattern, or leave the issue blocking by value. Do not trade real kind, relation, source-use, or admissible-use recovery for smooth prose; this check prevents precision-restoration theatre, not ontology repair.

Tool-assisted trigger inventories may help find candidate spans, but they cannot close ontological precision repair. Closure remains the object under repair; any obtaining relation, receiver-needed occurrence, reusable declaration, claim-bearing episteme, or representation and correspondence that is current; the selected pattern contribution when needed; admissible use; non-admissible overread; and remaining reader use.

**Replacement-candidate closure.** A repair that replaces one trigger word with another word or phrase is not closed until the replacement itself passes the same `E.10` trigger scan. If it is another umbrella word, quasi-scale, process metaphor, role-free deontic word, or untyped head, recover the kind, relation, admissible use, and relevant pattern contribution, apply `F.18` when a durable name is being minted, or fail closed. Repeat only until the wording reaches a stable closure point: ordinary wording with no FPF-governed use, local repair with recovered kind and use, direct pattern application, `F.18` durable-name result, controlled precision reduction, or explicit blocker. Do not accept a smoother synonym as repair evidence.

**MG-DA cold-reader closure.** A reader who has not read the `DRR`, campaign notes, or reviewer memory must still recover the object under repair and its FPF kind or ordinary non-FPF status, the relation or claim, any declaration or representation needed by the current use, the admissible reader use, the next practical action, and—when a stronger claim opens—the pattern that handles it. Broad heads such as `object`, `item`, `value`, `relation`, `record`, `condition`, `basis`, `material`, or `specialization` fail unless the sentence names the practitioner-recognizable object and use. A complete `specialization` phrase says what specializes what and which inherited or changed declarations or uses matter.

#### E.10:0.2b - Wording-Use Trigger Check Registry

`E.10:0.2` is the shared trigger scan. This section is the check registry for high-pressure wording in FPF-governed text and source prose being unpacked for possible FPF use. It does not create a second all-purpose ontology and does not create domain-pattern outcomes. It selects a closure disposition: local rewrite, selected precision-restoration pattern, direct application of a pattern whose contribution is already known, controlled precision reduction, `F.18` durable-name application, or fail-closed non-use.

The words below are frequent in conformant FPF text and in project texts that deliberately use FPF-governed terms, pattern references, relation names, or conformance claims.
Files carrying FPF pattern text are useful search examples, not the boundary of language cleanup: the same rule applies wherever the text under repair is claim-bearing FPF, project guidance that deliberately uses FPF-governed terms, pattern references, relation names, or conformance claims, or source prose being unpacked for possible FPF use.
They are not banned words.
They are words that trigger kind recovery when they carry an ontology, authority, evidence, or admissibility claim. The table gives alternatives to recover from; it is not a group kind. The chosen result may be a local wording repair, a selected restoration pattern, direct application of a pattern whose contribution is known, controlled precision reduction, or an explicit not-triggered disposition.
| Trigger words | Recovery choices; write the selected concrete result—specific object, obtaining relation and participants, receiver-needed occurrence, current declaration, claim-bearing episteme, or representation and correspondence—or a not-triggered disposition before use | Inadmissible reading |
| --- | --- | --- |
| `case`, `scenario`, `example`, `pilot`, `anti-case` | worked case, recognition case, pilot case, negative control, project situation, evidence case, comparison case, or source example | proof, evidence, universal pattern, accepted `DRR`, source basis, or decision by itself |
| `basis` | source basis, decision basis, evidence basis, comparison basis, threshold basis, grounding basis, admissibility basis, or authority basis | generic reason, untyped support, or "whatever the text relies on" |
| `force`, `load`, `bearing`, `claim force`, `claim-force-bearing`, `force-bearing`, `claim-bearing`, `relation force`, `qualifier force`, `support force`, or close compounds | claim being made or admissible-use boundary, relation-bearing use, or a `support` use recovered under `E.10:0.2` as ordinary or quoted non-use, a direct subject relation with its things and predicate named, or one common alternative stating what describes, bears on, enables, or helps what and for which use; qualifier claim; action-guidance use whose relevant pattern and contribution are named; evidence-use criterion; assurance, gate, work, decision, release, or admissibility use; or a conventional pattern-language `Forces` entry naming a tension that shapes the pattern | unstated strength scale, hidden authority, unnamed evidence weight, unnamed importance, process load, generic pressure, or proof that a wording repair closed |
| `context`, `scope`, `frame` | exact source or practice boundary, effective scheme, claim scope, A.1.1 `BoundedModelUseStructure`, working situation, design-time or run-time referent, reference frame, state or normative frame, selected viewpoint for one describing use, or ordinary narrative framing | generic Context object, authority, authority-reference status, or hidden qualifier |
| `state`, `status`, `posture`, `stance`, `currentness`, or close state-family compounds | exact object and claim or value under its direct pattern; apply `A.19.SPR` only while bearer or state frame remains hidden | maturity adjective, authority, gate passage, deontic permission, release authorization, evidence, assurance, source authority, work completion, or process state by appearance |
| `readiness`, `ready`, `full kit`, `work entry`, `launch-ready` | use `E.10.MOVE` while the governed value is hidden; then use A.19.SPR, A.2.5, A.15.5, A.21, or another direct pattern according to the recovered claim | one generic readiness kind or relation, automatic gate passage, permission, or performed Work |
| `claim`, `claim content`, `claim referent` | claim node or claim content in a claim-bearing episteme, claim-bearing publication, admissibility target, EntityOfConcern, or referent relation | sentence, opinion, text fragment, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, or whole publication unit |
| `evidence`, `witness`, `ground`, `proof` | evidence record, evidence relation, evidence-provenance relation, witness, grounding relation, source pin, observation, validation result, or assurance argument component | authority, approval, gate, engineering justification, or truth by label |
| `authority`, `permission`, `approval`, `commitment`, `obligation` | exact A.2.9 speech act; A.2.8 commitment; A.2.8.PER permission or permission-conflict relation; direct authority relation; exact beneficiary, grantor, policy, scope, window, and other participant references required by that predicate; gate record; decision record; or policy claim. If source wording also says *role*, pass it through `E.10.ROLE`; neither a title nor an assignment alone establishes permission or authority. | visible label, author confidence, reviewer praise, explanation, provenance mark, or generic assignment as authority |
| `requirement`, `required`, or close requirement-headed compounds | run `E.10:0.2b.1`; recover bearer, claim or relation kind, the pattern that supplies that construction when needed, practical consequence, and the construction itself | generic Requirement family, untyped condition, hidden command, commitment without accountable subject, or one shared suffix for unlike engineering claims |
| `admissible`, `lawful`, `legal`, `legality`, `allowed`, `permitted`, `authorized`, `valid`, `pass`, `ready`, `conformant`, `eligible`, or close admissibility-like compounds | claim-specific value, gate decision, constraint-validity result, evidence or assurance use, source-currentness relation, work-plan readiness, dated-work finalization or completion claim, measurement-result episteme, evaluation result, `C.11` `ChoiceResult` or decision record, external-rule claim, publication-use boundary, state-like value, pattern-quality result, or bounded admissible use whose bearer, source relation, value frame, non-admissible overread, reopen condition, and governing rule are named | generic deontic permission, generic authorization, external-rule truth, gate passage, evidence strength, release decision, work completion, source authority, or conformance by label alone |
| `algorithm`, `program`, `solver`, `proof`, `recipe`, `method`, `workflow`, `process`, `procedure`, `access path`, `query plan`, `control strategy`, `method algebra`, `method graph`, `selector calculus`, or programming-paradigm labels | One `U.Method`; exact method-side relations; an A.22-selected structure locally designated `MethodRelationStructure` only when a named use depends on their organization; `U.MethodDescription` only for a separately identified claim-bearing episteme whose EntityOfConcern is one admitted method and whose claims pass A.3.2; `U.Signature(profile=FormalSubstrate)`; mathematical-lens or C.29 representation use; `U.Mechanism` declaration or realization; `U.WorkPlan`; one dated Work occurrence admitted under `U.Work`; method-family registry or selector outcome; evidence or control relation; source quote; or another result selected by the recovered object, relation, declaration, representation use, or claim | one generic method, software-only algorithm, method algebra as root object, mechanism by default, `U.MethodDescription` by procedural or document form, performed work by description, selected structure without A.22, or instruction sequence by representation style |
| `input`, `raw material`, `source data`, `source material`, `output`, `result`, `outcome`, `deliverable`, `handoff`, or an action nominal or reusable work name | exact entity, exact related method, plan, work, transformation, evaluation, delivery, transfer, or receiving use, and one truthful `A.6.P.WMR` result family; `C.2.P` first for epistemic source data or source material; the pattern for the relevant physical relation when physical raw material is current; `A.15.1` occurrence basis before naming performed work; `F.18` only after the value under repair is recovered | universal input, output, work result, transformation result, outcome, deliverable, handoff, or production family; actual work inferred from an action nominal, WBS element, Work Package, method description, planned filling, or nearby result record |
| Change-situation wording whose object remains hidden—for example, `transformation`, `change`, `pipeline`, `dataflow`, `flow`, `network`, `circuit`, `path`, `slice`, `workflow`, `process`, or `operation` | Apply `A.3.4.P` when the wording points to a situation of change; recover one `U.Transformation` and its changed referent when that claim is current. For performed work, use A.15.1 and F.6 to identify the dated Work, its Method, time, containing System, every performer, and the assignment under which each acted; then state the work-to-change relation required by the use. A compact rewrite keeps that Work basis and every performer named or recoverable and may omit only an assignment identifier unused by the receiving claim after the attribution is established. A projection omitting other basis refs must say it is partial and retain a source path. For non-work action, recover the relevant actor-side relation. Then recover any separately current method, method description, mechanism, work plan, dated work, functioning or functional structure, `TransformationFlowStructure`, mathematical description, dynamics, temporal aspect, evidence, source, publication, gate, decision, assurance, operation-result binding, measurement-result episteme, evaluation result, `C.11` result, quote-only wording, or other direct claim. | one source-label ontology, generic flow or network head, continuity by source label alone, graph proof, path proof, method by default, work by default, function by default, generic transformer or actor by label, architecture influence as action, universal transformation result, or transformation occurrence by wording alone |
| `holon`, `system`, `episteme`, `collection`, `level`, `boundary`, `interaction`, `functioning`, `capability`, `emergence`, `BOSC`, `MHT`, `MET`, `MFT`, `post`, `promotion`, or close multilevel-holon labels | recover the object kind and relation being claimed: system holon, episteme holon, collection relation, part-whole relation, grounding holon, boundary-crossing relation, transformation relation, functioning or capability relation, architecture relation, control relation, supervisor-subholon feedback relation, interlevel ethical conflict, mediation use, source-label repair, or quote-only source wording. Use `B.2.P` only for emergence-family, MHT-family, MET-family, MFT-family, synergy, metric-mirage, whole-reidentification, and collection wording entangled with those ambiguities; then use `A.1`, `C.2.1`, the part-whole or collection pattern named by value, `B.2`, `B.2.2`, `B.2.3`, `B.2.4`, `B.2.5`, `A.3.4.P`, `A.6.F`, `C.30`, `C.30.ASV`, `C.30.LCA`, `C.30.ILC`, `C.30.STRAT`, `D.2`, `D.3`, `D.4`, or the pattern for the recovered claim | generic holon hierarchy, system-only architecture, episteme-as-document collapse, false level kind, boundary-as-proof, interaction-as-part-whole, emergence as proof word, MHT, BOSC, MET, or MFT as free heuristic, generic loop pattern, promotion as process travel, or `post` as an unexplained new phase |
| `culture`, `cultural evolution`, `style`, `tradition`, `genre`, `scene`, `technique`, `practice`, `platform`, `regime`, `measurement regime`, `attractor`, `developmental machinery`, or close cultural-evolution labels | After the immediate disposition row selects the current object, recover the method family, work family, discipline, canon or memory episteme, recognition or selection rule, mediation system or architecture, measurement or visibility relation, publication label, variant set, dynamics or mathematical-lens claim, exact source or practice boundary, A.1.1 model-use structure, development-loop relation, or cultural-evolution case. When source wording also says *role*, keep ordinary or quoted non-use or apply `E.10.ROLE` and recover the local system-role kind and classification, obtaining `U.SystemRoleAssignment` occurrence, relation among system-role kinds, or another direct relation actually claimed. Apply the rule that defines, constrains, or tests the selected object; use `F.17`, `F.18`, and `F.9` only for term and Bridge work after recovery. | root culture or style kind by label, platform or regime as root ontology, loose attractor metaphor as dynamics claim, genre tree as proof of cultural identity, default role ontology, generic Context object, or replacing one broad source word with another broad FPF-looking word |
| `route`, `path`, `workflow`, `lifecycle`, `dispatch`, `exit`, `receiver`, `call`, `invoke`, `run`, `flow`, `EvidencePath`, or close movement and control metaphors over representations or pattern relations | `C.2.P.DR` repair, `E.18` graph path or `PathSlice`, `A.10 evidence relation or evidence-provenance relation for a claim, effect, or use`, state predicate, checklist predicate, SQL-like query, table representation, dashboard representation, publication face, source-chain relation, carrier file path, mathematical-lens use, method claim, method-description claim, work plan, dated work occurrence, or declarative FPF pattern relation under `E.8` or `F.19` | imperative program, action route, deontic-permission route, work-authorization route, release-authorization route, evidence route, pattern dispatch, or work sequence unless that kind is recovered by value |
| `profile`, `harness`, `catalog`, `registry`, `index`, `map` | profile with a named source-basis relation, evidence-basis relation, architecture-basis relation, or review-basis relation or use; review harness; entry index; registry record; source-ref map with a named map kind and target kind; navigation index; catalog publication; benchmark harness; publication form; companion publication; publication-companion relation; or record kind named by value | pattern or source that defines or constrains a claim, ontology, Method, or release decision unless that exact object is named by value |
| `entry`, `front door`, `corridor`, `route` | navigation aid, recognition entry, navigation-bearing publication, corridor overview, or movement, control, and temporal relation | pattern body, fixed process sequence, release readiness, or proof that the target publication or record is complete |
| `same`, `parity`, `identity`, `equivalence`, `mirror` | same EntityOfConcern, semantic equivalence, bridge relation, version identity, carrier mirror relation, or file mirror relation | similarity, substitutability, no-loss transform, source equality, or authority equality by wording resemblance |
| `file`, `path`, `host`, `packet`, `bundle`, `package` | carrier path, file carrying FPF pattern text, review-facing target packet, review packet with its exact question, scope, and source set, package-form decision, or transport bundle | episteme, publication form, pattern body, review result, `authoritySourceRef` target, pattern that defines or constrains an FPF claim, generic Context, or authority-reference relation |
| `quality`, `characteristic`, `metric`, `indicator`, `score` | `U.Characteristic`, quality term, Q-bundle, scale, indicator, observed value, benchmark, or evaluation record | vague praise, scalar truth, success proof, or replacement for the named characteristic space |
| `slot`, `field`, `row`, `label`, `badge`, `mark` | actual participant of an obtaining direct relation; A.6.5 `SlotSpec` inside a current reusable `RelationSignature`; participant designation only inside a current assertion or relation-occurrence-description episteme; schema field, table row, or C.29 representation element with its represented object and explicit correspondence; publication label; provenance mark; status badge; or cue | kind, world-side participant, obtaining relation, evidence, authority, gate passage, or proof of currentness by position or label alone |
| `EntityOfConcern`, `EntityOfInterest`, `EoI`, `EoIClass`, `describedEntity`, `DescribedEntityRef`, `primary described entity`, or EntityOfConcern-like heads | EntityOfConcern, EntityOfConcern reference, EntityOfConcern class constraint, publication-unit primary entity of concern, source-language wording translated to the adopted EntityOfConcern family, ordinary topic or subject, or project-side kind and reference pair | universal object, second C.2.1 slot family, relation-valued bucket, free publication-unit field, authoring target, carrier, or reader interest |

##### E.10:0.2b.1 - `requirement` and `required` recovery

Treat `requirement` and `required` as trigger wording, not as a shared engineering kind or a durable suffix. Recover the exact construction before rewriting:

1. Name the bearer: the entity, relation, claim, candidate basis, result expectation, dependency position, evaluation state, or accountable subject to which the wording applies.
2. Name the claim or relation kind. Do not stop at `condition`, `item`, `value`, `record`, or another container head.
3. Name the pattern whose rule supplies the recovered construction when that identity matters. A lexical resemblance does not transfer the claim to E.10.
4. State the practical consequence: what use becomes admissible or blocked, which value is current, what return opens, or which accountable commitment exists.
5. Write the recovered construction and rescan the replacement wording. Close with ordinary prose only when no FPF-governed construction is being asserted.

```text
RequirementWordingRecovery:
  GovernedTextSpan:
  BearerRef:
  BearerKindRef:
  ClaimOrRelationKindRef:
  PatternRef?:
  PracticalConsequenceDescriptionRef:
  ExactRecoveredConstructionRef:
  FinalWordingOrBlocker:
```

This is a temporary wording-restoration check, not a project record and not a `Requirement` ontology. Its positions take only the values needed by the recovered construction.

| Current claim behind the wording | Exact recovery and practical consequence |
| --- | --- |
| An accountable subject undertakes a duty, accepts a recommendation-as-duty, or is prohibited under an issuing or authority relation. | `A.2.8 -> U.Commitment`; the commitment changes the accountable subject's declared duty, recommendation-as-duty, or prohibition stance for the stated scope and validity window. |
| A valid grant permits a beneficiary, no prohibition is found in a current sufficiently complete frame, dated work exercises a grant, actual dated work is found not to violate any applicable prohibition in a current sufficiently complete frame, or a same-scope permission conflict is found. | `A.2.8.PER` -> the exact `GrantedPermissionRelation@Context`, `NonProhibitionFinding@Context`, `PermissionExerciseRelation@Context`, `NonViolationFinding@Context`, or `PermissionNormConflictFinding@Context`; do not route it through `U.Commitment`. |
| A subject structure, value, or use must remain inside a stated engineering boundary. | The constraint claim under the pattern that defines it; the constraint blocks or admits the named use and does not create a commitment without an accountable subject and authority relation. |
| A public pattern-use template says which candidate-basis positions must have current fillers. | E.11 `CandidatePatternUseBasisCompletenessCondition@FPFReadme`; it describes positive completeness and does not order a participant to fill a form. |
| One candidate pattern use can precede another only because the first candidate's result is its basis. | E.11.PUR precedence with `prerequisiteResult` and the prerequisite candidate's exact `PatternUseResultExpectation@Context`; no duplicate result-kind field is created. |
| One transformation-flow position depends on another. | E.18.3 `basisDependency` with its exact supporting relation; dependency is not obligation. |
| An improvement loop cannot continue until missing information positions become sufficient. | E.23 `holdUntilInformationBasisSufficient` with non-empty unfilled-position descriptions and one sufficiency condition. |
| A framework-authoring dependency is absent or not current for the next use. | E.4.DPF separates availability from relevance; only a missing dependency carries an acquisition-condition description, and only `missing + currentForNextAuthoringUse` blocks the next authoring use. |
| A candidate framework organization must cover declared relation families for a stated use. | One E.4.DPF constraint claim node with covered family ref-kind pairs, admitted-use description, and coverage-criterion description; any WorkPlan acceptance target remains separate basis. |

Name admission precedes slot verification. `CandidatePatternUseBasisRelation@Context` is admissible because the head exposes the basis relation and its two sides; `CandidatePatternUseBinding` is not repaired by kind-correct fields because `Binding` hides that subject relation. Likewise, `BoundaryConditionKindSlot` names a slot whose values classify boundary conditions; `BoundaryRoleSlot` would falsely suggest a role value. Apply F.18 only when a durable name is actually being minted.

#### E.10:0.2c - Lexical Trigger Rewrite Rules


##### E.10:0.2c.1 - EntityOfConcern, primary entity of concern, and local topic wording

Do not replace every topic-like or object-like phrase with `EntityOfConcern`.
Classify the sentence first.

| If local wording meant... | Rewrite as... |
| --- | --- |
| the EntityOfConcern named by a claim-bearing episteme or episteme-lane `U.View` | the actual `EntityOfConcern` participant under C.2.1; use `EntityOfConcernRef` or `entityOfConcernRef` only when the applicable reference rule requires it, and keep the episteme or `U.View` separate |
| the admissible class constraint on actual EntityOfConcern participants corresponding to one current episteme-constitution declaration | `EntityOfConcernClass` only where that declaration or an EntityOfConcern-preserving law is being applied |
| the primary entity of concern for one bounded `PublicationUnit` | `publicationUnitPrimaryEntityOfConcern` when the unit carries or exposes a claim-bearing episteme or episteme-lane `U.View`; otherwise the non-claim-bearing kind or reference named by value, or plain `topic` or `subject` only when no claim-bearing episteme participant, current A.6.5 declaration, or direct reference use is current |
| wording such as `describedEntity`, `DescribedEntityRef`, `primary described entity`, `EntityOfInterest`, or `EoIClass` | recover the actual `EntityOfConcern` participant under C.2.1, the publication-unit primary-EntityOfConcern use, or the local FPF kind; use `EntityOfConcernSlot` only as an A.6.5 `SlotSpec` inside a current reusable constitution `RelationSignature`; keep `entityOfConcernRef` and `EntityOfConcernRef` under their applicable reference rules; and rewrite to the exact current value among those, `EntityOfConcernChangeMode`, `EntityOfConcernClass`, `publicationUnitPrimaryEntityOfConcern`, or the local FPF kind named by value. If no use can be recovered by value, keep the old wording only as quoted source or trigger wording and block reliance. |
| a review target | `review target`, review-facing target packet named by value, FPF pattern, pattern section, or file-carrier set only when the file-carrier interpretation is being made |
| a local table or paragraph topic with no claim-bearing episteme, C.2.1 participant, current declaration, or reference use | `topic`, `subject`, or direct noun |
| an FPF-side pattern, pattern section, accepted `DRR`, FPF publication, FPF view, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, or companion or projection material being improved | FPF pattern, pattern section, accepted `DRR`, FPF publication, FPF view, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, or companion or projection material |
| a project-side episteme, publication, record, carrier, or activity under work | project episteme, view, or publication named by value, `A.10` evidence relation, typed evidence record, `A.20` constraint or adjudication decision record, `A.21 GateDecision`, `A.21 DecisionLogRef`, `B.3` assurance or engineering-justification record, typed status record whose FPF status pattern is named, `A.2.8 U.Commitment`, exact `A.2.8.PER` permission result, `C.11 ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, one `A.15.1` dated Work occurrence admitted under `U.Work`, a separate episteme about that occurrence, `A.15 U.WorkPlan`, `U.Method`, `U.MethodDescription`, carrier relation, or front-end relation |

Recovery check:

```text
EntityOfConcern rewrite:
  sentence under repair:
  claim-bearing episteme or episteme-lane view used? yes or no
  EntityOfConcern participant; grounding relation; ClaimGraph; viewpoint declaration, assertion, or representation use triggered:
  PublicationUnit primary entity of concern, if any:
  review-target interpretation, process-description interpretation, source-basis-document interpretation, if any:
  source wording retained? yes or no, with reason:
  chosen replacement:
  distinction preserved:
  remaining admissible reader use:
```

##### E.10:0.2c.2 - publication-unit wording that implies authoring or interpretation work

When a phrase makes the bounded unit sound like authoring work or interpretation work, split the sentence by kind under repair.

| If local wording meant... | Rewrite as... |
| --- | --- |
| bounded human-inspected unit inside a publication | `PublicationUnit` |
| the act of writing or editing | authoring or editing Work when one dated occurrence is current; otherwise a planning cue or content inside an already admitted `U.WorkPlan` when only intended work is current. An exact episteme is `U.WorkPlan` only after A.15.2 recovers one present EntityOfConcern, one horizon, at least one `PlanItem`, and substantive coordination claims about possible future performed work. When the sentence instead concerns the authored object, use a separately identified claim-bearing episteme under its own exact kind. Any production or change relation between the Work and that episteme needs its own defining rule or pattern. The authored episteme is `U.MethodDescription` only if its exact EntityOfConcern is one admitted `U.Method` and its claims independently pass A.3.2; the writing or editing act is never the MethodDescription. |
| a pattern body or section | FPF pattern body, pattern section, or `PublicationUnit` of that pattern |
| a file or rendered medium | carrier, front-end, rendering, or document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use |
| a publication form | publication form |
| a generic publication face | generic publication face, or `U.View` only when the relevant view pattern states that relation |
| a declared MVPK face | declared MVPK face, and `U.EpistemeView` only under MVPK constraints |
| a claim-bearing episteme or episteme species named by value | selected `U.Episteme`, episteme-lane `U.View` with explicit episteme tether, or episteme species named by value; when current availability matters, name the exact `EpistemePublicationRelation` occurrence separately |

Do not make a permanent technical modifier by joining authoring, interpretation, and unit-boundary concerns.
That mix hides whether the sentence is about a publication unit, authoring work, reader inspection, or a carried claim.

##### E.10:0.2c.3 - `content`

Do not use `content` as a catch-all head.
Split it into:
- claim-bearing episteme content;
- publication-unit text;
- publication form;
- generic publication face;
- declared MVPK face;
- carrier data;
- payload of a record kind named by the pattern that defines that record;
- pattern section;
- source-basis excerpt;
- review target.

Plain explanatory prose may use `content` only when the sentence does not carry ontology, authority, or admissibility.

##### E.10:0.2c.4 - `publication`

Every FPF-governed `publication` sentence names the publication construction being used:
- act or occurrence of publishing, or publishing work;
- selected `U.Episteme` plus the exact `EpistemePublicationRelation` occurrence when availability to a declared audience for a bounded use is current;
- publication form;
- generic publication face;
- declared MVPK face;
- `PublicationUnit`;
- carrier or rendering;
- document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use;
- external-standard publication;
- project record publication.

If the sentence says a publication "supports", "authorizes", "proves", "permits", or "makes admissible" something, split the basis: fill `relationClaimSlice` when a relation claim is being made, fill `admissibleUse` when a boundary-use claim is being made, and fill `projectSideFPFRef` when project-side records, evidence or provenance relations, gate decisions, constraint or adjudication decisions, assurance records, work, action invitations, speech acts, commitments, methods, or carriers are being used. If either side is not triggered, say so explicitly rather than filling it with generic support.

##### E.10:0.2c.5 - `surface`, `view`, `face`

Do not treat these as synonyms.

| Word | First split |
| --- | --- |
| `view` | `U.View`, `U.EpistemeView`, reader viewpoint, UI view, declared-substrate interpretive view, or review view |
| `face` | generic publication face, declared MVPK face, UI face, or public-facing companion publication |
| `surface` | Treat as trigger wording, not as an accepted Tech head. Recover one of: publication face, publication form, publication unit, carrier, rendering, UI or front-end face, physical or geometric surface, companion publication, companion or projection material, carrier relation, or another FPF object named by value. |

If the sentence can survive only because these are blurred, the sentence is not ready.

##### E.10:0.2c.6 - `source`, `target`

These are relation words, not final kinds.

Recover the relation or use that makes something a `source`; common cases include a selected source `U.Episteme`, exact `EpistemePublicationRelation` occurrence or reference when availability is material, publication form or carrier when either is the source object, `U.View` over a source `U.Episteme`, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, `A.10` evidence relation, authority-reference relation, named FPF pattern cited as source, file carrier, exact source edition, source-local meaning under an effective scheme, source frame only when its defining pattern and endpoint kind are present, the actual source-side participant of an obtaining named relation, the source-side A.6.5 `SlotSpec` only when a reusable relation declaration is current, or project-side FPF kind and reference named by value.

Recover the relation or use that makes something a `target`; common cases include an EntityOfConcern, target `U.Episteme`, review target, FPF rule being applied, project target, work target, target publication form, project-side FPF kind and reference named by value, target frame, target-side situation or model-use boundary only when its defining rule is current, the actual target-side participant of an obtaining named relation, or the target-side A.6.5 `SlotSpec` only when a reusable relation declaration is current.

Generic `object` and `target` are not final recovered kinds. Keep them only when the sentence explicitly declares a named field or participant designation inside a current episteme, such as `ObjectKindUnderImprovement`, `ObjectVersionUnderImprovement`, or `ObjectVersionUnderQualityEvaluation`; names a `review target`; or states one direct-relation participant meaning whose actual-participant kind is supplied by value nearby. If a reusable relation declaration is current, name its A.6.5 `SlotSpec` separately. When the governed kind is known, write that kind by value: FPF pattern version, `DRR`, FPF corpus slice, publication form, `PublicationUnit`, file carrier, system carrier, exact changed referent, exact entity or value bound as the result of one particular `A.6.1` operation application, candidate proposal, evidence or provenance relation, gate decision, work plan, method description, object-under-improvement evaluation, or another named FPF kind.

Do not recover an FPF pattern, publication form, `PublicationUnit`, pattern body, or view as a `carrier`. `U.PresentationCarrier` is the publication-side carrier kind used under E.17 and E.24.PUB; ordinary carrier wording names the relation to the system, medium, file, rendering, front end, or transport object that bears or renders a publication or symbol. If the text means the FPF pattern publication form, write `FPF pattern publication form`; if it means the file, rendered, front-end, or transport side, name that exact carrier or relation.

Common repair examples:

| Problem wording | Recovery needed |
|---|---|
| `target version` in improvement prose | `ObjectVersionUnderImprovement` or `ObjectVersionUnderQualityEvaluation`, unless `target` is quoted source wording |
| `pattern carrier` | `FPF pattern publication form` when the pattern is the publication form; file carrier or rendering only when the system-side bearer is being claimed |
| `object evaluation` when the evaluated kind is known | object-under-improvement evaluation name, such as `PatternQualityQBundle`, `DRRDecisionAdequacyEvaluationCharacteristicSpace`, `FPFPillarAdequacyEvaluationCharacteristicSpace`, or declared local evaluation |
| `thing`, `object`, `target`, `artifact`, or `material` as final head | FPF kind named by value, project-side FPF kind, or blocker |

Do not publish "source and target" if the selected relation needs the actual FPF kind.

##### E.10:0.2c.7 - `input`, `raw material`, `source data`, `source material`, `artifact`, `output`, `result`, `outcome`, `deliverable`

These are high-risk relation-dependent source-word umbrellas, not final kinds or one result family. First name the exact entity and the exact object relative to which the word is being used. For epistemic `source data` or `source material`, close the exact source expression, episteme or publication, and source-to-use relation under `C.2.P` first. For physical raw material, name the relevant constituent, affected-referent, resource-use, supply, transfer, or transformation relation and use the pattern that defines it.

When the remaining current claim is relative to a method, plan, dated work, transformation, evaluation, delivery, transfer, or receiving use, apply `A.6.P.WMR`. Recover claim subject, modality and exact temporal extent, polarity, and recovery/support state independently. Closure is exactly one of four truthful families: an exact direct subject-relation claim, positive or governed negative; an exact `A.6.1` operation-application binding; an exact local `A.15.PROD` or `A.6.RCD` claim; or an exact non-assertability result whose reason is independently `factually unsupported`, `missing-information`, or `missing-governor`. A failed known predicate and an unavailable fact keep their known governor and name no future subject pattern or relation declaration; only a genuinely absent predicate, condition, or defining pattern or declaration names the affected receiving use and future subject pattern or relation declaration. Classification, a generic `result relation`, a method-description field, planned filling, a designation that merely type-checks against an A.6.5 `SlotSpec`, or a polarity inference is not closure.

Before opening that branch, test whether the phrase already names an independently identified `U.Episteme`; `U.View` or `U.EpistemeView`; publication form; publication face, including a declared MVPK face; `PublicationUnit`; carrier, front-end, or rendering relation; project-side FPF kind and reference named by value; evidence carrier or evidence relation; document under a named source-basis, evidence-basis, architecture-basis, or review-basis relation or use; review target; `C.11` `ChoiceResult`; measurement-result episteme; evaluation result; diagnostic finding; decision; or another project object whose record kind and defining rule are named by value. Retain ordinary `input`, `output`, `result`, `outcome`, or `deliverable` only while the exact defining relation rule remains recoverable. If no governor closes the selected WMR claim, return the bounded blocker. If the missing item is instead a non-WMR kind, retain an architecture-first candidate disposition under the pattern that defines that candidate. Do not invent either one inside pattern prose or replace it with a universal kind or relation.

##### E.10:0.2c.8 - `record`

Use `record` only when an FPF pattern or project practice defines the record kind and relation. The nearby wording says which FPF kind the record instantiates or records, for example:

- `A.10` evidence or provenance relation or evidence record for a named claim;
- `A.21` `GateDecision` or `DecisionLogRef`;
- `A.20` constraint or adjudication decision record;
- `C.11` `ChoiceResult` or decision record;
- `A.15` `U.WorkPlan`, one `A.15.1` dated Work occurrence admitted under `U.Work`, or a separately identified claim-bearing episteme about that occurrence; use a record-kind name only when its exact kind and defining record rule are recoverable;
- `A.2.8 U.Commitment`, exact `A.2.8.PER` permission result, or `A.2.9 SpeechAct` publication;
- a separately identified assignment-assertion or occurrence-description episteme that designates one exact `RA : U.SystemRoleAssignment`, or a status-register entry under its named status pattern; neither record is the world-side assignment occurrence;
- `E.19` review run record or another named review record whose review target and review relation are explicit;
- process run record in process documents.

Do not let `record` mean "any file that remembers something", "the missing source", or "the thing to create when support is absent". If a named support relation cannot be asserted because a required actual participant or value is absent, name that exact missing participant or value. If a reusable declaration is incomplete, name its missing `SlotSpec` or other missing declaration content and repair that declaration. If a receiving assertion or relation-occurrence-description episteme lacks a participant designation, name the missing designation under that episteme. If a `U.WorkPlan` lacks a planned participant designation or planned value, name that missing plan content under the WorkPlan. Create a prospective repair request, future decision request, prospective work-plan entry, or explicit missing-source-relation note as applicable; none backdates support, establishes actual participation, or makes the direct relation obtain.

##### E.10:0.2c.9 - `model`, `diagram`, `screen`, `dashboard`, `table`, `note`, `memo`, `summary`, `explanation`

These are recognition examples, not kinds.
Classify each occurrence as one of:
- episteme or episteme publication;
- `U.View`, `U.EpistemeView`;
- publication form;
- generic publication face;
- declared MVPK face;
- `PublicationUnit`;
- carrier, front-end, or rendering;
- project-side FPF kind and reference named by value;
- explanation and source-finding relation under `E.17.EFP`;
- evidence, currentness, and provenance relation under `A.10`;
- gate-bearing claim or effect under `A.20` or `A.21`;
- assurance and engineering-justification record under `B.3`;
- work- or reliance-guiding appearance whose missing prerequisite is recovered under `A.15.4`.

Keep the ordinary example word only after the actual kind is visible nearby.

##### E.10:0.2c.10 - `reader`, `reviewer`, `author`, `operator`

Do not use people-position words as hidden kind names.

Use:
- `working reader` or `intended practitioner` for ordinary usability;
- `engineer-manager` when the FPF use case is the engineer-manager applying the pattern in work;
- `reviewer` only for a participant in a named review relation; use review process, review gate, or review target for the process, gate, or object;
- `author` only for authoring or editing work;
- *operator* only after the claim is recovered: it may name an admitted system classified under an exact local `OperatorSystemRole`, a process or mathematical operator, an organizational or interface position, an ordinary title, or another direct relation; the word alone selects none;

If a text says "reader-facing" or "review-facing", it also names what is facing that person: generic publication face, declared MVPK face, packet, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, `PublicationUnit`, carrier, or UI or front-end.

##### E.10:0.2c.11 - `owner`, `home`, `host`, `locus`

These are not interchangeable.

Keep *owner* as ordinary architectural, organizational, policy, source-maintenance, or stewardship wording when the sentence already makes the precise ownership or responsibility relation and its participants clear. Otherwise name that direct relation. *Owner* does not mean a system-role kind, `U.SystemRoleAssignment`, authority, or Work by default, and it is not a substitute for `pattern`, `DRR`, selected `U.Episteme`, exact `EpistemePublicationRelation` occurrence, publication form, publication unit, file carrier, or project record.

Split the actual claim into the smallest applicable value:
- exact architectural, organizational, policy, source-maintenance, stewardship, ownership, or responsibility relation and participants;
- relation to an FPF pattern or an authority-reference relation;
- named source set used as authority for the claim;
- file carrying FPF pattern text, file carrier, or publication unit;
- evidence record or evidence source;
- FPF pattern or project target;
- support root; or
- ordinary or quoted non-use when *owner* is only title-like wording; otherwise use the result selected through `E.10.ROLE`—for example, a local system-role kind and classification, a named `U.SystemRoleAssignment` occurrence, or another relation.

Never use *owner* to avoid deciding which of those claims the sentence makes.

##### E.10:0.2c.12 - `route`, `branch`, `handoff`, `path`, `trajectory`, `move`, `flow`

Recover the movement, control, and temporal relation set before using these words:
- `E.10.MOVE` for project-move, first-move, working-move, next-move, pattern-use, work-entry-readiness, architecture-candidate-use, call-planning next-action, or other move-like wording whose direct FPF target is hidden;
- `A.16` local move;
- `A.16.0` trajectory account;
- `A.19`, `C.2.2a` position in characteristic space or state space;
- `B.2.5` control relation, control-layer relation;
- process handoff;
- selector relation or selection mechanism;
- work transfer;
- `E.18` graph path or `PathSlice` expression;
- `A.6.3`, `A.6.4` episteme morphism or retargeting.

When `handoff` instead names an entity, package, result, delivery, transfer, acceptance, or receiving-use boundary, apply `A.6.P.WMR` to that exact relation-bearing claim. Use `E.10.MOVE` for a process-baton or project-move case only when that movement itself is current; a handoff record or package remains an episteme or another entity, not the transfer.

If no movement, control, and temporal relation is being made, keep the word ordinary and non-authorizing.

##### E.10:0.2c.13 - `use`, `supported use`, `action`, `effect`

Split the word before accepting it:
- applying an FPF pattern to a problem situation;
- interpreting or using a publication, view, record, cue, or carrier;
- relying on a named project episteme, a named source-basis document, or a project-side FPF kind and reference named by value for a named claim or effect;
- admissible act, work, or claim under a named FPF pattern; an obtaining direct relation recovered through `A.6.P` with its actual participants named; a literal or source-local relation phrase retained only as wording; or a project-side FPF kind and reference named by value;
- non-admissible act, work, or claim requiring one other named value: FPF pattern; an `A.6.P`-recovered direct relation with its actual participants; a literal or source-local relation phrase identified only as wording; project-side FPF kind and reference named by value; `C.11` `ChoiceResult`; `C.11` decision record; `A.6.A` action invitation; `A.15` `U.WorkPlan`; one `A.15.1` dated Work occurrence admitted under `U.Work` or a separate episteme about it; `U.Method`; `U.MethodDescription`; `A.20` constraint or adjudication decision record; `A.21` `GateDecision`; `A.21` `DecisionLogRef`; `A.10` evidence relation; typed evidence record; `B.3` assurance or engineering-justification record; typed status record whose FPF status pattern is named; carrier relation; or front-end relation;
- planned work;
- an actual Work occurrence admitted under `U.Work`, kept distinct from any assertion or record about it;
- evidence of interpretation or effect;
- gate or admission decision.

Do not let `supported use` become a generic capability of a document.
The FPF-governed wording names the `admissibleUse` target named by value and non-admissible stronger or adjacent use, `relationClaimSlice` when a relation claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used.
If the sentence says "supported", conforming wording names the `admissibleUse` target named by value and non-admissible stronger or adjacent use, `relationClaimSlice` when a relation claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used. Do not satisfy the rule by naming only a project record, evidence record, gate record, assurance record, engineering-justification record, only an FPF pattern, or one mixed project-side entry when several values defined or constrained separately are being used—for example an exact local system-role kind or `U.SystemRoleAssignment` occurrence, `U.Method`, `U.WorkPlan`, and actual `U.Work`.

##### E.10:0.2c.14 - `sign`, `concept`, `denotat`, and school-semiotic labels

Do not import the school-semiotic triad as architecture ontology.
When a source or review text says `sign`, `signifier`, `signified`, `concept`, `denotat`, `representamen`, `interpretant`, or `sign vehicle`, apply the composite recovery order before the term appears in FPF-facing prose.

Possible recoveries include:
- `U.Episteme` or episteme species named by value;
- selected `EntityOfConcern`, grounding, reference-plane relation;
- `U.View`, `U.EpistemeView`;
- publication form, generic publication face, declared MVPK face, or `PublicationUnit`;
- carrier, front-end, or rendering;
- cue, displayed wording, mark, status display, credential display, provenance mark, signature evidence;
- evidence record, gate record, work-state record, commitment record, separate assertion or occurrence-description episteme about one exact `U.SystemRoleAssignment`, or another project-side FPF kind and reference named by value;
- FPF pattern, pattern section, accepted `DRR`, FPF publication, or FPF view when the object is on the FPF side.

Use `concept` only where current `FPF` already has the relevant concept-set, UTS, local-meaning, or Part F machinery available.
Otherwise recover the claim-bearing episteme; the obtaining direct relation and actual participants; the current A.6.5 declaration, participant designation, or C.29 representation and explicit correspondence when one of those is actually present; or the record kind and defining rule named by value.

##### E.10:0.2c.15 - `pattern`, generic FPF-side object wording, `locus`, `row`, `target`

`Pattern` is not a free synonym for regularity.
If the intended object is an FPF pattern, write `FPF pattern` or name the concrete pattern and what it contributes.
If it is not an FPF pattern, do not write `recovered FPF construction` as the final value. Choose one recovered value by sentence function: episteme, view, publication, publication form, generic publication face, declared MVPK face, `PublicationUnit`, carrier relation, front-end relation, project-side FPF kind and reference named by value, document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use, review target, obtaining direct relation and actual participants, receiver-needed relation occurrence, reusable `RelationSignature` and A.6.5 `SlotSpec` values, claim-bearing episteme with any current participant designations, C.29 representation element and explicit correspondence, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, one `A.15.1` dated Work occurrence admitted under `U.Work` or a separate episteme about it, `U.Method`, `U.MethodDescription`, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `A.10` evidence relation, typed evidence record, `B.3` assurance or engineering-justification record, or typed status record whose FPF status pattern is named.

Avoid generic FPF-side object wording, generic named-target wording, `locus`, `row`, and `host` when they hide kind.
Use them only when the kind is literally a table row, document with named source-basis relation or use, file carrying FPF pattern text, or review target and the sentence does not need a narrower FPF kind.
For FPF-facing wording that carries a claim being made, direct relation, admissible use, or remaining reader use, these are candidate recoveries, not a group kind: FPF pattern, pattern section, accepted `DRR`, FPF publication, FPF view, record kind with its defining rule, obtaining direct relation and actual participants, receiver-needed relation occurrence, claim-bearing episteme, reusable A.6.5 declaration, or C.29 representation and explicit correspondence. Choose one by sentence function and keep the different objects separate.

##### E.10:0.2c.16 - Union-field unpacking under A.6.P

Do not write `authority-bearing FPF pattern`, `authority-bearing FPF row`, `FPF row named by value`, `selected FPF pattern, record, or relation`, `governing FPF relation`, or `required project record or action` as final fields.

When one of these union-fields appears, make the A.6.P choice explicit:
- if the sentence is making a relation claim, recover the `RelationKind`, actual participants, qualifiers, scope, time, viewpoint, and admissibility target, then state the obtaining direct relation and those participants; distinguish one relation occurrence only for a named receiving use; add a reusable `RelationSignature` and A.6.5 `SlotSpec` values only when declaration is current; and keep any claim-bearing row or field as an assertion episteme, participant designation, or C.29 representation and explicit correspondence as its own assertion or representation rather than as the relation itself;
- if the sentence is not making one relation claim, unpack the wording and claim under repair into an FPF-side kind, reference, or relation named by value and one project-side FPF kind with its reference, or state that no project-side FPF kind is triggered;
- if the same unpacking recurs across cases with one stable recovery shape, record a light A.6.P specialization candidate rather than minting a vocabulary-wide replacement field.

Apply this unpacking whenever a publication, display, cue, explanation, dashboard tile, schema, signature, badge, or generated output is being read as evidence, gate passage, work, deontic permission, work authorization, approval speech act, commitment, release authorization, safety assurance, evidence sufficiency, or engineering justification.

Do not fill one authoring union-field position with whichever nearby FPF kind is easiest to name. A project publication, claim-bearing episteme, or record with a named kind and defining rule is a description-side object; one `A.15.1` dated Work occurrence admitted under `U.Work` is a world-side individual, while `A.6.A` action invitation, `A.2.9` `SpeechActRef`, `A.2.8` `U.Commitment`, `U.Method`, and `U.MethodDescription` belong to other kinds or relations.

##### E.10:0.2c.17 - Heterogeneous kind lists

Do not repair a heterogeneous list by giving it one broader umbrella name.
When a sentence lists unlike candidates such as pattern, `DRR`, publication, `U.View`, carrier relation, front-end relation, project-side FPF kind and reference named by value, `C.11` `ChoiceResult`, `C.11` decision record, `A.6.A` action invitation, `A.15` `U.WorkPlan`, one `A.15.1` dated Work occurrence admitted under `U.Work`, a separate claim-bearing episteme asserting a fact about that Work occurrence, `U.Method`, `U.MethodDescription`, `A.20` constraint or adjudication decision record, `A.21` `GateDecision`, `A.21` `DecisionLogRef`, `A.10` evidence relation, typed evidence record, `B.3` assurance or engineering-justification record, or typed status record whose FPF status pattern is named, do not promote the row to a new kind. Classify the list as one of:
- one kind under repair selected at bounded complete generality;
- several obtaining direct relations with actual participants;
- a reusable relation-declaration set with exact `RelationSignature` and A.6.5 `SlotSpec` values;
- a C.29 tuple representation with explicit represented objects and correspondences;
- several alternative cases;
- an indicator of failed ontology.

If the list asserts several direct relations, name each obtaining relation and its actual participants. If it declares reusable relation shapes, name each `RelationSignature` and A.6.5 `SlotSpec` value and do not infer that any relation obtains.
If it is a C.29 tuple representation, name the representation elements, represented objects, and explicit correspondences; if the same material is also a reusable relation declaration, name its `RelationSignature` and A.6.5 `SlotSpec` values separately.
If it is an alternative-case set, split the cases.
If it is failed ontology, repair the architecture before pattern or `DRR` prose depends on the list.

##### E.10:0.2c.18 - `strong`, `stronger`, `weak`, `weaker`, `support`

Do not use strength metaphors unless a named FPF scale, evidence class, threshold, or characteristic space is being used.

Preferred rewrites:
- `stronger claim` -> wider claim scope, higher evidence-basis threshold, gate or admission threshold, claim requiring world-contact evidence or authority relation, authority claim, or named evidence-support class;
- `weaker claim` -> narrower claim scope, lower evidence-support class, bounded admissible act, work, or claim, `source-loss mode` under `A.6.3.CSC` when a source-to-rendering loss is being claimed, coarsened rendering, or explicit abstain or reopen condition;
- `support` -> keep ordinary or quoted source wording when no FPF claim relies on it. Otherwise recover the claim before replacing the word; do not coin a generic `SupportRelation`. If the reading is base, anchor, or basedness, apply `A.6.6` and state `dependent`, `base`, `baseRelation`, `scope`, applicable `Γ_time`, witnesses, `admissibleUse`, and `nonAdmissibleUse`.

For FPF-governed `support`, test the direct-subject branch before consulting the common alternatives. Ask whether the sentence states a recognizable fact between subject-domain things rather than evidence, assurance, admissibility, work help, or reader help. If it does, name the things and say plainly what relation obtains between them; these are the actual participants and direct predicate. Apply the rule that defines or constrains that relation. If the relation or a participant remains unclear, use `A.6.P` to recover it. Once the participants and needed predicate are clear, use `A.6.RCD` only when no current pattern defines or constrains that predicate.

When the sentence is not already a recognizable direct subject relation, the following are common alternatives, not a complete list:
- source-description relation: a source episteme, publication, view, model, graph, trace, generated representation, or document describes, exposes, renders, cites, or makes inspectable one claim-bearing item;
- EntityOfConcern or grounding-holon grounding: the claim-bearing episteme, view, representation, or pattern application is grounded in its actual EntityOfConcern participant, actual grounding holon, local world contact, or observation setting; `EntityOfConcernSlot` and `GroundingHolonSlot` remain A.6.5 `SlotSpec` values only inside a current reusable declaration and do not constitute those participants;
- base, anchor, or basedness relation: the phrase means relative-to, based-on, anchored-in, base change, or scoped grounding as a base relation; use `A.6.6` support wording selection and rewrite as `baseRelation(dependent, base)` or SWBD, not as a generic `SupportBasis`, `SupportRelation`, or `SupportRecord`;
- evidence or witness support: an evidence-use relation, evidence-provenance relation, witness relation, witness carrier, observation, test, observation record, or test record bears on a claim;
- assurance or engineering-justification support: an assurance argument, trust calculus, safety case, or engineering-justification claim is being made;
- causal-use relation or evidence relation: a causal-use question, rung, estimand, the separate evidence/identification/estimate/sampling/simulation components actually used, a C.28 support result, supported use, and unsupported use are being claimed;
- mathematical-lens use or lens-use admissibility: a mathematical lens, mapping, similarity, or formal object makes a bounded claim admissible or exposes preserved structure and lost structure;
- characteristic, measurement, threshold, or comparison basis: a characteristic, metric, scale, benchmark, threshold, or comparison basis is being used;
- admissible-use or boundary-use basis: the sentence says what use, act, claim, publication use, or reliance is admissible;
- work, enablement, prerequisite, resource, or operational help: one thing helps, prepares, routes, resources, enables, or makes work easier without evidence, authority, truth, or admissibility claim;
- publication companion, entry, navigation, or reader help: a file, section, index, map, review packet, support document, or companion helps readers find, inspect, compare, or review another item.

Write the concrete sentence before selecting a predicate or pattern locator. `Test T supports claim C` becomes `Test T is evidence for claim C`; use `A.10` for that evidence relation. `Index I supports readers` can become `Index I helps readers find section S` and remains bounded reader help; it does not establish the truth of section S. `Column C supports roof R` remains a structural claim: state the structural relation it asserts, for example that C bears R's load, and use the pattern that defines that relation. If its relation or a participant is unclear, use `A.6.P`; if both are clear but no current pattern contains the defining content for the predicate, use `A.6.RCD` and return the established `missing-governor` result.

For a common alternative, use the applicable pattern once the sentence names the things involved, what one does for the other, the permitted use, and the blocked stronger conclusion. Use `C.2.P` and the relevant description, source-use, grounding, or publication pattern; `A.6.6` for basedness; `A.10` for evidence; `B.3` for assurance; `C.28` for causal use; `C.29` for mathematical-lens use; `C.16` for characteristic, measurement, threshold, or comparison construction; or the pattern for the stated admissible use, work, resource, publication companion, or reader help. Do not use `A.6.P` to choose one of these common lexical alternatives again.

Support-headed names such as `SupportRecord`, `SupportSource`, `SupportLine`, `SupportForm`, a support phrase that hides a state-family claim, `SupportSection`, `SupportMaterial`, `support basis`, `support relation`, `support view`, and `supported use` are diagnostic triggers. They are conformant only when rewritten to the specific object under the pattern that defines the recovered claim: a claim-bearing episteme or record kind named by value; an A.6.5 `SlotSpec` only when a reusable declaration is current; a publication function; a state-family value under `A.19.SPR` only when that claim is current; an obtaining direct relation and actual participants; an admissible-use boundary; or, for the A.19 case, `DeclaredSubstrateInterpretiveView` under `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW`. If the phrase is base-dependence, A.6.6 defines the basedness construction and conforming text exposes `dependent`, `base`, `baseRelation`, `scope`, applicable `Γ_time`, witnesses, `admissibleUse`, and `nonAdmissibleUse`. Otherwise rewrite the head to the selected interpretation: source-description relation, EntityOfConcern grounding, grounding-holon relation, evidence-provenance relation, source-use relation, source-currentness claim, source adoption decision, source adaptation decision, source rejection decision, obtaining direct relation and actual participants, admissible-use boundary, assurance claim, C.28 causal-use relation or causal-use verdict, C.29 lens-use output, C.16 characteristic construction, measure relation, comparability relation, bridge card, comparison card, work enablement relation, publication companion, or ordinary reader help.

A support-headed phrase selected by an accepted `DRR`, pattern authoring draft, table heading, schema field, coordinate name, or selected reusable authoring vocabulary already requires an `F.18` naming decision unless the text explicitly marks it as source-only, quote-only, or rejected. Do not accept `subject to F.18 later` as `E.10` closure when the phrase is already being used to guide authoring, review, landing, or reusable FPF wording. Either complete the naming decision now, replace the head with the selected interpretation named by value, or leave the naming issue blocking by value.

If no FPF claim relies on `support`, keep the ordinary or quoted wording and do not invent an ontology for it. Otherwise the reader must be able to say what supports what, in what sense, for which use, and what must not be inferred. Keep a recognizable direct subject relation in its domain and choose a common lexical alternative here in `E.10:0.2`. Use `A.6.3.CSC` for a source-loss mode and `C.2.P` for the source expression and its use. Use `A.6.P` only when the direct predicate or a participant remains unclear; once both are clear, use `A.6.RCD` only when no current pattern defines or constrains that predicate.

##### E.10:0.2c.19 - Applying patterns versus procedural calls

FPF patterns provide reusable guidance for recognizable problem situations. In ordinary prose, `apply pattern P` is acceptable metonymy for a person or system using the method, rule, test, constraint, or lookup described by P; the pattern itself does not perform the project action.

**Ordinary application.** Name the recognizable problem, state the concrete contribution taken from the pattern, and state the resulting user action or judgement. An ordinary PatternID citation is enough when the reader only needs to find that contribution. Do not require an ontology, conformance claim or section, exact assertion, `ClaimGraph`, or formal application record merely to use the guidance.

**Identity-sensitive application.** Open this branch only when a named live alternative or receiving use changes truth, action, stop, interpretation, migration, publication, reuse, or reliance. Name that dependency first, then add only the identity it needs: for example, the exact pattern edition, ontology, conformance claim or section, governed object, claim-bearing episteme, obtaining relation and participants, current declaration, or representation and correspondence.

Use `apply pattern`, `use the pattern guidance`, `the pattern applies to this problem situation`, or `the case falls under this pattern` for the ordinary FPF-side use. These expressions do not assert that the pattern acts.

Do not leave `project action` as final wording when it hides a distinction that changes the current claim or use. For ordinary project-side activity, say plainly who does what and what result or judgement follows. When a current claim or receiving use depends on formal classification, choose exactly one applicable kind or relation: `U.Method`; `U.MethodDescription`; `U.Mechanism`; `A.15` `U.WorkPlan`; one `A.15.1` dated Work occurrence admitted under `U.Work`; a separate claim-bearing episteme asserting a fact about that Work occurrence; exact entity plus a direct relation involving that occurrence recovered through `A.6.P.WMR`; exact `A.6.1` operation-application binding; local `A.15.PROD` claim; measurement-result episteme; evaluation or diagnostic finding; `C.11` `ChoiceResult`; `C.11` decision record; `A.6.A` action invitation; `A.20` constraint or adjudication decision record; `A.21` `GateDecision`; `A.21` `DecisionLogRef`; `A.10` evidence relation; typed evidence record; `B.3` assurance or engineering-justification record; typed status record whose FPF status pattern is named; carrier relation; front-end relation; or another accepted project-side FPF kind.

Keep `route`, `path`, `branch`, `handoff`, `trajectory`, `move`, or `flow` as ordinary navigation wording when no FPF movement, control, or temporal claim depends on it. When such a claim is current, name the relevant movement, control, and temporal relations and use the pattern that defines them.

##### E.10:0.2c.20 - FPF-side and project-side epistemes and publications

Semioarchitecture often talks about two different groups of epistemes, publications, records, and uses:
- FPF-side material: `FPF` as episteme, FPF patterns, pattern sections, `DRR`s, FPF publications, FPF views, support documents and documents with named source-basis, evidence-basis, architecture-basis, or review-basis relations or uses, and review targets;
- project-side material: the engineer-manager's project epistemes, publications, views, records, carriers, cues, evidence records, `A.20` constraint or adjudication decision records, `A.21` gate decisions, `A.21` decision-log refs, `B.3` assurance or engineering-justification records, commitments, one `A.15.1` dated Work occurrence admitted under `U.Work` plus any separate episteme about it, `C.11` `ChoiceResult` values, `C.11` decision records, and `A.6.A` action invitations.

Do not blur them with `source`, `artifact`, `object`, `material`, `target`, `pattern`, or broad `semiosis`.
If both sides are being used, split the sentence into `relationClaimSlice` when a relation claim is being made, `admissibleUse` when a boundary-use claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used.
If one side is not being used, state `not triggered` rather than leaving a placeholder.

##### E.10:0.2c.21 - `decision`, `action`, `work`, `method`, `plan`

Do not let `action` cover every project-side event. An action nominal such as `testing`, `assembly`, `maintenance`, `evaluation`, or `inspection` is a morphology cue, not a kind. Placement in function- or flow-structure prose identifies no `U.Function`: apply `A.6.F` when the function-like use remains claim-bearing and its FPF object or relation is hidden; otherwise name the already recovered method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, exact Work occurrence, or other value under the pattern that defines it. A WBS element, activity, or Work Package remains plan- or assignment-episteme content about intended work; none of these uses identifies an actual Work occurrence admitted under `U.Work`.

Split decision-making and decision records under `C.11`; local system-role-kind classification under A.2; `U.SystemRoleAssignment` occurrences under A.2.1; Method under A.3; planned work and WorkPlan under `A.15.2`; dated Work occurrences under `A.15.1`; actual launch or performed values under obtaining direct relations or A.6.1 bindings; separate performed-work, finalization, result, telemetry, and gate records under the patterns that define them; action invitation under `A.6.A`; communicative acts under `A.2.9`; commitments under `A.2.8`; and strong grants under `A.2.8.PER`. A method-description field, planned filling, compatible type, ticket, or nearby result record establishes no actual participant relation.

A reusable name for performed work goes to `F.18` only after A.15.1 and F.6 identify the Work occurrence, its time, Method, containing System, each performer, and the assignment under which each acted. Keep the affected referent, application bindings, resource use, and other direct facts separately recoverable. Add a continuity policy only when occurrence identity matters. Keep production, measurement, evaluation, delivery, acceptance, and downstream-effect claims under their direct patterns.

P2W language from `E.18` transformation-flow structure is not a generic `source-to-work` slogan. Use it only when the chain from principles, theories, and signatures through method choice, work planning, work execution, separate measurement or evaluation, and cycle return is actually being made.

##### E.10:0.2c.22 - Whole-corpus trigger use

When a whole-corpus cleanup is selected, use this pattern's trigger guide over claim-bearing FPF text and project text that deliberately uses FPF-governed terms, pattern references, relation names, or conformance claims.

Do not do a global string replacement. Classify each unclear term occurrence by the bounded complete rewrite mode and preserve accepted FPF names unless a separate accepted naming decision changes them.

##### E.10:0.2c.23 - `case`, `scenario`, `example`, `pilot`, `anti-case`

These words are useful for recognition and testing, but they often hide whether the text is talking about a project situation, evidence, a worked slice, a negative control, or a decision basis.

Split before use:
- working problem situation;
- worked case or example;
- pilot case;
- anti-case, negative control;
- evidence case;
- comparison case;
- source example;
- benchmark case;
- candidate corpus example.

A case can illustrate or test a pattern.
It does not by itself become evidence, a pattern, a `DRR`, a source basis, or an authority-reference relation.
If the case is being used to justify a claim-bearing text change, choose and name each EntityOfConcern under repair or relation separately: evidence record or evidence-provenance relation, decision basis or decision record, authority relation, relation to the FPF rule actually applied, or relation to an accepted `DRR`.

##### E.10:0.2c.24 - `basis`, `context`, `scope`, `frame`

These words can hide different subject questions; they do not name one common kind.

- For *basis*, name the source or direct relation actually used by the sentence—for example, a decision, evidence, comparison, threshold, grounding, or admissibility relation.
- For *context*, apply `E.10.D1` and recover the subject-defined content that changes the action—for example, a scheme, scope, model-use structure, situation, design-time or run-time referent, architecture, environment, domain subject, or local-practice use.
- For *scope*, use `A.2.6` when an actual claim scope and its slice-membership facts are current; otherwise use the subject pattern for the stated extent or boundary.
- For *frame*, say what the word refers to—for example, a viewpoint, reference frame, comparison frame, state frame, or ordinary narrative framing.

If a basis changes what may be done, state the admissible use. State a relation claim or project-side FPF reference only when the sentence actually makes that claim. If *context* hides the EntityOfConcern, recover that entity and the subject relation before any Bridge, parity, or identity claim.

##### E.10:0.2c.24a - translation and multilingual heads

A bilingual alias is not a Bridge by itself and does not create equivalence, substitution, UTS admission, or a cross-local naming relation.

When translated wording has FPF-governed use, recover the FPF kind named by value, local head, publication construction, source relation, and admissible use before accepting the translation. A translated explanation is a derivative rendering; operative claims need claim-bound source relations and `E.17.EFP` or `A.10` when reliance use is being made. A translated `PublicationUnit` may preserve form while shifting `publicationUnitPrimaryEntityOfConcern` or carried publication move; apply `E.17.AUD` or `E.17.AUD.OOTD` when that shift is being claimed. Local translated heads may use `E.17.AUD.LHR` or `C.2.P` without full `F.18` unless durable cross-local naming, a UTS row, a Core-facing term, or a reusable FPF head is intended.

##### E.10:0.2c.25 - `state`, `status`, `posture`, `readiness`

E.10 only recognizes the wording problem; it does not duplicate the recovery procedure. If `readiness` or `ready` still hides which governed value is meant, use `E.10.MOVE`. It exits to `A.19.SPR` only for a hidden bearer and state frame, to `A.2.5` for an assignment-state condition, to `A.15.5` for work-entry readiness, to `A.21` for a distinct gate decision, or to another direct pattern for the recovered claim.

For other state-family wording, use the direct pattern when the exact object and claim are already clear. Use `A.19.SPR` only while the object, state frame, or value remains hidden. Close with an ordinary statement of the recovered object and claim under that pattern; introduce a predicate only when the pattern defines or needs one. Otherwise keep ordinary prose, quote-only wording, a reduced-use cue, or a blocker.

##### E.10:0.2c.25a - `live`, `current`, `active`, and status or article overwrap

`live`, `current`, `active`, `open`, `pending`, and similar status-like modifiers are trigger wording when they attach to `pattern`, `record`, `object`, `field`, `operation`, `route`, `locus`, `move`, `text`, `claim`, `question`, `use`, or `relation` without saying which exact bearer and state or currentness value, temporal qualifier of an obtaining direct relation or assertion, source or use relation, or claim function the modifier adds.

First recover whether the modifier expresses a real FPF value:

- If `readiness` or `ready` still hides which governed value is meant, use `E.10.MOVE`; use `A.19.SPR` only if that recovery leaves a hidden bearer and state frame. For source currentness, another state or status, publication-use disposition, quality result, admission state, campaign state, or process state, use `C.2.P`, `E.9.DA`, `E.21`, `E.19`, the release or process carrier, `A.19.SPR` while its object or state frame remains hidden, or the direct pattern for the recovered value.
- If it means a claim, question, use, or relation is currently asserted, relied on, or action-bearing in the described situation, keep the modifier only when the sentence also names the claim or claim-bearing episteme, obtaining relation or source/use relation, admissible use, and—when needed—the pattern that defines it, or says why ordinary prose is enough.
- If it only points to "the thing under discussion", treat it as phrase-level apparatus and apply `F.19`: write `the pattern`, `pattern of concern`, record kind named by value, affected field, operation claim, relation claim, or other object named by value instead of `live X`.
- If it is development, review, projection, landing, or current-campaign state about an FPF pattern version, keep it in the process, quality, projection, release, or campaign carrier rather than in the pattern unless that state is the pattern's own primary `EntityOfConcern`.

Do not close this row by deleting `live` or replacing it with `current`, `active`, `at issue`, or another status word. Closure is a `KindRestorationCheck`: the modifier is ordinary prose; a state or currentness value under its governing rule; a temporal qualifier of a relation or assertion; a retained claim, use, or relation marker with named admissible use; an `F.19` apparatus removal; or a blocker.

##### E.10:0.2c.26 - `claim`, `evidence`, `witness`, `ground`, `proof`

`Claim` is not a synonym for sentence or prose.
`Evidence` is not a synonym for source, proof, approval, or confidence.

For `claim`, recover:
- claim-bearing episteme;
- claim node, claim content;
- EntityOfConcern or claim referent;
- viewpoint and representation scheme when needed for the claim;
- admissibility target when the claim is used.

For evidence-like words, recover:
- evidence record or evidence-provenance relation;
- witness or source pin;
- grounding relation;
- validation result;
- assurance argument component;
- provenance mark only as provenance, not as evidence by itself.

If evidence is being read as engineering justification, gate passage, deontic permission, work authorization, safety assurance, evidence sufficiency, release authorization, or release confidence, apply the FPF pattern for that stronger claim or use the project-side FPF kind and reference named by value instead of strengthening the evidence word.

##### E.10:0.2c.27 - `authority`, `permission`, `approval`, `commitment`, `obligation`

These are deontic claims or claims carrying an authority-reference relation, not visual or rhetorical properties.

Recover:
- the beneficiary System or reference required by the selected predicate; if source wording says *role*, apply `E.10.ROLE` and cite a local system-role kind and classification or an obtaining `U.SystemRoleAssignment` occurrence only when that permission or authority predicate actually uses it;
- speech act or issuing act;
- commitment record under `A.2.8` for obligation, recommendation-as-duty, or prohibition;
- exact `A.2.8.PER` strong grant, weak non-prohibition/non-violation finding, exercise relation, or permission-conflict finding;
- policy claim and policy/currentness frame;
- authority relation;
- entry predicate or gate record or decision record when that is the actual claim;
- authority-changing decision;
- wording such as `delegated permission`: recover the `A.2.9` granting or delegating speech-act occurrence and, only when the current policy validly institutes one, the resulting `A.2.8.PER GrantedPermissionRelation@Context`. Keep the grantor System, any grantor `U.SystemRoleAssignment` occurrence used by the predicate, the beneficiary System or reference, policy and currentness basis, scope and window, and any separate on-behalf-of or Work relation distinct. The cue mints neither `DelegatedPermissionRelation` nor another generic delegation or authorization kind; if the pattern that defines the permission claim cannot be recovered, block operative use of the wording rather than naming a relation without a governor;
- contestability, revocation, scope, window, and expiry condition.

Labels, badges, signatures, dashboards, certificates, comments, reviewer praise, and generated explanations may cue authority-looking cases.
They do not carry authority unless the authority act, authority record, authority-reference relation, and evidence or provenance relation selected by the direct authority pattern are named.

##### E.10:0.2c.28 - `profile`, `harness`, `catalog`, `registry`, `index`, `map`

These usually point to a review profile, review harness, registry record, catalog publication, navigation index, map, publication form, companion publication, publication-companion relation, or relation between one companion publication and the publication unit or project record it helps readers inspect or use. Choose that kind named by value before writing; do not leave `support record` as the recovered head unless the named FPF pattern really defines that record kind.
Treat one as an FPF pattern body, accepted campaign `DRR`, named current architecture document, or relation to one of them only when the named FPF pattern, accepted `DRR`, or architecture document and the obtaining direct relation with its actual participants are given by value; keep any row, index entry, or map element as its own claim-bearing episteme or C.29 representation.

Split:
- review profile;
- review harness;
- source map;
- navigation index;
- registry record;
- catalog publication;
- benchmark harness;
- entry aid or discoverability aid;
- FPF pattern body.

If the named companion publication, review profile, review harness, registry record, index, or map mainly helps readers find, compare, test, or review something, keep it as a companion, navigation, or testing aid until a named FPF pattern or accepted `DRR` records the recurring action-guidance gain by value.

##### E.10:0.2c.29 - `entry`, `front door`, `corridor`, `route`

These terms often mix navigation, recognition, movement, and authority.

Split:
- entry publication or navigation aid;
- first-use recognition text;
- navigation-bearing publication;
- movement, control, and temporal relation;
- process sequence;
- corridor overview;
- FPF pattern applicable to the problem under repair; if source or local wording merely groups patterns, name the cluster phrase or relation phrase as literal wording and name the patterns involved by value; if an actual relation between patterns is being claimed, name the exact direct relation, its actual pattern participants, and the pattern that defines it.

An entry can make the right pattern easier to find.
It does not prove the pattern is sufficient, complete, or ready for gate use.

##### E.10:0.2c.30 - `same`, `parity`, `identity`, `equivalence`, `mirror`

Similarity is not identity.
Before accepting same, parity, or equivalence wording, name which relation is being claimed:
- mirror file in parity with a governing source;
- same EntityOfConcern;
- same claim content;
- semantic equivalence;
- bridge relation;
- version identity;
- file or carrier equality;
- source-publication identity;
- no-loss transform.

If the relation is about mirror parity, verify against the governing source or state that the check is not performed.
If the relation is semantic, use `A.6.3`, `A.6.4`, `F.9`, or the selected bridge pattern or equivalence pattern rather than relying on matching labels.

##### E.10:0.2c.31 - `file`, `path`, `host`, `packet`, `bundle`, `package`

These are carrier, transport, or package-form words.

Split:
- file or carrier;
- mirror file;
- file carrying FPF pattern text;
- document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use;
- review-facing target packet;
- review packet with its exact question, scope, and source set;
- release package;
- pattern package, pattern family, or pattern group under an accepted decision;
- governing source section.

A packet or bundle can carry a review target by value.
It is not automatically the authority-reference status, the target pattern, the accepted review result, or the FPF `authoritySourceRef` target.

##### E.10:0.2c.32 - `quality`, `characteristic`, `metric`, `indicator`, `score`

Do not let evaluation words float.

Split:
- `U.Characteristic`;
- characteristic space;
- Q-bundle;
- `E.21 PatternQualityQBundle`;
- scale;
- indicator;
- observed value;
- benchmark result;
- review finding;
- decision threshold;
- qualitative judgment with no scale.

`metric` is especially risky because FPF often treats it as imprecise shorthand for scale, value, or indicator machinery.
If the text says a quality improved, name what changed: characteristic, scale, observed value, threshold, decision consequence, or admissible act, work, or claim.
If "quality improved" refers to an FPF pattern version, name whether the change affects an `E.21` coordinate floor or declared coordinate target, status payload, stop condition, bounded non-use, or how `E.21` or another named quality pattern is applied.

##### E.10:0.2c.33 - `slot`, `field`, `row`, `label`, `badge`, `mark`, `cue`

These words are not kinds by themselves.

Split:
- A.6.5 `SlotSpec` inside a current reusable episteme-constitution `RelationSignature`;
- actual participant of an obtaining direct relation;
- A.6.5 `SlotSpec` inside another current reusable `RelationSignature`;
- participant designation inside a current assertion or relation-occurrence-description episteme;
- schema field;
- table row;
- row in a pattern body;
- publication label;
- provenance mark;
- status badge;
- pre-articulation cue;
- displayed cue;
- evidence marker.

A label, badge, mark, or cue may trigger review.
It does not prove currentness, identity, authority, evidence, gate passage, deontic permission, or release authorization unless the source relation and the evidence or provenance relation selected by the relevant pattern are named by value.

#### E.10:0.2d - Current Scan Reading
For conformant text cleanup and source-expression unpacking, high-risk phrases are not automatically wrong. The shared scan is `E.10:0.2`; the rows below are episteme-publication-heavy candidate recovery prompts, not a second registry and not group kinds. Choose the recovered value by sentence function before reuse:
- topic-like or object-like wording: recover the actual `EntityOfConcern` or other governed participant of a claim-bearing episteme, the claim-bearing episteme itself, or a current A.6.5 episteme-constitution declaration and exact `SlotSpec`; otherwise recover the non-claim-bearing project kind;
- publication-unit wording that implies authoring or interpretation work: distinguish selected `U.Episteme`, exact publication occurrence when availability is material, publication form, `PublicationUnit`, file, source note, and review target;
- `content`: usually one of claim graph, text span, publication unit, carrier bytes, or document with named source-basis, evidence-basis, architecture-basis, or review-basis relation or use;
- primary-entity field names: use `publicationUnitPrimaryEntityOfConcern` when a bounded `PublicationUnit` carries or exposes a claim-bearing episteme or episteme-lane `U.View`; otherwise use the non-claim-bearing kind or reference named by value when no claim-bearing episteme participant, A.6.5 declaration, or direct reference use is current;
- `surface`: keep `publication face or publication form` or `interop publication form` only when `publication-face kind` discipline is named by value; otherwise rewrite to generic publication face, declared MVPK face, publication carrier, interop carrier, UI or front-end face, companion publication, source named by value, evidence, assurance, obtaining direct relation and actual participants, C.29 representation and explicit correspondence, or carrier relation;
- `artifact`, `material`, `output`, and `content`: do not let them stay as heads in architecture or pattern prose when they carry ontology or authority;
- `source`, `target`: acceptable only when the actual source-side and target-side participants of the obtaining direct relation are named, or—when reusable declaration is current—the endpoint kinds and exact A.6.5 `SlotSpec` values are named; a schema field, table cell, graph endpoint, or mathematical argument stays a C.29 representation element until explicit correspondence is stated;
- `reader`, `reviewer`: safe only when the word really names a usability reader, review participant, or review process; otherwise name the generic publication face, declared MVPK face, packet, or `PublicationUnit`;
- pre-FPF sign vocabulary: recover FPF episteme kinds, publication kinds, view kinds, carrier kinds, and record kinds before reuse; do not rebuild FPF episteme and publication ontology on a concept-sign-denotation triad;
- generic FPF-side object wording, `locus`, `row`, `host`, or `target`: choose what the sentence actually names: an FPF pattern; pattern section; accepted `DRR`; FPF publication; FPF view; document with a named source-basis, evidence-basis, architecture-basis, or review-basis relation or use; file carrier; review target; record kind and the pattern that defines it; obtaining relation and participants; receiver-needed relation occurrence; claim-bearing episteme; reusable A.6.5 declaration; or C.29 representation with explicit correspondence;
- `supported use`: replace with the `admissibleUse` target named by value and non-admissible stronger or adjacent use, `relationClaimSlice` when a relation claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used;
- `strong`, `stronger`, `weak`, `weaker`: replace with scope, evidence class, threshold, gate or admission threshold, `source-loss mode` under `A.6.3.CSC` when a source-to-rendering loss is being claimed, coarsened rendering, or explicit abstain or reopen condition;
- `authority-bearing FPF pattern or row`: distinguish the FPF pattern or section that supplies the rule, `relationClaimSlice` when a relation claim is being made, `admissibleUse` named by value when a boundary-use claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used;
- `route`, `call`, `invoke`, or procedure-like pattern wording: replace with pattern application or with project-side Work occurrence admitted under `U.Work`, `U.Method`, `C.11` decision value, or `A.6.A` action invitation.

High-risk residue classes:
- restore pre-FPF sign vocabulary to FPF kinds using the exact source or practice boundary and effective scheme that supply the intended meaning;
- unpack FPF-side umbrellas such as generic FPF-side object wording, generic named-target wording, `locus`, `row`, `host`, and `source` by naming what the sentence means: an FPF pattern; pattern section; `DRR`; FPF publication; `U.View`; document with a named source-basis, evidence-basis, architecture-basis, or review-basis relation or use; file carrier; record kind and the pattern that defines it; obtaining relation and participants; receiver-needed relation occurrence; claim-bearing episteme; reusable A.6.5 declaration; C.29 representation with explicit correspondence; or another file-carrier phrase;
- unpack project-side umbrellas such as `input`, `raw material`, `source data`, `source material`, `artifact`, `output`, `result`, `outcome`, `deliverable`, `handoff`, `screen`, `dashboard`, `credential`, `badge`, and `explanation` by naming the entity and relation they hide: a publication or carrier use; a project-side FPF kind and reference named by value; a direct relation claim with its participants or an `A.6.1` operation-application binding; a local `A.15.PROD` or `A.6.RCD` claim; an `A.10` evidence relation; measurement-result episteme; evaluation or diagnostic finding; `C.11` `ChoiceResult` or decision record; gate, assurance, status, action invitation, work plan, dated Work, Method, or MethodDescription as defined by the relevant pattern; or an `A.6.P.WMR` non-assertability result independently reasoned as `factually unsupported`, `missing-information`, or `missing-governor`. Only `missing-governor` also names the affected receiving use and future subject pattern or relation declaration. Do not leave a generic work-result or result-measurement record as the recovered value;
- make admissibility phrases such as `supported use`, stronger or adjacent use not carried by the pattern of concern, insufficient evidence relation, and similar formulas name the `admissibleUse` target named by value and non-admissible stronger or adjacent use, `relationClaimSlice` when a relation claim is being made, and `projectSideFPFRef` when a project-side FPF kind and reference named by value is being used;
- check pattern-control metaphors such as `route`, `call`, `invoke`, `exit`, `path`, `branch`, `chooser`, and `workflow` for declarative pattern application versus real movement, control, and temporal claims.

#### E.10:0.2e - Trigger Concordance And Closure Mechanism

`E.10` is applied to a bounded FPF-facing text object, not only to one remembered example sentence. Before claiming `E.10` closure over an accepted `DRR`, FPF pattern, extracted pattern host, monolith section, review-facing packet, or FPF-facing guidance, complete trigger concordance when a high-pressure trigger is FPF-governed across the bounded object.

Do not build a heavy concordance for every ordinary word. Trigger concordance applies when one trigger word or trigger-headed phrase:

- appears in a selected name, durable reusable name, heading, table column, schema field, coordinate name, status value, or selected reusable authoring vocabulary;
- recurs across the problem frame, decision, selected names, validation, and handoff-like action claims or conformance subjects often enough to carry the local architecture;
- acts as a replacement head for another broad head;
- appears in a returned finding or accepted basis as a term whose meaning is carried into FPF wording;
- or remains the only word that lets the sentence appear precise.

The mechanism is:

1. Inventory the trigger spans inside the bounded object, with exact locations or grouped locations and count. Mark structural role: ordinary prose, selected name, heading, table column, field, example, quote-only wording, source-only wording, relation phrase, publication phrase, or source-use phrase.
2. Group occurrences by local interpretation, not by trigger word alone: ordinary no FPF-governed use, local lexical repair, relation-like use, episteme use, publication use, source-use, durable naming need, quote-only or source-only wording, false positive, or blocker.
3. For each local interpretation, choose and complete the repair consequence. Local repair may close under `E.10`. For relation-like wording, use `A.6.P` or its retained specialization; use `A.6.RCD` only for the exact residual claim whose participants are known and which no current direct relation closes. For episteme, publication, or source-use wording, use `C.2.P`. For durable reusable naming, use `F.18` after recovering the kind and use. Quote-only or source-only wording needs a non-use disposition. Classification labels are not closure endpoints.
4. Rewrite the bounded object, or leave a blocker. A note saying `apply A.6.P when triggered`, `apply C.2.P when triggered`, `apply the pattern that defines or constrains the recovered claim`, `subject to F.18 later`, `classified under A.6.P`, `classified under C.2.P`, or `boundaries are stated nearby` is not closure unless the recovered result is already present in the final wording or the still-triggered repair is explicitly blocking. Every FPF-governed trigger has a non-empty `Final wording or blocker` cell.
5. Reread saturation. If one trigger word still carries several different local interpretations after repair, or dominates the selected names of the bounded object, the text has likely preserved an umbrella rather than repaired it. Split the local interpretations into names or concrete pattern applications named by value before accepting the wording.

Use this compact closure table when the governing review selects trigger concordance:

| Trigger span or name | Locations and count with structural role | selected interpretation | Recovery needed | Final wording or blocker | Closure disposition |
| --- | --- | --- | --- | --- | --- |
|  |  | ordinary no FPF-governed use; local repair; relation-like use; episteme, publication, or source-use; durable naming; quote-only; false positive; blocker | `E.10`, `A.6.P`, `C.2.P`, `F.18`, or not triggered |  | closed locally; recovered and integrated; quote-only; not triggered by value; still blocking |

Allowed closure dispositions are only:

- ordinary wording with no FPF-governed use accepted;
- local lexical repair closed under `E.10`;
- `A.6.P` recovery completed and integrated into the text;
- `C.2.P` recovery completed and integrated into the text;
- `F.18` naming decision completed after kind and use recovery and integrated into the text;
- quote-only, source-only, or non-use disposition stated by value;
- false positive stated by value;
- still blocking.

Do not close trigger concordance with a summary statement that `E.10 was applied`, with a citation to `A.6.P` or `C.2.P` alone, with a correct classification but no repaired claim or result, with a later-work promise, or with a table that covers only representative examples while the remaining FPF-governed occurrences keep the same unresolved head.

#### E.10:0.3 - Recovery and disposition table

`E.10` gives only a small local recovery and disposition form. It does not unpack relation-like or episteme-publication-heavy source meaning by itself.

| `E.10` result | Recovery product | Disposition |
| --- | --- | --- |
| local wording accepted | Ordinary wording with no FPF-governed use. | Leave as ordinary prose. |
| local wording rewrite | Repaired phrase that names the local kind named by value, register, ordinary sense, or admissible lighter wording. | Accept locally after the replacement-candidate anti-umbrella rule. |
| relational precision restoration triggered | Trigger span plus a relation-like use whose direct predicate or actual participant remains unclear: endpoint, qualifier, slot, scope, time, viewpoint, basedness, service, bridge wording, whole-part, mapping, comparison, or dependency. A `support` phrase enters this row only when `E.10:0.2` has identified a direct subject relation or common alternative but the reader still cannot name its direct predicate or an actual participant. | Apply `A.6.P` or the specialization for that relation to recover the missing predicate or participant. Once both are clear, apply `A.6.RCD` only if no current pattern defines or constrains that predicate. A common lexical alternative that is already clear goes straight to its subject pattern and is not chosen again in `A.6.P`; if the trigger is a false positive, say why. |
| epistemic precision restoration triggered | Trigger span plus the episteme, publication, source-use relation, or source-expression relation under repair. | Apply `C.2.P` before accepting current FPF wording; if the trigger is a false positive, state that reason by value. |
| combined precision restoration triggered | Trigger span plus both relation-like wording and episteme, publication, or source-use wording. | Apply `C.2.P` for the source-currentness relation and claim-bearing episteme or publication relation set; apply `A.6.P` for the relation-bearing slice. |

#### E.10:0.4 - Closure rules

| Closure question | Conforming answer |
| --- | --- |
| Can `E.10` alone close the case? | Yes only for `not-triggered`, false-positive by value, ordinary wording with no FPF-governed use, and local lexical-repair outcomes whose replacement candidate has also passed `E.10`. |
| What counts as `closed by value`? | The final wording or disposition names the concrete result: recovered kind; obtaining relation and participants; receiver-needed occurrence; current A.6.5 declaration; claim-bearing episteme and any participant designations; C.29 representation and correspondence; admissible use and the stronger or adjacent use it does not carry; source-use disposition; publication construction; durable naming decision; or false-positive reason. The reader can recover what the trigger meant without chat memory or a future pass. |
| What counts as `A.6.P` or `C.2.P` application? | A pattern citation is not the result. The result is the completed recovery: selected relation interpretation; obtaining relation and participants or reason-specific blocker; receiver-needed occurrence; current declaration, assertion episteme, participant designation, publication construction, or C.29 representation and correspondence; endpoint, qualifier, scope, admissible-use, source-use, project-side reference, false-positive, quote-only, or non-use result; or a named blocker integrated into the text or closure account. |
| Can `E.10` close relation-like wording by itself? | Not while the direct predicate or a participant remains unclear. For `support`, `E.10:0.2` first separates ordinary or quoted non-use, a recognizable direct relation, and common lexical alternatives. Ordinary non-use can stop here. A clear direct relation uses the pattern that defines it; a clear common alternative uses the pattern named in `E.10:0.2`. Apply `A.6.P` only to recover an unclear predicate or participant, and apply `A.6.RCD` only after both are clear and no current pattern defines or constrains that predicate. Do not choose a common alternative again in `A.6.P`. |
| Can `E.10` close episteme-publication or source-use wording by itself? | No. If the problem under repair is source wording, episteme, publication, view, face, carrier, publication unit, EntityOfConcern, grounding, FPF transfer, project-side claim, admissible-use claim, or pattern-application wording, the conforming text applies `C.2.P` or states the false-positive reason by value. |
| Can a replacement term close the case because it sounds more precise? | No. A repair is not conforming merely because the original overloaded word was replaced. The replacement candidate passes the same trigger scan and anti-umbrella test. |
| Can a trigger-headed selected name close with `F.18 later`? | No, not when the name is already selected by an accepted `DRR`, table heading, schema field, coordinate, pattern authoring draft, or selected reusable authoring vocabulary. Complete `F.18` now after kind and use recovery, replace the head with wording named by value, or leave the naming issue blocking by value. |
| Can a correct classification close the case without changing the text? | No. Correct classification only starts the consequence. For an FPF-governed trigger, closure means changed final wording, a concrete result from the selected pattern recorded by value, or an explicit blocker. |
| Can a high-frequency trigger close through representative examples? | No. When the governing review selects trigger concordance, representative examples may guide grouping, but the closure account covers all FPF-governed occurrences or exact grouped locations and counts and states what remains ordinary, repaired, quote-only, rejected, or blocking. |
| Where do trigger words and examples belong? | In this shared `E.10` scan architecture or in a named local application profile tied to a primary `EntityOfConcern`, an obtaining relation and its participants, a reusable A.6.5 declaration, a claim-bearing episteme and any participant designations, or a C.29 representation and explicit correspondence. Do not copy growing word lists into `F.18`, `A.6.P`, `C.2.P`, `E.19`, or local checklists. |

### E.10:1 - Problem frame
**Current name set.** `E.10` is the current FPF pattern. `E.10:0.2` is the shared wording-use trigger scan. The `LEX-BUNDLE` and `ULR` sections below are subordinate material for selected lexical, register, naming, morphology, and local rewrite problems. They are not a second ontology, wording-recognition table, or pattern head, and do not replace `E.10.ARCH`, a selected precision-restoration pattern, the concrete pattern for the recovered claim, or `F.18`. When subordinate material conflicts with `E.10:0.2`, `E.10.ARCH`, `A.3.4.P`, `A.6.F`, `C.2.P`, `E.24.*`, `F.18`, or another named pattern, the current applicability table and the pattern that defines the claim control the repair.

**Intent.** Provide one **normative** trigger-and-repair rule set that makes FPF language **unambiguous, composable across sources and uses, and teachable** by design. Authors, reviewers, and tooling use the subordinate material only for the selected wording problem after `E.10:0.2` has chosen the closure disposition:

* **Vertical stratification** (Kernel ↔ Extension patterns ↔ Local use ↔ Instance);
* **Twin registers** (Tech and Plain) with safe synonyms;
* **Naming morphology** (allowed suffixes and style) for the kernel’s core objects;
* **Minimal Generality** tests (names are neither parochial nor vacuous);
* **Ontology recovery rows** for overloaded words (e.g., *process*, *function*, *service*);
* **Conformance checks** and minimal examples.

**Scope.** Applies to:
(a) **Core** (Parts A–G), (b) **Extension pattern specifications** (CAL, LOG, and CHR), (c) **local source or practice glossaries** that claim FPF conformity, and (d) **diagrams and prose** in normative text. It **does not** constrain Tooling or Pedagogy wording other than where they quote Core semantics.

### E.10:2 - Problem

1. **Polysemy drift.** *Process, function, service, agent, activity* slide between structure, recipe, execution, and promise.
2. **Cross-local collision.** A label such as *Owner* is assumed to have one global meaning even though distinct sources, practices, or schemes use it differently.
3. **Name-bloat and parochialism tension.** Either hyper-specific domain names leak into core kinds, or vague umbrella names obscure invariants.
4. **EntityOfConcern and Description-episteme boundary and specification-use collapse.** Authors mix **EntityOfConcern** (the thing under concern), **Description episteme** (how we describe it), and **specification use** (testable criteria, formality, acceptance, and harness-gated use of a Description episteme).
5. **Register soup.** Tech terms bleed into Plain pedagogy and vice‑versa, inviting category errors.

### E.10:3 - Forces

| Force                          | Tension to resolve                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------ |
| **Universality and local fit** | Kernel stays universal while exact sources, practices, schemes, and uses retain their needed local distinctions. |
| **Brevity and clarity**        | Short names help, but only if morphology signals the right governed kind.                 |
| **Stability and evolution**    | Names should survive refactors while accommodating new roles and kinds without explosion. |
| **Pedagogy and precision**     | Plain words aid learners; Tech labels anchor formal checks.                                |

### E.10:4 - Solution - trigger scan, ontology recovery, and retained register

**LEX-BUNDLE** and **ULR (Unified Lexical Rules)** name subordinate register, naming, morphology, and local rewrite checks inside the current `E.10` pattern. They do not name a second pattern, a second ontology, or a second audit. Use this material only after the `E.10:0.2` scan has selected a lexical, register, morphology, or naming problem that actually needs those details.

1. **Vertical Stratification** (E.10 -> four strata);
2. **Twin‑Register Discipline** (Tech and Plain pairs);
3. **Minimal Generality (MG)** principle + tests;
4. **Morphology and Style** (suffixes, casing, reserved prefixes);
5. **Canonical Rewrites** for overloaded words (L‑rules);
6. **Conformance Checklist (CC‑LEX)** and **Regression Stubs (RSCR‑LEX)**.

The retained clauses below apply only within that selected problem and only when they agree with the current applicability table and the pattern that defines or constrains the recovered claim.

### E.10:5 - Vertical Stratification (four strata; no cross-bleed)

> **Rule V‑0 (Strata).** Every lexical item in a conformant text belongs to exactly one **stratum**:

1. **Kernel** — admitted `U.*` names, core relation kinds, and invariants (for example `U.Holon`, `U.SystemRoleAssignment`, `U.Method`, `U.Work`, and `U.PromiseContent`).
2. **Extension patterns** — CAL, LOG, and CHR exports (e.g., **Sys‑CAL**, **KD‑CAL**, **Agency‑CHR**) that **extend** but do not override Kernel.
3. **Local use** — the exact source or practice boundary, effective scheme, local meaning statements, aliases, local kind distinctions and classification rules that the use actually needs; cite an F.9 Bridge only when an exact relation between distinct local senses obtains.
4. **Instance** — concrete identifiers for admitted holder Systems, exact `U.SystemRoleAssignment` occurrences, Work occurrences, and carriers.

**V‑1 (Unidirectional meaning).** Meaning is constrained from Kernel to extension patterns to local use to Instance. A local source, practice, or scheme may add a narrower designation or distinction, but it does not silently redefine a higher stratum's term; any actual relation between distinct local senses is stated separately.

**V‑2 (Strata and authoring stances).** The four lexical strata above constrain **tokens**. They are independent of a claim-bearing unit's **stance** (its `CtxState` pins such as `DesignRunTag`, `ReferencePlane`, and `Locus`). Strata answer “what words mean here”; stance answers “where this claim is situated” and which evidence-lane expectations apply.

**V-3 (Citation style).** When a local Tech designation changes interpretation or action, its first use names the source or practice provenance and effective scheme needed to read that use—for example, `ReviewerSystemRole` under the JournalReview-2026 definition. Reuse under another local meaning first compares the exact governed values; use F.9 only if a direct Bridge between distinct exact cells actually obtains. A suffix may serve as a locator, but it establishes neither kind identity, admission, nor assignment.

**V-4 (Firewall).** Tooling and Pedagogy idioms remain outside Kernel prose (DevOps Lexical Firewall). CI/CD jargon, file formats, and API names are not admitted in Core definitions. Pedagogy may use them only as Plain-register examples with Tech anchors present.

### E.10:6 - Ontology Guards

#### E.10:6.1 - Tech register ontology guards

> **Purpose.** This section stabilises the Tech register of the kernel lexicon by enforcing head-anchored naming, explicit kind naming, EntityOfConcern and Description-episteme boundaries, specification-use morphology, guarded use of bare *role*, exact `SystemRole` compounds, and subject-specific recovery of Domain wording. It aligns with **E.10.D1**, **F.4 SystemRoleKindDescription**, **A.2.5 SystemRoleAssignmentStateRelation**, **A.2.7 SystemRoleKindRelationStructure**, **F.11 Method Quartet Harmonisation**, and **F.17 UTS**. **Scope:** Guidance is register-agnostic and applies across the FPF; illustrative examples pass Minimal Generality and Domain Anchoring (MG-DA) and the other rules of E.10.
>
**Onto1 — Head‑anchoring**  *(use Kernel heads + pass LEX.TokenClass, EntityOfConcern and Description-episteme boundary, and specification-use gates)*
* **Rule:** The **head noun of a term explicitly signals the kind** (`System`, `Holon`, `Work`, `Episteme`, `Tradition`, `Lineage`, `Characteristic`, `Method`, `Profile`, `Description`, `Spec`, `TransformationFlowStructure`, `Card`, `Pack`, `Dashboard`, …). `SystemRole` is allowed only as the common compound inside one concrete local system-role-kind designation such as `ReviewerSystemRole`; bare *role* remains a recovery trigger rather than a kind head.
* **Figurative heads** with obvious overload (“Tradition”, “family”, “process”, “function”) are not admitted in the kernel. Plain twins are admitted only with a one-to-one Tech mapping and declared **`LEX.TokenClass`** for the Tech token. They appear in the Plain register as one-to-one mappings to a Tech token, not in the Tech register. Plain language minimizes lexical error from overloaded terms through plain-twin lexical guards.
  * **Do:** `IncidentDashboard`, `MethodSpec`, `TraditionProfile`, `TransformationFlowStructureDescription`.
  * **Don’t:** `IncidentBoard`, `TDD Tradition`, `Production Process` (kernel), `Service Function` (kernel).

 **Onto2 — EntityOfConcern and Description-episteme boundary and specification-use morphology**  *(ref. E.10.D2)*
* **Rule:** A term for the EntityOfConcern uses the bare head for the FPF kind under concern: `Method`, `Tradition`, `Characteristic`. A **Description episteme** appends **`…Description`** only under the membership rule of the pattern defining that episteme kind. In particular, a claim-bearing episteme is `U.MethodDescription` only when its exact EntityOfConcern is one admitted `U.Method` and it makes at least one substantive claim about that method as a way of doing. `Algorithm`, code, pseudo-code, recipe, procedure, diagram, or other expression form first remains source wording, a C.29 representation, or a publication expression; none establishes that membership. A qualifying Description episteme appends **`...Spec`** only after a named specification-use gate grants that use. Thus `MethodSpec` is available only when the same episteme passes both A.3.2 membership and the E.10.D2 specification-use gate; formal language, pseudo-code, or bundled tests alone settle neither condition.
* **Formal-description guard:** A formal mathematical or physical theorem, including a formal postulate theorem in physics, remains a Description episteme until a bounded use assigns specification use. Its formal language belongs to formality and publication-expression discipline; it becomes a specification only under acceptance criteria, harness checks, normative invariants, measurable anchors, verification use, or another specification-granting condition named by value.
* **Extension:** Apply the same morphology to non-method EntitiesOfConcern where appropriate: `TransformationFlowStructureDescription`, `TransformationFlowStructureSpec`, `SystemDescription`, and `SystemSpec`.
* **Do:** `SamplingMethod` - `SamplingMethodDescription` - `SamplingMethodSpec`.
* **Don’t:** `SamplingAlgorithm` (when it is just prose), `SamplingProcessSpec` (head not signalling kind).
**Onto3 — System-role kinds, assignments, and carrier-relation separation** *(ref. E.10.ROLE, A.2, A.2.1, F.4, F.5, C.2.1, C.2.P, E.17, E.24.PUB, A.10, and C.35)*
* **Positive distinction:** A system role is an exact local kind for entities already admitted under A.1 as `U.System`. C.3 recovers it through the candidate domain, operative work-facing membership condition, intended member/non-member boundary, and continuity rule. A practice or source reference locates the definition or signals a comparison; it does not identify the kind. Its Tech designation ends in `...SystemRole`, for example `ReviewerSystemRole`. The name creates no admission, assignment, agency, capability, or Work.
* **Assignment rule:** A system-role assignment is an obtaining occurrence of one directly declared species under `U.SystemRoleAssignment`. The species declaration defines `HolderSystemSlot`, the exact local system-role-kind domain of `AssignedSystemRoleKindSlot`, any other participant meanings, its predicate, applicability, and occurrence-identity rule. The occurrence supplies the actual holder System, assigned-kind value, any other participant values, and extent. A source, interpretation, taxonomy, scheme, description, or display is not automatically an assignment participant; name it separately only when the assignment claim actually depends on it.
* **Readable example:** `Under the JournalReview practice, TeamAlpha is classified under ReviewerSystemRole because it can supply the substantive review judgment required by that practice.` Add `ReviewAssignment-42` only when the assignment itself matters and both its directly declared species and obtaining occurrence are recoverable. If performed Work is current, point to its complete A.15.1 occurrence basis and F.6 attribution basis. A short sentence may omit only an assignment identifier unused by the receiving claim; it does not omit a performer, Method, time, containing System, assignment occurrence, or F.6 attribution from the recoverable basis.
* **Carrier rule:** **Carrier** is not a free holon or system kind. Recover the direct carrier relation: use `U.PresentationCarrier` only under E.17 and E.24.PUB publication and presentation discipline. If a reusable carrier-relation declaration is separately current, `PresentationCarrierSlot` remains the declaration-local `SlotKind` of one A.6.5 `SlotSpec` and is not the carrier or relation. Other exits are a file, transport, rendering, front-end, or access-carrier relation under E.17; evidence or source-currentness carriage under A.10 or G.11; generated or produced carriage under C.35; or a named episteme-symbol carrier relation independent of any system-role assignment.
* **Source-word rule:** Job titles such as *reviewer*, *owner*, and *lead* remain Plain or quoted wording until the current claim is recovered. Use `E.10.ROLE` for an ambiguous claim-bearing *role*. Use `...SystemRole` only for an exact local system-role kind, and preserve *owner* when an actual architectural, organizational, policy, source, or responsibility ownership relation is what the sentence states.
* **Do:** `ReviewerSystemRole`; `ReviewAssignment-42 : U.SystemRoleAssignment`; `LeanTraditionCarrier` only when its direct episteme-symbol carrier relation is declared.
* **Don’t:** `Reviewer` as a U-kind, `ReviewerCarrier` for an assigned system, an unqualified `...Role` Tech head, or `Carrier` as an unstated system kind.
**Onto4 — Recover what *domain* means in this use**  *(ref. E.10.D1 and F.17)*
* **Rule:** The word *domain* does not create a kernel kind, catalogue mark, family, bundle, or inheritance relation by spelling. Recover what *domain* names in the current claim—for example, a DPF subject, discipline, source-defined field, model domain, market, physical region, or policy extent—or keep it as ordinary prose when it carries no FPF-governed use.
* **Local-meaning rule.** When a durable domain expression carries source-local meaning, identify its exact source edition, effective `ReferenceScheme`, local expression, local-sense claim, and any obtaining basis relation. Create an F.17 `SchemeSenseCell` only when a named receiver needs a stable address. Use F.9 only for an independently obtaining Bridge between distinct exact cells; state any proposed use separately.
* **Discipline boundary.** Use `U.Discipline` only when the claim satisfies the pattern that defines that kind. A domain label, shared vocabulary, or UTS row does not establish discipline identity.
* **DPF boundary.** A DPF states its domain subject, intended audience and use, source basis, scope, and qualification window under `E.4.DPF`; it need not invent `DomainFamily`, `DomainBundle`, or a list of Context identifiers.
* **Do:** “The Clinical Safety DPF addresses adverse-event analysis and device-labelling decisions for the stated audience and scope.”
* **Don’t:** infer `ClinicalSafetyDomain`, `DomainFamily`, or `DomainBundle` as a kind from that wording.

**Onto5 — Always state what the term names**
* **Rule.** The definition or first line of a gloss states the FPF kind or object named by the term—for example, a `U.Holon`, `U.System`, `U.Episteme`, `Tradition`, `Lineage`, `Profile`, exact local system-role kind, `U.Work` as the admitted kind or a Work occurrence admitted under it, `Characteristic`, or direct carrier relation.
* **Do:** “**Kind named:** `ReviewerSystemRole` — the exact local kind whose admitted-system candidates satisfy the current substantive-review condition. Its member/non-member boundary and continuity rule are recoverable under C.3; the named review practice locates that definition. A concrete assignment names its directly declared species and one separately obtaining occurrence under `U.SystemRoleAssignment`.”
* **Don’t:** “Reviewer — a person who …” (blurs the kind named).

**Onto6 — Bans and ontology recovery hints**  *(mirror E.10 § 9 L-rules; do not duplicate tables; not a substitution table)*
* `process`, `procedure`, `workflow`, `function`, or `activity` -> first recover the wording family: change-situation wording applies `A.3.4.P`; function-like wording applies `A.6.F`. Possible recovered values include `U.Method`, `U.MethodDescription`, `U.WorkPlan`, one dated Work occurrence admitted under `U.Work`, a separate episteme about it, `U.Transformation`, and `TransformationFlowStructure`. Choose among them only after naming the object, any obtaining method-side or other relation and its participants, the relevant declaration or representation use, or the claim kind and the pattern that defines it.
* `Tradition` → **`Tradition`** (Tech); leave “Tradition” only as a Plain twin with an adjacent Tech label.
* `domain` -> apply Onto4: name the actual domain subject, source or practice boundary, effective scheme, discipline claim, DPF scope, or ordinary use that matters here. Do not infer `DomainFamily`, `DomainBundle`, `ContextId`, or a UTS row from the word.
* `…CarrierRole` used for an assigned System -> start with `E.10.ROLE`; recover the holder System, local `...SystemRole` kind, A.2.1 assignment occurrence, and its declared species only when the passage asserts those facts. Recover carrier, source relation or source-local meaning, interpretation, publication, evidence-use, and Work claims through their own relations.
* ambiguous *owner* wording -> recover the precise relation or other claim being made—for example, an architectural, organizational, policy, source-maintenance, responsibility, authority, commitment, or work-facing claim. Keep *owner* when that precise ownership relation is current; use a `...SystemRole` designation only when the recovered object is an exact local system-role kind.
* job titles (`owner`, `lead`, `champion`) in the Kernel -> keep them in Plain or quoted wording until the claim is recovered; use exact `...SystemRole` designations only for admitted local system-role kinds.
* **Do:** `ReturnsTransformationFlowStructureDescription`, `Tradition: Test-Driven`; `LedgerTeam is classified under LedgerCustodianSystemRole`, with any exact assignment, responsibility, authority, source-maintenance, or interpretation relation stated separately when current.
* **Don’t:** `Returns Process`, `TDD Tradition` (kernel), `Ledger Owner` (underspecified).

**Worked mini-examples across arenas.** These names illustrate morphology only. Every `...MethodDescription` presupposes one claim-bearing episteme whose exact EntityOfConcern is one independently admitted `U.Method` and whose claims pass A.3.2; every `...Spec` also presupposes its subject-specific specification-use gate. The label establishes neither condition.

The Onto3 block above is the one bounded distinction and assignment example. The twelve rows below are morphology cues, not classification or assignment assertions. Read each candidate System label and candidate local system-role-kind label separately. Before asserting classification, pass C.3 and A.2; before saying an assignment obtains, admit the holder System and establish both the A.2.1 occurrence and its declared species. A schedule, place, office, desk, title, source or practice cue, taxonomy, scheme, or interpretation episteme supplies none of those facts by wording.

| Arena | Morphology examples | Candidate system label | Candidate local system-role kind | Separate source cue or ambiguity | Avoid |
| --- | --- | --- | --- | --- | --- |
| Software engineering | `BuildTransformationFlowStructureDescription`, `CIHarnessSpec` | `RepoTeam` | `MaintainerSystemRole` | `RepoX` is a repository or source cue; name the exact maintenance practice or source edition only when it changes the claim | `Build Process`, `Repo Owner` |
| Applied research and experimentation | `SamplingMethodSpec`, `CalibrationLineageCarrier` | `ReviewPanel` | `ReviewerSystemRole` | `GrantCallY` is a source cue; name its edition and review practice when they matter | `Sampling Algorithm` (if prose), `Lab Owner` |
| Production and service management | `ShiftWork`, `SafetyOfficerSystemRole` | `TeamAlpha` | `SafetyOfficerSystemRole` | name the exact plant-operations practice, source, or working situation if it changes the claim | `Safety Officer` as a U-kind, `SafetyDomain Governance` |
| Operations research and optimisation | `RoutingMethodDescription`, `CostCharacteristic` | `AnalysisGroup` | `ModelStewardSystemRole` | `ORProgram` is a source or practice cue; recover the exact use that changes the claim | `Routing Function`, `Model Owner` |
| Healthcare and clinical ops | `CarePathwayTransformationFlowStructureDescription`, `MedicationAdministrationWork` | `DrK` | `AttendingPhysicianSystemRole` | name the exact ward practice, source, or clinical situation if it changes the claim | `Care Process`, `Ward Owner` |
| Finance and accounting | `ReconciliationMethodSpec`, `JournalPostingWork` | `TreasuryTeam` | `TreasuryStewardSystemRole` | name the exact book, source edition, or treasury practice if it changes the claim | `Reconciliation Process`, `Account Owner` (underspecified) |
| Legal and compliance | `RetentionPolicySpec`, `InvestigationWork` | `PrivacyOffice` | `DataProtectionOfficerSystemRole` | name the exact policy source, organization practice, scope, and edition when they matter | `Compliance Function`, `Data Owner` (underspecified) |
| Cloud and IT operations | `IncidentTransformationFlowStructureDescription`, `RunbookMethodSpec` | `OnCallEngineerTeamSystem` | `OnCallEngineerSystemRole` | `OnCallRotation` is schedule or roster wording under L-SCHED, not a holder; name the exact service source, operating practice, or situation if it matters | `Incident Process`, `Service Owner` (underspecified) |
| Logistics and supply chain | `PickingWork`, `RoutingMethodSpec` | `DispatchTeamSystem` | `DispatcherSystemRole` | `DispatchDesk` is an ambiguous desk label, not a holder; name the exact hub practice or scope if it matters | `Picking Process`, `Fleet Owner` |
| Construction and civil engineering | `PermitAcquisitionTransformationFlowStructureDescription`, `InspectionMethodSpec` | `SiteInspectionTeamSystem` | `SiteStewardSystemRole` | `SiteOffice` is an ambiguous place or office label, not a holder; name the exact project lot or site practice if it matters | `Inspection Process`, `Site Owner` |
| Emergency response | `TriageMethodDescription`, `EvacuationTransformationFlowStructureDescription` | `ResponderSystem-17` | `IncidentCommanderSystemRole` | `IncidentLead` is title-like role wording, not a holder; name the exact incident situation or response practice if it matters | `Triage Function`, `Incident Owner` |
| Agriculture | `IrrigationTransformationFlowStructureDescription`, `SoilSamplingMethodSpec` | `FieldTeam` | `FieldStewardSystemRole` | name the exact plot, source, or field practice if it changes the claim | `Irrigation Process`, `Field Owner` |

**Checklist before minting a KernelToken**
* Head noun signals kind (Onto1).
* EntityOfConcern and Description-episteme boundary and specification-use morphology correct (Onto2).
* If system-role-related or carrier-related: local system-role kind, direct assignment species, and carrier relation remain separate; holder-system admission is explicit and the direct carrier-relation pattern is named (Onto3).
* Any action-changing Domain wording recovers its subject, use, and applicable pattern; a durable local expression uses F.17 only when its source-local meaning or public term row is current (Onto4, Onto6).
* Object‑of‑talk declared (Onto5).
* SCR-LEX rewrites checked for current system-role-kind, direct assignment-species, and carrier-relation separation (Onto6).
> **Note on registers.** Keep figurative or business-casual terms in the **Plain** register only, with strict **twin-label** links to the Tech token under current `E.10`. In the **Tech** register, speak in KL-CAL: **episteme-about-epistemes** (Tradition, Lineage, Profile), not in catalogue-admin idioms.

* **Onto‑Deon — Deontic lexicon guard (Core register)**
**Rule.** In the Conceptual Core, avoid using **“Standard”** as the head noun of an EntityOfConcern name unless the object is an explicit **deontic speech-act** under the **Gov** lens (cf. E.3).

For interface and boundary invariants concerning things such as holons, interfaces, and ports, name the exact invariant, compatibility condition, compliance profile, acceptance specification, or interoperability profile by value—for example `InterfaceCompatibilityCondition`, `ComplianceProfile`, `AcceptanceSpec`, or `InteropProfile`. State any promise or commitment separately; naming does not make it a property of the thing.

Use the word **standard** for a publication of a Description episteme, possibly admitted for specification use, that is *intended to be complied with* and has explicit compliance checks.

If an EntityOfConcern-side item is currently named `… Standard`, rename it to a proper EntityOfConcern-side name, and (optionally) add a separate publication of the relevant Description episteme under the needed compliance or specification use that contains the standard text and the intended compliance checks.
 **Rewrite hints (Tech → Tech).**
 `publication Standard` → `publication standard`;
 `frame Standard` → `frame standard`;
 `measurement Standard` → `measurement standard`;
 `Method Interface Standard (MIC)` → `Method Interface Standard (MIS)`;
 `Boundary-Inheritance Standard (BIC)` → `Boundary-Inheritance Standard (BIS)`.
 **Rationale.** Keeps Core prose centred on EntitiesOfConcern and their boundary invariants; reserves deontic obligations for governance contexts and **U.PromiseContent**‑like promises. Do **not** misuse “plane”: deontic speech‑acts are analysed via the **Gov** lens, while **ReferencePlane** remains `{world | concept | episteme}`.

#### E.10:6.2 - Twin‑Register Discipline (Tech and Plain)

**Plain twin (LEX).** A registry entry pairing the **authoritative Tech designation** with a **display-only Plain designation** for one named value under one stated local meaning and effective `ReferenceScheme`: an admitted durable U-kind, C.3 `U.Kind`, Concept-Set row, imported signature symbol, or another value whose kind and definition are already known. The LEX registry checks the pairing under **PTG (Plain Twin Governance)** and identifies it by `Twin-Map ID (LEX)`. Create an F.17 `SchemeSenseCell` only when stable reuse or another named receiver needs an exact address. *“Plain twin” ≠ the **Plain register** (the register is where twins may be used; the twin is the 1:1 mapping).*
**Convention.** In this spec, **Plain** (capitalized) names the register; **plain twin** (lowercase) names the 1:1 mapping entry.

> **Rule R-0 (Registers).** Every Kernel and extension-pattern concept has a **Tech designation** used in testable semantic clauses and may have one **Plain designation** for a stated didactic use. The Plain designation is admitted only when it names the same value under the stated local meaning and effective scheme; it does not create another value, cell, kind, or relation.

##### E.10:6.2.1 - Allowed pairs (normative table; examples)

| **Tech (authoritative)** | **Plain (didactic)**                        | **Notes and guards**                                                                           |
| ------------------------ | ------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `U.System`               | system, machine, team                        | Bare “service” is **never** a safe Plain twin for `U.System`. Apply L-SERV only when a relied-on use hides the concrete subject or next route, then use `A.6.P:4.11a`; quoted, historical, illustrative, and harmless ordinary wording stays outside. Avoid “service-instance”; after recovery use “system instance”, “service access point”, “service offering”, or another head phrase supplied by the pattern for the recovered claim. |
| `U.Episteme`             | body of knowledge, document, dataset, model | The pair preserves the **Carrier and Content** distinction (A.7).                                              |
| `U.Method`               | how‑to, procedure (abstract)                | Do **not** call this “process” (L‑PROC).                                                     |
| `U.MethodDescription`    | account of how one identified method is done | `recipe`, `SOP`, `playbook`, `code`, and `spec-text` are recognition cues, not automatic twins. Use this pair only after the claim-bearing episteme has one admitted `U.Method` as its exact EntityOfConcern and passes A.3.2's substantive-description threshold; call out **Spec** separately only after the E.10.D2 gate. |
| `U.Work`                 | work (work kind)                           | This plain twin names the admitted kind only. A run, execution, activity, job, or case can name one Work individual only after A.15.1 grounds that occurrence; show an explicit occurrence name and the head **work occurrence** rather than reusing the kind twin. |
| one exact local `...SystemRole` kind | reviewer (system role), maintainer (system role) | Local kind for entities independently admitted as `U.System`. On first use, say which systems can count, what work-facing condition separates members from relevant non-members, and what changes preserve that distinction. A practice or source reference may help readers find or compare the definition; it does not identify the kind. The Plain wording creates no system admission or assignment. |
| `U.PromiseContent`              | promise, offering, service offering         | Never equate to provider system or API (L‑SERV).                                             |
| `U.Capability` | ability, capacity (within bounds) | Separate from a system-role kind, system-role assignment, Method, and Work; carries its own envelope and measures. |
| `U.Dynamics`             | law of change, model of evolution           | Not a capability or a method.                                                                |

**R‑1 (Plain first-use).** At first use in a section, show the **Tech label** and, optionally, the Plain twin only after membership is known: *"...one `U.Method` (the **how-to**); and, when a separately identified claim-bearing episteme has that method as its exact EntityOfConcern and passes A.3.2, one `U.MethodDescription` (an **account of that how-to**, sometimes called a recipe)..."*
**R-2 (No unpaired Plain in CC).** Conformance Checklists use **Tech labels** only.

A source or practice may use local aliases in its glossary. Each alias points to one Tech designation under an effective scheme and an explicit local meaning claim. Create a `SchemeSenseCell` only when a named receiver needs a stable address; use F.9 only when an actual relation between distinct exact cells is current.

Make “plain twins” (reader-friendly labels) **safe by construction**, not just style. The plain twin preserves the named value, local meaning, scope, and reader expectations of the Tech designation; it is **display-only** and **local to the stated source, practice, scheme, and use**.

* **Tech name (tech)** — the canonical, kernel-conformant label used in **normative** clauses (for example `U.SystemRoleAssignment`, `TransformerSystemRole`).
* **Plain twin (plain)** — a didactic **display alias** permitted in **expository** prose and UI display only for the stated local meaning and use.

> **Principle:** *The Tech designation names the value; a Plain twin may not change that value or its stated local meaning.* Locality comes from the named source, practice, effective scheme, and use. A Bridge is added only when its own F.9 predicate obtains.

##### E.10:6.2.2 - Plain Twin Safety constraints (normative)

**CC‑TWIN‑1 - One‑to‑one and local.**
Each Tech designation has **at most one** plain twin for one stated local meaning and didactic use; that plain twin points to at most one Tech designation in the same use.

**CC‑TWIN‑2 - Sense‑equivalence proof.**
A plain twin names the **same value under the same local meaning claim and effective scheme** as its Tech designation. When an F.17 `SchemeSenseCell` exists for that use, both expressions resolve to that exact cell. The registry notes include at least one counterexample showing how the twin could be misread and why the stated use still passes.

**CC‑TWIN‑3 - Head‑term discipline (HND).**
The plain twin preserves the **head term** of the Tech name or appends an explicit bracketed head on **first use**:

* A Plain twin for one exact local system-role kind keeps **“(system role)”** and names its Tech designation on first use. Bare *role* is not a Plain twin for a universal kind. When *service* or *access* still hides its object or relation, follow L-SERV and A.6.P:4.11a; after recovery, keep that object's or relation's head. Methods keep **“(method)”**, `U.Work` as a kind keeps **“(work kind)”**, one Work individual keeps **“(work occurrence)”**, a separate episteme about it keeps **“(work record)”** only when its Tech name denotes that record, and Capability keeps **“(capability)”**.
  *Examples:*
  `TransformerSystemRole` → “**Transformer (system role)**”,
  `U.PromiseContent` → “**post-op monitoring service promise (promise content)**”; an exact access relation → “**service access (access relation)**”,
  `U.Work` -> **work (work kind)**; `PumpInspection_2026-07-22T0900` -> **inspection work occurrence**; `PumpInspectionRecord_2026-07-22` -> **inspection work record** only when that Tech name denotes a separate episteme.

**CC‑TWIN‑4 - Kind‑consistent.**
A plain twin does not map across **Kinds** (C.3). If its everyday interpretation can denote a different kind—for example, *Tradition* as organization, corpus, or field—it is admitted only with a bracketed head and a **first-use local gloss** (see CC-TWIN-7).

 **CC‑TWIN‑5 - Ambiguity stop‑list.**
The following base nouns are **reserved** and are not admitted as unqualified plain twins: *Tradition, service, process, function, model, system, method, standard, library, dataset, evidence, activity, task, action*.
They are allowed **only** with an explicit head per **CC‑TWIN‑3** and a **first-use local gloss** (CC-TWIN-7). *(This list may be extended in the registry.)*

**CC‑TWIN‑6 - No cross-local relation by label.**
Plain twins are **not portable by spelling**. Reuse under another local meaning first recovers that exact value, scheme, expression, and local-sense claim. Cite an F.9 Bridge only when its direct relation between distinct exact cells actually obtains; names alone carry no authority, equivalence, or substitution.

**CC‑TWIN‑7 - First‑use gloss.**
At first occurrence in a document or screen, show a plain twin as **“Plain twin [Tech designation] — local gloss”**, for example:
“**Transformer (system role)** \[**TransformerSystemRole**] — *one local kind for systems already admitted under A.1 and eligible for the stated transformer assignments in `OR_2025`; classification creates neither an assignment nor Work. An assignment claim names both an A.2.1 occurrence and its declared `U.SystemRoleAssignment` species*”.

**CC-TWIN-8 - Normative publication-form overread ban.**
Plain twins are not admitted in **Conformance Checklists, predicates, type signatures, or acceptance clauses**. Only Tech names are normative; Plain twins are strictly didactic.

**CC‑TWIN‑9 - Twin budget.**
**At most one** plain twin per Tech designation for one stated local meaning and didactic use. Synonym piles are non-conformant because they create uncontrolled vocabulary sprawl (see F.14).

**CC‑TWIN‑10 - Registry entry and DRR.**
Every admitted plain twin has a **registry entry** recording `tech`, `plain`, `referenceScheme`, `localSenseClaim`, `sourceOrPracticeBoundary`, `didacticUse`, `head`, **SenseFidelity = {3,2,1,0}**, ambiguity notes, counterexamples, and DRR id. A change opens a **DRR**.

**CC‑TWIN‑11 - Tests.**
Twin entries pass the **Twin Harness** (see F.15): *Head term*, *Kind consistency*, *same value and local meaning*, *Stop-list compliance*, and *First-use gloss*. When a `SchemeSenseCell` is current, the harness also checks the exact cell.

### E.10:7 - Minimal Generality and Domain Anchoring (MG-DA) — names neither parochial nor vacuous

> **Principle (MG-DA).** A minted name is **as general as necessary and no more**, and its **head noun is anchored to the FPF kind being named**. First classify the **NameToken** itself using **`LEX.TokenClass`**, then apply the guardrails corresponding to that class: kernel tokens unify **across domains**; discriminator tokens and existing `ContextToken` values make one recovered local source, practice, scheme, subject, or use legible from the name itself. `ContextToken` is the existing token-class identifier; it denotes no Context object. Names too general to have an obvious domain fail MG-DA.

#### E.10:7.1 - `LEX.TokenClass` (meta‑lexical; not a USM Scope)
**Definition.** `LEX.TokenClass : NameToken → {KernelToken | ContextToken | DiscriminatorToken}`.
This is a local lexical classification function on NameTokens with the closed value set `{KernelToken | ContextToken | DiscriminatorToken}`, used by the LEX registry and MG-DA checks. It is not thereby a `U.Characteristic` or a `CharacteristicSpace`; that CHR reading would require a separately named `U.Characteristic` with one declared CSLC scale.
It is **not** a USM scope and carries **no** truth or validity semantics.

#### E.10:7.2 - `KernelToken` — Minimal Generality (MG‑K)
**MG-K1 (Tri-domain witness).** A DRR note or Glossary note provides at least three heterogeneous arenas where the invariants hold, for example manufacturing, healthcare, and cloud operations. Otherwise reject or narrow the `KernelToken` candidate and recover each word or qualifier under the object and rule that define it. Use a `ContextToken` only after the exact local source, practice, scheme, meaning, and receiving use are recovered. Use an A.19 `CharacteristicSpace` only when one named `U.Characteristic`, one declared CSLC scale, and the exact receiving use make that construction current; an assignment-state relation remains under A.2.5.
**MG-K2 (No parochial nouns).** Kernel names contain no domain nouns such as *Ticket, Microservice, Patient,* or *Developer*. Domain-looking wording is a recovery trigger, not a destination: it may denote a C.3 local kind, exact system-role kind, system-role assignment, system or architecture object, episteme or record kind, declared Characteristic and scale, source wording, ordinary qualifier, recovered local-use `ContextToken`, or another value whose kind and use are already defined. Bare *role* has no default Tech reading. `SystemRole` appears only inside a concrete local kind designation admitted through C.3 and A.2; lexical shape alone creates neither that kind nor an assignment.
**MG-K3 (No vacuity).** Avoid vacuous heads such as *Thing, Event, Process,* or *Resource*. Use existing U-kind heads such as `U.Holon`, `U.Work`, and `U.Method`.
**MG-K4 (Intent after recovery).** U-kind names and labels for an exact local system-role kind or its F.4 `SystemRoleKindDescription` encode recovered semantic intent rather than notation, implementation, or local-realizer accidents. Algorithm, hardware-form, and recipe-flavor wording is a recovery trigger, not one ontological family: name one `U.Method`, qualifying `U.MethodDescription`, `U.Capability`, `U.Mechanism`, system or architecture object, A.19 `CharacteristicSpace`, A.2.5 `SystemRoleAssignmentStateRelation`, C.29 representation, formal substrate, source wording, or another value only when the predicate for that value is satisfied. Do not use Capability, CharacteristicSpace, assignment-state relation, or mechanism as disposal bins for unlike cases.
**MG‑K5 (Notation independence, SHOULD).** The EntityOfConcern-side kind criterion is separable from any one notation or toolchain.
**MG-K6 (Refactoring safety).** If a name fails MG, record a DRR and apply F.13 **Lexical Continuity and Deprecation** rather than mutating it silently.

#### E.10:7.3 - `DiscriminatorToken` and local-use `ContextToken` — Domain Anchoring (DA-D)
**DA-D1 (kind anchoring).** The head noun names the **FPF kind or exact local construction being classified**—for example *Sense*, *Bridge*, *Characteristic*, *SystemRole*, or another subject-specific head. A concrete local system-role-kind designation may use the `SystemRole` compound, for example `ReviewerSystemRole`; bare *Role* fails this test because it does not reveal whether the claim concerns classification, assignment, participation, declaration, representation, episteme use, or ordinary wording. Readers can answer “**X of what?**” without relying on an unstated container.
**DA-D2 (Enumeration rule, not axis).** An enumerated property is a CHR construction only when one named `U.Characteristic` is bound to one declared CSLC scale in a `CharacteristicSpace`. Otherwise recover the closed value set, classified kind, local classifier, state/status frame, source wording, C.29 representation, example or alternative set, or another construction defined for that value. Avoid spatial metaphors (*axis, dimension, plane, lane, tier, layer*) unless the metaphor is a pattern-defined primitive in this spec.
**DA-D3 (Enum clarity).** If the term denotes an enumeration, the value set is **small and closed**, membership criteria are obvious from the definition, and the **kind being classified** is explicit in the name (e.g., `SenseFamily`, not bare *Family*, *RowPlane* or overly general *Facet*).
**DA-D4 (Anti-recipe).** Do not bake *how-to* or local methods into discriminator names. The way of doing belongs in one exact `U.Method`; a claim-bearing episteme belongs in `U.MethodDescription` only when that method is its exact EntityOfConcern and A.3.2's positive threshold is met. Use `U.Capability` instead when the kind under repair is an ability envelope.
**DA-D5 (Mapping discipline).** A cross-local relation is not inferred from similar labels or token classes. Use F.9 only when its direct Bridge predicate obtains between exact distinct cells; discriminator names do not suggest global identity.
**DA-D6 (Register discipline).** Keep normative tokens stable; synonyms belong in the **Plain** register only and stay outside constraints and tests.
**DA-D7 (Ban generic combinators).** Reject vague composites like *NameUseMode*, *NamingScope*, `RowFacet`, `RowPlane`, or `RowLane`. Each candidate passes **DA-D1** and **DA-D3** for a kind-anchored head, explicit classified kind, and closed-value interpretation under its classification rule. Require a `CharacteristicSpace` only when one named `U.Characteristic` and its CSLC scale have independently been declared.

#### E.10:7.4  - Global tests (apply after 7.2 and 7.3)
**MG-DA-T1 (Three-arena witness).** A **`LEX.TokenClass`(t)=KernelToken** candidate includes the tri-domain witnesses from MG-K1. Other token classes document at least one contrasting arena.
**MG-DA‑T2 (Object‑of‑talk).** The head noun uniquely signals the subject area; avoid free-floating metaphors. **MG-DA‑T3 (Implementation-word recovery).** Do not relocate mechanism- or implementation-looking wording by lexical category. First recover the object and rule; remove accidental implementation wording from the candidate token only after that recovery. Use `U.Method`, qualifying `U.MethodDescription`, `U.Capability`, `U.Mechanism`, a system or architecture object, A.19 `CharacteristicSpace`, A.2.5 `SystemRoleAssignmentStateRelation`, C.29 representation, formal substrate, source wording, or another value only when its predicate is satisfied.
**MG-DA‑T4 (Enum clarity).** For an enumeration, list the closed value set, the kind being classified, and the rule that classifies it. Add a `CharacteristicSpace` only when the enumeration is one declared CSLC scale for a named `U.Characteristic`; list shape alone does not establish CHR membership.
**MG-DA-T5 (Collision and uniqueness).** Before merge, perform a **full-text search** over the corpus and the **Reserved-Names registry**. A candidate colliding with an existing token used in another FPF sense is not admitted; rename it or raise a DRR to deprecate the prior token.
**MG-DA‑T6 (Teaching swap).** In didactic prose (E.10.D2), the term can be swapped in **without caveats**.
**MG-DA-T7 (EntityOfConcern ground).** The definition card states the EntityOfConcern-side kind criterion for membership explicitly; reviewers can check membership without consulting external narrative.

#### E.10:7.5 - Compatibility with USM (how tokens and scopes meet)
**USM applies to acts, not tokens.** Mint, rename, and use are **LexicalActs** that carry a USM scope. `LEX.TokenClass` constrains **where** a token may be used via an **AllowedScopes** policy:
**Conformance rule.** For any usage `u` of a token `t`: `LEX.TokenClass(t)=c  ⇒  USM.Scope(u) ∈ AllowedScopes(c).`

The LEX registry defines `AllowedScopes(c)` (for example, `KernelToken` use in normative kernel constraints is admitted; Plain-register use outside a glossary is restricted; a locally scoped use under another scheme requires its own valid designation rule and does not gain a Bridge by alias alone).

**Audit.** Violations are flagged as **SCR‑LEX‑Sxx** (see acceptance tests below).

#### E.10:7.5a - Lexical prerequisites for a durable token

Mentioning `LEX.TokenClass`, `LEX.Reserved-Names`, or `LEX.AllowedScopes` does not create the values needed to admit a durable token. Before a NameCard can become current, the selected `FPFCoreReferenceScheme` must resolve four things: (1) the `U.NameToken`; (2) its current TokenClass classification assertion; (3) the current reserved-name or other authoritative collision-set value and the collision result; and (4) the current allowed-scope policy and a passing use-scope assertion. A prose example, full-text absence, heading, registry-shaped table, or intended policy supplies none of them by implication.

**Worked near-miss.** Suppose `SelectedRuleContentSubgraphDesignation`, `derivedUsingRuleContent`, and `evaluatedAgainstRuleContent` are proposed as `KernelToken` candidates. They can pass the tri-domain and object-of-talk tests through assembly-rule content selected in manufacturing derivation, protocol content used in healthcare derivation while evidence separately warrants case facts, and deployment-policy content selected for cloud release evaluation while service-provision Work and operational support remain separate. Even if their spellings do not collide in the inspected corpus, corpus absence is not a reserved-name or allowed-scope result. Do not publish their F.18 NameCards or F.17 rows until all four prerequisites resolve; a placeholder card or row closes none of them.

Using these names as candidate designators in declaration content changes no predicate semantics and does not admit them as public names, enumerations, Characteristics, CharacteristicSpace values, relation kinds, or U-kinds.

#### E.10:7.5b - Role-Precision Token Classes and Allowed Uses

The eight selected names below are `KernelToken` values under `FPFCoreReferenceScheme`. Each names one value already defined or constrained by its subject pattern; the lexical rule admits no kind, relation occurrence, declaration, judgment, description, structure, NameCard, row, or publication occurrence.

| `U.NameToken` | `LEX.TokenClass` | Named value and subject pattern | Stable admitted use |
| --- | --- | --- | --- |
| `U.SystemRoleAssignment` | `KernelToken` | direct assignment family under A.2.1 | exact Core definition, directly declared species, typed reference constraint, conformance check, worked case for the same family, F.18 NameCard, or F.17 row |
| `KindUseAdaptationDeclaration` | `KernelToken` | C.3.4 declaration-episteme family | exact Core definition, typed declaration or constraint, conformance check, worked case for the same family, F.18 NameCard, or F.17 row |
| `KindUseAdaptationCorrespondenceDeclaration` | `KernelToken` | C.3.4 correspondence-declaration family | exact Core definition, typed declaration or constraint, conformance check, worked case for the same family, F.18 NameCard, or F.17 row |
| `KindUseAdaptationJudgment` | `KernelToken` | C.3.4 three-valued judgment family | exact Core definition, typed judgment or constraint, conformance check, worked case for the same family, F.18 NameCard, or F.17 row |
| `SystemRoleKindDescription` | `KernelToken` | F.4 description-episteme construction | exact Core definition, typed description or constraint, conformance check, worked case for the same construction, F.18 NameCard, or F.17 row |
| `SystemRoleAssignmentStateRelation` | `KernelToken` | A.2.5 direct relation kind | exact Core definition, directly declared relation use or typed constraint, conformance check, worked case for the same relation, F.18 NameCard, or F.17 row |
| `SystemRoleAssignmentStatePredicate` | `KernelToken` | A.2.5 predicate-value family | exact Core definition, directly declared predicate use or typed constraint, conformance check, worked case for the same family, F.18 NameCard, or F.17 row |
| `SystemRoleKindRelationStructure` | `KernelToken` | A.2.7 selected-structure construction | exact Core definition, typed structure use or constraint, conformance check, worked case for the same construction, F.18 NameCard, or F.17 row |

For all eight names, Plain wording that silently turns the token into a neighboring object is prohibited. Reuse under another local practice, source, scheme, or meaning uses that value's own identity and designation rules; when two exact cells are compared, any Bridge and use claim remain separately admitted. A change to the named value, TokenClass classification, or stable allowed-use rule reopens only the affected NameCard and row. A collision or conformance result for one dated corpus or candidate is evidence for its publication decision; it is not a reusable lexical rule or a currentness participant in the public pattern.

`SystemRole` alone is not a universal token with its own FPF kind or a NameCard subject. It is common morphology inside a concrete local designation such as `ReviewerSystemRole`. C.3 and A.2 recover that kind through its system-candidate domain, operative work-facing membership condition, intended member/non-member boundary, and continuity rule; practice or source provenance only locates or prompts comparison of the definition. `AssignedSystemRoleKindSlot`, `SystemRoleAssignmentSlot`, and fields ending in `...SystemRoleKindRef` or `...SystemRoleAssignmentRef` remain declaration-local `ContextToken` uses; the token-class name adds no Context object, and the fields are typed by existing `U.KindRef` or `U.RelationRef`, not by newly minted RefKinds. `J_kindUse` remains local notation. None receives a public row merely because the spelling recurs.

#### E.10:7.6 - Metaphor guidance (informative heuristics)

Prefer **object‑anchored heads** to metaphors. If a metaphor is unavoidable, ensure it is (a) explicitly defined by a pattern here, and (b) unambiguous within the **NameClass**. Example families (use sparingly):
* **Progression metaphors** (*level, tier, ladder*): only where a **gate or upgrade** is defined by the pattern.
* **Separation metaphors** (*lane, track*): only where parallel, non‑interfering flows are enforced by rules.
* **Grouping metaphors** (*family, class*): only for **small, closed enumerations** attached to a clearly named classified kind (e.g., `SenseFamily` rather than bare *Family*).

#### E.10:7.7 - Short‑form and acronym discipline
**SF-1 (First expansion).** On first use, expand the term and place the short form in parentheses (e.g., “Minimal Generality and Domain Anchoring (**MG-DA**)”).
**SF-2 (Uniqueness).** Register short forms in the **Reserved-Names** list and perform the collision check (MG-DA-T5).
**SF‑3 (Form, SHOULD).** Prefer typographic separators (**MG-DA**) to fused acronyms (**MGDA**). Use the fused form only in code or identifiers where punctuation is disallowed, and only after registration.

#### E.10:7.8 - Examples (illustrative, canonical)
Prefer **`U.PromiseContent`** (promise) over *BusinessService*; **`U.Capability`** over *Function*; **`U.Dynamics`** over *NaturalProcess*. Replace *ScheduleProcess* with `U.WorkPlan` only when one episteme passes A.15.2: one present EntityOfConcern, one horizon, at least one `PlanItem`, and substantive coordination claims about possible future performed work. Otherwise retain the schedule representation, planning cue, or other recovered construction.
Do **not** mint *ETLService* at kernel level. Recover the ETL claim first: the way of doing may be one `U.Method`; a separately identified claim-bearing episteme may be `U.MethodDescription` only when that method is its EntityOfConcern and the A.3.2 substantive-description threshold is met. An ETL label, pipeline diagram, code expression, mechanism, work plan, dated Work occurrence, or API publication establishes neither membership. If a relied-on *service* use still hides another subject or relation, apply L-SERV and A.6.P:4.11a and name the recovered claim; the suffix alone requires no promise, access, acceptance, Work, or publication branch.

#### E.10:7.9 - Acceptance and regression checks (LEX and USM)
**SCR‑LEX‑S01 (TokenClass declaration).** Every normative token has a declared `LEX.TokenClass`.
**SCR‑LEX‑S02 (Collision and uniqueness).** Full‑text + Reserved‑Names check passes (no other meaning in FPF).
**SCR‑LEX‑S03 (kind anchoring).** Heads name the FPF kind classified (DA‑D1).
**SCR‑LEX‑S04 (Enumeration rule gate).** Every enumeration names its closed value set, classified kind, and classification rule. Require a `CharacteristicSpace` only when one named `U.Characteristic` is bound to one declared CSLC scale; otherwise retain the local classifier, state/status value set, source wording or C.29 representation, example or alternative set, local kind, or another construction defined for that classification.
**SCR‑LEX‑S05 (USM compatibility).** For each LexicalAct, `USM.Scope ∈ AllowedScopes(LEX.TokenClass)`.
**SCR‑LEX‑S06 (Slot and Ref suffix discipline).** A token ending in **`…Slot`** names the declaration-local **SlotKind** inside one exact A.6.5 `SlotSpec` of one reusable `RelationSignature`. A token ending in **`…Ref`** names either a RefKind admitted by its direct reference pattern or a receiving-episteme field explicitly typed by that RefKind; the field remains designation or reference apparatus and does not become the participant or SlotSpec. No ValueKind or representation field may acquire either suffix by shape alone.
**SCR-LEX-S07 (Manifest `provides` follows exact signature claims).** If a `SignatureManifest` is present, its `provides` entry is used only when that signature's exact `U.ClaimGraph` states that the signature introduces public names for dependent use. The entry carries that claim content or visibly represents it; list membership alone establishes neither provision nor a consumer dependency. Include only names actually introduced by this signature under the patterns that define them, such as its own A.6.5 relation-participant SlotKinds and RefKinds whose direct reference patterns admit them. A RefKind defined elsewhere remains defined there, and membership in an A.6.1 operation-argument or result declaration list does not transfer its definition to the manifest. A mathematical operand, table column, tuple place, or other C.29 representation element becomes no provided SlotKind by shape; any reuse still needs its independently governed declaration and explicit correspondence.
**RSCR‑LEX‑E01 (Banned generics).** Reject tokens matching the banned combinators list (DA‑D7).
**RSCR‑LEX‑E02 (Metaphor hygiene).** If a metaphor is used, show the pattern that defines it; otherwise rename.
**RSCR‑LEX‑E03 (Strategy token minting).** Reject new Kernel tokens named **Strategy** or **Policy** as kinds. Recover the subject first: use a **lens**, **flow**, or **composition** inside **G.5** when that is the actual construction, or use a subject-specific **…Description** or **…Spec** under the exact project profile and effective scheme when that construction's own admission gate passes. (Prevents kernel overloading; aligns with C.22 “no minted Strategy head”.)

### E.10:8 - Morphology and Lexical Form (LEX.Morph)

> **Principle.** Form follows the **FPF kind being named**. A token's morphology (suffix, prefix, and casing) expresses **what kind of thing** it names, respects **MG-DA** (Minimal Generality and Domain Anchoring), and passes **LEX.TokenClass** gates:
> `LEX.TokenClass(token) ∈ {KernelToken | ContextToken | DiscriminatorToken}`.
> Morphological choices never override **EntityOfConcern, Description episteme, specification use, publication faces, publication forms, `PublicationUnit`s, carriers, renderings,** or **CHR\:ReferencePlane** semantics.

#### E.10:8.0 - Casing and basic forms

**M‑0 (Casing and categories).**
Kind names and exact local system-role-kind labels: **UpperCamelCase** (`IncisionOperatorSystemRole`, `MethodDescription`).
Relations and verbs: **lowerCamelCase** (`performedUnderAssignment`, `isExecutionOf`, `bindsMethod`).
IDs and instances: **flat with delimiters** chosen by the exact local naming scheme or project profile, but never colliding with kind-name or system-role-kind-label forms (e.g., `W#Seam134`, `ctx:Hospital.OR_2025`).
**Register discipline:** normative tokens use the Technical register; Plain synonyms are allowed in prose only, never in constraints.

#### E.10:8.1 - Reserved suffixes (gated by LEX.TokenClass, EntityOfConcern and Description-episteme boundary, and specification use)

> **Use tables as a whitelist.** Rows indicate **when** a suffix is permitted and **what it means**. The EntityOfConcern and Description-episteme boundary and specification-use gate prevents EntityOfConcern, Description episteme, specification use, and publication-relation confusion; “Examples” are illustrative.

| **Suffix**              | **Kind named by suffix**                   | **EntityOfConcern and Description-episteme boundary and specification-use gate**                       | **LEX.TokenClass gate**         | **Examples**                                      | **Typical inadmissible uses**                                       |
| ----------------------- | ------------------------------------------ | ------------------------------------ | ------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------- |
| **`SystemRole`** (compound ending) | **One exact local system-role kind** | The kind is independently admitted under C.3 and A.2 through its `U.System` candidate domain, operative work-facing membership condition, member/non-member boundary, and continuity rule. Practice or source provenance only locates or prompts comparison of the definition. The name supplies no assignment, agency, capability, or Work. | ContextToken | `TransformerSystemRole`, `ApproverSystemRole` | Bare `...Role`; participant, declaration, representation, evidence, status, standard, source, constraint, commitment, or publication-use readings. |
| **`Method`**            | **One semantic way of doing** | EntityOfConcern side | KernelToken or ContextToken | `SteriliseInstrumentMethod` | Attaching an episteme edition or carrier version to the Method. When one exact method-description edition matters, use a separate governed `U.EpistemeRef` and only the narrow edition selector defined by A.3.2; keep tooling and carrier versions separate. |
| **`MethodDescription`** | **Claim-bearing episteme about one exact admitted method** | Description episteme only when its claims make at least one substantive statement about that method as a way of doing | KernelToken or ContextToken | `SteriliseInstrumentMethodDescription` | Admission by recipe, procedure, algorithm, code, diagram, document form, or label; calling it "process"; encoding runtime actuals; embedding an edition or carrier version in the conceptual name. |
| **`...Spec`**             | **Testable specification** (acceptance-bound) | Description episteme admitted for specification use                              | KernelToken or ContextToken        | `MethodSpec`, `TransformationFlowStructureSpec`, `SystemSpec`            | Using “Spec” without acceptance tests or harness; treating formal notation alone as specification; putting runtime actuals here. |
| **`Work`** | **Work occurrence kind or an occurrence classified under it** | `U.Work` is the admitted world-side kind; one Work individual is a dated occurrence. A run log, ticket, assertion, description, or record about it is a separate `U.Episteme`. | KernelToken for the kind; ContextToken for an individual or record with an explicit distinguishing head | `U.Work`; `W#Seam134WorkOccurrence`; `W#Seam134WorkRecord` | Plans and schedules; design-time recipes; using a run record as the occurrence; defining a Work subkind by an act label; storing actual relations as occurrence fields. |
| **`WorkPlan`** | **Claim-bearing episteme coordinating possible future performed work** | Same-individual dependent kind of `U.Episteme` only when A.15.2 recovers one present EntityOfConcern, one horizon, at least one `PlanItem`, and substantive coordination claims | ContextToken after membership | `MaintenanceWorkPlan_Q3` only after the A.15.2 gate | Admission by schedule, window, planned item, ticket, calendar, or plan-record form alone; logging actuals; claiming execution. |
| **`Service`** (recovery trigger only) | **No kind is named by this suffix before recovery; afterward use the head that names the recovered object or relation** | Apply L-SERV and A.6.P:4.11a to recover the promise content, commitment, bearer, Method, Work, acceptance, publication or API description, or direct relation actually used; preserve the EntityOfConcern/Description-episteme boundary and specification-use gate under the pattern for that claim. | Trigger wording only; any retained ContextToken must already name the recovered object or relation and its use | object-storage service promise; passport-issuance service-access claim | Using `Service` as a final durable head-kind; naming teams or APIs as Service; treating the possible readings as one bundle. |
| **`Capability`**        | **System ability**                         | EntityOfConcern side                              | KernelToken or ContextToken        | `ScheduleGenerationCapability`                    | Mislabeling system-role kinds, assignments, or methods as capabilities.                         |
| **`Dynamics`**          | **Law or model of change**                    | EntityOfConcern side                              | KernelToken or ContextToken        | `LotkaVolterraDynamics`                           | Using for abilities (`Capability`) or recipes (`Method`).             |
| **`Observation`**       | **Observation record or kind**                | (run record; not EntityOfConcern and Description-episteme or specification use)            | ContextToken or DiscriminatorToken | `VibrationObservation`                            | Mixing with `MethodDescription` or `Evaluation`.                      |
| **`Evaluation`**        | **Evaluation episteme or evaluation record**        | Description episteme or Description episteme admitted for specification use              | ContextToken or DiscriminatorToken | `CalibrationEvaluation`                           | Using to name system-role kinds, assignments, or methods.                                       |
| **`EvidenceRole`** (retired trigger only) | Source evidence-role wording; recover evidence-use, source-use, status-use, assurance-use, gate-use, or publication-use relation. | Trigger wording, not a system-role kind | Trigger wording | evidence-use, status-use, source-use, or publication-use relation named by its direct pattern | Using as a system-role kind, `U.SystemRoleAssignment`, or generic evidence. |
| **`Episteme`**          | **Epistemic knowledge unit** (structural)  | Description episteme or Description episteme admitted for specification use                            | KernelToken or ContextToken        | `TraceabilityEpisteme`                            | Colliding with CHR **ReferencePlane** (never suffix “Plane”).         |
| **`System` or `Holon`** | **Substantial entity** | EntityOfConcern side | KernelToken or ContextToken | `AnesthesiaSystem`, `OrderFulfillmentHolon` | Using to denote a source, scheme, local-use qualifier, or run record. |
| **`Boundary`**          | **System boundary**                        | EntityOfConcern side                              | KernelToken or ContextToken        | `SterileFieldBoundary`                            | Using as a system-role kind or method.                                            |
| **`Objective`** | **Target state** | EntityOfConcern side or Description episteme side, depending on formalization | KernelToken or ContextToken | `HemostasisObjective` | Encoding acceptance tests in the objective. Put tests in the specification governed by their actual subject; use `MethodDescription` or `MethodSpec` only when that subject is one admitted `U.Method`, A.3.2 membership holds, and the specification-use gate is present. |
| **`Requirement`** (trigger only) | **No FPF-wide suffix meaning.** Recover the constraint, commitment, completeness condition, result expectation, dependency, sufficiency condition, availability or relevance state, or coverage constraint. | Trigger wording; a durable local-use token exists only after its lexical admission rule is satisfied. | Trigger wording or a ContextToken named for the recovered construction | latency constraint under its constraint pattern; `U.Commitment` when accountable undertaking is current | Publishing `Requirement` as a general head or suffix; treating unlike constructions as one kind. |
| **`Context` or `BoundedContext`** (trigger or established source term only) | **No FPF-wide kind or card is named by this suffix** | Apply E.10.D1. For the established DDD term, use A.1.1 and name the exact model-use relations or selected `BoundedModelUseStructure`; for another use, name the actual source, scheme, scope, situation, frame, or local practice that changes the action. | Trigger wording or an already admitted local-use token | quoted DDD bounded context; source label retained as source wording | Minting `U.BoundedContext`, a mandatory Context Card, or a generic identity container. |
| **`surface`** (trigger only) | Not a durable Tech head by itself; recover publication face, form, unit, carrier, rendering, UI face, physical surface, geometric surface, or another FPF object named by value. | publication availability or ordinary source wording | Trigger wording | publication face, interop publication form, carrier relation | StructureSurface, MechanismSurface, PortfolioSurface |
| **`Card`**                 | UTS or record unit (episteme)               | Description episteme, Description episteme admitted for specification use, or publication-unit use, depending on FPF kind named by value       | ContextToken                     | MethodCard, ExternalIndexCard            | Encoding runtime actuals; using as a ‘Service’  |

##### E.10:8.1.1 - Suffix conventions and retained-family boundaries

| **Suffix** | **Lexical class** | **Meaning and ontology** | **Where it lives** | **Examples and notes** |
|--- |--- |--- |--- |--- |
| **Space** | EntityOfConcern-side kind | A typed **state space** (finite product of declared Characteristic×Scale components); no procedures | Kernel A.19; CHR and space consumers | `CharacteristicSpace`, `CreativitySpace`. Any episteme that defines or describes the Space remains separately identified. A selected definition edition is itself one exact `U.Episteme`; the Space is not editioned. |
| **SpaceRef** | Pointer | Governed reference to one exact Space | Direct reference pattern; data fields and UTS | `CharacteristicSpaceRef` resolves to the exact Space. When a use depends on one exact Space-definition episteme, carry a separate governed field typed by `U.EpistemeRef` whose referent is that episteme; only its direct reference pattern may define a narrow edition selector. |
| **Map** | EntityOfConcern-side kind (method) | One exact mapping `U.Method` from subjects to coordinates in a declared Space | A.3.1 and the method-family pattern; Description epistemes remain separate | `DescriptorMap` names the method only after A.3.1 admission. A claim-bearing episteme about that exact method may separately qualify as `U.MethodDescription`; a representation, record, or file does not. |
| **MapRef** | Pointer | Governed reference to one exact mapping `U.Method` | Direct method-reference pattern; data fields and UTS | `DescriptorMapRef` resolves to the method. If the use depends on one exact method-description episteme, carry a separate governed field typed by `U.EpistemeRef`; do not attach an edition selector to the method reference. |
| **Def** | Registry-local alternate token | A direct CG-Spec registry may use **...Def** for one exact governed definition or specification item; the suffix alone does not decide whether that item is an episteme, formal object, method, formula, or publication form | Exact CG-Spec registry | `DistanceDef` is admissible only inside the registry that defines its referent kind and use. Prefer **...Spec** in new normative prose when an exact Description episteme has actually been admitted for specification use; do not generalize **...Def** as an FPF-wide suffix. |
| **DefRef** | Pointer | Registry-local reference whose exact referent kind and RefKind are defined by the direct CG-Spec registry | Exact CG-Spec reference pattern; data fields and UTS | `DistanceDefRef` is admissible only when that registry says what it resolves to. If a use must pin one exact CG-Spec episteme, carry a separate governed field typed by `U.EpistemeRef` and use only a selector defined by that registry's direct reference pattern for that episteme edition. Do not treat **...DefRef** as a global synonym for **...SpecRef**. |
| **Spec** | Description episteme admitted for specification use | Testable invariants bound to acceptance harnesses | E.10 and A.21 | Stable, testable definitions; **normative** by default; admitted for specification use. Use for normative calculi plus scoring and normalization specifications. |
| **Slot** | Relation-declaration suffix | Declaration-local **SlotKind** inside one exact A.6.5 `SlotSpec` of a reusable `RelationSignature`; it distinguishes one relation-participant meaning and is neither the actual participant nor a representation place | A.6.0 `RelationSignature`; A.6.5 `SlotSpec` declaration | `EntityOfConcernSlot`, `GroundingHolonSlot`. A mathematical operand or argument place remains a C.29 representation element until explicit correspondence; operation argument and result declarations remain under A.6.1. `Position` and `place` are not alternate FPF names for a declaration slot. |
| **Ref** | Pointer | **Reference or identifier** whose RefKind is admitted by its direct reference pattern; a receiving assertion or relation-occurrence-description episteme may carry a field typed by that RefKind to designate an actual participant, but the reference, field, and participant remain distinct | Direct reference pattern; receiving episteme fields and UTS | `U.EntityRef`, `U.HolonRef`; episteme fields `…Ref : U.EntityRef`. `…Ref` never carries content and is never a ValueKind, SlotKind, or actual participant. |
| **Series** | Conditional collection or structure label | Not an edition mechanism. Several exact `EpistemeEditionRelation` occurrences may be selected as a lineage structure only when one named receiving use depends on their organization; any selected edition collection and its membership remain separate | C.2.1 with A.22 for the selected structure and A.14 for any collection | Do not mint `U.EditionSeries`; order, shared title, or collection membership establishes no edition continuity. |
| **edition selector** | Reference selector defined by its direct pattern | Optional only on a governed reference whose referent is one exact `U.Episteme` and whose direct reference pattern defines the selector; it selects an already recoverable edition and establishes neither episteme identity nor historical continuity | Direct reference pattern and C.2.1 | `signatureRef.edition` is admissible where A.6.0 defines that narrow selector. Do not infer a universal `<Thing>Ref.edition` property. |

**Notes.**
• **Kernel‑only ban list** remains in § 8.3.
• **CHR guard:** the only token that may use the word *plane* is **CHR:ReferencePlane**.
• **Axis and dimension metaphors** are not selected FPF heads; use **Characteristic** only for one declared measured aspect. For an enumeration, name its closed value set, classified kind, and classification rule; use **CharacteristicSpace** only when that enumeration is the declared CSLC scale of the named Characteristic (see § 7).

**Not only suffix guard**
* Suffixes are closely related to kinds and **should** be clearly guarded by MG-DA.
* Other morphemes, not only suffixes, also respect kinds. For example, **Space is a geometric concept** and is not admitted as a suffix (`...Space...`) or other morpheme for naming non-geometric entities. Prefer **Set**, **Kind**, or **Kit** where membership is intended.

**L-EPI-PUB — episteme, publication, view, carrier, direct-relation, representation, and authority-reference discipline**
* Use `U.Episteme` for the claim-bearing unit. `U.EpistemePublication` is a rejected kind name: when the selected edition is available as a published episteme, name or make recoverable its exact `EpistemePublicationRelation` occurrence, publication form, bounded use, and carrier under `E.24.PUB`. The rejected spelling may remain only in an explicit rejection explanation or a negative test, never as a positive object, kind, reference, or field.
* Name the publication form separately from the episteme: for example `U.PreArticulationCuePack`, `U.AbductivePrompt`, typed bounded projection, partial normal form, endpoint-specific publication form, or another declared form. A publication form is not itself the governing FPF source.
* Name `U.View` and MVPK face separately from the publication form. A `PlainView`, `TechCard`, `InteropCard`, or `AssuranceLane` is an episteme-level view or publication face, not the source claim, not the publication form itself, and not the SCR or RSCR carrier.
* Name the carrier or rendering relation separately. Documents, dashboards, generated screens, trace files, cards, and transport formats hold or render a publication; they are not the `U.Episteme`, not the claim or effect being relied on, and do not supply the rule for that claim.
* Name source-finding cues separately from source epistemes. A cue, badge, credential view, dashboard tile, heading, signature-looking mark, or generated explanation may help find a source; it does not by itself create an `authoritySourceRef` target, evidence relation, gate decision, assurance claim, exact `U.SystemRoleAssignment` occurrence, status assertion, Work occurrence, deontic permission, or Work authorization.
* Use an ordinary PatternID reference when a reader only needs to find the rule. Add `relationFunctionClaimRef` and the defining or constraining `ClaimGraph` only when admissible interpretation, comparison, migration, publication, or reuse depends on that exact rule identity. Use `authoritySourceRef` when a non-pattern target such as an external standard, editioned register, DRR, gate decision, policy record, system-role-assignment register, or status register carries the relevant authority. Do not use generic sign, source, project-work, or container-placement wording as solution terms.
* When a published episteme is used for work, name the P2W chain element being used: intended method family, selected method or method of work, one exact `U.WorkPlan` baseline, planned work, or one actual Work occurrence admitted under `U.Work`. Then name any separate claim-bearing episteme about that occurrence and any separately current direct resource-use, affected-referent, operation-application, measurement, evaluation, decision, delivery, acceptance, or receiving-use relation under the pattern that defines it; when a production-work, entity-inception, or production-completion claim is current, name one local A.15.PROD claim instead of implying a universal production relation. Apply `A.6.P.WMR` only while one such Work-to-Method boundary relation remains hidden after generic relation recovery. Do not let generic `action`, `use`, `material`, `work result`, or `result measurement` hide that distinction.
* Use `C.2.P` when episteme-publication-heavy wording carries an episteme, publication, view, carrier, relation, admissibility, evidence, work, gate, decision, method, or pattern-use claim. `E.10` keeps the lexical and naming discipline; `C.2.P` recovers the FPF kind; obtaining relation and participants; receiver-needed occurrence; reusable A.6.5 declaration; claim-bearing episteme and participant designations; C.29 representation and correspondence; project-side FPF kind and reference; or a not-triggered disposition before the wording is accepted.

**Publication face, form, unit, and carrier discipline - `surface` as trigger wording**
* **Definition.** `surface` is trigger wording, not a durable FPF Tech head by itself. When it has FPF-governed use, recover whether the sentence means publication face, publication form, publication unit, carrier, rendering, UI face, front-end face, physical surface, geometric surface, companion publication, projection material, carrier relation, or another FPF kind or relation named by value.
* **Allowed final heads:** publication or carrier terms named by value, or deliberately ordinary physical or geometric `surface` when no FPF-governed use is carried.
* **Inadmissible final heads:** `StructureSurface`, `MechanismSurface`, `PortfolioSurface`, and any `...Surface` that hides a structural, mechanistic, measurement, review, assurance, explanation, comparison, or publication-unit object.
* **Preferred alternatives:** name publication face, form, unit, carrier, and rendering; use `...Boundary` for structural borders, `...View` for episteme and view relations, and `...Card` only for a UTS or record unit when that is exact.

**L-Space - Disciplined use of *Space***
* Use *Space* only for **CHR‑grounded measurement and state constructs** such as `CharacteristicSpace` per A.19. Do **not** coin generic `…Space` for sets, portfolios, or publication forms. Publish portfolios and archives as **sets** via admissible selectors; publish them on UTS as **views** or **cards**, not as spaces.
* **Field-name and direct-declaration guard.** In A.6.0 and A.6.1 declarations, write `SubjectKind` and `RangedValueKind` as direct content fields. Add `ResultKind`, `SliceSet`, and `ExtentRule` only when their distinctions are current. A heading that merely wraps these fields is presentation, not another declaration component, and receives no Tech name. Reserve *Space* for CHR-grounded measurement, state, and `ReferencePlane` constructs when those are the governed value kinds. Let the referenced C.3 kind, admitted durable U-kind, Concept-Set row, or imported signature symbol carry `...Space` where appropriate; use `...Set` for an ordinary set-valued universe.
* Space is a geometric concept. Do not use it as a suffix or morpheme for non-geometric sets, portfolios, or publication forms; use `Set`, `Kit`, `Bundle`, `Portfolio`, or another direct FPF kind when that is the current object.

**L‑ROLE — guarded recovery from *role***
* Bare claim-bearing *role* is a lexical trigger with no default Tech reading. Apply `E.10.ROLE`, write the ordinary sentence with its recognizable object and action or relation, and stop as soon as one exact object or relation and its direct pattern are clear.
* Use `SystemRole` only as the common compound inside one concrete local system-role-kind designation such as `ReviewerSystemRole`. Recover the kind through C.3's candidate domain, operative membership distinction, member/non-member boundary, and continuity rule. Practice or source provenance is a locator and comparison cue; the spelling creates no system admission, assignment, agency, capability, responsibility, participation, Work, evidence use, or status.
* A participant meaning or actual participant remains under its direct relation; a reusable declaration place remains an A.6.5 `SlotKind` or A.6.1 declaration; a tuple, table, formula, graph, diagram, schema, or call position remains under its representation pattern and explicit correspondence. None becomes a system-role kind by wording.
* Preserve ordinary or quoted *role* when no FPF claim relies on it. Preserve *owner* when a precise ownership relation is current—for example, an architectural, organizational, policy, source, or responsibility relation. This rule forbids lexical cleansing as well as default formalization.

#### E.10:8.2 - Inadmissible suffixes and the DevOps, Data Governance and Repository-Workflow Lexical Firewall

**M-F (Inadmissible in Kernel tokens).** KernelToken names do not use *...Function*, *...Process*, *...Task*, or *...Activity*. These are ambiguous or vacuous; recover the object through section 6 before naming it: one `U.Method`, one qualifying `U.MethodDescription`, one Work occurrence admitted under `U.Work`, or another accepted recovered value. The source suffix alone selects none.

**M-FW (Tool and file markers).** Tooling and file suffixes (*...API*, *...JSON*, *...YAML*, *...CI*, *...Kafka*, *...Postgres*) are **not** part of conceptual names. Place them in local source or practice glossaries or operational configurations (DevOps Lexical Firewall). Kernel names never carry tool, format, or notation marks. This is conceptual discipline, not a data-management ontology.

#### E.10:8.3 - Prefix discipline

**M-P1 (Reserved prefixes).** `U.` is reserved for admitted U-kinds and dependent `U.*` forms admitted under their definitions; `Γ_` for algebraic operators; `CAL, LOG, and CHR` for **pattern packages**. A local glossary, scheme, source label, or use never mints `U.*`.

**M-P2 (Edition and version markers).** Use a model-use marker only when A.1.1's direct model-use relations or a selected `BoundedModelUseStructure` require it. Select one exact episteme edition only through a typed reference whose referent is that exact `U.Episteme`, with a narrow selector defined at its reference-pattern locator. Do not attach an edition selector to an EntityOfConcern-side `Method`, Space, system, bare `Service`, or their references. When a use depends on a defining, describing, CG-Spec, service-description, or service-offer episteme, reference that episteme separately. A service-access publication, publication occurrence, publication form, and carrier retain their own references and do not inherit the episteme selector. Tool and carrier versions remain separate. Authors may annotate local service labels for didactics only after every named value is recoverable.
**Norms (edition, release, and version).**
1) **edition** — one exact `U.Episteme` with its own C.2.1 identity. A later episteme is related to an earlier one only when the exact `EpistemeEditionRelation` predicate obtains; shared label, order, file version, or selector value establishes none. `PhaseOf` may describe one unchanged episteme over a proper interval but never connects different episteme identities.
2) **release** — a separately governed publication or release occurrence, or the exact Work that performs it when that Work claim is current. Publication occurrence, publication form, and carrier remain distinct; release establishes neither episteme identity nor `EpistemeEditionRelation`.
3) **version** — a tooling or carrier identifier for a file, package, code object, rendering, or other carrier-specific use. It is not an episteme edition, publication occurrence, or release claim and does not belong in Core EntityOfConcern names.

**Property discipline.** There is no universal `<Thing>Ref.edition` property. A direct reference pattern may define a narrow edition selector only for a governed reference whose referent is one exact `U.Episteme`. A Space, `U.Method`, formula, system, publication form, or carrier reference remains a reference to that object; pair it with a separately governed episteme reference when one exact defining or describing edition matters. A selector value identifies neither an edition relation nor historical continuity.

#### E.10:8.4 - Morphology tests (apply with § 7 MG-DA)

**M‑1 (Kind-side test).** The candidate fits **one** admitted kind or one side in the Strict Distinction lattice (EntityOfConcern ≠ Description episteme ≠ publication carrier; exact local system-role kind ≠ `U.SystemRoleAssignment` occurrence ≠ Method ≠ Work). If not, **rename** or split.

**M-2 (Classified-kind anchoring).** The head noun names the classified FPF kind or exact subject construction: exact local system-role kind, `U.SystemRoleAssignment` occurrence, Method, Work, Characteristic, Capability, constraint claim, `U.Commitment`, publication form, service-access relation, service-offer record, exact source or practice boundary, local-use designation, or another direct FPF value. Bare *role* first uses `E.10.ROLE`; no free-floating metaphor, bare `Service`, bare `Context`, or bare `Requirement` head passes by lexical shape.

**M-3 (Family congruence).** Where eligibility clarity is needed, add the exact subject-specific characteristic or `SystemRoleAssignmentStateRelation` as a separate qualifier for the current value; do not hide either in a system-role-kind name. Do not turn standards, requirements, evidence, or status labels into `...SystemRole` names, and do not fake families with bare metaphors such as `RowPlane`, `senseFamily`, or `...Lane`.

**M‑4 (Run and description split).** Use **`Work`** only for executions. Treat `recipe`, code, diagram step, procedure, or document form as recognition evidence only: classify a claim-bearing episteme as `U.MethodDescription` only when its exact EntityOfConcern is one admitted `U.Method` and its claims pass the A.3.2 substantive-description threshold; keep the method, representation, publication form, plan, and Work occurrence separate.

**M-5 (Kernel parochiality).** `KernelToken` names carry **no domain nouns**. Recover domain markers under the objects and rules that define them. Use `ContextToken` only after the exact local source, practice, scheme, meaning, and receiving use are recovered; use A.19 `CharacteristicSpace` only after its named `U.Characteristic`, declared CSLC scale, and exact receiving use are current; use A.2.5 `SystemRoleAssignmentStateRelation` only when that direct predicate obtains. Lexical shape establishes none of them.

**M‑6 (Vacuity ban).** Avoid vacuous heads (*Thing, Event, Process, Resource*). Use established U-kind heads such as `U.Holon`, `U.Work`, and `U.Method`.

**M-7 (Notation independence).** The EntityOfConcern-side meaning survives notation and tool swaps.

**M-8 (Collision and uniqueness).** Before merge, perform **full-text** and **Reserved-Names** checks; a token colliding with another FPF meaning is not admitted (cf. MG-DA-T5).

#### E.10:8.5 - Alias hygiene

Aliases are permitted only in one named local source or practice glossary under an effective scheme and explicit local meaning claim. Each alias points to one Tech designation; it does not assert semantic equivalence or a Bridge. No global aliases.

#### E.10:8.5a - Entry lexeme support and lexical-query discipline

Public first-entry scenario text, ToC query rows, local Problem-frame recognition text, or expanded `I.2` entry-disambiguation cases may use one compact **entry lexeme cue** block when the lexical issue changes the first useful FPF entry.
That cue block should not be copied into every pattern body by default.
Keep it instead in:

* FPF `readme` section,
* `E.11` public-entry positions,
* `I.2` expanded entry-disambiguation cases,
* `Table of Contents` query rows,
* or one bounded lexical-query record governed by `F.17`, `UTS`, or `F.18`.

This block remains one editorial lexical-query set.
It does not mint names, aliases, durable U-kinds, bridges, or semantic equivalences
by itself.
When visible, it should distinguish at least:

* canonical label,
* plain-language twin,
* domain alias,
* lexical-query cue,
* rejected cue,
* false friend or inadmissible synonym.

Minimal visible lexical-query shape may therefore use one compact field set such
as:

```text
canonical
noncanonical_visible
domain_query_examples
forbidden_aliases
```

Ordinary lexical-query support should stay compact:

* ordinary `Table of Contents` rows: prefer `2-5` query phrases;
* ordinary `README` scenario or `E.11` entry-distribution cues: keep only the most discriminating domain phrases and false friends;
* fuller lexical sets belong under `F.17, F.18, and E.10` only when one real
  naming, alias, bridge, or collision claim exists.

Lexical support should increase entry precision, not maximize keyword recall.
The same boundary should be kept explicit in lexical support:

* `lexical_hook` is not one alias;
* one alias is not one canonical name;
* one search cue is not one semantic equivalence;
* one `entry_orientation_label` is not one `RelationKind`.

Language-specific query cues may be added as entry-lexeme support.
They do not become canonical names, aliases, or semantic equivalents unless
an accepted F.18 naming settlement admits that use; otherwise keep the phrase as ordinary
local query wording. Such a practitioner phrase may help recover a
canonical FPF pattern while remaining lexical-query support only.

#### E.10:8.6 - Compatibility with USM (acts and tokens)

**LEX applies to tokens; USM applies to acts.** Mint, rename, and use are **LexicalActs** that carry a USM scope (e.g., ClaimScope, WorkScope). LEX constrains **where** a token form may appear via **AllowedScopes** policies:

`LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)`.

Example: use of a `KernelToken` in a locally scoped constraint is admitted only under the exact scheme and allowed-scope rule; an alias adds no Bridge. Logging `Work` inside a MethodDescription violates M-4 and the policy.

#### E.10:8.7 - Acceptance and regression checks (LEX and USM)

* **SCR‑MOR‑S01 (Suffix whitelist).** Every normative token with a reserved suffix matches § 8.1 row semantics and passes EntityOfConcern and Description-episteme boundary and specification-use gates.
* **SCR-MOR-S02 (Kernel exclusions).** KernelToken names contain none of the inadmissible suffixes from section 8.2.
* **SCR-MOR-S03 (Prefixes).** Reserved prefixes obey § 8.3; no local glossary, source, scheme, or use mints `U.*`.
* **SCR‑MOR‑S04 (Run and design gate).** `Work` appears only for executions; `MethodDescription` has no runtime actuals.
* **SCR‑MOR‑S05 (Collision).** Full‑text + Reserved‑Names checks pass (no other sense of the token elsewhere).
* **SCR‑MOR‑S06 (Object‑of‑talk).** Heads pass M‑2; no bare metaphors as heads.
* **RSCR-MOR-E01 (DevOps firewall).** Tool and file suffixes stay in local glossaries or operational configurations; none leak into KernelToken names.
* **RSCR‑MOR‑E02 (USM compliance).** For each LexicalAct, verify `USM.Scope ∈ AllowedScopes(LEX.TokenClass)` (see § 7.5).

#### E.10:8.8 - Autonomy lexicon (L‑AUTO )
**Inadmissible in Core:** bare “validity”, bare “actor” or “agent” as free-standing nouns, “kill switch”, “process” for behavior, and “envelope” when used **as scope**.
**Use instead:** *Scope (G)* for epistemic scope; *WorkScope* for capability bounds; an admitted `U.System` for the actor or doer. When performed Work is current, use A.15.1 and F.6 to identify the dated Work, performer, and assignment. Use a `...SystemRole` designation only when that classification itself matters. Use *SpeechAct* for overrides and *SafeStop* instead of “kill switch”.
**Named prefixes (policy and registry):**
* `aut:` for AutonomyBudgetDecl fields (e.g., `aut:action_tokens`, `aut:risk_bands`);
* `guard:` for guard checks bound to `AdmissibilityConditionsId`;
* `ovr:` for override SpeechActs (`ovr:PauseAutonomy`, `ovr:ResumeAutonomy`, …).

**Notes.**
1) Scope-sensitive guards declare the **Gamma_time** window selector used for admission checks.
2) Proper names of patterns and components that already include “Agent” or “Agency” (e.g., *Agency‑CHR*, *Agent‑Tools‑CAL*) are permitted as **titled terms**; avoid re‑introducing “agent” as a free‑standing noun in new prose.

#### E.10:8.9 - LEX-CHR-STRICT — Reserve *Characteristic* for CSLC-measurable aspects

**Intent.** Prevent calling **non-measurable** objects (sets, statuses, scopes, policies, bridges, contexts, guards) “characteristics”.

**Rule L-CHR-S1 (Reservation).** Use **Characteristic** **only** for variables that **declare a CSLC scale** (nominal, ordinal, interval, or ratio) with admissible values, units, and polarity (Part C.16 and A.17–A.18).
**Rule L-CHR-S2 (USM).** `U.Scope`, `U.ClaimScope (G)`, and `U.WorkScope` are **USM scope objects**, not Characteristics, and do not appear in a `CharacteristicSpace`.
**Rule L-CHR-S3 (Status).** Episteme statuses, `SystemRoleAssignmentStateRelation` occurrences or assertions, deontic statuses, and epistemic statuses are not Characteristics by label alone; each remains governed by its direct pattern.
**Rule L-CHR-S4 (Lexical classifiers).** Keep a lexical classifier or tag under its classification rule: a local classification function and value set, source wording, C.29 representation element, example or alternative set, status or state-frame value set, local kind or classifier, or another construction defined for that classifier. Call it a `U.Characteristic` only when that characteristic and one CSLC scale are declared. Do not default the residue to `Facet`, attribute, or another umbrella kind.
**Checks.**
— **CC-L-CHR-1.** `scope characteristic(s)` is banned in Kernel and local-use Tech wording.
— **CC-L-CHR-2.** `CharacteristicSpace` near `Scope` — error.
— **CC-L-CHR-3.** Kind-preserving repair: `F–G–R characteristics` → `F–G–R components` only when the recovered kind is component rather than characteristic.

#### E.10:8.10 - LEX-QA-1 - Using terms with the `-ility` and `-ilities` suffixes

**Rule.** Tokens ending with **-ility** or **-ilities** or widely used quality names (**Availability, Reliability, Security, Safety, Scalability, Maintainability, Usability**, …) are **Quality‑Family labels**, not automatically CHR **Characteristics**.

**Authoring choice:**
— To use such a term as a **CHR** characteristic, **bind** it to a **named `U.Characteristic` with one CSLC Scale** (A.18) and refer to that Characteristic in guards and UTS;
— Otherwise **publish a Q‑Bundle** (see **C.25**) that includes named **Measures (CHR)** for the selected measurable Characteristics and, where relevant, **Scope** (USM set over `U.ContextSlice`) plus window, mechanism, and status fields.

**Rationale.** Scope is **set-valued** (USM) and **not** a CHR measurement. Q-Bundle mechanism and status fields carry mechanism references, control presences, certification states, or other status values admitted by their specific patterns; they are not generic governance records or measurements. Claim scope, work scope, CHR measures, qualification window, mechanisms, status values, and evidence keep their own kinds even when one Q-Bundle authoring structure coordinates them. (A.2.6 § 6.2; A.6.1; C.16, A.18, and C.25).

### E.10:9 - Ontology recovery rows for overloaded words (LEX L-rules; normative)

> **What this section does.** LEX L-rules standardise **how we recover kind and use** in Core and local uses when overloaded everyday words hide FPF concepts.
> **What this section does not do.** It does **not** restate naming (see **§ 7 MG-DA**) or morphology, casing, and suffix rules (see **§ 8 LEX.Morph**); it **depends** on them.
> **Guards.** Tokens are classified by **`LEX.TokenClass ∈ {KernelToken, ContextToken, DiscriminatorToken}`** (§ 7.1). Only **CHR:ReferencePlane** may use the bare word *plane*. E.10.D2 keeps the EntityOfConcern, an episteme that describes it, and specification use of that episteme distinct; specification use needs a granting gate named by value. Publication faces, publication forms, `PublicationUnit`s, carriers, and renderings stay separate. An enumeration becomes a CHR construction only when it names a `U.Characteristic` with one declared CSLC scale. Without that declaration, recover the exact construction instead of defaulting to a non-measurable attribute: it may be source wording, a C.29 field or other representation element, an example set, unresolved alternatives, a status or state-frame value set, a local kind or classifier, or another value whose kind and definition are already known. It becomes an A.6.5 `SlotSpec` only inside one exact reusable `RelationSignature`.

#### E.10:9.1 - Hard bans and ontology recovery rows (single table; normative)

> **Use this table as a recovery guide.** “Ban” means the listed phrase is not accepted as an unexplained Tech term in Core prose, identifiers, or diagrams. It may remain as ordinary, quoted, or source-local wording when its use is clear; otherwise name the recovered value or relation. EntityOfConcern and Description-episteme boundaries, specification-use gates, and token gates prevent object, description, specification-use, publication-position, and TokenClass leaks (cf. § 8.1).

| **L‑rule**   | **Ambiguous or low-precision word (Ban)**                  | **Canonical FPF target(s)**                                                                                                                                                                     | **EntityOfConcern and Description-episteme boundary and specification-use gate**                                                                       | **TokenClass gate**                         | **Notes**                                                                                            |
| ------------ | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| **L-PROC** | *process*, *practice*, *procedure*, *workflow*, *activity*, a process-like function step, or method-structure wording | First decide what the sentence is about. Use `A.3.4.P` for a change situation and `U.Method` for one way of doing. Name composition, substitution, iteration, fallback, selection, family membership, or another method-side relation under the rule that defines it. Only when a named use depends on how several such relations are organized should the practitioner use A.22's criterion to select a structure, locally called `MethodRelationStructure`. Use `U.MethodDescription` only for an episteme whose EntityOfConcern is one admitted Method and whose claims substantially describe how to perform it. Keep a planning cue or schedule representation as such until A.15.2 admits a `U.WorkPlan`; use `U.Work` only for dated performance, and a separate episteme for its record. After `E.10.ROLE`, recover a local system-role kind and classification, an obtaining `U.SystemRoleAssignment`, or an A.2.7 relation only when work-facing wording actually states it. Other branches include an A.1.1 `BoundedModelUseStructure` when model-use organization changes the answer, an exact source, practice, scope, situation, discipline or cultural-evolution use, `U.Transformation`, `TransformationFlowStructure`, and C.29 notation. | Method, direct method-side relation, optional A.22-selected method relation structure, one-method Description episteme, other subject-description episteme, planning cue or WorkPlan, Work occurrence or Work record, system-role kind and classification, assignment, relation among system-role kinds, model-use structure, source or practice boundary, discipline or source label, Transformation or transformation-flow structure, or selected lens | `KernelToken` for admitted kinds; `ContextToken` for admitted local-use designations, occurrences, and records; lens or register when representation is current | A phrase such as “industrial process as line role” first uses `E.10.ROLE`; it creates neither a system nor a `...SystemRole` kind. Chemistry enters `U.Transformation`, `U.Dynamics`, or Method only after the claim is recovered. *Practice* is not a root kind, and procedural, planning, or document form establishes neither `U.Method`, `U.MethodDescription`, nor `U.WorkPlan`. |
| **L-FUNC** | *function*, *functional*, *functionality*, *effect* | Apply `A.6.F` first when kind or relation is hidden. Possible recovered values include `U.Capability`, `U.PromiseContent`, `U.Method`, one dated Work occurrence admitted under `U.Work`, mathematical function or operator under `C.29`, and functional-architecture or architecture-to-`TransformationFlowStructure` relation under `C.30`, `C.30.ASV`, or `C.30.TFS-REL`. | EntityOfConcern side for Capability, PromiseContent, Method, Work occurrence, mathematical object, architecture relation, or transformation-flow relation; any record about Work remains a separate Description episteme | `KernelToken` or `ContextToken` according to the recovered value and use | Never use *function* as a Core kind name or as default architecture meaning. |
| **L-SERV** | *service* or access-like wording used for provision, a team, software process, deployed component, endpoint, application, host, cluster, access point, offering, ticket, case, Method, or Work | Apply this row only when relied-on FPF wording hides the concrete subject, participant, predicate, kind, permission, Work occurrence, or next question. Bare *service* has no default system reading: ordinary wording may name service-provision Work, a Method, PromiseContent, participation, or another direct claim, while software wording may be metonymic for a process, deployed component, endpoint, application, host, or cluster. Apply E.10 and `A.6.P:4.11a` to recover the hidden choice. Quoted, historical, illustrative, or harmless prose remains outside. | Carry the original wording and relied-on use into A.6.P:4.11a. The recovered object and relation establish what the claim is about; the applicable pattern supplies any EntityOfConcern/Description-episteme boundary or specification-use gate. Use `A.1.SCR` only after A.6.P has named a bearer claim and the decision depends on systemhood; E.10 supplies neither classification nor a new kind. | Keep the source token's register and class until the claim is recovered; no TokenClass choice admits a kind. | Ask what *stopped*, what is *provided*, *how* it is provided, or which bearer must be *restarted*. Do not normalize *service* to server/system, Method, Work, PromiseContent, permission, or fulfilment. If the concrete subject, relation, or dependent use still cannot be named, stop the relied-on use. Record `missing-governor[...]` only after participants, needed predicate sentence, and dependent use are named but no current pattern supplies that predicate. |
| **L-SLA** | *SLA* or *service level agreement* used for an SLO, accountable undertaking, published terms, or a document | Unpack acceptance thresholds into `U.PromiseContent.acceptanceSpec`; accountable obligations or penalties into `U.Commitment`; the packaged SLA through A.6.C into its separate promise, utterance or publication, commitment, Work or consequence, and evidence claims; and published terms into a speech act plus clause episteme. Keep Work, measurement, evidence, and acceptance verdicts separate. | EntityOfConcern side for PromiseContent, Commitment, and any actual Work; episteme side for clauses, specifications, measurements, evidence, records, and verdicts | `KernelToken`, `ContextToken`, or `DiscriminatorToken` according to the recovered value and use | Treat SLA as polysemic shorthand, never one kind or Work record. |
| **L-SCHED** | *schedule*, *plan*, or *calendar* as execution | Keep a schedule, planned window, or calendar as source wording, a planning cue, or a representation until one exact episteme passes A.15.2's present-EntityOfConcern, horizon, `PlanItem`, and substantive-coordination predicate; only then use `U.WorkPlan`. For actual performance, identify one Work individual independently under A.15.1; telemetry, actuals assertions, and run records remain separate epistemes about obtaining facts. | Source or representation until the gate; Description episteme for an admitted WorkPlan and for records versus world-side Work occurrence | `ContextToken` only after the local-use designation or record is admitted | Never infer `U.WorkPlan` from an intent window or schedule label, attach actuals to a plan, treat telemetry as Work, or store actual relations as occurrence fields. |
| **L-ACT** | *activity*, *action*, *task*, or *step* as type | Recover the actual object before choosing the value: one dated `U.Work` occurrence; a separate work-record episteme when only a record is current; `U.Method` only for an independently recovered submethod of a composite Method; a C.29 representation element or claim-content constituent when the step appears only in code, diagram, recipe, or procedure; `U.MethodDescription` only when the claim-bearing episteme has one exact `U.Method` as EntityOfConcern and passes A.3.2; or a planning cue or `PlanItem` inside an admitted `U.WorkPlan`. If only order, fallback, substitution, or dispatch is current, name that direct method-side relation; use an A.22-selected `MethodRelationStructure` only when the receiving use depends on how several such relations are organized. | Work occurrence, record episteme, Method, direct method-side relation, representation or claim-content constituent, MethodDescription, planning content, or optional selected method relation structure | `ContextToken` for an admitted local-use designation, occurrence, or record; otherwise the token class of the recovered value | Reserve *assign* for an exact system-role assignment, *satisfy* for the A.2.5 assignment-state predicate, *perform* for Work, *actuate* for a System, and *approve* for the exact speech-act use. A verb, visible step, or planned-item label defines none of those objects by form. |
| **L‑AGENT** | *agent, actor, or doer* (bare) | Recover the acting entity and admit it as `U.System` only when A.1 passes. Name a local `...SystemRole` kind only when that classification matters, and an assignment only when its declared assignment species and obtaining occurrence are both current. For performed Work, use A.15.1 and F.6 to identify the dated Work, every performer, and assignment. A compact rewrite keeps the Work basis and performers recoverable and may omit only an unused assignment identifier after attribution is established. | Acting entity or admitted system; optional system-role classification; separately current assignment; for performed Work, the Work occurrence and its A.15.1 and F.6 account; separate assertion or description episteme when current | `KernelToken` or `ContextToken` according to the recovered value and use | A title, source or scheme cue, capability, evidence item, or declaration place establishes none of systemhood, classification, assignment, agency, or Work. |
| **L‑OWNER** | *owner of X* | Recover what ownership wording says in this claim. Keep *owner* when an actual architectural, organizational, policy, source-maintenance, responsibility, authority, or commitment relation is current. If the claim is instead a work-facing system classification or assignment, start with `E.10.ROLE` and use A.2 or A.2.1. | Exact ownership or responsibility relation, exact local system-role kind, exact direct assignment species, ordinary wording, or blocker | `ContextToken` only when an admitted local-use designation is actually current | No global owner property; no lexical replacement of a precise architectural owner; no assignment inferred from a title. |
| **L-CAP** | *capability* for assignment, recipe, run, or promise | `U.Capability` means ability within an envelope. Keep an exact system-role kind, direct `U.SystemRoleAssignment` species, `U.Method`, dated `U.Work`, Work record, and `U.PromiseContent` separate under their patterns. | EntityOfConcern side for capability, method, system-role kind, assignment, and Work occurrence; one-method Description episteme only after membership; separate run-record episteme | `KernelToken` or `ContextToken` according to the recovered value and use | A system-role kind or assignment establishes no capability; a recipe form or record establishes neither MethodDescription membership nor Work. |
| **L‑DYN** | *process of diffusion, growth, or learning* | `U.Dynamics` (law or model of change) | EntityOfConcern side | `KernelToken` or `ContextToken` according to the recovered value and use | Reserve for uncaused change models. |
| **L‑EVID** | “paper or dataset proves or ensures” | Recover the evidence-use, source-use, status-use, assurance-use, gate-use, or publication-use relation under `A.10`, `B.3`, `F.10`, `G.6`, `E.17`, `C.28`, or the rule that defines the recovered use relation. Use `U.SystemRoleAssignment` only for a separate exact assignment that currently obtains, whose holder is an admitted system and whose assigned participant is one exact local system-role kind. | Episteme with exact claim target and direct use relation; any system-role assignment remains separate | `ContextToken` or `DiscriminatorToken` according to the recovered value and use | Evidence use is a relation over an episteme and a claim or use; the episteme is not a system-role holder. |
| **L‑CTX** | *context* wording whose action-changing content is hidden | Apply `E.10.D1`; recover the subject-defined value or relation that changes the action—for example, a scheme, scope, model-use boundary, situation, design-time or run-time referent, architecture, environment, domain subject, or local-practice use. | Apply the pattern for the recovered subject and name its EntityOfConcern and any claim-bearing episteme; introduce no generic Context participant or card. | Keep the recovered subject's token class; the spelling *context* selects none. | Keep quoted and ordinary uses, and established uses already defined by a pattern. Rewrite only the use that hides the next action or stop. |
| **L-BRIDGE** | sameness, equivalence, alignment, or mapping inferred from a shared label | Identify the two exact local senses first. If the F.9 predicate is being asserted, address each sense as an exact F.17 `SchemeSenseCell` and apply F.9 only when the direct `Bridge` relation actually obtains; state any bounded use and any A.10 or B.3 reliance separately. | The Bridge relates the two exact cells. A card, row, label, score, or publication is a separate episteme or representation and makes no relation obtain. | Keep each source expression under its effective scheme. | A shared label creates neither a Bridge nor substitution, merge, admission, authorization, or performed use. |

> **Red and Green pattern (example).** ✗ "The **process** ensures quality." → ✓ "`M_quality : U.Method` names the recovered way of doing. `D_quality` is `U.MethodDescription` only because it is a separately identified claim-bearing episteme whose EntityOfConcern is `M_quality` and whose claims state the method's steps and applicability. Evaluate dated **Work** against the applicable acceptance condition, constraint, or commitment."

#### E.10:9.2 - Diagnostic examples, not substitutions

Use these rows as compact diagnostics for common ontology recoveries, not as a replacement table. A proposed repaired sentence is accepted only after the `EntityOfConcern`, head kind, relation or claim kind, admissible use, and scope under repair are recovered and the transformed sentence passes **§ 7 MG-DA**, **§ 8 LEX.Morph**, and the `KindRestorationCheck` from `E.10:10.2`. If the example row would change the kind in the local sentence, split the sentence or leave a blocker; do not copy the example as a ready-made rewrite.

| **Trigger symptom**             | **Recovered ontology example**                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------- |
| “the process owner approves” | Start with `E.10.ROLE` for the title-like wording. If *owner* names an architectural or responsibility relation, keep that relation instead of forcing a system-role reading. State `ApproverSystemRole` separately only when the classification matters. If approval is performed Work, use A.15.1 and F.6 to identify the Work, `ApprovalSystem` as performer, and its assignment; keep the approval speech act, authority, and decision separate. Omit assignment identifiers that the receiving claim does not use. |
| “the document enforces policy” | `Policy_vN` is an episteme used in the gate, constraint, commitment, or evidence relation named by its pattern; it does not act. If enforcement Work is current, use A.15.1 and F.6 to identify the Work, every performer, and assignment. Add `PolicyEnforcementSystemRole` only when that classification matters. A compact rewrite keeps the Work basis and performers recoverable and may omit only an unused assignment identifier after attribution is established. |
| “our service runs nightly jobs” | Apply `L-SERV` and A.6.P:4.11a first. If the sentence means dated service-provision Work performed by a scheduler system, use A.15.1 and F.6 to identify the Work, scheduler, and assignment. Add `SchedulerSystemRole` only when that classification matters. Promise content remains separate. |
| "the API is the service" | Apply `L-SERV` and A.6.P:4.11a. A reusable way of access may be `API_Access_Method : U.Method`; a claim-bearing interface specification is an episteme and becomes `U.MethodDescription` only under A.3.2; an addressable endpoint is a separate bearer; use A.1.SCR for it only when the claim depends on systemhood. Any API publication form/carrier remains separate, and **promise content** states the promised result and acceptance criteria. The source wording chooses none of these by itself. |
| “capability assigned to team Y” | Split the claims. `TeamY` may be an admitted System that has Capability C within envelope E. If the wording also means a work-facing classification, name its local system-role kind; if it means an assignment, name the occurrence with `TeamY` as holder and its declared `U.SystemRoleAssignment` species. Capability, classification, and assignment do not establish one another. |
| “process health green”          | Apply `A.19.SPR`: name the bearer, state frame, value `green`, criteria or evidence, admissible use, and change condition; the color alone does not establish health or acceptance. |
| “function of component A fails” | Apply `A.6.F`. If the recovered claim is behavior performed as Work, use A.15.1 and F.6 to identify that Work, the performer system, and its assignment. Add `ServiceOperatorSystemRole` only when that classification matters. The evaluation result separately records failed acceptance on the cited observations. |
| “context is unclear here” | Apply E.10.D1 and name what changes the interpretation or next action: the exact source and edition, effective scheme, claim scope, model-use structure, working situation, frame, referent, or local practice. If two local senses are compared, identify them; assert an F.9 Bridge only when its direct relation between exact cells actually obtains. |

#### E.10:9.3 - Acceptance tests (LEX‑AC)

A text **passes** LEX if all answers are **Green**:

1. **Action-changing use recovered.** Each use of *context* that changes interpretation or action names the exact source, scheme, scope, model-use structure, situation, frame, referent, or practice that matters. Ordinary, quoted, and already defined uses remain available.
2. **Right EntityOfConcern and Description-episteme boundary and specification use.** EntityOfConcern, Description-episteme, specification-use, publication relation, and run-record uses are not conflated (cf. § 8.1 gates).
3. **Promise, ability, and performance split.** `PromiseContent` (promise clause), `Capability` (ability), `Work` (performance) are not conflated.
4. **No anthropomorphism.** Documents, datasets, and models do not “do”; **Systems** do.
5. **Scheduling hygiene.** No actuals belong in a `U.WorkPlan`. A performed occurrence is dated `U.Work` and points to its complete A.15.1/F.6 basis. Other direct facts, including affected referent, bindings, and resource use, remain separate. A short sentence may omit only an assignment identifier unused by its receiving claim; the underlying occurrence and attribution remain recoverable. An assertion, description, log, or record about the Work is a separate episteme, not the occurrence.
6. **Cross-local relation.** When the text relates two different local senses, it identifies the exact F.17 cells and cites an F.9 Bridge only if that direct relation obtains under the applicable F.9 relation profile. When a receiving use is current, a separate C.2.1 claim says what action is proposed, its use direction, correspondence rule, tolerated loss, and polarity. That claim does not show that the action occurred. Use A.10 or B.3 only when reliance or assurance is actually current. Apply **A.6.9 (RPR-XCTX)** when published wording such as “same”, “equivalent”, “align”, or “map” still hides the relation.
7. **MG-DA ok.** New or refactored tokens pass **§ 7 MG-DA** (anchored head noun; collision check; an enumeration names its closed value set, classified kind, and classification rule; use `U.Characteristic` and `CharacteristicSpace` only when the enumeration is the declared CSLC scale of that exact Characteristic).
8. **Morphology ok.** Suffix, compound, prefix, and casing respect **§ 8 LEX.Morph** (for example, concrete `…SystemRole` kind designations, `MethodDescription`, `Work`, and reserved prefixes); bare `...Role` is not a default Tech form.
9. **Banned tokens absent or recovered.** No *process*, *practice*, *function*, *task*, or *activity* in Kernel senses unless the sentence applies the selected recovery pattern (`A.3.4.P`, `A.6.F`, work patterns, method patterns, `C.36.P`, or another relevant pattern) and names the recovered value by value; no tooling or file suffixes in Kernel tokens.
10. **State gating present (when needed).** Readiness of an assignment to a system role is expressed through `SystemRoleAssignmentStateRelation` plus a separate `SystemRoleAssignmentStateAssertion` when an assertion is needed, not through vague “approved” or “ready” wording.

#### E.10:9.4 - Coordination map (how LEX plugs into the rest of FPF)

* **With E.10.D1 — Recovering What “Context” Means in Use.**
  E10-CTX-1: When *context* changes the statement or next action, recover what supplies the boundary—for example, a value, relation, scope, scheme, situation, or use defined by the relevant pattern.
  E10-CTX-2: For source-local meaning, state the exact source, expression, effective scheme, and local sense. Create F.17 cells when stable addresses are needed; use F.9 only for an obtaining direct Bridge between two exact cells, and keep every proposed use and reliance claim separate.

* **With E.10.D2 (EntityOfConcern and Description-episteme boundary and specification use and refinement discipline).**
  Speak in the **right EntityOfConcern and Description-episteme boundary and specification use**. E10-EOC-DESC-SPEC-1..3 apply: the EntityOfConcern is named directly; Description suffixes name Description-episteme use; Spec suffixes name specification use on a Description episteme; a work assertion or description is a separate `U.Episteme` about one Work individual and is not the occurrence; a state assertion is a separately governed claim about a state and is not that state; an evaluation-result episteme is neither the evaluated object nor an occurrence. Upgrade a Description episteme to specification use only when **checkable acceptance** or another specification-granting gate named by value exists.

* **With E.10.ROLE, A.2, A.2.1, and A.15 (system-role-kind, assignment, Method, and Work alignment).**
  Bare *role* has no default Tech reading. A local system-role kind classifies independently admitted systems; classification, assignment, and Work remain separate. `U.Method` is a way of doing; `U.MethodDescription` is a claim-bearing episteme about one admitted method that passes A.3.2. A performed occurrence is dated `U.Work`; A.15.1 and F.6 identify its Method, time, containing System, every performer, and the assignment under which each acted. A compact account keeps that Work basis and all performers named or recoverable and may omit only an assignment identifier unused by the receiving claim after attribution is established. Assertions, descriptions, logs, and records about the occurrence are separate epistemes.

* **With F‑cluster (Unification) and UTS (F.17).**
  Recover each source-local cell under its effective scheme. A comparison row may cite direct Bridges, losses, contrasts, and separately warranted use claims; the row creates none of them. UTS is the human-readable term publication.

> **Acts and tokens.** LEX applies to **tokens**; USM applies to **acts**: mint, rename, and use. Conformance: `LEX.TokenClass(t)=c ⇒ USM.Scope(usage) ∈ AllowedScopes(c)` (see § 7.5).

#### E.10:9.5 - Conformance checklist (LEX‑CC)

1. **LEX‑CC‑1 (Triggered use, not spelling ban).** A listed word opens repair only when its FPF-governed use hides a kind, relation, claim, or action; quoted, ordinary, and already precise uses remain available.
2. **LEX‑CC‑2 (Context wording).** After `E.10.D1`, each action-changing use of *context* names what supplies the relevant boundary, interpretation, or situation and makes the next action or stop clear.
3. **LEX‑CC‑3 (EntityOfConcern and Description-episteme boundary and specification-use morphology).** Usage passes **§ 8** gates (suffix, prefix, and casing), EntityOfConcern and Description-episteme boundary checks, and specification-use checks.
4. **LEX‑CC‑4 (Bridge).** A positive cross-local relation cites an obtaining direct F.9 Bridge between identified cells; any proposed use and reliance remain separate. Shared spelling alone establishes none of them.
5. **LEX‑CC‑5 (MG-DA).** New tokens pass **MG-DA** tests, including **full‑text collision** and **Reserved‑Names** checks.
6. **LEX‑CC‑6 (Service, acceptance, and evidence).** Service or access wording establishes neither **Work** nor acceptance. An acceptance claim names the selected criterion episteme, any evaluation or acceptance Work that applied it, the returned value or result episteme, and the acceptance predicate with its participants under the applicable acceptance pattern; delivery Work, evidence, or a positive display proves none by itself. Evidence use is a relation over an **Episteme**, target claim or use, scope, polarity, time, and provenance under the evidence pattern.
7. **LEX‑CC‑7 (USM compatibility).** For each LexicalAct, `USM.Scope ∈ AllowedScopes(LEX.TokenClass)`.
8. **LEX-CC-8 (Naming discipline).** If overload cleanup yields one local replacement phrase, the text records the repaired phrase and applicable local repair pattern. If cleanup yields one durable reusable name, the text first records the applicable **F.8** decision for the already identified value, then completes an **F.18** NameCard; public, Core-facing, durable, or cross-local publication also supplies the **F.17** term row. Intuition-first labels, partial NameCards, and naming acts that substitute for value or kind admission are non-conformant.

#### E.10:9.6 - Worked micro‑examples (short, cross‑domain)

**Factory.**
✗ “The **process** failed; the **service** restarted itself.”
✓ The compact strings `PLC_17#ObserverRole:PipelineOps`, `CAB_Chair#ApproverRole:ChangeControl`, and `OpsBot#DeployerRole:CD_Pipeline_v7` remain quoted source cues only. Start with `E.10.ROLE`; they are neither system-role-kind designations nor assignment occurrences.
`PLC_17`, `ChangeControlBoardSystem`, and `OpsBot` are independently admitted systems. Use `ObserverSystemRole`, `ApproverSystemRole`, and `DeployerSystemRole` only where those classifications matter. For each dated Work occurrence attributed to one of them, apply A.15.1 and F.6; omit assignment identifiers that the receiving example does not use. Source suffixes and interpretation epistemes remain separate.
The exact dated Work occurrences, covering assignments, and F.6 attributions remain separate from one another and from the log episteme, approval speech-act content, and fulfillment claim.
**Cloud.**
✗ “The **process owner** approved; the **API service** deployed.”
✓ The source strings `ProductLead#AuthorizerRole:Rollout_2025` and `sCG‑Spec_ci_bot#DeployerRole:CD_Pipeline_v7` remain quoted cues. Recover `ProductLeadershipSystem` and `sCGSpecCIBot` independently; use `AuthorizerSystemRole` and `DeployerSystemRole` only for exact local classification claims.
For `RolloutApprovalWork-F123` and `DeployWork-F123`, apply A.15.1 and F.6 to identify each Work occurrence, performer, and assignment. Omit assignment identifiers that the receiving account does not use. Keep source titles, source or scheme cues, approval content, deployment results, and telemetry separate, and identify each through the rule for that value or relation.
`RESTAccessMethod : U.Method` names the exact API access method; `RESTAccessDescription` is `U.MethodDescription` only if its claim content substantively describes that method as its exact EntityOfConcern, and it is an access Spec only after the named specification-use gate. Any selected description edition is reached through a separate governed `U.EpistemeRef`, while file or carrier version remains separate. `FeatureAccessPromiseContent` states the acceptance condition; telemetry measurements provide evidence for the evaluation that the deployment fulfilled that promise content.

**Research.**
✗ “Dataset X **proves** the theory; the **process** is reproducible.”
✓ `DatasetX` is used in an evidence relation for claim C with model-fit scope, polarity, time, and provenance under `A.10`, `B.3`, `G.6`, `F.10`, or the applicable evidence pattern;
replication is recorded through evidence-use, source-use, status-use, or reproducibility-status relations under their respective patterns;
procedure wording first recovers one exact `U.Method`; a separately identified claim-bearing episteme is `U.MethodDescription` only when that method is its exact EntityOfConcern and its claims pass A.3.2, while re-runs are exact **Work** occurrences only on the A.15.1 basis.

**Semioarchitecture.**
✗ “`projection` has one meaning in routing and bridge prose.”
✓ `A.16` keeps `projection` as a move name for route-bounded partialization; `F.9.1` keeps `projection` as a bridge stance label. If one durable reusable replacement name is really needed, recover the value and use that need a name, record the applicable **F.8** decision, and then use **F.18** plus **F.17** when public publication is current; otherwise retain the source expression or local phrase explicitly rather than flattening both interpretations into one umbrella rewrite.

**Editorial note.**
This section inherits section 7 **MG-DA** (anchored head nouns; enumeration rule gate; `U.Characteristic` and `CharacteristicSpace` only when one named Characteristic has that enumeration as its declared CSLC scale; collision checks) and section 8 **LEX.Morph** (suffix, prefix, and casing). It deliberately omits their details to avoid duplication. The only admitted uses of *plane* in the Core are **CHR:ReferencePlane** and the derived operators **CL^plane** and **Phi_plane**; policy flags do not introduce new planes. To distinguish pre-operational and operational states within **ReferencePlane=world**, use **WorldRegime in {prep | live}** (formerly `PlaneRegime`).

#### E.10:9.7 - Guarded-head cross-reference *(normative lexical caution)*
When one wording head already carries several FPF-governed local interpretations, lexical cleanup should prefer a **guarded-head note** over silent flattening. The note may record that the head remains risky, name the cited texts or patterns that define or constrain the local interpretations, and point readers to the local canonical interpretation in each cited text.

If cleanup reveals that no admissible existing token can carry the needed meaning, use the local repair pattern for one-off wording. If the change needs one durable reusable name, first recover the value and its kind and record the applicable **F.8** decision, then use **F.18** for the NameCard and **F.17** when public, Core-facing, durable, or cross-local publication is current. Do not invent an ad hoc synonym or let naming settle an unresolved object.

This cross-reference is lexical only. It does **not** create a new repair-side definition site, does **not** establish global or cross-local equivalence, and does **not** overrule cited local definitions. It simply keeps overloaded heads from being normalized into one false global interpretation.

`projection` is the main current example: `A.16` keeps it as a move name for route-bounded partialization, while `F.9.1` keeps it as a bridge stance label. E.10 therefore uses deconfliction notes and explicit naming of the cited text that governs each local interpretation, not one umbrella rewrite that erases the distinction.

Bare claim-bearing *role* is another guarded head and has no default Tech reading. Use `E.10.ROLE` to recover the current object or relation; use `SystemRole` only inside a concrete local system-role-kind designation after that kind is independently admitted.

### E.10:10 - Reference routine for turning messy language into E.10-clean prose *(informative)*

> A pragmatic **three-pass** routine. It is subordinate to `E.10:0.2` and is used only when the selected wording problem needs register, naming, morphology, or local rewrite details. It works with plain text, diagrams, or models and uses no special tool.

#### E.10:10.1 - Pass 0 — *Pre‑flight (2 minutes per page)*

0.1 **Name only the local facts that matter here:** the exact source or practice, effective scheme, scope, model-use structure, working situation, frame, or referent when it changes interpretation or action. Do not create a generic Context card.
0.2 For every new or renamed token, **declare `LEX.TokenClass`** ∈ {KernelToken, ContextToken, DiscriminatorToken}.
0.3 Apply the **MG-DA pre-check** (anchored head noun; no metaphor heads; if an enumeration is current, name its closed value set, classified kind, and classification rule; declare a `CharacteristicSpace` only when the enumeration is the declared CSLC scale of one named `U.Characteristic`).
0.4 Perform **collision and uniqueness** checking: full-text grep plus Reserved-Names registry (see § 7). If collides -> rename or DRR deprecate.

#### E.10:10.2 - Pass 1 — *Inspect the selected span*

1.1 **Underline overloaded words** (*process, service, function, workflow, ticket, approval, spec, plan,* …).
1.2 For each, write a **one‑line intent** in Plain register (what FPF kind or relation is meant).
1.3 Mark shared labels whose local senses may differ; do not infer a relation from the label.

#### E.10:10.3 - Pass 2 — *Recover Core anchors (not substitution)*

Pass 2 is not a lexical replacement table. For each underlined word or phrase, first write one Plain-register sentence saying what the text is trying to assert or ask. Select the applicable `E.10:0.0a` branch when the use is relation-like; otherwise name the concrete object, applicable rule, admissible use, and scope. Compare the same object and claim before and after repair, then choose one disposition: keep with a guarded-head note, split into several kinds named by value, rewrite locally, record a durable naming case under `F.18`, apply the relevant pattern, or leave blocking. Name an exact predicate, assertion, `ClaimGraph`, Method, actor, assignment, or Work only when the current claim or a named later use depends on that identity. This proportional naming rule does not make a covering assignment or F.6 fact optional once performed Work is admitted. A replacement phrase is admissible only when it remains recoverable and introduces no umbrella flattening, semantic narrowing, accidental widening, declaration-participant collapse, representation-as-obtaining, or slot-as-kind substitution.

2.1 Recover underlined words through **§ 9 L‑rules** table:
 • recipe -> the exact **`U.Method`** when the wording denotes one way of doing; **`U.MethodDescription`** only for a separately identified claim-bearing episteme whose exact EntityOfConcern is that admitted method and whose claims pass A.3.2; otherwise a C.29 representation, publication form, source wording, or ordinary wording under its applicable rule
 • planned work window or dated occurrence -> a planning cue, schedule representation, or `PlanItem` content until one exact episteme passes A.15.2's present-EntityOfConcern, horizon, `PlanItem`, and substantive-coordination predicate; only then **`U.WorkPlan`**. A dated performed individual is independently admitted as a **Work occurrence under `U.Work`** only on the A.15.1 basis
 • promise -> **`U.PromiseContent`**
 • ability -> **`U.Capability`**
 • For actor or doer wording, identify the entity that acts; admit it as **`U.System`** only when A.1 passes. When performed Work is current, use A.15.1 and F.6 to identify the dated Work, performer, and assignment. Use a `...SystemRole` designation only when that classification matters.
 • document or evidence-bearing publication cue → **`Episteme`** used in an evidence-use, source-use, status-use, constraint, commitment, gate, or publication-use relation named by its evidence, source, status, constraint, commitment, gate, or publication pattern
2.2 Apply **LEX.Morph** (§ 8): compound and suffix gates such as concrete `...SystemRole` kind designations, `...Work`, `MethodDescription`, service-description episteme, service-access publication, or service-offer record labels, casing, and reserved prefixes. Bare `...Role` remains a trigger, not an accepted default form.
2.3 Pass **EntityOfConcern and Description-episteme boundary and specification-use** check: name the EntityOfConcern directly; do not type a recipe, procedure, code expression, diagram, ETL label, document form, or relation-structure description as `U.MethodDescription` by appearance. Admit only a claim-bearing episteme whose exact EntityOfConcern is one admitted `U.Method` and whose claims pass A.3.2; use Spec only where a named specification-granting gate is present. Recover actual performed facts as independently obtaining relations involving a Work occurrence, and keep run records as separate epistemes.
2.4 On first use, state the exact source or practice and effective scheme when they change meaning. Add a Tech-and-Plain twin pair in the local glossary only when a one-to-one didactic mapping is useful.
2.5 Perform one local `KindRestorationCheck` for each changed FPF-governed phrase. Write the full form below only when the repair needs a separately inspectable result; otherwise the repaired sentence and its kind-preservation check are enough. Keep any written result with the bounded repair instead of creating a second ledger:
   - `Situation`: quote the sentence and say in ordinary words why the phrase matters to its reader.
   - `Action`: write the intended sentence and select one `E.10:0.0a` branch, another concrete governed object, or explicit ordinary/quoted non-use.
   - `Before/after`: name the governed object, claim, applicable pattern contribution, admissible use, and scope on both sides; add only the distinctions required by the selected branch.
   - `Visible result and stop`: give the accepted wording, concrete result obtained by applying the selected rule, or blocker, plus the nearby case that must not be read into it. Stop when that result lets the reader return to the domain task.

Mark the disposition `preserved`, `split`, `intentionally changed`, or `blocker`. A changed phrase without this check remains an unresolved lexical finding. Cite the concrete pattern for any current relation, declaration, representation, bare-*role* recovery, exact local system-role kind or assignment, Method, Work, evidence, assurance, gate, or decision use, and state what it contributes; `E.10` detects the wording problem and does not replace that ontology.

#### E.10:10.4 - Pass 3 — *Stitch and publish*

3.1 Add **safe rewrites** for any anti‑patterns you found (use § 9.2 quick table).
3.2 If sameness or mapping between two exact local senses is being claimed, identify both senses and create their F.17 cells when stable addresses are needed. Cite an F.9 Bridge only if its direct relation actually obtains under the applicable F.9 relation profile. When a receiving use is current, state a separate C.2.1 claim with the proposed action, use direction, correspondence rule, tolerated loss, and polarity. Use A.10 or B.3 only when reliance or assurance is actually current, and recover any action that occurred under its own pattern. Apply **A.6.9 (RPR-XCTX)** when quoted or imported wording such as “same”, “equivalent”, “align”, or “map” still hides the relation.
3.3 Publish an F.17 row or compact UTS only when readers need a durable term address. State the value it names, effective scheme, source expression, local sense, Tech and Plain designations when both exist, and warnings. The row creates no Bridge, equivalence, use, or reliance.
3.4 Log a short **DRR** when renames or aliases occur (F.13), linking to grep results that motivated the change.

### E.10:11 - E.10 conformance prompts *(normative, concept-only questions)*

> Use these **prompts** during review. They reference § 7 (MG-DA) and § 8 (LEX.Morph) instead of repeating them.

1. **Local-use prompt.** When *context* changes interpretation or the next action, has E.10.D1 recovered the exact source, scheme, scope, model-use structure, situation, frame, referent, or practice that matters?
2. **EntityOfConcern and Description-episteme boundary and specification-use prompt.** Does each sentence use the correct boundary (the EntityOfConcern named directly; Description-episteme use for descriptions; specification use only where a direct gate pattern grants it; run: actuals)?
3. **Token prompt.** For new or renamed tokens, is **`LEX.TokenClass`** declared and consistent with where the token appears?
4. **Head-kind prompt.** Does the head noun name what the phrase is actually about—for example, a Method, Work, Characteristic, Capability, constraint claim, commitment, publication form, service-access relation, service-offer record, interpretation, local kind, `U.Transformation`, `TransformationFlowStructure`, authority use, source or practice boundary, or another exact object? If bare *role* is claim-bearing, use `E.10.ROLE`; a concrete `...SystemRole` compound is admissible only for an exact local system-role kind. A narrowing qualifier alone does not answer this question.
5. **Qualifier-claim prompt.** If an adjective, participle, genitive, or comparative modifier carries a claim being made, comparison criterion, relation, or admissible-use boundary, has that use been restored explicitly rather than left inside the modifier alone?
6. **Direct relation, declaration, designation, and representation prompt.** Can a reader select exactly one `E.10:0.0a` branch from the sentence and point to its visible result? If yes, name the pattern for that branch and preserve only the objects it needs. If no branch fits, state the other governed object or ordinary non-use. If the sentence still mixes branches or only lists possible patterns, rewrite it before applying `E.10.ARCH` or another pattern.
7. **Support interpretation prompt.** If `support`, `supported`, `supporting`, or a support-headed compound appears, keep it unchanged when it is ordinary or quoted wording and no FPF claim relies on it. Otherwise ask whether it already states a direct domain fact. If so, name the things and relation and use the pattern that defines that relation; apply `A.6.P` only when the predicate or a participant is unclear, and `A.6.RCD` only when both are clear but no current pattern defines or constrains the predicate. If it is not a direct relation, choose the matching common alternative in `E.10:0.2`, write the concrete sentence, and use the pattern for that alternative. Thus `Test T supports claim C` reaches `A.10`, `Index I supports readers` can remain bounded reader help, and `Column C supports roof R` reaches a structural relation or a missing-governor result; none is forced into another bucket. For base, anchor, or basedness, apply `A.6.6` and state `dependent`, `base`, `baseRelation`, `scope`, applicable `Γ_time`, witnesses, `admissibleUse`, and `nonAdmissibleUse`. Do not mint `SupportRelation` or ask `A.6.P` to choose among the common alternatives.
8. **Comparison-basis prompt.** If the sentence compares, ranks, escalates, or downgrades something, is the comparison basis ontologically homogeneous after head-kind and qualifier restoration?
9. **Morphology prompt.** Do suffix, compound, prefix, and casing pass **LEX.Morph** gates (for example, concrete `…SystemRole` kind designations, `MethodDescription`, and `Work`), with no default bare-`Role` Tech reading?
10. **Promise, ability, access, and performance split.** Are service promise or acceptance content, service-access relation, **Capability** (ability), and **Work** (performance) distinct and defined by their patterns?
11. **Plan and execution split.** Are planning cues and `U.WorkPlan` kept separate from performed `U.Work`? For each actual Work, do A.15.1 and F.6 identify its Method, time, containing System, performers, and assignments, while affected-referent, binding, resource-use, assertion, and description claims remain separate?
12. **Evidence prompt.** Do documents, epistemes, and publications stay in source-use, evidence-use, specification-use, or publication-use relations? When performed Work is current, is its actor an admitted `U.System`, and do A.15.1 and F.6 identify the Work, performer, and assignment? Does any bare *role* wording first pass `E.10.ROLE` rather than assigning the episteme?
13. **Bridge prompt.** If the text asserts a relation between two local senses, are the exact cells identified, and does the F.9 Bridge actually obtain under its applicable relation profile? When a receiving use is current, does a separate C.2.1 claim state the proposed action, use direction, correspondence rule, tolerated loss, and polarity? Are reliance, assurance, and any action that occurred kept separate and opened only when current?
14. **Collision prompt.** Were full-text and Reserved-Names checks completed, with no other meaning of this token anywhere in FPF?
15. **Naming-procedure prompt.** If one durable reusable name is needed because no admissible existing token carries the needed meaning beyond one local repair, was the governed value settled first, was the applicable **F.8** decision recorded, and were the **F.18** NameCard and any required **F.17** public term row completed rather than picking a label by intuition or filling publication apparatus around an unresolved object?
16. **Value-substitution prompt.** After the repair, can the declared reader still see the remaining admissible reader use, and did the repair preserve usability, affordability, semantic composability, fit with the rule governing the claim, and local action guidance? If not, narrow the repair, keep ordinary wording with a recovery note naming the recovered kind and use, or leave the issue blocking instead of optimizing for lexical purity.

**Working order for precision repair on FPF-governed prose.** Restore the head kind first; a narrowing qualifier such as `comparative`, `safe`, `interactive`, or `reliable` does **not** by itself restore that kind. Then unpack the qualifier claim, then check whether the comparison or escalation basis is homogeneous. Only after that may a later Plain, didactic, or coarsened rendering admissibly relax the sentence, while keeping the more precise upstream interpretation recoverable.

### E.10:12 - Archetypal Grounding - three worked micro-examples - E.10 across domains *(informative)*

#### E.10:12.1 - Healthcare (operating-room planning and work)

**Messy:** “The surgical **process** is scheduled at 08:00; the SOP approves the incision and the **service** documents recovery.”
**E.10-clean rewrite:**
"`OR_Case_221_WorkPlan` is used as `U.WorkPlan` only after A.15.2 membership is established: its already identified present EntityOfConcern is `Patient_221`, its horizon is the bounded surgical-planning interval, and `Incision_221`, a `PlanItem` substantively coordinates the intended surgeon classification and assignment conditions, operating-room resource reservation, planned start of 08:00, `IncisionMethod`, the `U.Method`, and the incision-readiness target. It cites `IncisionMethodDescription`, a separately identified claim-bearing episteme. That episteme is `U.MethodDescription` only because the method is its exact EntityOfConcern and its claims substantively describe how the method is carried out. Any edition identity needed by the plan is selected through a separate `U.EpistemeRef` whose subject pattern supplies its rule; carrier version remains separate.
`SOP_OR_v4` is used as a specification-use episteme for the incision-readiness constraint; it does not approve the incision. Source title `QA_Officer` does not identify the performer. For `ApprovalSpeechActWork-221`, apply A.15.1 and F.6 to identify `QAApprovalSystem` as performer and the assignment under which it acted. Add `ApproverSystemRole` only when that classification matters. Approval speech-act content and the resulting `GateDecision` remain separate, and that decision admits the planned run.
`PostOpMonitoringPromiseContent` states the promised monitoring and its vitals acceptance envelope. `WardAccessMethod : U.Method` names the exact access method; `WardProtocol` is `U.MethodDescription` only if it is a separately identified claim-bearing episteme about that method and passes A.3.2, while its publication form and carrier remain separate."

#### E.10:12.2 - Manufacturing (assembly line)

**Messy:** “The welding **function** provides air‑tight seams; the **process** costs 3 min.”
**E.10-clean rewrite:**
“`Robot_SN789` has **Capability** ‘execute `Weld_MIG_v3` within envelope E at measures M’.
For one run, `Robot_SN789` is admitted as a system and performs `WeldWork-SN789-4711`; A.15.1 and F.6 identify its time, Method, containing System, and assignment. Add `WelderSystemRole` only when that classification matters. Each bounded change of the workpiece joint is identified under A.3.4 before stating a work-to-change fact. If the Work first constitutes a distinct seam entity, `A.15.PROD` supplies its identity specification and inception boundary. Measurement-result epistemes remain separate evidence for acceptance and duration claims.
Treat source string `WeldingCellContext` as a quoted recovery cue. If it changes the claim, recover the exact source edition, plant practice, effective scheme, scope, or working situation that it denotes. Any assignment interval is described outside the four participant designations.”

#### E.10:12.3 - Cloud and SRE (production deployment and work)

**Messy:** “The storage **service** wrote logs and the deployment **process** failed after 2 min.”
**E.10-clean rewrite:**
“Source string `sCG‑Spec_ci_bot#DeployerRole:CD_v7` is a quoted recovery cue, not a performer or assignment. `sCGSpecCIBot` performs `DeployWork-r4711`; A.15.1 and F.6 identify its time, Method, containing System, and assignment. Use `DeployerSystemRole` only when that classification matters. The Work failed at T+120 s. Recover source `CD_v7` separately.
`ObjectStoragePromiseContent` states durability and availability targets; `S3_API_Spec_vX` describes the access method.
`LogWriterSystem` performs `LogWritingWork-r4711`; A.15.1 and F.6 identify its time, Method, containing System, and assignment. Use `TransformerSystemRole` only when that classification matters. The service promise remains separate and does not act.”

### E.10:13 - Bias-Annotation
Lenses tested: **Gov**, **Arch**, **Onto/Epist**, **Prag**, **Did**. Scope: FPF-governed wording-use repair; ordinary ungoverned language remains outside this pattern.

| Bias | How E.10 prevents it |
| --- | --- |
| Lexical-substitution bias | E.10 starts with trigger scan and governed-object recovery, not synonym replacement. |
| Umbrella-to-umbrella bias | Broad heads such as support, basis, route, status, force, object, record, and posture are unpacked into the governed object, relation, bearer, value set, predicate or ordinary claim, admissible use, and blocked overread. Add an exact assertion, `ClaimGraph`, or pattern reference only when that identity changes truth, action, comparison, publication, reuse, or reliance. |
| Semio-bias | Wording-use repair does not displace the EntityOfConcern; descriptions, publications, and source-use relations stay separate from the object or claim under concern. |
| Pattern-as-actor bias | Patterns supply rules or guidance; they do not write, decide, authorize, send, or repair project objects. |
| Source-provenance-as-prose bias | Source wording can be quoted or bounded as source-only, but live FPF prose states the current norm rather than narrating where a term came from. |

### E.10:14 - Conformance Checklist

Use this checklist for the accepted wording span, not for the whole corpus by reflex.

1. **Bounded span named.** The exact sentence, row, section, pattern, or project text under repair is recoverable.
2. **Trigger and use separated.** The trigger word is identified, and the FPF-governed use carried by that word is stated separately from the word itself.
3. **Plain result and applicable pattern recovered.** The repaired wording states the ordinary sentence or action first, selects one `E.10:0.0a` branch when the use is relation-like, and names that result's pattern and admissible use. A different governed object, source-use relation, explicit non-use, or blocker is named instead when no branch applies.
4. **Applicable rule identified.** If the issue is no longer lexical, name the pattern or precision-restoration realization pattern and its concrete contribution.
5. **The four relation-like branches remain distinct.** An obtaining world-side relation is not its reusable declaration, a report that claims it, or a field, table, graph, or formula that represents it. A declaration position, participant designation, label, or representation place creates no actual participant, obtaining relation, or new U-kind by itself.
6. **Math lens kept separate from ontology.** Graphs, tuples, algebras, spaces, mappings, and similar mathematical expressions are used as mathematical lenses only when that is the current claim.
7. **Final wording closes the local wording-use case.** The result is accepted wording, direct pattern use, controlled precision reduction, quote-only use, reduced-use cue, blocked use, incomplete rewrite, ordinary prose, or not-triggered disposition.
8. **No umbrella replacement.** The repair does not replace one broad head with another broad head such as `basis`, `support`, `route`, `path`, `status`, `record`, `object`, `role`, `method`, `mechanism`, `flow`, or `structure` without the recovered object and relation.
9. **Reader use remains visible.** The user can still see what to do next with the project object, relation, source, evidence, publication, method, work, architecture, characteristic, or other EntityOfConcern that made the wording important.
10. **Work/method boundary words close through a governor.** `input`, `raw material`, `source data`, `source material`, `output`, `result`, `outcome`, `deliverable`, `handoff`, and work-name wording either retain an already exact direct pattern use or produce one `A.6.P.WMR` result family. Classification, a generic result relation, method-description filling, or a designation that merely type-checks against an A.6.5 `SlotSpec` is not closure.


### E.10:15 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Correction |
| --- | --- | --- |
| Replace one umbrella with another | `support` becomes `basis`, `route` becomes `path`, or `posture` becomes `status` without recovering the kind. | Write the ordinary domain sentence, select one `E.10:0.0a` branch when relation-like, and name only the applicable pattern contribution and admissible use. If no branch or other governed object can be selected, keep ordinary wording or leave the repair blocked. |
| Pattern does the work | A pattern is said to send, route, approve, authorize, or repair a project object. | Name the person or system that acts and the action it performs. If the sentence is instead about a resulting fact, declaration, report, or representation, use the matching `E.10:0.0a` branch and its pattern. The pattern supplies guidance or a rule; it does not act. |
| Description becomes object | A description, diagram, publication face, source span, or dashboard is treated as the in-life object or authority. | Use A.7, C.2.1, E.17, publication patterns, and the pattern for the claim being made. |
| Source label becomes FPF kind | A quoted term, acronym, legacy label, or local handle is kept as a live kind. | Treat it as source wording until the FPF kind or relation is recovered. |

### E.10:16 - Consequences

Positive consequences:

- Wording repair becomes ontology-first precision restoration rather than taste-based editing.
- New names, field names, and pattern prose stay composable with FPF kinds, slot discipline, and the patterns that define their claims.
- FPF can admit ordinary prose, source quotations, and local names without letting them become hidden ontology.

Costs:

- A quick lexical replacement often becomes a short ontological check.
- Some attractive phrases remain blocked until the relevant rule, relation, bearer, value set, or admissible use is named.
- Broad source wording sometimes needs a precision-restoration pattern rather than a one-word replacement.

### E.10:17 - Rationale

Wording mistakes in FPF usually matter because they hide an ontology choice, relation and participants, declaration slot, participant designation, representation correspondence, source-use relation, admissible-use boundary, or applicable pattern. A synonym replacement can make the sentence smoother while changing the claim. `E.10` therefore starts with a cheap trigger scan; the practitioner then uses only the smallest pattern contribution needed for the recovered object.

The lexical rule content stays deliberately limited. It is not the ontology for evidence, assurance, work, gate, decision, publication, architecture, characteristic, temporal, role, method, mathematical-lens, or source-use claims. It only prevents wording from smuggling those claims in under broad heads. Once the recovered object or relation is visible, apply the relevant pattern or continue the ordinary task. Name an exact subject assertion or `ClaimGraph` only when truth, action, comparison, publication, reuse, or reliance depends on that identity; a PatternID may remain an ordinary citation. The fuller form `System S used Method M while performing Work W` remains correct when actor, Method, and Work identity are themselves part of the claim, but it is not the default paraphrase of `apply pattern P`.

The conformance prompts are bounded so lexical governance does not become a corpus-wide purity ritual. A local repair should restore composability, reader action, and admissible use; when it cannot do that, the honest result is quote-only use, reduced-use cue, blocked use, or an incomplete rewrite rather than a more polished umbrella word.


### E.10:18 - SoTA-Echoing - lexical governance

E.10 lexical governance is not a private FPF style preference. It is a compact authoring discipline for communication, comprehension, term formation, discoverability, and error prevention. These external practice rows are admitted only where they change what an author or reviewer does in a wording repair.

| Practice source | Use of source and source-currentness claim | What E.10 adopts | What E.10 rejects |
| --- | --- | --- | --- |
| Current FPF precision-restoration pattern-set edition used here on 2026-07-20, especially `A.6.P`, `A.6.RCD`, `C.2.P`, `E.24.CD`, `E.24.PUB`, `F.18`, and `F.19`. | Current problem-solving basis for FPF wording repair: `A.6.P` recovers participants and tests an existing direct relation; `A.6.RCD` handles only the residual relation-bearing claim. Each other named pattern contributes only its kind, relation, publication boundary, naming use, or phrase repair. | Mutates the `E.10:0.2` relation-like recovery rows, the `E.10:0.2e` trigger-concordance mechanism, the `E.10:0.3` relational-restoration disposition, and `E.10:22` Relations: after exact participants and direct-relation failure, an `A.6.RCD` application records only the applicable disposition-2 claim, disposition-3 definition with its conditional derived-candidate continuation, or disposition-4 primitive candidate; `E.24` and `E.24.UK` retain admission, and `A.6.0` remains post-admission. | Do not turn E.10 into a second relation, episteme, publication, ontic, or naming ontology; do not copy the neighboring patterns' apparatus into every wording repair. |
| Zhu, Reinecke, and Mitra, `Language Scent: Exploring Cross-Language Information Navigation`, arXiv:2604.03604, 2026. | Current preprint extending information-scent work to cross-language navigation; its formative and laboratory evidence is promising but small and does not establish universal label equivalence. | Mutates `E.10:0.2b`, `E.10:8.5a`, and F.17 coordination: admit compact in-situ entry cues when they preserve the named value and help a reader choose the right local interpretation; when a claim relates two local senses, identify them and use F.9 only if its direct Bridge predicate actually obtains. | Do not infer global synonyms, a universal multilingual term registry, or cross-local equivalence from similar labels or a small study. |
| W3C SKOS Reference for controlled structured vocabularies and lexical labels, with heavier OWL and RDF ontology practice used only by ontology-bearing patterns named by value. | Current reference source for controlled-vocabulary publication and label relations; not current-best source for every FPF wording repair. | Mutates `E.10:0.2b`, `E.10:0.2c.18`, and `E.10:0.2c.28`: keep vocabulary labels, concept-like heads, registries, maps, and reusable names recoverable as publication or naming objects named by value before reuse; F.18 defines durable naming, while relation, source, or domain ontology remains with the pattern that defines or constrains that claim. | Do not make OWL-style term-to-class modeling the default answer to every vague term. Do not let a controlled vocabulary become a second FPF ontology or replacement wording-recognition table. |
| W3C WCAG 2.2 headings and labels guidance plus consistent-identification guidance, with FPF-internal `E.11`, README, ToC, and `I.2` entry-distribution practice. | Current reference source for discoverability and label consistency; FPF entry projection remains the governing local architecture. | Mutates `E.10:0.2b`, `E.10:0.2c.29`, `E.10:19`, and `E.11` coordination: keep trigger wording discoverable enough for first repair, but make final wording, appropriate pattern use, and entry projection govern the result. | Do not turn wording-recognition lists into local lexical registries, front-door taxonomies, or accepted replacement vocabulary. Do not let search convenience select ontology. |

The practical result is simple: lexical governance improves action guidance and semantic composability instead of becoming language-police work. A SoTA row that does not change a rewrite, an inadmissible shortcut, an appropriate pattern use, a conformance prompt, or a reopen cue remains decorative and does not carry E.10. Reopen these source-use decisions when a named FPF precision-restoration pattern changes its kind or authority boundary, stronger language-scent evidence overturns the usefulness of in-situ cues, or a reference practice no longer supports the publication or discoverability use assigned to it.

### E.10:19 - E.10 regression cues *(concept-only “diff” triggers)*

Re-review your prose when any of these happen:

* **A source edition, effective scheme, or local meaning changes** → re-affirm any Tech-and-Plain twin mapping and first-use gloss; recheck an F.9 Bridge, use claim, reliance claim, or acceptance wording only when that exact changed value participates.
* **A system-role-kind or other kind name grows** (“and”, “plus”, or “--”) -> apply MG-DA: recover the one kind, explicit alternatives, relation, or bundle before renaming. Bare *role* first uses `E.10.ROLE`.
* **A slash, `and`, `plus`, `&`, or similar grouping mark appears in FPF-governed wording** -> classify the span before editing the mark. The trigger is the FPF-governed grouping use, not the character itself: LLM output, review text, intake notes, or draft prose often uses a slash as an unresolved alternative, an untyped bundle, or an attempt to point at a hidden kind. If the grouped words are claim-bearing heads, relation heads, kind candidates, an unresolved alternative, or an attempt to point at a hidden kind, apply MG-DA, `A.6.P`, or the selected restoration pattern: split, bundle, or recover the relation named by value and admissible use. If the mark is part of accepted notation or a conventional designation such as a source name, discipline abbreviation, established compound name, formula, ratio, fraction, unit, path-like quoted source token, title, product name, or URL, keep the notation and classify its use; do not rewrite `1/2` or similar conventional forms merely to remove the mark.
* **A “service” statement broadens scope** → use L-SERV and A.6.P:4.11a to recover the hidden subject, relation, and receiving use. Update only that recovered claim; do not apply a fixed reading list or rewrite every nearby service-related claim.
* **Recipes gain or lose steps** -> first recover the exact `U.Method`, the claim-bearing episteme, and the changed claim. Update **`U.MethodDescription`** only when that episteme has the method as its exact EntityOfConcern and passes A.3.2; a code, diagram, recipe, procedure, or document-form change remains under the pattern for that representation or publication unless claim content actually changes. Never move the change into service labels or system-role-kind names.
* **Evidence verbs creep into actor sentences** → re-apply L-rules (documents do not act).
* **A generic head or support-headed compound acquires an FPF claim or admissible use** (`comparative`, `safe`, `interactive`, `reliable`, `support`, `supported`, `supporting`, `support-looking`, and similar modifiers or heads) → restore the head kind first; then decide whether `support` states a direct subject relation or one of the common lexical alternatives, and route it as `E.10:0.2` requires before broader publication.
* **Wording about a way of doing or one of its neighboring objects changes**—for example, wording with *method*, *practice*, *technique*, *algorithm*, *program*, *proof*, *solver*, *workflow*, *process*, *procedure*, *access path*, *query plan*, *control strategy*, *method algebra*, *method graph*, or *selector calculus* → recover the method-side object or relation before rewriting. The result may be `U.Method`; an exact composition, substitution, iteration, fallback, selection, family-membership, or other direct method-side relation; an A.22-selected `MethodRelationStructure` only when a named use depends on their organization; `U.MethodDescription`; formal-substrate declaration; C.29 mathematical-lens use and correspondence; `U.Mechanism`; `U.WorkPlan`; one dated Work occurrence admitted under `U.Work`; a separate episteme about it; exact system-role assignment or relation among system-role kinds; A.1.1 `BoundedModelUseStructure`; an exact source, practice, scope, situation, discipline, or cultural-evolution label; method-family registry or selector outcome; evidence relation; or quote-only source wording. Do not replace one umbrella with another.
* **A declarative representation starts to sound imperative** (graph path, path slice, evidence-path wording, query, predicate, table, dashboard, publication face, mathematical representation, method-description representation, source-chain relation, carrier path, or FPF pattern relation `runs`, `routes`, `calls`, `dispatches`, `authorizes`, or `flows` without a recovered kind) → apply `C.2.P.DR` or the concrete pattern such as `E.18`, `A.10`, `A.19.SPR`, `E.17`, `C.29`, `A.3.1`, `A.3.2`, `A.15.2`, `A.15.1`, `E.8`, or `F.19`.
* **New token minted** → ensure `LEX.TokenClass` is declared and perform collision checks. If an enumeration is current, name its closed value set, classified kind, and classification rule; add a `CharacteristicSpace` only when the enumeration is the declared CSLC scale of one named `U.Characteristic`.
* **Suffix drift** (e.g., `…Work` on a plan) → fix via **LEX.Morph**.
* **A label is reused across local sources, practices, or schemes** → recover each local meaning. Keep them distinct unless an F.9 Bridge actually obtains between exact cells; state any proposed use and reliance separately.
* **A guarded head needs a new label** → prefer a guarded-head note first; if no admissible existing token remains for one durable reusable name, settle the value and its use, record the applicable **F.8** decision, and use **F.18** plus an **F.17** row when public publication is current.

### E.10:20 - Teaching deck — the E.10 quick card

> **Say it cleanly, once (memorise):**
> A **system role** is one exact local kind for entities already admitted under A.1 as `U.System`. C.3 recovers it through the candidate domain, operative work-facing membership condition, member/non-member boundary, and continuity rule; source or practice provenance only locates the definition. A person, team, organization, or non-human technical object may qualify. A **system-role assignment** is one exact occurrence under `U.SystemRoleAssignment`. Bare *role* identifies neither and has no default Tech reading. **Method** = one admitted way of doing - **MethodDescription** = one claim-bearing episteme about that exact method with at least one substantive way-of-doing claim - **`U.Work`** = admitted kind - **one Work individual** = one world-side dated occurrence admitted under it - **work assertion, description, log, or record** = a separate `U.Episteme`; occurrence facts obtain through their direct relations.
> **Capability** = can-do within bounds (envelope + measures) - service or access wording = recover the subject or relation through L-SERV and A.6.P:4.11a, then use the pattern for that recovered claim; no default service bundle
> **EntityOfConcern and Description-episteme boundary separates the EntityOfConcern from Description epistemes; specification use is a gated use of a Description episteme**; **publication faces, forms, units, and carriers do not act**. Source-local meaning is stated under the exact source or practice and effective scheme. An F.9 Bridge is asserted only for an actual relation between identified cells under the applicable F.9 relation profile. When a receiving use is current, a separate C.2.1 claim states the proposed action, use direction, correspondence rule, tolerated loss, and polarity; reliance, assurance, and any action that occurred remain separate.

**Name forms (allowed morphology):**
* **System-role kinds and other local kinds:** use `<Noun>SystemRole` only for a local system-role kind admitted under A.2 and C.3, and `<Noun><Kind>` for another local kind (`IncidentCommanderSystemRole`, `ShiftOperatorSystemRole`, `WorkItemKind`). Standards, evidence, requirements, statuses, relation participants, declaration places, and representation positions do not become system roles by suffix.
• **Statuses:** name them only under the exact state or status pattern (`ApprovedStatus` when that pattern admits it); a status is not a system-role kind and is not enactable by label.
• **No suitcase nouns:** avoid `and`, `plus`, and `&` in names; recover one kind, explicit alternatives, relation, or bundle instead of creating a composite system-role-kind name.
• **Acronyms:** first expansion + register; short‑form registered per **§ 7.7**.

### E.10:21 - Closing notes *(governance and purity)*

* **Notation-agnostic.** `E.10` is a wording-use governance pattern, not a scanner or template. Apply it in prose, sketches, or formal models.
* **Where checks belong.** Convenience checks belong to Tooling; `E.10` itself stays notation-agnostic. Conformance code belongs in **SCR-LEX** or **RSCR-LEX** as referenced above.
* **Acts and tokens.** LEX applies to **tokens**; USM applies to **acts**: mint, rename, and use. Conformance:
  `LEX.TokenClass(t)=c  ⇒  USM.Scope(usage) ∈ AllowedScopes(c)` (§ 7.5).
* **Guards honoured.** DevOps Lexical Firewall and Unidirectional Dependency remain intact.
* **Reserved “plane”.** Only **`CHR:ReferencePlane`** uses the bare word *plane*. E.10.D2 is the EntityOfConcern and Description-episteme boundary plus specification-use gates, with publication faces, publication forms, `PublicationUnit`s, carriers, and renderings kept separate; all other category talk is expressed as **Characteristics** in a **CharacteristicSpace** when scale semantics are declared.

> **One-line memory:** *“E.10 keeps words honest so ideas stay composable.”*

### E.10:22 - Relations

- **Builds on:** `A.7`, `C.2.1`, `E.17`, `E.24`, `A.6.0`, `A.6.5`, `F.18`, and `F.19` for EntityOfConcern discipline, description and publication separation, ontic discipline, slot discipline, naming, and phrase-level repair.
- **Coordinates with precision-restoration patterns:** `E.10.ARCH`, `E.10.ROLE`, `A.6.P`, `A.6.P.WMR`, `A.6.RCD`, `C.2.P`, `A.19.SPR`, `E.10.MOVE`, and the direct domain restoration pattern applicable to the current trigger; use `A.15.PROD` for local production-work, entity-inception, and production-completion claims when that result family is current.
- **Coordinates with `E.10.D1`:** use it when *context* hides subject-defined content that changes the next action—for example, a scheme, scope, model-use boundary, situation, design-time or run-time referent, architecture, environment, domain subject, or local-practice use.
- **Coordinates with patterns for these objects:** architecture, transformation, Work, evidence, assurance, gate, publication, source use, mathematical lens, Characteristic, temporal claim, exact local system-role kind and classification, `U.SystemRoleAssignment`, Method, and direct relation when those claims are current.
- **Use:** the concrete pattern for the recovered object, relation, evidence, authority, work, publication, or admissible-use claim whenever the issue is no longer wording precision.

### E.10:End

