## C.30.STRAT - Stratification Wording Precision Restoration

> **Type:** Architectural precision-restoration subpattern under `C.30`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Stratification and architecture-operation source-label repair.

**Intent.** Help a reader decide what a source label such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` means in one current sentence. Keep useful local language, but recover the actual object, relation, or claim before relying on it. This pattern introduces no universal kinds for these source labels or for stratification.

**Builds on.** `E.10`, `E.10.ARCH`, `E.8`, `F.19`, `F.18`, `C.30.P`, `A.22`, and `C.30`.

**Coordinates with.** `C.30.ASV`, `C.30.LCA`, `C.30.TFS-REL`, `C.30.ILC`, `A.6.M`, `A.6.F`, `E.18`, `C.16.P`, `C.16`, `A.19.SPR`, `C.2.P`, `E.17`, `C.29`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `A.2`, `G.5`, and `C.11`.

**Result boundary.** A practitioner receives the shortest sentence or note that names the recovered object, relation, or claim, the allowed use, the next action, and the stop or return condition. Include a blocked overread only when it passes F.19's plausible-reader test.

### C.30.STRAT:0 - Use this when

Use this pattern when a source uses a compact architecture or stratification label and that word alone does not tell you what technical claim is being made.

Typical labels are `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, and architecture-operation words such as `block`, `expert`, `cache`, `router`, and `gate`.

**What goes wrong if missed.** A useful local label starts acting as ontology. A `layer` is assumed to be a holon level, control layer, publication layer, scale window, or module boundary without deciding which. A `stack` becomes architecture by name; a `block` becomes a module; an `expert` becomes a system-role kind or performer; a `cache` becomes a state or memory relation; a `router` becomes a decision policy; a `gate` becomes a gate decision. Word shape establishes none of these.

**What this buys.** The reader can keep the source word while making its actual meaning and safe use explicit. Once the object, relation, or claim is clear, use the pattern that defines, constrains, or tests it.

**First useful move.** Copy the sentence and ask: “What does this label name here, what may I infer from it, and what must I do next?” If it is ordinary wording, keep it and stop. If the answer is already clear, use the applicable pattern directly. Otherwise write one line: `label -> recovered meaning; allowed use; next pattern or blocker; stop or return condition`. Do not fill an author-facing E.10.ARCH routing row during ordinary project work. Include a blocked overread only when it passes F.19's plausible-reader test.

**Not this pattern when.** Do not detour through C.30.STRAT when the object, relation, or claim is already clear. Do not use it merely because a familiar word appears. Ordinary source prose with no FPF claim remains ordinary prose or a quotation.

### C.30.STRAT:1 - Problem frame

Architecture and engineering sources use compact labels because they work in local practice. Neural-network prose says `block`, `expert`, `cache`, or `router`; control architecture says `layer`; organizations say `level` or `tier`; documentation says `section`, `stack`, or `view`; scale prose says `level`, `resolution`, or `coarse-graining step`.

These words are good recognition cues but poor stand-alone kinds. The same label can point to a selected structure, module relation, control relation, transformation-flow element, characteristic or scale, publication grouping, state, evidence claim, decision, or nothing beyond ordinary prose.

The repair question is simple: what does the label name in this sentence, what use does the recovered claim support, and which existing pattern supplies the needed definition, constraint, or test?

### C.30.STRAT:2 - Problem

How can FPF keep common stratification and architecture-operation language without turning the words into false root kinds, routing every structure-like phrase through C.30, copying the same trigger catalogue into many patterns, inferring technical claims from word shape, or deleting useful source language before its remaining reader use is clear?

### C.30.STRAT:3 - Forces

| Force | Tension |
| --- | --- |
| Source-language usability vs ontology | Practitioners need compact local words; a technical claim needs the actual object or relation, its participants or bearer, its scope, and its allowed use. |
| Pattern placement vs applicable rule | C.30 placement does not decide the applicable rule: the recovered claim may belong to control, modules, flow, scale, publication, state, evidence, work, or decision. |
| Thin repair vs shadow registry | One shared cue table is useful; copied local trigger lists are not. |
| Known meaning vs detour | When the current object or relation is already clear, use its pattern directly. |
| Precision vs action | A type-correct result is still a failure if the reader cannot see what to do next. |

### C.30.STRAT:4 - Solution

