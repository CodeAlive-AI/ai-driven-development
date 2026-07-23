## C.3 - Kinds, Intent and Extent, and Typed Reasoning

> **Type:** Typed reasoning discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.3:0 - Use This When

Use this pattern when a claim needs a context-local kind, a subkind order, a judgment about whether one exact candidate satisfies one local kind, or an optional representation of the candidates that satisfy it in one exact context slice.

**What goes wrong if missed.** A source type, local category, programming class, schema label, mathematical set, or public `U.*` name starts doing several jobs at once. The kind is confused with its declaration, evidence is treated as membership, an unavailable fact becomes false, a current extension becomes ontology, or claim scope is stored on the kind.

**What this buys.** Typed reasoning stays usable without premature ontology growth. A practitioner can recover the local kind, the declaration used to classify, one three-valued judgment, and any optional extension representation while leaving direct world-side features, evidence, scope, work, and durable U-kind admission with their own governors.

**Primary EntityOfConcern.** One typed-reasoning use under an effective `U.ReferenceScheme`: the exact local `U.Kind` and any `U.SubkindOf` order needed by the claim, together with the C.3.2 classification question that the use actually asks.

**First useful move.** Write the ordinary conclusion first. For example: `Pump #14 counts as a cooling pump in this plant slice because it satisfies the declared cooling-pump criterion.` Add a reusable declaration, explicit judgment details, evidence reference, or extension representation only when a named receiving use needs it.

**Not this pattern when.** Use `E.24.UK` when the question is durable public FPF U-kind admission. Use the direct subject pattern when the question is whether a physical quality, relation, construction, work occurrence, or other world-side feature obtains. Use `A.2.6` for claim, work, or publication scope and `C.29` for a claim-bearing mathematical representation.

### C.3:1 - Problem Frame

Across source ontologies, reference schemes, and project slices, "type" can mean ontology class, programming type, schema shape, category, source label, local kind, or public FPF U-kind. C.3 provides the smaller typed-reasoning architecture. A context-local `U.Kind` can be used now without being promoted to a durable public kind; its declared intent, candidate judgment, current extension representation, and the scope of any assertion remain separate objects.

### C.3:2 - Problem

A project often needs classification before it needs ontology governance. If the kind, its definition, the classified candidate, a record about the candidate, and a displayed set of current members are treated as one object, several false conclusions follow: a label classifies by itself, evidence creates the feature it reports, missing evidence proves non-membership, a table becomes an entity set, or a plan row becomes actual work. C.3 keeps each conclusion at its direct owner.

### C.3:3 - Forces

| Force | Tension |
| --- | --- |
| Local typed reasoning vs public ontology growth | A project needs typed claims now, but not every useful local kind deserves a durable FPF `U.*` name. |
| Kind vs declaration | A kind must remain usable across compatible declaration editions without becoming identical to the episteme that declares its criterion. |
| Truth vs support | Direct candidate features make classification true or false; evidence can support an assertion about those features but cannot create them. |
| False vs unknown | A known failed criterion differs from missing evidence, unavailable dependency, or out-of-domain input. |
| Extent vs ontology | A set of true members can be useful for a query without becoming a collection holon, entity-set kind, or direct relation occurrence. |
| Scope vs kind | A claim can have narrow scope without creating a narrower kind or storing scope on the kind. |
| Formal discipline vs ordinary use | Repeated typed use may need a declaration; one readable case should not require a card or extension table. |

### C.3:4 - Four Objects and Their Owners

Keep these four objects separately recoverable:

| Object | Meaning | Direct owner |
| --- | --- | --- |
| context-local `U.Kind` and `U.SubkindOf` order | The kind value used by the typed-reasoning claim and its local partial order. | `C.3` and `C.3.1` |
| `KindSignature` | One `U.Signature` declaration episteme whose exact EntityOfConcern is the local kind and whose claim content declares the candidate `ValueKind`, criterion, slice conditions, reference scheme, assumptions, dependencies, formality, and any current `ExtentRule`. It is neither the kind nor another root U-kind. | `C.3.2`, `A.6.0`, and `C.2.1` |
| classification judgment | One evaluation for an exact candidate, local kind, signature edition, and context slice with result `true`, `false`, or `unknown`. It is not a direct relation occurrence by default. | `C.3.2` |
| `KindExtension(k, slice)` | An optional set-valued representation of the declared candidates whose judgment is `true` for the fixed signature edition and slice. | `C.3.2`, with `C.29` when the representation changes a claim-bearing use |

Scope is not a fifth part of the kind. A `KindSignature` episteme may carry its own `U.ClaimScope`, and a separate classification assertion carries the scope of that assertion. The `U.ContextSlice` is an explicit input to the judgment.

### C.3:5 - Solution

Use the lightest object that answers the current typed-reasoning question.

1. **Recover the local kind.** State the effective `U.ReferenceScheme` and the typed-reasoning use. A local `U.Kind` is not automatically a durable FPF U-kind.
2. **Use C.3.1 for order and continuity.** `U.SubkindOf` is a partial order over local kinds. C.3.1 also decides whether the same local kind continues when a declaration edition changes.
3. **Use C.3.2 for declaration and judgment.** A repeated criterion may justify a `KindSignature`; one application judges an exact candidate against one exact edition in one exact slice.
4. **Let direct features decide.** Direct qualities, relations, constructive grounding, or other governed candidate features make the criterion hold or fail. Measurements, observations, schemas, sources, and evidence support claims about those features; they do not constitute membership.
5. **Keep three results.** A satisfied criterion gives `true`; a known failed criterion gives `false`; missing evidence, an unavailable declared dependency, or an out-of-domain candidate gives `unknown`. A guard may decline use on `unknown` without changing that judgment to `false`.
6. **Materialize an extension only for use.** A query, quantification, comparison, or review may need `KindExtension(k, slice)`. The representation contains the true candidates for the fixed signature edition and slice; notation, rows, or set membership do not create an ontic collection or classification relation.
7. **Keep scope, formality, and work separate.** Formality characterizes the declaration episteme. Scope belongs to claims or capabilities. `U.Work` is the admitted U-kind; `W : U.Work` is one independently grounded, world-side, dated 4D work occurrence; a plan, log, card, field bundle, or database row about W is a separate episteme. No kind symbol or record occupies an individual-occurrence position.

Typed reasoning composes with F-G-R and USM in this order: recover typed compatibility and the exact judgment; separately check claim-scope coverage; then apply evidence, assurance, freshness, and bridge consequences when the receiving use requires them.

### C.3:6 - Decision Split

| Current question | Governing pattern |
| --- | --- |
| What local kind does this claim quantify over? | `C.3` and `C.3.1` |
| Is one local kind a subkind of another, or does the same kind continue across a declaration change? | `C.3.1` |
| Does this exact candidate satisfy this local kind under this declaration edition and context slice? | `C.3.2` |
| Does a receiving use need the represented set of true members? | `C.3.2`; `C.29` when the representation itself changes a claim-bearing use |
| Does the assertion hold in a target slice? | `A.2.6` for its `U.ClaimScope`; do not attach that scope to the kind |
| Is the local kind being proposed as a durable public FPF `U.*` kind? | `E.24.UK`, followed by the applicable naming patterns |
| Is a candidate, quality, relation, construction, or work occurrence being identified? | The direct subject pattern; C.3 consumes the governed result and does not create it |

When typed reasoning is part of a structural construction-to-representation passage from a constructive representation or working model to a target kind or logical representation, cite `StructuralCT2RTypingGroundingUnfoldingStructureBlock` from `B.3.5`. C.3 contributes only the local kind, judgment, subkind, and bridge loci inside that B.3.5-governed local `A.22.CGUS` specialization. It does not create separate unfolding-structure authority and does not make a constructive trace, working-model relation, proof, evidence relation, or classification true by label. For a general diagnostic return from an inadequate working account to the exact subject construction, use `A.7.1`; classification remains one possible locus rather than a general ontology-return method.

