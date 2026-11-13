## A.19.SOURCE-SET-SPACE-SUBSTRATE - Source-Set and Search/Outcome-Space Substrate

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Source-set / search-outcome-space substrate.

**Working contribution.** Identify the set being searched or compared, the space used to describe its members, and the space in which their outcomes are judged. State the relation that connects source members to outcome values and the limits of that relation. Search and outcome may use the same A.19 space; the two uses still need to remain distinguishable.

### A.19.SOURCE-SET-SPACE-SUBSTRATE:0 - Use this when

Use this pattern when one working line depends on all of the following at once:

- one declared source set or composition of source sets still matters and must stay recoverable;
- one search-side space reference and one outcome-side space reference must both be explicit;
- the line must say whether those refs resolve to one declared `CharacteristicSpace` or to two distinct declared `CharacteristicSpace` values;
- the reader must know what the source-to-outcome relation connects, in which direction, and through which declared carrier, declared map ref, or qualifier ref;
- distortion, uncertainty, or error must be specified.

This is the right pattern for QD, OEE, archive/front, or adjacent synthesis lines when the problem is no longer only "what space exists?" and not yet "what shortlist or shipped result do we publish?".

Not this pattern when:

- you only need to declare or compare `CharacteristicSpace` itself, with no source-set or source-to-outcome requirement; use `A.19`;
- you are publishing selector or shipping metadata such as `SelectorOutcomeKind`, `SetResultFamily`, `HandoffKind`, or public shortlist identity; use `G.5` or `G.10`;
- you are building one interpretive view over an already-declared substrate; use `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` or a local specialization such as `G.2`;
- you are deciding live pool policy, frontier retention, or next-move planning; use `C.19` or `C.24`.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:0.1 - What goes wrong if missed

If this pattern is missed, authors usually collapse several different things into one vague "space" or one vague "projection":

- the declared source set disappears behind bare words such as `front`, `archive`, `palette`, or `portfolio`;
- `SearchSpaceRef` and `OutcomeSpaceRef` never become explicit, or `SpaceRefRelationKind` never becomes explicit, so one line hides whether search and outcome use one declared space twice or two different declared spaces;
- `DescriptorMapRef` or `DistanceDefRef` gets mistaken for the space itself rather than one representation or metric qualifier;
- publication metadata in `G.5` or `G.10` starts standing in for substrate semantics;
- and distortion, uncertainty, or error is either hidden or treated as if every non-trivial case were only one bridge-loss story.

The result looks tidy, but the reader cannot tell what is being searched, what is being evaluated, what is only being published, and where uncertainty enters.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:0.2 - What this buys

This pattern buys one conservative but expressive substrate declaration:

- the source set stays visible;
- the search-side and outcome-side references over `A.19` spaces stay distinct;
- the relation between those refs becomes inspectable instead of being hidden in one overloaded noun or verb;
- heavier qualifier refs remain available without being forced into every case;
- and interpretive-view or publication neighbors can reuse the substrate without changing what it means.

The practical payoff: readers can tell what the line is acting on, what relation between the two space refs it assumes, what kind of qualification they must keep in view, and which neighboring pattern governs the next use or action if that requirement grows.

### A.19.SOURCE-SET-SPACE-SUBSTRATE:0.a - TERM/LEX token-status guard (local-first)

Keep this token-status split explicit:

- `CharacteristicSpace` is the reused `A.19` kind. This pattern does not mint a second space kind.
- `SearchSpaceRef` and `OutcomeSpaceRef` are role-named local fields whose slot content is typed by the existing `CharacteristicSpaceRef` / `SpaceRef` idiom. They are not new heads, not slot aliases inside the space, and not `U.Role` claims. In source-set/space-substrate or typed-set-view passages, read them as role-specific refinements of that older `SpaceRef` idiom rather than collapsing the roles back into one umbrella `SpaceRef`.
- `SpaceRefRelationKind` is a local relation-kind field over those two refs. In this pattern, `sameDeclaredSpaceAs` and `distinctDeclaredSpaceFrom` are controlled token values for that field, not free prose.
- `SourceToOutcomeRelation` and `DistortionPosture` are local declaration fields. Their field names do not by themselves create one new generic ontology; the declaration requirement is satisfied only when their payload is explicit enough to audit.
- `SourceSetFamily`, `SourceSetComposition`, and `DerivedViewKind` are local fields in this `SourceSetSpaceSubstrate` declaration. Their use as fields does not establish a new object kind.
- `BasePaletteRef`, `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, `BridgeDistortionNote`, `DescriptorMapRef`, and `DistanceDefRef` are neighboring refs or interpretive qualifiers reused here. This pattern may cite them, but it does not redefine them.
- `carrier` inside `SourceToOutcomeRelation` identifies the relation definition, map, model or operation that supplies the connection. Its definition can be stated or cited where the reader can recover it. A containing paragraph expresses that definition; the physical or digital entity bearing that text is identified separately under E.24.PUB.

### A.19.SOURCE-SET-SPACE-SUBSTRATE:0.b - First-minute operator cue and confusion guide

When the receiving use depends on the source set, search space and outcome space together, recover the following facts from the existing account. Add only what is missing; an adequate paragraph or model declaration needs no duplicate form.

First recover:

1. Name the source set, or the contributing source sets and their composition.
2. Point `SearchSpaceRef` and `OutcomeSpaceRef` to declared `CharacteristicSpace`.
3. Choose `sameDeclaredSpaceAs` or `distinctDeclaredSpaceFrom`.
4. State the source-to-outcome relation in direction, mode, and carrier.
5. State the applicable limitations. A primary posture token may organize them; supply it when a selected interface requires one, without hiding other material qualifications.

If one of these facts cannot yet be recovered, preserve the established source and space facts, name the missing basis, and withhold the complete substrate claim and only the use that depends on that basis. Use the applicable subject pattern when it can supply the missing result.

| If the question under repair sounds like... | Use now | Why |
| --- | --- | --- |
| "Which space are we searching in and which space are we judging in?" | `A.19.SOURCE-SET-SPACE-SUBSTRATE` | This pattern governs the dual-ref substrate stack. |
| "How should I help the reader inspect that already-declared line?" | `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` | That is one interpretive reading over the substrate, not the substrate declaration itself. |
| "What do we publish, ship, keep live, or plan next?" | `G.5`, `G.10`, `C.19`, or `C.24` | Those are downstream output or policy questions. |
| "I only need one space declaration." | `A.19` | No source-to-outcome substrate stack is in play yet. |

A descriptor map or distance definition supplies one part of this account; it does not identify the source set and both spaces by itself.

### A.19.SOURCE-SET-SPACE-SUBSTRATE:1 - Problem frame

In many search, synthesis, and source-set/space-substrate lines, the substrate-bearing line is not just one `CharacteristicSpace` and not just one published shortlist or archive either. The line depends on a stack such as:

- one declared source set, such as a front, archive or palette, or a composition of identified source sets;
- one search-side reference to an `A.19` `CharacteristicSpace`;
- one outcome-side reference to an `A.19` `CharacteristicSpace`;
- one `SpaceRefRelationKind` over those two references, stating whether they resolve to the same declared space or to two different declared spaces;
- one relation from the source-side line into the outcome-side line;
- and one declared posture about whether that relation is transparent, approximate, learned, lossy, uncertain, or otherwise qualified.

Without a substrate declaration for that stack, nearby declarations start carrying loads they are not meant to carry. `A.19` gets stretched from space typing into source-set governance. `C.18` descriptor maps start masquerading as the whole search space. `G.5` and `G.10` publication fields start reading like ontology. Interpretive views or atlas views drift into default meaning instead of staying optional derived help.

### A.19.SOURCE-SET-SPACE-SUBSTRATE:2 - Problem

How should one declare a source-set and search/outcome-space line so that:

1. the declared source set remains explicit and recoverable;
2. `SearchSpaceRef` and `OutcomeSpaceRef` stay refs to declared `A.19` `CharacteristicSpace`, not new free-floating space kinds;
3. the text states whether those refs point to one declared space or to two distinct declared spaces;
4. the source-to-outcome relation is explicit enough for the reader to know which source-to-outcome relation mode is being claimed: mapped, projected, translated, scored, or otherwise connected;
5. distortion, uncertainty, and error are stated rather than hidden in prose;
6. `SourceSetComposition` and `DerivedViewKind` remain conditional fields rather than fabricated mandatory baggage;
7. qualifier refs such as `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, and `BridgeDistortionNote` remain available but substrate-side only;
8. and neighboring declarations such as `A.19`, `C.18`, `G.5`, `G.10`, and `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` can dock to the substrate without redefining it?

### A.19.SOURCE-SET-SPACE-SUBSTRATE:3 - Forces

| Force | Tension |
| --- | --- |
| `A.19` typing vs adjacent substrate requirement | `A.19` already declares `CharacteristicSpace`, but source-set and publication-form semantics still need a separate substrate declaration. |
| Precision vs over-typing | The line needs to state its ref positions, ref-to-ref relation kind, and relation posture, but it should not fabricate composition, derivation, metrics, or transition qualifier when the case does not need them. |
| Reuse vs semantic collapse | `DescriptorMapRef`, `DistanceDefRef`, `OutcomeMapRef`, or `BridgeDistortionNote` are useful qualifiers, but they must not silently become the whole substrate. |
| User readability vs architectural honesty | Cold readers need a first-minute explanation, while specialist readers still need boundaries and docking rules. |
| Interpretive views vs substrate core | Atlas or interpretive-view lines can be valuable, but they should remain optional derived help rather than the default meaning of the substrate. |
| Uncertainty honesty vs fake closure | Many current lines use learned, adaptive, unstructured, or distribution-valued spaces or relations; the pattern must expose that posture without pretending the heaviest qualification posture is already settled. |

