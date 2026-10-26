## C.2.6 - `U.LanguageStateAnchoringMode` — How Is the Episteme Anchored?

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Language-state anchoring mode.

**Use this pattern when.** Use C.2.6 when how an episteme is anchored changes its interpretation, comparison or use. The mode can distinguish bodily enactment, traces, model state, document mediation, an operator loop or an explicit mixture. An ordinary description of the anchor is sufficient unless the receiving use needs a declared mode.

**What goes wrong if missed.** A prose note hides an embodied, trace-based, model-latent, or operator-loop cue; bridge-loss notes disappear; and the final publication face is mistaken for the original anchoring regime.

**What this buys.** A nominal Characteristic for comparing how epistemes are anchored, independently of their publication forms. Evidence and loss accounts can then address the actual anchoring relation.

### C.2.6:1 - Problem frame
Published position claims in the declared language-state chart over `U.CharacteristicSpace` differ not only by articulation and closure, but by how the `U.Episteme` named in that claim is anchored to bodies, traces, model states, documents, or operator loops.

### C.2.6:2 - Problem
When a comparison or use depends on anchoring, leaving it implicit can hide the difference between a bodily cue, a trace and a description of either. A representation label alone may leave that difference unresolved.

### C.2.6:3 - Forces
| Force | Tension |
|---|---|
| **Embodiment vs abstraction** | Preserve embodied and operator-facing cases while making their anchoring explicit. |
| **Small core vs real diversity** | Keep the core compact while allowing multiple admissible anchoring regimes. |
| **Comparability vs oversimplification** | Compare anchoring regimes while retaining distinctions that a text-vs-nontext split hides. |

### C.2.6:4 - Solution
`U.LanguageStateAnchoringMode` is a nominal characteristic that states the primary anchoring regime of the `U.Episteme` named by the current position claim: bodily enactment, trace, model state, document, operator loop, or an explicit mixed regime. When a receiving episteme has a different anchoring regime from its source, distinguish both. A change of publication form alone does not establish that difference.

#### C.2.6:4.0a - Kind and characteristic boundary

`U.LanguageStateAnchoringMode` is the Characteristic of an episteme assessed in the declared language-state chart. Its readings belong to a nominal Scale; the chart slot binds that Characteristic to its Scale under A.18/A.19. The mode identifies how the episteme is anchored. Any evidence, currentness or action claim still needs the relation and conditions that establish it.

#### C.2.6:4.1 - Starter family
| Mode | Reading | Possible witness of anchoring |
|---|---|---|
| `AM.EmbodiedFelt` | bodily or kinesthetic anchoring matters directly | embodiment note, felt trace, human witness |
| `AM.TraceAnchored` | traces or observations anchor the episteme | trace references, measured events, observations |
| `AM.ModelLatent` | latent or internal model state is the key anchor | model-state refs, probe results, latent summaries |
| `AM.DocumentMediated` | document or description is the principal anchor | documents, cards, method-description text |
| `AM.OperatorLoop` | the episteme is directly tied to operator intervention or console control | operator witness, console event, policy hook |
| `AM.Mixed` | more than one anchoring mode matters substantively | explicit component list and why the mix matters |

#### C.2.6:4.2 - Contribution boundary

The mode characterizes anchoring of the episteme named in the position claim. Representation factors describe how information is represented; closure describes fixity. Neither follows from an anchoring mode. Apply the rule for any further claim, such as an evidence relation or permission to act.

If embodiment matters, it shall be declared here or immediately beside this characteristic rather than being hidden inside representation talk.

#### C.2.6:4.3 - Mixed-mode rule
`AM.Mixed` is admissible only when the component modes are named explicitly. "Mixed" shall not stand in for an undetermined anchoring mode.

#### C.2.6:4.4 - Bridge implications
An anchoring shift can matter when a receiving use needs a semantic relation between local senses from different semantic contexts. A receiving episteme anchored in a document may depend on a source anchored in bodily experience or model state. That difference may affect the evidence or loss account for the semantic correspondence. Use F.9 to state and test the Bridge and the separate bounded-use claim, with its evidence and loss account. Use F.9.1 only for a separate optional stance note about that claim.

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
The mode makes differences in anchoring available to comparison and use. Establishing a mode requires enough information about its anchor; a shift involved in a semantic Bridge also needs the applicable loss account.

