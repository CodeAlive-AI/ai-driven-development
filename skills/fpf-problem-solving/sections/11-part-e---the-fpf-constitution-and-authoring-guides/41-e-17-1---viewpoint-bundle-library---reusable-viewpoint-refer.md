## E.17.1 - Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Tech-name.** `ViewpointBundleLibrary` (pattern and catalogue form, not a U-kind).

**Plain-name.** Viewpoint bundle library.

**Use this when.** The same coherent family of already admitted viewpoint editions recurs across projects, schools, or publication uses, and users need one editioned catalogue from which exact viewpoint references can be imported without restating or reidentifying the viewpoints.

**First action.** Resolve one already admitted catalogue edition L and its family designator, retrieve the local declaration, and resolve only the `U.ViewpointRef` members needed now. If L or the declaration is new, missing, or disputed, use §4.2 to recover `<G_L, K_L, R_L>` and verify L's C.2.1 constitution for that edition; reuse that result while the edition, effective scheme, and relied-on premises stay unchanged.

**First useful result.** One exact catalogue edition L, one ordinary family designator retrieving a local declaration claim block, and one finite non-empty member set of `U.ViewpointRef` values that each resolve to an exact E.17.0 viewpoint episteme edition. L retains its C.2.1 identity; the compact locator `<editionDesignator(L), familyDesignator>` aids retrieval under `R_L` but is neither L's identity nor a separate bundle kind or entity.

**Ordinary stop.** Stop when exact L, the declaration, and the needed reference subset are recoverable. Do not reconstruct L's constitution, instantiate every member, select an A.22 structure, prove conformance, or publish the catalogue merely to import an admitted family.

**Admission boundary.** E.24.UK admits `U.Viewpoint` and `U.View`; it does not admit `U.ViewpointBundleLibrary` or `U.ViewpointBundle`. E.17.1 therefore defines an ordinary catalogue-episteme form and local bundle declarations in its claim content. The historical filename remains a discovery locator only and grants no kind membership.

**Do not use this when.** One describing use merely selects one viewpoint or a small one-off set that has no recurring family-level purpose. Keep the exact references local; a bundle adds no conformance, membership, structure, publication, or correspondence merely by collecting them.

**What changes in practice.** Authors reuse exact references and preserve their bundle provenance; reviewers can detect silent member substitution, alias collision, and package-driven membership claims.



**Builds on.**
`A.6.2-A.6.4` (episteme morphism classes), A.6.5 relation-declaration slot discipline, `A.7`, `E.7`, `E.10`, `E.10.D1`, `E.10.D2`, and `E.17.0 MultiViewDescribing`.

**Used by.**
`E.17.2` (TEVB engineering viewpoint bundles), `E.18:5.12`, and domain-specific viewpoint families for architecture, governance, safety, research, or assurance.

### E.17.1:1 - Problem frame

**Selected-family discipline.** A local declaration states the exact target-kind compatibility condition it uses: either a by-value criterion or a reference that resolves to the exact ClaimGraph defining or constraining the admitted target kind. Bundle labels, aliases, annexes, files, and publication faces never supply that criterion or select an actual entity by themselves.

`MultiViewDescribing` lets engineers recognize several epistemes about one exact entity as views under exact viewpoint editions and recover cross-view relations only when those relations actually obtain. In practice many such viewpoint families recur across projects and schools: engineering teams reuse functional / procedural / structural / interface viewpoints; governance teams reuse risk / control / compliance / operations viewpoints; research teams reuse theory / experiment / inference / limitation viewpoints.

E.17.1 therefore supplies one explicit packaging pattern for reusable viewpoint families so that authors can import them, name them stably, review them once, and keep viewpoint-family identity separate from document labels, publication faces, and publication forms.

### E.17.1:2 - Problem

Without a viewpoint-bundle library pattern:

1. **Each domain invents local viewpoint families.**
   Similar families reappear under slightly different labels, but no stable catalogue `U.Episteme` records whether the underlying viewpoints are actually the same.
2. **Viewpoint identity drifts.**
   A family called `functional`, `capability`, or `operational` may differ only lexically, or may differ semantically, but there is no disciplined place to tell which is which.
3. **`MultiViewDescribing` cannot reuse a family cleanly.**
   Every instance must restate its finite viewpoint family locally instead of importing an existing bundle.
4. **Reusable viewpoint-library practice remains external.**
   FPF lacks a native place where reusable viewpoint families can be expressed as reviewable catalogue content without importing a standard's ontology.
5. **Reader-facing labels leak into semantics.**
   Authors reuse the same name for viewpoints, views, publication faces, or folders, and the boundary between EntityOfConcern and Description episteme becomes unclear.

