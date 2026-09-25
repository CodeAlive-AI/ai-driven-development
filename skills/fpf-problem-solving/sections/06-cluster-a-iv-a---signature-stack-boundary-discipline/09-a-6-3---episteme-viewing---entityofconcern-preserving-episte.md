## A.6.3 - Episteme viewing - EntityOfConcern-preserving episteme construction
> **Status:** Stable

**Use this when.** You need to derive a smaller, reorganized, or differently expressed body of claims from existing claims while keeping the same thing under discussion. In FPF terms, the source and result are independently identifiable epistemes with the same `EntityOfConcern`. The result may select, reorganize, normalize, translate, or combine claims from the named sources, but it must not add a claim those sources do not support.

**First useful result.** Write one source-to-result statement. For example:

> `Result Y is made from source X. Both are about the same named thing. Y keeps [named claims], omits [named claims], and adds no claim unsupported by [named sources].`

Then name or show the rule that selects, rewrites, or combines the claims. Do not call the construction an A.6.3 viewing unless X and Y can be identified separately and this rule can be inspected.

**What this does not decide.** A.6.3 says how Y is licensed by named sources about the same thing. It neither proves the claims true nor makes Y a `U.View`; use E.17.0 for view membership. Use A.15.1 for the work that produced Y, A.15.PROD if first constitution matters, and E.24.PUB for publication, but only when those separate facts matter.

**Builds on:** A.6.0 direct declaration structure; A.6.2 effect-free episteme morphing; C.2.1 episteme identity; E.17.0 viewpoint conformance and view membership; A.6.3.CR conservative retextualization; A.6.3.RT representation-scheme transition; A.6.4 retargeting; C.29 mathematical-lens use; A.13 Work basis; A.15.1 work; A.15.PROD local work/change/entity-identity-inception claims.

**Used by:** E.17 publication-face construction, E.17.0 multi-view describing, E.18 transformation-flow descriptions, and domain patterns that derive a smaller or differently expressed episteme from one or more source epistemes.

### A.6.3:1 - Problem frame

Engineering work often needs a different body of claims about the same thing. Examples include a safety-focused slice of a system description, a normalized technical card, a conservative translation between notations, or a coverage view built from requirements and design epistemes plus stated correspondence claims.

Several neighboring facts can all be true but are not the same fact:

1. X and Y are identified as C.2.1 epistemes;
2. Y was constructed from X under one declared viewing rule;
3. X and Y have the same EntityOfConcern;
4. Y makes no stronger claims than the identified sources license;
5. Y conforms to an exact viewpoint and is therefore a `U.View`;
6. a system performed work that first constituted Y;
7. Y was later published through an exact form and carrier.

Ordinary use may need only items 1 through 4. The remaining claims are opened independently.

### A.6.3:2 - Problem

How can a project say that Y was constructed from X about the same thing while making clear what was preserved, what was lost, and why Y adds no unsupported claim?

Keep that construction separate from the work that produced Y, any publication of Y, and any separate check that Y qualifies as a `U.View`.

Without this distinction, a query execution is treated as view membership, a generated file is treated as the episteme, a new claim is hidden as harmless formatting, or an EntityOfConcern change is smuggled into a same-entity projection.

### A.6.3:3 - Forces

| Force | Tension |
|---|---|
| Conservativity vs usefulness | A receiving episteme may reorganize, summarize, or omit claims while adding no unsupported commitment about the EntityOfConcern. |
| Same concern vs changed expression | X and Y share one exact EntityOfConcern, while claim content or effective reference scheme may differ and therefore identify another episteme. |
| Algebraic composition vs actual work | Viewings should compose and replay as mathematical constructions, while systems and work occurrences remain separate. |
| Direct source vs several-source correspondence | Some constructions use X alone; others depend on exact relations among several source epistemes. |
| Construction history vs stable kind membership | Viewpoint conformance depends on Y and the viewpoint, independently of how Y was constructed. |
| Lightweight assertion vs assurance | A readable source-to-receiving statement often suffices; disputed loss or correspondence requires exact declarations and evidence. |

### A.6.3:4 - Solution

**Local mantra.** Identify X and Y. Hold their EntityOfConcern fixed. State the conservative construction and admitted loss. Add exact correspondence dependencies when used. Test `U.View` membership separately under E.17.0 only when the receiving use needs that membership.

#### A.6.3:4.1 - Identify both epistemes independently

Before declaring a viewing, recover for each of X and Y under C.2.1:

- exact claim content;
- exact EntityOfConcern;
- effective `U.ReferenceScheme`.