Write the direct local repair first. For example: `Here “gate” names the neural-network path selector; use E.18 to describe the selected path.` That sentence can be the complete result.

When the repair must be compared, handed on, or revisited, retain a compact note:

```text
StratificationSourceLabelRepairNote:
  sourceLabel:
  boundedTextSpan:
  recoveredObjectRelationOrClaim:
  actualParticipantsOrBearer?:
  sourceUseDisposition:
  patternRef?:
  repairedWordingOrDemotion:
  admissibleUse:
  stopOrReturnCondition:
  blockedOverread?:
  remainingReaderUse:
  disposition: direct-pattern-use | local-rewrite | ordinary-source-label |
    quote-only | reduced-use-cue | blocked-use | incomplete-rewrite
```

`groundedOverread?` is an alias for the same optional `blockedOverread?` value, selected through F.19's plausible-reader test.

The note is neither the selected structure nor the relation, claim, publication, or pattern result it points to. Omit it when the direct sentence is enough.

#### C.30.STRAT:4.1 - Recovery sequence

1. **Copy the sentence and label.** Keep enough source context to tell what the sentence is doing.
2. **Try the cheap exits.** If the word carries no FPF claim, keep ordinary prose or quote it and stop. If the source already gives the technical term one clear local meaning, keep that term and use its rule directly. If one local rewrite makes the meaning clear, write it and stop. A controlled vocabulary or preferred-word list is not by itself a reason to replace useful domain language.
3. **Recover plausible meanings.** Treat the label as a designation, not as the object, relation, or claim. If it belongs to a named model, viewpoint, standard, or local vocabulary, recover that source-local convention first. Then ask which object, relation, participants or bearer, claim, scope, time, and source use the sentence could be compressing. Include literal and metonymic readings when both are plausible.
4. **Choose by the recovered meaning.** Use the first matching row in C.30.STRAT:4.2; never choose from the label alone. A standard or model may settle the label inside its declared use, but neither its status nor its popularity extends that meaning to another subject or source.
5. **Open only the needed rule.** Name the actual participants, relation, structure, characteristic, state, publication, evidence, work, decision, or other object that makes the claim true or false. Do not copy every possible field into the result.
6. **Return to ordinary wording.** Write the shortest sentence that preserves the recovered claim and names the next pattern only when its contribution matters.
7. **State the stop.** Give the allowed use, the next action, and the condition for stopping or returning. Include a blocked overread only when it passes F.19's plausible-reader test. If no useful action survives, use quote-only, reduced-use, blocked, or incomplete-rewrite disposition.

#### C.30.STRAT:4.2 - Recovered meanings and patterns to use

| Recovered meaning | Common source labels | What must become clear | Pattern to use |
| --- | --- | --- | --- |
| Control structure | `layer`, `level`, `tier`, sometimes `gate` | The obtaining control relation, what its participants do, any rate band or locality boundary, and a B.2.5 supervisor-subholon relation only when it obtains. | `C.30.LCA`; use B.2.5, dynamics, temporal, evidence, assurance, or gate patterns only for their separate claims. |
| Selected structure or structural view | `layer`, `level`, `stack`, `block`, `view` | The selected, hidden, lost, or preserved structure; view selection; correspondence; source return; an `ArchitectureClaim` when claim content is needed; and a separate `ArchitectureRelation` only when that direct relation obtains. | `A.22`, `C.30`, `C.30.ASV`, or the applicable C.30 subpattern. |
| Module, interface, or substitution | `block`, `cache`, `router`, `expert`, sometimes `layer` or `stack` | Module boundary, interface specification, substitutability relation, variation point, conformance relation, or reliance boundary. | `A.6.M`; stop using C.30.STRAT once that relation is clear. |
| Function or transformation flow | `block`, `expert`, `cache`, `router`, `gate`, sometimes `layer` | Transformation or effect, path selection, graph node, path or crossing, architecture-to-flow relation, or E.18 flow valuation. | `A.6.F`, `E.18`, or `C.30.TFS-REL`. |
| Characteristic, scale, or mathematical lens | `level`, `tier`, `ladder`, `rung`, `layer`, `stack`, `block` | Characteristic and bearer, coordinate or value, scoring method, comparison criterion, scale window, resolution, coarse-graining, preserved or lost structure, lens-use result, and stop condition only where the claim needs them. State separately how the subject is mapped to a scale value; a scale or band does not by itself establish levels in the subject. | `C.16.P`, the applicable characterization pattern, or `C.29`. |
| Episteme, publication, view, or source use | `stack`, `layer`, `section`, `view`, `cache`, `gate` | Description episteme, publication unit, face, form, carrier, source-currentness or source-use relation, source-return condition, or ordinary publication label. | `C.2.P` for a remaining epistemic distinction; otherwise the direct pattern: `C.2.1` for episteme content, `E.17.0` for `U.View` membership, `E.17` for reader-facing publication of an accepted account, `E.24.PUB` for publication availability, or the pattern defining the source-use claim. |
| State, currentness, time, or dynamics | `cache`, `stable`, `level`, `readiness`, sometimes `gate` | Bearer, state frame and values, validity window, currentness relation, dynamics, temporal aspect or rate band, authored temporal-claim adequacy, and reopen condition. | `A.19.SPR` only while the state-family meaning is unresolved; otherwise `A.3.3`, `C.27.TA`, `C.27`, or the applicable state or temporal pattern. |
| Evidence, assurance, gate, work, decision, or causal use | `gate`, `proof`, `safety`, `decision`, `work`, `effect`, or any label used as authority | Evidence path, assurance argument, constraint-validity record, gate decision, Work occurrence, decision record, causal-use record, and any limits imposed by the applicable pattern on that claim. | `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15.1`, `C.11`, `C.28`, or the applicable neighboring pattern. |
| Ordinary source-label non-use | any source label | No FPF claim remains after the sentence is read in context. | No precision-restoration pattern; keep ordinary wording, quote it, reduce its use, or block reliance. |