### E.17.1:3 - Forces

| Force | Tension |
|---|---|
| **Reuse vs local fit** | Authors want reusable viewpoint families, but a local project may still need a subset or a context-specific extension. |
| **Stable identity vs evolution** | Bundles must stay stable enough for long-term reuse while still admitting editioned change. |
| **EntityOfConcern clarity vs label convenience** | A bundle library is a catalogue episteme whose members reference exact viewpoint epistemes, yet teams often prefer one reader-facing label across viewpoint, view, publication form, and carrier. |
| **Engineering vs publication discipline** | Engineering viewpoints and publication viewpoints both matter, but their reader-facing designators must not collapse into one lexical namespace. |
| **Rich libraries vs cognitive economy** | A library should be rich enough for real reuse without becoming so large that authors cannot choose from it coherently. |

### E.17.1:4 - Solution - one catalogue episteme with local bundle declarations

`E.17.1` defines a reusable form for one ordinary C.2.1 catalogue episteme L whose local bundle declarations package exact `U.ViewpointRef` values resolving to exact E.17.0 viewpoint episteme editions. L, a declaration claim block within L, its ordinary family designator, each reference, each viewpoint designator, and P remain distinct. Neither the catalogue nor a declaration redefines viewpoint identity or membership, grants `U.View` membership, or creates publication forms and carriers.

#### E.17.1:4.1 - Core role

A conforming viewpoint-bundle library makes three things explicit:

- **which family is being named,** via an ordinary family designator interpreted under exact `R_L`;
- **which `U.ViewpointRef` members resolve to the exact viewpoint episteme editions packaged by that family;**
- **which exact target-kind compatibility condition and catalogue-edition discipline constrain the family.**

This lets `MultiViewDescribing` import a finite viewpoint family from a stable catalogue `U.Episteme` instead of restating it ad hoc in every local description family.

#### E.17.1:4.2 - Reuse an admitted catalogue; open full constitution only when needed

**Existing-catalogue route.** Resolve the already admitted catalogue edition L, retrieve the local declaration by its family designator under L's effective `R_L`, and resolve only the member references needed now. Do not reconstruct L's complete C.2.1 constitution merely to import an admitted edition.

Open the complete constitution below for the affected catalogue edition when authoring or admitting a new L, when L or edition identity or reference resolution is disputed, or when a named later use needs the catalogue's ClaimGraph, subject, or scheme as inspectable premises. Reuse an existing check while that edition, its effective scheme, and the relied-on premises stay unchanged:

- `G_L` is the exact `U.ClaimGraph` that states the catalogue scope, the local family declarations, the referenced viewpoint editions, their target-kind compatibility conditions, and the edition-change rule;
- `K_L` is the exact catalogue subject: the independently identified finite C.13 collection of already admitted viewpoint episteme editions whose recurring reuse groupings L describes. Its collection identity, exact members, obtaining membership relations, and identity rule are established before L; neither the catalogue nor a declaration creates them; and
- `R_L : U.ReferenceScheme` is the exact effective scheme under which the catalogue's ordinary library, edition, and family designators resolve; each `U.ViewpointRef` resolves to exact P; target-kind criteria and compatibility claims are interpreted; and reference, omission, provenance, and edition-change rules are read.

`EpistemeConstitutionRelation(G_L, K_L, R_L)` must obtain. The participant-determined triple `<G_L, K_L, R_L>` identifies exact catalogue episteme L. If a proposed catalogue has only a file, label, list, or card but no truthful exact `K_L` or effective `R_L`, stop: L has not yet been constituted.

`G_L` makes at least these claims recoverable:

- one ordinary library designator and one ordinary edition designator interpreted under `R_L`;
- a finite set of local family-declaration claim blocks, each retrievable inside `G_L` by one ordinary family designator interpreted under `R_L`;
- the exact `U.ViewpointRef` members and target-kind compatibility claim for each declaration; and
- only maintenance claims currently needed, using the branch that matches the present claim:
  - for a current maintenance-System claim, cite the admitted maintenance `U.System`; cite an exact local system-role kind and its independently evaluated classification only when that classification is current;
  - for actual maintenance Work, cite the dated `U.Work` and its performer, and use F.6 to identify the assignment under which that System acted; a short catalogue claim may omit identifiers its bounded use does not need;
  - for current maintenance responsibility, cite its direct admitted predicate and actual participants or return the exact missing governor; assignment establishes no responsibility; and
  - for prospective maintenance guidance, retain only the change-control note, intended maintenance condition or `U.WorkPlan`, and scope tag; this content asserts no performed Work, current assignment, or responsibility.

The catalogue entry only cites these values, which are defined or constrained elsewhere and creates none of them.

