## B.5.2.0 - Question Form for Entering Abduction (`U.AbductivePrompt`)

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Question form for entering abduction.

**Use this when.** A stabilized cue, opportunity, probe-related observation or anomaly raises an explanatory question for B.5.2. Publish the question, its scope and motivating grounds while rival explanations remain open.

**What goes wrong if missed.** A cue is forced into anomaly form, an opportunity is treated as a hypothesis, or a prompt-like sentence silently smuggles in the preferred answer before rival hypotheses can be compared.

**What this buys.** A small admission form for abduction: prompt species, open question, scope, and provenance stay explicit while the downstream abductive loop remains free to compare rival answers.

**Not this pattern when.** Not this pattern when the object is still a raw cue (`B.4.1`), a language-state threshold claim (`C.2.4`, `C.2.5`), a chosen hypothesis (`B.5.2`), or a selector decision about methods, substrates, or portfolios.

### B.5.2.0:0 - Question, account and publication form

`U.AbductivePrompt` is a claim-bearing account of one open explanatory question. It records the question, its scope, prompt species and motivating grounds. It is a same-individual-dependent kind under `U.Episteme`: the account keeps C.2.1 identity, and §4.2.2 supplies its prompt-membership test. It may seed `B.5.2` when those grounds and the applicable language-state thresholds support rival comparison. The reusable form expresses the account; it can also express another account of another question.

### B.5.2.0:1 - Problem frame
`B.5.2` needs an entry form that preserves a question's motivating grounds, including when they arise from an opportunity or probe rather than an anomaly.

### B.5.2.0:2 - Problem
If anomaly is the only admissible input, pre-anomaly opportunity cues and route-derived prompt forms are excluded or misrepresented. If anything can enter, abduction loses its typed starting discipline.

### B.5.2.0:3 - Forces
| Force | Tension |
|---|---|
| **Breadth vs discipline** | Admit more than anomaly, but keep a bounded family of admissible prompt species. |
| **Reuse vs type inflation** | Use one entry form for several prompt species while keeping their questions distinguishable. |
| **Prompt vs hypothesis** | Keep the initiating prompt distinct from the downstream abductive outcome. |

### B.5.2.0:4 - Solution
`U.AbductivePrompt` classifies the question accounts used for entry into `B.5.2`. Use `A.16`, `A.16.1` and `B.4.1` when the initiating cue needs preservation, clarification or selection of its next reasoning contribution. Use `A.16.0` only when the cue-to-prompt history itself needs an explicit trajectory account. Publish the account through a suitable form and ordinary MVPK faces; account membership and current entry depend on the content and grounds described below.

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

A prompt is not yet a hypothesis. Prompt admission usually presupposes articulation high enough to publish a stable open question and closure low enough that rival answers remain live; those articulation and closure thresholds remain governed by `C.2.4` and `C.2.5`, typically reached through cue or route provenance from `A.16.1` and `B.4.1`. The published account must satisfy those entry conditions; its layout supplies no additional admission.

##### B.5.2.0:4.2.1 - Identify the explanatory question

Identify the question from what the inquiry asks someone to explain:

- the subject and the fact, contrast or expected effect to be explained;
- the relevant population, conditions and time horizon in `scope`;
- the explanatory demand: what remains unknown and what an answer would have to explain.

Resolve the terms against their intended referents and interpretation. These three elements identify the question together. A change of wording, notation or publication preserves it when those elements retain their meaning. Two questions differ when a change in any element changes what an explanation must answer. A current list of rival hypotheses helps compare answers; it need not exhaust the possible answers and does not identify the question by itself.

Distinguish making an existing condition explicit from changing that condition. Use the earlier expression and its recoverable context to establish which happened. If a table drops an essential condition, first restore the damaged expression. When the earlier question cannot be recovered, leave its continuity unresolved; do not carry an earlier answer across the gap as an answer to the new formulation.

Motivating evidence and `promptSpecies` qualify the entry. Changing them changes the question only when it changes the explanatory demand, subject or relevant scope. A new observation can change the grounds for comparing explanations of the same event. Correcting the reported event can instead remove the reason to seek that explanation or raise a different question. A budget change affects question identity when the question concerns performance under that budget; a change in the resources available to investigate the same event need not do so.

This rule identifies the explanatory content of the question. An occasion on which someone asks it has its own occurrence identity.

##### B.5.2.0:4.2.2 - Identify the prompt account and check its use

A prompt account makes claims about one question identified under §4.2.1: what is being asked, its scope, how it arose and the grounds for treating it as open in the stated inquiry. The question is its exact `EntityOfConcern`. C.2.1 identifies that account as one `U.Episteme` through its claim content, the question and the effective `ReferenceScheme`.