**When a level claim matters.** When a later decision or design relies on a sentence such as “X is at level L” or “A is above B,” name the subject at stake (the `EntityOfConcern`), what is being ordered, compared, grouped, or mapped, the relation or scale mapping that gives the claim its meaning, when it applies, and whether the sentence asserts, proposes, assumes, or merely illustrates the claim. Apply the same test when `layer`, `tier`, `band`, `scale`, or `stage` carries the stronger claim. A named model or standard may provide this mapping within its declared use; its status does not extend the claim beyond that use. The source word may remain, but these facts—not the label—carry the claim. A list, diagram row, first-then order, carrier section, curriculum, scale label, stage sequence, or coarse-grained description does not establish a subject level by form. If the facts are missing, keep the wording local or illustrative and block reliance on the stronger level claim.

#### C.30.STRAT:4.2a - Same-sentence claim boundary

One sentence may use a source label while making several claims. Split them instead of adding a local catalogue of everything the label does not prove. C.30.STRAT repairs the label; the applicable pattern defines, constrains, or tests each separate claim. The table above lists common destinations, not a mandatory reading list.

#### C.30.STRAT:4.3 - Source-label cue table

| Source label family | Recovery discipline |
| --- | --- |
| `layer` | Do not choose by the word. Test control structure; selected structure or structural view; module or interface; scale or mathematical lens; and publication or source-use meanings. |
| `level` | Before relying on “X is at or above level L,” name the subject, what is being ordered, compared, grouped, or mapped, the relation or scale mapping that gives the claim its meaning, when it applies, and whether the claim is asserted, proposed, assumed, or only illustrated. List order, a diagram row, first-then sequence, carrier section, curriculum, scale label, stage sequence, or coarse-grained view supplies none of these. Then test holon or aggregation use only when a named relation or structure pattern defines it; otherwise test characteristic or scale, ordinal classification, organization scope, Work scope, evidence scope, publication grouping, or ordinary source-label non-use. |
| `tier` | Test deployment, service, organization, classification, aggregation, and publication meanings. When one of those claims is current, use the pattern that defines or tests it; `tier` itself is not the ontology. |
| `stack` | Test signature or slot construction, relation set or relation chain, architecture or control arrangement, aggregation arrangement, virtualization arrangement, deployment arrangement, publication-section ordering, or ordinary source-label non-use. A stack is not architecture by itself. |
| `ladder` and `rung` | Test ordinal or classification scale, declared maturity or readiness progression, C.28 causal-use ladder or rung, publication taxonomy, or ordinary source-label non-use. Do not use ladder wording for an undeclared progression scale. |
| `block` | Test module or interface, selected structure or structural view, function or transformation flow, mathematical lens or coarse-graining, evidence, causal use, gate, and decision meanings. |
| `expert` | In MoE-like prose, first test submodel, subholon, specialized transformation, path-selection relation, candidate-selection relation, ordinary wording, or source-label non-use. If claim-bearing wording still means only “role,” use `E.10.ROLE`; then recover independently any local system-role kind, separate System-classification judgment, obtaining assignment, performer System, Work occurrence, complete F.6 basis only when precise assignment-bound Work attribution is current, responsibility or authority relation, or another direct subject relation. Infer none from `expert`. |
| `cache` | Test module-interface, flow buffer or path, state or currentness, capacity characteristic, latency characteristic, memory characteristic, reuse characteristic, source-currentness, publication cache, temporal-aspect or rate-band claim, authored temporal-claim adequacy, or ordinary source-label non-use. |
| `router` | Test path selection, flow relation, transformation function or selection function, module-interface relation, candidate selection, decision, ordinary label, local system-role kind, separate System-classification judgment, obtaining assignment, or actual Work only when that exact claim is being made. |
| `gate` | Test constraint-validity record or gate-decision record, gating function, path selection, flow relation, publication label, or ordinary source-label non-use. A source label `gate` is not gate passage. |

