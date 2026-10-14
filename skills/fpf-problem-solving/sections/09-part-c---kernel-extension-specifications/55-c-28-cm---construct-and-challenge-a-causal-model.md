## C.28.CM - Construct and Challenge a Causal Model

> **Type:** Method pattern
> **Status:** Stable
> **Normativity:** Normative unless marked informative

### C.28.CM:1 - Problem frame

Use this pattern when an explanation names a possible cause but leaves you unable to work out what follows, compare another mechanism, or say what observation could change the explanation. The difficulty can arise in a work process, a physical device or an AI-assisted task. A plausible story is available; the causal relations needed for the question still have to be constructed.

Begin with one outcome, the contrast that matters, and the relevant observations and subject knowledge. Express two materially different accounts when both remain plausible. Work out a consequence on which they differ, or identify the premise that prevents that comparison. An annotated sketch and a conditional explanation can be the first useful result.

The governed object is the causal model, or family of alternative causal models, being constructed for that question. This is the causal branch of broader modeling and explanation work. The model describes proposed mechanisms and the conditions of a consequence; it remains distinct from the situation, its observations and the evidence for those mechanisms.

Use a sufficient existing model directly. A calculation under known physical relations can finish in B.5.FM or C.28.MR. A disagreement about whose objective should govern needs that practical or normative decision; constructing more causal arrows will not supply it. If a subject relation cannot be recovered, ask for that relation or retain the missing premise. Neither a literature review nor a numerical model is a universal prerequisite.

### C.28.CM:2 - Problem

“Missing information caused the delay” can conceal several accounts. The information may be needed to perform the work. Both the omission and the delay may arise from overload. The recorded omission may describe a logging failure rather than the information actually available. Studying only reported incidents can introduce a further difference.

These accounts can support different responses while fitting the same initial story. Filling a field, changing the generating process, improving registration and temporarily supplying another route are different actions. A model makes their assumptions and consequences inspectable before one narrative becomes the explanation.

A second difficulty arises when a diagram is mistaken for evidence. Drawing a mediator does not establish that the mechanism operated. Leaving out an arrow makes a substantive assumption. A model can be useful for exposing such a premise before it supports an empirical effect claim.

### C.28.CM:3 - Forces

| Force | Consequence for construction |
| --- | --- |
| A useful first result may be qualitative. | Add equations or probability laws when the needed consequence requires them. |
| Subject knowledge constrains mechanisms, while the first account may be incomplete. | Keep the basis for a relation and a serious alternative recoverable. |
| More variables can expose a missed influence or make construction unaffordable. | Add a distinction when its omission can change the answer. |
| Different models can fit the available observations. | Preserve the resulting uncertainty instead of selecting a graph for its appearance. |
| An action can help before its complete explanation is known. | Return the supported conditional result and let the receiving decision judge whether further inquiry is worthwhile. |

### C.28.CM:4 - Solution

Construct the account around the question, then challenge the relations on which its useful consequence depends. The following moves can return to one another. A discovered measurement error may change the outcome definition; a missing mechanism may change the question.

#### C.28.CM:4.1 - Fix the contrast and the time that matter

State what needs explaining or changing. Name the outcome and the cases it concerns, the relevant time, and any proposed action or comparison. “Why did this queue start?”, “Why does it remain?” and “What will shorten it now?” can require different mechanisms.

Distinguish an observed comparison from an intervention query. Observing X=x supplies information about the mechanisms already operating; imposing X=x replaces a mechanism. When the question concerns the same past case under another action, preserve its factual observations and the underlying conditions they constrain. C.28.MR develops the corresponding model calculation; C.28 determines what supports that use.

Keep the question small enough for a useful contrast. If two retained accounts permit the same sufficient next action under its own grounds, C.11.DUA can settle whether distinguishing them is worth the effort.

#### C.28.CM:4.2 - Turn the story into variables with subject meaning