Library, edition, and family designators are lexical values under `R_L`, not local ValueKinds, public U-kinds, episteme identity discriminators, or entities by spelling. A local family declaration is claim content in `G_L`, not automatically a separate entity or episteme. Its compact locator `<editionDesignator(L), familyDesignator>` is a retrieval aid under `R_L`; it does not replace L's C.2.1 identity. If a receiving use truly needs one declaration as a separately identified episteme, constitute that new episteme independently under C.2.1 rather than inferring it from a row.

Normative constraints:

1. Within one exact `G_L`, every family designator **SHALL** retrieve exactly one local declaration claim block under `R_L`.
2. A catalogue **SHALL NOT** define new kernel episteme kinds, id kinds, reference kinds, or publication-face/form kinds merely to type its fields.
3. A catalogue **MAY** be a core FPF catalogue or an organization-local extension when the same constitution, resolution, and family-declaration discipline remains recoverable.

#### E.17.1:4.3 - Local bundle declaration and its ordinary family designator

A bundle declaration is a bounded claim block inside exact `G_L`. It states one finite, non-empty recurring family of exact `U.ViewpointRef` values drawn from exact catalogue subject `K_L`. Every reference resolves under `R_L` to one exact viewpoint episteme edition P that has already gained `U.Viewpoint` membership under E.17.0. The declaration neither admits P nor changes P's C.2.1 identity.

Its minimum claim content is:

- one ordinary `familyDesignator`, unique within exact `G_L` under `R_L`;
- one exact target-kind compatibility condition: either the by-value criterion actually used for this family or a reference that resolves to the exact ClaimGraph defining or constraining the admitted target kind; if member viewpoints use different fixed target-kind criteria, the declaration states the exact compatibility rule rather than inventing a common superclass token;
- `viewpointRefs`, one finite non-empty set of exact `U.ViewpointRef` values;
- optional references that resolve under their applicable schemes to exact archetypal-grounding examples or sections, with their intended recognition use stated;
- optional alignment claims naming the exact source and relation when a real correspondence is asserted; and
- optional references that resolve under their applicable schemes to exact annex assets, each with its local role such as lexical note, Bridge material, A.16 move-publication note, example, or SoTA companion.

The family designator retrieves the declaration claim block inside exact L. A member `U.ViewpointRef` resolves exact P, and any reader-facing viewpoint token is only P's designator. The family designator, declaration claim block, reference, viewpoint designator, P, and L are distinct; no token, list position, prefix, alias, or member spelling substitutes for an exact episteme or reference.

The compatibility condition neither selects an actual EntityOfConcern for a describing use nor supplies or changes any member P's fixed target-kind criterion. Those claims remain in exact P and E.17.0 conformance. A bundle is not a bundle of views, files, forms, carriers, or publication occurrences. If a receiving use needs an A.22 structure among the member viewpoints, it separately recovers exact obtaining relations and selects that structure; declaration adjacency or order is not structure.

Changing the member-reference set, family meaning, compatibility condition, or the interpretation supplied by `R_L` changes `G_L` or the effective scheme and therefore identifies another catalogue episteme. Repackaging, annex layout, publication form, carrier, or audience does not reidentify unchanged L or any unchanged member viewpoint episteme.

#### E.17.1:4.4 - Import discipline into `MultiViewDescribing`

When a describing use names a family designator, it resolves exact catalogue edition L and its effective `R_L`, retrieves the declaration claim block designated inside `G_L`, and then names the exact imported reference subset `Sigma`. If exact L or the declaration is not already recoverable, use §4.2 to establish `<G_L, K_L, R_L>` before import:

- `Sigma` is a subset of that declaration's `viewpointRefs` in exact L;
- every member is an exact `U.ViewpointRef` resolving to one admitted viewpoint episteme edition P;
- every candidate episteme E used under a member is independently identified under C.2.1 and is a `U.View` only when `EpistemeViewpointConformanceRelation(E,P)` obtains; and
- every actual one-viewpoint selection for one describing use carries one singular `viewpointRef`; importing the family neither selects P for that use nor establishes conformance.

A local subset names exact catalogue edition L, the source family designator, and the member references actually used, while keeping omitted members visible as unused or intentionally excluded. A multi-library use preserves each exact `<editionDesignator(L), familyDesignator>` source and member provenance rather than flattening everything into one unnamed family. If one use selects several viewpoints, it constructs their C.13 collection with exact membership; it does not overload one reference or infer a new family from adjacency.

Construction, identity viewing, transformation, declaration membership, selection, naming, rendering, or publication grants neither `U.Viewpoint` nor `U.View` membership. A local overlay may add didactic or publication material without changing exact L. Changing a member viewpoint's meaning, the reference target, membership set, or family meaning requires a new local catalogue edition or family declaration rather than silent mutation under the inherited family designator.

