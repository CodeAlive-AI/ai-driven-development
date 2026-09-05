## C.2.6 - `U.LanguageStateAnchoringMode`

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state anchoring mode.

**Use this pattern when.** Use C.2.6 when a `U.Episteme` publication needs to say whether its current position is anchored in bodily enactment, traces, model state, document mediation, operator loop, or an explicit mixed regime.

**What goes wrong if missed.** A prose note hides an embodied, trace-based, model-latent, or operator-loop cue; bridge-loss notes disappear; and the final publication face is mistaken for the original anchoring regime.

**What this buys.** A nominal anchoring-mode characteristic that keeps source anchoring, publication face, carrier, bridge loss, evidence, and reliance claims separate while still letting teams compare language-state positions.

### C.2.6:1 - Problem frame
Published position claims in the declared language-state chart over `U.CharacteristicSpace` differ not only by articulation and closure, but by how the `U.Episteme` named in that claim is anchored to bodies, traces, model states, documents, or operator loops.

### C.2.6:2 - Problem
Without an explicit anchoring-mode declaration, embodiment and source anchoring are smuggled into informal prose or folded into representation terms. That makes cues harder to compare, hides bridge-loss notes, and leaves operator-facing language-state work without an explicit anchoring rule.

### C.2.6:3 - Forces
| Force | Tension |
|---|---|
| **Embodiment vs abstraction** | Preserve embodied and operator-facing cases while making their anchoring explicit. |
| **Small core vs real diversity** | Keep the core compact while allowing multiple admissible anchoring regimes. |
| **Comparability vs oversimplification** | Compare anchoring regimes while retaining distinctions that a text-vs-nontext split hides. |

### C.2.6:4 - Solution
`U.LanguageStateAnchoringMode` is a nominal characteristic that states the primary anchoring regime of the `U.Episteme` named by the current position claim: bodily enactment, trace, model state, document, operator loop, or an explicit mixed regime. If source anchoring and current publication-face anchoring differ, both shall be distinguished rather than collapsed.

#### C.2.6:4.0a - Kind and characteristic boundary

`U.LanguageStateAnchoringMode` is a dependent durable characteristic value under the declared `U.LanguageStateSpace` / `U.CharacteristicSpace` boundary, not a root U-kind. Its identity is the anchoring-mode basis slot and nominal family for episteme publication positions. This characteristic does not decide evidence, source-currentness, publication-face, carrier, Work, gate, or reliance claims; those claims retain their own definitions and tests.

#### C.2.6:4.1 - Starter family
| Mode | Reading | Typical evidence anchor |
|---|---|---|
| `AM.EmbodiedFelt` | bodily or kinesthetic anchoring matters directly | embodiment note, felt trace, human witness |
| `AM.TraceAnchored` | traces, logs, telemetry traces, or observations anchor the episteme | trace references, measured events, observations |
| `AM.ModelLatent` | latent or internal model state is the key anchor | model-state refs, probe results, latent summaries |
| `AM.DocumentMediated` | document or description is the principal anchor | documents, cards, method-description text |
| `AM.OperatorLoop` | the episteme is directly tied to operator intervention or console control | operator witness, console event, policy hook |
| `AM.Mixed` | more than one anchoring mode matters substantively | explicit component list and why the mix matters |

#### C.2.6:4.2 - Contribution boundary

`U.LanguageStateAnchoringMode` is an anchoring-mode characteristic for one `U.Episteme` position claim. It is not a representation factor bundle, closure state, truth status, evidence relation, source-currentness relation, Work claim, gate claim, or reliance permission by itself. Model-latent, operator-loop, embodied, trace, and document-mediated cases name where the episteme is anchored for the current claim. A publication-face, carrier, source-currentness, bridge-loss, Work, evidence, or gate claim needs its applicable definition or test; anchoring mode alone does not decide it.

If embodiment matters, it shall be declared here or immediately beside this characteristic rather than being hidden inside representation talk.

#### C.2.6:4.3 - Mixed-mode rule
`AM.Mixed` is admissible only when the component modes are named explicitly. "Mixed" shall not stand in for an undetermined anchoring mode.