### C.2.6:10 - Rationale
The declared language-state chart over `U.CharacteristicSpace` needs one explicit anchoring basis slot so that `A.16.0`, `A.16.1`, `B.4.1`, and `F.9.1` can refer to anchoring regime without redefining it.

### C.2.6:11 - SoTA-Echoing
The facet is motivated by embodied cognition, operator-facing interaction practice, active inference, and modern model-probing practice, all of which distinguish cue content from anchoring regime.

### C.2.6:12 - Relations
- Builds on: `A.18`, `A.19`, `C.2.P`, `C.2.2a`, `C.2.LS`.
- Coordinates with: `A.7`, `A.16.0`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, `C.2.7`, `F.9` for any Bridge and bounded-use claim, and `F.9.1` only for an optional stance note about that claim.
- Constrains: cue publication and bridge loss notes.
### C.2.6:13 - Worked Examples and Bridge-Loss Cases

#### C.2.6:13.1 - Embodied-to-document shift
An operator first notices vibration through bodily sensation. That cue has `AM.EmbodiedFelt` anchoring even after it is described in prose. A later analyst who has only the written account may form a receiving episteme anchored in that document, with mode `AM.DocumentMediated`. Distinguish the source cue from the analyst's episteme and assess any loss that matters to the intended comparison or use. Apply F.9 when the use claims a semantic correspondence between local senses from different semantic contexts.

#### C.2.6:13.2 - Model-latent to operator-loop case
An episteme recording a latent probe score is anchored in model state (`AM.ModelLatent`). A receiving alert episteme can have `AM.OperatorLoop` anchoring when it is directly tied to operator intervention or console control. Keep the model-side source and the operator-loop anchor visible. Merely displaying the score on a console does not establish the operator-loop relation.

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
Check whether a mode attributed to a prose publication describes its actual anchor or merely its format.

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
- the source and transformations that affect the current anchoring claim;
- any secondary modes that remain load-bearing.

For a single unchanged anchor, its identification and any witness needed by the use can suffice.

#### C.2.6:16.2 - Source-versus-face rule
Distinguish the source episteme, any receiving episteme and their publication forms under C.2.P. Assign anchoring modes to the epistemes. A prose form by itself establishes neither `AM.DocumentMediated` nor a shift from the source mode.

#### C.2.6:16.3 - Mixed-mode decomposition rule
`AM.Mixed` is admissible only when its component modes are named and the reason for the mixture is operationally real. The component modes must be determined before the mixed-mode declaration is used.

### C.2.6:17 - Anchoring Shift and Transport Discipline

#### C.2.6:17.1 - Shift declaration rule
When the anchor changes, state the consequences for the intended comparison or use. In a report derived from an operator-loop cue, timing or bodily load may be omitted; identify the actual omission and its effect. If only the publication form changes, do not infer an anchoring shift or loss from that change alone.

#### C.2.6:17.2 - Bridge-loss rule
If an anchoring shift raises a semantic-correspondence question between local senses from different contexts, use F.9 to state and test the Bridge and its bounded-use claim, with the loss account; add an F.9.1 stance note only when it helps explain that claim. `C.2.6` only requires the shift to be noticed and not misrepresented as lossless.

#### C.2.6:17.3 - Same-content illusion test
Two cues may be paraphrased into the same sentence while remaining differently anchored. If the anchoring regime differs, the cues are not automatically substitutable.

### C.2.6:18 - Review Matrix and Extension Tests

#### C.2.6:18.1 - Review matrix
An assurance reader should ask:

- what the original anchoring regime was;
- how the current episteme is anchored;
- which source transformations affect that anchoring;
- whether a semantic-correspondence claim needs an F.9 loss account and whether an optional stance note adds a useful qualification;
- whether a declared mixed mode names its actual components.

#### C.2.6:18.2 - Local extension test
A new local anchoring mode is justified only when it answers a distinct anchoring question that the starter family cannot express without distortion.

#### C.2.6:18.3 - Cross-facet reminder
Anchoring mode often correlates with representation and articulation changes, but it does not define or test them. Reject prose that uses `AM.ModelLatent`, `AM.EmbodiedFelt`, or `AM.OperatorLoop` as shorthand for being vague, early, trustworthy, or closed.

### C.2.6:End
