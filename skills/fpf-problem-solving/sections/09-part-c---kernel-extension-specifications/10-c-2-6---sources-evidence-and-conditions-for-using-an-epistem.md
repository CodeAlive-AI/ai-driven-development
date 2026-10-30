## C.2.6 - Sources, Evidence and Conditions for Using an Episteme

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Sources and conditions of episteme use.

**Use this pattern when.** A claim or cue is being reused, translated or published elsewhere, and the receiving work needs to know what produced it, what supports it, or how someone can use it. An analyst reading an operator's vibration report, for example, may need the operator's observation and its circumstances before treating the report as evidence about a machine.

**Sufficient result and non-use.** State the relations and conditions that can change the intended interpretation, check or action. Use an already sufficient description directly. A new account, classification or chart is unnecessary when the receiving work can recover those facts and conditions from the available text.

**What goes wrong if missed.** A report can preserve a sentence while losing access to the observation, model state or interaction needed to use it. An unspecified claim that it is "anchored" leaves the reader to infer whether this means derivation, evidence or an actual condition of action.

**What this buys.** The recipient can identify which conclusions remain supported, which action conditions still hold and what must be recovered before the intended use can continue.

### C.2.6:1 - Problem frame
A `U.Episteme` may be produced from observations, refer to a model state, report another document's assertions and participate in an operator's decision. These facts answer different questions about the same episteme. Their importance changes with the receiving use.

### C.2.6:2 - Problem
A common label can conceal the particular relation on which a use depends. Knowing that a reading was computed from a trace establishes its provenance; using that trace as evidence for a claim also requires the relevant observation and target claim to match. Publishing the reading in a document supplies access to its expression. A separate interaction may make the reading available for an operator's next check.

### C.2.6:3 - Forces
| Force | Tension |
|---|---|
| **Embodiment vs abstraction** | Preserve bodily observations and operator participation while making their contribution explicit. |
| **Compact description vs relevant detail** | Keep only the relations needed by the receiving use, with enough detail to establish them. |
| **Comparability vs oversimplification** | Compare a shared aspect without treating different relations as values of one unspecified Scale. |

### C.2.6:4 - Solution
Recover the claims about sources, evidence, access and action conditions that the receiving work actually needs. State each with its participants and grounds. Then determine what publication, translation or a changed use preserves, changes or leaves unknown. The result is an ordinary account of those facts and conditions; C.2.1 governs the account and E.24.PUB governs its publication.

#### C.2.6:4.0a - Relations, readings and a shared account

A source relation, an evidence-use claim and an operator's use of an alert can hold together. Each keeps its own predicate and grounds. For empirical grounding, apply C.2.1:4.3 to the designated claim coverage and observation or test; apply A.2.4 to the relation between the evidence episteme and its target claim, and A.10 when provenance or bounded reliance must be established. Use C.2.P to distinguish the epistemic objects. When basedness is hidden by an umbrella word, apply A.6.6:4.0; A.6.P supplies the wider route to an unclear direct relation. Return their exact assertion or unresolved condition to the receiving use. An ordinary adequate statement can supply this account without a new formal record.

An account collecting several such statements is not one Coordinate. A language-state profile may cite it beside its Characteristic readings. A local summary can occupy a chart slot only when its single measured aspect, subject/input signature and Scale are defined under A.18/A.19, as :15.1 explains. The account's component relations remain recoverable.

#### C.2.6:4.1 - Distinctions that can change use
The following are recurring examples of questions to resolve, not a closed taxonomy or alternatives on one Scale. Select a question because its answer can change the intended use.

| Working question | Claim to recover | Possible basis |
|---|---|---|
| What did someone experience or do? | The person's bodily sensation, observation or enactment, and what the resulting cue reports. | Witness account, observation circumstances or an observed performance. |
| Where did this reading come from? | The source trace and the operation that produced the reading. If evidence is needed, separately establish what observation supports which target claim. | Trace references, measured events and the calculation or other derivation; evidence qualification for the target claim. |
| What does this model-derived account report? | The identified model state, probe or decoding operation and its output; the grounds for the interpretation made from that output. | Model-state references, probe conditions and results, and interpretation evidence. |
| What can the recipient recover from the document? | The particular assertions available to that recipient, and any source or evidence claim on which their use depends. | The identified document edition, accessible content and relevant cited sources. |
| How is the information used in an operator's work? | Who acknowledges, interprets or acts on it, and which actual interaction or rule connects that act to a check or control action. | Operator observation, console event or an applicable action rule, with the implementation or performance needed for the claimed connection. |

##### C.2.6:4.1.1 - Recover the relations needed for one receiving use

