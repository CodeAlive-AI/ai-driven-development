## C.30.STRAT - Stratification Wording Precision Restoration

> **Type:** Architectural precision-restoration subpattern under `C.30`
> **Status:** Stable
> **Normativity:** Normative unless explicitly marked informative

**Plain-name.** Stratification and architecture-operation source-label repair.

**Intent.** Help a reader decide what a source label such as `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, `block`, `expert`, `cache`, `router`, or `gate` means in one current sentence. Keep useful local language, but recover the actual object, relation, or claim before relying on it. No use of this pattern mints `U.Layer`, `U.Level`, `U.Tier`, `U.Stack`, `U.Ladder`, `U.Rung`, `U.Block`, `U.Expert`, `U.Cache`, `U.Router`, `U.Gate`, or one universal `U.Stratification`.

**Builds on.** `E.10`, `E.10.ARCH`, `E.8`, `F.18`, `C.30.P`, `A.22`, and `C.30`.

**Coordinates with.** `C.30.ASV`, `C.30.LCA`, `C.30.TFS-REL`, `C.30.ILC`, `A.6.M`, `A.6.F`, `E.18`, `C.16.P`, `C.16`, `A.19.SPR`, `C.2.P`, `E.17`, `C.29`, `C.28`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `A.2`, `G.5`, and `C.11`.

**Authoring boundary.** `C.30.STRAT` supplies one reusable E.10.ARCH applicability row for this wording family. Its `semanticArea*` and `ontologicalNeighborhood` coordinates help pattern authors maintain that row; they are not a project object or a form for ordinary engineers. A practitioner receives the shortest sentence or note that names the recovered object, relation, or claim, the allowed use, the blocked overread, and the next action.

### C.30.STRAT:0 - Use this when

Use this pattern when a source uses a compact architecture or stratification label and that word alone does not tell you what technical claim is being made.

Typical labels are `layer`, `level`, `tier`, `stack`, `ladder`, `rung`, and architecture-operation words such as `block`, `expert`, `cache`, `router`, and `gate`.

**What goes wrong if missed.** A useful local label starts acting as ontology. A `layer` is assumed to be a holon level, control layer, publication layer, scale window, or module boundary without deciding which. A `stack` becomes architecture by name; a `block` becomes a module; an `expert` becomes a system-role kind or performer; a `cache` becomes a state or memory relation; a `router` becomes a decision policy; a `gate` becomes a gate decision. Word shape establishes none of these.

**What this buys.** The reader can keep the source word while making its actual meaning and safe use explicit. Once the object, relation, or claim is clear, use the pattern that defines, constrains, or tests it.

**First useful move.** Copy the sentence and ask: “What does this label name here, what may I infer from it, and what must I do next?” If it is ordinary wording, keep it and stop. If the answer is already clear, use the applicable pattern directly. Otherwise write one line: `label -> recovered meaning; allowed use; blocked overread; next pattern or blocker`. Do not fill an author-facing E.10.ARCH routing row during ordinary project work.

**Not this pattern when.** Do not detour through C.30.STRAT when the object, relation, or claim is already clear. Do not use it merely because a familiar word appears. Ordinary source prose with no FPF claim remains ordinary prose or a quotation.

### C.30.STRAT:1 - Problem frame

Architecture and engineering sources use compact labels because they work in local practice. Neural-network prose says `block`, `expert`, `cache`, or `router`; control architecture says `layer`; organizations say `level` or `tier`; documentation says `section`, `stack`, or `view`; scale prose says `level`, `resolution`, or `coarse-graining step`.

These words are good recognition cues but poor stand-alone kinds. The same label can point to a selected structure, module relation, control relation, transformation-flow element, characteristic or scale, publication grouping, state, evidence claim, decision, or nothing beyond ordinary prose.

The repair question is simple: what does the label name in this sentence, what stronger reading must be blocked, and which existing pattern supplies the needed definition, constraint, or test?

### C.30.STRAT:2 - Problem

How can FPF keep common stratification and architecture-operation language without turning the words into false root kinds, routing every structure-like phrase through C.30, copying the same trigger catalogue into many patterns, inferring technical claims from word shape, or deleting useful source language before its remaining reader use is clear?

### C.30.STRAT:3 - Forces

| Force | Tension |
| --- | --- |
| Source-language usability vs ontology | Practitioners need compact local words; a technical claim needs the actual object or relation, its participants or bearer, its scope, and its allowed use. |
| Pattern placement vs applicable rule | This pattern sits under `C.30` because architecture prose is the usual entry, but the recovered claim may belong to control, modules, flow, scale, publication, state, evidence, work, or decision. |
| Thin repair vs shadow registry | One shared cue table is useful; copied local trigger lists are not. |
| Known meaning vs detour | When the current object or relation is already clear, use its pattern directly. |
| Precision vs action | A type-correct result is still a failure if the reader cannot see what to do next. |

### C.30.STRAT:4 - Solution

Write the direct local repair first. For example: `Here “gate” names the neural-network path selector, not a project gate decision; use E.18 to describe the selected path.` That sentence can be the complete result.

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
  blockedOverread:
  remainingReaderUse:
  disposition: direct-pattern-use | local-rewrite | ordinary-source-label |
    quote-only | reduced-use-cue | blocked-use | incomplete-rewrite
```