#### E.17.1:4.5 - Guard and naming discipline

- A viewpoint bundle is a family of **viewpoints**, not a bundle of views or documents.
- The family designator is an ordinary lexical value under `R_L`, not a local id kind, publication-face/form kind, reference, or entity.
- Engineering viewpoint designators and publication viewpoint designators may coexist, but their namespaces **SHALL** remain disambiguated.
- Bundle semantics come from the exact viewpoint episteme editions resolved by its member references, not from the spelling pattern of the family designator.

#### E.17.1:4.6 - Publication and representation stay outside the bundle

A published library is the same selected C.2.1 episteme edition participating in exact E.24.PUB relations:

- `PublicationFormExpressionRelation` relates that selected edition, one exact publication form, and one exact bounded-use declaration;
- `PublicationFormBearingRelation` relates one exact `U.PresentationCarrier` and that form; and
- `EpistemePublicationRelation` relates the selected edition, audience declaration, bounded-use declaration, form, and carrier for one maximal continuous availability interval.

Changing a participant or restoring availability after a gap yields another publication occurrence under E.24.PUB; it does not reidentify unchanged L or any member viewpoint. Rendering, printing, or uploading is separate system-performed `U.Work`. C.29 applies when a diagram or catalogue rendering represents independently recovered declarations or viewpoint epistemes. Publication, representation, form, carrier, or rendering grants no viewpoint or view membership and makes no represented world-side relation obtain.

### E.17.1:5 - Archetypal Grounding


**Tell.** A viewpoint bundle library lets FPF say "use this already-defined viewpoint family" without confusing that family with the concrete views or publication faces that later realize it.

**Show (System; hypothetical template instance).** E.17.2 can guide one project to bind local references `r_functional`, `r_procedural`, `r_allocation`, and `r_module` to exact project P editions inside one constituted catalogue L. Until those bindings and their resolution under exact `R_L` exist, these names are variables and no reusable TEVB family value is present.

**Show (Episteme; hypothetical family shape).** A project could bind local references for risk, control, compliance, and operations viewpoints in one exact catalogue declaration. The labels alone are not references or exact P editions; this example becomes reusable only after that project supplies complete `<G_L, K_L, R_L>`, exact bindings, and one ordinary family designator.

### E.17.1:6 - Bias-Annotation

After a recurring family-level use is established, the pattern biases FPF toward catalogue reuse and against silently re-inventing that same family under local labels. For a one-off selection, keep the exact references local: the catalogue cost is justified only when reuse, comparison, or maintenance changes a named practitioner action.

### E.17.1:7 - Conformance Checklist

- `CC-VBL-0` Exact `<G_L, K_L, R_L>` constitutes L; ordinary import resolves an admitted L and its declaration without reconstructing that triple, while authoring, admission, or disputed identity opens the complete §4.2 check. Within `G_L`, each ordinary family designator retrieves exactly one local declaration claim block and remains distinct from L, member references, P designators, views, forms, and carriers.
- `CC-VBL-1` Every member is an exact `U.ViewpointRef` resolving to one independently admitted viewpoint episteme edition whose fixed target-kind criterion is compatible with the bundle constraint.
- `CC-VBL-2` Bundle membership, position, spelling, alias, packaging, or publication admits no P as `U.Viewpoint`; E.17.0 alone defines the membership test.
- `CC-VBL-3` A describing use imports an exact subset from exact `<editionDesignator(L), familyDesignator>`, preserves omissions and provenance, and selects any one actual P through one singular reference.
- `CC-VBL-4` Every candidate E is independently identified and gains `U.View` membership only through obtaining E/P conformance—not through construction, selection, bundling, naming, form, carrier, rendering, or publication.
- `CC-VBL-5` A family designator is not used as an id kind, publication-face/form kind, carrier kind, viewpoint reference, or substitute for an exact member.
- `CC-VBL-6` Changes to member references, targets, family meaning, or compatibility constraints create another catalogue edition or family declaration; publication or annex-only change does not reidentify unchanged P.
- `CC-VBL-7` Multi-bundle imports preserve exact catalogue provenance and collisions only. Same-scheme comparison names its exact predicate and participants and applies the pattern that defines that predicate. Cross-context comparison resolves exact F.17 cells, obtaining F.9 Bridge, separate `<u,d,r,t>` claim, and required A.10 or B.3 reliance; otherwise it stops at lexical or structural contrast.
- `CC-VBL-8` E.24.PUB expression, bearing, publication, recurrence, rendering work, and C.29 representation remain distinct, grant no viewpoint or view membership, and make no represented world-side relation obtain.
- `CC-VBL-9` A bundle intended for non-expert reuse should provide references that resolve under their applicable schemes to exact archetypal-grounding examples or sections for its member viewpoints; grounding aids recognition but grants no membership.