Choose quantities or distinctions that can vary across the relevant cases or times. Give each a meaning, possible values and observation time. A particular late delivery is a case; its lateness is a value of a selected variable. Whether a variable is binary, ordinal or continuous depends on the question and measurement.

Separate the subject quantity from its registration when that difference matters. For example, distinguish an identifier present in the submitted report, a log entry reporting its absence, and inclusion of that report in an incident sample. Recover how the observation is produced through C.16 when needed. A copied ticket is another report of the same event, not another occurrence of it.

Retain enough distinctions for the proposed contrast. Combining two stages is unsafe when the action can change one while leaving the other unchanged. Conversely, a single “ready for dispatch” variable may suffice until readiness failures require different responses.

#### C.28.CM:4.3 - Propose mechanisms and serious alternatives

For each consequential relation, explain how changing a proposed cause could change its effect under the relevant conditions. Use the process arrangement, physical law, subject theory, observations or qualified source that supports that proposal. Mark a conjecture as such. A chronological sequence can suggest a mechanism while leaving common causes unresolved.

Construct a material alternative: another cause, a common influence, a recording difference, or a model in which the proposed direct influence is absent. Causes may coexist. An account of overload need not remove an effect of missing information. Keep the outcome and horizon comparable, and specify the same intervention in each model when that is the question.

A directed arrow X → Y represents a proposed direct causal influence in the chosen model. “Direct” is relative to the variables retained. Explain a consequential omitted influence as carefully as an included one: excluding it may be what makes the answer follow.

For an equation-based model, write the relevant mechanisms in a form such as Y=f(X,U), where U represents inputs left outside that mechanism. Specify shared inputs or their dependence when needed. A graph supplies qualitative restrictions; it does not supply an omitted functional form, effect size or disturbance law. Ask for these only when the receiving calculation needs them.

#### C.28.CM:4.4 - Inspect the whole relevant structure

Follow possible paths between the proposed cause and outcome. Look for common causes, intermediate mechanisms, measurement processes and selection of cases. A common cause can coexist with a causal path. The role of a node is relative to a path and question, not a permanent label attached to the variable.

For a **directed acyclic graph (DAG)**, the following path test makes that inspection precise. A path joins distinct nodes along edges, ignoring arrow direction when finding the path. At an internal node, two arrowheads meeting there make it a collider on that path; other internal nodes are noncolliders.

Given a conditioning set W disjoint from the endpoints, a path is open when every noncollider on it is outside W and every collider is itself in W or has a descendant in W. Otherwise it is blocked. If every path between two variable sets is blocked, the sets are d-separated by W. For a distribution satisfying the graph's Markov property, d-separation implies the corresponding conditional independence. An open path permits dependence; it does not guarantee it for every parameter choice. Inferring graph structure from observed independences needs further assumptions, often faithfulness (no extra independences beyond those entailed by the graph), as well as adequate data.

Apply this rule to all relevant paths, including those opened by the way the sample was selected. Conditioning on an incident being reported can matter even when “reported” is absent from the regression.

Consider the complete small graph:

~~~text
Z → X → M → Y
Z → Y
X → S ← Y
S → D
~~~

There are three simple X-to-Y paths. X → M → Y carries the proposed causal mechanism; X ← Z → Y carries a common cause; X → S ← Y is blocked at S before conditioning. Conditioning on Z blocks the common-cause path and retains the causal path. Conditioning on M blocks that causal path. Conditioning on S, or its descendant D, opens the collider path. Inspecting only the fork would miss that selection effect.

For a total effect in an appropriate causal DAG, the back-door criterion provides one sufficient adjustment rule: choose measured covariates that are not descendants of X and block every path entering X through an arrowhead. This leaves the directed causal paths available. The resulting identification still relies on the model's causal interpretation, suitable data and support for the required comparisons. Failure of this sufficient criterion is not proof that the effect is unidentified. Use C.28 for the identification question rather than inventing an adjustment from one recognizable three-node shape.

