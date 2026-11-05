## B.5.2.0 - Question Form for Entering Abduction (`U.AbductivePrompt`)

> **Type:** Definitional (D)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Question form for entering abduction.

**Use this when.** A stabilized cue, opportunity, probe-related observation or anomaly raises an explanatory question for B.5.2. Publish the question, its scope and motivating grounds while rival explanations remain open.

**What goes wrong if missed.** A cue is forced into anomaly form, an opportunity is treated as a hypothesis, or a prompt-like sentence silently smuggles in the preferred answer before rival hypotheses can be compared.

**What this buys.** A common entry criterion for abduction: prompt species, open question, scope and motivating grounds remain recoverable while candidate explanations stay open.

**Not this pattern when.** Not this pattern when the object is still a raw cue (`B.4.1`), a language-state threshold claim (`C.2.4`, `C.2.5`), a chosen hypothesis (`B.5.2`), or a selector decision about methods, substrates, or portfolios.

### B.5.2.0:0 - Question, account and publication form

`U.AbductivePrompt` is a claim-bearing account of one open explanatory question. It records the question, its scope, prompt species and motivating grounds. It is a same-individual-dependent kind under `U.Episteme`: the account keeps C.2.1 identity, and §4.2.2 supplies its prompt-membership test. It may seed `B.5.2` when those grounds and the applicable language-state thresholds support rival comparison. The reusable form expresses the account; it can also express another account of another question.

### B.5.2.0:1 - Problem frame
`B.5.2` needs a question account that preserves its motivating grounds, including when they arise from an opportunity or probe rather than an anomaly.

### B.5.2.0:2 - Problem
If anomaly is the only admissible input, pre-anomaly opportunity cues and route-derived prompt forms are excluded or misrepresented. If anything can enter, abduction loses its typed starting discipline.

### B.5.2.0:3 - Forces
| Force | Tension |
|---|---|
| **Breadth vs discipline** | Admit more than anomaly, but keep a bounded family of admissible prompt species. |
| **Reuse vs type inflation** | Use one entry form for several prompt species while keeping their questions distinguishable. |
| **Prompt vs hypothesis** | Keep the initiating prompt distinct from the downstream abductive outcome. |

### B.5.2.0:4 - Solution
`U.AbductivePrompt` classifies the question accounts used for entry into `B.5.2`. Use `A.16`, `A.16.1` and `B.4.1` when the initiating cue needs preservation, clarification or selection of its next reasoning contribution. Use `A.16.0` only when the cue-to-prompt history itself needs an explicit trajectory account. Publish the account in an expression adequate for the receiving use; reuse an adequate existing expression. Select a reusable form or additional publication faces when that use needs them. Account membership and current entry depend on the content and grounds below.

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
Use an extension species only when the motivating grounds support one of the bounded task-family, adaptation, utility or substrate questions defined below. Preserve the conditions needed to interpret that question; cue provenance or a trajectory account can carry those grounds.

`TaskFamilySpecializationPrompt` asks what explains a performance difference within the declared task family. `AdaptationProbePrompt` asks which rival explanations predict whether a proposed adaptation can reach the stated threshold. `NonHumanUtilityPrompt` asks what could explain the indicated utility advantage of a low-human-overlap approach. `SubstrateDiversificationPrompt` asks what explains the indicated limitation of the current substrate. For each species, B.5.2 may return a qualified explanatory conjecture or an abort, defer or split result. Preserve its motivating grounds and all conditions needed to interpret the question, including any applicable task-family, utility, threshold or budget conditions.

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

When returning to an earlier abductive inquiry, determine what changed and what the receiving work still needs before choosing a continuation:

| Finding | Warranted continuation |
|---|---|
| Same question and account; different support or candidate ranking | Reconsider the affected rivals under B.5.2 when further explanatory comparison is needed. |
| Same question; changed claims in its account | Identify the revised account under C.2.1; reassess current entry if the account will be used in B.5.2. |
| Changed explanatory demand, subject or relevant scope | State the new question and its relation to the earlier one; establish its entry grounds if it will be used in B.5.2. |
| Several distinct questions were bundled | Distinguish their accounts. Use B.5.2's split return when separate explanatory comparisons are needed; continue the needed questions under their own entry conditions. |
| An expression lost a condition needed to recover the question | Restore the expression before reusing the account or its answers. |
| The initiating ground fails or an adequate answer is already available | Abort or retire the current attempt as appropriate; preserve the earlier account and the reason for stopping. |