### A.19.SOURCE-SET-SPACE-SUBSTRATE:4 - Solution

Declare the source-set or search/outcome-space line through one substrate stack, keep only the core mandatory, and place every other requirement in conditional fields, interpretive qualifiers, or companion declarations.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.1 - Declared relation-and-ref-position stack and outside work

Use this pattern to declare only the substrate stack below:

- the source set, or composition of source sets, used by the search or comparison;
- the recoverable source-set identity when the family name alone would be ambiguous;
- the search-side reference to one declared `A.19` `CharacteristicSpace`;
- the outcome-side reference to one declared `A.19` `CharacteristicSpace`;
- the `SpaceRefRelationKind` over those two ref positions;
- the source-to-outcome relation;
- and the distortion, uncertainty, or error posture for that relation.

Do not use this pattern to declare:

- `A.19` space typing itself;
- selector outcome publication, shortlist identity, or shipping closure;
- live pool policy or enactment planning;
- or optional interpretive-view families that interpret or reorganize an already-declared substrate.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.2 - Minimal declaration stack

Use the following notation-independent stack:

```text
SourceSetSpaceSubstrate := <
  SourceSetFamily?,
  SourceSetRef?,
  SearchSpaceRef,
  OutcomeSpaceRef,
  SpaceRefRelationKind,
  SourceToOutcomeRelation,
  DistortionPosture,
  SourceSetComposition?,
  DerivedViewKind?,
  BasePaletteRef?,
  OutcomeMapRef?,
  SpaceMetricRef?,
  TransitionRelationRef?,
  BridgeDistortionNote?
>
```

Interpret the fields as follows:

- `SourceSetFamily?` names the declared family of the immediate source set and is required for a single-source account. For a composition without a distinguished source, `SourceSetComposition` supplies the source basis by identifying each contributing source, its family and member contribution rule. If the receiving use singles out a primary source, identify that source and retain its family in `SourceSetFamily`.
- `SourceSetRef?` names the declared source set or set result when its identity would otherwise be ambiguous, including when a neighboring governing pattern supplies that identity. For a composition, recover each contributing set through `SourceSetComposition`; add a separate `SourceSetRef` when the receiving use also depends on the identity of a combined set result. A reference may be omitted only when its intended set is otherwise unambiguous.
- `SearchSpaceRef` points to one declared `A.19` `CharacteristicSpace` in the search-side position.
- `OutcomeSpaceRef` points to one declared `A.19` `CharacteristicSpace` in the outcome-side position.
- `SpaceRefRelationKind` states how those two refs relate. In ordinary use, the token is either `sameDeclaredSpaceAs` or `distinctDeclaredSpaceFrom`.
- `SourceToOutcomeRelation` identifies the source members or values, target outcome values, direction and relation mode, with the defining map, model, operation or rule in `carrier`. The mode distinguishes a description, projection, prediction, scoring relation or other declared connection; naming it does not establish that its output is accurate or suitable for a receiving use.
- `DistortionPosture` states the conditions and limits needed by the receiving use. A primary token may organize this account or satisfy a selected interface requirement. It does not make the qualifications mutually exclusive: a learned map may also be uncertain and model-dependent. The local tokens include `transparent-for-current-use`, `lossy-bridge`, `metric/model-dependent`, `transition-dependent`, `uncertainty-bearing`, `learned/adaptive`, and `unstable-under-refresh`.
- `SourceSetComposition`, `DerivedViewKind`, and related `...Kind` values remain declaration fields or controlled field values unless some governing pattern promotes them; they are not automatically independent heads merely because their names end with `Kind`.

The two reference fields designate A.19 spaces. `SpaceRefRelationKind` reports whether their resolved values are the same or distinct under A.19 meaning. Two identifiers or declaration documents may describe the same space; different spellings alone establish no distinction. Recover a changed basis, Scale meaning or other space-defining content before asserting distinctness. This local token field is not itself an A.6.5 reusable relation-kind declaration.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.3 - Substrate declaration laws (SS-0..SS-7)

**SS-0 - One substrate line, one stack.**
Treat a line as declared substrate only if one recoverable source-set basis, two recoverable space refs, one explicit ref-to-ref relation kind, one explicit source-to-outcome relation, and one explicit posture are present together.

**SS-1 - Ref typing is preserved.**
`SearchSpaceRef` and `OutcomeSpaceRef` must resolve to declared `A.19` `CharacteristicSpace`. They do not become parallel space kinds, slot aliases, or role claims.