The ordinary d-separation rule above applies to DAGs. If feedback matters, distinguish times: an outcome at t may affect workload at t+1. A finite time-unfolded model still needs its initial conditions and omitted influences justified. An equilibrium with simultaneous causal feedback needs an appropriate cyclic model, its solution conditions and its separation rule. Do not erase feedback merely to obtain an acyclic picture.

#### C.28.CM:4.5 - Derive a consequence that can distinguish the accounts

Work the same question through each retained model. Start with a direction, a possible or impossible outcome, a conditional independence, or an observation that one account can explain only by adding another premise. Show which relation makes the consequence follow.

Keep three operations distinct. Conditioning restricts attention using an observed value. Intervention replaces the specified mechanism. Omitting a variable from a report or marginalizing it out leaves its possible influence in the subject model. Treating all three as “fix the variable” can reverse the conclusion.

When the mechanisms are specified, C.28.MR derives an intervention consequence while retaining the relevant other mechanisms and underlying inputs. Use C.29 when expressing or computing the model requires further mathematical construction. If the needed function or input law is missing, return that precise gap along with any qualitative result that survives.

Two graphs may entail the same observed independences. Two mechanisms may produce the same measurements in the available range. Retain both when the present material does not distinguish them. A causal-discovery procedure can contribute within its declared model class and assumptions; its returned graph does not remove those conditions.

#### C.28.CM:4.6 - Challenge the consequence with available evidence

Compare the consequence with an observation, contrasting case, subject argument or feasible intervention that bears on it. First check that the observation concerns the modeled variable, cases and time. A contradiction can arise from the mechanism, measurement, implementation of a proposed action, or a changed operating condition.

Distinguish a contradicted implication, an untested implication and compatibility with the inspected material. A graph with no relevant testable implication cannot acquire support merely from an absence of contradiction. Conversely, failure to reject an implied independence does not establish the graph. Deterministic constraints, measurement error, missing cases and sampling uncertainty can all change the interpretation.

Revise only as far as the finding warrants. Preserve a valid observation when its causal interpretation fails. Restore a rival when its rejected premise changes. If an additional study could change the answer, C.28:4.8 helps specify the evidence question and C.11.DUA helps choose whether to obtain it. A useful model may end with an unresolved distinction.

#### C.28.CM:4.7 - Return the model with the use it can support

Give the recipient the question, the relevant mechanisms and alternatives, their source basis and assumptions, the derived consequence, and the uncertainty that changes its use. A short explanation can carry this result; no universal record form is required.

Recognition can stop at “these two accounts imply different responses”. Consequential reliance requires the corresponding subject and evidential grounds. C.28 qualifies causal support; a statistical estimate or bound requires its own identification and estimation result. A controlled direct effect is a different query from a total effect. A claim about the cause of one historical outcome or responsibility also needs its chosen concept and subject standard; a population effect does not settle it.

Return the next useful contribution by what it must establish: for example, whether a log reflects an actual omission, whether a controller reads a display, or whether an apparent AI effect survives comparable task selection. Temporary mitigation can remain available under its own evidence, costs and authority while the causal question is open.

### C.28.CM:5 - Archetypal Grounding

The following constructed cases demonstrate reasoning under stated premises. They do not report field effects.

#### C.28.CM:5.1 - Separate an omission, its record and the incident sample

Four incident tickets mention missing order identifiers after a reporting-template change. A planner asks whether supplying the identifier before import would remove manual matching. All four tickets came from problematic reports; the frequency among all reports is unknown.

Choose M for an actually missing identifier and Y for manual matching after import. X denotes template use and L high process load. One account proposes X → M → Y, with load affecting template deployment and identifier omission. A second account proposes that load produces both missing identifiers and an additional wrong join key K; K causes matching work even after the identifier is supplied. The second account has L → M and L → K → Y without an M → Y mechanism.