#### C.30.STRAT:4.4 - Choose by recovered meaning

C.30 placement does not decide the recovered meaning. After recovery, use the rule that defines, constrains, or tests the actual object or claim.

#### C.30.STRAT:4.5 - Worked cases

| Wording | Repair |
| --- | --- |
| `The module layer is stable.` | Keep `layer` as a source label until the sentence reveals a module or interface relation, scale or comparison, publication or view, state, dynamics, or temporal claim. Use only the matching pattern: for example `A.6.M`, `C.16.P`, `C.29`, `C.2.P`, `A.19.SPR`, `A.3.3`, `C.27.TA`, or `C.27`. |
| `The expert routes the token.` | In mixture-of-experts prose, first test submodel or subholon, specialized transformation, path selection, architecture-to-flow relation, candidate selection, ordinary wording, or non-use. Only an unresolved claim-bearing use of *role* opens `E.10.ROLE`; any system-role kind, classification, assignment, performer, Work, responsibility, or authority claim must be established independently under its direct pattern. |
| `The cache proves the architecture scales.` | Split three questions: what `cache` names, whether an evidence or assurance relation exists, and what measurable scale or lens-use claim is being made. Use `A.6.M`, `A.6.F`, E.18, state or temporal patterns, `C.16.P`, C.29, A.10, B.3, or G.6 only for the branch that is actually present. |
| `The LCA upper layer guarantees safety.` | First decide whether `layer` names a control relation. If so, C.30.LCA records the relation, participant meanings, rate band, and relevant locality or model-use boundary. Safety, evidence, assurance, dynamics, temporal, and gate claims remain separate. |
| `The architecture description places service logic in the application layer.` | Recover the description's declared viewpoint or model-kind convention and what `application layer` means there. It may be a useful grouping in the description. State separately any claim that the described system itself has an obtaining layer, dependency, module, control, or flow relation; neither the diagram position nor architecture-description conformance establishes that world-side claim. |
| `Our operating model has strategic, coordination, and execution levels.` | If these are only headings or work areas, keep them as local labels. Before claiming levels in an organization or practice, say what the three areas are, how they are ordered or mapped, when that ordering applies, and whether it is asserted, proposed, assumed, or only illustrated. Slide order, a curriculum, or a first-then flow establishes none of this. |
| `This gate selects the winning architecture.` | A neural-network gate or router uses `A.6.F` or E.18; an internal-constraint result uses A.20; a project gate decision uses A.21; a selector-facing set-result declaration uses G.5, while a local choice among already available options uses C.11. The label alone decides none of these. |

#### C.30.STRAT:4.5a - Filled repair note

For `The cache proves the architecture scales`, do not hide the split inside one formal record. Read it as three candidate claims:

1. `cache` may name a state-bearing module, interface arrangement, flow buffer, or ordinary source label; the sentence does not yet decide which;
2. `proves` requires an actual evidence relation or assurance argument; otherwise lower that wording;
3. `scales` requires a characteristic and bearer, comparison or scale construction, architecture scale-preference claim, or mathematical-lens use.

A retained note can remain compact:

```text
StratificationSourceLabelRepairNote:
  sourceLabel: cache
  boundedTextSpan: “The cache proves the architecture scales.”
  recoveredObjectRelationOrClaim: cache meaning unresolved; proof and scale are separate claims
  sourceUseDisposition: keep cache as a source label until its relation or bearer is known
  patternRef?: A.6.M, A.6.F, E.18, A.19.SPR, or A.3.3 for the cache;
    C.16.P, C.29, or C.31.ASAP for scale; A.10, B.3, or G.6 for proof or assurance
  repairedWordingOrDemotion: “Identify what ‘cache’ names here, which scaling claim is being made, and what evidence supports it.”
  admissibleUse: start the three-way investigation
  stopOrReturnCondition: return to the source for the missing cache meaning, scaling basis, or evidence; use the direct pattern once that branch is recovered
  blockedOverread?: the source's proof-and-scale claim remains unsupported while its cache subject, scaling basis, and evidence are unresolved
  remainingReaderUse: state the smallest result for each recovered claim, or keep ordinary source wording
  disposition: reduced-use-cue; direct-pattern-use only for branches that become current
```

The note preserves every live branch without requiring a project engineer to reproduce E.10.ARCH authoring coordinates.

#### C.30.STRAT:4.6 - Lowering and reopen conditions

A repair remains usable only while its source span, recovered meaning, applicable rule, allowed use, and next action remain clear. Reopen or narrow it when the label begins carrying another relation or claim, the actual object becomes clear and makes this detour unnecessary, the interpretation was chosen from word similarity rather than evidence, or the repair is precise but leaves no useful reader action.

Lower the result to ordinary wording, quotation, reduced-use cue, blocked use, or incomplete rewrite when the object, applicable rule, allowed use, next action, or stop or return condition cannot be stated. Include a blocked overread only when it passes F.19's plausible-reader test.

### C.30.STRAT:5 - Archetypal Grounding

| Template element | `U.System` illustration | `U.Episteme` illustration |
| --- | --- | --- |
| Source-label cue | A neural-network source says an `expert block` sits above a `router layer`. | A publication note says a `cache layer` keeps a diagram or view current. |
| Recovery result | The words stay source labels until module, function, path-selection, flow, or selected-structure facts become clear. | The words stay source labels until publication, view, state, currentness, temporal, or ordinary non-use facts become clear. |
| Next move | Use `A.6.M`, `A.6.F`, E.18, C.30.TFS-REL, G.5, or C.11 only for the recovered claim. | Use the episteme/publication route in C.30.STRAT:4.2, or A.19.SPR, A.3.3, C.27.TA, or C.27 only for the recovered claim. |

### C.30.STRAT:6 - Bias-Annotation

Lenses: **Arch**, **Onto and Epist**, **Prag**, **Did**, and **Gov**. The pattern deliberately resists word-shape inference. Its counter-bias is equally important: ordinary prose stays ordinary, a known meaning uses its pattern directly, and the author-facing routing coordinates never become a project form.

### C.30.STRAT:7 - Conformance checklist

| ID | Check |
| --- | --- |
| `CC-C30STRAT-1` | The source word remains a source label until an object, relation, claim, or ordinary non-use is recovered. |
| `CC-C30STRAT-2` | The result names the bounded sentence, recovered meaning, any actual participants or bearer needed by the claim, repaired wording, allowed use, next action, and stop or return condition; an optional blocked overread passes F.19's plausible-reader test. |
| `CC-C30STRAT-3` | No universal kind is minted for layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or stratification. |
| `CC-C30STRAT-4` | The recovered meaning selects the applicable rule; the label and C.30 placement do not. |
| `CC-C30STRAT-5` | A known object or relation uses its pattern directly, without a restoration detour. |
| `CC-C30STRAT-6` | Several claims compressed into one sentence are separated; they are not forced under one label or invented common head. |
| `CC-C30STRAT-7` | Other patterns keep at most a thin pointer here and do not copy the cue table. |
| `CC-C30STRAT-8` | The engineer gets the shortest usable sentence or compact note; E.10.ARCH routing coordinates remain author-facing. |
| `CC-C30STRAT-9` | A consequential level claim names the subject, says what is being ordered, compared, grouped, or mapped and how, states when the claim applies, and marks it as asserted, proposed, assumed, or illustrative. No list, diagram row, first-then order, carrier section, curriculum, scale label, stage sequence, or coarse-grained description supplies that claim by form. |
| `CC-C30STRAT-10` | A label is treated as a designation in one bounded source use. Any model, viewpoint, standard, or local-vocabulary meaning is preserved in that use without becoming a universal kind or relation. |
| `CC-C30STRAT-11` | An architecture-description element is distinguished from the architecture or other world-side subject it describes; any claimed subject relation is stated and tested separately. |
| `CC-C30STRAT-12` | Controlled-language repair is used only when ambiguity changes reader action. It shortens or splits the sentence without deleting clear subject-specific terminology or choosing ontology from an approved-word list. |