### E.17.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Publication-face hijack** | A family designator is reused as a publication-face name or document type. | `CC-VBL-5` keeps the ordinary designator distinct from a publication face, form, carrier, viewpoint reference, or exact member. |
| **Bundle equals view collection** | A folder or report pack is called a viewpoint bundle even though no exact `U.ViewpointRef` values resolve to admitted `U.Viewpoint` epistemes. | `E.17.1` defines the bundle as a declared family of exact viewpoint references, not a file grouping. |
| **Silent local drift** | A local project keeps the old family designator but swaps in different viewpoints. | `CC-VBL-6` requires another catalogue edition or family declaration when member references, targets, family meaning, or compatibility constraints change. |
| **Namespace collapse** | Engineering and publication viewpoint designators are mixed as if they were one lexical namespace. | The solution keeps the designator namespaces distinct and requires explicit attribution. |

### E.17.1:9 - Consequences

| Benefit | Trade-off / Mitigation |
|---|---|
| **Reusable viewpoint families.** Stable family designators within exact catalogue editions let many projects reuse the same declaration without restating it. | Catalogues need maintenance and edition discipline. |
| **Cleaner `MultiViewDescribing`.** A use can import a reviewed bundle instead of spelling out every viewpoint locally. | Local exceptions must be made explicit rather than hidden in prose. |
| **Reusable catalogue without imported ontology.** A repeated-reference problem inside current FPF gains one local catalogue episteme while ISO 42010 remains vocabulary lineage rather than evidentiary authority or imported ontology. | Initial catalogue authoring requires care in exact C.2.1 constitution, reference resolution, and grounding. |
| **Lexical hygiene.** Family designators, viewpoint designators, views, publication faces, and publication forms stop collapsing into one label. | Authors must learn the separation once and then keep it. |

### E.17.1:10 - Rationale

`MultiViewDescribing` already assumes that viewpoint plurality exists. `E.17.1` supplies packaging and provenance discipline for that plurality, including cases where viewpoints are used to re-express positions in `U.LanguageStateSpace` or trajectories in `U.LanguageStateMoveTrajectory`. Without it, every domain can only improvise locally and member provenance becomes fragile. Semantic correspondence is a separate result: same-scheme comparison states its exact predicate and participants, while cross-context comparison uses F.9 and a bounded-use reliance path.

### E.17.1:11 - Source status, local rationale, and reopen condition

ISO 42010 is retained only as historical vocabulary lineage for the words *view* and *viewpoint*. It is not current architecting SoTA, does not supply FPF identity or conformance laws, and does not justify this catalogue architecture. No current external problem-solving source or reusable source comparison is claimed by this E.17.1 edition.

The present architecture is therefore an explicit local FPF rationale. The concrete problem is repeated use of the same exact E.17.0 viewpoint episteme editions: users need to resolve exact references, preserve source catalogue and omission provenance, and avoid reidentifying P or turning a family label into membership. One C.2.1 catalogue ClaimGraph with local declaration claim blocks is the least additional object that answers those actions while reusing C.2.1 identity, E.17.0 membership, C.13 collection, F.9 comparison, and E.24.PUB publication boundaries.

SysML v2 is deliberately absent from the positive source basis and is not treated as lineage for this question. Official status, search prominence, systems-oriented naming, and prospective scope are not evidence that it solves the exact reusable-catalogue and practitioner-use problem here. This exclusion imports no contrary SysML ontology claim; it only prevents popularity or status from standing in for demonstrated contribution.

Reopen the local architecture if an exact current source or exercised project catalogue demonstrates a simpler way to preserve reference resolution, exact P identity, subsets, omissions, provenance, and cross-context comparison without losing any of those practitioner actions; or if project replay shows that one catalogue ClaimGraph with local declarations adds apparatus without changing a practitioner action. Until then, describe this as provisional local design, not source-established SoTA.

### E.17.1:12 - Relations

