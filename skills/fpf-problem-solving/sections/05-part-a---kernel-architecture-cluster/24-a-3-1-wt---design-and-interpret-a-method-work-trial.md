## A.3.1.WT - Design and Interpret a Method Work Trial

> **Type:** Method pattern
> **Status:** Stable

> **Primary working result:** occurrence-level trial evidence and explicit missing-evidence positions for the separate A.3.1.CC coherence, A.3.1.FT fit or transfer, and C.11.MV practical-worth decisions. A candidate Method account remains a candidate; only independently admitted Work is reported as having occurred, and only independently admitted Methods as having been enacted.

### A.3.1.WT:0 - Use This When

Use this pattern when a Method or candidate Method account is ready for a trial in actual Work and the next decisions need observations from named situations rather than another plan, demonstration, or document review. Begin with one trial question: what must be learned from actual Work for a later coherence, fit, transfer, or worth decision?

The first useful result is a trial-slice row. It names the subject and its status, the situation-selection reason, the planned task, the Work that actually occurred, actual performers and enacted admitted Methods, relied-on Systems and capabilities, observations, gaps, and the later decision that may use them. A row that returns `missing-performed-work` is useful when the trial remains only planned.

Here *trial* is Plain practice wording for intentionally selected Work and observation. It is not a new subtype of `U.Work`, a Method admission, an evaluation result, or a claim that the situation statistically represents a population.

Do not use this pattern to declare description coherence, situational fit, transfer, practical worth, capability, causal contribution, or general effectiveness. A.3.1.WT makes later judgments possible; A.3.1.CC, A.3.1.FT, and C.11.MV make those judgments under their own questions and evidence.

#### A.3.1.WT:0.1 - Working Distinctions

| Item | Working meaning here | Boundary |
| --- | --- | --- |
| trial question | One evidence question whose answer can change a named later decision. | “Try the method” is not yet a bounded question. |
| representative situation | A situation selected because stated characteristics match the named current-use question. | The word does not imply random sampling, population coverage, or transfer. |
| discriminating situation | A situation selected because one changed condition can expose a claimed limit, burden, or failure. | Difference alone is insufficient; state which claim the changed condition can test. |
| WorkPlan | Intended performers, tasks, Methods, situations, observations, and stops. | A plan, script, simulation description, or scheduled demonstration is not performed Work. |
| admitted Work | One dated Work occurrence admitted under `A.15.1` from its actual performers, action history, enacted Method, temporal extent, and required containing-System relation. | A report, trace, attendance record, or output can support the claim but does not create the occurrence. |
| candidate-account trial branch | Actual Work is admitted separately while claims in a candidate Method account are compared with observations. | The candidate whole is not said to have been enacted. Only separately admitted constituent Methods may obtain in `enactsMethod` relations. |
| capability input | A claim about a holder System, Work family or result class, operating envelope, measures, qualification or currentness window, and evidence used for reliance. | Training, availability, assignment, permission, authority, or one success does not substitute for it. |
| trial evidence | Occurrence-level observations, source relations, burdens, adaptations, results, and gaps qualified for named later uses. | It is not itself coherence, fit, transfer, worth, contribution, or causal proof. |

### A.3.1.WT:1 - Problem Frame

Method trials are often easiest to describe after the fact: a team used some material, produced a result, and reported value. That compression hides what Method was admitted, which Work occurred, who performed it, which support conditions were present, what changed, and which conclusions the observations can support.

Convenient success cases also miss the situations that matter most. A Method may look usable in a familiar task and fail when feedback is closed-loop, information is incomplete, capability is stale, or a required relation is absent. Representative and discriminating situations therefore serve different purposes and must be selected for an explicit later question.

### A.3.1.WT:2 - Problem

A planned trial can be reported as performed Work. A candidate whole can be reported as enacted because some constituent activities occurred. Training completion can be reported as capability, tool logs as Work, immediate self-reports as lasting results, and one favourable occurrence as evidence of transfer or effectiveness.

These moves produce a positive story but weak evidence. Later reviewers cannot recover the actual occurrence, compare situations, separate Method claims from support conditions, or find the missing evidence that should stop a broader judgment.

### A.3.1.WT:3 - Forces

| Force | Tension |
| --- | --- |
| Real Work | Natural Work exposes practical burdens, while uncontrolled conditions complicate attribution. |
| Deliberate discrimination | Changed conditions can reveal a limit, while an artificial stress case may not answer the current-use question. |
| Status preservation | Candidate claims need testing, while useful Work must not be reported as enactment of an unidentified Method whole. |
| Observability | Later decisions need traceable observations, while instrumentation and reporting can burden or distort Work. |
| Capability | Performer ability can change the result, while training or one success invites premature capability claims. |
| Failure value | Failure can localize a correction, while teams and sponsors are biased toward a favourable trial narrative. |
| Evidence reach | Several occurrences can strengthen a local account, while they still may not establish contribution, causality, transfer, or practical worth. |

