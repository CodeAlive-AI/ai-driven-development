## A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW - Interpretive Views of Declared Source Sets and Search/Outcome Spaces

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Declared-substrate interpretive view.

**Declared-substrate interpretive view.** An explanation or representation that answers an inspection question about an already-declared source set, its search/outcome spaces and their connection. Cite that substrate directly or through a source set or set result that makes it recoverable. Use the simplest sufficient interpretation; use atlas form when the question needs several views or qualifications read together. Formal epistemic viewing and `U.View` claims have the additional conditions in §4.8.

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:0 - Use this when

Use this pattern when one already-declared substrate from `A.19.SOURCE-SET-SPACE-SUBSTRATE` is already in force, and the current passage either cites that substrate directly or works through one declared source-set entry point or set-result entry point that keeps the substrate recoverable, but the reader still needs one interpretive view to see how the line should be read in practice.

Typical indicators are:

- the substrate is already declared, but one thinner interpretive view is still needed so the active source set, search-side space, outcome-side space, or distortion posture stays understandable;
- one fuller atlas-form reading may help collect several typed set views, active set results, cited spaces, declared map refs, or interpretive qualifiers without changing the underlying substrate;
- one derived tradition or palette view must stay recoverable as a view over a base palette rather than silently becoming the palette's default meaning;
- or one line needs optional qualifier refs such as `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, or `BridgeDistortionNote`, but those pins must stay qualifiers rather than the semantic center.

This is the right pattern when the working need is no longer "what substrate is declared?" and not yet "what shortlist, publication form, or shipped result do we emit?".

Not this pattern when:

- you still need to declare the substrate itself, including source-set and search/outcome-space roles; use `A.19.SOURCE-SET-SPACE-SUBSTRATE`;
- you only need `CharacteristicSpace`, its slots, or its typing hooks; use `A.19`;
- you are publishing selector outcomes, shortlist identity, or shipping metadata; use `G.5` or `G.10`;
- you are setting live pool policy, retained-set policy, or enactment/planning posture; use `C.19` or `C.24`;
- you are defining a new generic view law, viewpoint bundle, or publication-view family rather than one domain-specific interpretive reading; use `A.6.3`, `E.17.0`, `E.17`, or `E.17.1`;
- the line would change the EntityOfConcern rather than preserve it; use `A.6.4` or the appropriate retargeting pattern.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:0.1 - What goes wrong if missed

If this pattern is missed, interpretive-view work usually fails in one of four ways:

- the substrate is forced to carry every inspection question itself, so `A.19.SOURCE-SET-SPACE-SUBSTRATE` starts reading as if it also governed interpretive views, atlas readings, or palette interpretation;
- the word `view` appears as one fresh local theory, detached from existing `U.EpistemicViewing` and `U.MultiViewDescribing`, so viewpoint, view, and publication face start collapsing again;
- one atlas-form reading quietly becomes the default meaning of the whole family, so a fuller interpretive form starts redefining the base palette or base source set;
- or qualifier refs such as `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, and `BridgeDistortionNote` either disappear into vague prose or are promoted into mandatory core everywhere.

The reader then cannot tell whether a visible interpretation is one optional interpretive view, one fuller atlas reading, one publication face, or one new semantic head.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:0.2 - What this buys

This pattern buys one disciplined middle layer:

- the substrate remains the semantic center;
- thinner interpretive views remain admissible when a full atlas form is unnecessary;
- `DeclaredSubstrateAtlasView` remains available as one fuller reusable specialization, but not as the default head;
- derived palette or tradition views keep their base palette and base source sets recoverable;
- active set results, cited spaces, declared map refs, and qualifiers stay recoverable when the current reading uses them;
- and publication, shipping, and pool-policy questions stay outside the view.

The practical payoff is simple: the reader can use one interpretive view to understand the declared line better without mistaking that interpretive view for the line's ontology, output, or policy.

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:0.a - TERM/LEX token-status guard (local-first)

Keep this token-status split explicit:

- `DeclaredSubstrateInterpretiveView` is the ordinary/common interpretive-view head introduced here for domain-specific reuse over one already-declared substrate-bearing basis: either the substrate line itself or one declared source set or declared set result that keeps the substrate recoverable.
- `DeclaredSubstrateAtlasView` is the fuller specialization of that same family. It is not the common head and it is not automatically required.
- `TypedSetViews` is one local plural field over already-declared set-view heads or ids. It is not a new generic set-result ontology.
- `TraditionAtlasView` is one local `G.2` specialization of `DeclaredSubstrateAtlasView`, not the family head for all interpretive-view use.
- `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, and `BridgeDistortionNote` are guarded neighboring refs or interpretive qualifiers reused here. This pattern may foreground them, but it does not mint them.
- `inspection question` is one local declaration field naming the interpretive load the current reading helps with. It is not a replacement for `U.Viewpoint`.
- `DerivedViewKind` and `BasePaletteRef` stay local recoverability aids here; they do not silently turn the derived reading into the base ontology.

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:0.b - First-minute operator cue and confusion guide

Use this pattern only after one substrate is already declared, either cited directly or kept recoverable through one declared source set or declared set result. The first-minute move here is not "write more about the same space". It is "decide what inspection question the reader needs answered without changing the EntityOfConcern".

Do this in the first minute:

1. Cite the base substrate or the source-set entry point or set-result entry point that stays recoverable with it.
2. State the inspection question in one sentence.
3. Choose thin interpretation or atlas interpretation.
4. Keep the active source set and any active set result recoverable.
5. Add only the qualifiers that truly discipline the reading.

If you cannot name the base substrate or the recoverable source-set entry point or set-result entry point that carries it, or if the current prose would change the source-to-outcome relation or its posture, stop. You are either repairing the substrate, retargeting the object, or drifting into publication/policy.

| If the question under repair sounds like... | Use now | Why |
| --- | --- | --- |
| "How do I help the reader inspect the declared substrate?" | `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` | This pattern governs substrate-side only reading. |
| "What is the substrate itself?" | `A.19.SOURCE-SET-SPACE-SUBSTRATE` | The base line has to exist first. |
| "Which palette-first or tradition-facing atlas reading should I use?" | `G.2` over this family | That is one local specialization of atlas interpretation. |
| "What do we publish, ship, keep live, or plan next?" | `G.5`, `G.10`, `C.19`, or `C.24` | Those publication, shipping, live-pool, and planning questions stay outside interpretive views. |

Common confusion to kill early: one visible atlas or metric note does not make atlas form automatically necessary. Thin interpretation is already a complete admissible answer.

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:1 - Problem frame

Once one source-set and search/outcome-space substrate has been declared, many lines still need one second-order interpretive view for ordinary work.

Examples include:

- one archive-centered reading that needs optional metric or transition qualifier to explain why certain regions stay promising;
- one derived tradition or palette reading that must remain visibly derived from a base palette;
- one atlas-form reading that collects several typed set views, active set results, spaces, declared map refs, metrics, or distortion notes so that cross-scale structure stays readable;
- one interpretive rendering that helps the reader inspect the declared substrate without turning that rendering into the substrate's default meaning.

`A.6.3` governs EntityOfConcern-preserving epistemic viewing; `E.17.0` separately qualifies a resulting episteme as a `U.View` through viewpoint conformance. `G.2` uses `TraditionAtlasView` for an optional interpretation of a palette and declared set results. This pattern applies those distinctions to inspection of a declared substrate, with the amount of representation determined by the inspection question.

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:2 - Problem

How should one declare an interpretive view so that:

1. it is explicitly one domain-specific use-site of existing `U.EpistemicViewing` and `U.MultiViewDescribing` law, not one fresh autonomous theory of views;
2. it keeps the already-declared substrate recoverable instead of replacing it;
3. it allows both ordinary thinner interpretive views and one fuller atlas-form interpretive view;
4. it keeps `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, and `BridgeDistortionNote` optional and substrate-side only;
5. it keeps derived palette or tradition views recoverable through `DerivedViewKind` and `BasePaletteRef` when those are active;
6. it does not mint new set-result family heads, selector policy, publication policy, or shipping semantics;
7. it lets `G.2` keep `TraditionAtlasView` as one local specialization rather than as the generic head of the whole family;
8. and it fails closed when the line would really be retargeting, new view-law work, substrate repair, publication, or policy?

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:3 - Forces

| Force | Tension |
| --- | --- |
| Existing view law vs local usefulness | The interpretive view must be useful in local substrate work, but it cannot invent a second `view` ontology beside `A.6.3` and `E.17.0`. |
| Substrate stability vs interpretive help | Readers need one interpretive layer, but that interpretive layer must not redefine the substrate. |
| Thin interpretation vs atlas-form reading | Some cases need only one light interpretive view; others genuinely need one fuller atlas-form reading. The pattern must admit both without making the fuller form default. |
| Recoverability vs convenience | Derived tradition or palette views help reading, but they must not hide the base palette, base source set, or active declared spaces. |
| Qualifier richness vs semantic inflation | Declared map refs, metrics, transition qualifiers, and distortion notes are often useful, but they must stay optional interpretive qualifiers rather than new mandatory core. |
| Readability vs downstream boundary discipline | The pattern should help cold readers immediately, while still keeping `G.5`, `G.10`, `C.19`, and `C.24` outside the interpretive view. |

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4 - Solution