### C.30.STRAT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Source label as ontology | `layer`, `block`, `expert`, `cache`, or `gate` is treated as a kind by name. | Recover the actual object or relation, or keep ordinary source wording. |
| C.30 takeover | Every structure-like word is treated as an architecture claim. | Choose from the recovered meaning; use the rule for the actual control, module, flow, scale, publication, state, evidence, work, or decision claim. |
| Standard-label overreach | A standard or popular model uses `layer` or `level`, so its local convention is treated as a universal subject structure. | Preserve the convention inside its declared source use; state and test any wider object, relation, mapping, or architecture claim separately. |
| Controlled-language purge | A preferred-word rule deletes a clear domain term or replaces it with formal apparatus although no reader action was at risk. | Keep the term; repair only the ambiguity that changes use, using the shortest direct sentence. |
| Level by layout | A list, vertical diagram, first-then flow, carrier section, curriculum, scale label, stage sequence, or coarse-grained description is treated as a subject stratification. | Keep the wording local, or name the subject, say what is being ordered, compared, grouped, or mapped and how, state when the claim applies, and mark it as asserted, proposed, assumed, or illustrative; then use the pattern that defines or tests that claim. |
| Local trigger fanout | C.30.LCA, A.6.M, C.31, or another pattern copies this label catalogue. | Keep one thin pointer here and the other pattern's own invariant there. |
| Expert-as-role false positive | `expert` in mixture-of-experts prose becomes a system-role kind, assignment, performer, Work, responsibility, or authority by word alone. | First test submodel, transformation, path selection, candidate selection, or ordinary non-use. If a claim-bearing use of *role* remains, use E.10.ROLE; identify each claimed system-role kind, classification judgment, assignment occurrence, performer System, or Work occurrence under its direct pattern; assert a responsibility, authority, or other relation only when its defining predicate independently obtains. |
| Gate-as-decision false positive | A gating function, UI label, or source word becomes gate passage. | Use A.20 or A.21 only for actual constraint-validity or gate-decision claims; otherwise use the applicable function, flow, publication, or ordinary-label result. |

### C.30.STRAT:9 - Consequences

| Benefit | Trade-off or mitigation |
| --- | --- |
| Local labels remain usable without becoming root kinds. | The reader pays a recovery cost only when the word carries a technical claim; ordinary prose closes immediately. |
| One cue table replaces copied local catalogues. | Other patterns need accurate thin pointers and must still state their own invariants. |
| A compressed sentence no longer smuggles several claims under one word. | The repair may name several applicable patterns, but only for branches that the sentence actually contains. |

### C.30.STRAT:10 - Rationale

Stratification words compress local practice. That compression is useful for recognition and unsafe as a substitute for an object, relation, or claim. C.30.STRAT therefore keeps the source word, recovers what it means in the current sentence, and returns the reader to the applicable technical rule.

### C.30.STRAT:11 - SoTA-Echoing

Standard status, publication date, and wide use do not by themselves show that an approach moves the relevant Pareto front. The comparison below adopts only contributions that recover a technical claim more reliably without making ordinary project language harder to use. The compact combination in this pattern—cheap exit, source-local meaning, recovered claim, next useful rule, stop or return condition, and any justified blocked overread—is FPF synthesis.