#### C.2.6:4.4 - Bridge implications
An anchoring shift can matter when a receiving use needs a semantic relation between local senses from different semantic contexts. A shift from `AM.EmbodiedFelt` or `AM.ModelLatent` source anchoring to `AM.DocumentMediated` publication-face anchoring may provide evidence about an F.9 Bridge or bounded-use claim. Use F.9 to state and test the Bridge and the separate bounded-use claim, with its evidence and loss account. Use F.9.1 only for a separate optional stance note about that claim.

### C.2.6:5 - Archetypal Grounding
**Tell.** A felt cue, a controller-side probe score, and a textual design note may all be early cues, but they are anchored differently.

**Show (System).** An alert episteme directly tied to operator intervention or console control has mode `AM.OperatorLoop`, even when displayed as text.

**Show (Episteme).** An episteme published from a model-probe cue grounded in latent state has mode `AM.ModelLatent` even when rendered into prose.

### C.2.6:6 - Bias-Annotation
The pattern prompts authors to declare anchoring when wording such as "the system wants" or "the note suggests" leaves the anchor unclear.

### C.2.6:7 - Conformance Checklist
- `CC-C.2.6-1` Anchoring mode **SHALL NOT** be inferred from publication phrasing alone when it matters for source use, reliance, or bridge interpretation.
- `CC-C.2.6-2` Embodiment-sensitive or operator-loop cases **SHOULD** declare the embodiment or operator anchor explicitly.
- `CC-C.2.6-3` `U.LanguageStateAnchoringMode` **MUST NOT** be collapsed into `U.LanguageStateRepresentationFactorBundle`.
- `CC-C.2.6-4` Mixed-mode declarations **SHALL** list their component modes explicitly.

### C.2.6:8 - Common Anti-Patterns and How to Avoid Them
- **Text-only illusion.** Treating every cue as document-mediated because it has been written down.
- **Representation capture.** Using symbolic/distributed labels to hide world-anchoring distinctions.
- **Embodiment mystification.** Treating bodily or operator-loop cues as beyond explicit publication.

### C.2.6:9 - Consequences
The benefit is cleaner reasoning about embodied, operator-facing, trace-based, and model-latent cues. The trade-off is more explicit declaration work and, for shifts involved in semantic Bridges, more explicit bridge loss notes.

### C.2.6:10 - Rationale
The declared language-state chart over `U.CharacteristicSpace` needs one explicit anchoring basis slot so that `A.16.0`, `A.16.1`, `B.4.1`, and `F.9.1` can refer to anchoring regime without redefining it.

### C.2.6:11 - SoTA-Echoing
The facet is motivated by embodied cognition, operator-facing interaction practice, active inference, and modern model-probing practice, all of which distinguish cue content from anchoring regime.

### C.2.6:12 - Relations
- Builds on: `A.18`, `C.2.2a`, `C.2.LS`.
- Coordinates with: `A.7`, `A.16.0`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, `C.2.7`, `F.9` for any Bridge and bounded-use claim, and `F.9.1` only for an optional stance note about that claim.
- Constrains: cue publication and bridge loss notes.
### C.2.6:13 - Worked Examples and Bridge-Loss Cases

#### C.2.6:13.1 - Embodied-to-document shift
A prose publication of an episteme grounded in a bodily felt cue may retain `AM.EmbodiedFelt` as source mode while using `AM.DocumentMediated` as publication-face mode. Such a shift may introduce bridge loss, which should be assessed when cross-context equivalence is claimed.

#### C.2.6:13.2 - Model-latent to operator-loop case
An episteme recording a latent probe score may first be `AM.ModelLatent`, then be published as an operator-facing alert with `AM.OperatorLoop` publication-face anchoring when the alert is directly tied to operator intervention or console control. A conforming account should keep both the model-side source mode and the operator-loop publication-face mode visible.

#### C.2.6:13.3 - Mixed-mode publication
An alert note may admissibly be `AM.Mixed` when it combines operator-loop anchoring, trace anchoring, and document mediation. The declaration must name each component mode explicitly.