The note is neither the selected structure nor the relation, claim, publication, or pattern result it points to. Omit it when the direct sentence is enough.

#### C.30.STRAT:4.1 - Recovery sequence

1. **Copy the sentence and label.** Keep enough source context to tell what the sentence is doing.
2. **Try the cheap exits.** If the word carries no FPF claim, keep ordinary prose or quote it and stop. If one local rewrite makes the meaning clear, write it and stop.
3. **Recover plausible meanings.** Ask which object, relation, participants or bearer, claim, scope, time, and source use the sentence could be compressing. Include literal and metonymic readings when both are plausible.
4. **Choose by the recovered meaning.** Use the first matching row in C.30.STRAT:4.2; never choose from the label alone.
5. **Open only the needed rule.** Name the actual participants, relation, structure, characteristic, state, publication, evidence, work, decision, or other object that makes the claim true or false. Do not copy every possible field into the result.
6. **Return to ordinary wording.** Write the shortest sentence that preserves the recovered claim and names the next pattern only when its contribution matters.
7. **State the stop.** Give the allowed use, the tempting stronger reading that remains blocked, and the next action. If no useful action survives, use quote-only, reduced-use, blocked, or incomplete-rewrite disposition.

#### C.30.STRAT:4.2 - Recovered meanings and patterns to use