- **Builds on:** `C.2.1` for library and member-episteme identity; `E.17.0` for exact P membership, reference resolution, singular use selection, and sole E/P view-membership rule; `C.13` for explicit imported collections; `A.22` for any separately selected organization; `A.6.2-A.6.4` for optional episteme-construction histories; `A.7`, `E.7`, and `E.10` for carrier, authoring, and naming discipline; `E.24.PUB` for publication; and `C.29` for representation.
- **Constrains:** E.17.0 consumers whenever they import a reusable family; an import narrows eligible references but neither selects one P for a use nor proves conformance.
- **Coordinates with:** `C.2.2a`, `A.16.0`, `E.17`, `E.17.2`, `E.18:5.12`, `F.9`, `F.9.1`, and domain-specific families requiring stable reuse.
- **Protects:** exact separation among catalogue triple `<G_L, K_L, R_L>`, catalogue episteme L, local declaration claim block, ordinary family designator, `U.ViewpointRef`, P designator, P, candidate/View E, any A.22 structure, form, carrier, publication occurrence, and C.29 representation.

#### E.17.1:12.1 - Resolvable annex references for thin bundles

An ordinary project family designator may be accompanied by references that resolve under the applicable source or reference scheme to exact annex assets. Each reference states its local role—such as `lexical`, `bridge`, `movePublication`, `examples`, optional `sota`, or optional `pilotTrace`. Neither the field spelling nor the role value creates a new reference kind, manifest entity, or typed annex asset. This keeps the declaration claim block thin while allowing A.16 move-publication notes, lexical material, Bridge material, and examples to remain explicit rather than folded into the core family claim.

### E.17.1:13 - Bundle Anatomy and Member Discipline

A viewpoint-bundle library becomes thin and reusable only when the bundle itself stays stable while the member viewpoints remain explicit enough to review independently. The bundle therefore has two simultaneous obligations: coherence at the family level and clarity at the member level.

#### E.17.1:13.1 - What a viewpoint member should make explicit

Each `U.ViewpointRef` member inside a reusable bundle resolves to one exact viewpoint episteme edition whose claim content makes explicit at least:

- the **concern family** it brings into focus,
- exact **stakeholder or audience referents** only when they change the concerns,
- the exact **target-kind criterion** it carries and the compatibility condition under which this family can reuse it,
- the **independently admitted episteme kinds** whose exact membership rules allow candidates under that viewpoint,
- any **bundle-specific conformance notes** later users must retain, plus an exact reference that resolves to the comparison claim or F.9 Bridge when either has independently been established; a note or reference creates no correspondence.

`E.17.1` does not redefine the internals of `U.Viewpoint`. It states what must remain visible if a viewpoint is to be reused as part of a bundle rather than as an undocumented local label.

#### E.17.1:13.2 - Bundle-level coherence

A bundle is not just a bag of viewpoints with one shared prefix. A coherent bundle should answer a recognizable family-level question, such as:

- *which engineering concerns are standard for holon description?*
- *which governance perspectives are required for a service review?*
- *which research-method viewpoints recur across inquiry reports?*

If the member viewpoints do not share that family-level purpose, the result is not one bundle but an uncurated catalogue fragment.

#### E.17.1:13.3 - Thin bundles, rich annexes

`E.17.1` intentionally allows bundles to stay thin. Rich companion material such as:

- lexical discipline notes,
- bridge overlays,
- A.16 move-publication notes,
- worked examples,
- or SoTA references

may be linked through references that resolve under their applicable schemes to exact annex assets, with each reference's local role stated. This preserves a stable declaration claim block while still letting reuse packages carry enough didactic material and review help.

### E.17.1:14 - Import, Subset, and Multi-Bundle Coordination

The value of viewpoint bundles appears most clearly when they are imported, subsetted, and coordinated across several reused families. Those cases need explicit discipline so that a local project does not quietly mutate what it claims to be reusing.

#### E.17.1:14.1 - Subset selection

A `MultiViewDescribing` use may legitimately import only a subset of a bundle's viewpoint references. When it does so, it should declare:

- which ordinary family designator is the source,
- which viewpoint members are actually in local use,
- and whether the omitted members are simply unused or are intentionally excluded because the local scope does not require them.

The local family must not speak as if it had imported the whole bundle while silently dropping inconvenient viewpoints.

#### E.17.1:14.2 - Local overlays vs new bundles

A local project often wants a small adaptation: one extra concern note, one narrower stakeholder emphasis, one local naming convention. `E.17.1` prefers explicit overlays or new editions over silent mutation.

A practical rule is:

- if the local project selects a subset or adds only didactic/publication material, keep exact catalogue edition L and its declaration unchanged and declare the local subset or annex; do not treat the overlay as declaration content;
- if the local project changes viewpoint membership or meaning, publish a new local catalogue edition or a new family declaration.

This is how bundle reuse remains trustworthy across organizations.

#### E.17.1:14.3 - Multi-bundle coordination: provenance first, comparison separately

Many real description families need more than one bundle, for example:

- one engineering viewpoint family,
- one safety or assurance family,
- and one governance or publication-oriented family.

