## C.2.7 - `LanguageStateRepresentationFactorBundle` — How Is the Representation Organized?

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state representation-factor bundle.

**Use this pattern when.** Use C.2.7 when a comparison or use depends on how an episteme is represented: the distribution of its code, its sparsity or its symbolic structure. Identify the representation and the units being assessed. An ordinary description can suffice when the receiving use needs no factor-bundle claim.

**What goes wrong if missed.** One representation label such as `symbolic`, `distributed`, or `encoding basis` starts doing too much work: it hides articulation, closure, source or use conditions, Bridge loss, or comparison assumptions.

**What this buys.** A comparison of representation factors on explicit bases, while keeping articulation, closure and source or use claims independently grounded.

### C.2.7:1 - Problem frame
Published position claims in the declared language-state chart over `U.CharacteristicSpace` must keep representation factors such as locality, sparsity, and symbolicity distinct.

### C.2.7:2 - Problem
Using `EncodingBasis` without its underlying factors collapses several independent choices. That makes comparison brittle and encourages one-factor stories such as distributed = informal or local = precise.

### C.2.7:3 - Forces
| Force | Tension |
|---|---|
| **Comparability vs reductionism** | Allow comparison while preserving the distinctions among factors. |
| **Compact core vs extensibility** | Keep a minimal starter bundle while leaving room for domain-specific refinements. |
| **Representation vs source and use** | Describe how information is represented while retaining the distinct claims about its source and use conditions. |

### C.2.7:4 - Solution
`LanguageStateRepresentationFactorBundle` is a factor bundle, not one scalar characteristic. The core starter set for the comparison questions below is:

- `LocalityDistribution`
- `Sparsity`
- `Symbolicity`

A local alias such as `EncodingBasis` shall identify the factors and readings it summarizes.

#### C.2.7:4.0a - Factors and their readings

`LanguageStateRepresentationFactorBundle` groups readings of distinct representation Characteristics. Each factor needs its own meaning and Scale, and the declared chart binds these under A.18/A.19. The bundle describes the representation identified in the position claim; a factor reading is distinct from that representation or its publication form.

#### C.2.7:4.1 - Minimal factor readings
| Factor | Question it answers | Typical values |
|---|---|---|
| `LocalityDistribution` | Is the representation concentrated in local units or distributed across many units? | local / mixed / distributed |
| `Sparsity` | How concentrated are activation, representation use, or descriptive marks? | sparse / mixed / dense |
| `Symbolicity` | How explicit are the symbolic structures and tokens? | symbolic / mixed / subsymbolic |

Before comparing factors, identify the representation and the units being described. A model-side code and its written summary need not have the same factors.

For example, one scheme represents four states by four distinct units, with one unit active at a time. Another represents 28 states by the unordered pairs of eight units, with two units active at a time. An individual unit identifies the state in the first scheme; a pair identifies it in the second. The active-unit fractions are equal, `1/4 = 2/8`, although locality differs. These fractions do not define a universal sparse/dense threshold.

In the second scheme, `[0,1,0,0,0,0,1,0]` and the list of active positions `{2,7}` express the same code: positions 2 and 7 are active and the other six are inactive. Suppose decoder D1 assigns that pair to state S. Both inscriptions then denote S. If decoder D2 assigns the same pair to state T, the interpretation has changed despite the unchanged list. The shorter inscription alone changes neither the underlying code nor its factors.

When the list travels separately, supply the unit order and decoding rule needed for its next use, directly or through an accessible return to the exact source content. Counting written marks instead of active units requires a different comparison basis.

##### C.2.7:4.1.1 - Why begin with these factors?

The starter set separates three questions that often change how a representation can be read or transferred. **LocalityDistribution** concerns whether one selected unit distinguishes a represented value or whether a combination is needed. **Sparsity** concerns how much of the declared unit set is active or used; its reading depends on what is counted and on the local comparison criterion. **Symbolicity** concerns the explicit tokens and structures available to the receiving interpretation, including the applicable decoding or composition rules. These questions can matter separately: locating a report, estimating the units used to express it and recovering its interpretation require different information.

The pair code in :4.1 explains why a count of active units cannot settle locality and why a compact inscription needs its decoder. The starter bundle keeps these distinctions available without requiring a complete model of the representation. Select only the factors that affect the receiving question, as :16.1 permits. Preserve the representation and unit basis for each reading; factors of a source model and factors of its explanation concern different representations.

