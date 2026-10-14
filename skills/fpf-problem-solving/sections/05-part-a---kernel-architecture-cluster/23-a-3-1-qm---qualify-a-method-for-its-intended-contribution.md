## A.3.1.QM - Qualify a Method for Its Intended Contribution

> **Type:** Method pattern
> **Status:** Stable

> **Primary working result:** one **status-preserving individual qualification** for each selected Method or candidate Method account, plus only those local input/result, schema-correspondence, or adapter-feasibility claims that can be judged without choosing a whole architecture.

### A.3.1.QM:0 - Use This When

Use this pattern when a project has one or more Methods identified under `A.3.1`, candidate Method accounts, and situational criteria, but it still does not know which subjects are individually usable for the bounded result. Use it before a several-structure comparison when a weak subject can be rejected cheaply on its own.

Begin with one Method or candidate account, its status, the contribution it is expected to make, and the criteria that matter for that contribution. Keep whole-level allocation, synchronization, composition, and compatibility questions outside the individual result.

The first useful result says one of the following: an identified Method is qualified or not qualified for the bounded use; a candidate account is retained or excluded while its Method-identification question remains open; or a local connection claim is supported, unsupported, or unresolved independently of a whole synthesis.

Do not use qualification wording to admit a candidate account as a Method, to establish compatibility or parthood, or to declare a Method architecture fit.

#### A.3.1.QM:0.1 - Working Distinctions

| Name used here | Meaning |
| --- | --- |
| identified Method subject | A Method already identified under `A.3.1`; A.3.1.QM judges bounded use without repeating identity. |
| candidate-account subject | An episteme about a possible Method whose unresolved identity conditions remain visible throughout qualification. |
| individual contribution | The result or preserved condition attributable to this subject under the stated use, not the success of a whole arrangement. |
| local connection | An input/result, schema-correspondence, or adapter-feasibility claim whose truth does not depend on choosing one whole synthesis. |
| individual qualification | A bounded result covering contribution, applicability, inputs/results, attributable time or burden, capability, support, authority/access, evidence, source limits, and stop. |
| architecture question | A claim about combined allocation, timing, composition, Work overlap, provider arrangement, authority distribution, or another several-structure relation. It belongs to C.32.MWA.PP when live. |

### A.3.1.QM:1 - Problem Frame

Method-selection literature correctly emphasizes situation and fit, but real project candidates arrive at unlike epistemic states. One is an identified Method with known use evidence, another is a candidate account recovered from Work records, and a third phrase refers only to a tool or support condition.

Individual qualification can save architecture effort by rejecting a candidate that cannot produce the required result or cannot meet one non-negotiable condition. It becomes misleading when it averages several Methods and support arrangements into one fit score or upgrades an account through confident language.

### A.3.1.QM:2 - Problem

Three errors recur. First, a retained candidate account is called a qualified Method. Second, one independently feasible schema mapping is called compatibility of the whole package. Third, a combined peak-load or authority conflict is hidden inside separate “passes” for each Method.

The project then believes the architecture problem is solved even though no result states how the individually plausible subjects work together.

### A.3.1.QM:3 - Forces

| Force | Tension |
| --- | --- |
| Cheap rejection | Individual defects should stop early, while whole conflicts must remain visible for C.32.MWA.PP. |
| Status preservation | Candidate accounts need useful assessment, while qualification cannot identify their Methods. |
| Comparable questions | A common set of questions aids choice, while not every question applies to every subject. |
| Evidence proportionality | A bounded use may need little evidence, while safety, authority, or high burden can require stronger support. |
| Local connections | A schema or adapter can be tested independently, while its placement and maintenance belong to a whole synthesis. |

### A.3.1.QM:4 - Solution

A.3.1 decides Method identity. This Method uses that result, or an explicitly unresolved candidate, to qualify one contribution for a receiving use. It does not repeat Method admission or infer the adequacy of a combined arrangement from the qualification of its participants.

Qualify one subject at a time against the bounded receiving use. Preserve status, expose unsupported conditions, and route only genuinely combined questions to C.32.MWA.PP.

#### A.3.1.QM:4.1 - Pattern-Use Unfolding

1. **State the subject and status.** Name the identified Method or candidate account and cite the identity or account basis already available. Reject unlike support facts as qualification subjects.
2. **Bind the use.** State the receiving Work or result, situation family, scope, time window, non-negotiable criteria, acceptable variation, and decision that will consume the qualification.
3. **Recover the individual contribution.** Name the input, result or preserved condition, procedure or invariant as far as known, applicability, and important source meaning. Do not credit the subject with another Method's result.
4. **Check attributable conditions.** Inspect timing and burden attributable to this subject; performer capability; support and provider access; authority or responsibility; evidence; and source or transfer limits.
5. **Test local connections only.** Check an input/result handoff, schema correspondence, or adapter feasibility when it can be supported independently. Record its scope and failure case.
6. **Return the truthful branch.** An identified Method is qualified or not qualified for the bounded use. A candidate account is retained or excluded *as an account*, with unresolved identification conditions unchanged. A local connection is supported, unsupported, or unresolved.
7. **Choose the stop.** Stop after one usable Method, one retained account, or several independently usable subjects when no whole question remains. Enter C.32.MWA.PP only when a several-structure choice can change the decision.