Preserve the exact provenance of every imported `U.ViewpointRef` and resolved P as `<editionDesignator(L), familyDesignator, member reference>`. That tuple answers where a member came from. It establishes no semantic sameness, difference, correspondence, translation, substitution, or admissible comparison by itself.

If the compared meanings are interpreted under one exact effective reference scheme, identify the exact P editions or claim subgraphs being compared, state the exact comparison predicate, polarity, scope, and participants, and apply the pattern that defines that predicate. If no direct semantic predicate is current, report only the observable lexical or structural contrast—members, omissions, order, target criteria, or claim-shape differences—and do not call it correspondence.

If the comparison crosses effective schemes or semantic contexts, first resolve the two exact F.17 `SchemeSenseCell` endpoints. Use F.9 only when its direct Bridge predicate is actually satisfied. Then state the proposed comparison or reuse separately as one bounded C.2.1 use claim about that exact Bridge with `<u,d,r,t>` and polarity, and recover the exact A.10 reliance disposition or the B.3 assurance branch when its threshold is met. Without the exact cells, obtaining Bridge, bounded-use claim, and required reliance path, stop at lexical or structural contrast. Catalogue provenance remains useful in every branch, but never substitutes for any of them.

#### E.17.1:14.4 - Engineering vs publication families

Some contexts need both engineering viewpoints and publication viewpoints. `E.17.1` permits both, but it does not allow one family designator to erase the distinction. A family that imports both kinds must keep the namespaces and catalogue origins explicit so that authors do not confuse *how the holon is being understood* with *how a publication face/form chooses to expose that understanding*.

### E.17.1:15 - Worked family shapes, not shipped catalogue values

#### E.17.1:15.1 - Hypothetical TEVB project binding

E.17.2 supplies an authoring template, not a repository-shipped family. One project may constitute exact catalogue L and bind four local variables:

- `r_functional -> P_functional`,
- `r_procedural -> P_procedural`,
- `r_allocation -> P_allocation`,
- `r_module -> P_module`.

Only after those are exact `U.ViewpointRef` values resolving exact admitted P editions under L's effective scheme can the project's ordinary family designator retrieve a reusable local declaration. Another project with similarly spelled variables or labels has not imported this family unless it resolves the same exact L and references.

#### E.17.1:15.2 - Hypothetical governance and risk shape

A project may author a governance-oriented declaration with local reference variables such as:

- `r_risk -> P_risk`,
- `r_control -> P_control`,
- `r_compliance -> P_compliance`,
- `r_operations -> P_operations`.

This is an example of a possible declaration shape, not an exact current family. Each left-hand variable must be bound to an exact local `U.ViewpointRef`; each right-hand variable must be bound to one exact P independently admitted under E.17.0; and exact L, `R_L`, and the family designator must exist before reusable import is claimed. The four positions recur together but remain non-interchangeable.

#### E.17.1:15.3 - Hypothetical research-method shape

A project may likewise consider local variables `r_theory`, `r_experiment`, `r_inference`, `r_limitations`, and, where appropriate, `r_reproducibility`. This list teaches a candidate family shape only. A local inquiry note can import a subset only after the project has constituted exact L, bound each retained variable to an exact reference and P, and made omitted members visible in one actual declaration claim block.

#### E.17.1:15.4 - Cross-family description relation positions

A serious project may use one materialized local TEVB instance for its design family, another exact local governance family for program oversight, and another exact local publication-oriented family for publication faces and forms. `E.17.1` keeps these relation positions reviewable by preserving which exact catalogue and declaration each viewpoint came from and by preventing a final publication face or form from masquerading as the catalogue itself.

### E.17.1:16 - Authoring and Review Guidance

#### E.17.1:16.1 - For bundle authors

Bundle authors should ask:

- what recurring family is being named,
- which viewpoints truly belong together in that family,
- what local didactic publications or examples belong in annexes instead of the bundle core,
- and whether the bundle is stable enough to deserve a reusable family designator.

A good bundle is not maximal. It is coherent, reviewable, and reusable.

#### E.17.1:16.2 - For reviewers

Reviewers should inspect both levels:

- **member level** - are the included viewpoints individually explicit enough to be reused?
- **bundle level** - do they actually form one coherent family rather than one convenient list?

They should also check whether a local project has silently forked the bundle while still using the inherited family designator.

#### E.17.1:16.3 - For integrators and librarians

Integrators should keep libraries small, curated, and editioned. Publish only the smallest declaration set the current reuse needs:

- one stable core declaration when a recurring family is established,
- one explicit local extension only when local membership or meaning changes,
- and one clear subset declaration only when the current use imports a subset.

Do not create all three by default. Library sprawl destroys the cognitive advantage that reusable bundles are supposed to provide.