These accounts make different conditional predictions. If missing identifiers are the operative joining failure and supplying one changes no other input, supplying it removes that modeled obstacle. If K remains wrong, the same correction leaves the K-related work. A report with its identifier restored but the same failed join can challenge the first account's claim of sufficiency. It does not establish the second account merely by eliminating one rival.

Now recover the observing process. Let R be a log saying the identifier is missing. A logging defect can make R=1 while M=0. Inspecting the submitted report and the importer’s actual inputs can therefore resolve a recording question before further causal research is useful.

Let S=1 mean a report entered the incident sample, either because R=1 or because matching work was severe. The structure R → S ← Y means that analyzing only S=1 conditions on a collider. The four tickets cannot by themselves establish the population association or the effect of correcting identifiers. Obtain the needed comparison cases if they could change the decision; retaining a qualified unresolved answer is also possible.

The first return is specific: determine which joining inputs were actually missing or wrong, then distinguish the two modeled failure mechanisms. If all retained accounts support a cheap temporary manual check under the decision's own conditions, using it does not establish which account caused the incident.

**Onset, persistence and amplification.** Suppose a queue began during a specialist's absence. After their return, ten new items and capacity for ten items arrive each day. Under the simplified balance B(t+1)=max(0, B(t)+A(t)+R(t)−C(t)), with backlog B(0)=12, A=10, R=0 and C=10, the backlog remains 12. Two daily rework items, R=2, increase it by two per day. The absence explains the initial loss of service; the present flow balance explains persistence; rework explains growth under these premises. Restoring attendance alone need not clear the backlog. A different arrival pattern, capacity or feedback from delay to rework reopens the corresponding part of the model.

#### C.28.CM:5.2 - Construct the measurement and device mechanisms separately

An idealized regulated supply has command C=12 volts and a fixed 6-ohm resistive load. Its display reads D=14 volts. The practical question is whether correcting the display can reduce the load current.

Construct separate variables for delivered voltage V, display D and current I. Use the load relation I=V/6. Two accounts fit the displayed value:

| Account | Proposed mechanisms | Current implied by the account |
| --- | --- | --- |
| Display bias | V=C; D=V+2. | V=12 and I=2 amperes. |
| Supply offset | V=C+2; D=V. | V=14 and I=7/3 amperes. |

Setting the displayed number to 12 replaces the display mechanism in either model. It leaves V and I unchanged. Changing C to 6 instead gives V=6, I=1 in the first model and V=8, I=4/3 in the second, if the stated offsets and load relation remain valid. The observation D=14 alone does not choose between the accounts.

A separately qualified voltage or current observation can discriminate these idealized models. The need is a measurement of the physical quantity with a suitable independent basis, not another copy of the same display.

Change the situation: the displayed value is fed into an automatic controller for the next command. The earlier absence of a display-to-device path no longer applies over that horizon. Add D(t) → C(t+1) → V(t+1) and obtain the controller law before predicting the later current. The current instant and later controlled behavior are different questions. C.28.MR then performs the chosen replacement in the model actually constructed.

#### C.28.CM:5.3 - Separate AI assistance from assignment and selection

A team reports that AI-assisted tasks had a higher success rate. The question is the effect of actually using assistance A on success Y for the same eligible task population. Let D denote pre-existing task difficulty and H the worker's prior skill.

One model contains A → Y, D → A, D → Y, H → A and H → Y. The rival keeps the assignment and difficulty/skill relations but omits A → Y: the observed difference could arise through who used assistance and on which tasks. Success rates alone do not settle that difference.

The models permit different intervention consequences even when they fit the same aggregate report. Under the explicit assumption that D and H suffice to block common-cause paths, with comparable treatment versions and adequate overlap, adjustment might identify the chosen effect. Those conditions are additional premises, not results of drawing D and H. If workers choose assistance using an unmeasured expectation of difficulty, preserve that possible influence and return the identification gap.