### A.3.1.WT:4 - Solution

A.15.1 identifies performed Work and A.10 governs a claimed evidence use. The trial construction below determines which Work, variation, observation and stopping condition can answer the unresolved Method question. Its result is distinct from coherence, transfer and comparative worth; reuse a matching existing observation before commissioning a trial.

Select situations from the later evidence questions, arrange and observe actual Work, preserve every subject's status, and return occurrence-level evidence with explicit gaps and limits on the conclusions it supports.

#### A.3.1.WT:4.1 - Pattern-Use Unfolding

1. **Name the later decisions and trial questions.** Separate the questions that may feed A.3.1.CC coherence, A.3.1.FT situational fit or transfer, and C.11.MV practical worth. Do not hide several conclusions inside “does the Method work?”.
2. **Preserve the subject branch.** Identify the admitted Method under `A.3.1`, or keep the proposed whole as a candidate account. In the candidate branch, state which candidate claims are being compared and which constituent Methods, if any, are separately admitted and may be enacted.
3. **Select one representative situation.** Name the intended-use characteristics that matter to the question: task purpose, development phase, technical or domain conditions, performer population, holder capabilities, participating Systems, direct relations, constraints, and qualification window. State why this situation covers the current question without claiming population representativeness.
4. **Select a discriminating situation when the decision needs one.** Change or seek one condition whose outcome can show whether a live claim holds in that situation: unfamiliar technical coupling, another domain, missing support relation, changed capability envelope, stale material, or another named alternative. State the claim that could fail. Do not require every trial to contain an artificial stress case.
5. **Write the WorkPlan without backdating Work.** State intended tasks, performers, admitted Methods, support conditions, observation points, protected conditions, burdens to record, stop rules, and the later use of each observation. Keep simulation and demonstration as planned or separately typed activities unless independently admitted Work occurs.
6. **Check capability and support inputs separately.** When reliance on capability changes interpretation, identify the holder System, Work family or result class, operating envelope, measures, qualification or currentness condition, and evidence. Recover only A.15.8.MS material, access, tool, provider, feedback, and decision conditions supported for the relevant task rows; preserve retained candidates, split boundaries, untested conditions, and gaps rather than treating them as configured inputs.
7. **Admit only Work that occurred.** For each occurrence, recover every actual performer System and its A.13 basis, the action history, at least one admitted Method actually followed, temporal extent, and required containing-System relation under `A.15.1`. Add assignment attribution, System use, operation binding, affected referent, resource use, or result relations only when their own predicates obtain.
8. **Record conditions and departures.** For each Work occurrence, record the situation, relied-on Systems and direct relations, holder capabilities used in interpretation, deviations from the WorkPlan, adaptations, burdens, stops, domain results, and observations. Keep the domain result, report, log, and evidence-use relation separate from Work.
9. **Qualify the evidence reach.** Distinguish direct observation, participant report, source interpretation, observed association, contribution claim, and causal claim. Return the strongest supported level and name missing comparison, temporal, capability, relation, or alternative evidence.
10. **Return evidence by later use.** Send contradicted description or relation claims to A.3.1.CC, situation comparisons and an unlike-situation result to A.3.1.FT, and results, burdens, alternatives, side effects, and evidence limits to C.11.MV. Return `missing-performed-work`, `missing-method-admission`, `missing-capability-basis`, `missing-direct-relation`, or the named missing premise when a required condition is absent.

#### A.3.1.WT:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| trial use | Later decision, bounded trial question, qualification window, and stop. |
| subject status | Admitted Method, or candidate account plus each separately admitted constituent Method whose enactment is claimed. |
| situations | Representative and any discriminating situation, selection criteria, matched conditions, changed conditions, and claim each can test. |
| plan baseline | Intended Work, performers, Methods, support conditions, observations, burdens, protected conditions, and stop rules. |
| actual Work | Each admitted Work occurrence, actual performers, enacted admitted Methods, temporal extent, containing System, and deviations from plan. |
| relied-on conditions | Holder capabilities, Systems, Agent-performed Work, direct relations, access, assignments, permissions, authority, tools, providers, and support conditions that actually obtain or remain missing. |
| observations | Domain results, burdens, adaptations, failures, participant reports, direct observations, and their source or evidence-use relations. |
| reach and gaps | Supported observation level, unsupported contribution or causal overreads, missing evidence, and conditions that would reopen the slice. |
| return | Occurrence-level evidence routed separately to A.3.1.CC, A.3.1.FT, and C.11.MV, or a supported lower result. |