1. Identify the episteme edition, the claim or cue being used and the receiving judgement or action. Keep a source episteme and an analyst's resulting account distinct under C.2.P when their contents or concerns differ.
2. Ask which facts the receiving work needs: for example, the source of a reading when diagnosing a calculation, the relevant observation when checking a pressure claim, or an acknowledgement condition when arranging an operator's next check. Obtain only the relations that can change that work. The table in :4.1 helps locate common questions; the subject of the work determines the answer and can require another relation.
3. State each needed relation with its actual participants, applicable scope and grounds. When a trace is used as evidence, establish its relation to the target claim as well as its provenance. When an action is claimed, establish the actual interaction or governing condition and the relevant performer. Preserve a consequential unknown instead of filling it from a neighbouring fact.
4. Compare the source situation with the receiving situation. Identify what remains accessible and applicable, what changed and what those changes permit or prevent. Retain supported claims and return to a missing observation, interpretation or action condition where the proposed use depends on it.

For example, an alert can be computed from a measurement, delivered in a report and acknowledged by an operator. Replacing the report file while preserving the accessible assertions can leave the derivation and evidence unchanged. Discovering that the measurement concerned another pump changes its evidential use for the pressure claim. Disabling an acknowledgement channel changes the interaction available to the operator. These changes call for different continuations, so the account must keep their predicates distinct.

#### C.2.6:4.2 - Contribution boundary

This pattern organizes the source and use questions; their direct patterns establish the individual claims. Representation factors describe how information is represented; closure describes fixity of the current candidate space. Assess those Characteristics under their own definitions. A required bodily observation or operator participation is stated here or in the cited account, with its actual contribution to the receiving work.

#### C.2.6:4.3 - Several relations and incomplete information
When several relations matter together, name each and explain its contribution. Distinguish their established conjunction from alternatives left unresolved by the available evidence. For example, "the source was either a sensor reading or a simulation" leaves provenance uncertain; it does not establish that both sources contributed. A generic "mixed" label supplies neither the missing facts nor their conjunction.

#### C.2.6:4.4 - Bridge implications
A receiving use may need a semantic relation between local senses from different semantic contexts. The recipient's access to a report can differ from the source practitioner's bodily observation or access to model state. That difference may affect the evidence or loss account for the proposed semantic correspondence. Use F.9 to state and test the Bridge and the separate bounded-use claim, with its evidence and loss account. Use F.9.1 only for a separate optional stance note about that claim.

### C.2.6:5 - Archetypal Grounding
**Tell.** A felt cue, a controller-side probe score and a textual design note can all help begin an inquiry. Recover the observation, computation or reported assertions that the intended inquiry needs.

**Show (System).** A console alert is used in an acknowledgement-and-check procedure. Its use account identifies the operator's acknowledgement and how the next diagnostic check is selected. A text display can carry the alert while these action conditions remain essential.

**Show (Episteme).** A model probe produces a score from an identified internal state. A later prose account reports that result. Recovering the state and probe establishes the derivation; the account's interpretation needs its own stated grounds.

### C.2.6:6 - Bias-Annotation
The questions favour explicit source and use claims when they affect a decision. Statements about bodily experience need an obtainable witness or other appropriate basis for the claim being made; describing that experience does not require reducing it to a document property.

### C.2.6:7 - Conformance Checklist
- `CC-C.2.6-1` Source, evidence or action relations **SHALL NOT** be inferred from publication phrasing alone when they matter for source use, reliance or Bridge interpretation.
- `CC-C.2.6-2` Embodiment-sensitive or operator-loop cases **SHOULD** declare the relevant observation, enactment or operator interaction explicitly.
- `CC-C.2.6-3` Source and use claims **MUST NOT** be collapsed into the representation-factor readings governed by C.2.7.
- `CC-C.2.6-4` A declaration that several relations jointly matter **SHALL** identify those relations and their contribution explicitly.

### C.2.6:8 - Common Anti-Patterns and How to Avoid Them
- **Text-only illusion.** Treating a written report as a sufficient account of the observation or interaction that its use needs. Recover the relevant claim and its basis.
- **Representation capture.** Using symbolic/distributed labels to conceal a source or use condition. State that condition separately.
- **Embodiment mystification.** Treating bodily or operator-loop cues as beyond explicit publication. Publish the relevant observation or action account and the limits of its recovery.
- **Common-word classification.** Grouping provenance, evidence and interaction as alternative values because each has been called "anchoring". Establish the actual predicate before choosing a Scale.

