## C.3 - Kinds, Intent and Extent, and Typed Reasoning

> **Type:** Typed reasoning discipline pattern
> **Status:** Stable
> **Normativity:** Normative unless a section is explicitly informative

### C.3:0 - Use This When

Use this pattern when a claim needs a reusable kind, a subkind comparison, a judgment about whether one exact candidate satisfies one kind, or an optional representation of the candidates that satisfy it in one exact context slice. A kind may be used locally without receiving its own public `U.*` name; “local” describes the bounded use, not an identity component.

**What goes wrong if missed.** A source type, practice label, programming class, schema label, mathematical set, or public `U.*` name starts doing several jobs at once. A source boundary splits one unchanged kind; several kinds inside one source collapse; the kind is confused with its declaration; evidence is treated as membership; a non-applicable request becomes `unknown`; or a current extension becomes ontology.

**What this buys.** A practitioner can recover the kind's membership distinction, the declaration used to classify, an admissibility result, one three-valued judgment when admissible, and any optional extension representation while leaving source provenance, direct world-side conditions, evidence, scope, Work, and public naming with their own patterns.

**Primary EntityOfConcern.** One typed-reasoning question: the exact `U.Kind` individual, its intended candidate domain and membership distinction, any `U.SubkindOf` comparison needed by the claim, and the C.3.2 candidate question the use actually asks. The exact `KindSignature` edition carries the effective `U.ReferenceScheme` in its claim content; the scheme and practice/source provenance are not stored on the kind.

**First useful move.** Write the ordinary conclusion first. For example: `Pump #14 counts as a cooling pump in this plant slice because it satisfies the declared cooling-pump condition.` Add a reusable declaration, admissibility detail, explicit judgment, support reference, or extension representation only when a named receiving use needs it.

**Not this pattern when.** Use `E.24.UK` when the question is admission of another durable public FPF U-kind. Use the direct subject pattern when the question is whether a physical quality, relation, registration, certification, publication occurrence, Work, or other governed condition obtains. Use `A.2.6` for claim, work, or publication scope and `C.29` for a claim-bearing mathematical representation.

### C.3:1 - Problem Frame

`U.Kind` is the admitted meta-kind whose individuals are reusable intensional classification distinctions. One kind individual is recovered by its declared candidate domain, the membership condition that distinguishes intended members from non-members, and the continuity rule for a material declaration change. A `KindSignature` states that content for repeated use but is not the kind itself. A current extension can change while the kind continues, and two different intensional kinds can happen to classify the same current candidates.

A practice, source, team, or locality tells a reviewer where meaning may have changed. It does not decide kind identity. When a typed use moves, compare the exact membership distinctions. Reuse the same kind when the candidate domain and operative distinction continue. If they differ, identify two kinds; only then can C.3.3 ask whether an exact directional `KindBridge` obtains. When local wording or interpretation also differs, F.9 may relate the corresponding F.17 cells, but it neither creates the kinds nor maps a `U.ReferenceScheme` as a whole. A changed scheme creates another `KindSignature` edition; C.3.1 separately decides kind continuity. A changed `U.ContextSlice` alone creates neither a kind nor a bridge.

### C.3:2 - Problem

A project often needs classification before it needs another public ontology name. If the kind, its definition, the classified candidate, a record about the candidate, and a displayed set of current members are treated as one object, a label classifies by itself, evidence creates its subject, missing information proves non-membership, a table becomes an entity set, or a plan row becomes actual Work. If locality is made an identity key, the same kind also fragments across teams and sources. C.3 keeps each conclusion at its direct pattern.

### C.3:3 - Forces

| Force | Tension |
| --- | --- |
| Bounded typed use vs public ontology growth | A project needs typed claims now, but not every useful kind needs its own durable public `U.*` name. |
| Kind vs declaration | A kind can continue across compatible declaration editions without becoming identical to the episteme that declares its criterion. |
| Identity vs locality | A changed practice or source warns that the membership distinction may differ, but cannot prove sameness or difference. |
| Admissibility vs uncertainty | An ill-typed or out-of-applicability request must not look like an admissible candidate whose relevant facts are unsettled. |
| Condition vs evidentiary use | The governed condition named by the criterion makes membership hold; an item's use as evidence alone does not. The criterion may itself concern an episteme, status, or relation. |
| Extent vs ontology | A set of true members can serve a query without becoming a collection holon, entity-set kind, or direct classification relation. |
| Scope vs kind | A claim can have narrow scope without creating a narrower kind or storing scope on the kind. |
| Formal discipline vs ordinary use | Repeated typed use may need a declaration; one readable case should not require a card or extension table. |