#### A.3.1.WT:4.3 - What Changes in Practice

Teams stop calling a scheduled exercise or positive report “the trial”. They can point to the actual Work, the admitted Method that was enacted, the conditions on which the result depended, and the named later question each observation can answer.

A failed or incomplete occurrence remains useful. It can expose a description defect, a representation difficulty, a missing support relation, a capability condition, or a situation boundary without being inflated into a universal verdict on the Method.

#### A.3.1.WT:4.4 - Minimal Constructed Trial Replay

The following is a constructed teaching replay, not field evidence. It shows the smallest result that lets later checks reuse the same Work without turning the trial into their conclusion.

`M-Unit-Review-1` is admitted for reviewing temperature-sensor calibration reports before release. Its current description tells the reviewer to identify every source unit, normalize values, compare them with the declared tolerance, and stop on an unresolved mismatch. `WP-ME11-1` plans two review tasks for the same week. `S-Rep-1` is a current same-unit report of the ordinary kind. `S-Disc-1` keeps the product, decision, reviewer, description, and support fixed but introduces a Celsius/Kelvin mismatch; it is selected because the live claim is that the Method lets this reviewer expose a unit mismatch before release.

The interpretation relies on `CAP-R17-1`: holder `Reviewer-17`; calibration-report-review Work family; temperature-sensor-report envelope; measure “four of four seeded unit cases detected with description edition 4”; current through day D30; qualification record `QR-R17-1`. The qualification, assignment, permission to inspect the report, and release authority remain different facts. The trial also records description edition 4 and the manually retrieved conversion table as A.15.8.MS support inputs.

Two occurrences then happen and are admitted separately. `W-Rep-1` is performed by `Reviewer-17` inside `Calibration-Team-A` from 10:03 to 10:10, enacts `M-Unit-Review-1`, accepts the same-unit report, and records seven minutes of review burden. `W-Disc-1` is performed by the same System in the same containing System from 11:14 to 11:26, enacts the same admitted Method, normalizes the Celsius/Kelvin values before comparison, detects an unresolved mismatch, stops the release decision, and returns the report for correction; it records twelve minutes and one conversion-table lookup. The WorkPlan, two Work occurrences, domain decisions, timing record, and observation account remain separate.

| Later use | Evidence returned | Stop retained |
| --- | --- | --- |
| A.3.1.CC coherence | The two occurrences identify the description edition and the operations actually followed; neither exposed an internal contradiction in this slice. | A.3.1.WT does not conclude that the whole MethodDescription or Method construction is coherent. |
| A.3.1.FT fit or transfer | The matched pair records one changed situation condition and the resulting task observations for one current holder. | One discriminating occurrence establishes no transfer to another holder, domain, tool, or qualification window. |
| C.11.MV practical worth | The domain decisions, seven- and twelve-minute burdens, lookup, and stop are available for comparison with named alternatives. | A task pass establishes neither net worth nor causal contribution. |

If `W-Disc-1` had not occurred, return `missing-performed-work`; if its enacted-Method relation or relied-on capability basis were absent, return that missing premise. A favourable plan, simulated trace, or qualification record cannot replace the occurrence.

### A.3.1.WT:5 - Archetypal Grounding - SSFD Workplace Projects

The automotive SSFD programme supplies reports and review evidence about actual workplace projects without supplying a universal effectiveness claim. More than 300 engineers participated in a three-year transfer programme; training was followed by supported four-to-six-month workplace projects. Seventy-two of the first 100 reviewed project reports recorded SSFD use, and 41 contained enough detail for deeper analysis. Across those 41, the study reports 95 examples of evidenced individual benefits while distinguishing direct and indirect contribution.

The published paper supplies report evidence. A local application admits a particular project Work occurrence only from the records required by §4.1(7); otherwise retain the report and name the missing occurrence or performer basis. The slices below distinguish possible answers to the later questions without admitting Work by citation.

#### A.3.1.WT:5.1 - Preserve the Status Branch

Before using the replay, establish whether SSFD is an admitted Method for the current FPF use. If it is, each supported project occurrence may be tested for its own obtaining `enactsMethod` relation. If it is not, admit the workplace Work independently, retain the SSFD account as a candidate, and name only separately admitted constituent Methods as enacted. The report statement “used SSFD” does not perform either admission automatically.

#### A.3.1.WT:5.2 - Representative and Discriminating Slices