**SS-2 - Source-set recoverability is mandatory.**
The reader must be able to recover the source set and its declared family. For a composition, recover every contributing set, its family and its member contribution rule; identify a primary source only when the receiving use distinguishes one. Use `SourceSetRef`, `SourceSetComposition` or an accessible source that uniquely supplies the needed identities. A family name alone does not resolve several same-family sources.

**SS-3 - Relation requirement must be explicit.**
`SourceToOutcomeRelation` is conforming when its participants, direction, mode and defining map, model, operation or rule are recoverable. Add an interpretive qualifier only when it changes that relation's use.

**SS-4 - Posture honesty is mandatory.**
`DistortionPosture` must say whether the line is transparent for current use or qualified by loss, metric/model dependence, transition dependence, uncertainty, learning/adaptation, or instability under refresh. State all material qualifications, even when one primary token is used for indexing. A token alone supplies no error bound, validation result or permission to rely on the outcome.

**SS-5 - Conditional and qualifier fields stay subordinate.**
`SourceSetComposition`, `DerivedViewKind`, `BasePaletteRef`, `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, and `BridgeDistortionNote` may clarify the substrate, but they do not replace the core stack and do not become mandatory everywhere.

**SS-6 - Publication and policy stay outside.**
Publication metadata, shortlist identity, live-pool policy, and enactment policy remain neighboring decisions. A substrate line may feed them, but it does not decide them.

**SS-7 - Admission is fail-closed.**
If the source basis cannot be recovered, either space ref is unresolved, `SpaceRefRelationKind` cannot be chosen, relation direction, mode or carrier remains vague, or a qualification needed by the receiving use is unresolved, then the complete substrate claim is not established. Preserve the recovered source and space facts, state the missing basis and withhold only the use that depends on it. Use the applicable subject pattern when it can supply the missing result.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.4 - Profiles

Use one of these ordinary profiles:

- **Shared-space profile.**
  `SearchSpaceRef` and `OutcomeSpaceRef` both resolve to the same declared `CharacteristicSpace`, and `SpaceRefRelationKind = sameDeclaredSpaceAs`.
- **Cross-space profile.**
  `SearchSpaceRef` and `OutcomeSpaceRef` resolve to two distinct declared `CharacteristicSpace` values, and `SpaceRefRelationKind = distinctDeclaredSpaceFrom`.
- **Derived-source supplement.**
  If the visible source set is derived, make the derivation recoverable. Use `DerivedViewKind` and `BasePaletteRef` when the receiving use needs that derivation or would otherwise lose the base palette, as §4.7 specifies.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.5 - Operational declaration sequence (fail-closed)

When declaring one substrate-bearing line, proceed in this order:

0. **Entry test.** Confirm that the line needs source-set plus search/outcome-space plus relation/posture discipline. If it only needs `CharacteristicSpace` typing, use `A.19`. If it only needs publication or policy, apply the governing pattern that carries that publication or policy question.
1. **Recover the source basis.** For one immediate source set, state its family and recover its identity. For a composition, use `SourceSetComposition` to identify every contributing set, its family and how its members contribute; designate a primary source only when the receiving use singles one out. Add `SourceSetRef` or cite a source when needed to make an identity unique.
2. **Recover the space refs.** Point `SearchSpaceRef` and `OutcomeSpaceRef` to already-declared `CharacteristicSpace`.
3. **Choose the ref-to-ref relation kind.** Declare `sameDeclaredSpaceAs` when both references resolve to the same A.19 space by value, and `distinctDeclaredSpaceFrom` when their defining contents establish distinct values. If that identity question is unresolved, retain the uncertainty rather than inferring difference from two declarations.
4. **State the source-to-outcome relation.** Give direction, mode, and carrier. If one named `OutcomeMapRef` or another declared interpretive qualifier carries the relation, cite that qualifier. Otherwise state the relation definition or supplying operation in prose.
5. **State the qualifications.** Identify the loss, model or metric dependence, transition dependence, uncertainty, adaptation or refresh limit that affects the use. A transparency claim needs a basis. Retain every material condition; use a primary token when useful for indexing or required by a selected interface.
6. **Add only needed fields.** Add composition, derived-view, base-palette, metric, transition, or bridge qualifiers only when the case depends on them.
7. **Run the boundary check.** If the line starts deciding publication metadata, shortlist identity, live candidate policy, enactment policy, or interpretive-view organization, stop and apply the pattern that governs that question.

**Incomplete-account result.** An unresolved requirement in steps 1-5 leaves the complete substrate claim unestablished. Apply SS-7: preserve what is known and withhold only uses that require the missing basis. A declared uncertainty is a qualification to preserve, not by itself a failure to identify the substrate.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.6 - Canonical rewrite forms

The §4.2 schema can express either profile: both space references may resolve to the same A.19 value or to distinct values. Use a block, prose or an existing model account that makes the source, spaces, relation and limitations recoverable. A new block is not required when that content is already sufficient.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.7 - Conditional fields stay conditional

Use `SourceSetComposition` when the account consumes several declared source sets. Identify each contributing set and its family, and state how its members enter the source basis, such as a union or specified subsets when that is the construction.

For a single immediate source, `SourceSetFamily` remains required. For a composition, retain a primary source and its family only when the receiving use distinguishes one. Otherwise the recoverable composition supplies the source basis without inventing a primary family. Neither branch silently changes any contributing set's identity or family.

For example, a comparison may consume the union of declared `Front-F` and `Archive-A` without privileging either. `SourceSetComposition` identifies both sets, their families and the union. No primary `SourceSetFamily` is required; both space refs and the source-to-outcome rule apply to that declared source basis.

Use `DerivedViewKind` only when one derived view is active and the reader must be able to recover that derivation.

Use `BasePaletteRef` only when a derived tradition or palette view would otherwise hide the recoverable base palette.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.8 - Qualifier refs stay substrate-side

`OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, and `BridgeDistortionNote` are admitted as substrate-side qualifier refs.