The unfolding is admitted only when the block names the starting representation, target kind or logical representation, current bridge when one is used, preserved structure, lost or collapsed structure, `CL` or `CL^k`, admissible reuse, blocked substitution, and the proof or evidence governing pattern when that stronger claim is current.

### C.3:7 - Archetypal Grounding

| Situation | C.3 typed-reasoning move | Boundary |
| --- | --- | --- |
| Pump #14 is evaluated as a cooling pump. | Use one local kind, one declared criterion, one exact plant slice, and one `true`/`false`/`unknown` judgment. | The pump and its cooling, flow, and measured-state facts remain under direct physical and measurement governors. |
| A maintenance episteme is classified while PDF and HTML forms circulate. | Judge the exact episteme against the local kind criterion. | Publication form and carrier do not decide membership. |
| A temperature value is classified into an interval. | Keep the value under its unit and measurement interpretation and judge the value directly. | Do not fabricate a value-shaped entity merely to classify it. |
| A schema labels a row `Customer`. | Treat the label as a cue to recover the actual candidate and criterion. | Schema spelling alone yields neither `true` nor a public U-kind. |
| A measurement required by a criterion is unavailable. | Return `unknown`; let a safety guard decline the use separately. | Do not coerce missing information to `false`. |
| A log row is labelled `inspection work`. | First identify any exact dated `W : U.Work` under `A.15.1`; only then can W be a candidate for a local kind. | The row, plan, or label is not W, and `U.Work` never occupies W's individual position. |

### C.3:8 - Bias-Annotation

C.3 counters lexical bias, document bias, and ontology-growth bias. A familiar type word or schema label does not supply the declared criterion. A record or evidence item does not create the candidate feature. A displayed set does not create a collection holon. The mitigation is the four-object split, direct-feature judgment, three-valued result, and progressive elaboration from one readable sentence.

### C.3:9 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C3-1` | The local `U.Kind` and any `U.SubkindOf` order remain distinct from durable FPF U-kind admission. |
| `CC-C3-2` | Kind, `KindSignature`, classification judgment, and optional `KindExtension` are separately recoverable. |
| `CC-C3-3` | The judgment names an exact candidate, kind, signature edition, context slice, and one of `true`, `false`, or `unknown`. |
| `CC-C3-4` | Direct governed candidate features decide classification; evidence or representation does not create membership. |
| `CC-C3-5` | Missing evidence, unavailable dependency, and out-of-domain input yield `unknown`, not `false`. |
| `CC-C3-6` | Kind scope is absent; declaration and assertion scopes remain on their own epistemes, and `U.ContextSlice` remains an evaluation input. |
| `CC-C3-7` | An extension is a representation of true candidates, not `U.EntitySet`, A.14 `MemberOf`, a collection holon, or a direct relation occurrence. |
| `CC-C3-8` | Public `U.*` admission uses `E.24.UK`; cross-context kind use uses `C.3.3`. |
| `CC-C3-9` | `U.Work`, an exact `W : U.Work`, and any episteme about W remain distinct. |

### C.3:10 - Common Anti-Patterns and How to Avoid Them

* Treating a programming type, schema class, source ontology class, regulatory category, or ordinary noun as a durable public FPF U-kind.
* Treating a `KindSignature` as the kind, or attaching its formality and claim scope to the kind.
* Using A.14 `MemberOf` or minting a classification relation merely to state one judgment.
* Treating evidence availability, a schema row, or a publication form as the fact that makes classification true.
* Returning `false` when the criterion cannot be evaluated.
* Treating `KindExtension` or mathematical set notation as ontology.
* Repairing a subkind counterexample by silently changing an extension table.
* Treating a plan or work record as a dated work occurrence.

### C.3:11 - Consequences