### E.17.1:17 - Edition and Migration Notes

#### E.17.1:17.1 - Rename vs semantic change

A lexical rename that leaves viewpoint meaning and membership unchanged may be treated as a naming-layer migration. A change in membership, concern, admissibility, or member semantics is not just a rename; it requires another catalogue edition or family declaration.

#### E.17.1:17.2 - Migration from local `Sigma` lists

Legacy `MultiViewDescribing` uses often publish only one local list of viewpoints. Migration should proceed by:

1. identifying recurring families across several such local lists,
2. publishing those families as explicit bundles,
3. then rewriting the local families to import the new ordinary family designator and declare any subset selection explicitly.

This sequence preserves provenance and avoids pretending that the reusable family had always existed.

#### E.17.1:17.3 - Migration from publication-face/form-bound naming

If a legacy practice uses one label interchangeably for a viewpoint family, a viewpoint, a report section, and a publication face, migration separates those positions explicitly. The ordinary family designator remains at the declaration layer; exact `U.ViewpointRef` values resolve P while any reader-facing viewpoint token is only P's designator; publication-face names remain publication-layer vocabulary.

#### E.17.1:17.4 - Boundary to annex growth

Annex references are useful, but a declaration should not become a thin shell hiding all of its meaning elsewhere. The core declaration claim block still needs enough explicit member and family structure to stand on its own. Annexes deepen reuse; they do not replace the declaration's primary claims.
### E.17.1:18 - Import Collision and Alias Discipline

#### E.17.1:18.1 - A family designator is not a synonym bag
An ordinary family designator does not mean that all member viewpoints are interchangeable labels for one concern. It means that one declaration claim block says a reviewed family of viewpoints is intended to recur together. Authors should therefore resist the drift where one convenient designator begins to substitute for all of its members.

#### E.17.1:18.2 - Import collision rule
When two imported bundles contribute viewpoints with overlapping lexical names, preserve the originating viewpoint designators and exact catalogue provenance rather than silently merging the members. Inspectable collisions make provenance adequate; they do not show that the local senses correspond or that either member may substitute for the other.

#### E.17.1:18.3 - Alias boundary
Local teaching aliases may be added for readability, but the alias must dock to explicit member viewpoints and must not erase bundle provenance. If the alias starts doing bundle-selection work by itself, it is making an unsupported bundle-selection claim and should be replaced by explicit member references.

### E.17.1:19 - Bundle Projection and Comparative Use

#### E.17.1:19.1 - Projection to local subsets
A description family may project only a subset of a reusable bundle. This is admissible if the omitted members remain visible as omitted rather than disappearing into an ad hoc local list. Projection keeps bundle provenance intact while acknowledging that local publication rarely uses every member.

#### E.17.1:19.2 - Comparative bundle use

First decide whether the comparison stays inside one exact effective reference scheme. In that branch, name the exact members or claim subgraphs, comparison predicate, polarity, scope, and participants, then apply the pattern that defines the predicate; provenance merely identifies their catalogue origins. If only names, member sets, omissions, or structures can be compared, state that bounded lexical or structural contrast and stop.

When local senses cross schemes or semantic contexts, resolve the exact F.17 cells and apply F.9. Claim a semantic correspondence only when the exact Bridge obtains. A proposed comparison, translation, or reuse also needs its own bounded-use claim naming the proposed use, direction, correspondence rule, tolerated loss, and polarity, plus a current A.10 reliance disposition or the B.3 assurance branch when its threshold is met. Similar family labels, matching designators, matching member counts, or provenance tuples establish none of those results. Use F.9.1 only to add a separate stance episteme whose EntityOfConcern is that bounded-use claim; it neither annotates nor reidentifies the Bridge and cannot widen the claim.

#### E.17.1:19.3 - Boundary to publication-face design
A publication face may render one composite presentation of several viewpoints, but the face is not the bundle. `E.17.1` therefore requires the underlying member structure to remain recoverable even when a public-facing document flattens it for readability.

### E.17.1:20 - Review Matrix and Catalogue Maintenance

A reviewer can test a viewpoint bundle library with five questions:

1. **Do the member viewpoints still have explicit standalone meaning?**
2. **Does the local declaration and its family designator describe one coherent recurring family rather than one convenience list?**
3. **If a subset is imported, is the omitted remainder still visible as omission rather than silent deletion?**
4. **If several bundles interact, is exact provenance preserved without being called correspondence, and does any actual comparison follow the correct same-scheme or F.9 cross-context branch?**
5. **Has a publication face started impersonating the library itself?**

Prefer small, provenance-preserving declarations inside exact editioned catalogues over lexical mega-families that are easy to name but hard to reuse truthfully.
### E.17.1:End