#### A.3.1.QM:4.2 - Record the Result

| Result position | Required content |
| --- | --- |
| subject and status | Method identity or candidate-account reference and the status that remains after qualification. |
| bounded use | Receiving result or Work, situation, scope, window, criteria, and consuming decision. |
| contribution | Inputs, result or preserved condition, known procedure/invariant, applicability, and variation. |
| attributable conditions | Time/burden, capability, support/provider access, authority/responsibility, evidence, and source limits attributable to this subject. |
| local connections | Independently tested input/result, schema, or adapter claims with scope and status. |
| verdict and stop | Qualified/not-qualified Method or retained/excluded account, open identity conditions, remaining whole question, and next action. |

#### A.3.1.QM:4.3 - What Changes in Practice

Teams stop scoring a methodology bundle as one object. They can reject one Method, retain a promising account without admitting it, and prove one schema mapping without calling the whole arrangement compatible. C.32.MWA.PP then receives only the genuinely combined timing, allocation, support, authority, or composition questions.

### A.3.1.QM:5 - Archetypal Grounding — EC-417 Individual Stops

The EC-417 dossier supplies four identified Methods and several candidate accounts. The bounded use is a safety-relevant release arrangement in which signed evidence must exist before safety closure, confidential supplier geometry must stay outside the AI provider, and decision Work remains with admitted human Systems under separate covering assignments and permission or direct decision-authority relations.

| Subject and prior status | Individual result | A.3.1.QM return |
| --- | --- | --- |
| `M-HW-Verify`, identified Method | accepts the affected change and pinout version; produces a verification result with named rig and hardware capability conditions | qualified for the bounded use |
| `M-SW-Integrate`, identified Method | accepts explicitly versioned provisional or signed pinout evidence; its integration record preserves the exact edition, any provisional uncertainty, and the edition actually used; later signed evidence supersedes a provisional edition only for safety-closure reliance while the earlier use and provisional-to-signed relation remain traceable; software remains reversible until `D-1` | qualified under the evidence-version, history, closure-reliance, and reversibility conditions |
| `M-Supplier-Approve`, identified Method | produces signed supplier approval or the explicit missing-approval stop; requires supplier-configuration responsibility and evidence access | qualified under the named access and responsibility conditions |
| `M-Release-Authorize`, identified Method | consumes the safety result and named evidence conditions; admitted human System `ReleaseDecider-17` performs `W-ReleaseDecision-17` under covering assignment `ASG-ReleaseDecision-17` and independently supported direct relation `AUTH-ReleaseDecision-17`; returns release, withhold, or next-slot authorization | qualified for the bounded Work, assignment, and authority scope; none proves the others |
| `C-Evidence-Reconcile-Internal`, candidate account | eight internal cases support an account in which the versioned provisional edition, uncertainty, and earlier integration use remain traceable through reconciliation to later signed evidence before closure | retained as a candidate account; `A.3.1` identification remains open |
| `C-Evidence-Reconcile-Supplier`, candidate account | four supplier-originated cases and one held-out supplier case support a signed-evidence branch | retained as a candidate account; `A.3.1` identification remains open |
| `C-AI-Trace-Review`, candidate account | the account specifies a trace-suggestion contribution; `TraceReviewer-17` performs the accept/reject Work under `ASG-TraceReview-17` and `PERM-TraceAcceptReject-17`, while the AI provider holds neither | retained as a human-governed candidate account |

The `provider-default AI proposal` is outside A.3.1.QM's present qualification subjects because no identified Method or candidate Method account has been supplied for it. Independently, implementing the proposal would disclose confidential geometry to the AI provider, and the proposal names no admitted human decision performer, covering assignment, or permission/authority relation. Those failures would block this use even if a candidate account were supplied.

Local schema correspondence `A-17` maps signed or explicitly provisional pinout-version fields to the integration bundle and preserves the exact edition and uncertainty used. Five stored bundles support that mapping for the named schema editions. The mapping preserves the provisional basis after later signed evidence becomes the safety-closure basis. This is a local connection result, not whole compatibility.

Two honest stops are now available. A project needing only hardware verification can stop with the qualified `M-HW-Verify`; no architecture comparison is required. A project investigating supplier reconciliation can stop with the retained `C-Evidence-Reconcile-Supplier` account and its open `A.3.1` question. EC-417 continues to C.32.MWA.PP only because the combined safety allocation, board timing, evidence routing, and recovery burden differ among whole alternatives.

