## B.5.2.0 - `U.AbductivePrompt`

> **Type:** Definitional (D)
> **Status:** Draft
> **Normativity:** Normative unless marked informative

**Plain-name.** Abductive prompt.


### B.5.2.0:1 - Problem frame
`B.5.2` needs an entry form that can accept lawful language-state trajectories after cue preservation and routing, without pretending that anomaly is the only admissible starting form.

### B.5.2.0:2 - Problem
If anomaly is the only admissible input, pre-anomaly opportunity cues and route-derived prompt forms are excluded or misrepresented. If anything can enter, abduction loses its typed starting discipline.

### B.5.2.0:3 - Forces
| Force | Tension |
|---|---|
| **Breadth vs discipline** | Admit more than anomaly, but keep a bounded family of lawful prompt species. |
| **Reuse vs type inflation** | Introduce a clean entry form without exploding the number of heavy publication kinds. |
| **Prompt vs hypothesis** | Keep the initiating prompt distinct from the later abductive outcome. |

### B.5.2.0:4 - Solution
`U.AbductivePrompt` is a narrow supertype for the prompt forms that may admissibly seed `B.5.2` after admissible cue preservation and governing-pattern selection under `A.16`, `A.16.1`, and `B.4.1`. `A.16.0` is used only when the cue-to-prompt history itself has governance value as an explicit trajectory account. When rendered, a prompt uses ordinary MVPK faces; prompt status is a property of the publication form, not a rival face ontology.

#### B.5.2.0:4.1 - Starter canonical species and conditional extension species
- starter canonical species:
  - `AnomalyStatement`
  - `ProblemCuePrompt`
  - `OpportunityCuePrompt`
  - `ProbeCuePrompt`
- conditional extension species:
  - `TaskFamilySpecializationPrompt`
  - `AdaptationProbePrompt`
  - `NonHumanUtilityPrompt`
  - `SubstrateDiversificationPrompt`

##### B.5.2.0:4.1.1 - Specialization-sensitive prompt species
These extension species are admissible only when cue provenance or trajectory account already carries the bounded-specialization support requirement by value; they are not the starter canonical entry set for ordinary abduction.

`TaskFamilySpecializationPrompt` asks what narrower higher-fit specialist lane should be acquired for the declared task family, where that lane may later resolve into one specialist method, portfolio, or competence bundle. `AdaptationProbePrompt` asks which bounded probe would most cheaply reveal whether threshold-reaching specialization is actually attainable. `NonHumanUtilityPrompt` asks whether a low-human-overlap approach or corridor may still satisfy the declared utility target better than the current familiar repertoire. `SubstrateDiversificationPrompt` asks whether the current substrate is too narrow and a broader or different substrate should be tested before later commitment.

#### B.5.2.0:4.2 - Core shape
A conforming abductive prompt may publish:

- `promptSpecies`
- `motivatingCueRef?`
- `openQuestion`
- `contrastSet?`
- `scope?`
- `witnessRefs?`
- `routeProvenance?`
- `GammaTime?`

A prompt is not yet a hypothesis. Prompt legality usually presupposes articulation high enough to publish a stable open question and closure low enough that rival answers remain live; those articulation and closure thresholds remain governed by `C.2.4` and `C.2.5`, typically reached through cue or route provenance from `A.16.1` and `B.4.1`. It is the initiating publication form that licenses entry into the abductive loop.

#### B.5.2.0:4.3 - Boundary rule
`U.AbductivePrompt` is an entry form, not an excuse to let arbitrary prose count as abductive input. Only declared prompt species may enter `B.5.2` through this form.

### B.5.2.0:5 - Archetypal Grounding
**Tell.** An anomaly is one prompt species, not the only one.

**Show (System).** A control cue may begin probe-design abduction even before it is framed as anomaly.

**Show (Episteme).** A promising mismatch can begin an opportunity-style abductive prompt rather than only a problem statement.

### B.5.2.0:6 - Bias-Annotation
The pattern broadens the entry form to abduction, but still keeps it typed and auditable.