Under `FPFCoreReferenceScheme`, that same episteme is a `U.AbductivePrompt` when its content records one recoverable explanatory question, a declared species with the conditions in §4.1, and the scope and motivating provenance in §4.2, while leaving rival answers open. Thus `U.AbductivePrompt(E)` implies `U.Episteme(E)` for the same individual. This is the same-individual-dependent membership rule. An unfilled layout, an underspecified cue and an account that asserts its preferred answer as settled fail this test for different reasons: no particular account, an unrecoverable question, or an answer-bearing account.

Use §4.2 and §17 to judge whether that account supports entry into B.5.2 now. An account can remain identifiable after its grounds have failed or its question has been answered. Keep it available as the earlier entry and record the warranted continuation; its earlier admission does not authorize a new run without current grounds.

The same question may have several accounts with different claims or effective schemes. Additional evidence changes account identity only when it changes one of C.2.1's identity constituents; adding an evidence relation alone need not do so. A reusable publication form can express different accounts. E.24.PUB governs the selected account's expression and publication; A.6.3.RT governs a prose-to-table transfer when that representation changes. A note containing several questions may express several prompt accounts in the same document.

On return to an earlier abductive inquiry, determine what changed before restarting it:

| Finding | Warranted continuation |
|---|---|
| Same question and account; different support or candidate ranking | Reconsider the affected rivals under B.5.2. |
| Same question; changed claims in its account | Identify the revised account under C.2.1 and reassess entry on its current grounds. |
| Changed explanatory demand, subject or relevant scope | State the new question and its relation to the earlier one; establish its own entry. |
| Several distinct questions were bundled | Separate their accounts and use B.5.2's split return. |
| An expression lost a condition needed to recover the question | Restore the expression before reusing the account or its answers. |
| The initiating ground fails or an adequate answer is already available | Abort or retire the current attempt as appropriate; preserve the earlier account and the reason for stopping. |

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
- `CC-B.5.2.0-7` Before restarting an inquiry, or reusing its prompt after a change in wording, scope or motivating grounds that may affect the question or account, the user **SHALL** apply §4.2.1–4.2.2 to establish the affected continuity and entry conditions. Already established identity and unaffected grounds remain reusable while their basis holds; comparing another rival with an unchanged prompt requires no new continuity assessment.

### B.5.2.0:8 - Common Anti-Patterns and How to Avoid Them
- **Prompt equals hypothesis.** Keep the prompt distinct from the abductive output.
- **A choice disguised as abduction.** Recover the explanatory question, if one exists; send the probe, action or acquisition choice to its actual Method.
- **Route amnesia.** A cue-derived prompt loses the early route provenance that explains why it entered here.

### B.5.2.0:9 - Consequences
The benefit is a common entry criterion for cue clarification, abductive comparison and later return to the inquiry. The cost is distinguishing the question from its account when either changes; a new form, file or question identifier is unnecessary when the existing publication makes that distinction recoverable.

### B.5.2.0:10 - Rationale
A typed prompt lets a preserved cue contribute its explanatory question to `B.5.2` while retaining the grounds that made the question worth asking.

### B.5.2.0:11 - SoTA-Echoing
An opportunity or a probe-related contrast can raise an explanatory question without being formulated as an anomaly.