| Recovered meaning | Common source labels | What must become clear | Pattern to use |
| --- | --- | --- | --- |
| Control structure | `layer`, `level`, `tier`, sometimes `gate` | The obtaining control relation, what its participants do, any rate band or locality boundary, and a B.2.5 supervisor-subholon relation only when it obtains. | `C.30.LCA`; use B.2.5, dynamics, temporal, evidence, assurance, or gate patterns only for their separate claims. |
| Selected structure or structural view | `layer`, `level`, `stack`, `block`, `view` | The selected, hidden, lost, or preserved structure; view selection; correspondence; source return; an `ArchitectureClaim` when claim content is needed; and a separate `ArchitectureRelation` only when that direct relation obtains. | `A.22`, `C.30`, `C.30.ASV`, or the applicable C.30 subpattern. |
| Module, interface, or substitution | `block`, `cache`, `router`, `expert`, sometimes `layer` or `stack` | Module boundary, interface specification, substitutability relation, variation point, conformance relation, or reliance boundary. | `A.6.M`; stop using C.30.STRAT once that relation is clear. |
| Function or transformation flow | `block`, `expert`, `cache`, `router`, `gate`, sometimes `layer` | Transformation or effect, path selection, graph node, path or crossing, architecture-to-flow relation, or E.18 flow valuation. | `A.6.F`, `E.18`, or `C.30.TFS-REL`. |
| Characteristic, scale, or mathematical lens | `level`, `tier`, `ladder`, `rung`, `layer`, `stack`, `block` | Characteristic and bearer, coordinate or value, scoring method, comparison criterion, scale window, resolution, coarse-graining, preserved or lost structure, lens-use result, and stop condition only where the claim needs them. | `C.16.P`, the applicable characterization pattern, or `C.29`. |
| Episteme, publication, view, or source use | `stack`, `layer`, `section`, `view`, `cache`, `gate` | Description episteme, publication unit, face, form, carrier, source-currentness or source-use relation, source-return condition, or ordinary publication label. | `C.2.P`, `E.17`, or the pattern for the publication or source-use claim. |
| State, currentness, time, or dynamics | `cache`, `stable`, `level`, `readiness`, sometimes `gate` | Bearer, state frame and values, validity window, currentness relation, dynamics, temporal aspect or rate band, authored temporal-claim adequacy, and reopen condition. | `A.19.SPR`, `A.3.3`, `C.27.TA`, `C.27`, or the applicable state or temporal pattern. |
| Evidence, assurance, gate, work, decision, or causal use | `gate`, `proof`, `safety`, `decision`, `work`, `effect`, or any label used as authority | Evidence path, assurance argument, constraint-validity record, gate decision, Work occurrence, decision record, causal-use record, and the stronger readings that remain blocked. | `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, `C.28`, or the applicable neighboring pattern. |
| Ordinary source-label non-use | any source label | No FPF claim remains after the sentence is read in context. | No precision-restoration pattern; keep ordinary wording, quote it, reduce its use, or block reliance. |

#### C.30.STRAT:4.2a - Same-sentence claim boundary

One sentence may use a source label while making several claims. Split them instead of adding a local catalogue of everything the label does not prove. C.30.STRAT repairs the label; the applicable pattern defines, constrains, or tests each separate claim. The table above lists common destinations, not a mandatory reading list.

#### C.30.STRAT:4.3 - Source-label cue table

| Source label family | Recovery discipline |
| --- | --- |
| `layer` | Do not choose by the word. Test control structure; selected structure or structural view; module or interface; scale or mathematical lens; and publication or source-use meanings. |
| `level` | Test holon-level or aggregation use only when a named relation or structure pattern defines it; otherwise test characteristic or scale, ordinal classification, organization scope, Work scope, evidence scope, publication grouping, or ordinary source-label non-use. |
| `tier` | Test deployment, service, organization, classification, aggregation, and publication meanings. When one of those claims is current, use the pattern that defines or tests it; `tier` itself is not the ontology. |
| `stack` | Test signature or slot construction, relation set or relation chain, architecture or control arrangement, aggregation arrangement, virtualization arrangement, deployment arrangement, publication-section ordering, or ordinary source-label non-use. A stack is not architecture by itself. |
| `ladder` and `rung` | Test ordinal or classification scale, declared maturity or readiness progression, C.28 causal-use ladder or rung, publication taxonomy, or ordinary source-label non-use. Do not use ladder wording for an undeclared progression scale. |
| `block` | Test module or interface, selected structure or structural view, function or transformation flow, mathematical lens or coarse-graining, evidence, causal use, gate, and decision meanings. |
| `expert` | In MoE-like prose, first test submodel, subholon, specialized transformation, path-selection relation, candidate-selection relation, ordinary wording, or source-label non-use. If claim-bearing wording still means only “role,” use `E.10.ROLE`; then recover independently any local system-role kind, separate System-classification judgment, obtaining assignment, performer System and complete Work-attribution basis, responsibility or authority relation, or another direct subject relation. Infer none from `expert`. |
| `cache` | Test module-interface, flow buffer or path, state or currentness, capacity characteristic, latency characteristic, memory characteristic, reuse characteristic, source-currentness, publication cache, temporal-aspect or rate-band claim, authored temporal-claim adequacy, or ordinary source-label non-use. |
| `router` | Test path selection, flow relation, transformation function or selection function, module-interface relation, candidate selection, decision, ordinary label, local system-role kind, separate System-classification judgment, obtaining assignment, or actual Work only when that exact claim is being made. |
| `gate` | Test constraint-validity record or gate-decision record, gating function, path selection, flow relation, publication label, or ordinary source-label non-use. A source label `gate` is not gate passage. |

#### C.30.STRAT:4.4 - Author-facing placement note

This subsection maintains the E.10.ARCH applicability row; it is not part of the ordinary project result.

- `semanticAreaBaseConcept` is stratification wording and architecture-operation source labels.
- `semanticArea` is the Part-F row-set for `layer`, `level`, `tier`, `stack`, `ladder`, and `rung`, plus `block`, `expert`, `cache`, `router`, and `gate` when they appear before their technical meaning is known.
- `semanticAreaSenseFamily` is source-label wording for stratification, ordering, aggregation, and architecture-operation recognition. It is not a topic, workstream, or pattern grouping.
- `ontologicalNeighborhood` is the author-facing applicability family selected from C.30.STRAT:4.2. It is neither a second ontology nor a field that an engineer adds to the project object.

The pattern is placed under `C.30.*` because architecture and structure prose is the recurring entry. Placement does not decide the recovered meaning. After recovery, use the rule that defines, constrains, or tests the actual object or claim.

#### C.30.STRAT:4.5 - Worked cases

| Wording | Repair |
| --- | --- |
| `The module layer is stable.` | Keep `layer` as a source label until the sentence reveals a module or interface relation, scale or comparison, publication or view, state, dynamics, or temporal claim. Use only the matching pattern: for example `A.6.M`, `C.16.P`, `C.29`, `C.2.P`, `A.19.SPR`, `A.3.3`, `C.27.TA`, or `C.27`. |
| `The expert routes the token.` | In mixture-of-experts prose, first test submodel or subholon, specialized transformation, path selection, architecture-to-flow relation, candidate selection, ordinary wording, or non-use. Only an unresolved claim-bearing use of *role* opens `E.10.ROLE`; any system-role kind, classification, assignment, performer, Work, responsibility, or authority claim must then obtain independently. |
| `The cache proves the architecture scales.` | Split three questions: what `cache` names, whether an evidence or assurance relation exists, and what measurable scale or lens-use claim is being made. Use `A.6.M`, `A.6.F`, E.18, state or temporal patterns, `C.16.P`, C.29, A.10, B.3, or G.6 only for the branch that is actually present. |
| `The LCA upper layer guarantees safety.` | First decide whether `layer` names a control relation. If so, C.30.LCA records the relation, participant meanings, rate band, and relevant locality or model-use boundary. Safety, evidence, assurance, dynamics, temporal, and gate claims remain separate. |
| `This gate selects the winning architecture.` | A neural-network gate or router uses `A.6.F` or E.18; a project gate decision uses A.20 or A.21; candidate selection uses G.5 or C.11. The label alone decides none of these. |

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
  repairedWordingOrDemotion: “The response cache is a candidate state-bearing part of the architecture; no proof or scaling claim has yet been established.”
  admissibleUse: start the three-way investigation
  blockedOverread: cache does not prove scaling, substitutability, or architecture quality
  remainingReaderUse: state the smallest result for each recovered claim, or keep ordinary source wording
  disposition: local-rewrite; direct-pattern-use only for branches that become current
```