#### B.5.2.0:4.3 - Boundary rule
An account enters B.5.2 only when its question and declared prompt species meet the entry conditions in §4.1–4.2 and §17. For a choice among available probes, actions or specialist options, use C.11. Use C.38 to develop incomplete alternatives for the same intended result, C.11.DUA to examine an unclear evidence demand, and C.19 when the question is policy over a still-live candidate pool. C.18 records generation and comparison results; C.22.1 describes an adaptation signature. Neither performs the missing choice. An explanatory subquestion arising during planning can still enter B.5.2 on its own grounds.

### B.5.2.0:5 - Archetypal Grounding
**Tell.** An anomaly is one prompt species, not the only one.

**Show (System).** A control observation may raise competing explanations of an apparent response improvement without being framed as an anomaly. The abductive result qualifies those explanations; choosing a discriminating probe is a separate C.11 decision.

**Show (Episteme).** Suppose a revised theory appears to account for two previously separate results. An opportunity-style prompt asks what could explain this apparent gain in explanatory reach.

### B.5.2.0:6 - Bias-Annotation
The pattern admits several prompt species while keeping the explanatory question and its motivating grounds explicit.

### B.5.2.0:7 - Conformance Checklist
- `CC-B.5.2.0-1` Every `U.AbductivePrompt` **SHALL** declare its prompt species.
- `CC-B.5.2.0-2` A prompt **SHALL NOT** be confused with a finished hypothesis.
- `CC-B.5.2.0-3` Cue-derived prompts **SHOULD** preserve route provenance when it exists and contributes to their entry.
- `CC-B.5.2.0-4` Prompt publication **SHALL** include the explanatory question, its scope and the motivating provenance that make abduction appropriate.
- `CC-B.5.2.0-5` An account that asserts its answer as settled or suppresses plausible rivals **SHALL NOT** be used as the open prompt for that inquiry.
- `CC-B.5.2.0-6` When a specialization-sensitive prompt species is used, the prompt account **SHALL** make explicit the declared task family or utility target and the grounds for its explanatory question. Include every threshold, budget or other condition needed to interpret that question or its proposed use, and preserve the cue, witness or route provenance actually used.
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
- the **motivating provenance actually used**,
- the **contrast set**, if one is already visible,
- the **scope** in which the question is being asked,
- and the **witnesses or cue grounds** that justify beginning abduction.

This package lets downstream conjectures be assessed against the same identified explanatory question.

For specialization-sensitive prompt species, preserve the declared task family or utility target, the conditions needed for the explanatory question, including any stated threshold or budget, and the motivating provenance actually used. Preserve alternative prompt shapes when they remain live and matter to entry.

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

Entry into `B.5.2` requires a question explicit enough to compare potential explanations under its scope. An underspecified question needs clarification before that entry. Continue stabilization or routing when needed for the receiving question.

Determine what a missing contrast or witness prevents. If it leaves the explanatory question or other membership conditions unrecoverable, `U.AbductivePrompt` membership is not established. If the account meets those conditions but lacks grounds for entry now, retain the account with that current-use limit under §4.2.2.

A common failure mode is drift from cue -> prompt -> hypothesis without anyone naming the boundary crossings. `B.5.2.0` blocks that drift by keeping the prompt package distinct from both the earlier cue pack and the downstream prime hypothesis.

### B.5.2.0:17 - Scope, rival-set, and comparative-validity discipline

A prompt should declare the scope in which its question is being asked: the domain fragment, operational horizon, or inquiry-bounded scope cut that makes the question answerable. If the relevant scope is unresolved, apparent rivals may answer different questions; establish the scope needed for their comparison.

A prompt need not list hypotheses yet. Its explanatory demand and scope must make clear what a candidate explanation would have to explain; any already identified answer types can help clarify that demand.

A prompt may be narrowed to become more discriminating, but the narrowing must not silently smuggle in the answer it is supposedly asking about. Otherwise the prompt ceases to be an initiating question and becomes a disguised conclusion. If its formulation excludes plausible rivals without grounds, repair that restriction; if it asserts an answer as settled, treat the answer-bearing account under its governing pattern.

Prompts may be compared across contexts only when their species, scope, and provenance are explicit. A probe-shaped question and an opportunity-shaped question are not the same kind of abductive entry merely because both invite explanation.

One note may legitimately contain a bundle of closely related prompts. If so, the bundle members should be distinguishable and still allow downstream rival comparison without confusion.

An assurance reader can test prompt readiness with three questions:

1. **Is there an open explanatory question?** An asserted answer is no longer a prompt; narrowing the scope must leave the answer open. An action-choice question needs its own Method.
2. **Does the prompt species fit its initiating grounds?** If those grounds are an opportunity or a probe-related contrast, forcing anomaly species misclassifies the question.
3. **Is the question explicit enough to generate and compare candidate explanations under its declared scope?** Establish the question and the grounds required for entry before using B.5.2. Identified rival hypotheses are not an entry requirement; their generation and comparison belong to B.5.2.
### B.5.2.0:End