As a foundational semantic comparison, Ciardelli, *Why We Need a Question Semantics* (author preprint, 2021; published chapter, 2022), distinguishes an issue from its expression and from the act of asking, and develops resolution conditions for questions. His *Inquisitive Action Logic* (2026) continues to treat questions as semantic content used within a formal system. Here that distinction supports separating the question from an account about it. The local explanatory-question rule in §4.2.1 is an FPF construction; these sources do not supply its account-membership rule or a universal identity test for explanations. Sources: [chapter record](https://research.unipd.it/handle/11577/3466402), [2026 paper](https://arxiv.org/abs/2606.31866).

### B.5.2.0:12 - Relations
- Builds on: `C.2.1`, `C.2.2a`, `A.16`, `A.16.1`, `B.4.1`, `C.2.LS`, `C.2.4`, `C.2.5`, `E.24.PUB`, `E.24.UK`.
- Coordinates with `A.6.3.RT` for representation transfer and `B.5.QD` for developing or changing a question.
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

#### B.5.2.0:13.5 - Same question, revised account and reused form

Continue the constructed service case in §13.1. The question asks what explains the rise from 8 ms to 40 ms for the named service, workload and time window. A paragraph and a table preserve the same question when both retain that contrast and scope. If the table also preserves the account's claims and effective scheme, C.2.1 identifies the same account; E.24.PUB separately governs its new expression and availability. If the table omits the workload, restore that condition before treating its shortened question as equivalent.

New contention logs can support one rival more strongly while the latency question stays unchanged. An assertion about that new support can belong to a revised account, or to a separate evidence account linked to the unchanged prompt. Determine which content actually changed. If corrected measurements establish that latency stayed at 8 ms, the current attempt to explain an actual rise loses its initiating ground. Asking why the monitor reported 40 ms is a different question about the report; its answer need not explain a real slowdown.

The same `AnomalyStatement` layout can express that reporting question and a question about a real slowdown in another service. Its shared columns do not identify one common question. Record each subject, contrast and scope so that the two accounts and their rivals remain distinguishable; they may occupy two rows of one note. One hypothesis that happens to answer both questions would still not make the questions identical.

### B.5.2.0:14 - Prompt package discipline

A prompt becomes reusable in `B.5.2` only when its initiating question is explicit enough to remain stable across downstream hypothesis work.

#### B.5.2.0:14.1 - Minimal prompt package

An abductive prompt should make explicit:

- the **prompt species**,
- the **open question**,
- the **motivating cue or route provenance**,
- the **contrast set**, if one is already visible,
- the **scope** in which the question is being asked,
- and the **witnesses or cue grounds** that justify beginning abduction.

This package lets downstream conjectures be tested against the same question rather than against a rewritten paraphrase.

For specialization-sensitive prompt species, the package should also make explicit the declared task family or utility target, the threshold or success condition being probed, the current budget window, the prior route provenance, and the rival prompt shapes still in play.

#### B.5.2.0:14.2 - Claims about the question and an asserted answer

A prompt account states what is being asked and why, while leaving the answer open. It may cue one explanation among rivals. If the text instead asserts the answer as settled, it has moved past prompt status and should be treated under `B.5.2` or another governing pattern that carries the asserted answer.

#### B.5.2.0:14.3 - Prompt provenance remains load-bearing

The motivating provenance is part of prompt admission. Preserve the route, cue or witness basis actually used; a prompt with no routing history does not need an invented route.

#### B.5.2.0:14.4 - Check prompt against silent promotion
An assurance reader should watch for the common mistake where authors silently upgrade a prompt into a hypothesis merely because the prose sounds explanatory. If the text already leans on one preferred answer as settled, either rewrite it back into a real question or explicitly apply the governing pattern that carries the asserted answer.

### B.5.2.0:15 - Species boundary reminders

Use anomaly species for an explanatory question arising from a failure, contradiction or surprising departure from the current model. Use opportunity species for an explanatory question arising from an indicated advantage. Use probe species for rival explanations of an observation or predicted contrast associated with a stated probe.

For the four specialization-sensitive species, use the explanatory questions and conditions in §4.1.1. Questions asking which option to acquire, which probe to perform or which substrate to try follow the direct choice routes in §4.3.

Name each cue-derived entry as a prompt species, preserving the explanatory question it introduces.

### B.5.2.0:16 - Boundary crossing and invalid drift

A prompt should enter `B.5.2` only when the question is explicit enough that rival hypotheses can now be compared against it. If the question is still underspecified, the admissible continuation is further stabilization or routing, not premature abduction.

A routed cue may be close to prompt form but still missing one decisive contrast or witness. In such cases the candidate stays outside `U.AbductivePrompt` until its initiating question is stable.

A common failure mode is drift from cue -> prompt -> hypothesis without anyone naming the boundary crossings. `B.5.2.0` blocks that drift by keeping the prompt package distinct from both the earlier cue pack and the downstream prime hypothesis.

### B.5.2.0:17 - Scope, rival-set, and comparative-validity discipline

A prompt should declare the scope in which its question is being asked: the domain fragment, operational horizon, or inquiry-bounded scope cut that makes the question answerable. If scope remains unbounded, rival hypotheses become incomparable because they are answering different questions.

A prompt need not list full hypotheses yet, but it should make visible whether rival answer types are already imaginable. If no rival answer space is even latent, the publication may still be a cue or orientation note rather than a true abductive prompt.

A prompt may be narrowed to become more discriminating, but the narrowing must not silently smuggle in the answer it is supposedly asking about. Otherwise the prompt ceases to be an initiating question and becomes a disguised conclusion. If a prompt already excludes every serious rival except one preferred explanatory line, the publication may already be preloading a hypothesis. Review should then either rewrite the prompt back into a real question or explicitly apply the governing pattern that carries the asserted answer.

Prompts may be compared across contexts only when their species, scope, and provenance are explicit. A probe-shaped question and an opportunity-shaped question are not the same kind of abductive entry merely because both invite explanation.

One note may legitimately contain a bundle of closely related prompts. If so, the bundle members should be distinguishable and still allow downstream rival comparison without confusion.

An assurance reader can test prompt readiness with three questions:

1. **Is there an open explanatory question?** An asserted answer is no longer a prompt; narrowing the scope must leave the answer open. An action-choice question needs its own Method.
2. **Does the prompt species fit its initiating grounds?** If those grounds are an opportunity or a probe-related contrast, forcing anomaly species misclassifies the question.
3. **Could meaningful rival hypotheses now be compared under the declared scope?** The rival set need not yet be fully written, but possible alternatives and a scope that permits their comparison must be recoverable. Otherwise stabilize the prompt before entering `B.5.2`.
### B.5.2.0:End