Use them when:

- one `OutcomeMapRef` or named declared map ref disciplines the source-to-outcome relation;
- one metric disciplines spread, neighborhood, or comparison claims;
- one `TransitionRelationRef` disciplines dynamic coupling or transfer;
- or one bridge-loss note is the reason the relation is qualified.

These qualifiers help explain the relation. They do not replace the recoverable source basis, the search-side and outcome-side spaces, or the declared relation and its applicable limitations. The source basis may be one set or the composition described in §4.7.

The substrate cites the qualifier definition on which it relies. A later view may introduce its own representational qualification; distinguish that view claim from a change to the source-to-outcome relation. If the underlying relation changes, revise its declaration and recheck dependent uses.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.9 - Descriptor maps and distance definitions dock here, but do not replace the space refs

When a neighboring line already uses `DescriptorMapRef` or `DistanceDefRef`, dock it:

- `DescriptorMapRef` may realize or qualify the search-side or outcome-side representation requirement, as the current line requires;
- `DistanceDefRef` may realize or qualify the metric requirement over that representation on either side, as the current line requires;
- but neither one replaces `SearchSpaceRef` or `OutcomeSpaceRef`;
- and `CharacteristicSpace` remains a different kind from `DescriptorMap`.

Use this docking rule whenever a reader could otherwise mistake one local representation layer for the whole search-side or outcome-side space reference.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.10 - Publication and shipping remain downstream consumers

`G.5` and `G.10` may carry metadata such as `SelectorOutcomeKind`, `SetResultFamily`, `SourceSetFamily`, `SourceSetComposition`, `DerivedViewKind`, and `BasePaletteRef` when one selected or shipped result is being published.

That does not mean `G.5` or `G.10` defines the substrate.

Read the boundary this way:

- this pattern defines the substrate that later publication must preserve;
- `G.5` publishes selector-facing outcome metadata;
- `G.10` ships publication metadata and pins;
- neither one redefines the search-side reference, the outcome-side reference, or the source-to-outcome relation.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.11 - Ordinary and heavier use

Stop with the source set, both resolved spaces, their same/distinct relation, the source-to-outcome connection and its applicable limits. Add composition, derivation, map, metric, transition or Bridge detail only when it changes the receiving use. A later view or publication can reuse this account without copying it into another declaration.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:4.13 - Using the substrate with neighboring patterns

Once the substrate is declared, select the neighboring pattern for the remaining question:

- Use `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` when the next requirement is interpretive help over the same substrate. The interpretive view may foreground the line, but it does not become the ontology.
- Use `G.2` when that interpretation becomes palette-first, tradition-facing atlas work. Keep the base palette and the cited substrate recoverable while doing it.
- Use `A.6.P` when one passage collapses source set, space ref, interpretive view, atlas view, or map/ref wording into one umbrella word. Repair the wording back to the substrate declaration before adding more theory.
- Use `F.18` when the problem is label choice or naming-side comparison around this stack. Naming notes may explain why one head is better named; they do not settle the substrate relation.
- Use `A.0` when the task is cold-reader glossing of these tokens. Glosses explain the terms; the source, spaces, relation and limitations required by §4.2 must still be recoverable from the account.

If a neighboring use needs a changed source-to-outcome relation or qualification, revise the declaration and reconsider the conclusions that depend on the change. Reuse unaffected content.

### A.19.SOURCE-SET-SPACE-SUBSTRATE:5 - Archetypal Grounding

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:5.1 - System

One QD line keeps saying that one archive is both the search-side role and the evaluation basis. Downstream readers need to see that the same declared `CharacteristicSpace` can still occupy two different role positions without turning the archive or the descriptor layer into the space itself.