| Slice | Reported project facts used | Evidence returned | Stop retained |
| --- | --- | --- | --- |
| Project 11 | The report concerns functional analysis of a new by-wire steering system and records 48 failure modes for four system functions, 44 new requirements and design rules, 44 test cases for individual systems, and 33 requirements and test cases for the overall system. | One bounded application account for checking whether description, representation, and support claims were usable in that project situation, plus the reported results and burdens available from the source. | Do not infer that this project caused or preceded Project 32, that every programme participant had the same capability, or that the reported benefits came from SSFD alone. |
| Project 32 | The report exposes difficulty representing the relation between a closed-loop sensor and controller. | A discriminating representation difficulty for A.3.1.CC and an unlike-situation comparison for A.3.1.FT. A.3.1.CC uses C.37 and the direct representation governor for one action; when several unlike Method-related actions are current, it checks the affected action and cross-use dependency in the complete C.37.MP profile defined in C.37.MP:4.2. The report establishes neither selection result by itself. | Do not turn the difficulty into general Method failure or claim that Project 11 supplies the counterfactual. |
| 41-report evidence set | The review identifies 95 examples of evidenced individual benefits across business results, process improvement, and product-development-team capability improvement, while separating direct and indirect contribution. | Bounded report and review evidence for later comparison of results, burdens, and evidence strength in C.11.MV. | Counts and source classifications do not establish causality, universal superiority, transfer, or current capability for every participant. |

The useful A.3.1.WT result is therefore not “SSFD works”. It is a set of reported workplace-project accounts, situation and support conditions, observed representation difficulties, reported results and burdens, evidence-source qualifications, and explicit gaps for three separate later judgments.

#### A.3.1.WT:5.3 - EC-417 Early Stop