Suppose inclusion in the showcase S depends on both use of assistance and success. A → S ← Y adds a selection path; conditioning on showcased tasks opens it. Reconstruct the eligible set and inclusion process before using the selected comparison for the population question.

Now randomize an offer Z while leaving actual use A voluntary. The offer's effect is a different estimand from the effect of A. If the offer also teaches a technique used without the AI, Z has a route to Y outside A. Using the offer as an instrument to learn the effect of actual use would require it to affect success only through use, among other assumptions. The additional route violates that requirement. The model returns the exact identification question and keeps observed performance descriptive until the required result is available.

The useful return can be a revised comparison population, a retained unmeasured cause, or a direct-effect route that invalidates a proposed design. A larger benchmark or more detailed simulation does not resolve those missing premises by itself.

### C.28.CM:6 - Bias-Annotation

The scope is construction for a bounded causal question. Epistemic discipline separates a mechanism proposal from its evidence; pragmatic discipline stops at a useful conditional result; ontological discipline separates variables, their values, observations and the subject being changed.

Narrative closure favors the first fluent explanation. Diagram authority favors a tidy graph. Observed-variable bias omits causes that were not measured. Remedy these tendencies by constructing a material rival, explaining consequential omissions, and checking how observations and case selection were produced. Retaining every imaginable model can also prevent useful work; narrow the family by subject grounds and the receiving question.

### C.28.CM:7 - Conformance Checklist

- The outcome, cases, time and required contrast can be recovered.
- Each consequential variable and relation has a subject meaning; registration and selection are explicit when they change the answer.
- Important included and excluded influences have stated grounds or remain assumptions.
- Material alternatives receive comparable questions, including coexisting causes where relevant.
- The graph or equation class supports the rule used; DAG path inspection covers all relevant paths and conditioning, including selection.
- A consequence follows from named premises, or the missing premise is returned precisely.
- Compatibility, contradiction and absent discrimination retain different meanings.
- The returned use distinguishes recognition, model consequence, evidential support and action choice.

### C.28.CM:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| “We drew the intermediate cause, so the mechanism is established.” | Recover what supports the intermediate relation and what the rival predicts. |
| “The common cause explains everything, so there is no direct effect.” | Inspect the proposed direct path separately; both mechanisms may operate. |
| “This variable is always a confounder.” | Name the question and path before deciding its role or adjustment use. |
| “All reports in our incident set show the effect.” | Recover registration and selection, then the comparison needed for the target cases. |
| “The graph fits, so it is the true graph.” | Name the implication actually tested and retain indistinguishable alternatives. |
| “Remove the original cause and the ongoing problem ends.” | Reconstruct the present persistence mechanism and horizon. |
| “A better model must precede any response.” | Compare the value of further discrimination with an independently justified available response. |

### C.28.CM:9 - Consequences

The practitioner obtains explicit alternatives, a usable conditional consequence and a concrete return when a premise is missing. This can prevent spending effort on an intervention that changes only a record or on a study that cannot distinguish the live accounts.

The cost is recovering mechanisms, meaningful variables and competing assumptions. Limit that cost to distinctions that can change the question's answer or a consequential use. Some questions remain unidentified or underdetermined; a clearer statement of that limit is a useful result.

### C.28.CM:10 - Rationale

Constructing a causal account and judging its support answer different questions. A coherent hypothetical model can expose a decisive experiment or invalidate an inference without establishing that the model describes the subject. Preserving both the constructive and evidential questions makes that intermediate result usable.

A model family preserves a live disagreement when the available grounds do not select one account. Explicit measurement and selection processes prevent uncertainty about observing from disappearing into a confident story about the subject. Time distinctions make the same discipline usable when an initiating event and an ongoing mechanism differ.

### C.28.CM:11 - SoTA-Echoing

The comparison concerns usable construction and criticism for a bounded causal question. It does not rank causal-discovery algorithms or claim a universally best empirical workflow.