X and Y are separate epistemes whenever one of those identity discriminators differs. A filename, table, diagram, query result, `viewpointRef`, or publication form is not a substitute for either identity.

If the supposed receiving item has no recoverable claim content or EntityOfConcern, stop: the receiving episteme has not been identified. If the exact EntityOfConcern differs, use A.6.4 retargeting rather than A.6.3.

#### A.6.3:4.2 - Declare the viewing construction

A.6.3 viewing is the EntityOfConcern-preserving branch of A.6.2's local effect-free arrow class. In the selected formal substrate, one viewing arrow is written `v : X -> Y` and has exact source episteme X and exact receiving episteme Y.

The reusable A.6.0 declaration describes the admitted local arrow family, rather than turning one arrow or endpoint pair into a kind:

```text
SubjectKind      = local A.6.2 EpMorphism type restricted to preserve-mode viewing arrows
RangedValueKind = admitted ordered-pair range over exact U.Episteme values satisfying the declared endpoint-kind constraints
ResultKind       = omitted; v is the declared subject and Y is its exact receiving endpoint
Applicability    = selected formal substrate, admitted endpoint kinds, viewing-rule conditions, and preserve mode
```

`EpMorphism` is a local mathematical type in the selected substrate, not a durable FPF U-kind. The arrow records the declared construction from X to Y. Section 4.6 separately governs an account of its actual execution.

A concrete viewing declaration states:

1. exact X and exact Y;
2. that `EntityOfConcern(X)=EntityOfConcern(Y)`;
3. the claim-content construction from X and any additional exact sources to Y;
4. how the source and receiving reference schemes are related;
5. preserved claim components, admitted omissions or losses, and prohibited strengthening;
6. applicability conditions and any fixed configuration needed for replay.

A separate assertion says whether this arrow supports one named receiving use and states any use-specific loss or conditions. If the current use needs an account of a query, rewrite, model, or other method being applied, identify that application and any admitted Work separately; `v : X -> Y` alone does not assert that they occurred.

#### A.6.3:4.3 - Apply the same-EntityOfConcern and conservativity laws

For every admitted `v : X -> Y`:

1. **Same EntityOfConcern.** X and Y designate the same exact EntityOfConcern. Similar labels, bridge claims, or one shared project do not establish this equality.
2. **No unsupported strengthening.** Every claim in Y about that entity is recoverable as a consequence, conservative re-expression, or explicitly admitted aggregation of claims in the identified sources under the declared reference and representation semantics.
3. **Declared loss.** Every omitted concern or claim family that affects receiving use is named, together with the condition under which the loss is admitted.
4. **Reference discipline.** A changed effective reference scheme is explicit. If the change alters available operations or representation semantics, use A.6.3.RT; apply C.29 when the transition uses a declared mathematical lens. Do not call such a change formatting.
5. **No hidden retargeting.** Subsystem-to-system, method-to-work, model-to-modeled-system, or episteme-to-publication changes are not same-EntityOfConcern viewing.

For a lightweight check, take each claim in Y—or each group covered by one rule—and point to the source claims and the selection, rewriting, or aggregation rule that licenses it. Mark omitted claim groups. If a result claim cannot be traced this way, treat it as a new claim rather than a viewing result. If support cannot be decided exactly, state the structural or domain check used as an approximation and what it cannot establish. Add a proof only when disagreement, risk, or the receiving use makes it necessary.

Truth of source claims is a separate evaluation. Conservativity says what Y is licensed to claim from the sources; it does not establish that those claims are true in the world or adequate for a decision.

#### A.6.3:4.4 - Keep optional viewpoint selection and view membership separate

For the current use of receiving episteme Y, name the describing use and exact viewpoint P only when that selection changes what the receiver reads or checks. Keep Y, its EntityOfConcern, the use, and P distinct. Selecting P is outside C.2.1 identity and does not make E.17.0 conformance obtain.

After Y is identified, apply E.17.0 only when the current use needs `U.View` membership:

```text
EpistemeViewpointConformanceRelation(Y,P) obtains
  -> the same episteme Y is a U.View
```

Directly authored Y can be a view without any A.6.3 source relation. Conversely, a valid A.6.3 construction can yield Y that fails P's concern-coverage or semantic-form rules and therefore is not a view under P.

#### A.6.3:4.5 - Distinguish direct and correspondence-mediated construction

**Direct viewing.** Y is constructed from X and fixed configuration only. The declaration names the exact claim selection or rewriting rule and any loss. No generic correspondence object is required.

**Correspondence-mediated viewing.** Y depends on several exact source epistemes or on exact relations between their claim-bearing contents. Recover each direct correspondence, realization, trace, equivalence, or consistency relation under its governing pattern before using it. Then identify the C.2.1 episteme that states or describes those relations if the construction must cite it.