### B.5.2.0:7 - Conformance Checklist
- `CC-B.5.2.0-1` Every `U.AbductivePrompt` **SHALL** declare its prompt species.
- `CC-B.5.2.0-2` A prompt **SHALL NOT** be confused with a finished hypothesis.
- `CC-B.5.2.0-3` Cue-derived prompts **SHOULD** preserve route provenance.
- `CC-B.5.2.0-4` Prompt publication **SHALL** include the open question that makes abduction appropriate.
- `CC-B.5.2.0-5` A publication that already fixes the answer or suppresses plausible rivals **SHALL NOT** remain in prompt status.
- `CC-B.5.2.0-6` When a specialization-sensitive prompt species is used, the prompt package **SHALL** make explicit the declared task family or utility target, the threshold or success condition being probed, the current budget window, and the route or cue provenance that made the prompt lawful.

### B.5.2.0:8 - Common Anti-Patterns and How to Avoid Them
- **Prompt equals hypothesis.** Keep the prompt distinct from the abductive output.
- **Anything can begin abduction.** No: only declared prompt species can.
- **Route amnesia.** A cue-derived prompt loses the early route provenance that explains why it entered here.

### B.5.2.0:9 - Consequences
The benefit is cleaner, less brittle abduction-entry terms. The trade-off is one additional explicit prompt supertype and one more declared publication form.

### B.5.2.0:10 - Rationale
This keeps admissible cue preservation and trajectory publication able to dock into `B.5.2` through a typed prompt form without anomaly inflation and without making `A.16.0` mandatory.

### B.5.2.0:11 - SoTA-Echoing
The pattern reflects real abductive practice, where opportunities, probe prompts, and stabilized cues often begin the loop before a full anomaly formulation exists.

### B.5.2.0:12 - Relations
- Builds on: `C.2.2a`, `A.16`, `A.16.1`, `B.4.1`, `C.2.LS`, `C.2.4`, `C.2.5`.
- Coordinates with: `A.16.0`, `A.16.2`, `C.2.6`, `C.2.7`, `B.5.2`, `A.6.P`, `C.16.Q`, `A.6.A`, `F.9.1`.
- Constrains: lawful prompt entry into abduction.
### B.5.2.0:13 - Worked Prompt Species

#### B.5.2.0:13.1 - Anomaly statement as canonical prompt
An anomaly statement remains a canonical prompt species, especially when the contrast and failure condition are already explicit.

#### B.5.2.0:13.2 - Opportunity-style prompt
A cue may admissibly become an opportunity prompt when the open question concerns a potentially valuable line of probe or intervention rather than a failure description.

#### B.5.2.0:13.3 - Probe-style prompt
A routed cue may become a probe prompt when what matters is not yet explanation but the explicit need to test, contrast, instrument, or perturb.

#### B.5.2.0:13.4 - Specialization-sensitive prompt set
A cue set may admissibly become a `TaskFamilySpecializationPrompt`, `AdaptationProbePrompt`, `NonHumanUtilityPrompt`, or `SubstrateDiversificationPrompt` when the live question is not yet a selector decision but a bounded entry into specialist acquisition, adaptation probing, nonhuman-utility discovery, or substrate widening. The point is to preserve the task family, budget window, rival candidate paths, and corridor-entry evidence requirement long enough for later comparison rather than smuggling a commitment into prompt form.

### B.5.2.0:14 - Prompt package discipline

A prompt becomes reusable in `B.5.2` only when its initiating question is explicit enough to remain stable across later hypothesis work.

#### B.5.2.0:14.1 - Minimal prompt package

A robust abductive prompt should make explicit:

- the **prompt species**,
- the **open question**,
- the **motivating cue or route provenance**,
- the **contrast set**, if one is already visible,
- the **scope** in which the question is being asked,
- and the **witnesses or cue grounds** that justify beginning abduction.

This package lets later conjectures be tested against the same question rather than against a later paraphrase.

For specialization-sensitive prompt species, the package should also make explicit the declared task family or utility target, the threshold or success condition being probed, the current budget window, the prior route provenance, and the rival prompt shapes still in play.

#### B.5.2.0:14.2 - Prompts are questions, not claims

A prompt may cue one explanation, but it remains a question-bearing entry form. If the text already asserts the answer, it has moved past prompt status and should be treated under `B.5.2` or another governing pattern that carries the asserted answer.