### C.3:4 - Four Objects and a Pre-judgment Check

Keep these four objects separately recoverable:

| Object | Meaning | Subject pattern |
| --- | --- | --- |
| `U.Kind` individual and any `U.SubkindOf` facts | One intensional classification distinction, recovered through its candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. `U.SubkindOf` facts form a preorder; mutually obtaining facts state classification equivalence for the declared alignment and do not merge kind identities. | `C.3`, `C.3.1`, and accepted E.24.UK results for `U.Kind` and `U.SubkindOf` |
| `KindSignature` | One `U.Signature` declaration episteme whose exact EntityOfConcern is the kind and whose claim content declares candidate `ValueKind`, criterion, applicability, reference scheme, assumptions, dependencies, formality, and any current `ExtentRule`. | `C.3.2`, `A.6.0`, and `C.2.1` |
| classification judgment | One evaluation for an admissible exact candidate, kind, signature edition, and context slice with result `true`, `false`, or `unknown`. It is not a direct relation occurrence by default. | `C.3.2` |
| `KindExtension(k, slice)` | An optional set-valued representation of candidates whose admissible judgment is `true` for the fixed signature edition and slice. | `C.3.2`, with `C.29` when the representation changes a claim-bearing use |

Before the judgment, C.3.2 returns `admissible` or `not-applicable`. Candidate mismatch with the declared `ValueKind`, or a slice outside declared applicability, is `not-applicable` and no three-valued judgment is formed. Missing support or an unavailable dependency for an admissible candidate instead yields `unknown`.

Scope is not a fifth part of the kind. A `KindSignature` episteme may carry its own `U.ClaimScope`, and a separate classification assertion carries the scope of that assertion. The `U.ContextSlice` is an evaluation input.

### C.3:5 - Solution

Use the lightest object that answers the current typed-reasoning question.

1. **Recover the kind.** Name the candidate domain and the operative membership distinction: what an intended member must satisfy and what separates a relevant non-member. Record the continuity rule used when that distinction changes. Keep practice/source provenance as a cue to compare definitions, not as an automatic identity key. Do not store the current use, ClaimScope, context slice, or reference scheme on the kind.
2. **Use C.3.1 for subkind and continuity.** A `U.SubkindOf` fact obtains through exact criterion entailment under an aligned interpretation or through exhaustive evaluation over a deliberately closed finite domain. The facts form a preorder. Opposite facts between distinct kinds may express classification equivalence for that applicability; a consumer may order the resulting equivalence groups without identifying the kinds.
3. **Use C.3.2 for declaration and admissible judgment.** A repeated condition may justify a `KindSignature`. First check candidate `ValueKind` and applicability. Only an admissible application returns `true`, `false`, or `unknown`.
4. **Let the governed criterion condition decide.** A direct quality, relation, construction, episteme, registration, certification, publication occurrence, legal status, or other governed condition makes the criterion hold when the criterion actually names it. An observation, record, or source used merely as evidence does not constitute an independently governed condition. Use each condition's direct pattern.
5. **Keep four outcomes distinct.** `not-applicable` means the judgment should not be formed. For an admissible candidate, a satisfied criterion gives `true`, a known failed criterion gives `false`, and missing support or an unavailable required dependency gives `unknown`. A guard may decline use without rewriting any of these results.
6. **Materialize an extension only for use.** A query, quantification, comparison, or review may need `KindExtension(k, slice)`. It represents admissible candidates judged `true`; notation, rows, or set membership do not create an ontic collection or classification relation.
7. **Keep scope, formality, Work, and publication separate.** Formality characterizes the declaration episteme. Scope belongs to claims or capabilities. `U.Work` is a kind and `W : U.Work` is one independently grounded dated work occurrence. Plans, logs, cards, field bundles, carriers, and rows remain their own objects.

Typed reasoning composes with F-G-R and USM in this order: recover kind compatibility; check classification admissibility and, when admissible, the exact judgment; separately check claim-scope coverage; then apply support, assurance, freshness, and any justified bridge consequence required by the receiver.

### C.3:6 - Decision Split