Plain `correspondence model` may name that exact claim-bearing episteme for convenience. It is not a public `U.CorrespondenceModel` kind, and its graph edges or table cells do not establish the direct relations. If a needed relation lacks a governor, return the exact missing-relation blocker or use A.6.RCD.

The viewing declaration cites the exact source epistemes and exact correspondence claims on which Y depends. If Y asserts facts about a correspondence episteme, evidence, or evaluation result, those assertions belong to Y's claim content and follow C.2.1's identity rule. The cited objects remain independently identified, and the assertions still require the support specified by the viewing law.

#### A.6.3:4.6 - Keep mathematical construction, work, production, and publication distinct

Describe querying, rewriting, modeling or rendering in ordinary practitioner terms. When the account claims a particular dated `U.Work` occurrence, establish its A.13 basis and A.15.1 admission; identify the system that performed the work and the method it used. The source epistemes, parameters, tools, and receiving entities participate only through their direct relations or A.6.1 operation bindings.

If that work first constitutes exact episteme Y and the identity-inception claim matters, A.15.PROD governs the local work/change/identity claim. Neither work nor inception establishes conservativity or E.17.0 conformance.

If Y is made available, E.24.PUB separately identifies the publication occurrence, publication form, and `U.PresentationCarrier`. Publication neither creates the A.6.3 construction nor grants `U.View` membership.

#### A.6.3:4.7 - Preserve composition and replay

The selected formal substrate supplies the identities, admitted compositions, and arrow equivalence. For fixed source epistemes, rules, reference semantics, correspondence dependencies, and configuration:

- identity viewing preserves the same C.2.1 episteme;
- composing `f : X -> Y` with `g : Y -> Z` gives the admitted composite `compose(g,f) : X -> Z` under A.6.2 P3;
- if a separately declared construction operation is deterministic, replay with the same admitted inputs yields the same receiving C.2.1 identity discriminators;
- random seeds, model editions, external service state, or timing that can change Y are explicit inputs to the work or declaration, not hidden meta;
- a normalization repeat claim identifies `n_X : X -> Y` and the next arrow `n_Y : Y -> Z`, establishes `Z = Y` under C.2.1, and witnesses `compose(n_Y,n_X) ≃ n_X` under the declared arrow equivalence. One `X -> Y` arrow is self-composable only when X = Y.

A composition requires the exact middle episteme to match. A claim that two routes yield the same receiving episteme requires equality of all three C.2.1 identity discriminators; representation equivalence alone does not establish that identity. The repeat claim requires a fixture or proof under A.6.2 P4.

#### A.6.3:4.8 - Stop at the lightest sufficient statement

For ordinary use, this can be enough:

> `Safety summary Y is conservatively constructed from plant description X; both concern Plant-7; Y omits maintenance-cost claims and introduces no safety claim not recoverable from X.`

Add a reusable declaration, explicit mathematical arrow, correspondence episteme, evaluation result, work occurrence, production claim, or publication objects only when a named receiving work or decision depends on that object.

### A.6.3:5 - Worked cases

#### A.6.3:5.1 - Safety-focused system description

X is a rich system-description episteme about exact plant S. Y is a smaller episteme about the same S containing only safety-critical functions, hazards, and mitigations recoverable from X. The viewing declaration names the filter and omitted claim families. A.6.3 construction obtains. Y becomes a `U.View` only after exact safety viewpoint P is resolved and `EpistemeViewpointConformanceRelation(Y,P)` obtains.

#### A.6.3:5.2 - Directly authored view without a source

Architecture episteme E is authored directly against maintainability viewpoint P and passes E.17.0 conformance. E is a `U.View`, but no A.6.3 viewing from another episteme exists. Inventing an identity source merely to satisfy this pattern would falsify the construction history.

#### A.6.3:5.3 - Query result that fails conformance

Query Q constructs Y from source X while preserving the same system and making only licensed claims. Y omits one concern required by viewpoint P. A.6.3 construction is valid; E.17.0 conformance fails, so Y is not a view under P.

#### A.6.3:5.4 - Normalized publication card

X and Y are separately identified epistemes about exact morphism f. Y reorders claims and normalizes names without changing their interpretation. `NormalizeTechCard : X -> Y` is a direct viewing. For a repeat claim under the same scheme and normalization rules, identify the next normalization arrow `n_Y : Y -> Z`; establish `Z = Y` under C.2.1 and `compose(n_Y, NormalizeTechCard) ≃ NormalizeTechCard` under the substrate's declared arrow equivalence, with a fixture or proof. A later publication occurrence makes Y available through a TechCard form. Y is called `U.View` only if it conforms to the exact publication viewpoint; the form and carrier remain separate.