Declare interpretive views as substrate-side only readings over one already-declared substrate-bearing basis, keep them explicitly under existing view law, and reserve atlas form for the cases that truly need it.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.1 - Declared-substrate interpretive-view record and outside work

Use this pattern to declare:

- one `DeclaredSubstrateInterpretiveView`, the ordinary/common head of this interpretive-view family;
- one substrate-side only reading over one already-declared substrate-bearing basis: either one explicit `A.19.SOURCE-SET-SPACE-SUBSTRATE` line or one already-declared source set or declared set result whose declared spaces, declared map refs, and qualifiers remain recoverable through such a line;
- the inspection question that makes this view worth showing;
- the recoverable source set or source sets that the interpretive view is reading;
- any active set result, derived view, or base palette that the current reading keeps in play;
- any cited spaces or declared map refs that the current reading depends on, provided those remain recoverable through declared refs or the cited substrate-bearing line;
- and any optional qualifiers that the current view genuinely needs.

`DeclaredSubstrateAtlasView` is one fuller specialization inside that same family. It is not the common head.

Do not use this pattern to declare:

- `CharacteristicSpace` itself;
- the substrate role/relation stack from `A.19.SOURCE-SET-SPACE-SUBSTRATE`;
- selector outcomes, shortlist heads, or shipping outputs;
- live pool policy or enactment policy;
- or a new generic law for views, viewpoints, or publication faces.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.2 - Minimal interpretive view declaration

A conforming interpretive view makes the following explicit:

- which interpretive-family head is active: ordinary `DeclaredSubstrateInterpretiveView` or fuller `DeclaredSubstrateAtlasView`;
- which already-declared substrate-bearing basis it is reading: either the explicit substrate line or the declared source-set entry point or set-result entry point that keeps that substrate recoverable;
- which inspection question the view is answering;
- which source set or source sets must stay recoverable while the view is active;
- which active set result, if any, the current reading is using over that source set;
- which cited spaces and declared map refs, if any, the current reading depends on, and how they remain recoverable;
- which optional qualifiers are genuinely doing work in the current case;
- and any use boundary needed to distinguish this interpretation from a substrate revision, publication or policy decision.

The minimum ordinary interpretive view declaration is therefore:

1. one declared substrate-bearing basis from `A.19.SOURCE-SET-SPACE-SUBSTRATE`: either the explicit base substrate line or one declared source set or declared set result whose substrate remains recoverable with it;
2. one explicit inspection question;
3. one recoverable active source-set basis, plus any active set result drawn from it when the reading uses one;
4. any cited spaces, maps and applicable uncertainty or distortion qualifications remain recoverable.

These are content requirements. Existing prose or a model can supply them; a separate record or repeated boundary statement is unnecessary when the content and use are already clear.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.3 - Interpretive-view declaration laws (IV-0..IV-8)

**IV-0 - View-law docking is explicit.**
An ordinary interpretive reading keeps its declared substrate recoverable. An asserted epistemic viewing follows `A.6.3`; an asserted `U.View` additionally satisfies `E.17.0` viewpoint conformance, as specified in §4.8.

**IV-1 - The EntityOfConcern is preserved.**
The interpretation continues to concern the declared substrate. In an A.6.3 epistemic viewing, the source and receiving epistemes preserve the same EntityOfConcern while their ClaimGraphs or ReferenceSchemes may differ. Changing that EntityOfConcern requires a separate retargeting account.

**IV-2 - The base substrate remains the semantic center.**
The interpretive view may foreground aspects of the base line, but it does not replace or repair the base substrate declaration. Substrate repair belongs back in `A.19.SOURCE-SET-SPACE-SUBSTRATE`.

**IV-3 - Source, set-result, and palette recoverability are mandatory.**
The current source set, any active set result drawn from it, and any active derived view or base palette must remain recoverable while the interpretive view is active.

**IV-4 - Distinguish substrate and view qualifications.**
The view may foreground the substrate's `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef` or `BridgeDistortionNote`. It may also introduce a qualification of its own representation. State which relation a qualification concerns; changing the underlying source-to-outcome relation requires revising its substrate declaration.