In this constructed case, `Archive-12` is the selected candidate set. The declared descriptor map assigns behavior Coordinates to its members; the separately declared neighborhood metric is used to assess coverage in that same behavior space.

```text
SourceSetFamily       = Archive
SourceSetRef          = Archive-12
SearchSpaceRef          = BehaviorCharacteristicSpace@ed=12
OutcomeSpaceRef         = BehaviorCharacteristicSpace@ed=12
SpaceRefRelationKind    = sameDeclaredSpaceAs
SourceToOutcomeRelation = QDDescriptorMap@ed=9 assigns each Archive-12 candidate
                          its Coordinates in BehaviorCharacteristicSpace@ed=12;
                          a coverage comparison uses ArchiveNeighborhoodMetric@ed=4
                          on those Coordinates
DistortionPosture       = metric/model-dependent; descriptor realization and
                          neighborhood metric qualifier are active
DescriptorMapRef        = QDDescriptorMap@ed=9
DistanceDefRef          = ArchiveNeighborhoodDistance@ed=4
SpaceMetricRef          = ArchiveNeighborhoodMetric@ed=4
```

The archive supplies the candidate members; both space references resolve to the same declared `CharacteristicSpace`. The descriptor map assigns Coordinates, and the distance and metric define the stated coverage comparison. Selection or archive maintenance can reuse these relations while keeping the archive distinct from the space.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:5.2 - Episteme

One synthesis line presents one derived tradition front and then starts speaking as if the visible front were the default meaning of the whole palette.


```text
SourceSetFamily        = Front
DerivedViewKind        = TraditionFront
BasePaletteRef         = SoTAPaletteDescriptionId
SearchSpaceRef         = TraditionComparisonSpace@ed=3
OutcomeSpaceRef        = AdoptionOutcomeSpace@ed=2
SpaceRefRelationKind   = distinctDeclaredSpaceFrom
SourceToOutcomeRelation = for each retained tradition profile, AdoptionEstimate@ed=1
                          uses its integration requirements and the named team's
                          capability and workload facts to estimate adoption cost
                          and expected benefit in AdoptionOutcomeSpace@ed=2
DistortionPosture      = metric/model-dependent; the estimate is conditional on those
                         team and workload facts and omits unmodelled adoption effects
```

The visible front stays a derived view over the recoverable palette. `AdoptionEstimate@ed=1` supplies the stated conditional source-to-outcome mapping. A later interpretive or atlas view may reorganize the presentation while preserving that mapping and its model limitations.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:5.3 - Boundary anti-case

One note says only that "the shortlist front is the published result for the current selector result" and names no source-to-outcome relation, no search-side space, no outcome-side space, and no posture.

This is not a substrate declaration. It is publication metadata over one already-selected set.

Apply `G.5` or `G.10` to that note.

#### A.19.SOURCE-SET-SPACE-SUBSTRATE:5.4 - Use-situation spread

Use the pattern this way across different working situations:

| Working situation | What to do with this pattern | What must stay explicit | Common miss avoided |
| --- | --- | --- | --- |
| Archive-side QD line where navigation and evaluation stay in one declared behavior space | Use the shared-space profile. Recover the source basis, both space uses, their same-space relation, the source-to-outcome connection and its limitations; add descriptor/metric qualifiers when used. | The archive as source set, both role-refs, the same declared space and applicable qualifications. | Treating the archive or descriptor layer as if it were the space itself. |
| Derived tradition/front line that is judged against one different outcome space | Use the cross-space profile. Keep the derivation and base palette recoverable where the receiving use depends on them; add `DerivedViewKind` and `BasePaletteRef` when needed or required by its selected publication contract. | The derived view stays derived, the needed base palette remains recoverable, and the cross-space relation stays explicit. | Letting the visible front replace the base palette or hiding the adoption model's limitations. |
| Learned, adaptive, or uncertainty-bearing line where the space is declared but heavier qualification remains case-bound | Keep the substrate core recoverable and state the uncertainty, adaptation or refresh conditions that affect the receiving use. Add a posture token when the selected interface requires it. | The reader can distinguish the declared substrate from unresolved accuracy, applicability or stability claims. | Pretending every case is either fully transparent or fully described by one metric stack. |
| Shortlist or publication note that only says what set result or publication form is shown or shipped | Do not use this pattern. Apply `G.5` or `G.10`. | The note stays publication-facing instead of imitating substrate depth. | Padding publication metadata with pseudo-substrate language. |

### A.19.SOURCE-SET-SPACE-SUBSTRATE:6 - Bias-Annotation

- **Gov bias.** The pattern prefers explicit declaration over convenient shorthand.
- **Arch bias.** The pattern keeps substrate, interpretive view, and publication consumers separated even when one merged story would read more smoothly.
- **Prag bias.** The pattern prefers a short substrate declaration that can be reused across search, synthesis, and publication-adjacent lines.
- **Qualification bias.** Learned or adaptive relations need their applicable uncertainty and model limits. A metric or transition model is added only when the claim uses it.