The note preserves every live branch without requiring a project engineer to reproduce E.10.ARCH authoring coordinates.

#### C.30.STRAT:4.6 - Lowering and reopen conditions

A repair remains usable only while its source span, recovered meaning, applicable rule, allowed use, and next action remain clear. Reopen or narrow it when the label begins carrying another relation or claim, the actual object becomes clear and makes this detour unnecessary, the interpretation was chosen from word similarity rather than evidence, or the repair is precise but leaves no useful reader action.

Also reopen the affected authoring row when E.10.ARCH changes its internal coordinates, C.30.P changes architecture-wording repair, F.19 changes the plain-language boundary, or another realization pattern now handles this wording family. Lower the result to ordinary wording, quotation, reduced-use cue, blocked use, or incomplete rewrite when the object, applicable rule, allowed use, blocked overread, or next action cannot be stated.

### C.30.STRAT:5 - Archetypal Grounding

| Template element | `U.System` illustration | `U.Episteme` illustration |
| --- | --- | --- |
| Source-label cue | A neural-network source says an `expert block` sits above a `router layer`. | A publication note says a `cache layer` keeps a diagram or view current. |
| Recovery result | The words stay source labels until module, function, path-selection, flow, or selected-structure facts become clear. | The words stay source labels until publication, view, state, currentness, temporal, or ordinary non-use facts become clear. |
| Next move | Use `A.6.M`, `A.6.F`, E.18, C.30.TFS-REL, G.5, or C.11 only for the recovered claim. | Use C.2.P, E.17, A.19.SPR, A.3.3, C.27.TA, or C.27 only for the recovered claim. |

### C.30.STRAT:6 - Bias-Annotation

Lenses tested: **Arch**, **Onto and Epist**, **Prag**, **Did**, and **Gov**. The pattern deliberately resists word-shape inference. Its counter-bias is equally important: ordinary prose stays ordinary, a known meaning uses its pattern directly, and the author-facing routing coordinates never become a project form.

### C.30.STRAT:7 - Conformance checklist

| ID | Check |
| --- | --- |
| `CC-C30STRAT-1` | The source word remains a source label until an object, relation, claim, or ordinary non-use is recovered. |
| `CC-C30STRAT-2` | The result names the bounded sentence, recovered meaning, any actual participants or bearer needed by the claim, repaired wording, allowed use, blocked overread, and next action. |
| `CC-C30STRAT-3` | No universal kind is minted for layer, level, tier, stack, ladder, rung, block, expert, cache, router, gate, or stratification. |
| `CC-C30STRAT-4` | The recovered meaning selects the applicable rule; the label and C.30 placement do not. |
| `CC-C30STRAT-5` | A known object or relation uses its pattern directly, without a restoration detour. |
| `CC-C30STRAT-6` | Several claims compressed into one sentence are separated; they are not forced under one label or invented common head. |
| `CC-C30STRAT-7` | Other patterns keep at most a thin pointer here and do not copy the cue table. |
| `CC-C30STRAT-8` | The engineer gets the shortest usable sentence or compact note; E.10.ARCH routing coordinates remain author-facing. |

