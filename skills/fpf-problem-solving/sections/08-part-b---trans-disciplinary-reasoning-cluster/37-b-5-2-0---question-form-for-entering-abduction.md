## B.5.2.0 - Question Form for Entering Abduction (`U.AbductivePrompt`)

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Question form for entering abduction.

**Use this when.** Use this pattern when a stabilized cue, opportunity, probe-related observation or anomaly raises an explanatory question for B.5.2. Publish the question, its scope and motivating grounds while rival explanations remain open.

**What goes wrong if missed.** A cue is forced into anomaly form, an opportunity is treated as a hypothesis, or a prompt-like sentence silently smuggles in the preferred answer before rival hypotheses can be compared.

**What this buys.** A small admission form for abduction: prompt species, open question, scope, and provenance stay explicit while the downstream abductive loop remains free to compare rival answers.

**Not this pattern when.** Not this pattern when the object is still a raw cue (`B.4.1`), a language-state threshold claim (`C.2.4`, `C.2.5`), a chosen hypothesis (`B.5.2`), or a selector decision about methods, substrates, or portfolios.

### B.5.2.0:0 - Kind and publication-form boundary

`U.AbductivePrompt` is a dependent durable publication-form value under episteme publication and abductive entry, not a root U-kind. Its identity is the typed prompt form that may seed `B.5.2` after cue preservation, routing, and language-state threshold checks. A cue, routing note, anomaly sentence, candidate hypothesis, or local prompt label does not become `U.AbductivePrompt` unless the prompt species, open question, scope, and provenance required by this pattern are present.

### B.5.2.0:1 - Problem frame
`B.5.2` needs an entry form that can accept admissible language-state trajectories after cue preservation and routing, without pretending that anomaly is the only admissible starting form.

### B.5.2.0:2 - Problem
If anomaly is the only admissible input, pre-anomaly opportunity cues and route-derived prompt forms are excluded or misrepresented. If anything can enter, abduction loses its typed starting discipline.

### B.5.2.0:3 - Forces
| Force | Tension |
|---|---|
| **Breadth vs discipline** | Admit more than anomaly, but keep a bounded family of admissible prompt species. |
| **Reuse vs type inflation** | Introduce a clean entry form without exploding the number of heavy publication kinds. |
| **Prompt vs hypothesis** | Keep the initiating prompt distinct from the downstream abductive outcome. |

### B.5.2.0:4 - Solution
`U.AbductivePrompt` is a narrow family head for the prompt forms that may admissibly seed `B.5.2` after admissible cue preservation and governing-pattern selection under `A.16`, `A.16.1`, and `B.4.1`. `A.16.0` is used only when the cue-to-prompt history itself has governance value as an explicit trajectory account. When rendered, a prompt uses ordinary MVPK faces; prompt status is a property of the publication form, not a rival face ontology.

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
These extension species are admissible only when cue provenance or trajectory account already carries the bounded-specialization evidence requirement by value; they are not the starter canonical entry set for ordinary abduction.

`TaskFamilySpecializationPrompt` asks what explains a performance difference within the declared task family. `AdaptationProbePrompt` asks which rival explanations predict whether a proposed adaptation can reach the stated threshold. `NonHumanUtilityPrompt` asks what could explain the indicated utility advantage of a low-human-overlap approach. `SubstrateDiversificationPrompt` asks what explains the indicated limitation of the current substrate. In each species, B.5.2 returns qualified explanatory conjectures; task family, utility target, threshold, budget and motivating evidence qualify that question.

#### B.5.2.0:4.2 - Core shape
A conforming abductive prompt makes `promptSpecies`, its explanatory `openQuestion`, `scope` and motivating provenance explicit. The provenance may be carried by `motivatingCueRef`, `witnessRefs` or `routeProvenance`; include the applicable basis even when no routing history exists. A rendering may additionally include `contrastSet` and `GammaTime`.

A prompt is not yet a hypothesis. Prompt admission usually presupposes articulation high enough to publish a stable open question and closure low enough that rival answers remain live; those articulation and closure thresholds remain governed by `C.2.4` and `C.2.5`, typically reached through cue or route provenance from `A.16.1` and `B.4.1`. It is the initiating publication form that licenses entry into the abductive loop.

#### B.5.2.0:4.3 - Boundary rule
Only a declared prompt species carrying an explanatory question enters B.5.2 through this form. For a choice among available probes, actions or specialist options, use C.11. Use C.38 to develop incomplete alternatives for the same intended result, C.11.DUA to examine an unclear evidence demand, and C.19 when the question is policy over a still-live candidate pool. C.18 records generation and comparison results; C.22.1 describes an adaptation signature. Neither performs the missing choice. An explanatory subquestion arising during planning can still enter B.5.2 on its own grounds.