| Current question | Subject pattern |
| --- | --- |
| What kind does this claim quantify over, and what makes it the same kind later? | `C.3` and `C.3.1`; use candidate domain, membership distinction, and continuity rule |
| Does one kind count as a subkind of another for this declared applicability? | `C.3.1`; distinguish criterion entailment, exhaustive closed-domain evaluation, classification equivalence, and kind identity |
| May this candidate be evaluated under this declaration and slice? | `C.3.2` admissibility; `not-applicable` forms no three-valued judgment |
| Does this admissible candidate satisfy this kind under this declaration edition and slice? | `C.3.2` returns `true`, `false`, or `unknown` |
| Does a receiving use need the represented set of true members? | `C.3.2`; `C.29` when the representation itself changes a claim-bearing use |
| Does the assertion hold in a target slice? | `A.2.6` for its `U.ClaimScope`; do not attach that scope to the kind |
| Did the practice, source, team, or other locality change? | Compare exact kind definitions. Reuse the same kind when its distinction continues. Use `C.3.3` only after two distinct kinds and a proposed correspondence are independently present |
| Did only the reference-scheme edition change? | `C.3.2` for another `KindSignature` edition and `C.3.1` for continuity and any renewed subkind test; the scheme is not a kind or relation-occurrence identity key |
| Did only the context slice change? | `C.3.2` for another applicability check, judgment input, and possible extension; the slice alone creates no bridge |
| Is this kind proposed as another durable public FPF `U.*` kind? | `E.24.UK`, followed by applicable naming patterns |
| Is a candidate, quality, relation, construction, episteme, status, publication occurrence, or Work being identified? | Its direct subject pattern; C.3 consumes that result and does not create it by classification notation |

When typed reasoning is part of a structural construction-to-representation passage from a constructive representation or working model to a target kind or logical representation, cite `StructuralCT2RTypingGroundingUnfoldingStructureBlock` from `B.3.5`. C.3 contributes only the kind, admissibility and judgment, subkind, and bridge loci inside that B.3.5-governed local `A.22.CGUS` specialization. It does not create separate unfolding-structure authority and does not make a constructive trace, working-model relation, proof, evidence relation, or classification true by label. For general diagnostic recovery from an inadequate working account to the exact subject construction, use `A.7.1`; classification remains one possible locus rather than a general ontology-return method.

The unfolding is admitted only when the block names the starting representation, target kind or logical representation, current bridge when one is used, preserved structure, lost or collapsed structure, `CL` or `CL^k`, admissible reuse, blocked substitution, and the proof or evidence subject pattern when that stronger claim is current.

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

C.3 counters lexical, locality, document, and ontology-growth bias. A familiar word, source label, or practice boundary supplies neither kind identity nor membership. A record used as evidence does not create an independently governed condition, while an episteme, status, or relation directly named by the criterion keeps its own governor. The kind/declaration/admissibility/judgment/extension split and the readable first move keep the remedy usable.

### C.3:9 - Conformance Checklist

| Check | Requirement |
| --- | --- |
| `CC-C3-1` | `U.Kind` and `U.SubkindOf` rely on exact accepted E.24.UK results; another public kind name still requires its own admission. |
| `CC-C3-2` | Kind, `KindSignature`, admissibility result, admissible three-valued judgment, and optional extension remain distinct; scheme and locality are not stored on the kind. |
| `CC-C3-3` | Kind identity is tested through candidate domain, membership distinction, intended member/non-member boundary, and continuity rule. A practice/source change is a comparison cue, not proof. |
| `CC-C3-4` | Candidate and slice applicability is checked before judgment; `not-applicable` is distinct from admissible `unknown`. |
| `CC-C3-5` | The governed condition named by the criterion decides membership. Evidentiary use alone does not constitute an independent condition, while directly criterion-bearing epistemes, statuses, and relations keep their own governors. |
| `CC-C3-6` | Subkind facts follow C.3.1's criterion-entailment or exhaustive closed-domain branch and form a preorder; classification equivalence does not merge kind identities. |
| `CC-C3-7` | Kind scope is absent; declaration and assertion scopes remain on their epistemes, and the slice remains an evaluation input. |
| `CC-C3-8` | An extension is a representation of admissible true candidates, not `U.EntitySet`, A.14 `MemberOf`, a collection holon, or a direct relation occurrence. |
| `CC-C3-9` | C.3.3 is used only after distinct kinds and a proposed correspondence are independently established; same-kind reuse still gets a fresh receiving judgment. |
| `CC-C3-10` | `U.Work`, exact `W : U.Work`, and any episteme about W remain distinct. |

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