**Benefits.** C.3 supports local typed claims, subkind reasoning, classification, and queryable extensions without premature ontology growth or evidence-created membership.

**Costs.** Repeated uses must pin a declaration edition and context slice, and receiving uses must distinguish `false` from `unknown`.

**Risks avoided.** False sameness, implicit time, scope-on-kind, record ontology, accidental relation minting, kind/individual substitution, and mathematical-set overread are blocked at the first use.

### C.3:12 - Rationale

The kind, its declaration, one classification judgment, and a representation of current true members answer different engineering questions and change for different reasons. Keeping them separate lets a kind continue across compatible declaration revisions, lets candidate state change an extension without changing the kind, and lets evidence or a guard change reliance without rewriting the world-side classification.

### C.3:13 - SoTA-Echoing

Model theory, type systems, ontology engineering, and schema practice distinguish intensional declarations, candidate evaluation, extensions, and assertion scope. C.3 adapts that separation to FPF's object discipline: declaration epistemes follow `A.6.0` and `C.2.1`, context slices and claim scope follow `A.2.6`, mathematical representations follow `C.29`, and durable kind admission follows `E.24.UK`.

### C.3:14 - Detail Map
C.3 is the head pattern for typed reasoning. It leaves each detailed mechanism at its direct neighboring pattern while preserving a discoverable route to that mechanism.

| Needed detail | Governing locus | Content carried there |
| --- | --- | --- |
| Local kind order and continuity | `C.3.1` | `U.Kind`, `U.SubkindOf`, partial-order law, judgment monotonicity, and continuity across signature editions. |
| Declaration, candidate judgment, and extension | `C.3.2` | `KindSignature`, exact four-key judgment, `true`/`false`/`unknown`, optional `KindExtension`, and scope/formality/evidence boundaries. |
| Cross-context kind use | `C.3.3` | The direct `KindBridge` relation between exact source and target local kinds, its separate bridge-assertion episteme, declared preservation and loss, and target-context reevaluation under the exact target `KindSignature` edition. |
| Local adaptation without cloning a kind | `C.3.4` | A `RoleMask` declaration episteme, its pinned base-kind judgment and additional candidate-feature constraints, the exact three-valued masked judgment, and any separately declared cross-context adapter. |
| Abstraction facet | `C.3.5` | `KindAT` as an editorial planning facet on one exact local kind, with no effect on the kind, declaration, judgment, extension, bridge assessment, guard, or F–G–R. |
| Typed guards and applied examples | `C.3.A` | Declaration-level kind compatibility and exact candidate-use judgments kept separate across regulatory, assurance, ESG, and Method–Work uses, including the independently grounded actual `W : U.Work` boundary. |

Do not treat this compact head pattern as the whole C.3 discipline when a case needs declaration, classification, extension, bridge, mask, abstraction, or applied-guard detail. Use the neighboring C.3 pattern that governs the live detail.

### C.3:15 - Relations

- **Builds on:** `A.2.6` context-slice and scope discipline, `A.6.0` reusable declaration discipline, `C.2.1` episteme identity, F-G-R, and direct subject patterns for candidate features.
- **Coordinates with:** `C.3.1` through `C.3.5`, `C.3.A`, `C.29`, `E.24.UK`, `A.8`, `A.11`, `F.8`, `F.18`, and generic `A.22.CGUS` when typed reasoning is one locus in an admitted unfolding structure; coordinates with `StructuralCT2RTypingGroundingUnfoldingStructureBlock` only when C.3 supplies local-kind, judgment, subkind, and bridge loci inside a structural construction-to-typed/logical projection, with any cross-context bridge remaining a bridge within that projection rather than an alternative trigger; coordinates with `A.7.1` for a general diagnostic return.
- **Does not replace:** direct candidate-feature ontology, A.14 collection membership, `A.2.6` scope, `C.29` representation use, ontic settlement in `E.24`, U-kind admission in `E.24.UK`, or naming in Part F.

### C.3:End