#### A.6.3:5.5 - Cross-model coverage

Requirements episteme R and design episteme D concern exact system S. Exact realization relations connect particular requirements to design elements. A correspondence assertion episteme states those occurrences. Receiving episteme Y selects only requirements with an obtaining realization relation. A.6.3 records the correspondence-mediated construction from the exact sources to Y; the assertion episteme and matrix representation remain separate from the realization occurrences.

#### A.6.3:5.6 - Retargeting boundary

X concerns pump P-14. A proposed Y concerns the whole cooling skid. Even if every Y claim is derived from X plus neighboring descriptions, A.6.3 does not apply because the exact EntityOfConcern changed. Use A.6.4 and state the retargeting invariant.

### A.6.3:6 - Consequences

| Gain | Cost or boundary |
|---|---|
| Construction history is inspectable without defining view membership. | X and Y must be independently identified before the construction is asserted. |
| Direct authoring and generated epistemes coexist. | A generated result needs a separate E.17.0 test before it can be called a view. |
| Correspondence-mediated constructions can use exact domain relations. | Graph edges and trace tables cannot substitute for relation obtaining. |
| Work and publication stay outside the mathematical construction. | Tool execution and availability require their own patterns when current. |
| Composition can be replayed. | Hidden state or undeclared loss invalidates the algebraic claim. |

### A.6.3:7 - Rationale and SoTA-Echoing

| Source or practice line | Adopted move | Rejected overread | Practical effect |
|---|---|---|---|
| Lenses, optics, and compositional transformation research | Use identity, composition, conservativity, and explicit loss as checks over episteme-to-episteme construction. | The mathematical construction does not itself establish that a direct world-side relation obtains. | Viewing arrows can be composed and replayed while operation applications, Work occurrences, and world-side relations remain separately governed. |
| Bidirectional transformation and model-synchronization practice | Make cross-model correspondence dependencies explicit and test path agreement. | A generic correspondence record or graph edge does not establish correspondence. | Coverage and consistency viewing declarations cite exact source relations, so broken dependencies can be repaired locally. |
| Model-based view-as-query practice | Treat query and projection as common construction routes. | Query execution does not establish E.17.0 conformance. | Generated and directly authored epistemes meet the same independent E.17.0 membership rule. |
| FPF C.2.1 and E.17.0 architecture | Keep episteme identity, viewing construction, conformance, evaluation, work, production, and publication separate. | — | The next engineering action can rely on the exact relation it actually needs. |

### A.6.3:8 - Conformance checklist

1. X and Y each have recoverable C.2.1 identity.
2. X and Y have the same exact EntityOfConcern; otherwise the route is A.6.4.
3. The declaration states the exact claim construction, reference semantics, applicability, preserved content, and admitted loss.
4. Y introduces no unsupported commitment about the EntityOfConcern.
5. Every correspondence-mediated dependency resolves to exact source epistemes and governed direct relations.
6. `U.View` is asserted only after independent E.17.0 conformance.
7. A viewpoint selected for a named describing use is not used as membership evidence and does not enter X or Y identity.
8. Systems, tools, work, parameters, and production claims are recovered separately when actual construction work matters.
9. Publication occurrence, form, carrier, and rendering remain separate from X, Y, and v.
10. Composition, deterministic replay, and declared loss pass for the receiving use.
11. Ordinary use stops without materializing objects the next work or decision does not need.

### A.6.3:9 - Relations

- **A.6.0** supplies the direct declaration structure used in A.6.3:4.2.
- **A.6.2** supplies the effect-free morphism and composition discipline.
- **C.2.1** identifies source and receiving epistemes.
- **E.17.0** alone governs `U.Viewpoint`, conformance, and `U.View` membership.
- **A.6.3.CR** governs conservative textual re-expression when wording and organization are the main change.
- **A.6.3.RT** governs same-EntityOfConcern representation-scheme transition with explicit recoverability and loss.
- **A.6.4** governs a changed EntityOfConcern.
- **C.29** governs a declared mathematical-lens use of the construction or correspondence, including a diagram used for that mathematical claim.
- **A.13** supplies the basis for an explicit dated Work claim; **A.15.1 and A.15.PROD** govern its admission and any local entity-identity-inception or completion claim.
- **E.24.PUB** governs publication occurrence, form, and carrier.
- Use **A.6.RCD** when a needed correspondence relation lacks a governed expression.

### A.6.3:End