| Current source or practice | By-value decision | Contribution carried into this pattern | Limit and receiving loci |
| --- | --- | --- | --- |
| [ISO 704:2022, *Terminology work — Principles and methods*](https://www.iso.org/standard/79077.html) | Current published terminology-work standard checked 2026-08-22. **Adapt:** distinguish objects, concepts, definitions, and designations before standardizing a term; do not require a terminological entry for every ordinary sentence. | Treat `layer`, `level`, `gate`, and their neighbours first as designations in a bounded source use. Recover the object, relation, or claim before choosing a technical pattern. | A designation is not the thing or claim it helps name. Applied in recovery steps 2-4, the cue table, CC-C30STRAT-1/10, and the standard-label anti-pattern. |
| [ISO/IEC/IEEE 42010:2022, *Architecture description*](https://www.iso.org/standard/74393.html) | Current published architecture-description standard checked 2026-08-22. **Adopt narrowly:** distinguish an entity's architecture from an architecture description and recover the viewpoint or model-kind convention used by the description. **Reject:** using this standard as a system ontology, architecting Method, or proof that a described layer exists in the world. | When a label occurs in an architecture description, recover first what the description element means in its declared model or viewpoint; state separately any world-side structure or relation the sentence claims. | Architecture-description conformance is not architecture truth. Applied in recovery steps 3-5, the architecture-description worked case, the level-claim boundary, and CC-C30STRAT-11. |
| [ASD-STE100 Issue 9 (2025), *Simplified Technical English*](https://www.asd-ste100.org/) and its [scope explanation](https://www.asd-ste100.org/about_STE.html) | Current maintained controlled natural language checked 2026-08-22. **Adapt:** use short direct sentences and disambiguate a word when misunderstanding changes action; preserve subject-specific nouns and verbs. **Reject:** applying its controlled dictionary as a universal FPF vocabulary or deleting clear domain terms by lexical rule. | Keep the cheap exit and shortest direct repair; split compressed claims; preserve an already clear source-local technical term. | Controlled-language conformance cannot choose ontology and is not needed for every prose use. Applied in recovery steps 2 and 6, CC-C30STRAT-8/12, and the controlled-language-purge anti-pattern. |
| Current FPF `E.10`, `E.10.ARCH`, `F.18`, `F.19`, and the direct subject patterns | Current local architecture. **Adopt:** F.19 ordinary rewrite, E.10 cues, ontology-first recovery, direct source-local naming, and return to the pattern that defines or tests the recovered claim. | One short repair states recovered meaning, allowed use, next action, stop or return condition, and any blocked overread justified through F.19; author-facing routing stays out of ordinary project work. | This composition is the novel FPF synthesis. It must be reopened when a selected external source or a direct subject pattern supplies a better low-burden repair. Applied throughout Solution, Grounding, checklist, and Relations. |

Reopen only the affected cue, worked case, check, or pointer when a source changes. Reopen the wider pattern when a current approach demonstrates a meaning-recovery method that is more reliable at comparable reader effort, or when repeated use shows that the present cue table either misses consequential readings or sends clear ordinary language through unnecessary formal repair.

### C.30.STRAT:12 - Relations

- E.10 catches the wording trigger; E.10.ARCH supplies the author-facing recovery architecture and anti-fanout rule.
- C.30.P is the broader architecture and structure wording repair; C.30.STRAT is the narrow recurring source-label case.
- Use A.22, C.30, C.30.ASV, C.30.LCA, C.30.TFS-REL, or C.30.ILC only for the selected structure, architecture relation, view, control, flow, or conflict question each pattern defines or tests.
- Use A.6.M for recovered module and interface relations; A.6.F for recovered function claims; E.18 for graph, path, crossing, and transformation-flow claims; C.16.P, C.16, C.29, C.31, or C.31.RSA for recovered characteristic, scale, mathematical-lens, reusable-locus, bespoke-residue, or report-only-share claims.
- Use the episteme, publication, and source-use routes in C.30.STRAT:4.2; A.19.SPR for unresolved state wording; the applicable state rule, A.3.3, C.27.TA, or C.27 for recovered state, dynamics, temporal, or rate claims; C.28 for causal use; A.10 and G.6 for evidence; B.3 for assurance; A.20 for internal-constraint results and A.21 for gate decisions; A.15.1 for Work; A.2 for system-role kinds; G.5 for selector-facing set-result declarations and C.11 for local choice among already available options.
- C.33, C.34, and C.35 handle captured, lost, preserved, generated-carrier, or discovered-carrier structure when those claims are current.
- A recovered level claim returns to the pattern that defines or tests its subject relation or mapping. C.30.STRAT establishes no level by itself.

Stop after repairing the source label and naming the next useful action. Use the defining or testing pattern for each recovered object or claim, and keep its rules there.

### C.30.STRAT:End