### C.30.STRAT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Source label as ontology | `layer`, `block`, `expert`, `cache`, or `gate` is treated as a kind by name. | Recover the actual object or relation, or keep ordinary source wording. |
| C.30 takeover | Every structure-like word is treated as an architecture claim. | Choose from the recovered meaning; use the rule for the actual control, module, flow, scale, publication, state, evidence, work, or decision claim. |
| Local trigger fanout | C.30.LCA, A.6.M, C.31, or another pattern copies this label catalogue. | Keep one thin pointer here and the other pattern's own invariant there. |
| Expert-as-role false positive | `expert` in mixture-of-experts prose becomes a system-role kind, assignment, performer, Work, responsibility, or authority by word alone. | First test submodel, transformation, path selection, candidate selection, or ordinary non-use. If a claim-bearing use of *role* remains, use E.10.ROLE; admit each system-role, classification, assignment, performer, Work, responsibility, authority, or other relation only when it independently obtains. |
| Gate-as-decision false positive | A gating function, UI label, or source word becomes gate passage. | Use A.20 or A.21 only for actual constraint-validity or gate-decision claims; otherwise use the applicable function, flow, publication, or ordinary-label result. |

### C.30.STRAT:9 - Consequences

| Benefit | Trade-off or mitigation |
| --- | --- |
| Local labels remain usable without becoming root kinds. | The reader pays a recovery cost only when the word carries a technical claim; ordinary prose closes immediately. |
| One cue table replaces copied local catalogues. | Other patterns need accurate thin pointers and must still state their own invariants. |
| A compressed sentence no longer smuggles several claims under one word. | The repair may name several applicable patterns, but only for branches that the sentence actually contains. |

### C.30.STRAT:10 - Rationale

Stratification words compress local practice. That compression is useful for recognition and unsafe as a substitute for an object, relation, or claim. C.30.STRAT therefore keeps the source word, recovers what it means in the current sentence, and returns the reader to the applicable technical rule.

The pattern sits under C.30 because architecture and structure prose is the usual entry. That placement is a navigation choice, not an ontological claim and not authority over every recovered case.

### C.30.STRAT:11 - SoTA-Echoing

This pattern does not import a new external stratification ontology. It responds to a widespread engineering practice: local fields use compact words such as `layer`, `level`, `tier`, `stack`, `block`, `expert`, `cache`, `router`, and `gate` for different objects and relations. FPF keeps that useful recognition language and requires the technical meaning to be recovered before the word carries a stronger claim.

E.10 supplies the cheap wording trigger, E.10.ARCH keeps the author-facing applicability architecture, C.30.P handles broader architecture wording, F.19 supplies the plain-language test, and the applicable technical patterns define or test the recovered claims. Recheck only the affected cue, table row, worked case, or pointer when one of those sources changes; do not rebuild a local trigger registry.

### C.30.STRAT:12 - Relations

- E.10 catches the wording trigger; E.10.ARCH supplies the author-facing recovery architecture and anti-fanout rule.
- C.30.P is the broader architecture and structure wording repair; C.30.STRAT is the narrow recurring source-label case.
- Use A.22, C.30, C.30.ASV, C.30.LCA, C.30.TFS-REL, or C.30.ILC only for the selected structure, architecture relation, view, control, flow, or conflict question each pattern defines or tests.
- Use A.6.M for recovered module and interface relations; A.6.F for recovered function claims; E.18 for graph, path, crossing, and transformation-flow claims; C.16.P, C.16, C.29, C.31, or C.31.RSA for recovered characteristic, scale, mathematical-lens, reusable-locus, bespoke-residue, or report-only-share claims.
- Use C.2.P and E.17 for source and publication relations; A.19.SPR, A.3.3, C.27.TA, and C.27 for state, dynamics, temporal, and rate claims; C.28 for causal use; A.10 and G.6 for evidence; B.3 for assurance; A.20 and A.21 for constraint validity and gates; A.15 for Work; A.2 for system-role kinds; G.5 and C.11 for selection and decision.
- C.33, C.34, and C.35 handle captured, lost, preserved, generated-carrier, or discovered-carrier structure when those claims are current.

C.30.STRAT stops after repairing the source label and naming the next useful action. It creates none of the recovered objects or claims and carries no duplicate version of their rules.

### C.30.STRAT:End