### A.19.SOURCE-SET-SPACE-SUBSTRATE:7 - Conformance Checklist

Apply these declaration checks to the claims and qualifiers used:

| ID | Check question | Fail when | Repair or governing pattern |
| --- | --- | --- | --- |
| `CC-A19SS-1` | Is the line declaring one substrate-bearing relation rather than only `CharacteristicSpace`, publication metadata, or policy? | The line only names a space object, or only publishes, ships, or retains something, with no explicit source, ref, relation, or posture stack. | Move to `A.19`, `G.5`, `G.10`, `C.19`, or `C.24` as appropriate. |
| `CC-A19SS-2` | Is the source basis recoverable for the case? | A contributing set, its family or its member contribution rule is ambiguous, or a primary source is invented for a composition that distinguishes none. | Recover each set identity and family and any composition under §4.7; use refs or accessible defining sources as needed. |
| `CC-A19SS-3` | Do `SearchSpaceRef` and `OutcomeSpaceRef` both resolve to declared `A.19` `CharacteristicSpace`, and is `SpaceRefRelationKind` explicit? | One or both refs are vague, or the line leaves the same-space versus cross-space question to inference. | Restore the two refs and declare `sameDeclaredSpaceAs` or `distinctDeclaredSpaceFrom`. |
| `CC-A19SS-4` | Is the source-to-outcome relation explicit in its participants, direction, mode and defining basis? | The relation remains hidden in an umbrella phrase with no recoverable map, model, operation or rule. | State the participants, direction, mode and defining basis or cite where they can be recovered. |
| `CC-A19SS-5` | Are the relevant qualifications explicit and supported for the claimed use? | Material limits are missing, or different qualified cases are blurred into one generic loss story. | State the qualifications and the basis needed by that use. If needed support is missing, retain the established content and withhold only the dependent conclusion; a primary token is required only by a selected interface. |
| `CC-A19SS-6` | Are conditional and qualifier fields used only when they do work? | Composition, derivation, base-palette, declared map ref, metric, transition, or bridge qualifiers are fabricated everywhere or silently become core. | Remove unused qualifiers; keep only the fields the case depends on. |
| `CC-A19SS-7` | If `DescriptorMapRef` or `DistanceDefRef` is active, does the text say they realize or qualify the relation rather than replace the space ref? | The representation or metric layer is treated as if it were the declared search-side or outcome-side space. | Re-state the docking rule and keep the two space refs visible. |
| `CC-A19SS-8` | Does the line stay out of publication and policy work? | The prose starts deciding shortlist identity, selector outcome, shipping closure, or live-pool/enactment policy. | Split the line and move those downstream decisions to their governing patterns. |
| `CC-A19SS-9` | Can the account establish the substrate claim needed by the use without inventing facts? | A required source identity, space resolution, relation or material qualification remains unsupported. | Return the recovered components and the missing basis; withhold the complete claim and only uses that depend on that gap. |
| `CC-A19SS-10` | Could a cold reader take the next declaration step from this line without surrounding memo help? | The line still speaks only in umbrella words such as `space`, `projection`, or `portfolio`, and the reader cannot tell what to fill next. | Use the declaration sequence in §4.5 and recover the needed content from §4.2 before reuse. |
| `CC-A19SS-11` | When the next question is interpretive-view, publication, or policy, is the next governing pattern explicit? | The text keeps talking as if substrate, interpretation, publication, and policy were one layer, so the reader cannot tell where to continue. | Split the line and cite `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW`, `G.5`, `G.10`, `C.19`, or `C.24` as the next governing pattern. |
| `CC-A19SS-12` | Does the use claim only the breadth its declared posture and qualifiers license? | The prose implies universal geometric closure or one universal heavy-qualification story, but the declared posture or qualifiers stay narrower, uncertain, learned/adaptive, or case-bound. | Narrow the claim or add the missing posture/interpretive qualifiers that make the broader claim honest. |

### A.19.SOURCE-SET-SPACE-SUBSTRATE:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Treating one archive or front as the search space itself | A source set is not the same kind as one declared `CharacteristicSpace`. | Keep the source-set identity and family, or its composition, separate from `SearchSpaceRef`. |
| Leaving `SpaceRefRelationKind` implicit | The reader then has to guess whether search and outcome share one declared space or use two distinct declared spaces. | Declare `sameDeclaredSpaceAs` or `distinctDeclaredSpaceFrom` next to the two refs. |
| Letting `DescriptorMapRef` stand in for the whole substrate | A representation layer is not identical to the position-typed space declaration. | State the docking rule and keep the space refs visible. |
| Making `SourceSetComposition` or `DerivedViewKind` mandatory in every line | The line fabricates composition or derivation where none exists. | Keep them conditional. |
| Publishing with bare `portfolio` language | `portfolio` blurs retained-set, selected-set, and posture talk. | Use declared source-set and outcome metadata instead. |
| Treating all distortion as one bridge story | Not every qualified relation is bridge-mediated. | State the posture. |
| Letting `G.5` or `G.10` sound like the substrate itself | Publication metadata then replaces substrate semantics. | Keep publication as downstream use of the substrate. |