### C.2.6:9 - Consequences
The recipient can inspect the facts that make the proposed use possible and return to the particular missing basis. This requires enough source and interaction detail for that use. An account can cite existing adequate descriptions; repeating them or filling every row of :4.1 adds no necessary assurance.

### C.2.6:10 - Rationale
`A.16.0`, `A.16.1`, `B.4.1` and an applicable F.9 use need to preserve different facts when a cue is expressed or used elsewhere. An observation may remain the source after it is reported in text, while the recipient has access only to that report. An operator's interaction can change independently of either. Direct statements preserve these distinctions and explain which continuation changes. A common nominal summary is useful only when a specified comparison really consumes it and its criterion consistently measures one aspect (:15.1).

### C.2.6:11 - SoTA-Echoing
The following sources contribute particular distinctions and alternatives for the use questions in :4.1.1. They do not establish one universal classification of the listed relations.

| Source and status | Contribution and boundary |
|---|---|
| [Hutchins, *How a Cockpit Remembers Its Speeds* (1995)](https://pages.ucsd.edu/~c8johnson/COGS102B/Hutchins95.pdf), historical account, pp.13–16 | Coordinated instrument settings, spoken reports and pilot actions show why the actual working connections matter. This supports recovery of operator interaction and its conditions. |
| [W3C PROV-DM (2013)](https://www.w3.org/TR/prov-dm/#term-Derivation), §§2.2.1.2 and 5.2.1, stable provenance comparator | Derivation exposes the entities, activity, usage and generation involved. Such explicit relations preserve the dependency needed to inspect where a result came from. |
| [Fraser-Taliente et al., *Natural Language Autoencoders* (2026)](https://transformer-circuits.pub/2026/nla/index.html), Method and Discussion | Activation verbalization distinguishes model-state input from its textual explanation. Reported confabulations require a separate basis for the explanation's claims; identification of the input establishes the source connection only. |
| [Denamganaï (October 2026)](https://arxiv.org/html/2610.18727v1), §§6.2–7, exploratory preprint | In limited transcript-level tests, activation identification and true-account discrimination differ. This reinforces the boundary between recovering a source connection and warranting an interpretation; processing-level claims remain untested. |

### C.2.6:12 - Relations
- Builds on: `C.2.1`, `C.2.P`, `A.2.4` and `A.10` for the relevant direct claims; `A.6.6` and `A.6.P` when the relation needs recovery; `A.18/A.19` for an independently defined local Characteristic.
- Coordinates with: `A.7`, `A.16.0`, `A.16`, `A.16.1`, `B.4.1`, `B.5.2.0`, `C.2.2a`, `C.2.LS`, `C.2.7`, `F.9` for any Bridge and bounded-use claim, and `F.9.1` only for an optional stance note about that claim.
- Constrains: source and use accounts in cue publication and Bridge loss notes.
### C.2.6:13 - Worked Examples and Bridge-Loss Cases

#### C.2.6:13.1 - Bodily observation and its written report
An operator first notices vibration through bodily sensation. A prose report describes that observation. A later analyst who has only the report can recover its assertions but cannot repeat the operator's sensation from the text. Distinguish the source cue from the analyst's episteme; identify which observation circumstances the intended comparison or check needs and whether the report preserves them. Apply F.9 when the use claims a semantic correspondence between local senses from different semantic contexts.

#### C.2.6:13.2 - Model-derived score used by an operator
An episteme records a probe score obtained from a model state. A receiving alert reports that score in a procedure that requires operator acknowledgement before selection of the next diagnostic check. Keep both the source/probe derivation and the acknowledgement condition visible. A console display establishes the latter connection only when the required interaction is actually provided; the displayed score alone does not show that.

#### C.2.6:13.3 - Provenance, evidence and interaction in one alert
An alert E asserts that Pump P's pressure is below 90 kPa. The software produced E from trace T. An operator has acknowledged E and selected a diagnostic check under the stated procedure. Inspection then shows that T was a measurement of Pump Q.

The derivation from T remains established. T supplies no measurement of P for the claimed pressure: return to an appropriate observation of P before using that measurement as support for this claim. The acknowledgement and selected check remain facts about the operator's work. Whether to continue, suspend or change that check follows its actual rule and purpose; neither derivation nor acknowledgement settles the truth of the pressure claim. A report can publish all these statements together with their different grounds.

### C.2.6:14 - Authoring and Review Guidance

#### C.2.6:14.1 - Author prompt
Start from the receiving judgement or action. Identify the particular claim, source or observation it needs and the conditions of access or interaction that can change its use. State several relations separately when each contributes; leave a consequential missing fact unresolved.

#### C.2.6:14.2 - Review prompt
Check that each relation attributed to a published account has the needed participants and grounds. Then change one condition in the case and determine which claim or continuation changes. If the wording cannot distinguish the changed relation from the retained ones, recover the objects through C.2.P and the relation through A.6.6 or A.6.P as applicable.

#### C.2.6:14.3 - Bridge note
If a changed source, access or interaction raises a semantic-correspondence question between local senses from different contexts, use F.9 for the Bridge, bounded-use claim and its evidence and loss account. Use F.9.1 only when a separate stance note helps explain that claim.

### C.2.6:15 - Local Summaries and Precision Restoration

#### C.2.6:15.1 - Local summary rule
A repeated comparison may benefit from a nominal Characteristic summarizing one aspect of the recovered facts. Define that aspect and its subject/input signature, the Scale, the rule mapping the relevant facts to a value, and the receiving comparison that uses it under A.18/A.19. Account for jointly satisfied conditions and keep incomplete information separate from a value. A new relation is not automatically a new value of an existing Scale.

For example, a team comparing access to a designated primary check can define one nominal Characteristic for the tuple (claim, designated check, recipient, time): the recipient can perform that check at that time, or cannot. Establish the capability and access required by the check before assigning either value; otherwise leave the reading unknown. The value helps choose between performing the check and arranging the missing access. This local comparison concerns availability of that check; it does not classify the claim's provenance or evidence quality.

Declare such a Characteristic as its own chart slot. A changed aspect or Scale changes the chart meaning under A.19:5.1.2; preserve or establish an explicit mapping when an old position must be compared with it. C.3.2 governs any separate classification using these readings.

#### C.2.6:15.2 - Recover a relation hidden by metaphor
When wording such as "the system wants" or "the note suggests" leaves the intended action or claim unclear, identify what the system does, what the note asserts, or who makes the interpretation. Recover the relevant detector, performer or witness through the direct subject pattern. An ordinary understood metaphor needs no expanded record.

#### C.2.6:15.3 - Boundary reminder
Source and use relations answer their stated questions. Representation, articulation, closure and trust retain their own definitions and tests.
### C.2.6:16 - Publishing the Required Account

#### C.2.6:16.1 - Minimal account
Identify the episteme and the receiving use, then state or cite only the source, evidence, access or action conditions that use needs. Make their participants, grounds and any consequential uncertainty recoverable. Include a source transformation when it changes the claim or its use. For one unchanged relation, its adequate existing description can suffice.

#### C.2.6:16.2 - Source-versus-form rule
Distinguish the source episteme, any receiving episteme and their publication forms under C.2.P. State provenance, evidence and use claims about the actual participants. A prose form alone establishes neither a document as the original source nor a change in the observation or interaction being reported.

#### C.2.6:16.3 - Joint-use account
When several relations jointly enable the use, identify their separate contributions and which facts establish each. Retain the known relations while recovering a missing one; uncertainty about one does not erase the others or establish a mixture.

### C.2.6:17 - Changed Sources, Access and Use

#### C.2.6:17.1 - State the change and its consequence
When a source, access condition or interaction changes, state the consequences for the intended comparison or action. A report derived from an operator's cue may omit timing or bodily load; identify the actual omission and its effect. A change of publication form alone does not establish such an omission.

#### C.2.6:17.2 - Bridge-loss rule
If that change raises a semantic-correspondence question between local senses from different contexts, use F.9 to state and test the Bridge and its bounded-use claim, with the loss account; add an F.9.1 stance note only when it helps explain that claim. C.2.6 requires the relevant change to be noticed and represented accurately.

#### C.2.6:17.3 - Same-content substitution test
Two cues may be paraphrased into the same sentence while being produced by different observations or available under different conditions. Establish the relations required by the receiving use before substituting one for the other.

### C.2.6:18 - Review and Extension Tests

#### C.2.6:18.1 - Review matrix
For the stated use, check the original source and relevant transformations, what the recipient can recover or do now, and the grounds for the resulting claims. Include the separate F.9 question when a semantic correspondence is claimed. A joint-use account identifies each relation that matters.

#### C.2.6:18.2 - Local extension test
Add another direct relation when the receiving work needs it. Introduce a nominal summary only when :15.1's aspect, mapping and comparison are actually supplied; a common word for several dependencies is insufficient.

#### C.2.6:18.3 - Cross-facet reminder
A changed source or interaction can accompany a change in representation or articulation. Test those changes separately. A model-derived score, a bodily observation or an operator's acknowledgement supplies no reading of vagueness, closure or trust without the corresponding criterion and grounds.

### C.2.6:End