#### B.5.2.0:14.3 - Prompt provenance remains load-bearing

Route provenance, cue provenance, and witness provenance are part of prompt legality, not optional history.

#### B.5.2.0:14.4 - Review prompt against silent promotion
A reviewer should watch for the common mistake where authors silently upgrade a prompt into a hypothesis merely because the prose sounds explanatory. If the text already leans on one preferred answer as settled, either rewrite it back into a real question or explicitly apply the governing pattern that carries the asserted answer.

### B.5.2.0:15 - Species boundary reminders

Use anomaly species when the key form is an explicit failure, contradiction, or surprising departure from what the current model expected. Use opportunity species when the pressure comes from a promising line of development or advantageous contrast. Use probe species when what matters is the need to instrument, contrast, perturb, or ask a question that could discriminate among several future explanations.

Use `TaskFamilySpecializationPrompt` when the live question is which narrower higher-fit specialist lane should be acquired for one declared task family. Use `AdaptationProbePrompt` when the next honest move is a bounded probe that tests whether threshold-reaching specialization is attainable under the current budget. Use `NonHumanUtilityPrompt` when the prompt must keep a low-human-overlap approach or corridor admissible because it may satisfy the declared utility target better than the current familiar repertoire. Use `SubstrateDiversificationPrompt` when the current question is whether the present substrate is too narrow and a broader or different substrate should be tested before later commitment.

Cue-derived prompt entries should stay prompt-headed species rather than projection-headed aliases. The load-bearing question is the prompt kind itself, not one package-local naming trick.

### B.5.2.0:16 - Handoff, deferral, and invalid drift

A prompt should enter `B.5.2` only when the question is explicit enough that rival hypotheses can now be compared against it. If the question is still underspecified, the lawful continuation is further stabilization or routing, not premature abduction.

A routed cue may be close to prompt form but still missing one decisive contrast or witness. In such cases the prompt may be deferred explicitly rather than forced into `U.AbductivePrompt` before its initiating question is stable.

A bare intuition, slogan, or rhetorical question with no prompt species and no cue provenance is not yet a lawful `U.AbductivePrompt`.

A common failure mode is drift from cue -> prompt -> hypothesis without anyone naming the boundary crossings. `B.5.2.0` blocks that drift by keeping the prompt package distinct from both the earlier cue pack and the later prime hypothesis.

### B.5.2.0:17 - Scope, rival-set, and comparative-validity discipline

A prompt should declare the scope in which its question is being asked: the domain fragment, operational horizon, or inquiry-bounded scope cut that makes the question answerable. If scope remains unbounded, rival hypotheses will later become incomparable because they are answering different questions.

A prompt need not list full hypotheses yet, but it should make visible whether rival answer types are already imaginable. If no rival answer space is even latent, the publication may still be a cue or orientation note rather than a true abductive prompt.

A prompt may be narrowed to become more discriminating, but the narrowing must not silently smuggle in the answer it is supposedly asking about. Otherwise the prompt ceases to be an initiating question and becomes a disguised conclusion. If a prompt already excludes every serious rival except one preferred explanatory line, the publication may already be preloading a hypothesis. Review should then either rewrite the prompt back into a real question or explicitly apply the governing pattern that carries the asserted answer.

Prompts may be compared across contexts only when their species, scope, and provenance are explicit. A probe-shaped question and an opportunity-shaped question are not the same kind of abductive entry merely because both invite explanation.

One note may legitimately contain a bundle of closely related prompts. If so, the bundle members should be distinguishable and still support later rival comparison without confusion.

A reviewer can test prompt readiness with three questions:

1. **Is there a real open question?** If the text already asserts the answer, it is no longer a prompt.
2. **Is the prompt species plausible?** If the initiating pressure is opportunity-shaped or probe-shaped, forcing anomaly species is a category error.
3. **Could rival hypotheses now be compared against this prompt?** If not, the prompt candidate probably needs more stabilization before entering `B.5.2`.

Add three follow-up checks:

- **Is the scope tight enough for later comparison?**
- **Is there an imaginable rival-set, even if not yet fully written?**
- **Is the narrowing still a question rather than a disguised answer?**
### B.5.2.0:End