### C.2.6:14 - Authoring and Review Guidance

#### C.2.6:14.1 - Author prompt
When declaring anchoring mode, ask:

- what is the primary anchor kind?
- does bodily or operator participation matter directly?
- is the key anchor trace-based, model-internal, or document-based?
- if multiple modes matter, which ones and why?

#### C.2.6:14.2 - Review prompt
An assurance reader should watch for the common mistake where prose formatting tricks authors into forgetting the original anchoring mode.

#### C.2.6:14.3 - Bridge note
If anchoring changes across publication or translation and the receiving use needs a semantic relation between local senses from different contexts, use F.9 for the Bridge, bounded-use claim, and its evidence and loss account. Use F.9.1 only when a separate stance note about that claim helps replace silent equivalence language with a bounded reading.

### C.2.6:15 - Extension and Migration Notes

#### C.2.6:15.1 - Local extension rule
Contexts may add local anchoring modes, but they should do so by extension of the starter family rather than by collapsing the family into a text-vs-world binary.

#### C.2.6:15.2 - Migration from metaphorical prose
When wording such as "the system wants", "the note suggests", or "the operator-facing publication says" leaves anchoring unclear, it should be repaired by naming the anchoring mode and any detector, enactor, or witness needed to explain it.

#### C.2.6:15.3 - Boundary reminder
`U.LanguageStateAnchoringMode` does not decide representation, articulation, closure, or trust by itself. It only names how the episteme is anchored.
### C.2.6:16 - Anchoring Publication Package Discipline

#### C.2.6:16.1 - Minimal anchoring package
A publishable `U.LanguageStateAnchoringMode` claim should normally identify:

- the primary anchor kind;
- any directly relevant embodiment, operator, trace, model, or document witness;
- the transformation chain if the current note is not at the original anchoring site;
- any secondary modes that remain load-bearing.

This is especially important when the final wording is prose, because prose often hides the anchoring regime.

#### C.2.6:16.2 - Source-versus-face rule
Distinguish the anchoring mode of the source cue from the anchoring mode of the current publication face. A bodily cue written into a document may still require `AM.EmbodiedFelt` as source mode and `AM.DocumentMediated` as publication face.

#### C.2.6:16.3 - Mixed-mode decomposition rule
`AM.Mixed` is admissible only when its component modes are named and the reason for the mixture is operationally real. The component modes must be determined before the mixed-mode declaration is used.

### C.2.6:17 - Anchoring Shift and Transport Discipline

#### C.2.6:17.1 - Shift declaration rule
When an episteme crosses from one anchoring mode to another, state whether the shift is merely publication-level or whether it changes what can be preserved, compared, or trusted. A move from operator-loop enactment to report prose, for example, often drops timing, bodily load, and enactment friction.

#### C.2.6:17.2 - Bridge-loss rule
If an anchoring shift raises a semantic-correspondence question between local senses from different contexts, use F.9 to state and test the Bridge and its bounded-use claim, with the loss account; add an F.9.1 stance note only when it helps explain that claim. `C.2.6` only requires the shift to be noticed and not misrepresented as lossless.

#### C.2.6:17.3 - Same-content illusion test
Two cues may be paraphrased into the same sentence while remaining differently anchored. If the anchoring regime differs, the cues are not automatically substitutable.

### C.2.6:18 - Review Matrix and Extension Tests

#### C.2.6:18.1 - Review matrix
An assurance reader should ask:

- what the original anchoring regime was;
- what the current publication regime is;
- whether the transformation chain is explicit;
- whether any bridge loss or stance note is missing;
- whether a declared mixed mode is genuinely decomposed.

#### C.2.6:18.2 - Local extension test
A new local anchoring mode is justified only when it answers a distinct anchoring question that the starter family cannot express without distortion.

#### C.2.6:18.3 - Cross-facet reminder
Anchoring mode often correlates with representation and articulation changes, but it does not define or test them. Reject prose that uses `AM.ModelLatent`, `AM.EmbodiedFelt`, or `AM.OperatorLoop` as shorthand for being vague, early, trustworthy, or closed.

### C.2.6:End