The [full EC-417 application](https://github.com/ailev/FPF/blob/main/FPF-Spec.md#fpfreference169---choose-the-smallest-method-development-result-needed-for-release-ec-417) supplies the receiving problem, alternatives, calculations and the distinct limits used below.

In `EC-417`, the three-release statement remains a WorkPlan. The three named-user retrieval, tailoring, and selection-support occurrences from A.15.8.MS establish only those support tasks; they do not perform a release or enact the candidate whole `C-EC-Release-v2`.

For a release trial, apply §4.1(6–9) to the release's own occurrence, support, evidence and authority facts. The observed support tasks do not supply that release Work; until its basis is recovered, return `missing-performed-work`. Even after a release is admitted, keep `C-EC-Release-v2` as a candidate and send the occurrence evidence separately to A.3.1.CC, A.3.1.FT, C.11.MV.

### A.3.1.WT:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| plan-completion bias | A scheduled or demonstrated task is recorded as trial Work. | Admit each actual Work occurrence separately; otherwise return `missing-performed-work`. |
| candidate-laundering bias | Constituent activity is reported as enactment of the candidate whole. | Preserve the candidate account and name only separately admitted enacted Methods. |
| success-selection bias | Convenient positive occurrences stand in for the intended situation family. | State representative criteria and add a discriminating situation when the later question needs one. |
| instrument bias | Logs, reports, or telemetry are treated as the Work or result. | Keep the occurrence, result, record, and evidence-use relation separate. |
| capability inflation | Training or one success becomes a holder capability claim. | Require the A.2.2 holder, Work family, envelope, measures, window, and evidence. |
| causal inflation | Reported benefit or association becomes Method-caused effect. | State the observation level and missing comparison or causal basis. |
| trial-judgment collapse | One trial record decides coherence, fit, transfer, and worth at once. | Route evidence to A.3.1.CC, A.3.1.FT, and C.11.MV as separate receiving uses. |

### A.3.1.WT:7 - Conformance Checklist

- [ ] One later decision and bounded trial question are stated before the trial design.
- [ ] The Method is admitted, or the proposed whole remains a candidate account throughout.
- [ ] Every claimed enacted Method is independently admitted; no candidate whole is said to be enacted.
- [ ] Representative criteria are named, and every discriminating situation states the claim it can distinguish.
- [ ] WorkPlan, demonstration, simulation, report, trace, result, and actual Work remain separate.
- [ ] Each claimed Work occurrence independently satisfies the admission basis in §4.1(7).
- [ ] Capability, System use, assignment, permission, authority, support, operation binding, and result relations are asserted only from their own bases.
- [ ] Conditions, deviations, adaptations, burdens, observations, and domain results are recorded per occurrence.
- [ ] Direct observation, self-report, association, contribution, and causality are not merged.
- [ ] The result routes evidence and gaps separately to A.3.1.CC, A.3.1.FT, and C.11.MV and claims none of their judgments.

### A.3.1.WT:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “The rehearsal ran, so the Method was trialled.” | Recover actual Work and its enacted admitted Method; otherwise keep the rehearsal at its supported status. |
| “The team enacted the candidate Method.” | Admit the Work, preserve the candidate account, and name only admitted constituent Methods whose enactment relations obtain. |
| “Everyone was trained, so capability was controlled.” | Record training separately and recover the holder capability input actually used in interpretation. |
| “The log proves the task occurred and succeeded.” | Use the log as evidence for independently admitted Work and a separately established task result. |
| “Most reports were favourable, so the Method transfers.” | Send the occurrence evidence and situation differences to A.3.1.FT; do not make the transfer judgment here. |
| “Reported benefit proves the Method caused the outcome.” | Record the report and its contribution category, then return the missing causal basis. |

### A.3.1.WT:9 - Consequences

Trial Work produces inspectable evidence. Failures and missing premises survive as useful results, and later assurance decisions can compare the same occurrences without changing their identity or truth status.

The cost is more explicit occurrence recovery and narrower conclusions. Projects must record performer, Method, situation, capability, support, direct relations, burdens, and source limits, and they may finish a costly trial with a precise gap instead of a favourable verdict.

### A.3.1.WT:10 - Rationale

Actual Work is the shared empirical base, but coherence, fit, transfer, worth, capability, contribution, and causality are different claims. Keeping them separate lets the same occurrence inform several decisions without allowing one decision to inherit another's conclusion.

Representative and discriminating situations are paired because typical-use evidence and boundary-finding evidence answer different questions. Their selection is decision-relative; it does not create statistical representativeness or a universal situation taxonomy.

### A.3.1.WT:11 - SoTA-Echoing

| Source | Adopted or adapted contribution | Boundary and practitioner implication |
| --- | --- | --- |
| Yildirim, Campean, and Uddin, [function-modeling evaluation in industry practice](https://doi.org/10.1017/dsj.2026.10056) | Adopt workplace projects, varied application situations, reported limitations, later report analysis, and separation of direct and indirect contribution as trial-design and evidence-recording cues. | One automotive OEM, SSFD used within a broader methodology, and retrospective reports establish neither SSFD-only causality nor universal transfer. |
| Tsai, Zdravkovic, and Söder, [DBE-design Method action research](https://doi.org/10.1007/s10270-022-01068-z) | Adopt repeated plan-perform-evaluate cycles in an operating health-services ecosystem as an unlike-domain replay of actual validation actions. | The evaluation is ex ante and case-specific; it establishes neither long-term effect nor transfer to the other elicited domains. |
| Faludi, Yiu, and Agogino, [empirical tests of sustainable-design Methods](https://doi.org/10.1017/dsj.2020.17) | Adopt explicit alternative Methods, several industry situations, participant Work, activities, and immediate value reports as a bounded comparison input. | Immediate self-report establishes neither long-term product results, causal superiority, nor the effectiveness of recombined variants. |
| Current FPF `A.3.1`, `A.15.1`, `A.2.2`, and `A.10` | Adopt independent Method admission, Work occurrence admission, capability qualification, and evidence-use relations. | A.3.1.WT contributes the practitioner move for situation selection and occurrence-level trial evidence; it does not redefine those claims or make the downstream judgments. |

Reopen the pattern when practitioners cannot select a discriminating situation without a universal trial taxonomy, when actual Work cannot be distinguished from demonstrations or records, when the candidate branch repeatedly loses status, or when current field evidence supports a stronger trial-selection move without broadening the later judgments.

### A.3.1.WT:12 - Relations

- B.1.5.CM supplies an admitted Method or a status-preserved candidate account and may supply a realization or trial plan; it does not supply performed Work.
- A.3.2.DE supplies MethodDescription content or candidate-account content for the trial question. A.15.8.MS supplies supported material and task conditions or a retained configuration set, split boundary, or gap; A.3.1.WT consumes only the obtaining support inputs and preserves every unresolved status. Neither pattern establishes trial Work or its result.
- RMP.10 may supply a reconstructed candidate account and a trial question while preserving the candidate branch.
- `A.3.1` governs Method admission; `A.15.2` keeps the WorkPlan separate; `A.15.1` governs each Work occurrence; `A.2.2` governs capability inputs; `A.10` governs relied-on evidence paths.
- A.3.1.CC consumes evidence for construction and description coherence, A.3.1.FT consumes situation comparisons for fit or transfer, and C.11.MV consumes results, burdens, alternatives, and evidence strength for practical worth. None of those conclusions is returned by A.3.1.WT.

### A.3.1.WT:End