### A.19.SOURCE-SET-SPACE-SUBSTRATE:9 - Consequences

**Benefits**

- Readers can see what the line is acting on, what spaces it distinguishes, what relation is declared between the two space refs, and what outcome load it claims.
- `A.19`, `C.18`, `G.5`, and `G.10` stay coordinated without collapsing into one layer.
- Heavier qualifiers such as declared map refs, metrics, transitions, and bridge-loss notes remain usable without being forced into every initial declaration.

**Trade-offs**

- The line must expose one relation and one posture instead of hiding them in umbrella prose.
- Some cases that used to look "simple" will expose uncertainty or loss that now needs to be declared.
- Neighboring interpretive-view or publication patterns may need to be read as companions rather than assumed from local shorthand.

### A.19.SOURCE-SET-SPACE-SUBSTRATE:10 - Rationale

`A.19` already declares `CharacteristicSpace`. The missing load is not another free-floating space kind. It is the ref-position and relation stack that tells the reader:

- which declared source set is active;
- which declared space is named in the search-side position;
- which declared space is named in the outcome-side position;
- what `SpaceRefRelationKind` says about those two refs;
- and how much transparency, distortion, uncertainty, or error the line is claiming.

That is why this pattern stops before interpretive views and before publication metadata. If it tried to say less, the load would collapse back into vague `space` or `projection` talk. If it tried to say more, it would start absorbing views, fronts, archives, shortlists, or shipping semantics that belong elsewhere.

### A.19.SOURCE-SET-SPACE-SUBSTRATE:11 - SoTA-Echoing

| SoTA practice | Primary source(s) | Practice demand disciplined here | Practical safeguard bought | Adoption stance |
| --- | --- | --- | --- | --- |
| Evolutionary models relate genotype and phenotype descriptions or model selection across several levels. | [Vanchurin, *Geometric framework for biological evolution* (2026)](https://arxiv.org/abs/2603.15198); [Warrell et al., *Variational methods for Learning Multilevel Genetic Algorithms using the Kantorovich Monad* (2024)](https://arxiv.org/abs/2411.09779). | `SS-0`, `SS-2`, `CC-A19SS-1`, `CC-A19SS-2`. | Provides comparisons for making the represented objects and their connecting relations explicit. | **Adapt.** These are subject-specific mathematical constructions; the source-set declaration rules here are an FPF adaptation. |
| MOUR-QD distinguishes candidate solutions, feature descriptions, objective values and an archive with local Pareto comparisons. | [Janmohamed and Cully, *Multi-Objective Quality-Diversity in Unstructured and Unbounded Spaces* (2025), Introduction and §2](https://arxiv.org/html/2504.03715v1). | `SS-1`, `SS-3`, `CC-A19SS-3`, `CC-A19SS-4`, worked cases `5.1` and `5.2`. | Keeps the source members, space uses and source-to-outcome relation distinguishable. | **Adopt/Adapt.** Preserve the subject distinctions; express the needed references and relations under FPF. |
| Feature spaces may be learned or unstructured, while uncertain QD may require distributions of fitness and descriptor values rather than single deterministic values. | [Janmohamed and Cully (2025), Introduction and §2](https://arxiv.org/html/2504.03715v1); [Flageat et al., *Extract-QD Framework: A Generic Approach for Quality-Diversity in Noisy, Stochastic or Uncertain Domains* (2025), Introduction and §2.2](https://arxiv.org/html/2502.06585v1). | `SS-4`, `SS-5`, `CC-A19SS-5`, `CC-A19SS-6`. | Makes the applicable uncertainty and model limits explicit without prescribing one metric or transition model for every use. | **Adopt/Adapt.** Retain the stated qualifications; select additional models and references for the receiving use. |

### A.19.SOURCE-SET-SPACE-SUBSTRATE:12 - Relations

- **Builds on:** `A.19`, `A.17`, `A.18`.
- **Coordinates with:** `C.18`, `C.19`, `G.5`, `G.10`, `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW`, `A.6.P`, `A.0`.
- **Used by:** `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` and interpretive or atlas methods when a receiving use needs a derived view over the declared substrate.
- **Does not replace:** selector outcome publication, shipping metadata, live pool policy, or enactment planning.

### A.19.SOURCE-SET-SPACE-SUBSTRATE:End

---