An assessment aimed at reconstruction error, robustness or the effect of a causal intervention may need other Characteristics directly. Use those Characteristics when they answer the question; retain a starter factor only when its reading contributes. The gain from the shared triple is a reusable starting vocabulary for code organization, use of units and explicit symbolic structure. It is not an exhaustive representation-quality model, and it supplies no universal thresholds or empirical claim that the factors are statistically independent. Add a needed factor under :4.3 while keeping the meanings of the factors already used.

#### C.2.7:4.2 - Non-collapse rules

Representation organization, articulation and closure are assessed under their own Characteristics; source and use claims retain their direct predicates. A distributed code can be computed from an identified trace; a symbolic note can leave its meaning unclear; a sparse representation can express a claim that remains open. Assess each relevant facet on its own grounds. The representation factors alone establish neither evidence for the claim nor permission to act on it.

#### C.2.7:4.3 - Extension rule
Authors may add extra local representation factors only if the extension is published as a factor addition rather than as a new master factor that erases the core factor bundle.

### C.2.7:5 - Archetypal Grounding
**Tell.** A model-state cue can use a highly distributed representation and be obtained from an identified recorded state; a symbolic note can be low articulation if its semantics are still vague.

**Show (System).** An operator decision aid may mix sparse alert codes and symbolic method-description text.

**Show (Episteme).** A researcher can describe a distributed activation pattern in a symbolic hypothesis. Assess the model-side code and the hypothesis's expression separately; the new expression alone establishes neither the hypothesis's articulation nor its warrant.

### C.2.7:6 - Bias-Annotation
The pattern resists folk theories that try to line up one representation factor with one stage or progression story.

### C.2.7:7 - Conformance Checklist
- `CC-C.2.7-1` `LanguageStateRepresentationFactorBundle` **SHALL** be published as a factor bundle, not as a hidden scalar.
- `CC-C.2.7-2` Local aliases such as `EncodingBasis` **MAY** exist only with an explicit docking to the governed factors.
- `CC-C.2.7-3` Representation factors **MUST NOT** silently replace the source and use claims recovered through C.2.6 or `LanguageStateClosureDegree`.
- `CC-C.2.7-4` New local factors **SHALL** preserve the factor-bundle discipline.

### C.2.7:8 - Common Anti-Patterns and How to Avoid Them
- **One-factor myth.** Treating distributed/local or symbolic/subsymbolic as the whole story.
- **Progression collapse.** Equating representation shifts with formalization or closure.
- **Alias capture.** Letting `EncodingBasis` or a similar local alias erase the factor bundle.

### C.2.7:9 - Consequences
The benefit is cleaner comparison across schools, substrates, and publication forms. The trade-off is the effort needed to make the relevant factor readings explicit.

### C.2.7:10 - Rationale
Separate representation factors let the reader compare code organization while assessing articulation and closure and establishing the required source or use claims on their own grounds. The starter triple earns its place through the three receiving questions in :4.1.1. A direct selection of other representation Characteristics is preferable when it answers the actual task with less irrelevant assessment.

### C.2.7:11 - SoTA-Echoing
The triple is an FPF starting choice for :4.1.1, with bounded external comparisons:

| Source and status | Contribution and boundary |
|---|---|
| [Elhage et al., *Toy Models of Superposition* (2022)](https://transformer-circuits.pub/2022/toy_model/toy_model.pdf), pp.1–5, historical research basis | Feature directions can differ from neuron basis directions. This supports identifying the units and basis before interpreting locality or sparsity; the toy models do not establish the FPF triple for all representations. |
| [Fraser-Taliente et al., *Natural Language Autoencoders* (2026)](https://transformer-circuits.pub/2026/nla/index.html), Method and Discussion | The method maps activations to text and reconstructs activations from that text. Reconstruction and the interpretation of the explanation require their own assessment. This is a current case for selecting task-specific Characteristics alongside, or instead of, starter factors. |

### C.2.7:12 - Relations
- Builds on: `A.18`, `A.19`, `C.2.2a`, `C.2.LS`.
- Coordinates with: `C.2.6`, `A.16.0`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, `F.9` for any Bridge and bounded-use claim, and `F.9.1` only for an optional stance note about that claim.
- Constrains: language-state position publication and bridge loss notes around representation shifts.
### C.2.7:13 - Worked Examples and Factor Interaction Notes

#### C.2.7:13.1 - Distributed but explicit
The pair code in :4.1 is distributed. Publishing its unit order and complete decoding rule can make its interpretation highly articulated without changing the code's locality. A symbolic wrapper with an unspecified decoder would leave that interpretation unresolved.

#### C.2.7:13.2 - Symbolic but still low-articulation
A glossary-like note may be fully symbolic while still low in `AE` because the meaning needed by its receiving use remains unclear.

#### C.2.7:13.3 - Mixed representation publication
An operator decision aid may display alert codes beside text explaining a back-end model. Assess the alert code, the text and the model-side code on their stated units. A text summary of a distributed model does not inherit the model's distribution merely by describing it. If one bundle reports several components, identify which readings concern which component.

### C.2.7:14 - Authoring and Review Guidance

#### C.2.7:14.1 - Author prompt
To publish a representation-factor bundle, ask separately:

- how local or distributed is the representation?
- how sparse or dense is it?
- how symbolic or subsymbolic is it?
- which additional factor changes the intended comparison or use?

#### C.2.7:14.2 - Review prompt
Check whether the reported factors support the intended comparison. Do not infer unreported factors from one label without a relation that establishes them.

#### C.2.7:14.3 - Cross-facet reminder
Assurance readers should also watch for silent replacement of the source and use claims recovered through C.2.6, `AE`, or `CD` by representation talk.

### C.2.7:15 - Extension and Migration Notes

#### C.2.7:15.1 - Local extension rule
Authors may add extra local factors, but each added factor should answer a distinct question rather than duplicating locality, sparsity, or symbolicity under another label.

#### C.2.7:15.2 - Migration from alias-heavy prose
Aliases such as `EncodingBasis` or similar should be unfolded into explicit factor dockings before they are relied upon for comparison, bridge claims, or downstream use.

#### C.2.7:15.3 - Boundary reminder
`LanguageStateRepresentationFactorBundle` describes representational organization only. Admissible use, closure and source or interaction claims retain their own conditions and grounds.
### C.2.7:16 - Factor-Bundle Publication Discipline

#### C.2.7:16.1 - Minimal representation package
A bundle claim should show the readings relevant to its stated use, using the starter factors and any declared additions. A partial bundle can suffice; identify an omitted or unresolved factor when it could change the comparison or continuation. An alias must not imply that an unreported reading is known.

#### C.2.7:16.2 - No hidden scalar rule
Compact overlays such as "sparse-symbolic" are admissible only when they dock to the underlying factor bundle. No compact label may behave as a hidden master score for comparison, bridge comparison, or stage/progression talk.

#### C.2.7:16.3 - Alias docking rule
Local aliases such as `EncodingBasis` are admissible only when their docking to the governed factors is explicit and stable. If an alias compresses several factors, the compression should remain visible.

### C.2.7:17 - Factor Interaction and Cross-Facet Reading Rule

#### C.2.7:17.1 - Interaction rule
Representation factors may be related under a particular code or model. State that relation and its conditions before inferring one reading from another. Locality and active-unit fraction are distinct, as :4.1 shows. Publish the readings needed for the comparison; assess articulation independently under C.2.4.

#### C.2.7:17.2 - Cross-facet non-substitution
Representation talk must not silently replace `AE`, `CD`, or the source and use claims recovered through C.2.6. A symbolic account of a distributed code may be easier to read while leaving interpretation unclear, closure open or an operator acknowledgement still required.

#### C.2.7:17.3 - Bridge reminder
If a representation shift matters in transport across contexts, note that the shift may alter what is preserved or salient. Use `F.9` for the Bridge and its bounded-use claim when the receiving use needs a semantic relation between local senses from different contexts; use `F.9.1` only for a separate optional stance note about that claim.

### C.2.7:18 - Review Matrix and Extension Tests

#### C.2.7:18.1 - Review matrix
An assurance reader should ask:

- are all claimed factors visible in the publication or cited source;
- does any alias hide the factor bundle;
- is one factor being used as if it summarized the whole representation state;
- has representation talk started to replace articulation, closure, or source and use claims.

#### C.2.7:18.2 - Local extension test
An additional factor is justified only if it captures a distinct representational question that cannot be reduced to locality, sparsity, or symbolicity. The extra factor should extend the bundle, not become a rival master factor.

#### C.2.7:18.3 - Migration test for source terminology
For a source term such as "symbolic", "distributed" or "encoding basis", retain its source-local meaning and scope. If an FPF comparison needs factor readings, establish which factors the source actually supports and leave the others unresolved. Mere citation of the source term needs no reconstruction into a complete bundle. Test any further cross-facet claim separately.

#### C.2.7:18.4 - Bundle-comparison reminder
Representation bundles may be compared across contexts only after the compared factors are explicit. If one context uses a compact local alias and another publishes the full factor bundle, require explicit docking before treating the two descriptions as commensurable.

### C.2.7:End