**Costs.** Reliance-bearing uses must recover the kind distinction, pin the declaration and slice, check admissibility, and keep `not-applicable`, `false`, and `unknown` distinct.

**Risks avoided.** False sameness, implicit time, scope-on-kind, record ontology, accidental relation minting, kind/individual substitution, and mathematical-set overread are blocked at the first use.

### C.3:12 - Rationale

The kind, its declaration, pre-judgment admissibility, one classification judgment when admissible, and a representation of current true members answer different engineering questions and change for different reasons. Keeping them separate lets a kind continue across compatible declaration revisions, lets candidate state change an extension without changing the kind, and lets evidence or a guard change reliance without rewriting the world-side classification.

### C.3:13 - SoTA-Echoing

Model theory, type systems, ontology engineering, and schema practice distinguish intensional declarations, candidate evaluation, extensions, and assertion scope. C.3 adapts that separation to FPF's object discipline: declaration epistemes follow `A.6.0` and `C.2.1`, context slices and claim scope follow `A.2.6`, mathematical representations follow `C.29`, and durable kind admission follows `E.24.UK`.

### C.3:14 - Detail Map
C.3 is the head pattern for typed reasoning. It leaves each detailed mechanism at its direct neighboring pattern while preserving a discoverable route to that mechanism.

| Needed detail | Direct locus | Content carried there |
| --- | --- | --- |
| Kind identity, subkind relation, and continuity | `C.3.1` | admitted `U.Kind` and `U.SubkindOf`, criterion-entailment or exhaustive closed-domain obtaining, preorder and classification equivalence, participant-determined relation identity, and operational before/after continuity. |
| Declaration, candidate judgment, and extension | `C.3.2` | `KindSignature`, exact four-key judgment, `true`/`false`/`unknown`, optional `KindExtension`, and scope/formality/evidence boundaries. |
| Cross-local kind use | `C.3.3` | identity comparison first; same-kind reuse without a bridge; for distinct kinds, an obtaining directional `KindBridge`, its separate assertion, preservation/loss, and a fresh admissible receiving judgment. |
| Local adaptation without cloning a kind | `C.3.4` | A `KindUseAdaptationDeclaration` for one named local use of an exact base kind, its pinned base-kind judgment and additional candidate-feature constraints, the exact three-valued `KindUseAdaptationJudgment`, and any separately declared `KindUseAdaptationCorrespondenceDeclaration` between two exact adaptation declarations. |
| Abstraction facet | `C.3.5` | `KindAT` as an editorial planning facet on one exact local kind, with no effect on the kind, declaration, judgment, extension, bridge assessment, guard, or F–G–R. |
| Typed guards and applied examples | `C.3.A` | Declaration-level kind compatibility and exact candidate-use judgments kept separate across regulatory, assurance, ESG, and Method–Work uses, including the independently grounded actual `W : U.Work` boundary. |

Do not treat this compact head pattern as the whole C.3 discipline when a case needs declaration, classification, extension, Bridge, kind-use adaptation, abstraction, or applied-guard detail. Use the neighboring C.3 pattern that defines or constrains the live detail.

### C.3:15 - Relations

- **Builds on:** `A.2.6` context-slice and scope discipline, `A.6.0` reusable declaration discipline, `C.2.1` episteme identity, F-G-R, and direct subject patterns for candidate features.
- **Coordinates with:** `C.3.1` through `C.3.5`, `C.3.A`, `C.29`, `E.24.UK`, `A.8`, `A.11`, `F.8`, `F.18`, and generic `A.22.CGUS` when typed reasoning is one locus in an admitted unfolding structure; coordinates with `StructuralCT2RTypingGroundingUnfoldingStructureBlock` only when C.3 supplies local-kind, judgment, subkind, and bridge loci inside a structural construction-to-typed or logical projection, with any cross-local bridge remaining a bridge within that projection rather than an alternative trigger; coordinates with `A.7.1` for a general diagnostic return.
- **Does not replace:** direct candidate-feature ontology, A.14 collection membership, `A.2.6` scope, `C.29` representation use, ontic settlement in `E.24`, U-kind admission in `E.24.UK`, or naming in Part F.

### C.3:End