### B.5.2.0:5 - Archetypal Grounding
**Tell.** An anomaly is one prompt species, not the only one.

**Show (System).** A control observation may raise competing explanations of an apparent response improvement without being framed as an anomaly. The abductive result qualifies those explanations; choosing a discriminating probe is a separate C.11 decision.

**Show (Episteme).** A promising mismatch can begin an opportunity-style abductive prompt rather than only a problem statement.

### B.5.2.0:6 - Bias-Annotation
The pattern broadens the entry form to abduction, but still keeps it typed and auditable.

### B.5.2.0:7 - Conformance Checklist
- `CC-B.5.2.0-1` Every `U.AbductivePrompt` **SHALL** declare its prompt species.
- `CC-B.5.2.0-2` A prompt **SHALL NOT** be confused with a finished hypothesis.
- `CC-B.5.2.0-3` Cue-derived prompts **SHOULD** preserve route provenance.
- `CC-B.5.2.0-4` Prompt publication **SHALL** include the explanatory question, its scope and the motivating provenance that make abduction appropriate.
- `CC-B.5.2.0-5` A publication that already fixes the answer or suppresses plausible rivals **SHALL NOT** remain in prompt status.
- `CC-B.5.2.0-6` When a specialization-sensitive prompt species is used, the prompt package **SHALL** make explicit the declared task family or utility target, the threshold or success condition being probed, the current budget window, and the route or cue provenance that made the prompt admissible.

### B.5.2.0:8 - Common Anti-Patterns and How to Avoid Them
- **Prompt equals hypothesis.** Keep the prompt distinct from the abductive output.
- **A choice disguised as abduction.** Recover the explanatory question, if one exists; send the probe, action or acquisition choice to its actual Method.
- **Route amnesia.** A cue-derived prompt loses the early route provenance that explains why it entered here.

### B.5.2.0:9 - Consequences
The benefit is cleaner, less brittle abduction-entry terms. The trade-off is one additional explicit prompt family head and one more declared publication form.

### B.5.2.0:10 - Rationale
This keeps admissible cue preservation and trajectory publication able to dock into `B.5.2` through a typed prompt form without anomaly inflation and without making `A.16.0` mandatory.

### B.5.2.0:11 - SoTA-Echoing
The pattern reflects real abductive practice, where opportunities, probe prompts, and stabilized cues often begin the loop before a full anomaly formulation exists.

### B.5.2.0:12 - Relations
- Builds on: `C.2.2a`, `A.16`, `A.16.1`, `B.4.1`, `C.2.LS`, `C.2.4`, `C.2.5`.
- Coordinates with: `A.16.0`, `A.16.2`, `C.2.6`, `C.2.7`, `B.5.2`, `A.6.P`, `C.16.Q`, `A.6.A`, `F.9.1`.
- Constrains: admissible prompt entry into abduction.
### B.5.2.0:13 - Worked Prompt Species

#### B.5.2.0:13.1 - Anomaly statement as canonical prompt
In a constructed service case, latency rises from 8 ms to 40 ms under the same declared workload. The prompt asks what could explain that contrast, names the service and time window, and cites the measurements. Rival explanations may concern contention or a changed cache path; neither is asserted by publishing the prompt. B.5.2 compares their plausibility and may return a qualified conjecture or defer.

#### B.5.2.0:13.2 - Opportunity-style prompt
An opportunity cue may raise an explanatory question about an indicated advantage without a failure. For example, an unexpectedly stable response in one operating range invites rival explanations of that stability. Whether to exploit the opportunity is a separate action choice.

#### B.5.2.0:13.3 - Probe-style prompt
A probe-related observation may prompt an explanatory question: which rival explanations predict the measured contrast under the stated perturbation? If the question is instead which available probe is cheapest or most discriminating for the current purpose, use C.11. The probe choice does not require an abductive prompt merely to acquire that input form.

#### B.5.2.0:13.4 - Specialization-sensitive prompt set
Use a specialization-sensitive species for its explanatory question in §4.1.1. For example, a measured performance contrast can prompt rival explanations tied to a declared task family and budget. Acquiring a specialist Method or competence bundle instead requires the applicable option or alternative-development decision. Retain task family, threshold, budget and cue provenance in whichever receiving use needs them; prompt publication does not select the acquisition.

### B.5.2.0:14 - Prompt package discipline

A prompt becomes reusable in `B.5.2` only when its initiating question is explicit enough to remain stable across downstream hypothesis work.

#### B.5.2.0:14.1 - Minimal prompt package