**IV-5 - Thin interpretation and atlas interpretation are different profiles.**
Ordinary `DeclaredSubstrateInterpretiveView` is a complete admissible profile, not a placeholder. `DeclaredSubstrateAtlasView` is used only when the fuller composite inspection question is real.

**IV-6 - Atlas form requires a complete composite record.**
If atlas form is active, the view must keep the base substrate, the active source or set result, the relevant `TypedSetViews`, any cited spaces, any cited declared map refs, and any qualifiers explicit enough that the reader can recover why thin interpretation was not enough.

**IV-7 - Local specialization stays local.**
If `TraditionAtlasView` is used, it remains one `G.2` specialization of `DeclaredSubstrateAtlasView`; it does not become the common head of the family.

**IV-8 - Admission is fail-closed.**
If the current line would change the EntityOfConcern, add new generic view law, repair the substrate, decide publication, or decide policy, it is not a conforming interpretive view here. Apply the pattern that governs that question instead of stretching the family.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.4 - Profiles

Use one of these profiles explicitly:

- **Thin-interpretation profile.**
  Use ordinary `DeclaredSubstrateInterpretiveView` when a direct explanation answers the inspection question. The number of cited references alone does not require atlas form.
- **Atlas-interpretation profile.**
  Use `DeclaredSubstrateAtlasView` when answering the question requires showing how several declared views, spaces, maps or qualifications relate within the same substrate.

If neither profile can be chosen honestly, the line is not ready as interpretive-view text.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.5 - Operational declaration sequence (fail-closed)

When declaring one interpretive view, proceed in this order:

0. **Entry test.** Confirm that one already-declared substrate exists and that the current inspection question can cite it either directly or through one declared source-set entry point or set-result entry point that keeps it recoverable, rather than drifting into substrate repair, publication, or policy.
1. **Name the active interpretive head.** Use ordinary `DeclaredSubstrateInterpretiveView` unless the current reading genuinely needs the fuller atlas form.
2. **Cite the base line.** Name the already-declared substrate the view is reading, or cite the source-set entry point or set-result entry point together with the recoverable substrate it depends on.
3. **State the inspection question directly.** Say what the view helps the reader see that the substrate alone leaves hard to inspect.
4. **Keep the base source/result recoverable.** Name the active source set, and if the view is over one declared front, archive, shortlist, palette, or other set result drawn from that source, keep that active set result recoverable too.
5. **Recover derived-view and palette structure when it matters.** If the view depends on one derived tradition or palette reading, state `DerivedViewKind` and `BasePaletteRef`.
6. **Add the actual qualifiers.** Add `TypedSetViews`, cited spaces, declared map refs, metrics, transition qualifiers, or distortion notes only when the current reading truly depends on them.
7. **Run the preservation check.** If the interpretive prose would materially change the base source-to-outcome relation or the base distortion/uncertainty/error posture, stop and reopen the substrate declaration.
8. **Run the boundary check.** If the prose starts changing the EntityOfConcern, minting new generic view law, publishing selected sets, shipping outputs, or deciding policy, apply the pattern that governs that question.

**Incomplete declaration.** Missing base recovery or an unresolved change to the underlying relation prevents the dependent interpretive-view claim. Preserve independently established content and resolve the missing basis. Split out any separate publication or policy decision and apply its governing pattern.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.6 - Thin interpretation remains a complete admissible form

Many cases need one interpretive view but not one atlas-form interpretation package.

Stay with one thinner interpretive view when:

- the current reading needs only one declared source set or one derived view over it;
- the current question does not need several typed set views assembled at once;
- one explicit interpretive sentence is enough to keep the current line readable;
- or the case does not genuinely depend on metrics, transitions, or bridge-loss notes.

This matters because the interpretive layer should stay proportionate to the inspection question. If a thin interpretive view already solves the reader's problem, forcing atlas form would over-type the line and create fake necessity.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.7 - Atlas form is fuller interpretation and needs a complete record

Use `DeclaredSubstrateAtlasView` for the fuller interpretive cases:

- when several typed set views over one declared source set or one active derived set result must be read together;
- when one atlas-form reading helps the reader inspect cross-scale structure, cross-space structure, qualifier plurality, or declared-map-ref plurality;
- when the current interpretation genuinely depends on one declared map ref, metric, transition qualifier, or distortion note and those qualifiers must stay visible together with the active source sets or active set results they qualify.

The minimal admissible atlas-form interpretation declaration therefore contains:

- the cited base substrate or source-set entry point or set-result entry point;
- the active source set and any active set result drawn from it;
- `TypedSetViews` when several declared set views are being held together;
- any cited `SearchSpaceRef`, `OutcomeSpaceRef`, or other declared space refs that the atlas reading depends on;
- any cited `OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, or `BridgeDistortionNote` that materially disciplines the reading;
- `DerivedViewKind` and `BasePaletteRef` whenever the atlas reading is over one derived palette or tradition view;
- one explicit reason thin interpretation is insufficient.

If atlas form cannot state that composite interpretation view without invention, stay with thin interpretation or apply the pattern that governs the missing question.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.8 - No autonomous local view law is introduced here

Start with the declared substrate and the inspection question. An ordinary interpretation can stop with a recoverable explanation. When the use claims an A.6.3 epistemic viewing, identify the source episteme `X` whose ClaimGraph describes that substrate and the receiving episteme `Y` produced by the stated projection or re-expression. Both retain the same EntityOfConcern; state the transformed ClaimGraph and any changed ReferenceScheme explicitly.

Qualify `Y` as an `E.17.0` `U.View` only when it independently conforms to the named `U.Viewpoint` for that concern. A return to A.6.3 alone does not establish viewpoint conformance. Keep the viewpoint, the view episteme and any E.17 publication face separate. A different EntityOfConcern requires the applicable retargeting account; changing or repairing the substrate returns to `A.19.SOURCE-SET-SPACE-SUBSTRATE`.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.9 - Qualifier refs stay substrate-side

`OutcomeMapRef`, `SpaceMetricRef`, `TransitionRelationRef`, and `BridgeDistortionNote` are admitted here only as interpretive qualifiers.

Qualifiers of the source-to-outcome relation are declared with the substrate and reused here. Qualifiers of the view itself belong to its representation account; for example, rounding displayed Coordinates can lose distinctions while the underlying Coordinates and map remain unchanged.

Use them when the current interpretive view genuinely needs them:

- `OutcomeMapRef` when the current reading must show how one declared source or set result bears on one outcome-side declared space/ref;
- `SpaceMetricRef` when neighborhood, spread, reachability, or crowding claims are load-bearing in the current reading;
- `TransitionRelationRef` when the current reading depends on explicit transition or cross-scale state-change qualifier;
- `BridgeDistortionNote` when the reader must keep one declared loss or distortion visible near the current reading.

If a new loss, uncertainty or other qualification changes the underlying source-to-outcome relation, revise the substrate declaration and recheck dependent uses. Reuse unaffected content. A view-only qualification does not by itself change that relation.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.10 - Publication, set-result, and pool-policy boundaries

This pattern does not publish selected sets, declare shortlist heads, or decide which candidate lines stay live.

Keep the split explicit:

- `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` helps the reader inspect one already-declared substrate;
- `G.5` publishes selector outcomes and their source/publication metadata;
- `G.10` ships publication faces and pins;
- `C.19` governs live candidate-pool and frontier policy;
- `C.24` governs enactment/planning posture.

If the prose starts deciding who survives, what is published, or what is shipped, it has already left this pattern.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.11 - `G.2` keeps the tradition-facing atlas specialization

When the current interpretive view is tradition-facing and palette-first recoverability matters, use the local specialization governed by `G.2`.

Read the relation this way:

- `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` states the generic interpretive-view family and the generic fuller atlas form `DeclaredSubstrateAtlasView`;
- `G.2` keeps the palette-first, tradition-facing specialization `TraditionAtlasView`;
- `TraditionAtlasView` is therefore one local specialization of the fuller atlas form, not the common head of the whole interpretive family.

This keeps the family honest in both directions:

- the common interpretive-view family does not force `Tradition` or `Atlas` into every case;
- and the `G.2` specialization does not lose its palette-first recoverability.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:4.13 - Using the interpretive view with neighboring patterns

Once the interpretation is sufficient, stop. Select a neighboring pattern only for a remaining question:

- Use `G.2` when the interpretive view becomes palette-first, tradition-facing atlas work. That is one local specialization of atlas interpretation, not the common family head.
- Use `F.18` when the question under repair is label choice around interpretive-view, atlas, palette, or declared-map-ref language. Naming notes may explain the labels, but they do not change the base substrate or the inspection question.
- Use `A.6.P` when one passage collapses view, surface, space, map, or palette into one umbrella word. Repair the layer split first, then continue.
- Use `A.0` when cold-reader glossing is what the current line lacks. Glosses help recognition; they do not replace the base interpretive view declaration.
- Use `G.5`, `G.10`, `C.19`, or `C.24` when the passage starts deciding outputs, survivor sets, or planning posture.

If a neighboring passage would change the EntityOfConcern or the base substrate posture, this pattern is no longer the governing pattern for that sentence. Reopen the base line or apply the pattern that governs the new question.

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:5 - Archetypal Grounding

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:5.1 - System

**Tell.** One QD archive has a declared substrate. A reader asks which candidates are neighbors of candidate p under its declared metric.

**Show.** In this constructed case, `Archive-12` uses `BehaviorCharacteristicSpace@ed=12` and `ArchiveNeighborhoodMetric@ed=4`. The declared neighborhood criterion is distance at most 0.3. Distances from p to q and r are 0.2 and 0.8 respectively. An ordinary `DeclaredSubstrateInterpretiveView` groups q with p and leaves r outside that neighborhood, showing the criterion alongside the grouping. The source Coordinates and metric remain recoverable.

**Cash-out.** The reader can recover why q is a neighbor and r is not. This grouping answers the inspection question; it does not itself select which candidates to retain. No fuller atlas is needed.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:5.2 - Episteme

**Tell.** One synthesis line already keeps a base SoTA palette and one derived tradition-facing reading. The reader now needs one fuller atlas-form interpretive view that keeps the base palette recoverable while showing how several tradition-facing views and cross-scale notes sit together.

**Show.** The active interpretive head is `DeclaredSubstrateAtlasView`. It reads one declared palette-facing substrate line whose source-set family remains `TraditionPalette`, whose active derived view remains `TraditionFront`, and whose base palette remains recoverable through `SoTAPaletteDescriptionId`. The cited spaces stay explicit as `TraditionComparisonSpace@ed=3` and `AdoptionOutcomeSpace@ed=2`. The atlas reading keeps together the declared set views `TraditionFront` and `TraditionArchive`, the `OutcomeMapRef` value `PaletteToAdoptionOutcomeMap@ed=1`, the distortion note `CrossTraditionComparisonLossNote@ed=1`, and the local `G.2` specialization `TraditionAtlasView`.

**Cash-out.** The reader follows a tradition profile from the palette into its front or archive view, then follows `PaletteToAdoptionOutcomeMap@ed=1` to its conditional adoption outcome. The comparison-loss note stays beside comparisons that depend on it. These connections explain why the views are shown together; a front alone would hide the archive and its relation to the same palette. The atlas changes inspection, not membership of the base palette.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:5.3 - Boundary anti-case

**Tell.** One note starts from "atlas view" language, then quietly changes the base outcome posture and argues that only one shortlisted tradition should remain live.

**Show.** The changed-relation and retention claims need their own governing patterns.

**Cash-out.** Reopen the substrate if the base relation or posture changed. Apply `C.19`, `C.24`, `G.5`, or `G.10` to retention or shipping decisions instead of using interpretive-view prose to smuggle them in.

#### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:5.4 - Use-situation spread

Use the interpretive-view family this way across different working situations:

| Working situation | Choose | What must stay explicit | Common miss avoided |
| --- | --- | --- | --- |
| Archive-side QD line that only needs one metric cue so the reader can see local neighborhoods | Thin interpretation | One base substrate, one inspection question, one active source set, and the specific metric qualifier doing work. | Forcing atlas form into a case that only needs one simple reading aid. |
| Palette-first synthesis line that really needs several declared views, spaces, declared map refs, and loss notes held together | Atlas interpretation, with `G.2` when the case is tradition-facing | The base palette, derived view, cited spaces, qualifying map-ref/distortion refs, and the reason thin interpretation is insufficient. | Letting the most salient visible atlas overlay replace the palette-first base line. |
| Derived tradition/front note that only needs to remind the reader how to read one already-declared substrate | Thin interpretation | The inspection question, derived-view recoverability, and the base palette when it would otherwise disappear. | Treating every derived tradition reading as if it were already full atlas work. |
| Passage that starts changing the outcome posture, survivor set, or publication result | Do not use this pattern | The boundary out to substrate repair, publication, or policy stays explicit. | Smuggling retargeting or policy decisions into interpretive-view prose. |

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:6 - Bias-Annotation

- **Gov bias.** The pattern prefers explicit reuse of existing view law over local convenience talk about one `view`.
- **Arch bias.** The pattern keeps substrate, interpretive reading, publication, and policy separated even when one merged story would sound simpler.
- **Prag bias.** The pattern prefers thinner interpretive views by default and treats atlas form as one fuller option rather than a universal baseline.
- **Did bias.** The pattern insists on recoverability of the base palette or base source set because readers otherwise over-trust the most salient visible interpretive form.

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:7 - Conformance Checklist

Apply these checks to the interpretation and claims actually made.

| ID | Check question | Fail when | Repair or governing pattern |
| --- | --- | --- | --- |
| `CC-A19IV-1` | Is one already-declared base substrate or source-set entry point or set-result entry point named explicitly? | The interpretive view floats free of the line it is supposed to help read. | Cite the base substrate or the recoverable source-set entry point or set-result entry point. |
| `CC-A19IV-2` | When formal viewing is claimed, are the A.6.3 source and receiving epistemes recoverable, and is E.17.0 viewpoint conformance established separately for a `U.View` claim? | A pattern citation is treated as sufficient to establish either relation. | Recover the exact epistemes and viewing transformation; test the named viewpoint only when `U.View` qualification is needed. |
| `CC-A19IV-3` | Does the line preserve the same EntityOfConcern and keep the base substrate as semantic center? | The interpretive prose retargets the EntityOfConcern or repairs the substrate in place. | Reopen under `A.19.SOURCE-SET-SPACE-SUBSTRATE`, `A.6.4`, or the appropriate neighboring pattern. |
| `CC-A19IV-4` | Are the current source set, any active set result, and any active derived view or base palette recoverable? | The interpretive reading hides the base palette, base source/result, or active derived set result behind one fuller visible overlay. | Restore the missing recoverability fields. |
| `CC-A19IV-5` | Is the active profile chosen honestly: thin interpretation or atlas interpretation? | Atlas language is used by reflex, or the line needs atlas interpretation but never says so. | State the profile and the inspection question it answers; explain the composite need when choosing atlas form. |
| `CC-A19IV-6` | If atlas form is active, is the composite atlas-form interpretation declaration complete? | Several views, spaces, declared map refs, or qualifiers are being used, but `TypedSetViews`, cited spaces, declared map refs, qualifiers, or the reason thin interpretation is insufficient remain hidden. | Publish the missing atlas-form interpretation declaration or step back to thin interpretation. |
| `CC-A19IV-7` | Is each qualification attached to the relation it qualifies? | A view qualification silently changes the source-to-outcome relation, or a material substrate qualification disappears. | Preserve substrate qualifications; state any view-only loss separately. Revise the substrate if its underlying relation changes. |
| `CC-A19IV-8` | If `TraditionAtlasView` is used, is it kept as one `G.2` specialization rather than the common family head? | The local specialization is treated as if every interpretive case were already palette-first atlas work. | Restore the split between `DeclaredSubstrateAtlasView` and `TraditionAtlasView`. |
| `CC-A19IV-9` | Does the line stay out of publication and policy work? | The prose starts deciding who survives, what is published, or what is shipped. | Split the line and apply `G.5`, `G.10`, `C.19`, or `C.24` to those questions. |
| `CC-A19IV-10` | Could a cold reader choose thin interpretation versus atlas interpretation and fill one interpretive view declaration without hidden invention? | The reader still needs surrounding memo knowledge to know which head to use, what fields matter, or why atlas is or is not needed. | Use the content requirements in §4.2 and sequence in §4.5; show the composite inspection need if atlas form is necessary. |
| `CC-A19IV-11` | Is the inspection question explicit enough to tell the reader what this view helps inspect now? | The view mostly restates the base theory, but the practical inspection load stays unnamed. | State the inspection question directly and keep the base line recoverable beside it. |
| `CC-A19IV-12` | When specialization, naming repair, publication, or policy becomes the next question, is the governing neighbor explicit? | The interpretive prose silently drifts into `G.2`, `F.18`, `A.6.P`, `G.5`, `G.10`, `C.19`, or `C.24` without naming the boundary. | Split the line and cite the governing neighbor instead of stretching interpretive-view prose across that boundary. |

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Writing as if `A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` were a fresh autonomous theory of views | It duplicates existing `A.6.3` and `E.17.0` law and collapses `U.Viewpoint`, `U.View`, and publication-face discipline. | State the docking to existing view law explicitly. |
| Letting atlas language become the default meaning of every interpretive case | The fullest visible interpretive form silently becomes the family head. | Keep ordinary thinner interpretive views admissible and say when atlas form is actually needed. |
| Treating qualifier refs as the view's semantic center | Metrics, transitions, or distortion notes then replace the base substrate. | Keep the base substrate and inspection question explicit, and keep qualifier refs optional. |
| Letting a derived tradition view replace its base palette | The reader loses palette-first recoverability and mistakes one local interpretation for the default ontology. | Keep `DerivedViewKind` and `BasePaletteRef` visible together. |
| Turning the interpretive view into publication or pool policy | The reader can no longer tell whether the text is helping interpret the line or deciding what survives and gets published. | Keep `G.5`, `G.10`, `C.19`, and `C.24` outside this pattern. |
| Forcing atlas form into every first reading | Simple cases become over-typed and harder to use. | Start with the thinner interpretive-view form and widen only when the current need genuinely requires it. |

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:9 - Consequences

**Benefits**

- Readers get one explicit interpretive layer without losing the declared substrate.
- FPF keeps one common interpretive-view family without forcing `G.2` or another local specialization to carry the whole interpretive requirement.
- Atlas-form interpretation remains available where it helps, but thinner interpretive views stay lawful.

**Trade-offs**

- The declaration must keep more boundaries explicit: view law, substrate, publication, and policy no longer collapse into one comfortable narrative.
- Some cases that once looked like "just a view" must now say whether they are thin interpretation, atlas interpretation, publication, or policy.
- The pattern requires the base palette or source set to stay recoverable, which can make local prose slightly less terse.

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:10 - Rationale

The family needs one common interpretive-view pattern because neither of the earlier extremes is good enough.

If everything stays in the substrate, the substrate starts carrying interpretive and atlas-form requirements that are not part of its semantic center.

If everything stays inside one local specialization such as `G.2`, the common interpretive requirement gets trapped inside one tradition-facing case and starts looking like a local accident rather than a reusable family.

`A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW` is the middle answer:

- it keeps the interpretive layer generic and reusable;
- it keeps the layer explicitly under existing view law;
- it lets ordinary thinner interpretive views remain first-class;
- and it reserves atlas-form reading for the cases that truly need it.

That is why `DeclaredSubstrateAtlasView` appears here as one richer interpretive specialization, while `TraditionAtlasView` remains one `G.2` specialization of it rather than the common head.

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:11 - SoTA-Echoing

| Practice line | Primary accepted basis | Practice demand disciplined here | Practical safeguard bought | Adoption stance |
| --- | --- | --- | --- | --- |
| Interpretive readings should remain entityOfConcern-preserving views rather than becoming fresh semantic centers. | `A.6.3` preserves EntityOfConcern between source and receiving epistemes; `E.17.0` adds independent viewpoint conformance for `U.View`. | `IV-0`, `IV-1`, `IV-8`, `CC-A19IV-2`, `CC-A19IV-3`. | Keeps interpretive prose from quietly turning into retargeting or new view-law invention. | **Adopt.** Reuse the existing view law directly rather than minting one local alternative. |
| Palette-first SoTA synthesis already treats atlas interpretation as optional neighboring interpretation rather than the default meaning of `Tradition` or `SoTAPaletteDescription`. | `G.2:4.7` already keeps `TraditionAtlasView` as optional neighboring interpretation and preserves palette-first recoverability. | `IV-5`, `IV-6`, `IV-7`, `CC-A19IV-5`, `CC-A19IV-8`, worked slice `5.2`. | Keeps atlas form available without letting the most salient visible interpretive layer replace the base palette or family head. | **Adopt/Adapt.** Adopt palette-first recoverability and adapt it into one reusable common interpretive family. |
| FPF keeps richer map, metric and transition qualifications conditional on the inspection question. | The bounded QD and atlas comparisons in `A.19.SOURCE-SET-SPACE-SUBSTRATE:11` motivate this design choice; they do not establish it as a universal rule of contemporary practice. | `IV-4`, `IV-5`, `IV-6`, `CC-A19IV-5`, `CC-A19IV-6`, `CC-A19IV-7`. | Keeps thinner interpretation admissible, keeps atlas interpretation reusable but non-default, and prevents rich formal qualifier from being smuggled in by default. | **Adapt.** Keep richer formal qualifier available without pretending it is the baseline for every interpretive reading. |

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:12 - Relations

- **Builds on:** `A.19.SOURCE-SET-SPACE-SUBSTRATE`, `A.19`, `A.6.3`, `E.17.0`, `E.17`.
- **Coordinates with:** `G.2`, `G.5`, `G.10`, `C.19`, `C.24`, `A.6.P`, `A.0`.
- **Specialized locally by:** `DeclaredSubstrateAtlasView`, and in palette-first tradition work `TraditionAtlasView` under `G.2`.
- **Does not replace:** substrate declaration, selector outcome publication, shipping metadata, or live candidate-pool / enactment policy.

### A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW:End

---