| Practice question and selected move | Alternative, trade-off and concrete use | Source role, limits and reopening |
| --- | --- | --- |
| How can a working account become explicit causal assumptions? **Adapt** extraction, translation and critical integration of subject claims. | Directly drawing the preferred story is cheaper but can hide missing or conflicting premises. :4.2–4.3 recover meanings and alternatives; a full evidence synthesis is reserved for questions that need it. | [Ferguson et al., 2020, Table 1 and Discussion](https://pdfs.semanticscholar.org/cb52/45fd90f7942f734911ebd1492c3d3e5a4e24.pdf) supplies a developed construction comparator. Its integration heuristics do not establish causal truth. Reopen when this extraction loses a subject mechanism or a simpler adequate construction is available. |
| Which conditioning changes the causal question or opens a misleading path? **Adopt** whole-graph path inspection; **reject** deciding from a variable's name or one three-node picture. | Classifying a few familiar motifs is quicker but can miss another open path or conditioning through selection. :4.4 works the entire small graph and :5.3 preserves assignment and selection. | [Geiger, Verma and Pearl, 1990](https://ftp.cs.ucla.edu/pub/stat_ser/r116.pdf) gives the formal separation basis; [Cinelli, Forney and Pearl, 2022](https://ftp.cs.ucla.edu/pub/stat_ser/r493-reprint.pdf) supplies the current practice comparison for controls. These are conditional graphical results, not tests of omitted subject premises. Change the rule when the graph class or estimand changes. |
| What if the graph itself is uncertain? **Adapt** comparison of the causal query over admissible structures. | Selecting one convenient graph simplifies calculation but can suppress a result-changing rival. :4.5 retains the remaining family and states its shared or differing consequences. | [Padh et al., 2025, §§2 and 6](https://arxiv.org/html/2502.17030v2) supplies a computational line with explicit structural uncertainty; its procedure assumes no hidden confounding and has optimization limitations. [Peters et al., 2014](https://jmlr.org/papers/volume15/peters14a/peters14a.pdf) shows how additional model assumptions can identify structure. Neither licenses assumption-free discovery. Reopen when a qualified result excludes a live rival or reveals another. |
| How should feedback affect construction? **Adopt** temporal distinction where it answers the query; otherwise request a suitable cyclic model. | Forcing an equilibrium loop into a DAG can delete the operative mechanism. :4.4 and :5.2 retain the horizon and the controller dependency. | [Bongers et al., 2021](https://staff.fnwi.uva.nl/j.m.mooij/articles/21-AOS2064.pdf) supplies existence and interpretation conditions for cyclic structural models. Its theory makes a cyclic alternative available under conditions, not automatically solvable. Reopen when the chosen temporal resolution or equilibrium premise changes. |
| Is specialized construction needed at all? **Retain** direct use of sufficient general modeling or a supplied mechanism model. | B.5.FM can construct the thermal limiting argument without a causal-model family; C.28.MR can transform supplied equations directly. This pattern adds work only when the causal account or a material alternative is missing. | These internal alternatives determine :1 and :4.7. In :5.2 the additional work distinguishes supply, display and feedback before choosing a transformation. The examples establish conditional reasoning, not superior field performance. Prefer the simpler route when it supplies that distinction already. |

### C.28.CM:12 - Relations

- **B.5.FM** constructs a general first model; this method develops the missing causal relations and returns their conditional consequences.
- **B.5.2** generates and compares hypotheses. Causal-model construction can change their plausibility grounds or expose an unresolved rival.
- **C.16** qualifies measurement and registration; **C.27** qualifies temporal claims when those questions are needed.
- **C.28** governs causal-use support, identification and evidence questions; **C.28.MR** derives a consequence of changing specified mechanisms.
- **C.29** supplies needed mathematical representation and computation.
- **C.11.DUA** compares worthwhile inquiry with available action; **A.15.9** obtains a missing contribution from another practice.

### C.28.CM:End