### A.3.1.QM:6 - Bias-Annotation

| Recurring bias | Likely drift | Repair |
| --- | --- | --- |
| fit-score bias | Unlike contribution, capability, authority, evidence, and burden claims collapse into one number. | Return the decision-changing conditions and truthful branch instead of an opaque total. |
| candidate-upgrade bias | “Qualified candidate” is read as identified Method. | Repeat the account status in the verdict and state the open `A.3.1` condition. |
| compatibility bias | One feasible handoff or schema mapping becomes whole fit. | Call it a bounded local connection and route combined questions to C.32.MWA.PP. |
| decomposition bias | Each support System, role, or evidence item is evaluated as a Method candidate. | Accept only identified Methods and candidate Method accounts as qualification subjects. |

### A.3.1.QM:7 - Conformance Checklist

- [ ] Every subject is an identified Method or a candidate Method account and keeps that status.
- [ ] The qualification names one receiving use, scope, situation, window, and consuming decision.
- [ ] Contribution, inputs/results, applicability, attributable burden, capability, support, authority/access, evidence, and source limits are checked as applicable.
- [ ] No subject receives credit for another Method or whole arrangement's result.
- [ ] Local connection claims are independently testable and bounded.
- [ ] A candidate-account verdict preserves unresolved `A.3.1` identification conditions.
- [ ] Whole allocation, synchronization, composition, provider, and architecture questions remain explicit rather than hidden in individual verdicts.
- [ ] The result states whether to stop, reject, retain, or enter C.32.MWA.PP.

### A.3.1.QM:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| “This account fits, so it is a Method.” | Retain or exclude the account and send identity to `A.3.1`. |
| “All individual Methods pass, so the architecture is compatible.” | State the unresolved combined structure and use C.32.MWA.PP only when it changes the decision. |
| “The adapter works, so integration is solved.” | Bound the adapter-feasibility result; compare placement, versioning, responsibility, and failure in C.32.MWA.PP. |
| “Use the same checklist for every subject.” | Ask only applicable questions but preserve the common result positions needed by the decision. |
| “More evidence is always safer.” | Select evidence by consequence and claim; stop when the bounded decision can be made honestly. |

### A.3.1.QM:9 - Consequences

Weak subjects fail early, promising accounts remain usable without ontological promotion, and local handoffs become inspectable. Architecture comparison is smaller because it receives only retained subjects and unresolved combined questions.

The cost is refusal to publish one convenient compatibility score. A project may receive several qualified individual results and still have no acceptable synthesis.

### A.3.1.QM:10 - Rationale

Individual suitability and whole architecture answer different questions. A Method can be usable alone yet overload a shared Agent when combined with others. A candidate account can be useful evidence for design while still failing Method identification. Keeping the individual and architecture results separate protects both cheap stops and escalation when combined questions remain.

### A.3.1.QM:11 - SoTA-Echoing

| Source | Retained contribution | Use boundary |
| --- | --- | --- |
| Henderson-Sellers and Ralyté, [Situational Method Engineering review](https://opus.lib.uts.edu.au/handle/10453/13456) | Situational construction, selection, and adaptation questions. | Source-local fragment and process ontologies do not determine FPF subject status. |
| Daalhuizen and Cash, [Method Content Theory](https://doi.org/10.1016/j.destud.2021.101018) | Goal, procedure, rationale, framing, and mindset questions relevant to individual content and use. | These variables do not become universal qualification dimensions or Method parts. |
| Gericke, Eckert, and Stacey, [Elements of a design method](https://doi.org/10.1017/dsj.2022.23) | Intended use, scope, representation, procedure, tool, ecosystem, and adaptation conditions. | Conceptual elements guide questions; current project evidence supplies the verdict. |
| Current FPF `A.3.1`, `C.18`, and `G.5` | Method identity, candidate generation when needed, and bounded family/selector results. | A.3.1.QM adds status-preserving individual qualification and the local-connection boundary. |

Reopen when a current source or use shows that an individual question cannot be judged without a named whole structure, or when a repeated C.32.MWA.PP finding can be prevented by one affordable individual check.

### A.3.1.QM:12 - Relations

- C.39.RQ or an applicable domain result supplies situational criteria; A.3.1.DR or another lawful route supplies identified Methods/accounts and dependency slices. Neither named predecessor is compulsory when equivalent content exists.
- `A.3.1` alone governs Method identification. A.3.1.QM does not admit Methods.
- C.32.MWA.PP receives retained subjects only when combined Method, Work, allocation, support, description, subject, or cultural structures change the decision.
- B.1.5.CM resolves a proposed whole; A.3.1.QM qualification supplies no whole identity, compatibility, or `methodPartOf` fact.
- `C.11` or the applicable domain decision Method consumes the bounded individual results when a choice is live.

### A.3.1.QM:End