A robust abductive prompt should make explicit:

- the **prompt species**,
- the **open question**,
- the **motivating cue or route provenance**,
- the **contrast set**, if one is already visible,
- the **scope** in which the question is being asked,
- and the **witnesses or cue grounds** that justify beginning abduction.

This package lets downstream conjectures be tested against the same question rather than against a rewritten paraphrase.

For specialization-sensitive prompt species, the package should also make explicit the declared task family or utility target, the threshold or success condition being probed, the current budget window, the prior route provenance, and the rival prompt shapes still in play.

#### B.5.2.0:14.2 - Prompts are questions, not claims

A prompt may cue one explanation, but it remains a question-bearing entry form. If the text already asserts the answer, it has moved past prompt status and should be treated under `B.5.2` or another governing pattern that carries the asserted answer.

#### B.5.2.0:14.3 - Prompt provenance remains load-bearing

The motivating provenance is part of prompt admission. Preserve the route, cue or witness basis actually used; a prompt with no routing history does not need an invented route.

#### B.5.2.0:14.4 - Check prompt against silent promotion
An assurance reader should watch for the common mistake where authors silently upgrade a prompt into a hypothesis merely because the prose sounds explanatory. If the text already leans on one preferred answer as settled, either rewrite it back into a real question or explicitly apply the governing pattern that carries the asserted answer.

### B.5.2.0:15 - Species boundary reminders

Use anomaly species for an explanatory question arising from a failure, contradiction or surprising departure from the current model. Use opportunity species for an explanatory question arising from an indicated advantage. Use probe species for rival explanations of an observation or predicted contrast associated with a stated probe.

For the four specialization-sensitive species, use the explanatory questions and conditions in §4.1.1. Questions asking which option to acquire, which probe to perform or which substrate to try follow the direct choice routes in §4.3.

Cue-derived prompt entries should stay prompt-headed species rather than projection-headed aliases. The load-bearing question is the prompt kind itself, not one package-local naming trick.

### B.5.2.0:16 - Boundary crossing and invalid drift

A prompt should enter `B.5.2` only when the question is explicit enough that rival hypotheses can now be compared against it. If the question is still underspecified, the admissible continuation is further stabilization or routing, not premature abduction.

A routed cue may be close to prompt form but still missing one decisive contrast or witness. In such cases the candidate stays outside `U.AbductivePrompt` until its initiating question is stable.

A bare intuition, slogan, or rhetorical question with no prompt species and no cue provenance is not yet an admissible `U.AbductivePrompt`.

A common failure mode is drift from cue -> prompt -> hypothesis without anyone naming the boundary crossings. `B.5.2.0` blocks that drift by keeping the prompt package distinct from both the earlier cue pack and the downstream prime hypothesis.

### B.5.2.0:17 - Scope, rival-set, and comparative-validity discipline

A prompt should declare the scope in which its question is being asked: the domain fragment, operational horizon, or inquiry-bounded scope cut that makes the question answerable. If scope remains unbounded, rival hypotheses become incomparable because they are answering different questions.

A prompt need not list full hypotheses yet, but it should make visible whether rival answer types are already imaginable. If no rival answer space is even latent, the publication may still be a cue or orientation note rather than a true abductive prompt.

A prompt may be narrowed to become more discriminating, but the narrowing must not silently smuggle in the answer it is supposedly asking about. Otherwise the prompt ceases to be an initiating question and becomes a disguised conclusion. If a prompt already excludes every serious rival except one preferred explanatory line, the publication may already be preloading a hypothesis. Review should then either rewrite the prompt back into a real question or explicitly apply the governing pattern that carries the asserted answer.

Prompts may be compared across contexts only when their species, scope, and provenance are explicit. A probe-shaped question and an opportunity-shaped question are not the same kind of abductive entry merely because both invite explanation.

One note may legitimately contain a bundle of closely related prompts. If so, the bundle members should be distinguishable and still allow downstream rival comparison without confusion.

An assurance reader can test prompt readiness with three questions:

1. **Is there a real open explanatory question?** An asserted answer is no longer a prompt; an action-choice question needs its own Method.
2. **Is the prompt species plausible?** If the initiating cue shape is opportunity-shaped or probe-shaped, forcing anomaly species is a category error.
3. **Could rival hypotheses now be compared against this prompt?** If not, the prompt candidate probably needs more stabilization before entering `B.5.2`.

Add three follow-up checks:

- **Is the scope tight enough for downstream comparison?**
- **Is there an imaginable rival-set, even if not yet fully written?**
- **Is the narrowing still a question rather than a disguised answer?**
### B.5.2.0:End
